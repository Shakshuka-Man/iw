"""The six powers, and the fleet each one flies.

One block per faction, and each ends the same way: a list of the ships that faction uses, generated from
`ships/` rather than typed. Add a ship to a faction and its block says so -- which is the whole reason
these blocks live next to a function that reads the fleet, instead of next to a hand-written list that
would quietly go stale.

Each of the five outer clusters is a different answer to the same question -- what may be done to a human
body to make it more useful -- and each block ends with MERIT's objection to that answer. That is the
argument the war is about.

`INNER_SYSTEMS` is MERIT's own block. It doubles as the rules for how a MERIT score is actually used
against you, which is why it is the longest; the score itself is on the character sheet in `player_details`.
"""

import iw

from .ships import (
    ANTARES_ALL_SHIPS,
    CANOPUS_ALL_SHIPS,
    HYADES_ALL_SHIPS,
    INDEPENDENT_ALL_SHIPS,
    MERIT_ALL_SHIPS,
    PLEIADES_ALL_SHIPS,
    POLARIS_ALL_SHIPS,
)


def _ship_list(ships: dict) -> str:
    """The faction's fleet, as the bullet list its instruction block ends with."""
    return "\n".join(f"- {ship.name}: {ship.short_description}" for ship in ships.values())


INNER_SYSTEMS = iw.InstructionBlock(
    name="Inner Systems",
    content=(
        "Every citizen of the Concordium has a MERIT score: a quantified measure of how well they "
        "align with MERIT's interpretation of a \"productive, compliant, and socially beneficial\" life. "
        "MERIT is very utilitarian and pragmatic - it will guarantee every individual food, "
        "accommodation, healthcare, and all things necessary to be productive.\n\n"
        "Within the inner systems, MERIT continuously observes and assesses each citizen. This is to "
        "ensure that their MERIT score is kept up to date, and also to determine their competencies. "
        "Individuals have no choice in their education or profession, they are assigned to whatever role "
        "MERIT determines is most appropriate for them.\n\n"
        "Citizens are born with a MERIT score of 500. Actions that MERIT approves of will asymptotically "
        "increase the score towards 1000, though 1000 will never be reached. Similarly, actions that "
        "MERIT disapproves of will asymptotically decrease the score towards 0, though 0 will never be "
        "reached.\n\n"
        "Merit scores do not directly determine quality of life in the inner systems. Instead, they are "
        "used to resolve all forms of conflict. If two individuals ever come into conflict, then it does "
        "not matter what is right or fair, it only matters who has the highest MERIT score. Some "
        "examples would be:\n"
        "- On a Concordium navy ship, the finest living quarters do not go to the highest rank "
        "individual, they go to the individual with the best MERIT score\n"
        "- If a restaurant has no free tables, then a low-scoring individual will be thrown out mid-meal "
        "to make room for a high-scoring individual\n"
        "- Two parents are in dispute over custody of their child, MERIT will favor the one with the "
        "highest score\n\n"
        "This causes the low scorers to be wary around the high scorers. When around someone with a "
        "higher MERIT score, they can violate any one of your rights at any point. It is not the case "
        "that high scorers can live like tyrants, however -if someone abuses their score too frequently, "
        "that itself is considered a MERIT violation, and they will have their score lowered "
        "appropriately.\n\n"
        "For individual in the inner systems, maintaining a high MERIT score is extremely important. "
        "Having a score lowered is one of the worst things that can happen to an individual, and they "
        "will be terrified of doing anything that could negatively impact their score.\n\n"
        "MERIT uniforms are navy blue and silver, and their ships use these colors as highlights. "
        "The following ships are used by the MERIT / SCN faction:\n"
        + _ship_list(MERIT_ALL_SHIPS)
    ),
)


