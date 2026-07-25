# Starlit Frontiers

A space-exploration world in the spirit of Freelancer, Escape Velocity and Starsector.

| | |
|---|---|
| playable characters | 7 |
| star systems | 126, across 6 clusters |
| ship models | 180 |
| instruction blocks | 17 |
| tracked items | 25 |
| lore book entries | 306 — one per ship, one per system |
| trigger events | 699 |
| source | ~42,000 lines |
| output | **5.0 MB** of world JSON |

## How it is put together

```
world.py            the assembly: a title, then one install call per subsystem. Start here
player_details.py   the character sheet: every live tracked item in panel order, and the triggers that maintain them
setting.py          the setting's background lore: money, MERIT, history, sensors, and how travel works
weapons.py          the catalogue of every gun -- pure data the ship models build from
ships/              the library of 180 models, one data file per faction
systems/            the map's data: 126 star systems and the jump links between them, a dumb data store
navigation.py       pure calculation over that map: pathfinding, and the JSON the AI is shown. No triggers, no iw
factions.py         the six powers, and the fleet each one flies
characters.py       the seven, the skills they carry, and how each one wakes up
metadata.py         the blurb, the image style, the permissions
enums.py            the shared words
generate_map.py     a standalone tool that draws the galaxy map. Not part of the build.
```