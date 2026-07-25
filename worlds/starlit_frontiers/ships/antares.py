from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


WISP = ShipTemplate(
    name="Wisp",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.SMALL,
    ship_archetype="Scout",
    combat_role="Reconnaissance / forward sensor platform",
    length=12,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=2,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Stripped-down reconnaissance craft optimized for speed",
    long_description=(
        "The Wisp is the smallest and fastest thing in the Antaren fleet. Stripped of "
        "every gram of unnecessary weight, it carries a pilot, a sensor package, and a "
        "light laser that exists more for morale than lethality. The pilot doses before "
        "launch -- a fast-onset perceptual stimulant that sharpens visual processing and "
        "accelerates reaction time, turning the firehose of sensor data into something "
        "the human brain can parse at combat speed. A stimmed Wisp pilot sees contacts "
        "faster, classifies them faster, and feeds targeting data back to the fleet "
        "faster than any baseline human could manage. The tradeoff is that a Wisp pilot "
        "who stays out too long crashes hard -- the stimulant metabolizes in hours, and "
        "the cognitive drop-off is steep. Wisps run short, intense reconnaissance "
        "sorties. They do not loiter."
    ),
    exterior_appearance_description=(
        "A 12-meter single-seat military spacecraft with a pale grey hull. A small, angular "
        "body with a triangular cross-section and a large wraparound glazed canopy. A light "
        "laser mounted under the nose. Thin hull plating. A single oversized engine nacelle "
        "mounted on a short pylon above the rear fuselage. Orange angular slashes along the "
        "sides and nacelle pylon. Steel-blue identification numbers beneath the canopy."
    ),
    interior_appearance_description=(
        "A single seat in a cockpit barely wider than the pilot's shoulders. Instrument "
        "panels are dense and bright -- high-refresh displays calibrated for stimmed "
        "perception, flickering at speeds that would be illegible to a baseline eye. A "
        "stim auto-injector is mounted in the seat's headrest, delivering the dose on "
        "a timer linked to the launch sequence. The cockpit smells faintly of the "
        "chemical tang that permeates everything Antaren -- metabolic accelerant off-"
        "gassing through the pilot's skin."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Pre-launch stim injector", "High-refresh sensor displays"],
)

THUNDERBOLT = ShipTemplate(
    name="Thunderbolt",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=18,
    armor=2,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=5,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Fast bomber with stimmed approach run and single torpedo",
    long_description=(
        "The Thunderbolt carries a single antimatter torpedo to point-blank range. Every "
        "faction's bombers face the same harrowing approach through point defense fire. "
        "The Antaren answer is speed. The Thunderbolt is faster than any other faction's "
        "bomber -- Moderate where the template is Slow -- because its crew doses with a "
        "combat stimulant cocktail that lets them fly a lighter, faster airframe at the "
        "ragged edge of human reaction time. A stimmed Thunderbolt pilot threads point "
        "defense fire through reflexes that a baseline human simply does not have, "
        "jinking and rolling at speeds that would be suicidal without chemical "
        "enhancement. The tradeoff is hull integrity -- the Thunderbolt is lighter and "
        "more fragile than other factions' bombers. It survives the approach by not being "
        "where the fire is, not by absorbing it. When it works, it's beautiful. When it "
        "doesn't, the pilot is too stimmed to feel the impact."
    ),
    exterior_appearance_description=(
        "An 18-meter two-seat military spacecraft with a pale grey hull. A flat, angular body "
        "with a broad diamond-shaped cross-section. A glazed tandem canopy on top. The torpedo "
        "housing dominates the underside. Thin hull plating. Two engine nacelles on swept "
        "pylons mounted at the rear flanks, angled outward. Orange angular slashes across the "
        "torpedo housing and along the sides. A stylised flame emblem in orange and steel-blue "
        "on both sides. Steel-blue identification numbers on the upper fuselage."
    ),
    interior_appearance_description=(
        "Two seats in tandem -- pilot forward, weapons officer behind -- in a cockpit "
        "that feels more like a racing craft than a military bomber. The instruments are "
        "bright and fast, the controls twitchy and responsive. Stim auto-injectors in "
        "both headrests. The torpedo arming display is the only thing in the cockpit that "
        "feels heavy and deliberate. The interior smells of chemical accelerant and sweat."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Pre-launch stim injectors (x2)", "High-response flight controls"],
)

ZEPHYR = ShipTemplate(
    name="Zephyr",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.SMALL,
    ship_archetype="Interceptor",
    combat_role="Fast attack / anti-scout / anti-bomber",
    length=10,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=2,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_LASER_ARRAY],
    default_small_craft=[],
    short_description="Ultra-fast interceptor with stim-enhanced gunnery",
    long_description=(
        "The Zephyr is the Antaren interceptor -- the fastest, most aggressive small "
        "craft in their inventory and arguably the best interceptor in known space. Zero "
        "armor, minimal hull, maximum engine. The pilot doses with a fast-twitch combat "
        "stimulant that accelerates hand-eye coordination to the point where the Zephyr's "
        "stim-response laser tracks targets faster than any automated system. The weapon "
        "is the same class of emitter as the standard interceptor laser, but Antaren "
        "gunners push the firing cycle harder -- shorter pulses, faster tracking, more "
        "damage per second at the cost of accelerated component wear. A Zephyr burns "
        "through its laser emitter faster than any other interceptor, but the engagement "
        "is usually over before it matters. A Zephyr that hasn't killed its target in the "
        "first pass is unlikely to survive the second."
    ),
    exterior_appearance_description=(
        "A 10-meter single-seat military spacecraft with a pale grey hull. A needle-profile "
        "angular body with a faceted hexagonal cross-section. A narrow glazed canopy. A heavy "
        "laser array integrated into the nose. Thin hull plating with the structural frame "
        "visible at the edges. A single large engine bell at the rear on a short raised mount. "
        "Orange slashes along the fuselage spine and across the nose. Steel-blue wing "
        "designation stencilled beneath the canopy."
    ),
    interior_appearance_description=(
        "The pilot lies nearly prone in a contoured acceleration couch that constitutes "
        "the entire interior. The cockpit wraps tight around the body -- flight suit "
        "plugged directly into the ship's G-compensation system. Instruments are a "
        "heads-up display projected onto the narrow canopy, refreshing at a rate "
        "calibrated for stimmed perception. The stim auto-injector is wrist-mounted -- "
        "the pilot controls the dose. Veterans adjust their own cocktail. The space is "
        "barely larger than a coffin and smells of sweat and chemical accelerant."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Wrist-mounted stim injector", "High-refresh HUD", "G-compensation system"],
)

SQUALL = ShipTemplate(
    name="Squall",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.SMALL,
    ship_archetype="Fighter",
    combat_role="Escort / area control / anti-small-craft",
    length=15,
    armor=4,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=8,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.PLASMA_LAUNCHER],
    default_small_craft=[],
    short_description="Fast escort fighter with stimmed pilot reflexes",
    long_description=(
        "The Squall is the Antaren general-purpose fighter -- faster than any other "
        "faction's equivalent, lighter than all of them. Where other factions' fighters "
        "balance speed and survivability, the Squall leans hard into speed and trusts its "
        "stimmed pilot to avoid the hits that its thin hull cannot absorb. Squalls escort "
        "Thunderbolt bombers through enemy interceptor screens, and their speed advantage "
        "lets them dictate engagement terms -- a Squall pilot on combat stims can choose "
        "when and where to fight, closing to plasma range, firing, and breaking away "
        "before the target can reorient. Squalls work in wings, their stimmed pilots "
        "coordinating through the jittery, overlapping radio chatter that characterizes "
        "Antaren combat communications -- too fast for baseline humans to follow, a "
        "stimmed conversation happening at chemical speed."
    ),
    exterior_appearance_description=(
        "A 15-meter single-seat military spacecraft with a pale grey hull. A faceted angular "
        "body with a pentagonal cross-section -- flat top, two angled lower surfaces meeting "
        "at a sharp keel line. A large wraparound glazed canopy. A plasma launcher housing "
        "under the nose. Thin hull plating with the structural frame visible beneath at the "
        "edges. Two engine nacelles on short pylons mounted high on the rear flanks, angled "
        "outward. Orange angular slashes across the hull -- on the sides, across the nose, and "
        "along the nacelle pylons. A stylised flame emblem in orange and steel-blue on both "
        "sides. Steel-blue wing designation stencilled beneath the canopy."
    ),
    interior_appearance_description=(
        "A single-seat cockpit with a wide canopy and dense, bright instrument panels. "
        "The controls are light and responsive -- designed for the twitchy, accelerated "
        "inputs of a stimmed pilot. A baseline human would over-correct constantly. The "
        "stim auto-injector is seat-mounted, and a secondary manual injector is clipped "
        "to the flight harness for the pilot to adjust dosage mid-engagement. Veterans "
        "carry their own preferred cocktail blends."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Seat-mounted stim injector", "Manual backup injector", "High-response flight controls"],
)

FLURRY = ShipTemplate(
    name="Flurry",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=20,
    armor=8,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=15,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.REINFORCED_PLASMA_CANNON],
    default_small_craft=[],
    short_description="Fast gunship with overcharged plasma cannon and stimmed crew",
    long_description=(
        "The Flurry is the Antaren gunship -- faster than any other faction's equivalent, "
        "carrying a plasma cannon that its crew pushes past safe operating limits. The "
        "overcharged plasma cannon is a lighter weapon class than the standard gunship "
        "mount, but Antaren gunners run it at power settings the manufacturer would not "
        "approve, achieving higher damage output than a standard plasma cannon at the "
        "cost of accelerated barrel wear and occasional capacitor failures. The Flurry's "
        "crew of four are all stimmed for combat -- the pilot and gunner on fast-twitch "
        "compounds, the engineer on a focus stimulant that lets them manage the "
        "overcharged weapon's power demands in real time. The Flurry dashes through "
        "escort screens rather than walking through them -- speed where other factions "
        "use armor. If it gets hit, it dies. It is very hard to hit."
    ),
    exterior_appearance_description=(
        "A 20-meter multi-crew military spacecraft with a pale grey hull. A broad, faceted "
        "angular body with an irregular hexagonal cross-section -- flat top, angled sides, "
        "flat bottom. A wide glazed canopy. A reinforced plasma cannon housing on the "
        "underside. Thin hull plating. Two engine nacelles on swept pylons at the midsection, "
        "protruding from the sides. Orange angular slashes in aggressive patterns across the "
        "hull and nacelle pylons. A stylised flame emblem in orange and steel-blue on both "
        "sides. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "Four stations in a tight cabin -- pilot and gunner forward, engineer and sensor "
        "operator behind. The overcharged plasma cannon's power feeds run through the "
        "cabin center, running hotter than spec and radiating a warmth the crew learns "
        "to ignore. Stim auto-injectors at each station. The engineer's station has "
        "additional displays for weapon power management -- the overcharged cannon "
        "requires constant attention to keep from burning out. The cockpit smells of "
        "ozone, chemical accelerant, and the faint sweet note of capacitor coolant."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}],
    secondary_crew=[{"engineer": 1}, {"sensor_operator": 1}],
    additional_systems=["Stim auto-injectors (x4)", "Weapon power management system", "Overcharged capacitor array"],
)

