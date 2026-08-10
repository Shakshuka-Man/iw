# %% [markdown]
# # Plot tutorial 4 — One plot, different people
#
# It is quite common that a world designer wants the player to be able to choose between different playable
# characters, and have the plot vary between those characters. Sometimes we want minor variations, and sometimes
# we want the plot to be fundamentally different for these different characters. This is something that the
# plot engine can handle, and this example will show off how we can have the plotline vary for multiple
# different characters.
#
# In this example, we have a simple fantasy setting about defeating an evil tyrant by breaking into his keep and
# slaying him to liberate the land. Each of the three characters has a character specific intro scene. They then
# converge into a stage with different descriptions based on the character, and we then have a character specific
# transition to the final plot stage.
#
# ```
# ENTRY ─▶ OUTER_KEEP ─┬──▶ THRONE_ROOM ─────────────┐
#                      │                             ├─▶ VICTORY
#                      └─(mage only)─▶ POWER_SOURCE ─┘
# ```
#

# %%
import pathlib
import iw
from iw import plot

world = iw.World(
    title="The Tyrant's Keep",
    instructions="I am a hero who has come to the keep of a cruel tyrant to end his reign.",
)

plot_instructions = iw.InstructionBlock(name="Plot stage specific instructions")
world.instructionBlocks.append(plot_instructions)

# %% [markdown]
# ## The characters
#
# We will have three different playable characters, each of which will have a different experience as the plot develops.

# %%
warrior = iw.PossibleCharacter(name="Sir Garran", description="A seasoned warrior and master of the blade.")
mage = iw.PossibleCharacter(name="Lyra", description="A mage who feels hidden magic and can shapeshift into beasts.")
thief = iw.PossibleCharacter(name="Sable", description="A thief at home in sewers, shadows, and other people's houses.")
world.possibleCharacters.extend([warrior, mage, thief])

# %% [markdown]
# ## Character specific plot details
#
# The initial plot stage is getting into the keep. Each of our three characters has different strengths and
# weaknesses, and so we will want a different instruction block for each that describes their method for
# entering the keep.
#
# Where before we were using the `plot_details` attribute of a `PlotStage`, we are now using a different attribute:
# `character_specific_plot_details`. This allows us to specify that some plot details are relevant to some characters
# but not others.

# %%
ENTRY = plot.PlotStage(description="Getting into the keep")
ENTRY.character_specific_plot_details = [
    plot.PlotStageDetails(characters=warrior, instruction_blocks={
        plot_instructions:
            "I am a warrior, come to end the tyrant. His gate is held by two guards, and I mean to go "
            "through them -- I am a seasoned warrior, easily able to defeat them."
    }),
    plot.PlotStageDetails(characters=thief, instruction_blocks={
        plot_instructions:
            "I am a thief, come to end the tyrant. I will not go near his guarded gate: there is a sewer "
            "grate beneath the east wall, and I can use it to enter the keep silently and unseen."
    }),
    plot.PlotStageDetails(characters=mage, instruction_blocks={
        plot_instructions:
            "I am a mage, come to end the tyrant. His gate is guarded, so I will not approach it as a "
            "human -- I will shapeshift into an animal to bypass the guards."
    }),
]

# %% [markdown]
# ## Character specific overrides
#
# The next plot stage is about moving through the outer parts of the tyrant's keep. For this, we want the warrior
# and the thief to have the same experience, but we want a special experience available to just the mage. Instead
# of needing to repeat the same instructions for multiple characters, we can set up some default instructions using
# `plot_details`, as well as character specific details for just the mage.
#
# If a character has any character-specific plot stage details, then those will take priority over the standard ones.

