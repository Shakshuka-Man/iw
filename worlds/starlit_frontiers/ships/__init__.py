"""Ships: the library of all 180 models.

This is the catalogue -- the 180 `ShipTemplate`s, one data file per faction, and `template.py` for the
shape they all share. It is pure reference data: the models, their stats, their weapon loadouts, and the
lore entries generated straight off them (one per model, keyed on its own name, so the AI is told about a
Bison only on the turns somebody says "Bison").

What the world tracks about the *one you are flying* -- its name, model, hull and the rest -- is not here:
that is the character sheet in `player_details`, along with the per-model triggers that read this
catalogue and pin the sheet's derived values to whatever model you are flying.
"""

import iw

from .template import ShipTemplate

from .merit import (
    MERIT_SMALL_CRAFT,
    MERIT_CORVETTES,
    MERIT_FRIGATES,
    MERIT_DESTROYERS,
    MERIT_CRUISERS,
    MERIT_CAPITALS,
    MERIT_SUPPORT,
    MERIT_ALL_SHIPS,
)
from .independent import (
    INDEPENDENT_DRONES,
    INDEPENDENT_TRANSPORT,
    INDEPENDENT_INDUSTRIAL,
    INDEPENDENT_PERSONAL,
    INDEPENDENT_COMBAT,
    INDEPENDENT_ALL_SHIPS,
)
from .pleiades import (
    PLEIADES_SMALL_CRAFT,
    PLEIADES_CORVETTES,
    PLEIADES_FRIGATES,
    PLEIADES_DESTROYERS,
    PLEIADES_CRUISERS,
    PLEIADES_CAPITALS,
    PLEIADES_SUPPORT,
    PLEIADES_ALL_SHIPS,
)
from .hyades import (
    HYADES_SMALL_CRAFT,
    HYADES_CORVETTES,
    HYADES_FRIGATES,
    HYADES_DESTROYERS,
    HYADES_CRUISERS,
    HYADES_CAPITALS,
    HYADES_SUPPORT,
    HYADES_ALL_SHIPS,
)
from .antares import (
    ANTARES_SMALL_CRAFT,
    ANTARES_CORVETTES,
    ANTARES_FRIGATES,
    ANTARES_DESTROYERS,
    ANTARES_CRUISERS,
    ANTARES_CAPITALS,
    ANTARES_SUPPORT,
    ANTARES_ALL_SHIPS,
)
from .canopus import (
    CANOPUS_SMALL_CRAFT,
    CANOPUS_CORVETTES,
    CANOPUS_FRIGATES,
    CANOPUS_DESTROYERS,
    CANOPUS_CRUISERS,
    CANOPUS_CAPITALS,
    CANOPUS_SUPPORT,
    CANOPUS_ALL_SHIPS,
)
from .polaris import (
    POLARIS_SMALL_CRAFT,
    POLARIS_CORVETTES,
    POLARIS_FRIGATES,
    POLARIS_DESTROYERS,
    POLARIS_CRUISERS,
    POLARIS_CAPITALS,
    POLARIS_SUPPORT,
    POLARIS_ALL_SHIPS,
)
from .special import (
    SPECIAL_ALL_SHIPS,
)

ALL_SHIPS = {
    **MERIT_ALL_SHIPS,
    **INDEPENDENT_ALL_SHIPS,
    **PLEIADES_ALL_SHIPS,
    **HYADES_ALL_SHIPS,
    **ANTARES_ALL_SHIPS,
    **CANOPUS_ALL_SHIPS,
    **POLARIS_ALL_SHIPS,
    **SPECIAL_ALL_SHIPS,
}


def lore_entries() -> list[iw.LoreBookEntry]:
    """One entry per model, keyed on the model's own name."""
    return [
        iw.LoreBookEntry(
            name=f"Ship - {ship.faction.value} {ship.name}",
            content=ship.to_info_json(),
            keywords=[ship.name],
        )
        for ship in ALL_SHIPS.values()
    ]


def install_into(world: iw.World) -> None:
    """Add the lore book of all 180 models. The four items that track the ship you are *currently* flying
    live on the character sheet in `player_details`, with the boarding and change-ship logic that
    maintains them."""
    world.loreBookEntries.extend(lore_entries())
