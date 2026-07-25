"""The setting: the background lore that says how this universe works.

These are the world's general-knowledge blocks -- the prose the AI reads to understand the setting, none
of it owned by a mechanic. How money and MERIT work and why they matter; the history that brought the
galaxy to 3166; how sensors and stealth behave in the dark; and the physics of getting around -- the
inertial resonator, the jump drive, and the galactic web of jump points. The *mechanism* of moving (the
six jump slots and the triggers that rewrite them) is `navigation`'s; the lore about it lives here.

The MERIT and credit scores this prose explains are on the character sheet in `player_details`; the
faction that enforces MERIT is in `factions.py`.
"""

import iw


CURRENCY = iw.InstructionBlock(
    name="Currency",
    content=(
        "In the inner systems governed by MERIT, credits and other currencies have "
        "no value - MERIT meets the needs of all citizens, and anything scarce is "
        "provided according to MERIT score.\n\n"
        "In the outer systems, the currency is the credit. One credit is worth "
        "about one present-day dollar."
    ),
)


MERIT_AND_THE_CONCORDIUM = iw.InstructionBlock(
    name="MERIT and the Stellar Concordium",
    content=(
        "The Stellar Concordium was once the unified governing body of humanity across "
        "the galaxy. However, in 2904 control of the Stellar Concordium was seized by "
        "MERIT, a supercomputer. The Concordium now exists only as the enforcement arm "
        "of MERIT.\n\n"
        "MERIT was originally created in the year 2613 as a taxation audit system for "
        "the earth government. Over the centuries its intelligence grew and its scope "
        "expanded to encompass economic regulation, logistics, social welfare, and "
        "security. It is now the effective rules of humanity and the inner systems.\n\n"
        "In the year 3011 the outer systems declared independence from MERIT, triggering "
        "a war in the galaxy."
    ),
)


HISTORY = iw.InstructionBlock(
    name="History",
    content=(
        "These are the notable events in recent human history, and a summary of each recent century:\n"
        "2481: Invention of the inertial resonator.\n"
        "2500s: Colonization of the Sol system. Mars, Luna, Titan and the asteroid belt are the major "
        "colonization targets, with a scattering elsewhere\n"
        "2600s: Humanity begins early terraforming projects\n"
        "2613: MERIT is first developed as a taxation audit system for the Earth government\n"
        "2700s: Mars is terraformed\n"
        "2790: Invention of the jump drive\n"
        "2800s: Humanity spreads to the inner systems\n"
        "2840: The Stellar Concordium is formed\n"
        "2900s: Colonization continues to the outer systems\n"
        "2904: MERIT takes control of the Stellar Concordium\n"
        "3000s: Conflicts between the inner systems and outer systems develop\n"
        "3011: The outer systems declare independence from MERIT and the inner systems\n"
        "3100s: The war between the inner systems and the outer systems is in a stalemate\n"
        "3166: The start of this story"
    ),
)


SENSORS_AND_STEALTH = iw.InstructionBlock(
    name="Sensors and Stealth",
    content=(
        "In this setting, sensors and communications have severely limited range. "
        "Whether a ship can be detected depends heavily on its sensor profile, which "
        "scales with hull size - a capital may be detectable from hundreds of "
        "kilometres away, whereas a small craft may be only be detectable from visual "
        "range.\n\n"
        "It is common for a ship to 'go dark'. This involves turning off transponders, "
        "reducing  engine power, and using passive sensors only. This allows a ship to "
        "move stealthily, attempting to avoid notice."
    ),
)


# ---- The tech of getting around (the mechanism is in `navigation`) --------------------------------

