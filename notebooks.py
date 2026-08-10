#!/usr/bin/env python3
"""Generate the notebooks and the tutorial docs from the worlds.

    python notebooks.py           # regenerate out/notebooks/*.ipynb and docs/tutorial-*.md
    python notebooks.py --check   # fail if any generated file is out of date (for CI)

**A world's `world.py` is the source of truth.** It is written once, in the jupytext "percent" format --
`# %%` starts a code cell, `# %% [markdown]` a prose cell -- and that one file is:

    worlds/tutorial_iw/5_triggers/world.py
        |-- notebooks.py --> out/notebooks/worlds/tutorial_iw/5_triggers/world.ipynb  (JupyterLite)
        |               `--> docs/tutorial-*.md                  the tutorial page (-> .wiki)
        `-- build.py     --> out/tutorial_iw_5_triggers.json     the world itself

The notebook stays in the world's own folder, so the site's file browser is this `worlds/` tree, folder
for folder. Only the world *JSON* takes the long flattened name -- it is the one thing that leaves.

The point of the percent format is that the file stays a plain, importable Python script -- so the
thing the reader runs in the browser and the thing `build.py` imports are the same bytes, and neither
can drift from the docs.

Notebooks are generated for every world; the tutorial pages are built from the `tutorial_*` worlds
only, in the order they are meant to be read.
"""

import argparse
import os
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"
NOTEBOOKS = ROOT / "out" / "notebooks"

sys.path.insert(0, str(ROOT))
from iw.notebook import parse_cells, to_ipynb  # noqa: E402  -- the same converter the browser runs
from build import discover  # noqa: E402  -- one definition of what a world is, and where it lives

WORLDS_BY_NAME = discover()


def source(name: str) -> str:
    """A world's source: the world.py in its folder."""
    return (WORLDS_BY_NAME[name] / "world.py").read_text()


def notebook(name: str) -> pathlib.Path:
    """Where a world's notebook goes: its own folder, as `world.ipynb`.

    The same path the repo has, with `world.ipynb` for `world.py`. So the site's file browser *is* this
    tree, and a world's folder is that world's workspace on the site: the notebook, and every JSON anybody
    generates from it, in one place instead of a heap at the root."""
    return NOTEBOOKS / WORLDS_BY_NAME[name].relative_to(ROOT) / "world.ipynb"

# The three tutorial pages, and the worlds each is built from, in reading order. A tutorial world that is
# in none of these lists is an error -- silently leaving a world out of the docs is exactly the drift
# this script exists to prevent.
PAGES = [
    {
        "path": DOCS / "tutorial-1-iw.md",
        "title": "Tutorial 1 — `iw`: the data model",
        "intro": (
            "This is the first of three tutorials. It covers `iw`, the layer that mirrors the engine's "
            "world format: the world itself, the cast, instruction blocks, keyword blocks, tracked "
            "items, triggers. All five build one world — a lighthouse on an uninhabited rock in the "
            "Outer Hebrides, an eighteen-month posting, and a keeper who will not be able to tell "
            "whether the island is haunted or they are simply coming apart. "
            "[Tutorial 2](tutorial-2-advanced.md) is what this is *worth* — the case for doing any of "
            "this in Python rather than in the engine's own editor. [Tutorial 3](tutorial-3-plot.md) "
            "covers `plot`, a compiler for story structure built on top of both.\n"
            "\n"
            "Five worlds, each adding one idea to the last. **Every one of them is a notebook you can "
            "run in your browser** — nothing to install. This page is the same material as a single "
            "read-through.\n"
            "\n"
            "Each notebook has the same three parts: an **input** (which world to start from), a "
            "**transformation** (the lesson), and an **output** (save the result). Leave the input "
            "alone to follow along, or point it at a world of your own and the lesson is applied to "
            "*that* instead."
        ),
        "worlds": [
            "tutorial_iw_1_simple_world",
            "tutorial_iw_2_instruction_blocks",
            "tutorial_iw_3_characters",
            "tutorial_iw_4_tracked_items",
            "tutorial_iw_5_triggers",
        ],
    },
    {
        "path": DOCS / "tutorial-2-advanced.md",
        "title": "Tutorial 2 — advanced: why not just use the editor",
        "intro": (
            "This is the second of three tutorials, and it assumes [tutorial 1](tutorial-1-iw.md).\n"
            "\n"
            "Infinite Worlds ships a perfectly good editor. It has a box for every field in the world "
            "format, it validates as you type, and it does not ask you to know what a dataclass is. "
            "**For a small world it is better than this library**, and you should use it.\n"
            "\n"
            "These four worlds are the other case. First the **tools**: `iw.tools`, the two helpers that "
            "read and write a tracked item without ever typing its id twice. **Generate**: a spreadsheet "
            "of shipwrecks becomes a lore book, and a spreadsheet of sanity bands becomes the triggers the "
            "basic track wrote by hand. **Structure**: as the world grows, give the rows a dataclass and "
            "split each subsystem into its own file. And finally, **combining everything**: nothing new, "
            "just every idea so far combined into one complete world.\n"
            "\n"
            "The question underneath every one of them is the same: *what happens when there are four "
            "hundred of them?*"
        ),
        "worlds": [
            "tutorial_advanced_1_helpers",
            "tutorial_advanced_2_generating_from_data",
            "tutorial_advanced_3_classes_and_files",
            "tutorial_advanced_4_combining_everything",
        ],
    },
    {
        "path": DOCS / "tutorial-3-plot.md",
        "title": "Tutorial 3 — `plot`: the plot engine",
        "intro": (
            "This is the third of three tutorials, and it assumes [tutorial 1](tutorial-1-iw.md) and "
            "[tutorial 2](tutorial-2-advanced.md).\n"
            "\n"
            "`plot` is a compiler. You describe a story as **stages** and the **transitions** between "
            "them; it emits the hidden tracked items and the trigger events that make the engine run "
            "it — a stage tracker, a trigger per stage, a trigger per transition, a per-turn gate so "
            "two transitions cannot fire at once. Tutorial 2 builds that bookkeeping by hand, to show "
            "there is nothing magic in it; the other worlds let the compiler write it.\n"
            "\n"
            "Six worlds, in increasing order of what they ask of the compiler."
        ),
        "worlds": [
            "tutorial_plot_1_simple",
            "tutorial_plot_2_behind_the_scenes",
            "tutorial_plot_3_branching",
            "tutorial_plot_4_characters",
            "tutorial_plot_5_multiple_plotlines",
            "tutorial_plot_6_hub_and_spoke",
        ],
    },
]



