"""The character sheet: everything the world tracks about the player's live state, in one place.

Every "volatile" tracked item lives here, each one beside the triggers that keep it current. The order the
*player* sees the items in is not the order they are defined -- it is fixed by `install_into` at the foot
of the file -- so the definitions here are free to group by what each one does.
"""


import itertools

import iw

from .enums import JumpDifficulty
from .weapons import ALL_WEAPONS
from .ships import ALL_SHIPS
from .systems import ALL_SYSTEMS
from .navigation import adjacent_jumps, info_json, paths_json


# ---- Basic details -------------------------------------------------------------------------------
#
# These are simple tracked items that get updated by simple instructions

MERIT_SCORE = iw.TrackedItem(
    name="MERIT score",
    dataType=iw.TrackedItemDataType.NUMBER,
    description="My MERIT score.",
    updateInstructions=(
        "Whenever MERIT observes me perform an action it approves of, increase this "
        "asymptotically towards 1000. Whenever MERIT observes me perform an action it "
        "disapproves of, decrease this asymptotically towards 0."
    ),
    initialValue="500",
    autoUpdate=True,
)

CREDITS = iw.TrackedItem(
    name="Credits",
    dataType=iw.TrackedItemDataType.NUMBER,
    description="How many credits I possess",
    updateInstructions=(
        "Update whenever I gain, earn, spend or lose money. Remember that millicredits "
        "(millicreds) count as one-thousandth of a credit."
    ),
    initialValue="75",
    autoUpdate=True,
)

CURRENT_SHIP_NAME = iw.TrackedItem(
    name="Current ship name",
    description="The name of my current spaceship.",
    updateInstructions="Update whenever I change spaceship, or whenever my current spaceship is renamed.",
    autoUpdate=True,
)

CURRENT_SHIP_MODEL = iw.TrackedItem(
    name="Current ship model",
    description="The name of the model of my current spaceship",
    updateInstructions="Update whenever I change spaceship",
    autoUpdate=True,
)


# ---- Current ship details ------------------------------------------------------------------------
#
# We also have tracked items of ship details that we don't trust the storyteller AI to maintain. Instead,
# we let the AI maintain the ship model and then use triggers to set these to exactly what we want them to be.

CURRENT_SHIP_INFO = iw.TrackedItem(
    name="Current ship info",
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    description="Detailed information about my current ship, in JSON format.",
)

CURRENT_SHIP_DESCRIPTION = iw.TrackedItem(
    name="Ship description",
    visibility=iw.TrackedItemVisibility.PLAYER_ONLY,
    description="A description of my current ship.",
)

MAXIMUM_HULL_INTEGRITY = iw.TrackedItem(
    name="Maximum hull integrity",
    dataType=iw.TrackedItemDataType.NUMBER,
    description="The maximum hitpoints of my current ship",
)

CURRENT_ARMOR = iw.TrackedItem(
    name="Current Ship Armor",
    dataType=iw.TrackedItemDataType.NUMBER,
    description="How much damage is reduced by whenever my ship is hit be a weapon",
)

CURRENT_SHIP_JUMP_STRENGTH = iw.TrackedItem(
    name="Current ship jump strength",
    autoUpdate=True,
)

# For each ship model, we set up a trigger that sets the ship details for that ship model. These will fire
# every turn that the player is in that model of ship. We use a dictionary with a key of ship name, so we
# can reuse this logic later on for character specific start of game triggers. Current hull integrity is
# deliberately not here, that is updated by the storyteller AI.
SET_SHIP_DETAIL_TRIGGERS: dict[str, iw.TriggerEvent] = {
    ship.name: iw.TriggerEvent(
        name=f"Set ship details - {ship.name}",
        triggerEffects=[
            iw.tools.set_tracked_item(CURRENT_SHIP_INFO, ship.to_info_json()),
            iw.tools.set_tracked_item(CURRENT_SHIP_DESCRIPTION, ship.long_description),
            iw.tools.set_tracked_item(MAXIMUM_HULL_INTEGRITY, str(ship.max_hull_points)),
            iw.tools.set_tracked_item(CURRENT_ARMOR, str(ship.armor)),
            iw.tools.set_tracked_item(CURRENT_SHIP_JUMP_STRENGTH, ship.max_jump_strength.value),
        ],
        triggerConditions=[
            iw.tools.tracked_item_is(CURRENT_SHIP_MODEL, ship.name),
        ],
        canTriggerMoreThanOnce=True,
    )
    for ship in ALL_SHIPS.values()
}

# ---- Hull Integrity ------------------------------------------------------------------------------
#
# Although this is updated by the AI, we put it in this section since it references maximum hull integrity
# and therefore needs to be defined after it.

