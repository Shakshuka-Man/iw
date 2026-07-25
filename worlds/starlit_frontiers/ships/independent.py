from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


LIGHT_CARGO_DRONE = ShipTemplate(
    name="Light Cargo Drone",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.SMALL,
    ship_archetype="Cargo Drone",
    combat_role="None -- automated, unarmed",
    length=4,
    armor=0,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=2,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=14,
    default_weapons=[],
    default_small_craft=[],
    short_description="Smallest automated cargo drone -- a container with an engine",
    long_description=(
        "The Light Cargo Drone is the smallest interstellar shipping unit -- barely "
        "four metres long, carrying a few cubic metres of cargo. An inertial resonator, "
        "the simplest possible navigation computer, a soft-jump drive, and a cargo "
        "container. No crew. No weapons. No manoeuvring capability beyond point-to-point "
        "navigation. Light drones are programmed with a destination, launched, and "
        "forgotten. They arrive days or weeks later depending on the jump route. In core "
        "systems, thousands transit at any given time -- swarms of small containers "
        "drifting between stations, planets, and jump points. In dangerous systems, they "
        "are rare because they are defenceless. The lowest-tier pirates subsist on "
        "intercepting light drones -- the cargo is never the most valuable, but there is "
        "no risk. A light drone cannot fight, cannot run, and cannot call for help."
    ),
    exterior_appearance_description=(
        "A 4-meter unmanned spacecraft with a white hull. A small rectangular container with "
        "an engine housing at one end and a navigation antenna at the other. Standardised "
        "cargo fittings on all faces. No windows. A shipping code stencilled in grey on the "
        "side. Mass-produced and featureless."
    ),
    interior_appearance_description=(
        "There is no interior in any meaningful sense. A sealed cargo compartment, "
        "a navigation computer the size of a shoebox, and the inertial resonator. "
        "No life support. No atmosphere. No space for a person."
    ),
    minimum_crew=[],
    secondary_crew=[],
    additional_systems=[
        "Automated navigation (point-to-point)",
        "Inertial resonator",
        "No life support",
        "No weapons",
    ],
)

STANDARD_CARGO_DRONE = ShipTemplate(
    name="Standard Cargo Drone",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Cargo Drone",
    combat_role="None -- automated, unarmed",
    length=28,
    armor=2,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=18,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=21,
    default_weapons=[],
    default_small_craft=[],
    short_description="Standard automated cargo drone -- the backbone of interstellar shipping",
    long_description=(
        "The Standard Cargo Drone is the most common interstellar vessel by number. "
        "Corvette-sized, carrying a meaningful cargo load between systems on pre-"
        "programmed routes. The standard drone is the backbone of interstellar commerce "
        "in safe space -- cheaper than crewing a freighter for routine cargo that doesn't "
        "justify the expense of a manned ship. Bulk orders, routine supplies, non-urgent "
        "deliveries -- the standard drone handles the unglamorous majority of interstellar "
        "shipping. In core systems, the transit lanes are thick with them. In frontier "
        "systems, they are less common -- the risk of interception is higher, and losing "
        "a drone means losing the cargo with no crew to fight or negotiate. Pirates with "
        "ambitions beyond the smallest scale target standard drones -- the cargo is more "
        "valuable than a light drone's, and the risk is still zero."
    ),
    exterior_appearance_description=(
        "A 28-meter unmanned spacecraft with a white hull. A rectangular cargo container with "
        "an engine housing at one end and a navigation antenna at the other. Cargo access "
        "hatches along the sides. No windows. Shipping codes stencilled in grey on the hull. "
        "No features suggesting habitation."
    ),
    interior_appearance_description=(
        "Sealed cargo compartments filling the entire volume. A slightly more "
        "capable navigation computer than the light drone, handling multi-jump "
        "routes autonomously. No life support. No atmosphere."
    ),
    minimum_crew=[],
    secondary_crew=[],
    additional_systems=[
        "Automated navigation (multi-jump capable)",
        "Inertial resonator",
        "No life support",
        "No weapons",
    ],
)

HEAVY_CARGO_DRONE = ShipTemplate(
    name="Heavy Cargo Drone",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Cargo Drone",
    combat_role="None -- automated, unarmed",
    length=55,
    armor=4,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=30,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[],
    default_small_craft=[],
    short_description="Largest automated cargo drone -- significant cargo capacity, still defenceless",
    long_description=(
        "The Heavy Cargo Drone is the largest automated cargo vessel -- pushing the upper "
        "boundary of corvette size. It carries a significant cargo load and is used for "
        "bulk shipments between core systems where the route is safe and the cargo "
        "doesn't justify the cost of a crewed freighter. Heavy drones are slower than "
        "standard drones -- the engine is sized for economy, not speed. In safe systems "
        "they are common and unremarkable. In frontier systems they represent a tempting "
        "target -- a heavy drone carrying industrial supplies or processed materials is "
        "worth intercepting, and it cannot resist. Some shipping companies hire escorts "
        "for heavy drone convoys through marginal systems. Others accept the loss rate "
        "as a cost of business."
    ),
    exterior_appearance_description=(
        "A 55-meter unmanned spacecraft with a white hull. A large rectangular cargo container "
        "with an engine housing at one end and a navigation antenna at the other. Standardised "
        "cargo fittings and access hatches. No windows. Shipping codes stencilled in grey on "
        "the hull. No features suggesting habitation."
    ),
    interior_appearance_description=(
        "Sealed cargo compartments. A navigation computer capable of multi-jump routes "
        "with basic obstacle avoidance. No life support."
    ),
    minimum_crew=[],
    secondary_crew=[],
    additional_systems=[
        "Automated navigation (multi-jump, obstacle avoidance)",
        "Inertial resonator",
        "No life support",
        "No weapons",
    ],
)

