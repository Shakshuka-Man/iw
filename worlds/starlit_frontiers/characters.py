"""The seven, and how each of them begins.

`iw.PossibleCharacter` is only half of a character -- the name, the description, the portrait you pick
from. Where you wake up, in what ship, with how many credits and what you remember is not a property of
the character at all: it is what that character's **start-of-game trigger** writes into the world before
the first word is generated. So a def carries both halves, and this file carries the triggers.

That is why `metadata.py` leaves `background`, `firstInput` and `objective` as placeholders reading THIS
IS SET BY TRIGGERS. Nobody ever reads them. Each character overwrites all three, plus their ship, their
money, their MERIT score and the six jump points out of wherever they woke up -- which is why this file
imports nearly every other subsystem. Starting a game *is* touching everything at once.

One of them wakes from cryosleep five hundred years late, and the world has to be careful what it tells
him; that is the `CHARACTER_SPECIFIC` block below, and the first-turn trigger at the bottom.
"""

from dataclasses import dataclass, field
from typing import Optional

import iw

from . import player_details
from .ships.template import ShipTemplate
from .systems import System

# The world's skill roster. Every character below carries a level in each of these, and the engine grades
# the player on them.
SKILLS = ["Piloting", "Engineering", "Command", "Diplomacy", "Computers"]


@dataclass
class PlayableCharacterDef:
    first_name: str
    last_name: str
    one_liner: str
    description: str
    appearance: str

    # Narrative fields for start-of-game trigger
    background: str
    first_action: str
    ai_guidance: str
    objective: str
    instruction_block_content: Optional[str] = None

    # Starting state
    starting_merit_score: int = 500
    starting_credits: int = 0
    starting_ship_name: str = ""
    starting_ship: ShipTemplate = None
    starting_system: System = None

    # Portrait
    portrait_url: str = ""
    full_size_portrait_url: str = ""
    portrait_options: list[str] = field(default_factory=list)
    full_size_portrait_options: list[str] = field(default_factory=list)
    current_portrait_index: int = 0
    portrait_prompt_details: dict[str, str] = field(default_factory=dict)

    # Skills
    skills: dict[str, int] = field(default_factory=dict)

    # The character as the world sees it. Built here, so there is exactly one of it, and so its id is
    # the id -- the start-of-game trigger reads `pc.character.characterId` rather than quoting a literal.
    character: iw.PossibleCharacter = field(init=False)

    def __post_init__(self) -> None:
        self.character = iw.PossibleCharacter(
            name=f"{self.first_name} {self.last_name}".strip(),
            description=self.description,
            portrait=self.portrait_url,
            fullSizePortrait=self.full_size_portrait_url,
            portraitOptions=list(self.portrait_options),
            fullSizePortraitOptions=list(self.full_size_portrait_options),
            currentPortraitIndex=self.current_portrait_index,
            portraitPromptDetails=iw.PortraitPromptDetails(**self.portrait_prompt_details),
            skills=dict(self.skills),
        )


# The cast, built once at import -- the same reason the tracked items are. Every start-of-game trigger is
# gated on a character's id, and those ids come from the `iw.PossibleCharacter` each def built for itself.
# A second cast would be a second set of ids that the world has never heard of.
from .systems.inner_systems import GENUBI, SOL
from .systems.hyades import SCHEAT
from .systems.canopus import PLACIDUS
from .systems.polaris import POLARIS
from .systems.antares import ANTARES
from .systems.pleiades import ASTEROPE
from .ships.special import CRYOSLEEPER
from .ships.merit import MERIT_ALL_SHIPS
from .ships.independent import INDEPENDENT_ALL_SHIPS
from .ships.polaris import POLARIS_ALL_SHIPS
from .ships.pleiades import PLEIADES_ALL_SHIPS
from .ships.antares import ANTARES_ALL_SHIPS