GALE = ShipTemplate(
    name="Gale",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=56,
    armor=18,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=50,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=14,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast patrol corvette with stimmed crew and short endurance",
    long_description=(
        "The Gale is the fastest patrol corvette in known space and the most commonly "
        "encountered Antaren warship. It runs system security with a skeleton crew on "
        "maintenance stim doses -- low-level chemical enhancement that keeps the crew "
        "alert and reactive during patrol without the metabolic cost of full combat "
        "stimulation. When contact is made, the crew doses up and the Gale becomes "
        "something fundamentally different: a corvette with the reaction speed of a "
        "fighter, closing to engagement range faster than contacts expect. The Gale's "
        "weakness is endurance. Its shorter supply duration and the cumulative metabolic "
        "toll of sustained stim use mean it cannot stay on station as long as other "
        "factions' patrol corvettes. An Antaren system with a single Gale on patrol "
        "has aggressive, fast security coverage -- but it has gaps."
    ),
    exterior_appearance_description=(
        "A 56-meter military spacecraft with a pale grey hull. An angular, faceted body with a "
        "sharp front and a trapezoidal cross-section -- wide flat top, narrowing toward the "
        "bottom. A particle cannon housing along the top ridge. A heavy laser turret on top "
        "behind the bridge. A glazed bridge canopy near the front. Thin hull plating. Engine "
        "nacelles on pylons at the midsection, protruding from both sides. Orange angular "
        "slashes along the hull sides, around the bridge, and on the nacelle pylons. A "
        "stylised flame emblem in orange and steel-blue on both sides. Steel-blue "
        "identification numbers and fleet markings stencilled on the sides."
    ),
    interior_appearance_description=(
        "The bridge is a tight half-circle of high-refresh stations with acceleration "
        "couches instead of standard chairs. The crew run maintenance stims during patrol "
        "-- a low dose dispensed through the ship's stim system, keeping everyone alert "
        "without the metabolic spike of combat dosing. Combat stim packs are racked by "
        "each station for rapid dosing when contact is made. Crew quarters are small and "
        "utilitarian. The ship carries a basic dispensary amidships -- stim compounds, "
        "metabolic stabilizers, and the crash recovery medications that every Antaren "
        "vessel stocks. The air has the faint chemical sweetness of metabolic accelerant."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 10}],
    secondary_crew=[{"gunners": 3}],
    additional_systems=[
        "Stim dispensary (basic)",
        "Bridge stim distribution system",
        "Crash recovery supplies",
        "High-refresh combat displays",
    ],
)

UPDRAFT = ShipTemplate(
    name="Updraft",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=52,
    armor=10,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=30,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=14,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Squall", 5)],
    short_description="Fast tender corvette carrying five Squall fighters",
    long_description=(
        "The Updraft carries and supports a detachment of Antaren small craft -- typically "
        "five Squall fighters -- extending their operational range. The Updraft itself is "
        "faster than the template tender, reaching threatened areas quickly and deploying "
        "its wing without delay. The ship carries stim resupply for its embarked pilots "
        "-- the chemical compounds that Antaren small craft burn through faster than "
        "ammunition. An Updraft's most critical stores are not fuel or spare parts but "
        "the carefully regulated stim packs that keep its pilots combat-effective. The "
        "tender's hangar crew work on low-dose maintenance stims during turnaround "
        "operations, keeping rearming times short. Supply endurance is limited -- the "
        "Updraft operates from forward positions and returns to resupply frequently."
    ),
    exterior_appearance_description=(
        "A 52-meter military spacecraft with a pale grey hull. A wide, flat angular body with "
        "a rectangular cross-section and hard-angled edges. Launch cradles for fighters "
        "visible along both sides, lit from within in amber. A light ion turret on top. Thin "
        "hull plating. Engine nacelles on short pylons at the rear flanks. Orange trim along "
        "the hull edges and around the launch bay openings. Steel-blue identification numbers "
        "on the sides and top."
    ),
    interior_appearance_description=(
        "The interior splits between a small crew section forward and the hangar aft. "
        "The hangar is functional and fast -- launch cradles built for rapid turnaround, "
        "with stim resupply stations at each craft position where pilots top up their "
        "injector packs between sorties. The crew section is compact. A small dispensary "
        "handles stim resupply for both ship crew and embarked pilots. The ship has the "
        "frantic, wired energy of a place where people are always slightly accelerated."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 7}],
    secondary_crew=[
        {"embarked_craft_pilots": 5},
        {"hangar_maintenance": 3},
    ],
    additional_systems=[
        "Hangar bay (5 small craft)",
        "Craft maintenance and rearm facilities",
        "Pilot stim resupply station",
        "Stim dispensary (basic)",
        "Crash recovery supplies",
    ],
)

