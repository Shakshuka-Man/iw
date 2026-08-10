# Tutorial 1 — `iw`: the data model

This is the first of three tutorials. It covers `iw`, the layer that mirrors the engine's world format: the world itself, the cast, instruction blocks, keyword blocks, tracked items, triggers. All five build one world — a lighthouse on an uninhabited rock in the Outer Hebrides, an eighteen-month posting, and a keeper who will not be able to tell whether the island is haunted or they are simply coming apart. [Tutorial 2](tutorial-2-advanced.md) is what this is *worth* — the case for doing any of this in Python rather than in the engine's own editor. [Tutorial 3](tutorial-3-plot.md) covers `plot`, a compiler for story structure built on top of both.

Five worlds, each adding one idea to the last. **Every one of them is a notebook you can run in your browser** — nothing to install. This page is the same material as a single read-through.

Each notebook has the same three parts: an **input** (which world to start from), a **transformation** (the lesson), and an **output** (save the result). Leave the input alone to follow along, or point it at a world of your own and the lesson is applied to *that* instead.

| | notebook | the idea |
|---|---|---|
| 1 | `tutorial_iw_1_simple_world` | A simple world |
| 2 | `tutorial_iw_2_instruction_blocks` | Extra instruction blocks and keyword instruction blocks (EIBs and KIBs) |
| 3 | `tutorial_iw_3_characters` | Characters |
| 4 | `tutorial_iw_4_tracked_items` | Tracked items |
| 5 | `tutorial_iw_5_triggers` | Triggers |

## Tutorial 1 — A simple world

Creating a world is simple — all you need is a title and at least one skill, and in a pinch you can even
skip those:

```python
import pathlib
import iw

world = iw.World(
    title="A really simple world",
    skills=["Brawn", "Charisma"],
)
```

### Extracting the JSON

Once you have created your world, you can write it to a JSON that can then be imported into Infinite
Worlds and played. Run the cell below and a new file appears in the file browser on the left, containing
the JSON of the world.

```python
pathlib.Path("minimal_world.json").write_text(world.to_json())
```

### A world worth playing

However, although that world is functional, it is not very interesting. Let's instead go with a more
interesting premise: a psychological horror where the player is alone on a remote island, and has to
deal with their fraying sanity and supernatural elements.

A world is a plain object, so you can build it a field at a time — create an empty `iw.World()` and set
what you care about.

