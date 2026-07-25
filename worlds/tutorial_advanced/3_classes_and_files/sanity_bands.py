"""The sanity meter, as a subsystem in a file of its own: a `SanityBand` dataclass, a reader for
`sanity_bands.csv`, and an `install_into(world)` that adds the whole meter to a world.

Same reason this is a module as `wrecks.py`: a module has a `__file__`, so it finds its CSV cleanly in
both the build and the browser.
"""

import csv
import dataclasses
import pathlib

import iw

DATA = pathlib.Path(__file__).parent / "sanity_bands.csv"


@dataclasses.dataclass
class SanityBand:
    """One tier of the sanity meter -- one row of sanity_bands.csv, with a shape."""

    low: int
    high: int
    day: str
    night: str

    def trigger(self, sanity: iw.TrackedItem, block: iw.InstructionBlock) -> iw.TriggerEvent:
        """The trigger basic tutorial 5 wrote out by hand: while the meter is inside this band, rewrite the
        block. canTriggerMoreThanOnce, or it fires once and freezes -- written here, right for every band."""
        return iw.TriggerEvent(
            name=f"Sanity {self.low}-{self.high}",
            canTriggerMoreThanOnce=True,
            triggerConditions=[
                iw.tools.tracked_item_is(sanity, str(self.low), iw.Inequality.AT_LEAST),
                iw.tools.tracked_item_is(sanity, str(self.high), iw.Inequality.AT_MOST),
            ],
            triggerEffects=[
                iw.TriggerEffect(
                    type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
                    data={"id": block.id, "content": f"Day: {self.day}\n\nNight: {self.night}"},
                ),
            ],
        )


# One SanityBand per row, read once when the module is imported.
with DATA.open(newline="", encoding="utf-8") as handle:
    BANDS = [
        SanityBand(low=int(row["low"]), high=int(row["high"]), day=row["day"], night=row["night"])
        for row in csv.DictReader(handle)
    ]


def install_into(world: iw.World) -> None:
    """Add the sanity meter *to* `world`: the tracked item, the block the bands rewrite, and one trigger per
    band. The meter goes into the world, not the world into the meter."""
    sanity = iw.TrackedItem(
        name="Sanity",
        dataType=iw.TrackedItemDataType.NUMBER,
        visibility=iw.TrackedItemVisibility.AI_ONLY,
        initialValue="100",
        autoUpdate=True,
    )
    world.trackedItems.append(sanity)

    block = iw.InstructionBlock(name="The day and the night")
    world.instructionBlocks.append(block)

    world.triggerEvents.extend(band.trigger(sanity, block) for band in BANDS)