NIMBUS = ShipTemplate(
    name="Nimbus",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Survey Corvette",
    combat_role="Hazardous environment operations / exploration",
    length=48,
    armor=18,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=30,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Fast survey corvette with stim-enhanced sensor operators",
    long_description=(
        "The Nimbus is the Antaren survey corvette -- built to enter hazardous "
        "environments faster than the template and leave before the environment kills it. "
        "Its sensor operators dose with a perceptual stimulant that accelerates data "
        "processing, allowing them to extract usable intelligence from a brief, fast pass "
        "through conditions that other factions' survey ships would approach slowly and "
        "methodically. The Nimbus does not linger. It jumps in, burns through the survey "
        "area at speed, and jumps out before radiation, gravitational distortion, or "
        "nebular interference accumulates enough to threaten the lighter hull. This "
        "aggressive survey doctrine sacrifices thoroughness for speed -- an Antaren survey "
        "will miss details a Polaran Quadrant would catch, but it completes in hours "
        "what other factions take days to accomplish."
    ),
    exterior_appearance_description=(
        "A 48-meter military spacecraft with a pale grey hull. A compact angular body with a "
        "faceted pentagonal cross-section. A glazed bridge canopy near the front. A light ion "
        "turret on top toward the rear. Minimal sensor equipment -- a small cluster at the "
        "front. Thin hull plating. Engine nacelles on pylons at the midsection. Orange trim "
        "along the hull edges. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The bridge is configured for rapid sensor processing -- high-refresh displays "
        "surrounding the sensor operators' stations, calibrated for stimmed perception. "
        "The analysis room amidships is a dense cluster of processing equipment where "
        "survey data is compressed and packaged in real time. Crew quarters are minimal. "
        "The dispensary stocks the specific perceptual stimulants that the sensor team "
        "uses -- different compounds from the combat stims, optimized for data processing "
        "rather than physical reaction speed."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[{"survey_specialists": 3}],
    additional_systems=[
        "Stim dispensary (basic, perceptual compounds)",
        "High-refresh sensor displays",
        "Rapid survey processing suite",
        "Crash recovery supplies",
    ],
)

TEMPEST = ShipTemplate(
    name="Tempest",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Combat Frigate",
    combat_role="Fleet screening / torpedo attack",
    length=140,
    armor=30,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=75,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=21,
    default_weapons=[
        weapons.RAILGUN,
        weapons.ANTIMATTER_TORPEDO,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Fast combat frigate with stim-enhanced gunnery and torpedo armament",
    long_description=(
        "The Tempest is the Antaren fleet's primary screening combatant -- a frigate "
        "built for speed and aggression at the expense of everything else. Faster than "
        "the template combat frigate, lighter on armor and hull, the Tempest closes to "
        "torpedo range faster than the enemy expects and fires before they can react. A "
        "pack of Tempests on combat stims executing a torpedo run is one of the most "
        "dangerous attacks in known space -- not because of individual ship quality, but "
        "because of the stimmed speed of the approach. The combat pharmacology bay "
        "manages crew chemistry in real time during engagements, adjusting doses to "
        "mission phase: perceptual stims for the approach, fast-twitch compounds for the "
        "engagement, metabolic stabilizers for the withdrawal. The Tempest's stim-response "
        "laser turret is manned by a gunner whose reaction time has been chemically "
        "reduced to the point where the weapon tracks faster than its automated backup. "
        "The Tempest cannot sustain a prolonged fight -- its crew burns through stim "
        "reserves, its thin hull accumulates damage it cannot absorb, and its shorter "
        "supply duration means it cannot stay in the field as long. It wins fast or it "
        "dies."
    ),
    exterior_appearance_description=(
        "A 140-meter military spacecraft with a pale grey hull. A narrow, faceted angular body "
        "with a sharp front and a diamond-shaped cross-section -- angled surfaces meeting at "
        "hard edges on all four sides. Thin hull plating. A railgun housing along the top "
        "ridge. A recessed torpedo bay in the lower front with flush-fitting doors. Engine "
        "nacelles on swept pylons at the midsection, protruding from the sides. A large bridge "
        "canopy near the front. Orange angular slashes in aggressive geometric patterns across "
        "the hull -- along the sides, radiating from the engine pylons, and in chevron "
        "patterns on the front. A stylised flame emblem in orange and steel-blue on both sides "
        "forward. Steel-blue identification numbers stencilled beneath the engine pylons."
    ),
    interior_appearance_description=(
        "The bridge is a ring of acceleration couches with high-refresh combat displays. "
        "The combat pharmacology bay is a sealed compartment amidships, staffed by a "
        "combat pharmacologist who monitors the crew's chemical state in real time and "
        "adjusts dosing through the ship's stim distribution system. The system runs "
        "stim compound through dedicated lines to every combat station -- the crew doses "
        "without leaving their posts. The torpedo room is forward, its crew on fast-twitch "
        "compounds for rapid loading. Crew quarters are small and spartan. The crash ward "
        "adjacent to the pharmacology bay handles the post-combat metabolic crash -- bunks "
        "with monitoring equipment, IV lines, and the bitter stabilizer compounds that "
        "ease the comedown."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 38}],
    secondary_crew=[
        {"gunners": 10},
        {"torpedo_crew": 6},
        {"combat_pharmacologist": 1},
        {"medical": 2},
    ],
    additional_systems=[
        "Combat pharmacology bay",
        "Ship-wide stim distribution system",
        "Crash ward (8 bunks)",
        "High-refresh combat displays",
        "Stim-response weapon tracking system",
    ],
)

MIRAGE = ShipTemplate(
    name="Mirage",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=150,
    armor=5,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=35,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=28,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Fast hard-jump scout with stim-enhanced sensor processing",
    long_description=(
        "The Mirage is the Antaren scout frigate -- a hard-jump-capable vessel that "
        "appears where no one expects, gathers intelligence at speed, and vanishes. "
        "Faster than the template scout frigate, the Mirage compensates for its lighter "
        "hull with the ability to outrun anything that detects it. Its sensor operators "
        "dose with perceptual stimulants that allow them to process the firehose of "
        "intelligence data from a fast pass through an enemy system -- absorbing in hours "
        "what a baseline crew would need days to analyze. The Mirage's weakness is "
        "endurance. Its supply duration is well below template, and its crew's stim "
        "reserves limit how long they can sustain the enhanced perception that makes "
        "the ship effective. A Mirage does not conduct long-duration intelligence "
        "missions. It conducts fast, aggressive reconnaissance raids -- in, observe, "
        "out -- and returns to the fleet to report."
    ),
    exterior_appearance_description=(
        "A 150-meter military spacecraft with a pale grey hull. A long, narrow angular body "
        "with a faceted octagonal cross-section and a pointed front. An ion cannon on the top "
        "ridge. A glazed bridge canopy near the front. Thin hull plating. Engine nacelles on "
        "long swept pylons at the midsection. The hull is clean and spare -- fewer external "
        "fittings than a combat vessel. Orange trim in thin lines along the hull edges and "
        "nacelle pylons. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The forward section is sensor equipment and a fast-processing analysis room "
        "where intelligence specialists work on perceptual stims, absorbing data at "
        "accelerated speed. The hard-jump drive occupies the aft section. Living spaces "
        "are compressed in the middle -- small berths, a galley, and the pharmacology bay "
        "that manages the sensor team's specialized stim compounds. The crash ward is "
        "larger than on a combat frigate -- the perceptual stims used by intelligence "
        "specialists produce a harder metabolic crash than combat compounds, and "
        "recovery times are longer. The ship has the tense, wired atmosphere of a place "
        "where everyone is running slightly too fast."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 20}],
    secondary_crew=[
        {"intelligence_analysts": 6},
        {"sensor_specialists": 4},
        {"combat_pharmacologist": 1},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array",
        "Intelligence analysis suite (rapid processing)",
        "Combat pharmacology bay (perceptual compounds)",
        "Crash ward (6 bunks)",
        "High-refresh sensor displays",
    ],
)

CROSSWIND = ShipTemplate(
    name="Crosswind",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=128,
    armor=15,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=45,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.REINFORCED_PLASMA_CANNON, weapons.HEAVY_LASER_ARRAY],
    default_small_craft=[],
    short_description="Extremely fast escort frigate with stim-enhanced tracking",
    long_description=(
        "The Crosswind is the fastest frigate in known space -- Very Fast where the "
        "template is Fast -- and it uses that speed to provide an aggressive, mobile "
        "defensive screen for Antaren convoys. Where other factions' escort frigates "
        "hold position and absorb incoming attacks, the Crosswind intercepts threats "
        "before they reach the convoy, closing on incoming bombers and torpedo craft "
        "at speeds that turn defense into attack. Its stimmed gunners track targets with "
        "chemically enhanced reaction times, the stim-response laser engaging small craft "
        "with a speed that automated point defense cannot match. The overcharged plasma "
        "cannon handles heavier threats. The Crosswind's weakness is the same as every "
        "Antaren ship: thin hull, short endurance, no ability to absorb sustained "
        "punishment. If the Crosswind's aggressive interception fails and the engagement "
        "becomes a slugging match, it loses."
    ),
    exterior_appearance_description=(
        "A 128-meter military spacecraft with a pale grey hull. A compact, angular body with a "
        "trapezoidal cross-section and a blunt front. A reinforced plasma cannon housing on "
        "the top ridge. A heavy laser array integrated into the front. Thin hull plating. "
        "Engine nacelles on swept pylons at the midsection. Orange angular slashes across the "
        "hull and nacelle pylons. A stylised flame emblem in orange and steel-blue on both "
        "sides. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The bridge is built for speed -- acceleration couches rated for high-G "
        "maneuvering, inertial compensation systems throughout. The combat pharmacology "
        "bay manages the crew's stim state during the rapid accelerations that the "
        "Crosswind's interception doctrine demands -- dosing adjustments account for the "
        "physiological effects of sustained high-G turns. The gunners' stations have "
        "enhanced tracking displays calibrated for stimmed perception. The crash ward "
        "handles both stim crashes and G-force injuries. Crew quarters are minimal -- "
        "the Crosswind's short supply duration means it operates from forward bases "
        "rather than on extended independent deployment."
    ),
    minimum_crew=[{"officers": 6}, {"crew": 24}],
    secondary_crew=[
        {"gunners": 8},
        {"combat_pharmacologist": 1},
        {"medical": 2},
    ],
    additional_systems=[
        "Combat pharmacology bay",
        "Ship-wide stim distribution system",
        "High-G inertial compensation system",
        "Crash ward (6 bunks)",
        "Stim-response weapon tracking system",
    ],
)