```python
world = iw.World()

# The title and description are shown to the player when they browse the list of worlds. They set
# expectations, but have no effect on the story itself.
world.title = "The Lighthouse"
world.description = (
    "This world is a psychological horror, where you play the solitary lighthouse keeper on an "
    "uninhabited island. As time goes on, the isolation drains your sanity, and your grip on reality "
    "weakens. Will you be able to survive, or will you meet the same fate as the previous lighthouse "
    "keeper?"
)

# The instructions are the AI's brief: what this world is, and how it should be run.
world.instructions = """This adventure is a psychological horror set on the island of Rona, an uninhabited island in the Outer Hebrides.

The sea around Rona hides rocks and reefs that have wrecked many ships over the centuries. Rona itself is little more than the largest of these rocky outcrops, a jumble of cliffs, windswept heather, and caves that are home to swarms of sea birds.

The weather is harsh and unforgiving. Storms are frequent, with gale force winds. Fog rolls in every morning, so thick you can't see more than arm's length away.

The main feature of Rona is the lighthouse. The lighthouse has stood for centuries, tended by a solitary lighthouse keeper. Living alone on this island takes a toll on these keepers, and those that finish their term come back changed - quieter, watchful, and haunted by nightmares. Many do not come back at all, their disappearance ruled as suicide.

I am the newly appointed lighthouse keeper of Rona. I have been appointed after the previous keeper, Alex Rennick, disappeared. My posting is for six months, and I will have to spend that time alone. I have no radio, no internet, and no contact with the outside world. My only human contact is with the boatman, if that can be called human contact. The boatman is a mysterious figure that I do not know anything about, not even his name. He arrives every two weeks, bringing all the supplies that I need to survive and maintain the lighthouse. No matter how much I talk to him, he never says a word back.

As I spend time on the island, with only the sea birds for company, my sanity will start fraying due to the isolation. I will start to have visual and auditory hallucinations, seeing or hearing things that I know are not real, cannot be possible.

Maintaining the lighthouse is a challenge. The machinery is ancient and difficult to run. As long as the light is running, my sanity remains intact and can even recover slowly. However, if the light ever goes out, my sanity will quickly deteriorate.

Over the centuries, several ships have been shipwrecked on the rocks near Rona, with hundreds of souls lost. The island is haunted by the spirits of these lost souls. These spirits are lonely and cold, and are drawn to me as the only living soul on the island, like moths drawn to a flame. The spirits are not malicious, but their attention and presence has negative effects on me - my sense of identity frays, my health suffers, and in extreme cases I may lose control of my body.

While the lighthouse is lit, I am kept safe from the spirits and I can recover my health and sanity. Whenever the lighthouse goes out, I will not be protected from the spirits.

The most important rule to remember is that the existence of the spirits should always be ambiguous. There should never be anything happening that confirms or denies that these spirits are real and are haunting me. Any effects of the spirits must have a mundane explanation. For example:
- Objects that are not where I expect them to be may have been moved by the spirits, or I may have just forgotten where I put them
- I may see or hear something supernatural, but I do not know if it is a spirit or something I am hallucinating in my isolation
- I may observe unusual activity or behavior in the sea birds, but I do not know if this is the birds being affected by the spirits, or me being unfamiliar with normal behavior of sea birds
- I may find unusual objects scattered around the island, but it is unclear if they are just wrack, or if they have supernatural origin
"""

# The background is the backstory the story opens on, set before the first turn begins.
world.background = """You had heard stories about Rona, and none of them were good.

Some say that this island is cursed. Some say that the spirits of lost sailors haunt the place. Some say that all those stories are superstitious hogwash, and it's just that being alone on an island for six months causes you to hallucinate. The only thing that everyone agrees on is that being the lighthouse keeper on Rona is a bad idea.

But when a bad job market and rising bills collide, the outcome was inescapable: You are now the lighthouse keeper for Rona, the most remote island in the Outer Hebrides.

You packed your bags, and took the flight to Stornoway. In the pre-dawn darkness, you made your way to the docks and met the boatman, your only human contact for the next six months. Large, muscular and silent, the man took you on board his ship and you left civilization behind. During the journey you tried to make conversation, but the man never spoke a word.

The journey took four hours, during which dawn broke. As the morning fog started to dissipate, you saw it looming above you: Rona Lighthouse, your home for the next six months.
"""

# The first action is the opening move the story starts from, written as the player would act it. The
# engine seeds the first turn from it.
world.firstInput = "I step off the boat, onto the beach, feeling the shale crunch underfoot. The boatman silently unloads my bags and supplies. While he unloads, I take some time to take in my surroundings."

# Every world needs at least one skill, and every playable character carries a level in each. Ours are the
# two axes this story runs on: keeping the machine alive, and keeping yourself alive.
world.skills = ["Mechanics", "Mental Resilience"]

print(world.summary())
```

Save it the same way as before. Name the file after the world, not after this tutorial — a `.json`
ends up in your downloads folder with no tree around it, so `the_lighthouse.json` says what it is and
`tutorial_iw_1_simple_world.json` does not. This is the file you paste into Infinite Worlds.

```python
pathlib.Path("the_lighthouse.json").write_text(world.to_json())
```

### Changing a world you already have

We can also load an existing world definition in order to make changes to it. For example, we might
decide that we want to rename our world from `The Lighthouse` to `Bones in the Ocean`. Instead of having
to recreate the world from scratch, we can load the JSON we just saved, make our changes, and write it
back out under the new name.

```python
world = iw.World.from_json(pathlib.Path("the_lighthouse.json").read_text())
world.title = "Bones in the Ocean"
pathlib.Path("bones_in_the_ocean.json").write_text(world.to_json())

print(f"reloaded and renamed to: {world.title!r}")
```

### Where to go next

We have only covered the basics of world editing here. To learn more:

- The **`iw` reference** at `docs/iw.md` lists every object, every attribute, the type it takes and what
  it is for, plus every enum member with a line of code using it. Its structure is generated from the
  library, so it is never out of date.
- Or carry on with the rest of these tutorials. **Next:** `tutorial_iw_2_instruction_blocks` — the
  island itself, and the keyword blocks that make it deep for free.

## Tutorial 2 — Extra instruction blocks and keyword instruction blocks (EIBs and KIBs)

Often, you want to provide instructions to the storyteller AI that are not relevant every turn.
If they were to be provided every turn, then this would potentially cost a lot of credits.
Keyword instruction blocks can be used to ensure that the storyteller AI gets these instructions
when they are relevant, but save credits when they are not relevant.

In this world, we want to have keyword instruction blocks that give details on the different shipwrecks around
Rona. They're not important enough to be relevant to every turn, but they are important enough that we want
to provide details if they were to ever come up.

