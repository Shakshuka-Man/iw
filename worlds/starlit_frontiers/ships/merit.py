from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


SPRITE = ShipTemplate(
    name="Sprite",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.SMALL,
    ship_archetype="Scout",
    combat_role="Reconnaissance / forward sensor platform",
    length=12,
    armor=2,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=4,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Standard scout with full instrumentation and ejection system",
    long_description=(
        "The Sprite is the SCN's eyes -- the smallest crewed vessel in the fleet. It is "
        "a thoroughly competent, thoroughly standard scout: full instrumentation, a proper "
        "canopy, cockpit lighting, atmospheric controls, and an ejection system. None of "
        "these things are remarkable. All of them are absent from the Pleiadian Zoog. "
        "The Sprite's pilot is a baseline human using standard instruments with standard "
        "eyes, and the Sprite is designed to make that pilot as effective as possible "
        "through good engineering rather than biological modification or neural "
        "integration. The Sprite is not the fastest scout (the Polaris equivalent is "
        "more agile), not the toughest (the Hyades Dart carries armor), and not the "
        "longest-ranging (the Pleiadian Zoog's modified pilot needs less). But the "
        "Sprite is reliable, well-built, and there are more of them than any other "
        "faction's scout."
    ),
    exterior_appearance_description=(
        "A 12-meter single-seat military spacecraft with a light grey hull. A compact angular "
        "wedge with a glazed canopy on top and a sensor cluster at the front. A small laser "
        "mounted beneath the nose. Two short angled stabiliser fins. Engine bells mounted at "
        "the rear. Navy blue pinstriping along the fuselage centreline. Silver MERIT seal on "
        "the upper fuselage. White running lights at the wingtips."
    ),
    interior_appearance_description=(
        "A single-seat cockpit with standard instruments, standard lighting, standard "
        "atmospheric controls, and a proper ejection system. The pilot wears a standard "
        "flight suit. The instruments are readable by any trained baseline human. The "
        "cockpit is pressurized, heated, and lit. Everything works the way it should."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Ejection system", "Standard instrumentation"],
)

HARPY = ShipTemplate(
    name="Harpy",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=22,
    armor=4,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=8,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Standard antimatter torpedo bomber with full crew safety systems",
    long_description=(
        "The Harpy carries a single antimatter torpedo through enemy point defense to "
        "strike capital ships. The torpedo approach run is the same harrowing experience "
        "for every faction. The difference is what surrounds the crew. A Harpy pilot has "
        "a pressurized cockpit, standard instruments, an ejection system, and a weapons "
        "officer in the tandem seat behind who arms and guides the torpedo through "
        "conventional targeting equipment. No prosthetic interfaces. No neural links. "
        "No modified physiology. Two baseline humans in a well-built bomber doing the "
        "most dangerous job in the fleet. The Harpy is slightly better armored and "
        "hulled than the template, which translates to marginally better survival rates "
        "on the approach run -- not because of exotic technology, but because MERIT's "
        "industrial base builds things a little better across the board."
    ),
    exterior_appearance_description=(
        "A 22-meter two-seat military spacecraft with a light grey hull. A stocky, blunt-nosed "
        "rectangle with a glazed tandem canopy on top. The torpedo housing dominates the "
        "underside. Twin engine bells at the rear. Short swept fins. Navy blue trim along the "
        "torpedo bay edges and engine housing. Silver identification numbers on the upper "
        "fuselage. White running lights at the wingtips."
    ),
    interior_appearance_description=(
        "Two tandem stations -- pilot forward, weapons officer behind -- in a pressurized, "
        "lit, heated cockpit. Standard instruments. Standard targeting equipment. Ejection "
        "systems for both crew. The weapons officer arms and releases the torpedo through "
        "conventional controls. Everything is designed for baseline human operation."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Ejection system (x2)", "Standard targeting suite"],
)

VALKYRIE = ShipTemplate(
    name="Valkyrie",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.SMALL,
    ship_archetype="Interceptor",
    combat_role="Fast attack / anti-scout / anti-bomber",
    length=10,
    armor=1,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=4,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Standard interceptor with minimal armor plating",
    long_description=(
        "The Valkyrie is the SCN interceptor -- the fastest combat craft in the fleet. "
        "Like the Hyades Dart, the MERIT Valkyrie carries a single point of armor where "
        "the template specifies zero, because MERIT's industrial base can afford the "
        "marginal weight cost and the marginal survival benefit adds up across thousands "
        "of engagements. The Valkyrie's pilot uses standard instruments and standard "
        "flight controls -- no neural interface, no prosthetic sockets, no stimulant-"
        "enhanced reaction times. The pilot is good because SCN training is thorough, "
        "not because the pilot has been modified. The Valkyrie is not the most agile "
        "interceptor (Polaris) or the most survivable (Hyades), but it is competent, "
        "well-built, and mass-produced."
    ),
    exterior_appearance_description=(
        "A 10-meter single-seat military spacecraft with a light grey hull. A needle-thin "
        "fuselage with swept-back fins and a narrow glazed canopy. A small laser in the nose "
        "and a turret housing on top behind the canopy. Engine cluster at the rear. Navy blue "
        "pinstriping along the spine and fin edges. Silver identification numbers on the fins. "
        "White running lights at the wingtips."
    ),
    interior_appearance_description=(
        "A single-seat cockpit with standard flight controls, standard instruments, "
        "ejection system, and proper atmospheric controls. The pilot wears a standard "
        "flight suit with a standard helmet. Everything is designed for a baseline human "
        "to fly at the limits of human capability."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Ejection system", "Standard instrumentation"],
)

GRIFFIN = ShipTemplate(
    name="Griffin",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.SMALL,
    ship_archetype="Fighter",
    combat_role="Escort / area control / anti-small-craft",
    length=18,
    armor=8,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=15,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.PLASMA_LAUNCHER],
    default_small_craft=[],
    short_description="Standard general-purpose fighter with slightly above-average survivability",
    long_description=(
        "The Griffin is the SCN's general-purpose fighter -- the most-produced combat "
        "craft in known space. Tens of thousands serve across hundreds of systems. The "
        "Griffin is the fighter that every other faction's fighter is implicitly compared "
        "to, because the Griffin is the template. It is slightly better armored and "
        "hulled than the generic baseline -- not dramatically, but enough that across "
        "thousands of engagements, the statistical survival advantage is meaningful. "
        "Griffin pilots are trained through the most comprehensive pilot training "
        "programme in known space: standardized, thorough, and producing consistent "
        "quality. A Griffin pilot from any SCN squadron can slot into any other "
        "squadron and perform to standard within hours. This interchangeability is "
        "the MERIT advantage -- not individual excellence but systemic competence at "
        "scale."
    ),
    exterior_appearance_description=(
        "An 18-meter single-seat military spacecraft with a light grey hull. An angular wedge "
        "shape with a flat top, angled lower surfaces, and a glazed canopy. A plasma launcher "
        "housing set into the lower front. Two canted stabiliser fins. Engine bells mounted at "
        "the rear. Navy blue trim along the hull edges and engine housing. Silver MERIT seal "
        "on the upper fuselage. White running lights at the wingtips."
    ),
    interior_appearance_description=(
        "A single-seat cockpit with standard controls, standard instruments, proper "
        "lighting, ejection system, and atmospheric controls. Identical across all "
        "production runs. A Griffin cockpit on one side of MERIT space is identical "
        "to a Griffin cockpit on the other. This is intentional."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Ejection system", "Standard instrumentation"],
)

CENTAUR = ShipTemplate(
    name="Centaur",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=24,
    armor=12,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=25,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.PLASMA_LAUNCHER, weapons.PLASMA_LAUNCHER, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Standard heavy gunship with full crew complement",
    long_description=(
        "The Centaur is the SCN's heavy strike craft -- the largest small craft in the "
        "fleet, crewed by six baseline humans in a pressurized cabin with standard "
        "instruments and standard atmospheric controls. The Centaur's advantage over "
        "other factions' gunships is not dramatic -- it is the same marginal improvement "
        "in armor and hull that characterises all MERIT construction. But the Centaur "
        "also benefits from the SCN's logistics depth: a Centaur squadron is resupplied "
        "faster, rearmed more reliably, and maintained to higher standards than any "
        "other faction's equivalent because the supply chain behind it is deeper. A "
        "Centaur squadron that has been fighting for a week is in better material "
        "condition than other factions' equivalents because the spare parts arrived "
        "on time."
    ),
    exterior_appearance_description=(
        "A 24-meter multi-crew military spacecraft with a light grey hull. A broad, heavy "
        "hexagonal cross-section with a wide glazed canopy. Twin plasma launcher housings on "
        "the lower sides. A small point-defense turret on top. Engine bells in a row across "
        "the rear. Short angular fins. Navy blue trim along the hull edges and weapon "
        "housings. Silver identification numbers on the sides. White running lights at the "
        "wingtips."
    ),
    interior_appearance_description=(
        "Six stations in a pressurized, lit cabin -- pilot and gunner forward, engineer "
        "and sensor operator amidships, two damage control ratings aft. Standard "
        "instruments at every station. Standard atmospheric controls. Standard lighting. "
        "The cabin is comfortable and functional. Everything works."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}],
    secondary_crew=[{"engineer": 1}, {"sensor_operator": 1}, {"damage_control": 2}],
    additional_systems=["Ejection system (all crew)", "Standard instrumentation"],
)

SATYR = ShipTemplate(
    name="Satyr",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=68,
    armor=25,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=80,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Standard patrol corvette with extended supply duration",
    long_description=(
        "The Satyr is the most common warship in known space. More Satyrs patrol more "
        "systems than any other single ship class from any faction. The Satyr is the "
        "backbone of peacetime MERIT authority -- the ship that shows the flag, "
        "investigates contacts, enforces trade regulations, and responds to distress "
        "calls. It is a thoroughly professional, thoroughly unremarkable vessel that "
        "does everything slightly better than the template because MERIT's industrial "
        "base produces slightly better ships in every dimension. Its extended supply "
        "duration -- a week longer than the template -- reflects the SCN's logistical "
        "depth rather than any exotic crew modification. The crew eats normal food, "
        "breathes normal air, and serves normal watch rotations. They just have more "
        "supplies and they arrive on time."
    ),
    exterior_appearance_description=(
        "A 68-meter military spacecraft with a light grey hull. An elongated angular block "
        "with a raised bridge section toward the front with bridge windows. A particle cannon "
        "housing runs along the top spine. A heavy laser turret mounted behind the bridge. "
        "Engine bells in a pair at the rear flanked by manoeuvring thrusters. Navy blue trim "
        "along the hull edges and around the bridge section. Silver MERIT seal and fleet "
        "markings on the sides. White running lights along the hull."
    ),
    interior_appearance_description=(
        "Standard corridors with standard lighting and standard atmospheric controls. "
        "The bridge is a professional arrangement of stations. Crew quarters are "
        "small but comfortable -- bunks, personal storage, a shared head. The wardroom "
        "serves standard food. The ship is clean, orderly, and maintained to regulation. "
        "It looks like a military vessel because it is one."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 16}],
    secondary_crew=[{"gunners": 4}],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

NEREID = ShipTemplate(
    name="Nereid",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=65,
    armor=18,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=55,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Griffin", 5)],
    short_description="Standard tender corvette carrying five Griffin fighters",
    long_description=(
        "The Nereid carries a detachment of five SCN small craft -- typically Griffin "
        "fighters -- extending their operational range. The Nereid's hangar is standard: "
        "pressurized, lit, heated, with conventional launch cradles and a maintenance "
        "bay staffed by trained technicians using standard tools. The hangar crew does "
        "not have prosthetic hands or modified eyes. They have proper training, proper "
        "tools, and proper procedures. Turnaround times are competitive with other "
        "factions' tenders because the SCN's maintenance doctrine is thorough and "
        "standardized -- every technician follows the same procedures regardless of "
        "which Nereid they serve on."
    ),
    exterior_appearance_description=(
        "A 65-meter military spacecraft with a light grey hull. A wide, flat-bodied shape with "
        "launch cradles for five fighters visible along both sides, hangar lighting visible "
        "from outside. A light ion turret on top. Engine bells in a pair at the rear. Navy "
        "blue trim along the hull edges and around the launch bay doors. Silver identification "
        "numbers on the sides and top. White running lights along the hull and at the launch "
        "bays."
    ),
    interior_appearance_description=(
        "The hangar section is a well-lit, pressurized bay with five launch cradles and "
        "a maintenance area. The crew section forward is standard corvette "
        "accommodation -- small but functional. Standard lighting, standard air, standard "
        "food. The ship is comfortable in a military way."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 10}],
    secondary_crew=[
        {"embarked_craft_pilots": 5},
        {"hangar_technicians": 4},
    ],
    additional_systems=[
        "Hangar bay (5 small craft)",
        "Craft maintenance facilities",
        "Standard life support",
    ],
)

SPHINX = ShipTemplate(
    name="Sphinx",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Survey Corvette",
    combat_role="Hazardous environment operations / exploration",
    length=60,
    armor=25,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=55,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Standard survey corvette with extended supply for hazardous operations",
    long_description=(
        "The Sphinx conducts survey operations in hazardous environments -- radiation "
        "zones, nebulae, unstable systems. Unlike the Pleiadian Kadath, whose modified "
        "crew tolerates the environment directly, the Sphinx protects its baseline crew "
        "through engineering: radiation shielding, environmental hardening, sensor "
        "equipment designed to operate through interference. This makes the Sphinx "
        "heavier and less capable in extreme environments than the Kadath, but it means "
        "the crew comes home without biological modification. The Sphinx carries extended "
        "supplies for long survey deployments, reflecting MERIT's logistical depth. A "
        "Sphinx survey team has more consumables, more spare parts, and more "
        "contingency stores than any other faction's equivalent."
    ),
    exterior_appearance_description=(
        "A 60-meter military spacecraft with a light grey hull. A compact, rounded body with "
        "sensor blisters clustered around the front section. Thicker hull sections visible "
        "around the sensor housings. A light ion turret on top toward the rear. Engine bells "
        "in a pair at the rear. Navy blue trim along the hull edges and around the sensor "
        "blisters. Silver identification numbers on the sides. White running lights along the "
        "hull."
    ),
    interior_appearance_description=(
        "The sensor section is a cluster of stations with standard displays. The survey "
        "lab processes samples and environmental data. The crew quarters are standard "
        "corvette accommodation. Radiation monitoring equipment is visible throughout -- "
        "the ship tracks exposure carefully because the crew is baseline human and "
        "exposure matters."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[{"survey_specialists": 3}],
    additional_systems=[
        "Extended passive sensor array",
        "Hazardous environment survey suite",
        "Radiation shielding (enhanced)",
        "Environmental hardening",
        "Radiation monitoring system",
        "Standard life support",
    ],
)

GORGON = ShipTemplate(
    name="Gorgon",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Combat Frigate",
    combat_role="Fleet screening / torpedo attack",
    length=175,
    armor=45,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=160,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.RAILGUN, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Standard combat frigate with railgun, torpedo, and extended supply",
    long_description=(
        "The Gorgon is the SCN's fleet screening combatant -- a combat frigate that sits "
        "at the high end of the template in every dimension. Its railgun hits slightly "
        "harder. Its armor is slightly thicker. Its hull takes slightly more punishment. "
        "And its supply stores last a week longer. None of these advantages are dramatic. "
        "All of them add up. A Gorgon squadron screening a capital ship formation does "
        "its job slightly better than the template predicts because every component is "
        "slightly better than the template specifies. The SCN deploys more Gorgons than "
        "any other faction deploys combat frigates, and the logistics chain keeps them "
        "supplied, maintained, and at full combat readiness longer than any competitor."
    ),
    exterior_appearance_description=(
        "A 175-meter military spacecraft with a light grey hull. A broad, flat angular block "
        "-- wider than it is tall, with a blunt front and sheer slab sides. A railgun in a "
        "long housing along the top spine. A torpedo bay with visible loading doors in the "
        "lower front. A heavy laser turret in a recessed top mount behind the railgun. Engine "
        "bells in a cluster at the rear. Navy blue chevrons on the front and flanking the "
        "sides. Silver MERIT seal and fleet markings on both sides. Ship name in silver block "
        "lettering. Navy blue edge striping along both sides."
    ),
    interior_appearance_description=(
        "Standard frigate interior -- functional corridors, standard lighting, standard "
        "air. The bridge is a professional command space. The torpedo room is a "
        "pressurized compartment where baseline human ratings load torpedoes using "
        "standard equipment. The wardroom serves standard food. Crew quarters are "
        "small but comfortable. Everything is maintained to regulation."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 60}],
    secondary_crew=[
        {"gunners": 16},
        {"torpedo_crew": 8},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

WYVERN = ShipTemplate(
    name="Wyvern",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Patrol Frigate",
    combat_role="Commerce protection / independent operations",
    length=160,
    armor=25,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=100,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=42,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Standard patrol frigate with extended supply for independent operations",
    long_description=(
        "The Wyvern is the SCN's independent patrol vessel -- the ship sent to hold a "
        "system alone for weeks. It is the MERIT equivalent of the Pleiadian Bokrug, "
        "the Hyades Partisan, and the Polaran equivalent, and it outperforms none of "
        "them in their area of specialty. It does not have the Bokrug's environmental "
        "tolerance, the Partisan's repairability, or the Polaran ship's neural agility. "
        "But it has standard, competent capability in every dimension and the deepest "
        "supply chain backing it. A Wyvern captain knows that resupply is coming on "
        "schedule, that the replacement parts in the Wyvern's stores are standardized "
        "across the entire SCN, and that any SCN supply runner can resupply any Wyvern "
        "without compatibility issues. This logistical certainty is MERIT's real "
        "advantage."
    ),
    exterior_appearance_description=(
        "A 160-meter military spacecraft with a light grey hull. A narrow, elongated angular "
        "block with a pointed front. A particle cannon housing along the top spine. A torpedo "
        "bay in the lower front. A heavy laser turret in a recessed top mount. Extended hull "
        "sections along the lower sides for supply storage. Engine bells in a cluster at the "
        "rear. Navy blue chevrons on the front. Silver MERIT seal and fleet markings on both "
        "sides. Navy blue edge striping along both sides."
    ),
    interior_appearance_description=(
        "Standard frigate accommodation for extended independent deployment. Crew "
        "quarters are small but properly furnished. The wardroom is a functional "
        "social space. The bridge is professional and conventional. Standard lighting, "
        "standard air, standard food. The ship is comfortable enough for weeks of "
        "solo patrol."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 42}],
    secondary_crew=[
        {"gunners": 10},
        {"torpedo_crew": 4},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

ARGUS = ShipTemplate(
    name="Argus",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=180,
    armor=15,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=80,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=49,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Hard-jump scout frigate with comprehensive intelligence suite",
    long_description=(
        "The Argus is the SCN's deep reconnaissance platform -- a hard-jump-capable "
        "frigate that enters enemy systems and gathers intelligence. The Argus does "
        "not have the Pleiadian Commoriom's near-invisible sensor profile or the "
        "Polaran equivalent's neural-enhanced sensor processing. It compensates with "
        "the most comprehensive conventional intelligence suite in any faction's fleet -- "
        "excellent sensors operated by well-trained baseline analysts using well-designed "
        "equipment. The Argus's analysts are intelligence professionals, not modified "
        "organisms or neural-linked sensors. They are very good at their jobs because "
        "they were selected and trained by the most rigorous intelligence service in "
        "known space. Extended supply duration allows long-duration intelligence "
        "operations."
    ),
    exterior_appearance_description=(
        "A 180-meter military spacecraft with a light grey hull. A narrow angular fuselage "
        "with a large sensor array at the front -- a cluster of antenna housings and receiver "
        "dishes wider than the main hull, making the profile front-heavy. An ion cannon "
        "mounted on top. Engine bells in a cluster at the rear. Navy blue trim along the hull "
        "edges and around the sensor array housing. Silver identification numbers on the "
        "sides. White running lights along the hull."
    ),
    interior_appearance_description=(
        "The intelligence section forward is a well-equipped analysis centre -- standard "
        "displays, standard lighting, comfortable working conditions for analysts on "
        "long deployments. The hard-jump drive occupies the aft section. Crew quarters "
        "are standard. The ship is designed for extended deployments and the crew spaces "
        "reflect this -- slightly more comfortable than the Gorgon's."
    ),
    minimum_crew=[{"officers": 6}, {"crew": 28}],
    secondary_crew=[
        {"intelligence_analysts": 8},
        {"sensor_specialists": 4},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array",
        "Intelligence analysis suite",
        "Emission reduction design",
        "Standard life support",
    ],
)

CERBERUS = ShipTemplate(
    name="Cerberus",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=155,
    armor=25,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=100,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.PLASMA_CANNON, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Standard escort frigate with extended supply for convoy operations",
    long_description=(
        "The Cerberus provides defensive screening for MERIT convoys and transport "
        "groups. It is the most numerous escort frigate in known space -- MERIT's "
        "commercial shipping volume is the largest in the galaxy, and every convoy "
        "needs escorts. The Cerberus is slightly better in every dimension than the "
        "template, and more importantly, there are always enough of them. A MERIT "
        "convoy has escorts. A MERIT convoy has enough escorts. This is not true for "
        "every faction. The SCN's ability to assign Cerberus escorts to routine "
        "commercial convoys -- not just military operations -- is a function of "
        "industrial scale that no other faction can match."
    ),
    exterior_appearance_description=(
        "A 155-meter military spacecraft with a light grey hull. A short, blocky angular body "
        "with a blunt front. A plasma cannon housing on the top spine. An ion turret in a "
        "recessed mount behind it. Thicker hull plating along the sides visible as a step in "
        "the hull profile. Engine bells in a cluster at the rear. Navy blue trim along the "
        "hull edges and weapon housings. Silver MERIT seal and fleet markings on the sides. "
        "Navy blue edge striping along both sides."
    ),
    interior_appearance_description=(
        "Standard frigate interior. The bridge is professional and conventional. "
        "Gunnery stations have standard targeting displays. Crew quarters are small "
        "but adequate. Standard food, standard air, standard lighting."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 36}],
    secondary_crew=[{"gunners": 12}],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

HYDRA = ShipTemplate(
    name="Hydra",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=250,
    armor=60,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=300,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Standard fleet destroyer with triple point defense and extended supply",
    long_description=(
        "The Hydra is the shield of the SCN battle fleet. Triple point defense turrets "
        "create a defensive umbrella over capital ships, and the Hydra's slightly above-"
        "template armor and hull let it absorb incoming fire while maintaining its "
        "coverage. The Hydra does not repair itself as fast as a Hyades Rampart or "
        "coordinate its fire through neural links like a Polaris equivalent. It "
        "maintains its defensive coverage through disciplined, well-trained baseline "
        "crews executing standard doctrine. The point defense crews rotate on standard "
        "watch schedules and maintain effectiveness through training and rest rather "
        "than stimulants or modification. The Hydra's extended supply duration means it "
        "can maintain its station longer than the template predicts -- the fleet's "
        "defensive umbrella doesn't collapse because the destroyers ran out of supplies."
    ),
    exterior_appearance_description=(
        "A 250-meter military spacecraft with a light grey hull. A broad, angular slab shape "
        "with a squared-off front. A railgun housing along the top spine. Four heavy laser "
        "turrets in recessed positions -- two on top, two on the bottom. Engine bells in two "
        "rows of three at the rear. Navy blue chevrons on the front and sides. Silver MERIT "
        "seal and fleet markings at large scale on both sides. Ship name in silver block "
        "lettering. Navy blue edge striping along the hull."
    ),
    interior_appearance_description=(
        "Three point defense battery stations distributed port, starboard, and dorsal. "
        "Standard targeting displays. Standard crew rotation schedules. The bridge is a "
        "professional command space. Crew quarters are standard destroyer accommodation. "
        "The ship is well-maintained and orderly."
    ),
    minimum_crew=[{"officers": 18}, {"crew": 115}],
    secondary_crew=[
        {"gunners": 35},
        {"point_defense_crew": 30},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

FENRIR = ShipTemplate(
    name="Fenrir",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=240,
    armor=45,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=250,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=42,
    default_weapons=[weapons.PARTICLE_LANCE, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Fast pursuit destroyer with extended endurance for long-duration hunts",
    long_description=(
        "The Fenrir is the SCN's pursuit ship -- faster than the template, with the "
        "extended supply duration that MERIT logistics provides. The Fenrir hunts "
        "pirates, smugglers, and hostile raiders through MERIT space, and its advantage "
        "is not exotic technology but the depth of the network behind it. A Fenrir "
        "pursuing a contact through medium jump points can request resupply from any "
        "SCN supply runner in any system along the pursuit route. The contact being "
        "pursued cannot. A Fenrir hunting in pairs can coordinate through standard "
        "communications using standard doctrine that every SCN officer has trained on. "
        "The pursuit doesn't rely on the Pleiadian crew's inhuman endurance or the "
        "Hyades crew's mechanical self-repair. It relies on the SCN's ability to keep "
        "the hunter supplied and the target unable to rest."
    ),
    exterior_appearance_description=(
        "A 240-meter military spacecraft with a light grey hull. A lean, elongated angular "
        "shape with a narrow front. A particle lance housing extends forward from the front in "
        "a long barrel. A torpedo bay in the lower front. An ion turret and point-defense "
        "mount on top. Oversized engine bells in two rows at the rear. Navy blue trim along "
        "the hull edges and lance housing. Silver identification numbers on the sides. White "
        "running lights along the hull."
    ),
    interior_appearance_description=(
        "Designed for sustained pursuit. Crew quarters are slightly more comfortable "
        "than the Hydra's -- the Fenrir deploys independently for longer. The torpedo "
        "room forward is standard. The bridge is a pursuit-oriented command space. "
        "Standard food, standard air, standard rest cycles."
    ),
    minimum_crew=[{"officers": 16}, {"crew": 90}],
    secondary_crew=[
        {"gunners": 22},
        {"torpedo_crew": 6},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

LAMIA = ShipTemplate(
    name="Lamia",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Infiltrator Destroyer",
    combat_role="Deep operations behind enemy lines",
    length=210,
    armor=35,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=160,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=42,
    default_weapons=[weapons.PARTICLE_LANCE],
    default_small_craft=[],
    short_description="Hard-jump infiltrator for deep operations behind enemy lines",
    long_description=(
        "The Lamia is the SCN's deep infiltration platform -- a hard-jump-capable "
        "destroyer that operates behind enemy lines for extended periods. MERIT is the "
        "only faction besides Polaris that fields a dedicated infiltrator destroyer, "
        "because MERIT is the only other faction with the intelligence infrastructure "
        "to support deep operations. The Lamia's crew are baseline humans -- they cannot "
        "rely on Polaran neural coordination or exotic technology. They rely on training, "
        "tradecraft, and the SCN intelligence service's deep network of assets, dead "
        "drops, and pre-positioned supply caches throughout the outer systems. A Lamia "
        "operating behind Canopan lines knows that MERIT intelligence placed supply "
        "caches in that sector years ago. The deep operation is supported by the deepest "
        "intelligence network in known space."
    ),
    exterior_appearance_description=(
        "A 210-meter military spacecraft with a light grey hull. A smooth, flat angular shape "
        "with minimal external features. Recessed fittings and angled hull surfaces. A "
        "particle lance housing extends from the front. No other visible weapons. Engine bells "
        "with baffled exhausts at the rear. Minimal markings -- navy blue trim limited to thin "
        "lines along the hull edges. Silver identification numbers in small font. Fewer "
        "running lights than standard."
    ),
    interior_appearance_description=(
        "The intelligence operations centre is a sealed compartment with analysis "
        "stations. The hard-jump drive occupies the aft section. Crew quarters are "
        "designed for extended independent operations -- slightly more comfortable "
        "than a standard destroyer. The ship carries contingency supplies and "
        "equipment for intelligence operations."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 55}],
    secondary_crew=[
        {"gunners": 12},
        {"intelligence_specialists": 8},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Intelligence operations centre",
        "Low-emission hull design",
        "Standard life support",
    ],
)

MEDUSA = ShipTemplate(
    name="Medusa",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="EW Destroyer",
    combat_role="Electronic warfare / jamming / information denial",
    length=230,
    armor=40,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=200,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Standard EW destroyer with comprehensive jamming and analysis suite",
    long_description=(
        "The Medusa is the SCN's electronic warfare platform -- denying the enemy "
        "information, disrupting their sensors, and degrading their communications. "
        "MERIT's EW doctrine is conventional: broadband jamming, targeted disruption, "
        "and sensor spoofing using standard technology operated by well-trained EW "
        "specialists. The Medusa does not have the Pleiadian Nyarlathotep's exotic "
        "perceptual advantages. It has the best conventional EW equipment available, "
        "operated by specialists trained through the SCN's standardized EW programme. "
        "The Medusa's advantage is the same as all MERIT ships: marginal quality "
        "advantage across the board, backed by numbers and logistics."
    ),
    exterior_appearance_description=(
        "A 230-meter military spacecraft with a light grey hull. An angular body with "
        "electronic warfare arrays clustered along the top and sides -- flat panels, antenna "
        "clusters, and emitter housings giving the hull a distinctive ridged profile. An ion "
        "cannon on the top spine. Engine bells in a cluster at the rear. Navy blue trim along "
        "the hull edges and at the base of each EW array. Silver identification numbers on the "
        "sides. White running lights along the hull."
    ),
    interior_appearance_description=(
        "The electronic warfare centre is a dedicated compartment with analysis and "
        "jamming control stations. Standard displays, standard lighting, standard "
        "equipment. The EW operators work in comfortable conditions using standard "
        "instruments. The rest of the ship is standard destroyer interior."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 50}],
    secondary_crew=[{"ew_operators": 14}],
    additional_systems=[
        "Electronic warfare centre",
        "Jamming array (broadband)",
        "Sensor spoofing system",
        "Emissions analysis suite",
        "Standard life support",
    ],
)

CYCLOPS = ShipTemplate(
    name="Cyclops",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Siege Destroyer",
    combat_role="Anti-capital firepower on a destroyer hull",
    length=230,
    armor=25,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=150,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.SIEGE_CANNON, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Standard siege cannon platform with slightly above-template construction",
    long_description=(
        "The Cyclops mounts a siege cannon on a destroyer hull. The SCN fields more "
        "siege destroyers than any other faction because its industrial base can afford "
        "to build dedicated weapons platforms in numbers that other factions cannot "
        "match. A Cyclops is not individually superior to other factions' siege "
        "destroyers -- the Hyades Bombard has more armor around the weapon, the Pleiadian "
        "Mordiggian is faster. But the SCN can deploy more Cyclops in a siege formation "
        "than any other faction can deploy equivalent ships, and the concentrated fire "
        "of multiple siege cannons is what breaks defensive positions."
    ),
    exterior_appearance_description=(
        "A 230-meter military spacecraft with a light grey hull. A squat, reinforced angular "
        "frame dominated by a single massive siege cannon housing running the full length of "
        "the top -- a weapon as long as the ship. A point-defense mount near the rear on top. "
        "Engine bells in a cluster at the rear. The cannon housing is the dominant visual "
        "feature. Navy blue trim along the hull edges and cannon housing. Silver "
        "identification numbers on the sides. White running lights along the hull."
    ),
    interior_appearance_description=(
        "The ship is built around the cannon. Standard crew spaces packed into the "
        "remaining volume. The gun crew works in a standard, pressurized, lit loading "
        "section. Standard food, standard air. The bridge is a cramped forward "
        "compartment. The ship exists to fire its cannon."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 52}],
    secondary_crew=[{"gunnery_specialists": 12}],
    additional_systems=[
        "Spinal siege cannon mount",
        "Standard life support",
    ],
)

TYPHON = ShipTemplate(
    name="Typhon",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=430,
    armor=80,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=500,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[
        weapons.PRECISION_RAILGUN,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Standard line cruiser -- the backbone of the SCN battle fleet",
    long_description=(
        "The Typhon is the SCN's main line combatant and the most numerous heavy "
        "cruiser in known space. The Typhon is not the most heavily armored cruiser "
        "(Hyades Onager), not the fastest (Pleiadian Dagon), not the most agile "
        "(Polaris equivalent), not the hardest to kill (Canopan Megalania). It is "
        "slightly above average in every dimension and backed by more logistics, more "
        "supply, more reserve ships, and more industrial capacity than any other "
        "faction can bring to bear. A Typhon battle group fights the way MERIT fights "
        "everything: competently, persistently, and with more resources than the enemy "
        "expected. Typhon captains are products of the most standardized officer "
        "training programme in known space. They are consistently good. Consistently "
        "reliable. Consistently adequate to the demands of the engagement. MERIT does "
        "not produce heroes. It produces professionals."
    ),
    exterior_appearance_description=(
        "A 430-meter military spacecraft with a light grey hull. A massive angular slab with a "
        "blunt front and thick, flat sides. A precision railgun housing along the top spine. "
        "Weapon batteries in housings along both sides. Point-defense turrets spaced at "
        "regular intervals along the sides. Engine bells in two rows of four across the rear. "
        "Navy blue chevrons on the front and sides. Silver fleet emblems -- MERIT seal and "
        "designation bars -- at large scale on both sides. Ship name in silver block "
        "lettering. Navy blue edge striping along the hull."
    ),
    interior_appearance_description=(
        "Standard cruiser interior -- proper corridors, proper lighting, proper air. The "
        "bridge is a professional command amphitheatre. Gunnery stations are manned by "
        "trained baseline crews using standard targeting equipment. Crew quarters are "
        "standard military accommodation. The wardroom serves standard food. Medical "
        "facilities are competent. The ship is orderly, well-maintained, and "
        "unremarkable."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 45}, {"crew": 360}],
    secondary_crew=[
        {"gunners": 70},
        {"point_defense_crew": 28},
        {"medical": 12},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

BASILISK = ShipTemplate(
    name="Basilisk",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=400,
    armor=60,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=350,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Standard medium-jump cruiser for flanking and independent operations",
    long_description=(
        "The Basilisk is the largest SCN combatant that can use medium jump points -- "
        "the backbone of flanking forces and independent task groups. The Basilisk's "
        "advantage in flanking operations is logistical: a MERIT flanking force can be "
        "resupplied through the medium jump network because the SCN has supply "
        "infrastructure at every jump point. A flanking force from another faction "
        "operates on what it carries. A MERIT flanking force operates on what the "
        "supply chain delivers, which is always more."
    ),
    exterior_appearance_description=(
        "A 400-meter military spacecraft with a light grey hull. A lean, elongated angular "
        "body -- narrower and longer in proportion than typical for this size. A heavy railgun "
        "housing along the top spine. Two laser turrets in recessed top mounts. A "
        "point-defense mount on the rear upper hull. Engine bells in two rows of three at the "
        "rear. Navy blue trim along the hull edges and railgun housing. Silver MERIT seal and "
        "fleet markings on the sides. Navy blue edge striping along the hull."
    ),
    interior_appearance_description=(
        "Standard cruiser interior with a task force coordination section for managing "
        "flanking group operations. Crew quarters are standard. The ship is comfortable "
        "for extended independent operations. Standard food, standard air."
    ),
    minimum_crew=[{"senior_officers": 6}, {"officers": 35}, {"crew": 280}],
    secondary_crew=[
        {"gunners": 45},
        {"point_defense_crew": 18},
        {"task_force_staff": 10},
    ],
    additional_systems=[
        "Task force coordination suite",
        "Standard life support",
    ],
)

MUSE = ShipTemplate(
    name="Muse",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Command Cruiser",
    combat_role="Fleet coordination / flagship / C2 platform",
    length=410,
    armor=50,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=350,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.PARTICLE_LANCE, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Dedicated fleet coordination platform with comprehensive C2 systems",
    long_description=(
        "The Muse is the SCN's dedicated command cruiser -- a fleet coordination platform "
        "that centralises tactical command, strategic communications, and intelligence "
        "processing. MERIT is the only faction that fields a dedicated command cruiser "
        "because MERIT is the only faction whose doctrine explicitly centralises command "
        "authority on a purpose-built platform. Other factions distribute command across "
        "line ships or rely on enhanced cognition (Pleiades) or neural coordination "
        "(Polaris). MERIT centralises command because its doctrine is built around "
        "standardised, hierarchical coordination -- and a dedicated platform does that "
        "better than a line ship's bridge. The Muse carries comprehensive communications "
        "equipment, tactical displays, a fleet-scale sensor fusion system, and "
        "accommodation for the flag officer and their staff. When an SCN battle group "
        "fights, the Muse is where the decisions are made."
    ),
    exterior_appearance_description=(
        "A 410-meter military spacecraft with a light grey hull. An angular body with a "
        "raised, enlarged bridge superstructure toward the front -- visibly oversized, housing "
        "the fleet coordination centre. Communications antenna clusters at the top of the "
        "bridge superstructure. A particle lance housing extends from the front. A heavy laser "
        "turret on top behind the bridge. Engine bells in two rows of three at the rear. Navy "
        "blue chevrons on the front and around the bridge superstructure. Silver fleet emblems "
        "and ship name prominently displayed on the sides. White running lights along the hull "
        "and on the bridge superstructure."
    ),
    interior_appearance_description=(
        "The combat information centre is the heart of the ship -- a large, well-lit "
        "space with tactical displays, communications stations, and intelligence fusion "
        "equipment. The flag officer's quarters and staff compartments are larger than "
        "standard. The bridge is a command amphitheatre designed for fleet coordination "
        "rather than ship-to-ship combat. Standard lighting, standard air, comfortable "
        "working conditions. The Muse is built for the people making decisions under "
        "pressure to do so in the best conditions possible."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 30}, {"crew": 220}],
    secondary_crew=[
        {"gunners": 20},
        {"flag_staff": 25},
        {"communications_specialists": 15},
        {"intelligence_analysts": 10},
        {"sensor_fusion_operators": 8},
    ],
    additional_systems=[
        "Combat information centre (fleet-scale)",
        "Fleet tactical display",
        "Sensor fusion system",
        "Strategic communications array",
        "Flag officer's quarters and staff compartments",
        "Standard life support",
    ],
)

ECHIDNA = ShipTemplate(
    name="Echidna",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Carrier",
    combat_role="Cruiser combatant with embarked small craft",
    length=380,
    armor=55,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=350,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=49,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.PLASMA_PD],
    default_small_craft=[("Griffin", 10)],
    short_description="Standard light carrier with ten embarked Griffin fighters",
    long_description=(
        "The Echidna is a cruiser hull carrying a wing of ten Griffin fighters -- "
        "combining line combat capability with the force projection of an embarked "
        "strike wing. The Echidna's hangar is standard: pressurized, lit, heated, with "
        "conventional launch equipment and a trained deck crew using standard tools and "
        "standard procedures. The Echidna sustains its wing through the SCN's logistics "
        "network -- spare parts, replacement craft, and consumables arrive through the "
        "supply chain. A light carrier that loses three fighters can expect replacements "
        "from the nearest fleet depot. Other factions' light carriers operate on what "
        "they brought."
    ),
    exterior_appearance_description=(
        "A 380-meter military spacecraft with a light grey hull. A wide, flat angular body "
        "with a flight deck dominating the midsection. Launch bays visible along both sides, "
        "hangar lighting visible from outside. A railgun housing along the top spine forward "
        "of the flight deck. Two heavy laser turrets in recessed top mounts. A point-defense "
        "mount at the rear. Engine bells in two rows of three at the rear. Navy blue trim "
        "along the hull edges and around the launch bay doors. Silver identification numbers "
        "on the sides and top. White running lights along the hull and at the launch bays."
    ),
    interior_appearance_description=(
        "The hangar is a well-lit, pressurized bay with ten launch cradles. Standard "
        "maintenance equipment. The flight operations centre manages the wing through "
        "conventional displays. The pilot ready room is a comfortable compartment. The "
        "rest of the ship is standard cruiser interior."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 20}, {"crew": 150}],
    secondary_crew=[
        {"ship_gunners": 18},
        {"embarked_craft_pilots": 10},
        {"wing_coordinators": 2},
        {"hangar_crew": 14},
    ],
    additional_systems=[
        "Hangar bay (10 small craft)",
        "Craft maintenance facilities",
        "Flight operations centre",
        "Standard life support",
    ],
)

LEVIATHAN = ShipTemplate(
    name="Leviathan",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=950,
    armor=95,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1800,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=84,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Standard battleship -- the capital backbone of the SCN",
    long_description=(
        "The Leviathan is the SCN's battleship and the most produced capital ship in "
        "known space. More Leviathans exist than any other faction's battleship "
        "equivalent. The Leviathan is not the most heavily armored battleship (Hyades "
        "Fortress), not the fastest (Pleiadian Hastur), not the most agile (Polaris "
        "equivalent), not the hardest to kill permanently (Canopan equivalent). It is "
        "slightly above average in every dimension. And there are more of them. MERIT's "
        "capital ship doctrine is built on the assumption that the Leviathan will never "
        "fight alone -- it will fight as part of a battle group with destroyer escorts, "
        "logistics support, and reserve forces that no other faction can match. A "
        "Leviathan is a competent battleship. A Leviathan battle group is the most "
        "formidable military formation in known space because the supporting "
        "infrastructure is unmatched."
    ),
    exterior_appearance_description=(
        "A 950-meter military spacecraft with a light grey hull. A massive angular slab with a "
        "blunt front and thick, sheer sides. A gauss cannon housing along the top spine. "
        "Weapon batteries in armoured housings along both sides in two tiers. Point-defense "
        "turrets at regular intervals along the sides and top. Engine bells in a grid of "
        "twelve across the stepped rear face. Navy blue chevrons on the front and sides. "
        "Silver fleet emblems -- MERIT seal and designation bars -- at large scale on both "
        "sides. Ship name in silver block lettering. Rows of white running lights along the "
        "hull edges."
    ),
    interior_appearance_description=(
        "Kilometres of standard military corridors with proper lighting, proper air, and "
        "proper gravity. The bridge is a large command amphitheatre. Gunnery stations are "
        "manned by trained baseline crews. Crew quarters are standard capital ship "
        "accommodation -- small but functional. Medical facilities are comprehensive. "
        "Recreation spaces exist and are used. The mess serves standard food to thousands "
        "of crew. The ship functions as a military community -- orderly, professional, "
        "and unremarkable."
    ),
    minimum_crew=[{"senior_officers": 22}, {"officers": 140}, {"crew": 1700}],
    secondary_crew=[
        {"gunners": 220},
        {"point_defense_crew": 110},
        {"medical": 30},
    ],
    additional_systems=["Standard instrumentation", "Standard life support"],
)

GAIA = ShipTemplate(
    name="Gaia",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1250,
    armor=60,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1400,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=84,
    default_weapons=[
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_PD,
        weapons.LASER_PD,
        weapons.LASER_PD,
    ],
    default_small_craft=[
        ("Harpy", 10),
        ("Harpy", 10),
        ("Griffin", 10),
        ("Centaur", 10),
    ],
    short_description="Standard fleet carrier deploying four wings of strike craft",
    long_description=(
        "The Gaia is the SCN fleet carrier -- deploying four wings of strike craft in "
        "the standard composition: two wings of Harpy bombers, one wing of Griffin "
        "fighters, and one wing of Centaur gunships. The Gaia's advantage is the same "
        "as all MERIT capital assets: the logistics behind it. A Gaia that loses half "
        "its air wing in an engagement receives replacement craft from the nearest fleet "
        "depot. Other factions' carriers operate on what they launched with. The SCN's "
        "ability to replace strike craft losses in the field is a strategic advantage "
        "that no other faction can match. The Gaia's deck crews are trained through "
        "standardised programmes and execute standardised procedures. Turnaround times "
        "are competitive with other factions' carriers because the procedures are "
        "optimized and consistently executed, not because the crew is modified or "
        "enhanced."
    ),
    exterior_appearance_description=(
        "A 1250-meter military spacecraft with a light grey hull. A long, flat-topped "
        "rectangular block with a blunt front and sheer, slab-sided walls. The top surface is "
        "a broad flat flight deck. Tiered hangar openings are cut into the sides, interior "
        "lighting visible within. Engine bells in clusters along the lower rear and underside. "
        "Navy blue chevrons on the front and flanking the hangar openings. Silver fleet "
        "emblems -- the MERIT seal flanked by designation bars -- displayed at large scale on "
        "both sides. Ship name in silver block lettering beneath each emblem. Navy blue edge "
        "striping runs the full length of both sides."
    ),
    interior_appearance_description=(
        "Four hangar bays -- vast, well-lit, pressurized spaces where forty strike craft "
        "sit in standard launch cradles. The deck crews work in standard conditions with "
        "standard tools. The flight operations centre is a large, well-equipped command "
        "space. Pilot ready rooms are comfortable. The ship carries thousands of crew in "
        "standard accommodation. Medical facilities, recreation spaces, and the other "
        "amenities of a capital ship community. Standard food, standard air, standard "
        "everything."
    ),
    minimum_crew=[{"senior_officers": 35}, {"officers": 220}, {"crew": 3400}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"wing_coordinators": 6},
        {"flight_deck_crew": 200},
        {"hangar_maintenance": 120},
        {"ship_gunners": 45},
        {"medical": 45},
    ],
    additional_systems=[
        "Hangar bays (x4, 10 craft each)",
        "Craft maintenance facilities",
        "Flight operations centre",
        "Standard life support",
    ],
)

TITAN = ShipTemplate(
    name="Titan",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=1900,
    armor=100,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=3000,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=98,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Standard dreadnought -- the ultimate expression of SCN capital power",
    long_description=(
        "The Titan is the SCN dreadnought -- the most powerful conventional warship "
        "produced by MERIT and the strategic deterrent that anchors their military "
        "position. The Titan is not the hardest dreadnought to kill (Hyades Acropolis), "
        "not the most effective in hostile environments (Pleiadian Azathoth), not the "
        "most capable of replacing crew losses (Canopan Mammoth). It is the dreadnought "
        "with the deepest supply chain, the most professional crew, and the most "
        "reliable logistics. A Titan on station for months receives regular resupply, "
        "regular crew rotation, and regular maintenance from a support infrastructure "
        "that no other faction can duplicate. The Titan's twin siege cannons fire "
        "slightly harder than the template -- not dramatically, but enough to matter "
        "over the course of a siege. MERIT fields more dreadnoughts than any other "
        "faction. This is the MERIT advantage: not the best ship, but the most ships, "
        "with the best support."
    ),
    exterior_appearance_description=(
        "A 1900-meter military spacecraft with a light grey hull. A massive elongated "
        "hexagonal prism, tapering slightly toward the front, with a flat top and angled lower "
        "facets. Twin siege cannon housings run the full length of the ship along the top, "
        "side by side. Engine bells in a rectangular grid across the rear face. Point-defense "
        "turrets in recessed mounts at regular intervals along the sides. Navy blue trim along "
        "the hull edges, siege cannon housings, and broad chevrons on the front and sides. "
        "Silver fleet markings and ship name at large scale on the top and both sides. Rows of "
        "white running lights along the hull edges. A fortress that moves."
    ),
    interior_appearance_description=(
        "The Titan's interior is a military city. Standard corridors, standard lighting, "
        "standard air, standard gravity. Thousands of crew serve in standard "
        "accommodation. The bridge is a vast command amphitheatre. The siege cannon "
        "sections are manned by trained gunnery crews using standard equipment. Medical "
        "facilities are comprehensive. Recreation spaces, worship spaces, exercise "
        "facilities, and the other amenities needed to sustain a community of thousands "
        "for months. The Titan is not exotic. It is the largest, most expensive, and "
        "most conventional warship in known space."
    ),
    minimum_crew=[{"senior_officers": 60}, {"officers": 400}, {"crew": 6200}],
    secondary_crew=[
        {"gunners": 320},
        {"point_defense_crew": 70},
        {"fleet_coordination_staff": 65},
        {"medical": 90},
        {"sensor_specialists": 40},
    ],
    additional_systems=[
        "Twin spinal siege cannon mounts",
        "Standard life support",
    ],
)

CORNUCOPIA = ShipTemplate(
    name="Cornucopia",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Fleet Tender",
    combat_role="Resupply / ammunition and fuel transport",
    length=330,
    armor=35,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=200,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=63,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Standard fleet tender -- the backbone of SCN logistics",
    long_description=(
        "The Cornucopia is the SCN's fleet tender -- the ship that keeps the fleet fed, "
        "armed, and fueled. More Cornucopias serve in the SCN than any other faction's "
        "equivalent. MERIT's logistical advantage is not exotic -- it is the systematic "
        "ability to keep supply ships where they're needed, loaded with what the fleet "
        "requires, arriving on schedule. A Cornucopia carries ammunition, fuel, food, "
        "spare parts, medical supplies, and the thousand other items a fleet consumes. "
        "The SCN's supply doctrine ensures that every item aboard is standardized across "
        "the entire fleet -- a replacement part from any Cornucopia fits any SCN ship. "
        "This interoperability is MERIT's hidden advantage. No compatibility issues. No "
        "custom parts. Everything works with everything else."
    ),
    exterior_appearance_description=(
        "A 330-meter military spacecraft with a light grey hull. A bulky, boxy shape -- a wide "
        "cargo and supply module with docking clamps and transfer booms along both sides. A "
        "compact bridge module at the front. An ion turret on top. A point-defense mount at "
        "the rear. Engine bells in a cluster at the rear. Navy blue trim along the hull edges "
        "and around the docking clamps. Silver identification numbers on the sides and top. "
        "White running lights along the hull and at the docking points."
    ),
    interior_appearance_description=(
        "The interior is mostly cargo space -- modular containers of ammunition, fuel "
        "cells, food, spare parts, medical supplies. The crew section forward is standard "
        "accommodation. The ship is functional and professional."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 70}],
    secondary_crew=[{"cargo_handlers": 35}, {"repair_technicians": 15}],
    additional_systems=[
        "Modular cargo system",
        "Standardized supply stores",
        "Field repair facilities (limited)",
        "Standard life support",
    ],
)

HERMES = ShipTemplate(
    name="Hermes",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Supply Runner",
    combat_role="Fast resupply through medium jump points",
    length=120,
    armor=20,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=80,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fast supply runner delivering standardized supplies through medium jumps",
    long_description=(
        "The Hermes delivers ammunition, fuel, and supplies to forward-deployed task "
        "forces through medium jump points. MERIT's supply runner fleet is the largest "
        "in known space -- the SCN can sustain forward operations through a continuous "
        "flow of Hermes runs that other factions cannot match. The Hermes carries "
        "standardized supplies that work with any SCN ship. This logistical "
        "interoperability means that a single Hermes can resupply a mixed task force "
        "without compatibility issues."
    ),
    exterior_appearance_description=(
        "A 120-meter military spacecraft with a light grey hull. A long, narrow rectangular "
        "body -- a slim crew module at the front and a long cargo midsection with loading "
        "hatches along the sides. An ion turret on top of the front section. Oversized engine "
        "bells at the rear for the hull size. Navy blue trim along the hull edges and around "
        "the loading hatches. Silver identification numbers on the sides and top. White "
        "running lights along the hull."
    ),
    interior_appearance_description=(
        "Engine, jump drive, and cargo. The crew section is minimal -- a standard bridge "
        "and standard quarters for a small crew. The cargo hold stores standardized "
        "containers."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 12}],
    secondary_crew=[{"cargo_handlers": 6}],
    additional_systems=[
        "Modular cargo system",
        "Standard life support",
    ],
)

DRYAD = ShipTemplate(
    name="Dryad",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Logistics Corvette",
    combat_role="Emergency resupply / hard-jump logistics",
    length=58,
    armor=12,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=45,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump logistics corvette resupplying deep operations",
    long_description=(
        "The Dryad is the smallest dedicated logistics vessel in the SCN -- a hard-jump-"
        "capable corvette that resupplies ships operating deep behind enemy lines. The "
        "Dryad carries limited supplies -- enough to sustain an Argus scout frigate or "
        "Lamia infiltrator destroyer on extended deep operations. The Dryad's existence "
        "is what makes MERIT's deep intelligence operations viable at scale. Without "
        "the Dryad, deep operations are limited to what the ships carry. With the Dryad, "
        "operations can last months. MERIT's intelligence service pre-positions Dryad "
        "supply runs through hard jump networks, ensuring that deep assets receive "
        "regular resupply."
    ),
    exterior_appearance_description=(
        "A 58-meter military spacecraft with a light grey hull. A compact, boxy rectangular "
        "body -- a small bridge section at the front, the majority of the hull given to cargo "
        "space with loading hatches on the sides and underside. A light ion turret on top. "
        "Engine bells in a pair at the rear. Navy blue trim along the hull edges and around "
        "the loading hatches. Silver identification numbers on the sides. White running lights "
        "along the hull."
    ),
    interior_appearance_description=(
        "The hard-jump drive and cargo hold consume most of the interior. Crew spaces "
        "are minimal -- a standard bridge and bunks for a skeleton crew. The cargo hold "
        "carries sealed containers of ammunition, food, and supplies."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 7}],
    secondary_crew=[{"cargo_handlers": 3}],
    additional_systems=[
        "Hard-jump drive",
        "Sealed cargo system",
        "Standard life support",
    ],
)

ASCLEPIUS = ShipTemplate(
    name="Asclepius",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Field Support Ship",
    combat_role="Medical / repair / fleet maintenance hub",
    length=480,
    armor=50,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=400,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=63,
    default_weapons=[weapons.ION_CANNON, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Fleet medical and repair hub with comprehensive facilities",
    long_description=(
        "The Asclepius is the SCN's field support ship -- carrying medical facilities, "
        "ship repair equipment, and the spare parts that keep a task force operational. "
        "Where the Hyades Smithy manufactures prosthetics, the Canopan Ammonite "
        "reanimates the dead, and the Pleiadian Pnakotus maintains biological "
        "modifications, the Asclepius provides conventional medical care and conventional "
        "ship repair. It treats wounded crew with standard medicine. It repairs damaged "
        "ships with standard parts. It is very good at both because the SCN's medical "
        "and engineering training programmes are comprehensive, and the supply chain "
        "keeps the Asclepius stocked with everything it needs. A task force with an "
        "Asclepius attached maintains combat effectiveness longer because wounded crew "
        "return to duty, damaged ships return to the line, and the logistics chain "
        "keeps the Asclepius supplied."
    ),
    exterior_appearance_description=(
        "A 480-meter military spacecraft with a light grey hull. A wide angular body with a "
        "prominent medical bay section amidships marked by large red cross symbols. Docking "
        "ports and transfer airlocks along both sides. An ion cannon on the top spine forward. "
        "Two point-defense mounts on the sides toward the rear. Engine bells in two rows of "
        "three at the rear. Navy blue trim along the hull edges. Silver identification numbers "
        "and fleet markings on the sides. Red cross medical markings on the sides and top "
        "amidships. White running lights along the hull."
    ),
    interior_appearance_description=(
        "The medical section is a well-equipped hospital -- operating theatres, recovery "
        "wards, triage, and the full spectrum of baseline medical capability. The repair "
        "section carries fabrication equipment and standardized spare parts for field-"
        "level ship repair. The crew is a mix of medical professionals and engineering "
        "specialists. Standard lighting, standard air, standard food. The ship is "
        "brightly lit and warm -- the opposite of a Pleiadian vessel."
    ),
    minimum_crew=[{"officers": 20}, {"crew": 130}],
    secondary_crew=[
        {"medical_officers": 15},
        {"medical_staff": 30},
        {"repair_technicians": 25},
        {"fabrication_specialists": 10},
    ],
    additional_systems=[
        "Medical facilities (hospital-grade)",
        "Operating theatres (x4)",
        "Ship repair bay",
        "Fabrication equipment (standardized parts)",
        "Ship-to-ship docking ports",
        "Standard life support",
    ],
)

TROJAN = ShipTemplate(
    name="Trojan",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=700,
    armor=85,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1200,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=63,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Standard assault transport deploying baseline marines with full equipment",
    long_description=(
        "The Trojan delivers a MERIT marine force into hostile territory. MERIT marines "
        "are baseline humans in standard armour with standard weapons -- no prosthetic "
        "augmentation, no biological modification, no stimulant enhancement. They are "
        "well-trained, well-equipped, and well-supplied professionals. The Trojan "
        "carries more marines than any other faction's assault transport because it "
        "carries full life support for baseline humans -- heated, lit, pressurized troop "
        "decks with standard accommodation. This makes the Trojan heavier than the "
        "Pleiadian R'lyeh (which doesn't heat or light its troop decks) but ensures "
        "the marine force arrives in condition to fight without environmental adaptation. "
        "MERIT marines operate on standard supplies from a standard logistics chain."
    ),
    exterior_appearance_description=(
        "A 700-meter military spacecraft with a light grey hull. A heavy, angular block with a "
        "blunt, armoured front. A particle cannon housing on top. The midsection is a massive "
        "troop and vehicle bay with large loading ramps on the underside and rear. "
        "Point-defense turrets spaced along the sides and top. Engine bells in two rows of "
        "four at the rear. Navy blue chevrons on the front. Silver MERIT seal and fleet "
        "markings on the sides and top. Ship name in silver block lettering. White running "
        "lights along the hull."
    ),
    interior_appearance_description=(
        "The troop decks are vast compartments with standard bunks, standard food, "
        "standard lighting, and standard air. Vehicle bays on the lower decks carry "
        "standard armoured transports. The medical section is a field hospital. The "
        "ship functions as a military base during transit -- the marines train, eat, "
        "sleep, and prepare in standard military conditions."
    ),
    minimum_crew=[{"officers": 20}, {"crew": 140}],
    secondary_crew=[
        {"marine_officers": 60},
        {"marines": 5000},
        {"vehicle_crew": 250},
        {"medical": 35},
        {"ship_gunners": 24},
    ],
    additional_systems=[
        "Troop decks (standard accommodation)",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Field hospital",
        "Standard life support",
    ],
)

PHANTOM = ShipTemplate(
    name="Phantom",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Insertion Transport",
    combat_role="Special operations deployment behind enemy lines",
    length=150,
    armor=12,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=60,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump insertion transport for special operations deployment",
    long_description=(
        "The Phantom delivers SCN special forces behind enemy lines through hard jump "
        "points. SCN special operators are baseline humans -- extensively trained but "
        "not modified, augmented, or enhanced. They rely on training, equipment, and "
        "the intelligence network that MERIT maintains across the outer systems. The "
        "Phantom carries them in standard conditions -- pressurized, lit, heated -- "
        "because the operators are baseline humans who need standard conditions. The "
        "Phantom's low sensor profile comes from emission reduction design rather than "
        "the absence of life support systems."
    ),
    exterior_appearance_description=(
        "A 150-meter military spacecraft with a light grey hull. A smooth, flat angular shape "
        "with minimal external features. Recessed fittings and angled hull surfaces. A light "
        "ion turret in a flush mount on top. Engine bells with baffled exhausts at the rear. "
        "Loading ramps on the lower rear. Minimal markings -- navy blue trim limited to thin "
        "lines along the hull edges. Silver identification numbers in small font. Fewer "
        "running lights than standard."
    ),
    interior_appearance_description=(
        "The operator compartment holds bunks and equipment storage in standard "
        "conditions. The crew section is minimal -- a standard bridge and bunks. The "
        "hard-jump drive occupies the aft section."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 10}],
    secondary_crew=[
        {"special_forces": 48},
        {"special_forces_officers": 4},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Low-emission hull design",
        "Operator compartment (standard conditions)",
        "Standard life support",
    ],
)

IRIS = ShipTemplate(
    name="Iris",
    faction=ShipFaction.MERIT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Comms Ship",
    combat_role="Fleet communications relay",
    length=170,
    armor=25,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=120,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fleet communications relay extending SCN coordination range",
    long_description=(
        "The Iris extends SCN fleet communications beyond the range of fixed relay "
        "stations. MERIT's communications infrastructure is the most comprehensive in "
        "known space -- fixed relay stations at every major jump point, backed by Iris "
        "vessels that extend the network to wherever the fleet operates. The SCN's "
        "ability to maintain real-time fleet coordination across extended operations is "
        "a function of this communications depth. Other factions rely on modified crew "
        "(Pleiades), neural links (Polaris), or simply accept degraded coordination at "
        "range. MERIT builds the infrastructure to avoid the problem entirely."
    ),
    exterior_appearance_description=(
        "A 170-meter military spacecraft with a light grey hull. An angular fuselage with a "
        "large communications array on top -- a forest of antenna masts and relay dishes "
        "dominating the upper profile, making the ship top-heavy in silhouette. An ion turret "
        "on top forward of the antenna array. Engine bells in a cluster at the rear. Navy blue "
        "trim along the hull edges and at the base of the antenna array. Silver identification "
        "numbers on the sides. White running lights along the hull and at the antenna tips."
    ),
    interior_appearance_description=(
        "The communications centre is a well-lit compartment with operator stations. "
        "Standard displays, standard equipment. The crew works in comfortable conditions "
        "using standard instruments. Standard accommodation throughout."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 26}],
    secondary_crew=[{"communications_specialists": 12}],
    additional_systems=[
        "Fleet communications relay array",
        "Encrypted high-bandwidth communications suite",
        "Standard life support",
    ],
)


