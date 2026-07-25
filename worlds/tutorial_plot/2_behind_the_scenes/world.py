# %% [markdown]
# # Plot tutorial 2 — Behind the scenes
#
# In the last tutorial, we used the plot engine to construct a linear plot. We created some `PlotStage`,
# `PlotTransition` and `PlotStageDetails` objects, and then the plot engine translated those into the
# native Infinite Worlds objects to implement the plot.
#
# In this tutorial, we will be exploring what the plot engine did, by recreating the same output by creating
# the Infinite Worlds objects ourselves. This tutorial doesn't show off any new features compared to the last
# one, it just shows off what is happening behind the scenes.
#

# %%
import pathlib
import iw

world = iw.World(title="The Dark Lord")

# %% [markdown]
# ## The player-facing objects
#
# We start by creating the instruction block and the tracked item that are updated by the `PlotStageDetails` objects.

# %%
PLOT_INSTRUCTIONS=iw.InstructionBlock(name="Plot stage specific instructions")
DARK_LORD_STATUS = iw.TrackedItem(
    name="Dark Lord Status",
    dataType=iw.TrackedItemDataType.TEXT,
    visibility=iw.TrackedItemVisibility.EVERYONE,
)
world.instructionBlocks.append(PLOT_INSTRUCTIONS)
world.trackedItems.append(DARK_LORD_STATUS)

# %% [markdown]
# ## The plot state tracked items
#
# The plot engine always creates a tracked item that tracks the current state of the plot, and a tracked item that
# is used to detect if the plot state has advanced on each turn. If there are multiple plotlines in a single world
# (something that we will explore in a later tutorial), then we will have a plot stage tracked item and a plot
# change tracked item for each plotline.
#
# The value of the plot change tracked item is either 0 (if no plot change occurred this turn) or 1 (if a plot
# change occurred this turn).
#
# The plot state item tracks which of the plot states is considered active at any one time. The world designer
# can choose to provide a tracked item they have prepared in advance, or allow the plot engine to create its own
# tracked item to track the plot state.
#
# Each plot state is given its own unique ID, which by default is a number counting up from 1. Once again, the
# world designer can also give a custom ID to each of the plot stages instead of relying on the generated IDs.

# %%

PLOT_STAGE = iw.TrackedItem(name="Plot Stage", dataType=iw.TrackedItemDataType.NUMBER,
                            visibility=iw.TrackedItemVisibility.HIDDEN, initialValue="0")
PLOT_CHANGE = iw.TrackedItem(name="Plot Change", dataType=iw.TrackedItemDataType.NUMBER,
                             visibility=iw.TrackedItemVisibility.HIDDEN, initialValue="1")
world.trackedItems.extend([PLOT_STAGE, PLOT_CHANGE])

# %% [markdown]
# ## The plot situation tracked item
#
# When we created our plot transitions, we identified three different scenarios that could cause a plot transition.
# However, not all of these will be relevant at the same time, and each trigger scenario causes a bit of overhead
# and credit cost each turn, even if the trigger scenario is not relevant.
#
# The plot engine is clever enough to avoid wasting credits. It analyzes the plot transitions, and in this scenario
# it noticed that in the worst case scenario, only one trigger scenario is relevant at a time. Therefore, we can be
# efficient by using a tracked item for these trigger scenarios, setting the contents of it to the trigger scenario
# that is relevant at each stage of the plot.
#
# As above, if there are multiple plotines in a world, or a plotline that has multiple trigger scenarios that could
# apply at the same time, we would have multiple plot situation tracked items.
# %%

PLOT_SITUATION = iw.TrackedItem(name="Plot Situation 1", dataType=iw.TrackedItemDataType.TEXT,
                                visibility=iw.TrackedItemVisibility.HIDDEN, initialValue=" ")
world.trackedItems.append(PLOT_SITUATION)

# %% [markdown]
# ## The plot transition triggers
#
# We now construct the triggers for advancing the plot. This is where the `PLOT_CHANGE` tracked item comes into
# play - because we are reusing the same tracked item for multiple trigger scenarios, IW will resolve that trigger
# scenario as true, even if we change the value of the tracked item during trigger evaluation. Therefore, we need
# to use the `PLOT_CHANGE` tracked item to limit the plot to only progress one stage per turn.
#
# %%

# Before any of the transition triggers fire, we need to reset the `PLOT_CHANGE` variable back to 0, indicating
# that no plot changes have occurred this turn.
#
# The trigger requires at least one condition, so we require turn_number to be at least 1, which will always be true.
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot: reset per-turn change gate",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is("turn_number", "1", iw.Inequality.AT_LEAST)],
    triggerEffects=[iw.tools.set_tracked_item(PLOT_CHANGE, "0")],
))

# The plot engine recognizes that stage 1 is a starting stage, as there are no transitions to stage 1. If there was
# not a starting stage, or if there were multiple possible starting stages in the same plotline, then the plot
# engine would throw an error instead of adding in the plotlines.

world.triggerEvents.append(iw.TriggerEvent(
    name="Plot: start of game (stage 1)",
    triggerOnStartOfGame=True,
    canTriggerMoreThanOnce=True,
    triggerEffects=[
        iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={
            "id": PLOT_INSTRUCTIONS.id,
            "content": "I am a knight in a fantasy land. The evil dark lord rules like a tyrant. He has an "
                       "immortality spell that protects him. I must travel to the forbidden library to find "
                       "the secret to breaking it.",
        }),
        iw.tools.set_tracked_item(DARK_LORD_STATUS, "immortal"),
        iw.tools.set_tracked_item(PLOT_STAGE, "1"),
        iw.tools.set_tracked_item(PLOT_SITUATION, "I enter the forbidden library"),
    ],
))