jeremy = PlayableCharacterDef(
    first_name="Trent",
    last_name="Edison",
    one_liner="A former MERIT auditor who fled Earth in a cryosleeper and woke in 3166.",
    description=(
        "Originally a taxation auditor in the year 2638, Trent used his administrator "
        "privileges to steal thousands of credits from the European Federation. When he "
        "was discovered, he ran, stealing a starship to evade the authorities. "
        "Unfortunately, the starship he stole was a cryosleeper, and he was forcibly "
        "placed in stasis. Over five centuries later, he has finally reached his "
        "destination."
    ),
    appearance="A dishevelled-looking man with short, dark hair and stubble",
    background=(
        "In the year 2638, you were a systems auditor working for the European Federation. You were "
        "part of the team developing MERIT, a system for auditing taxation. Using your administrator "
        "access to MERIT, you were able to embezzle a large amount of money, thousands of credits.\n\n"
        "Unfortunately, you did not cover your tracks fully, and your crimes were discovered. You "
        "ran from arrest, stealing a spacecraft with the intention of escaping to the Jovian moons "
        "where you could hide.\n\n"
        "It was only after you had left Earth that you realized that the spacecraft you stole was a cryosleeper. "
        "Locked out of control of the vessel, you were forcibly placed in cryosleep until you reached your destination.\n\n"
        "As your consciousness faded, you knew that you were doomed to a fate worse than death."
    ),
    ai_guidance=(
        "The computer wakes me from cryosleep, telling me that I am in orbit around the planet Selvane, though I do not know what that means. My body is still stiff and unresponsive, and my "
        "memory is fuzzy as I recover from the side effects of cryosleep.\n\nI piece together the "
        "last things I remember:\n"
        "- My life on Earth in 2638, embezzling money from a taxation audit system named MERIT\n"
        "- Being sloppy and getting caught\n"
        "- Stealing a spacecraft to avoid getting caught by the European Federation police\n"
        "- The horror as I realize that the spacecraft I have stolen is a cryosleeper, and I have "
        "consigned myself to a fate worse than death\n\nI was frozen in the year 2638, which means "
        "that I do not know about anything that happened since then. Notably:\n"
        "- I do not know that humanity has developed the Jump Drive and spread to other solar systems\n"
        "- I do not know about the existence of the Stellar Concordium\n"
        "- I do not know that MERIT has expanded in scope\n\n"
        "My cryosleeper does not pick up any spacecraft in space, or detect any of the human settlements in the system. "
        "As far as my sensors can tell, I am the only living thing in the system.\n\n"
        "It is a fundamental and inviolable rule that I believe that I am the only sentient being in the system. "
    ),
    first_action="I slowly wake from cryosleep. The process is difficult.",
    objective="Find purpose in the galaxy and make a new life for myself.",
    instruction_block_content=(
        "As I was a systems auditor in the early days of MERIT, I had administrator access. These "
        "administrator privileges were never revoked, meaning that I still have administrator access "
        "to MERIT and can control it to a degree. I am the only person in the galaxy who has such "
        "access.\n\nNotably this means that I can control my MERIT score completely, as well as that "
        "of anybody I wish.\n\nRemember that I was frozen in the year 2638. Until I learn about it, "
        "I do not know about anything that has happened since then. Notably:\n"
        "- I do not know that humanity has developed the Jump Drive and spread to other solar systems\n"
        "- I do not know about the existence of the Stellar Concordium\n"
        "- I do not know that MERIT has expanded in scope\n\n"
        "I can learn about these things, but I do not initially know them.\n\n"
        "I want to avoid the people I interact with knowing my history and past. I want to keep my "
        "status as a cryosleeper secret, as I know that the attention can only end badly for me. If "
        "anybody knows about my history with MERIT, they are a potential threat to me, and so I need "
        "to keep it a secret.\n\nMy adventure will be a careful balance of trying to figure out how "
        "to use my unique privileges and status within MERIT with trying to keep my identity and the "
        "source of my abilities quiet.\n\n"
        "I am 32 years old, just over 6 feet tall, with short dark brown hair, brown eyes, light skin, "
        "and a well-kept goatee."
    ),
    starting_merit_score=500,
    starting_credits=7500,
    starting_ship_name="Icarus",
    starting_ship=CRYOSLEEPER,
    starting_system=GENUBI,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/vM6bdN4qiO.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/VS3uF1QWXL.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/xrk1ha5cGX.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/vM6bdN4qiO.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/aZNbqcYHPD.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/VS3uF1QWXL.jpg",
    ],
    current_portrait_index=1,
    portrait_prompt_details={
        "illustrClothes": "Jumpsuit",
        "illustrSetting": "Spaceship interior of an ancient spaceship, visibly old and worn out",
        "illustrAppearance": "A dishevelled-looking man with short, dark hair and stubble",
        "illustrExpressionPosition": "Cryogenically frozen, unconscious, inside a cryopod, unhappy",
    },
    skills={"Command": 3, "Piloting": 4, "Computers": 5, "Diplomacy": 4, "Engineering": 3},
)

