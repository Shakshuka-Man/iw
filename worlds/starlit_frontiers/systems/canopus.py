from ..enums import StarClusters
from .models import System, StellarObject

CANOPUS = System(
    name='Canopus',
    star='Bright yellow-white supergiant (F0Ib-II), approximately 10,000 times Sol luminosity -- the second brightest star visible from Earth, enormous and radiant, casting brilliant white-gold light',
    population=15_000_000_000,
    distance_to_sol=310.0,
    stellar_objects=[
        StellarObject(
            name='Vethane',
            short_description='The nominal capital of the Canopus cluster -- seat of the Emperor of Canopus and the council chamber where the cluster\'s emperors convene.',
            long_description=(
                'Vethane is the nominal capital of the Canopus cluster -- the world where '
                'the council of emperors meets, where the diplomatic functions of the '
                'Undying are conducted, and where the Emperor of Canopus maintains the seat '
                'that tradition designates as first among equals. The Emperor of Canopus is '
                'old. All the emperors are old -- reanimated enough times that the original '
                'person is layers deep beneath the restorations -- but the Emperor of '
                'Canopus is among the oldest, a figure whose first life ended centuries ago '
                'and whose current existence is maintained by the finest reanimation '
                'technology the cluster can provide.\n\n'
                'The council chamber on Vethane is where the emperors of the cluster\'s '
                'systems meet to coordinate policy, allocate military resources, and manage '
                'the collective governance of a civilisation built on the premise that '
                'death is a problem to be solved rather than a fate to be accepted. The '
                'council is not a democracy. The emperors rule their systems through the '
                'kings who govern individual planets, and the kings hold their positions '
                'through the same mechanism that sustains the emperors: they can afford to '
                'keep dying and coming back. Wealth buys reanimation. Reanimation buys '
                'time. Time buys power. The cycle is self-reinforcing and has been running '
                'for centuries.\n\n'
                'Vethane itself is a temperate, well-developed world bathed in the '
                'brilliant white-gold light of the Canopus supergiant -- a star so luminous '
                'that the daylight on Vethane is brighter and more vivid than on almost '
                'any other inhabited world. The cities are grand in the way that ancient '
                'power produces grandeur: monumental architecture, wide processional '
                'avenues, and the palaces of the planetary kings who maintain their courts '
                'with the accumulated wealth of lifetimes that have spanned centuries. The '
                'population is large, prosperous by Canopan standards, and accustomed to '
                'the presence of rulers who do not age and do not leave.\n\n'
                'The shells on Vethane are kept carefully out of sight. The nominal capital '
                'maintains appearances: the reanimated labour force that sustains the '
                'infrastructure works underground, in the service tunnels beneath the '
                'monumental streets, in the maintenance corridors that visitors never see. '
                'The surface of Vethane is for the living and the well-restored. The '
                'shells -- the cheap, crude reanimations that are barely more than animated '
                'corpses -- are not part of the image that the capital projects.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Ganthor',
            short_description='A military world -- the Canopan fleet\'s forward base, staging the heavy warships that guard the gateway to the cluster.',
            long_description=(
                'Ganthor is the system\'s military heart -- a rocky, cold world whose '
                'surface installations and orbital facilities house the Canopan fleet\'s '
                'forward garrison. The fleet stationed at Ganthor is substantial: the '
                'heavy, dense, thick-hulled warships that define Canopan military doctrine, '
                'built to absorb damage that would destroy other factions\' vessels, crewed '
                'by personnel who fight differently because death is not permanent for '
                'them.\n\n'
                'The Canopan military advantage is attritional. The crews can be reanimated. '
                'A ship that loses half its crew to a MERIT broadside can have those crew '
                'members restored and returned to duty -- not immediately, not cheaply, but '
                'within weeks rather than the months or years that training replacements '
                'would require. The fleet absorbs losses that would cripple other navies '
                'and continues fighting. The morale implications are complex: the crews '
                'know that death is not the end, which makes them willing to accept risks '
                'that other crews would not. It also means that the same person can die in '
                'combat, be reanimated, and be sent back to die again, and the psychological '
                'toll of repeated death and restoration is a problem that Canopan military '
                'medicine has documented extensively and solved inadequately.\n\n'
                'The garrison on Ganthor includes reanimation facilities for military '
                'personnel -- not the luxurious restoration suites that the emperors and '
                'kings use but functional military-grade installations that bring dead crew '
                'members back to operational status as quickly as possible. The quality is '
                'adequate. The restored personnel are functional. They are not always who '
                'they were before, and the degree to which repeated military reanimation '
                'erodes the person underneath is a subject that the fleet command '
                'acknowledges in classified reports and does not discuss publicly.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Tesseret',
            short_description='A temperate second world -- civilian, commercial, and the system\'s economic engine beneath its own planetary king.',
            long_description=(
                'Tesseret is the system\'s civilian counterpart to Ganthor\'s military '
                'presence -- a temperate, well-developed world with a diversified economy '
                'that supports the system\'s fifteen billion people. The planetary king of '
                'Tesseret is one of the wealthier rulers in the system -- the commercial '
                'economy generates revenue that funds both the king\'s court and the '
                'planet\'s contribution to the cluster\'s military operations.\n\n'
                'The cities on Tesseret are prosperous and hierarchical in the way that '
                'all Canopan civilisation is hierarchical: the well-restored at the top, '
                'living in districts where the architecture reflects centuries of '
                'accumulated wealth; the living middle class beneath them, working the '
                'professional and skilled occupations that the economy requires; and the '
                'shells at the bottom, out of sight, performing the labour that sustains '
                'everything above. The hierarchy is not unique to Tesseret. It is the '
                'structure of every Canopan world. Tesseret is simply the version of it '
                'that visitors encounter first, because Tesseret handles much of the '
                'civilian traffic that enters the cluster through the gateway.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='The Veil',
            short_description='The contested space where the routes to the inner systems converge -- patrolled by the Canopan fleet and probed by MERIT from Castor.',
            long_description=(
                'The Veil is the volume of space where the jump routes connecting the '
                'Canopus cluster to the inner systems converge. All traffic passes through '
                'here -- military, commercial, the smugglers running reanimation technology '
                'to Pollux, and the independent traders who carry goods between civilisations '
                'that are officially at war. The Canopan fleet patrols the Veil in '
                'strength, and MERIT\'s forces from Castor probe it regularly -- testing '
                'response times, mapping patrol patterns, and occasionally engaging in the '
                'skirmishes that both sides treat as intelligence-gathering rather than '
                'combat.\n\n'
                'The Veil is busier than its Antarian equivalent. The Canopus cluster '
                'trades more heavily with the inner systems than the Antares does -- the '
                'reanimation technology that Pollux\'s black market craves, the luxury goods '
                'that Canopan artisans produce, and the raw materials that the cluster\'s '
                'industry demands all flow through this contested space. The independent '
                'traders who navigate the Veil have learned to read the tactical '
                'situation the same way traders at Antares\' Gateway have: know the patrol '
                'patterns, time the transits, and accept the risk as the cost of doing '
                'business with a civilisation that the inner systems officially condemn and '
                'unofficially cannot do without.'
            ),
            population=0,
        ),
        StellarObject(
            name='Coronet Station',
            short_description='The system\'s primary orbital port -- where the cluster\'s trade is processed and the emperors\' representatives greet arriving dignitaries.',
            long_description=(
                'Coronet Station is the Canopus system\'s primary orbital facility -- a '
                'large station in orbit above Vethane that handles the system\'s military, '
                'commercial, and diplomatic traffic. The station is designed to impress: '
                'the diplomatic reception areas are as grand as anything on the surface, '
                'because Coronet is the first Canopan installation that visitors from the '
                'inner systems encounter and the council of emperors is particular about '
                'first impressions.\n\n'
                'The traffic at Coronet is heavy and mixed. Military vessels dock alongside '
                'commercial freighters and the private yachts of the Canopan elite -- '
                'ancient, wealthy figures whose personal vessels are maintained to standards '
                'that exceed some navies. The commercial district serves the traders who '
                'move goods between the cluster and the inner systems, and the prices '
                'reflect the gateway premium: everything costs more at the point where two '
                'civilisations meet.\n\n'
                'The shells on Coronet Station handle the cargo. The loading, unloading, '
                'sorting, and movement of goods through the station\'s freight bays is '
                'performed by reanimated labour that works the shifts no living worker '
                'would accept -- continuous, around the clock, without rest or complaint. '
                'The shells work the freight bays at night when the commercial district is '
                'quiet, and are moved to interior corridors before the station\'s day cycle '
                'begins. Visitors who arrive during the day see a station run by the living. '
                'Visitors who arrive at night see the truth.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Kelvorin',
            short_description='A gas giant whose fuel processing supports the system\'s heavy military and commercial traffic -- crewed by the living, maintained by the dead.',
            long_description=(
                'Kelvorin is the system\'s gas giant -- a large body in the outer system '
                'whose moons host fuel processing operations sized for the Canopus system\'s '
                'enormous traffic volume. The military fleet, the commercial traffic, and '
                'the steady flow of ships entering and leaving the cluster all require fuel, '
                'and Kelvorin\'s operations run continuously to meet the demand.\n\n'
                'The fuel processing is managed by living engineers and technicians. The '
                'physical labour -- the maintenance, the cleaning, the repairs that are too '
                'dangerous or too tedious for living workers -- is performed by shells. The '
                'arrangement is standard across the cluster: the skilled work is done by '
                'people who can think. The work that requires only a body is done by bodies '
                'that no longer think. The fuel workers on Kelvorin\'s moons have learned not '
                'to look too closely at the shells that share their workspace. The shells '
                'were people once. The workers know this. Acknowledging it makes the '
                'arrangement harder to live with, so they do not acknowledge it.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Solarn',
            short_description='A hot inner world -- energy collection powering the system\'s infrastructure, maintained by shells because the radiation makes living workers expensive to replace.',
            long_description=(
                'Solarn is a hot, dense inner world close to the brilliant supergiant -- '
                'solar collection arrays harvesting the star\'s enormous output to power '
                'the system\'s military and civilian infrastructure. The radiation '
                'environment is harsh. Living workers who maintain the arrays accumulate '
                'exposure that shortens their lives. Shells that maintain the arrays '
                'accumulate exposure that degrades their remaining function. The difference '
                'is cost: a living worker who dies from radiation exposure is a loss. A '
                'shell that ceases functioning from radiation exposure is replaced from the '
                'supply. The economics are clear. Solarn\'s maintenance crews are '
                'predominantly shells, supervised by a small living staff who monitor from '
                'shielded facilities and manage the rotation of shells as they degrade.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Verdath',
            short_description='An agricultural world feeding the system -- fertile, productive, and farmed by a mix of living workers and shells who do the work that is too hard or too dangerous.',
            long_description=(
                'Verdath is the system\'s agricultural world -- warm, fertile, and farmed '
                'at a scale that feeds fifteen billion people. The farming is conducted by '
                'a workforce that is part living, part reanimated: the skilled agricultural '
                'work -- crop management, soil chemistry, genetic engineering of crop '
                'strains -- is performed by living workers. The manual labour -- planting, '
                'harvesting, the physical work that is repetitive and gruelling -- is '
                'performed by shells.\n\n'
                'The division is practical and visible. The living workers manage the '
                'operations from climate-controlled facilities. The shells work the fields '
                'in daylight, in heat, in conditions that would exhaust a living worker '
                'within hours and that a shell endures until it stops functioning. The '
                'shells on Verdath are replaced regularly -- the physical demands of '
                'agricultural labour wear them down faster than less demanding work -- and '
                'the replacement cycle is managed with the same logistical efficiency that '
                'governs the crop rotation. The planetary king of Verdath considers the '
                'agricultural output a point of pride. The method of achieving it is not '
                'discussed at court.'
            ),
            population=1_800_000_000,
        ),
    ],
    short_description='Gateway to the Undying -- the nominal capital of a cluster ruled by emperors who have cheated death for centuries, guarded by fleets crewed by people for whom death is not permanent.',
    long_description=(
        'Canopus is the gateway to the cluster of the Undying and the nominal capital '
        'of a civilisation built on the defeat of death. The star is a brilliant '
        'yellow-white supergiant -- 10,000 times Sol\'s luminosity, casting vivid '
        'white-gold light across worlds ruled by emperors and kings who have been '
        'reanimated so many times that the original person is buried beneath layers '
        'of restoration. The council of emperors meets on Vethane in a chamber whose '
        'occupants have collectively been alive for millennia, each one sustained by '
        'the technology that defines their civilisation and the wealth that makes the '
        'technology available.\n\n'
        'Fifteen billion people live in the Canopus system across worlds that are '
        'prosperous, hierarchical, and sustained by a labour force that is partly '
        'alive and partly reanimated. The shells -- the crude, cheap reanimations that '
        'serve as the cluster\'s workforce -- are kept out of sight on the capital '
        'worlds, working underground, in service tunnels, at night. The surface is '
        'for the living and the well-restored. The image that Canopus projects is '
        'grandeur, permanence, and the triumph over mortality. The reality that '
        'sustains the image is a labour economy built on animated corpses.\n\n'
        'The military presence is heavy. The Canopan fleet guards the Veil -- '
        'the contested space where the routes to the inner systems converge -- with '
        'the heavy, dense warships that define Canopan doctrine. The crews fight '
        'knowing that death is not permanent, which makes them willing to accept '
        'risks other navies would not. The ships absorb damage that would be '
        'catastrophic for other fleets. The attritional advantage is real and '
        'expensive: reanimating crew members is not cheap, and the psychological toll '
        'of repeated death and restoration is a cost that the fleet\'s classified '
        'reports document and the fleet\'s public statements do not mention.\n\n'
        'The trade through the gateway is heavy -- heavier than the Antarian '
        'equivalent. Reanimation technology flows to Pollux\'s black market. Luxury '
        'goods and raw materials flow in both directions. Independent traders navigate '
        'the Veil with the same careful skill as those at Antares\' Gateway. The '
        'cluster officially condemns the smuggling of its technology to the inner '
        'systems and unofficially benefits from the revenue. The emperors are '
        'pragmatic. They have had centuries to learn pragmatism.'
    ),
    cluster=StarClusters.CANOPUS,
)

ADHARA = System(
    name='Adhara',
    star='Hot blue-white giant (B2II), approximately 22,000 times Sol luminosity -- one of the brightest stars in the cluster, casting intense blue-white light across the system',
    population=28_000_000_000,
    distance_to_sol=430.0,
    stellar_objects=[
        StellarObject(
            name='Sovrath',
            short_description='The de facto capital of the Canopus cluster -- ten billion people in a civilisation older and richer than anything on Vethane, ruled by an emperor who considers the council a formality.',
            long_description=(
                'Sovrath is where the power is. Vethane on Canopus is the nominal capital '
                '-- the council chamber, the diplomatic functions, the ceremonies. Sovrath '
                'is the de facto capital -- the world with the largest population, the '
                'greatest economic output, and an emperor whose wealth and influence exceed '
                'the Emperor of Canopus by a margin that the council\'s protocol of equals '
                'cannot conceal. The Emperor of Adhara attends the council meetings on '
                'Vethane. The Emperor of Adhara\'s preferences are known before the meetings '
                'begin, and the other emperors adjust their positions accordingly. The '
                'council is a formality. The decisions are made on Sovrath.\n\n'
                'The planet is enormous, well-terraformed, and developed to a degree that '
                'reflects centuries of continuous investment by rulers who do not die and '
                'therefore plan on timescales that mortal administrators cannot. The cities '
                'on Sovrath are the oldest and grandest in the cluster -- architectural '
                'programmes begun by kings who died and were restored and continued their '
                'projects across lifetimes. The result is urban landscapes of extraordinary '
                'coherence: buildings designed by the same mind over centuries, districts '
                'that evolved according to a single vision that was never interrupted by '
                'death or succession. The effect is beautiful and deeply unsettling, '
                'because it is the product of a continuity that human civilisation is not '
                'supposed to have.\n\n'
                'Ten billion people live on Sovrath. The hierarchy is steeper here than '
                'anywhere else in the cluster. The Emperor of Adhara has been restored so '
                'many times that the records of the earliest restorations are historical '
                'documents rather than medical files. The planetary kings who serve the '
                'Emperor are themselves centuries old. The aristocracy beneath them -- the '
                'wealthy who can afford quality reanimation -- forms a permanent upper '
                'class that never turns over because its members never permanently die. '
                'Beneath them, the living population works, ages, and dies once. Beneath '
                'the living, the shells.\n\n'
                'The shells on Sovrath are more numerous than on Vethane and more carefully '
                'hidden. The de facto capital maintains the most rigorous separation between '
                'the living and the reanimated labour force -- the shells work in the deep '
                'infrastructure, in sealed sections of the transit network, in the '
                'industrial zones that the residential and commercial districts are '
                'designed never to see. The image Sovrath projects is civilisation perfected '
                'by immortality. The labour that sustains the image is buried.'
            ),
            population=10_000_000_000,
        ),
        StellarObject(
            name='Thalien',
            short_description='The system\'s industrial heart -- manufacturing, processing, and the economic engine that makes Adhara the most productive system in the cluster.',
            long_description=(
                'Thalien is where Adhara\'s wealth is generated. The planet is heavily '
                'industrialised -- manufacturing, materials processing, technology '
                'production, and the high-value industries that the cluster\'s economy '
                'depends on. The output is vast. Adhara\'s economic dominance in the cluster '
                'is built on Thalien\'s productivity, and Thalien\'s productivity is built '
                'on a workforce that is part living, part shell, and organised with the '
                'ruthless efficiency of a system that has been optimised over centuries by '
                'rulers who never leave.\n\n'
                'The living workforce on Thalien handles the skilled and technical work -- '
                'the engineering, the precision manufacturing, the management of the '
                'industrial operations. The shells handle everything else: the heavy '
                'lifting, the toxic processing, the work in environments that would injure '
                'or kill living workers. The factories on Thalien run continuously because '
                'the shell workforce does not need rest, does not need breaks, and does '
                'not object to conditions that would be illegal for living workers in any '
                'civilisation, including this one. The legal framework on Thalien '
                'distinguishes between labour laws that apply to the living and the '
                'separate, considerably thinner, regulations that govern the use of '
                'reanimated labour.\n\n'
                'The planetary king of Thalien is the Emperor of Adhara\'s most important '
                'vassal -- the ruler whose industrial output funds the Emperor\'s court, '
                'the military, and the cluster-wide influence that makes Adhara the de '
                'facto capital. The relationship is feudal in character: the king provides '
                'revenue and the Emperor provides protection and political patronage. The '
                'arrangement has functioned for centuries because neither party dies long '
                'enough for the relationship to be disrupted by succession.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='Korrath',
            short_description='A warm, populous world -- the system\'s residential overflow, where the living middle class raises families in cities that were planned centuries ago.',
            long_description=(
                'Korrath is the system\'s third major world -- warmer than Sovrath, more '
                'residential than Thalien, and home to the bulk of the system\'s living '
                'middle class. The population works in the service sector, education, '
                'healthcare, and the administrative apparatus that a system of twenty-eight '
                'billion people requires. Korrath is where the living live -- the world '
                'where families are raised, children attend schools, and the population '
                'experiences something that resembles a normal life beneath the rule of '
                'kings and an emperor who have watched generations pass from above.\n\n'
                'The cities on Korrath were planned by kings who knew they would see the '
                'plans completed. The urban design reflects centuries of continuous vision '
                '-- parks that were planted as saplings by a king who intended to walk '
                'beneath them as mature trees, transit systems designed for a population '
                'that would not arrive for a hundred years, infrastructure built to '
                'standards that assumed the builders would be alive to maintain them '
                'indefinitely. The result is cities that are extraordinarily well-designed '
                'and faintly oppressive in their perfection -- the work of minds that did '
                'not need to compromise with the urgency that mortality imposes.\n\n'
                'The shells on Korrath are present but less visible than on the industrial '
                'worlds. The residential districts are maintained by living workers during '
                'the day. The shells handle the night maintenance -- the cleaning, the '
                'repairs, the waste processing. The children of Korrath grow up in cities '
                'that are spotless every morning without understanding who cleaned them.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Dressal',
            short_description='A cold outer world -- mining operations that supply Thalien\'s factories with raw materials, worked by the living and the dead in roughly equal proportion.',
            long_description=(
                'Dressal is the system\'s mining world -- a cold, rocky planet with mineral '
                'deposits that supply Thalien\'s factories. The extraction is intensive, '
                'conducted in deep mines and open-cast operations that the system has '
                'maintained for centuries. The workforce is roughly half living miners and '
                'half shells, working side by side in conditions that make the distinction '
                'between them uncomfortably clear.\n\n'
                'The living miners on Dressal work the skilled positions -- operating '
                'extraction equipment, managing the logistics, handling the decisions that '
                'require judgment. The shells do the physical labour: hauling rock, '
                'clearing debris, working in the sections of the mines that are too '
                'unstable or too toxic for living workers. The mine collapses that occur -- '
                'they occur regularly in deep extraction operations -- are triaged by the '
                'same calculus that governs the rest of the cluster: living miners are '
                'rescued first. Shells are recovered if practical and written off if not. '
                'The living miners have learned to work beside the shells without seeing '
                'them as people, because the alternative is seeing people die in the mines '
                'and not be rescued, and that is harder to live with than the comfortable '
                'fiction that the shells are not people at all.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Imperium Station',
            short_description='The system\'s primary orbital port -- the largest commercial installation in the cluster, processing the trade that makes Adhara the economic centre.',
            long_description=(
                'Imperium Station is the largest orbital installation in the Canopus '
                'cluster -- a massive commercial port above Sovrath that processes the '
                'trade volume generated by the cluster\'s most productive system. The '
                'station handles interstellar freight, passenger traffic, the diplomatic '
                'traffic that the de facto capital generates, and the private vessels of '
                'the Canopan elite who visit Sovrath\'s courts on business that is '
                'conducted in person because the emperors and kings prefer it that way.\n\n'
                'The station is grand in the way that the Emperor of Adhara\'s court is '
                'grand -- deliberately, expensively, as a projection of power that is '
                'intended to be noticed. The commercial districts cater to the wealthy. '
                'The diplomatic facilities rival Coronet Station on Canopus. The docking '
                'capacity exceeds any other installation in the cluster. The shells that '
                'run the freight operations are, as everywhere, out of sight -- but the '
                'volume of goods they move is visible in the constant stream of cargo '
                'containers that flows through the station\'s industrial bays at all hours.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Oberath',
            short_description='A massive gas giant -- fuel processing at a scale matching the system\'s enormous traffic, its moons host military reserves and strategic stockpiles.',
            long_description=(
                'Oberath is the system\'s gas giant -- a massive body whose moons host '
                'fuel processing operations sized for Adhara\'s enormous traffic volume. '
                'The system\'s position as the cluster\'s economic centre means a constant '
                'flow of commercial vessels, and the fuel demand is matched only by the '
                'Canopus system\'s combined military and commercial traffic.\n\n'
                'Oberath\'s outer moons also host the Emperor of Adhara\'s strategic '
                'reserves -- military supplies, reanimation stockpiles, and the resources '
                'that the Emperor maintains independently of the cluster\'s collective '
                'military. The reserves are the Emperor\'s insurance against the kind of '
                'future that a person who has lived for centuries learns to anticipate: '
                'changes in the council\'s balance, shifts in the cluster\'s politics, the '
                'possibility that the other emperors might one day decide that Adhara\'s '
                'dominance is a threat. The reserves are not secret. Their existence is a '
                'statement that the Emperor of Adhara is prepared for contingencies that '
                'the other emperors would prefer not to think about.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Brillan',
            short_description='A hot inner world -- energy collection under the intense blue-white star, powering the system\'s industry, maintained entirely by shells.',
            long_description=(
                'Brillan is a hot, dense world close to Adhara\'s brilliant blue-white '
                'star -- solar collection arrays harvesting the star\'s 22,000 times Sol '
                'luminosity to power the system\'s vast industrial operations. The radiation '
                'environment is extreme. The maintenance of the arrays is performed entirely '
                'by shells -- the radiation degrades them, but shells are replaced from the '
                'supply and the supply is constant. No living worker has set foot on '
                'Brillan\'s surface in decades. The planet is a workplace staffed entirely '
                'by the dead, producing the energy that sustains the living, under a star '
                'so bright that the light would blind an unprotected human eye within '
                'seconds.'
            ),
            population=0,
        ),
    ],
    short_description='The de facto capital of the Canopus cluster -- twenty-eight billion people in the oldest, richest, and most powerful system the Undying have built.',
    long_description=(
        'Adhara is where the real power of the Canopus cluster resides. Vethane on '
        'Canopus hosts the council chamber and the ceremonies. Sovrath on Adhara hosts '
        'the Emperor whose preferences the council ratifies. The distinction is '
        'understood by everyone in the cluster and acknowledged by nobody, because the '
        'protocol of the council requires the fiction of equals and the Emperor of '
        'Adhara permits the fiction because it costs nothing and the reality is '
        'undisturbed.\n\n'
        'Twenty-eight billion people live in a system that has been developed '
        'continuously for centuries by rulers who do not die. The cities on Sovrath '
        'were designed by the same minds across lifetimes -- architectural programmes '
        'of extraordinary coherence, urban landscapes that reflect a continuity human '
        'civilisation is not supposed to have. Thalien\'s factories produce the '
        'economic output that makes Adhara dominant -- manufacturing, processing, and '
        'technology production powered by a workforce that is part living, part shell, '
        'and governed by labour laws that distinguish sharply between the two. Korrath '
        'houses the living middle class in cities planned centuries in advance by kings '
        'who knew they would see the plans completed. Dressal mines the raw materials '
        'that feed the factories.\n\n'
        'The hierarchy is the steepest in the cluster. The Emperor has been restored '
        'so many times that the earliest records are historical documents. The kings '
        'are centuries old. The aristocracy -- those who can afford quality reanimation '
        '-- forms a permanent upper class that never turns over. Beneath them, the '
        'living work and age and die once. Beneath the living, the shells sustain '
        'everything: the factories, the mines, the infrastructure, the energy '
        'collection on Brillan where no living worker has set foot in decades. The '
        'shells are hidden on the capital worlds and visible on the industrial ones '
        'and everywhere the foundation on which the civilisation stands.\n\n'
        'The Emperor of Adhara maintains strategic reserves on Oberath\'s moons -- '
        'insurance against futures that a centuries-old mind has learned to anticipate. '
        'The reserves are not secret. Their existence is a statement. The Emperor has '
        'outlived every challenge, every rival, every shift in the cluster\'s politics, '
        'and intends to outlive whatever comes next. This is the advantage of '
        'immortality: patience is not a virtue when you have all the time in the '
        'world. It is a strategy.'
    ),
    cluster=StarClusters.CANOPUS,
)

PLACIDUS = System(
    name='Placidus',
    star='White main sequence (A2V), approximately 40 times Sol luminosity',
    population=12_000_000_000,
    distance_to_sol=340.0,
    stellar_objects=[
        StellarObject(
            name='Verantis',
            short_description='The reanimation capital -- where the technology that defines Canopan civilisation is researched, refined, and performed at every quality level from exquisite to obscene.',
            long_description=(
                'Verantis is the centre of the reanimation industry and the most important '
                'world in the cluster after Sovrath. The technology that makes the Canopan '
                'civilisation possible -- the ability to bring the dead back -- is researched, '
                'developed, and performed here at a scale and sophistication unmatched '
                'anywhere else. The finest reanimation facilities in the galaxy are on '
                'Verantis: suites where the emperors and kings come to be restored, where the '
                'process is conducted with a precision and care that produces results nearly '
                'indistinguishable from the original person. Nearly. The faint uncanny quality '
                'that even the best restoration cannot eliminate is smaller here than anywhere '
                'else, and the researchers work constantly to close the gap.\n\n'
                'The facilities descend in quality with the price. Below the imperial suites '
                'are the aristocratic clinics -- excellent work, minor imperfections that only '
                'an expert would notice. Below those, the professional-grade facilities that '
                'serve the wealthy middle class -- good restorations with visible tells, a '
                'stiffness in the movement, a flatness in the voice that the restored learn to '
                'mask. Below those, the military-grade facilities that bring dead soldiers back '
                'to operational status. Below those, the industrial facilities that produce '
                'shells -- the cheapest, crudest reanimations, bodies restored to basic motor '
                'function without cognition, without personality, without anything that the '
                'original person would recognise as themselves. The shells are produced in '
                'volume. The volume is the point.\n\n'
                'The Emperor of Placidus is the custodian of the technology that every other '
                'emperor depends on for their immortality. This gives the Emperor of Placidus '
                'a unique position in the council -- not the wealthiest, not the most '
                'powerful in conventional terms, but the one that nobody can afford to '
                'antagonise. The reanimation facilities on Verantis are the reason every '
                'emperor is alive. The Emperor of Placidus does not need to threaten. The '
                'implication is sufficient.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Tesshelan',
            short_description='The research world -- where the next generation of reanimation technology is developed by the best minds the cluster can produce or buy.',
            long_description=(
                'Tesshelan is the cluster\'s reanimation research centre -- the world where '
                'the fundamental science of bringing the dead back is advanced. The research '
                'institutions are the best-funded in the outer systems, drawing talent from '
                'across the cluster and, quietly, from the inner systems -- MERIT-trained '
                'medical researchers who have defected for the opportunity to work on problems '
                'that MERIT\'s ethics prohibit.\n\n'
                'The research spans the full spectrum. At the top end, the scientists work on '
                'closing the uncanny gap -- the subtle wrongness that even the finest '
                'restorations produce. The gap is neurological, rooted in the impossibility of '
                'perfectly reconstructing the quantum-level states of a human brain from the '
                'macro-level information that preservation captures. The researchers believe '
                'the gap can be narrowed further. Whether it can be closed entirely is the '
                'field\'s defining question. At the bottom end, the research focuses on '
                'efficiency -- producing shells faster, cheaper, and in greater volume, '
                'because the cluster\'s appetite for reanimated labour is growing and the '
                'supply must keep pace.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Morven',
            short_description='A cold world where the bodies are stored -- the cluster\'s largest preservation facility, holding millions of dead awaiting reanimation.',
            long_description=(
                'Morven is the cluster\'s cold storage. The planet is naturally cold -- thin '
                'atmosphere, frozen surface -- and the subsurface facilities that have been '
                'built into the crust house millions of preserved bodies awaiting reanimation. '
                'The dead arrive from across the cluster: the recently deceased whose families '
                'have purchased reanimation services, the military dead awaiting restoration, '
                'and the bodies that have been acquired for shell production through channels '
                'that the cluster\'s legal framework permits and its ethical framework does not '
                'examine too closely.\n\n'
                'The preservation facilities are managed with the clinical efficiency of a '
                'logistics operation -- which is what they are. Bodies are received, assessed, '
                'catalogued, and stored at temperatures that halt decay until they are '
                'scheduled for processing. The staff who manage the facilities are '
                'professionals who have learned to see the bodies as inventory rather than '
                'people, because the alternative makes the work impossible. The scale is the '
                'thing that visitors find most difficult: not one body, not ten, but millions, '
                'stored in rows in vaults that extend kilometres into the frozen rock.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Callisant',
            short_description='A temperate world -- the system\'s civilian population, living normal lives in a system whose primary industry is death and its reversal.',
            long_description=(
                'Callisant is the system\'s residential world -- temperate, well-developed, '
                'and home to the civilian population that supports the reanimation industry. '
                'The people on Callisant work in the service sector, education, agriculture, '
                'and the thousand occupations that a system of twelve billion requires beyond '
                'its primary industry. The planetary king of Callisant rules a population '
                'whose relationship with the reanimation industry is the same as any company '
                'town\'s relationship with the company: dependent, aware, and careful not to '
                'think too hard about what the company actually does.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Keraph Station',
            short_description='The system\'s orbital port -- where the bodies arrive, the technology ships out, and the business of death is conducted with commercial efficiency.',
            long_description=(
                'Keraph Station is Placidus\'s primary orbital facility -- a large station '
                'that handles the system\'s heavy traffic in reanimation-related cargo. Bodies '
                'arrive in stasis pods. Reanimation technology and compounds ship outward to '
                'facilities across the cluster. The restored depart on passenger transports, '
                'returning to lives that were interrupted by death and resumed by technology. '
                'The station processes all of it with the commercial efficiency of an industry '
                'that has had centuries to optimise its logistics.\n\n'
                'The traffic also includes the supplies for Pollux\'s black market -- the '
                'reanimation technology that is smuggled into the inner systems through '
                'the Corridor. The cluster officially condemns this trade. The Emperor of '
                'Placidus officially condemns this trade. The revenue from the trade enters '
                'the Emperor\'s treasury through intermediaries whose existence is not '
                'acknowledged. The condemnation is sincere in the way that profitable '
                'condemnations tend to be.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Therival',
            short_description='A gas giant with fuel processing -- and moons where experimental reanimation procedures too dangerous for Verantis are conducted.',
            long_description=(
                'Therival is the system\'s gas giant -- fuel processing on the inner moons, '
                'and on the outer moons, facilities where the most experimental reanimation '
                'research is conducted. The experiments that are too dangerous, too uncertain, '
                'or too ethically problematic for Verantis\'s regulated facilities are '
                'performed on Therival\'s remote installations -- procedures that push the '
                'boundaries of what reanimation can achieve, tested on subjects whose consent '
                'is a legal formality and whose outcomes are not always reported in the '
                'official research literature. The Emperor of Placidus is aware of Therival\'s '
                'outer-moon facilities. The Emperor does not visit them.'
            ),
            population=150_000_000,
        ),
    ],
    short_description='The reanimation capital -- where the technology that makes emperors immortal and the dead into labour is researched, performed, and shipped across the cluster.',
    long_description=(
        'Placidus is where death is reversed. The system is the Canopus cluster\'s '
        'reanimation centre -- the world where the technology is researched, the '
        'facilities where it is performed, and the cold storage where millions of '
        'bodies await their turn. The quality spectrum runs from the imperial suites '
        'on Verantis where emperors are restored with near-perfect fidelity to the '
        'industrial facilities that produce shells in volume -- the crude reanimations '
        'that provide the cluster\'s labour force.\n\n'
        'Twelve billion people live in a system whose primary industry is the reversal '
        'of death. The research on Tesshelan pushes the technology forward -- narrowing '
        'the uncanny gap at the top end, improving efficiency at the bottom. The '
        'preservation vaults on Morven hold millions of dead in frozen storage. The '
        'Emperor of Placidus holds a unique position in the council: the custodian of '
        'the technology that every other emperor depends on for immortality. The '
        'Emperor does not need to threaten. The implication is sufficient.\n\n'
        'The trade in reanimation technology -- including the supplies that feed '
        'Pollux\'s black market in the inner systems -- flows through Keraph Station '
        'with the commercial efficiency of an industry that has been optimised over '
        'centuries. The cluster officially condemns the smuggling. The revenue enters '
        'the treasury anyway. On Therival\'s outer moons, experiments too dangerous '
        'for the regulated facilities push the boundaries of what the technology can '
        'achieve, tested on subjects whose consent is a formality. Placidus is where '
        'the Canopan miracle is manufactured, and manufacturing has never been a '
        'clean business.'
    ),
    cluster=StarClusters.CANOPUS,
)

PHAET = System(
    name='Phaet',
    star='Orange giant (K2III), approximately 60 times Sol luminosity -- a dim, warm star casting amber light that does not flatter what it illuminates',
    population=12_000_000_000,
    distance_to_sol=380.0,
    stellar_objects=[
        StellarObject(
            name='Morriden',
            short_description='The system\'s most populous world -- where the shell population outnumbers the living and the distinction between the two is harder to maintain than the cluster pretends.',
            long_description=(
                'Morriden is where the Canopus cluster\'s labour model is most visible and '
                'least deniable. The planet is heavily industrialised, densely populated, '
                'and home to a shell population that outnumbers the living by a ratio that '
                'the census does not officially record because recording it would require '
                'acknowledging it. The estimates -- compiled by researchers on Revane who '
                'study the demographics of reanimated labour -- suggest that for every '
                'living person on Morriden, there are between three and five shells.\n\n'
                'The shells on Morriden are not hidden. This is what makes the system '
                'uncomfortable even for Canopans who have grown up in a civilisation built '
                'on reanimated labour. On Sovrath and Vethane, the shells work underground, '
                'at night, in sealed sections. On Morriden, the shell population is too '
                'large to conceal. The streets have shells on them during the day. The '
                'factories have shells working alongside the living on the same floor. The '
                'transit systems carry shells to their work assignments in the same '
                'vehicles -- separated into designated sections, but visible through the '
                'partition. The living residents of Morriden walk past shells every day, '
                'and the shells walk past them with the slow, purposeful gait that '
                'characterises low-quality reanimation -- not quite right, not quite '
                'coordinated, recognisably human and recognisably not.\n\n'
                'The living population on Morriden has adapted to the visibility in ways '
                'that visitors find disturbing. The residents do not look at the shells. '
                'Not in the way that people avoid looking at something unpleasant -- in the '
                'way that people do not look at furniture. The shells are background. They '
                'are infrastructure. The living have learned to perceive them as objects '
                'rather than as the remains of people, and the learning is so complete that '
                'a visitor who stares at a shell is stared at in turn by the living, who '
                'find the attention given to a shell more disturbing than the shell '
                'itself.\n\n'
                'The Emperor of Phaet rules a system that the rest of the cluster considers '
                'distasteful but cannot do without. Morriden\'s industrial output depends on '
                'the shell workforce, and the shell workforce is supplied from across the '
                'cluster -- the bodies of the poor who could not afford quality reanimation '
                'and whose remains were purchased by the labour corporations that supply '
                'Phaet\'s factories. The Emperor\'s wealth comes from the shells. The '
                'Emperor\'s political position at the council is weakened by the shells. The '
                'other emperors need Phaet\'s output and prefer not to acknowledge how it '
                'is produced.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Kethra',
            short_description='The system\'s shell processing world -- where the bodies arrive, are reanimated to the minimum functional standard, and are shipped to their work assignments.',
            long_description=(
                'Kethra is where the shells are made. The planet hosts the cluster\'s '
                'largest shell production facilities -- industrial-scale reanimation '
                'operations that process incoming bodies and produce functional shells at a '
                'rate that matches Phaet\'s industrial demand. The work is the crude inverse '
                'of what happens on Revane: where Revane\'s practitioners spend weeks '
                'restoring a single client to the highest possible quality, Kethra\'s '
                'technicians process hundreds of bodies per shift to the lowest standard '
                'that produces a working unit.\n\n'
                'The incoming bodies arrive from across the cluster -- purchased from the '
                'families of the dead, acquired from institutional sources, and supplied '
                'through channels that the labour corporations describe as procurement and '
                'that critics describe as grave-robbing with paperwork. The bodies are '
                'assessed for physical condition, processed through the reanimation '
                'procedure -- which at this quality level takes hours rather than weeks -- '
                'and tested for basic motor function. A shell that can walk, lift, and '
                'follow simple instructions is functional. A shell that cannot is recycled '
                'for biological material. The pass rate is approximately seventy percent. '
                'The thirty percent that fail are not discussed in the same terms.\n\n'
                'The living workers on Kethra are the cluster\'s most morally exhausted '
                'professionals. The technicians who perform the shell reanimations are '
                'trained at the same academies on Tessavin that produce the practitioners '
                'who restore emperors -- they learned the same techniques, studied the '
                'same science, and ended up here rather than on Revane because their '
                'grades were not good enough or their connections were not strong enough. '
                'They perform the work with the mechanical efficiency of people who cannot '
                'afford to think about what they are doing to the bodies on the table.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Dravven',
            short_description='An industrial world where the shell labour force is deployed at its densest -- factories staffed almost entirely by the reanimated, supervised by skeleton living crews.',
            long_description=(
                'Dravven is the system\'s heaviest industrial world -- manufacturing, '
                'processing, and production operations staffed almost entirely by shells '
                'under the supervision of small living crews. The factories on Dravven '
                'operate continuously. The shells do not need light, so the factories are '
                'dark. The shells do not need heating, so the factories are cold. The shells '
                'do not need rest, so the factories never stop. The living supervisors '
                'work from enclosed control rooms with windows that look out onto factory '
                'floors where hundreds of shells move through the dark, performing their '
                'assigned tasks with the repetitive precision that simple reanimation '
                'produces.\n\n'
                'The living supervisors on Dravven are the system\'s most psychologically '
                'stressed population. The work is not physically dangerous -- the control '
                'rooms are safe and comfortable. The stress is existential. The supervisors '
                'spend their shifts watching the dead work. The factories are silent except '
                'for the machinery, because the shells do not speak, do not communicate, '
                'do not acknowledge each other or their supervisors. The only human sounds '
                'on the factory floor are the occasional thud of a shell that has ceased '
                'functioning and fallen, and the mechanical sounds of the retrieval system '
                'that removes the failed unit and delivers a replacement from storage.\n\n'
                'The turnover rate for living supervisors on Dravven is the highest in the '
                'cluster. The pay is excellent. The shifts are short. The psychological '
                'support is available. The supervisors still leave, because the experience '
                'of watching the dead work in the dark is something that the human mind is '
                'not designed to process for extended periods, and no amount of pay makes '
                'the processing easier.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Embark Station',
            short_description='The system\'s orbital port -- where the body shipments arrive and the industrial output departs, and where visitors first encounter the shell presence they were warned about.',
            long_description=(
                'Embark Station is Phaet\'s primary orbital facility -- a large, functional '
                'station that handles the system\'s heavy industrial traffic and the '
                'distinctive cargo that defines Phaet\'s economy: bodies in, manufactured '
                'goods out. The incoming shipments of cadavers destined for Kethra\'s '
                'processing facilities are the station\'s most visible traffic -- large '
                'transports carrying hundreds or thousands of bodies in preservation '
                'containers, docking at dedicated bays that the commercial district is '
                'designed to be far from but that the station\'s layout cannot entirely '
                'conceal.\n\n'
                'Embark Station is where visitors from other Canopan systems first '
                'encounter Phaet\'s shell visibility. The station uses shell labour for '
                'cargo handling, maintenance, and cleaning -- standard across the cluster '
                '-- but does not restrict the shells to night shifts or sealed sections. '
                'The shells are present during the day, moving through the corridors, '
                'performing their tasks in view of the living. Visitors from Sovrath or '
                'Vethane, where the shells are carefully hidden, find the experience '
                'jarring. Visitors from the inner systems find it horrifying. The station '
                'staff, who are from Phaet, do not understand the reaction. The shells '
                'are working. What is there to see?'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Grennis',
            short_description='An agricultural world feeding twelve billion -- farmed by shells under the amber light, producing food that the living population tries not to think too hard about.',
            long_description=(
                'Grennis is the system\'s agricultural world -- warm, fertile under the '
                'orange giant\'s amber light, and farmed primarily by shells. The '
                'agricultural operations are large-scale and efficient in the way that '
                'reanimated labour enables: the shells work the fields continuously, do '
                'not require the housing and amenities that living workers demand, and '
                'are replaced when they wear out with a logistical simplicity that living '
                'workforce management cannot match.\n\n'
                'The food produced on Grennis feeds the system\'s twelve billion people. '
                'The living population eats the food that the dead grew, harvested, and '
                'processed. This is true across the cluster -- Verdath on Canopus uses '
                'shell labour in its fields as well -- but on Grennis the scale makes '
                'the fact harder to set aside. The agricultural workforce is almost '
                'entirely shells. The food was touched, at every stage of production, by '
                'hands that belong to bodies that were once people and are now tools. The '
                'living population of Phaet eats without comment because commenting would '
                'require acknowledging what they have learned not to see.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Morben',
            short_description='A gas giant with fuel processing -- the one operation in the system where shells are not used, because fuel processing requires judgment that dead minds do not have.',
            long_description=(
                'Morben is the system\'s gas giant -- fuel processing on its moons '
                'supporting Phaet\'s heavy industrial traffic. The fuel operations are '
                'staffed entirely by living workers -- one of the few operations in the '
                'system where shells are not deployed. The reason is technical rather than '
                'moral: fuel processing requires real-time judgment, the ability to respond '
                'to pressure fluctuations and chemical variations that shells cannot '
                'assess. A shell that makes the wrong decision in a fuel refinery produces '
                'an explosion. The labour corporations have calculated the cost of '
                'explosions versus the cost of living workers and concluded that living '
                'workers are cheaper.\n\n'
                'The fuel workers on Morben\'s moons are the system\'s most relieved '
                'employees. Their work is standard fuel processing -- the same job that '
                'fuel workers perform across the galaxy. The relief is in what their work '
                'is not: they do not work beside shells, they do not supervise the dead, '
                'and they do not have to maintain the studied blindness that the rest of '
                'Phaet\'s living population has cultivated. The fuel workers see dead '
                'people only when they return to the inhabited worlds for leave, and the '
                'shock of re-encountering the shell presence after weeks of normality is '
                'something they describe to each other and to nobody else.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Cold Storage',
            short_description='A cold outer world used as shell storage -- hundreds of millions of reanimated bodies in standby, warehoused in the dark until they are needed.',
            long_description=(
                'Cold Storage is a cold, airless body in the outer system that the labour '
                'corporations have converted into the cluster\'s largest shell storage '
                'facility. The surface installations are vast, windowless warehouses carved '
                'into the rock, maintained at temperatures that preserve the reanimated '
                'tissue without the environmental costs of heating. Inside, the shells '
                'stand in rows -- hundreds of millions of them, powered down to standby '
                'mode, motionless in the dark, waiting to be activated and shipped to their '
                'assignments.\n\n'
                'Cold Storage exists because Phaet\'s industrial demand fluctuates with the '
                'cluster\'s economic cycle, and the labour corporations have learned that '
                'maintaining a buffer stock is cheaper than accelerating production at '
                'Kethra when demand spikes. The shells in the Reserve are functional -- '
                'tested, catalogued, and ready for deployment. They stand in their rows in '
                'the dark and the cold and they do not experience the waiting because '
                'there is nothing left in them that experiences anything.\n\n'
                'Cold Storage is not visited. The maintenance is automated. The living staff '
                'who manage the facility do so from an orbital station and have never set '
                'foot on the surface. The few journalists who have requested access have '
                'been denied. The few who have obtained access through other means have '
                'described the experience in terms that the labour corporations contest and '
                'the public does not want to read.'
            ),
            population=0,
        ),
    ],
    short_description='The system where the shells are visible -- twelve billion people and the reanimated labour force that outnumbers them, working in the open because there are too many to hide.',
    long_description=(
        'Phaet is the Canopus cluster\'s most uncomfortable system. Every Canopan '
        'system uses reanimated labour. Every Canopan system hides the shells -- in '
        'the underground, at night, in sealed sections that the living never enter. '
        'Phaet cannot hide them. The shell population is too large. The industrial '
        'demand is too heavy. The economics of concealment do not work at this scale. '
        'The result is a system where the shells are visible -- on the streets, in the '
        'factories, on the transit systems, in the fields -- and the living population '
        'has adapted by learning not to see them.\n\n'
        'Twelve billion living people share the system with a shell population '
        'estimated at three to five times that number. Kethra processes the incoming '
        'bodies into functional shells at industrial scale -- hundreds per shift, '
        'reanimated to the minimum standard that produces a working unit. Dravven\'s '
        'factories run in the dark, staffed almost entirely by shells, supervised by '
        'living crews from enclosed control rooms. Cold Storage stores hundreds of '
        'millions of shells in standby, warehoused in rows in the cold, waiting for '
        'activation.\n\n'
        'The Emperor of Phaet rules a system that the rest of the cluster considers '
        'distasteful. The other emperors need Phaet\'s industrial output and prefer '
        'not to acknowledge how it is produced. The Emperor\'s wealth comes from the '
        'shells. The Emperor\'s political position is weakened by the shells. The '
        'visitors who arrive at Embark Station and encounter the shell presence for '
        'the first time are warned in advance, and the warning does not help, because '
        'nothing prepares a person for a world where the dead walk beside the living '
        'and the living have learned that the appropriate response is to look through '
        'them the way you look through furniture.\n\n'
        'Phaet is honest in a way that the rest of the cluster is not. Every system '
        'in the Canopus cluster is built on reanimated labour. Phaet is the one that '
        'does not pretend otherwise. The other emperors find this distasteful. The '
        'Emperor of Phaet finds their distaste hypocritical. Both positions have '
        'merit. Neither is comfortable.'
    ),
    cluster=StarClusters.CANOPUS,
)

ALSEPHINA = System(
    name='Alsephina',
    star='Blue-white main sequence (A2V), approximately 25 times Sol luminosity -- bright, steady light over fields that produce the cluster\'s food supply',
    population=10_000_000_000,
    distance_to_sol=410.0,
    stellar_objects=[
        StellarObject(
            name='Harvane',
            short_description='The cluster\'s breadbasket -- six billion people overseeing agricultural operations where the shells plant the crops, tend the livestock, and eventually become part of the supply chain they serve.',
            long_description=(
                'Harvane is the Canopus cluster\'s primary agricultural world -- a warm, '
                'fertile planet with deep soil, reliable climate, and growing conditions '
                'that produce enormous yields. The farming is conducted almost entirely by '
                'shells. The manual labour of agriculture -- planting, tending, harvesting, '
                'the physical work that requires hands and endurance but not thought -- is '
                'performed by reanimated workers who toil in the fields under the bright '
                'blue-white light from dawn to dusk and beyond, because shells do not '
                'register fatigue and do not stop when the sun sets.\n\n'
                'The work is dangerous. Agricultural operations at this scale involve '
                'heavy machinery -- harvesters, ploughs, transport vehicles, processing '
                'equipment -- and the shells that operate alongside this machinery lack '
                'the reflexes and spatial awareness to avoid it consistently. Shells are '
                'struck by equipment, caught in mechanisms, crushed beneath vehicles. The '
                'livestock operations are worse: the animals are large, agitated by the '
                'proximity of things that move like people but do not smell like people '
                'and do not react like people, and the shells that tend the herds sustain '
                'injuries from kicks, charges, and trampling at rates that would shut down '
                'any operation using living workers.\n\n'
                'The shells accumulate damage. A shell that loses a limb to a harvester '
                'continues working with the remaining limbs until the loss makes it '
                'non-functional. A shell that is trampled by livestock continues if it can '
                'still stand. The damage is not repaired -- repair costs more than '
                'replacement, and the supply from Kethra is constant. When a shell\'s '
                'accumulated damage renders it unable to perform its assigned tasks, it is '
                'withdrawn from the workforce and sent to the processing facilities.\n\n'
                'The processing facilities are the part that the rest of the cluster '
                'prefers not to know about. The shells that can no longer work are not '
                'decommissioned and disposed of. They are recycled. The reanimated tissue '
                'is broken down and processed into protein supplements, animal feed, and '
                'the organic fertilisers that are spread on the same fields the shell '
                'worked before it was withdrawn. The cycle is closed: the shell works the '
                'field, is damaged by the field, and is returned to the field as material '
                'that feeds the next crop. The living population of Harvane knows this in '
                'the abstract way that people know unpleasant facts about systems they '
                'depend on. The specifics are not advertised. The food is eaten without '
                'inquiry because the inquiry leads to answers that make the food harder '
                'to eat.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Gelden',
            short_description='The system\'s second agricultural world -- cooler, specialising in grain and staple crops, where the shell recycling is the same but the livestock damage is less.',
            long_description=(
                'Gelden is the system\'s second agricultural world -- cooler than Harvane, '
                'with broad plains that support the grain and staple crops that form the '
                'caloric foundation of the cluster\'s diet. The farming follows the same '
                'model as Harvane: shells perform the manual labour, living workers manage '
                'the operations, and the shells that are damaged beyond function are '
                'recycled into the agricultural supply chain.\n\n'
                'Gelden\'s operations are less dangerous than Harvane\'s. The grain farming '
                'involves heavy machinery but not livestock, and the shell attrition rate '
                'is lower. The shells last longer on Gelden\'s plains -- the work is less '
                'physically destructive, and a shell assigned to grain farming may function '
                'for years before accumulated wear renders it non-functional. The recycling '
                'when it comes is the same: the worn-out shells are processed into '
                'fertiliser and feed. The cycle is the same. The timescale is longer. The '
                'moral calculus is identical.\n\n'
                'The living population on Gelden is smaller than Harvane\'s and more '
                'rural -- farming communities spread across the plains, managing the shell '
                'workforce from homesteads and regional control centres. The culture is '
                'agricultural in the quiet, practical way of grain-farming communities '
                'everywhere, with the addition that the workers in the fields are dead '
                'and the community has decided that this is normal.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Treven',
            short_description='An ocean world -- aquaculture operations producing the protein that supplements the grain and produce, with shells working the sea farms in conditions that would drown living workers.',
            long_description=(
                'Treven is a warm ocean world -- shallow seas covering most of the surface, '
                'with extensive aquaculture operations producing the marine protein that '
                'supplements the cluster\'s diet. The sea farms are worked by shells -- '
                'reanimated workers who operate in and under the water in conditions that '
                'would be dangerous for living workers. The shells do not need to breathe. '
                'They work submerged for hours, tending the fish stocks, maintaining the '
                'enclosures, harvesting the kelp and shellfish that the sea farms produce.\n\n'
                'The aquaculture shells degrade faster than the agricultural shells on '
                'Harvane and Gelden. The saltwater corrodes the reanimated tissue, the '
                'marine organisms foul the shell\'s remaining biological surfaces, and the '
                'constant immersion accelerates the decay that all shells eventually '
                'undergo. A shell assigned to Treven\'s sea farms functions for months '
                'rather than years. The replacement rate is high. The recycling follows '
                'the same pattern -- the shells that cease functioning in the water are '
                'retrieved, processed, and returned to the food chain as marine feed and '
                'fertiliser for the kelp beds.\n\n'
                'The living population on Treven is small -- island communities and '
                'floating platform settlements managing the aquaculture operations. The '
                'workers monitor the shell crews from the surface, tracking the submerged '
                'workers on sonar displays that show the shells as dots moving through the '
                'water. When a dot stops moving, a retrieval team is dispatched. The '
                'retrieval teams describe their work in technical terms that carefully '
                'avoid acknowledging what they are retrieving.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Reclaim Station',
            short_description='The system\'s orbital processing hub -- where the agricultural output is packaged for export and the shell recycling byproducts enter the supply chain.',
            long_description=(
                'Reclaim Station is Alsephina\'s primary orbital facility -- a large '
                'processing station that handles the export of the system\'s agricultural '
                'output to the rest of the cluster. The station processes, packages, and '
                'ships the food that feeds tens of billions of Canopan citizens -- grain '
                'from Gelden, produce and livestock from Harvane, marine protein from '
                'Treven.\n\n'
                'The station also processes the shell recycling byproducts that enter the '
                'agricultural supply chain. The protein supplements derived from recycled '
                'shell tissue, the organic fertilisers produced from processed remains, '
                'and the animal feed that incorporates shell-derived nutrients are all '
                'handled through Reclaim Station\'s industrial bays. The byproducts are '
                'not labelled as shell-derived in the export manifests. They are listed '
                'under categories that are technically accurate -- organic protein '
                'supplement, biological fertiliser, processed nutrient compound -- and '
                'that do not invite the question of what organism the organic material '
                'came from. The labelling is legal. The omission is deliberate. The '
                'consumers who eat the food do not ask because the system has been '
                'designed to ensure they do not think to ask.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Hollund',
            short_description='A gas giant with fuel processing -- supporting the freighter traffic that carries the cluster\'s food supply.',
            long_description=(
                'Hollund is the system\'s gas giant -- fuel processing on its moons '
                'supporting the freighter traffic that moves Alsephina\'s agricultural '
                'output to the rest of the cluster. The traffic is heavy and continuous -- '
                'the cluster\'s population depends on Alsephina\'s output, and the '
                'freighters that carry it run on schedules that do not accommodate delays. '
                'The fuel workers are living -- the same technical requirement as Phaet\'s '
                'Morben -- and they process the fuel with the steady efficiency of people '
                'who understand that a disruption in fuel means a disruption in food means '
                'a disruption in everything.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Kessane',
            short_description='A hot inner world -- energy collection for the system, maintained by shells whose degradation under the radiation is faster than the agricultural shells but slower than Treven\'s.',
            long_description=(
                'Kessane is a hot inner world with solar collection arrays powering the '
                'system\'s agricultural infrastructure -- the irrigation systems, the '
                'climate management on Harvane, the processing facilities on Reclaim '
                'Station. The arrays are maintained by shells. The radiation environment '
                'degrades them faster than agricultural work but slower than Treven\'s '
                'saltwater. The shells on Kessane function for approximately a year before '
                'the radiation renders them non-functional. They are retrieved and recycled '
                'through the same processing facilities as the agricultural shells. The '
                'cycle applies everywhere in Alsephina. Nothing is wasted. The system is '
                'efficient in a way that efficiency should not be.'
            ),
            population=5_000_000,
        ),
    ],
    short_description='The cluster\'s breadbasket -- where the shells grow the food, are damaged by the work, and are recycled into the food chain when they can no longer function.',
    long_description=(
        'Alsephina feeds the Canopus cluster. Ten billion people oversee the '
        'agricultural operations that produce the food for tens of billions across '
        'Canopan space -- grain from Gelden\'s plains, produce and livestock from '
        'Harvane\'s fertile fields, marine protein from Treven\'s shallow seas. The '
        'work is performed almost entirely by shells. The manual labour of agriculture '
        '-- planting, tending, harvesting, the physical work that requires hands and '
        'endurance but not thought -- is done by the reanimated.\n\n'
        'The work is dangerous. Shells are struck by heavy machinery, trampled by '
        'livestock that is agitated by their presence, corroded by saltwater in the '
        'sea farms. They accumulate damage until they can no longer function. A shell '
        'that loses a limb continues with the remaining limbs. A shell that is '
        'trampled continues if it can stand. When the damage is too great, the shell '
        'is withdrawn and sent to the processing facilities.\n\n'
        'The processing facilities are the part the cluster prefers not to know about. '
        'The non-functional shells are not disposed of. They are recycled -- broken '
        'down into protein supplements, animal feed, and organic fertiliser that is '
        'spread on the same fields the shell once worked. The cycle is closed. The '
        'shell works the field, is damaged by the field, and is returned to the field '
        'as material that feeds the next crop. The byproducts are not labelled as '
        'shell-derived in the export manifests. The categories are technically '
        'accurate. The consumers do not ask because the system is designed to ensure '
        'they do not think to ask.\n\n'
        'The Emperor of Alsephina rules a system that is essential and unpleasant in '
        'equal measure. The cluster cannot function without Alsephina\'s output. The '
        'cluster does not want to know how the output is produced. The Emperor '
        'supplies the food and does not burden the council with the details, and the '
        'other emperors eat what Alsephina provides and do not inquire into the '
        'ingredients. The arrangement is comfortable for everyone except the shells, '
        'who are not capable of comfort and are not consulted.'
    ),
    cluster=StarClusters.CANOPUS,
)

MIRZAM = System(
    name='Mirzam',
    star='Blue giant (B1II-III), approximately 26,000 times Sol luminosity -- a pulsating variable star whose brightness fluctuates on a six-hour cycle, giving the system a slow, rhythmic pulse of light',
    population=14_000_000_000,
    distance_to_sol=500.0,
    stellar_objects=[
        StellarObject(
            name='Karveth',
            short_description='The cluster\'s commercial capital -- seven billion people in a trading civilisation where everything is for sale, including the things that other systems pretend are not.',
            long_description=(
                'Karveth is the commercial heart of the Canopus cluster -- the world where '
                'the cluster\'s internal trade is brokered, where the inter-faction trade is '
                'negotiated, and where the grey-market commerce that no other system will '
                'officially host is conducted openly. The planet is heavily urbanised, '
                'densely populated, and built around the business of buying and selling at '
                'a scale that makes it the busiest commercial centre in the outer systems.\n\n'
                'The trade on Karveth is comprehensive. The legitimate commerce -- raw '
                'materials, manufactured goods, agricultural products, technology -- flows '
                'through trading houses and exchanges that operate around the clock, their '
                'schedules synchronised to the star\'s six-hour pulsation cycle because the '
                'traders discovered decades ago that the rhythmic fluctuation in light '
                'affects human attention patterns and the trading day is structured '
                'accordingly. The grey-market commerce operates in the spaces between: '
                'reanimation technology sold to inner-system smugglers, shell labour '
                'contracts brokered between the labour corporations and systems that '
                'officially limit shell use, and the trade in cadavers that supplies '
                'Kethra\'s processing facilities and Tessavin\'s training academies.\n\n'
                'Everything on Karveth has a price. The living sell their labour. The dead '
                'are sold as material. The rights to a person\'s remains after death are '
                'traded as futures contracts -- a living person can sell their post-mortem '
                'reanimation rights today for credits they receive now, and the buyer '
                'acquires the legal right to the body when the seller dies. The practice '
                'is widespread among the poor, who need the credits, and the contracts are '
                'traded on the same exchanges as agricultural commodities and industrial '
                'metals. The moral implications are discussed in academic papers on Revane '
                'and ignored in the trading pits on Karveth, where morality is a cost that '
                'the market has not priced in.\n\n'
                'The Emperor of Mirzam is the cluster\'s wealthiest ruler -- richer than '
                'the Emperor of Adhara by some measures, though the comparison depends on '
                'whether you count political influence or liquid wealth. The Emperor of '
                'Mirzam has the credits. The Emperor of Adhara has the power. The '
                'relationship between the two is the cluster\'s most important and most '
                'carefully managed rivalry.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='Barrin',
            short_description='The system\'s logistics world -- warehousing, freight management, and the infrastructure that keeps the cluster\'s trade moving.',
            long_description=(
                'Barrin is the system\'s logistics backbone -- a temperate world whose '
                'economy is built around warehousing, freight management, and the movement '
                'of goods. Where Karveth is where the deals are made, Barrin is where the '
                'goods are stored, sorted, and shipped. The planet\'s surface is covered in '
                'distribution centres -- vast automated facilities linked by orbital '
                'elevators to the stations above, processing the physical volume of trade '
                'that Karveth\'s exchanges generate.\n\n'
                'The distribution centres are operated by shells under living management. '
                'The work -- sorting, loading, moving containers between storage bays and '
                'orbital elevators -- is physical, repetitive, and continuous. The shell '
                'workforce operates around the clock in the same pattern as Phaet\'s '
                'factories: dark warehouses, cold environments, no breaks. The throughput '
                'is enormous. The cluster\'s trade flows through Barrin, and the shells '
                'move it with the tireless efficiency that makes reanimated labour the '
                'foundation of Canopan logistics.\n\n'
                'The living population on Barrin works in management, systems '
                'coordination, and the skilled technical roles that the logistics industry '
                'requires. The culture is practical, schedule-driven, and shaped by the '
                'constant awareness that delays at Barrin ripple across the cluster. The '
                'logistics workers take their responsibilities seriously and take their '
                'vacations on other worlds, because Barrin is a place to work rather than '
                'a place to live, and the distinction matters to people who spend their '
                'days managing the dead.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Bazaar',
            short_description='The system\'s primary orbital station -- the largest trading installation in the outer systems, where the cluster\'s commerce meets the rest of the galaxy.',
            long_description=(
                'The Bazaar is Mirzam\'s primary orbital station and the largest trading '
                'installation in the outer systems. The station is enormous -- docking '
                'capacity for hundreds of vessels simultaneously, trading floors that '
                'operate continuously, and a commercial district that caters to traders '
                'from every faction in the galaxy. Canopan merchants, Antarian stim '
                'dealers, Polaran neural-tech traders, Hyadean prosthetics brokers, '
                'Pleiadian biologics specialists, and the independent operators who buy '
                'and sell across factional lines -- all of them pass through the Bazaar.\n\n'
                'The inter-faction trade is the Bazaar\'s distinctive feature. The factions '
                'are at war with MERIT and nominally hostile to each other, but trade flows '
                'regardless because commerce does not respect political boundaries. The '
                'Bazaar provides the neutral ground -- a station where factional rivalries '
                'are suspended in the trading districts and enforced in the bars afterward. '
                'The security on the Bazaar is heavy, professional, and focused on '
                'preventing the factional tensions from disrupting the commerce that is '
                'the station\'s reason for existing.\n\n'
                'The Bazaar is where the cluster\'s grey-market reanimation technology is '
                'sold to the inner systems. The smugglers who supply Pollux\'s black market '
                'purchase their materials here -- the neural reconstruction matrices, the '
                'tissue regeneration compounds, the chemical cocktails that the Canopan '
                'reanimation process requires. The sales are conducted openly in '
                'designated trading zones that the Emperor of Mirzam maintains for the '
                'purpose. The other emperors disapprove of the openness. They do not '
                'disapprove of the revenue.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Selwick',
            short_description='An agricultural world feeding the system -- unremarkable in a system whose identity is commerce, which is exactly how the farmers prefer it.',
            long_description=(
                'Selwick is the system\'s agricultural world -- temperate, productive, and '
                'overshadowed by the commercial operations that define Mirzam\'s identity. '
                'The farming follows the standard Canopan model: shells perform the manual '
                'labour, living workers manage the operations. The output feeds the '
                'system\'s fourteen billion people with a modest surplus for export.\n\n'
                'The farmers on Selwick are the system\'s least commercially minded '
                'residents, which in a system built entirely around commerce makes them '
                'unusual. They grow food. They sell it at market rates. They do not trade '
                'futures, do not speculate on cadaver contracts, and do not participate in '
                'the grey-market commerce that defines Karveth. The traders consider them '
                'unsophisticated. The farmers consider the traders parasites. Both continue '
                'to need each other.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Golvane',
            short_description='A gas giant with fuel processing at a scale matching the system\'s enormous traffic -- the busiest fuel operation in the cluster.',
            long_description=(
                'Golvane is the system\'s gas giant -- fuel processing on its moons at a '
                'scale that matches Mirzam\'s position as the cluster\'s trade hub. The '
                'traffic through Mirzam is the heaviest in the outer systems: commercial '
                'freighters, independent traders, inter-faction vessels, and the constant '
                'stream of ships that the Bazaar\'s commerce generates. The fuel demand is '
                'enormous and the processing operations run continuously to meet it.\n\n'
                'The fuel operations are mixed -- living engineers managing the systems, '
                'shells performing the physical labour of maintenance and cleaning. The '
                'fuel workers are among the system\'s least commercially oriented -- they '
                'process fuel, they do not trade it, and the speculative mentality that '
                'pervades Karveth has not reached Golvane\'s moons. The traders find this '
                'baffling. The fuel workers find the traders exhausting. The fuel is '
                'processed regardless.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Vaulthen',
            short_description='A cold, secure world -- the cluster\'s financial infrastructure, where the credits are stored, the contracts are enforced, and the Emperor\'s personal wealth is managed.',
            long_description=(
                'Vaulthen is a cold, rocky world in the outer system that hosts the '
                'cluster\'s financial infrastructure -- the banking systems, the contract '
                'enforcement mechanisms, and the credit exchanges that underpin the '
                'commerce conducted on Karveth and the Bazaar. The financial systems are '
                'hardened against interference, housed in facilities built into the rock, '
                'and managed by institutions that have operated continuously for centuries '
                'under the patronage of emperors who understand that commerce requires '
                'trust and trust requires infrastructure.\n\n'
                'The Emperor of Mirzam\'s personal wealth is managed from Vaulthen -- a '
                'fortune accumulated over centuries of trade that is stored, invested, and '
                'deployed from facilities that the Emperor controls directly. The scale of '
                'the Emperor\'s personal holdings is not publicly disclosed but is estimated '
                'by the financial analysts on Vaulthen to exceed the total economic output '
                'of several smaller systems combined. The wealth is not static -- it is '
                'actively traded, invested in enterprises across the cluster, and used as '
                'political leverage with the subtlety that centuries of practice produce. '
                'The Emperor of Mirzam does not need to make threats. The Emperor controls '
                'the financial infrastructure that everyone else\'s commerce depends on, '
                'and that control is the most effective threat available.'
            ),
            population=400_000_000,
        ),
    ],
    short_description='The cluster\'s commercial heart -- fourteen billion people in a trading civilisation where everything has a price, including the dead.',
    long_description=(
        'Mirzam is where the Canopus cluster does business. The system is the '
        'cluster\'s trade hub -- the largest commercial centre in the outer systems, '
        'processing the internal trade between Canopan worlds, the inter-faction '
        'commerce that flows despite political hostility, and the grey-market trade '
        'in reanimation technology that supplies the inner systems\' black markets. '
        'Fourteen billion people live here, and the system\'s culture is commercial '
        'to its core: everything has a price and everything is traded.\n\n'
        'The trading on Karveth is comprehensive and amoral. Legitimate goods flow '
        'through the exchanges alongside shell labour contracts, cadaver supply '
        'agreements, and the futures contracts that allow the living poor to sell '
        'their post-mortem reanimation rights today for credits they need now. The '
        'moral implications are discussed on Revane and ignored on Karveth, where '
        'morality is a cost the market has not priced in. The Bazaar -- the system\'s '
        'enormous orbital station -- hosts traders from every faction, providing '
        'neutral ground where factional rivalries are suspended in the trading '
        'districts and enforced in the bars afterward.\n\n'
        'The Emperor of Mirzam is the cluster\'s wealthiest ruler -- a fortune '
        'accumulated over centuries, managed from Vaulthen\'s hardened financial '
        'facilities, and deployed with the subtlety that immortality teaches. The '
        'Emperor\'s rivalry with the Emperor of Adhara is the cluster\'s most '
        'important political dynamic: Adhara has the power, Mirzam has the credits, '
        'and neither can dominate the other because power without wealth is blunt '
        'and wealth without power is vulnerable.\n\n'
        'The star pulses on a six-hour cycle -- a rhythmic fluctuation in brightness '
        'that the traders have incorporated into their schedules because it affects '
        'human attention patterns. The trading day on Karveth rises and falls with '
        'the light, and the commerce flows with the pulse of a star that does not '
        'care what is being sold beneath it.'
    ),
    cluster=StarClusters.CANOPUS,
)

AVIOR = System(
    name='Avior',
    star='Binary system: a hot blue-white giant (B2IV) and a cooler orange giant (K3II) in a close orbit, casting shifting light that alternates between harsh blue-white and warm amber as the pair rotates',
    population=16_000_000_000,
    distance_to_sol=630.0,
    stellar_objects=[
        StellarObject(
            name='Kallenden',
            short_description='The system\'s most populous world -- six billion people managing the industrial machine that builds the Canopan fleet, under a sky that shifts between blue and amber every few hours.',
            long_description=(
                'Kallenden is Avior\'s primary world -- heavily industrialised, densely '
                'populated, and oriented entirely toward the production of the heavy '
                'warships that Canopan military doctrine demands. The planet is the '
                'cluster\'s Sargas -- the forge where the fleet is made -- and the scale '
                'of the operations matches the cluster\'s need for ships that are denser, '
                'heavier, and more damage-absorbent than anything MERIT or the other outer '
                'factions produce.\n\n'
                'The industrial cities on Kallenden are built around the foundries and '
                'fabrication plants that produce the structural components the shipyards '
                'consume. The foundries are the largest in the cluster -- cavernous '
                'facilities where raw ore is smelted into the dense alloys that give '
                'Canopan warships their characteristic mass. The work is brutal. The '
                'living workforce handles the skilled positions: metallurgists, systems '
                'engineers, quality inspectors who verify that the alloys meet the '
                'specifications that the shipyards demand. The shells handle the rest -- '
                'the pouring, the hauling, the work in the heat and the fumes that would '
                'kill a living worker in months and that degrades a shell in weeks.\n\n'
                'The sky over Kallenden shifts as the binary pair rotates. For a few hours '
                'the blue-white primary dominates -- harsh, bright light that bleaches the '
                'industrial landscape into sharp contrasts. Then the orange giant swings '
                'into prominence and the light softens to amber, casting the foundries and '
                'the smoke they produce in tones that are almost beautiful. The workers do '
                'not notice the shift. The shift has been happening since before they were '
                'born and will continue after they die. The shells do not notice because '
                'the shells do not notice anything.\n\n'
                'The Emperor of Avior is a military figure -- a former fleet commander who '
                'accumulated wealth from shipbuilding contracts and purchased the throne '
                'from a predecessor who had grown tired of ruling after six centuries. The '
                'Emperor understands warships the way the Emperor of Placidus understands '
                'reanimation, and the fleet that Avior produces reflects that understanding '
                '-- ships designed by someone who has fought in them and intends to build '
                'the fleet they wished they had commanded.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='The Berths',
            short_description='The orbital shipyards -- construction bays large enough to build the heaviest capital ships in the galaxy, where the fleet is assembled from Kallenden\'s output.',
            long_description=(
                'The Berths are Avior\'s orbital shipyards -- the largest military '
                'construction facility in the Canopus cluster and one of the largest in '
                'the galaxy. The construction bays are enormous, sized for the capital '
                'ships that are the backbone of Canopan doctrine: vessels so massive that '
                'the bays that contain them during construction are visible from '
                'Kallenden\'s surface as points of reflected light in the orbital plane.\n\n'
                'The ships built at the Berths are the dense, heavy, thick-hulled warships '
                'that define Canopan military identity. The design philosophy is simple: '
                'the crew can be reanimated, so the ship does not need to protect them as '
                'aggressively as a MERIT vessel does. Instead, the armour protects the '
                'ship\'s systems -- the engines, the weapons, the reanimation facilities '
                'that bring the crew back when they die at their stations. A Canopan '
                'capital ship is built to sustain damage that would destroy any other '
                'vessel, to continue fighting through that damage, and to restore its own '
                'crew while under fire. The design produces ships that are slow, brutally '
                'tough, and terrifying to engage because they do not stop.\n\n'
                'The shipyard workforce is mixed. The precision work -- weapons '
                'installation, systems integration, the calibration of the onboard '
                'reanimation suites that are as critical as the weapons -- is performed by '
                'living engineers. The structural work -- welding, fitting, the physical '
                'assembly of hull sections that weigh thousands of tonnes -- is performed '
                'by shells in the vacuum of space. The shells work without suits. They do '
                'not need atmosphere. They work in the vacuum directly, exposed to the '
                'radiation and temperature extremes that would kill a living worker '
                'instantly. The shells degrade in the vacuum but they degrade slowly enough '
                'to be useful, and the supply from Kethra replaces them as they fail.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Drenholm',
            short_description='A mineral-rich world -- deep mining operations feeding Kallenden\'s foundries with the dense ores that Canopan shipbuilding demands.',
            long_description=(
                'Drenholm is the system\'s mining world -- a dense, rocky planet with '
                'mineral deposits that include the heavy elements and rare metals that '
                'Canopan ship construction requires. The mining is deep extraction -- bore '
                'shafts sunk kilometres into the crust, extraction operations running '
                'continuously, and a throughput of raw ore that feeds Kallenden\'s foundries '
                'at the rate the shipyards demand.\n\n'
                'The mines on Drenholm are among the most dangerous workplaces in the '
                'cluster. Deep extraction in dense, heavy rock produces collapses, '
                'gas pockets, and the structural failures that deep mining always generates. '
                'The living miners work the upper levels -- the sections that have been '
                'stabilised and reinforced. The shells work the deep levels -- the freshly '
                'cut sections where the rock is unstable and the risk of collapse is '
                'highest. When the deep sections collapse, the shells in them are buried. '
                'The operations continue around the collapse. New shafts are cut. New '
                'shells are deployed. The ore keeps flowing because the shipyards cannot '
                'afford to wait for the mines to be safe, and the mines will never be safe '
                'because the ore the shipyards need is in the places that safety cannot '
                'reach.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Senthire',
            short_description='A residential and support world -- where the living workers raise families away from the foundries and the mines, in cities built with the same dense alloys the shipyards use.',
            long_description=(
                'Senthire is the system\'s residential world -- a temperate planet further '
                'from the binary pair, where the living workforce that manages Kallenden\'s '
                'foundries and Drenholm\'s mines raises families in conditions that the '
                'industrial worlds cannot provide. The cities on Senthire are built with '
                'the same dense alloys that the foundries produce for the shipyards -- a '
                'pragmatic use of surplus material that gives the architecture a '
                'distinctive solidity, as though the buildings were built to survive '
                'weapons fire. Some of the older structures were.\n\n'
                'The population on Senthire commutes -- orbital shuttles carrying workers '
                'to the industrial worlds and back on shift rotations. The commute is the '
                'system\'s defining rhythm: the workers leave Senthire\'s comfortable cities '
                'for shifts on Kallenden\'s foundry floors or Drenholm\'s mine heads, work '
                'beside shells for the duration, and return to a world where shells are '
                'kept underground and out of sight. The transition is daily and the workers '
                'manage it by compartmentalising -- the foundries are one reality, Senthire '
                'is another, and the commute between them is the membrane that keeps the '
                'two from contaminating each other.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Brethane',
            short_description='A gas giant with fuel processing and military staging -- fleet vessels are fuelled here before departing for deployment across the cluster.',
            long_description=(
                'Brethane is the system\'s gas giant -- fuel processing on its moons '
                'supporting both the industrial traffic and the military fleet. Newly '
                'completed warships from the Berths are fuelled at Brethane before '
                'departing for deployment at Canopus or the other systems that the fleet '
                'defends. The fuelling operation is the final step in the production '
                'chain: ore from Drenholm, alloy from Kallenden, ship from the Berths, '
                'fuel from Brethane, war from wherever the council decides.\n\n'
                'The military staging areas on Brethane\'s moons also serve as the '
                'shakedown zone for new vessels. The ships are tested here -- weapons '
                'fired, systems stressed, the onboard reanimation suites verified by '
                'actually killing and restoring test subjects under controlled conditions. '
                'The test subjects are shells. The practice is considered necessary and '
                'is not discussed outside the military.'
            ),
            population=250_000_000,
        ),
        StellarObject(
            name='Welland',
            short_description='An agricultural world feeding the system -- productive enough to support sixteen billion, supplemented by imports from Alsephina.',
            long_description=(
                'Welland is the system\'s agricultural world -- temperate, fertile, and '
                'farmed at a scale that feeds most of the system\'s sixteen billion people. '
                'The farming follows the standard Canopan model: shells perform the manual '
                'labour, living workers manage the operations. The output is supplemented '
                'by imports from Alsephina -- Avior\'s population is large enough and its '
                'industrial orientation intense enough that local agriculture cannot '
                'cover the full demand.\n\n'
                'The farmers on Welland occupy an unusual position in a system defined by '
                'military industry. They feed the workers who build the ships that fight '
                'the war, and the connection is direct enough that the agricultural workers '
                'feel a pride in their contribution that agricultural workers in other '
                'systems do not. The food goes to the foundries. The foundries make the '
                'alloy. The alloy becomes a warship. The chain is visible and the farmers '
                'are part of it.'
            ),
            population=1_200_000_000,
        ),
    ],
    short_description='The forge of the Canopan fleet -- sixteen billion people building the heaviest warships in the galaxy under a binary sky that shifts between blue and amber.',
    long_description=(
        'Avior builds the fleet that the Canopus cluster sends to war. The system is '
        'the cluster\'s industrial and military production centre -- the shipyards '
        'that construct the dense, heavy, damage-absorbent warships that Canopan '
        'doctrine demands, the foundries that produce the alloys, and the mines that '
        'supply the ore. Sixteen billion people live here, and the system\'s identity '
        'is singular: this is where the ships are made.\n\n'
        'The design philosophy of Canopan warships is built on the reanimation '
        'advantage. The crew can be restored. The ship protects its systems rather '
        'than its people -- engines, weapons, and the onboard reanimation suites that '
        'bring the crew back when they die at their stations. The ships are slow, '
        'brutally tough, and terrifying to engage because they do not stop when they '
        'should. The Berths -- the orbital shipyards above Kallenden -- build these '
        'vessels in construction bays large enough to be visible from the surface.\n\n'
        'The industrial chain is direct: ore from Drenholm\'s deep mines, alloy from '
        'Kallenden\'s foundries, ship from the Berths, fuel from Brethane, war from '
        'wherever the council decides. The living workforce handles the skilled '
        'positions. The shells handle everything that would kill a living worker -- '
        'the pouring in the foundries, the deep mining, the structural assembly in '
        'the vacuum of space where they work without suits because they do not need '
        'atmosphere. The shells degrade. The supply replaces them. The ships keep '
        'coming.\n\n'
        'The Emperor of Avior is a former fleet commander who bought the throne and '
        'builds the fleet they wished they had commanded. The binary star shifts '
        'between harsh blue-white and warm amber as the pair rotates, casting the '
        'foundries and the shipyards in alternating light. The workers do not notice '
        'the shift. The shells do not notice anything. The ships are built regardless.'
    ),
    cluster=StarClusters.CANOPUS,
)

NIHAL = System(
    name='Nihal',
    star='Yellow giant (G8III), approximately 80 times Sol luminosity -- warm golden light that the media producers describe as ideal for broadcast and the theologians describe as divine',
    population=6_000_000_000,
    distance_to_sol=460.0,
    stellar_objects=[
        StellarObject(
            name='Veritate',
            short_description='The cluster\'s voice -- four billion people producing the media, theology, and propaganda that tells the Canopan population what to believe about being dead and coming back.',
            long_description=(
                'Veritate is where the Canopus cluster explains itself to itself. The '
                'planet is the cluster\'s media capital -- the production centre for the '
                'broadcasts, publications, entertainment, and theological content that '
                'shapes how tens of billions of Canopan citizens understand the civilisation '
                'they live in. The message, refined over centuries and delivered through '
                'every medium the technology allows, is simple: death is not an ending. '
                'Reanimation is not an abomination. The hierarchy that reanimation creates '
                '-- where the wealthy live forever and the poor become shells -- is natural, '
                'just, and divinely ordained.\n\n'
                'The theology is the foundation. The Canopan faith -- developed on Veritate, '
                'promoted by Veritate\'s institutions, and taught to every Canopan citizen '
                'from childhood -- holds that the soul persists through death and '
                'reanimation, that restoration is a sacred act, and that the quality of '
                'one\'s restoration reflects the quality of one\'s soul. The wealthy are '
                'restored beautifully because they deserve it. The poor become shells '
                'because their souls are lesser. The theology is elegant, internally '
                'consistent, and provides a moral framework that makes the cluster\'s '
                'grotesque inequality feel like cosmic justice.\n\n'
                'The people who produce this theology do not believe it. The Emperor of '
                'Nihal -- centuries old, restored dozens of times, the architect of the '
                'theological framework that sustains the cluster\'s social order -- is a '
                'pragmatist who understands that the population needs a story that makes '
                'the system tolerable and that the theology is the most effective story '
                'available. The senior theologians who develop the doctrine are scholars '
                'who approach their work as an intellectual exercise in social engineering. '
                'The media executives who distribute it are professionals who measure '
                'effectiveness in audience metrics and behavioural compliance. The faith is '
                'manufactured. The manufacturing is excellent.\n\n'
                'The cynicism at the top does not mean the faith is not real at the bottom. '
                'The billions of ordinary Canopan citizens who hear the theology from '
                'childhood, who are told that the emperors\' immortality is earned rather '
                'than purchased, who believe that their own post-mortem fate reflects their '
                'spiritual worth -- these people believe. The faith provides comfort in a '
                'civilisation where the alternative is confronting the fact that the '
                'difference between a beautiful restoration and a mindless shell is money '
                'and nothing else. The Emperor of Nihal understands that comfort is the '
                'product, and the production never stops.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='The Edicts',
            short_description='An orbital broadcast complex -- the transmission hub that delivers the cluster\'s media and theological content to every inhabited system.',
            long_description=(
                'The Edicts is an orbital broadcast complex above Veritate -- a network of '
                'transmission stations that relay the media and theological content produced '
                'on the surface to every system in the Canopus cluster. The broadcast '
                'infrastructure is the most powerful in the outer systems -- capable of '
                'reaching every inhabited world, every station, every ship in Canopan space '
                'with content that is continuous, pervasive, and calibrated by professionals '
                'who have spent centuries refining the techniques of mass persuasion.\n\n'
                'The Edicts broadcasts theological programming, entertainment that '
                'reinforces the theological messaging, news that is framed within the '
                'theological context, and the educational content that Canopan children '
                'consume from their first years. The content is not crude propaganda. It is '
                'sophisticated, well-produced, and often genuinely entertaining -- the '
                'Emperor of Nihal learned centuries ago that propaganda that feels like '
                'propaganda is ineffective, and the content that the Edicts produces feels '
                'like culture. The theological messaging is woven into dramas, comedies, '
                'historical narratives, and the daily news with a subtlety that the '
                'audience does not detect because detecting it would require the tools '
                'of analysis that the educational content does not provide.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Canthel',
            short_description='A temperate second world -- the theological academies, where the doctrine is developed by scholars who treat faith as an engineering discipline.',
            long_description=(
                'Canthel is the system\'s academic world -- home to the theological '
                'academies that develop the Canopan faith\'s doctrine, train its clergy, '
                'and produce the scholarship that gives the theology its intellectual '
                'weight. The academies are the oldest institutions in the system -- founded '
                'centuries ago by the Emperor of Nihal\'s predecessors, refined by each '
                'successive Emperor, and staffed by scholars whose approach to theology is '
                'closer to engineering than devotion.\n\n'
                'The theological development on Canthel is conducted with the rigour of a '
                'science. The scholars study the population\'s beliefs, identify points of '
                'doubt or resistance, and develop doctrinal responses that address the '
                'doubt without acknowledging the legitimacy of the questioning. When MERIT '
                'broadcasts criticism of reanimation into Canopan space -- which MERIT does '
                'regularly -- the theologians on Canthel produce counter-narratives within '
                'days, framed in theological terms that transform MERIT\'s moral objections '
                'into evidence of spiritual ignorance. The counter-narratives are '
                'effective. The population believes because the alternative is unbearable, '
                'and the scholars provide the intellectual structure that makes the '
                'believing easier.\n\n'
                'The clergy trained on Canthel are deployed across the cluster -- in every '
                'system, on every world, preaching the doctrine that the academies '
                'develop. The clergy believe. This is the system\'s most effective design: '
                'the scholars who develop the doctrine are cynics, but the clergy who '
                'deliver it are sincere, because the training selects for sincerity and '
                'the insincere are redirected to the media production track on Veritate '
                'where their scepticism is an asset rather than a liability.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Morthen',
            short_description='A cold outer world -- where the counter-propaganda operations are based, monitoring MERIT\'s broadcasts and the inner systems\' criticism of Canopan practices.',
            long_description=(
                'Morthen is the system\'s intelligence and counter-propaganda world -- a '
                'cold, quiet planet where the analysts who monitor MERIT\'s information '
                'warfare against the cluster are based. The work is defensive: tracking '
                'MERIT\'s broadcasts into Canopan space, identifying the messages that are '
                'gaining traction with the Canopan population, and coordinating the '
                'theological and media responses that neutralise them.\n\n'
                'Morthen also monitors internal dissent. The Canopan population is not '
                'uniformly faithful -- there are sceptics, questioners, and the people who '
                'have seen too many shells to believe that the difference between a '
                'beautiful restoration and a mindless worker is spiritual worth rather than '
                'financial. The analysts on Morthen track these dissenting voices, assess '
                'their reach, and recommend responses that range from targeted theological '
                'programming to more direct interventions that the Emperor authorises on a '
                'case-by-case basis and that the theologians on Canthel do not ask '
                'about.\n\n'
                'The Emperor of Nihal considers Morthen the system\'s most important world '
                'after Veritate. The theology is only effective if the counter-narratives '
                'are suppressed, and suppression requires knowledge of what the counter-'
                'narratives are. Morthen provides that knowledge. The Emperor uses it with '
                'the precision of someone who has been managing a population\'s beliefs for '
                'centuries and who understands that faith is a garden that requires '
                'constant weeding.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Provender',
            short_description='An agricultural world feeding the system -- the farms are blessed by the clergy and the shells that work them are described in theological terms as \'vessels of service.\'',
            long_description=(
                'Provender is the system\'s agricultural world -- warm, fertile, and farmed '
                'with the standard Canopan combination of living management and shell '
                'labour. What distinguishes Provender from the agricultural worlds of other '
                'systems is the theological overlay. The farms are blessed by clergy from '
                'Canthel\'s academies. The harvests are occasions for religious observance. '
                'The shells that work the fields are described in the theological framework '
                'as vessels of service -- souls completing a divine purpose through labour '
                'that the theology frames as sacred rather than exploitative.\n\n'
                'The living farmers on Provender believe this. The clergy who perform the '
                'blessings believe this. The shells do not believe anything because the '
                'shells are not capable of belief. The theological framework transforms '
                'the uncomfortable reality of dead people working fields into a spiritual '
                'narrative that the farming community finds comforting. The comfort is the '
                'point. The Emperor of Nihal designed it to be.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Ostren',
            short_description='A gas giant with fuel processing -- unremarkable operations in a system whose product is not physical goods but the beliefs that hold the cluster together.',
            long_description=(
                'Ostren is the system\'s gas giant -- fuel processing on its moons '
                'supporting the traffic that Nihal\'s media and theological output '
                'generates. The traffic is distinctive: broadcast relay ships carrying '
                'content updates to the cluster\'s systems, clergy transports delivering '
                'newly trained theologians to their assignments, and the private vessels '
                'of the media executives and senior scholars who travel between Nihal and '
                'the other systems on the Emperor\'s business. The fuel workers process the '
                'traffic and do not comment on its character. In a system that manufactures '
                'belief, the fuel workers\' agnosticism is the most honest thing about it.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='The cluster\'s voice -- six billion people manufacturing the theology, media, and propaganda that tells the Canopan population the hierarchy is divine rather than purchased.',
    long_description=(
        'Nihal is where the Canopus cluster\'s story is written. The system is the '
        'cluster\'s media capital and theological centre -- the production hub for the '
        'broadcasts, doctrine, and cultural content that shapes how tens of billions '
        'of Canopan citizens understand the civilisation they live in. The message is '
        'simple: reanimation is sacred. The hierarchy it creates is divinely ordained. '
        'The wealthy are restored beautifully because they deserve it. The poor become '
        'shells because their souls are lesser. The theology is elegant, internally '
        'consistent, and provides a moral framework that makes grotesque inequality '
        'feel like cosmic justice.\n\n'
        'The people who produce this theology do not believe it. The Emperor of Nihal '
        '-- centuries old, the architect of the theological framework -- is a '
        'pragmatist who understands that the population needs a story and that this is '
        'the most effective one available. The senior theologians on Canthel approach '
        'doctrine development as engineering. The media executives on Veritate measure '
        'effectiveness in audience metrics. The propaganda that feels like propaganda '
        'is ineffective, so the content feels like culture -- sophisticated, '
        'entertaining, with theological messaging woven into dramas and news with a '
        'subtlety the audience does not detect.\n\n'
        'The cynicism at the top does not mean the faith is not real at the bottom. '
        'Billions of ordinary citizens believe. The clergy who deliver the doctrine '
        'are sincere -- selected for sincerity during training, with the insincere '
        'redirected to media production where scepticism is an asset. The population '
        'believes because the alternative is confronting the fact that the difference '
        'between a beautiful restoration and a mindless shell is money and nothing '
        'else, and the theologians on Canthel ensure that the alternative is never '
        'presented clearly enough to be confronted.\n\n'
        'Morthen monitors the counter-narratives -- MERIT\'s broadcasts, internal '
        'dissent, the sceptics who have seen too many shells to believe. The responses '
        'range from targeted theological programming to interventions the Emperor '
        'authorises and the theologians do not ask about. Faith is a garden. It '
        'requires constant weeding. The Emperor of Nihal has been weeding for '
        'centuries and the garden has never looked healthier.'
    ),
    cluster=StarClusters.CANOPUS,
)

TURAIS = System(
    name='Turais',
    star='Yellow-white main sequence (F3V), approximately 5 times Sol luminosity -- a pleasant, stable star casting light that makes the system look deceptively normal',
    population=9_000_000_000,
    distance_to_sol=470.0,
    stellar_objects=[
        StellarObject(
            name='Sothane',
            short_description='The system where the shells are not hidden and nobody minds -- five billion people who have integrated the reanimated into daily life so completely that the horror has become ordinary.',
            long_description=(
                'Sothane is the world that MERIT uses in its propaganda to demonstrate '
                'what Canopan civilisation truly is. The planet is temperate, well-developed, '
                'and home to five billion living people who share their world with a shell '
                'population of comparable size. The shells are not hidden. They are not '
                'restricted to night shifts or sealed sections or underground corridors. '
                'The shells on Sothane are everywhere -- walking the streets, riding the '
                'transit, standing in queues at service counters, sitting in designated '
                'areas of public spaces, waiting for instructions in the patient, motionless '
                'stance that characterises a shell with no current task.\n\n'
                'The difference between Sothane and Phaet is not the visibility. On Phaet, '
                'the shells are visible and the living population has adapted by learning '
                'not to see them. On Sothane, the shells are visible and the living '
                'population sees them, interacts with them, and does not find the '
                'interaction disturbing. The normalisation on Sothane goes deeper than '
                'Phaet\'s studied blindness. The living residents of Sothane give their '
                'household shells names. They speak to them, knowing the shells cannot '
                'understand or respond. They develop preferences -- this shell is better '
                'at cleaning, that one is steadier carrying loads. Children grow up with '
                'shells in the household the way children elsewhere grow up with domestic '
                'appliances, and the comparison is not metaphorical: on Sothane, a shell '
                'is an appliance that happens to be shaped like a person.\n\n'
                'The integration extends to public life. Shells serve in retail -- standing '
                'behind counters, stocking shelves, performing the repetitive tasks that '
                'retail requires. They serve in food preparation -- the theological '
                'framework from Nihal has been particularly successful on Sothane, and the '
                'population does not object to food handled by shells because the shells '
                'are vessels of service fulfilling their divine purpose. They serve as '
                'personal attendants to the middle class -- not just the wealthy, as in '
                'other systems, but ordinary families who can afford a shell the way '
                'ordinary families elsewhere afford a vehicle.\n\n'
                'Visitors from other Canopan systems find Sothane unsettling. Visitors from '
                'the inner systems find it nightmarish. The sight of a family dining in a '
                'restaurant while a shell stands motionless behind the table, waiting to '
                'clear the plates, is an image that MERIT\'s propagandists have broadcast '
                'across the inner systems. The residents of Sothane do not understand the '
                'reaction. The shell is providing a service. The family is eating dinner. '
                'What is there to be disturbed by?'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Beladen',
            short_description='A second world where the shell integration goes further -- the shells perform roles that other systems reserve for the living, including childcare and elder care.',
            long_description=(
                'Beladen is Sothane\'s smaller, warmer companion -- a world where the '
                'normalisation of shell labour has progressed further than anywhere else '
                'in the cluster. On Sothane, shells are household appliances and service '
                'workers. On Beladen, shells occupy roles that every other system in the '
                'cluster reserves exclusively for the living: childcare and elder care.\n\n'
                'The childcare shells are selected for physical attributes that approximate '
                'gentleness -- shells whose motor function degradation produces slow, '
                'careful movements rather than the jerky imprecision that characterises '
                'most low-quality reanimation. The shells cannot comfort a crying child. '
                'They cannot read stories or answer questions or provide the emotional '
                'presence that childcare requires. What they can do is carry, hold, follow, '
                'and prevent a small child from injuring itself with the tireless patience '
                'of something that does not experience impatience. The parents of Beladen '
                'consider this adequate supervision. Parents from other systems consider '
                'it abandonment to a corpse.\n\n'
                'The elder care is grimmer. The old and infirm on Beladen who cannot afford '
                'quality reanimation and who are approaching death are tended by shells -- '
                'fed, cleaned, turned, and maintained by reanimated workers who perform '
                'the physical tasks of care without the emotional content. The dying are '
                'attended by the dead. The theological framework from Nihal describes this '
                'as preparation -- the shells are guiding the dying toward the transition '
                'that the shells themselves have already completed. The families who cannot '
                'afford to hire living caregivers accept this framing because the '
                'alternative is accepting that their parents are being tended by animated '
                'corpses and that nobody cares enough to provide anything better.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Turnstile Station',
            short_description='The system\'s orbital port -- where the shell integration is immediately visible to arriving visitors in ways the station staff genuinely do not understand are disturbing.',
            long_description=(
                'Turnstile Station is Turais\'s primary orbital facility -- a busy station '
                'that handles the system\'s traffic with a workforce that is, like '
                'everything on Turais, a mix of living and shell. The shells perform '
                'customer-facing roles on the station -- guiding visitors to their '
                'destinations, carrying luggage, staffing the information desks. The shells '
                'cannot answer questions, but they can gesture toward the correct direction '
                'and carry belongings with the careful steadiness that Turais\'s shell '
                'workforce is selected for.\n\n'
                'The station is the first point of contact for visitors, and the experience '
                'is jarring for anyone who has not been to Turais before. A shell in a '
                'uniform approaching to assist with luggage -- the face blank, the '
                'movements almost right but not quite, the hands that reach for the bags '
                'with a coordination that is recognisably human and recognisably wrong -- '
                'is an experience that visitors from the inner systems describe as the most '
                'disturbing moment of their lives. The station staff, all from Turais, '
                'observe the visitors\' reactions with polite confusion. The shell is '
                'helping. The visitor is distressed. The staff do not connect the two.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Graith',
            short_description='A light industrial world -- manufacturing and services, where the shell workforce is integrated into the factories the same way it is integrated into the households.',
            long_description=(
                'Graith is the system\'s industrial world -- light manufacturing, services, '
                'and the commercial operations that support the system\'s economy. The '
                'factories on Graith are not the dark, cold, shell-only operations of '
                'Phaet\'s Dravven. They are lit, heated, and mixed -- living workers and '
                'shells on the same floor, performing complementary tasks in an arrangement '
                'that Turais considers natural and that industrial managers from other '
                'systems consider a psychological hazard.\n\n'
                'The integration on Graith\'s factory floors reflects the system\'s broader '
                'normalisation. The living workers talk to each other across the shells the '
                'way people in other systems talk across furniture -- the shells are '
                'present, occupying space, performing tasks, and completely absent from the '
                'social landscape of the workplace. A living worker on Graith will hand a '
                'tool to a shell with the same casual disregard they would use handing a '
                'tool to a rack. The shell takes the tool. The shell uses the tool. The '
                'interaction is mechanical on both sides, because on Turais the living have '
                'learned to be as mechanical in their interactions with shells as the shells '
                'are in everything.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Fenwick',
            short_description='An agricultural world -- farmed by shells under living management, with the theological overlay from Nihal more deeply embedded here than in any other farming community.',
            long_description=(
                'Fenwick is the system\'s agricultural world -- warm, productive, and '
                'farmed by shells under living management. The farming operations are '
                'standard for the cluster, but the cultural context is distinctly Turais: '
                'the shells in the fields are viewed with the same casual acceptance as the '
                'shells in the households and the factories. The farmers of Fenwick treat '
                'their agricultural shells the way farmers elsewhere treat draft animals '
                '-- useful tools that are maintained while functional and replaced when '
                'not.\n\n'
                'The theological overlay from Nihal is deeply embedded in Fenwick\'s farming '
                'culture. The harvest blessings, the seasonal observances, and the '
                'theological framework that describes the shells as vessels of service are '
                'not simply accepted on Fenwick -- they are lived. The farming families '
                'genuinely believe that the shells working their fields are fulfilling a '
                'sacred purpose, and the belief gives the community a serenity about the '
                'reanimated labour force that visitors find either admirable or horrifying '
                'depending on whether they share the faith.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Hovander',
            short_description='A gas giant with fuel processing -- the one workplace in the system where the living work alone, and where they sometimes remember what alone feels like.',
            long_description=(
                'Hovander is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The operations are staffed by living '
                'workers only -- the same technical requirement as elsewhere in the cluster. '
                'For the fuel workers on Hovander, the posting is the only environment '
                'they will encounter in their careers where no shells are present. The '
                'experience is reported differently by different workers: some find the '
                'absence of shells disorienting, the way a constant background noise is '
                'disorienting when it stops. Others find it a relief they did not know '
                'they needed. A few describe the experience of working in a space occupied '
                'only by the living as something they cannot name -- a quality of presence '
                'that the constant proximity of the dead on the inhabited worlds has '
                'quietly eroded.'
            ),
            population=50_000_000,
        ),
    ],
    short_description='The system where the dead are family -- nine billion people who have normalised shell labour so completely that the horror has become invisible.',
    long_description=(
        'Turais is the Canopus cluster\'s most normalised system. Every Canopan system '
        'uses shells. Most hide them. Phaet cannot hide them and the population has '
        'adapted by learning not to see. Turais does not hide them and the population '
        'does not need to learn not to see because the population does not find them '
        'disturbing. The shells on Turais are integrated into daily life at every '
        'level -- household servants, retail workers, food handlers, factory labour, '
        'and on Beladen the roles that every other system reserves for the living: '
        'childcare and elder care.\n\n'
        'The normalisation is complete. Living residents name their household shells. '
        'They speak to them knowing the shells cannot understand. They develop '
        'preferences. Children grow up with shells in the household the way children '
        'elsewhere grow up with appliances, and the comparison is not metaphorical. A '
        'family dines while a shell stands motionless behind the table waiting to '
        'clear the plates, and the family does not register the presence as unusual '
        'because it has never been anything else.\n\n'
        'Visitors from other Canopan systems find Turais unsettling. Visitors from '
        'the inner systems find it nightmarish. MERIT uses images from Turais in its '
        'propaganda -- the family at dinner with the shell behind them is one of the '
        'most widely broadcast images in the inner systems. The residents of Turais '
        'do not understand the reaction. The theological framework from Nihal has been '
        'particularly effective here: the shells are vessels of service, the living '
        'are their custodians, and the arrangement is sacred. The belief is sincere. '
        'The sincerity is what makes it terrifying.\n\n'
        'On Hovander\'s fuel-processing moons, the only workplace without shells, '
        'some workers report that the absence is disorienting -- a background presence '
        'removed. Others describe a quality of being among only the living that they '
        'cannot name but that the constant proximity of the dead has quietly eroded. '
        'They return to the inhabited worlds and the shells are there and the quality '
        'disappears and they cannot remember what it was.'
    ),
    cluster=StarClusters.CANOPUS,
)

ACRUX = System(
    name='Acrux',
    star='Binary system: a hot blue-white main sequence star (B0.5IV) and a dimmer blue-white companion (B1V) in a close orbit, combined luminosity approximately 40,000 times Sol',
    population=8_000_000_000,
    distance_to_sol=320.0,
    stellar_objects=[
        StellarObject(
            name='Delvorn',
            short_description='The system\'s most populous world -- a dense, mineral-rich planet that has been mined for centuries and will be mined for centuries more because the shells do not run out.',
            long_description=(
                'Delvorn is the Canopus cluster\'s primary mining world -- a dense, rocky '
                'planet with mineral deposits that include the heavy metals, rare earths, '
                'and exotic compounds that the cluster\'s industry and reanimation '
                'technology require. The mining has been continuous for centuries. The '
                'deposits are deep. The extraction is intensive. The planet\'s surface is '
                'scarred with open-cast operations visible from orbit, and the subsurface '
                'is threaded with mine shafts that extend kilometres into the crust.\n\n'
                'The mining on Delvorn is performed overwhelmingly by shells. The deep '
                'extraction that the cluster demands -- the shafts sunk into unstable rock, '
                'the operations in atmospheres toxic with mineral dust, the work in '
                'temperatures that exceed what living bodies can sustain -- is shell work. '
                'The shells descend into the mines at the start of their functional period '
                'and work until they cease functioning. Some last months. Some last weeks. '
                'The deep mines are the most destructive environment for shells in the '
                'cluster -- worse than Alsephina\'s livestock operations, worse than '
                'Treven\'s saltwater. The mine shafts consume shells at a rate that Kethra\'s '
                'processing facilities are calibrated to match.\n\n'
                'The living workforce on Delvorn is small relative to the population -- '
                'engineers, geologists, logistics coordinators, and the mine managers who '
                'oversee the operations from surface facilities. The living do not enter '
                'the deep mines. The conditions are too dangerous and the economics do not '
                'justify the risk when shells are available. The mine managers monitor the '
                'shell workforce on instrumentation that tracks each unit\'s location, '
                'output, and functional status. When a unit\'s status changes from '
                'functional to non-functional, the display updates and a replacement is '
                'dispatched. The process is automatic. The managers do not pause.\n\n'
                'The Emperor of Acrux is the cluster\'s oldest ruler -- older than the '
                'Emperor of Adhara, older than the Emperor of Canopus, restored so many '
                'times that the medical records span volumes. The Emperor has ruled the '
                'mining system since before the other emperors were born, and the longevity '
                'has produced a ruler of extraordinary patience and minimal sentiment. The '
                'mines produce. The shells are consumed. The ore flows to Avior and '
                'Placidus. The Emperor considers this sufficient.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Torvallis',
            short_description='A second mining world -- specialising in the rare compounds that Placidus\'s reanimation technology requires, mined from geological formations found nowhere else in the cluster.',
            long_description=(
                'Torvallis is the system\'s second mining world -- a cold, dense planet '
                'whose geological history produced mineral formations that include compounds '
                'critical to the reanimation process. The neural reconstruction matrices '
                'that Revane\'s practitioners use, the tissue regeneration compounds that '
                'the Lazaret\'s restoration suites require, and the chemical precursors that '
                'make the entire technology possible -- the raw materials for all of these '
                'are mined on Torvallis.\n\n'
                'The mining is specialised and exacting. The compounds are found in narrow '
                'geological veins that require careful extraction -- crude methods destroy '
                'the molecular structures that make the compounds useful. The extraction '
                'shells on Torvallis are selected for fine motor function rather than '
                'strength -- shells whose reanimation produced unusually precise hand '
                'control, capable of the delicate work that the extraction requires. These '
                'shells are more expensive to produce and more valuable to maintain, and '
                'the attrition rate is monitored more carefully than on Delvorn because a '
                'fine-motor shell that ceases functioning is harder to replace than a '
                'general-labour unit.\n\n'
                'Torvallis\'s output is the bottleneck that the entire reanimation industry '
                'depends on. If the mines on Torvallis stop producing, the restoration '
                'clinics on Revane run out of materials within months. The emperors and '
                'kings who depend on reanimation for their immortality understand this '
                'dependency, and the Emperor of Acrux uses it with the same quiet leverage '
                'that the Emperor of Placidus uses the waiting list. The ore is the '
                'foundation. Everything else is built on it.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Rendak',
            short_description='A processing world -- where the raw ore from Delvorn and Torvallis is refined into the materials that the cluster\'s shipyards and restoration clinics consume.',
            long_description=(
                'Rendak is the system\'s processing world -- a warm, rocky planet where the '
                'raw ore extracted from Delvorn and Torvallis is refined, purified, and '
                'prepared for shipment to the cluster\'s consumers. The refineries on Rendak '
                'handle two distinct supply chains: the heavy metals and structural alloys '
                'destined for Avior\'s shipyards, and the delicate pharmaceutical compounds '
                'destined for Placidus\'s restoration clinics. The two chains share the '
                'planet but not the facilities -- the heavy processing is conducted in '
                'massive industrial complexes on the equatorial plains, while the '
                'pharmaceutical refinement is conducted in clean-room facilities in the '
                'northern highlands where the air is thinner and the contamination risk is '
                'lower.\n\n'
                'The workforce split reflects the two chains. The heavy processing is '
                'shell-intensive -- the same brutal, toxic work that characterises heavy '
                'industry across the cluster. The pharmaceutical refinement is living-'
                'intensive -- the precision required exceeds what shells can reliably '
                'provide, and the value of the compounds being processed makes the cost '
                'of living workers justified. The pharmaceutical workers on Rendak are '
                'among the best-paid in the cluster, because the materials they handle '
                'are worth more per gram than anything else the mining industry produces.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Refinery Station',
            short_description='The system\'s orbital port -- where the refined materials are loaded onto the freighters that carry them to every system in the cluster.',
            long_description=(
                'Refinery Station is Acrux\'s primary orbital facility -- a large industrial '
                'port handling the system\'s heavy freight traffic. The station processes '
                'two streams of outgoing cargo: the bulk shipments of structural materials '
                'destined for Avior\'s shipyards, loaded onto heavy freighters in enormous '
                'quantities, and the small, high-value shipments of pharmaceutical '
                'compounds destined for Placidus, transported in sealed, climate-controlled '
                'containers under security that reflects their worth.\n\n'
                'The station\'s freight operations are shell-operated, as is standard. The '
                'pharmaceutical containers are the exception -- handled exclusively by '
                'living workers because the precision required to move containers worth '
                'more than the ships carrying them exceeds shell capability. The juxtaposition '
                'is visible: shells hauling tonnes of structural alloy in one bay while '
                'living workers in clean-room suits carefully transfer gram-weight containers '
                'of pharmaceutical compound in the next. The ore and the medicine. The '
                'ships and the immortality. Both from the same rock.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Kelthane',
            short_description='A gas giant with fuel processing -- supporting the heavy freighter traffic that carries the cluster\'s raw materials.',
            long_description=(
                'Kelthane is the system\'s gas giant -- fuel processing on its moons '
                'supporting the constant freighter traffic that Acrux\'s mining output '
                'generates. The traffic is heavy and directional: freighters arrive empty '
                'from Avior and Placidus, load at Refinery Station, and depart full. The '
                'fuel operations are sized for this traffic pattern -- processing capacity '
                'weighted toward the outbound vessels that depart heavier than they '
                'arrived.\n\n'
                'The fuel workers are living -- standard across the cluster for fuel '
                'processing. The posting on Kelthane\'s moons is considered one of the '
                'better assignments in the system, because the fuel workers are distant '
                'from the mines and the processing plants and the constant, visible '
                'consumption of shells that defines life on the inner worlds. The fuel '
                'workers describe the posting as quiet. In a system built on extraction, '
                'quiet is valued.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Brethaven',
            short_description='An agricultural world feeding the system -- small, functional, supplemented by imports from Alsephina because the system\'s economy is extraction, not farming.',
            long_description=(
                'Brethaven is the system\'s agricultural world -- a temperate planet further '
                'from the binary pair, farmed at a scale that covers part of the system\'s '
                'food demand. The output is insufficient for eight billion people, and the '
                'deficit is covered by imports from Alsephina. The Emperor of Acrux has '
                'never invested in expanding Brethaven\'s agricultural capacity because the '
                'Emperor\'s resources are directed at the mines and the processing '
                'facilities -- the operations that generate the revenue and the leverage '
                'that the agricultural world does not.\n\n'
                'The farming is shell-operated under living management -- the standard '
                'model. The farmers on Brethaven are the system\'s quietest population, '
                'overshadowed by the mining operations that define the system\'s identity '
                'and character. The food is grown, shipped, and consumed without remark, '
                'which is the highest aspiration of a farming community in a system that '
                'considers agriculture a support function rather than a purpose.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The cluster\'s foundation -- eight billion people extracting the raw materials that the shipyards and the reanimation industry cannot function without.',
    long_description=(
        'Acrux is where the cluster\'s physical foundation is extracted from the rock. '
        'The system is the Canopus cluster\'s primary mining operation -- two worlds '
        'producing the raw materials that flow to Avior\'s shipyards and Placidus\'s '
        'restoration clinics, processed on a third world into the structural alloys '
        'and pharmaceutical compounds that the cluster\'s industry and immortality '
        'depend on. Eight billion people live here, and the system\'s character is '
        'defined by extraction -- the removal of material from the ground by a '
        'workforce that is overwhelmingly dead.\n\n'
        'Delvorn is the primary mining world -- centuries of continuous extraction '
        'from a dense, mineral-rich crust, performed by shells that descend into the '
        'deep mines and work until they cease functioning. The deep mines are the most '
        'destructive environment for shells in the cluster. Torvallis specialises in '
        'the rare compounds that the reanimation industry requires -- delicate '
        'extraction by fine-motor shells selected for precision. Rendak processes the '
        'raw ore into the two supply chains: bulk structural materials for the '
        'shipyards, high-value pharmaceutical compounds for the clinics.\n\n'
        'The Emperor of Acrux is the cluster\'s oldest ruler -- older than any other '
        'emperor, restored so many times that the medical records span volumes. The '
        'longevity has produced a ruler of extraordinary patience and minimal '
        'sentiment. The mines produce. The shells are consumed. The ore flows. The '
        'Emperor of Acrux controls the raw materials that every other system depends '
        'on, and exercises that control with the quiet certainty of someone who has '
        'been watching empires rise and fall for longer than most of the other '
        'emperors have been alive.\n\n'
        'Torvallis is the critical leverage. The reanimation compounds mined there '
        'are the bottleneck that the entire industry depends on -- if Torvallis stops '
        'producing, the restoration clinics on Revane run dry within months. Every '
        'emperor who depends on reanimation for their immortality understands this '
        'dependency, and the Emperor of Acrux ensures they never forget it.'
    ),
    cluster=StarClusters.CANOPUS,
)

ASPID = System(
    name='Aspid',
    star='Blue-white subgiant (B5IV), approximately 4,000 times Sol luminosity -- a hot, bright star casting harsh light over the cluster\'s military rear area',
    population=7_000_000_000,
    distance_to_sol=690.0,
    stellar_objects=[
        StellarObject(
            name='Halstrom',
            short_description='The cluster\'s military staging world -- where the ships built at Avior are crewed, the crews are trained, and the dead learn to fight again.',
            long_description=(
                'Halstrom is where the Canopan fleet becomes operational. The warships '
                'arrive from Avior\'s Berths -- newly built, fuelled, and empty. They are '
                'crewed on Halstrom. The crews are trained on Halstrom. The ships that '
                'will carry the cluster\'s war to MERIT are assembled here into the fleet '
                'formations that Canopan doctrine prescribes, and they depart from Halstrom '
                'for deployment at the Canopus gateway or wherever the council\'s military '
                'planning requires.\n\n'
                'The training on Halstrom is unlike military training anywhere else in the '
                'galaxy. The Canopan fleet\'s advantage is attritional -- the crews can be '
                'reanimated, and the training must prepare them for the experience of dying '
                'and returning to duty. The recruits on Halstrom train for combat. They '
                'also train for death. The training programme includes controlled '
                'reanimation exercises -- the recruits are killed under medical supervision, '
                'restored, and returned to training. The purpose is acclimatisation: a crew '
                'member who has already died and been restored once is less likely to '
                'hesitate in combat than one who has not. The psychological cost of this '
                'training is documented, managed, and accepted as the price of a military '
                'advantage that no other faction can replicate.\n\n'
                'The reanimation facilities on Halstrom are military-grade -- functional '
                'rather than luxurious, restoring personnel to operational status as quickly '
                'as possible. The quality is adequate. The restored personnel are capable of '
                'fighting. Whether they are fully who they were before each successive '
                'restoration is a question the military has decided is less important than '
                'whether they can operate their stations, follow orders, and absorb the '
                'damage that Canopan doctrine expects them to absorb.\n\n'
                'The Emperor of Aspid is a military ruler -- one of the few emperors who '
                'still actively commands fleet operations rather than delegating to '
                'subordinates. The Emperor\'s military experience is measured in centuries '
                'of warfare and dozens of personal deaths in combat, each one followed by '
                'restoration and return to command. The Emperor of Aspid has died more '
                'times than any other emperor and considers this a qualification rather '
                'than a liability.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='The Cruciform',
            short_description='The system\'s primary orbital installation -- fleet staging, training exercises in the orbital space, and the assembly point for strike forces deploying to the gateway.',
            long_description=(
                'The Cruciform is Aspid\'s primary orbital facility -- a massive military '
                'station that serves as the fleet\'s staging area and the coordination '
                'centre for the training exercises that fill the system\'s orbital space. '
                'The station is built for military throughput rather than comfort: docking '
                'bays sized for capital ships, logistics infrastructure for fleet-scale '
                'supply operations, and the command facilities from which the Emperor of '
                'Aspid personally oversees the fleet\'s readiness.\n\n'
                'The orbital space around the Cruciform is the cluster\'s primary training '
                'ground. Fleet exercises are conducted regularly -- live-fire drills, '
                'formation manoeuvres, and the simulated engagements that prepare crews for '
                'combat against MERIT\'s faster, lighter vessels. The Canopan tactical '
                'problem is always the same: their ships are slower than MERIT\'s but '
                'tougher, and the training emphasises how to force an engagement that plays '
                'to the Canopan advantage -- closing to ranges where the attritional '
                'superiority of crews that can be reanimated outweighs the speed advantage '
                'of crews that cannot.\n\n'
                'The Cruciform is also the assembly point for strike forces deploying to '
                'the Canopus gateway or other operational areas. When the council authorises '
                'an offensive operation, the ships gather at the Cruciform, the crews are '
                'briefed, and the fleet departs as a formation. The departure of a Canopan '
                'strike force from the Cruciform is a distinctive sight: the heavy ships '
                'moving slowly, in close formation, their dense mass registering on sensors '
                'as a wall of metal approaching at a pace that MERIT\'s strategists have '
                'learned to take seriously despite the lack of speed.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Kellastre',
            short_description='A rocky world used for ground combat training and the controlled reanimation exercises that prepare recruits for the experience of dying.',
            long_description=(
                'Kellastre is the system\'s ground training world -- a rocky, barren planet '
                'with a thin atmosphere that the military uses for the training operations '
                'that require surface conditions. The ground combat training is conventional '
                '-- unit tactics, weapons proficiency, the skills that infantry require '
                'in boarding operations and planetary assault. The unconventional training '
                'is what makes Kellastre notorious.\n\n'
                'The controlled reanimation exercises are conducted on Kellastre. The '
                'recruits who are selected for the programme -- the best candidates, the '
                'ones who will crew the fleet\'s front-line vessels -- are killed under '
                'medical supervision in the exercise facilities. The deaths are clinical: '
                'cardiac arrest induced by injection, the body confirmed dead by medical '
                'staff, and the reanimation procedure initiated within minutes. The '
                'restored recruit wakes in a recovery ward, alive again, knowing that they '
                'have died and been brought back. The experience is described by those who '
                'have undergone it in terms that the military psychologists study '
                'extensively and that the recruits discuss only with each other.\n\n'
                'Not every recruit survives the exercise. The reanimation process at '
                'military-grade quality has a failure rate that is small but nonzero. '
                'The recruits who die in the exercise and cannot be restored are buried '
                'on Kellastre with full military honours. The ceremonies are conducted '
                'by the Emperor of Aspid in person when possible. The Emperor has died '
                'dozens of times and considers the dead recruits comrades rather than '
                'casualties, which is either the most respectful or the most disturbing '
                'perspective available depending on where you stand on the practice.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Vrentiss',
            short_description='A residential world -- where the military families live, away from the training grounds and the staging operations, in communities shaped by the knowledge that death is temporary.',
            long_description=(
                'Vrentiss is the system\'s residential world -- a temperate planet where the '
                'families of the military personnel who train and deploy from Halstrom live '
                'in communities shaped by the peculiar character of Canopan military '
                'service. The culture on Vrentiss is military-adjacent but not military: '
                'the families are civilians who live with the knowledge that their partners '
                'and parents will go to war, may die in combat, and may come back.\n\n'
                'The may is the weight. Reanimation is not guaranteed. Military-grade '
                'restoration has a success rate that is high but not total, and the quality '
                'of each successive restoration degrades slightly -- a cumulative erosion '
                'that the families on Vrentiss track in the small changes they notice when '
                'their person comes back. A little less patient. A little less present. '
                'The laugh not quite the same. The families learn to accept the changes '
                'because the alternative is a partner or parent who does not come back at '
                'all, and the changes are small enough to be absorbed if you do not look '
                'too closely.\n\n'
                'The children on Vrentiss grow up with a relationship to death that no '
                'other human community shares. A parent deploys, dies in combat, is '
                'restored, and returns. The child has a parent who died and came back. '
                'The parent is mostly the same. The child learns that death is not '
                'permanent but that it changes the person, and the child carries this '
                'understanding into adulthood with effects that the military psychologists '
                'on Halstrom study in classified reports that the families are not shown.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Stannard',
            short_description='A gas giant with fuel processing and the military stockpiles that support fleet operations -- the last fuel stop before the weapons testing range at CNP-3318.',
            long_description=(
                'Stannard is the system\'s gas giant -- fuel processing on its moons '
                'supporting the military traffic and the fleet operations that define the '
                'system. The fuel operations are military-priority: fleet vessels are '
                'fuelled first, training exercises second, and civilian traffic last. The '
                'military stockpiles on Stannard\'s outer moons maintain reserves for '
                'sustained fleet operations -- enough fuel and supplies to support a '
                'deployment without resupply.\n\n'
                'Stannard is also the last fuel stop before the jump to CNP-3318 -- the '
                'uninhabited system one jump away that the military uses as a weapons '
                'testing range for ordnance too dangerous to test in inhabited space. The '
                'ships that transit to CNP-3318 fuel at Stannard and carry enough to '
                'return, because CNP-3318 has no fuel processing and nothing else that '
                'would support a sustained presence. The weapons testers describe the '
                'transit as routine. The weapons they are testing are not.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Cottam',
            short_description='An agricultural world feeding the system -- productive enough to support the military population without relying heavily on imports.',
            long_description=(
                'Cottam is the system\'s agricultural world -- temperate, well-farmed, and '
                'productive enough to feed seven billion people with a modest surplus. The '
                'Emperor of Aspid invested in agricultural self-sufficiency early in the '
                'system\'s development -- a military mind\'s instinct that a system '
                'dependent on food imports is a system with a supply chain that an enemy '
                'can cut. Cottam\'s output ensures that Aspid can feed itself even if the '
                'freighter routes from Alsephina are disrupted.\n\n'
                'The farming follows the standard Canopan model: shells in the fields, '
                'living management. The agricultural workers on Cottam have the particular '
                'pride of people who feed a military -- the knowledge that the fleet\'s '
                'crews train and deploy on calories that Cottam produced, and that the '
                'connection between the field and the fight is as direct as it is in Avior.'
            ),
            population=800_000_000,
        ),
    ],
    short_description='The cluster\'s war machine -- seven billion people training the crews, staging the fleet, and preparing for combat in a military where death is part of the training.',
    long_description=(
        'Aspid is where the Canopan fleet learns to fight and to die. The system is '
        'the cluster\'s military staging and training centre -- the place where ships '
        'from Avior\'s Berths are crewed, where those crews are trained in the '
        'distinctive challenges of Canopan warfare, and where the fleet formations '
        'that deploy to the gateway and beyond are assembled. Seven billion people '
        'live here, the majority connected to the military apparatus that is the '
        'system\'s purpose.\n\n'
        'The training is what makes Aspid unique. Canopan military doctrine is built '
        'on the attritional advantage of crews that can be reanimated, and the '
        'training must prepare recruits for the experience of dying in combat and '
        'returning to duty. The controlled reanimation exercises on Kellastre -- where '
        'recruits are killed under medical supervision and restored -- are the '
        'cluster\'s most controversial military practice and its most effective. A '
        'crew member who has already died once does not hesitate when the ship takes '
        'damage that would terrify an unacclimated crew. The psychological cost is '
        'documented and accepted.\n\n'
        'The Emperor of Aspid is a military ruler who has died in combat more times '
        'than any other emperor -- dozens of deaths, dozens of restorations, each one '
        'followed by return to command. The Emperor considers this a qualification. '
        'The Emperor still actively commands fleet operations and oversees the '
        'training personally from the Cruciform. The fleet that departs Aspid for '
        'deployment is the product of this leadership: crews who have been trained to '
        'fight, to die, and to fight again, in ships that are built to sustain the '
        'damage that makes the dying necessary.\n\n'
        'One jump from Aspid is CNP-3318 -- the uninhabited system used as a weapons '
        'testing range for ordnance too dangerous to test in inhabited space. The '
        'proximity is deliberate. The weapons developed and tested at CNP-3318 are '
        'designed for the fleet that trains at Aspid, and the feedback loop between '
        'the testers and the fleet command is tight. The weapons are tested. The '
        'results are assessed. The fleet adapts. The cycle is continuous.'
    ),
    cluster=StarClusters.CANOPUS,
)

NAOS = System(
    name='Naos',
    star='Hot blue supergiant (O3If), approximately 800,000 times Sol luminosity -- one of the most luminous stars in the galaxy, casting intense blue-white light that the system\'s atmospheric engineering filters to comfortable levels',
    population=10_000_000_000,
    distance_to_sol=460.0,
    stellar_objects=[
        StellarObject(
            name='Serenath',
            short_description='The best place to be alive in the Canopus cluster -- five billion people living in genuine comfort because the shells do everything that comfort requires.',
            long_description=(
                'Serenath is the system that the Canopus cluster points to the way Kaus is '
                'the system the Antares cluster points to: proof that the model works. The '
                'planet is temperate, beautifully terraformed, and home to five billion '
                'people who live in conditions that rival the best inner-system worlds. '
                'The cities are clean, the infrastructure is excellent, the housing is '
                'spacious, the parks are maintained, the healthcare is superb. The quality '
                'of life on Serenath is, by every measurable metric, outstanding.\n\n'
                'The quality is possible because the shells do everything else. On other '
                'Canopan worlds, the living workforce performs the skilled labour and the '
                'shells perform the manual labour. On Serenath, the optimisation has been '
                'pushed further: the shells perform all labour that the living find '
                'unpleasant, tedious, or merely inconvenient. The cleaning, the maintenance, '
                'the construction, the waste processing, the agricultural work, the '
                'manufacturing, the logistics -- all of it is shell work on Serenath. The '
                'living population works only in roles that are intellectually stimulating, '
                'creatively fulfilling, or socially rewarding. The unpleasant work does not '
                'exist in a living person\'s experience because the shells absorb it '
                'entirely.\n\n'
                'The result is a civilisation of extraordinary leisure and refinement. The '
                'arts flourish. The research institutions produce excellent science. The '
                'cultural output is sophisticated and varied. The population is educated, '
                'healthy, and genuinely happy in a way that is measurable and not faked. '
                'Serenath produces the cluster\'s best artists, its most innovative '
                'researchers, and its most contented citizens. The living population on '
                'Serenath has more free time, less stress, and longer lives than any other '
                'living population in the outer systems.\n\n'
                'The shells on Serenath are kept out of sight with a thoroughness that '
                'exceeds even Sovrath. The infrastructure is designed so that the shell '
                'workforce operates in parallel -- separate transit networks, separate '
                'access corridors, separate work schedules timed so that the living never '
                'encounter the dead. The cities are designed with dual architecture: the '
                'visible city for the living, clean and beautiful, and the invisible city '
                'beneath and behind it for the shells, functional and lightless. The '
                'separation is so complete that children on Serenath can grow to adulthood '
                'without ever seeing a shell, and many do. The comfort is total. The cost '
                'is hidden. The arrangement is the Canopan model perfected.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Lanthery',
            short_description='A second world of similar quality -- warmer, coastal, and the cluster\'s premier destination for the Canopan elite who want beauty without the reminder of what sustains it.',
            long_description=(
                'Lanthery is the system\'s second habitable world -- warmer than Serenath, '
                'with extensive coastlines, tropical forests, and a climate that has been '
                'engineered for pleasure. The planet is the cluster\'s luxury destination '
                '-- where the Canopan elite come when they want beauty, warmth, and the '
                'complete absence of any reminder that their civilisation is built on '
                'reanimated labour.\n\n'
                'The shell infrastructure on Lanthery is the most invisible in the cluster. '
                'The shells that maintain the resorts, the estates, and the pristine '
                'landscapes operate entirely underground and at night. The surface of '
                'Lanthery during the day is a world without shells -- maintained to '
                'perfection by a workforce that is never seen, producing an illusion of '
                'effortless beauty that the visitors enjoy without questioning how the '
                'gardens are tended, how the beaches are cleaned, how the buildings are '
                'maintained. The illusion is the product.\n\n'
                'The Canopan aristocracy maintains estates on Lanthery -- properties that '
                'have been held by the same families for centuries because the families do '
                'not die. The estates are grand, the grounds are immaculate, and the staff '
                'are shells that the owners have never seen because the estate management '
                'systems ensure that the shell maintenance crews complete their work before '
                'the owners wake. The aristocrats live in houses that clean themselves, '
                'gardens that tend themselves, and a world that maintains itself, and the '
                'fiction is so complete that some of the younger aristocrats -- the ones '
                'who have never left Lanthery -- genuinely do not understand that the '
                'maintenance requires labour at all.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Perdane',
            short_description='The world beneath -- where the shell workforce that sustains Serenath and Lanthery is managed, maintained, and replaced in facilities the living population never visits.',
            long_description=(
                'Perdane is the system\'s working world -- a colder, less hospitable planet '
                'that houses the management infrastructure for the shell workforce that '
                'sustains Serenath and Lanthery\'s quality of life. The shell logistics -- '
                'procurement, processing, deployment, maintenance, and the replacement '
                'cycle that keeps the workforce functional -- are all managed from Perdane. '
                'The living staff on Perdane are the people who make the invisible city '
                'work: the logistics coordinators who schedule the shell shifts, the '
                'technicians who repair malfunctioning shells, and the managers who ensure '
                'that the separation between the living and the dead on the other worlds '
                'is maintained to the standard that Naos demands.\n\n'
                'The living population of Perdane is aware of the irony. They live on the '
                'worst world in the system so that the populations of Serenath and Lanthery '
                'can live on the best ones without seeing what makes their comfort possible. '
                'The Perdane workers are well-paid -- the Emperor of Naos understands that '
                'the people who manage the illusion must be compensated enough not to '
                'resent it. The compensation is generous. The resentment exists anyway, '
                'expressed in a dry humour about the beautiful worlds they maintain and '
                'the functional one they inhabit. The workers on Perdane call themselves '
                'the stagehands, and the name has stuck.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Lustren Station',
            short_description='The system\'s orbital port -- beautiful, immaculate, and the first impression that tells arriving visitors they have entered a civilisation that has solved the problem of discomfort.',
            long_description=(
                'Lustren Station is Naos\'s primary orbital facility -- and it is, '
                'deliberately, the most beautiful station in the Canopus cluster. The '
                'design is elegant. The materials are the finest available. The public '
                'spaces are art -- curated installations, living gardens, and architectural '
                'details that reflect centuries of continuous refinement by designers who '
                'serve an Emperor with exacting aesthetic standards.\n\n'
                'The station is immaculate. The cleaning is invisible. The shells that '
                'maintain the station work in the service corridors that the public spaces '
                'are designed to conceal, and the timing is so precise that a visitor can '
                'spend a week on Lustren Station without seeing a single shell, a single '
                'cleaner, or a single piece of evidence that maintenance occurs. The '
                'station simply is: beautiful, clean, and apparently self-sustaining, as '
                'though the elegance is a natural property of the materials rather than the '
                'product of dead hands working in the dark.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Respleth',
            short_description='A gas giant with fuel processing -- the one facility in the system where the working reality is visible, because fuel processing cannot be performed by the dead.',
            long_description=(
                'Respleth is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The fuel operations are staffed by '
                'living workers, as standard, and the posting is unremarkable by the '
                'standards of the cluster. What makes Respleth notable is that it is the '
                'one facility in Naos where work is visible -- where the living can see '
                'that labour occurs, that things do not maintain themselves, that the '
                'comfort of the inhabited worlds is produced rather than inherent.\n\n'
                'Visitors to Respleth\'s moons from Serenath sometimes express surprise '
                'at the sight of people working -- actual living people performing physical '
                'tasks. The fuel workers find this reaction fascinating and depressing in '
                'equal measure. The people on Serenath have been so thoroughly insulated '
                'from the reality of labour that the sight of a living person working is '
                'surprising. The fuel workers return to their shifts and do not discuss '
                'the implications.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Susthen',
            short_description='An agricultural world feeding the system -- productive, shell-operated, and managed from Perdane because the food production is part of the infrastructure the living never see.',
            long_description=(
                'Susthen is the system\'s agricultural world -- fertile, productive, and '
                'farmed entirely by shells under management from Perdane. The agricultural '
                'operations are part of the invisible infrastructure: the food arrives in '
                'Serenath\'s markets and Lanthery\'s restaurants without any visible '
                'connection to the fields that produced it or the shells that worked those '
                'fields. The supply chain is designed to be invisible -- the food is '
                'harvested, processed, packaged, and delivered without the living population '
                'encountering any stage of the production.\n\n'
                'The Emperor of Naos considers the agricultural invisibility the system\'s '
                'finest achievement. On other worlds, the food supply is at least '
                'acknowledged as something that requires effort. On Naos, the food appears '
                'in the markets as though it grew there. The fiction is complete. The '
                'living eat without knowing where the food came from, who grew it, or what '
                'the growers were. The Emperor considers this the definition of civilisation.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The cluster\'s paradise -- ten billion people in a civilisation of extraordinary comfort, sustained by a shell workforce so thoroughly hidden that the living have forgotten labour exists.',
    long_description=(
        'Naos is the Canopan model perfected. Ten billion people living in conditions '
        'that rival the best inner-system worlds -- clean cities, excellent '
        'infrastructure, superb healthcare, flourishing arts, and a quality of life '
        'that is measurably outstanding. The living population works only in roles '
        'that are stimulating, fulfilling, or rewarding. The unpleasant work does not '
        'exist in a living person\'s experience because the shells absorb it entirely.\n\n'
        'The shell workforce is the most thoroughly hidden in the cluster. Serenath\'s '
        'dual architecture -- the visible city for the living and the invisible city '
        'for the dead -- ensures that the two populations never encounter each other. '
        'Lanthery\'s luxury estates are maintained by shells the owners have never '
        'seen. Children grow to adulthood without seeing a shell. The separation is '
        'so complete that the living have not learned to ignore the shells, as on '
        'Phaet, or to normalise them, as on Turais. They have simply never '
        'encountered them. The comfort is total. The cost is invisible.\n\n'
        'Perdane is where the illusion is managed -- the working world where the '
        'shell logistics are coordinated by staff who call themselves the stagehands '
        'and who live on the system\'s worst world so that the others can live on its '
        'best. The compensation is generous. The resentment is real. The irony is not '
        'lost on the people who maintain a paradise they are not invited to enjoy.\n\n'
        'The star is an O-type blue supergiant -- one of the most luminous in the '
        'galaxy, 800,000 times Sol\'s output. The atmospheric engineering that filters '
        'its intensity to comfortable levels is itself a metaphor the Emperor of Naos '
        'would appreciate: even the light is managed, softened, made pleasant. '
        'Everything in Naos is made pleasant. The question of what unpleasantness is '
        'concealed to achieve it is not asked on Serenath, where the population has '
        'never had reason to ask, and is answered on Perdane, where the stagehands '
        'know exactly what is behind the curtain.'
    ),
    cluster=StarClusters.CANOPUS,
)

SUHAIL = System(
    name='Suhail',
    star='Blue-white subgiant (B2.5IV), approximately 7,000 times Sol luminosity -- a hot, bright star illuminating a system that the brightness does nothing to improve',
    population=4_000_000_000,
    distance_to_sol=570.0,
    stellar_objects=[
        StellarObject(
            name='Karshane',
            short_description='The cluster\'s most dangerous inhabited world -- two billion people in a system where piracy is the economy, crime is the culture, and the shells are weapons.',
            long_description=(
                'Karshane is what happens when a Canopan system has no resource the cluster '
                'needs and no industry worth protecting. The planet is habitable -- warm, '
                'fertile enough to feed itself -- but it has no strategic minerals, no '
                'industrial capacity worth the name, and no position on the trade routes '
                'that would make legitimate commerce viable. What Karshane has is people, '
                'ships, and a willingness to take what legitimate commerce does not provide.\n\n'
                'The piracy in Suhail is not the individual raiding that Lesath in the '
                'Antares cluster produces. It is organised, professional, and run by '
                'criminal syndicates whose operations have the structure and sophistication '
                'of corporations. The syndicates operate fleets -- not the improvised armed '
                'traders of Lesath but purpose-built raiding vessels, crewed by professionals '
                'who treat piracy as a career rather than an act of desperation. The '
                'syndicates have territories, agreements, and the hierarchical organisation '
                'that sustained criminal enterprise requires.\n\n'
                'The shells are what makes Suhail\'s piracy distinctive. The syndicates '
                'use shells as shock troops -- boarding parties composed of reanimated '
                'bodies that are sent onto captured vessels first, absorbing the defensive '
                'fire that would kill living pirates. A shell boarding party does not take '
                'cover. It does not flinch. It walks into weapons fire and continues '
                'advancing until it is destroyed or the defenders are overwhelmed. The '
                'living pirates follow behind the shell wave, entering the ship after the '
                'resistance has been broken by bodies that feel nothing and stop for nothing. '
                'The tactic is effective and terrifying. Crews who have been boarded by '
                'shell wave attacks describe the experience in terms that the military '
                'psychologists on Halstrom recognise as combat trauma.\n\n'
                'The Emperor of Suhail is a fiction. The title exists -- someone holds it, '
                'someone attends the council on Vethane -- but the holder is a figurehead '
                'installed by whichever syndicate is currently dominant. The real power in '
                'Suhail is the syndicate leaders, who have been reanimated enough times to '
                'be functionally immortal and who have used that immortality to build '
                'criminal empires of extraordinary durability. A syndicate leader who has '
                'been running operations for three centuries is not overthrown easily. The '
                'younger rivals who try tend to die. The syndicate leaders also die, '
                'occasionally, but they come back. The rivals do not, because the syndicate '
                'leaders control the reanimation facilities and the rivals do not.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Dremwick',
            short_description='A second world controlled by a rival syndicate -- the competition between Karshane\'s syndicates and Dremwick\'s is the system\'s closest thing to politics.',
            long_description=(
                'Dremwick is the system\'s second inhabited world -- cooler, rockier, and '
                'controlled by syndicates that operate independently of Karshane\'s criminal '
                'hierarchy. The rivalry between the two worlds is Suhail\'s internal '
                'politics: not ideology or governance but competing criminal organisations '
                'disputing territory, trade routes, and the share of plunder that each '
                'world\'s syndicates claim.\n\n'
                'Dremwick\'s syndicates specialise in the aspects of piracy that Karshane\'s '
                'syndicates consider beneath them: the hijacking of shell transports. The '
                'bodies in transit from Phaet\'s processing facilities to their destinations '
                'across the cluster are valuable cargo -- a transport carrying a thousand '
                'functional shells represents an asset that the syndicates can use directly '
                'as workforce or sell on the black market. The hijacking of shell transports '
                'is Suhail\'s most profitable speciality, and the cluster\'s labour '
                'corporations have calculated the cost of the losses and added it to the '
                'price of shells as a line item in the budget.\n\n'
                'The syndicate leaders on Dremwick are, like their counterparts on Karshane, '
                'centuries-old figures who have been restored often enough to be effectively '
                'immortal. The longevity produces criminal leaders of extraordinary '
                'cunning and patience -- people who plan operations on timescales that '
                'mortal criminals cannot manage and who hold grudges that outlast '
                'generations. A betrayal against a Dremwick syndicate leader is not '
                'forgotten in years or decades. It is remembered for centuries, and the '
                'response comes when the leader decides the moment is right, which may be '
                'long after the betrayer has forgotten the original offence.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='The Wrack',
            short_description='An orbital debris field and black market -- where stolen goods are traded, hijacked ships are stripped, and the syndicates conduct business under rules that only criminals enforce.',
            long_description=(
                'The Wrack is Suhail\'s equivalent of Lesath\'s Scrapfield -- a zone of '
                'orbital space above Karshane where the accumulated wreckage of piracy '
                'collects and where the system\'s black-market commerce is conducted. The '
                'Wrack is larger and more organised than the Scrapfield: the syndicates '
                'maintain it as a trading venue with the efficiency that professional '
                'criminal enterprise produces.\n\n'
                'The trade in the Wrack covers everything that piracy generates: stolen '
                'cargo, hijacked vessels, captured shells, weapons, and the intelligence '
                'on shipping routes and patrol schedules that the syndicates sell to each '
                'other when the price is right. The Wrack also hosts the transactions that '
                'connect Suhail\'s criminal economy to the legitimate cluster: the fences '
                'who move stolen goods into legal commerce, the brokers who launder the '
                'profits through the financial systems on Mirzam, and the intermediaries '
                'who arrange the deals that the syndicates cannot conduct directly because '
                'even in the Canopus cluster, appearing to do business with pirates is '
                'politically inconvenient.\n\n'
                'The rules in the Wrack are syndicate-enforced: no attacking during trades, '
                'contracts honoured or the violator is blacklisted by all syndicates, and '
                'the understanding that the Wrack is neutral ground where the competition '
                'between syndicates is suspended. The rules work because the syndicates '
                'need them to work, and the enforcement -- which includes killing the '
                'violator and then not reanimating them, the most permanent punishment '
                'available in Canopan space -- is decisive.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Shardholm',
            short_description='A cold, barren world used as a staging area for raiding operations -- where the fleets assemble and the shell boarding parties are loaded.',
            long_description=(
                'Shardholm is a cold, barren world in the outer system that the syndicates '
                'use as a staging area for raiding operations. The surface installations '
                'are crude -- landing pads, supply depots, and the shell storage facilities '
                'that hold the boarding parties between operations. The shell boarding '
                'troops are kept on Shardholm in standby -- hundreds of thousands of '
                'reanimated bodies standing in dark warehouses, waiting to be loaded onto '
                'the raiding vessels and sent into the breach of the next captured ship.\n\n'
                'The staging operations on Shardholm are where the syndicates\' '
                'professionalism is most visible. The operations are planned with military '
                'precision -- target identification, route analysis, timing calculations, '
                'and the coordination of multiple vessels that complex piracy requires. '
                'The syndicate planners who work from Shardholm\'s command facilities are '
                'former military officers, intelligence analysts, and logistics '
                'professionals who found that the criminal pay was better and the moral '
                'constraints were fewer. The operations they plan are as sophisticated as '
                'anything the Canopan fleet produces. The targets are different. The '
                'methods are similar.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Gorren',
            short_description='A gas giant where fuel is taken by force of presence -- the syndicates control the processing and charge whatever the traffic will bear.',
            long_description=(
                'Gorren is the system\'s gas giant -- fuel processing on its moons '
                'controlled not by the Emperor\'s administration but by the syndicates who '
                'claimed the installations decades ago and have held them since. The fuel '
                'is processed competently -- the syndicates need fuel for their own vessels '
                'and understand that functional infrastructure is worth maintaining. The '
                'pricing, however, is not competitive. Ships that enter Suhail for any '
                'reason -- including ships that were forced into the system by pirate '
                'interdiction -- pay whatever the syndicates charge for fuel, and the '
                'syndicates charge what the desperation of the buyer will bear.\n\n'
                'The fuel workers on Gorren\'s moons are syndicate employees -- living '
                'workers who accepted the posting because the pay is excellent and the '
                'alternative employment options in Suhail are worse. The workers process '
                'the fuel, collect the inflated fees, and do not ask questions about the '
                'ships that dock with battle damage and cargo bays full of goods that '
                'clearly belonged to someone else an hour ago.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Sutton',
            short_description='An agricultural world that barely functions -- farmed by shells under syndicate management that invests the minimum required because the real money is in piracy.',
            long_description=(
                'Sutton is the system\'s agricultural world -- warm, potentially productive, '
                'and farmed at a fraction of its capacity because the syndicates that '
                'control the system invest in piracy rather than agriculture. The food '
                'production on Sutton is sufficient to prevent starvation and not much more. '
                'The farming is shell-operated under minimal living management, and the '
                'management is minimal because the syndicates do not consider food '
                'production a priority.\n\n'
                'The deficit is covered by piracy -- raided food shipments from Alsephina\'s '
                'freighters supplement the local production, and the irony of a system that '
                'steals its food supply rather than growing it is noted by the few '
                'legitimate observers who study Suhail\'s economy and is not noted by the '
                'syndicates, who consider food a logistical problem rather than a moral one.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The cluster\'s wound -- four billion people in a system run by criminal syndicates who use shells as weapons and immortality as leverage.',
    long_description=(
        'Suhail is the Canopus cluster\'s criminal heart. The system has no strategic '
        'resources, no significant industry, and no position on the trade routes that '
        'would support legitimate commerce. What it has is organised piracy -- '
        'criminal syndicates that operate fleets of purpose-built raiding vessels, '
        'crewed by professionals who treat piracy as a career, and backed by a '
        'distinctive weapon: shell boarding parties. The reanimated shock troops that '
        'the syndicates send onto captured vessels walk into weapons fire without '
        'flinching, absorb the defensive fire, and overwhelm the resistance so that '
        'the living pirates can follow into a cleared ship.\n\n'
        'The syndicates are run by leaders who have been reanimated often enough to be '
        'functionally immortal -- centuries-old figures of extraordinary cunning who '
        'plan on timescales mortal criminals cannot manage and hold grudges that '
        'outlast generations. The Emperor of Suhail is a figurehead installed by '
        'whichever syndicate is currently dominant. The real power is the syndicate '
        'leaders, and their power is sustained by the same mechanism that sustains the '
        'legitimate emperors: control of the reanimation facilities. A leader who '
        'controls who comes back and who stays dead is a leader who cannot be '
        'permanently overthrown.\n\n'
        'The Wrack -- the orbital debris field and black market above Karshane -- is '
        'where the criminal economy interfaces with the legitimate one. Stolen goods '
        'are fenced, profits are laundered through Mirzam\'s financial systems, and '
        'the hijacked shell transports that are Suhail\'s most profitable speciality '
        'are sold to buyers who do not ask where the shells came from. The cluster\'s '
        'labour corporations have priced the piracy losses into their budgets. The '
        'council has calculated the cost of pacifying Suhail and decided it exceeds '
        'the cost of the losses. The syndicates continue. The shells continue to walk '
        'into weapons fire. The dead are the weapons, and the weapons do not care.'
    ),
    cluster=StarClusters.CANOPUS,
)

CNP_2190 = System(
    name='CNP-2190',
    star='Red dwarf (M1V), approximately 0.1 times Sol luminosity -- dim and stable, requiring extensive terraforming to make any world habitable',
    population=0,
    distance_to_sol=520.0,
    stellar_objects=[
        StellarObject(
            name='CNP-2190-a',
            short_description='A world being terraformed almost entirely by shells -- atmospheric processors operated by the dead, under the supervision of a living staff so small it fits on a single station.',
            long_description=(
                'CNP-2190-a is a world in the process of being made habitable. The planet '
                'sits in the habitable zone of the dim red dwarf -- cold, thin-atmosphered, '
                'with surface water locked in polar ice caps and conditions that are '
                'decades of terraforming away from supporting unassisted human life. The '
                'atmospheric processors are running. The ice is being melted. The soil is '
                'being engineered. The work is being done.\n\n'
                'The work is being done by shells. The terraforming operation on CNP-2190-a '
                'is the cluster\'s most ambitious application of reanimated labour -- a '
                'planet-scale engineering project conducted almost entirely by a workforce '
                'that does not need the atmosphere it is creating, does not need the warmth '
                'it is generating, and does not need the water it is releasing from the '
                'ice. The shells operate the atmospheric processors. They maintain the '
                'equipment. They dig the channels that will become rivers when the ice '
                'melts. They prepare the soil for crops that will be planted decades from '
                'now by people who have not yet been born. The shells do this work in an '
                'atmosphere they cannot breathe, in temperatures that would kill a living '
                'worker in hours, on a world that is hostile to every form of life -- and '
                'the shells are not alive, so the hostility is irrelevant.\n\n'
                'The shell workforce on CNP-2190-a is enormous -- hundreds of thousands of '
                'units deployed across the planet\'s surface, operating the machinery, '
                'performing the physical labour, and degrading in the cold and the thin air '
                'at a rate that the supply ships from Kethra are calibrated to replace. The '
                'supply runs are regular: transports arrive carrying fresh shells in '
                'standby, offload them at the surface depots, and collect the non-functional '
                'units for recycling. The cycle is continuous. The planet is being built by '
                'a workforce that is consumed by the building.\n\n'
                'The living presence on CNP-2190-a is minimal. A monitoring station in '
                'orbit houses a staff of fewer than two hundred -- engineers who oversee '
                'the terraforming programme, logistics coordinators who manage the shell '
                'deployment, and the systems operators who monitor the atmospheric '
                'processors and adjust the parameters as the terraforming progresses. The '
                'living staff do not go to the surface. The surface is not for them -- not '
                'yet. The surface is for the shells, and the shells are building a world '
                'that the shells will never inhabit.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-2190-b',
            short_description='A barren moon used as the shell supply depot -- where the transports from Kethra offload fresh units and collect the broken ones for recycling.',
            long_description=(
                'CNP-2190-b is a small, airless moon orbiting the world being terraformed '
                '-- repurposed as the operation\'s supply depot. The surface installations '
                'are simple: landing pads for the supply transports, storage facilities for '
                'the shells in standby awaiting deployment, and the collection bays where '
                'the non-functional shells are gathered for return to Kethra\'s recycling '
                'facilities.\n\n'
                'The depot is automated. The shells that manage the depot\'s operations -- '
                'unloading transports, moving units to storage, loading non-functional units '
                'for return -- are themselves shells, supervised remotely from the orbital '
                'station. The depot is a facility where the dead manage the dead: shells '
                'unpacking shells, shells storing shells, shells loading the broken shells '
                'onto the transports that will carry them back to be processed into '
                'something else. No living person has visited the depot\'s surface in '
                'years. The automation is sufficient. The living staff monitor from orbit '
                'and intervene only when the automation fails, which is rarely, because '
                'the tasks are simple enough for shells to manage without error.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-2190-c',
            short_description='A small gas giant -- unprocessed, unused, designated as the future colony\'s fuel source in a development plan that assumes the terraforming will succeed.',
            long_description=(
                'CNP-2190-c is a small gas giant in the outer system -- catalogued in the '
                'development plan as the future colony\'s fuel source. No processing '
                'facilities have been built. The supply transports that service the '
                'terraforming operation carry their own fuel from the cluster\'s established '
                'systems, because the traffic volume does not justify local processing. '
                'The gas giant waits in the development plan alongside the agricultural '
                'schedules, the population targets, and the infrastructure projections that '
                'will become relevant when the terraforming is complete -- in decades, if '
                'the funding continues and the shell supply holds.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-2190-d',
            short_description='A frozen outer body -- surveyed and ignored, one more entry in a development plan that is focused entirely on the world the shells are building.',
            long_description=(
                'CNP-2190-d is a frozen body in the far outer system -- ice and rock, '
                'catalogued in the initial survey and not revisited. The development plan '
                'mentions it as a potential source of water ice if the polar melt on '
                'CNP-2190-a proves insufficient, but the current projections suggest that '
                'the planet\'s own ice reserves are adequate. CNP-2190-d sits in the '
                'plan as a contingency, unvisited and unused, while the real work happens '
                'on the inner world where the shells dig channels in the frozen soil and '
                'the atmosphere thickens by fractions of a percent per year.'
            ),
            population=0,
        ),
    ],
    short_description='A world being built by the dead -- shells terraforming a planet they will never inhabit, supervised by a living staff of fewer than two hundred.',
    long_description=(
        'CNP-2190 is a terraforming operation conducted almost entirely by shells. '
        'The world being built -- a cold, thin-atmosphered planet orbiting a dim red '
        'dwarf -- is decades from habitability. The atmospheric processors are running. '
        'The ice is being melted. The soil is being engineered. The channels that will '
        'become rivers are being dug. All of it is being done by a shell workforce of '
        'hundreds of thousands, operating in conditions that would kill living workers '
        'in hours, on a world that is hostile to every form of life and therefore '
        'perfectly suited to a workforce that is not alive.\n\n'
        'The living presence is minimal -- fewer than two hundred staff on an orbital '
        'monitoring station, overseeing the terraforming programme and managing the '
        'shell logistics from a distance. The living do not visit the surface. The '
        'surface is for the shells, and the shells are building a world for people '
        'who have not yet been born, in an atmosphere they cannot breathe, in cold '
        'they cannot feel, with a purpose they cannot comprehend.\n\n'
        'The supply runs from Kethra are regular -- fresh shells in, broken shells '
        'out. The depot on CNP-2190-b is automated: shells managing shells, the dead '
        'unpacking the dead. The operation is the Canopan labour model at its most '
        'distilled: a planet-scale engineering project performed by a disposable '
        'workforce that is consumed by the work and replaced from a supply chain that '
        'does not distinguish between building a world and filling a factory.\n\n'
        'The terraforming will take decades. The shells will build the world. The '
        'people who eventually colonise it will walk on soil prepared by dead hands, '
        'breathe air processed by dead lungs that never needed it, and drink water '
        'released from ice by workers who could not feel the cold. The colony will '
        'be the cluster\'s newest world, built from nothing by the labour of nothing, '
        'and the colonists will not think about how it was made because nobody in the '
        'Canopus cluster thinks about that.'
    ),
    cluster=StarClusters.CANOPUS,
)

CNP_3318 = System(
    name='CNP-3318',
    star='White dwarf (DA3), approximately 0.01 times Sol luminosity -- the collapsed remnant of a dead star, dim and dense, illuminating nothing that the weapons have not already destroyed',
    population=0,
    distance_to_sol=700.0,
    stellar_objects=[
        StellarObject(
            name='CNP-3318-a',
            short_description='The primary weapons testing target -- a rocky world whose surface has been cratered, melted, and restructured by decades of ordnance that was too dangerous to test anywhere inhabited.',
            long_description=(
                'CNP-3318-a is the primary target. The world was never habitable -- a '
                'cold, airless rock orbiting a white dwarf, with no atmosphere, no water, '
                'and no geological features that would have justified colonisation or '
                'terraforming even if the cluster had needed another world. The assessment '
                'that designated CNP-3318 as a weapons testing range noted that the system '
                'had no value for any purpose other than the one it was assigned, and the '
                'assessment has been vindicated by what the testing has done to the planet.\n\n'
                'The surface of CNP-3318-a is no longer recognisable as a natural '
                'formation. Decades of weapons testing have cratered, melted, vitrified, '
                'and in some areas completely restructured the surface geology. The impact '
                'sites overlap -- older craters intersected by newer ones, vitrified plains '
                'shattered by subsequent detonations, and the deeper scars where the '
                'heavier ordnance has punched through the crust into the mantle. The '
                'weapons tested here are the ones that the fleet command at Aspid '
                'considers too dangerous for inhabited space: planet-scale bombardment '
                'systems, experimental warheads, and the weapons designed to crack the '
                'hulls of MERIT\'s heaviest fortifications.\n\n'
                'The testing is conducted by automated systems deployed from Aspid -- '
                'weapons platforms placed in orbit, target arrays on the surface, and the '
                'sensor packages that record the detonation characteristics. The data is '
                'transmitted to Aspid\'s fleet command for analysis. No living person is '
                'present during a test. The ordnance being tested does not leave survivors '
                'at the ranges being measured, and the safety margin is the entire system.\n\n'
                'The planet has become, inadvertently, a geological record of the cluster\'s '
                'weapons development. The oldest craters on the surface were made by '
                'ordnance that the current generation of weapons engineers considers '
                'primitive. The newest craters are made by weapons that the engineers '
                'consider adequate and that the fleet command considers a start. The '
                'progression from oldest to newest is visible in the scale of the damage: '
                'the craters get larger, deeper, and more thorough as the weapons improve.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-3318-b',
            short_description='A smaller rocky body used for testing weapons designed to destroy ships rather than planets -- target hulls placed on the surface and in orbit.',
            long_description=(
                'CNP-3318-b is a smaller rocky body used as the range for anti-ship weapons '
                'testing. The surface is scattered with the remains of decommissioned hulls '
                '-- old warships, retired freighters, and purpose-built target structures '
                'placed to simulate the profiles of MERIT vessels. The weapons tested here '
                'are the ship-killing ordnance that the fleet carries: torpedoes, kinetic '
                'impactors, the close-range weapons designed to breach hull armour and the '
                'long-range weapons designed to cripple a ship before it reaches engagement '
                'distance.\n\n'
                'The orbital space around CNP-3318-b contains target hulls as well -- '
                'decommissioned vessels placed in stable orbits to simulate space combat '
                'conditions. The weapons are tested against these targets under conditions '
                'as close to real engagement as possible: the target hulls are equipped '
                'with the shield profiles and armour ratings that MERIT intelligence '
                'estimates for current-generation MERIT warships. The testing determines '
                'whether the weapons will perform as designed against an enemy that builds '
                'lighter, faster ships with living crews who die when the hull is breached '
                'and who cannot be brought back.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Residue',
            short_description='The contaminated orbital space -- weapons debris, unexploded ordnance, and the radiation from decades of testing that makes the system hazardous for unshielded vessels.',
            long_description=(
                'The Residue is the designation for the contaminated space that fills the '
                'inner system -- the accumulated debris from decades of weapons testing. '
                'Fragments of destroyed target hulls, unexploded ordnance that failed to '
                'detonate and drifts on unpredictable trajectories, and the radiation '
                'signatures from experimental warheads that produced effects the engineers '
                'are still studying. The contamination makes transit through the inner '
                'system hazardous for any vessel without military-grade shielding, which '
                'is why civilian traffic is prohibited and why the navigation charts mark '
                'CNP-3318 with a hazard designation that the pilots take seriously.\n\n'
                'The unexploded ordnance is the most immediate danger. Weapons that failed '
                'during testing -- guidance malfunctions, detonator failures, the prototypes '
                'that did not work as intended -- drift through the system on orbits that '
                'are tracked when possible and avoided when not. The catalogue of '
                'unexploded ordnance in CNP-3318 is maintained by Aspid\'s weapons '
                'engineers and runs to thousands of entries, each one a weapon that was '
                'designed to destroy something significant and that is waiting in the dark '
                'for a collision that nobody wants.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-3318-c',
            short_description='A frozen outer body beyond the testing range -- the monitoring post where the automated sensor systems that record the tests are maintained.',
            long_description=(
                'CNP-3318-c is a frozen body in the outer system -- far enough from the '
                'testing range that it is outside the contamination zone, and used as the '
                'base for the automated monitoring systems that record the weapons tests. '
                'The sensor arrays on CNP-3318-c observe the detonations, record the '
                'yields, and transmit the data to Aspid for analysis. The monitoring post '
                'is maintained by shells -- the radiation environment in the inner system '
                'occasionally produces spikes that reach the outer body, and the shells '
                'that maintain the sensors are replaced on a schedule that accounts for '
                'the degradation.\n\n'
                'The monitoring post is the only permanent installation in the system. '
                'Everything else is targets, debris, and the weapons that created both. '
                'The shells that tend the sensors are the system\'s only inhabitants in '
                'the loosest possible use of the word, and even that use is generous for '
                'beings that do not know where they are and do not know what they are '
                'recording.'
            ),
            population=0,
        ),
    ],
    short_description='The cluster\'s weapons range -- a dead system orbiting a dead star, cratered and contaminated by decades of testing the ordnance too dangerous for inhabited space.',
    long_description=(
        'CNP-3318 is one jump from Aspid and exists for one purpose: testing the '
        'weapons that the Canopan fleet considers too dangerous to test anywhere '
        'people live. The system orbits a white dwarf -- the collapsed remnant of a '
        'dead star -- and was selected because it had no value for any other purpose. '
        'No habitable worlds. No terraforming potential. No resources worth '
        'extracting. The assessment that designated it a weapons range noted that the '
        'system\'s only asset was its worthlessness.\n\n'
        'The testing has been continuous for decades. CNP-3318-a, the primary target '
        'world, has been cratered, melted, and restructured by planet-scale '
        'bombardment systems, experimental warheads, and the ordnance designed to '
        'crack MERIT\'s heaviest fortifications. The surface is a geological record of '
        'the cluster\'s weapons development -- the craters get larger and deeper as '
        'the weapons improve. CNP-3318-b hosts anti-ship testing against target hulls '
        'simulating MERIT vessel profiles. The Residue -- the contaminated inner '
        'system -- drifts with debris, radiation, and thousands of unexploded '
        'ordnance entries waiting in the dark for collisions nobody wants.\n\n'
        'No living person is present during a test. The testing is automated, the data '
        'transmitted to Aspid. The monitoring post on the frozen outer body is tended '
        'by shells. The system is a dead place made deader by the weapons designed to '
        'make other places dead, orbiting a star that died long before the cluster '
        'decided to use its corpse as a firing range.'
    ),
    cluster=StarClusters.CANOPUS,
)

CNP_0871 = System(
    name='CNP-0871',
    star='Magnetar -- a neutron star with a magnetic field approximately one quadrillion times Earth\'s, producing irregular bursts of X-ray and gamma radiation that make the system lethal to unshielded electronics and biological life',
    population=0,
    distance_to_sol=550.0,
    stellar_objects=[
        StellarObject(
            name='CNP-0871-a',
            short_description='A dense remnant world in close orbit -- its surface magnetised to the point where the rock itself has aligned with the magnetar\'s field, producing geological formations that should not exist.',
            long_description=(
                'CNP-0871-a is a small, dense body in a close orbit around the magnetar -- '
                'a remnant of whatever system existed before the star collapsed. The planet '
                'survived the supernova that created the magnetar, but the magnetic field '
                'has transformed it into something that the survey team\'s geologists '
                'struggled to describe in conventional terms. The rock is magnetised. The '
                'entire crust has aligned with the magnetar\'s field over millennia, '
                'producing crystalline structures in the mineral formations that follow '
                'magnetic field lines rather than geological strata. The surface is covered '
                'in formations that rise in arcs and spirals that trace the invisible '
                'field -- spires of magnetised rock that look sculpted rather than formed, '
                'curving toward the star in patterns that are beautiful and profoundly '
                'wrong.\n\n'
                'The survey was conducted by a single hardened drone that lasted forty '
                'minutes on the surface before the magnetic field stripped its shielding '
                'and destroyed its electronics. The data returned in those forty minutes '
                'was enough to confirm the geological anomalies and insufficient to explain '
                'them. A follow-up mission has been proposed by the geologists who reviewed '
                'the data and rejected by the funding authorities who reviewed the cost of '
                'hardened drones. The planet remains the most scientifically interesting '
                'and least accessible body in the cluster.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-0871-b',
            short_description='A frozen outer body -- far enough from the magnetar that the field is weaker, but the irregular radiation bursts reach here with enough intensity to sterilise the surface periodically.',
            long_description=(
                'CNP-0871-b is a frozen body in the outer system -- distant enough that the '
                'magnetic field is attenuated to levels that hardened equipment could '
                'theoretically survive for extended periods. The theory is complicated by '
                'the magnetar\'s irregular radiation bursts. Unlike a pulsar\'s predictable '
                'rotation, the magnetar produces bursts at unpredictable intervals -- hours, '
                'days, or weeks apart, with no pattern that the astrophysicists have been '
                'able to identify. Each burst floods the system with X-ray and gamma '
                'radiation at intensities that vary from manageable to lethal, and the '
                'unpredictability means that any installation in the system must be built '
                'to survive the worst burst at any time.\n\n'
                'The survey team that catalogued CNP-0871-b spent three days in the outer '
                'system and experienced two bursts. The first was a minor event -- elevated '
                'radiation that the ship\'s shielding handled without difficulty. The second '
                'was a major event that nearly exceeded the ship\'s shielding capacity and '
                'produced radiation levels inside the hull that the crew\'s dosimeters '
                'registered as concerning. The crew departed immediately and recommended '
                'in their report that the system be classified as a radiation hazard with '
                'a strong advisory against prolonged presence. The recommendation was '
                'accepted. CNP-0871 is marked on the navigation charts with the same red '
                'hazard designation as ATR-0088, and pilots avoid it for the same reasons.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Magnetosphere',
            short_description='The magnetar\'s field itself -- a quadrillion times Earth\'s magnetic field, strong enough to distort atomic structure and lethal to any technology not specifically hardened against it.',
            long_description=(
                'The Magnetosphere is the defining feature of CNP-0871 -- the magnetic '
                'field produced by the magnetar, extending through the system at intensities '
                'that diminish with distance but remain hazardous far beyond the orbits of '
                'either body. The field is strong enough in the inner system to distort '
                'atomic structure in unshielded materials -- the crystalline alignment of '
                'CNP-0871-a\'s surface geology is a demonstration of what the field does to '
                'rock over time. What it does to electronics is faster and more destructive: '
                'unshielded systems fail within minutes, data storage is wiped, and the '
                'electromagnetic interference makes communication impossible at ranges '
                'where the field is strongest.\n\n'
                'The irregular radiation bursts compound the hazard. The magnetar produces '
                'starquakes -- seismic events in the neutron star\'s crystalline crust that '
                'release enormous bursts of X-ray and gamma radiation. The bursts are '
                'unpredictable. A ship transiting the outer system might experience nothing '
                'for days and then be struck by a burst intense enough to overwhelm '
                'military-grade shielding. The combination of the constant magnetic field '
                'and the unpredictable radiation bursts makes CNP-0871 one of the most '
                'dangerous natural environments in the cluster.\n\n'
                'The system cannot be inhabited. It cannot be terraformed. It cannot be '
                'mined, processed, or used for any purpose that requires a sustained '
                'presence. Even shells -- which tolerate radiation better than the living '
                'because they do not suffer from it, only degrade -- would be consumed '
                'too quickly to be economically viable. The magnetar has rendered the '
                'system useless by every measure that the cluster applies, and the cluster '
                'has responded by cataloguing it, marking it, and leaving it alone.'
            ),
            population=0,
        ),
    ],
    short_description='A magnetar system -- a neutron star with a magnetic field strong enough to restructure rock and radiation bursts intense enough to kill anything that stays too long.',
    long_description=(
        'CNP-0871 is a magnetar -- a neutron star with a magnetic field approximately '
        'one quadrillion times Earth\'s strength, producing a constant electromagnetic '
        'environment that destroys unshielded electronics and irregular bursts of X-ray '
        'and gamma radiation that can overwhelm even military-grade shielding. The '
        'system was surveyed briefly and catalogued as a natural hazard that cannot be '
        'inhabited, terraformed, mined, or used for any purpose.\n\n'
        'The inner body -- CNP-0871-a -- has been transformed by the magnetic field '
        'into something geologically unprecedented: rock whose crystalline structure '
        'has aligned with the field lines over millennia, producing formations that '
        'rise in arcs and spirals tracing the invisible field. The survey drone that '
        'recorded this lasted forty minutes before the field destroyed it. The data '
        'was enough to confirm the anomalies and insufficient to explain them.\n\n'
        'The outer body is reachable but unsafe. The survey team spent three days, '
        'experienced two radiation bursts -- one minor, one that nearly exceeded the '
        'ship\'s shielding -- and departed with a strong recommendation against '
        'prolonged presence. The bursts are unpredictable: starquakes in the neutron '
        'star\'s crystalline crust releasing energy at intervals that follow no '
        'pattern the astrophysicists have identified.\n\n'
        'CNP-0871 is marked in red on the navigation charts alongside ATR-0088. The '
        'two systems represent different flavours of stellar hostility -- the pulsar\'s '
        'constant, predictable sweep versus the magnetar\'s unpredictable violence -- '
        'but the practical conclusion is the same: the system is empty and will remain '
        'so because the star that occupies it makes everything else impossible. Even '
        'shells degrade too quickly. The magnetar has found the floor beneath which '
        'even disposable labour is not disposable enough.'
    ),
    cluster=StarClusters.CANOPUS,
)

CNP_5502 = System(
    name='CNP-5502',
    star='Yellow main sequence (G2V), approximately 1 times Sol luminosity -- a star almost identical to Sol, which is the detail that every report about this system mentions first',
    population=0,
    distance_to_sol=780.0,
    stellar_objects=[
        StellarObject(
            name='CNP-5502-a',
            short_description='A world in the habitable zone of a Sol-like star -- the most promising discovery the cluster has made in decades, and the furthest from anyone who could use it.',
            long_description=(
                'CNP-5502-a is the discovery that made the survey team\'s careers and the '
                'planning authority\'s headache. The world orbits a G2V star -- a yellow '
                'main sequence star almost identical to Sol in luminosity, temperature, '
                'and spectral class -- at a distance that places it squarely in the '
                'habitable zone. The preliminary readings are extraordinary: a nitrogen-'
                'oxygen atmosphere at roughly eighty percent of standard pressure, surface '
                'water covering approximately sixty percent of the planet, and temperature '
                'ranges that fall within the bounds of human comfort without terraforming.\n\n'
                'The planet may be habitable without intervention. The survey team, which '
                'arrived less than five years ago and is still conducting its assessment, '
                'has confirmed that the atmosphere is breathable -- thin, but breathable. '
                'The surface water is liquid and, in the samples the drones have returned, '
                'chemically compatible with human biology. The soil analysis is ongoing but '
                'the preliminary results suggest organic compounds that could support '
                'agriculture with minimal engineering. The survey team\'s lead geologist '
                'described the planet in the interim report as the best candidate for '
                'unassisted colonisation discovered since the expansion began.\n\n'
                'The problem is distance. CNP-5502 is the furthest system the cluster has '
                'reached -- at the end of a chain of jump links that places it farther '
                'from the cluster\'s core than any other discovered system. The jump chain '
                'is long and the links are hard -- the transit from the nearest inhabited '
                'system takes weeks and requires a ship capable of sustained independent '
                'operation. A colony at CNP-5502 would be the most isolated human '
                'settlement in the galaxy, further from support than any other inhabited '
                'world, dependent on a supply chain that stretches across jump links that '
                'a single disruption could sever.\n\n'
                'The council of emperors has received the interim reports with interest and '
                'has not authorised a colonisation programme. The distance is one concern. '
                'The cost is another. But the concern that the reports do not state and '
                'the council discusses privately is the precedent: a colony this far from '
                'the core, this difficult to supply, would need to be self-sustaining. '
                'Self-sustaining means independent reanimation capability. Independent '
                'reanimation capability means a population that does not depend on Placidus '
                'and does not answer to the council. The emperors who have spent centuries '
                'building a civilisation where immortality flows from the centre are not '
                'eager to create a colony that could survive without them.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-5502-b',
            short_description='A second habitable-zone world -- smaller, drier, but potentially terraformable, making the system a twin-world prospect that the planners find tantalising and the emperors find threatening.',
            long_description=(
                'CNP-5502-b is the system\'s second habitable-zone world -- smaller than '
                'CNP-5502-a, drier, with a thinner atmosphere and less surface water, but '
                'within the parameters that terraforming could address. The survey team '
                'has conducted orbital assessments but has not prioritised CNP-5502-b over '
                'the primary candidate -- the resources of a five-person geological team '
                'and a handful of drones are focused on the world that may not need '
                'terraforming at all.\n\n'
                'The existence of a second candidate makes the system more valuable and '
                'the political problem more acute. A twin-world system with a Sol-like '
                'star is the kind of discovery that colonial planners dream about. It is '
                'also the kind of discovery that makes emperors who have ruled for '
                'centuries uncomfortable, because a self-sustaining twin-world colony at '
                'the edge of known space is not a colony. It is the seed of a civilisation '
                'that does not need the one that planted it.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-5502-c',
            short_description='A large gas giant -- fuel processing potential that would support a colony\'s traffic, if a colony is ever authorised.',
            long_description=(
                'CNP-5502-c is a large gas giant in the outer system -- standard hydrogen-'
                'helium composition, extensive moon system, and the fuel processing '
                'potential that any future colony would require. The survey team uses '
                'CNP-5502-c as their fuel source, skimming the upper atmosphere on the '
                'same resupply runs that keep their ship operational for the years-long '
                'mission.\n\n'
                'The gas giant\'s moons have not been individually surveyed -- the team\'s '
                'resources are focused on the habitable-zone worlds. The moons are '
                'catalogued from orbital scans as a set: at least eleven, mostly icy, none '
                'showing obvious signs of geological activity. They wait in the '
                'development plan alongside everything else that depends on a decision the '
                'council has not made.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-5502-d',
            short_description='A hot inner world -- surveyed quickly, unremarkable, a footnote in a system whose habitable-zone worlds are the story.',
            long_description=(
                'CNP-5502-d is a small, hot world in a close orbit -- dense, airless, and '
                'mineral-bearing in concentrations that are adequate without being '
                'exceptional. The survey team catalogued it in the mission\'s first weeks '
                'and has not returned. In a system containing what may be the best '
                'unassisted colonisation candidate ever discovered, a hot inner rock is '
                'not worth the drone fuel.'
            ),
            population=0,
        ),
        StellarObject(
            name='CNP-5502-e',
            short_description='A frozen outer body -- the most distant known object from Sol in any discovered system, a point of cold rock at the edge of everything.',
            long_description=(
                'CNP-5502-e is a frozen body in the far outer system -- ice and rock, no '
                'atmosphere, orbiting the Sol-like star at the greatest distance of any '
                'catalogued object. The survey team detected it on long-range scans and '
                'has not visited it. The body is, by the metrics of distance, the most '
                'remote known object from Sol in any system humans have reached -- a point '
                'of cold rock at the edge of the furthest system, orbiting a star that '
                'looks like the one humanity started from, seven hundred and eighty '
                'light-years away from the world where it all began.\n\n'
                'The survey team\'s astronomer noted this in the mission log with a brevity '
                'that may or may not have been intentional: furthest known object from Sol. '
                'The entry has no additional commentary. The distances involved make '
                'commentary feel small.'
            ),
            population=0,
        ),
    ],
    short_description='The furthest reach -- a Sol-like star with a potentially habitable world at the edge of known space, too promising to ignore and too dangerous to colonise.',
    long_description=(
        'CNP-5502 is the furthest system the Canopus cluster has discovered -- at the '
        'end of a jump chain that places it farther from the cluster\'s core than any '
        'other known system. The star is a G2V yellow main sequence -- almost identical '
        'to Sol -- and the system contains what may be the best unassisted colonisation '
        'candidate ever discovered: a world with a breathable atmosphere, liquid '
        'surface water, and conditions that fall within human comfort without '
        'terraforming. A second habitable-zone world offers a twin-world prospect that '
        'colonial planners find tantalising.\n\n'
        'The survey team -- a small crew that has been in the system for less than '
        'five years -- is still conducting the assessment. The preliminary data is '
        'extraordinary. The interim reports have been received by the council of '
        'emperors with interest and have not resulted in a colonisation authorisation. '
        'The distance is a concern. The cost is a concern. The real concern is not '
        'stated in the reports: a colony this far from the core would need to be '
        'self-sustaining, and self-sustaining means independent reanimation capability, '
        'and independent reanimation capability means a population that does not '
        'depend on Placidus and does not answer to the council.\n\n'
        'The emperors have spent centuries building a civilisation where immortality '
        'flows from the centre. The technology is controlled. The supply chains are '
        'controlled. The hierarchy is sustained by the dependency of every system on '
        'the reanimation infrastructure that the council governs. CNP-5502 threatens '
        'this not because the world is dangerous but because the world is perfect -- '
        'a place where a colony could thrive without the cluster, and a colony that '
        'does not need the cluster is a colony the cluster cannot control.\n\n'
        'The survey continues. The data accumulates. The council deliberates. The '
        'world orbits its Sol-like star at the edge of known space, breathable and '
        'blue and waiting for a decision that the emperors are in no hurry to make, '
        'because the emperors have all the time in the world and the world will still '
        'be there when they decide.'
    ),
    cluster=StarClusters.CANOPUS,
)

CANOPUS_SYSTEMS: list[System] = [
    CANOPUS, ADHARA, PLACIDUS, PHAET, ALSEPHINA, MIRZAM, AVIOR,
    NIHAL, TURAIS, ACRUX, ASPID, NAOS, SUHAIL,
    CNP_2190, CNP_3318, CNP_0871, CNP_5502,
]
