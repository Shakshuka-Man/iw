# %% [markdown]
# # Tutorial 1 — A simple world
#
# Creating a world is simple — all you need is a title and at least one skill, and in a pinch you can even
# skip those:

# %%
import pathlib
import iw

world = iw.World(
    title="A really simple world",
    skills=["Brawn", "Charisma"],
)

# %% [markdown]
# ## Extracting the JSON
#
# Once you have created your world, you can write it to a JSON that can then be imported into Infinite
# Worlds and played. Run the cell below and a new file appears in the file browser on the left, containing
# the JSON of the world.

# %%
pathlib.Path("minimal_world.json").write_text(world.to_json())

# %% [markdown]
# ## A world worth playing
#
# However, although that world is functional, it is not very interesting. Let's instead go with a more
# interesting premise: a psychological horror where the player is alone on a remote island, and has to
# deal with their fraying sanity and supernatural elements.
#
# A world is a plain object, so you can build it a field at a time — create an empty `iw.World()` and set
# what you care about.

# %%
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

# %% [markdown]
# Save it the same way as before. Name the file after the world, not after this tutorial — a `.json`
# ends up in your downloads folder with no tree around it, so `the_lighthouse.json` says what it is and
# `tutorial_iw_1_simple_world.json` does not. This is the file you paste into Infinite Worlds.

# %%
pathlib.Path("the_lighthouse.json").write_text(world.to_json())

# %% [markdown]
# ## Changing a world you already have
#
# We can also load an existing world definition in order to make changes to it. For example, we might
# decide that we want to rename our world from `The Lighthouse` to `Bones in the Ocean`. Instead of having
# to recreate the world from scratch, we can load the JSON we just saved, make our changes, and write it
# back out under the new name.

# %%
world = iw.World.from_json(pathlib.Path("the_lighthouse.json").read_text())
world.title = "Bones in the Ocean"
pathlib.Path("bones_in_the_ocean.json").write_text(world.to_json())

print(f"reloaded and renamed to: {world.title!r}")

# %% [markdown]
# ## Where to go next
#
# We have only covered the basics of world editing here. To learn more:
#
# - The **`iw` reference** at `docs/iw.md` lists every object, every attribute, the type it takes and what
#   it is for, plus every enum member with a line of code using it. Its structure is generated from the
#   library, so it is never out of date.
# - Or carry on with the rest of these tutorials. **Next:** `tutorial_iw_2_instruction_blocks` — the
#   island itself, and the keyword blocks that make it deep for free.
