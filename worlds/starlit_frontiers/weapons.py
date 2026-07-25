"""Weapons: the catalogue every ship's loadout is built from.

Pure reference data -- one `Weapon` per model of gun, with its damage and range. Nothing here is a world
object: the ship models in `ships/` list their `default_weapons` from this file, and the character sheet's
"Current hull integrity" item builds its damage table by walking `ALL_WEAPONS`. A hit takes a weapon's
damage off the hull, minus armour, to a minimum of 1 -- but none of that arithmetic happens in Python; the
AI does it in prose, from that table, so a weapon cannot be rebalanced without the table (and the AI)
changing with it.
"""

from dataclasses import dataclass

from .enums import Distance


@dataclass
class Weapon:
    name: str
    damage: int
    range: Distance


LIGHT_LASER = Weapon(name="Light Laser", damage=6, range=Distance.SHORT)
LASER_TURRET = Weapon(name="Laser Turret", damage=10, range=Distance.SHORT)
HEAVY_LASER_TURRET = Weapon(name="Heavy Laser Turret", damage=13, range=Distance.SHORT)
HEAVY_LASER_ARRAY = Weapon(name="Heavy Laser Array", damage=15, range=Distance.SHORT)
LASER_PD = Weapon(name="Laser Point Defense", damage=10, range=Distance.POINT_BLANK)
PLASMA_PD = Weapon(name="Plasma Point Defense", damage=20, range=Distance.POINT_BLANK)
PLASMA_LAUNCHER = Weapon(name="Plasma Launcher", damage=20, range=Distance.SHORT)
PLASMA_CANNON = Weapon(name="Plasma Cannon", damage=33, range=Distance.SHORT)
REINFORCED_PLASMA_CANNON = Weapon(name="Reinforced Plasma Cannon", damage=38, range=Distance.SHORT)
HEAVY_PLASMA_CANNON = Weapon(name="Heavy Plasma Cannon", damage=45, range=Distance.SHORT)
LIGHT_ION_TURRET = Weapon(name="Light Ion Turret", damage=15, range=Distance.MEDIUM)
ION_TURRET = Weapon(name="Ion Turret", damage=20, range=Distance.MEDIUM)
ION_CANNON = Weapon(name="Ion Cannon", damage=25, range=Distance.MEDIUM)
PARTICLE_CANNON = Weapon(name="Particle Cannon", damage=33, range=Distance.MEDIUM)
HEAVY_PARTICLE_CANNON = Weapon(name="Heavy Particle Cannon", damage=45, range=Distance.MEDIUM)
PARTICLE_LANCE = Weapon(name="Particle Lance", damage=48, range=Distance.MEDIUM)
PARTICLE_CANNON_BATTERY = Weapon(name="Particle Cannon Battery", damage=55, range=Distance.MEDIUM)
LIGHT_RAILGUN = Weapon(name="Light Railgun", damage=42, range=Distance.LONG)
RAILGUN = Weapon(name="Railgun", damage=50, range=Distance.LONG)
HEAVY_RAILGUN = Weapon(name="Heavy Railgun", damage=70, range=Distance.LONG)
GAUSS_CANNON = Weapon(name="Gauss Cannon", damage=105, range=Distance.LONG)
PRECISION_RAILGUN = Weapon(name="Precision Railgun", damage=80, range=Distance.EXTREME)
SIEGE_CANNON = Weapon(name="Siege Cannon", damage=160, range=Distance.EXTREME)
ANTIMATTER_TORPEDO = Weapon(name="Antimatter Torpedo", damage=200, range=Distance.POINT_BLANK)

ALL_WEAPONS: list[Weapon] = [value for value in list(vars().values()) if isinstance(value, Weapon)]
