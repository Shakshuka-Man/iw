from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


JAVELIN = ShipTemplate(
    name="Javelin",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=24,
    armor=5,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=10,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Heavy bomber with reinforced hull and prosthetic crew interface",
    long_description=(
        "The Javelin is the Hyades bomber -- the heaviest, toughest bomber in known space. "
        "Where the Canopan Sabertooth is over-built and the Antaren Thunderbolt is fast, "
        "the Javelin is simply armored beyond anything else in its weight class. Hyades "
        "engineers applied the same industrial construction philosophy to a twenty-metre "
        "bomber that they apply to a kilometer-long dreadnought: thicker plate, heavier "
        "frame, standardized fasteners. The Javelin's crew interface with the ship "
        "through prosthetic connections -- a pilot with mechanical hands socketed into "
        "the flight controls, a weapons officer with a synthetic eye feeding targeting "
        "data directly to the torpedo system. The torpedo approach run is the same "
        "harrowing experience for every faction. The difference is that a Javelin "
        "absorbs point defense hits that would destroy lighter bombers and keeps flying. "
        "A Javelin that loses its pilot has a weapons officer with a prosthetic arm "
        "already socketed into the backup flight controls."
    ),
    exterior_appearance_description=(
        "A 24-meter two-seat military spacecraft with a bare metal hull. A flat rectangular "
        "body with a blunt front. Hull plates on the front and sides, but the top is open "
        "framework -- structural cross-bracing and cable bundles visible. The torpedo housing "
        "dominates the underside, bolted on with visible mounting brackets and fuel lines. A "
        "glazed canopy with a heavy welded metal frame. Engine bells in exposed mechanical "
        "housings at the rear, exhaust piping visible. Weld seams and bolt heads across every "
        "plated surface. Yellow hazard striping around the torpedo housing and engine "
        "housings. A maroon guild crest stencilled on both sides."
    ),
    interior_appearance_description=(
        "Two stations in tandem -- pilot forward, weapons officer behind -- in a cockpit "
        "built from the same heavy-gauge steel as the hull. Control interfaces are "
        "mechanical sockets where prosthetic limbs plug directly into the ship's systems. "
        "A pilot with standard-issue mechanical hands slots into the flight controls and "
        "feels the ship's attitude through haptic feedback in their prosthetic wrists. "
        "The cockpit has the industrial, unfinished feel common to all Hyades vessels -- "
        "exposed conduit, visible fasteners, bare metal surfaces. Nothing decorative. "
        "Everything built to be repaired by someone with a wrench for a hand."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Prosthetic flight interface sockets", "Backup flight controls"],
)

DART = ShipTemplate(
    name="Dart",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Interceptor",
    combat_role="Fast attack / anti-scout / anti-bomber",
    length=12,
    armor=1,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=4,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Armored interceptor with prosthetic pilot interface",
    long_description=(
        "The Dart is the Hyades interceptor -- and uniquely among interceptors, it carries "
        "armor. Not much -- a single point of plating where every other faction's "
        "interceptor carries zero -- but enough to absorb a glancing point defense hit "
        "that would destroy a bare-hulled interceptor. Hyades engineers refused to build "
        "a ship with no armor. It is against their institutional instincts. The weight "
        "cost is marginal, and the Dart retains Very Fast speed because the hull was "
        "designed from the start to carry the extra mass. The pilot interfaces with the "
        "ship through prosthetic sockets -- mechanical hands in the flight controls, a "
        "synthetic eye feeding raw instrument data without the processing delay of a "
        "display screen. A Hyades interceptor pilot with full prosthetic replacement "
        "of both arms and eyes is the preferred crew configuration -- the ship becomes "
        "an extension of the body in a way that is purely mechanical, without the neural "
        "dependency that Polaran integration creates."
    ),
    exterior_appearance_description=(
        "A 12-meter single-seat military spacecraft with a bare metal hull. A small, narrow "
        "rectangular box with a blunt front. Minimal hull plating -- much of the body is "
        "exposed structural frame with cable bundles and hydraulic lines visible. A heavy "
        "laser turret bolted to the top in a welded housing. A glazed canopy with a heavy "
        "metal frame. Engine bells at the rear in an exposed mount, exhaust piping visible. "
        "Weld seams across every surface. Yellow hazard striping around the canopy frame and "
        "engine mount. A maroon guild crest stencilled on both sides."
    ),
    interior_appearance_description=(
        "A single-seat cockpit with prosthetic socket interfaces at both armrests and "
        "the instrument panel. The pilot's mechanical hands lock into the flight controls "
        "with an audible click. A synthetic eye interfaces with the targeting system "
        "through a dedicated socket at the canopy frame. The cockpit is tight, functional, "
        "and has the mechanical smell of lubricant and clean metal that characterizes "
        "all Hyades vessels."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Prosthetic flight interface sockets", "Direct eye-targeting link"],
)

STILETTO = ShipTemplate(
    name="Stiletto",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Fighter",
    combat_role="Escort / area control / anti-small-craft",
    length=20,
    armor=9,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=18,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.PLASMA_LAUNCHER],
    default_small_craft=[],
    short_description="Heavy fighter with reinforced construction and prosthetic crew interface",
    long_description=(
        "The Stiletto is the Hyades general-purpose fighter -- slower than the template "
        "but armored and hulled beyond anything else in its weight class. Like the "
        "Canopan Raptor, the Stiletto trades speed for survivability, but the mechanism "
        "is different: where the Raptor is over-built, the Stiletto is over-armored. "
        "Hyades fighters carry more plate per tonne than any other faction's equivalent. "
        "The Stiletto's pilot interfaces through prosthetic sockets, and the fighter "
        "is designed around the assumption that the pilot has at minimum mechanical "
        "hands and a synthetic eye. A baseline human can fly a Stiletto through "
        "conventional controls, but the ship is optimized for augmented operation -- "
        "the prosthetic interface is faster, more precise, and more intuitive. "
        "Stilettos work in wings, their heavy armor allowing them to absorb fire "
        "that would destroy lighter fighters while they close to plasma range."
    ),
    exterior_appearance_description=(
        "A 20-meter single-seat military spacecraft with a bare metal hull. A squat "
        "rectangular box -- flat on all sides, squared off at every edge. Hull plates cover "
        "the front and sides but the top and rear are open framework -- exposed structural "
        "cross-bracing, cable bundles, and hydraulic lines visible. A plasma launcher bolted "
        "to the underside. A glazed canopy with a heavy metal frame. Blunt stabiliser surfaces "
        "welded to the rear. Engine bells mounted in an exposed mechanical housing at the "
        "rear, exhaust piping visible. Weld seams and bolt heads across every plated surface. "
        "Yellow hazard striping around the canopy frame and engine housing. A maroon guild "
        "crest stencilled on both sides."
    ),
    interior_appearance_description=(
        "A single-seat cockpit surrounded by armor plate. Prosthetic sockets at the "
        "control interfaces -- hands, eyes, and a spinal socket at the seat back that "
        "feeds attitude data to pilots with spinal augmentation. The instruments are "
        "a mix of conventional displays and direct prosthetic feeds. The canopy is "
        "narrow and heavily reinforced. The cockpit smells of lubricant and has the "
        "unfinished, functional feel of a machine rather than an aircraft."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=[
        "Prosthetic flight interface sockets",
        "Spinal attitude feedback socket",
        "Reinforced cockpit armor",
    ],
)

CUTLASS = ShipTemplate(
    name="Cutlass",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=26,
    armor=14,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=30,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_PLASMA_CANNON],
    default_small_craft=[],
    short_description="Heavy gunship with maximum armor and augmented damage control crew",
    long_description=(
        "The Cutlass is the Hyades gunship -- the most heavily armored small craft in "
        "known space. Where the Antaren Flurry dashes through escort screens at speed "
        "and the Canopan Tarpan walks through them on hull points, the Cutlass shoulders "
        "through on raw armor. Point defense fire that would strip the plating from other "
        "gunships bounces off the Cutlass. The crew of six includes an engineer with "
        "prosthetic arms who can perform field repairs on the plasma cannon's power "
        "systems mid-engagement -- reaching into live electrical systems with mechanical "
        "hands that don't burn, don't conduct, and don't flinch. A baseline human "
        "engineer cannot do this. A Hyades engineer does it as routine maintenance. "
        "The Cutlass is slow. It is not subtle. It arrives at the escort screen and "
        "begins firing, and the escort screen discovers that killing it takes longer "
        "than expected."
    ),
    exterior_appearance_description=(
        "A 26-meter multi-crew military spacecraft with a bare metal hull. A broad, flat "
        "rectangular box -- broad and flat, squared off on all sides. Hull plates on the "
        "front and lower sides, but the upper hull is exposed framework with cable runs, "
        "hydraulic lines, and structural cross-bracing visible. A heavy plasma cannon bolted "
        "to the underside in a welded mount, the cannon's power cabling exposed along the "
        "hull. A wide glazed canopy with a heavy metal frame. Engine bells in a row across the "
        "rear in exposed mechanical housings. Weld seams and bolt heads across every surface. "
        "Yellow hazard striping around the weapon mount and engine housings. A maroon guild "
        "crest stencilled on both sides."
    ),
    interior_appearance_description=(
        "Six stations in a functional cabin -- pilot and gunner forward, engineer and "
        "sensor operator amidships, two damage control ratings aft. Prosthetic interface "
        "sockets at every station. The engineer's station includes a tool socket where "
        "a mechanical arm plugs directly into the ship's repair systems -- the engineer "
        "becomes the tool, feeling the ship's power feeds through haptic feedback and "
        "making adjustments with prosthetic precision. The interior is bare metal, "
        "exposed conduit, visible fasteners. The ship smells of lubricant and ozone."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}],
    secondary_crew=[{"engineer": 1}, {"sensor_operator": 1}, {"damage_control": 2}],
    additional_systems=[
        "Prosthetic interface sockets (all stations)",
        "Engineer tool socket",
        "Reinforced armor plating (heavy gauge)",
    ],
)

