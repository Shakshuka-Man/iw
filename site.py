#!/usr/bin/env python3
"""Build the JupyterLite site -- the worlds, running in a browser, with nothing installed.

    python site.py            # build the site into _site/
    python site.py --serve    # ...then serve it at http://localhost:8000 to try it

Needs the site tooling, which is not a dependency of `iw` itself:

    pip install -r requirements-site.txt

`iw` has no dependencies and no C extensions, which is the whole reason this works: Pyodide runs the
library unmodified. So there is no wheel to build and nothing to install in the browser -- we simply
copy the package into the site's contents, at the root of the file browser (`/drive/iw/`), beside the
worlds that import it.

**The file browser is the repo.** Same tree, `world.ipynb` where the repo has `world.py`:

    iw/                                          the library
    docs/                                        the references, and the data dictionaries
    worlds/README.md                             what a world is
    worlds/tutorial_iw/README.md                 the track's contents page
    worlds/tutorial_iw/1_simple_world/           a world -- and, on the site, its workspace:
        world.ipynb                                  the notebook
        bones_in_the_ocean.json                      ...and whatever the reader builds with it
    worlds/tutorial_advanced/3_classes_and_files/
        world.ipynb                                  a world of several files: the notebook,
        wrecks.py, sanity_bands.py, *.csv            ...and the modules and data it reads
    welcome.md                                   the landing page

**A world is a folder** because that folder is where the reader's own output lands. The kernel's working
directory is the notebook's folder, so a world they run three variations of leaves three JSONs together,
in that world's folder, rather than three files in a heap at the root.

It is also why the folder must arrive *whole*: a notebook that does `import stations` and finds no
`stations.py` beside it is not a notebook, it is a traceback. Everything in a world's folder ships, minus
the `world.py` that became the notebook.

That working directory is on `sys.path` for free, which is most of what the notebooks need. The rest comes
from `jupyter-lite.json`, which passes `env: {PYTHONPATH: ...}` through JupyterLite's `loadPyodideOptions`
into Pyodide (CPython reads PYTHONPATH at startup). See `required_pythonpath` for what has to be in it and
why -- and note it is *derived* from the worlds, so a new package world in a new place fails the build
rather than shipping broken.

Two more files shape what a visitor sees, and `jupyter lite build` picks both up from this directory by
name -- neither is mentioned below because neither has to be:

    workspaces/default.jupyterlab-workspace   the layout the lab opens with: `welcome.md`, rendered,
                                              and the file browser. Without it you land on a bare
                                              launcher, which explains nothing to anybody.
    overrides.json                            JupyterLab settings. It makes a `.json` open in the text
                                              editor rather than the collapsible tree widget -- a world
                                              is something you copy out whole, not something you browse.

Both are defaults, not decrees: the lab saves the visitor's own layout over the workspace as soon as
they move a tab, and a right-click still offers any other viewer.
"""

import argparse
import functools
import http.server
import json
import pathlib
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import discover  # noqa: E402  -- one definition of what a world is, and where it lives

ROOT = pathlib.Path(__file__).resolve().parent
WORLDS = ROOT / "worlds"
DOCS = ROOT / "docs"
NOTEBOOKS = ROOT / "out" / "notebooks"
CONTENTS = ROOT / "out" / "contents"
SITE = ROOT / "_site"
CACHE = ROOT / ".jupyterlite.doit.db"   # jupyter lite's task cache; see build()

# The docs go on the drive in their own `docs/` folder rather than flattened into the root, so that the
# links *between* them -- `plot.md` from `iw.md`, `../worlds/README.md` from `plot.md` -- are the same
# link here and on GitHub. One set of docs, correct in both places, and `check_links` proves it.


