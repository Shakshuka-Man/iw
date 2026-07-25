"""The world's look and framing, as a subsystem of its own: the art direction the illustrator works to,
the cover art, the voice the prose is written in, and the handful of flags that govern what a player may
change once the world is shared.

None of this changes what *happens* in the world -- it decides how it looks and how it reads. It was
authored in the web UI and lifted back into the build, which is why the values are literal rather than
derived: they are art direction, not logic.
"""

import iw

# The voice. This is the single most load-bearing string for how the prose actually reads.
AUTHOR_STYLE = (
    "Robert Macfarlane crossed with Shirley Jackson \u2014 precise, atmospheric literary prose that renders landscape with visceral beauty and renders psychological horror through restraint, implication, and the weight of what is left unsaid"
)

# --- Art direction ------------------------------------------------------------------------------
# Two registers: how people are drawn, and how everything else is. Each has a phrase wrapped around the
# subject (`Pre`/`Post`) and a low-priority style hint the illustrator falls back on.
IMAGE_STYLE = "photo_dramatic"

CHARACTER_PRE = "A dynamic, dark, gritty, hyperrealist photograph of"
CHARACTER_POST = (
    "hyperrealist anatomy and facial features. dark dramatic lighting. Style is inspired by hand-painted comic book covers of Todd McFarlane with earthy tones and rich shadowing. Entire body is visible."
)
CHARACTER_STYLE = (
    "isolated, weathered, early 20th century working clothes, oil-stained, wind-battered, gaunt, haunted eyes, muted palette"
)

NON_CHARACTER_PRE = "Hyperrealist dark, gritty photograph of"
NON_CHARACTER_POST = (
    "cinematic, intense, and steeped in heroic tension. golden-hour light casting dramatic shadows."
)
NON_CHARACTER_STYLE = (
    "isolated Scottish island, stark, atmospheric, muted palette of greys and deep blues, oil painting texture, Turner seascapes, fog, weathered stone, early 20th century"
)

# The cover art: one generated image, and the prompt that produced it.
PREVIEW_IMAGE = "https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/C4oHCbFRcp.webp"
FULL_SIZE_PREVIEW_IMAGE = "https://infinite-worlds-images-4.us-mia-1.linodeobjects.com/NZlXWk7pC3.webp"

COVER_PROMPT = iw.ImagePromptDetails(
    illustrSubject="The lighthouse keeper",
    illustrAppearance="A solitary lighthouse on a desolate island, its light piercing through the darkness",
    illustrClothes="heavy dark wool sweater, worn canvas trousers",
    illustrSetting="A dramatic thunderstorm at night, with driving rain and violent waves",
    illustrExpressionPosition="calm, standing",
    illustrIsCharacter=False,
)


def install_into(world: iw.World) -> None:
    """Add the world's voice, its art direction, its cover image, and the sharing permissions."""
    world.authorStyle = AUTHOR_STYLE

    world.imageStyle = IMAGE_STYLE
    world.imageStyleCharacterPre = CHARACTER_PRE
    world.imageStyleCharacterPost = CHARACTER_POST
    world.illustrationStyleCharacterLowPriority = CHARACTER_STYLE
    world.imageStyleNonCharacterPre = NON_CHARACTER_PRE
    world.imageStyleNonCharacterPost = NON_CHARACTER_POST
    world.illustrationStyleNonCharacterLowPriority = NON_CHARACTER_STYLE

    world.previewImage = PREVIEW_IMAGE
    world.fullSizePreviewImage = FULL_SIZE_PREVIEW_IMAGE
    world.previewImageOptions = [PREVIEW_IMAGE]
    world.fullSizePreviewImageOptions = [FULL_SIZE_PREVIEW_IMAGE]
    world.currentPreviewImageIndex = 0
    world.imagePromptDetails = COVER_PROMPT

    # What a player may change once this world is shared with them.
    world.allowChangeCharacterSkills = True
    world.allowChangeCharacterPortrait = False

    world.schemaVersion = 2.2
    world.version = "1.00"
    world.autoAdvanceVersion = True
