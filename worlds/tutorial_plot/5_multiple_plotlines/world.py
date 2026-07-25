# %% [markdown]
# # Plot tutorial 5 — Many plots at once
#
# So far, every world we have built has had a single plotline, and as the player advances through that plot,
# they have a single axis of progression. However, it is common for the world designer to want multiple axes
# of progression, or multiple simultaneous plotlines. In this world, we will show how it can be done.
#
# In this example, we build a fantasy world where the hero practices martial arts that can manipulate the elements.
# The protagonist can train in four base elements -- fire, water, earth and air -- and use their expertise in this
# to unlock advanced hybrid elements and eventually become the master of elements.
#
# We will model the player's progress in each of the martial arts as its own separate plotline - a player will be
# able to advance along the fire plotline and the water plotline independently, with progress in each tracked
# separately.

# %%
import pathlib

import iw
from iw import plot

world = iw.World(title="The Four Disciplines")
world.instructions = """
This is an adventure set in a fantasy world dominated by martial arts. Martial arts can be used to control the four classical elements - Fire, Water, Air and Earth.

There are also advanced hybrid elements that can be mastered by becoming proficient with multiple elements.

I am on a journey to master all four elements, and become Master of Elements.
"""

# %% [markdown]
# ## The four basic elements
#
# Each of the basic elements will have the following:
# - A tracked item that tracks the player's skill with that element, ranging from 0 to 100
# - An instruction block that tells the AI what the user's skill with that element is
# - A plotline that updates this instruction block as the user gains skill
#
# The skill tracked item auto-increments as the player uses that element. The plotline's transitions then fire
# when the skill crosses a threshold -- 25 for apprentice, then 50, 75 and 100 -- so the plot rank keeps pace
# with the skill automatically. Because the transition fires on a tracked-item value rather than the player
# saying something, it carries an `additional_conditions` gate instead of a `trigger_on_scenario`.

# %%
# ─── Fire ────────────────────────────────────────────────────────────────────────────────────────
FIRE_SKILL = iw.TrackedItem(
    name="Fire Skill",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    updateInstructions="Whenever I use a fire skill, increase this by 1, to a maximum of 100.",
    autoUpdate=True,
)
world.trackedItems.append(FIRE_SKILL)

FIRE_INSTRUCTIONS = iw.InstructionBlock(name="Fire")
world.instructionBlocks.append(FIRE_INSTRUCTIONS)

FIRE_NOVICE = plot.PlotStage()
FIRE_NOVICE.plot_details = plot.PlotStageDetails(instruction_blocks={FIRE_INSTRUCTIONS: "I am a novice of fire, able to conjure little more than sparks and smoke."})

FIRE_APPRENTICE = plot.PlotStage()
FIRE_TO_APPRENTICE = plot.PlotTransition(starting_stage=FIRE_NOVICE, ending_stage=FIRE_APPRENTICE, additional_conditions=[iw.tools.tracked_item_is(FIRE_SKILL, "25", iw.Inequality.AT_LEAST)])
FIRE_APPRENTICE.plot_details = plot.PlotStageDetails(instruction_blocks={FIRE_INSTRUCTIONS: "I am an apprentice of fire, able to kindle and hold a steady flame at will."})

FIRE_ADEPT = plot.PlotStage()
FIRE_TO_ADEPT = plot.PlotTransition(starting_stage=FIRE_APPRENTICE, ending_stage=FIRE_ADEPT, additional_conditions=[iw.tools.tracked_item_is(FIRE_SKILL, "50", iw.Inequality.AT_LEAST)])
FIRE_ADEPT.plot_details = plot.PlotStageDetails(instruction_blocks={FIRE_INSTRUCTIONS: "I am an adept of fire, hurling fireballs and stepping unburned through flame."})

FIRE_EXPERT = plot.PlotStage()
FIRE_TO_EXPERT = plot.PlotTransition(starting_stage=FIRE_ADEPT, ending_stage=FIRE_EXPERT, additional_conditions=[iw.tools.tracked_item_is(FIRE_SKILL, "75", iw.Inequality.AT_LEAST)])
FIRE_EXPERT.plot_details = plot.PlotStageDetails(instruction_blocks={FIRE_INSTRUCTIONS: "I am an expert of fire, calling up roaring walls of flame at a gesture."})

