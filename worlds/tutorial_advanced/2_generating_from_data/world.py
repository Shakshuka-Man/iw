# %% [markdown]
# # Advanced tutorial 2 — Generating objects from external data
#
# In the basic tutorial, we had a few repeated blocks of logic - when we created a KIB for each shipwreck,
# we had to inline all of these in our code, and repeat the boilerplate logic to set up KIBs. Similarly,
# when we created our triggers to update sanity instructions, we created all ten triggers manually,
# requiring a lot of boilerplate logic that is difficult to maintain.
#
# The real strength of using this python editor over Infinite World's built-in editor is that we can generate
# this content dynamically from other sources. In our case, we have two csv files of data that we want to
# feed into this world - one that gives details of each of the shipwrecks, and one that gives details of the
# sanity instructions.
#
# You can see these csv files in the same folder as this notebook. They can be opened and edited without having
# to worry about maintaining any coding boilerplate, or without needing advanced coding skills.

# %%
import csv
import pathlib

import iw

world = iw.World(title="Bones in the Ocean")

# Both CSVs sit in this folder. We find it by `__file__` when this runs as a script (build.py sets it), and
# by the working directory when it runs as a notebook (a notebook has no `__file__`). One of the two is
# always right: a bare `open("wrecks.csv")` would work in the browser but look in the wrong place under
# build.py, which runs from `out/`.
FOLDER = pathlib.Path(__file__).parent if "__file__" in globals() else pathlib.Path.cwd()

# %% [markdown]
# ### Building the wrecks
#
# Each shipwreck corresponds to one row in the CSV. We just need to write the logic to convert a single csv row
# into a KIB, and we can iterate through the file to generate all of them

# %%
# csv.DictReader hands back one dict per row, keyed by the header line. We read the whole file once (so we
# can walk the wrecks twice -- here for the KIBs, and below for the summary), then build one KIB per row.
with (FOLDER / "wrecks.csv").open(newline="", encoding="utf-8") as handle:
    wrecks = list(csv.DictReader(handle))

for wreck in wrecks:
    name, year = wreck["ship_name"], wreck["year"]
    # Every word that should summon this wreck: her name, "the " + her name, and the year. Derived from the
    # row, so it is the same few lines for twelve ships or twelve thousand, and never a typo on the fifteenth.
    keywords = sorted({word.strip().lower() for word in (name, f"the {name}", year) if word.strip()})
    article = "an" if wreck["type"][:1].lower() in "aeiou" else "a"
    crew = "; ".join(part.strip() for part in wreck["notable_crew"].split(";") if part.strip())
    world.loreBookEntries.append(iw.LoreBookEntry(
        name=f"Wreck: {name} ({year})",
        keywords=keywords,
        content=(
            f"The {name}, {article} {wreck['type']}, lost on the reef off Rona in {year}. "
            f"{wreck['souls']} souls lost.\n"
            f"Of note aboard: {crew}.\n"
            f"{wreck['ship_story']}"
        ),
    ))

# %% [markdown]
# ### The wreck summary instructions
#
# The KIBs are given to the storyteller AI when the keywords are seen in the recent turns. However, if this is
# the only place the wrecks are known about, then the AI will never bring them up and the KIBs will never fire.
# We will therefore need to create an extra instruction block that always gets fed to the AI, giving the AI a
# brief overview of each of the wrecks, so it can factor those into the turns it generates.

# %%
world.instructionBlocks.append(iw.InstructionBlock(
    name="The wrecks",
    content=(
        "The reef north of the light has been taking ships for centuries. Mention them in passing when it fits -- "
        "a name in the log, the graves under the cairn, a spar on the shore after a storm. The wrecks of note are:\n"
        + "\n".join(f"- {wreck['ship_name']} ({wreck['year']}): {wreck['brief']}" for wreck in wrecks)
    ),
))

# %% [markdown]
# ### The sanity instructions
#
# In the basic tutorial, we introduced the SANITY tracked item, and how the instructions varied as sanity varied.
# However, we had to do it the long way - we had all the instructions inline, and we had to repeat the trigger
# definitions for each, as well as the boilerplate around trigger conditions and effects.
#
# Fortunately, we can similarly do this programmatically.

# %%
SANITY = iw.TrackedItem(
    name="Sanity",
    dataType=iw.TrackedItemDataType.NUMBER,
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    initialValue="100",
    autoUpdate=True,
)
world.trackedItems.append(SANITY)

# The block the band triggers rewrite: what the day and the night are like at the keeper's current sanity.
DAY_AND_NIGHT = iw.InstructionBlock(name="The day and the night")
world.instructionBlocks.append(DAY_AND_NIGHT)

# One trigger per band: while the meter is inside [low, high], rewrite the block with that band's day and
# night. canTriggerMoreThanOnce, or the band fires once and then freezes -- easy to forget on the tenth one.
with (FOLDER / "sanity_bands.csv").open(newline="", encoding="utf-8") as handle:
    for band in csv.DictReader(handle):
        world.triggerEvents.append(iw.TriggerEvent(
            name=f"Sanity {band['low']}-{band['high']}",
            canTriggerMoreThanOnce=True,
            triggerConditions=[
                iw.tools.tracked_item_is(SANITY, band["low"], iw.Inequality.AT_LEAST),
                iw.tools.tracked_item_is(SANITY, band["high"], iw.Inequality.AT_MOST),
            ],
            triggerEffects=[
                iw.TriggerEffect(
                    type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
                    data={"id": DAY_AND_NIGHT.id, "content": f"Day: {band['day']}\n\nNight: {band['night']}"},
                ),
            ],
        ))

# %% [markdown]
# ## Output

# %%
print(world.summary())
pathlib.Path("tutorial_advanced_2_generating_from_external_data.json").write_text(world.to_json())
