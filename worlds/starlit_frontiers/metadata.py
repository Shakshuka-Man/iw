"""The world's metadata: everything it says about itself before anyone plays it, plus the two blocks that
are about how it should be *written* rather than what is in it.

Like every other subsystem, it installs itself. `world.py` makes a bare `iw.World` with only a title, and
`install_into` fills in the AI's brief, the voice, the cover art, the permissions, the two writing blocks,
and -- last of all -- the blurb. It is installed *last* for that last reason: a description of how much is
in the world can only be written once the world has things in it, so the ship and system totals in the
blurb cannot go stale. Add a ship and the blurb says so.

`background`, `firstInput` and `objective` are placeholders. They are never seen: this world has seven
playable characters who each begin in a different place, ship and past, so all three are rewritten by that
character's start-of-game trigger before the first word is generated. See `characters.py`.
"""

import iw

from .ships import ALL_SHIPS
from .systems import ALL_SYSTEMS

_SET_BY_TRIGGERS = "THIS IS SET BY TRIGGERS"

AUTHOR_STYLE = (
    "A writer of hard science fiction in the tradition of Alastair Reynolds and Ann Leckie, with "
    "attention to technological realism and moral complexity"
)

DESCRIPTION_REQUEST = (
    "You must generate a description of at least seventy well-developed paragraphs.\n\n"
    "Keep technical language and jargon to a minimum.\n\n"
    "Give evocative descriptions of each spaceship, each system and each stellar object in these "
    "systems.\n\n"
    "At the end of outcomeDescription, you must give a list of all spaceship models that I am aware of "
    "in the system, and the count of each. For example, if I am aware of one Bison, three Smilodons and "
    "eight Mules, then the end of outcomeDescription should read:\n"
    "`OBSERVED SHIPS:\n"
    "Bison (1)\n"
    "Smilodon (3)\n"
    "Mule (8)\n"
    "`"
)

# The cover art. The engine keeps every option the world was ever given and an index saying which one is
# live, so these are lists and a choice -- not one URL. Change CURRENT_PREVIEW_IMAGE to swap the cover.
PREVIEW_IMAGES = [
    "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/pCIXLDxsnV.jpg",
    "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/QEG6i65UF8.jpg",
]
FULL_SIZE_PREVIEW_IMAGES = [
    "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/wAhAf1h3Zt.jpg",
    "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/XkEzZYSLSe.jpg",
]
CURRENT_PREVIEW_IMAGE = 1


# ---- Two blocks that are really about how the world is *written*, not what is in it ---------------

NAMES = iw.InstructionBlock(
    name="Names",
    content="This adventure takes place in the 32nd century. As a result, names that are common in the 21st century each such as 'Marcus' and 'Chen' are not present. Instead, all characters have futuristic names that do not exist in the 21st century.",
)

IMAGE_INSTRUCTIONS = iw.InstructionBlock(
    name="Image instructions",
    content="When generating IllustrSubject and IllustrAppearance, never use nautical terms such as `Ship` and `Yacht`. If illustrating a starship, use the word `Starship` instead. You should always include the `exterior_appearance_description` of the ship being illustrated in IllustrAppearance and IllustrSubject exactly, without any rewording.",
)


def describe(world: iw.World) -> str:
    """The blurb the player reads when browsing.

    It counts a world that has already been assembled, which is why `install_into` calls this last rather
    than at the start: a description of how much is in the world can only be written once the world has
    things in it. The numbers therefore cannot go stale -- add a ship and the blurb says so."""
    num_lore = len(world.loreBookEntries)
    num_triggers = len(world.triggerEvents)
    num_ships = len(ALL_SHIPS)
    num_systems = len(ALL_SYSTEMS)
    return (
        "The year is 3166, and the galaxy is at war.\n\n"
        "Humanity once lived under the watchful eye of MERIT—an all-seeing intelligence that "
        "guided civilization into a golden age. Technology flourished, scarcity vanished, and "
        "humanity spread across the stars. But as new worlds were settled and distant systems "
        "grew beyond MERIT’s reach, humanity rediscovered something it had not known for "
        "centuries: freedom. With it came ambition, rivalry, and conflict.\n\n"
        "War was inevitable.\n\n"
        "The galaxy has been locked in a stalemate for over a century. MERIT still rules the "
        "wealthy inner systems, guarding them with the vast fleets of the Stellar Concordium. "
        "Beyond them lie the outer systems - MERIT is powerful enough to crush any one of them, "
        "but not all of them at once. If it strikes too hard in one direction, the others will "
        "move. So the war grinds on, century after century, neither side able to deliver the "
        "final blow.\n\n"
        "In the outer systems, people watch the inner worlds with dread, waiting for the day "
        "MERIT decides to finish the war and bring them to heel. In the inner systems, citizens "
        "fear something just as dangerous - that their civilization will slowly wither, trapped "
        "within its shrinking domain while the rest of humanity drifts beyond its control.\n\n"
        "The galaxy is a powder keg, ready to explode. And you may just be the match that sets "
        "it alight.\n\n"
        "------------------------------------------------------------\n\n"
        "This is a space exploration world inspired by games such as Freelancer, Escape "
        "Velocity, and Starsector. \n\n"
        "This world features:\n"
        "- 6 factions\n"
        f"- {num_ships} ships\n"
        f"- {num_systems} systems\n"
        "- over 110,000 words of source material\n"
        f"- {num_lore} keyword lore entries and {num_triggers} triggers to keep the "
        "credit cost low\n\n"
        "A galactic map is available at: https://i.imgur.com/qRLP7mc.png"
    )


