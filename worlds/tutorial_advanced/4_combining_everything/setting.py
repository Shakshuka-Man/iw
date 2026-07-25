"""The premise, as a subsystem in a file of its own: the world's description, the AI's main instructions,
the opening backstory, and the first input. No objects and no data -- just the strings that say what kind
of story this is and where it starts, lifted from basic tutorial 1.
"""

import iw

# Shown to the player when they browse the list of worlds. Sets expectations; has no effect on the story.
DESCRIPTION = (
    "This world is a psychological horror, where you play the solitary lighthouse keeper on an "
    "uninhabited island. As time goes on, the isolation drains your sanity, and your grip on reality "
    "weakens. Will you be able to survive, or will you meet the same fate as the previous lighthouse "
    "keeper?"
)

# The AI's brief: what this world is, and how it should be run.
INSTRUCTIONS = """This adventure is a psychological horror set on the island of Rona, an uninhabited island in the Outer Hebrides.

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

# The backstory the story opens on, set before the first turn begins.
BACKGROUND = """You had heard stories about Rona, and none of them were good.

Some say that this island is cursed. Some say that the spirits of lost sailors haunt the place. Some say that all those stories are superstitious hogwash, and it's just that being alone on an island for six months causes you to hallucinate. The only thing that everyone agrees on is that being the lighthouse keeper on Rona is a bad idea.

But when a bad job market and rising bills collide, the outcome was inescapable: You are now the lighthouse keeper for Rona, the most remote island in the Outer Hebrides.

You packed your bags, and took the flight to Stornoway. In the pre-dawn darkness, you made your way to the docks and met the boatman, your only human contact for the next six months. Large, muscular and silent, the man took you on board his ship and you left civilization behind. During the journey you tried to make conversation, but the man never spoke a word.

The journey took four hours, during which dawn broke. As the morning fog started to dissipate, you saw it looming above you: Rona Lighthouse, your home for the next six months.
"""

# The opening move the story starts from, written as the player would act it. The engine seeds the first
# turn from it.
FIRST_INPUT = (
    "I step off the boat, onto the beach, feeling the shale crunch underfoot. The boatman silently "
    "unloads my bags and supplies. While he unloads, I take some time to take in my surroundings."
)


# The goal the whole posting is measured against.
OBJECTIVE = (
    "To complete your six-month posting as keeper of the Rona lighthouse \u2014 keep the light burning, survive the isolation, and board the relief boat when it finally comes for you."
)


def install_into(world: iw.World) -> None:
    """Set the world's premise: description (shown in the browser), instructions (the AI's brief),
    background (the backstory the first turn opens on), and first input (the opening move)."""
    world.description = DESCRIPTION
    world.instructions = INSTRUCTIONS
    world.background = BACKGROUND
    world.firstInput = FIRST_INPUT
    world.objective = OBJECTIVE
