# iw — build Infinite Worlds worlds in Python

Authoring a large Infinite Worlds world by hand is painful: the interesting parts of a world are its
**trigger events**, and a world with any real plot needs dozens of them, each a hand-wired bundle of
conditions and effects referencing tracked items by opaque id. Change your mind about the plot and you
are editing twenty triggers by hand.

This repo lets you write the world in Python and generate that JSON.

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

That becomes the trigger events, tracked items and conditions the engine wants — and it refuses to
build a plot with content nobody can ever reach.

## Run it in your browser

**Every world here is a notebook, and you can run it without installing anything.** The site is
JupyterLite: Python compiled to WebAssembly, running in the tab. Nothing is uploaded, nothing is
executed on a server, and there is no account to make.

Each notebook has the same three parts:

- an **input** — which world to start from. Leave it alone to follow the tutorial, or point it at a
  world of your own.
- a **transformation** — the lesson. Add a plot, add tracked items, generate sixteen triggers.
- an **output** — the world JSON, which appears in the file browser on the left. Right-click it and
  choose *Download*, then paste it into Infinite Worlds.

So there are three ways in, and you can stop at any of them:

- **Never written Python.** Open a tutorial, run it top to bottom, read what it says.
- **Want it applied to your own world.** Upload your world's JSON, put its filename in the input cell,
  and re-run. The lesson is now applied to *your* world. That is one line changed.
- **Want to go further.** Rewrite the transformation cell — it is ordinary Python against the real
  library. Still nothing to install.

Clone the repo when you want version control, or a world too big to comfortably hold in a browser tab.

## The two layers

**`iw`** is a typed mirror of the world JSON: `World`, `TrackedItem`, `TriggerEvent`, `TriggerCondition`,
`TriggerEffect`, `PossibleCharacter`, `InstructionBlock`, and so on. Anything the format can express,
you can build here, and `World.from_json` reads an existing world back in. Use it directly when you
want a trigger the plot layer doesn't model — the two layers compose freely in one world.

**`iw.plot`** compiles a *plot* down onto that machinery. You describe **stages** (states the plot can
be in), the **content** at each stage, and the **transitions** between them; `plot` generates the stage
tracker, the per-turn advance gate, the situation-slot pool, and every trigger. It also supports
several independent **plotlines** at once, with cross-plotline "synergy" gates.

Full reference: [docs/iw.md](docs/iw.md) — every object, attribute and enum member, with its type,
default, purpose and a line of code using it. [docs/plot.md](docs/plot.md) is the same for the plot
compiler. Both have their structure generated from the library itself, so neither can be out of date.

## Learn it

Three tutorials, fifteen worlds, each adding one idea to the last. **Start with the first** — the plot
layer compiles down to the tracked items and triggers the first tutorial teaches, and it is no fun to
debug otherwise.

**[Tutorial 1 — `iw`: the data model](docs/tutorial-1-iw.md)**

| | world | the idea |
|---|---|---|
| 1 | `tutorial_iw_1_simple_world` | the `World` object, the round trip, and why every world has skills |
| 2 | `tutorial_iw_2_instruction_blocks` | the island's map, always on; its history, only when named (KIBs) |
| 3 | `tutorial_iw_3_characters` | two keepers who are mirror images, and one boatman who does not speak |
| 4 | `tutorial_iw_4_tracked_items` | a sanity meter the player never sees, and a light that they do |
| 5 | `tutorial_iw_5_triggers` | four triggers that change what is on the island, and never say so |

**[Tutorial 2 — advanced: why not just use the editor](docs/tutorial-2-advanced.md)**

For a small world, Infinite Worlds' own editor is genuinely nicer than this library, and you should use
it. These are the other case — the one where the number of things you would have to click *is* the
problem. A helper primer, three arguments, and — nothing new — combining all of them into one finished world.

| | world | the idea |
|---|---|---|
| 1 | `tutorial_advanced_1_helpers` | **the tools** — `iw.tools`, reading and writing a tracked item without typing its id twice |
| 2 | `tutorial_advanced_2_generating_from_data` | **generate** — `wrecks.csv` becomes a lore book, `sanity_bands.csv` becomes the basic track's ten band triggers |
| 3 | `tutorial_advanced_3_classes_and_files` | **structure** — give the rows a dataclass, split each subsystem into its own file |
| 4 | `tutorial_advanced_4_combining_everything` | **combine** — nothing new, all of it combined into one finished world |