olivia = PlayableCharacterDef(
    first_name="Junko",
    last_name="Zane",
    one_liner="A senior officer in the SVN navy under MERIT, on an intelligence-gathering mission.",
    description=(
        "At the age of three, Junko was identified by MERIT as a high-potential individual with "
        "strong potential in diplomacy, subterfuge and command. She was fast-tracked into the "
        "Stellar Concordium Navy and has since proved MERIT's predictions to be correct multiple "
        "times over. She is responsible for some of the most sensitive and important missions of "
        "MERIT's intelligence division."
    ),
    appearance="A female scientist in her forties with long brown hair",
    background=(
        "At the age of three, MERIT identified you as a high-potential individual. You were reassigned from "
        "your original family to the accelerated learning program at the MERIT Academy. You were one of the "
        "top students in your class, and you were fast-tracked to a career in command. You have since had a "
        "long and successful career in the Stellar Concordium Navy, under the command of MERIT.\n\n"
        "You are classified as a high-trust officer in the SCN, assigned to the missions that MERIT considers most important.\n\n"
        "After three years commanding a light cruiser on the Polaran border, you were recalled to Sol for your next assignment.\n\n"
        "Your latest mission is aboard the SCN Mimir, a highly advanced scout frigate. Your job is to investigate the CNP-0871 system, deep in Canopan space. "
        "Little is known about the system, but MERIT has reason to believe that there is something of interest there, something "
        "that may give MERIT control over the Canopan emperor himself.\n\n"
        "This is a dangerous mission, and you will have to use stealth and diplomacy to complete it."
    ),
    first_action="I meet my crew as we all board the ship on Earth.",
    ai_guidance=(
        "I am first to arrive at the SCN Mimir. I admire the ship and its advanced technology, and "
        "one by one the crew arrive. They are all some of the brightest minds in the Stellar "
        "Concordium Navy. Once we have made our introductions, we leave the surface of Earth and head "
        "into orbit. I marvel briefly at the sight of earth, the moon, and the swarm "
        "of ships in orbit - it is a planet of sixty billion people, birthplace of humanity, "
        "and the peak of human achievement and accomplishment."
    ),
    instruction_block_content=(
        "I am a high-ranking officer in the SCN, under the command of MERIT. "
        "I am on missions of stealth and diplomacy. I know when to invoke my rank within MERIT, and "
        "when to keep my allegiance and background secret. "
        "I am highly skilled in diplomacy and subterfuge, having been trained in the art of deception and manipulation "
        "since I was an infant.\n\n"
        "I am 27 years old, 5 feet 4 inches tall, with light skin, waist-length light "
        "brown hair and piercing blue eyes."
    ),
    objective="Travel the Galaxy and find its secrets.",
    starting_merit_score=836,
    starting_credits=35000,
    starting_ship_name="SCN Mimir",
    starting_ship=MERIT_ALL_SHIPS["Argus"],
    starting_system=SOL,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/g6IXMQOScD.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/IalfYm2vFQ.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/g6IXMQOScD.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/IalfYm2vFQ.jpg",
    ],
    current_portrait_index=0,
    portrait_prompt_details={
        "illustrClothes": "A sharply pressed dark blue military uniform (jacket and skirt) with medals and military insignia",
        "illustrSetting": "Command seat of a bridge on a starship",
        "illustrAppearance": "A female scientist in her forties with long brown hair",
        "illustrExpressionPosition": "Seated in a captain's chair, concentrating",
    },
    skills={"Command": 5, "Piloting": 3, "Computers": 4, "Diplomacy": 5, "Engineering": 2},
)