BUCKLER = ShipTemplate(
    name="Buckler",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=74,
    armor=28,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=90,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy patrol corvette with augmented crew and modular repair systems",
    long_description=(
        "The Buckler is the standard Hyades patrol vessel and the most commonly "
        "encountered ship in their navy. Heavier and slower than the template, with "
        "more armor than any other faction's patrol corvette, the Buckler is the "
        "embodiment of Hyades shipbuilding philosophy: build it tough, build it to be "
        "fixed, build it to last. A Buckler's crew is entirely augmented -- every rating "
        "has at minimum prosthetic hands and eyes, and most have more extensive "
        "replacement. The ship is designed around this: repair panels open with "
        "standardized fasteners that prosthetic hands grip better than organic ones. "
        "Power conduits route through accessible channels where a mechanical arm can "
        "reach without tools. Diagnostic sockets accept prosthetic interface plugs "
        "that let an engineer feel the state of a system through haptic feedback. "
        "The Buckler is slower than other factions' patrol corvettes and cannot chase "
        "fast contacts, but it holds position longer, absorbs more punishment, and "
        "repairs damage faster than anything else in its weight class."
    ),
    exterior_appearance_description=(
        "A 74-meter military spacecraft with a bare metal hull. A blocky rectangular body with "
        "a flat top, flat sides, and a blunt front. Heavy hull plates on the front, but the "
        "sides and top are partially open framework -- structural ribs, cable runs, piping, "
        "and hydraulic lines visible between plated sections. A particle cannon in a heavy "
        "mechanical mount along the top, the gun's cabling and feed mechanisms exposed. A "
        "heavy laser turret bolted to the top behind the bridge in a welded housing. A bridge "
        "section at the front with a glazed canopy. Engine bells at the rear in exposed "
        "mechanical frames. Weld seams, bolt patterns, and clamp fittings across every plated "
        "surface. Yellow hazard striping around the weapon mounts, engine housings, and "
        "exposed moving parts. Maroon guild crests stencilled on the sides. Yellow work lights "
        "in bolted-on metal housings clamped to the structural frame."
    ),
    interior_appearance_description=(
        "The interior has the unfinished, functional quality of a machine rather than a "
        "vessel designed for human habitation. Corridors are wider than expected -- built "
        "for crew with prosthetic limbs that extend further than organic ones. Repair "
        "access panels line every corridor, each with standardized fasteners and "
        "diagnostic sockets. The bridge is a practical arrangement of stations with "
        "prosthetic interface sockets at every position. Crew quarters are small but "
        "include charging stations for powered prosthetics and maintenance kits for "
        "field-level self-repair. The ship smells of lubricant, clean metal, and the "
        "faint electrical ozone of prosthetic systems cycling."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 14}],
    secondary_crew=[{"gunners": 4}],
    additional_systems=[
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
        "Prosthetic charging stations",
        "Crew prosthetic maintenance supplies",
    ],
)

SCABBARD = ShipTemplate(
    name="Scabbard",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=70,
    armor=20,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=60,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Stiletto", 5)],
    short_description="Heavy tender corvette carrying five Stiletto fighters",
    long_description=(
        "The Scabbard carries and supports a detachment of Hyades small craft -- typically "
        "five Stiletto fighters -- extending their operational range. The Scabbard's hangar "
        "is where Hyades modular construction philosophy is most visible: each launch "
        "cradle uses standardized fittings that accept any Hyades small craft type "
        "without modification. A Scabbard that launched Stilettos in the morning can "
        "recover Javelins in the afternoon -- the cradles adjust mechanically, the fuel "
        "lines use universal connections, and the augmented hangar crew can reconfigure "
        "the bay with prosthetic tools that are literally part of their bodies. "
        "The Scabbard is slower than the template tender but substantially tougher, "
        "with armor that protects its embarked craft during the vulnerable launch and "
        "recovery phases."
    ),
    exterior_appearance_description=(
        "A 70-meter military spacecraft with a bare metal hull. A wide, flat rectangular body. "
        "Launch cradles for fighters visible along both sides, the cradle mechanisms and "
        "hydraulic launch arms exposed. Hull plates on the front and underside, but much of "
        "the upper hull is open framework with cable runs and structural ribs visible. A light "
        "ion turret bolted to the top in a welded housing. Engine bells at the rear in exposed "
        "mechanical frames. Weld seams and bolt patterns across every surface. Yellow hazard "
        "striping around the launch cradles and engine housings. Maroon guild crests "
        "stencilled on the sides. Yellow work lights clamped to the structural frame."
    ),
    interior_appearance_description=(
        "The hangar section dominates the aft half -- five launch cradles with universal "
        "fittings, fuel and power connections using standardized couplings, and a repair "
        "bay where augmented technicians work with tools that are part of their arms. An "
        "engineer with a prosthetic hand configured as a torque wrench can service a "
        "launch cradle faster than a baseline crew with a toolbox. The crew section is "
        "compact and functional, with the same exposed-conduit aesthetic as all Hyades "
        "vessels. Prosthetic charging stations in the crew quarters."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[
        {"embarked_craft_pilots": 5},
        {"hangar_technicians": 4},
    ],
    additional_systems=[
        "Hangar bay (5 small craft, universal fittings)",
        "Standardized launch cradles",
        "Craft maintenance bay",
        "Prosthetic interface sockets (all stations)",
        "Prosthetic charging stations",
    ],
)

BALLISTA = ShipTemplate(
    name="Ballista",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Combat Frigate",
    combat_role="Fleet screening / torpedo attack",
    length=185,
    armor=50,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=180,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[weapons.RAILGUN, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavily armored combat frigate with prosthetic maintenance bay",
    long_description=(
        "The Ballista is the Hyades fleet's primary screening combatant -- the most "
        "heavily armored frigate in known space. Armor that would be appropriate on a "
        "light destroyer sits on a frigate hull, and the hull beneath that armor is "
        "built to Hyades industrial standards: thick-gauge structural members, "
        "redundant load paths, standardized repair access throughout. The Ballista "
        "carries the smallest prosthetic maintenance bay in the Hyades fleet -- a "
        "workshop where a technician can repair or replace damaged crew prosthetics "
        "during an engagement. A gunner who loses a prosthetic hand to shrapnel is "
        "pulled from station, given a replacement hand from stores, recalibrated, and "
        "returned to duty. The hand is standardized -- any hand fits any socket. "
        "The Ballista fights in packs, closing to torpedo range through fire that "
        "would destroy lighter frigates. It arrives heavier, slower, and harder to "
        "kill than anything in its weight class."
    ),
    exterior_appearance_description=(
        "A 185-meter military spacecraft with a bare metal hull. A broad rectangular box -- "
        "flat top, flat sides, flat bottom, blunt front. Heavy hull plates on the front and "
        "lower sides, but much of the upper hull and rear is exposed framework -- structural "
        "ribs, cable runs, hydraulic lines, piping, and mechanical joints all visible from "
        "outside. A railgun in a heavy mechanical mount along the top, the gun's cabling and "
        "feed mechanisms exposed. A torpedo bay in the lower front with visible loading "
        "machinery. A heavy laser turret bolted to the top in a welded housing. Engine bells "
        "mounted across the rear in exposed mechanical frames, exhaust piping and fuel lines "
        "visible. Mismatched hull plates in different metal tones where sections have been "
        "replaced at different times. Weld seams, bolt patterns, and clamp fittings across "
        "every surface. Yellow hazard striping around the torpedo bay, engine housings, and "
        "exposed moving parts. Multiple maroon guild crests stencilled on the sides. Ship name "
        "stamped in maroon block lettering on the front. Yellow work lights in bolted-on metal "
        "housings clamped to the structural frame."
    ),
    interior_appearance_description=(
        "The prosthetic maintenance bay is a small workshop amidships -- a room with a "
        "workbench, diagnostic equipment, a rack of standardized replacement parts "
        "(hands, forearms, eyes, interface cables), and the calibration tools that tune "
        "a fresh prosthetic to its new wearer. The technician who runs it can swap a "
        "hand in twenty minutes and have the gunner back at station in thirty. The "
        "bridge is forward, conventional, with prosthetic interface sockets at every "
        "position. The torpedo room is manned by crew whose mechanical arms handle "
        "the heavy lifting of torpedo loading without fatigue. Corridors are lined with "
        "repair access panels. The ship has the industrial, mechanical atmosphere of a "
        "working factory -- because that is what Hyades shipwrights build."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 52}],
    secondary_crew=[
        {"gunners": 14},
        {"torpedo_crew": 6},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Prosthetic maintenance bay (small)",
        "Standardized prosthetic replacement stores",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
        "Reinforced armor plating (heavy gauge)",
    ],
)

PARTISAN = ShipTemplate(
    name="Partisan",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Patrol Frigate",
    combat_role="Commerce protection / independent operations",
    length=168,
    armor=28,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=115,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Independent patrol frigate with prosthetic maintenance and field repair capability",
    long_description=(
        "The Partisan is the Hyades independent operator -- the ship sent to patrol a "
        "system alone for weeks, maintaining law, investigating contacts, and representing "
        "Hyades authority. Slower than the template patrol frigate but tougher, the "
        "Partisan's real advantage is self-sufficiency. Its augmented crew can perform "
        "repairs that would require a dockyard visit for other factions' frigates. A "
        "Hyades engineer with a prosthetic arm socketed into the ship's diagnostic "
        "network can identify a failing power conduit, access it through a standardized "
        "panel, replace it with a modular spare, and have the system back online without "
        "leaving the corridor. The Partisan carries a prosthetic maintenance bay and "
        "enough replacement parts to keep its crew operational for extended solo "
        "deployments. A Partisan captain is the highest-ranking Hyades military officer "
        "in a system, and the ship is built to keep that officer on station longer than "
        "anyone else's patrol frigate."
    ),
    exterior_appearance_description=(
        "A 168-meter military spacecraft with a bare metal hull. A rectangular body with a "
        "flat top, flat sides, and a blunt front. Hull plates on the front and lower hull, "
        "upper hull partially exposed framework -- structural ribs, cable runs, and piping "
        "visible. A particle cannon in a heavy mechanical mount along the top with exposed "
        "cabling. A torpedo bay in the lower front with visible loading machinery. A heavy "
        "laser turret bolted to the top in a welded housing. Engine bells at the rear in "
        "exposed mechanical frames. Mismatched hull plates where sections have been replaced. "
        "Weld seams and bolt patterns across every surface. Yellow hazard striping around the "
        "torpedo bay, engine housings, and exposed machinery. Multiple maroon guild crests "
        "stencilled on the sides. Ship name stamped in maroon block lettering. Yellow work "
        "lights clamped to the frame."
    ),
    interior_appearance_description=(
        "More liveable than the Ballista -- the Partisan is designed for extended solo "
        "deployment. Crew quarters are small but functional, each with a prosthetic "
        "charging station and basic maintenance tools for self-service adjustment. The "
        "wardroom doubles as a briefing room. The prosthetic maintenance bay is slightly "
        "larger than the Ballista's, carrying more replacement stock for the longer "
        "deployments. The ship has the practical, functional domesticity of a place where "
        "augmented people live and work for months at a time -- everything is built for "
        "mechanical hands, every surface can be repaired, every system can be accessed."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 36}],
    secondary_crew=[
        {"gunners": 8},
        {"torpedo_crew": 4},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Prosthetic maintenance bay (small, extended stock)",
        "Standardized prosthetic replacement stores",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
        "Modular spare parts storage",
    ],
)

