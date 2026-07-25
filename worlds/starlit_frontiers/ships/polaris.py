from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


CALIPER = ShipTemplate(
    name="Caliper",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.SMALL,
    ship_archetype="Scout",
    combat_role="Reconnaissance / neural sensor platform",
    length=14,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Neural-linked reconnaissance craft with oversized sensor suite",
    long_description=(
        "The Caliper is the eyes of a Polaran fleet. Its single neural-linked pilot "
        "experiences the surrounding space as an extension of their own senses -- enemy "
        "emissions register as pressure, gravity wells as texture, jump point resonance "
        "as sound. The result is a scout that doesn't just detect targets but perceives "
        "them with an intuitive depth that no instrument panel can replicate. The Caliper "
        "carries minimal armament and avoids all fights. Its value is in the intelligence "
        "it feeds back through encrypted neural relay to the fleet's capital ships."
    ),
    exterior_appearance_description=(
        "A 14-meter single-seat military spacecraft with a pale grey hull. A smooth, compact "
        "ellipsoid -- a continuous curved surface with no flat faces or sharp edges. The hull "
        "is seamless with no visible seams, panels, or external fittings. No canopy. A light "
        "laser behind a flush panel in the front. Engine bells recessed into sculpted cavities "
        "in the rear, flush with the hull surface. Indigo trim in thin parallel lines along "
        "the hull centreline. Ice blue lines trace neural interface pathways in a fine "
        "branching network pattern across the hull, faintly luminous, glowing brighter when "
        "the connection is active. A small indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "There is no cockpit in any conventional sense. The pilot reclines in a contoured "
        "neural cradle that occupies most of the interior, surrounded by interface conduits "
        "that connect directly to the sensor array. No windows, no screens, no manual "
        "controls -- the pilot sees through the ship's sensors as though they were their "
        "own eyes. The space is intimate and womb-like, padded in dark composite material "
        "that absorbs sound and vibration. A faint hum from the interface is the only "
        "indication the ship is active."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Neural interface cradle", "Extended passive sensor array", "Encrypted neural relay"],
)

RETORT = ShipTemplate(
    name="Retort",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=20,
    armor=2,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=6,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Neural-guided bomber carrying a single antimatter torpedo",
    long_description=(
        "The Retort is a delivery system for a single devastating antimatter torpedo. Its "
        "two-person crew -- pilot and weapons officer -- are both neural-linked, allowing "
        "the weapons officer to guide the torpedo's final approach with a precision that "
        "automated targeting cannot match. The Retort's approach is the most dangerous "
        "minutes in Polaran service: slow, lightly armored, crossing a killing field of "
        "point defense fire to reach point-blank range. Neural linking makes the crew "
        "acutely aware of every incoming shot. Veterans describe the approach as feeling "
        "each near-miss as a physical sensation. Retorts fire once and retreat to rearm."
    ),
    exterior_appearance_description=(
        "A 20-meter two-seat military spacecraft with a pale grey hull. A smooth, flattened "
        "ellipsoid -- wide and flat, with a continuous curved surface. "
        "The hull is seamless. No canopy. The torpedo housing is integrated into the underside "
        "behind a flush panel that opens for firing. Engine bells recessed into sculpted "
        "cavities in the rear. Indigo trim in thin parallel lines along the hull. Ice blue "
        "lines trace neural interface pathways in a branching network pattern across the hull, "
        "faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "Two neural cradles sit in tandem -- pilot forward, weapons officer behind -- in a "
        "space so cramped their shoulders nearly touch. The torpedo housing occupies the "
        "entire ventral section, and the interface conduits run along both walls in exposed "
        "bundles. The interior is stripped to essentials: dark composite paneling, no "
        "personal storage, no comfort features. The weapons officer's cradle includes "
        "additional interface leads for torpedo guidance. The space smells faintly of "
        "ozone and the chemical tang of interface fluid."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Neural interface cradle (x2)", "Torpedo guidance neural link"],
)

SCALPEL = ShipTemplate(
    name="Scalpel",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.SMALL,
    ship_archetype="Interceptor",
    combat_role="Fast attack / anti-scout / anti-bomber",
    length=11,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_LASER_ARRAY],
    default_small_craft=[],
    short_description="Ultra-fast neural-linked interceptor with zero-lag response",
    long_description=(
        "The Scalpel is the Polaran interceptor -- the fastest, most agile small craft in "
        "their inventory. With no manual controls whatsoever, it is literally unflyable by "
        "a baseline human. The ship responds to its pilot's intentions with zero input lag, "
        "turning thought into thrust. A Scalpel pilot doesn't fly the ship so much as wear "
        "it. Primary targets are scouts and bombers, both too slow to evade a neural-linked "
        "pursuit. The Scalpel's neural-linked laser is slightly more powerful than the "
        "standard interceptor weapon -- core-assisted targeting wrings extra performance "
        "from the same class of emitter. Not intended for sustained fights; a Scalpel "
        "that hasn't killed its target in the first pass is in trouble."
    ),
    exterior_appearance_description=(
        "An 11-meter single-seat military spacecraft with a pale grey hull. A smooth, "
        "elongated lenticular shape -- a flattened disc stretched lengthwise, tapering to a "
        "thin edge at the front and rear. The hull is a single unbroken surface with no "
        "visible seams, panels, or external fittings. No canopy. A heavy laser array behind a "
        "flush panel in the front that opens for firing. Engine bells recessed into sculpted "
        "cavities in the rear, flush with the hull surface. Indigo trim in thin parallel lines "
        "along the hull centreline. Ice blue lines trace neural interface pathways from the "
        "front to the rear in a fine branching network pattern, faintly luminous, glowing "
        "brighter when the connection is active. A small indigo neural node emblem on both "
        "sides."
    ),
    interior_appearance_description=(
        "The pilot lies nearly prone in a form-fitting neural cradle that constitutes the "
        "entire interior. The cradle wraps around the pilot's body from ankles to skull, "
        "with interface leads connecting at the base of the neck, wrists, and spine. There "
        "is no room to move, no windows, no displays. The pilot perceives the outside "
        "world entirely through the ship's sensors -- a full spherical awareness that "
        "baseline humans find disorienting and Polaran pilots find liberating. The space "
        "is barely larger than a coffin."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Neural interface cradle", "Zero-lag neural flight system"],
)

BORE = ShipTemplate(
    name="Bore",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=22,
    armor=8,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=18,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_PLASMA_CANNON],
    default_small_craft=[],
    short_description="Neural-linked heavy gunship for breaking escort screens",
    long_description=(
        "The Bore is the Polaran gunship -- a crewed strike craft carrying weapons heavy "
        "enough to threaten corvettes and frigates. Its role is clearing the escort screen "
        "that protects enemy capital ships from bomber attacks. A team of Bores punching "
        "through the destroyer line opens the gap that Retort bombers need to reach "
        "high-value targets. The Bore's crew of four are all neural-linked, with the pilot "
        "and gunner sharing a targeting awareness that allows the ship to maneuver and fire "
        "as a single coordinated action. Polaran Bores are faster than the standard gunship "
        "template -- neural coordination extracts more from the engines -- though slightly "
        "less armored."
    ),
    exterior_appearance_description=(
        "A 22-meter multi-crew military spacecraft with a pale grey hull. A smooth, thick disc "
        "shape -- a rounded, flattened body wider than it is long. The hull is seamless with "
        "no visible seams or external fittings. No canopy. A heavy plasma cannon behind a "
        "flush panel on the underside. Engine bells recessed into sculpted cavities "
        "distributed around the rear rim. Indigo trim in concentric rings on the top and "
        "bottom surfaces. Ice blue lines trace neural interface pathways in a branching "
        "network pattern across the hull, faintly luminous. An indigo neural node emblem on "
        "both sides."
    ),
    interior_appearance_description=(
        "Four neural cradles arranged in a tight diamond -- pilot and gunner forward, "
        "engineer and sensor operator behind. The heavy plasma cannon's power feeds run "
        "through the center of the cabin, radiating warmth during sustained fire. Each "
        "crew station has its own interface leads but all four share a common neural mesh, "
        "allowing any crew member to feel what the others perceive. The interior is "
        "functional and cramped, with dark composite walls and the constant low vibration "
        "of the weapon capacitors charging."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}],
    secondary_crew=[{"engineer": 1}, {"sensor_operator": 1}],
    additional_systems=["Neural interface cradle (x4)", "Shared crew neural mesh"],
)

