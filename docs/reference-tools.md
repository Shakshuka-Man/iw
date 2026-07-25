# `iw.tools` — helpers

*Generated from the source by `reference.py`. Do not edit -- edit the library and re-run.*

The convenience constructors for the two trigger payloads that are a trap to write by hand. **Nothing here is part of the world format** — that is what `iw` mirrors, one field for one field. These take a tracked item and build the redundant condition or effect the engine wants, writing the item's id once instead of the two places that must agree.

The basic tutorials build triggers from the raw `iw` objects; the advanced tutorials reach for these once writing them by hand stops scaling.

## The objects

## The functions

### `set_tracked_item(item: TrackedItem | str, value: str, action: TrackedItemAction = TrackedItemAction.SET) -> TriggerEffect`

An effect that writes a tracked item: set it, or add to / subtract from it.

### `tracked_item_is(item: TrackedItem | str, value: str, inequality: Inequality = Inequality.IS_EXACTLY) -> TriggerCondition`

A condition that reads a tracked item: fire while it is exactly / at least / at most `value`.