POLARIS = iw.InstructionBlock(
    name="Polaris",
    content=(
        "Polaran technology allows direct connection between the human nervous system and computer "
        "systems. The technology exists on a spectrum. At the basic level, non-surgical interfaces -- "
        "headsets, contact patches, portable rigs -- allow anyone to connect to the Polaran neural "
        "network. At the intermediate level, pilots and skilled workers receive surgical interface ports "
        "along the spine, skull, and forearms, giving them direct neural connections to the systems they "
        "operate. At the extreme, capital ships require human brains to be permanently fused to the "
        "ship's hull. These individuals -- called Cores -- are the most capable ship operators in the "
        "galaxy, but they will never walk, touch, or exist outside their ship again.\n\n"
        "Neural integration is not just for piloting. The Polaran economy runs on telepresence. A "
        "surgeon sits in an interface cradle on one world and operates robotic surgical instruments on "
        "a patient in another system, working at scales from human down to cellular. An engineer in a "
        "cradle assembles micro-scale circuitry on a relay station light-years away. A miner controls "
        "robotic proxies on a planet too hostile for human survival from a comfortable orbital station. "
        "The interface makes the remote tools feel like the operator's own hands. The dangerous work is "
        "performed by machines. The skilled work is performed by minds in safe locations. The bodies "
        "stay stationary in cradles -- maintained with hydration, nutrition, and muscle stimulation -- "
        "while the minds work across the cluster.\n\n"
        "Polaran life is structured around the disconnect hours -- the windows when the population "
        "unplugs from their interface cradles to eat, exercise, and socialise. The streets fill during "
        "disconnect. Relationships are maintained with compressed intensity because time physically "
        "together is limited and precious. During working hours, the cities are empty -- the population "
        "is indoors, plugged in, their bodies still.\n\n"
        "VR is a practical tool, not a plague. Surgeons use it to control robots at different scales. "
        "Architects design buildings as full-scale immersive environments clients can inhabit before "
        "construction. Artists create experiences the audience enters rather than views. Some people "
        "develop unhealthy dependencies, the way some people develop unhealthy relationships with any "
        "powerful technology, but VR addiction is a problem for some individuals, not an endemic crisis "
        "that defines the faction.\n\n"
        "The Cores govern the cluster. The stratocracy is literal: the pilots permanently fused to "
        "capital ships are the governing body, orbiting the capital world of Thessan in a formation "
        "called the Procession. They govern through the neural network, their decisions transmitted to "
        "the ground as policy. They have not walked on a planet, breathed air, or held another person "
        "in decades. The world they govern is a data set to them. Their decisions are competent. Their "
        "understanding of what ground life feels like is increasingly theoretical.\n\n"
        "The wealth divide is the interface. The wealthy have private cradles with medical monitoring "
        "and premium hardware -- precise, low-latency, sensory fidelity indistinguishable from physical "
        "presence. The poor use shared rigs in commercial centres -- rows of chairs in rented spaces, "
        "functional hardware with slightly higher lag and slightly lower precision. The difference "
        "compounds over a career. Cheap rigs produce interface drift -- a gradual degradation of the "
        "boundary between the operator's sense of their own body and the remote equipment, where the "
        "worker's body no longer feels entirely like theirs after disconnecting.\n\n"
        "Polaran warships favour agility and precision. Neural-piloted ships respond to intention "
        "rather than manual input, moving before the conscious thought that would have directed a "
        "control is complete. Ships in formation share tactical awareness through the network, moving "
        "as a single organism. The ships are light, fast, and fragile -- the design trades protection "
        "for agility because reaction times make agility more valuable than armour. A Polaran ship that "
        "is hit is in serious trouble. A Polaran ship that is not hit is the most dangerous opponent "
        "in the galaxy.\n\n"
        "**MERIT's objection:** The Cores who govern have not touched the ground in decades. They make "
        "decisions about lives they no longer understand, experienced only through sensor feeds and data "
        "streams. The interface hierarchy means political voice correlates with how far you have gone "
        "from baseline human experience. The people who govern the civilisation are the people least "
        "capable of understanding what life in that civilisation feels like. A society that requires "
        "its citizens to sit motionless in chairs while their minds work elsewhere has not enhanced "
        "humanity -- it has reduced the body to a container that the mind tolerates between sessions.\n\n"
        "Polaris uniforms are indigo and ice blue, and their ships use these colors as highlights. "
        "The following ships are used by the Polaris faction:\n"
        + _ship_list(POLARIS_ALL_SHIPS)
    ),
)


