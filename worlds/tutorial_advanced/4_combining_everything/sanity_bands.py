"""The sanity bands, as a subsystem in a file of its own: a `SanityBand` dataclass, a reader for
`sanity_bands.csv`, and an `install_into(world)` that hangs one trigger per band off the Sanity meter.

Unlike advanced tutorial 3, this module does NOT own the Sanity meter. `tracked_items.py` owns it (with
its full description and update rules); we import that exact object and wire the band triggers to it. That
is the one cross-module dependency in this tutorial -- see the note on the import below.

Same reason this is a module as `wrecks.py`: a module has a `__file__`, so it finds its CSV cleanly in
both the build and the browser.
"""

import csv
import dataclasses
import pathlib

import iw

# DEPENDENCY: the Sanity meter is defined once, in tracked_items.py. We import that exact object so our
# triggers reference the same tracked-item id the meter is registered under. tracked_items.install_into()
# is what actually adds SANITY to the world; we only add triggers that point at it. Because both modules
# share this one object, the order they install in does not matter -- the ids agree either way.
from tracked_items import SANITY

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
    """Add the sanity bands *to* `world`: the block the bands rewrite, and one trigger per band, all wired
    to the shared `SANITY` meter from `tracked_items.py` (which is what registers the meter itself)."""
    block = iw.InstructionBlock(name="The day and the night")
    world.instructionBlocks.append(block)

    world.triggerEvents.extend(band.trigger(SANITY, block) for band in BANDS)