FIRE_MASTER = plot.PlotStage()
FIRE_TO_MASTER = plot.PlotTransition(starting_stage=FIRE_EXPERT, ending_stage=FIRE_MASTER, additional_conditions=[iw.tools.tracked_item_is(FIRE_SKILL, "100", iw.Inequality.AT_LEAST)])
FIRE_MASTER.plot_details = plot.PlotStageDetails(instruction_blocks={FIRE_INSTRUCTIONS: "I am a master of fire, able to summon infernos and forge weapons of pure heat."})

FIRE_PLOTLINE = plot.Plotline("Fire",
    [FIRE_NOVICE, FIRE_APPRENTICE, FIRE_ADEPT, FIRE_EXPERT, FIRE_MASTER],
    [FIRE_TO_APPRENTICE, FIRE_TO_ADEPT, FIRE_TO_EXPERT, FIRE_TO_MASTER],
)

# ─── Water ───────────────────────────────────────────────────────────────────────────────────────
WATER_SKILL = iw.TrackedItem(
    name="Water Skill",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    updateInstructions="Whenever I use a water skill, increase this by 1, to a maximum of 100.",
    autoUpdate=True,
)
world.trackedItems.append(WATER_SKILL)

WATER_INSTRUCTIONS = iw.InstructionBlock(name="Water")
world.instructionBlocks.append(WATER_INSTRUCTIONS)

WATER_NOVICE = plot.PlotStage()
WATER_NOVICE.plot_details = plot.PlotStageDetails(instruction_blocks={WATER_INSTRUCTIONS: "I am a novice of water, able to do little more than ripple a still pool."})

WATER_APPRENTICE = plot.PlotStage()
WATER_TO_APPRENTICE = plot.PlotTransition(starting_stage=WATER_NOVICE, ending_stage=WATER_APPRENTICE, additional_conditions=[iw.tools.tracked_item_is(WATER_SKILL, "25", iw.Inequality.AT_LEAST)])
WATER_APPRENTICE.plot_details = plot.PlotStageDetails(instruction_blocks={WATER_INSTRUCTIONS: "I am an apprentice of water, drawing clean water from the very air."})

WATER_ADEPT = plot.PlotStage()
WATER_TO_ADEPT = plot.PlotTransition(starting_stage=WATER_APPRENTICE, ending_stage=WATER_ADEPT, additional_conditions=[iw.tools.tracked_item_is(WATER_SKILL, "50", iw.Inequality.AT_LEAST)])
WATER_ADEPT.plot_details = plot.PlotStageDetails(instruction_blocks={WATER_INSTRUCTIONS: "I am an adept of water, shaping currents and turning aside the falling rain."})

WATER_EXPERT = plot.PlotStage()
WATER_TO_EXPERT = plot.PlotTransition(starting_stage=WATER_ADEPT, ending_stage=WATER_EXPERT, additional_conditions=[iw.tools.tracked_item_is(WATER_SKILL, "75", iw.Inequality.AT_LEAST)])
WATER_EXPERT.plot_details = plot.PlotStageDetails(instruction_blocks={WATER_INSTRUCTIONS: "I am an expert of water, commanding crashing waves and freezing what I touch."})

WATER_MASTER = plot.PlotStage()
WATER_TO_MASTER = plot.PlotTransition(starting_stage=WATER_EXPERT, ending_stage=WATER_MASTER, additional_conditions=[iw.tools.tracked_item_is(WATER_SKILL, "100", iw.Inequality.AT_LEAST)])
WATER_MASTER.plot_details = plot.PlotStageDetails(instruction_blocks={WATER_INSTRUCTIONS: "I am a master of water, able to part rivers and calm the wildest sea."})

WATER_PLOTLINE = plot.Plotline("Water",
    [WATER_NOVICE, WATER_APPRENTICE, WATER_ADEPT, WATER_EXPERT, WATER_MASTER],
    [WATER_TO_APPRENTICE, WATER_TO_ADEPT, WATER_TO_EXPERT, WATER_TO_MASTER],
)