HAILSTORM = ShipTemplate(
    name="Hailstorm",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=210,
    armor=45,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=140,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[
        weapons.RAILGUN,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Fast fleet destroyer with stim-enhanced triple point defense",
    long_description=(
        "The Hailstorm is the shield of the Antaren battle fleet -- faster than the "
        "template fleet destroyer, with point defense gunners whose stimmed reaction "
        "times let them track and engage incoming small craft with a speed that "
        "compensates for the lighter Antaren hull. The three stim-response laser turrets "
        "are each manned by a stimmed gunner whose chemically enhanced hand-eye "
        "coordination turns the weapon into something faster than automated tracking -- "
        "the gunner doesn't follow the target, they anticipate it, the stims giving "
        "them the processing speed to lead shots at ranges that baseline humans cannot "
        "manage. The combat pharmacology bay manages the point defense crew's chemistry "
        "as a combat-critical system -- the PD gunners run hotter doses than the rest of "
        "the crew, burning through stim reserves faster. A Hailstorm's PD coverage is "
        "excellent in the first hours of an engagement and degrades as the gunners "
        "metabolize their compounds. The Hailstorm does not carry enough stim reserves "
        "for a prolonged defensive action."
    ),
    exterior_appearance_description=(
        "A 210-meter military spacecraft with a pale grey hull. A broad, angular body with a "
        "faceted hexagonal cross-section -- flat top, angled upper sides, vertical lower "
        "sides, flat bottom. A railgun housing along the top ridge. Two heavy laser arrays "
        "mounted on the angled upper sides. Thin hull plating. Engine nacelles on heavy pylons "
        "at the midsection, protruding from both sides. A glazed bridge section near the "
        "front. Orange angular slashes in bold patterns across the hull -- along the sides, "
        "across the front, and radiating from the engine pylons. A stylised flame emblem in "
        "orange and steel-blue at large scale on both sides. Steel-blue fleet markings and "
        "ship name stencilled on the sides."
    ),
    interior_appearance_description=(
        "The three point defense battery stations are distributed port, starboard, and "
        "dorsal, each built around the stimmed gunner's acceleration couch with direct "
        "stim feed lines from the pharmacology bay. The pharmacology bay is larger than "
        "on a frigate -- two combat pharmacologists managing the chemistry of a larger "
        "crew, with dedicated monitoring for the PD gunners who run the hottest doses "
        "aboard. The crash ward is sized for the post-engagement crash: when the stims "
        "wear off, the PD gunners go down hard, and the medical staff manage the "
        "metabolic fallout. The bridge is a command amphitheater of acceleration couches "
        "with high-refresh displays."
    ),
    minimum_crew=[{"officers": 14}, {"crew": 80}],
    secondary_crew=[
        {"gunners": 25},
        {"point_defense_crew": 20},
        {"combat_pharmacologists": 2},
        {"medical": 6},
    ],
    additional_systems=[
        "Combat pharmacology bay (expanded)",
        "Ship-wide stim distribution system",
        "PD gunner dedicated stim feeds",
        "Crash ward (16 bunks)",
        "High-speed tracking gimbals (PD turrets)",
        "Stim-response weapon tracking system",
    ],
)

CYCLONE = ShipTemplate(
    name="Cyclone",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=200,
    armor=30,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=110,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fast pursuit destroyer with stimmed crew and torpedo armament",
    long_description=(
        "The Cyclone is the Antaren pursuit ship -- and unlike the Canopan Thunderbird, "
        "which hunts through endurance, the Cyclone hunts through raw speed. It is the "
        "fastest hunter destroyer in known space. When a Cyclone locks onto a target, "
        "the crew doses with pursuit-optimized stims and the ship accelerates to a speed "
        "that nothing in its weight class can match. The pursuit is short and violent -- "
        "the Cyclone closes, fires its heavy particle cannon and torpedo at close range, "
        "and either kills the target or breaks off. It does not track targets for weeks. "
        "It does not wait for them to make mistakes. It runs them down, kills them, and "
        "moves to the next. The Cyclone's weakness is the same as every Antaren warship: "
        "it cannot sustain a prolonged chase. If the target evades the initial closure, "
        "the Cyclone's stim reserves and supply endurance limit how long the pursuit can "
        "continue. Cyclones often operate in pairs -- if the first ship's closure fails, "
        "the second is already on an intercept vector."
    ),
    exterior_appearance_description=(
        "A 200-meter military spacecraft with a pale grey hull. A lean, elongated angular body "
        "with a diamond-shaped cross-section and a sharp pointed front. A heavy particle "
        "cannon housing extends forward from the front. A torpedo bay recessed in the lower "
        "front. An ion turret on top. Thin hull plating. Oversized engine nacelles on heavy "
        "swept pylons at the midsection. Orange angular slashes along the hull and nacelle "
        "pylons. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "Built for the intensity of pursuit and close-range engagement. The bridge is "
        "a cluster of acceleration couches with high-refresh displays showing closure "
        "rates and intercept geometry. The torpedo room is forward, its crew on "
        "fast-twitch stims for rapid loading. The combat pharmacology bay manages "
        "pursuit-specific compound blends -- stim cocktails optimized for sustained focus "
        "and reaction speed during the high-G closure phase. The crash ward is aft, "
        "handling the metabolic fallout from the pursuit stims. Crew quarters are "
        "spartan -- the Cyclone does not spend long at sea."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 65}],
    secondary_crew=[
        {"gunners": 15},
        {"torpedo_crew": 6},
        {"combat_pharmacologist": 1},
        {"medical": 4},
    ],
    additional_systems=[
        "Combat pharmacology bay",
        "Ship-wide stim distribution system",
        "Pursuit-optimized compound blends",
        "Crash ward (12 bunks)",
        "High-refresh combat displays",
    ],
)

AURORA = ShipTemplate(
    name="Aurora",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="EW Destroyer",
    combat_role="Electronic warfare / jamming / information denial",
    length=220,
    armor=25,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=90,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Fast EW destroyer with stim-enhanced electronic warfare operators",
    long_description=(
        "The Aurora is the Antaren electronic warfare platform -- a destroyer-sized vessel "
        "packed with jamming equipment, sensor spoofing systems, and emissions warfare "
        "arrays. Its EW operators dose with a specialized perceptual stimulant that "
        "accelerates their ability to identify, classify, and counter enemy electronic "
        "emissions in real time. A stimmed EW operator on the Aurora processes the "
        "electromagnetic environment faster than automated systems, identifying "
        "vulnerabilities in enemy sensor networks and exploiting them before the enemy "
        "can adapt. The Aurora is one of the few ships that distinguishes Antaren "
        "doctrine from pure brute-force aggression -- electronic warfare is a thinking "
        "person's game, and the stims make the thinking faster. The Aurora's speed lets "
        "it reposition rapidly, denying the enemy a stable picture of where the jamming "
        "is coming from. Light hull and short endurance are its standard Antaren weaknesses."
    ),
    exterior_appearance_description=(
        "A 220-meter military spacecraft with a pale grey hull. An angular body with a faceted "
        "pentagonal cross-section. Electronic warfare arrays mounted in angular housings along "
        "the top and sides -- flat panels and emitter housings at sharp angles to the hull. An "
        "ion cannon on the top ridge. Thin hull plating. Engine nacelles on pylons at the "
        "midsection. Orange trim along the hull edges and around each EW housing. Steel-blue "
        "identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The electronic warfare center is a large, sealed compartment amidships -- a "
        "room of operator stations where the EW team works on perceptual stims, "
        "immersed in the electromagnetic environment displayed on high-refresh screens. "
        "The operators describe the stimmed experience as seeing radio -- emissions become "
        "visual patterns, jamming becomes a physical gesture, and the entire electromagnetic "
        "battlespace unfolds as something the stimmed brain can grasp intuitively. The "
        "pharmacology bay stocks specialized perceptual compounds for the EW team. The "
        "crash ward is larger than typical -- EW operators burn through perceptual stims "
        "faster than combat crews, and the metabolic crash is harsher. The bridge is "
        "forward, conventional."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 55}],
    secondary_crew=[
        {"ew_operators": 16},
        {"combat_pharmacologist": 1},
        {"medical": 4},
    ],
    additional_systems=[
        "Electronic warfare center",
        "Jamming array (broadband)",
        "Sensor spoofing system",
        "Emissions analysis suite",
        "Combat pharmacology bay (perceptual compounds)",
        "Crash ward (12 bunks)",
        "High-refresh EW displays",
    ],
)