VERNIER = ShipTemplate(
    name="Vernier",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=62,
    armor=18,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=60,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast patrol corvette with neural-enhanced sensor coverage",
    long_description=(
        "The Vernier is the standard Polaran patrol vessel and the most commonly "
        "encountered ship in their navy. It runs security in settled systems, escorts "
        "civilian traffic through jump points, and serves as the first response to "
        "incidents. The Vernier's neural-linked crew gives it sensor awareness and "
        "reaction times that belie its size -- a Vernier detects and classifies contacts "
        "faster than corvettes twice its crew complement. In wartime, Verniers form early "
        "warning screens at jump points, their linked crews feeding contact data directly "
        "to fleet command through neural relay. Not built for prolonged fleet combat, but "
        "a pair of Verniers can outmaneuver and harass much larger ships."
    ),
    exterior_appearance_description=(
        "A 62-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "-- a continuous curved surface tapering at both ends. The hull is seamless with no "
        "visible plate joins, no external fittings, no windows. A particle cannon behind a "
        "flush panel along the top. A heavy laser turret behind a flush panel on the upper "
        "hull. Engine bells recessed into sculpted cavities at the rear, flush with the hull "
        "surface. Indigo trim in thin precise geometric lines -- parallel stripes along the "
        "hull and concentric rings around the weapon panel seams. Ice blue lines trace neural "
        "interface pathways in a branching network pattern across the hull, faintly luminous. "
        "An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The bridge is a ring of neural cradles arranged around a central holographic "
        "display that the crew perceives through their links rather than their eyes. "
        "Corridors are narrow but well-lit in cool blue-white tones. Crew quarters are "
        "minimal -- small private compartments with integrated neural access points for "
        "off-duty monitoring. The ship's interior has the clean, clinical feel common to "
        "Polaran vessels: smooth composite surfaces, recessed lighting, and an absence of "
        "physical controls that visitors from other factions find unsettling."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 8}],
    secondary_crew=[{"sensor_specialists": 2}, {"gunners": 2}],
    additional_systems=["Neural interface stations (bridge)", "Passive sensor array"],
)

CAROUSEL = ShipTemplate(
    name="Carousel",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=58,
    armor=11,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=40,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Scalpel", 4)],
    short_description="Small-craft tender carrying a half-wing of interceptors",
    long_description=(
        "The Carousel carries and supports a detachment of Polaran small craft, extending "
        "their operational range by providing a jump-capable platform they can operate "
        "from. A Carousel with four Scalpels aboard is the standard system defense package "
        "-- enough fast interceptors to respond to a raiding force, with the Carousel "
        "providing rearm, repair, and neural relay support. The ship's most distinctive "
        "feature is its neural coordination suite, which maintains a direct relay link "
        "with embarked pilots even after launch, allowing the Carousel's crew to feed "
        "targeting data and situational awareness to its craft in real time."
    ),
    exterior_appearance_description=(
        "A 58-meter military spacecraft with a pale grey hull. A smooth, wide ellipsoid -- "
        "flattened and broad. The hull is seamless. No windows. "
        "Launch cradles for fighters visible along both sides as clean rectangular apertures "
        "in the curved hull. A light ion turret behind a flush panel on top. Engine bells "
        "recessed into sculpted cavities at the rear. Indigo trim in thin geometric lines "
        "along the hull and concentric rings around the launch apertures. Ice blue lines trace "
        "neural interface pathways across the hull, faintly luminous. An indigo neural node "
        "emblem on both sides."
    ),
    interior_appearance_description=(
        "The interior is split between crew spaces forward and a hangar section aft that "
        "dominates the ship's volume. The hangar is a controlled environment -- launch "
        "cradles hold each small craft in neural-linked readiness, with interface conduits "
        "running from the ship's systems directly into the craft so pilots can link in "
        "and launch without delay. The crew section is compact and functional, with the "
        "same clean Polaran aesthetic. A small coordination room near the hangar contains "
        "neural stations for the flight controller and maintenance chief."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 6}],
    secondary_crew=[
        {"embarked_craft_pilots": 4},
        {"hangar_maintenance": 3},
    ],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Hangar bay (4 small craft)",
        "Small-craft neural relay suite",
        "Craft maintenance and rearm facilities",
    ],
)

QUADRANT = ShipTemplate(
    name="Quadrant",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Survey Corvette",
    combat_role="Hazardous environment operations / exploration",
    length=54,
    armor=20,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=42,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Heavily shielded survey corvette for hazardous environments",
    long_description=(
        "The Quadrant is built to go where other ships can't. Radiation zones, unstable "
        "jump points, stellar proximity, nebular interference -- the Quadrant carries "
        "shielding disproportionate to its size and sensor packages designed for extreme "
        "conditions. Its neural-linked crew perceives environmental hazards as intuitive "
        "sensations -- radiation as warmth, gravitational distortion as pressure, jump "
        "point instability as a subsonic hum -- giving them reaction times that keep the "
        "ship alive in conditions that would overwhelm a crew reading instruments. Often "
        "the first ship sent into unknown territory. Carries slightly more supplies than "
        "a standard corvette for extended solo survey missions."
    ),
    exterior_appearance_description=(
        "A 54-meter military spacecraft with a pale grey hull. A smooth, compact ellipsoid. "
        "The hull is seamless with no visible seams or external fittings. No windows. Sensor "
        "equipment behind flush panels at the front -- a slight thickening of the hull the "
        "only indication. A light ion turret behind a flush panel on the upper hull. Engine "
        "bells recessed into sculpted cavities at the rear. Indigo trim in thin geometric "
        "lines along the hull. Ice blue lines trace neural interface pathways across the hull, "
        "faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "Heavier and more cramped than the Vernier. The layered shielding eats into "
        "interior volume, and the sensor processing equipment fills spaces that would be "
        "crew quarters on another ship. The bridge cradles are reinforced against "
        "electromagnetic interference, with additional shielding around the neural "
        "interface leads. Crew quarters are tight but private. A dedicated analysis room "
        "amidships contains neural stations optimized for processing survey data -- the "
        "crew can replay sensor recordings through their links, experiencing a jump point "
        "survey again and again to catch details they missed."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 6}],
    secondary_crew=[{"survey_specialists": 3}],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Reinforced environmental shielding",
        "Extreme-condition sensor package",
        "Neural survey analysis suite",
    ],
)

LANCET = ShipTemplate(
    name="Lancet",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Combat Frigate",
    combat_role="Fleet screening / torpedo attack",
    length=155,
    armor=32,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=110,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[
        weapons.RAILGUN,
        weapons.ANTIMATTER_TORPEDO,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Core-equipped combat frigate with railgun and torpedo",
    long_description=(
        "The Lancet is the smallest Polaran warship to carry a fused neural core. That "
        "core handles sensor integration, damage control, and point defense coordination, "
        "freeing the linked crew to focus entirely on combat. The result is a frigate-weight "
        "vessel that fights above its class. The Lancet screens the capital fleet, hunts "
        "enemy frigates, and carries an antimatter torpedo for devastating close-range "
        "strikes. A pack of Lancets closing to point blank is one of the most dangerous "
        "torpedo attacks in known space -- their core-coordinated approach vectors make them "
        "nearly impossible to predict. Faster than the template combat frigate but lighter "
        "on armor, reflecting the Polaran preference for speed over protection."
    ),
    exterior_appearance_description=(
        "A 155-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "-- a continuous curved surface tapering to a point at the front and rounding at the "
        "rear. The hull is seamless with no visible plate joins, no external fittings, no "
        "windows. All sensors behind flush panels. A railgun behind a long flush panel along "
        "the top that opens for firing. A torpedo bay behind a flush panel in the lower front. "
        "A heavy laser array behind a flush panel on the upper hull. Engine bells recessed "
        "into sculpted cavities distributed across the rear, flush with the hull surface. "
        "Indigo trim in thin precise geometric lines -- parallel stripes along the hull, "
        "concentric rings around the weapon panel seams, angular patterns converging amidships "
        "on the core chamber. Ice blue lines trace neural interface pathways across the hull "
        "surface in a branching network pattern, converging on the core chamber amidships -- "
        "faintly luminous, glowing brighter when the ship's neural systems are active. An "
        "indigo neural node emblem on both sides forward."
    ),
    interior_appearance_description=(
        "The bridge is a circle of eight neural cradles surrounding a central core chamber "
        "-- a reinforced compartment where the ship's fused core resides in a life-support "
        "pod. The core's presence is felt throughout the ship: systems respond before crew "
        "request them, damage control teams arrive at breaches before alarms sound, and "
        "point defense tracks targets with an unblinking precision that the crew has "
        "learned not to question. Corridors are narrow and efficient. Crew quarters are "
        "spartan single berths with neural access. The torpedo room is amidships, its "
        "single weapon tended by a dedicated crew who understand that their one shot may "
        "decide the engagement."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 35}],
    secondary_crew=[{"gunners": 10}, {"torpedo_crew": 6}, {"damage_control": 8}],
    additional_systems=[
        "Fused neural core (x1)",
        "Core-guided point defense system",
        "Neural interface stations (bridge)",
        "Encrypted fleet neural relay",
    ],
)

