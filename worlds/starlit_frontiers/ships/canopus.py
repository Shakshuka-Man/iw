from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate


AUK = ShipTemplate(
    name="Auk",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.SMALL,
    ship_archetype="Scout",
    combat_role="Reconnaissance / sensor platform",
    length=16,
    armor=2,
    speed=Speed.VERY_FAST,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=4,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.LIGHT_LASER],
    default_small_craft=[],
    short_description="Expendable reconnaissance craft with redundant crew",
    long_description=(
        "The Auk is the eyes of a Canopan fleet -- a small, unassuming scout built at the "
        "heavy end of the template. Canopan engineers added a second crew station where "
        "most factions use one. The second seat is a sensor operator, usually a junior "
        "rating gaining experience. If the pilot is killed, the sensor operator flies "
        "the ship home. This redundancy is characteristic of Canopan small craft doctrine: "
        "everything has a backup, because Canopan planners think in terms of what still "
        "works after something goes wrong. The Auk avoids all fights. Its value is the "
        "intelligence it feeds back to the fleet. Too small for onboard reanimation -- a "
        "dead Auk crew member waits for recovery by a larger ship."
    ),
    exterior_appearance_description=(
        "A 16-meter single-seat military spacecraft with a dark grey hull. A small, rounded "
        "body with a thick oval cross-section and a blunt nose. Layered armour plates overlap "
        "across the hull, giving a scaled texture. A narrow reinforced glazed canopy. A light "
        "laser mounted under the nose. Engine bells recessed into the rear behind armoured "
        "cowlings. Crimson trim along the armour plate edges. Gold filigree borders the canopy "
        "frame. A small gold emperor's crest on both sides. A short crimson pennant trails "
        "from a mount on the top rear."
    ),
    interior_appearance_description=(
        "Two seats in tandem in a cramped cockpit lit by dim amber instrument lighting. "
        "Bare gunmetal interior, unpadded, with exposed cable runs bolted to the "
        "bulkheads. A faint chemical smell from the sealant compound Canopan shipwrights "
        "apply to every seam. Nothing decorative, nothing wasted, everything built to be "
        "hosed down and put back in service."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[{"sensor_operator": 1}],
    additional_systems=["Redundant flight controls", "Reinforced sensor array"],
)

SABERTOOTH = ShipTemplate(
    name="Sabertooth",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.SMALL,
    ship_archetype="Bomber",
    combat_role="Anti-capital strike craft",
    length=22,
    armor=4,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=9,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.ANTIMATTER_TORPEDO],
    default_small_craft=[],
    short_description="Over-built bomber carrying a single antimatter torpedo",
    long_description=(
        "The Sabertooth carries a single antimatter torpedo to point-blank range through "
        "a killing field of enemy point defense fire. Every faction's bombers face this "
        "harrowing run. The difference is that a Sabertooth absorbs hits that would "
        "destroy other factions' bombers and keeps flying. Canopan engineers over-built "
        "the hull well beyond the standard template, adding structural reinforcement at "
        "no meaningful cost -- the bomber was already slow, and you cannot make slow worse. "
        "A Sabertooth that takes a point defense hit through the port side arrives at "
        "torpedo range trailing atmosphere but still functional. The crew knows that if "
        "they die on the approach, a Canopan carrier has reanimation bays waiting. This "
        "knowledge does not make the approach less terrifying. It makes it more."
    ),
    exterior_appearance_description=(
        "A 22-meter two-seat military spacecraft with a dark grey hull. A wide, rounded body "
        "with a thick oval cross-section. A narrow reinforced glazed tandem canopy. The "
        "torpedo housing dominates the underside, framed by gold moulding. Layered armour "
        "plates overlap across the hull. Engine bells recessed into the rear behind armoured "
        "cowlings. Crimson trim along every armour plate edge. Gold filigree along the torpedo "
        "housing frame and canopy surround. A gold emperor's crest on both sides. Crimson "
        "pennants trailing from mounts on both rear flanks."
    ),
    interior_appearance_description=(
        "Two seats in tandem -- pilot forward, weapons officer behind -- in a cockpit built "
        "like the inside of a vault. The torpedo housing fills the ventral section, its "
        "arming mechanism visible through a floor panel. Emergency medical supplies are "
        "bolted to the bulkhead within arm's reach -- not for comfort, but because a "
        "wounded crew member who can still press the firing switch can still complete the "
        "mission. The interior smells of metal and the faint antiseptic tang common to "
        "all Canopan vessels."
    ),
    minimum_crew=[{"pilot": 1}, {"weapons_officer": 1}],
    secondary_crew=[],
    additional_systems=["Reinforced hull plating", "Emergency medical kit"],
)

RAPTOR = ShipTemplate(
    name="Raptor",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.SMALL,
    ship_archetype="Fighter",
    combat_role="Escort / area control / anti-small-craft",
    length=18,
    armor=8,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=16,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.PLASMA_LAUNCHER],
    default_small_craft=[],
    short_description="Heavy escort fighter trading speed for survivability",
    long_description=(
        "The Raptor is the Canopan general-purpose fighter -- slower than the template but "
        "substantially tougher. Where other factions' fighters outmaneuver threats, the "
        "Raptor outlasts them. In a turning fight a Raptor will lose to a faster "
        "interceptor, but the interceptor has to kill it first, and Raptors are difficult "
        "to kill. Raptors escort Sabertooth bombers through enemy interceptor screens, and "
        "their durability makes them excellent at it -- an interceptor that commits to a "
        "Raptor gets bogged down fighting a craft that refuses to die while the bombers "
        "slip through. The ejection system is robust and well-maintained. Canopan doctrine "
        "prioritizes crew recovery, because a recovered pilot flies again tomorrow and a "
        "dead pilot flies again next week."
    ),
    exterior_appearance_description=(
        "An 18-meter single-seat military spacecraft with a dark grey hull. A squat, rounded "
        "body with a thick oval cross-section and blunt front. Layered armour plates overlap "
        "across the hull, giving a scaled texture. A narrow reinforced glazed canopy. A plasma "
        "launcher housing on the underside. Engine bells recessed into the rear behind "
        "armoured cowlings. Crimson trim along every armour plate edge. Gold filigree borders "
        "the canopy frame and engine cowlings. A small gold emperor's crest on both sides. A "
        "short crimson pennant trails from a mount on the top rear."
    ),
    interior_appearance_description=(
        "A single-seat cockpit surrounded by more hull than seems necessary for a craft "
        "this size. The canopy is narrow and reinforced with layered composites. "
        "Instruments are simple, analogue-heavy, designed to keep working after damage "
        "that would blank out digital displays. A backup manual release for the plasma "
        "launcher sits within reach in case the primary firing system fails."
    ),
    minimum_crew=[{"pilot": 1}],
    secondary_crew=[],
    additional_systems=["Reinforced cockpit structure", "Backup manual weapon release", "Heavy ejection system"],
)

TARPAN = ShipTemplate(
    name="Tarpan",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.SMALL,
    ship_archetype="Gunship",
    combat_role="Anti-escort / heavy strike craft",
    length=24,
    armor=12,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=28,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=1,
    default_weapons=[weapons.HEAVY_PLASMA_CANNON],
    default_small_craft=[],
    short_description="Heavy gunship with reanimated ammunition handlers",
    long_description=(
        "The Tarpan is the Canopan answer to the escort screen problem. Where other "
        "factions build fast gunships that dash through the screen, the Tarpan walks "
        "through it. Slower than the template but substantially tougher, the Tarpan "
        "absorbs fire from destroyers and frigates while delivering sustained heavy "
        "plasma fire. Its crew of six includes two reanimated shells who handle damage "
        "control and ammunition feeds -- work that keeps the weapon firing even as the "
        "ship takes hits. A heavy bulkhead separates the living crew forward from the "
        "shells aft, not for safety, but because most living crew find extended proximity "
        "to the reanimated uncomfortable."
    ),
    exterior_appearance_description=(
        "A 24-meter multi-crew military spacecraft with a dark grey hull. A broad, rounded "
        "body with a thick circular cross-section and a blunt nose. Layered armour plates "
        "overlap across the hull. A narrow reinforced glazed canopy. A heavy plasma cannon "
        "housing on the underside, framed by gold moulding. Engine bells recessed into the "
        "rear behind armoured cowlings with crimson-painted rims. Crimson trim along every "
        "armour plate edge. Gold filigree along the weapon housing and engine cowlings. A gold "
        "emperor's crest on both sides. Crimson pennants trailing from mounts on both flanks."
    ),
    interior_appearance_description=(
        "Six stations in a cramped cabin -- pilot and gunner forward, engineer and sensor "
        "operator amidships, and two reanimated shells in the aft section near the "
        "ammunition feeds and plasma cannon power systems. The shells work in a section "
        "that runs hotter and louder than the forward cabin, handling the physical labor "
        "of keeping the weapon fed. The interior is dark, loud when the cannon fires, "
        "and smells of ozone and the preservative compounds used on reanimated tissue."
    ),
    minimum_crew=[{"pilot": 1}, {"gunner": 1}, {"crew": 2}, {"shells": 2}],
    secondary_crew=[],
    additional_systems=["Reinforced weapon housing", "Shell work compartment (aft)"],
)


