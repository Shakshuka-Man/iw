from enum import IntEnum, StrEnum


class StarClusters(StrEnum):
    INNER_SYSTEMS = "Inner Systems"
    ANTARES = "Antares"
    CANOPUS = "Canopus"
    HYADES = "Hyades"
    POLARIS = "Polaris"
    PLEIADES = "Pleiades"


class JumpDifficulty(StrEnum):
    """Difficulty of a jump link. Order: Soft < Moderate < Hard."""
    Soft = "Soft"
    Moderate = "Moderate"
    Hard = "Hard"

    @classmethod
    def from_str(cls, s: str) -> "JumpDifficulty":
        """Parse JSON/string value; 'Medium' maps to Moderate."""
        m = {"Soft": cls.Soft, "Medium": cls.Moderate, "Moderate": cls.Moderate, "Hard": cls.Hard}
        return m.get(s, cls.Soft)

class ShipFaction(StrEnum):
    CIVILIAN = "Civilian"
    SCN = "SCN"
    MERIT = "MERIT"
    INDEPENDENT = "Independent"
    PLEIADES = "Pleiades"
    HYADES = "Hyades"
    ANTARES = "Antares"
    CANOPUS = "Canopus"
    POLARIS = "Polaris"
    SPECIAL = "Special"


class Speed(IntEnum):
    VERY_SLOW = 1
    SLOW = 2
    MEDIUM = 3
    FAST = 4
    VERY_FAST = 6


class ShipSize(IntEnum):
    SMALL = 1
    CORVETTE = 2
    FRIGATE = 3
    BATTLESHIP = 4
    CRUISER = 5
    CAPITAL = 6


class JumpStrength(StrEnum):
    NONE = "None"
    SOFT = "Soft"
    MODERATE = "Moderate"
    HARD = "Hard"


class SensorProfileLevel(IntEnum):
    INSIGNIFICANT = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


class Distance(IntEnum):
    POINT_BLANK = 0
    SHORT = 1
    MEDIUM = 2
    LONG = 3
    EXTREME = 4