SPYGLASS = ShipTemplate(
    name="Spyglass",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=190,
    armor=18,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=90,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Hard-jump intelligence frigate with augmented sensor operators",
    long_description=(
        "The Spyglass is the Hyades scout frigate -- a hard-jump-capable vessel built for "
        "deep reconnaissance. Where the Antaren Mirage relies on speed and the Canopan "
        "Bunyip on endurance, the Spyglass relies on its augmented crew. Sensor operators "
        "with synthetic eyes that see across electromagnetic spectra process intelligence "
        "data with a fidelity that baseline eyes cannot match. An operator with a "
        "prosthetic hand socketed into the sensor system's diagnostic interface reads "
        "the raw data stream through haptic feedback -- feeling the electromagnetic "
        "environment rather than watching it on a screen. The Spyglass is slower and "
        "bulkier than other factions' scout frigates, with a higher sensor profile -- "
        "Hyades engineers could not make the ship both tough and invisible. But its "
        "augmented crew extracts more intelligence from each observation pass than "
        "baseline crews, and the ship itself survives detection better than lighter "
        "alternatives."
    ),
    exterior_appearance_description=(
        "A 190-meter military spacecraft with a bare metal hull. A rectangular body with a "
        "blunt front and a cluster of sensor equipment at the front -- antenna masts and "
        "receiver dishes bolted to the hull on welded brackets, their cabling running exposed "
        "along the hull exterior. An ion cannon in a mechanical mount on the top. Hull plates "
        "on the front, sides and upper hull partially exposed framework. Engine bells at the "
        "rear in exposed mechanical frames. Weld seams and bolt patterns across every surface. "
        "Yellow hazard striping around the sensor mounts and engine housings. Maroon guild "
        "crests stencilled on the sides. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The forward section is sensor equipment and an analysis room where augmented "
        "intelligence specialists work with prosthetic interfaces -- hands in diagnostic "
        "sockets, synthetic eyes processing multi-spectrum feeds. The hard-jump drive "
        "occupies the aft section. The prosthetic maintenance bay is included because a "
        "sensor operator who loses a synthetic eye during a months-long deployment loses "
        "their primary capability -- the bay carries replacement optics calibrated for "
        "intelligence work. Living spaces are compressed in the middle, functional and "
        "austere, with the same exposed-conduit aesthetic as all Hyades vessels."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 24}],
    secondary_crew=[
        {"intelligence_analysts": 6},
        {"sensor_specialists": 4},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array",
        "Intelligence analysis suite",
        "Prosthetic maintenance bay (small, sensor optics stock)",
        "Prosthetic interface sockets (sensor stations)",
        "Diagnostic socket network",
    ],
)

GORGET = ShipTemplate(
    name="Gorget",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=162,
    armor=28,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=115,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.PLASMA_CANNON, weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Heavy escort frigate with augmented gunnery and field repair capability",
    long_description=(
        "The Gorget provides a defensive screen over Hyades convoys and transport groups. "
        "Slower than the template escort frigate, the Gorget compensates with armor and "
        "hull integrity that let it absorb fire meant for the ships it protects -- and "
        "then repair the damage while still on station. A Hyades escort frigate that "
        "takes a hull breach has an engineer with prosthetic arms sealed in a vacuum suit "
        "patching the breach with standardized repair plates before the next wave of "
        "bombers arrives. The augmented crew's ability to perform repairs in combat "
        "conditions that would stop baseline crews is the Gorget's hidden advantage. "
        "The ship doesn't just absorb damage -- it heals it, with mechanical hands and "
        "modular parts, faster than the enemy expects."
    ),
    exterior_appearance_description=(
        "A 162-meter military spacecraft with a bare metal hull. A compact rectangular body "
        "with a blunt front and flat sides. Hull plates on the front and lower hull, upper "
        "hull partially exposed framework with cable runs and structural ribs visible. A "
        "plasma cannon in a mechanical mount on the top with exposed cabling. A light ion "
        "turret bolted behind it in a welded housing. Engine bells at the rear in exposed "
        "mechanical frames. Mismatched hull plates where sections have been replaced. Weld "
        "seams and bolt patterns across every surface. Yellow hazard striping around the "
        "weapon mounts and engine housings. Maroon guild crests stencilled on the sides. Ship "
        "name stamped in maroon block lettering. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The bridge is forward, with prosthetic interface sockets at every gunnery and "
        "command position. The plasma cannon's power feeds route through accessible "
        "channels where augmented engineers can reach them mid-combat. The prosthetic "
        "maintenance bay is amidships. Standardized repair plates and spare hull sections "
        "are racked in the engineering section -- ready to be grabbed by a mechanical "
        "hand and welded into place over a breach. The ship is built to be fixed while "
        "it fights."
    ),
    minimum_crew=[{"officers": 7}, {"crew": 32}],
    secondary_crew=[
        {"gunners": 10},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Prosthetic maintenance bay (small)",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Field repair plate storage",
        "Diagnostic socket network",
    ],
)