COMPASS = ShipTemplate(
    name="Compass",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Patrol Frigate",
    combat_role="Commerce protection / torpedo attack / independent operations",
    length=145,
    armor=17,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=70,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Independent patrol frigate with torpedo and medium-jump capability",
    long_description=(
        "The Compass is the Polaran independent operator -- the ship sent to patrol a system "
        "alone for weeks, making decisions without backup. It carries a fused core that "
        "serves as both a tireless watch officer and an intelligence analyst, processing "
        "the constant stream of sensor data that a neural-linked crew generates. Fast "
        "enough to dictate engagement range against most opponents, armed with a particle "
        "cannon for medium-range engagements and an antimatter torpedo for close-range "
        "killing power. A Compass captain may be the highest-ranking Polaran military "
        "officer in a system. Medium-jump capability lets it reach places the Lancet "
        "cannot. Carries additional supplies for extended independent deployment."
    ),
    exterior_appearance_description=(
        "A 145-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "tapering at both ends. The hull is seamless. No windows. A particle cannon behind a "
        "flush panel along the top. A torpedo bay behind a flush panel in the lower front. A "
        "heavy laser turret behind a flush panel on the upper hull. Engine bells recessed into "
        "sculpted cavities at the rear. Indigo trim in thin geometric lines -- parallel "
        "stripes and concentric rings around weapon panels. Ice blue lines trace neural "
        "interface pathways across the hull in a branching network pattern, converging on the "
        "core chamber amidships, faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "Less cramped than the Lancet -- the Compass is designed for extended independent "
        "cruises, and it shows. Crew quarters are still small but include personal neural "
        "access points for off-duty recreation through the ship's VR network. The bridge "
        "is arranged around the core chamber with additional sensor processing stations. "
        "A small wardroom serves as both dining area and briefing room. The ship has the "
        "feel of a vessel meant to be lived in, not just fought from -- a concession to "
        "the weeks-long patrols the Compass routinely undertakes."
    ),
    minimum_crew=[{"officers": 6}, {"crew": 25}],
    secondary_crew=[{"gunners": 6}, {"torpedo_crew": 4}, {"sensor_specialists": 3}],
    additional_systems=[
        "Fused neural core (x1)",
        "Neural interface stations (bridge)",
        "Extended passive sensor array",
        "Encrypted neural relay",
        "Crew VR network",
    ],
)

THEODOLITE = ShipTemplate(
    name="Theodolite",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=168,
    armor=7,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=55,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Core-equipped intelligence frigate with massive passive sensor array",
    long_description=(
        "The Theodolite is a frigate-sized vessel built around an enormous passive sensor "
        "array. Its two fused cores are dedicated entirely to processing the firehose of "
        "sensor data the array produces -- filtering, correlating, and interpreting signals "
        "across the entire electromagnetic spectrum simultaneously. The result is an "
        "intelligence picture of breathtaking resolution. Hard-jump capable, the Theodolite "
        "appears where no one expects a ship, watches, and reports back. Its crews are "
        "elite, its ships expensive, and losing one is painful -- the two cores represent "
        "irreplaceable human lives. The intelligence a Theodolite provides is often more "
        "valuable than what a cruiser could accomplish by fighting. Carries extended "
        "supplies for long-duration intelligence missions deep behind enemy lines."
    ),
    exterior_appearance_description=(
        "A 168-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "-- slightly longer and narrower in proportion. The hull is seamless. No windows. An "
        "ion cannon behind a flush panel on the top. Sensor equipment behind flush panels at "
        "the front -- no visible antenna or dishes. Engine bells recessed into sculpted "
        "cavities at the rear. Indigo trim in thin geometric lines along the hull. Ice blue "
        "lines trace neural interface pathways across the hull in a branching network pattern, "
        "faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The forward third of the ship is given over entirely to the sensor array and its "
        "processing systems. The two core chambers sit adjacent to the array, their "
        "occupants permanently immersed in a torrent of electromagnetic data that they "
        "experience as a vast, shifting landscape of light and sound. The crew spaces are "
        "aft -- functional, quiet, and designed for the long silences of an intelligence "
        "mission. A dedicated analysis compartment lets the crew replay and examine "
        "sensor recordings through their neural links. The ship runs quieter than any "
        "other Polaran vessel -- even the life support is dampened to minimize emissions."
    ),
    minimum_crew=[{"officers": 4}, {"crew": 20}],
    secondary_crew=[{"intelligence_analysts": 8}, {"sensor_specialists": 6}],
    additional_systems=[
        "Fused neural cores (x2)",
        "Oversized passive sensor array",
        "Neural interface stations (bridge)",
        "Neural analysis suite",
        "Hard-jump drive",
        "Emission dampening system",
    ],
)

PRECIPITATOR = ShipTemplate(
    name="Precipitator",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=140,
    armor=16,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=68,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.PLASMA_CANNON, weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Fast escort frigate with core-assisted point defense tracking",
    long_description=(
        "The Precipitator provides a defensive umbrella over convoys and transport groups. "
        "Its fused core is dedicated almost entirely to tracking and point defense "
        "coordination -- identifying, classifying, and engaging incoming small craft and "
        "torpedoes with a speed and precision that no baseline crew can match. The core "
        "tracks dozens of targets simultaneously, assigning priority and directing fire "
        "without conscious crew input. The linked crew handles maneuvering and ship-to-ship "
        "engagements while the core handles the defensive screen. This division of labor "
        "makes the Precipitator one of the most effective anti-small-craft platforms in "
        "known space relative to its size."
    ),
    exterior_appearance_description=(
        "A 140-meter military spacecraft with a pale grey hull. A smooth, compact ellipsoid. "
        "The hull is seamless. No windows. A plasma cannon behind a flush panel on the top. A "
        "light ion turret behind a flush panel on the upper hull. Engine bells recessed into "
        "sculpted cavities at the rear. Indigo trim in thin geometric lines -- parallel "
        "stripes and concentric rings around weapon panels. Ice blue lines trace neural "
        "interface pathways across the hull in a branching network pattern, converging on the "
        "core chamber amidships, faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The core chamber is positioned centrally with direct hardline connections to every "
        "point defense turret -- no network lag, no signal processing delay. The bridge crew "
        "operates in neural cradles arranged around the core, aware through their links of "
        "every target the core is tracking. The effect is disconcerting for new crew: a "
        "constant peripheral awareness of dozens of threat vectors being managed "
        "simultaneously by an intelligence that isn't quite the ship and isn't quite a "
        "person. The turret maintenance bays line both flanks, kept spotlessly clean."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 22}],
    secondary_crew=[{"gunners": 8}, {"turret_maintenance": 4}],
    additional_systems=[
        "Fused neural core (x1, point defense dedicated)",
        "Core-guided point defense network",
        "Neural interface stations (bridge)",
        "Multi-target tracking array",
    ],
)