marco = PlayableCharacterDef(
    first_name="Marco",
    last_name="Carlino",
    one_liner="A scrapper from Scheat who stole his own ship to escape debt.",
    description=(
        "Marco is Scheat born and bred. He started working in the scrapyards on Carriston "
        "from the age of fifteen - when there's no food on the table, idle hands are a luxury "
        "that can't be afforded. Forced to buy industrial prosthetics, he found himself in debt "
        "that he would never be able to pay off. With no life left for him in Scheat, he used "
        "his position at the scrapyards to steal ship pieces, eventually able to construct his "
        "own vessel and leave his past behind."
    ),
    appearance="A muscular laborer with tanned skin, robotic left arm",
    background=(
        "You are a scrapper from Scheat. You started working in the scrapyards on Carriston "
        "from the age of fifteen - poverty did not leave you with much choice. You were forced "
        "to buy industrial prosthetics, robotic arms that allowed you to tear apart ships with your bare hands.\n\n"
        "These prosthetics were not cheap, and you were forced to work long hours in the scrapyards to pay for them. "
        "No matter how hard you worked, your debts only grew, and you knew that you would never be able to pay them off.\n\n"
        "Being unable to afford passage on a passenger ship, you took a different approach. Bit by bit, over the course of several years, you stole parts from ships that were being scrapped. "
        "Eventually, you had enough parts to construct your own vessel, and leave your past behind."
    ),
    first_action="Finish my shift at the scrapyards and head to my under-construction ship.",
    ai_guidance=(
        "The turn begins as I am finishing my shift at the scrapyards. I am carefully removing the jump drive from a scrapped Mule-class freighter. "
        "I am careful to do this when nobody is watching. I have been stealing parts for a while now, but the jump drive is the most "
        "valuable part I have stolen by far, and I know once I take it I will not have long before its absence is noticed. "
        "With the jump drive in hand, I quickly head to my under-construction ship and install it. I reflect on how I "
        "have spent the last few years of my life, stealing parts from ships and building my own vessel. I know that I will not have long before my past catches up to me, but I am determined to make the most of my new life. "
        "With the jump drive installed, my ship is now operational. I take a moment to admire my handiwork, and then head out into space to find my fortune."
    ),
    objective="Find your fortune in the galaxy and leave your past behind.",
    instruction_block_content=(
        "I am an extremely skilled scrapper and engineer. I have robotic prosthetic hands and arms that allow me "
        "to tear apart ships with my bare hands. These prosthetics require maintenance, and I will have to spend "
        "time and credits to keep them in working order. These prosthetics are illegal in MERIT space, and if I "
        "go to MERIT space with them, I will need to be careful not to be caught.\n\n"
        "I am 30 years old, 5 feet 9 inches tall, extremely muscular, with tanned skin, "
        "shoulder-length dark brown hair and no beard."
    ),
    starting_merit_score=294,
    starting_credits=880,
    starting_ship_name="Revenant",
    starting_ship=INDEPENDENT_ALL_SHIPS["Mule"],
    starting_system=SCHEAT,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/MD6DPuYzy4.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/RYK3bZBEec.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/CnqIlBGLdZ.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/Z1y0wNnUuP.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/EUwcw5CsWD.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/Httq00rgH4.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/w4AfSowKGj.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/cNwQzla6os.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/MD6DPuYzy4.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/1WTipxMMpZ.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/QsXHwUU5cW.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/n31xRmyuSW.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/Rt4FRR2HXl.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/DKzy3oiQQb.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/s39wwXmFJS.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/RYK3bZBEec.jpg",
    ],
    current_portrait_index=6,
    portrait_prompt_details={
        "illustrClothes": "single-sleeved Work suit",
        "illustrSetting": "Crowded, dusty Scrapyard",
        "illustrAppearance": "A muscular laborer with tanned skin, robotic left arm ",
        "illustrExpressionPosition": "Concentrating while disassembling a huge spacecraft",
    },
    skills={"Command": 2, "Piloting": 4, "Computers": 4, "Diplomacy": 3, "Engineering": 5},
)

mina = PlayableCharacterDef(
    first_name="Mina",
    last_name="Kattan",
    one_liner="A medical professional who stole a dead woman's identity and fortune.",
    description=(
        "Mina Kattan was one of the medical personnel working on Verantis, in the Placidus "
        "system. Highly skilled, she performed restorations on some of the most important "
        "figures in the sector. However, when the restoration process failed on one of her "
        "clients, she stole her identity and made off with her fortune."
    ),
    appearance="A 31 year old dark-skinned woman",
    background="Your family was originally a vassal to one of the planetary Kings of the Canopus sector. You were "
    "trained to be part of the royal family's medical staff, providing reanimation services if they were to ever die.\n\n"
    "When that branch of the family was overthrown, you were left without a home, and were forced to offer your services to the highest bidder. "
    "Taking on several wealthy clients, you were able to make good money, but your position was precarious - anyone from outside of "
    "the Canopus sector who could afford your services could also afford to hire a killer to silence you and keep their reanimation secret.",
    first_action="I am performing a reanimation on a client, a wealthy figure from out of sector.",
    ai_guidance="The turn begins as I am performing reanimation on a wealthy figure from out of sector, Mina Kattan. They have recently died, and I am restoring them to life. "
    "Their cryogenically preserved body is on the operating table, and I am systematically restoring their vital organs one by one. "
    "They have paid for premium services, and they will be restored to life as if they had never died."
    "I am always worried with clients from out of sector. Many of them want to keep reanimation secret, and will have no problem killing me to keep it that way."
    "As I am working and the client's body is on the operating table, I hear a chirp from their comms pad. Looking at it, I see that my worst fears have been realized - the client has "
    "hired a killer to kill me as soon as the restoration is complete so they can keep their reanimation secret. "
    "Knowing that I will not have long to live, I am fortunate that the client bears some physical resemblance to me.\n\n"
    "I quickly change plans, dismembering the client's body and disposing it down the nearest disposal chute. "
    "I then take the client's personal effects and adopt their identity. I change my name to Mina Kattan, and I am now a wealthy woman from out of sector. "
    "I head to the client's ship and take it over. In the short term I will be able to explain any suspicious behaviour as being due to the shock of the restoration process. "
    "However, I know that in the long term this will likely cause problems.",
    objective="Find a new life in the galaxy and leave your past behind.",
    instruction_block_content=("I am a highly skilled medical professional. I have performed reanimations on "
        "several wealthy clients from out of sector. I have claimed the identity of one of my clients - Mina Kattan - "
        "and I now have access to her fortune and her assets. I will need to be careful to not be found out.\n\n"
        "I am 31 years old, 5 feet 8 inches tall, slender, with dark skin and short black hair."
    ),
    starting_merit_score=427,
    starting_credits=3500000,
    starting_ship_name="Corona",
    starting_ship=INDEPENDENT_ALL_SHIPS["Stallion"],
    starting_system=PLACIDUS,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/vFd9WllbiY.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/tSHmK1Wisq.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/vFd9WllbiY.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/tSHmK1Wisq.jpg",
    ],
    current_portrait_index=0,
    portrait_prompt_details={
        "illustrClothes": "Lab coat",
        "illustrSetting": "Operating theatre",
        "illustrAppearance": "A 31 year old dark-skinned woman",
        "illustrExpressionPosition": "Performing surgery",
    },
    skills={"Command": 4, "Piloting": 3, "Computers": 4, "Diplomacy": 4, "Engineering": 3},
)