RAMPART = ShipTemplate(
    name="Rampart",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=270,
    armor=65,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=330,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Massively armored fleet destroyer with augmented repair crews",
    long_description=(
        "The Rampart is the shield of the Hyades battle fleet -- a fleet destroyer with "
        "armor that belongs on a cruiser. Its job is protecting capital ships from bomber "
        "and torpedo attacks, and it does this through triple point defense turrets backed "
        "by armor that lets it stay on station while absorbing fire that would force "
        "lighter destroyers to withdraw. The Rampart's augmented damage control crews "
        "are its defining feature at this scale: engineers with prosthetic arms socketed "
        "into the ship's repair network, feeling damage through haptic feedback and "
        "directing modular repair teams to breaches and system failures with the speed "
        "of thought. A Rampart that takes a railgun hit through the port armor has an "
        "augmented repair crew cutting away the damaged plate, replacing it with a "
        "standardized section from stores, and welding it into place while the next "
        "salvo is still incoming. The ship repairs itself while it fights, faster than "
        "any baseline crew could manage."
    ),
    exterior_appearance_description=(
        "A 270-meter military spacecraft with a bare metal hull. A broad, heavy rectangular "
        "body -- flat on all six faces. Heavy hull plates on the front and lower hull, but "
        "large sections of the sides and top are exposed framework -- structural ribs, cable "
        "runs, hydraulic lines, piping, and mechanical joints visible. A railgun in a heavy "
        "mechanical mount along the top with exposed feed mechanisms. Three heavy laser "
        "turrets bolted to the hull in welded housings -- one on top, two on the sides. Engine "
        "bells in a rectangular cluster at the rear in exposed mechanical frames, fuel lines "
        "and exhaust piping visible. Mismatched hull plates in different metal tones. Weld "
        "seams, bolt patterns, and clamp fittings everywhere. Yellow hazard striping around "
        "every weapon mount, engine housing, and exposed moving part. Multiple maroon guild "
        "crests stencilled on the sides. Ship name stamped in maroon block lettering on the "
        "front. Yellow work lights in bolted-on housings across the hull."
    ),
    interior_appearance_description=(
        "The three point defense battery stations are distributed port, starboard, and "
        "dorsal, each with prosthetic interface sockets for augmented gunners. The "
        "prosthetic maintenance bay is expanded -- two technicians maintaining the crew's "
        "augmentation during sustained combat. The modular repair system is the ship's "
        "most distinctive feature: standardized hull plates, conduit sections, and "
        "system modules stored in racks throughout the ship, accessible to augmented "
        "repair crews through panels that open with a twist of a mechanical wrist. The "
        "bridge is forward, conventional, built to last. The ship feels like a factory "
        "that happens to carry weapons."
    ),
    minimum_crew=[{"officers": 16}, {"crew": 100}],
    secondary_crew=[
        {"gunners": 30},
        {"point_defense_crew": 25},
        {"prosthetic_technicians": 2},
    ],
    additional_systems=[
        "Prosthetic maintenance bay (expanded)",
        "Modular repair system (standardized hull plates and conduit)",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
        "Field repair plate and conduit storage",
        "Reinforced armor plating (heavy gauge)",
    ],
)

COURSER = ShipTemplate(
    name="Courser",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=255,
    armor=48,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=275,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Heavy pursuit destroyer with augmented crew and superior endurance",
    long_description=(
        "The Courser is the Hyades pursuit ship -- slower than the template but "
        "substantially tougher, with the field repair capability that defines Hyades "
        "doctrine. The Courser does not run targets down through speed. Like the Canopan "
        "Thunderbird, it pursues through endurance -- following contacts through medium "
        "jump points, maintaining operational readiness through sustained self-repair, "
        "and arriving at the engagement heavier and in better condition than the target "
        "expects. A Courser that has been pursuing a target for a week is in nearly the "
        "same condition it was when the chase began, because its augmented crew has been "
        "repairing accumulated wear throughout the pursuit. The target, in contrast, has "
        "been accumulating damage with no ability to repair it. When the engagement "
        "comes, the Courser is fresh and the target is not. Coursers often operate in "
        "pairs for mutual support."
    ),
    exterior_appearance_description=(
        "A 255-meter military spacecraft with a bare metal hull. A rectangular body with a "
        "blunt front -- narrow in proportion, elongated. Hull plates on the "
        "front and lower hull, upper hull and sides partially exposed framework. A heavy "
        "particle cannon in a mechanical mount extending from the front, the cannon's power "
        "cabling and cooling lines exposed along the hull. A torpedo bay in the lower front "
        "with visible loading machinery. An ion turret bolted to the top. Engine bells at the "
        "rear in exposed mechanical frames. Mismatched hull plates. Weld seams and bolt "
        "patterns across every surface. Yellow hazard striping around the cannon mount, "
        "torpedo bay, and engine housings. Maroon guild crests stencilled on the sides. Ship "
        "name stamped in maroon block lettering. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "Designed for the sustained pursuit. Crew quarters are functional, with "
        "prosthetic charging stations and self-maintenance kits. The torpedo room is "
        "forward, crewed by augmented ratings whose mechanical arms handle the heavy "
        "lifting. The prosthetic maintenance bay carries extended stock for the longer "
        "deployments. The modular repair system lets the augmented crew maintain the "
        "ship continuously during pursuit -- a rolling maintenance cycle that keeps "
        "every system at operational readiness. The ship has the steady, patient "
        "atmosphere of something built to keep working indefinitely."
    ),
    minimum_crew=[{"officers": 14}, {"crew": 78}],
    secondary_crew=[
        {"gunners": 18},
        {"torpedo_crew": 6},
        {"prosthetic_technicians": 2},
    ],
    additional_systems=[
        "Prosthetic maintenance bay (expanded, extended stock)",
        "Modular repair system",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
    ],
)

BOMBARD = ShipTemplate(
    name="Bombard",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Siege Destroyer",
    combat_role="Anti-capital firepower on a destroyer hull",
    length=240,
    armor=28,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=170,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[weapons.SIEGE_CANNON],
    default_small_craft=[],
    short_description="Armored siege cannon platform with augmented gunnery crew",
    long_description=(
        "The Bombard mounts a siege cannon on a destroyer hull -- but unlike other "
        "factions' siege destroyers, the Hyades version carries meaningful armor around "
        "the weapon and crew spaces. The Bombard is still fragile relative to a fleet "
        "destroyer, but its augmented crew can perform emergency repairs on the siege "
        "cannon's systems under fire -- an engineer with a prosthetic arm socketed into "
        "the weapon's diagnostic network feels a capacitor failure before it registers "
        "on instruments and reroutes power with mechanical precision. The siege cannon's "
        "loading cycle requires significant physical labor, handled by augmented crew "
        "whose prosthetic arms do not tire under the repetitive strain of feeding "
        "magnetic accelerator rounds into the breach. A Bombard crew can sustain a "
        "higher rate of fire over a longer engagement than baseline crews."
    ),
    exterior_appearance_description=(
        "A 240-meter military spacecraft with a bare metal hull. A squat, reinforced "
        "rectangular body dominated by a massive siege cannon in a heavy mechanical mount "
        "running the full length of the top -- the cannon's feed mechanisms, power cabling, "
        "and recoil dampeners all exposed. The hull beneath is a thick rectangular frame with "
        "heavy hull plates on the front and sides. Engine bells at the rear in reinforced "
        "mechanical frames. Weld seams, bolt patterns, and heavy clamp fittings across every "
        "surface. Yellow hazard striping along the cannon mount, around the engine housings, "
        "and around every exposed mechanism. Maroon guild crests stencilled on the sides. Ship "
        "name stamped in maroon block lettering. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The ship is built around the weapon. The siege cannon's magnetic accelerator "
        "runs the full length, with crew spaces and the prosthetic maintenance bay "
        "packed into the remaining volume. The gun crew work in the loading section "
        "with prosthetic arms that handle the heavy rounds without fatigue -- mechanical "
        "muscles doing work that would exhaust organic ones in hours. The diagnostic "
        "socket network runs through the weapon system, letting augmented engineers "
        "monitor the cannon's health through haptic feedback. The bridge is a cramped "
        "forward compartment. The ship exists to fire its cannon, and everything aboard "
        "serves that purpose."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 45}],
    secondary_crew=[
        {"gunnery_specialists": 10},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Spinal siege cannon mount",
        "Prosthetic maintenance bay (small)",
        "Prosthetic interface sockets (gunnery stations)",
        "Siege cannon diagnostic socket network",
        "Reinforced weapon housing armor",
    ],
)

