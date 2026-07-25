from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


ZOOG = ShipTemplate(
    name="Zoog",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Scout",
    combat_role="Reconnaissance / forward sensor platform",
    length=9,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=2,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Stripped-down scout with modified pilot in unlit cockpit",
    long_description=(
        "The Zoog is the smallest craft in the Pleiadian fleet -- and smaller than any "
        "other faction's scout because it doesn't carry the systems that other factions "
        "consider essential. No cockpit lighting. No atmospheric processing. No thermal "
        "regulation. No cockpit pressurization beyond the thin, chemical-heavy atmosphere "
        "that Pleiadian pilots breathe natively. The pilot sits in darkness that would "
        "be total for a baseline human, reading instruments through infrared-sensitive "
        "eyes that see the electromagnetic spectrum in ways baseline vision cannot. The "
        "Zoog's sensor profile is lower than any other scout because it radiates less -- "
        "no heat from life support, no light from displays, no EM emissions from systems "
        "that don't exist. It is a tiny, dark, cold thing that watches from the void."
    ),
    exterior_appearance_description=(
        "A 9-meter single-seat military spacecraft with a dark, matte hull. A tiny, curved "
        "body shaped like a flattened seed -- a smooth, continuous organic curve with no flat "
        "surfaces. The hull has a faint green discolouration and a chitinous texture from "
        "biological hull coatings. No glazed canopy -- the hull is an unbroken carapace. A "
        "light laser integrated into the front, visible only as a slight ridge in the shell. "
        "Engine bells recessed into the tapered rear beneath overlapping hull material. No "
        "external lights. Faint green bioluminescent traces in branching patterns along the "
        "hull seams. Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "A single seat in total darkness. No instrument lighting -- the pilot's modified "
        "eyes read infrared emissions from the instrument panels directly. The cockpit "
        "atmosphere is thin and cold, carrying the chemical compounds that modified "
        "Pleiadian lungs process but baseline lungs cannot. The only sound is the pilot's "
        "breathing and the hum of the engine. A baseline human sealed in a Zoog cockpit "
        "would suffocate in darkness."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Infrared instrument displays", "Minimal atmosphere (Pleiadian standard)"],
)

BYAKHEE = ShipTemplate(
    name="Byakhee",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=16,
    armor=2,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=7,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=2,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Fast, lightweight bomber with modified crew tolerance for high-G approach",
    long_description=(
        "The Byakhee carries a single antimatter torpedo through enemy point defense -- "
        "faster than the template bomber because the stripped-down construction saves "
        "mass, and the modified crew tolerates G-forces that would incapacitate baseline "
        "pilots. A Byakhee pilot's modified cardiovascular system maintains consciousness "
        "through sustained acceleration that would grey out a baseline human, allowing "
        "the bomber to execute approach manoeuvres at speeds that other factions' bombers "
        "cannot match. The cockpit has no ejection system -- Pleiadian engineering budgets "
        "do not spend mass on systems the crew considers unnecessary. The pilot with "
        "thickened bone density and restructured organs is the survival system."
    ),
    exterior_appearance_description=(
        "A 16-meter two-seat military spacecraft with a dark, matte hull. A wide, curved body "
        "shaped like a flattened oval -- a broad carapace with a humped upper surface curving "
        "down to a narrow underside. The hull has a faint green discolouration and a chitinous "
        "texture. No glazed canopy. The torpedo housing is integrated into the underside, "
        "visible as a smooth bulge in the shell rather than an obvious mount. Engine bells "
        "recessed into the tapered rear beneath overlapping hull material. No external lights. "
        "Faint green bioluminescent traces in branching patterns along the hull seams. Violet "
        "strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Two stations in tandem in darkness -- pilot forward, weapons officer behind. "
        "No instrument lighting. No thermal regulation. The cockpit atmosphere is thin "
        "and cold. The crew breathe easily in conditions that would leave a baseline "
        "human unconscious in minutes. The torpedo arming display is the only system "
        "that emits in a spectrum baseline eyes could detect, and it is calibrated for "
        "infrared perception."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Infrared instrument displays", "Minimal atmosphere (Pleiadian standard)"],
)

NIGHTGAUNT = ShipTemplate(
    name="Nightgaunt",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Interceptor",
    combat_role="Fast attack / anti-scout / anti-bomber",
    length=8,
    armor=0,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=2,
    default_weapons=[weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Silent interceptor with modified pilot in dark, cold cockpit",
    long_description=(
        "The Nightgaunt is the Pleiadian interceptor -- the smallest, lightest interceptor "
        "in known space. It carries no systems that the modified pilot doesn't need, and "
        "the modified pilot doesn't need much. No cockpit lighting. No heating. No "
        "pressurization beyond Pleiadian standard thin atmosphere. The mass saved by "
        "stripping these systems is distributed to the engine and the weapon. The "
        "Nightgaunt's pilot sees in infrared, reads instruments through modified eyes, "
        "and tracks targets through perceptions that baseline humans do not have -- some "
        "Pleiadian interceptor pilots have modified visual cortices that process motion "
        "faster than baseline neurology, giving them a reaction-time advantage that "
        "doesn't come from chemicals or electronics but from rewired biology. The "
        "Nightgaunt arrives in silence and darkness. Its targets see it on instruments "
        "but not through windows. It has no running lights."
    ),
    exterior_appearance_description=(
        "An 8-meter single-seat military spacecraft with a dark, matte hull. A tiny, narrow "
        "body shaped like an elongated thorn -- a thin, curved profile tapering to a point at "
        "both ends. The hull has a faint green discolouration and a chitinous texture. No "
        "glazed canopy. A heavy laser turret integrated into the upper surface, visible as a "
        "smooth dome flush with the carapace. Engine bells recessed into the rear point. No "
        "external lights. Faint green bioluminescent traces along the hull seams. Violet "
        "strain insignia visible only at close range."
    ),
    interior_appearance_description=(
        "The pilot lies nearly prone in a contoured acceleration couch in total darkness. "
        "No instrument lighting -- the pilot's modified eyes read the panels directly. "
        "The cockpit is near-freezing. The thin atmosphere carries compounds that smell "
        "faintly sweet to the modified pilot and would smell like nothing to a baseline "
        "human because the baseline human would already be unconscious."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Infrared instrument displays", "Minimal atmosphere (Pleiadian standard)"],
)

VOORMI = ShipTemplate(
    name="Voormi",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Fighter",
    combat_role="Escort / area control / anti-small-craft",
    length=13,
    armor=4,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=12,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=2,
    default_weapons=[weapons.PLASMA_LAUNCHER],
    default_small_craft=[],
    short_description="Fast, lightweight fighter with modified pilot and stripped-down systems",
    long_description=(
        "The Voormi is the Pleiadian general-purpose fighter -- faster than the template, "
        "lighter, and crewed by a pilot whose biological modifications make the stripped-"
        "down cockpit environment irrelevant. Voormi fly in wings, and the modified "
        "pilots coordinate through communications that exploit Pleiadian perceptual "
        "modifications -- transmissions compressed into frequency ranges that baseline "
        "communications equipment doesn't monitor, at speeds that baseline cognition "
        "cannot follow. An intercepted Pleiadian wing communication sounds like static. "
        "It is not static. The Voormi's speed advantage comes from mass savings -- every "
        "system that the modified pilot doesn't need is absent, and the weight goes to "
        "the engine instead. In hostile environments -- radiation zones, nebulae, near "
        "stellar bodies -- the Voormi fights at full effectiveness while other factions' "
        "fighters suffer degraded crew performance."
    ),
    exterior_appearance_description=(
        "A 13-meter single-seat military spacecraft with a dark, matte hull. A compact, curved "
        "body shaped like an elongated seed pod -- no flat surfaces, no sharp edges, the hull "
        "a continuous organic curve tapering to a point at the rear. The surface has a faint "
        "green discolouration and a chitinous texture from biological hull coatings. No glazed "
        "canopy -- the hull is an unbroken carapace. A plasma launcher integrated into the "
        "underside, barely visible as a slight bulge in the hull surface. Engine bells "
        "recessed into the tapered rear, nearly hidden beneath overlapping hull material. No "
        "external lights. Faint green bioluminescent traces in branching patterns along the "
        "hull seams. Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "A single-seat cockpit in darkness. The pilot's modified eyes read infrared "
        "instrument displays. The atmosphere is thin and cold. The controls are lighter "
        "than standard -- designed for modified hands that may not have the same geometry "
        "as baseline hands. Some Pleiadian fighter pilots have restructured grip "
        "geometry optimized for their specific control interface. The cockpit is smaller "
        "than other factions' fighters because the modified pilot is often smaller -- "
        "restructured for the environment, not for baseline proportions."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=[
        "Infrared instrument displays",
        "Minimal atmosphere (Pleiadian standard)",
        "Modified-geometry flight controls",
    ],
)

GUG = ShipTemplate(
    name="Gug",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=18,
    armor=7,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=20,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=2,
    default_weapons=[weapons.HEAVY_PLASMA_CANNON],
    default_small_craft=[],
    short_description="Fast gunship with modified crew operating in dark, cold conditions",
    long_description=(
        "The Gug is the Pleiadian gunship -- faster than the template, lighter, crewed "
        "by four modified operators in conditions that would incapacitate a baseline "
        "crew within minutes. The cockpit is dark, near-freezing, and filled with thin "
        "atmosphere that baseline lungs cannot process. The Gug's crew works in these "
        "conditions without discomfort because their biology has been restructured to "
        "treat them as normal. The engineer's modified hands -- restructured grip, "
        "thickened skin, enhanced tactile sensitivity in non-standard frequency ranges -- "
        "manage the plasma cannon's power systems by touch in darkness. A baseline "
        "engineer would need lights, gloves, and thermal regulation to do the same work. "
        "The Gug's mass savings from stripped life support go to the engine. In hostile "
        "environments -- the radiation-soaked, nebula-choked systems that Pleiadian space "
        "is full of -- the Gug fights at full effectiveness while other factions' gunships "
        "struggle with degraded crew performance."
    ),
    exterior_appearance_description=(
        "An 18-meter multi-crew military spacecraft with a dark, matte hull. A broad, curved "
        "body shaped like a horseshoe crab shell -- a wide, humped upper carapace with a flat "
        "underside and a tapered rear. The hull has a faint green discolouration and a "
        "chitinous, layered texture. No glazed canopy. A heavy plasma cannon integrated into "
        "the underside, visible as a long, ridged protrusion beneath the shell. Engine bells "
        "recessed into the tapered rear beneath overlapping hull material. No external lights. "
        "Faint green bioluminescent traces in branching patterns along the hull seams. Violet "
        "strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Four stations in a cabin that is dark, cold, and filled with thin atmosphere. "
        "No instrument lighting visible to baseline eyes. The crew see in infrared -- "
        "to them, the cabin is lit by the thermal signatures of the instruments, the "
        "engine's heat bleed, and each other's body heat. To a baseline human, it would "
        "be a freezing dark box with no visible controls and air that tastes wrong. The "
        "crew work by touch and infrared sight, their modified hands on controls shaped "
        "for modified grip geometry."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}],
    secondary_crew=[{"engineer": 1}, {"sensor_operator": 1}],
    additional_systems=[
        "Infrared instrument displays",
        "Minimal atmosphere (Pleiadian standard)",
        "Modified-geometry controls (all stations)",
    ],
)

ULTHAR = ShipTemplate(
    name="Ulthar",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=48,
    armor=17,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=65,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast, stripped-down patrol corvette with extended endurance",
    long_description=(
        "The Ulthar is the standard Pleiadian patrol vessel -- the most commonly "
        "encountered ship in their fleet and the first thing outsiders see when entering "
        "Pleiadian space. It is smaller, faster, and lighter than the template patrol "
        "corvette, with a sensor profile so low it reads as insignificant -- a corvette "
        "that hides like a scout. The mass savings from stripped environmental systems "
        "are distributed across the engine and supply stores, giving the Ulthar both "
        "higher speed and longer endurance than any other faction's patrol corvette. A "
        "modified crew that needs less food, less air processing, and less heating stays "
        "on station longer. The Ulthar patrols Pleiadian systems for weeks on supplies "
        "that would sustain a baseline crew for days. Outsiders encountering an Ulthar "
        "find the experience unsettling -- the ship responds to hails but shows no running "
        "lights, no visible crew, no emissions that suggest habitation. It appears "
        "abandoned. It is not."
    ),
    exterior_appearance_description=(
        "A 48-meter military spacecraft with a dark, matte hull. A long, curved body shaped "
        "like an elongated mussel shell -- a humped upper carapace narrowing to a keel line "
        "along the underside, tapering at both ends. The hull has a faint green discolouration "
        "and a chitinous, layered texture from biological hull coatings -- overlapping organic "
        "plates. No visible windows or bridge structure. A particle cannon integrated into the "
        "top ridge, visible as a long raised seam in the carapace. A heavy laser turret "
        "recessed into the upper surface, visible as a smooth dome flush with the shell. "
        "Engine bells recessed into the tapered rear beneath overlapping hull material. No "
        "external lights. Faint green bioluminescent traces in branching patterns along the "
        "hull seams, concentrated where the carapace plates overlap. Violet strain insignia on "
        "the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Dark corridors near freezing. The crew navigates by infrared sight through "
        "passages that a baseline human would experience as a pitch-black frozen maze "
        "of unbreathable air. The bridge is a ring of stations visible to the crew as "
        "glowing infrared displays and to a baseline human as nothing. Crew quarters "
        "are small pods -- the modified crew sleeps in cold that would be hypothermic for "
        "baseline humans, breathing thin atmosphere that would suffocate them. The galley "
        "stores are unrecognizable compounds that the modified digestive systems process "
        "as nutrition. The ship is quiet. The modified crew communicates in low tones "
        "and frequencies that carry differently in the thin atmosphere."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[{"gunners": 2}],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation (ambient cold)",
        "No standard lighting",
        "Infrared instrument displays",
        "Modified-geometry controls (all stations)",
        "Low-emission hull design",
    ],
)

CELEPHAIS = ShipTemplate(
    name="Celephais",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=44,
    armor=9,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=45,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Voormi", 5)],
    short_description="Fast tender carrying five Voormi fighters with extended endurance",
    long_description=(
        "The Celephais carries and supports a detachment of Pleiadian small craft -- "
        "typically five Voormi fighters -- extending their operational range. The hangar "
        "is unlit and unheated, which for other factions' tenders would be a maintenance "
        "problem -- condensation, thermal cycling, lubricant viscosity in cold conditions. "
        "For the Celephais, it is the standard environment. The embarked craft are "
        "designed for these conditions. The hangar crew works in darkness by infrared "
        "sight with modified hands that maintain dexterity at temperatures that would "
        "numb baseline fingers to uselessness. Turnaround times are comparable to other "
        "factions' tenders despite the extreme conditions because the conditions are "
        "not extreme for the crew. The Celephais's extended supply duration means it "
        "can keep its wing operational longer than other factions' tenders."
    ),
    exterior_appearance_description=(
        "A 44-meter military spacecraft with a dark, matte hull. A wide, curved body shaped "
        "like a broad beetle carapace -- a humped upper surface with a flat underside. Launch "
        "cradles for fighters visible along both sides as dark recesses in the hull, no "
        "interior lighting visible. The hull has a faint green discolouration and a chitinous "
        "texture. No visible windows. A light ion turret recessed into the upper surface as a "
        "smooth dome. Engine bells recessed into the rear beneath overlapping hull material. "
        "No external lights. Faint green bioluminescent traces in branching patterns along the "
        "hull seams. Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The hangar is a cold, dark space where five Voormi sit in launch cradles. The "
        "hangar crew works by infrared, their modified eyes seeing the craft as thermal "
        "silhouettes against the near-freezing bay. The crew section forward is the "
        "standard Pleiadian environment -- dark, cold, thin atmosphere. Living spaces "
        "are minimal. The galley stores compounds that would be unrecognizable as food "
        "to a baseline human."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 5}],
    secondary_crew=[
        {"embarked_craft_pilots": 5},
        {"hangar_crew": 2},
    ],
    additional_systems=[
        "Hangar bay (5 small craft)",
        "Craft maintenance facilities",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared instrument displays",
    ],
)

KADATH = ShipTemplate(
    name="Kadath",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Survey Corvette",
    combat_role="Hazardous environment operations / exploration",
    length=42,
    armor=17,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=45,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=42,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Fast survey corvette with modified crew tolerating extreme environments",
    long_description=(
        "The Kadath is the Pleiadian survey corvette -- and where it truly excels is in "
        "environments that other factions' survey ships cannot safely enter. Radiation "
        "zones, extreme thermal environments, nebular interference, stellar proximity -- "
        "the conditions that force other factions to make fast passes or accept degraded "
        "sensor data are the conditions the Kadath was built for. Its modified crew "
        "tolerates radiation levels that would require heavy shielding on other ships. "
        "Its sensor operators see in spectra that baseline eyes cannot perceive. Its "
        "engineers work in temperatures that would incapacitate baseline humans. The "
        "Kadath enters hazardous environments and stays -- conducting thorough, extended "
        "surveys where other factions conduct fast passes. Its supply duration is "
        "significantly above template because the modified crew consumes less of "
        "everything. A Kadath can survey a radiation zone for weeks while other factions' "
        "survey ships measure their exposure in hours."
    ),
    exterior_appearance_description=(
        "A 42-meter military spacecraft with a dark, matte hull. A compact, curved body shaped "
        "like a rounded carapace -- a smooth, humped upper surface curving down on all sides. "
        "The hull has a faint green discolouration and a chitinous texture. No visible "
        "windows. Minimal sensor equipment visible -- a slight thickening of the hull at the "
        "front. A light ion turret recessed into the upper surface as a smooth dome. Engine "
        "bells recessed into the rear beneath overlapping hull material. No external lights. "
        "Faint green bioluminescent traces along the hull seams. Violet strain insignia on the "
        "sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The sensor section is a cluster of stations where modified operators work in "
        "conditions that would require a hazmat suit for baseline humans. Radiation "
        "levels aboard during a hot survey would trigger evacuation alarms on other "
        "ships. The Pleiadian crew's restructured cellular biology tolerates the "
        "exposure. The analysis room is dark and cold and the crew processes data "
        "through infrared displays. Living spaces are spartan even by Pleiadian "
        "standards -- the Kadath is a small ship on long deployments."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 5}],
    secondary_crew=[{"survey_specialists": 2}],
    additional_systems=[
        "Extended passive sensor array",
        "Hazardous environment survey suite",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared instrument displays",
        "Reduced radiation shielding (crew tolerant)",
    ],
)

BOKRUG = ShipTemplate(
    name="Bokrug",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Patrol Frigate",
    combat_role="Commerce protection / independent operations",
    length=130,
    armor=14,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=75,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=49,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast, long-endurance patrol frigate with modified crew",
    long_description=(
        "The Bokrug is the Pleiadian independent patrol vessel -- faster and longer-"
        "ranged than any other faction's patrol frigate. Its modified crew stays on "
        "station for weeks beyond what baseline crews can sustain, consuming less food, "
        "less air, and less power because the ship doesn't heat or light itself. The "
        "Bokrug patrols Pleiadian systems in silence and darkness, and contacts that "
        "enter its patrol zone are often unaware of its presence until it hails them. "
        "The hail comes from a ship with no running lights, no visible crew, and a "
        "sensor profile that suggests something much smaller. Outsiders find the "
        "experience deeply unnerving. The Bokrug's captain is the highest Pleiadian "
        "military authority in a system, and the ship is built to keep that authority "
        "present longer than anyone expects."
    ),
    exterior_appearance_description=(
        "A 130-meter military spacecraft with a dark, matte hull. A long, curved body shaped "
        "like an elongated carapace -- a humped upper surface curving down to a narrower "
        "underside, tapering at both ends. The hull has a faint green discolouration and a "
        "chitinous, layered texture from biological hull coatings -- overlapping organic "
        "plates. No visible windows or bridge structure. A particle cannon integrated into the "
        "top ridge as a long raised seam. A torpedo bay integrated into the lower front, "
        "visible as a seam in the shell that opens for firing. A heavy laser turret recessed "
        "into the upper surface as a smooth dome. Engine bells recessed into the tapered rear "
        "beneath overlapping hull material. No external lights. Faint green bioluminescent "
        "traces in branching patterns across the hull surface, concentrated along the seams "
        "where the carapace plates overlap. Violet strain insignia on the sides, visible only "
        "at close range."
    ),
    interior_appearance_description=(
        "Dark corridors in near-freezing thin atmosphere. The bridge is a circle of "
        "infrared-emitting stations visible to the modified crew and invisible to "
        "baseline eyes. Crew quarters are small cold pods. The wardroom, such as it is, "
        "stores compounds that the modified crew's restructured digestive systems process "
        "as nutrition. The ship could sustain its crew for months on stores that would "
        "last a baseline crew weeks. Living aboard a Bokrug on extended patrol is "
        "comfortable for the modified crew and would be a survival situation for anyone "
        "else."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 22}],
    secondary_crew=[
        {"gunners": 5},
        {"torpedo_crew": 3},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared instrument displays",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

COMMORIOM = ShipTemplate(
    name="Commoriom",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=135,
    armor=5,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=60,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Hard-jump scout frigate with minimal emissions and extended endurance",
    long_description=(
        "The Commoriom is the Pleiadian scout frigate -- a hard-jump-capable vessel "
        "that is nearly invisible. Its sensor profile is insignificant for a frigate -- "
        "achieved not through stealth technology but through the absence of emissions "
        "that other factions' ships cannot avoid. No thermal emissions from heating. No "
        "EM from lighting systems. No atmospheric processing signatures. The ship "
        "radiates almost nothing because it runs almost nothing. The modified crew "
        "doesn't need what the ship doesn't carry. The Commoriom enters enemy systems "
        "through hard jump points and conducts extended intelligence operations, staying "
        "on station longer than any other faction's scout frigate because its modified "
        "crew consumes less of everything. Its sensor operators see in spectra that "
        "baseline sensors don't monitor, and the intelligence they gather includes "
        "environmental data that other factions' scouts cannot perceive."
    ),
    exterior_appearance_description=(
        "A 135-meter military spacecraft with a dark, matte hull. A long, narrow body shaped "
        "like a thin shell -- a smooth, curved upper surface over a flat underside, tapering "
        "at both ends. The hull has a faint green discolouration and a chitinous texture. No "
        "visible windows. An ion cannon integrated into the top ridge as a raised seam. Engine "
        "bells recessed into the tapered rear. No external lights. Faint green bioluminescent "
        "traces along the hull seams. Violet strain insignia on the sides, visible only at "
        "close range."
    ),
    interior_appearance_description=(
        "The forward section is sensor equipment and an analysis room where modified "
        "intelligence specialists work in darkness by infrared sight. The hard-jump "
        "drive occupies the aft section. Living spaces in the middle are minimal -- small "
        "cold pods for the crew, stores of unrecognizable nutrition compounds, and the "
        "thin cold atmosphere that is the only environment the modified crew needs. The "
        "Commoriom on a deep intelligence mission is a ship of ghosts -- dark, cold, "
        "silent, crewed by people who are comfortable in conditions that would be a "
        "survival emergency for anyone else."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 12}],
    secondary_crew=[
        {"intelligence_analysts": 4},
        {"sensor_specialists": 3},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array (flush-mounted)",
        "Intelligence analysis suite",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

EIBON = ShipTemplate(
    name="Eibon",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=115,
    armor=14,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=75,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.PLASMA_CANNON, weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Fast escort frigate with extended endurance for convoy protection",
    long_description=(
        "The Eibon provides defensive screening for Pleiadian convoys -- faster than "
        "the template escort frigate, lighter, with extended endurance that lets it stay "
        "with a convoy longer than other factions' escorts. The Eibon's defensive "
        "advantage is not just speed but perception: modified crew whose infrared vision "
        "and enhanced sensory processing detect incoming threats faster than baseline "
        "crews, giving the Eibon marginally more reaction time to interpose itself "
        "between the threat and its charges. In hostile environments -- the radiation "
        "zones and nebular systems that Pleiadian space is full of -- the Eibon fights "
        "at full effectiveness while attacking forces from other factions suffer degraded "
        "crew performance. A convoy escorted by Eibons through a nebula is attacking "
        "into the Pleiadian environmental advantage."
    ),
    exterior_appearance_description=(
        "A 115-meter military spacecraft with a dark, matte hull. A compact, curved body "
        "shaped like a broad carapace -- a humped upper surface with a flat underside. The "
        "hull has a faint green discolouration and a chitinous, layered texture. No visible "
        "windows. A plasma cannon integrated into the top ridge as a raised seam. A light ion "
        "turret recessed into the upper surface as a smooth dome. Engine bells recessed into "
        "the rear beneath overlapping hull material. No external lights. Faint green "
        "bioluminescent traces in branching patterns along the hull seams. Violet strain "
        "insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Standard Pleiadian interior -- dark, cold, thin atmosphere. The gunnery stations "
        "have infrared targeting displays. The bridge crew works in conditions that would "
        "require full environmental suits for baseline humans. The crew quarters are "
        "small cold pods. The ship operates in silence broken only by the low-frequency "
        "communications the modified crew uses."
    ),
    minimum_crew=[{"officers": 4}, {"crew": 18}],
    secondary_crew=[{"gunners": 5}],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared targeting displays",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

ATLACH_NACHA = ShipTemplate(
    name="Atlach-Nacha",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=190,
    armor=42,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=225,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=49,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Fast fleet destroyer with extended endurance and modified point defense crews",
    long_description=(
        "The Atlach-Nacha is the Pleiadian fleet destroyer -- faster, lighter, and "
        "longer-enduring than the template. Its point defense crews see in infrared, "
        "tracking targets through modified visual processing that detects thermal "
        "signatures other factions' gunners cannot perceive. In the hostile environments "
        "where Pleiadian fleets prefer to fight -- radiation zones, nebulae, stellar "
        "proximity -- the Atlach-Nacha's point defense remains at full effectiveness "
        "while other factions' destroyer crews suffer degraded performance from heat, "
        "radiation, or sensor interference. The ship's sensor profile is low for a "
        "destroyer -- the stripped environmental systems produce less emissions, making "
        "the Atlach-Nacha harder to target. The modified crew sustains combat operations "
        "longer than baseline crews: they tire slower, need less rotation, and consume "
        "fewer supplies. An Atlach-Nacha's point defense coverage does not degrade over "
        "time the way other factions' does."
    ),
    exterior_appearance_description=(
        "A 190-meter military spacecraft with a dark, matte hull. A long, curved body shaped "
        "like an enormous beetle carapace -- a humped upper surface curving down to a narrower "
        "underside, tapering at both the front and rear. The hull surface has a faint green "
        "discolouration and a chitinous, layered texture from biological hull coatings -- "
        "overlapping organic plates. No visible windows or bridge structure. A railgun "
        "integrated into the top ridge, visible as a long raised seam in the carapace. Three "
        "heavy laser turrets recessed into the hull surface, each visible only as a smooth "
        "dome flush with the surrounding shell. Engine bells recessed into the tapered rear "
        "beneath overlapping hull material. No external lights. Faint green bioluminescent "
        "traces in branching patterns across the hull surface, concentrated along the seams "
        "where the carapace plates overlap. Violet strain insignia on the sides, visible only "
        "at close range."
    ),
    interior_appearance_description=(
        "The three point defense battery stations are distributed port, starboard, and "
        "dorsal. Each is a dark compartment where modified gunners track targets through "
        "infrared displays and perception that goes beyond what the displays show. The "
        "bridge is a command space visible only in infrared. Corridors are dark and cold. "
        "The crew moves through the ship with the comfortable certainty of beings in "
        "their native environment. Crew quarters are small cold pods. The mess stores "
        "compounds. The ship is silent except for the low-frequency hum of systems and "
        "the modified crew's quiet communications."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 55}],
    secondary_crew=[
        {"gunners": 16},
        {"point_defense_crew": 14},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared targeting displays",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

ITHAQUA = ShipTemplate(
    name="Ithaqua",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=180,
    armor=28,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=185,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=49,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Fast pursuit destroyer with extended endurance for long-duration hunts",
    long_description=(
        "The Ithaqua is the Pleiadian pursuit ship -- and its pursuit doctrine is "
        "uniquely terrifying. Faster than the template, with supply duration that lets "
        "it chase longer, and a modified crew that does not fatigue at the rate baseline "
        "crews do. The Ithaqua follows contacts through hostile environments that other "
        "factions' hunter destroyers avoid -- radiation zones, nebulae, systems with "
        "extreme thermal conditions -- knowing that the pursuit degrades the target's "
        "crew while the Pleiadian crew remains unaffected. A ship running from an "
        "Ithaqua through a radiation belt is running into the Ithaqua's advantage. "
        "The modified crew does not need to rotate as frequently, does not suffer "
        "from the psychological effects of extended pursuit operations as severely, "
        "and does not consume supplies at the same rate. The Ithaqua pursues with the "
        "patient, inhuman endurance of something that was built for an environment "
        "the target was not."
    ),
    exterior_appearance_description=(
        "A 180-meter military spacecraft with a dark, matte hull. A lean, elongated body "
        "shaped like a narrow shell -- a smooth, curved upper surface tapering to a point at "
        "the front. The hull has a faint green discolouration and a chitinous texture. No "
        "visible windows. A heavy particle cannon integrated into the front, visible as a "
        "ridged protrusion extending from the hull. A torpedo bay integrated into the lower "
        "front as a seam in the shell. An ion turret recessed into the upper surface as a "
        "smooth dome. Engine bells recessed into the tapered rear. No external lights. Faint "
        "green bioluminescent traces in branching patterns along the hull seams. Violet strain "
        "insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The bridge is built for extended pursuit -- acceleration couches in darkness, "
        "infrared displays showing closure rates and intercept geometry. The torpedo room "
        "forward is crewed by modified ratings whose restructured musculature handles "
        "the heavy loading work without the fatigue that limits baseline crews. Crew "
        "quarters are cold pods. The ship on a multi-week pursuit is a dark, cold, "
        "quiet vessel crewed by people who are comfortable in conditions the target's "
        "crew would find barely survivable."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 42}],
    secondary_crew=[
        {"gunners": 10},
        {"torpedo_crew": 4},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared targeting displays",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

NYARLATHOTEP = ShipTemplate(
    name="Nyarlathotep",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="EW Destroyer",
    combat_role="Electronic warfare / jamming / information denial",
    length=200,
    armor=24,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=150,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=49,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Fast EW destroyer with modified operators and low-emission hull",
    long_description=(
        "The Nyarlathotep is the Pleiadian electronic warfare platform -- and its "
        "effectiveness is compounded by the faction's existing sensor advantages. The "
        "ship's low-emission hull already makes it harder to detect and classify. Its "
        "modified EW operators perceive the electromagnetic environment through sensory "
        "modifications that go beyond baseline human perception -- operators with modified "
        "visual cortices that process signal data in ways that baseline neurology cannot "
        "replicate. The Nyarlathotep denies the enemy information not just through "
        "conventional jamming but through the exploitation of Pleiadian perceptual "
        "advantages -- identifying and disrupting enemy sensor systems in ways that "
        "baseline EW operators cannot conceive of because they cannot perceive what the "
        "modified operators perceive. In hostile environments, the Nyarlathotep's "
        "advantage compounds further: the enemy's sensors are degraded by the "
        "environment while the Pleiadian operators remain unaffected."
    ),
    exterior_appearance_description=(
        "A 200-meter military spacecraft with a dark, matte hull. A broad, curved body shaped "
        "like a wide carapace -- a humped upper surface with irregular ridges along the top "
        "and sides. The ridges house electronic warfare arrays, their emitter surfaces flush "
        "with the organic hull coating. The hull has a faint green discolouration and a "
        "chitinous texture. No visible windows. An ion cannon integrated into the top ridge. "
        "Engine bells recessed into the rear beneath overlapping hull material. No external "
        "lights. Faint green bioluminescent traces in branching patterns along the hull seams "
        "and around the EW ridges. Violet strain insignia on the sides, visible only at close "
        "range."
    ),
    interior_appearance_description=(
        "The electronic warfare centre is a sealed compartment amidships where modified "
        "operators work in darkness, perceiving the electromagnetic environment through "
        "senses that baseline humans do not have. The operators describe the experience "
        "in terms that baseline humans find incomprehensible -- synesthetic perceptions "
        "that map electromagnetic phenomena onto sensory channels that were biologically "
        "constructed for this purpose. The rest of the ship is standard Pleiadian -- dark, "
        "cold, thin atmosphere, silent."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 36}],
    secondary_crew=[{"ew_operators": 12}],
    additional_systems=[
        "Electronic warfare centre",
        "Jamming array (broadband)",
        "Sensor spoofing system",
        "Emissions analysis suite",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

MORDIGGIAN = ShipTemplate(
    name="Mordiggian",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Siege Destroyer",
    combat_role="Anti-capital firepower on a destroyer hull",
    length=215,
    armor=14,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=125,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.SIEGE_CANNON],
    default_small_craft=[],
    short_description="Fast siege cannon platform with modified gunnery crew",
    long_description=(
        "The Mordiggian mounts a siege cannon on a destroyer hull -- lighter and faster "
        "than the template, with a modified gunnery crew whose enhanced concentration "
        "and environmental tolerance allow them to sustain extreme-range fire in "
        "conditions that degrade other factions' siege crews. The loading cycle is "
        "handled by modified ratings whose restructured musculature does not fatigue "
        "under the repetitive strain. In hostile environments -- the Mordiggian's "
        "preferred operating conditions -- the siege crew maintains accuracy while enemy "
        "crews suffer from radiation exposure, thermal stress, or atmospheric "
        "interference. The Mordiggian is the Pleiadian answer to the question of how to "
        "apply siege-weight firepower: not through armour and endurance, but through "
        "operating in conditions where the enemy cannot effectively fight back."
    ),
    exterior_appearance_description=(
        "A 215-meter military spacecraft with a dark, matte hull. A squat, heavy body shaped "
        "like a thick carapace dominated by a massive siege cannon integrated into the top "
        "ridge -- visible as an enormous raised seam running the full length of the hull, the "
        "weapon barely distinguishable from the organic hull surface. The hull has a faint "
        "green discolouration and a chitinous, layered texture. No visible windows. Engine "
        "bells recessed into the rear beneath overlapping hull material. No external lights. "
        "Faint green bioluminescent traces in branching patterns along the hull seams. Violet "
        "strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The ship is built around the cannon. The gun crew works in darkness and cold, "
        "loading rounds with modified musculature and tracking targets through infrared "
        "fire-control displays. The crew spaces are packed into whatever volume the "
        "cannon doesn't occupy. Standard Pleiadian environment throughout -- dark, cold, "
        "thin atmosphere. The ship exists to fire its weapon."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 28}],
    secondary_crew=[{"gunnery_specialists": 8}],
    additional_systems=[
        "Spinal siege cannon mount",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared fire-control displays",
        "Low-emission hull design",
    ],
)

DAGON = ShipTemplate(
    name="Dagon",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=350,
    armor=58,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=400,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=63,
    default_weapons=[
        weapons.PRECISION_RAILGUN,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Fast, long-endurance line cruiser with reduced emissions",
    long_description=(
        "The Dagon is the Pleiadian main line combatant -- faster than the template heavy "
        "cruiser, lighter, with a sensor profile that belongs on a smaller ship and supply "
        "endurance that exceeds the template by weeks. The Dagon fights in the line like "
        "any heavy cruiser, but its advantages emerge in prolonged engagements and hostile "
        "environments. A Dagon holds station longer because its crew consumes less. It "
        "maintains combat effectiveness in radiation zones and nebulae because its crew "
        "is unaffected by conditions that degrade baseline performance. Its reduced "
        "sensor profile makes it harder to target at range. In open space, the Dagon is "
        "competitive with other factions' heavy cruisers. In hostile environments, it is "
        "superior because the crew is fighting at full capability while the enemy is not. "
        "Pleiadian fleet doctrine builds engagements around this asymmetry -- manoeuvre "
        "the battle into conditions where the environmental advantage matters, and the "
        "Dagons become the most effective line cruisers afloat."
    ),
    exterior_appearance_description=(
        "A 350-meter military spacecraft with a dark, matte hull. A massive, curved body "
        "shaped like an enormous shell -- a high, humped upper carapace curving down to a flat "
        "underside, the hull widest amidships and tapering at both ends. The hull surface has "
        "a faint green discolouration and a pronounced chitinous, layered texture -- "
        "overlapping organic plates visible across the entire surface. No visible windows or "
        "bridge structure. A precision railgun integrated into the top ridge as a long raised "
        "seam. Weapon batteries integrated into the sides, visible as rows of smooth blisters "
        "in the carapace. Point-defense turrets recessed into the hull as small domes. Engine "
        "bells recessed into the tapered rear beneath overlapping hull material. No external "
        "lights. Faint green bioluminescent traces in branching patterns across the hull "
        "surface. Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The bridge is a command amphitheatre in total darkness -- acceleration couches "
        "surrounding infrared displays that would be invisible to baseline eyes. Gunnery "
        "stations throughout the ship are dark and cold. The corridors are pitch-black "
        "freezing passages in unbreathable air. Modified crew move through them with the "
        "comfort of beings in their native environment. Crew quarters are cold pods. The "
        "mess is a compartment of sealed nutrition compounds. The ship at battle stations "
        "is a dark, cold, silent thing crewed by hundreds of modified people who are "
        "comfortable in conditions that would be an emergency for anyone else."
    ),
    minimum_crew=[{"senior_officers": 4}, {"officers": 22}, {"crew": 180}],
    secondary_crew=[
        {"gunners": 38},
        {"point_defense_crew": 14},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Infrared instrument displays (all stations)",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

SHOGGOTH = ShipTemplate(
    name="Shoggoth",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=330,
    armor=43,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=275,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=63,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Fast medium-jump flanking cruiser with extended endurance",
    long_description=(
        "The Shoggoth is the Pleiadian flanking cruiser -- the largest ship that can use "
        "medium jump points and the backbone of their flanking forces. Faster than the "
        "template, lighter, with extended endurance that lets a flanking force sustain "
        "operations longer than the enemy expects. A Pleiadian flanking force led by a "
        "Shoggoth does not need to win fast -- it can sustain itself in a contested "
        "position, wearing down the enemy through attrition while its modified crew "
        "consumes less and fatigues slower. The Shoggoth's doctrine exploits the same "
        "environmental asymmetry as the rest of the Pleiadian fleet: manoeuvre the "
        "flanking engagement into hostile conditions and fight at full effectiveness "
        "while the enemy does not."
    ),
    exterior_appearance_description=(
        "A 330-meter military spacecraft with a dark, matte hull. A long, curved body shaped "
        "like a narrow, elongated carapace -- a smooth upper surface tapering at both ends. "
        "The hull has a faint green discolouration and a chitinous, layered texture. No "
        "visible windows. A heavy railgun integrated into the top ridge as a raised seam. Two "
        "laser turrets recessed into the upper surface as smooth domes. Engine bells recessed "
        "into the tapered rear beneath overlapping hull material. No external lights. Faint "
        "green bioluminescent traces in branching patterns along the hull seams. Violet strain "
        "insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Standard Pleiadian interior at cruiser scale -- dark, cold, thin atmosphere "
        "throughout. A task force coordination section includes additional stations for "
        "managing a flanking group. The ship is more liveable than the Dagon in the sense "
        "that it operates independently for longer -- crew quarters are marginally larger "
        "cold pods, and the nutrition stores are more varied. Still dark. Still freezing. "
        "Still unbreathable."
    ),
    minimum_crew=[{"senior_officers": 3}, {"officers": 16}, {"crew": 130}],
    secondary_crew=[
        {"gunners": 22},
        {"point_defense_crew": 10},
        {"task_force_staff": 6},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Task force coordination suite",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

ABHOTH = ShipTemplate(
    name="Abhoth",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Carrier",
    combat_role="Cruiser combatant with embarked small craft",
    length=335,
    armor=38,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=275,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[("Voormi", 10)],
    short_description="Fast light carrier with modified flight crews and extended endurance",
    long_description=(
        "The Abhoth is a cruiser hull carrying a wing of ten Voormi fighters. The hangar "
        "is unlit and unheated -- standard Pleiadian conditions that would be a maintenance "
        "nightmare for other factions but are normal operating environment for modified "
        "deck crews. The embarked pilots launch from darkness into darkness, their "
        "modified eyes adjusting seamlessly between the infrared interior and the void. "
        "The Abhoth's flight operations are efficient not through the stimmed speed of "
        "an Antaren deck crew or the prosthetic tools of a Hyades crew, but through "
        "the simple advantage of crew that do not need the environmental support that "
        "slows other factions down. No time lost cycling airlocks between heated spaces "
        "and cold hangars -- the entire ship is cold. No time lost adjusting lighting -- "
        "there is no lighting. The Abhoth sustains its wing longer than other light "
        "carriers through extended supply stores and reduced crew consumption."
    ),
    exterior_appearance_description=(
        "A 335-meter military spacecraft with a dark, matte hull. A wide, curved body shaped "
        "like a broad carapace -- a humped upper surface with a flat underside. Launch bays "
        "along both sides visible as dark slots in the hull, no interior lighting visible. The "
        "hull has a faint green discolouration and a chitinous, layered texture. No visible "
        "windows. A railgun integrated into the top ridge as a raised seam forward of the "
        "launch bays. Two heavy laser turrets recessed into the upper surface as smooth domes. "
        "Engine bells recessed into the rear beneath overlapping hull material. No external "
        "lights. Faint green bioluminescent traces in branching patterns across the hull "
        "surface. Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The hangar is a cold, dark bay where ten Voormi sit in launch cradles. The deck "
        "crew works by infrared, their modified eyes seeing the craft as thermal "
        "silhouettes. The flight operations centre manages the wing through infrared "
        "displays. The pilot ready room is a dark compartment with acceleration couches "
        "where pilots wait in conditions baseline humans would find intolerable. The rest "
        "of the ship is standard Pleiadian -- dark, cold, thin atmosphere, silent."
    ),
    minimum_crew=[{"senior_officers": 3}, {"officers": 14}, {"crew": 110}],
    secondary_crew=[
        {"ship_gunners": 12},
        {"embarked_craft_pilots": 10},
        {"wing_coordinators": 2},
        {"hangar_crew": 10},
    ],
    additional_systems=[
        "Hangar bay (10 small craft)",
        "Craft maintenance facilities",
        "Flight operations centre",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

HASTUR = ShipTemplate(
    name="Hastur",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=800,
    armor=78,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=1500,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=91,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Fast, long-endurance battleship with modified crew of over a thousand",
    long_description=(
        "The Hastur is the Pleiadian battleship -- faster than any other faction's "
        "equivalent and capable of sustaining combat operations for weeks beyond what "
        "other battleships can manage. The modified crew of over a thousand operates in "
        "total darkness at near-freezing temperatures, breathing atmosphere that would "
        "kill baseline humans. The mass savings from eliminating life support systems "
        "that a thousand-person baseline crew would require are staggering -- the weight "
        "goes to engines that make the Hastur the fastest battleship afloat, and to "
        "supply stores that let it fight for months. The Hastur's sensor profile is below "
        "template -- a battleship that reads on sensors as something lighter. In hostile "
        "environments, the Hastur is at full combat effectiveness while other factions' "
        "battleships suffer degraded crew performance. The Hastur does not win through "
        "the Hyades method of being unkillable or the Antaren method of burning fast and "
        "bright. It wins through the Pleiadian method of fighting at full capability in "
        "conditions where the enemy cannot."
    ),
    exterior_appearance_description=(
        "An 800-meter military spacecraft with a dark, matte hull. A massive, curved body "
        "shaped like an enormous elongated carapace -- a high, humped upper surface curving "
        "down on all sides, widest amidships, tapering at both ends. The hull surface has a "
        "faint green discolouration and a pronounced chitinous, layered texture -- heavy "
        "overlapping organic plates visible across the entire surface. No visible windows or "
        "bridge structure. A gauss cannon integrated into the top ridge as a massive raised "
        "seam. Weapon batteries integrated into the sides as rows of smooth blisters. "
        "Point-defense turrets recessed into the hull as small domes. Engine bells recessed "
        "into the tapered rear beneath overlapping hull material. No external lights. Faint "
        "green bioluminescent traces in branching patterns across the hull surface, glowing "
        "along every seam where the organic plates overlap. Violet strain insignia on the "
        "sides, visible only at close range."
    ),
    interior_appearance_description=(
        "Kilometres of pitch-black freezing corridors in unbreathable air. Over a "
        "thousand modified crew navigate by infrared, communicate in low frequencies, "
        "and work in conditions that would be a mass casualty event for baseline humans. "
        "The bridge is a vast dark amphitheatre of acceleration couches surrounding "
        "infrared displays. Gunnery stations are dark and cold. Engineering spaces are "
        "dark and cold. Crew quarters are rows of cold pods. The mess stores sealed "
        "nutrition compounds. The ship has no sound that baseline ears would register as "
        "human activity -- the modified crew communicates at frequencies and volumes that "
        "don't carry in standard atmosphere. A baseline human aboard the Hastur would "
        "experience it as an enormous, freezing, airless tomb crewed by silent shapes "
        "that move in perfect darkness."
    ),
    minimum_crew=[{"senior_officers": 10}, {"officers": 65}, {"crew": 750}],
    secondary_crew=[
        {"gunners": 120},
        {"point_defense_crew": 65},
        {"sensor_specialists": 20},
    ],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting (ship-wide)",
        "Infrared instrument displays (all stations)",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

TIAMAT = ShipTemplate(
    name="Tiamat",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1050,
    armor=38,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=1200,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=91,
    default_weapons=[
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_PD,
        weapons.LASER_PD,
        weapons.LASER_PD,
    ],
    default_small_craft=[
        ("Byakhee", 10),
        ("Byakhee", 10),
        ("Nightgaunt", 10),
        ("Voormi", 10),
    ],
    short_description="Fast carrier deploying modified strike wings from dark, cold hangar bays",
    long_description=(
        "The Tiamat is the Pleiadian fleet carrier -- faster than the template, with "
        "extended endurance and four wings of strike craft crewed by modified pilots "
        "who launch from dark, freezing hangar bays into the void without the transition "
        "shock that other factions' pilots experience moving from heated, lit interiors "
        "to vacuum. There is no transition. The interior is already dark and cold. The "
        "standard wing composition is two wings of Byakhee bombers, one wing of "
        "Nightgaunt interceptors, and one wing of Voormi fighters. Every craft is "
        "lighter and faster than its equivalent from other factions. The Tiamat sustains "
        "its air wing longer through reduced consumable consumption -- modified pilots "
        "need less between sorties, and the carrier's extended stores support more "
        "cycles. Medium-jump capable, allowing it to project strike power through "
        "flanking routes."
    ),
    exterior_appearance_description=(
        "A 1050-meter military spacecraft with a dark, matte hull. A long, narrow body shaped "
        "like an enormous teardrop -- tapering to a point at the front, swelling to its widest "
        "amidships, narrowing again at the rear. The hull surface has a faint green "
        "discolouration and a pronounced chitinous, layered texture -- heavy overlapping "
        "organic plates. No visible windows or bridge structure. Hangar openings along both "
        "sides are dark slots in the carapace with no interior lighting visible. Laser turrets "
        "recessed into the hull surface as smooth domes. Engine bells recessed into the rear "
        "beneath overlapping hull material. No external lights. Faint green bioluminescent "
        "traces in branching patterns across the hull surface, concentrated along the seams "
        "where the organic plates overlap. Violet strain insignia on the sides, visible only "
        "at close range."
    ),
    interior_appearance_description=(
        "The four hangar bays are vast dark spaces where forty strike craft sit in "
        "launch cradles. The deck crews work by infrared, seeing the craft as thermal "
        "silhouettes. The pilot ready rooms are dark compartments where modified pilots "
        "wait in cold silence. The flight operations centre coordinates the wing through "
        "infrared displays and low-frequency communications. The rest of the ship is "
        "kilometres of dark, freezing corridor connecting the hangars to crew spaces, "
        "engineering, and the bridge. A baseline human aboard the Tiamat would need a "
        "full environmental suit, a light source, and a guide to avoid dying in the "
        "dark."
    ),
    minimum_crew=[{"senior_officers": 16}, {"officers": 110}, {"crew": 1600}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"wing_coordinators": 6},
        {"flight_deck_crew": 120},
        {"hangar_maintenance": 80},
        {"ship_gunners": 24},
    ],
    additional_systems=[
        "Hangar bays (x4, 10 craft each)",
        "Craft maintenance facilities",
        "Flight operations centre",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting (ship-wide)",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption)",
    ],
)

AZATHOTH = ShipTemplate(
    name="Azathoth",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=1600,
    armor=92,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=2500,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=112,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Fast dreadnought with modified siege crews and extreme operational endurance",
    long_description=(
        "The Azathoth is the largest vessel in the Pleiadian fleet -- and the most alien "
        "warship in known space. Nearly two kilometres of dark, freezing, airless ship "
        "crewed by thousands of modified humans who navigate, fight, eat, sleep, and "
        "communicate in conditions that would be a civilisational emergency for baseline "
        "humans. The Azathoth is faster than any other dreadnought -- Slow where the "
        "template is Very Slow -- and its operational endurance exceeds the template by "
        "weeks. Its modified siege crews sustain extreme-range fire longer than baseline "
        "crews: they do not fatigue at the same rate, they do not need rotation as "
        "frequently, and they do not suffer from the psychological effects of sustained "
        "high-intensity combat operations as severely. In hostile environments, the "
        "Azathoth operates at full effectiveness while other dreadnoughts' crews "
        "struggle. Only a handful exist. Each one is a strategic asset that represents "
        "the furthest extreme of Pleiadian design philosophy -- a ship built entirely "
        "for a crew that has been modified so far from baseline that the ship itself "
        "would be lethal to anyone else."
    ),
    exterior_appearance_description=(
        "A 1600-meter military spacecraft with a dark, matte hull. A massive body shaped like "
        "an enormous curved shell -- a high, humped upper carapace curving down on all sides, "
        "widest amidships, tapering at both ends. The hull surface has a faint green "
        "discolouration and a heavy chitinous, layered texture -- thick overlapping organic "
        "plates across the entire surface, giving a scaled appearance. No visible windows or "
        "bridge structure. Twin siege cannons integrated into the top ridge as two parallel "
        "raised seams running much of the hull length. Point-defense turrets recessed into the "
        "hull as small domes at regular intervals. Engine bells recessed into the tapered rear "
        "beneath overlapping hull material. No external lights. Faint green bioluminescent "
        "traces in branching patterns across the entire hull surface, glowing along every seam "
        "where the organic plates overlap. Violet strain insignia on the sides, visible only "
        "at close range. An enormous dark shape that looks more grown than built."
    ),
    interior_appearance_description=(
        "The Azathoth's interior is an alien environment. Kilometres of pitch-black "
        "corridors at near-freezing temperatures in thin, chemical-heavy atmosphere. "
        "Thousands of modified crew navigate by infrared, communicate in frequencies "
        "that baseline ears cannot detect, and consume nutrition compounds that baseline "
        "stomachs cannot process. The bridge is an enormous dark amphitheatre. The siege "
        "cannon fire-control sections are dark and cold. Engineering is dark and cold. "
        "Crew quarters are thousands of cold pods in dark compartments. The mess halls "
        "are rooms of sealed compounds consumed in silence. Recreation spaces exist but "
        "are dark and cold and the activities that occur in them are adapted to modified "
        "bodies. A baseline human aboard the Azathoth without a full environmental suit "
        "would be dead within minutes. With a suit, they would be lost within hours in "
        "the dark."
    ),
    minimum_crew=[{"senior_officers": 35}, {"officers": 230}, {"crew": 3200}],
    secondary_crew=[
        {"gunners": 180},
        {"point_defense_crew": 40},
        {"fleet_coordination_staff": 35},
        {"sensor_specialists": 60},
    ],
    additional_systems=[
        "Twin spinal siege cannon mounts",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation (ship-wide)",
        "No standard lighting (ship-wide)",
        "Infrared instrument displays (all stations)",
        "Low-emission hull design",
        "Extended supply stores (reduced crew consumption, months-duration)",
    ],
)

YUGGOTH = ShipTemplate(
    name="Yuggoth",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Fleet Tender",
    combat_role="Resupply / ammunition and fuel transport",
    length=290,
    armor=18,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=150,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=70,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Fast fleet tender with extended endurance and reduced crew",
    long_description=(
        "The Yuggoth is the Pleiadian logistics backbone -- carrying fuel, ammunition, "
        "and the specialized nutrition compounds that Pleiadian crews consume. The "
        "Yuggoth's cargo is lighter per unit of crew sustained than other factions' "
        "tenders because the modified crew aboard the ships it resupplies needs less "
        "of everything: less food, less atmospheric processing compounds, less heating "
        "fuel (none), less lighting equipment (none). A Yuggoth resupplying a Pleiadian "
        "task force delivers ammunition and fuel; the crew sustainability stores are a "
        "fraction of what other factions' tenders carry. This makes the Pleiadian "
        "logistics chain lighter and faster -- fewer tender runs needed, and each run "
        "carries a higher proportion of combat-relevant supplies."
    ),
    exterior_appearance_description=(
        "A 290-meter military spacecraft with a dark, matte hull. A bulky, curved body shaped "
        "like a broad carapace with a flat underside. Docking clamps and transfer fittings "
        "along both sides, integrated into the hull surface -- visible as ridged protrusions "
        "in the shell. The hull has a faint green discolouration and a chitinous texture. No "
        "visible windows. An ion turret recessed into the upper surface as a smooth dome. A "
        "point-defense mount recessed into the rear. Engine bells recessed into the rear "
        "beneath overlapping hull material. No external lights. Faint green bioluminescent "
        "traces along the hull seams. Violet strain insignia on the sides, visible only at "
        "close range."
    ),
    interior_appearance_description=(
        "Mostly cargo space -- modular containers of ammunition, fuel cells, and the "
        "sealed nutrition compounds that Pleiadian ships stock instead of food. The cargo "
        "bays are dark and cold. The crew section forward is standard Pleiadian -- dark, "
        "cold, thin atmosphere. The crew is smaller than other factions' tender crews "
        "because the modified ratings handle cargo operations with fewer people."
    ),
    minimum_crew=[{"officers": 6}, {"crew": 35}],
    secondary_crew=[{"cargo_handlers": 12}],
    additional_systems=[
        "Modular cargo system",
        "Nutrition compound storage",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design",
    ],
)

SHANTAK = ShipTemplate(
    name="Shantak",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Supply Runner",
    combat_role="Fast resupply through medium jump points",
    length=95,
    armor=9,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=60,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Extremely fast supply runner with minimal emissions",
    long_description=(
        "The Shantak is the fastest supply vessel in known space -- matching the Antaren "
        "Jetstream for the title but with longer endurance. The Shantak delivers "
        "ammunition, fuel, and nutrition compounds to forward-deployed task forces "
        "through medium jump points. Its sensor profile is insignificant for a frigate-"
        "weight vessel -- the stripped environmental systems produce almost no emissions, "
        "making the Shantak difficult to detect and intercept. A supply runner that "
        "cannot be found cannot be destroyed, and the Pleiadian logistics chain relies "
        "on the Shantak's near-invisibility as much as its speed."
    ),
    exterior_appearance_description=(
        "A 95-meter military spacecraft with a dark, matte hull. A long, narrow body shaped "
        "like an elongated seed pod. A small crew section at the front. The majority of the "
        "hull is cargo space, loading hatches integrated into the sides as seams in the "
        "carapace. The hull has a faint green discolouration and a chitinous texture. No "
        "visible windows. An ion turret recessed into the upper surface as a smooth dome. "
        "Engine bells recessed into the tapered rear. No external lights. Faint green "
        "bioluminescent traces along the hull seams. Violet strain insignia on the sides, "
        "visible only at close range."
    ),
    interior_appearance_description=(
        "Engine, jump drive, and cargo. The cargo hold stores ammunition, fuel cells, "
        "and sealed nutrition compounds. Crew spaces are minimal -- a dark bridge, cold "
        "bunks for the skeleton crew, and a small compartment of nutrition compounds. "
        "Standard Pleiadian environment throughout."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 5}],
    secondary_crew=[],
    additional_systems=[
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design",
    ],
)

PNAKOTUS = ShipTemplate(
    name="Pnakotus",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Field Support Ship",
    combat_role="Medical / biological maintenance / fleet repair hub",
    length=460,
    armor=28,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=300,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=70,
    default_weapons=[weapons.ION_CANNON, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Biological maintenance and fleet support ship -- the heart of Pleiadian fleet sustainment",
    long_description=(
        "The Pnakotus is the Pleiadian equivalent of a field support ship -- but where "
        "the Hyades Smithy repairs mechanical prosthetics and the Canopan Ammonite "
        "reanimates the dead, the Pnakotus maintains biological modifications. Modified "
        "crew across the fleet develop complications -- symbiotic organisms that grow "
        "too fast, photosynthetic pigments that produce unexpected compounds, "
        "restructured organs that drift from their intended parameters. The Pnakotus "
        "carries bioengineering laboratories where specialists can diagnose, adjust, "
        "and repair the biological modifications that keep the fleet's crew functional. "
        "It also carries stocks of the mutagenic compounds, symbiotic cultures, and "
        "surgical equipment needed for field-level modification work. A Pleiadian task "
        "force without a Pnakotus gradually loses crew effectiveness as modifications "
        "drift. With one, the fleet sustains its biological edge. The Pnakotus also "
        "provides conventional medical treatment and ship repair facilities, but its "
        "primary role is maintaining the biology that makes the Pleiadian fleet what "
        "it is."
    ),
    exterior_appearance_description=(
        "A 460-meter military spacecraft with a dark, matte hull. A wide, curved body shaped "
        "like a broad, heavy carapace. A prominent section amidships for medical and "
        "biological support -- marked with faintly bioluminescent symbols in green and violet, "
        "the Pleiadian variant of medical markings. Docking ports along both sides integrated "
        "into the hull surface. The hull has a faint green discolouration and a chitinous, "
        "layered texture. No visible windows. An ion cannon integrated into the top ridge as a "
        "raised seam. Two point-defense mounts recessed into the hull as smooth domes. Engine "
        "bells recessed into the rear beneath overlapping hull material. No external lights. "
        "Faint green bioluminescent traces in branching patterns across the hull surface. "
        "Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The bioengineering laboratories are the ship's heart -- sealed compartments "
        "where specialists work in conditions calibrated for the modification work "
        "rather than the standard Pleiadian cold-and-dark. Some laboratories are warm "
        "and bright -- conditions that the modified specialists find uncomfortable but "
        "that the symbiotic cultures and biological samples require. These are the only "
        "spaces on any Pleiadian warship with standard lighting and heating, and the "
        "crew avoids them when possible. The ship repair facilities are dark and cold. "
        "The medical bay handles conventional injuries. The rest of the ship is standard "
        "Pleiadian environment. The Pnakotus smells different from other Pleiadian "
        "vessels -- the bioengineering laboratories produce organic compounds that give "
        "the ship a distinctive, unsettling biological odour."
    ),
    minimum_crew=[{"officers": 16}, {"crew": 100}],
    secondary_crew=[
        {"bioengineering_specialists": 20},
        {"medical": 15},
        {"repair_technicians": 12},
        {"laboratory_technicians": 8},
    ],
    additional_systems=[
        "Bioengineering laboratories (x4)",
        "Symbiotic culture storage",
        "Mutagenic compound stores",
        "Modification calibration equipment",
        "Ship-to-ship medical transfer facilities",
        "Conventional ship repair bay",
        "Minimal atmosphere (Pleiadian standard, except laboratories)",
        "Laboratory environmental controls (heated, lit -- exceptions to fleet standard)",
        "Extended supply stores (reduced crew consumption)",
    ],
)

RLYEH = ShipTemplate(
    name="R'lyeh",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=560,
    armor=68,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=1000,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=70,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Fast assault transport deploying modified ground forces",
    long_description=(
        "The R'lyeh delivers a Pleiadian ground force into hostile territory -- and that "
        "ground force is modified for conditions that would incapacitate baseline "
        "infantry. Pleiadian marines with restructured lungs, radiation-tolerant "
        "biology, cold-adapted physiology, and enhanced low-light vision fight at full "
        "effectiveness in environments that force baseline defenders to operate in "
        "environmental suits. The R'lyeh itself is faster than the template assault "
        "transport, reaching the deployment zone quickly. The troop decks carry the "
        "same thin, cold, dark atmosphere as the rest of the ship -- the marines live "
        "in conditions that would be a hazmat situation for baseline troops. The "
        "deployment is fast: hatches open, ramps extend, and modified marines advance "
        "into conditions they were built for. If the contested environment is hostile "
        "-- radiation, extreme cold, toxic atmosphere -- the Pleiadian ground force "
        "has arrived at home."
    ),
    exterior_appearance_description=(
        "A 560-meter military spacecraft with a dark, matte hull. A massive, heavy body "
        "shaped like a thick, rounded carapace -- a humped upper surface with a broad, flat "
        "underside. The hull has a faint green discolouration and a pronounced chitinous, "
        "layered texture -- overlapping organic plates. No visible windows. A particle cannon "
        "integrated into the top ridge as a raised seam. Loading ramps on the underside and "
        "rear, visible as large seams in the shell that open for deployment. Point-defense "
        "turrets recessed into the hull as smooth domes along the sides and top. Engine bells "
        "recessed into the rear beneath overlapping hull material. No external lights. Faint "
        "green bioluminescent traces in branching patterns across the hull surface. Violet "
        "strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The troop decks are vast dark compartments -- thousands of marines in cold pods, "
        "their modified biology comfortable in conditions that would be hypothermic for "
        "baseline troops. Vehicle bays on the lower decks carry armoured transports and "
        "heavy weapons. The deployment bays are built for rapid disembarkation. The "
        "bioengineering section handles field-level modification maintenance for the "
        "embarked force. The ship has the dark, silent, cold atmosphere of every "
        "Pleiadian vessel, scaled to carry an army."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 60}],
    secondary_crew=[
        {"marine_officers": 40},
        {"marines": 3500},
        {"vehicle_crew": 150},
        {"bioengineering_specialists": 4},
        {"medical": 20},
        {"ship_gunners": 14},
    ],
    additional_systems=[
        "Troop decks (modified environment)",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Bioengineering section (field-level)",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
    ],
)

SPIRULA = ShipTemplate(
    name="Spirula",
    faction=ShipFaction.PLEIADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Insertion Transport",
    combat_role="Special operations deployment behind enemy lines",
    length=130,
    armor=5,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=45,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Near-invisible hard-jump insertion transport with modified special forces",
    long_description=(
        "The Spirula is a hard-jump-capable transport that delivers Pleiadian special "
        "operations forces behind enemy lines. Its sensor profile is insignificant -- "
        "the lowest of any frigate-weight vessel in any faction's fleet -- achieved "
        "through the near-total absence of emissions. No heat. No light. No atmospheric "
        "processing signatures. The ship radiates almost nothing because it runs almost "
        "nothing. The modified special operators it carries are adapted for infiltration "
        "in hostile environments -- they can operate without environmental suits in "
        "conditions that would require full life support for baseline troops, making "
        "them nearly undetectable by the environmental signatures that betray other "
        "factions' special forces. The Spirula arrives through hard jump points, "
        "deploys its operators into darkness, and vanishes."
    ),
    exterior_appearance_description=(
        "A 130-meter military spacecraft with a dark, matte hull. A compact, curved body "
        "shaped like a narrow carapace -- a smooth upper surface tapering at both ends. The "
        "hull has a faint green discolouration and a chitinous texture. No visible windows. A "
        "light ion turret recessed into the upper surface as a smooth dome. Loading ramps on "
        "the underside, visible as seams in the shell. Engine bells recessed into the tapered "
        "rear. No external lights. Faint green bioluminescent traces along the hull seams. "
        "Violet strain insignia on the sides, visible only at close range."
    ),
    interior_appearance_description=(
        "The interior splits between the hard-jump drive, crew section, and operator "
        "compartment. The operator compartment holds bunks and equipment storage in "
        "standard Pleiadian conditions -- dark, cold, thin atmosphere. The special "
        "operators wait in conditions that would be survival training for other factions' "
        "troops. The crew section is minimal. The ship is the quietest vessel in any "
        "faction's fleet."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 5}],
    secondary_crew=[
        {"special_forces": 36},
        {"special_forces_officers": 4},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Minimal atmosphere (Pleiadian standard)",
        "No thermal regulation",
        "No standard lighting",
        "Low-emission hull design (maximum suppression)",
        "Operator compartment",
    ],
)


PLEIADES_SMALL_CRAFT = {
    "Zoog": ZOOG,
    "Byakhee": BYAKHEE,
    "Nightgaunt": NIGHTGAUNT,
    "Voormi": VOORMI,
    "Gug": GUG,
}

PLEIADES_CORVETTES = {
    "Ulthar": ULTHAR,
    "Celephais": CELEPHAIS,
    "Kadath": KADATH,
}

PLEIADES_FRIGATES = {
    "Bokrug": BOKRUG,
    "Commoriom": COMMORIOM,
    "Eibon": EIBON,
}

PLEIADES_DESTROYERS = {
    "Atlach-Nacha": ATLACH_NACHA,
    "Ithaqua": ITHAQUA,
    "Nyarlathotep": NYARLATHOTEP,
    "Mordiggian": MORDIGGIAN,
}

PLEIADES_CRUISERS = {
    "Dagon": DAGON,
    "Shoggoth": SHOGGOTH,
    "Abhoth": ABHOTH,
}

PLEIADES_CAPITALS = {
    "Hastur": HASTUR,
    "Tiamat": TIAMAT,
    "Azathoth": AZATHOTH,
}

PLEIADES_SUPPORT = {
    "Yuggoth": YUGGOTH,
    "Shantak": SHANTAK,
    "Pnakotus": PNAKOTUS,
    "R'lyeh": RLYEH,
    "Spirula": SPIRULA,
}

PLEIADES_ALL_SHIPS = {
    **PLEIADES_SMALL_CRAFT,
    **PLEIADES_CORVETTES,
    **PLEIADES_FRIGATES,
    **PLEIADES_DESTROYERS,
    **PLEIADES_CRUISERS,
    **PLEIADES_CAPITALS,
    **PLEIADES_SUPPORT,
}