CURRENT_HULL_INTEGRITY = iw.TrackedItem(
    name="Current hull integrity",
    dataType=iw.TrackedItemDataType.NUMBER,
    description="The hull integrity of my current ship. When it reaches zero, the ship will explode.",
    updateInstructions=(
        "Whenever my ship is repaired, increase this to a maximum of "
        f"{MAXIMUM_HULL_INTEGRITY.as_substitution()}.\n\n"
        f"Whenever I change ship, set this equal to {MAXIMUM_HULL_INTEGRITY.as_substitution()}."
        "Whenever my ship is hit by a weapon, decrease this according to "
        "the damage of the weapon. This damage is reduced by by armor "
        f"(which is {CURRENT_ARMOR.as_substitution()}), to a minimum of 1 damage. "
        "The damage that each weapon deals is:\n"
        + "\n".join(
            f"- {weapon.name}: {weapon.damage} damage"
            for weapon in sorted(ALL_WEAPONS, key=lambda weapon: (weapon.range.value, weapon.damage))
        )
    ),
    initialValue="0",
    autoUpdate=True,
)

# ---- System Info ---------------------------------------------------------------------------------
#
# We keep two tracked items related to the current system. One of them is simply the name of the current
# system, and it is used as key for later triggers. The other is the system info, a large json of details
# of the current system. This gets given to the AI directly, as it is a bit too cumbersome to be given
# to the player directly.
#
# A trigger updates the system info each turn, based on the current system -- defined below, after the jump
# slots it also refills on arrival. Since the current system is only ever set by triggers, its name is never
# malformed, so keying on it is reliable. That trigger installs after the jump triggers, so if a jump
# happens this turn the info reflects the system you land in.

CURRENT_SYSTEM = iw.TrackedItem(
    name="Current system",
    description="The name of the star system I am in",
)

CURRENT_SYSTEM_INFO = iw.TrackedItem(
    name="Current system info",
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    description="Information about my current star system, in JSON format",
)

# ---- Adjacent systems ----------------------------------------------------------------------------
#
# Each system has up to six adjacent systems that can be jumped to, and each of those has a jump difficulty.
# We set up tracked items for these six adjacent systems, to keep track of where the player can jump to.
# There will then be six transition triggers that cover the six different systems the player can jump to
# from their current system.

# Destination item, difficulty item and the jump trigger for each slot are built together, one slot at a
# time, so a slot is one thing in one place. The jump trigger reads the slot's own substitution token in
# both its condition and its effect: "when I jump to whatever this slot names, put that in Current system".
_ORDINALS = ["first", "second", "third", "fourth", "fifth", "sixth"]
ADJACENT_JUMP_DESTINATIONS: list[iw.TrackedItem] = []
ADJACENT_JUMP_DIFFICULTIES: list[iw.TrackedItem] = []
PERFORM_JUMP_TRIGGERS: list[iw.TriggerEvent] = []
for slot, ordinal in enumerate(_ORDINALS, start=1):
    destination = iw.TrackedItem(
        name=f"Adjacent jump destination {slot}",
        description=f"The destination of the {ordinal} jump point in this system",
    )
    difficulty = iw.TrackedItem(
        name=f"Adjacent jump difficulty {slot}",
        description=f"The difficulty of the {ordinal} jump point in this system",
    )
    ADJACENT_JUMP_DESTINATIONS.append(destination)
    ADJACENT_JUMP_DIFFICULTIES.append(difficulty)
    PERFORM_JUMP_TRIGGERS.append(iw.TriggerEvent(
        name=f"Perform adjacent jump {slot}",
        triggerEffects=[iw.tools.set_tracked_item(CURRENT_SYSTEM, destination.as_substitution())],
        triggerConditions=[
            iw.TriggerCondition(
                type=iw.ConditionType.ON_EVENT,
                category="condition",
                data=f"I travel through the jump point to {destination.as_substitution()}",
            ),
        ],
        canTriggerMoreThanOnce=True,
        advancedLogic=True,
    ))

_UNUSED_SLOT = (" ", "N/A")

# For each system, we have a trigger that sets the necessary tracked items detailing that system's info. This
# fires every turn, ensuring that all the details of system info are correct. We ensure this trigger is listed
# after the triggers about performing jumps, so we get the info of the new system. This is keyed off of the
# CURRENT_SYSTEM tracked item.
SET_SYSTEM_DETAIL_TRIGGERS: dict[str, iw.TriggerEvent] = {
    system.name: iw.TriggerEvent(
        name=f"System info - {system.name}",
        triggerConditions=[iw.tools.tracked_item_is(CURRENT_SYSTEM, system.name)],
        # We have six slots for adjacent jump destinations, but not all systems have six adjacent destinations,
        # so we fill out the remainder with dummy entries from _UNUSUED_SLOT so all the tracked items get
        # rewritten and we don't have stale data in the higher jump slots.
        triggerEffects=[
            iw.tools.set_tracked_item(CURRENT_SYSTEM_INFO, info_json(system)),
            *(
                iw.tools.set_tracked_item(slot_item, value)
                for destination, difficulty, (dest_name, diff_value) in zip(
                    ADJACENT_JUMP_DESTINATIONS,
                    ADJACENT_JUMP_DIFFICULTIES,
                    adjacent_jumps(system.name) + [_UNUSED_SLOT] * len(ADJACENT_JUMP_DESTINATIONS),
                )
                for slot_item, value in ((destination, dest_name), (difficulty, diff_value))
            ),
        ],
        canTriggerMoreThanOnce=True,
    )
    for system in ALL_SYSTEMS
}