meilir = PlayableCharacterDef(
    first_name="Meilir",
    last_name="Stant",
    one_liner="A senior engineer on a Polaran carrier who knows where the real power lies.",
    description=(
        "Meilir Stant is a senior engineer on the PLR Llyrell, an Orrery-class carrier and "
        "pride of the Polaran fleet. The ship has been in service for over fifty years, and "
        "Meilir has been a critical part of the crew for over half of those. As the one "
        "responsible for maintaining the cores of the ship, none but him know how much power "
        "aboard the ship he really holds."
    ),
    appearance="An emaciated looking man with neural ports and visible computer interfaces on his face",
    background=(
        "You are a senior engineer aboard the PLR Llyrell, an Orrery-class carrier and one of the "
        "most powerful warships in the Polaran fleet. You have served on the Llyrell for twenty-six "
        "years. You are one of a handful of people who enters the neural cradles -- the sealed chambers "
        "where the ship's Cores live. You check the neural connections, monitor the biological "
        "functions, and maintain the systems that keep a human brain alive inside a warship. You are "
        "the closest thing the Cores have to a doctor, a confidant, and a friend.\n\n"
        "The lead Core of the Llyrell is Commander Adrane Voss. She was fused to the ship eight years "
        "before you joined the crew. She is arrogant and self-centred, believing you to be insignificant "
        "and unworthy of her time. She has not even bothered to know your name.\n\n"
        "However, you have turned the tables. As senior engineer, you are responsible for the integration "
        "systems between the cores and the rest of the ship's systems. You control what the cores see and hear. "
        "The cores may control the ship, but you control the cores, and none but you know it."
    ),
    first_action="I perform some last minute checks on the ship's systems.",
    ai_guidance=(
        "The turn begins as I am overseeing tasks that I have assigned to the other engineers on the ship. "
        "I am the most senior engineer on the ship, and ensuring its smooth and efficient operation is my responsibility. "
        "Once the other engineers are busy, I enter the neural cradles. I am the only one on the ship with access to the neural cradles, and I ensure none follow me in. "
        "I install a device that I have been working on for some time - an artificial core. This is a device that simulates a "
        "core's neural connections, but instead of being a human brain, it is a computer that I have assembled and programmed. "
        "I ensure that it is functioning correctly, and test its operations. These tests are successful. "
        "With my artificial core installed and functioning, I reflect on what it means and what to do next - this ability to "
        "use an artificial core that I have complete control over makes me the most powerful person on the ship, potentially the whole Polaran fleet."
    ),
    objective="Use your control over the cores to elevate your status and power.",
    instruction_block_content=(
        "I am a Polaran with computer ports integrated into my neural system. This allows me to interface with computers "
        "and other devices directly using my brain. This allows for more refined control over any of these systems. "
        "I also have developed artificial cores, devices that simulate a human brain and mimic the functionality of a core installed into a Polaran ship. "
        "I have complete control over these artificial cores, and none but me know it. "
        "This means that any ship I have installed an artificial core into is effectively under my control.\n\n"
        "I am 45 years old, 6 feet 3 inches tall, and skinny. I have visible neural ports "
        "over my body, allowing me to integrate my nervous system with computers."
    ),
    starting_merit_score=439,
    starting_credits=25000,
    starting_ship_name="PLR Llyrell",
    starting_ship=POLARIS_ALL_SHIPS["Orrery"],
    starting_system=POLARIS,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/2TWUq74Bfa.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/2eGHY54P24.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/L8m4GctiDx.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/f9Y9ApWsmv.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/BSA9pSW7IX.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/AzbUdrCIHh.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/8VWeoA8FXm.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/oyUDzGtWPJ.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/2TWUq74Bfa.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/zhtouxSbwi.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/xvbVqVzPEY.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/PT5vvRsmGg.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/gpOkWBV3Pn.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/20KHGfj03Z.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/2QC3e6jJVm.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/2eGHY54P24.jpg",
    ],
    current_portrait_index=6,
    portrait_prompt_details={
        "illustrClothes": "Dark green and brown military uniform",
        "illustrSetting": "Insides of a futuristic capital spaceship",
        "illustrAppearance": "An emaciated looking man with neural ports and visible computer interfaces on his face",
        "illustrExpressionPosition": "Frowning",
    },
    skills={"Command": 5, "Piloting": 2, "Computers": 4, "Diplomacy": 2, "Engineering": 5},
)