def demote(markdown: str) -> str:
    """Push every heading down one level: a notebook's H1 title becomes a section of the tutorial page.
    Headings inside a fenced block are left alone -- a '#' there is a Python comment, not a heading."""
    out, fenced = [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def reroot_links(markdown: str, world_dir: pathlib.Path) -> str:
    """Rewrite relative links in a world's markdown cell so they resolve from the tutorial page in `docs/`
    rather than from the world's own folder, where the notebook lives.

    A world links to its neighbours in the `worlds/` tree by paths relative to its own folder -- right for
    the notebook, wrong once the same cell is embedded in a `docs/` page. So a link the notebook writes as
    `../../tutorial_plot/README.md` becomes `../worlds/tutorial_plot/README.md` here. Absolute (`http`) and
    pure-anchor (`#...`) links are left alone; a `#fragment` on a relative link is preserved. Links inside a
    fenced block are code, not links, so they are skipped."""
    def rewrite(match: re.Match) -> str:
        text, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        path, sep, fragment = url.partition("#")
        target = os.path.normpath(world_dir / path)
        return f"[{text}]({os.path.relpath(target, DOCS)}{sep}{fragment})"

    out, fenced = [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced:
            line = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", rewrite, line)
        out.append(line)
    return "\n".join(out)


def to_markdown(page: dict) -> str:
    """One tutorial page: an intro, a table of its worlds, then every world's cells in order -- prose as
    prose, code in fences."""
    parts = [f"# {page['title']}", "", page["intro"], ""]

    parts.append("| | notebook | the idea |")
    parts.append("|---|---|---|")
    for number, name in enumerate(page["worlds"], start=1):
        cells = parse_cells(source(name))
        heading = next(line for _, cell in cells for line in cell.splitlines() if line.startswith("# "))
        idea = heading.split("—", 1)[-1].strip() if "—" in heading else heading[2:].strip()
        parts.append(f"| {number} | `{name}` | {idea} |")
    parts.append("")

    for name in page["worlds"]:
        for kind, cell in parse_cells(source(name)):
            if kind == "markdown":
                parts.append(demote(reroot_links(cell, WORLDS_BY_NAME[name])))
            else:
                parts.append(f"```python\n{cell}\n```")
            parts.append("")

    return re.sub(r"\n{3,}", "\n\n", "\n".join(parts)).strip() + "\n"


def worlds() -> list[str]:
    return sorted(WORLDS_BY_NAME)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if any generated file is out of date")
    args = parser.parse_args()

    documented = {name for page in PAGES for name in page["worlds"]}
    undocumented = [n for n in worlds() if n.startswith("tutorial_") and n not in documented]
    if undocumented:
        print(f"Tutorial worlds missing from a page in notebooks.py: {', '.join(undocumented)}", file=sys.stderr)
        return 1

    # Regenerate the notebooks from empty. Rename or regroup a world and its old notebook is still
    # sitting there, and site.py would ship it -- a stale duplicate of a world, under a name nothing
    # builds any more. The directory is a build artifact; there is nothing in it worth keeping.
    if not args.check:
        shutil.rmtree(NOTEBOOKS, ignore_errors=True)

    # The tutorial pages are committed, so they can go stale in a way review would miss -- those are what
    # `--check` guards. The notebooks are build artifacts under out/, regenerated every time and never
    # committed; checking them would only ever fail on a fresh clone, where they do not exist yet.
    pages = {page["path"]: to_markdown(page) for page in PAGES}
    notebooks = {
        notebook(name): to_ipynb(name, parse_cells(source(name)))
        for name in worlds()
    }
    generated = pages if args.check else notebooks | pages

    stale = []
    for destination, content in generated.items():
        current = destination.read_text() if destination.exists() else None
        if args.check:
            if current != content:
                stale.append(destination.relative_to(ROOT))
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)
        print(f"  {destination.relative_to(ROOT)}{'' if current == content else '  (updated)'}")

    if stale:
        print("Out of date -- run `python notebooks.py`:", file=sys.stderr)
        for path in stale:
            print(f"  {path}", file=sys.stderr)
        return 1
    if args.check:
        print("  tutorial pages are up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
