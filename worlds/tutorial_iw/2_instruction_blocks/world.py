# %% [markdown]
# # Tutorial 2 — Extra instruction blocks and keyword instruction blocks (EIBs and KIBs)
#
# Often, you want to provide instructions to the storyteller AI that are not relevant every turn.
# If they were to be provided every turn, then this would potentially cost a lot of credits.
# Keyword instruction blocks can be used to ensure that the storyteller AI gets these instructions
# when they are relevant, but save credits when they are not relevant.
#
# In this world, we want to have keyword instruction blocks that give details on the different shipwrecks around
# Rona. They're not important enough to be relevant to every turn, but they are important enough that we want
# to provide details if they were to ever come up.
#
# If we just have the keyword instruction blocks, then we will run into a different problem - the storyteller
# AI does not know that the KIBs exist, and so the shipwrecks will never come up, and so the KIBs will never fire.
# We get around this by adding an extra instruction block that gives a brief description of the KIBs - enough to
# generate a turn mentioning them, but not enough to be a significant drain on credits

# %%
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")

# %% [markdown]
# Each wreck is a keyword instruction block (a KIB): an `iw.LoreBookEntry` with a `keywords` list and some
# `content`, added to `world.loreBookEntries`. The storyteller AI is given the content only when the recent text
# matches one of the keywords, so we can give detailed descriptions without worry about bloating the input costs.