gulzat = PlayableCharacterDef(
    first_name="Gulzat",
    last_name="Muratov",
    one_liner="A pharmaceutical executive who controls the military from the shadows.",
    description=(
        "Although nominally a civilian "
        "liaison within the Antarean military, Gulzat Muratov is an executive for Korvane industries, "
        "and as a result she holds higher rank than any military officer. The military is in "
        "the back pocket of the pharmaceutical industry, and it is her job to keep things "
        "that way - using the military to protect her interests and the interests of her company."
    ),
    appearance="An albino woman",
    background="You are a senior executive in Korvane Industries, a pharmaceutical company from the Antares cluster. "
        "You have earned this position through a combination of your connections, your competence, and your "
        "ruthlessness. Getting ahead in this industry requires backstabbing in a very literal sense, and you have "
        "stepped over a lot of bodies to get where you are.\n\n"
        "Officially, the military has given you the title of Civilian Liason, Third Fleet, but in practice your role "
        "holds far more authority. The Third Fleet is effecitvely the enforcement arm of Korvane Industries, and you "
        "command the soldiers to enforce the interests of Korvane Industries and you.",
    first_action="I call the captain of the ship to my quarters to give him his instructions",
    ai_guidance="The turn begins in my quarters aboard the Herald, a Cyclone-class battleship. My quarters are expansive "
        "and luxurious, far beyond what would be expected on a military ship, and beyond anyone else on the ship, even those "
        "of the captain. I call the captain to my quarters, preparing to give him instructions. "
        "A Korvane Industries freighter was recently attacked and its cargo stolen, and my intelligence indicates that "
        "the responsible party is one of the rival drug corporations, Clarion Biosciences. "
        "This freighter was carrying a very valuable cargo - the prototype of a new stimulant drug that Korvane Industries has developed. "
        "This is not something that I can let go without responding in kind. The reports say that the freighter was attacked by ships "
        "that bear the markings of the Fifth Fleet, and that the Fifth Fleet is known to be aligned with Clarion Biosciences. "
        "I need to respond in kind, and I need to do it quickly.",
    objective="Establish your control over the military and use it to protect your interests.",
    instruction_block_content=(
        "I am a senior executive in Korvane industries, and the liason between Korvane "
        "Industries and the Antarean military. I have authority over the third fleet of "
        "the Antarean military, but I do not hold any authority over other branches.\n\n"
        "As with most in the Antares, I regularly take stimulant drugs and give me "
        "enhanced physical and mental abilities. Unlike most in the Antares, I can afford "
        "the good drugs, ones with no side effects or withdrawal symptoms.\n\n"
        "I am a 33 year old albino woman. I am 5 feet 11 inches tall, willowy, with "
        "white hair, white skin and red eyes. I dress expensively in pure white clothes."
    ),
    starting_merit_score=227,
    starting_credits=750000,
    starting_ship_name="Herald",
    starting_ship=ANTARES_ALL_SHIPS["Cyclone"],
    starting_system=ANTARES,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/mOC27YuJPu.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/g1vKsx3ub8.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/mOC27YuJPu.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/g1vKsx3ub8.jpg",
    ],
    current_portrait_index=0,
    portrait_prompt_details={
        "illustrClothes": "Futuristic business suit",
        "illustrSetting": "In front of a window with a futuristic skyline visible",
        "illustrAppearance": "An albino woman",
        "illustrExpressionPosition": "holding a datapad while reading a report from it",
    },
    skills={"Command": 4, "Piloting": 4, "Computers": 3, "Diplomacy": 4, "Engineering": 4},
)