# ─── Earth ───────────────────────────────────────────────────────────────────────────────────────
EARTH_SKILL = iw.TrackedItem(
    name="Earth Skill",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    updateInstructions="Whenever I use an earth skill, increase this by 1, to a maximum of 100.",
    autoUpdate=True,
)
world.trackedItems.append(EARTH_SKILL)

EARTH_INSTRUCTIONS = iw.InstructionBlock(name="Earth")
world.instructionBlocks.append(EARTH_INSTRUCTIONS)

EARTH_NOVICE = plot.PlotStage()
EARTH_NOVICE.plot_details = plot.PlotStageDetails(instruction_blocks={EARTH_INSTRUCTIONS: "I am a novice of earth, able only to shift a small handful of pebbles."})

EARTH_APPRENTICE = plot.PlotStage()
EARTH_TO_APPRENTICE = plot.PlotTransition(starting_stage=EARTH_NOVICE, ending_stage=EARTH_APPRENTICE, additional_conditions=[iw.tools.tracked_item_is(EARTH_SKILL, "25", iw.Inequality.AT_LEAST)])
EARTH_APPRENTICE.plot_details = plot.PlotStageDetails(instruction_blocks={EARTH_INSTRUCTIONS: "I am an apprentice of earth, raising low mounds of soil and loose stone."})

EARTH_ADEPT = plot.PlotStage()
EARTH_TO_ADEPT = plot.PlotTransition(starting_stage=EARTH_APPRENTICE, ending_stage=EARTH_ADEPT, additional_conditions=[iw.tools.tracked_item_is(EARTH_SKILL, "50", iw.Inequality.AT_LEAST)])
EARTH_ADEPT.plot_details = plot.PlotStageDetails(instruction_blocks={EARTH_INSTRUCTIONS: "I am an adept of earth, hurling boulders and standing utterly unshaken."})

EARTH_EXPERT = plot.PlotStage()
EARTH_TO_EXPERT = plot.PlotTransition(starting_stage=EARTH_ADEPT, ending_stage=EARTH_EXPERT, additional_conditions=[iw.tools.tracked_item_is(EARTH_SKILL, "75", iw.Inequality.AT_LEAST)])
EARTH_EXPERT.plot_details = plot.PlotStageDetails(instruction_blocks={EARTH_INSTRUCTIONS: "I am an expert of earth, raising walls of solid rock from bare ground."})

EARTH_MASTER = plot.PlotStage()
EARTH_TO_MASTER = plot.PlotTransition(starting_stage=EARTH_EXPERT, ending_stage=EARTH_MASTER, additional_conditions=[iw.tools.tracked_item_is(EARTH_SKILL, "100", iw.Inequality.AT_LEAST)])
EARTH_MASTER.plot_details = plot.PlotStageDetails(instruction_blocks={EARTH_INSTRUCTIONS: "I am a master of earth, able to reshape hills and split the ground asunder."})

EARTH_PLOTLINE = plot.Plotline("Earth",
    [EARTH_NOVICE, EARTH_APPRENTICE, EARTH_ADEPT, EARTH_EXPERT, EARTH_MASTER],
    [EARTH_TO_APPRENTICE, EARTH_TO_ADEPT, EARTH_TO_EXPERT, EARTH_TO_MASTER],
)

# ─── Air ─────────────────────────────────────────────────────────────────────────────────────────
AIR_SKILL = iw.TrackedItem(
    name="Air Skill",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    updateInstructions="Whenever I use an air skill, increase this by 1, to a maximum of 100.",
    autoUpdate=True,
)
world.trackedItems.append(AIR_SKILL)

AIR_INSTRUCTIONS = iw.InstructionBlock(name="Air")
world.instructionBlocks.append(AIR_INSTRUCTIONS)

AIR_NOVICE = plot.PlotStage()
AIR_NOVICE.plot_details = plot.PlotStageDetails(instruction_blocks={AIR_INSTRUCTIONS: "I am a novice of air, able to stir no more than a faint breeze."})