AUROCHS = ShipTemplate(
    name="Aurochs",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Patrol Corvette",
    combat_role="System defense / peacetime security",
    length=70,
    armor=25,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=90,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy patrol corvette with extended endurance and shell crew",
    long_description=(
        "The Aurochs is the standard Canopan patrol vessel and the most commonly "
        "encountered ship in their navy. Heavier and slower than the template corvette, "
        "it carries a larger crew supplemented by reanimated shells who handle "
        "maintenance, cleaning, cargo loading, and damage control -- the endless menial "
        "work that wears down living crew on long patrols. The Aurochs stays on station "
        "longer than equivalent ships from other factions, not because it carries more "
        "supplies but because its shells do not eat, sleep, or need rotation. The living "
        "crew stays fresher. In wartime, Aurochs patrol corvettes form early warning "
        "screens at jump points. They are slower than other factions' patrol corvettes "
        "and cannot chase down fast contacts, but they hold position longer and absorb "
        "more punishment if attacked."
    ),
    exterior_appearance_description=(
        "A 70-meter military spacecraft with a dark grey hull. A heavy, rounded cylinder with "
        "a blunt domed front and a thick body. Layered armour plates overlap across the entire "
        "hull surface, giving a pronounced scaled texture. A particle cannon housing along the "
        "top, framed by ornamental gold moulding. A heavy laser turret in a gilded housing "
        "behind the bridge. A narrow reinforced bridge canopy near the front. Engine bells "
        "recessed into the rear behind armoured cowlings. Crimson trim along every armour "
        "plate edge. Gold ornamentation across the hull -- the emperor's crest on both sides, "
        "gold laurel borders around the weapon housings, gilded rank insignia near the bridge. "
        "A crimson banner mounted on the top spine, trailing from an ornamental pole. Dim "
        "amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The interior is divided between living crew spaces forward and shell work areas "
        "aft. The bridge is a practical half-circle of conventional stations with manual "
        "backup controls for every system. Corridors are wider than expected -- built to "
        "allow shells carrying equipment to pass crew without contact. Crew quarters are "
        "small but functional, lit in dim amber. The shell compartment aft is unlit and "
        "unheated, separated by a sealed bulkhead. The ship has the grim, antiseptic "
        "cleanliness common to Canopan vessels -- everything scrubbed, everything in its "
        "place, a faint chemical smell that never quite goes away."
    ),
    minimum_crew=[{"officers": 3}, {"crew": 10}, {"shells": 8}],
    secondary_crew=[{"gunners": 3}, {"shells": 4}],
    additional_systems=[
        "Shell compartment (aft)",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

MOA = ShipTemplate(
    name="Moa",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Tender Corvette",
    combat_role="Small-craft carrier / forward deployment",
    length=66,
    armor=18,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=60,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=28,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[("Raptor", 5)],
    short_description="Heavy tender corvette carrying five Raptor fighters",
    long_description=(
        "The Moa carries and supports a detachment of Canopan small craft, extending "
        "their operational range by providing a jump-capable platform. A Moa with five "
        "Raptors aboard is the standard Canopan system defense package -- durable fighters "
        "deployed from a durable platform. The Moa's hangar includes shell labor for "
        "rearming and refueling craft -- work that is physically demanding and often "
        "dangerous when ordnance is involved. Shells handle it without complaint or "
        "fatigue. The Moa is slower than the template tender corvette, reflecting "
        "Canopan construction priorities, but its additional hull integrity means it "
        "survives in contested space longer than equivalents."
    ),
    exterior_appearance_description=(
        "A 66-meter military spacecraft with a dark grey hull. A wide, rounded body with a "
        "thick oval cross-section. Launch cradles for fighters visible along both sides, the "
        "bay openings framed by gold moulding. A light ion turret in a gilded housing on top. "
        "Layered armour plates across the hull. Engine bells recessed into the rear behind "
        "armoured cowlings. Crimson trim along the armour plate edges and around the launch "
        "bay openings. Gold filigree borders the bay frames and engine cowlings. A gold "
        "emperor's crest on both sides. Crimson pennants trailing from mounts at the rear. Dim "
        "amber lights at the launch bay openings."
    ),
    interior_appearance_description=(
        "The interior is split between crew spaces forward and a hangar section aft. The "
        "hangar is functional and unadorned -- launch cradles hold each fighter in "
        "mechanical clamps, with shell labor handling the physical work of moving "
        "ordnance, connecting fuel lines, and performing heavy maintenance. The shells "
        "work continuously during turnaround operations, their movements mechanical and "
        "efficient. The crew section is compact and functional, lit in the same dim "
        "amber as all Canopan vessels."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 6}, {"shells": 6}],
    secondary_crew=[
        {"embarked_craft_pilots": 5},
        {"hangar_technicians": 3},
        {"shells": 4},
    ],
    additional_systems=[
        "Hangar bay (5 small craft)",
        "Craft maintenance and rearm facilities",
        "Shell compartment (hangar)",
        "Extended consumable storage",
    ],
)


SMILODON = ShipTemplate(
    name="Smilodon",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Combat Frigate",
    combat_role="Fleet screening / torpedo attack",
    length=175,
    armor=45,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=175,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.RAILGUN, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy combat frigate with reanimation bay and torpedo armament",
    long_description=(
        "The Smilodon is the Canopan fleet's primary screening combatant -- a frigate "
        "built heavier than anything else in its weight class. It holds the outer ring "
        "of the battle line, hunts enemy frigates, and carries an antimatter torpedo for "
        "close-range strikes. A pack of Smilodons closing to torpedo range is a "
        "characteristic Canopan tactic: they absorb the fire that would destroy lighter "
        "frigates and arrive at point blank with torpedoes armed. The Smilodon carries "
        "the smallest reanimation bay in the Canopan fleet -- enough to restore a handful "
        "of casualties to shell status during a battle. This means crew losses in an "
        "engagement are partially recoverable: a dead gunner is pulled from their station, "
        "taken below, reanimated as a shell, and returned to damage control duty within "
        "the hour. The ship fights harder the longer the battle lasts, because its dead "
        "keep working."
    ),
    exterior_appearance_description=(
        "A 175-meter military spacecraft with a dark grey hull. A broad, rounded oblong body "
        "with a thick oval cross-section and a blunt, curved front. Layered armour plates "
        "overlap across the entire hull surface, giving a scaled, reptilian texture. A railgun "
        "housing along the top, framed by ornamental gold moulding. A recessed torpedo bay in "
        "the lower front behind heavy doors with gold filigree borders. A heavy laser turret "
        "in a housing with a gilded frame. Engine bells recessed deep into the rear behind "
        "armoured cowlings with crimson-painted rims. Crimson trim along every armour plate "
        "edge. Gold ornamentation across the hull -- the emperor's crest in raised gold relief "
        "on the front, gold laurel borders around weapon housings, gilded rank insignia on the "
        "sides. Crimson and gold banners mounted on the top spine, trailing from ornamental "
        "poles. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The bridge is a practical arrangement of manual stations with the captain's chair "
        "elevated at center. Below decks, the reanimation bay occupies a sealed section "
        "amidships -- a cold, clinical space with operating tables, preservation equipment, "
        "and the chemical systems that restart a body's motor functions. The living crew "
        "avoid the bay unless duty requires it. Corridors are wide enough for shells "
        "carrying casualties. The torpedo room is forward, tended by a mixed crew of "
        "living ratings and shells who handle the heavy lifting. The ship has the "
        "characteristic Canopan atmosphere: dim lighting, antiseptic smell, everything "
        "built to keep functioning after damage that would cripple another faction's ship."
    ),
    minimum_crew=[{"officers": 10}, {"crew": 40}, {"shells": 28}],
    secondary_crew=[
        {"gunners": 12},
        {"torpedo_crew": 6},
        {"reanimation_technicians": 2},
        {"shells": 16},
    ],
    additional_systems=[
        "Reanimation bay (small -- capacity 4)",
        "Shell compartment",
        "Reinforced hull structure",
        "Redundant critical systems",
    ],
)

THYLACINE = ShipTemplate(
    name="Thylacine",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Patrol Frigate",
    combat_role="Commerce protection / torpedo attack / independent operations",
    length=160,
    armor=25,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=115,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=49,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Independent patrol frigate with extended endurance and reanimation bay",
    long_description=(
        "The Thylacine is the Canopan independent operator -- the ship sent to patrol a "
        "system alone for weeks, making decisions without backup. Slower than the template "
        "but with substantially more hull integrity and endurance, the Thylacine stays on "
        "station longer than any equivalent patrol frigate. Its crew is supplemented by "
        "reanimated shells who handle the maintenance work that grinds down living crews "
        "on extended solo deployments -- hull cleaning, cargo handling, minor repairs, "
        "watch rotation for non-critical stations. A Thylacine captain may be the "
        "highest-ranking Canopan military officer in a system. The ship's reanimation bay "
        "means even combat losses on a solo patrol are partially recoverable -- a captain "
        "who loses crew in an engagement can restore them to shell status and keep the "
        "ship operational until reinforcements arrive."
    ),
    exterior_appearance_description=(
        "A 160-meter military spacecraft with a dark grey hull. A heavy, rounded oblong body "
        "with a blunt curved front. Layered armour plates across the entire hull. A particle "
        "cannon housing along the top, framed by gold moulding. A torpedo bay in the lower "
        "front behind heavy doors with gold filigree borders. A heavy laser turret in a gilded "
        "housing. Engine bells recessed into the rear behind armoured cowlings. Crimson trim "
        "along every armour plate edge. Gold ornamentation -- emperor's crest in raised relief "
        "on the front, gilded borders around weapon housings, rank insignia on the sides. "
        "Crimson and gold banners trailing from ornamental poles on the top spine. Dim amber "
        "lights set into the armour seams."
    ),
    interior_appearance_description=(
        "More liveable than the Smilodon -- the Thylacine is designed for extended solo "
        "patrols, and it shows. Crew quarters are small but private, with personal storage "
        "and reading lights. A wardroom serves as dining area, briefing room, and the "
        "only social space aboard. The reanimation bay is below the waterline amidships, "
        "sealed behind a heavy bulkhead. The shell compartment aft houses the reanimated "
        "when not on duty -- rows of standing alcoves where the shells wait, motionless, "
        "until called. The ship has the grim domesticity of a place people live in for "
        "a long time without ever being comfortable."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 28}, {"shells": 22}],
    secondary_crew=[
        {"gunners": 8},
        {"torpedo_crew": 4},
        {"reanimation_technicians": 2},
        {"shells": 14},
    ],
    additional_systems=[
        "Reanimation bay (small -- capacity 4)",
        "Shell compartment (standing alcoves)",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

BUNYIP = ShipTemplate(
    name="Bunyip",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Scout Frigate",
    combat_role="Deep reconnaissance / intelligence gathering",
    length=180,
    armor=15,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=90,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=56,
    default_weapons=[weapons.ION_CANNON],
    default_small_craft=[],
    short_description="Hard-jump intelligence frigate with extended deep-deployment endurance",
    long_description=(
        "The Bunyip is the Canopan scout frigate -- a hard-jump-capable vessel built for "
        "deep reconnaissance behind enemy lines. It sacrifices most combat capability for "
        "an oversized jump drive, excellent sensors, and the extended supply duration that "
        "Canopan construction provides. Where other factions' scout frigates rely on speed "
        "and stealth to survive, the Bunyip relies on endurance -- it stays deployed longer "
        "than anyone expects, watching from positions that faster ships would have abandoned "
        "weeks ago. The Bunyip is the only hard-jump Canopan frigate. Its crew is elite "
        "and its construction expensive. Shell labor handles the maintenance and manual "
        "work that would otherwise consume the small living crew's energy during months-long "
        "intelligence deployments. The Bunyip's higher sensor profile compared to other "
        "factions' scout frigates is a known weakness -- Canopan engineers could not make "
        "the ship both tough and invisible."
    ),
    exterior_appearance_description=(
        "A 180-meter military spacecraft with a dark grey hull. A long, rounded body with a "
        "curved front and a thick oval cross-section. Layered armour plates across the hull. "
        "An ion cannon housing on the top. Minimal external sensor equipment. Engine bells "
        "recessed into the rear behind armoured cowlings. Crimson trim along the armour plate "
        "edges. Gold filigree along the weapon housing and around the bridge. A gold emperor's "
        "crest on both sides. A single crimson banner trailing from the top spine. Dim amber "
        "lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The forward third is sensor equipment and analysis stations. The hard-jump drive "
        "occupies the aft third. Living spaces are compressed into the middle -- small "
        "private berths, a galley, and a combined briefing and analysis room where the "
        "intelligence team works. The reanimation bay is minimal -- barely a closet with "
        "a single operating table, included because a crew member lost during a months-long "
        "deployment cannot be replaced. The shell compartment is a row of standing alcoves "
        "in the engineering section. The ship runs quiet and dark, with the tense, stripped-"
        "down feel of a vessel operating where it should not be."
    ),
    minimum_crew=[{"officers": 5}, {"crew": 18}, {"shells": 12}],
    secondary_crew=[
        {"intelligence_analysts": 6},
        {"sensor_specialists": 4},
        {"reanimation_technician": 1},
        {"shells": 6},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Extended passive sensor array",
        "Intelligence analysis suite",
        "Reanimation bay (minimal -- capacity 1)",
        "Shell compartment (standing alcoves)",
        "Extended consumable storage",
    ],
)

AMAROK = ShipTemplate(
    name="Amarok",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Escort Frigate",
    combat_role="Convoy protection / anti-small-craft",
    length=158,
    armor=25,
    speed=Speed.MEDIUM,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=115,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=35,
    default_weapons=[weapons.PLASMA_CANNON, weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Heavy escort frigate with reanimation bay and shell damage control teams",
    long_description=(
        "The Amarok provides a defensive umbrella over Canopan convoys and transport "
        "groups. Slower than the template escort frigate, the Amarok compensates with "
        "hull integrity that lets it absorb fire meant for the ships it protects. Its "
        "plasma cannon is optimized for anti-small-craft work, engaging incoming bombers "
        "and torpedo craft while the convoy continues on course. The Amarok's reanimation "
        "bay and shell damage control teams give it the Canopan staying power -- hull "
        "breaches are sealed by shells working in vacuum, damaged systems are repaired by "
        "shell labor teams directed by a living engineer, and battle casualties are "
        "reanimated and returned to damage control duty. A convoy escort that can repair "
        "itself mid-engagement is a convoy escort that remains on station when the enemy "
        "expects it to withdraw."
    ),
    exterior_appearance_description=(
        "A 158-meter military spacecraft with a dark grey hull. A compact, rounded oblong body "
        "with a blunt front and thick hull. Layered armour plates across the hull. A plasma "
        "cannon housing on the top, framed by gold moulding. A light ion turret in a gilded "
        "housing behind it. Engine bells recessed into the rear behind armoured cowlings. "
        "Crimson trim along every armour plate edge. Gold ornamentation -- emperor's crest on "
        "both sides, gilded borders around weapon housings. Crimson and gold banners trailing "
        "from ornamental poles on the top spine. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The bridge is forward, conventional, with manual stations and a clear sightline "
        "to the main displays. The plasma cannon's power feeds run through the core of "
        "the ship, radiating warmth during sustained fire. The reanimation bay is "
        "amidships, adjacent to the main corridor for rapid casualty transport. Shell "
        "damage control teams stage from a compartment near engineering, ready to deploy "
        "to any section of the hull. The living crew learn to ignore the shells moving "
        "through the corridors on their way to work details -- or they learn to request "
        "a transfer."
    ),
    minimum_crew=[{"officers": 7}, {"crew": 25}, {"shells": 22}],
    secondary_crew=[
        {"gunners": 10},
        {"reanimation_technicians": 2},
        {"shells": 14},
    ],
    additional_systems=[
        "Reanimation bay (small -- capacity 4)",
        "Shell compartment",
        "Reinforced hull structure",
        "Multi-target tracking array",
    ],
)


TANIWHA = ShipTemplate(
    name="Taniwha",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Fleet Destroyer",
    combat_role="Capital ship escort / point defense umbrella",
    length=260,
    armor=60,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=330,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=42,
    default_weapons=[weapons.RAILGUN, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy fleet destroyer with triple point defense batteries and shell repair crews",
    long_description=(
        "The Taniwha is the guardian of the Canopan battle fleet. Its job is protecting "
        "capital ships from bomber, torpedo, and gunship attacks, and it does this through "
        "a combination of triple heavy laser turrets and the sheer hull integrity to "
        "remain on station while absorbing hits meant for the ships it guards. The "
        "Taniwha's shell complement is its hidden advantage: reanimated damage control "
        "teams work continuously during battle, sealing breaches, rerouting damaged "
        "systems, and performing hull repairs that would be impossible for a living crew "
        "under fire. Shells work in vacuum without suits, in fires without protection, "
        "and in radiation zones without hesitation. A Taniwha that should be combat-"
        "ineffective keeps fighting because its shells are still working. The reanimation "
        "bay restores combat casualties to shell status within the hour, feeding the "
        "damage control machine with the fleet's own dead."
    ),
    exterior_appearance_description=(
        "A 260-meter military spacecraft with a dark grey hull. A broad, heavy rounded body "
        "with a thick circular cross-section and a blunt domed front. Layered armour plates "
        "across the entire hull in pronounced overlapping rows. A railgun housing along the "
        "top, framed by ornamental gold moulding. Three heavy laser turrets in gilded housings "
        "spaced along the top and sides. Engine bells recessed into the rear behind heavily "
        "armoured cowlings with crimson rims. Crimson trim along every armour plate edge. "
        "Extensive gold ornamentation -- the emperor's crest in raised gold relief on the "
        "front, gold laurel motifs along the top spine, gilded rank insignia and fleet "
        "markings on the sides. Multiple crimson and gold banners trailing from ornamental "
        "poles along the top spine. Dim amber lights set into the armour seams. Ship name in "
        "gold lettering on both sides."
    ),
    interior_appearance_description=(
        "The three point defense battery stations are distributed port, starboard, and "
        "dorsal, each manned by living gunners with shell ammunition handlers feeding the "
        "weapons. The reanimation bay is a sealed section amidships with multiple "
        "operating tables and preservation equipment -- larger than a frigate's bay, "
        "capable of processing several casualties simultaneously. The shell compartment "
        "is a long, unlit corridor of standing alcoves near engineering. The bridge is "
        "forward, conventional, built for endurance rather than elegance. The point "
        "defense bays are maintained to strict standards -- the living crew know that "
        "their survival depends on those turrets working, and the shells that feed "
        "them ammunition never tire."
    ),
    minimum_crew=[{"officers": 16}, {"crew": 80}, {"shells": 70}],
    secondary_crew=[
        {"gunners": 30},
        {"point_defense_crew": 25},
        {"reanimation_technicians": 4},
        {"shells": 50},
    ],
    additional_systems=[
        "Reanimation bay (medium -- capacity 8)",
        "Shell compartment (standing alcoves)",
        "Reinforced hull structure",
        "Redundant point defense power feeds",
        "Vacuum-rated shell deployment system",
    ],
)

THUNDERBIRD = ShipTemplate(
    name="Thunderbird",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Hunter Destroyer",
    combat_role="Anti-piracy / pursuit / torpedo attack",
    length=245,
    armor=45,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=270,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=42,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.ANTIMATTER_TORPEDO, weapons.ION_TURRET],
    default_small_craft=[],
    short_description="Heavy pursuit destroyer with torpedo and extended endurance",
    long_description=(
        "The Thunderbird is the Canopan pursuit ship -- though 'pursuit' is generous for "
        "a ship slower than the template. The Thunderbird does not chase targets down "
        "through speed. It hunts them through endurance. A corvette or frigate fleeing a "
        "Thunderbird can outrun it in a sprint, but the Thunderbird stays on the trail "
        "for weeks, following through medium-jump routes with supplies to outlast its "
        "prey. Eventually the target runs out of consumables, makes a mistake, or turns "
        "to fight -- and the Thunderbird closes with a heavy particle cannon and an "
        "antimatter torpedo. It arrives slower but it arrives heavier, and in a fight "
        "against a target that has been running for days, heavier wins. The Thunderbird "
        "often operates in pairs for mutual support. A pair showing up in a system is a "
        "statement that the Canopan navy has decided someone in this system needs to die."
    ),
    exterior_appearance_description=(
        "A 245-meter military spacecraft with a dark grey hull. A lean, rounded body with an "
        "oval cross-section -- narrow in proportion, elongated, still heavy and "
        "curved. A heavy particle cannon housing extends from the front, framed by gold "
        "moulding. A torpedo bay in the lower front behind heavy doors with gilded borders. An "
        "ion turret in a gilded housing on top. Engine bells recessed into the rear behind "
        "armoured cowlings. Crimson trim along every armour plate edge. Gold ornamentation -- "
        "emperor's crest on both sides, gilded weapon housing frames, rank insignia. Crimson "
        "and gold banners trailing from the top spine. Dim amber lights set into the armour "
        "seams."
    ),
    interior_appearance_description=(
        "Designed for the long hunt. Crew quarters are functional, with private berths "
        "and a small mess. The torpedo room is forward, tended by a mixed crew of living "
        "ratings and shells. The reanimation bay is amidships, included because a "
        "weeks-long pursuit cannot afford to lose trained crew without recovery. The "
        "shell compartment houses reanimated labor for the maintenance and repair work "
        "that accumulates on a destroyer operating independently for extended periods. "
        "The ship has the patient, heavy atmosphere of something built to wait."
    ),
    minimum_crew=[{"officers": 14}, {"crew": 60}, {"shells": 45}],
    secondary_crew=[
        {"gunners": 18},
        {"torpedo_crew": 6},
        {"reanimation_technicians": 3},
        {"shells": 23},
    ],
    additional_systems=[
        "Reanimation bay (medium -- capacity 6)",
        "Shell compartment (standing alcoves)",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

MOSASAUR = ShipTemplate(
    name="Mosasaur",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.BATTLESHIP,
    ship_archetype="Siege Destroyer",
    combat_role="Anti-capital firepower on a destroyer hull",
    length=225,
    armor=25,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.MEDIUM,
    max_hull_points=165,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=35,
    default_weapons=[weapons.SIEGE_CANNON],
    default_small_craft=[],
    short_description="Siege cannon platform with reinforced hull and shell gunnery labor",
    long_description=(
        "The Mosasaur mounts a siege cannon on a destroyer-sized hull. Everything else "
        "has been sacrificed to make this possible: no point defense, no secondary "
        "weapons, minimal armor even by siege destroyer standards. The Canopan version "
        "is marginally tougher than the template -- enough to survive a hit that would "
        "kill another faction's siege destroyer, which may be the difference between "
        "firing one more shot and dying. The siege cannon's loading and power cycling "
        "require significant manual labor, handled by reanimated shells who work the "
        "ammunition feeds and capacitor banks with the tireless, mechanical efficiency "
        "that characterizes shell labor. A Mosasaur without its Taniwha escorts is dead "
        "the moment enemy small craft reach it -- but a Mosasaur behind a Taniwha screen "
        "puts siege-class fire on enemy capital ships at extreme range."
    ),
    exterior_appearance_description=(
        "A 225-meter military spacecraft with a dark grey hull. A squat, heavily reinforced "
        "rounded body dominated by a massive siege cannon housing running the full length of "
        "the top -- the housing framed by elaborate gold moulding and laurel motifs. The hull "
        "beneath is a thick, rounded frame with pronounced overlapping armour plates. Engine "
        "bells recessed deep into the rear behind armoured cowlings. Crimson trim along every "
        "armour plate edge. Gold ornamentation -- emperor's crest in raised relief on the "
        "front, gilded borders along the cannon housing, rank insignia on the sides. Crimson "
        "and gold banners trailing from ornamental poles. Dim amber lights set into the armour "
        "seams."
    ),
    interior_appearance_description=(
        "The ship is built around the weapon. The siege cannon's magnetic accelerator "
        "runs the full length of the vessel, with crew spaces, engineering, and the shell "
        "compartment packed into the remaining volume. The living crew occupy a cramped "
        "forward section -- bridge, minimal berths, a galley barely large enough to stand "
        "in. The shells work aft in the cannon's loading section, a loud, hot space where "
        "the capacitor banks cycle with a subsonic thrum the crew feels in their teeth. "
        "The reanimation bay is a single table in a closet. The Mosasaur exists to fire "
        "its cannon, and everything aboard serves that purpose."
    ),
    minimum_crew=[{"officers": 8}, {"crew": 35}, {"shells": 25}],
    secondary_crew=[
        {"gunnery_specialists": 10},
        {"reanimation_technician": 1},
        {"shells": 18},
    ],
    additional_systems=[
        "Spinal siege cannon mount",
        "Reanimation bay (minimal -- capacity 1)",
        "Shell compartment",
        "Reinforced hull structure",
    ],
)


MEGALANIA = ShipTemplate(
    name="Megalania",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Heavy Cruiser",
    combat_role="Line combatant / fleet backbone",
    length=445,
    armor=80,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=530,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=56,
    default_weapons=[
        weapons.PRECISION_RAILGUN,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Over-built line cruiser with full reanimation bay and massive shell complement",
    long_description=(
        "The Megalania is the Canopan main line combatant and the ship where their "
        "attrition doctrine becomes genuinely frightening. It holds a position in the "
        "fleet battle line and slugs it out with its opposite number -- and keeps slugging "
        "long after the other ship would have been forced to withdraw. The Megalania's "
        "hull integrity exceeds the template by a wide margin, its armor is at the "
        "maximum of the range, and its reanimation bay processes battle casualties "
        "continuously during an engagement. As the battle grinds on, the Megalania's "
        "living crew fight the ship while its growing complement of freshly reanimated "
        "shells seal breaches, repair systems, feed ammunition, and perform the physical "
        "labor that keeps the ship fighting. The enemy sees a cruiser that should be "
        "combat-ineffective and watches it keep firing. When two fleets meet, the "
        "Megalania engagement is where the Canopan advantage in endurance decides the "
        "outcome."
    ),
    exterior_appearance_description=(
        "A 445-meter military spacecraft with a dark grey hull. A massive, broad rounded body "
        "with a thick oval cross-section and a blunt domed front. Layered armour plates in "
        "heavy overlapping rows across the entire hull. A precision railgun housing along the "
        "top, framed by elaborate gold moulding. Weapon batteries in rounded housings along "
        "both sides, each housing bordered by gold filigree. Point-defense turrets along the "
        "lower hull. Engine bells recessed into the rear behind heavily armoured cowlings. "
        "Crimson trim along every armour plate edge. Extensive gold ornamentation -- the "
        "emperor's crest in large raised gold relief on the front, gold laurel motifs along "
        "the top spine, gilded rank insignia and fleet markings on the sides, gold filigree "
        "borders around every weapon housing and hull opening. Multiple crimson and gold "
        "banners trailing from ornamental poles along the top spine. Ship name in gold "
        "lettering on both sides. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The reanimation bay is a full medical section amidships -- multiple operating "
        "tables, preservation systems, chemical storage, and a recovery area where "
        "freshly reanimated shells stand in rows waiting for assignment. The bay operates "
        "continuously during battle, staffed by reanimation technicians who have learned "
        "to work fast and not think too hard about who arrives on their tables. The "
        "shell compartment is an unlit deck below the main corridors, with hundreds of "
        "standing alcoves. During combat, shells stream upward through dedicated access "
        "trunks to damage control stations throughout the hull. The bridge is a "
        "reinforced compartment forward with conventional stations. Crew quarters are "
        "functional, grouped by department. The living crew develop an awareness of the "
        "shells as a presence in the ship -- footsteps in corridors that should be empty, "
        "shapes moving in the dark lower decks, the faint chemical smell that marks "
        "every Canopan warship."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 40}, {"crew": 280}, {"shells": 200}],
    secondary_crew=[
        {"gunners": 65},
        {"point_defense_crew": 25},
        {"reanimation_technicians": 8},
        {"shells": 135},
    ],
    additional_systems=[
        "Reanimation bay (full -- capacity 20)",
        "Shell compartment (standing alcoves, 150+)",
        "Shell deployment access trunks",
        "Reinforced hull structure",
        "Redundant critical systems",
        "Extended consumable storage",
    ],
)

LIVYATAN = ShipTemplate(
    name="Livyatan",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Light Cruiser",
    combat_role="Flanking operations / independent task force lead",
    length=415,
    armor=60,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=380,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[weapons.HEAVY_RAILGUN, weapons.LASER_TURRET, weapons.LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy medium-jump cruiser for sustained flanking operations",
    long_description=(
        "The Livyatan is the largest Canopan combat ship that can use medium jump points. "
        "It serves as the backbone of flanking forces -- when a Canopan task force comes "
        "through a medium jump to hit the enemy's rear, the Livyatan is the biggest gun "
        "they have. Slower than the template light cruiser, the Livyatan compensates with "
        "hull integrity that lets it absorb fire from ships that should outclass it. A "
        "Canopan flanking force led by a Livyatan fights differently than other factions' "
        "flanking groups: it arrives slower but hits harder per ship, and it holds its "
        "position through endurance rather than speed. The Livyatan's reanimation bay and "
        "shell complement give it the staying power to operate independently for extended "
        "periods, and its supply endurance exceeds the template significantly."
    ),
    exterior_appearance_description=(
        "A 415-meter military spacecraft with a dark grey hull. A rounded, elongated body with "
        "an oval cross-section. Layered armour plates across the hull. A heavy railgun housing "
        "along the top, framed by gold moulding. Two laser turrets in gilded housings on the "
        "upper hull. Engine bells recessed into the rear behind armoured cowlings. Crimson "
        "trim along every armour plate edge. Gold ornamentation -- emperor's crest in raised "
        "relief on the front, gilded borders around weapon housings, rank insignia and fleet "
        "markings in gold on the sides. Crimson and gold banners trailing from ornamental "
        "poles on the top spine. Ship name in gold lettering. Dim amber lights set into the "
        "armour seams."
    ),
    interior_appearance_description=(
        "The interior reflects the ship's dual role as flanking combatant and independent "
        "operator. Crew quarters are a step above the spartan standard of smaller Canopan "
        "vessels -- still austere, but with private berths and a larger mess for the "
        "extended independent deployments the Livyatan undertakes. The reanimation bay "
        "is full-sized, amidships. The shell compartment is one deck below the main "
        "corridors. A task force command section includes additional stations for "
        "coordinating a flanking group. The ship has a settled, heavy atmosphere -- the "
        "weight of a vessel that expects to be somewhere difficult for a long time."
    ),
    minimum_crew=[{"senior_officers": 6}, {"officers": 30}, {"crew": 200}, {"shells": 140}],
    secondary_crew=[
        {"gunners": 40},
        {"point_defense_crew": 15},
        {"reanimation_technicians": 6},
        {"task_force_staff": 8},
        {"shells": 80},
    ],
    additional_systems=[
        "Reanimation bay (full -- capacity 15)",
        "Shell compartment (standing alcoves, 100+)",
        "Shell deployment access trunks",
        "Task force coordination suite",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

MASTODON = ShipTemplate(
    name="Mastodon",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Command Cruiser",
    combat_role="Fleet coordination / flagship for medium-jump task forces",
    length=430,
    armor=50,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=380,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=56,
    default_weapons=[weapons.HEAVY_PARTICLE_CANNON, weapons.HEAVY_LASER_TURRET],
    default_small_craft=[],
    short_description="Heavy command cruiser with full reanimation facilities",
    long_description=(
        "The Mastodon is where a Canopan admiral sits when leading a flanking force or an "
        "independent task group. Reduced armament in exchange for expanded communications, "
        "sensor fusion, and command-and-control facilities -- but built on the same "
        "over-engineered Canopan hull that makes every ship in their fleet harder to kill "
        "than expected. The Mastodon makes a group of ships fight as a fleet rather than "
        "a collection of individuals. Its command section is larger than the template, "
        "reflecting the Canopan preference for redundant staff and backup systems. The "
        "Mastodon's reanimation bay serves a fleet coordination role: it can receive "
        "casualties from other ships in the task force, reanimate them, and return them "
        "as shell labor to ships that have lost crew. The Mastodon is a command ship that "
        "also serves as a replacement depot -- feeding the fleet's attrition machine."
    ),
    exterior_appearance_description=(
        "A 430-meter military spacecraft with a dark grey hull. A broad rounded body with a "
        "raised, enlarged bridge superstructure near the front -- an ornate structure with "
        "gilded frames around the bridge windows and gold filigree across its surfaces. "
        "Communications antenna clusters mounted on the bridge superstructure in gilded "
        "housings. A heavy particle cannon housing extends from the front, framed by gold "
        "moulding. A heavy laser turret in a gilded housing behind the bridge. Engine bells "
        "recessed into the rear behind armoured cowlings. Crimson trim along every armour "
        "plate edge. Extensive gold ornamentation -- the emperor's crest in large raised "
        "relief on the front and on the bridge superstructure, gold laurel motifs, gilded rank "
        "insignia. Multiple crimson and gold banners trailing from ornamental poles on the top "
        "spine and from the bridge superstructure. Ship name in gold lettering on both sides. "
        "Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The command section is the ship's heart -- a large, reinforced compartment with "
        "stations for the admiral, flag staff, and communications officers. Additional "
        "briefing rooms and an intelligence analysis suite surround it. The reanimation "
        "bay is larger than a standard cruiser's, with additional capacity for processing "
        "casualties transferred from other ships. A dedicated shuttle bay receives "
        "casualty transfers during battle. The shell compartment houses both the ship's "
        "own shells and a reserve of freshly reanimated shells awaiting transfer to "
        "other vessels. The living crew quarters are the best in the Canopan fleet at "
        "this size class -- still austere by other factions' standards, but recognizing "
        "that a flag crew on extended deployment needs functional comfort."
    ),
    minimum_crew=[{"senior_officers": 8}, {"officers": 35}, {"crew": 220}, {"shells": 130}],
    secondary_crew=[
        {"gunners": 20},
        {"flag_staff": 15},
        {"communications_officers": 12},
        {"reanimation_technicians": 8},
        {"shells": 65},
    ],
    additional_systems=[
        "Fleet command section",
        "Reanimation bay (large -- capacity 25, fleet casualty processing)",
        "Casualty transfer shuttle bay",
        "Shell compartment (standing alcoves, 100+)",
        "Shell deployment access trunks",
        "Fleet communications suite",
        "Intelligence analysis suite",
        "Reinforced hull structure",
    ],
)


PTERODACTYL = ShipTemplate(
    name="Pterodactyl",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Battleship",
    combat_role="Aggressive line combatant / mobile capital",
    length=965,
    armor=95,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1900,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=84,
    default_weapons=[
        weapons.GAUSS_CANNON,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.PARTICLE_CANNON_BATTERY,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
        weapons.HEAVY_LASER_TURRET,
    ],
    default_small_craft=[],
    short_description="Slow, devastating battleship with industrial-scale reanimation facilities",
    long_description=(
        "The Pterodactyl is the Canopan battleship -- slower than any other faction's "
        "equivalent but tougher than all of them. Where other factions' battleships close "
        "and kill through speed, the Pterodactyl advances and kills through refusal to "
        "stop. It cannot chase anything that runs. But anything that stands and fights a "
        "Pterodactyl is fighting a ship that absorbs punishment that would cripple its "
        "opposite number, repairs damage mid-battle through hundreds of reanimated shells, "
        "and keeps its guns firing through crew losses that would render another "
        "battleship combat-ineffective. The Pterodactyl's reanimation facilities operate "
        "at industrial scale -- dozens of casualties processed per hour during heavy "
        "combat, each one returned to the ship as a shell performing damage control, "
        "ammunition handling, or hull repair. The living crew fight the ship. The dead "
        "crew keep it alive. Over the course of a prolonged engagement, the Pterodactyl "
        "becomes more shell than human -- its living crew shrinking, its shell complement "
        "growing, its combat effectiveness barely diminished because the work that matters "
        "most is the work shells can do."
    ),
    exterior_appearance_description=(
        "A 965-meter military spacecraft with a dark grey hull. A massive, broad rounded body "
        "with a thick oval cross-section and a blunt domed front. Layered armour plates in "
        "heavy overlapping rows across the entire hull, giving a pronounced reptilian texture. "
        "A gauss cannon housing along the top, framed by elaborate gold moulding with laurel "
        "and wreath motifs. Weapon batteries in rounded housings along both sides in two "
        "tiers, each housing bordered by gold filigree. Point-defense turrets along the hull. "
        "Engine bells in a recessed cluster at the rear behind heavily armoured cowlings. "
        "Crimson trim along every armour plate edge. Lavish gold ornamentation -- the "
        "emperor's crest in large raised gold relief on the front and both sides, gold laurel "
        "motifs along the top spine, gilded borders around every weapon housing, filigree "
        "panels between the weapon tiers. Multiple crimson and gold banners trailing from "
        "ornamental poles along the top spine. Ship name in gold lettering at large scale on "
        "both sides. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The Pterodactyl's interior is divided into living decks and shell decks. The "
        "living decks -- bridge, officer country, crew quarters, the wardroom, medical -- "
        "are in the upper and forward sections, lit in dim amber, functional but "
        "recognizable as spaces for people. The shell decks occupy the lower and aft "
        "sections: long, unlit corridors lined with standing alcoves, connected to every "
        "section of the hull by access trunks. The reanimation bay is a full industrial "
        "facility amidships -- a cold, brightly lit space with rows of operating tables, "
        "chemical systems, and the mechanical efficiency of a production line. During "
        "battle, casualties flow down from the fighting decks and shells flow up from "
        "the bays below. The living crew learn not to look too closely at the shells "
        "they pass in the corridors. Some of them were crewmates an hour ago."
    ),
    minimum_crew=[{"senior_officers": 20}, {"officers": 120}, {"crew": 1100}, {"shells": 800}],
    secondary_crew=[
        {"gunners": 200},
        {"point_defense_crew": 100},
        {"reanimation_technicians": 20},
        {"medical": 30},
        {"shells": 500},
    ],
    additional_systems=[
        "Reanimation bay (industrial -- capacity 50+, continuous processing)",
        "Shell compartment (standing alcoves, 600+)",
        "Shell deployment access trunks (multiple)",
        "Reinforced hull structure",
        "Redundant critical systems",
        "Battle casualty recovery system",
        "Extended consumable storage",
    ],
)

ARCHELON = ShipTemplate(
    name="Archelon",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Carrier",
    combat_role="Force projection / strike craft coordination",
    length=1260,
    armor=60,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1500,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=84,
    default_weapons=[
        weapons.LASER_TURRET,
        weapons.LASER_TURRET,
        weapons.LASER_PD,
        weapons.LASER_PD,
        weapons.LASER_PD,
    ],
    default_small_craft=[
        ("Sabertooth", 10),
        ("Sabertooth", 10),
        ("Raptor", 10),
        ("Tarpan", 10),
    ],
    short_description="Massive carrier deploying durable strike wings with onboard reanimation for pilots",
    long_description=(
        "The Archelon is the Canopan fleet carrier. It deploys four wings -- typically "
        "two wings of Sabertooth bombers, one wing of Raptor fighters, and one wing of "
        "Tarpan gunships -- a strike package built for the same attrition doctrine that "
        "defines every Canopan warship. The Archelon's embarked craft are tougher than "
        "other factions' equivalents: Sabertooths that survive hits other bombers would "
        "not, Raptors that outlast faster fighters, Tarpans that walk through escort "
        "screens. The carrier itself is slower and heavier than the template, with hull "
        "integrity that lets it absorb punishment while recovering and rearming its wings. "
        "The Archelon's most distinctive feature is its pilot reanimation bay -- a "
        "dedicated facility that reanimates killed pilots to shell status for immediate "
        "reassignment to non-combat flight duties, freeing living pilots for the next "
        "strike. Shells cannot pilot combat missions, but they can ferry craft between "
        "hangars, perform flight checks, and taxi returning craft into launch cradles, "
        "reducing the workload on surviving living pilots. Medium-jump capable, allowing "
        "it to project strike power through flanking routes."
    ),
    exterior_appearance_description=(
        "A 1260-meter military spacecraft with a dark grey hull. A broad, rounded oblong -- "
        "wide and heavy with a curved top, flat bottom, and blunt rounded front. The sides "
        "bulge outward. Layered armour plates visible at the edges where sections overlap, "
        "giving a scaled, reptilian texture. Hangar openings recessed behind heavy blast doors "
        "framed by ornate gilded moulding. Engine bells distributed across the rear and "
        "underside behind armoured cowlings. Crimson trim along every armour plate edge. "
        "Extensive gold ornamentation -- filigree borders around the hangar frames, the "
        "emperor's crest in raised gold relief on the front, laurel motifs along the top "
        "spine, gilded rank insignia flanking the crest. Crimson and gold bands around the "
        "front section. Multiple crimson and gold banners trailing from ornamental poles along "
        "the top spine and flanking the hangar openings. Ship name in gold lettering at large "
        "scale on both sides. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The Archelon's interior is dominated by its four hangar bays -- vast, dimly lit "
        "spaces where forty strike craft sit in mechanical launch cradles. Shell hangar "
        "crews handle the physical work of rearming, refueling, and repositioning craft "
        "-- carrying torpedoes, connecting fuel lines, and hauling damaged craft to repair "
        "bays with the tireless efficiency of the reanimated. The pilot reanimation bay "
        "is adjacent to the flight operations center, a grim necessity that the flight "
        "crews try not to think about. The living crew spaces are extensive -- the Archelon "
        "carries thousands and must function as a self-contained community for months. "
        "The shell compartment is the largest on any Canopan vessel: an entire deck of "
        "standing alcoves, hundreds of reanimated waiting in the dark for the next call."
    ),
    minimum_crew=[{"senior_officers": 30}, {"officers": 200}, {"crew": 800}, {"shells": 2000}],
    secondary_crew=[
        {"embarked_craft_pilots": 40},
        {"flight_deck_crew": 150},
        {"hangar_technicians": 80},
        {"ship_gunners": 40},
        {"reanimation_technicians": 15},
        {"medical": 50},
        {"shells": 410},
    ],
    additional_systems=[
        "Hangar bays (x4, 10 craft each)",
        "Craft maintenance and rearm facilities",
        "Pilot reanimation bay (dedicated -- capacity 10)",
        "Reanimation bay (industrial -- capacity 40+, continuous processing)",
        "Shell compartment (standing alcoves, 500+)",
        "Shell deployment access trunks (multiple)",
        "Flight operations center",
        "Reinforced hull structure",
        "Reinforced hangar armor",
        "Extended consumable storage",
    ],
)

MAMMOTH = ShipTemplate(
    name="Mammoth",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Dreadnought",
    combat_role="Siege platform / strategic deterrent / fleet anchor",
    length=1920,
    armor=100,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=3200,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=98,
    default_weapons=[weapons.SIEGE_CANNON, weapons.SIEGE_CANNON, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Maximum-armor dreadnought with twin siege cannons and a city of shells",
    long_description=(
        "The Mammoth is the largest and most powerful vessel in the Canopan fleet. It "
        "does not chase. It does not maneuver. It arrives, and everything at extreme "
        "range begins to die. Its twin siege cannons fire with the same accuracy as any "
        "faction's dreadnought -- Canopan weapon technology holds no advantage. What the "
        "Mammoth has instead is hull integrity that exceeds every other dreadnought in "
        "known space, maximum armor, and a reanimated workforce measured in the hundreds. "
        "A Mammoth under sustained fire repairs damage as fast as some ships take it. "
        "Hull breaches are sealed by shell teams working in vacuum. Damaged power "
        "conduits are rerouted by shells who cannot feel pain. Fires are walked into and "
        "extinguished by reanimated who do not burn, or rather, burn without caring. The "
        "Mammoth's reanimation facilities are the largest afloat -- an industrial operation "
        "that processes casualties from across the fleet, returning them as shells to any "
        "ship that needs them. Only a handful of Mammoths exist. Each one is a strategic "
        "asset, a fleet anchor, and a floating monument to the Canopan willingness to "
        "use death as a resource."
    ),
    exterior_appearance_description=(
        "A 1920-meter military spacecraft with a dark grey hull. A massive, rounded oblong "
        "body with a thick oval cross-section and a blunt, domed front. Layered armour plates "
        "in heavy overlapping rows across the entire hull, giving a pronounced scaled texture. "
        "Twin siege cannon housings along the top, each framed by elaborate gold moulding with "
        "wreath and laurel motifs. Point-defense turrets in recessed mounts along the sides. "
        "Engine bells in a recessed cluster at the rear behind heavily armoured cowlings. "
        "Crimson trim along every armour plate edge. Lavish gold ornamentation across the "
        "hull -- the emperor's personal crest in massive raised gold relief on the front, "
        "gold filigree covering much of the upper hull surface, gilded borders around every "
        "weapon housing and hull opening, laurel garlands and wreath motifs in gold along the "
        "top spine, gilded rank insignia and dynasty markings at large scale on the sides. "
        "Numerous crimson and gold banners trailing from ornamental poles along the top spine "
        "and sides. Crimson and gold bands around the front section. Ship name in gold "
        "lettering at massive scale on both sides. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The Mammoth is a city. Living crew spaces occupy the upper decks -- the bridge, "
        "officer country, crew quarters, mess halls, medical bays, and the few "
        "recreational spaces that a Canopan warship permits. Below that is the shell "
        "city: an entire section of the ship given over to standing alcoves, work "
        "staging areas, and the access trunks that connect them to every part of the "
        "hull. The reanimation bay is a factory -- rows of operating tables, chemical "
        "processing systems, preservation vats, and the staff who run them around the "
        "clock during battle. Casualties from across the fleet arrive by shuttle, are "
        "processed, and return to service as shells assigned wherever need is greatest. "
        "The living crew walk above the shell decks and try not to think about the "
        "hundreds below them, standing in the dark, waiting. Veterans describe the "
        "Mammoth as a ship that is always slightly heavier than it should be -- not in "
        "any measurable way, but in the sense that there is always more presence aboard "
        "than the living crew accounts for."
    ),
    minimum_crew=[{"senior_officers": 55}, {"officers": 380}, {"crew": 4500}, {"shells": 10000}],
    secondary_crew=[
        {"gunners": 300},
        {"point_defense_crew": 60},
        {"fleet_coordination_staff": 60},
        {"reanimation_technicians": 40},
        {"medical": 100},
        {"shells": 800},
    ],
    additional_systems=[
        "Reanimation bay (industrial -- capacity 80+, fleet-scale processing)",
        "Fleet casualty receiving bay (shuttle dock)",
        "Shell compartment (standing alcoves, 900+)",
        "Shell deployment access trunks (multiple, all decks)",
        "Reinforced hull structure (maximum rating)",
        "Redundant critical systems (triple redundancy)",
        "Twin spinal siege cannon mounts",
        "Extended consumable storage",
    ],
)


QUAGGA = ShipTemplate(
    name="Quagga",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Fleet Tender",
    combat_role="Resupply / ammunition and fuel transport",
    length=365,
    armor=35,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=220,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=63,
    default_weapons=[weapons.ION_TURRET, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Heavy fleet tender with shell cargo crews and preservation compound stores",
    long_description=(
        "The Quagga is the Canopan logistics backbone. It carries fuel, ammunition, spare "
        "parts, preservation compounds for reanimation bays, and consumables for extended "
        "fleet operations. A Canopan fleet's operational range is limited by its Quaggas "
        "-- without them, ammunition runs dry, reanimation bays run out of compounds, and "
        "the fleet's attrition advantage vanishes. The Quagga carries a unique logistics "
        "burden: in addition to standard fleet supplies, it stocks the chemical compounds, "
        "replacement tissue, and preservation fluids that Canopan reanimation facilities "
        "consume at industrial rates during battle. Shell labor handles the physical work "
        "of cargo transfer -- moving crates, connecting fuel lines, hauling ammunition -- "
        "at a pace that living crews cannot sustain. Destroying a Canopan fleet's Quaggas "
        "doesn't just starve the fleet of ammunition. It starves the reanimation bays."
    ),
    exterior_appearance_description=(
        "A 365-meter military spacecraft with a dark grey hull. A bulky, rounded body with a "
        "thick oval cross-section. The midsection is a wide supply module with docking clamps "
        "and transfer booms along both sides, the docking fittings framed by gold moulding. An "
        "ion turret in a gilded housing on top. A point-defense mount at the rear. Layered "
        "armour plates across the hull. Engine bells recessed into the rear behind armoured "
        "cowlings. Crimson trim along the armour plate edges and around the docking fittings. "
        "Gold ornamentation -- emperor's crest on both sides, gilded borders around the "
        "docking clamps. Crimson banners trailing from the top spine. Dim amber lights set "
        "into the armour seams."
    ),
    interior_appearance_description=(
        "The interior is mostly cargo space -- modular containers of ammunition, fuel "
        "cells, spare parts, and the sealed chemical storage that holds reanimation "
        "compounds. The chemical storage is kept at controlled temperature and "
        "segregated from other cargo. Shell labor teams work the cargo bays continuously "
        "during resupply operations, moving with the mechanical efficiency that makes "
        "shell labor so effective for physical work. Crew spaces forward are functional "
        "and unceremonious. No reanimation bay -- the Quagga carries the supplies, not "
        "the facilities."
    ),
    minimum_crew=[{"officers": 12}, {"crew": 55}, {"shells": 40}],
    secondary_crew=[{"cargo_handlers": 15}, {"shells": 30}],
    additional_systems=[
        "Modular cargo system",
        "Reanimation compound storage (temperature-controlled)",
        "Shell compartment",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

DODO = ShipTemplate(
    name="Dodo",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CORVETTE,
    ship_archetype="Logistics Corvette",
    combat_role="Emergency resupply / hard-jump logistics",
    length=62,
    armor=12,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=50,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump logistics corvette carrying reanimation compounds to deep operations",
    long_description=(
        "The Dodo is the smallest dedicated logistics vessel in the Canopan fleet, built "
        "around a hard-jump drive. It carries limited supplies -- enough to resupply a "
        "Bunyip scout frigate operating deep behind enemy lines. The Dodo's most critical "
        "cargo is preservation compound: without regular resupply, a Canopan ship's "
        "reanimation bay becomes inoperable and its existing shells begin to degrade. "
        "The Dodo keeps deep operations alive in both senses -- supplying food and "
        "ammunition for the living crew, and the chemicals that keep the shells working. "
        "A small vessel with a skeleton crew, the Dodo is not meant to fight. It shows "
        "up where it is needed, delivers its cargo, and disappears."
    ),
    exterior_appearance_description=(
        "A 62-meter military spacecraft with a dark grey hull. A compact, rounded body with a "
        "thick oval cross-section. A small bridge section at the front. The majority of the "
        "hull is cargo space with loading hatches on the sides, each hatch framed by gold "
        "moulding. A light ion turret in a gilded housing on top. Layered armour plates across "
        "the hull. Engine bells recessed into the rear behind armoured cowlings. Crimson trim "
        "along the armour plate edges. Gold filigree around the loading hatches and engine "
        "cowlings. A gold emperor's crest on both sides. A crimson pennant trailing from the "
        "rear. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The hard-jump drive and cargo hold consume most of the interior. Crew spaces are "
        "minimal -- bunks, a tiny galley, and a bridge barely large enough for three "
        "stations. The cargo hold carries sealed containers of ammunition, food, spare "
        "parts, and the temperature-controlled cases of preservation compound that are "
        "the Dodo's most important cargo. A single shell assists with cargo handling. "
        "The ship has the spartan feel of something designed for a job, not for people."
    ),
    minimum_crew=[{"officers": 1}, {"crew": 4}, {"shells": 2}],
    secondary_crew=[{"cargo_handlers": 2}, {"shells": 1}],
    additional_systems=[
        "Hard-jump drive",
        "Sealed cargo system",
        "Preservation compound storage (temperature-controlled)",
    ],
)

AMMONITE = ShipTemplate(
    name="Ammonite",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CRUISER,
    ship_archetype="Field Support Ship",
    combat_role="Medical support / reanimation facility / field repair",
    length=485,
    armor=50,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.HIGH,
    max_hull_points=430,
    max_jump_strength=JumpStrength.MODERATE,
    max_supply_duration_days=63,
    default_weapons=[weapons.ION_CANNON, weapons.LASER_PD, weapons.LASER_PD],
    default_small_craft=[],
    short_description="Dedicated reanimation and medical ship -- the heart of Canopan attrition doctrine",
    long_description=(
        "The Ammonite is the keystone of Canopan attrition warfare. Where other factions' "
        "field support ships combine medical facilities with repair workshops, the Ammonite "
        "dedicates the majority of its interior to reanimation. It carries the largest "
        "reanimation facility outside of a dreadnought, capable of processing dozens of "
        "casualties per hour during sustained operations. Damaged ships across the task "
        "force send their dead to the Ammonite by shuttle; the Ammonite returns shells. "
        "The ship also carries conventional medical facilities for the living wounded and "
        "repair workshops for damaged vessels, but its defining purpose is the factory "
        "amidships that turns the fleet's dead into the fleet's workforce. A task force "
        "with an Ammonite attached fights fundamentally differently than one without -- "
        "the fleet's effective strength degrades slower, its damage control capability "
        "actually increases as the battle progresses, and the psychological burden of "
        "casualties is offset by the grim knowledge that the dead are still contributing. "
        "The Ammonite is not a ship the Canopan navy is proud of. It is a ship the "
        "Canopan navy cannot fight without."
    ),
    exterior_appearance_description=(
        "A 485-meter military spacecraft with a dark grey hull. A wide, rounded body with a "
        "thick oval cross-section. A prominent medical section amidships with large crimson "
        "and gold restoration symbols -- the Canopan variant of medical markings. Docking "
        "ports and transfer airlocks along both sides, framed by gold moulding. An ion cannon "
        "housing on the top, framed by gold moulding. Two point-defense mounts on the sides "
        "toward the rear. Layered armour plates across the hull. Engine bells recessed into "
        "the rear behind armoured cowlings. Crimson trim along every armour plate edge. Gold "
        "ornamentation -- emperor's crest on both sides, gilded borders around the medical "
        "section and docking ports. Crimson and gold banners trailing from the top spine. Ship "
        "name in gold lettering. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The reanimation facility occupies the central third of the ship -- a cold, "
        "brightly lit industrial space with rows of operating tables, chemical processing "
        "systems, tissue repair stations, and the preservation vats where bodies are "
        "stabilized before reanimation. The staff work with practiced efficiency, "
        "processing the dead with the detached professionalism of people who have made "
        "their peace with what they do. The medical section forward handles living "
        "casualties -- surgical bays, recovery wards, trauma care. The repair workshops "
        "aft carry equipment for patching battle-damaged ships. The shell staging area "
        "is between the reanimation facility and the shuttle bays -- freshly reanimated "
        "shells stand in rows, tagged for transfer to specific ships, waiting for the "
        "next shuttle. The living crew find ways to avoid walking through the staging "
        "area. The Ammonite's crew carry a weight that other factions' medical staff "
        "do not -- they know every shell that leaves their ship was a person an hour ago."
    ),
    minimum_crew=[{"officers": 25}, {"crew": 120}, {"shells": 80}],
    secondary_crew=[
        {"surgeons": 12},
        {"reanimation_specialists": 25},
        {"reanimation_technicians": 30},
        {"nurses": 35},
        {"repair_technicians": 25},
        {"shells": 55},
    ],
    additional_systems=[
        "Reanimation facility (industrial -- capacity 60+, fleet-scale processing)",
        "Preservation vat system",
        "Chemical processing plant",
        "Surgical bays",
        "Recovery wards (capacity 200)",
        "Ship repair workshop",
        "Casualty transfer shuttle bays (x2)",
        "Shell staging area",
        "Shell compartment (standing alcoves)",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

GLYPTODON = ShipTemplate(
    name="Glyptodon",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.CAPITAL,
    ship_archetype="Assault Transport",
    combat_role="Large-scale troop deployment into contested territory",
    length=720,
    armor=85,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.VERY_HIGH,
    max_hull_points=1300,
    max_jump_strength=JumpStrength.SOFT,
    max_supply_duration_days=63,
    default_weapons=[weapons.PARTICLE_CANNON, weapons.PLASMA_PD, weapons.PLASMA_PD, weapons.PLASMA_PD],
    default_small_craft=[],
    short_description="Heavily armored troop transport with reanimated labor force and shell combat reserve",
    long_description=(
        "The Glyptodon delivers a Canopan ground force into hostile space. It carries "
        "thousands of living troops plus heavy equipment -- vehicles, siege weapons, "
        "prefabricated fortifications -- supported by a large shell labor force that "
        "handles the physical work of deployment. The Glyptodon's reanimation bay serves "
        "a dual purpose: during the approach into contested space, it processes crew "
        "casualties from defensive actions, and after deployment, it operates as a "
        "ground-side reanimation facility, turning battlefield dead into shell labor for "
        "construction, fortification building, and non-combat ground operations. The "
        "Canopan ground doctrine mirrors the naval one: the living fight, the dead work. "
        "A Canopan invasion force digs in faster than anyone expects because its "
        "construction labor does not sleep, eat, or stop."
    ),
    exterior_appearance_description=(
        "A 720-meter military spacecraft with a dark grey hull. A massive, heavy rounded body "
        "with a thick oval cross-section and a blunt, armoured front. Layered armour plates in "
        "heavy overlapping rows across the hull. A particle cannon housing on the top, framed "
        "by gold moulding. The midsection is a massive troop bay with loading ramps on the "
        "underside and rear, the ramp frames bordered by gold filigree. Point-defense turrets "
        "spaced along the sides and top in gilded housings. Engine bells recessed into the "
        "rear behind heavily armoured cowlings. Crimson trim along every armour plate edge. "
        "Extensive gold ornamentation -- emperor's crest in raised relief on the front, gilded "
        "borders around every opening, laurel motifs along the sides. Multiple crimson and "
        "gold banners trailing from ornamental poles. Ship name in gold lettering on both "
        "sides. Dim amber lights set into the armour seams."
    ),
    interior_appearance_description=(
        "The troop decks are vast compartments with row after row of bunks for the "
        "living troops, interspersed with shell alcove sections where the reanimated "
        "labor force stands in the dark between work details. Vehicle bays on the lower "
        "decks carry armored transports and heavy weapons. The reanimation bay is sized "
        "for field operations -- designed to keep working after the ship has landed and "
        "become a ground installation. The deployment bays are built for rapid "
        "disembarkation: doors open, ramps extend, and the living troops advance while "
        "shell labor crews follow behind, already building fortifications before the "
        "shooting stops."
    ),
    minimum_crew=[{"officers": 18}, {"crew": 100}, {"shells": 250}],
    secondary_crew=[
        {"marine_officers": 55},
        {"marines": 4500},
        {"vehicle_crew": 220},
        {"reanimation_technicians": 10},
        {"medical": 30},
        {"ship_gunners": 20},
        {"shells": 390},
    ],
    additional_systems=[
        "Reanimation bay (field operations -- capacity 30, deployable ground-side)",
        "Shell compartment (standing alcoves, 400+)",
        "Vehicle deployment bays",
        "Heavy equipment storage",
        "Rapid disembarkation system",
        "Prefabricated fortification storage",
        "Reinforced hull structure",
        "Extended consumable storage",
    ],
)

YOWIE = ShipTemplate(
    name="Yowie",
    faction=ShipFaction.CANOPUS,
    size_class=ShipSize.FRIGATE,
    ship_archetype="Insertion Transport",
    combat_role="Special operations deployment behind enemy lines",
    length=148,
    armor=12,
    speed=Speed.SLOW,
    sensor_profile_level=SensorProfileLevel.LOW,
    max_hull_points=68,
    max_jump_strength=JumpStrength.HARD,
    max_supply_duration_days=35,
    default_weapons=[weapons.LIGHT_ION_TURRET],
    default_small_craft=[],
    short_description="Hard-jump insertion transport for special operations behind enemy lines",
    long_description=(
        "The Yowie is a small, heavy transport built around a hard-jump drive. It carries "
        "a company-sized element of Canopan special forces -- living soldiers, not shells, "
        "because special operations require judgment, adaptability, and initiative that "
        "the reanimated cannot provide. The Yowie gets its troops in through jump points "
        "nobody expects, deploys them, and either extracts them later or disappears. "
        "Slower than the template insertion transport, with a higher sensor profile -- "
        "Canopan engineers could not make the ship both tough and stealthy. The Yowie "
        "compensates with hull integrity: if detected, it survives long enough to "
        "complete deployment where a lighter ship would be destroyed on approach. A "
        "small reanimation facility allows the embarked force to recover casualties "
        "during extended operations behind enemy lines. Shell labor handles the ship's "
        "maintenance during long deployments."
    ),
    exterior_appearance_description=(
        "A 148-meter military spacecraft with a dark grey hull. A rounded, compact body with a "
        "thick oval cross-section. Layered armour plates across the hull. A light ion turret "
        "in a gilded housing on top. Loading ramps on the lower rear. Engine bells recessed "
        "into the rear behind armoured cowlings. Crimson trim along the armour plate edges. "
        "Gold filigree around the loading ramps and engine cowlings. A gold emperor's crest on "
        "both sides. A crimson pennant trailing from the top rear. Dim amber lights set into "
        "the armour seams."
    ),
    interior_appearance_description=(
        "The interior is split between the hard-jump drive, a small crew section, and "
        "the troop compartment. The troop compartment holds bunks and equipment storage "
        "for the embarked operators. No neural cradles, no simulations -- Canopan special "
        "forces prepare through briefings and physical rehearsal, not virtual reality. "
        "The crew section is minimal: a bridge, bunks, and a galley. A closet-sized "
        "reanimation bay sits adjacent to the troop compartment. Shell labor maintains "
        "the ship during transit. The ship has the tense, heavy feel of something built "
        "to go somewhere dangerous and come back."
    ),
    minimum_crew=[{"officers": 2}, {"crew": 6}, {"shells": 4}],
    secondary_crew=[
        {"special_forces": 44},
        {"special_forces_officers": 4},
        {"reanimation_technician": 1},
        {"shells": 3},
    ],
    additional_systems=[
        "Hard-jump drive",
        "Reanimation bay (minimal -- capacity 2)",
        "Shell compartment",
        "Troop compartment",
        "Extended consumable storage",
    ],
)


CANOPUS_SMALL_CRAFT = {
    "Auk": AUK,
    "Sabertooth": SABERTOOTH,
    "Raptor": RAPTOR,
    "Tarpan": TARPAN,
}

CANOPUS_CORVETTES = {
    "Aurochs": AUROCHS,
    "Moa": MOA,
}

CANOPUS_FRIGATES = {
    "Smilodon": SMILODON,
    "Thylacine": THYLACINE,
    "Bunyip": BUNYIP,
    "Amarok": AMAROK,
}

CANOPUS_DESTROYERS = {
    "Taniwha": TANIWHA,
    "Thunderbird": THUNDERBIRD,
    "Mosasaur": MOSASAUR,
}

CANOPUS_CRUISERS = {
    "Megalania": MEGALANIA,
    "Livyatan": LIVYATAN,
    "Mastodon": MASTODON,
}

CANOPUS_CAPITALS = {
    "Pterodactyl": PTERODACTYL,
    "Archelon": ARCHELON,
    "Mammoth": MAMMOTH,
}

CANOPUS_SUPPORT = {
    "Quagga": QUAGGA,
    "Dodo": DODO,
    "Ammonite": AMMONITE,
    "Glyptodon": GLYPTODON,
    "Yowie": YOWIE,
}

CANOPUS_ALL_SHIPS = {
    **CANOPUS_SMALL_CRAFT,
    **CANOPUS_CORVETTES,
    **CANOPUS_FRIGATES,
    **CANOPUS_DESTROYERS,
    **CANOPUS_CRUISERS,
    **CANOPUS_CAPITALS,
    **CANOPUS_SUPPORT,
}