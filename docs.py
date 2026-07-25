#!/usr/bin/env python3
"""Generate the MediaWiki docs from the Markdown docs.

    python docs.py            # regenerate docs/*.wiki from docs/*.md
    python docs.py --check    # fail if any .wiki is out of date (for CI / pre-commit)

**The Markdown is the source of truth. Never edit a .wiki by hand — it will be overwritten.**

This converts the small, closed subset of Markdown the docs actually use. Anything outside that subset
raises, loudly, naming the file and line: a silently mangled wiki page is far worse than a failed
build, and the fix is either to write the Markdown differently or to teach this script the construct.
"""

import argparse
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"

# Markdown links to another doc become wiki page links: [text](plot.md) -> [[plot|text]].
LOCAL_DOC = re.compile(r"^([\w.-]+)\.md(#.*)?$")


class UnsupportedMarkdown(Exception):
    """A construct this converter does not handle. Raised rather than guessed at."""


def _inline(text: str, where: str) -> str:
    """Convert inline markup.

    Code spans are stashed behind placeholders *before* any other markup is applied, then restored
    HTML-escaped at the end. That ordering matters twice over: markup inside a code span must not be
    interpreted (`**not bold**` stays literal), and markup *around* a code span must still be — a bold
    span like **`PlotStage`** opens and closes on opposite sides of the code, so converting code first
    and bold second would tear the `**` markers apart and pair them with the wrong partners."""
    spans: list[str] = []

    def stash(match: re.Match) -> str:
        spans.append(match.group(1))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)

    if "<" in text or ">" in text:
        # Raw HTML outside a code span. We will not pass it through blindly and we will not guess.
        raise UnsupportedMarkdown(f"{where}: raw HTML/angle bracket outside a code span: {text.strip()!r}")

    text = re.sub(r"\*\*(.+?)\*\*", r"'''\1'''", text)                 # bold (may wrap a code span)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"''\1''", text)       # italic
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: _link(m, spans), text)

    def restore(match: re.Match) -> str:
        return f"<code>{html.escape(spans[int(match.group(1))], quote=False)}</code>"

    return re.sub(r"\x00(\d+)\x00", restore, text)


def _plain(text: str, spans: list[str]) -> str:
    """A link's label with its code spans put back as plain text, so we can tell whether `[`iw`](iw.md)`
    is just naming its own target."""
    return re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)


def _link(match: re.Match, spans: list[str]) -> str:
    text, target = match.group(1), match.group(2)
    local = LOCAL_DOC.match(target)
    if local:
        page = local.group(1)
        return f"[[{page}]]" if _plain(text, spans) == page else f"[[{page}|{text}]]"
    if target.startswith("#"):
        return text  # an anchor within the page; MediaWiki numbers its own sections
    return f"[{target} {text}]"


def _table(rows: list[str], where: str) -> list[str]:
    """A pipe table -> a wikitable. The second row of a Markdown table is the |---|---| separator."""
    cells = [[c.strip() for c in row.strip().strip("|").split("|")] for row in rows]
    header, body = cells[0], cells[2:]
    out = ['{| class="wikitable"']
    if any(header):
        out.append("! " + " !! ".join(_inline(c, where) for c in header))
    for row in body:
        out.append("|-")
        out.append("| " + " || ".join(_inline(c, where) for c in row))
    out.append("|}")
    return out


def convert(markdown: str, source: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        where = f"{source}:{index + 1}"

        if not line.strip():
            out.append("")
            index += 1

        elif line.startswith("```"):                                   # fenced code
            language = line[3:].strip()
            close = index + 1
            while close < len(lines) and not lines[close].startswith("```"):
                close += 1
            if close >= len(lines):
                raise UnsupportedMarkdown(f"{where}: unclosed code fence")
            body = "\n".join(lines[index + 1:close])
            if language:
                out.append(f'<syntaxhighlight lang="{language}">\n{body}\n</syntaxhighlight>')
            else:
                out.append(f"<pre>\n{body}\n</pre>")                    # diagrams, shell output
            index = close + 1

        elif re.match(r"^#{1,6} ", line):                               # heading
            level = len(line) - len(line.lstrip("#"))
            text = _inline(line[level:].strip(), where)
            # An H1 is the page title in MediaWiki; the page name supplies it, so it is dropped.
            if level > 1:
                out.append(f"{'=' * level} {text} {'=' * level}")
            index += 1

        elif re.match(r"^-{3,}\s*$", line):                             # horizontal rule
            out.append("----")
            index += 1

        elif line.startswith("|"):                                      # table
            close = index
            while close < len(lines) and lines[close].startswith("|"):
                close += 1
            out.extend(_table(lines[index:close], where))
            index = close

        elif re.match(r"^[-*] ", line):                                 # bullet (wrapped lines joined)
            close = index + 1
            while close < len(lines) and lines[close].startswith("  ") and lines[close].strip():
                close += 1
            text = " ".join(l.strip() for l in lines[index:close])[2:]
            out.append("* " + _inline(text, where))
            index = close

        elif re.match(r"^\s*\d+\. ", line) or line.startswith(">") or line.startswith("  "):
            raise UnsupportedMarkdown(
                f"{where}: numbered lists, blockquotes and indented blocks are not supported: "
                f"{line.strip()!r}"
            )

        else:                                                           # paragraph (wrapped lines joined)
            close = index
            while (close < len(lines) and lines[close].strip()
                   and not re.match(r"^(#{1,6} |[-*] |\||```|-{3,}\s*$)", lines[close])):
                close += 1
            out.append(_inline(" ".join(l.strip() for l in lines[index:close]), where))
            index = close

    text = "\n".join(out).strip() + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if any .wiki is out of date")
    args = parser.parse_args()

    stale = []
    for source in sorted(DOCS.glob("*.md")):
        destination = source.with_suffix(".wiki")
        generated = convert(source.read_text(), source.name)
        current = destination.read_text() if destination.exists() else None
        if args.check:
            if current != generated:
                stale.append(destination.relative_to(ROOT))
            continue
        destination.write_text(generated)
        print(f"  {source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}"
              f"{'' if current == generated else '  (updated)'}")

    if stale:
        print("Out of date -- run `python docs.py`:", file=sys.stderr)
        for path in stale:
            print(f"  {path}", file=sys.stderr)
        return 1
    if args.check:
        print("  all .wiki files are up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
