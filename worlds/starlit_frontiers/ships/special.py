from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from .. import weapons
from .template import ShipTemplate

CRYOSLEEPER = ShipTemplate(
    name="Cryosleeper",
    faction=ShipFaction.SPECIAL,
    size_class=ShipSize.SMALL,
    ship_archetype="Cryogenic Transport",
    combat_role="None -- pre-jump-drive relic with no weapons or defenses",
    length=15,
    armor=0,
    speed=Speed.VERY_SLOW,
    sensor_profile_level=SensorProfileLevel.INSIGNIFICANT,
    max_hull_points=3,
    max_jump_strength=JumpStrength.NONE,
    max_supply_duration_days=0,
    default_weapons=[],
    default_small_craft=[],
    short_description="A pre-jump-drive relic -- a coffin with an engine, built for a one-way trip that was never meant to end well",
    long_description=(
        "Cryosleepers were an experimental type of spacecraft first developed in the "
        "2600s. Humanity had developed the Inertial Resonator, allowing for travel "
        "within the solar system, but had not developed the jump drive yet. The "
        "Inertial Resonator could in theory be used to travel between star systems, "
        "but even the closest systems would take centuries of travel.\n\n"
        "The intention of a cryosleeper is that it would hold a single inhabitant. "
        "That inhabitant would be placed in suspended animation for centuries, being "
        "woken when they reached their destination system. Once at their destination "
        "system, they would use the nanoforge and terraforming tools within the "
        "spacecraft to begin the terraforming process at their destination. The "
        "inhabitant was expected to live out the rest of their life alone at the "
        "destination, making the planet habitable for a later wave of human "
        "colonization. Being placed in a cryosleeper was considered a terrible fate, "
        "equivalent to the death penalty.\n\n"
        "The development of the jump drive rendered cryosleepers redundant. Most "
        "cryosleepers never made it to their destination, and those that did found "
        "that they had been leapfrogged by later humans equipped with jump drives.\n\n"
        "Cryosleepers contain equipment that is considered thoroughly outdated by the "
        "standards of 3166. They do contain an Inertial Resonator, but they do not "
        "contain a jump drive, as they were developed before the invention of the "
        "jump drive. They do not contain communication arrays or transponders. A side "
        "effect of this is that they are extremely hard to detect by 3166 sensors."
    ),
    exterior_appearance_description=(
        "A 15-meter spacecraft with a battered, dark metal hull. A small, narrow cylinder "
        "with a rounded front and a single engine housing at the rear. The hull is pitted "
        "and scarred from centuries of micrometeorite impacts. The design is archaic -- no "
        "markings, no running lights, no transponder signal. No visible weapons. A single "
        "antenna stub. The metal is discoloured and corroded. To a modern observer, it "
        "looks like a piece of space debris that happens to have an engine."
    ),
    interior_appearance_description=(
        "A single cryogenic pod dominates the interior, surrounded by life support "
        "systems of antique design. A nanoforge and basic terraforming tools are "
        "stowed in sealed compartments -- equipment intended for a colonist who would "
        "never see home again. The control interface is primitive by 3166 standards, "
        "with physical switches and a screen-based display. There is no jump drive "
        "housing, no weapons systems, and no communications array. The air smells "
        "of recycled centuries."
    ),
    minimum_crew=[{"occupant": 1}],
    secondary_crew=[],
    additional_systems=[
        "Cryogenic suspension pod",
        "Nanoforge (pre-jump-drive model)",
        "Basic terraforming tools",
        "Inertial Resonator (no jump drive)",
        "No communications array",
        "No sensors that can detect other spacecraft",
        "No sensors that can detect other lifeforms",
        "No transponder",
        "No weapons",
    ],
)

SPECIAL_ALL_SHIPS = {
    "Cryosleeper": CRYOSLEEPER,
}