# %%
OUTER_KEEP = plot.PlotStage(description="The outer keep")
TO_OUTER_KEEP = plot.PlotTransition(
    starting_stage=ENTRY, ending_stage=OUTER_KEEP,
    trigger_on_scenario="I get inside the keep",
)
OUTER_KEEP.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am moving through the outer halls of the keep -- guardrooms, cold storerooms, a chapel gone to "
        "dust. The way to the throne room lies somewhere ahead."
})
OUTER_KEEP.character_specific_plot_details = [
    plot.PlotStageDetails(characters=mage, instruction_blocks={
        plot_instructions:
            "I am moving through the outer halls of the keep, and where another would see only dust and "
            "stone, I see it: a seam of arcane light buried in one wall, a concealment ward hiding a "
            "passage. Something is being kept out of sight back there."
    }),
]

# %% [markdown]
# ## Character-exclusive plot stages
#
# We have two methods of defeating the tyrant. The first is a showdown in the throne room, which any character can do.
# The second is mage-exclusive - by finding the power source of the tyrant, the mage can destroy it and defeat the
# tyrant without need for a confrontation.
#
# Although a plot stage cannot inherently be restricted to a specific character, we can restrict the transitions
# into a plot stage to a character. In this case, we restrict the transition into the POWER_SOURCE plot stage to
# the mage only. This will produce a warning down the line, but we can ignore that warning.

# %%
THRONE_ROOM = plot.PlotStage(description="The throne room")
TO_THRONE_ROOM = plot.PlotTransition(
    starting_stage=OUTER_KEEP, ending_stage=THRONE_ROOM,
    trigger_on_scenario="I press on toward the throne room",
)
THRONE_ROOM.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am in the tyrant's throne room, and the tyrant himself is before me on his black throne. There "
        "is no more keep to cross and no one left between us. It ends here."
})

POWER_SOURCE = plot.PlotStage(description="The tyrant's power source")
TO_POWER_SOURCE = plot.PlotTransition(
    starting_stage=OUTER_KEEP, ending_stage=POWER_SOURCE,
    trigger_on_scenario="I follow the magical trail and slip into the hidden passage",
    characters=mage, # This can be a single character or a list of characters
    transition_event=(
        "Following the traces of magic, I pass through the hidden passage and into a secret chamber. "
        "In the center of this chamber is a corrupted well of foul water that the tyrant draws his power from."
    ),
)
POWER_SOURCE.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I have found the source of the tyrant's power - a corrupted well of foul water in a hidden chamber. "
        "If I cleanse the well, I can defeat the tyrant without need for a confrontation."
})

# %% [markdown]
# ## Finishing off the plotline
#
# With both of the plot branches resolved, we can create a victory plot stage.

# %%
VICTORY = plot.PlotStage(description="Victory")
DEFEAT_TYRANT = plot.PlotTransition(
    starting_stage=THRONE_ROOM, ending_stage=VICTORY,
    trigger_on_scenario="I defeat the tyrant",
    end_game=True, can_continue=True,
    transition_event="The tyrant falls at last, and from the cells far below a cheer goes up. It is over.",
)
DESTROY_POWER_SOURCE = plot.PlotTransition(
    starting_stage=POWER_SOURCE, ending_stage=VICTORY,
    trigger_on_scenario="I cleanse the well",
    end_game=True, can_continue=True,
    transition_event=(
        "I cleanse the well and its waters run clear. Far off in the throne room the tyrant "
        "crumples as his stolen power leaves him. I celebrate, having been victorious without a fight."
    ),
)
VICTORY.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "The tyrant is dead and his keep is ours. The gates stand open, the prisoners are free, and "
        "daylight is in these halls for the first time in years."
})

# %% [markdown]
# ## Warnings
#
# As we add the plot, you will see some warnings here about how there is a plot stage not reachable by two characters.
# This is fine for this example, but it may be useful for more complex worlds to ensure that everything is reachable.
# %%
plot.add_single_plot(
    world,
    [ENTRY, OUTER_KEEP, THRONE_ROOM, POWER_SOURCE, VICTORY],
    [TO_OUTER_KEEP, TO_THRONE_ROOM, TO_POWER_SOURCE, DEFEAT_TYRANT, DESTROY_POWER_SOURCE],
)

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_plot_4_characters.json").write_text(world.to_json())

