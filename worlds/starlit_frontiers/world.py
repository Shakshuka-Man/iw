# %% [markdown]
# # Starlit Frontiers
#
# *The year is 3166. MERIT rules the inner systems. The war has been a stalemate for a century.*
#
# This is a **big** world — around 5 MB of JSON, built from 42,000 lines of source. It is here partly
# because it is a good world and partly because it is the proof that this library scales.
#
# | | |
# |---|---|
# | playable characters | 7, each starting in a different place, ship and century |
# | star systems | 126, across 6 clusters |
# | ship models | 180 |
# | lore entries | ~300 — one per ship, one per system |
# | trigger events | ~700 |

# %%
import pathlib

import iw

from starlit_frontiers import (
    characters,
    factions,
    metadata,
    player_details,
    setting,
    ships,
    systems,
)

# %% [markdown]
# ## Transformation
#
# The assembly, and nothing else. `world.py` owns exactly one thing — the title; every other field, object
# and trigger arrives from a subsystem's `install_into(world)`. This cell just calls them in turn, and the
# one thing it decides is the **order**, which runs down the dependency graph — each subsystem after the
# ones it is built from. `player_details`, the character sheet, comes after `ships` and `systems`, whose
# catalogues it reads, and before `characters`, which writes into it. Only one call *has* to sit where it
# does: `metadata` is **last**, because its blurb counts the finished world. (`weapons` and `navigation`
# hold no world objects — the parts the ship models are built from, and the pure graph calculation the
# sheet's triggers call — so they are imported by the subsystems that need them but never installed here.)
#
# `player_details` is the only call that adds tracked items, so where it sits does not change the order
# they appear on screen — that is fixed inside the sheet. What the call order fixes is the order the AI
# reads the blocks and the order the triggers fire.
#
# The lore book — one entry per ship and one per system, 306 in all — rides along inside `ships` and
# `systems`, each entry keyed on its own name. That is what makes a 5 MB world affordable: the engine only
# ever pays for the two or three that the current turn actually mentions.

# %%
world = iw.World(title="Starlit Frontiers")

# The setting's background lore and basic information.
setting.install_into(world)
# The library of ship models and their descriptions.
ships.install_into(world)
# The library of systems, planets, and other stellar objects.
systems.install_into(world)
# The character sheet: every live tracked item in panel order, and every trigger that maintains it -- the
# status line, the ship-detail triggers, and the jump/arrival triggers that rewrite the location half.
player_details.install_into(world)
# The six factions, and their fleet details.
factions.install_into(world)
# The seven playable characters, and the start-of-game trigger that fills in the sheet for whoever you pick.
characters.install_into(world)
# Other miscellaneous data. Last, because the description counts the features of the world.
metadata.install_into(world)

# %% [markdown]
# ## Output
#
# `to_json()` checks the whole thing over before it writes a byte, and on a world this size that is not a
# formality: ~700 triggers reach into tracked items and instruction blocks, and a trigger that points at
# something the world does not contain is not an error the engine reports — it loads, and that trigger
# just never fires.
#
# In practice this world can't get that wrong, because nothing in it writes an id down: the triggers
# reference the tracked-item *objects*, so a mistake is a `NameError` here rather than a silence in play.
# The check is the belt to that pair of braces.
#
# The result is around **5 MB**. In the browser it will take a moment.

# %%
print(world.summary())
pathlib.Path("starlit_frontiers.json").write_text(world.to_json())