AIR_APPRENTICE = plot.PlotStage()
AIR_TO_APPRENTICE = plot.PlotTransition(starting_stage=AIR_NOVICE, ending_stage=AIR_APPRENTICE, additional_conditions=[iw.tools.tracked_item_is(AIR_SKILL, "25", iw.Inequality.AT_LEAST)])
AIR_APPRENTICE.plot_details = plot.PlotStageDetails(instruction_blocks={AIR_INSTRUCTIONS: "I am an apprentice of air, riding gusts to soften every fall."})

AIR_ADEPT = plot.PlotStage()
AIR_TO_ADEPT = plot.PlotTransition(starting_stage=AIR_APPRENTICE, ending_stage=AIR_ADEPT, additional_conditions=[iw.tools.tracked_item_is(AIR_SKILL, "50", iw.Inequality.AT_LEAST)])
AIR_ADEPT.plot_details = plot.PlotStageDetails(instruction_blocks={AIR_INSTRUCTIONS: "I am an adept of air, gliding on the wind and batting arrows aside with gales."})

AIR_EXPERT = plot.PlotStage()
AIR_TO_EXPERT = plot.PlotTransition(starting_stage=AIR_ADEPT, ending_stage=AIR_EXPERT, additional_conditions=[iw.tools.tracked_item_is(AIR_SKILL, "75", iw.Inequality.AT_LEAST)])
AIR_EXPERT.plot_details = plot.PlotStageDetails(instruction_blocks={AIR_INSTRUCTIONS: "I am an expert of air, conjuring whirlwinds and snatching the breath from foes."})

AIR_MASTER = plot.PlotStage()
AIR_TO_MASTER = plot.PlotTransition(starting_stage=AIR_EXPERT, ending_stage=AIR_MASTER, additional_conditions=[iw.tools.tracked_item_is(AIR_SKILL, "100", iw.Inequality.AT_LEAST)])
AIR_MASTER.plot_details = plot.PlotStageDetails(instruction_blocks={AIR_INSTRUCTIONS: "I am a master of air, able to ride the open sky and call down howling cyclones."})

AIR_PLOTLINE = plot.Plotline("Air",
    [AIR_NOVICE, AIR_APPRENTICE, AIR_ADEPT, AIR_EXPERT, AIR_MASTER],
    [AIR_TO_APPRENTICE, AIR_TO_ADEPT, AIR_TO_EXPERT, AIR_TO_MASTER],
)

# %% [markdown]
# ## Hybrid arts -- gating one plotline on the others
#
# The hybrid arts allow us to have progression in one plotline depend on progression in another. For
# example, in order to unlock steam manipulation, the player must be at least adept level in both fire
# and water. This is done with `requires=`, which lists the stages of other plotlines that must be current for the
# transition to fire.
#
# Stages from the same plotline are OR'd together, and different plotlines are AND'd. So
# `requires=[FIRE_ADEPT, FIRE_EXPERT, FIRE_MASTER, WATER_ADEPT, WATER_EXPERT, WATER_MASTER]` reads as "(fire
# is adept, expert or master) AND (water is adept, expert or master)".

# %%
# ─── Steam (Fire + Water) ────────────────────────────────────────────────────────────────────────
STEAM_INSTRUCTIONS = iw.InstructionBlock(name="Steam")
world.instructionBlocks.append(STEAM_INSTRUCTIONS)

STEAM_LOCKED = plot.PlotStage()
STEAM_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={STEAM_INSTRUCTIONS: "The art of steam still eludes me; fire and water will not yet answer as one."})

STEAM_UNLOCKED = plot.PlotStage()
UNLOCK_STEAM = plot.PlotTransition(
    starting_stage=STEAM_LOCKED, ending_stage=STEAM_UNLOCKED,
    requires=[FIRE_ADEPT, FIRE_EXPERT, FIRE_MASTER, WATER_ADEPT, WATER_EXPERT, WATER_MASTER],
    show_message="You have unlocked the Steam technique!",
)
STEAM_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={STEAM_INSTRUCTIONS: "I wield steam, scalding clouds that blind and burn at once."})

STEAM_PLOTLINE = plot.Plotline("Steam", [STEAM_LOCKED, STEAM_UNLOCKED], [UNLOCK_STEAM])

