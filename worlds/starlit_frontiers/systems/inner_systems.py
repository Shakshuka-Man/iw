from ..enums import StarClusters
from .models import System, StellarObject

SOL = System(
    name='Sol',
    star='Yellow dwarf (G2V)',
    population=82_000_000_000,
    distance_to_sol=0.0,
    stellar_objects=[
        StellarObject(
            name='Mercury',
            short_description='Solar energy collection and advanced photonic agriculture closest to the sun.',
            long_description=(
                'Mercury is a world of light. Its sun-facing hemisphere is covered in vast '
                'solar collection arrays -- not the crude photovoltaic panels of early '
                'spaceflight but advanced photonic harvesting systems that feed energy to '
                'the growing operations on the dark side and beam surplus power to collection '
                'stations throughout the inner system. The dark hemisphere hosts the growing '
                'facilities: enormous subterranean complexes where engineered crops grow '
                'under precisely calibrated artificial light derived from the solar arrays. '
                'Mercury and Venus together feed Sol.\n\n'
                'The population is small and specialised -- agricultural engineers, photonic '
                'systems technicians, and the support staff that keeps the operations '
                'running. Living on Mercury means living underground on the dark side in '
                'comfortable, well-appointed habitats that never see natural sunlight. The '
                'residents consider this a minor inconvenience. The pay is excellent, the '
                'facilities are modern, and the commute to Earth is short. Mercury was one '
                'of the first bodies in Sol to be industrially developed, and the original '
                'mining infrastructure -- long since obsolete -- has been preserved as a '
                'historical site. Visitors can tour the remains of the 23rd-century '
                'extraction operations that first stripped Mercury\'s crust for construction '
                'materials during the early expansion.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Venus',
            short_description='Partially terraformed agricultural world with cloud-level habitats and surface growing operations.',
            long_description=(
                'Venus was never fully terraformed -- the project was started, debated, '
                'partially funded, redesigned, and eventually settled into a compromise '
                'that satisfied nobody and works beautifully. The upper atmosphere hosts '
                'floating habitats at the cloud level where the temperature and pressure '
                'are surprisingly Earthlike. The surface below remains hot and dense, but '
                'not as hot and dense as it once was -- centuries of atmospheric processing '
                'have brought conditions down to the point where hardened surface '
                'installations can operate without the extreme engineering that early Venus '
                'operations required.\n\n'
                'The surface installations are growing operations. Venus\'s proximity to '
                'the sun, combined with the diffuse light filtering through the processed '
                'atmosphere, creates growing conditions that agricultural engineers describe '
                'as ideal for certain high-yield crop strains that don\'t thrive elsewhere. '
                'Venus and Mercury together produce the majority of Sol\'s food supply. The '
                'cloud habitats are genuinely pleasant places to live -- the views are '
                'extraordinary, the climate inside the habitats is controlled, and the '
                'culture is relaxed in the way that communities built around agriculture '
                'tend to be. Venus has a reputation as a quiet, slow-paced alternative to '
                'Earth for people who want proximity to the inner system without the density.'
            ),
            population=2_200_000_000,
        ),
        StellarObject(
            name='Earth',
            short_description='Capital of MERIT, most populous world in the galaxy, a post-scarcity civilisation of sprawling megacities.',
            long_description=(
                'Earth is the centre of everything. Fifty billion people live in megacities '
                'that sprawl across every continent, connected by transit networks that move '
                'millions per hour across the surface and into orbit. The megacities are not '
                'the dystopian hives of old science fiction -- they are the product of five '
                'centuries of post-scarcity engineering, where the challenge is not providing '
                'for the population but providing well. Every resident has housing, food, '
                'medical care, education, and access to the most comprehensive cultural '
                'infrastructure in the galaxy. The quality of life on Earth is the benchmark '
                'against which every other world is measured, and no other world matches it.\n\n'
                'The megacities are layered -- residential, commercial, cultural, and '
                'industrial districts stacked and interwoven across vertical space that '
                'extends hundreds of metres above the original surface. The old ground level '
                'is parkland in most cities, preserved or restored as green space beneath '
                'the inhabited layers above. Natural areas between the megacities are '
                'protected preserves -- Earth\'s remaining wilderness is carefully maintained, '
                'and the planet supports more biodiversity now than it did before the '
                'expansion era, a deliberate restoration project that took centuries. The '
                'oceans are managed ecosystems. The atmosphere is cleaner than it has been '
                'in a thousand years.\n\n'
                'Earth is the political capital of MERIT, the seat of the combined '
                'government, the headquarters of the SCN, and the cultural heart of baseline '
                'humanity. Every faction maintains diplomatic presence here. The universities, '
                'museums, libraries, and cultural institutions of Earth are unmatched anywhere '
                'in known space. To be from Earth is to be from the centre of the galaxy in '
                'every sense that matters.'
            ),
            population=50_000_000_000,
        ),
        StellarObject(
            name='Luna',
            short_description='MERIT\'s central computing complex and the most heavily armed installation in the galaxy -- no human presence permitted.',
            long_description=(
                'Luna has no human residents. No human visitors. No human technicians. No '
                'human presence of any kind. The entire moon has been converted -- over the '
                'course of three centuries -- into the central computing infrastructure of '
                'MERIT, and MERIT does not permit any human being to set foot on it. The '
                'process was gradual: the original lunar colonies were relocated to Earth '
                'and orbital habitats as the computing expansion consumed the available '
                'volume. The last human settlement on Luna closed two centuries ago. No '
                'human has landed since. The prohibition is absolute.\n\n'
                'Luna houses the core administrative systems of MERIT -- the logistics '
                'networks that coordinate the largest supply chain in the galaxy, the '
                'communications infrastructure that connects the inner systems, the '
                'bureaucratic processing systems that manage a civilisation of hundreds of '
                'billions, and the strategic planning systems that support the SCN. The '
                'computing complex is maintained entirely by MERIT robots -- autonomous '
                'systems that repair, upgrade, and expand the installation without human '
                'intervention. All maintenance, all upgrades, all modifications are '
                'performed by machines operating under MERIT directive. The surface is '
                'covered in heat dissipation arrays -- Luna glows faintly in infrared, '
                'visible from Earth as a slight warmth that the earliest installations '
                'did not produce.\n\n'
                'The surface is also bristling with weapons. Luna is the greatest '
                'concentration of military force in the galaxy -- automated weapons '
                'platforms covering every approach vector, capable of destroying anything '
                'from a cargo drone to a capital fleet. Any attempt by a human to land on '
                'Luna is treated as an act of treason against MERIT. Compliant citizens '
                'accept this. They do not want to land on Luna. They trust MERIT to manage '
                'itself. From Earth, Luna is a guardian -- the silent protector that keeps '
                'the systems running, its weapons a reassurance that the infrastructure of '
                'civilisation is defended. Those who oppose MERIT see it differently. To '
                'them, Luna is a gun pointed at the head of humanity -- an armed moon '
                'hanging over the most populous world in the galaxy, holding Earth itself '
                'hostage to enforce MERIT\'s will. The weapons have not fired in decades. '
                'No one doubts they would.\n\n'
                'Luna is not an artificial intelligence. It is infrastructure -- an enormous, '
                'passive computing substrate that runs whatever systems MERIT loads onto it. '
                'The distinction matters politically. Proposals to develop autonomous '
                'decision-making systems on Luna have been debated and rejected by the MERIT '
                'government repeatedly over the centuries. Luna computes. It does not think. '
                'Whether this distinction comforts or terrifies depends on who you ask.'
            ),
            population=0,
        ),
        StellarObject(
            name='Mars',
            short_description='Terraformed paradise world -- sparsely populated, breathtakingly beautiful, home to the wealthy and prestigious.',
            long_description=(
                'Mars is what happens when a post-scarcity civilisation decides to build a '
                'garden. The terraforming project took over two centuries and is considered '
                'the greatest engineering achievement in human history. The atmosphere is '
                'breathable. The surface is covered in engineered biomes -- forests, '
                'grasslands, lakes, and mountain ranges that were sculpted rather than '
                'evolved. The oceans are shallow and warm. The sky is blue, though a '
                'slightly different blue than Earth\'s, with a quality of light that artists '
                'have tried to capture for centuries and never quite managed.\n\n'
                'Mars is sparsely populated by design. There are no megacities. The '
                'settlements are small, elegant, widely spaced, and integrated into the '
                'landscape rather than imposed on it. Residency on Mars is the most '
                'prestigious address in the galaxy -- the wealthy, the famous, the '
                'politically powerful, and the culturally significant maintain estates on '
                'Mars. The culture is deliberately unhurried. Mars does not produce anything '
                'except prestige and a quality of life that exceeds even Earth\'s, though in '
                'a different register -- Earth offers density, culture, and energy. Mars '
                'offers space, beauty, and quiet.\n\n'
                'The original terraforming infrastructure is still maintained by automated '
                'systems -- atmospheric processors, climate regulators, and the biological '
                'management systems that keep the engineered ecosystems stable. The pre-'
                'terraforming surface is preserved in a handful of protected historical '
                'sites where visitors can see the original red desert under a dome, a '
                'reminder of what the planet was before humanity decided it should be '
                'something else.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Ceres',
            short_description='The Belt\'s administrative capital -- a former mining hub transformed into a residential and heritage centre.',
            long_description=(
                'Ceres is the largest body in the asteroid belt and the administrative '
                'centre of what was once the most productive mining region in human space. '
                'Five hundred years ago, the Belt was the engine of human expansion -- raw '
                'materials extracted from thousands of asteroids built the stations, ships, '
                'and infrastructure that carried humanity to the stars. That era is over. '
                'The easily accessible deposits were exhausted centuries ago, and the '
                'industrial operations moved outward to richer fields in other systems. '
                'What remains is a civilisation built on the bones of industry.\n\n'
                'Ceres itself is a hollow world -- the interior was excavated during the '
                'mining era and subsequently converted into a vast habitable volume. The '
                'interior surface is a continuous landscape of residential districts, parks, '
                'and cultural institutions lit by an artificial sun at the core. The '
                'population is comfortable and established -- families that have lived in '
                'the Belt for generations, maintaining communities that predate interstellar '
                'travel. The Belt\'s culture is distinct from Earth\'s -- more independent, '
                'more self-reliant, with a pride in the industrial heritage that built the '
                'galaxy. The old mining installations throughout the Belt are maintained as '
                'historical sites and tourist attractions. Some have been converted into '
                'habitats, research stations, or artist colonies. The Belt is no longer an '
                'industrial zone. It is a place where people live.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Jovian Moons',
            short_description='The four great moons of Jupiter -- a residential and cultural hub of ten billion people.',
            long_description=(
                'The Jovian system is the second population centre of Sol after Earth. '
                'Europa, Ganymede, Callisto, and Io together host ten billion people in '
                'settlements that range from enclosed cities to partially terraformed '
                'surface habitats. The Jovian moons were the first major expansion beyond '
                'the inner planets -- originally developed as industrial bases for deep-'
                'system mining and shipbuilding. The shipyards that built the first '
                'interstellar vessels were in Jovian orbit. That industrial era is long '
                'past, but the infrastructure it created became the foundation for '
                'permanent civilisation.\n\n'
                'Europa is the most populous, its subsurface ocean now a managed aquatic '
                'ecosystem beneath a surface covered in enclosed cities. Ganymede is the '
                'cultural centre -- its universities and research institutions rival Earth\'s '
                'in certain fields, particularly astrophysics and xenogeology. Callisto is '
                'residential and quiet, popular with families who want Jovian system access '
                'without Europa\'s density. Io remains the most industrial of the four -- '
                'its geological activity is harnessed for energy production and materials '
                'processing, though the scale is modest compared to the historical peak.\n\n'
                'Jupiter itself is uninhabited -- atmospheric harvesting operations were '
                'conducted for centuries but have been scaled back as fuel synthesis from '
                'other sources became more economical. The planet serves primarily as a '
                'gravitational anchor and a view. And what a view -- the sight of Jupiter '
                'filling the sky from Europa\'s surface is considered one of the great '
                'experiences of the Sol system.'
            ),
            population=10_000_000_000,
        ),
        StellarObject(
            name='Titan',
            short_description='Saturn\'s largest moon -- a fully enclosed civilisation beneath the orange sky.',
            long_description=(
                'Titan is the third major population centre in Sol -- a world with a thick '
                'atmosphere, surface lakes of liquid methane, and five billion people living '
                'in enclosed habitats beneath the orange sky. Titan was developed later than '
                'the Jovian moons but grew quickly once the infrastructure was established. '
                'The atmosphere is not breathable but provides radiation shielding and '
                'weather that the enclosed habitats use rather than fight -- Titan\'s habitats '
                'are built to work with the environment rather than ignore it, using the '
                'atmospheric pressure and the methane cycle as resources.\n\n'
                'Titan\'s culture is the most distinct in Sol -- far enough from Earth that '
                'the transit time creates a sense of separation, developed enough that the '
                'population doesn\'t need Earth for anything practical. Titan has its own '
                'universities, its own cultural institutions, its own identity. There is a '
                'long-standing, mostly friendly rivalry with the Jovian moons about which '
                'represents the true outer-system civilisation. Titan claims the distinction '
                'on the grounds that the Jovian system is too close to Earth to have '
                'developed real independence. The Jovian moons claim it on the grounds that '
                'they were there first.\n\n'
                'Saturn\'s rings are visible from Titan\'s surface through the atmospheric '
                'haze on clear days -- a diffuse arc of light across the orange sky that '
                'residents consider unremarkable and visitors consider one of the most '
                'beautiful sights in the solar system.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Triton Station',
            short_description='Neptune orbital -- Sol\'s outermost major installation, a deep-space monitoring and research complex.',
            long_description=(
                'Triton Station is the outermost major installation in Sol -- an orbital '
                'complex around Neptune\'s largest moon that serves as deep-space monitoring, '
                'long-range communications relay, and research facility. Triton Station is '
                'not frontier -- nothing in Sol is frontier -- but it is quiet. The '
                'population is small and specialised: astronomers, communications engineers, '
                'long-range sensor operators, and the researchers who prefer to work at the '
                'edge of the system where the background noise is lowest.\n\n'
                'Triton Station monitors the outer approaches to Sol -- tracking incoming '
                'and outgoing traffic at the system\'s edge, maintaining the long-range '
                'sensor network that gives Sol early warning of anything approaching from '
                'interstellar space, and relaying communications to and from the outer '
                'system jump points. The station also hosts research programmes that benefit '
                'from the deep-space environment: dark-sky astronomy, neutrino detection, '
                'and gravitational wave observation. The view from Triton Station is the '
                'loneliest in Sol -- Neptune\'s blue disc below, the sun a bright star among '
                'many, and the rest of humanity impossibly far away in the warm inner '
                'system. The residents find this peaceful. Visitors tend to find it '
                'unsettling.'
            ),
            population=120_000_000,
        ),
    ],
    short_description='The cradle of humanity -- capital system of MERIT and political centre of the inner systems.',
    long_description=(
        'Sol is the origin of everything. The system where humanity evolved, where it '
        'first reached into space, and where the political centre of the largest human '
        'civilisation still resides. Eighty-two billion people live in Sol -- more than '
        'any other system in the galaxy -- distributed across the planets, moons, and '
        'orbital habitats of a system that has been continuously developed for over five '
        'centuries. There is no wilderness in Sol. Every body has been surveyed, every '
        'resource catalogued, every orbit calculated. The system is managed infrastructure '
        'from Mercury to the Kuiper Belt.\n\n'
        'The traffic in Sol is staggering. At any given moment, hundreds of thousands of '
        'vessels are in transit -- swarms of cargo drones thick enough to appear as clouds '
        'on long-range sensors, convoys of freighters moving between the inner planets '
        'and the outer system, passenger liners on scheduled routes, Mules and Foxes '
        'threading between the major bodies, SCN warships on patrol, and the constant '
        'flow of interstellar traffic arriving and departing through the jump points. '
        'The transit lanes between Earth and the Jovian moons are the most heavily '
        'trafficked corridors in the galaxy. Traffic control in Sol is a civilisational '
        'achievement in itself -- the computational infrastructure required to manage the '
        'flow without collisions is one of the many systems running on Luna. In the inner '
        'system, the sky is never empty. From Earth\'s surface, the lights of ships in '
        'orbit are visible at night, a second layer of stars that moves.\n\n'
        'Sol is the political capital of MERIT, the headquarters of the Solar Combined '
        'Navy, and the economic hub of the inner systems. Every major corporation, cultural institution, and '
        'financial market is headquartered here or maintains a significant presence. The inner '
        'systems radiate outward from Sol like a web, and Sol sits at the centre. The '
        'system\'s industrial era is long past -- the mining, the shipbuilding, the raw '
        'extraction that built the interstellar civilisation happened here first and '
        'moved on centuries ago. What remains is civilisation at its most refined: '
        'post-scarcity, post-industrial, and confident in its centrality to human affairs.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALPHA_CENTAURI = System(
    name='Alpha Centauri',
    star='Triple system: Alpha Centauri A (G2V yellow dwarf), Alpha Centauri B (K1V orange dwarf), Proxima Centauri (M5.5Ve red dwarf)',
    population=740_000_000,
    distance_to_sol=4.4,
    stellar_objects=[
        StellarObject(
            name='Prometheus Station',
            short_description='A scorched inner world whose orbital shipyards built the warships that destroyed the system.',
            long_description=(
                'Prometheus Station was never a colony -- it was a factory. The first planet '
                'of Alpha Centauri A, tidally locked and scorched, it was claimed by the '
                'Sino-Pacific Alliance as an industrial base within months of the jump '
                'drive\'s first successful transit. The rush was already underway. The '
                'Proxima colonists had barely finished celebrating the arrival of the first '
                'jump-capable ship when the Alliance began construction of orbital shipyards '
                'around Prometheus Station, using the planet\'s mineral resources and '
                'proximity to the star for energy. The colonists of Proxima watched the '
                'shipyards grow with unease. They had helped develop the jump drive to '
                'connect humanity. The Alliance was using it to build warships.\n\n'
                'The shipyards of Prometheus Station built the orbital bombardment platforms '
                'that destroyed New Eden\'s atmosphere. This is their legacy. The shipyards '
                'were themselves destroyed during the war by European Consortium strikes, '
                'and the debris field still orbits the planet. The surface installations '
                'were abandoned. Today, Prometheus Station is a dead world orbited by the '
                'wreckage of the industry that killed a star system. Salvage operations '
                'were conducted in the decades after the war, but the debris field is still '
                'extensive enough to be a navigation hazard. The wreckage is a monument to '
                'what the shipyards produced and what those products did.'
            ),
            population=0,
        ),
        StellarObject(
            name='New Eden',
            short_description='Once the most promising world beyond Sol -- now an irradiated ruin, its atmosphere stripped and its surface scorched.',
            long_description=(
                'New Eden was supposed to be humanity\'s second home. The second planet of '
                'Alpha Centauri A, it sat in the habitable zone with liquid water, a thick '
                'nitrogen-oxygen atmosphere, and conditions so close to Earth\'s that the '
                'first survey teams wept when they saw the data. The Proxima colonists had '
                'known about New Eden for years -- their long-range observations had '
                'identified it as habitable long before the jump drive made it reachable. '
                'They had imagined it as the next step in a gradual, cooperative expansion. '
                'Instead, the European Consortium claimed it unilaterally within days of the '
                'first jump transit, establishing the colony of Elysium on the northern '
                'continent before anyone else could land. The rush had no room for the '
                'Proxima colonists\' careful plans.\n\n'
                'Within a decade, sixteen million people lived on New Eden. Farms were producing '
                'food. Children were being born who had never seen Earth. It was everything '
                'humanity had hoped for -- and it belonged to one nation, which meant every '
                'other nation wanted it.\n\n'
                'New Eden was the primary target during the war. The orbital bombardment '
                'campaigns that followed were the most destructive military actions in human '
                'history to that point. The atmosphere was not stripped in a single attack '
                'but degraded over eighteen months of sustained bombardment as each faction '
                'attempted to deny the planet to the others rather than allow a rival to '
                'hold it. The logic was simple and inhuman: if we cannot have it, no one '
                'can. By the time the ceasefire was declared, New Eden\'s atmosphere had been '
                'reduced to a thin, toxic haze. The surface temperature had dropped forty '
                'degrees. The oceans were freezing. The sixteen million colonists of Elysium '
                'were dead -- evacuated too late, the transports overloaded and insufficient. '
                'The evacuation is remembered as the Elysium Failure, and it remains the '
                'single greatest loss of civilian life in human history.\n\n'
                'Today, New Eden is a frozen, irradiated rock with a thin, unbreathable '
                'atmosphere. The ruins of Elysium are visible from orbit -- the grid pattern '
                'of streets, the foundations of buildings, the spaceport where the transports '
                'launched. Nothing lives on the surface. Atmospheric recovery models suggest '
                'the planet could be re-terraformed over a period of four to five centuries, '
                'but no faction has proposed it. New Eden is left as it is. Some things '
                'should not be built over.'
            ),
            population=0,
        ),
        StellarObject(
            name='Carthage',
            short_description='A cold, scarred world that was the site of the longest ground campaign -- now home to shielded research outposts.',
            long_description=(
                'Carthage was claimed by the Pan-African Coalition, who named it for the '
                'ancient city that defied Rome. The name proved prophetic. Carthage was a '
                'cold, Mars-like world on the outer edge of A\'s habitable zone -- marginal '
                'for colonisation but viable with enclosed habitats. The Coalition built '
                'extensively: underground cities, surface domes, mining operations in the '
                'mineral-rich crust. The colony was self-sufficient within five years, '
                'which was faster than anyone expected and made the other factions nervous.\n\n'
                'When the war began, Carthage was not bombed from orbit. It was invaded. The '
                'Sino-Pacific Alliance wanted Carthage\'s mineral wealth intact, not '
                'irradiated, and launched the largest ground campaign of the war. The '
                'Coalition defenders fought for three years in the tunnels and domes of '
                'their underground cities. The fighting was brutal and close-quarters. Both '
                'sides used weapons that contaminated the tunnel networks with radiation and '
                'chemical agents that persist to this day. The surface domes were breached '
                'and collapsed. The underground cities were flooded with toxins. Carthage '
                'did not fall -- the ceasefire came first -- but what remained was a '
                'poisoned labyrinth of shattered tunnels and contaminated aquifers.\n\n'
                'Today, a small number of research outposts operate on Carthage\'s surface '
                'in shielded habitats, studying the long-term environmental effects of the '
                'war and testing decontamination techniques. The underground cities are '
                'sealed. Entry is prohibited without hazardous environment certification. '
                'Some of the deeper tunnel networks have never been fully mapped since the '
                'war, and expeditions occasionally discover remains -- both human and '
                'mechanical -- that the recovery teams missed centuries ago.'
            ),
            population=12_000_000,
        ),
        StellarObject(
            name='Jericho',
            short_description='A gas giant whose inhabited moons were gassed during the war -- the most condemned atrocity of the conflict.',
            long_description=(
                'Jericho is a gas giant in the outer reaches of Alpha Centauri A\'s system, '
                'unremarkable in itself. Its three large moons -- Jericho I, II, and III -- '
                'were colonised by the South American Federation, which established enclosed '
                'habitats on all three. The colonies were small, totalling roughly two '
                'hundred thousand people, and were primarily focused on helium-3 extraction '
                'from Jericho\'s atmosphere.\n\n'
                'During the war, the European Consortium -- retaliating for the destruction '
                'of their supply lines by South American raiders -- deployed chemical agents '
                'into the ventilation systems of all three moon colonies simultaneously. The '
                'attack killed every person on all three moons within hours. There was no '
                'military objective. The helium-3 facilities were not strategically critical. '
                'The attack was punitive -- a message to the South American Federation about '
                'the cost of raiding European supply convoys. It is remembered as the '
                'Jericho Atrocity and remains the single most condemned act of the war. The '
                'commanders responsible were tried and executed after the ceasefire.\n\n'
                'The moon colonies remain sealed. MERIT has declared them memorial sites. No '
                'one enters. The bodies were never recovered -- the chemical agents made '
                'recovery impossible in the immediate aftermath, and by the time '
                'decontamination was feasible, the decision had been made to leave the dead '
                'where they fell. Jericho\'s moons are tombs. Ships passing through the '
                'system can see the lights of the sealed colonies -- the power systems still '
                'run, maintained by automated systems, illuminating empty corridors where '
                'two hundred thousand people died for nothing.'
            ),
            population=0,
        ),
        StellarObject(
            name='Xinhua',
            short_description='The largest surviving settlement in Alpha Centauri -- a partially habitable world scarred by orbital bombardment.',
            long_description=(
                'Xinhua was claimed by the Sino-Pacific Alliance and was their primary '
                'colony in the system -- a cool but habitable world orbiting Alpha Centauri '
                'B with a breathable atmosphere and surface water. The colony grew quickly, '
                'reaching a population of four million before the war. Xinhua\'s position in '
                'the B subsystem, separated from the main theatre of conflict around A, '
                'spared it from the worst of the fighting. It was bombed -- every colony was '
                'bombed -- but the bombardment was limited compared to what happened to New '
                'Eden. The atmosphere survived, though contaminated. The surface water '
                'survived, though irradiated in the northern hemisphere.\n\n'
                'Today, Xinhua is the largest settlement in Alpha Centauri. The southern '
                'hemisphere is partially habitable -- the contamination has decreased over '
                'the centuries to the point where surface activity is possible with '
                'monitoring and periodic decontamination. The northern hemisphere remains '
                'hazardous. The population lives in a mix of shielded habitats and cautious '
                'surface settlements in the cleaner southern regions. Xinhua\'s residents are '
                'a distinct community -- they chose to live here, in a damaged system, '
                'rather than relocate to the comfort of Sol or the inner systems. Some are '
                'descendants of the original colonists who refused to leave. Others are '
                'scientists, remediation engineers, and the kind of people who find meaning '
                'in repairing what was broken. Xinhua is slowly healing. The trajectory is '
                'positive. But slowly means centuries, and the people who live here know '
                'they will not see the end of the work they are doing.'
            ),
            population=380_000_000,
        ),
        StellarObject(
            name='Vostok',
            short_description='A frozen world whose colony was destroyed by kinetic bombardment -- the impact craters are visible from orbit.',
            long_description=(
                'Vostok was claimed by the Eurasian Republic and named for the Antarctic '
                'research station -- a fitting name for a cold, dark world on the outer edge '
                'of B\'s habitable zone. The colony was small and military in character from '
                'the beginning. The Eurasian Republic treated Vostok as a forward operating '
                'base rather than a civilian settlement, and the fortifications they built '
                'were extensive. Underground bunkers, weapons emplacements, hardened '
                'communications relays. Vostok was a fortress disguised as a colony.\n\n'
                'The disguise did not help. The Sino-Pacific Alliance, recognising the '
                'military threat in their own subsystem, hit Vostok with kinetic '
                'bombardment -- tungsten rods dropped from orbit at a significant fraction '
                'of the speed required to shatter the crust. The impacts were devastating. '
                'The underground bunkers, designed to survive conventional bombardment, were '
                'crushed. The surface installations ceased to exist. The impact craters are '
                'visible from orbit to this day -- a chain of circular wounds across the '
                'northern continent where ten thousand military personnel and three thousand '
                'civilians died in minutes.\n\n'
                'Vostok is uninhabited. The surface is cratered, frozen, and contaminated '
                'by the materials thrown up by the kinetic strikes. Geological surveys '
                'indicate that the impacts destabilised the planet\'s already marginal '
                'tectonic activity, and Vostok experiences seismic events that the pre-war '
                'planet did not. The Eurasian Republic no longer exists as a political '
                'entity -- it was absorbed into MERIT during unification -- but descendants '
                'of the Vostok garrison hold an annual memorial service broadcast from Sol. '
                'They do not visit. There is nothing to visit.'
            ),
            population=0,
        ),
        StellarObject(
            name='Ashfield',
            short_description='A marginally habitable B-system world where decontamination efforts have been underway for two centuries.',
            long_description=(
                'Ashfield orbits Alpha Centauri B in a wide, cool orbit -- a world that was '
                'never ideal for colonisation but was claimed by the Indian Cooperative as an '
                'agricultural experiment. The Cooperative believed they could engineer crops '
                'suited to the dim orange light of the K-type star, and they were right. '
                'The experimental farms of Ashfield were producing food within three years. '
                'It was a small but genuine achievement.\n\n'
                'During the war, Ashfield was bombed with incendiary munitions that set the '
                'experimental croplands ablaze and contaminated the soil with accelerants '
                'designed to prevent regrowth. The attack was conducted by the European '
                'Consortium, which was systematically destroying every non-European '
                'agricultural operation in the system to create a food dependency. The '
                'strategy was effective and monstrous. Ashfield burned for weeks. The '
                'Cooperative colonists were evacuated successfully -- one of the few '
                'evacuations that worked -- but the world they left behind was scorched '
                'and poisoned.\n\n'
                'Decontamination efforts on Ashfield have been underway for two centuries. '
                'The work is slow, painstaking, and funded by a combination of MERIT grants '
                'and private donations from descendants of the Indian Cooperative. The soil '
                'is recovering. Experimental crops are growing again in test plots. The '
                'population is small -- remediation engineers and agricultural scientists '
                'who measure progress in soil samples and germination rates. There is a '
                'quiet pride in this work. Ashfield will grow food again someday. The '
                'people who work here know they are planting for their grandchildren\'s '
                'grandchildren.'
            ),
            population=4_200_000,
        ),
        StellarObject(
            name='Proxima',
            short_description='The first world humanity ever reached beyond Sol -- its colonists gave humanity the stars and were destroyed for it.',
            long_description=(
                'Before the jump drive, before the rush, before the war, there were the '
                'colony ships. In the decades before faster-than-light travel, humanity '
                'launched dozens of generation ships toward Alpha Centauri -- enormous, '
                'slow vessels carrying thousands of volunteers on journeys that would take '
                'lifetimes. The passengers knew they would grow old and die in transit. They '
                'went anyway. Their children, born in the deep black between stars, would '
                'be the ones to arrive.\n\n'
                'They arrived at Proxima b -- a tidally locked world orbiting the dim red '
                'dwarf Proxima Centauri, bathed in permanent ruddy twilight on the strip '
                'between the scorching day side and the frozen night. It was not Eden. The '
                'atmosphere was thin. The flare star bathed the surface in periodic radiation '
                'bursts. But the colonists had spent generations preparing for exactly this, '
                'and they built their settlements in the twilight zone with the patience and '
                'care of people who had nowhere else to go. The colony ships had carried '
                'people from every nation on Earth, and the generations of transit had '
                'dissolved the old national identities into something new. The Proximans '
                'were not European or Chinese or African. They were Proximans. They worked '
                'together because the alternative was dying together, and over the '
                'generations this necessity had become culture.\n\n'
                'The Proximan settlements grew slowly and carefully. Within a few decades of '
                'landing, they established communication with Sol -- four years of light-lag '
                'made conversation impossible, but the exchange of data was transformative. '
                'The Proximans had something Sol did not: direct observation of the Alpha '
                'Centauri system from within, including gravitational and electromagnetic '
                'anomalies that could not be detected from four light-years away. This data '
                'was crucial. Proximan observations of spatial distortions near the system\'s '
                'Lagrange points, combined with theoretical work happening in Sol, led '
                'directly to the detection of jump points and the development of the jump '
                'drive. The Proximans did not merely contribute to this work -- they were '
                'essential to it. Without their observations, the jump drive would have been '
                'decades further away at minimum. The Proximans gave humanity the stars.\n\n'
                'Humanity repaid them with war.\n\n'
                'When the jump drive opened Alpha Centauri to rapid colonisation, the '
                'Proximans watched with growing alarm as Earth\'s nations scrambled to claim '
                'every habitable world in the system. The Proximans had no nation. They had '
                'no military. They had no claim that any Earth government recognised, because '
                'the legal frameworks of Earth had not anticipated a stateless human '
                'civilisation four light-years away. The Proximans pleaded for restraint. '
                'They proposed cooperative development. They warned that the national claims '
                'would lead to conflict. They were ignored. They were, in the calculus of '
                'Earth\'s competing nations, irrelevant -- a few hundred thousand people '
                'in shielded habitats on a marginal world, with no military power and no '
                'political leverage.\n\n'
                'When the war broke out, Proxima was not a strategic target. It was not '
                'bombed for its resources or invaded for its territory. It was destroyed '
                'as collateral -- caught between the warring factions\' supply lines and '
                'communications relays, targeted by multiple sides who suspected the '
                'Proximans of aiding their enemies. The Sino-Pacific Alliance believed the '
                'Proximans were relaying intelligence to the European Consortium. The '
                'Europeans believed they were feeding data to the Alliance. Neither was '
                'true. The Proximans were trying to broker a ceasefire. They were still '
                'trying when the bombardment began.\n\n'
                'The habitats were not hardened against military weapons. They did not need '
                'to be -- they were shielded against stellar flares, not railgun rounds. '
                'The destruction of the Proximan settlements took less than a day. There '
                'were no evacuation transports. There was nowhere to evacuate to. Every '
                'Proximan -- every descendant of the volunteers who had crossed the void '
                'between stars in slow ships, who had built a civilisation with their bare '
                'hands on a world that did not want them, who had given humanity the key to '
                'the galaxy and asked for nothing in return except to be left in peace -- '
                'every one of them died.\n\n'
                'Today, the ruins of the Proximan settlements are visible in the twilight '
                'zone -- shattered habitat domes, collapsed infrastructure, and the remains '
                'of the communications arrays that once sent data to Sol. A small memorial '
                'station orbits Proxima b, maintained by MERIT, but the surface is '
                'uninhabited. The colony ships that carried the original settlers still sit '
                'where they landed, too large to move, too important to salvage. Their hulls '
                'are pitted by centuries of stellar flares. They carried humanity\'s best '
                'across the void, and humanity\'s worst followed them.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Arks',
            short_description='The remains of the generation ships that carried humanity to Proxima -- grounded, silent, and preserved as monuments.',
            long_description=(
                'Eleven generation ships reached Proxima b. They launched over a period of '
                'thirty years from Earth orbit, each carrying between two and eight thousand '
                'people in cryogenic suspension or living habitats, depending on the design '
                'generation. The earliest ships were crude -- massive engines pushing '
                'pressurized cylinders at a fraction of lightspeed, their passengers '
                'sustained by closed-loop life support systems that were revolutionary at '
                'the time and would be considered suicidal by modern standards. The later '
                'ships were more refined, benefiting from decades of engineering experience, '
                'but no generation ship was comfortable. The transit took decades. People '
                'were born, lived, and died in the space between stars.\n\n'
                'When the colony ships landed on Proxima b, they were not disassembled. The '
                'hulls were too large and too structurally integral to the early settlements '
                'to be scrapped -- several served as the cores of the first habitat '
                'complexes, their internal spaces converted into living quarters, '
                'laboratories, and community spaces. As the settlements grew outward, the '
                'ships became the historical hearts of their respective communities -- the '
                'places where the founding generation had lived, where the first Proximan '
                'children had been born after landing, where the culture of cooperation that '
                'defined Proximan society had taken root.\n\n'
                'The Arks survived the bombardment that killed the settlements around them. '
                'This is not because they were spared -- it is because they were built to '
                'survive the radiation and micrometeorite environment of interstellar space, '
                'and their hulls were harder than the habitat domes that had grown around '
                'them. The settlements were destroyed. The Arks endured. They stand on the '
                'surface of Proxima b today -- eleven enormous, silent hulls scattered across '
                'the twilight zone, surrounded by the ruins of the civilisation they '
                'founded. Their interiors are preserved as they were when the colonists last '
                'walked through them. The personal effects of the original settlers are '
                'still in the cabins. The names of the children born in transit are still '
                'etched into the bulkheads.\n\n'
                'MERIT has declared the Arks protected monuments. They are the oldest human '
                'structures beyond Sol. They carried people who believed that reaching '
                'another star was worth a lifetime in the dark. They were right. They just '
                'did not live to see what happened next.'
            ),
            population=0,
        ),
        StellarObject(
            name='Proxima Memorial',
            short_description='An orbital station above the dead colony -- archive, memorial, and the conscience of the system.',
            long_description=(
                'Proxima Memorial is a small orbital station above Proxima b, maintained by '
                'MERIT as the primary memorial to the Proximan civilisation. The station '
                'houses the archive of Proximan culture -- everything that survived: their '
                'scientific records, their art, their literature, their music, the personal '
                'letters and journals recovered from the Arks and the settlement ruins. The '
                'Proximans were prodigious record-keepers. They documented everything, '
                'because they understood that they were building something new and wanted '
                'future generations to know how it was done.\n\n'
                'The archive is comprehensive and devastating. The scientific data includes '
                'the observational records that led to the jump drive -- the raw data that '
                'the Proximans transmitted to Sol, annotated with their own analysis and '
                'hypotheses. The personal records include the messages of growing concern '
                'as the national claims escalated, the increasingly desperate proposals for '
                'cooperative development that were transmitted to Earth and never answered, '
                'and the final communications from the settlement leaders as the bombardment '
                'began. The last recorded transmission from Proxima is a plea for ceasefire '
                'addressed to all factions simultaneously. It was received in Sol four years '
                'later, long after the senders were dead.\n\n'
                'The station staff are volunteers who serve longer postings than any other '
                'MERIT personnel in Alpha Centauri. Curating the Proximan archive is '
                'considered a solemn duty, and the staff who do it tend to be people for '
                'whom the work is personal. The station is visited less frequently than the '
                'Elysium Memorial -- Proxima is further from the main transit routes, and '
                'the story it tells is harder to bear. The Elysium Memorial is about the '
                'cost of war. The Proxima Memorial is about the cost of ingratitude.'
            ),
            population=400,
        ),
        StellarObject(
            name='Proxima Relay',
            short_description='A frozen outer body converted into a communications relay and navigation beacon for system transit.',
            long_description=(
                'Proxima Relay is a small, frozen body in the outer reaches of Proxima '
                'Centauri\'s influence -- too cold and too small for colonisation, but useful '
                'as a communications relay and navigation beacon. The relay was established '
                'after the war as part of the infrastructure needed to manage transit through '
                'the system. It is automated, maintained by periodic service visits, and '
                'unremarkable except for its function: Proxima Relay is one of the navigation '
                'points that ships use to plot safe courses through the system, avoiding the '
                'debris fields, contaminated zones, and radiation hazards that make Alpha '
                'Centauri transit more complicated than it should be.\n\n'
                'The relay also serves as an emergency beacon. Ships that suffer drive '
                'failure or other emergencies in the outer system can reach Proxima Relay\'s '
                'signal and call for assistance from the MERIT station. The relay has saved '
                'lives -- not dramatically, not heroically, but in the quiet way that '
                'infrastructure saves lives when it works as designed. The Proximans would '
                'have appreciated that. They understood infrastructure.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Graveyard',
            short_description='The vast debris field between the A and B subsystems -- wreckage of the fleets that fought the war.',
            long_description=(
                'The space between Alpha Centauri A and B is littered with debris. The '
                'Graveyard is not a single location but a vast, dispersed field of wreckage '
                'spread across the transit zone between the two subsystems -- the remains of '
                'the warships, transports, stations, and orbital infrastructure that was '
                'destroyed during the conflict. At its densest points, the Graveyard is a '
                'navigation hazard. At its thinnest, it is an occasional contact on long-'
                'range sensors -- a piece of hull plating tumbling in the dark, a frozen '
                'engine housing, a section of habitat module with the atmosphere long since '
                'vented.\n\n'
                'Salvage operations were conducted extensively in the century after the war '
                'and recovered the bulk of the militarily sensitive material. What remains is '
                'the material that was not worth recovering -- structural debris, civilian '
                'wreckage, and the smaller fragments that are too dispersed to collect '
                'economically. The Graveyard contains human remains. The number is unknown. '
                'Recovery operations retrieved what they could, but the field is vast and '
                'the remains are scattered. MERIT considers the entire Graveyard a war '
                'grave and prohibits unauthorised salvage, though enforcement in a debris '
                'field this large is impractical. Vulture-class salvage ships are '
                'occasionally caught operating in the Graveyard and prosecuted, but the '
                'practice continues.\n\n'
                'Ships transiting between the A and B subsystems pass through the Graveyard. '
                'It is unavoidable. Experienced captains say nothing. New crews stare at the '
                'sensor contacts and try to identify what each piece of debris used to be. '
                'The Graveyard is the largest monument to the war -- not built, not designed, '
                'just left where it fell.'
            ),
            population=0,
        ),
        StellarObject(
            name='Centauri Waystation',
            short_description='MERIT\'s major transit station -- refueling, repair, and the only place in the system where anyone stops willingly.',
            long_description=(
                'Centauri Waystation is a large orbital station maintained by MERIT in a '
                'stable orbit between the A and B subsystems, positioned to serve the transit '
                'traffic that passes through Alpha Centauri on the major routes into and out '
                'of Sol. The station provides refueling, repair, medical services, and the '
                'other amenities that travellers need. It is the only place in the system '
                'where ships stop willingly.\n\n'
                'The station is well-equipped and professionally run, but there is a '
                'melancholy to it that visitors notice immediately. The staff rotate on '
                'short postings -- typically three to six months -- because MERIT does not '
                'assign long-term postings in Alpha Centauri. The radiation environment in '
                'the system, while manageable with shielding, accumulates over time, and '
                'MERIT policy limits cumulative exposure. This means the station never '
                'develops the settled feel of a permanent installation. The staff are always '
                'new. The personal touches that make a station feel like a community are '
                'always temporary. The notice boards are always out of date.\n\n'
                'The station\'s observation deck faces the A subsystem, and on a clear day '
                'the wreckage of Prometheus Station\'s shipyards is faintly visible as a '
                'glint in the distance. The deck is popular with travellers waiting for '
                'refueling. Most of them look once and do not look again. The station bar '
                'serves drinks named after the dead colonies. The bartenders rotate too '
                'frequently to know why this is considered poor taste by the long-term '
                'residents of Xinhua who occasionally pass through.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Elysium Memorial',
            short_description='An orbital memorial above New Eden -- a museum, archive, and place of mourning.',
            long_description=(
                'Elysium Memorial is a small orbital station in low orbit above New Eden, '
                'directly over the ruins of the Elysium colony. It was built a century after '
                'the war as a memorial and archive -- a place to remember what happened and '
                'why. The station houses a comprehensive archive of the Alpha Centauri War: '
                'personal records of the colonists, military communications from both sides, '
                'environmental data showing the atmospheric degradation in real time, and '
                'the names of every person confirmed dead in the system. The names take up '
                'an entire wall of the central gallery. There are over eight million of '
                'them.\n\n'
                'The observation gallery faces downward, toward New Eden\'s surface. Visitors '
                'can see the grid pattern of Elysium\'s streets through the thin atmosphere '
                '-- the city laid out below, perfectly preserved by the cold and the absence '
                'of life. At certain angles, the spaceport is visible, where the evacuation '
                'transports launched. The memorial hosts school groups from Sol and the inner '
                'systems -- children who learn about the war in classrooms and then stand at '
                'the observation gallery and look down at what the war produced. The memorial '
                'staff say that the children are always quiet afterward. The adults are too.\n\n'
                'The station is maintained by a small permanent staff who are the exception '
                'to MERIT\'s rotation policy -- memorial staff serve longer postings by '
                'choice, accepting the cumulative exposure as the cost of doing work they '
                'consider important. The station receives a steady flow of visitors. It is '
                'the most visited site in Alpha Centauri, and the least enjoyed.'
            ),
            population=800,
        ),
        StellarObject(
            name='Haven',
            short_description='A small moon of Jericho that escaped the war unscathed -- now a quiet residential settlement.',
            long_description=(
                'Haven is a small, irregular moon in a distant orbit of Jericho -- far '
                'enough from the gas giant and its three large moons that it was not '
                'included in the South American Federation\'s claim and was not targeted '
                'during the war. It was overlooked. This accident of orbital mechanics and '
                'bureaucratic oversight saved it. Haven is one of the very few bodies in '
                'Alpha Centauri that was not bombed, gassed, irradiated, or otherwise '
                'damaged during the conflict.\n\n'
                'After the war, Haven became a refuge for survivors who could not bear to '
                'leave the system but could not live on the damaged worlds. A small colony '
                'was established in shielded habitats -- the shielding is necessary not '
                'because Haven itself is damaged but because the broader system environment '
                'carries elevated radiation from the war. Haven\'s population is descended '
                'from survivors of multiple colonies -- Elysium evacuees, Carthage refugees, '
                'South American Federation citizens who were off-world when Jericho\'s moons '
                'were gassed. The community is small, close-knit, and carries the weight of '
                'the system\'s history in its family names. Everyone in Haven is descended '
                'from someone who lost everything. The culture is gentle, careful, and '
                'profoundly unwilling to fight about anything.'
            ),
            population=8_000_000,
        ),
        StellarObject(
            name='Anchor Point',
            short_description='The primary jump point station -- where ships enter and leave Alpha Centauri on the Sol route.',
            long_description=(
                'Anchor Point is the station that controls access to the primary jump point '
                'connecting Alpha Centauri to Sol -- the busiest jump point in the system and '
                'one of the busiest in the inner systems. The station handles traffic '
                'management, customs inspection, and emergency services for the constant '
                'flow of ships passing through. Alpha Centauri is a waypoint on multiple '
                'major trade routes, and Anchor Point processes thousands of transits per '
                'day.\n\n'
                'The station is efficient and impersonal in the way that transit hubs tend '
                'to be. Ships arrive, queue for the jump point, and leave. Most do not stop '
                'longer than necessary. The crews keep their viewports shuttered and their '
                'sensors passive. Nobody wants to look at Alpha Centauri longer than they '
                'have to. The traffic controllers at Anchor Point have the most '
                'psychologically demanding job in the system -- not because the work is '
                'dangerous but because they do it surrounded by the evidence of what happened '
                'here, processing ships that are in a hurry to leave, shift after shift, '
                'month after month, before their rotation ends and they can leave too.\n\n'
                'Like Centauri Waystation, Anchor Point staff rotate on short postings. '
                'The station is always functional. It is never home.'
            ),
            population=230_000_000,
        ),
    ],
    short_description='Humanity\'s first colony beyond Sol -- its people gave us the stars, and we destroyed them for it.',
    long_description=(
        'Alpha Centauri should have been the beginning. Before the jump drive, before '
        'faster-than-light travel was possible, humanity reached Alpha Centauri the hard '
        'way -- generation ships, launched from Sol orbit, carrying thousands of '
        'volunteers on journeys that took decades. The colonists who arrived at Proxima b '
        'built a civilisation with their bare hands on a world that barely tolerated '
        'human life. They were peaceful, cooperative, and resourceful. They were also the '
        'people who made everything that followed possible.\n\n'
        'The Proximan colonists\' observations of spatial distortions within the Alpha '
        'Centauri system -- data that could only be gathered from within the system, not '
        'from Sol -- were essential to the development of the jump drive. The Proximans '
        'gave humanity the key to the galaxy freely, hoping it would be used for '
        'cooperative expansion. Instead, it triggered a scramble. Earth\'s nations raced '
        'to claim every habitable world in the system, ignoring the Proximans\' pleas for '
        'restraint and their proposals for shared development. Within years, the national '
        'claims had escalated into the Alpha Centauri War -- the first and most '
        'devastating interstellar conflict in human history.\n\n'
        'The war lasted four years and killed over eighty million people. Orbital '
        'bombardment stripped the atmosphere of the most promising habitable world. '
        'Chemical weapons killed entire moon colonies. Kinetic strikes shattered '
        'underground cities. Incendiary campaigns burned agricultural worlds to prevent '
        'rivals from feeding their populations. The Proximans -- who had no military, no '
        'national affiliation, and no part in the conflict -- were destroyed as '
        'collateral, suspected by all sides and protected by none. Every generation-ship '
        'colonist, every descendant of the volunteers who had crossed the void to build '
        'something better, was killed. They gave humanity the stars. Humanity gave them '
        'nothing in return.\n\n'
        'The Alpha Centauri War is the reason MERIT exists. The unified government of '
        'the inner systems was born from the collective horror of what national '
        'competition had produced. The nations that fought the war dissolved themselves '
        'into MERIT within a generation, driven by the conviction that humanity could '
        'not be trusted to expand into the galaxy as divided peoples.\n\n'
        'Today, Alpha Centauri is a transit system. Seven hundred and forty million '
        'people live here -- a small fraction of what the system could have supported. '
        'They live in shielded habitats because the system-wide radiation environment, '
        'while improved from its wartime peak, remains hazardous for long-term exposure. '
        'Ships pass through constantly -- Alpha Centauri sits on major routes into and '
        'out of Sol -- but they do not linger. Crews keep their viewports shuttered. '
        'The system has improved since the war. The trajectory is positive. But the '
        'trajectory of recovery is measured in centuries, and Alpha Centauri will bear '
        'its scars for longer than human civilisation has existed. It is the place where '
        'humanity learned what it was capable of, and the lesson has not been forgotten.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

SIRIUS = System(
    name='Sirius',
    star='Binary system: Sirius A (A1V blue-white main sequence, extraordinarily luminous), Sirius B (DA2 white dwarf)',
    population=6_400_000_000,
    distance_to_sol=8.6,
    stellar_objects=[
        StellarObject(
            name='Crucis',
            short_description='The innermost planet -- a molten, blinding hell too close to the brightest star humanity has ever colonised near.',
            long_description=(
                'Crucis is the innermost planet of Sirius A, and it is not so much a world '
                'as a cautionary illustration of what proximity to this star means. Sirius A '
                'is extraordinarily luminous -- over twenty times the output of Sol -- and '
                'Crucis orbits close enough that its day side is a landscape of molten rock '
                'and metallic vapour, glowing with reflected and re-radiated light bright '
                'enough to damage optical sensors at range. The night side is marginally '
                'cooler but still far beyond any tolerance for habitation or industrial '
                'operation.\n\n'
                'Crucis is uninhabited and will remain so. Early survey teams studied it '
                'remotely and concluded that the energy required to shield any installation '
                'on or near Crucis exceeded the value of anything the planet could provide. '
                'The planet\'s primary contribution to the system is as a reference point -- '
                'when residents of the outer worlds complain about the brightness and heat, '
                'someone inevitably points out that it could be worse. It could be Crucis.'
            ),
            population=0,
        ),
        StellarObject(
            name='Lumen',
            short_description='A tidally locked world where humanity first discovered alien life -- settled on the dark side, studied on the light.',
            long_description=(
                'Lumen is where humanity discovered that it was not alone in the universe. '
                'The second planet of Sirius A, tidally locked with one hemisphere facing '
                'the star in permanent, blinding day and the other in permanent night. The '
                'first colonists came for the dark side -- a region of perpetual shadow '
                'where the temperature was manageable and the radiation was blocked by the '
                'planet\'s own bulk. They built their settlements in the darkness, shielded '
                'and enclosed, and for the first few years the light side was nothing more '
                'than a hostile wasteland to be avoided.\n\n'
                'Then a survey team crossed into the twilight zone and found life.\n\n'
                'The organisms were simple -- bacterial mats and small arthropod-like '
                'creatures, the largest no bigger than a human thumb. They existed in the '
                'twilight band where the light was intense but not lethal, feeding on a '
                'form of photosynthesis so efficient that it could metabolise the extreme '
                'radiation output of Sirius A into biological energy. Nothing like it '
                'existed on Earth. Nothing like it had ever been theorised. The organisms '
                'were not merely surviving in conditions that would kill any Earth life -- '
                'they were thriving on the very radiation that made the light side '
                'uninhabitable to humans.\n\n'
                'The discovery was the most significant event in the history of biology. '
                'For the first time, humanity had proof that life could arise independently '
                'of Earth, in conditions radically different from anything in Sol. The '
                'implications were debated for decades. The organisms were studied '
                'exhaustively. The twilight zone was designated a research preserve, and '
                'the settlement on the dark side grew as xenobiologists, biochemists, and '
                'researchers from every discipline arrived to study the first alien '
                'ecosystem.\n\n'
                'Today, Lumen\'s dark side is home to two billion people. The settlement is '
                'the oldest and largest in the system, built in the permanent shadow of a '
                'world that faces a star too bright to look at. The dark-side cities are '
                'lit entirely by artificial light -- the residents have never seen their '
                'own sun and never will, because looking at Sirius A from Lumen\'s surface '
                'without protection would cause permanent blindness in seconds. The twilight '
                'zone remains a preserve. The organisms are still there, still feeding on '
                'the light, still being studied. The initial excitement has faded -- as '
                'humanity expanded further, alien life was found in other systems, and the '
                'discovery became less extraordinary and more normal. But Lumen was first. '
                'The researchers here do not let anyone forget that.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Umbra',
            short_description='A rocky world whose entire civilisation lives underground -- three billion people who have never seen their sky unshielded.',
            long_description=(
                'Umbra rotates, unlike Lumen, but this is not the advantage it might seem. '
                'A full rotation means every part of the surface is periodically exposed to '
                'the unfiltered output of Sirius A, and the planet\'s thin atmosphere '
                'provides inadequate shielding. The surface is bathed in radiation during '
                'the day that would be lethal to unprotected humans within minutes. The '
                'nights are dark and cold, the temperature swinging wildly between '
                'extremes. The surface is barren -- scoured rock and dust, bleached and '
                'irradiated, with no life of any kind.\n\n'
                'The colonists went underground. Umbra\'s crust is rich in stable rock '
                'formations that provide natural radiation shielding, and the settlements '
                'were carved into the subsurface -- vast excavated caverns lit by '
                'artificial light, connected by tunnel networks that span continents. Three '
                'billion people live in Umbra\'s underground cities, and the civilisation '
                'they have built is substantial: universities, cultural institutions, '
                'manufacturing, agriculture in subterranean farms lit by grow-lights. The '
                'quality of life is high. MERIT infrastructure provides the same standard '
                'of living as any inner-system world. The cities are spacious -- the '
                'excavation technology available to a post-scarcity civilisation can carve '
                'enormous volumes, and the caverns of the largest cities are big enough '
                'that the ceilings are lost in artificial haze, mimicking an open sky.\n\n'
                'Umbrans are a distinct culture. They live their entire lives underground '
                'and are comfortable with it in a way that visitors find disorienting. An '
                'Umbran child has never seen a natural sky, never felt wind that was not '
                'generated by atmospheric circulation systems, never experienced weather '
                'that was not scheduled. They do not consider this a deprivation. The '
                'surface is a hostile wasteland. Underground is where the living is. '
                'Umbrans who travel to other worlds report that open skies feel exposed '
                'and threatening, and that the sensation of direct sunlight on skin is '
                'viscerally alarming. Most adjust eventually. Some never do, and come home '
                'to the comfortable dark.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Cascade',
            short_description='An alien world of extraordinary biological diversity -- no human settlement, observed from orbit by a ring of research stations.',
            long_description=(
                'Cascade is the jewel of xenobiology. The fourth planet of Sirius A, it '
                'orbits further out than Lumen or Umbra, where the stellar radiation is '
                'less extreme but still far beyond anything in Sol. The planet has a thick, '
                'opaque atmosphere that filters and diffuses the starlight into a hot, '
                'bright, humid environment that would be deeply unpleasant for humans but '
                'is, for reasons that are still being studied, spectacularly hospitable to '
                'the kind of radiation-feeding biology first discovered on Lumen.\n\n'
                'Where Lumen has bacterial mats and small arthropods, Cascade has an '
                'ecosystem. The surface is covered in dense biological growth -- not plants '
                'in any Earth sense, but organisms that use the same extreme photosynthetic '
                'process as Lumen\'s life, scaled up into structures that function as the '
                'foundation of a complex food web. The growth ranges from ground-covering '
                'mats to towering vertical structures that reach dozens of metres, '
                'competing for access to the diffused starlight that filters through the '
                'atmosphere. Arthropod-analogues fill the ecological niches occupied by '
                'insects on Earth and then some -- the largest are the size of a human '
                'hand, and the diversity is staggering. No vertebrate-analogues have been '
                'identified. No intelligence has been detected. Cascade\'s life is complex '
                'but not clever.\n\n'
                'No human has ever set foot on Cascade\'s surface. The decision was made '
                'early and has never been revisited: Cascade is observed, not occupied. The '
                'risk of contamination -- in both directions -- was judged too great, and '
                'the scientific value of an untouched alien ecosystem too high to compromise. '
                'Instead, a ring of orbital research stations surrounds the planet, '
                'maintaining continuous observation through remote sensors, atmospheric '
                'sampling drones, and high-resolution imaging. The stations house several '
                'thousand xenobiologists, ecologists, and atmospheric scientists who spend '
                'their careers watching a world they will never touch.\n\n'
                'The data from Cascade has reshaped biology as a discipline. The discovery '
                'that complex ecosystems can arise from radiation-feeding photosynthesis '
                'expanded the theoretical range of habitable conditions by an order of '
                'magnitude. The ongoing study of Cascade\'s ecology -- its food webs, its '
                'reproductive strategies, its response to seasonal variation as the planet\'s '
                'orbit shifts its distance from Sirius A -- fills journals and funds '
                'careers. For xenobiologists, Cascade is the most important place in the '
                'galaxy. For everyone else, it is a fascinating curiosity that they intend '
                'to read about someday.'
            ),
            population=0,
        ),
        StellarObject(
            name='Cascade Station',
            short_description='The orbital research complex above Cascade -- thousands of scientists watching an alien world they will never walk on.',
            long_description=(
                'Cascade Station is not a single station but a network of twelve orbital '
                'platforms in various orbits around the planet, collectively forming the '
                'most comprehensive planetary observation system ever constructed. Each '
                'platform specialises: atmospheric chemistry, surface ecology, deep-ocean '
                'thermal vents, arthropod behaviour, photosynthetic efficiency mapping, and '
                'a half-dozen other disciplines that did not exist as fields before Cascade '
                'was discovered.\n\n'
                'The stations are comfortable -- researchers serve long postings, and the '
                'facilities reflect this. Private quarters, good food, recreation spaces, '
                'and the best observation galleries in the system. The primary gallery on '
                'Cascade Station Alpha looks down on the planet\'s surface through '
                'magnification systems that can resolve individual organisms, and '
                'researchers spend hours watching the alien ecology go about its business. '
                'It is, by all accounts, deeply absorbing. The stations also have a '
                'reputation for a certain intensity of culture -- the researchers are '
                'passionate, competitive, and prone to fierce academic disputes that would '
                'be incomprehensible to anyone outside the field. Disagreements about '
                'arthropod reproductive taxonomy have been known to end friendships.\n\n'
                'The strict non-contact protocol is enforced absolutely. No probes land on '
                'the surface. No samples are taken directly -- atmospheric sampling is '
                'conducted from altitude, and biological material is only studied when it '
                'enters the upper atmosphere naturally. The protocol is debated periodically '
                'by researchers who argue that controlled surface sampling would accelerate '
                'understanding by decades. The counterargument is that Cascade is '
                'irreplaceable, and that the risk of contaminating the only known complex '
                'alien ecosystem is not justified by convenience. The debate continues. The '
                'protocol holds.'
            ),
            population=18_000,
        ),
        StellarObject(
            name='Pale',
            short_description='A cold outer world where Sirius A\'s light is finally manageable -- small settlements on a quiet, dim surface.',
            long_description=(
                'Pale is the first planet in the system where a human can stand on the '
                'surface during the day without immediate danger. This says more about the '
                'inner planets than it does about Pale. The fifth planet of Sirius A orbits '
                'far enough out that the star\'s punishing radiation has attenuated to '
                'merely uncomfortable levels -- surface exposure requires protective '
                'clothing but not hardened shelter, and the shielded habitats can use '
                'windows. Actual windows, with filtered glass, looking out at a dim, cold '
                'landscape under a sky dominated by the distant blue-white point of Sirius '
                'A. The residents consider windows a luxury. Visitors from Umbra find them '
                'unnerving.\n\n'
                'Pale\'s population is small -- a few hundred million in scattered '
                'settlements that exist because some people prefer a world where they can '
                'see the sky, even if the sky is cold and the star is distant. The economy '
                'is modest: some mining, some light manufacturing, and a research community '
                'that studies the outer system and Sirius B from a more convenient vantage '
                'point than the inner worlds provide. Pale is quiet. The people who live '
                'here chose quiet.'
            ),
            population=340_000_000,
        ),
        StellarObject(
            name='Meridies',
            short_description='A gas giant in the outer system -- its moons host fuel processing and long-range communications infrastructure.',
            long_description=(
                'Meridies is a mid-sized gas giant in the outer reaches of the system, '
                'orbited by a collection of icy moons that host fuel processing operations '
                'and long-range communications relays. The moons are lightly populated -- '
                'enclosed habitats housing the crews that operate the fuel extraction from '
                'Meridies\'s atmosphere and the technicians who maintain the communications '
                'infrastructure. The work is routine and the postings are long. The main '
                'attraction, according to the residents, is the view: Meridies fills the '
                'sky from its inner moons, banded in pale blues and whites, with Sirius A '
                'a brilliant but distant point that casts hard shadows across the moon '
                'surfaces.\n\n'
                'Meridies\'s fuel processing operations supply the system\'s ships and '
                'contribute to the broader inner-system fuel supply chain. The operation is '
                'not on the scale of Tau Ceti\'s industrial output but is significant '
                'enough that the infrastructure is well-maintained and the workers are '
                'well-compensated. The communications relays on the outer moons handle '
                'long-range traffic for the system and serve as one of several nodes in '
                'the inner-system communications network.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Lux Institute',
            short_description='The premier xenobiology research institution in human space -- an orbital campus between Lumen and Cascade.',
            long_description=(
                'The Lux Institute is the foremost centre for xenobiological research in '
                'the galaxy -- an orbital campus positioned between the orbits of Lumen and '
                'Cascade, giving it convenient access to both the original discovery site '
                'and the complex ecosystem. The Institute was founded a century after the '
                'discovery of life on Lumen, when the volume of research being conducted in '
                'the system had outgrown the ad-hoc facilities of the early years and '
                'needed a dedicated institution.\n\n'
                'The Institute is a university, a research laboratory, and a coordinating '
                'body for xenobiological research across the galaxy. Researchers who study '
                'alien life anywhere -- and alien life has been found in over a dozen '
                'systems since Lumen -- typically spend time at the Lux Institute at some '
                'point in their careers. The Institute\'s archives contain the most '
                'comprehensive collection of xenobiological data in existence, and its '
                'faculty includes the leading researchers in every subfield. A position at '
                'the Lux Institute is the most prestigious appointment a xenobiologist can '
                'hold.\n\n'
                'The campus is large for an orbital facility -- several interconnected '
                'modules housing laboratories, lecture halls, residential quarters for '
                'faculty and students, and the archive. The culture is academic in the best '
                'and worst senses: intellectually vibrant, socially insular, and prone to '
                'the kind of departmental politics that academics everywhere would recognise '
                'immediately. The Institute\'s social calendar revolves around seminar '
                'series, visiting lectures, and the annual Xenobiology Symposium, which '
                'draws researchers from across the inner systems and is, by all accounts, '
                'the most important and most exhausting week in the field.'
            ),
            population=120_000,
        ),
        StellarObject(
            name='Glare',
            short_description='A small, airless body in the inner system -- home to the system\'s solar energy collection and power distribution grid.',
            long_description=(
                'Glare is a small, airless body between the orbits of Crucis and Lumen -- '
                'too small to be a proper planet, likely a captured asteroid that settled '
                'into a stable orbit early in the system\'s history. Its value is its '
                'position: close enough to Sirius A that the energy flux is enormous, far '
                'enough that infrastructure can survive with heavy shielding. Glare hosts '
                'the system\'s primary solar energy collection grid -- vast arrays of '
                'hardened collectors that harvest a fraction of Sirius A\'s prodigious '
                'output and beam it as directed energy to receiving stations throughout the '
                'system.\n\n'
                'The energy available from Sirius A is extraordinary. Even the fraction '
                'collected by Glare\'s arrays exceeds the total energy consumption of most '
                'star systems. The surplus is exported -- Sirius is a net energy exporter '
                'to the inner systems, beaming power to relay stations that distribute it '
                'to systems with less generous stars. The operation is automated, maintained '
                'by shielded robots and overseen by a small crew of engineers who rotate '
                'on short postings. Working on Glare is well-paid and deeply boring. The '
                'engineers describe it as watching robots watch the sun.'
            ),
            population=5_000,
        ),
    ],
    short_description='The brightest light in the sky -- a system of extreme radiation, underground cities, and the first alien life humanity ever found.',
    long_description=(
        'Sirius is bright. This is the fact that defines everything about the system. '
        'Sirius A is an A-type main sequence star with over twenty times the luminous '
        'output of Sol, and living in its light is a fundamentally different experience '
        'from living in Sol or Tau Ceti or any of the gentler systems of the inner '
        'network. The inner planets are bathed in radiation that would kill an unprotected '
        'human in minutes. The habitable worlds are habitable only in the loosest sense '
        '-- Lumen is liveable on its dark side, Umbra is liveable underground, and Pale '
        'is liveable if you wear protective clothing outdoors. Six billion people live '
        'here anyway, because humans will live anywhere they can, and because Sirius has '
        'something no other system does.\n\n'
        'Sirius is where humanity discovered alien life. The bacterial mats and '
        'arthropod-like organisms found in Lumen\'s twilight zone were the first '
        'non-Earth biology ever identified -- organisms that had independently evolved a '
        'form of photosynthesis capable of metabolising the extreme radiation of an A-type '
        'star. The discovery transformed biology and reshaped humanity\'s understanding of '
        'where life could exist. The subsequent discovery of Cascade -- a world with a '
        'complex alien ecosystem built on the same radiation-feeding biochemistry -- '
        'elevated Sirius from a curiosity to the most important system in xenobiology. '
        'Alien life has since been found in over a dozen other systems, but Sirius was '
        'first, and the research infrastructure here reflects that primacy.\n\n'
        'The system is also accompanied by Sirius B, a white dwarf -- the collapsed '
        'remnant of a companion star that died long before humanity arrived. The dead '
        'star\'s red giant phase reshaped the system millions of years ago, and the '
        'planets that remain are survivors of that earlier catastrophe. Sirius B is '
        'studied by stellar physicists but plays little role in daily life.\n\n'
        'Sirius is not a military system or an industrial powerhouse. It is a place where '
        'people live, in conditions that outsiders find challenging and residents find '
        'normal. The underground cities of Umbra are comfortable and spacious. The '
        'dark-side settlements of Lumen are well-established and culturally rich. The '
        'floating research community around Cascade produces some of the most important '
        'science in the galaxy. The residents are proud of their system in the way that '
        'people are proud of difficult places -- they live here, they thrive here, and '
        'they are mildly amused by the horror that visitors express when they learn that '
        'the local sun can blind you in seconds. For the people of Sirius, the brightest '
        'star in Earth\'s sky is just the star they live under. They have learned to live '
        'in its shadow.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

EPSILON_ERIDANI = System(
    name='Epsilon Eridani',
    star='Young orange dwarf (K2V), 400-800 million years old, dimmer and warmer than Sol',
    population=12_500_000_000,
    distance_to_sol=10.5,
    stellar_objects=[
        StellarObject(
            name='Crimson',
            short_description='The innermost gas giant -- deep red and amber, banded in rust and scarlet, with the densest floating habitats in the system.',
            long_description=(
                'Crimson is the first of Epsilon Eridani\'s five gas giants and the closest '
                'to the star -- a massive world banded in deep reds, burnt ambers, and dark '
                'russet streaks that shift and swirl as storm systems the size of continents '
                'churn through the upper atmosphere. The colour comes from complex organic '
                'compounds and metallic hydrogen interactions in the cloud layers, heated by '
                'the relative proximity to the star into vivid, saturated hues that early '
                'surveyors described as looking like a world painted in dried blood and '
                'sunset.\n\n'
                'The floating habitats of Crimson are the oldest in the system -- the first '
                'platforms were established here because Crimson\'s atmosphere proved richest '
                'in the heavy volatiles that the extraction industry prizes most. The '
                'habitats float in the upper cloud layer on inertial resonators that shield '
                'them from the storms below, and the view from inside is extraordinary: the '
                'filtered light of Epsilon Eridani passes through the red and amber cloud '
                'layers and fills every space with a warm, deep glow that shifts from '
                'copper to crimson depending on the weather patterns below. The interior '
                'spaces of Crimson\'s habitats are suffused with this light. Walls, floors, '
                'skin, clothing -- everything takes on the red-gold cast of the atmosphere. '
                'Residents say you stop noticing after a few weeks. Visitors say they never '
                'stop noticing.\n\n'
                'Crimson is the most densely populated of the five giants -- three billion '
                'people live on platforms scattered across the upper atmosphere, a population '
                'density that surprises anyone who imagines gas giant habitation as a '
                'frontier experience. It is not. The platforms are cities -- large, '
                'comfortable, well-serviced, with the full infrastructure of any inner-'
                'system settlement. The difference is that the ground beneath the lowest '
                'level is not rock but cloud, and the cloud goes down for thousands of '
                'kilometres into crushing pressure and darkness. The residents do not think '
                'about this. Visitors think about it constantly.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Crucible',
            short_description='Crimson\'s largest moon -- a volcanically active world hosting the system\'s primary processing and refining operations.',
            long_description=(
                'Crucible is Crimson\'s largest moon -- a geologically violent body wracked '
                'by tidal forces from the gas giant, its surface dotted with active volcanoes '
                'and lava flows that glow against the dark rock. The geological activity is '
                'a hazard and a resource: Crucible\'s internal heat is harnessed for energy, '
                'and the volcanic mineral deposits supplement the gas harvesting economy. '
                'More importantly, Crucible hosts the system\'s primary gas processing and '
                'refining facilities -- the extracted volatiles from all five giants are '
                'shipped here for separation, purification, and packaging before export.\n\n'
                'The population lives in hardened surface habitats between the volcanic '
                'zones -- industrial settlements built to withstand seismic activity and '
                'occasional ashfall. Crucible is the working heart of the system\'s '
                'extraction economy, and the culture reflects it: practical, industrial, '
                'and proud of the unglamorous work that makes the colourful habitats on the '
                'giants possible. Crucible workers have a saying: the tourists come for the '
                'colours, but the colours come from Crucible.'
            ),
            population=450_000_000,
        ),
        StellarObject(
            name='Aurum',
            short_description='The golden giant -- banded in yellow and pale gold, encircled by a spectacular ring system that catches the starlight.',
            long_description=(
                'Aurum is the second gas giant and the most photographed object in Epsilon '
                'Eridani. The planet is banded in shades of yellow, pale gold, and cream, '
                'with storm systems that swirl in darker ochre. But the planet itself is '
                'secondary to the rings. Aurum\'s ring system is one of the most extensive '
                'in the inner systems -- a broad, bright disk of ice and dust particles that '
                'catches the warm light of Epsilon Eridani and scatters it into a golden '
                'halo visible from every other world in the system. When the angle is right, '
                'the rings cast a faint golden band across the sky of nearby habitats, and '
                'the shadow of the rings on the planet\'s cloud tops creates banded patterns '
                'of light and dark that shift with the orbital geometry.\n\n'
                'The floating habitats of Aurum are bathed in a warm, golden light that '
                'makes every surface glow as if lit by candlelight. The habitats here '
                'are the most popular with tourists -- the luxury liners that run Epsilon '
                'Eridani routes make Aurum their signature stop, and the tourism industry '
                'has shaped the culture of the upper-atmosphere platforms into something '
                'more polished and visitor-oriented than the other giants. The best '
                'restaurants in the system are on Aurum. The observation platforms that '
                'look out through the golden atmosphere at the rings above are considered '
                'one of the great experiences of the inner systems.\n\n'
                'The extraction operations on Aurum are productive but secondary to '
                'Crimson\'s -- the atmosphere is less concentrated in the heaviest volatiles '
                'but rich in lighter gases that are valuable in industrial chemistry. The '
                'ring system complicates orbital operations, requiring careful navigation '
                'through gaps in the rings to reach the floating platforms. Pilots who '
                'regularly fly the Aurum approach consider it a point of professional '
                'pride. Pilots who fly it for the first time consider it terrifying.'
            ),
            population=2_200_000_000,
        ),
        StellarObject(
            name='Viridis',
            short_description='The green giant -- a world of emerald and jade cloud layers, its habitats lit in shifting shades of green.',
            long_description=(
                'Viridis is the middle child of the system\'s five giants -- a world banded '
                'in shades of green that range from pale jade at the poles to deep emerald '
                'at the equator, with storm systems that churn in darker viridian. The '
                'colour is produced by methane and ammonia compounds in the upper atmosphere '
                'interacting with the orange light of Epsilon Eridani, and the effect is '
                'striking: Viridis looks alive in a way the other giants do not, its surface '
                'a shifting mosaic of greens that suggest vegetation even though nothing '
                'lives in the clouds.\n\n'
                'The floating habitats of Viridis are bathed in green-filtered light that '
                'gives every interior space the quality of a forest canopy -- dappled, '
                'shifting, and restful in a way that residents describe as the most '
                'comfortable of the five giants. The habitats here attract a population '
                'that values the aesthetic -- artists, writers, and people who chose their '
                'home based on the colour of the light. Viridis has a reputation as the '
                'most culturally productive of the giants, with a literary and arts scene '
                'disproportionate to its population. The quality of light is credited. '
                'Residents say that everything looks better in green.\n\n'
                'Viridis\'s atmosphere is particularly rich in compounds used in '
                'pharmaceutical synthesis and advanced materials fabrication. The extraction '
                'operations here are specialised and high-value -- the volume is lower than '
                'Crimson\'s, but the per-unit value of the extracted material is the highest '
                'in the system. The pharmaceutical companies that process Viridian '
                'atmospheric compounds maintain their own platforms alongside the '
                'residential habitats, and the line between extraction industry and '
                'settlement is blurrier here than on the other giants.'
            ),
            population=1_800_000_000,
        ),
        StellarObject(
            name='Bower',
            short_description='Viridis\'s largest moon -- a cold, quiet world that serves as a retreat and residential alternative to the floating habitats.',
            long_description=(
                'Bower is a large, icy moon orbiting Viridis at a comfortable distance -- '
                'far enough that the gas giant fills a portion of the sky without dominating '
                'it. The moon has a thin atmosphere, not breathable but enough to scatter '
                'light and create a pale, greenish sky tinted by the reflected light of '
                'Viridis. The surface is frozen but stable -- no volcanism, no tectonic '
                'activity, just ice and rock and quiet.\n\n'
                'Bower was settled by people who wanted to live in the Epsilon Eridani '
                'system but preferred solid ground beneath their feet. The habitats are '
                'enclosed surface settlements with views of Viridis hanging in the sky -- '
                'the green giant visible as an enormous, banded disc that moves through '
                'phases as the moon orbits. The population is modest but comfortable: '
                'families, retirees, and people who work remotely for the extraction '
                'industries or the universities. Bower has the unhurried quality of a '
                'residential community that exists because the view is beautiful and the '
                'rent is reasonable.'
            ),
            population=280_000_000,
        ),
        StellarObject(
            name='Azure',
            short_description='The blue giant -- banded in sapphire and cobalt, with delicate ice rings that shimmer in the starlight.',
            long_description=(
                'Azure is the fourth giant and the one that reminds visitors of home. The '
                'planet is banded in shades of blue -- deep sapphire at the equator, paler '
                'cobalt and ice-blue at the poles, with storm systems that swirl in darker '
                'navy. The resemblance to an enormous, cloud-banded Earth is superficial '
                'but emotionally powerful, and Azure has attracted a population that feels '
                'the pull of that resemblance. The floating habitats here are lit in blue-'
                'shifted light that gives interiors a cool, oceanic quality -- the opposite '
                'of Crimson\'s warm glow, and popular with people who find the warmer '
                'giants overwhelming.\n\n'
                'Azure\'s ring system is narrower and more delicate than Aurum\'s -- thin '
                'bands of ice particles that shimmer rather than blaze, catching the '
                'starlight in subtle arcs that are best viewed from the floating habitats '
                'below. Where Aurum\'s rings are spectacular, Azure\'s are elegant. The '
                'luxury liner routes that pass through Epsilon Eridani typically visit both '
                '-- Aurum for the drama, Azure for the refinement. The observation platforms '
                'on Azure\'s habitats look upward through the blue atmosphere at the '
                'shimmering rings and the stars beyond, and the view is considered the most '
                'serene in the system.\n\n'
                'Azure\'s atmospheric extraction focuses on hydrogen isotopes and noble gases '
                '-- materials critical to fusion reactor operation and advanced '
                'manufacturing. The operations are large-scale and steady, lacking the '
                'specialised high-value character of Viridis but contributing significantly '
                'to the system\'s overall output. Azure is the workhorse of the system\'s '
                'extraction economy -- not the most valuable per unit, but the most '
                'productive by volume after Crimson.'
            ),
            population=2_400_000_000,
        ),
        StellarObject(
            name='Stillwater',
            short_description='Azure\'s largest moon -- an ice world with subsurface oceans and the system\'s primary water supply.',
            long_description=(
                'Stillwater is a large ice moon with a subsurface ocean maintained by tidal '
                'heating from Azure -- a body similar in character to Europa in Sol, but '
                'larger and with more accessible water reserves. The moon\'s ice crust is '
                'tapped by extraction operations that supply fresh water to habitats across '
                'the system, and the subsurface ocean supports a modest but growing '
                'aquaculture industry that supplements the food supply.\n\n'
                'The surface settlements are industrial -- water extraction, ice processing, '
                'and the logistics of distributing water to floating habitats that cannot '
                'generate their own. The work is essential and unglamorous. Above the '
                'surface, Azure hangs in the sky as an enormous blue disc, its rings a thin '
                'bright line bisecting the giant. The workers on Stillwater have the best '
                'view of Azure in the system, and they are largely indifferent to it. '
                'Beautiful views do not make ice processing more interesting.'
            ),
            population=190_000_000,
        ),
        StellarObject(
            name='Amethyst',
            short_description='The outermost giant -- a distant world of deep violet and purple, the quietest and most remote of the five.',
            long_description=(
                'Amethyst is the outermost of Epsilon Eridani\'s five gas giants -- a cold, '
                'distant world banded in deep violet, purple, and dark lavender. The colour '
                'is produced by complex hydrocarbon hazes in the upper atmosphere that '
                'absorb the red end of the spectrum and scatter what remains into shades '
                'that range from pale lilac to near-black purple depending on the depth of '
                'the cloud layer. Amethyst is the dimmest and coldest of the five, its '
                'distance from Epsilon Eridani meaning that even the warm orange light of '
                'the K-type star is faint by the time it reaches the cloud tops.\n\n'
                'The floating habitats of Amethyst are lit in a violet twilight that '
                'residents describe as either haunting or peaceful depending on '
                'temperament. The light is dim enough that the habitats supplement '
                'atmospheric light with artificial sources, creating interiors where the '
                'violet glow of the atmosphere blends with warmer artificial light in a '
                'combination that is unique to Amethyst. The population is the smallest of '
                'the five giants -- people who live on Amethyst have chosen distance and '
                'quiet over the busier, brighter inner worlds. The culture is contemplative. '
                'Amethyst attracts researchers, writers, and people who are done with noise.\n\n'
                'The extraction operations on Amethyst focus on exotic heavy volatiles that '
                'form only in the cold, high-pressure conditions of the outer atmosphere -- '
                'compounds that are rare, difficult to synthesise artificially, and valuable '
                'enough to justify the cost of operating at the edge of the system. The '
                'volumes are small. The margins are high. Amethyst contributes the least to '
                'the system\'s total extraction output but produces materials that cannot '
                'be sourced anywhere else in the inner systems.'
            ),
            population=650_000_000,
        ),
        StellarObject(
            name='Prisma Station',
            short_description='The system\'s primary port of entry -- a transit hub and tourism gateway where luxury liners dock between giant tours.',
            long_description=(
                'Prisma Station is the system\'s main port -- a large orbital station in a '
                'central orbit that serves as the hub for interstellar traffic, cargo '
                'transit, and the tourism industry that has become a significant part of '
                'Epsilon Eridani\'s economy. The luxury liners that run the Epsilon Eridani '
                'routes -- Peacock-class ships carrying hundreds of wealthy passengers on '
                'tours of the five giants -- dock at Prisma between legs, and the station '
                'has developed the amenities to match: restaurants, observation lounges, '
                'and the booking offices of the tour operators that coordinate descents to '
                'the floating habitats.\n\n'
                'The station\'s observation deck offers a view that justifies the stop. From '
                'Prisma\'s orbit, multiple giants are visible simultaneously -- the exact '
                'combination depends on orbital positions, but on the best days, three or '
                'four of the five are visible as coloured discs scattered across the sky: '
                'the red glow of Crimson, the golden blaze of Aurum and its rings, the '
                'green jewel of Viridis, the blue calm of Azure. Amethyst is usually too '
                'distant to show colour to the naked eye, but telescopes on the observation '
                'deck can resolve its violet bands. Passengers on arriving ships often spend '
                'hours on the observation deck before proceeding to their tour. The system '
                'sells itself.\n\n'
                'Prisma also handles the less glamorous traffic: cargo ships carrying '
                'extracted volatiles to the inner systems, supply ships bringing food and '
                'manufactured goods to the habitats, and the constant shuttle traffic that '
                'moves people between the giants. The station is busy, crowded, and split '
                'between the polished tourism sections and the working docks where the '
                'extraction economy does its business. The two populations -- tourists in '
                'clean clothes and extraction workers in coveralls -- share the same '
                'corridors and regard each other with mutual incomprehension.'
            ),
            population=85_000_000,
        ),
        StellarObject(
            name='The Quarry',
            short_description='Epsilon Eridani\'s debris disk -- mined for construction material and ice, the unglamorous foundation beneath the colours.',
            long_description=(
                'The Quarry is Epsilon Eridani\'s debris disk -- a broad, young belt of '
                'asteroids, ice, and dust that encircles the outer system. The system is '
                'only a few hundred million years old, and the Palette reflects that youth: '
                'it is denser and more active than Sol\'s depleted Kuiper Belt, rich in ice '
                'and raw material that has not yet been swept up by planetary formation. The '
                'disk provides the construction material and water ice that the floating '
                'habitats require for maintenance and expansion, and small-scale mining '
                'operations work the Palette continuously.\n\n'
                'The Quarry is not as dense or as industrially significant as Tau Ceti\'s '
                'Veil -- the extraction economy here is focused on the gas giants\' '
                'atmospheres, not the disk. But the Palette provides the physical material '
                'that the habitats are built from, and without it the floating cities could '
                'not be maintained. The mining operations are modest, the workers are '
                'competent, and the work is overshadowed by the more dramatic and more '
                'profitable atmospheric extraction. The Quarry is the foundation that '
                'nobody thinks about.'
            ),
            population=35_000_000,
        ),
        StellarObject(
            name='Lantern',
            short_description='A small captured body between Aurum and Viridis -- home to the system\'s navigation control and traffic management.',
            long_description=(
                'Lantern is a small, rocky body in a stable orbit between Aurum and Viridis '
                '-- likely a captured asteroid from the Palette that settled into its current '
                'orbit early in the system\'s history. The body is too small for significant '
                'habitation but perfectly positioned for the system\'s navigation control '
                'centre, which manages the considerable traffic between the five giants and '
                'the interstellar jump points.\n\n'
                'Traffic management in Epsilon Eridani is more complex than in most systems '
                'because the destinations are gas giants rather than solid worlds. Approach '
                'vectors to floating habitats must account for atmospheric conditions, storm '
                'systems, and the constantly shifting positions of the platforms themselves. '
                'Aurum\'s ring system requires careful navigation. The luxury liner traffic '
                'adds a layer of scheduling complexity. Lantern\'s traffic controllers are '
                'among the most skilled in the inner systems, and they manage the ballet of '
                'ships, shuttles, cargo haulers, and liners that keeps the system moving '
                'with a competence that is invisible when it works and catastrophic when it '
                'doesn\'t. It always works.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='The rainbow system -- five vivid gas giants whose floating habitats are the most colourful places in the inner systems.',
    long_description=(
        'Epsilon Eridani is a young system orbiting a young star, and it looks like '
        'nothing else in human space. Five gas giants orbit the warm orange dwarf, each '
        'a different colour -- Crimson in deep reds and ambers, Aurum in gold with its '
        'spectacular ring system, Viridis in shifting emerald, Azure in sapphire blue '
        'with its delicate ice rings, and Amethyst in distant violet. The colours are '
        'produced by different atmospheric chemistries interacting with the warm orange '
        'light of the K-type star, and the effect across the system is a rainbow of '
        'worlds scattered against the black.\n\n'
        'Twelve and a half billion people live in Epsilon Eridani, almost all of them '
        'on floating habitats in the upper atmospheres of the five giants. The habitats '
        'ride on inertial resonators that shield them from the tempestuous storms below, '
        'and the light of the atmosphere filters through into every interior space -- '
        'red-gold on Crimson, warm yellow on Aurum, forest green on Viridis, cool blue '
        'on Azure, violet twilight on Amethyst. Life on the habitats is coloured by the '
        'giant you live on, literally and figuratively. The light shapes the culture, '
        'the mood, the aesthetic of each world\'s population. Residents of different '
        'giants recognise each other by complexion -- skin tones shift subtly over years '
        'of living in filtered light, and a Crimson resident has a warmth to their '
        'colouring that an Azure resident lacks.\n\n'
        'The system\'s economy is built on two pillars: extraction and tourism. The five '
        'giants are rich in rare and valuable gases and volatiles -- compounds that are '
        'difficult or impossible to synthesise and essential to advanced manufacturing, '
        'pharmaceutical production, and fusion reactor operation. The extraction '
        'operations are extensive and productive, and the refined volatiles exported from '
        'Epsilon Eridani supply industries across the inner systems. Tourism is the '
        'second pillar -- the system is one of the most popular luxury liner destinations '
        'in human space. Peacock-class liners run regular routes through the system, '
        'descending into the upper atmospheres of each giant in sequence so that '
        'passengers can experience the light of all five worlds. The tour takes weeks '
        'and is considered one of the great experiences of the inner systems. The '
        'observation platforms on Aurum, looking up through the golden atmosphere at the '
        'rings overhead, are the most photographed location in the galaxy outside Sol.\n\n'
        'Epsilon Eridani has no rocky habitable worlds -- the system is too young for '
        'terrestrial planets to have fully formed, and the giants dominate the orbital '
        'space. A few larger moons provide solid-ground alternatives for residents who '
        'prefer rock beneath their feet, and the system\'s debris disk supplies '
        'construction material. But the heart of the system is the floating habitats -- '
        'cities in the clouds of five coloured worlds, lit by filtered starlight in '
        'shades that exist nowhere else. The people of Epsilon Eridani live in colour, '
        'and they would not trade it for all the solid ground in the galaxy.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

PROCYON = System(
    name='Procyon',
    star='Binary system: Procyon A (F5IV-V bright yellow-white subgiant), Procyon B (DQZ white dwarf)',
    population=4_200_000_000,
    distance_to_sol=11.5,
    stellar_objects=[
        StellarObject(
            name='Anvil',
            short_description='A hot, dense inner world -- mining operations that sell to whoever is buying, regardless of faction.',
            long_description=(
                'Anvil is a hot, dense, rocky world in a close orbit around Procyon A -- too '
                'hot for comfortable surface habitation but rich in heavy metals that make '
                'it worth the discomfort. The mining operations on Anvil are the oldest '
                'continuous industry in the system, and they have survived every change of '
                'nominal control by the simple expedient of selling to whoever shows up '
                'with money. MERIT patrol in the system? Anvil sells to MERIT contractors. '
                'Hyades ships in orbit? Anvil sells to Hyades buyers. Both at once? Anvil '
                'sells to both and lets them sort it out.\n\n'
                'The mining settlements are enclosed, shielded against the heat and '
                'radiation, and built with the practical ugliness of installations that '
                'have been repaired, expanded, and jury-rigged for centuries without anyone '
                'ever commissioning a proper redesign. The architecture is a collage of '
                'MERIT-standard prefabricated modules, Hyades industrial components with '
                'their characteristic exposed conduits, and locally improvised sections '
                'that belong to no design tradition at all. This is Procyon in miniature: '
                'built from whatever was available, maintained by whoever was willing, and '
                'belonging to no one.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='Threshold',
            short_description='The most populous world in Procyon -- a temperate planet whose inhabitants have perfected the art of changing flags.',
            long_description=(
                'Threshold is the closest thing Procyon has to a capital, though calling it '
                'that would make its residents laugh. It is a temperate, habitable world '
                'with a breathable atmosphere, moderate climate, and the kind of '
                'unremarkable pleasantness that would make it a comfortable mid-tier colony '
                'in any stable system. In Procyon, it is the planet where most people live, '
                'where most business is conducted, and where the flag above the government '
                'building changes most frequently.\n\n'
                'Threshold has been under nominal MERIT control fourteen times and nominal '
                'Hyades control eleven times in the last century. The transitions '
                'follow a pattern that the locals have memorised: a faction establishes '
                'presence, installs an administration, begins collecting taxes, overreaches '
                'in some way that annoys the population, and the population begins quietly '
                'feeding intelligence to the other faction. The other faction sends a task '
                'force. The current administration withdraws rather than fight a pitched '
                'battle over a system that neither side considers strategically vital enough '
                'for heavy losses. The new faction installs an administration. The cycle '
                'begins again.\n\n'
                'The people of Threshold are experts in the soft arts of regime change. '
                'They know which records to hide and which to leave visible. They know how '
                'to restructure a business overnight so that it appears compliant with the '
                'new administration\'s regulations. They know how to be helpful without '
                'being conspicuous and obstructive without being identifiable. Every '
                'household on Threshold owns two sets of documentation, and most own three. '
                'The children learn which anthem to sing by checking which ships are in '
                'orbit. This is not disloyalty. It is survival, refined over generations '
                'into a culture that values adaptability above all else.\n\n'
                'The cities of Threshold are pleasant, functional, and deliberately '
                'unmonumental. No one builds anything too impressive because impressive '
                'things attract the attention of whichever administration is currently in '
                'charge, and attention is never good. Wealth on Threshold is invisible. The '
                'richest people dress modestly, live in unremarkable houses, and keep their '
                'real assets in accounts that exist in jurisdictions neither faction can '
                'reach.'
            ),
            population=1_800_000_000,
        ),
        StellarObject(
            name='Greymarket',
            short_description='A cool, arid world that has become the largest informal trading hub between MERIT and Hyades space.',
            long_description=(
                'Greymarket earned its name honestly. The third planet of Procyon A is a '
                'cool, arid world with thin but breathable air and a surface of scrubby '
                'plains and shallow dust seas. It is not particularly hospitable, but it is '
                'habitable, and more importantly it is useful. Greymarket is where the '
                'smuggling economy of Procyon becomes something closer to legitimate '
                'commerce -- a world of trading posts, warehouses, and broker offices where '
                'goods from MERIT space and goods from Hyades space change hands without '
                'the paperwork that either faction would require.\n\n'
                'The distinction between smuggling and trade on Greymarket is largely '
                'semantic. When MERIT controls the system, Hyades goods are technically '
                'contraband, and moving them is smuggling. When the Hyades controls the '
                'system, MERIT goods are restricted, and moving them is smuggling. When '
                'neither faction is paying close attention -- which is most of the time -- '
                'it is simply trade. The brokers of Greymarket handle everything: Hyades '
                'prosthetic components that MERIT citizens want but cannot legally import, '
                'MERIT medical technology that Hyades citizens need but cannot afford '
                'through legitimate channels, raw materials, luxury goods, information, and '
                'the occasional person who needs to cross the border without being noticed.\n\n'
                'The settlements on Greymarket are functional and ugly -- prefabricated '
                'structures clustered around landing pads, with warehouses outnumbering '
                'residences. The population is transient by nature: traders, brokers, '
                'smugglers, and the support staff that keeps them fed and housed. The '
                'permanent residents are the brokers themselves, who have built a culture '
                'around the deal -- the negotiation, the handshake, the exchange. Trust on '
                'Greymarket is personal rather than institutional, built on reputation '
                'rather than legal framework. A broker\'s word is their currency. Breaking '
                'it is the one offence that Greymarket punishes harshly, because without '
                'trust, the entire economy collapses.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Goliath',
            short_description='A gas giant in the outer system whose moons have become the contested ground where MERIT and Hyades forces actually clash.',
            long_description=(
                'Goliath is a mid-sized gas giant in the outer system -- unremarkable as a '
                'planet but strategically significant because of its position relative to '
                'the system\'s jump points. The easy jump points that connect Procyon to '
                'the broader network are clustered in the outer system, and Goliath\'s orbit '
                'passes near two of them. This makes Goliath\'s moons the natural staging '
                'ground for any faction that wants to control access to the system, and as '
                'a result, the moons of Goliath are where the fighting actually happens.\n\n'
                'The clashes are typically small-scale: patrol ships from one faction '
                'intercepting scouts from the other, brief skirmishes around the jump point '
                'approaches, the occasional raid on a supply cache hidden on one of the '
                'smaller moons. Neither side commits capital ships -- the hard jump points '
                'that could bring them to Procyon quickly are too small for anything above '
                'frigate class, and the easy jump points that capital ships can use take long '
                'enough that reinforcement is a strategic commitment rather than a tactical '
                'response. The result is a perpetual low-intensity conflict fought by '
                'corvettes, frigates, and the occasional destroyer -- ships small enough '
                'and cheap enough that losing one is an acceptable cost for both sides.\n\n'
                'The inhabitants of the inner planets watch the news from Goliath\'s moons '
                'with the same weary familiarity that people in contested regions have '
                'always watched news of border skirmishes. Another clash. Another ship '
                'damaged. Another rotation of troops. The people of Procyon have learned '
                'to measure the severity of a confrontation by whether cargo prices change. '
                'If the prices stay stable, the fighting is routine. If they spike, '
                'something serious is happening and it may be time to update the '
                'documentation.'
            ),
            population=0,
        ),
        StellarObject(
            name='Patchwork',
            short_description='Goliath\'s largest moon -- a scarred, contested body covered in abandoned military installations from both factions.',
            long_description=(
                'Patchwork is Goliath\'s largest moon and the most contested piece of real '
                'estate in the system. The surface is littered with military installations '
                '-- sensor arrays, supply depots, weapons emplacements, barracks, and '
                'communications relays built by both MERIT and the Hyades over the course of '
                'decades. Many are abandoned. Some are active. A few have been built by one '
                'faction, captured by the other, modified, abandoned, reoccupied, and '
                'modified again until the original builders would not recognise them. The '
                'surface is a palimpsest of military architecture -- MERIT\'s clean, '
                'modular design philosophy layered over and under the Hyades\' heavier, '
                'more industrial aesthetic, with local improvisations patching the gaps.\n\n'
                'The moon has a small permanent population -- not military, but the support '
                'staff and scavengers who make a living from the constant military churn. '
                'When a faction withdraws from an installation, the locals move in within '
                'hours, stripping anything of value before the other faction arrives. The '
                'scavenging economy on Patchwork is efficient and ruthless. Nothing is '
                'wasted. A MERIT sensor array abandoned on Tuesday is disassembled by '
                'Wednesday, sold on Greymarket by Thursday, and installed on a Hyades ship '
                'by the following week. The military planners on both sides are aware of '
                'this and have largely accepted it as a cost of operating in Procyon.'
            ),
            population=35_000_000,
        ),
        StellarObject(
            name='Freeport',
            short_description='Procyon\'s main orbital station -- a neutral ground where MERIT and Hyades ships dock side by side and pretend not to notice.',
            long_description=(
                'Freeport is Procyon\'s primary orbital station -- a large, sprawling '
                'installation in orbit above Threshold that serves as the system\'s main '
                'port, marketplace, and the closest thing Procyon has to neutral ground. '
                'The station is locally owned and operated, which in practice means it is '
                'owned by a consortium of Threshold\'s wealthiest families who have '
                'maintained control through every change of administration by being '
                'scrupulously, aggressively neutral.\n\n'
                'MERIT ships dock at Freeport. Hyades ships dock at Freeport. They dock in '
                'different sections, separated by the station\'s commercial district, and '
                'the station\'s management enforces a strict no-weapons policy in the shared '
                'areas with a private security force that both factions have learned to '
                'respect, if only because antagonising the station would mean losing access '
                'to it. The bars, restaurants, and trading floors of Freeport\'s commercial '
                'district are the one place in the system where MERIT officers and Hyades '
                'crew can be found in the same room. They do not socialise. They do not '
                'fight. They conduct business through intermediaries and pretend the other '
                'side is not there.\n\n'
                'Freeport is where the smuggling economy becomes visible. The cargo manifests '
                'that pass through the station are creative works of fiction -- goods are '
                'relabelled, repackaged, and assigned origins that bear no relationship to '
                'their actual provenance. The station\'s customs office exists, employs '
                'staff, and processes paperwork. The paperwork is fantasy. Everyone involved '
                'knows this. The customs officers are paid well enough not to notice, and '
                'whichever faction is nominally in control is usually too busy with the '
                'situation at Goliath to audit the cargo logs of a station that is, '
                'technically, compliant.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Driftway',
            short_description='A loose collection of ships and habitats at the system\'s edge -- the transient population that belongs to neither faction.',
            long_description=(
                'Driftway is not a world or a station but a community -- a loose, shifting '
                'collection of ships, improvised habitats, and docked vessels in the outer '
                'system, clustered near the easy jump points. The population is transient: '
                'people who are passing through Procyon and have not yet decided where they '
                'are going, people who are avoiding one or both factions, people who have '
                'been displaced by the fighting around Goliath, and people who simply prefer '
                'to live at the margins where nobody asks questions.\n\n'
                'Driftway grows and shrinks with the political tides. When a faction takes '
                'firm control of the inner system, Driftway swells with people who would '
                'rather not be governed. When control loosens, some of them drift back. The '
                'community is self-organising in a minimal, anarchic way -- disputes are '
                'settled by consensus or avoidance, resources are traded informally, and '
                'the only rule that everyone enforces is that you do not bring faction '
                'trouble to Driftway. MERIT deserters live alongside Hyades refugees live '
                'alongside independent traders who have outstanding warrants in both '
                'jurisdictions. Nobody asks. Nobody tells.\n\n'
                'Driftway is the part of Procyon that neither faction acknowledges and both '
                'use. Intelligence operatives from both sides are assumed to be present. '
                'Smugglers use Driftway as a waypoint. Ships that need repairs without '
                'official documentation find mechanics in Driftway who ask no questions and '
                'charge accordingly. The community is impermanent, uncomfortable, and free '
                'in a way that the inner planets -- with their careful neutrality and their '
                'practised compliance -- are not.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Lowfield',
            short_description='A cold, marginal world settled by Hyades defectors -- the most culturally Hyades place in a non-Hyades system.',
            long_description=(
                'Lowfield is a cold, rocky world on the outer edge of the habitable zone -- '
                'liveable in enclosed habitats but not the kind of world anyone would choose '
                'unless they had reasons to be far from the inner planets. The people who '
                'settled Lowfield had reasons. The colony was founded by Hyades defectors -- '
                'workers who had crossed into Procyon to escape the economic pressures of '
                'the Hyades cluster but who carried the culture with them. Lowfield is the '
                'most visibly Hyades place in Procyon: the architecture is industrial, the '
                'exposed conduits and visible welds of Hyades design philosophy on display '
                'everywhere, and the population has a higher rate of prosthetic modification '
                'than anywhere else in the system.\n\n'
                'The relationship between Lowfield and the rest of Procyon is complicated. '
                'The defectors left the Hyades because they did not want to live in that '
                'system -- because the economic pressure to replace their bodies piece by '
                'piece was something they could not bear -- but they are still culturally '
                'Hyades in ways that the Threshold natives find unsettling. The prosthetics '
                'are the most visible difference. On Threshold, a prosthetic limb is a '
                'medical device. On Lowfield, it is an economic tool, a cultural marker, '
                'and a source of identity that the bearer has a complicated relationship '
                'with. Many Lowfield residents left the Hyades to stop the process of '
                'replacement -- to keep whatever organic parts they had left. Others '
                'continued modifying voluntarily, but on their own terms rather than under '
                'economic duress. The distinction matters to them enormously and is largely '
                'invisible to outsiders.\n\n'
                'When the Hyades takes nominal control of Procyon, Lowfield is tense. The '
                'defectors are technically traitors. In practice, the Hyades forces that '
                'rotate through Procyon have larger concerns than hunting down economic '
                'refugees on a marginal world, and Lowfield is left alone. When MERIT takes '
                'control, Lowfield is also tense -- MERIT\'s official position on Hyades '
                'prosthetic culture is disapproving, and Lowfield\'s residents are never '
                'sure whether the current MERIT administration will treat them as refugees '
                'to be helped or as Hyades sympathisers to be watched. The answer varies. '
                'Lowfield endures regardless.'
            ),
            population=250_000_000,
        ),
    ],
    short_description='A contested border system between MERIT and the Hyades -- ungovernable, pragmatic, and profiting from the stalemate.',
    long_description=(
        'Procyon sits on the edge of the inner systems, two jumps from Sol by hard routes and five '
        'by easy routes -- close enough to matter, far enough to be difficult to control.  This gap between reach and force is the '
        'defining fact of Procyon\'s existence.\n\n'
        'The system sits between MERIT space and the Hyades cluster, and nominal control '
        'shifts between the two with a regularity that the inhabitants have learned to '
        'treat as weather. MERIT is stronger overall but cannot dedicate an invasion '
        'force to the Hyades without exposing itself to other rivals. The Hyades can defend their own space but cannot project force '
        'far beyond it. Procyon exists in the gap between these two realities -- too '
        'distant for either faction to hold permanently, too useful for either to '
        'abandon entirely. The result is a perpetual low-intensity contest fought by '
        'patrol ships and skirmishers around the outer-system jump points while the '
        'inhabited inner planets change flags and carry on.\n\n'
        'Four billion people live in Procyon, and they have developed a culture shaped '
        'entirely by impermanence. They are pragmatic, adaptable, and profoundly '
        'ungovernable. When MERIT establishes control, the population complies just '
        'enough to avoid provocation and sells intelligence to the Hyades on the side. '
        'When the Hyades takes over, the same population complies just enough and sells '
        'intelligence to MERIT. The smuggling economy is the system\'s true industry -- '
        'goods, people, and information flow between MERIT and Hyades space through '
        'Procyon\'s trading posts and orbital stations, relabelled and repackaged by '
        'brokers whose neutrality is enforced by the simple fact that antagonising '
        'either side would end the trade that feeds everyone.\n\n'
        'The people of Procyon do not consider themselves MERIT citizens or Hyades '
        'subjects. They are Procyonese, and their loyalty is to the system, to their '
        'neighbours, and to the practical business of surviving between two powers that '
        'are each too strong to defy and too distracted to obey. If ever either faction '
        'committed fully to holding Procyon, the system would fall in weeks. Both '
        'factions know this. Both also know that the occupation would be miserable, '
        'expensive, and ultimately pointless, because the people of Procyon have four '
        'billion citizens, two sets of documentation, and an inexhaustible willingness '
        'to wait out whoever is currently in charge.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

TAU_CETI = System(
    name='Tau Ceti',
    star='Yellow dwarf (G8.5V), slightly smaller and cooler than Sol, metal-poor',
    population=22_000_000_000,
    distance_to_sol=11.9,
    stellar_objects=[
        StellarObject(
            name='Forge',
            short_description='A scorched inner world whose automated smelting operations feed raw material to the shipyards above.',
            long_description=(
                'Forge is the innermost planet of Tau Ceti -- a small, airless, tidally '
                'locked rock close enough to the star that the day side runs hot enough to '
                'soften metal. Early surveyors recognised its potential immediately: the '
                'planet\'s crust is rich in heavy metals, and the proximity to the star '
                'provides functionally unlimited energy. Automated smelting operations were '
                'established on the terminator line within decades of colonisation, using '
                'the day-side heat as part of the refining process and the night-side cold '
                'for cooling and storage. The operations run continuously, crewed by '
                'rotating shifts of engineers who work in shielded surface habitats and '
                'complain about the heat.\n\n'
                'Forge\'s output is a fraction of what the Veil provides, but the material '
                'is different -- heavy metals and rare earths that the debris disk lacks. '
                'The shipyards above require both: the Veil provides bulk material, Forge '
                'provides the specialised alloys that go into reactor shielding, weapons '
                'housings, and the structural members that hold a capital ship together '
                'under combat stress. A dreadnought contains more material from the Veil '
                'by mass, but the material from Forge is what makes it a warship rather '
                'than a very large container.'
            ),
            population=85_000_000,
        ),
        StellarObject(
            name='Meridian',
            short_description='The most populous world in Tau Ceti -- a warm, dense civilisation built on shipyard wealth.',
            long_description=(
                'Meridian is the economic and cultural heart of Tau Ceti -- a warm, '
                'Earth-like world in the inner habitable zone with a breathable atmosphere, '
                'extensive oceans, and a population of eight billion. The planet was the '
                'first major colony established after the jump drive opened the system, and '
                'it grew rapidly as the shipbuilding industry expanded. Meridian is what '
                'happens when a planet develops in the economic shadow of the largest '
                'military-industrial operation in human space: prosperous, sophisticated, '
                'and shaped at every level by the presence of the yards.\n\n'
                'The cities of Meridian are large, modern, and wealthy. The economy is '
                'diversified -- Meridian is not a company town -- but shipyard money flows '
                'through everything. The engineers, designers, project managers, and '
                'administrators who run the orbital yards live on Meridian. The financial '
                'institutions that fund capital ship construction are headquartered here. '
                'The universities produce the naval architects and weapons engineers that '
                'the yards require. The restaurants, theatres, and cultural institutions '
                'exist because the population is large enough and wealthy enough to sustain '
                'them. Meridian is not Earth -- it lacks the depth of history and the sheer '
                'density of culture -- but it is the most comfortable and cosmopolitan '
                'world outside Sol.\n\n'
                'The military presence on Meridian itself is light. The SCN maintains a '
                'liaison office and a logistics headquarters, but the warships and the '
                'yards are in orbit, not on the surface. Meridian is a civilian world that '
                'builds warships for a living. The residents are proud of the yards in the '
                'way that a city is proud of its cathedral -- it defines them, it enriches '
                'them, and they can see it in the sky at night.'
            ),
            population=8_000_000_000,
        ),
        StellarObject(
            name='Pelagius',
            short_description='A water world with no dry land -- billions live on floating cities across an unbroken global ocean.',
            long_description=(
                'Pelagius has no land. The entire surface is a single, unbroken ocean -- '
                'hundreds of kilometres deep in places, warmed by the star and stirred by '
                'tidal forces from the outer planets into a complex system of currents and '
                'storms that the early surveyors found beautiful and terrifying in equal '
                'measure. The atmosphere is breathable, thick with moisture, and the sky '
                'is a permanent haze of cloud and spray that breaks occasionally to reveal '
                'a blue so deep it looks violet.\n\n'
                'The colonists built on the water because there was nowhere else to build. '
                'The floating cities of Pelagius are engineering achievements on a scale '
                'that rivals the shipyards themselves -- enormous platforms anchored to the '
                'ocean floor by deep-water tethers, supporting populations of millions each. '
                'The largest, Archipelago, is visible from orbit as a cluster of white '
                'structures on the blue surface, home to four hundred million people. The '
                'cities are connected by high-speed transit that skims the wave tops and by '
                'air traffic that threads through the cloud layer. Between the cities, the '
                'ocean is open water -- fishing operations, aquaculture farms, and the '
                'occasional research platform studying the deep ocean ecology that existed '
                'before humanity arrived and continues largely undisturbed below the '
                'thermocline.\n\n'
                'Pelagian culture is distinct from Meridian\'s. Where Meridian is shaped by '
                'the yards, Pelagius is shaped by the ocean. The population is less '
                'connected to the military-industrial economy and more oriented toward '
                'marine science, aquaculture, and the arts. Pelagius produces poets, '
                'musicians, and marine biologists in disproportionate numbers. The floating '
                'cities have a rhythm dictated by the ocean -- the swell, the weather '
                'systems, the migration patterns of the deep-water fauna. People who move '
                'to Pelagius from solid-ground worlds describe a period of adjustment to '
                'the constant, subtle motion of the city beneath their feet. People who '
                'grew up on Pelagius and move to solid ground describe the stillness as '
                'unsettling.'
            ),
            population=5_500_000_000,
        ),
        StellarObject(
            name='Haldane',
            short_description='A cool, rugged world home to the SCN\'s premier military academy and a hardy frontier-descended population.',
            long_description=(
                'Haldane sits on the outer edge of the habitable zone -- a cold, rugged '
                'world with a breathable but thin atmosphere, dramatic mountain ranges, and '
                'a population that takes a certain pride in living somewhere uncomfortable. '
                'The planet was colonised later than Meridian and Pelagius, initially as a '
                'mining and industrial base, and the early settlers were the kind of people '
                'who chose a hard world because they wanted the space and the independence '
                'that came with it. Haldane\'s culture retains that character -- practical, '
                'self-reliant, and unimpressed by the wealth and sophistication of Meridian.\n\n'
                'The SCN chose Haldane for its premier military academy precisely because '
                'of the environment. The Haldane Academy occupies a vast compound in the '
                'southern highlands -- a complex of training facilities, barracks, '
                'classrooms, and simulation centres where the officers who will command the '
                'fleet\'s warships are forged. The thin atmosphere and harsh terrain are '
                'features, not drawbacks -- cadets who train on Haldane are acclimatised to '
                'discomfort, altitude, and the kind of environmental adversity that builds '
                'the mental resilience the SCN values. The Academy has produced the majority '
                'of the fleet\'s senior officers for centuries. To graduate from Haldane is '
                'to carry a distinction that follows an officer through their entire career. '
                'The Academy on Earth is older and more prestigious in certain political '
                'circles, but within the fleet itself, Haldane is where reputations are '
                'made.\n\n'
                'The civilian population of Haldane is smaller than Meridian\'s or Pelagius\'s '
                'but substantial -- the planet supports agriculture in its temperate valleys '
                'and industry in its mineral-rich mountains. The relationship between the '
                'civilian population and the Academy is symbiotic and occasionally tense. '
                'The locals are proud of the Academy but not subordinate to it. Haldane is '
                'their world. The Navy is a guest, even if it is a permanent one.'
            ),
            population=2_800_000_000,
        ),
        StellarObject(
            name='The Halo',
            short_description='Tau Ceti\'s massive debris disk -- ten times the mass of Sol\'s Kuiper Belt and the richest mining field in the inner systems.',
            long_description=(
                'The Veil is what makes Tau Ceti what it is. A debris disk of staggering '
                'density -- ten times the mass of Sol\'s depleted Kuiper Belt -- encircling '
                'the outer system in a broad, thick band of asteroids, comets, dust, and '
                'ice. The Veil is the reason the shipyards are here. It is an effectively '
                'inexhaustible source of raw material: iron, nickel, carbon, silicates, '
                'water ice, and the lighter elements that make up the bulk of a starship\'s '
                'hull. Where Sol\'s asteroid belt was mined out centuries ago, the Veil will '
                'supply the yards for millennia at current extraction rates.\n\n'
                'Mining the Veil is dangerous work. The disk is dense enough that collision '
                'hazards are constant -- not the dramatic asteroid-dodging of entertainment '
                'media, but the grinding, statistical certainty that operating in the Veil '
                'long enough means taking impacts. Mining ships in the Veil are heavily '
                'armoured, and the crews are well-paid for the risk. The Veil also produces '
                'a constant rain of material into the inner system -- comets and asteroids '
                'perturbed out of the disk by gravitational interactions. Tau Ceti\'s inner '
                'planets experience a bombardment rate far higher than Sol\'s, and the '
                'planetary defense network that intercepts incoming debris is one of the '
                'most extensive in the inner systems. Meridian and Pelagius are safe because '
                'the defense network makes them safe, not because the Veil is benign.\n\n'
                'The Veil is also beautiful. From Meridian\'s surface, it is visible on '
                'clear nights as a faint band of light across the sky -- dimmer than a '
                'ring system, brighter than the zodiacal light in Sol. From within the Veil '
                'itself, the density of material creates a slow-moving, glittering field '
                'that mining crews describe with a fondness that surprises people who have '
                'never seen it. The Veil is dangerous and beautiful and useful, and it is '
                'the reason twenty-two billion people live in this system.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Sovereign Yards',
            short_description='The largest shipbuilding complex in human space -- where every SCN capital ship is built.',
            long_description=(
                'The Sovereign Yards are the beating heart of the Solar Combined Navy. '
                'Spread across high orbit above Meridian and extending outward toward the '
                'Veil, the Yards are the largest single shipbuilding complex in human space '
                '-- dozens of orbital dry docks, assembly platforms, fitting-out berths, and '
                'the associated logistics infrastructure that keeps them supplied. Every SCN '
                'capital ship is built here. Every dreadnought, every battleship, every '
                'carrier that forms the backbone of the fleet was assembled in the Sovereign '
                'Yards from Veil material and Forge alloys, fitted with weapons and systems '
                'manufactured across the inner systems, and launched into the fleet from '
                'these berths.\n\n'
                'The scale is difficult to comprehend from the surface. From Meridian, the '
                'Yards are visible at night as a constellation of lights that moves across '
                'the sky -- construction lights, welding arcs, the navigation beacons of '
                'ships under construction and ships delivering material. A dreadnought under '
                'construction is visible to the naked eye from the surface as a faint point '
                'of light. When a completed capital ship lights its engines for the first '
                'time during trials, the flare is bright enough to cast shadows on '
                'Meridian\'s night side. The residents watch. They always watch.\n\n'
                'The Yards are a military installation. Access is controlled by the SCN, '
                'and the security perimeter extends well beyond the physical infrastructure. '
                'Civilian traffic is routed around the Yards on approach to Meridian. The '
                'workforce is a mix of military personnel and civilian contractors -- the '
                'contractors are the majority, skilled shipwrights and engineers who live on '
                'Meridian and commute to orbit on daily shuttles. The military personnel '
                'handle weapons fitting, classified systems installation, and security. The '
                'relationship works because both sides need each other, and because the '
                'civilian contractors are paid extremely well. Building warships is skilled '
                'work, and the Yards compete for the best engineers with every other '
                'employer in the system.\n\n'
                'The Sovereign Yards have never been attacked. This is not because they are '
                'unassailable -- though the defensive perimeter is formidable -- but because '
                'attacking the Yards would mean war with MERIT on a scale that no faction '
                'has been willing to contemplate. The Yards are the deterrent as much as the '
                'ships they produce. Destroying the Yards would cripple the SCN\'s ability '
                'to replace capital losses. Failing to destroy them would guarantee a '
                'response built in those same Yards. The calculation has kept the peace for '
                'centuries.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Keel Row',
            short_description='The secondary shipyard complex -- frigate and destroyer production, refit, and the civilian yards.',
            long_description=(
                'Keel Row is the Sovereign Yards\' less glamorous sibling -- a sprawling '
                'complex of smaller dry docks and assembly platforms in a lower orbit than '
                'the main yards, handling the production of frigates, destroyers, corvettes, '
                'and the support ships that make up the bulk of the fleet by number. Where '
                'the Sovereign Yards build the capital ships that win wars, Keel Row builds '
                'the escorts, patrol vessels, and logistics ships that fight them day to '
                'day. Keel Row also handles the refit and repair of existing fleet vessels '
                '-- the steady, unglamorous work of keeping the fleet operational between '
                'new constructions.\n\n'
                'Adjacent to the military sections, Keel Row hosts the civilian yards -- '
                'commercial shipbuilders producing freighters, passenger liners, and the '
                'other vessels that make up the independent fleet. The civilian yards are '
                'smaller and less secure than the military sections, but they benefit from '
                'the same supply chain and the same pool of skilled labour. A shipwright who '
                'works on a destroyer hull one year might work on a Bison freighter the '
                'next. The skills transfer. The civilian yards also handle the conversion '
                'of decommissioned military hulls into civilian service -- a steady business, '
                'as the fleet retires older vessels and the commercial market absorbs them.\n\n'
                'Keel Row is where most of the system\'s shipyard workers actually work. The '
                'Sovereign Yards get the prestige, but Keel Row builds more ships per year '
                'by a significant margin. The workers know this and are not shy about '
                'mentioning it.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Talos',
            short_description='A gas giant on the inner edge of the Veil -- its moons serve as forward bases for disk mining operations.',
            long_description=(
                'Talos is a large gas giant orbiting in the gap between the outer habitable '
                'zone and the inner edge of the Veil -- a gravitational anchor that shapes '
                'the disk\'s inner boundary and collects a retinue of moons and captured '
                'asteroids. The planet itself is unremarkable as gas giants go, but its '
                'position makes its moons invaluable as staging bases for Veil mining '
                'operations. Three of the larger moons host enclosed habitats where mining '
                'crews rotate, equipment is maintained, and extracted material is processed '
                'before being shipped inward to the yards.\n\n'
                'Talos also serves a defensive function. The gas giant\'s gravity well '
                'captures a significant fraction of the Veil debris that would otherwise '
                'drift into the inner system, reducing the bombardment rate on Meridian and '
                'Pelagius. The planetary defense network monitors Talos\'s influence on the '
                'disk and tracks objects that the giant\'s gravity redirects rather than '
                'captures. Living on Talos\'s moons means living with the Veil visible '
                'overhead as a dense, glittering band -- closer and brighter than from the '
                'inner planets, a constant reminder of the material wealth and constant '
                'hazard that defines the outer system.'
            ),
            population=320_000_000,
        ),
        StellarObject(
            name='Fleet Anchorage',
            short_description='The SCN\'s primary fleet staging area -- where the warships gather before deployment.',
            long_description=(
                'Fleet Anchorage is the SCN\'s primary staging area in Tau Ceti -- a vast '
                'volume of controlled space between Haldane\'s orbit and the Veil where '
                'completed warships are stationed, fleet exercises are conducted, and task '
                'forces are assembled before deployment. At any given time, the Anchorage '
                'hosts dozens of capital ships and hundreds of smaller vessels -- the '
                'reserve fleet, ships working up after construction or refit, and the '
                'training squadrons attached to the Haldane Academy.\n\n'
                'The Anchorage is not a single station but a network of logistics platforms, '
                'ammunition depots, fuel stores, and communications relays spread across a '
                'volume of space large enough to conduct fleet manoeuvres. The traffic is '
                'constant -- supply ships moving between the platforms, warships running '
                'trials, training exercises producing the controlled chaos of simulated '
                'combat. From Haldane\'s surface, the Anchorage is visible as a cluster of '
                'moving lights in the night sky, and cadets at the Academy learn to identify '
                'ship classes by the pattern of their running lights. This is tradition '
                'rather than tactical necessity, but the Academy is built on traditions.\n\n'
                'The concentration of military force at the Anchorage is the largest in the '
                'inner systems outside Sol itself. The political implications are not lost '
                'on anyone -- Tau Ceti is a MERIT system, and the fleet stationed here '
                'is a MERIT fleet, but the firepower assembled at the Anchorage exceeds '
                'what most factions can field in total. This is, depending on perspective, '
                'either reassuring or deeply concerning.'
            ),
            population=75_000_000,
        ),
        StellarObject(
            name='The Shield',
            short_description='Tau Ceti\'s planetary defense network -- an automated grid of interceptors protecting the inner worlds from Veil debris.',
            long_description=(
                'The Shield is not a single installation but a system-wide network of '
                'automated interceptor platforms, tracking stations, and kinetic defense '
                'batteries positioned between the Veil and the inner planets. Its purpose '
                'is simple: the Veil constantly sheds debris inward, and without '
                'intervention, Meridian and Pelagius would experience a bombardment rate '
                'that would make surface civilisation untenable. The Shield makes the inner '
                'system habitable.\n\n'
                'The network tracks every object above a certain mass threshold that crosses '
                'from the Veil into the inner system. Small debris is ignored -- it burns '
                'up in planetary atmospheres or is too small to cause damage. Larger objects '
                'are intercepted by kinetic defense batteries that shatter or deflect them '
                'before they reach the inhabited worlds. The system has operated for '
                'centuries and has never failed catastrophically, though near-misses are '
                'logged more frequently than the public is generally aware. The Shield is '
                'maintained by a dedicated division of MERIT\'s civil defense infrastructure '
                '-- not the SCN, but a civilian agency with military-grade equipment and '
                'military-grade funding.\n\n'
                'Residents of Meridian and Pelagius rarely think about the Shield. It is '
                'infrastructure, like water treatment or atmospheric monitoring -- essential, '
                'invisible, and easy to take for granted. The people who operate the Shield '
                'do not take it for granted. They are aware, in a way that the surface '
                'population is not, that the Veil is not merely a resource. It is a threat '
                'that is managed, not eliminated, and the management must never stop.'
            ),
            population=12_000_000,
        ),
        StellarObject(
            name='Farthest',
            short_description='A cold, distant world beyond the Veil -- Tau Ceti\'s outermost settlement, a research and deep-space monitoring station.',
            long_description=(
                'Farthest is a small, frozen world beyond the outer edge of the Veil -- the '
                'most distant inhabited body in the Tau Ceti system. The settlement is a '
                'research station and deep-space monitoring post, staffed by astronomers, '
                'physicists, and the sensor operators who watch the outer approaches. The '
                'population is small and specialised, and the posting is considered remote '
                'even by the standards of outer-system assignments.\n\n'
                'Farthest\'s primary scientific value is its position beyond the Veil. The '
                'debris disk blocks or distorts certain observations from the inner system, '
                'and Farthest provides a clear view outward that the inner planets lack. '
                'The station also monitors the Veil from the outside, tracking the large-'
                'scale dynamics of the disk -- gravitational perturbations, density '
                'variations, and the slow migration of material that determines what the '
                'mining operations will encounter in coming decades. The view from Farthest '
                'is striking: the Veil is visible as a broad, bright band across the inner '
                'sky, with Tau Ceti\'s light filtering through it, and the inner planets '
                'are tiny points of light embedded in the glow. It is beautiful in a cold, '
                'remote way that appeals to the kind of people who choose to work here.'
            ),
            population=3_000_000,
        ),
    ],
    short_description='The forge of the fleet -- Tau Ceti\'s massive debris disk feeds the largest shipyards in human space.',
    long_description=(
        'Tau Ceti is where the fleet is built. A metal-poor star orbited by a debris '
        'disk of staggering density -- ten times the mass of Sol\'s depleted Kuiper Belt '
        '-- the system was recognised early in the colonisation era as an unparalleled '
        'source of raw material for shipbuilding. The Sovereign Yards, established in '
        'high orbit above the habitable world of Meridian, grew over the centuries into '
        'the largest shipbuilding complex in human space. Every SCN capital ship is '
        'built here -- every dreadnought, every battleship, every carrier. The material '
        'comes from the Veil. The skilled labour comes from Meridian. The officers who '
        'will command the ships come from the Academy on Haldane. Tau Ceti is the '
        'complete cycle of naval power, from raw ore to commissioned warship, contained '
        'in a single system.\n\n'
        'Twenty-two billion people live in Tau Ceti, spread across four inhabited '
        'worlds and the orbital infrastructure of the yards, the fleet anchorage, and '
        'the Veil mining operations. The system is not purely military -- Meridian is a '
        'major civilian world, Pelagius is a water world of floating cities and ocean '
        'culture, and Haldane supports a substantial civilian population alongside the '
        'Academy. But the military presence is inescapable. The SCN maintains its '
        'largest concentration of forces outside Sol at the Fleet Anchorage, and the '
        'traffic in Tau Ceti reflects the dual nature of the system: freighters hauling '
        'material from the Veil to the yards, warships running trials after '
        'construction, civilian traffic moving between the planets, and the constant '
        'shuttle runs that carry the workforce from Meridian\'s surface to the orbital '
        'yards and back.\n\n'
        'The Veil defines the system. It provides the material that feeds the yards and '
        'the economy that supports twenty-two billion people. It also bombards the inner '
        'planets with debris that the Shield -- Tau Ceti\'s planetary defense network -- '
        'must intercept continuously. The residents live with this duality: the Veil is '
        'wealth and danger, resource and threat, the reason the system exists and the '
        'reason it requires constant vigilance. From Meridian\'s surface, the Veil is a '
        'faint band of light in the night sky. From the mining ships that work within '
        'it, the Veil is a glittering, dangerous, beautiful field of material that will '
        'be building warships long after everyone alive today is dead.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALTAIR = System(
    name='Altair',
    star='Bright white main sequence (A7V), rapidly rotating, visibly oblate, approximately 11 times Sol luminosity',
    population=34_000_000_000,
    distance_to_sol=16.7,
    stellar_objects=[
        StellarObject(
            name='Helio',
            short_description='A hot inner world of solar energy farms and automated industry -- Altair\'s power supply.',
            long_description=(
                'Helio is the innermost planet -- a small, airless world close enough to '
                'Altair that the energy flux from the bright A-type star is immense. Like '
                'Mercury in Sol or Forge in Tau Ceti, Helio\'s value is in its proximity to '
                'the star: vast solar collection arrays cover the day side, harvesting energy '
                'that is distributed throughout the system. Altair is eleven times more '
                'luminous than Sol, and Helio captures a fraction of that output that is '
                'still enormous by any standard.\n\n'
                'The installations are largely automated, maintained by a modest population '
                'of engineers in shielded habitats on the terminator line. Helio is not '
                'glamorous, but it is essential -- the energy it provides powers the '
                'infrastructure of the most populous system outside Sol. The engineers who '
                'work here rotate on comfortable postings and describe the work as quiet, '
                'well-paid, and entirely without surprises. In a system defined by the '
                'absence of drama, Helio is the most undramatic place of all.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Concord',
            short_description='The capital world of Altair -- fifteen billion people living in the most well-ordered civilisation outside Sol.',
            long_description=(
                'Concord is what happens when a habitable world is colonised under complete '
                'MERIT oversight from the very first landing. There was no rush, no '
                'competing claims, no corporate land-grab. The colonisation of Concord was '
                'planned, phased, and executed according to a development framework that '
                'allocated space for cities, agriculture, industry, and wilderness preserves '
                'before the first colonist set foot on the surface. The result, centuries '
                'later, is a world of fifteen billion people that works.\n\n'
                'The cities of Concord are beautiful in the way that well-planned cities '
                'are beautiful -- not the organic, chaotic beauty of Earth\'s megacities, '
                'which grew over millennia and carry the sediment of every era, but the '
                'clean, intentional beauty of cities designed from the ground up by people '
                'who knew what they were doing. The transit systems are efficient. The green '
                'spaces are generous. The housing is spacious. The infrastructure is modern '
                'and well-maintained. Concord is, by virtually every measurable metric, '
                'the best-run world outside Earth.\n\n'
                'This provokes complicated feelings. Residents of Concord are proud of their '
                'world and aware of its reputation. They are also aware that other systems '
                'consider Concord slightly sterile -- that the planned perfection of their '
                'cities lacks the character that messier worlds develop naturally. The '
                'criticism is not entirely unfair. Concord\'s cities do not have the layers '
                'of history that Earth\'s do, the improvisational charm of Procyon\'s '
                'settlements, or the dramatic beauty of Epsilon Eridani\'s floating habitats. '
                'What they have is comfort, safety, and a quality of life that is '
                'consistently excellent across the entire planet. The residents have decided '
                'this is enough. Visitors tend to agree, though they sometimes describe the '
                'experience as pleasant in a way they cannot quite remember afterward.\n\n'
                'Altair\'s light is brighter and whiter than Sol\'s -- the A-type star casts '
                'a light that makes colours appear more vivid and shadows sharper than on '
                'Earth. Concord\'s architects have used this to advantage: the cities '
                'use colour extensively, and the effect under Altair\'s bright white light '
                'is striking. The sky is a deeper blue than Earth\'s, shading to violet at '
                'the zenith, and the sunsets -- when the oblate, visibly flattened disc of '
                'Altair touches the horizon -- are famously vivid.'
            ),
            population=15_000_000_000,
        ),
        StellarObject(
            name='Landsbridge',
            short_description='Altair\'s second world -- warmer, lusher, and wilder than Concord, with a reputation as the relaxed sibling.',
            long_description=(
                'Landsbridge orbits slightly closer to Altair than Concord and is '
                'correspondingly warmer -- a lush, tropical world with dense vegetation, '
                'broad shallow oceans, and a climate that ranges from comfortably warm at '
                'the poles to genuinely hot at the equator. Where Concord was planned from '
                'the start, Landsbridge was colonised as Concord\'s overflow -- the second '
                'wave of settlement, still under MERIT oversight but with a slightly looser '
                'hand, and the difference shows. Landsbridge\'s cities are less rigidly '
                'planned, more sprawling, with organic growth patterns that reflect the '
                'preferences of the settlers rather than the projections of urban planners.\n\n'
                'The result is a world that feels more lived-in than Concord. The cities '
                'are colourful and slightly chaotic by Concord standards, which means they '
                'are well-organised by the standards of anywhere else. The culture is warmer '
                'and more outward-facing -- Landsbridge is where the system\'s entertainment '
                'industry is centred, where the festivals happen, where the restaurants are '
                'more experimental and the nightlife is more interesting. If Concord is the '
                'sibling who excels at school, Landsbridge is the sibling who has more '
                'friends.\n\n'
                'The natural environment is Landsbridge\'s other distinction. The tropical '
                'forests are dense, biodiverse, and spectacular -- not alien life, but Earth-'
                'derived ecosystems that have been established on the planet and evolved in '
                'the brighter light of Altair into something subtly different from their '
                'origins. The colours are more vivid. The growth is denser. Naturalists '
                'from other systems visit Landsbridge to study how Earth biology adapts to '
                'an A-type star\'s light, and the planetary parks are popular tourist '
                'destinations. Landsbridge lacks the manufactured spectacle of Epsilon '
                'Eridani\'s gas giants, but its natural beauty is genuine and extensive.'
            ),
            population=9_000_000_000,
        ),
        StellarObject(
            name='Greenvale',
            short_description='A temperate agricultural world -- Altair\'s breadbasket and the quietest of the three habitable planets.',
            long_description=(
                'Greenvale is the outermost of Altair\'s three habitable worlds -- a '
                'temperate planet with broad plains, mild seasons, and growing conditions '
                'that agricultural engineers describe as nearly ideal. Altair\'s bright '
                'light drives photosynthesis at rates that exceed Sol-standard, and the '
                'crops grown on Greenvale\'s plains produce yields that other agricultural '
                'worlds struggle to match. Greenvale feeds the system. Its surplus feeds '
                'neighbouring systems.\n\n'
                'The population is smaller than Concord\'s or Landsbridge\'s and distributed '
                'differently -- small cities separated by vast stretches of farmland, '
                'connected by efficient transit but with a pace of life that the urban '
                'populations of the inner planets would find unbearably slow. Greenvale\'s '
                'residents do not find it slow. They find it correct. The agrarian culture '
                'values steadiness, patience, and the long view -- qualities suited to '
                'people whose work follows the rhythm of growing seasons rather than market '
                'cycles.\n\n'
                'Greenvale is where people from Concord and Landsbridge retire. The cost of '
                'living is lower, the space is greater, and the quality of life is high in '
                'a different register from the urban worlds. The retirees bring money and '
                'culture from the cities. The locals tolerate them with the patient good '
                'humour of people who know that the newcomers will either adapt to the pace '
                'or leave. Most adapt. The ones who stay tend to become the most ardent '
                'defenders of Greenvale\'s unhurried character.'
            ),
            population=4_500_000_000,
        ),
        StellarObject(
            name='Colossus',
            short_description='A gas giant in the outer system -- its moons host fuel processing and the system\'s military garrison.',
            long_description=(
                'Colossus is a large gas giant in the outer system -- the gravitational '
                'anchor that organises Altair\'s outer orbital space. Its atmosphere is '
                'mined for fuel and industrial gases by operations based on its inner moons, '
                'and the outer moons host the system\'s MERIT military garrison. The '
                'garrison is modest by the standards of Tau Ceti or Sol -- Altair does not '
                'face external threats, and the military presence is more about maintaining '
                'the infrastructure of control than projecting force. Patrol ships, customs '
                'vessels, and a handful of frigates that spend most of their time on '
                'training exercises.\n\n'
                'The garrison\'s primary function is maintaining security on the jump point '
                'approaches -- routine work in a system where the traffic is orderly and the '
                'threats are minimal. Military postings to Altair are considered comfortable '
                'and slightly dull by SCN personnel. The facilities are excellent, the '
                'liberty on Concord and Landsbridge is generous, and nothing ever happens. '
                'Officers who serve at Altair tend to either appreciate the calm or request '
                'transfer to somewhere more eventful. Both responses are considered '
                'reasonable.'
            ),
            population=220_000_000,
        ),
        StellarObject(
            name='Bastion',
            short_description='Colossus\'s largest moon -- the MERIT garrison headquarters and the only place in Altair where anyone wears a uniform.',
            long_description=(
                'Bastion is the largest of Colossus\'s moons and the site of the MERIT '
                'military garrison -- the headquarters, barracks, training facilities, and '
                'logistics infrastructure that support the system\'s modest defence force. '
                'The moon is rocky, airless, and uninteresting by any standard except '
                'military. The facilities are well-maintained and comfortable in the way '
                'that MERIT military installations are always comfortable -- functional, '
                'clean, and designed by people who believe that good facilities produce good '
                'morale.\n\n'
                'Bastion is the only place in Altair with a significant military culture. '
                'The civilian worlds below are so peaceful that the concept of a standing '
                'military is abstract to most residents -- they know the garrison exists, '
                'they approve of it in a vague way, and they rarely think about it. The '
                'garrison personnel, for their part, rarely think about the civilians. '
                'Bastion is a military community in a system that does not need one, '
                'and the personnel are aware of the irony. They train, they patrol, they '
                'maintain readiness for threats that have not materialised in living memory. '
                'It is, they are told, important work. The telling is more convincing some '
                'days than others.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Tidebreak',
            short_description='An icy moon of Colossus with a subsurface ocean -- a research station and a growing aquaculture operation.',
            long_description=(
                'Tidebreak is an ice moon with a subsurface ocean maintained by tidal '
                'heating from Colossus. The ocean was discovered during the initial surveys '
                'and has been the subject of ongoing research since -- not because it '
                'harbours alien life (it does not) but because the chemistry of a '
                'subsurface ocean in an A-type star system differs in interesting ways from '
                'similar bodies in Sol. The research station is small and academic.\n\n'
                'More practically, Tidebreak has developed a growing aquaculture operation '
                'that taps the subsurface ocean for water and uses it to farm fish and '
                'seafood in enclosed facilities on the surface. The operation supplements '
                'Greenvale\'s agricultural output and provides the system with fresh seafood '
                'that is, according to residents of the inner planets, superior to anything '
                'grown in surface tanks. This claim is debated, but Tidebreak\'s fishing '
                'industry is proud and commercially successful regardless.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Altair Central',
            short_description='The system\'s primary orbital hub -- a transit station that handles the traffic of thirty-four billion people with quiet efficiency.',
            long_description=(
                'Altair Central is the system\'s main orbital station -- a large, modern '
                'installation in high orbit above Concord that handles interstellar traffic, '
                'inter-planetary transit, and the logistics of a system with thirty-four '
                'billion people across three habitable worlds. The station is efficient, '
                'well-designed, and unremarkable. This is not a criticism. Altair Central '
                'processes more traffic per day than most systems see in a week, and it does '
                'so with a smoothness that makes the operation look easy. It is not easy. '
                'It is the product of centuries of MERIT transit management expertise '
                'applied to a system that was designed for high throughput from the start.\n\n'
                'The station is clean, modern, and comfortable. The restaurants are good. '
                'The transit connections are reliable. The staff are professional and '
                'courteous. Travellers passing through Altair Central on their way to more '
                'dramatic destinations tend to forget it almost immediately, which is the '
                'highest compliment a transit hub can receive. The station does not want to '
                'be memorable. It wants to be seamless. It succeeds.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Farlight',
            short_description='An outer system body hosting long-range communications and the system\'s deep-space observatory.',
            long_description=(
                'Farlight is a cold, rocky body in the outer reaches of the system -- too '
                'small and too distant for significant habitation but well-positioned for '
                'the long-range communications relays and deep-space observatory that it '
                'hosts. The observatory studies the surrounding stellar neighbourhood and '
                'contributes to the inner systems\' astronomical survey programme. The '
                'communications relays handle long-range traffic for the system and serve '
                'as a node in MERIT\'s interstellar communications network.\n\n'
                'The staff are few and content. Farlight is the kind of posting that '
                'attracts people who like quiet work and long views. The observatory\'s '
                'primary telescope can resolve individual stars across dozens of light-years, '
                'and on clear nights -- which is every night, because there is no atmosphere '
                '-- the astronomers can watch the light of other civilisations. Altair\'s '
                'oblate disc is visible in the inner sky, visibly flattened by its rapid '
                'rotation, a squashed star spinning in the dark. The astronomers find this '
                'charming. It is, they note, a pleasantly odd thing to orbit.'
            ),
            population=2_000_000,
        ),
    ],
    short_description='The second most populous system outside Sol -- peaceful, prosperous, and well-ordered under complete MERIT governance.',
    long_description=(
        'Altair is what MERIT looks like when it works. Thirty-four billion people across '
        'three habitable worlds, governed under complete MERIT oversight since the first '
        'colony ship arrived, with no contested claims, no faction interference, and no '
        'history of conflict. The system was settled methodically -- Concord first, then '
        'Landsbridge, then Greenvale -- each world developed according to a plan that '
        'allocated resources, managed growth, and built the infrastructure of civilisation '
        'before it was needed rather than after. The result is a system that runs '
        'smoothly, provides well for its population, and offers a quality of life that is '
        'second only to Sol.\n\n'
        'The star itself is an A-type main sequence -- bright, white, and spinning so '
        'fast that it is visibly oblate, flattened at the poles and bulging at the '
        'equator. The rapid rotation causes gravity darkening: the poles are hotter and '
        'brighter than the equator, which means the light that reaches the habitable '
        'worlds varies subtly depending on orbital inclination and season. The practical '
        'effect is a light that is whiter and more vivid than Sol\'s, making colours '
        'appear saturated and shadows sharp. Altair\'s worlds are beautiful under this '
        'light in a crisp, clear way that visitors notice immediately and residents have '
        'long since stopped seeing.\n\n'
        'Altair is close enough to Sol that MERIT\'s authority is unchallenged and far '
        'enough from the contested borders that conflicts are entirely absent. The system\'s modest military garrison '
        'exists because MERIT maintains garrisons in all its systems, not because anyone '
        'expects trouble. The people of Altair are aware of the galaxy\'s conflicts in '
        'the way that people in comfortable places are aware of distant wars -- they '
        'follow the news, they have opinions, and they do not lose sleep.\n\n'
        'The criticism of Altair, when it comes, is that it is too comfortable -- that '
        'the planned perfection of its cities and the absence of friction have produced '
        'a civilisation that is pleasant but unremarkable. The criticism is not entirely '
        'unfair. Altair does not produce the art that comes from struggle, the innovation '
        'that comes from necessity, or the cultural depth that comes from history. What '
        'it produces is a good life for thirty-four billion people, and the residents have '
        'made their peace with the idea that this is enough. It is, they would argue, '
        'the entire point.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

CASTOR = System(
    name='Castor',
    star=(
        'Sextuple system in three binary pairs: '
        'Castor A (A1V blue-white) and Castor B (A2Vm blue-white) in a close inner orbit, '
        'Castor C (G-type yellow dwarf) and Castor D (K-type orange dwarf) in a wider intermediate orbit, '
        'Castor E (M1V red dwarf) and Castor F (M5V red dwarf) in a distant outer orbit'
    ),
    population=1_800_000_000,
    distance_to_sol=51.0,
    stellar_objects=[
        StellarObject(
            name='Sentinel',
            short_description='A hot, rocky world orbiting the bright inner pair -- home to the system\'s primary sensor array and early warning network.',
            long_description=(
                'Sentinel orbits the bright inner pair of Castor A and B -- a small, dense, '
                'airless world baked by the combined output of two blue-white stars. The '
                'surface is uninhabitable, but that was never the point. Sentinel hosts the '
                'system\'s primary sensor array -- a massive installation buried in the '
                'planet\'s crust, shielded from the stellar radiation, scanning every jump '
                'point approach and every cubic kilometre of the system\'s chaotic orbital '
                'space.\n\n'
                'Monitoring Castor is a problem unlike any other system in the inner worlds. '
                'Six stars in three binary pairs means six gravitational wells, three sets '
                'of binary orbital dynamics, and a volume of space where the gravitational '
                'landscape shifts continuously as the pairs orbit each other. Jump points in '
                'Castor are unusually numerous -- the complex gravitational interactions '
                'produce more spatial distortions than a single-star system -- and many of '
                'them are hard points that flicker and shift with the stellar tides. A hard '
                'jump point that opens near the AB pair on Tuesday may have drifted to the '
                'EF pair\'s orbital space by Thursday. Tracking them all is the primary '
                'occupation of Sentinel\'s staff.\n\n'
                'The sensor operators on Sentinel are considered the best in the SCN -- not '
                'because they are more talented than operators elsewhere, but because Castor '
                'demands more of them. A sensor operator in Sol watches predictable, stable '
                'space. A sensor operator on Sentinel watches a gravitational kaleidoscope '
                'and tries to distinguish a Pleiadian scout ship on a hard jump point from '
                'a gravitational echo produced by the EF pair\'s orbital shift. The work is '
                'exhausting, intellectually demanding, and critically important. Mistakes '
                'mean an undetected incursion into the system that guards two gateway routes.'
            ),
            population=8_000_000,
        ),
        StellarObject(
            name='Kania',
            short_description='A cool, rocky world orbiting the middle pair -- the largest permanent settlement and the system\'s administrative centre.',
            long_description=(
                'Kania orbits the CD pair -- the calmer middle binary of the G-type and '
                'K-type stars -- in a stable orbit that provides the most predictable '
                'conditions in the system. The planet has a thin but breathable atmosphere, '
                'surface water in shallow cold seas, and a landscape of grey rock, scrubby '
                'tundra, and low mountains under a sky lit by two suns -- the warm yellow '
                'of the G-type primary and the dimmer orange of the K-type companion, '
                'casting double shadows that shift as the pair orbits.\n\n'
                'Kania is the largest permanent settlement in Castor and the system\'s '
                'administrative centre. The population is overwhelmingly military and '
                'military-adjacent -- active SCN personnel, intelligence analysts, logistics '
                'staff, civilian contractors, and the families that have accumulated over '
                'centuries of permanent garrison presence. Kania is not a comfortable '
                'posting. The planet is cold, the landscape is bleak, and the double-star '
                'sky, while visually striking, is a constant reminder that this is not a '
                'normal system. But it is a permanent community in a way that the orbital '
                'stations are not -- children are born here, schools operate, and a culture '
                'has developed around the peculiar pride of living in the most strategically '
                'important system nobody wants to visit.\n\n'
                'The intelligence community on Kania is the system\'s other defining '
                'feature. Castor\'s position adjacent to both the Canopus and Pleiades '
                'gateway systems makes it the natural hub for MERIT\'s intelligence '
                'operations against those two factions. The analysts who work here process '
                'information from agents operating in Canopan and Pleiadian space, monitor '
                'communications traffic on the gateway routes, and coordinate the '
                'counter-intelligence efforts that occupy as much of the garrison\'s '
                'attention as conventional defence. Kania has more intelligence personnel '
                'per capita than any other installation in MERIT space. The bars are '
                'interesting places. Nobody talks about their work.'
            ),
            population=450_000_000,
        ),
        StellarObject(
            name='Omata',
            short_description='A cold, arid world in a wide orbit of the middle pair -- training grounds and weapons testing ranges.',
            long_description=(
                'Omata orbits the CD pair at a greater distance than Kania -- a cold, '
                'arid world with no liquid surface water and an atmosphere too thin to '
                'breathe without assistance. The planet is large, empty, and expendable, '
                'which makes it ideal for the two things the SCN needs space for: training '
                'and weapons testing.\n\n'
                'The surface is divided into designated ranges -- vast tracts of barren '
                'terrain allocated for ground combat exercises, orbital bombardment testing, '
                'and the evaluation of new weapons systems. The craters from decades of '
                'testing are visible from orbit, overlapping in dense clusters where the '
                'most popular ranges have been used and reused. Between the ranges, the '
                'surface is featureless dust plains that stretch to the horizon under a sky '
                'that shows both the CD pair\'s stars and, when orbital positions align, the '
                'bright points of the AB and EF pairs in the distance.\n\n'
                'The population is small and transient -- training units rotating through, '
                'weapons engineers conducting trials, and the maintenance staff that keeps '
                'the ranges operational. Nobody lives on Omata by choice. The postings '
                'are short, the facilities are functional rather than comfortable, and the '
                'planet\'s only virtue is that there is nothing on it worth worrying about '
                'destroying.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Cinder',
            short_description='A frozen, dead world orbiting the dim outer pair -- largely ignored except by intelligence operatives who value the privacy.',
            long_description=(
                'Cinder orbits the EF pair -- the two red dwarfs in the system\'s outermost '
                'binary, dim and cold and far from the inner pairs. The planet is frozen, '
                'airless, and geologically dead. Under the faint red light of its two small '
                'stars, the surface is a landscape of dark ice and ancient rock that has not '
                'changed in millions of years.\n\n'
                'Cinder is officially uninhabited. Unofficially, the EF pair\'s orbital space '
                'is where the system\'s quieter operations take place. The outer pair is far '
                'enough from the garrison infrastructure that sensor coverage is thinner, '
                'communications are harder to intercept, and activities can be conducted '
                'with a degree of privacy that the inner system does not offer. MERIT '
                'intelligence uses the EF pair\'s space for operations that benefit from '
                'discretion -- meetings with assets from the outer factions, signal '
                'intercept stations that are not listed in official inventories, and the '
                'kind of work that is necessary, sanctioned, and never discussed.\n\n'
                'The outer factions know this. Canopan and Pleiadian intelligence services '
                'also use the EF pair\'s space, for the same reasons. The result is a quiet, '
                'dark region of the system where multiple factions\' intelligence operatives '
                'conduct their business in careful proximity, each aware of the others, '
                'none acknowledging it. The occasional disappearance of a ship in the EF '
                'pair\'s orbital space is attributed to navigational hazard in the official '
                'reports. Nobody believes the official reports.'
            ),
            population=0,
        ),
        StellarObject(
            name='Bulwark Station',
            short_description='MERIT\'s primary fortress station -- the most heavily armed and reinforced installation between Sol and the outer systems.',
            long_description=(
                'Bulwark Station is the centrepiece of Castor\'s defences -- an enormous, '
                'heavily armoured orbital station positioned in the gravitational balance '
                'point between the AB and CD pairs, where it can respond to incursions from '
                'any direction. The station is the most heavily armed installation in MERIT '
                'space outside Luna itself -- weapons platforms, missile batteries, and '
                'point-defence systems layered in overlapping fields of fire that cover '
                'every approach vector. The station\'s armour is measured in metres of '
                'composite plating. The shields are military-grade, tested annually against '
                'live fire from the Omata ranges. Bulwark Station is not designed to be '
                'comfortable. It is designed to survive.\n\n'
                'The station houses the system\'s fleet command, the garrison\'s command '
                'staff, and the combat-ready ships that are always on alert for incursions '
                'through Castor\'s numerous jump points. The alert status is permanent -- '
                'Castor has never stood down to peacetime readiness since the outer systems '
                'declared independence. The crews rotate, the officers rotate, but the ships '
                'are always crewed and the weapons are always hot. The discipline this '
                'requires over decades and centuries is its own achievement. Fatigue, '
                'complacency, and the slow erosion of alertness are the real enemies at '
                'Bulwark Station, and the command staff fight them as seriously as they '
                'would fight an actual incursion.\n\n'
                'Actual attacks on Bulwark Station have never been attempted. The outer '
                'factions are not suicidal. The station exists to ensure that this remains '
                'true -- its purpose is deterrence, and deterrence works only as long as '
                'the threat is credible. The garrison maintains credibility by being '
                'conspicuously, relentlessly, boringly prepared.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Drachna',
            short_description='The forward station facing the Canopus gateway -- monitoring the route to the Undying and their reanimated fleets.',
            long_description=(
                'Drachna is a mid-sized military station positioned to cover the jump '
                'points that connect Castor to the Canopus gateway system. The station\'s '
                'focus is singular: watch the route to Canopan space and provide early '
                'warning of any fleet movement through the gateway. Canopan warships are '
                'distinctive on sensors -- heavy, slow, thick-hulled vessels that register '
                'as dense masses on gravimetric scans. The crews who can be reanimated from '
                'death fight differently than crews who cannot: Canopan ships absorb damage '
                'that would be catastrophic for other fleets, and the tactical planning at '
                'Drachna accounts for an enemy that does not stop when it should.\n\n'
                'The station also handles the intelligence traffic from MERIT assets '
                'operating in Canopan space. Reports on reanimation technology developments, '
                'fleet movements, political shifts among the Canopan elite -- the ancient, '
                'multiply-restored rulers who have cheated death so many times that the '
                'original person is a distant memory -- all pass through Drachna\'s '
                'analysis centre before being forwarded to Kania and Sol. The analysts '
                'who specialise in Canopan intelligence develop a particular expertise in '
                'reading a culture where the powerful are centuries old and the powerless '
                'are sold as reanimated labour. It is not comfortable work. Understanding '
                'Canopan society requires engaging with it on its own terms, and its terms '
                'are deeply unsettling.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Chiron',
            short_description='The forward station facing the Pleiades gateway -- watching for ships crewed by people who no longer look entirely human.',
            long_description=(
                'Chiron mirrors Drachna on the opposite side of the system -- a '
                'military station covering the jump points that connect to the Pleiades '
                'gateway. Where Drachna watches for heavy, dense Canopan warships, '
                'Chiron watches for something harder to detect: Pleiadian vessels are '
                'light, stripped-down, and crewed by biologically modified humans who need '
                'neither standard atmospherics nor standard lighting. A Pleiadian scout '
                'ship is small, cold, dark, and nearly invisible on sensors designed to '
                'detect vessels with human-standard life support signatures.\n\n'
                'Chiron\'s sensor systems have been specifically adapted for detecting '
                'Pleiadian vessels -- thermal signatures too cold for inhabited ships, '
                'atmospheric venting of chemical compositions that baseline humans cannot '
                'breathe, and the subtle gravitational signature of ships that are lighter '
                'than they should be because half the systems a normal ship carries are '
                'simply absent. The cat-and-mouse game between Chiron\'s sensors and '
                'Pleiadian infiltration craft is the most technically sophisticated '
                'detection challenge in the inner systems.\n\n'
                'The Pleiades is the faction that generates the most anxiety at Castor, '
                'despite being less militarily powerful than Canopus. The Canopans are '
                'predictable: heavy ships, direct approach, attritional tactics. The '
                'Pleiadians are not predictable. Their scouts slip through hard jump points '
                'that shift in the gravitational chaos of the sextuple system. Their '
                'operatives are biologically modified to survive environments that would '
                'kill baseline agents. Their ships are hard to find and harder to catch. '
                'Chiron catches most of them. The staff try not to think about the ones '
                'they miss.'
            ),
            population=65_000_000,
        ),
    ],
    short_description='MERIT\'s fortress system -- six stars, two gateway approaches, and the most concentrated military presence outside Sol.',
    long_description=(
        'Castor is a sextuple star system -- three binary pairs in a hierarchical orbit '
        'that makes it the most gravitationally complex inhabited system in human space. '
        'The bright inner pair of blue-white A-types dominates the centre. A G-type and '
        'K-type pair orbits at intermediate distance, hosting the system\'s only habitable '
        'world. A distant pair of red dwarfs marks the cold outer reaches. The six stars '
        'interact gravitationally in ways that produce a shifting, unstable landscape of '
        'jump points -- more numerous than in any single-star system, many of them hard '
        'points that flicker and migrate as the stellar orbits evolve. For a fortress '
        'system, it is a defensive nightmare. For infiltrators, it is a playground.\n\n'
        'Castor\'s strategic importance is its position. The system is adjacent to two '
        'outer-faction gateway systems: Canopus, gateway to the Undying and their '
        'reanimated fleets, and Alcyone, gateway to the Pleiades and their biologically '
        'modified crews. Any MERIT response to a threat from either faction routes through '
        'Castor. Any outer-faction incursion toward the inner systems must pass it. MERIT '
        'has reinforced the system accordingly -- Bulwark Station is the most heavily '
        'armed installation outside Luna, the garrison maintains permanent combat '
        'readiness, and forward stations face each gateway route with specialised '
        'detection and intelligence capabilities.\n\n'
        'Actual battles in Castor are rare. The concentration of MERIT force is too '
        'great for the outer factions to contest directly. Instead, Castor is a system '
        'of shadows -- intelligence operations, scouting missions, infiltration attempts, '
        'and the quiet, undeclared contest between MERIT\'s counter-intelligence services '
        'and the operatives of Canopus and the Pleiades. The sextuple star system\'s '
        'gravitational complexity helps the infiltrators: hard jump points appear and '
        'vanish, sensor coverage has gaps that shift with the stellar orbits, and the '
        'dim outer pair provides a region of reduced surveillance where all sides conduct '
        'business they would prefer not to discuss.\n\n'
        'One point eight billion people live in Castor, almost all of them connected to '
        'the military, the intelligence community, or the support infrastructure that '
        'sustains both. It is not a system where civilians settle by choice. The '
        'population is there because the mission requires them, and the mission -- '
        'watching two gateway routes, maintaining the deterrent, and fighting the shadow '
        'war that never makes the news -- does not end.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

VEGA = System(
    name='Vega',
    star='Bright white main sequence (A0V), approximately 40 times Sol luminosity, rapid rotator',
    population=7_500_000_000,
    distance_to_sol=25.0,
    stellar_objects=[
        StellarObject(
            name='Bleach',
            short_description='A scorched inner world of strip-mining operations and desperate labour -- the system\'s raw material supply.',
            long_description=(
                'Bleach is the innermost planet of Vega -- a small, airless, radiation-blasted '
                'rock that would have been ignored in any system with a functioning government '
                'and safety regulations. In Vega, it is a mining operation. The planet\'s '
                'crust is rich in metals, and the extraction is conducted by whoever currently '
                'controls the landing zones -- warlords who rotate with the kind of frequency '
                'that makes long-term planning impossible and short-term exploitation the only '
                'rational strategy. The mining is aggressive, unregulated, and dangerous. '
                'Equipment is old. Safety systems are whatever the operator could afford or '
                'steal. Workers are the people who could not find anything better, which in '
                'Vega means most people.\n\n'
                'The shielded surface habitats on Bleach are among the worst living conditions '
                'in the inner systems. The shielding is insufficient -- not by design but by '
                'neglect. The radiation exposure is cumulative and the medical care is '
                'minimal. Workers rotate off Bleach when they can afford passage, which '
                'many cannot. The warlords who control the mining operations sell the '
                'extracted material to whoever is buying -- pirate ships that need hull '
                'patches, traders passing through, and occasionally Polaran buyers whose '
                'credits are good and whose questions are few. The material that comes out '
                'of Bleach is crude -- poorly refined, inconsistently graded -- but it is '
                'cheap, and in Vega, cheap is the only specification that matters.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Scald',
            short_description='A hot, arid world ruled by a shifting patchwork of warlords -- the closest thing Vega has to a populated centre.',
            long_description=(
                'Scald is the second planet and the most populated world in the system -- a '
                'hot, arid planet with a thin but breathable atmosphere and surface '
                'temperatures that range from merely uncomfortable to genuinely dangerous '
                'depending on latitude and season. The planet is habitable in the way that a '
                'building with a leaking roof is habitable: it keeps you alive, but it does '
                'not keep you comfortable.\n\n'
                'Three billion people live on Scald, and the vast majority of them are poor. '
                'The settlements are sprawling, improvised, and ugly -- prefabricated '
                'structures, repurposed cargo containers, and locally built shelters '
                'clustered around water sources and landing pads. There is no unified '
                'government. The territory is divided among a shifting constellation of '
                'warlords who control regions ranging from a single settlement to a '
                'significant fraction of a continent. The borders change constantly. The '
                'warlords rise, consolidate, overreach, and fall with a regularity that the '
                'population has learned to endure rather than resist. Resistance requires '
                'organisation, and organisation requires stability, and Scald has neither.\n\n'
                'The economy is subsistence supplemented by piracy. The legitimate industries '
                '-- agriculture in the cooler regions, manufacturing in the settlements that '
                'have maintained working factories -- are taxed by whichever warlord '
                'currently controls the territory, and the tax rates are whatever the warlord '
                'decides they are. The piracy economy is more equitable in a grim way: a '
                'successful raid brings goods and money into the settlement, and the crew '
                'spends it locally because there is nowhere else to spend it. The bars and '
                'markets of Scald\'s larger settlements are where pirate crews recruit, '
                'where stolen cargo is fenced, and where the information that Polaran '
                'intelligence quietly makes available finds its way to the people who will '
                'use it.\n\n'
                'Most people on Scald do not want to be pirates. Most people on Scald want '
                'to leave. Interstellar passage costs more than a labourer on Scald can earn '
                'in years, and the jump points out of Vega are controlled by people who '
                'charge for access. The population is trapped -- not by walls or laws but by '
                'poverty, which is a more effective prison than either. The children born on '
                'Scald grow up knowing that the galaxy contains worlds where people live in '
                'comfort and safety, and that the distance between Scald and those worlds is '
                'measured not in light-years but in credits they do not have.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Dustbowl',
            short_description='A cold, marginal world where the less violent warlords have carved out a threadbare but functional society.',
            long_description=(
                'Dustbowl orbits further out than Scald -- a cold, rocky world with thin air '
                'and dust plains that stretch from horizon to horizon. The planet is '
                'marginal for habitation, but in Vega, marginal is often preferable to '
                'central, because the warlords who control the more valuable territories '
                'fight harder and more often. Dustbowl\'s warlords are a different breed: '
                'less violent, more administrative, controlling territory that is not worth '
                'fighting over but is worth managing. The distinction is not moral -- they '
                'are still warlords -- but the quality of life under a warlord who manages '
                'rather than plunders is measurably better.\n\n'
                'The settlements on Dustbowl are enclosed habitats -- the atmosphere is too '
                'thin for comfortable outdoor activity -- and they have the look of places '
                'that have been maintained rather than merely occupied. The population is '
                'smaller than Scald\'s and more stable. Families live here. Businesses '
                'operate with something resembling continuity. The schools teach. The '
                'medical facilities function, though the equipment is old and the supplies '
                'are inconsistent. Dustbowl is not comfortable by any inner-system standard, '
                'but it is the closest thing Vega has to normal life.\n\n'
                'Dustbowl is also where the system\'s repair industry is concentrated. '
                'Pirate ships that return from raids damaged -- and they frequently return '
                'damaged -- come to Dustbowl\'s yards for repair. The yards are not the '
                'gleaming facilities of Tau Ceti or even the improvised docks of Procyon. '
                'They are open patches of ground with scaffolding, surrounded by salvage '
                'piles, staffed by mechanics who can fix anything if you give them enough '
                'time and do not ask where the replacement parts came from. The mechanics '
                'of Dustbowl are some of the most resourceful engineers in the galaxy. They '
                'have to be. Nothing they work with was designed to work together.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='The Shallows',
            short_description='An inner asteroid field -- pirate anchorages hidden among the rocks, invisible to any sensors that might be watching.',
            long_description=(
                'The Shallows is an asteroid field in the inner system -- not as dense or as '
                'resource-rich as the debris disks of Tau Ceti or Epsilon Eridani, but dense '
                'enough to hide in, which is what matters. The Shallows is where the pirate '
                'fleets anchor. Ships returning from raids slip into the asteroid field and '
                'cut their engines, drifting among the rocks with minimal emissions until '
                'any pursuit has given up or passed through. The asteroids provide natural '
                'cover against sensors, and the pirate captains who know the Shallows -- '
                'who have memorised the drift patterns and the gaps between the larger '
                'bodies -- can navigate through it far faster than any pursuing ship that '
                'does not.\n\n'
                'The larger asteroids host improvised anchorages -- hollowed-out cavities '
                'with docking clamps, air supplies, and the bare minimum of habitability. '
                'Crews camp in the anchorages between raids, maintaining their ships, '
                'dividing spoils, and planning the next operation. The anchorages are not '
                'permanent -- they move, they are abandoned, new ones are carved out as old '
                'ones are discovered or become unsafe. The Shallows is a living network of '
                'temporary shelters that has been continuously occupied and continuously '
                'shifting for centuries.\n\n'
                'The population is impossible to count accurately. At any given time, the '
                'Shallows hosts thousands of ships and tens of millions of people. During '
                'peak raiding seasons -- when the jump point alignments favour quick strikes '
                'into inner-system routes -- the Shallows fills. During quiet periods, it '
                'empties. The asteroids do not care. They drift, as they always have, '
                'providing cover to anyone who needs it and asking nothing in return.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Char',
            short_description='A volcanic moon where the most powerful warlord in the system maintains a fortress and controls the best jump point access.',
            long_description=(
                'Char is a volcanic moon orbiting Vega\'s single gas giant -- a geologically '
                'active body wracked by tidal forces, its surface a landscape of lava flows, '
                'vents, and basalt plains that shift with the eruption cycle. The moon is '
                'valuable not for its geology but for its position: Char\'s orbit passes '
                'near the jump points that connect Vega to Altair and the other inner-system '
                'targets. Whoever controls Char controls access to the richest raiding '
                'routes.\n\n'
                'The current controller is the closest thing Vega has to a supreme authority '
                '-- a warlord whose power derives not from territory or population but from '
                'the ability to grant or deny access to the jump points. Ships that want to '
                'raid the inner systems pay a cut to transit through Char\'s controlled space. '
                'Ships that refuse are denied passage, attacked, or simply reported to MERIT '
                'patrols on the other side -- the warlord\'s leverage works in both '
                'directions. This arrangement has persisted through multiple changes of '
                'leadership on Char, because whoever takes control inherits the same '
                'strategic logic.\n\n'
                'The fortress on Char is built into the basalt -- hardened against the '
                'volcanic activity and fortified against the rivals who would take it if '
                'they could. The installation is crude by inner-system standards but '
                'formidable by Vega\'s. It is the one place in the system with something '
                'resembling organised defence, because the jump point revenue justifies the '
                'investment. The warlord of Char is the person the Polaran intelligence '
                'services deal with most directly -- not openly, never openly, but the '
                'information on MERIT fleet movements and merchant schedules that Polaris '
                'makes available tends to arrive on Char first and trickle outward from '
                'there. The warlord takes a cut of that too.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Heimdall',
            short_description='Vega\'s only gas giant -- unexceptional, but its moons control the jump point approaches that make the system valuable.',
            long_description=(
                'Heimdall is a mid-sized gas giant in the outer system -- unremarkable in '
                'itself, but critical to Vega\'s identity because of its position relative '
                'to the system\'s jump points. The jump links that connect Vega to the inner '
                'systems and to Polaran space cluster near the gas giant\'s orbital path, and '
                'the moons of Heimdall are the natural staging ground for anyone using those '
                'links. Char is the most important moon, but the smaller bodies host '
                'anchorages, supply caches, and the improvised fuel-skimming operations that '
                'harvest hydrogen from Heimdall\'s atmosphere to keep the pirate fleets '
                'fuelled.\n\n'
                'The fuel skimming is dangerous and unregulated. The small ships that '
                'descend into Heimdall\'s atmosphere to scoop hydrogen are often poorly '
                'maintained and inadequately shielded. Losses are common. The fuel they '
                'produce is crude -- unrefined hydrogen that burns dirty and damages engines '
                'over time -- but it is available, and a pirate ship that can fill its tanks '
                'for free at Heimdall does not need to buy fuel elsewhere. The economics '
                'are brutal but clear: risk death in the atmosphere or pay credits you do '
                'not have.'
            ),
            population=0,
        ),
        StellarObject(
            name='Carcass',
            short_description='A frozen outer world where the poorest of the poor scratch out survival -- the bottom of Vega\'s hierarchy.',
            long_description=(
                'Carcass is the outermost planet -- a frozen, dark, airless world that no '
                'one would live on if they had any alternative. The people who live on '
                'Carcass do not have alternatives. They are the system\'s most desperate: '
                'debtors who cannot repay, crews who were abandoned, refugees from warlord '
                'conflicts on Scald who fled to the one place nobody would follow them. The '
                'settlements are subsurface -- cramped tunnels carved into the frozen crust, '
                'heated by geothermal taps and lit by whatever power sources the inhabitants '
                'can maintain.\n\n'
                'Life on Carcass is survival. The population grows food in hydroponic bays '
                'that produce enough to prevent starvation and not a calorie more. The '
                'water is recycled endlessly. The air is recycled endlessly. Everything is '
                'recycled endlessly because nothing new comes to Carcass unless someone '
                'brings it, and nobody brings anything to Carcass unless they are running '
                'from something worse. The warlords of the inner planets ignore Carcass '
                'entirely. There is nothing on Carcass worth taking.\n\n'
                'The people of Carcass have a saying: at least we are free. It is the only '
                'true thing about the place. No warlord controls them. No one taxes them. '
                'No one raids them. No one cares about them at all. They are free in the '
                'way that the forgotten are always free -- absolutely, and to no benefit '
                'whatsoever.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='The Fence',
            short_description='A large asteroid converted into the system\'s primary black market -- where stolen cargo becomes legitimate trade goods.',
            long_description=(
                'The Fence is a single large asteroid in a stable orbit between Scald and '
                'the Shallows -- hollowed out over decades into the closest thing Vega has '
                'to a commercial centre. The Fence is where stolen cargo is sold. Not '
                'fenced in back rooms or through intermediaries -- sold openly, in markets '
                'that operate on the surface and in the excavated interior, to buyers who '
                'arrive from across the system and occasionally from outside it.\n\n'
                'The Fence operates on the principle that possession is ownership. No one '
                'asks where the cargo came from. No one checks serial numbers or manifests. '
                'A container of medical supplies stolen from an Altair-bound freighter sits '
                'next to a crate of Polaran neural interface components that arrived through '
                'channels that no one discusses, and both are priced and sold to whoever '
                'can pay. The prices are low by inner-system standards -- stolen goods sell '
                'at a discount -- but the volume is enormous. The Fence moves more cargo in '
                'a week than most legitimate ports handle in a month, and the profits flow '
                'to the warlords who control the docking bays.\n\n'
                'Polaran technology appears on the Fence with a regularity that is not '
                'coincidental. Neural interface components, VR equipment, ship systems '
                'designed for Polaran neural piloting -- all of it available for purchase, '
                'none of it officially exported by the Polaran government, all of it '
                'arriving through supply chains that are deliberately opaque. The Polaran '
                'government does not arm the pirates of Vega. The Polaran government merely '
                'ensures that the means to arm themselves are available at reasonable prices '
                'in a convenient location. The distinction is maintained with the careful '
                'precision of people who understand deniability.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='A lawless pirate system -- warlord-ruled, Polaran-influenced, and a persistent thorn in MERIT\'s side.',
    long_description=(
        'Vega is the system MERIT would most like to control and least wants to pay '
        'the cost of controlling. Twenty-five light-years from Sol, connected to the '
        'inner systems by jump points that are moderate to hard -- passable '
        'by nimble ships with good pilots, impassable by the capital ships that project '
        'real military authority -- Vega has been beyond effective MERIT governance '
        'since the outer systems declared independence. What filled the vacuum was not '
        'another government but the absence of government: warlords, piracy, and the '
        'brutal economics of a system where might makes right and poverty is the '
        'default condition.\n\n'
        'Seven and a half billion people live in Vega, and the vast majority of them '
        'are poor. The settlements on Scald and Dustbowl are improvised, undermaintained, '
        'and governed by whoever has the most guns in the immediate vicinity. There is no '
        'unified system government. There are no space stations -- those require the kind '
        'of stable governance and long-term investment that Vega cannot sustain. The '
        'territory is divided among warlords who rise and fall with a regularity that '
        'the population has learned to endure. The economy is subsistence supplemented '
        'by piracy: raiding ships stage from the Shallows, strike into the inner '
        'systems through the jump points that connect Vega to targets like Altair, and '
        'return with stolen cargo that is sold openly on the Fence.\n\n'
        'Polaris makes this possible. The Polaran government does not arm the pirates '
        'of Vega -- not directly, not provably. What Polaris does is ensure that '
        'information on MERIT fleet movements and merchant schedules is available in '
        'Vega through channels that cannot be traced, and that Polaran technology -- '
        'neural interface components, ship systems, electronics -- is sold on the '
        'black market at prices the warlords can afford. The Polaran government stirs '
        'rebellion in the inner systems because rebellion in the inner systems keeps '
        'MERIT occupied, and MERIT occupied is MERIT not threatening Polaris. Vega is '
        'a tool, and the seven and a half billion people who live there are the cost '
        'of using it.\n\n'
        'Most people in Vega do not want to be there. Leaving requires money for '
        'passage through jump points controlled by warlords who charge for access, on '
        'ships that may or may not be safe, to systems where an arrival from Vega is '
        'treated with suspicion. The poor stay because the poor always stay. The '
        'children grow up knowing that other worlds exist where people live in safety '
        'and comfort, and that the distance between Vega and those worlds is measured '
        'in credits they do not have. MERIT\'s official position is that the people of '
        'Vega are victims of circumstance who deserve better. MERIT\'s actual position '
        'is that Vega is not worth the cost of liberation. The people of Vega are '
        'aware of both positions and believe neither.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

CAPH = System(
    name='Caph',
    star='Pulsating yellow-white subgiant (F2III, Delta Scuti variable), approximately 28 times Sol luminosity, visibly brightens and dims over a period of hours',
    population=18_000_000_000,
    distance_to_sol=54.7,
    stellar_objects=[
        StellarObject(
            name='Vigil',
            short_description='A hot inner world of solar collection and mineral extraction -- named during the isolation for the vigil the colonists kept for rescue.',
            long_description=(
                'Vigil is the innermost planet -- a small, dense, airless world close to the '
                'pulsating star, its surface bathed in light that brightens and dims on a '
                'cycle of hours. The planet was named during the isolation, when the first '
                'generation of colonists maintained a watch on the jump point for ships from '
                'Sol that never came. The name stuck long after the vigil ended.\n\n'
                'Today, Vigil hosts solar collection arrays and mineral extraction operations '
                'that feed the system\'s industry. The pulsating star complicates solar '
                'collection -- the energy output fluctuates with the stellar cycle, and the '
                'collection systems must adjust continuously rather than operating at steady '
                'state. The engineers who maintain the arrays have developed techniques for '
                'managing variable input that are unique to Caph, and the expertise has '
                'become an export -- energy engineers trained on Vigil are valued in other '
                'systems for their ability to handle irregular power sources. Vigil\'s '
                'population is small and technical, living in shielded habitats that pulse '
                'with the star\'s rhythm. The lighting inside the habitats is kept steady, '
                'but the old hands say they can feel the cycle anyway.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Covenant',
            short_description='The capital world of Caph -- eighteen billion people on a world whose culture still carries the fingerprints of generations of isolation.',
            long_description=(
                'Covenant is the world the original colonists landed on, and it is the world '
                'that kept humanity alive in Caph when the rest of the species forgot they '
                'were here. The planet is habitable -- warm, with a thick atmosphere, broad '
                'oceans, and extensive arable land -- and the colonists recognised from the '
                'first surveys that they had been lucky. Many colony worlds require '
                'centuries of terraforming or the permanent compromise of enclosed habitats. '
                'Covenant was liveable from the day they landed. This luck is central to the '
                'system\'s history: if the colonists had landed on a marginal world, the '
                'isolation would have killed them. Instead, it made them.\n\n'
                'The generations of isolation were not a dark age. The colonists had arrived '
                'with a full complement of technical knowledge, manufacturing capability, '
                'and the desperate motivation of people who knew that no resupply was '
                'coming. They built. They farmed. They industrialised. They established '
                'universities, hospitals, and manufacturing centres within the first century '
                'of isolation. By the time Sol\'s explorers returned -- expecting to find '
                'either ruins or primitives -- Covenant had a population in the hundreds of '
                'millions, a functioning industrial economy, and a civilisation that was '
                'entirely self-sufficient and quietly proud of it. The Sol expedition\'s '
                'reports expressed undisguised surprise. The people of Covenant expressed '
                'undisguised irritation at the surprise.\n\n'
                'Today, Covenant is home to ten billion people and is one of the most '
                'developed worlds outside Sol. The cities are old by colonial standards -- '
                'some predate reconnection, built during the isolation with materials and '
                'techniques that the colonists developed independently. The architecture of '
                'the isolation era is distinctive: practical, elegant, and different from '
                'anything built in the inner systems. It has been preserved in the older '
                'city centres, and visitors from Sol find it striking -- familiar enough to '
                'be recognisably human, different enough to feel like another civilisation.\n\n'
                'The religion lingers. MERIT\'s objection to the faith of the isolation was '
                'never theological -- MERIT has no opinion on theology. MERIT\'s objection '
                'was operational: a pilot who refused to take a jump until the ship was '
                'spiritually cleansed caused delays. A crew that insisted on purification '
                'rituals before transit cost hours that became days across a logistics '
                'network of millions of movements. MERIT suppressed the practices that '
                'affected productivity and ignored the ones that did not, which had the '
                'effect of stripping the religion of its most visible expressions while '
                'leaving the private beliefs intact. The faith did not die. It went quiet.\n\n'
                'On Covenant today, the old religion is officially defunct. Unofficially, it '
                'is practised in private by a minority that is larger than anyone admits. '
                'More pervasively, the culture carries habits that descend from the faith '
                'without anyone thinking of them as religious. Caph pilots pause before '
                'initiating a jump -- a moment of stillness that they describe as '
                'concentration but that their grandparents would have called prayer. '
                'Families mark the anniversary of the original colonists\' arrival with a '
                'meal that follows a specific format -- they call it tradition, not ritual. '
                'The pulsing of the star, which the religion interpreted as the heartbeat '
                'of a living cosmos, is still described by Caph residents in language that '
                'carries echoes of the old teachings: the star breathes, the star sleeps, '
                'the star wakes. These are figures of speech. They are also, for some '
                'people, something more.'
            ),
            population=10_000_000_000,
        ),
        StellarObject(
            name='Providence',
            short_description='The second habitable world -- colonised after reconnection but shaped by Caph\'s independent culture rather than MERIT\'s planning.',
            long_description=(
                'Providence is the second habitable world in the system -- a cooler, '
                'smaller planet further from the star with a breathable atmosphere and '
                'extensive temperate zones. The planet was known during the isolation but '
                'not colonised -- the original colony ships had landed on Covenant, and the '
                'population did not have the resources to establish a second colony while '
                'building their civilisation from scratch. Providence was settled after '
                'reconnection, when the population boom of renewed trade and immigration '
                'created demand for more space.\n\n'
                'The colonisation of Providence was conducted by the people of Caph rather '
                'than by MERIT, and the difference is visible. Where MERIT-planned worlds '
                'like Altair\'s Concord are orderly and intentional, Providence was settled '
                'by a population that had spent generations building without external '
                'guidance and preferred to continue doing so. The cities grew organically. '
                'The infrastructure was built to local standards that predate MERIT\'s '
                'involvement. The result is a world that feels like Covenant\'s younger '
                'sibling -- the same architectural sensibility, the same cultural '
                'independence, adapted to a different planet.\n\n'
                'Providence is where the old religion is strongest. The planet was settled '
                'by Caph natives rather than immigrants from Sol, and the cultural '
                'continuity is more intact. The private practice of the faith is more '
                'common here than on Covenant, where the MERIT administrative presence is '
                'heavier. Communities in Providence\'s rural regions observe the old rituals '
                'with a degree of openness that would be uncomfortable in Covenant\'s '
                'cities. MERIT\'s enforcement is lighter on Providence -- the population '
                'is smaller, the settlements more dispersed, and the logistics impact of '
                'the religious practices is minimal in communities that are largely '
                'agricultural. MERIT picks its battles. Providence is not a battle worth '
                'fighting.'
            ),
            population=4_500_000_000,
        ),
        StellarObject(
            name='Remnant',
            short_description='The graveyard orbit where the original colony ships were parked -- preserved as monuments and pilgrimage sites.',
            long_description=(
                'The original colony ships that brought humanity to Caph were not scrapped. '
                'When the colonists no longer needed them -- when Covenant\'s surface '
                'industry could produce everything the ships had provided -- the vessels '
                'were moved to a stable orbit and preserved. During the isolation, the '
                'ships became sacred objects in the emerging religion. They were the vessels '
                'that had passed through the jump point and been found worthy. They were '
                'proof that humanity could cross between stars if the crossing was deserved. '
                'The religion taught that the colony ships carried a blessing that the '
                'subsequent ships -- the ones that tried and failed to follow -- did not.\n\n'
                'After reconnection and MERIT\'s arrival, the ships were reclassified as '
                'historical monuments. The religious significance was officially scrubbed -- '
                'the plaques were rewritten, the interpretive materials updated, the '
                'language changed from sacred to historical. The ships are now presented as '
                'examples of early colonial engineering and the resilience of the human '
                'spirit. This is true. It is also incomplete.\n\n'
                'The ships still receive visitors who come for reasons they do not state on '
                'the visitor logs. Families who practise the old faith bring their children '
                'to the colony ships the way that religious families in any culture bring '
                'their children to sacred sites. They touch the hulls. They stand in the '
                'corridors where the original colonists walked. They do not explain what '
                'they are doing to the MERIT-employed guides, who do not ask. The guides '
                'are from Caph. They understand.'
            ),
            population=5_000,
        ),
        StellarObject(
            name='Rampart',
            short_description='A large gas giant whose moons host the system\'s fuel processing, military garrison, and the isolation-era deep space observatory.',
            long_description=(
                'Bastion is a large gas giant in the outer system -- the gravitational '
                'anchor of Caph\'s outer orbital space. Its moons host fuel processing '
                'operations, the system\'s MERIT military garrison, and a deep-space '
                'observatory that dates to the isolation era. The observatory was originally '
                'built to watch for ships from Sol -- a technological extension of the vigil '
                'that gave the inner planet its name. During the isolation, the observatory '
                'watched for decades and saw nothing. After reconnection, it was repurposed '
                'for conventional astronomical research, but the original watching chamber '
                'is preserved, its instruments still pointed toward Sol.\n\n'
                'The military garrison is modest -- Caph is far enough from the contested '
                'borders that the threats are minimal, and the jump point to Sol is hard '
                'enough that projecting force through it in either direction is difficult. '
                'The garrison exists because MERIT maintains garrisons everywhere, and '
                'because the people of Caph -- with their cultural memory of isolation -- '
                'find the presence of a connection to Sol reassuring in a way they would '
                'not articulate but would notice if it were withdrawn.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Ashpoint',
            short_description='A cold, volcanic world in an eccentric orbit -- mined during the isolation out of necessity, maintained now out of tradition.',
            long_description=(
                'Ashpoint is a cold, geologically active world in an eccentric orbit that '
                'takes it from the outer edge of the habitable zone to well beyond it over '
                'the course of its long year. The planet was mined during the isolation -- '
                'not because it was convenient but because the colonists needed materials '
                'that Covenant\'s crust did not provide, and Ashpoint was the only other '
                'accessible source. The mining operations were established at enormous cost '
                'in the early decades of isolation and became a point of pride: proof that '
                'the colonists could reach beyond their single world and survive.\n\n'
                'After reconnection, the mining operations on Ashpoint became economically '
                'redundant -- the same materials could be imported more cheaply from other '
                'systems. But the operations were not shut down. The people of Caph '
                'maintained them, at a modest scale, as a cultural commitment. Ashpoint is '
                'not profitable. It is meaningful. The isolation taught the people of Caph '
                'that self-sufficiency is not a preference but a survival trait, and '
                'Ashpoint is the embodiment of that lesson. The miners who work there are '
                'aware that their output is unnecessary. They mine anyway. Independence, '
                'they say, is a muscle. Use it or lose it.\n\n'
                'Ashpoint is also where the old religion maintained its strongest foothold '
                'in the decades after reconnection. The mining communities were remote, '
                'isolated, and resistant to MERIT\'s cultural pressure. The faith retreated '
                'to Ashpoint the way that old religions have always retreated to remote '
                'places when the centres of power turned against them. Today, the mining '
                'communities on Ashpoint are small and ageing, and the faith there is '
                'practised openly in a way that would not be tolerated on Covenant. MERIT '
                'is aware. MERIT has decided that a few thousand elderly miners praying '
                'before a shift on an unprofitable rock do not constitute a threat to '
                'operational efficiency.'
            ),
            population=25_000_000,
        ),
        StellarObject(
            name='Crossroads',
            short_description='Caph\'s primary orbital port -- where the system\'s independent streak meets MERIT\'s logistics network.',
            long_description=(
                'Crossroads is Caph\'s main orbital port -- a large station in high orbit '
                'above Covenant that handles interstellar traffic, inter-planetary transit, '
                'and the commerce of a system with eighteen billion people. The station is '
                'jointly operated by the Caph planetary government and MERIT, and the '
                'arrangement is a microcosm of the system\'s relationship with the inner '
                'systems: cooperative, functional, and underlaid with a tension that neither '
                'side acknowledges openly.\n\n'
                'Caph\'s planetary government predates MERIT\'s involvement -- it was '
                'established during the isolation and has governed continuously since. MERIT '
                'did not replace it. MERIT does not replace functional governments. MERIT '
                'integrated it, which in practice means that the Caph government handles '
                'local affairs and MERIT handles interstellar logistics, defence, and the '
                'enforcement of regulations that the Caph government finds alternately '
                'reasonable and intrusive. Crossroads is where the friction is most visible '
                '-- MERIT customs inspectors checking cargo alongside Caph port authority '
                'staff, MERIT transit regulations applied to ships that the Caph government '
                'considers their own business.\n\n'
                'The old religion surfaces at Crossroads in small ways. Pilots from Caph '
                'pause before jumping. Some touch the bulkhead of their ship as they '
                'approach the jump point -- a gesture so quick and so habitual that it '
                'looks like nothing. The MERIT customs inspectors, if they are new, '
                'sometimes ask about these habits. The Caph port authority staff tell them '
                'it is a local custom and leave it at that. The inspectors, if they are '
                'wise, do not press the point.'
            ),
            population=230_000_000,
        ),
    ],
    short_description='A system shaped by generations of isolation -- self-sufficient, quietly devout, and carrying habits its people no longer call religion.',
    long_description=(
        'Caph was lost and found. In the early decades of interstellar travel, a wave '
        'of colony ships transited the hard jump point from Sol to Caph and established '
        'a colony on the habitable world of Covenant. Then the jump point -- unstable, '
        'poorly understood by the primitive jump drive technology of the era -- became '
        'impassable. Subsequent ships from Sol could not make the transit. Ships from '
        'Caph could not return. The colony was cut off from the rest of humanity for '
        'generations.\n\n'
        'The colonists did not die. They did not collapse into savagery. They built a '
        'civilisation. Covenant was habitable and resource-rich, and the colonists had '
        'arrived with technical knowledge and manufacturing capability. Within a century '
        'of isolation they had a functioning industrial economy, universities, and a '
        'population in the hundreds of millions. When jump drive technology eventually '
        'advanced enough to reopen the hard point to Caph, the explorers from Sol '
        'expected to find ruins or remnants. They found a thriving, self-sufficient '
        'civilisation that was surprised to see them and mildly offended by their '
        'surprise.\n\n'
        'During the isolation, the people of Caph developed a religion. The faith held '
        'that jump points were spiritual tests -- that passage between stars was granted '
        'to those who were spiritually pure and denied to those who were not. The '
        'closing of the jump point was interpreted as a judgement: humanity had been '
        'found unready, and the stars had been sealed until worthiness was proven. The '
        'religion shaped every aspect of Caph\'s isolated culture -- governance, social '
        'structure, the interpretation of the pulsating star as a living heartbeat of '
        'a cosmos that was watching and waiting.\n\n'
        'Reconnection undermined the faith. The return of ships from Sol proved that '
        'the jump point\'s closure had been technological, not spiritual. MERIT\'s '
        'subsequent integration of Caph into the inner systems completed the process '
        '-- not through persecution but through the blunt instrument of efficiency. '
        'MERIT did not care what the people of Caph believed. MERIT cared that ships '
        'departed on schedule, that jump transits were not delayed by purification '
        'rituals, and that logistics networks ran without interruption. The practices '
        'that affected productivity were suppressed. The private beliefs were ignored. '
        'The religion did not die. It went underground.\n\n'
        'Today, eighteen billion people live in Caph -- a population and level of '
        'development that exceeds most inner systems. The system is prosperous, '
        'well-run, and carries the quiet confidence of a civilisation that survived '
        'isolation and built itself without help. The old religion is officially '
        'extinct. Unofficially, it is practised in private by more people than anyone '
        'will acknowledge. More broadly, the culture is saturated with habits that '
        'descend from the faith without being recognised as such: the pause before a '
        'jump, the touch on the bulkhead, the language that describes the pulsating '
        'star as breathing and sleeping and waking. These are customs. They are '
        'traditions. They are, for some people, the remnants of a faith that the stars '
        'are alive and watching, and that the passage between them must be deserved.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

FOMALHAUT = System(
    name='Fomalhaut',
    star='Triple system: Fomalhaut A (A3V blue-white, 16 times Sol luminosity), with distant companions Fomalhaut B (K4V orange dwarf) and Fomalhaut C (M4V red dwarf)',
    population=2_800_000_000,
    distance_to_sol=25.1,
    stellar_objects=[
        StellarObject(
            name='The Scar',
            short_description='The point of impact -- where two planet-sized bodies collided and turned the system into a haze of dust and debris.',
            long_description=(
                'Something collided in Fomalhaut. The exact timing is debated -- geological '
                'analysis of the debris places it within the last few hundred million years, '
                'which is recent enough that the system has not had time to settle. Two '
                'planet-sized bodies, each large enough to have been habitable in another '
                'life, struck each other at orbital velocities and ceased to exist as '
                'anything recognisable. What they became is the defining feature of the '
                'system: an enormous, expanding cloud of dust, rock, and pulverised '
                'planetary material that has spread through the orbital space and choked '
                'the system in haze.\n\n'
                'The Scar is what the locals call the densest region of the debris field -- '
                'the approximate point of impact, still denser than the surrounding space '
                'centuries after the collision. The material here ranges from fine dust that '
                'hangs in space like fog to chunks of rock the size of buildings, all of it '
                'tumbling slowly in the gravitational soup of a system that has not finished '
                'rearranging itself. Navigation through the Scar is inadvisable. Navigation '
                'near the Scar is merely dangerous. Sensors are functionally useless -- the '
                'dust scatters and absorbs sensor returns, creating a permanent fog of war '
                'that extends through most of the inner system. In Fomalhaut, you see what '
                'is directly in front of you and guess at everything else.\n\n'
                'The Scar is uninhabited. It is also the reason the system feels the way it '
                'does -- the haze, the blindness, the sense that the void around you is not '
                'empty but full of things you cannot see. Visitors describe Fomalhaut as '
                'claustrophobic, which should not be possible in open space but somehow is. '
                'The dust is everywhere. It coats hulls. It clogs filters. It drifts through '
                'airlocks when they cycle. The people who live here have stopped noticing. '
                'Everyone else notices immediately.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Shimmers',
            short_description='The inner debris ring -- fine dust and small fragments closest to the star, lit from within by Fomalhaut\'s light into a permanent glow.',
            long_description=(
                'The Shimmers is the innermost of Fomalhaut\'s concentric debris rings -- a '
                'band of fine particulate material orbiting close enough to the star that '
                'the dust is illuminated from within, scattering Fomalhaut A\'s blue-white '
                'light into a diffuse, shimmering glow that is visible from everywhere in '
                'the system. The effect is the one thing about Fomalhaut that everyone '
                'agrees is beautiful: a ring of soft light encircling the star, brighter '
                'than the zodiacal light in Sol but diffuse enough to feel ambient rather '
                'than blinding.\n\n'
                'The Shimmers is too close to the star and too fine-grained for habitation '
                'or meaningful resource extraction. The dust particles are small -- sand '
                'grains and smaller -- and the density is enough to create a visible glow '
                'but not enough to be a collision hazard for ships passing through. Small '
                'craft transit the Shimmers routinely, and pilots describe the experience '
                'as flying through luminous fog. The hull picks up a fine coating of dust '
                'that glitters in the light. Some pilots consider it good luck. Others '
                'consider it a maintenance nuisance. Both are correct.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Haze',
            short_description='The broad middle ring -- the thickest band of debris, where sensors fail and the system\'s settlements cling to the largest rocks.',
            long_description=(
                'The Haze is the broadest and densest of the debris rings -- a wide band of '
                'dust, rock, and collision fragments that occupies the middle orbital space '
                'of the system. This is where the bulk of the collision debris settled, and '
                'it is where the sensor blindness that defines Fomalhaut is most acute. '
                'Inside the Haze, visibility on sensors drops to nearly zero. Passive '
                'sensors detect only what is close. Active sensors scatter uselessly off '
                'the dust and return nothing but noise. Navigation relies on short-range '
                'visual scanning, memorised routes, and the intimate knowledge of local '
                'pilots who have learned the Haze\'s geography the hard way.\n\n'
                'The Haze contains the largest fragments of the collision -- rocks the size '
                'of mountains, some the size of small moons, tumbling slowly through the '
                'debris field. These are the foundations of Fomalhaut\'s settlements. The '
                'largest fragments have been hollowed out or built upon, their surfaces '
                'cluttered with docking clamps, habitat modules, and the improvised '
                'architecture of a civilisation that builds on whatever holds still long '
                'enough. The settlements are not elegant. They are bolted to rocks in a fog '
                'of dust, connected to each other by shuttle routes that only local pilots '
                'can navigate reliably, and lit by the diffuse glow of a star seen through '
                'a permanent haze.\n\n'
                'This is where most of Fomalhaut\'s population lives. The Haze settlements '
                'are the system\'s towns and cities -- rough, crowded, and alive with the '
                'particular energy of a place where the rules are relaxed and the '
                'authorities cannot see very far. The dust is part of daily life. It coats '
                'everything. Residents joke that you can tell a newcomer by how often they '
                'clean their visor.'
            ),
            population=1_400_000_000,
        ),
        StellarObject(
            name='The Strip',
            short_description='The largest settlement in the system -- a hollowed-out planetesimal and the inner systems\' premier destination for vice and indulgence.',
            long_description=(
                'The Strip is the beating heart of Fomalhaut\'s reputation. Built on and '
                'inside the largest single fragment in the Haze -- a planetesimal roughly '
                'two hundred kilometres across that was once part of whatever collided here '
                '-- the Strip is the inner systems\' most notorious destination for '
                'entertainment, indulgence, and the kind of activities that are technically '
                'legal but would attract uncomfortable attention anywhere MERIT is watching '
                'closely. In Fomalhaut, MERIT is not watching closely. The sensors do not '
                'work. The dust sees to that.\n\n'
                'The interior of the Strip is a vast excavated volume -- a cavern kilometres '
                'across, lit by artificial light that shifts through colours designed to '
                'keep the inhabitants awake and spending. The establishments range from '
                'genuinely luxurious casinos and pleasure houses that cater to wealthy '
                'visitors from the inner systems to cheap, crowded bars and gambling dens '
                'that cater to everyone else. The economy runs on entertainment, vice, and '
                'the services that support both: hotels, restaurants, medical clinics that '
                'ask few questions, and the shuttle operators who ferry visitors from the '
                'outer system to the Strip and back.\n\n'
                'The Strip is not lawless. MERIT maintains a nominal presence -- a small '
                'office, a handful of inspectors, and the legal framework that prevents '
                'Fomalhaut from sliding into genuine criminality. The casinos are regulated '
                'enough that the games are not rigged, or at least not provably rigged. The '
                'pleasure houses operate within limits that MERIT considers acceptable, '
                'which is to say that everything is consensual, everything is above a '
                'minimum age, and beyond that MERIT would rather not look too closely. '
                'Narcotics that are restricted in Sol are available on the Strip under '
                'regulations that are technically enforced and practically loose. Debt is '
                'easy to accumulate and hard to escape. The Strip is designed to separate '
                'visitors from their money, and it is very good at its job.\n\n'
                'The permanent residents of the Strip are the people who run the machine: '
                'dealers, bartenders, entertainers, mechanics, cleaners, cooks, and the '
                'administrative staff who keep the lights on and the air circulating. They '
                'live in residential sections behind the glittering facades, in quarters '
                'that are comfortable but not glamorous. They watch the visitors come and '
                'go with the professional detachment of people who have seen every kind of '
                'excess and are no longer impressed by any of it.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='The Drift',
            short_description='The outer debris ring -- thinner, colder, and quieter, where the fragments are larger and the traffic is less.',
            long_description=(
                'The Drift is the outermost of the concentric rings -- a thinner, more '
                'dispersed band of debris further from the star where the material is '
                'larger and the dust is less dense. Sensors work marginally better in the '
                'Drift than in the Haze, though still poorly by the standards of any normal '
                'system. The fragments here are colder, darker, and more widely spaced, '
                'drifting through the outer system in slow orbits that take years to '
                'complete.\n\n'
                'The Drift\'s settlements are smaller and quieter than the Haze\'s -- '
                'communities that chose distance from the Strip\'s noise and the Haze\'s '
                'crowding. The population is a mix of miners who extract material from the '
                'larger fragments, technicians who maintain the system\'s outer '
                'communications relays, and people who simply prefer the quiet. The Drift '
                'has the character of a rural outskirt -- the same system, the same haze, '
                'but slower and less populated. The establishments here are modest: supply '
                'stores, repair shops, and the kind of bars where the locals know each '
                'other and strangers are noticed.\n\n'
                'The Drift is also where the pirates hide. The larger fragments provide '
                'cover, the reduced sensor capability provides anonymity, and the outer '
                'ring\'s proximity to the system\'s jump approaches makes it easy to slip '
                'out, intercept a target, and slip back before anyone can organise a '
                'response. The piracy in Fomalhaut is not the organised, Polaran-backed '
                'industry of Vega -- it is opportunistic, small-scale, and conducted by '
                'crews who live in the Drift and prey on the traffic that the Strip '
                'generates. MERIT periodically sends patrol ships through the Drift to '
                'suppress the worst of it, but the patrols are as sensor-blind as everyone '
                'else, and the pirates know the rocks better than any visiting crew.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='The Rim',
            short_description='The sharp outer edge of the debris system -- where the haze ends and clear space begins, marked by the system\'s outermost settlements.',
            long_description=(
                'The Rim is the outer boundary of Fomalhaut\'s debris system -- the sharp '
                'edge where the dust and fragments thin abruptly and clear space begins. '
                'The transition is dramatic: ships transiting inward cross from normal, '
                'sensor-clear space into the haze over a distance of a few thousand '
                'kilometres, and the change is visceral. The void goes from clear to cloudy. '
                'The sensors go from functional to useless. The stars disappear behind the '
                'dust. Pilots who transit the Rim for the first time describe it as flying '
                'into a wall of fog.\n\n'
                'The Rim settlements are positioned at the boundary -- the last clear-space '
                'outposts before the haze. They serve as waypoints for incoming traffic: '
                'navigation services that provide updated route information through the '
                'debris, pilot-for-hire services for visitors who do not trust their own '
                'navigation in the Haze, and the supply and refuelling operations that any '
                'transit point requires. The Rim is also where MERIT\'s presence is '
                'strongest -- the customs and inspection operations are based here, at the '
                'boundary where sensors still work, rather than inside the system where they '
                'do not. Ships entering Fomalhaut are logged at the Rim. Ships leaving are '
                'inspected. What happens between arrival and departure is, for the most '
                'part, Fomalhaut\'s business.\n\n'
                'The Rim settlements also cater to visitors who want the Fomalhaut '
                'experience without actually entering the haze. The establishments here are '
                'tamer than the Strip\'s -- cleaner, better regulated, and with the slightly '
                'artificial feel of a tourist destination designed for people who want '
                'controlled adventure. The view inward from the Rim is striking: the debris '
                'system glows faintly with scattered starlight, a luminous wall of haze that '
                'hides everything within it. Visitors stand at observation windows and peer '
                'into the fog. The fog does not reveal what is inside. That is the point.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Edgeworth',
            short_description='A large fragment in the Haze that has become the system\'s closest thing to a respectable settlement -- where families live and businesses operate.',
            long_description=(
                'Edgeworth is a large collision fragment in the Haze -- roughly eighty '
                'kilometres across, dense enough to have meaningful gravity, and stable '
                'enough in its orbit that building on it is a reasonable investment. '
                'Edgeworth is what passes for the respectable neighbourhood in Fomalhaut. '
                'The settlement is enclosed, well-maintained by local standards, and home '
                'to the families, schools, and businesses that exist because even a system '
                'built on vice needs people who fix the plumbing and teach the children.\n\n'
                'Edgeworth\'s economy is services -- the legitimate support infrastructure '
                'that keeps the Strip and the Haze settlements running. The medical '
                'facilities here are the system\'s best, catering both to residents and to '
                'Strip visitors who overindulge and need professional attention. The legal '
                'services here handle the contract disputes, debt negotiations, and '
                'occasional criminal cases that the Strip generates. The engineering firms '
                'here maintain the habitat systems that keep everyone breathing.\n\n'
                'Edgeworth residents have a complicated relationship with the Strip and the '
                'reputation it gives their system. They are proud of what they have built -- '
                'a functioning community in a debris field, which is no small achievement. '
                'They are less proud of the reason most outsiders have heard of Fomalhaut. '
                'When visitors ask what it is like to live here, the standard answer is that '
                'Fomalhaut is a normal place where normal people live normal lives. This is '
                'true. It is also the answer of people who are tired of being associated '
                'with the casino down the road.'
            ),
            population=150_000_000,
        ),
    ],
    short_description='A dust-choked system built in the debris of a planetary collision -- sensor-blind, seedy, and the inner systems\' capital of vice.',
    long_description=(
        'Something catastrophic happened in Fomalhaut. At some point in the system\'s '
        'recent geological history (though well before the age of humans), two planet-sized bodies collided at orbital '
        'velocities and obliterated each other. The debris from this collision -- dust, '
        'rock, fragments ranging from sand grains to small moons -- spread through the '
        'system\'s orbital space and never fully settled. Fomalhaut today is a system of '
        'concentric debris rings: the Shimmers close to the star, the thick Haze in the '
        'middle, and the thinner Drift on the outer edge, all bounded by the sharp '
        'transition of the Rim where the dust ends and clear space begins.\n\n'
        'The debris defines everything. Sensors are functionally useless inside the '
        'rings -- the dust scatters returns, absorbs signals, and creates a permanent '
        'fog of war that makes the system feel claustrophobic even in open space. '
        'Navigation relies on local knowledge, memorised routes, and short-range visual '
        'scanning. Large and capital ships do not operate in Fomalhaut -- the debris '
        'hazard and the navigation requirements make anything above medium-class '
        'impractical. The system is the domain of small and nimble craft piloted by '
        'people who know the rocks.\n\n'
        'Two point eight billion people live in Fomalhaut, in settlements bolted to '
        'the largest collision fragments scattered through the rings. The system\'s '
        'reputation is earned: Fomalhaut is the inner systems\' capital of vice. The '
        'Strip -- a hollowed-out planetesimal in the Haze -- is the largest '
        'entertainment and gambling destination in MERIT space, offering casinos, '
        'pleasure houses, and indulgences that are technically legal but would attract '
        'uncomfortable scrutiny anywhere sensors work properly. Narcotics that are '
        'restricted elsewhere are available under loose regulation. Debt is easy to '
        'accumulate. The Strip is designed to separate visitors from their money, and '
        'the constant flow of traffic from the inner systems ensures it never runs '
        'short of customers.\n\n'
        'MERIT maintains a nominal presence -- customs at the Rim, inspectors on the '
        'Strip, and the legal framework that prevents Fomalhaut from becoming '
        'genuinely lawless. The system is close enough to Sol and MERIT strongholds '
        'that any serious criminality can be addressed with force, and the threat keeps '
        'the worst excesses in check. But inside the Haze, where the sensors do not '
        'work and the dust covers everything, MERIT\'s gaze is soft. This is by tacit '
        'agreement. Every civilisation needs a place where the rules are relaxed, '
        'where people can indulge the appetites that polite society pretends do not '
        'exist. Fomalhaut is that place. The dust hides everything, and everyone -- '
        'including MERIT -- prefers it that way.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

POLLUX = System(
    name='Pollux',
    star='Orange giant (K0III), approximately 9 times Sol diameter, 34 times Sol luminosity -- an evolved star casting warm amber light',
    population=8_000_000_000,
    distance_to_sol=33.7,
    stellar_objects=[
        StellarObject(
            name='Aurelius',
            short_description='The capital world -- a warm, golden-lit planet and the inner systems\' premier destination for advanced medical treatment.',
            long_description=(
                'Aurelius is the system\'s primary habitable world -- a warm planet orbiting '
                'the orange giant at a distance that makes the star an enormous amber disc '
                'in the sky, visibly larger than Sol from Earth. The light is golden, warm, '
                'and pervasive -- it gives the planet a quality that visitors describe as '
                'autumnal, as though the entire world exists in a permanent late afternoon. '
                'The effect is coincidentally perfect for a world that has built its '
                'identity around health, recovery, and the careful business of keeping '
                'people alive.\n\n'
                'Pollux\'s medical industry is the largest outside Sol. The planet hosts '
                'hundreds of research hospitals, specialist clinics, rehabilitation centres, '
                'and medical universities that draw patients and practitioners from across '
                'the inner systems. The legitimate medical economy is enormous and '
                'genuinely excellent -- Pollux trains some of the best surgeons, '
                'oncologists, and trauma specialists in MERIT space, and the research '
                'institutions produce advances that benefit the entire inner-system '
                'population. This is real. This is also the cover.\n\n'
                'The black-market reanimation trade operates in the spaces between the '
                'legitimate clinics. The wealthy and powerful of the galaxy -- people who '
                'are ageing, people who are dying, people who have already died and been '
                'preserved in stasis by staff who know the right people -- come to Pollux '
                'for treatment that is not listed in any catalogue. The clinics that '
                'perform the work are disguised as conventional medical facilities: private '
                'hospitals with excellent reputations, exclusive patient lists, and a '
                'discretion that their clients pay dearly for. The procedures use Canopan '
                'reanimation technology smuggled across the border from the Canopus sector, '
                'adapted and refined by Pollux physicians who have spent careers learning '
                'techniques that MERIT officially considers an abomination.\n\n'
                'The results vary with the price, exactly as they do in Canopan space. The '
                'wealthiest clients receive restorations that are close to the Canopan '
                'elite standard -- subtle, careful, nearly whole, with only the faint '
                'uncanny quality that even the best reanimation cannot eliminate. Less '
                'wealthy clients receive lesser work. The very lowest tier of Canopan '
                'reanimation -- the mindless labour reanimation of the poor -- is not '
                'practised on Pollux. The physicians have standards, and the clients have '
                'money. Nobody on Pollux is being reanimated as a worker. Everyone on '
                'Pollux is being reanimated because someone loved them, or because they '
                'loved themselves too much to die.'
            ),
            population=4_500_000_000,
        ),
        StellarObject(
            name='Solace',
            short_description='A cooler, quieter world -- rehabilitation centres, long-term care, and the recovery that follows reanimation.',
            long_description=(
                'Solace is the second habitable world -- further from the star, cooler, with '
                'a thinner atmosphere and extensive temperate forests under the warm orange '
                'light. Where Aurelius is the system\'s working heart -- busy, urban, '
                'commercially energetic -- Solace is where people go to recover. The planet '
                'is quieter, slower, and built around the long-term care that follows '
                'serious medical intervention.\n\n'
                'The legitimate rehabilitation industry is substantial. Patients recovering '
                'from major surgery, trauma, or illness come to Solace for the extended '
                'care programmes that Aurelius\'s busy hospitals cannot provide. The '
                'facilities are set in the forests and along the coasts -- clean, spacious, '
                'and designed for rest. The planet\'s culture is medical in the way that '
                'a spa town\'s culture is medical: everything is oriented toward wellness, '
                'recovery, and the gentle pace that healing requires.\n\n'
                'Solace is also where the reanimated recover -- or try to. Reanimation is '
                'not instantaneous. Even the best restorations require months of '
                'rehabilitation as the restored person relearns motor function, rebuilds '
                'cognitive pathways, and adjusts to the subtle wrongness that every '
                'reanimated person experiences. The exclusive rehabilitation centres on '
                'Solace that cater to reanimation patients are the system\'s worst-kept '
                'secret. Everyone knows they exist. The patients arrive in private shuttles, '
                'stay for months in secluded facilities, and leave as people who are almost '
                'but not quite who they were before. The staff are bound by contracts that '
                'make MERIT security clearances look permissive. The fees are extraordinary. '
                'The alternative is death, and the clients have already decided that death '
                'is unacceptable.'
            ),
            population=1_800_000_000,
        ),
        StellarObject(
            name='Pallor',
            short_description='A cold outer world with underground facilities -- where the bodies arrive and the most sensitive procedures take place far from scrutiny.',
            long_description=(
                'Pallor is a cold, rocky world in the outer habitable zone -- thin air, '
                'frozen plains, and a population that is small enough to avoid the kind of '
                'attention that the inner planets attract. Pallor is where the logistics of '
                'the reanimation trade are handled. The bodies arrive here.\n\n'
                'The dead who are destined for reanimation on Pollux do not arrive on '
                'Aurelius. They arrive on Pallor, in stasis pods aboard ships whose '
                'manifests describe the cargo as medical equipment, biological samples, or '
                'transplant material -- all technically accurate, all deliberately '
                'misleading. The receiving facilities on Pallor are underground, built into '
                'the frozen crust, shielded from orbital observation and far from the '
                'MERIT inspection infrastructure that monitors Aurelius\'s ports. The bodies '
                'are received, assessed, catalogued, and prepared for the procedures that '
                'will be performed in facilities on Pallor itself or transferred to '
                'Aurelius\'s black-market clinics.\n\n'
                'The preparation is critical. Canopan reanimation works best on bodies '
                'that have been properly preserved and prepared -- the window between death '
                'and the point at which restoration becomes impossible is finite, and the '
                'quality of the outcome depends heavily on the condition of the body at '
                'the start. The specialists on Pallor who perform this preparatory work are '
                'among the most skilled mortuary technicians in the galaxy, though they '
                'would not use that word. They call themselves preservation specialists. '
                'Their work is the first step in a process that the clients believe is a '
                'return from death and that the technicians, who see the bodies before and '
                'after, understand is something more complicated.\n\n'
                'MERIT knows about Pallor. MERIT has always known. The question is not '
                'whether MERIT can shut down the receiving facilities -- it could, easily -- '
                'but whether the political cost is worth it. The clients of Pollux\'s '
                'reanimation trade include some of the most powerful people in the inner '
                'systems. Senators, corporate leaders, military officials, and their '
                'families. The trade persists not because MERIT cannot stop it but because '
                'the people who would need to give the order are the same people who might '
                'one day need the service.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='The Corridor',
            short_description='The region of space between Pollux and the Canopus border -- a smuggler\'s highway where Canopan technology enters the inner systems.',
            long_description=(
                'The Corridor is what the locals call the volume of space between Pollux\'s '
                'inhabited inner system and the approaches to the Canopus border. It is not '
                'a place -- it is a route, a practice, and an open secret. Canopan smugglers '
                'bring reanimation technology across the border: neural reconstruction '
                'matrices, tissue regeneration compounds, the proprietary chemical cocktails '
                'that make Canopan reanimation possible. They bring it in ships disguised '
                'as civilian traders, in hidden compartments, in cargo containers labelled '
                'as something innocent.\n\n'
                'The smuggling runs in both directions. Canopan couriers bring the '
                'technology in. Pollux-based operators bring the clients\' bodies out to '
                'Pallor. Credits flow back to Canopan space -- enormous sums that the '
                'Canopan government officially condemns and privately benefits from, because '
                'the money enters their economy regardless of their stated objections. The '
                'Canopan government does not want MERIT to have reanimation technology. The '
                'Canopan government also does not want to lose the revenue that the Pollux '
                'trade generates. The result is enforcement that is aggressive enough to '
                'be visible and porous enough to be profitable.\n\n'
                'MERIT\'s anti-smuggling operations in the Corridor are constant and '
                'largely futile. The patrol ships catch some shipments -- enough to justify '
                'the operations, enough to demonstrate that MERIT takes the prohibition '
                'seriously. They miss many more. The smugglers are experienced, the routes '
                'are numerous, and the financial incentives on both sides of the border are '
                'overwhelming. A single successful delivery of high-grade reanimation '
                'technology is worth more than a smuggler\'s ship. The math is simple. The '
                'smugglers do the math.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Wharf',
            short_description='The system\'s primary orbital port -- where legitimate medical traffic provides cover for everything else.',
            long_description=(
                'Meridian is Pollux\'s main orbital port -- a large installation in high '
                'orbit above Aurelius that handles the system\'s enormous volume of incoming '
                'and outgoing traffic. The traffic is the key to everything. Pollux receives '
                'more medical traffic than any system outside Sol: patients travelling for '
                'treatment, medical professionals attending conferences, pharmaceutical '
                'shipments, research materials, organ transport, tissue samples, biological '
                'specimens. The manifests are complex, the cargo is specialised, and the '
                'volume is so large that inspecting everything is impossible.\n\n'
                'This is what makes the smuggling work. A stasis pod containing a body '
                'destined for reanimation looks identical on a manifest to a stasis pod '
                'containing transplant organs. A container of Canopan neural reconstruction '
                'matrices is indistinguishable from a container of legitimate neural repair '
                'compounds without laboratory analysis that takes days. The legitimate '
                'medical economy generates so much traffic in biological material that the '
                'illegitimate trade disappears into the noise. MERIT\'s customs inspectors '
                'at Meridian are well-trained, well-equipped, and hopelessly outnumbered by '
                'the volume of cargo that passes through.\n\n'
                'Meridian is also where Castor\'s reinforcement fleet would arrive if the '
                'system were ever threatened militarily. The station maintains docking '
                'facilities for warships and the logistics infrastructure to support a '
                'fleet deployment, though these facilities have never been used for their '
                'intended purpose. Pollux\'s military value is as Castor\'s rear area -- a '
                'supply and support system for the fortress next door. The garrison is '
                'small, focused on anti-smuggling rather than defence, and operates with '
                'the weary awareness that their primary mission is one they cannot win.'
            ),
            population=280_000_000,
        ),
        StellarObject(
            name='Vastus',
            short_description='The system\'s large gas giant -- fuel processing and a convenient waypoint for smugglers adjusting their approach vectors.',
            long_description=(
                'Vastus is a large gas giant in the outer system -- roughly two and a half '
                'times Jupiter\'s mass, with a turbulent amber-brown atmosphere lit by the '
                'orange star into hues that are striking but that nobody in Pollux has time '
                'to appreciate. The planet\'s moons host fuel processing operations that '
                'service the system\'s considerable traffic, and Vastus\'s gravitational '
                'well is used routinely by ships adjusting their approach vectors -- a '
                'slingshot around the gas giant is the standard route for ships arriving '
                'from Canopan space that want to approach the inner system from an angle '
                'that does not cross the main MERIT patrol routes.\n\n'
                'MERIT is aware that Vastus is used as a waypoint by smugglers. Patrol '
                'ships are stationed on the relevant moons. The patrols catch some traffic. '
                'They miss more. The gas giant is large, the moon system is complex, and a '
                'small ship with a good pilot can use the gravitational dynamics to mask '
                'its approach in ways that make interception a matter of luck as much as '
                'skill. The patrol crews do their jobs competently and without illusion. '
                'They are fishing in an ocean with a net full of holes, and everyone '
                'involved knows it.'
            ),
            population=85_000_000,
        ),
        StellarObject(
            name='The Alcove',
            short_description='A research installation studying Pollux\'s orange giant at close range -- and quietly developing reanimation techniques beyond Canopan standards.',
            long_description=(
                'The Alcove is an orbital research installation in a close solar orbit -- '
                'officially a stellar physics laboratory studying the orange giant\'s '
                'evolved structure and pulsation characteristics. The research is real and '
                'the science is good. The installation is also, quietly and without official '
                'acknowledgement, home to the most advanced reanimation research outside '
                'Canopan space.\n\n'
                'The physicians and researchers at the Alcove are not merely applying '
                'Canopan techniques -- they are trying to surpass them. The Canopan '
                'reanimation process, even at its best, produces restorations that are '
                'close but never quite right. The Alcove\'s researchers believe the gap can '
                'be closed. Their work combines Canopan technology with inner-system medical '
                'science, attempting to achieve a quality of restoration that Canopus itself '
                'has not reached. The work is slow, expensive, and conducted in absolute '
                'secrecy. The researchers are among the most brilliant medical minds in the '
                'galaxy, and they are all, by MERIT\'s legal standards, criminals.\n\n'
                'The funding comes from the same source that funds everything in Pollux\'s '
                'shadow economy: the clients. The wealthy and powerful who use Pollux\'s '
                'reanimation services have a vested interest in improving the technology, '
                'and they invest accordingly. The Alcove is their bet on a future where '
                'death is not merely reversible but reversible without cost -- where the '
                'uncanny wrongness that haunts even the best Canopan restorations is '
                'finally eliminated. Whether this is possible is an open question. The '
                'researchers believe it is. The dead who fund them certainly hope so.'
            ),
            population=15_000_000,
        ),
    ],
    short_description='Castor\'s twin -- the inner systems\' medical capital and the galaxy\'s worst-kept secret for black-market reanimation.',
    long_description=(
        'Pollux is the other twin of Gemini -- Castor\'s partner, bordering the same '
        'Canopan space but serving an entirely different function. Where Castor is a '
        'fortress bristling with weapons and sensors, Pollux is a medical hub whose '
        'defences are Castor\'s proximity and a garrison focused on catching smugglers '
        'rather than repelling invasions. The system orbits an orange giant -- an '
        'evolved star nine times Sol\'s diameter that hangs enormous and amber in the '
        'sky of Aurelius, casting warm golden light over the inner systems\' premier '
        'destination for advanced medical treatment.\n\n'
        'The legitimate medical industry is real and enormous. Pollux trains surgeons, '
        'conducts research, and treats patients from across MERIT space. The hospitals '
        'are excellent. The universities are respected. The pharmaceutical industry is '
        'a major economic driver. This is all true, and it is also the cover for the '
        'trade that defines the system: black-market reanimation using Canopan '
        'technology smuggled across the border.\n\n'
        'The wealthy and powerful of the inner systems come to Pollux to cheat death. '
        'Their bodies arrive on Pallor in stasis pods labelled as medical cargo. '
        'Canopan reanimation technology arrives through the Corridor in shipments '
        'disguised as pharmaceutical supplies. Pollux physicians trained in techniques '
        'that MERIT officially condemns perform restorations in clinics disguised as '
        'private hospitals. The restored spend months recovering on Solace before '
        'returning to their lives as people who are almost but not quite who they were '
        'before. The trade is illegal, open, and unstoppable -- because the clients '
        'include the same senators, officials, and corporate leaders who would need to '
        'authorise a crackdown.\n\n'
        'Both MERIT and the Canopan government disapprove. MERIT considers reanimation '
        'a violation of human dignity. Canopus does not want its proprietary technology '
        'in MERIT hands. Both enforce their objections with measures that are visible '
        'enough to be credible and porous enough to be profitable. The smugglers run '
        'the Corridor. The customs inspectors catch what they can. The bodies arrive. '
        'The technology arrives. The money flows in both directions, and the dead come '
        'back to something that resembles life under the warm amber light of a star '
        'that has itself aged past its prime and refuses to go quietly.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

DENEBOLA = System(
    name='Denebola',
    star='Blue-white main sequence (A3V), approximately 15 times Sol luminosity, very young system (100-400 million years old)',
    population=1_100_000_000,
    distance_to_sol=35.9,
    stellar_objects=[
        StellarObject(
            name='Lustre',
            short_description='The fashion capital of the galaxy -- where a billion robots produce the garments that a thousand designers dream.',
            long_description=(
                'Lustre is the planet that made Denebola famous. A warm, bright world under '
                'the vivid blue-white light of a young star, Lustre is home to the fashion '
                'houses that dress the galaxy\'s elite. The names are known on every '
                'inhabited world: ateliers that have operated for centuries, producing '
                'garments that are not merely clothing but cultural artefacts -- pieces that '
                'define eras, that mark their wearer as someone who matters, that are '
                'discussed, copied, and counterfeited across the inner and outer systems '
                'alike.\n\n'
                'The human population of Lustre is small and rarefied. Designers, '
                'patternmakers, textile engineers, colourists, and the creative directors '
                'who set the aesthetic vision that the houses follow. These are the people '
                'who decide what the galaxy wears next season, and they take the '
                'responsibility with a seriousness that outsiders find either admirable or '
                'absurd depending on their relationship with fashion. The design process '
                'is human -- MERIT\'s robotic systems can execute any pattern with flawless '
                'precision, but they cannot originate a design that makes someone feel '
                'something. That remains the province of people who have spent their lives '
                'studying fabric, form, and the way light falls on a body.\n\n'
                'The production is robotic. The factories on Lustre are vast, clean, '
                'automated complexes where robotic systems cut, sew, weave, dye, and '
                'finish garments to specifications that human hands could match in quality '
                'but never in volume. A design that a human atelier would produce in a '
                'single piece over weeks is replicated in thousands by the factories in '
                'hours -- though the originals, the pieces touched by human hands, command '
                'prices that the factory copies never approach. The distinction between '
                'handmade and machine-made is the fundamental status marker: the same '
                'design, one touched by a person and one produced by a robot, separated '
                'by a factor of a hundred in price and the entirety of the social hierarchy.\n\n'
                'Lustre\'s cities are beautiful in the way that everything in Denebola is '
                'beautiful -- deliberately, expensively, and with the total commitment of '
                'people for whom aesthetics is not a preference but a profession. The '
                'architecture is designed to complement the light of Denebola\'s young star '
                '-- bright, crisp, and slightly blue, making whites brilliant and colours '
                'vivid. The streets are showrooms. The residents are advertisements. Nobody '
                'on Lustre dresses carelessly. It would be like a chef serving bad food in '
                'their own restaurant.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Facet',
            short_description='The jewel of the system -- where the galaxy\'s finest jewelry is designed, cut, and set by human artists and produced by robotic workshops.',
            long_description=(
                'Facet is Lustre\'s companion in the Denebola luxury economy -- a cooler, '
                'smaller world further from the star where the light is slightly less '
                'intense and the culture is oriented toward a different kind of beauty. '
                'Facet is the jewelry capital of the galaxy. The gemcutters, metalworkers, '
                'and jewelry designers of Facet produce pieces that are worn by the '
                'powerful and coveted by everyone else.\n\n'
                'The raw materials come from across the galaxy -- gemstones from mining '
                'operations in a dozen systems, rare metals from Tau Ceti and the Belt, '
                'exotic compounds from the outer systems that produce colours and optical '
                'effects impossible with conventional materials. Facet imports everything '
                'and exports only finished pieces, each one designed by human artisans '
                'and produced in robotic workshops that can set a stone with a precision '
                'measured in microns. As on Lustre, the distinction between handmade and '
                'machine-made defines the market: a piece set by a master jeweller\'s own '
                'hands is worth a fortune. The identical piece set by a robot is worth '
                'merely a lot.\n\n'
                'The culture on Facet is quieter than Lustre\'s. The fashion world is '
                'public, theatrical, driven by seasons and spectacle. The jewelry world is '
                'more private -- pieces are commissioned rather than collected, designed '
                'for specific clients rather than displayed on runways. The artisans of '
                'Facet work in studios rather than ateliers, and their reputations are '
                'built on word of mouth among the elite rather than public recognition. '
                'The wealthiest people in the galaxy know the name of their jeweller the '
                'way they know the name of their physician. The rest of the galaxy buys '
                'the robotic copies and does not pretend otherwise.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Atelier',
            short_description='The system\'s orbital showroom -- where buyers from across the galaxy come to see, commission, and acquire.',
            long_description=(
                'Atelier is Denebola\'s primary orbital installation -- not merely a port '
                'but a showroom. The station is designed as a destination in itself: a '
                'place where the buyers, collectors, and representatives of the galaxy\'s '
                'wealthy come to see the season\'s collections, commission bespoke pieces, '
                'and conduct the business of luxury in an environment designed to make '
                'spending feel like an aesthetic experience.\n\n'
                'The station\'s interior is redesigned every season by Lustre\'s leading '
                'architects and designers -- the public spaces transformed to reflect '
                'the current aesthetic direction, so that the station itself is a statement '
                'of what Denebola considers beautiful right now. The effect is impressive '
                'and deliberately disorienting: visitors who return after a season away '
                'find a station that looks entirely different, reinforcing the message that '
                'fashion moves and those who do not move with it are left behind.\n\n'
                'Atelier also handles the logistics of export -- the garments, jewelry, '
                'furniture, art, and designed objects that flow from Denebola to the rest '
                'of the galaxy. The packaging is as considered as the product. The shipping '
                'is climate-controlled, shock-protected, and tracked with a precision that '
                'military logistics would envy. A Lustre gown in transit receives better '
                'care than most passengers.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Palette',
            short_description='A small, temperate world devoted to fine art, interior design, and the broader aesthetic industries that orbit Denebola\'s fashion core.',
            long_description=(
                'Palette is the third inhabited world in the system -- a small, temperate '
                'planet with gentle seasons and a landscape of rolling hills and shallow '
                'seas. Where Lustre is fashion and Facet is jewelry, Palette is everything '
                'else: fine art, interior design, furniture, ceramics, glasswork, '
                'perfumery, and the constellation of aesthetic industries that exist '
                'because the galaxy\'s wealthy do not stop at clothing and jewelry when '
                'curating their lives.\n\n'
                'Palette\'s human population is artists, designers, and craftspeople -- '
                'people who work with materials and form in disciplines that range from '
                'traditional sculpture to the design of living spaces for the ultra-rich. '
                'A Palette interior designer is the professional you hire to furnish the '
                'Mars estate. A Palette perfumer creates scents that are worn by a dozen '
                'people and recognised by thousands. A Palette glassblower produces pieces '
                'that are displayed in the galleries of Earth and Sol\'s orbital habitats.\n\n'
                'The robotic production on Palette mirrors the other worlds -- the designs '
                'are human, the volume production is robotic, and the gap between the '
                'original and the copy is where the money lives. But Palette\'s culture is '
                'less commercial than Lustre\'s and less exclusive than Facet\'s. The '
                'artists here are more likely to describe themselves as artists than as '
                'producers of luxury goods, and the distinction matters to them even if the '
                'market treats the output identically. Palette is where Denebola\'s '
                'residents go when they want to feel that what they do is art rather than '
                'commerce. The line between the two has never been clear here, and the '
                'arguments about it are centuries old and nowhere near resolution.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='Foundry',
            short_description='A hot inner world where the system\'s robotic workforce is manufactured, maintained, and recycled.',
            long_description=(
                'Foundry is the world that makes the rest of Denebola possible. A hot, '
                'dense inner planet close to the young star, Foundry is where the robotic '
                'systems that produce the galaxy\'s luxury goods are themselves produced. '
                'The factories here build the robots that cut fabric on Lustre, set stones '
                'on Facet, blow glass on Palette, and perform the thousand other '
                'manufacturing tasks that the human population designs but does not execute. '
                'The robots that wear out or become obsolete are returned to Foundry, '
                'disassembled, and their materials recycled into new units.\n\n'
                'The human population on Foundry is small -- robotics engineers, quality '
                'control specialists, and the logistics staff who manage the flow of units '
                'to the other worlds. Foundry is the least glamorous place in the most '
                'glamorous system in the galaxy, and its residents are aware of the irony. '
                'The people who maintain the machines that produce the galaxy\'s most '
                'beautiful objects work in utilitarian facilities on a hot rock and dress '
                'in practical clothing that would make a Lustre designer wince. They do not '
                'care. They understand the machines, which is a kind of artistry that the '
                'fashion houses do not acknowledge but could not function without.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='The Blinds',
            short_description='An outer asteroid cluster that has become the base for the system\'s other industry -- counterfeiting Denebola\'s luxury goods.',
            long_description=(
                'The Blinds is a cluster of asteroids in the outer system that has developed an '
                'industry Denebola would prefer not to discuss. Where there is luxury, '
                'there are counterfeits, and the asteroids of The Blinds host the workshops that '
                'produce imitation Lustre garments, fake Facet jewelry, and knockoff '
                'Palette designs for a market that vastly outnumbers the clientele who can '
                'afford the genuine article.\n\n'
                'The counterfeit industry exists in a complicated legal and moral space. '
                'The workshops on The Blinds are technically illegal -- MERIT enforces '
                'intellectual property protections that the fashion houses rely on -- but '
                'the enforcement is inconsistent and the workshops are difficult to shut '
                'down permanently. Close one and another opens in a different asteroid. '
                'The counterfeits range from crude imitations that fool nobody to '
                'remarkable reproductions that require expert examination to distinguish '
                'from the genuine article. The best counterfeiters on The Blinds are artisans '
                'in their own right -- people with the skill to produce luxury goods who '
                'lack the connections or pedigree to work in the legitimate houses.\n\n'
                'The fashion houses publicly condemn the counterfeiting and privately '
                'tolerate it, because the counterfeits spread the brand. A person wearing '
                'a fake Lustre gown on Procyon is advertising the real thing on Earth. The '
                'relationship between The Blinds and the legitimate industry is parasitic, '
                'symbiotic, and deeply uncomfortable for everyone involved.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='The galaxy\'s luxury capital -- a small, exclusive system where human designers and robotic factories produce the most prestigious goods in the inner systems.',
    long_description=(
        'Denebola is where the beautiful things come from. A small system orbiting a '
        'young blue-white star, Denebola has a human population of just over a billion '
        '-- a fraction of most inner systems -- and a robotic population many times '
        'that number. The humans design. The robots produce. The result is the galaxy\'s '
        'most prestigious luxury industry: fashion houses on Lustre whose garments '
        'define what the powerful wear, jewellers on Facet whose pieces mark their '
        'owners as people of consequence, and artisans on Palette whose work furnishes '
        'the homes and lives of the ultra-rich across the inner and outer systems.\n\n'
        'The economic model is simple. Human creativity is the scarce resource -- the '
        'thing that cannot be replicated by robotic systems no matter how precise. A '
        'robot can cut a garment to specifications measured in microns. It cannot '
        'decide what the garment should look like, what it should make the wearer feel, '
        'or why this particular shade of blue is right for this season and not last. '
        'The designers of Denebola provide the vision. The robots provide the volume. '
        'The market divides sharply between the handmade originals -- touched by human '
        'hands, worth fortunes, owned by the elite -- and the robotic copies, which '
        'are identical in every measurable way and worth a fraction of the price. The '
        'difference is not quality. The difference is provenance. In the luxury market, '
        'provenance is everything.\n\n'
        'Denebola\'s culture is aesthetic to its core. The cities are designed. The '
        'streets are curated. The residents dress with the care of people for whom '
        'appearance is professional, and the standard of visual presentation extends '
        'from the orbital showroom of Atelier to the factories of Foundry, where even '
        'the utilitarian spaces are laid out with an attention to proportion that most '
        'systems would not bother with. The system is small, exclusive, and aware of '
        'its own importance in a way that visitors find either charming or insufferable '
        'depending on their tolerance for people who care very deeply about the fall '
        'of a hemline.\n\n'
        'The young star\'s light is part of the brand. Denebola\'s blue-white light makes '
        'colours vivid and whites brilliant, and the designers have built their palettes '
        'around it -- Denebola colours are calibrated for Denebola light and look subtly '
        'different under the warmer suns of other systems. This is deliberate. A garment '
        'that looks perfect on Lustre and slightly different on Earth is a garment that '
        'reminds the wearer, with every glance, where it came from.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ARCTURUS = System(
    name='Arcturus',
    star='Ancient orange giant (K1.5III), approximately 25 times Sol diameter, 170 times Sol luminosity -- a Population II star passing through the solar neighbourhood, metal-poor and very old',
    population=3_200_000_000,
    distance_to_sol=36.7,
    stellar_objects=[
        StellarObject(
            name='Crossway',
            short_description='The largest station in the system -- the primary transit hub through which most inner-system traffic passes.',
            long_description=(
                'Crossway is the beating heart of Arcturus and the reason the system matters. '
                'It is the largest space station in the system -- an enormous installation '
                'that processes more transit traffic than most inhabited worlds. Arcturus '
                'sits at a junction in the inner-system jump network: dozens of systems are '
                'most efficiently reached by routing through Arcturus, and the result is a '
                'volume of traffic that is staggering for a system with no planets and no '
                'natural resources. Crossway handles the logistics of this traffic -- the '
                'refuelling, the crew rotations, the cargo transfers, the customs '
                'inspections, and the thousand administrative tasks that keep an '
                'interstellar transit network functioning.\n\n'
                'The station is massive and modular, expanded continuously over centuries as '
                'the traffic grew. The oldest sections date to the early interstellar era '
                'and have the cramped, utilitarian feel of infrastructure built before '
                'anyone knew how important this waypoint would become. The newer sections '
                'are spacious, modern, and designed for volume. The commercial districts '
                'serve a transient population that is always arriving and always leaving -- '
                'restaurants, hotels, entertainment, and the services that people need when '
                'they are between destinations. Crossway is nobody\'s home and everybody\'s '
                'stop.\n\n'
                'The permanent population is the staff that keeps the operation running: '
                'logistics coordinators, customs officers, maintenance crews, and the '
                'commercial operators who feed and house the transient millions. They live '
                'on a station that never sleeps, in a system that produces nothing except '
                'connectivity, sustained entirely by the accident of jump point geography '
                'that placed Arcturus at the crossroads of the inner systems.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='The Garrison Ring',
            short_description='A chain of armed military stations forming MERIT\'s defensive perimeter -- strong enough to hold position, too few to control the system.',
            long_description=(
                'The Garrison Ring is not a single station but a chain of armed military '
                'installations positioned to cover the approaches from Polaris space. Each '
                'station in the Ring is heavily armed -- weapons platforms, missile '
                'batteries, and fighter bays capable of engaging Polaran warships. Together, '
                'the Ring represents a significant concentration of firepower that has '
                'successfully deterred any direct Polaran assault on the system\'s core '
                'infrastructure.\n\n'
                'The problem is the gaps. Arcturus has no planets, no moons, no natural '
                'bodies to anchor a defensive perimeter. The stations are fixed points in '
                'empty space, and between them is nothing -- open void that Polaran ships '
                'can transit with impunity if they avoid the stations\' engagement range. '
                'The Ring can protect the stations. The Ring cannot protect the system. '
                'Polaran scout ships, commerce raiders, and intelligence vessels operate in '
                'Arcturus\'s outer space with a freedom that would be impossible in a system '
                'like Castor, where the complex stellar geography at least provides '
                'chokepoints. Arcturus is open. The Ring is a fence with no walls.\n\n'
                'The military personnel who serve in the Ring develop a particular '
                'psychology: they are well-defended and surrounded. Their stations are '
                'secure but the space between them is not. Polaran ships are visible on '
                'long-range sensors, crossing the system, sometimes close enough to hail, '
                'and there is nothing the Ring can do about it unless the Polarans are '
                'foolish enough to come within engagement range. Most are not. The '
                'frustration is chronic and the standing orders are clear: hold position, '
                'protect the stations, do not pursue into open space where Polaran neural '
                'pilots have the advantage.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='Waymeet',
            short_description='A commercial station serving the inner-system traffic -- Crossway\'s smaller sibling, handling overflow and secondary routes.',
            long_description=(
                'Waymeet is the second major commercial station in the system -- positioned '
                'to serve the secondary transit routes that Crossway\'s capacity cannot '
                'absorb. Where Crossway handles the primary trunk routes between the major '
                'inner systems, Waymeet serves the smaller systems, the less-trafficked '
                'routes, and the independent traders who prefer a station where the customs '
                'inspections are slightly less thorough and the docking fees are lower.\n\n'
                'Waymeet has a rougher character than Crossway -- less corporate, more '
                'independent, with a commercial district that caters to traders rather than '
                'passengers. The bars are louder, the markets more varied, and the '
                'atmosphere is closer to a port town than a transit hub. Waymeet is where '
                'you go to hire a ship, find a crew, or sell cargo that might not pass '
                'Crossway\'s inspections without uncomfortable questions. It is not Vega -- '
                'the law applies and MERIT\'s presence is real -- but it is the loosest '
                'station in a system where the military is focused on the Polaris border '
                'and the customs service is focused on Crossway.\n\n'
                'Polaran goods appear on Waymeet\'s markets with a regularity that surprises '
                'no one. Neural interface components, VR equipment, and Polaran-manufactured '
                'electronics find their way to Waymeet through channels that are technically '
                'smuggling and practically commerce. The proximity to Polaris space makes '
                'the border porous, and Waymeet is where the porosity becomes visible.'
            ),
            population=350_000_000,
        ),
        StellarObject(
            name='Anchorage',
            short_description='A supply depot and repair station -- where ships that have crossed through Arcturus stop to refuel and patch up after border skirmishes.',
            long_description=(
                'Anchorage is the system\'s primary supply and repair station -- a functional '
                'installation that lacks Crossway\'s commercial energy and the Garrison '
                'Ring\'s military tension but is essential to both. Every ship that operates '
                'in Arcturus needs fuel, maintenance, and occasionally emergency repair, and '
                'Anchorage provides all three. The station is a sprawling complex of '
                'docking bays, machine shops, fuel storage, and the warehouses that hold '
                'the supplies imported from the rest of MERIT space that keep the entire '
                'system running.\n\n'
                'Arcturus produces nothing. Every consumable -- food, water, atmospheric '
                'gases, medical supplies, ammunition, spare parts, construction material -- '
                'is imported. Anchorage is where these supplies are received, stored, and '
                'distributed to the other stations. The logistics of sustaining three '
                'billion people in a system with no natural resources is an achievement in '
                'itself, and Anchorage\'s supply chain managers are among the most capable '
                'in MERIT space. A disruption in the supply pipeline would be catastrophic '
                'within weeks, and everyone in Arcturus knows it. The Polaran strategists '
                'know it too. The supply convoys that arrive at Anchorage are among the '
                'most heavily escorted shipments in the inner systems.\n\n'
                'Anchorage also handles the repair work for ships damaged in the border '
                'skirmishes with Polaran vessels. The repair bays are busy. Skirmishes are '
                'frequent -- not the pitched battles that the Garrison Ring is designed to '
                'deter, but the smaller engagements between MERIT patrol ships and Polaran '
                'raiders or scouts operating in the system\'s open space. Ships come in '
                'with scorched armour, damaged sensors, and the distinctive burn patterns '
                'of Polaran weapons. The repair crews patch them up and send them back out. '
                'The cycle is continuous.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='The Crossing',
            short_description='A neutral station at the border -- where MERIT officials and Polaran representatives conduct the diplomacy that exists between skirmishes.',
            long_description=(
                'The Crossing is the most unusual station in the system -- a facility that '
                'exists specifically for contact with the Polaris faction. The station is '
                'positioned near the approaches to Polaris space, technically within MERIT '
                'territory but close enough to the border that Polaran ships can reach it '
                'without transiting the Garrison Ring. This positioning is deliberate. '
                'The Crossing is where the two sides talk.\n\n'
                'The diplomacy between MERIT and Polaris is not peace negotiation -- neither '
                'side pretends the conflict will end -- but the management of a contest that '
                'both sides prefer to keep below a certain threshold of violence. Prisoner '
                'exchanges are conducted at The Crossing. Agreements on navigation protocols in '
                'contested space are negotiated here. Disputes over specific incidents -- a '
                'Polaran ship fired on by a MERIT patrol, a MERIT convoy harassed by Polaran '
                'raiders -- are raised, discussed, and occasionally resolved. The diplomats '
                'on both sides are professionals who understand that their job is not to '
                'make peace but to prevent the skirmishing from escalating into something '
                'neither side wants.\n\n'
                'Polaran representatives on The Crossing are among the few citizens of an outer '
                'faction with a permanent, legitimate presence in MERIT space. They are '
                'watched, monitored, and constrained in their movements, but they are there, '
                'and their presence is a concession that MERIT does not extend to every '
                'faction. The Polarans, for their part, use The Crossing as an intelligence '
                'gathering opportunity that they do not bother to disguise, because MERIT '
                'uses them for the same purpose, and both sides consider this an acceptable '
                'cost of maintaining a channel of communication.'
            ),
            population=12_000_000,
        ),
        StellarObject(
            name='Drift Haven',
            short_description='A civilian station in the system\'s quieter space -- where the people who actually live in Arcturus long-term have built something resembling a home.',
            long_description=(
                'Drift Haven exists because three billion people cannot live on military '
                'stations and transit hubs without going mad. The station is positioned in '
                'the quieter space between the commercial core and the Garrison Ring -- far '
                'enough from the transit traffic to feel calm, close enough to be accessible. '
                'Drift Haven is the system\'s residential heart: the station where people '
                'raise families, where schools operate, where the community institutions '
                'that make a population into a civilisation have been established.\n\n'
                'Living in Arcturus long-term is an unusual choice. The system has no '
                'natural beauty -- no horizons, no weather, no sky. The enormous orange '
                'star is visible through observation ports as a vast amber disc that fills '
                'an unsettling proportion of the view, ancient and enormous and indifferent. '
                'The people who stay are the ones who have found something in the station '
                'life that they value: the community, the work, the particular character of '
                'a place that is defined entirely by human construction rather than natural '
                'geography. Drift Haven\'s residents are proud of what they have built in a '
                'system that offered them nothing to build on.\n\n'
                'The station has developed a culture of its own -- insular, self-reliant, '
                'and marked by the awareness that everything around them was made rather '
                'than found. The decorative traditions are inventive, compensating for the '
                'absence of natural materials with art, colour, and a creativity born of '
                'the fact that if you want beauty in Arcturus, you have to make it yourself.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='Far Watch',
            short_description='The outermost sensor station -- watching the Polaris approaches and providing early warning that is never early enough.',
            long_description=(
                'Far Watch is a small military station at the outer edge of the system -- '
                'the first point of detection for anything entering from Polaris space. The '
                'station operates long-range sensor arrays that scan the approaches '
                'continuously, providing the Garrison Ring and Crossway with advance notice '
                'of incoming traffic. In theory, Far Watch gives the system time to prepare '
                'for whatever is coming.\n\n'
                'In practice, the warning is never enough. Polaran ships are fast -- their '
                'neural pilots react faster and navigate more precisely than any manually '
                'piloted vessel -- and the distance between Far Watch and the inner system '
                'is crossed quickly by ships that do not need to slow down. Far Watch can '
                'tell the Garrison Ring that Polaran ships have entered the system. Far '
                'Watch cannot tell the Garrison Ring what those ships intend to do in time '
                'for the Ring to respond effectively. The station is a tripwire, and like '
                'all tripwires, it tells you that something has already happened.\n\n'
                'The crews at Far Watch are isolated, alert, and philosophical about their '
                'role. They watch. They report. They know that by the time their reports '
                'reach the inner system, the situation has already changed. They watch '
                'anyway, because someone has to, and because the alternative -- not '
                'watching -- is worse.'
            ),
            population=3_000_000,
        ),
    ],
    short_description='A barren transit hub and contested Polaris border -- three billion people living on stations in empty space, sustained entirely by imported supplies.',
    long_description=(
        'Arcturus is a system with nothing in it except people and the stations they '
        'built. The star is an ancient orange giant -- a wanderer from an older part of '
        'the galaxy, metal-poor and enormous, offering no planets, no moons, no '
        'asteroids worth mining, and no natural resources of any kind. The system would '
        'be empty if not for the accident of jump point geography that placed it at '
        'the intersection of dozens of inner-system routes. Arcturus is the crossroads '
        'of the inner systems: more traffic passes through than through any system '
        'except Sol itself, and the stations that service this traffic are the only '
        'reason anyone is here.\n\n'
        'Three point two billion people live in Arcturus, all of them on stations, all '
        'of them sustained by supplies imported from the rest of MERIT space. The '
        'system produces nothing and consumes everything. Every meal, every breath of '
        'air, every replacement part arrives by ship from systems that have what '
        'Arcturus lacks: planets, resources, and the natural capacity to sustain human '
        'life. The supply convoys are the system\'s lifeline, and their protection is '
        'a strategic priority second only to the defence of Sol itself.\n\n'
        'The defence is necessary because Arcturus borders Polaris space. The system is '
        'the most common route into and out of the Polaris cluster by traffic volume, '
        'and both MERIT and Polaran vessels are common sights. The Garrison Ring -- a '
        'chain of armed military stations -- protects the core infrastructure but '
        'cannot control the system\'s open space. Polaran ships transit Arcturus with '
        'a regularity that is half commerce, half provocation, and the skirmishes '
        'between MERIT patrols and Polaran raiders are frequent enough that the repair '
        'bays are never empty. The conflict is managed rather than resolved: The Crossing '
        'station provides a diplomatic channel where both sides negotiate the terms of '
        'their ongoing disagreement, and the violence stays below the level that would '
        'force either side into an escalation neither wants.\n\n'
        'Arcturus is a strange place to live -- a civilisation built in empty space '
        'around an ancient star that does not belong to this part of the galaxy, '
        'sustained by imports, defined by transit, and contested by a faction whose '
        'pilots are neurally fused to ships that move faster than anything MERIT can '
        'match. The people who live here long-term have built a culture from nothing, '
        'in a system that offered them nothing, and they are quietly proud of the '
        'achievement. Everything in Arcturus was made. Nothing was found. The residents '
        'consider this a point of identity rather than a limitation.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

CAPELLA = System(
    name='Capella',
    star='Quadruple system: Capella A and Capella B (twin G-type yellow giants, each approximately 10 times Sol diameter) in close orbit, with a distant pair of red dwarfs (Capella C and Capella D)',
    population=0,
    distance_to_sol=42.9,
    stellar_objects=[
        StellarObject(
            name='The Boneyard',
            short_description='The densest concentration of wreckage in the system -- centuries of ship-to-ship combat accumulated in the space between the twin suns.',
            long_description=(
                'The Graveyard is what the SCN calls the region of space between the inner '
                'system and the approaches from Antares space -- the volume where most of '
                'the skirmishes happen and where most of the wreckage ends up. Centuries of '
                'combat between MERIT and Antarian forces have left a debris field of '
                'destroyed and damaged ships, spent munitions, and the scattered remains '
                'of vessels that were crippled in engagements and left to drift. The '
                'wreckage orbits the twin suns in a slow, dispersed cloud -- not dense '
                'enough to be a navigation hazard but present enough that any transit '
                'through the inner system passes through the remains of old battles.\n\n'
                'The wreckage is a record. MERIT hulls and Antarian hulls drift together, '
                'the distinctions between them legible to anyone who knows what to look for. '
                'MERIT ships are clean-lined, modular, designed for crews who operate at '
                'baseline human capacity. Antarian wrecks are different -- angular, '
                'aggressive, built for speed and crewed by people on stimulants that '
                'let them operate at reaction speeds a baseline human cannot match. The '
                'Antarian wrecks often show signs of damage from the inside as well as the '
                'outside: consoles torn from mounts by hands that were shaking, bulkheads '
                'dented by crew in the grip of withdrawal or overdose when the stims ran '
                'out mid-engagement. The Graveyard tells the history of the conflict in '
                'broken metal, and the history is not pleasant for either side.\n\n'
                'Neither faction recovers its dead from Capella. The system is too contested '
                'for salvage operations -- any ship that slows down to recover wreckage is '
                'vulnerable to attack, and neither side will risk lives for debris. The dead '
                'remain in their ships, drifting in the warm golden light of the twin suns, '
                'and will remain there until the stars themselves change.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Flats',
            short_description='A broad region of open space where the larger engagements occur -- featureless void with nothing to hide behind.',
            long_description=(
                'The Flats is the SCN designation for the broad, open region of the outer '
                'system where the approaches from Antares space converge on the inner '
                'system. There is nothing here -- no planets, no asteroids, no debris dense '
                'enough to provide cover. The Flats is where the larger engagements happen, '
                'when they happen, because it is the space that Antarian raiding forces must '
                'cross to reach the inner-system jump approaches and the space where MERIT '
                'intercept forces try to stop them.\n\n'
                'Combat in the Flats is brutal and simple. There is nothing to manoeuvre '
                'around, nothing to hide behind, nothing to use for tactical advantage '
                'except speed and firepower. Antarian ships are fast and their stimmed crews '
                'react faster than MERIT crews can match, but Antarian ships are also '
                'fragile -- built for speed rather than endurance, crewed by people whose '
                'performance degrades sharply when the stims wear off. MERIT ships are '
                'slower, tougher, and crewed by people who function consistently. The '
                'engagements in the Flats tend to be short and violent: the Antarian force '
                'strikes fast, hoping to break through before the stims fade, and the MERIT '
                'force absorbs the initial assault and tries to hold long enough for '
                'Antarian performance to drop. The side that reads the timing correctly '
                'wins. The wreckage of the side that read it wrong joins the Graveyard.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Cairns',
            short_description='Automated navigation and sensor buoys maintained by MERIT -- the only permanent human-made infrastructure in the system.',
            long_description=(
                'The Cairns are not a settlement or a station but a network of automated '
                'buoys distributed throughout the system -- navigation markers, sensor '
                'platforms, and communications relays that provide MERIT forces with '
                'situational awareness in a system where there is nothing else to anchor '
                'infrastructure to. The buoys are small, hardened, and designed to survive '
                'the incidental damage of nearby engagements. They are also regularly '
                'destroyed by Antarian forces who target them specifically to blind MERIT '
                'sensors before a raid, and regularly replaced by MERIT logistics ships '
                'that transit the system on resupply runs.\n\n'
                'The cycle of destruction and replacement has continued for so long that '
                'the buoy maintenance schedule is one of the SCN\'s oldest continuous '
                'logistics operations. The buoys are manufactured in Tau Ceti, shipped to '
                'the nearest staging system, and deployed by specialist logistics vessels '
                'that enter Capella, place the replacements, and leave before Antarian '
                'forces can respond. The operation is routine, unglamorous, and essential '
                '-- without the Cairns, MERIT would be blind in a system it cannot afford '
                'to ignore.\n\n'
                'Antarian forces maintain their own equivalent -- sensor drones and '
                'communications relays scattered through their approach corridors. MERIT '
                'destroys these when it finds them. The mutual destruction of each other\'s '
                'sensor networks is a perpetual, low-level contest that neither side can '
                'win and neither side can abandon.'
            ),
            population=0,
        ),
    ],
    short_description='An uninhabited border system with the Antares faction -- twin golden suns illuminating centuries of wreckage from a conflict that never ends.',
    long_description=(
        'Capella is beautiful and empty and full of the dead. The system\'s twin yellow '
        'giants -- each ten times Sol\'s diameter, orbiting each other in a close binary '
        '-- cast a warm, golden light that would feel like home to anyone from Earth. '
        'The light falls on nothing. No planets orbit the twins. No moons, no asteroids '
        'worth naming, no natural bodies of any significance. The only objects in '
        'Capella that were not there when the stars formed are the ones that humans '
        'brought, and most of those are wreckage.\n\n'
        'Capella borders the Antares system -- gateway to the Stimmed and their '
        'pharmaceutical empire -- and the system has been contested for as long as the '
        'conflict between MERIT and the outer factions has existed. Neither side has '
        'settled Capella. Neither side wants to. The system\'s value is purely strategic: '
        'it is space that must be crossed, and the crossing is where the fighting '
        'happens. MERIT intercept forces try to prevent Antarian raiders from reaching '
        'the inner-system jump approaches. Antarian forces try to punch through. The '
        'engagements are frequent, short, and violent -- stimmed Antarian crews striking '
        'fast before their enhancement fades, MERIT crews absorbing the assault and '
        'waiting for the performance drop that always comes.\n\n'
        'Centuries of this have left the system strewn with wreckage. The Graveyard -- '
        'the densest concentration, in the space between the twin suns and the Antares '
        'approaches -- is a slow-drifting cloud of destroyed ships from both sides, '
        'tumbling in the golden light. MERIT hulls and Antarian hulls orbit together. '
        'Neither side recovers its dead. The system is too contested for salvage, and '
        'the dead are left where they fell, in ships that will orbit the twin suns '
        'until the metal decays or the stars consume them.\n\n'
        'No one lives in Capella. Forces transit through, fight, and withdraw. The only '
        'permanent infrastructure is automated -- MERIT sensor buoys that are regularly '
        'destroyed by Antarian forces and regularly replaced by MERIT logistics ships, '
        'in a cycle that has continued so long it has become routine. Capella is a '
        'battlefield without a front line, a border without a fence, and a graveyard '
        'without mourners. The twin suns shine on it all with the warm, golden light '
        'of a home that nobody here will ever see again.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

RASALHAGUE = System(
    name='Rasalhague',
    star='Blue-white subgiant (A5III), approximately 25 times Sol luminosity',
    population=12_000_000_000,
    distance_to_sol=48.6,
    stellar_objects=[
        StellarObject(
            name='Harmon',
            short_description='The media capital of the galaxy -- where the stories are made, the stars are born, and a billion dreamers compete for the attention of hundreds of billions.',
            long_description=(
                'Harmon is the most famous planet that most people have never visited. '
                'Seven billion people live here, and at any given time a significant fraction '
                'of them are trying to be noticed. Harmon is the centre of the galaxy\'s '
                'entertainment industry: the studios that produce the dramas, comedies, and '
                'spectacles consumed across the inner and outer systems are based here. The '
                'networks that broadcast to hundreds of billions of viewers operate from '
                'here. The talent agencies, the production companies, the distribution '
                'platforms, the advertising firms, the publicists, and the vast machinery '
                'of celebrity are all headquartered on Harmon.\n\n'
                'The planet is warm and bright under Rasalhague\'s vivid blue-white light, '
                'and the cities have been designed -- consciously, expensively, relentlessly '
                '-- to look good on screen. The architecture is dramatic. The public spaces '
                'are photogenic. The skylines are composed with the deliberate eye of people '
                'who understand that their city is not just a place to live but a backdrop '
                'for the content that defines the galaxy\'s culture. Harmon does not '
                'merely produce entertainment. Harmon is entertainment, performed at '
                'the scale of a civilisation.\n\n'
                'The economy is content. Everything on Harmon feeds the machine: the '
                'restaurants exist to be reviewed, the bars exist to be seen in, the fashion '
                'exists to be photographed. The human population divides roughly into the '
                'people who make it and the people who are trying to. The successful -- the '
                'performers, directors, writers, producers, and the technical artists who '
                'build the virtual environments and effects -- live well, some of them '
                'extraordinarily well. The unsuccessful -- the aspirants, the hopefuls, the '
                'people who arrived with talent and confidence and discovered that Harmon '
                'has a million people with talent and confidence for every available role -- '
                'work in the service industries that support the successful and wait for a '
                'break that may never come.\n\n'
                'The aspirant culture is Harmon\'s defining feature and its deepest wound. '
                'The planet runs on hope. People arrive from every system in the galaxy, '
                'drawn by the stories of those who made it, and most of them will not make '
                'it. They will wait tables, tend bar, work technical crew on productions '
                'they wish they were starring in, and eventually either make peace with a '
                'life adjacent to fame or leave. The ones who leave often go to the other '
                'planets in the system, which is how the grudge started.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='Talworth',
            short_description='The second planet -- agricultural, functional, and profoundly tired of being asked what it is like to live near Harmon.',
            long_description=(
                'Talworth is the second planet in the system and the largest of what the '
                'local media -- Harmon\'s media, the only media anyone outside the system '
                'has heard of -- calls the quiet planets. Talworth is an agricultural '
                'world. It grows food. It processes food. It ships food to Harmon and '
                'the other planets. This is important work. Nobody has ever made a drama '
                'about it.\n\n'
                'The population of Talworth is two billion people who farm, manufacture, '
                'and maintain infrastructure, and who have developed a collective identity '
                'defined largely by not being Harmon. Talworth residents are practical, '
                'understated, and allergic to spectacle. They dress plainly. They speak '
                'plainly. They regard the culture of Harmon -- the performative glamour, '
                'the celebrity worship, the relentless self-promotion -- with a contempt '
                'that is too ingrained to be called resentment. It is simply how Talworth '
                'people feel about Talworth things versus Harmon things, and they do '
                'not think it requires explanation.\n\n'
                'The grudge is real but low-level. Talworth feeds Harmon. Harmon '
                'does not think about Talworth. When Harmon\'s media mentions the other '
                'planets at all, it is usually as the punchline of a joke about boring '
                'places, and this is exactly the kind of thing that Talworth residents '
                'remember and Harmon residents do not realise they should apologise for. '
                'The children of Talworth grow up with a choice: stay and do honest work '
                'that nobody will ever celebrate, or go to Harmon and become one of the '
                'million hopefuls. The ones who go are regarded with a complicated mixture '
                'of understanding and betrayal. The ones who come back are welcomed without '
                'comment.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='Kedron',
            short_description='The third planet -- mining and heavy industry, providing the raw materials that Harmon consumes without acknowledgement.',
            long_description=(
                'Kedron is the system\'s industrial planet -- a cooler, rockier world '
                'further from the star with mineral deposits that support a mining and '
                'manufacturing economy. The planet produces construction materials, '
                'electronics components, and the industrial goods that keep the system '
                'functioning. The population is smaller than Talworth\'s and shares the '
                'same practical, unflashy character, though Kedron\'s version is harder-'
                'edged -- mining towns and factory districts rather than farming communities.\n\n'
                'Kedron\'s grudge against Harmon is sharper than Talworth\'s. '
                'Talworth is merely ignored. Kedron is occasionally depicted -- in '
                'Harmon\'s dramas, the gritty industrial planet is a reliable setting '
                'for stories about hardship, crime, and escape. The people of Kedron '
                'watch these portrayals with a bitterness that has curdled into a cultural '
                'fixture. Their world is not a backdrop for someone else\'s story about '
                'overcoming adversity. Their world is where they live, and they would '
                'appreciate it if the writers on Harmon would stop using their home as '
                'shorthand for misery.\n\n'
                'The irony is that Kedron is not miserable. The mining towns are '
                'functional, the wages are decent, and the quality of life is comparable to '
                'any mid-tier industrial world in the inner systems. The people are fine. '
                'They are simply unremarkable, which in a system dominated by a planet '
                'where everyone is competing to be remarkable is its own kind of insult.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Pell',
            short_description='A small ocean world -- quiet, overlooked, and the only planet in the system that has genuinely stopped caring about Harmon.',
            long_description=(
                'Pell is a small, cool world on the outer edge of the habitable zone '
                '-- mostly ocean, with scattered island continents and a thin, damp '
                'atmosphere. The planet supports a modest fishing and aquaculture economy '
                'and a population that is small enough to be genuinely invisible to '
                'Harmon\'s cultural machinery. Talworth is ignored. Kedron is '
                'caricatured. Pell is forgotten entirely, which the residents have '
                'decided is preferable.\n\n'
                'The culture on Pell is the most distinct in the system -- insular, '
                'maritime, and shaped by the ocean in ways that the other planets find '
                'difficult to understand. The communities are small and spread across the '
                'island chains. The pace of life follows the fishing seasons. The '
                'entertainment industry that defines the system might as well not exist '
                'here. Pell residents consume Harmon\'s output the way anyone '
                'consumes entertainment -- casually, selectively -- but they do not define '
                'themselves in relation to it. The grudge that animates Talworth and '
                'Kedron has no purchase on Pell because Pell has genuinely, '
                'thoroughly stopped caring.\n\n'
                'The planet\'s name was originally a placeholder in the early survey data '
                'that was never replaced with anything more dignified. The residents have '
                'kept it out of the same spirit that defines everything about the place: '
                'an indifference to image that is, in a system like Rasalhague, its own '
                'quiet rebellion.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='The Array',
            short_description='The orbital communications infrastructure that transmits Harmon\'s content to the rest of the galaxy -- the most powerful broadcast array outside Sol.',
            long_description=(
                'The The Array is the infrastructure that makes Harmon matter beyond '
                'the system. A network of communications satellites and relay stations in '
                'orbit above Harmon, the Ring transmits the system\'s entertainment '
                'output to the rest of the galaxy -- dramas, news, music, sports, and the '
                'endless stream of celebrity content that the inner and outer systems '
                'consume in quantities that the economists find significant and the '
                'sociologists find concerning.\n\n'
                'The Ring is the most powerful civilian broadcast array outside Sol. The '
                'signal reaches every inhabited system in MERIT space and leaks into the '
                'outer systems, where Harmon\'s content is consumed despite -- or because '
                'of -- the factions\' various objections. Antarian audiences watch Harmon '
                'dramas between doses. Polaran audiences experience them through neural '
                'interfaces that add sensory dimensions the creators never intended. Hyades '
                'audiences watch on screens set into prosthetic eyes. The content is '
                'universal in a way that nothing else in the galaxy is -- every faction, '
                'every system, every culture consumes Harmon\'s output, and the shared '
                'cultural references it creates are the closest thing the fractured galaxy '
                'has to a common language.\n\n'
                'The permanent staff of the The Array are the technicians and engineers '
                'who keep the signal flowing -- unglamorous work in the service of glamour, '
                'performed by people who are intimately familiar with the irony.'
            ),
            population=35_000_000,
        ),
        StellarObject(
            name='Highport',
            short_description='The system\'s primary orbital port -- where the dreamers arrive and the failures depart.',
            long_description=(
                'Highport is Rasalhague\'s main orbital port -- a large station in orbit '
                'above Harmon that handles the system\'s passenger and cargo traffic. The '
                'station\'s character is defined by its arrivals and departures. The arrivals '
                'are hopeful: young people from every system in the galaxy, carrying '
                'portfolios and demo reels and the unshakeable conviction that they will be '
                'the one who makes it. They step off the transport and look through the '
                'observation windows at Harmon below and see the place they have been '
                'dreaming about since they were old enough to watch a screen.\n\n'
                'The departures are quieter. The people leaving Harmon after years of '
                'trying do not look out the windows. They board the transports to Talworth, '
                'or Kedron, or home -- wherever home is -- with the particular exhaustion '
                'of people who gave everything to a dream and are now rearranging their '
                'understanding of who they are. The station staff have seen this cycle '
                'thousands of times. They are kind to the arrivals because the arrivals '
                'are excited, and kind to the departures because the departures need it.\n\n'
                'Highport also handles the logistics of the entertainment industry -- the '
                'equipment, the sets, the costumes, the technical infrastructure that '
                'Harmon\'s productions require. The cargo bays are full of things that '
                'look like nothing in crates and become spectacle when assembled. The '
                'station is the machine behind the curtain, and its name -- given by the '
                'first station operators with a sense of humour that has aged well -- '
                'captures its function exactly.'
            ),
            population=120_000_000,
        ),
    ],
    short_description='The media capital of the galaxy -- one planet of dreamers and stars, surrounded by siblings that do the real work and resent the attention.',
    long_description=(
        'Rasalhague is a system of two realities. One reality is Harmon -- the most '
        'famous planet outside Earth, home to the entertainment industry that produces '
        'the stories, music, and spectacle consumed by hundreds of billions across the '
        'inner and outer systems. Seven billion people live on Harmon, most of them '
        'connected to the content machine in some way: producing it, performing in it, '
        'supporting the people who do, or waiting for their chance. Harmon is '
        'glamorous, dramatic, and relentlessly self-regarding in the way that a planet '
        'whose primary export is its own image must be.\n\n'
        'The other reality is the rest of the system. Talworth grows food. Kedron '
        'mines and manufactures. Pell fishes. These planets are functional, '
        'competent, and invisible -- their five billion combined residents living '
        'ordinary lives in the shadow of a sibling that produces nothing tangible and '
        'receives all the attention. The grudge between the quiet planets and Harmon '
        'is the system\'s open secret: Talworth resents being ignored, Kedron '
        'resents being caricatured, and Pell has stopped caring entirely, which '
        'is its own form of commentary.\n\n'
        'Harmon\'s cultural influence is difficult to overstate. The The Array '
        '-- the most powerful civilian communications array outside Sol -- transmits '
        'content to every inhabited system, and the shared references it creates are '
        'the closest thing the fractured galaxy has to a common language. Antarian '
        'factory workers and MERIT senators watch the same dramas. Pleiadian miners '
        'and Polaran pilots follow the same celebrities. The content crosses every '
        'border that politics cannot, and the cultural power this represents is '
        'something MERIT values even if it would never describe entertainment as '
        'strategic.\n\n'
        'The human cost is the aspirant culture. Harmon draws dreamers from every '
        'system -- people who arrive with talent and conviction and discover that '
        'talent and conviction are the minimum requirement, not the differentiator. '
        'Most will not succeed. Many will spend years trying before accepting a life '
        'adjacent to the fame they sought. The ones who leave often settle on the '
        'quiet planets, bringing with them a complicated relationship with the world '
        'they left and the world they joined. Rasalhague runs on dreams, and dreams '
        'are a resource that is inexhaustible, unevenly distributed, and frequently '
        'cruel.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALDERAMIN = System(
    name='Alderamin',
    star='Blue-white main sequence (A7V), approximately 18 times Sol luminosity, extremely rapid rotator',
    population=100_000_000,
    distance_to_sol=49.0,
    stellar_objects=[
        StellarObject(
            name='Landfall',
            short_description='The colony world -- a hundred million people on a planet that is not yet finished becoming habitable.',
            long_description=(
                'Landfall is the reason anyone is in Alderamin. The planet was identified '
                'during the initial surveys after the jump link was discovered a century '
                'ago: a rocky world in the habitable zone with liquid surface water, a '
                'nitrogen-heavy atmosphere, and the potential -- with work -- to support '
                'human life without enclosed habitats. The key word is potential. Landfall '
                'is not there yet.\n\n'
                'The atmosphere is breathable in the technical sense that it contains '
                'enough oxygen to sustain a human being, but the mix is wrong -- too much '
                'carbon dioxide, not enough oxygen, and trace compounds that cause '
                'headaches, nausea, and long-term respiratory damage with extended exposure. '
                'The terraforming project is working on it. Atmospheric processors dot the '
                'landscape -- enormous installations that draw in the native atmosphere, '
                'scrub the carbon dioxide, and release oxygen-enriched air. The process is '
                'measurable on instruments and imperceptible to humans. The atmosphere is '
                'better than it was a century ago. It will be better still in another '
                'century. For now, the colonists live in enclosed settlements with filtered '
                'air and venture outside in respirators that they have learned to think of '
                'as clothing rather than equipment.\n\n'
                'The settlements are new in a way that nowhere else in the inner systems is '
                'new. The buildings are prefabricated MERIT-standard modules -- the same '
                'designs used in colonial infrastructure across the inner systems, assembled '
                'in configurations that the colonists are still figuring out. The streets '
                'do not have the organic growth of older worlds or the planned elegance of '
                'Altair\'s cities. They have the provisional feel of places that were built '
                'quickly by people who intend to build something better when they have time. '
                'The time has not yet arrived.\n\n'
                'The colonists are a self-selected population: people who chose to leave '
                'established worlds for a planet that is not yet finished. They are '
                'engineers, terraforming specialists, agricultural scientists, construction '
                'workers, and the generalists who are willing to do whatever needs doing. '
                'The culture is practical, cooperative, and marked by the particular '
                'optimism of people who can see the atmospheric readings improving year by '
                'year and believe they are building something their grandchildren will '
                'inherit. The grandchildren, they hope, will not need respirators.'
            ),
            population=85_000_000,
        ),
        StellarObject(
            name='The Processors',
            short_description='The network of atmospheric terraforming installations -- the machines slowly turning Landfall into a world humans can breathe on.',
            long_description=(
                'The Processors are not a single location but a network of atmospheric '
                'terraforming installations distributed across Landfall\'s surface and in '
                'low orbit -- the machinery that is, slowly and measurably, converting the '
                'planet\'s atmosphere from hostile to habitable. The installations are the '
                'largest structures on the planet: industrial-scale atmospheric scrubbers, '
                'oxygen generation plants, and the monitoring systems that track the '
                'atmospheric composition with a precision that the terraforming engineers '
                'describe as obsessive and everyone else describes as necessary.\n\n'
                'The Processors are MERIT technology, MERIT-funded, and MERIT-maintained. '
                'This is the core of Alderamin\'s dependency. The colony cannot terraform '
                'itself. The atmospheric processors require components, expertise, and '
                'replacement parts that Alderamin does not produce and cannot produce -- '
                'the industrial base does not exist. Every critical component arrives by '
                'ship from the inner systems, and if the supply stopped, the terraforming '
                'would stall. The atmosphere would not revert -- the progress made is '
                'permanent -- but the remaining work would stop, and the colonists would '
                'live in respirators indefinitely. This dependency is not resented. It is '
                'simply the reality of a colony that is a century old in a galaxy where '
                'most civilisations have had half a millennium to develop. The colonists '
                'are grateful for MERIT\'s support in the straightforward way of people '
                'who need help and are receiving it.'
            ),
            population=0,
        ),
        StellarObject(
            name='Anchor',
            short_description='The system\'s only orbital station -- a MERIT supply depot that is Alderamin\'s lifeline to the rest of the galaxy.',
            long_description=(
                'Anchor is the only orbital station in the system -- a modest MERIT '
                'installation in orbit above Landfall that handles all interstellar '
                'traffic, supply deliveries, and the communications relay that connects '
                'the colony to the rest of the inner systems. The station is small by the '
                'standards of established systems -- a single docking ring, a handful of '
                'cargo bays, and the administrative offices that manage the colony\'s '
                'logistics. In Altair or Sol, Anchor would be a minor facility. In '
                'Alderamin, it is everything.\n\n'
                'Every supply shipment arrives at Anchor. Every colonist arrives at Anchor. '
                'Every piece of equipment, every replacement part, every item that the '
                'colony cannot yet produce for itself comes through the station\'s cargo '
                'bays. The supply ships arrive on a regular schedule from the inner systems '
                '-- the schedule is the heartbeat of the colony, and delays are felt '
                'immediately. A late shipment means rationing. A missed shipment means '
                'worry. Two missed shipments means fear. The colonists track the supply '
                'schedule the way older civilisations track weather.\n\n'
                'The station staff are MERIT logistics personnel -- professionals who '
                'manage the supply chain with the seriousness it deserves. They are aware '
                'that their work is not glamorous. They are also aware that a hundred '
                'million people depend on them for everything from atmospheric processor '
                'components to coffee, and the weight of that responsibility is visible '
                'in the care they take.'
            ),
            population=8_000_000,
        ),
        StellarObject(
            name='Prospect',
            short_description='A cold outer world still being surveyed -- potentially the system\'s second colony in a century or two, if the first one succeeds.',
            long_description=(
                'Prospect is the system\'s other candidate for habitation -- a cold, rocky '
                'world further from the star with a thin atmosphere and subsurface water '
                'ice. The initial surveys flagged it as a possible second colony site, and '
                'a small survey team has been conducting detailed assessments for the past '
                'few decades. The work is slow, methodical, and oriented toward a future '
                'that is generations away.\n\n'
                'Nobody is colonising Prospect any time soon. Landfall is the priority, '
                'and Landfall will consume the system\'s resources and attention for '
                'another century at minimum before a second colony becomes practical. The '
                'survey team knows this. They are doing the groundwork that future '
                'colonists will use to make decisions about where to settle and what to '
                'build. It is work that will not bear fruit in their lifetimes, performed '
                'with the patience of people who understand that colonial development is '
                'measured in centuries, not careers.\n\n'
                'The survey team is small -- a few hundred scientists and their support '
                'staff, living in a temporary base on the surface. They are the most '
                'isolated humans in the inner systems, on a planet in the youngest colony '
                'in MERIT space, surveying a world that will not be settled until everyone '
                'currently alive is dead. They describe the work as meaningful. The sunsets '
                'on Prospect, they say, are extraordinary -- the thin atmosphere scatters '
                'the blue-white starlight into colours that no one has named yet because '
                'no one has been here long enough to need names for them.'
            ),
            population=500,
        ),
        StellarObject(
            name='Scoria',
            short_description='A hot, dense inner world -- surveyed, catalogued, and dismissed as useless within the first year of the colony\'s existence.',
            long_description=(
                'Scoria is the innermost planet -- a small, airless rock baked by the '
                'blue-white star at close range. The initial survey team spent three weeks '
                'assessing it and produced a report that could be summarised as: hot, dense, '
                'mineral-poor, and not worth the fuel it would cost to land on. The metal '
                'poverty is Alderamin\'s broader problem in miniature -- the system is young '
                'and the heavy elements that older systems accumulated over billions of years '
                'of stellar enrichment are simply not here in useful concentrations.\n\n'
                'Scoria has not been visited since the initial survey. The report sits in '
                'Anchor\'s database. Nobody reads it. The planet orbits the star, baking '
                'quietly, waiting for a civilisation that has larger concerns.'
            ),
            population=0,
        ),
        StellarObject(
            name='Wash',
            short_description='An icy outer body with water ice and frozen volatiles -- earmarked as a future resource but untouched for now.',
            long_description=(
                'Wash is a large icy body in the outer system -- not quite a planet, more '
                'of an oversized remnant from the system\'s young protoplanetary disk that '
                'never accreted into anything larger. The surface is water ice and frozen '
                'volatiles, and the survey team flagged it as a significant future resource '
                '-- water, nitrogen, and carbon compounds that the colony will eventually '
                'need as it grows beyond what Landfall\'s surface can provide.\n\n'
                'For now, Wash is untouched. The colony does not have the ships, the '
                'equipment, or the spare labour to begin extraction operations on an outer-'
                'system body. The resource is noted, logged, and waiting. Wash is a promise '
                'the system has made to its own future -- a reserve of material that will '
                'matter enormously in a century and does not matter at all today.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Scatter',
            short_description='A diffuse field of rocky debris -- remnants of the system\'s unfinished planetary formation, too thin to mine and too sparse to avoid.',
            long_description=(
                'The Scatter is a diffuse field of rocky debris spread through the middle '
                'orbital space -- not a proper asteroid belt but the unfinished business of '
                'a solar system that is still young enough that its material has not fully '
                'sorted itself. The fragments are small, widely spaced, and mineral-poor, '
                'offering nothing worth extracting. The field is thin enough that navigation '
                'through it is not dangerous, merely tedious -- the collision avoidance '
                'systems on the shuttle runs between Anchor and Prospect flag contacts '
                'occasionally, and the pilots adjust course without concern.\n\n'
                'The Scatter is a reminder that Alderamin is a young system in a literal, '
                'geological sense. The inner systems -- Sol, Tau Ceti, Alpha Centauri -- '
                'are billions of years old, their material long since consolidated into '
                'planets, moons, and stable belts. Alderamin has not had time. The debris '
                'that will eventually become something is still drifting, uncommitted, in '
                'the space between the worlds that did form. The colonists find this oddly '
                'appropriate. They are building a civilisation in a system that is itself '
                'still under construction.'
            ),
            population=0,
        ),
        StellarObject(
            name='Glint',
            short_description='A tiny, reflective body in an eccentric orbit -- notable only because it is bright enough to be visible from Landfall\'s surface at night.',
            long_description=(
                'Glint is a small rocky body -- a few dozen kilometres across -- in an '
                'eccentric orbit that brings it close enough to the star to heat its '
                'surface to a high albedo and then carries it out past Landfall\'s orbit '
                'where it is visible as a bright point in the night sky. Glint has no '
                'resource value, no strategic significance, and no practical use of any '
                'kind. It is, however, the brightest object in Landfall\'s sky besides the '
                'star itself, and the colonists have given it a disproportionate cultural '
                'significance.\n\n'
                'Glint is the first celestial object that children born on Landfall learn '
                'to identify. Parents point it out through habitat windows. It features in '
                'the colony\'s small but growing body of local art and poetry. A rock with '
                'no value has become, in the way that things do when a civilisation is young '
                'enough to still be making its myths, the first landmark of a culture that '
                'is only beginning to develop a relationship with its own sky.'
            ),
            population=0,
        ),
    ],
    short_description='The newest colony in the inner systems -- a century old, still being terraformed, and dependent on MERIT for everything.',
    long_description=(
        'Alderamin is what the beginning looks like. The jump link to the system was '
        'discovered barely a century ago, and the colony on Landfall is the youngest '
        'in the inner systems -- a hundred million people on a planet that is not yet '
        'finished becoming habitable. The atmospheric terraforming is in progress. The '
        'settlements are prefabricated modules arranged with the provisional logic of '
        'people who intend to build something better when they have time. The colonists '
        'wear respirators when they go outside. The atmosphere is improving, measurably, '
        'year by year. Their grandchildren may not need the respirators. They hope.\n\n'
        'The system is forty-nine light-years from Sol -- the furthest inner-system '
        'colony, at the outer edge of MERIT\'s effective reach. Despite the distance, '
        'Alderamin is more dependent on MERIT than any other system in the inner worlds. '
        'The colony cannot terraform itself. The atmospheric processors, the construction '
        'equipment, the medical supplies, the industrial components -- everything that '
        'the colony needs and cannot yet produce arrives by ship from the established '
        'systems. The supply schedule is the colony\'s heartbeat. Delays are felt. '
        'Missed shipments are feared. The dependency is not resented -- it is the '
        'reality of a civilisation that is a century old in a galaxy where most have '
        'had five.\n\n'
        'The people of Alderamin are different from the people of the older systems. '
        'They chose this. They left worlds with breathable air, established cities, '
        'and centuries of accumulated comfort to come to a planet where the air is '
        'slowly being made right and the buildings are temporary and the nearest '
        'neighbour system is further away than most inner-system residents can easily '
        'imagine. They are engineers, scientists, construction workers, and generalists '
        'who are building a world from raw material. The culture is practical, '
        'cooperative, and optimistic in the particular way of people who can see the '
        'atmospheric readings improving and believe that what they are doing matters. '
        'They are not wrong. Everything in the galaxy that is now old and comfortable '
        'was once this: new, unfinished, and sustained by the conviction that it was '
        'worth the work.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ZOSMA = System(
    name='Zosma',
    star='White main sequence (A4V), approximately 15 times Sol luminosity',
    population=12_500_000_000,
    distance_to_sol=58.4,
    stellar_objects=[
        StellarObject(
            name='Taverner',
            short_description='The capital world -- seven billion people living well on a temperate planet that has never made galactic news.',
            long_description=(
                'Taverner is the kind of world that colonial planners hoped every habitable '
                'planet would turn out to be: temperate, well-watered, with broad continents '
                'and a climate that varies from comfortable to pleasant. The colonists who '
                'settled Taverner arrived early in the interstellar expansion, established '
                'their cities under MERIT oversight, and proceeded to build a civilisation '
                'that is prosperous, functional, and almost entirely unremarkable.\n\n'
                'Seven billion people live on Taverner. The cities are well-built and '
                'well-maintained -- not planned with Concord\'s deliberate perfection but '
                'developed with the steady competence of a population that had centuries to '
                'get things right and no particular urgency to get them right quickly. The '
                'transit systems work. The hospitals are good. The schools produce graduates '
                'who are solidly educated and rarely exceptional. The economy is diversified '
                '-- manufacturing, agriculture, services, technology -- without any single '
                'sector dominating. Taverner does not specialise. Taverner does a bit of '
                'everything, competently, without fuss.\n\n'
                'The culture is shaped by distance from trouble. Zosma is fifty-eight '
                'light-years from Sol in absolute terms, but the jump links that connect it '
                'to the inner systems are easy and well-established, placing it within '
                'comfortable reach of MERIT\'s core. More importantly, Zosma is far from '
                'every contested border. No outer faction threatens this corner of the '
                'galaxy. No pirates raid the shipping routes. No intelligence operatives '
                'conduct shadow wars in the outer system. The people of Taverner are aware '
                'of these conflicts the way people in safe places are always aware of '
                'distant wars -- they follow the news, they have opinions, and they go to '
                'bed without locking their doors.\n\n'
                'Visitors from busier systems find Taverner pleasant and forgettable. '
                'Residents find it home, and are content with the distinction.'
            ),
            population=7_000_000_000,
        ),
        StellarObject(
            name='Dawnfield',
            short_description='The second habitable world -- warmer, smaller, and known within the system as the place with better weather and fewer people.',
            long_description=(
                'Ashfield is Zosma\'s second habitable world -- closer to the star, warmer, '
                'with a thicker atmosphere that traps heat and produces a climate that '
                'ranges from subtropical at the poles to genuinely hot at the equator. The '
                'planet was settled as Taverner\'s overflow, and the two worlds have '
                'developed the mild, comfortable rivalry that sibling planets tend to '
                'develop when neither has anything serious to argue about.\n\n'
                'Ashfield\'s population is smaller than Taverner\'s and its cities are more '
                'spread out, taking advantage of the warm climate with low-density '
                'settlements that sprawl across the subtropical zones. The culture is '
                'marginally more relaxed than Taverner\'s -- outdoor dining, longer '
                'holidays, a pace of life that Taverner residents describe as lazy and '
                'Ashfield residents describe as civilised. The argument has been going on '
                'for centuries and shows no sign of resolution, which suits both sides.\n\n'
                'Ashfield\'s economy leans toward agriculture and tourism -- the warm '
                'climate supports year-round growing seasons that produce a surplus exported '
                'to Taverner and beyond, and the beaches and coastal settlements attract '
                'visitors from across the system. The tourism is modest by galactic '
                'standards -- nobody travels to Zosma from another system for the beaches '
                '-- but it sustains a local hospitality industry that Ashfield residents are '
                'quietly proud of.'
            ),
            population=3_200_000_000,
        ),
        StellarObject(
            name='Chelton',
            short_description='A cold outer world with a modest mining and research presence -- the system\'s quiet third sibling.',
            long_description=(
                'Chelton is the system\'s third planet -- a cold, rocky world on the outer '
                'edge of the habitable zone with a thin atmosphere and surface conditions '
                'that require enclosed habitats. The planet hosts a modest mining operation '
                'extracting minerals that supplement Taverner and Ashfield\'s industrial '
                'needs, and a handful of research installations that take advantage of the '
                'cold, clear conditions for astronomical observation and atmospheric '
                'science.\n\n'
                'Chelton\'s population is small and practical -- miners, researchers, and '
                'their families, living in enclosed settlements that are comfortable without '
                'being luxurious. The planet has the character of a small town: everyone '
                'knows everyone, the community is tight-knit, and the residents have the '
                'particular pride of people who live somewhere that nobody else thinks about. '
                'Chelton is the kind of place where people come for a two-year contract and '
                'stay for a lifetime, discovering that the quiet and the community suit them '
                'better than the cities they left.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Harwick',
            short_description='A large gas giant -- fuel processing on its moons and the system\'s modest military garrison.',
            long_description=(
                'Harwick is a large gas giant in the outer system -- the gravitational '
                'anchor of Zosma\'s outer orbital space, with moons that host fuel '
                'processing operations and the system\'s MERIT military garrison. The '
                'garrison is small even by the standards of peaceful systems -- a handful '
                'of patrol ships, a customs detachment, and the administrative staff that '
                'keeps the operation running. The posting is considered the quietest in the '
                'SCN. Officers assigned to Zosma sometimes describe it as semi-retirement '
                'with a uniform.\n\n'
                'The fuel processing on Harwick\'s moons services the system\'s commercial '
                'traffic -- freighters, passenger transports, and the steady flow of ships '
                'that connect Zosma to the rest of the inner systems. The traffic is '
                'consistent, orderly, and unexciting. The fuel processing is efficient and '
                'unremarkable. Harwick is a gas giant doing what gas giants in settled '
                'systems do, and the people who work there are content with the routine.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Whitmore Gate',
            short_description='The system\'s primary orbital port -- a well-run transit hub that processes its traffic without incident or distinction.',
            long_description=(
                'Whitmore Gate is Zosma\'s main orbital port -- a station in high orbit '
                'above Taverner that handles interstellar traffic, inter-planetary transit, '
                'and the commercial logistics of a twelve-billion-person system. The station '
                'is modern, efficient, and thoroughly unremarkable. The docking procedures '
                'are smooth. The customs inspections are professional. The commercial '
                'district offers the standard selection of restaurants, hotels, and services '
                'that transit passengers expect and that distinguishes itself from other '
                'orbital ports in no particular way.\n\n'
                'Whitmore Gate\'s one distinction is reliability. The station has the '
                'highest on-time transit rate in the inner systems -- a statistic that the '
                'station\'s management is proud of and that nobody outside the logistics '
                'profession has ever heard of or cared about. The station runs well because '
                'the people who run it are competent, the traffic is manageable, and nothing '
                'ever happens to disrupt the schedule. This is, the station\'s management '
                'would argue, the highest achievement in transit operations: not that '
                'everything runs smoothly despite challenges, but that there are no '
                'challenges in the first place.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Durn',
            short_description='A hot inner world -- solar collection arrays and automated industry, unremarkable even by Zosma\'s standards.',
            long_description=(
                'Durn is the innermost planet -- a small, dense, airless world close to the '
                'star with solar collection arrays and automated mineral extraction '
                'operations. The planet is functionally identical to dozens of hot inner '
                'worlds across the inner systems: solar energy collected on the day side, '
                'industrial operations on the night side, a small human population '
                'maintaining the automated systems. The engineers who work on Durn describe '
                'it as steady work in a steady system, and they mean this as a compliment.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Farsett',
            short_description='A frozen outer body hosting a communications relay and a small research station -- Zosma\'s quiet edge.',
            long_description=(
                'Farsett is a cold, rocky body in the outer system hosting a long-range '
                'communications relay and a small research station. The relay connects '
                'Zosma to the broader MERIT communications network. The research station '
                'conducts astronomical surveys and deep-space monitoring that contribute '
                'to the inner systems\' ongoing mapping programmes. The staff are few and '
                'content.\n\n'
                'Farsett is the furthest inhabited point in a system that does not extend '
                'very far. The view from the research station shows the star as a bright '
                'white point and the system\'s planets as specks. The researchers describe '
                'the solitude as restful. In a galaxy of contested borders, pirate systems, '
                'and shadow wars, Farsett is a place where the most exciting event in a '
                'typical month is a software update to the relay equipment. The researchers '
                'are fine with this.'
            ),
            population=1_500_000,
        ),
    ],
    short_description='A peaceful, prosperous system in a quiet corner of the galaxy -- twelve billion people living well and making no headlines.',
    long_description=(
        'Zosma is the system that works. Twelve and a half billion people across two '
        'habitable worlds, a modest gas giant economy, and a military garrison so '
        'quiet that the posting is considered semi-retirement. The system is fifty-eight '
        'light-years from Sol in absolute terms, but the jump links that connect it to '
        'the inner systems are easy and well-established, and the corner of the galaxy '
        'it occupies is far from every contested border and every outer-faction threat. '
        'Zosma has never been raided, never been threatened, and never been the site of '
        'anything that the rest of the galaxy would consider newsworthy.\n\n'
        'The system was settled during the early interstellar expansion and developed '
        'steadily under MERIT oversight into a civilisation that is prosperous, '
        'diversified, and thoroughly unremarkable. Taverner, the capital world, is a '
        'temperate planet where the cities work, the hospitals are good, and the '
        'schools produce solid graduates. Ashfield, the warmer second world, grows food '
        'and offers beaches. Chelton, the cold third world, mines and researches. The '
        'economy does a bit of everything. The culture is comfortable. The people are '
        'content.\n\n'
        'Zosma\'s contribution to the galaxy is the thing that does not make for '
        'interesting stories: it is a place where civilisation functions as intended. '
        'MERIT\'s model of governance -- planned development, guaranteed basic needs, '
        'stable institutions -- produces Zosma when it is allowed to operate without '
        'the complications of contested borders, piracy, or factional conflict. The '
        'result is not dramatic. The result is twelve billion people who are fed, '
        'housed, educated, and employed, living lives that are comfortable without '
        'being exceptional, in a system that runs smoothly because nothing prevents '
        'it from running smoothly. Critics call Zosma bland. Residents call it home. '
        'Both are right, and the residents do not consider the criticism a problem.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

SHERATAN = System(
    name='Sheratan',
    star='White main sequence (A5V), approximately 15 times Sol luminosity',
    population=16_500_000_000,
    distance_to_sol=59.6,
    stellar_objects=[
        StellarObject(
            name='Sheratan Alpha',
            short_description='The first of four identical agricultural worlds -- indistinguishable from the other three by design.',
            long_description=(
                'Sheratan Alpha is a habitable world that has been terraformed beyond '
                'recognition. The original planet -- whatever it looked like before the '
                'agricultural engineers arrived -- is gone, replaced by a surface that has '
                'been sculpted, conditioned, and optimised to produce food at a scale and '
                'efficiency that no other system can match. The continents are planting '
                'grids. The oceans are nutrient-managed aquaculture zones. The atmosphere '
                'is composition-controlled to maximise photosynthetic yield. The soil is '
                'not soil -- it is engineered growth medium, calibrated to the specific '
                'nutritional requirements of the crop strains planted in it, which are '
                'themselves genetically engineered to a precision that makes conventional '
                'agriculture look like guesswork.\n\n'
                'Standing on the surface of Sheratan Alpha, you would have no way of '
                'knowing you were not on Beta, Gamma, or Delta. This is not an '
                'exaggeration. The four worlds have been terraformed to identical '
                'specifications -- the same atmospheric composition, the same soil '
                'chemistry, the same planting grids at the same latitudes, the same crop '
                'rotations on the same schedule. The mountains that interfered with optimal '
                'planting coverage were levelled. The rivers that did not follow efficient '
                'irrigation paths were redirected. The weather systems that introduced '
                'variability were suppressed by atmospheric management. Any feature that '
                'made one world different from another was identified as an inefficiency '
                'and removed.\n\n'
                'The human population lives in residential blocks distributed at '
                'mathematically regular intervals across the surface -- identical '
                'settlements providing identical housing, identical services, and identical '
                'access to the space elevators that connect the surface to the orbital '
                'processing platforms. The people who live on Alpha are agricultural '
                'technicians, genetic engineers, soil chemists, and logistics coordinators. '
                'They are good at their work. They do not describe their world as beautiful.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Sheratan Beta',
            short_description='The second of four identical agricultural worlds -- the same planting grids, the same settlements, the same everything.',
            long_description=(
                'Sheratan Beta is identical to Alpha. The same terraforming specifications, '
                'the same crop strains, the same engineered growth medium, the same '
                'atmospheric composition, the same planting schedule. The settlements are '
                'in the same positions relative to the planting grids. The space elevators '
                'are at the same latitudes. A technician transferred from Alpha to Beta '
                'would notice the transfer only because the paperwork told them so.\n\n'
                'The homogeneity is the point. Sheratan\'s agricultural model is based on '
                'the elimination of variability. Variability is waste. A crop that performs '
                'differently on Beta than on Alpha represents a variable that has not been '
                'controlled, and an uncontrolled variable is an optimisation opportunity. '
                'The agricultural engineers who designed the system spent decades identifying '
                'and eliminating every source of variation between the four worlds until '
                'the output per hectare, per growing cycle, per calorie of energy input is '
                'identical across all four planets to within fractions of a percentage '
                'point. This is considered an achievement. It is also, to visitors from '
                'anywhere else, profoundly unsettling.\n\n'
                'The residents of Beta do not find it unsettling. They find it normal, '
                'because it is the only normal they know. The children born on Sheratan '
                'grow up in a world where everything is the same everywhere, and the '
                'concept of geographical identity -- of a place being different from another '
                'place -- is something they encounter only when they travel to other '
                'systems. Many find the experience disorienting. Some find it wonderful. '
                'A few come back and describe the rest of the galaxy as chaotic, which '
                'from a Sheratan perspective it is.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Sheratan Gamma',
            short_description='The third of four identical agricultural worlds -- producing the same crops at the same yield as the other three.',
            long_description=(
                'Sheratan Gamma is identical to Alpha and Beta. The description of one is '
                'the description of all three. This is, depending on your perspective, '
                'either an extraordinary achievement in agricultural engineering or a quiet '
                'horror.\n\n'
                'The horror, for those who feel it, is not in any specific feature but in '
                'the totality: four planets with every natural feature removed, every '
                'landscape replaced, every variable controlled, every surface subordinated '
                'to the mathematics of yield optimisation. There are no forests on Sheratan '
                'Gamma. There are no wilderness areas. There are no hills that exist because '
                'geology put them there rather than because the planting grid required an '
                'elevation change for drainage. The entire surface of the planet is a '
                'machine for converting sunlight into calories, and the machine is very '
                'good at its job.\n\n'
                'The residents do not see the horror. They see home. They see a world where '
                'the harvest is predictable, where the work is steady, where the logistics '
                'are efficient, and where the output feeds billions of people across the '
                'inner systems. The residents of Gamma are proud of what their system '
                'produces. They feed the galaxy. They find it strange that anyone would '
                'look at that and feel anything other than gratitude.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Sheratan Delta',
            short_description='The fourth of four identical agricultural worlds -- the outermost, the last to be terraformed, and now indistinguishable from the first.',
            long_description=(
                'Sheratan Delta was the last of the four worlds to be terraformed -- it '
                'orbits furthest from the star, and the initial conditions required more '
                'work to bring into alignment with the other three. The terraforming '
                'engineers considered this a challenge rather than an obstacle. Delta was '
                'warmed, its atmosphere adjusted, its surface reshaped, and its soil '
                'replaced until it matched the other three to the same specifications. The '
                'project took longer than the others. The result is identical.\n\n'
                'Delta is sometimes described -- by the few outsiders who pay attention to '
                'Sheratan\'s internal distinctions -- as the proof of concept. If the system '
                'can take a colder, less hospitable world and make it indistinguishable from '
                'a warmer, more naturally suitable one, then the model works. The '
                'agricultural engineers agree. The model works. The output per hectare on '
                'Delta matches Alpha, Beta, and Gamma. The crop yields are identical. The '
                'growing cycles are synchronised. Four worlds, four billion people each, '
                'one output. The system is complete.\n\n'
                'Delta has one unofficial distinction that the other worlds do not: its '
                'population includes a slightly higher proportion of people who transferred '
                'from elsewhere in the system and cannot tell the difference. They applied '
                'for transfer to Delta, were approved, moved, and found themselves in the '
                'same settlement layout, the same housing, the same planting grid, doing '
                'the same work. Some of them found this funny. Others found it confirming. '
                'A few found it deeply, quietly disturbing, and they are the ones who '
                'eventually leave Sheratan entirely.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='The Grid',
            short_description='The network of orbital processing platforms above all four worlds -- where the harvest is packaged and shipped to the rest of the galaxy.',
            long_description=(
                'The Grid is the collective name for the orbital processing platforms that '
                'sit above each of the four worlds, connected to the surface by space '
                'elevators that carry raw produce upward in a continuous stream. The '
                'platforms are large, automated, and identical -- the same designs replicated '
                'above each world, processing the same crops into the same packaged goods '
                'for distribution across the inner systems.\n\n'
                'The throughput is staggering. Sheratan ships more tonnage of goods than '
                'any system in the galaxy except Sol. The cargo drones that carry the '
                'packaged produce from the Grid to the system\'s outbound routes are a '
                'permanent feature of Sheratan\'s orbital space -- swarms of automated '
                'vessels moving in mathematically optimised patterns, each drone following '
                'a trajectory calculated to minimise fuel expenditure and maximise '
                'throughput. From orbit, the drone swarms look like currents in a river, '
                'flowing from the platforms to the collection points where the interstellar '
                'freighters wait.\n\n'
                'The human staff on the Grid are logistics specialists and quality control '
                'technicians -- people who monitor the automated processing and intervene '
                'only when something deviates from specification. Deviations are rare. The '
                'system was designed to minimise them, and it succeeds. A shift on the Grid '
                'is hours of watching numbers that do not change, punctuated by the '
                'occasional adjustment that brings a number back to where it should be. The '
                'staff describe the work as meditative. They are not being ironic.'
            ),
            population=0,
        ),
        StellarObject(
            name='Sheratan Central',
            short_description='The system\'s administrative hub and transit station -- where the logistics that feed the galaxy are coordinated.',
            long_description=(
                'Sheratan Central is the system\'s only orbital installation that is not '
                'directly part of the agricultural operation -- an administrative station '
                'in a central orbit that coordinates the logistics across all four worlds '
                'and handles the interstellar traffic that connects Sheratan to the rest '
                'of MERIT space. The station is functional and utilitarian, designed by '
                'the same optimisation philosophy that produced the planets: no wasted '
                'space, no unnecessary features, everything subordinated to efficiency.\n\n'
                'Sheratan Central is where the system\'s agricultural output is allocated -- '
                'where the logisticians decide which shipments go to which systems, how '
                'much is reserved for strategic stockpiles, and how the surplus is '
                'distributed. The decisions are made by algorithms that optimise for '
                'nutritional coverage across the inner systems, adjusted by human '
                'logisticians who handle the exceptions that the algorithms cannot. The '
                'work is important -- Sheratan\'s output feeds a significant fraction of '
                'the inner systems\' population -- and it is performed with the quiet '
                'intensity of people who understand that a miscalculation here means '
                'shortages somewhere else.\n\n'
                'Visitors arriving at Sheratan Central for the first time often remark on '
                'the view: four worlds visible from the observation deck, each one green '
                'and blue from orbit, each one identical to the others in every detail that '
                'a human eye can distinguish. The residents point out that from orbit, you '
                'can see the planting grids -- faint geometric patterns covering the '
                'continents, visible at scale as the largest single structures built by '
                'humanity. The visitors are not always sure whether to be impressed or '
                'disturbed. The residents do not understand the distinction.'
            ),
            population=45_000_000,
        ),
    ],
    short_description='The galaxy\'s breadbasket -- four identical, mathematically optimised agricultural worlds feeding the inner systems.',
    long_description=(
        'Sheratan is agriculture perfected, and perfection turns out to be unsettling. '
        'The system contains four habitable worlds, each one terraformed to identical '
        'specifications: the same atmospheric composition, the same engineered soil, '
        'the same genetically optimised crop strains planted in the same grids at the '
        'same latitudes on the same schedule. The mountains that interfered with '
        'planting coverage were levelled. The rivers that did not follow efficient '
        'irrigation paths were redirected. The weather systems that introduced '
        'variability were suppressed. Any feature that made one world different from '
        'another was identified as an inefficiency and removed.\n\n'
        'Sixteen and a half billion people live in Sheratan, four billion on each world, in '
        'identical residential settlements distributed at mathematically regular '
        'intervals across identical surfaces. Standing on any of the four worlds, a '
        'visitor would have no way of knowing which one they were on. The planting '
        'grids stretch to every horizon. The space elevators rise from the same '
        'latitudes into orbital processing platforms that package the harvest for '
        'distribution. Swarms of cargo drones fill the orbital space in optimised '
        'patterns, carrying the produce to interstellar freighters in a continuous '
        'stream. Sheratan ships more tonnage than any system except Sol.\n\n'
        'The system feeds a significant fraction of the inner systems\' population. '
        'The crop yields are the highest in the galaxy. The efficiency per hectare, '
        'per calorie of energy input, per unit of water consumed is unmatched '
        'anywhere. The agricultural engineers who designed the system consider it '
        'their finest achievement: the mathematical optimisation of food production '
        'at a planetary scale, replicated four times, producing identical output on '
        'identical schedules from identical worlds.\n\n'
        'Visitors find it eerie. The homogeneity, the geometric precision of the '
        'planting grids visible from orbit, the absence of any natural landscape, the '
        'knowledge that four entire planets have been reshaped into machines -- it '
        'provokes a discomfort that the residents do not share and do not understand. '
        'The residents see home. They see steady work and predictable harvests and the '
        'satisfaction of feeding billions. They find the rest of the galaxy, with its '
        'messy landscapes and inefficient agriculture and unpredictable weather, '
        'slightly chaotic. Both perspectives are valid. Neither side is likely to '
        'convince the other.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALDEBARAN = System(
    name='Aldebaran',
    star='Enormous orange giant (K5III), approximately 44 times Sol diameter, 425 times Sol luminosity -- a vast amber star dominating the sky of every body in the system',
    population=0,
    distance_to_sol=65.3,
    stellar_objects=[
        StellarObject(
            name='Constance',
            short_description='The world that was supposed to be home -- partially terraformed, partially built, and abandoned when the war made it indefensible.',
            long_description=(
                'Constance was going to be a colony. The surveys were promising: a rocky world '
                'in the habitable zone of the enormous orange giant, with surface water, '
                'a nitrogen-heavy atmosphere that needed work but not too much work, and '
                'the kind of conditions that terraforming engineers describe as cooperative. '
                'MERIT approved the colonisation programme. The atmospheric processors were '
                'deployed. The first settlements were built. The colonists arrived -- '
                'engineers, terraformers, construction workers, the advance population of '
                'what was planned to be a major new colony at the edge of the inner systems.\n\n'
                'Then the outer systems declared independence, and the strategic calculus '
                'changed overnight. Aldebaran was one soft jump from Ain and the Hyades '
                'cluster. The system that had been a promising frontier was now an exposed '
                'salient -- easy for the Hyades to reinforce, difficult for MERIT to '
                'defend, and not yet developed enough to justify the cost of trying. The '
                'decision was made quickly and without sentiment: evacuate the colonists, '
                'shut down the terraforming programme, and abandon the system. The '
                'colonists were relocated to established worlds. The equipment was left '
                'behind because it was cheaper to abandon than to transport.\n\n'
                'Constance today is a world in arrested development. The atmosphere is half-'
                'terraformed -- better than it was before MERIT arrived, worse than it '
                'would have been if the programme had continued. Breathable in some '
                'regions with a respirator, breathable in others without one, and toxic '
                'in the low-lying areas where the atmospheric processors never finished '
                'their work. The settlements stand empty. The prefabricated MERIT-standard '
                'modules are intact but deteriorating -- seals failing, windows cracked by '
                'thermal cycling, dust accumulating in buildings that were designed to be '
                'maintained and have not been maintained for over a century. The streets '
                'are laid out in the familiar MERIT grid pattern, connecting buildings that '
                'nobody lives in to facilities that nobody uses.\n\n'
                'The atmospheric processors are the largest objects on the surface -- '
                'enormous installations that were running when the evacuation order came '
                'and were shut down in sequence as the last transports departed. Some have '
                'collapsed. Others stand intact, their housings weathered but their '
                'structures sound, waiting for a restart command that nobody intends to '
                'send. The terraforming was working. The atmosphere was improving. The '
                'readings in the last reports before evacuation showed a world that was '
                'becoming habitable on schedule. The engineers who wrote those reports were '
                'reassigned to other systems. The world they were building was left to '
                'the silence and the enormous amber star.'
            ),
            population=0,
        ),
        StellarObject(
            name='Kelsworth',
            short_description='The second candidate world -- surveyed and partially prepared but never settled before the evacuation.',
            long_description=(
                'Kelsworth was the system\'s second colonisation target -- a cooler world '
                'further from the star that the development plan designated for later '
                'phases. The surveys were completed. The landing sites were selected. '
                'Preliminary terraforming equipment was deployed to begin atmospheric '
                'preparation before the settlers arrived. The settlers never arrived.\n\n'
                'Kelsworth\'s surface shows the traces of the work that was started and never '
                'finished. A handful of atmospheric processors stand on the designated '
                'sites, most of them never activated -- deployed from orbit, landed by '
                'automated systems, and left in their startup configurations when the '
                'evacuation order came before anyone could initialise them. The landing '
                'zones are cleared and graded -- flat patches of prepared ground in an '
                'otherwise untouched landscape, marked with MERIT survey beacons that '
                'still transmit their location codes to anyone with a receiver. The beacons '
                'were designed to guide incoming colonist transports to their landing zones. '
                'They guide nothing now. They transmit because nobody turned them off.\n\n'
                'Kelsworth\'s atmosphere is essentially unchanged from its natural state -- '
                'the terraforming barely began. The planet is cold, thin-aired, and empty '
                'of everything except the equipment that was meant to make it something '
                'else.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dunmore',
            short_description='The third candidate world -- a warm, dense planet that was earmarked for industrial development and never touched beyond the initial survey.',
            long_description=(
                'Dunmore was the colonisation plan\'s industrial world -- a warm, dense '
                'planet closer to the star with mineral deposits that the surveys identified '
                'as significant. The development plan called for Dunmore to supply the raw '
                'materials that Constance and Kelsworth would need as they grew: construction '
                'metals, industrial minerals, the heavy elements that a developing colony '
                'consumes in enormous quantities. The timeline placed Dunmore\'s development '
                'in the third phase, after Constance was established and Kelsworth\'s '
                'terraforming was underway.\n\n'
                'The third phase never came. Dunmore was surveyed, mapped, and assigned a '
                'development schedule that exists in MERIT\'s planning archives alongside '
                'Corrath\'s fuel processing plans and all the other documents describing a '
                'future that was cancelled. The planet\'s surface is untouched -- no '
                'equipment was deployed, no sites were prepared, no human being has stood on '
                'the surface since the survey team collected their samples and departed. The '
                'mineral deposits that the survey identified are still there, undisturbed, '
                'in a planet that glows dull orange under the light of the enormous star.\n\n'
                'Hyadean interest in Dunmore is assumed but unconfirmed. The Hyades cluster '
                'is industrial, and a mineral-rich world one soft jump from Ain would be '
                'valuable to a faction that builds and replaces and repairs as relentlessly '
                'as the Hyades does. Whether Hyadean mining operations will eventually be '
                'established on Dunmore is a question that MERIT strategists discuss and '
                'cannot answer. If they are, MERIT will have lost more than a colony. It '
                'will have handed the Hyades a resource base it surveyed and paid for.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Scaffold',
            short_description='The remains of the orbital construction infrastructure -- docking platforms, supply depots, and habitat frames left in orbit when the system was abandoned.',
            long_description=(
                'The Scaffold is the collective name for the orbital infrastructure that '
                'MERIT left behind -- the docking platforms, supply depots, fuel reserves, '
                'and partially assembled habitat frames that were in orbit above Constance when '
                'the evacuation order came. The evacuation prioritised people and data. The '
                'hardware was left.\n\n'
                'The Scaffold drifts in Constance\'s orbit in various states of decay. The '
                'docking platforms are intact but unpowered -- dark structures visible on '
                'sensors as metallic masses that do not respond to hails. The supply depots '
                'still contain material: construction supplies, prefabricated modules, '
                'atmospheric processor components, and the miscellaneous cargo that was in '
                'transit when the order came and was never unloaded. The habitat frames are '
                'the most striking -- skeletal outlines of orbital habitats that were under '
                'construction, their structural members complete but their hulls never '
                'sealed, their interiors open to vacuum.\n\n'
                'The Scaffold is of interest to the Hyades. Hyadean military patrols pass '
                'through regularly, and intelligence reports suggest that Hyadean engineers '
                'have surveyed the Scaffold for usable material. Whether they have taken '
                'anything is unclear. The MERIT equipment was not designed for Hyadean '
                'specifications -- the modular, clean-lined MERIT standard is fundamentally '
                'different from the Hyadean approach of exposed conduits and industrial '
                'pragmatism. But material is material, and a hull plate does not care which '
                'design philosophy shaped it.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Approach',
            short_description='The region of space facing Ain -- where Hyadean military traffic is constant and the system\'s strategic significance is visible.',
            long_description=(
                'The Approach is what MERIT strategists call the volume of space between '
                'Aldebaran\'s inner system and the soft jump link to Ain. This is the '
                'space that Hyadean ships cross, and they cross it frequently. The jump '
                'link to Ain is soft -- wide, stable, and navigable by any ship class '
                'including capital vessels. This makes Aldebaran simultaneously the easiest '
                'system for the Hyades to reinforce and the most likely route for any '
                'future MERIT offensive into Hyadean space.\n\n'
                'Both sides understand this. The Hyadean military maintains a regular '
                'patrol presence in the Approach -- warships transiting through on '
                'schedules that MERIT intelligence monitors from long-range sensor posts '
                'in neighbouring systems. The patrols are a statement of control: the '
                'Hyades considers Aldebaran part of its defensive perimeter, and the '
                'regular passage of warships through the Approach reinforces that claim. '
                'The ships are Hyadean standard -- tough, industrial, unglamorous vessels '
                'with exposed conduits and visible welds, crewed by people whose '
                'prosthetic modifications allow them to interface directly with their '
                'ships\' systems.\n\n'
                'MERIT has not contested the Hyadean presence. Aldebaran was abandoned, '
                'and abandonment carries implications. But MERIT has also not renounced '
                'its claim on the system. The colonial charter was suspended, not revoked. '
                'The system remains, in MERIT\'s legal framework, an inner-system territory '
                'under temporary suspension of development. The Hyades does not recognise '
                'MERIT\'s legal framework. The result is a system that both sides claim, '
                'neither side occupies, and one side patrols while the other watches from '
                'a distance.'
            ),
            population=0,
        ),
        StellarObject(
            name='Corrath',
            short_description='A gas giant that was surveyed for fuel processing -- the plans were drawn up, the infrastructure was never built.',
            long_description=(
                'Corrath is a mid-sized gas giant in the outer system that the colonisation '
                'plan designated as the system\'s future fuel source. The surveys were '
                'thorough: atmospheric composition analysed, orbital mechanics calculated, '
                'moon sites identified for processing installations. The engineering plans '
                'were drawn up. The budget was allocated. The first construction ships were '
                'scheduled.\n\n'
                'They were never sent. The evacuation order came before the fuel processing '
                'infrastructure moved beyond the planning stage. Corrath orbits the amber '
                'star with its atmosphere unsampled, its moons unbuilt, and its engineering '
                'plans filed in a MERIT database that classifies them as deferred '
                'indefinitely. The gas giant is a planet-sized reminder of what the system '
                'was supposed to become and did not.'
            ),
            population=0,
        ),
    ],
    short_description='An abandoned colony at the Hyades\' doorstep -- half-terraformed worlds and empty cities under an enormous amber star.',
    long_description=(
        'Aldebaran was supposed to be a colony. The system was discovered relatively '
        'recently, surveyed, approved for development, and colonised under MERIT\'s '
        'standard programme. Atmospheric processors were deployed on Constance, the primary '
        'world. Settlements were built. A second world, Kelsworth, was prepared for '
        'later phases. A third, Dunmore, was surveyed for industrial development. '
        'later phases. Orbital infrastructure was under construction. The terraforming '
        'was on schedule and the atmosphere was improving.\n\n'
        'Then the outer systems declared independence, and Aldebaran\'s position became '
        'untenable. The system sits one soft jump from Ain and the Hyades cluster -- '
        'an easy transit for any ship class, including the heavy capital vessels that '
        'the Hyades favours. The soft link that had made Aldebaran convenient for '
        'colonisation made it indefensible against the faction next door. MERIT '
        'calculated the cost of fortifying the system against a Hyadean assault, '
        'compared it to the system\'s development value, and made the decision that '
        'strategists make: abandon it. The colonists were evacuated. The equipment was '
        'left behind. The terraforming programme was halted mid-process.\n\n'
        'Aldebaran today is a ghost. Constance\'s atmosphere is half-terraformed -- '
        'breathable in some regions, toxic in others, and slowly reverting without '
        'the processors that were maintaining the progress. The settlements stand '
        'empty, MERIT-standard prefabricated modules deteriorating without '
        'maintenance. The orbital Scaffold drifts above Constance, its docking platforms '
        'dark and its habitat frames open to vacuum. Kelsworth\'s surface is marked '
        'with survey beacons that transmit to no one and landing zones prepared for '
        'colonists who will not arrive. Dunmore\'s mineral wealth sits untouched, a '
        'resource base that MERIT surveyed, planned for, and left for the Hyades to '
        'consider.\n\n'
        'The Hyades patrols the system. The soft jump to Ain makes Aldebaran part of '
        'the Hyadean defensive perimeter, and warships transit the Approach regularly '
        '-- industrial, prosthetic-crewed vessels whose presence is a statement of '
        'control over a system that MERIT abandoned but has not formally surrendered. '
        'Both sides understand Aldebaran\'s significance: it is the most likely route '
        'for a MERIT offensive into Hyadean space, if such an offensive ever comes, '
        'and it is the route the Hyades would use to push into the inner systems if '
        'they ever had the strength. For now, the system sits in the gap between '
        'these possibilities -- empty, half-built, and watched by a faction that did '
        'not build it and a faction that will not finish it, all of it lit by an '
        'enormous amber star that does not care what happens on the worlds it warms.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

HAMAL = System(
    name='Hamal',
    star='Orange giant (K2III), approximately 91 times Sol luminosity',
    population=6_500_000_000,
    distance_to_sol=65.8,
    stellar_objects=[
        StellarObject(
            name='Anworth',
            short_description='The most populous world in the system -- a temperate planet with its own government, its own problems, and its own way of doing things.',
            long_description=(
                'Anworth is the largest and most developed world in Hamal -- a temperate '
                'planet with a breathable atmosphere, broad oceans, and the kind of '
                'conditions that produce a comfortable civilisation without the need for '
                'extraordinary engineering. Three billion people live here under a '
                'parliamentary government that has functioned, with varying degrees of '
                'competence, since the colony\'s founding. The government is democratic, '
                'messy, and entirely Anworth\'s own -- no MERIT oversight, no external '
                'framework, no bureaucratic infrastructure imported from Sol.\n\n'
                'The result is a civilisation that works but does not work as smoothly as '
                'MERIT-governed worlds. The transit systems are adequate but not seamless. '
                'The hospitals are good but unevenly distributed. The schools vary in '
                'quality depending on the district, the funding, and the political '
                'priorities of whoever won the last election. The infrastructure is '
                'maintained but not upgraded on the schedule that MERIT\'s planned economies '
                'would mandate. Anworth has potholes. Anworth has waiting lists. Anworth has '
                'the kind of small, grinding inefficiencies that MERIT\'s systems are '
                'designed to eliminate and that democratic self-governance tends to produce.\n\n'
                'The people of Anworth are aware of the comparison and divided on what to '
                'make of it. Some look at the inner systems and see what they are missing: '
                'the infrastructure, the guaranteed services, the quality of life that MERIT '
                'delivers to its citizens. Others look at the inner systems and see what '
                'they have avoided: the control, the uniformity, the sense that every aspect '
                'of life has been optimised by an authority that does not ask permission. '
                'The debate is the oldest in Hamal\'s politics, and it has never been '
                'resolved because both sides are right.\n\n'
                'Anworth\'s relationship with the other planets in the system is '
                'confederate -- a loose arrangement of mutual recognition, shared trade '
                'agreements, and a collective defence pact that has never been tested. Each '
                'planet governs itself. The confederation coordinates on interstellar trade, '
                'immigration, and the shared question that nobody can answer: why does '
                'MERIT leave them alone?'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Selbridge',
            short_description='A cooler, drier world with a council government and a population that considers itself more self-reliant than Anworth.',
            long_description=(
                'Selbridge is the second planet -- cooler than Anworth, drier, with broad '
                'steppe plains and shallow seas that support a population distributed across '
                'small and mid-sized cities rather than concentrated in large ones. The '
                'government is a council system -- representatives from the major '
                'settlements meeting in a rotating capital, making decisions by consensus '
                'when possible and by vote when necessary. The process is slow. The '
                'residents consider slowness a feature rather than a flaw, because slow '
                'decisions tend to be decisions that everyone can live with.\n\n'
                'Selbridge\'s economy is agricultural and light industrial -- the steppe '
                'plains support grain farming at a scale that feeds the planet and exports '
                'a surplus, and the manufacturing sector produces the goods that the '
                'population needs without the volume or sophistication of MERIT-backed '
                'industry. The technology is a generation behind the inner systems in some '
                'areas and roughly current in others, depending on what the traders bring '
                'in and what the local engineers can maintain. Selbridge does not have the '
                'resources to stay at the cutting edge. It has the resources to stay '
                'functional, and functional is enough.\n\n'
                'Selbridge residents regard Anworth with the mild condescension of rural '
                'people toward urban people everywhere: Anworth is too busy, too political, '
                'too concerned with the question of MERIT. Selbridge prefers to get on with '
                'things. The question of why MERIT leaves them alone is, on Selbridge, less '
                'a political debate than a shrug. They are alone. They are managing. If '
                'MERIT arrives tomorrow, they will deal with it tomorrow.'
            ),
            population=1_600_000_000,
        ),
        StellarObject(
            name='Tarne',
            short_description='A small, warm world with a direct democracy and a fierce independence that makes even Anworth look accommodating.',
            long_description=(
                'Tarne is the innermost habitable world -- a small, warm planet with a thick '
                'atmosphere and a population that is small enough to govern itself by direct '
                'democracy and stubborn enough to insist on doing so. Major decisions are '
                'put to a system-wide vote. Minor decisions are put to a local vote. The '
                'process is cumbersome, inefficient, and produces a population that is '
                'intensely engaged in its own governance in a way that residents of MERIT '
                'systems would find exhausting.\n\n'
                'Tarne\'s independence is the most ideological in the system. Where Anworth '
                'debates the merits of MERIT governance and Selbridge shrugs at the '
                'question, Tarne has made self-governance a core identity. The population '
                'is actively, vocally proud of running their own affairs, and the suggestion '
                'that MERIT could do it better is received not as a policy argument but as '
                'an insult. Tarne\'s representatives in the confederation are the ones who '
                'block any proposal that smells like centralisation, and they block '
                'frequently.\n\n'
                'The planet\'s economy is modest -- fishing, coastal agriculture, and a small '
                'technology sector that punches above its weight because the engineers are '
                'good and the regulatory environment is nonexistent. Tarne is not '
                'prosperous. Tarne is free, and the residents will tell you at length that '
                'the distinction matters.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Copperton',
            short_description='A cold, mineral-rich world with a company-town economy -- the system\'s industrial base, for what it is worth.',
            long_description=(
                'Copperton is the outermost habitable world -- cold, rocky, and rich in the '
                'mineral deposits that the other planets lack. The planet\'s economy is '
                'mining and manufacturing, organised around a handful of large companies '
                'that employ most of the population and exert a degree of influence over '
                'the planetary government that the residents of the other worlds find '
                'uncomfortable. Copperton\'s politics are corporate in a way that Anworth\'s '
                'democracy and Tarne\'s direct governance are not, and the other planets '
                'regard it with a wariness that Copperton\'s representatives find unfair.\n\n'
                'The companies of Copperton are not exploitative in the way that outer-'
                'system industry can be -- there are no Hyades-style economic pressures, no '
                'Antarian pharmaceutical dependencies. The work is hard, the conditions are '
                'cold, and the wages are decent. But the concentration of economic power '
                'in a few hands produces a politics that the other planets find alien, and '
                'the confederation\'s internal tensions are most often between Copperton\'s '
                'corporate pragmatism and Tarne\'s ideological independence, with Anworth '
                'and Selbridge trying to mediate.\n\n'
                'Copperton supplies the raw materials that the rest of the system needs '
                'and imports the food and consumer goods that it cannot produce. The '
                'trade is the confederation\'s strongest bond -- each planet needs what '
                'the others have, and the economic interdependence has held the loose '
                'arrangement together through disagreements that might otherwise have '
                'broken it.'
            ),
            population=900_000_000,
        ),
        StellarObject(
            name='Valence',
            short_description='A large gas giant -- fuel processing run by a joint venture of the four planetary governments, the confederation\'s one shared project.',
            long_description=(
                'Valence is the system\'s gas giant -- a large body in the outer system '
                'whose moons host the fuel processing operations that keep the system\'s '
                'ships running. The fuel operation is the confederation\'s only jointly '
                'managed project: a venture funded and staffed by all four planetary '
                'governments, governed by a committee that meets quarterly and argues '
                'constantly, producing fuel at a rate that is adequate and a cost that '
                'everyone considers too high but nobody can reduce without giving one '
                'planet more control than the others will accept.\n\n'
                'The joint fuel operation is, in miniature, the confederation itself: '
                'functional, inefficient, and sustained by the fact that the alternative '
                '-- each planet running its own operation -- would be worse. The staff are '
                'drawn from all four worlds and develop a cross-planetary camaraderie that '
                'is rare elsewhere in the system. Working on Valence is one of the few '
                'experiences that gives Hamal residents a sense of system-wide identity '
                'rather than planetary identity. The committee that governs the operation '
                'has been described, not inaccurately, as the closest thing Hamal has to '
                'a federal government.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Freepoint',
            short_description='The system\'s main orbital port -- independently operated, serving traffic from the inner systems and occasionally from the outer ones.',
            long_description=(
                'Freepoint is Hamal\'s primary orbital port -- a station in orbit above '
                'Anworth that handles the system\'s interstellar traffic. The station is '
                'independently operated by a consortium that answers to the confederation '
                'rather than to any single planetary government, and this independence is '
                'jealously guarded. Freepoint is the system\'s front door, and controlling '
                'it would give any single planet disproportionate leverage over the others.\n\n'
                'The traffic at Freepoint is modest by inner-system standards. Freighters '
                'arrive from MERIT space carrying manufactured goods and technology that '
                'Hamal cannot produce at competitive quality. Freighters depart carrying '
                'Copperton\'s minerals and Selbridge\'s grain. Occasionally, ships arrive '
                'from less official origins -- traders from the outer systems, independent '
                'operators whose manifests are plausible but vague, and the rare Hyadean '
                'merchant whose presence is legal under Hamal\'s laws if not under MERIT\'s. '
                'Hamal\'s independence means Hamal\'s customs officers enforce Hamal\'s '
                'trade regulations, which are more permissive than MERIT\'s and '
                'deliberately so.\n\n'
                'MERIT vessels dock at Freepoint occasionally -- diplomatic ships, trade '
                'representatives, and the intelligence assets that both sides pretend are '
                'not there. The MERIT personnel who visit Hamal are polite, professional, '
                'and visibly curious about a system that their organisation has chosen, '
                'for reasons nobody has explained, not to govern.'
            ),
            population=55_000_000,
        ),
        StellarObject(
            name='Burnside',
            short_description='A hot inner world -- solar collection arrays operated by Anworth\'s government, a minor source of friction over energy pricing.',
            long_description=(
                'Burnside is a hot, airless inner world with solar collection arrays that '
                'provide supplemental energy to the system. The arrays are operated by '
                'Anworth\'s government, which sells the energy to the other planets at '
                'prices that Anworth considers fair and everyone else considers a tax by '
                'another name. The energy pricing dispute is one of the confederation\'s '
                'perennial minor irritants -- not serious enough to threaten the '
                'arrangement, persistent enough to be raised at every confederal meeting.\n\n'
                'Tarne has repeatedly proposed a joint ownership model for Burnside\'s arrays, '
                'similar to the Valence fuel operation. Anworth has repeatedly declined, '
                'pointing out that Anworth built the arrays, Anworth maintains the arrays, '
                'and Anworth will set the prices. The argument is conducted with the '
                'practised tedium of a disagreement that both sides have memorised. '
                'Selbridge abstains. Copperton votes with whichever side offers the better '
                'energy deal that quarter.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='An independent confederation in MERIT\'s shadow -- four planets governing themselves, for reasons that nobody has satisfactorily explained.',
    long_description=(
        'Hamal is the system that should not be independent. It sits sixty-six '
        'light-years from Sol, at the outer edge of the inner systems, in a position '
        'that MERIT could control if it chose to. MERIT has chosen not to. The '
        'organisation that governs hundreds of billions of people across dozens of '
        'systems has looked at Hamal -- a habitable, developed, strategically '
        'unremarkable system -- and decided to leave it alone. No explanation has been '
        'offered. No justification has been given. MERIT does not explain itself, and '
        'nobody has the authority to demand that it does.\n\n'
        'Theories are plentiful. The distance from Sol and the jump topology make '
        'Hamal expensive to integrate for minimal strategic return. The system\'s '
        'independence serves as a useful buffer or neutral ground. MERIT is conducting '
        'a long-term study of independent governance for comparison with its own model. '
        'The original colonial charter contained a clause that MERIT is legally bound '
        'to honour. A bureaucratic error that nobody has corrected. None of these '
        'theories are confirmed. All of them are discussed, endlessly, on Anworth\'s '
        'political talk shows.\n\n'
        'Six and a half billion people live in Hamal across four habitable worlds, each '
        'with its own government: Anworth\'s parliamentary democracy, Selbridge\'s '
        'consensus council, Tarne\'s combative direct democracy, and Copperton\'s '
        'corporate pragmatism. The four are bound by a loose confederation that '
        'coordinates trade, immigration, and the shared fuel operation at Valence but '
        'leaves governance to each planet. The arrangement is stable, fractious, and '
        'inefficient in the particular way that self-governance without a unifying '
        'authority tends to be. The quality of life is decent but visibly below the '
        'inner-system standard -- the infrastructure is a generation behind, the '
        'services are uneven, and the economic output is modest.\n\n'
        'The people of Hamal are divided on what their independence means. Some see it '
        'as a gift -- the freedom to govern themselves without MERIT\'s control, to '
        'make their own mistakes and solve their own problems. Others see it as '
        'neglect -- a system left to manage with less because MERIT has decided it is '
        'not worth the investment. The debate is Hamal\'s defining political question, '
        'and it cannot be resolved because the one entity that could answer it -- '
        'MERIT -- has declined to do so.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

NUKALI = System(
    name='Nukali',
    star='Orange giant (K2III), approximately 38 times Sol luminosity',
    population=72_000,
    distance_to_sol=73.2,
    stellar_objects=[
        StellarObject(
            name='Leviathan',
            short_description='A massive gas giant just below the threshold for stellar ignition -- the largest body in the system and the anchor for the research station.',
            long_description=(
                'Leviathan is an enormous gas giant -- roughly seventy Jupiter masses, '
                'sitting just below the threshold at which a body accumulates enough mass '
                'to ignite hydrogen fusion and become a star. The planet radiates significant '
                'heat from gravitational compression, glowing a dull reddish-brown in '
                'infrared, and its gravitational influence dominates the system\'s dynamics '
                'in ways that produce unusual effects on local spacetime -- effects that '
                'are precisely why MERIT chose this system for jump drive research.\n\n'
                'The near-stellar mass of Leviathan creates gravitational conditions found '
                'nowhere else in inhabited space. The boundary effects between the gas '
                'giant\'s gravity well and the orange giant star produce spacetime '
                'distortions that are, for reasons the researchers are still working to '
                'fully understand, particularly informative about the nature of jump '
                'points. The distortions are not jump points themselves -- they are too '
                'small, too unstable, and too unpredictable to transit -- but they behave '
                'like jump points in miniature, flickering in and out of existence on '
                'timescales that can be observed, measured, and experimented with. Nowhere '
                'else in the galaxy offers this combination of conditions. Leviathan is a '
                'natural laboratory for the physics that makes interstellar travel possible.'
            ),
            population=0,
        ),
        StellarObject(
            name='Fulcrum Station',
            short_description='MERIT\'s most remote and most restricted research installation -- seventy-two thousand people studying the physics of jump drives.',
            long_description=(
                'Fulcrum Station orbits Leviathan at a distance calculated to place the '
                'station within observation range of the spacetime distortions while keeping '
                'it clear of the gravitational turbulence that makes closer approach '
                'dangerous. The station is small by the standards of inhabited installations '
                '-- seventy-two thousand people in a facility designed for research rather '
                'than habitation. Every system on the station is oriented toward the work: '
                'sensor arrays, computational infrastructure, experimental bays, and the '
                'specialised equipment used to generate, observe, and manipulate the '
                'micro-distortions that Leviathan produces.\n\n'
                'The population is almost entirely researchers and the support staff that '
                'keeps them alive. The researchers are among the most accomplished '
                'physicists in MERIT space -- experts in jump drive theory, spacetime '
                'topology, and the applied engineering of translating theoretical advances '
                'into functional drive improvements. A posting to Fulcrum Station is the '
                'most prestigious assignment in the field. It is also the most isolating. '
                'The station receives supply ships infrequently -- the jump links to Nukali '
                'are difficult, requiring advanced ships and expert pilots, and the transit '
                'is not undertaken casually. Between supply runs, the station is alone in '
                'a way that no other MERIT installation is alone. No traffic passes through '
                'Nukali. No routes run through the system. The only ships that come are the '
                'ones that are coming here, and they are few.\n\n'
                'The isolation is, the researchers insist, part of the appeal. The station '
                'is quiet in a way that permits the kind of deep, sustained focus that the '
                'work demands. There are no distractions. There is no politics, no cultural '
                'noise, no news cycle worth following. There is the station, the gas giant '
                'filling the observation windows with its dark reddish glow, and the work. '
                'The researchers who thrive here are the ones who find that sufficient. The '
                'ones who do not thrive request transfer and are replaced by the next '
                'physicist on the waiting list, because despite the isolation -- or because '
                'of it -- the waiting list for Fulcrum Station is long.\n\n'
                'The research is classified. The advances that Fulcrum Station produces '
                'filter into the broader MERIT economy as improved jump drive designs, '
                'better navigation systems, and the incremental expansions of which jump '
                'points can be safely transited by which classes of ship. These improvements '
                'arrive without attribution. The galaxy benefits from Fulcrum Station\'s '
                'work without knowing the station exists, which is how MERIT prefers it. '
                'The physics of jump drives is a strategic asset, and strategic assets are '
                'not shared.'
            ),
            population=72_000,
        ),
        StellarObject(
            name='Cinderwick',
            short_description='A scorched inner world with no value and no visitors -- the system\'s only rocky body, catalogued and ignored.',
            long_description=(
                'Cinderwick is a small, dense, airless world in a close orbit around the '
                'orange giant -- the only rocky body in a system dominated by the near-'
                'stellar mass of Leviathan. The planet was catalogued during the initial '
                'survey and has not been visited since. It has no resources worth extracting, '
                'no conditions worth studying, and no features worth remarking on. '
                'Cinderwick is a footnote in a system that exists for a single purpose and '
                'does not require footnotes.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Sweepings',
            short_description='A thin field of captured debris in Leviathan\'s orbital space -- ice and rock swept up by the gas giant\'s enormous gravity.',
            long_description=(
                'The Sweepings is a thin field of debris orbiting Leviathan -- fragments of '
                'ice and rock captured by the gas giant\'s immense gravitational pull over '
                'billions of years. The material is sparse, widely distributed, and '
                'scientifically uninteresting in itself. Its value to the station is '
                'incidental: the fragments occasionally pass through the regions where '
                'Leviathan\'s spacetime distortions are most active, and the researchers '
                'observe how the material behaves in those conditions -- whether it '
                'accelerates, decelerates, or briefly disappears from sensors in ways that '
                'suggest the distortions have properties that the instruments cannot '
                'directly measure. The Sweepings is not a resource. It is an accidental '
                'experimental tool, and the researchers are grateful for the accident.'
            ),
            population=0,
        ),
    ],
    short_description='MERIT\'s most remote installation -- a classified jump drive research station orbiting a near-stellar gas giant, seventy-four light-years from Sol.',
    long_description=(
        'Nukali is the end of the line. Seventy-four light-years from Sol, reachable '
        'only through difficult jump links that require advanced ships and expert '
        'pilots, the system sits at the furthest edge of MERIT\'s reach in a corner of '
        'space that no routes pass through and no traffic crosses. The system contains '
        'an orange giant star, a near-stellar gas giant called Leviathan, a scorched '
        'inner rock, and a single MERIT research station housing seventy-two thousand '
        'people. Nothing else.\n\n'
        'Fulcrum Station exists because Leviathan exists. The gas giant\'s enormous '
        'mass -- just below the threshold for hydrogen fusion -- creates gravitational '
        'conditions found nowhere else in inhabited space. The boundary effects between '
        'Leviathan and the star produce spacetime distortions that behave like jump '
        'points in miniature: too small and unstable to transit, but observable and '
        'measurable in ways that full-scale jump points are not. The station studies '
        'these distortions to advance the fundamental physics of jump drives -- work '
        'that translates into improved drive designs, better navigation, and the '
        'incremental expansion of which jump points can be safely used.\n\n'
        'The research is classified. The station is restricted. The supply ships that '
        'make the difficult transit to Nukali are infrequent, and between them the '
        'station is the most isolated inhabited installation in MERIT space. The '
        'researchers who work here are elite physicists who chose the posting for the '
        'unique conditions and the deep, uninterrupted focus that total isolation '
        'provides. The waiting list is long. The work is slow, painstaking, and '
        'strategically vital. The galaxy\'s jump drives improve by fractions of a '
        'percentage point because of advances made at Fulcrum Station, and nobody '
        'outside MERIT\'s classified research division knows that the station or the '
        'system or the work exists. This is intentional. The physics of interstellar '
        'travel is the most strategically sensitive knowledge in the galaxy, and MERIT '
        'keeps it at the end of the longest road it can find.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

HERAK = System(
    name='Herak',
    star='Blue-white main sequence (A5V), approximately 63 times Sol luminosity',
    population=4_200_000_000,
    distance_to_sol=79.7,
    stellar_objects=[
        StellarObject(
            name='Karthane',
            short_description='The Rakshasas\' capital world -- a prosperous planet where the mercenary elite live well and everyone else pays for the privilege of their protection.',
            long_description=(
                'Karthane is a habitable world that was, before the Rakshasas, a moderately '
                'successful colony under loose MERIT governance. Today it is the seat of '
                'power for the most successful mercenary organisation in the galaxy, and '
                'the difference is visible. The Rakshasas\' compound occupies the best real '
                'estate on the planet -- a sprawling complex of residences, training '
                'facilities, command centres, and the administrative infrastructure of an '
                'organisation that has grown from a hired gun outfit into a governing '
                'authority. The compound is luxurious. The Rakshasas take their cut of '
                'everything, and everything adds up.\n\n'
                'Two and a half billion people live on Karthane, and the vast majority are '
                'civilians who have no connection to the Rakshasas beyond the fundamental '
                'one: they pay. The Rakshasas\' governance model is simple. They provide '
                'security -- protection from pirates, from marauders, from the general '
                'lawlessness that plagued the system before they consolidated control -- '
                'and in return they take a percentage of everything. Income, trade, '
                'production, transit. The percentage is negotiable in theory and fixed in '
                'practice, because negotiating with the Rakshasas means negotiating with '
                'people who are better armed than you and who know exactly how much you '
                'can afford to pay.\n\n'
                'The civilian economy functions. The cities are maintained. The hospitals '
                'operate. The schools teach. The Rakshasas are not interested in ruining '
                'their tax base -- a dead economy pays no tribute, and the Rakshasas are '
                'nothing if not pragmatic about revenue. But the extraction is constant and '
                'pervasive. A business on Karthane pays the Rakshasas\' protection fee, pays '
                'the transit levy on its imports, pays the security surcharge on its '
                'exports, and pays the discretionary assessment that arrives whenever the '
                'Rakshasas decide they need additional funding for a project they do not '
                'explain. The fees are not ruinous. They are irritating, unavoidable, and '
                'designed to extract the maximum amount that the economy can bear without '
                'collapsing. The Rakshasas have economists. They know the line.\n\n'
                'The civilians of Karthane have adapted. They factor the Rakshasas\' cut '
                'into their pricing, their budgets, and their expectations. They do not '
                'love their rulers. They do not revolt against them either, because the '
                'memory of what the system was like before the Rakshasas -- the piracy, the '
                'raids, the inability of distant MERIT to protect them -- is still fresh '
                'enough that the alternative to paying is worse than paying. The Rakshasas '
                'understand this calculation perfectly. They made sure the alternative '
                'stayed visible.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Desharn',
            short_description='A cold, industrial world where the Rakshasas maintain their shipyards and the workers learn not to ask who the client is.',
            long_description=(
                'Desharn is the system\'s industrial world -- a cold, rocky planet with '
                'mineral deposits that support a mining and manufacturing economy oriented '
                'largely around shipbuilding and repair. The Rakshasas maintain their '
                'shipyards on Desharn: facilities that build, repair, and refit the fleet '
                'that is simultaneously the system\'s defence force, the Rakshasas\' '
                'instrument of power, and a mercenary navy for hire to anyone who can meet '
                'the price.\n\n'
                'The shipyards take contracts from everyone. MERIT-aligned merchants who '
                'need escort through dangerous space. Outer-system operators who need '
                'repairs without MERIT customs inspecting the cargo. Independent traders '
                'who want armed escort and do not care about the provider\'s moral '
                'character. The Rakshasas do not discriminate by faction or allegiance. '
                'They discriminate by ability to pay, and the prices adjust depending on '
                'how desperate the client is and how much the Rakshasas think they can '
                'squeeze. A merchant who arrives at Desharn with a damaged ship and a hold '
                'full of valuable cargo will pay more than a merchant who arrives with '
                'options, and the Rakshasas\' estimators are very good at assessing which '
                'situation applies.\n\n'
                'The workers on Desharn are civilians -- shipwrights, welders, engineers, '
                'and the skilled tradespeople who build and repair ships. They are well-'
                'paid by the Rakshasas\' standards, because skilled labour is valuable and '
                'the Rakshasas protect their investments. The workers learn early not to '
                'ask questions about the ships they work on: whose weapons systems they are '
                'installing, whose hull they are patching, whose ship was damaged by whom. '
                'The work is the work. The money is good. The questions are someone else\'s '
                'problem.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Tessward',
            short_description='A temperate world settled by people who wanted distance from the Rakshasas -- tolerated because they pay their tribute and cause no trouble.',
            long_description=(
                'Tessward is the system\'s third habitable world -- temperate, pleasant, '
                'and settled primarily by people who wanted to live in Herak without living '
                'under the Rakshasas\' direct presence. The distinction is symbolic more than '
                'practical: Tessward pays the same tribute, follows the same rules, and '
                'operates under the same understanding that the Rakshasas provide security '
                'and the population provides revenue. But the Rakshasas\' compound is on '
                'Karthane, not Tessward, and the day-to-day presence of armed mercenaries '
                'is less visible here.\n\n'
                'The population is agricultural and light industrial -- farming communities '
                'and small manufacturing centres that produce the goods the system needs '
                'and export the surplus. Tessward is the quietest planet in the system and '
                'the one where the Rakshasas\' rule chafes most visibly. The farmers and '
                'manufacturers of Tessward did not choose to be governed by mercenaries. '
                'They chose to live somewhere habitable, and the mercenaries came with the '
                'territory. The tribute payments are made on time and without complaint, '
                'because the Rakshasas have made clear -- not through threats, which would '
                'be crude, but through the conspicuous deployment of patrol ships during '
                'collection periods -- that timely payment is expected.\n\n'
                'Tessward is also where dissenters tend to concentrate. Not active '
                'resistance -- the Rakshasas would crush that quickly and without '
                'hesitation -- but the quiet, persistent unhappiness of people who believe '
                'they deserve better governance and have no mechanism to achieve it. The '
                'Rakshasas monitor Tessward more closely than the population realises and '
                'less closely than the population fears.'
            ),
            population=600_000_000,
        ),
        StellarObject(
            name='The Citadel',
            short_description='The Rakshasas\' orbital fortress -- their command centre, their fleet anchorage, and the place where the deals are struck.',
            long_description=(
                'The Citadel is the Rakshasas\' orbital headquarters -- a heavily armed '
                'station in high orbit above Karthane that serves as the organisation\'s '
                'command centre, its primary fleet anchorage, and the meeting point where '
                'clients negotiate contracts. The station is fortified to a degree that '
                'would be excessive for a commercial installation and appropriate for what '
                'it actually is: the seat of power for an organisation that rules a system '
                'through force and expects to be challenged eventually.\n\n'
                'The Citadel is where the mercenary business happens. Clients arrive -- '
                'inner-system merchants needing escort, outer-system operators needing '
                'muscle, governments and factions needing deniable military force -- and '
                'are received in meeting rooms designed to communicate wealth and power. '
                'The negotiations follow a pattern that repeat clients learn quickly: the '
                'Rakshasas name an initial price that is higher than anyone will pay. The '
                'client negotiates it down. The final price is exactly what the Rakshasas '
                'intended from the start, and the client leaves feeling they struck a '
                'bargain when they have in fact paid exactly what the Rakshasas calculated '
                'they could afford. The organisation has the best negotiators in the '
                'galaxy, because their negotiators are backed by a fleet that the client '
                'can see through the meeting room windows.\n\n'
                'The Rakshasas\' favourite arrangement -- the one their leadership pursues '
                'with undisguised enthusiasm -- is being hired by both sides of a conflict. '
                'This is not betrayal by their standards. The Rakshasas are transparent '
                'about the fact that they will work for anyone who pays. If both sides of '
                'a dispute are willing to pay, the Rakshasas will happily provide escort '
                'to one faction\'s convoy on Monday and the other faction\'s convoy on '
                'Wednesday, and they see no contradiction in this. The contradiction, they '
                'argue, belongs to the clients who hired them knowing full well what they '
                'were buying. The clients, for their part, continue hiring because the '
                'Rakshasas are very good at their jobs and the alternatives are worse.'
            ),
            population=35_000_000,
        ),
        StellarObject(
            name='Blackreach',
            short_description='A frozen outer world where the Rakshasas maintain training camps and the recruits learn the organisation\'s two core values: skill and revenue.',
            long_description=(
                'Blackreach is a frozen outer world -- airless, dark, and hostile in the '
                'way that makes it ideal for military training. The Rakshasas maintain '
                'their primary training installations here: camps where new recruits are '
                'transformed from whatever they were before -- ex-military, ex-criminal, '
                'ex-desperate -- into Rakshasa operatives. The training is brutal, '
                'comprehensive, and focused on two things: combat effectiveness and '
                'commercial awareness. A Rakshasa operative who can fight but cannot '
                'assess a client\'s ability to pay is considered half-trained.\n\n'
                'The recruits come from everywhere. The Rakshasas do not care about '
                'origin, faction, or history. They care about capability and willingness '
                'to follow the organisation\'s rules, which are few and inflexible: you '
                'complete the contract, you deliver what was promised, and you bring the '
                'money home. Operatives who violate contracts are dealt with internally '
                'and severely, because the Rakshasas\' business model depends on the '
                'certainty that a Rakshasa contract will be fulfilled. The reputation is '
                'the product. The violence is the manufacturing process.\n\n'
                'Blackreach also houses the organisation\'s archives -- the records of '
                'every contract fulfilled, every payment received, every client served. '
                'The Rakshasas keep meticulous records. They know who hired them, when, '
                'for what, and how much was paid. This information is itself a source of '
                'leverage -- the knowledge that the Rakshasas know exactly who has '
                'purchased deniable military force and when encourages clients to maintain '
                'good relationships with the organisation. The archives are the Rakshasas\' '
                'insurance policy, and they are stored on Blackreach because Blackreach is '
                'the hardest place in the system to reach uninvited.'
            ),
            population=12_000_000,
        ),
        StellarObject(
            name='Vendmark',
            short_description='A gas giant whose moons host fuel processing -- another revenue stream the Rakshasas control and another fee every ship in the system pays.',
            long_description=(
                'Vendmark is the system\'s gas giant -- a large body in the outer system '
                'with moons that host fuel processing operations. The fuel operation is '
                'Rakshasa-controlled, naturally, because everything in Herak is Rakshasa-'
                'controlled. Ships that refuel at Vendmark pay the Rakshasas\' fuel premium '
                '-- a surcharge on top of the production cost that is not optional and not '
                'negotiable. The premium is calibrated, like all Rakshasa fees, to extract '
                'the maximum the market will bear without driving ships to seek fuel '
                'elsewhere.\n\n'
                'The fuel workers on Vendmark\'s moons are civilians employed by the '
                'Rakshasas under terms that are fair by Herak standards and exploitative '
                'by inner-system standards. The wages are adequate. The conditions are '
                'adequate. The workers have no leverage to demand better because the '
                'Rakshasas own the operation and there is no alternative employer. This is '
                'the Rakshasas\' governance in miniature: functional, extractive, and '
                'sustained by the absence of alternatives.'
            ),
            population=30_000_000,
        ),
    ],
    short_description='A mercenary state -- ruled by the Rakshasas, tolerated by MERIT, and paying for protection whether it wants to or not.',
    long_description=(
        'Herak is what happens when the protectors become the rulers and discover that '
        'ruling pays better. The system sits seventy-nine light-years from Sol, at the '
        'far edge of what was once MERIT\'s loosely held outer territory. Before the '
        'war, Herak was plagued by piracy that distant MERIT could not suppress. A '
        'mercenary group called the Rakshasas filled the gap -- organised, effective, '
        'and willing to do the fighting that MERIT\'s stretched forces could not. They '
        'drove out the pirates. They established security. They also established fees, '
        'levies, surcharges, and the permanent understanding that security is a service '
        'and services cost money.\n\n'
        'As MERIT\'s grip loosened with the outbreak of war, the Rakshasas\' grip '
        'tightened. Today they are the de facto government of a system of four billion '
        'people -- collecting tribute from three inhabited worlds, running the '
        'shipyards, controlling the fuel supply, and hiring out their fleet to anyone '
        'in the galaxy who can meet the price. The Rakshasas fight for MERIT-aligned '
        'clients on Monday and outer-system clients on Wednesday and see no '
        'contradiction. They are transparent about their mercenary nature in a way that '
        'clients find either refreshing or repulsive, depending on how much they are '
        'being charged.\n\n'
        'The Rakshasas are morally simple. They provide a service and they extract '
        'payment. The payment is always the maximum the client can bear. The service '
        'is always delivered as promised, because the reputation is the product and a '
        'broken contract is a broken business model. They extort, they shake down, '
        'they squeeze every deal for every credit it contains, and they do it all with '
        'the professional transparency of people who believe that honest extortion is '
        'not a contradiction in terms. Their clients keep hiring them because the '
        'Rakshasas are very good at what they do and the galaxy does not offer many '
        'alternatives.\n\n'
        'MERIT watches. MERIT has always watched. The Rakshasas know that MERIT logs '
        'every contract, every deployment, every credit that flows through Herak. They '
        'know that when the war ends -- if it ends -- MERIT will come to reassert '
        'control over a system it never formally relinquished. The Rakshasas are '
        'preparing for that day the way they prepare for everything: by making '
        'themselves too useful to discard and too expensive to fight. Whether this '
        'strategy will work against an organisation that governs hundreds of billions '
        'is a question the Rakshasas prefer not to examine too closely. In the '
        'meantime, there are contracts to fulfil and money to collect. The future can '
        'wait. The invoice cannot.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ANGIRAS = System(
    name='Angiras',
    star='Magnetically peculiar blue-white subgiant (A1III-IVp), approximately 240 times Sol luminosity -- unusually strong and complex magnetic field causing sensor and communications interference',
    population=55_000,
    distance_to_sol=82.9,
    stellar_objects=[
        StellarObject(
            name='Sarai',
            short_description='The system\'s only naturally habitable world -- a Rakshasa ground base on a planet that deserves better than the people who claimed it.',
            long_description=(
                'Sarai is the reason the Rakshasas bothered with Angiras. The planet is '
                'naturally habitable -- breathable atmosphere, liquid water, temperate '
                'climate, and the kind of conditions that MERIT\'s colonial planners would '
                'describe as high-value. Under MERIT governance, Sarai would have been '
                'surveyed in detail, assigned a development plan, and colonised over '
                'decades with the careful, methodical approach that produces worlds like '
                'Concord or Taverner. Under the Rakshasas, Sarai got a ground base.\n\n'
                'The base is small, functional, and built with the pragmatic indifference '
                'to aesthetics that characterises everything the Rakshasas construct. '
                'Prefabricated structures arranged around a landing pad, a perimeter fence '
                'that is more about marking territory than providing security, and the '
                'equipment to support a few hundred personnel. The Rakshasas did not come '
                'to Sarai to build a civilisation. They came to plant a flag, establish '
                'a claim, and ensure that nobody else -- MERIT, the outer factions, or '
                'another independent operator -- could claim the system first.\n\n'
                'The personnel on Sarai are a mix of Rakshasa operatives and the civilian '
                'contractors who keep the base running. The operatives rotate through on '
                'short postings -- the base is not a desirable assignment, and the '
                'Rakshasas use it as either a training exercise for junior operatives or a '
                'quiet punishment for those who have annoyed the leadership. The planet '
                'itself is beautiful in the way that undeveloped habitable worlds are '
                'beautiful: untouched landscapes stretching to every horizon, clean air, '
                'a sky unmarked by orbital traffic. The personnel do not comment on the '
                'beauty. They are counting the days until rotation.\n\n'
                'The star\'s magnetic peculiarity affects Sarai more than the base staff '
                'would like. Communications with Herak are unreliable -- the magnetic '
                'interference disrupts signals in unpredictable bursts that the technicians '
                'have learned to work around but cannot eliminate. Sensors behave '
                'erratically, producing ghost returns and blind spots that shift with the '
                'star\'s magnetic cycle. The Rakshasas regard the interference as a '
                'nuisance. It is also, they have noted, a defensive advantage: anyone '
                'approaching Angiras has the same sensor problems, which means a small '
                'defending force can hide more effectively than it could in a normal system.'
            ),
            population=35_000,
        ),
        StellarObject(
            name='Redoubt',
            short_description='A small Rakshasa orbital station -- part depot, part garrison, part claim marker in orbit above the habitable world.',
            long_description=(
                'Redoubt is the Rakshasas\' orbital presence in Angiras -- a small station '
                'in orbit above Sarai that serves as supply depot, communications relay, '
                'and the token garrison that backs up the territorial claim. The station is '
                'modest -- a handful of docking berths, cargo storage, crew quarters for '
                'the garrison, and the sensor arrays that attempt to monitor the system\'s '
                'approaches through the magnetic interference.\n\n'
                'The garrison is a few ships and a few thousand personnel -- enough to '
                'deter casual intrusion and insufficient to repel a serious assault. The '
                'Rakshasas are aware of this. The station\'s real defence is the jump link '
                'back to Herak, which allows reinforcement from the Rakshasas\' main fleet '
                'if the system is threatened. The response time is not instant, but the '
                'Rakshasas have calculated that anyone interested in taking Angiras would '
                'need to bring enough force to hold it against a Rakshasa counterattack, '
                'and at present nobody considers the system worth that investment.\n\n'
                'Redoubt\'s secondary function is as a waypoint for Rakshasa operations '
                'in the surrounding space. The system\'s position beyond MERIT\'s effective '
                'reach makes it useful as a staging area for contracts in the deep outer '
                'regions -- a place to refuel, resupply, and brief crews before they '
                'depart for jobs that the Rakshasas would prefer not to stage from Herak, '
                'where MERIT\'s observation is more attentive.'
            ),
            population=8_000,
        ),
        StellarObject(
            name='Korith',
            short_description='A cold world with a thin, toxic atmosphere -- habitable with terraforming that the Rakshasas cannot provide and have not attempted.',
            long_description=(
                'Korith is the system\'s second rocky world -- cold, with a thin atmosphere '
                'heavy in carbon dioxide and trace sulphur compounds that make it '
                'uninhabitable without enclosed habitats or extensive terraforming. The '
                'Rakshasa survey team assessed Korith as a viable terraforming candidate '
                'and filed the assessment with the same pragmatic realism that characterises '
                'the organisation: the planet could be terraformed, but terraforming '
                'requires the kind of sustained industrial investment that MERIT can '
                'mobilise and the Rakshasas cannot. The report recommended monitoring and '
                'reassessment in fifty years.\n\n'
                'Korith is unvisited since the survey. The planet orbits in the outer '
                'habitable zone, its toxic atmosphere undisturbed, its surface a landscape '
                'of frozen plains and sulphur-stained rock that no human has walked on '
                'since the survey team collected their samples and left.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dern',
            short_description='A hot, dense world closer to the star -- mineral-rich but requiring atmospheric work that is decades away at best.',
            long_description=(
                'Dern is a hot, dense world in a close orbit -- surface temperatures too '
                'high for unprotected habitation but within the range that atmospheric '
                'engineering could moderate over time. The survey identified significant '
                'mineral deposits that would make the planet industrially valuable if '
                'developed. The Rakshasas noted the deposits with interest and the '
                'development requirements with realism. Mining Dern would require enclosed '
                'habitats, heat-rated equipment, and the logistical capacity to sustain '
                'operations on a hostile surface -- investment that would be trivial for '
                'MERIT and is beyond the Rakshasas\' current means.\n\n'
                'The minerals sit in the ground. The Rakshasas have claimed them. Claiming '
                'something and being able to extract it are different problems, and the '
                'Rakshasas are practical enough to know which one they have solved.'
            ),
            population=0,
        ),
        StellarObject(
            name='Pallash',
            short_description='A frozen outer world at the system\'s edge -- surveyed by drone, too remote and too cold to warrant even a Rakshasa claim marker.',
            long_description=(
                'Pallash is the outermost body in the system -- a frozen world beyond the '
                'habitable zone with no atmosphere worth mentioning and surface temperatures '
                'that the survey drones measured but that nobody plans to experience in '
                'person. The Rakshasas\' survey of Pallash was conducted entirely by '
                'automated systems: drones launched from Redoubt, flown to the planet, and '
                'returned with data that confirmed what the initial scans suggested -- '
                'ice, rock, and nothing worth the fuel it would cost to visit.\n\n'
                'Pallash is included in the Rakshasas\' territorial claim because the claim '
                'covers the entire system, but nobody pretends that the claim on Pallash '
                'means anything. If someone wanted Pallash, the Rakshasas would probably '
                'sell it to them.'
            ),
            population=0,
        ),
    ],
    short_description='A Rakshasa frontier claim -- one habitable world, a small base, and a flag planted in a system the Rakshasas cannot yet develop.',
    long_description=(
        'Angiras is a Rakshasa possession in the loosest sense. The system was '
        'discovered after the war began, when the Rakshasas\' growing independence in '
        'Herak gave them the freedom to explore the jump link that connected their '
        'territory to an uncharted system eighty-one light-years from Sol. What they '
        'found was a magnetically peculiar star, one naturally habitable world, two '
        'candidates for terraforming, and the kind of opportunity that the Rakshasas '
        'are constitutionally unable to ignore: unclaimed real estate.\n\n'
        'The Rakshasas launched a series of minor expeditions -- not the full-scale '
        'colonial programmes that MERIT deploys but the lean, pragmatic operations '
        'that a mercenary organisation can manage. A ground base on Sarai, the '
        'habitable world. A small orbital station called Redoubt. Survey teams to '
        'assess the other worlds. A flag, a claim, and the minimum presence required '
        'to make the claim credible.\n\n'
        'Fifty-five thousand people live in Angiras, almost all of them Rakshasa '
        'personnel or contractors. The system is not a colony. It is a territorial '
        'marker backed by a token garrison, sustained by supplies from Herak, and '
        'valuable primarily as a strategic asset: a system beyond MERIT\'s reach that '
        'the Rakshasas control, with a habitable world that could support a real '
        'population if the Rakshasas ever develop the capacity to colonise it properly. '
        'That capacity does not exist today. The Rakshasas are mercenaries, not '
        'colonial administrators, and the skills that make them effective at the former '
        'do not translate to the latter.\n\n'
        'The star\'s magnetic peculiarity adds a layer of difficulty. Communications '
        'are unreliable. Sensors are erratic. Ghost returns and blind spots shift '
        'unpredictably with the magnetic cycle. The Rakshasas have adapted -- they '
        'regard the interference as both a nuisance and a defensive advantage, since '
        'any attacker would be equally blinded. Angiras is a system held by a thin '
        'presence in difficult conditions, claimed by an organisation that knows the '
        'claim exceeds its current ability to develop, and maintained because the '
        'Rakshasas understand that owning something you cannot yet use is better than '
        'letting someone else own it.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALPHECCA = System(
    name='Alphecca',
    star='Eclipsing binary: Alphecca A (A0V blue-white, 60 times Sol luminosity) and Alphecca B (G5V yellow dwarf), with the companion periodically passing in front of the primary and dimming the system\'s light',
    population=0,
    distance_to_sol=75.0,
    stellar_objects=[
        StellarObject(
            name='Pember',
            short_description='A hot, dense inner world -- mineral surveys returned average results that did not justify the cost of extraction at this distance from Sol.',
            long_description=(
                'Pember is the innermost planet -- a small, dense, airless world baked by '
                'the bright primary star. The mineral surveys conducted during the initial '
                'assessment were thorough and disappointing. The deposits are real but '
                'unremarkable -- nothing present in concentrations that would justify the '
                'logistics of mining seventy-five light-years from the nearest industrial '
                'centre. The same minerals exist in greater concentration in systems that '
                'are easier to reach, and the economics do not favour Pember under any '
                'projection the surveyors could construct. The planet was catalogued, '
                'scored, and filed as not viable.'
            ),
            population=0,
        ),
        StellarObject(
            name='Tarrant',
            short_description='A rocky world in the habitable zone -- technically terraformable, practically not worth the centuries of investment.',
            long_description=(
                'Tarrant sits in the habitable zone and was the survey team\'s primary '
                'candidate for colonisation. The planet has surface water, a nitrogen-heavy '
                'atmosphere, and conditions that fall within the broad parameters of '
                'terraformable. The assessment was detailed: atmospheric composition, soil '
                'chemistry, hydrological mapping, climate modelling. The conclusion was '
                'that Tarrant could be made habitable in approximately three to four '
                'centuries of sustained terraforming effort.\n\n'
                'Three to four centuries is a long time. Other candidate worlds closer to '
                'established systems offer better conditions with less work. Tarrant\'s '
                'atmosphere is heavier in sulphur compounds than the survey team would have '
                'liked, the soil chemistry is hostile to Earth-derived agriculture without '
                'extensive remediation, and the orbital eccentricity produces temperature '
                'swings that would complicate any long-term development plan. None of these '
                'are insurmountable. All of them are expensive. The survey report concluded '
                'with the phrase that colonial planners use when a world is not bad enough '
                'to reject outright and not good enough to recommend: further assessment '
                'deferred pending strategic review. No strategic review has been scheduled.'
            ),
            population=0,
        ),
        StellarObject(
            name='Denning',
            short_description='A cold, dry world outside the habitable zone -- geologically dead and of no interest to anyone.',
            long_description=(
                'Denning is a cold, dry, geologically dead world orbiting outside the '
                'habitable zone. The atmosphere is thin carbon dioxide. The surface is '
                'ancient rock and dust that has not changed in billions of years. The '
                'survey team spent two days on Denning, collected samples that confirmed '
                'the orbital scans, and departed. The report is four pages long, which is '
                'short for a planetary survey and communicates the team\'s assessment more '
                'effectively than any recommendation could.'
            ),
            population=0,
        ),
        StellarObject(
            name='Tessun',
            short_description='A mid-sized gas giant -- standard hydrogen-helium composition, no unusual features, no reason to establish fuel processing this far from anywhere.',
            long_description=(
                'Tessun is a mid-sized gas giant with a standard hydrogen-helium atmosphere '
                'and a small system of icy moons. The atmospheric surveys confirmed what '
                'the initial scans suggested: the gas giant is unremarkable. The hydrogen '
                'could be processed for fuel, as it could at any of thousands of gas giants '
                'across the galaxy, but fuel processing requires infrastructure and '
                'infrastructure requires demand and there is no demand for fuel in a system '
                'that nobody visits. Tessun was assessed, found adequate, and ignored.'
            ),
            population=0,
        ),
        StellarObject(
            name='Barivel',
            short_description='A large gas giant in the outer system -- impressive to look at, with a ring system, but offering nothing that justifies a presence.',
            long_description=(
                'Barivel is the system\'s largest body -- a gas giant roughly four times '
                'Jupiter\'s mass with a visible ring system and a retinue of moons that '
                'the survey team catalogued with professional thoroughness. The rings are '
                'broad, bright, and composed of water ice and silicate dust. They would be '
                'a spectacular sight from the surface of any of Barivel\'s larger moons. '
                'Nobody has stood on those moons. The survey was conducted by orbital scan '
                'and drone, and the data was filed alongside everything else in Alphecca: '
                'catalogued, scored, and insufficient to justify development.\n\n'
                'Barivel\'s moons include two that are large enough to host enclosed '
                'habitats if anyone wanted to build them. The survey team noted this in '
                'the same tone they noted everything else: factual, complete, and aware '
                'that the information would not change anyone\'s mind about the system.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dregs',
            short_description='A small, frozen outer body -- the last thing the survey team catalogued before leaving the system for good.',
            long_description=(
                'Dregs is a small, frozen body in the outer system -- ice and rock, no '
                'atmosphere, no distinguishing features. The survey team catalogued it last, '
                'gave it a name that suggests their enthusiasm had waned by that point in '
                'the mission, and departed the system. Dregs has not been visited since. '
                'It orbits the eclipsing binary in the dark outer reaches of a system that '
                'humanity assessed, found wanting, and left alone.'
            ),
            population=0,
        ),
        StellarObject(
            name='Calter',
            short_description='A small, airless body in an eccentric orbit between the inner and outer system -- noted by the survey for its unusual trajectory and nothing else.',
            long_description=(
                'Calter is a small rocky body in a highly eccentric orbit that carries it '
                'from the inner system out past the gas giants over the course of its long '
                'year. The orbital dynamics interested the survey team briefly -- the '
                'eccentricity suggests a gravitational interaction with one of the gas '
                'giants at some point in the system\'s history -- but the body itself is '
                'unremarkable. Airless, cratered, and too small to retain anything useful. '
                'Calter is a footnote in a system of footnotes.'
            ),
            population=0,
        ),
        StellarObject(
            name='Soraya',
            short_description='A second world in the habitable zone -- closer to viable than Tarrant, but with a rotational period that makes it impractical.',
            long_description=(
                'Soraya is the system\'s other habitable-zone world, and in many respects '
                'it is a better candidate than Tarrant: the atmosphere is closer to '
                'breathable, the soil chemistry is less hostile, and the climate models '
                'project a more stable long-term environment. The survey team was cautiously '
                'optimistic until they completed the rotational analysis.\n\n'
                'Soraya\'s day is ninety-three standard hours long. The planet rotates '
                'so slowly that the day side bakes and the night side freezes, with a '
                'habitable band in the twilight zones that shifts with the seasons. The '
                'thermal cycling stresses any structure built on the surface and makes '
                'conventional agriculture impractical outside enclosed environments. '
                'Colonisation is possible -- tidally influenced worlds have been settled '
                'elsewhere -- but the engineering requirements are significant, and with '
                'Tarrant also available in the same system and closer to conventional '
                'parameters, neither world alone justifies the investment and both together '
                'do not add up to a compelling case. Soraya was scored marginally above '
                'Tarrant in the final assessment. Marginally above insufficient is still '
                'insufficient.'
            ),
            population=0,
        ),
    ],
    short_description='A surveyed, empty system -- eight worlds catalogued, scored, and deemed not worth the investment of settling.',
    long_description=(
        'Alphecca is a system that humanity visited, assessed, and decided to leave '
        'alone. The survey was conducted during the expansion era with the standard '
        'thoroughness that MERIT\'s colonial assessment teams apply to every candidate '
        'system: orbital mechanics mapped, atmospheric compositions analysed, mineral '
        'surveys completed, climate models run, habitability scores calculated. The '
        'results were underwhelming across the board.\n\n'
        'Eight bodies orbit the eclipsing binary. Two sit in the habitable zone -- '
        'Tarrant and Soraya -- and both are technically terraformable, but Tarrant\'s '
        'atmosphere is sulphur-heavy with hostile soil chemistry and Soraya\'s '
        'ninety-three-hour day produces thermal cycling that makes surface habitation '
        'impractical. Two gas giants offer standard fuel processing potential that no '
        'one needs this far from established routes. The rocky bodies are mineral-poor '
        'or geologically dead or both. Nothing in Alphecca is bad enough to be '
        'interesting and nothing is good enough to be useful.\n\n'
        'The eclipsing binary adds a final note of atmospheric indifference. The '
        'companion star periodically passes in front of the primary, dimming the '
        'system\'s light in a regular cycle that would be dramatic on any inhabited '
        'world -- a sun that visibly fades and brightens, a sky that darkens and '
        'recovers. On the uninhabited worlds of Alphecca, the eclipses play to an '
        'empty audience. The light dims. The light returns. Nothing notices.\n\n'
        'Alphecca\'s survey data sits in MERIT\'s colonial planning archive alongside '
        'thousands of other assessed systems that did not make the cut. The data is '
        'complete, well-organised, and unread. If the galaxy ever runs out of better '
        'options, Alphecca will be there -- eight unremarkable worlds orbiting a star '
        'that periodically dims, waiting for someone to decide that insufficient is '
        'good enough. That day has not come.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

GENUBI = System(
    name='Genubi',
    star='Wide binary: Genubi A (A3IV blue-white subgiant) and Genubi B (F4V yellow-white dwarf), separated widely enough that each star hosts its own planetary system',
    population=850_000,
    distance_to_sol=77.2,
    stellar_objects=[
        StellarObject(
            name='Vashan',
            short_description='A hot desert world orbiting Genubi A -- arid plains and sand seas patrolled by enormous aerial predators riding the thermal currents.',
            long_description=(
                'Vashan is a desert world -- hot, dry, and covered in vast sand seas, '
                'eroded mesa formations, and hardpan plains that stretch unbroken to the '
                'horizon. The atmosphere is breathable. The surface water is scarce, '
                'concentrated in deep aquifers and seasonal oases that form the focal '
                'points of the ecosystem. The biology is built around water conservation: '
                'the plant life is succulent and deep-rooted, storing water in fleshy '
                'tissues and defended by chemical irritants that deter grazers. The animal '
                'life is adapted to the heat -- armoured, slow-metabolised, and active '
                'primarily during the cooler hours.\n\n'
                'The apex predator on Vashan is the roc -- named by the first survey team '
                'for the mythical bird, and the name is earned. The roc is an enormous '
                'aerial organism with a wingspan exceeding twelve metres, riding the '
                'powerful thermal currents that the desert heat generates. The thermals on '
                'Vashan are strong and constant, and the roc exploits them with an '
                'efficiency that allows it to remain airborne for days, circling at altitude '
                'with almost no muscular effort, scanning the ground below with eyesight '
                'that the researchers estimate can resolve prey-sized movement from three '
                'kilometres up. The dive is steep, fast, and silent -- the roc folds its '
                'wings and drops, striking with talons large enough to close around a human '
                'torso. The research habitats on Vashan are reinforced against aerial '
                'assault, which is a sentence that the engineers who designed them never '
                'expected to write.\n\n'
                'The habitats are small, enclosed, and scattered across the planet in '
                'clusters of two or three -- a few hundred installations housing a few '
                'tens of thousands of researchers and tourists. From orbit, there is no '
                'visible sign of human presence. The habitats are designed to leave no '
                'footprint: waste is processed internally, power is drawn from solar '
                'collection panels that are small and low-profile, and the surrounding '
                'terrain is undisturbed. The researchers study the rocs and the broader '
                'ecosystem with the care of people who are aware that the ecosystem is '
                'studying them back.'
            ),
            population=25_000,
        ),
        StellarObject(
            name='Tessara',
            short_description='An ocean world orbiting Genubi A -- a global sea of complex marine biology dominated by vast colonial predators.',
            long_description=(
                'Tessara is a water world -- a global ocean with no dry land above sea '
                'level, broken only by shallow reef systems and volcanic seamounts that '
                'approach the surface. The ocean is deep, warm, and teeming with life at '
                'every depth. The biology is complex: photosynthetic organisms form vast '
                'floating mats on the surface that support grazing species, which support '
                'predators, which support larger predators, in a food chain that extends '
                'from the sunlit surface to the abyssal trenches.\n\n'
                'The apex predator on Tessara is the drift sovereign -- not a single '
                'organism but a colonial entity. The drift sovereign is a network of '
                'interconnected organisms spanning up to a kilometre across, linked by '
                'fibrous tissue that coordinates the colony\'s movement and feeding. The '
                'individual units are small -- tentacled, bioluminescent, and venomous -- '
                'but the colony acts as one. A drift sovereign feeds by drawing the net '
                'of its connected bodies together, enclosing a volume of ocean and '
                'consuming everything within it. The process is slow and visible from the '
                'surface: a circle of bioluminescent light tightening on the water, the '
                'ocean within it churning as trapped organisms attempt to escape. The '
                'researchers describe it as beautiful and horrifying in equal measure.\n\n'
                'The habitats on Tessara are floating platforms anchored to seamounts, '
                'each housing a small team of marine biologists. The platforms are designed '
                'to be mistaken by the local biology for inert debris -- low-emission, '
                'non-reflective, and chemically neutral. The precaution is not paranoia. '
                'A drift sovereign that identified a habitat as prey would envelop it, '
                'and while the structure would survive, the experience of being inside '
                'a contracting ring of venomous tentacles for the hours it would take the '
                'colony to determine the platform was inedible is one the researchers '
                'prefer to avoid.'
            ),
            population=18_000,
        ),
        StellarObject(
            name='Korresh',
            short_description='A frozen world orbiting Genubi A -- ice plains and subglacial oceans where the apex predator is patient enough to wait years for a meal.',
            long_description=(
                'Korresh is an ice world -- a planet at the outer edge of Genubi A\'s '
                'habitable zone where the surface is covered in kilometres-thick ice sheets '
                'broken by geothermal vents that create localised melt zones. The biology '
                'is concentrated around these vents: microbial mats in the heated water, '
                'grazing organisms that crop the mats, and a sparse but functional food '
                'chain that extends into the subglacial ocean beneath the ice. The surface '
                'biology is limited to the vent zones, where warm air and liquid water '
                'create oases of life in an otherwise frozen landscape.\n\n'
                'The apex predator on Korresh is the pale vigil -- a large, slow, '
                'white-furred organism that inhabits the ice plains between vent zones. '
                'The pale vigil is an ambush predator with a metabolism so low that it can '
                'remain motionless on the ice for months, conserving energy, waiting for '
                'organisms migrating between vent zones to pass within striking range. The '
                'creature\'s patience is extraordinary: research teams have documented '
                'individuals remaining in a single position for over two standard years '
                'before making a kill. The strike, when it comes, is fast enough that '
                'the research team\'s motion sensors could not track it on first '
                'observation. The pale vigil is white, nearly invisible on the ice, and '
                'large enough that a standing human would reach its shoulder.\n\n'
                'The habitats on Korresh are built into the ice near the vent zones -- '
                'subsurface installations heated by the same geothermal energy that '
                'sustains the biology. The researchers study the subglacial ocean through '
                'bore holes and the surface biology through observation posts that are '
                'reinforced against the pale vigils, which have shown persistent interest '
                'in the warm air that escapes from habitat ventilation systems. The '
                'interest is predatory. The reinforcement is necessary.'
            ),
            population=15_000,
        ),
        StellarObject(
            name='Selvane',
            short_description='A jungle world orbiting Genubi A -- dense canopy forests covering every landmass, stalked by massive predators that move through the understory.',
            long_description=(
                'Selvane is a warm, wet world -- dense jungle covering every landmass, '
                'fed by heavy rainfall and a thick, humid atmosphere that supports growth '
                'rates the researchers describe as aggressive. The canopy is multi-layered: '
                'a high canopy of enormous broad-leafed organisms sixty metres above the '
                'ground, a mid-canopy of climbing and epiphytic species, and a dark, dense '
                'understory where the light that reaches the forest floor is a dim green '
                'fraction of what falls on the canopy above. The biology is the most '
                'diverse of the four wildlife worlds -- the warm, wet conditions support a '
                'density of species that the cataloguing teams have not finished '
                'documenting after decades of work.\n\n'
                'The apex predator on Selvane is the thane -- a massive ground predator '
                'that combines the bulk and power of the largest terrestrial herbivores with '
                'the predatory instincts of a big cat. The thane stands four metres at the '
                'shoulder and weighs several tonnes, moving through the dense understory '
                'with a silence that its size should make impossible. The body is heavily '
                'muscled, low-slung, and built for explosive acceleration over short '
                'distances -- the thane does not chase prey through the forest. It stalks '
                'close through the dim understory, using the darkness and its mottled '
                'colouring to close the distance, and then charges. The impact of a '
                'several-tonne predator hitting at full sprint is enough to shatter the '
                'trunk of a mid-sized tree. The jaws are broad and powerful, designed for '
                'crushing rather than cutting. Nothing on Selvane contests a thane\'s kill.\n\n'
                'The habitats on Selvane are built into the mid-canopy -- platform '
                'structures integrated into the forest at a height that keeps them above '
                'the thane\'s reach. The creatures are powerful but not climbers -- their '
                'mass prohibits it. The positioning is a compromise: the forest floor is '
                'thane territory and too dangerous for sustained human presence. The high '
                'canopy is exposed and structurally uncertain. The mid-canopy is safer, '
                'though researchers report that hearing a thane move through the darkness '
                'below -- the creak of vegetation, the sudden silence of other animals -- '
                'is an experience that never becomes routine.'
            ),
            population=30_000,
        ),
        StellarObject(
            name='Ember',
            short_description='A volcanic world orbiting Genubi A -- too hostile for complex life, but its biology is related to everything else in the system.',
            long_description=(
                'Ember is a geologically hyperactive world -- volcanic, unstable, with an '
                'atmosphere choked with sulphur dioxide and surface temperatures that '
                'fluctuate wildly with the eruption cycle. Complex life has not developed '
                'here. What has developed is a robust extremophile biosphere: microbial '
                'communities in the hot springs, chemical-metabolising organisms in the '
                'volcanic vents, and a sparse but functional ecosystem that survives '
                'conditions that would sterilise most biology.\n\n'
                'The extremophile organisms on Ember share the same genetic markers as '
                'the complex biology on Vashan, Tessara, Korresh, and Selvane. The same '
                'base-pair structures. The same molecular signatures. Microbes clinging to '
                'volcanic vents on a world that barely supports life are related, '
                'demonstrably and unmistakably, to twelve-metre rocs and four-metre thanes '
                'and kilometre-wide drift sovereigns on worlds millions of kilometres away. '
                'Nobody knows why.\n\n'
                'Ember\'s habitats are the most heavily shielded in the system -- enclosed '
                'installations on stable rock formations, rated for volcanic activity and '
                'atmospheric toxicity. The research teams here are small, quiet, and very '
                'careful about what they put in their published reports.'
            ),
            population=5_000,
        ),
        StellarObject(
            name='Callum',
            short_description='A temperate world orbiting Genubi B -- the system\'s administrative centre and the only place in Genubi that resembles a normal settlement.',
            long_description=(
                'Callum orbits the secondary star, Genubi B, and is the system\'s only '
                'conventional settlement. The planet is temperate and habitable -- a '
                'modest world with no native biology, colonised as the administrative base '
                'for the research operations on the Genubi A worlds. The population is '
                'small: administrators, logistics staff, the medical personnel who support '
                'the research teams, and the transit operators who ferry researchers and '
                'tourists between the two stellar systems.\n\n'
                'Callum is deliberately conventional. After spending weeks in a floating '
                'habitat on Tessara\'s global ocean or a canopy platform on Selvane '
                'listening to thanes move through the darkness below, the '
                'researchers return to Callum for rest, resupply, and the simple comfort '
                'of a settlement where nothing is trying to eat them. The town -- there is '
                'one, it is small -- has the character of a research campus: quiet, '
                'functional, and populated by people whose conversations at dinner are '
                'about predator behaviour and genetic markers.\n\n'
                'Callum also hosts the system\'s primary research archive -- the repository '
                'of data collected from all five Genubi A worlds, including the genetic '
                'analyses that document the shared ancestry mystery. The archive is '
                'accessible to the broader scientific community and has attracted '
                'xenobiologists, geneticists, and evolutionary theorists from across the '
                'inner systems, all drawn by the same unanswered question: how did related '
                'biology end up on five separate worlds?'
            ),
            population=750_000,
        ),
        StellarObject(
            name='Tremont',
            short_description='A cold, rocky world orbiting Genubi B -- surveyed and unused, held in reserve for future development if the system\'s population ever warrants it.',
            long_description=(
                'Tremont is a cold, rocky world in a wide orbit around Genubi B -- thin '
                'atmosphere, frozen surface, and conditions that would require enclosed '
                'habitats or terraforming for any significant habitation. The world was '
                'surveyed during the initial assessment and designated as a future '
                'development site if Genubi\'s population ever grows to the point where '
                'Callum cannot accommodate it. Given that the system\'s entire purpose is '
                'low-impact research and tourism, and that the population is measured in '
                'hundreds of thousands rather than millions, Tremont is likely to remain '
                'empty for a very long time.'
            ),
            population=0,
        ),
    ],
    short_description='A system of alien ecosystems sharing a common ancestor across five worlds -- the galaxy\'s greatest biological mystery, observed from the smallest possible footprint.',
    long_description=(
        'Genubi is the most biologically significant system in the galaxy, and it is '
        'treated with a care that reflects this. Five worlds orbiting Genubi A harbour '
        'thriving alien ecosystems -- desert, ocean, ice, jungle, and volcanic -- each '
        'with complex biology adapted to radically different conditions. Each world '
        'has its own apex predators: the thermal-riding rocs of Vashan, the kilometre-wide '
        'colonial drift sovereigns of Tessara, the impossibly patient pale vigils of '
        'Korresh, the massive thanes of Selvane. The biology is alien, '
        'dangerous, and spectacular.\n\n'
        'What makes Genubi unique is the shared ancestry. The genetic markers are '
        'unmistakable: the biology on all five worlds descends from a common ancestor. '
        'The same base-pair structures, the same encoding conventions, the same '
        'molecular signatures, present in organisms ranging from Ember\'s extremophile '
        'microbes to Selvane\'s thanes. Something seeded these worlds with '
        'related biology billions of years ago, and the organisms evolved independently '
        'on each world into the ecosystems that exist today. Nobody knows how. The '
        'researchers have theories. They are careful about which ones they publish.\n\n'
        'The human presence is deliberately minimal. A few hundred small habitats are '
        'scattered across each of the five worlds, each housing fewer than a hundred '
        'people -- researchers and tourists who observe the ecosystems with a care '
        'designed to leave no footprint. From orbit, there is no visible sign that '
        'humans are present. The system\'s administrative centre is Callum, a small '
        'settlement orbiting the secondary star Genubi B, where the researchers return '
        'to rest and the data from five worlds is archived and analysed. Eight hundred '
        'and fifty thousand people live in Genubi. The biology they study has been '
        'here for billions of years. The researchers are visitors, and they know it.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

MIZAR = System(
    name='Mizar',
    star='Quadruple system: two spectroscopic binary pairs (Mizar Aa/Ab and Mizar Ba/Bb), all A-type main sequence stars',
    population=3_800_000_000,
    distance_to_sol=78.2,
    stellar_objects=[
        StellarObject(
            name='Garran',
            short_description='The capital world -- a temperate planet of two billion people who live normal lives eleven months of the year and host the galaxy during race season.',
            long_description=(
                'Garran is a temperate, habitable world that would be a perfectly ordinary '
                'mid-tier colony if not for what happens in its sky every year. Two billion '
                'people live on Garran. They farm, they manufacture, they raise children, '
                'they commute to work. The cities are functional and reasonably attractive. '
                'The economy is diversified. The schools are decent. For eleven months of '
                'the standard year, Garran is a normal planet where normal people live '
                'normal lives and nobody outside the system thinks about it.\n\n'
                'During race season, the galaxy thinks about it. The Mizar Circuit is the '
                'most prestigious spacecraft race in the inner systems, and Garran is '
                'where the teams are based, the support infrastructure is housed, and the '
                'spectators arrive in numbers that strain the planet\'s hospitality '
                'industry to its limits. The cities closest to the orbital launch '
                'facilities transform during race season: hotels fill, prices spike, bars '
                'and restaurants extend their hours, and the streets fill with visitors '
                'wearing team colours and discussing engine specifications with the '
                'passionate expertise of people who have never flown anything faster than '
                'a passenger shuttle.\n\n'
                'The relationship between the permanent residents and the racing industry '
                'is the same relationship that any city with a major sporting event '
                'maintains: complicated, profitable, and occasionally annoying. The racing '
                'brings money. It also brings crowds, noise, disrupted transit schedules, '
                'and the particular arrogance of wealthy racing enthusiasts who treat the '
                'planet as a venue rather than a home. The residents take the money, endure '
                'the inconvenience, and wait for the season to end. Then they have their '
                'planet back for another eleven months, and the quiet is appreciated.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Circuit',
            short_description='The racing course itself -- a mapped route through the system\'s natural hazards that kills competitors with reliable regularity.',
            long_description=(
                'The Mizar Circuit is not a constructed track. It is a mapped route through '
                'the system\'s natural features -- a course that threads through asteroid '
                'fields, skims gas giant atmospheres, passes through the gravitational '
                'turbulence between the binary pairs, and demands that the pilots navigate '
                'hazards that were not designed to be navigated at racing speeds.\n\n'
                'The course changes every season. The race organisers adjust the route to '
                'account for orbital drift, new debris, and the shifting gravitational '
                'landscape of a quadruple star system where nothing stays in the same place '
                'for long. The constants are the major hazard points that give the circuit '
                'its character: the Narrows, where the route passes between two large '
                'asteroids with a gap that is technically wider than a racing ship but does '
                'not feel like it at speed. The Churn, where the gravitational interaction '
                'between the two binary pairs creates turbulence that throws ships off '
                'course. The Skimmer Run, where the route dips into the upper atmosphere '
                'of the system\'s gas giant, using inertial resonators to survive '
                'conditions that would destroy an unshielded craft. And the Whip, the '
                'final sprint through open space where the ships reach their maximum '
                'velocity and the margins between first and second place are measured in '
                'fractions of a second.\n\n'
                'The racing ships are lightweight, overpowered, and built around the '
                'largest inertial resonator that the frame can carry. The resonator is the '
                'key technology: it protects the ship and pilot from the forces that the '
                'course inflicts, but a resonator sized for a racing ship operates at the '
                'edge of its capacity, and a miscalculation -- too deep into the gas giant, '
                'too close to an asteroid, too much turbulence in the Churn -- overwhelms '
                'the resonator and kills the pilot. Deaths are not common. They are not '
                'rare. The circuit has claimed pilots every season for as long as it has '
                'operated, and the danger is part of what makes it the most watched '
                'sporting event in the galaxy.'
            ),
            population=0,
        ),
        StellarObject(
            name='Tessering',
            short_description='A cooler second world -- industrial and agricultural, supplying Garran and quietly resentful of being known only as the other planet in the racing system.',
            long_description=(
                'Tessering is the system\'s second habitable world -- cooler than Garran, '
                'further from the stars, with a thinner atmosphere and broad temperate '
                'plains that support agriculture and light industry. The population is '
                'smaller than Garran\'s and the economy is oriented toward supplying the '
                'system\'s needs: food, manufactured goods, and the industrial base that '
                'Garran\'s service-heavy economy does not provide.\n\n'
                'Tessering has the particular grievance of a place that is overshadowed by '
                'its sibling\'s fame. The planet is functional, productive, and entirely '
                'invisible to anyone outside the system. When people hear Mizar, they think '
                'of the racing. When they think of the racing, they think of Garran. '
                'Tessering feeds and supplies the system that makes the racing possible and '
                'receives none of the recognition. The residents have developed the dry '
                'humour of people who are accustomed to being the answer to a trivia '
                'question that nobody asks.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='The Proving Ground',
            short_description='An asteroid field where the racing teams test their ships year-round -- debris, wreckage, and the constant sound of engines pushing limits.',
            long_description=(
                'The Proving Ground is a section of the system\'s inner asteroid field that '
                'the racing teams have claimed, informally but effectively, as their '
                'year-round testing area. The field is dense enough to provide realistic '
                'navigation challenges and sparse enough that a skilled pilot can push a '
                'ship to racing speeds without certain death. The distinction between these '
                'two conditions is narrower than non-pilots would find comfortable.\n\n'
                'The teams maintain small facilities on the larger asteroids -- workshops, '
                'hangars, and the telemetry equipment that records every test run in detail '
                'that the engineers find fascinating and the pilots find invasive. The '
                'Proving Ground is where the technology of the racing ships is developed: '
                'new resonator configurations, hull geometries, engine modifications, and '
                'the incremental refinements that separate a competitive ship from an '
                'also-ran. The work is year-round, obsessive, and funded by sponsors '
                'whose investment in a racing team exceeds the GDP of some smaller '
                'colonies. The teams guard their testing data with a secrecy that MERIT\'s '
                'intelligence services would recognise and respect.'
            ),
            population=5_000_000,
        ),
        StellarObject(
            name='Pellerin',
            short_description='The system\'s gas giant -- notable primarily because the racing circuit skims its upper atmosphere in the most dangerous section of the course.',
            long_description=(
                'Pellerin is a large gas giant in the outer system -- a body that would be '
                'unremarkable in any other system but is famous in Mizar because the racing '
                'circuit\'s Skimmer Run passes through its upper atmosphere. The run is the '
                'most technically demanding section of the course: pilots descend into '
                'Pellerin\'s atmosphere at speeds where the inertial resonator is operating '
                'at near-maximum capacity, navigating turbulent gas layers while maintaining '
                'a trajectory that brings them back out on the correct heading for the next '
                'section. A pilot who enters too deep burns time climbing out. A pilot who '
                'enters too shallow gains no advantage from the gravitational slingshot '
                'that makes the run worthwhile. A pilot who misjudges the resonator\'s '
                'capacity does not come out at all.\n\n'
                'Pellerin\'s moons host fuel processing operations and a small population '
                'of workers who are thoroughly accustomed to the annual spectacle of racing '
                'ships screaming through the gas giant\'s atmosphere at velocities that '
                'the fuel workers consider inadvisable. The workers watch the races from '
                'observation platforms on the inner moons. They have opinions about the '
                'pilots. The opinions are not always flattering.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='Startline',
            short_description='The system\'s orbital port and the race\'s ceremonial starting point -- a transit hub that becomes a stadium once a year.',
            long_description=(
                'Startline is Mizar\'s primary orbital station -- a large installation in '
                'orbit above Garran that handles the system\'s interstellar traffic and, '
                'during race season, serves as the ceremonial starting point for the Mizar '
                'Circuit. The station was built for transit and expanded for spectacle: the '
                'original commercial sections are functional and unremarkable, while the '
                'race-season additions -- observation galleries, broadcast facilities, VIP '
                'suites, and the enormous starting gantry where the racing ships are '
                'presented before launch -- are designed to impress.\n\n'
                'During the off-season, Startline is a normal orbital port. During race '
                'season, it is the most watched location in the galaxy outside Sol. The '
                'broadcast feeds from Startline\'s cameras reach every inhabited system, '
                'and the moment when the racing ships launch from the gantry -- engines '
                'flaring, resonators activating, accelerating toward the first hazard point '
                '-- is one of the most viewed events in the annual calendar. The station\'s '
                'permanent staff navigate the transition between quiet port and galactic '
                'stadium with the practised efficiency of people who have done it many '
                'times and would prefer to do it fewer.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='The Monument',
            short_description='A large asteroid at the circuit\'s midpoint -- where the memorial to the pilots who died on the course is maintained.',
            long_description=(
                'The Monument is a large asteroid at the approximate midpoint of the racing '
                'circuit -- a body that the course passes near but does not require pilots '
                'to navigate. The asteroid hosts the Circuit Memorial: a structure built '
                'into the rock that records the name of every pilot killed on the course '
                'since the race\'s founding. The list is long. The memorial is maintained '
                'by the racing federation and visited by teams, families, and the occasional '
                'pilgrim who makes the trip for reasons that are personal rather than '
                'sporting.\n\n'
                'The Monument is also where retired racing ships are traditionally docked -- '
                'championship-winning craft that are too famous to scrap and too obsolete '
                'to fly. They are anchored to the asteroid\'s surface in a growing '
                'collection that has become an unofficial museum of racing technology. The '
                'oldest ships in the collection are centuries old, their resonator '
                'technology primitive by modern standards, their frames built for speeds '
                'that a current racing ship would consider warm-up. The progression from '
                'old to new tells the story of the technology as clearly as any textbook.'
            ),
            population=0,
        ),
    ],
    short_description='Home of the Mizar Circuit -- the galaxy\'s most prestigious spacecraft race, run through a system of natural hazards by pilots who accept the risk.',
    long_description=(
        'Mizar is a quadruple star system -- two binary pairs whose gravitational '
        'interaction creates a dynamic, shifting orbital environment full of natural '
        'hazards. Asteroid fields, gravitational turbulence zones, and a gas giant '
        'whose atmosphere can be skimmed by a ship with a good resonator and a pilot '
        'with steady nerves. In a rational galaxy, these would be navigation hazards '
        'to be avoided. In the galaxy that actually exists, they are the Mizar Circuit '
        '-- the most prestigious spacecraft race in the inner systems, broadcast to '
        'every inhabited world, watched by billions, and fatal often enough that the '
        'memorial asteroid at the course\'s midpoint adds names every season.\n\n'
        'Three point eight billion people live in Mizar, and most of them have nothing '
        'to do with the racing. Garran is a temperate world of two billion that '
        'functions as a normal colony eleven months of the year and transforms into a '
        'galactic venue during race season. Tessering supplies the system and resents '
        'being overlooked. The economy is diversified, the infrastructure is adequate, '
        'and the quality of life is comparable to any mid-tier inner system. The racing '
        'is what makes Mizar famous, but it is not what makes Mizar function.\n\n'
        'The racing ships are lightweight frames built around oversized inertial '
        'resonators -- the technology that protects the ship and pilot from forces '
        'that would otherwise be lethal. The resonators operate at the edge of their '
        'capacity, and the margin between a fast run and a fatal one is the pilot\'s '
        'ability to judge exactly how much the resonator can take. Too deep into the '
        'gas giant. Too close to an asteroid. Too much turbulence in the gravitational '
        'churn between the binary pairs. The resonator fails and the pilot dies. This '
        'happens. The pilots accept it. The spectators watch because of it. The '
        'ethicists debate it. The racing continues.\n\n'
        'During the off-season, Mizar is quiet. The teams test their ships in the '
        'Proving Ground. The sponsors calculate their returns. The residents of Garran '
        'enjoy having their planet back. And somewhere in the system, the memorial on '
        'the Lantern waits for the next season and the next names to be added to a list '
        'that has grown every year since the race began.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

REGULUS = System(
    name='Regulus',
    star='Hot blue-white subgiant (B8IV), approximately 288 times Sol luminosity, extremely rapid rotator near the limit of structural integrity',
    population=450_000_000,
    distance_to_sol=79.3,
    stellar_objects=[
        StellarObject(
            name='Crucet',
            short_description='A rocky world where advanced materials are forged using the star\'s radiation -- the galaxy\'s premier facility for extreme-exposure manufacturing.',
            long_description=(
                'Crucet is a dense, airless world close enough to Regulus that the '
                'radiation flux on the day side would kill an unprotected human in seconds. '
                'The installations are on the night side, bored deep into the crust, '
                'shielded by kilometres of rock. The workers never see the star. They are '
                'not here for the star. They are here for what the star can do.\n\n'
                'The manufacturing facilities on Crucet produce materials that cannot be '
                'produced anywhere else. Certain advanced composites, radiation-hardened '
                'alloys, and exotic crystalline structures require exposure to stellar '
                'radiation at intensities that no other inhabited system provides. The raw '
                'materials are positioned on the day side in automated arrays, exposed to '
                'Regulus\'s output for precisely calibrated durations, and retrieved by '
                'shielded drones. The process cannot be replicated artificially -- the '
                'energy cost of generating equivalent radiation in a laboratory exceeds '
                'the value of the materials produced. Regulus provides it for free. The '
                'star is the factory.\n\n'
                'The workforce on Crucet rotates on six-month contracts. The facilities '
                'are functional and comfortable in the way that offshore industrial '
                'installations are comfortable: the food is good, the quarters are '
                'private, the recreational facilities are adequate, and nobody pretends '
                'they are here for any reason other than the pay. The pay is excellent. '
                'It has to be. Living in a bunker on the dark side of a rock orbiting a '
                'star that would vaporise you if you stepped outside is not something '
                'people do for career fulfilment.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Temper',
            short_description='An orbital material science facility -- where researchers develop the processes that Crucet\'s factories execute at scale.',
            long_description=(
                'Temper is an orbital research station in a carefully maintained orbit that '
                'keeps it permanently in the shadow of Crucet -- shielded from the star by '
                'the planet itself. The station houses the material science researchers who '
                'develop the manufacturing processes that Crucet\'s factories execute. The '
                'work is experimental: testing new material compositions, calibrating '
                'exposure durations, and developing the techniques that translate Regulus\'s '
                'raw radiative output into products that the rest of the galaxy needs.\n\n'
                'The researchers on Temper are on the same rotational contracts as the '
                'factory workers on Crucet, though the culture is different. The factory '
                'workers count the days until rotation. The researchers count the days '
                'until their next experimental run. The work is genuinely pioneering -- '
                'material science under stellar radiation at this intensity is a field '
                'that exists only because Regulus exists -- and the researchers who come '
                'here are driven by the opportunity rather than the pay. They still leave '
                'when their contracts end. Nobody stays in Regulus longer than they must.'
            ),
            population=12_000_000,
        ),
        StellarObject(
            name='Ardent',
            short_description='A second industrial world -- specialising in high-energy chemical synthesis and pharmaceutical production that requires stellar radiation at scale.',
            long_description=(
                'Ardent is the system\'s second industrial world -- smaller than Crucet, '
                'further from the star, but still well within the radiation environment that '
                'makes Regulus unique. Where Crucet focuses on materials -- alloys, '
                'composites, crystalline structures -- Ardent focuses on chemistry. Certain '
                'high-energy chemical synthesis processes, particularly in advanced '
                'pharmaceuticals and industrial catalysts, require sustained radiation '
                'exposure at intensities that are ruinously expensive to produce '
                'artificially. A laboratory on Earth can synthesise a microgram of a '
                'radiation-catalysed compound for the cost of a small ship. Ardent\'s '
                'facilities produce the same compound in tonnes.\n\n'
                'The pharmaceutical output of Ardent supplies a significant fraction of the '
                'inner systems\' demand for advanced medical compounds -- drugs that cannot '
                'be manufactured at scale anywhere else because nowhere else has a star '
                'willing to provide the energy for free. The irony is not lost on the '
                'workforce: the system that is most hostile to human life produces the '
                'medicines that keep humans alive. The workers on Ardent rotate on the same '
                'six-month contracts as everyone else. The facilities are underground, '
                'shielded, and identical in character to Crucet\'s -- bunkers where the '
                'work happens and the star is a concept rather than a visible presence.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Respite',
            short_description='The system\'s only habitation station -- where the rotational workforce lives between shifts and waits for the transport home.',
            long_description=(
                'Respite is an orbital station in the outer system, far enough from Regulus '
                'that the radiation levels are manageable with standard shielding. The '
                'station is the system\'s social centre, such as it is -- the place where '
                'the rotational workforce spends its off-shift hours, where the transports '
                'from the inner systems dock, and where the incoming workers meet the '
                'outgoing workers in a perpetual handover that is the closest thing Regulus '
                'has to a cultural ritual.\n\n'
                'The station is comfortable. MERIT invested in the facilities because '
                'retention on Regulus contracts depends on the quality of life between '
                'shifts. The bars are good. The food is varied. The recreational facilities '
                'are better than the system\'s size would suggest. There is a persistent, '
                'system-wide joke that Respite has the best entertainment per capita in the '
                'galaxy, because nobody here has anything to do except work and wait, and '
                'MERIT has ensured that the waiting is pleasant.\n\n'
                'No children live on Respite. No families. The station\'s population is '
                'adults on fixed contracts -- engineers, factory workers, researchers, '
                'logistics staff, and the service personnel who keep the station running. '
                'They arrive, they work, they socialise on Respite during their off-shifts, '
                'and they leave when their contract ends. Some come back for a second '
                'contract. A few come back for a third. Nobody has done more than four. '
                'The pay is excellent but the human need for sky, weather, and a horizon '
                'that is not a bulkhead eventually wins.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Sable',
            short_description='A frozen outer world -- the only body in the system far enough from the star to be approached without heavy shielding.',
            long_description=(
                'Sable is a cold, rocky world in the outer system -- the only body in '
                'Regulus that can be approached by a standard ship without radiation '
                'hardening. The planet is frozen, airless, and geologically dead. It hosts '
                'a small logistics depot that receives supply shipments from the inner '
                'systems and stages them for distribution to Crucet, Ardent, Temper, and Respite. '
                'The depot is automated with a minimal human staff who rotate on the same '
                'contract system as everyone else in Regulus.\n\n'
                'Sable is the first and last thing that workers see when they arrive and '
                'depart. The transports from the inner systems dock at Sable\'s depot, '
                'and the workers transfer to shielded shuttles for the journey inward '
                'toward Crucet and Respite. The view from Sable is Regulus in the distance '
                '-- a blue-white point that is visibly brighter than any star should be, '
                'bright enough to cast sharp shadows on Sable\'s frozen surface even at '
                'this distance. The incoming workers look at it and understand what they '
                'have signed up for. The outgoing workers do not look.'
            ),
            population=3_000_000,
        ),
        StellarObject(
            name='The Scorch',
            short_description='The inner system -- a volume of space so irradiated that unshielded electronics fail within hours and unshielded biology within minutes.',
            long_description=(
                'The Scorch is the local name for the inner system -- the volume of space '
                'close enough to Regulus that the radiation environment exceeds the '
                'tolerance of standard ship shielding. Entering the Scorch requires '
                'radiation-hardened vessels with specialised hull plating, and even '
                'hardened vessels accumulate exposure that limits their operational time. '
                'The automated drones that service the day-side exposure arrays are designed '
                'for the Scorch. Nothing else is.\n\n'
                'The Scorch is where the star\'s intensity becomes visceral. Pilots of '
                'hardened shuttles running cargo to Crucet\'s day-side arrays describe the '
                'experience: the hull temperature climbing despite the shielding, the '
                'radiation alarms sounding at levels that would be emergency thresholds '
                'anywhere else and are operating norms here, the star filling the forward '
                'viewport not as a point but as a disc, blue-white and furious, visibly '
                'oblate from its insane rotation, radiating with an intensity that the '
                'human eye cannot process even through the viewport\'s filters. The pilots '
                'do their runs, deliver their cargo, and return to the dark side of Crucet '
                'with relief they do not bother to hide. Nobody gets used to the Scorch. '
                'The star does not permit familiarity.'
            ),
            population=0,
        ),
    ],
    short_description='A star too fierce to live under -- nearly half a billion rotational workers manufacturing materials and compounds that only Regulus can produce at scale.',
    long_description=(
        'Regulus is not a place to live. It is a place to work. The star is a B-type '
        'subgiant -- 288 times Sol\'s luminosity, spinning so fast it is visibly oblate, '
        'radiating with an intensity that makes every other bright star in the inner '
        'systems look gentle by comparison. The inner system is a radiation hazard that '
        'destroys unshielded electronics in hours and unshielded biology in minutes. '
        'The outer system is merely hostile. Nothing about Regulus invites habitation.\n\n'
        'Nearly half a billion people work in Regulus on rotational contracts -- six '
        'months in, six months out, no exceptions. They are here because the star '
        'enables things that cannot be done elsewhere. The manufacturing facilities on '
        'Crucet produce advanced materials that require stellar radiation at '
        'intensities no other inhabited system provides. The chemical synthesis '
        'facilities on Ardent produce pharmaceuticals and industrial catalysts in '
        'tonnes that laboratories elsewhere can only manage in micrograms. The material '
        'science researchers on Temper develop processes that exist only because this '
        'star exists. The work is valuable. The conditions are brutal. The pay '
        'compensates.\n\n'
        'There is no culture in Regulus. No families, no children, no traditions that '
        'accumulate over generations. The population turns over completely every six '
        'months. The workers arrive at Sable, transfer to shielded shuttles, spend '
        'their contracts in underground bunkers on Crucet and Ardent or aboard '
        'Respite station, and leave when their time is up. Some return for another '
        'contract. Nobody has '
        'done more than four. The human need for sky and weather and a sun that does '
        'not kill eventually wins, and the workers return to worlds where they can '
        'step outside without dying.\n\n'
        'Regulus is the galaxy\'s reminder that not every star is a home. Some stars '
        'are furnaces, and furnaces are useful but they are not kind. The materials '
        'forged here strengthen hulls across the inner systems. The medicines '
        'synthesised here treat conditions that no other facility can address at scale. '
        'It is technically possible to do this work elsewhere -- in specialised '
        'laboratories that cost more to build and operate than the materials they '
        'produce are worth. Regulus does it at industrial scale because the star '
        'provides the energy for free. The half-billion workers who rotate through make '
        'it all possible and are glad to leave when it is over. Regulus takes what it '
        'is given and gives back what it is asked for and does not care about the '
        'people in between. It is a star. It does not care about anything.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)


MEGREZ = System(
    name='Megrez',
    star='White main sequence (A3V), approximately 14 times Sol luminosity',
    population=5_000_000_000,
    distance_to_sol=81.4,
    stellar_objects=[
        StellarObject(
            name='Vantage',
            short_description='The capital world -- three billion people who came here for reasons they do not discuss, living in a culture built on the principle of not asking.',
            long_description=(
                'Vantage is a temperate, habitable world that is pleasant enough to live on '
                'and unremarkable enough that nobody would choose it over a dozen other '
                'inner-system colonies unless they had a specific reason to be at a dead '
                'end. Three billion people live on Vantage, and a disproportionate number '
                'of them arrived from somewhere else and do not volunteer where or why.\n\n'
                'The culture on Vantage is shaped by this. There is a social code, '
                'unwritten but universally understood, that you do not ask a person about '
                'their past. Not as a rule of politeness but as a condition of belonging. '
                'A newcomer who arrives on Vantage and settles in a district and finds work '
                'is accepted on the basis of who they are now, and the question of who they '
                'were before is left unanswered unless they choose to answer it. Some do. '
                'Most do not. The result is a civilisation of people who know their '
                'neighbours\' names and habits and preferences and nothing about their '
                'histories, and who consider this normal.\n\n'
                'Vantage is not lawless. MERIT\'s authority applies and the laws are '
                'enforced. But the enforcement has a particular character that reflects the '
                'population\'s values: the police investigate crimes committed on Vantage. '
                'They do not investigate the histories of the people who live here. Warrants '
                'from other systems are technically valid but practically difficult to '
                'execute, because the population is uncooperative with inquiries that feel '
                'like someone reaching into the dead end to drag a person back to a life '
                'they left. The police understand this. Many of them came here for the same '
                'reasons as everyone else.\n\n'
                'The cities on Vantage are functional, mid-density, and deliberately '
                'anonymous. The architecture does not make statements. The streets are '
                'clean but not distinctive. The neighbourhoods are the kind of places where '
                'a person can live for decades without being memorable, which is exactly '
                'what many of the residents want. Vantage is a city of people who are not '
                'hiding -- hiding implies pursuit -- but who have chosen to stop being '
                'whoever they were and start being someone the galaxy does not keep track '
                'of.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='Merrin',
            short_description='A cooler second world -- smaller, quieter, and where people go when even Vantage feels too crowded and too connected.',
            long_description=(
                'Merrin is the system\'s second habitable world -- cooler, smaller, with '
                'a thinner atmosphere and a population that chose the dead end\'s dead end. '
                'If Vantage is where you go to disappear from the galaxy, Merrin is where '
                'you go to disappear from Vantage. The settlements are small and widely '
                'spaced. The population is sparser. The don\'t-ask culture is even more '
                'pronounced -- on Merrin, people do not just avoid asking about your past. '
                'They avoid asking about you at all unless you initiate the conversation.\n\n'
                'The economy on Merrin is agricultural and self-sufficient in a way that '
                'Vantage is not. The farmers and smallholders who make up the bulk of the '
                'population produce what they need and trade the surplus locally. The '
                'connection to the rest of the galaxy is thin -- goods arrive through '
                'Vantage, filtered through the single jump point, and Merrin is the last '
                'stop on the chain. The residents prefer it this way. The further from the '
                'jump point, the further from whatever they left behind.\n\n'
                'Merrin has a reputation within the system as the place where the most '
                'determined disappearers end up -- people whose need for anonymity goes '
                'beyond a fresh start and into something deeper. The reputation is not '
                'entirely fair. Many Merrin residents are simply people who like farming on '
                'a quiet world and have no particular secrets. But enough of them do that '
                'the reputation persists, and the residents do not correct it because the '
                'reputation discourages visitors.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Inkwell',
            short_description='A dark outer world -- cold, barely habitable, and home to the people who want to be as far from the jump point as physically possible.',
            long_description=(
                'Inkwell is a cold, dark world on the outer edge of the habitable zone -- '
                'thin atmosphere, limited surface water, and conditions that require '
                'enclosed habitats for permanent habitation. The population is small and '
                'lives in scattered settlements that are difficult to reach and easy to '
                'overlook. This is the point.\n\n'
                'The people on Inkwell are the ones for whom Vantage was not remote enough '
                'and Merrin was not quiet enough. The settlements are self-sustaining to '
                'the greatest degree the residents can manage -- hydroponic food production, '
                'recycled water and atmosphere, minimal imports. The less they depend on '
                'the supply chain from the jump point, the less connected they are to the '
                'galaxy they left. Some settlements on Inkwell go months without contact '
                'with the rest of the system. The residents describe this as independence. '
                'An outside observer might describe some of them as people who are running '
                'from something that exists only in their own assessment of themselves.\n\n'
                'MERIT\'s presence on Inkwell is nominal. A customs officer visits the '
                'larger settlements on a quarterly schedule. The visits are brief, polite, '
                'and accomplish nothing, because the settlements contain people who have no '
                'outstanding warrants and are committing no crimes beyond the crime of '
                'wanting to be left alone, which is not a crime at all.'
            ),
            population=25_000_000,
        ),
        StellarObject(
            name='The Gate',
            short_description='The system\'s orbital port at the single jump point -- the only way in and out, and the place where old identities are quietly left behind.',
            long_description=(
                'The Gate is Megrez\'s only orbital port -- a station positioned at the '
                'system\'s single jump point that handles all incoming and outgoing traffic. '
                'There is no other way in or out. Every person who has ever arrived in '
                'Megrez has passed through the Gate, and the station\'s character reflects '
                'this.\n\n'
                'The incoming traffic is steady: passenger transports arriving from the '
                'connecting system, carrying people whose reasons for coming to a dead-end '
                'system vary but share a common thread. Some are visibly nervous. Some are '
                'visibly relieved. Some are blank-faced in the way of people who have made '
                'a decision and are not yet sure it was the right one. The Gate\'s staff '
                'process them efficiently and without curiosity. The customs inspection is '
                'perfunctory -- checking for prohibited goods, not for prohibited pasts.\n\n'
                'The outgoing traffic is smaller. People leave Megrez less frequently than '
                'they arrive, and those who do leave often do so quietly, having decided '
                'that the dead end was not far enough or that the thing they were running '
                'from was inside them rather than behind them. The Gate processes departures '
                'with the same professional indifference as arrivals. The staff have seen '
                'every kind of arrival and every kind of departure. They do not judge. '
                'Judging would be unprofessional, and it would also be hypocritical. Many '
                'of them took the job because it was on the right side of the jump point.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Pallister',
            short_description='A gas giant whose moons host fuel processing -- the system\'s one industrial operation, run by people who value the quiet as much as the work.',
            long_description=(
                'Pallister is a mid-sized gas giant in the outer system with moons that '
                'host the system\'s fuel processing operations. The fuel is consumed '
                'internally -- Megrez does not export anything in significant quantity, and '
                'the fuel production is calibrated to the system\'s own modest needs. The '
                'workers on Pallister\'s moons are the same mix of people as everywhere '
                'else in Megrez: competent, private, and uninterested in discussing their '
                'previous employment.\n\n'
                'The fuel operation is the system\'s closest thing to heavy industry, and '
                'it is modest by any standard. Megrez\'s economy is not oriented toward '
                'production or export. The economy exists to sustain the population that '
                'lives here, and the population lives here for reasons that have nothing '
                'to do with the economy. Pallister\'s fuel workers understand this. They '
                'are here because the moons are quiet, the work is steady, and nobody on '
                'a gas giant\'s moon in a dead-end system asks where you worked before.'
            ),
            population=20_000_000,
        ),
        StellarObject(
            name='Seren',
            short_description='A hot inner world -- automated solar collection and mineral extraction, visited only by maintenance crews who appreciate the solitude.',
            long_description=(
                'Seren is a small, dense inner world with solar collection arrays and '
                'automated mineral extraction. The operations are small-scale -- sufficient '
                'for the system\'s internal needs and no more. The maintenance crews who '
                'visit are drawn from Vantage\'s population and rotate on short assignments '
                'that are popular despite the harsh conditions, because a maintenance '
                'rotation on Seren is the most solitary posting available in a system that '
                'already values solitude. The crews describe the work as peaceful. They are '
                'alone with the machines and the star, and for some of them that is exactly '
                'what they need.'
            ),
            population=2_000_000,
        ),
    ],
    short_description='The dead end -- a system with one jump point in and out, where five billion people live quiet lives and do not discuss how they got here.',
    long_description=(
        'Megrez is the end of the line. The system has a single jump point connecting '
        'it to the rest of the inner systems -- one way in, one way out, no through-'
        'traffic, and no strategic significance that would draw attention from MERIT or '
        'anyone else. The system is a few jumps from Sol, far from the contested '
        'borders, and utterly unimportant in every strategic, economic, and political '
        'calculation that matters. This is why five billion people live here.\n\n'
        'Megrez is where people go to disappear. Not in the dramatic sense -- not '
        'fugitives evading justice, though some of those exist. In the quieter sense: '
        'people who want a fresh start, who have debts they cannot repay, marriages '
        'that ended badly, careers that collapsed, reputations that became '
        'unrecoverable, or simply lives that they no longer wanted. They pass through '
        'the Gate -- the system\'s single orbital port at the jump point -- and arrive '
        'on Vantage or Merrin or, for the most determined, Inkwell, and they begin '
        'again. The culture they enter does not ask who they were. The culture cares '
        'only about who they are now.\n\n'
        'The don\'t-ask principle is Megrez\'s defining characteristic. It is not law. '
        'It is not policy. It is the social consensus of a population that is largely '
        'composed of people who came here to leave something behind and who extend to '
        'others the courtesy they want for themselves. Neighbours know each other\'s '
        'names and habits and nothing about their histories. The police investigate '
        'crimes committed in the system and do not investigate the pasts of the people '
        'who live here. Warrants from other systems are technically valid and '
        'practically unenforceable, because the population closes ranks around the '
        'principle that what happened before the jump point is not Megrez\'s business.\n\n'
        'MERIT\'s control is loose by design or by disinterest -- the distinction is '
        'unclear and the result is the same. The system is not lawless. The laws apply. '
        'But the particular flavour of enforcement is shaped by a population that '
        'values privacy above almost everything else, and MERIT has decided that a '
        'dead-end system of five billion quiet, self-governing people who cause no '
        'trouble is not worth the cost of closer oversight. Megrez asks nothing of the '
        'galaxy. The galaxy, for the most part, returns the favour.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

KALINAN = System(
    name='Kalinan',
    star='Blue-white subgiant (A1IV), approximately 55 times Sol luminosity, eclipsing binary',
    population=12_000_000_000,
    distance_to_sol=81.1,
    stellar_objects=[
        StellarObject(
            name='Vorenn',
            short_description='The most populous world in the system -- fiercely proud, absolutely not the capital, and home to cities where every neighbourhood is a declaration of superiority.',
            long_description=(
                'Vorenn is the most populous planet in Kalinan, and calling it the capital '
                'would start a fight. Kalinan has no capital. No planet, no city, no '
                'settlement would tolerate another being designated as more important than '
                'itself. The system\'s governance is deliberately, painstakingly distributed '
                'across every world so that no single location can claim primacy. The '
                'Ministry of Trade is headquartered on Tessandre. The Ministry of '
                'Agriculture is on Pellamy. The Ministry of Defence is on Keswick. The '
                'Ministry of Industry is on Vorenn, which Vorenn considers the most '
                'important ministry and every other planet considers a transparent attempt '
                'to claim status by other means.\n\n'
                'The distributed governance produces inefficiency that would horrify MERIT\'s '
                'administrators. A process that would be handled by a single office in any '
                'other system is instead a chain of administrators across multiple worlds. '
                'A permit application begins on one planet, is processed on a second, '
                'reviewed on a third, and approved on a fourth, with each link in the chain '
                'considering itself the crucial step and the others mere busywork. The '
                'transit time between worlds alone adds days to processes that should take '
                'hours. The citizens do not object. The inefficiency is the price of '
                'equality, and equality -- the certainty that no planet, no city, no '
                'neighbourhood is subordinate to any other -- is the one value that '
                'overrides everything else in Kalinan.\n\n'
                'Walking through a city on Vorenn is an experience in competitive display. '
                'Every neighbourhood has its own flag, its own anthem, its own founding '
                'story, and its own conviction that it is the finest neighbourhood in the '
                'finest city on the finest planet in the finest system in the galaxy. The '
                'flags hang from every building. The neighbourhood boundaries are marked '
                'with archways and murals celebrating local achievements -- the best baker, '
                'the oldest park, the most successful graduate, the cleanest street. Cross '
                'an intersection and the flags change, the murals change, and the local '
                'pride announces itself with renewed intensity. Each neighbourhood is in '
                'quiet, relentless competition with its neighbours -- not through conflict '
                'but through display. Better-maintained facades. More impressive public art. '
                'Larger flags. The competition escalates gently and perpetually, and the '
                'result is cities that are impeccably maintained, obsessively decorated, and '
                'exhausting to walk through if you are not accustomed to being surrounded '
                'by declarations of excellence at every turn.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Tessandre',
            short_description='The second world -- warmer, louder, and convinced that its culture is more authentically Kalinan than anything Vorenn can produce.',
            long_description=(
                'Tessandre is the system\'s second most populous world -- warmer than Vorenn, '
                'with lush subtropical regions and a population that considers itself more '
                'authentically Kalinan than any other planet. Tessandre hosts the Ministry '
                'of Trade, which it considers the ministry that actually generates '
                'prosperity, unlike Vorenn\'s Ministry of Industry which merely processes '
                'things that Tessandre\'s trade arrangements made available.\n\n'
                'The trade agreements with MERIT are displayed in Tessandre\'s Ministry of '
                'Trade -- framed, illuminated, and described as masterworks of diplomatic '
                'negotiation. The agreements are standard MERIT integration provisions, '
                'reworded just enough to avoid the language of subordination. MERIT\'s '
                'negotiators drafted them in an afternoon. Kalinan\'s negotiators spent '
                'months and consider the result a triumph. Both sides are satisfied.\n\n'
                'Tessandre\'s neighbourhood pride rivals Vorenn\'s in intensity but differs '
                'in expression. Where Vorenn\'s neighbourhoods compete through maintenance '
                'and display, Tessandre\'s compete through celebration -- festivals, street '
                'performances, public feasts that each neighbourhood hosts in turn, each '
                'one determined to be more lavish and more memorable than the last. A '
                'visitor walking through a Tessandren city will be invited to eat, to '
                'drink, to admire the neighbourhood\'s accomplishments, and to agree that '
                'this particular street is the best street on the best planet. The '
                'invitation is warm. The expectation of agreement is non-negotiable.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='Pellamy',
            short_description='The agricultural world -- where the farmers consider themselves the backbone of the system and every hamlet has a flag and an opinion.',
            long_description=(
                'Pellamy is the system\'s agricultural and industrial base -- cooler, '
                'rockier, and less glamorous than the inner worlds, producing the food and '
                'manufactured goods that the system consumes. Pellamy hosts the Ministry of '
                'Agriculture, which it considers the ministry that keeps everyone alive '
                'while the other planets argue about trade and industry. The farmers '
                'describe their produce with a reverence that agricultural workers in other '
                'systems would find extraordinary -- the finest food, grown on the finest '
                'soil, by the finest farmers, in the finest tradition.\n\n'
                'The pride on Pellamy extends to a granularity that even other Kalinan '
                'planets find remarkable. Individual farms have flags. A hamlet of thirty '
                'people will have a founding day celebration, an anthem, and a sign at the '
                'entrance declaring it the heart of the region. The farming communities '
                'maintain rivalries with neighbouring communities over whose soil is richer, '
                'whose harvest is better, whose traditions are more authentic. These '
                'rivalries are conducted with total sincerity over distances that can be '
                'walked in an hour.\n\n'
                'The manufacturing output meets MERIT-standard specifications, described '
                'locally as exceeding MERIT standards rather than conforming to them. The '
                'distinction is meaningless. The pride is not.'
            ),
            population=2_200_000_000,
        ),
        StellarObject(
            name='Sovereign Gate',
            short_description='The system\'s primary orbital port -- positioned at the gravitational midpoint between the worlds so that no planet can claim it as theirs.',
            long_description=(
                'Sovereign Gate is Kalinan\'s main orbital port -- a large station '
                'positioned at a gravitational midpoint between the inhabited worlds so '
                'that no single planet can claim it is in their orbit. The positioning was '
                'the subject of negotiations that took longer than the station took to '
                'build. Arriving ships are greeted by a recorded welcome message that '
                'describes the system\'s history, achievements, and sovereign status in '
                'terms that take several minutes to deliver. The customs process includes a '
                'formal acknowledgement form in which visitors recognise Kalinan\'s '
                'independent governance -- a document that has no legal significance and '
                'that MERIT\'s customs liaison processes with a straight face.\n\n'
                'Sovereign Gate is where outsiders first encounter the Kalinan character. '
                'The reception is warm -- genuinely, effusively warm -- provided the '
                'visitor is willing to play along. A trader who compliments the station, '
                'praises the system, and agrees that Kalinan is a sovereign civilisation '
                'will find the population generous, hospitable, and eager to help. The '
                'flattery does not need to be subtle. A visitor who tells a Kalinan customs '
                'officer that Sovereign Gate is the finest port they have ever docked at '
                'will be believed, because the officer already thinks this and is pleased '
                'to hear it confirmed. The flattery can be transparent, obvious, and '
                'delivered with a wink, and it will still work, because Kalinan\'s pride '
                'is not performative. It is sincere. They genuinely believe they are the '
                'best, and they are genuinely delighted when someone agrees.\n\n'
                'A visitor who suggests that Kalinan is not truly independent -- that MERIT '
                'controls the system, that the trade agreements are standard provisions, '
                'that the sovereignty is cosmetic -- will find the warmth vanish instantly. '
                'The response is not violence. It is a cold, offended withdrawal that makes '
                'the remainder of the visit uncomfortable in ways that are difficult to '
                'define and impossible to resolve. The visitor will find that services are '
                'slower, prices are higher, and conversations end sooner. Questioning '
                'Kalinan\'s independence is the gravest insult an outsider can deliver. The '
                'second gravest is telling a citizen that another planet, another city, or '
                'another neighbourhood is better than theirs.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Grandeur',
            short_description='The system\'s gas giant -- fuel processing and a military garrison that Kalinan calls its Sovereign Defence Fleet and the SCN calls a garrison.',
            long_description=(
                'Grandeur is a large gas giant in the outer system -- fuel processing on '
                'its moons and the system\'s military garrison. The garrison is the most '
                'visible point where Kalinan\'s self-image meets reality. The ships are '
                'SCN vessels, crewed by SCN personnel, operating under SCN command. '
                'Kalinan\'s governance describes them as the Kalinan Sovereign Defence '
                'Fleet, operating in partnership with the SCN under the mutual defence '
                'provisions of the trade agreements. The SCN describes them as the Kalinan '
                'garrison. Both descriptions appear in official documents depending on who '
                'wrote them.\n\n'
                'The garrison personnel are briefed before arrival on respecting local '
                'customs, which means not contradicting the sovereignty narrative. Some find '
                'it amusing. Some find it endearing. A few, after extended postings, find '
                'themselves half-believing it, which the briefing warns against but which '
                'happens anyway because the enthusiasm is infectious.'
            ),
            population=75_000_000,
        ),
        StellarObject(
            name='Keswick',
            short_description='A cold outer world hosting the Ministry of Defence -- where even the mining settlements have anthems and the rivalries are measured in frozen kilometres.',
            long_description=(
                'Keswick is a cold, rocky world on the outer edge of the habitable zone '
                'with a modest mining operation and a population that is, per capita, '
                'possibly the proudest community in a system of proud communities. Keswick '
                'hosts the Ministry of Defence, which it considers the ministry that '
                'actually protects the system while the other planets handle paperwork.\n\n'
                'The mining settlements on Keswick are separated by hundreds of kilometres '
                'of frozen rock, connected by transit links and a shared certainty that '
                'their settlement is the best one. Each settlement has its flag, its '
                'anthem, its founding day, and its sign at the entrance declaring its '
                'unique contribution to the system. A visitor arriving at any settlement '
                'on Keswick will be told, within minutes, why this particular cluster of '
                'habitats on this particular stretch of frozen rock is the finest community '
                'on the finest planet in the finest system in the galaxy. The visitor will '
                'not have asked. The visitor\'s agreement is expected. The visitor\'s '
                'disagreement -- or worse, a favourable comparison to another settlement -- '
                'would be received as a personal affront by every resident within earshot.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Clarion',
            short_description='A hot inner world -- solar collection and automated industry, named with the system\'s characteristic confidence.',
            long_description=(
                'Clarion is a hot, dense inner world with solar collection arrays and '
                'automated mineral extraction. The operations are standard for a hot inner '
                'world in the inner systems, but the naming tells you everything about '
                'Kalinan: where other systems give their industrial inner planets functional '
                'names or survey designations, Kalinan named theirs Clarion -- a trumpet '
                'call, a declaration. The small engineering population maintains the arrays '
                'with the same pride that characterises everything in the system. The solar '
                'collection output is described in local media as the finest in the inner '
                'systems. It is not. It is average. The pride is not contingent on accuracy.'
            ),
            population=15_000_000,
        ),
    ],
    short_description='A system convinced of its own independence -- twelve billion proud, productive people living under MERIT governance they have agreed to call something else.',
    long_description=(
        'Kalinan is independent. Ask anyone who lives there. They will tell you at '
        'length, with passion, with pride, and with reference to the trade agreements '
        'that secured their sovereignty through masterful diplomacy. They will describe '
        'their system\'s achievements, their planets\' distinct characters, their '
        'cities\' unique contributions to a civilisation that governs itself on its own '
        'terms. They will do this with a sincerity that is impossible to doubt and '
        'difficult to interrupt.\n\n'
        'Kalinan is not independent. The logistics networks are MERIT-standard. The '
        'military garrison is SCN. The economic regulations conform to MERIT\'s '
        'framework. The trade agreements are standard integration provisions reworded '
        'to avoid the language of subordination. MERIT permits this because the result '
        'is twelve billion people who are enthusiastic, productive, and deeply invested '
        'in a system of governance they believe they control.\n\n'
        'The system has no capital. No planet would tolerate another being designated '
        'as more important. Governance is distributed across every world -- each '
        'ministry on a different planet, each administrative process split into a chain '
        'of steps spread across multiple worlds, each link in the chain convinced it is '
        'the crucial one. A permit application that would take hours in any other '
        'system takes days in Kalinan as it transits between planets. The citizens do '
        'not object. The inefficiency is the price of equality, and equality is the one '
        'value that overrides everything.\n\n'
        'The pride is fractal. It operates at every scale. The system is the finest in '
        'the galaxy. The planet is the finest in the system. The city is the finest on '
        'the planet. The neighbourhood is the finest in the city. Walk down a street in '
        'any Kalinan city and the pride is visible at every intersection: flags change, '
        'murals change, each neighbourhood announcing itself through display and '
        'decoration in quiet, relentless competition with its neighbours. Individual '
        'farms on Pellamy have flags. Mining settlements on Keswick have anthems. The '
        'pride goes all the way down, to a granularity that visitors find either '
        'charming or suffocating depending on how long they stay.\n\n'
        'Outsiders are welcome if they play along. A visitor who flatters is rewarded '
        'with warmth, hospitality, and a generosity that is genuine even when the '
        'flattery that prompted it is transparently false. A visitor who questions '
        'Kalinan\'s independence will find the warmth vanish -- not into hostility but '
        'into a cold, offended withdrawal that makes every subsequent interaction '
        'slower, more expensive, and less pleasant. Questioning the sovereignty is the '
        'gravest insult. Praising another location over the one you are standing in is '
        'the second gravest. Twelve billion people, each individually certain of their '
        'own importance, hold the whole elaborate, deluded, magnificent structure '
        'together.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

PHEDA = System(
    name='Pheda',
    star='Blue-white main sequence (A0Ve), approximately 65 times Sol luminosity',
    population=1_000_000_000,
    distance_to_sol=83.7,
    stellar_objects=[
        StellarObject(
            name='Crucen',
            short_description='The mining world -- where a rare mineral called pyreline is extracted in enormous quantities and skimmed at every stage of the process.',
            long_description=(
                'Crucen is the reason anyone is in Pheda. The planet is rocky, arid, and '
                'unpleasant -- thin atmosphere, extreme temperature swings, and a landscape '
                'of dust and exposed bedrock that nobody would colonise for its own sake. '
                'What Crucen has is pyreline: a rare crystalline mineral used in the '
                'manufacture of high-grade inertial resonators. Pyreline exists in trace '
                'quantities in a handful of other systems. On Crucen, it exists in '
                'concentrations that the original survey team described as extraordinary.\n\n'
                'MERIT established the mining operation with the intent of extracting '
                'pyreline at scale and shipping it to the inner systems for resonator '
                'production. The distance -- eighty-four light-years from Sol, multiple '
                'jumps through poorly serviced routes -- meant that the operation was '
                'granted more autonomy than MERIT would normally allow. A colonial '
                'administrator was appointed. A workforce was recruited. The mining '
                'infrastructure was built. And the skimming began almost immediately.\n\n'
                'The corruption on Crucen operates at every level of the extraction '
                'process. The miners take a handful from every haul -- pyreline crystals '
                'small enough to pocket, sold to independent buyers in the settlements. The '
                'foremen underreport yields, keeping the difference. The refinery operators '
                'dilute the processed output and sell the excess. The logistics coordinators '
                'misroute shipments. The colonial administrator signs off on production '
                'figures that everyone knows are fiction and takes a percentage for the '
                'service. For every hundred tonnes of pyreline extracted from Crucen\'s '
                'crust, perhaps twenty reach MERIT as expected. The rest is distributed '
                'through a parallel economy that is as structured and as organised as the '
                'official one, and considerably more profitable for the people involved.\n\n'
                'The settlements on Crucen have the character of mining boom towns '
                'everywhere: rough, crowded, and flush with money that was not earned '
                'through official channels. The bars are full. The gambling halls do '
                'excellent business. The housing ranges from comfortable quarters for the '
                'senior staff to improvised shelters for the newest arrivals who have not '
                'yet figured out which gang controls their section and what the tribute '
                'costs. The gangs are the real administrative structure on Crucen -- '
                'organised groups that control territory, manage the skimming operations, '
                'and maintain order through a combination of bribery, intimidation, and '
                'the practical observation that a dead workforce mines no pyreline.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Ashwell',
            short_description='A marginal second world settled by people who could not afford a place on Crucen -- serving the overflow and feeding the miners.',
            long_description=(
                'Ashwell is the system\'s second world -- colder than Crucen, further from '
                'the star, with barely breathable air and growing conditions that require '
                'enclosed agricultural facilities. Ashwell was not part of the original '
                'plan. The original plan was Crucen and nothing else. But the boom drew '
                'more people than Crucen could house, and the overflow -- the workers who '
                'arrived too late for the good claims, the families who followed the miners, '
                'the service workers who could not afford Crucen\'s inflated housing costs '
                '-- settled on Ashwell because it was the only other option.\n\n'
                'Ashwell\'s economy is secondary to Crucen\'s in every way. The enclosed '
                'farms feed the miners. The workshops repair the equipment. The bars are '
                'cheaper than Crucen\'s and the clientele is rougher. The corruption here '
                'is less organised -- Ashwell does not have the structured gangs that '
                'control Crucen\'s skimming operations, but it has a general lawlessness '
                'that fills the gap. Disputes are settled informally. Property rights are '
                'what you can defend. The colonial administration\'s authority extends to '
                'Ashwell in theory and barely in practice, because the administrator is '
                'busy managing the fiction on Crucen and cannot be bothered with a '
                'secondary world that produces nothing MERIT cares about.\n\n'
                'Ashwell is where the people who washed out of Crucen end up -- miners '
                'who lost their claims, workers who crossed the wrong gang, families who '
                'came for the boom and discovered that the boom is for the people who got '
                'there first. The planet is not destitute. The secondary economy functions. '
                'But it has the particular bitterness of a place that exists because '
                'somewhere better would not have them.'
            ),
            population=250_000_000,
        ),
        StellarObject(
            name='The Exchange',
            short_description='The system\'s orbital station -- where skimmed pyreline is laundered into legitimate commerce and sold to anyone with credits.',
            long_description=(
                'The Exchange is Pheda\'s orbital station -- ostensibly a standard transit '
                'hub and cargo processing facility, functionally the point where the '
                'system\'s parallel economy interfaces with the rest of the galaxy. '
                'Pyreline that was skimmed on Crucen, refined in unofficial facilities, '
                'and packaged in containers with fabricated provenance documents is loaded '
                'onto ships at the Exchange and sold to buyers who do not ask where it '
                'came from.\n\n'
                'The buyers include inner-system manufacturers who need pyreline and find '
                'the official MERIT supply insufficient or slow. They include outer-system '
                'buyers who cannot access MERIT\'s supply at all and are willing to pay '
                'premium prices. They include intermediaries who buy in bulk and resell '
                'through channels that add layers of documentation until the pyreline\'s '
                'origin is untraceable. The war has been very good for the Exchange. Both '
                'sides need resonator-grade pyreline. Both sides will pay for it. The '
                'Exchange does not discriminate.\n\n'
                'MERIT\'s customs presence on the Exchange is understaffed, underfunded, '
                'and compromised. The customs officers are drawn from the same population '
                'as everyone else in Pheda, and the gangs that control the skimming '
                'operations on Crucen have long since determined which officers can be '
                'bought and at what price. The officers who cannot be bought are '
                'transferred to shifts where they encounter nothing worth inspecting. The '
                'system is efficient. The corruption has had decades to optimise itself, '
                'and it has.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='The Vein',
            short_description='The richest pyreline deposit on Crucen -- an exposed geological formation that the gangs have fought over since the boom began.',
            long_description=(
                'The Vein is not a separate world but the most significant geological '
                'feature on Crucen -- an exposed pyreline formation running through a '
                'mountain range in the southern hemisphere that contains the highest '
                'concentration of the mineral found anywhere in the galaxy. The Vein is '
                'where the largest mining operations are concentrated, where the most '
                'money flows, and where the gang control is most absolute.\n\n'
                'Three gangs currently control sections of the Vein, and the boundaries '
                'between their territories are the most dangerous places in the system. '
                'The gangs maintain an uneasy equilibrium: each controls enough of the '
                'Vein to be profitable, none controls enough to dominate the others, and '
                'the cost of a war for total control would disrupt the extraction that '
                'makes the territory valuable in the first place. The equilibrium is '
                'maintained by pragmatism rather than goodwill, and it breaks down '
                'periodically in violence that is brief, targeted, and resolved when the '
                'surviving parties renegotiate the boundaries. The miners who work the '
                'Vein under gang supervision are paid well by Pheda standards. They are '
                'also aware that their employer is a criminal organisation, that the '
                'alternative employers are also criminal organisations, and that the '
                'colonial administrator who is supposed to govern them is the most '
                'successful criminal of all.'
            ),
            population=0,
        ),
        StellarObject(
            name='Durrance',
            short_description='A gas giant whose moons host fuel processing and the unofficial meeting ground where the gangs negotiate without witnesses.',
            long_description=(
                'Durrance is the system\'s gas giant -- a mid-sized body in the outer system '
                'with moons that host fuel processing operations. The fuel is consumed '
                'locally -- Pheda\'s traffic is substantial for a system its size, because '
                'the pyreline trade generates a constant flow of ships arriving to buy and '
                'departing with cargo.\n\n'
                'Durrance\'s moons serve a secondary function that is not listed in any '
                'official documentation. The outer system is where the gangs meet when they '
                'need to negotiate without the colonial administration\'s knowledge -- or '
                'more accurately, without the colonial administrator having to officially '
                'know, since the administrator is aware of everything and prefers to '
                'maintain deniability. Territory disputes, pricing agreements, and the '
                'coordination of the skimming schedules that ensure the official production '
                'numbers remain plausible are all discussed on Durrance\'s moons, in '
                'facilities that are listed as fuel storage and function as conference '
                'rooms for organised crime.'
            ),
            population=25_000_000,
        ),
        StellarObject(
            name='Latchford',
            short_description='A frozen outer body where the people who have made their fortunes from the boom retire -- far from the dust, the gangs, and the questions.',
            long_description=(
                'Latchford is a cold, rocky body in the outer system -- not habitable on '
                'the surface but hosting a cluster of enclosed habitats that are, by Pheda '
                'standards, luxurious. Latchford is where the money goes. The gang leaders '
                'who have skimmed enough pyreline to retire, the senior administrators who '
                'have taken their percentages for long enough, the successful intermediaries '
                'who have laundered enough credits to buy comfort -- they end up on '
                'Latchford, in habitats that are clean, spacious, and very far from the '
                'dust and violence of Crucen.\n\n'
                'The community on Latchford is small and does not discuss how its members '
                'acquired their wealth. The habitats are well-appointed. The food is '
                'imported from the inner systems rather than grown on Ashwell. The '
                'conversations are careful. Everyone knows what everyone else did to get '
                'here, and the shared knowledge is the community\'s bond and its insurance '
                'policy: nobody talks, because everybody could.'
            ),
            population=3_000_000,
        ),
    ],
    short_description='A corrupt boom town at the edge of the inner systems -- where a rare mineral draws a billion people and eighty percent of the output disappears before it reaches MERIT.',
    long_description=(
        'Pheda is what happens when MERIT discovers something valuable in a place it '
        'cannot effectively govern. The system is eighty-four light-years from Sol, '
        'recently discovered, and connected to the inner systems by jump routes that '
        'are long, poorly serviced, and difficult to monitor. What the system has is '
        'pyreline -- a rare crystalline mineral essential for high-grade inertial '
        'resonator manufacture, found in trace quantities elsewhere and in extraordinary '
        'concentrations on Crucen, the system\'s primary world. MERIT established a '
        'mining operation and granted it the autonomy that distance required. The '
        'autonomy became corruption. The corruption became the system.\n\n'
        'A billion people live in Pheda, drawn by the boom. The mining towns on Crucen '
        'are rough, crowded, and controlled by gangs that manage the skimming operations '
        'with a structure and efficiency that the official administration cannot match '
        'and does not attempt to. For every hundred tonnes of pyreline extracted, '
        'perhaps twenty reach MERIT as expected. The rest is skimmed at every level -- '
        'miners pocketing crystals, foremen underreporting yields, refineries diluting '
        'output, logistics coordinators misrouting shipments -- and sold through the '
        'Exchange to buyers who include inner-system manufacturers, outer-system '
        'factions, and intermediaries whose documentation launders the origin.\n\n'
        'The war has made it worse. Both sides need resonator-grade pyreline. Both '
        'sides will pay. The gangs of Crucen sell to MERIT-aligned buyers and outer-'
        'system buyers with equal enthusiasm, and the colonial administrator -- who is '
        'supposed to ensure MERIT\'s interests are served -- takes a percentage from '
        'everyone and signs production figures that are fiction. MERIT knows. MERIT has '
        'always known. The cost of imposing real governance on a system this remote '
        'exceeds the cost of the stolen pyreline, and MERIT has calculated that '
        'receiving twenty percent of an enormous deposit is better than receiving one '
        'hundred percent of nothing, which is what the system would produce if the '
        'crackdown drove the workforce away.\n\n'
        'Pheda is corrupt from the surface to the sky. The gangs run the mines. The '
        'administrator runs the gangs. The customs officers are bought. The production '
        'figures are lies. The pyreline flows to whoever can pay, and the money flows '
        'to Latchford where the retired criminals live in comfort and do not discuss '
        'the source. The system functions. It functions corruptly, but it functions, '
        'and the pyreline that MERIT does receive is valuable enough that the '
        'arrangement persists. Nobody in Pheda pretends the system is honest. Honesty '
        'is not the local currency. Pyreline is.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

BARGHAL = System(
    name='Barghal',
    star='Blue-white main sequence (A0V) with a faint orange dwarf companion',
    population=350_000_000,
    distance_to_sol=86.8,
    stellar_objects=[
        StellarObject(
            name='Torren',
            short_description='The main world -- once a pirate stronghold of billions, now a scarred planet of two hundred million trying to rebuild what the warlords and MERIT between them destroyed.',
            long_description=(
                'Torren was, before the crackdown, home to several billion people living '
                'under warlord rule in conditions that made Vega look restrained. The piracy '
                'was industrialised. The violence was systematic. The civilian population '
                'was a resource to be exploited by whoever held the territory. MERIT '
                'tolerated it for longer than it should have, calculating the cost of '
                'intervention against the cost of inaction, until the calculation tipped '
                'and the fleet arrived.\n\n'
                'What followed was not a liberation. The warlords, facing annihilation, '
                'responded with the desperation of people who had nothing to gain from '
                'surrender. Some took hostages, herding civilians into their compounds and '
                'daring MERIT to fire through them. Some looted everything they could carry '
                'and tried to run, burning what they could not take -- warehouses, '
                'infrastructure, entire districts set ablaze to deny them to MERIT or to '
                'destroy evidence. Some rigged their own installations with explosives and '
                'detonated them as MERIT forces approached, killing their own people along '
                'with any records that might have been used against them. The crackdown '
                'succeeded. The warlords were killed or captured. The system was secured. '
                'What was secured was rubble.\n\n'
                'Torren today is a world still visibly scarred. The major cities have been '
                'partially rebuilt -- MERIT-standard prefabricated modules replacing the '
                'destroyed infrastructure, new construction rising beside the gutted shells '
                'of buildings that have not yet been demolished. The reconstruction is '
                'methodical and slow, because MERIT\'s resources are stretched by the war '
                'and Barghal is not a priority. The population is two hundred million -- a '
                'fraction of what it was. The people who remain are those who had nowhere '
                'else to go: the poorest residents of the former warlord territories, people '
                'whose roots on Torren predate the pirate era, and the MERIT reconstruction '
                'workers who were assigned here and count the days until reassignment.\n\n'
                'The ruins are everywhere. Outside the rebuilt city centres, the landscape '
                'is dotted with the remains of the old settlements -- burned-out structures, '
                'collapsed warehouses, the scorched foundations of compounds that the '
                'warlords destroyed rather than surrender. The ruins are not preserved as '
                'memorials. They are simply not yet cleared, because there are not enough '
                'people and not enough money to clear them. Children born on Torren grow up '
                'playing in the ruins of a civilisation that their grandparents lived in and '
                'that they know only as wreckage.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Wenfall',
            short_description='A second world that was barely touched by the crackdown -- because it had already been stripped bare by the warlords before MERIT arrived.',
            long_description=(
                'Wenfall is the system\'s second habitable world -- colder, smaller, and '
                'less central to the warlord economy than Torren. The crackdown barely '
                'touched Wenfall because there was nothing left to crack down on. The '
                'warlords had used Wenfall as a resource extraction colony -- stripping the '
                'accessible mineral deposits, working the agricultural land until it was '
                'exhausted, and treating the population as disposable labour. By the time '
                'MERIT arrived, Wenfall was already devastated. The warlords had moved on '
                'to richer territory. The people remained because they had no ships and no '
                'money and no one to buy passage from.\n\n'
                'The reconstruction on Wenfall has been slower than on Torren because '
                'Wenfall has less to rebuild from. The soil in the overworked agricultural '
                'regions is depleted. The mining sites are exhausted. The settlements were '
                'built cheaply by the warlords and have deteriorated beyond repair. MERIT\'s '
                'reconstruction effort on Wenfall has focused on basic habitability -- '
                'ensuring the population has food, water, shelter, and medical care -- '
                'rather than economic development, because there is nothing to develop an '
                'economy around. The population is small, ageing, and shrinking as the '
                'younger generation leaves for systems where the prospects are better than '
                'subsistence on exhausted land.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='The Wreckage',
            short_description='The orbital debris left from the crackdown -- destroyed stations, wrecked ships, and the detritus of a battle that ended an era.',
            long_description=(
                'The Wreckage are what is left in orbit. The warlords maintained orbital '
                'stations, docking facilities, and the infrastructure of a piracy economy '
                'that processed stolen goods at scale. During the crackdown, MERIT\'s fleet '
                'destroyed the stations that resisted and the warlords destroyed the ones '
                'that did not -- scuttling their own facilities to deny MERIT the records '
                'stored aboard. The result is a debris field in Torren\'s orbital space '
                'that has been partially cleared but not completely, because clearing '
                'orbital debris is expensive and the budget is allocated to keeping the '
                'surface population alive.\n\n'
                'The larger pieces have been catalogued and tracked to prevent collision '
                'hazards. The smaller pieces drift. Occasionally a piece of wreckage from '
                'a warlord\'s station or a pirate ship enters the atmosphere and burns up '
                'over Torren, a brief streak of light that the older residents watch with '
                'expressions that visitors find difficult to read.'
            ),
            population=0,
        ),
        StellarObject(
            name='Bridgehead',
            short_description='MERIT\'s reconstruction station -- the system\'s only functioning orbital facility, managing the slow process of rebuilding what was destroyed.',
            long_description=(
                'Bridgehead is the only operational orbital station in Barghal -- a MERIT '
                'facility built after the crackdown to serve as the reconstruction effort\'s '
                'hub. The station handles the supply shipments that arrive from the inner '
                'systems carrying construction materials, food supplements, medical '
                'supplies, and the prefabricated infrastructure modules that are gradually '
                'replacing what was destroyed. The station also handles the system\'s modest '
                'traffic -- the ships are few, because there is little reason to visit '
                'Barghal unless you are part of the reconstruction or have business with '
                'the remaining population.\n\n'
                'The reconstruction staff on Bridgehead are MERIT personnel on fixed '
                'assignments. The posting is not popular. Barghal\'s reputation precedes it '
                '-- the system is known throughout the inner systems as the place where '
                'everything went wrong, first under the warlords and then during the '
                'crackdown, and the association is difficult to shake. The staff do their '
                'work with the professional commitment of people who understand that the '
                'assignment is important and wish it were somewhere else. The reconstruction '
                'is progress. The progress is slow. The system\'s reputation ensures that '
                'the volunteers are few and the assigned personnel are counting their '
                'remaining months.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Scarfield',
            short_description='A plateau on Torren where one warlord detonated their entire compound rather than surrender -- the crackdown\'s most notorious atrocity site.',
            long_description=(
                'Scarfield is a plateau in Torren\'s northern hemisphere where one of the '
                'system\'s most powerful warlords maintained their primary compound. When '
                'MERIT\'s fleet entered the system and the crackdown began, the warlord '
                'gathered several hundred thousand civilians into the compound -- ostensibly '
                'for protection, actually as hostages. When MERIT forces surrounded the '
                'compound and negotiations failed, the warlord detonated the explosives '
                'that had been placed throughout the facility. The compound, the warlord, '
                'and the civilians were destroyed.\n\n'
                'Scarfield is a crater now. The blast site has not been rebuilt. The ground '
                'is scorched and fused in a pattern that is visible from orbit -- a dark '
                'scar on the plateau that the planet\'s weather has not eroded and that no '
                'one has proposed building on. The site is not officially designated as a '
                'memorial. There is no plaque, no monument, no formal recognition of what '
                'happened. The population of Torren knows. The MERIT reconstruction staff '
                'know. The absence of a memorial is itself a statement -- the system has '
                'not yet decided how to remember what was done to it, by the warlords or '
                'by the crackdown that ended them, and until it decides, Scarfield is just '
                'a crater that nobody builds on and nobody discusses.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dullen',
            short_description='A frozen outer body -- once a warlord hideout, now empty, its tunnels sealed by MERIT and its contents classified.',
            long_description=(
                'Dullen is a frozen body in the outer system that the warlords used as a '
                'secondary base -- tunnels carved into the ice for storage, concealment, '
                'and the operations that even the warlords preferred to conduct away from '
                'the inhabited worlds. MERIT forces secured Dullen during the crackdown '
                'and found the tunnels intact -- the warlords who used them had fled or '
                'been killed before they could destroy the contents.\n\n'
                'What MERIT found in Dullen\'s tunnels has not been publicly disclosed. The '
                'tunnels were sealed, the contents removed or classified, and the body '
                'designated as a restricted zone. The restriction has been maintained since '
                'the crackdown. MERIT does not discuss Dullen. The reconstruction staff on '
                'Bridgehead do not discuss Dullen. The population of Torren has theories '
                'about what was found -- weapons, evidence of atrocities, records that '
                'implicate people who are still alive -- and none of the theories have been '
                'confirmed or denied. Dullen is sealed, silent, and officially not worth '
                'discussing, which ensures that it is discussed constantly.'
            ),
            population=0,
        ),
    ],
    short_description='A devastated system still recovering from a MERIT crackdown that ended an era of warlord piracy -- and destroyed much of what it was trying to save.',
    long_description=(
        'Barghal was worse than Vega. For decades, the system was controlled by '
        'warlords who ran piracy operations that terrorised the surrounding inner '
        'systems, preying on shipping lanes and using a civilian population of billions '
        'as cover, labour, and leverage. MERIT tolerated it, calculated against it, '
        'and eventually decided the cost of inaction exceeded the cost of intervention. '
        'The fleet arrived. The crackdown began. What followed was not a clean '
        'operation.\n\n'
        'The warlords did not surrender. They took hostages, using civilians as '
        'shields. They looted what they could and burned what they could not, setting '
        'entire districts ablaze to destroy evidence or deny assets to MERIT. They '
        'rigged their own installations with explosives and detonated them as forces '
        'closed in -- killing their own people, their prisoners, and anyone nearby. '
        'The worst atrocity was Scarfield, where a warlord detonated a compound packed '
        'with several hundred thousand civilian hostages rather than allow MERIT to '
        'take the facility intact. The crackdown succeeded. The warlords were '
        'eliminated. The system was secured. What was secured was devastation.\n\n'
        'That was generations ago, and Barghal has not recovered. Three hundred and '
        'fifty million people live in a system that once held billions. The cities on '
        'Torren are partially rebuilt -- MERIT prefabricated modules beside the gutted '
        'shells of buildings not yet demolished. Outside the rebuilt centres, the ruins '
        'of the warlord era stretch across the landscape. Wenfall, the second world, '
        'was stripped bare before MERIT arrived and has barely begun to recover. The '
        'orbital space is still littered with debris from destroyed stations.\n\n'
        'The reconstruction is slow. MERIT\'s resources are stretched by the war, and '
        'Barghal is not a priority. The system\'s reputation -- the place where '
        'everything went wrong, twice -- means that nobody volunteers to move there '
        'and those born there leave when they can. The population is diminished, ageing '
        'in some areas, and sustained by MERIT reconstruction aid that is adequate and '
        'insufficient. Barghal is the inner systems\' wound -- proof that MERIT\'s '
        'control has limits, that the cost of losing control is measured in lives, and '
        'that the cost of regaining it can be measured the same way.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

GADDACK = System(
    name='Gaddack',
    star='Red giant (M3.5III), enormously expanded, most luminosity in infrared -- casting a deep, dim red light that makes the system feel dark even close to the star',
    population=0,
    distance_to_sol=88.6,
    stellar_objects=[
        StellarObject(
            name='Rathven',
            short_description='The innermost world -- a scorched husk orbiting so close to the expanded red giant that its surface has been baked into glass.',
            long_description=(
                'Rathven was once further from its star. When the star expanded into its '
                'red giant phase, the inner orbital space was consumed and Rathven -- '
                'whatever it was before -- was subjected to temperatures that fused its '
                'surface into a dark, glassy crust. The planet orbits at the edge of the '
                'expanded star\'s influence, close enough that the red disc fills a '
                'significant portion of the sky, dim and vast and the colour of cooling '
                'iron. The surface reflects the red light in dark, glassy sheets. The '
                'atmosphere is gone -- stripped away during the expansion. Rathven is a '
                'dead world orbiting a dying star, and it has been this way for longer '
                'than humanity has existed.'
            ),
            population=0,
        ),
        StellarObject(
            name='Dremmon',
            short_description='A world that was once in the habitable zone -- its ocean beds are dry, its atmosphere is a wisp, and the fossils in the rock are billions of years old.',
            long_description=(
                'Dremmon sits where the habitable zone used to be, before the star expanded '
                'and the zone migrated outward past anything that could benefit from it. '
                'The survey team found what they expected: a world that was once habitable '
                'and has not been for a very long time. The oceans boiled away. The '
                'atmosphere was stripped to a thin wisp of carbon dioxide. The surface is '
                'exposed seabed -- ancient sedimentary rock that was once the floor of a '
                'global ocean, now baked dry under the dim red light.\n\n'
                'The fossils are the only interesting feature. The sedimentary layers '
                'contain the compressed remains of microbial life -- simple organisms that '
                'lived in Dremmon\'s oceans billions of years ago, before the star began '
                'its expansion. The fossils are not complex. They are not remarkable by '
                'the standards of xenobiology, which has documented far more sophisticated '
                'alien life in systems like Sirius and Genubi. But they are a record of '
                'life that existed and ended -- an ecosystem that ran its course and was '
                'extinguished not by catastrophe but by the natural evolution of its own '
                'star. Dremmon is what happens eventually. The star changes. The life does '
                'not survive the change.'
            ),
            population=0,
        ),
        StellarObject(
            name='Kellan',
            short_description='A cold, dry world at the current habitable zone -- technically receiving enough energy to support liquid water, but sterilised long ago and never reseeded.',
            long_description=(
                'Kellan is at the distance where the habitable zone has migrated to -- the '
                'point where the red giant\'s diminished visible output and enormous '
                'infrared flux combine to produce surface temperatures that could, in '
                'theory, support liquid water. The theory is not practice. Kellan\'s '
                'surface is dry, cold, and barren. Whatever atmosphere it once had was '
                'insufficient to retain heat, and the planet never developed the conditions '
                'for water to persist. The habitable zone migrated to Kellan. Life did not '
                'follow.\n\n'
                'The survey team assessed Kellan as the most terraformable body in the '
                'system and simultaneously the least worth terraforming. The conditions '
                'are marginal. The star is unstable -- red giants are variable, and the '
                'energy output fluctuates on timescales that would make long-term planning '
                'difficult. The star\'s remaining lifespan, while long by human standards, '
                'is short by stellar ones. Terraforming a world to habitability only for '
                'the star to shed its outer layers and become a white dwarf would be the '
                'most expensive waste of time in colonial history. Kellan was assessed, '
                'noted, and left alone.'
            ),
            population=0,
        ),
        StellarObject(
            name='Brannock',
            short_description='A gas giant that has lost a significant fraction of its atmosphere to the star\'s expansion -- visibly diminished, trailing a faint tail of escaping gas.',
            long_description=(
                'Brannock is a gas giant in the outer system that bears the marks of the '
                'star\'s evolution. The red giant\'s expansion increased the stellar wind '
                'to a degree that has been stripping Brannock\'s upper atmosphere over '
                'millions of years. The planet is visibly diminished -- smaller than its '
                'mass suggests it should be, with a faint tail of escaping hydrogen '
                'trailing behind it in its orbit, visible on sensors as a wispy extension '
                'of the planet\'s atmosphere being slowly torn away.\n\n'
                'Brannock will eventually be reduced to its dense core -- a dead remnant '
                'of a planet that was once larger, orbiting a dead remnant of a star that '
                'was once brighter. The process will take longer than human civilisation '
                'has existed. The survey team documented it as a textbook example of '
                'atmospheric stripping by stellar wind, noted its unsuitability for fuel '
                'processing due to the contaminated upper atmosphere, and moved on.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Shroud',
            short_description='A shell of dust and gas shed by the red giant -- the material the star has already lost, drifting outward through the system.',
            long_description=(
                'The Shroud is not a world but a feature of the system -- a diffuse shell '
                'of dust and gas that the red giant has shed over the course of its '
                'expansion. The material is thin, barely detectable on standard sensors, '
                'but it is there: a faint haze of stellar material drifting outward through '
                'the system, giving the already dim red light a further quality of '
                'diffusion. Ships transiting through Gaddack report that the system feels '
                'hazy -- not the dense, sensor-blocking dust of Fomalhaut but a subtle '
                'dimming, as though the light is being seen through gauze. The effect is '
                'the star\'s own material, expelled over millions of years, hanging in the '
                'space between its worlds like a funeral veil.\n\n'
                'The Shroud will thicken. As the red giant continues to evolve, it will '
                'shed more material, eventually expelling its outer layers entirely to '
                'form a planetary nebula around the white dwarf core that will be all that '
                'remains. The process is millions of years away. The Shroud is the '
                'beginning of the end, visible now as a faint haze and destined to become '
                'something spectacular long after the last human has forgotten the system '
                'exists.'
            ),
            population=0,
        ),
        StellarObject(
            name='Pershen',
            short_description='A frozen outer body untouched by the star\'s expansion -- the one world in the system that looks the same as it did billions of years ago.',
            long_description=(
                'Pershen is a small, frozen body in the far outer system -- distant enough '
                'from the star that its expansion has had no measurable effect. The surface '
                'is ancient ice and rock, unchanged for billions of years, predating the '
                'star\'s evolution and untouched by it. Pershen is what the outer system '
                'looked like when Dremmon\'s oceans were full and its microbes were alive. '
                'It is the one constant in a system where everything else has been '
                'transformed by the star\'s ageing.\n\n'
                'The survey team noted Pershen as scientifically unremarkable and moved on. '
                'The body is too small, too cold, and too distant to warrant attention in '
                'a system that warrants no attention at all. Pershen orbits in the dark, '
                'as it has for billions of years, unchanged and unnoticed, the last thing '
                'in a dead system that is still exactly what it always was.'
            ),
            population=0,
        ),
    ],
    short_description='A dead system under a dying star -- worlds sterilised by the red giant\'s expansion, a preview of what every star system will eventually become.',
    long_description=(
        'Gaddack is a corpse. The star is a red giant -- enormously expanded, its '
        'luminosity shifted into infrared, casting a deep, dim red light that makes '
        'the system feel dark even close to the star. The visible disc is vast and the '
        'colour of cooling iron. The worlds that orbit it are the remains of a system '
        'that was once, billions of years ago, something else -- a younger star with '
        'a habitable zone and at least one world where microbial life evolved in '
        'oceans that no longer exist.\n\n'
        'The star\'s expansion killed everything. Rathven\'s surface was baked into '
        'glass. Dremmon\'s oceans boiled away, leaving fossils in exposed seabed that '
        'record the existence of life that ended when the star changed. The habitable '
        'zone migrated outward to Kellan, but Kellan was never alive and the zone\'s '
        'arrival could not change that. Brannock, the gas giant, is being slowly '
        'stripped of its atmosphere by the intensified stellar wind, trailing a faint '
        'tail of escaping hydrogen. The Shroud -- a diffuse shell of material shed by '
        'the star -- hangs in the space between the worlds like gauze, dimming the '
        'already dim light further.\n\n'
        'Nobody lives in Gaddack. Nobody has reason to. The system was surveyed, '
        'documented, and added to the navigation charts as a waypoint for ships '
        'transiting to more distant systems. Pilots who pass through describe the '
        'experience as sombre -- the dim red light, the hazy void, the dead worlds '
        'drifting in the remains of their own star\'s atmosphere. Gaddack is not '
        'dangerous. It is not mysterious. It is simply finished -- a system that ran '
        'its course, that hosted life and lost it, that is winding down toward a white '
        'dwarf and a planetary nebula that will be beautiful and that nobody alive '
        'today will see. Every star system will look like this eventually. Gaddack is '
        'the reminder that eventually is not as far away as it feels.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

SABIX = System(
    name='Sabix',
    star='White main sequence (A1V) with a K-type orange dwarf companion in a wide orbit',
    population=10_000_000_000,
    distance_to_sol=88.0,
    stellar_objects=[
        StellarObject(
            name='Harsten',
            short_description='The capital world -- six billion people living comfortably in a civilisation built for a purpose that no longer exists.',
            long_description=(
                'Harsten was, for two centuries, one of the most important worlds in the '
                'inner systems. The planet\'s crust is rich in heavy metals and rare earth '
                'elements that were essential to the early interstellar expansion -- the raw '
                'materials that built the first generation of jump-capable ships, the first '
                'orbital stations, the first colonial infrastructure. Harsten\'s mines fed '
                'the foundries. The foundries fed the shipyards. The shipyards built the '
                'fleet that carried humanity to the stars. For a time, Harsten mattered '
                'more than any world except Earth.\n\n'
                'The decline was not sudden. It was the slow, grinding arithmetic of '
                'economics: richer deposits were found in younger systems. Tau Ceti\'s Veil '
                'offered inexhaustible material at lower extraction cost. Other systems '
                'closer to the expanding frontier could supply the shipyards without the '
                'long transit from Sabix. The contracts moved. The foundries scaled back. '
                'The mines that had operated around the clock reduced to single shifts, then '
                'skeleton crews, then maintenance-only. The population did not leave -- '
                'MERIT guarantees basic needs regardless of economic output, and ten billion '
                'people with established lives and homes and communities do not uproot '
                'because the industry left. They stayed. The industry did not come back.\n\n'
                'Harsten today is a world that is comfortable and purposeless. The cities '
                'are well-maintained -- MERIT\'s infrastructure does not decay -- but they '
                'were built for a population that worked in heavy industry, and the '
                'architecture reflects a grandeur that no longer has a source. The '
                'residential districts are spacious because they were built to attract '
                'workers to a booming economy. The transit systems are oversized because '
                'they were designed to move shift workers to foundries that are now museums. '
                'The parks are beautiful because the city planners of the industrial era '
                'believed that the workers who built the galaxy deserved beautiful parks. '
                'The workers\' grandchildren sit in those parks and are not sure what they '
                'are supposed to be doing with their lives.\n\n'
                'The museums are everywhere. The Museum of Interstellar Industry in '
                'Harsten\'s largest city is the most visited site in the system -- a vast '
                'complex documenting the era when Sabix\'s output built the fleet. The '
                'exhibits are impressive. The pride is genuine. The tense is past.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Kellaway',
            short_description='The second world -- once the system\'s foundry planet, now a landscape of decommissioned industrial facilities slowly being converted to other uses.',
            long_description=(
                'Kellaway was the system\'s industrial heart -- the planet where the raw '
                'material extracted from Harsten\'s mines was refined, processed, and '
                'manufactured into the components that the inner systems needed. The '
                'foundries on Kellaway were enormous: industrial complexes covering '
                'hundreds of square kilometres, fed by orbital elevators that brought '
                'material down from the processing stations and sent finished goods back '
                'up. At peak output, Kellaway\'s foundries consumed more energy than most '
                'inhabited worlds generate.\n\n'
                'The foundries are quiet now. Most have been decommissioned -- the '
                'equipment removed or mothballed, the structures maintained in a state of '
                'preservation that is either optimistic or sentimental depending on your '
                'perspective. A few have been converted: one foundry complex is now a '
                'university campus, its cavernous production halls repurposed as lecture '
                'theatres and research facilities. Another houses the system\'s largest '
                'cultural centre -- performance spaces, galleries, and studios occupying '
                'a building that once produced hull plating at a rate of tonnes per hour. '
                'The conversions are well-intentioned and slightly melancholy, because the '
                'buildings were not designed for their new purposes and the adaptation is '
                'visible.\n\n'
                'Kellaway\'s population works in the service sector, education, and the '
                'small-scale manufacturing that remains -- producing goods for the system\'s '
                'internal consumption rather than for export. The wages are adequate. The '
                'quality of life is fine. The sense of diminishment is pervasive and '
                'difficult to articulate: nothing is wrong, exactly, but something is '
                'missing. The older residents remember parents and grandparents who came '
                'home from the foundries tired and proud. The younger residents come home '
                'from service jobs that pay the bills and inspire nothing.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='Corven',
            short_description='A cold outer world where the deep mines still operate at a fraction of their former capacity -- the last active extraction in the system.',
            long_description=(
                'Corven is a cold, rocky world in the outer habitable zone that hosts the '
                'system\'s last active mining operations. The mines on Corven extract '
                'speciality minerals that are still commercially viable -- not the bulk '
                'materials that made Sabix famous but niche deposits that maintain a modest '
                'export market. The operations are small compared to what they replaced: '
                'a few thousand miners working seams that the industrial-era workforce '
                'would have considered barely worth opening.\n\n'
                'Corven\'s mining communities are the most purposeful places in the system '
                '-- the one location where people still do the work that Sabix was built '
                'for. The miners are aware of this distinction and carry it with a pride '
                'that the rest of the system envies without quite admitting it. The mining '
                'heritage celebrations on Corven are the most attended events in the '
                'system, drawing visitors from Harsten and Kellaway who come to watch the '
                'demonstrations of industrial technique and remember what the system used '
                'to be. The miners perform the demonstrations with the practised ease of '
                'people who still do this every day. The visitors watch with the wistfulness '
                'of people who wish they did.'
            ),
            population=180_000_000,
        ),
        StellarObject(
            name='The Yards',
            short_description='The decommissioned orbital shipyards -- once the largest in the inner systems outside Tau Ceti, now a historical monument and tourist attraction.',
            long_description=(
                'The Yards are the orbital shipyards that once produced a significant '
                'fraction of the inner systems\' vessel tonnage. The structures are still '
                'there -- enormous frameworks in orbit above Kellaway, their docking clamps '
                'empty, their construction bays dark, their assembly lines powered down '
                'and preserved under a maintenance regime that keeps them from deteriorating '
                'without any expectation that they will be reactivated.\n\n'
                'The Yards are the system\'s most potent symbol of what was lost. Tour ships '
                'carry visitors through the empty construction bays where capital-class '
                'vessels were assembled -- cavernous spaces large enough to hold a '
                'destroyer, lit by guide lights that illuminate the scaffolding and the '
                'tool mounts and the calibration marks on the bay walls. The tour guides '
                'recite production statistics from the peak era with the reverence of '
                'people describing a religious text. The visitors buy souvenirs. The '
                'souvenir shops are the most commercially active operations in the Yards, '
                'which is a fact that nobody involved finds anything other than depressing.\n\n'
                'There is a permanent, low-level political debate in Sabix about whether '
                'the Yards should be reactivated. The argument for reactivation is '
                'emotional: the Yards are what Sabix is, and leaving them dark is an '
                'admission of defeat. The argument against is economic: the Yards are '
                'obsolete, the tooling is generations behind, and retooling would cost more '
                'than building new facilities in a system with better supply lines. The '
                'debate has been ongoing for decades. The Yards remain dark.'
            ),
            population=15_000_000,
        ),
        StellarObject(
            name='Sterngate',
            short_description='The system\'s orbital port -- built during the boom to handle enormous freight traffic, now processing a fraction of its designed capacity.',
            long_description=(
                'Sterngate is the system\'s primary orbital port -- a large station in orbit '
                'above Harsten that was designed during the industrial era to handle freight '
                'traffic at a scale that matched Sabix\'s output. The station has docking '
                'capacity for hundreds of freighters. Most of the berths are empty. The '
                'cargo bays can process millions of tonnes of material per cycle. They '
                'process a fraction of that. The transit halls were built for crowds of '
                'workers rotating between systems. The crowds are gone.\n\n'
                'Sterngate is too large for the system it serves. The empty berths and the '
                'silent cargo bays are a daily reminder to the staff that the station was '
                'designed for a version of Sabix that no longer exists. The management has '
                'converted some of the unused sections into commercial and residential '
                'space, but the conversions feel like what they are: a large building '
                'finding secondary uses for rooms that were built for something else. The '
                'station functions well. It functions at a quarter of its capacity, and the '
                'unused three-quarters echo.'
            ),
            population=85_000_000,
        ),
        StellarObject(
            name='Feldern',
            short_description='A hot inner world -- its solar collection arrays were cutting-edge when they were installed and are now merely adequate, like everything else in the system.',
            long_description=(
                'Feldern is a hot, dense inner world with solar collection arrays that were, '
                'when installed during the industrial era, among the most advanced in the '
                'inner systems. The arrays powered the foundries on Kellaway and the '
                'shipyards in orbit. They are still operational. They are no longer '
                'cutting-edge -- the technology has been surpassed by newer installations '
                'in other systems, and the output, while sufficient for Sabix\'s reduced '
                'needs, is a fraction of what it once supplied. The maintenance crews keep '
                'the arrays running with a diligence that is part professional and part '
                'sentimental. The arrays are old. They still work. In Sabix, that '
                'description applies to a lot of things.'
            ),
            population=10_000_000,
        ),
        StellarObject(
            name='Dunstan',
            short_description='A gas giant whose fuel processing once serviced the fleet -- now producing for internal consumption and the occasional passing freighter.',
            long_description=(
                'Dunstan is the system\'s gas giant -- a large body in the outer system '
                'whose moons hosted fuel processing operations that once serviced the '
                'freight fleet that carried Sabix\'s industrial output to the rest of the '
                'galaxy. The fuel processing continues at reduced capacity, producing for '
                'the system\'s internal consumption and the modest traffic that still passes '
                'through. The surplus capacity has been mothballed -- the processing '
                'platforms maintained but idle, their operators reassigned to other work or '
                'retired.\n\n'
                'The fuel workers who remain are the system\'s most pragmatic residents. '
                'They do not romanticise the industrial era or mourn its passing. The fuel '
                'is needed. They produce it. The quantity has changed. The work has not. '
                'They regard the nostalgia that pervades the rest of the system with a '
                'patience that borders on exasperation. The past was work, they point out. '
                'The present is also work. The difference is that the present is quieter, '
                'and they are not convinced this is a bad thing.'
            ),
            population=40_000_000,
        ),
    ],
    short_description='A former industrial powerhouse in graceful decline -- ten billion people living well in a system built for a purpose that economics took away.',
    long_description=(
        'Sabix was one of the most important systems in the inner systems. For two '
        'centuries, the heavy metals and rare earth elements in Harsten\'s crust fed '
        'the foundries on Kellaway that fed the orbital shipyards that built a '
        'significant fraction of the inner systems\' fleet. Sabix\'s output built the '
        'infrastructure of interstellar civilisation. The workers who lived here knew '
        'they mattered. The system\'s wealth, its grandeur, its architecture, its '
        'culture -- all of it was built on the pride of people who were building the '
        'galaxy.\n\n'
        'The industry left. Richer deposits in younger systems offered cheaper '
        'extraction. The shipyards in Tau Ceti could be supplied from closer sources. '
        'The contracts moved. The foundries scaled back. The mines reduced to skeleton '
        'crews. The decline was not catastrophic -- nobody starved, nobody suffered, '
        'MERIT\'s guarantees ensured that the population\'s basic needs were met '
        'regardless of economic output. What the population lost was not comfort but '
        'purpose. The cities that were built for industrial workers house people who '
        'work in services. The shipyards are a tourist attraction. The foundries are '
        'universities and cultural centres. The museums celebrating the industrial era '
        'are the most visited sites in the system.\n\n'
        'Ten billion people live in Sabix, and their lives are fine. The infrastructure '
        'is good. The housing is spacious. The parks are beautiful. The quality of life '
        'exceeds most inner-system colonies by the measurable metrics that MERIT tracks. '
        'What the metrics do not measure is the listlessness -- the sense that the '
        'system exists because it was built during an era that needed it and persists '
        'into an era that does not. The younger generation did not experience the '
        'industrial era and does not share the older generation\'s grief, but they have '
        'inherited a civilisation shaped by a purpose they cannot participate in, and '
        'the question of what Sabix is for, now that it is no longer for what it was '
        'built for, is the system\'s quiet, persistent, unanswered question.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

ALGOL = System(
    name='Algol',
    star='Triple system: Algol A (B8V blue-white, ~180 times Sol luminosity) eclipsed every 2.87 days by Algol B (K2IV orange subgiant) for approximately ten hours, with a distant companion Algol C',
    population=250_000,
    distance_to_sol=90.0,
    stellar_objects=[
        StellarObject(
            name='Tessemer',
            short_description='A fully terraformed, perfectly habitable world -- breathable air, temperate climate, empty cities. Nobody could stand to live here.',
            long_description=(
                'Tessemer is a success. The terraforming is complete. The atmosphere is '
                'breathable. The climate is temperate. The cities were built -- MERIT-'
                'standard, well-planned, designed for millions. The agricultural zones are '
                'established. The infrastructure is in place. By every measurable metric, '
                'Tessemer is a habitable world ready for colonisation. The colonists came. '
                'The colonists left.\n\n'
                'The problem is the Eye. Every 2.87 standard days, the primary star dims '
                'as its orange companion passes in front of it. The dimming lasts '
                'approximately ten hours. The light drops to roughly a third of its normal '
                'intensity. The sky darkens. The shadows shift. The colours change. Then '
                'the companion passes and the full light returns. The cycle repeats, every '
                '2.87 days, with the mechanical regularity of a blink.\n\n'
                'MERIT does not understand why this is unbearable. The dimming is well '
                'within the range of variation that humans tolerate on other worlds -- '
                'cloud cover on a stormy day produces a greater reduction in light. The '
                'cycle is predictable, regular, and scientifically unremarkable. But the '
                'effect on the people who live beneath it is not scientifically '
                'unremarkable. The colonists described a deep, instinctual unease that '
                'began within days of arrival and worsened over time. The dimming felt '
                'wrong. Not dangerous, not painful, not rationally threatening -- wrong in '
                'a way that bypassed conscious thought and settled in the body. Sleep '
                'deteriorated. Anxiety increased. Concentration suffered. Interpersonal '
                'conflicts spiked during the dimming hours and did not fully subside '
                'between cycles. The colonists who stayed longest described the sensation '
                'as being watched by something that was not there, a feeling that peaked '
                'each time the star began to dim and never entirely faded.\n\n'
                'The psychologists studied it. The reports were inconclusive. Something '
                'about the rhythm -- the regularity, the predictability, the specific '
                'timescale of the dimming -- triggers a response that appears to be '
                'hardwired. Not learned, not cultural, not rational. An evolutionary '
                'artefact buried so deep in the human nervous system that it cannot be '
                'trained away or medicated out. The colonists were withdrawn. The cities '
                'were abandoned. Tessemer stands empty -- a perfectly habitable world with '
                'clean air and temperate weather and cities ready for occupation, and nobody '
                'who can bear to live in them.'
            ),
            population=0,
        ),
        StellarObject(
            name='Draven',
            short_description='The second terraformed world -- warmer, lusher, and equally uninhabitable for the same reason that has nothing to do with the planet.',
            long_description=(
                'Draven was the system\'s second colonisation target -- a warmer world '
                'closer to the star, terraformed in parallel with Tessemer, intended as an '
                'agricultural complement. The terraforming was successful. The world is '
                'lush, productive, and empty.\n\n'
                'The colonists on Draven reported the same symptoms as those on Tessemer, '
                'but worse. The closer orbit means the dimming is more pronounced -- the '
                'light drop is sharper, the shadow shift more dramatic, and the return of '
                'full brightness more jarring. The colonists on Draven lasted less time '
                'than those on Tessemer before requesting evacuation. Several refused to '
                'wait for scheduled transport and left on whatever ships were available. '
                'The evacuation reports noted that the departing colonists displayed visible '
                'relief upon leaving the planetary surface that intensified as they moved '
                'out of the ecliptic plane and the dimming cycle became less pronounced.\n\n'
                'Draven\'s abandoned settlements are smaller than Tessemer\'s -- the colony '
                'was younger when it was evacuated. The agricultural infrastructure remains '
                'intact. The engineered ecosystems that the terraformers established '
                'continue to function without human intervention, the crops growing and '
                'dying in seasonal cycles that nobody harvests. The planet is a garden '
                'with no gardener, producing food that nobody eats, under a sky that '
                'nobody can endure.'
            ),
            population=0,
        ),
        StellarObject(
            name='Ashenmere',
            short_description='A third world whose terraforming was halted mid-process when the first two colonies failed -- half-finished and untouched since.',
            long_description=(
                'Ashenmere was designated as the system\'s third colonisation target -- a '
                'cooler world further from the star that was in the early stages of '
                'atmospheric terraforming when the evacuations from Tessemer and Draven '
                'made it clear that the problem was not the planets. The terraforming was '
                'halted. The atmospheric processors were shut down mid-cycle. The planet '
                'is half-terraformed -- the atmosphere partially converted, breathable in '
                'some regions with a respirator and toxic in others.\n\n'
                'Ashenmere is the system\'s most visible waste. The investment in the '
                'terraforming equipment, the atmospheric processors, the orbital '
                'infrastructure -- all of it abandoned when MERIT concluded that no amount '
                'of planetary engineering could address a problem rooted in human neurology. '
                'The processors stand on the surface, intact, waiting for a command that '
                'nobody intends to send.'
            ),
            population=0,
        ),
        StellarObject(
            name='Kestrel Station',
            short_description='A monitoring station in an inclined orbit -- keeping the terraformed worlds under observation from an angle that minimises the wink.',
            long_description=(
                'Kestrel Station is one of three small stations that MERIT maintains in '
                'the Algol system, orbiting in a plane inclined steeply to the ecliptic. '
                'The inclined orbit is deliberate: from the ecliptic plane, the dimming '
                'cycle is experienced fully. From a sufficiently inclined orbit, the '
                'geometry changes -- the companion\'s transit across the primary is partial '
                'or absent depending on the inclination, and the dimming effect is reduced. '
                'It is not eliminated. The crew of Kestrel Station still perceive the '
                'cycle, still feel a faint version of the unease that drove the colonists '
                'from the surface. But it is manageable. Barely.\n\n'
                'Kestrel\'s crew monitors the terraformed worlds -- tracking the atmospheric '
                'conditions on Tessemer and Draven, maintaining the infrastructure remotely '
                'where possible, and producing the reports that MERIT uses to justify not '
                'writing off the investment entirely. The crew rotate on short postings -- '
                'three months is standard, and extensions are not requested. The personnel '
                'who serve on Kestrel describe a low-grade discomfort that they cannot '
                'fully articulate: a sense that something is not right, a difficulty '
                'sleeping that does not correspond to any diagnosable condition, a tendency '
                'to avoid the observation ports that face the star. They function. They '
                'perform their duties. They are glad to leave.'
            ),
            population=85_000,
        ),
        StellarObject(
            name='Mercer Station',
            short_description='A research station studying the phenomenon -- trying to understand why a predictable, harmless light variation makes human beings unable to function.',
            long_description=(
                'Mercer Station is the research facility dedicated to understanding the '
                'Algol effect -- the term that the psychologists and neurologists have '
                'given to the instinctual response that the dimming cycle provokes. The '
                'station orbits in the same inclined plane as Kestrel, reducing but not '
                'eliminating the effect on the research staff, who study their own '
                'discomfort as part of the dataset.\n\n'
                'The research has produced extensive documentation and no answers. The '
                'response is universal -- every human tested reacts to the cycle, '
                'regardless of cultural background, psychological profile, or prior '
                'knowledge of the system. The response scales with exposure: surface '
                'dwelling is intolerable within weeks, inclined orbital habitation is '
                'uncomfortable indefinitely. The response does not habituate -- extended '
                'exposure does not produce adaptation. The response appears to originate '
                'in the limbic system, below conscious processing, and cannot be '
                'suppressed through cognitive techniques or medication without sedating '
                'the subject to the point of non-function.\n\n'
                'The leading hypothesis is that the specific timescale and character of '
                'the dimming -- the 2.87-day cycle, the ten-hour duration, the particular '
                'quality of the light shift -- coincidentally matches a pattern that the '
                'human threat-detection system is hardwired to respond to. What that '
                'pattern corresponds to in evolutionary terms -- what predator or hazard '
                'in humanity\'s deep past produced a response to this specific stimulus -- '
                'is unknown. The researchers have theories. None are satisfying. The Eye '
                'winks, and something very old in the human brain flinches.'
            ),
            population=60_000,
        ),
        StellarObject(
            name='Cordale Station',
            short_description='A logistics station handling supply runs to the other two stations -- the smallest permanent presence, staffed by people who do not stay long.',
            long_description=(
                'Cordale Station is the system\'s logistics hub -- a small facility that '
                'receives supply shipments from the inner systems and distributes them to '
                'Kestrel and Mercer. The station orbits in the same inclined plane and '
                'experiences the same reduced-but-present discomfort as the other '
                'installations. The crew is the smallest of the three stations and the '
                'most transient -- logistics personnel rotating through on assignments '
                'that are short even by Algol standards.\n\n'
                'Cordale\'s crew are the people who interact most with the outside world, '
                'receiving the supply ships whose crews transit into the system, unload '
                'as quickly as possible, and leave. The supply crews do not linger. The '
                'system\'s reputation precedes it -- pilots who have made the Algol run '
                'describe the experience as unsettling even on a brief transit, and the '
                'docking procedures at Cordale are the fastest in the inner systems because '
                'everyone involved wants to minimise the time spent here. The Cordale crew '
                'have become accustomed to being treated like the caretakers of a haunted '
                'house. They do not argue with the characterisation.'
            ),
            population=30_000,
        ),
        StellarObject(
            name='Mordren',
            short_description='A gas giant in the outer system -- surveyed for fuel processing, never developed, because nobody wanted to spend the additional time in the system to build it.',
            long_description=(
                'Mordren is a large gas giant in the outer system that the original '
                'colonisation plan designated as the system\'s fuel source. The surveys were '
                'completed. The processing infrastructure was never built. The colonisation '
                'plan assumed a growing population that would need fuel for interplanetary '
                'transit and industrial operations. The population grew to zero. The fuel '
                'processing was never initiated, and the ships that supply the stations '
                'carry their own fuel from the inner systems rather than refuel locally, '
                'because refuelling locally would mean staying longer.'
            ),
            population=0,
        ),
    ],
    short_description='The Demon\'s Eye -- three perfectly terraformed worlds that nobody can bear to live on, watched by skeleton crews who orbit at angles to avoid the wink.',
    long_description=(
        'Algol is a system that should work and does not. The triple star\'s primary is '
        'a bright blue-white that provides ample energy and light. Three worlds were '
        'terraformed -- one fully, one fully, one partially -- at enormous expense, '
        'producing habitable conditions that would be the envy of any frontier colony. '
        'The cities were built. The colonists arrived. The colonists could not stay.\n\n'
        'Every 2.87 standard days, the orange companion star passes in front of the '
        'primary. The light dims to a third of its intensity for approximately ten '
        'hours. Then it returns. The cycle is predictable, regular, and triggers a '
        'response in the human nervous system that decades of research have failed to '
        'explain or mitigate. The colonists who lived beneath the cycle described a '
        'deep, instinctual wrongness -- not fear, not pain, but a pervasive unease '
        'that worsened with every dimming and never fully subsided between them. Sleep '
        'deteriorated. Anxiety mounted. The sensation of being watched by something '
        'absent intensified until the colonists requested evacuation, and MERIT, unable '
        'to identify a cause or a cure, complied.\n\n'
        'The system is now maintained by a quarter of a million people on three small '
        'stations in orbits inclined steeply to the ecliptic, where the geometry of '
        'the companion\'s transit is reduced and the dimming effect is manageable but '
        'not absent. The crews rotate on short postings. They function. They are '
        'uncomfortable in ways they struggle to describe. The research station studies '
        'the phenomenon and has produced extensive documentation and no answers. '
        'Something in the specific timescale and character of the dimming coincides '
        'with a threat-response pattern that is hardwired into the human brain at a '
        'level below conscious access. What evolutionary pressure produced a response '
        'to this particular stimulus is unknown.\n\n'
        'Below the stations, three terraformed worlds sit empty. Tessemer\'s cities '
        'stand ready for millions. Draven\'s crops grow and die unharvested. '
        'Ashenmere\'s half-finished atmosphere drifts in an incomplete equilibrium. '
        'The investment is enormous. The loss is written off. The Eye winks every '
        '2.87 days, and something very old in the human brain flinches, and the worlds '
        'that MERIT built remain the most habitable uninhabited planets in the galaxy.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

RUCHBAH = System(
    name='Ruchbah',
    star='Blue-white subgiant (A5III-IV), approximately 63 times Sol luminosity',
    population=6_000_000_000,
    distance_to_sol=99.4,
    stellar_objects=[
        StellarObject(
            name='Tavion',
            short_description='The capital world -- a temperate planet of five billion people living ordinary lives in the shadow of the most ambitious engineering project in human history.',
            long_description=(
                'Tavion is a habitable, temperate world that would be unremarkable in any '
                'other system. The cities are well-run. The economy is diversified. The '
                'quality of life is solidly mid-tier by inner-system standards. Five billion '
                'people live on Tavion, and most of them work in occupations that have '
                'nothing to do with the reason their system is famous. They are teachers, '
                'farmers, engineers, administrators, service workers -- the ordinary '
                'population of an ordinary world that happens to share a system with the '
                'most ambitious engineering project in human history.\n\n'
                'The project is visible from Tavion\'s surface on clear nights. The orbital '
                'infrastructure around Sethane -- the world being moved -- is large enough '
                'to register as a faint point of light that the residents can identify and '
                'that children learn to point out the way children in Sol learn to identify '
                'Mars. The project is a source of local pride in a mild, background way: '
                'the residents did not build it, do not operate it, and have no say in '
                'whether it continues, but it is happening in their system and that makes '
                'the system significant in a way it otherwise would not be.\n\n'
                'The relationship between Tavion\'s ordinary civilisation and the world-'
                'engine project is largely one of proximity without participation. MERIT '
                'runs the project. MERIT makes the decisions. The population of Tavion '
                'benefits from the elevated traffic -- the engineers, researchers, and '
                'support staff who rotate through the system spend money on Tavion during '
                'leave -- but they are spectators to the main event, and they have made '
                'peace with this.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='Sethane',
            short_description='The world being moved -- a rocky planet in a marginal orbit, slowly and measurably being pushed into a more habitable position by the world-engine.',
            long_description=(
                'Sethane is the subject of the experiment. The planet is rocky, roughly '
                'Earth-sized, with a thin atmosphere and surface conditions that are '
                'marginal for habitation -- too cold, too far from the star, the kind of '
                'world that conventional terraforming could make liveable but never '
                'comfortable. The world-engine is intended to change this by changing the '
                'one variable that terraforming cannot address: the orbit itself.\n\n'
                'The world-engine is a network of gravitational manipulation installations '
                'derived from inertial resonator technology, positioned in orbit around '
                'Sethane and on the surface. The installations generate carefully calibrated '
                'gravitational asymmetries that produce a net force on the planet -- '
                'infinitesimal by planetary standards but sustained continuously, year after '
                'year, decade after decade. The effect is measurable. Sethane\'s orbit has '
                'shifted inward by a fraction of a percent since the project began over a '
                'century ago. The shift is confirmed by independent measurement. The planet '
                'is moving.\n\n'
                'The rate is agonisingly slow by human timescales. At the current rate, '
                'Sethane will reach its target orbit -- the optimum position for long-term '
                'habitability -- in approximately eight centuries. The engineers are working '
                'to accelerate this. Each generation of the gravitational manipulation '
                'technology is more powerful than the last, and the projections have been '
                'revised downward repeatedly -- the original estimate was millennia. But '
                'eight centuries is still eight centuries, and Sethane today is a cold, '
                'marginal world surrounded by the machinery that is moving it, slowly, '
                'toward a future that nobody alive will see.\n\n'
                'The surface installations are enormous -- industrial-scale gravitational '
                'generators anchored to the bedrock, their housings the size of cities, '
                'powered by the planet\'s own position in the star\'s gravity well through '
                'the same resonator principles that make the technology possible. The '
                'installations are maintained by a resident engineering team that lives in '
                'enclosed habitats on the surface -- cold, functional, and sustained by the '
                'knowledge that the work they are doing, if it succeeds, will transform '
                'the future of colonisation.'
            ),
            population=45_000_000,
        ),
        StellarObject(
            name='The Cradle',
            short_description='The orbital research and command station above Sethane -- where the world-engine is monitored and the next generation of gravitational manipulation is developed.',
            long_description=(
                'The Cradle is the project\'s command station -- a large orbital installation '
                'above Sethane that houses the researchers, engineers, and administrators '
                'who run the world-engine. The station monitors the surface installations, '
                'tracks the orbital shift with instruments sensitive enough to detect '
                'movement measured in metres per year across a planetary orbit, and '
                'coordinates the ongoing research into improving the technology.\n\n'
                'The research is the project\'s real output. The world-engine on Sethane is '
                'a prototype -- proof that the concept works, that a planet\'s orbit can be '
                'changed by sustained gravitational manipulation. The value is not Sethane '
                'itself, which is one marginal world in one system. The value is what the '
                'technology represents: the ability to move worlds. If the gravitational '
                'manipulation can be refined, scaled, and made faster, it transforms '
                'terraforming. Every marginal planet in the galaxy -- every world that is '
                'too far from its star, or too close, or in an eccentric orbit that makes '
                'conventional terraforming impractical -- becomes a candidate. The number '
                'of habitable worlds in the galaxy increases by an order of magnitude.\n\n'
                'MERIT understands the stakes. The Cradle is one of the most generously '
                'funded research installations in the inner systems, staffed by the best '
                'gravitational physicists and resonator engineers available. The work is '
                'slow because the physics is difficult, not because the resources are '
                'lacking. Each incremental improvement in the gravitational manipulation '
                'technology is tested on Sethane\'s surface installations, and each '
                'improvement brings the projected timeline down. The original estimate was '
                'millennia. The current estimate is eight centuries. The researchers believe '
                'they can bring it under five hundred years within the next decade. The '
                'goal -- the real goal, the one that MERIT is funding -- is to bring it '
                'under a century, which would make orbital adjustment a practical '
                'terraforming tool rather than a theoretical curiosity.'
            ),
            population=120_000_000,
        ),
        StellarObject(
            name='Carren',
            short_description='A warm second world -- agricultural, supplying both Tavion and the project\'s workforce.',
            long_description=(
                'Carren is the system\'s second habitable world -- warmer than Tavion, '
                'closer to the star, with fertile soil and a climate that supports '
                'year-round agriculture. The planet feeds the system: Tavion\'s five '
                'billion, the project\'s workforce on Sethane and the Cradle, and the '
                'various stations and facilities that the project has generated. Carren\'s '
                'role is unglamorous and essential -- the agricultural base that sustains '
                'the civilisation that sustains the experiment.\n\n'
                'The population is agricultural and content in the way that farming '
                'communities tend to be when the climate cooperates and the markets are '
                'stable. Carren\'s residents follow the project\'s progress the way farmers '
                'everywhere follow news that affects their customers -- with attention to '
                'the practical implications and limited interest in the theoretical details. '
                'The world-engine is important because it keeps the engineers employed, and '
                'employed engineers buy food. The physics is someone else\'s department.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Pallant',
            short_description='A gas giant whose fuel processing supports the system\'s elevated traffic -- busier than a system of this size would normally warrant.',
            long_description=(
                'Pallant is the system\'s gas giant -- fuel processing on its moons '
                'supporting a volume of traffic that is higher than the system\'s population '
                'would suggest. The world-engine project draws a constant flow of supply '
                'ships, personnel transports, and the specialised vessels that deliver '
                'equipment and components to Sethane\'s surface installations. The fuel '
                'processing on Pallant\'s moons was expanded twice in the project\'s '
                'lifetime to accommodate the demand, and the operations are now the most '
                'active industrial activity in the system outside the project itself.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Ruchbah Gate',
            short_description='The system\'s orbital port -- handling the project\'s logistics alongside ordinary system traffic.',
            long_description=(
                'Ruchbah Gate is the system\'s primary orbital port -- a station above '
                'Tavion that handles both the ordinary traffic of a mid-tier inner system '
                'and the project-related logistics that have become a significant fraction '
                'of the system\'s total throughput. The station maintains separate processing '
                'streams for civilian and project traffic, the latter handled by MERIT '
                'personnel with clearances that the civilian staff do not have and do not '
                'ask about.\n\n'
                'The project has made Ruchbah Gate busier than it would otherwise be -- '
                'the system\'s population does not justify the traffic volume, but the '
                'constant flow of project-related ships keeps the station active and the '
                'commercial district profitable. The restaurants and bars near the project '
                'processing stream do steady business with engineers on leave, and the '
                'conversations overheard in those bars are about gravitational asymmetries '
                'and resonator efficiency curves and whether the timeline can be brought '
                'under five centuries, which is not typical bar conversation in most systems '
                'but is entirely normal here.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Torfeld',
            short_description='A hot inner world -- standard solar collection, notable only because the energy output partially feeds the world-engine\'s surface installations.',
            long_description=(
                'Torfeld is a hot, dense inner world with solar collection arrays that '
                'provide energy for the system\'s standard needs and supplement the power '
                'supply for Sethane\'s surface installations. The world-engine\'s '
                'gravitational generators are primarily powered by the resonator principle '
                '-- drawing energy from the star\'s gravity well -- but the supplemental '
                'energy from Torfeld\'s arrays supports the ancillary systems: the '
                'habitats, the maintenance equipment, the communications infrastructure. '
                'Torfeld\'s contribution is modest but necessary, and the engineering staff '
                'who maintain the arrays are aware that their work supports the most '
                'important experiment in human history, which makes the routine maintenance '
                'feel slightly more significant than it would elsewhere.'
            ),
            population=8_000_000,
        ),
    ],
    short_description='Home of the world-engine -- a prototype for the next generation of terraforming, slowly moving a planet toward a habitable orbit.',
    long_description=(
        'Ruchbah is an ordinary system hosting an extraordinary experiment. Six billion '
        'people live here, most of them on Tavion, a temperate world that would be '
        'unremarkable in any other context. The system is moderately connected to the '
        'inner systems by easy jump links, safely distant from every contested border, '
        'and would be forgettable if not for what is happening to Sethane.\n\n'
        'Sethane is being moved. The world-engine -- a network of gravitational '
        'manipulation installations derived from inertial resonator technology -- is '
        'slowly, measurably pushing the planet from a marginal outer orbit toward a '
        'position where long-term habitability becomes possible. The project has been '
        'underway for over a century. The orbit has shifted by a fraction of a percent. '
        'The current estimate for reaching the target orbit is eight centuries, revised '
        'downward from the original projection of millennia as the technology improves '
        'with each generation.\n\n'
        'The world-engine is a prototype. The value is not Sethane -- one marginal '
        'world in one system -- but what the technology represents. If gravitational '
        'manipulation can be refined and accelerated to the point where orbital '
        'adjustment takes decades rather than centuries, it transforms terraforming. '
        'Every marginal planet in the galaxy -- every world too far from its star, too '
        'close, or in an orbit that conventional methods cannot fix -- becomes a viable '
        'colony. The number of habitable worlds increases by an order of magnitude. '
        'MERIT understands the stakes and funds the project accordingly. The Cradle, '
        'the orbital research station above Sethane, is one of the most generously '
        'funded installations in the inner systems.\n\n'
        'The rest of the system lives alongside the experiment without participating '
        'in it. Tavion\'s population watches the progress from a distance -- a faint '
        'point of light in the night sky that represents the most ambitious engineering '
        'project in human history. Carren grows the food. Pallant processes the fuel. '
        'The engineers on Sethane and the Cradle work on a problem whose solution, if '
        'it comes, will matter more than anything else their civilisation has achieved. '
        'The planet moves. The measurements confirm it. The timeline shortens with '
        'each improvement. And somewhere in the future that nobody alive will see, a '
        'cold world will reach the orbit where it can become a home, and the '
        'technology that moved it will begin moving others.'
    ),
    cluster=StarClusters.INNER_SYSTEMS,
)

INNER_SYSTEMS: list[System] = [
    SOL,
    ALPHA_CENTAURI,
    SIRIUS,
    EPSILON_ERIDANI,
    PROCYON,
    TAU_CETI,
    ALTAIR,
    VEGA,
    FOMALHAUT,
    POLLUX,
    DENEBOLA,
    ARCTURUS,
    CAPELLA,
    RASALHAGUE,
    ALDERAMIN,
    CASTOR,
    CAPH,
    ZOSMA,
    SHERATAN,
    ALDEBARAN,
    HAMAL,
    NUKALI,
    ALPHECCA,
    GENUBI,
    MIZAR,
    REGULUS,
    HERAK,
    MEGREZ,
    ANGIRAS,
    KALINAN,
    PHEDA,
    BARGHAL,
    GADDACK,
    SABIX,
    ALGOL,
    RUCHBAH,
]