ONAGER = ShipTemplate(
    name="Onager",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=460,
    armor=88,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=540,
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
    short_description="Maximum-armor line cruiser with industrial repair capability",
    long_description=(
        "The Onager is the Hyades main line combatant and the most heavily armored "
        "cruiser in known space. Where the Canopan Megalania absorbs damage through "
        "hull points and the Antaren Typhoon evades it through speed, the Onager simply "
        "bounces fire that would penetrate other cruisers' armor. Hits that reach the "
        "hull are repaired by augmented damage control crews working through the modular "
        "repair system -- standardized plates cut and welded by prosthetic hands, damaged "
        "conduit replaced with modular sections, failed systems swapped out with spares "
        "from stores. The Onager's prosthetic workshop is a full facility capable of "
        "rebuilding a crew member's augmentation from components. Over the course of a "
        "prolonged engagement, the Onager maintains combat effectiveness not through "
        "the Canopan method of replacing dead crew with shells, but through the Hyades "
        "method of replacing damaged ship with spare parts. The crew stays the same. "
        "The ship around them is rebuilt, piece by piece, while they fight."
    ),
    exterior_appearance_description=(
        "A 460-meter military spacecraft with a bare metal hull. A massive rectangular body -- "
        "flat on all six faces, squared off at every edge. Heavy hull plates on the front and "
        "lower hull, but large sections of the sides, top, and rear are exposed framework -- "
        "structural ribs, cable runs, hydraulic lines, piping, mechanical joints, and "
        "cross-bracing all visible. A precision railgun in a heavy mechanical mount along the "
        "top with exposed feed mechanisms. Weapon batteries in mechanical mounts along both "
        "sides, their power cabling running exposed along the hull. Point-defense turrets "
        "bolted to the hull in welded housings. Engine bells across the rear in exposed "
        "mechanical frames, fuel lines and exhaust piping visible. Mismatched hull plates in "
        "different metal tones. Weld seams, bolt patterns, and clamp fittings everywhere. "
        "Yellow hazard striping around every weapon mount, engine housing, and exposed moving "
        "part. Multiple maroon guild crests stencilled on the sides. Ship name stamped in "
        "maroon block lettering at large scale on the front. Yellow work lights in bolted-on "
        "housings across the hull."
    ),
    interior_appearance_description=(
        "The prosthetic workshop is a full manufacturing facility amidships -- workbenches, "
        "diagnostic equipment, component fabricators, and racks of standardized prosthetic "
        "parts. The workshop can rebuild a hand, recalibrate an eye, or replace an entire "
        "forearm assembly from components. The modular repair system is the ship's most "
        "impressive feature: entire hull sections can be replaced in the field by "
        "augmented repair crews working through the standardized access system. Damaged "
        "plate is cut away, a fresh section is pulled from stores, and prosthetic hands "
        "weld it into place. The bridge is a reinforced compartment forward with "
        "prosthetic interface sockets at every station. Crew quarters are functional, "
        "each with charging stations and maintenance tools. The ship has the industrial "
        "atmosphere of a factory that fights."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 40}, {"crew": 320}],
    secondary_crew=[
        {"gunners": 65},
        {"point_defense_crew": 25},
        {"prosthetic_technicians": 4},
        {"repair_fabricators": 8},
    ],
    additional_systems=[
        "Prosthetic workshop (full facility)",
        "Component fabrication equipment",
        "Standardized prosthetic replacement stores (extensive)",
        "Modular repair system (hull sections, conduit, systems)",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
        "Field repair plate and section storage",
        "Reinforced armor plating (maximum gauge)",
    ],
)

CORVUS = ShipTemplate(
    name="Corvus",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=425,
    armor=64,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=380,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=49,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy medium-jump cruiser for sustained flanking operations",
    long_description=(
        "The Corvus is the largest Hyades combat ship that can use medium jump points "
        "and the backbone of their flanking forces. Slower than the template light "
        "cruiser but substantially tougher, the Corvus arrives at a flanking position "
        "later than other factions' equivalents -- but arrives in condition to hold that "
        "position indefinitely. A Hyades flanking force led by a Corvus does not hit "
        "and run. It hits and stays. The Corvus's modular repair system and augmented "
        "crew mean it can sustain operations in a contested flanking position, repairing "
        "battle damage between engagements, maintaining its combat effectiveness across "
        "days of sustained action. Other factions' flanking cruisers either win quickly "
        "or withdraw. The Corvus digs in."
    ),
    exterior_appearance_description=(
        "A 425-meter military spacecraft with a bare metal hull. A rectangular body -- "
        "narrower and longer in proportion. Heavy hull plates on the front and lower hull, "
        "upper hull and sides partially exposed framework with structural ribs and cable runs "
        "visible. A heavy railgun in a mechanical mount along the top with exposed cabling. "
        "Two laser turrets bolted to the upper hull in welded housings. Engine bells at the "
        "rear in exposed mechanical frames. Mismatched hull plates. Weld seams and bolt "
        "patterns across every surface. Yellow hazard striping around weapon mounts and engine "
        "housings. Multiple maroon guild crests stencilled on the sides. Ship name stamped in "
        "maroon block lettering. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The interior reflects the ship's role as a sustained flanking combatant. The "
        "prosthetic workshop is full-sized, amidships. The modular repair system carries "
        "extensive stores -- enough to replace major hull sections during extended "
        "operations away from a dockyard. A task force coordination section includes "
        "additional stations for managing a flanking group. Crew quarters are functional "
        "and austere, with the prosthetic charging stations and self-maintenance kits "
        "standard on all Hyades vessels. The ship has the settled, heavy atmosphere of "
        "something built to be somewhere difficult and stay there."
    ),
    minimum_crew=[{"senior_officers": 6}, {"officers": 30}, {"crew": 250}],
    secondary_crew=[
        {"gunners": 40},
        {"point_defense_crew": 15},
        {"prosthetic_technicians": 3},
        {"repair_fabricators": 6},
        {"task_force_staff": 8},
    ],
    additional_systems=[
        "Prosthetic workshop (full facility)",
        "Modular repair system (extensive stores)",
        "Task force coordination suite",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
        "Diagnostic socket network",
    ],
)

FORTRESS = ShipTemplate(
    name="Fortress",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=990,
    armor=100,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1950,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=70,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Maximum-armor battleship with industrial repair capability",
    long_description=(
        "The Fortress is the Hyades battleship -- the most heavily armored capital ship "
        "in known space short of a dreadnought. It carries armor rated at 100 -- matching "
        "the plate thickness of other factions' dreadnoughts on a battleship hull. The "
        "Fortress is slower than the template battleship, arriving at the engagement "
        "later, but arriving in a condition that makes it nearly impossible to kill "
        "through conventional fire. Its augmented repair crews operate at industrial "
        "scale -- hundreds of engineers with prosthetic arms socketed into the ship's "
        "repair network, replacing damaged hull sections, rerouting failed systems, and "
        "rebuilding weapon mounts while the ship fights. A Fortress under sustained fire "
        "repairs damage as fast as many ships take it. The modular construction means "
        "every component is replaceable, every system has a spare, and the augmented "
        "crew can swap them faster than baseline humans. The enemy sees a battleship "
        "they cannot kill. Over the course of a prolonged engagement, the Fortress "
        "simply outlasts whatever is shooting at it."
    ),
    exterior_appearance_description=(
        "A 990-meter military spacecraft with a bare metal hull. A massive rectangular slab -- "
        "flat on all six faces, squared off at every edge. Heavy hull plates on the front "
        "face, but much of the hull is exposed framework -- structural ribs, cable runs, "
        "hydraulic lines, piping, cross-bracing, and mechanical joints visible across the "
        "sides, top, and rear. A gauss cannon in a massive mechanical mount along the top, the "
        "cannon's feed mechanisms and power cabling exposed. Weapon batteries in mechanical "
        "mounts along both sides in two tiers, power cabling running exposed between tiers. "
        "Point-defense turrets bolted to the hull in welded housings. Engine bells in a "
        "rectangular grid across the rear face in exposed mechanical frames. Mismatched hull "
        "plates in different metal tones across every plated section. Weld seams, bolt "
        "patterns, and heavy clamp fittings everywhere. Yellow hazard striping around every "
        "weapon mount, engine housing, and exposed mechanism. Multiple maroon guild crests "
        "stencilled on the sides. Ship name stamped in maroon block lettering at large scale "
        "on the front. Yellow work lights in bolted-on housings across the hull."
    ),
    interior_appearance_description=(
        "The prosthetic manufacturing facility is a full industrial section -- fabrication "
        "equipment, component assembly lines, calibration stations, and extensive stores "
        "of prosthetic components and raw materials. The modular repair system operates "
        "at industrial scale: entire weapon mounts can be swapped, hull sections replaced, "
        "power systems rebuilt from modular components. Augmented repair crews work in "
        "shifts, maintaining a continuous repair cycle during sustained combat. The bridge "
        "is a reinforced command amphitheater with prosthetic interface sockets at every "
        "station. Crew quarters are functional, each with charging stations. Living "
        "spaces have the industrial, unfinished feel of a factory -- because the ship "
        "is one."
    ),
    minimum_crew=[{"senior_officers": 20}, {"officers": 120}, {"crew": 1500}],
    secondary_crew=[
        {"gunners": 200},
        {"point_defense_crew": 100},
        {"prosthetic_technicians": 12},
        {"repair_fabricators": 30},
        {"medical": 25},
    ],
    additional_systems=[
        "Prosthetic manufacturing facility (industrial)",
        "Component fabrication lines",
        "Modular repair system (industrial scale)",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels (all decks)",
        "Diagnostic socket network (ship-wide)",
        "Hull section and component storage (extensive)",
        "Reinforced armor plating (dreadnought-grade)",
    ],
)

