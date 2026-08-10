# %% [markdown]
# # Plot tutorial 1 — Stages and transitions
#
# A story in `plot` is a set of stages and the transitions between them. A **stage** is a state the plot
# can be in; a **transition** is how the story gets from one stage to the next. Each plot stage can also
# have **details**, which controls what information is given to the Storyteller AI each turn.
#
# In this tutorial we build a simple, linear story: a knight sets out to kill an immortal dark lord, learns
# how his immortality can be broken, breaks it, and kills him.
#
# %%
import pathlib
import iw
from iw import plot
world = iw.World(title="The Dark Lord")

# %% [markdown]
# ## Building the plot stages
#
# The first thing we will do is define the plot stages. Our planned story beats are:
# - The protagonist needs to search for the secret to breaking the dark lord's immortality
# - The protagonist has found the secret to breaking the dark lord's immortality, and needs to actually break it
# - The protagonist has broken the dark lord's immortality, but need to kill him to save the land
# - The protagonist has killed the dark lord and freed the land
# Each of these gets their own `PlotStage` object.

# %%

STAGE_1 = plot.PlotStage(description="Finding the dark lord's secret")
STAGE_2 = plot.PlotStage(description="Breaking the dark lord's immortality")
STAGE_3 = plot.PlotStage(description="Defeating the dark lord")
STAGE_4 = plot.PlotStage(description="Victory")

# %% [markdown]
# Now that we have created the plot stages, we need to decide how we want to transition between them. In this example,
# we have a simple linear plot, we go from `STAGE_1` to `STAGE_2`, then to `STAGE_3` and finally to `STAGE_4`.
#
# We need to tell the AI how we want these transitions to happen. You can do some complex logic, but for this basic
# example, we will just use trigger situations. Each `PlotTransition` is implemented as an IW trigger, and any trigger
# logic can be added to a PlotTransition to add conditions or effects.
#
# Some of our transitions will have a transition event. This causes the trigger to tell the AI what should happen
# next turn.
# %%

TO_STAGE_2 = plot.PlotTransition(
    starting_stage=STAGE_1,
    ending_stage=STAGE_2,
    trigger_on_scenario="I enter the forbidden library",
    transition_event=(
        "I search the library and find an evil tome of magic. Reading it, I discover that the dark lord's "
        "immortality spell is tied to an enormous corrupted oak tree."
    )
)
TO_STAGE_3 = plot.PlotTransition(
    starting_stage=STAGE_2,
    ending_stage=STAGE_3,
    trigger_on_scenario="I destroy the corrupted oak tree",
    transition_event=(
        "I destroy the oak tree, tearing out its roots and burning it to ash. As the last splinter erupts "
        "into flame, I see the clouds overhead clear, and know that the dark lord is vulnerable."
    )
)
TO_STAGE_4 = plot.PlotTransition(
    starting_stage=STAGE_3,
    ending_stage=STAGE_4,
    trigger_on_scenario="I slay the dark lord",
    end_game=True,        # this transition wins the game
    can_continue=True,    # ...but the player may keep playing in the freed land
)

# %% [markdown]
# We have defined the plot stages and the transitions, and we could stop here if we wanted, but we
# wouldn't have a very interesting plot if we did. We can make things more interesting by using
# plot details.
#
# For each plot stage, we can also give it a `PlotStageDetails` object. These are used to define what
# the contents of instruction blocks, tracked items, and other objects should be at each stage of the
# plot.
#
# In our case, we will have two objects that we want to change as the plot progresses. We will have an
# instruction block that gives the current objective, and a tracked item that gives the current state
# of the dark lord.

# %%
PLOT_INSTRUCTIONS=iw.InstructionBlock(name="Plot stage specific instructions")
DARK_LORD_STATUS = iw.TrackedItem(
    name="Dark Lord Status",
    dataType=iw.TrackedItemDataType.TEXT,
    visibility=iw.TrackedItemVisibility.EVERYONE,
)
world.instructionBlocks.append(PLOT_INSTRUCTIONS)
world.trackedItems.append(DARK_LORD_STATUS)

STAGE_1.plot_details = plot.PlotStageDetails(
    instruction_blocks={PLOT_INSTRUCTIONS:
        "I am a knight in a fantasy land. The evil dark lord rules like a tyrant. He has an immortality "
        "spell that protects him. I must travel to the forbidden library to find the secret to breaking it.",},
    tracked_items={DARK_LORD_STATUS: "immortal"},
)

STAGE_2.plot_details = plot.PlotStageDetails(
    instruction_blocks={PLOT_INSTRUCTIONS:
        "I am a knight in a fantasy land. The dark lord's immortality spell is tied to an enormous "
        "corrupted oak tree. I can break the spell, and make him vulnerable, by destroying that tree.",},
    tracked_items={DARK_LORD_STATUS: "immortal"},
)

STAGE_3.plot_details = plot.PlotStageDetails(
    instruction_blocks={PLOT_INSTRUCTIONS:
        "I am a knight in a fantasy land. I have broken the dark lord's spell of immortality, and now he "
        "is vulnerable. I must kill him to liberate the land.",},
    tracked_items={DARK_LORD_STATUS: "vulnerable"},
)

STAGE_4.plot_details = plot.PlotStageDetails(
    instruction_blocks={PLOT_INSTRUCTIONS:
        "I am a knight in a fantasy land. I have defeated the evil dark lord, and freed everybody from "
        "his tyranny.",},
    tracked_items={DARK_LORD_STATUS: "dead"},
)

# %% [markdown]
#
# Now that we have created everything needed for our plot, we can add it to our world. Using `plot.add_plot`
# will create all the tracked items, triggers and other behind-the-scenes machinery to make this plot work.

# %%
plot.add_single_plot(
    world=world,
    plot_stages=[STAGE_1, STAGE_2, STAGE_3, STAGE_4],
    plot_transitions=[TO_STAGE_2, TO_STAGE_3, TO_STAGE_4],
)

# %% [markdown]
# ## Output
#
# When we generate the summary of the world, we can see that the count of triggers and tracked items has increased
# from the plot engine adding additional objects to implement the plot.
#
# In the next tutorial, we will look into what happens behind the scenes here.

# %%

print(world.summary())
pathlib.Path("tutorial_plot_1_simple.json").write_text(world.to_json())
