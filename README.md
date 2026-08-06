# iw — build Infinite Worlds worlds in Python

Authoring a large Infinite Worlds world by hand is painful: as a world grows and the number of tracked 
items, tirgger events, and other interconnect systems grows, the web interface becomes increasingly 
unwieldy. This repo contains tools for developing worlds programatically, unlocking the ability to use
python scripting when developing the world.

You can find the browser interface for these tools [here](https://shakshuka-man.github.io/iw/lab/index.html).

```python
import iw
from iw import plot

world = iw.World(title="The Dark Lord")
block = iw.InstructionBlock(name="Plot")
world.instructionBlocks.append(block)

HUNT = plot.PlotStage()
HUNT.plot_details = plot.PlotStageDetails(instruction_blocks={block: "I must find the dark lord."})

SLAIN = plot.PlotStage()
VICTORY = plot.PlotTransition(starting_stage=HUNT, ending_stage=SLAIN,
                              trigger_on_scenario="I slay the dark lord",
                              end_game=True, can_continue=False)
SLAIN.plot_details = plot.PlotStageDetails(instruction_blocks={block: "The dark lord is dead."})

plot.add_plot(world, [HUNT, SLAIN], [VICTORY])
```

## Running this yourself

**Every world here is a notebook, and you can run it without installing anything.** The site is
JupyterLite: Python compiled to WebAssembly, running in the tab. Nothing is uploaded, nothing is
executed on a server, and there is no account to make.

There are multiple ways to use this, depending on how comfortable you are with coding:

- **Never written Python.** Open a tutorial, run it top to bottom, read what it says.
- **Play around with the tutorials.** Each of the cells in the tutorial are editable, and you can
  try making changes and see how the generated world reflects your changes.
- **Apply it to your own wold.** Upload your world's json, and change the input of the notebook
  to read your world. Run the notebook again, and you can see the changes applied to the world
  you supplied.
- **Develop your own worlds from scratch** As you develop more complex worlds, you will outgrow
  the browser-based notebooks. When that time comes, you will want to clone this repo and
  set up your own local development environment. See the **Working locally** section below for
  more details.

## The tutorials

This repo contains the following tutorials to demonstrate world development: 

- **[Tutorial 1 — `iw`: the data model](https://shakshuka-man.github.io/iw/lab/index.html?path=worlds/tutorial_iw/README.md)**: This tutorial covers the basics
  of creating worlds and the objects within them.
- **[Tutorial 2 — automation](https://shakshuka-man.github.io/iw/lab/index.html?path=worlds/tutorial_advanced/README.md)**: This tutorial covers how to leverage
  this repo to make developing large worlds more efficient that using IW's built-in editor.
- **[Tutorial 3 — `plot`: the plot engine](https://shakshuka-man.github.io/iw/lab/index.html?path=worlds/tutorial_plot/README.md)**: This tutorial covers how to
  use the plot engine, a tool for developing plotlines, world advancement, and tracking player
  progression.

If you want to delve more into the full set of features, then there are two reference documents that
contain the details on the two main modules of this repo:

- **`iw`** is a mirror of the Infinite Worlds JSON, where each IW object has a python equivalent. The
  reference document is located at [docs/iw.md](docs/iw.md).
- **`iw.plot`** is the plot engine, used to contruct the machinery to implement plotlines. The reference
  document is located at [docs/plot.md](docs/plot.md).

## Working locally

Requires Python 3.14 or newer.

```bash
git clone <this repo> && cd iw
python build.py --list                # what's in here
python build.py tutorial_iw_5_triggers   # build one world -> out/tutorial_iw_5_triggers.json
python build.py                       # build them all
```

Then paste `out/<world>.json` into Infinite Worlds. `build.py` puts the repo on the import path itself,
so nothing needs installing. If you want `import iw` to work from your own scripts anywhere,
`pip install -e .`.

To build and try the browser site locally:

```bash
pip install -r requirements-site.txt
python site.py --serve                # http://localhost:8000/lab/index.html
python site.py --clean                # delete everything generated (out/, _site/, caches)
```