FARADAY = ShipTemplate(
    name="Faraday",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=228,
    armor=45,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=210,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[
        weapons.RAILGUN,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Core-shielded fleet destroyer with neural point defense network",
    long_description=(
        "The Faraday is the shield of the Polaran battle fleet. Its three fused cores "
        "divide responsibility -- one tracks incoming threats, one coordinates point "
        "defense fire, one manages the ship itself -- allowing targeting response times "
        "that no purely human crew can achieve. The Faraday's core-guided point defense "
        "turrets are slightly more powerful than standard models, each core-linked weapon "
        "achieving a precision that compensates for lighter Polaran armor. A capital ship "
        "without Faraday escorts is vulnerable to a coordinated strike; a capital ship "
        "with three Faradays is very hard to reach. The Faraday is faster than the "
        "template fleet destroyer -- Moderate speed where the standard is Slow -- reflecting "
        "the Polaran doctrine of positioning speed over passive protection."
    ),
    exterior_appearance_description=(
        "A 228-meter military spacecraft with a pale grey hull. A smooth, broad ellipsoid -- "
        "wider and heavier in proportion, with a continuous curved surface. The hull is "
        "seamless. No windows. A railgun behind a long flush panel along the top. Two heavy "
        "laser arrays behind flush panels on the upper hull and sides. Engine bells recessed "
        "into sculpted cavities distributed across the rear. Indigo trim in thin precise "
        "geometric lines -- parallel stripes along the hull, concentric rings around weapon "
        "panels, angular patterns converging on the core chamber. Ice blue lines trace neural "
        "interface pathways across the hull in an elaborate branching network, converging "
        "amidships -- faintly luminous, glowing brighter when active. An indigo neural node "
        "emblem on both sides. Ship designation in indigo on the upper hull."
    ),
    interior_appearance_description=(
        "Three core chambers are distributed through the hull -- one forward near the "
        "sensor arrays, one amidships near the point defense coordination nexus, and one "
        "aft near engineering. Each core experiences the battlespace differently: the "
        "threat-tracking core perceives incoming contacts as a field of moving lights, "
        "the PD core experiences weapon firing solutions as geometric patterns, and the "
        "ship-management core feels the vessel's systems as an extension of its own body. "
        "The bridge crew works in neural cradles, each sharing awareness with the cores "
        "relevant to their role. The point defense bays are maintained to exacting "
        "standards -- the cores notice degradation before diagnostic systems do."
    ),
    minimum_crew=[{"officers": 15}, {"crew": 80}],
    secondary_crew=[{"gunners": 25}, {"point_defense_crew": 30}, {"damage_control": 20}],
    additional_systems=[
        "Fused neural cores (x3)",
        "Core-guided point defense network",
        "Neural interface stations (bridge)",
        "Distributed core architecture",
        "Fleet neural relay",
    ],
)

ASPIRATOR = ShipTemplate(
    name="Aspirator",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=215,
    armor=33,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=170,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fast pursuit destroyer with torpedo and medium-jump capability",
    long_description=(
        "The Aspirator is the Polaran pursuit ship -- designed to chase down and kill "
        "corvettes, frigates, and pirate vessels across medium-jump routes. Faster than "
        "the template hunter destroyer, with two fused cores dedicated to tracking and "
        "pursuit coordination. Once an Aspirator locks onto a target through its cores' "
        "predictive tracking, escape is nearly impossible -- the cores calculate intercept "
        "vectors faster than a fleeing ship can change course. Carries an antimatter "
        "torpedo for finishing off prey at close range. Often operates in pairs, the two "
        "ships' cores sharing tracking data through neural relay to cut off escape routes. "
        "A pair of Aspirators showing up in a system is a statement that the Polaris "
        "consider the situation serious."
    ),
    exterior_appearance_description=(
        "A 215-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "-- lean and narrow in proportion. The hull is seamless. No windows. A heavy particle "
        "cannon behind a flush panel extending from the front. A torpedo bay behind a flush "
        "panel in the lower front. An ion turret behind a flush panel on the upper hull. "
        "Engine bells recessed into sculpted cavities at the rear. Indigo trim in thin "
        "geometric lines along the hull. Ice blue lines trace neural interface pathways across "
        "the hull in a branching network pattern, converging on the core chamber, faintly "
        "luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The two core chambers sit flanking the central corridor amidships, their occupants "
        "permanently focused on tracking and pursuit calculations. The bridge crew "
        "experiences the cores' tracking data as an intuitive sense of where the target "
        "will be -- not where it is, but where it's going. The torpedo room is forward, "
        "its crew trained for rapid loading because an Aspirator in pursuit may get only "
        "one chance at a close-range shot. Crew quarters reflect the ship's operational "
        "pattern: long stretches of patrol punctuated by intense pursuit, with a small "
        "gym and VR recreation space to keep the crew sharp during the waiting."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 65}],
    secondary_crew=[{"gunners": 15}, {"torpedo_crew": 6}, {"sensor_specialists": 8}],
    additional_systems=[
        "Fused neural cores (x2)",
        "Predictive tracking system",
        "Neural interface stations (bridge)",
        "Paired-ship neural relay",
    ],
)

EPHEMERIS = ShipTemplate(
    name="Ephemeris",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Infiltrator Destroyer",
    combat_role="Forward command / deep reconnaissance",
    length=235,
    armor=22,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=105,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=56,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON],
    default_small_craft=[],
    short_description="Hard-jump command destroyer with neural coordination hub",
    long_description=(
        "The Ephemeris is the largest Polaran ship capable of navigating hard jump "
        "points. It pays dearly for the privilege -- reduced armament, reduced armor, an "
        "oversized jump drive -- but what it brings through a hard jump is irreplaceable: "
        "a neural command hub for an entire deep operation. The Ephemeris's four fused "
        "cores serve as the coordination nexus for all Polaran assets operating behind "
        "enemy lines -- Theodolite scout frigates, Trocar insertion transports, and Ampoule "
        "logistics corvettes all relay through the Ephemeris's cores, which maintain a "
        "unified intelligence picture of the operational area. Losing an Ephemeris means "
        "losing the command node for an entire intelligence network. These are strategic "
        "assets deployed sparingly and recovered carefully. Extended supply duration "
        "supports deep operations lasting months."
    ),
    exterior_appearance_description=(
        "A 235-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "with an exceptionally clean hull surface -- even by Polaran standards, minimal "
        "features. The hull is seamless. No windows. A heavy particle cannon behind a flush "
        "panel extending from the front. No other visible weapons. Engine bells recessed "
        "deeply into sculpted cavities at the rear. Minimal markings -- indigo trim limited to "
        "thin lines along the centreline. Ice blue neural pathway lines are dimmer than "
        "standard, barely visible. A small indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The interior is divided between the hard-jump drive (which occupies nearly a "
        "third of the ship's volume), the four core chambers, and the command coordination "
        "center. The CCC is the ship's heart -- a room of neural cradles where intelligence "
        "officers link in and perceive the combined sensor feeds of every Polaran asset in "
        "the operational area, assembled into a single coherent picture by the cores. The "
        "four cores are arranged in a hierarchy: two handle operational coordination, one "
        "manages the ship, and one serves as a dedicated communications processor. Crew "
        "quarters are functional and designed for long deployments. A small medical bay "
        "includes neural repair equipment."
    ),
    minimum_crew=[{"officers": 14}, {"crew": 60}],
    secondary_crew=[{"intelligence_officers": 12}, {"communications": 8}, {"sensor_specialists": 6}],
    additional_systems=[
        "Fused neural cores (x4)",
        "Hard-jump drive",
        "Command coordination center",
        "Deep operations neural relay hub",
        "Neural interface stations (bridge)",
        "Emission dampening system",
    ],
)

ACCELERATOR = ShipTemplate(
    name="Accelerator",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Siege Destroyer",
    combat_role="Anti-capital firepower on a destroyer hull",
    length=210,
    armor=16,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=115,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[weapons.SIEGE_CANNON],
    default_small_craft=[],
    short_description="Core-aimed siege platform with extreme-range cannon",
    long_description=(
        "The Accelerator mounts a siege cannon -- the same class of weapon carried by the "
        "Stellarator dreadnought -- on a destroyer-sized hull. Everything else has been "
        "sacrificed to make this possible: less armor than a frigate, no point defense, no "
        "secondary weapons. What it has instead is a single fused core dedicated entirely "
        "to fire control, achieving a targeting precision at extreme range that partially "
        "compensates for the absence of paired cannons. A pair of Accelerators firing at "
        "a battleship is a serious threat -- and at Extreme range, they can engage before "
        "most targets can fire back. But the Accelerator cannot defend itself against "
        "anything except the capital ship it's shooting at. Without Faraday escorts, an "
        "Accelerator dies to the first fighter wing or torpedo frigate that reaches it."
    ),
    exterior_appearance_description=(
        "A 210-meter military spacecraft with a pale grey hull. A smooth, squat ellipsoid -- "
        "shorter and thicker in proportion, built around the siege cannon. The hull is "
        "seamless. No windows. A siege cannon behind a long flush panel running the full "
        "length of the top. Engine bells recessed into sculpted cavities at the rear. Indigo "
        "trim in thin geometric lines along the hull and concentric rings around the cannon "
        "panel seam. Ice blue lines trace neural interface pathways across the hull in a "
        "branching network, converging on the core chamber, faintly luminous. An indigo neural "
        "node emblem on both sides."
    ),
    interior_appearance_description=(
        "The ship is built around the weapon. The siege cannon's magnetic accelerator "
        "runs the full length of the vessel, with the crew spaces, core chamber, and "
        "engineering packed into the remaining volume like an afterthought. The single "
        "core chamber sits directly adjacent to the cannon's fire control systems, its "
        "occupant experiencing each firing solution as a geometric certainty -- the core "
        "doesn't aim so much as know where the shot will land. The bridge is a minimal "
        "cluster of neural cradles forward. There is no wardroom, no recreation space, "
        "no comfort. The Accelerator exists to fire its cannon, and everything aboard "
        "serves that purpose."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 40}],
    secondary_crew=[{"gunnery_specialists": 12}, {"damage_control": 8}],
    additional_systems=[
        "Fused neural core (x1, fire control dedicated)",
        "Neural interface stations (bridge)",
        "Spinal siege cannon mount",
    ],
)