If we just have the keyword instruction blocks, then we will run into a different problem - the storyteller
AI does not know that the KIBs exist, and so the shipwrecks will never come up, and so the KIBs will never fire.
We get around this by adding an extra instruction block that gives a brief description of the KIBs - enough to
generate a turn mentioning them, but not enough to be a significant drain on credits

```python
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")
```

Each wreck is a keyword instruction block (a KIB): an `iw.LoreBookEntry` with a `keywords` list and some
`content`, added to `world.loreBookEntries`. The storyteller AI is given the content only when the recent text
matches one of the keywords, so we can give detailed descriptions without worry about bloating the input costs.

```python
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
```

On their own the KIBs never fire: the AI does not know the wrecks exist, so it never mentions them, so
the player never asks. We fix that with one extra instruction block (an EIB), always in context. It
lists the wrecks, a line each — enough for the AI to raise one in passing — but holds no detail, so it
stays cheap. When the AI mentions a wreck and the player asks, the matching KIB loads the rest.

```python
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
```

### Output
With the shipwrecks added, we can export the world again and load it into IW to see the results.

```python
print(world.summary())
pathlib.Path("bones_in_the_ocean_with_shipwrecks.json").write_text(world.to_json())
```

## Tutorial 3 — Characters

In order to play a world, we need to play as a character in that world. Although you can leave this section empty
when defining a world, when you actually play the world a default character will be generated, which probably won't
make for as good of a play experience as if you play with a character whose backstory makes sense in the world.

We will create three different options for the playable character. As we have two different skills in the
world (Mechanics and Mental Resilience), two of the options each specialize in one of the two skills. The
third spreads the same eight points evenly across both, so they are competent at everything and exceptional at
nothing -- a different way to play rather than a weaker one.

```python
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
```

Although this world is mostly about isolation, there is one NPC that the player interact with: the boatman.

```python
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
```

### Output
With our player character options and NPC added, we can output the world and import the JSON into IW again.

```python
print(world.summary())
pathlib.Path("bones_in_the_ocean_with_characters.json").write_text(world.to_json())
```

## Tutorial 4 — Tracked items

So far, we have been constructing a world about the player's fraying sanity, and how it will change over time.
However, before now we have been relying on the storyteller AI's vibes to keep track of this between turns.
In the interest of keeping the player's sanity consistent as the world progresses, we can introduce a tracked
item to track the player's sanity.

We will be able to take advantage of this even further in the next tutorial.

```python
import pathlib
import iw

world = iw.World(title="Bones in the Ocean")
```

We will have sanity range from 0 to 100, where 100 is completely sane, starting at 100.
It should be easy for sanity to decrease, and hard for it to increase.
Mental Resilience will decrease the rate it decreases by.
We will set it to be visible to the AI only, so the player is never certain how sane they are.

```python
SANITY = iw.TrackedItem(
    name="Sanity",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    initialValue="100",
    description=(
        "A measure of how sane I am. 100 represents optimal mental health, and 0 represents complete mental breakdown."
    ),
    updateInstructions=(
        "Whenever dawn breaks, if I was able to keep the lighthouse operational throughout the night, increase this by 5 to "
        "a maximum of 100.\n"
        "Whenever the lighthouse fails during the night, reduce this by <<10-$player.skills.mental_resilience>> to a minimum of 0.\n"
    ),
    autoUpdate=True,
)

DAYS_ON_ISLAND = iw.TrackedItem(
    name="Days On The Island",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.EVERYONE,
    initialValue="0",
    description="How many days I have been on the island of Rona",
    updateInstructions=(
        "Whenever dawn breaks, increase this by 1."
    ),
    autoUpdate=True,
)

world.trackedItems.extend([SANITY, DAYS_ON_ISLAND])

print(world.summary())
pathlib.Path("bones_in_the_ocean_with_tracked_items.json").write_text(world.to_json())
```

## Tutorial 5 — Triggers

In the last tutorial, we went over how to create tracked items to track how the player's sanity changes over time
Now, we will set up some triggers so we can change how the world operates as the player's sanity changes.

```python
import pathlib
import iw

world = iw.World(
    title="Bones in the Ocean",
)
```

We will recreate a simpler version of the sanity tracked item from last tutorial.
We will also create a new instruction block that we want to change based on the player's sanity
We will also want a trigger that actually ends the game after the player has survived 6 months.

