"""Convenience constructors for the two trigger payloads that are a trap to write by hand.

`iw.iw` is a 1-1 reconstruction of the Infinite Worlds objects, and nothing more -- the engine has no
helpers, so neither does it. This module is where the conveniences live instead, kept out of the model on
purpose. The basic tutorials build triggers from the raw `iw` objects; the advanced tutorials reach for
this once doing it by hand stops scaling.

Reading and writing a tracked item are the two things triggers overwhelmingly do, and the engine's payload
for both is a trap: it carries the item's id *inside* `data`, next to the `trackedItemID` field that also
carries it. Write it by hand and you write the id twice, and nothing checks that the two agree. Get it
wrong and the world loads perfectly and the trigger silently never fires.

These take the item itself, so the id is written once, by us.
"""

from .iw import (
    ConditionType,
    EffectType,
    Inequality,
    TrackedItem,
    TrackedItemAction,
    TriggerCondition,
    TriggerEffect,
)


def _id_of(item: "TrackedItem | str") -> str:
    """An item, or a raw id -- `turn_number` and friends are engine built-ins with no TrackedItem."""
    return item if isinstance(item, str) else item.id


def set_tracked_item(
    item: "TrackedItem | str",
    value: str,
    action: TrackedItemAction = TrackedItemAction.SET,
) -> TriggerEffect:
    """An effect that writes a tracked item: set it, or add to / subtract from it."""
    item_id = _id_of(item)
    return TriggerEffect(
        type=EffectType.SET_TRACKED_ITEM_VALUE,
        trackedItemID=item_id,
        data={
            "action": action,
            "newValue": value,
            "replaceWith": "",
            "trackedItemID": item_id,
        },
    )


def tracked_item_is(
    item: "TrackedItem | str",
    value: str,
    inequality: Inequality = Inequality.IS_EXACTLY,
) -> TriggerCondition:
    """A condition that reads a tracked item: fire while it is exactly / at least / at most `value`.

    Two things match the engine's own export (schema 2.2). The inequality is written into `data` always,
    and *also* alongside it -- but only when it is not `IS_EXACTLY`, the default it does not write down.
    And `textComparison` is `"contains"`: the engine puts it on every tracked-item condition, text or
    number. Text items in fact have no exact match -- only `contains` / `does_not_contain` -- so a
    condition that omits `textComparison` is dropped on import."""
    item_id = _id_of(item)
    return TriggerCondition(
        type=ConditionType.ON_TRACKED_ITEM,
        category="condition",
        trackedItemID=item_id,
        inequality=None if inequality == Inequality.IS_EXACTLY else inequality,
        data={
            "inequality": inequality,
            "requiredValue": value,
            "trackedItemID": item_id,
            "textComparison": "contains",
        },
    )
