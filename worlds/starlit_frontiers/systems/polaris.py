from ..enums import StarClusters
from .models import System, StellarObject


POLARIS = System(
    name='Polaris',
    star='Yellow-white supergiant triple system: Polaris Aa (F7Ib, approximately 1,260 times Sol luminosity) with two smaller companions -- the North Star, the one fixed point in Earth\'s sky, now the gateway to a civilisation where nobody is where they appear to be',
    population=9_000_000_000,
    distance_to_sol=430.0,
    stellar_objects=[
        StellarObject(
            name='Ondaren',
            short_description='The gateway world -- five billion people in a city whose streets are empty because the population is indoors, plugged in, their bodies stationary in interface rigs while their minds work across the cluster.',
            long_description=(
                'Ondaren is the first thing visitors see in the Polaris cluster, and the '
                'first thing visitors notice is that nobody is outside. The planet has five '
                'billion people. The cities are designed for five billion people. The '
                'streets, the transit systems, the public spaces -- all built for a '
                'population that uses them only in the gaps between sessions, during the '
                'hours when the bodies need to eat, exercise, and move before returning '
                'to the rigs. The cities of Ondaren are empty during working hours because '
                'the population is indoors: sitting in interface chairs, lying in cradles, '
                'connected to the neural network, their bodies stationary and their minds '
                'operating surgical robots on Schedar, running mining rigs on Grumium, '
                'designing structures in the VR studios on Cor Caroli.\n\n'
                'The architecture reflects the reality. The buildings are designed around '
                'the rigs -- residential blocks where each apartment contains the interface '
                'cradle that is the most important piece of furniture in a Polaran home. '
                'The cradles maintain the body during connection: hydration, temperature '
                'regulation, the gentle muscle stimulation that prevents atrophy during '
                'long sessions. The wealthy have private cradles with medical monitoring '
                'and premium interface hardware. The poor use shared rigs in commercial '
                'centres -- rows of chairs in rented spaces, bodies side by side, minds '
                'scattered across the cluster.\n\n'
                'The neural interface infrastructure on Ondaren is the most sophisticated '
                'in the cluster. Basic non-surgical interfaces -- headsets, contact patches '
                '-- are available for visitors from MERIT space to experience the network. '
                'The experience is disorienting: the network is not a screen. It is a '
                'layer of perception that overlays the user\'s senses with data, '
                'communication, and the presence of other connected minds. A visitor who '
                'puts on a basic interface for the first time feels the network the way a '
                'deaf person feels sound for the first time -- overwhelming, beautiful, '
                'and impossible to explain to someone who has not experienced it.\n\n'
                'The military presence is substantial. The defense fleet that guards the '
                'gateway is neural-piloted -- pilots with surgical interface ports along '
                'the spine, skull, and forearms, giving them direct neural connections to '
                'their ships\' systems. A neural-piloted fighter does not respond to hands '
                'on controls. It responds to the pilot\'s intentions, the ship moving '
                'before the conscious thought that would have directed a manual input is '
                'complete. The reaction time advantage is decisive in open-space combat '
                'and deeply unsettling to MERIT commanders who must plan against opponents '
                'whose ships respond at the speed of thought.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Vestallen',
            short_description='A residential world where the disconnect hours are the only hours the city comes alive -- the brief windows when the population unplugs to eat, exercise, and remember they have bodies.',
            long_description=(
                'Vestallen is Ondaren\'s residential companion -- a temperate world where '
                'much of the system\'s workforce lives. The rhythm of life on Vestallen is '
                'defined by the disconnect hours -- the periods when the population unplugs '
                'from their interface rigs and the streets fill with people who have been '
                'sitting still for hours, blinking in the sunlight, stretching muscles that '
                'the cradle\'s stimulation systems have kept functional but that feel stiff '
                'after a long session.\n\n'
                'The disconnect hours are when Vestallen becomes a city. The restaurants '
                'fill. The parks fill. The social life that physical presence requires '
                'happens in compressed bursts -- people meeting, talking, touching in the '
                'hours between sessions because the sessions are where they work and the '
                'disconnect hours are where they live. The culture has adapted: meals are '
                'social events because they are the time when everyone is physically '
                'present. Exercise is communal because the body needs movement and the '
                'movement is better shared. The relationships that matter are maintained '
                'in the disconnect hours with an intensity that visitors find exhausting '
                'and that the residents consider normal -- you have limited time with the '
                'people you love in the same room. You do not waste it.\n\n'
                'The children of Vestallen grow up in the disconnect hours. The parents '
                'are present -- physically, attentively present -- during the hours they '
                'are unplugged, and absent during the hours they are connected. The '
                'children learn early that the parent in the cradle is working and the '
                'parent at the dinner table is theirs. The boundary is clear. The children '
                'accept it because it is all they have known, and they look forward to the '
                'age when they will have their own rigs and their own sessions and their '
                'own work somewhere else in the cluster.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Interface',
            short_description='The system\'s primary orbital port -- where the interface screening happens, the basic headsets are issued, and visitors learn that they have been living without a sense they did not know existed.',
            long_description=(
                'The Interface is the orbital port above Ondaren -- the facility where '
                'visitors are processed, screened for neural compatibility, and offered '
                'their first basic interface. The station handles the transition between '
                'the unconnected world of MERIT space and the networked world of the '
                'Polaris cluster.\n\n'
                'The first-time interface experience is carefully managed. The station\'s '
                'staff guide visitors through the initial connection -- the moment when '
                'the network becomes perceptible and the visitor realises that every '
                'Polaran they have met has been perceiving a layer of reality that the '
                'visitor could not see, hear, or feel. The reactions vary. Some find it '
                'transcendent. Some find it invasive. Some remove the interface immediately '
                'and do not put it back on. The staff have seen every reaction and judge '
                'none of them.\n\n'
                'The military screening is the station\'s other function. Every arrival is '
                'assessed for hostile interface capability -- MERIT intelligence hardware '
                'designed to probe or disrupt the network. The screening is the most '
                'advanced countermeasure suite in the galaxy, because the network is the '
                'cluster\'s nervous system and an intrusion is an intrusion into everything.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Wenthane',
            short_description='A gas giant with fuel processing operated via telepresence -- the workers sit in cradles on orbital stations and pilot skimmers through the atmosphere without leaving their chairs.',
            long_description=(
                'Wenthane is the system\'s gas giant -- fuel processing at gateway scale, '
                'operated via telepresence. The fuel skimmers in Wenthane\'s atmosphere are '
                'robotic -- remotely operated by workers sitting in interface cradles on '
                'orbital stations, their bodies stationary, their minds connected to the '
                'skimmer controls through the neural network. The workers experience the '
                'gas giant\'s atmosphere through the skimmers\' sensors -- the pressure, '
                'the turbulence, the chemical composition rendered as sensory data.\n\n'
                'The arrangement is standard Polaran industry: the dangerous work is '
                'performed by machines controlled by minds in safe locations. When the '
                'shift ends, the worker disconnects, stands up from the cradle, and walks '
                'to the station\'s common areas. The transition from piloting a skimmer '
                'in a gas giant\'s atmosphere to standing in a corridor is instantaneous '
                'and routine -- a commute measured in the time it takes to unplug rather '
                'than the distance between home and workplace.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Tilderen',
            short_description='An agricultural world where the farming is physical -- the one major industry in the system that requires hands in the soil rather than minds in the network.',
            long_description=(
                'Tilderen is the system\'s agricultural world -- terraformed, temperate, '
                'and the most physically active population in the gateway system. Farming '
                'on Tilderen is largely conventional -- the crops require physical tending, '
                'the livestock require physical handling, and the sensory feedback from a '
                'robotic proxy is not yet precise enough for the delicate judgment that '
                'agriculture demands.\n\n'
                'The farmers on Tilderen are the system\'s most grounded population -- '
                'people who spend their working hours in the physical world rather than in '
                'interface cradles. They use basic interfaces for communication and data '
                'management, but the core work is hands-on. The farmers regard the '
                'telepresence economy with the amused tolerance of people who understand '
                'that somebody has to grow the food that the bodies in the cradles consume. '
                'The disconnect hours that structure life on Ondaren and Vestallen do not '
                'apply on Tilderen -- the farmers are disconnected by default and connect '
                'when they choose to, which is the inverse of every other population in '
                'the system.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Caskren',
            short_description='A hot inner world -- energy collection and the cluster\'s primary network security facility, because a breach in the neural network is a breach in the cluster\'s reality.',
            long_description=(
                'Caskren is a hot inner world hosting energy collection arrays and the '
                'cluster\'s primary network security facility. The security installation '
                'develops and maintains the countermeasures that protect the neural network '
                'from hostile intrusion.\n\n'
                'The network is the cluster\'s nervous system. A successful attack could '
                'disrupt every telepresence connection in the cluster -- severing workers '
                'from the equipment they operate, surgeons from the patients they are '
                'mid-procedure on, pilots from the ships they fly. A more sophisticated '
                'attack could inject false sensory data into the interfaces of millions of '
                'connected people, or compromise the neural links the military pilots use. '
                'The security staff treat network defense with the seriousness other '
                'factions reserve for nuclear deterrence, because the consequences of a '
                'breach are comparable.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='Gateway to the Polaris cluster -- nine billion people in cities whose streets are empty during working hours because the population is indoors, plugged in, their minds working across the cluster while their bodies sit still.',
    long_description=(
        'Polaris is the front door to a civilisation where nobody is where they '
        'appear to be. The gateway system\'s nine billion people live on worlds '
        'whose streets empty during working hours -- the population indoors in '
        'interface cradles, bodies stationary, minds operating surgical robots, '
        'mining rigs, and construction equipment across the cluster through the '
        'neural network.\n\n'
        'The neural interface is the first thing visitors encounter. Basic non-'
        'surgical headsets available to anyone. The experience of connecting for '
        'the first time is the gateway\'s defining moment: the network is not a '
        'screen but a layer of perception, an awareness of other minds, a sense '
        'the visitor did not know existed. The buildings are designed around the '
        'rigs -- apartments built around the interface cradle that is the most '
        'important piece of furniture in a Polaran home. The wealthy have private '
        'cradles with medical monitoring. The poor use shared rigs in commercial '
        'centres, bodies side by side, minds scattered across the cluster.\n\n'
        'Life is structured around the disconnect hours -- the windows when the '
        'population unplugs to eat, exercise, socialise, and remember they have '
        'bodies. The restaurants fill. The streets fill. Relationships are '
        'maintained with compressed intensity because the time when everyone is '
        'physically present is limited and precious.\n\n'
        'The defense fleet is neural-piloted -- surgically enhanced pilots whose '
        'ships respond to intention rather than manual input, moving before the '
        'conscious thought is complete. The reaction time advantage is decisive '
        'and deeply unsettling to MERIT commanders. The Interface screens every '
        'arrival for hostile interface capability, because the network is the '
        'cluster\'s nervous system and an intrusion into the network is an '
        'intrusion into everything.'
    ),
    cluster=StarClusters.POLARIS,
)


KOCHAB = System(
    name='Kochab',
    star='Orange giant (K3III), approximately 500 times Sol luminosity -- an old, warm star whose amber light falls on the shipyards where people become ships and the ships become the government',
    population=12_000_000_000,
    distance_to_sol=130.0,
    stellar_objects=[
        StellarObject(
            name='Thessan',
            short_description='The capital of the Polaris cluster -- six billion people governed from orbit by Cores who have not touched the ground in decades and who experience the world they rule through sensor feeds.',
            long_description=(
                'Thessan is the capital of the Polaris cluster -- the most populous world, '
                'the administrative centre, and the planet the government orbits but does '
                'not touch. The Cores -- the pilots permanently fused to their capital '
                'ships -- circle Thessan in the orbital fleet that is simultaneously the '
                'cluster\'s military backbone and its governing body. The stratocracy is '
                'literal: the people who command the most powerful ships in the fleet are '
                'the people who command the civilisation, and they do both from the same '
                'interface.\n\n'
                'The Cores govern through the network. Their decisions are transmitted to '
                'the ground as policy -- legislation, resource allocation, strategic '
                'direction, the thousand administrative functions that a civilisation of '
                'billions requires. The Cores experience the consequences of their '
                'decisions through sensor feeds, data streams, and the reports that the '
                'ground administration provides. They have not walked on Thessan\'s '
                'surface. They have not breathed its air. They have not felt its gravity '
                'in years or decades. The world they govern is an abstraction to them -- '
                'a data set, a sensor image, a collection of metrics that describe a '
                'planet they can see from orbit and cannot visit because their bodies are '
                'fused to ships that will never land.\n\n'
                'The ground population of Thessan lives under this arrangement with the '
                'complicated acceptance of people who understand that the Cores are the '
                'best pilots, the best networked minds, and the most committed citizens '
                'the cluster has produced -- and who also understand that the Cores have '
                'not stood in a queue, eaten a meal they cooked themselves, or held another '
                'person\'s hand in longer than most of the ground population has been alive. '
                'The Cores\' decisions are competent. The Cores\' understanding of what life '
                'on the ground feels like is increasingly theoretical. The gap between '
                'competence and understanding is the central tension of Polaran politics.\n\n'
                'The city of Thessan is the cluster\'s largest -- administrative districts, '
                'residential blocks built around interface cradles, the commercial centres '
                'where the shared rigs operate, and the government liaison offices where '
                'the ground administration translates the Cores\' policy into the practical '
                'reality of managing a planet the governors cannot touch.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='The Fundament',
            short_description='The orbital shipyard where the Cores are made -- where a pilot enters a capital ship and does not leave, the fusion procedure binding mind to vessel in a process that is irreversible and voluntary and the most solemn act in the cluster.',
            long_description=(
                'The Fundament is the orbital shipyard complex above Thessan where two '
                'things happen: capital ships are built, and people are fused to them. The '
                'construction is enormous -- the capital ships of the Polaran fleet are '
                'the largest vessels in the galaxy, designed not just as warships but as '
                'permanent habitats for the mind that will occupy them. A Core\'s ship is '
                'not a vehicle. It is a body -- the pilot\'s nervous system extended '
                'through the hull, the sensors becoming eyes and ears, the engines becoming '
                'muscles, the weapons becoming hands.\n\n'
                'The fusion procedure is performed in the Fundament\'s deep bays -- sealed '
                'surgical environments where the pilot is connected to the ship through a '
                'series of neural interfaces that are progressively more invasive, more '
                'permanent, and more total. The early stages are surgical -- ports '
                'installed along the spine, the skull, the major nerve clusters, each one '
                'extending the pilot\'s neural reach further into the ship\'s systems. The '
                'later stages are biological -- the pilot\'s nervous system grows into the '
                'ship\'s interface architecture, forming connections that cannot be severed '
                'without killing the pilot. The final stage is cognitive -- the pilot\'s '
                'sense of self expands to include the ship, the boundary between person '
                'and vessel dissolving until the Core does not experience the ship as '
                'something they are inside but as something they are.\n\n'
                'The fusion is voluntary. Every Core chose this. The candidates are the '
                'cluster\'s best pilots -- neural integration veterans who have spent '
                'careers flying with surgical ports and who choose to take the final step. '
                'The ceremony before the fusion is the most solemn event in the cluster -- '
                'the candidate says goodbye to the people they will never touch again, '
                'walks into the ship under their own power for the last time, and lies '
                'down in the fusion bay knowing that they will never lie down again because '
                'the concept of lying down will cease to have meaning when their body is a '
                'ship. The families attend. The families always attend. The goodbye is '
                'permanent in a way that death is not -- the Core will still be alive, '
                'still be present on the network, still be reachable. But never touchable. '
                'Never in the same room. Never again a person who can be held.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Drevnik',
            short_description='A second world housing the support infrastructure -- the people who maintain the ships the Cores inhabit, performing the closest thing to healthcare the Cores receive.',
            long_description=(
                'Drevnik is Kochab\'s second inhabited world -- a cooler, quieter planet '
                'that houses the support infrastructure for the Core fleet. The maintenance '
                'crews who service the capital ships are the people who keep the Cores '
                'alive -- the technicians, engineers, and medical specialists who maintain '
                'the ships\' life support, the neural interface connections, and the '
                'biological support systems that sustain the pilot\'s body inside the '
                'vessel.\n\n'
                'The work is intimate and strange. A maintenance crew that services a '
                'Core\'s ship is performing the closest thing to healthcare the Core '
                'receives -- checking the neural connections, monitoring the pilot\'s '
                'biological functions, maintaining the systems that keep a human body '
                'alive inside a warship. The crews develop relationships with the Cores '
                'they maintain -- not friendships exactly, because the Core\'s experience '
                'of reality is so different from the crew\'s that the common ground for '
                'friendship is narrow, but something closer to the relationship between a '
                'caretaker and the person they care for. The crews know their Core\'s '
                'medical data, their neural patterns, the signs that indicate stress or '
                'degradation in the interface connections. The crews are the only people '
                'who enter the Core\'s ship, the only people who see the pilot\'s body in '
                'the fusion bay, and the only people who understand that the governing '
                'mind of the cluster is a human being in a chamber who has not moved under '
                'their own power in decades.\n\n'
                'The maintenance crews do not discuss what they see. The Cores\' physical '
                'condition is classified -- not because it is secret but because the '
                'ground population\'s image of the Cores as powerful, elevated beings who '
                'have transcended physical limitation is easier to maintain when the '
                'population does not think too carefully about what transcendence looks '
                'like in a fusion bay.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='The Procession',
            short_description='The orbital corridor where the Core fleet circles Thessan -- the visible manifestation of the government, a ring of capital ships that the ground population can see in the night sky.',
            long_description=(
                'The Procession is the orbital corridor above Thessan where the Core fleet '
                'maintains its formation -- the governing fleet visible from the ground as '
                'a chain of lights circling the planet. The Cores orbit in formation '
                'because the formation is the government\'s physical expression -- the '
                'fleet that protects the cluster is the same fleet that governs it, and '
                'the formation above the capital is the visible symbol that the two '
                'functions are one.\n\n'
                'The ground population of Thessan can look up at night and see the '
                'Procession -- the chain of lights that are the capital ships that are the '
                'Cores that are the government. The sight is intended to inspire. The sight '
                'does inspire, for most. For some it produces something else -- the '
                'awareness that the lights in the sky are people who were once like them '
                'and who chose to become something that can never come down, and that those '
                'people make decisions about the lives below with a perspective that is '
                'literally orbital. The Procession is the most visible symbol in the '
                'cluster. What it symbolises depends on who is looking up.'
            ),
            population=0,
        ),
        StellarObject(
            name='Olskane',
            short_description='A gas giant where the fuel processing supports the capital\'s enormous fleet -- the Cores\' ships consume fuel at rates that dwarf civilian traffic.',
            long_description=(
                'Olskane is the system\'s gas giant -- fuel processing at a scale that '
                'reflects the capital\'s fleet requirements. The Core ships are the largest '
                'vessels in the galaxy and their fuel consumption is proportional. The '
                'fuel operations on Olskane\'s moons are the largest in the cluster, '
                'operated via telepresence by workers in cradles on Drevnik\'s orbital '
                'stations.\n\n'
                'The fuel workers are aware that they are feeding the government. The '
                'fuel that Olskane produces goes to the Procession -- to the ships that '
                'are the Cores that are the stratocracy. A disruption in Olskane\'s fuel '
                'supply would not ground the government -- the Cores\' ships carry reserves '
                'measured in months -- but it would force the fleet to reduce operations '
                'and eventually to disperse from the Procession to refuel elsewhere. The '
                'symbolic impact of the Procession breaking formation would be significant '
                'even if the practical impact was manageable.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Stenmark',
            short_description='An agricultural world feeding the capital -- conventional farming by a physically present workforce, with the added requirement of feeding a fleet that never docks.',
            long_description=(
                'Stenmark is the system\'s agricultural world -- terraformed, temperate, '
                'producing food for the capital\'s twelve billion people and the Core fleet '
                'that orbits above. The farming is conventional -- physical work, hands in '
                'soil, the same agricultural reality that every cluster\'s breadbasket '
                'shares.\n\n'
                'The supply chain to the Procession is Stenmark\'s distinctive contribution '
                '-- the regular shipments of food and consumables to the Core ships, which '
                'never dock at a station and must be resupplied by tender vessels that '
                'match the fleet\'s orbital velocity and transfer cargo in space. The '
                'supply tenders are a constant presence in the Procession -- small ships '
                'moving between the capital ships, delivering the food, water, and medical '
                'supplies that the Cores\' biological bodies still require even though the '
                'Cores themselves have not thought about food in years. The bodies are fed '
                'by the maintenance systems. The Cores do not experience hunger. The bodies '
                'need nutrition anyway. The tenders carry it up.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='The Anteroom',
            short_description='The orbital facility where Core candidates prepare -- the last place a candidate lives as a person before becoming a ship.',
            long_description=(
                'The Anteroom is the orbital station where Core candidates spend their '
                'final months before the fusion procedure. The preparation is physical, '
                'psychological, and bureaucratic -- the candidate\'s body is assessed for '
                'fusion compatibility, the neural interface infrastructure is progressively '
                'expanded with additional surgical ports, and the candidate\'s affairs are '
                'settled. The settling includes legal arrangements, family provisions, and '
                'the formal transfer of all personal property, because a Core owns nothing '
                '-- the ship is not the Core\'s property. The Core is the ship\'s pilot. '
                'The distinction matters legally and the candidates learn to accept it.\n\n'
                'The Anteroom\'s culture is unique in the cluster. The candidates know what '
                'they are about to do. They are about to give up their bodies, their '
                'ability to touch, their ability to stand in sunlight, and their ability '
                'to be in the same room as anyone they love. They chose this. They are '
                'the cluster\'s best. The mood in the Anteroom is not grief -- it is the '
                'focused, solemn intensity of people who are about to do something '
                'irreversible that they believe is the most important thing a person can '
                'do. The candidates eat their last meals with their families. The meals '
                'are long. Nobody hurries them.'
            ),
            population=20_000_000,
        ),
    ],
    short_description='The capital -- twelve billion people governed from orbit by Cores who have not touched the ground in decades, in a system where the shipyards build the ships and the ships become the government.',
    long_description=(
        'Kochab is the capital of the Polaris cluster and the place where people '
        'become ships. The Cores -- pilots permanently fused to capital ships -- '
        'orbit Thessan in the Procession, a chain of lights visible from the ground '
        'that is simultaneously the military fleet and the governing body. The '
        'stratocracy is literal: the people who command the most powerful ships '
        'command the civilisation, and they do both from the same interface.\n\n'
        'The Fundament is where the fusion happens -- orbital shipyards where the '
        'capital ships are built and the candidates are connected through '
        'progressively more invasive neural interfaces until the pilot\'s nervous '
        'system grows into the ship and the boundary between person and vessel '
        'dissolves. The fusion is voluntary. The ceremony before it is the most '
        'solemn event in the cluster -- the candidate says goodbye to the people '
        'they will never touch again and walks into the ship for the last time. '
        'The Core will still be alive, still reachable on the network. Never '
        'touchable. Never in the same room. Never again a person who can be held.\n\n'
        'The Cores govern through the network -- policy transmitted to the ground, '
        'consequences experienced through sensor feeds and data. They have not '
        'walked on Thessan, breathed its air, or felt its gravity in decades. The '
        'world they govern is a data set. Their decisions are competent. Their '
        'understanding of what ground life feels like is increasingly theoretical. '
        'The gap between competence and understanding is the central tension of '
        'Polaran politics.\n\n'
        'The Anteroom prepares the candidates. The maintenance crews on Drevnik '
        'keep the Cores alive -- the only people who enter the ships and see the '
        'pilot\'s body in the fusion bay. What transcendence looks like in a fusion '
        'bay is classified, not because it is secret but because it is easier to '
        'maintain the image of the Cores as elevated beings when the population '
        'does not think too carefully about it.'
    ),
    cluster=StarClusters.POLARIS,
)

ELTANIN = System(
    name='Eltanin',
    star='Orange giant (K5III), approximately 700 times Sol luminosity -- a stable, unspectacular star hosting the most important and least exciting system in the cluster',
    population=5_000_000_000,
    distance_to_sol=150.0,
    stellar_objects=[
        StellarObject(
            name='Condaren',
            short_description='The network world -- three billion people maintaining the infrastructure that connects every mind in the cluster, in a system that nobody visits on purpose and everybody depends on.',
            long_description=(
                'Condaren is the world the Polaris cluster cannot function without and '
                'that nobody would choose to visit. The planet hosts the central processing '
                'infrastructure of the cluster-wide neural network -- the relay stations, '
                'signal processors, routing systems, and data centres that carry every '
                'telepresence connection, every network communication, and every neural '
                'pilot\'s link to their ship. The network is the cluster\'s nervous system. '
                'Condaren is the spine.\n\n'
                'The infrastructure is vast and physically unimpressive. The relay stations '
                'are arrays of processing units in hardened facilities -- bunkers spread '
                'across the planet\'s surface and in orbital installations, redundant, '
                'shielded, and maintained by a population whose entire professional '
                'existence is devoted to ensuring that the signal never drops. The work is '
                'monitoring, maintenance, and the incremental upgrades that keep the '
                'network\'s capacity ahead of the cluster\'s growing demand. The work is '
                'unglamorous. The work is essential. The technicians on Condaren accept '
                'the combination with the resigned pride of people who know that the '
                'moment they stop doing their jobs, every surgeon mid-operation in the '
                'cluster loses contact with their patient.\n\n'
                'The population is technical -- engineers, signal specialists, systems '
                'architects, and the support staff that any population of three billion '
                'requires. The culture on Condaren is defined by the work: precise, '
                'methodical, and allergic to the dramatic. The rest of the cluster deals '
                'in the extraordinary -- Cores fused to ships, telepresence across light-'
                'years, VR environments that rival reality. Condaren deals in latency '
                'measurements, packet routing, and the firmware updates that prevent the '
                'extraordinary from collapsing. The system\'s unofficial motto, printed on '
                'mugs in every control room, is attributed to a long-dead chief engineer: '
                'the network works because we do. The motto is unremarkable. The truth of '
                'it is absolute.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Lattice',
            short_description='The orbital relay network -- a constellation of signal processing stations that form the cluster\'s primary data backbone, carrying every connection the civilisation depends on.',
            long_description=(
                'The Lattice is the orbital component of Eltanin\'s network infrastructure '
                '-- a constellation of relay stations in carefully calculated orbits that '
                'provide the signal routing the cluster\'s inter-system connections require. '
                'The stations are small, automated where possible, and crewed where '
                'automation is insufficient -- the signal processing that the neural '
                'network demands is too complex for fully automated management and too '
                'critical for the latency that automated failover introduces.\n\n'
                'The Lattice carries everything. The telepresence connections that let a '
                'worker on Polaris operate a mining rig on Grumium. The neural pilot links '
                'that connect the fleet to their ships. The Core-to-Core communication '
                'that the stratocracy uses for governance. The civilian data traffic that '
                'the population generates. The entertainment, the social connections, the '
                'personal communications -- all of it flows through the Lattice, and the '
                'Lattice\'s operators maintain the infrastructure with the knowledge that '
                'a failure is not a dropped call but a dropped civilisation.\n\n'
                'The redundancy is extreme. Every relay station has a backup. Every '
                'routing path has alternatives. Every critical system has failover that '
                'activates in milliseconds. The redundancy is the reason the network has '
                'never experienced a cluster-wide failure, and the engineers who maintain '
                'the redundancy are the reason the redundancy works. The Lattice is the '
                'most reliable piece of infrastructure in the galaxy. The reliability is '
                'not automatic. It is the product of people who have devoted their '
                'careers to ensuring that a thing that must not fail does not fail.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Morsten',
            short_description='A cold world hosting the network\'s deep storage -- the archive of every transaction, communication, and connection the cluster has ever made.',
            long_description=(
                'Morsten is a cold world in the outer habitable zone that hosts the '
                'network\'s deep storage facilities -- the archive where the data the '
                'cluster generates is stored. Every telepresence session, every neural '
                'pilot log, every communication, every transaction -- the data is '
                'compressed, catalogued, and stored in hardened facilities beneath '
                'Morsten\'s frozen surface.\n\n'
                'The cold is an asset. The storage facilities generate heat that the '
                'planet\'s environment absorbs, reducing the cooling costs that data '
                'centres in warmer environments must manage. The facilities are buried '
                'deep -- shielded from solar radiation, seismic activity, and the kind of '
                'military strike that would target the cluster\'s data archive. The '
                'population is small and specialised -- data management staff, security '
                'personnel, and the archivists who maintain the records that the legal and '
                'administrative systems of the cluster depend on.\n\n'
                'The archive contains the neural logs of every Core that has ever governed '
                '-- the decision records, the deliberation data, the neural patterns of '
                'the minds that have led the cluster. The logs are legally significant, '
                'historically valuable, and deeply private. The archivists who manage them '
                'carry security clearances that reflect the sensitivity of data that is '
                'not merely what the Cores decided but how the Cores\' minds worked when '
                'they decided it.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='The Switchboard',
            short_description='The network engineering academy -- where the technicians who keep the cluster connected are trained, because the network is too important to be maintained by anyone who learned on the job.',
            long_description=(
                'The Switchboard is the orbital training facility where Eltanin\'s network '
                'engineers are produced. The academy is the most selective technical '
                'programme in the cluster -- the entrance requirements are rigorous because '
                'the graduates will be responsible for infrastructure that the civilisation '
                'cannot survive without, and the training is thorough because the '
                'consequences of a poorly trained engineer making a mistake are measured in '
                'the connections that drop when the mistake propagates through the network.\n\n'
                'The curriculum includes deliberate failure exercises -- controlled network '
                'disruptions in sandboxed environments that simulate the cascading effects '
                'of a relay failure, a routing collapse, or a hostile intrusion. The '
                'trainees experience what the cluster would experience if the network '
                'failed: the telepresence connections severing, the pilot links dropping, '
                'the Cores\' governance feed cutting out. The exercises are stressful by '
                'design. The trainees who cannot perform under the stress of a simulated '
                'failure are not cleared for the real infrastructure, because a real '
                'failure would be worse and the engineer must function anyway.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Torveldt',
            short_description='A gas giant with fuel processing and the system\'s emergency power reserves -- because the network cannot run without power and the power cannot be allowed to fail.',
            long_description=(
                'Torveldt is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic and, more critically, the emergency '
                'power reserves that the network infrastructure maintains. The relay '
                'stations, the processing centres, the Lattice -- all of them carry backup '
                'power that Torveldt\'s fuel operations supply. The reserves are sized for '
                'a scenario the engineers hope never occurs: a total power failure across '
                'the system that the backup reserves must bridge until primary power is '
                'restored.\n\n'
                'The fuel workers on Torveldt share the system\'s culture of quiet '
                'competence -- the understanding that their work is part of the redundancy '
                'that keeps the network running, and that the redundancy is the reason the '
                'network has never failed. The fuel workers find this satisfying in the '
                'specific way that infrastructure workers find reliability satisfying -- '
                'the best outcome is the one where nothing happens and nobody notices.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Grenden',
            short_description='An agricultural world feeding the system -- conventional farming by people who grow the food that keeps the network engineers alive so the engineers can keep the network alive.',
            long_description=(
                'Grenden is the system\'s agricultural world -- terraformed, temperate, '
                'and unremarkable in every way except its function. The farms feed the '
                'system\'s five billion people, the majority of whom are employed in the '
                'network infrastructure that the rest of the cluster depends on. The '
                'farmers on Grenden are aware of their position in the dependency chain: '
                'they grow the food that feeds the engineers who maintain the network that '
                'connects the cluster. If the farmers stop, the engineers stop. If the '
                'engineers stop, the cluster stops.\n\n'
                'The farmers do not think about this often. They grow food. The chain of '
                'consequences that extends from their fields to the functioning of a '
                'civilisation is too abstract to carry every day, and the farmers are '
                'practical people who find abstraction less useful than knowing when to '
                'harvest.'
            ),
            population=800_000_000,
        ),
    ],
    short_description='The backbone -- five billion people maintaining the network infrastructure that connects every mind in the cluster, in a system nobody visits on purpose and everybody depends on.',
    long_description=(
        'Eltanin is the system the Polaris cluster cannot function without and that '
        'nobody would choose to visit. The planet Condaren hosts the central '
        'processing infrastructure of the cluster-wide neural network -- relay '
        'stations, signal processors, routing systems, data centres. The Lattice '
        'orbits above -- a constellation of relay stations carrying every '
        'telepresence connection, every pilot link, every Core governance feed, '
        'every civilian communication. The network is the cluster\'s nervous system. '
        'Eltanin is the spine.\n\n'
        'The work is monitoring, maintenance, and incremental upgrades. The culture '
        'is precise, methodical, and allergic to the dramatic. The rest of the '
        'cluster deals in the extraordinary. Eltanin deals in latency measurements, '
        'packet routing, and the firmware updates that prevent the extraordinary '
        'from collapsing. The unofficial motto on mugs in every control room: the '
        'network works because we do.\n\n'
        'The redundancy is extreme -- every relay has a backup, every path has '
        'alternatives, every critical system has millisecond failover. The '
        'redundancy is why the network has never experienced a cluster-wide failure. '
        'The engineers who maintain the redundancy are why the redundancy works. '
        'Morsten archives every transaction and communication the cluster has ever '
        'made, including the neural logs of every Core that has ever governed. The '
        'Switchboard trains the engineers who will maintain infrastructure the '
        'civilisation cannot survive without.\n\n'
        'Five billion people in a system that is boring, essential, and the single '
        'point that a hostile force would need to destroy to bring the Polaris '
        'cluster to its knees. The military defense of Eltanin is accordingly the '
        'second-heaviest in the cluster after the gateway, because the enemy that '
        'understands the network understands that this is where the network lives.'
    ),
    cluster=StarClusters.POLARIS,
)


RASTABAN = System(
    name='Rastaban',
    star='Yellow supergiant (G2Ib), approximately 1,000 times Sol luminosity -- a warm, golden star that makes the most prosperous system in the cluster look as good as it thinks it is',
    population=18_000_000_000,
    distance_to_sol=380.0,
    stellar_objects=[
        StellarObject(
            name='Callidren',
            short_description='The showcase -- ten billion people living proof that neural integration enhances rather than diminishes, in a system where the interfaces are precise, the connections are clean, and the wealth makes it all look effortless.',
            long_description=(
                'Callidren is the Polaris cluster at its best -- the system where the '
                'technology works the way the promotional material describes and the '
                'quality of life justifies the philosophy. The planet is the most populous '
                'in the cluster, the most prosperous, and the place where premium neural '
                'interfaces are designed and manufactured. The interfaces produced on '
                'Callidren are the best in the galaxy: precise, low-latency, with sensory '
                'fidelity that makes the telepresence experience indistinguishable from '
                'physical presence for the operator.\n\n'
                'The population of Callidren uses these interfaces and the difference is '
                'visible in everything. A surgeon on Callidren working through a premium '
                'interface operates with a precision that the crude shared rigs on poorer '
                'worlds cannot match -- the feedback is sharper, the control is finer, '
                'the lag is imperceptible. An engineer on Callidren designs in VR '
                'environments that are rendered with a fidelity that the budget systems '
                'elsewhere produce only as approximation. The quality of the interface '
                'determines the quality of the work, and Callidren\'s interfaces are the '
                'standard that everything else in the cluster is measured against.\n\n'
                'The wealth divide is the interface. On Callidren, the private cradles '
                'have medical monitoring, ergonomic support, and the premium hardware that '
                'makes every session productive and comfortable. The shared rigs in '
                'the commercial centres are good by cluster standards -- better than '
                'anything available on Navi or the outer systems. The gap between '
                'Callidren\'s shared rigs and the premium private cradles is the same gap '
                'that exists everywhere in the cluster, expressed here with the clarity '
                'that prosperity provides: the wealthy work in higher resolution than '
                'the poor.\n\n'
                'The disconnect hours on Callidren are the cluster\'s most lavish -- the '
                'restaurants, the entertainment districts, the social spaces designed for '
                'the compressed intensity of physical presence. The population lives well '
                'in both modes: productive and precise in the interface, comfortable and '
                'connected during the disconnect. Callidren is the argument that neural '
                'integration makes life better. MERIT\'s counter-argument is that it makes '
                'life better for the people who can afford the version that works.'
            ),
            population=10_000_000_000,
        ),
        StellarObject(
            name='Helvarden',
            short_description='The manufacturing world -- where the premium interfaces are assembled in facilities that are themselves showcases of what telepresence manufacturing can achieve.',
            long_description=(
                'Helvarden is the system\'s manufacturing centre -- the world where the '
                'premium neural interfaces that define Callidren\'s quality of life are '
                'designed and assembled. The manufacturing is a showcase of Polaran '
                'industry: the precision components are assembled by telepresence operators '
                'working through the same premium interfaces the factories produce, in a '
                'recursive loop where the quality of the product determines the quality of '
                'the production.\n\n'
                'The factories on Helvarden are among the most technically sophisticated '
                'manufacturing facilities in the galaxy. The operators sit in cradles on '
                'the factory floors -- rows of connected workers, bodies still, minds '
                'controlling robotic assembly systems at scales from the macro to the '
                'microscopic. A single operator can switch between assembling a cradle\'s '
                'structural frame and placing the neural contact points that are measured '
                'in micrometres, the interface scaling the operator\'s perception to match '
                'the task. The work requires training, precision, and the premium hardware '
                'that Helvarden produces for itself before exporting to the rest of the '
                'cluster.\n\n'
                'The quality control is obsessive. A neural interface that malfunctions is '
                'not a broken appliance -- it is a device connected to a person\'s nervous '
                'system, and a malfunction can produce sensory distortion, pain, or the '
                'cognitive disruption that the industry calls feedback cascade and that '
                'the medical profession calls brain damage. The testing facilities on '
                'Helvarden reject units at rates that the accountants find expensive and '
                'that the engineers find necessary. The rejected units are destroyed, not '
                'recycled. A substandard interface that enters the market through secondary '
                'channels is a lawsuit, a medical emergency, and a reputational '
                'catastrophe. Helvarden does not permit any of the three.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Showcase',
            short_description='An orbital station where the latest interface technology is demonstrated to buyers from across the galaxy -- the annual exhibition that every faction attends and MERIT officially ignores.',
            long_description=(
                'The Showcase is Rastaban\'s orbital exhibition station -- the venue where '
                'the cluster\'s premium interface manufacturers display their latest '
                'products to buyers from across the galaxy. The annual exhibition draws '
                'delegations from every faction: Hyadean buyers evaluating interfaces for '
                'prosthetic integration, Antarian buyers assessing neural hardware for '
                'drug-delivery optimisation, Pleiadian buyers examining the telepresence '
                'systems that could complement their gene-splicing operations. MERIT does '
                'not officially attend. MERIT\'s intelligence services are present in '
                'sufficient numbers that the exhibition\'s security staff have stopped '
                'pretending not to notice.\n\n'
                'The demonstrations are immersive -- visitors are offered trial connections '
                'with the latest hardware, experiencing the difference between their '
                'faction\'s interface technology and Polaris\'s best. The experience is '
                'the most effective sales pitch available: a buyer who has felt the '
                'precision of a premium Polaran interface does not need to be told that '
                'it is better than what they have. They felt the difference. The orders '
                'follow.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Restell',
            short_description='A world dedicated to the physical health that interface use demands -- rehabilitation, exercise, and the medical care that keeps the bodies functional while the minds work elsewhere.',
            long_description=(
                'Restell is the system\'s answer to the physical cost of the telepresence '
                'economy. Extended interface use takes a toll on the body -- muscle '
                'atrophy despite the cradle\'s stimulation systems, joint degradation from '
                'immobility, cardiovascular deconditioning from the reduced physical '
                'activity that a life lived largely in a chair produces. The cradle systems '
                'mitigate these effects. They do not eliminate them. Restell exists '
                'because the bodies need maintenance that the cradles cannot provide.\n\n'
                'The planet hosts rehabilitation centres, fitness facilities, and the '
                'medical institutions that specialise in the specific health problems that '
                'interface-dependent populations develop. The staff are physicians and '
                'therapists who work with their hands on their patients\' bodies -- one of '
                'the few medical specialties in the cluster that is practised in person '
                'rather than via telepresence, because the work is physical rehabilitation '
                'and the patient\'s physical body is the point.\n\n'
                'The wealthy visit Restell on regular schedules -- maintenance cycles '
                'that keep their bodies in condition for the decades of interface use they '
                'plan. The poor visit Restell when the degradation has become a problem, '
                'which is later than it should be and more expensive to address than '
                'prevention would have been. The wealth divide expresses itself in bodies: '
                'the wealthy are physically fit despite their interface hours. The poor '
                'carry the signs of sessions too long in rigs too cheap, and the '
                'rehabilitation they receive on Restell is treatment for a condition that '
                'better hardware would have prevented.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Ostrand',
            short_description='A gas giant with fuel processing at scale -- the traffic that Rastaban\'s manufacturing and exhibition generate is the heaviest commercial volume in the cluster.',
            long_description=(
                'Ostrand is the system\'s gas giant -- fuel processing on its moons '
                'supporting the heaviest commercial traffic in the cluster. Rastaban\'s '
                'manufacturing output and the exhibition traffic generate a volume of '
                'freight and passenger movement that exceeds any other system except the '
                'gateway. The fuel operations are large, efficient, and operated via '
                'telepresence with the premium interfaces that the system produces -- the '
                'fuel workers experience what may be the galaxy\'s most comfortable '
                'industrial telepresence, piloting skimmers through a gas giant\'s '
                'atmosphere from cradles that are the best hardware the cluster manufactures.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Dunfeld',
            short_description='An agricultural world feeding the showcase -- the largest farming operation in the cluster, because eighteen billion people require food at a scale that telepresence cannot replace.',
            long_description=(
                'Dunfeld is the system\'s agricultural world -- the largest farming '
                'operation in the Polaris cluster, scaled for a population of eighteen '
                'billion. The farming is conventional and physical, as it is across the '
                'cluster -- the crops require hands, the livestock require handling, and '
                'the scale of Rastaban\'s food demand means that Dunfeld\'s farming '
                'population is the largest single community of physical workers in the '
                'cluster.\n\n'
                'The farmers on Dunfeld carry the same quiet awareness as Tilderen\'s '
                'farmers on the gateway -- they are the people who keep the bodies alive '
                'while the minds work elsewhere. The farmers are disconnected by default, '
                'physical by profession, and essential in a way that the telepresence '
                'economy cannot replicate. The food goes to Callidren\'s restaurants, to '
                'the cradle-side feeding systems that sustain the connected workers, and '
                'to the Procession\'s supply tenders at Kochab. The farmers feed the '
                'showcase. The showcase does not think about the farmers often.'
            ),
            population=2_000_000_000,
        ),
    ],
    short_description='The showcase -- eighteen billion people in the system where neural integration works the way the promotional material describes, where the interfaces are premium and the wealth makes it look effortless.',
    long_description=(
        'Rastaban is the Polaris cluster at its best. Eighteen billion people in the '
        'most prosperous system, where premium neural interfaces are designed and '
        'manufactured, and where the quality of life justifies the philosophy. '
        'Callidren\'s population works through interfaces that produce precision and '
        'fidelity the rest of the cluster measures itself against. The surgeons are '
        'more precise. The engineers design in higher resolution. The quality of the '
        'interface determines the quality of the work, and Rastaban\'s interfaces are '
        'the standard.\n\n'
        'Helvarden manufactures the premium hardware in factories that are themselves '
        'showcases -- operators in cradles controlling robotic assembly from macro to '
        'microscopic scale, the product determining the quality of its own production. '
        'Quality control is obsessive because a malfunctioning interface is not a '
        'broken appliance but a device connected to a nervous system. The Showcase '
        'hosts the annual exhibition where every faction\'s buyers experience the '
        'difference between their technology and Polaris\'s best.\n\n'
        'Restwell addresses the physical cost -- the muscle atrophy, joint '
        'degradation, and cardiovascular deconditioning that interface-dependent life '
        'produces. The wealthy visit on preventive schedules. The poor visit when the '
        'degradation is already a problem. The wealth divide expresses itself in '
        'bodies: the wealthy are physically fit despite their interface hours. The '
        'poor carry the signs of sessions too long in rigs too cheap.\n\n'
        'The disconnect hours on Callidren are the cluster\'s most lavish. Rastaban '
        'is the argument that neural integration makes life better. MERIT\'s counter-'
        'argument is that it makes life better for the people who can afford the '
        'version that works. Both arguments contain the truth they prefer.'
    ),
    cluster=StarClusters.POLARIS,
)


THUBAN = System(
    name='Thuban',
    star='White giant (A0III), approximately 300 times Sol luminosity -- a pale, clinical star casting flat white light over a system where the bodies are stored and the people are somewhere else',
    population=8_000_000_000,
    distance_to_sol=300.0,
    stellar_objects=[
        StellarObject(
            name='Holst',
            short_description='The body houses -- five billion people in a city of interface cradles, the largest concentration of telepresence workers in the cluster, where entire districts exist to store the bodies of people whose minds are working three systems away.',
            long_description=(
                'Holst is the system the rest of the cluster tries not to think about '
                'too carefully. The planet is the largest concentration of telepresence '
                'workers in the Polaris cluster -- not because the work is here but '
                'because the bodies are. Holst\'s economy is bodies: housing them, '
                'maintaining them, feeding them, exercising them, and keeping them alive '
                'while the minds that own them operate equipment, perform surgeries, and '
                'build structures across the cluster.\n\n'
                'The body houses are Holst\'s defining architecture. Entire districts '
                'are given over to the cradle facilities -- buildings designed from the '
                'foundation as storage for human bodies in interface rigs. The layouts are '
                'efficient: rows of cradles in climate-controlled rooms, each cradle '
                'maintaining a single body with hydration, nutrition, waste processing, '
                'temperature regulation, and the muscle stimulation that prevents the '
                'worst of the atrophy that immobility produces. The rooms are quiet. The '
                'bodies are still. The only sound is the hum of the cradle systems and '
                'the occasional shift of a body responding to a dream or a neural '
                'feedback spike from whatever the mind is doing elsewhere.\n\n'
                'The economics are straightforward. Holst is cheap. The cost of living '
                'is the lowest in the cluster because the planet offers nothing except '
                'the cradle facilities and the support infrastructure they require. A '
                'worker who cannot afford a private cradle on Callidren or a shared rig '
                'on Ondaren can afford a body house on Holst. The worker\'s mind '
                'connects to the same network, accesses the same jobs, earns the same '
                'wages -- but the body is stored in a cheaper facility, in a cheaper '
                'system, maintained by cheaper hardware. The interface rigs in the body '
                'houses are functional but not premium. The lag is slightly higher. The '
                'sensory fidelity is slightly lower. The difference is measurable and the '
                'workers feel it -- a surgeon on Holst working through a body-house rig '
                'is slightly less precise than the same surgeon on Callidren, and the '
                'slight difference compounds over a career.\n\n'
                'The disconnect hours on Holst are the cluster\'s bleakest. The workers '
                'unplug into a city that was not designed for living -- the infrastructure '
                'is cradle facilities, feeding stations, exercise centres, and the transit '
                'systems that move bodies between them. The restaurants are functional. '
                'The entertainment is basic. The social spaces exist because the workers '
                'need them, not because anyone invested in making them pleasant. The '
                'workers describe Holst as the place where your body waits for you. '
                'The description is affectionate in the way that people are affectionate '
                'about things that are not good but are theirs.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='The Wards',
            short_description='The medical facilities that keep the body-house population functional -- treating the chronic conditions that cheap cradles and long sessions produce.',
            long_description=(
                'The Wards are Holst\'s medical infrastructure -- hospitals and clinics '
                'dedicated to the health problems that the body-house population develops. '
                'The conditions are predictable: the muscle atrophy that cheap cradles '
                'manage less effectively than premium ones, the joint degradation from '
                'years of immobility, the pressure sores that develop when the cradle\'s '
                'positional adjustment systems are not maintained frequently enough, and '
                'the neurological effects of extended interface use on hardware that is '
                'functional but not quite good enough.\n\n'
                'The neurological effects are the Wards\' speciality. The cheap rigs '
                'produce a condition the physicians call interface drift -- a gradual '
                'degradation of the boundary between the operator\'s sense of their own '
                'body and the equipment they control remotely. A worker with interface '
                'drift disconnects from the rig and feels, for minutes or hours, that '
                'their hands are the wrong size, that their legs are in the wrong '
                'position, that their body is not the shape they expect. The condition is '
                'temporary in the early stages and manageable with treatment. In the '
                'advanced stages -- the stages that workers reach when they cannot afford '
                'to take time off from the rigs -- the drift becomes permanent, and the '
                'worker\'s sense of their own body does not fully return after '
                'disconnecting. The Wards treat these workers. The treatment is rest, '
                'physical therapy, and time away from the rigs. The workers cannot afford '
                'the time. The Wards know this. The treatment is provided anyway, because '
                'the alternative is a worker whose body has become unfamiliar to the mind '
                'that lives in it.'
            ),
            population=0,
        ),
        StellarObject(
            name='Lintrel',
            short_description='A second world where the body houses serve the cluster\'s industrial workforce -- the miners, the construction workers, the heavy-labour telepresence operators whose rigs take the hardest toll.',
            long_description=(
                'Lintrel is Thuban\'s second inhabited world -- colder, less developed, '
                'and home to the body houses that serve the cluster\'s industrial '
                'telepresence workforce. The operators on Lintrel control mining rigs, '
                'construction equipment, and the heavy industrial machinery that the '
                'cluster\'s economy requires. The work is physically demanding on the '
                'interface -- the neural feedback from operating heavy equipment produces '
                'strain that the operators\' bodies absorb even though the bodies are not '
                'performing the work.\n\n'
                'The phenomenon is called sympathetic load -- the neural connection to '
                'heavy equipment causes the operator\'s muscles to tense in sympathy with '
                'the effort the remote machinery exerts. An operator controlling a mining '
                'drill feels the resistance in their own arms. An operator lifting a '
                'structural beam feels the weight in their own back. The load is not real '
                '-- the body is in a cradle -- but the neural system does not know this, '
                'and the chronic tension produces injuries that the physicians classify as '
                'occupational despite the fact that the occupation is performed while '
                'lying still.\n\n'
                'The body houses on Lintrel are built heavier than Holst\'s -- the '
                'cradles reinforced for the sympathetic load, the muscle stimulation '
                'systems calibrated for workers whose bodies are under chronic tension, '
                'and the medical facilities integrated into the body houses rather than '
                'separate. The workers on Lintrel describe the experience of their work '
                'in physical terms -- the ache in the shoulders after a shift operating '
                'the drill, the stiffness in the back after moving structural components '
                '-- and visitors are surprised to learn that the aches are real and the '
                'work is remote.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='The Commissary',
            short_description='An orbital station dedicated to the logistics of feeding a planet of stationary bodies -- the most efficient food distribution system in the galaxy, because the recipients do not move.',
            long_description=(
                'The Commissary is an orbital facility that coordinates the food '
                'distribution for Holst\'s body-house population. Feeding five billion '
                'people who are mostly lying in cradles is a logistical challenge with a '
                'simplifying condition: the recipients do not move. The Commissary '
                'coordinates the automated delivery systems that supply nutrition directly '
                'to the cradles during sessions and the meal services that feed the workers '
                'during disconnect hours.\n\n'
                'The cradle nutrition is functional -- calibrated nutrient solutions '
                'delivered intravenously or through oral feeds during long sessions. The '
                'disconnect meals are real food, served in the body houses\' communal '
                'dining facilities, and the Commissary\'s logistical achievement is '
                'ensuring that both systems operate at the scale Holst requires. The '
                'workers joke that the cradle nutrition tastes like nothing and the '
                'disconnect meals taste like not-quite-enough. The Commissary\'s staff '
                'consider both assessments accurate and neither actionable at the '
                'budget they operate on.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Brevary',
            short_description='A gas giant with fuel processing -- operated, like everything in Thuban, via telepresence from cradles on Holst.',
            long_description=(
                'Brevary is the system\'s gas giant -- fuel processing on its moons, '
                'operated via telepresence by workers in Holst\'s body houses. The fuel '
                'workers pilot the skimmers from the same cradle facilities that house '
                'every other category of worker. The body next to the fuel skimmer pilot '
                'in the cradle row might be a surgeon operating on Schedar, or a miner '
                'drilling on Grumium, or another fuel worker piloting a skimmer in a '
                'different system entirely. The bodies are side by side. The minds are '
                'light-years apart.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Paget',
            short_description='An agricultural world feeding the body houses -- the farms that grow the food that becomes the cradle nutrition and the disconnect meals for five billion stationary bodies.',
            long_description=(
                'Paget is the system\'s agricultural world -- producing the food that '
                'Holst\'s body houses consume. The scale is substantial -- five billion '
                'bodies require feeding regardless of where the minds are working -- and '
                'the farming is conventional. The farmers on Paget produce the raw '
                'ingredients that the Commissary processes into cradle nutrition and '
                'disconnect meals.\n\n'
                'The farmers are the system\'s most physically present population and the '
                'population least likely to visit Holst. The body houses are an '
                'abstraction to the farmers -- they grow the food, the food goes to the '
                'Commissary, and the Commissary feeds the bodies. The farmers do not '
                'think about the rows of still bodies in the cradle rooms being sustained '
                'by the crops they planted. The abstraction is preferable to the image.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The body houses -- eight billion people in the system where the cluster stores its workforce, bodies maintained in cradles while minds work across the galaxy.',
    long_description=(
        'Thuban is where the Polaris cluster keeps its bodies. Eight billion people '
        'in a system whose economy is storage -- housing, maintaining, feeding, and '
        'exercising the physical forms of workers whose minds are operating equipment '
        'across the cluster through the neural network. The body houses are '
        'Holst\'s defining architecture: rows of cradles in climate-controlled '
        'rooms, each maintaining a single body with hydration, nutrition, waste '
        'processing, and muscle stimulation. The rooms are quiet. The bodies are '
        'still.\n\n'
        'The economics are clear: Holst is cheap. A worker who cannot afford a '
        'private cradle on Callidren can afford a body house here. The mind connects '
        'to the same network, earns the same wages -- but the hardware is functional '
        'rather than premium. The lag is slightly higher. The precision slightly '
        'lower. The difference compounds over a career.\n\n'
        'The Wards treat the conditions cheap cradles produce: interface drift, '
        'where the boundary between the operator\'s body and the remote equipment '
        'degrades until the worker\'s sense of their own body does not fully return '
        'after disconnecting. Lintrel houses the industrial workforce -- operators '
        'whose bodies absorb sympathetic load from heavy equipment, developing real '
        'injuries from work performed while lying still.\n\n'
        'The disconnect hours are the cluster\'s bleakest -- a city not designed for '
        'living, functional restaurants, basic entertainment, transit systems that '
        'move bodies between cradle facilities. The workers describe Holst as the '
        'place where your body waits for you. The description is affectionate in the '
        'way that people are affectionate about things that are not good but are '
        'theirs.'
    ),
    cluster=StarClusters.POLARIS,
)


DUBHE = System(
    name='Dubhe',
    star='Orange giant binary (K0III + F0V), approximately 300 times combined Sol luminosity -- the warm primary and its bright companion casting mixed light over the system where Polaris sells its mind to the rest of the galaxy',
    population=7_000_000_000,
    distance_to_sol=124.0,
    stellar_objects=[
        StellarObject(
            name='Miravel',
            short_description='The cluster\'s shopfront -- four billion people adapting Polaran neural technology for buyers who want the interfaces without the civilisation that produced them.',
            long_description=(
                'Miravel is where Polaris sells itself. The planet is the cluster\'s trade '
                'hub -- the system where neural interface technology is adapted, repackaged, '
                'and exported to every faction willing to buy. The buyers are varied: the '
                'Hyades buys interface components that improve prosthetic-neural '
                'integration. The Antares cluster buys the telepresence systems that let '
                'their drug-calibrated workforce operate equipment without the physical '
                'side effects of the performance enhancers. The Pleiades buys neural '
                'monitoring hardware for their gene-splicing procedures. Canopus buys the '
                'cognitive preservation technology that improves reanimation quality. MERIT '
                'absorbs Polaran interface tech through grey markets it officially condemns '
                'and unofficially depends on.\n\n'
                'The export trade is translation. The interfaces that work in the Polaris '
                'cluster -- designed for a population with surgical ports and a lifetime of '
                'network familiarity -- do not work directly for buyers who have never '
                'connected. The engineers on Miravel specialise in the adaptation: stripping '
                'the interfaces to the functions the buyer needs, simplifying the neural '
                'protocols for populations that lack the cluster\'s network infrastructure, '
                'and packaging the result as a product that delivers enough of the Polaran '
                'capability to justify the price without requiring the Polaran commitment.\n\n'
                'The trading houses on Miravel have relationships with every faction and the '
                'discretion that inter-faction commerce requires. A Hyadean delegation '
                'negotiating interface contracts sits in the same district as a Canopan '
                'delegation purchasing cognitive hardware, and neither acknowledges the '
                'other because acknowledging the other would mean acknowledging that their '
                'faction\'s technology depends on imports from the same source their '
                'propaganda claims to oppose.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Brask',
            short_description='The export manufacturing world -- where Polaran interfaces are stripped down, simplified, and rebuilt for bodies and minds that have never been connected.',
            long_description=(
                'Brask is the system\'s manufacturing centre -- the world where the export-'
                'grade neural interfaces are produced. The factories take the premium '
                'designs from Rastaban\'s Helvarden and reverse-engineer them for non-'
                'Polaran use: removing the features that require surgical ports, reducing '
                'the bandwidth to levels that unaugmented neural systems can handle, and '
                'adding the safety limiters that prevent the feedback cascades the premium '
                'hardware is designed to manage through the operator\'s training.\n\n'
                'The manufacturing is conducted via telepresence -- operators in cradles '
                'assembling the export hardware with the same precision the domestic '
                'factories on Helvarden use. The irony is noted and accepted: the workers '
                'building interfaces for populations that have never connected are '
                'themselves deeply connected, assembling the products through the very '
                'technology they are simplifying for export.\n\n'
                'The quality control is different from Helvarden\'s. The export interfaces '
                'are designed to lower standards -- not because the engineers are careless '
                'but because the buyers\' neural systems cannot handle the full bandwidth '
                'and the interfaces must be limited to prevent damage. The engineers who '
                'work on export products describe the job as building deliberately worse '
                'versions of things they know how to build properly. The description is '
                'accurate and the engineers accept it, because the alternative is selling '
                'full-bandwidth hardware to buyers whose brains would be damaged by the '
                'experience.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='The Forum',
            short_description='The orbital trading station -- where buyers from every faction negotiate for Polaran technology on a trading floor where the demonstrations are the most persuasive argument.',
            long_description=(
                'The Forum is Dubhe\'s primary orbital station and the largest neural '
                'technology trading installation in the galaxy. The station is the Polaris '
                'cluster\'s equivalent of the Hyades\' Emporium or the Pleiades\' Bourse -- '
                'a neutral trading floor where buyers from every faction browse, negotiate, '
                'and purchase.\n\n'
                'The demonstrations are the Forum\'s selling point. Buyers are offered '
                'trial connections with export-grade hardware tailored for their faction\'s '
                'physiology and modification level. A Hyadean buyer with prosthetic limbs '
                'can experience the neural integration that makes the prosthetics respond '
                'to thought rather than muscle signal. A Pleiadian buyer with sensory '
                'splicing can feel the interface extend their already-modified perception '
                'into data realms the splicing alone cannot reach. The experience sells '
                'the product because the product is an experience -- a buyer who has felt '
                'what the interface does cannot unfeel it, and the purchase follows.\n\n'
                'The security on the Forum is focused on intellectual property rather '
                'than physical threat. The export interfaces contain proprietary Polaran '
                'engineering that the other factions would prefer to reverse-engineer '
                'rather than purchase. The counter-espionage staff on the Forum are among '
                'the best in the cluster, and the trading floor is the most closely '
                'monitored space in the outer systems.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Whittal',
            short_description='A world where the trade hub\'s diverse population lives -- Polaran residents alongside permanent delegations from every faction, in a city designed for people with different levels of neural integration.',
            long_description=(
                'Whittal is Dubhe\'s residential world -- a temperate planet where the '
                'system\'s mixed population lives. The trade hub attracts permanent '
                'residents from every faction: Hyadean trade representatives with '
                'prosthetic limbs, Antarian commercial agents on their performance '
                'regimens, Pleiadian buyers with the visible splicing that marks their '
                'origin, and the Canopan delegations whose senior members are old enough '
                'that the reanimation is visible in their skin tone.\n\n'
                'The city on Whittal is designed for coexistence -- public spaces that '
                'accommodate people with different neural integration levels, from the '
                'fully connected Polaran residents who spend their offline hours here to '
                'the baseline MERIT visitors who carry no interfaces at all. The '
                'restaurants serve food for every faction\'s dietary requirements. The '
                'medical facilities handle the health concerns of five different '
                'modification cultures. The social dynamics are complex and the residents '
                'navigate them with the fluency that comes from living in a place where '
                'every person you meet may be a fundamentally different kind of human.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Corsin',
            short_description='A gas giant with fuel processing for the inter-faction traffic -- the heaviest mix of foreign vessels in the cluster.',
            long_description=(
                'Corsin is the system\'s gas giant -- fuel processing on its moons '
                'supporting the heavy inter-faction traffic that the trade hub generates. '
                'The fuel operations serve the most diverse fleet in the cluster: Polaran '
                'ships with their minimal-signature hulls alongside Hyadean freighters '
                'built heavy and visible, Antarian vessels running hot from their crews\' '
                'enhanced metabolisms, and the occasional Pleiadian ship whose biological '
                'hull modifications make the fuel workers uneasy. The fuel is fuel. The '
                'ships it goes into are a catalogue of every way humanity has decided to '
                'be different.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Gable',
            short_description='An agricultural world feeding the trade hub\'s mixed population -- multiple cuisine tracks for buyers from factions whose dietary needs reflect their modification cultures.',
            long_description=(
                'Gable is the system\'s agricultural world -- producing food for the '
                'trade hub\'s diverse population. The farming is more varied than any other '
                'system in the cluster: standard Polaran crops alongside the modified '
                'produce that the Pleiadian delegations require, the nutrient-dense food '
                'that the Antarian visitors\' enhanced metabolisms demand, and the baseline '
                'terrestrial crops that the MERIT visitors expect. The farming is '
                'segregated by dietary compatibility, similar to the Pleiades\' approach on '
                'Celaeno but driven by inter-faction variety rather than intra-strain '
                'divergence.\n\n'
                'The farmers on Gable are the system\'s most practically multicultural '
                'population -- people who understand, at the level of soil chemistry and '
                'crop management, what the differences between the factions mean for the '
                'body. The farmers grow what each faction needs and do not judge the needs. '
                'The food is the food. The modifications that require it are not the '
                'farmers\' concern.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The cluster\'s shopfront -- seven billion people selling Polaran neural technology to every faction, on a trading floor where the demonstrations are the most persuasive argument.',
    long_description=(
        'Dubhe is where Polaris sells its mind to the rest of the galaxy. The '
        'system is the cluster\'s trade hub -- neural interface technology adapted '
        'and exported to every faction willing to buy. The Hyades buys prosthetic-'
        'neural integration. Antares buys telepresence systems. The Pleiades buys '
        'neural monitoring for gene-splicing. Canopus buys cognitive preservation '
        'for reanimation. MERIT absorbs the tech through grey markets it officially '
        'condemns and unofficially depends on.\n\n'
        'The export trade is translation -- stripping the interfaces to what the '
        'buyer needs, simplifying the neural protocols for populations without the '
        'cluster\'s network infrastructure, adding safety limiters to prevent the '
        'feedback cascades that untrained operators cannot manage. Brask manufactures '
        'the export hardware -- engineers building deliberately worse versions of '
        'things they know how to build properly, because the buyers\' brains would '
        'be damaged by the full-bandwidth experience.\n\n'
        'The Forum hosts the demonstrations that sell the product. Buyers try '
        'export-grade hardware tailored for their physiology. A buyer who has felt '
        'what the interface does cannot unfeel it, and the purchase follows. The '
        'security is intellectual property rather than physical -- the counter-'
        'espionage staff are among the cluster\'s best.\n\n'
        'Whittal houses the mixed population -- permanent delegations from every '
        'faction in a city designed for people with different levels of neural '
        'integration and different kinds of body. Seven billion people selling the '
        'most advanced neural technology in the galaxy to buyers who want Polaran '
        'capability without Polaran commitment.'
    ),
    cluster=StarClusters.POLARIS,
)


SCHEDAR = System(
    name='Schedar',
    star='Orange giant (K0IIIa), approximately 680 times Sol luminosity -- a steady, reliable star for the system where steady, reliable hands operate on patients they have never been in the same room with',
    population=6_000_000_000,
    distance_to_sol=230.0,
    stellar_objects=[
        StellarObject(
            name='Colmaris',
            short_description='The cluster\'s hospital -- three billion people in the system where the surgeons sit in cradles and their hands are robots on other worlds, performing operations with a precision no physical hand can match.',
            long_description=(
                'Colmaris is the Polaris cluster\'s medical capital and the place that '
                'demonstrates the practical case for neural integration more convincingly '
                'than any propaganda. The planet hosts the largest concentration of '
                'telepresence medical professionals in the galaxy -- surgeons, diagnosticians, '
                'trauma specialists, and the support staff who keep the medical '
                'infrastructure running.\n\n'
                'The surgeons on Colmaris operate on patients they have never met in '
                'person. A surgeon sits in an interface cradle in a clinic on Colmaris, '
                'connects through the neural network, and their hands become robotic '
                'surgical instruments on a patient in another system. The instruments '
                'range from human-scale manipulators to micro-scale tools that operate at '
                'the cellular level -- scales that no physical human hand could work at, '
                'controlled with a precision that the neural interface makes feel natural. '
                'The surgeon\'s perception is scaled to match the tools: when operating at '
                'micro-scale, the surgeon perceives the surgical field as if they were the '
                'size of the instruments, the patient\'s tissue becoming a landscape they '
                'navigate rather than a surface they cut.\n\n'
                'The medical outcomes are the argument. Polaran telepresence surgery '
                'produces results that conventional surgery cannot match -- the precision '
                'of the instruments, the scaling of the operator\'s perception, and the '
                'neural interface\'s ability to filter out the hand tremor that every '
                'physical surgeon carries. The survival rates, the recovery times, the '
                'complication rates -- every metric favours telepresence surgery performed '
                'by a trained operator through a premium interface. The metrics are why '
                'every faction buys Polaran medical technology even when they condemn '
                'Polaran philosophy.\n\n'
                'The surgeons work shifts in the cradles and disconnect into a city that '
                'caters to their particular needs. The disconnect hours on Colmaris are '
                'structured around the physical recovery from high-concentration interface '
                'work -- the micro-scale operations demand intense neural focus that '
                'leaves the operator mentally exhausted in ways that conventional work '
                'does not. The surgeons describe the fatigue as specific: the body is '
                'rested but the mind has spent hours perceiving reality at a scale the '
                'brain was not evolved for, and the recalibration to normal perception '
                'after a micro-scale session takes time. The surgeons sit in the parks '
                'during disconnect hours and stare at trees because the trees are the '
                'right size and the rightness is restorative.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Routing',
            short_description='The orbital hub where the telepresence connections to patients across the cluster are routed -- the switching station that determines which surgeon\'s hands arrive at which patient\'s bedside.',
            long_description=(
                'The Routing is the orbital facility above Colmaris that handles the '
                'telepresence routing for the system\'s medical operations. The station is '
                'a switching hub -- the facility that connects a surgeon in a cradle on '
                'Colmaris to the surgical robot at a patient\'s location, managing the '
                'connection quality, the latency, and the bandwidth that the operation '
                'requires.\n\n'
                'The routing is the critical function. A surgeon performing micro-scale '
                'work requires a connection with latency measured in single-digit '
                'milliseconds -- any higher and the surgeon\'s movements and the '
                'instruments\' responses fall out of sync, producing errors at scales '
                'where errors are measured in damaged cells. The Routing\'s operators '
                'manage the connection quality in real time, rerouting through the '
                'Lattice at Eltanin when a primary path degrades, maintaining the latency '
                'standard that the surgeons\' work demands. A routing failure during an '
                'operation is not a dropped call. It is a surgeon whose hands have stopped '
                'responding with a patient open on the table.\n\n'
                'The Routing handles the scheduling that the cluster\'s medical demand '
                'requires -- matching surgeons to patients across the cluster based on '
                'speciality, availability, and the connection quality available to the '
                'patient\'s location. A patient on Rastaban receives a premium connection. '
                'A patient on Navi receives whatever the network can provide at that '
                'distance. The quality of care correlates with the quality of connection, '
                'which correlates with the patient\'s location, which correlates with the '
                'patient\'s wealth. The Routing\'s operators are aware of this. The Routing\'s '
                'operators route the connections they are given.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Pembrook',
            short_description='The training world -- where the next generation of telepresence surgeons learn to operate at scales their eyes cannot see and to trust hands that are not their own.',
            long_description=(
                'Pembrook is Schedar\'s training world -- a planet dedicated to producing '
                'the telepresence medical professionals the cluster depends on. The '
                'training is long, demanding, and unlike any medical education in the '
                'galaxy. The trainees must learn to operate through the interface -- to '
                'trust the robot\'s hands as their own, to perceive at scales the brain '
                'was not evolved for, and to maintain surgical focus through a neural '
                'connection that interposes technology between the surgeon and the '
                'patient in ways that conventional training does not prepare for.\n\n'
                'The hardest transition is scale. A trainee learning micro-scale surgery '
                'must accept that their perception is being artificially scaled -- that '
                'the landscape they are navigating is a human cell, that the instruments '
                'they are wielding are smaller than the eye can see, and that the '
                'movements they make are being translated across orders of magnitude. The '
                'trainees who succeed describe the moment the scaling becomes natural as '
                'the point where the interface disappears -- where they stop thinking '
                'about the technology between them and the patient and simply operate. '
                'The trainees who do not reach this point wash out. The washout rate is '
                'high. The standard is absolute because the consequence of a surgeon who '
                'has not achieved the transition is a surgeon who is thinking about the '
                'interface when they should be thinking about the patient.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Locke',
            short_description='A world housing the engineering services -- telepresence engineers who design and build across the cluster with the same scaled precision the surgeons use on tissue.',
            long_description=(
                'Locke is Schedar\'s engineering counterpart -- a world where the skilled '
                'telepresence engineers who design and build infrastructure across the '
                'cluster are based. The engineering services use the same interface '
                'technology as the surgeons -- scaled perception, robotic manipulators, '
                'the neural connection that makes the remote tools feel like the '
                'operator\'s own hands -- applied to construction, maintenance, and the '
                'technical work the cluster\'s systems require.\n\n'
                'An engineer on Locke can assemble micro-scale circuitry on Eltanin\'s '
                'relay stations in the morning, switch to macro-scale structural work on '
                'a Kochab orbital facility in the afternoon, and perform precision '
                'calibration on a Core\'s neural interface system before the shift ends. '
                'The versatility is the interface\'s gift to engineering: the same operator, '
                'the same skills, applied across scales and distances that would require '
                'separate teams of specialists in any other faction. The engineers on '
                'Locke are generalists whose interface makes them specialists at whatever '
                'scale the job demands.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Kerwick',
            short_description='A gas giant with fuel processing -- routine, unremarkable, and maintained to the standard that a system full of people whose work requires perfect infrastructure demands.',
            long_description=(
                'Kerwick is the system\'s gas giant -- fuel processing on its moons '
                'supporting the traffic that the medical and engineering hub generates. '
                'The fuel operations are routine and maintained to a high standard because '
                'the system\'s population has no tolerance for infrastructure failure. A '
                'fuel disruption that affects the network connections to Colmaris is a '
                'fuel disruption that affects the surgical connections to patients across '
                'the cluster. The fuel workers understand the chain of consequence and '
                'maintain the standard accordingly.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Denholm',
            short_description='An agricultural world where the farming population feeds the surgeons and engineers -- and where the local medical care is the best in the galaxy because the surgeons are right there.',
            long_description=(
                'Denholm is the system\'s agricultural world -- temperate, productive, and '
                'the beneficiary of the most convenient healthcare arrangement in the '
                'cluster. The farmers on Denholm who need medical care receive it from '
                'Colmaris\'s surgeons operating through the local clinic\'s surgical '
                'robots -- the same surgeons who serve patients across the cluster, '
                'providing care to the farming population with the premium connection '
                'quality that physical proximity to Colmaris guarantees.\n\n'
                'The farmers are aware that they receive the best medical care in the '
                'galaxy as a side effect of geography. They did not choose to farm on '
                'Denholm for the healthcare. They farm on Denholm because the soil is '
                'good. The healthcare is a bonus that the farmers accept with the '
                'practical gratitude of people who understand that being near the '
                'hospital is better than being far from it, even when the hospital\'s '
                'surgeons are sitting in cradles and the surgery is performed by robots '
                'they have learned not to find unsettling.'
            ),
            population=700_000_000,
        ),
    ],
    short_description='The hospital -- six billion people in the system where the surgeons\' hands are robots on other worlds and the engineers build across the cluster from their cradles.',
    long_description=(
        'Schedar is the Polaris cluster\'s medical and engineering capital -- the '
        'system that demonstrates the practical case for neural integration more '
        'convincingly than any propaganda. The surgeons on Colmaris operate on '
        'patients they have never met in person -- sitting in cradles, their hands '
        'becoming robotic instruments at scales from human to cellular. The '
        'perception scales to match: at micro-scale, the surgical field becomes a '
        'landscape the surgeon navigates. The hand tremor every physical surgeon '
        'carries is filtered out. The metrics favour telepresence surgery on every '
        'measure, which is why every faction buys the technology even when they '
        'condemn the philosophy.\n\n'
        'The Routing routes the connections -- matching surgeons to patients across '
        'the cluster, managing latency in real time, rerouting when paths degrade. '
        'A routing failure during an operation is a surgeon whose hands have '
        'stopped responding with a patient open on the table. The quality of care '
        'correlates with connection quality, which correlates with location, which '
        'correlates with wealth.\n\n'
        'Pembrook trains the next generation -- the long, demanding process of '
        'learning to operate through the interface, to trust robot hands as your '
        'own, to perceive at scales the brain was not evolved for. The moment the '
        'scaling becomes natural is the moment the interface disappears and the '
        'surgeon simply operates. Locke provides the engineering counterpart -- '
        'the same scaled precision applied to construction and maintenance.\n\n'
        'The surgeons stare at trees during disconnect hours because the trees are '
        'the right size and the rightness is restorative.'
    ),
    cluster=StarClusters.POLARIS,
)


GRUMIUM = System(
    name='Grumium',
    star='Red giant (M3III), approximately 1,100 times Sol luminosity -- an enormous, cool star casting deep red light over a world where the machines work and the people watch from orbit',
    population=5_000_000_000,
    distance_to_sol=340.0,
    stellar_objects=[
        StellarObject(
            name='Halvek',
            short_description='A world too hostile for human survival and too mineral-rich to ignore -- the surface is worked entirely by robotic proxies controlled by operators who have never set foot on the planet below them.',
            long_description=(
                'Halvek is a dense, mineral-rich world with a surface that would kill a '
                'baseline human in minutes and a modified human not much later. The '
                'atmosphere is a superheated mix of sulphur compounds and carbon dioxide '
                'at three times standard pressure. The surface temperature averages four '
                'hundred degrees. The geological activity produces toxic outgassing that '
                'shifts the atmospheric composition unpredictably. The mineral deposits '
                'are among the richest in the cluster -- rare elements concentrated by '
                'the extreme geology into formations that the surveyors described as '
                'extraordinary and that the mining operators describe as worth the '
                'trouble.\n\n'
                'No human has ever stood on Halvek. No human ever will. The surface is '
                'worked entirely by robotic proxies -- mining rigs, extraction equipment, '
                'processing plants, and the maintenance machines that service the other '
                'machines, all controlled via telepresence by operators sitting in cradles '
                'on the orbital stations above. The operators experience Halvek through '
                'the proxies\' sensors: the heat rendered as warmth in their perception, '
                'the pressure as resistance, the toxic atmosphere as a chemical dataset '
                'their trained senses interpret without breathing it. The operators work '
                'the surface of a world that would kill them, from chairs in comfortable '
                'orbit, and the dissonance between the danger they operate in and the '
                'safety they sit in is the defining experience of a Grumium shift.\n\n'
                'The mining is heavy and continuous. The proxies operate around the clock '
                '-- an operator disconnects at shift end and another connects to the same '
                'machine, the transition seamless from the proxy\'s perspective. The '
                'machines do not rest because the machines do not need to. The operators '
                'rest because the operators do, and the shift schedules are built around '
                'human limitations that the machines they control do not share.'
            ),
            population=0,
        ),
        StellarObject(
            name='Tannert Station',
            short_description='The primary orbital station -- where two billion operators sit in cradles and work the planet below through machines they maintain, repair, and occasionally lose to the conditions they cannot survive.',
            long_description=(
                'Tannert Station is the largest orbital installation in the Grumium system '
                '-- a massive facility housing the operators who work Halvek\'s surface. '
                'The station is built around the cradle bays: floors of interface rigs '
                'where the operators connect to the proxies below. The bays are organised '
                'by operation type -- mining operators in one section, extraction in '
                'another, processing in a third, maintenance in a fourth -- and the '
                'operators specialise in the machines they control.\n\n'
                'The maintenance operators are the system\'s most valued workers. The '
                'proxies on Halvek\'s surface degrade -- the heat warps components, the '
                'pressure stresses seals, the corrosive atmosphere eats through protective '
                'coatings. A maintenance operator controls repair proxies that service the '
                'mining proxies, working in conditions that damage the repair machines '
                'themselves. The repair proxies have a shorter operational life than the '
                'mining equipment they maintain, and the maintenance operators occasionally '
                'lose a proxy to the conditions mid-repair -- the machine failing in the '
                'heat or the pressure, the operator\'s connection severing as the proxy '
                'dies. The operators describe the experience as abrupt: one moment they '
                'are hands in the machine, the next they are sitting in a chair in orbit. '
                'The proxy is gone. The operator requests another.\n\n'
                'The disconnect hours on Tannert are shaped by the work\'s particular '
                'psychology. The operators spend their shifts in lethal conditions through '
                'the proxies\' senses, and the shift to the station\'s safe, climate-'
                'controlled environment requires adjustment. The operators develop habits: '
                'touching the station\'s walls to confirm solidity, breathing deliberately '
                'to feel the air that the proxy does not need, the small reassurances that '
                'the body is here and the surface is there.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Corvel Station',
            short_description='A second orbital station housing the industrial workforce -- the processing and logistics operators who handle the extracted materials after they leave the surface.',
            long_description=(
                'Corvel Station is the system\'s second major orbital installation -- '
                'housing the operators who handle the extracted materials after the mining '
                'proxies have brought them off Halvek\'s surface. The processing is '
                'conducted in orbital refineries -- automated facilities where the raw '
                'materials from Halvek are processed into the industrial goods the cluster '
                'requires. The operators control the refinery systems via telepresence, '
                'though the orbital environment is less hostile than the surface and some '
                'of the processing work is performed by physically present crews in the '
                'refineries\' safer sections.\n\n'
                'The logistics operators on Corvel handle the distribution -- the '
                'freighters that carry Grumium\'s industrial output to the rest of the '
                'cluster. The system produces structural materials, rare-element '
                'components, and the refined alloys that the shipyards at Kochab and the '
                'manufacturing facilities on Rastaban require. The output is the cluster\'s '
                'industrial foundation, and Corvel\'s logistics operators are aware that '
                'the materials flowing through their systems become the ships the Cores '
                'inhabit and the interfaces the population connects through.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Pryce',
            short_description='A habitable world in the outer system -- where the operators\' families live, far enough from Halvek to forget what the parent is doing during their shift.',
            long_description=(
                'Pryce is the system\'s habitable world -- a cool, temperate planet in the '
                'outer system where the operators\' families live. The planet is far enough '
                'from Halvek that the lethal world is not visible in the night sky, which '
                'the families consider a feature. The children on Pryce know that their '
                'parents work on the stations above, controlling machines on a world that '
                'would kill them. The children accept this the way children accept the '
                'facts of their parents\' work -- as a reality that is normal because it '
                'is theirs.\n\n'
                'Pryce is a contrast to the stations. The planet is green, quiet, and '
                'physically present in a way the stations are not. The operators who '
                'rotate down to Pryce on their rest cycles describe the transition as '
                'the best part of the job -- the shift from the station\'s artificial '
                'environment and the proxy\'s lethal one to a world where the air is real '
                'and the ground is something you can stand on without a machine between '
                'you and it.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Bastern',
            short_description='A gas giant with fuel processing for the heavy industrial traffic -- the freighters that carry Grumium\'s output consume fuel at rates that reflect the weight of what they carry.',
            long_description=(
                'Bastern is the system\'s gas giant -- fuel processing on its moons '
                'supporting the heavy freighter traffic that Grumium\'s industrial output '
                'generates. The freighters are among the largest in the cluster -- heavy '
                'haulers built for the structural materials and refined alloys that are '
                'Grumium\'s primary export. The fuel consumption is proportional to the '
                'cargo, and Bastern\'s fuel operations are sized accordingly.\n\n'
                'The fuel processing is operated via telepresence from Corvel Station -- '
                'the operators adding fuel skimmer piloting to the list of remote tasks '
                'the system\'s workforce performs from orbit. The fuel workers describe '
                'the gas giant work as the easiest shift in the system -- after operating '
                'mining proxies on Halvek\'s four-hundred-degree surface, piloting a '
                'skimmer through a gas giant\'s atmosphere feels like a holiday.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Forshaw',
            short_description='An agricultural world feeding the system -- conventional farming on Pryce\'s temperate surface, by farmers who are the only people in the system who work with their own hands.',
            long_description=(
                'Forshaw is the system\'s agricultural region on Pryce -- the farming '
                'communities that feed the system\'s five billion people. The farming is '
                'conventional, physical, and the farmers are the only workers in Grumium '
                'who do their jobs with their own hands rather than through proxies. The '
                'distinction gives the farmers a particular identity in a system defined '
                'by remote operation -- they are the people who touch what they work on, '
                'and the operators on the stations regard them with a respect that '
                'contains a thread of envy for work that does not require a machine '
                'between the worker and the task.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The mine -- five billion people in orbit above a world too hostile for human survival, working its surface through robotic proxies controlled from comfortable chairs.',
    long_description=(
        'Grumium is the Polaris cluster\'s heavy industry system -- a dense, mineral-'
        'rich world with a surface that would kill any human in minutes: superheated '
        'atmosphere, three times standard pressure, toxic outgassing. No human has '
        'ever stood on Halvek. No human ever will. The surface is worked entirely '
        'by robotic proxies controlled via telepresence by operators in cradles on '
        'the orbital stations above.\n\n'
        'The operators experience Halvek through the proxies\' sensors -- heat as '
        'warmth, pressure as resistance, toxic atmosphere as a chemical dataset. '
        'They work the surface of a world that would kill them from chairs in '
        'comfortable orbit. The dissonance between the danger they operate in and '
        'the safety they sit in is the defining experience of a Grumium shift. '
        'Maintenance operators lose proxies to the conditions mid-repair -- one '
        'moment hands in the machine, the next sitting in a chair. The proxy is '
        'gone. The operator requests another.\n\n'
        'Tannert and Corvel stations house the workforce -- mining operators, '
        'processing crews, logistics staff. The output is the cluster\'s industrial '
        'foundation: structural materials, rare-element components, refined alloys '
        'for the shipyards and manufacturing facilities. Pryce is the habitable '
        'world where the families live, far enough from Halvek that the lethal '
        'world is not visible in the night sky.\n\n'
        'The operators develop habits after shifts: touching walls to confirm '
        'solidity, breathing deliberately to feel the air. The small reassurances '
        'that the body is here and the surface is there. Five billion people doing '
        'lethal work in perfect safety, separated from the danger by the interface '
        'that makes the danger feel real and the safety feel strange.'
    ),
    cluster=StarClusters.POLARIS,
)

COR_CAROLI = System(
    name='Cor Caroli',
    star='Binary system: blue-white main sequence (A0V) and yellow-white main sequence (F0V), approximately 100 times combined Sol luminosity -- two stars whose combined light produces the colour shifts the artists build their work around',
    population=6_000_000_000,
    distance_to_sol=110.0,
    stellar_objects=[
        StellarObject(
            name='Nellick',
            short_description='The creative capital -- three billion people in the system where VR is not a tool but a medium, and the art produced in simulation is more real to the audience than anything physical.',
            long_description=(
                'Nellick is the Polaris cluster\'s creative heart -- the system where the '
                'neural interface is used not for work but for expression. The artists on '
                'Nellick create in VR: immersive environments that are experienced through '
                'the interface as fully realised sensory spaces -- not images on a screen '
                'but places the audience inhabits, with light, sound, texture, temperature, '
                'scent, and the proprioceptive sensations that make the experience feel '
                'like being somewhere rather than looking at something.\n\n'
                'The art is the medium\'s natural expression. A painter in the inner systems '
                'works with pigment on a surface. A sculptor works with material in three '
                'dimensions. A Nellick artist works with reality itself -- designing '
                'environments that the audience\'s neural interface renders as sensory '
                'experience, controlling every element the audience perceives. The art on '
                'Nellick is not representational. It is experiential. The audience does not '
                'view the work. The audience enters it, and the distinction between viewing '
                'and entering is the distinction between every previous art form and what '
                'the neural interface has made possible.\n\n'
                'The cultural influence is difficult to overstate. Nellick\'s immersive works '
                'are consumed across the cluster and exported to every faction -- even MERIT '
                'space, where the works are experienced on the limited non-surgical '
                'interfaces that Polaran exports make available. The experience is '
                'diminished on the export hardware -- the sensory fidelity is lower, the '
                'depth of immersion is shallower -- but even the diminished version is '
                'unlike anything the inner systems\' conventional media can produce. The '
                'cultural soft power this represents is something the Cores value even '
                'though the stratocracy would never describe art as strategic.\n\n'
                'The artists work in cradles, like everyone else. The creative process is '
                'a session -- the artist connects, enters the work-in-progress, and builds '
                'the environment from inside it. The disconnect hours on Nellick are the '
                'cluster\'s most vibrant -- the artists unplug into a physical city that '
                'has been shaped by centuries of creative residents, and the architecture, '
                'the public spaces, and the social life reflect a population that thinks '
                'about aesthetics professionally and cannot stop thinking about them '
                'during their time off.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Studio',
            short_description='An orbital facility where the immersive works are hosted -- the servers that store the environments the audience enters, and the connection infrastructure that makes the experience possible at scale.',
            long_description=(
                'The Studio is the orbital facility that hosts the immersive works Nellick\'s '
                'artists produce -- the server infrastructure that stores the environments '
                'and the connection systems that allow audiences across the cluster to '
                'enter them. An immersive work is not a file that is transmitted. It is a '
                'shared environment that multiple audience members inhabit simultaneously, '
                'each experiencing the work from their own perspective, the environment '
                'responding to their presence and their neural interface\'s capacity.\n\n'
                'The hosting is the technical challenge. A popular work might have millions '
                'of simultaneous audience members, each one\'s experience individually '
                'rendered and transmitted through the network at the latency the immersion '
                'requires. The Studio\'s processing capacity is enormous -- the second-'
                'largest concentration of computing power in the cluster after Eltanin\'s '
                'network backbone, dedicated entirely to the creative output that the '
                'population produces and consumes. The engineers who maintain the Studio '
                'consider themselves technicians in service of art. The artists consider '
                'them essential and occasionally remember to say so.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Quinlan',
            short_description='The architecture world -- where buildings are designed in VR, refined through immersive simulation, and then built by telepresence crews who construct what the architects dreamed.',
            long_description=(
                'Quinlan is Cor Caroli\'s practical counterpart to Nellick\'s artistic output '
                '-- the world where the immersive design technology is applied to '
                'architecture, engineering, and the built environment. The architects on '
                'Quinlan design buildings in VR -- not as drawings or models but as full-'
                'scale immersive environments that the client can enter and inhabit before '
                'a single physical component is manufactured.\n\n'
                'The design process is iterative. The architect builds the environment in '
                'VR. The client enters it, walks through it, experiences the light, the '
                'space, the proportions. The architect adjusts in real time -- moving walls, '
                'changing materials, altering the light -- while the client stands inside '
                'the design and feels the changes. The process produces architecture that '
                'is tested by human experience before it is tested by physics, and the '
                'buildings that result are designed for how they feel to inhabit rather '
                'than how they look in a rendering.\n\n'
                'The construction is performed by telepresence crews on Locke and the '
                'other engineering worlds -- the architects transmit the finalised designs '
                'and the engineers build them with the scaled-precision tools the interface '
                'provides. The gap between design and construction is the gap between '
                'the dream and the physics, and the engineers occasionally inform the '
                'architects that the building they designed in VR cannot exist in reality '
                'because reality has load-bearing requirements that the simulation did '
                'not enforce. The architects find this frustrating. The engineers find it '
                'predictable.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Morrow',
            short_description='A residential world where the physical environment reflects the creative population -- a city built by its own architects, the most beautiful physical space in the cluster.',
            long_description=(
                'Morrow is Cor Caroli\'s residential world -- a temperate planet where '
                'the system\'s creative population lives during their disconnect hours. '
                'The city on Morrow is the most beautiful physical space in the Polaris '
                'cluster, because the people who live in it are the people who design '
                'beautiful spaces for a living and who could not bear to live in an '
                'ugly one.\n\n'
                'The architecture is the product of centuries of creative residents '
                'iterating on their own environment -- each generation of architects '
                'refining, rebuilding, and reimagining the city in the light of the '
                'work they produce in VR. The buildings incorporate design principles '
                'that originated in immersive art and were adapted for physical reality. '
                'The public spaces are designed for the sensory experience of occupying '
                'them -- the light falls the way it does because an architect cared about '
                'how it would feel at this hour, in this season, from this bench.\n\n'
                'The irony the residents acknowledge is that the physical city, beautiful '
                'as it is, is less immersive than the environments they create in VR. The '
                'physical world has constraints that VR does not. The light cannot be '
                'redesigned. The materials have properties the architect must accept. The '
                'city is the best the physical can offer, and the residents know that the '
                'virtual can offer more. They live in the physical city anyway, during the '
                'hours they are unplugged, because the body needs a place and the place '
                'should be worthy of the people who built it.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Jessamine',
            short_description='A gas giant whose atmospheric banding the artists have incorporated into the system\'s visual identity -- the colours referenced in works, architecture, and the local aesthetic vocabulary.',
            long_description=(
                'Jessamine is the system\'s gas giant -- fuel processing on its moons '
                'and an atmospheric banding pattern that the system\'s creative population '
                'has adopted as a visual signature. The gas giant\'s bands display colours '
                'produced by the binary star\'s mixed light interacting with the '
                'atmospheric chemistry -- pale blues, warm ambers, and the transitional '
                'gradients between that the artists on Nellick reference in their work the '
                'way painters once referenced the colours of the landscape they lived in.\n\n'
                'The fuel processing is standard. The aesthetic appreciation is not. '
                'Jessamine is the most observed gas giant in the cluster -- not by '
                'scientists but by artists who watch the bands shift and incorporate the '
                'changes into the evolving visual language of the system\'s creative '
                'output.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Felden',
            short_description='An agricultural world feeding the creative population -- the farms are functional, the food is good, and the farmers have opinions about the art their neighbours produce.',
            long_description=(
                'Felden is the system\'s agricultural world -- producing food for the '
                'creative population on Nellick and Morrow. The farming is conventional and '
                'the farmers are practical, and the relationship between the farming '
                'population and the creative population is the system\'s defining social '
                'dynamic: the farmers think the artists are impractical, the artists think '
                'the farmers are unimaginative, and both are wrong in ways that make the '
                'relationship productive.\n\n'
                'The farmers on Felden have opinions about the immersive art their '
                'neighbours produce. The opinions are not uninformed -- the farmers use '
                'basic interfaces and consume the works the way the rest of the cluster '
                'does. The farmers\' criticism tends toward the practical: does the work '
                'mean something, does the experience justify the time spent in the cradle, '
                'and is the artist saying anything that the farmer could not have said '
                'more efficiently by just talking. The artists find the criticism '
                'reductive. The farmers find the art excessive. The system functions '
                'because both sides need each other and neither admits it gracefully.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The creative heart -- six billion people in the system where VR is a medium, architecture is dreamed before it is built, and the art is experienced rather than viewed.',
    long_description=(
        'Cor Caroli is where the Polaris cluster\'s neural interface becomes art. '
        'The artists on Nellick create immersive environments experienced through the '
        'interface as fully realised sensory spaces -- not images but places the '
        'audience inhabits, with light, texture, temperature, scent. The artist '
        'works with reality itself, controlling every element the audience perceives. '
        'The audience does not view the work. The audience enters it.\n\n'
        'The cultural influence extends across every faction -- even MERIT space, '
        'where the works are experienced on export interfaces at diminished fidelity. '
        'Even diminished, the experience is unlike anything conventional media '
        'produces. The cultural soft power is something the Cores value even though '
        'the stratocracy would never describe art as strategic.\n\n'
        'Quinlan applies the technology to architecture -- buildings designed as '
        'full-scale immersive environments the client inhabits before a single '
        'component is manufactured. Architects adjust walls and light in real time '
        'while the client stands inside the design. The engineers who build the '
        'results occasionally inform the architects that reality has load-bearing '
        'requirements the simulation did not enforce.\n\n'
        'Morrow is the most beautiful physical city in the cluster -- built by '
        'its own architects over centuries, each generation refining the environment '
        'they live in. The irony the residents acknowledge: the physical city is '
        'less immersive than the environments they create in VR. They live in it '
        'anyway, during the hours they are unplugged, because the body needs a '
        'place and the place should be worthy of the people who built it.'
    ),
    cluster=StarClusters.POLARIS,
)

ALFIRK = System(
    name='Alfirk',
    star='Blue-white subgiant (B8IVe), approximately 1,500 times Sol luminosity -- a hot, bright star illuminating the system where the fleet trains for a war fought at the speed of thought',
    population=4_000_000_000,
    distance_to_sol=420.0,
    stellar_objects=[
        StellarObject(
            name='Vedris',
            short_description='The fleet world -- two billion people in the system where the Polaran military trains, deploys, and maintains the combat advantage that MERIT cannot match: ships that respond before the pilot has finished thinking.',
            long_description=(
                'Vedris is the Polaris cluster\'s military centre -- the system where the '
                'combat fleet is based, trained, and deployed. The planet houses the fleet '
                'command, the pilot training infrastructure, and the support population '
                'that keeps a war machine running. The military on Vedris is not the '
                'largest in the galaxy. It is the fastest.\n\n'
                'The neural-piloted combat fleet is Polaris\'s decisive advantage. A '
                'pilot with surgical interface ports does not fly a ship the way a manual '
                'pilot does. A manual pilot perceives a threat, processes it, decides on '
                'a response, and moves their hands to the controls. A neural pilot '
                'perceives the threat and the ship responds -- the intention translating '
                'to action without the bottleneck of conscious decision and physical '
                'movement. The reaction time difference is fractions of a second. In '
                'combat, fractions of a second are the difference between a hit and a '
                'miss, between evasion and impact, between survival and destruction.\n\n'
                'The fleet\'s coordination compounds the advantage. Neural-piloted ships '
                'in formation share tactical data through the network -- each pilot aware '
                'of every other pilot\'s position, vector, and intention. The formation '
                'moves as a single organism because each pilot knows what the others are '
                'about to do before they do it. A MERIT squadron engaging a Polaran '
                'formation encounters ships that anticipate each other\'s manoeuvres with '
                'a precision that manual coordination cannot reproduce. The MERIT pilots '
                'are fighting individual ships. The Polaran pilots are fighting as one '
                'mind in many bodies.\n\n'
                'The limitation is the ships themselves. The neural advantage is speed '
                'and coordination, not firepower or armour. Polaran warships are light, '
                'fast, and fragile by MERIT standards -- the design philosophy trades '
                'protection for agility because the pilots\' reaction times make agility '
                'more valuable than armour. A Polaran ship that is hit is in serious '
                'trouble. A Polaran ship that is not hit -- because the pilot evaded at '
                'the speed of thought -- is the most dangerous opponent in the galaxy.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Proving',
            short_description='The training grounds -- an orbital zone where the pilots drill formation flying, combat manoeuvres, and the neural coordination that makes a squadron into a single mind.',
            long_description=(
                'The Proving is the orbital training zone above Vedris -- the space where '
                'the fleet\'s pilots drill the combat tactics that the neural interface '
                'enables. The training is unlike any other military programme in the galaxy '
                'because the capabilities are unlike any other military\'s.\n\n'
                'The formation drills are the foundation. A squadron of neural-piloted '
                'ships must learn to share tactical awareness through the network -- to '
                'feel the other pilots\' intentions and to trust those intentions enough to '
                'act on them without verification. A pilot in formation who hesitates to '
                'verify what the network is telling them introduces a delay that defeats '
                'the purpose of the neural link. The training is the elimination of '
                'hesitation -- the slow, difficult process of teaching the pilot\'s instincts '
                'to trust the network the way they trust their own senses.\n\n'
                'The combat exercises use MERIT-specification targets -- drones programmed '
                'with manual-pilot reaction times and conventional formation tactics. The '
                'exercises are not fair. They are not designed to be fair. They are designed '
                'to train the fleet for the specific asymmetry that neural piloting '
                'produces: faster, more coordinated, more fragile. The pilots learn to '
                'exploit the speed and to never, under any circumstances, trade speed for '
                'the stand-up engagement that MERIT\'s heavier ships would win.'
            ),
            population=0,
        ),
        StellarObject(
            name='Strack',
            short_description='A world dedicated to the surgical enhancement programme -- where the pilots receive the interface ports that connect their nervous systems to their ships.',
            long_description=(
                'Strack is the system\'s surgical centre -- the world where the fleet\'s '
                'pilots receive the interface ports that the military piloting programme '
                'requires. The surgical enhancements are more extensive than civilian '
                'interface ports: additional connections along the spine for propulsion '
                'integration, ports at the base of the skull for weapons systems, and the '
                'peripheral nerve connections in the forearms and hands that give the pilot '
                'fine control over the ship\'s manoeuvring systems.\n\n'
                'The surgery is performed by Schedar\'s telepresence surgeons -- the best '
                'in the cluster, operating through robotic instruments at the micro-scale '
                'precision the neural connections demand. The recovery is long. The ports '
                'must integrate with the pilot\'s nervous system, the connections must '
                'stabilise, and the pilot must relearn their body\'s proprioception with '
                'the new hardware installed. A pilot who has received the full military '
                'port suite feels different to themselves -- the spine carries the '
                'awareness of connections that were not there before, the skull has points '
                'of contact that register as new senses, and the hands have a precision '
                'that the pilot did not possess before the surgery.\n\n'
                'The pilots describe the post-surgery period as learning to be a new '
                'version of themselves. The ports are permanent. The pilot who enters the '
                'surgical programme does not leave it as the same person -- not in the '
                'Core\'s total sense, but in the quiet, permanent way that additional '
                'hardware in the nervous system changes what it feels like to be alive.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Pembert',
            short_description='A residential world where the military families live -- where the parent comes home with new ports after each enhancement cycle and the children learn to recognise the changes.',
            long_description=(
                'Pembert is the system\'s residential world -- temperate, comfortable, and '
                'home to the military families. The culture on Pembert is shaped by the '
                'surgical enhancement programme: the parent who deploys for a new '
                'enhancement cycle returns with additional ports, additional capabilities, '
                'and the subtle difference in presence that each enhancement produces. The '
                'children learn to recognise the changes -- the new port at the base of '
                'the skull, the different way the parent moves their hands after the '
                'forearm connections are installed, the slight pause in conversation that '
                'indicates the parent is processing input from the ports that the family '
                'cannot perceive.\n\n'
                'The families accept the changes because the alternative is a parent who '
                'is not the cluster\'s best pilot, and the cluster needs its best pilots '
                'in ships that respond at the speed of thought. The acceptance is genuine '
                'and the loss is real: each enhancement makes the parent more capable in '
                'the ship and slightly more distant at the dinner table, not because the '
                'parent loves the family less but because the parent\'s nervous system now '
                'carries connections that the family cannot share and that the parent '
                'cannot fully describe.'
            ),
            population=700_000_000,
        ),
        StellarObject(
            name='Lorrick',
            short_description='A gas giant with military-grade fuel processing -- the fleet\'s fuel supply maintained at readiness levels that civilian operations would consider extravagant.',
            long_description=(
                'Lorrick is the system\'s gas giant -- fuel processing at military '
                'readiness, sized for a fleet that must be able to deploy at full strength '
                'on short notice. The fuel reserves are maintained at levels the civilian '
                'systems would consider wasteful -- the fleet\'s fuel is always available, '
                'always processed, always ready, because the response time that neural '
                'piloting provides is worthless if the ships are waiting for fuel.\n\n'
                'The fuel operations are a mix of telepresence and physical crew -- the '
                'skimmer piloting is remote, the processing is partially automated, and '
                'the quality control is performed by physical technicians who insist on '
                'inspecting the fuel rather than trusting the instruments. The military '
                'fuel workers consider the civilian fuel operations at Eltanin and '
                'Rastaban adequate for commerce and insufficient for combat. The standard '
                'is higher because the stakes are higher, and the fuel workers maintain '
                'the standard with the same precision the pilots bring to the cockpit.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Bartel',
            short_description='An agricultural world feeding the military system -- conventional farming by a population that has a higher proportion of veterans than any other farming community in the cluster.',
            long_description=(
                'Bartel is the system\'s agricultural world -- producing food for the '
                'military population on Vedris and the families on Pembert. The farming '
                'population includes a higher proportion of retired military personnel than '
                'any other agricultural community in the cluster -- pilots whose enhancement '
                'cycles are complete, whose bodies carry the ports they no longer use, and '
                'who have chosen farming as the work that reconnects them to the physical '
                'world after years of experiencing it through the interface.\n\n'
                'The veterans farm with their hands in the soil and their ports dormant. '
                'The ports are still there -- the connections along the spine, the sockets '
                'at the skull, the forearm interfaces. The hardware does not deactivate. '
                'It simply has nothing to connect to, and the veterans carry the quiet '
                'awareness of capabilities their body still possesses and their life no '
                'longer requires. The farming is deliberate, physical, and valued for '
                'precisely the qualities the interface cannot provide: the feel of soil, '
                'the weight of a harvest, the experience of working with hands that are '
                'only hands.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The fleet -- four billion people in the system where ships respond at the speed of thought and the pilots fight as one mind in many bodies.',
    long_description=(
        'Alfirk is the Polaris cluster\'s military staging system -- the place where '
        'the combat fleet that MERIT cannot match is trained and deployed. The '
        'neural-piloted ships respond to intention rather than manual input: the '
        'pilot perceives a threat and the ship acts, without the bottleneck of '
        'conscious decision and physical movement. Fractions of a second faster '
        'than manual pilots. In combat, fractions of a second are everything.\n\n'
        'The coordination compounds the advantage. Ships in formation share '
        'tactical awareness through the network -- each pilot aware of every '
        'other\'s position, vector, and intention. The formation moves as a single '
        'organism. A MERIT squadron encounters ships that anticipate each other\'s '
        'manoeuvres with precision manual coordination cannot reproduce. The MERIT '
        'pilots fight individual ships. The Polaran pilots fight as one mind in '
        'many bodies.\n\n'
        'The limitation is fragility. The design trades protection for agility '
        'because reaction times make agility more valuable than armour. A Polaran '
        'ship that is hit is in serious trouble. A ship that is not hit -- because '
        'the pilot evaded at the speed of thought -- is the most dangerous opponent '
        'in the galaxy.\n\n'
        'Strack performs the surgical enhancements -- ports along the spine, skull, '
        'forearms. The pilots describe the post-surgery period as learning to be a '
        'new version of themselves. Pembert houses the families who learn to '
        'recognise the changes each enhancement cycle brings. Bartel is farmed by '
        'veterans whose bodies carry the ports they no longer use, choosing soil '
        'and hands as the work that reconnects them to the physical world.'
    ),
    cluster=StarClusters.POLARIS,
)


EDASICH = System(
    name='Edasich',
    star='Orange giant (K2III), approximately 600 times Sol luminosity -- a warm, familiar star for the system that has decided that being in the room is worth more than being in the network',
    population=5_000_000_000,
    distance_to_sol=100.0,
    stellar_objects=[
        StellarObject(
            name='Torland',
            short_description='The most physically present world in the cluster -- three billion people who use interfaces when they must and prefer not to, in a civilisation that considers this quaint and cannot explain why it also finds it unsettling.',
            long_description=(
                'Torland is the Polaris cluster\'s most deliberately physical world. The '
                'population uses neural interfaces -- they are not Luddites, not anti-'
                'technology, not making a political statement. They communicate through the '
                'network, access data through the interfaces, and connect when the task '
                'requires it. They simply prefer not to. The default on Torland is '
                'disconnected. The interfaces are tools that are used and put down, the '
                'way a previous era used telephones -- essential for communication, not '
                'the medium through which life is conducted.\n\n'
                'The consequence is a city that looks occupied. The streets have people on '
                'them during working hours because the people are going to work in person. '
                'The offices are staffed by people who are physically present, doing their '
                'jobs with their hands and their voices and their faces in the same room '
                'as their colleagues. The restaurants are full during meals because meals '
                'are not compressed into disconnect windows -- meals happen when people '
                'are hungry, the way meals have happened for the entirety of human history '
                'prior to the interface cradle.\n\n'
                'Visitors from the rest of the cluster find Torland disorienting in a '
                'direction they do not expect. The disorientation is not that Torland is '
                'strange. The disorientation is that Torland is familiar -- that the '
                'streets full of people, the offices full of workers, the restaurants full '
                'of diners feel like something the visitor remembers from before the '
                'cradles, and the remembering produces an emotion the visitor did not '
                'anticipate. The Polaran word for the feeling translates roughly as '
                'presence-grief -- the sadness of recognising a way of living you did not '
                'know you had lost.\n\n'
                'The economy is smaller. Torland\'s GDP per capita is lower than '
                'Callidren\'s or Holst\'s because the telepresence economy multiplies a '
                'worker\'s reach and Torland\'s workers reach only as far as their arms. A '
                'surgeon on Torland operates on the patient in the room. An engineer on '
                'Torland builds what is in front of them. The economic limitation is the '
                'philosophical point: the work is slower, less scalable, and performed by '
                'a person who is entirely in the room with the thing they are working on. '
                'Torland considers this a feature. The rest of the cluster considers it '
                'a charming inefficiency.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Saddler',
            short_description='A second world where the physical-first culture has produced the cluster\'s best hands-on craftspeople -- artisans whose work is valued precisely because it was made by a person who was there.',
            long_description=(
                'Saddler is Edasich\'s artisan world -- a planet where the physical-first '
                'culture has produced craftspeople whose work commands premiums across the '
                'cluster. The products are furniture, instruments, clothing, tools, and the '
                'objects of daily life, all made by hand by people who were physically '
                'present for every step of the process. In a cluster where manufacturing '
                'is performed via telepresence and the operator may never have been in the '
                'same system as the product, the fact that a Saddler artisan touched the '
                'thing they made is a selling point that commands prices the economics do '
                'not justify and the buyers pay anyway.\n\n'
                'The value is authenticity in a civilisation that has made physical '
                'presence optional. A chair made by a Saddler craftsperson was shaped by '
                'hands that felt the wood, in a workshop the craftsperson walked to that '
                'morning, using tools they picked up rather than remotely operated. The '
                'chair is not better than a telepresence-manufactured equivalent. The '
                'chair was made differently, and the difference matters to buyers who '
                'spend their lives in cradles and want something in their homes that was '
                'made by someone who was standing up.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Merritt Station',
            short_description='The orbital port where the disconnect happens -- visitors from the connected cluster arrive and are gently encouraged to unplug for the duration of their stay.',
            long_description=(
                'Merritt Station is Edasich\'s orbital port -- the facility where visitors '
                'arrive from the connected cluster and encounter the system\'s culture for '
                'the first time. The station\'s staff do not require visitors to disconnect '
                '-- the interfaces work in Edasich, the network reaches here, and nobody '
                'is forced to unplug. The staff simply suggest it. The suggestion is '
                'gentle, experienced, and effective: the staff explain that Edasich is '
                'designed for the physically present, that the experience of the system is '
                'the experience of being in a place without the network overlay, and that '
                'the visitor will understand Torland better unplugged than connected.\n\n'
                'Most visitors unplug. The experience of walking through Merritt Station '
                'without the network -- the sudden absence of the data overlay, the '
                'presence of other minds, the ambient awareness that the connected take '
                'for granted -- is itself the introduction to Edasich\'s philosophy. The '
                'visitors feel the absence as loss and then, gradually, as clarity. The '
                'world without the network is quieter, simpler, and more immediately '
                'present. Some visitors find the clarity refreshing. Some find it '
                'intolerable. The staff have seen both responses and serve coffee to '
                'either with the same patience.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Hald',
            short_description='An agricultural world where the farming is entirely physical and the farmers consider themselves the most honest workers in the cluster because their work has always been done this way.',
            long_description=(
                'Hald is the system\'s agricultural world -- conventional farming by a '
                'population that farms the way farming has been done since before the '
                'interfaces existed. The farmers on Hald are the system\'s philosophical '
                'anchor -- the people who do the work that has never needed to be '
                'telepresence and who regard the cluster\'s transformation of every other '
                'profession into a cradle-based activity with the mild bewilderment of '
                'people whose job was never going to change.\n\n'
                'The food from Hald is exported across the cluster alongside Saddler\'s '
                'crafts -- the produce carrying the same implicit value of physical '
                'presence. The crops were grown by people who walked the fields. The '
                'animals were raised by people who touched them. The food tastes the same '
                'as food grown anywhere else. The buyers pay the premium anyway, for '
                'reasons that have more to do with what the food represents than what it '
                'contains.'
            ),
            population=700_000_000,
        ),
        StellarObject(
            name='Casper',
            short_description='A gas giant with fuel processing -- the one operation in the system that uses telepresence without apology, because the alternative is sending bodies into a gas giant.',
            long_description=(
                'Casper is the system\'s gas giant -- fuel processing on its moons, '
                'operated via telepresence because the alternative is sending physical '
                'workers into a gas giant\'s atmosphere and the system\'s commitment to '
                'physical presence does not extend to suicide. The fuel operations are the '
                'one activity on Edasich that uses telepresence without apology or '
                'philosophical hedging. The workers connect, pilot the skimmers, '
                'disconnect, and do not feel conflicted about it.\n\n'
                'The inconsistency is noted by visitors and accepted by the residents. '
                'Edasich\'s philosophy is preference, not dogma. The interfaces are used '
                'when the task genuinely requires them and set down when it does not. '
                'Fuel skimming in a gas giant genuinely requires them. The residents '
                'consider this obvious and find the visitors\' observation that it '
                'constitutes hypocrisy mildly tiresome.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Vernell',
            short_description='A small world that has become the cluster\'s retreat destination -- where connected Polarans come to spend time unplugged and remember what it feels like to be only where they are.',
            long_description=(
                'Vernell is a small, temperate world that has become the Polaris cluster\'s '
                'most unlikely export: the disconnected retreat. Polarans from across the '
                'cluster travel to Vernell to spend time unplugged -- days or weeks without '
                'the network, without the interface, without the ambient awareness of other '
                'minds. The retreats are not religious or ideological. They are practical: '
                'the connected population occasionally needs to remember what it feels like '
                'to be only where they are, and Vernell provides the environment for it.\n\n'
                'The retreats are popular with the body-house workers from Thuban, the '
                'telepresence operators from Grumium, and the military pilots from Alfirk '
                '-- the people whose working lives are spent most deeply in the interface '
                'and whose need for physical recalibration is greatest. The Core maintenance '
                'crews from Kochab visit in notable numbers -- the people who spend their '
                'working hours inside ships that contain people who will never disconnect, '
                'choosing to spend their rest in a place that is defined by disconnection.\n\n'
                'The retreat industry is Vernell\'s economy. The facilities are simple -- '
                'comfortable housing, natural spaces, physical activities, and the '
                'deliberate absence of cradles. The staff are Edasich locals who find the '
                'visitors\' need to schedule their disconnection both understandable and '
                'faintly sad.'
            ),
            population=200_000_000,
        ),
    ],
    short_description='The disconnected -- five billion people who use interfaces when they must and prefer not to, in a system where the streets are full because the population is physically present.',
    long_description=(
        'Edasich is the Polaris cluster\'s most deliberately physical system. The '
        'population uses neural interfaces -- they are not anti-technology. They '
        'communicate through the network and connect when the task requires it. '
        'They simply prefer not to. The default is disconnected. The interfaces are '
        'tools that are used and put down.\n\n'
        'The consequence is a city that looks occupied. Streets with people on them '
        'during working hours. Offices staffed by people physically present. '
        'Restaurants full during meals because meals are not compressed into '
        'disconnect windows. Visitors from the connected cluster find it '
        'disorienting in an unexpected direction -- not that Torland is strange but '
        'that Torland is familiar, and the familiarity produces what the Polarans '
        'call presence-grief: the sadness of recognising a way of living you did '
        'not know you had lost.\n\n'
        'Saddler\'s artisans produce handmade goods that command premiums across '
        'the cluster -- the value is that a person was physically present for every '
        'step. Vernell hosts disconnection retreats for the body-house workers, '
        'telepresence operators, and military pilots whose need for physical '
        'recalibration is greatest. The Core maintenance crews visit in notable '
        'numbers.\n\n'
        'The economy is smaller. Torland\'s workers reach only as far as their '
        'arms. The rest of the cluster considers this a charming inefficiency. '
        'Torland considers it a feature. The fuel operations use telepresence '
        'without apology because the alternative is sending bodies into a gas '
        'giant, and the system\'s philosophy is preference, not dogma.'
    ),
    cluster=StarClusters.POLARIS,
)


NAVI = System(
    name='Navi',
    star='Blue-white subgiant (B0.5IVpe), approximately 65,000 times Sol luminosity -- an enormously bright, unstable star at the edge of the cluster\'s network reach, casting harsh light on a population that the civilisation\'s defining technology has left behind',
    population=3_000_000_000,
    distance_to_sol=550.0,
    stellar_objects=[
        StellarObject(
            name='Calvey',
            short_description='The lag world -- two billion people living in a civilisation built on telepresence who cannot use telepresence because the network takes too long to reach them.',
            long_description=(
                'Calvey is what happens when a Polaran world is too far from the backbone. '
                'The planet is habitable, terraformed, and populated by two billion people '
                'who are citizens of a civilisation built on neural telepresence and who '
                'cannot meaningfully use it. The network reaches Navi. The signal takes '
                'too long. The latency between Calvey and the Lattice at Eltanin is '
                'measured in hundreds of milliseconds -- imperceptible for communication, '
                'usable for data access, and catastrophic for the skilled telepresence '
                'work that the cluster\'s economy runs on.\n\n'
                'A surgeon on Calvey cannot operate on a patient at Schedar. The latency '
                'is too high -- the instruments would respond a quarter-second after the '
                'surgeon\'s intention, producing errors at the micro-scale that the '
                'precision work demands. An engineer on Calvey cannot assemble components '
                'on Grumium. A pilot on Calvey cannot fly a ship at Alfirk with the '
                'neural coordination the formation requires. The work that the rest of the '
                'cluster performs through the interface -- the work that defines Polaran '
                'economic life -- is not available to Calvey\'s population at the quality '
                'level the market demands.\n\n'
                'The population works with their hands. The surgeons on Calvey operate in '
                'person, on patients who are in the room, with physical instruments. The '
                'engineers build with tools they hold. The factories are staffed by workers '
                'who stand at their stations. The economy resembles an inner-systems world '
                'more than a Polaran one, and the cultural dissonance is Calvey\'s defining '
                'feature: the population has the interfaces, has the training, has the '
                'skills -- and cannot deploy them at the quality that the connected '
                'systems\' workers achieve because the network will not cooperate.\n\n'
                'The resentment is quiet and specific. Calvey\'s population does not '
                'resent the technology. They resent the geography. The cluster built a '
                'civilisation on a network and settled a world outside the network\'s '
                'effective range, and the population that lives there pays the price in '
                'careers that are limited by latency rather than talent. A surgeon on '
                'Calvey who is the equal of a surgeon on Colmaris earns less because the '
                'Calvey surgeon can only operate on patients who are physically present, '
                'and the pool of physically present patients is two billion rather than '
                'the entire cluster.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Rodwell',
            short_description='A second world where the latency has produced the cluster\'s most self-sufficient industrial economy -- because if you cannot import skilled labour through the network, you must produce it locally.',
            long_description=(
                'Rodwell is Navi\'s industrial world -- a colder, mineral-rich planet where '
                'the manufacturing and mining operations are performed by physical workers '
                'rather than telepresence operators. The industry on Rodwell is the most '
                'self-sufficient in the cluster because it must be: the skilled telepresence '
                'labour that other systems import through the network is not available at '
                'Navi\'s latency, and the system must train and maintain its own workforce '
                'for every speciality.\n\n'
                'The self-sufficiency has produced unexpected strengths. Rodwell\'s physical '
                'engineers -- people who build with their hands rather than through '
                'interfaces -- have developed techniques that the telepresence-dependent '
                'systems have lost. The knowledge of how to physically assemble a component '
                'at a workbench, how to diagnose a malfunction by touch and sound rather '
                'than through the interface\'s diagnostic overlay, how to improvise a '
                'repair when the correct part is not available because the supply chain '
                'from the connected systems takes weeks to reach Navi. The skills are '
                'practical, hard-won, and increasingly rare in a cluster that has '
                'outsourced physical competence to the interface.\n\n'
                'The rest of the cluster has begun to notice. When a system\'s network '
                'connection fails -- a relay outage on Eltanin, a routing disruption at '
                'the Lattice -- the population discovers that it has forgotten how to do '
                'things without the interface. The workers who can still function during a '
                'network outage are disproportionately from Navi, because Navi\'s workers '
                'never had the luxury of depending on the network in the first place.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Tolver Station',
            short_description='The orbital relay that represents the system\'s best connection to the cluster -- the station the population watches the way a desert settlement watches its well.',
            long_description=(
                'Tolver Station is Navi\'s primary orbital facility and the system\'s '
                'network relay -- the station that provides whatever connection to the '
                'cluster the distance allows. The relay is the most important piece of '
                'infrastructure in the system, maintained with an intensity that reflects '
                'the population\'s relationship with the network: they cannot use it for '
                'the skilled work it was designed for, but they depend on it for '
                'communication, data access, and the cultural connection to a civilisation '
                'they are technically part of and practically at the margins of.\n\n'
                'The relay engineers on Tolver are the system\'s elite -- the technical '
                'staff who maintain the connection and who lobby Eltanin\'s backbone '
                'administration for bandwidth upgrades, latency improvements, and the '
                'infrastructure investment that might, someday, bring Navi within the '
                'network\'s effective range. The lobbying has been ongoing for decades. '
                'The improvements have been incremental. The physics of the distance is '
                'the fundamental problem, and the physics does not respond to lobbying.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Jessop',
            short_description='A gas giant with fuel processing done by physical crews rather than telepresence -- not by choice but because the latency makes remote skimmer piloting dangerously imprecise.',
            long_description=(
                'Jessop is the system\'s gas giant -- fuel processing on its moons by '
                'physical crews who pilot the skimmers in person rather than via '
                'telepresence. The latency that makes skilled work impractical across the '
                'cluster network also makes local telepresence unreliable -- the signal '
                'between Calvey and Jessop is fast enough for communication but the '
                'precision required for skimmer piloting in a gas giant\'s atmosphere '
                'demands response times that the local network infrastructure struggles '
                'to provide consistently.\n\n'
                'The physical fuel crews are another expression of Navi\'s self-sufficiency. '
                'The crews pilot the skimmers from cockpits rather than cradles, flying the '
                'machines with manual controls that the rest of the cluster has largely '
                'abandoned. The work is more dangerous -- a physical crew in a skimmer is '
                'at risk in a way a telepresence operator is not. The crews accept the '
                'risk because the alternative is no fuel, and no fuel means no ships, and '
                'no ships means a system that is already at the margins becomes entirely '
                'cut off.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Carrick',
            short_description='An agricultural world that feeds the system -- the farming indistinguishable from farming anywhere in the galaxy, which is the point.',
            long_description=(
                'Carrick is the system\'s agricultural world -- terraformed, temperate, '
                'farmed by hand. The farming on Carrick is identical to farming on Hald '
                'at Edasich or Tilderen at Polaris -- physical work, physical crops, '
                'physical harvest. The difference is that on Hald and Tilderen the farmers '
                'farm physically by choice, and on Carrick the farmers farm physically '
                'because there is no alternative.\n\n'
                'The distinction matters to the farmers. Edasich\'s physical culture is a '
                'philosophy. Navi\'s physical culture is a constraint. The farmers on '
                'Carrick do not romanticise their hands-on work the way Saddler\'s '
                'artisans do. They farm with their hands because the network does not '
                'reach, and they would use telepresence if they could, and the fact that '
                'they cannot is not a feature but a limitation that the rest of the '
                'cluster has not bothered to fix.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The lag -- three billion people in a civilisation built on telepresence who cannot use it because the network takes too long to reach them.',
    long_description=(
        'Navi is what happens when a Polaran world is too far from the backbone. '
        'The network reaches. The signal takes too long. The latency is hundreds '
        'of milliseconds -- usable for communication, catastrophic for the skilled '
        'telepresence the economy runs on. A surgeon on Calvey cannot operate on a '
        'patient at Schedar. An engineer cannot assemble components on Grumium. The '
        'work that defines Polaran economic life is not available at the quality '
        'the market demands.\n\n'
        'The population works with their hands. Surgeons operate in person. '
        'Engineers build with tools they hold. The economy resembles an inner-'
        'systems world more than a Polaran one. The resentment is quiet and '
        'specific: not the technology but the geography. The cluster built a '
        'civilisation on a network and settled a world outside its effective range. '
        'Careers are limited by latency rather than talent.\n\n'
        'The self-sufficiency has produced unexpected strengths. Rodwell\'s physical '
        'engineers have techniques the telepresence-dependent systems have lost -- '
        'diagnosing by touch, improvising repairs without the correct part. When a '
        'network outage hits the connected systems and the population discovers it '
        'has forgotten how to do things without the interface, the workers who can '
        'still function are disproportionately from Navi.\n\n'
        'Edasich is physical by choice. Navi is physical by constraint. The '
        'distinction matters. Edasich\'s culture is a philosophy. Navi\'s is a '
        'limitation the rest of the cluster has not bothered to fix.'
    ),
    cluster=StarClusters.POLARIS,
)

PHERKAD = System(
    name='Pherkad',
    star='White giant (A7III), approximately 180 times Sol luminosity -- a pale, quiet star for the system where the most powerful minds in the cluster link together and the ground population is not invited',
    population=2_000_000_000,
    distance_to_sol=480.0,
    stellar_objects=[
        StellarObject(
            name='Vassik',
            short_description='The world below the congress -- one billion people living under the orbital formation where the Cores link their minds together to make the decisions that shape the cluster, in a process the ground population cannot observe or participate in.',
            long_description=(
                'Vassik is the world that exists in the shadow of the deliberation. The '
                'planet is habitable, temperate, and home to a billion people whose '
                'relationship with the Cores above them is different from Thessan\'s. On '
                'Thessan, the Procession is the visible government -- the chain of lights '
                'that represents the stratocracy in orbit. On Vassik, the Cores are not '
                'governing. They are thinking together, and the thinking is something the '
                'ground population cannot perceive, cannot participate in, and cannot '
                'fully understand.\n\n'
                'The Core deliberations at Pherkad are the cluster\'s most important '
                'decision-making process. The Cores link their minds through direct neural '
                'connections -- not the standard network that the civilian population uses '
                'but close-range, high-bandwidth links that require the ships to be in '
                'physical proximity. The linked Cores share perception, analysis, and the '
                'cognitive processing that produces decisions of a depth and speed that '
                'individual minds -- even Core minds -- cannot achieve alone. The linked '
                'deliberation is described by the Cores who have participated as thinking '
                'with more than one brain: the problem perceived from multiple '
                'perspectives simultaneously, the analysis conducted in parallel, the '
                'solution emerging from a cognitive process that no single participant '
                'could have performed.\n\n'
                'The ground population of Vassik watches the Core fleet arrive for a '
                'deliberation -- the capital ships moving into the close formation that '
                'the linking requires, the ships\' systems aligning, and then silence. The '
                'deliberation produces no visible output. The ships sit in formation, the '
                'Cores link, and the decision is made in a process that the ground '
                'population experiences as waiting. The ships arrive, go quiet, and '
                'eventually depart. The policy that results is transmitted to Thessan and '
                'the ground learns what was decided without ever knowing how.\n\n'
                'The democratic deficit is the system\'s defining political problem. The '
                'linked deliberation is the stratocracy\'s most effective decision-making '
                'tool -- the quality of the decisions is demonstrably high, the speed is '
                'unmatched, and the depth of analysis exceeds anything a conventional '
                'government could produce. The process is also entirely opaque to the '
                'citizens it governs. The Cores cannot explain the linked deliberation to '
                'unlinked minds because the experience has no analogue in individual '
                'cognition. The citizens must trust that the process produces good '
                'decisions without being able to verify the process itself. The trust '
                'holds because the decisions are competent. The trust is fragile because '
                'the competence is unverifiable.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='The Convocation',
            short_description='The orbital zone where the Core fleet links -- the physical space where the capital ships align for the neural congress that produces decisions the ground cannot observe.',
            long_description=(
                'The Convocation is the orbital zone above Vassik where the Core fleet '
                'assembles for deliberation -- a defined region of space where the capital '
                'ships move into the close formation the linking requires. The ships must '
                'be within a specific range for the high-bandwidth neural connections to '
                'function -- close enough that the direct links operate without the '
                'latency that the standard network introduces, far enough apart that the '
                'ships\' systems do not interfere with each other.\n\n'
                'The formation is precise and the approach is choreographed -- capital '
                'ships manoeuvring into position with the care that the neural links '
                'demand. A ship that is out of position by metres can degrade the link '
                'quality for the entire formation. The approach is performed by the Cores '
                'themselves -- the linked fleet moving with the coordination that neural '
                'piloting provides, each Core aware of every other Core\'s position and '
                'adjusting with the precision that is the defining advantage of the '
                'technology.\n\n'
                'Once linked, the Convocation is silent. The ships\' external systems go '
                'quiet -- the Cores directing all processing capacity inward, toward the '
                'shared cognitive space where the deliberation occurs. The ground-based '
                'monitoring stations on Vassik can detect the formation and confirm that '
                'the ships are present. They cannot detect the deliberation itself. The '
                'linked cognition produces no external signal. The most powerful decision-'
                'making process in the cluster is invisible to every instrument the ground '
                'population possesses.'
            ),
            population=0,
        ),
        StellarObject(
            name='Proval',
            short_description='A world housing the analysts and advisors who prepare the material the Cores deliberate on -- the closest the ground population comes to participating in the linked congress.',
            long_description=(
                'Proval is Pherkad\'s second inhabited world -- a cooler planet housing '
                'the analysts, advisors, and policy specialists who prepare the material '
                'the Cores deliberate on. The work is the ground population\'s closest '
                'approach to the linked congress: the analysts identify the issues, '
                'compile the data, model the options, and transmit the briefing packages '
                'to the Core fleet before the deliberation begins. The Cores receive the '
                'material, integrate it into the linked cognition, and produce decisions '
                'that the analysts then interpret for ground-level implementation.\n\n'
                'The analysts on Proval are the stratocracy\'s translators -- the people '
                'who convert ground-level reality into data the Cores can process and who '
                'convert the Cores\' decisions back into policy the ground can implement. '
                'The translation is imperfect in both directions. The analysts cannot '
                'convey the full complexity of ground-level life to minds that experience '
                'reality through ship sensors. The Cores cannot convey the full reasoning '
                'of a linked deliberation to minds that think individually. The gap '
                'between the two is the space where misunderstanding accumulates, and the '
                'analysts spend their careers managing the gap with the awareness that it '
                'cannot be closed.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Oster',
            short_description='A small world where the Core fleet is serviced between deliberations -- the maintenance that keeps the governing minds alive performed by crews who are not permitted to know what was decided.',
            long_description=(
                'Oster is a small, rocky world with the orbital facilities that service '
                'the Core fleet between deliberations. The maintenance crews from Kochab\'s '
                'Drevnik rotate through Oster during deliberation cycles -- performing the '
                'same intimate, classified work of maintaining the ships that house the '
                'Cores\' bodies, checking the neural connections, and monitoring the '
                'biological systems that sustain the pilots.\n\n'
                'The crews who service the fleet at Oster operate under additional security '
                'protocols during deliberation cycles. The Cores\' neural state during and '
                'after a linked deliberation is sensitive data -- the maintenance crews can '
                'read the Cores\' biological telemetry and potentially infer information '
                'about the deliberation from the neural activity patterns. The security '
                'protocols require the crews to perform the maintenance without analysing '
                'the data beyond what the maintenance requires. The crews describe this as '
                'changing the oil without reading the odometer -- performing the physical '
                'care while deliberately not learning what the machine has been doing.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Brevitt',
            short_description='A gas giant with fuel processing for the Core fleet -- sized for the capital ships\' enormous consumption during the close-formation manoeuvres the linking requires.',
            long_description=(
                'Brevitt is the system\'s gas giant -- fuel processing sized for the Core '
                'fleet\'s requirements. The capital ships\' fuel consumption during the '
                'close-formation manoeuvres that precede a deliberation is substantial -- '
                'the ships must maintain precise positions against each other\'s '
                'gravitational influence, and the station-keeping burns consume fuel at '
                'rates that exceed normal orbital operations. Brevitt\'s fuel reserves are '
                'maintained for the deliberation cycles, topped up between sessions by '
                'routine processing.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Landsford',
            short_description='An agricultural world feeding the system -- the farmers who look up at the Core fleet in orbit and know that the decisions being made above their fields will determine the shape of their lives.',
            long_description=(
                'Landsford is the system\'s agricultural world -- producing food for '
                'Pherkad\'s two billion people and the Core fleet during deliberation '
                'cycles. The farmers on Landsford are accustomed to the sight of the Core '
                'fleet in formation above their fields -- the capital ships visible as '
                'bright points in the daytime sky during deliberations, silent and '
                'unmoving for days at a time.\n\n'
                'The farmers have developed the habit of watching the fleet for movement '
                '-- when the formation shifts, the deliberation is ending, and the '
                'decisions that result will eventually reach Landsford as policy changes '
                'that affect crop quotas, export allocations, and the administrative '
                'details of agricultural life. The farmers cannot influence the decisions. '
                'The farmers can watch the ships that make them and speculate, which is '
                'the full extent of the democratic participation that the linked '
                'deliberation permits.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The congress -- two billion people living under the orbital formation where the Cores link their minds and make the decisions the ground cannot observe, participate in, or fully understand.',
    long_description=(
        'Pherkad is where the Cores think together. The system hosts the linked '
        'deliberations -- the process where the governing fleet assembles in close '
        'formation and the Cores connect through direct, high-bandwidth neural '
        'links that require physical proximity. The linked Cores share perception '
        'and analysis, producing decisions of a depth and speed that individual '
        'minds cannot achieve. The Cores describe it as thinking with more than '
        'one brain: the problem perceived from multiple perspectives simultaneously, '
        'the solution emerging from a cognitive process no single participant could '
        'have performed.\n\n'
        'The Convocation is the orbital zone where the formation assembles -- ships '
        'manoeuvring into position with the precision neural piloting provides, a '
        'ship out of position by metres degrading the link for the entire formation. '
        'Once linked, the fleet goes silent. The deliberation produces no external '
        'signal. The most powerful decision-making process in the cluster is '
        'invisible to every instrument the ground possesses.\n\n'
        'Proval\'s analysts prepare the material and translate the decisions back '
        'into policy -- the imperfect bridge between ground-level reality and '
        'linked cognition. The gap between the two is where misunderstanding '
        'accumulates, and the analysts spend careers managing a gap that cannot '
        'be closed.\n\n'
        'The democratic deficit is the system\'s defining problem. The decisions '
        'are demonstrably competent. The process is entirely opaque. The Cores '
        'cannot explain the linked deliberation to unlinked minds because the '
        'experience has no analogue in individual cognition. The citizens must '
        'trust a process they cannot verify. The trust holds because the decisions '
        'are good. The trust is fragile because the goodness is unverifiable.'
    ),
    cluster=StarClusters.POLARIS,
)

SEGIN = System(
    name='Segin',
    star='Blue-white main sequence (B9V), approximately 200 times Sol luminosity -- a hot, young star for the system where the next version of what a human mind can do is being built',
    population=3_000_000_000,
    distance_to_sol=430.0,
    stellar_objects=[
        StellarObject(
            name='Meriden',
            short_description='The research capital -- two billion people in the system where the next generation of neural interfaces is designed, and where the test subjects carry hardware that does not exist anywhere else in the galaxy.',
            long_description=(
                'Meriden is where the Polaris cluster invents its future. The planet hosts '
                'the research institutions that develop the next generation of neural '
                'interface technology -- the hardware and protocols that will define what '
                'the cluster\'s population can do with their minds in ten, twenty, fifty '
                'years. The current interfaces are extraordinary by the rest of the '
                'galaxy\'s standards. The researchers on Meriden consider them crude.\n\n'
                'The research programmes are layered. The near-term work improves the '
                'existing interfaces: better latency, higher bandwidth, finer sensory '
                'fidelity, the incremental gains that make each generation of interface '
                'slightly more transparent -- the technology between the mind and the task '
                'becoming thinner until the mind forgets the technology is there. The '
                'mid-term work develops new capabilities: interfaces that carry emotional '
                'data alongside cognitive, allowing the operator to feel the state of the '
                'machine they control. Interfaces that support multi-operator linkage for '
                'ground-dwellers -- the congress capability that currently requires a '
                'Core\'s architecture, adapted for minds that have not been fused to ships. '
                'Interfaces that extend perception into spectra the human brain was never '
                'designed to process.\n\n'
                'The long-term work is the research that the institutions do not discuss '
                'publicly. The boundary between mind and machine is a line the cluster has '
                'been approaching for centuries, and Meriden\'s long-term programmes are '
                'the ones that intend to cross it. The specifics are classified. The '
                'direction is not: the researchers are working toward an interface that '
                'does not connect the mind to the machine but makes the distinction between '
                'mind and machine meaningless. The Cores achieved something close to this '
                'through fusion -- the pilot\'s nervous system growing into the ship until '
                'the boundary dissolves. Meriden\'s long-term goal is the dissolution '
                'without the fusion. A mind that extends into a machine without being '
                'trapped in it.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Pen',
            short_description='The testing facility -- where the experimental interfaces are installed in volunteers who carry hardware that has never been in a human body before and whose side effects are discovered rather than predicted.',
            long_description=(
                'The Pen is Segin\'s orbital testing facility -- the place where the '
                'experimental interfaces developed on Meriden are installed in human '
                'volunteers and the results are observed. The name is old, sardonic, and '
                'accurate: the volunteers are penned -- confined to the facility for the '
                'duration of the trial, monitored continuously, their neural activity '
                'recorded at resolutions that capture every firing pattern the experimental '
                'hardware produces.\n\n'
                'The volunteers are not conscripts. They are the cluster\'s most committed '
                'researchers -- scientists who install their own experimental hardware '
                'because the only way to understand what a new interface does to a mind is '
                'to experience it. The practice is controversial even within the research '
                'community. The counter-argument is practical: an interface designed to '
                'extend human perception cannot be fully evaluated by instruments that '
                'measure from the outside. The experience must be reported from the inside, '
                'and the report requires a mind trained to observe its own modification.\n\n'
                'The side effects are discovered rather than predicted. An experimental '
                'interface that extends perception into the infrared may also produce '
                'synaesthesia -- the new spectral data interpreted by the brain as sound '
                'or texture because the neural pathways for processing the new input have '
                'not been established and the brain improvises. A multi-operator linkage '
                'prototype may produce bleed -- traces of the linked partner\'s thoughts '
                'persisting after disconnection, the volunteer hearing echoes of a mind '
                'that is no longer connected. The side effects are documented, studied, '
                'and in some cases incorporated into the design when the researchers '
                'determine that the unintended effect is more useful than the intended one.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Cantwell',
            short_description='A world where the long-term test subjects live -- people carrying experimental hardware that has been in their bodies for years, whose daily lives are the ongoing data.',
            long_description=(
                'Cantwell is the residential world for Segin\'s long-term test subjects -- '
                'volunteers who have carried experimental interface hardware for years and '
                'whose daily lives are the ongoing study. The subjects live normally -- '
                'they work, raise families, participate in the community -- and the '
                'research staff monitor how the experimental hardware interacts with the '
                'long-term reality of a human life.\n\n'
                'The long-term data is the research\'s most valuable output. An interface '
                'that works in the controlled environment of the Pen may behave differently '
                'over years of use -- the neural pathways adapting to the hardware, the '
                'hardware adapting to the neural pathways, the slow mutual adjustment that '
                'produces effects the short-term testing did not reveal. A subject who '
                'has carried an emotional-data interface for three years reports that they '
                'can feel their spouse\'s mood through the interface without a direct '
                'connection -- the hardware has learned the spouse\'s neural patterns from '
                'proximity, and the subject perceives the patterns without conscious effort. '
                'The researchers did not design this. The hardware and the brain designed '
                'it together, over time, without being asked.\n\n'
                'The subjects on Cantwell are aware that they are the experiment. The '
                'awareness is part of the culture -- the community shares its experiences '
                'openly, compares side effects, discusses the capabilities their hardware '
                'has developed, and collectively represents the most neurologically diverse '
                'population in the galaxy. No two subjects carry the same experimental '
                'hardware. Every mind on Cantwell perceives reality slightly differently. '
                'The conversations are interesting in ways that visitors find difficult to '
                'follow because the participants are referencing perceptions the visitor '
                'does not have.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Oakes',
            short_description='The manufacturing prototype facility -- where experimental interfaces are fabricated in quantities of one, each unique, each designed for a specific volunteer\'s neural architecture.',
            long_description=(
                'Oakes is Segin\'s fabrication world -- the place where the experimental '
                'interfaces are manufactured. Unlike Helvarden\'s mass production or '
                'Brask\'s export manufacturing, every interface produced on Oakes is unique '
                '-- designed for a specific volunteer\'s neural architecture, fabricated in '
                'a quantity of one, and installed with the understanding that it has never '
                'existed before in a human body and that the results are uncertain.\n\n'
                'The fabrication is the most precise manufacturing in the cluster -- '
                'components at scales that push the limits of what the telepresence '
                'operators can assemble, tolerances that the production hardware on '
                'Helvarden is not designed to achieve. The fabricators on Oakes are the '
                'cluster\'s most skilled interface engineers, and their work is artisanal '
                'in the literal sense: each piece is handcrafted for a specific mind, '
                'and the craftsperson\'s skill determines whether the interface will '
                'function as designed or fail in the unpredictable ways that experimental '
                'hardware fails.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Kellam',
            short_description='A gas giant with fuel processing -- standard operations in a system where nothing else is standard.',
            long_description=(
                'Kellam is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The fuel operations are standard and '
                'the fuel workers consider the normalcy a relief. The rest of the system '
                'is experimental hardware, unknown side effects, and volunteers whose '
                'perception of reality is being deliberately altered. The fuel workers '
                'process hydrogen and helium. The fuel workers find this grounding.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Darsett',
            short_description='An agricultural world feeding the research population -- farmers who have become accustomed to neighbours who perceive things the farmers cannot and who occasionally describe colours that do not exist.',
            long_description=(
                'Darsett is the system\'s agricultural world -- producing food for '
                'Meriden\'s research population and Cantwell\'s test subjects. The farmers '
                'are conventional and the neighbours are not. The long-term test subjects '
                'who visit Darsett\'s markets carry hardware that produces perceptions the '
                'farmers do not share, and the social interactions are coloured by the '
                'gap: a subject might comment on the infrared warmth of the fruit on the '
                'stall, or flinch at a sound the farmer cannot hear, or describe the '
                'colour of the sunset in terms that do not correspond to any colour the '
                'farmer\'s eyes can see.\n\n'
                'The farmers have adapted. The subjects are good neighbours -- polite, '
                'aware that their perceptions are unusual, and generally careful about '
                'describing experiences that might alarm people whose hardware is standard. '
                'The occasional lapses are accepted as the cost of living next to the '
                'future, which is how the farmers describe their neighbours: the people '
                'who are already living in the version of reality that everyone else will '
                'inhabit once the research is finished.'
            ),
            population=400_000_000,
        ),
    ],
    short_description='The frontier -- three billion people in the system where the next generation of neural interfaces is invented, tested on volunteers who carry hardware that has never been in a human body, and lived with on a world where every mind perceives reality differently.',
    long_description=(
        'Segin is where the Polaris cluster invents its future. The research '
        'institutions on Meriden develop the next generation of neural interfaces: '
        'near-term incremental gains, mid-term new capabilities like emotional data '
        'transfer and ground-dweller congress, and the long-term classified work '
        'aimed at making the distinction between mind and machine meaningless '
        'without requiring the Core\'s fusion.\n\n'
        'The Pen tests the experimental hardware on volunteers who are also '
        'researchers -- scientists who install their own experiments because an '
        'interface designed to extend perception cannot be fully evaluated from '
        'outside. Side effects are discovered rather than predicted: synaesthesia '
        'from infrared extension, bleed from multi-operator prototypes. Some '
        'unintended effects prove more useful than the intended ones.\n\n'
        'Cantwell houses the long-term subjects -- volunteers carrying experimental '
        'hardware for years, whose daily lives are the data. The hardware and the '
        'brain adapt to each other over time in ways the short-term testing did not '
        'reveal. A subject carrying an emotional-data interface for three years '
        'reports feeling their spouse\'s mood without a direct connection -- the '
        'hardware learned the patterns from proximity. The researchers did not '
        'design this. The hardware and the brain designed it together.\n\n'
        'Oakes fabricates each experimental interface as a unique piece -- designed '
        'for a specific volunteer\'s neural architecture, manufactured in a quantity '
        'of one. Darsett\'s farmers have become accustomed to neighbours who '
        'perceive things they cannot and who occasionally describe colours that '
        'do not exist.'
    ),
    cluster=StarClusters.POLARIS,
)

ALKAID = System(
    name='Alkaid',
    star='Blue-white main sequence (B3V), approximately 700 times Sol luminosity -- a hot, bright star at the edge of the cluster, pointing outward toward the space that nobody has reached and that the drones keep trying to cross',
    population=2_000_000_000,
    distance_to_sol=104.0,
    stellar_objects=[
        StellarObject(
            name='Rossen',
            short_description='The launch world -- one billion people in the system dedicated to finding out what is beyond the edge, building the machines that might get there, and recovering the ones that come back broken.',
            long_description=(
                'Rossen is the Polaris cluster\'s outermost ambition -- the world dedicated '
                'to exploration beyond the known jump network. The planet hosts the '
                'research institutions, the drone manufacturing, and the mission control '
                'infrastructure that the exploration programme requires. The goal is '
                'simple to state and has resisted decades of effort: find new systems, '
                'map new jump points, and eventually find routes that take humanity beyond '
                'this corner of the galaxy.\n\n'
                'The challenge is the jump points. The known network connects the systems '
                'that humanity has settled, but the network has edges -- jump points that '
                'lead to systems that are mapped but unoccupied, and beyond those, jump '
                'points that the survey data suggests exist but that no ship has '
                'successfully transited. The problem is not the jump physics. The problem '
                'is the human. Some jump points produce transit conditions that the human '
                'body or mind cannot survive -- gravitational stresses that exceed the '
                'inertial resonators\' capacity, radiation spikes that overwhelm shielding, '
                'or the transit distortions that the pilots call shear, where the jump\'s '
                'geometry twists the ship in ways that the crew\'s perception cannot '
                'process without neurological damage.\n\n'
                'The solution is to remove the human. The drone programme on Rossen builds '
                'unmanned probes designed to make the jumps that crewed ships cannot -- '
                'machines with no nervous system to damage, no perception to distort, no '
                'biological limit on the transit conditions they can survive. The drones '
                'are launched toward the edge jump points, transit the points that would '
                'kill a crew, and transmit data from whatever is on the other side. Some '
                'transmit. Many do not. The jump points at the edge are hostile in ways '
                'the known network is not, and the drones that do not return are the '
                'majority.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='The Catapult',
            short_description='The launch facility -- an orbital complex from which the exploration drones are dispatched toward jump points that have killed every crewed ship that has attempted them.',
            long_description=(
                'The Catapult is the orbital launch facility above Rossen -- the complex '
                'from which the exploration drones are dispatched toward the edge jump '
                'points. The facility manufactures, tests, and launches the probes in a '
                'continuous cycle that the programme has maintained for decades. The launch '
                'rate is high because the return rate is low -- the drones that transit '
                'the hostile jump points and successfully transmit data from the other side '
                'are a fraction of the total launched.\n\n'
                'The launches are routine in the way that a programme that has been running '
                'for decades makes failure routine. A drone is launched, approaches the '
                'jump point, transits, and either transmits or does not. The mission '
                'controllers on the Catapult wait for the signal. When it comes, the data '
                'is processed and the mission is a success. When it does not come -- when '
                'the drone has been destroyed by the transit conditions or has emerged on '
                'the other side damaged beyond communication -- the controllers log the '
                'failure, update the jump point\'s profile, and prepare the next drone. '
                'The programme is not discouraged by failure. The programme is calibrated '
                'for it.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Talbert',
            short_description='The analysis world -- where the data from the successful drones is processed, the new systems are mapped, and the slow picture of what lies beyond the edge is assembled one transmission at a time.',
            long_description=(
                'Talbert is the system\'s analysis centre -- the world where the data from '
                'the drones that successfully transmit is processed and assembled into the '
                'expanding map of what lies beyond the known network. The work is slow. '
                'Each successful drone provides a fragment -- a survey of a single system, '
                'a partial map of the jump points available on the other side, the '
                'astronomical data that tells the analysts what kind of star, what kind '
                'of planets, what kind of possibilities.\n\n'
                'The map is growing. The decades of drone launches have produced a picture '
                '-- incomplete, fragmented, full of gaps -- of the systems that lie beyond '
                'the cluster\'s edge. The picture includes habitable worlds that nobody can '
                'reach because the jump points that lead to them are too hostile for crewed '
                'ships. The picture includes systems with resources that the cluster needs '
                'and cannot access. The picture includes, at the furthest range of the '
                'most successful drones, hints of structures that the analysts are not '
                'ready to describe as artificial but that they are not ready to describe '
                'as natural either.\n\n'
                'The hints are classified. The analysts discuss them in sealed meetings '
                'and do not discuss them outside. The hints may be artefacts of the '
                'drones\' damaged sensors. The hints may be natural geological formations '
                'that the resolution cannot distinguish from constructed ones. The hints '
                'may be something else. The programme continues launching drones toward '
                'the systems where the hints were detected, and the drones continue to '
                'mostly not come back.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Warsett',
            short_description='The drone graveyard -- a world where the drones that return damaged are recovered, studied, and stripped for data, their broken bodies telling the story of the jump that nearly destroyed them.',
            long_description=(
                'Warsett is where the drones come home to die. The world hosts the '
                'recovery and analysis facilities for the probes that transit the hostile '
                'jump points and return -- damaged, often barely functional, carrying the '
                'physical evidence of what the transit did to them. The drones\' hulls are '
                'warped by gravitational stresses. The electronics are scrambled by '
                'radiation. The structural members are twisted by the shear that kills '
                'crews and damages machines.\n\n'
                'The engineers on Warsett study the damage the way forensic scientists '
                'study evidence -- reading the drone\'s injuries to understand the jump '
                'point\'s characteristics. A hull warped in a specific pattern tells the '
                'engineers about the gravitational profile. Radiation damage to specific '
                'components reveals the spectrum and intensity. The shear damage tells them '
                'about the geometric distortion. Each broken drone is a data point, and '
                'the accumulated data points are slowly teaching the programme how to '
                'build drones that survive the jumps more reliably.\n\n'
                'The surface of Warsett is littered with the remains of drones that have '
                'been studied and stripped. The field of broken machines extends for '
                'kilometres around the analysis facilities -- thousands of probes that '
                'were launched toward the unknown and came back as wreckage. The programme '
                'considers the field a monument to persistence. The visitors consider it '
                'a monument to something they are not sure they can name.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Trennick',
            short_description='A gas giant with fuel processing for the exploration programme -- the drones need fuel and the programme needs a lot of drones.',
            long_description=(
                'Trennick is the system\'s gas giant -- fuel processing on its moons '
                'supporting the exploration programme\'s considerable appetite. The drones '
                'require fuel for the transit and the launch rate is high enough that the '
                'fuel operations are substantial. The fuel workers are aware that the fuel '
                'they process goes into machines that mostly do not come back, and the '
                'awareness produces a particular attitude: the work is important, the '
                'results are uncertain, and the fuel goes out the door and the programme '
                'builds another drone and the fuel goes out the door again.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Haslam',
            short_description='An agricultural world feeding the exploration system -- farmers who watch the drone launches from their fields and who have become accustomed to the streaks of light that mostly do not come back.',
            long_description=(
                'Haslam is the system\'s agricultural world -- producing food for '
                'Rossen\'s research population and the support staff across the system. '
                'The farmers work their fields under a sky that occasionally shows the '
                'bright streak of a drone launch from the Catapult -- the acceleration '
                'flare visible as a line of light pointing toward the edge jump points. '
                'The farmers have watched these launches for decades and have developed '
                'the habit of counting the streaks going out and the fainter streaks '
                'coming back. The ratio is not encouraging. The farmers count anyway, '
                'the way people who live near a lighthouse count the ships.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The edge -- two billion people building the machines that might find a way beyond this corner of the galaxy, launching them toward jump points that destroy most of what enters, and waiting for the signal that mostly does not come.',
    long_description=(
        'Alkaid is the Polaris cluster\'s outermost ambition -- the system dedicated '
        'to exploration beyond the known jump network. The challenge is the jump '
        'points at the edge: transit conditions that the human body cannot survive '
        '-- gravitational stresses beyond the resonators\' capacity, radiation '
        'spikes, the geometric shear that twists perception into neurological '
        'damage. The solution is to remove the human. The drone programme builds '
        'unmanned probes to make the jumps crewed ships cannot.\n\n'
        'The Catapult launches the drones. The return rate is low. The controllers '
        'wait for the signal, process the data when it comes, log the failure when '
        'it does not, and prepare the next drone. The programme is calibrated for '
        'failure. Talbert assembles the fragments into a growing, incomplete map of '
        'what lies beyond -- habitable worlds behind hostile jump points, resources '
        'behind lethal transits, and at the furthest range, hints of structures the '
        'analysts are not ready to describe as artificial but not ready to describe '
        'as natural either. The hints are classified.\n\n'
        'Warsett studies the drones that come back broken -- reading the damage '
        'like forensic evidence, each warped hull and scrambled circuit a data '
        'point teaching the programme how to build survivors. The field of broken '
        'machines extends for kilometres. The programme considers it a monument to '
        'persistence.\n\n'
        'The farmers on Haslam watch the launch streaks from their fields and '
        'count the ones going out and the fainter ones coming back. The ratio is '
        'not encouraging. The farmers count anyway, the way people who live near a '
        'lighthouse count the ships.'
    ),
    cluster=StarClusters.POLARIS,
)

UPL_1037 = System(
    name='UPL-1037',
    star='Red dwarf (M4V), approximately 0.02 times Sol luminosity -- a dim star barely visible through the dust cloud that has become the substrate for the largest living thing humanity has ever encountered',
    population=0,
    distance_to_sol=500.0,
    stellar_objects=[
        StellarObject(
            name='The Bloom',
            short_description='A spacefaring fungal organism colonising an enormous dust cloud -- spore structures feeding on interstellar dust, growing like mould across millions of kilometres, the largest single living thing in the known galaxy.',
            long_description=(
                'The Bloom is the reason UPL-1037 is on every research priority list in '
                'the cluster and the reason nobody lives here. The system contains an '
                'enormous cloud of interstellar dust -- a remnant of stellar formation '
                'that never coalesced into planets, spread across a volume of space '
                'measured in hundreds of millions of kilometres. The dust cloud is '
                'colonised by a spacefaring fungal organism that feeds on the dust\'s '
                'mineral content, extracting energy and nutrients from the particulate '
                'matter through biochemical processes the researchers on Meriden are still '
                'trying to understand.\n\n'
                'The organism grows like mould. The structure is a network of filaments -- '
                'threads of biological material that extend through the dust cloud, '
                'branching and connecting in patterns that span millions of kilometres. '
                'The filaments are thin -- individually no wider than a human hair -- but '
                'the network is vast, and the total biomass of the Bloom is larger than '
                'any other single organism humanity has encountered. The organism is not '
                'colonial. Genetic analysis confirms it is a single individual -- one '
                'organism, one genome, spread across a volume of space that dwarfs most '
                'solar systems.\n\n'
                'The spore structures are the most visible feature. At irregular intervals '
                'along the filament network, the organism produces fruiting bodies -- '
                'bulbous structures that range from metres to kilometres in diameter, '
                'growing on the filaments the way mushrooms grow on mycelium. The fruiting '
                'bodies produce spores that drift through the dust cloud on the faint '
                'stellar wind, colonising new regions of dust and extending the network '
                'further. The spores are hardy -- resistant to vacuum, radiation, and the '
                'temperature extremes of interstellar space. The researchers estimate that '
                'the spores can survive dormant for centuries before encountering dust '
                'dense enough to germinate.\n\n'
                'The Bloom is not dangerous. The organism does not react to ships. The '
                'filaments are fragile enough that a vessel can pass through the network '
                'without difficulty, the threads breaking and regrowing behind the ship '
                'the way a spider\'s web repairs after a disturbance. The danger is '
                'navigational -- the dust cloud reduces sensor range, the filaments '
                'produce false readings, and the fruiting bodies are dense enough to '
                'damage a ship that collides with one at speed. The system is transitable '
                'with care. Settlement is impractical because the dust cloud extends '
                'through the habitable zone and the organism has colonised every surface '
                'that holds still long enough.\n\n'
                'The research value is extraordinary. The Bloom is a spacefaring organism '
                '-- a biological system that survives and reproduces in the interstellar '
                'medium without a planet, without an atmosphere, without any of the '
                'conditions that terrestrial biology considers necessary for life. The '
                'biochemistry is unlike anything in the cluster\'s catalogue. The '
                'researchers want to understand how the organism extracts energy from dust, '
                'how the filaments maintain biological function in vacuum, and whether the '
                'spore dormancy mechanisms have applications for human biology. The '
                'research is ongoing. The organism continues to grow. The Bloom does not '
                'know it is being studied and would not care if it did, because the Bloom '
                'is a fungus and the fungus is busy.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-1037-a',
            short_description='A rocky body at the dust cloud\'s edge -- the research station where the Bloom is studied from a safe distance, by scientists who can see the filaments on their sensors and the fruiting bodies from the observation deck.',
            long_description=(
                'UPL-1037-a is a small rocky body at the edge of the dust cloud -- the '
                'only solid surface in the system not colonised by the Bloom, because it '
                'sits outside the cloud\'s densest region. The research station on the '
                'surface studies the organism from a distance that the scientists consider '
                'safe and that the organism does not consider at all.\n\n'
                'The station\'s observation deck faces the dust cloud, and the view is the '
                'research programme\'s unofficial recruiting tool. The cloud is visible as '
                'a faint haze against the starfield, and the Bloom\'s fruiting bodies are '
                'visible within it -- dim shapes, some large enough to resolve with the '
                'naked eye, glowing faintly with the bioluminescence that the organism '
                'produces as a metabolic byproduct. The view from the observation deck is '
                'a dust cloud full of dim, glowing shapes that are alive and that are all '
                'one organism. The scientists who work here find it beautiful. The visitors '
                'who see it for the first time find it difficult to process at the scale '
                'the mind requires.'
            ),
            population=0,
        ),
    ],
    short_description='The Bloom -- a spacefaring fungal organism colonising an enormous dust cloud, the largest single living thing humanity has ever encountered.',
    long_description=(
        'UPL-1037 contains the Bloom -- a spacefaring fungal organism that has '
        'colonised an enormous interstellar dust cloud. The organism feeds on the '
        'dust\'s mineral content through biochemical processes the researchers are '
        'still trying to understand. The structure is a network of filaments -- '
        'threads of biological material spanning millions of kilometres, branching '
        'and connecting through the cloud. Individually thin as a human hair. '
        'Collectively the largest single organism in the known galaxy.\n\n'
        'The fruiting bodies grow on the filaments like mushrooms on mycelium -- '
        'structures from metres to kilometres in diameter, producing spores that '
        'drift on the stellar wind and colonise new dust regions. The spores '
        'survive dormant for centuries in vacuum. The organism is not dangerous -- '
        'the filaments break and regrow around ships. The danger is navigational: '
        'reduced sensor range, false readings, dense fruiting bodies that damage '
        'ships at speed.\n\n'
        'The research value is extraordinary. A biological system that survives '
        'and reproduces in the interstellar medium without a planet or atmosphere. '
        'The biochemistry is unlike anything in the catalogue. The researchers '
        'want to understand the energy extraction from dust, the vacuum-functional '
        'filaments, the spore dormancy. The organism continues to grow. The Bloom '
        'does not know it is being studied and would not care if it did, because '
        'the Bloom is a fungus and the fungus is busy.'
    ),
    cluster=StarClusters.POLARIS,
)

UPL_4479 = System(
    name='UPL-4479',
    star='Yellow-orange main sequence (G5V), approximately 0.8 times Sol luminosity -- a stable, Sol-like star that the survey team reached six months ago and that the data is still coming in on',
    population=0,
    distance_to_sol=490.0,
    stellar_objects=[
        StellarObject(
            name='UPL-4479-a',
            short_description='A habitable-zone world that the survey team is still assessing -- the initial data is promising and the full picture is months away.',
            long_description=(
                'UPL-4479-a is the system\'s primary world -- a rocky body in the habitable '
                'zone that the survey team\'s initial scans suggest may be habitable with '
                'terraforming. The data is preliminary. The atmospheric composition '
                'readings are incomplete. The surface surveys have covered less than '
                'twenty percent of the landmass. The survey team has been in the system '
                'for six months and the work is ongoing.\n\n'
                'The preliminary data is promising in the careful way that survey teams '
                'use the word promising -- the atmosphere contains the precursors for '
                'terraforming, the surface temperature range is within the band that '
                'engineering can address, and the geological data suggests mineral '
                'deposits that would support a colony\'s industrial needs. The survey team '
                'has not yet committed to a recommendation because the data does not yet '
                'support one. The team leader\'s interim reports use phrases like '
                'encouraging preliminary indicators and warrants continued assessment, '
                'which the cluster\'s colonial planners have learned to translate as the '
                'team is optimistic but will not say so until the numbers are complete.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-4479-b',
            short_description='A second rocky world further from the star -- cold, marginal, surveyed as part of the system assessment but not the primary candidate.',
            long_description=(
                'UPL-4479-b is the system\'s second rocky world -- colder, further from '
                'the star, and assessed as a secondary candidate. The world is marginal '
                'for habitation even with terraforming, but the mineral surveys suggest '
                'deposits that would complement a colony based on UPL-4479-a. The survey '
                'team has allocated less time to UPL-4479-b than to the primary world, '
                'focusing resources on the candidate with the most potential. The secondary '
                'world\'s assessment will be completed after the primary\'s, if the '
                'preliminary data continues to warrant the team\'s continued presence.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-4479-c',
            short_description='A gas giant -- confirmed by the initial survey, fuel processing potential noted, details pending.',
            long_description=(
                'UPL-4479-c is the system\'s gas giant -- confirmed by the initial orbital '
                'survey, fuel processing potential noted in the interim report, and '
                'detailed assessment pending. The gas giant\'s presence is positive for '
                'the system\'s colonial viability -- a local fuel source reduces the '
                'dependency on imports that makes remote colonies expensive. The survey '
                'team has used the gas giant for their own fuel needs during the mission, '
                'which constitutes an informal proof of concept that the formal assessment '
                'will confirm with more data and less informality.'
            ),
            population=0,
        ),
    ],
    short_description='The newest discovery -- a system the survey team reached six months ago, still being assessed, the data promising and incomplete.',
    long_description=(
        'UPL-4479 is the most recently discovered system in the Polaris cluster -- '
        'a Sol-like star that the survey team reached six months ago. The data is '
        'still coming in. The primary world is a habitable-zone candidate that the '
        'preliminary scans suggest may be terraformable -- atmospheric precursors, '
        'acceptable temperature range, mineral deposits that would support industry. '
        'The survey team is optimistic but will not say so until the numbers are '
        'complete.\n\n'
        'The system is the cluster\'s freshest possibility -- a world that might '
        'become something, assessed by a team that is still measuring what it is. '
        'The gas giant provides local fuel. The second world offers mineral '
        'potential. The survey continues. The interim reports say encouraging '
        'preliminary indicators. The colonial planners read optimistic between '
        'the lines.'
    ),
    cluster=StarClusters.POLARIS,
)

UPL_7741 = System(
    name='UPL-7741',
    star='Red dwarf (M5V), approximately 0.003 times Sol luminosity -- the dimmest star in the cluster, orbited by nothing worth mentioning',
    population=0,
    distance_to_sol=460.0,
    stellar_objects=[
        StellarObject(
            name='UPL-7741-a',
            short_description='A frozen rock -- no atmosphere, no minerals of value, no reason to land.',
            long_description=(
                'UPL-7741-a is a frozen rock orbiting a dim red dwarf. The survey team '
                'that catalogued the system spent three weeks here, completed a thorough '
                'assessment, and produced a report that is comprehensive, professional, and '
                'unremarkable in every respect. The planet has no atmosphere. The mineral '
                'deposits are common elements available in more accessible concentrations '
                'in dozens of other systems. The surface is frozen regolith under a sky '
                'lit by a star so dim that midday resembles twilight.\n\n'
                'The survey team\'s geologist noted in the report that UPL-7741-a is the '
                'most boring world she has personally assessed, and that she has assessed '
                'thirty-seven worlds. The note was left in the report by a review process '
                'that presumably agreed.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-7741-b',
            short_description='A second frozen rock -- smaller, darker, equally devoid of interest.',
            long_description=(
                'UPL-7741-b is a smaller body in the outer system -- a frozen rock that '
                'the survey team scanned from orbit and did not bother to land on. The '
                'remote scans confirmed what the survey team expected: ice, rock, common '
                'minerals, and nothing that justifies the fuel expenditure of a landing. '
                'The system\'s only contribution to the cluster is its position on the '
                'jump network -- a waypoint between systems that contain things people '
                'want, connecting places that matter through a place that does not.'
            ),
            population=0,
        ),
    ],
    short_description='Empty -- a dim red dwarf orbited by frozen rocks with nothing to offer except a position on the jump network between systems that actually matter.',
    long_description=(
        'UPL-7741 is the system the cluster routes through and does not think about. '
        'A dim red dwarf orbited by frozen rocks with no atmosphere, no valuable '
        'minerals, and no reason to visit. The survey report is comprehensive and '
        'unremarkable. The geologist noted it was the most boring world she had '
        'personally assessed out of thirty-seven. The review process left the note '
        'in the report.\n\n'
        'The system\'s contribution is its position -- a waypoint on the jump '
        'network between systems that contain things people want. The traffic '
        'passes through without stopping. The rocks orbit the dim star. Nothing '
        'happens here. Nothing has ever happened here. The probability that '
        'anything will ever happen here is, according to the survey team\'s '
        'assessment, low.'
    ),
    cluster=StarClusters.POLARIS,
)

UPL_2281 = System(
    name='UPL-2281',
    star='Orange main sequence (K2V), approximately 0.4 times Sol luminosity -- a stable, patient star waiting for the terraforming to finish and the colonists to arrive in a few decades',
    population=0,
    distance_to_sol=520.0,
    stellar_objects=[
        StellarObject(
            name='UPL-2281-a',
            short_description='A world being terraformed -- the atmospheric processors are running, the orbital mirrors are adjusting the temperature, and the first colonists are scheduled to arrive in approximately thirty years.',
            long_description=(
                'UPL-2281-a is becoming habitable. The world was assessed two decades ago '
                'as a terraforming candidate -- rocky, within the habitable zone, with an '
                'atmosphere that contained the chemical precursors the processors could '
                'work with. The terraforming was authorised by the Cores, funded by the '
                'cluster\'s colonial development budget, and commenced fifteen years ago. '
                'The atmospheric processors are running. The orbital mirrors are adjusting '
                'the surface temperature. The microbial seeding has begun in the regions '
                'where the processors have brought the atmospheric composition within '
                'survivable range.\n\n'
                'The timeline is approximately thirty years to habitability -- the point '
                'where the atmosphere will support human respiration with minor interface-'
                'assisted environmental monitoring rather than sealed habitats. The '
                'timeline is a projection that the engineers update annually and that the '
                'colonial planners treat as a commitment. The engineers are careful to note '
                'that terraforming timelines are projections rather than promises. The '
                'colonial planners are careful to ignore this distinction because the '
                'settlement planning that depends on the timeline has already begun.\n\n'
                'The world is currently uninhabited except for the engineering staff who '
                'maintain the terraforming equipment. The staff live in sealed habitats '
                'on the surface and in the orbital facilities that support the mirror '
                'array, and they are the first people to live in a system that will not '
                'be a colony for decades. The staff describe the experience as living in '
                'the future\'s construction site -- the world outside the habitat windows '
                'is changing, slowly, measurably, the atmospheric readings ticking toward '
                'the target values month by month. The staff will not be here when the '
                'colonists arrive. The staff are building a world they will never live in.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-2281-b',
            short_description='A rocky outer world earmarked for mining when the colony arrives -- the mineral surveys are complete, the deposits are mapped, and the extraction will begin when there are people to do it.',
            long_description=(
                'UPL-2281-b is a cold, rocky world in the outer system -- surveyed, '
                'assessed, and earmarked for mining operations that will commence when the '
                'colony on UPL-2281-a is established. The mineral deposits are mapped in '
                'detail -- the survey team spent months cataloguing the resources that the '
                'future colony will need. The deposits are good. The deposits are also '
                'decades away from being useful, and the survey data sits in the colonial '
                'planning archives alongside the settlement layouts, the infrastructure '
                'schedules, and the population projections that describe a colony that does '
                'not yet exist on a world that is not yet habitable.'
            ),
            population=0,
        ),
        StellarObject(
            name='UPL-2281-c',
            short_description='A gas giant -- fuel processing initiated early to support the terraforming traffic, producing fuel for a colony that will not arrive for thirty years.',
            long_description=(
                'UPL-2281-c is the system\'s gas giant -- fuel processing initiated on its '
                'moons to support the terraforming traffic. The equipment runs at a '
                'fraction of the capacity it was built for because the traffic is currently '
                'limited to the engineering supply ships and the occasional inspection '
                'vessel from the colonial planning office. The full capacity will be needed '
                'when the colonists arrive. Until then, the fuel operations run quiet, '
                'producing fuel for ships that visit infrequently, maintaining equipment '
                'that was built for a future that is decades away and approaching at the '
                'speed of atmospheric chemistry.'
            ),
            population=0,
        ),
    ],
    short_description='The future -- a world being terraformed, the processors running, the colonists scheduled to arrive in thirty years, built by engineers who will never live in what they are making.',
    long_description=(
        'UPL-2281 is becoming a colony. The primary world was assessed two decades '
        'ago and the terraforming commenced fifteen years ago -- atmospheric '
        'processors, orbital mirrors, microbial seeding in the regions where the '
        'composition has reached survivable range. The timeline to habitability is '
        'approximately thirty years. The engineers update the projection annually. '
        'The colonial planners treat it as a commitment. The engineers note that '
        'terraforming timelines are projections rather than promises. The planners '
        'ignore the distinction because the settlement planning has already begun.\n\n'
        'The engineering staff live in sealed habitats on a world that is changing '
        'outside the windows -- atmospheric readings ticking toward target values '
        'month by month. The staff are building a world they will never live in. '
        'The mineral surveys on the outer world are complete, the deposits mapped, '
        'the extraction plans filed alongside settlement layouts and population '
        'projections for a colony that does not yet exist.\n\n'
        'The gas giant\'s fuel processing runs at a fraction of capacity -- built '
        'for the traffic the colony will generate, currently serving the handful '
        'of engineering supply ships. The future is approaching at the speed of '
        'atmospheric chemistry. The system waits.'
    ),
    cluster=StarClusters.POLARIS,
)


POLARIS_SYSTEMS: list[System] = [
    POLARIS, ALFIRK, ALKAID, COR_CAROLI, DUBHE, EDASICH,
    ELTANIN, GRUMIUM, UPL_1037, UPL_7741, KOCHAB, NAVI,
    PHERKAD, RASTABAN, SCHEDAR, SEGIN, THUBAN,
    UPL_2281, UPL_4479,
]