TYPHOON = ShipTemplate(
    name="Typhoon",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=390,
    armor=58,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=280,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[
        weapons.PRECISION_RAILGUN,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Fast, aggressive line cruiser with stim-enhanced gunnery and short endurance",
    long_description=(
        "The Typhoon is the Antaren main line combatant and the ship where their "
        "doctrine's strengths and weaknesses are most visible. Faster than the template "
        "heavy cruiser -- Moderate where the standard is Slow -- the Typhoon maneuvers "
        "into advantageous positions and delivers devastating gunnery from stimmed crew "
        "who achieve hit rates that compensate for the lighter hull. The combat "
        "pharmacology department manages the chemistry of hundreds of crew in real time, "
        "tuning compound blends to the engagement phase: approach, engagement, sustained "
        "combat, withdrawal. A Typhoon in the first hours of a battle is terrifying -- its "
        "stimmed gunnery is the most accurate in any faction's fleet. A Typhoon after "
        "twelve hours of sustained combat is in serious trouble -- stim reserves depleted, "
        "crew crashing, thin hull accumulating damage it cannot absorb. The Typhoon wins "
        "battles that are decided fast. It loses battles that grind."
    ),
    exterior_appearance_description=(
        "A 390-meter military spacecraft with a pale grey hull. A massive angular body with an "
        "irregular hexagonal cross-section -- flat top, sharply angled upper sides, vertical "
        "lower sides. A precision railgun housing along the top ridge. Weapon batteries in "
        "angular housings along both upper sides. Point-defense turrets spaced along the lower "
        "sides. Thin hull plating. Engine nacelles on heavy pylons at the "
        "midsection and additional engine bells at the rear. A large glazed bridge section "
        "near the front. Orange angular slashes in bold patterns across the hull. A stylised "
        "flame emblem in orange and steel-blue at large scale on both sides. Steel-blue fleet "
        "markings and ship name on the sides."
    ),
    interior_appearance_description=(
        "The combat pharmacology department is a full medical section amidships -- two "
        "pharmacologists, dedicated stim compounding equipment, and a monitoring suite "
        "that tracks the chemical state of every combat station on the ship. The stim "
        "distribution system runs compound through dedicated lines to every gunnery "
        "station, bridge position, and damage control post. The crash ward occupies a "
        "full section adjacent to the pharmacology department -- dozens of bunks with "
        "monitoring equipment, IV lines, and the metabolic stabilizers that manage the "
        "post-combat crash. The bridge is a command amphitheater of acceleration couches. "
        "Crew quarters are spartan. The wardroom is small -- the Typhoon's shortened "
        "supply duration means shorter deployments and less need for shipboard amenities."
    ),
    minimum_crew=[{"senior_officers": 6}, {"officers": 32}, {"crew": 260}],
    secondary_crew=[
        {"gunners": 55},
        {"point_defense_crew": 20},
        {"combat_pharmacologists": 2},
        {"medical": 10},
    ],
    additional_systems=[
        "Combat pharmacology department",
        "Ship-wide stim distribution system",
        "Stim compounding facility",
        "Crash ward (30 bunks)",
        "Crew chemical state monitoring suite",
        "High-refresh combat displays",
    ],
)

SIROCCO = ShipTemplate(
    name="Sirocco",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=365,
    armor=42,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=185,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Fast medium-jump cruiser for aggressive flanking strikes",
    long_description=(
        "The Sirocco is the largest Antaren combat ship that can use medium jump points "
        "and the backbone of their flanking forces. When a Sirocco comes through a medium "
        "jump at the enemy's rear, the stimmed crew is already dosed and the weapons are "
        "already hot. No other faction's flanking cruiser arrives this fast or this "
        "aggressive. The Sirocco's doctrine is pure Antaren: hit hard from an unexpected "
        "angle before the enemy can react, then exploit the chaos. The flanking force "
        "does not plan to hold position -- it plans to break something important and "
        "withdraw before the enemy can reorient. The Sirocco's weaknesses -- thin armor, "
        "light hull, short endurance -- are mitigated by the flanking doctrine itself: "
        "if the enemy is shooting back in a sustained way, the flanking force has "
        "already failed."
    ),
    exterior_appearance_description=(
        "A 365-meter military spacecraft with a pale grey hull. A lean, elongated angular body "
        "with a diamond-shaped cross-section. A lean, elongated profile. A heavy railgun housing along the top ridge. Two laser turrets on the upper "
        "sides. Thin hull plating. Oversized engine nacelles on swept pylons at the "
        "midsection. Orange angular slashes along the hull. A stylised flame emblem in orange "
        "and steel-blue on both sides. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The bridge includes additional stations for task force coordination -- the Sirocco "
        "often leads a flanking group and its captain needs situational awareness of "
        "every ship in the formation. The combat pharmacology department manages "
        "stim compounds optimized for the unique demands of flanking operations: "
        "high-alertness compounds for the approach through the jump point, fast-twitch "
        "combat stims for the engagement, and immediate crash management for the "
        "withdrawal. A full medical bay handles combat casualties and stim-related "
        "injuries. Crew quarters are a step above the Typhoon -- the Sirocco operates "
        "independently and needs slightly more liveable spaces."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 24}, {"crew": 190}],
    secondary_crew=[
        {"gunners": 30},
        {"point_defense_crew": 15},
        {"combat_pharmacologists": 2},
        {"task_force_staff": 8},
        {"medical": 8},
    ],
    additional_systems=[
        "Combat pharmacology department",
        "Ship-wide stim distribution system",
        "Task force coordination suite",
        "Crash ward (20 bunks)",
        "Crew chemical state monitoring suite",
    ],
)

MONSOON = ShipTemplate(
    name="Monsoon",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Command Cruiser",
    combat_role="Fleet coordination / flagship for medium-jump task forces",
    length=400,
    armor=33,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=185,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast command cruiser with fleet stim coordination",
    long_description=(
        "The Monsoon is where an Antaren admiral sits -- and an Antaren admiral's job "
        "includes something no other faction's flag officer deals with: fleet-wide "
        "chemical coordination. The Monsoon's command section includes a senior combat "
        "pharmacologist who advises the admiral on fleet stim state -- which ships' crews "
        "are at peak performance, which are approaching metabolic limits, and which are "
        "going to crash within the hour. This information shapes Antaren fleet tactics "
        "in ways that outsiders find baffling: ships are rotated in and out of the "
        "battle line not based on damage but on their crew's chemical state. A ship "
        "with a fresh stim dose replaces one whose crew is burning out, maintaining "
        "the fleet's aggregate performance even as individual ships cycle. The Monsoon "
        "coordinates this chemical ballet alongside conventional fleet command."
    ),
    exterior_appearance_description=(
        "A 400-meter military spacecraft with a pale grey hull. An angular body with a "
        "trapezoidal cross-section and a raised bridge superstructure near the front -- larger "
        "than standard, with a wide glazed bridge for fleet coordination. Communications "
        "antenna clusters at the top of the bridge section. A heavy particle cannon housing "
        "extends from the front. A heavy laser turret on top behind the bridge. Engine "
        "nacelles on heavy pylons at the midsection. Orange angular slashes across the hull "
        "and around the bridge superstructure. A stylised flame emblem in orange and "
        "steel-blue at large scale on both sides. Steel-blue fleet markings and ship name "
        "prominently displayed."
    ),
    interior_appearance_description=(
        "The command section is the ship's heart -- stations for the admiral, flag staff, "
        "communications officers, and the senior combat pharmacologist who monitors "
        "fleet-wide stim state on a dedicated display. The fleet pharmacology section "
        "maintains compound reserves for resupply to other ships in the task force -- "
        "stim packs, metabolic stabilizers, and crash recovery compounds shipped by "
        "shuttle during lulls. Additional briefing rooms and an intelligence analysis "
        "suite surround the command section. The crash ward is the largest in the fleet "
        "at this size class -- the flag staff and command crew run sustained stim doses "
        "during multi-day operations, and the metabolic cost accumulates. The Monsoon's "
        "crew quarters are the best in the Antaren fleet at cruiser size -- an admission "
        "that flag officers need rest between stim cycles."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 30}, {"crew": 210}],
    secondary_crew=[
        {"gunners": 18},
        {"flag_staff": 12},
        {"communications_officers": 10},
        {"senior_combat_pharmacologist": 1},
        {"combat_pharmacologists": 2},
        {"medical": 10},
    ],
    additional_systems=[
        "Fleet command section",
        "Fleet stim state monitoring system",
        "Fleet pharmacology resupply section",
        "Combat pharmacology department",
        "Ship-wide stim distribution system",
        "Crash ward (25 bunks)",
        "Fleet communications suite",
        "Intelligence analysis suite",
    ],
)