MERIT_SMALL_CRAFT = {
    "Sprite": SPRITE,
    "Harpy": HARPY,
    "Valkyrie": VALKYRIE,
    "Griffin": GRIFFIN,
    "Centaur": CENTAUR,
}

MERIT_CORVETTES = {
    "Satyr": SATYR,
    "Nereid": NEREID,
    "Sphinx": SPHINX,
}

MERIT_FRIGATES = {
    "Gorgon": GORGON,
    "Wyvern": WYVERN,
    "Argus": ARGUS,
    "Cerberus": CERBERUS,
}

MERIT_DESTROYERS = {
    "Hydra": HYDRA,
    "Fenrir": FENRIR,
    "Lamia": LAMIA,
    "Medusa": MEDUSA,
    "Cyclops": CYCLOPS,
}

MERIT_CRUISERS = {
    "Typhon": TYPHON,
    "Basilisk": BASILISK,
    "Muse": MUSE,
    "Echidna": ECHIDNA,
}

MERIT_CAPITALS = {
    "Leviathan": LEVIATHAN,
    "Gaia": GAIA,
    "Titan": TITAN,
}

MERIT_SUPPORT = {
    "Cornucopia": CORNUCOPIA,
    "Hermes": HERMES,
    "Dryad": DRYAD,
    "Asclepius": ASCLEPIUS,
    "Trojan": TROJAN,
    "Phantom": PHANTOM,
    "Iris": IRIS,
}

MERIT_ALL_SHIPS = {
    **MERIT_SMALL_CRAFT,
    **MERIT_CORVETTES,
    **MERIT_FRIGATES,
    **MERIT_DESTROYERS,
    **MERIT_CRUISERS,
    **MERIT_CAPITALS,
    **MERIT_SUPPORT,
}