def install_into(world: iw.World) -> None:
    """Fill in everything the world says about itself: the AI's brief, the voice, the cover art, the
    permissions, the two blocks about how it is written, and -- last -- the blurb, which counts the
    finished world. Install this subsystem last, so those counts are complete."""
    world.background = _SET_BY_TRIGGERS
    world.instructions = (
        "This adventure starts in the year 3166.\n\n"
        "The setting's technology should be consistent: inertial resonators allow fast atmospheric "
        "and orbital flight but are impractical to travel between solar systems; jump drives enable "
        "instantaneous interstellar travel but only between specific points; MERIT's surveillance "
        "is absolute in the inner systems but weakens toward the frontier."
    )
    world.firstInput = _SET_BY_TRIGGERS
    world.objective = _SET_BY_TRIGGERS

    world.authorStyle = AUTHOR_STYLE
    world.descriptionRequest = DESCRIPTION_REQUEST

    world.imageModel = "manticore"
    world.imageStyle = "comic_book"
    world.illustrationStyleNonCharacterLowPriority = (
        "far future space station, hard science fiction aesthetic, gritty realism"
    )
    world.illustrationStyleCharacterLowPriority = (
        "3166 CE far future setting, practical spacer clothing, diverse human ethnicity"
    )
    world.imageStyleCharacterPre = "A bright, futuristic image of"
    world.imageStyleCharacterPost = (
        "Depicting fashionable, space-age optimism. Objects are clean and smooth. Spacecraft are "
        "sleek and futuristic. The overall tone is optimistic, stylish, and effortlessly futuristic "
        "rather than solemn or theatrical. The aesthetic suggests a wild fantasy of how people "
        "would dress casually in space, prioritizing style, confidence, and impracticality over "
        "realism. Clothing is skintight and futuristic, not resembling any present-day clothing or "
        "spacesuits."
    )
    world.imageStyleNonCharacterPre = "A bright, futuristic image of"
    world.imageStyleNonCharacterPost = (
        "Depicting fashionable, space-age optimism. Objects are clean and smooth. Spacecraft are "
        "sleek and futuristic. Colors are vivid, and the overall tone is optimistic, stylish, and "
        "effortlessly modern rather than solemn or theatrical."
    )
    world.imagePromptDetails = iw.ImagePromptDetails(
        illustrClothes="A futuristic jumpsuit, covered in a thin layer of frost and ice",
        illustrSetting="In space, several ships visible in background",
        illustrSubject="A data courier in cybernetic gear",
        illustrAppearance=(
            "A sleek spaceship narrowly evading projectiles and explosions from an intimidating "
            "capital ship"
        ),
        illustrIsCharacter=False,
        illustrExpressionPosition="Frozen solid in a cryosleeper",
    )

    world.permissionsOnceShared = iw.PermissionsOnceShared(sharing=True, editing=True)
    world.allowChangeCharacterName = True
    world.allowChangeCharacterDescription = True
    world.allowChangeCharacterSkills = True
    world.allowChangeCharacterItemValues = False
    world.allowChangeCharacterPortrait = False
    world.allowChangeCharacterNewPortrait = True

    world.nsfw = False
    world.enableAISpecificInstructionBlocks = False
    world.schemaVersion = 2.2
    world.autoAdvanceVersion = True
    world.version = "3.24"

    world.previewImageOptions = PREVIEW_IMAGES
    world.fullSizePreviewImageOptions = FULL_SIZE_PREVIEW_IMAGES
    world.currentPreviewImageIndex = CURRENT_PREVIEW_IMAGE
    world.previewImage = PREVIEW_IMAGES[CURRENT_PREVIEW_IMAGE]
    world.fullSizePreviewImage = FULL_SIZE_PREVIEW_IMAGES[CURRENT_PREVIEW_IMAGE]

    world.instructionBlocks.extend([NAMES, IMAGE_INSTRUCTIONS])

    world.description = describe(world)
