# Build Infinite Worlds worlds in Python

This is a Python notebook environment that runs entirely inside your browser tab. There is nothing to
install, nothing gets uploaded, no code runs on a server, and there is no account to make. To reset any
changes made, click `Help` -> `Clear Browser Data`.

## Try it now

1. Open the first tutorial: [worlds / tutorial_iw / 1_simple_world](worlds/tutorial_iw/1_simple_world/world.ipynb).
   Or find it yourself in the file browser on the left and double-click `world.ipynb`.
2. Wait a moment for the kernel to start. The circle in the top right goes from ○ to ●. The first
   start is slow, because Python itself is being downloaded into the tab.
3. In the menu, pick **Run → Run All Cells**.
4. A few new `.json` files appear in that same folder, one for each world the notebook builds. The finished
   one is `bones_in_the_ocean.json`. Right-click it and choose Download. That file is a world. Paste it
   into Infinite Worlds and play it.

Every world is a folder, and that folder is your workspace for it. The notebook is always
`world.ipynb`, and anything you build with it lands beside the notebook that built it. Change the filename
in the last cell and run again, and both versions sit there together. That is easier to keep track of than
a pile of JSONs at the root with no clue which came from what.

## The three tutorials

Each one is a folder of notebooks with a contents page. Read them in order, because each one assumes the
one before it. Click a title to open its contents page.

### [1 — `iw`: the data model](worlds/tutorial_iw/README.md)

This tutorial explains the basic functionality of how to create worlds. The first notebook creates a simple 
example of a world, and each subsequent notebook shows how new features can be added to flesh out the world
and add new functionality.

This is intended as the starting point to get familiar with the basics.

### [2 — advanced: why not just use the editor](worlds/tutorial_advanced/README.md)

This tutorial demonstrates how we can programmatically construct a more complex world. The core of the world
is the same as the basic tutorial, but it demonstrates how to handle a growing world and how to leverage the
Python tools to make things more efficient than IW's native editor.

### [3 — `plot`: the plot engine](worlds/tutorial_plot/README.md)

The plot engine is a tool which allows the world designer to handle complex plotlines, character advancement, 
and world development. It generates the necessary tracked items, triggers, and other objects to control how a 
world develops and changes as a player plays it.

## Fully-fleshed out worlds

Within the `worlds` directory, there are examples of complete, large-scale worlds. These can be used as examples of 
advanced projects and a showcase of what these tools can achieve.

## Reference documents

There are three reference pages, and they are here on the drive. Open them beside a notebook while you work.

| |                                                                                                                                  |
|---|----------------------------------------------------------------------------------------------------------------------------------|
| [**`iw` reference**](docs/iw.md) | Every object in `iw`, every attribute with its type, default and purpose, and every enum member with a line of code using it. |
| [**`plot` reference**](docs/plot.md) | The same for the plot compiler, plus what it emits, what it refuses to emit, and why.                                         |
| [**`iw.tools` helpers**](docs/reference-tools.md) | Additional functions that do not map directly to IW objects but help in the construction of advanced worlds.                     |

Each page is one document: the structure is generated from the library itself, so it cannot be out of
date, and what each field is *for* sits in the row beside it.

## Exporting the json

There are two ways, and they suit different sizes:

- Right-click and choose Download in the file browser. This always works, including for the 5 MB world.
- Double-click the `.json` to open it as plain text, then select all and copy. That is fine for a tutorial
  world, but don't do it to `starlit_frontiers.json` unless you enjoy watching a browser think.

## How to use this

- **You have never written Python.** Open a tutorial, run it top to bottom, and read what it says. The
  prose is the point; the code is there to be run, not written.
- **You want to tinker.** Change any code cell and run it again -- rewrite the story text, move the numbers
  around, add a stage. It is ordinary Python against the real library, the same `iw` package the repository
  ships, so anything a tutorial does you can do too. You cannot break anything but your own copy.
- **You want to build something of your own.** Make a new folder in the file browser with its own
  `world.ipynb`, or -- once the tab starts to feel small -- move to your own machine (below) and work in a
  real editor.

Everything you do here is saved in your browser, and it stays there: the notebooks you have run, the
worlds you have generated, the files you have uploaded. That is what lets you close the tab and come back.
It also means a file you made last week is still sitting in the file browser today, and a notebook
you have edited keeps *your* version rather than picking up a newer one.

To throw all of it away and get the site back exactly as it ships, choose **Help → Clear Browser Data**. It
is permanent, and it will take your uploaded worlds with it, so download anything you want to keep first.

## Running it on your own machine

Nothing here requires it. But a browser tab is a poor place to keep work you care about, and sooner or
later you will want a proper editor, version control, and a world too big to hold in a tab. When that
happens, you clone the repository and run the very same files -- the notebooks on this site are *generated
from* the `world.py` files in it, so nothing you have learned is thrown away.

You need three things: Python (3.11 or newer), Git, and an editor. Rather than reinvent those instructions
here, follow your editor's own getting-started guide -- each one walks you through installing Python and the
editor together:

- **VS Code** — [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- **PyCharm** — [Install PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html), then its
  [Quick Start Guide](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

The one change from those guides: wherever they have you create a new project, **clone this repository and
open that folder instead**.

```bash
git clone <this repository> && cd iw
python build.py --list                       # every world, and where it lives
python build.py tutorial_iw_5_triggers       # build one -> out/tutorial_iw_5_triggers.json
python build.py                              # build them all
```

`iw` has no dependencies, so a bare Python is enough for the worlds -- no virtual environment required. You
only need one, plus `pip install -r requirements-site.txt`, if you want to rebuild *this site* itself with
`python site.py --serve`; that part has dependencies, the worlds do not.

To write your own, make a folder under `worlds/`, put a `world.py` in it that defines a module-level
`world`, and end it by saving the JSON. `python build.py` finds it automatically, and it becomes a notebook
on the site by the same route everything here did.
