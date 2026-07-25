"""Turn a world written in the jupytext "percent" format into a notebook.

A `# %%` line starts a code cell and `# %% [markdown]` a prose cell, which keeps a world file both a
plain importable Python script *and* a notebook. That is the whole trick: what runs in the browser and
what `build.py` imports are the same bytes.

`notebooks.py` is the one caller: at build time it runs every world through here, into the `.ipynb` the
site ships and the markdown of the tutorial pages.

Pure stdlib, like the rest of the package -- so it would also run *inside the browser*, under Pyodide,
turning a world fetched at runtime into a notebook live. Nothing asks it to today.
"""

from __future__ import annotations

import json
import re

CELL_MARKER = re.compile(r"^# %%(.*)$")


def parse_cells(source: str) -> list[tuple[str, str]]:
    """A world's source -> [(kind, text)], kind being 'code' or 'markdown'.

    Anything before the first marker is a code cell, so a world written as a plain script -- no markers
    at all -- still converts, to a single code cell."""
    cells: list[tuple[str, list[str]]] = []
    kind = "code"
    body: list[str] = []

    def flush() -> None:
        while body and not body[-1].strip():
            body.pop()
        if body:
            cells.append((kind, list(body)))
        body.clear()

    for line in source.splitlines():
        marker = CELL_MARKER.match(line)
        if marker:
            flush()
            kind = "markdown" if "[markdown]" in marker.group(1) else "code"
            continue
        body.append(line)
    flush()

    out = []
    for cell_kind, cell_lines in cells:
        if cell_kind == "markdown":
            # Strip the leading '# ' that makes the prose a comment in the .py.
            cell_lines = [line[2:] if line.startswith("# ") else line.lstrip("#") for line in cell_lines]
        out.append((cell_kind, "\n".join(cell_lines).strip("\n")))
    return out


def to_ipynb(name: str, cells: list[tuple[str, str]]) -> str:
    """The .ipynb JSON. Cell ids are derived from the world's name and the cell's position, so the same
    source always produces byte-identical output -- `notebooks.py --check` would be useless otherwise."""
    def cell(index: int, kind: str, source: str) -> dict:
        common = {
            "cell_type": kind,
            "id": f"{name}-{index}",
            "metadata": {},
            "source": source.splitlines(keepends=True),
        }
        if kind == "code":
            common |= {"execution_count": None, "outputs": []}
        return common

    notebook = {
        "cells": [cell(i, kind, source) for i, (kind, source) in enumerate(cells)],
        "metadata": {
            "kernelspec": {"display_name": "Python (Pyodide)", "language": "python", "name": "python"},
            "language_info": {"name": "python", "file_extension": ".py", "mimetype": "text/x-python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return json.dumps(notebook, indent=1, ensure_ascii=False) + "\n"