MULE = ShipTemplate(
    name="Mule",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Light Freighter",
    combat_role="Armed cargo transport -- discourages opportunists",
    length=95,
    armor=10,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=50,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="The most common crewed ship in the galaxy -- light freighter for everything",
    long_description=(
        "The Mule is the most common crewed vessel in the galaxy. More Mules are in "
        "service than any other single ship type -- millions of them, carrying modest "
        "cargo loads between systems on every trade route that exists. The Mule is the "
        "independent captain's first ship, the small trader's workhorse, the smuggler's "
        "friend, and the frontier settler's lifeline. It carries enough cargo to make a "
        "living, enough fuel to reach most destinations through medium jump points, and "
        "enough armament to discourage the lowest tier of pirate -- the kind that preys "
        "on cargo drones and thinks twice about anything with a gun turret. The Mule "
        "is not a warship. Its single ion turret is a deterrent, not a weapon system. "
        "A Mule captain who encounters a Jackal raider is negotiating, running, or "
        "dying -- not fighting. But the turret exists because a galaxy where every "
        "freighter is unarmed is a galaxy where every freighter is a target. A Mule "
        "is cheap, reliable, and available everywhere. The quality varies enormously -- "
        "a new Mule from a reputable yard is a solid ship. A Mule that has changed "
        "hands a dozen times and been repaired with whatever was available is a "
        "different experience."
    ),
    exterior_appearance_description=(
        "A 95-meter spacecraft with a white hull showing grey scuff marks and patching from "
        "years of use. A blocky rectangular body with cargo access hatches along both sides. A "
        "glazed bridge canopy at the front. A single laser turret on top. Engine bells at the "
        "rear. Company logo and registration numbers painted on the sides in grey or the "
        "company colour. Standard white running lights. The hull is plain, practical, and "
        "showing its age."
    ),
    interior_appearance_description=(
        "The cargo hold takes up the aft two-thirds. The crew section forward is "
        "compact -- a small bridge, a few bunks, a galley barely large enough to stand "
        "in, a shared head. The quality of the interior depends entirely on the owner. "
        "A well-maintained Mule is comfortable in a spartan way. A neglected Mule smells "
        "of old cargo, recycled air, and the previous owner's cooking."
    ),
    minimum_crew=[{"captain": 1}, {"crew": 2}],
    secondary_crew=[{"additional_crew": 3}],
    additional_systems=[
        "Cargo hold (modular fittings)",
        "Standard life support",
    ],
)

OX = ShipTemplate(
    name="Ox",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Medium Freighter",
    combat_role="Armed cargo transport -- meaningful defensive capability",
    length=200,
    armor=22,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=110,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Medium freighter -- dedicated cargo hauler on regular trade routes",
    long_description=(
        "The Ox is the step up from the Mule -- a proper cargo ship with dedicated holds, "
        "a real crew, and enough armament to give a single raider pause. The Ox runs "
        "regular trade routes carrying cargo in volumes that justify the larger crew and "
        "operating costs. Where a Mule captain is often an independent operator making "
        "opportunistic runs, an Ox is typically owned by a shipping company and assigned "
        "to a route. The Ox carries an ion turret and a laser turret -- enough to fight "
        "off a single Hornet gunboat or discourage an opportunistic Jackal, but not "
        "enough to survive a coordinated attack. Ox captains in dangerous systems travel "
        "in convoy or hire escort. The Ox is the ship that makes interstellar trade "
        "economically viable at moderate scale -- too large for a single operator, too "
        "small for the major trade lanes where Bisons run."
    ),
    exterior_appearance_description=(
        "A 200-meter spacecraft with a white hull showing grey wear and patching. A broad, "
        "heavy rectangular body with large cargo access hatches along both sides. A glazed "
        "bridge section at the front. A light ion turret on top and a light laser underneath. "
        "Engine bells in a cluster at the rear. Company logo and registration numbers on the "
        "sides. Standard white running lights. Functional, unglamorous, built to carry cargo."
    ),
    interior_appearance_description=(
        "Larger cargo holds than the Mule, with proper loading equipment and modular "
        "fittings. The crew section is more liveable -- individual bunks rather than "
        "shared, a proper galley, a small common area. The bridge has stations for "
        "a proper watch rotation. The ship feels like a workplace rather than a "
        "cramped survival situation."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 2}, {"crew": 6}],
    secondary_crew=[{"additional_crew": 4}, {"gunners": 2}],
    additional_systems=[
        "Cargo holds (x2, modular fittings)",
        "Loading equipment",
        "Standard life support",
    ],
)

BISON = ShipTemplate(
    name="Bison",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Bulk Freighter",
    combat_role="Defensive armament -- point defense and anti-boarding",
    length=380,
    armor=35,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=250,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Bulk freighter -- enormous, slow, the backbone of major trade lanes",
    long_description=(
        "The Bison is the container ship of space -- enormous, slow, carrying massive "
        "quantities of cargo on the major trade lanes between core systems. Bisons "
        "travel in convoys escorted by military vessels because they are too valuable "
        "to lose and too slow to run. A loaded Bison is the most tempting target in "
        "interstellar commerce -- the cargo of a single Bison can fund a small pirate "
        "operation for months. Bison convoys are what military escort frigates exist to "
        "protect. The Bison's armament is defensive -- an ion cannon for deterrence and "
        "point defense against boarders and small craft. A Bison cannot fight a warship. "
        "It can make boarding difficult and discourage the smallest attackers. The route "
        "of a specific Bison carrying specific cargo is valuable intelligence -- a large-"
        "scale pirate operation will plan a surgical strike around knowing when a Bison "
        "will be in vulnerable space."
    ),
    exterior_appearance_description=(
        "A 380-meter spacecraft with a white hull showing grey wear and numerous patches from "
        "decades of service. An enormous rectangular body dominated by modular container "
        "fittings along the entire length. A small bridge section at the front. An ion turret "
        "on top. Point-defense mounts on the sides. Engine bells in a cluster at the rear, "
        "undersized for the hull. Company logo and registration numbers on the sides at large "
        "scale. Standard white running lights. Slow and enormous."
    ),
    interior_appearance_description=(
        "The vast majority of the interior is cargo space -- enormous holds with "
        "standardized container fittings, loading cranes, and cargo management systems. "
        "The crew section is a small island in a sea of cargo -- bridge, quarters, galley, "
        "and engineering spaces packed into the forward section. Comfortable enough for "
        "the long, slow runs between systems. The crew is small for the ship's size "
        "because most of the ship doesn't need people in it."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 4}, {"crew": 16}],
    secondary_crew=[{"cargo_handlers": 10}, {"gunners": 4}],
    additional_systems=[
        "Cargo holds (multiple, standardized container fittings)",
        "Loading cranes",
        "Cargo management system",
        "Standard life support",
    ],
)