ASTROLABE = ShipTemplate(
    name="Astrolabe",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=410,
    armor=62,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=380,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=49,
    default_weapons=[
        weapons.PRECISION_RAILGUN,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Eight-core heavy cruiser with core-coordinated gunnery",
    long_description=(
        "The Astrolabe is the Polaran main line combatant and the ship where their naval "
        "philosophy becomes genuinely frightening. Its eight fused cores divide the work "
        "of running a warship in combat -- navigation, gunnery, damage control, sensor "
        "processing, communications, point defense -- each core dedicated to a domain, "
        "each operating at a speed and focus no human crew can sustain. The result is a "
        "cruiser that fights like something much larger. An Astrolabe in a turning fight "
        "will outmaneuver heavier ships from other factions thanks to its Moderate speed "
        "(where the template heavy cruiser is Slow), and its core-coordinated gunnery "
        "achieves hit rates that border on precognitive. Less armored than its template "
        "equivalent, the Astrolabe compensates by simply not being where incoming fire "
        "expects it to be."
    ),
    exterior_appearance_description=(
        "A 410-meter military spacecraft with a pale grey hull. A smooth, massive ellipsoid -- "
        "a continuous curved surface with no flat faces or angular features. The hull is "
        "seamless. No windows. A precision railgun behind a long flush panel along the top. "
        "Weapon batteries behind flush panels along both sides. Point-defense mounts behind "
        "flush panels distributed across the hull. Engine bells recessed into sculpted "
        "cavities distributed across the rear and underside. Indigo trim in precise geometric "
        "lines -- parallel stripes, concentric rings around weapon panels, angular convergence "
        "patterns amidships. Ice blue lines trace neural interface pathways across the hull in "
        "an elaborate branching network, converging on the core chamber amidships -- luminous, "
        "glowing visibly when active. An indigo neural node emblem at large scale on both "
        "sides. Ship name in indigo on the upper hull."
    ),
    interior_appearance_description=(
        "The eight core chambers are distributed throughout the hull in individually "
        "hardened compartments, each linked to its area of responsibility. The gunnery "
        "core sits near the main battery. The damage control core is amidships near the "
        "engineering spaces. The navigation core is forward. Destroying individual cores "
        "degrades capability but doesn't cripple the ship -- surviving cores redistribute "
        "the workload, the ship getting slower and less precise as cores die but never "
        "going fully dark until the last one is gone. The bridge is a command ring of "
        "neural cradles where senior officers experience the combined awareness of all "
        "eight cores simultaneously -- a sensation most describe as overwhelming the first "
        "time and addictive thereafter. Crew quarters are small but well-appointed for "
        "extended deployment. The ship has a quiet intensity to it -- the cores are always "
        "working, and the crew can feel it through their links."
    ),
    minimum_crew=[{"senior_officers": 6}, {"officers": 34}, {"crew": 280}],
    secondary_crew=[{"gunners": 60}, {"point_defense_crew": 30}, {"damage_control": 45}, {"sensor_specialists": 15}],
    additional_systems=[
        "Fused neural cores (x8)",
        "Distributed core architecture",
        "Core-coordinated gunnery system",
        "Neural interface stations (bridge)",
        "Fleet neural relay",
    ],
)

OCTANT = ShipTemplate(
    name="Octant",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=385,
    armor=46,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=260,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=49,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Fast medium-jump cruiser leading flanking task forces",
    long_description=(
        "The Octant is the largest Polaran combat ship that can use medium jump points. "
        "It serves as the backbone of flanking forces -- when a Polaran task force comes "
        "through a medium jump to hit the enemy's rear, the Octant is the biggest gun "
        "they've got. Six fused cores provide the coordination that makes a Polaran "
        "flanking force fight like a fleet twice its size. The Octant is notably faster "
        "than the template light cruiser, reaching Fast speed where the standard is "
        "Moderate -- critical for a ship whose doctrine depends on arriving where it's "
        "not expected and hitting before the enemy can reposition. Less armored than its "
        "template equivalent, but the six cores provide enough coordination to keep the "
        "ship ahead of incoming fire."
    ),
    exterior_appearance_description=(
        "A 385-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "-- longer and narrower in proportion. The hull is seamless. No windows. A heavy "
        "railgun behind a flush panel along the top. Two laser turrets behind flush panels on "
        "the upper hull. Engine bells recessed into sculpted cavities at the rear. Indigo trim "
        "in precise geometric lines along the hull. Ice blue lines trace neural interface "
        "pathways across the hull in a branching network, converging on the core chamber, "
        "luminous when active. An indigo neural node emblem on both sides. Ship name in indigo "
        "on the upper hull."
    ),
    interior_appearance_description=(
        "The six core chambers are arranged in two tiers -- four handling ship operations "
        "and two dedicated to task force coordination when the Octant serves as flagship "
        "of a flanking group. The bridge includes additional neural stations for task "
        "force command staff. The ship is designed for the intensity of independent "
        "operations: a full medical bay, a dedicated intelligence analysis room, and "
        "crew facilities a step above the spartan standard of smaller Polaran vessels. "
        "The coordination cores give the Octant's captain an awareness of every ship in "
        "their task force -- their status, their ammunition, their crew condition -- "
        "experienced as an intuitive sense rather than a data readout."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 26}, {"crew": 200}],
    secondary_crew=[{"gunners": 35}, {"point_defense_crew": 20}, {"damage_control": 30}, {"task_force_staff": 10}],
    additional_systems=[
        "Fused neural cores (x6)",
        "Distributed core architecture",
        "Task force coordination suite",
        "Neural interface stations (bridge)",
        "Fleet neural relay",
    ],
)

ARMILLARY = ShipTemplate(
    name="Armillary",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Carrier",
    combat_role="Cruiser combatant with embarked small craft",
    length=395,
    armor=40,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=255,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[
        weapons.RAILGUN,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[("Scalpel", 10)],
    short_description="Light carrier with neural relay to embarked interceptor wing",
    long_description=(
        "The Armillary is a cruiser hull that trades armor and broadside batteries for a "
        "hangar bay carrying a full wing of ten Scalpel interceptors. Unlike a pure "
        "carrier, the Armillary fights with its own railgun while its wing provides "
        "capability the cruiser line otherwise lacks -- fast interceptors to chase down "
        "enemy frigates, screen against enemy small craft, or harry capital ships. The "
        "Armillary's six cores split between ship operations and wing coordination, "
        "maintaining a direct neural relay with every embarked pilot. The result is a "
        "wing that moves with the eerie Polaran synchronization -- each Scalpel receiving "
        "tactical updates directly from a dedicated core's awareness. The ship's defensive "
        "systems provide cover for its craft during launch and recovery."
    ),
    exterior_appearance_description=(
        "A 395-meter military spacecraft with a pale grey hull. A smooth, wide ellipsoid -- "
        "broader and flatter in proportion. The hull is seamless. No windows. Launch bays "
        "along both sides as clean rectangular apertures in the curved hull. A railgun behind "
        "a flush panel along the top forward of the launch bays. Two heavy laser arrays behind "
        "flush panels on the upper hull. Engine bells recessed into sculpted cavities "
        "distributed across the rear. Indigo trim in precise geometric lines -- parallel "
        "stripes and concentric rings around the launch apertures. Ice blue lines trace neural "
        "interface pathways across the hull in a branching network, converging on the core "
        "chamber, luminous when active. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The aft third of the ship is hangar space -- a cavernous bay where ten Scalpels "
        "sit in neural-linked launch cradles, their pilots able to link in from the "
        "ready room and launch within seconds. The wing coordination cores sit adjacent "
        "to the hangar, their occupants perceiving each Scalpel as an extension of their "
        "own awareness. The forward two-thirds house the bridge, crew quarters, and "
        "combat systems. A flight operations center near the hangar serves as the nerve "
        "center during strike operations -- the wing coordinator's neural cradle here is "
        "the most demanding station on the ship, managing ten simultaneous pilot feeds."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 21}, {"crew": 170}],
    secondary_crew=[
        {"ship_gunners": 20},
        {"embarked_craft_pilots": 10},
        {"wing_coordinators": 3},
        {"hangar_maintenance": 20},
    ],
    additional_systems=[
        "Fused neural cores (x6)",
        "Wing coordination neural relay",
        "Hangar bay (10 small craft)",
        "Craft neural launch cradles",
        "Small craft shield system",
        "Neural interface stations (bridge)",
    ],
)