ARSENAL = ShipTemplate(
    name="Arsenal",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1300,
    armor=65,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1500,
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
        ("Javelin", 10),
        ("Javelin", 10),
        ("Stiletto", 10),
        ("Cutlass", 10),
    ],
    short_description="Heavily armored carrier with modular hangar bays and augmented deck crews",
    long_description=(
        "The Arsenal is the Hyades fleet carrier -- slower than any other faction's "
        "equivalent but tougher, with hangar bays designed around the same modular "
        "philosophy that defines all Hyades construction. The standardized launch "
        "cradles accept any Hyades small craft type without modification, and the "
        "augmented hangar crews rearm and repair embarked craft faster than baseline "
        "crews using tools that are part of their bodies. An engineer with a prosthetic "
        "hand configured as a power driver services a Stiletto's plasma launcher in "
        "half the time a baseline crew with hand tools would need. The Arsenal deploys "
        "four wings -- typically two wings of Javelin bombers, one of Stiletto fighters, "
        "and one of Cutlass gunships -- a strike package optimized for the Hyades doctrine "
        "of toughness. Every craft in the Arsenal's hangar is heavier and harder to kill "
        "than its equivalent from other factions. Medium-jump capable, allowing it to "
        "project strike power through flanking routes."
    ),
    exterior_appearance_description=(
        "A 1300-meter military spacecraft with a bare metal hull. A massive rectangular box -- "
        "flat on all six faces, squared off at every edge. Heavy hull plates on the front "
        "face, but large sections of the hull are exposed framework -- structural ribs, cable "
        "runs, hydraulic lines, cross-bracing visible. Hangar openings cut into the sides "
        "behind heavy blast doors, the door mechanisms and hydraulic arms exposed. Interior "
        "hangar lighting visible within. Laser turrets bolted to the hull in welded housings. "
        "Engine bells in a rectangular grid across the rear face in exposed mechanical frames. "
        "Mismatched hull plates in different metal tones. Weld seams, bolt patterns, and clamp "
        "fittings everywhere. Yellow hazard striping around every hangar opening, engine "
        "housing, and exposed mechanism. Multiple maroon guild crests stencilled on the sides. "
        "Ship name stamped in maroon block lettering at large scale on the front. Yellow work "
        "lights in bolted-on housings across the hull."
    ),
    interior_appearance_description=(
        "The four hangar bays are the ship's defining spaces -- vast industrial halls "
        "where forty strike craft sit in standardized launch cradles with universal "
        "fittings. Augmented deck crews work with prosthetic tools that are part of "
        "their bodies: hands configured as wrenches, power drivers, and calibration "
        "instruments. The turnaround cycle is fast and mechanical. The craft maintenance "
        "bay includes component fabrication equipment for building replacement parts "
        "from raw stock. The prosthetic manufacturing facility maintains the thousands "
        "of crew aboard. Living spaces are extensive, functional, and industrial -- the "
        "Hyades aesthetic scaled to capital proportions."
    ),
    minimum_crew=[{"senior_officers": 30}, {"officers": 200}, {"crew": 3000}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"flight_deck_crew": 180},
        {"hangar_technicians": 100},
        {"ship_gunners": 40},
        {"prosthetic_technicians": 10},
        {"repair_fabricators": 20},
        {"medical": 40},
    ],
    additional_systems=[
        "Hangar bays (x4, 10 craft each, universal fittings)",
        "Standardized launch cradles",
        "Craft maintenance and rearm facilities",
        "Craft component fabrication equipment",
        "Prosthetic manufacturing facility (industrial)",
        "Modular repair system (industrial scale)",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels (all decks)",
        "Diagnostic socket network (ship-wide)",
        "Reinforced hangar armor",
    ],
)

ACROPOLIS = ShipTemplate(
    name="Acropolis",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=2000,
    armor=100,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=3400,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=84,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Maximum-armor dreadnought with industrial repair and augmented crew of thousands",
    long_description=(
        "The Acropolis is the largest and most powerful vessel in the Hyades fleet -- and "
        "the hardest ship to kill in known space. Maximum armor, hull integrity that "
        "exceeds even the Canopan Mammoth, and an augmented crew that repairs damage "
        "faster than any other dreadnought's crew can manage. The Acropolis does not "
        "rely on the Mammoth's strategy of replacing dead crew with reanimated shells. "
        "It relies on the Hyades strategy of keeping the ship intact around living crew "
        "who fix it as fast as it breaks. An Acropolis under sustained fire is a factory "
        "in overdrive -- hundreds of augmented engineers with prosthetic arms socketed "
        "into the repair network, replacing hull sections, rerouting damaged systems, "
        "and rebuilding weapon mounts with mechanical precision while the siege cannons "
        "continue firing. The modular construction means every part of the ship is "
        "replaceable from stores. The augmented crew means the replacement happens at "
        "a speed that baseline humans cannot match. A Hyades Acropolis that has been "
        "fighting for a day looks like it has been fighting for an hour. Only a handful "
        "exist. Each one is the oldest ship in the fleet -- rebuilt hundreds of times, "
        "every component replaced many times over, the ship of Theseus made literal "
        "and armored."
    ),
    exterior_appearance_description=(
        "A 2000-meter military spacecraft with a bare metal hull. A massive rectangular slab "
        "-- flat on all six faces, squared off at every edge. Heavy hull plates across the front face and lower hull, but enormous "
        "sections of the sides, top, and rear are exposed framework -- structural ribs the "
        "size of buildings, cable runs as thick as corridors, hydraulic lines, piping, "
        "cross-bracing, and mechanical joints all visible. Twin siege cannons in massive "
        "mechanical mounts along the top, their feed mechanisms, power cabling, and recoil "
        "dampeners exposed. Point-defense turrets bolted to the hull in welded housings at "
        "regular intervals. Engine bells in a large rectangular grid across the rear face in "
        "exposed mechanical frames, fuel lines and exhaust piping visible. Mismatched hull "
        "plates in different metal tones across every plated section. Weld seams, bolt "
        "patterns, and heavy clamp fittings everywhere. Yellow hazard striping around every "
        "weapon mount, engine housing, and exposed mechanism. Numerous maroon guild crests "
        "stencilled across the sides. Ship name stamped in maroon block lettering at massive "
        "scale on the front. Yellow work lights in bolted-on housings across the entire hull."
    ),
    interior_appearance_description=(
        "The Acropolis is a factory. The prosthetic manufacturing facility is a full "
        "industrial section -- fabrication lines, component assembly, calibration "
        "stations, and raw material stores. The modular repair system operates on a "
        "scale that is essentially continuous shipbuilding: hull sections are fabricated, "
        "installed, damaged, removed, and replaced in a cycle that never stops. The "
        "augmented repair crews work in shifts around the clock, maintaining every "
        "system on the ship. The bridge is a vast command amphitheater with prosthetic "
        "interface sockets at every station. Living spaces are extensive -- the Acropolis "
        "carries thousands and must function as a self-contained industrial community. "
        "Crew quarters include full prosthetic maintenance stations. The ship has the "
        "atmosphere of a place where everything is being built, repaired, replaced, and "
        "rebuilt -- because it is, constantly, by people whose bodies have undergone the "
        "same process."
    ),
    minimum_crew=[{"senior_officers": 55}, {"officers": 380}, {"crew": 5800}],
    secondary_crew=[
        {"gunners": 300},
        {"point_defense_crew": 60},
        {"fleet_coordination_staff": 60},
        {"prosthetic_technicians": 25},
        {"repair_fabricators": 80},
        {"medical": 80},
    ],
    additional_systems=[
        "Prosthetic manufacturing facility (industrial, fleet-scale)",
        "Component fabrication lines (continuous production)",
        "Modular repair system (industrial scale, continuous cycle)",
        "Prosthetic interface sockets (all stations, all decks)",
        "Standardized repair access panels (all decks)",
        "Diagnostic socket network (ship-wide)",
        "Hull section and component storage (extensive)",
        "Raw material stores (fabrication stock)",
        "Twin spinal siege cannon mounts",
        "Reinforced armor plating (maximum rating)",
    ],
)