# ---- Sector paths --------------------------------------------------------------------------------
#
# We use Sector paths to maintain a list of the route the player can take to reach any system in their
# current sector from their current location. As this depends on both their current system and the
# strength of the jump drive of their ship, we cannot include it in the system details triggers that
# are calculated above, we instead need a new set of triggers that depend on the combination of current
# system and current ship jump strength.

CURRENT_SECTOR_PATHS = iw.TrackedItem(
    name="Current sector paths",
    visibility=iw.TrackedItemVisibility.AI_ONLY,
    description="Paths to all reachable systems in the current cluster.",
)


_ARRIVAL_DIFFICULTIES = (JumpDifficulty.Soft, JumpDifficulty.Moderate, JumpDifficulty.Hard)

# What is reachable from a system, in a ship that can manage jumps this hard -- one per system per
# difficulty, because the answer depends on both. Keyed by (system name, difficulty) for the same reuse.
SET_SECTOR_PATH_TRIGGERS: dict[tuple[str, JumpDifficulty], iw.TriggerEvent] = {
    (system.name, difficulty): iw.TriggerEvent(
        name=f"Sector paths - {system.name} ({difficulty.value})",
        triggerEffects=[iw.tools.set_tracked_item(CURRENT_SECTOR_PATHS, paths_json(system, difficulty))],
        triggerConditions=[
            iw.tools.tracked_item_is(CURRENT_SYSTEM, system.name),
            iw.tools.tracked_item_is(CURRENT_SHIP_JUMP_STRENGTH, difficulty.value),
        ],
        canTriggerMoreThanOnce=True,
    )
    for system in ALL_SYSTEMS
    for difficulty in _ARRIVAL_DIFFICULTIES
}


# ---- The status line -----------------------------------------------------------------------------
# Each turn we provide an update to the player giving their current ship name and details. This also
# is useful to make sure the KIBs on the player's current ship fires each turn.

def status_trigger() -> iw.TriggerEvent:
    """Every turn: the ship's name, model and hull, along the top."""
    return iw.TriggerEvent(
        name="Status update",
        triggerEffects=[
            iw.TriggerEffect(
                type=iw.EffectType.SHOW_MESSAGE,
                data=(
                    f"{CURRENT_SHIP_NAME.as_substitution()} - {CURRENT_SHIP_MODEL.as_substitution()} - "
                    f"{CURRENT_HULL_INTEGRITY.as_substitution()}/"
                    f"{MAXIMUM_HULL_INTEGRITY.as_substitution()}"
                ),
            ),
        ],
        triggerConditions=[
            iw.TriggerCondition(type=iw.ConditionType.ON_TURN, category="condition", data=1),
        ],
        canTriggerMoreThanOnce=True,
    )


# ---- Assembly ------------------------------------------------------------------------------------
#
# `install_into` fixes the panel order the player sees the tracked items in -- the one order no single item
# can decide. The triggers it simply adds in the order they are declared above, which is also the order they
# must fire in when several match one turn: the ship-detail triggers, then the jump triggers, then each
# system's info and its sector-path tables (so a jump this turn shows up in the info you are then given),
# and last the status line.

def install_into(world: iw.World) -> None:
    """Add the whole character sheet: every live tracked item in the panel order the player sees them, then
    every trigger that maintains it, each block of triggers in the order it is declared above."""
    world.trackedItems.extend([
        MERIT_SCORE,
        CREDITS,
        CURRENT_SHIP_NAME,
        CURRENT_SHIP_MODEL,
        CURRENT_SHIP_INFO,
        CURRENT_SHIP_DESCRIPTION,
        CURRENT_HULL_INTEGRITY,
        MAXIMUM_HULL_INTEGRITY,
        CURRENT_ARMOR,
        CURRENT_SYSTEM,
        CURRENT_SYSTEM_INFO,
        CURRENT_SHIP_JUMP_STRENGTH,
        # The six slots on the panel, destination then difficulty for each in turn.
        *itertools.chain.from_iterable(zip(ADJACENT_JUMP_DESTINATIONS, ADJACENT_JUMP_DIFFICULTIES)),
        CURRENT_SECTOR_PATHS,
    ])
    world.triggerEvents.extend(SET_SHIP_DETAIL_TRIGGERS.values())
    world.triggerEvents.extend(PERFORM_JUMP_TRIGGERS)
    world.triggerEvents.extend(SET_SYSTEM_DETAIL_TRIGGERS.values())
    world.triggerEvents.extend(SET_SECTOR_PATH_TRIGGERS.values())
    world.triggerEvents.append(status_trigger())