CYCLOTRON = ShipTemplate(
    name="Cyclotron",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=920,
    armor=78,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1400,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=70,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Twenty-five-core battleship that reacts as a single organism",
    long_description=(
        "The Cyclotron is the Polaran battleship. Its twenty-five fused cores are "
        "distributed throughout the hull in hardened chambers, each handling a slice of "
        "the ship's operations -- gunnery sections, engine control, sensor arrays, point "
        "defense zones, damage control sectors. The cores communicate with each other and "
        "with the linked crew at neural speed, making the Cyclotron react as a single "
        "organism rather than a crewed vessel. Faster than any other faction's battleship "
        "-- Fast speed where the template is Moderate -- the Cyclotron closes and kills "
        "with an aggression that belies its size. Less armored than the template "
        "battleship, it compensates through core-coordinated evasion and the sheer speed "
        "of its damage control response. Destroying individual cores degrades capability "
        "but doesn't cripple it -- the remaining cores redistribute workload, the ship "
        "getting slower and less precise as cores die but never going fully dark until "
        "the last one is gone. Somewhere in the Cyclotron's core chambers are twenty-five "
        "people who will never leave."
    ),
    exterior_appearance_description=(
        "A 920-meter military spacecraft with a pale grey hull. A massive, smooth ellipsoid -- "
        "a continuous curved surface at enormous scale. The hull is seamless. No windows. A "
        "gauss cannon behind a long flush panel along the top. Weapon batteries behind flush "
        "panels along both sides. Point-defense mounts behind flush panels distributed across "
        "the hull. Engine bells recessed into sculpted cavities distributed across the rear "
        "and underside. Indigo trim in precise geometric lines at large scale -- parallel "
        "stripes, concentric rings, angular convergence patterns. Ice blue lines trace neural "
        "interface pathways across the hull in an extensive branching network, converging on "
        "the core chamber -- luminous, glowing visibly at distance when active. An indigo "
        "neural node emblem at large scale on both sides. Ship name in indigo at large scale "
        "on the upper hull."
    ),
    interior_appearance_description=(
        "The twenty-five core chambers are distributed like organs through a body -- each "
        "in its own hardened compartment, each connected to its neighbors by redundant "
        "neural conduits. Walking the corridors, the crew feels the cores' presence as a "
        "background awareness -- a sense that the ship is thinking around them, aware of "
        "their position and status. The bridge is a command amphitheater of neural cradles "
        "where the captain and senior officers experience the combined awareness of all "
        "twenty-five cores. First-time visitors to the bridge describe the sensation as "
        "standing inside a mind. Crew quarters are larger than on smaller Polaran vessels "
        "but still austere. The ship carries a full medical bay, neural repair facilities, "
        "and a shrine -- maintained by the crew -- to the twenty-five who gave their lives "
        "to become the ship."
    ),
    minimum_crew=[{"senior_officers": 15}, {"officers": 105}, {"crew": 1200}],
    secondary_crew=[
        {"gunners": 200},
        {"point_defense_crew": 120},
        {"damage_control": 180},
        {"sensor_specialists": 40},
        {"medical": 30},
    ],
    additional_systems=[
        "Fused neural cores (x25)",
        "Distributed core architecture with redundant neural conduits",
        "Core-coordinated gunnery system",
        "Core-guided point defense network",
        "Neural interface stations (bridge amphitheater)",
        "Fleet neural relay",
        "Neural repair facilities",
    ],
)

ORRERY = ShipTemplate(
    name="Orrery",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1180,
    armor=42,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1100,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=70,
    default_weapons=[
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_PD,
        weapons.LASER_PD,
        weapons.LASER_PD,
    ],
    default_small_craft=[
        ("Retort", 10),
        ("Retort", 10),
        ("Scalpel", 10),
        ("Scalpel", 10),
    ],
    short_description="Forty-core carrier that orchestrates its wings as a single swarm",
    long_description=(
        "The Orrery is the Polaran fleet carrier. Its forty fused cores are split between "
        "ship operations and strike coordination -- roughly half run the carrier itself, "
        "while the other half maintain direct neural relay with every pilot in the wing. "
        "The result is a carrier that doesn't just launch strike craft -- it orchestrates "
        "them as a single coordinated swarm, each pilot receiving tactical updates directly "
        "from a dedicated core's awareness. An Orrery's strike wing moves with an eerie "
        "synchronization that no amount of radio communication can replicate. The Orrery "
        "deploys four wings -- typically two wings of Retort bombers and two wings of "
        "Scalpel interceptors -- though composition varies by mission. The carrier's own "
        "combat capability is minimal: point defense only. Medium-jump capable, allowing "
        "it to project strike power through flanking routes that battleships cannot use. "
        "Its defensive systems provide cover for its craft during launch and recovery."
    ),
    exterior_appearance_description=(
        "A 1180-meter military spacecraft with a pale grey hull. A smooth elongated ellipsoid "
        "-- a continuous curved surface with no sharp edges or angular features. The hull is "
        "seamless with no visible plate joins or external fittings. Hangar openings along both "
        "sides are clean rectangular apertures cut into the curved hull. Communications arrays "
        "on the top, integrated into the hull surface. Laser turrets behind flush panels along "
        "the sides. Engine bells recessed into sculpted cavities distributed across the rear "
        "and underside. Indigo trim in thin precise geometric lines -- parallel stripes, "
        "concentric rings around the hangar openings, angular patterns converging amidships. "
        "Ice blue lines trace neural interface pathways across the hull surface in a branching "
        "network pattern, converging toward the core chambers amidships -- faintly luminous, "
        "glowing brighter when the ship's neural systems are active. An indigo neural node "
        "emblem at large scale on both sides."
    ),
    interior_appearance_description=(
        "The Orrery's interior is dominated by its four hangar bays -- vast spaces where "
        "forty strike craft sit in neural-linked launch cradles, ready to deploy in "
        "seconds. The twenty wing coordination cores are arranged in a dedicated "
        "operations center adjacent to the hangars, their occupants each linked to two "
        "or three pilots simultaneously, experiencing the battle through their eyes. The "
        "remaining twenty cores handle the carrier itself. Crew spaces are extensive -- "
        "the Orrery carries thousands and must function as a self-contained community for "
        "months. Medical facilities include neural repair, essential for maintaining both "
        "cores and pilots. The flight operations center is the ship's beating heart during "
        "combat -- a room of neural cradles where wing coordinators experience the entire "
        "strike as a unified awareness, guiding forty craft as one mind."
    ),
    minimum_crew=[{"senior_officers": 25}, {"officers": 175}, {"crew": 2500}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"wing_coordinators": 20},
        {"flight_deck_crew": 200},
        {"hangar_maintenance": 150},
        {"ship_gunners": 40},
        {"damage_control": 120},
        {"medical": 50},
    ],
    additional_systems=[
        "Fused neural cores (x40)",
        "Distributed core architecture with redundant neural conduits",
        "Wing coordination neural relay (20 dedicated cores)",
        "Hangar bays (x4, 10 craft each)",
        "Craft neural launch cradles",
        "Small craft shield system",
        "Neural interface stations (bridge)",
        "Fleet neural relay",
        "Neural repair facilities",
        "Strike operations center",
    ],
)

STELLARATOR = ShipTemplate(
    name="Stellarator",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=1780,
    armor=90,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=2400,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=84,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="One hundred and twenty core dreadnought with twin siege cannons",
    long_description=(
        "The Stellarator is the largest and most powerful vessel in the Polaran fleet. "
        "It carries over one hundred and twenty fused cores distributed across every major "
        "system -- a small city's worth of human brains permanently integrated into the "
        "ship's architecture. The cores form a layered hierarchy: dozens handle local ship "
        "functions, scores manage fleet-wide coordination, and a command tier of senior "
        "cores -- often volunteers who were once flag officers themselves -- oversee strategic "
        "decision-making. The Stellarator thinks faster than any crew could communicate, "
        "reacts faster than any captain could order, and coordinates a fleet with a "
        "precision that approaches telepathy. Its twin siege cannons fire at Extreme range "
        "with core-guided accuracy. Its single plasma point defense turret is its only "
        "defense against small craft -- making it desperately dependent on its Faraday "
        "escorts. Only a handful exist. Each one consumed over a hundred human lives to "
        "build, and every one of those people is still in there -- conscious, aware, and "
        "never leaving. The Stellarator is the pinnacle of Polaran naval philosophy and "
        "its most damning indictment."
    ),
    exterior_appearance_description=(
        "A 1780-meter military spacecraft with a pale grey hull. A massive elongated ellipsoid "
        "-- a continuous curved surface at enormous scale, tapering at both ends. The hull is "
        "seamless. No windows. Twin siege cannons behind long flush panels running much of the "
        "top surface, the panels opening for firing. Point-defense mounts behind flush panels "
        "distributed across the hull. Engine bells recessed into sculpted cavities distributed "
        "across the rear and underside. Indigo trim in precise geometric lines at large scale "
        "-- parallel stripes along the full length, concentric rings around the cannon panels, "
        "angular convergence patterns amidships. Ice blue lines trace neural interface "
        "pathways across the entire hull surface in an extensive branching network, converging "
        "on the core chamber -- luminous, glowing visibly at distance when active. An indigo "
        "neural node emblem at massive scale on both sides. Ship name in indigo at large scale "
        "on the upper hull."
    ),
    interior_appearance_description=(
        "The Stellarator's interior is a city. Over a hundred and twenty core chambers are "
        "distributed through the hull like neurons through a brain, each in its own "
        "hardened compartment, connected by redundant neural conduits that pulse with data. "
        "The command tier cores occupy a reinforced section deep in the ship's center -- "
        "former admirals and strategists whose experience now runs the fleet. The bridge "
        "is a vast amphitheater of neural cradles where the captain and flag staff "
        "experience the combined awareness of every core aboard -- a sensation that has "
        "been described as feeling like a god and a prisoner simultaneously. Crew quarters, "
        "mess halls, medical bays, neural repair facilities, recreation spaces, and a "
        "memorial hall listing every core by their original name fill the living spaces. "
        "The memorial hall is always lit, always quiet, and always visited. The "
        "Stellarator's crew lives alongside the people who became the ship, and they "
        "never forget it."
    ),
    minimum_crew=[{"senior_officers": 50}, {"officers": 350}, {"crew": 5000}],
    secondary_crew=[
        {"gunners": 300},
        {"point_defense_crew": 80},
        {"damage_control": 500},
        {"sensor_specialists": 100},
        {"fleet_coordination_staff": 80},
        {"medical": 120},
        {"neural_maintenance": 60},
    ],
    additional_systems=[
        "Fused neural cores (x120+)",
        "Hierarchical core architecture (local, fleet, command tiers)",
        "Redundant neural conduit network",
        "Core-guided siege cannon targeting",
        "Fleet-wide neural coordination hub",
        "Neural interface stations (command amphitheater)",
        "Neural repair facilities",
        "Core memorial hall",
    ],
)