def assemble() -> None:
    """The contents of the site's file browser: the notebooks, and everything they read."""
    subprocess.run([sys.executable, "notebooks.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "reference.py"], cwd=ROOT, check=True)

    if CONTENTS.exists():
        shutil.rmtree(CONTENTS)
    CONTENTS.mkdir(parents=True)

    shutil.copytree(ROOT / "iw", CONTENTS / "iw", ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))

    # Each notebook lands in its world's own folder, so the file browser is the `worlds/` tree.
    for notebook in sorted(NOTEBOOKS.rglob("*.ipynb")):
        destination = CONTENTS / notebook.relative_to(NOTEBOOKS)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(notebook, destination)

    # ...and beside it, everything else in that world's folder: the modules a multi-file world imports,
    # the data files it reads, the README it came with. A world's folder is the world, and it has to
    # arrive whole -- a notebook that does `import stations` and finds no stations.py is not a notebook,
    # it is a traceback.
    #
    # Not world.py, though: the notebook beside it was generated from it, and shipping both would put the
    # same world in the file browser twice, in two formats, one of which nobody can run.
    for name, world in sorted(discover().items()):
        destination = CONTENTS / world.relative_to(ROOT)
        shutil.copytree(
            world, destination, dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__", ".DS_Store", "world.py"),
        )
        alongside = sorted(p for p in destination.rglob("*") if p.is_file() and p.suffix != ".ipynb")
        if alongside:
            print(f"  world:    {world.relative_to(WORLDS)}/  (+{len(alongside)} files beside the notebook)")

    # A README per tutorial track -- the contents page for that track, in that track's folder -- plus the
    # one above them that says what a world *is*. A reader who is browsing rather than following a link
    # should find a way in wherever they happen to land.
    for readme in [WORLDS / "README.md", *sorted(WORLDS.glob("*/README.md"))]:
        destination = CONTENTS / readme.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(readme, destination)

    # The docs: the two prose references, the two data dictionaries generated from the library a moment
    # ago, and the tutorial pages for reading straight through rather than running.
    (CONTENTS / "docs").mkdir()
    for page in sorted(DOCS.glob("*.md")):
        shutil.copy2(page, CONTENTS / "docs" / page.name)

    # The landing page. `workspaces/default.jupyterlab-workspace` is what opens it -- it has to be on
    # the drive under this name for that layout to find anything to restore.
    shutil.copy2(ROOT / "welcome.md", CONTENTS / "welcome.md")
    check_links()

    print(f"  contents: {len(list(CONTENTS.rglob('*.ipynb')))} notebooks + welcome.md + the iw package")


def check_links() -> None:
    """Every link in every markdown file on the drive points at something that is on the drive.

    The pages link to each other and straight into the notebooks, and JupyterLab opens them in the app
    rather than navigating away -- which is lovely right up until one of them is wrong. A link to a world
    that has been renamed does not 404 and does not look broken. It does *nothing* when a reader clicks
    it, which is the worst of the available failures. Renaming a tutorial folder is what this catches.

    Relative to the page that holds it, not to the drive root -- `../worlds/README.md` in `docs/plot.md`
    is the same link on GitHub and here, and that is the point of shipping the docs in a `docs/` folder
    rather than flattening them."""
    dead, checked = [], 0
    for page in sorted(CONTENTS.rglob("*.md")):
        for target in re.findall(r"\]\(([^)]+)\)", page.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            checked += 1
            if not (page.parent / target.split("#")[0]).exists():
                dead.append(f"{page.relative_to(CONTENTS)}  ->  {target}")

    if dead:
        raise SystemExit(
            "Markdown on the drive links at files that are not on the drive:\n"
            + "\n".join(f"  {entry}" for entry in dead)
            + "\n\nA reader clicking one of these gets silence, not an error. Fix the link, or ship the"
              "\nfile. Refusing to build a site whose contents page does nothing when you click it."
        )
    print(f"  links:    {checked} internal links across "
          f"{len(list(CONTENTS.rglob('*.md')))} pages, all live")


def build() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)

    # `jupyter lite build` is a doit pipeline, and it caches which tasks it has already run in this file.
    # We have just deleted its entire output, so every one of those "already done" answers is a lie --
    # and it lies *quietly*: the task that merges our jupyter-lite.json into the site gets skipped, the
    # build succeeds, and the settings we put there are simply not in the site. PYTHONPATH went missing
    # exactly that way, and the only symptom was that notebooks inside a folder stopped running.
    #
    # The cache saves a couple of seconds on a build that takes thirty. It is not worth a config that
    # depends on what the last build happened to do.
    CACHE.unlink(missing_ok=True)

    subprocess.run(
        ["jupyter", "lite", "build", "--contents", str(CONTENTS), "--output-dir", str(SITE)],
        cwd=ROOT,
        check=True,
    )
    check_config()
    print(f"  -> {SITE.relative_to(ROOT)}")


def required_pythonpath() -> str:
    """What the kernel's path has to contain for the notebooks to import anything.

    The kernel's working directory is the notebook's own folder, and that is on the path for free. Two
    kinds of thing are not, and each needs an entry:

        /drive          `iw` itself, which every notebook imports on its first line.
        /drive/worlds   the folder *above* a package world, so `from starlit_frontiers import ...`
                        resolves -- a package is found by its folder's name, from one level up.

    Derived rather than written down, so that adding a package world somewhere new fails the build below
    instead of shipping a site where that one world's notebook cannot import itself."""
    entries = ["/drive"]
    for world in discover().values():
        if not (world / "__init__.py").exists():
            continue
        above = f"/drive/{world.parent.relative_to(ROOT).as_posix()}"
        if above not in entries:
            entries.append(above)
    return ":".join(entries)


def check_config() -> None:
    """The settings we asked for are actually in the site we just built.

    Cheap, and it earns its keep: a JupyterLite build drops settings it does not apply without failing,
    and the site still looks perfectly healthy right up until a notebook in a folder cannot `import iw`."""
    config = json.loads((SITE / "jupyter-lite.json").read_text())["jupyter-config-data"]
    kernel = config.get("litePluginSettings", {}).get("@jupyterlite/pyodide-kernel-extension:kernel", {})
    built = kernel.get("loadPyodideOptions", {}).get("env", {}).get("PYTHONPATH")
    wanted = required_pythonpath()
    if built != wanted:
        raise SystemExit(
            f"The built site has PYTHONPATH={built!r}, and the worlds in this repo need {wanted!r}.\n"
            "Set it in jupyter-lite.json. Without it the kernel's path is just the notebook's own folder,\n"
            "and a notebook under worlds/ dies on its first import. Refusing to ship that."
        )
    if not (SITE / "api" / "workspaces" / "all.json").exists():
        raise SystemExit("The built site has no default workspace -- visitors would land on a bare launcher.")


def serve(port: int) -> None:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
    print(f"\n  http://localhost:{port}/lab/index.html\n\n  Ctrl-C to stop.")
    http.server.ThreadingHTTPServer(("", port), handler).serve_forever()


def clean() -> None:
    """Delete everything this repo generates, so the next build starts from nothing.

    Every path here is an artifact -- `out/` and `_site/` are gitignored, and the .db is a cache. Nothing
    you wrote lives in any of them.

    This does *not* touch the copy of the site living in your browser. It cannot: that is in the browser's
    own storage, keyed to the origin you served from, and it outlives any rebuild. To clear that, open the
    site and use **Help -> Clear Browser Data**."""
    removed = []
    for path in [CONTENTS, NOTEBOOKS, SITE, CACHE, *ROOT.rglob("__pycache__")]:
        if SITE in path.parents:
            continue                       # already going, with the rest of _site/
        if path.is_dir():
            shutil.rmtree(path)
            removed.append(f"{path.relative_to(ROOT)}/")
        elif path.exists():
            path.unlink()
            removed.append(str(path.relative_to(ROOT)))

    # The built worlds, but not the directory: `out/` is where a world writes itself, and build.py
    # expects to be able to chdir into it.
    for world in sorted(ROOT.glob("out/*.json")):
        world.unlink()
        removed.append(str(world.relative_to(ROOT)))

    for path in removed:
        print(f"  removed  {path}")
    print(f"\n  {len(removed)} artifacts gone. `python site.py` rebuilds all of it.")
    print("  Leftovers in the *browser* are separate -- open the site and use Help -> Clear Browser Data.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--serve", action="store_true", help="serve the site after building it")
    parser.add_argument("--clean", action="store_true", help="delete everything generated, and exit")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if args.clean:
        clean()
        return 0

    assemble()
    build()
    if args.serve:
        serve(args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
