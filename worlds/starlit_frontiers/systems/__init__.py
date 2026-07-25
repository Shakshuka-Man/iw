"""The star map: 126 systems and the jump links between them -- all the map's data, and nothing else.

A system is a place; a jump link is a connection between two of them, with a difficulty. Both are inert
data: the nodes are one data file per cluster, and the edges are `jump_links.py`. This file is a dumb data
store, the same shape as `ships` -- the catalogue of what the map *is*. What you *do* with it -- the
pathfinding, the routes out to each gateway, and the triggers that move you across the graph -- is logic,
and lives in `navigation.py`.

The lore entries are the reason a world with 126 systems is affordable at all. Each one is keyed on its
system's own name, so the AI is told about Sargas only on the turns when somebody says "Sargas".
"""
from __future__ import annotations

import iw

from . import antares, canopus, polaris, hyades, pleiades, inner_systems
from .models import System, StellarObject, JumpLink  # noqa: F401
from .jump_links import ALL_JUMP_LINKS, get_all_jump_links  # noqa: F401

ANTARES_SYSTEMS = antares.ANTARES_SYSTEMS
CANOPUS_SYSTEMS = canopus.CANOPUS_SYSTEMS
POLARIS_SYSTEMS = polaris.POLARIS_SYSTEMS
HYADES_SYSTEMS = hyades.HYADES_SYSTEMS
PLEIADES_SYSTEMS = pleiades.PLEIADES_SYSTEMS
INNER_SYSTEMS = inner_systems.INNER_SYSTEMS


ALL_SYSTEMS = INNER_SYSTEMS + ANTARES_SYSTEMS + CANOPUS_SYSTEMS + POLARIS_SYSTEMS + HYADES_SYSTEMS + PLEIADES_SYSTEMS


def get_systems() -> list[System]:
    """Return all defined systems."""
    return ALL_SYSTEMS


# ---- Where you are ------------------------------------------------------------------------------

def lore_entries() -> list[iw.LoreBookEntry]:
    """One entry per system, keyed on the system's own name.

    Deliberately leaner than navigation's `info_json`, which is what the sheet's `Current system info`
    holds: a lore entry is paid for on every turn that happens to mention the name, so it carries short
    descriptions and no neighbours. The rich version is only ever held for the one system you are
    standing in."""
    return [
        iw.LoreBookEntry(
            name=f"System - {system.cluster.value} - {system.name}",
            content=system.to_lore_json(),
            keywords=[system.name],
        )
        for system in ALL_SYSTEMS
    ]


def install_into(world: iw.World) -> None:
    """Add the lore book of all 126 systems. The items that say where you *are* (`Current system`, `Current
    system info`) are on the character sheet in `player_details`; this is the map they point into."""
    world.loreBookEntries.extend(lore_entries())