**[Tutorial 3 — `plot`: stages, transitions, plotlines](docs/tutorial-3-plot.md)**

| | world | the idea |
|---|---|---|
| 1 | `tutorial_plot_1_simple` | stages, transitions, and the shape of a plot file |
| 2 | `tutorial_plot_2_behind_the_scenes` | the tracked items and triggers a plot compiles to, by hand |
| 3 | `tutorial_plot_3_branching` | forks, reconvergence, and a moral choice of endings |
| 4 | `tutorial_plot_4_characters` | one plot, several people walking it |
| 5 | `tutorial_plot_5_multiple_plotlines` | many plots at once, gating each other |

Those pages and the notebooks are the same material — they are generated from the same files.

## Working locally

Requires Python 3.14 or newer — the version Pyodide runs, so the site and your clone execute the same
thing. **`iw`'s only dependency is PyYAML**, which Pyodide ships, so it still runs unmodified in a
browser.

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

**The site you are looking at is half in your browser.** JupyterLite keeps its filesystem in the
browser's own storage, keyed to the origin you served from — so notebooks you have run and worlds you
have generated survive a rebuild, and stale ones from an older build keep showing up in the file browser
next to the new ones. `--clean` cannot touch that; nothing on disk can. Clear it from inside the site:
**Help → Clear Browser Data**.

## Layout

```
iw/                    the library — iw.py (data model), plot.py (plot compiler),
                       notebook.py (percent format -> .ipynb, at build time)
worlds/                one folder per world, each with a world.py, grouped into the three
                       tutorial tracks. A README.md per track is that track's contents page.
welcome.md             the site's landing page — what a first-time visitor reads
workspaces/            the layout the site opens with: the welcome page, and the file browser
overrides.json         JupyterLab settings for the site (a .json opens as text, not a tree widget)
jupyter-lite.json      PYTHONPATH=/drive — what lets a notebook in a folder still `import iw`
docs/                  iw.md + plot.md          the prose references: what the fields are *for*
                       reference-*.md           the data dictionaries: what they *are*  (generated)
                       tutorial-*.md            the three tutorials, to read straight through (generated)
                       reference-world.json     a world the engine itself exported
build.py               worlds/**/<world>/world.py  ->  out/<name>.json
notebooks.py           worlds/**/<world>/world.py  ->  .../world.ipynb + docs/tutorial-*.md
reference.py           iw/iw.py, iw/plot.py        ->  docs/reference-*.md   (by introspection)
docs.py                docs/*.md                   ->  docs/*.wiki
site.py                everything above            ->  _site/   (the JupyterLite site)
out/, _site/           generated (gitignored — artifacts, rebuild them)
```

**`worlds/` is what the site's file browser shows**, with `world.ipynb` where the repo has `world.py` —
same tree, folder for folder. So the site is a view of the repo, and cloning after using it is not a
translation exercise. It is also why a world is a *folder*: on the site, the JSON a reader generates is
written next to the notebook that generated it, so a world's folder holds that world's work — and so does
whatever else that world reads. A world split across modules, or driven by a CSV, ships those files into
its folder on the site and imports them there exactly as it does here.

It holds the fifteen tutorials and [`starlit_frontiers`](worlds/starlit_frontiers/) — a real, large world
(126 systems, 699 triggers, 5.2 MB of JSON) that doubles as the proof this all scales.

**The data dictionaries are generated from the library, by introspection.** `reference.py` reads the
dataclasses and writes out every object, attribute, type and default. A hand-written one is a promise to
update two things whenever you change one, and it is a promise nobody keeps; this one cannot drift,
because there is nothing to drift from. `python reference.py --check` fails the build if it is stale.

## One source, four outputs