# In addition to their declared conditions, the transitions require `PLOT_CHANGE` to be 0. In addition to
# their declared effects, they also set `PLOT_CHANGE` to 1. As this happens after the reset above, this
# means we can only have one plot advancement per turn.

world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Transition 1",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.tools.tracked_item_is(PLOT_CHANGE, "0"),
        iw.tools.tracked_item_is(PLOT_STAGE, "1"),
        iw.TriggerCondition(type=iw.ConditionType.ON_EVENT, category="condition",
                            data=PLOT_SITUATION.as_substitution()),
    ],
    triggerEffects=[
        iw.tools.set_tracked_item(PLOT_CHANGE, "1"),
        iw.tools.set_tracked_item(PLOT_STAGE, "2"),
        iw.TriggerEffect(type=iw.EffectType.TELL_AI, data=(
            "I search the library and find an evil tome of magic. Reading it, I discover that the dark "
            "lord's immortality spell is tied to an enormous corrupted oak tree."
        )),
    ],
))
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Transition 2",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.tools.tracked_item_is(PLOT_CHANGE, "0"),
        iw.tools.tracked_item_is(PLOT_STAGE, "2"),
        iw.TriggerCondition(type=iw.ConditionType.ON_EVENT, category="condition",
                            data=PLOT_SITUATION.as_substitution()),
    ],
    triggerEffects=[
        iw.tools.set_tracked_item(PLOT_CHANGE, "1"),
        iw.tools.set_tracked_item(PLOT_STAGE, "3"),
        iw.TriggerEffect(type=iw.EffectType.TELL_AI, data=(
            "I destroy the oak tree, tearing out its roots and burning it to ash. As the last splinter "
            "erupts into flame, I see the clouds overhead clear, and know that the dark lord is vulnerable."
        )),
    ],
))
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Transition 3",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.tools.tracked_item_is(PLOT_CHANGE, "0"),
        iw.tools.tracked_item_is(PLOT_STAGE, "3"),
        iw.TriggerCondition(type=iw.ConditionType.ON_EVENT, category="condition",
                            data=PLOT_SITUATION.as_substitution()),
    ],
    triggerEffects=[
        iw.tools.set_tracked_item(PLOT_CHANGE, "1"),
        iw.tools.set_tracked_item(PLOT_STAGE, "4"),
        iw.TriggerEffect(type=iw.EffectType.ENDS_GAME, data=True),
    ],
))

# %% [markdown]
# ## The stage content
#
# Each plot stage has a trigger that applies its plot details. These triggers fire every turn, and importantly they
# are lower in the trigger list than the transitions, and therefore are evaluated after. These triggers actually set
# the plot details that are relevant for the plot stage.
#
# The reason for them firing every turn is to allow for easier debugging and manual control over the world. If the
# player wants to skip from one plot stage to another directly, they can simply update the value of the `PLOT_STAGE`
# tracked item, and the following turn the details of the new plot stage will be fully applied.

# %%

world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Stage 1",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(PLOT_STAGE, "1")],
    triggerEffects=[
        iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={
            "id": PLOT_INSTRUCTIONS.id,
            "content": "I am a knight in a fantasy land. The evil dark lord rules like a tyrant. He has an "
                       "immortality spell that protects him. I must travel to the forbidden library to find "
                       "the secret to breaking it.",
        }),
        iw.tools.set_tracked_item(DARK_LORD_STATUS, "immortal"),
        iw.tools.set_tracked_item(PLOT_SITUATION, "I enter the forbidden library"),
    ],
))
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Stage 2",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(PLOT_STAGE, "2")],
    triggerEffects=[
        iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={
            "id": PLOT_INSTRUCTIONS.id,
            "content": "I am a knight in a fantasy land. The dark lord's immortality spell is tied to an "
                       "enormous corrupted oak tree. I can break the spell, and make him vulnerable, by "
                       "destroying that tree.",
        }),
        iw.tools.set_tracked_item(DARK_LORD_STATUS, "immortal"),
        iw.tools.set_tracked_item(PLOT_SITUATION, "I destroy the corrupted oak tree"),
    ],
))
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Stage 3",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(PLOT_STAGE, "3")],
    triggerEffects=[
        iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={
            "id": PLOT_INSTRUCTIONS.id,
            "content": "I am a knight in a fantasy land. I have broken the dark lord's spell of immortality, "
                       "and now he is vulnerable. I must kill him to liberate the land.",
        }),
        iw.tools.set_tracked_item(DARK_LORD_STATUS, "vulnerable"),
        iw.tools.set_tracked_item(PLOT_SITUATION, "I slay the dark lord"),
    ],
))
world.triggerEvents.append(iw.TriggerEvent(
    name="Plot Stage 4",
    canTriggerMoreThanOnce=True,
    triggerConditions=[iw.tools.tracked_item_is(PLOT_STAGE, "4")],
    triggerEffects=[
        iw.TriggerEffect(type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK, data={
            "id": PLOT_INSTRUCTIONS.id,
            "content": "I am a knight in a fantasy land. I have defeated the evil dark lord, and freed "
                       "everybody from his tyranny.",
        }),
        iw.tools.set_tracked_item(DARK_LORD_STATUS, "dead"),
        iw.tools.set_tracked_item(PLOT_SITUATION, " "),
    ],
))

# %% [markdown]
# ## Output
#
# We can compare what we have generated here and what we have generated in the previous tutorial, and see that the
# outputted JSONs are identical (except for the ids, which are randomly generated). We can also see that this is a
# lot more code, and a lot harder to maintain, than just using the plot engine. As we look at the more advanced
# plot engine features, such as branching plotlines or character specific plotlines, then the automation of the plot
# engine becomes even more important.

# %%
print(world.summary())
pathlib.Path("tutorial_plot_2_behind_the_scenes.json").write_text(world.to_json())