from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from typing import Optional

from ..enums import StarClusters, JumpDifficulty


@dataclass
class StellarObject:
    name: str
    desc: str = ""
    population: int = 0
    short_description: str = ""
    long_description: str = ""


@dataclass
class System:
    name: str
    star: str
    population: int
    stellar_objects: list[StellarObject]
    description: str = ""
    cluster: StarClusters = StarClusters.INNER_SYSTEMS
    short_description: str = ""
    long_description: str = ""
    distance_to_sol: float = 0.0
    stub: bool = False
    stub_parent: Optional[str] = None

    @property
    def system_is_populated(self) -> bool:
        return self.population > 10_000_000

    def to_lore_json(self) -> str:
        """This system as its lore-book entry, as JSON.

        Deliberately leaner than navigation's `info_json`: a lore entry is paid for every turn that
        happens to say this system's name, so it carries the short descriptions and no neighbours at all.
        The rich version -- with neighbours and gateway routes -- is for the one system you are actually
        standing in, and it lives with the graph in `navigation`."""
        return json.dumps({
            "name": self.name,
            "cluster": self.cluster.value,
            "population": self.population,
            "short_description": self.short_description or self.description,
            "stellar_objects": [
                {
                    "name": obj.name,
                    "population": obj.population,
                    "short_description": obj.short_description or obj.desc,
                }
                for obj in self.stellar_objects
            ],
        }, indent=2)


_jump_duration_rng = random.Random(123)


@dataclass
class JumpLink:
    """A link between two systems with a given jump difficulty.

    An edge of the map: inert data, the same kind of fact as a `System`. The pathfinding and everything
    else that *uses* these links is logic, and lives in `navigation`."""
    difficulty: JumpDifficulty
    system1: System
    system2: System
    duration_days: int = field(default_factory=lambda: _jump_duration_rng.randint(5, 8))