REFRACTOR = ShipTemplate(
    name="Refractor",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Fleet Tender",
    combat_role="Resupply / ammunition and fuel transport",
    length=340,
    armor=24,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=140,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Fleet logistics backbone carrying fuel, ammunition, and interface hardware",
    long_description=(
        "The Refractor is the Polaran logistics backbone. It carries fuel, ammunition, "
        "spare parts, replacement neural interface hardware, and consumables for extended "
        "fleet operations. A Polaran fleet's operational range is limited by its "
        "Refractors -- without them, interface hardware degrades, ammunition runs dry, and "
        "the fleet's core-driven coordination advantage vanishes. The Refractor also "
        "carries limited repair facilities for field maintenance on damaged ships, "
        "including specialized equipment for neural conduit repair. Travels with the fleet "
        "rather than waiting at fixed supply points."
    ),
    exterior_appearance_description=(
        "A 340-meter military spacecraft with a pale grey hull. A smooth, bulky ellipsoid -- "
        "wider and rounder in proportion. The hull is seamless. No windows. Docking clamps and "
        "transfer fittings along both sides, integrated into the hull as smooth protrusions. "
        "An ion turret behind a flush panel on top. A point-defense mount behind a flush panel "
        "at the rear. Engine bells recessed into sculpted cavities at the rear. Indigo trim in "
        "thin geometric lines along the hull and concentric rings around the docking fittings. "
        "Ice blue lines trace neural interface pathways across the hull, faintly luminous. An "
        "indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The Refractor's interior is mostly cargo space -- modular containers of ammunition, "
        "fuel cells, spare interface leads, neural conduit sections, and the thousand other "
        "items a fleet consumes. The crew spaces forward are functional and unceremonious. "
        "A small repair bay amidships has the equipment to splice neural conduits and "
        "recalibrate interface hardware -- skilled work performed by technicians who "
        "understand that a damaged conduit can mean a core in pain. The Refractor has no "
        "fused cores, making it one of the few Polaran vessels where the crew operates "
        "through conventional neural links only."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 60}],
    secondary_crew=[{"cargo_handlers": 30}, {"repair_technicians": 15}, {"neural_interface_specialists": 8}],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Modular cargo system",
        "Neural conduit repair bay",
        "Interface hardware storage",
    ],
)

AMPOULE = ShipTemplate(
    name="Ampoule",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Logistics Corvette",
    combat_role="Emergency resupply / hard-jump logistics",
    length=55,
    armor=7,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=32,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump logistics corvette supplying deep operations",
    long_description=(
        "The Ampoule is the smallest dedicated logistics vessel in the Polaran fleet, "
        "built around a hard-jump drive. It carries limited supplies -- enough to resupply "
        "a Theodolite scout frigate or Ephemeris infiltrator destroyer operating deep "
        "behind enemy lines. The Ampoule's existence is what makes extended hard-jump "
        "intelligence operations possible. Without it, a deep operation's duration is "
        "limited to what the ships launched with. With it, operations can last months. "
        "Crucially, the Ampoule carries replacement neural interface hardware -- the most "
        "critical consumable for a Polaran fleet, and the one that degrades fastest under "
        "field conditions."
    ),
    exterior_appearance_description=(
        "A 55-meter military spacecraft with a pale grey hull. A smooth, compact ellipsoid. "
        "The hull is seamless. No windows. Loading hatches integrated into the sides as flush "
        "panels. A light ion turret behind a flush panel on top. Engine bells recessed into "
        "sculpted cavities at the rear. Indigo trim in thin geometric lines along the hull. "
        "Ice blue lines trace neural interface pathways across the hull, faintly luminous. An "
        "indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The hard-jump drive and cargo hold consume most of the interior. Crew spaces are "
        "minimal -- bunks, a tiny galley, and a bridge barely large enough for three neural "
        "cradles. The cargo hold is carefully organized with sealed containers of interface "
        "hardware, ammunition, medical supplies, and food. No fused cores -- the Ampoule "
        "runs on a skeleton crew with conventional neural links. The ship has the spartan "
        "feel of something designed for a job, not for people."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 5}],
    secondary_crew=[{"cargo_handlers": 2}],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Hard-jump drive",
        "Sealed cargo system",
        "Interface hardware storage",
    ],
)

AUTOCLAVE = ShipTemplate(
    name="Autoclave",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Field Support Ship",
    combat_role="Medical support / field repair / neural repair",
    length=460,
    armor=35,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=280,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Neural repair and medical ship specializing in interface trauma",
    long_description=(
        "The Autoclave is a dedicated medical and repair vessel specializing in neural "
        "interface injuries -- the most common and most debilitating combat wound in a "
        "Polaran fleet. It carries facilities for emergency disconnection, interface "
        "repair, and long-term neural rehabilitation, alongside conventional trauma care "
        "and ship repair workshops. A damaged neural interface left untreated can cause "
        "permanent cognitive loss; the Autoclave is the difference between a wounded pilot "
        "returning to service and one spending the rest of their life unable to process "
        "sensory input normally. Also handles neural conduit repair on damaged ships "
        "and -- in the most extreme cases -- emergency stabilization of damaged cores. "
        "Medium-jump capable because casualties don't always happen where the capital "
        "fleet is."
    ),
    exterior_appearance_description=(
        "A 460-meter military spacecraft with a pale grey hull. A smooth, wide ellipsoid. The "
        "hull is seamless. No windows. A prominent medical section amidships marked with "
        "indigo and ice blue medical symbols -- the Polaran variant. Docking ports along both "
        "sides integrated into the hull as smooth recesses. An ion cannon behind a flush panel "
        "on top. Two point-defense mounts behind flush panels on the sides. Engine bells "
        "recessed into sculpted cavities at the rear. Indigo trim in precise geometric lines "
        "along the hull. Ice blue lines trace neural interface pathways across the hull in a "
        "branching network, faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The Autoclave's interior is dominated by medical spaces -- surgical bays, neural "
        "rehabilitation wards, and the quiet, heavily shielded rooms where emergency "
        "disconnections are performed. The disconnection suite is the most dreaded space "
        "on the ship: where a failing neural interface is severed before it kills its "
        "user, a procedure that is agonizing and sometimes leaves lasting damage. The "
        "rehabilitation ward is gentler -- neural cradles configured for therapeutic "
        "retraining, helping patients relearn how to process sensory input after interface "
        "trauma. A ship repair workshop occupies the lower decks, with equipment for "
        "splicing neural conduits, recalibrating interface systems, and performing hull "
        "repairs. The medical staff carry a weight that other factions' medics don't -- "
        "some of their patients are cores, conscious and suffering inside damaged ships, "
        "and the best the Autoclave can offer is stabilization until a proper facility "
        "can be reached."
    ),
    minimum_crew=[{"officers": 20}, {"crew": 120}],
    secondary_crew=[
        {"surgeons": 12},
        {"neural_specialists": 20},
        {"rehabilitation_therapists": 8},
        {"repair_technicians": 30},
        {"nurses": 40},
    ],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Surgical bays",
        "Neural disconnection suite",
        "Neural rehabilitation ward",
        "Ship repair workshop",
        "Neural conduit repair facilities",
        "Core stabilization equipment",
        "Patient capacity: 200",
    ],
)