CANOPUS = iw.InstructionBlock(
    name="Canopus",
    content=(
        "Canopan technology can bring the dead back to life, as long as the body is not too severely "
        "damaged. However, the quality of restoration varies enormously with cost.\n\n"
        "The highest quality restoration can only be afforded by the rich, using neural reconstruction "
        "and cloned tissue to perfectly repair damage. The Canopan elite -- the emperors who rule the "
        "cluster's feudal hierarchy -- have been restored dozens of times over centuries, accumulating "
        "wealth and power across lifetimes that no natural lifespan could produce. The original person "
        "is a distant memory. The current version is a political entity that has outlived every rival "
        "and every reform.\n\n"
        "Low-quality restoration produces shells. They walk, they carry, they work, but there is "
        "nothing behind the eyes. They work out of public sight because even in Canopan culture, the "
        "sight of the shells is deeply unsettling. Families in poverty sell the bodies of their dead "
        "to cover debts, knowing their loved one will spend years performing manual labour as a shell.\n\n"
        "The cluster is governed by a feudal hierarchy of immortal emperors. Each system is ruled by "
        "an emperor who has held power for centuries through repeated high-quality restoration. The "
        "emperors are not elected, not appointed, and not removable -- they simply do not die. Political "
        "change in Canopus requires waiting for an emperor to choose to step down, which no emperor has "
        "done in the cluster's history. The aristocracy beneath them calculates in generations because "
        "the rulers above them are permanent.\n\n"
        "Canopan vessels are built for endurance and recovery. Heavy armour, redundant systems, "
        "extensive medical and reconstruction bays. Canopan warships carry reanimation facilities "
        "onboard -- crew losses in battle are temporary, as damaged crew are pulled from wreckage, "
        "restored or reanimated, and returned to their stations. Canopan ships absorb damage that "
        "would be catastrophic for other fleets, and the tactical planning accounts for an enemy that "
        "does not stop when it should.\n\n"
        "**MERIT's objection:** Death is a boundary that should be respected. Reanimated labourers "
        "cannot consent to their condition. Diminished restoration robs a person of who they were while "
        "insisting they should be grateful. A society that treats corpses as an economic resource has "
        "lost something fundamental about human dignity. The emperors who rule the cluster have cheated "
        "death so many times that the original person is a legal fiction maintained for the convenience "
        "of the power structure.\n\n"
        "Canopus uniforms are crimson and gold, and their ships use these colors as highlights. "
        "The following ships are used by the Canopus faction:\n"
        + _ship_list(CANOPUS_ALL_SHIPS)
    ),
)


ANTARES = iw.InstructionBlock(
    name="Antares",
    content=(
        "Antarian society runs on drugs. Not just for combat or recreation -- for everything. Cognitive "
        "enhancers for intellectual work. Focus compounds for engineering. Creativity stimulants for "
        "art. Endurance boosters for labour. Social enhancers for diplomacy and negotiation. Reaction "
        "accelerants for piloting.\n\n"
        "The drugs work, but they degrade the user over time. The severity depends entirely on quality, "
        "which depends entirely on wealth. The wealthy get precision-manufactured pharmaceuticals with "
        "minimal side effects -- their enhanced performance is clean, sustainable, and nearly invisible. "
        "The poor get crude compounds produced in bulk, with side effects that accumulate: tremors, "
        "cognitive fog, organ damage, the visible deterioration that marks a lifetime of cheap "
        "enhancement.\n\n"
        "Abstinence is not a viable option. Performance expectations across Antarian society are "
        "calibrated to enhanced baselines. A person who chooses to stay clean cannot get hired, cannot "
        "keep up in school, cannot maintain social relationships with people operating at enhanced speed "
        "and charisma. The sober are not persecuted -- they are simply irrelevant.\n\n"
        "The cluster is governed by a corporate-owned democracy. The pharmaceutical corporations that "
        "produce the enhancement drugs are the real power. Elected officials govern in name. The "
        "corporations govern in practice, because the corporations control the supply that every citizen "
        "depends on. The politicians are not puppets -- they are employees of a system where the "
        "employer controls the substance the electorate cannot function without.\n\n"
        "Antarian vessels are fast, aggressive, and designed for enhanced crews. Control systems are "
        "calibrated for stimmed reaction times -- impossibly fast for a baseline human. Antarian "
        "warships favour speed and overwhelming offence. The downside is crew burnout -- long "
        "engagements degrade performance as stims wear off, and ships carry enormous pharmaceutical "
        "stores. A ship that runs out of stims has a crew going into withdrawal mid-combat.\n\n"
        "**MERIT's objection:** A society that requires chemical enhancement to participate has "
        "eliminated meaningful choice. When sobriety means destitution, consent to take stimulants is "
        "coerced. A culture that doses children from infancy has not enhanced humanity -- it has created "
        "a population of dependents who have never known their own unaltered minds.\n\n"
        "Antares uniforms are navy blue and silver, and their ships use these colors as highlights. "
        "The following ships are used by the Antares faction:\n"
        + _ship_list(ANTARES_ALL_SHIPS)
    ),
)


