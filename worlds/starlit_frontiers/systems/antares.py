from ..enums import StarClusters
from .models import System, StellarObject

ANTARES = System(
    name='Antares',
    star='Red supergiant (M1.5Iab), approximately 680 times Sol diameter and 10,000 times Sol luminosity -- so vast that its habitable zone is an enormous ring far from the star, with a hidden blue-white companion (B2.5V) lost in the supergiant\'s glare',
    population=25_000_000_000,
    stellar_objects=[
        StellarObject(
            name='The Band',
            short_description='The ring of worlds -- dozens of rocky bodies orbiting the supergiant in a vast habitable belt, the most densely populated orbital region in the outer systems.',
            long_description=(
                'The Band is Antares\' defining feature: a broad ring of rocky bodies '
                'orbiting the red supergiant at the enormous distance that the star\'s '
                'habitable zone demands. Where a main-sequence star\'s habitable zone '
                'contains a handful of worlds, Antares\' zone is so wide and so far out '
                'that it has swept up dozens of rocky bodies -- planets, captured asteroids, '
                'and planetesimals large enough to hold atmospheres or support enclosed '
                'habitation. The Band is not a single world. It is a ring of worlds, '
                'orbiting together in a broad belt that is the most densely populated '
                'orbital region in the outer systems.\n\n'
                'The worlds of the Band range from large, atmosphere-bearing planets that '
                'host billions to small rocky bodies with enclosed habitats supporting '
                'millions. The variety is enormous -- no two worlds in the Band are alike, '
                'and the cultural differences between them are as varied as anything in the '
                'inner systems. What unites them is the stims. Every world in the Band runs '
                'on pharmaceutical enhancement. The cognitive enhancers that make the '
                'traders sharp, the focus compounds that keep the dockworkers efficient, '
                'the reaction accelerants that make the pilots fast -- the chemistry varies '
                'by world and by occupation, but the principle is universal. An unenhanced '
                'person in the Band is not competitive in any field.\n\n'
                'The sky from the Band is dominated by the supergiant -- a vast red disc '
                'that occupies a significant arc of the sky despite the enormous distance. '
                'The star is not a point. It is a presence, deep red and enormous, dimmer '
                'than its size suggests because most of its output is infrared. The light '
                'it casts is warm, ruddy, and constant, giving the worlds of the Band a '
                'permanent amber-red illumination that the inhabitants consider normal and '
                'that visitors from the inner systems find unsettling. The blue-white '
                'companion star is invisible to the naked eye, lost in the supergiant\'s '
                'glare. The inhabitants know it is there. They cannot see it. In a system '
                'that runs on stims, there is a certain poetry in a hidden star.'
            ),
            population=8_000_000_000,
        ),
        StellarObject(
            name='Kaelin',
            short_description='The largest world in the Band and the system\'s commercial capital -- where the trade between the Antares cluster and the rest of the galaxy is conducted.',
            long_description=(
                'Kaelin is the largest and most populous single world in the Band -- a '
                'rocky planet with a thick atmosphere and conditions that are genuinely '
                'habitable without enclosed habitats, which is a distinction that matters '
                'in a ring of worlds where many require domes and seals. Kaelin is the '
                'commercial heart of the system: the world where the trade between the '
                'Antares cluster and the rest of the galaxy is negotiated, contracted, and '
                'executed.\n\n'
                'The cities on Kaelin are dense, fast, and loud in a way that reflects the '
                'stimmed culture. The population operates at enhanced speed -- conversations '
                'are faster, decisions are quicker, the pace of commerce is calibrated to '
                'people who are chemically augmented for cognitive performance. A baseline '
                'human visiting Kaelin\'s trading floors would feel slow, not because they '
                'are stupid but because everyone around them is operating at a speed that '
                'baseline neurology cannot match. The experience is described by inner-'
                'system traders as being a step behind in every conversation -- understanding '
                'the words but missing the subtext, following the argument but arriving at '
                'the conclusion after the other party has already moved on.\n\n'
                'The wealth divide is visible on Kaelin\'s streets. The wealthy districts '
                'are clean, modern, and populated by people whose stim regimes are precise '
                'and carefully managed -- clean compounds, minimal side effects, the kind '
                'of enhancement that looks like natural brilliance. The poorer districts '
                'are crowded, louder, and populated by people on cheaper stims whose '
                'effects are cruder: the tremor in the hands of a dockworker on industrial '
                'focus compounds, the paranoid edge in the voice of a courier on cheap '
                'reaction accelerants, the hollow eyes of long-term users whose bodies are '
                'burning through the enhancement faster than they can afford to replace it.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Gantry',
            short_description='The system\'s primary orbital port and military staging area -- the busiest installation in the outer systems.',
            long_description=(
                'Gantry is the system\'s main orbital station and the busiest installation '
                'in the outer systems. The station handles three overlapping streams of '
                'traffic simultaneously: the military traffic of the Antarian fleet, the '
                'civilian commercial traffic moving goods and people within the cluster, '
                'and the independent traffic flowing between the Antares cluster and the '
                'inner systems.\n\n'
                'The military presence is enormous. Antares is the gateway to the cluster, '
                'and every ship that enters or leaves passes through the system. The '
                'Antarian fleet maintains a permanent garrison: capital ships, cruisers, '
                'destroyers, and the fast frigates that are the Antarian navy\'s preferred '
                'strike weapon -- angular, aggressive vessels crewed by stimmed personnel '
                'whose reaction times exceed anything baseline crews can match. The '
                'garrison is not defensive in posture. It is a staging area. Antarian '
                'military doctrine favours speed and offence, and the fleet at Gantry is '
                'positioned to strike outward through the gateway rather than hold position '
                'against incursion.\n\n'
                'The civilian traffic is equally intense. The Antares cluster is an economic '
                'powerhouse -- the stim industry alone generates trade volumes that rival '
                'entire inner-system economies -- and Gantry processes the cargo, the '
                'passengers, and the pharmaceutical shipments that flow in and out. The '
                'station is loud, crowded, and fast. The staff are stimmed. The traders are '
                'stimmed. The dockworkers are stimmed. The pace of operations would be '
                'impossible for a baseline crew to maintain, and visiting inner-system '
                'pilots describe Gantry\'s traffic control as the most demanding docking '
                'experience in the galaxy -- instructions delivered at a speed that assumes '
                'enhanced cognition, with no accommodation for those who do not have it.\n\n'
                'MERIT warships do not dock at Gantry. MERIT and Antares are at war, and '
                'military vessels from either side that encounter the other in the gateway '
                'space engage. Independent traffic, however, flows freely -- merchants, '
                'traders, and the civilian ships that carry goods and people between the '
                'warring factions pass through Gantry under the practical understanding '
                'that commerce does not stop because governments are fighting.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Vossen',
            short_description='A world in the Band dedicated to the export trade -- finding buyers in the inner systems, fostering dependency, and weaponising addiction.',
            long_description=(
                'Vossen is the Antares cluster\'s interface with the inner systems\' drug '
                'market. The world\'s economy is built around a single mission: getting '
                'Antarian stims into the hands of inner-system consumers. The sales '
                'operations, marketing networks, and distribution channels that move '
                'Antarian pharmaceuticals into MERIT space are designed, managed, and '
                'coordinated from Vossen. The work is part commerce and part strategy: '
                'every inner-system citizen who becomes dependent on Antarian stims is a '
                'citizen whose productivity benefits Antarian suppliers, whose loyalty to '
                'MERIT is complicated by dependency, and whose withdrawal symptoms are a '
                'reminder that the Antares cluster provides something MERIT cannot.\n\n'
                'The sales networks on Vossen are sophisticated. The operatives who manage '
                'the inner-system distribution are trained in market analysis, regulatory '
                'evasion, and the art of finding legitimate-seeming channels for products '
                'that MERIT officially restricts. The stims enter the inner systems through '
                'traders, intermediaries, and the grey-market networks that exist in every '
                'system where MERIT\'s oversight is less than total. The products are '
                'positioned carefully: not as Antarian drugs -- the association with the '
                'enemy faction would limit the market -- but as performance enhancers, '
                'cognitive supplements, and productivity aids whose origin is obscured by '
                'layers of repackaging and relabelling.\n\n'
                'The Antarian government supports Vossen\'s operations with undisguised '
                'enthusiasm. The revenue is significant. The strategic value is greater. '
                'Every inner-system professional who takes a cognitive enhancer manufactured '
                'in Dschubba and sold through Vossen\'s networks is a thread of dependency '
                'that weakens MERIT\'s position and strengthens the Antares cluster\'s. The '
                'addiction is the weapon. The sales team on Vossen is, in the Antarian '
                'government\'s strategic calculus, as valuable as a warship.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Tessek',
            short_description='A military world in the Band -- the Antarian fleet\'s forward garrison, staging the ships that defend the gateway and strike into MERIT space.',
            long_description=(
                'Tessek is the Antarian fleet\'s forward garrison -- the military world '
                'closest to the gateway, where the ships that patrol and defend the cluster\'s '
                'most contested space are based, maintained, and crewed. The warships are '
                'built at Sargas\'s Docks and delivered here, where they are assigned to the '
                'gateway fleet and their crews complete the final operational training before '
                'deployment. Tessek is not where the ships are made. Tessek is where they '
                'become dangerous.\n\n'
                'The garrison is substantial -- capital ships, cruisers, destroyers, and '
                'the fast frigates that Antarian doctrine favours. The ships rotate between '
                'Tessek and the gateway on patrol schedules calibrated to the stim cycle: '
                'a ship deploys enhanced, operates at peak for the duration of the '
                'enhancement window, and returns to Tessek for the crew\'s comedown and '
                'recovery before the next deployment. The rotation is constant. The gateway '
                'is never undefended. The crews are never deployed past the point where the '
                'stims fade, because a crew in comedown is a crew that cannot fight.\n\n'
                'Tessek also serves as the staging area for offensive operations into MERIT '
                'space. When the Antarian command decides to strike -- a raid on an inner-'
                'system convoy, a probe of MERIT\'s defensive perimeter, a show of force '
                'at the gateway -- the strike force assembles at Tessek, the crews are '
                'enhanced to combat levels, and the ships depart on trajectories calculated '
                'to reach their targets within the performance window. The timing is '
                'everything. Antarian military operations are planned to the hour because '
                'the stims define the hour, and Tessek is where the clock starts.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Brennar',
            short_description='An agricultural world in the Band -- feeding twenty-five billion people under the red light of a supergiant, on stims that make the work faster and the workers expendable.',
            long_description=(
                'Brennar is the system\'s primary agricultural world -- one of the larger '
                'bodies in the Band with conditions that support farming at scale. The '
                'agricultural output feeds the system\'s twenty-five billion people, and '
                'the farming is conducted at the same enhanced pace as everything else in '
                'Antarian society. The workers are on endurance boosters and focus compounds '
                'that allow them to work longer hours at higher efficiency than any baseline '
                'farmer could sustain.\n\n'
                'The agricultural communities on Brennar are the most visible example of '
                'the stim economy\'s human cost at the bottom end. The endurance boosters '
                'that the farm workers use are industrial-grade -- cheap, effective in the '
                'short term, and physically devastating over years. The workers know this. '
                'The alternative is unemployment, because an unenhanced farm worker cannot '
                'match the output that enhanced workers produce and the employers hire '
                'accordingly. The farms produce food. The food feeds billions. The workers '
                'who produce it are burning through their bodies to remain employable, and '
                'the system considers this an acceptable cost of feeding itself.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='The Fringe',
            short_description='The outer edge of the Band -- smaller worlds, poorer populations, and the cheapest stims available in a system where cheap stims kill slowly.',
            long_description=(
                'The Fringe is the collective name for the smaller, less developed worlds '
                'at the outer edge of the Band -- rocky bodies too small for full '
                'atmospheres, hosting populations in enclosed habitats that range from '
                'adequate to grim. The Fringe is where the system\'s poorest people live: '
                'workers in mining, salvage, and the low-margin industries that the larger '
                'worlds do not want. The stims available on the Fringe are the cheapest '
                'in the system -- industrial-grade compounds shipped in bulk from '
                'Dschubba\'s factories, with quality control that meets minimum '
                'functional standards and nothing more.\n\n'
                'The Fringe populations are the system\'s underclass. The tremors, the '
                'paranoia, the organ damage, the cognitive erosion that cheap stims produce '
                'over time -- all of it is concentrated here, in communities of people who '
                'cannot afford better and cannot function without what they can afford. '
                'Withdrawal from industrial stims is medically dangerous. The Fringe has '
                'clinics that manage withdrawal for workers who want to stop. The clinics '
                'are underfunded and the waiting lists are long and the workers who '
                'successfully withdraw discover that the job market does not accommodate '
                'baseline performance. Most go back on the stims. The Fringe endures.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='The Gateway',
            short_description='The region of space where the routes to the inner systems converge -- the most contested volume in the outer systems, where MERIT and Antarian warships clash.',
            long_description=(
                'The Gateway is the volume of space where the jump routes connecting the '
                'Antares cluster to the inner systems converge. All traffic -- military, '
                'commercial, civilian -- passes through this region, and it is the most '
                'contested space in the outer systems. MERIT\'s warships patrol the inner-'
                'system side of the gateway routes. Antarian warships patrol the outer side. '
                'The space between is where the skirmishes happen.\n\n'
                'The engagements are frequent and follow the pattern that the war has '
                'established: Antarian ships strike fast, exploiting their stimmed crews\' '
                'superior reaction times, aiming to destroy or disable MERIT vessels before '
                'the enhancement window closes. MERIT ships absorb the initial assault and '
                'fight a longer engagement that favours their consistent, unenhanced '
                'performance. The Gateway is littered with the wreckage of ships from both '
                'sides -- the angular, aggressive hulls of Antarian vessels alongside the '
                'clean-lined modular construction of MERIT ships.\n\n'
                'Independent traffic navigates the Gateway with the careful skill of people '
                'who have learned to read the tactical situation from a distance. The '
                'merchants and traders who run the gateway route know the patrol patterns '
                'of both sides, know which corridors are currently active combat zones and '
                'which are quiet, and time their transits accordingly. The route is '
                'profitable because it is dangerous, and the traders who fly it charge '
                'accordingly.'
            ),
            population=0,
        ),
        StellarObject(
            name='Durren',
            short_description='A gas giant inside the Band\'s orbit -- fuel processing and the hidden companion star\'s closest visible influence.',
            long_description=(
                'Durren is a large gas giant orbiting inside the Band -- closer to the '
                'supergiant, in a region too hot for habitation but suitable for fuel '
                'processing. The moons of Durren host fuel operations that service the '
                'system\'s enormous traffic volume -- military, commercial, and civilian '
                'ships all require fuel, and the demand in a system of twenty-five billion '
                'people with a major military garrison is immense.\n\n'
                'Durren is also the point in the system where the hidden companion star\'s '
                'influence is most detectable. Antares B -- the blue-white star lost in '
                'the supergiant\'s glare -- orbits close enough that its gravitational '
                'effects on Durren\'s orbit are measurable, and on rare occasions when the '
                'orbital geometry is favourable, the companion\'s light can be separated '
                'from the supergiant\'s output by instruments on Durren\'s inner moons. The '
                'blue light of the hidden star, seen briefly through the red glare, is '
                'considered a novelty by the fuel workers and a research opportunity by the '
                'astronomers. Neither group lingers -- the radiation environment close to '
                'the supergiant is hostile, and Durren\'s moons are working installations '
                'rather than comfortable postings.'
            ),
            population=200_000_000,
        ),
    ],
    short_description='Gateway to the Stimmed -- a red supergiant surrounded by a ring of worlds where twenty-five billion people live fast, work enhanced, and burn through themselves to keep up.',
    long_description=(
        'Antares is the heart of the Stimmed and the gateway to their cluster. The '
        'star is a red supergiant -- 680 times Sol\'s diameter, so vast that its '
        'habitable zone is an enormous ring far from the stellar surface, containing '
        'dozens of rocky bodies that form the Band: the most densely populated orbital '
        'region in the outer systems. Twenty-five billion people live in the Band, on '
        'worlds that range from large, atmosphere-bearing planets to small enclosed '
        'habitats, all of them united by the pharmaceutical culture that defines '
        'Antarian society. Everyone is on stims. Everyone has been on stims since '
        'childhood. The unenhanced are not persecuted. They are irrelevant.\n\n'
        'The system is busy in every sense. Gantry, the orbital station, processes '
        'three overlapping traffic streams: the Antarian military fleet, the civilian '
        'commerce of the cluster, and the independent traffic flowing between Antarian '
        'space and the inner systems. The military presence is enormous -- capital '
        'ships, cruisers, and the fast, aggressive frigates that Antarian doctrine '
        'favours, crewed by stimmed personnel whose reaction times exceed anything '
        'baseline humans can match. The Gateway -- the contested space where the routes '
        'to the inner systems converge -- is the most active combat zone in the outer '
        'systems, where Antarian and MERIT warships clash in engagements that follow '
        'the war\'s established rhythm: Antarian speed against MERIT endurance, '
        'stimmed burst against baseline consistency.\n\n'
        'The commerce is equally intense. The stim industry alone generates trade '
        'volumes that rival entire inner-system economies. The compounds are '
        'manufactured in Dschubba and consumed across the cluster -- from the clean, '
        'precise formulations that the wealthy use without consequence to the crude '
        'industrial-grade products that the poor burn through their bodies to remain '
        'employable. Vossen\'s operatives push the products into the inner systems, '
        'fostering dependency that weakens MERIT and generates revenue simultaneously. '
        'Kaelin\'s trading floors operate at enhanced speed, conducting '
        'commerce at a pace that baseline visitors cannot match. The wealth divide is '
        'visible in every district: the wealthy enhanced with precision and grace, the '
        'poor enhanced with power and tremors.\n\n'
        'The supergiant dominates the sky -- a vast red disc that is not a point of '
        'light but a presence, casting the entire system in warm, ruddy illumination '
        'that the inhabitants consider normal. The hidden companion star is invisible '
        'in the glare. The system runs at a pace that the inner systems would find '
        'exhausting and that Antarian society considers baseline. Twenty-five billion '
        'people, chemically enhanced, commercially aggressive, militarily dangerous, '
        'living fast under a dying star that is itself burning through its own material '
        'faster than it can sustain. The parallel is there. Nobody in Antares '
        'acknowledges it.'
    ),
    cluster=StarClusters.ANTARES,
)

DSCHUBBA = System(
    name='Dschubba',
    star='Hot blue-white subgiant (B0.3IV), approximately 14,000 times Sol luminosity -- unpredictably variable, with occasional brightening events when the companion star makes a close pass',
    population=20_000_000_000,
    distance_to_sol=490.0,
    stellar_objects=[
        StellarObject(
            name='Osaren',
            short_description='The wealthiest world in the Antares cluster -- where the pharmaceutical corporations are headquartered and the money from the stim trade accumulates.',
            long_description=(
                'Osaren is where the money lives. The planet is the administrative and '
                'financial centre of the Antares cluster\'s pharmaceutical industry -- the '
                'corporations that manufacture, formulate, and sell the stims that the '
                'entire cluster depends on are headquartered here, and the wealth they '
                'generate is visible in every street. The cities on Osaren are the most '
                'opulent in the outer systems -- architecture designed to project success, '
                'public spaces maintained to a standard that rivals Altair\'s Concord, and '
                'a population that is, on average, the wealthiest in the Antares cluster '
                'by a significant margin.\n\n'
                'The corporate executives and senior researchers on Osaren use the finest '
                'stims available -- compounds so precisely formulated that the enhancement '
                'is seamless and the side effects are functionally zero. These are not the '
                'industrial-grade products that the factory workers on other worlds burn '
                'through. These are bespoke formulations, tailored to individual '
                'neurochemistry, managed by personal pharmaceutical consultants who '
                'monitor their clients\' health with a care that the cluster\'s poor could '
                'not imagine. The executives who run the stim industry are the best '
                'advertisement for their own product: sharp, healthy, energetic, ageing '
                'gracefully. The fact that this version of the product is available only '
                'to those who can afford it is not something they discuss.\n\n'
                'The political power in the Antares cluster is concentrated on Osaren. The '
                'corporations that control the stim supply control the cluster -- not '
                'through formal governance but through the simple leverage of a product '
                'that the entire population depends on. The Antarian government exists and '
                'functions, but its decisions are shaped by the corporations whose revenue '
                'funds the military, the infrastructure, and the economy. The relationship '
                'is not secret. It is simply how Antarian society works: the people who '
                'make the drugs make the decisions.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='The Furnaces',
            short_description='The manufacturing worlds -- a chain of heavily industrialised planets where the cluster\'s stim supply is synthesised at a scale that defies comprehension.',
            long_description=(
                'The Furnaces are a group of rocky worlds in Dschubba\'s habitable zone '
                'that have been given over entirely to pharmaceutical manufacturing. The '
                'worlds are not habitable in the conventional sense -- the atmospheres are '
                'breathable but the surfaces are industrial landscapes of factory complexes, '
                'chemical processing plants, synthesis laboratories, and the logistics '
                'infrastructure that moves raw materials in and finished product out. The '
                'scale is difficult to grasp. The Furnaces produce the stims consumed by '
                'the entire Antares cluster -- tens of billions of daily doses across '
                'dozens of systems, in hundreds of formulations, at quality levels ranging '
                'from bespoke executive-grade to bulk industrial.\n\n'
                'The factories operate continuously. The workforce is enormous -- billions '
                'of people working in facilities that range from the sterile, precision-'
                'controlled laboratories that produce the premium compounds to the vast '
                'bulk synthesis plants that churn out industrial-grade product by the '
                'tonne. The workers are on stims. The factory floors are calibrated for '
                'enhanced performance. The production targets assume enhanced productivity. '
                'A stimmed workforce producing the stims that the workforce depends on, '
                'at a scale that feeds an entire cluster\'s addiction -- the circularity '
                'is total and the system is self-sustaining in the most literal sense.\n\n'
                'The wealth divide is manufactured here. The same companies, the same '
                'factories, the same supply chains produce the clean compounds that keep '
                'the wealthy sharp and the crude products that burn through the poor. The '
                'difference is quality control, ingredient purity, and the time invested '
                'in formulation -- which is to say, the difference is cost, and cost is '
                'the only variable that Antarian society uses to sort its citizens.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Velleren',
            short_description='The research world -- where the next generation of stims is developed, tested, and approved by the corporations that will profit from them.',
            long_description=(
                'Velleren is the Antares cluster\'s pharmaceutical research centre -- the '
                'world where new stim formulations are developed, tested, and refined before '
                'being approved for production on the Furnaces. The research institutions '
                'on Velleren are the most advanced in the outer systems, funded by the '
                'pharmaceutical corporations whose profits depend on a constant stream of '
                'improved, more effective, more addictive products.\n\n'
                'The research is genuinely sophisticated. The neuroscience conducted on '
                'Velleren is the best in the galaxy -- the understanding of human '
                'neurochemistry, cognitive enhancement, and the interaction between '
                'pharmaceutical compounds and the human nervous system exceeds anything '
                'produced in the inner systems. MERIT\'s medical researchers acknowledge '
                'this with discomfort. The science is brilliant. The application of the '
                'science is a society in which abstinence means destitution.\n\n'
                'The researchers on Velleren are the cluster\'s aristocracy -- the most '
                'valued professionals in a society that values pharmaceutical innovation '
                'above everything else. They live well, they work on the finest stims '
                'available, and they produce the compounds that will shape the next '
                'generation\'s experience of enhancement. The ethical questions that MERIT '
                'raises about the stim culture are not debated on Velleren. They are '
                'considered. They are understood. They are filed under concerns that do '
                'not affect the research budget.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Ashavar',
            short_description='An agricultural world feeding the system\'s twenty billion -- the farms enhanced, the farmers enhanced, the output staggering.',
            long_description=(
                'Ashavar is Dschubba\'s agricultural world -- a large, fertile planet whose '
                'output feeds a system of twenty billion people and exports surplus to other '
                'systems in the cluster. The farming is conducted at enhanced efficiency: '
                'the agricultural workers are on endurance boosters and focus compounds, '
                'the crop strains are engineered for maximum yield, and the growing cycles '
                'are managed by logistics systems that optimise every hectare.\n\n'
                'Ashavar\'s farms are productive in a way that inner-system agricultural '
                'worlds cannot match -- the combination of enhanced workers, engineered '
                'crops, and relentless optimisation produces yields per hectare that Sheratan '
                'would envy. The cost is the same as everywhere in the Antares cluster: the '
                'workers who produce the food are on cheap industrial stims that degrade '
                'their health over time, because the productivity targets are set for '
                'enhanced workers and baseline performance means unemployment. The farms '
                'are beautiful from orbit -- vast, geometric, efficient. The workers are '
                'less beautiful up close.'
            ),
            population=2_800_000_000,
        ),
        StellarObject(
            name='Pinnacle',
            short_description='The system\'s orbital port -- the second busiest in the cluster after Antares\' Gantry, processing the pharmaceutical trade that feeds the outer systems.',
            long_description=(
                'Pinnacle is Dschubba\'s primary orbital station -- an enormous facility '
                'that handles the system\'s vast trade volume. The traffic is relentless: '
                'freighters arriving with raw materials for the Furnaces, freighters '
                'departing loaded with finished pharmaceutical product destined for every '
                'system in the cluster, passenger transports carrying the workforce that '
                'the factories consume, and the corporate traffic of executives, '
                'researchers, and the financial specialists who manage the industry\'s '
                'enormous revenue.\n\n'
                'Pinnacle is the second busiest installation in the Antares cluster, after '
                'Gantry in the Antares system itself. The difference is character: Gantry '
                'handles military, commercial, and independent traffic in equal measure. '
                'Pinnacle is almost entirely commercial -- the pharmaceutical trade is so '
                'dominant that the military presence is modest, limited to the escort '
                'vessels that protect the high-value pharmaceutical shipments and the '
                'customs enforcement that ensures the trade flows through official channels '
                'rather than being diverted by the smugglers and counterfeiters who '
                'would love to get their hands on Dschubba\'s output.\n\n'
                'The station\'s commercial district caters to the wealthy -- the corporate '
                'travellers and senior researchers whose expenses are covered by the '
                'pharmaceutical companies. The restaurants are excellent. The accommodations '
                'are luxurious. The stim dispensaries in the commercial district offer '
                'formulations that are not available anywhere else in the cluster at any '
                'price, because Pinnacle is where the newest products are soft-launched '
                'before cluster-wide distribution. The wealthy try the latest compounds '
                'here first. The results of their experience determine what the rest of '
                'the cluster will be taking next year.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='The Undercroft',
            short_description='The worker habitats beneath the Furnaces\' factories -- where the manufacturing workforce lives in conditions that the executives on Osaren prefer not to see.',
            long_description=(
                'The Undercroft is the collective name for the residential infrastructure '
                'beneath and between the Furnaces\' factory complexes -- the habitats where '
                'the manufacturing workforce lives. The Undercroft sprawls across the '
                'Furnaces\' worlds -- the underside of the manufacturing operation, '
                'compressed into the spaces between the industrial complexes. Three billion '
                'people live in the Undercroft, and their experience of Dschubba is '
                'entirely different from the executives on Osaren or the researchers on '
                'Velleren.\n\n'
                'The conditions vary from adequate to grim. The better habitats -- provided '
                'by the larger corporations for their skilled workers -- are functional, '
                'clean, and equipped with medical facilities that manage the health effects '
                'of long-term stim use. The worse habitats -- housing the unskilled bulk '
                'workforce of the synthesis plants -- are crowded, poorly ventilated, and '
                'maintained to a standard that would be illegal in the inner systems. The '
                'workers live on the stims they produce. The medical care available to them '
                'is calibrated to keep them functional rather than healthy, because '
                'functional is what the production targets require.\n\n'
                'The Undercroft is where the human cost of the Antares cluster\'s '
                'pharmaceutical economy is most concentrated. The tremors, the paranoia, '
                'the organ damage, the cognitive erosion -- all of it is visible here, in '
                'the faces and hands and voices of people who make the drugs that are '
                'making them sick. The corporations provide the stims. The stims keep the '
                'workers productive. The productivity funds the corporations. The cycle is '
                'closed and self-perpetuating and nobody inside it has the leverage to '
                'break it.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Vasthen',
            short_description='A gas giant whose moons process fuel and host the chemical feedstock operations that supply the Furnaces\' raw materials.',
            long_description=(
                'Vasthen is a large gas giant in the outer system whose moons serve double '
                'duty: fuel processing for the system\'s enormous traffic, and chemical '
                'feedstock production for the Furnaces. Many of the precursor compounds '
                'used in stim synthesis are derived from atmospheric gases -- hydrogen, '
                'nitrogen, methane, and trace compounds that are processed on Vasthen\'s '
                'moons into the chemical building blocks that the factories on the '
                'Furnaces assemble into finished pharmaceuticals. The feedstock operations '
                'are industrial in scale and essential to the manufacturing chain -- a '
                'disruption at Vasthen would halt production on the Furnaces within '
                'weeks.\n\n'
                'The workers on Vasthen\'s moons are chemical engineers and processing '
                'technicians -- skilled labour on better stims than the bulk workforce on '
                'the Furnaces, because the work is technical and errors in feedstock '
                'production propagate through the entire manufacturing chain. The '
                'corporations invest in Vasthen\'s workforce because the cost of a '
                'feedstock error exceeds the cost of premium stims for the engineers. '
                'The calculus is transparent. The engineers do not pretend it is anything '
                'other than what it is.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Kindling',
            short_description='A hot inner world -- energy collection that powers the Furnaces\' manufacturing, named with an optimism that the conditions do not support.',
            long_description=(
                'Kindling is a hot, dense world close to Dschubba\'s searing blue-white '
                'star -- solar collection arrays harvesting the star\'s enormous output to '
                'power the Furnaces\' manufacturing operations. The star\'s 14,000 times '
                'Sol luminosity means the energy available at collection distance is vast, '
                'and the arrays on Kindling supply a significant fraction of the system\'s '
                'industrial energy demand.\n\n'
                'The star\'s unpredictable variability complicates the operation. Dschubba '
                'occasionally brightens when its companion star makes a close pass, and '
                'the energy spike can overwhelm collection systems that are not designed '
                'for the surge. The engineers on Kindling have learned to predict the '
                'brightening events with reasonable accuracy and adjust the arrays '
                'accordingly, but the margin for error is small and the consequences of '
                'misjudging a surge are expensive. The work is demanding, the conditions '
                'are harsh, and the posting is filled by engineers who are on the best '
                'focus compounds the corporations provide, because a mistake here costs '
                'the factories downtime and the factories do not tolerate downtime.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='The factory of the Stimmed -- where the drugs that an entire cluster depends on are manufactured at a scale that makes the wealth divide visible from orbit.',
    long_description=(
        'Dschubba is where the stims come from. The system is the Antares cluster\'s '
        'pharmaceutical manufacturing centre -- the Furnaces, a chain of heavily '
        'industrialised worlds, produce the tens of billions of daily doses that the '
        'cluster\'s population depends on. Every cognitive enhancer, every focus '
        'compound, every endurance booster, every reaction accelerant consumed in '
        'Antarian space was synthesised in Dschubba\'s factories and shipped outward '
        'through a distribution network that reaches every inhabited world in the '
        'cluster. The system is the wealthiest in the Antares cluster because it '
        'controls the supply of the one product that Antarian society cannot function '
        'without.\n\n'
        'Twenty billion people live in Dschubba. The wealth divide between them is the '
        'starkest in the outer systems. On Osaren, the corporate executives and senior '
        'researchers live in opulence that rivals the inner systems, using bespoke stim '
        'formulations tailored to their individual neurochemistry by personal '
        'pharmaceutical consultants. In the Undercroft -- the worker habitats beneath '
        'the Furnaces\' factories -- the manufacturing workforce lives in conditions '
        'ranging from adequate to grim, on the industrial-grade products they produce, '
        'their health managed to the standard of functional rather than well.\n\n'
        'The star is a searing blue-white subgiant -- 14,000 times Sol\'s luminosity, '
        'compact and brilliant and unpredictably variable. The contrast with Antares\' '
        'vast, dim red supergiant is total: where Antares is enormous and slow, '
        'Dschubba is bright and volatile. The metaphor is convenient -- the system that '
        'manufactures the stims burns hotter than the system that consumes them -- but '
        'the residents do not think in metaphors. They think in production quotas, '
        'quarterly revenues, and the relentless logistics of supplying a product that '
        'tens of billions of people need every day and will become medically dangerous '
        'without.\n\n'
        'The pharmaceutical corporations that control Dschubba are the real power in '
        'the Antares cluster. The Antarian government functions but its decisions are '
        'shaped by the corporations whose revenue funds the military, the '
        'infrastructure, and the economy. The people who make the drugs make the '
        'decisions. The neuroscience produced on Velleren is the best in the galaxy. '
        'The ethics of applying that neuroscience to a society where sobriety means '
        'unemployment are not debated in Dschubba. They are understood and filed under '
        'concerns that do not affect the production schedule.'
    ),
    cluster=StarClusters.ANTARES,
)

ACRAB = System(
    name='Acrab',
    star='Sextuple system: three binary pairs, with the primary pair dominated by a bright blue-white main sequence star (B1V)',
    population=12_000_000_000,
    distance_to_sol=530.0,
    stellar_objects=[
        StellarObject(
            name='Talwen',
            short_description='The most populous world -- a warm, fertile planet that feeds a significant fraction of the Antares cluster on stim-enhanced farming.',
            long_description=(
                'Talwen is the breadbasket of the Antares cluster. The planet is warm, '
                'fertile, and blessed with the kind of growing conditions that agricultural '
                'engineers describe as cooperative -- deep soil, reliable rainfall, a '
                'climate that supports multiple growing seasons per year across most of '
                'the arable surface. The output is enormous. Talwen feeds its own five '
                'billion people and exports a surplus that supports populations on Antares, '
                'Dschubba, and a half-dozen other systems in the cluster whose economies '
                'are oriented toward industry, military, or pharmaceuticals rather than '
                'food production.\n\n'
                'The farming on Talwen is not planned to the acre the way Sheratan\'s '
                'mathematical grids are. The Antarian approach is less systematic and more '
                'aggressive: enhanced workers on endurance boosters and focus compounds '
                'pushing longer hours and faster cycles than baseline agriculture could '
                'sustain. The crop strains are engineered for yield but the planting is '
                'decided by local operators rather than system-wide optimisation algorithms. '
                'The result is productive but uneven -- some regions are meticulously '
                'managed by operators on premium stims whose focus is surgical, while '
                'others are worked hard by labourers on cheap compounds whose judgment '
                'degrades over a season and whose fields show it.\n\n'
                'The wealth divide on Talwen follows the stim divide. The large-scale '
                'operators who can afford quality enhancement run precision agriculture '
                'that approaches inner-system standards. The smallholders and contract '
                'labourers on industrial-grade compounds produce lower-quality output at '
                'higher personal cost -- tremors in the hands that plant the seeds, '
                'paranoia that makes cooperation difficult, the slow erosion that every '
                'cheap-stim worker in the cluster knows and accepts because the alternative '
                'is not being able to work at all.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Borasa',
            short_description='The second agricultural world -- cooler, drier, specialising in grain crops that thrive in conditions Talwen\'s tropical climate cannot provide.',
            long_description=(
                'Borasa is the system\'s second major agricultural world -- cooler than '
                'Talwen, with broad steppe plains and a drier climate that supports the '
                'grain crops and hardy staples that form the caloric foundation of the '
                'cluster\'s diet. Where Talwen produces the variety -- fruits, vegetables, '
                'the high-value crops that the wealthy consume -- Borasa produces the '
                'volume. The grain output from Borasa\'s plains is measured in billions of '
                'tonnes per cycle, and the logistical operation that moves it from the '
                'fields to the orbital processing facilities to the freighters that carry '
                'it across the cluster is one of the largest in the outer systems.\n\n'
                'The farming communities on Borasa are large, spread across the plains, '
                'and shaped by the particular character of grain farming at scale: seasonal '
                'rhythms, long hours during planting and harvest, and the downtime between '
                'cycles when the workers rest and the stims are reduced to maintenance '
                'doses. The seasonal rhythm gives Borasa a different feel from Talwen\'s '
                'continuous production -- the planet breathes with its growing cycle in a '
                'way that the year-round farming worlds do not.\n\n'
                'Borasa\'s residents are proud of their work in the straightforward way of '
                'people who grow food and know it matters. The pride is less complicated '
                'here than on the manufacturing worlds or the military installations -- '
                'nobody questions whether growing food is worthwhile. The farmers of Borasa '
                'feed the cluster. The cluster is fed. The transaction is simple, and the '
                'simplicity is a relief in a civilisation that complicates everything else '
                'with chemistry.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Kelther',
            short_description='A warm ocean world -- aquaculture on a massive scale, feeding the cluster\'s protein demand from fish farms that stretch across shallow seas.',
            long_description=(
                'Kelther is a warm ocean world -- shallow seas covering most of the surface, '
                'with scattered island continents and a climate that supports aquaculture at '
                'a scale unmatched in the outer systems. The fish farms and kelp operations '
                'on Kelther produce the protein and marine nutrients that supplement the '
                'grain and produce from Talwen and Borasa, completing the dietary base '
                'that feeds the Antares cluster.\n\n'
                'The aquaculture is industrial -- vast enclosed sea farms managed by '
                'workers on focus compounds who monitor water chemistry, feeding schedules, '
                'and growth rates with enhanced precision. The operations are efficient but '
                'not gentle: the fish stocks are engineered for rapid growth, the kelp '
                'strains are selected for caloric density, and the sea farms are managed '
                'for maximum output rather than ecological balance. The natural marine '
                'ecosystems that existed before colonisation have been displaced by the '
                'farming operations in most of the shallow seas. The deeper ocean remains '
                'untouched, largely because it is not economically useful.\n\n'
                'Kelther\'s island communities are the system\'s most distinctive culture -- '
                'maritime, independent-minded, and shaped by the ocean in ways that the '
                'inland farming populations of Talwen and Borasa do not share. The island '
                'residents consider themselves tougher and more practical than the dirt '
                'farmers, a claim that the dirt farmers consider laughable but do not '
                'bother to contest because the argument is not worth the time.'
            ),
            population=1_800_000_000,
        ),
        StellarObject(
            name='Harben Station',
            short_description='The system\'s orbital processing and export hub -- where the agricultural output is packaged and shipped to the rest of the cluster.',
            long_description=(
                'Harben Station is the system\'s primary orbital facility -- a large '
                'installation handling the processing, packaging, and export of Acrab\'s '
                'agricultural output. The throughput is enormous: grain from Borasa, '
                'produce from Talwen, protein from Kelther, all arriving via orbital '
                'elevators and shuttle traffic, processed in the station\'s industrial '
                'sections, and loaded onto the freighters that carry it to Antares, '
                'Dschubba, and the rest of the cluster.\n\n'
                'The station is busy in the functional, unglamorous way of logistics '
                'infrastructure. The commercial district serves the freighter crews and '
                'the processing workers -- practical establishments catering to people '
                'who are passing through rather than staying. The traffic is steady and '
                'seasonal, peaking during Borasa\'s harvest cycles when the grain output '
                'floods the processing bays and the freighter queue extends beyond the '
                'station\'s docking capacity. During peak harvest, Harben Station is '
                'one of the busiest installations in the cluster. Between harvests, it '
                'is merely busy.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Kessik',
            short_description='A cold industrial world -- light manufacturing and food processing equipment, supplying the machinery that the agricultural worlds consume.',
            long_description=(
                'Kessik is a cold, rocky world in the outer habitable zone that hosts the '
                'system\'s industrial base -- manufacturing the equipment, vehicles, '
                'processing machinery, and agricultural technology that the farming worlds '
                'consume. The factories on Kessik are modest compared to the Furnaces on '
                'Dschubba or the industrial worlds of the inner systems, but they produce '
                'what the system needs: harvesters, irrigation systems, aquaculture '
                'enclosures, and the thousand mundane manufactured goods that agriculture '
                'at scale requires.\n\n'
                'Kessik\'s population is smaller than the agricultural worlds and '
                'culturally different -- factory workers rather than farmers, urban rather '
                'than rural, and operating on the focus compounds and cognitive enhancers '
                'that precision manufacturing requires. The relationship between Kessik and '
                'the farming worlds is symbiotic and slightly resentful: the farmers '
                'consider Kessik\'s factory workers soft. The factory workers consider the '
                'farmers unsophisticated. Both need each other and neither enjoys admitting '
                'it.'
            ),
            population=900_000_000,
        ),
        StellarObject(
            name='Palloway',
            short_description='A gas giant whose moons host fuel processing for the freighter fleet that carries the cluster\'s food supply.',
            long_description=(
                'Palloway is the system\'s gas giant -- a large body in the outer system '
                'with moons that host fuel processing operations sized for the freighter '
                'traffic that Acrab\'s agricultural exports generate. The fuel demand is '
                'substantial: dozens of large freighters depart daily during peak season, '
                'each carrying thousands of tonnes of processed food to systems across the '
                'cluster. The fuel workers on Palloway\'s moons keep the fleet fuelled with '
                'the steady efficiency of people who understand that a fuel shortage means '
                'a food shortage somewhere else.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Durat',
            short_description='A hot inner world -- solar collection supplementing the system\'s energy needs, unremarkable and functional.',
            long_description=(
                'Durat is a hot, dense inner world with solar collection arrays that '
                'supplement the system\'s energy needs. The arrays are adequate and '
                'unremarkable. The engineering crews maintain them efficiently and without '
                'fanfare. In a system whose identity is food production, the energy '
                'infrastructure is background -- essential and invisible, the way plumbing '
                'is essential and invisible. The crews do not mind. Invisible and essential '
                'is a comfortable place to be.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='The breadbasket of the Antares cluster -- three agricultural worlds feeding tens of billions across the Stimmed\'s territory.',
    long_description=(
        'Acrab feeds the Antares cluster. Three worlds -- Talwen, Borasa, and Kelther '
        '-- produce the food that sustains the tens of billions of people across '
        'Antarian space whose systems are oriented toward pharmaceuticals, industry, '
        'and military rather than agriculture. The output is enormous: grain from '
        'Borasa\'s steppe plains, produce from Talwen\'s tropical farms, protein from '
        'Kelther\'s shallow-sea aquaculture, all processed and shipped through '
        'Harben Station to the rest of the cluster on a freighter fleet that '
        'operates year-round.\n\n'
        'The farming is productive but not as efficient or as planned as the best '
        'inner-system agricultural worlds. Sheratan\'s mathematical precision and '
        'planet-scale optimisation are not replicated here. The Antarian approach is '
        'less systematic: enhanced workers pushing longer hours and faster cycles than '
        'baseline farming could sustain, crop strains engineered for yield, and '
        'management decisions made by local operators rather than system-wide '
        'algorithms. The result is high output with high variance -- precision '
        'agriculture from the large operators on premium stims alongside rougher '
        'production from the labourers on cheap compounds whose fields show the '
        'effects of degrading focus over a season.\n\n'
        'Twelve billion people live in Acrab, and the system\'s character is simpler '
        'than most in the cluster. The pharmaceutical politics, the military posturing, '
        'the corporate maneuvering that define Antares and Dschubba are less prominent '
        'here. Acrab grows food. The food feeds the cluster. The work is hard, the '
        'stims are the same as everywhere in Antarian space, and the farmers carry the '
        'same costs as every enhanced worker in the cluster. But there is a '
        'directness to agricultural work that the pharmaceutical factories and trading '
        'floors do not share, and the people of Acrab take a quiet satisfaction in '
        'the knowledge that whatever else the cluster does, it does it on a full '
        'stomach that Acrab provided.'
    ),
    cluster=StarClusters.ANTARES,
)

SHAULA = System(
    name='Shaula',
    star='Triple system dominated by a blue-white subgiant (B2IV), approximately 35,000 times Sol luminosity',
    population=18_000_000_000,
    distance_to_sol=570.0,
    stellar_objects=[
        StellarObject(
            name='Kothane',
            short_description='The most populous world -- nine billion people in conditions that the inner systems would call a humanitarian crisis and the Antares cluster calls normal.',
            long_description=(
                'Kothane is the most populated world in Shaula and one of the most densely '
                'inhabited in the outer systems. Nine billion people live in cities that '
                'were never planned for this many, in housing that was never built for this '
                'density, under conditions that deteriorate with every generation as the '
                'population grows and the infrastructure does not. The planet is habitable '
                '-- breathable atmosphere, adequate water, a climate that is hot and humid '
                'but survivable. The problem is not the planet. The problem is that nine '
                'billion people are living on a world whose infrastructure was built for '
                'three billion and has never been expanded to match.\n\n'
                'The cities are overcrowded in ways that defy description. The housing is '
                'stacked -- improvised vertical extensions built on top of structures that '
                'were not designed to bear them, held together by engineering that ranges '
                'from competent to terrifying. The streets at ground level are permanent '
                'twilight, shadowed by the layers above. The sanitation is inadequate. The '
                'medical facilities are overwhelmed. The food is sufficient in calories '
                'and deficient in everything else -- bulk grain from Acrab, processed into '
                'the cheapest possible forms, distributed through systems that work only '
                'because the alternative is riots.\n\n'
                'The stims on Kothane are the worst in the cluster. The population cannot '
                'afford even the standard industrial-grade compounds -- what is available '
                'is the residue of the supply chain, the products that did not meet minimum '
                'quality standards for sale elsewhere and were diverted to Shaula where '
                'the standards are lower. The side effects are severe and onset is fast. '
                'A young worker on Kothane\'s cheapest stims begins to show tremors within '
                'months, not years. The cognitive erosion is measurable within a year. The '
                'life expectancy on Kothane is decades below the cluster average, which '
                'is itself decades below the inner-system average. People are born, they '
                'work, they degrade, they die. The cycle is fast.\n\n'
                'The birth rate is the highest in the cluster. Children are an economic '
                'necessity -- more hands to work, more income in a household where every '
                'credit counts, and the knowledge that some of the children will not '
                'survive to working age and the family needs those who do. The children '
                'start on developmental stims earlier than anywhere else in the cluster '
                'because the competition for work begins earlier. A child on Kothane is '
                'economically active by the age that an inner-system child is choosing '
                'which school to attend.'
            ),
            population=9_000_000_000,
        ),
        StellarObject(
            name='Tessavar',
            short_description='The second world -- marginally less overcrowded than Kothane, marginally less desperate, and the source of most of the cluster\'s indentured labour.',
            long_description=(
                'Tessavar is the system\'s second populated world -- cooler than Kothane, '
                'with a thinner atmosphere and conditions that require more infrastructure '
                'to sustain habitation. The infrastructure exists but is stretched as thin '
                'as Kothane\'s -- the population has grown past what the systems can '
                'support, and the result is the same grinding overcrowding and the same '
                'desperate economics.\n\n'
                'Tessavar is where the labour contracts originate. The recruiters from the '
                'other Antarian systems come to Tessavar because Tessavar\'s population is '
                'desperate enough to sign and literate enough to understand what they are '
                'signing, which is the combination the recruiters need. The contracts are '
                'indentured servitude: passage to another system, housing, stims, and a '
                'wage, in exchange for a fixed term of labour at rates that the workers '
                'cannot negotiate. The terms are legal under Antarian law. The terms are '
                'also exploitative in ways that the workers understand and accept because '
                'the alternative is Tessavar.\n\n'
                'The recruiting offices line the streets of Tessavar\'s major cities -- '
                'clean, well-lit facilities staffed by professionals who explain the '
                'contracts with the careful courtesy of people selling something the buyer '
                'cannot refuse. The contracts vary: factory work on Dschubba\'s Furnaces, '
                'agricultural labour on Acrab, military service in the Antarian fleet, '
                'domestic service for the wealthy on Osaren. The workers sign. They leave. '
                'Some return when their terms are complete, with enough savings to live '
                'slightly better than before. Many do not return because the terms are '
                'extended for debts incurred during service -- medical costs, stim costs, '
                'equipment costs, housing costs that were not included in the original '
                'contract but were added through clauses that the workers understood when '
                'they signed and could not afford to refuse. The indenture that was '
                'supposed to be temporary becomes permanent. The workers know this happens. '
                'They sign anyway. Tessavar is worse.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Kellum',
            short_description='A hot, arid world settled because the other two were full -- the newest and most desperate of Shaula\'s populated worlds.',
            long_description=(
                'Kellum is the system\'s third populated world -- a hot, arid planet that '
                'was not colonised by choice but by overflow. When Kothane and Tessavar\'s '
                'populations grew past what even their degraded infrastructure could '
                'contain, the excess moved to Kellum because it was the only remaining '
                'habitable option. The planet is marginal: hot, dry, with water scarcity '
                'that makes agriculture difficult and living conditions harsher than the '
                'other worlds.\n\n'
                'Kellum\'s settlements are the rawest in the system -- newer, less '
                'established, built by people who arrived with nothing and built with '
                'whatever they could find. The water rationing is constant. The food '
                'supply is dependent on imports from the other worlds, which makes '
                'Kellum\'s population vulnerable to any disruption in the supply chain. '
                'The stims available here are even worse than Kothane\'s -- the supply '
                'chain\'s dregs, compounds so crude that the medical effects are visible '
                'within weeks of first use.\n\n'
                'Kellum is where hope goes to die. The residents of Kothane and Tessavar '
                'describe their lives as hard but survivable. The residents of Kellum '
                'describe their lives in shorter terms. The recruiting offices on Kellum '
                'do the best business in the system, because the indenture contracts that '
                'look exploitative from the outside look like rescue from the inside.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Burden Station',
            short_description='The system\'s orbital port -- where the labour transports dock, the contracts are processed, and the indentured workers depart for lives that are better than this one.',
            long_description=(
                'Burden Station is the system\'s primary orbital facility -- a large, '
                'overcrowded installation that handles Shaula\'s traffic. The traffic is '
                'distinctive: inbound freighters carrying the food and basic supplies that '
                'the system\'s population depends on, and outbound transports carrying the '
                'indentured workers to their contract destinations across the cluster. The '
                'labour transports are the station\'s signature -- large, functional vessels '
                'operated by the recruiting corporations, loading hundreds of thousands of '
                'workers per cycle and shipping them to the factories, farms, and '
                'installations that their contracts specify.\n\n'
                'The processing halls on Burden Station are where the contracts become '
                'real. The workers who signed in the recruiting offices on the surface '
                'arrive at the station, are processed through medical screening -- cursory '
                'enough to confirm they can work, thorough enough to identify conditions '
                'that would make them a liability -- and are assigned to transports. The '
                'screening rejects a percentage. The rejected are returned to the surface '
                'with their contracts voided. They are the unluckiest people in the system, '
                'which is a distinction that requires effort in Shaula.\n\n'
                'The station is grim. The facilities are functional and nothing more. The '
                'staff who process the workers have learned to do the job without looking '
                'too closely at the faces, because the faces are young and frightened and '
                'hopeful and the staff know what the contracts actually mean.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Vinthem',
            short_description='A gas giant whose fuel processing is run by indentured workers on the worst contracts available -- the posting nobody volunteers for.',
            long_description=(
                'Vinthem is the system\'s gas giant -- fuel processing on its moons '
                'supporting the transport traffic that moves workers and supplies in and '
                'out of the system. The fuel operations are staffed by indentured workers '
                'on the cheapest contracts the recruiting corporations offer -- the '
                'contracts that workers sign when they have been rejected from everything '
                'else. Fuel processing on Vinthem\'s moons is hard, isolated, and dangerous, '
                'conducted in enclosed facilities on airless rocks with equipment that is '
                'maintained to the minimum standard that keeps it operational.\n\n'
                'The workers on Vinthem are the system\'s forgotten. Their contracts are '
                'long, their wages are the lowest in the cluster, and the conditions are '
                'harsh enough that the completion rate -- the percentage of workers who '
                'finish their term and leave -- is lower than any other posting. The '
                'workers who do not complete their terms are not always dead. Some are '
                'injured and returned to the surface. Some are extended indefinitely for '
                'accumulated debts. Some simply disappear from the records, and the '
                'recruiting corporations do not explain what happened to them because the '
                'explanation would be bad for business.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Scathel',
            short_description='A hot inner world -- solar collection powering the system\'s infrastructure, staffed by workers who drew the short straw and know it.',
            long_description=(
                'Scathel is a hot, dense inner world with solar collection arrays that '
                'provide energy for the system\'s infrastructure. The 35,000 times Sol '
                'luminosity of the primary star means the energy collection is efficient '
                'and the radiation environment is hostile. The maintenance crews are '
                'indentured workers on short-rotation contracts -- the postings are '
                'undesirable enough that the recruiting corporations assign them to '
                'workers who have no leverage to refuse. The work is functional. The '
                'conditions are survivable. The workers survive them and return to the '
                'surface and consider themselves fortunate, which is the kind of fortune '
                'that only Shaula produces.'
            ),
            population=5_000_000,
        ),
    ],
    short_description='The cluster\'s cheap labour pool -- eighteen billion people in grinding poverty, supplying the indentured workforce that the rest of the Antares runs on.',
    long_description=(
        'Shaula is where the people come from. Eighteen billion of them, living on '
        'three overcrowded worlds in conditions that deteriorate with every generation. '
        'The infrastructure was built for a fraction of the current population and has '
        'not been expanded to match. The cities are stacked, improvised, held together '
        'by engineering that ranges from competent to terrifying. The sanitation is '
        'inadequate. The medical care is overwhelmed. The food is bulk grain processed '
        'into the cheapest possible forms. The stims are the worst in the cluster -- '
        'sub-standard compounds that produce tremors within months and cognitive '
        'erosion within a year. The life expectancy is decades below the cluster '
        'average. The birth rate is the highest. People are born, they work, they '
        'degrade, they die. The cycle is fast.\n\n'
        'Shaula\'s export is labour. The recruiting corporations from across the '
        'Antares cluster maintain offices on every populated world, offering indenture '
        'contracts that provide passage, housing, stims, and a wage in exchange for '
        'fixed terms of work at rates the workers cannot negotiate. The contracts are '
        'legal. They are also exploitative -- terms are extended through accumulated '
        'debts for medical costs, stim costs, and equipment charges that were buried '
        'in clauses the workers understood and could not afford to refuse. Temporary '
        'indenture becomes permanent. The workers know this happens. They sign anyway '
        'because the alternative is staying.\n\n'
        'The labour transports depart from Burden Station carrying hundreds of '
        'thousands of workers per cycle -- to the Furnaces on Dschubba, to the farms '
        'on Acrab, to the military, to domestic service, to every corner of the '
        'cluster that needs cheap, desperate, disposable labour. The workers who '
        'return -- some do, when their terms are genuinely complete and their debts '
        'are genuinely paid -- come back to a system that is slightly worse than when '
        'they left, because eighteen billion people on infrastructure built for six '
        'billion gets worse every year and nobody is investing in the difference.\n\n'
        'Shaula is the foundation that the Antares cluster is built on. The drugs are '
        'manufactured on Dschubba. The food is grown on Acrab. The military is based '
        'at Antares. But the labour that makes all of it run comes from Shaula -- '
        'from eighteen billion people who were born into poverty so deep that signing '
        'away their freedom for a fixed term feels like opportunity. The cluster does '
        'not acknowledge this dependency. Shaula does not have the leverage to make '
        'them.'
    ),
    cluster=StarClusters.ANTARES,
)

SARGAS = System(
    name='Sargas',
    star='Bright yellow-white giant (F1II), approximately 6,000 times Sol luminosity -- unusually warm-toned for the Antares cluster',
    population=13_000_000_000,
    distance_to_sol=300.0,
    stellar_objects=[
        StellarObject(
            name='Dekhar',
            short_description='The system\'s primary world -- a dense, mineral-rich planet that has been mined, smelted, and forged for centuries to build the Antarian fleet.',
            long_description=(
                'Dekhar is a dense, rocky world with mineral deposits that made it the '
                'natural foundation for the Antares cluster\'s industrial base. The planet '
                'has been mined intensively since colonisation -- deep extraction operations '
                'pulling heavy metals, rare earths, and structural alloys from a crust that '
                'is rich enough to have sustained centuries of industrial demand without '
                'exhaustion. The surface shows it: vast open-cast mines visible from orbit, '
                'smelting complexes that glow at night, and industrial cities built around '
                'the foundries that process the raw material into the components that the '
                'shipyards consume.\n\n'
                'Five billion people live on Dekhar, and the majority work in the extraction '
                'and processing chain. The work is heavy, physical, and conducted on stims '
                'that prioritise endurance and focus over the longer-term health of the '
                'workforce. The miners are on compounds that suppress fatigue and dull pain '
                '-- necessary because the deep extraction shifts run longer than a baseline '
                'human body can sustain, and the injury rate in the mines is high enough '
                'that working through minor injuries is an economic requirement rather than '
                'a choice. The foundry workers are on focus compounds that let them operate '
                'precision smelting equipment at enhanced speed. The logistics workers are '
                'on cognitive enhancers that let them coordinate the movement of millions '
                'of tonnes of material per cycle.\n\n'
                'Dekhar is not a pleasant world. The atmosphere carries particulates from '
                'the smelting operations -- the air quality in the industrial cities is '
                'poor enough that respiratory complications are endemic and accepted as a '
                'cost of living where the work is. The cities themselves are functional '
                'rather than attractive: housing blocks, transit links, and the commercial '
                'districts that service a population whose lives are organised around shift '
                'schedules. The warm yellow-white light of Sargas\'s star gives the planet '
                'an amber glow that would be beautiful if it were not filtered through '
                'industrial haze.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='The Docks',
            short_description='The orbital shipyards -- the largest military construction facility in the Antares cluster, where the fleet is built, repaired, and refit.',
            long_description=(
                'The Docks are the Antares cluster\'s premier military shipyards -- an '
                'enormous orbital construction complex above Dekhar where the Antarian '
                'fleet is built. The facility is vast: dozens of construction bays capable '
                'of assembling everything from frigates to capital ships, repair and refit '
                'berths that service the active fleet, and the testing ranges where newly '
                'completed vessels are shaken down before commissioning. The Docks produce '
                'the angular, aggressive warships that Antarian doctrine favours -- ships '
                'designed for speed, built for stimmed crews, and optimised for the short, '
                'violent engagements that exploit enhanced reaction times.\n\n'
                'The workforce on the Docks is the most skilled labour in the system -- '
                'shipwrights, welders, systems engineers, and weapons installers whose '
                'stim regimes are better than the miners\' because precision construction '
                'requires steadier hands and clearer heads. The corporations that run the '
                'Docks invest in their shipyard workers the way Dschubba\'s corporations '
                'invest in their feedstock engineers: because the cost of a construction '
                'error in a warship exceeds the cost of premium compounds. The investment '
                'is pragmatic. The workers are aware that their health is maintained '
                'because their mistakes are expensive, not because their wellbeing matters.\n\n'
                'The military presence at the Docks is heavy. The Antarian fleet maintains '
                'a permanent garrison to protect the shipyards -- the most strategically '
                'valuable installation in the cluster outside Antares itself. The garrison '
                'includes capital ships, cruisers, and the screening forces that patrol '
                'the approaches. An attack on the Docks would be an attack on the cluster\'s '
                'ability to sustain the war, and the defences reflect this. MERIT\'s '
                'strategists have identified the Docks as a priority target. The Antarian '
                'command has identified this identification and reinforced accordingly.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Torvel',
            short_description='An industrial world specialising in weapons systems and ship components -- the supply chain that feeds the Docks.',
            long_description=(
                'Torvel is the system\'s second industrial world -- smaller than Dekhar, '
                'with fewer mineral resources of its own but extensive manufacturing '
                'capacity oriented toward the higher-order components that the shipyards '
                'consume. Where Dekhar produces the raw structural materials -- hull '
                'plating, frame members, armour composites -- Torvel produces the systems '
                'that go inside: weapons arrays, sensor packages, engine components, the '
                'control interfaces calibrated for stimmed operators, and the '
                'pharmaceutical storage and dispensing systems that every Antarian warship '
                'carries because a ship that runs out of stims has a crew going into '
                'withdrawal mid-combat.\n\n'
                'The factories on Torvel are precision operations -- cleaner than Dekhar\'s '
                'foundries, staffed by engineers and technicians on better stims, producing '
                'components to tolerances that the shipyards demand. The weapons '
                'manufacturing is the most tightly controlled: the production of warship-'
                'grade weapons systems is overseen by military inspectors who verify every '
                'unit before it leaves the factory floor. The inspectors are Antarian '
                'military personnel on military-grade stims, and they are not forgiving of '
                'defects.\n\n'
                'Torvel\'s population is industrial and focused in the way that a community '
                'built around precision manufacturing tends to be. The culture values '
                'competence and reliability. The social hierarchy tracks skill: a master '
                'weapons engineer outranks a factory manager in the informal status system '
                'that governs daily life. The workers on Torvel are proud of their output '
                'in a way that the miners on Dekhar -- whose work is brutal and '
                'undifferentiated -- are not. They build the weapons that the fleet carries. '
                'The fleet\'s victories are, in part, theirs.'
            ),
            population=2_800_000_000,
        ),
        StellarObject(
            name='Brassard',
            short_description='A military world -- the Antarian fleet\'s primary training and staging base in the rear area, where crews are assembled and ships are assigned.',
            long_description=(
                'Brassard is the system\'s military world -- not a production facility but '
                'the base where the fleet\'s human element is assembled, trained, and '
                'prepared. Newly commissioned ships from the Docks are crewed at Brassard. '
                'Newly recruited personnel from across the cluster -- including the '
                'indentured military recruits from Shaula -- are trained at Brassard\'s '
                'facilities. Damaged ships that return from the front for repair at the '
                'Docks stage their crews at Brassard while the work is done.\n\n'
                'The training on Brassard is focused on the distinctive challenge of '
                'Antarian military operations: fighting stimmed. The recruits learn to '
                'trust enhanced reflexes, to operate ship systems calibrated for reaction '
                'times they cannot achieve without compounds, and to manage the performance '
                'window that defines Antarian tactics -- the hours of superhuman capability '
                'followed by the degradation that comes when the stims wear off. The '
                'training includes managing the comedown under combat conditions, which is '
                'as important as the combat itself: an Antarian crew that cannot execute an '
                'orderly withdrawal when the enhancement fades is a dead crew.\n\n'
                'Brassard\'s population is largely military -- active personnel, trainees, '
                'instructors, and the support staff that keeps the base operational. The '
                'culture is military in character: disciplined, hierarchical, and shaped by '
                'the awareness that the fleet is at war and the people trained here will be '
                'fighting within months of completing their courses.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Prevatt',
            short_description='An agricultural world feeding the system\'s thirteen billion -- less productive than Acrab\'s farms but sufficient for local demand.',
            long_description=(
                'Prevatt is the system\'s agricultural world -- a temperate planet further '
                'from the star with conditions that support farming at a scale sufficient '
                'to feed the system\'s population without relying entirely on imports from '
                'Acrab. The farming is conducted at the standard Antarian pace -- enhanced '
                'workers on endurance compounds, engineered crop strains, productivity '
                'targets calibrated for stimmed labour. The output is less impressive than '
                'Acrab\'s dedicated agricultural worlds but adequate for the system\'s '
                'needs.\n\n'
                'Prevatt\'s population is the system\'s most civilian -- the one world in '
                'Sargas where the dominant culture is not industrial or military. The '
                'farming communities have the character of agricultural communities '
                'everywhere: seasonal rhythms, practical values, and a mild disdain for '
                'the urban and military populations on the other worlds who eat the food '
                'without understanding what it takes to produce it.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Holvane',
            short_description='A gas giant whose fuel processing supports both the military fleet and the freighter traffic that keeps the industrial supply chain moving.',
            long_description=(
                'Holvane is the system\'s gas giant -- a large body in the outer system '
                'whose moons host fuel processing at a scale that matches the system\'s '
                'dual demand: the military fleet stationed at the Docks and the freighter '
                'traffic that brings raw materials in and carries finished warships and '
                'components out. The fuel production is split between military-priority '
                'processing -- reserved for fleet vessels and given precedence in all '
                'scheduling -- and civilian processing for the commercial traffic. During '
                'periods of high military activity, the civilian allocation is reduced, '
                'and the freighter crews wait.\n\n'
                'The fuel workers on Holvane\'s moons are experienced and pragmatic -- '
                'skilled enough that the military trusts them with fleet fuelling and '
                'practical enough to manage the competing demands without the friction that '
                'military-civilian priority conflicts produce in other systems.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='The Trials',
            short_description='A barren outer world used as a weapons testing range and live-fire training ground -- where the ships built at the Docks prove they work.',
            long_description=(
                'The Trials is a barren, airless outer world that the military has claimed '
                'as its testing and training range. Newly completed warships from the Docks '
                'are put through their shakedown runs here: weapons systems are live-fired '
                'against target drones and decommissioned hulls, propulsion systems are '
                'pushed to rated limits and beyond, and the crews that will fly the ships '
                'into combat run simulated engagements under conditions as close to real '
                'combat as the training officers can produce without actually killing '
                'anyone.\n\n'
                'The surface of the Trials is cratered from decades of weapons testing -- '
                'the impacts visible from orbit as overlapping scars on the rock. Debris '
                'from destroyed target drones litters the orbital space. The training '
                'exercises are conducted under stim conditions -- the crews are enhanced '
                'to the same levels they will be in combat, and the training is timed to '
                'the same performance window. A crew that cannot complete the exercise '
                'before the stims fade is sent back to Brassard for additional training. '
                'A ship that fails its shakedown is sent back to the Docks. Neither '
                'failure is forgiven easily.'
            ),
            population=0,
        ),
    ],
    short_description='The forge of the Antarian fleet -- heavy industry, orbital shipyards, and the military infrastructure that keeps the cluster at war.',
    long_description=(
        'Sargas builds the fleet. The system is the Antares cluster\'s industrial and '
        'military production centre -- the shipyards that construct the angular, '
        'aggressive warships that Antarian doctrine demands, the foundries that produce '
        'the structural materials, the factories that build the weapons systems and '
        'components, and the military bases that train the crews and stage the ships '
        'for deployment. Thirteen billion people live in Sargas, and the majority are '
        'connected to the military-industrial chain that is the system\'s reason for '
        'existing.\n\n'
        'Dekhar is the foundation -- a dense, mineral-rich world whose crust has been '
        'mined for centuries without exhaustion, feeding the foundries that produce '
        'the raw materials the shipyards consume. The Docks, in orbit above Dekhar, '
        'are the largest military construction facility in the cluster -- dozens of '
        'construction bays producing everything from frigates to capital ships, '
        'defended by a garrison that reflects the shipyards\' strategic value. Torvel '
        'manufactures the weapons and systems that go inside the hulls. Brassard '
        'trains the crews and stages the ships. The Trials tests both.\n\n'
        'The system runs on the same stim economy as the rest of the cluster, but the '
        'military overlay gives it a different character. The hierarchy is sharper. The '
        'discipline is tighter. The awareness that the fleet is at war and the ships '
        'built here will be fighting within months of completion gives the work a '
        'weight that pure commercial manufacturing does not carry. The workers on '
        'Dekhar mine the ore knowing it will become a warship. The engineers on Torvel '
        'build the weapons knowing they will be fired at MERIT vessels. The crews on '
        'Brassard train knowing they will be in combat before their stim regimes have '
        'completed a full cycle. The production is not abstract. The consequences are '
        'visible in the damaged ships that return to the Docks for repair, in the '
        'crews that do not return at all, and in the new ships that are built to '
        'replace them.\n\n'
        'Sargas\'s star is an unusual warm yellow-white in a cluster dominated by '
        'blue-white giants and the vast red of the Antares supergiant. The amber light '
        'gives the system a quality that the inhabitants do not remark on and visitors '
        'notice immediately -- a warmth that is at odds with the industrial character '
        'of the worlds below. The light falls on foundries and shipyards and weapons '
        'factories and military bases, and it makes none of them gentler.'
    ),
    cluster=StarClusters.ANTARES,
)

NUNKI = System(
    name='Nunki',
    star='Blue-white main sequence (B2.5V), approximately 3,000 times Sol luminosity',
    population=7_000_000_000,
    distance_to_sol=228.0,
    stellar_objects=[
        StellarObject(
            name='Sovren',
            short_description='The capital of the Antares cluster -- where the democratic process operates flawlessly and the corporations that own it watch from comfortable offices.',
            long_description=(
                'Sovren is the seat of the Antarian government -- the world where the '
                'elected representatives of the Antares cluster convene, debate, legislate, '
                'and execute the policies that govern tens of billions of people across '
                'half a dozen systems. The democracy is real. The elections are held on '
                'schedule. The votes are counted accurately. The representatives are '
                'chosen by the people. The representatives are also, with a consistency '
                'that the electorate understands and cannot change, owned by the '
                'pharmaceutical corporations.\n\n'
                'The political factions on Sovren do not represent ideologies, regions, '
                'or social classes. They represent corporations. The Tessaline Bloc is '
                'backed by the cluster\'s largest stim manufacturer. The Veridian Coalition '
                'represents the second largest. The Compound Alliance, the Threshold '
                'Group, the Meridian Caucus -- each faction maps to a corporate interest, '
                'and the political debates that fill the legislative chamber are, stripped '
                'of their rhetorical dressing, negotiations between companies over market '
                'share, regulatory advantage, and the distribution of military contracts. '
                'The representatives argue with genuine passion. The passion is for their '
                'sponsors\' quarterly revenue.\n\n'
                'The city that houses the government is beautiful in the way that corporate '
                'money produces beauty: the legislative complex is grand, the public '
                'spaces are immaculate, and the corporate headquarters that ring the '
                'government district are towers of glass and light that make no pretence '
                'of being separate from the political process they dominate. The corporate '
                'offices are closer to the legislative chamber than the representatives\' '
                'own residences. The proximity is practical. The symbolism is unintentional '
                'and accurate.\n\n'
                'Politicians disappear. Not frequently -- the system is not crude -- but '
                'with a regularity that the political class understands as a cost of '
                'business. A representative who threatens to disrupt the balance between '
                'corporations, who takes a position that would advantage one sponsor too '
                'dramatically at the expense of another, who pushes for reforms that would '
                'weaken the corporate hold on the process -- that representative may find '
                'that their security detail has been reassigned, or that their vehicle\'s '
                'navigation system has malfunctioned, or that they have simply stopped '
                'appearing at legislative sessions and their office states they have '
                'resigned for personal reasons. The investigations are brief. The '
                'replacements are swift. The lesson is absorbed by the surviving '
                'representatives, who adjust their positions accordingly.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Prentice',
            short_description='The second world -- home to the bureaucratic machinery that implements what the government decides, staffed by people who know who is really in charge.',
            long_description=(
                'Prentice is the administrative world -- where the policies debated and '
                'enacted on Sovren are translated into the regulations, directives, and '
                'operational orders that govern the cluster. The bureaucracy on Prentice is '
                'enormous: ministries, agencies, regulatory bodies, and the interstellar '
                'coordination offices that manage the logistics of governing multiple '
                'systems across hundreds of light-years. The civil servants who staff these '
                'institutions are competent, stimmed for cognitive performance, and under '
                'no illusions about who they work for.\n\n'
                'The bureaucracy\'s most important function is balance. The Antares cluster '
                'survives because the corporations cooperate, and the corporations cooperate '
                'because the alternative -- the fragmentation that MERIT would exploit -- '
                'is worse than sharing. The regulatory framework that Prentice administers '
                'is designed to prevent any single corporation from dominating the others '
                'to the point where the alliance fractures. The regulations are complex, '
                'frequently amended, and the product of negotiations between corporate '
                'lawyers that make the legislative debates on Sovren look simple. The civil '
                'servants who implement these regulations understand that their real job is '
                'not governance. Their real job is preventing the cluster from eating '
                'itself.\n\n'
                'Prentice is also where the cluster\'s military coordination is '
                'administered. The Antarian fleet is funded by the corporations '
                'collectively, and the allocation of military resources -- which systems '
                'get which ships, which fronts are prioritised, which operations are '
                'funded -- is decided through a process that is nominally strategic and '
                'practically political. A corporation that is contributing more revenue '
                'expects more military protection for its assets. A corporation that is '
                'contributing less expects the same protection and negotiates aggressively '
                'to get it. The military planners on Prentice navigate these demands with '
                'the weary expertise of people who have learned that military strategy in '
                'the Antares cluster is corporate strategy with weapons attached.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Quorum',
            short_description='The cluster\'s primary orbital station -- where the corporate leadership meets, the export strategy is coordinated, and the real decisions are made.',
            long_description=(
                'The Quorum is the orbital station above Sovren that serves as the Antares '
                'cluster\'s primary orbital facility and, more importantly, the venue where '
                'the corporate leadership meets to make the decisions that the government '
                'will subsequently ratify. The station is luxurious by any standard -- the '
                'corporate suites are designed to project wealth and power, the conference '
                'facilities are equipped for the secure communications that inter-system '
                'corporate negotiations require, and the dining is the finest in the outer '
                'systems.\n\n'
                'The Quorum is where the export strategy is coordinated. The effort to '
                'spread Antarian stims into the inner systems is the one initiative that '
                'every corporation supports without reservation, because the benefits are '
                'universal: more revenue, more dependency, more strategic leverage over '
                'MERIT. The coordination meetings bring together the corporate leaders, the '
                'intelligence specialists who track inner-system drug policy and enforcement '
                'patterns, and the operatives who manage the distribution networks that '
                'move Antarian compounds into MERIT space. The meetings are professional, '
                'data-driven, and conducted with the focused intensity of people who '
                'understand that every inner-system citizen who becomes dependent on '
                'Antarian stims is a strategic asset.\n\n'
                'The export operation is the corporations\' greatest point of cooperation. '
                'In every other arena -- market share, regulatory advantage, military '
                'allocation -- they compete. On the export question, they align, because '
                'the revenue flows to all of them and the strategic damage to MERIT '
                'benefits all of them. The coordination is genuine, efficient, and pursued '
                'with a unity of purpose that the cluster\'s internal politics never '
                'achieves. The corporations that cannot agree on tax policy can agree '
                'perfectly on the value of getting the inner systems addicted to their '
                'products.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Vestara',
            short_description='An intelligence and operations world -- where the covert export networks are managed and the inner-system distribution channels are maintained.',
            long_description=(
                'Vestara is the system\'s most discreet world -- a cooler, smaller planet '
                'further from the star that hosts the operational infrastructure for the '
                'cluster\'s covert activities. The intelligence services that monitor '
                'MERIT\'s military movements, the operatives who manage the inner-system '
                'drug distribution networks, and the analysts who track the spread of '
                'Antarian stim dependency across the inner systems are based on Vestara.\n\n'
                'The export networks managed from Vestara are the cluster\'s most '
                'sophisticated operation. The stims that enter the inner systems are '
                'repackaged, relabelled, and routed through intermediaries to obscure their '
                'Antarian origin. The networks operate through independent traders, grey-'
                'market distributors, and the commercial channels that exist in every inner '
                'system where MERIT\'s enforcement is less than total. The operatives who '
                'manage these networks are trained in tradecraft that would be familiar to '
                'any intelligence service -- cover identities, secure communications, dead '
                'drops, and the patient cultivation of contacts in positions where they can '
                'facilitate distribution.\n\n'
                'The analysts on Vestara track the results with the same metrics that the '
                'corporations track sales: market penetration, dependency rates, repeat '
                'usage, geographic spread. The data is presented to the corporate leadership '
                'at the Quorum in quarterly briefings that read like sales reports and '
                'function like strategic assessments. The number of inner-system citizens '
                'dependent on Antarian compounds is a metric that the corporations and the '
                'military track with equal interest, because it measures both revenue and '
                'strategic damage simultaneously.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Thurmond',
            short_description='An agricultural world feeding the system -- quieter and less politically charged than the inner planets.',
            long_description=(
                'Thurmond is the system\'s agricultural world -- temperate, fertile, and '
                'oriented toward feeding Nunki\'s seven billion people. The farming follows '
                'the standard Antarian model: enhanced workers, engineered crops, '
                'productivity targets calibrated for stimmed labour. The output is '
                'sufficient for local demand with a modest surplus.\n\n'
                'Thurmond is the system\'s least political world. The corporate rivalries, '
                'the legislative maneuvering, the intelligence operations -- none of it '
                'touches the farming communities directly. The farmers grow food. The food '
                'feeds the politicians and the bureaucrats and the corporate executives '
                'and the intelligence operatives, and the farmers do not particularly care '
                'which faction any of them represent as long as the contracts for the '
                'harvest are honoured.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Gravven',
            short_description='A gas giant with fuel processing -- and the location where politicians who have become inconvenient are rumoured to be taken.',
            long_description=(
                'Gravven is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The operations are standard and '
                'unremarkable. What is remarkable is the persistent rumour -- never '
                'confirmed, never denied, never investigated with any seriousness -- that '
                'Gravven\'s outer moons are where the corporations dispose of political '
                'problems. The representatives who disappear from Sovren, the bureaucrats '
                'who learn too much on Prentice, the operatives on Vestara who become '
                'liabilities -- the rumour says they end up on Gravven. Not alive.\n\n'
                'The fuel workers on Gravven\'s moons report nothing unusual. The moons '
                'are cold, airless, and occupied only by fuel processing facilities and '
                'their crews. There is nothing on Gravven that would confirm the rumours. '
                'There is also nothing that would dispel them, and in a system where '
                'politicians vanish with regularity, the absence of evidence is not '
                'reassuring.'
            ),
            population=40_000_000,
        ),
    ],
    short_description='The political capital of the Antares cluster -- a democracy owned by drug corporations, governing a war effort funded by addiction.',
    long_description=(
        'Nunki is where the Antares cluster is governed, which is to say it is where '
        'the pharmaceutical corporations allow governance to occur. The system hosts '
        'the elected government of the Antarian faction -- a democracy that functions '
        'flawlessly by every procedural measure and is controlled completely by the '
        'corporations whose revenue funds the military, the infrastructure, and the '
        'war. The political factions represent corporate interests. The debates are '
        'negotiations over market share. The elections determine which corporation\'s '
        'preferred candidates hold the seats, and the electorate participates with the '
        'informed resignation of people who understand the system and cannot change it.\n\n'
        'The government\'s most important function is balance. The corporations compete '
        'relentlessly -- for market share, regulatory advantage, and the military '
        'contracts that determine whose assets are protected -- but the competition '
        'must not fracture the alliance that keeps MERIT at bay. The bureaucracy on '
        'Prentice administers a regulatory framework designed to prevent any single '
        'corporation from dominating the others to the point of collapse. The balance '
        'is maintained by the shared understanding that fragmentation means MERIT '
        'wins, and MERIT winning means the corporations lose everything.\n\n'
        'The one arena of genuine cooperation is the export strategy. Every '
        'corporation supports the effort to spread Antarian stims into the inner '
        'systems, because the benefits are universal: revenue from sales, strategic '
        'damage from dependency. The coordination is managed from the Quorum -- the '
        'orbital station where corporate leaders meet -- and executed through the '
        'covert networks managed from Vestara. The operatives who run the inner-system '
        'distribution channels are as valued as military assets, because every '
        'inner-system citizen who becomes dependent on Antarian compounds is a thread '
        'of leverage that weakens MERIT\'s position and funds the cluster\'s war '
        'effort simultaneously.\n\n'
        'Politicians disappear in Nunki. Not frequently, but with a regularity that '
        'the political class understands. A representative who disrupts the balance, '
        'who threatens a corporation too directly, who pushes reforms that the '
        'corporate consensus has not approved -- that representative stops appearing '
        'at sessions. The investigations are brief. The replacements are swift. The '
        'fuel workers on Gravven\'s outer moons report nothing unusual. The system '
        'functions. The democracy operates. The corporations decide what the democracy '
        'decides, and the cluster holds together because the alternative is worse.'
    ),
    cluster=StarClusters.ANTARES,
)

KAUS = System(
    name='Kaus',
    star='Blue-white giant (B9.5III), approximately 3,500 times Sol luminosity',
    population=12_000_000_000,
    distance_to_sol=143.0,
    stellar_objects=[
        StellarObject(
            name='Aveline',
            short_description='The capital world -- six billion people living well, working enhanced, and demonstrating what the Antarian model looks like when the money is there.',
            long_description=(
                'Aveline is the system MERIT does not want you to see. The planet is '
                'temperate, well-terraformed, and home to six billion people who live in '
                'cities that are clean, modern, and genuinely pleasant. The infrastructure '
                'works. The hospitals are well-equipped. The schools are good. The housing '
                'is spacious. The parks are maintained. By the measurable metrics that '
                'define quality of life, Aveline competes with the best inner-system worlds '
                '-- and it does it on stims.\n\n'
                'The stim regimes on Aveline are what the pharmaceutical industry markets '
                'as the intended experience. The population can afford quality compounds -- '
                'clean, precisely formulated, managed by medical professionals who monitor '
                'dosage and adjust for individual neurochemistry. The cognitive enhancers '
                'sharpen without jittering. The focus compounds sustain without crashing. '
                'The endurance boosters extend the working day without the tremors and '
                'paranoia that cheap industrial stims produce on Shaula and the Fringe. '
                'The side effects are minimal. The dependency is real but managed -- the '
                'population is dependent on compounds they can afford and that do not '
                'destroy them, which is the version of the stim economy that the '
                'corporations present as proof that the system works.\n\n'
                'And it does work, here. The productivity on Aveline is extraordinary. The '
                'enhanced workforce produces economic output per capita that exceeds most '
                'inner-system worlds. The businesses are competitive. The research '
                'institutions are productive. The creative industries -- art, design, '
                'entertainment -- benefit from enhancement compounds that the artists '
                'describe as clarifying rather than distorting. The culture on Aveline is '
                'energetic, ambitious, and confident in a way that feels earned rather '
                'than chemically induced, though the distinction is philosophical.\n\n'
                'MERIT\'s objection is not that Aveline is unpleasant. MERIT\'s objection '
                'is that Aveline is the advertisement and Shaula is the product -- that '
                'the system works beautifully when everyone can afford the good compounds '
                'and catastrophically when they cannot, and that a civilisation that '
                'requires chemical enhancement to participate has not enhanced humanity '
                'regardless of how pleasant the results look at the top.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Thessaly',
            short_description='The second world -- warmer, lusher, and the cluster\'s premier destination for people who can afford to live where the stims are good and the weather is better.',
            long_description=(
                'Thessaly is Kaus\'s second habitable world -- warmer than Aveline, with '
                'subtropical forests, broad coastlines, and a climate that the terraforming '
                'engineers calibrated for comfort rather than merely habitability. The '
                'planet is gorgeous. The cities are integrated into the landscape with an '
                'architectural sensibility that reflects the wealth of a population that '
                'can afford to care about aesthetics.\n\n'
                'Thessaly attracts the cluster\'s wealthy -- corporate executives, senior '
                'researchers, successful entrepreneurs, and the people who have made enough '
                'money elsewhere in the Antares to choose where they live. The population '
                'is smaller than Aveline\'s and wealthier on average. The stim regimes are '
                'the best available -- bespoke formulations from personal pharmaceutical '
                'consultants, the same calibre of compounds that the corporate leadership '
                'on Osaren uses. The result is a population that is enhanced, healthy, '
                'productive, and ageing gracefully in a system where graceful ageing is '
                'not the default.\n\n'
                'Thessaly is the Antares cluster\'s answer to the inner systems\' criticism. '
                'When MERIT argues that the stim economy destroys people, the Antarian '
                'response is Thessaly -- a world of three billion happy, healthy, enhanced '
                'citizens living lives that are demonstrably better than the unenhanced '
                'baseline. The response is effective. It is also selective, because Thessaly '
                'represents what the stim economy produces for those who can afford it, and '
                'the tens of billions who cannot afford it are not part of the presentation.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Braith',
            short_description='A temperate third world -- diversified economy, comfortable living, and the system\'s most balanced population.',
            long_description=(
                'Braith is the system\'s third habitable world -- temperate, well-'
                'terraformed, and home to a population whose economy is more diversified '
                'than the other worlds. Braith has agriculture, light industry, services, '
                'and a growing technology sector that produces the medical monitoring '
                'systems and pharmaceutical management tools that make Kaus\'s quality stim '
                'regimes possible. The planet is where the infrastructure of comfortable '
                'enhancement is developed -- the devices that track individual '
                'neurochemistry, the software that adjusts dosage in real time, the '
                'diagnostic tools that catch side effects before they manifest.\n\n'
                'The population on Braith is the system\'s most middle-class -- not as '
                'wealthy as Thessaly\'s residents, not as numerous as Aveline\'s, but '
                'comfortable in the way that a well-functioning economy with good stims '
                'produces. The cities are pleasant without being spectacular. The culture '
                'is productive without being intense. Braith is the system\'s workhorse -- '
                'the world where the ordinary business of civilisation happens without '
                'the glamour of Thessaly or the scale of Aveline.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Lathom',
            short_description='The system\'s orbital port -- modern, well-run, and the showcase that the Antarian government brings visiting dignitaries to.',
            long_description=(
                'Lathom is Kaus\'s primary orbital station -- a modern facility that '
                'handles the system\'s traffic with the smooth efficiency that wealth '
                'enables. The station is clean, well-designed, and comfortable in a way '
                'that makes an immediate impression on visitors arriving from other '
                'Antarian systems. The contrast with Gantry\'s overwhelming bustle or '
                'Burden Station\'s grimness is deliberate: Lathom is the port that the '
                'Antarian government brings people to when it wants to make a good '
                'impression.\n\n'
                'The traffic at Lathom is commercial and civilian -- the system has no '
                'significant military presence beyond a modest garrison, because Kaus is '
                'deep enough in the cluster that the war does not touch it directly. The '
                'commerce is high-value: the pharmaceutical management technology produced '
                'on Braith, the luxury goods and services that Thessaly\'s wealthy '
                'population demands, and the steady flow of people moving to Kaus from '
                'other systems because they have made enough money to afford the good '
                'life that Kaus offers.\n\n'
                'Lathom is also where the recruitment happens -- not the desperate '
                'indenture of Shaula but the targeted recruitment of skilled professionals '
                'from across the cluster who are offered salaries, quality stims, and a '
                'standard of living that their home systems cannot match. The brain drain '
                'from the poorer systems to Kaus is a source of quiet resentment across '
                'the cluster, and Lathom\'s polished arrivals terminal is where the drain '
                'becomes visible.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Colburn',
            short_description='An agricultural world feeding the system -- productive, well-managed, and where even the farm workers can afford stims that don\'t destroy them.',
            long_description=(
                'Colburn is the system\'s agricultural world -- fertile, temperate, and '
                'farmed with a productivity that reflects Kaus\'s overall wealth. The '
                'agricultural workers on Colburn are on endurance boosters and focus '
                'compounds, the same as agricultural workers everywhere in the cluster. '
                'The difference is quality: the compounds available on Colburn are '
                'mid-grade rather than the industrial-grade products that Acrab\'s '
                'labourers and Shaula\'s indentured workers burn through. The farm workers '
                'on Colburn work enhanced, work long hours, and go home at the end of the '
                'season with their hands steady and their cognition intact.\n\n'
                'This is the difference that money makes. The same work, the same '
                'enhancement, the same productivity targets -- but the compounds are '
                'cleaner, the medical monitoring is better, and the workers can afford to '
                'maintain their health while maintaining their output. Colburn\'s farmers '
                'are not rich. They are comfortable, which in the Antares cluster is a '
                'privilege that most agricultural workers in other systems do not share.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Tremaine',
            short_description='A gas giant with fuel processing -- standard operations, well-maintained, unremarkable in the way that everything in Kaus is unremarkable when it works.',
            long_description=(
                'Tremaine is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s commercial traffic. The operations are standard '
                'and well-maintained. The workers are on decent compounds. The facilities '
                'are modern. The fuel is processed on schedule and without incident. '
                'Tremaine is unremarkable in the specific way that Kaus specialises in: '
                'the unremarkable quality of things that work as they should. The fuel '
                'workers in other Antarian systems -- on cheaper stims, in worse '
                'facilities, with equipment maintained to the minimum rather than the '
                'optimum -- would find Tremaine\'s normality extraordinary.'
            ),
            population=35_000_000,
        ),
        StellarObject(
            name='Lindern',
            short_description='A small, cool world hosting medical research institutions -- studying the long-term effects of quality stim use and quietly proving that even the good compounds change you.',
            long_description=(
                'Lindern is a small, cool world in the outer habitable zone that hosts '
                'Kaus\'s medical research institutions. The research focus is the long-term '
                'effects of quality stim use -- not the devastating degradation that cheap '
                'compounds produce, which is well-documented and politically convenient for '
                'both MERIT and the Antarian corporations, but the subtler effects that '
                'decades of premium enhancement produce in populations that can afford the '
                'best.\n\n'
                'The findings are not published with the same enthusiasm as the cluster\'s '
                'commercial research. The data shows that even the finest compounds, over '
                'a lifetime, produce changes: subtle personality shifts, narrowing of '
                'emotional range, a measured reduction in the capacity for unstructured '
                'thought -- creativity, spontaneity, the kind of thinking that does not '
                'have a target. The enhanced population on Aveline and Thessaly is '
                'productive, healthy, and gradually becoming less of something that the '
                'researchers struggle to define. Not less intelligent. Not less capable. '
                'Less something. The research continues. The publications are careful. The '
                'corporations fund the institutions and do not interfere with the findings '
                'and do not promote them either.'
            ),
            population=60_000_000,
        ),
    ],
    short_description='The showcase of the Antares cluster -- twelve billion people demonstrating what the stim economy looks like when everyone can afford the good compounds.',
    long_description=(
        'Kaus is the argument the Antares cluster makes in its own defence. Twelve '
        'billion people on well-terraformed worlds, living in clean cities with good '
        'infrastructure, working enhanced on compounds that are precisely formulated, '
        'medically managed, and free of the devastating side effects that define the '
        'stim experience on the cluster\'s poorer worlds. The productivity is '
        'extraordinary. The quality of life competes with the best inner systems. The '
        'population is healthy, energetic, and ageing gracefully. Kaus is what the '
        'pharmaceutical corporations point to when MERIT argues that the stim economy '
        'destroys people.\n\n'
        'The argument is effective and incomplete. Kaus works because Kaus is wealthy. '
        'The population can afford quality compounds. The medical infrastructure can '
        'manage individual dosage. The economy generates enough revenue that even the '
        'farm workers on Colburn are on mid-grade stims rather than the industrial '
        'products that burn through the labourers on Acrab and the indentured workers '
        'on Shaula. Kaus is the top of a system whose bottom is eighteen billion '
        'people in grinding poverty, and the showcase does not include the foundation.\n\n'
        'The system attracts the cluster\'s ambitious and talented -- a brain drain from '
        'poorer systems that reinforces Kaus\'s advantage and deepens the inequality. '
        'Skilled professionals are recruited with salaries and quality stims that their '
        'home systems cannot match. The wealth concentrates. The showcase brightens. '
        'The worlds it draws from dim.\n\n'
        'On Lindern, the medical researchers study what even the good compounds do '
        'over a lifetime: subtle changes, narrowing ranges, a measured reduction in '
        'something the researchers cannot quite name. The findings are not suppressed. '
        'They are not promoted. The corporations fund the research and file the '
        'results and the population of Kaus continues to live well and work enhanced '
        'and not think too hard about what they might be trading for the clarity and '
        'energy and focus that the compounds provide. The trade-off, if it exists, is '
        'subtle enough that it does not feel like a trade-off. That may be the most '
        'Antarian sentence in the galaxy.'
    ),
    cluster=StarClusters.ANTARES,
)

DIZUO = System(
    name='Dizuo',
    star='Red bright giant (M5Ib-II), massive and unstable -- actively shedding material from a pulsating atmosphere, filling the system with clouds of stellar dust',
    population=300_000_000,
    distance_to_sol=360.0,
    stellar_objects=[
        StellarObject(
            name='Verathen',
            short_description='The system\'s only inhabited world -- corporate headquarters, support infrastructure, and little else besides the reason the corporation exists.',
            long_description=(
                'Verathen is a cool, rocky world in the outer system that would be '
                'unremarkable in any other context. The planet is habitable in enclosed '
                'habitats -- thin atmosphere, cold surface, adequate mineral resources '
                'for local construction. The population is small and exists for one '
                'purpose: to support the Lucirin Corporation\'s operations in the system.\n\n'
                'The Lucirin Corporation is one of the major pharmaceutical companies of '
                'the Antares cluster, and Dizuo is where it began. The corporate '
                'headquarters on Verathen is the company\'s ancestral home -- a complex '
                'that has grown over centuries from the original research facility where '
                'the dust\'s properties were first analysed into the administrative centre '
                'of a corporation whose revenue places it among the largest in the cluster. '
                'The headquarters is maintained with the particular care that corporations '
                'apply to their founding sites: the original laboratory is preserved as a '
                'museum, the corporate history is displayed in the lobby, and the executives '
                'who run the company from Osaren and Sovren make pilgrimages to Verathen '
                'with the regularity of the devout visiting a shrine.\n\n'
                'The rest of Verathen is support infrastructure. The orbital control '
                'facilities that coordinate the trawler stations. The logistics depots that '
                'receive the harvested dust and prepare it for shipment to the processing '
                'plants on Dschubba. The residential habitats for the workforce. The '
                'medical facilities that monitor the health of workers who spend their '
                'careers in proximity to a substance that has stimulant properties in its '
                'raw form and whose long-term exposure effects are documented in studies '
                'that the corporation publishes selectively.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='The Trawlers',
            short_description='The harvesting stations -- vast collection arrays drifting through the stellar dust clouds, gathering the raw material that built a pharmaceutical empire.',
            long_description=(
                'The Trawlers are the system\'s defining feature: a fleet of large, slow '
                'stations that do not orbit the star in the conventional sense but drift '
                'through the system on calculated trajectories that carry them through the '
                'densest concentrations of the stellar dust. Each Trawler is built around '
                'its collection arrays -- enormous mesh structures, kilometres across, '
                'that extend from the station like the nets of a deep-sea fishing vessel '
                'and sweep the dust from the space through which they pass.\n\n'
                'The dust is the star\'s shed material -- particles expelled from the red '
                'giant\'s unstable, pulsating atmosphere over millions of years, drifting '
                'through the system in clouds that are visible on sensors and faintly '
                'visible to the eye as a reddish haze against the deep red light of the '
                'star. The dust contains trace compounds that, when processed, produce a '
                'family of stimulant effects on the human nervous system. The compounds '
                'cannot be synthesised artificially -- the molecular structures are '
                'products of the specific conditions in the red giant\'s atmosphere, and '
                'no laboratory has replicated them. Dizuo\'s dust is the sole source. The '
                'Lucirin Corporation controls the sole source. The economics follow.\n\n'
                'The Trawlers move slowly -- their trajectories are calculated years in '
                'advance, adjusted for the star\'s pulsation cycle and the shifting density '
                'of the dust clouds. The collection is continuous. The arrays fill, the '
                'dust is compressed and stored in the station\'s holds, and when the holds '
                'are full the Trawler returns to Verathen\'s orbital facilities to offload '
                'before beginning another sweep. The cycle takes months. The Trawlers are '
                'crewed by small teams who live aboard for the duration of each sweep -- '
                'isolated, surrounded by the red haze of a dying star\'s exhalations, '
                'harvesting the material that makes the corporation possible.\n\n'
                'The crews wear respiratory protection at all times. The dust in its raw '
                'form is a stimulant -- the original discovery was made by a ship\'s crew '
                'in the 2900s who performed an EVA and failed to decontaminate properly, '
                'exposing themselves to the dust aboard their ship. The effects were '
                'immediate and obvious: heightened alertness, accelerated cognition, a '
                'clarity that the crew described in terms that caught the attention of '
                'people who understood the commercial potential. The company that formed '
                'around this discovery became the Lucirin Corporation. The dust that coated '
                'a spacesuit became an industry that shapes the politics of an interstellar '
                'cluster.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='The Efflux',
            short_description='The dust clouds themselves -- the shed material of a dying star, drifting through the system in reddish haze, and the most valuable natural resource in the Antares cluster.',
            long_description=(
                'The Efflux is what the Lucirin Corporation calls the dust clouds that fill '
                'the Dizuo system -- the material shed by the red giant\'s unstable '
                'atmosphere, expelled in pulses that correspond to the star\'s irregular '
                'pulsation cycle and drifting outward through the system in concentrations '
                'that vary with distance from the star, time since the last major pulse, '
                'and the gravitational influence of the system\'s other bodies.\n\n'
                'The Efflux is not uniform. The densest clouds are closest to the star -- '
                'too hot and too radiation-heavy for the Trawlers to operate safely. The '
                'Trawlers work the middle regions where the dust has cooled and dispersed '
                'to concentrations that the collection arrays can harvest without '
                'overwhelming the stations\' filtration systems. The outer regions are too '
                'thin for efficient collection. The sweet spot is a band of space that the '
                'corporation has mapped in extraordinary detail -- the density gradients, '
                'the flow patterns, the seasonal shifts as the star\'s pulsation cycle '
                'pushes new material outward and the existing clouds redistribute.\n\n'
                'The Efflux is a finite resource, in the sense that the star\'s shedding '
                'will eventually slow as the giant evolves. The timescale is millions of '
                'years. The Lucirin Corporation does not worry about supply. The '
                'corporation worries about competitors attempting to establish their own '
                'harvesting operations in the system, which is why the corporate security '
                'presence in Dizuo is disproportionate to the population -- armed vessels '
                'patrolling the Efflux, ensuring that the sole source remains sole.'
            ),
            population=0,
        ),
        StellarObject(
            name='Obsavar',
            short_description='A hot inner world too close to the shedding star -- its surface coated in accumulated dust that has baked into a dark, metallic crust.',
            long_description=(
                'Obsavar is the innermost planet -- a rocky world close enough to the '
                'red giant that the dust settles on its surface faster than it disperses. '
                'Over millions of years, the accumulated material has baked into a dark, '
                'metallic crust that gives the planet a distinctive appearance: a world '
                'that looks forged rather than formed, its surface a smooth, dark shell '
                'of compressed stellar material. The Lucirin Corporation has studied '
                'Obsavar\'s surface as a naturally compressed form of the dust and '
                'determined that the stimulant compounds degrade under the heat and '
                'radiation at this distance. The planet is scientifically interesting and '
                'commercially worthless.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dulith',
            short_description='A frozen outer world beyond the Efflux -- too far from the dust clouds and too cold for habitation, surveyed and ignored.',
            long_description=(
                'Dulith is a frozen body in the far outer system, beyond the range of the '
                'Efflux. The dust does not reach this far in useful concentrations. The '
                'planet is cold, airless, and of no commercial interest to the corporation '
                'that controls the system. Dulith was surveyed during the initial '
                'assessment and has not been visited since. The only notable feature is '
                'that from Dulith\'s surface, the Efflux is visible as a faint reddish '
                'glow surrounding the dim red star -- the exhalation of a dying giant, '
                'seen from far enough away that it looks like a halo rather than the '
                'industrial feedstock it has become.'
            ),
            population=0,
        ),
    ],
    short_description='The origin of an empire -- a red giant shedding stimulant dust, harvested by trawler stations for the corporation that turned a contaminated spacesuit into a pharmaceutical dynasty.',
    long_description=(
        'Dizuo is where it started. In the 2900s, a ship transiting the system '
        'performed an EVA and the crew\'s spacesuits were coated in the reddish dust '
        'that fills the system -- material shed by the red giant\'s unstable, pulsating '
        'atmosphere. The crew failed to decontaminate properly. The dust entered the '
        'ship. The effects on the exposed crew were immediate: heightened alertness, '
        'accelerated cognition, a clarity that the crew described in terms that caught '
        'the attention of people who understood what they were hearing. The company '
        'that formed around this discovery became the Lucirin Corporation, and the dust '
        'that coated a spacesuit became the foundation of a pharmaceutical industry '
        'that shapes the politics of an interstellar cluster.\n\n'
        'The dust contains trace compounds that produce stimulant effects on the human '
        'nervous system and that cannot be synthesised artificially -- the molecular '
        'structures are products of conditions specific to the red giant\'s atmosphere. '
        'Dizuo is the sole source. The Lucirin Corporation controls the sole source. '
        'The Trawlers -- large, slow stations trailing kilometre-wide collection arrays '
        '-- drift through the dust clouds on calculated trajectories, harvesting the '
        'material in sweeps that take months. The raw dust is compressed, stored, and '
        'shipped to the processing plants on Dschubba where it is refined into the '
        'family of compounds that the Lucirin brand is built on.\n\n'
        'Three hundred million people live in Dizuo -- a small population for an '
        'Antarian system, concentrated on Verathen and aboard the Trawlers. The '
        'corporate headquarters on Verathen is the Lucirin Corporation\'s ancestral '
        'home, maintained with the reverence of a founding site. The original '
        'laboratory where the dust\'s properties were first analysed is preserved as '
        'a museum. The executives who run the company from the cluster\'s political '
        'and commercial centres make pilgrimages here with the regularity of the '
        'devout.\n\n'
        'The system is quiet, red, and hazy. The star is enormous and dim -- a vast '
        'red disc shedding material that drifts through the system in clouds visible '
        'as a reddish glow. The Trawlers move slowly through the haze, their '
        'collection arrays extended, gathering the substance that an entire cluster '
        'depends on. The crews wear respiratory protection at all times. The dust is '
        'a stimulant in its raw form, and the irony of harvesting an addictive '
        'substance while wearing a mask to avoid becoming addicted to it is not lost '
        'on the workers who do the harvesting.'
    ),
    cluster=StarClusters.ANTARES,
)

YED_PRIOR = System(
    name='Yed Prior',
    star='Red giant (M0.5III), large and cool, casting deep amber-red light across the system',
    population=2_000_000_000,
    distance_to_sol=171.0,
    stellar_objects=[
        StellarObject(
            name='Soval',
            short_description='The world MERIT terraformed for grain that now grows the most potent drug crops in the Antares cluster -- on soil that MERIT paid for.',
            long_description=(
                'Soval is a warm, fertile world that MERIT terraformed in the 2900s as an '
                'agricultural colony. The terraforming was thorough and expensive: '
                'atmospheric processing, soil engineering, hydrological management, the '
                'full programme that MERIT\'s colonial planners deploy when they identify '
                'a world with high agricultural potential. The result was exactly what the '
                'planners intended -- a planet with deep, rich soil, reliable rainfall, '
                'and growing conditions that agricultural engineers describe as ideal. MERIT '
                'built a world for grain. The people who lived on it had other ideas.\n\n'
                'The illicit crops started small -- a few fields in remote regions, managed '
                'by administrators and farm operators who recognised that the same soil and '
                'climate that produced exceptional grain yields could produce exceptional '
                'yields of other things. The early crops were crude: naturally occurring '
                'plants with mild stimulant properties, grown in quantities that were easy '
                'to hide in the agricultural data and profitable enough to justify the '
                'risk. MERIT\'s oversight was distant. The auditors checked the grain '
                'output. The grain output was fine. The other output was not in the '
                'reports.\n\n'
                'When the outer systems declared independence, the side business became the '
                'main business. The company that had been managing the illicit crops -- a '
                'quiet operation run by a handful of agricultural administrators -- '
                'incorporated as the Verdaine Corporation and invested everything into '
                'expanding production. The grain fields were converted. The growing '
                'facilities were repurposed. The genetic engineers who had been quietly '
                'improving the crop strains for years were given resources and told to stop '
                'being quiet.\n\n'
                'The results, over generations of genetic modification, have been '
                'remarkable. The crops that grow on Soval today bear almost no resemblance '
                'to the wild plants that the original administrators cultivated. Each '
                'generation of modification has increased potency, yield, and the '
                'specificity of the stimulant compounds the plants produce. The current '
                'strains are engineered organisms that exist to produce pharmaceutical '
                'precursors with a precision that rivals synthetic manufacturing -- and '
                'they do it in soil, under sunlight, at a cost per dose that Dschubba\'s '
                'chemical synthesis cannot match for certain compound families. The soil '
                'that MERIT paid to engineer grows the drugs that fund the war against '
                'MERIT. The irony is noted in every strategic briefing and has not become '
                'less irritating with repetition.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Kelden',
            short_description='A second agricultural world -- still growing food, because even a drug corporation needs to feed its workforce.',
            long_description=(
                'Kelden is the system\'s second habitable world -- cooler, drier, and still '
                'performing the function that Soval was originally intended for: growing '
                'food. The Verdaine Corporation is a drug company but it employs two '
                'billion people and those people eat. Kelden\'s farms produce the grain, '
                'produce, and protein that feeds the system\'s population, supplemented by '
                'imports from Acrab when the local output falls short.\n\n'
                'Kelden is the system\'s quieter world -- less money, less intensity, less '
                'of the focused ambition that characterises Soval\'s genetically engineered '
                'crop operations. The farmers on Kelden grow food. The work is enhanced -- '
                'the same endurance compounds and focus stims as everywhere in the cluster '
                '-- but the product is honest calories rather than pharmaceutical '
                'precursors. The Kelden farmers regard the Soval operations with a '
                'complicated mix of dependence and disdain: Soval\'s drug crops fund the '
                'corporation that employs everyone in the system, but the Kelden farmers '
                'remember that this was supposed to be an agricultural colony and they are '
                'the ones still doing the original job.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Verdaine Tower',
            short_description='The orbital headquarters of the Verdaine Corporation -- built above the world that MERIT terraformed, running the business that MERIT made possible.',
            long_description=(
                'Verdaine Tower is the Verdaine Corporation\'s headquarters -- an orbital '
                'station above Soval that houses the corporate leadership, the research '
                'division, and the administrative infrastructure of a company whose revenue '
                'places it among the major pharmaceutical corporations of the Antares '
                'cluster. The station is named with the straightforwardness of a company '
                'that does not pretend to be anything other than what it is.\n\n'
                'The research division on Verdaine Tower is the corporation\'s most valuable '
                'asset. The genetic engineers who have spent generations modifying the crop '
                'strains on Soval work from laboratories aboard the station, developing the '
                'next generation of modifications that will push potency, yield, and '
                'compound specificity further. The work is agricultural science applied to '
                'pharmaceutical ends, and the researchers are among the best geneticists '
                'in the cluster -- recruited from Velleren, from Kaus, from wherever talent '
                'can be found and purchased. The Verdaine Corporation cannot match the '
                'Lucirin Corporation\'s monopoly on the Dizuo dust, but it can and does '
                'compete on the compounds that biological production can deliver more '
                'cheaply than chemical synthesis.\n\n'
                'The corporate history is displayed in the station\'s public areas with a '
                'candour that visitors find either refreshing or alarming. The original '
                'administrators who started the illicit crops under MERIT\'s nose are '
                'celebrated as founders. The conversion from grain to drug production is '
                'described as visionary pivoting. The MERIT-funded terraforming that made '
                'it all possible is acknowledged with what can only be described as '
                'gratitude.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='The Nurseries',
            short_description='Orbital growing facilities where the most sensitive genetic modification work is conducted -- controlled environments producing the next generation of crop strains.',
            long_description=(
                'The Nurseries are a network of orbital growing facilities above Soval -- '
                'enclosed, climate-controlled stations where the Verdaine Corporation\'s '
                'genetic engineers test new crop strains before they are deployed to the '
                'surface. The controlled environment allows the researchers to isolate '
                'variables that surface growing cannot: precise light spectra, exact '
                'nutrient mixes, and the ability to observe multiple generations of a '
                'modified strain in compressed timeframes.\n\n'
                'The Nurseries are where the next generation of potency is born. Each '
                'successful modification -- a strain that produces a higher concentration '
                'of a target compound, or a new compound entirely, or the same compound '
                'with fewer unwanted byproducts -- is tested in the Nurseries before being '
                'scaled to Soval\'s surface operations. The progression over generations has '
                'been steady and dramatic: the current crop strains produce compounds at '
                'concentrations that the original wild plants could not approach, tailored '
                'to pharmaceutical applications with a specificity that improves with every '
                'iteration. The Nurseries are the engine of this progression, and the '
                'Verdaine Corporation guards them accordingly.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Terrath',
            short_description='A gas giant with fuel processing -- supporting the freighter traffic that carries Soval\'s output to the processing plants on Dschubba.',
            long_description=(
                'Terrath is the system\'s gas giant -- fuel processing on its moons '
                'supporting the freighter traffic that moves Soval\'s harvested crop '
                'material to the processing plants on Dschubba and the distribution '
                'networks beyond. The traffic is steady -- Soval\'s output is continuous '
                'rather than seasonal, because the genetically modified crop strains have '
                'been engineered for year-round production rather than the cyclical growing '
                'patterns that natural agriculture follows. The freighters arrive empty and '
                'depart loaded, and the fuel workers on Terrath\'s moons keep them fuelled '
                'with the same steady rhythm.'
            ),
            population=20_000_000,
        ),
    ],
    short_description='A MERIT-terraformed agricultural world turned drug plantation -- where the soil that was paid for with inner-system taxes grows the compounds that fund the war against them.',
    long_description=(
        'Yed Prior is the Antares cluster\'s most pointed irony. The system was '
        'discovered in the 2900s and terraformed by MERIT as an agricultural colony -- '
        'atmospheric processing, soil engineering, the full programme, funded by the '
        'inner systems\' taxes and executed by MERIT\'s colonial planners. The result was '
        'a world of exceptional agricultural potential. The administrators who managed '
        'the colony recognised this potential and applied it to crops that MERIT had '
        'not sanctioned.\n\n'
        'The illicit growing started as a side business -- a few fields of naturally '
        'occurring stimulant plants hidden in the agricultural data while MERIT\'s '
        'distant auditors checked the grain output and found it satisfactory. When the '
        'outer systems declared independence, the side business became the main '
        'business. The quiet operation incorporated as the Verdaine Corporation. The '
        'grain fields were converted to drug crops. The genetic engineers who had been '
        'discreetly improving the strains were given resources and freedom. Over '
        'generations of modification, the crops have grown in potency until the current '
        'strains bear almost no resemblance to the wild plants that the original '
        'administrators cultivated.\n\n'
        'Two billion people live in Yed Prior. Soval, the primary world, is the '
        'Verdaine Corporation\'s production base -- the MERIT-terraformed soil growing '
        'engineered drug crops at costs that rival Dschubba\'s chemical synthesis for '
        'certain compound families. Kelden, the second world, still grows food, '
        'because even a drug company needs to feed its people. The Nurseries -- orbital '
        'growing facilities above Soval -- develop the next generation of strains, '
        'pushing potency and specificity further with every iteration.\n\n'
        'The Verdaine Corporation competes with the Lucirin Corporation and the other '
        'pharmaceutical giants of the cluster, carving out a market position built on '
        'biological production\'s cost advantages over chemical synthesis. The '
        'corporation is not the largest in the cluster. It is the one whose founding '
        'story most embarrasses MERIT: an agricultural colony, terraformed at MERIT\'s '
        'expense, growing drugs under MERIT\'s nose before independence, and now '
        'producing the compounds that fund the faction fighting against them. The '
        'corporate history celebrates the original administrators as visionaries. '
        'MERIT\'s strategic briefings describe them with different language.'
    ),
    cluster=StarClusters.ANTARES,
)

LESATH = System(
    name='Lesath',
    star='Blue-white subgiant (B2IV), approximately 8,000 times Sol luminosity',
    population=1_500_000_000,
    distance_to_sol=580.0,
    stellar_objects=[
        StellarObject(
            name='Rathke',
            short_description='The most populated world -- a billion people living in armed camps that raid each other and everyone else, united only by their refusal to be united.',
            long_description=(
                'Rathke is a habitable world in the way that a place with breathable air '
                'and drinkable water is habitable. The planet supports a billion people. '
                'The planet does not support a civilisation. There is no government on '
                'Rathke. There are no institutions. There is no police force, no judiciary, '
                'no administrative apparatus of any kind. What exists is territory -- '
                'patchworks of armed communities that control the land they can defend and '
                'raid the land they cannot hold. The boundaries shift constantly. The '
                'violence is endemic.\n\n'
                'The communities range from fortified settlements of tens of thousands to '
                'roving bands of a few hundred. The larger settlements have walls, weapons '
                'emplacements, and the grim organisation of people who have learned that '
                'defence is the first requirement of survival. The smaller bands are mobile '
                '-- raiding the settlements for supplies, hitting the weaker communities, '
                'and relocating before a coordinated response can form. Coordinated '
                'responses rarely form. Coordination requires trust, and trust does not '
                'exist on Rathke.\n\n'
                'The stims on Rathke are combat-oriented -- reaction accelerants and '
                'aggression enhancers that the Antarian military uses in controlled doses '
                'and that Rathke\'s fighters use in whatever quantities they can obtain. '
                'The compounds are acquired through raiding -- stolen from shipments bound '
                'for other systems, traded from smugglers, or manufactured in crude local '
                'labs that produce compounds of unpredictable quality and frequently lethal '
                'potency. A fighter on Rathke is either on stims or dead, and the stims '
                'they are on are the most dangerous in the cluster because quality control '
                'does not exist when there is no one to enforce it.\n\n'
                'The Antarian government has tried to bring Lesath under control. The '
                'attempts have failed because the cost of pacification exceeds the value '
                'of the system, and because the population of Rathke fights the Antarian '
                'military with the same ferocity it fights itself. Lesath was unruly before '
                'independence. It did not become less unruly when the authority changed. '
                'The population does not recognise the Antarian government\'s legitimacy '
                'any more than it recognised MERIT\'s. It does not recognise anyone\'s '
                'legitimacy. The concept is foreign here.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Torburn',
            short_description='A harsh second world -- where the communities that were driven off Rathke reestablished and became raiders themselves.',
            long_description=(
                'Torburn is the system\'s second habitable world -- hotter, drier, and '
                'less hospitable than Rathke. The population is smaller and arrived not by '
                'colonial planning but by displacement: communities that lost their '
                'territory on Rathke, bands that were driven out by stronger rivals, and '
                'the people who decided that starting over on a worse planet was preferable '
                'to dying on a better one. Torburn\'s settlements are newer, rougher, and '
                'built by people whose first experience of community was losing one.\n\n'
                'The raiders who operate from Torburn are the system\'s primary threat to '
                'the rest of the cluster. Rathke\'s violence is mostly internal -- the '
                'communities fight each other. Torburn\'s population has less to fight over '
                'locally and more reason to look outward. The raiding ships that strike '
                'Shaula\'s transports, that hit Acrab\'s freighter convoys, that pick off '
                'isolated vessels in the transit routes between Antarian systems -- a '
                'disproportionate number originate from Torburn. The planet does not have '
                'a navy. It has hundreds of independent operators who own armed ships and '
                'use them to take what they need from people who cannot stop them.\n\n'
                'Shaula is the preferred target. Shaula\'s labour transports are large, '
                'slow, lightly armed, and carry human cargo that can be ransomed or sold '
                'or put to work. The Torburn raiders intercept the transports, strip what '
                'is valuable, and disappear back into Lesath\'s space where pursuit is '
                'dangerous because the system has no traffic control, no navigation '
                'beacons, and the local pilots know the routes that outsiders do not.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='The Scrapfield',
            short_description='An orbital debris zone of stripped ships and stolen hulls -- Lesath\'s shipyard, where raiders refit and repair from the wreckage of their victims.',
            long_description=(
                'The Scrapfield is the closest thing Lesath has to infrastructure -- a zone '
                'of orbital space above Rathke where the accumulated wreckage of decades '
                'of raiding has collected. Stripped hulls, salvaged components, stolen '
                'cargo containers, and the remains of ships that were taken intact and '
                'cannibalised for parts. The Scrapfield is not organised. It is not '
                'maintained. It is a junkyard in orbit, and it is where the raiders go '
                'to repair their ships, refit with salvaged weapons, and trade the stolen '
                'goods that are the system\'s primary economy.\n\n'
                'The trading in the Scrapfield is conducted under the only rule that Lesath '
                'universally observes: you do not attack someone while trading. The rule '
                'exists because without it, trading would be impossible, and without '
                'trading, the raiders cannot convert their stolen goods into the supplies '
                'they need. The rule is enforced by consensus -- a raider who violates it '
                'is blacklisted by everyone, which in a system with no law means that '
                'nobody will trade with them and everybody will target them. The punishment '
                'is effective because it is the only social contract that Lesath\'s '
                'population has agreed to, and they enforce it with the energy of people '
                'who have nothing else to rely on.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Vetch',
            short_description='A gas giant where fuel is taken rather than processed -- the raiders skim the atmosphere directly because nobody has built the infrastructure to do it properly.',
            long_description=(
                'Vetch is the system\'s gas giant -- a mid-sized body in the outer system '
                'that would, in any other system, host fuel processing facilities on its '
                'moons. Lesath has no fuel processing facilities. Building facilities '
                'requires investment, and investment requires confidence that the facility '
                'will not be raided by the people it is intended to serve. Nobody in Lesath '
                'has that confidence.\n\n'
                'The raiders fuel their ships by skimming Vetch\'s upper atmosphere directly '
                '-- diving into the gas giant\'s atmosphere with ships whose inertial '
                'resonators are powerful enough to survive the descent, scooping raw '
                'hydrogen, and processing it aboard in crude shipboard refineries. The '
                'method is inefficient, dangerous, and produces fuel of inconsistent '
                'quality. It is also the only method available when there is no '
                'infrastructure and no one willing to build any. Vetch\'s atmosphere has '
                'claimed ships -- pilots who misjudged the depth or whose resonators '
                'failed under the pressure. The losses are accepted as a cost of doing '
                'business in a system where every cost is accepted because the alternative '
                'is not operating at all.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dross',
            short_description='A frozen outer body where the most paranoid and dangerous operators maintain hidden caches -- weapons, stims, and the proceeds of raids too valuable to keep on a ship.',
            long_description=(
                'Dross is a frozen body in the outer system -- airless, dark, and used by '
                'the system\'s more successful raiders as a cache site. The surface is '
                'dotted with hidden storage facilities -- some carved into the ice, others '
                'buried beneath the surface -- containing weapons, stim stockpiles, '
                'valuable salvage, and the accumulated proceeds of raids that are too '
                'valuable to keep aboard a ship that might be raided in turn.\n\n'
                'The caches are secrets. A raider\'s cache is their insurance, their '
                'retirement, and their vulnerability -- the knowledge of its location is '
                'the most valuable thing a competitor could learn. The surface of Dross is '
                'unmarked. The caches are located by memory and personal navigation that '
                'the operators do not share with anyone, including their own crews. The '
                'frozen surface is pocked with the evidence of raiders who tried to find '
                'someone else\'s cache: excavation marks, blasting scars, and the '
                'occasional frozen remains of people who went looking and found the '
                'booby traps instead.'
            ),
            population=0,
        ),
    ],
    short_description='The cluster\'s internal wound -- a pirate system that preys on its own, ungovernable by any authority including the one it nominally belongs to.',
    long_description=(
        'Lesath is the Antares cluster\'s embarrassment. A system of one and a half '
        'billion people who refuse to be governed, who fight each other and everyone '
        'else, and who have resisted every attempt at pacification by the Antarian '
        'government with the same ferocity they resisted MERIT before independence. '
        'Lesath was unruly under MERIT. It is unruly under the Antarian government. It '
        'will be unruly under whatever authority replaces the current one, because the '
        'population does not recognise authority as a concept.\n\n'
        'Rathke, the primary world, is a patchwork of armed communities that control '
        'what they can defend and raid what they cannot hold. There is no government, '
        'no police, no institutions of any kind. The stims are combat-oriented and '
        'acquired through theft, smuggling, and crude local manufacturing. Torburn, '
        'the second world, is worse -- settled by people driven off Rathke, its raiders '
        'are the cluster\'s primary internal security threat, striking Shaula\'s labour '
        'transports, Acrab\'s freighter convoys, and isolated vessels throughout '
        'Antarian space.\n\n'
        'The system has no infrastructure. The Scrapfield -- an orbital junkyard of '
        'stripped ships and stolen hulls -- serves as a shipyard and trading post under '
        'the only rule Lesath observes: no attacking during trades. The raiders fuel '
        'their ships by skimming Vetch\'s atmosphere directly because nobody will build '
        'processing facilities that would be immediately raided. The caches on Dross '
        'hold the proceeds of raids too valuable to keep on a ship.\n\n'
        'The Antarian government has calculated the cost of pacifying Lesath and '
        'decided it is not worth the expense. The system is contained rather than '
        'controlled -- the Antarian fleet patrols the routes between Lesath and the '
        'rest of the cluster, interdicting the raiders when possible and accepting the '
        'losses when not. The raids on Shaula\'s transports are a persistent drain. The '
        'cost is borne by the people who can least afford it -- the indentured workers '
        'who are captured, the transports that are stripped, the supply chains that are '
        'disrupted. Lesath takes from the weak because the strong are too expensive to '
        'fight. This is the system\'s only consistent principle.'
    ),
    cluster=StarClusters.ANTARES,
)

SULAFAT = System(
    name='Sulafat',
    star='Blue-white giant (B9III), approximately 2,500 times Sol luminosity',
    population=9_000_000_000,
    distance_to_sol=620.0,
    stellar_objects=[
        StellarObject(
            name='Calloden',
            short_description='The most populous world -- five billion people who use stims the way other systems use coffee, and consider the rest of the cluster\'s intensity a form of collective madness.',
            long_description=(
                'Calloden is a temperate, well-terraformed world where five billion people '
                'live at a pace that the rest of the Antares cluster finds baffling. The '
                'population uses stims. Everyone in the cluster uses stims. The difference '
                'is degree. Where Kaelin\'s traders are on cognitive enhancers that push '
                'them to the edge of human processing speed, Calloden\'s traders are on '
                'light focus compounds that sharpen attention without accelerating it. '
                'Where Dekhar\'s miners are on endurance boosters that suppress pain and '
                'fatigue for twelve-hour shifts, Calloden\'s workers are on mild '
                'sustainers that extend the working day by an hour or two without the '
                'tremors and the crash.\n\n'
                'The culture on Calloden has made a deliberate, sustained choice to use '
                'less. The choice was not ideological -- nobody on Calloden is anti-stim '
                'in the way that MERIT\'s critics are. The choice was pragmatic. The '
                'founding population, drawn from across the cluster, looked at what heavy '
                'stim use produced -- the productivity but also the tremors, the burnout, '
                'the shortened lives, the narrowing that Lindern\'s researchers document '
                'even in the wealthy -- and decided that the trade-off was not worth it. '
                'They would use enhancement. They would use less of it. They would be '
                'less productive per capita and more intact per person.\n\n'
                'The result is a world that moves at a different speed. The conversations '
                'are slower. The working day is shorter. The productivity per capita is '
                'lower than the cluster average. The restaurants close earlier. The '
                'evenings are spent in ways that the residents of Kaelin and Antares would '
                'consider a waste of enhanced hours: cooking, walking, sitting with family, '
                'the unremarkable activities of people who are not optimising every waking '
                'moment. The rest of the cluster calls Calloden lazy. Calloden calls the '
                'rest of the cluster addicts. Both descriptions are reductive. Neither is '
                'entirely wrong.\n\n'
                'The health outcomes are measurable. Calloden\'s population lives longer '
                'than any other system in the cluster. The tremor rate is negligible. The '
                'cognitive erosion that Lindern\'s researchers track in even the best-'
                'enhanced populations is present on Calloden at rates so low that the '
                'researchers initially assumed their instruments were miscalibrated. They '
                'were not. The people of Calloden are simply less enhanced and more '
                'themselves, and the data shows it.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Tessim',
            short_description='The second world -- warmer, agricultural, and where the lighter stim culture produces farmers who work at human pace and finish the day without shaking.',
            long_description=(
                'Tessim is the system\'s agricultural world -- warm, fertile, and farmed at '
                'a pace that Acrab\'s operators would consider uncompetitive. The yields per '
                'hectare are lower. The working hours are shorter. The farmers use mild '
                'sustainers during planting and harvest and nothing at all during the '
                'quieter months. The output feeds the system and produces a modest surplus '
                'for export -- not the enormous volumes that Acrab ships across the cluster '
                'but enough to contribute to the supply chain.\n\n'
                'The farming communities on Tessim are the system\'s cultural heart -- '
                'slower-paced, family-oriented, and shaped by seasonal rhythms that the '
                'year-round production schedules of other Antarian agricultural worlds have '
                'eliminated. The farmers on Tessim have harvests and fallow periods, busy '
                'seasons and quiet ones, and the culture cycles with them. The festivals '
                'that mark the seasons are the system\'s largest communal events -- '
                'celebrations that the rest of the cluster regards with puzzled amusement, '
                'because the festivals are not enhanced. The food is cooked by hand. The '
                'music is played at tempos that unenhanced ears can follow. The dancing is '
                'at speeds that unenhanced bodies can sustain. The festivals feel, to '
                'visitors from other Antarian systems, like something from a different '
                'century.'
            ),
            population=1_800_000_000,
        ),
        StellarObject(
            name='Varden',
            short_description='A temperate third world -- light industry and services, operating at Sulafat\'s characteristic unhurried pace.',
            long_description=(
                'Varden is the system\'s industrial and service world -- temperate, '
                'well-developed, and producing the manufactured goods and services that the '
                'system\'s economy needs. The factories operate at a pace that Sargas\'s '
                'industrial managers would find maddening -- single shifts where Sargas '
                'runs three, maintenance schedules that prioritise equipment longevity over '
                'output maximisation, and a workforce that goes home at the end of the day '
                'and does not come back until tomorrow.\n\n'
                'The economic output per capita on Varden is lower than the cluster average. '
                'The economic output per unit of human suffering is, the residents would '
                'argue, the highest in the galaxy. The factories run. The goods are '
                'produced. The workers are healthy. The trade-off is volume, and Sulafat '
                'has decided that volume is someone else\'s problem. The system imports '
                'what it cannot produce at its own pace and pays for the imports with the '
                'exports it does produce. The economics work. They work modestly. The '
                'residents are fine with modest.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Kelbridge',
            short_description='The system\'s orbital port -- where visitors from other Antarian systems arrive and immediately notice that everything moves at a different speed.',
            long_description=(
                'Kelbridge is Sulafat\'s primary orbital station -- a modern, well-'
                'maintained facility that handles the system\'s traffic at a pace that '
                'visiting crews find disorienting. The docking procedures are unhurried. '
                'The cargo processing is thorough rather than fast. The communications are '
                'conducted at a speed that assumes the listener is paying attention rather '
                'than chemically accelerated. A pilot arriving from Gantry -- where the '
                'traffic control operates at stimmed speed and expects the same -- '
                'experiences Kelbridge as a station operating in slow motion.\n\n'
                'The station\'s commercial district is pleasant in a way that other '
                'Antarian stations are not. The restaurants serve meals that are eaten '
                'rather than consumed between tasks. The bars close at reasonable hours. '
                'The staff are friendly without the manic energy that heavy stim use '
                'produces. Visiting crews from other systems react in one of two ways: '
                'some find it infuriating, an entire system operating below capacity by '
                'choice. Others find it restful in a way they did not expect and stay '
                'longer than they planned. The second group sometimes does not leave. '
                'Sulafat\'s immigration rate from other Antarian systems is the highest '
                'in the cluster.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Durrant',
            short_description='A gas giant with fuel processing -- operated on single shifts at a pace that services the system\'s moderate traffic without urgency.',
            long_description=(
                'Durrant is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The operations run on single shifts. The '
                'workers go home at the end of the day. The fuel is processed on schedule '
                'and without the round-the-clock urgency that characterises fuel operations '
                'in the busier systems. The traffic volume is moderate -- Sulafat is not a '
                'major trade hub and does not aspire to be one.\n\n'
                'The fuel workers on Durrant\'s moons are on the same light sustainers as '
                'the rest of the system -- enough to stay focused through a shift, not '
                'enough to feel enhanced. They describe the work as steady. In a cluster '
                'where fuel workers in other systems are on endurance compounds that let '
                'them work double shifts and hate the experience, steady is a luxury.'
            ),
            population=25_000_000,
        ),
        StellarObject(
            name='Solwen',
            short_description='A cool outer world hosting clinics where people from across the cluster come to step down from heavy stim use -- the only such facility in Antarian space.',
            long_description=(
                'Solwen is a cool, quiet world in the outer habitable zone that hosts '
                'Sulafat\'s most distinctive institution: the reduction clinics. These are '
                'medical facilities where people from across the Antares cluster come to '
                'step down from heavy stim use to the lighter regimes that Sulafat\'s '
                'culture favours. The process is medically managed -- withdrawal from heavy '
                'stims is dangerous and the step-down must be gradual, supervised, and '
                'supported by replacement compounds that ease the transition.\n\n'
                'The clinics are not abstinence programmes. They do not preach sobriety. '
                'The goal is not zero enhancement -- the staff are on light stims '
                'themselves. The goal is reduction: from the heavy compounds that the '
                'cluster\'s economy demands to the lighter regimes that Sulafat has proven '
                'are sustainable. The patients are people who have decided that the '
                'productivity is not worth the cost -- executives whose tremors have '
                'started, factory workers whose cognition is eroding, military personnel '
                'whose comedowns have become medically dangerous. They come to Solwen, '
                'they spend months stepping down, and they either stay in Sulafat or '
                'return to systems where the economy will push them back to heavy use '
                'within a year.\n\n'
                'The corporations do not officially acknowledge the clinics. Unofficially, '
                'the corporate executives who can afford to choose use Solwen\'s services '
                'themselves -- discreetly, privately, stepping down to the lighter regimes '
                'that will extend their careers and their lives. The clinics are the '
                'cluster\'s quiet admission that the system has a cost, and Sulafat is the '
                'only place in the Antares that has built an alternative.'
            ),
            population=45_000_000,
        ),
    ],
    short_description='The cluster\'s slow lane -- nine billion people who chose to use less, produce less, and keep more of themselves intact.',
    long_description=(
        'Sulafat is the Antares cluster\'s anomaly: a system of nine billion people '
        'who use stims lightly and consider the rest of the cluster insane for doing '
        'otherwise. The population is enhanced -- everyone in the cluster is enhanced '
        '-- but the degree is different. Light focus compounds instead of cognitive '
        'accelerants. Mild sustainers instead of endurance boosters. Enhancement that '
        'sharpens without distorting, that extends the day without consuming the '
        'person. The choice was pragmatic rather than ideological: the founding '
        'population looked at what heavy stim use produced and decided the trade-off '
        'was not worth it.\n\n'
        'The result is a system that moves at a different speed. The productivity per '
        'capita is lower than the cluster average. The health outcomes are the best in '
        'the cluster -- longer lives, negligible tremor rates, cognitive erosion so '
        'low that the researchers on Lindern initially thought their instruments were '
        'broken. The working days are shorter. The evenings are spent cooking, walking, '
        'sitting with family -- activities that the heavily enhanced populations of '
        'other systems consider a waste of optimisable hours and that Sulafat considers '
        'the point of being alive.\n\n'
        'The rest of the cluster calls Sulafat lazy. Sulafat calls the rest of the '
        'cluster addicts. The corporations tolerate Sulafat because its economic '
        'output, while modest, is sufficient and its population is stable and healthy '
        'and does not require the constant replacement that the heavily enhanced '
        'systems demand. The military tolerates Sulafat because its personnel, while '
        'less explosive in combat, are more consistent and do not crash mid-engagement. '
        'The immigration rate from other Antarian systems is the highest in the '
        'cluster -- people who have decided that the intensity is not worth the cost '
        'and who come to Sulafat for the slower pace and stay for the longer life.\n\n'
        'Solwen, the outer world, hosts the cluster\'s only reduction clinics -- '
        'medical facilities where people from across the Antares step down from heavy '
        'use to lighter regimes. The clinics are not abstinence programmes. The goal '
        'is not zero. The goal is less. In a cluster that has made more into a '
        'religion, less is the closest thing Sulafat has to a creed.'
    ),
    cluster=StarClusters.ANTARES,
)

SADAL = System(
    name='Sadal',
    star='Yellow supergiant (G0Ib), approximately 2,200 times Sol luminosity -- warm, golden light unlike anything else in the Antares cluster',
    population=7_000_000_000,
    distance_to_sol=540.0,
    stellar_objects=[
        StellarObject(
            name='Aureth',
            short_description='The capital world -- four billion people living in golden light, proud to be Antarian, proud to be free, and convinced the rest of the galaxy is missing out.',
            long_description=(
                'Aureth is beautiful. The warm golden light of the yellow supergiant gives '
                'the planet a quality that no inner-system world can match -- everything is '
                'bathed in deep amber-gold, from the architecture to the oceans to the '
                'faces of the four billion people who live here and who will tell you, at '
                'length and with genuine feeling, that they would not live anywhere else.\n\n'
                'The pride on Aureth is not the manufactured patriotism of Kalinan or the '
                'corporate showcase of Kaus. It is the organic conviction of people who '
                'believe their way of life is genuinely good and who have evidence to '
                'support the belief. The evidence is the life itself. The cities on Aureth '
                'are vibrant -- not planned to MERIT\'s precise specifications but grown '
                'organically, shaped by the preferences of the people who live in them, '
                'full of the messy individuality that MERIT\'s urban planning optimises '
                'away. The markets are unregulated -- not in the Lesath sense of lawless, '
                'but in the sense that people sell what they want, where they want, without '
                'the permitting and zoning and oversight that MERIT\'s framework imposes. '
                'The art is everywhere. The music is everywhere. The expression is '
                'unconstrained in ways that inner-system citizens find exhilarating or '
                'overwhelming depending on their tolerance for chaos.\n\n'
                'The freedoms that Aureth\'s population celebrates are specific. The freedom '
                'to modify your own body without MERIT\'s medical regulations dictating what '
                'is permissible. The freedom to start a business without MERIT\'s economic '
                'planners deciding whether the market needs it. The freedom to build your '
                'home in the style you choose rather than the style the planning authority '
                'mandates. The freedom to say what you think about the government without '
                'the conversation being logged by systems that track sentiment for '
                'administrative purposes. The residents of Aureth consider these freedoms '
                'fundamental. The residents of the inner systems do not realise they are '
                'missing them, which Aureth\'s population considers the saddest thing about '
                'living under MERIT.\n\n'
                'The stims are part of the freedom. On Aureth, you choose your own '
                'enhancement -- what compounds, what dosage, what schedule. There is no '
                'employer-mandated regime, no corporate-selected formulation, no pressure '
                'to enhance beyond what you personally want. Some people on Aureth are '
                'heavily enhanced. Some use light compounds. A small minority uses nothing '
                'at all. The choice is individual, and the individuality of the choice is '
                'the point.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Talessen',
            short_description='The second world -- where the golden light falls on open land and settlers build what they want, how they want, because nobody is going to stop them.',
            long_description=(
                'Talessen is the system\'s second habitable world -- temperate, spacious, '
                'and settled with the frontier energy of people who chose to start fresh '
                'with no restrictions. The planet has land to spare -- the population is '
                'smaller than Aureth\'s and the settlements are spread out, each community '
                'building according to its own preferences without the standardisation '
                'that MERIT\'s colonial framework imposes.\n\n'
                'The result is a world of extraordinary variety. One settlement is a '
                'vertical city of towers connected by sky bridges, built by architects who '
                'wanted to see how high they could go. The next is a sprawling low-rise '
                'commune spread across a river valley, built by people who wanted space and '
                'quiet. A third is an experimental community where the buildings are grown '
                'from engineered biological material rather than constructed. A fourth is a '
                'conventional town that looks like it could be anywhere in the inner systems '
                'except for the golden light and the absence of planning permits.\n\n'
                'Talessen is where the Antarian independence argument is most persuasive. '
                'The communities are functional. The people are fed, housed, and healthy. '
                'The economy works -- not with MERIT\'s optimised efficiency but with the '
                'adaptive messiness of people figuring things out for themselves. The '
                'infrastructure is imperfect. The hospitals vary in quality. The schools '
                'are not standardised. And the residents would not trade any of it for the '
                'guarantee of MERIT\'s baseline, because the guarantee comes with a '
                'framework that tells you how to build your house and where to put it and '
                'what colour it should be, and Talessen considers that a price too high '
                'to pay for reliable plumbing.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Korabel',
            short_description='The system\'s creative hub -- an orbital station where artists from across the cluster come because Sadal doesn\'t censor.',
            long_description=(
                'Korabel is an orbital station above Aureth that has become the Antares '
                'cluster\'s cultural centre -- not by design but by accumulation. Artists, '
                'musicians, writers, performers, and the uncategorisable creative people '
                'who do not fit into any system\'s economic planning have gravitated to '
                'Sadal because Sadal does not tell them what to create. The station has '
                'filled with studios, galleries, performance spaces, and the chaotic '
                'infrastructure of a creative community that grew without anyone managing '
                'it.\n\n'
                'The art produced on Korabel is the Antares cluster\'s most distinctive '
                'cultural export. The work is raw, diverse, and unconstrained in ways that '
                'inner-system art is not -- MERIT\'s cultural frameworks, while not formally '
                'censorious, produce art that operates within understood boundaries of '
                'taste and subject matter. Korabel has no boundaries. The work ranges from '
                'brilliant to terrible, from profound to vulgar, from the kind of art that '
                'makes visitors weep to the kind that makes them leave the room. The '
                'freedom is total. The quality control is nonexistent. The residents '
                'consider both of these features rather than bugs.\n\n'
                'Korabel is also where the Antarian independence message is crafted for '
                'export. The artists and propagandists -- the line between them is blurred '
                'here -- produce the content that is distributed across the galaxy: the '
                'stories of freedom, the images of golden-lit cities, the music that '
                'carries the emotional case for independence that the political arguments '
                'alone cannot make. The content is not directed by the corporations or the '
                'government. It does not need to be. The artists of Korabel believe in the '
                'message because they are living it.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='Sumaren',
            short_description='An agricultural world under golden light -- the crops grow in amber and the farmers consider industrial agriculture an obscenity.',
            long_description=(
                'Sumaren is the system\'s agricultural world -- warm, fertile, and farmed '
                'with an approach that reflects Sadal\'s values. The farming is productive '
                'but not industrialised to the degree that Acrab\'s operations are -- the '
                'farms are smaller, more varied, and managed by operators who choose their '
                'own methods rather than following corporate directives. The output feeds '
                'the system and produces a modest surplus.\n\n'
                'The golden light of the supergiant gives Sumaren\'s agricultural landscape '
                'a quality that the residents describe as irreplaceable -- the crops grow '
                'under amber skies, the fields are warm gold at harvest time, and the '
                'visual character of the planet is unlike any other agricultural world in '
                'the cluster. The farmers on Sumaren consider Sheratan\'s mathematical '
                'monocultures and Acrab\'s industrial operations obscene -- agriculture '
                'reduced to equations, land treated as a production input rather than a '
                'living system. The residents would rather produce less and produce it '
                'their way.'
            ),
            population=700_000_000,
        ),
        StellarObject(
            name='Galdren',
            short_description='A gas giant with fuel processing -- independently operated by a cooperative, because even the fuel workers in Sadal refused to work for a corporation.',
            long_description=(
                'Galdren is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The operations are run by an independent '
                'cooperative rather than a corporation -- the workers own the operation '
                'collectively, set their own schedules, and sell fuel at prices they '
                'determine without corporate intermediaries. The arrangement is less '
                'efficient than a corporate operation and the fuel costs more than it would '
                'in Antares or Dschubba. The workers consider the premium a fair price for '
                'not having a manager.\n\n'
                'The cooperative model on Galdren is characteristic of Sadal\'s economy -- '
                'less optimised, more autonomous, and sustained by people who value '
                'ownership of their own work above the efficiency that surrendering control '
                'would provide.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='The Reach',
            short_description='An outer-system settlement of people who wanted to be even freer -- the system\'s most radical community, testing the limits of what independence means.',
            long_description=(
                'The Reach is a small settlement on a cold outer body -- home to a '
                'community that considered even Sadal\'s freedom insufficient and moved to '
                'the edge of the system to build something more radical. The community '
                'operates without formal governance of any kind -- decisions are made by '
                'consensus, property is communal, and the stim use is entirely '
                'unmonitored.\n\n'
                'The Reach is a social experiment that the rest of Sadal regards with '
                'affectionate scepticism. The community has survived for decades, which '
                'its residents consider proof that radical freedom works. The community is '
                'also small, isolated, and dependent on supply shipments from Aureth for '
                'goods it cannot produce, which the sceptics consider proof that radical '
                'freedom works only when someone else is growing the food. The argument '
                'continues. The Reach endures. The supplies keep coming, because Sadal '
                'believes in the freedom to try even when the trying looks impractical.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='Freedom in golden light -- seven billion people living the Antarian ideal, proud and convinced that the rest of the galaxy should join them.',
    long_description=(
        'Sadal is the Antares cluster\'s truest believer. Seven billion people living '
        'under the warm golden light of a yellow supergiant, in cities they built '
        'without permission, running businesses they started without approval, making '
        'art that nobody vetted, and choosing their own stim regimes without an '
        'employer or a medical authority dictating the terms. The population is proud '
        'to be Antarian -- not in the manufactured sense of corporate propaganda but in '
        'the genuine sense of people who believe their way of life is worth defending '
        'because they are living it and it is good.\n\n'
        'The freedom is real. The cities on Aureth are vibrant and messy and shaped by '
        'the preferences of the people who live in them rather than the specifications '
        'of planners. The settlements on Talessen are wildly varied -- each community '
        'built according to its own vision, functional and imperfect and owned by the '
        'people who made them. The art on Korabel is unconstrained and ranges from '
        'brilliant to terrible because freedom does not guarantee quality, only the '
        'opportunity to produce it. The farms on Sumaren are productive and '
        'unoptimised and the farmers would rather produce less their way than more '
        'someone else\'s way.\n\n'
        'Sadal is the emotional case for Antarian independence. Kaus is the economic '
        'showcase -- the proof that the stim economy can produce prosperity. Sadal is '
        'the cultural argument -- the proof that independence produces a way of life '
        'that people genuinely love and that MERIT\'s framework cannot replicate because '
        'the framework is the thing that Sadal\'s people rejected. The cities are '
        'imperfect. The infrastructure is uneven. The hospitals vary in quality. And '
        'the residents would not trade any of it for the guarantee of MERIT\'s baseline, '
        'because the guarantee comes with controls that Sadal\'s population considers '
        'worse than the problems the controls are designed to solve.\n\n'
        'The golden light of the supergiant makes everything look the way Sadal feels '
        '-- warm, rich, suffused with a quality that the residents consider irreplaceable '
        'and that visitors from the inner systems find either intoxicating or naive. '
        'The residents do not mind being called naive. They mind being called subjects. '
        'The distinction matters to them more than any criticism, and the golden light '
        'falls on a civilisation that has made freedom its identity and will not '
        'surrender it for anything MERIT can offer.'
    ),
    cluster=StarClusters.ANTARES,
)

ATR_1156 = System(
    name='ATR_1156',
    star='Orange dwarf (K3V), approximately 0.4 times Sol luminosity -- dim, stable, and unremarkable',
    population=0,
    distance_to_sol=520.0,
    stellar_objects=[
        StellarObject(
            name='ATR_1156-a',
            short_description='A rocky world in the habitable zone -- technically terraformable, practically not worth the effort when better candidates exist closer to the supply chain.',
            long_description=(
                'ATR_1156-a is the system\'s only habitable-zone world -- a rocky planet '
                'with thin atmosphere and surface water in the polar regions. The survey '
                'team assessed it as terraformable in approximately two centuries of '
                'sustained work. Two centuries is a long time, and the Antares cluster has '
                'better candidates closer to Dschubba\'s pharmaceutical supply chain and '
                'Acrab\'s food exports. A colony this far from the cluster\'s infrastructure '
                'would need to be self-sustaining for extended periods, and a self-'
                'sustaining colony in the Antares means a colony that can produce its own '
                'stims -- a capability that the corporations have no interest in enabling '
                'because decentralised production undermines the supply monopoly.\n\n'
                'The survey data is filed in the Antarian colonial planning archive. The '
                'world is catalogued as ATR_1156-a because nobody cared enough to name it. '
                'The naming convention tells you everything: a system important enough to '
                'name is a system important enough to settle. ATR_1156 is not important '
                'enough to name.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR_1156-b',
            short_description='A hot inner world -- small, dense, mineral-poor, and the survey team\'s least interesting finding.',
            long_description=(
                'ATR_1156-b is a small, dense world in a close orbit -- hot, airless, and '
                'mineral-poor. The survey team spent less than a day on it. The report is '
                'a single page of standard measurements and a recommendation of no further '
                'investigation. In a cluster where Dekhar\'s mineral-rich crust feeds the '
                'shipyards, a mineral-poor rock orbiting a dim star is not worth the fuel '
                'it costs to survey it a second time.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR_1156-c',
            short_description='A small gas giant -- standard composition, no unusual features, fuel processing potential that nobody needs.',
            long_description=(
                'ATR_1156-c is a small gas giant in the outer system with a hydrogen-helium '
                'atmosphere and a handful of icy moons. The atmospheric composition is '
                'standard. The fuel processing potential is real and irrelevant -- there '
                'is no traffic in ATR_1156 that would require fuel, and no prospect of '
                'traffic developing. The gas giant orbits the dim star in the outer system, '
                'unprocessed and unvisited, one of thousands of similar bodies in the '
                'galaxy that are adequate for purposes that nobody has.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR_1156-d',
            short_description='A frozen outer body -- the last thing the survey team catalogued before leaving a system that gave them nothing to write home about.',
            long_description=(
                'ATR_1156-d is a frozen body in the far outer system -- ice and rock, no '
                'atmosphere, no features. The survey team catalogued it with the '
                'thoroughness that procedure requires and the enthusiasm that the system\'s '
                'mediocrity did not inspire. The entry in the survey log notes the body\'s '
                'mass, composition, and orbital parameters, and contains no additional '
                'commentary. The survey team moved on to the next system. ATR_1156 was '
                'added to the catalogue, given a number, and forgotten.'
            ),
            population=0,
        ),
    ],
    short_description='A surveyed, catalogued, and forgotten system -- not bad enough to be interesting, not good enough to be useful, not important enough to name.',
    long_description=(
        'ATR_1156 is a number in a catalogue. The system was surveyed during the '
        'Antares cluster\'s expansion, assessed by a team that followed standard '
        'procedure, and filed with a designation rather than a name because the results '
        'did not justify the dignity of one. The star is a dim orange dwarf. The '
        'habitable-zone world is technically terraformable in approximately two '
        'centuries. The inner world is mineral-poor. The gas giant is standard. The '
        'outer body is ice and rock.\n\n'
        'Nothing in ATR_1156 is bad. Nothing is good. The system is the definition of '
        'mediocre -- every world assessed as adequate and none assessed as worthwhile. '
        'The Antares cluster has better options closer to its supply chains, and a '
        'colony in ATR_1156 would face the additional problem of being too far from '
        'Dschubba to maintain the pharmaceutical supply that Antarian society requires. '
        'A colony without reliable stim supply in the Antares cluster is a colony in '
        'withdrawal, and the corporations have no interest in enabling decentralised '
        'production that would undermine their monopoly.\n\n'
        'ATR_1156 sits in the colonial planning archive alongside hundreds of other '
        'surveyed systems that did not make the cut. The data is complete and unread. '
        'If the cluster ever exhausts its better options, ATR_1156 will be there -- '
        'dim, adequate, and unnamed, waiting for someone to decide that mediocre is '
        'good enough.'
    ),
    cluster=StarClusters.ANTARES,
)

KORNEPHOROS = System(
    name='Kornephoros',
    star='Yellow giant (G7IIIa), approximately 150 times Sol luminosity -- warm golden light, smaller and brighter than Sadal\'s supergiant',
    population=4_000_000_000,
    distance_to_sol=139.0,
    stellar_objects=[
        StellarObject(
            name='Pelagir',
            short_description='An ocean world whose marine organisms produce neurologically active compounds -- the foundation of the Tethyn Corporation and the cluster\'s marine pharmaceutical industry.',
            long_description=(
                'Pelagir is a warm ocean world -- shallow seas covering most of the surface, '
                'with scattered archipelagos and a marine biosphere that the original survey '
                'team catalogued as unremarkable. The biochemists who followed the survey '
                'team disagreed. The marine organisms on Pelagir -- simple invertebrates, '
                'colonial filter-feeders, and the microbial mats that form the base of the '
                'food chain -- produce neurologically active compounds as part of their '
                'natural metabolism. The compounds are varied, potent, and in several cases '
                'unlike anything that synthetic chemistry or terrestrial biology has '
                'produced.\n\n'
                'The Tethyn Corporation was founded to exploit this discovery. The company '
                'farms the marine organisms at industrial scale -- vast enclosed sea farms '
                'covering thousands of square kilometres of shallow ocean, cultivating the '
                'organisms under controlled conditions that maximise the production of '
                'target compounds. The harvested biomass is processed in floating refineries '
                'that extract, purify, and concentrate the active compounds for shipment to '
                'Dschubba\'s formulation plants or direct sale to the cluster\'s markets.\n\n'
                'The Tethyn Corporation\'s products occupy a distinctive niche. The marine-'
                'derived compounds have properties that synthetic stims and crop-based '
                'products do not: a smoothness of onset that users describe as natural, a '
                'duration curve that tapers rather than crashes, and a lower incidence of '
                'the tremors and cognitive erosion that plague users of cruder compounds. '
                'The products are not cheap -- marine cultivation is slower and more '
                'resource-intensive than chemical synthesis or crop farming -- but the '
                'market for compounds that enhance without the characteristic harshness of '
                'industrial stims is large and growing.\n\n'
                'The population on Pelagir lives on the archipelagos and on floating '
                'platform settlements above the sea farms. The culture is maritime -- '
                'shaped by the ocean, the weather, and the rhythm of the cultivation '
                'cycles. The Tethyn Corporation is the dominant employer and the dominant '
                'political force. The relationship between the corporation and its '
                'workforce is better than most in the cluster -- the marine work is skilled, '
                'the compounds the workers use are the company\'s own mid-grade products, '
                'and the health outcomes are measurably better than the industrial '
                'populations on Dschubba or Sargas. Pelagir is not Kaus. But it is closer '
                'to Kaus than to Shaula, and in the Antares cluster that distinction is '
                'the difference between a life and a slow consumption.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Morrath',
            short_description='A world of vast subterranean fungal networks -- mined for the compounds they produce, and the foundation of the Rhizic Corporation.',
            long_description=(
                'Morrath is a cool, rocky world with a thin atmosphere and a surface that '
                'the survey team found unpromising. The discovery was underground. Morrath\'s '
                'crust is permeated by an enormous fungal network -- a subterranean biosphere '
                'that extends kilometres deep, feeding on geothermal energy and mineral '
                'substrates, producing biomass in quantities that the biologists who '
                'discovered it found difficult to credit. The fungal organisms are not '
                'complex by biological standards. They are extraordinarily productive, and '
                'the compounds they produce as metabolic byproducts include a family of '
                'neurologically active substances that the pharmaceutical industry found '
                'immediately interesting.\n\n'
                'The Rhizic Corporation was founded to harvest the fungal compounds. The '
                'extraction is mining rather than farming -- bore shafts sunk into the '
                'fungal networks, collection systems that tap the biomass and pump the '
                'compound-rich fluid to surface processing plants. The operation has the '
                'character of a mining industry rather than an agricultural one: hard hats, '
                'bore crews, shift work in tunnels that are warm, dark, and permeated by '
                'the faintly sweet smell of the fungal metabolism. The workers wear '
                'respiratory protection because the raw fungal compounds are active in '
                'their unprocessed form -- a lesson learned the same way Dizuo\'s dust was '
                'discovered, through accidental exposure and the unexpected clarity that '
                'followed.\n\n'
                'The Rhizic Corporation\'s products are the cluster\'s workhorses -- the '
                'endurance boosters and focus compounds that the industrial workforce '
                'depends on. The fungal-derived compounds are cheaper to produce than '
                'marine or synthetic equivalents, and the supply is effectively unlimited '
                '-- the fungal networks regenerate faster than the extraction operations '
                'can deplete them. The products are not premium. They are reliable, '
                'affordable, and available in the quantities that the cluster\'s billions '
                'of enhanced workers require. Rhizic\'s market position is volume, and the '
                'volume is vast.\n\n'
                'The rivalry between Tethyn and Rhizic defines Kornephoros. Two corporations '
                'in the same system, drawing from different biospheres, targeting different '
                'markets -- Tethyn\'s premium marine compounds versus Rhizic\'s bulk fungal '
                'products. The rivalry is commercial rather than violent, conducted through '
                'pricing wars, regulatory lobbying on Nunki, and the constant effort to '
                'encroach on each other\'s market segments. The workers on Morrath drink '
                'Tethyn\'s products when they can afford them and Rhizic\'s when they '
                'cannot, which tells you everything about the market positioning.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Arbitrage',
            short_description='The system\'s orbital station -- where Tethyn and Rhizic\'s products are traded side by side and the rivalry is conducted in real time on the exchange floor.',
            long_description=(
                'Arbitrage is the system\'s primary orbital station -- a facility that '
                'handles the trade traffic from both corporations and serves as the venue '
                'where their commercial rivalry plays out most visibly. The station\'s '
                'trading floor processes the pharmaceutical output of both worlds -- '
                'Tethyn\'s marine compounds and Rhizic\'s fungal products -- and the '
                'pricing dynamics between the two are a daily spectacle that the cluster\'s '
                'pharmaceutical traders watch closely.\n\n'
                'The station is divided by an informal geography that reflects the rivalry. '
                'The Tethyn-affiliated sections are sleek, maritime-themed, and cater to '
                'the premium market. The Rhizic-affiliated sections are utilitarian, '
                'practical, and process bulk orders at volumes that the Tethyn side cannot '
                'match. The common areas are where the two sides mix, and the bars in the '
                'common areas are where the commercial intelligence flows -- traders '
                'assessing production numbers, buyers comparing quality reports, and the '
                'brokers who play the two corporations against each other to extract better '
                'prices for their clients.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='Grevane',
            short_description='An agricultural world feeding the system -- neutral ground in the corporate rivalry, because both sides need to eat.',
            long_description=(
                'Grevane is the system\'s agricultural world -- temperate, fertile, and '
                'the one place in Kornephoros where the Tethyn-Rhizic rivalry does not '
                'dominate. The farming communities supply food to both worlds and both '
                'corporations, and the agricultural workers have cultivated a studied '
                'neutrality that serves them well commercially. A farmer on Grevane sells '
                'to Tethyn and Rhizic with equal willingness, attends neither corporation\'s '
                'promotional events, and changes the subject when the rivalry is raised at '
                'dinner. The neutrality is pragmatic -- picking a side means losing half '
                'your customers.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Sevander',
            short_description='A gas giant with fuel processing -- jointly operated by the two corporations in the system\'s only cooperative venture, conducted with mutual suspicion.',
            long_description=(
                'Sevander is the system\'s gas giant -- fuel processing on its moons '
                'supporting the trade traffic that both corporations generate. The fuel '
                'operation is the system\'s one joint venture: Tethyn and Rhizic co-fund '
                'the processing because neither wants the other to control the fuel supply, '
                'and neither can afford to operate a separate facility. The joint operation '
                'is conducted with the minimum cooperation necessary and the maximum '
                'suspicion available. The accounting is audited quarterly by both sides. '
                'The fuel allocation is negotiated monthly. The negotiations are described '
                'by participants as the most tedious experience in the cluster, which in a '
                'cluster that includes Nunki\'s regulatory process is a significant claim.'
            ),
            population=35_000_000,
        ),
    ],
    short_description='Two corporations, two biospheres, one system -- marine compounds and fungal extracts competing for the cluster\'s pharmaceutical market under warm golden light.',
    long_description=(
        'Kornephoros is a system defined by its rivalry. Two pharmaceutical '
        'corporations share the system and compete for the cluster\'s market: the '
        'Tethyn Corporation, harvesting neurologically active compounds from Pelagir\'s '
        'marine organisms, and the Rhizic Corporation, extracting similar compounds '
        'from Morrath\'s vast subterranean fungal networks. The products target '
        'different segments -- Tethyn\'s marine-derived compounds are premium products '
        'with smooth onset and gentle taper, while Rhizic\'s fungal extracts are the '
        'affordable workhorses that the cluster\'s industrial billions depend on. The '
        'rivalry is commercial rather than violent, conducted through pricing wars and '
        'regulatory lobbying rather than armed conflict.\n\n'
        'Four billion people live in Kornephoros across two production worlds, an '
        'agricultural support world, and the orbital station where the rivalry plays '
        'out on the trading floor. Pelagir\'s marine culture and Morrath\'s mining '
        'culture are as different as the biospheres they harvest -- one shaped by '
        'ocean and weather, the other by tunnels and bore shafts -- but both are built '
        'around the extraction of natural compounds that the pharmaceutical industry '
        'cannot synthesise artificially.\n\n'
        'The system\'s warm golden light -- cast by a yellow giant that gives '
        'Kornephoros a different quality from the cluster\'s blue-white and red-'
        'dominated systems -- falls on two worlds that each believe their product is '
        'superior. Tethyn\'s employees use Tethyn\'s compounds and consider Rhizic\'s '
        'products crude. Rhizic\'s employees use Rhizic\'s compounds when they must and '
        'Tethyn\'s when they can afford them, which tells you everything about the '
        'rivalry\'s outcome that the trading floor does not.'
    ),
    cluster=StarClusters.ANTARES,
)

ATR_6619 = System(
    name='ATR-6619',
    star='Red dwarf (M2V), approximately 0.08 times Sol luminosity -- dim and cool, the kind of star that demands significant terraforming investment to make anything habitable',
    population=0,
    distance_to_sol=510.0,
    stellar_objects=[
        StellarObject(
            name='ATR-6619-a',
            short_description='A world whose terraforming was halted when the war with MERIT made the resources unavailable -- atmospheric processors running on maintenance mode, settlements half-built.',
            long_description=(
                'ATR-6619-a was going to be a colony. The Antarian government approved the '
                'development programme in the decades after independence, when the cluster '
                'was expanding and the future felt limitless. The world was marginal -- '
                'cold, dim under the red dwarf\'s feeble light, with a thin atmosphere '
                'heavy in carbon dioxide -- but the terraforming engineers were confident. '
                'The atmospheric processors were deployed. The first settlements were '
                'constructed. The advance population -- engineers, terraformers, '
                'construction crews -- arrived and began the work.\n\n'
                'Then the war intensified. The resources that had been allocated to '
                'colonisation were redirected to the military. The shipments of construction '
                'materials slowed, then stopped. The pharmaceutical supply that the workers '
                'depended on became irregular as the logistics chains prioritised the fleet '
                'and the established systems. The advance population was not evacuated in '
                'one decisive order, the way MERIT evacuated Aldebaran. The Antarian '
                'withdrawal was slower and less organised: the funding dried up, the '
                'supplies stopped arriving, and the workers left in ones and twos as their '
                'contracts expired and were not renewed. The last crew departed when the '
                'stim supply ran out entirely, because a workforce in withdrawal cannot '
                'operate atmospheric processors.\n\n'
                'The terraforming was not complete. The atmospheric processors had been '
                'running for several years -- long enough to shift the composition '
                'measurably, not long enough to make the air breathable. The processors '
                'were placed on maintenance mode by the last departing crew -- a minimal '
                'power setting that keeps the systems from freezing but does not advance '
                'the terraforming. The atmosphere is in limbo: better than it was when the '
                'engineers arrived, worse than it would have been if they had stayed, and '
                'slowly reverting as the maintenance-mode processors cannot sustain the '
                'gains the active programme was making.\n\n'
                'The settlements are half-built. The prefabricated habitats that the first '
                'crews occupied are intact but unpowered. The foundations for buildings '
                'that were never completed are exposed to the thin wind. The construction '
                'equipment was too expensive to retrieve and too heavy to fit on the '
                'departing transports. It sits where the crews left it -- excavators, '
                'graders, and assemblers parked in rows, their operating systems in '
                'standby, waiting for crews that the war has consumed.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-6619-b',
            short_description='A second world that was surveyed as a future expansion target -- the survey data is thorough, the development plan is detailed, and neither will be acted on.',
            long_description=(
                'ATR-6619-b was the development programme\'s second phase -- a warmer world '
                'closer to the star that the planners designated for settlement after '
                'ATR-6619-a\'s terraforming was complete. The surveys were conducted while '
                'the first world\'s processors were running: geological assessments, '
                'atmospheric analysis, climate modelling, the full suite of data that '
                'colonial planners use to design a terraforming programme. The data is '
                'excellent. The development plan derived from it is detailed and costed '
                'and filed in the Antarian colonial archive alongside ATR-6619-a\'s '
                'suspended programme.\n\n'
                'No equipment was deployed to ATR-6619-b. No landing sites were prepared. '
                'The world is untouched -- a rocky planet under a dim red star that was '
                'measured and modelled and planned for by people who are now working in '
                'shipyards on Sargas or serving in the fleet at Antares. The development '
                'plan assumes resources that the war has claimed and a timeline that the '
                'war has invalidated. ATR-6619-b is a future that was cancelled before it '
                'began.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-6619-c',
            short_description='A gas giant that was supposed to fuel the colonisation effort -- the processing infrastructure was planned, budgeted, and never built.',
            long_description=(
                'ATR-6619-c is a mid-sized gas giant in the outer system that the '
                'development programme designated as the colony\'s fuel source. The '
                'processing facilities were designed. The construction was scheduled for '
                'year three of the programme, after ATR-6619-a\'s settlements were '
                'established and the demand for local fuel justified the investment. Year '
                'three came and the budget was gone. The gas giant orbits the dim star '
                'with its atmosphere unprocessed and its moons unbuilt, one more entry in '
                'a development plan that reads like a history of what was intended and a '
                'catalogue of what was not.'
            ),
            population=0,
        ),
    ],
    short_description='A colony that the war interrupted -- half-terraformed, half-built, and waiting for resources that the military has consumed.',
    long_description=(
        'ATR-6619 is what happens when a civilisation at war tries to expand. The '
        'Antarian government approved the colonisation programme in the optimistic '
        'years after independence -- a new system, a new colony, proof that the '
        'cluster was growing and the future was worth fighting for. The terraforming '
        'began. The settlements were constructed. The advance population arrived. The '
        'atmospheric processors started converting the thin, cold air of a world '
        'orbiting a dim red dwarf into something humans could eventually breathe.\n\n'
        'The war consumed the resources. The construction materials were redirected to '
        'Sargas\'s shipyards. The pharmaceutical supply was prioritised for the fleet '
        'and the established systems. The funding dried up in stages rather than all '
        'at once, and the withdrawal was a slow erosion rather than a decisive '
        'evacuation -- workers leaving as contracts expired, supplies thinning until '
        'the stim supply ran out and the last crew departed because a workforce in '
        'withdrawal cannot maintain atmospheric processors.\n\n'
        'The system is empty now. ATR-6619-a\'s processors run on maintenance mode, '
        'sustaining themselves without advancing the terraforming, the atmosphere in '
        'limbo between what it was and what it was supposed to become. The settlements '
        'are half-built. The construction equipment sits in rows where the crews left '
        'it. ATR-6619-b is untouched, its development plan filed and unfunded. The gas '
        'giant\'s fuel processing was never built.\n\n'
        'The Antarian government has not cancelled the programme. Cancellation would '
        'be an admission that the war is consuming the cluster\'s future, and '
        'admissions of that kind are not politically convenient. The programme is '
        'suspended. The suspension is indefinite. The atmospheric processors on '
        'ATR-6619-a run on maintenance mode and the atmosphere slowly reverts and the '
        'construction equipment waits in its rows and the war that was supposed to be '
        'won by now continues, and the colony that was supposed to prove the cluster '
        'was growing is the quiet evidence that the cluster is not.'
    ),
    cluster=StarClusters.ANTARES,
)

ATR_0088 = System(
    name='ATR-0088',
    star='Pulsar -- a rapidly rotating neutron star emitting beams of intense radiation that sweep the system like a lighthouse, making sustained presence in any orbital plane extremely hazardous',
    population=0,
    distance_to_sol=527.8,
    stellar_objects=[
        StellarObject(
            name='ATR-0088-a',
            short_description='A dense remnant world -- scoured by the pulsar\'s radiation beam on every rotation, its surface stripped to bare, magnetised rock.',
            long_description=(
                'ATR-0088-a is a small, dense body in a close orbit -- the remnant of '
                'whatever planetary system existed before the star that became the pulsar '
                'went supernova. The planet survived the explosion, barely. Its atmosphere '
                'was stripped. Its surface was blasted. What remains is bare rock, heavily '
                'magnetised by the pulsar\'s intense magnetic field, and scoured by the '
                'radiation beam on every rotation. The beam sweeps across ATR-0088-a\'s '
                'surface multiple times per second -- a pulse of radiation intense enough '
                'to sterilise any biological material and degrade unshielded electronics '
                'within minutes of exposure.\n\n'
                'The initial survey was conducted entirely by drone, and the drones did '
                'not last long. The radiation degraded their systems faster than the '
                'engineers anticipated, and the data returned was fragmentary -- enough to '
                'confirm the body\'s existence, composition, and orbital parameters, not '
                'enough to conduct a thorough survey. A second drone mission has been '
                'proposed and not funded. The body is scientifically interesting and '
                'practically unreachable.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-0088-b',
            short_description='A frozen outer body -- far enough from the pulsar that the radiation is survivable in hardened equipment, but nobody has stayed long enough to confirm this.',
            long_description=(
                'ATR-0088-b is a frozen body in the outer system -- distant enough from the '
                'pulsar that the radiation flux is reduced to levels that hardened equipment '
                'can theoretically survive for extended periods. The theory has not been '
                'tested. The survey team that discovered the system spent less than a week '
                'in the outer regions before departing, and their report noted that even at '
                'this distance the radiation environment was uncomfortable -- not in the '
                'measurable, instrument-confirmed sense, but in the instinctive, skin-'
                'crawling awareness that the pulsar\'s beam was sweeping through the ship '
                'multiple times per second, passing through the hull and through the crew '
                'with every rotation.\n\n'
                'The body itself is unremarkable -- ice and rock, no atmosphere, no '
                'features that justify the risk of remaining in the system to study it. '
                'ATR-0088-b exists in the survey data as a set of measurements taken '
                'quickly by a crew that wanted to leave.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Beam',
            short_description='The pulsar\'s radiation emission -- sweeping the system multiple times per second, making the entire system a hazard that navigation charts mark in red.',
            long_description=(
                'The Beam is the system\'s defining hazard -- the focused emission of '
                'electromagnetic radiation from the pulsar\'s magnetic poles, sweeping '
                'the system like a lighthouse as the neutron star rotates. The rotation '
                'period is milliseconds. The beam passes through any given point in the '
                'system multiple times per second. The radiation intensity varies with '
                'distance from the pulsar -- lethal in the inner system, hazardous in the '
                'mid-regions, and detectable but survivable in the outer system with '
                'adequate shielding.\n\n'
                'The Beam is what makes ATR-0088 effectively inaccessible. A ship '
                'transiting the system must either stay in the outer regions -- where the '
                'radiation is manageable but there is nothing worth visiting -- or '
                'penetrate deeper with radiation hardening that most vessels do not carry '
                'because most vessels have no reason to enter a pulsar system. The military '
                'has considered the system as a natural fortress -- a location that is '
                'inherently difficult to attack or surveil -- but the same properties that '
                'make it defensible make it impossible to occupy. A garrison in ATR-0088 '
                'would be a garrison being irradiated multiple times per second, and no '
                'hardening eliminates the exposure entirely.\n\n'
                'The navigation charts mark ATR-0088 in red. The system is flagged as a '
                'radiation hazard with a recommendation of avoidance. Ships that transit '
                'through the outer system on their way to other destinations do so quickly, '
                'on trajectories calculated to minimise time in the system. Pilots who have '
                'made the transit describe it as unpleasant -- the knowledge that an '
                'invisible beam of radiation is passing through your body dozens of times '
                'per second, too fast to feel, too constant to ignore once you know it is '
                'happening. The transit is brief. The pilots do not volunteer for a second '
                'one.'
            ),
            population=0,
        ),
    ],
    short_description='A pulsar system -- a rotating neutron star sweeping the system with radiation beams multiple times per second, making it one of the most hazardous locations in the cluster.',
    long_description=(
        'ATR-0088 is a pulsar -- a rapidly rotating neutron star, the collapsed remnant '
        'of a supernova, emitting beams of intense radiation from its magnetic poles '
        'that sweep the system like a lighthouse multiple times per second. The system '
        'was discovered recently and has barely been explored because the pulsar makes '
        'sustained presence extremely hazardous. The initial survey was brief: a crew '
        'that entered the outer system, took measurements as quickly as their '
        'instruments allowed, sent drones toward the inner system that degraded faster '
        'than anticipated, and departed within a week.\n\n'
        'The survey confirmed two bodies: a dense, scoured remnant world in the inner '
        'system that the radiation beam strips on every rotation, and a frozen outer '
        'body that is unremarkable and not worth the risk of studying. The system has '
        'no habitable zone in any meaningful sense -- the pulsar does not provide the '
        'kind of energy that sustains life, and the radiation environment would '
        'sterilise any biology and degrade any unshielded technology.\n\n'
        'ATR-0088 is marked in red on the navigation charts. Ships avoid it. The '
        'military has noted its properties as a natural fortress -- inherently '
        'difficult to attack or surveil -- and filed the observation alongside the '
        'acknowledgement that it is equally impossible to occupy. The system exists as '
        'a hazard marker and a scientific curiosity that nobody has the equipment or '
        'the inclination to investigate further. The pulsar rotates. The beam sweeps. '
        'The system is empty and will remain so because the star that illuminates it '
        'is also the thing that makes it uninhabitable.'
    ),
    cluster=StarClusters.ANTARES,
)

ATR_4401 = System(
    name='ATR-4401',
    star='Orange dwarf (K5V), approximately 0.2 times Sol luminosity -- dim, quiet, and at the end of a hard jump link that discourages casual visitors',
    population=0,
    distance_to_sol=530.0,
    stellar_objects=[
        StellarObject(
            name='ATR-4401-a-i',
            short_description='A small moon orbiting the system\'s gas giant -- home to an automated, heavily armed installation of unknown ownership that fires on anything that approaches.',
            long_description=(
                'ATR-4401-a-i is a small, rocky moon orbiting the system\'s gas giant. The '
                'moon is unremarkable. What is on the moon is not. A facility is built into '
                'the rock -- sensor-shielded, difficult to detect unless you know where to '
                'look, and defended by automated weapons systems that engage any vessel that '
                'approaches within a defined perimeter. The weapons are military-grade. The '
                'targeting is precise. The warnings are not given.\n\n'
                'The facility was discovered by accident -- a survey team that entered the '
                'system through the hard jump link and sent a drone toward the gas giant\'s '
                'moons as part of routine cataloguing. The drone was destroyed. A second '
                'drone, sent at greater distance with passive sensors, detected the '
                'installation before it was also destroyed. The survey team withdrew and '
                'filed a report. The report was noted. No action was taken.\n\n'
                'What is known about the facility comes from the brief sensor data the '
                'drones returned before destruction. The installation is large -- built '
                'into the moon\'s subsurface, with the weapons systems and sensor-shielding '
                'equipment on the surface and the habitable spaces below. The habitable '
                'sections are designed for human occupation -- the thermal signatures '
                'suggest climate-controlled spaces, and the power output is consistent with '
                'a facility that includes life-support, gravity management, and the kind '
                'of energy-intensive environmental systems that are associated with '
                'luxury habitation rather than functional shelter. The facility is '
                'maintained by robots. No human biosignatures have been detected. The '
                'shelter is built, furnished, defended, and empty -- waiting for an '
                'occupant who has not yet arrived or who arrives and departs without '
                'being observed.\n\n'
                'The identity of the owner is unknown. The cost of the installation -- '
                'the military-grade weapons, the sensor shielding, the robotic maintenance '
                'systems, the hard jump link that limits access, the luxury habitation '
                'built into a moon in an uninhabited system -- narrows the list of people '
                'who could afford it to a very short number. The pharmaceutical '
                'corporations of the Antares cluster contain individuals with this kind of '
                'wealth. The installation has the character of a bolt-hole: a place to '
                'disappear to when the political situation changes, when the war turns, '
                'when the corporate rivalries become lethal rather than commercial. Someone '
                'powerful enough to build this is someone powerful enough to need it, and '
                'the need implies a future that the owner is preparing for and the rest of '
                'the cluster is not.\n\n'
                'The few visitors who stumble into ATR-4401 -- pilots who transit the hard '
                'jump link by accident or necessity -- learn about the installation through '
                'the destruction of their drones or the warnings that the weapons systems '
                'deliver through targeting locks. They leave. They do not investigate '
                'further. Whoever built the facility on ATR-4401-a-i has the resources to '
                'build military-grade defences on a moon in a dead-end system, and a person '
                'with those resources is not someone whose secrets are safe to uncover.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-4401-a',
            short_description='A mid-sized gas giant -- unremarkable except for the moon that somebody has turned into a fortress.',
            long_description=(
                'ATR-4401-a is a mid-sized gas giant in the outer system with a handful of '
                'icy moons, one of which hosts the installation that makes the system '
                'notable. The gas giant itself is standard -- hydrogen-helium atmosphere, '
                'no unusual features, fuel processing potential that nobody has developed '
                'because nobody lives here. The gas giant\'s value to the installation\'s '
                'owner is positional: the moon\'s orbit around the gas giant provides an '
                'additional layer of navigational complexity for anyone attempting to '
                'approach, and the gas giant\'s own magnetic field adds interference that '
                'complements the installation\'s sensor shielding.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-4401-b',
            short_description='A rocky inner world -- surveyed in the brief window before the survey team discovered the installation and decided to leave.',
            long_description=(
                'ATR-4401-b is a small, rocky world in the inner system -- catalogued by '
                'the same survey team that discovered the installation on ATR-4401-a-i. The '
                'survey data is minimal: the team completed the inner-system scans before '
                'sending drones to the gas giant\'s moons, and after the second drone was '
                'destroyed they withdrew without completing the survey. ATR-4401-b is '
                'listed in the catalogue with basic orbital and compositional data and a '
                'note that the survey was interrupted. The note does not explain why. The '
                'reason is classified at a level that the survey team did not have and that '
                'the people who do have it have not acted on.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-4401-c',
            short_description='A cold, dry world in the habitable zone -- marginally terraformable, but nobody is terraforming anything in a system with an automated weapons platform.',
            long_description=(
                'ATR-4401-c is a cold, dry world sitting in the outer habitable zone of the '
                'dim orange dwarf. The survey data -- incomplete as it is -- suggests the '
                'planet is marginally terraformable: thin atmosphere, some subsurface water '
                'ice, conditions that centuries of investment could make habitable. The '
                'assessment is academic. Nobody is going to invest centuries of terraforming '
                'in a dead-end system where an automated weapons platform destroys anything '
                'that gets too close to a gas giant moon. The planet sits in the catalogue '
                'as a theoretical possibility that the installation\'s existence has made '
                'practically impossible.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-4401-d',
            short_description='A sparse asteroid belt between the inner worlds and the gas giant -- unremarkable debris that the survey team scanned on their way to the discovery that cut the survey short.',
            long_description=(
                'ATR-4401-d is a sparse asteroid belt occupying the space between the inner '
                'worlds and the gas giant. The belt is thin -- scattered rocky bodies with '
                'no significant mineral concentrations and no features that would warrant '
                'closer investigation even in a system without other complications. The '
                'survey team scanned the belt in transit and recorded standard compositional '
                'data. The belt\'s one point of interest is navigational: a ship approaching '
                'the gas giant from the inner system must transit through the belt, and the '
                'scattered debris provides additional sensor clutter that complements the '
                'installation\'s shielding. Whether this was a factor in the owner\'s choice '
                'of location is unknown. It is convenient.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-4401-e',
            short_description='A frozen outer body beyond the gas giant -- the most distant object in the system, undisturbed and unvisited.',
            long_description=(
                'ATR-4401-e is a frozen body in the far outer system -- ice and rock, no '
                'atmosphere, orbiting beyond the gas giant in the cold outer reaches of a '
                'dim star\'s influence. The survey team catalogued it from long-range scans '
                'without approaching. The body shows no signs of modification, no energy '
                'signatures, and no indication that whoever built the installation on '
                'ATR-4401-a-i has any interest in the outer system. ATR-4401-e is simply '
                'the last thing in a system where the only thing that matters is buried in '
                'a moon closer to the star.'
            ),
            population=0,
        ),
    ],
    short_description='A dead-end system with a secret -- an automated, heavily armed luxury shelter on a moon, owned by someone powerful enough to build it and dangerous enough to discourage questions.',
    long_description=(
        'ATR-4401 is a dead-end system at the terminus of a hard jump link that '
        'discourages casual visitors. The star is a dim orange dwarf. The system '
        'contains a rocky inner world, a gas giant, and a handful of moons. One of '
        'those moons has been converted into something that the system\'s catalogue '
        'designation does not suggest: a heavily armed, sensor-shielded, robotically '
        'maintained luxury shelter built into the subsurface rock and defended by '
        'weapons systems that destroy anything that approaches without warning.\n\n'
        'The installation was discovered by accident and has not been investigated by '
        'design. The facility is expensive -- military-grade defences, sensor '
        'shielding, robotic maintenance, luxury habitation built to a standard that '
        'implies an occupant of extraordinary wealth. The cost narrows the list of '
        'possible owners to a handful of individuals at the top of the Antares '
        'cluster\'s pharmaceutical corporations. The installation has the character of '
        'a bolt-hole: a place prepared for a future that the owner is anticipating and '
        'that the rest of the cluster has not been told about. Someone with the '
        'resources to build a fortress on a moon in a dead-end system is someone who '
        'believes they may need one.\n\n'
        'The system sees almost no traffic. The hard jump link limits access to '
        'skilled pilots in capable ships, and there is nothing in ATR-4401 that would '
        'justify the transit for anyone who does not already know what is here. The '
        'few who stumble in learn quickly -- through destroyed drones or targeting '
        'locks -- that the system is not as empty as the catalogue suggests, and they '
        'leave without investigating further. The identity of the owner is unknown. '
        'The questions that would reveal it are not being asked, because the kind of '
        'person who builds this kind of facility is the kind of person whose enemies '
        'do not do well.'
    ),
    cluster=StarClusters.ANTARES,
)

ATR_8812 = System(
    name='ATR-8812',
    star='Yellow-white main sequence (F5V), approximately 3 times Sol luminosity -- a promising star type for habitable worlds, which is why the survey team was excited when the jump link was discovered',
    population=0,
    distance_to_sol=620.0,
    stellar_objects=[
        StellarObject(
            name='ATR-8812-a',
            short_description='A habitable-zone world currently under active survey -- preliminary data suggests a viable terraforming candidate, but the assessment is years from completion.',
            long_description=(
                'ATR-8812-a is the reason the survey team requested an extended mission. '
                'The planet sits in the habitable zone of a yellow-white star -- the '
                'combination that colonial planners consider most promising -- with '
                'preliminary readings that suggest surface water, a nitrogen-heavy '
                'atmosphere, and conditions that fall within the broad parameters of '
                'terraformable. The data is preliminary. The survey team has been in the '
                'system for less than a decade and the full planetary assessment requires '
                'years of orbital observation, atmospheric sampling, geological survey, and '
                'the patient accumulation of seasonal data that determines whether a world '
                'is genuinely viable or merely promising.\n\n'
                'The team is cautiously optimistic. The atmospheric readings are '
                'encouraging but incomplete -- the composition suggests terraformability but '
                'the seasonal variation has not been fully characterised, and a world that '
                'looks cooperative in one season can reveal complications in another. The '
                'surface water is confirmed from orbit but the hydrological mapping is '
                'ongoing. The geological survey has covered approximately fifteen percent '
                'of the surface through drone overflights and sample returns. The remaining '
                'eighty-five percent is known only from orbital scans, which provide '
                'resolution but not certainty.\n\n'
                'The survey team lives in orbit aboard their ship -- a long-duration survey '
                'vessel with a crew of forty who have spent the better part of a decade in '
                'the system and expect to spend several more. The work is methodical and '
                'slow in the way that planetary science demands: each finding generates '
                'questions that require additional observation, and the observation requires '
                'time. The crew submit interim reports to the Antarian colonial planning '
                'authority. The reports are read with interest. The funding continues. The '
                'war has not yet consumed the budget for exploration, though the crew is '
                'aware that it might.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-8812-b',
            short_description='A hot inner world -- surveyed in the early months, data complete, unremarkable.',
            long_description=(
                'ATR-8812-b is a dense, hot world in a close orbit that the survey team '
                'assessed during the mission\'s first months. The survey is complete: the '
                'world is airless, mineral-bearing but not exceptionally so, and of no '
                'particular interest as a development target. The data sits in the mission '
                'files as a finished section of an unfinished report -- one world fully '
                'characterised while the important one is still being studied.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-8812-c',
            short_description='A cold outer world -- partially surveyed, lower priority than the habitable-zone candidate, the team will get to it when the primary assessment is done.',
            long_description=(
                'ATR-8812-c is a cold, rocky world in the outer system that the survey '
                'team has partially assessed. The initial orbital scans suggest a frozen '
                'surface with subsurface ice deposits and a thin carbon dioxide atmosphere. '
                'The full assessment has been deferred -- the team\'s resources are focused '
                'on ATR-8812-a, and the outer world is lower priority. The preliminary '
                'data is filed with a note that the survey will be completed when the '
                'primary candidate\'s assessment is finished. The note has been in the file '
                'for seven years.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-8812-d',
            short_description='A large gas giant -- surveyed enough to confirm standard composition, with moons the team has not yet had time to catalogue individually.',
            long_description=(
                'ATR-8812-d is a large gas giant in the outer system with an extensive moon '
                'system that the survey team has catalogued in aggregate but not '
                'individually. The gas giant\'s atmospheric composition is confirmed as '
                'standard hydrogen-helium -- suitable for fuel processing if the system is '
                'ever developed. The moons number at least fourteen, identified from '
                'orbital scans but not individually surveyed. The team intends to conduct '
                'individual moon surveys after the primary planetary assessment is '
                'complete. The moons wait.\n\n'
                'The gas giant is the survey team\'s fuel source -- the crew refuel their '
                'ship by skimming ATR-8812-d\'s upper atmosphere, a routine operation that '
                'has become the mission\'s most practised manoeuvre after nearly a decade '
                'of repetition. The crew can execute the skim in their sleep, which some '
                'of the junior crew members claim the pilot has done.'
            ),
            population=0,
        ),
        StellarObject(
            name='ATR-8812-e',
            short_description='A distant frozen body detected on long-range scans -- its existence is confirmed, its properties are estimated, and the team has not visited it.',
            long_description=(
                'ATR-8812-e is a frozen body in the far outer system, detected by the '
                'survey team\'s long-range instruments during the mission\'s second year. '
                'The body\'s existence is confirmed. Its approximate mass, orbit, and '
                'albedo are estimated from the scan data. Its detailed properties are '
                'unknown because the team has not visited it -- the body is far from the '
                'star, far from the habitable-zone candidate that is the mission\'s '
                'priority, and far from anything that would justify the fuel expenditure '
                'of a dedicated survey run. ATR-8812-e is a dot on a chart, confirmed and '
                'unvisited, waiting for a survey team that has more important work to '
                'finish first.'
            ),
            population=0,
        ),
    ],
    short_description='The newest discovery in the Antares cluster -- a system still being surveyed by a crew of forty who have spent a decade studying what might be the cluster\'s next colony.',
    long_description=(
        'ATR-8812 is one of the most recently discovered systems in the galaxy. The '
        'jump link was found approximately a decade ago, and a survey team was '
        'dispatched to assess the system\'s potential. They are still there. The system '
        'contains a yellow-white main sequence star -- the type that colonial planners '
        'consider most promising -- and a habitable-zone world whose preliminary '
        'readings suggest a viable terraforming candidate. The assessment is ongoing.\n\n'
        'A crew of forty lives aboard a long-duration survey vessel in orbit above '
        'ATR-8812-a, the candidate world. They have spent nearly a decade conducting '
        'the patient, methodical work that planetary assessment requires: orbital '
        'observation, atmospheric sampling, geological survey by drone, and the slow '
        'accumulation of seasonal data that determines whether a world\'s promise '
        'survives a full characterisation. The preliminary data is encouraging. The '
        'team is cautiously optimistic. The full assessment will take years more.\n\n'
        'The rest of the system is known in varying degrees of completeness. The inner '
        'world is fully surveyed and unremarkable. The outer world is partially '
        'surveyed and deferred. The gas giant\'s composition is confirmed but its '
        'fourteen moons have not been individually catalogued. A frozen outer body was '
        'detected on long-range scans and has not been visited. The system is a work '
        'in progress -- data accumulating, sections completing at the pace that a '
        'forty-person crew can manage with one ship and one priority.\n\n'
        'ATR-8812 is the Antares cluster\'s future, if the cluster has one. A new '
        'system, a potential colony, proof that expansion is still possible even '
        'during a war. The survey team is aware of what their work represents. They '
        'are also aware that the war consumes the resources that colonisation requires, '
        'and that a promising survey does not guarantee a funded development programme. '
        'They do the work. They submit the reports. They refuel from the gas giant and '
        'continue the observations and wait for the cluster to decide whether the '
        'future is worth investing in.'
    ),
    cluster=StarClusters.ANTARES,
)

ANTARES_SYSTEMS: list[System] = [
    ANTARES, DSCHUBBA, ACRAB, SHAULA, SARGAS, NUNKI,
    KAUS, DIZUO, YED_PRIOR, LESATH, SULAFAT,
    ATR_1156, SADAL, KORNEPHOROS, ATR_6619, ATR_0088,
    ATR_4401, ATR_8812,
]