# ─── Magma (Fire + Earth) ────────────────────────────────────────────────────────────────────────
MAGMA_INSTRUCTIONS = iw.InstructionBlock(name="Magma")
world.instructionBlocks.append(MAGMA_INSTRUCTIONS)

MAGMA_LOCKED = plot.PlotStage()
MAGMA_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={MAGMA_INSTRUCTIONS: "The art of magma is beyond me; stone and flame remain stubbornly apart."})

MAGMA_UNLOCKED = plot.PlotStage()
UNLOCK_MAGMA = plot.PlotTransition(
    starting_stage=MAGMA_LOCKED, ending_stage=MAGMA_UNLOCKED,
    requires=[FIRE_ADEPT, FIRE_EXPERT, FIRE_MASTER, EARTH_ADEPT, EARTH_EXPERT, EARTH_MASTER],
    show_message="You have unlocked the Magma technique!",
)
MAGMA_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={MAGMA_INSTRUCTIONS: "I wield magma, molten rock that flows wherever I will it."})

MAGMA_PLOTLINE = plot.Plotline("Magma", [MAGMA_LOCKED, MAGMA_UNLOCKED], [UNLOCK_MAGMA])

# ─── Lightning (Fire + Air) ──────────────────────────────────────────────────────────────────────
LIGHTNING_INSTRUCTIONS = iw.InstructionBlock(name="Lightning")
world.instructionBlocks.append(LIGHTNING_INSTRUCTIONS)

LIGHTNING_LOCKED = plot.PlotStage()
LIGHTNING_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={LIGHTNING_INSTRUCTIONS: "The art of lightning is beyond me; heat and wind refuse to spark."})

LIGHTNING_UNLOCKED = plot.PlotStage()
UNLOCK_LIGHTNING = plot.PlotTransition(
    starting_stage=LIGHTNING_LOCKED, ending_stage=LIGHTNING_UNLOCKED,
    requires=[FIRE_ADEPT, FIRE_EXPERT, FIRE_MASTER, AIR_ADEPT, AIR_EXPERT, AIR_MASTER],
    show_message="You have unlocked the Lightning technique!",
)
LIGHTNING_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={LIGHTNING_INSTRUCTIONS: "I wield lightning, splitting the sky with crackling bolts."})

LIGHTNING_PLOTLINE = plot.Plotline("Lightning", [LIGHTNING_LOCKED, LIGHTNING_UNLOCKED], [UNLOCK_LIGHTNING])

# ─── Mud (Water + Earth) ─────────────────────────────────────────────────────────────────────────
MUD_INSTRUCTIONS = iw.InstructionBlock(name="Mud")
world.instructionBlocks.append(MUD_INSTRUCTIONS)

MUD_LOCKED = plot.PlotStage()
MUD_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={MUD_INSTRUCTIONS: "The art of mud escapes me; water and earth will not yet bind."})

MUD_UNLOCKED = plot.PlotStage()
UNLOCK_MUD = plot.PlotTransition(
    starting_stage=MUD_LOCKED, ending_stage=MUD_UNLOCKED,
    requires=[WATER_ADEPT, WATER_EXPERT, WATER_MASTER, EARTH_ADEPT, EARTH_EXPERT, EARTH_MASTER],
    show_message="You have unlocked the Mud technique!",
)
MUD_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={MUD_INSTRUCTIONS: "I wield mud, dragging mires that swallow my foes whole."})

MUD_PLOTLINE = plot.Plotline("Mud", [MUD_LOCKED, MUD_UNLOCKED], [UNLOCK_MUD])

# ─── Storm (Water + Air) ─────────────────────────────────────────────────────────────────────────
STORM_INSTRUCTIONS = iw.InstructionBlock(name="Storm")
world.instructionBlocks.append(STORM_INSTRUCTIONS)

STORM_LOCKED = plot.PlotStage()
STORM_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={STORM_INSTRUCTIONS: "The art of the storm is beyond me; rain and wind will not yet rage together."})

STORM_UNLOCKED = plot.PlotStage()
UNLOCK_STORM = plot.PlotTransition(
    starting_stage=STORM_LOCKED, ending_stage=STORM_UNLOCKED,
    requires=[WATER_ADEPT, WATER_EXPERT, WATER_MASTER, AIR_ADEPT, AIR_EXPERT, AIR_MASTER],
    show_message="You have unlocked the Storm technique!",
)
STORM_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={STORM_INSTRUCTIONS: "I wield the storm, lashing rain and wind into a single tempest."})