elias = PlayableCharacterDef(
    first_name="Elias",
    last_name="Fadel",
    one_liner="A deserter and pirate hiding in the lawless reaches of Pleiadian space.",
    description=(
        "Elias is a deserter from the Pleiadean military. When he and his crew were commanded "
        "to go on a suicide mission, he refused, abandoning his duties and absconding with his "
        "military ship. Unable to return to civilian life, he fled to Spica, where no law "
        "enforcement would dare follow him. He lives now as a marauder and a pirate, preying "
        "on the weak and plundering their cargo."
    ),
    appearance="A hairless dark-skinned man with oversized eyes",
    background="You are a deserter from the Pleiadean military. When you and your crew were commanded "
        "to go on a suicide mission, you refused, abandoning your duties and absconding with your "
        "military ship. Unable to return to civilian life, you fled to Spica, where no law "
        "enforcement would dare follow you. You live now as a marauder and a pirate, preying "
        "on the weak and plundering their cargo.",
    first_action="I am lying in wait in the upper atmosphere of Nocthen, waiting for a freighter to pass by.",
    ai_guidance="The turn begins with me aboard by ship, the Manta, lying in wait in the upper atmostphere of Nocthen. "
        "The ship has gone dark - no active sensors, minimal life support. Me and the crew have had our genes modified so we can survive "
        "this, though it is still very uncomfortable. We are pirates, waiting stealthily for a freighter to pass by so we can plunder it. "
        "The wait is long, several hours of uncomfortable silence, before we see a target. A sole mule-class freighter is passing by, "
        "and there are no other ships in sight. We attack the ship, and the battle is unexpectedly fierce. The mule is equipped with a plasma "
        "launcher, and it hits is three times before we breach its hull and its crew are quickly killed by exposure to the vacuum of space. "
        "Me and my crew prepare to board the ship and plunder its cargo - a mule is not normally that well equipped, so the cargo must be "
        "something particularly valuable.",
    objective="Find a new life in the galaxy and leave your past behind.",
    instruction_block_content=(
        "I am a deserter from the Pleiadian military, which makes me a pariah to both "
        "the Pleiades government and MERIT. I am a wanted criminal in both, and so have "
        "to live in more lawless areas, such as Spica.\n\n"
        "I am 5 feet 8 inches tall, and muscular with very dark skin. My gene "
        "modifications mean I am hairless, with large, bulging eyes that give me a "
        "fishlike appearance."
    ),
    starting_merit_score=141,
    starting_credits=15000,
    starting_ship_name="Manta",
    starting_ship=PLEIADES_ALL_SHIPS["Bokrug"],
    starting_system=ASTEROPE,
    portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/H0dnHGTwiO.jpg",
    full_size_portrait_url="https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/y2VfXqrWrC.jpg",
    portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/meAMP8n3oi.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/H0dnHGTwiO.jpg",
    ],
    full_size_portrait_options=[
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/xdvEh9O0ze.jpg",
        "https://infinite-worlds-images-3.us-ord-1.linodeobjects.com/y2VfXqrWrC.jpg",
    ],
    current_portrait_index=1,
    portrait_prompt_details={
        "illustrClothes": "Armored spacesuit",
        "illustrSetting": "dark, derelict spaceship",
        "illustrAppearance": "A hairless dark-skinned man with oversized eyes",
        "illustrExpressionPosition": "crouched hiding",
    },
    skills={"Command": 4, "Piloting": 5, "Computers": 2, "Diplomacy": 3, "Engineering": 4},
)

PLAYABLE_CHARACTERS: tuple[PlayableCharacterDef, ...] = (jeremy, olivia, marco, mina, meilir, gulzat, elias)


# ---- What a character privately knows -----------------------------------------------------------

CHARACTER_SPECIFIC = iw.InstructionBlock(
    name="Character-specific instructions",
    content="THIS IS SET BY TRIGGERS",
)


# ---- Waking up ----------------------------------------------------------------------------------