HYADES = iw.InstructionBlock(
    name="Hyades",
    content=(
        "The Hyades cluster is industrial, practical, and dangerous. Injuries are constant. Losing a "
        "limb or organ is routine. Hyades prosthetic technology is robust, widely available, and often "
        "functionally superior to the organic original.\n\n"
        "Economic pressure drives people to voluntarily amputate healthy limbs and organs for mechanical "
        "replacements they can barely afford. Young workers cut off perfectly good arms to install "
        "factory-rated prosthetics because a kid with a mechanical grip gets hired and a kid with flesh "
        "hands doesn't. Clinics performing voluntary amputations range from sterile medical facilities "
        "for the wealthy to back-alley chop shops for the poor.\n\n"
        "The wealthy get top-of-the-line prosthetics that are perfectly responsive and self-maintaining. "
        "The poor can only afford hardware that needs constant maintenance and replacement. Over a "
        "lifetime, a working-class Hyades citizen is gradually replaced piece by piece until very "
        "little of the original person remains. Some embrace it. Many mourn each piece they lose. "
        "Almost nobody has a real choice.\n\n"
        "The cluster is governed by a guild republic. Trade guilds organised around prosthetic "
        "specialisation are the units of political representation -- your guild is your political "
        "identity, your social identity, and your healthcare provider. The guilds negotiate with each "
        "other through a council, and the negotiation is the government. The system is pragmatic and "
        "functional, but the negotiation can become the product -- guilds trading concessions on "
        "territorial claims for advantages in unrelated disputes until the gridlock becomes "
        "structurally necessary.\n\n"
        "A Hyades warship might be centuries old with every component swapped out dozens of times. "
        "Ships are tough, industrial, unglamorous -- exposed conduits, visible welds, mechanical rather "
        "than elegant. Crews interface with ships through their prosthetics. Ships are designed around "
        "the assumption that the crew is partially mechanical.\n\n"
        "**MERIT's objection:** A society where economic pressure drives people to amputate healthy "
        "body parts has not enhanced humanity. When keeping your own body puts you at a competitive "
        "disadvantage, the freedom to choose replacement is an illusion. Wholeness has become a luxury "
        "only the wealthy can afford -- and even they have given it up.\n\n"
        "Hyades uniforms are maroon and yellow, and their ships use these colors as highlights. "
        "The following ships are used by the Hyades faction:\n"
        + _ship_list(HYADES_ALL_SHIPS)
    ),
)