A world is written **once**, as `worlds/<...>/<world>/world.py`. It is a plain Python script with `# %%`
cell markers in it — the [jupytext "percent" format](https://jupytext.readthedocs.io/en/latest/formats-scripts.html).
That one file becomes the notebook, the tutorial page, the wiki page, and the world JSON:

```
worlds/tutorial_plot/1_simple/world.py
    |
    |-- notebooks.py --> out/notebooks/worlds/tutorial_plot/1_simple/world.ipynb   (the browser)
    |                --> docs/tutorial-2-plot.md
    |                          |
    |                          `-- docs.py --> docs/tutorial-2-plot.wiki   (the MediaWiki site)
    |
    `-- build.py     --> out/tutorial_plot_1_simple.json                   (the engine)
```

The point of the percent format is that the file stays a **plain, importable Python script**. What runs
in the browser and what `build.py` imports are the same bytes, so the docs cannot drift from the code.

The generators all take `--check`, which fails if a committed file is stale; CI runs them, so a world
cannot be changed without its docs following.

## Writing your own world

Make `worlds/<your-world>/world.py`, anywhere under `worlds/` you like. Two rules:

1. Define a module-level `world`.
2. End by saving it as `<your-world>.json` — named after the world, not its folder, so no two worlds
   overwrite each other's output.

```python
# %%
import pathlib
import iw
from iw import plot

# %%
world = iw.World(title="...")
...
plot.add_plot(world, plot_stages, plot_transitions)   # adds the plot to world, in place

# %%
pathlib.Path("my_world.json").write_text(world.to_json())
```

`build.py` runs it with the working directory set to `out/`, so the world's own save *is* the build
output — the file you read is exactly the file that runs. The cell markers are optional (a world with
none becomes a single-cell notebook), but they are what makes it read well in the browser.

A world may split itself across several files in its own folder, and import them by plain name — the
folder is on the path, here and in the browser alike. For a big one, make the folder a package (add an
`__init__.py`) and import it by the folder's name: `from my_world import ships`. Import it absolutely,
never with a relative `from . import`: `world.py` is also a notebook, and as cells it is top-level code
with no package to be relative to.

Three things that catch people out:

- **`add_plot` mutates the world in place and returns nothing** — do not write `world = add_plot(...)`,
  which would bind `world` to `None`. The stages and transitions you pass are deep-copied and left untouched.
- **A stage's content is re-applied every turn it is active**, so it must read as "what is true while I
  am here", not "what just happened". For a one-shot, use the transition (`transition_event`,
  `show_message`, or its `tracked_items`).
- **Cells get re-run.** Build the world at the top of the cell that transforms it, so re-running that
  cell rebuilds from scratch instead of adding the same plot twice. The tutorials all do this.

## The build refuses bad plots

Rather than generating a world that quietly misbehaves in the engine, the build fails on content that
can never be seen: a stage nothing reaches, a transition that can never fire, content written for a
character who can't get there. It also warns about the subtler traps — a stage some character can't
reach (often deliberate), two plotlines fighting over the same instruction block, or a stage that
leaves a stale value in one.

This analysis understands `requires` gates across plotlines, so it catches things like a mutual
deadlock between two plotlines, or a gate that depends on a stage only reachable after the game has
already ended. See [Reachability](docs/plot.md#reachability).

Give your stages a `description`. It is never emitted — it exists only so those messages can say
*stage '3' (the mage's secret passage)* instead of *stage '3'*.

`World.to_json()` applies the same idea one layer down. It validates before it dumps, and raises rather
than emit a world whose triggers point at tracked items, blocks or characters that aren't there. That
is the failure a notebook invites — re-run a cell, get a new object with a new id, and an older trigger
is still holding the old one. The engine would load that world happily and then silently never fire it.

The check lives in `to_json()` rather than in a `validate()` you are trusted to remember, because the
world you never want written to a file is exactly the world you forgot to check. (`World.validate()` is
still there, and still public, if you want to check a world without serialising it.)

## Working on this

Generated JSON is **not** checked in — `out/` is gitignored. Build it yourself; the output is
byte-for-byte reproducible, so the same source always gives the same world (ids included), whether you
build one world or all of them.

Branch, edit or add a world, run `python build.py`, and open a PR. CI builds every world, checks the
generated docs are current, and deploys the site from `main`.
