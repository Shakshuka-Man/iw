"""The cast, as a subsystem in a file of its own: the world's two skills, the three playable characters,
and the single NPC. Lifted from basic tutorial 3, then re-authored in the web UI and brought back here.

The three keepers are deliberately not symmetrical. Two are specialists -- one who can keep the machine
running, one who can keep herself intact -- and the third splits the same total evenly, competent at both and expert in neither. Each carries
their own portrait and the prompt that produced it, so they are recognisably different people on the
character-select screen rather than three names.
"""

import iw

# The two axes this story runs on: keeping the machine alive, and keeping yourself alive. Every playable
# character carries a level in each.
SKILLS = ["Mechanics", "Mental Resilience"]

# The machinist. Strong on Mechanics, and sleeps too heavily to notice what the island does at night.
ENGINEER = iw.PossibleCharacter(
    name="Douglas Odell",
    description=(
        "A man of forty-three, formerly an engineer in the merchant marine until an incident he will not discuss "
        "ended his career at sea. Broad-shouldered, methodical, and quiet in the way of someone who learned long "
        "ago that speaking invites questions. He took the Rona posting because the Board doesn't ask for "
        "references and the sea is the only thing he knows. He is good with machines \u2014 patient, precise, able to "
        "coax life from seized metal \u2014 but he has always been poor at noticing the small wrong things until they "
        "are large wrong things. He sleeps heavily and dreams rarely, which he considers a blessing."
    ),
    skills={"Mechanics": 5, "Mental Resilience": 3},
    portrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/Ss0qaESczt.webp",
    fullSizePortrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/VvxsiNRXWr.webp",
    portraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/Ss0qaESczt.webp"],
    fullSizePortraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/VvxsiNRXWr.webp"],
    portraitPromptDetails=iw.PortraitPromptDetails(
        illustrSubject="Douglas Odell",
        illustrAppearance="a 43 year old male Scottish former marine engineer with grey-green eyes, weathered ruddy skin, and short-cropped dark brown hair flecked with grey",
        illustrClothes="heavy wool fisherman's jumper, dark oilskin trousers",
        illustrSetting="inside a lighthouse keeper's quarters with whitewashed stone walls, a small iron stove, and a single window showing grey sea under overcast sky during daytime, psychological horror, atmospheric, muted colors, isolated",
        illustrExpressionPosition="calm",
        illustrGenre="psychological horror, atmospheric, muted colors, isolated",
        illustrIsCharacter=True,
    ),
)

# The one who has watched minds come apart before. Strong on Mental Resilience -- she will
# recognise her own unravelling, which is armour and curse at once.
NURSE = iw.PossibleCharacter(
    name="Ruth Kellerman",
    description=(
        "A woman of thirty-six who spent twelve years as a nurse in a sanatorium for shell-shocked soldiers "
        "before the funding was cut and the patients were sent elsewhere. She is familiar with minds that have "
        "come apart, which is both her armour and her curse \u2014 she will recognise the signs of her own "
        "unravelling, but recognition is not prevention. She is iron-willed, accustomed to long hours and grim "
        "work, and entirely unafraid of solitude. She is less comfortable with machinery, having had no training "
        "in it, and will need to learn the lighthouse's demands from the manuals left behind. She took the "
        "posting because she wanted silence after years of other people's screaming."
    ),
    skills={"Mechanics": 3, "Mental Resilience": 5},
    portrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/Q5eKLDS5DX.webp",
    fullSizePortrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/MLG5mZ2HdI.webp",
    portraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/Q5eKLDS5DX.webp"],
    fullSizePortraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/MLG5mZ2HdI.webp"],
    portraitPromptDetails=iw.PortraitPromptDetails(
        illustrSubject="Ruth Kellerman",
        illustrAppearance="a 36 year old female Scottish nurse with grey-green eyes, fair freckled skin, and dark brown hair pulled back in a severe low bun",
        illustrClothes="heavy wool cardigan over a plain grey blouse, dark woollen skirt",
        illustrSetting="standing at the base of a weathered stone lighthouse on a barren windswept island under an overcast sky during daytime, gothic, atmospheric, realistic, muted tones",
        illustrExpressionPosition="calm",
        illustrGenre="gothic, atmospheric, realistic, muted tones",
        illustrIsCharacter=True,
    ),
)

# The generalist: competent at both, expert in neither, raised on stories nobody taught him to
# disbelieve. His gift and his affliction is that he notices things.
CROFTER = iw.PossibleCharacter(
    name="Ewan Macrae",
    description=(
        "A young man of twenty-seven from a crofting family on Lewis, soft-spoken and sharp-eyed, raised on "
        "stories of selkies and the restless dead told without irony by people who believed them. He is attuned "
        "to the small wrongnesses of a place \u2014 the silence that falls too suddenly, the shadow that moves against "
        "the wind \u2014 in a way that will serve him and torment him in equal measure. He took the posting because "
        "his father's croft went under and there was nothing on Lewis for a youngest son with no trade but "
        "watchfulness. He knows boats, weather, and the sea's moods, and is competent enough with tools, but he "
        "has never been tested by true hardship alone, and privately fears he is not strong enough for what he "
        "cannot see."
    ),
    skills={"Mechanics": 4, "Mental Resilience": 4},
    portrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/9pmKmZhZnc.webp",
    fullSizePortrait="https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/CJgPMqTA5e.webp",
    portraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/9pmKmZhZnc.webp"],
    fullSizePortraitOptions=["https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/CJgPMqTA5e.webp"],
    portraitPromptDetails=iw.PortraitPromptDetails(
        illustrSubject="Ewan Macrae",
        illustrAppearance="a 27 year old male Scottish lighthouse keeper with grey-green eyes, fair weathered skin, and short dark brown hair tousled by wind",
        illustrClothes="heavy navy wool sweater, dark oilskin jacket, worn brown corduroy trousers",
        illustrSetting="standing on a windswept rocky headland beside a tall whitewashed lighthouse, grey overcast sky, rough sea in the background, during daytime, gothic, atmospheric, realist",
        illustrExpressionPosition="calm",
        illustrGenre="gothic, atmospheric, realist",
        illustrIsCharacter=True,
    ),
)

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

def install_into(world: iw.World) -> None:
    """Add the cast *to* `world`: the two skills every character carries a level in, the three playable
    characters, and the boatman."""
    world.skills.extend(SKILLS)
    world.possibleCharacters.extend([ENGINEER, NURSE, CROFTER])
    world.NPCs.append(BOATMAN)