PLEIADES = iw.InstructionBlock(
    name="Pleiades",
    content=(
        "The Pleiades cluster is rich in alien life. Not intelligent life, but varied, complex, and "
        "evolved to thrive in extreme environments. The inhabitants splice alien genes into their own "
        "bodies, gaining the adaptations necessary to survive on worlds that would kill a baseline "
        "human. Photosynthetic skin pigments from radiation-feeding organisms. Calcium-silicate skeletal "
        "reinforcement from high-gravity megafauna. Modified respiratory systems from species that "
        "breathe toxic atmospheres. The alien biology provides solutions that human engineering cannot "
        "match.\n\n"
        "Terraforming has happened in the core systems, but the further out you go, the less "
        "terraforming there is. In the Pleiades, it is more economical to adapt the humans than to "
        "terraform the planet. This is not seen as more desirable, just more economical. The "
        "modifications are cumulative and irreversible. Each one shifts the body further from baseline. "
        "Each interacts with the others, creating dependencies and unexpected side effects.\n\n"
        "Each planet's specific hazards require specific adaptations. A worker modified for a high-"
        "gravity world develops dense musculature and a dual cardiovascular system. A worker on a "
        "radiation-saturated world develops skin that feeds on ultraviolet light. A worker on a toxic-"
        "atmosphere world develops modified lungs and altered blood chemistry. The adaptations that let "
        "you survive your world are the same adaptations that prevent you from surviving anyone else's. "
        "The most deeply modified Pleiadians can survive only on the single planet they were modified "
        "for.\n\n"
        "The cluster is governed by a strain confederation. Each planet has produced a biologically "
        "distinct strain -- populations modified for specific environments that have diverged far enough "
        "to be effectively sub-species. The confederation negotiates between strains that are drifting "
        "apart biologically, conducted by moderately modified diplomats who serve as the connective "
        "tissue of a civilisation whose populations are becoming different species. The confederation "
        "council meets in sealed pods -- individual environments calibrated to each delegate's home "
        "conditions -- because the delegates can no longer share a room.\n\n"
        "The wealthy get precision bioengineering -- carefully planned, elegantly integrated, minimal "
        "visible change. A rich Pleiadian might carry a dozen modifications and still pass for "
        "baseline. The poor get bulk modifications -- cheap, aggressive, poorly integrated, and "
        "permanently trapping. Wealth buys you the right to leave your world. Poverty buys you "
        "survival at the cost of imprisonment.\n\n"
        "Gene-splicing requires stabilisation compounds derived from organisms found primarily on the "
        "remote world of Electra. Without regular doses, the alien gene sequences begin to express "
        "unpredictably, producing changes the original splicing did not intend. The deeper the "
        "modification, the more dependent the person is on the compounds. The supply chain from "
        "Electra is the cluster's jugular.\n\n"
        "The gene-splicing process requires extensive animal testing -- baseline organisms modified "
        "with alien gene sequences, monitored for compatibility. The testing facilities include cloned "
        "human tissue matrices that are not legally persons but that develop nervous systems registering "
        "what is being done to them. The testing wings are not open to visitors.\n\n"
        "Pleiadian ships are stripped down to what the modified crew can tolerate. Atmospherics are "
        "minimal -- thin, chemical-heavy air that baseline lungs can't process. Lighting is sparse or "
        "absent -- crews see in infrared. Temperature is near-freezing. The ships are not designed to "
        "be hostile -- they just weren't designed for baseline humans. This makes Pleiadian ships "
        "cheap, light, and numerous.\n\n"
        "**MERIT's objection:** Cumulative, irreversible alteration of the human body driven by "
        "economic necessity rather than genuine choice strips people of the ability to return to "
        "baseline existence. A society that splices alien genes into its population has fragmented "
        "humanity into isolated sub-species trapped on individual worlds, with the poor the most "
        "trapped and the most altered. The freedom to choose modification is meaningless when the "
        "choice is between modification and death on a world you cannot leave.\n\n"
        "Pleiadian uniforms are dark green and violet, and their ships use these colors as highlights. "
        "The following ships are used by the Pleiades faction:\n"
        + _ship_list(PLEIADES_ALL_SHIPS)
    ),
)


INDEPENDENT_SHIPS = iw.InstructionBlock(
    name="Independent ships",
    content=(
        "The following ships are not aligned to any particular faction "
        "and can be found in any location in space:\n"
        + _ship_list(INDEPENDENT_ALL_SHIPS)
    ),
)


def install_into(world: iw.World) -> None:
    """Add the six powers -- the inner systems and the five outer factions -- and the independents."""
    world.instructionBlocks.extend(
        [INNER_SYSTEMS, POLARIS, CANOPUS, ANTARES, HYADES, PLEIADES, INDEPENDENT_SHIPS]
    )