```python
SANITY = iw.TrackedItem(name="Sanity", dataType=iw.TrackedItemDataType.NUMBER)
world.trackedItems.append(SANITY)
DAYS_ON_ISLAND = iw.TrackedItem(name="Days on the Island", dataType=iw.TrackedItemDataType.NUMBER)
world.trackedItems.append(DAYS_ON_ISLAND)
SANITY_INSTRUCTIONS = iw.InstructionBlock(name="Sanity Instructions")
world.instructionBlocks.append(SANITY_INSTRUCTIONS)
```

We will set up victory and defeat conditions - we win if we survive the 6 months and are taken off the island, and we lose if we die.

```python
world.victoryCondition = iw.VictoryDefeatCondition(
    condition="I am taken off the island after surviving six months.",
    text=("It has been the longest six months of your life, but you have survived. As you head back to the mainland, you know that even though you have left Rona, it has left its mark on you and you will never be the same again."),
)
world.defeatCondition = iw.VictoryDefeatCondition(
    condition="I die.",
    text="Your adventure ends here - yet another lighthouse keeper claimed by Rona.",
)
```

We will also set up some helper triggers - when 180 days are reached, a boat arrives to pick up the player.
We will also add an alternate defeat condition - when sanity reaches 0

Note that by default, triggers can get a bit wordy - we have to repeat the tracked item id a couple times, and threre is a lot of boilerplate.
There are more efficient ways of doing this, and we will explore the more efficient ways in the advanced tutorial.

```python
world.triggerEvents.append(iw.TriggerEvent(
    name="Boat comes to pick me up",
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=DAYS_ON_ISLAND.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "180",
                "trackedItemID": DAYS_ON_ISLAND.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[iw.TriggerEffect(
        type=iw.EffectType.TELL_AI,
        data=(
            "I have served my full six months. The boatman arrives out of the fog to take "
            "me off Rona and back to the mainland."
        ),
    )],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity defeat",
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "0",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.SHOW_MESSAGE,
            data=(
                "The last traces of your sanity slip away. When the boatman makes his next trip to the "
                "island, he finds it empty. You are never seen or heard from again."
            ),
        ),
        iw.TriggerEffect(type=iw.EffectType.ENDS_GAME, data=False),
    ],
))
```

For each band of sanity, we will create a trigger that sets the sanity instruction block to the appropriate value.
As the player can move between bands multiple times, we will set up the triggers to fire multiple times.
For now we will do it in the lengthy but straightforward way - in the advanced tutorial, we will see how to do this programatically

