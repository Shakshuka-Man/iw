# %% [markdown]
# # Plot tutorial 6 — A plot that can go back to earlier stages
#
# Every plot so far has run forwards. Even the branching one in tutorial 3 forked and rejoined, but never
# doubled back — and that is what let the engine work out where the story begins on its own. It looks for
# the one stage that nothing transitions into, and starts there.
#
# Some stories do not have such a stage. Ours is about a master thief who sits in her lair choosing which
# museum to rob next. Each heist is a stage; finishing one returns her to the lair to pick the next. The
# lair has transitions *into* it, from every heist — so does every other stage, and the engine has nothing
# to single out.
#
# That is what `starting_stage` is for.
#
# %%
import pathlib
import iw
from iw import plot
world = iw.World(title="The Quiet Professional")

# %% [markdown]
# ## The lair, and the jobs
#
# One instruction block carries whatever the thief is currently working on. Each stage rewrites it.

# %%

BRIEF = iw.InstructionBlock(name="The job")
world.instructionBlocks.append(BRIEF)

LAIR = plot.PlotStage(description="The lair, choosing the next job")
LAIR.plot_details = plot.PlotStageDetails(instruction_blocks={BRIEF: (
    "I am in my lair beneath the city, surrounded by floor plans and photographs. No job is in progress. "
    "I am deciding which of the great paintings to take next, and there is no hurry about it."
)})

# %% [markdown]
# Three heists. Each is reached from the lair, and returns to it when it is over.

# %%

MONA_LISA = plot.PlotStage(description="The Mona Lisa, Paris")
MONA_LISA.plot_details = plot.PlotStageDetails(instruction_blocks={BRIEF: (
    "The job is the Mona Lisa, in Paris. She sits behind bulletproof glass in a room that is never empty, "
    "watched by more cameras than any other object on earth. The difficulty is not the glass. It is leaving."
)})

STARRY_NIGHT = plot.PlotStage(description="The Starry Night, New York")
STARRY_NIGHT.plot_details = plot.PlotStageDetails(instruction_blocks={BRIEF: (
    "The job is The Starry Night, in New York. The building is modern, which means the security is too - "
    "pressure plates, motion sensors, a guard rotation with no gap in it. But modern buildings have "
    "service ducts, and service ducts have no cameras."
)})

THE_SCREAM = plot.PlotStage(description="The Scream, Oslo")
THE_SCREAM.plot_details = plot.PlotStageDetails(instruction_blocks={BRIEF: (
    "The job is The Scream, in Oslo. It has been stolen twice before, which means two things: the museum "
    "has learned, and someone will pay a great deal to own it a third time."
)})

# %% [markdown]
# ## Out and back
#
# Each heist needs two transitions: one out of the lair to begin it, one back to the lair when it is done.
# Six transitions for three jobs.
#
# Nothing here is new — these are the same `PlotTransition` objects as tutorial 1. What is new is the
# shape they make. Follow the arrows and you can go round forever, which is the point: the thief can rob
# the same museum twice, in either order, or ignore one entirely.

# %%

HEISTS = [MONA_LISA, STARRY_NIGHT, THE_SCREAM]

transitions = []
for heist in HEISTS:
    transitions.append(plot.PlotTransition(
        starting_stage=LAIR,
        ending_stage=heist,
        trigger_on_scenario=f"I decide to steal {heist.description}",
    ))
    transitions.append(plot.PlotTransition(
        starting_stage=heist,
        ending_stage=LAIR,
        trigger_on_scenario=f"I get away from {heist.description}, with or without the painting",
        transition_event="I return to the lair and put the job behind me, one way or the other.",
    ))

plot.add_single_plot(
    world=world,
    plot_stages=[LAIR, *HEISTS],
    plot_transitions=transitions,
    starting_stage=LAIR,
)

print(world.summary())
pathlib.Path("tutorial_plot_6_revisiting_stages.json").write_text(world.to_json())
