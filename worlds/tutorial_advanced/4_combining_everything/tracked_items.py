"""The tracked items, as a subsystem in a file of its own: the Sanity meter and the day counter, lifted
from basic tutorial 4.

`SANITY` is exposed at module level on purpose. `sanity_bands.py` imports this exact object to hang its
band triggers off it, so the meter is defined once, here, and referenced everywhere else.
"""

import iw

SANITY = iw.TrackedItem(
    name="Sanity",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    initialValue="100",
    description=(
        "A measure of how sane I am. 100 represents optimal mental health, and 0 represents complete mental breakdown."
    ),
    updateInstructions=(
        "Whenever dawn breaks, if I was able to keep the lighthouse operational throughout the night, increase this by 5 to "
        "a maximum of 100.\n"
        "Whenever the lighthouse fails during the night, reduce this by <<10-$player.skills.mental_resilience>> to a minimum of 0.\n"
    ),
    autoUpdate=True,
)

DAYS_ON_ISLAND = iw.TrackedItem(
    name="Days On The Island",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    description="How many days I have been on the island of Rona",
    updateInstructions=(
        "Whenever dawn breaks, increase this by 1."
    ),
    autoUpdate=True,
)


def install_into(world: iw.World) -> None:
    """Add both tracked items *to* `world`. `SANITY` is the object `sanity_bands.py` imports from here, so
    this install is what actually registers the meter the band triggers point at."""
    world.trackedItems.extend([SANITY, DAYS_ON_ISLAND])