MANATEE = ShipTemplate(
    name="Manatee",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Tanker",
    combat_role="Defensive only -- fighting near a tanker is dangerous for everyone",
    length=350,
    armor=30,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=220,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Tanker for fuel, gases, water, and hazardous liquids -- don't shoot at it",
    long_description=(
        "The Manatee carries pressurized, cryogenic, or hazardous liquid cargo -- fuel, "
        "atmospheric gases, water, chemical feedstocks. It is a fundamentally different "
        "ship from a freighter because the cargo is dangerous. A Manatee carrying fuel "
        "that takes weapons fire in the wrong section becomes a bomb. A Manatee carrying "
        "cryogenic gases that suffers a containment breach becomes an environmental "
        "catastrophe. For this reason, the Manatee's armament is limited to point "
        "defense -- the ship is designed not to provoke fights, because fights near a "
        "tanker are bad for everyone. Pirates who target Manatees do so carefully, "
        "using precision boarders rather than weapons fire. Smart pirates take the "
        "whole ship. Stupid pirates shoot at it and learn why that was a mistake. "
        "The Manatee folds in all specialized liquid and gas transport -- fuel tankers, "
        "water haulers, atmospheric gas carriers, chemical transport. The hull design "
        "is the same; the tank fittings change."
    ),
    exterior_appearance_description=(
        "A 350-meter spacecraft with a white hull and prominent hazardous cargo markings in "
        "red and grey. A round, swollen body -- the tank sections dominate the profile, giving "
        "the ship a bulbous shape wider amidships than at either end. A small bridge section "
        "at the front. Point-defense mounts on the sides. Engine bells at the rear. Company "
        "logo and registration numbers on the sides. Standard white running lights. The hull "
        "looks pressurised because it is."
    ),
    interior_appearance_description=(
        "The crew section is a small compartment forward, isolated from the tank "
        "sections by heavy bulkheads. The tanks themselves are pressurized or cryogenic "
        "containment vessels that fill the rest of the hull. The crew does not enter the "
        "tank sections during transit. Monitoring is remote. The bridge is built with "
        "containment breach alarms prominently displayed. The ship smells of whatever "
        "it last carried."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 3}, {"crew": 12}],
    secondary_crew=[{"cargo_specialists": 4}, {"gunners": 2}],
    additional_systems=[
        "Pressurized tank sections",
        "Cryogenic containment systems",
        "Containment breach monitoring",
        "Emergency venting systems",
        "Hazardous cargo isolation bulkheads",
        "Standard life support",
    ],
)

SWAN = ShipTemplate(
    name="Swan",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Passenger Liner",
    combat_role="Defensive -- attacking a passenger liner brings heat",
    length=340,
    armor=32,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=230,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Passenger liner -- hundreds of passengers on regular interstellar routes",
    long_description=(
        "The Swan moves hundreds of passengers between systems on regular scheduled "
        "routes. It is the airliner of interstellar travel -- comfortable, jump-capable, "
        "and running on a timetable. The Swan is faster than a freighter of equivalent "
        "size because passengers pay for schedule reliability and nobody wants to spend "
        "an extra week in transit. The Swan's armament is defensive -- an ion cannon and "
        "point defense to discourage boarders. Attacking a passenger liner is a "
        "statement that brings disproportionate response from whatever faction controls "
        "the space -- pirates who hit passenger liners get hunted harder and longer than "
        "pirates who hit freighters. The passengers are not the target; there is no "
        "cargo worth stealing. But hostage situations happen, and some routes pass "
        "through space that is not as safe as the brochure suggests."
    ),
    exterior_appearance_description=(
        "A 340-meter spacecraft with a clean white hull -- better maintained than most "
        "independent ships. A long, rectangular body with rows of passenger viewports along "
        "both sides. A glazed bridge section at the front. An ion turret on top and a "
        "point-defense mount, both kept discreet. Engine bells in a cluster at the rear. "
        "Company livery -- a stripe in the company colour running the length of the hull. "
        "Registration numbers on the sides. Standard white running lights along the hull."
    ),
    interior_appearance_description=(
        "Passenger decks with individual cabins, a dining hall, observation lounges "
        "with viewports, and the amenities expected by paying passengers. Crew section "
        "forward is standard. The bridge is professional. The ship is designed to feel "
        "safe and comfortable -- the armament is present but not prominently displayed "
        "to passengers. Different deck classes offer different levels of comfort."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 5}, {"crew": 30}],
    secondary_crew=[
        {"passengers": 400},
        {"service_staff": 25},
        {"gunners": 2},
        {"medical": 2},
    ],
    additional_systems=[
        "Passenger decks (multiple classes)",
        "Observation lounges",
        "Passenger life support (enhanced capacity)",
        "Medical bay",
        "Standard life support",
    ],
)

PEACOCK = ShipTemplate(
    name="Peacock",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Luxury Liner",
    combat_role="Surprisingly good defensive armament -- wealthy passengers pay for safety",
    length=680,
    armor=48,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=650,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON, weapons.LIGHT_ION_TURRET, weapons.LASER_PD, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Luxury liner -- the cruise ship of space, enormous, beautiful, tempting target",
    long_description=(
        "The Peacock is the cruise ship of interstellar space -- an enormous, beautiful "
        "vessel carrying wealthy passengers on exotic routes past nebulae, binary stars, "
        "and the scenic wonders of the galaxy. The Peacock is not about getting from A "
        "to B -- it is about the experience. Fine dining while a gas giant fills the "
        "viewport. A concert hall with a view of a stellar nursery. Cabins larger than "
        "most independent captains' entire ships. The Peacock is an extraordinarily "
        "tempting target -- the passengers carry personal wealth, and the ship itself "
        "carries luxury goods. But attacking a Peacock brings enormous heat. The "
        "passengers are wealthy, connected, and politically significant. Every faction "
        "hunts pirates who target luxury liners because the passengers have the influence "
        "to demand it. The Peacock also carries surprisingly good defensive armament -- "
        "a particle cannon and multiple point defense turrets. Wealthy passengers pay for "
        "safety, and the operating companies invest in defensive systems that would be "
        "excessive on a freighter. The Peacock also carries its own security detail."
    ),
    exterior_appearance_description=(
        "A 680-meter spacecraft with a bright white hull, polished and immaculate. A long, "
        "graceful body with sweeping curves -- an elongated oval cross-section, elegant in "
        "proportion. Panoramic observation decks with large windows along the upper sides. A "
        "glazed bridge section at the front. An ion cannon and turrets recessed into the hull "
        "to maintain the clean profile. Point-defense mounts kept flush and discreet. Engine "
        "bells at the rear, faired smoothly into the hull. Company livery in silver and the "
        "company colour -- a decorative stripe along the full length, the company name in "
        "large elegant lettering. Registration numbers in silver. White running lights along "
        "the entire hull."
    ),
    interior_appearance_description=(
        "Luxury. The passenger decks feature individual suites, panoramic lounges, "
        "restaurants, entertainment spaces, and the amenities expected by the very "
        "wealthy. The observation deck offers unobstructed views through floor-to-"
        "ceiling viewports. The crew section is professional and well-appointed -- the "
        "crew of a Peacock is better paid and better accommodated than most independent "
        "crews. The bridge is a modern, well-equipped command space. Security stations "
        "are discreetly positioned throughout."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 14}, {"crew": 80}],
    secondary_crew=[
        {"passengers": 600},
        {"service_staff": 120},
        {"security_detail": 20},
        {"gunners": 6},
        {"medical": 4},
        {"entertainment_staff": 15},
    ],
    additional_systems=[
        "Luxury passenger decks",
        "Panoramic observation deck",
        "Entertainment facilities",
        "Restaurant and galley (commercial grade)",
        "Enhanced life support (passenger capacity)",
        "Security stations",
        "Medical bay (enhanced)",
    ],
)