COURIER = ShipTemplate(
    name="Courier",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Supply Runner",
    combat_role="Fast resupply through medium jump points",
    length=115,
    armor=22,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=85,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Armored supply runner carrying ammunition, spare parts, and prosthetic components",
    long_description=(
        "The Courier is the Hyades fast supply vessel -- a medium-jump-capable ship that "
        "delivers ammunition, modular repair components, and prosthetic replacement parts "
        "to forward-deployed task forces. The Courier carries standardized repair "
        "components -- hull plates, conduit sections, system modules -- that Hyades ships "
        "consume as they repair themselves in the field. It also carries prosthetic "
        "replacement stock: hands, arms, eyes, interface cables, and the calibration "
        "equipment that makes them work. A Hyades task force without Courier resupply "
        "eventually runs out of spare parts, and a fleet that can't repair itself loses "
        "its defining advantage. The Courier is tougher than other factions' supply "
        "runners -- Hyades engineers refused to build a thin-skinned ship even for "
        "logistics duty. Speed is maintained at template because even Hyades planners "
        "recognize that a supply runner needs to be fast."
    ),
    exterior_appearance_description=(
        "A 115-meter military spacecraft with a bare metal hull. A long, narrow rectangular "
        "body -- a small crew module at the front and a long cargo midsection with loading "
        "hatches along the sides. Hull plates on the front module, but the cargo midsection is "
        "partially exposed framework with cable runs and structural ribs visible between the "
        "hatches. An ion turret bolted to the top of the crew module. Engine bells at the rear "
        "in exposed mechanical frames. Weld seams across every surface. Yellow hazard striping "
        "around the loading hatches and engine housings. Maroon guild crests stencilled on the "
        "sides. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The interior is mostly cargo space -- modular containers of ammunition, repair "
        "components, hull sections, system modules, and the sealed cases of prosthetic "
        "replacement parts that are the Courier's most specialized cargo. The prosthetic "
        "stores are organized by type and calibration -- a Courier's quartermaster can "
        "locate and deliver a specific hand model or optic calibration in minutes. Crew "
        "spaces forward are functional and compact."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 10}],
    secondary_crew=[{"cargo_handlers": 6}],
    additional_systems=[
        "Modular cargo system",
        "Prosthetic replacement stores",
        "Repair component storage (standardized)",
        "Prosthetic interface sockets (bridge)",
    ],
)

MUSETTE = ShipTemplate(
    name="Musette",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Logistics Corvette",
    combat_role="Emergency resupply / hard-jump logistics",
    length=64,
    armor=14,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=50,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump logistics corvette carrying repair components to deep operations",
    long_description=(
        "The Musette is the smallest dedicated logistics vessel in the Hyades fleet, "
        "built around a hard-jump drive. It carries limited supplies -- enough to "
        "resupply a Spyglass scout frigate operating deep behind enemy lines. The "
        "Musette's most critical cargo is standardized repair components and prosthetic "
        "replacement parts. A Hyades ship operating deep without resupply eventually "
        "depletes its repair stores, and an augmented crew without spare prosthetic "
        "components gradually loses capability as their hardware degrades. The Musette "
        "keeps deep operations functional in both senses -- supplying ammunition and "
        "food for the ship, and the modular parts that keep both ship and crew in "
        "working order. Heavier than the template logistics corvette because Hyades "
        "engineers do not build thin ships."
    ),
    exterior_appearance_description=(
        "A 64-meter military spacecraft with a bare metal hull. A compact rectangular box -- a "
        "small bridge section at the front, the majority of the hull given to cargo space. "
        "Loading hatches on the sides, their hinge mechanisms and hydraulic arms exposed. Hull "
        "plates on the front, upper hull partially exposed framework. A light ion turret "
        "bolted to the top. Engine bells at the rear in exposed mechanical frames. Weld seams "
        "and bolt patterns across every surface. Yellow hazard striping around the loading "
        "hatches and engine housings. A maroon guild crest stencilled on both sides. Yellow "
        "work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The hard-jump drive and cargo hold consume most of the interior. Crew spaces "
        "are minimal -- bunks, a tiny galley, and a bridge barely large enough for three "
        "stations. The cargo hold carries sealed containers of ammunition, food, repair "
        "components, and prosthetic parts organized for rapid delivery. The ship has the "
        "spartan, functional feel of a tool designed for a job."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 6}],
    secondary_crew=[{"cargo_handlers": 2}],
    additional_systems=[
        "Hard-jump drive",
        "Sealed cargo system",
        "Prosthetic replacement stores (compact)",
        "Repair component storage (standardized)",
    ],
)

SMITHY = ShipTemplate(
    name="Smithy",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CRUISER,
    ship_archetype="Field Support Ship",
    combat_role="Heavy repair / prosthetic manufacturing / fleet maintenance hub",
    length=500,
    armor=55,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=440,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Dedicated repair and prosthetic manufacturing ship -- the heart of Hyades fleet maintenance",
    long_description=(
        "The Smithy is the keystone of Hyades fleet doctrine. Where the Canopan Ammonite "
        "processes the fleet's dead into shells, the Smithy processes the fleet's damage "
        "into repaired ships. It carries the largest repair and fabrication facility "
        "outside of a dockyard, capable of manufacturing hull sections, weapon components, "
        "power systems, and prosthetic parts from raw materials. Damaged ships across the "
        "task force dock with the Smithy or receive repair teams by shuttle, and the "
        "Smithy's augmented fabrication crews build whatever is needed. The ship also "
        "carries the fleet's prosthetic manufacturing capability -- producing replacement "
        "limbs, organs, and interface components for crew across the task force who have "
        "lost or damaged their augmentation. A task force with a Smithy attached fights "
        "fundamentally differently than one without -- the fleet's ships repair faster, "
        "stay operational longer, and the augmented crew maintain peak capability because "
        "damaged prosthetics are replaced rather than endured. The Smithy also serves as "
        "a cannibalization hub: components salvaged from ships too damaged to repair are "
        "processed, standardized, and redistributed to ships that need them. Nothing is "
        "wasted."
    ),
    exterior_appearance_description=(
        "A 500-meter military spacecraft with a bare metal hull. A wide rectangular body with "
        "a prominent workshop and repair bay section amidships -- large access doors along "
        "both sides, the door mechanisms exposed, the interior lit with yellow work lights "
        "visible from outside. Docking clamps and mechanical transfer arms along both sides, "
        "their hydraulics and cabling exposed. An ion cannon in a mechanical mount on the top. "
        "Two point-defense turrets bolted to the sides. Hull plates on the front, much of the "
        "hull exposed framework. Engine bells at the rear in exposed mechanical frames. Weld "
        "seams, bolt patterns, and clamp fittings everywhere. Yellow hazard striping around "
        "every door, docking clamp, and engine housing. Multiple maroon guild crests "
        "stencilled on the sides. Ship name stamped in maroon block lettering. Yellow work "
        "lights in bolted-on housings across the hull."
    ),
    interior_appearance_description=(
        "The Smithy's interior is a factory. The main fabrication bay occupies the central "
        "third -- a large industrial space with fabrication equipment, assembly lines, raw "
        "material stores, and the augmented fabrication crews who can build a hull section "
        "from stock metal or a prosthetic hand from component parts. The prosthetic "
        "manufacturing section produces replacement limbs, eyes, interface cables, and "
        "spinal assemblies for fleet-wide distribution. The repair bay handles ship-to-ship "
        "work -- augmented repair crews shuttle to damaged vessels or work through docking "
        "connections, carrying fabricated components to where they're needed. The "
        "cannibalization section processes salvaged components from damaged ships, "
        "stripping them to usable parts. Medical facilities for the living crew are "
        "competent but secondary to the repair mission. The ship smells of metal, "
        "lubricant, and the hot ozone of fabrication equipment running at capacity."
    ),
    minimum_crew=[{"officers": 25}, {"crew": 150}],
    secondary_crew=[
        {"repair_fabricators": 40},
        {"prosthetic_manufacturers": 15},
        {"prosthetic_technicians": 10},
        {"salvage_specialists": 12},
        {"medical": 15},
    ],
    additional_systems=[
        "Main fabrication bay (hull sections, weapon components, systems)",
        "Prosthetic manufacturing section (limbs, optics, interfaces)",
        "Component assembly lines",
        "Raw material stores (fabrication stock)",
        "Ship-to-ship repair docking ports",
        "Salvage and cannibalization section",
        "Repair shuttle bay",
        "Prosthetic interface sockets (all stations)",
        "Standardized repair access panels",
    ],
)