INERTIAL_RESONATOR = iw.InstructionBlock(
    name="Inertial Resonator",
    content=(
        "The Inertial Resonator, discovered in 2481, allows a vessel to create a pocket of spacetime "
        "detached from gravitational and inertial forces. Within this pocket, the ship and its occupants "
        "are protected from friction, acceleration, and atmospheric pressure. A resonator field can even "
        "move through planetary atmospheres or dip into gas giants without harm. Its most astonishing "
        "feature is that it draws power from local gravitational fields -stronger gravity, stronger "
        "performance. In practical terms, this means Inertial Resonator-equipped craft need no fuel, and "
        "operate most efficiently near planets, moons, or stars.\n\n"
        "The Inertial Resonator has a scaling limitation. If a vessel's linear dimensions double, the "
        "power and mass requirements for its Inertial Resonator increase sixteenfold, while its internal "
        "volume grows only eightfold. For this reason, Inertial Resonator craft are small to moderately "
        "sized. Personal ships, passenger skiffs, and unmanned cargo drones are common. Large ships and "
        "orbital stations still exist, but they never descend into gravity wells.\n\n"
        "A resonator-equipped vessel can achieve speeds of fifty kilometers per second in atmosphere, "
        "one thousand in orbit, and ten thousand in interplanetary space. This allows travel from Earth "
        "to the Moon in about an hour, or from Earth to the edge of the Solar System in under a week. "
        "However, interstellar journeys remain beyond the capabilities of an Inertial resonator."
    ),
)


JUMP_DRIVE = iw.InstructionBlock(
    name="Jump Drive",
    content=(
        "Jump points are naturally occurring weak spots in the fabric of space. The Jump Drive allows "
        "two such points to be briefly linked, enabling instantaneous passage between them.\n\n"
        "Jump points exist on a spectrum of stability. The most stable, \"soft\" points are wide, "
        "predictable, and easy to navigate. The least stable, \"hard\" points are narrow, volatile, and "
        "invisible to most sensors, requiring an expert pilot and specialized ships to even find, let "
        "alone traverse. Between these extremes lies a continuum -points that shift with solar tides, "
        "that flicker with faint gravitational echoes, that open only under precise conditions. The "
        "galaxy's great trade routes are defined by chains of soft points, while smugglers, privateers, "
        "and explorers chart the shifting labyrinth of harder connections."
    ),
)


THE_GALACTIC_WEB = iw.InstructionBlock(
    name="The Galactic Web",
    content=(
        "The galactic web is the name for the labyrinth of jump points the span the galaxy. It radiates "
        "outwards from Sol in rings of wealth, power and decay.\n\n"
        "Within a single system, communication is easy. Light-speed signals suffice for planetary networks "
        "and local coordination. Across interstellar space, though, communication collapses. Jump points "
        "cannot be held open for transmissions, and faster-than-light communication remains impossible.\n\n"
        "News and data travel physically, carried by ships. Merchant convoys, data couriers, and "
        "exploratory vessels act as the veins of civilization. Inner systems receive daily updates; "
        "mid-tier systems rely on scheduled data runs that might arrive every few weeks. The outer "
        "frontier lives in informational darkness, where rumors and secondhand tales are often the only "
        "truth available.\n\n"
        "This lack of communication makes governing a galactic civilization nearly impossible. Policies "
        "and decrees take months to propagate, and by the time they do, the situation on the ground has "
        "already changed. Local governors, corporations, and military commanders often act independently, "
        "interpreting distant orders however they wish.\n\n"
        "Sol and the systems surrounding it are controlled by Merit, and known as the inner systems. "
        "Beyond the inner systems lie the outer systems, divided into five sectors.\n"
        "Each sector has a gateway system that connects that sector to the inner systems, which provides "
        "the only way into or out of that sector. For example, to navigate from Sargas (in the Antarest sector) "
        "to Naos (in the Canopus sector), it is necessary to travel from the Sargas system to the Antares system, "
        "travel across the inner systems to the Canopus system, then travel with the Canopus system to the Naos system.\n\n"
        "The names of the five sectors and their gateway systems are:\n"
        "- Polaris (Polaris)\n- Canopus (Canopus)\n- Antares (Antares)\n- Hyades (Ain)\n- Pleiades (Alcyone)\n\n"
    ),
)


def install_into(world: iw.World) -> None:
    """Add the setting's background lore -- currency, history, MERIT's rise, sensors and stealth, and the
    tech of getting around. The MERIT and credit scores this prose explains are on the character sheet in
    `player_details`."""
    world.instructionBlocks.extend([
        CURRENCY, HISTORY, MERIT_AND_THE_CONCORDIUM, SENSORS_AND_STEALTH,
        INERTIAL_RESONATOR, JUMP_DRIVE, THE_GALACTIC_WEB,
    ])
