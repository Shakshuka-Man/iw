# %% [markdown]
# # Plot tutorial 3 — Branching and reconverging
#
# In the previous tutorial, we looked at a straightforward linear plot. But most plots are not linear - they branch,
# they diverge, they converge again, and they can even loop. The plot engine handles all of these.
#
# In this example, we are going to construct a simple detective story that branches depending on how the player
# wants to approach the case. The plot will branch according to the following diagram:
#
# ```
#                  ┌─ WITNESSES ─┐
# INVESTIGATION ───┼─ EVIDENCE ──┼──▶ SUSPECT ──┬─"turn them in"───▶ JUSTICE
#                  └─ INFORMANT ─┘              └─"keep the loot"──▶ CORRUPTION
# ```
#

# %%
import pathlib
import iw
from iw import plot

world = iw.World(
    title="The Blackwood Theft",
    instructions="I am a detective investigating the theft of a priceless artifact from Blackwood House.",
)

plot_instructions = iw.InstructionBlock(name="Plot stage specific instructions")
world.instructionBlocks.append(plot_instructions)

# %% [markdown]
# ## The opening
#
# INVESTIGATION is the starting stage -- nothing transitions into it. From here the detective can open the
# case along any of three lines of inquiry.

# %%
INVESTIGATION = plot.PlotStage(description="Opening the case")
INVESTIGATION.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am a detective newly assigned to a theft at Blackwood House: a priceless jade nightingale, gone "
        "from a locked study. I can open the case along one of three lines -- question the household, comb "
        "the physical evidence, or lean on a street informant."
})

# %% [markdown]
# ## Divergence
#
# We can easily have a branching transition out of the initial investigation by setting up multiple `PlotTransition`
# objects, each of which starts from the same stage.

# %%
WITNESSES = plot.PlotStage(description="Working the household")
TO_WITNESSES = plot.PlotTransition(
    starting_stage=INVESTIGATION, ending_stage=WITNESSES,
    trigger_on_scenario="I start questioning the household",
)
WITNESSES.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am working the household -- taking statements, checking alibis, catching the small "
        "contradictions between them. It is slow going, but a name is beginning to surface."
})

EVIDENCE = plot.PlotStage(description="Combing the evidence")
TO_EVIDENCE = plot.PlotTransition(
    starting_stage=INVESTIGATION, ending_stage=EVIDENCE,
    trigger_on_scenario="I start combing the physical evidence",
)
EVIDENCE.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am in the study with what the scene gave up -- the forced case, a single smudged print, fibres "
        "on the sill, the timeline of the evening. Piece by piece it is pointing somewhere."
})

INFORMANT = plot.PlotStage(description="Working an informant")
TO_INFORMANT = plot.PlotTransition(
    starting_stage=INVESTIGATION, ending_stage=INFORMANT,
    trigger_on_scenario="I start leaning on a street informant",
)
INFORMANT.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I am working my informant in the back rooms of the city, trading favours and cash for whispers. "
        "He knows who has been moving stolen art; it is a matter of patience before he says the name."
})

# %% [markdown]
# ## Reconvergence
#
# In order to make the plot branches converge again, we can give a list of `PlotStage` objects as `starting_stage`
# instead of a single object. The plot engine will allow this trigger to fire from any of the starting stages.

# %%
SUSPECT = plot.PlotStage(description="They have found the thief")
TO_SUSPECT = plot.PlotTransition(
    starting_stage=[WITNESSES, EVIDENCE, INFORMANT], ending_stage=SUSPECT,
    trigger_on_scenario="I identify the thief and bring them in",
    transition_event=(
        "The threads pull together into one face: Julian Blackwood, the collector's own estranged nephew. "
        "I find him within the day, the jade nightingale still in his rooms."
    ),
)
SUSPECT.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions:
        "I have identified Julian Blackwood as the thief, and found the jade nightingale in his possession. "
        "He is frightened, desperate to make this all go away quietly. He is also rich, and I could easily "
        "turn the screws on him to get rich, if I was willing to give up my principles."
})

# %% [markdown]
# ## Two ways to end it
#
# We fork again for the different kinds of ending.

# %%
JUSTICE = plot.PlotStage(description="The honest ending")
TO_JUSTICE = plot.PlotTransition(
    starting_stage=SUSPECT, ending_stage=JUSTICE,
    trigger_on_scenario="I turn Julian in to face justice",
    end_game=True, can_continue=False,
    transition_event="I book Julian Blackwood and log the nightingale into evidence. The case closes clean.",
)
JUSTICE.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions: "I turned the thief in and returned what he took. The case is closed, honestly."
})

CORRUPTION = plot.PlotStage(description="The crooked ending")
TO_CORRUPTION = plot.PlotTransition(
    starting_stage=SUSPECT, ending_stage=CORRUPTION,
    trigger_on_scenario="I take the nightingale for myself and let Julian walk",
    end_game=True, can_continue=False,
    transition_event=(
        "I let Julian go, and the jade nightingale goes home with me. The file records an unsolved theft, "
        "and no one thinks to search the detective's own shelves."
    ),
)
CORRUPTION.plot_details = plot.PlotStageDetails(instruction_blocks={
    plot_instructions: "I let the thief walk and kept the prize for myself. The case is closed, dishonestly."
})

# %%
plot.add_plot(
    world=world,
    plot_stages=[INVESTIGATION, WITNESSES, EVIDENCE, INFORMANT, SUSPECT, JUSTICE, CORRUPTION],
    plot_transitions=[TO_WITNESSES, TO_EVIDENCE, TO_INFORMANT, TO_SUSPECT, TO_JUSTICE, TO_CORRUPTION],
)

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_plot_3_branching.json").write_text(world.to_json())