CLOUDBANK = ShipTemplate(
    name="Cloudbank",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Carrier",
    combat_role="Cruiser combatant with embarked small craft",
    length=370,
    armor=38,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=185,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[
        weapons.RAILGUN,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[("Squall", 10)],
    short_description="Fast light carrier with stimmed fighter wing and stim-response point defense",
    long_description=(
        "The Cloudbank is a cruiser hull that trades armor and broadside batteries for a "
        "hangar bay carrying a full wing of ten Squall fighters. The Cloudbank fights "
        "with its own railgun while its wing provides aggressive screening -- Squalls "
        "chasing down enemy small craft, harrying frigates, and screening for the cruiser "
        "line. The Cloudbank's flight operations are faster than any other faction's light "
        "carrier: stimmed pilots launch and recover at accelerated speed, and the hangar "
        "crew on maintenance stims turn craft around in times that other factions' deck "
        "crews cannot match. The stim-response laser turrets provide close defense during "
        "launch and recovery. The ship carries significant stim reserves for both its own "
        "crew and its embarked pilots -- the Squall wing burns through combat compounds "
        "fast, and a wing that runs out of stims mid-engagement becomes dramatically less "
        "effective."
    ),
    exterior_appearance_description=(
        "A 370-meter military spacecraft with a pale grey hull. A wide, angular body with a "
        "flat-topped trapezoidal cross-section. A flight deck along the top. Launch bays cut "
        "into the sides, lit from within in amber. A railgun housing on the top spine forward "
        "of the flight deck. Two heavy laser arrays on the upper sides. Thin hull plating. "
        "Engine nacelles on heavy pylons at the midsection. Orange angular slashes along the "
        "sides and around the launch bay openings. A stylised flame emblem in orange and "
        "steel-blue on both sides. Steel-blue identification numbers on the sides and top."
    ),
    interior_appearance_description=(
        "The aft third is hangar space -- a brightly lit bay where ten Squalls sit in "
        "rapid-turnaround launch cradles. Stim resupply stations at each craft position "
        "let pilots top up injector packs between sorties. The hangar crew operates on "
        "maintenance stims during surge operations, keeping turnaround times short. A "
        "pilot ready room adjacent to the hangar includes acceleration couches and stim "
        "dosing stations. The flight operations center manages wing coordination -- less "
        "sophisticated than a Polaran neural relay but faster in raw human terms. The "
        "combat pharmacology department manages compounds for both the ship's crew and "
        "the embarked pilots. The crash ward handles both populations."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 20}, {"crew": 160}],
    secondary_crew=[
        {"ship_gunners": 18},
        {"embarked_craft_pilots": 10},
        {"wing_coordinators": 2},
        {"hangar_maintenance": 16},
        {"combat_pharmacologists": 2},
        {"medical": 8},
    ],
    additional_systems=[
        "Hangar bay (10 small craft)",
        "Craft maintenance and rapid rearm facilities",
        "Pilot stim resupply stations",
        "Combat pharmacology department",
        "Ship-wide stim distribution system",
        "Crash ward (20 bunks)",
        "Flight operations center",
    ],
)

HURRICANE = ShipTemplate(
    name="Hurricane",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=880,
    armor=75,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1100,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
        weapons.HEAVY_LASER_ARRAY,
    ],
    default_small_craft=[],
    short_description="Fast battleship with stimmed gunnery and aggressive closing doctrine",
    long_description=(
        "The Hurricane is the fastest battleship in known space -- Fast where the template "
        "is Moderate -- and it uses that speed to close with the enemy before they expect "
        "a capital engagement. The Hurricane's doctrine is pure Antaren: close fast, hit "
        "hard, overwhelm the target with stimmed gunnery that achieves hit rates no "
        "baseline crew can match, and win before the thin hull and depleted stim reserves "
        "become fatal liabilities. A Hurricane closing at Fast speed with its crew on peak "
        "combat stims is the most devastating short-duration combatant in known space. "
        "Its stimmed gunners fire faster and more accurately than any other battleship's "
        "crew. Its damage control teams work at chemically enhanced speed. Its bridge crew "
        "process tactical information faster than the enemy can generate it. For the first "
        "hours of an engagement, the Hurricane is almost unbeatable. After that, the stim "
        "reserves deplete, the crew begins to crash, the thin hull accumulates damage, "
        "and the Hurricane becomes the most expensive liability in the fleet. Antaren "
        "admirals know exactly how long they have. The clock starts when the stims hit."
    ),
    exterior_appearance_description=(
        "An 880-meter military spacecraft with a pale grey hull. A massive angular body with a "
        "faceted hexagonal cross-section. A gauss cannon housing along the top ridge. Weapon "
        "batteries in angular housings along both upper sides in two tiers. Point-defense "
        "turrets along the lower sides. Thin hull plating. Engine "
        "nacelles on massive pylons at the midsection and additional engine bells at the rear. "
        "Orange angular slashes in bold patterns across the entire hull. A stylised flame "
        "emblem in orange and steel-blue at large scale on both sides and on the front. "
        "Steel-blue fleet markings and ship name at large scale on the sides."
    ),
    interior_appearance_description=(
        "The combat pharmacology department is an industrial operation -- a full section "
        "of the ship dedicated to stim compounding, distribution, monitoring, and crash "
        "recovery. Four combat pharmacologists manage the chemistry of over a thousand "
        "crew, with a monitoring suite that displays the chemical state of every combat "
        "station in real time. The stim distribution system runs compound through "
        "dedicated lines to every gunnery station, bridge position, engineering watch, "
        "and damage control post. The crash ward is a full medical section -- fifty bunks "
        "with monitoring equipment, IV lines, and metabolic stabilizers. During a "
        "prolonged engagement, the crash ward fills with crew who have burned through "
        "their stim cycle, replaced at their stations by crew who dosed later. The "
        "bridge is a command amphitheater of acceleration couches. Crew quarters are "
        "functional but not generous -- the Hurricane's shortened deployment duration "
        "means it spends less time at sea than other factions' battleships."
    ),
    minimum_crew=[{"senior_officers": 14}, {"officers": 100}, {"crew": 1100}],
    secondary_crew=[
        {"gunners": 180},
        {"point_defense_crew": 100},
        {"combat_pharmacologists": 4},
        {"medical": 30},
        {"sensor_specialists": 30},
    ],
    additional_systems=[
        "Combat pharmacology department (industrial)",
        "Ship-wide stim distribution system",
        "Stim compounding facility (industrial)",
        "Crash ward (50 bunks)",
        "Crew chemical state monitoring suite",
        "High-refresh combat displays",
        "Stim-response weapon tracking system",
    ],
)

AVALANCHE = ShipTemplate(
    name="Avalanche",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1120,
    armor=38,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=900,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_PD,
        weapons.LASER_PD,
        weapons.LASER_PD,
    ],
    default_small_craft=[
        ("Thunderbolt", 10),
        ("Thunderbolt", 10),
        ("Zephyr", 10),
        ("Zephyr", 10),
    ],
    short_description="Fast carrier deploying aggressive strike wings with stim-enhanced pilots",
    long_description=(
        "The Avalanche is the Antaren fleet carrier -- faster than any other faction's "
        "equivalent, deploying four wings of small craft crewed by stimmed pilots who "
        "fight at the chemical edge of human performance. The standard wing composition "
        "is two wings of Thunderbolt bombers and two wings of Zephyr interceptors -- a "
        "pure offensive package with no defensive fighters. The Thunderbolts are faster "
        "bombers than any other faction fields, and the Zephyrs are the best interceptors "
        "in known space. Together they execute strike packages of terrifying speed and "
        "precision. The Avalanche's flight operations are the fastest afloat: stimmed "
        "deck crews launch and recover at accelerated rates, and stimmed pilots cycle "
        "through sorties faster than baseline humans can sustain. The limiting factor is "
        "stim reserves -- the Avalanche burns through combat compounds faster than any "
        "other capital ship, both for its own crew and for its forty embarked pilots. "
        "The carrier's pharmacology department manages compounds for both populations. "
        "Medium-jump capable, allowing it to project strike power through flanking routes."
    ),
    exterior_appearance_description=(
        "A 1120-meter military spacecraft with a pale grey hull. A long, angular arrowhead "
        "shape -- a sharp pointed front widening to broad, flat rear surfaces. Faceted hull "
        "surfaces meeting at hard angles. Hangar openings cut into the upper sides, lit from "
        "within in amber. Thin hull plating. Engine nacelles in forward-swept mounts at the "
        "midsection and additional engine bells across the rear. Orange angular slashes in "
        "aggressive patterns across the hull -- along the sides, across the front, radiating "
        "from the engine mounts. A stylised flame emblem in orange and steel-blue at large "
        "scale on both sides forward. Steel-blue identification numbers and wing designations "
        "stencilled beneath the hangars."
    ),
    interior_appearance_description=(
        "The four hangar bays dominate the ship -- vast, brightly lit spaces where forty "
        "strike craft sit in rapid-turnaround launch cradles. Stim resupply stations at "
        "every craft position. The deck crew operates on maintenance stims during surge "
        "operations, and the turnaround times are the fastest in any navy. The pilot "
        "ready rooms are adjacent to the hangars -- acceleration couches, stim dosing "
        "stations, and the bright, jittery atmosphere of people running at chemical "
        "speed. The flight operations center coordinates the wing -- stimmed controllers "
        "processing sortie data faster than automated systems. The pharmacology "
        "department is the largest on any Antaren vessel except the Hurricane -- managing "
        "compounds for over three thousand crew and forty pilots. The crash ward is a "
        "full section. Living spaces are extensive but utilitarian."
    ),
    minimum_crew=[{"senior_officers": 24}, {"officers": 165}, {"crew": 2400}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"wing_coordinators": 8},
        {"flight_deck_crew": 180},
        {"hangar_maintenance": 130},
        {"ship_gunners": 35},
        {"combat_pharmacologists": 4},
        {"medical": 40},
    ],
    additional_systems=[
        "Hangar bays (x4, 10 craft each)",
        "Craft maintenance and rapid rearm facilities",
        "Pilot stim resupply stations (40 positions)",
        "Combat pharmacology department (industrial)",
        "Ship-wide stim distribution system",
        "Stim compounding facility",
        "Crash ward (40 bunks)",
        "Flight operations center",
        "High-refresh combat displays",
    ],
)

