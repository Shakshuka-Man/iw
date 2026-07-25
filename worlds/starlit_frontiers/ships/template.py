import json
from dataclasses import dataclass, field

from ..enums import ShipFaction, ShipSize, Speed, SensorProfileLevel, JumpStrength
from ..weapons import Weapon


@dataclass
class ShipTemplate:
    name: str
    faction: ShipFaction
    size_class: ShipSize
    ship_archetype: str
    combat_role: str
    length: int
    armor: int
    speed: Speed
    sensor_profile_level: SensorProfileLevel
    max_hull_points: int
    max_jump_strength: JumpStrength
    max_supply_duration_days: int
    default_weapons: list[Weapon]
    default_small_craft: list[tuple[str, int]]
    short_description: str
    long_description: str
    exterior_appearance_description: str
    interior_appearance_description: str
    minimum_crew: list[dict[str, int]]
    secondary_crew: list[dict[str, int]]
    additional_systems: list[str] = field(default_factory=list)

    def to_info_json(self) -> str:
        """Everything the AI is told about this ship, as JSON.

        Serves both jobs the world has for it: it is the content of the ship's lore entry, and it is
        what the "Current ship info" tracked item holds while you are flying one."""
        return json.dumps({
            "name": self.name,
            "faction": self.faction.value,
            "size_class": self.size_class.name.replace("_", " ").title(),
            "ship_archetype": self.ship_archetype,
            "combat_role": self.combat_role,
            "length_m": self.length,
            "armor": self.armor,
            "speed": self.speed.name.replace("_", " ").title(),
            "sensor_profile": self.sensor_profile_level.name.replace("_", " ").title(),
            "max_hull_points": self.max_hull_points,
            "max_jump_strength": self.max_jump_strength.value,
            "max_supply_duration_days": self.max_supply_duration_days,
            "default_weapons": [
                {"name": w.name, "damage": w.damage, "range": w.range.name.replace("_", " ").title()}
                for w in self.default_weapons
            ],
            "default_small_craft": [
                {"type": name, "count": count}
                for name, count in self.default_small_craft
            ],
            "short_description": self.short_description,
            "long_description": self.long_description,
            "exterior_appearance": self.exterior_appearance_description,
            "interior_appearance": self.interior_appearance_description,
            "minimum_crew": self.minimum_crew,
            "secondary_crew": self.secondary_crew,
            "additional_systems": self.additional_systems,
        }, indent=2)