BELFRY = ShipTemplate(
    name="Belfry",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=740,
    armor=90,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1350,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Maximum-armor troop transport with augmented ground forces",
    long_description=(
        "The Belfry delivers a Hyades ground force into hostile space -- and that ground "
        "force is augmented. Hyades marines with prosthetic limbs, reinforced skeletal "
        "structures, and synthetic organs that shrug off wounds that would incapacitate "
        "baseline soldiers. The Belfry itself is the most heavily armored assault "
        "transport in known space, surviving the approach into contested territory through "
        "plate thickness that makes point defense fire ineffective. The ship carries "
        "vehicles, heavy weapons, prefabricated fortifications, and the field prosthetic "
        "manufacturing capability that lets a Hyades ground force maintain its augmented "
        "troops' hardware in the field. A Hyades marine who loses a prosthetic arm in "
        "combat receives a replacement from the Belfry's field fabrication bay and "
        "returns to the line. The Belfry also carries the standardized repair components "
        "that let a Hyades invasion force dig in and fortify faster than baseline troops -- "
        "augmented engineers with prosthetic tools building prefabricated defenses at "
        "mechanical speed."
    ),
    exterior_appearance_description=(
        "A 740-meter military spacecraft with a bare metal hull. A massive rectangular box "
        "with a blunt front. Heavy hull plates on the front face. The sides and top are "
        "partially exposed framework -- structural ribs, cable runs, and piping visible. A "
        "particle cannon in a mechanical mount on the top with exposed cabling. The midsection "
        "is a massive troop and vehicle bay with large loading ramps on the underside and "
        "rear, the ramp mechanisms and hydraulic arms exposed. Point-defense turrets bolted to "
        "the hull in welded housings along the sides and top. Engine bells across the rear in "
        "exposed mechanical frames. Weld seams, bolt patterns, and clamp fittings everywhere. "
        "Yellow hazard striping around the loading ramps, weapon mounts, and engine housings. "
        "Multiple maroon guild crests stencilled on the sides. Ship name stamped in maroon "
        "block lettering. Yellow work lights in bolted-on housings across the hull."
    ),
    interior_appearance_description=(
        "The troop decks are vast compartments with bunks and prosthetic charging stations "
        "for the augmented marines. Vehicle bays on the lower decks carry armored "
        "transports and heavy weapons. A field prosthetic fabrication bay can produce "
        "replacement components for the ground force's augmentation. The deployment bays "
        "are built for rapid disembarkation -- doors open, ramps extend, and augmented "
        "troops advance with the mechanical endurance that defines Hyades infantry. "
        "The ship has the industrial, heavy atmosphere of a mobile factory preparing "
        "to deliver its output."
    ),
    minimum_crew=[{"officers": 18}, {"crew": 120}],
    secondary_crew=[
        {"marine_officers": 55},
        {"marines": 4500},
        {"vehicle_crew": 220},
        {"prosthetic_technicians": 8},
        {"repair_fabricators": 15},
        {"medical": 30},
        {"ship_gunners": 20},
    ],
    additional_systems=[
        "Field prosthetic fabrication bay",
        "Modular repair system",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Prefabricated fortification storage",
        "Prosthetic charging stations (troop decks)",
        "Reinforced armor plating (maximum gauge)",
    ],
)

GIMLET = ShipTemplate(
    name="Gimlet",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Insertion Transport",
    combat_role="Special operations deployment behind enemy lines",
    length=155,
    armor=15,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=70,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump insertion transport with augmented special operations forces",
    long_description=(
        "The Gimlet is a hard-jump-capable transport that delivers Hyades special "
        "operations forces behind enemy lines. Slower and bulkier than other factions' "
        "insertion transports, the Gimlet compensates with hull integrity and the "
        "capability of its embarked troops. Hyades special operators are extensively "
        "augmented -- prosthetic limbs optimized for their specialty, synthetic organs "
        "that tolerate environmental extremes, and interface hardware that lets them "
        "plug directly into enemy systems. The Gimlet carries a compact prosthetic "
        "maintenance facility for field-level repair and replacement during extended "
        "operations. A Hyades special operator who damages a prosthetic hand behind "
        "enemy lines can have it replaced from the Gimlet's stores without aborting "
        "the mission."
    ),
    exterior_appearance_description=(
        "A 155-meter military spacecraft with a bare metal hull. A rectangular body with a "
        "blunt front. Hull plates on the front and lower hull, upper hull partially exposed "
        "framework. A light ion turret bolted to the top. Loading ramps on the lower rear, the "
        "ramp mechanisms and hydraulic arms exposed. Engine bells at the rear in exposed "
        "mechanical frames. Weld seams and bolt patterns across every surface. Yellow hazard "
        "striping around the loading ramps and engine housings. Maroon guild crests stencilled "
        "on the sides. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The interior splits between the hard-jump drive, crew section, and troop "
        "compartment. The troop compartment holds bunks, equipment storage, and "
        "prosthetic charging stations for the operators. A compact prosthetic "
        "maintenance facility handles field repair. The crew section is minimal -- "
        "bridge, bunks, galley. The ship has the heavy, functional feel of something "
        "built to survive being found."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 8}],
    secondary_crew=[
        {"special_forces": 44},
        {"special_forces_officers": 4},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Prosthetic maintenance facility (compact)",
        "Prosthetic charging stations (troop deck)",
        "Troop compartment",
    ],
)

HERALD = ShipTemplate(
    name="Herald",
    faction=ShipFaction.HYADES,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Comms Ship",
    combat_role="Fleet communications relay",
    length=180,
    armor=28,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=135,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Armored fleet communications relay with augmented signals crew",
    long_description=(
        "The Herald extends Hyades fleet communications beyond the range of fixed relay "
        "stations. Its communications operators interface with the relay systems through "
        "prosthetic connections -- hands socketed into signal processing equipment, "
        "synthetic eyes reading data streams at speeds that baseline eyes cannot follow. "
        "The Herald is substantially more heavily armored than other factions' comms "
        "ships -- Hyades doctrine recognizes that communications relays are priority "
        "targets and builds them to survive being targeted. Where other factions' comms "
        "ships are fragile and rely on not being found, the Herald absorbs hits and "
        "keeps relaying. Its augmented crew can perform field repairs on damaged "
        "communications equipment during an engagement, maintaining the fleet's "
        "coordination capability through damage that would silence a lighter vessel."
    ),
    exterior_appearance_description=(
        "A 180-meter military spacecraft with a bare metal hull. A rectangular body with a "
        "communications array on the top -- antenna masts and relay dishes bolted to the hull "
        "on welded brackets, their cabling running exposed along the hull exterior. An ion "
        "turret bolted to the top forward of the array. Hull plates on the front and lower "
        "hull, upper hull partially exposed framework. Engine bells at the rear in exposed "
        "mechanical frames. Weld seams and bolt patterns across every surface. Yellow hazard "
        "striping around the antenna mounts and engine housings. Maroon guild crests "
        "stencilled on the sides. Yellow work lights clamped to the frame."
    ),
    interior_appearance_description=(
        "The communications center is the heart of the ship -- a room of operator "
        "stations with prosthetic interface sockets for signal processing. Augmented "
        "operators process fleet communications through direct prosthetic feeds, "
        "managing the data stream with mechanical precision. The prosthetic maintenance "
        "bay handles crew augmentation repair. Communications equipment is modular and "
        "field-repairable -- damaged antenna arrays can be replaced from standardized "
        "stores by augmented technicians. The ship has the same industrial, functional "
        "atmosphere as all Hyades vessels."
    ),
    minimum_crew=[{"officers": 4}, {"crew": 22}],
    secondary_crew=[
        {"communications_specialists": 10},
        {"prosthetic_technician": 1},
    ],
    additional_systems=[
        "Fleet communications relay array (armored housing)",
        "Encrypted high-bandwidth communications suite",
        "Prosthetic maintenance bay (small)",
        "Prosthetic interface sockets (signals stations)",
        "Modular communications equipment stores",
    ],
)


HYADES_SMALL_CRAFT = {
    "Javelin": JAVELIN,
    "Dart": DART,
    "Stiletto": STILETTO,
    "Cutlass": CUTLASS,
}

HYADES_CORVETTES = {
    "Buckler": BUCKLER,
    "Scabbard": SCABBARD,
}

HYADES_FRIGATES = {
    "Ballista": BALLISTA,
    "Partisan": PARTISAN,
    "Spyglass": SPYGLASS,
    "Gorget": GORGET,
}

HYADES_DESTROYERS = {
    "Rampart": RAMPART,
    "Courser": COURSER,
    "Bombard": BOMBARD,
}

HYADES_CRUISERS = {
    "Onager": ONAGER,
    "Corvus": CORVUS,
}

HYADES_CAPITALS = {
    "Fortress": FORTRESS,
    "Arsenal": ARSENAL,
    "Acropolis": ACROPOLIS,
}

HYADES_SUPPORT = {
    "Courier": COURIER,
    "Musette": MUSETTE,
    "Smithy": SMITHY,
    "Belfry": BELFRY,
    "Gimlet": GIMLET,
    "Herald": HERALD,
}

HYADES_ALL_SHIPS = {
    **HYADES_SMALL_CRAFT,
    **HYADES_CORVETTES,
    **HYADES_FRIGATES,
    **HYADES_DESTROYERS,
    **HYADES_CRUISERS,
    **HYADES_CAPITALS,
    **HYADES_SUPPORT,
}