MAELSTROM = ShipTemplate(
    name="Maelstrom",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=1700,
    armor=88,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1800,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=70,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Fast dreadnought with stimmed siege gunnery and reduced endurance",
    long_description=(
        "The Maelstrom is the largest and most powerful vessel in the Antaren fleet -- "
        "and it is faster than every other faction's dreadnought. Slow where the template "
        "is Very Slow, the Maelstrom can reposition during a battle in ways that other "
        "dreadnoughts cannot, bringing its twin siege cannons to bear on targets that "
        "expected to remain at extreme range. The siege cannon crews dose with a "
        "specialized focus stimulant that enhances the sustained concentration required "
        "for extreme-range fire -- the stimmed gunners achieve targeting solutions faster "
        "and maintain accuracy over longer firing cycles than baseline crews. The "
        "Maelstrom pays for this speed with the same weaknesses that define every Antaren "
        "ship: less armor and less hull integrity than any other dreadnought, and shorter "
        "supply duration. A Maelstrom that runs out of stim compounds becomes the most "
        "expensive conventional warship in the fleet -- still dangerous, but fighting at "
        "baseline human speed with a hull that cannot absorb the punishment its peers "
        "can. Only a handful exist. Each one is a strategic asset that the Antaren navy "
        "deploys carefully -- not out of caution, but because losing one wastes the stim "
        "infrastructure that makes it more than just a ship with two big guns."
    ),
    exterior_appearance_description=(
        "A 1700-meter military spacecraft with a pale grey hull. A massive, elongated angular "
        "shape with a faceted octagonal cross-section -- eight flat surfaces meeting at hard "
        "angles. Twin siege cannon housings run along the top two facets. Point-defense "
        "turrets in mounts along the side facets. Thin hull plating. "
        "Engine nacelles on massive pylons at the midsection and a large engine bell array "
        "across the rear. Orange angular slashes in bold patterns across the entire hull -- "
        "every facet marked. A stylised flame emblem in orange and steel-blue at massive scale "
        "on the two widest side facets. Steel-blue fleet markings and ship name at large "
        "scale."
    ),
    interior_appearance_description=(
        "The Maelstrom is a city built around two siege cannons. The gun crews work in "
        "dedicated fire control sections with direct stim feed lines from the pharmacology "
        "department, running specialized focus compounds that keep them locked on "
        "targeting solutions for hours at a stretch. The pharmacology department is the "
        "largest in the Antaren fleet -- an industrial facility managing the chemistry of "
        "thousands of crew, with compounding labs, storage vaults of concentrated stim "
        "precursors, and a monitoring suite that tracks the chemical state of every "
        "section of the ship. The crash ward is an entire medical deck. The bridge is "
        "a vast command amphitheater. Crew quarters, mess halls, and recreation spaces "
        "fill the living sections -- more generous than smaller Antaren vessels because "
        "even Antaren admirals accept that a dreadnought crew needs functional rest "
        "between stim cycles. The ship has the wired, electric atmosphere of something "
        "enormous running slightly too fast."
    ),
    minimum_crew=[{"senior_officers": 50}, {"officers": 340}, {"crew": 4800}],
    secondary_crew=[
        {"gunners": 280},
        {"point_defense_crew": 60},
        {"fleet_coordination_staff": 50},
        {"combat_pharmacologists": 6},
        {"medical": 100},
    ],
    additional_systems=[
        "Combat pharmacology department (industrial, fleet-scale)",
        "Ship-wide stim distribution system",
        "Stim compounding facility (industrial)",
        "Siege crew dedicated stim feeds",
        "Crash ward (medical deck -- 80+ bunks)",
        "Crew chemical state monitoring suite (all sections)",
        "Twin spinal siege cannon mounts",
        "Fleet-wide stim state coordination",
    ],
)

TRADEWIND = ShipTemplate(
    name="Tradewind",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Fleet Tender",
    combat_role="Resupply / ammunition, fuel, and stim compound transport",
    length=320,
    armor=20,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=90,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Fast fleet tender carrying ammunition, fuel, and stim compounds",
    long_description=(
        "The Tradewind is the Antaren logistics backbone -- and the most important ship "
        "in the fleet that nobody wants to think about. It carries fuel, ammunition, "
        "spare parts, and stim compounds. The stim compounds are the critical cargo. An "
        "Antaren fleet without Tradewind resupply burns through its stim reserves in "
        "days, and a fleet without stims is a fleet fighting at baseline human "
        "performance -- which, for a navy built around chemical enhancement, is a "
        "catastrophic reduction in capability. The Tradewind carries compounds in "
        "temperature-controlled storage, precursor chemicals for field compounding, and "
        "the metabolic stabilizers and crash recovery medications that every ship in the "
        "fleet consumes. Destroying an Antaren fleet's Tradewinds does not starve it "
        "of ammunition -- it starves it of the chemistry that makes it fight above "
        "baseline. Faster than other factions' fleet tenders, keeping up with the "
        "faster Antaren battle fleet."
    ),
    exterior_appearance_description=(
        "A 320-meter military spacecraft with a pale grey hull. A bulky, angular body with a "
        "rectangular cross-section and hard-angled edges. The midsection is a wide cargo and "
        "supply module with docking clamps and transfer booms along both sides. An ion turret "
        "on top. A point-defense mount at the rear. Thin hull plating. Engine nacelles on "
        "pylons at the midsection. Orange trim along the hull edges and around the docking "
        "clamps. Steel-blue identification numbers on the sides and top."
    ),
    interior_appearance_description=(
        "The interior is mostly cargo space -- modular containers of ammunition, fuel "
        "cells, spare parts, and the temperature-controlled pharmaceutical storage that "
        "holds stim compounds, precursor chemicals, and metabolic stabilizers. The "
        "pharmaceutical storage is climate-controlled and segregated from other cargo -- "
        "stim compounds degrade at elevated temperatures. A small compounding lab can "
        "produce basic stim blends from precursors in the field. Crew spaces forward "
        "are functional. The Tradewind carries its own basic dispensary for the crew, "
        "but its primary purpose is fleet resupply, not its own consumption."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 55}],
    secondary_crew=[
        {"cargo_handlers": 20},
        {"pharmaceutical_logistics": 8},
    ],
    additional_systems=[
        "Modular cargo system",
        "Pharmaceutical storage (temperature-controlled)",
        "Field compounding lab",
        "Stim dispensary (basic, crew use)",
        "Crash recovery supplies",
    ],
)