# %%
world.loreBookEntries.extend([
    iw.LoreBookEntry(
        name="Wreck: Cormorant (1888)",
        keywords=["1888", "cormorant", "the cormorant"],
        content=(
            "The Cormorant, an iron steam coaster, lost on the reef off Rona in 1888. 20 souls lost.\n"
            "Of note aboard: Master Donald Rankin; Dr. Aeneas Croll, district physician; Miss Isobel Frew, a "
            "young woman travelling to her wedding.\n"
            "The Cormorant was an iron-hulled steam coaster of the modern sort, running a regular scheduled "
            "trade around the north and west coasts — coal, general cargo, the mail, and a few passengers, "
            "threading the islands on a timetable in a way the old sailing traders never could. By her time "
            "the lighthouse stood on Rona, tended and lit, and her loss was the first the light was built to "
            "prevent and did not. She carried fourteen crew and, that final trip, nine passengers, under a "
            "master named Donald Rankin who had run the route for eleven years and knew every rock on it by "
            "name. Among the passengers were Dr. Aeneas Croll, a district physician well known along the "
            "coast, and a young woman, Isobel Frew, travelling to the mainland to be married.\n"
            "\n"
            "She was lost close under Rona on a night of thick fog, and here the ambiguity turns on the "
            "lighthouse itself. The keeper of the day swore, in the inquiry that followed, that the light had "
            "burned steady and true all night, exactly as his log recorded. The three survivors swore with "
            "equal conviction that they had seen no light at all in the fog — and one of them, a deckhand, "
            "insisted that they had seen a light, and steered by it, and that it had been in the wrong place, "
            "drawing them in toward the rocks rather than warning them off.\n"
            "\n"
            "The inquiry could not reconcile a keeper's sworn word and log against three sworn survivors, and "
            "recorded the loss as due to fog and an error of navigation — while wondering, in its margins, "
            "whether the keeper had let the lamp fail and lied to save his post, or whether frightened men in "
            "fog can be trusted on anything at all. Both remain possible. Neither was ever proved. Twenty "
            "people drowned, the bride Isobel Frew and the doctor Croll among them, a mile from a light that "
            "either was or was not shining.\n"
            "\n"
            "The one further fact the record holds is a small and cold one: the keeper of that night finished "
            "his six months, was relieved, and went home — and the relief crew noted, as such things were "
            "sometimes noted, that he came back very much changed."
        ),
    ),
    iw.LoreBookEntry(
        name="Wreck: Freya (1871)",
        keywords=["1871", "freya", "the freya"],
        content=(
            "The Freya, a Norwegian timber barque, lost on the reef off Rona in 1871. 14 souls lost.\n"
            "Of note aboard: Captain Anders Holt; Nils Holt, his son, ship's boy, aged twelve.\n"
            "The Freya was a Norwegian barque in the Baltic timber trade, carrying a full cargo of sawn deals "
            "bound south for the building yards, worked by a crew of fourteen out of a small port near Bergen. "
            "Among them was her master, Captain Anders Holt, and his own son Nils, a boy of twelve making an "
            "early voyage as ship's boy in the way of seafaring families. They were foreigners in these "
            "waters, following a coasting route south, and Rona's reefs were not a danger they knew well. She "
            "struck them on a black night of rising wind and was holed and lost with all hands.\n"
            "\n"
            "What sets the Freya apart, and what has kept her in the stories, is what happened after she "
            "struck. A timber ship does not always sink; her cargo of deals can hold a broken hull awash long "
            "after the sea should have claimed it, and the Freya did not go down. She was seen for three days "
            "afterward by fishing boats and by a passing coaster — low in the water, dismasted, "
            "half-submerged, but afloat, drifting slowly with the tide off Rona, refusing to sink. And more "
            "than one of those who saw her swore there was a figure at her wheel: a man standing at the helm "
            "of a dead ship awash to her rails, unmoving, as the hulk turned in the current.\n"
            "\n"
            "The explanation is not hard to reach. A waterlogged timber ship will float for days; the \"figure "
            "at the wheel\" was a tangle of rigging and canvas, or a body lashed or caught upright, or the eye "
            "of a frightened man making a shape out of wreckage across a mile of grey water. When the Freya "
            "finally went down, or drifted off beyond sight, the figure went with her, and no one came close "
            "enough to say what it truly was. Fourteen Norwegians drowned that night, the boy Nils among them, "
            "far from home in a sea they did not know — and for three days their ship would not lie down and "
            "be dead."
        ),
    ),
    iw.LoreBookEntry(
        name="Wreck: Aurora K (1973)",
        keywords=["1973", "aurora k", "the aurora k"],
        content=(
            "The Aurora K, a steel side trawler, lost on the reef off Rona in 1973. 12 souls lost.\n"
            "Of note aboard: Skipper Robert Hume; Mate Iain Tolmie; a crew of experienced trawlermen.\n"
            "The Aurora K is the most recent of Rona's wrecks, and the most unsettling for being modern — a "
            "steel-hulled side trawler with radar, radio, and echo-sounder, crewed by twelve experienced "
            "fishermen who had every instrument the sea had yet devised to keep them off the rocks. She was "
            "working the grounds north of Lewis in winter, no different from a hundred trips before, under a "
            "skipper, Robert Hume, reckoned a careful and able man, with a trusted mate, Iain Tolmie, beside "
            "him. That a vessel so equipped, so crewed, could end on the same reefs that took sailing ships "
            "two centuries dead is the thing no one has ever comfortably explained.\n"
            "\n"
            "What is known comes from her radio. She made ordinary contact through the evening, and then, "
            "late, sent a broken transmission that those who heard it have never agreed on. The official "
            "transcript records a report of fog and a request for a position check, cut off mid-sentence. The "
            "men who were listening on the coast station and on other boats remember it less tidily: a "
            "skipper's voice gone oddly flat and slow; a mention of a light — \"steering for the light,\" more "
            "than one of them swears he heard, though the light Hume should have been steering away from — "
            "and, under the words, before the set went dead, a sound that the transcript does not note and "
            "that none of those who heard it will describe.\n"
            "\n"
            "The inquiry found fog, a misread radar return, and an error of navigation, which is very likely "
            "the whole of it. Modern instruments do not save men who trust them wrongly; radar returns are "
            "misread; fog kills the well-equipped as readily as the old sailing ships, and the rocks off Rona "
            "have never cared how a vessel was fitted out. She was found broken on the reef with all twelve "
            "hands lost, Hume and Tolmie among them. Whatever Hume was steering for, if he was steering for "
            "anything, went down with him — and the Aurora K, being the newest and the nearest, is the wreck "
            "whose drowned a modern keeper may feel could still reach out and touch him, because they died in "
            "a world he remembers."
        ),
    ),
])

# %% [markdown]
# On their own the KIBs never fire: the AI does not know the wrecks exist, so it never mentions them, so
# the player never asks. We fix that with one extra instruction block (an EIB), always in context. It
# lists the wrecks, a line each — enough for the AI to raise one in passing — but holds no detail, so it
# stays cheap. When the AI mentions a wreck and the player asks, the matching KIB loads the rest.

# %%
world.instructionBlocks.append(iw.InstructionBlock(
    name="The wrecks",
    content=(
        "There are countless wrecks around Rona. The most notable ones are:\n"
        "- Cormorant (1888): The first wreck the light was meant to prevent — and the keeper swore the lamp "
        "was burning, while the living swore it dark.\n"
        "- Freya (1871): She struck by night, and was seen for three days afterward — drifting, awash, a "
        "figure at her wheel.\n"
        "- Aurora K (1973): The most recent dead: a modern ship with every instrument, lost on the same rocks "
        "as the sailing ships, and her last words were \"steering for the light.\""
    ),
))

# %% [markdown]
# ## Output
# With the shipwrecks added, we can export the world again and load it into IW to see the results.

# %%
print(world.summary())
pathlib.Path("bones_in_the_ocean_with_shipwrecks.json").write_text(world.to_json())