```python
world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 91-100",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "91",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "100",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I spend the daylight hours walking the island and resting from the night's work. The "
                "emptiness of the place unsettles me — no voices, no company, only rock and sea and wind. The "
                "birds, the shore, and the water are exactly as they should be, and my unease is only the "
                "ordinary loneliness of a person left alone.\n"
                "\n"
                "Night: The night is a constant fight to keep the lighthouse working. The machinery fails "
                "again and again, and I move from one problem to the next without rest, forcing the light to "
                "stay lit until morning. By dawn I am exhausted, and the work has taken everything I have."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 81-90",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "81",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "90",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I use the day to explore the island and recover from the night. Being this alone is "
                "strange, and the silence presses on me, but I notice nothing out of the ordinary. Once in a "
                "while something small catches my attention, and I find the plain reason for it and think no "
                "more of it.\n"
                "\n"
                "Night: The night is spent keeping the lighthouse running, and it does not make it easy. It "
                "breaks down often and demands my attention through the dark hours, and I work hard to keep "
                "the light burning until dawn. The effort leaves me worn out."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 71-80",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "71",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "80",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daytime I walk the island and rest. The loneliness has an eerie edge to it, and "
                "now and then I hear a sound I cannot place or see the birds moving in a way that seems wrong. "
                "I can usually explain these things to myself, though I am not always sure the explanation is "
                "right.\n"
                "\n"
                "Night: At night I work to keep the lighthouse operational. It still fails frequently, and "
                "much of the dark is spent on repairs to keep the light lit. The task is demanding and I feel "
                "it by morning."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 61-70",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "61",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "70",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: I spend the day out on the island and resting from the night. The solitude feels strange "
                "in a way I cannot quite name, and I sometimes notice things I cannot easily explain — a noise "
                "with no source, a shape at the edge of my sight that is gone when I look. The moments pass, "
                "and I tell myself they were nothing.\n"
                "\n"
                "Night: The night is given over to the lighthouse, which needs regular attention to keep "
                "running. Something goes wrong often enough that I cannot rest for long, and I work through "
                "the dark to keep the light burning. Now and then, in the quiet between tasks, I have the "
                "sense that I am not alone."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 51-60",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "51",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "60",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: During the day I explore and try to rest, but the island no longer feels entirely empty "
                "to me. I hear sounds I cannot find the source of, and I come across things on the shore and "
                "among the rocks that I do not remember from before. Some of it I can explain, and some of it "
                "I cannot, and I have begun to look twice at what is around me.\n"
                "\n"
                "Night: At night I keep the lighthouse lit, and it still gives me trouble, though I can manage "
                "it. Between the repairs, in the dark at the top of the tower, I find the light itself holds "
                "my attention more than it used to. I catch myself pausing to look into it before I turn back "
                "to the work."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 41-50",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "41",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "50",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: The day is filled with things I cannot account for. I hear voices and footsteps when I "
                "know I am alone, I see figures that vanish when I turn toward them, and the sea birds gather "
                "and move in patterns that seem to mean something I cannot read. I cannot tell whether any of "
                "it is real or whether my mind is making it, and I have no way to be sure.\n"
                "\n"
                "Night: At night the lighthouse needs little from me, and the light draws me to it. I spend "
                "long stretches simply looking into it, and I find it steadying in a way I cannot explain. The "
                "work I ought to do falls away while I stand there, and the hours pass without my noticing."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 31-40",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "31",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "40",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daylight I wander the island and find it changed. I see and hear people who are "
                "not there, the birds wheel in shapes that feel deliberate, and I keep finding strange objects "
                "washed up along the shore that I cannot account for. I can no longer reliably tell what is "
                "truly in front of me and what I am imagining.\n"
                "\n"
                "Night: The lighthouse asks little of me, and I give myself over to the light. I stand before "
                "it for hours, held by it, unable and unwilling to look away. It comforts me, and the night "
                "goes by while I watch it, the way one might watch something that is calling to them."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 21-30",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "21",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "30",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: My days are full of things that may not be real. Figures, voices, and the feeling of "
                "others close by are with me constantly, the patterns in the birds seem to carry a meaning "
                "meant for me, and the shore offers up objects I cannot explain. I lose track of time and "
                "cannot always say what I have done or how I came to be where I am.\n"
                "\n"
                "Night: At night the light holds me completely. I spend the dark hours before it, staring into "
                "it as though it were calling me, and I struggle to pull myself away. The lighthouse seems to "
                "run without my help, and I do nothing but watch the light, hour after hour, until the day "
                "returns."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 11-20",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "11",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "20",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: In the daylight I can no longer trust what I perceive. I see whole events and people in "
                "full detail that may exist only in my mind, the birds move in patterns I am certain are meant "
                "for me, and the shore is strewn with things I cannot explain. I forget my own actions and "
                "lose long stretches of time, and I rarely know what is real.\n"
                "\n"
                "Night: The light is all there is at night. I stand before it, unable to look away, and the "
                "hours dissolve while I watch it draw me in."
            )},
        ),
    ],
))

world.triggerEvents.append(iw.TriggerEvent(
    name="Sanity 1-10",
    canTriggerMoreThanOnce=True,
    triggerConditions=[
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_LEAST,
            data={
                "inequality": iw.Inequality.AT_LEAST,
                "requiredValue": "1",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
        iw.TriggerCondition(
            type=iw.ConditionType.ON_TRACKED_ITEM,
            category="condition",
            trackedItemID=SANITY.id,
            inequality=iw.Inequality.AT_MOST,
            data={
                "inequality": iw.Inequality.AT_MOST,
                "requiredValue": "10",
                "trackedItemID": SANITY.id,
                "textComparison": "contains",
            },
        ),
    ],
    triggerEffects=[
        iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": SANITY_INSTRUCTIONS.id, "content": (
                "Day: My days have no firm shape. I cannot separate what is real from what is not — the "
                "figures, the birds, the things on the shore all arrive the same way, and I do not know what "
                "is happening, what I have done, or where on the island I am. At times I am not in control of "
                "my own body, and I find myself moving and acting without deciding to.\n"
                "\n"
                "Night: At night the light consumes me. I stand before it and cannot leave it, and there is "
                "nothing else — no work, no thought, no sense of time, only the light and the pull of it. I "
                "watch it until the dark ends, or until I no longer know whether the dark has ended, held by "
                "it as if it were a voice I have to answer."
            )},
        ),
    ],
))
```

### Output
Now we have added the triggers, we can output the world
We can then look at the advanced triggers to see how to do these things programatically

```python
print(world.summary())
pathlib.Path("bones_in_the_ocean_with_triggers.json").write_text(world.to_json())
```
