from ..enums import StarClusters
from .models import System, StellarObject

AIN = System(
    name='Ain',
    star='Orange giant (K0III), approximately 100 times Sol luminosity -- a warm amber star, the first of the Hyades visible from Sol and the last thing visitors see before entering the cluster',
    population=10_000_000_000,
    distance_to_sol=155.0,
    stellar_objects=[
        StellarObject(
            name='Thresken',
            short_description='The gateway world -- five billion people in the system that controls access to the Hyades cluster, where every ship is inspected and every prosthetic is noted.',
            long_description=(
                'Thresken is the front door to the Hyades cluster. The planet is the '
                'system\'s most populous world -- the administrative centre, the customs '
                'hub, and the first Hyadean world that visitors encounter. All traffic '
                'entering the cluster passes through Ain, and most of it passes through '
                'Thresken\'s orbital infrastructure before being cleared for onward transit. '
                'The traffic is heavy: Hyadean citizens returning from the inner systems, '
                'traders carrying goods in both directions, the smugglers who run '
                'prosthetic components to Procyon\'s grey markets, and the steady stream of '
                'out-of-system visitors who come to the Hyades for reasons that range from '
                'commerce to curiosity to desperation.\n\n'
                'The military presence is substantial. The Hyadean fleet maintains a '
                'permanent garrison at Ain -- the warships that guard the gateway and the '
                'patrol vessels that monitor the approaches from MERIT space. The ships are '
                'the Hyadean standard: tough, industrial, unglamorous vessels with exposed '
                'conduits and visible welds, centuries old with every component swapped out '
                'dozens of times, crewed by personnel who interface with their ships through '
                'prosthetic connections that make the distinction between operator and '
                'machine a question of philosophy rather than engineering.\n\n'
                'The guild presence on Thresken is administrative rather than industrial. '
                'The gateway guilds -- the customs processors, the transit coordinators, '
                'the trade facilitators -- operate the system\'s commercial infrastructure '
                'with the practical efficiency that the guild republic applies to '
                'everything. The guild representatives at the gateway are the cluster\'s '
                'first impression: competent, direct, and modified in ways that visitors '
                'from the inner systems find striking. A customs officer with mechanical '
                'hands processing your documentation is a small thing. It is also the '
                'moment when visitors understand that they have entered a civilisation '
                'where flesh is optional.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Vellume',
            short_description='The cosmetic prosthetics world -- where the modifications are designed to look organic, for clients who need to pass as unmodified in MERIT space.',
            long_description=(
                'Vellume is Ain\'s second habitable world and the cluster\'s most unusual '
                'prosthetics market. Where the rest of the Hyades builds prosthetics that '
                'are visibly, proudly mechanical -- exposed joints, industrial finishes, '
                'the aesthetic of function over form -- Vellume builds prosthetics that '
                'look like flesh. The industry on Vellume specialises in organic-appearance '
                'modifications: synthetic skin that passes visual and tactile inspection, '
                'joints that move with biological smoothness, and the subtle details -- '
                'temperature, texture, the micro-movements of living tissue -- that would '
                'betray a standard prosthetic to a careful observer.\n\n'
                'The market is driven by demand from people who need to enter MERIT space '
                'without being identified as modified. MERIT\'s border screening detects '
                'standard Hyadean prosthetics easily -- the materials, the energy '
                'signatures, the mechanical interfaces are all distinctive. Vellume\'s '
                'products are designed to defeat this screening. The promise is '
                'undetectability: a Vellume prosthetic will pass a standard MERIT medical '
                'scan, fool a visual inspection, and feel like flesh to anyone who touches '
                'it. The promise is not always kept. MERIT\'s screening improves. Vellume\'s '
                'engineers improve faster. The arms race between detection and concealment '
                'is Vellume\'s entire economy.\n\n'
                'The out-of-system traffic to Vellume is heavy. The clients include Hyadean '
                'intelligence operatives, commercial agents who work in MERIT space, '
                'and private citizens who travel between the factions and prefer not to '
                'advertise their modifications. The clinics on Vellume are discreet, '
                'expensive, and staffed by engineers who consider their work an art form -- '
                'the art of making the mechanical indistinguishable from the biological. '
                'The rest of the Hyades considers Vellume\'s products faintly shameful -- '
                'prosthetics designed to look like flesh are prosthetics designed to deny '
                'what they are, and in a culture that takes pride in modification, denial '
                'is a complicated choice. Vellume\'s engineers do not care about the '
                'cultural judgement. Their clients need to pass. Their products pass. The '
                'judgement is someone else\'s problem.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Margin',
            short_description='The contested space between Ain and Aldebaran -- where the Hyadean fleet patrols and MERIT probes from the abandoned inner-system colony one jump away.',
            long_description=(
                'The Margin is the volume of space between Ain and the routes that lead '
                'to MERIT space -- including the soft jump to Aldebaran, the abandoned '
                'inner-system colony that MERIT evacuated rather than defend. The Hyadean '
                'fleet patrols the Margin in strength, and MERIT\'s forces from the inner '
                'systems probe it regularly -- reconnaissance flights, sensor sweeps, and '
                'the occasional skirmish that both sides treat as routine.\n\n'
                'The Margin is busier than most gateway contested zones because of the '
                'Hyades\' proximity to Sol. At 155 light-years, the Hyades is the closest '
                'outer faction to the inner systems, and the traffic reflects the distance: '
                'more traders, more smugglers, more intelligence operatives from both sides, '
                'and more of the casual cross-border traffic that proximity enables. The '
                'Hyadean patrol commanders manage this traffic with the pragmatic '
                'understanding that the border is a line on a chart, not a wall, and that '
                'the commerce flowing across it benefits the cluster regardless of what the '
                'guild council\'s official trade policy states.'
            ),
            population=0,
        ),
        StellarObject(
            name='Anvil Gate',
            short_description='The system\'s primary orbital station -- the busiest port in the cluster, processing the traffic between the Hyades and the rest of the galaxy.',
            long_description=(
                'Anvil Gate is Ain\'s primary orbital station and the busiest port in the '
                'Hyades cluster. The station processes the enormous volume of traffic that '
                'the gateway generates: commercial freighters, military vessels, the private '
                'ships of traders and travellers, and the out-of-system visitors who arrive '
                'from MERIT space, from Procyon\'s grey markets, and from the other outer '
                'factions. The station is built in the Hyadean style -- industrial, '
                'functional, with the exposed-conduit aesthetic that defines the cluster\'s '
                'architecture. It is not beautiful. It works.\n\n'
                'The customs processing at Anvil Gate is thorough. Incoming visitors are '
                'screened for prohibited technology -- MERIT surveillance equipment, '
                'restricted software, anything that the guild council considers a security '
                'risk. The screening also catalogues the visitors\' prosthetic status: '
                'modified or unmodified, and if modified, the type and quality of the '
                'hardware. The catalogue is not a legal requirement. It is an economic one '
                '-- the guilds that operate in Ain want to know the prosthetic profile of '
                'the traffic flowing through the gateway, because the profile tells them '
                'what the market needs.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Kellwade',
            short_description='An agricultural world feeding the system -- where the farming is done by workers with specialised prosthetics and the chop shops serve the seasonal labour demand.',
            long_description=(
                'Kellwade is the system\'s agricultural world -- warm, fertile under the '
                'orange giant\'s amber light, and farmed by a workforce whose prosthetic '
                'modifications are calibrated for the work. The agricultural prosthetics '
                'on Kellwade are specialised: reinforced grips for operating heavy equipment, '
                'hardened joints for repetitive physical labour, sensory enhancements that '
                'monitor soil chemistry and crop health through direct interface. The '
                'farmers are modified for farming the way the shipyard workers on Alpha '
                'Pegasi are modified for shipbuilding -- the prosthetics define the job.\n\n'
                'The chop shops on Kellwade serve the seasonal labour demand. Workers who '
                'arrive for the harvest without adequate prosthetics are directed to the '
                'modification clinics in the farming towns -- ranging from the guild-'
                'certified facilities that install quality hardware to the unlicensed '
                'operators in the back streets who install whatever the worker can afford. '
                'A worker who arrives at Kellwade with organic hands leaves with mechanical '
                'ones, because the farms hire the modified and the modified get paid. The '
                'choice is the same as everywhere in the Hyades: keep your flesh and lose '
                'the work, or lose the flesh and keep the work.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Cheldern',
            short_description='A gas giant with fuel processing at gateway scale -- supporting the heaviest traffic volume in the cluster.',
            long_description=(
                'Cheldern is the system\'s gas giant -- fuel processing on its moons at a '
                'scale that matches the gateway\'s enormous traffic. Ain processes more '
                'ships per cycle than any other system in the cluster, and the fuel demand '
                'is matched to that throughput. The fuel operations are guild-operated -- '
                'the fuel processors\' guild is one of the smaller guilds in the republic '
                'but one of the most strategically positioned, because a fuel disruption at '
                'the gateway would bottleneck the entire cluster\'s trade.\n\n'
                'The fuel workers are modified for the job -- interface prosthetics that '
                'connect to the processing equipment, reinforced respiratory systems for '
                'the chemical environment, and the hardened hands that fuel work demands. '
                'In the Hyades, even the fuel workers are prosthetically adapted to their '
                'role. The guild system ensures it: you join the fuel processors\' guild, '
                'you get the fuel processors\' modifications, you do the fuel processors\' '
                'work. The body follows the guild.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Burnwick',
            short_description='A hot inner world -- energy collection and sensor arrays monitoring the border, maintained by workers whose heat-resistant prosthetics let them operate where organic bodies cannot.',
            long_description=(
                'Burnwick is a hot, dense inner world with solar collection arrays and the '
                'border sensor network that monitors the approaches from MERIT space. The '
                'maintenance crews operate in temperatures that would incapacitate an '
                'unmodified human -- their prosthetics include heat-resistant casings, '
                'thermal regulation systems, and the hardened interfaces that let them work '
                'in environments where flesh would cook. The modifications are extreme by '
                'even Hyadean standards: the Burnwick maintenance crews are among the most '
                'heavily modified workers in the cluster, because the environment demands '
                'it and the guild system provides it.\n\n'
                'The sensor arrays on Burnwick are the gateway\'s early warning system -- '
                'scanning the approaches from Aldebaran and the inner systems for military '
                'traffic, commercial vessels, and the intelligence ships that both sides '
                'pretend are civilian traders. The sensor operators interface with their '
                'equipment through neural prosthetics that process the data faster than '
                'organic cognition allows. A Hyadean sensor operator sees the border the '
                'way a machine sees it: in wavelengths, signatures, and patterns that the '
                'prosthetic brain interprets and the organic brain reviews.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='Gateway to the Hyades -- ten billion people at the front door of a prosthetic civilisation, where the border traffic never stops and the body is the first thing that changes.',
    long_description=(
        'Ain is the gateway to the Hyades cluster -- the closest outer faction to Sol '
        'at 155 light-years, and the system through which all traffic into and out of '
        'Hyadean space must pass. Ten billion people live here, and the system\'s '
        'character is defined by the traffic: the heaviest cross-border flow in the '
        'outer systems, driven by the proximity to MERIT space that makes the Hyades '
        'the most accessible of the five factions.\n\n'
        'The military presence is substantial -- the Hyadean fleet guards the gateway '
        'with the tough, industrial warships that define the cluster\'s military, '
        'crewed by personnel who interface with their ships through prosthetic '
        'connections. The Margin -- the contested space between Ain and the routes to '
        'MERIT space -- is patrolled, probed, and busier than any other faction\'s '
        'gateway zone because the distance is shorter and the traffic is heavier.\n\n'
        'Vellume is the system\'s most distinctive feature: a world that builds '
        'prosthetics designed to look like flesh. The organic-appearance market serves '
        'clients who need to enter MERIT space without being identified as modified -- '
        'intelligence operatives, commercial agents, private citizens who travel '
        'between factions. The products promise undetectability. The arms race between '
        'Vellume\'s engineers and MERIT\'s screening technology is the system\'s most '
        'technically sophisticated contest. The rest of the Hyades considers Vellume\'s '
        'products faintly shameful -- prosthetics designed to deny what they are -- '
        'but the clients need to pass, and the products pass, and the cultural '
        'judgement is someone else\'s problem.\n\n'
        'The out-of-system traffic is heavy. Visitors from MERIT space, from Procyon\'s '
        'grey markets, from the other factions -- all of them pass through Ain, are '
        'processed at Anvil Gate, and encounter the first customs officer with '
        'mechanical hands who stamps their documentation and sends them into a '
        'civilisation where flesh is optional and the body follows the guild.'
    ),
    cluster=StarClusters.HYADES,
)

PRIMA_HYADUM = System(
    name='Prima Hyadum',
    star='Orange giant (K0III), approximately 85 times Sol luminosity -- the brightest star in the cluster as seen from Sol, which earned it the name First despite the system being neither the largest nor the most important',
    population=14_000_000_000,
    distance_to_sol=154.0,
    stellar_objects=[
        StellarObject(
            name='Foundren',
            short_description='The guild capital in all but name -- where the major guilds maintain their headquarters and the prosthetics industry showcases what it wants the cluster to want.',
            long_description=(
                'Foundren is where the guilds live. The planet hosts the headquarters of '
                'the cluster\'s major prosthetic guilds -- the heavy-lifters\', the '
                'precision-workers\', the interface specialists\', the medical-grade guild, '
                'and the dozens of smaller guilds that represent the specialised trades the '
                'prosthetic economy has produced. The guild headquarters are architectural '
                'statements -- each one designed to project the identity and values of its '
                'guild, built in the industrial aesthetic that the cluster favours but with '
                'the resources that major guild treasuries can command. The heavy-lifters\' '
                'headquarters is a fortress of exposed steel. The precision-workers\' is a '
                'study in mechanical elegance. The interface specialists\' is wired into the '
                'city\'s data network so thoroughly that the building itself is a prosthetic.\n\n'
                'The political function of Foundren is informal but real. The guild council '
                'meets on Secunda Hyadum -- that is the official capital, and the council '
                'chamber is there. But the negotiations that determine what the council '
                'decides happen on Foundren, in the guild headquarters, between the guild '
                'masters whose organisations represent the cluster\'s workforce. The council '
                'on Secunda Hyadum ratifies. Foundren decides. The distinction is understood '
                'by everyone in the cluster and maintained by the fiction that the official '
                'capital is where the power resides.\n\n'
                'The system was named Prima Hyadum -- First of the Hyades -- because it was '
                'the brightest star in the cluster as seen from Sol, long before humanity '
                'left Earth. The name has been a source of mild irritation for centuries, '
                'because the system is neither the largest, the most populous, nor the most '
                'prosperous in the cluster. It is the guild capital. It is the industrial '
                'showcase. It is important. It is not first in anything except the name '
                'that astronomers gave it from a planet 154 light-years away, and the '
                'residents of Secunda Hyadum and Epsilon Tauri never tire of pointing this '
                'out.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='The Exhibition',
            short_description='An orbital complex that is part industry showcase, part propaganda operation -- demonstrating what prosthetics can do and creating the pressure to want them whether you need them or not.',
            long_description=(
                'The Exhibition is an orbital complex above Foundren that the guilds '
                'maintain as the prosthetics industry\'s permanent showcase. The complex is '
                'part trade fair, part museum, part propaganda installation -- a carefully '
                'designed experience that walks visitors through the history, the '
                'capabilities, and the aspirational future of prosthetic modification.\n\n'
                'The showcase floor displays the latest advances from every major guild: '
                'the heavy-lifters\' newest reinforced limbs that can bend structural steel, '
                'the precision-workers\' hands that can manipulate individual molecules, the '
                'interface specialists\' neural connections that process data at machine '
                'speed. The demonstrations are impressive, the engineering is genuine, and '
                'the messaging is relentless: you could be more than you are. Your organic '
                'body is the limitation. The technology is the solution. The guilds are '
                'here to help.\n\n'
                'The propaganda element is not subtle, but it is effective. The Exhibition '
                'is where young workers come before their first modification -- brought by '
                'parents, by guild recruiters, by the cultural expectation that visiting '
                'the Exhibition is part of growing up in the Hyades. The experience is '
                'designed to make modification feel exciting rather than inevitable, a '
                'choice rather than an economic requirement. The young visitors leave the '
                'Exhibition wanting prosthetics. The Exhibition has done its job. The fact '
                'that the same young visitors would need prosthetics to find work regardless '
                'of whether the Exhibition existed is a truth that the showcase does not '
                'include in its displays.\n\n'
                'The Exhibition also hosts the annual Guild Demonstrations -- a week-long '
                'event where the guilds compete to showcase their newest technology, their '
                'most impressive modifications, and the capabilities of their most heavily '
                'modified members. The Demonstrations are the cluster\'s premier cultural '
                'event -- broadcast across every system, attended by guild delegations from '
                'every world, and watched by the young with the aspirational intensity that '
                'the guilds have cultivated for precisely this purpose.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Kelstrand',
            short_description='The system\'s manufacturing world -- where the mid-range prosthetics that most of the cluster actually uses are produced at industrial scale.',
            long_description=(
                'Kelstrand is Prima Hyadum\'s manufacturing base -- a heavily industrialised '
                'world that produces the prosthetics the cluster runs on. Not the premium '
                'products that the Exhibition showcases, and not the budget hardware that '
                'Chamukuy\'s factories stamp out for the agricultural workforce. Kelstrand '
                'produces the mid-range: the standard-grade prosthetics that the guild '
                'system installs in its members as part of their trade certification. A '
                'precision-worker\'s hands. A heavy-lifter\'s arms. An interface specialist\'s '
                'neural connectors. The hardware that defines what a guild member is and '
                'what a guild member does.\n\n'
                'The factories on Kelstrand are the guild system made physical. Each major '
                'guild operates its own manufacturing lines, producing the prosthetics that '
                'its members will use, to specifications that the guild sets and the guild '
                'inspects. The quality is consistent and adequate -- good enough to function '
                'reliably, not good enough to be mistaken for premium. The workers who '
                'produce the prosthetics are themselves prosthetically modified for the '
                'work, wearing the hardware they manufacture, maintaining the machines that '
                'make the machines that replace the flesh. The recursion is not lost on the '
                'workers. They find it funny in the dry, mechanical way that Hyadean humour '
                'tends to operate.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Sorren',
            short_description='A residential world -- where the guild workers raise families in communities organised around their guild identity rather than geography.',
            long_description=(
                'Sorren is the system\'s residential world -- a temperate planet where the '
                'manufacturing workforce raises families in communities that are organised '
                'by guild rather than by neighbourhood. The heavy-lifters\' districts are '
                'built solid, with oversized doorways and reinforced furniture that '
                'accommodates the mass of a fully modified heavy-lifter\'s body. The '
                'precision-workers\' districts are finer, cleaner, designed for people whose '
                'hands can feel the texture of individual threads and who find rough '
                'surfaces physically unpleasant. The interface specialists\' districts are '
                'wired -- every surface connected, every room networked, the residents '
                'swimming in data the way other people swim in air.\n\n'
                'The guild identity on Sorren is the strongest in the cluster -- children '
                'grow up in guild districts, attend guild schools, and absorb the culture '
                'of their parents\' guild from birth. The choice of guild is nominally free '
                '-- a young person can apply to any guild -- but in practice most follow '
                'their parents because the guild district is home and the guild is family. '
                'The first modification happens in adolescence, when the guild\'s apprentice '
                'programme installs the starter hardware that marks the beginning of a '
                'lifetime of progressive replacement. The ceremony is celebratory. The '
                'parents watch. The young person\'s first prosthetic is installed by the '
                'same guild technician who installed the parents\'. The continuity is the '
                'point.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Brenthane',
            short_description='A gas giant with fuel processing -- and the testing ground where newly manufactured prosthetics are stress-tested under extreme conditions before certification.',
            long_description=(
                'Brenthane is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s industrial traffic. The outer moons also host '
                'the guild certification testing facilities -- controlled environments where '
                'newly manufactured prosthetics are stress-tested under extreme conditions '
                'before being approved for installation. The testing is rigorous: pressure '
                'extremes, temperature cycling, radiation exposure, impact resistance, and '
                'the long-duration endurance tests that simulate a decade of heavy use in '
                'weeks. A prosthetic that passes Brenthane\'s certification is a prosthetic '
                'the guild will stand behind. A prosthetic that fails is recycled, and the '
                'manufacturing line that produced it is reviewed.\n\n'
                'The certification process is the guild system\'s quality control -- the '
                'mechanism that ensures the mid-range hardware produced on Kelstrand meets '
                'the standards that the guild\'s members depend on. The process is taken '
                'seriously because the consequences of failure are personal: a prosthetic '
                'that fails in use fails on a person\'s body, and the person wearing it is '
                'a guild member whose guild promised them the hardware would work.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Drellis',
            short_description='An agricultural world feeding the system -- standard Hyadean farming with the prosthetic modifications that the work demands.',
            long_description=(
                'Drellis is the system\'s agricultural world -- warm, productive under the '
                'amber light, and farmed by a workforce with the standard agricultural '
                'prosthetics that Hyadean farming requires. The output feeds fourteen '
                'billion people -- a substantial demand that the farming operations meet '
                'through the combination of modified workers, engineered crop strains, and '
                'the industrial-scale agriculture that the Hyadean approach to farming '
                'produces.\n\n'
                'The farmers on Drellis are members of the agricultural workers\' guild -- '
                'one of the larger guilds in the republic, with a political voice that '
                'reflects the essential nature of the work. The agricultural guild\'s '
                'representatives on the council argue for the interests of a workforce that '
                'feeds the cluster, and the other guilds listen because the alternative to '
                'listening is going hungry.'
            ),
            population=1_200_000_000,
        ),
    ],
    short_description='The guild capital -- fourteen billion people in the system where the prosthetics industry showcases itself and the guilds decide what the cluster will become.',
    long_description=(
        'Prima Hyadum is named First of the Hyades because it was the brightest star '
        'in the cluster as seen from Sol, 154 light-years away, long before humanity '
        'left Earth. The name has been a mild irritation for centuries because the '
        'system is not first in anything except the astronomers\' catalogue. It is not '
        'the largest, the most populous, or the most prosperous system in the cluster. '
        'What it is, is the guild capital: the system where the major prosthetic '
        'guilds maintain their headquarters, where the industry showcases itself, and '
        'where the negotiations that determine what the guild council on Secunda '
        'Hyadum will decide actually happen.\n\n'
        'Foundren hosts the guild headquarters -- the heavy-lifters\', the precision-'
        'workers\', the interface specialists\', and the dozens of smaller guilds that '
        'the prosthetic economy has spawned. The political function is informal but '
        'real: the council ratifies on Secunda Hyadum, but Foundren decides. The '
        'Exhibition -- the orbital showcase above Foundren -- is the industry\'s '
        'permanent propaganda installation, walking visitors through the capabilities '
        'and the aspirational future of prosthetic modification with messaging that '
        'is relentless and effective: you could be more. Your body is the limitation.\n\n'
        'Kelstrand manufactures the mid-range prosthetics that the cluster runs on -- '
        'the standard-grade hardware that the guild system installs in its members as '
        'part of trade certification. Sorren houses the workforce in guild-organised '
        'communities where children grow up in guild districts, attend guild schools, '
        'and receive their first prosthetic in adolescence from the same technician '
        'who installed their parents\'. The continuity is the point. The guild is the '
        'family. The body follows the guild.\n\n'
        'The system named First is not first. The residents know this. The guilds '
        'headquartered here know this. The tourists who visit the Exhibition and leave '
        'wanting prosthetics they did not need before they arrived do not know this '
        'and do not care, because the Exhibition has done its job and the guild system '
        'has gained another member and the cycle that replaces flesh with metal has '
        'turned one more time.'
    ),
    cluster=StarClusters.HYADES,
)

SECUNDA_HYADUM = System(
    name='Secunda Hyadum',
    star='Yellow-orange giant (G9.5III), approximately 70 times Sol luminosity -- slightly warmer and yellower than Prima Hyadum\'s star, casting a richer golden light that the residents consider superior in every way',
    population=18_000_000_000,
    distance_to_sol=153.0,
    stellar_objects=[
        StellarObject(
            name='Verdemain',
            short_description='The capital of the Hyades cluster -- where the guild council convenes, the inter-guild negotiations are conducted, and the system named Second runs everything.',
            long_description=(
                'Verdemain is the capital of the Hyades cluster and the seat of the guild '
                'republic\'s governing council. The planet is the better world in the better '
                'system -- more temperate than anything in Prima Hyadum, better terraformed, '
                'with a richer golden light from a star that is marginally warmer and '
                'yellower than Prima\'s. The residents of Verdemain are aware of this '
                'superiority and express it with the measured patience of people who know '
                'they are right and do not need to raise their voices about it.\n\n'
                'The guild council meets on Verdemain. The council chamber is a functional '
                'space -- not grand in the way that the Canopan emperors\' council chamber '
                'is grand, or dramatic in the way that the Antarian legislature is dramatic. '
                'The chamber is a negotiating room, built for the practical business of '
                'getting guilds that compete commercially to cooperate politically. The '
                'seats are arranged by guild rather than by system. The debates are '
                'conducted in the language of industrial negotiation -- quotas, allocations, '
                'standards, contracts -- rather than the rhetoric of ideology. The guild '
                'republic does not pretend to be inspired. It pretends to be functional. '
                'The pretence is mostly accurate.\n\n'
                'The governance is practical. The guild masters who sit on the council '
                'represent their members\' interests the way a union represents its workers: '
                'negotiating for resources, market share, regulatory advantage, and the '
                'military protection that the cluster\'s war with MERIT requires. The '
                'inter-guild politics are constant and complicated -- alliances form around '
                'shared economic interests, fracture when those interests diverge, and '
                'reform around the next issue. The heavy-lifters and the mining guild '
                'collaborate because their members work the same sites. The precision-'
                'workers and the interface specialists compete because their markets '
                'overlap. The agricultural guild votes with whoever promises the best trade '
                'terms for food exports. The politics are unglamorous and effective, which '
                'is the Hyadean approach to everything.\n\n'
                'The name is the system\'s quiet triumph. Secunda Hyadum -- Second of the '
                'Hyades -- was named by astronomers on Earth who measured brightness rather '
                'than worth. The system is second in nothing except the catalogue. The '
                'residents have considered petitioning to change the name and have decided '
                'not to, because the discrepancy between the name and the reality is its '
                'own form of satisfaction.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='Kelrath',
            short_description='The system\'s administrative world -- where the guild republic\'s bureaucracy translates council decisions into the regulations that govern the cluster.',
            long_description=(
                'Kelrath is the system\'s bureaucratic engine -- a temperate, well-developed '
                'world that houses the administrative apparatus of the guild republic. The '
                'council on Verdemain makes the decisions. Kelrath implements them -- '
                'translating inter-guild agreements into the regulations, standards, and '
                'enforcement mechanisms that govern the cluster\'s prosthetic economy.\n\n'
                'The regulatory framework is enormous. The guilds operate under a web of '
                'standards that govern prosthetic quality, installation procedures, '
                'certification requirements, trade terms, and the labour practices that '
                'determine how the prosthetic workforce is managed. The bureaucrats on '
                'Kelrath who administer this framework are the cluster\'s most essential '
                'and least celebrated professionals -- civil servants with administrative '
                'prosthetics optimised for data processing, working in offices where the '
                'interfaces are wired into the regulatory databases and the work is '
                'conducted at the speed of thought rather than the speed of paperwork.\n\n'
                'Kelrath is also where the guild disputes are adjudicated. When guilds '
                'disagree on standards, on territory, on the allocation of resources -- '
                'which is constantly -- the dispute resolution mechanisms on Kelrath '
                'process the claims with the industrial efficiency that the cluster applies '
                'to everything. The arbitrators are modified for the work: enhanced memory '
                'for case law, accelerated processing for complex negotiations, and the '
                'neural interfaces that let them access the full regulatory database in '
                'real time during arbitration. Justice in the Hyades is not blind. It is '
                'wired.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Thornden',
            short_description='An industrial world producing the specialised prosthetics that the administrative and professional classes require -- the white-collar hardware.',
            long_description=(
                'Thornden is the system\'s manufacturing world -- but where Kelstrand on '
                'Prima Hyadum produces the mid-range prosthetics for the guild workforce, '
                'Thornden produces the specialised hardware for the administrative, '
                'professional, and managerial classes. The administrative prosthetics '
                'produced on Thornden are different from the industrial hardware: neural '
                'interfaces optimised for data processing rather than machine operation, '
                'cognitive enhancers that accelerate analytical thinking, and the sensory '
                'modifications that let the cluster\'s managers and bureaucrats process '
                'information at speeds that unmodified administrators cannot match.\n\n'
                'The market for Thornden\'s products is smaller than Kelstrand\'s but the '
                'margins are higher. An administrative neural interface costs more than a '
                'heavy-lifter\'s arm because the engineering is more precise and the '
                'installation is more delicate. The guild that represents the administrative '
                'workers -- the processionals\' guild, as they style themselves -- is one of '
                'the wealthier guilds in the republic despite its smaller membership, '
                'because the per-member cost of modification is the highest in the cluster.\n\n'
                'The chop shops on Thornden serve the professional workers who cannot '
                'afford the guild-certified installations. A young bureaucrat who needs a '
                'cognitive enhancer to compete for promotions but cannot afford the '
                'processionals\' guild rates will find unlicensed clinics in Thornden\'s '
                'commercial districts that install uncertified hardware at a fraction of '
                'the cost. The hardware works. It is not guaranteed. When it fails, the '
                'failure is neurological rather than mechanical, and the consequences are '
                'worse than a broken arm.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Council Station',
            short_description='The system\'s primary orbital port -- where the guild delegations arrive for council sessions and the diplomatic traffic of a prosthetic civilisation is processed.',
            long_description=(
                'Council Station is Secunda Hyadum\'s primary orbital facility -- a large '
                'station that handles the system\'s traffic with an emphasis on the '
                'political function that the capital provides. The guild delegations that '
                'arrive for council sessions dock at Council Station -- the guild masters '
                'and their staffs, modified in the distinctive styles of their respective '
                'guilds, arriving from every system in the cluster. The station\'s docking '
                'bays during a council session are a catalogue of Hyadean prosthetic '
                'diversity: heavy-lifters whose mass requires reinforced docking clamps '
                'beside precision-workers whose hands are too delicate for a standard '
                'handshake.\n\n'
                'The station also handles the diplomatic traffic from the other factions '
                'and from MERIT -- conducted through intermediaries and unofficial channels, '
                'because the Hyades and MERIT are formally at war and formal diplomatic '
                'contact does not exist. The informal contact is extensive. The guild '
                'republic is pragmatic about commerce with the inner systems, and the '
                'intermediaries who facilitate that commerce pass through Council Station '
                'with the studied casualness of people who are not diplomats and are not '
                'conducting diplomacy and whose ships are not carrying messages from '
                'MERIT\'s government.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Orbrand',
            short_description='A gas giant with fuel processing and the guild republic\'s strategic reserves -- the cluster\'s insurance against supply disruption.',
            long_description=(
                'Orbrand is the system\'s gas giant -- fuel processing on its moons '
                'supporting the capital\'s traffic, and the outer moons hosting the guild '
                'republic\'s strategic reserves. The reserves are maintained by the council '
                'collectively -- fuel, raw materials for prosthetic manufacturing, and the '
                'stockpiles of certified prosthetic components that would sustain the '
                'cluster\'s replacement cycle if the manufacturing systems were disrupted.\n\n'
                'The reserves represent the guild republic\'s institutional caution. The '
                'guilds compete commercially but cooperate on strategic security, because a '
                'disruption in prosthetic supply affects every guild equally and a cluster '
                'full of people with failing hardware is a cluster that cannot function. '
                'The reserves are the council\'s agreement that whatever else they disagree '
                'on, the supply must not fail.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Prestwick',
            short_description='An agricultural world feeding the capital -- productive, well-managed, and the agricultural guild\'s political base for council negotiations.',
            long_description=(
                'Prestwick is the system\'s agricultural world -- fertile, warm under the '
                'golden light, and farmed at a scale that feeds eighteen billion people. '
                'The agricultural guild\'s strongest political base is here -- Prestwick\'s '
                'farming communities produce the guild representatives who sit on the '
                'council and negotiate with the directness of people who understand that '
                'food is the one thing nobody can do without.\n\n'
                'The agricultural guild on Prestwick is politically savvy in the way that '
                'a guild that feeds the capital learns to be. The guild\'s votes on the '
                'council are traded for concessions -- better terms for agricultural '
                'prosthetics, priority access to maintenance services, the regulatory '
                'exemptions that make farming operations viable. The other guilds consider '
                'the agricultural guild\'s negotiating tactics aggressive. The agricultural '
                'guild considers them proportionate to the importance of not starving.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Calcen',
            short_description='A hot inner world -- energy collection and the guild republic\'s secure communications hub, where the encrypted channels that connect the council to every system are maintained.',
            long_description=(
                'Calcen is a hot inner world with solar collection arrays and the guild '
                'republic\'s secure communications infrastructure. The encrypted channels '
                'that connect the council on Verdemain to every system in the cluster are '
                'routed through Calcen\'s relay network -- a hardened system designed to '
                'maintain communications even under military attack. The communications '
                'guild operates the network with the understanding that if the network '
                'fails, the council cannot coordinate and the cluster fragments.\n\n'
                'The maintenance crews on Calcen are modified for the heat and radiation '
                'environment -- the same kind of extreme adaptation that Burnwick\'s crews '
                'on Ain require. The communications guild considers the Calcen posting one '
                'of its most important, and the technicians who maintain the relay network '
                'are among the guild\'s most experienced members.'
            ),
            population=20_000_000,
        ),
    ],
    short_description='The actual capital -- eighteen billion people in the system named Second that runs the guild republic and has never needed to be named First.',
    long_description=(
        'Secunda Hyadum is the capital of the Hyades cluster and the seat of the guild '
        'republic -- the system named Second by astronomers on Earth who measured '
        'brightness rather than worth, and that has been running the cluster from the '
        'position of quiet superiority ever since. The star is warmer and yellower '
        'than Prima Hyadum\'s, the worlds are better terraformed, and the system is '
        'larger and more populous. The residents have considered changing the name and '
        'decided not to, because the discrepancy between the name and the reality is '
        'its own satisfaction.\n\n'
        'The guild council meets on Verdemain in a chamber designed for negotiation '
        'rather than ceremony. The seats are arranged by guild. The debates are '
        'conducted in the language of quotas, allocations, and contracts rather than '
        'ideology. The guild masters represent their members the way unions represent '
        'workers -- negotiating for resources, market share, and the military '
        'protection that the war with MERIT requires. The politics are unglamorous '
        'and effective, which is the Hyadean approach to everything.\n\n'
        'Kelrath administers the regulatory framework that governs the prosthetic '
        'economy -- quality standards, certification, trade terms, dispute resolution. '
        'The arbitrators are wired into the regulatory database in real time. Justice '
        'in the Hyades is not blind; it is wired. Thornden manufactures the '
        'white-collar prosthetics -- neural interfaces, cognitive enhancers, the '
        'administrative hardware that the professional class requires. The chop shops '
        'on Thornden serve the young professionals who cannot afford guild rates, and '
        'when the uncertified neural hardware fails the consequences are worse than a '
        'broken arm.\n\n'
        'Eighteen billion people live in a system that runs on negotiation, '
        'regulation, and the pragmatic understanding that guilds that compete '
        'commercially must cooperate politically or the cluster falls apart. The '
        'council chamber on Verdemain is where this understanding is maintained, '
        'session by session, negotiation by negotiation, in a system that was named '
        'Second and has never needed to be first.'
    ),
    cluster=StarClusters.HYADES,
)

EPSILON_TAURI = System(
    name='Epsilon Tauri',
    star='Orange giant (K0III), approximately 100 times Sol luminosity -- a confirmed exoplanet-hosting star, with a Jupiter-mass gas giant that was one of the first discovered around a giant star in an open cluster',
    population=22_000_000_000,
    distance_to_sol=155.0,
    stellar_objects=[
        StellarObject(
            name='Valcourt',
            short_description='The most prosperous world in the Hyades cluster -- nine billion people demonstrating what the prosthetic economy looks like when everything works and everyone can afford the good hardware.',
            long_description=(
                'Valcourt is the Hyades cluster\'s answer to every criticism MERIT levels '
                'at the prosthetic economy. The planet is temperate, beautifully developed, '
                'and home to nine billion people who are prosthetically modified and '
                'genuinely thriving. The prosthetics on Valcourt are premium -- the finest '
                'hardware the guilds produce, installed by certified practitioners, '
                'maintained by a support infrastructure that ensures the hardware functions '
                'perfectly for decades. The heavy-lifters on Valcourt have arms that '
                'respond like flesh but lift like machines. The precision-workers have hands '
                'that feel texture at the molecular level and never shake. The interface '
                'specialists process data with a fluency that makes the organic brain feel '
                'like an accessory rather than the operator.\n\n'
                'The quality of life is outstanding. The cities are clean, modern, and '
                'designed for a population whose bodies are partly mechanical -- the '
                'architecture accommodates the range of Hyadean modification, from the '
                'lightly enhanced to the heavily replaced, with an elegance that makes the '
                'accommodation feel natural rather than adaptive. The infrastructure works. '
                'The healthcare -- which in the Hyades means prosthetic maintenance as much '
                'as biological medicine -- is excellent. The education system produces '
                'graduates who are skilled, modified for their chosen guild, and confident '
                'in a way that prosperity enables.\n\n'
                'MERIT\'s objection is the same as always: the system works beautifully at '
                'the top. The prosthetics on Valcourt are premium because Valcourt\'s '
                'population can afford premium. The workers on Enif\'s mines cannot. The '
                'seasonal labourers on Chamukuy\'s farms cannot. The showcase is real. It '
                'is also selective. Valcourt demonstrates what the prosthetic economy '
                'produces for the wealthy, and the billions who cannot afford the good '
                'hardware are not part of the demonstration.\n\n'
                'The residents of Valcourt are aware of this criticism and consider it '
                'unfair. They did not choose to be prosperous at the expense of others. '
                'They chose to be prosperous, and the prosperity produced excellent '
                'prosthetics, and the excellent prosthetics produced more prosperity, and '
                'the cycle is virtuous here in a way that it is not elsewhere, and Valcourt '
                'is not responsible for elsewhere. The argument is sincere. It is also '
                'the argument that wealth has made in every civilisation that has ever '
                'existed, and it is no more convincing here than it has ever been.'
            ),
            population=9_000_000_000,
        ),
        StellarObject(
            name='Senneth',
            short_description='A second prosperous world -- where the luxury prosthetics market produces the bespoke modifications that the wealthy commission as art as much as function.',
            long_description=(
                'Senneth is Epsilon Tauri\'s second major world -- warm, well-developed, '
                'and home to the luxury end of the prosthetic market. Where Valcourt\'s '
                'prosthetics are premium standard -- the best the guilds produce in volume '
                '-- Senneth\'s market is bespoke. The workshops on Senneth produce '
                'prosthetics that are commissioned individually, designed for a specific '
                'client, and crafted with an attention to aesthetics that the standard '
                'guild hardware does not attempt.\n\n'
                'The bespoke market treats prosthetics as art. A Senneth arm is not just '
                'functional -- it is beautiful, designed to complement the client\'s body, '
                'to express their identity, to make a statement about who they are and what '
                'they value. The materials are exotic: polished alloys, inlaid composites, '
                'surfaces that shift colour with temperature or light. The engineering is '
                'the finest in the cluster, exceeding even Thornden\'s precision work '
                'because the bespoke market demands perfection at every level -- mechanical, '
                'aesthetic, and the integration with the client\'s remaining organic tissue '
                'that determines whether the prosthetic feels like part of the body or '
                'like something attached to it.\n\n'
                'The clients are the Hyades cluster\'s wealthiest citizens -- guild masters, '
                'industrial magnates, and the families whose prosperity spans generations '
                'and whose prosthetics are heirlooms as much as hardware. A bespoke '
                'Senneth prosthetic is passed down: the design is archived, and when the '
                'next generation requires a similar modification the workshop produces a '
                'new piece in the family\'s established style. The continuity of design '
                'across generations is a mark of status that the wealthy maintain and the '
                'less wealthy imitate with cheaper materials and less skilled artisans.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Brandell',
            short_description='A residential and services world -- comfortable, well-run, where the middle class lives well enough to afford decent prosthetics and not well enough to afford Senneth\'s.',
            long_description=(
                'Brandell is the system\'s third major world -- temperate, comfortable, and '
                'home to the middle class that Valcourt\'s showcase and Senneth\'s luxury '
                'market both depend on. The population works in services, education, '
                'healthcare, and the administrative roles that a system of twenty-two '
                'billion people requires. The prosthetics are mid-to-high range -- better '
                'than the standard guild hardware on Prima Hyadum, not as fine as the '
                'bespoke work on Senneth. The workers on Brandell can afford hardware that '
                'functions reliably, looks good, and lasts. They cannot afford art.\n\n'
                'The culture on Brandell is shaped by this middle position. The residents '
                'are modified, comfortable, and aware that they occupy the space between '
                'the showcase and the reality that MERIT describes. Their prosthetics work '
                'well. Their lives are good. They are not the advertisement and they are '
                'not the cautionary tale. They are the ordinary, which in a cluster that '
                'tends toward extremes is a distinction that Brandell\'s residents value '
                'more than the residents of the extreme systems understand.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Aionos',
            short_description='The confirmed gas giant -- a Jupiter-mass world discovered from Earth, whose moons host fuel processing and the system\'s most exclusive rehabilitation clinics.',
            long_description=(
                'Aionos is the system\'s gas giant -- a Jupiter-mass world that was one of '
                'the first exoplanets discovered orbiting a giant star in an open cluster, '
                'confirmed from Earth long before humanity reached the Hyades. The '
                'discovery is a historical footnote that Epsilon Tauri\'s residents mention '
                'with casual pride -- the planet was known before it was reached, named '
                'before it was visited, and now hosts fuel processing operations on its '
                'moons that service the system\'s considerable traffic.\n\n'
                'The outer moons of Aionos host the system\'s most exclusive prosthetic '
                'rehabilitation clinics -- facilities where clients recovering from major '
                'modifications or upgrades spend weeks adjusting to new hardware in '
                'controlled, private environments. The clinics cater to the wealthy: the '
                'same clientele who commission bespoke work on Senneth come to Aionos\'s '
                'moons for the recovery that follows. The process of integrating a new '
                'prosthetic -- retraining the neural pathways, calibrating the sensory '
                'feedback, adjusting to the changed weight and balance of a body that is '
                'part new -- takes time and care that the clinics provide at rates that '
                'ensure the care is unhurried.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Meridine Station',
            short_description='The system\'s primary orbital port -- gleaming, modern, and the most visually impressive station in the cluster because Epsilon Tauri can afford to make it so.',
            long_description=(
                'Meridine Station is Epsilon Tauri\'s primary orbital facility -- a large, '
                'modern station that is, unlike most Hyadean infrastructure, designed to be '
                'beautiful. The standard Hyadean aesthetic is industrial and functional -- '
                'exposed conduits, visible welds, the honest display of mechanical '
                'structure. Meridine Station does not abandon this aesthetic but refines it: '
                'the conduits are polished, the welds are precise, and the structural '
                'elements are arranged with a compositional awareness that makes the '
                'station look designed rather than assembled. The effect is the Hyadean '
                'industrial aesthetic elevated to elegance.\n\n'
                'The station handles the system\'s traffic -- commercial, civilian, and the '
                'luxury vessels of the wealthy clients who visit Senneth\'s workshops and '
                'Aionos\'s rehabilitation clinics. The commercial district caters to the '
                'prosperous: the goods are high-end, the services are refined, and the '
                'prosthetic maintenance shops offer calibration and adjustment at a quality '
                'that workers from other systems describe as life-changing and that '
                'Meridine\'s residents consider the minimum acceptable standard.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Grenfeld',
            short_description='An agricultural world feeding the system -- productive and well-managed, with prosthetic farming technology that other agricultural systems cannot afford.',
            long_description=(
                'Grenfeld is the system\'s agricultural world -- warm, fertile, and farmed '
                'with prosthetic technology that reflects Epsilon Tauri\'s wealth. The '
                'agricultural prosthetics on Grenfeld are not the budget hardware of '
                'Chamukuy\'s farms -- they are high-quality modifications that make farming '
                'precise, efficient, and considerably less destructive to the workers than '
                'the standard agricultural modifications. The farmers on Grenfeld work with '
                'hardware that lasts, in conditions that their prosthetics can handle, and '
                'the difference between Grenfeld\'s farming and Chamukuy\'s is the same '
                'difference that runs through the entire cluster: the difference that money '
                'makes.\n\n'
                'The output feeds twenty-two billion people with a surplus that is exported '
                'to less self-sufficient systems. The agricultural guild\'s presence on '
                'Grenfeld is the cluster\'s wealthiest agricultural community -- farmers '
                'who can afford the good hardware, whose yields reflect it, and whose '
                'political voice in the guild council is amplified by the economic weight '
                'of the system they feed.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Ardith',
            short_description='A hot inner world -- energy collection and advanced prosthetic testing, where the radiation environment is used to stress-test premium hardware.',
            long_description=(
                'Ardith is a hot inner world with solar collection arrays and a secondary '
                'function that Epsilon Tauri\'s prosperity enables: advanced prosthetic '
                'stress-testing under real radiation conditions. The premium hardware that '
                'Valcourt\'s population depends on and that Senneth\'s workshops produce is '
                'tested here -- exposed to the radiation environment of a close solar orbit '
                'to verify that the materials and engineering will hold under the most '
                'demanding conditions a client might encounter.\n\n'
                'The testing is a quality assurance measure that most systems in the '
                'cluster do not invest in because the cost is prohibitive. Epsilon Tauri '
                'invests because the system\'s reputation depends on the hardware being as '
                'good as advertised, and the hardware being tested on Ardith is advertised '
                'as the finest in the galaxy.'
            ),
            population=15_000_000,
        ),
    ],
    short_description='The showcase of the Hyades -- twenty-two billion people in the most prosperous system the prosthetic economy has produced, demonstrating what modification looks like when everyone can afford the best.',
    long_description=(
        'Epsilon Tauri is the Hyades cluster\'s showcase -- the most populous, most '
        'prosperous system in a civilisation built on the replacement of flesh with '
        'metal. Twenty-two billion people live here, and the system demonstrates what '
        'the prosthetic economy looks like when the hardware is premium, the '
        'maintenance is excellent, and the population can afford the best of both. The '
        'cities on Valcourt are clean, modern, and designed for bodies that are partly '
        'mechanical. The workshops on Senneth produce bespoke prosthetics that are art '
        'as much as function. The rehabilitation clinics on Aionos\'s moons provide the '
        'unhurried recovery that major modifications require.\n\n'
        'The quality of life is outstanding. The prosthetics work perfectly. The '
        'healthcare is excellent. The education produces confident, skilled graduates '
        'modified for their chosen guilds. The infrastructure accommodates the full '
        'range of Hyadean modification with an elegance that makes the accommodation '
        'feel natural. Epsilon Tauri is the argument the Hyades makes in its own '
        'defence: look at what modification produces when the investment is sufficient.\n\n'
        'MERIT\'s objection is unchanged: the system works beautifully at the top. The '
        'showcase is real and selective. Valcourt demonstrates what prosperity buys. '
        'The miners on Enif, the seasonal labourers on Chamukuy, the workers in '
        'Scheat\'s organ banks are not part of the demonstration. The residents of '
        'Epsilon Tauri consider this criticism unfair -- they did not choose to be '
        'prosperous at the expense of others. The argument is sincere. It is also the '
        'argument that wealth has made in every civilisation that has ever existed.\n\n'
        'The gas giant -- Aionos -- was discovered from Earth, one of the first '
        'exoplanets confirmed around a giant star in an open cluster. The historical '
        'footnote is mentioned with casual pride. The planet was known before it was '
        'reached, and now its moons host the clinics where the wealthy recover from '
        'the modifications that their wealth can afford. The irony of a planet '
        'discovered through human curiosity hosting the industry that replaces human '
        'parts is not noted by the residents, who have long since stopped thinking of '
        'flesh and metal as opposites.'
    ),
    cluster=StarClusters.HYADES,
)

CHAMUKUY = System(
    name='Chamukuy',
    star='Orange giant (K0IIIb), approximately 75 times Sol luminosity -- the same warm amber light as the rest of the core Hyades, falling on fields worked by hands that are no longer flesh',
    population=12_000_000_000,
    distance_to_sol=155.0,
    stellar_objects=[
        StellarObject(
            name='Morthane',
            short_description='The cluster\'s breadbasket -- six billion people farming at industrial scale with prosthetics designed for the work, on a world where keeping your organic hands means you don\'t eat.',
            long_description=(
                'Morthane is the Hyades cluster\'s primary agricultural world -- a warm, '
                'fertile planet with deep soil, reliable seasons, and growing conditions '
                'that produce yields rivalling anything in the inner systems. The farming '
                'is industrial in scale and prosthetic in practice: the workforce is '
                'modified for the work with specialised agricultural prosthetics that make '
                'organic farming impossible to compete with.\n\n'
                'The agricultural prosthetics on Morthane are the guild system\'s most '
                'visible success and its most uncomfortable demonstration. The farming '
                'hands are mechanical -- reinforced grips that operate harvesting equipment '
                'without fatigue, sensory arrays in the fingertips that read soil chemistry '
                'and moisture content on contact, interface ports that connect the farmer '
                'directly to the automated systems that manage irrigation, pest control, '
                'and crop rotation. A modified farmer on Morthane outproduces an unmodified '
                'farmer by a factor that makes competition meaningless. The organic farmer '
                'cannot compete. The organic farmer does not get hired. The organic farmer '
                'gets modified or leaves.\n\n'
                'The chop shops on Morthane are the cluster\'s busiest agricultural '
                'modification facilities. The guild-certified clinics in the farming towns '
                'install the standard agricultural package: hands, forearms, and the '
                'sensory suite that the farms require. The unlicensed operators in the '
                'back streets install cheaper versions -- hardware that works but requires '
                'more maintenance, with sensory arrays that are less precise and interfaces '
                'that are less reliable. The workers who use the cheap hardware maintain it '
                'themselves, with tools and parts traded in the informal economy that '
                'surrounds every chop shop district. A farmer whose prosthetic hand fails '
                'during harvest does not go to the guild clinic. A farmer whose prosthetic '
                'hand fails during harvest goes to the nearest back-street operator and '
                'pays whatever the operator charges, because the harvest does not wait.\n\n'
                'The agricultural workers\' guild on Morthane is the cluster\'s largest '
                'guild by membership -- more people farm than do anything else, and the '
                'guild\'s political weight reflects this. The guild negotiates aggressively '
                'on the council for the terms that matter to its members: the cost of '
                'agricultural prosthetics, the maintenance schedules, and the replacement '
                'cycle that determines how often a farmer\'s hardware is refreshed. The '
                'cost of the standard agricultural package is the most politically '
                'sensitive price in the cluster, because it determines how much debt a '
                'young farmer takes on at the start of a career that will require '
                'progressively more modification as the body ages and the hardware demands '
                'increase.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Brannick',
            short_description='The system\'s budget prosthetics world -- where the general-purpose hardware that the cluster\'s working class actually uses is manufactured at scale.',
            long_description=(
                'Brannick is the system\'s industrial world and the cluster\'s primary '
                'source of budget prosthetics. Not the mid-range guild-certified hardware '
                'that Kelstrand on Prima Hyadum produces, and not the specialised equipment '
                'that the various systems manufacture for their local industries. Brannick '
                'produces the cheap, general-purpose prosthetics that the majority of the '
                'cluster\'s working population actually uses -- the hardware that costs the '
                'least, does the job adequately, and needs replacing sooner than the '
                'manufacturers\' specifications suggest.\n\n'
                'The factories on Brannick are high-volume, low-margin operations that '
                'produce prosthetic hands, arms, legs, joints, and basic sensory packages '
                'in quantities that the more prestigious manufacturing worlds cannot match. '
                'The quality is functional. The engineering is competent. The hardware '
                'works. It is not elegant. It is not self-maintaining. It requires the '
                'regular maintenance that the budget market\'s customers can barely afford '
                'and that the manufacturers have calibrated to ensure repeat business. A '
                'Brannick prosthetic is designed to work long enough to justify the '
                'purchase and fail soon enough to require replacement, and the line between '
                'the two is the most carefully engineered feature of the product.\n\n'
                'The workers on Brannick\'s factory floors wear Brannick\'s products. The '
                'irony is structural: the people who manufacture the budget prosthetics '
                'cannot afford the better hardware, and the hardware they can afford is the '
                'hardware they make. The factories are staffed by workers wearing their own '
                'output, maintaining their own prosthetics with parts diverted from the '
                'production line in the informal economy that the factory managers tolerate '
                'because the alternative is a workforce that cannot maintain itself.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Selland',
            short_description='A second agricultural world -- cooler, drier, specialising in grain crops and the livestock operations that the prosthetic workforce makes safer than they would otherwise be.',
            long_description=(
                'Selland is the system\'s second agricultural world -- cooler than Morthane, '
                'with broad steppe plains that support the grain crops and livestock '
                'operations that supplement Morthane\'s produce. The grain farming is '
                'standard prosthetic agriculture -- the same modified workforce, the same '
                'economics. The livestock operations are where the prosthetic advantage is '
                'most visible.\n\n'
                'Livestock handling is dangerous. The animals are large, agitated, and '
                'unpredictable. An organic farmer working with livestock risks broken bones, '
                'crushed limbs, and the injuries that large-animal agriculture has always '
                'produced. A prosthetic farmer working with livestock risks damaged '
                'hardware. The difference is the consequence: a broken arm takes months to '
                'heal. A damaged prosthetic arm takes hours to replace. The economics of '
                'livestock farming in the Hyades favour the modified worker so dramatically '
                'that the few remaining organic livestock handlers are curiosities rather '
                'than competitors -- holdouts whose stubbornness the other farmers respect '
                'in the abstract and whose injury rates the insurance calculations do not '
                'support.\n\n'
                'The livestock workers on Selland are among the most frequently repaired '
                'workers in the cluster. A livestock handler\'s prosthetic arms are '
                'replaced or repaired multiple times per season -- kicked, stepped on, '
                'caught in fencing, crushed against walls by animals that outweigh the '
                'handler by an order of magnitude. The repair facilities in Selland\'s '
                'farming communities do the most business during calving season, when the '
                'injury rate spikes and the repair queues extend for hours. The handlers '
                'wait with their damaged arms and swap stories about which animal did the '
                'damage, in the way that workers everywhere swap stories about the job.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Millhaven Station',
            short_description='The system\'s orbital port -- where the agricultural output and the budget prosthetics are loaded for export to the rest of the cluster.',
            long_description=(
                'Millhaven Station is Chamukuy\'s primary orbital facility -- a large '
                'industrial port that handles the system\'s twin exports: agricultural '
                'produce heading to every system in the cluster, and budget prosthetics '
                'heading to the same destinations. The two cargo streams share the station\'s '
                'freight bays -- containers of grain beside containers of mechanical hands, '
                'the cluster\'s food supply and the cluster\'s hardware supply loaded onto '
                'the same freighters by dockworkers whose own prosthetics are Brannick\'s '
                'cheapest.\n\n'
                'The station is functional in the way that agricultural and industrial '
                'infrastructure tends to be -- built for throughput rather than impression, '
                'maintained to the standard that keeps it operational rather than the '
                'standard that makes it attractive. Visitors from Prima Hyadum\'s Exhibition '
                'or Epsilon Tauri\'s premium clinics find Millhaven Station unglamorous. '
                'The station staff find the visitors\' expectations amusing. The station '
                'moves more tonnage per cycle than any other facility in the cluster. '
                'It does not need to be pretty to do it.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Wendover',
            short_description='A gas giant with fuel processing -- supporting the heavy freighter traffic that carries the cluster\'s food and hardware.',
            long_description=(
                'Wendover is the system\'s gas giant -- fuel processing on its moons at a '
                'scale that matches the freighter traffic Chamukuy\'s exports generate. The '
                'traffic is heavy and continuous -- the cluster depends on Chamukuy\'s '
                'agricultural output the way it depends on Ain\'s gateway, and the fuel '
                'operations are sized for the demand. The fuel processors\' guild operates '
                'the facilities with the understanding that a fuel disruption at Chamukuy '
                'means a food disruption everywhere.\n\n'
                'The fuel workers are modified with the standard fuel-processing package -- '
                'the same hardware as Cheldern\'s crews on Ain. The guild ensures '
                'consistency: a fuel worker transferred from Wendover to Cheldern or any '
                'other system\'s fuel operation carries the same modifications and performs '
                'the same work. The body follows the guild. The guild follows the work.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Suthern',
            short_description='A hot inner world -- energy collection for the system\'s agricultural and manufacturing operations, maintained by workers with heat-grade prosthetics.',
            long_description=(
                'Suthern is a hot inner world with solar collection arrays powering the '
                'system\'s agricultural infrastructure -- the irrigation systems, the '
                'climate management, the processing facilities that prepare the produce for '
                'export. The maintenance crews wear heat-grade prosthetics: the same kind '
                'of thermal-resistant hardware that Burnwick\'s crews on Ain and Calcen\'s '
                'crews on Secunda Hyadum use. The guild system standardises the hardware '
                'across systems, so a heat-grade technician is a heat-grade technician '
                'regardless of which star they work under.'
            ),
            population=15_000_000,
        ),
    ],
    short_description='The cluster\'s breadbasket and budget hardware factory -- twelve billion people growing the food and making the prosthetics that the working class depends on.',
    long_description=(
        'Chamukuy feeds the Hyades cluster and equips its working class. The system '
        'is the cluster\'s primary agricultural producer and the source of the budget '
        'prosthetics that the majority of the population actually uses -- the cheap, '
        'general-purpose hardware that costs the least, works adequately, and needs '
        'replacing sooner than the specifications suggest.\n\n'
        'Morthane is the breadbasket -- six billion people farming at industrial scale '
        'with prosthetics designed for the work. The agricultural modifications are '
        'the guild system\'s most visible demonstration: a modified farmer outproduces '
        'an organic farmer by a factor that makes competition meaningless. Keep your '
        'organic hands and you don\'t get hired. The chop shops in the farming towns '
        'are the cluster\'s busiest, installing the standard agricultural package or '
        'whatever the worker can afford from the unlicensed operators in the back '
        'streets. Selland handles the grain and livestock -- the livestock operations '
        'where the prosthetic advantage is most dramatic, because a broken prosthetic '
        'arm takes hours to replace and a broken organic arm takes months.\n\n'
        'Brannick manufactures the budget prosthetics -- high-volume, low-margin '
        'hardware designed to work long enough to justify the purchase and fail soon '
        'enough to require replacement. The workers on Brannick\'s factory floors '
        'wear their own output, maintaining their prosthetics with parts diverted '
        'from the production line because the hardware they can afford is the hardware '
        'they make. The irony is structural and nobody laughs.\n\n'
        'Twelve billion people in a system that produces the two things the cluster '
        'cannot do without: food and cheap replacement parts. The agricultural guild '
        'is the largest by membership and the most politically aggressive on the '
        'council, because the cost of the standard agricultural prosthetic package '
        'determines how much debt a young farmer takes on at the start of a career '
        'that will require progressively more modification as the body ages. The '
        'cluster eats what Chamukuy grows and wears what Chamukuy builds, and '
        'Chamukuy\'s workers do both with hardware that is adequate and nothing more.'
    ),
    cluster=StarClusters.HYADES,
)

ALPHA_PEGASI = System(
    name='Alpha Pegasi',
    star='Blue-white giant (B9III), approximately 200 times Sol luminosity -- harsh and bright, the only blue-white star in the core Hyades systems, casting cold light over the shipyards that build the fleet',
    population=15_000_000_000,
    distance_to_sol=133.0,
    stellar_objects=[
        StellarObject(
            name='Vosthen',
            short_description='The forge of the Hyadean fleet -- seven billion people building the tough, industrial warships that define the cluster\'s military, under a star that looks nothing like home.',
            long_description=(
                'Vosthen is where the Hyadean fleet is built. The planet is heavily '
                'industrialised -- foundries, fabrication plants, and the component '
                'factories that feed the orbital shipyards with the structural materials, '
                'weapons systems, and the prosthetic interface hardware that every Hyadean '
                'warship carries. The industrial scale rivals anything in the inner systems '
                'or the other outer factions -- the Hyadean fleet is large, and the demand '
                'for new vessels and replacement components is continuous.\n\n'
                'The light is wrong. Alpha Pegasi is a blue-white giant -- harsh, bright, '
                'casting the industrial cities and the foundry complexes in cold tones that '
                'are strikingly different from the warm amber that illuminates every other '
                'core Hyades system. The residents of Vosthen have lived under this light '
                'for generations and no longer notice. Visitors from Prima Hyadum or Ain '
                'notice immediately -- the shift from golden to blue-white is disorienting, '
                'as though the system belongs to a different cluster. The shipyard workers '
                'consider the visitors\' discomfort amusing. The light is fine. It is the '
                'rest of the cluster that is too warm.\n\n'
                'The prosthetics on Vosthen are the heaviest in the cluster. The shipyard '
                'and foundry work demands hardware that the standard guild modifications '
                'cannot provide: reinforced skeletal frames that let workers lift structural '
                'components that weigh tonnes, thermal shielding integrated into the arms '
                'and hands for working near the foundry pours, and the heavy-duty interface '
                'connections that let a shipyard worker operate the construction equipment '
                'as an extension of their own body. A fully modified heavy-industrial '
                'worker on Vosthen masses two to three times what an unmodified human '
                'weighs, and the additional mass is all hardware. The heavy-lifters\' guild '
                'is the dominant political force on Vosthen, and the guild\'s members are '
                'the most visibly modified people in the cluster -- walking industrial '
                'machinery that happens to have a human being somewhere inside.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='The Slipways',
            short_description='The orbital shipyards -- where the tough, unglamorous warships of the Hyadean fleet are assembled by workers who interface with the construction equipment through their prosthetics.',
            long_description=(
                'The Slipways are Alpha Pegasi\'s orbital shipyards -- the largest military '
                'construction facility in the Hyades cluster and the source of the warships '
                'that define Hyadean military identity. The ships built here are the fleet\'s '
                'character made physical: tough, industrial, unglamorous vessels with exposed '
                'conduits and visible welds, designed to be repaired rather than replaced, '
                'with every component swappable because the assumption is that every '
                'component will eventually need swapping.\n\n'
                'The design philosophy mirrors the prosthetic philosophy. A Hyadean warship '
                'is built the way a Hyadean body is built: incrementally, pragmatically, '
                'with the understanding that what matters is function rather than form and '
                'that the original is less important than what replaces it. A ship that has '
                'served for centuries with every component replaced dozens of times is still '
                'the same ship, the same way a worker who has replaced every limb and most '
                'of their organs is still the same person. The metaphor is not accidental. '
                'The Hyadean relationship with identity -- the question of what persists '
                'when every part is replaced -- applies to ships and bodies equally.\n\n'
                'The shipyard workers interface with the construction equipment through '
                'their prosthetics -- direct neural connections that let them operate '
                'welding systems, assembly cranes, and precision alignment tools as '
                'extensions of their own bodies. A shipyard worker building a warship is '
                'not operating a machine. They are the machine, and the ship they are '
                'building is a larger machine that will be operated by crew members who '
                'are themselves partly machine. The layers of human-machine integration are '
                'deep enough that the philosophers on Secunda Hyadum write papers about '
                'them and the workers on the Slipways do not think about them because '
                'thinking about them does not help with the welding.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Drekham',
            short_description='A mineral-rich mining world -- deep extraction feeding the foundries, worked by miners whose prosthetics are survival equipment in conditions that would kill an organic body.',
            long_description=(
                'Drekham is the system\'s mining world -- a dense, rocky planet with the '
                'mineral deposits that the foundries on Vosthen consume. The mining is deep '
                'extraction -- bore shafts sunk kilometres into a crust that is rich in the '
                'heavy metals and structural alloys that warship construction demands. The '
                'conditions in the deep mines are extreme: heat from the planetary core, '
                'toxic atmospheres in the unventilated sections, and the structural '
                'instability that deep extraction always produces.\n\n'
                'The mining prosthetics on Drekham are the cluster\'s most extreme '
                'industrial modifications. The miners wear reinforced respiratory systems '
                'that filter the toxic atmospheres. Their hands and arms are hardened for '
                'the heat and the impacts that rock extraction produces. Their skeletal '
                'frames are reinforced against the collapses that occur in the deep '
                'sections. The modifications are not optional -- an unmodified miner in '
                'Drekham\'s deep mines would be dead within days. The prosthetics are not '
                'enhancement. They are the minimum equipment for survival, and the mining '
                'guild installs them as part of the job assignment with the same matter-of-'
                'fact process that other industries issue safety equipment.\n\n'
                'The chop shops on Drekham serve the miners who need emergency repairs -- '
                'hardware damaged in the mines that needs to be functional before the next '
                'shift. The repair facilities in the mining towns are the roughest in the '
                'cluster -- fast, competent, and designed for the specific damage profiles '
                'that deep mining produces. A Drekham repair technician can rebuild a '
                'crushed hand in an hour because they rebuild crushed hands every day.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Calstone',
            short_description='A residential world -- where the shipyard and mining workforce raises families under the blue-white star, in communities built to accommodate bodies that are mostly hardware.',
            long_description=(
                'Calstone is the system\'s residential world -- a temperate planet where '
                'the industrial workforce raises families away from the foundries and the '
                'mines. The cities are built to accommodate the heavily modified population '
                '-- wide corridors for workers whose reinforced frames take up more space '
                'than an organic body, reinforced flooring for the mass that heavy-industrial '
                'prosthetics add, and the maintenance facilities integrated into the '
                'residential districts because a worker\'s prosthetics need servicing the '
                'way a worker\'s body needs rest.\n\n'
                'The families on Calstone live with the awareness that modification is '
                'progressive. A young worker arrives at Vosthen\'s foundries with the '
                'starter package -- hands and forearms, the minimum for the job. Over a '
                'career, the modification deepens: the arms are replaced entirely, then the '
                'legs for the workers who need the stability, then the respiratory system '
                'for those who work near the pours, then the skeletal reinforcement for '
                'those who move to the heavy lifting. The spouse watches the partner change '
                'over years. The children grow up with a parent who is progressively less '
                'organic and whose voice, grip, and warmth change with each replacement. '
                'The families adapt because the alternative is a partner who is injured or '
                'dead, and damaged hardware is preferable to damaged flesh.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Ironclad Station',
            short_description='The system\'s orbital port and fleet staging area -- where newly built warships are handed over to the military and the construction crews celebrate with the restraint of people who will start the next ship tomorrow.',
            long_description=(
                'Ironclad Station is Alpha Pegasi\'s primary orbital facility -- part '
                'commercial port, part military staging area, and the venue for the '
                'handover ceremonies when newly completed warships are transferred from the '
                'Slipways to the fleet. The ceremonies are brief and functional -- a Hyadean '
                'warship commissioning involves a systems check, a formal acceptance by the '
                'fleet command, and a drink in the station\'s bar for the construction crew '
                'who built it. The drink is one. The crew starts the next ship tomorrow.\n\n'
                'The station also handles the heavy-duty prosthetics trade that the system '
                'generates. Alpha Pegasi\'s foundries and mining operations produce the '
                'specialised industrial prosthetics that the cluster\'s heavy-industry '
                'workforce uses, and these products are exported from Ironclad Station to '
                'every system with mining or manufacturing operations. The heavy-industrial '
                'prosthetics market is smaller than Brannick\'s budget market or Kelstrand\'s '
                'mid-range but the products are more expensive and the margins are healthy.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Vastrek',
            short_description='A gas giant with fuel processing and military staging -- the last stop for newly built warships before they transit to Ain for deployment.',
            long_description=(
                'Vastrek is the system\'s gas giant -- fuel processing on its moons '
                'supporting both the industrial traffic and the military fleet. Newly '
                'completed warships from the Slipways are fuelled at Vastrek before '
                'transiting to Ain for deployment at the gateway or wherever the guild '
                'council\'s military planning requires. The fuelling is the final step in '
                'the production chain: ore from Drekham, alloy from Vosthen, ship from the '
                'Slipways, fuel from Vastrek, war from wherever the council decides.\n\n'
                'The military staging areas on Vastrek\'s outer moons also serve as the '
                'shakedown zone for new vessels -- systems tested, interfaces verified, and '
                'the crew\'s prosthetic connections to the ship\'s systems calibrated under '
                'operational conditions. A Hyadean warship\'s crew does not merely operate '
                'the ship. The crew interfaces with the ship through prosthetic connections '
                'that make the boundary between operator and vessel a philosophical '
                'question. The calibration ensures that the question is answered '
                'consistently.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Fenholm',
            short_description='An agricultural world feeding fifteen billion -- supplemented by imports from Chamukuy because the system\'s industrial appetite exceeds the local food supply.',
            long_description=(
                'Fenholm is the system\'s agricultural world -- warm enough despite the '
                'blue-white star\'s harsher light, and farmed at a scale that covers most '
                'of the system\'s food demand. The deficit is covered by imports from '
                'Chamukuy -- Alpha Pegasi\'s population is large and its industrial '
                'orientation intense enough that local agriculture cannot meet the full '
                'demand. The farming follows the standard Hyadean model: prosthetically '
                'modified workers with the agricultural package, managed by the '
                'agricultural guild.\n\n'
                'The farmers on Fenholm work under the blue-white light that distinguishes '
                'the system from the rest of the cluster. The crops are engineered for the '
                'different spectral output -- the photosynthesis calculations are adjusted '
                'for blue-white rather than amber, and the crop strains reflect the '
                'adaptation. The farmers consider this unremarkable. The agricultural '
                'engineers who designed the crop strains consider it one of their more '
                'interesting challenges.'
            ),
            population=1_000_000_000,
        ),
    ],
    short_description='The forge of the fleet -- fifteen billion people building warships under the cluster\'s only blue-white star, with prosthetics so heavy the workers are walking industrial machinery.',
    long_description=(
        'Alpha Pegasi builds the Hyadean fleet. The system is the cluster\'s heavy '
        'industry centre -- the shipyards that construct the tough, unglamorous '
        'warships that define Hyadean military identity, the foundries that produce '
        'the structural materials, and the mines that supply the ore. Fifteen billion '
        'people live here, and the system\'s identity is the fleet.\n\n'
        'The star is wrong for the Hyades. Alpha Pegasi is a blue-white giant -- the '
        'only one in the core cluster, casting cold, harsh light over the foundries '
        'and the shipyards instead of the warm amber that illuminates every other '
        'Hyadean system. The visual difference is striking. The workers do not notice. '
        'Visitors from the amber systems find the blue-white disorienting, as though '
        'the system belongs to a different cluster.\n\n'
        'The prosthetics are the heaviest in the Hyades. The foundry and shipyard '
        'work demands reinforced skeletal frames, thermal shielding, and the heavy-'
        'duty interfaces that let workers operate construction equipment as extensions '
        'of their own bodies. A fully modified heavy-industrial worker masses two to '
        'three times an organic human. The heavy-lifters\' guild is the dominant '
        'political force. The mining prosthetics on Drekham are the cluster\'s most '
        'extreme -- not enhancement but the minimum equipment for survival in '
        'conditions that would kill an organic body in days.\n\n'
        'The ships built at the Slipways mirror the prosthetic philosophy: '
        'incremental, pragmatic, designed to be repaired rather than replaced. A ship '
        'that has served for centuries with every component swapped is still the same '
        'ship, the same way a worker who has replaced every limb is still the same '
        'person. The metaphor is not accidental. The Hyadean relationship with '
        'identity -- what persists when every part is replaced -- applies to ships '
        'and bodies equally. The philosophers write papers about it. The workers do '
        'not think about it because thinking about it does not help with the welding.'
    ),
    cluster=StarClusters.HYADES,
)

SCHEAT = System(
    name='Scheat',
    star='Red giant (M2.5II-III), semi-regular variable -- brightness fluctuates unpredictably over weeks, casting a dim red light that brightens and fades as though the star is breathing',
    population=6_000_000_000,
    distance_to_sol=196.0,
    stellar_objects=[
        StellarObject(
            name='Carriston',
            short_description='The organ bank -- three billion people in a system that runs the full prosthetic cycle: the poor sell their flesh to get metal, the rich buy the flesh to replace their metal.',
            long_description=(
                'Carriston is Scheat\'s primary world and the place where the Hyadean '
                'prosthetic economy reveals its full shape. The standard industry is here '
                'and thriving -- modification clinics, guild-certified installations, the '
                'chop shops that serve workers who need hardware. The poor come to Carriston '
                'the same way they come to modification clinics across the cluster: to sell '
                'their organic parts for prosthetics and the credits to survive. A young '
                'worker sells a healthy hand, receives a mechanical one and a payment that '
                'covers a month\'s rent. This is standard. This is the cluster.\n\n'
                'What makes Carriston different is what happens next. The organic hand is '
                'not discarded. It is preserved -- catalogued, stored in the Vaults, and '
                'added to an inventory of millions of organs, limbs, and tissue samples that '
                'the system\'s other clients will browse the way shoppers browse a catalogue. '
                'The Reversal is the product: for clients who can afford it, Carriston\'s '
                'clinics install organic material back -- replacing a prosthetic with flesh, '
                'restoring what the standard economy removed. The food chain is undisguised: '
                'the poor sell their bodies upward, piece by piece, and the wealthy buy the '
                'pieces back when they decide that metal is not enough.\n\n'
                'The wealthy clients come from across the cluster and beyond. Hyadeans who '
                'modified young and want their hands back at sixty. The old whose degraded '
                'biology rejects newer hardware and who need an organic replacement. '
                'Inner-system citizens with illegal prosthetics seeking restoration. Clients '
                'from other factions. The wealthiest arrive with their preferred donors in '
                'tow -- people who have agreed, for a price, to be modified on Carriston so '
                'that their specific organic material can be harvested, preserved, and '
                'installed in the client who brought them. The donor receives prosthetics '
                'and payment. The client receives the donor\'s flesh. The transaction is '
                'voluntary, legal, and conducted with the clinical professionalism of an '
                'industry that has stopped pretending the ethics are simple.\n\n'
                'The out-of-system traffic is heavy. Scheat draws visitors from every '
                'faction and from MERIT space -- people who have heard that there is one '
                'place in the galaxy where you can buy back what the prosthetic economy '
                'took, or buy what someone else\'s economy took from them. The clinics '
                'profit from both ends: credits from the poor who sell, credits from the '
                'rich who buy.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Vaults',
            short_description='The tissue preservation facilities -- underground, temperature-controlled, holding millions of preserved organs and limbs in the largest biological archive in the galaxy.',
            long_description=(
                'The Vaults are the foundation that the Reversal is built on -- vast '
                'underground preservation facilities on Carriston\'s northern continent, '
                'temperature-controlled and environmentally sealed, holding the biological '
                'material that makes the Reversal possible. The scale is staggering: '
                'millions of preserved organs, limbs, tissue samples, and the neural '
                'material that is the most valuable and most difficult to preserve. The '
                'Vaults are the largest biological archive in the galaxy, and the inventory '
                'is catalogued with the precision that the value of the contents demands.\n\n'
                'The material comes from two sources. The first is the modification clinics '
                'on Carriston itself -- every client who is modified on Carriston has the '
                'option to preserve their removed organic material, for a fee, in the '
                'Vaults. Many do. The fee is an investment: if they want the material back '
                'later, it is there. If they do not, the material enters the general '
                'inventory and becomes available to other clients. The second source is '
                'acquisition from other systems -- the clinics on Carriston purchase '
                'preserved organic material from modification facilities across the '
                'cluster, from hospitals, from the chop shops that have learned to save '
                'rather than discard. The supply chain is extensive, well-organised, and '
                'operates in the uncomfortable space between medical procurement and the '
                'organ trade that MERIT\'s ethics would condemn.\n\n'
                'The Vaults employ preservation specialists whose skills are unique to '
                'Scheat -- technicians who understand the biology of long-term tissue '
                'preservation at a level that no other system\'s medical community matches, '
                'because no other system\'s medical community needs to. The specialists '
                'maintain the material in the Vaults with the care of archivists tending '
                'irreplaceable documents, because in a civilisation that discards flesh as '
                'waste, preserved flesh is irreplaceable.'
            ),
            population=0,
        ),
        StellarObject(
            name='Nathren',
            short_description='A second world specialising in the biological sciences that the Reversal requires -- tissue growth, organ cultivation, and the research that pushes the limits of what can be restored.',
            long_description=(
                'Nathren is the system\'s research and cultivation world -- a cooler planet '
                'where the biological sciences that underpin the Reversal are developed and '
                'where the organic material that the Vaults cannot supply is grown. The '
                'cultivation facilities on Nathren produce lab-grown organs, tissue, and '
                'the biological components that supplement the harvested material from the '
                'Vaults when the inventory runs short or when a client requires material '
                'that the Vaults do not carry.\n\n'
                'The research on Nathren pushes the limits of what the Reversal can '
                'achieve. The current technology can replace a prosthetic limb with a '
                'biological one, can install a preserved heart or liver, can restore the '
                'organic function that the prosthetic replaced. What it cannot reliably do '
                'is restore sensation -- the neural connections between a replacement '
                'biological limb and the brain are imperfect, and a Reversal client who '
                'receives a new organic hand may find that the hand works but does not '
                'feel the way the original did. The researchers on Nathren are working on '
                'this problem. The neural interface technology that the Hyades developed '
                'for prosthetics is, ironically, the most promising approach to restoring '
                'the biological connections that the prosthetics replaced.\n\n'
                'Nathren\'s population is smaller than Carriston\'s and more academic -- '
                'researchers, biologists, and the medical professionals who train for the '
                'Reversal procedures. The culture is quieter and more reflective than the '
                'commercial intensity of Carriston\'s clinics. The researchers on Nathren '
                'think about what the Reversal means in ways that the clinic operators on '
                'Carriston do not have time for: what it means to give flesh back to people '
                'who gave it up, whether the restored hand is the same hand, and whether '
                'the person who wants their body back is the same person who gave it away.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Shelvane',
            short_description='A world for the recovering -- where Reversal clients spend months relearning how to use organic limbs that feel different from the prosthetics they replaced.',
            long_description=(
                'Shelvane is where the Reversal patients recover. The planet is temperate '
                'and quiet -- designed for convalescence in the way that Solace on Pollux '
                'is designed for the recovery of the reanimated. The comparison is apt: '
                'both systems manage the aftermath of a procedure that changes what the '
                'patient is, and both require time and patience that the patients did not '
                'anticipate needing.\n\n'
                'The recovery from a Reversal is longer than the recovery from a prosthetic '
                'installation. The body must accept the biological material. The neural '
                'connections must establish themselves. The brain, which has spent years or '
                'decades interfacing with mechanical hardware, must relearn how to operate '
                'organic limbs that respond differently -- slower, less precise, but with '
                'the warmth and sensation that the prosthetics could not provide. The '
                'patients on Shelvane describe the experience as relearning their own body '
                '-- the hand that was mechanical for thirty years is now flesh, and the '
                'flesh does not respond the way the metal did, and the patient must learn '
                'to accept the imprecision as the price of the warmth.\n\n'
                'Some patients cannot adjust. The organic replacement feels wrong -- too '
                'slow, too imprecise, too vulnerable after years of mechanical reliability. '
                'A small percentage of Reversal clients return to Carriston and ask to have '
                'the prosthetic reinstalled, trading the flesh they paid to recover for the '
                'metal they paid to escape. The clinics perform the reinstallation without '
                'comment. In Scheat, the body is a choice that can be made and remade, and '
                'the only judgement is the price.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Scarren Station',
            short_description='The system\'s orbital port -- where the out-of-system clients arrive discreetly and the organic material shipments are processed with the clinical efficiency of an industry that trades in flesh.',
            long_description=(
                'Scarren Station is Scheat\'s primary orbital facility -- a station that '
                'handles the system\'s distinctive traffic with the discretion that the '
                'clientele demands. The out-of-system arrivals -- the wealthy Hyadeans '
                'seeking Reversals, the inner-system citizens with illegal prosthetics, '
                'the visitors from other factions -- dock at Scarren and are processed '
                'through customs that is designed to be thorough and discreet. The station '
                'does not advertise what it offers. The clients who arrive already know.\n\n'
                'The station also processes the incoming organic material shipments -- '
                'preserved tissue from modification clinics across the cluster, transported '
                'in climate-controlled containers to the standards that the Vaults require. '
                'The shipments are catalogued, inspected, and transferred to Carriston\'s '
                'preservation facilities with the logistical precision of a supply chain '
                'that handles material worth more per gram than most manufactured goods. '
                'The dockworkers who process these shipments are accustomed to the cargo. '
                'The visitors who see the containers being moved are sometimes not.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Ruthven',
            short_description='A gas giant with fuel processing -- supporting the out-of-system traffic and the organic material supply ships under the pulsing red light of the variable star.',
            long_description=(
                'Ruthven is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The traffic pattern is distinctive: '
                'the out-of-system clients arriving for Reversals, the supply ships carrying '
                'organic material from across the cluster, and the departing clients '
                'leaving with new bodies or newly restored old ones. The fuel workers '
                'process the traffic under the red light of the variable star -- a dim '
                'illumination that brightens and fades on an unpredictable cycle, as though '
                'the star is breathing. The fuel workers have learned to ignore the '
                'fluctuation. Visitors find it unsettling in ways they cannot articulate, '
                'as though the system itself is alive and uncertain.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Garmond',
            short_description='An agricultural world feeding the system -- standard Hyadean farming, notable only because the food is grown under a red light that makes the crops look wrong and taste fine.',
            long_description=(
                'Garmond is the system\'s agricultural world -- warm enough despite the red '
                'giant\'s dimmer output, farmed by prosthetically modified workers with the '
                'standard agricultural package. The crop strains are engineered for the '
                'red spectral output -- photosynthesis calibrated for light that is dimmer '
                'and redder than the amber that most Hyadean agricultural worlds receive. '
                'The crops look wrong to visitors from other systems -- the colours are '
                'shifted, the growth patterns are different, and the fields under the dim '
                'red light have a quality that visitors describe as unsettling. The food '
                'tastes fine. The appearance is the star\'s fault, not the farmers\'.'
            ),
            population=800_000_000,
        ),
    ],
    short_description='The organ bank -- six billion people in a system that runs the full cycle: the poor sell their flesh for prosthetics, the rich buy the flesh back, and the system profits from both transactions.',
    long_description=(
        'Scheat runs the full cycle of the Hyadean prosthetic economy in a single '
        'system. The standard industry is here -- modification clinics, guild '
        'installations, the chop shops that serve the workers who need hardware they '
        'cannot afford through official channels. The poor come to Scheat and sell '
        'their organic parts for prosthetics, the same as anywhere in the cluster. '
        'The difference is what happens to the flesh they leave behind. On other '
        'worlds, the organic material is discarded. On Scheat, it is preserved.\n\n'
        'The Vaults on Carriston hold the result -- millions of preserved organs, '
        'limbs, and tissue samples in the largest biological archive in the galaxy. '
        'The supply flows upward from the poor: a worker who sells a healthy hand for '
        'a mechanical one provides the inventory that a wealthy client will later '
        'purchase to replace the mechanical hand they no longer want. The food chain '
        'is clear and undisguised. The poor sell their flesh for prosthetics and the '
        'credits to survive. The rich buy the flesh back -- either their own, '
        'preserved from an earlier modification, or someone else\'s, selected from the '
        'Vaults\' catalogue. Wealthy clients from out of system often arrive with '
        'their preferred donors in tow -- people who have agreed, for a price, to '
        'undergo modification on Scheat so that their specific organic material can '
        'be harvested, preserved, and installed in the client who brought them.\n\n'
        'The out-of-system traffic is heavy. The wealthy come from across the cluster '
        'and beyond: Hyadeans who modified young and want their bodies back, '
        'inner-system citizens with illegal prosthetics seeking restoration, clients '
        'from other factions who have heard that Scheat can provide what no other '
        'system offers. Nathren\'s research pushes the limits -- growing replacement '
        'tissue, solving the neural restoration problem that makes reinstalled flesh '
        'feel different from the original. Shelvane is where the patients recover, '
        'relearning organic limbs that are slower and less precise than the '
        'prosthetics they replaced.\n\n'
        'The star is a semi-regular variable -- a red giant whose brightness '
        'fluctuates unpredictably, brightening and fading as though the star is '
        'breathing. The light falls on a system that profits from every direction: '
        'credits from the poor who sell their flesh, credits from the rich who buy '
        'it back, credits from the prosthetics that replace what was sold, and '
        'credits from the Reversal that reinstalls what was bought. The cycle is '
        'closed. The system takes a margin on every transaction. In Scheat, the '
        'body is currency, and the exchange rate favours the wealthy.'
    ),
    cluster=StarClusters.HYADES,
)

GENIB = System(
    name='Genib',
    star='Blue-white subgiant (B2IV), a Beta Cephei variable that pulsates regularly -- brightness fluctuating on a precise cycle that the traders have built their schedules around',
    population=8_000_000_000,
    distance_to_sol=390.0,
    stellar_objects=[
        StellarObject(
            name='Marchalan',
            short_description='The cluster\'s trade capital -- five billion people in a system where Hyadean prosthetics are adapted, repackaged, and sold to every faction in the galaxy.',
            long_description=(
                'Marchalan is where the Hyades sells itself to the rest of the galaxy. The '
                'planet is the cluster\'s primary trade hub -- the system where Hyadean '
                'prosthetic technology is adapted for non-Hyadean bodies, repackaged for '
                'non-Hyadean markets, and exported to every faction that will buy it, '
                'which is all of them. The Antares cluster buys Hyadean interface '
                'technology to supplement its stim-based enhancement. The Canopus cluster '
                'buys Hyadean components for the mechanical systems that support their '
                'reanimation infrastructure. The Polaris cluster buys neural interface '
                'hardware that complements their own integration technology. Even MERIT '
                'space absorbs Hyadean prosthetics through the smuggling networks that '
                'run through Procyon\'s grey markets.\n\n'
                'The export trade on Marchalan is not the same as the domestic prosthetics '
                'industry. The hardware sold to other factions is adapted -- recalibrated '
                'for bodies that are not progressively modified from adolescence, designed '
                'for integration with biological systems that have not been prepared by '
                'years of guild-standard modification. An export-grade Hyadean prosthetic '
                'is a different product from a guild-standard installation: more self-'
                'contained, less reliant on the supporting modifications that a Hyadean '
                'citizen carries, and packaged with the documentation and training that '
                'non-Hyadean physicians need to install and maintain it. The adaptation '
                'industry employs thousands of engineers whose specialty is making Hyadean '
                'technology work in bodies that were not built for it.\n\n'
                'The trading houses on Marchalan are the system\'s defining institutions '
                '-- commercial operations that have been brokering prosthetic exports for '
                'centuries, with relationships across every faction and expertise in the '
                'regulatory environments that govern prosthetic technology in each market. '
                'The Antarian market has different standards from the Canopan market, which '
                'has different standards from the MERIT black market, which has no standards '
                'at all. The trading houses navigate these differences with the fluency of '
                'people who have been doing it for longer than most of their clients\' '
                'governments have existed.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Revnik',
            short_description='The adaptation world -- where domestic Hyadean prosthetics are re-engineered for non-Hyadean bodies and the export-grade hardware is manufactured.',
            long_description=(
                'Revnik is the system\'s manufacturing world -- but where other systems '
                'produce prosthetics for the domestic market, Revnik produces exclusively '
                'for export. The factories here do not make the standard guild hardware '
                'that Hyadean citizens use. They make the adapted versions: prosthetics '
                'redesigned for bodies that have not undergone the progressive modification '
                'that the guild system assumes, interfaces simplified for physicians who '
                'were not trained in Hyadean installation techniques, and the modular '
                'components that let a non-Hyadean buyer install individual prosthetics '
                'without committing to the full guild package.\n\n'
                'The engineering challenge is substantial. A guild-standard Hyadean '
                'prosthetic is designed to work within an ecosystem of modifications -- '
                'the hand connects to the arm, which connects to the shoulder interface, '
                'which connects to the neural bridge, which connects to the central '
                'nervous system through a series of graduated installations that the guild '
                'manages over years. An export-grade prosthetic must work as a standalone '
                'unit, integrated into a body that has none of the supporting '
                'infrastructure. The engineers on Revnik describe the work as building a '
                'wheel that functions without the rest of the vehicle.\n\n'
                'The chop shops on Revnik serve a different market than the chop shops on '
                'other worlds. The clients are not Hyadean workers modifying for employment '
                'but foreign visitors who want Hyadean hardware installed quickly and '
                'cheaply before returning home. The back-street operators on Revnik '
                'specialise in fast installations for non-Hyadean bodies -- a service that '
                'the guild system does not officially endorse and that the trading houses '
                'tolerate because the clients generate demand for the export products.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='The Emporium',
            short_description='The system\'s primary orbital station -- the largest prosthetics trading installation in the galaxy, where buyers from every faction browse the catalogue.',
            long_description=(
                'The Emporium is Genib\'s primary orbital station and the largest '
                'prosthetics trading installation in the galaxy. The station is built '
                'around its trading floor -- an enormous commercial space where the '
                'trading houses display their export catalogues and buyers from every '
                'faction in the galaxy browse, negotiate, and purchase. The floor is '
                'organised by product category: limbs in one section, organs in another, '
                'neural interfaces in a third, and the specialised hardware -- mining '
                'prosthetics, agricultural prosthetics, military-grade modifications -- in '
                'dedicated zones that the relevant buyers know to find.\n\n'
                'The Emporium is neutral ground in the way that Mirzam\'s Bazaar is neutral '
                'ground in the Canopus cluster -- a trading space where factional rivalries '
                'are suspended because the commerce is more valuable than the hostility. '
                'Antarian buyers and Canopan buyers and Polaran buyers and the smugglers '
                'who supply MERIT\'s black market all walk the same trading floor, '
                'separated by commercial interest rather than political alignment. The '
                'security is heavy, professional, and focused on preventing disputes from '
                'becoming violent. The disputes are frequent. The violence is rare. The '
                'commerce continues.\n\n'
                'The Emporium also hosts the demonstration facilities where the trading '
                'houses showcase their products to potential buyers. The demonstrations are '
                'impressive -- live installations on volunteer subjects, stress tests of '
                'export-grade hardware, and the comparison displays that show how Hyadean '
                'prosthetics outperform the competing technologies that the other factions '
                'produce. The demonstrations are sales pitches. They are also genuine, '
                'because the technology is genuinely superior. Hyadean prosthetics are the '
                'best in the galaxy. The Emporium exists to make sure everyone knows it.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Stellwick',
            short_description='An industrial world producing the raw components that the export factories on Revnik assemble -- the supply chain behind the trade.',
            long_description=(
                'Stellwick is the system\'s component manufacturing world -- the supply '
                'chain behind Revnik\'s export factories. The planet produces the raw '
                'prosthetic components -- joints, actuators, neural connectors, synthetic '
                'tissue interfaces, and the hundreds of subcomponents that a finished '
                'prosthetic contains. The manufacturing is high-volume and high-precision '
                '-- the export market demands both, because the buyers are spending '
                'significant money on technology that must work in bodies the technology '
                'was not originally designed for.\n\n'
                'The workforce on Stellwick is guild-standard -- modified for manufacturing '
                'with the precision-workers\' and interface specialists\' hardware that the '
                'component production requires. The workers produce export-grade components '
                'while wearing domestic-grade prosthetics, and the quality difference '
                'between what they make and what they wear is a point of dry humour on the '
                'factory floors.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Pendrik',
            short_description='A gas giant with fuel processing at trade-hub scale -- supporting the inter-faction traffic that makes Genib the prosthetics market of the galaxy.',
            long_description=(
                'Pendrik is the system\'s gas giant -- fuel processing on its moons at a '
                'scale that matches the inter-faction traffic Genib\'s trade generates. '
                'The traffic is diverse: Hyadean freighters carrying export hardware, '
                'Antarian traders, Canopan buyers, Polaran delegation ships, and the '
                'independent operators who carry prosthetic technology to the corners of '
                'the galaxy that the official trade channels do not reach. The fuel '
                'operations process them all without distinction. Credits are credits. '
                'The fuel processors\' guild does not care which faction the ship belongs '
                'to as long as the payment clears.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Holworth',
            short_description='An agricultural world feeding the system -- supplemented by imports, because Genib\'s economy is trade rather than self-sufficiency.',
            long_description=(
                'Holworth is the system\'s agricultural world -- warm enough under the '
                'blue-white star\'s light, farmed by the standard prosthetically modified '
                'workforce. The output covers most of the system\'s food demand but not all '
                '-- the deficit is covered by imports from Chamukuy. Genib\'s economy is '
                'oriented toward trade rather than self-sufficiency, and the guild council '
                'has accepted the dependency on food imports as a reasonable trade-off for '
                'the revenue that the export market generates.\n\n'
                'The farmers on Holworth are the system\'s least cosmopolitan residents -- '
                'working the fields under the pulsating blue-white star while the traders '
                'on Marchalan negotiate with buyers from civilisations the farmers have '
                'never visited. The farmers do not mind. The trade brings the credits that '
                'keep the system funded. The farmers grow the food that keeps the traders '
                'fed. The relationship is symbiotic and does not require the farmers to '
                'care about the Antarian market for neural interfaces.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The cluster\'s shopfront -- eight billion people adapting and selling Hyadean prosthetics to every faction in the galaxy.',
    long_description=(
        'Genib is where the Hyades sells its technology to the rest of the galaxy. '
        'The system is the cluster\'s primary export hub -- the place where domestic '
        'Hyadean prosthetics are adapted for non-Hyadean bodies, repackaged for '
        'non-Hyadean markets, and sold to every faction that will buy. The Antares '
        'buys interface technology. Canopus buys mechanical components. Polaris buys '
        'neural hardware. MERIT absorbs Hyadean prosthetics through Procyon\'s grey '
        'markets. The buyers are officially hostile. The commerce flows regardless.\n\n'
        'The trading houses on Marchalan have been brokering prosthetic exports for '
        'centuries, with relationships across every faction and expertise in the '
        'regulatory environments of each market. Revnik manufactures the export-grade '
        'hardware -- prosthetics re-engineered for bodies that lack the supporting '
        'modifications the guild system assumes. The engineering challenge is making '
        'a wheel that works without the rest of the vehicle. The Emporium -- the '
        'system\'s orbital station and the largest prosthetics trading installation '
        'in the galaxy -- hosts buyers from every faction on a neutral trading floor '
        'where the commerce is more valuable than the hostility.\n\n'
        'The star is a Beta Cephei variable -- pulsating on a precise, regular cycle '
        'that the traders have built their schedules around. Where Scheat\'s variable '
        'star fluctuates unpredictably, Genib\'s pulsates like a heartbeat, and the '
        'trading day rises and falls with it. The metaphor is not lost on the '
        'residents: the system runs on a pulse, and the pulse is commerce.\n\n'
        'Eight billion people in a system that makes money by selling the cluster\'s '
        'defining technology to everyone else. The guilds that manufacture domestically '
        'view the export market with complicated feelings -- the revenue is welcome, '
        'the idea that non-Hyadean bodies are wearing Hyadean hardware is culturally '
        'uncomfortable, and the engineers on Revnik who adapt the technology for '
        'foreign bodies are considered by some guilds to be diluting what the '
        'prosthetics represent. The revenue wins the argument. The revenue always '
        'wins the argument.'
    ),
    cluster=StarClusters.HYADES,
)

ENIF = System(
    name='Enif',
    star='Orange supergiant (K2Ib), approximately 12,000 times Sol luminosity -- a massive, swollen star prone to recorded flare events, illuminating a system where the work is too dangerous for organic bodies and too valuable to stop',
    population=5_000_000_000,
    distance_to_sol=690.0,
    stellar_objects=[
        StellarObject(
            name='Durngate',
            short_description='The deepest mines in the cluster -- two billion people extracting the rare materials that premium prosthetics require, in conditions where modification is not enhancement but the minimum cost of survival.',
            long_description=(
                'Durngate is a dense, mineral-rich world with the most valuable ore deposits '
                'in the Hyades cluster. The minerals extracted here are the ones that '
                'premium prosthetics require -- the rare alloys for the high-end neural '
                'connectors, the compounds used in the interface materials that the '
                'precision-workers\' and interface specialists\' guilds depend on, and the '
                'structural metals that the military-grade hardware demands. The deposits '
                'are deep. The extraction is difficult. The conditions are the worst in the '
                'cluster.\n\n'
                'The mining on Durngate is deep extraction at a scale and difficulty that '
                'Drekham on Alpha Pegasi cannot match. The bore shafts descend kilometres '
                'into a crust that is geologically active -- heat from the core, toxic '
                'gas pockets that breach without warning, seismic instability that '
                'collapses tunnel sections with a regularity the mining guild has learned '
                'to budget for rather than prevent. The conditions in the deep mines would '
                'kill an unmodified human in hours. The prosthetics that the miners wear '
                'are not enhancement. They are the equipment that makes it possible to '
                'enter the mines and come back.\n\n'
                'The mining prosthetics on Durngate are the most extreme in the cluster -- '
                'more heavily modified than even the heavy-lifters on Vosthen. The miners '
                'carry reinforced respiratory systems that filter atmospheres toxic enough '
                'to dissolve organic lung tissue. Their skeletal frames are hardened against '
                'the crush pressures in the deepest sections. Their sensory packages '
                'include seismic monitors that detect the micro-tremors that precede a '
                'collapse -- a warning system wired into the miner\'s nervous system that '
                'triggers an involuntary flinch response faster than conscious thought. '
                'The miners describe the flinch as the prosthetic saving your life before '
                'you know it needs saving.\n\n'
                'The star adds a complication. Enif is an orange supergiant prone to flare '
                'events -- sudden, dramatic brightenings that flood the system with '
                'radiation. The flares are irregular but recorded: the mining operations '
                'have adapted by building the surface infrastructure to withstand the '
                'radiation spikes and by designing the mine entrances as radiation shelters. '
                'The deep mines are naturally shielded by the rock above them. The surface '
                'crews are the ones who suffer when a flare hits, and the surface '
                'prosthetics include radiation-hardened components that the deep miners do '
                'not need and that add to the cost of working in a system where the star '
                'itself is trying to kill you.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Blackvane',
            short_description='A second mining world -- strip extraction on a barren surface, where the work is less deep but the flare exposure is worse and the prosthetic replacement rate is the highest in the cluster.',
            long_description=(
                'Blackvane is the system\'s second mining world -- a barren, airless body '
                'where the mineral extraction is surface and shallow-bore rather than the '
                'deep mining that Durngate specialises in. The deposits on Blackvane are '
                'less valuable individually but easier to access -- strip mining operations '
                'that tear the surface apart with industrial equipment operated by miners '
                'whose prosthetics are calibrated for a different set of hazards.\n\n'
                'The hazard on Blackvane is exposure. The miners work on the surface, '
                'under the orange supergiant\'s swollen disc, and when a flare event '
                'occurs they are directly in the radiation path. The surface installations '
                'include shelters, but the work does not stop during flares -- the mining '
                'guild has calculated the productivity loss against the health cost and '
                'decided that prosthetic replacement is cheaper than downtime. The miners '
                'on Blackvane have the highest prosthetic replacement rate in the cluster '
                '-- radiation-damaged components swapped out on a cycle that the '
                'maintenance facilities in the mining camps have optimised to the point '
                'where a full arm replacement takes less time than a shift meal.\n\n'
                'The chop shops on Blackvane are the roughest in the cluster -- faster '
                'than Drekham\'s, cruder than Scheat\'s, and staffed by technicians whose '
                'only qualification is speed. A miner walks in with a radiation-scorched '
                'arm, the technician strips it, installs the replacement from the stack, '
                'and the miner walks out and goes back to work. The quality is adequate. '
                'The speed is the point. The mining guild considers the replacement cycle '
                'a consumable cost, like fuel or drill bits.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Cordane',
            short_description='A residential and maintenance world -- where the mining workforce recovers between rotations and the prosthetic maintenance facilities run continuously.',
            long_description=(
                'Cordane is the system\'s residential world -- a planet far enough from Enif '
                'that the flare exposure is manageable, where the mining workforce lives '
                'between rotations to Durngate and Blackvane. The planet is functional '
                'rather than comfortable -- housing built to the standard that the mining '
                'guild considers adequate, with the maintenance facilities that the '
                'workforce\'s heavily modified bodies require.\n\n'
                'The maintenance facilities on Cordane run continuously. The miners\' '
                'prosthetics take damage faster than any other workers\' in the cluster, '
                'and the repair and replacement cycle is constant. A miner returning from '
                'a Durngate rotation goes to maintenance before going home -- the hardware '
                'is inspected, the damaged components are replaced, and the systems that '
                'keep the miner alive in the deep mines are verified as functional before '
                'the next rotation begins. The maintenance technicians on Cordane are '
                'specialists in mining-grade prosthetics -- they see damage patterns that '
                'no other facility in the cluster encounters, and the repair techniques '
                'they have developed are proprietary knowledge that the mining guild does '
                'not share.\n\n'
                'The families on Cordane live with the awareness that the mines take '
                'pieces. A miner\'s career is measured in replacements -- not the gradual '
                'progression of guild modification that workers in other systems experience, '
                'but the repeated emergency replacements that the mines demand. A miner '
                'who has worked Durngate for twenty years has had every major component '
                'replaced multiple times. The original prosthetics installed at the start '
                'of the career are long gone. The miner is the same person. The body is '
                'entirely different. The families track the changes the way families '
                'everywhere track the wear that a hard job puts on the person they love.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Trevask Station',
            short_description='The system\'s orbital port -- where the mineral output is loaded for export and the replacement prosthetics are unloaded by the shipment.',
            long_description=(
                'Trevask Station is Enif\'s primary orbital facility -- a heavy industrial '
                'port that handles two cargo streams: the mineral output heading to the '
                'cluster\'s manufacturing systems, and the replacement prosthetics arriving '
                'from every factory in the Hyades. Enif consumes prosthetics the way the '
                'mines consume drill bits -- at a rate that the guild system treats as a '
                'supply-chain problem rather than a human one. The shipments of replacement '
                'arms, hands, respiratory units, and skeletal components that arrive at '
                'Trevask are stored in warehouses and distributed to the mining worlds on a '
                'schedule matched to the damage rate.\n\n'
                'The station is built to withstand the flare events -- heavy radiation '
                'shielding on all external surfaces, and the emergency protocols that '
                'bring all docking operations inside when the flare monitors detect an '
                'event building. The station crews are modified with the radiation-hardened '
                'packages that the star demands. Even the orbital infrastructure in Enif '
                'is designed around the assumption that the star is hostile.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Osbreth',
            short_description='A gas giant in the outer system -- fuel processing and the one posting in Enif where the star\'s flares are a distant problem rather than a daily hazard.',
            long_description=(
                'Osbreth is the system\'s gas giant -- fuel processing on its moons '
                'supporting the mining traffic and the freighters that carry the mineral '
                'output to the cluster. The outer-system position means the flare exposure '
                'is attenuated -- the fuel workers on Osbreth\'s moons experience the '
                'flares as elevated radiation readings rather than the emergency events '
                'that the inner-system workers endure. The posting is considered the best '
                'in the system, which is a relative assessment -- the best posting in Enif '
                'is still a posting in Enif.\n\n'
                'The fuel workers wear standard fuel-processing prosthetics rather than the '
                'mining-grade or radiation-hardened hardware that the inner system demands. '
                'They are the least modified workforce in the system, and they are aware '
                'of the privilege. Workers who have served rotations in the inner system '
                'before transferring to Osbreth describe the posting as the first time '
                'they could forget what their prosthetics were for.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Greathall',
            short_description='An agricultural world feeding the system -- producing food under a star whose flares periodically scorch the crops and require the agricultural cycle to account for radiation damage.',
            long_description=(
                'Greathall is the system\'s agricultural world -- farmed at a scale that '
                'feeds five billion people, under conditions that no other agricultural '
                'world in the cluster faces. The flare events from the orange supergiant '
                'periodically flood the surface with radiation that damages crops, '
                'contaminates soil, and disrupts the growing cycle. The agricultural '
                'operations on Greathall are designed around the flares -- crop strains '
                'engineered for radiation resistance, growing cycles timed to maximise '
                'yield between expected flare windows, and the emergency harvest protocols '
                'that bring in whatever is ready when a major flare is detected.\n\n'
                'The farmers on Greathall are modified with both the standard agricultural '
                'prosthetics and the radiation-hardened components that the star demands. '
                'The double modification is expensive -- the agricultural guild and the '
                'mining guild have negotiated a cost-sharing arrangement for the radiation '
                'hardware, because the mining guild needs the food and the agricultural '
                'guild cannot afford the radiation upgrades alone. The arrangement is one '
                'of the cluster\'s more pragmatic examples of inter-guild cooperation: '
                'two guilds sharing the cost of keeping people alive because both guilds '
                'need them alive for different reasons.'
            ),
            population=700_000_000,
        ),
    ],
    short_description='The deepest mines under the most dangerous star -- five billion people extracting the materials the cluster cannot do without, in conditions that consume prosthetics the way the mines consume drill bits.',
    long_description=(
        'Enif is the Hyades cluster\'s most extreme inhabited system. The star is an '
        'orange supergiant -- 12,000 times Sol\'s luminosity, prone to flare events '
        'that flood the system with radiation at irregular intervals. The worlds are '
        'mineral-rich, holding the rare alloys and compounds that premium prosthetics '
        'require. The extraction is deep, dangerous, and essential. The cluster '
        'cannot build its best hardware without Enif\'s output.\n\n'
        'The mining prosthetics on Durngate are the most extreme in the cluster -- '
        'reinforced respiratory systems, hardened skeletal frames, seismic monitors '
        'wired into the nervous system that trigger an involuntary flinch response '
        'before the miner consciously registers the danger. The prosthetics are not '
        'enhancement. They are the minimum equipment for survival in conditions that '
        'would kill an unmodified human in hours. Blackvane\'s surface miners work '
        'under the supergiant\'s direct radiation -- the mining guild has calculated '
        'that prosthetic replacement is cheaper than downtime, and the replacement '
        'rate is the highest in the cluster.\n\n'
        'The star adds the dimension that makes Enif uniquely hostile. The flare '
        'events are irregular and intense -- sudden brightenings that force the '
        'surface operations to either shelter or absorb the radiation cost. The '
        'infrastructure is built to withstand the flares. The prosthetics are '
        'designed to be replaced when the radiation damages them. The agricultural '
        'cycle accounts for crop damage. The entire system is engineered around the '
        'assumption that the star is actively hostile.\n\n'
        'Five billion people live here because the minerals are worth the cost. The '
        'miners\' careers are measured in replacements -- every major component '
        'swapped multiple times over a working life, the original prosthetics long '
        'gone, the body entirely different from the one that started. The families '
        'on Cordane track the changes the way families everywhere track the wear '
        'that a hard job puts on the person they love. Enif takes pieces. The '
        'cluster needs what Enif provides. The exchange continues.'
    ),
    cluster=StarClusters.HYADES,
)

ALPHARD = System(
    name='Alphard',
    star='Orange giant (K3II-III), approximately 50 times Sol luminosity -- known as The Solitary One because it is the only bright star in its constellation, a name the system has inherited and earned',
    population=4_000_000_000,
    distance_to_sol=177.0,
    stellar_objects=[
        StellarObject(
            name='Dalvaren',
            short_description='The most organic world in the Hyades -- two billion people who modify when the work requires it and stop when it doesn\'t, in a system where keeping your own body is not a competitive disadvantage.',
            long_description=(
                'Dalvaren is the system that the rest of the Hyades finds uncomfortable '
                'for reasons the residents of Dalvaren consider revealing. The planet is '
                'habitable, temperate, and pleasant in a modest way -- not spectacular, '
                'not wealthy, not strategically important. What Dalvaren is, is restrained. '
                'The population modifies when the work requires it and stops when it does '
                'not. A farmer on Dalvaren has the agricultural prosthetics that farming '
                'demands. The farmer does not have the additional modifications that a '
                'farmer on Morthane would carry -- the sensory upgrades, the interface '
                'ports, the progressive replacements that the guild system encourages as '
                'career advancement. The farmer on Dalvaren has mechanical hands and '
                'organic arms. The farmer considers this sufficient.\n\n'
                'The restraint is cultural rather than ideological. Dalvaren is not anti-'
                'prosthetic. The population does not protest modification or argue that '
                'the organic body is sacred. They simply do not see the need to replace '
                'what works. An organic knee that functions adequately is not replaced with '
                'a mechanical knee that functions better, because the improvement does not '
                'justify the cost and the discomfort and the dependency on maintenance that '
                'the mechanical knee introduces. The calculus is practical: modify what you '
                'must, keep what you can, and do not let the guild system convince you that '
                'adequate is not enough.\n\n'
                'The guild presence on Dalvaren is the weakest in the cluster. The guilds '
                'operate here -- the agricultural guild, the maintenance workers\' guild, '
                'the small manufacturing guilds that the local economy supports -- but '
                'their influence is diluted by a population that joins guilds for the work '
                'and ignores the cultural expectations. The guild recruiters who visit '
                'Dalvaren find a population that is politely uninterested in the '
                'aspirational messaging that works on every other world. The Exhibition on '
                'Prima Hyadum broadcasts to Dalvaren. The residents watch it with the '
                'detached interest of people evaluating a product they do not intend to '
                'buy.\n\n'
                'The rest of the cluster regards Dalvaren with a mixture of puzzlement and '
                'faint suspicion. A population that does not want more modification is a '
                'population that implicitly questions whether more modification is better, '
                'and the question makes the guild system uncomfortable. The guild council '
                'on Secunda Hyadum has discussed Dalvaren in sessions that the minutes '
                'describe as concerning economic underperformance and that the participants '
                'describe as concerning the precedent. If Dalvaren can function with '
                'minimal modification, the argument that the guild system is necessary '
                'rather than merely profitable becomes harder to make.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Wetherton',
            short_description='A second world with a mixed economy -- small-scale manufacturing and services, where the prosthetic level is functional rather than progressive and nobody talks about it.',
            long_description=(
                'Wetherton is the system\'s second inhabited world -- a cooler planet with a '
                'mixed economy of small-scale manufacturing, services, and the light '
                'industry that a modest population requires. The prosthetic level on Wetherton '
                'mirrors Dalvaren\'s: functional, restrained, calibrated to the work rather '
                'than the guild system\'s expectations. The factories produce goods for '
                'local consumption rather than export, and the workforce is modified to '
                'the minimum that the work demands.\n\n'
                'The distinctive feature of Wetherton is the population\'s relationship with '
                'visitors from the rest of the cluster. Hyadean citizens who visit from the '
                'more heavily modified systems find Wetherton disconcerting -- not because the '
                'population is hostile to prosthetics but because the organic bodies are '
                'visible. On most Hyadean worlds, an unmodified arm is unusual enough to '
                'draw a glance. On Wetherton, unmodified arms are common, and the visitors '
                'from other systems find themselves staring at organic hands the way '
                'inner-system visitors to the Hyades stare at mechanical ones. The '
                'disorientation works in both directions.\n\n'
                'MERIT\'s propaganda uses Alphard cautiously. The system is evidence that '
                'Hyadean citizens can live with minimal modification -- that the economic '
                'pressure to replace healthy limbs is a choice the cluster makes rather '
                'than a necessity it faces. The Hyadean response is that Alphard is a '
                'backwater whose economy underperforms precisely because the population '
                'does not modify adequately. Both arguments contain truth. Neither side '
                'finds the other\'s truth comfortable.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Solitary Station',
            short_description='The system\'s orbital port -- smaller and quieter than any other Hyadean orbital, reflecting a system that does not seek traffic and does not turn it away.',
            long_description=(
                'Solitary Station is Alphard\'s orbital port -- a modest facility that '
                'handles the system\'s limited traffic with the unhurried efficiency of a '
                'port that is never overwhelmed. The traffic is light: supply ships from '
                'Chamukuy carrying the goods that the local economy does not produce, the '
                'occasional guild delegation visiting to assess the system\'s economic '
                'output and departing with reports that recommend increased modification '
                'incentives, and the visitors who come to Alphard specifically because it '
                'is the system where the Hyades is least itself.\n\n'
                'The visitors are a small but steady stream. Some are Hyadean citizens who '
                'have decided they want to live in a system where the modification pressure '
                'is lower -- people who are tired of the guild expectations, the Exhibition '
                'messaging, the cultural assumption that more hardware is always better. '
                'Some are inner-system visitors who want to see the Hyades without the '
                'full intensity -- Alphard as an introduction rather than an immersion. '
                'The station processes them all with the same quiet competence and does '
                'not ask why they came.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Aldwick',
            short_description='An agricultural world that demonstrates the Alphard philosophy -- the farming works, the yields are adequate, the farmers are less modified, and the system feeds itself without imports.',
            long_description=(
                'Aldwick is the system\'s agricultural world -- warm, fertile, and farmed '
                'at a scale that feeds four billion people without the imports that most '
                'Hyadean systems require from Chamukuy. The self-sufficiency is deliberate '
                '-- the system\'s founding generation chose agricultural independence over '
                'the trade dependency that ties other systems to the cluster\'s supply '
                'chains, and the choice has been maintained for centuries.\n\n'
                'The farming on Aldwick demonstrates the Alphard approach. The farmers are '
                'modified -- mechanical hands, the basic sensory packages that agricultural '
                'work requires. They are not modified beyond the minimum. The yields are '
                'lower than Morthane\'s per-hectare output because the farmers lack the '
                'progressive enhancements that Morthane\'s workforce carries. The total '
                'output is sufficient because the system\'s population is smaller and the '
                'agricultural land is extensive. The guild council\'s economists point to '
                'the lower yields as evidence that minimal modification produces inferior '
                'results. Aldwick\'s farmers point to the full granaries and ask what '
                'problem, exactly, the economists are solving.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Ostmark',
            short_description='A gas giant with modest fuel processing -- sized for a system that does not generate heavy traffic and does not want to.',
            long_description=(
                'Ostmark is the system\'s gas giant -- fuel processing on its moons at a '
                'scale matched to the modest traffic that Alphard generates. The fuel '
                'operations are guild-operated but small -- the fuel processors\' guild '
                'maintains a minimal presence because the traffic does not justify more. '
                'The fuel workers are modified with the standard package and do not '
                'discuss modification beyond the requirements of the job, which is the '
                'Alphard approach to the subject applied to fuel processing.\n\n'
                'The system\'s isolation -- reflected in the star\'s ancient name, the '
                'Solitary One -- is physical as well as cultural. Alphard sits away from '
                'the main trade routes that connect the cluster\'s core systems, and the '
                'jump links that reach it are not the most direct. The isolation is not '
                'total -- the system is connected, supplied, and governed by the guild '
                'republic like every other Hyadean system. But the distance gives the '
                'population space that the core systems do not have: the space to be '
                'Hyadean on their own terms, which means being less Hyadean than the '
                'guild system would prefer.'
            ),
            population=20_000_000,
        ),
    ],
    short_description='The Solitary One -- four billion people in a system that modifies when it must and stops when it can, in a cluster that considers restraint a provocation.',
    long_description=(
        'Alphard inherits its star\'s ancient name -- the Solitary One, the only '
        'bright star in its constellation, isolated by nature. The system has earned '
        'the name. Four billion people live here with a relationship to prosthetic '
        'modification that the rest of the Hyades finds puzzling, faintly suspicious, '
        'and difficult to argue with: they modify when the work requires it and stop '
        'when it does not.\n\n'
        'The population is not anti-prosthetic. They do not protest or argue that the '
        'organic body is sacred. They simply do not replace what works. An organic '
        'knee that functions adequately stays organic, because the improvement a '
        'mechanical knee offers does not justify the cost, the discomfort, and the '
        'dependency on maintenance. The calculus is practical rather than ideological: '
        'modify what you must, keep what you can, and do not let the guild system '
        'convince you that adequate is not enough.\n\n'
        'The guild presence is the weakest in the cluster. The recruiters find a '
        'population politely uninterested in the aspirational messaging. The '
        'Exhibition broadcasts. The residents watch with the detached interest of '
        'people evaluating a product they do not intend to buy. The guild council '
        'discusses Alphard in sessions recorded as concerning economic '
        'underperformance and remembered as concerning the precedent: if Alphard can '
        'function with minimal modification, the argument that the guild system is '
        'necessary rather than merely profitable becomes harder to make.\n\n'
        'MERIT uses Alphard cautiously in its propaganda -- evidence that the '
        'economic pressure to modify is a choice the cluster makes rather than a '
        'necessity. The Hyadean response is that Alphard is a backwater that '
        'underperforms because it does not modify adequately. Both arguments contain '
        'truth. Neither side finds the other\'s truth comfortable. Alphard continues '
        'regardless, solitary and sufficient, feeding itself from its own fields and '
        'keeping its own knees, in a cluster that considers restraint a provocation.'
    ),
    cluster=StarClusters.HYADES,
)

GLENNAH = System(
    name='Glennah',
    star='Blue-white giant (B8IIIp), approximately 150 times Sol luminosity -- the p designation means peculiar: chemically anomalous, with unusual abundances of mercury and manganese that the researchers came for and the prosthetics industry stayed for',
    population=5_000_000_000,
    distance_to_sol=165.0,
    stellar_objects=[
        StellarObject(
            name='Mendara',
            short_description='The cluster\'s research capital -- three billion people designing the next generation of prosthetics in a system whose chemically peculiar star provides materials that cannot be sourced anywhere else.',
            long_description=(
                'Mendara is where the Hyades invents its future. The planet is the '
                'cluster\'s primary research and development centre -- the place where the '
                'next generation of prosthetic technology is designed, prototyped, and '
                'tested before being passed to the manufacturing systems for production. '
                'The research institutions on Mendara are the cluster\'s most prestigious '
                'and most competitive -- staffed by engineers and researchers whose '
                'cognitive prosthetics are the most advanced available, working on problems '
                'that the current generation of hardware cannot solve.\n\n'
                'The research agenda is driven by the star. Glennah\'s star is chemically '
                'peculiar -- a B8III giant with anomalous abundances of mercury, manganese, '
                'and a suite of heavier elements that are rare in normal stellar '
                'environments. The stellar wind deposits these elements throughout the '
                'system, and the planetary surfaces and orbital debris contain compounds '
                'that cannot be sourced in meaningful quantities anywhere else in the '
                'cluster. The compounds are the foundation of the next-generation '
                'prosthetic materials -- alloys with properties that conventional materials '
                'cannot match, interface substrates that conduct neural signals with less '
                'degradation, and the experimental composites that the researchers are '
                'still characterising.\n\n'
                'The research guilds on Mendara are among the cluster\'s smallest and '
                'wealthiest. The researchers\' guild and the materials scientists\' guild '
                'together represent a fraction of the cluster\'s population but control '
                'the intellectual property that the entire prosthetics industry depends on. '
                'Every significant advance in prosthetic technology in the last century '
                'has originated on Mendara, and the guilds that produced those advances '
                'hold the patents, the manufacturing secrets, and the quiet leverage that '
                'comes from being the people who decide what the next generation of '
                'hardware can do. The guild council on Secunda Hyadum treats the research '
                'guilds with a deference that the larger guilds resent and cannot avoid, '
                'because the larger guilds need what the research guilds produce.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Smelters',
            short_description='Orbital processing facilities that extract the rare compounds from the stellar debris -- the raw material pipeline that makes Glennah\'s research possible.',
            long_description=(
                'The Smelters are a network of orbital processing facilities that harvest '
                'and refine the rare compounds deposited by Glennah\'s chemically peculiar '
                'star. The stellar wind carries the anomalous elements outward through the '
                'system, and the Smelters collect the debris, separate the valuable '
                'compounds, and process them into the raw materials that the research '
                'institutions on Mendara require. The processing is delicate -- the '
                'compounds are valuable because of their unusual properties, and the '
                'extraction must preserve those properties rather than destroy them.\n\n'
                'The Smelters are operated by the materials scientists\' guild -- a '
                'specialised guild whose members are modified for the precision that the '
                'extraction work demands. The prosthetics are research-grade: sensory '
                'packages that can detect molecular composition by contact, manipulation '
                'systems precise enough to separate compounds at near-molecular scales, and '
                'the cognitive enhancements that let the operators process the analytical '
                'data in real time. The materials scientists are among the most precisely '
                'modified workers in the cluster -- not the heaviest, not the most '
                'extensive, but the most finely calibrated.\n\n'
                'The output of the Smelters is small in volume and enormous in value. The '
                'processed compounds that flow from the Smelters to Mendara\'s research '
                'institutions are the most expensive raw materials in the Hyades -- gram '
                'for gram, worth more than anything the mining systems produce. The '
                'materials scientists\' guild controls this pipeline and uses the control '
                'the way any guild uses a monopoly: carefully, profitably, and with the '
                'awareness that the monopoly is what makes the guild indispensable.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Kethbridge',
            short_description='The prototyping world -- where experimental prosthetics are built, tested on volunteers, and refined before the designs are released to manufacturing.',
            long_description=(
                'Kethbridge is the system\'s prototyping and testing world -- the stage '
                'between Mendara\'s research and the cluster\'s manufacturing systems. The '
                'experimental prosthetics designed on Mendara are built on Kethbridge in '
                'small batches, tested under controlled conditions, and refined through '
                'iterations that may take years before a design is certified for '
                'production.\n\n'
                'The testing involves volunteers. The research guilds maintain a programme '
                'of volunteer test subjects -- people who agree to have experimental '
                'prosthetics installed in exchange for compensation and the prestige of '
                'wearing hardware that nobody else in the cluster has. The volunteers are '
                'a self-selecting group: young, confident, and willing to accept the risk '
                'that an experimental prosthetic may not work as designed. Most prototypes '
                'function. Some function better than expected. A few fail in ways that the '
                'researchers study intensively and the volunteers experience personally. '
                'The failure rate is low but nonzero, and the volunteers who carry failed '
                'prototypes until the replacement arrives are the research programme\'s most '
                'visible cost.\n\n'
                'The population on Kethbridge walks around with hardware that visitors '
                'from other systems do not recognise. The experimental prosthetics are '
                'visually distinctive -- different materials, different engineering, '
                'different aesthetics from the production hardware. A Kethbridge resident '
                'with a next-generation arm is immediately identifiable as someone wearing '
                'technology that the rest of the cluster will not see for years. The '
                'residents consider this a badge of distinction. The researchers consider '
                'it a field test.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Patent Station',
            short_description='The system\'s orbital port -- where the intellectual property that drives the cluster\'s prosthetics industry is licensed, traded, and guarded with the intensity of a strategic asset.',
            long_description=(
                'Patent Station is Glennah\'s primary orbital facility -- a station that '
                'handles the system\'s traffic and, more importantly, the intellectual '
                'property transactions that are the system\'s most valuable export. The '
                'research guilds license their designs to the manufacturing guilds on other '
                'systems -- the terms negotiated on Patent Station, the contracts signed '
                'in the station\'s secure transaction rooms, and the technical specifications '
                'transmitted through encrypted channels that the research guilds consider '
                'more important to protect than any physical cargo.\n\n'
                'The security on Patent Station is the tightest in the cluster -- not '
                'military security, but intellectual property security. The research guilds '
                'invest more in protecting their designs than most systems invest in '
                'military defence. The station\'s data systems are hardened against '
                'intrusion. The transaction rooms are shielded. The staff who handle the '
                'technical specifications are bonded to the research guilds with contracts '
                'that make the consequences of disclosure more frightening than anything '
                'the military could threaten. In the Hyades, the patents are the weapons.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Vestren',
            short_description='A gas giant whose atmospheric composition reflects the star\'s chemical peculiarity -- the gases contain trace elements that the Smelters cannot extract from the stellar debris alone.',
            long_description=(
                'Vestren is the system\'s gas giant -- notable because the star\'s chemical '
                'peculiarity has influenced its atmospheric composition. The gases contain '
                'trace amounts of the anomalous elements that the stellar wind deposits '
                'throughout the system, and the fuel processing operations on Vestren\'s '
                'moons include a secondary extraction process that separates these trace '
                'elements from the fuel gases and channels them to the Smelters for '
                'processing.\n\n'
                'The secondary extraction is low-yield but valuable -- a supplementary '
                'source of the rare compounds that the research institutions require. The '
                'materials scientists\' guild operates the extraction alongside the fuel '
                'processors\' guild, and the relationship between the two guilds on '
                'Vestren\'s moons is one of the cluster\'s more functional inter-guild '
                'partnerships: the fuel processors extract the fuel, the materials '
                'scientists extract the trace elements, and neither interferes with the '
                'other\'s operations.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Standen',
            short_description='An agricultural world feeding the system -- standard Hyadean farming under the peculiar star\'s blue-white light.',
            long_description=(
                'Standen is the system\'s agricultural world -- farmed at a scale that '
                'feeds five billion people, under the blue-white light of a star whose '
                'chemical peculiarity does not significantly affect the growing conditions. '
                'The farming follows the standard Hyadean model: prosthetically modified '
                'workers with the agricultural package, managed by the agricultural guild. '
                'The output is sufficient for local consumption with a small surplus.\n\n'
                'The farmers on Standen are the system\'s most conventional population -- '
                'standard guild members with standard modifications, doing standard work '
                'in a system where everyone else is doing something experimental. The '
                'farmers find the contrast amusing. The researchers on Mendara are '
                'inventing the future of prosthetic technology. The farmers on Standen '
                'are growing the potatoes that the researchers eat. Both are necessary. '
                'The researchers occasionally remember this.'
            ),
            population=700_000_000,
        ),
    ],
    short_description='The cluster\'s laboratory -- five billion people designing the next generation of prosthetics under a chemically peculiar star that provides materials found nowhere else.',
    long_description=(
        'Glennah is where the Hyades invents its future. The system\'s star is '
        'chemically peculiar -- a B8III giant with anomalous abundances of mercury, '
        'manganese, and heavier elements that are rare in normal stellar environments. '
        'The stellar wind deposits these elements throughout the system, providing '
        'compounds that cannot be sourced elsewhere and that form the foundation of '
        'the next-generation prosthetic materials the cluster\'s researchers are '
        'developing.\n\n'
        'Mendara is the research capital -- the cluster\'s most prestigious '
        'institutions, staffed by researchers whose cognitive prosthetics are the most '
        'advanced available, working on problems the current hardware cannot solve. '
        'The research guilds are small and wealthy, controlling the intellectual '
        'property that the entire prosthetics industry depends on. Every significant '
        'advance in the last century originated on Mendara. The guild council treats '
        'the research guilds with a deference the larger guilds resent and cannot '
        'avoid.\n\n'
        'The Smelters process the rare compounds from the stellar debris -- orbital '
        'extraction facilities operated by materials scientists with the most finely '
        'calibrated prosthetics in the cluster. Kethbridge tests the prototypes on '
        'volunteers who carry experimental hardware that nobody else in the cluster '
        'has. Patent Station guards the intellectual property with security tighter '
        'than most military installations, because in the Hyades the patents are the '
        'weapons.\n\n'
        'The star\'s chemical peculiarity is the system\'s strategic asset and its '
        'constraint. The research depends on the rare compounds. The rare compounds '
        'come from this star and no other. Glennah cannot be replicated, relocated, '
        'or replaced. The system\'s value is geological and astrophysical -- a '
        'fortunate accident of stellar chemistry that has made five billion people '
        'the custodians of the cluster\'s technological future, under a star whose '
        'peculiarity is the most valuable property in the Hyades.'
    ),
    cluster=StarClusters.HYADES,
)

ALGIEBA = System(
    name='Algieba',
    star='Binary system: two orange giants (K0IIIb + G7IIIa), approximately 70 and 35 times Sol luminosity respectively -- a close pair casting double amber light that shifts in hue as the stars orbit each other',
    population=9_000_000_000,
    distance_to_sol=130.0,
    stellar_objects=[
        StellarObject(
            name='Kassimer',
            short_description='The cultural heart of the Hyades -- five billion people living in the system where guild identity is strongest, the traditions are deepest, and the first modification is a celebration.',
            long_description=(
                'Kassimer is where the Hyades feels most like itself. The planet is not '
                'the capital, not the richest, not the most industrially productive -- but '
                'it is the system where the culture of the guild republic is most deeply '
                'rooted and most visibly expressed. The guild identity on Kassimer is not '
                'the administrative affiliation it is on other worlds. It is who you are. '
                'It shapes the district you live in, the people you marry, the festivals '
                'you celebrate, and the way your body looks.\n\n'
                'The guilds on Kassimer maintain their oldest and most elaborate traditions. '
                'Each guild has its own calendar of observances -- the heavy-lifters\' '
                'Founding Day, the precision-workers\' Exhibition of Hands, the interface '
                'specialists\' Signal Festival, and dozens of smaller celebrations that mark '
                'the guild\'s history, its founders, and the achievements of its members. '
                'The festivals are public and spectacular -- parades of guild members in '
                'full modification displaying the capabilities of their hardware, '
                'competitions between guilds that are technically friendly and practically '
                'fierce, and the communal meals that bring the guild\'s membership together '
                'across the district lines.\n\n'
                'The first modification is the centrepiece. On Kassimer, the installation '
                'of a young person\'s first prosthetic is a community celebration -- the '
                'guild\'s coming-of-age ceremony, attended by family, guild elders, and '
                'the neighbourhood. The procedure is performed by a senior guild '
                'technician in a ceremonial setting rather than a clinic. The young person '
                'enters with an organic body and leaves with the guild\'s starter hardware '
                '-- typically the hands, the tool that defines what the guild member does. '
                'The ceremony is joyful. The family celebrates. The young person is now a '
                'guild member, marked in their flesh -- or rather, in the metal that '
                'replaced their flesh -- as belonging.\n\n'
                'The joy is genuine and the pressure is invisible. The ceremony is a '
                'celebration of identity and belonging. It is also the moment when a '
                'teenager\'s organic hands are removed and replaced with mechanical ones, '
                'and the teenager has been raised in a culture where refusing is '
                'unthinkable. Nobody is forced. Nobody needs to be. The culture does the '
                'work that force would do clumsily, and the young person walks out of the '
                'ceremony proud and modified and certain that they chose this, which they '
                'did, in the same way that anyone raised inside a set of assumptions '
                'chooses the thing the assumptions point toward.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Helvane',
            short_description='A second world where the inter-guild culture is strongest -- where the guilds compete, collaborate, and intermarry in the patterns that define Hyadean social life.',
            long_description=(
                'Helvane is the system\'s second inhabited world -- warmer, coastal, and '
                'the place where the inter-guild dynamics that define Hyadean social life '
                'are most visible. The guilds on Kassimer maintain their traditions in '
                'relative isolation -- each guild in its own district, its own festivals, '
                'its own identity. On Helvane, the guilds interact: the inter-guild '
                'markets where the heavy-lifters buy precision components and the '
                'precision-workers buy structural materials, the mixed districts where '
                'guild members live alongside members of other guilds, and the inter-guild '
                'marriages that the traditionalists on Kassimer consider controversial and '
                'that Helvane\'s population considers normal.\n\n'
                'The inter-guild marriages are the most interesting social dynamic. A '
                'heavy-lifter who marries a precision-worker produces children who must '
                'choose a guild -- the child cannot belong to both, and the choice is made '
                'in adolescence at the first modification ceremony. The choosing is '
                'Helvane\'s most emotionally charged tradition: the child selects the '
                'parent\'s guild that feels right, and the other parent accepts the choice '
                'with grace or with grief depending on how the family navigates the '
                'moment. The child\'s first prosthetic comes from the chosen guild\'s '
                'technician, and the other parent watches their child receive hardware '
                'from a different guild and becomes, in a small but real way, less the '
                'parent\'s child and more the guild\'s member.\n\n'
                'The binary star\'s double amber light gives Helvane a distinctive visual '
                'character -- the two orange giants casting overlapping shadows that shift '
                'as the stars orbit, producing a warm, complex illumination that the '
                'residents consider the most beautiful light in the cluster. The coastal '
                'cities under the double light host the inter-guild festivals that bring '
                'the cluster\'s guilds together -- not the competitive displays of '
                'Kassimer\'s guild-specific celebrations but the cooperative events where '
                'the guilds demonstrate what they can build together.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Anneal',
            short_description='An orbital complex dedicated to the cultural preservation of the guild traditions -- archives, training centres, and the ceremonial facilities where the guild technicians are taught.',
            long_description=(
                'The Anneal is an orbital complex above Kassimer that serves as the '
                'cultural preservation centre for the guild traditions. The complex houses '
                'the archives of guild history -- records of every guild\'s founding, the '
                'evolution of the modification practices, the ceremonial protocols that '
                'govern the first modification, and the accumulated cultural heritage of a '
                'civilisation that has been replacing its bodies for centuries.\n\n'
                'The Anneal is also where the guild ceremonial technicians are trained -- '
                'the senior guild members who perform the first modification ceremonies on '
                'Kassimer and across the cluster. The training is part technical, part '
                'cultural: the technician must be able to perform the installation with '
                'the precision the hardware requires and the ritual significance the '
                'ceremony demands. A first modification performed by an untrained '
                'technician is a medical procedure. A first modification performed by an '
                'Anneal-trained ceremonial technician is a rite of passage. The distinction '
                'matters to the guilds and to the families, and the Anneal exists to '
                'ensure the distinction is maintained.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Kindred Station',
            short_description='The system\'s orbital port -- the arrival point for the guild delegations, the cultural tourists, and the young people from other systems who come to Kassimer for a traditional first modification.',
            long_description=(
                'Kindred Station is Algieba\'s primary orbital facility -- a port that '
                'handles the system\'s traffic with an emphasis on the cultural function '
                'that makes Algieba distinctive. The traffic includes the standard '
                'commercial and supply ships, but the distinctive flow is the cultural '
                'traffic: guild delegations visiting for the festivals, families from other '
                'systems who bring their children to Kassimer for a traditional first '
                'modification ceremony, and the visitors from the inner systems who come '
                'to Algieba to understand what the Hyades is rather than what it makes.\n\n'
                'The station is built in the Hyadean industrial style but with decorative '
                'elements that the other orbital stations lack -- guild insignia on the '
                'docking bays, the traditional patterns of the major guilds worked into '
                'the station\'s architecture, and the ceremonial welcome that the station '
                'staff offer to arriving guild delegations. Kindred Station is the one '
                'orbital facility in the Hyades that tries to be beautiful as well as '
                'functional, and the effort is noticeable if not entirely successful.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Galvrek',
            short_description='A gas giant orbiting the binary pair -- fuel processing and the traditional guild training exercises where apprentices test their new hardware under operational conditions.',
            long_description=(
                'Galvrek is the system\'s gas giant -- a large body orbiting the binary '
                'pair at sufficient distance that both stars appear as distinct discs in '
                'the sky. The fuel processing on Galvrek\'s moons supports the system\'s '
                'traffic, and the outer moons host the traditional guild training exercises '
                'that Algieba is known for.\n\n'
                'The training exercises are a Kassimer tradition that has spread to the '
                'other systems -- apprentices who have received their first modification '
                'travel to Galvrek\'s moons for the guild trials, a series of practical '
                'tests that verify the young member\'s ability to use their new hardware '
                'under operational conditions. The heavy-lifters\' trial involves moving '
                'structural loads in low gravity. The precision-workers\' trial involves '
                'assembling components under pressure. The interface specialists\' trial '
                'involves connecting to unfamiliar systems and operating them cold. The '
                'trials are challenging, the failure rate is low because the guilds '
                'prepare their apprentices well, and the completion of the trials is the '
                'second celebration -- the young member has been modified and has proven '
                'that the modification works.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Dranneth',
            short_description='An agricultural world feeding the system -- where the agricultural guild\'s traditions are the oldest and the first modification ceremony uses a planting hand rather than a tool hand.',
            long_description=(
                'Dranneth is the system\'s agricultural world -- fertile under the double '
                'amber light, farmed by the agricultural guild\'s members with the '
                'traditional practices that Algieba preserves. The agricultural guild on '
                'Dranneth claims the oldest continuous first modification tradition in the '
                'cluster -- a ceremony that installs a planting hand rather than a '
                'standard agricultural prosthetic, a ceremonial modification that is '
                'replaced with functional hardware after the ceremony but that represents '
                'the guild\'s founding identity: people who grow things with hands built '
                'for growing.\n\n'
                'The planting hand is a symbolic prosthetic -- designed to plant a seed '
                'in the ceremony\'s final act, where the newly modified guild member '
                'plants a crop in the guild\'s ceremonial field using their first '
                'prosthetic hand. The crop is tended by the guild and harvested at the '
                'next season\'s ceremony. The tradition has been maintained for centuries, '
                'and the ceremonial field on Dranneth has been continuously cultivated by '
                'every generation of the agricultural guild\'s membership since the '
                'colony\'s founding. The field is the guild\'s most sacred space, which '
                'in the Hyades means it is a piece of ground where the work is done by '
                'hand, by the guild\'s newest members, with hardware that was designed '
                'for ceremony rather than efficiency.'
            ),
            population=700_000_000,
        ),
    ],
    short_description='The cultural heart -- nine billion people in a binary system where the guild traditions are deepest and the first modification is a celebration that nobody questions and everyone chooses.',
    long_description=(
        'Algieba is the cultural heart of the Hyades cluster -- the system where the '
        'guild identity is most deeply rooted and most visibly expressed. The binary '
        'star casts double amber light that shifts as the two orange giants orbit '
        'each other, and the system\'s character is as layered as its illumination. '
        'At 130 light-years from Sol, Algieba is the closest Hyadean system to the '
        'inner systems, and the proximity has not diluted the culture. If anything, '
        'the awareness that MERIT space is close has made the population hold its '
        'traditions tighter.\n\n'
        'The first modification is the centrepiece. On Kassimer, the installation of '
        'a young person\'s first prosthetic is a community celebration -- a coming-of-'
        'age ceremony performed by an Anneal-trained ceremonial technician, attended '
        'by family and guild elders, joyful and proud. The young person enters with '
        'an organic body and leaves with the guild\'s starter hardware. Nobody is '
        'forced. Nobody needs to be. The culture does the work that force would do '
        'clumsily, and the young person walks out certain they chose this, in the '
        'same way anyone raised inside a set of assumptions chooses the thing the '
        'assumptions point toward.\n\n'
        'Helvane is where the guilds interact -- inter-guild markets, mixed '
        'districts, the inter-guild marriages that produce children who must choose '
        'a parent\'s guild at adolescence and receive their first prosthetic from the '
        'chosen guild\'s technician. The choosing is Helvane\'s most emotionally '
        'charged tradition: one parent watches their child receive hardware from a '
        'different guild and becomes, in a small but real way, less the parent\'s '
        'child and more the guild\'s member.\n\n'
        'The Anneal preserves the traditions -- archives of guild history, training '
        'of the ceremonial technicians, the protocols that make a first modification '
        'a rite of passage rather than a medical procedure. Dranneth\'s agricultural '
        'guild maintains the oldest continuous ceremony in the cluster: the planting '
        'hand, a ceremonial prosthetic used to plant a seed in the guild\'s sacred '
        'field, continuously cultivated since the colony\'s founding. Nine billion '
        'people in a system that has made the replacement of the body a thing of '
        'beauty, community, and belonging -- and in doing so has made the question '
        'of whether anyone would choose differently almost impossible to ask.'
    ),
    cluster=StarClusters.HYADES,
)

MUSCIDA = System(
    name='Muscida',
    star='Yellow giant (G4II-III), approximately 40 times Sol luminosity -- an unremarkable star illuminating a system whose inhabitants have found the most brutal application of the cluster\'s defining technology',
    population=2_000_000_000,
    distance_to_sol=184.0,
    stellar_objects=[
        StellarObject(
            name='Krennal',
            short_description='The cluster\'s pirate capital -- a billion people in a system where the most valuable cargo is not in the hold but attached to the crew.',
            long_description=(
                'Krennal is a habitable world with no significant resources, no strategic '
                'position, and no industry that the guild council considers worth '
                'protecting. What Krennal has is raiders -- organised, professional, and '
                'specialised in a form of piracy that is unique to the Hyades: stripping '
                'prosthetics from captured crews.\n\n'
                'The raiders who operate from Krennal do not care about cargo. A captured '
                'freighter\'s hold might contain grain, fuel, manufactured goods -- all '
                'valuable, all worth taking. But the crew is worth more. A Hyadean crew '
                'member carries prosthetics that represent years of guild-certified '
                'installation -- hardware that cost thousands of credits to manufacture, '
                'install, and calibrate, and that can be stripped, reconditioned, and '
                'resold for a fraction of the original price to buyers who cannot afford '
                'new. The raiders board a ship, immobilise the crew, and strip the '
                'prosthetics with the practised efficiency of people who have done this '
                'hundreds of times. The crew is left alive -- organic, unmodified, and '
                'unable to do the work their guild trained them for because the hardware '
                'that made them guild members is gone.\n\n'
                'The stripping is the cruelty. In the Antares cluster, Lesath\'s pirates '
                'steal cargo. In the Canopus cluster, Suhail\'s pirates steal cargo and '
                'use shells as shock troops. In the Hyades, Muscida\'s pirates steal the '
                'crew\'s bodies. The victim is not robbed of property. The victim is robbed '
                'of capability -- the hands that performed their trade, the arms that '
                'lifted their loads, the interfaces that connected them to their ships and '
                'their work. A stripped crew member returns to their guild unable to work, '
                'unable to afford replacement hardware, and facing a guild system that '
                'treats them as a member who has lost their tools rather than a victim who '
                'has been violated.\n\n'
                'The raider gangs on Krennal are organised around the stripping crews -- '
                'technicians who specialise in fast removal of prosthetics under field '
                'conditions. A good stripping crew can process a ten-person freighter crew '
                'in under an hour: immobilise, disconnect, extract, package. The work is '
                'medical in its precision and industrial in its speed. The stripping crews '
                'are the most valued members of the raider gangs, and their skills are '
                'the inverse of the guild ceremonial technicians on Algieba -- where the '
                'Anneal trains people to install the first prosthetic with ritual '
                'significance, Krennal trains people to remove prosthetics with brutal '
                'efficiency.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='The Salvage',
            short_description='An orbital market for stripped prosthetics -- where the stolen hardware is reconditioned and sold to buyers who cannot afford guild-certified installations.',
            long_description=(
                'The Salvage is Muscida\'s orbital market -- a station where the stripped '
                'prosthetics are brought, reconditioned, and sold. The market operates '
                'openly because the guild council\'s enforcement does not extend to Muscida '
                'in practice, and the buyers who come to the Salvage need the hardware too '
                'badly to care about its provenance.\n\n'
                'The buyers are the cluster\'s poor -- workers who cannot afford guild-'
                'certified prosthetics at full price and who find in the Salvage the '
                'hardware they need at a cost they can bear. A reconditioned arm from the '
                'Salvage costs a quarter of what a new installation from Brannick\'s '
                'factories would cost, and the quality is often better because the '
                'stripped hardware was guild-certified when it was originally installed. '
                'The reconditioning process cleans the hardware, replaces the worn '
                'components, and recalibrates the interfaces for the new owner. The process '
                'is competent. The origin is not discussed.\n\n'
                'The Salvage also sells to the chop shops across the cluster -- the back-'
                'street operators who install hardware without guild certification and who '
                'need a supply of affordable components. The supply chain from Muscida\'s '
                'raiders to the cluster\'s chop shops is the prosthetic economy\'s black '
                'market, and the volume is large enough that the guild council has '
                'estimated the percentage of installed prosthetics across the cluster that '
                'originated as stripped hardware. The estimate is higher than the council '
                'publishes.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Droskane',
            short_description='A rocky world used as a staging area for raiding operations -- where the ships are maintained and the stripping crews practise on decommissioned hardware.',
            long_description=(
                'Droskane is a cold, rocky world in the outer habitable zone that the '
                'raider gangs use as a staging area. The surface installations are '
                'functional and crude -- landing pads, maintenance bays for the raiding '
                'ships, and the training facilities where new stripping crews are taught '
                'the techniques that the work requires.\n\n'
                'The training uses decommissioned prosthetics installed on practice rigs '
                'that simulate a restrained crew member. The trainees learn the disconnect '
                'sequences, the extraction techniques, and the speed that separates a '
                'professional stripping crew from an amateur who damages the hardware '
                'during removal and reduces its resale value. Damaged hardware is worth '
                'less. Clean extraction is worth more. The economics drive the training, '
                'and the training produces technicians whose skills would be valued in any '
                'guild\'s medical facility if the application were not the violent removal '
                'of hardware from unwilling subjects.\n\n'
                'The raiding ships maintained on Droskane are fast and lightly armed -- '
                'built for interception rather than combat. The raiders do not want to '
                'fight. They want to catch, board, strip, and leave. The ships are '
                'designed for the approach and the getaway, with boarding equipment and '
                'the restraint systems that the stripping crews need to immobilise a crew '
                'quickly. A raider ship from Muscida registers on sensors as a fast '
                'contact with a distinctive profile that the merchant captains in the '
                'cluster have learned to recognise and to dread.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Remnick',
            short_description='A world where stripped crew members are dumped -- left organic, unmodified, and unable to work, in communities of victims who cannot afford to rejoin the guild system.',
            long_description=(
                'Remnick is the system\'s quiet horror. The planet is where the stripped '
                'crew members end up -- the people who were caught by Muscida\'s raiders, '
                'had their prosthetics removed, and were left organic and unable to work. '
                'The guild system does not have a category for a member who has been '
                'stripped. The stripped person is technically still a guild member but '
                'cannot perform their trade without the hardware that defined their '
                'membership. The guild offers replacement at standard rates. The stripped '
                'person cannot afford standard rates, because the stripped person cannot '
                'work, because the stripped person does not have the hardware to work with.\n\n'
                'The communities on Remnick are populated by people caught in this loop. '
                'Former heavy-lifters with organic arms that cannot lift what the job '
                'requires. Former precision-workers with organic hands that lack the '
                'calibration the work demands. Former interface specialists with organic '
                'brains that process data at biological speed. They are whole. They are '
                'organic. They are, by MERIT\'s standards, unmodified and healthy. They '
                'are, by the Hyades\' standards, broken -- people without the hardware that '
                'their civilisation requires for participation, living in communities of '
                'the similarly dispossessed, doing what unskilled organic labour the '
                'local economy can provide.\n\n'
                'MERIT\'s propagandists have documented Remnick extensively. The images -- '
                'organic, healthy people who are functionally disabled by the standards '
                'of their own civilisation -- are among the most effective anti-Hyadean '
                'material MERIT produces. The Hyadean response is that Remnick is a '
                'criminal problem, not a systemic one. The stripped people on Remnick '
                'do not find the distinction meaningful.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Grevnik',
            short_description='A gas giant with fuel processing controlled by the raider gangs -- the fuel is priced for the raiders\' convenience and everyone else pays the premium.',
            long_description=(
                'Grevnik is the system\'s gas giant -- fuel processing on its moons '
                'controlled by the raider gangs rather than the fuel processors\' guild. '
                'The guild\'s authority does not extend to Muscida in practice, and the '
                'fuel operations are run by the gangs with the efficiency that criminal '
                'enterprise applies when the product is essential. The fuel is processed '
                'competently. The pricing favours the raider ships. Everyone else pays '
                'what the gangs charge, and the gangs charge what the traffic will bear.\n\n'
                'Ships that enter Muscida for fuel -- the occasional merchant captain who '
                'miscalculated their reserves, the independent traders who operate on the '
                'margins -- pay the inflated rates and leave quickly. The raider gangs do '
                'not strip ships that come to Muscida voluntarily for fuel, because '
                'stripping your customers eliminates the customer base. The rule is '
                'pragmatic rather than ethical, and it is enforced by the gangs with the '
                'understanding that the fuel business is the system\'s only legitimate '
                'revenue and the raiders need it to continue.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Striven',
            short_description='An agricultural world that barely functions -- farmed by the stripped population on Remnick who cannot do their original work but can do the organic labour that feeding a system requires.',
            long_description=(
                'Striven is the system\'s agricultural world -- and the darkest irony in a '
                'system full of them. The farming is done by the stripped population from '
                'Remnick -- people who lost their prosthetics to the raiders and who have '
                'found in organic agriculture the only work available to organic hands. '
                'The farming is pre-prosthetic in its methods: manual labour, hand tools, '
                'the techniques that the rest of the cluster abandoned generations ago '
                'when the agricultural prosthetics made them obsolete.\n\n'
                'The yields are low. The work is hard. The stripped farmers do it because '
                'the alternative is starvation, and because the work has a quality the '
                'stripped population does not discuss openly but that the observers from '
                'MERIT\'s propaganda division have noted: the farmers on Striven are using '
                'their organic bodies to do real work, and the work gives them a function '
                'that the guild system has denied them. A former precision-worker who '
                'cannot calibrate components with organic hands can plant a field with '
                'organic hands. The hands are the same. The work is different. The dignity '
                'is complicated.'
            ),
            population=150_000_000,
        ),
    ],
    short_description='The cluster\'s predator -- two billion people in a system where the pirates strip prosthetics from living crews and sell the stolen hardware to the poor who cannot afford new.',
    long_description=(
        'Muscida is the Hyades cluster\'s pirate system -- a world of raiders who have '
        'found the most brutal application of the cluster\'s defining technology. The '
        'pirates of Muscida do not steal cargo. They steal bodies. A captured '
        'freighter\'s crew is worth more than its hold, because the prosthetics '
        'attached to the crew represent years of guild-certified installation that '
        'can be stripped, reconditioned, and resold at the Salvage -- the orbital '
        'market where stolen hardware finds buyers who cannot afford new.\n\n'
        'The stripping is the cruelty. In Lesath, pirates steal cargo. In Suhail, '
        'pirates steal cargo and use shells as shock troops. In Muscida, pirates '
        'steal the crew\'s capability -- the hands that performed their trade, the '
        'arms that lifted their loads, the interfaces that connected them to their '
        'work. The stripping crews are trained to the standard of guild medical '
        'technicians, their skills the inverse of the Anneal\'s ceremonial '
        'technicians: where Algieba trains people to install the first prosthetic '
        'with ritual significance, Muscida trains people to remove prosthetics with '
        'brutal efficiency.\n\n'
        'Remnick is the aftermath. The stripped crew members -- organic, healthy by '
        'MERIT\'s standards, broken by the Hyades\' -- live in communities of the '
        'dispossessed, unable to work because the guild system requires hardware '
        'they cannot afford to replace. They farm Striven with organic hands and '
        'manual tools, doing pre-prosthetic agriculture that the rest of the cluster '
        'abandoned generations ago. MERIT\'s propagandists document Remnick '
        'extensively. The images of healthy organic people who are functionally '
        'disabled by their own civilisation\'s standards are among the most effective '
        'anti-Hyadean material MERIT produces.\n\n'
        'The guild council treats Muscida as a criminal problem. The raiders '
        'continue. The Salvage continues. The stripped continue to arrive on '
        'Remnick, whole and organic and unable to participate in a civilisation that '
        'has decided wholeness is not enough. Two billion people in a system that '
        'reveals the Hyadean economy\'s deepest assumption: that an unmodified body '
        'is a body without value.'
    ),
    cluster=StarClusters.HYADES,
)

HYD_4478 = System(
    name='HYD-4478',
    star='Orange dwarf (K3V), approximately 0.3 times Sol luminosity -- a dim, stable star that did nothing wrong, orbited by worlds that the Hyades broke trying to improve',
    population=0,
    distance_to_sol=200.0,
    stellar_objects=[
        StellarObject(
            name='HYD-4478-a',
            short_description='A world the Hyades tried to terraform without MERIT protocols -- the atmosphere is now toxic, the soil is contaminated, and the processors that caused the damage are still running.',
            long_description=(
                'HYD-4478-a was supposed to be a colony. The world sat in the habitable '
                'zone of a stable orange dwarf -- cold, thin-atmosphered, but within the '
                'parameters that terraforming could address. The Hyades assessed the planet, '
                'approved a terraforming programme, and began the work. The programme was '
                'designed to be fast. MERIT\'s terraforming protocols -- the procedures '
                'developed over centuries of planetary engineering in the inner systems -- '
                'were available. The guild council rejected them. The protocols were slow, '
                'cautious, and designed by a faction the Hyades had declared independence '
                'from. The council authorised a faster approach, developed by Hyadean '
                'engineers, using Hyadean methods, on a Hyadean timeline.\n\n'
                'The approach failed. The atmospheric processors introduced chemical '
                'imbalances that the MERIT protocols were designed to prevent -- cascading '
                'reactions in the upper atmosphere that converted the thin but harmless '
                'original atmosphere into something actively toxic. The soil engineering '
                'programme introduced compounds intended to accelerate biological '
                'colonisation of the surface, and the compounds interacted with the '
                'planet\'s native chemistry in ways the engineers had not modelled. The '
                'soil is now contaminated with persistent toxins that the original planet '
                'did not have. The water cycle, which was supposed to be enhanced by the '
                'atmospheric thickening, instead distributes the atmospheric contaminants '
                'across the surface in acid rainfall that etches the abandoned equipment '
                'and makes the contamination worse with every storm.\n\n'
                'The planet is worse than it was before the Hyades touched it. The '
                'original world was cold and thin-aired but chemically inert -- a blank '
                'slate that patient, careful terraforming could have made habitable over '
                'decades. The current world is actively hostile: toxic atmosphere, '
                'contaminated soil, acid rain, and the biological compounds in the soil '
                'that have begun producing their own secondary reactions, generating new '
                'toxins that the engineers did not introduce and cannot predict.\n\n'
                'The atmospheric processors are still running. The programme was suspended '
                'rather than terminated -- the guild council could not agree on whether to '
                'shut down the processors or attempt to correct the atmospheric chemistry '
                'by modifying the processor output. While the council deliberated, the '
                'processors continued on their original settings, pumping the same '
                'compounds into the atmosphere that caused the problem. The deliberation '
                'has lasted years. The processors are still running. The atmosphere is '
                'still getting worse.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-4478-b',
            short_description='A second world that was scheduled for terraforming and never started -- the programme was suspended after the first world\'s failure, leaving the equipment staged but unused.',
            long_description=(
                'HYD-4478-b was the programme\'s second phase -- a smaller, colder world '
                'further from the star that the terraforming plan scheduled for engineering '
                'after the primary world was established. The failure on HYD-4478-a halted '
                'the second phase before it began. The equipment staged for the operation '
                '-- atmospheric processors, soil engineering systems, the infrastructure '
                'for a programme that was never initiated -- sits on the surface where it '
                'was placed, untouched, slowly degrading in the cold.\n\n'
                'The equipment is valuable. The guild council has discussed recovering it '
                'multiple times, and the discussions have stalled on the same question '
                'that stalls everything about HYD-4478: the system is an embarrassment. '
                'Sending recovery teams means acknowledging the failure publicly, '
                'documenting the loss, and facing the questions about why the MERIT '
                'protocols were rejected. The equipment continues to degrade. The council '
                'continues to defer. The cost of the unused equipment grows with each '
                'year it sits in the cold, and the cost of recovering it grows with the '
                'political price of admitting what happened.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-4478-c',
            short_description='A small gas giant -- unprocessed, the fuel source for a colony that will never exist.',
            long_description=(
                'HYD-4478-c is a small gas giant in the outer system -- designated in the '
                'original terraforming plan as the future colony\'s fuel source. No '
                'processing facilities were built. The plan assumed that fuel processing '
                'would be constructed during the later phases of colonisation, after the '
                'primary world was habitable. The primary world is not habitable. The '
                'primary world is less habitable than it was before the Hyades intervened. '
                'The gas giant waits in a plan that failed, alongside the atmospheric '
                'targets and the population projections and the agricultural schedules '
                'that assumed the terraforming would work.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-4478-d',
            short_description='A frozen outer body -- the only object in the system that the Hyades did not attempt to improve, and therefore the only one in its original condition.',
            long_description=(
                'HYD-4478-d is a frozen body in the outer system -- ice and rock, too '
                'distant and too small for the terraforming programme to have included. '
                'The body is in its original condition, which makes it unique in HYD-4478: '
                'the only object the Hyades did not attempt to change, and therefore the '
                'only one that is not worse than it was. The irony is noted in the survey '
                'records and not discussed in the guild council\'s reports, because the '
                'guild council\'s reports do not include irony.'
            ),
            population=0,
        ),
    ],
    short_description='The failure -- a system the Hyades tried to terraform without MERIT protocols, turning habitable worlds into toxic ones, with the processors still running and making it worse.',
    long_description=(
        'HYD-4478 is the system the guild council does not discuss. The Hyades '
        'assessed the system, found a habitable-zone world suitable for '
        'terraforming, and launched a programme designed to be fast. MERIT\'s '
        'terraforming protocols -- slow, cautious, developed over centuries -- were '
        'available and were rejected. The council authorised a Hyadean approach on a '
        'Hyadean timeline, developed by Hyadean engineers who were certain they could '
        'improve on the inner systems\' methods.\n\n'
        'The approach failed. The atmospheric processors introduced cascading '
        'chemical imbalances. The soil engineering produced persistent toxins. The '
        'water cycle distributes the contamination as acid rain. The planet that was '
        'cold but chemically inert -- a blank slate that patient work could have made '
        'habitable -- is now actively hostile. The original atmosphere was harmless. '
        'The current atmosphere is toxic. The original soil was barren. The current '
        'soil is poisoned. The Hyades took a world that could have been a colony and '
        'made it worse than useless.\n\n'
        'The processors are still running. The programme was suspended rather than '
        'terminated -- the council could not agree on whether to shut down or '
        'attempt correction, and while they deliberated the processors continued on '
        'their original settings, pumping the same compounds that caused the problem. '
        'The deliberation has lasted years. The atmosphere is still getting worse. '
        'The second world\'s equipment sits unused, degrading in the cold, too '
        'politically expensive to recover because recovery means acknowledging the '
        'failure.\n\n'
        'MERIT cites HYD-4478 as evidence that the outer factions lack the '
        'institutional knowledge for planetary engineering. The Hyades does not '
        'respond because there is no response that makes the toxic atmosphere '
        'breathable or the poisoned soil fertile. The processors are still running. '
        'The council is still deliberating. The planet is still getting worse. The '
        'frozen outer body -- the one thing the Hyades did not try to improve -- is '
        'the only object in the system in its original condition.'
    ),
    cluster=StarClusters.HYADES,
)

HYD_1192 = System(
    name='HYD-1192',
    star='Blue supergiant (B1Ia), approximately 250,000 times Sol luminosity -- a massive, luminous star in the final stages of its life, nominally stable but on a timescale that means nothing to astrophysicists and everything to colonists',
    population=0,
    distance_to_sol=220.0,
    stellar_objects=[
        StellarObject(
            name='HYD-1192-a',
            short_description='An idyllic world that cannot be settled -- temperate, fertile, beautiful, orbiting a star that will destroy it at some point between tomorrow and ten thousand years from now.',
            long_description=(
                'HYD-1192-a is the best world the Hyades has ever found and the cruelest '
                'joke the galaxy has played on the cluster. The planet orbits at a distance '
                'from the blue supergiant that, despite the star\'s enormous luminosity, '
                'places it in a habitable zone -- the mathematics of orbital distance '
                'compensating for the output. The survey team that arrived five years ago '
                'found a world with a thick, breathable atmosphere, liquid surface water '
                'covering forty percent of the surface, temperate climate bands, and soil '
                'chemistry that the agricultural specialists described as exceptional. The '
                'planet could support a colony without terraforming. The planet could '
                'support a large colony. The planet is, by every metric the survey team '
                'measured, ideal.\n\n'
                'The star will go supernova. The astrophysicists who assessed the system '
                'confirmed what the spectral classification implied: HYD-1192\'s star is '
                'a blue supergiant in the late stages of its evolution, burning through '
                'its remaining fuel at a rate that places the expected supernova within a '
                'window that the astrophysicists describe as geologically imminent. In '
                'human terms, the window is enormous -- the star could collapse tomorrow, '
                'or it could burn for another thousand years. The astrophysicists '
                'cannot narrow the window further. The physics does not permit it. The '
                'star will die. The timing is unknowable.\n\n'
                'The guild council received the survey report and the astrophysical '
                'assessment together. The report described a world that could support '
                'twenty billion people. The assessment described a star that would destroy '
                'everything in the system when it collapsed. The council\'s response was '
                'silence, followed by a request for a second astrophysical opinion, '
                'followed by a third, each confirming the first: the star is dying, the '
                'world is perfect, and the two facts cannot be reconciled.\n\n'
                'The survey team remains on station. The data continues to accumulate. '
                'The world continues to orbit a star that will kill it, and the world '
                'does not know or care, and the sunsets over HYD-1192-a\'s oceans are, '
                'according to the survey team\'s geologist, the most beautiful she has '
                'ever seen.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-1192-b',
            short_description='A second habitable-zone world -- smaller, drier, but viable, doubling the tragedy by providing a second world that the dying star forbids.',
            long_description=(
                'HYD-1192-b is the system\'s second habitable-zone world -- a smaller, '
                'drier planet with a thinner atmosphere and less surface water than '
                'HYD-1192-a, but well within the parameters that colonisation could '
                'address. The world would need modest terraforming -- atmospheric '
                'thickening, water cycle enhancement -- but the work would be '
                'straightforward by the standards of the discipline. The agricultural '
                'potential is lower than HYD-1192-a\'s but still substantial.\n\n'
                'The existence of a second viable world makes the system\'s tragedy '
                'proportionally worse. A single condemned world is a loss. A twin-world '
                'system with a dying star is a loss that the colonial planners quantify '
                'in terms of the population that could have been supported, the industrial '
                'capacity that could have been built, and the strategic position that a '
                'twin-world colony would have occupied in the cluster\'s development. The '
                'numbers are large. The numbers are theoretical. The star does not care '
                'about the numbers.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-1192-c',
            short_description='A gas giant whose atmospheric bands glow in the blue supergiant\'s intense light -- beautiful and doomed like everything else in the system.',
            long_description=(
                'HYD-1192-c is a large gas giant in the outer system -- its atmospheric '
                'bands illuminated by the blue supergiant\'s intense light in colours that '
                'the survey team\'s astronomer described as unlike anything in the cluster. '
                'The light from a B1 supergiant is blue-white and extraordinarily bright, '
                'and the gas giant\'s atmosphere scatters it into patterns that are vivid, '
                'complex, and transient -- the bands shift and reform on timescales of '
                'hours, driven by the intense radiation pressure.\n\n'
                'The gas giant has fuel processing potential that the survey team noted '
                'in their report with the same dutiful completeness with which they noted '
                'every other asset in a system that cannot be used. The fuel is there. '
                'The infrastructure to process it could be built. The colony that would '
                'need the fuel will never exist. The gas giant orbits a dying star and '
                'glows in colours that nobody will see after the survey team departs.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-1192-d',
            short_description='A hot inner world -- mineral-rich, close to the star, and the first thing the supernova will consume.',
            long_description=(
                'HYD-1192-d is a dense, hot inner world with mineral deposits that the '
                'survey team catalogued as significant -- heavy metals and structural '
                'alloys in concentrations that would support a mining operation if the '
                'system were safe. The world orbits close to the blue supergiant, bathed '
                'in radiation that makes surface operations difficult even now, and that '
                'will become irrelevant when the star collapses because HYD-1192-d will '
                'be the first object consumed by the supernova\'s expanding shockwave.\n\n'
                'The survey team\'s mineralogist spent a week cataloguing the deposits '
                'with the thoroughness of a professional who understood that the data '
                'would never be acted on. The report is complete, detailed, and filed '
                'in the survey archives alongside the astrophysical assessment that '
                'renders it academic.'
            ),
            population=0,
        ),
    ],
    short_description='The tragedy -- a dying star orbited by perfect worlds that the Hyades found, measured, documented, and cannot touch.',
    long_description=(
        'HYD-1192 is the system the Hyades cannot use. The star is a blue supergiant '
        'in the late stages of its evolution -- 250,000 times Sol\'s luminosity, '
        'burning through its remaining fuel at a rate that places the expected '
        'supernova within a window of tomorrow to a thousand years. The '
        'astrophysicists cannot narrow the window. The physics does not permit it.\n\n'
        'The worlds are perfect. HYD-1192-a is the best colonisation candidate the '
        'cluster has found -- breathable atmosphere, liquid water, exceptional soil, '
        'capable of supporting twenty billion people without terraforming. HYD-1192-b '
        'is a second viable world that modest engineering could make habitable. The '
        'gas giant glows in colours unlike anything in the cluster. The inner world '
        'holds mineral deposits that would support a generation of industry. '
        'Everything the Hyades needs is here, orbiting a star that will destroy it '
        'all.\n\n'
        'The guild council requested three separate astrophysical opinions. Each '
        'confirmed the first: the star is dying, the world is perfect, and the two '
        'facts cannot be reconciled. A colony planted on HYD-1192-a might thrive for '
        'centuries before the star collapses. It might thrive for a decade. It might '
        'be destroyed before the colonists finish unpacking. The risk is not that the '
        'supernova will happen but that nobody knows when, and colonising a world '
        'under a death sentence of unknowable timing is a gamble the guild council '
        'has decided it cannot take.\n\n'
        'The survey team remains on station, collecting data on worlds that will '
        'never be settled, under a star that will not last. The geologist\'s report '
        'notes that the sunsets over HYD-1192-a\'s oceans are the most beautiful she '
        'has ever seen. The note is unprofessional. Nobody has asked her to remove it.'
    ),
    cluster=StarClusters.HYADES,
)

HYD_7703 = System(
    name='HYD-7703',
    star='Yellow-orange main sequence (G8V), approximately 0.7 times Sol luminosity -- a stable, unremarkable star orbited by perfectly usable worlds that nobody is allowed to use',
    population=0,
    distance_to_sol=210.0,
    stellar_objects=[
        StellarObject(
            name='HYD-7703-a',
            short_description='A habitable world claimed by three guilds and settled by none -- the most valuable piece of real estate in the cluster that nobody can touch because nobody can agree who gets it.',
            long_description=(
                'HYD-7703-a is a temperate, habitable world in the habitable zone of a '
                'stable yellow-orange star. The planet has a breathable atmosphere, liquid '
                'water, and conditions that would require minimal terraforming to support '
                'a colony. The survey was completed eight years ago. The survey data is '
                'excellent. The world is available. Nobody lives here.\n\n'
                'The problem is political. Three guilds have filed territorial claims on '
                'HYD-7703-a: the mining guild, which has identified significant mineral '
                'deposits in the northern hemisphere and wants the world designated as a '
                'mining operation; the agricultural guild, which has assessed the soil and '
                'growing conditions and wants the world designated as farmland; and the '
                'heavy-lifters\' guild, which wants to establish an industrial base to '
                'supplement Alpha Pegasi\'s shipyard output. Each claim is legitimate. Each '
                'guild has the resources to develop the world. Each guild refuses to '
                'concede to the others.\n\n'
                'The guild council has been adjudicating the dispute for eight years. The '
                'arbitration process on Kelrath has generated thousands of pages of '
                'submissions, counter-submissions, expert assessments, and procedural '
                'challenges. The mining guild argues that the mineral deposits make the '
                'world\'s highest-value use obvious. The agricultural guild argues that '
                'the cluster needs food more than ore. The heavy-lifters argue that '
                'industrial capacity is the strategic priority. Each argument is sound. '
                'Each guild has council votes to block the others\' claims. The result is '
                'stalemate.\n\n'
                'The world sits empty while the guilds argue about it. The survey team '
                'departed years ago. The automated monitoring station they left behind '
                'continues to transmit weather data, soil readings, and atmospheric '
                'measurements to the arbitration archive on Kelrath, where the data is '
                'filed and cited in submissions that generate counter-submissions that '
                'generate procedural challenges that generate more data requests. The '
                'world is perfect. The process is endless. The planet orbits its star '
                'and does not care which guild thinks it belongs to them.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-7703-b',
            short_description='A second habitable world that has made the gridlock worse -- two more guilds have filed claims on this one, expanding the dispute to five claimants across two worlds.',
            long_description=(
                'HYD-7703-b is a cooler, drier world further from the star -- habitable '
                'with terraforming, less immediately attractive than HYD-7703-a but still '
                'viable. The world\'s existence has made the political problem worse rather '
                'than better. Two additional guilds have filed claims on HYD-7703-b: the '
                'precision-workers\' guild, which wants a manufacturing facility for '
                'specialised components, and the fuel processors\' guild, which wants to '
                'develop the system\'s gas giant and considers a presence on HYD-7703-b '
                'a prerequisite for the fuel operations.\n\n'
                'The five-guild dispute has expanded the arbitration into the most complex '
                'territorial case in the guild republic\'s history. The original three-way '
                'claim on HYD-7703-a was difficult. The five-way claim across two worlds '
                'is a procedural labyrinth that the arbitrators on Kelrath describe in '
                'terms that suggest professional despair. Each guild\'s claim interacts '
                'with every other guild\'s claim. The mining guild\'s proposal for '
                'HYD-7703-a affects the agricultural guild\'s projections for food '
                'production, which affects the heavy-lifters\' workforce estimates, which '
                'affects the precision-workers\' component demand calculations, which '
                'affects the fuel processors\' traffic projections. The claims are '
                'interdependent. The guilds are not cooperating.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-7703-c',
            short_description='A gas giant that the fuel processors\' guild has claimed -- the claim is contingent on the resolution of the planetary dispute, adding another layer to the gridlock.',
            long_description=(
                'HYD-7703-c is a mid-sized gas giant in the outer system -- standard '
                'hydrogen-helium composition, suitable for fuel processing. The fuel '
                'processors\' guild has filed a claim that links the gas giant to their '
                'claim on HYD-7703-b: they argue that the fuel operations and the surface '
                'presence are a package, and that the council cannot approve one without '
                'the other. The other guilds consider this tactic a transparent attempt to '
                'leverage a secondary claim into priority on the primary dispute, which it '
                'is, and which the fuel processors\' guild does not deny.\n\n'
                'The gas giant waits alongside everything else in the system -- usable, '
                'unclaimed in practice, and held hostage by a political process that the '
                'guilds have allowed to become more important than the outcome. The '
                'arbitrators on Kelrath have noted privately that the guilds involved have '
                'begun using the HYD-7703 dispute as a bargaining chip in unrelated '
                'negotiations on the council -- trading concessions on HYD-7703 for '
                'advantages in other disputes, which means that resolving HYD-7703 would '
                'collapse a web of inter-guild agreements that now depend on the dispute '
                'remaining unresolved. The gridlock has become structurally necessary. '
                'The system remains empty because the emptiness is more politically '
                'useful than the settlement would be.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-7703-d',
            short_description='A frozen outer body -- unclaimed, because no guild has found a use for it, making it the only object in the system that is not the subject of a territorial dispute.',
            long_description=(
                'HYD-7703-d is a frozen body in the outer system -- ice and rock, too '
                'small and too distant for any guild to consider worth claiming. The body '
                'is the only object in HYD-7703 that is not part of the territorial '
                'dispute, which makes it the only object in the system whose status is '
                'clear. Nobody wants it. Nobody is arguing about it. In a system defined '
                'by the inability to agree, the frozen outer body has achieved the only '
                'consensus available: it is not worth fighting over.'
            ),
            population=0,
        ),
    ],
    short_description='The gridlock -- a system of perfectly usable worlds that five guilds have claimed and none can settle because the dispute has become more politically useful than the resolution.',
    long_description=(
        'HYD-7703 is the guild republic\'s most expensive argument. The system '
        'contains two habitable worlds, a gas giant suitable for fuel processing, '
        'and the resources to support a substantial colony. The survey was completed '
        'eight years ago. The worlds are available. Nobody lives here, because five '
        'guilds have filed territorial claims and none will concede.\n\n'
        'The mining guild wants HYD-7703-a for its mineral deposits. The '
        'agricultural guild wants it for farming. The heavy-lifters want it for '
        'industrial expansion. The precision-workers want HYD-7703-b for '
        'manufacturing. The fuel processors want the gas giant and the surface '
        'presence they argue is prerequisite for operations. Each claim is '
        'legitimate. Each guild has the votes to block the others. The arbitration '
        'on Kelrath has generated thousands of pages and consumed eight years.\n\n'
        'The gridlock has evolved beyond the original dispute. The guilds have '
        'begun using HYD-7703 as a bargaining chip in unrelated council '
        'negotiations -- trading concessions on the system for advantages in other '
        'disputes. Resolving HYD-7703 would collapse a web of inter-guild '
        'agreements that now depend on the dispute remaining unresolved. The '
        'gridlock has become structurally necessary. The emptiness is more '
        'politically useful than the settlement would be.\n\n'
        'The guild republic\'s greatest strength is the pragmatic negotiation that '
        'keeps competing guilds cooperating. HYD-7703 is the system where that '
        'strength becomes a weakness -- where the negotiation itself has become the '
        'product, and the worlds that the negotiation is nominally about sit empty '
        'under a stable star, habitable and unused, while the guilds argue about '
        'them on Kelrath and trade them on the council floor and forget, sometimes, '
        'that the argument is about real worlds with real soil and real potential '
        'that nobody is using because nobody can agree.'
    ),
    cluster=StarClusters.HYADES,
)

HYD_0055 = System(
    name='HYD-0055',
    star='Orange main sequence (K1V), approximately 0.5 times Sol luminosity -- a stable, quiet star at the edge of Hyadean space, waiting for a decision that the guild council is not ready to make',
    population=0,
    distance_to_sol=260.0,
    stellar_objects=[
        StellarObject(
            name='HYD-0055-a',
            short_description='A habitable world at the edge of the cluster -- promising, distant, and raising the question that the guild republic does not want to answer: what happens when a colony can make its own prosthetics.',
            long_description=(
                'HYD-0055-a is a temperate world in the habitable zone of a stable orange '
                'star -- breathable atmosphere at roughly ninety percent standard pressure, '
                'surface water, moderate climate, and soil chemistry that the survey team '
                'assessed as suitable for agriculture with minimal engineering. The world is '
                'habitable. The world could support a colony. The survey team has been in '
                'the system for three years and the data supports what the initial '
                'assessment suggested: HYD-0055-a is a viable colonisation candidate.\n\n'
                'The distance is the problem and the distance is the point. HYD-0055 is '
                'the furthest system the Hyades has reached -- at the end of a jump chain '
                'that places it farther from the cluster\'s core than any other discovered '
                'system. The transit from the nearest inhabited system takes weeks. A '
                'colony at HYD-0055 would be the most isolated Hyadean settlement in '
                'existence, dependent on a supply chain that stretches across jump links '
                'that any disruption could sever.\n\n'
                'A colony that isolated would need to be self-sustaining. Self-sustaining '
                'means local food production, local energy, local manufacturing. Local '
                'manufacturing means local prosthetics production. Local prosthetics '
                'production means a colony that does not depend on the guild system for '
                'the hardware that defines Hyadean life. A colony that manufactures its '
                'own prosthetics does not need the guilds. A colony that does not need '
                'the guilds does not need the guild council. A colony that does not need '
                'the guild council is not governed by the guild republic.\n\n'
                'The logic is the same logic that keeps CNP-5502 unsettled in the Canopus '
                'cluster -- a colony too far from the centre is a colony that can survive '
                'without the centre, and a colony that can survive without the centre is '
                'a colony the centre cannot control. The Canopan emperors fear a colony '
                'with independent reanimation. The Hyadean guilds fear a colony with '
                'independent manufacturing. The technology is different. The political '
                'calculation is identical.\n\n'
                'The survey team continues to collect data. The guild council receives '
                'the reports and does not authorise colonisation. The world orbits its '
                'quiet star at the edge of known Hyadean space, habitable and empty, '
                'waiting for a decision that the guilds are in no hurry to make because '
                'the guilds have built a civilisation on dependency and the world at the '
                'edge does not need them.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-0055-b',
            short_description='A cold, rocky world with mineral deposits -- the resource base that would make a self-sustaining colony viable and that makes the guild council\'s reluctance sharper.',
            long_description=(
                'HYD-0055-b is a cold, rocky world in the outer habitable zone -- not '
                'comfortable for surface habitation but mineral-rich in the specific '
                'deposits that prosthetic manufacturing requires. The survey team\'s '
                'mineralogist identified alloys, structural metals, and traces of the '
                'compounds that the precision-workers\' and interface specialists\' guilds '
                'use in their hardware. The deposits are not as rich as Enif\'s or as '
                'rare as the compounds from Glennah\'s peculiar star. They are adequate. '
                'They are enough.\n\n'
                'Adequate and enough are the words that make the guild council nervous. A '
                'colony with access to adequate mineral deposits and enough manufacturing '
                'capacity could produce its own prosthetics -- not the premium hardware '
                'that Glennah\'s research enables, not the specialised equipment that '
                'Alpha Pegasi\'s foundries produce, but the standard guild-grade hardware '
                'that the majority of the cluster\'s population uses. A colony that can '
                'produce standard hardware does not need to import it. A colony that does '
                'not need to import it does not need the supply chain. A colony that does '
                'not need the supply chain does not need the guilds that control it.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-0055-c',
            short_description='A gas giant with fuel processing potential -- the third element that would make the colony self-sustaining and the guild council\'s decision more difficult.',
            long_description=(
                'HYD-0055-c is a mid-sized gas giant in the outer system -- standard '
                'composition, suitable for fuel processing. The survey team has used it '
                'as their fuel source during the three-year mission, skimming the upper '
                'atmosphere with the same equipment they carried from the cluster\'s core. '
                'The gas giant completes the self-sufficiency equation: habitable world for '
                'the colony, mineral-rich world for the manufacturing, fuel giant for the '
                'energy and transit. The system contains everything a colony would need to '
                'function independently.\n\n'
                'The survey team\'s mission commander noted in the latest report that the '
                'system is the most complete self-sustaining prospect the cluster has '
                'found. The note was factual, not advocacy. The commander understands that '
                'the completeness is precisely what makes the system politically difficult, '
                'and that drawing attention to the completeness does not accelerate the '
                'council\'s decision. The commander has served long enough to understand '
                'that the guild council\'s reluctance is not about the system\'s viability. '
                'The viability is the problem.'
            ),
            population=0,
        ),
        StellarObject(
            name='HYD-0055-d',
            short_description='A frozen outer body at the edge of the furthest known Hyadean system -- the most distant point the cluster has reached.',
            long_description=(
                'HYD-0055-d is a frozen body in the far outer system -- ice and rock, '
                'catalogued by long-range scan and not visited. The body is the most '
                'distant known object in Hyadean space -- a point of cold rock at the '
                'edge of the furthest system the cluster has discovered, 260 light-years '
                'from Sol.\n\n'
                'The survey team\'s astronomer logged the body with a note that mirrors '
                'the one in CNP-5502\'s records: furthest known Hyadean object. The '
                'parallel with the Canopus cluster\'s furthest reach is not accidental -- '
                'both factions have found worlds at their edges that they could settle and '
                'have chosen not to, for the same reason, wearing different masks. The '
                'emperors call it strategic caution. The guilds call it economic prudence. '
                'The meaning is the same: the centre holds because the edges depend on '
                'it, and a colony that does not depend on the centre is a colony the '
                'centre fears.'
            ),
            population=0,
        ),
    ],
    short_description='The furthest reach -- a system at the edge of Hyadean space with everything a colony would need, unsettled because a self-sustaining colony is a colony the guilds cannot control.',
    long_description=(
        'HYD-0055 is the furthest system the Hyades has discovered -- at the end '
        'of a jump chain that places it farther from the cluster\'s core than any '
        'other known system. The star is a stable orange main sequence. The primary '
        'world is habitable -- breathable atmosphere, surface water, soil suitable '
        'for agriculture. The second world is mineral-rich with the deposits that '
        'prosthetic manufacturing requires. The gas giant provides fuel. The system '
        'contains everything a colony would need to function independently.\n\n'
        'The independence is the problem. A colony this far from the core would '
        'need to be self-sustaining. Self-sustaining means local prosthetics '
        'production. Local prosthetics production means a colony that does not '
        'depend on the guild system for the hardware that defines Hyadean life. A '
        'colony that does not need the guilds does not need the guild council. A '
        'colony that does not need the guild council is not governed by the guild '
        'republic. The logic is a chain that leads from adequate mineral deposits '
        'to political independence, and the guild council can see every link.\n\n'
        'The parallel with CNP-5502 in the Canopus cluster is precise. Both '
        'factions have found worlds at their edges that they could settle and have '
        'chosen not to. The Canopan emperors fear a colony with independent '
        'reanimation capability. The Hyadean guilds fear a colony with independent '
        'manufacturing capability. The technology is different. The political '
        'calculation is identical. The centre holds because the edges depend on it, '
        'and a colony that does not depend on the centre is a colony the centre '
        'fears.\n\n'
        'The survey team continues to collect data. The guild council receives the '
        'reports and does not authorise colonisation. The mission commander '
        'understands that the system\'s viability is precisely what makes it '
        'politically difficult. The guilds have built a civilisation on dependency '
        '-- the body follows the guild, the guild follows the council, the council '
        'controls the supply. HYD-0055 is the world where the dependency could '
        'end, and the guilds are in no hurry to let it begin.'
    ),
    cluster=StarClusters.HYADES,
)

HYADES_SYSTEMS: list[System] = [
    AIN, GENIB, ALGIEBA, ALPHA_PEGASI, ALPHARD, CHAMUKUY,
    HYD_7703, ENIF, SECUNDA_HYADUM, GLENNAH, HYD_4478, MUSCIDA,
    HYD_1192, EPSILON_TAURI, SCHEAT, PRIMA_HYADUM, HYD_0055,
]