ARMADILLO = ShipTemplate(
    name="Armadillo",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Prospector",
    combat_role="Armed for claim defense -- single operator in dangerous space",
    length=35,
    armor=12,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=30,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Small prospecting vessel -- one or two crew hunting high-value deposits",
    long_description=(
        "The Armadillo is the gold panner of space -- a small, cheap, jump-capable ship "
        "carrying one or two crew and enough scanning equipment to find high-value mineral "
        "deposits, exotic compounds, and anomalies worth selling. Armadillo operators "
        "work alone in places nobody else goes -- uncharted asteroid fields, unclaimed "
        "systems, the fringes of explored space. The work is solitary, dangerous, and "
        "occasionally enormously profitable. An Armadillo pilot who finds a deposit of "
        "rare minerals sells the coordinates and retires. An Armadillo pilot who finds "
        "nothing spends another month in the dark. The ship is armed with a single ion "
        "turret because prospectors work alone in dangerous places where claim-jumpers, "
        "pirates, and the simple hazards of uncharted space are all real threats. Some "
        "Armadillo operators mine small deposits themselves -- the ship carries basic "
        "extraction equipment for cherry-picking the most valuable material."
    ),
    exterior_appearance_description=(
        "A 35-meter spacecraft with a grey hull, scuffed and dented from use. A compact, "
        "rounded body with sensor arrays at the front and a small extraction arm or drill "
        "mount on the underside. A glazed canopy. A single laser turret on top. Engine bells "
        "at the rear. Registration numbers stencilled on the sides. Standard white running "
        "lights. A working tool that looks like it has been working."
    ),
    interior_appearance_description=(
        "Extremely cramped. A combined bridge and living space -- the pilot's seat, "
        "the bunk, the galley, and the scanning equipment are all in the same room. "
        "Sample storage and basic extraction equipment aft. The ship is a one-room "
        "apartment with an engine. Prospectors personalize their Armadillos heavily -- "
        "after months alone, the ship becomes a home."
    ),
    minimum_crew=[{"prospector": 1}],
    secondary_crew=[{"partner": 1}],
    additional_systems=[
        "Geological scanning array",
        "Basic extraction equipment",
        "Sample storage",
        "Standard life support",
    ],
)

PANGOLIN = ShipTemplate(
    name="Pangolin",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Mining Ship",
    combat_role="Claim defense -- armed against claim-jumpers and opportunists",
    length=420,
    armor=40,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=280,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON, weapons.LIGHT_LASER, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Industrial-scale mining ship -- potentially capital-sized for major operations",
    long_description=(
        "The Pangolin is the industrial end of mining -- a cruiser-scale ship that goes "
        "to a known deposit and strips it. Extraction drills, processing equipment, ore "
        "storage, and a large crew operating heavy machinery. Some Pangolins carry full "
        "refining capability, producing processed materials on-site. The Pangolin sits "
        "on a deposit for weeks or months, consuming the asteroid or planetary body and "
        "filling its holds. This makes it a stationary target in unclaimed space, and "
        "claim-jumping is a real problem -- a rival operation may arrive and dispute "
        "the claim, or pirates may decide that a ship full of processed minerals and "
        "nowhere to run is worth attacking. The Pangolin is armed accordingly -- a "
        "particle cannon and turrets provide meaningful defensive capability. A Pangolin "
        "cannot fight a warship, but it can make an attack expensive enough that "
        "most opportunists look for easier targets. The largest mining operations use "
        "multiple Pangolins with hired escort ships."
    ),
    exterior_appearance_description=(
        "A 420-meter spacecraft with a grey hull, scarred and patched from years of mining "
        "operations. An enormous, heavy rectangular body with extraction equipment dominating "
        "the underside -- drills, grappling arms, processing intakes. Ore storage sections "
        "along the sides. A bridge section at the front. An ion cannon on top. Laser mounts on "
        "the sides. Engine bells in a cluster at the rear. Company logo and registration "
        "numbers on the sides. Yellow hazard markings around the extraction equipment. "
        "Standard white running lights. Industrial and heavy."
    ),
    interior_appearance_description=(
        "The extraction section is an industrial space -- heavy machinery, processing "
        "equipment, ore conveyors, and the heat and noise of mining operations. The "
        "crew section is separated from the extraction section and is functional but "
        "comfortable for the extended deployments -- proper bunks, a mess hall, recreation "
        "space. The bridge oversees both the mining operation and the ship's systems. "
        "The ship runs in shifts around the clock when working a deposit."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 6}, {"crew": 40}],
    secondary_crew=[
        {"mining_operators": 25},
        {"processing_technicians": 10},
        {"gunners": 4},
    ],
    additional_systems=[
        "Extraction drills and grappling arms",
        "Ore processing equipment",
        "Ore storage holds",
        "Refining capability (optional, varies by configuration)",
        "Geological scanning array",
        "Standard life support",
    ],
)