CRUCIBLE = ShipTemplate(
    name="Crucible",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=650,
    armor=70,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=950,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Heavily armored troop transport with neural-linked marine complement",
    long_description=(
        "The Crucible delivers a Polaran ground force into hostile space. It carries "
        "thousands of neural-linked marines plus heavy equipment -- vehicles, siege weapons, "
        "prefabricated fortifications -- all coordinated through a neural command network "
        "that gives the embarked force the same eerie synchronization that defines Polaran "
        "naval operations. The Crucible is built to survive the approach into a contested "
        "system, absorbing fire long enough to deploy its forces. Interface cradles for "
        "embarked troops maintain neural link during transit, because a Polaran marine "
        "disconnected for weeks of travel arrives combat-impaired. Less armored than the "
        "template assault transport -- the Polaris accept this tradeoff to maintain the "
        "neural infrastructure that makes their ground forces fight as one."
    ),
    exterior_appearance_description=(
        "A 650-meter military spacecraft with a pale grey hull. A smooth, massive ellipsoid -- "
        "heavier and thicker in proportion. The hull is seamless. No windows. A particle "
        "cannon behind a flush panel on top. Loading ramps on the underside and rear, "
        "integrated as flush panels that open for deployment. Point-defense mounts behind "
        "flush panels along the sides and top. Engine bells recessed into sculpted cavities "
        "distributed across the rear and underside. Indigo trim in precise geometric lines "
        "along the hull. Ice blue lines trace neural interface pathways across the hull in a "
        "branching network, converging on the core chamber, luminous when active. An indigo "
        "neural node emblem at large scale on both sides."
    ),
    interior_appearance_description=(
        "The Crucible's interior is split between troop spaces and the ship proper. The "
        "troop decks are vast open compartments lined with thousands of neural cradles -- "
        "marines spend transit linked in, running simulations and maintaining the neural "
        "cohesion that makes them effective. The ship's crew operates from a relatively "
        "small section forward. Vehicle bays on the lower decks carry armored transports "
        "and heavy weapons. The deployment bays are designed for rapid disembarkation -- "
        "doors open, ramps extend, and thousands of marines who have been mentally "
        "rehearsing the operation for weeks execute it as a single coordinated action. "
        "The ship has a tense, purposeful atmosphere -- everyone aboard knows they're "
        "going somewhere contested."
    ),
    minimum_crew=[{"officers": 15}, {"crew": 100}],
    secondary_crew=[
        {"marine_officers": 50},
        {"marines": 4000},
        {"vehicle_crew": 200},
        {"medical": 30},
        {"ship_gunners": 20},
    ],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Troop neural cradles (4,000+)",
        "Marine neural command network",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Rapid disembarkation system",
    ],
)

TROCAR = ShipTemplate(
    name="Trocar",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Insertion Transport",
    combat_role="Special operations deployment behind enemy lines",
    length=135,
    armor=7,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=40,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Stealthy hard-jump insertion transport for special operations",
    long_description=(
        "The Trocar is a small, stealthy transport built around a hard-jump drive. It "
        "carries a company-sized element of elite Polaran special forces -- neural-linked "
        "operators who fight with the same synchronization as the fleet, but on the "
        "ground. The Trocar gets its troops in through jump points nobody expects to see "
        "a ship come through, deploys them, and either extracts them later or disappears. "
        "Faster than the template insertion transport, with a lower sensor profile -- the "
        "Polaran emphasis on stealth technology pays dividends here. Lightly armed and "
        "not meant to fight its way in. If a Trocar has been detected, the mission has "
        "already failed. Works in concert with Ephemeris infiltrator destroyers and "
        "Theodolite scout frigates as part of deep operations."
    ),
    exterior_appearance_description=(
        "A 135-meter military spacecraft with a pale grey hull. A smooth, elongated ellipsoid "
        "with an exceptionally clean hull surface. The hull is seamless. No windows. A light "
        "ion turret behind a flush panel on top. Loading ramps on the underside, integrated as "
        "flush panels. Engine bells recessed deeply into sculpted cavities at the rear. "
        "Minimal markings -- indigo trim limited to thin lines along the centreline. Ice blue "
        "neural pathway lines are dim, barely visible. A small indigo neural "
        "node emblem on both sides."
    ),
    interior_appearance_description=(
        "The interior is split between the hard-jump drive, a small crew section, and the "
        "troop compartment. The troop compartment holds neural cradles for the embarked "
        "operators -- they spend transit linked in, running the operation in simulation "
        "until they can execute it in their sleep. The crew section is minimal: three "
        "neural cradles for the bridge crew, bunks, and a tiny galley. Everything is "
        "designed to minimize emissions -- even the life support runs quieter than "
        "standard. The ship has the tense, stripped-down feel of something built for a "
        "single purpose."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 6}],
    secondary_crew=[{"special_forces": 40}, {"special_forces_officers": 4}],
    additional_systems=[
        "Neural interface stations (bridge)",
        "Hard-jump drive",
        "Troop neural cradles (44)",
        "Emission dampening system",
        "Radar-absorbing hull coating",
    ],
)

HELIOGRAPH = ShipTemplate(
    name="Heliograph",
    faction=ShipFaction.POLARIS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Comms Ship",
    combat_role="Fleet communications relay / neural network extension",
    length=195,
    armor=17,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=85,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Neural relay ship extending fleet-wide linked communication",
    long_description=(
        "The Heliograph extends the Polaran neural communication network beyond the range "
        "of fixed relay stations. Its two fused cores serve as living signal processors, "
        "maintaining fleet-wide linked communication across an entire star system with a "
        "fidelity that automated relays cannot match. In peacetime, Heliographs serve as "
        "mobile VR infrastructure nodes, extending the civilian neural network to "
        "settlements too small or remote for permanent relay stations. In wartime, they "
        "are priority targets -- destroying the Heliographs degrades the fleet's "
        "coordination from supernatural to merely excellent. The Heliograph is the "
        "invisible backbone of everything that makes a Polaran fleet fight as one mind."
    ),
    exterior_appearance_description=(
        "A 195-meter military spacecraft with a pale grey hull. A smooth ellipsoid with "
        "communications arrays integrated into the upper hull surface -- visible as a series "
        "of smooth, raised geometric shapes rather than protruding masts or dishes. An ion "
        "turret behind a flush panel on top. The hull is seamless. No windows. Engine bells "
        "recessed into sculpted cavities at the rear. Indigo trim in thin geometric lines "
        "along the hull and concentric rings around the communications array housings. Ice "
        "blue lines trace neural interface pathways across the hull in a branching network, "
        "faintly luminous. An indigo neural node emblem on both sides."
    ),
    interior_appearance_description=(
        "The two core chambers are the heart of the ship, their occupants serving as "
        "living signal processors -- receiving, amplifying, and retransmitting neural "
        "communication with a nuance and bandwidth that automated systems can't match. "
        "The cores experience fleet communications as a vast conversation happening at "
        "the speed of thought, filtering and routing thousands of simultaneous neural "
        "links. The rest of the ship is communications equipment -- arrays, amplifiers, "
        "encryption systems, and the power systems to run them all. Crew spaces are "
        "modest. The bridge is quiet and focused. The Heliograph's crew know they are a "
        "priority target and carry themselves accordingly."
    ),
    minimum_crew=[{"officers": 4}, {"crew": 22}],
    secondary_crew=[{"communications_specialists": 10}, {"neural_relay_technicians": 6}],
    additional_systems=[
        "Fused neural cores (x2, communications dedicated)",
        "Neural interface stations (bridge)",
        "Fleet neural relay array",
        "Civilian VR network node capability",
        "Encrypted high-bandwidth communications suite",
    ],
)


POLARIS_SMALL_CRAFT = {
    "Caliper": CALIPER,
    "Retort": RETORT,
    "Scalpel": SCALPEL,
    "Bore": BORE,
}

POLARIS_CORVETTES = {
    "Vernier": VERNIER,
    "Carousel": CAROUSEL,
    "Quadrant": QUADRANT,
}

POLARIS_FRIGATES = {
    "Lancet": LANCET,
    "Compass": COMPASS,
    "Theodolite": THEODOLITE,
    "Precipitator": PRECIPITATOR,
}

POLARIS_DESTROYERS = {
    "Faraday": FARADAY,
    "Aspirator": ASPIRATOR,
    "Ephemeris": EPHEMERIS,
    "Accelerator": ACCELERATOR,
}

POLARIS_CRUISERS = {
    "Astrolabe": ASTROLABE,
    "Octant": OCTANT,
    "Armillary": ARMILLARY,
}

POLARIS_CAPITALS = {
    "Cyclotron": CYCLOTRON,
    "Orrery": ORRERY,
    "Stellarator": STELLARATOR,
}

POLARIS_SUPPORT = {
    "Refractor": REFRACTOR,
    "Ampoule": AMPOULE,
    "Autoclave": AUTOCLAVE,
    "Crucible": CRUCIBLE,
    "Trocar": TROCAR,
    "Heliograph": HELIOGRAPH,
}

POLARIS_ALL_SHIPS = {
    **POLARIS_SMALL_CRAFT,
    **POLARIS_CORVETTES,
    **POLARIS_FRIGATES,
    **POLARIS_DESTROYERS,
    **POLARIS_CRUISERS,
    **POLARIS_CAPITALS,
    **POLARIS_SUPPORT,
}