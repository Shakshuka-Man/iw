# The worlds

A world is a folder with a `world.py` in it that defines a module-level `world`. Folders can nest, and
the three tutorials are grouped under `tutorial_iw/`, `tutorial_plot/` and `tutorial_advanced/`.

A world's name is its folder's path, with the separators turned into underscores. So
`tutorial_iw/5_triggers/` is the world `tutorial_iw_5_triggers`. That is what it builds to, and what you
type to build it:

```bash
python build.py --list                     # what's here, and where each one lives
python build.py tutorial_iw_5_triggers     # build one -> out/tutorial_iw_5_triggers.json
python build.py                            # build them all
```

The folder is short and the name is long on purpose. You read the folder in a tree that already tells you
where you are, but the built `.json` lands somewhere flat that does not -- `out/` when you build locally, or
your browser's Downloads folder when you save one from the site -- so its long name is the only thing
telling it apart from every other world's.

## The folder is the world's workspace

The site's file browser is this exact tree, with `world.ipynb` where the repo has `world.py`. That is why
a world is a folder and not a loose file: the JSON a reader generates is written next to the notebook that
generated it. Run a world three times with three different settings, and the three JSONs sit together in
that world's folder instead of in one undifferentiated heap.

Every `world.py` is also a notebook. The `# %%` markers in it are cell boundaries (the jupytext
"percent" format), which `notebooks.py` turns into a `.ipynb` for the browser and into the tutorial pages,
while the file itself stays a plain, importable Python script. There is one source, so the docs cannot
drift from the code.

## When a world outgrows one file

Make its folder a package: add an `__init__.py`, and have `world.py` import the folder by name.

```python
from starlit_frontiers import combat, navigation, ships
```

By name, though, never `from . import`. `world.py` is *also the notebook*, and when it is run as cells it
is top-level code with no package to be relative to, so a relative import there raises.

This has a consequence. A world with a package must have a folder name that is a Python identifier
(`starlit_frontiers`, not `5_triggers`), because that name is an import. A single-file world is under no
such obligation, which is why the tutorials can lead with a digit.

## The tutorials

Three tutorial tracks, each adding one idea to the last. Read them in order -- every world is a notebook
you can run in your browser with nothing installed, and each track's README is its contents page:

- [**Tutorial 1 — `iw`: the data model**](tutorial_iw/README.md) — the basic elements of a world.
- [**Tutorial 2 — advanced: why not just use the editor**](tutorial_advanced/README.md) — automation and
  programatically generating worlds.
- [**Tutorial 3 — `plot`: the plot engine**](tutorial_plot/README.md) — a tool for implementing plotlines
  and character advancement.

Each track also reads straight through as a [tutorial page](../docs/) with nothing to run.

## Writing your own

Make `worlds/<your-world>/world.py`. Define a module-level `world`, and end by saving it as
`<your-world>.json`, named after the world and not its folder, so no two worlds overwrite each other's
output. `build.py` runs it with the working directory set to `out/`, so that save *is* the build.

A world may split itself across several files in its own folder and import them by plain name. That
folder is on the path, here and in the browser alike, which is how you keep a big data table out of the
world itself.

The repository's top-level README has the skeleton and the three things that catch people out.