VULTURE = ShipTemplate(
    name="Vulture",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Salvage Ship",
    combat_role="Armed for wreck-site competition and debris field hazards",
    length=185,
    armor=18,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=90,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Salvage ship -- wreck sites, debris fields, post-battle scavenging",
    long_description=(
        "The Vulture goes to wreck sites and strips them for usable components. Part "
        "scavenger, part treasure hunter, part junkyard operator. The Vulture carries "
        "cutting equipment, cargo cranes, tractor beams, and a crew that knows which "
        "parts of a destroyed warship are worth taking and which will kill you if you "
        "try. Operating in debris fields is dangerous work -- unexploded ordnance, "
        "reactor remnants, structural collapse, and sharp metal moving at speed. "
        "Operating in debris fields after a battle is more dangerous -- the wrecks are "
        "fresh, the ordnance is live, and other salvagers are competing for the same "
        "wrecks. Some factions consider battlefield salvage legitimate commerce. Others "
        "consider it grave robbing. The line depends on whether the bodies have been "
        "recovered first and whether the salvager cares. The Vulture is well-armed "
        "because wreck sites attract competition, and disputes over salvage claims are "
        "settled by whoever is willing to escalate."
    ),
    exterior_appearance_description=(
        "A 185-meter spacecraft with a grey hull, battered and scarred. A rectangular body "
        "built around its salvage equipment -- cutting arms, cargo cranes, and tractor beam "
        "emitters mounted on the front and sides, the mechanisms exposed. A bridge section at "
        "the front with a wide glazed canopy. A light ion turret on top. A light laser on the "
        "underside. Engine bells at the rear. Registration numbers stencilled on the sides. "
        "The hull is dented, welded, and patched -- the ship collects damage the way it "
        "collects salvage."
    ),
    interior_appearance_description=(
        "The cargo hold is a workshop -- salvaged components are stored, sorted, and "
        "sometimes repaired aboard. The cutting equipment control station is a "
        "specialized bridge position. The crew section is functional and worn -- Vulture "
        "crews work hard in dirty conditions. The bridge has salvage scanning equipment "
        "alongside standard navigation. The ship smells of cutting plasma and old metal."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 2}, {"crew": 8}],
    secondary_crew=[
        {"salvage_operators": 6},
        {"gunners": 2},
    ],
    additional_systems=[
        "Cutting equipment (plasma torches, saws)",
        "Cargo cranes",
        "Tractor beam emitters",
        "Salvage scanning array",
        "Component storage and sorting",
        "Standard life support",
    ],
)

OWL = ShipTemplate(
    name="Owl",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Survey Vessel",
    combat_role="Armed for uncharted-space hazards",
    length=170,
    armor=14,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=80,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=49,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Survey and exploration vessel -- maps jump points, charts fields, goes where no one has been",
    long_description=(
        "The Owl maps jump points, charts asteroid fields, assesses resource deposits, "
        "and explores uncharted systems. It sells the data. An Owl operator who maps a "
        "new hard jump point sells the coordinates to military intelligence, mining "
        "companies, and anyone else willing to pay. An Owl that charts a rich asteroid "
        "field sells the survey data to mining operations. The Owl is the scout of the "
        "commercial world -- going where no one has been and bringing back information "
        "rather than cargo. Hard-jump capable for deep-range variants that push into "
        "unexplored space. The Owl is armed because the unknown is dangerous -- uncharted "
        "systems may contain hazards, hostile wildlife, or other parties who don't want "
        "their location known. Survey crews are a specific breed: patient, curious, "
        "comfortable with solitude, and willing to spend months in the deep."
    ),
    exterior_appearance_description=(
        "A 170-meter spacecraft with a white hull, clean and well-maintained. A rectangular "
        "body with sensor arrays and antenna clusters at the front. A glazed bridge section. A "
        "light ion turret on top. Engine bells at the rear. Company or institution markings on "
        "the sides. Registration numbers. Standard white running lights. Functional and "
        "professional."
    ),
    interior_appearance_description=(
        "The survey section is a cluster of sensor stations and a data analysis lab. "
        "The crew section is designed for extended deployments -- comfortable bunks, a "
        "proper galley, a small recreation space. The bridge is oriented around survey "
        "operations rather than combat. The ship is quieter and more academic than most "
        "independent vessels."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 2}, {"crew": 4}],
    secondary_crew=[
        {"survey_specialists": 4},
        {"data_analysts": 2},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array",
        "Survey scanning suite",
        "Data analysis lab",
        "Jump point detection equipment",
        "Standard life support",
    ],
)

