# %% [markdown]
# # Advanced tutorial 4 — Combining everything: Bones in the Ocean, complete
#
# This tutorial doesn't cover anything new, it is just showing how we can combine everything we've seen before
# into a complete version of the world.
#
# | module | what it owns | where it comes from |
# |---|---|---|
# | `setting.py` | the premise: description, instructions, backstory, opening move | basic 1 |
# | `characters.py` | the two skills, the three playable characters, the boatman | basic 3 |
# | `tracked_items.py` | the Sanity meter and the day counter | basic 4 |
# | `wrecks.py` + `wrecks.csv` | a keyword block per ship, and the roster that names them | advanced 3 |
# | `sanity_bands.py` + `sanity_bands.csv` | the ten band triggers that rewrite the day and the night | advanced 3 |
#
# Each module exposes one function, `install_into(world)`, that adds its part to a world you pass in. Open
# the modules in the file browser to see how each works; this notebook only combines them.
#
# Four of the five modules are self-contained -- they touch the world and nothing else. The exception is
# `sanity_bands.py`. Its triggers have to point at the *same* Sanity meter that `tracked_items.py` defines,
# so rather than build a second meter it imports the one object (`from tracked_items import SANITY`) and
# wires its triggers to that. Because both modules share the one object, the order they install in does not
# matter -- the tracked-item id agrees either way.

# %%
import pathlib

import iw

# Modules beside this one, imported by plain name. Never `from . import` -- this file is also a notebook,
# and cells are top-level code with no package to be relative to.
import setting
import presentation
import characters
import tracked_items
import wrecks
import sanity_bands

# %% [markdown]
# ## Assembly
#
# The notebook owns only the world's title. Everything else arrives from a module. Each `install_into` adds
# that subsystem's fields, tracked items, instruction blocks, keyword blocks, and triggers to the world.

# %%
world = iw.World(title="Bones in the Ocean")

setting.install_into(world)          # description, instructions, background, first input, objective
presentation.install_into(world)     # the voice, the art direction, the cover art, the permissions
characters.install_into(world)       # the two skills, the three keepers, the boatman
tracked_items.install_into(world)    # the Sanity meter and the day counter
wrecks.install_into(world)           # a KIB per ship, and the roster that names them
sanity_bands.install_into(world)     # the ten band triggers, wired to tracked_items' SANITY


# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_advanced_4_combining_everything.json").write_text(world.to_json())

# %% [markdown]
# ## Where to go next
#
# From here, you can do the following:
# - Try editing these scripts to generate a world more to your liking
# - Read the [tutorial for the plot engine](../../tutorial_plot/README.md) to see how structured story development can be implemented
# - Have a look at the [fully fleshed out worlds](../../starlit_frontiers/README.md) to see more complex worlds that can be created
# - Follow the [instructions to set this up on your own machine](../../../welcome.md#running-it-on-your-own-machine) and start developing your own worlds