JETSTREAM = ShipTemplate(
    name="Jetstream",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Supply Runner",
    combat_role="Fast resupply through medium jump points",
    length=105,
    armor=10,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=35,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=14,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Extremely fast medium-jump supply runner carrying critical stim compounds",
    long_description=(
        "The Jetstream is the fastest supply vessel in known space -- Very Fast where "
        "the template is Fast -- and it carries the most time-critical cargo in the "
        "Antaren fleet: fresh stim compounds. Stim compounds degrade. Stim compounds "
        "are consumed at rates that surprise outsiders. A forward-deployed Antaren task "
        "force burns through its chemical reserves faster than its ammunition, and the "
        "Jetstream is what keeps them fighting at chemical speed rather than baseline. "
        "The Jetstream uses medium jump points to reach forward positions that fleet "
        "tenders cannot, delivering its pharmaceutical cargo at the speed the Antaren "
        "fleet demands. Lightly armed and fragile -- the Jetstream runs, not fights. "
        "Losing a Jetstream is not a combat loss. It is a chemical supply crisis."
    ),
    exterior_appearance_description=(
        "A 105-meter military spacecraft with a pale grey hull. A long, narrow angular body "
        "with a faceted diamond cross-section. A slim crew module at the front with a glazed "
        "canopy. The majority of the hull is cargo space with loading hatches along the sides. "
        "An ion turret on top. Oversized engine nacelles on swept pylons -- the ship is built "
        "for speed. Thin hull plating. Orange trim along the hull edges and around the loading "
        "hatches. Steel-blue identification numbers on the sides."
    ),
    interior_appearance_description=(
        "The interior is engine, jump drive, and cargo. The cargo hold is "
        "temperature-controlled for pharmaceutical storage, with secured racks for stim "
        "compound containers. Crew spaces are minimal -- a bridge, bunks for the skeleton "
        "crew, and a galley. The Jetstream's crew run on maintenance stims during "
        "transit -- the irony of a supply ship dependent on the same supplies it carries "
        "is not lost on anyone."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[{"pharmaceutical_logistics": 2}],
    additional_systems=[
        "Pharmaceutical storage (temperature-controlled)",
        "Stim dispensary (basic, crew use)",
    ],
)

DELUGE = ShipTemplate(
    name="Deluge",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=610,
    armor=65,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=750,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Fast assault transport deploying stim-enhanced ground forces",
    long_description=(
        "The Deluge delivers an Antaren ground force into hostile space -- and that "
        "ground force arrives stimmed and wired and moving faster than the defenders "
        "expect infantry to move. Antaren marines dose before deployment with a combat "
        "cocktail optimized for ground assault: fast-twitch reflexes, pain suppression, "
        "and a metabolic accelerant that keeps them fighting at a tempo that overwhelms "
        "baseline defenders. The Deluge itself is faster than the template assault "
        "transport, reaching the deployment zone quicker and spending less time in the "
        "vulnerable approach phase. The ship carries extensive stim reserves for the "
        "embarked force -- enough to sustain enhanced combat performance for the initial "
        "assault phase, after which the ground force must either have achieved its "
        "objectives or transition to baseline operations. The Deluge's weakness is "
        "duration: an Antaren assault force that has not won within days is an assault "
        "force that begins to crash, and a crashing army is a vulnerable army."
    ),
    exterior_appearance_description=(
        "A 610-meter military spacecraft with a pale grey hull. A heavy, angular body with a "
        "hexagonal cross-section and a blunt, armoured front. A particle cannon housing on "
        "top. The midsection is a massive troop and vehicle bay with loading ramps on the "
        "underside and rear. Point-defense turrets spaced along the sides and top. Thicker "
        "hull plating than standard Antarian construction. Engine nacelles on heavy pylons at "
        "the midsection. Orange angular slashes across the front and along the sides. A "
        "stylised flame emblem in orange and steel-blue on both sides. Steel-blue fleet "
        "markings and ship name on the sides."
    ),
    interior_appearance_description=(
        "The troop decks are vast compartments with bunks and pre-deployment stim dosing "
        "stations -- marines dose in their staging areas, the compounds taking effect "
        "during the final approach so the force deploys at peak chemical performance. "
        "The ship's pharmacology department manages stim logistics for thousands of "
        "marines -- a major operation requiring dedicated pharmaceutical staff. Vehicle "
        "bays on the lower decks carry armored transports and heavy weapons. The "
        "deployment bays are designed for rapid disembarkation at stimmed speed -- faster "
        "than other factions' assault ships can empty. The ship has the tense, charged "
        "atmosphere of several thousand people about to dose and go to war."
    ),
    minimum_crew=[{"officers": 14}, {"crew": 90}],
    secondary_crew=[
        {"marine_officers": 50},
        {"marines": 4000},
        {"vehicle_crew": 200},
        {"combat_pharmacologists": 4},
        {"medical": 30},
        {"ship_gunners": 18},
    ],
    additional_systems=[
        "Troop stim dosing stations",
        "Combat pharmacology department (ground force scale)",
        "Marine stim compound storage",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Rapid disembarkation system",
        "Crash ward (40 bunks -- post-deployment recovery)",
    ],
)

CORONA = ShipTemplate(
    name="Corona",
    faction=ShipFaction.ANTARES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Comms Ship",
    combat_role="Fleet communications relay",
    length=175,
    armor=15,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=55,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fast fleet communications relay with stim-enhanced signals processing",
    long_description=(
        "The Corona extends Antaren fleet communications beyond the range of fixed relay "
        "stations. Its communications operators dose with perceptual stimulants that "
        "accelerate signal processing, allowing them to manage the jittery, overlapping, "
        "fast-paced communications traffic that characterizes an Antaren fleet in combat. "
        "Antaren fleet communications are notoriously difficult for outsiders to follow "
        "-- stimmed operators transmit and receive at a pace that sounds like noise to "
        "baseline humans. The Corona's stimmed signals team keeps this torrent organized "
        "and routed. The Corona is also one of the fleet's most vulnerable ships -- light "
        "hull, no serious armament, and the communications arrays make it a visible "
        "priority target. Destroying the Coronas forces the Antaren fleet to communicate "
        "at baseline speed, which for a fleet built on chemical reaction time is a "
        "significant degradation."
    ),
    exterior_appearance_description=(
        "A 175-meter military spacecraft with a pale grey hull. An angular body with a "
        "pentagonal cross-section. A communications array on top -- antenna masts and relay "
        "dishes in angular housings. An ion turret on top forward of the array. Thin hull "
        "plating. Engine nacelles on pylons at the midsection. Orange trim along the hull "
        "edges and at the base of the antenna array. Steel-blue identification numbers on the "
        "sides."
    ),
    interior_appearance_description=(
        "The communications center is the heart of the ship -- a room of operator "
        "stations where the signals team works on perceptual stims, processing the fast "
        "Antaren combat communications traffic. The operators describe stimmed signals "
        "work as hearing the fleet think -- each ship's communications becoming a voice "
        "in a conversation happening at chemical speed. The pharmacology bay stocks "
        "the perceptual compounds the signals team uses. The crash ward handles the "
        "post-engagement crash. Crew spaces are modest. The Corona's crew know they "
        "are a priority target and carry themselves accordingly."
    ),
    minimum_crew=[{"officers": 4}, {"crew": 20}],
    secondary_crew=[
        {"communications_specialists": 10},
        {"combat_pharmacologist": 1},
    ],
    additional_systems=[
        "Fleet communications relay array",
        "Encrypted high-bandwidth communications suite",
        "Combat pharmacology bay (perceptual compounds)",
        "Crash ward (6 bunks)",
        "High-refresh signals processing displays",
    ],
)

ANTARES_SMALL_CRAFT = {
    "Wisp": WISP,
    "Thunderbolt": THUNDERBOLT,
    "Zephyr": ZEPHYR,
    "Squall": SQUALL,
    "Flurry": FLURRY,
}

ANTARES_CORVETTES = {
    "Gale": GALE,
    "Updraft": UPDRAFT,
    "Nimbus": NIMBUS,
}

ANTARES_FRIGATES = {
    "Tempest": TEMPEST,
    "Mirage": MIRAGE,
    "Crosswind": CROSSWIND,
}

ANTARES_DESTROYERS = {
    "Hailstorm": HAILSTORM,
    "Cyclone": CYCLONE,
    "Aurora": AURORA,
}

ANTARES_CRUISERS = {
    "Typhoon": TYPHOON,
    "Sirocco": SIROCCO,
    "Monsoon": MONSOON,
    "Cloudbank": CLOUDBANK,
}

ANTARES_CAPITALS = {
    "Hurricane": HURRICANE,
    "Avalanche": AVALANCHE,
    "Maelstrom": MAELSTROM,
}

ANTARES_SUPPORT = {
    "Tradewind": TRADEWIND,
    "Jetstream": JETSTREAM,
    "Deluge": DELUGE,
    "Corona": CORONA,
}

ANTARES_ALL_SHIPS = {
    **ANTARES_SMALL_CRAFT,
    **ANTARES_CORVETTES,
    **ANTARES_FRIGATES,
    **ANTARES_DESTROYERS,
    **ANTARES_CRUISERS,
    **ANTARES_CAPITALS,
    **ANTARES_SUPPORT,
}