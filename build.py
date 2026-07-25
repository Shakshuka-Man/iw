#!/usr/bin/env python3
"""Build worlds to JSON.

    python build.py                 # build every world into out/
    python build.py simple          # build one
    python build.py simple endings  # build several
    python build.py --list          # list the worlds in this repo
    python build.py --out dist      # write somewhere other than out/

**A world is a folder with a `world.py` in it** that defines a module-level `world` (an `iw.World`). The
folder is the world: its source, and -- on the site -- the notebook and every JSON anybody generates from
it. Folders can nest as deep as you like; the two tutorials are grouped under `worlds/tutorial_iw/` and
`worlds/tutorial_plot/`.

A world's **name** is its folder's path under `worlds/`, with the separators turned into underscores:
`worlds/tutorial_iw/5_triggers/` is `tutorial_iw_5_triggers`. That is what you type to build it. It is
also the name most worlds save their JSON under (`out/tutorial_iw_5_triggers.json`) -- a saved file wants
to be self-describing, because it ends up in a downloads folder with no tree around it, and the long name
does that job. But a world whose *title* already says what it is can simply save under that
(`bones_in_the_ocean.json`); the only rule is that no two worlds write the same file into `out/`.

The site's file browser is this same tree, with `world.ipynb` where this has `world.py`. That is why the
world is a folder rather than a loose file: the JSON a reader generates lands next to the notebook that
made it, and if they keep three versions, all three sit in that world's folder instead of in one heap.

A world too big for one file makes its own folder a **package**: add an `__init__.py`, and `world.py`
imports it by the folder's name -- `from starlit_frontiers import ...`. Absolutely, by name, never with a
relative `from . import`: `world.py` is also the notebook, and run as cells it is top-level code with no
package to be relative to.

Warnings raised while a world is built (unreachable stages, contested instruction blocks, and so on)
are printed under that world's name. They do not stop the build -- errors do.
"""

import argparse
import contextlib
import importlib.util
import pathlib
import sys
import warnings

ROOT = pathlib.Path(__file__).resolve().parent
WORLDS_DIR = ROOT / "worlds"

# So `import iw` resolves to this repo's package without needing an install.
sys.path.insert(0, str(ROOT))
import iw  # noqa: E402


def discover() -> dict[str, pathlib.Path]:
    """Every buildable world: name -> its folder. The one definition of what a world is; notebooks.py and
    site.py import this rather than glob for themselves."""
    return {
        "_".join(path.parent.relative_to(WORLDS_DIR).parts): path.parent
        for path in sorted(WORLDS_DIR.rglob("world.py"))
    }


def load(folder: pathlib.Path):
    """Import a world's world.py.

    Two directories go on the path, and they are the two the browser gives a notebook for free:

        the world's own folder    -- the kernel's working directory. Anything a world keeps beside its
                                     world.py, it can import by plain name.
        the folder above it       -- so a world whose own folder is a package can import it by that
                                     folder's name: `from starlit_frontiers import ...`.

    Which is the whole trick. `world.py` runs as a script here and as cells there, and in both places the
    same imports resolve, because in both places it is sitting in the same two directories.

    A world's sibling modules are then dropped from the import cache on the way out, and that is not
    housekeeping -- it is the difference between right and wrong. Two worlds may each keep a `wrecks.py`
    beside their `world.py`; they are different files and have nothing to do with each other. But
    `sys.modules` is keyed by the *name* `wrecks`, and it is global to this process. Leave the first
    world's module in there and the second world silently imports it -- and builds itself, without error,
    from the wrong ship list. In the browser this cannot happen (one notebook, one kernel), so it would
    be a bug that exists only in the build, only when you build more than one world at a time, and never
    where you are looking."""
    path = folder / "world.py"
    added = [str(folder), str(folder.parent)]
    sys.path[:0] = added
    cached = set(sys.modules)
    try:
        spec = importlib.util.spec_from_file_location(f"worlds.{folder.name}.world", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        for entry in added:
            sys.path.remove(entry)
        for name in set(sys.modules) - cached:
            origin = getattr(sys.modules[name], "__file__", None)
            if origin and pathlib.Path(origin).is_relative_to(folder):
                del sys.modules[name]


def build(name: str, world: pathlib.Path, out_dir: pathlib.Path) -> list[pathlib.Path]:
    """Build one world. Returns the JSON file(s) it wrote.

    The world writes its own JSON -- its last cell saves, exactly as it does when the same file is run as
    a notebook (`to_json` validates on the way out, so a world that does not hang together raises there
    rather than reaching disk). So we don't write anything here; we just run it with the working directory
    set to `out/`, and its own writes land where we want them. What you read in the file is what runs, in
    the browser and here alike.

    A world may name its output whatever suits it -- most save `<name>.json` and that is a good default,
    but a tutorial whose world is *called* "Bones in the Ocean" reads better saving `bones_in_the_ocean`
    than its own long folder-name. All we require here is that it writes *something*: a world that forgot
    its last cell saved nothing, and that is the mistake worth catching. The rule that no two worlds may
    write the *same* file -- which is what stops them clobbering each other in one flat `out/` -- is
    enforced across the whole build in `main`, because it is only knowable there.

    We detect what a world wrote by mtime: the files in `out/` that are new, or newer than before we ran
    it. In the browser none of this applies -- each world writes into its own folder, one kernel at a
    time -- so this is a build-time guard, for the one flat directory the CLI shares."""
    # Ids come from one seeded sequence, so without this a world's ids would depend on which worlds
    # were built before it in this process -- the same world would produce different JSON depending on
    # how it was invoked.
    iw.reset_ids()
    out_dir.mkdir(parents=True, exist_ok=True)
    source = (world / "world.py").relative_to(ROOT)

    before = {path: path.stat().st_mtime_ns for path in out_dir.glob("*.json")}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with contextlib.chdir(out_dir):
            module = load(world)

    for warning in caught:
        print(f"  warning: {warning.message}")

    if getattr(module, "world", None) is None:
        raise SystemExit(f"{source} does not define a module-level `world`.")

    written = sorted(
        path for path in out_dir.glob("*.json")
        if path not in before or path.stat().st_mtime_ns != before[path]
    )
    if not written:
        raise SystemExit(
            f"{source} saved no JSON. Its last cell must write the world to a file, e.g. "
            'pathlib.Path("my_world.json").write_text(world.to_json()).'
        )
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("worlds", nargs="*", help="worlds to build (default: all of them)")
    parser.add_argument("--list", action="store_true", help="list the worlds in this repo and exit")
    parser.add_argument("--out", default="out", type=pathlib.Path, help="output directory (default: out)")
    args = parser.parse_args()

    available = discover()
    if args.list:
        for name, world in available.items():
            print(f"{name:<30} {world.relative_to(ROOT)}")
        return 0

    selected = args.worlds or list(available)
    unknown = [name for name in selected if name not in available]
    if unknown:
        print(f"No such world: {', '.join(unknown)}", file=sys.stderr)
        print(f"Available: {', '.join(available)}", file=sys.stderr)
        return 1

    out_dir = args.out if args.out.is_absolute() else ROOT / args.out
    claimed: dict[str, str] = {}          # output filename -> the world that wrote it
    for name in selected:
        print(f"{name}")
        for destination in build(name, available[name], out_dir):
            owner = claimed.setdefault(destination.name, name)
            if owner != name:
                raise SystemExit(
                    f"{name} writes {destination.name}, but {owner} already did. Two worlds cannot write "
                    "the same file into one out/ -- give one of them a different output name."
                )
            print(f"  -> {destination.relative_to(ROOT)}  ({destination.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
