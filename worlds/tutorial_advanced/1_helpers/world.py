# %% [markdown]
# # Advanced tutorial 1 — The helper functions
#
# In the basic tutorial, we saw how we can build trigger objects, but we also saw that it was fairly clunky
# to do - we needed a lot of boilerplate, and we needed to repeat ourselves to make sure everything was
# set up properly. Maintaining a lot of triggers like that can be difficult, and so we have some helper functions
# that make things easier.
#
# First, let's set up a basic version of the world.

# %%
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")

SANITY = iw.TrackedItem(
    name="Sanity",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    initialValue="100",
)
world.trackedItems.append(SANITY)

# %% [markdown]
# ## Reading a tracked item
#
# Let us suppose that we want a trigger that happens when the sanity is below 25. The full way of writing that out is:

# %%
old = iw.TriggerCondition(
    type=iw.ConditionType.ON_TRACKED_ITEM,
    category="condition",
    trackedItemID=SANITY.id,
    inequality=iw.Inequality.AT_MOST,
    data={
        "inequality": iw.Inequality.AT_MOST,
        "requiredValue": "24",
        "trackedItemID": SANITY.id,
        "textComparison": "contains",
    },
)

# %% [markdown]
# `SANITY.id` is in there twice, and `AT_MOST` twice, and if the two copies of the id ever disagree the
# trigger quietly stops firing. `iw.tools.tracked_item_is` is the same condition, built from the item
# itself so the id is written once, by the library:

# %%
new = iw.tools.tracked_item_is(SANITY, "24", iw.Inequality.AT_MOST)

# we can verify it really is the same condition:
assert old.data == new.data and old.trackedItemID == new.trackedItemID

# %% [markdown]
# ## Setting a tracked item
#
# Setting a tracked item involves a similar amount of clunkiness. For example, let us suppose we want to set the sanity
# to a specific value. The full way of writing this out would be:

# %%
old = iw.TriggerEffect(
    type=iw.EffectType.SET_TRACKED_ITEM_VALUE,
    trackedItemID=SANITY.id,
    data={
        "action": iw.TrackedItemAction.SET,
        "newValue": "100",
        "replaceWith": "",
        "trackedItemID": SANITY.id,
    },
)

# We can similarly use the helper function iw.tools.set_tracked_item to come up with a cleaner example:

new = iw.tools.set_tracked_item(SANITY, "100")

# %% [markdown]
#
# We can use these to create some triggers that clamp sanity to be between 0 and 100 while avoiding boilerplate

# %%
CLAMP_MINIMUM = iw.TriggerEvent(
    name="Clamp (minimum)",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(SANITY, "0", iw.Inequality.AT_MOST)],
    triggerEffects=[iw.tools.set_tracked_item(SANITY, "0")]
)
CLAMP_MAXIMUM = iw.TriggerEvent(
    name="Clamp (maximum)",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(SANITY, "100", iw.Inequality.AT_LEAST)],
    triggerEffects=[iw.tools.set_tracked_item(SANITY, "100")]
)
world.triggerEvents.extend([CLAMP_MINIMUM, CLAMP_MAXIMUM])

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_advanced_1_helpers.json").write_text(world.to_json())