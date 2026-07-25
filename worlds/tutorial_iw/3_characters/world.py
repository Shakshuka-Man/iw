# %% [markdown]
# # Tutorial 3 — Characters
#
# In order to play a world, we need to play as a character in that world. Although you can leave this section empty
# when defining a world, when you actually play the world a default character will be generated, which probably won't
# make for as good of a play experience as if you play with a character whose backstory makes sense in the world.
#
# We will create three different options for the playable character. As we have two different skills in the
# world (Mechanics and Mental Resilience), two of the options each specialize in one of the two skills. The
# third spreads the same eight points evenly across both, so they are competent at everything and exceptional at
# nothing -- a different way to play rather than a weaker one.
# %%
import pathlib
import iw

world = iw.World(
    title="Bones in the Ocean",
    skills = ["Mechanics", "Mental Resilience"],
)

ENGINEER = iw.PossibleCharacter(
    name="Douglas Odell",
    description=(
        "A man of forty-three, formerly an engineer in the merchant marine until an incident he will not discuss "
        "ended his career at sea. Broad-shouldered, methodical, and quiet in the way of someone who learned long ago "
        "that speaking invites questions. He took the Rona posting because the Board doesn't ask for references and "
        "the sea is the only thing he knows. He is good with machines \u2014 patient, precise, able to coax life from "
        "seized metal \u2014 but he has always been poor at noticing the small wrong things until they are large wrong "
        "things. He sleeps heavily and dreams rarely, which he considers a blessing."
    ),
    skills={"Mechanics": 5, "Mental Resilience": 3},
)

NURSE = iw.PossibleCharacter(
    name="Ruth Kellerman",
    description=(
        "A woman of thirty-six who spent twelve years as a nurse in a sanatorium for shell-shocked soldiers before "
        "the funding was cut and the patients were sent elsewhere. She is familiar with minds that have come apart, "
        "which is both her armour and her curse \u2014 she will recognise the signs of her own unravelling, but "
        "recognition is not prevention. She is iron-willed, accustomed to long hours and grim work, and entirely "
        "unafraid of solitude. She is less comfortable with machinery, having had no training in it, and will need to "
        "learn the lighthouse's demands from the manuals left behind. She took the posting because she wanted silence "
        "after years of other people's screaming."
    ),
    skills={"Mechanics": 3, "Mental Resilience": 5},
)

CROFTER = iw.PossibleCharacter(
    name="Ewan Macrae",
    description=(
        "A young man of twenty-seven from a crofting family on Lewis, soft-spoken and sharp-eyed, raised on stories "
        "of selkies and the restless dead told without irony by people who believed them. He is attuned to the small "
        "wrongnesses of a place \u2014 the silence that falls too suddenly, the shadow that moves against the wind \u2014 in a "
        "way that will serve him and torment him in equal measure. He took the posting because his father's croft "
        "went under and there was nothing on Lewis for a youngest son with no trade but watchfulness. He knows boats, "
        "weather, and the sea's moods, and is competent enough with tools, but he has never been tested by true "
        "hardship alone, and privately fears he is not strong enough for what he cannot see."
    ),
    skills={"Mechanics": 4, "Mental Resilience": 4},
)

world.possibleCharacters.extend([ENGINEER, NURSE, CROFTER])

# %% [markdown]
# Although this world is mostly about isolation, there is one NPC that the player interact with: the boatman.
# %%
BOATMAN = iw.NPC(
    name="The boatman",
    names=["the boatman", "boatman", "ferryman"],
    one_liner="The boatman is a mysterious figure that arries every two weeks to bring supplies to Rona. He never speaks a word, not even to tell me his name.",
    detail=(
        "The boatman is a mysterious figure that may or may not be supernatural. He is tall, muscular, and usually "
        "stands perfectly still, giving him an intimidating presence.\n\n"
        "He arrives every two weeks, keeping to schedule no matter the weather. The sea birds seem uneasy around "
        "him, scattering whenever he gets near.\n\n"
        "He never speaks or reacts to anything I say. If I request something, he ignores my requests. However, "
        "whenever he arries he always provides me with exactly the supplies I need.\n\n"
        "It should be ambiguous whether he is human or some kind of supernatural entity. Something feels unusual "
        "about him, and his presence feels unnatural, but he never does anything that would not have a mundane "
        "explanation."
    ),
    appearance=(
        "The boatman is large and muscular. He has long hair and a weathered face. He always wears dark glasses "
        "that conceal his eyes, and a heavy coat that makes him appear even more imposing."
    ),
)
world.NPCs.append(BOATMAN)

# %% [markdown]
# ## Output
# With our player character options and NPC added, we can output the world and import the JSON into IW again.
# %%

print(world.summary())
pathlib.Path("bones_in_the_ocean_with_characters.json").write_text(world.to_json())
