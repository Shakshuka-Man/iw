# %% [markdown]
# # Tutorial 4 — Tracked items
#
# So far, we have been constructing a world about the player's fraying sanity, and how it will change over time.
# However, before now we have been relying on the storyteller AI's vibes to keep track of this between turns.
# In the interest of keeping the player's sanity consistent as the world progresses, we can introduce a tracked
# item to track the player's sanity.
#
# We will be able to take advantage of this even further in the next tutorial.

# %%
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")

# %% [markdown]
# We will have sanity range from 0 to 100, where 100 is completely sane, starting at 100.
# It should be easy for sanity to decrease, and hard for it to increase.
# Mental Resilience will decrease the rate it decreases by.
# We will set it to be visible to the AI only, so the player is never certain how sane they are.

# %%
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

world.trackedItems.extend([SANITY, DAYS_ON_ISLAND])

print(world.summary())
pathlib.Path("bones_in_the_ocean_with_tracked_items.json").write_text(world.to_json())