STORM_PLOTLINE = plot.Plotline("Storm", [STORM_LOCKED, STORM_UNLOCKED], [UNLOCK_STORM])

# ─── Sand (Earth + Air) ──────────────────────────────────────────────────────────────────────────
SAND_INSTRUCTIONS = iw.InstructionBlock(name="Sand")
world.instructionBlocks.append(SAND_INSTRUCTIONS)

SAND_LOCKED = plot.PlotStage()
SAND_LOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={SAND_INSTRUCTIONS: "The art of sand eludes me; earth and air will not yet scatter as one."})

SAND_UNLOCKED = plot.PlotStage()
UNLOCK_SAND = plot.PlotTransition(
    starting_stage=SAND_LOCKED, ending_stage=SAND_UNLOCKED,
    requires=[EARTH_ADEPT, EARTH_EXPERT, EARTH_MASTER, AIR_ADEPT, AIR_EXPERT, AIR_MASTER],
    show_message="You have unlocked the Sand technique!",
)
SAND_UNLOCKED.plot_details = plot.PlotStageDetails(instruction_blocks={SAND_INSTRUCTIONS: "I wield sand, stinging stormfronts that scour and blind."})

SAND_PLOTLINE = plot.Plotline("Sand", [SAND_LOCKED, SAND_UNLOCKED], [UNLOCK_SAND])

# %% [markdown]
# ## The victory condition
#
# Our overall victory condition is reaching master status in all four base elements. We can track this by
# introducing another plotline to track the player's overall status as master of elements or not. It only
# has a single transition, which also ends the game.

# %%
MASTER_OF_ELEMENTS_INSTRUCTIONS = iw.InstructionBlock(name="Master of Elements")
world.instructionBlocks.append(MASTER_OF_ELEMENTS_INSTRUCTIONS)

NOT_MASTER_OF_ELEMENTS = plot.PlotStage()
NOT_MASTER_OF_ELEMENTS.plot_details = plot.PlotStageDetails(instruction_blocks={MASTER_OF_ELEMENTS_INSTRUCTIONS: "I am skilled, but I have not yet mastered all four disciplines."})

MASTER_OF_ELEMENTS = plot.PlotStage()
BECOME_GRANDMASTER = plot.PlotTransition(
    starting_stage=NOT_MASTER_OF_ELEMENTS, ending_stage=MASTER_OF_ELEMENTS,
    requires=[FIRE_MASTER, WATER_MASTER, EARTH_MASTER, AIR_MASTER],  # each base art exactly at master
    end_game=True,
    can_continue=True,
    show_message="You have become a grandmaster of all four elements. You win!",
)
MASTER_OF_ELEMENTS.plot_details = plot.PlotStageDetails(instruction_blocks={MASTER_OF_ELEMENTS_INSTRUCTIONS: "I am a grandmaster of all four elements; my mastery is complete."})

VICTORY_PLOTLINE = plot.Plotline("Victory", [NOT_MASTER_OF_ELEMENTS, MASTER_OF_ELEMENTS], [BECOME_GRANDMASTER])

# %% [markdown]
# ## Building the plot
#
# `add_plots` (plural) takes the whole set of plotlines at once -- it has to, because they gate on each
# other, and it cannot check that a `requires` gate is satisfiable without seeing every plotline it refers
# to. Before it emits anything, it also proves that every stage of all eleven plotlines is reachable. Because
# the plotlines are coupled by `requires`, that is a search over combinations of states, not a walk of one
# graph.

# %%
plot.add_plots(world, [
    FIRE_PLOTLINE, WATER_PLOTLINE, EARTH_PLOTLINE, AIR_PLOTLINE,
    STEAM_PLOTLINE, MAGMA_PLOTLINE, LIGHTNING_PLOTLINE, MUD_PLOTLINE, STORM_PLOTLINE, SAND_PLOTLINE,
    VICTORY_PLOTLINE,
])

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_plot_5_multiple_plotlines.json").write_text(world.to_json())