SPARROW = ShipTemplate(
    name="Sparrow",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.SMALL,
    ship_archetype="Shuttle",
    combat_role="Minimal -- single defensive weapon",
    length=10,
    armor=0,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Short-range shuttle -- the taxi of space",
    long_description=(
        "The Sparrow is the smallest piloted vessel in common use -- a short-range "
        "shuttle that moves a handful of people between nearby locations. Station to "
        "planet. Ship to ship. Orbit to surface. The Sparrow has no jump capability -- "
        "it operates within a single system, usually within a single orbital zone. "
        "Millions are in service. Every station, every port, every orbital facility has "
        "Sparrows. The single light laser is a token defensive weapon -- enough to "
        "discourage the most desperate opportunist, not enough to matter in any real "
        "engagement. A Sparrow is cheap, simple, and the first thing most people learn "
        "to fly."
    ),
    exterior_appearance_description=(
        "A 10-meter spacecraft with a white hull. A small, simple rectangular body with a "
        "glazed canopy on top. A light laser mounted underneath. Engine bells at the rear. "
        "Registration numbers stencilled on the sides. Standard white running lights. The "
        "simplest crewed spacecraft in common use."
    ),
    interior_appearance_description=(
        "A pilot's seat and three to six passenger seats behind it. Minimal instruments. "
        "Basic atmospheric controls. No galley, no head, no bunks. The interior of a "
        "taxi -- functional and nothing more."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[{"passengers": 6}],
    additional_systems=["Basic life support"],
)

FOX = ShipTemplate(
    name="Fox",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Runabout",
    combat_role="Light defensive armament",
    length=30,
    armor=6,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=22,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=14,
    default_weapons=[weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Small personal ship -- the family car of space, jump-capable",
    long_description=(
        "The Fox is a small, versatile personal ship -- bigger than a Sparrow shuttle, "
        "smaller than a Mule freighter. Jump-capable through medium points, carrying a "
        "small number of people and modest personal cargo between systems. The Fox is "
        "the family car of interstellar travel -- owned by individuals, families, and "
        "small groups who need the ability to move between systems without booking "
        "passage on a Swan or hiring a Mule. The Fox is fast for its size, carries a "
        "single laser turret for basic defense, and has enough living space for a few "
        "people to spend a week or two in transit without going insane. Foxes vary "
        "enormously in condition and configuration -- a new Fox is a comfortable small "
        "ship, while a thirty-year-old Fox might be held together with aftermarket "
        "repairs and optimism."
    ),
    exterior_appearance_description=(
        "A 30-meter spacecraft with a white hull. A compact rectangular body with a glazed "
        "bridge canopy at the front. A laser turret on top. Cargo or passenger space behind "
        "the bridge. Engine bells at the rear. Registration numbers on the sides. Standard "
        "white running lights. Often personalised by the owner -- custom paint, modified "
        "fittings, aftermarket additions."
    ),
    interior_appearance_description=(
        "A small bridge forward with one or two seats. Behind it, a combined living "
        "space -- a few bunks, a tiny galley, a head, and some personal cargo storage. "
        "The interior is tight but liveable for short trips. The quality depends on "
        "the owner -- some Foxes are immaculate, some are cluttered, and some are "
        "barely functional."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[{"passengers": 4}],
    additional_systems=[
        "Modest cargo storage",
        "Standard life support",
    ],
)

STALLION = ShipTemplate(
    name="Stallion",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Yacht",
    combat_role="Armed to owner's preference -- token to surprisingly heavy",
    length=80,
    armor=12,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=45,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.LIGHT_ION_TURRET, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Personal yacht -- fast, comfortable, a status symbol with guns",
    long_description=(
        "The Stallion is the personal yacht -- a fast, comfortable frigate-weight ship "
        "owned by someone wealthy enough to afford a ship they don't use for commerce. "
        "The Stallion is not for making money. It is for personal travel, status, and "
        "the pleasure of owning a beautiful ship. Stallions are fast -- the owners pay "
        "for speed because they can, and because wealthy people value their time. The "
        "armament varies by owner: the stock configuration carries an ion turret and a "
        "laser turret, but wealthy owners in dangerous space often upgrade significantly. "
        "Some Stallions carry weapons that would be appropriate on a combat frigate -- "
        "the owner has the money and the threat profile to justify it. A Stallion is "
        "a status symbol, and attacking one means the owner has the resources to pursue "
        "consequences."
    ),
    exterior_appearance_description=(
        "An 80-meter spacecraft with a white hull, polished and immaculate. A sleek, elongated "
        "body with clean lines and visible craftsmanship. A glazed bridge section at the "
        "front. Turret mounts integrated smoothly into the hull rather than bolted on. Engine "
        "bells at the rear, faired into the hull. Custom paint or detailing reflecting the "
        "owner's taste. Registration numbers in discreet lettering. The ship is designed to be "
        "admired."
    ),
    interior_appearance_description=(
        "The interior reflects the owner's wealth and taste. A comfortable bridge. "
        "A private cabin or suite for the owner. Guest accommodation. A galley that "
        "serves real food. The ship is well-appointed, well-maintained, and well above "
        "the standard of any commercial vessel. Some Stallions are more luxurious than "
        "others -- the baseline is comfortable, the ceiling is extravagant."
    ),
    minimum_crew=[{"captain": 1}, {"crew": 3}],
    secondary_crew=[
        {"guests": 8},
        {"personal_staff": 2},
        {"gunners": 1},
    ],
    additional_systems=[
        "Enhanced life support",
        "Guest accommodation",
        "Upgraded galley",
    ],
)

HORNET = ShipTemplate(
    name="Hornet",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Gunboat",
    combat_role="Light combat -- entry-level warship for pirates, mercenaries, and local defense",
    length=40,
    armor=14,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=38,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=14,
    default_weapons=[weapons.PLASMA_LAUNCHER, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Small, cheap gunboat -- the weapon of choice for pirates and local defense",
    long_description=(
        "The Hornet is the entry-level combat ship -- a small, heavily armed corvette "
        "that is the most common warship outside faction navies. Hornets serve as the "
        "primary combat vessel for small-scale pirates, mercenary companies, local "
        "defense forces, and independent system militias. They are cheap enough that "
        "a warlord can build a fleet of them, simple enough that a crew without formal "
        "naval training can operate them, and armed enough to threaten anything up to "
        "a light freighter. A single Hornet can take a Mule. Two or three can threaten "
        "an Ox. Against a real warship -- even a patrol corvette -- a Hornet is outclassed, "
        "and Hornet crews know it. The Hornet's doctrine is to pick fights it can win "
        "and run from fights it can't. A Hornet that encounters a Satyr patrol corvette "
        "is already calculating its jump route out."
    ),
    exterior_appearance_description=(
        "A 40-meter spacecraft with a grey hull, scratched and modified. A compact, angular "
        "body with weapon mounts prominently visible -- a plasma launcher on the underside and "
        "a light laser on top. A glazed canopy. Engine bells at the rear. Aftermarket "
        "modifications visible -- salvaged weapon mounts, non-standard fittings, welded "
        "reinforcement plates. Custom paint or markings. No two look identical."
    ),
    interior_appearance_description=(
        "Cramped, functional, and reflecting the crew's means. The bridge is a few "
        "stations packed into a small compartment. Crew quarters are bunks in a "
        "corridor. The galley is a heating element and some storage. The ship is not "
        "comfortable -- it is armed. The condition of the interior tells you everything "
        "about the crew."
    ),
    minimum_crew=[{"captain": 1}, {"crew": 4}],
    secondary_crew=[{"gunners": 2}],
    additional_systems=["Standard life support"],
)

JACKAL = ShipTemplate(
    name="Jackal",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Raider",
    combat_role="Hit-and-run piracy, mercenary operations, independent defense",
    length=110,
    armor=16,
    speed=Speed.FAST,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=55,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=21,
    default_weapons=[weapons.ION_CANNON, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Fast raider with cargo space -- the purpose-built pirate ship",
    long_description=(
        "The Jackal is the purpose-built raider -- fast enough to catch freighters, "
        "armed enough to threaten them, and carrying enough cargo space to haul the "
        "loot. The Jackal is the ship that makes piracy viable as a business model. "
        "A Jackal finds a trade lane, identifies a juicy-looking target -- an Ox without "
        "escort, a Mule running alone -- and attacks. The engagement is fast: close, "
        "threaten, demand cargo or board. If the target surrenders, load up and go. If "
        "the target fights, kill it quickly and take what survives. If military ships "
        "appear, run. The Jackal is designed for this cycle. It is also used by "
        "legitimate mercenary outfits, independent system defense forces, and anyone "
        "who needs a fast, armed ship with cargo capacity. A Jackal flying independent "
        "defence force colours is the same ship as a Jackal flying pirate colours -- "
        "the difference is who's paying and who's being shot at."
    ),
    exterior_appearance_description=(
        "A 110-meter spacecraft with a grey hull, patched and modified. A lean rectangular "
        "body with cargo access hatches along the sides. The hull profile could pass for a "
        "light freighter at distance -- the weapon mounts are not prominently placed. An ion "
        "cannon in a housing on top. A light laser underneath. A glazed bridge section at the "
        "front. Engine bells at the rear. Aftermarket modifications and reinforcement visible "
        "up close. Registration numbers that may or may not be genuine."
    ),
    interior_appearance_description=(
        "Split between combat spaces and cargo hold. The bridge is a combat-oriented "
        "command position. The cargo hold is large for the ship's size -- the whole point "
        "is carrying stolen goods. Crew quarters are functional. The ship is built for "
        "short, intense operations rather than extended cruises."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 2}, {"crew": 8}],
    secondary_crew=[
        {"gunners": 3},
        {"boarding_party": 6},
    ],
    additional_systems=[
        "Cargo hold (raider-sized)",
        "Boarding equipment",
        "Standard life support",
    ],
)

GAZELLE = ShipTemplate(
    name="Gazelle",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Blockade Runner",
    combat_role="Speed is the defense -- lightly armed, runs rather than fights",
    length=100,
    armor=8,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=40,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=21,
    default_weapons=[weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Extremely fast blockade runner -- survives by not being caught",
    long_description=(
        "The Gazelle is built for one thing: getting through space that someone else "
        "doesn't want you to get through. Fast, jump-capable through hard points, and "
        "carrying high-value cargo in a hull designed for speed rather than combat. The "
        "Gazelle is the smuggler's ship, the wartime merchant's ship, and the blockade "
        "runner's ship. Its armament is a single light ion turret -- a token gesture. If "
        "a Gazelle is firing its weapon, something has gone wrong. The defense is not "
        "being caught. The Gazelle's hard-jump capability is its most valuable feature -- "
        "it can use jump routes that most ships cannot, appearing in systems that "
        "blockading forces don't have covered. A Gazelle running contraband through a "
        "military blockade uses hard jump points to bypass the picket line, delivers "
        "its cargo, and vanishes back through a different hard point before the response "
        "arrives."
    ),
    exterior_appearance_description=(
        "A 100-meter spacecraft with a grey hull, clean and stripped down. A narrow, elongated "
        "body with oversized engine bells at the rear. Minimal external features. A laser "
        "turret on top. A glazed bridge section at the front. The hull is smooth and "
        "featureless -- nothing to create drag or sensor return. Registration numbers on the "
        "sides. The ship looks fast because it is."
    ),
    interior_appearance_description=(
        "Engine, jump drive, cargo, and a tiny crew section. The cargo hold is "
        "optimized for high-value, low-volume goods. The crew section is minimal -- a "
        "bridge, bunks for a handful, and the essentials. Comfort is not the point. "
        "Getting there first is the point."
    ),
    minimum_crew=[{"captain": 1}, {"crew": 3}],
    secondary_crew=[],
    additional_systems=[
        "Hard-jump drive",
        "High-value cargo hold",
        "Low-emission hull design",
        "Standard life support",
    ],
)

PANTHER = ShipTemplate(
    name="Panther",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Privateer",
    combat_role="Sustained combat operations -- mercenary, letter of marque, independent defense",
    length=140,
    armor=22,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=70,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_RAILGUN, weapons.LIGHT_LASER, weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Frigate-weight privateer -- the heaviest common independent combat ship",
    long_description=(
        "The Panther is a proper frigate-weight warship built by independent shipyards "
        "for serious customers: mercenary companies with real contracts, independent "
        "systems with real defense budgets, and privateers with letters of marque from "
        "factions willing to outsource commerce raiding. The Panther carries a railgun -- "
        "a real warship weapon, not the light armament of a Hornet or Jackal. It can "
        "engage military frigates with a meaningful chance of survival, though a faction "
        "navy frigate will outclass it in every dimension. The Panther is the ship that "
        "divides casual pirates from professional operators. Owning a Panther means you "
        "have real resources, real crew, and real ambitions. A pirate fleet led by a "
        "Panther with a screen of Jackals and Hornets is a genuine regional threat "
        "that requires a military response."
    ),
    exterior_appearance_description=(
        "A 140-meter spacecraft with a grey hull, well-maintained and purposeful. A "
        "rectangular body, heavy and solidly built. A light "
        "railgun housing along the top. Light laser mounts on the sides. A glazed bridge "
        "section at the front. Engine bells in a cluster at the rear. The ship looks like a "
        "warship -- the weapon mounts and construction quality are visible. Organisation "
        "markings or custom paint on the sides. Registration numbers."
    ),
    interior_appearance_description=(
        "The bridge is a real combat command space. The gunnery stations have proper "
        "targeting displays. Crew quarters are military-standard -- bunks, lockers, a "
        "shared mess. The ship is built for sustained operations and the crew spaces "
        "reflect it. Better maintained and more disciplined than a Hornet or Jackal -- "
        "the crew of a Panther are usually professionals."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 4}, {"crew": 20}],
    secondary_crew=[
        {"gunners": 6},
        {"boarding_party": 8},
    ],
    additional_systems=[
        "Standard targeting suite",
        "Boarding equipment",
        "Standard life support",
    ],
)

TIGER = ShipTemplate(
    name="Tiger",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Corsair",
    combat_role="Full combat capability -- a real warship flying independent colours",
    length=220,
    armor=35,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=160,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=28,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Destroyer-scale independent warship -- a warlord's flagship",
    long_description=(
        "The Tiger is a destroyer-scale warship built by a successful warlord's shipyard "
        "or a well-funded independent system's military programme. Building a Tiger "
        "requires industrial infrastructure that most independents don't have -- a "
        "shipyard capable of destroyer construction, a supply chain for military-grade "
        "weapons, and the crew to operate a real warship. A Tiger represents a regional "
        "power. A fleet built around a Tiger -- with Panthers, Jackals, and Hornets as "
        "supporting ships -- is a military force that requires a faction navy response. "
        "The Tiger carries a heavy particle cannon and antimatter torpedoes -- real "
        "capital-ship weapons, though at lower effectiveness than faction equivalents. "
        "A Tiger cannot match a faction destroyer in a straight fight, but it can "
        "threaten anything smaller, and a Tiger that picks its engagements carefully "
        "can operate for years without being caught."
    ),
    exterior_appearance_description=(
        "A 220-meter spacecraft with a grey hull, heavily modified and armed. A rectangular "
        "body with heavy weapon mounts -- a particle cannon housing on top and a torpedo bay "
        "in the lower front. A light ion turret on the upper hull. A glazed bridge section at "
        "the front. Engine bells in a cluster at the rear. The ship is unmistakably a warship. "
        "Organisation markings, custom paint, and modifications that vary from ship to ship. "
        "No two are identical."
    ),
    interior_appearance_description=(
        "Military interior. The bridge is a command space built for combat. Gunnery "
        "stations have targeting displays. The torpedo room is a proper weapons space. "
        "Crew quarters are military bunks. The mess serves institutional food. The ship "
        "functions like a military vessel because it is one -- just not a faction's."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 8}, {"crew": 50}],
    secondary_crew=[
        {"gunners": 14},
        {"torpedo_crew": 4},
        {"boarding_party": 12},
    ],
    additional_systems=[
        "Standard targeting suite",
        "Torpedo bay",
        "Boarding equipment",
        "Standard life support",
    ],
)

RHINO = ShipTemplate(
    name="Rhino",
    faction=ShipFaction.INDEPENDENT,
    size_class=ShipSize.CRUISER,
    ship_archetype="Marauder",
    combat_role="Cruiser-scale combat -- a faction in all but name",
    length=340,
    armor=48,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=280,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[
        weapons.RAILGUN,
        weapons.PARTICLE_LANCE,
        weapons.LIGHT_LASER,
        weapons.LIGHT_LASER,
    ],
    default_small_craft=[],
    short_description="Cruiser-scale independent warship -- the biggest thing flying independent colours",
    long_description=(
        "The Rhino is the largest warship built outside the faction navies -- a cruiser-"
        "scale vessel that represents industrial infrastructure, territorial ambition, "
        "and military capability approaching that of a minor faction. Building a Rhino "
        "requires shipyards, supply chains, trained crew, and the economic base to "
        "support a capital-class warship's operating costs. A warlord who fields a Rhino "
        "is not a pirate -- they are a political entity with territorial claims, military "
        "forces, and the industrial base to sustain them. The Rhino carries a heavy "
        "railgun and a particle cannon battery -- lighter than a faction heavy cruiser's "
        "armament, but real capital-ship weapons capable of engaging faction warships. A "
        "Rhino cannot match a Typhon or a Dagon in a line fight, but it can threaten "
        "anything lighter, and a Rhino with supporting ships is a strategic problem that "
        "faction navies must address with significant force. Seeing a Rhino means the "
        "local power structure is serious."
    ),
    exterior_appearance_description=(
        "A 340-meter spacecraft with a grey hull, heavily armed and heavily modified. A "
        "massive rectangular body with heavy weapon mounts -- a railgun housing along the top, "
        "a particle lance extending from the front, turrets along the sides. A glazed bridge "
        "section at the front. Engine bells in a large cluster at the rear. Point-defense "
        "mounts along the hull. The ship is unambiguously a warship of significant size. "
        "Organisation markings and custom modifications that vary from ship to ship. No two "
        "are built to the same specifications."
    ),
    interior_appearance_description=(
        "Military interior at cruiser scale. A proper bridge, proper gunnery stations, "
        "proper crew quarters. The ship functions as the flagship of an independent "
        "fleet. The quality varies -- some Rhinos are built to near-faction standards, "
        "while others are rougher, reflecting the resources available. The crew is "
        "large enough to require military-style organization: watches, departments, "
        "chain of command."
    ),
    minimum_crew=[{"captain": 1}, {"officers": 12}, {"crew": 100}],
    secondary_crew=[
        {"gunners": 22},
        {"point_defense_crew": 8},
        {"boarding_party": 20},
        {"medical": 2},
    ],
    additional_systems=[
        "Standard targeting suite",
        "Boarding equipment",
        "Standard life support",
    ],
)


INDEPENDENT_DRONES = {
    "Light Cargo Drone": LIGHT_CARGO_DRONE,
    "Standard Cargo Drone": STANDARD_CARGO_DRONE,
    "Heavy Cargo Drone": HEAVY_CARGO_DRONE,
}

INDEPENDENT_TRANSPORT = {
    "Mule": MULE,
    "Ox": OX,
    "Bison": BISON,
    "Manatee": MANATEE,
    "Swan": SWAN,
    "Peacock": PEACOCK,
}

INDEPENDENT_INDUSTRIAL = {
    "Armadillo": ARMADILLO,
    "Pangolin": PANGOLIN,
    "Vulture": VULTURE,
    "Owl": OWL,
}

INDEPENDENT_PERSONAL = {
    "Sparrow": SPARROW,
    "Fox": FOX,
    "Stallion": STALLION,
}

INDEPENDENT_COMBAT = {
    "Hornet": HORNET,
    "Jackal": JACKAL,
    "Gazelle": GAZELLE,
    "Panther": PANTHER,
    "Tiger": TIGER,
    "Rhino": RHINO,
}

INDEPENDENT_ALL_SHIPS = {
    **INDEPENDENT_DRONES,
    **INDEPENDENT_TRANSPORT,
    **INDEPENDENT_INDUSTRIAL,
    **INDEPENDENT_PERSONAL,
    **INDEPENDENT_COMBAT,
}