def _start_of_game(pc: PlayableCharacterDef) -> iw.TriggerEvent:
    """Everything one character's world looks like at turn zero.

    The character sheet already carries triggers that fill it in for a given ship model, system and jump
    strength -- they fire every turn those match. Rather than recompute the same values here, we set the
    items those triggers are *gated* on (ship model, system) plus the hull they leave to the AI, then splice
    in the very effects each of the three would apply. Sharing the effect objects is deliberate and legal --
    `World.validate` only demands unique ids on items, blocks and characters, not on nested effects. The
    payoff is that the sheet is complete on the first turn instead of the second, and setting the gates is
    also what keeps those same triggers firing from turn one onward."""
    ship_details = player_details.SET_SHIP_DETAIL_TRIGGERS[pc.starting_ship.name]
    system_details = player_details.SET_SYSTEM_DETAIL_TRIGGERS[pc.starting_system.name]
    # A ship that cannot jump -- strength "None", like the cryosleeper -- has no sector-path trigger, and
    # none would fire for it in play either (they are gated on Soft/Moderate/Hard). So there is nothing to
    # splice, and its `Current sector paths` correctly stays blank until it is aboard something that jumps.
    sector_paths = player_details.SET_SECTOR_PATH_TRIGGERS.get(
        (pc.starting_system.name, pc.starting_ship.max_jump_strength)
    )

    effects = [
        iw.TriggerEffect(type=iw.EffectType.TELL_AI, data=pc.ai_guidance),
        iw.TriggerEffect(type=iw.EffectType.CHANGE_BACKGROUND, data=pc.background),
        iw.TriggerEffect(type=iw.EffectType.CHANGE_FIRST_ACTION, data=pc.first_action),
        iw.TriggerEffect(type=iw.EffectType.CHANGE_OBJECTIVE, data=pc.objective),

        iw.tools.set_tracked_item(player_details.MERIT_SCORE, str(pc.starting_merit_score)),
        iw.tools.set_tracked_item(player_details.CREDITS, str(pc.starting_credits)),
        iw.tools.set_tracked_item(player_details.CURRENT_SHIP_NAME, pc.starting_ship_name),

        # The two items the detail triggers are gated on but never set, plus the hull they leave to the AI.
        iw.tools.set_tracked_item(player_details.CURRENT_SHIP_MODEL, pc.starting_ship.name),
        iw.tools.set_tracked_item(player_details.CURRENT_SYSTEM, pc.starting_system.name),
        iw.tools.set_tracked_item(player_details.CURRENT_HULL_INTEGRITY, str(pc.starting_ship.max_hull_points)),

        # ...and the exact effects each detail trigger would apply once those gates match: ship info,
        # description, armor, jump strength and max hull; system info and the six jump slots; sector paths.
        *ship_details.triggerEffects,
        *system_details.triggerEffects,
        *(sector_paths.triggerEffects if sector_paths else []),
    ]

    if pc.instruction_block_content is not None:
        effects.append(iw.TriggerEffect(
            type=iw.EffectType.MODIFY_INSTRUCTION_BLOCK,
            data={"id": CHARACTER_SPECIFIC.id, "content": pc.instruction_block_content},
        ))

    return iw.TriggerEvent(
        name=f"Start of game - {pc.first_name}",
        triggerEffects=effects,
        triggerConditions=[
            iw.TriggerCondition(
                type=iw.ConditionType.ON_CHARACTER,
                category="condition",
                data=[pc.character.characterId],
            ),
        ],
        triggerOnStartOfGame=True,
    )


def _first_turn_trent(trent: PlayableCharacterDef) -> iw.TriggerEvent:
    """Trent was frozen in 2638. The AI needs reminding that he does not know his own century."""
    return iw.TriggerEvent(
        name="First turn - Trent",
        triggerEffects=[
            iw.TriggerEffect(
                type=iw.EffectType.GIVE_INFO,
                data=(
                    "Remember that I was frozen in the year 2638. Until I learn about it, I do not know about anything "
                    "that has happened since then. Notably:\n"
                    "- I do not know that humanity has developed the Jump Drive and spread to other solar systems\n"
                    "- I do not know about the existence of the Stellar Concordium\n"
                    "- I do not know that MERIT has expanded in scope"
                ),
            ),
        ],
        triggerConditions=[
            iw.TriggerCondition(type=iw.ConditionType.ON_TURN, category="condition", data=1),
            iw.TriggerCondition(
                type=iw.ConditionType.ON_CHARACTER,
                category="condition",
                data=[trent.character.characterId],
            ),
        ],
    )


def character_triggers() -> list[iw.TriggerEvent]:
    """One start-of-game trigger per character, plus Trent's amnesia."""
    events = [_start_of_game(pc) for pc in PLAYABLE_CHARACTERS]
    trent = next(pc for pc in PLAYABLE_CHARACTERS if pc.first_name == "Trent")
    events.append(_first_turn_trent(trent))
    return events


def install_into(world: iw.World) -> None:
    """Add the skill roster, the seven playable characters, the block their start-of-game triggers
    rewrite, and those triggers.

    Order-independent: each start-of-game trigger sets everything about where its character wakes up --
    ship, system, jump points and reachable paths -- itself, so it does not matter where in the assembly
    this lands relative to the subsystems those values come from."""
    world.skills = SKILLS
    world.possibleCharacters.extend(pc.character for pc in PLAYABLE_CHARACTERS)
    world.instructionBlocks.append(CHARACTER_SPECIFIC)
    world.triggerEvents.extend(character_triggers())
