"""The wrecks, as a subsystem in a file of their own: a `Wreck` dataclass, a reader for `wrecks.csv`, and
an `install_into(world)` that adds the ships to a world.

Because this is a module it has a `__file__`, so it finds its CSV with `pathlib.Path(__file__).parent` --
no working-directory guessing, in the build or the browser. That is the quiet reason loading belongs in a
module: a notebook has no `__file__`, but a module always does.
"""

import csv
import dataclasses
import pathlib

import iw

DATA = pathlib.Path(__file__).parent / "wrecks.csv"


@dataclasses.dataclass
class Wreck:
    """One ship, and everyone who went down with her -- one row of wrecks.csv, with a shape."""

    ship_name: str
    year: int
    type: str                # galleon, brig, trawler...  what she was
    souls: int               # how many were lost with her
    notable_crew: list[str]  # the people aboard worth naming
    brief: str               # one line for the always-on roster
    ship_story: str          # how she was lost, and what is still strange about it

    def keywords(self) -> list[str]:
        """Every word that should summon this wreck: her name, "the " + her name, and the year. Derived, so
        it is the same few lines for twelve ships or twelve thousand, and never a typo on the fifteenth."""
        words = {self.ship_name, f"the {self.ship_name}", str(self.year)}
        return sorted({word.strip().lower() for word in words if word.strip()})

    def lore_entry(self) -> iw.LoreBookEntry:
        """The KIB. Name the ship and the AI learns what she was, who was aboard, and what is still here."""
        article = "an" if self.type[:1].lower() in "aeiou" else "a"
        return iw.LoreBookEntry(
            name=f"Wreck: {self.ship_name} ({self.year})",
            keywords=self.keywords(),
            content=(
                f"The {self.ship_name}, {article} {self.type}, lost on the reef off Rona in {self.year}. "
                f"{self.souls} souls lost.\n"
                f"Of note aboard: {'; '.join(self.notable_crew)}.\n"
                f"{self.ship_story}"
            ),
        )


# The CSV, as objects, read once when the module is imported. Naming each column is most of the work; the
# rest is the two things a CSV cannot say on its own -- a number is a number (year, souls), and a list is a
# list (notable_crew, semicolons).
with DATA.open(newline="", encoding="utf-8") as handle:
    WRECKS = [
        Wreck(
            ship_name=row["ship_name"],
            year=int(row["year"]),
            type=row["type"],
            souls=int(row["souls"]),
            notable_crew=[name.strip() for name in row["notable_crew"].split(";") if name.strip()],
            brief=row["brief"],
            ship_story=row["ship_story"],
        )
        for row in csv.DictReader(handle)
    ]


def install_into(world: iw.World) -> None:
    """Add the wrecks *to* `world`: a keyword block per ship, plus the always-on roster that makes the AI
    know they exist and name them. The wrecks go into the world, not the world into the wrecks."""
    world.loreBookEntries.extend(wreck.lore_entry() for wreck in WRECKS)
    world.instructionBlocks.append(iw.InstructionBlock(
        name="The wrecks",
        content=(
            "The reef north of the light has been taking ships for centuries. Mention them in passing when "
            "it fits -- a name in the log, the graves under the cairn, a spar on the shore after a storm. "
            "The wrecks of note are:\n"
            + "\n".join(f"- {wreck.ship_name} ({wreck.year}): {wreck.brief}" for wreck in WRECKS)
        ),
    ))
