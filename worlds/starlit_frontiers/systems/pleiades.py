from ..enums import StarClusters
from .models import System, StellarObject

ALCYONE = System(
    name='Alcyone',
    star='Blue-white giant (B7IIIe), approximately 2,000 times Sol luminosity -- the brightest star in the Pleiades, casting cold blue light over the most terraformed system in a cluster that has largely stopped bothering to terraform',
    population=11_000_000_000,
    distance_to_sol=440.0,
    stellar_objects=[
        StellarObject(
            name='Kalstren',
            short_description='The gateway world -- six billion people in the cluster\'s most terraformed system, where the air is almost normal and the diplomatic class pretends that the rest of the Pleiades is like this.',
            long_description=(
                'Kalstren is the Pleiades at its most presentable. The planet has been '
                'terraformed to near-baseline conditions -- breathable atmosphere, stable '
                'climate, managed biosphere. The alien life that originally occupied '
                'Kalstren has been pushed to the margins: domesticated species in managed '
                'preserves, useful organisms integrated into the agricultural system, and '
                'the rest contained in wilderness zones that the terraforming did not '
                'reach. Kalstren is the system the Pleiades shows visitors, and the '
                'system works hard to justify the showing.\n\n'
                'The population on Kalstren is the least modified in the cluster. The '
                'terraforming has made deep splicing unnecessary -- the environment is '
                'human-compatible, so the humans do not need to become something else to '
                'survive it. The modifications that Kalstren\'s population carries are '
                'modest: minor immune adaptations for the local pathogens, slight '
                'respiratory adjustments for an atmosphere that is close to baseline but '
                'not identical, and the cosmetic gene-splicing that the wealthy use for '
                'aesthetic purposes -- alien pigmentation patterns, bioluminescent skin '
                'accents, the fashionable modifications that the diplomatic class wears '
                'like jewellery.\n\n'
                'The diplomatic class is Kalstren\'s defining population. These are the '
                'moderately modified Pleiadians who represent the confederation at the '
                'cluster level -- baseline-compatible enough to travel between worlds, '
                'to breathe the atmospheres on Atlas, to dock at MERIT stations without '
                'triggering the biological screening. The deeply adapted populations on '
                'the outer worlds consider the diplomats tourists in their own '
                'civilisation -- people who carry enough alien genes to claim membership '
                'but not enough to understand what membership costs on a world that has '
                'not been made safe for human bodies.\n\n'
                'The military presence is substantial. Alcyone is the gateway -- all '
                'traffic in and out of the cluster passes through, and the fleet that '
                'guards the gateway is the Pleiades\' first line of defence against MERIT. '
                'The warships are the Pleiadian standard: light, stripped-down, crewed by '
                'personnel spliced for vacuum tolerance and radiation resistance, carrying '
                'minimal life support because the crews do not need it. The ships are '
                'cold, dark, and nearly invisible on sensors designed for vessels with '
                'human-standard atmospherics. The fleet\'s advantage is not firepower but '
                'stealth -- the difficulty of finding and targeting ships that register on '
                'sensors as debris rather than vessels.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='Orvanne',
            short_description='A second terraformed world -- warmer, wetter, with alien life more visible in the ecosystem and the first hint that the Pleiades is not as baseline as Kalstren pretends.',
            long_description=(
                'Orvanne is Alcyone\'s second habitable world -- warmer than Kalstren, '
                'wetter, with a biosphere where the alien life has been integrated rather '
                'than contained. The terraforming on Orvanne was less thorough than '
                'Kalstren\'s -- the alien organisms were adapted into the ecosystem instead '
                'of pushed to the margins, and the result is a world where the parks have '
                'alien trees, the rivers have alien fish, and the birds that cross the '
                'skyline at sunset are not birds but something that fills the same niche '
                'with a different evolutionary ancestry.\n\n'
                'The population on Orvanne is slightly more modified than Kalstren\'s -- '
                'the immune adaptations are deeper because the alien organisms are more '
                'present, and some of the population carries spliced digestive enzymes '
                'that let them eat the alien-origin food that the integrated biosphere '
                'produces. The modifications are minor by Pleiadian standards but visible '
                'to baseline visitors: slightly different skin tone from the alien '
                'pigmentation genes, the faintly iridescent quality in the eyes that comes '
                'from the visual-spectrum adaptation, and the other small differences that '
                'mark a person as Pleiadian even at the gateway\'s mildest.\n\n'
                'Orvanne is where MERIT visitors first encounter the alien life that '
                'defines the Pleiades. The experience is disorienting -- the trees look '
                'almost right, the animals behave almost normally, and the food tastes '
                'almost familiar, but the almost is constant and cumulative. Visitors '
                'describe the feeling as walking through a world that is trying to be '
                'Earth and not quite succeeding, which is exactly what it is.'
            ),
            population=2_500_000_000,
        ),
        StellarObject(
            name='The Conservatory',
            short_description='An orbital research station cataloguing the alien species brought from every system in the cluster -- the largest collection of non-terrestrial life in the galaxy.',
            long_description=(
                'The Conservatory is an orbital station above Kalstren that houses the '
                'Pleiades\' central catalogue of alien life. Specimens from every system in '
                'the cluster are brought here -- organisms from the extreme environments '
                'of the outer worlds, the unique species from Electra\'s biosphere, the '
                'dangerous fauna from the quarantined worlds, all maintained in controlled '
                'habitats that replicate the conditions of their home environments.\n\n'
                'The Conservatory is the largest collection of non-terrestrial life in the '
                'galaxy. The habitats contain organisms that breathe chlorine, organisms '
                'that metabolise heavy metals, organisms that have evolved radiation '
                'resistance that human bioengineers are still trying to understand, and the '
                'deep-ocean species from worlds with crushing atmospheric pressure whose '
                'cellular structures hold clues to the next generation of human adaptation. '
                'The catalogue is the foundation of the cluster\'s gene-splicing industry '
                '-- every modification available in the Pleiades began as a gene sequence '
                'identified in a specimen at the Conservatory.\n\n'
                'The animal testing facilities are attached to the Conservatory. The '
                'testing is where the gene splicing is validated before human application '
                '-- baseline animals modified with alien sequences, observed for '
                'compatibility, monitored for cascading effects. The testing wings are '
                'not open to visitors. The specimens in the testing wings include the '
                'successes -- animals that have incorporated alien genes and function -- '
                'and the failures. The failures are alive. Some of them should not be.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Terminus Station',
            short_description='The system\'s primary orbital port -- where the strain diplomats arrive, the MERIT intelligence operatives pretend to be traders, and the biological screening is the most sophisticated in the galaxy.',
            long_description=(
                'Terminus Station is Alcyone\'s primary orbital facility -- the busiest '
                'port in the Pleiades and the one with the most sophisticated biological '
                'screening in the galaxy. Every arrival is screened -- not for weapons or '
                'contraband but for biological compatibility. The screening determines '
                'what the visitor\'s body can tolerate: which atmospheres, which food, '
                'which pathogens the visitor\'s immune system can handle. The results '
                'determine which worlds the visitor is cleared to visit. A baseline human '
                'from MERIT space is cleared for Kalstren and Orvanne. The outer worlds '
                'require modifications the visitor does not carry and environments the '
                'visitor cannot survive.\n\n'
                'The station handles the strain diplomats who arrive from across the '
                'cluster for confederation business -- representatives of populations so '
                'biologically divergent that some require different atmospheric mixes in '
                'their quarters. The station\'s life support is modular: sections can be '
                'pressurised to different levels, filled with different atmospheric '
                'compositions, and maintained at different temperatures to accommodate the '
                'range of biological requirements that the confederation\'s representatives '
                'bring. A station that must house people who breathe different air is a '
                'station that has redefined what the word people means.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Belvara',
            short_description='A gas giant with fuel processing at gateway scale -- its upper atmosphere home to alien gas-dwelling organisms that the researchers are still classifying.',
            long_description=(
                'Belvara is the system\'s gas giant -- fuel processing on its moons '
                'supporting the gateway\'s heavy traffic. The gas giant is notable for '
                'the alien life in its upper atmosphere -- gas-dwelling organisms that '
                'float in the hydrogen-helium layers, filtering chemical compounds from '
                'the atmospheric currents. The organisms are large, slow-moving, and '
                'poorly understood -- the researchers at the Conservatory have catalogued '
                'twelve distinct species and suspect there are more in the deeper layers '
                'that the survey probes cannot reach.\n\n'
                'The fuel processing operations avoid the atmospheric layers where the '
                'organisms concentrate, partly for research preservation and partly '
                'because the organisms\' biochemistry corrodes the processing equipment '
                'in ways the engineers find expensive. The gas-dwellers are not dangerous. '
                'They are simply incompatible with the machinery, which is a concise '
                'summary of the relationship between alien life and human infrastructure '
                'across the entire cluster.'
            ),
            population=150_000_000,
        ),
        StellarObject(
            name='Grothane',
            short_description='An agricultural world feeding the gateway -- the most conventional farming in the cluster, using terrestrial crops on terraformed soil because Alcyone can afford to do it the expensive way.',
            long_description=(
                'Grothane is the system\'s agricultural world -- and one of the few places '
                'in the Pleiades where the farming looks like farming anywhere else in the '
                'galaxy. The soil has been terraformed. The crops are terrestrial. The '
                'livestock are baseline. The food produced on Grothane is edible by any '
                'human, regardless of modification level -- a distinction that matters '
                'because the food produced on the outer worlds is often not.\n\n'
                'Alcyone can afford terrestrial agriculture because Alcyone was terraformed '
                'early and thoroughly. The outer systems, where the terraforming was '
                'partial or never attempted, grow food from alien-hybrid crops that the '
                'local population can eat and that baseline visitors cannot. Grothane\'s '
                'baseline food is exported to the outer systems as a supplement -- the '
                'food that the diplomats and the travellers and the moderately modified '
                'political class eat when they visit worlds where the local cuisine would '
                'kill them.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='Scolden',
            short_description='A hot inner world -- energy collection and the biological quarantine facilities where incoming alien specimens are screened before transfer to the Conservatory.',
            long_description=(
                'Scolden is a hot inner world with solar collection arrays and the '
                'biological quarantine facilities that screen alien specimens arriving from '
                'the outer systems before they are transferred to the Conservatory. The '
                'quarantine is essential -- organisms from the outer worlds may carry '
                'pathogens, parasites, or biochemical properties that are safe in their '
                'native environment and catastrophic in a terraformed one. The screening '
                'process is thorough, slow, and occasionally fails, which is why the '
                'quarantine is conducted on Scolden rather than anywhere near the '
                'inhabited worlds.\n\n'
                'The quarantine failures are the reason the facility is here -- a hot '
                'inner world where a containment breach is sterilised by the environment '
                'rather than managed by the staff. The heat does not discriminate between '
                'alien organisms and human error. The staff work in sealed environments '
                'and carry minor thermal-resistance splicing that lets them tolerate the '
                'conditions. The posting is unpopular and important.'
            ),
            population=20_000_000,
        ),
    ],
    short_description='Gateway to the Pleiades -- eleven billion people in the cluster\'s most terraformed system, where the alien life is managed, the modifications are mild, and the diplomats pretend this is representative.',
    long_description=(
        'Alcyone is the front door to the Pleiades cluster -- the most terraformed '
        'system in a cluster that has largely stopped bothering to terraform. The '
        'gateway is the Pleiades at its most presentable: breathable atmospheres, '
        'managed biospheres, and a population whose modifications are modest enough '
        'that MERIT visitors can look at them without flinching. Kalstren and Orvanne '
        'are habitable by baseline humans, which is true of almost no other world in '
        'the cluster.\n\n'
        'The diplomatic class lives here -- the moderately modified Pleiadians who '
        'represent the strain confederation, baseline-compatible enough to travel '
        'between worlds and breathe the atmospheres on Atlas and dock at MERIT '
        'stations without triggering the biological screening. The deeply adapted '
        'populations on the outer worlds consider the diplomats tourists in their own '
        'civilisation: people who carry enough alien genes to claim membership but '
        'not enough to understand what membership costs on a world that has not been '
        'made safe for human bodies.\n\n'
        'The alien life is the undercurrent. Even on terraformed Alcyone, the alien '
        'biology is present -- integrated into Orvanne\'s ecosystem, floating in '
        'Belvara\'s atmosphere, catalogued in the Conservatory\'s habitats. The '
        'Conservatory is the largest collection of non-terrestrial life in the '
        'galaxy, and the animal testing facilities attached to it are where the '
        'gene-splicing is validated before human application. The testing wings are '
        'not open to visitors. The failures in the testing wings are alive. Some of '
        'them should not be.\n\n'
        'The fleet guards the gateway with ships that are cold, dark, and nearly '
        'invisible -- crewed by personnel spliced for vacuum tolerance, carrying '
        'minimal life support because the crews do not need it. The Pleiadian '
        'military advantage is not firepower but the difficulty of finding ships '
        'that register on sensors as debris rather than vessels. Eleven billion '
        'people behind the most presentable face the cluster can manage, and the '
        'face is a lie of omission -- everything here is true, and nothing here is '
        'representative of what lies beyond.'
    ),
    cluster=StarClusters.PLEIADES,
)

ATLAS = System(
    name='Atlas',
    star='Blue-white giant (B8III), approximately 950 times Sol luminosity -- a hot, bright star whose light falls on a system engineered to be nobody\'s home and everybody\'s meeting place',
    population=8_000_000_000,
    distance_to_sol=380.0,
    stellar_objects=[
        StellarObject(
            name='Convaren',
            short_description='The capital of the Pleiades cluster -- four billion people on a world whose atmosphere has been engineered so that the widest possible range of strains can survive there, though none comfortably.',
            long_description=(
                'Convaren is the capital of the Pleiades -- not because it is the best '
                'world in the cluster but because it is the most neutral. The planet\'s '
                'atmosphere has been engineered over centuries to a compromise composition '
                'that the largest number of Pleiadian strains can tolerate. The air is not '
                'ideal for any strain. The pressure is slightly wrong for everyone. The '
                'temperature regulation is a negotiated midpoint that leaves the cold-'
                'adapted strains too warm and the heat-adapted strains too cold. Convaren '
                'is a planet designed to be equally uncomfortable for the greatest number '
                'of people, which is the only form of equality the strain confederation '
                'has managed to achieve.\n\n'
                'The confederation meets on Convaren because nobody else can host. A '
                'council session on Taygeta would kill the delegates from the low-gravity '
                'strains. A session on Asterope would irradiate the delegates who lack the '
                'radiation-splicing. A session on any world adapted for a specific strain '
                'is a session that excludes every other strain. Convaren\'s engineered '
                'neutrality is the only option -- a world where everyone suffers a little '
                'so that everyone can attend.\n\n'
                'The strain delegates arrive with entourages that include medical staff, '
                'atmospheric supplements, and the biological support systems that let them '
                'function outside their native environment for the duration of the session. '
                'A delegate from Taygeta wears an exoskeletal frame that compensates for '
                'the lower gravity. A delegate from Asterope carries radiation supplements '
                'that replace the cellular repair processes their body expects from the '
                'ambient radiation it is not receiving. The delegates from the deeply '
                'adapted outer worlds arrive in sealed environments and participate through '
                'remote interfaces because Convaren\'s atmosphere would kill them despite '
                'the engineering.\n\n'
                'The governance is slow, difficult, and shaped entirely by the biological '
                'reality that the people in the room are not the same species in any '
                'functional sense. The debates concern the issues that matter to a '
                'civilisation fragmenting along genetic lines: trade standards between '
                'strains whose food is mutually toxic, transit rights through systems whose '
                'atmospheres are mutually lethal, the allocation of gene-splicing resources '
                'between populations that are diverging faster than the confederation can '
                'bridge, and the question that underlies every session -- how long can a '
                'government of a single species persist when the species is becoming many.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='The Atrium',
            short_description='The confederation\'s orbital council station -- modular, compartmentalised, with each section maintaining the specific atmosphere its delegates require to survive.',
            long_description=(
                'The Atrium is the orbital station where the strain confederation conducts '
                'its business when the planetary sessions are impractical -- which is '
                'increasingly often, as the strains diverge further and the number of '
                'delegates who can tolerate Convaren\'s atmosphere shrinks. The station is '
                'the engineering solution to biological politics: a modular facility where '
                'each section can be configured to a different atmospheric composition, '
                'pressure, temperature, and radiation level.\n\n'
                'The council chamber in the Atrium is the most unusual meeting space in '
                'the galaxy. The delegates sit in sealed pods -- individual environments '
                'calibrated to their home world\'s conditions -- arranged around a central '
                'floor where the proceedings are projected in formats that each pod can '
                'perceive. Some delegates see in the visual spectrum that baseline humans '
                'use. Some have shifted into ultraviolet or infrared ranges that their '
                'home world\'s light conditions favoured. The projection system accommodates '
                'them all, displaying the same information in wavelengths that the '
                'delegates\' modified eyes can process.\n\n'
                'The corridors between sections are airlocks. A delegate moving from the '
                'high-pressure section to the low-pressure section passes through '
                'equalisation chambers. A delegate from a methane-atmosphere world cannot '
                'enter the oxygen-atmosphere section without a sealed suit. The station is '
                'a civilisation\'s government conducted through bulkheads and pressure '
                'seals, and the architecture is the most honest expression of the '
                'confederation\'s central problem: these are people who can no longer '
                'share a room.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Deverne',
            short_description='A world where alien life has been cultivated rather than contained -- the cluster\'s primary research site for alien ecosystem dynamics.',
            long_description=(
                'Deverne is Atlas\'s second habitable world -- partially terraformed, with '
                'a managed alien biosphere that the cluster\'s researchers use to study '
                'how non-terrestrial ecosystems function at planetary scale. The alien life '
                'on Deverne was not eliminated during terraforming but cultivated -- the '
                'researchers wanted a world where the alien organisms could interact with '
                'introduced terrestrial species under observation, and Deverne provides '
                'that laboratory.\n\n'
                'The results have been scientifically invaluable and occasionally '
                'alarming. The alien organisms on Deverne have adapted to the terrestrial '
                'species faster than the models predicted -- the alien predators learned '
                'to hunt terrestrial prey, the alien plants began competing with '
                'terrestrial crops, and the microbial ecosystems merged in ways that '
                'produced new organisms that were neither terrestrial nor alien but '
                'something the researchers had not anticipated. The merged organisms are '
                'being studied for potential gene-splicing applications. Some of them '
                'represent adaptation pathways that neither the terrestrial nor the alien '
                'biology could have produced alone.\n\n'
                'The population on Deverne is mostly research staff -- biologists, '
                'geneticists, and the field workers who monitor the ecosystem interactions '
                'across the planet\'s managed zones. The staff carry moderate splicing for '
                'the local conditions and a deeper understanding of alien biology than '
                'most Pleiadians, because they live inside an experiment that is producing '
                'results nobody fully controls.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Strathven',
            short_description='A world housing the populations that cannot live on Convaren -- communities of the deeply adapted who have relocated to the capital system but require sealed habitats.',
            long_description=(
                'Strathven is a colder, harsher world in the outer habitable zone that has '
                'become home to the deeply adapted Pleiadian populations who need to be '
                'near the capital but cannot survive on Convaren. The planet hosts sealed '
                'habitat communities -- enclosed environments where the atmosphere, '
                'pressure, and radiation levels are maintained to match the home conditions '
                'of the various deep-adapted strains that have established permanent '
                'delegations.\n\n'
                'The habitats are the confederation\'s concession to the reality that '
                'political participation requires physical presence, and physical presence '
                'requires the right atmosphere. A Taygetan trade delegation lives in a '
                'high-gravity habitat. An Asteropan mining delegation lives in a radiation-'
                'saturated habitat. The habitats are separated by kilometres of surface '
                'that none of the inhabitants can cross without sealed transit vehicles. '
                'The communities are permanent, established, and completely isolated from '
                'each other -- neighbours who have never breathed the same air and never '
                'will.\n\n'
                'The children born in Strathven\'s habitats grow up in their parents\' '
                'home atmosphere but on a world that is not their home, surrounded by '
                'habitats they cannot enter containing people they can see through the '
                'windows but cannot touch. The children of the confederation learn early '
                'that humanity is a word that covers an increasing number of things that '
                'cannot share a room.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Korvedan',
            short_description='A gas giant with fuel processing and alien atmospheric life -- larger organisms than Belvara\'s, including colonial species that form structures visible from orbit.',
            long_description=(
                'Korvedan is the system\'s gas giant -- fuel processing on its moons '
                'supporting the capital\'s traffic. The alien life in Korvedan\'s atmosphere '
                'is more developed than Belvara\'s -- the organisms are larger, more '
                'diverse, and include colonial species that aggregate into structures '
                'visible from orbit. The colonial organisms form floating rafts of '
                'biological material in the upper atmosphere, kilometres across, that the '
                'researchers on Deverne have been studying for decades without fully '
                'understanding the colonial communication that coordinates them.\n\n'
                'The fuel processors work around the organisms with the practiced caution '
                'of people who have learned which atmospheric layers are safe to skim and '
                'which are occupied. The colonial organisms are not aggressive but they '
                'are large enough that a fuel skimmer that enters a colonial raft risks '
                'being entangled in biological material that fouls the intake systems. The '
                'entanglement is not predatory. The organisms do not know the skimmer is '
                'there. They are simply big, and the skimmer is not.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Hennavik',
            short_description='An agricultural world that grows food for multiple strains -- different fields producing different crops for populations with incompatible dietary requirements.',
            long_description=(
                'Hennavik is the system\'s agricultural world and the cluster\'s most '
                'unusual farming operation. The planet produces food for multiple strains '
                '-- fields of baseline terrestrial crops alongside fields of alien-hybrid '
                'crops alongside fields of heavily modified organisms that only specific '
                'strains can metabolise. The farming is segregated by dietary compatibility: '
                'the food from one field would nourish one strain and poison another, and '
                'the agricultural management is as much about preventing cross-'
                'contamination as it is about maximising yield.\n\n'
                'The farmers on Hennavik are among the cluster\'s most broadly modified -- '
                'not deeply adapted for a single extreme environment but broadly spliced '
                'for compatibility with the range of organisms they cultivate. A Hennavik '
                'farmer handles alien crops that would cause contact dermatitis in a '
                'baseline human, feeds livestock whose biology is partly terrestrial and '
                'partly alien, and manages soil chemistry that varies field by field '
                'depending on which strain\'s food supply that field supports. The '
                'expertise is unique and the training is long.'
            ),
            population=900_000_000,
        ),
    ],
    short_description='The capital -- eight billion people on a world engineered to be equally uncomfortable for everyone, governing a civilisation whose populations can no longer share a room.',
    long_description=(
        'Atlas is the capital of the Pleiades cluster -- not because it is the best '
        'system but because it is the most neutral. Convaren\'s atmosphere has been '
        'engineered to a compromise that the largest number of strains can tolerate, '
        'though none comfortably. The pressure is slightly wrong for everyone. The '
        'temperature is a negotiated midpoint. Convaren is equally uncomfortable for '
        'the greatest number of people, which is the only equality the strain '
        'confederation has achieved.\n\n'
        'The confederation meets here because nobody else can host. A session on '
        'Taygeta would kill the low-gravity delegates. A session on Asterope would '
        'irradiate the unshielded. The Atrium -- the orbital council station -- is '
        'the engineering solution: modular sections with different atmospheres, the '
        'council chamber a ring of sealed pods where delegates sit in their home '
        'conditions and view the proceedings in whatever wavelength their modified '
        'eyes can process. The corridors between sections are airlocks. A '
        'civilisation\'s government conducted through bulkheads and pressure seals.\n\n'
        'Strathven houses the deeply adapted populations who need to be near the '
        'capital but cannot survive on Convaren -- sealed habitats separated by '
        'kilometres of surface none of the inhabitants can cross. Neighbours who '
        'have never breathed the same air and never will. The children grow up in '
        'their parents\' atmosphere surrounded by habitats they cannot enter, learning '
        'early that humanity is a word that covers an increasing number of things '
        'that cannot share a room.\n\n'
        'Deverne is the alien biology research world -- cultivated ecosystems where '
        'alien and terrestrial species merge in ways the models did not predict. '
        'Hennavik grows food for multiple strains in segregated fields -- one '
        'strain\'s nourishment is another\'s poison, and the farming is as much about '
        'preventing cross-contamination as maximising yield. Eight billion people in '
        'a system that exists to hold together a civilisation that is pulling apart '
        'at the genetic level, governed by delegates in sealed pods who represent '
        'populations that are becoming different species and who negotiate the terms '
        'of a unity that biology is slowly making impossible.'
    ),
    cluster=StarClusters.PLEIADES,
)

MAIA = System(
    name='Maia',
    star='Blue-white giant (B8III), approximately 850 times Sol luminosity -- a hot, luminous star at the junction of the cluster\'s most important routes, where the traffic never stops because the supply must not stop',
    population=9_000_000_000,
    distance_to_sol=380.0,
    stellar_objects=[
        StellarObject(
            name='Sondrak',
            short_description='The junction world -- five billion people at the start of the Electra route, where the gene-splicing economy is visible for the first time and the strategic importance is felt in the garrison\'s size.',
            long_description=(
                'Sondrak is where the Pleiades stops pretending to be normal. The planet '
                'is partially terraformed -- breathable but harsh, with an atmosphere that '
                'requires minor splicing to tolerate comfortably and an alien biosphere '
                'that has been managed rather than eliminated. The alien organisms are '
                'visible on Sondrak in ways they are not on Alcyone\'s controlled worlds: '
                'alien vegetation covering the hillsides in colours that no terrestrial '
                'plant produces, alien insects filling ecological niches with anatomies '
                'that visitors find unsettling, and the larger alien fauna in the '
                'wilderness zones that the terraforming did not reach.\n\n'
                'The gene-splicing economy is open here. On Alcyone, the modification '
                'industry is discreet -- the Conservatory and its testing wings kept '
                'separate from the diplomatic face. On Sondrak, the clinics are '
                'commercial and prominent. The modification houses advertise openly: '
                'radiation resistance from Asterope\'s deep-bore organisms, cold tolerance '
                'from the alpine fauna on PLX-8801, immune packages derived from the '
                'microbial ecosystems on a dozen different worlds. The wealthy browse the '
                'catalogues for precise, targeted splicing. The poor take what they can '
                'afford -- crude packages that solve the survival problem and lock them '
                'to their destination world permanently.\n\n'
                'The strategic importance is the Electra route. All shipments of '
                'stabilisation compounds from Electra pass through Maia. The route runs '
                'Electra to PLX-9902 to PLX-9901 to Maia, and from Maia the compounds are '
                'distributed across the cluster. A disruption at Maia would not cut the '
                'supply immediately -- other systems produce synthetic alternatives and '
                'Pleione\'s labs supplement the supply -- but it would degrade the '
                'cluster\'s capacity to stabilise new modifications over years. The '
                'garrison at Maia reflects this: the military presence is the heaviest in '
                'the cluster after Alcyone, and the fleet patrols the route approaches '
                'with the focus of people guarding something that cannot be lost.'
            ),
            population=5_000_000_000,
        ),
        StellarObject(
            name='The Grafthouse',
            short_description='The cluster\'s largest commercial gene-splicing complex -- where the modifications are sold, installed, and tested on a scale that makes Alcyone\'s Conservatory look like a research library.',
            long_description=(
                'The Grafthouse is an orbital complex above Sondrak that houses the '
                'cluster\'s largest commercial gene-splicing operation. Where Alcyone\'s '
                'Conservatory is research and the Pleione labs are development, the '
                'Grafthouse is production -- the place where the modification packages '
                'that the cluster\'s population actually uses are assembled, quality-'
                'tested, and installed.\n\n'
                'The testing is the horror. The Grafthouse maintains extensive animal '
                'testing facilities -- floors of laboratories where baseline organisms '
                'are modified with alien gene sequences and monitored for compatibility. '
                'The testing subjects include standard laboratory animals and, for the '
                'modifications that require closer biological analogues, primates and '
                'cloned human tissue cultures that the ethical oversight committees on '
                'Alcyone have approved with the careful language that approval of '
                'uncomfortable necessities requires. The tissue cultures are not people. '
                'The tissue cultures grow, respond, and sometimes develop in ways that '
                'blur the line between culture and organism. The researchers do not '
                'discuss this in the published literature.\n\n'
                'The failures in the testing floors are the Grafthouse\'s open secret. A '
                'modification package that works on the tissue culture may fail on the '
                'animal subject in ways that produce organisms that are functional but '
                'wrong -- animals with alien sensory organs they cannot process, with '
                'metabolisms that sustain them but that produce byproducts the body cannot '
                'clear, with structural changes that let them survive the target '
                'environment but that cause pain the researchers can measure and the '
                'animals cannot articulate. The failures are studied, documented, and '
                'euthanised when the research value is exhausted. The word euthanised '
                'appears in the records. The word mercy does not.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Bresken',
            short_description='A world where the alien biosphere is dominant -- the first system on the route toward Electra where humans are the invasive species rather than the other way around.',
            long_description=(
                'Bresken is Maia\'s outer habitable world -- colder, less terraformed, and '
                'the first place in the cluster where the balance between human and alien '
                'biology tips toward the alien. The terraforming on Bresken was partial -- '
                'the atmosphere was adjusted enough to breathe with splicing, but the '
                'biosphere was left largely intact because the cost of eliminating it '
                'exceeded the budget and the alien organisms were more useful alive than '
                'dead.\n\n'
                'The population on Bresken is more heavily modified than Sondrak\'s -- '
                'deeper immune splicing for the denser alien pathogen load, digestive '
                'modifications for the alien-origin food that the local agriculture '
                'produces, and the respiratory adjustments for an atmosphere that the '
                'partial terraforming left richer in compounds that baseline lungs cannot '
                'process. The modifications are still reversible in theory -- a Bresken '
                'resident could be genetically restored to baseline with extensive '
                'treatment -- but in practice nobody does, because the treatment is '
                'expensive and the baseline body cannot survive on Bresken.\n\n'
                'The alien fauna on Bresken includes species that have become central to '
                'the local economy. The livestock are alien -- large, slow herbivores '
                'whose meat is nutritious for the spliced population and whose hides '
                'produce a material the textile industry values. The crop plants are '
                'alien-terrestrial hybrids that the agricultural researchers developed '
                'over decades of cross-breeding that would horrify a MERIT botanist. The '
                'food chain on Bresken is a tangle of alien and terrestrial biology that '
                'nobody fully maps and everybody depends on.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Dispatch Station',
            short_description='The orbital logistics hub for the Electra route -- where the stabilisation compound shipments are received, processed, and distributed across the cluster.',
            long_description=(
                'Dispatch Station is the logistics hub for the Electra supply chain -- '
                'the facility where the stabilisation compound shipments from Electra '
                'arrive via the PLX-9901/PLX-9902 route and are processed for distribution '
                'across the cluster. The compounds arrive in climate-controlled containers '
                'that the station\'s staff transfer to distribution freighters bound for '
                'every inhabited system.\n\n'
                'The logistics are the Pleiades\' most critical supply chain. The '
                'stabilisation compounds prevent cumulative gene-splicing from cascading '
                'into genetic instability -- without regular doses, the alien gene '
                'sequences integrated into a modified person\'s genome begin to express '
                'unpredictably, producing changes that the original splicing did not '
                'intend. The deeper the modification, the more dependent the person is '
                'on the compounds, and the deeply adapted populations on the outer worlds '
                'require the highest doses. Dispatch Station is the bottleneck through '
                'which this supply flows, and the station\'s staff understand that a '
                'failure in their logistics means people on dozens of worlds begin to '
                'change in ways nobody can predict or control.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Heskane',
            short_description='A gas giant with fuel processing and alien atmospheric ecology -- the organisms here produce compounds the Grafthouse has identified as potential splicing substrates.',
            long_description=(
                'Heskane is the system\'s gas giant -- fuel processing on its moons '
                'supporting the heavy traffic that Maia\'s junction status generates. The '
                'alien life in Heskane\'s atmosphere is more complex than the gas-dwellers '
                'in Alcyone\'s Belvara -- the organisms here form symbiotic chains, each '
                'species dependent on the metabolic outputs of the others, producing an '
                'aerial ecosystem of interlocking dependencies that the biologists on '
                'Deverne consider one of the most elegant biological systems in the '
                'cluster.\n\n'
                'The symbiotic chains produce compounds that the Grafthouse has identified '
                'as potential gene-splicing substrates -- organic molecules with properties '
                'that could improve the stability of certain modification packages. The '
                'harvesting is experimental and cautious. The symbiotic chains are fragile '
                '-- removing one species from the chain can collapse the entire system, '
                'and the researchers are working to understand the dependencies before '
                'attempting extraction at commercial scale.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Valstow',
            short_description='An agricultural world producing food for two populations -- baseline-compatible for the gateway traffic and alien-hybrid for the local spliced population.',
            long_description=(
                'Valstow is the system\'s agricultural world -- partially terraformed, with '
                'a dual farming operation that produces food for two different populations. '
                'The baseline-compatible fields grow terrestrial crops for the gateway '
                'traffic and the moderately modified population that can still eat standard '
                'food. The alien-hybrid fields grow the modified crops that the more deeply '
                'spliced local population requires -- food engineered to match the '
                'digestive modifications that life on Bresken and the outer worlds demands.\n\n'
                'The dual operation is Maia\'s agricultural compromise -- a farming world '
                'that feeds both the people who are still mostly human and the people who '
                'are becoming something else. The fields are segregated because cross-'
                'contamination would render the baseline food inedible and the alien-hybrid '
                'food unstable. The farmers manage the boundary between the two operations '
                'with the care of people who understand that the wrong pollen in the wrong '
                'field could poison a population.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Ardenne',
            short_description='A rocky outer world housing the garrison that protects the Electra route -- the most important military posting in the cluster after the gateway.',
            long_description=(
                'Ardenne is a cold, rocky world in the outer system that houses the '
                'garrison protecting the Electra route approaches. The military presence '
                'is focused on the jump points that connect Maia to PLX-9901 -- the first '
                'link in the four-jump chain to Electra. The garrison crews are spliced for '
                'the standard Pleiadian military package: vacuum tolerance, radiation '
                'resistance, reduced atmospheric requirements that let the ships run cold '
                'and dark.\n\n'
                'The posting is the most important in the cluster after the gateway. The '
                'garrison commanders understand that they are guarding the supply chain '
                'that prevents the cluster\'s modified populations from destabilising. A '
                'successful attack on the Electra route would not kill anyone immediately '
                '-- the stabilisation compounds in storage would last months. But the '
                'knowledge that the supply had been cut would change the political '
                'calculations across the cluster instantly, and the deeply adapted '
                'populations who depend on the compounds most heavily would begin planning '
                'for a future that the garrison exists to prevent.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The junction -- nine billion people at the start of the Electra route, where the gene-splicing economy is open and the supply chain that keeps the cluster stable passes through.',
    long_description=(
        'Maia is the junction where the Pleiades\' most important routes converge. '
        'The system sits at the start of the four-jump chain to Electra -- the '
        'remote system that produces the largest share of the stabilisation compounds '
        'that prevent cumulative gene-splicing from cascading into genetic '
        'instability. Every shipment from Electra passes through Maia. A disruption '
        'here would not cut the supply immediately -- Pleione\'s labs and other '
        'sources provide alternatives -- but it would degrade the cluster\'s '
        'stabilisation capacity over years.\n\n'
        'Maia is where the Pleiades stops pretending to be normal. The gene-splicing '
        'economy is open and commercial -- modification houses advertising openly on '
        'Sondrak, the Grafthouse operating the cluster\'s largest commercial '
        'splicing complex with testing facilities whose animal subjects include '
        'failures that are functional but wrong. The horror of the testing floors is '
        'the Grafthouse\'s open secret: organisms with alien sensory organs they '
        'cannot process, metabolisms that sustain but produce byproducts the body '
        'cannot clear, structural changes that cause pain the researchers can '
        'measure and the animals cannot articulate.\n\n'
        'Bresken is the first world where alien biology is dominant -- humans as the '
        'invasive species, livestock that is alien, crops that are alien-terrestrial '
        'hybrids, a food chain that is a tangle nobody fully maps and everybody '
        'depends on. The population is more heavily modified, the modifications are '
        'still theoretically reversible, and nobody reverses them because the '
        'baseline body cannot survive on Bresken.\n\n'
        'Nine billion people at a junction that the cluster cannot afford to lose, '
        'guarded by a garrison that understands what it is protecting: not a system '
        'but the supply chain that prevents a civilisation of genetically modified '
        'humans from destabilising into something the modifications were never '
        'designed to produce.'
    ),
    cluster=StarClusters.PLEIADES,
)

MEROPE = System(
    name='Merope',
    star='Blue-white subgiant (B6IVe), approximately 630 times Sol luminosity -- a hot, bright star whose light falls on the cluster\'s most comfortable system, where the gene-splicing is art and the alien biology is curated',
    population=16_000_000_000,
    distance_to_sol=360.0,
    stellar_objects=[
        StellarObject(
            name='Lassiter',
            short_description='The showcase -- eight billion people living proof that gene-splicing can be beautiful, precise, and liberating, if you can afford the version that does not trap you.',
            long_description=(
                'Lassiter is what the Pleiades looks like when money is not a constraint. '
                'The planet is the cluster\'s most populous, most prosperous, and most '
                'thoroughly terraformed world after Alcyone -- breathable atmosphere, '
                'stable climate, managed alien biosphere integrated into an ecosystem that '
                'has been engineered for beauty as much as function. The alien trees in '
                'Lassiter\'s parks produce bioluminescent flowers. The alien fauna in the '
                'managed preserves includes species selected for visual spectacle as much '
                'as ecological function. The world looks designed, because it is.\n\n'
                'The gene-splicing on Lassiter is the premium product. The wealthy '
                'population carries modifications that are precise, targeted, and '
                'reversible -- the work of the cluster\'s best bioengineers, who splice '
                'alien genes with a delicacy that preserves baseline compatibility while '
                'adding the desired traits. A Lassiter citizen might carry radiation '
                'resistance from Asterope\'s organisms, cold tolerance from the alpine '
                'fauna, enhanced visual range from a deep-ocean species -- and still pass '
                'a baseline medical scan on a MERIT station, because the modifications '
                'are integrated so precisely that the body reads as human with minor '
                'variations rather than as something else.\n\n'
                'The aesthetic splicing is Lassiter\'s cultural signature. The wealthy do '
                'not just splice for survival or capability -- they splice for beauty. '
                'Alien pigmentation patterns across the skin in geometric designs that '
                'follow the individual\'s chosen aesthetic. Bioluminescent accents in the '
                'fingertips, the collarbones, the temples -- subtle glows that activate '
                'under certain light conditions. Eyes modified with alien visual genes '
                'that produce colours no baseline human eye displays. The modifications '
                'are fashion, identity, and status marker simultaneously. On Lassiter, '
                'what your body looks like is a statement of taste, wealth, and the '
                'quality of bioengineering you can command.\n\n'
                'The contrast with the outer worlds is the point MERIT makes and Lassiter '
                'does not like hearing. On Lassiter, the splicing is art -- chosen, '
                'beautiful, reversible. On Taygeta or Asterope, the splicing is survival '
                '-- forced, crude, permanent. The same technology produces elegance for '
                'the wealthy and imprisonment for the poor. Lassiter\'s citizens consider '
                'themselves proof that gene-splicing enhances humanity. MERIT considers '
                'them proof that it only enhances the humans who can pay.'
            ),
            population=8_000_000_000,
        ),
        StellarObject(
            name='Isendri',
            short_description='A second world of carefully managed beauty -- where the alien biosphere has been curated into the most spectacular natural environment in the cluster.',
            long_description=(
                'Isendri is Merope\'s second inhabited world -- warmer, lusher, and the '
                'planet where the alien biosphere has been cultivated into something that '
                'visitors describe as the most beautiful natural environment in the outer '
                'systems. The curation is deliberate: the alien species on Isendri have '
                'been selected for visual impact, ecological stability, and the capacity '
                'to coexist with the human population without the hazards that alien life '
                'presents on the less managed worlds.\n\n'
                'The forests on Isendri glow at night. The bioluminescent organisms that '
                'colonise the alien trees produce a soft light that shifts colour through '
                'the evening hours, following a biochemical cycle that the researchers have '
                'mapped but that the residents simply call the evening colours. The coastal '
                'waters contain alien marine life -- transparent organisms with internal '
                'bioluminescence that light the shallows in patterns that respond to water '
                'temperature and current, producing a display that the tourism industry '
                'has marketed successfully and that the biologists insist is a '
                'thermoregulation mechanism rather than a performance.\n\n'
                'The population carries aesthetic splicing that complements the '
                'environment -- the same bioluminescent accents that Lassiter\'s fashion '
                'culture produces, but calibrated to resonate with Isendri\'s organisms. '
                'A resident\'s skin accents glow in the same frequencies as the forest '
                'organisms, producing the impression that the human and the alien are part '
                'of the same display. The effect is beautiful, intentional, and deeply '
                'uncomfortable for baseline visitors who find that the people look like '
                'the trees.'
            ),
            population=3_500_000_000,
        ),
        StellarObject(
            name='The Promenade',
            short_description='An orbital station that is part luxury port, part gallery of aesthetic splicing -- where the cluster\'s wealthiest display their modifications and the bioengineers compete for prestige.',
            long_description=(
                'The Promenade is Merope\'s primary orbital station and the cluster\'s '
                'premier destination for the wealthy. The station is designed to display '
                '-- the public spaces are lit to show aesthetic splicing at its best, the '
                'architecture incorporates alien biological elements that complement the '
                'modified bodies of the residents, and the social spaces are stages where '
                'the cluster\'s wealthiest citizens display their modifications as art.\n\n'
                'The Promenade hosts the annual Bioengineering Exhibition -- the cluster\'s '
                'most prestigious event, where the leading bioengineers display their '
                'latest aesthetic work on volunteer subjects who walk the exhibition space '
                'as living demonstrations. The competition is fierce. A bioengineer whose '
                'work is featured at the Exhibition gains commissions that can sustain a '
                'practice for years. The aesthetic standards evolve annually -- what is '
                'considered beautiful shifts as the bioengineers push the boundaries of '
                'what alien genes can produce in a human body.\n\n'
                'The Promenade is also where the outer-system populations encounter what '
                'their modifications could have been. A worker from Taygeta who has been '
                'crudely spliced for high-gravity survival -- the dense musculature, the '
                'thickened skin, the compressed frame -- can walk the Promenade and see '
                'citizens whose bodies carry the same alien genes expressed with precision '
                'and artistry. The same genes. Different money. The worker returns to '
                'Taygeta carrying an understanding of the wealth divide that no '
                'propaganda could produce as effectively.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Delvraine',
            short_description='The premium bioengineering world -- where the cluster\'s best practitioners maintain their clinics and the aesthetic splicing that defines Lassiter\'s culture is designed.',
            long_description=(
                'Delvraine is the system\'s bioengineering centre -- a temperate world '
                'where the cluster\'s most prestigious gene-splicing practitioners '
                'maintain clinics that serve the wealthy clientele from Lassiter, Isendri, '
                'and the other prosperous systems. The clinics on Delvraine are not the '
                'commercial modification houses of Maia\'s Grafthouse. They are ateliers '
                '-- small, exclusive practices where the bioengineers design bespoke '
                'modifications for individual clients with the attention to detail that '
                'justifies the premium pricing.\n\n'
                'The bioengineers on Delvraine are artists who work in living tissue. The '
                'best of them are known across the cluster by name -- their aesthetic '
                'signatures recognisable in the modifications of their clients the way a '
                'painter\'s style is recognisable in their canvases. A client wearing a '
                'modification by one of Delvraine\'s premier practitioners is wearing a '
                'status symbol that other wealthy Pleiadians can identify on sight.\n\n'
                'The testing on Delvraine is more discreet than the Grafthouse\'s but no '
                'less extensive. The bespoke modifications require testing -- each one is '
                'unique, and the gene sequences must be validated before installation. The '
                'testing subjects are maintained in private facilities attached to the '
                'clinics. The failures are handled quietly. The clients do not ask about '
                'the testing process the same way they do not ask about the sourcing of '
                'the alien gene material. The result is what matters. The cost is someone '
                'else\'s problem.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Vintara',
            short_description='A gas giant with a spectacular ring system colonised by alien organisms -- the most photographed object in the cluster, and the source of the ring-organisms\' bioluminescent compounds.',
            long_description=(
                'Vintara is the system\'s gas giant -- notable for a spectacular ring '
                'system that alien organisms have colonised. The ring-dwellers are small, '
                'photosynthetic organisms that feed on the starlight filtering through the '
                'ring particles, and their bioluminescent metabolic byproducts cause the '
                'rings to glow in shifting patterns that are visible from the inhabited '
                'worlds. The rings of Vintara are the most photographed natural feature in '
                'the cluster, and the bioluminescent compounds the ring-organisms produce '
                'are harvested for the aesthetic splicing industry -- the same compounds '
                'that produce the glowing accents in the skin of Lassiter\'s wealthy.\n\n'
                'The fuel processing on Vintara\'s moons is standard. The ring-organism '
                'harvesting is not -- the collection is delicate, conducted by specialised '
                'crews who work in the ring environment with the care required by organisms '
                'that are fragile, valuable, and the source of the compounds that the '
                'entire aesthetic economy depends on.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Berenstal',
            short_description='An agricultural world producing the premium food that the wealthy population demands -- alien-terrestrial cuisine elevated to an art form.',
            long_description=(
                'Berenstal is the system\'s agricultural world -- and unlike the '
                'functional farming operations on the other systems, the agriculture on '
                'Berenstal is oriented toward quality rather than volume. The farms produce '
                'the alien-terrestrial hybrid cuisine that Merope\'s wealthy population '
                'demands -- food that is part terrestrial, part alien, and engineered for '
                'flavour profiles that baseline human palates cannot detect and that the '
                'spliced palates of Lassiter\'s residents experience as extraordinary.\n\n'
                'The cuisine is an art form. The chefs on Lassiter who work with '
                'Berenstal\'s produce are among the cluster\'s most celebrated artists -- '
                'people who design dishes for mouths that can taste compounds that '
                'baseline tongues cannot perceive, using ingredients that would be toxic '
                'to anyone without the appropriate digestive splicing. Eating on Merope '
                'is a modified experience for modified people, and the food is the most '
                'visceral demonstration of how far the wealthy have diverged from baseline '
                'while insisting they are still the same species.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The showcase -- sixteen billion people in the system where gene-splicing is art, the alien biology is beautiful, and the wealth divide between elegant modification and crude survival has never been more visible.',
    long_description=(
        'Merope is what the Pleiades looks like when money is not a constraint. '
        'Sixteen billion people in the cluster\'s most prosperous system, where the '
        'gene-splicing is precise, targeted, and reversible -- the work of the '
        'cluster\'s best bioengineers, producing modifications that enhance without '
        'trapping. A Lassiter citizen can carry radiation resistance, cold tolerance, '
        'and enhanced visual range while still passing a baseline medical scan, '
        'because the modifications are integrated so precisely that the body reads '
        'as human with minor variations rather than as something else.\n\n'
        'The aesthetic splicing is the cultural signature. The wealthy splice for '
        'beauty -- alien pigmentation patterns, bioluminescent accents, eyes in '
        'colours no baseline human displays. The modifications are fashion, identity, '
        'and status marker simultaneously. Isendri\'s curated alien biosphere glows '
        'at night, and the residents\' skin accents glow in the same frequencies, '
        'producing the impression that the human and the alien are part of the same '
        'display. The Promenade hosts the annual Bioengineering Exhibition where the '
        'leading practitioners display their latest work on living subjects.\n\n'
        'The contrast with the outer worlds is the point MERIT makes and Merope '
        'does not want to hear. On Lassiter, the splicing is art -- chosen, '
        'beautiful, reversible. On Taygeta, the splicing is survival -- forced, '
        'crude, permanent. The same technology, the same alien genes, different '
        'money. A worker from Taygeta who visits the Promenade can see citizens '
        'whose bodies carry the same genes expressed with precision and artistry. '
        'The worker returns carrying an understanding of the wealth divide that no '
        'propaganda could produce as effectively.\n\n'
        'Vintara\'s rings glow with alien organisms whose bioluminescent compounds '
        'are harvested for the aesthetic industry. Delvraine\'s ateliers design '
        'bespoke modifications for individual clients. Berenstal\'s farms produce '
        'cuisine for mouths that taste compounds baseline tongues cannot perceive. '
        'Everything in Merope is beautiful, curated, and available to those who can '
        'pay. The system is proof that gene-splicing enhances humanity. MERIT '
        'considers it proof that enhancement is a luxury, and the workers on the '
        'outer worlds who carry the same genes expressed as survival rather than '
        'art would agree, if anyone on Merope asked them.'
    ),
    cluster=StarClusters.PLEIADES,
)

MIRACH = System(
    name='Mirach',
    star='Red giant (M0III), approximately 1,900 times Sol luminosity -- a large, cool star casting deep red light over the system where the Pleiades sells its biology to the rest of the galaxy',
    population=7_000_000_000,
    distance_to_sol=200.0,
    stellar_objects=[
        StellarObject(
            name='Renthane',
            short_description='The cluster\'s shopfront -- four billion people adapting Pleiadian gene-splicing technology for buyers who want alien biology without the commitment of becoming something else.',
            long_description=(
                'Renthane is where the Pleiades sells itself. The planet is the cluster\'s '
                'primary trade hub -- the system where Pleiadian gene-splicing technology '
                'is adapted, packaged, and sold to every faction willing to buy. The '
                'buyers are varied and their needs are specific: the Antares cluster buys '
                'biological compounds that enhance the efficacy of its performance drugs. '
                'The Canopus cluster buys tissue-preservation techniques that improve the '
                'quality of reanimation. The Hyades buys biological interface substrates '
                'that improve prosthetic-tissue compatibility. MERIT\'s black market absorbs '
                'Pleiadian gene therapies through channels that the confederation officially '
                'does not acknowledge.\n\n'
                'The export trade is adaptation. The gene-splicing technology that works in '
                'the Pleiades -- where the population has been progressively modified over '
                'generations and the bodies are prepared for alien gene integration -- does '
                'not work directly in baseline humans. The bioengineers on Renthane '
                'specialise in the translation: taking the alien-derived compounds, gene '
                'therapies, and biological technologies that the Pleiades has developed '
                'and reformulating them for bodies that have not been spliced. The work '
                'is technically demanding and commercially lucrative. The Pleiades\' alien '
                'biology is the most advanced biological technology in the galaxy, and '
                'every faction wants access to it on terms they can survive.\n\n'
                'The trading houses on Renthane are the biological equivalent of Genib\'s '
                'prosthetic trading houses in the Hyades -- commercial operations with '
                'relationships across every faction, expertise in the regulatory '
                'environments of each market, and the fluency in inter-faction commerce '
                'that centuries of trade produce. The negotiations are conducted in the '
                'deep red light of the system\'s red giant, which the traders consider '
                'atmospheric and the visitors from blue-white systems find oppressive.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Thenvale',
            short_description='The adaptation manufacturing world -- where Pleiadian biology is reformulated for non-Pleiadian bodies in laboratories that reverse-engineer alien genes for baseline compatibility.',
            long_description=(
                'Thenvale is the system\'s manufacturing world -- where the export-grade '
                'biological products are produced. The factories are not the industrial '
                'plants of the Hyades or the foundries of the Antares cluster. They are '
                'laboratories -- clean, climate-controlled facilities where the alien '
                'biological compounds are processed, the gene therapies are formulated, '
                'and the products are quality-tested for compatibility with bodies that '
                'have never been spliced.\n\n'
                'The testing on Thenvale is the export trade\'s necessary horror. The '
                'products must be validated on baseline organisms before sale -- the '
                'buyers insist, because the consequences of an incompatible gene therapy '
                'in a baseline body range from ineffective to lethal. The testing subjects '
                'are animals maintained in conditions that the labs describe as humane and '
                'that the animal welfare advocates from MERIT describe differently. The '
                'baseline testing animals are modified with the export-grade products and '
                'monitored for compatibility, rejection, and the cascading side effects '
                'that alien-derived gene therapies can produce in bodies that were not '
                'prepared for them. The success rate is high enough for commercial '
                'viability. The failure rate is low enough for the labs to publish. The '
                'gap between the two rates contains the animals that the reports '
                'categorise as inconclusive.'
            ),
            population=1_200_000_000,
        ),
        StellarObject(
            name='The Bourse',
            short_description='The system\'s orbital trading station -- where buyers from every faction negotiate for Pleiadian biology on a trading floor that smells different in every section.',
            long_description=(
                'The Bourse is Mirach\'s primary orbital station and the largest biological '
                'trading installation in the galaxy. The station is the Pleiades\' answer '
                'to the Hyades\' Emporium on Genib -- a neutral trading floor where buyers '
                'from every faction browse, negotiate, and purchase. The difference is the '
                'product. The Emporium trades in prosthetics -- inert hardware in crates. '
                'The Bourse trades in biology -- living compounds, active gene therapies, '
                'and preserved alien organisms in climate-controlled containers that the '
                'station\'s environmental systems struggle to accommodate.\n\n'
                'The trading floor on the Bourse smells different in every section. The '
                'Antarian buyers\' zone has the chemical tang of the compounds they are '
                'evaluating. The Canopan buyers\' zone has the preservative scent of the '
                'tissue-preservation products. The section where the raw alien organisms '
                'are displayed has the unmistakable smell of alien biology -- a scent that '
                'baseline visitors describe as wrong in a way they cannot specify and that '
                'the Pleiadian traders have long since stopped noticing. The environmental '
                'systems filter and separate the atmospheric zones, but the boundaries are '
                'imperfect and the smells leak across sections in combinations that the '
                'station\'s management has stopped trying to control.\n\n'
                'The security on the Bourse is biological rather than military. The '
                'products on the trading floor are more dangerous than weapons -- a gene '
                'therapy vial that breaks on the wrong surface could contaminate the '
                'station with alien compounds that the environmental systems cannot clear. '
                'The containment protocols are strict, the handling procedures are rigid, '
                'and the consequences of a containment failure are severe enough that the '
                'security staff are the most carefully trained personnel on any trading '
                'station in the galaxy.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Strannik',
            short_description='A world where the alien biosphere has been maintained as a living catalogue -- the trade hub\'s showcase of what Pleiadian biology can offer, displayed for the buyers.',
            long_description=(
                'Strannik is Mirach\'s showcase world -- a planet where the alien biosphere '
                'has been maintained and curated as a living demonstration of what Pleiadian '
                'biology can offer. The buyers who visit Mirach are brought to Strannik to '
                'see the organisms in their native or near-native conditions: the radiation-'
                'resistant species in contained high-radiation zones, the pressure-adapted '
                'organisms in deep-bore observation facilities, and the bioluminescent '
                'species in darkened habitats where the alien light displays are shown to '
                'maximum effect.\n\n'
                'The tours are sales pitches. The guides are bioengineers who explain how '
                'each organism\'s adaptive traits can be translated into gene therapies '
                'for the buyers\' populations. The radiation-resistant organism becomes a '
                'product for the Hyades\' mining workforce. The pressure-adapted organism '
                'becomes a product for the deep-space construction crews. The presentation '
                'is professional, the biology is genuine, and the buyers leave with a '
                'catalogue of possibilities that they could not develop from their own '
                'technology base. The Pleiades has something that nobody else has: alien '
                'life that has solved survival problems that human biology cannot solve '
                'alone. The trade is the translation of those solutions into products that '
                'the rest of the galaxy can use.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Ossivane',
            short_description='A gas giant under the red giant\'s deep light -- fuel processing for the inter-faction traffic, with alien atmospheric organisms adapted to the red star\'s spectral output.',
            long_description=(
                'Ossivane is the system\'s gas giant -- fuel processing on its moons '
                'supporting the inter-faction traffic that the trade hub generates. The '
                'alien life in Ossivane\'s atmosphere is adapted to the red giant\'s deep '
                'spectral output -- the organisms photosynthesise in wavelengths that are '
                'nearly invisible to baseline human eyes, producing a bioluminescence in '
                'the deep infrared that makes the gas giant\'s atmosphere appear to glow '
                'to visitors with modified visual range and appear dark to those without.\n\n'
                'The infrared bioluminescence has commercial value -- the compounds are '
                'used in the visual-range modification packages that the Pleiades offers '
                'to buyers who want enhanced perception. The fuel processors work '
                'alongside the organism harvesters, the two operations sharing the moons '
                'with the practical coexistence that commerce between different industries '
                'produces.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Wendern',
            short_description='An agricultural world producing food for the trade hub\'s diverse population -- multiple cuisine tracks for the buyers from different factions who eat different things.',
            long_description=(
                'Wendern is the system\'s agricultural world -- and one of the most '
                'culinarily diverse in the cluster. The trade hub\'s population includes '
                'Pleiadian residents with various levels of splicing, baseline visitors '
                'from MERIT space, and the buyers from other factions whose dietary '
                'requirements reflect their own modification cultures. Wendern\'s farms '
                'produce food across the compatibility spectrum: baseline terrestrial for '
                'the MERIT visitors, modified terrestrial for the lightly spliced, and '
                'the alien-hybrid food that the more deeply adapted local population '
                'requires.\n\n'
                'The farming under the red giant\'s light produces crops with a distinctive '
                'colour palette -- the photosynthesis adapted for the deep red spectral '
                'output produces vegetation in dark purples and near-blacks that look '
                'unsettling to visitors from blue-white or yellow-star systems. The food '
                'tastes normal. The appearance is the star\'s contribution to the general '
                'atmosphere of wrongness that visitors to the Pleiades learn to tolerate.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The cluster\'s shopfront -- seven billion people selling Pleiadian biology to every faction in the galaxy, on a trading floor that smells different in every section.',
    long_description=(
        'Mirach is where the Pleiades sells its biology to the rest of the galaxy. '
        'The system is the cluster\'s primary trade hub -- the place where the alien-'
        'derived gene therapies, biological compounds, and living organisms that the '
        'Pleiades has developed are adapted for non-Pleiadian bodies and sold to '
        'every faction willing to buy. The Antares buys compounds that enhance drug '
        'efficacy. Canopus buys tissue-preservation techniques. The Hyades buys '
        'biological interface substrates. MERIT\'s black market absorbs Pleiadian '
        'gene therapies through channels the confederation officially does not '
        'acknowledge.\n\n'
        'The Bourse -- the orbital trading station -- is the largest biological '
        'trading installation in the galaxy. Where the Hyades\' Emporium trades '
        'inert hardware in crates, the Bourse trades living compounds in climate-'
        'controlled containers. The trading floor smells different in every section. '
        'The security is biological rather than military -- a broken gene therapy '
        'vial could contaminate the station with compounds the environmental systems '
        'cannot clear.\n\n'
        'Thenvale manufactures the export-grade products -- reformulating Pleiadian '
        'biology for baseline bodies in laboratories where the testing animals '
        'include results the reports categorise as inconclusive. Strannik showcases '
        'the alien organisms in curated habitats where the buyers are shown what '
        'each species\' adaptive traits can become when translated into gene '
        'therapies for their populations.\n\n'
        'The star is a red giant -- deep, cool light that makes the vegetation '
        'grow in purples and near-blacks and that the traders consider atmospheric. '
        'Seven billion people selling the most advanced biological technology in '
        'the galaxy to buyers who want the alien biology without the commitment '
        'of becoming something else. The Pleiades has what nobody else has: alien '
        'life that has solved survival problems human biology cannot solve alone. '
        'The trade is the translation. The price is negotiable. The biology is not.'
    ),
    cluster=StarClusters.PLEIADES,
)

TAYGETA = System(
    name='Taygeta',
    star='Blue-white subgiant (B6IV), approximately 600 times Sol luminosity -- a hot, bright star whose light presses down on a world where everything is heavy and the people have become heavy to match',
    population=10_000_000_000,
    distance_to_sol=440.0,
    stellar_objects=[
        StellarObject(
            name='Gravmark',
            short_description='The heaviest world in the cluster -- six billion people spliced with the genes of alien megafauna to survive a gravity that would cripple a baseline human in hours.',
            long_description=(
                'Gravmark is a large, dense world with a surface gravity of approximately '
                '2.4 standard -- high enough that a baseline human standing on the surface '
                'would feel their weight more than double, their cardiovascular system '
                'labouring, their joints compressing, their movement reduced to a careful '
                'shuffle that would become collapse within hours. Nobody baseline lives on '
                'Gravmark. The population is spliced.\n\n'
                'The alien megafauna on Gravmark is what made colonisation possible. The '
                'world\'s native life evolved under the crushing gravity -- massive '
                'creatures with dense musculature, reinforced skeletal structures of a '
                'calcium-silicate composite that is stronger than bone, cardiovascular '
                'systems with multiple hearts that push blood against the gravity\'s drag, '
                'and cellular structures that resist compression at pressures that would '
                'rupture terrestrial cells. The colonists studied the megafauna, identified '
                'the gene sequences responsible for the adaptations, and spliced them into '
                'the human population.\n\n'
                'The result is a strain that does not look baseline. The Gravmark population '
                'is shorter, broader, and denser than any other human strain -- compressed '
                'frames packed with the dense musculature the alien genes provide, '
                'thickened skin with the alien calcium-silicate reinforcement woven through '
                'the dermal layers, and the dual cardiovascular system that the gravity '
                'demands. A Gravmark worker is visibly, unmistakably not baseline. The '
                'proportions are wrong. The skin has a mineral sheen from the silicate '
                'deposits. The movement is powerful and deliberate in a way that reads as '
                'alien to visitors who see them on the rare occasions that Gravmark\'s '
                'population travels offworld.\n\n'
                'The trapping is the gravity. A Gravmark worker\'s dual cardiovascular '
                'system is designed to push blood against 2.4 standard gravity. At '
                'standard gravity, the system overpressures -- the hearts push blood with '
                'a force that the lower gravity does not resist, producing vascular damage, '
                'headaches, haemorrhaging in the extremities, and the long-term organ '
                'damage that makes extended stays at standard gravity life-threatening. A '
                'Gravmark citizen can visit a standard-gravity world for days. Living on one '
                'would kill them within months. The adaptation that lets them survive on '
                'Gravmark is the adaptation that imprisons them there.\n\n'
                'The heavy industry on Gravmark is the system\'s purpose. The dense world '
                'is mineral-rich, the gravity concentrating heavy elements in accessible '
                'deposits. The foundries and fabrication plants operate at a scale that '
                'rivals Alpha Pegasi in the Hyades -- structural materials, ship '
                'components, and the heavy industrial goods that the cluster\'s economy '
                'requires. The workers carry the industrial loads in the crushing gravity '
                'with the strength the megafauna genes provide, doing work that no other '
                'human strain could perform and that no machine has been built to replace, '
                'because the machines designed for 2.4g are more expensive than the workers '
                'the splicing produces.'
            ),
            population=6_000_000_000,
        ),
        StellarObject(
            name='The Reserves',
            short_description='The managed wilderness where Gravmark\'s megafauna is maintained -- the living gene bank whose DNA the colony\'s existence depends on.',
            long_description=(
                'The Reserves are the managed wilderness zones on Gravmark where the alien '
                'megafauna is maintained in near-natural conditions. The megafauna is the '
                'colony\'s gene bank -- the living source of the gene sequences that the '
                'population\'s splicing depends on. The creatures are enormous: the largest '
                'herbivores mass over thirty tonnes, moving across the high-gravity plains '
                'with a slow, grinding power that makes the ground vibrate under their '
                'passage. The predators are smaller but dense -- compact killing machines '
                'whose calcium-silicate-reinforced claws can tear through materials that '
                'would stop a cutting tool.\n\n'
                'The Reserves are maintained by wildlife management teams whose splicing '
                'includes the megafauna\'s sensory adaptations -- enhanced hearing tuned to '
                'the low-frequency vibrations the creatures use to communicate, and the '
                'chemical sensitivity that detects the pheromone markers the predators use '
                'to define territory. The management teams live among the megafauna in '
                'conditions that would terrify a baseline visitor and that the teams '
                'consider routine. The creatures are not domesticated. They are managed, '
                'which means respected, avoided when aggressive, and studied continuously '
                'for the genetic variations that might improve the next generation of '
                'human splicing.'
            ),
            population=0,
        ),
        StellarObject(
            name='Culvane',
            short_description='An orbital station in standard gravity -- where Gravmark\'s population goes for medical treatment their bodies cannot receive on the surface, limited to days before the low gravity starts killing them.',
            long_description=(
                'Culvane is an orbital station above Gravmark that serves a specific and '
                'painful function: medical treatment that requires standard gravity. Some '
                'procedures -- delicate surgeries, certain gene-therapy adjustments, the '
                'calibration of the splicing that maintains the population\'s stability '
                '-- are easier to perform when the patient\'s cardiovascular system is not '
                'fighting 2.4g. The patients travel to Culvane for treatment and return '
                'to the surface as quickly as possible, because every hour at standard '
                'gravity is an hour their overpressured cardiovascular system is damaging '
                'itself.\n\n'
                'The medical staff on Culvane are the system\'s most conflicted '
                'professionals. They treat patients by bringing them to an environment '
                'that is slowly hurting them -- the treatment requires standard gravity, '
                'but the body requires high gravity, and the schedule is a race between '
                'completing the procedure and the onset of vascular damage. The stays are '
                'measured in days. The staff monitor the patients\' blood pressure, '
                'vascular integrity, and the micro-haemorrhaging that begins within hours '
                'of arrival. The patients endure it because the alternative is not '
                'receiving the treatment, and they return to the crushing surface with '
                'relief because the gravity that traps them is also the gravity their '
                'bodies were built for.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Drowen',
            short_description='A standard-gravity world where the system\'s trade and diplomacy are conducted -- populated by the lightly spliced who can travel, serving a population that cannot.',
            long_description=(
                'Drowen is a standard-gravity world in the outer habitable zone -- cooler, '
                'less hospitable, but liveable for baseline and lightly spliced humans. '
                'The planet houses the system\'s trade infrastructure, the diplomatic '
                'facilities, and the population of lightly spliced Pleiadians who serve as '
                'Taygeta\'s interface with the rest of the cluster. The Gravmark population '
                'cannot come here -- the standard gravity would damage them. The diplomats '
                'on Drowen represent six billion people they can visit only briefly and '
                'carefully, conducting the system\'s business on behalf of a population '
                'that is trapped on a world the diplomats cannot live on.\n\n'
                'The alien life on Drowen is standard-gravity fauna -- smaller, lighter '
                'species than Gravmark\'s megafauna, adapted for conditions that baseline '
                'humans find tolerable. The biosphere has been partially managed and the '
                'splicing available on Drowen is modest -- the light adaptations that make '
                'the local pathogens survivable and the minor enhancements that the '
                'diplomatic population carries for professional rather than survival '
                'reasons. Drowen is the normal world in an abnormal system, and the '
                'residents carry the awareness that normalcy is a privilege that six '
                'billion people below them cannot share.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='Ossander',
            short_description='A gas giant whose moons host fuel processing and the alien organisms that thrive in the high-pressure lower atmosphere -- species that survive pressures the Gravmark population was spliced to match.',
            long_description=(
                'Ossander is the system\'s gas giant -- a large body whose deep atmosphere '
                'hosts alien organisms adapted for pressures that exceed even Gravmark\'s '
                'surface gravity. The deep-atmosphere species are being studied for gene '
                'sequences that could improve the Gravmark population\'s pressure tolerance '
                '-- the current splicing allows survival at 2.4g, but the industrial '
                'demands of the deep mines push workers into environments where even the '
                'spliced body is at its limits.\n\n'
                'The fuel processing on Ossander\'s moons supports the system\'s heavy '
                'industrial traffic -- the freighters that carry Gravmark\'s industrial '
                'output to the rest of the cluster. The fuel workers are lightly spliced '
                '-- standard-gravity operations that the Gravmark population could not '
                'perform without the vascular damage that low gravity causes them. The '
                'irony is structural: the people who produce the industrial goods cannot '
                'operate the ships that carry them.'
            ),
            population=80_000_000,
        ),
        StellarObject(
            name='Ondrath',
            short_description='An agricultural world feeding the system -- alien-hybrid crops grown under high gravity by farmers whose splicing matches the world they feed.',
            long_description=(
                'Ondrath is an agricultural moon of Gravmark -- high-gravity, farmed by '
                'workers with the same megafauna splicing as the industrial population. '
                'The crops are alien-terrestrial hybrids engineered for the gravity and '
                'the soil chemistry -- food that the Gravmark population can eat and that '
                'baseline humans cannot, because the nutritional compounds that sustain a '
                'body with dual cardiovascular systems and calcium-silicate skeletal '
                'reinforcement are toxic to a body without them.\n\n'
                'The food supply is the final layer of the trap. The Gravmark population '
                'cannot leave because the gravity would damage them. They also cannot '
                'leave because the food they need is produced under the gravity they '
                'require, from organisms adapted for conditions they share, in a closed '
                'loop that makes every element of survival dependent on every other element '
                'and that makes escape not a question of transportation but of biology.'
            ),
            population=800_000_000,
        ),
    ],
    short_description='The heaviest world -- ten billion people in a system where the gravity spliced them into something that cannot leave, doing work that no other strain can perform.',
    long_description=(
        'Taygeta is the Pleiades\' heavy industry system -- a high-gravity world '
        'where the population has been spliced with the genes of alien megafauna to '
        'survive a surface gravity of 2.4 standard. The splicing is extensive: dense '
        'musculature, calcium-silicate skeletal reinforcement, dual cardiovascular '
        'systems, thickened skin with mineral deposits. The Gravmark population is '
        'shorter, broader, and denser than any other human strain -- visibly, '
        'unmistakably not baseline.\n\n'
        'The trapping is the gravity. The dual cardiovascular system designed for '
        '2.4g overpressures at standard gravity -- vascular damage, haemorrhaging, '
        'organ damage that makes extended stays at standard gravity life-threatening. '
        'A Gravmark citizen can visit a normal world for days. Living on one would '
        'kill them within months. The adaptation that lets them survive is the '
        'adaptation that imprisons them. The food they eat is grown under the '
        'gravity they require, from organisms adapted for conditions they share, in '
        'a closed loop that makes escape a question of biology rather than '
        'transportation.\n\n'
        'The megafauna is the gene bank -- thirty-tonne herbivores on the high-'
        'gravity plains, compact predators with calcium-silicate claws, maintained '
        'in the Reserves by management teams spliced with the creatures\' sensory '
        'adaptations. Culvane station provides the medical treatments that require '
        'standard gravity, conducted as a race between completing the procedure and '
        'the onset of vascular damage. Drowen houses the diplomats who represent '
        'six billion people they can visit only briefly -- conducting business on '
        'behalf of a population trapped on a world the diplomats cannot live on.\n\n'
        'The heavy industry rivals Alpha Pegasi -- structural materials, ship '
        'components, industrial goods produced by workers who carry the loads in '
        'crushing gravity with the strength the megafauna genes provide. The work '
        'that no other strain could perform and that no machine replaces, because '
        'the machines designed for 2.4g are more expensive than the workers the '
        'splicing produces. Ten billion people in a system where the planet made '
        'the people and the people cannot leave the planet.'
    ),
    cluster=StarClusters.PLEIADES,
)

CELAENO = System(
    name='Celaeno',
    star='Blue-white subgiant (B7IV), approximately 300 times Sol luminosity -- a hot star illuminating worlds where the soil is poison to terrestrial crops and the solution was to stop growing terrestrial crops',
    population=8_000_000_000,
    distance_to_sol=430.0,
    stellar_objects=[
        StellarObject(
            name='Haldren',
            short_description='The cluster\'s breadbasket -- four billion people farming an alien biosphere that they have spliced themselves to eat, on soil that would kill a terrestrial crop in days.',
            long_description=(
                'Haldren is the Pleiades\' primary agricultural world and the system that '
                'demonstrates the cluster\'s philosophy most clearly: it is cheaper to '
                'change the human than to change the planet. The soil on Haldren is rich '
                'in compounds that are toxic to terrestrial biology -- heavy metal '
                'concentrations and alien biochemical residues that kill terrestrial crops '
                'within days of planting. Terraforming the soil would have taken decades '
                'and cost more than the colony could justify. The alternative was to farm '
                'what the soil could already grow.\n\n'
                'The crops on Haldren are alien. The native plants that thrive in the '
                'toxic soil were identified, cultivated, and modified into agricultural '
                'strains that produce food -- food that a baseline human cannot eat, '
                'because the same heavy metal compounds that the plants absorb from the '
                'soil are concentrated in the edible portions at levels that would cause '
                'organ damage in an unmodified body. The solution was to modify the body. '
                'The farming population on Haldren carries digestive splicing that lets '
                'them metabolise the alien food safely -- modified liver function that '
                'processes the heavy metal compounds, altered gut bacteria that break down '
                'the alien proteins, and the cellular adaptations that sequester the '
                'residual toxins in tissues that can tolerate them.\n\n'
                'The food chain on Haldren is entirely alien-derived. The crops grow in '
                'alien soil. The livestock are alien species domesticated from the native '
                'fauna -- slow, heavy grazers whose meat is rich in the same compounds '
                'that make the crops toxic to baseline humans. The dairy equivalents are '
                'secretions from alien organisms that the population has learned to '
                'process into something that functions as food for their modified '
                'digestive systems. A meal on Haldren looks wrong, smells wrong, and '
                'would hospitalize a baseline visitor who tried to eat it.\n\n'
                'The farming is the trap. The digestive splicing that lets the population '
                'eat Haldren\'s food is the same splicing that makes terrestrial food '
                'difficult to digest. The modified gut bacteria that break down the alien '
                'proteins are less effective at processing terrestrial proteins. The '
                'altered liver that handles the heavy metal compounds handles standard '
                'terrestrial nutrition less efficiently. A Haldren farmer can survive on '
                'terrestrial food -- it is not lethal the way Haldren\'s food is to a '
                'baseline human -- but the nutrition is poor, the digestion is difficult, '
                'and the farmer\'s body functions better on the alien food it was modified '
                'to eat. The modification does not prevent leaving. It makes leaving '
                'uncomfortable enough that most people stay.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Serricane',
            short_description='A second agricultural world specialising in the livestock operations -- alien herd animals managed by farmers whose splicing includes the sensory adaptations to work with species that do not think like terrestrial animals.',
            long_description=(
                'Serricane is Celaeno\'s livestock world -- a warmer planet with the '
                'extensive grasslands that the alien herd animals require. The livestock '
                'species were domesticated from Celaeno\'s native fauna over generations '
                'of selective breeding and genetic management, producing animals that are '
                'tractable enough to farm and alien enough that the farming requires '
                'adaptations a terrestrial rancher would not anticipate.\n\n'
                'The alien herd animals do not behave like terrestrial livestock. Their '
                'social structures are chemical rather than visual -- the herds organise '
                'around pheromone hierarchies that the animals perceive and that baseline '
                'humans cannot detect. A farmer who cannot read the pheromone signals '
                'cannot manage the herd -- cannot identify the dominant animals, cannot '
                'predict the movement patterns, cannot detect the stress signals that '
                'precede a stampede. The farming population on Serricane carries sensory '
                'splicing that gives them the chemical perception the work requires -- '
                'modified olfactory systems that detect the pheromone markers, and the '
                'neural processing to interpret them. A Serricane farmer smells the herd '
                'the way a terrestrial rancher watches it.\n\n'
                'The sensory splicing produces side effects the farmers accept as part of '
                'the job. The enhanced olfactory system that detects alien pheromones also '
                'detects human biochemical signals with uncomfortable precision. A '
                'Serricane farmer can smell fear, arousal, illness, and deception on other '
                'humans -- not with the specificity that the alien pheromones provide but '
                'with enough clarity that social interactions off-farm carry an undercurrent '
                'of involuntary perception that the farmers find intrusive and that their '
                'neighbours find unsettling. The farmers learn to ignore what they smell. '
                'The neighbours learn not to ask what the farmers can detect.'
            ),
            population=1_500_000_000,
        ),
        StellarObject(
            name='The Silo',
            short_description='An orbital processing station where the alien food is prepared for distribution -- packaged by strain compatibility, because one strain\'s nutrition is another strain\'s poison.',
            long_description=(
                'The Silo is Celaeno\'s primary orbital facility -- a food processing and '
                'distribution station where the agricultural output from Haldren and '
                'Serricane is packaged and shipped to the rest of the cluster. The '
                'packaging is the complexity: the food must be sorted by strain '
                'compatibility, because the digestive splicing varies between strains and '
                'the food that nourishes one strain may be indigestible or toxic to another.\n\n'
                'The Silo maintains the cluster\'s most comprehensive dietary compatibility '
                'database -- a catalogue of which foods are safe for which strains, updated '
                'as new modifications alter the populations\' digestive capabilities. The '
                'logistics are a nightmare of biological specificity: a shipment destined '
                'for Taygeta must be compatible with the heavy-gravity strain\'s modified '
                'metabolism. A shipment for Asterope must account for the radiation '
                'strain\'s altered nutrient requirements. A shipment for Merope must meet '
                'the aesthetic standards of a population that expects food to be beautiful '
                'as well as edible. A mislabelled shipment is not an inconvenience. A '
                'mislabelled shipment is a medical emergency.\n\n'
                'The Silo also produces the baseline-compatible food supplements that '
                'the diplomatic class requires -- processed versions of the alien food '
                'that have been modified to remove the toxic compounds and reformulated '
                'for baseline digestion. The supplements taste nothing like the original '
                'food. The diplomatic class eats them without complaint because the '
                'alternative is starving on worlds where the local cuisine is lethal.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Vedderan',
            short_description='A world where the alien biosphere is being studied for new crop species -- the agricultural research frontier, where the gene-splicing and the farming intersect.',
            long_description=(
                'Vedderan is Celaeno\'s agricultural research world -- a planet with a '
                'rich alien biosphere that the researchers are systematically cataloguing '
                'for potential crop species. The work is slow and careful: each candidate '
                'species must be assessed for nutritional value, toxicity profile, '
                'cultivation requirements, and the digestive splicing that the consuming '
                'population would need. A new crop species that feeds one strain may '
                'require modification packages that take years to develop and test.\n\n'
                'The animal testing on Vedderan is agricultural rather than medical -- '
                'test subjects fed the candidate crops to determine digestive compatibility '
                'before the food is approved for human consumption. The testing is '
                'extensive because the consequences of a miscalculated crop are population-'
                'scale: a food supply that passes testing but produces long-term '
                'cumulative toxicity could damage an entire strain before the effects are '
                'detected. The researchers on Vedderan carry the weight of this '
                'responsibility with the caution of people who understand that their '
                'errors are measured in lives rather than data points.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Pellethen',
            short_description='A gas giant with fuel processing and alien atmospheric organisms whose metabolic compounds are being evaluated as potential flavouring agents for the alien food industry.',
            long_description=(
                'Pellethen is the system\'s gas giant -- fuel processing on its moons '
                'supporting the heavy freighter traffic that the agricultural exports '
                'generate. The alien organisms in Pellethen\'s atmosphere produce metabolic '
                'compounds that the food researchers on Vedderan have identified as '
                'potential flavouring agents -- organic molecules that interact with the '
                'modified taste receptors of the spliced population to produce flavour '
                'experiences that terrestrial food chemistry cannot replicate.\n\n'
                'The harvesting is in early stages. The compounds are being tested on '
                'Vedderan\'s subjects for compatibility and the results are promising -- '
                'the flavouring agents appear to be safe for the major strains and produce '
                'taste responses that the test panels describe as extraordinary. The food '
                'industry on Merope has expressed interest. The researchers caution that '
                'the testing is incomplete. The food industry is impatient. The compounds '
                'are potentially lucrative. The tension between caution and commerce is '
                'familiar to everyone in the Pleiades.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Scaldwell',
            short_description='A hot inner world -- energy collection for the system\'s agricultural operations and the seed vaults where the alien crop strains are preserved against catastrophe.',
            long_description=(
                'Scaldwell is a hot inner world with solar collection arrays powering '
                'Celaeno\'s agricultural infrastructure and the system\'s seed vaults. The '
                'vaults preserve samples of every alien crop strain the Pleiades has '
                'developed -- the genetic library that the cluster\'s food supply depends '
                'on, stored in sealed, temperature-controlled facilities that are '
                'hardened against military attack, stellar events, and the contamination '
                'that would make the samples unusable.\n\n'
                'The seed vaults are the cluster\'s agricultural insurance. A catastrophe '
                'that destroyed Haldren\'s crops could be recovered from the vaults. A '
                'blight that swept through a strain\'s food supply could be replaced with '
                'resistant variants stored on Scaldwell. The vaults are the quietest and '
                'most important facility in the system -- maintained by staff who '
                'understand that the seeds in their care are more valuable than the '
                'industrial output of entire systems, because the industrial output feeds '
                'machines and the seeds feed people.'
            ),
            population=15_000_000,
        ),
    ],
    short_description='The breadbasket -- eight billion people farming an alien biosphere they have spliced themselves to eat, producing food that nourishes the modified and poisons the baseline.',
    long_description=(
        'Celaeno feeds the Pleiades cluster with food that would kill anyone who has '
        'not been modified to eat it. The system\'s soil is toxic to terrestrial '
        'crops -- heavy metal compounds and alien biochemical residues that kill '
        'terrestrial plants within days. Terraforming the soil would have taken '
        'decades. Modifying the humans took less. The crops are alien. The livestock '
        'are alien. The food chain is alien. The people who eat it carry digestive '
        'splicing -- modified livers, altered gut bacteria, cellular adaptations -- '
        'that lets them metabolise what would hospitalise a baseline visitor.\n\n'
        'The farming is the trap. The digestive splicing that lets the population '
        'eat Haldren\'s food makes terrestrial food harder to digest. The modified '
        'gut handles alien proteins and handles terrestrial proteins less efficiently. '
        'The modification does not prevent leaving. It makes leaving uncomfortable '
        'enough that most people stay -- their bodies function better on the alien '
        'food they were modified to eat.\n\n'
        'Serricane\'s livestock operations add the sensory dimension -- farmers '
        'spliced with olfactory systems that detect alien pheromone hierarchies, '
        'who can smell fear and illness on other humans as an unwanted side effect. '
        'The Silo packages the food by strain compatibility -- one strain\'s '
        'nutrition is another\'s poison, and a mislabelled shipment is a medical '
        'emergency. Vedderan researches new crop species with the caution of people '
        'whose errors are measured in lives.\n\n'
        'Eight billion people producing the food that a civilisation of diverging '
        'sub-species requires -- a food supply as fragmented as the population it '
        'feeds, sorted by compatibility, segregated by biology, and growing in soil '
        'that would kill the crops that fed the species these people used to be.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLEIONE = System(
    name='Pleione',
    star='Blue-white dwarf (B8IVpe), a shell star with an unstable circumstellar disc of ejected material -- a star that is shedding itself, orbited by worlds where the science of changing what a body is has been perfected',
    population=6_000_000_000,
    distance_to_sol=390.0,
    stellar_objects=[
        StellarObject(
            name='Rendeven',
            short_description='The laboratory world -- three billion people in a system where every gene-splicing procedure in the cluster is designed, tested, and approved, and where the testing is the thing nobody talks about.',
            long_description=(
                'Rendeven is where the Pleiades makes its people. The planet is the '
                'cluster\'s primary bioengineering centre -- the place where every gene-'
                'splicing procedure available in the Pleiades is designed, prototyped, '
                'tested, and certified for use. The research institutions on Rendeven are '
                'the most advanced biological laboratories in the galaxy -- staffed by '
                'bioengineers whose own splicing includes cognitive enhancements derived '
                'from alien neural organisms, giving them processing speed and pattern '
                'recognition that baseline researchers cannot match.\n\n'
                'The design process begins with the alien biology. A gene sequence is '
                'identified in an alien organism -- radiation resistance from an Asterope '
                'species, pressure tolerance from a deep-ocean organism, thermal '
                'regulation from a desert-adapted fauna. The sequence is isolated, '
                'analysed, and mapped against the human genome to identify integration '
                'points. The integration is designed on Rendeven\'s computers. The '
                'integration is tested on Rendeven\'s subjects.\n\n'
                'The testing is the system\'s weight. The gene-splicing must be validated '
                'before human application, and the validation requires subjects that are '
                'biologically close enough to human that the results are meaningful. The '
                'testing programme uses cloned human tissue matrices -- engineered '
                'biological constructs that are not legally persons but that are '
                'functionally human tissue, grown in vats to the developmental stage where '
                'the splicing can be applied and the results observed. The matrices develop '
                'organ systems. The matrices respond to stimuli. The matrices, in the later '
                'stages of testing, develop nervous systems that register what is being '
                'done to them in ways the ethical oversight committees have decided do not '
                'constitute pain because the matrices are not legally persons.\n\n'
                'The failures are the worst of it. A splicing that works on the tissue '
                'matrix may produce unintended interactions -- the alien gene sequence '
                'expressing in tissues it was not designed for, producing growths, '
                'deformities, organ failures, and the cascading biological errors that the '
                'researchers catalogue as adverse outcomes. The matrices that experience '
                'adverse outcomes are maintained for study until the research value is '
                'exhausted. The duration of the study depends on the nature of the '
                'outcome. Some outcomes are studied for months. The matrices are alive for '
                'all of them.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Columns',
            short_description='The testing facilities -- an orbital complex of laboratories where the tissue matrices are grown, modified, and observed, in wings that the station\'s general population is not permitted to enter.',
            long_description=(
                'The Columns are the orbital testing complex above Rendeven -- a facility '
                'dedicated to the growth, modification, and observation of the tissue '
                'matrices that the gene-splicing validation requires. The name comes from '
                'the growth chambers -- vertical cylinders in which the matrices develop, '
                'arranged in rows that extend through the facility\'s core, each one '
                'containing a biological construct at a different stage of development.\n\n'
                'The Columns are divided into stages. The early-stage wings contain the '
                'matrices in initial growth -- undifferentiated tissue that has not yet '
                'developed the organ systems that make the later stages uncomfortable to '
                'observe. The mid-stage wings contain the matrices that have been spliced '
                'and are being monitored for integration. The late-stage wings contain the '
                'matrices that have fully developed and that display the results of the '
                'splicing -- the successes, which are documented and harvested for the data '
                'they contain, and the failures, which are documented and maintained for '
                'as long as the data requires.\n\n'
                'The late-stage wings are restricted. The staff who work there carry '
                'psychological support splicing -- modifications to the stress response '
                'that reduce the emotional impact of the work. The modifications were '
                'developed specifically for the Columns\' staff after the early years '
                'produced burnout rates that threatened the programme\'s viability. The '
                'staff can now observe the late-stage matrices -- including the failures, '
                'including the ones that have developed enough neural complexity to respond '
                'to the observation -- without the psychological cost that unmodified '
                'researchers experienced. The solution to the researchers\' trauma was to '
                'modify the researchers. The irony is noted in the programme\'s own '
                'literature, in a footnote, without comment.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Drethven',
            short_description='The stabilisation compound production world -- Pleione\'s secondary source of the compounds that prevent cumulative splicing from cascading into genetic instability.',
            long_description=(
                'Drethven is a cold, rocky world with a unique alien biosphere that '
                'produces the biological precursors for stabilisation compounds. The '
                'production is Pleione\'s secondary contribution to the cluster\'s '
                'stabilisation supply -- smaller than Electra\'s output but significant '
                'enough that the loss of Drethven would reduce the cluster\'s total '
                'stabilisation capacity by approximately fifteen percent.\n\n'
                'The alien organisms on Drethven that produce the precursors are '
                'slow-growing, environmentally sensitive, and difficult to cultivate at '
                'scale. The production is limited by the biology rather than the demand '
                '-- the organisms grow at the rate they grow and the bioengineers have '
                'not found a way to accelerate the process without degrading the '
                'compounds\' efficacy. The production staff manage the organisms with the '
                'patience of people who understand that the biology sets the schedule and '
                'the schedule does not negotiate.\n\n'
                'Drethven also hosts the synthetic stabilisation programme -- the ongoing '
                'effort to produce stabilisation compounds artificially rather than '
                'biologically. The programme has produced synthetic alternatives that '
                'partially replicate the biological compounds\' function, reducing the '
                'cluster\'s total dependency on Electra and Drethven. The synthetics are '
                'less effective than the biologicals -- they stabilise the common '
                'modification packages but struggle with the deeper, more complex splicing '
                'that the outer-world populations carry. The deeply adapted strains still '
                'need the biological compounds. The synthetics buy time. They do not '
                'solve the problem.'
            ),
            population=500_000_000,
        ),
        StellarObject(
            name='Vervain',
            short_description='A residential world where the laboratory workforce lives -- communities shaped by the awareness that the work their partners do involves things that are almost human.',
            long_description=(
                'Vervain is the system\'s residential world -- a temperate, partially '
                'terraformed planet where the research workforce raises families away from '
                'the laboratories. The communities are comfortable by Pleiadian standards '
                '-- managed alien biosphere, breathable atmosphere with minor splicing '
                'required, and the amenities that a well-funded research system provides '
                'its staff.\n\n'
                'The culture on Vervain is shaped by what the residents do for a living. '
                'The bioengineers and lab technicians who work on Rendeven and the Columns '
                'come home to families who know, in general terms, what the work involves. '
                'The specifics are not discussed. The staff who work in the late-stage '
                'wings carry their psychological support splicing into their personal lives '
                '-- the dampened stress response that lets them observe the matrices also '
                'dampens their emotional responses to their families, their children, their '
                'relationships. The partners notice. The children notice. The dampening '
                'that makes the work bearable makes the worker slightly less present in '
                'their own life, and the families on Vervain have developed a culture of '
                'quiet accommodation around partners who come home from the Columns a '
                'little distant, a little flat, a little less able to feel the things that '
                'the work requires them not to feel.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='Ostaven',
            short_description='A gas giant with fuel processing and alien atmospheric life whose neural compounds are harvested for the cognitive enhancement splicing the researchers carry.',
            long_description=(
                'Ostaven is the system\'s gas giant -- fuel processing on its moons '
                'supporting the system\'s traffic. The alien organisms in Ostaven\'s '
                'atmosphere are notable for their neural complexity -- the gas-dwelling '
                'species have developed distributed nervous systems that process '
                'environmental data across their entire bodies, and the neural compounds '
                'they produce are the basis for the cognitive enhancement splicing that '
                'Rendeven\'s researchers carry.\n\n'
                'The harvesting is conducted by specialised crews who enter the atmosphere '
                'in shielded craft and collect the neural compounds from the organisms '
                'without killing them -- the organisms regenerate the compounds, making '
                'the harvesting sustainable if conducted carefully. The crews describe the '
                'organisms as the most alien life they have encountered: beings that are '
                'essentially floating nervous systems, sensing and processing and '
                'responding to an environment that humans can barely survive. The '
                'researchers find them beautiful. The crews find them unsettling. The '
                'compounds they produce make the researchers smarter, which the crews '
                'consider an arrangement that benefits the researchers more than the '
                'organisms.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Asperal',
            short_description='An agricultural world feeding the system -- alien-hybrid farming under the shell star\'s variable light, with crop strains adapted for the irregular illumination.',
            long_description=(
                'Asperal is the system\'s agricultural world -- partially terraformed, '
                'farmed with alien-hybrid crops by a spliced workforce. The shell star\'s '
                'circumstellar disc causes the light to vary as the disc material shifts '
                '-- the illumination fluctuates unpredictably, dimming when the disc is '
                'dense and brightening when it thins. The crop strains on Asperal are '
                'adapted for the variable light -- alien photosynthetic pathways that '
                'function across a range of illumination levels, storing energy during '
                'bright periods and drawing on reserves during the dim.\n\n'
                'The farmers carry the standard agricultural splicing plus the visual '
                'adaptations that let them work under the fluctuating light without the '
                'headaches and disorientation that the variation produces in unmodified '
                'eyes. The star\'s instability is Pleione\'s defining atmospheric feature '
                '-- a light that cannot be relied upon, illuminating a system where the '
                'question of what a body should be is answered differently every day in '
                'the laboratories above.'
            ),
            population=500_000_000,
        ),
    ],
    short_description='The laboratory -- six billion people in the system where every gene-splicing procedure in the cluster is designed, and where the testing is conducted on things that are not legally persons but that have developed enough to respond to what is being done to them.',
    long_description=(
        'Pleione is where the Pleiades makes its people. The system is the cluster\'s '
        'primary bioengineering centre -- every gene-splicing procedure available in '
        'the Pleiades is designed, prototyped, tested, and certified on Rendeven. The '
        'research institutions are the most advanced biological laboratories in the '
        'galaxy, staffed by researchers whose own cognitive splicing gives them '
        'processing speed derived from alien neural organisms.\n\n'
        'The testing is the weight. The gene-splicing must be validated on cloned '
        'human tissue matrices -- biological constructs that are not legally persons '
        'but that develop organ systems, respond to stimuli, and in the later '
        'stages develop nervous systems that register what is being done to them in '
        'ways the ethical committees have decided do not constitute pain. The '
        'Columns -- the orbital testing complex -- contain the growth chambers in '
        'rows, each cylinder holding a construct at a different stage. The late-'
        'stage wings are restricted. The staff carry psychological support splicing '
        'that reduces the emotional impact of the work. The solution to the '
        'researchers\' trauma was to modify the researchers.\n\n'
        'Drethven produces stabilisation compounds -- the cluster\'s secondary '
        'source after Electra, approximately fifteen percent of total supply. The '
        'synthetic alternative programme produces compounds that stabilise common '
        'modifications but struggle with the deeper splicing the outer-world '
        'populations carry. The synthetics buy time. They do not solve the problem.\n\n'
        'Vervain houses the workforce in communities shaped by the awareness of '
        'what the work involves. The staff who carry the psychological dampening '
        'that makes the Columns bearable bring it home -- slightly less present, '
        'slightly less able to feel the things the work requires them not to feel. '
        'The star is a shell star shedding its own material into a circumstellar '
        'disc, casting variable light on a system where the science of changing '
        'what a body is has been perfected, and where the cost of the perfection '
        'is measured in constructs that are alive and not legally persons and that '
        'respond to the observation in ways the programme has decided not to '
        'investigate too carefully.'
    ),
    cluster=StarClusters.PLEIADES,
)

ASTEROPE = System(
    name='Asterope',
    star='Blue-white main sequence binary (B9V + A0V), approximately 300 times combined Sol luminosity -- two hot stars bathing the system in ultraviolet radiation that kills baseline tissue and feeds the alien life that the miners have become',
    population=5_000_000_000,
    distance_to_sol=430.0,
    stellar_objects=[
        StellarObject(
            name='Skathren',
            short_description='The radiation world -- three billion people spliced with alien organisms that thrive in ultraviolet saturation, who have become so visibly non-human that visitors from other systems struggle to recognise them as the same species.',
            long_description=(
                'Skathren is a rocky, mineral-rich world bathed in the ultraviolet output '
                'of the binary star -- radiation levels that would cause severe burns and '
                'cellular damage to a baseline human within minutes of unshielded surface '
                'exposure. The planet is uninhabitable by baseline standards. It is home to '
                'three billion people who are not baseline.\n\n'
                'The alien life on Skathren does not survive the radiation. It feeds on it. '
                'The native organisms have evolved photosynthetic pathways that harvest '
                'ultraviolet radiation the way terrestrial plants harvest visible light -- '
                'the ecosystem runs on the energy that would destroy terrestrial biology. '
                'The organisms\' cellular structures include radiation-absorbing pigments '
                'that convert the ultraviolet into metabolic energy, and their DNA repair '
                'mechanisms operate at speeds that make radiation-induced mutation a '
                'manageable metabolic cost rather than a death sentence.\n\n'
                'The colonists spliced these adaptations into themselves. The result is the '
                'Pleiades\' most visibly alien strain. The Skathren population\'s skin has '
                'changed -- the radiation-absorbing pigments have altered the colouration '
                'to deep iridescent blues and violets that shift in the ultraviolet light, '
                'producing a shimmer that baseline eyes perceive as unsettling and that the '
                'Skathren population\'s modified visual range perceives as normal skin '
                'tone. The eyes have adapted to the ultraviolet-dominated light environment '
                '-- the pupils are larger, the irises darker, and the visual processing '
                'extends into wavelengths that baseline humans cannot see. The bone '
                'structure has shifted subtly -- the alien DNA repair mechanisms have '
                'altered the skeletal development in ways the bioengineers did not fully '
                'predict, producing facial structures that are recognisably human in '
                'arrangement but wrong in proportion. The jaw is wider. The brow is '
                'heavier. The symmetry is off in ways that trigger the uncanny response '
                'in baseline observers.\n\n'
                'The mining on Skathren is the system\'s purpose. The mineral deposits are '
                'extensive -- rare elements concentrated by the radiation environment in '
                'formations that the geological surveys describe as exceptional. The miners '
                'work on the surface without radiation shielding because they do not need '
                'it -- the radiation that would kill a baseline worker feeds the miners\' '
                'alien-derived metabolism. The miners work better in the radiation than out '
                'of it. They are slower, weaker, and hungrier in shielded environments '
                'because the radiation-harvesting pigments are not being fed. A Skathren '
                'miner in a shielded habitat is a worker operating on reduced power, and '
                'the trapping is biological: the body needs the radiation the way a '
                'terrestrial body needs sunlight, but at intensities that would sterilise '
                'a terrestrial body.'
            ),
            population=3_000_000_000,
        ),
        StellarObject(
            name='The Underbore',
            short_description='The deep mining complex -- where the radiation does not reach and the miners carry bioluminescent organs that the alien splicing produced as an unintended side effect.',
            long_description=(
                'The Underbore is the deep mining complex beneath Skathren\'s surface -- '
                'bore shafts descending kilometres into the crust, where the radiation '
                'that feeds the surface population does not penetrate and the miners must '
                'work without the energy source their metabolism expects. The deep miners '
                'carry additional splicing -- biological energy storage compounds derived '
                'from the alien organisms\' dormancy adaptations, allowing them to function '
                'underground for extended shifts before returning to the surface to '
                'recharge.\n\n'
                'The unintended side effect of the energy storage splicing is '
                'bioluminescence. The stored energy produces a visible glow in the miners\' '
                'skin -- a soft blue-violet light that intensifies when the energy '
                'reserves are full and dims as the reserves deplete during underground '
                'shifts. The deep miners work in the dark of the bore shafts lit by their '
                'own bodies, moving through tunnels illuminated by the glow of human skin '
                'that is not quite human and that produces light from energy harvested '
                'from radiation that would kill the species the miners used to belong to. '
                'The sight of a deep-mine shift change -- hundreds of glowing figures '
                'ascending from the bore shafts into the ultraviolet surface light -- is '
                'described by the few baseline observers who have witnessed it in terms '
                'that suggest religious experience more than industrial process.'
            ),
            population=0,
        ),
        StellarObject(
            name='Revicane',
            short_description='An orbital station in the radiation shadow -- where the off-world trade is conducted by intermediaries because the Skathren population\'s appearance makes direct commerce with other strains difficult.',
            long_description=(
                'Revicane is an orbital station positioned in the radiation shadow of '
                'Skathren -- shielded from the binary star\'s ultraviolet output by the '
                'planet\'s mass. The station handles the system\'s trade and diplomacy, '
                'conducted by intermediaries because the Skathren population\'s appearance '
                'makes direct face-to-face commerce with other strains complicated. The '
                'deep iridescent skin, the altered facial structure, the eyes that see in '
                'wavelengths the other party cannot perceive -- the visual impact of a '
                'Skathren trade delegation triggers responses in baseline and lightly '
                'spliced humans that are involuntary, uncomfortable, and not conducive to '
                'negotiation.\n\n'
                'The intermediaries are lightly spliced Pleiadians from the diplomatic '
                'class -- modified enough to tolerate the station\'s environment but '
                'baseline enough in appearance to negotiate without triggering the uncanny '
                'response. The Skathren population considers the need for intermediaries '
                'humiliating and practical in equal measure. They are aware that their '
                'appearance disturbs people who have not been modified as they have. They '
                'are also aware that the disturbance is not their problem -- they did not '
                'choose to look this way for aesthetic reasons. They look this way because '
                'the planet required it and the alternative was not colonising the planet.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Vernisk',
            short_description='A shielded residential world -- where the families live in habitats that block the radiation, raising children who will be spliced at adolescence for the surface they cannot yet survive.',
            long_description=(
                'Vernisk is a smaller body in Skathren\'s orbital space that has been '
                'developed as the system\'s shielded residential zone. The habitats on '
                'Vernisk are radiation-shielded -- enclosed communities where the '
                'ultraviolet levels are managed to the range that the population can '
                'tolerate without the full surface intensity. The families live here, and '
                'the children grow up here, in an environment that is reduced from the '
                'surface but still far above baseline safe levels.\n\n'
                'The children are born with the radiation-splicing their parents carry -- '
                'the iridescent skin, the modified eyes, the altered bone structure. But '
                'the children\'s splicing is developmental rather than complete -- the full '
                'radiation-harvesting metabolism activates during adolescence, when the '
                'biological systems mature enough to handle the energy conversion. Before '
                'adolescence, the children can tolerate the residential habitats\' managed '
                'radiation but not the surface. The transition to surface capability is a '
                'coming-of-age milestone -- the adolescent\'s first unshielded surface '
                'walk, when the metabolism activates and the ultraviolet light feeds them '
                'for the first time. The parents describe it as watching their child light '
                'up. The description is literal.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Nocthen',
            short_description='A gas giant whose atmosphere filters the binary star\'s radiation into wavelengths the alien organisms in the cloud layers can use -- a second radiation-fed ecosystem.',
            long_description=(
                'Nocthen is the system\'s gas giant -- notable because the alien life in '
                'its atmosphere has independently evolved the same radiation-harvesting '
                'strategy as Skathren\'s surface organisms. The atmospheric organisms '
                'filter the binary star\'s ultraviolet output through the gas giant\'s '
                'upper layers, converting it into metabolic energy in a parallel ecosystem '
                'that the researchers on Rendeven consider one of the most elegant examples '
                'of convergent alien evolution in the cluster.\n\n'
                'The atmospheric organisms\' gene sequences are being studied for '
                'variations that could improve the Skathren population\'s radiation '
                'harvesting -- the gas giant species have evolved refinements that the '
                'surface species lack, and the cross-referencing of the two lineages may '
                'produce splicing improvements that benefit the mining workforce. The fuel '
                'processing on Nocthen\'s moons operates in the radiation shadow, '
                'shielded for the lightly spliced fuel workers who cannot tolerate the '
                'unshielded environment.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Solvrek',
            short_description='An agricultural station producing food for a population whose metabolism runs on radiation -- the crops photosynthesise in ultraviolet and the food glows faintly on the plate.',
            long_description=(
                'Solvrek is the system\'s agricultural facility -- a large orbital station '
                'and surface installation that produces food for the Skathren population. '
                'The crops are derived from Skathren\'s alien organisms -- plants that '
                'photosynthesise in ultraviolet, grown under the binary star\'s unshielded '
                'output on surface farms that baseline agricultural workers could not '
                'approach. The food produced is compatible with the Skathren strain\'s '
                'modified metabolism and incompatible with most other strains -- the '
                'radiation-derived compounds in the food are nutritious for bodies that '
                'harvest radiation and toxic to bodies that do not.\n\n'
                'The food glows. The radiation-absorbing pigments that the crop organisms '
                'carry are present in the harvested food, producing a faint blue-violet '
                'luminescence that is visible in low light. A meal on Skathren is eaten '
                'under the ultraviolet sky by people whose skin shimmers with the same '
                'pigments, from plates of food that glow faintly with stored radiation. '
                'The aesthetic is beautiful to the Skathren population and deeply '
                'unsettling to the baseline visitors who encounter it on Revicane, where '
                'the diplomatic food service includes the Skathren cuisine as a cultural '
                'offering that most visitors photograph and none eat.'
            ),
            population=300_000_000,
        ),
    ],
    short_description='The radiation world -- five billion people who have become something that feeds on ultraviolet light, mining a world that would kill a baseline human in minutes.',
    long_description=(
        'Asterope is the Pleiades\' most visibly alien inhabited system. The binary '
        'star bathes the system in ultraviolet radiation that would cause severe '
        'burns and cellular damage to a baseline human within minutes. The alien '
        'life on Skathren does not survive the radiation -- it feeds on it, '
        'harvesting ultraviolet the way terrestrial plants harvest visible light. '
        'The colonists spliced these adaptations into themselves and became '
        'something that visitors from other systems struggle to recognise as human.\n\n'
        'The Skathren population\'s skin is deep iridescent blue-violet, shifting '
        'in the ultraviolet light. The eyes see wavelengths baseline humans cannot '
        'perceive. The bone structure has shifted -- wider jaw, heavier brow, '
        'proportions that trigger the uncanny response in baseline observers. The '
        'miners work the surface without radiation shielding because the radiation '
        'feeds them. They are slower and weaker in shielded environments. The '
        'trapping is absolute: the body needs the radiation at intensities that '
        'would sterilise a terrestrial body.\n\n'
        'The deep miners carry bioluminescence as an unintended side effect -- '
        'stored energy producing a blue-violet glow that lights the bore shafts '
        'with human skin that is not quite human. A shift change of hundreds of '
        'glowing figures ascending from the mines into the ultraviolet surface '
        'light is described by observers in terms that suggest religious experience '
        'more than industrial process.\n\n'
        'The food glows on the plate. The children light up at adolescence when '
        'their radiation-harvesting metabolism activates for the first time. The '
        'trade is conducted through intermediaries because the population\'s '
        'appearance makes direct commerce difficult -- not because the Skathren '
        'are hostile but because the involuntary uncanny response in baseline '
        'humans is not conducive to negotiation. Five billion people who have '
        'become something beautiful and alien and trapped, mining a world that '
        'feeds them with light that would kill the species they used to be.'
    ),
    cluster=StarClusters.PLEIADES,
)

ALMACH = System(
    name='Almach',
    star='Orange giant binary (K3II + B9.5V), approximately 2,000 times combined Sol luminosity -- the bright blue companion hidden behind the orange primary, the way the fleet hides in the dark behind the worlds it protects',
    population=4_000_000_000,
    distance_to_sol=350.0,
    stellar_objects=[
        StellarObject(
            name='Kalderen',
            short_description='The fleet world -- two billion people building, crewing, and deploying the ships that are the hardest to detect in the galaxy, crewed by people who no longer need to breathe.',
            long_description=(
                'Kalderen is the Pleiades\' military heart. The planet is partially '
                'terraformed -- breathable with moderate splicing -- and home to the '
                'fleet infrastructure that produces and maintains the warships the '
                'confederation deploys. The Pleiadian fleet is not the largest in the '
                'galaxy. It is not the heaviest or the most heavily armed. It is the '
                'hardest to find, and Kalderen is where the finding becomes impossible.\n\n'
                'The military splicing programme on Kalderen produces crews that do not '
                'need what other crews need. The vacuum-tolerance splicing is the '
                'foundation -- derived from alien organisms on Skathren\'s deep mines '
                'and the pressure-adapted species in the cluster\'s gas giant atmospheres, '
                'the splicing gives the crews\' cells the ability to maintain integrity in '
                'hard vacuum for periods that would kill a baseline human. The crews do '
                'not need pressure suits for short EVA operations. They do not die '
                'immediately in a hull breach. The ships they crew can carry thinner hulls '
                'because the consequence of a breach is discomfort rather than death.\n\n'
                'The radiation tolerance is layered on top -- derived from Asterope\'s '
                'organisms, tuned for the military application rather than the mining '
                'one. The crews tolerate radiation levels that would incapacitate a '
                'baseline crew, which means the ships can reduce their radiation '
                'shielding. The reduced atmospheric requirements mean the ships carry '
                'minimal life support -- the crews breathe an atmospheric mix so thin '
                'and cold that a baseline human would lose consciousness within minutes. '
                'The ships run dark because the crews can function in near-darkness, '
                'their modified eyes adapted for low-light conditions.\n\n'
                'The result is a warship that is cold, dark, thin-hulled, and nearly '
                'invisible. The thermal signature is minimal because there is almost '
                'no heating. The atmospheric signature is minimal because there is '
                'almost no atmosphere. The electromagnetic signature is minimal because '
                'the systems that a normal ship runs -- lighting, climate control, '
                'atmospheric processing -- are absent or reduced to levels that sensors '
                'designed for human-standard vessels cannot reliably detect. A Pleiadian '
                'warship registers on MERIT sensors as debris, as a cold rock, as '
                'nothing. The fleet\'s advantage is not firepower. It is the impossibility '
                'of knowing the fleet is there until it fires.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Gantries',
            short_description='The orbital shipyards -- where the dark ships are built by workers who assemble hulls in vacuum without suits, because the splicing that lets them crew the ships also lets them build them.',
            long_description=(
                'The Gantries are Almach\'s orbital shipyards -- the facilities where the '
                'Pleiadian fleet\'s warships are constructed. The shipyards are unlike any '
                'other construction facility in the galaxy: the workers build the ships in '
                'vacuum. The vacuum-tolerance splicing that the military crews carry is '
                'shared by the construction crews, and the shipyards are unpressurised -- '
                'open frameworks where the workers move through hard vacuum to assemble '
                'the hulls, weld the structures, and install the minimal systems that the '
                'ships carry.\n\n'
                'The efficiency is extraordinary. A conventional shipyard must maintain '
                'pressurised construction bays, atmospheric processing, and the life '
                'support that the construction crews require. The Gantries maintain none of '
                'this. The workers need no pressure suits, no atmospheric supply, and '
                'minimal thermal protection. The construction happens in the same '
                'environment the ships will operate in -- vacuum, cold, and dark. The '
                'workers\' bioluminescent skin accents provide the light they work by, '
                'supplemented by the UV work-lights that their modified eyes can use and '
                'that baseline eyes cannot see.\n\n'
                'The Gantries are invisible from a distance. An unpressurised, unlit '
                'shipyard with no atmospheric signature and minimal thermal output does '
                'not register on sensors the way a conventional shipyard does. MERIT '
                'intelligence knows the Shrouds exist. MERIT intelligence cannot always '
                'find them, because the shipyards are periodically relocated -- moved to '
                'new orbital positions by construction tugs, the frameworks disassembled '
                'and reassembled at coordinates that MERIT\'s surveillance must rediscover. '
                'The fleet builds its ships in the dark, and the dark moves.'
            ),
            population=300_000_000,
        ),
        StellarObject(
            name='Sendrake',
            short_description='The training world -- where the military crews learn to fight in the dark, in the cold, in the vacuum that their bodies can survive and their enemies\' cannot.',
            long_description=(
                'Sendrake is a cold, rocky world used for military training -- the place '
                'where the Pleiadian fleet\'s crews learn the tactics that their biological '
                'advantages enable. The training is unlike any other military programme in '
                'the galaxy because the capabilities are unlike any other military\'s.\n\n'
                'The crews train for vacuum combat -- engagements where the crew operates '
                'in a ship that has been deliberately depressurised to reduce its '
                'signature, fighting in an internal environment that would kill a baseline '
                'crew. The training teaches the crews to function at peak effectiveness in '
                'conditions that their enemies cannot survive, and to exploit the '
                'asymmetry: a boarding action against a Pleiadian ship requires the '
                'boarders to wear pressure suits in the dark while the defenders move '
                'freely in the vacuum, seeing in wavelengths the boarders\' suit helmets '
                'do not transmit.\n\n'
                'The training also covers the fleet\'s signature discipline -- the '
                'protocols that keep the ships invisible. Every system that produces a '
                'detectable emission is trained away. The crews learn to operate without '
                'the lighting, the heating, the atmospheric processing that other fleets '
                'consider essential. The discipline is absolute because the consequence of '
                'failure is detection, and detection eliminates the fleet\'s only advantage. '
                'A Pleiadian warship that is detected is a lightly armed, thinly hulled '
                'vessel that any MERIT frigate can destroy. A Pleiadian warship that is '
                'not detected is the most dangerous ship in the galaxy.'
            ),
            population=400_000_000,
        ),
        StellarObject(
            name='Harkstow',
            short_description='A residential world for the military families -- where the children grow up with parents who are slowly becoming something that belongs to the dark more than the light.',
            long_description=(
                'Harkstow is the system\'s residential world -- a temperate, partially '
                'terraformed planet where the military families live. The communities are '
                'shaped by the particular character of Pleiadian military service: the '
                'parent who deploys is spliced for vacuum, for cold, for darkness. The '
                'parent who returns is the same person with a body that is progressively '
                'more adapted for an environment that the family cannot share.\n\n'
                'The military splicing is cumulative. Each deployment may add adaptations '
                '-- refinements to the vacuum tolerance, deeper radiation resistance, '
                'further reduction in atmospheric requirements. The career soldier who '
                'has served for decades is more deeply modified than the recruit, and the '
                'modifications are visible: the skin tone shifts as the radiation-'
                'absorbing pigments deepen, the eyes adapt further into wavelengths the '
                'family cannot see, and the body temperature drops as the metabolism '
                'adjusts for the cold environment the ships maintain. A veteran who comes '
                'home is cooler to the touch than they were when they left, and the '
                'children notice because children always notice.\n\n'
                'The families adapt because the alternative is a parent who does not '
                'come home. The adjustments are small -- warmer bedding, dimmer lighting '
                'in the house because the veteran\'s eyes are sensitive to brightness, '
                'the understanding that the parent\'s skin feels different now and that '
                'the difference is the cost of the service. The families on Harkstow '
                'carry the knowledge that military service in the Pleiades is not a job '
                'the parent leaves at the door. It is a change in what the parent is, '
                'and the change comes home with them.'
            ),
            population=700_000_000,
        ),
        StellarObject(
            name='Koldrim',
            short_description='A gas giant where the fleet conducts its shakedown exercises -- newly built ships tested in the dark, invisible, by crews learning to be ghosts.',
            long_description=(
                'Koldrim is the system\'s gas giant -- fuel processing on its moons '
                'supporting the military traffic, and the orbital space around the giant '
                'serving as the fleet\'s shakedown and exercise zone. Newly built ships '
                'from the Shrouds are crewed and tested here -- the signature discipline '
                'verified, the stealth capabilities confirmed, the crew\'s ability to '
                'operate in the dark and the cold and the vacuum validated under '
                'operational conditions.\n\n'
                'The exercises are conducted dark -- the ships running without detectable '
                'emissions, the exercise controllers attempting to locate them with the '
                'same sensor systems that MERIT\'s fleet uses. A ship that the controllers '
                'can detect has failed the exercise and the crew is retrained. A ship that '
                'the controllers cannot detect has passed, and the crew is cleared for '
                'deployment. The pass rate is high because the training is thorough. The '
                'standard is absolute because the consequence of detection in combat is '
                'not retraining but destruction.'
            ),
            population=60_000_000,
        ),
        StellarObject(
            name='Selthane',
            short_description='An agricultural world feeding the system -- standard Pleiadian hybrid farming, unremarkable except that the military population\'s splicing requires specific nutritional compounds that the farms must produce.',
            long_description=(
                'Selthane is the system\'s agricultural world -- partially terraformed, '
                'farmed with alien-hybrid crops by a moderately spliced workforce. The '
                'farming is standard by Pleiadian norms but the dietary requirements are '
                'specific -- the military population\'s vacuum-tolerance and radiation-'
                'resistance splicing requires nutritional compounds that the standard '
                'Pleiadian diet does not provide in sufficient quantities. The farms on '
                'Selthane produce supplemental crops -- alien-derived organisms rich in '
                'the compounds the military splicing demands, grown specifically for the '
                'fleet personnel.\n\n'
                'The supplemental crops are another link in the dependency chain. The '
                'military personnel cannot maintain their splicing without the nutritional '
                'compounds. The compounds are produced from organisms that grow on '
                'Selthane and a handful of other worlds. The supply is adequate but '
                'concentrated, and the fleet planners include the supplemental food supply '
                'in their strategic calculations alongside fuel, ammunition, and the '
                'stabilisation compounds from Electra. An army marches on its stomach. A '
                'spliced army marches on a stomach that has been modified to require '
                'things that only specific farms produce.'
            ),
            population=400_000_000,
        ),
    ],
    short_description='The dark fleet -- four billion people building and crewing the ships that nobody can find, in a system where the military advantage is biological and the darkness is the weapon.',
    long_description=(
        'Almach is the Pleiades\' military staging system -- the place where the '
        'fleet that MERIT fears most is built, crewed, and deployed. The Pleiadian '
        'fleet is not the largest or the most heavily armed. It is the hardest to '
        'find. The military splicing programme produces crews that do not need '
        'pressure suits, do not need standard atmospherics, and do not need lighting '
        '-- the ships they crew run cold, dark, and nearly depressurised, producing '
        'thermal, atmospheric, and electromagnetic signatures so minimal that MERIT '
        'sensors designed for human-standard vessels cannot reliably detect them.\n\n'
        'The Gantries build the ships in vacuum -- unpressurised orbital frameworks '
        'where the construction crews work in hard vacuum without suits, their '
        'bioluminescent skin providing the light, invisible from a distance and '
        'periodically relocated so that MERIT surveillance must rediscover them. '
        'Sendrake trains the crews in the tactics the biological advantages enable '
        '-- vacuum combat where the defenders move freely while the boarders wear '
        'pressure suits in the dark, signature discipline so absolute that a single '
        'detectable emission means retraining.\n\n'
        'The binary star\'s orange primary hides the blue companion the way the '
        'fleet hides behind its stealth. Harkstow houses the families of veterans '
        'who come home progressively more adapted for dark and cold and vacuum -- '
        'cooler to the touch, eyes sensitive to brightness, bodies that belong to '
        'the dark more than the light. The children notice because children always '
        'notice.\n\n'
        'A Pleiadian warship that is detected is a lightly armed, thinly hulled '
        'vessel that any MERIT frigate can destroy. A Pleiadian warship that is not '
        'detected is the most dangerous ship in the galaxy. The fleet exists in '
        'the gap between detection and destruction, and Almach exists to ensure '
        'the gap remains wide enough to fight in.'
    ),
    cluster=StarClusters.PLEIADES,
)

ALBIREO = System(
    name='Albireo',
    star='Binary system: gold giant (K2II) and blue dwarf (B8V), approximately 1,200 times combined Sol luminosity -- the most famous colour-contrast binary visible from Earth, casting warm gold and cold blue light that the residents consider a metaphor for everything about their system',
    population=6_000_000_000,
    distance_to_sol=380.0,
    stellar_objects=[
        StellarObject(
            name='Serenden',
            short_description='The most human world in the Pleiades -- four billion people who have spliced only what the environment demands and stopped where the environment permits, in a cluster that considers restraint suspicious.',
            long_description=(
                'Serenden is the Pleiades at its most baseline-compatible. The planet has '
                'been terraformed more thoroughly than any system except Alcyone -- '
                'breathable atmosphere, managed alien biosphere, stable climate engineered '
                'for human comfort rather than human adaptation. The alien life is present '
                'but controlled: domesticated species in the agricultural system, managed '
                'preserves in the wilderness zones, and the decorative alien flora in the '
                'cities that the residents have cultivated for beauty rather than survival.\n\n'
                'The population\'s splicing is minimal. The immune adaptations for the '
                'local pathogens, the minor respiratory adjustments, and nothing more. No '
                'radiation harvesting. No pressure adaptation. No digestive modification '
                'for alien food. The residents of Serenden eat terrestrial crops from '
                'terraformed fields, breathe atmosphere that a baseline human could '
                'tolerate without modification, and maintain bodies that a MERIT physician '
                'would recognise as essentially human with minor notes.\n\n'
                'The restraint is philosophical rather than accidental. Serenden\'s '
                'founding population invested in terraforming rather than splicing -- the '
                'expensive choice, the slow choice, the choice that changes the world '
                'rather than the people. The philosophy has been maintained for centuries: '
                'if the environment can be made safe for humans, make the environment safe. '
                'Do not change the human unless the alternative is not living there at all. '
                'The philosophy is practical rather than ideological -- the residents are '
                'not anti-splicing. They splice when necessary. They consider most of what '
                'the outer worlds call necessary to be a failure of engineering rather than '
                'a requirement of biology.\n\n'
                'The deeply adapted strains regard Serenden with the same mixture of '
                'puzzlement and suspicion that the Hyades directs at Alphard. A population '
                'that chooses not to splice is a population that implicitly questions '
                'whether splicing is the answer, and the question makes the confederation '
                'uncomfortable. The confederation\'s diplomatic class draws heavily from '
                'Serenden\'s population -- baseline-compatible people who can travel '
                'between worlds, breathe multiple atmospheres, and represent the cluster '
                'at the Atrium without requiring a sealed pod. The diplomats from Serenden '
                'are the confederation\'s face, which means the least modified population '
                'represents the most modified civilisation, and nobody discusses the irony.'
            ),
            population=4_000_000_000,
        ),
        StellarObject(
            name='Halvaine',
            short_description='A second terraformed world where the alien life has been integrated as aesthetic rather than functional -- gardens rather than gene banks, beauty rather than survival.',
            long_description=(
                'Halvaine is Albireo\'s second inhabited world -- cooler, smaller, and the '
                'planet where the system\'s relationship with alien life is most visible. '
                'The alien organisms on Halvaine have been cultivated for beauty rather than '
                'utility -- the bioluminescent species that light the gardens at night, the '
                'alien flowering plants that produce colours terrestrial botany cannot '
                'match, and the small alien fauna that fills the ecological niches between '
                'the terrestrial species the terraforming introduced.\n\n'
                'The result is a world where the alien life is decorative rather than '
                'dominant -- present in the way that ornamental plants are present in a '
                'terrestrial garden, adding variety and interest without replacing the '
                'baseline ecosystem. Halvaine\'s parks and wilderness areas are the '
                'Pleiades\' most accessible natural environments for baseline visitors -- '
                'beautiful, alien-accented, and safe to walk through without splicing.\n\n'
                'The tourism is Halvaine\'s contribution to the system\'s economy. The '
                'planet draws visitors from across the cluster -- deeply adapted Pleiadians '
                'who come to see what the alien life looks like when it is not a survival '
                'requirement, and inner-system visitors who want to experience the Pleiades '
                'without the commitment of modification. Halvaine offers the alien beauty '
                'without the alien cost, which is precisely the trade-off that the rest of '
                'the cluster considers a luxury and that Halvaine considers the point.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Spectra Station',
            short_description='The system\'s orbital port -- where the gold and blue light of the binary star produces the colour contrasts that have made the station the most photographed port in the Pleiades.',
            long_description=(
                'Spectra Station is Albireo\'s orbital facility -- a port that handles '
                'the system\'s traffic and that has become, unintentionally, one of the '
                'most visited destinations in the cluster. The binary star\'s gold-and-blue '
                'light produces colour contrasts on the station\'s surfaces that shift as '
                'the stars orbit -- warm gold tones from the K-type primary, cold blue '
                'accents from the B-type companion, and the mixed light between that '
                'produces colours the residents call the between-light and that visitors '
                'call extraordinary.\n\n'
                'The station\'s designers incorporated the colour contrasts into the '
                'architecture -- surfaces angled to catch the gold and blue at different '
                'times, public spaces that shift from warm to cool as the binary pair '
                'orbits, and the observation galleries where the visitors can watch the '
                'two stars side by side. The station is the most photographed port in the '
                'Pleiades, which the station\'s management considers a mixed blessing -- '
                'the tourism revenue is welcome, the congestion is not.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='The Academy',
            short_description='The diplomatic training facility -- where the confederation\'s representatives are prepared for the work of negotiating between populations that are becoming different species.',
            long_description=(
                'The Academy is an orbital facility above Serenden that trains the '
                'confederation\'s diplomatic class. The training is unique in the galaxy -- '
                'the diplomats must learn to represent populations they cannot physically '
                'visit, to negotiate between strains whose biology they do not share, and '
                'to communicate across the sensory and cognitive differences that the '
                'various strains\' splicing has produced.\n\n'
                'The curriculum includes biological immersion -- the diplomats undergo '
                'simulated exposure to the conditions the outer-world strains experience, '
                'using controlled environments that replicate the radiation levels, the '
                'atmospheric compositions, and the gravitational conditions that the '
                'strains live in. The exposure is brief and carefully managed, but it '
                'produces an understanding that briefing documents cannot: the physical '
                'experience of what it feels like to need the atmosphere your strain '
                'breathes and to be in an atmosphere that is not quite right. The '
                'diplomats carry this understanding into their work, and the deeply '
                'adapted populations who receive them can tell the difference between a '
                'diplomat who has been through the Academy\'s immersion and one who has '
                'only read the briefings.\n\n'
                'The Academy also teaches the language of biological diplomacy -- the '
                'terminology, the protocols, and the sensitivity required to negotiate '
                'with populations whose bodies are their identity in a way that baseline '
                'humans find difficult to understand. A strain\'s modifications are not '
                'accessories. They are what the strain is. The diplomatic language must '
                'reflect this, and the Academy exists to ensure that it does.'
            ),
            population=50_000_000,
        ),
        StellarObject(
            name='Vedren',
            short_description='A gas giant bathed in the binary\'s contrasting light -- fuel processing and alien atmospheric organisms whose bioluminescence responds to the gold and blue wavelengths alternately.',
            long_description=(
                'Vedren is the system\'s gas giant -- fuel processing on its moons '
                'supporting the traffic that Albireo\'s tourism and diplomatic function '
                'generates. The alien organisms in Vedren\'s atmosphere have evolved a '
                'bioluminescent response to the binary star\'s alternating light -- the '
                'organisms glow gold when the K-type primary dominates and shift to blue '
                'when the B-type companion\'s light is stronger. The alternation produces '
                'a slow pulse of colour in the gas giant\'s upper atmosphere that the '
                'observation galleries on Spectra Station face directly.\n\n'
                'The organisms are studied but not harvested -- the research community '
                'considers them more valuable as an intact example of alien bioluminescent '
                'adaptation than as a source of extractable compounds. The restraint '
                'mirrors the system\'s broader philosophy: use what you must, preserve '
                'what you can, and do not consume something beautiful to make something '
                'merely useful.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='Thursten',
            short_description='An agricultural world growing terrestrial crops on terraformed soil -- one of the few places in the Pleiades where the food is recognisable to a baseline human.',
            long_description=(
                'Thursten is the system\'s agricultural world -- terraformed soil, '
                'terrestrial crops, baseline-compatible food. The farming on Thursten '
                'resembles farming in the inner systems more than farming anywhere else '
                'in the Pleiades -- the crops are recognisable, the livestock are '
                'terrestrial, and the food is edible by any human regardless of '
                'modification level. The output feeds Albireo\'s population and exports '
                'the baseline-compatible food that the diplomatic class across the cluster '
                'requires.\n\n'
                'Thursten\'s farmers are the most conventional agricultural workers in the '
                'Pleiades -- minimally spliced, working terrestrial soil with terrestrial '
                'methods, producing food that does not glow, does not require modified '
                'taste receptors to appreciate, and does not need a strain-compatibility '
                'check before serving. The farmers consider this unremarkable. The visitors '
                'from the outer systems consider it extraordinary. A plate of food that '
                'looks like food, on a world that looks like a world, is the rarest '
                'experience the Pleiades offers.'
            ),
            population=600_000_000,
        ),
    ],
    short_description='The human world -- six billion people in the system that chose to terraform rather than splice, where the alien life is beautiful rather than necessary and the diplomats who represent the cluster are the least modified people in it.',
    long_description=(
        'Albireo is the Pleiades\' most human system -- the world that chose '
        'terraforming over splicing, the expensive choice that changes the planet '
        'rather than the people. Six billion people live here with modifications '
        'so minimal that a MERIT physician would recognise them as essentially '
        'baseline. They eat terrestrial food, breathe engineered atmosphere, and '
        'maintain bodies that the deeply adapted strains consider a luxury and '
        'that Serenden\'s residents consider the point.\n\n'
        'The binary star -- the famous gold-and-blue colour-contrast pair visible '
        'from Earth -- casts light that shifts between warm and cool as the stars '
        'orbit. The residents consider it a metaphor: the gold of terrestrial '
        'humanity and the blue of alien biology, neither dominant, coexisting. The '
        'alien life on Halvaine is cultivated for beauty rather than survival -- '
        'bioluminescent gardens, ornamental alien flora, the accessible alien '
        'experience without the alien cost.\n\n'
        'The confederation\'s diplomatic class draws heavily from Serenden -- '
        'baseline-compatible people who can travel between worlds and represent '
        'the cluster without requiring sealed pods. The Academy trains them for '
        'the work of negotiating between populations whose biology they do not '
        'share, including simulated exposure to the conditions the outer strains '
        'live in. The deeply adapted populations can tell the difference between '
        'a diplomat who has been through the immersion and one who has only read '
        'the briefings.\n\n'
        'The irony the system lives with: the least modified population represents '
        'the most modified civilisation. The face the Pleiades shows the galaxy -- '
        'at the Atrium, at Alcyone\'s gateway, in the negotiations that hold the '
        'confederation together -- belongs to people who look the most like the '
        'species the Pleiades is leaving behind. Albireo is the human world in a '
        'cluster that is becoming something else, and the question it raises is '
        'whether that makes it the most important system or the most irrelevant.'
    ),
    cluster=StarClusters.PLEIADES,
)

SPICA = System(
    name='Spica',
    star='Blue-white main sequence binary (B1III + B2V), approximately 12,000 times combined Sol luminosity -- two massive blue stars in a close, violent orbit, illuminating a system where the predators are human and the prey cannot follow them home',
    population=3_000_000_000,
    distance_to_sol=250.0,
    stellar_objects=[
        StellarObject(
            name='Skelvane',
            short_description='The cluster\'s pirate capital -- a billion people on a world whose atmosphere is a weapon, spliced to survive conditions their victims cannot follow them into.',
            long_description=(
                'Skelvane is a world that should not be inhabited. The atmosphere is a '
                'dense, toxic cocktail of compounds that would kill a baseline human in '
                'minutes -- hydrogen sulphide concentrations high enough to overwhelm any '
                'standard filtration system, corrosive acidic compounds that attack '
                'unprotected equipment, and a surface pressure fifty percent above standard '
                'that compounds every other hazard. The alien life on Skelvane thrives in '
                'this -- the native organisms have evolved to metabolise the toxic '
                'compounds, to breathe the corrosive atmosphere, and to function at '
                'pressures that would incapacitate a baseline human.\n\n'
                'The population of Skelvane is spliced with these organisms\' adaptations. '
                'The splicing is aggressive, extensive, and deliberately chosen for its '
                'defensive properties. The residents breathe the toxic atmosphere without '
                'filtration. Their skin resists the corrosive compounds. Their bodies '
                'function at the elevated pressure. The modifications make them capable of '
                'living on Skelvane, which is their home. The modifications also make '
                'Skelvane a fortress, because nobody who has not been spliced for the '
                'environment can survive on the surface.\n\n'
                'The raiding is the system\'s economy. The pirates of Spica operate from '
                'Skelvane with a tactical advantage that no other pirate faction in the '
                'galaxy possesses: they can retreat into an atmosphere that kills their '
                'pursuers. A raiding party that is intercepted does not fight to the '
                'death. It runs for Skelvane\'s atmosphere and descends. The pursuit must '
                'stop at the atmospheric boundary because the pursuit\'s crew cannot '
                'survive below it. The raiders land, wait for the pursuit to withdraw, '
                'and launch again when the approach is clear.\n\n'
                'The raider crews are among the most aggressively spliced people in the '
                'cluster. The atmospheric adaptations are the foundation, but the raiding '
                'crews carry additional combat splicing -- enhanced reflexes derived from '
                'Skelvane\'s alien predators, accelerated healing from the native '
                'organisms\' regenerative biology, and the sensory enhancements that let '
                'them operate in the dense, murky atmosphere where visibility is measured '
                'in metres. The raiders are adapted for their world the way the Taygetan '
                'workers are adapted for theirs. The difference is that the Taygetans '
                'adapted to work. The Skelvanites adapted to hunt.'
            ),
            population=1_000_000_000,
        ),
        StellarObject(
            name='The Miasma',
            short_description='The atmospheric zone above Skelvane where the toxic compounds thin enough for ships to operate but thick enough to corrode unprotected hulls -- the raiding fleet\'s staging area.',
            long_description=(
                'The Miasma is the atmospheric transition zone above Skelvane -- the band '
                'of altitude where the toxic compounds are thin enough that ships can '
                'operate but concentrated enough that unprotected hulls begin to corrode '
                'within hours. The raider fleet stages in the Miasma -- the ships\' hulls '
                'are treated with compounds derived from the alien organisms\' corrosion-'
                'resistant biology, giving them a surface that the atmosphere does not '
                'attack. Pursuing ships that enter the Miasma without this treatment find '
                'their hulls degrading, their sensors blinded by the atmospheric '
                'interference, and their crews breathing air that the filtration systems '
                'are losing the fight to keep clean.\n\n'
                'The Miasma is the raiders\' killing ground. A merchant ship that is '
                'pursued into the Miasma by its own escort finds that the escort\'s '
                'equipment degrades faster than the raiders\'. The raiders know the '
                'atmospheric layers -- which altitudes are survivable for unprotected '
                'ships and which are not, where the corrosive pockets concentrate, and '
                'the tactics of using the atmosphere as a weapon. A raider crew that '
                'lures a pursuing frigate into a corrosive pocket and watches the hull '
                'begin to pit is using a weapon the frigate cannot shoot back at.'
            ),
            population=0,
        ),
        StellarObject(
            name='Rothen',
            short_description='An orbital market above the Miasma -- where the stolen cargo is traded and the buyers dock at a station whose lower levels are already being eaten by the atmosphere below.',
            long_description=(
                'Rothen is Spica\'s orbital station -- positioned above the Miasma at an '
                'altitude where the atmospheric corrosion is manageable but not absent. '
                'The station\'s lower levels show the effects: pitting on the hull plating, '
                'corrosion on the external fittings, and the constant maintenance cycle '
                'that the station\'s crews perform to keep the structure sound. The station '
                'is functional rather than comfortable, and the decay is part of the '
                'aesthetic -- a trading venue that is slowly being consumed by the '
                'atmosphere of the world it orbits.\n\n'
                'The trade on Rothen is stolen goods -- cargo taken from raided ships, '
                'sold to buyers who dock at the station and try not to stay long enough '
                'for the corrosion to damage their ships. The transactions are fast. The '
                'buyers come with credits, leave with cargo, and depart before the '
                'atmospheric compounds begin working on their hull seals. The raiders '
                'who sell the goods are comfortable -- their ships are treated, their '
                'bodies are adapted, and the corrosion that makes their buyers nervous '
                'is the same corrosion that protects them from the navies that would '
                'shut the market down if the navies could survive in the atmosphere long '
                'enough to try.\n\n'
                'The confederation has considered pacifying Spica and has calculated the '
                'cost of operating a fleet in an atmosphere that corrodes the hulls. The '
                'calculation produced the same result every time: the losses from piracy '
                'are cheaper than the cost of the operation. The raiders continue. The '
                'atmosphere protects them. The buyers come and go quickly. The station '
                'corrodes.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Carroden',
            short_description='A second world with a less extreme atmosphere -- where the pirate population that cannot tolerate Skelvane\'s full toxicity lives, and where the raider crews\' families are raised.',
            long_description=(
                'Carroden is a second habitable world in the system -- smaller, with an '
                'atmosphere that is toxic by baseline standards but significantly less '
                'extreme than Skelvane\'s. The atmospheric compounds are present but at '
                'lower concentrations, and the splicing required to survive on Carroden is '
                'less aggressive than Skelvane\'s full combat package. The population '
                'includes the raider crews\' families, the support staff who maintain the '
                'raiding infrastructure, and the people who chose piracy as a life but not '
                'the full commitment of Skelvane\'s extreme adaptation.\n\n'
                'The children on Carroden grow up with the lesser splicing and the '
                'knowledge that full adaptation to Skelvane is a choice they will face in '
                'adolescence. The raiding crews recruit from Carroden\'s young adults -- '
                'the ones who choose the deeper splicing, the combat modifications, and '
                'the life on a world that will trap them as surely as Taygeta\'s gravity '
                'traps its workers. The ones who choose not to remain on Carroden and do '
                'the support work that the raiding economy requires. The choice is real. '
                'The pressure is also real. The raider crews have status. The support '
                'staff do not. In a pirate system, the hierarchy runs on who is willing '
                'to become the most alien.'
            ),
            population=800_000_000,
        ),
        StellarObject(
            name='Nelvask',
            short_description='A gas giant whose atmosphere contains the same corrosive compounds as Skelvane\'s -- the fuel processing requires the same anti-corrosion treatments the raider fleet uses.',
            long_description=(
                'Nelvask is the system\'s gas giant -- fuel processing on its moons, with '
                'the complication that the gas giant\'s atmosphere shares some of the '
                'corrosive compounds that define Skelvane\'s environment. The fuel '
                'processing equipment requires the same anti-corrosion treatments that the '
                'raider fleet\'s hulls carry, which makes the fuel operations more '
                'expensive and more specialised than standard. The fuel workers are lightly '
                'spliced for the corrosive trace compounds in the processing environment.\n\n'
                'The shared chemistry between the gas giant and the habitable world '
                'suggests a common origin -- the system\'s formation left corrosive '
                'compounds distributed through the inner and outer bodies. The researchers '
                'on Rendeven find the chemistry interesting. The raiders find it convenient '
                '-- the same compounds that make their world a fortress also make the '
                'fuel processing inaccessible to anyone without the treatment, adding '
                'another layer to the system\'s natural defences.'
            ),
            population=40_000_000,
        ),
        StellarObject(
            name='The Stench',
            short_description='The system\'s agricultural operation -- alien crops grown in the toxic atmosphere, producing food that smells the way the atmosphere does and that only Skelvane\'s strain can stomach.',
            long_description=(
                'The Stench is Spica\'s agricultural operation -- surface farms on '
                'Skelvane and orbital processing above Carroden, producing food from the '
                'alien organisms that thrive in the toxic atmosphere. The food is derived '
                'from the same organisms whose genes the population carries -- crops that '
                'metabolise the hydrogen sulphide and corrosive compounds, producing '
                'nutrition that is compatible with the Skelvane strain\'s modified '
                'digestive system and that smells, to a baseline nose, like the atmosphere '
                'it grew in.\n\n'
                'The name is not official but it is universal. The food from Spica\'s '
                'farms smells of sulphur, of acid, of the toxic compounds that the '
                'organisms have absorbed and partially metabolised. The Skelvane '
                'population does not notice the smell -- their modified olfactory systems '
                'register the compounds as neutral rather than offensive. Visitors to '
                'Rothen who encounter the food describe the experience as the most '
                'convincing argument against piracy they have ever encountered. The '
                'raiders find this funny.'
            ),
            population=200_000_000,
        ),
    ],
    short_description='The predators -- three billion people on a toxic world that serves as both home and fortress, raiding from an atmosphere their pursuers cannot survive.',
    long_description=(
        'Spica is the Pleiades\' pirate system -- a toxic world orbiting a violent '
        'binary star, inhabited by a population spliced to survive an atmosphere '
        'that kills baseline humans in minutes. The piracy is built on the biology: '
        'the raiders operate from Skelvane, retreat into the toxic atmosphere when '
        'pursued, and wait for the pursuit to withdraw because the pursuit\'s crews '
        'cannot survive below the atmospheric boundary. The atmosphere is the weapon. '
        'The splicing is the armour. The combination produces the only pirate '
        'faction in the galaxy that is functionally immune to conventional pursuit.\n\n'
        'The Miasma -- the atmospheric transition zone -- is the killing ground. '
        'Raider ships with corrosion-treated hulls operate freely in the acidic '
        'atmosphere that degrades pursuing ships\' equipment within hours. The '
        'raiders know the atmospheric layers the way a hunter knows terrain, using '
        'corrosive pockets as weapons the enemy cannot shoot back at. Rothen '
        'station trades the stolen goods above the Miasma, its lower levels already '
        'being eaten by the atmosphere below.\n\n'
        'The raider crews carry the most aggressive combat splicing in the cluster '
        '-- the atmospheric adaptations plus enhanced reflexes from Skelvane\'s '
        'predators, accelerated healing, and the sensory enhancements for operating '
        'in an atmosphere where visibility is measured in metres. The hierarchy runs '
        'on who is willing to become the most alien: the full Skelvane adaptation '
        'versus Carroden\'s lesser modification, raider crew versus support staff.\n\n'
        'The confederation has calculated the cost of pacifying Spica -- operating '
        'a fleet in an atmosphere that corrodes the hulls -- and concluded that the '
        'piracy losses are cheaper than the operation. The food smells like the '
        'atmosphere. The raiders find this funny. The three billion people on a '
        'world that is both prison and fortress have built an economy on the '
        'simple fact that their home is a place nobody else can go.'
    ),
    cluster=StarClusters.PLEIADES,
)

ELECTRA = System(
    name='Electra',
    star='Blue-white giant (B6III), approximately 1,400 times Sol luminosity -- a hot, bright star at the end of a four-jump chain, illuminating a world whose biology keeps the cluster alive and whose people have never seen the cluster they sustain',
    population=3_000_000_000,
    distance_to_sol=600.0,
    stellar_objects=[
        StellarObject(
            name='Sathren',
            short_description='The world the cluster depends on -- two billion people so deeply spliced with the local alien biosphere that they have become part of it, producing the compounds that prevent every other strain from falling apart.',
            long_description=(
                'Sathren is the most important world in the Pleiades and the least '
                'accessible. The planet hosts an alien biosphere of extraordinary '
                'complexity -- an ecosystem that has evolved over billions of years in '
                'isolation, producing organisms with biochemical properties found nowhere '
                'else in the galaxy. The stabilisation compounds that prevent cumulative '
                'gene-splicing from cascading into genetic instability are derived from '
                'organisms that live only on Sathren, in symbiotic relationships with '
                'other organisms that live only on Sathren, in soil chemistry that exists '
                'only on Sathren. The compounds cannot be fully synthesised. The organisms '
                'cannot be transplanted. The biochemistry is dependent on a web of '
                'ecological relationships so complex that removing any element degrades '
                'the output.\n\n'
                'The population of Sathren is the most deeply spliced strain in the '
                'Pleiades. The colonists who arrived generations ago needed extensive '
                'modification to survive the alien biosphere -- immune systems rebuilt '
                'from the ground up to tolerate the local pathogens, respiratory systems '
                'adapted for an atmosphere rich in compounds that would destroy baseline '
                'lung tissue, digestive systems reconfigured for the alien food chain that '
                'is the only food source on a world that has never been terraformed. The '
                'modifications went further. The population is spliced with the same '
                'organisms whose compounds they harvest -- a symbiotic integration that '
                'lets the harvesters detect the organisms, understand their biochemical '
                'cycles, and collect the compounds at the precise stage of the organisms\' '
                'metabolism when the stabilisation properties are at their peak.\n\n'
                'The integration has continued for generations. The Sathren population is '
                'no longer human in any way that a baseline observer would recognise at '
                'first glance. The skin has taken on the texture and colouration of the '
                'alien organisms they are symbiotic with -- mottled patterns that shift '
                'with the body\'s biochemical state, producing a living display that the '
                'population reads the way baseline humans read facial expressions. The '
                'sensory adaptations are extreme: olfactory systems that detect individual '
                'compounds in parts per billion, tactile sensitivity that can feel the '
                'metabolic pulse of the organisms they harvest, and a proprioceptive '
                'awareness of the local ecosystem that the researchers on Rendeven '
                'describe as environmental empathy and that the Sathren population '
                'describes as knowing where things are.\n\n'
                'The trapping is total. The Sathren population cannot leave their world '
                'for any meaningful duration. The symbiotic organisms integrated into '
                'their biology require the local ecosystem to sustain them -- separated '
                'from Sathren\'s biosphere, the symbiotes begin to die within days, and '
                'the host\'s biology, now dependent on the symbiotes\' metabolic '
                'contributions, destabilises. A Sathren citizen who leaves the planet '
                'begins to sicken within a week and faces organ failure within a month '
                'without intervention. The people who produce the compounds that keep the '
                'cluster stable are themselves the most unstable population in the '
                'Pleiades -- the most dependent on their specific world, the most trapped, '
                'and the most essential.'
            ),
            population=2_000_000_000,
        ),
        StellarObject(
            name='The Canopy',
            short_description='The vast alien forest ecosystem that produces the stabilisation compounds -- a living infrastructure so complex that the population tends it rather than manages it.',
            long_description=(
                'The Canopy is the name for the dominant ecosystem on Sathren -- a vast '
                'alien forest that covers sixty percent of the planet\'s landmass and that '
                'produces the organisms from which the stabilisation compounds are derived. '
                'The forest is not terrestrial in any recognisable sense. The structures '
                'that function as trees are interconnected -- root systems that form a '
                'single network spanning thousands of kilometres, canopy organisms that '
                'share nutrients and chemical signals across the forest\'s extent, and the '
                'smaller organisms that live in the network\'s interstices and that produce '
                'the compounds the cluster needs.\n\n'
                'The compound-producing organisms are not the forest\'s primary species. '
                'They are symbiotes of symbiotes -- small organisms that live on the root '
                'network\'s surface, feeding on the chemical outputs of the network\'s '
                'metabolism, and producing stabilisation compounds as a metabolic byproduct '
                'of a relationship that involves at least seven other species in a chain '
                'that the biologists have mapped but do not fully understand. Removing any '
                'species in the chain degrades the compound production. The compounds '
                'cannot be produced without the chain. The chain cannot be maintained '
                'without the forest. The forest cannot be transplanted.\n\n'
                'The Sathren population tends the Canopy the way a caretaker tends a '
                'cathedral -- with reverence, attention, and the understanding that the '
                'structure is more important than the caretaker. The harvesting is careful: '
                'the compound-producing organisms are collected at specific points in their '
                'metabolic cycle, in quantities that the forest\'s reproductive capacity '
                'can replace, on schedules calibrated to the forest\'s seasonal rhythms. '
                'Over-harvesting has been attempted once, during a supply crisis three '
                'centuries ago. The forest\'s compound production dropped for a decade. '
                'The lesson was learned. The forest sets the pace. The cluster waits.'
            ),
            population=0,
        ),
        StellarObject(
            name='Kolvander Station',
            short_description='The orbital facility where the compounds are processed and loaded for the four-jump transit to Maia -- the bottleneck through which the cluster\'s stability flows.',
            long_description=(
                'Kolvander Station is Electra\'s primary orbital facility -- the place '
                'where the stabilisation compounds harvested from the Canopy are processed, '
                'packaged in climate-controlled containers, and loaded onto the freighters '
                'that carry them along the four-jump route to Maia. The station is the '
                'bottleneck: every compound shipment that sustains the cluster\'s gene-'
                'splicing stability passes through Kolvander before beginning the transit '
                'through PLX-9902, PLX-9901, and on to Dispatch Station at Maia.\n\n'
                'The station is staffed by two populations that cannot interact directly. '
                'The Sathren workers who process the compounds operate in the station\'s '
                'Sathren-atmosphere sections -- sealed environments that replicate the '
                'planet\'s atmospheric composition and that the non-Sathren staff cannot '
                'enter without sealed suits. The transit crew who operate the freighters '
                'are lightly spliced Pleiadians from the diplomatic strain -- the only '
                'people who can crew the ships and survive the four-jump route. The '
                'compound containers pass through airlocks between the two sections, '
                'handled by Sathren workers on one side and transit crew on the other, '
                'the two populations conducting the most important logistics operation in '
                'the cluster through a wall they cannot open.\n\n'
                'The station maintains a garrison -- a small fleet of Pleiadian warships '
                'assigned to protect the supply chain\'s origin. The garrison is the most '
                'remote military posting in the Pleiades, four jumps from the nearest '
                'inhabited system, and the crews serve rotations that the fleet considers '
                'hardship postings. The garrison\'s purpose is to ensure that the compound '
                'shipments depart on schedule. Nothing else in the system matters as much '
                'as the schedule.'
            ),
            population=100_000_000,
        ),
        StellarObject(
            name='Althesk',
            short_description='A second world with its own alien biosphere -- being studied for alternative stabilisation sources that could reduce the cluster\'s dependency on a single ecosystem.',
            long_description=(
                'Althesk is Electra\'s second habitable world -- smaller than Sathren, '
                'with its own distinct alien biosphere that has evolved independently in '
                'the same system. The biosphere on Althesk does not produce stabilisation '
                'compounds, but the researchers stationed here are studying whether the '
                'organisms\' biochemistry includes pathways that could be developed into '
                'alternative sources.\n\n'
                'The research is the confederation\'s longest-running contingency programme '
                '-- the effort to find a second source of stabilisation compounds that '
                'does not depend on the Canopy\'s fragile symbiotic chain. The programme '
                'has been running for over a century. The results are promising in the way '
                'that research results are promising when the researchers need more funding '
                '-- the organisms on Althesk produce compounds with some of the '
                'stabilisation properties but not all, and the gap between some and all '
                'is the gap the programme has been trying to close for decades.\n\n'
                'The research staff on Althesk are lightly spliced for the local '
                'conditions -- the biosphere is less extreme than Sathren\'s and the '
                'atmosphere is closer to manageable. The staff can rotate off Althesk '
                'without the symbiotic dependency that traps the Sathren population. They '
                'are aware that they are working to solve a problem that would free three '
                'billion people from a world they cannot leave, and that the problem has '
                'resisted a century of effort by the cluster\'s best biologists.'
            ),
            population=200_000_000,
        ),
        StellarObject(
            name='Oskelan',
            short_description='A gas giant with fuel processing for the route traffic -- the only fuel source between PLX-9902 and Electra, making it as critical as the compounds it helps transport.',
            long_description=(
                'Oskelan is the system\'s gas giant -- fuel processing on its moons '
                'supporting the freighter traffic that carries the stabilisation compounds '
                'to Maia. The fuel operations are critical because Oskelan is the only fuel '
                'source between PLX-9902 and Electra -- the freighters that carry the '
                'compounds must refuel here before the return transit, and a disruption in '
                'Oskelan\'s fuel processing would strand the freighters and interrupt the '
                'compound supply as effectively as an attack on the Canopy itself.\n\n'
                'The fuel workers carry light splicing and serve rotations that are counted '
                'as hardship postings -- four jumps from the nearest inhabited system, on '
                'moons orbiting a gas giant in a system that most of the cluster has never '
                'visited. The workers describe the posting as quiet, important, and lonely '
                'in a specific way: the loneliness of knowing that the nearest help, if '
                'anything goes wrong, is weeks away through three jump points and that the '
                'help cannot arrive faster regardless of the emergency.'
            ),
            population=30_000_000,
        ),
        StellarObject(
            name='Farshen',
            short_description='A frozen outer body -- the most remote inhabited point in the Pleiades, hosting a long-range communications relay that keeps Electra connected to a cluster it cannot visit.',
            long_description=(
                'Farshen is a frozen body in the far outer system -- hosting the long-range '
                'communications relay that keeps Electra connected to the rest of the '
                'cluster. The relay is essential because the four-jump distance introduces '
                'communication lag that the compound logistics cannot tolerate -- the '
                'schedule coordination between Kolvander Station and Dispatch Station at '
                'Maia requires real-time data that the jump-point relay network provides.\n\n'
                'The relay staff are the most remote permanent inhabitants in the Pleiades '
                '-- further from the cluster\'s core than anyone except the survey teams on '
                'the frontier. The staff maintain the equipment, monitor the signal, and '
                'live with the knowledge that the data flowing through their relay is the '
                'scheduling information that keeps the compound supply on track. A relay '
                'failure would not stop the shipments -- the freighters would continue on '
                'their established schedule -- but it would blind the logistics '
                'coordinators on Maia to any disruption at the source, and the time it '
                'would take to discover that something had gone wrong at Electra would be '
                'measured in the weeks it takes a ship to make the four-jump transit.'
            ),
            population=5_000_000,
        ),
    ],
    short_description='The source -- three billion people at the end of a four-jump chain, so deeply spliced with the local alien biosphere that they cannot leave the world whose compounds keep the cluster alive.',
    long_description=(
        'Electra is the most important system in the Pleiades and the hardest to '
        'reach. Four jumps from Maia -- Maia to PLX-9901 to PLX-9902 to Electra -- '
        'at the end of a chain that is the cluster\'s jugular. The system contains '
        'Sathren, a world with an alien biosphere of extraordinary complexity whose '
        'organisms produce the stabilisation compounds that prevent cumulative gene-'
        'splicing from cascading into genetic instability. The compounds cannot be '
        'fully synthesised. The organisms cannot be transplanted. The biochemistry '
        'depends on a symbiotic chain of at least seven species in a forest that '
        'covers sixty percent of the landmass.\n\n'
        'The Sathren population is the most deeply spliced strain in the Pleiades '
        '-- modified over generations into symbiotic integration with the organisms '
        'they harvest. The skin displays the body\'s biochemical state. The senses '
        'detect individual compounds in parts per billion. The population reads its '
        'ecosystem the way baseline humans read faces. The trapping is total: the '
        'symbiotic organisms integrated into their biology require the local '
        'ecosystem. Separated from Sathren, the symbiotes die within days and the '
        'host destabilises. A Sathren citizen who leaves sickens within a week and '
        'faces organ failure within a month.\n\n'
        'The people who keep the cluster alive have never seen the cluster. They '
        'cannot travel to the worlds their compounds sustain. They cannot visit the '
        'strains whose stability they maintain. They tend the Canopy -- the vast '
        'alien forest -- with the care of people who understand that the forest is '
        'more important than the caretaker, harvesting at the pace the forest sets '
        'because over-harvesting was tried once and the production dropped for a '
        'decade.\n\n'
        'Althesk\'s research programme has been searching for an alternative source '
        'for over a century. The results are promising in the way that research '
        'needing more funding is always promising. The gap between some of the '
        'stabilisation properties and all of them has resisted the cluster\'s best '
        'biologists for decades. Three billion people at the end of the longest '
        'supply chain in the Pleiades, trapped on a world they sustain and that '
        'sustains them, producing the compounds that hold a civilisation together '
        'from a place the civilisation cannot reach without weeks of transit and '
        'four jumps through systems that a single disruption could close.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_0010 = System(
    name='PLX-0010',
    star='Orange dwarf (K4V), approximately 0.2 times Sol luminosity -- a dim, stable star that nobody would visit if it were not sitting at the junction of every route that matters',
    population=0,
    distance_to_sol=410.0,
    stellar_objects=[
        StellarObject(
            name='PLX-0010-a',
            short_description='A rocky world with no atmosphere and no value except its position -- the junction where the cluster\'s major trade routes converge and the busiest uninhabited system in the Pleiades.',
            long_description=(
                'PLX-0010-a is a small, airless rock that would not merit a footnote in any '
                'survey catalogue if it were not orbiting a star that happens to sit at the '
                'convergence of the jump links connecting the cluster\'s most important '
                'systems. The routes from Alcyone to the inner cluster, from Maia to the '
                'trade systems, from Mirach to the outer worlds -- they all pass through '
                'PLX-0010. The system has no resources, no habitable worlds, and no reason '
                'to exist except geometry.\n\n'
                'The surface of PLX-0010-a hosts fuel depots, communications relays, and '
                'the navigational beacons that the traffic requires. The installations are '
                'automated and maintained by rotating crews who serve short postings and '
                'leave without forming attachments to a world that offers nothing to attach '
                'to. The crews describe the posting as boring in a way that involves a lot '
                'of ships -- the traffic through PLX-0010 is the heaviest of any '
                'uninhabited system in the cluster, and the crews watch the freighters, '
                'the warships, the diplomatic transports, and the trade vessels pass '
                'through without stopping because nobody stops at PLX-0010 unless they '
                'need fuel.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-0010-b',
            short_description='A frozen outer body hosting the system\'s largest fuel depot -- the refuelling stop that keeps the trade routes functional.',
            long_description=(
                'PLX-0010-b is a frozen body in the outer system that hosts the junction\'s '
                'primary fuel depot. The depot is large by uninhabited-system standards -- '
                'sized for the traffic volume that the junction generates, with storage '
                'capacity and processing equipment that a system with actual inhabitants '
                'would consider respectable. The fuel is processed from imported feedstock '
                'rather than local sources -- the system has no gas giant, and the fuel '
                'must be brought in from neighbouring systems and stored for the traffic '
                'that passes through.\n\n'
                'The absence of a local fuel source is PLX-0010\'s vulnerability. The depot '
                'depends on regular resupply, and a disruption in the resupply would '
                'bottleneck the trade routes within weeks. The confederation maintains the '
                'resupply as a strategic priority -- the fuel convoys to PLX-0010 are '
                'scheduled with the reliability that the cluster\'s commerce demands, and '
                'the convoys are escorted because a pirate attack on a PLX-0010 fuel '
                'convoy would be an attack on every trade route in the cluster '
                'simultaneously.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-0010-c',
            short_description='A small rocky body hosting the communications relay hub -- the node through which the cluster\'s inter-system data traffic is routed.',
            long_description=(
                'PLX-0010-c is a small rocky body that hosts the junction\'s communications '
                'relay hub -- the node through which the cluster\'s inter-system data '
                'traffic is routed. The relay handles the coordination signals for the '
                'trade routes, the military communications that the fleet encrypts through '
                'the junction, and the civilian data traffic that the cluster\'s population '
                'generates. The relay is the most important piece of communications '
                'infrastructure in the Pleiades outside of Electra\'s Farshen relay, and '
                'the maintenance crew treats it accordingly -- redundant systems, backup '
                'power, and the monitoring that ensures the signal never drops because a '
                'signal drop at PLX-0010 would be felt across the cluster within hours.'
            ),
            population=0,
        ),
    ],
    short_description='The junction -- no inhabitants, no resources, and the busiest uninhabited system in the cluster because every trade route passes through it.',
    long_description=(
        'PLX-0010 exists because of geometry. The system has no habitable worlds, no '
        'significant resources, and no reason to be visited except that the jump links '
        'connecting the cluster\'s major systems converge here. Every trade route '
        'passes through PLX-0010. Every military transit crosses it. The system is '
        'the busiest uninhabited point in the Pleiades -- a constant flow of '
        'freighters, warships, and transports passing through a system that offers '
        'nothing except the fuel depot, the communications relay, and the navigational '
        'beacons that the traffic requires.\n\n'
        'The vulnerability is the fuel. PLX-0010 has no gas giant and no local fuel '
        'source -- the depot depends on imported feedstock from neighbouring systems. '
        'A disruption in the resupply would bottleneck every trade route in the '
        'cluster within weeks. The confederation maintains the fuel convoys as a '
        'strategic priority, escorted because an attack on PLX-0010\'s fuel supply '
        'would be an attack on the cluster\'s commerce simultaneously. The system '
        'has no inhabitants, no value, and no replacement.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_3301 = System(
    name='PLX-3301',
    star='Yellow-orange main sequence (G8V), approximately 0.7 times Sol luminosity -- a stable, pleasant star orbited by a world where the colonists became the wildlife',
    population=0,
    distance_to_sol=480.0,
    stellar_objects=[
        StellarObject(
            name='PLX-3301-a',
            short_description='The world the colonists lost -- a habitable planet whose descendants are now the apex predators, no longer capable of speech, reason, or recognition that the overgrown settlements were built by their ancestors.',
            long_description=(
                'PLX-3301-a is a habitable world -- temperate, fertile, orbiting a stable '
                'star, with an alien biosphere that the original survey team assessed as '
                'manageable. The colonists who arrived three centuries ago agreed. The '
                'biosphere was challenging -- aggressive alien predators, toxic flora, '
                'atmospheric compounds that required respiratory modification -- but the '
                'challenges were within the range that the Pleiades\' gene-splicing '
                'technology could address. The splicing programme was designed to make the '
                'colonists competitive with the native fauna: enhanced reflexes, '
                'strengthened musculature, sensory adaptations for the local light and '
                'atmospheric conditions, and the immune modifications that the alien '
                'pathogens required.\n\n'
                'The splicing worked. The colonists survived. The programme continued. Each '
                'generation was spliced further -- deeper integration with the alien biology '
                'that the environment demanded, additional adaptations as new threats were '
                'identified, and the cognitive modifications that the programme\'s designers '
                'believed would improve the colonists\' ability to process the alien sensory '
                'environment. The cognitive modifications were the mistake.\n\n'
                'The alien sensory data that the colonists\' modified brains processed was '
                'vast -- the olfactory landscape of a complex alien biosphere, the visual '
                'data from eyes adapted for wavelengths the original colonists could not '
                'see, the tactile and proprioceptive information from bodies that had been '
                'redesigned for a predatory role in the alien ecosystem. The cognitive '
                'modifications that were intended to process this data instead prioritised '
                'it. Over generations, the brains optimised for processing the alien '
                'sensory environment at the expense of the cognitive functions that the '
                'alien sensory environment did not require: abstract thought, language, '
                'tool use, and the social cognition that makes a human being a person '
                'rather than an animal.\n\n'
                'The decline was not sudden. The early generations were human -- modified, '
                'adapted, but human. The communications with the cluster continued. The '
                'children went to school. The colony functioned. The reports to the '
                'confederation noted that each generation was more physically capable and '
                'less interested in the activities that the reports were written to '
                'describe. The schools closed because the children stopped attending. The '
                'communications became shorter, then intermittent, then stopped. A '
                'confederation inspection team that arrived two centuries after the colony\'s '
                'founding found the settlements overgrown, the equipment abandoned, and '
                'the descendants of the colonists living in the wilderness. The descendants '
                'did not respond to communication. The descendants did not recognise the '
                'inspection team as members of their species. The descendants hunted the '
                'inspection team.\n\n'
                'The system is quarantined. The descendants are the apex predators of '
                'PLX-3301-a -- fast, strong, adapted for the alien environment with a '
                'perfection that the original programme intended and a cost the programme '
                'did not. They hunt in packs using the chemical communication the alien '
                'organisms use. They breed. They raise young that are indistinguishable '
                'from the adults within months. They are, by every biological measure, '
                'superb animals. They are not people. The settlements they were born in are '
                'overgrown. The equipment their grandparents built is rusting. The DNA in '
                'their cells is still recognisably human in origin. Nothing else about '
                'them is.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-3301-b',
            short_description='A quarantine station in orbit -- where the monitoring teams observe the descendants from a distance and the confederation decides, repeatedly, not to intervene.',
            long_description=(
                'PLX-3301-b is an orbital station that serves as the quarantine monitoring '
                'post -- a small facility where the research teams observe the descendants '
                'on the surface and the confederation\'s ethics committees review the data '
                'and decide, each cycle, what to do about a population that was human and '
                'is not.\n\n'
                'The options have been debated for two centuries. Intervene and attempt '
                'genetic restoration -- a programme that the biologists on Rendeven '
                'estimate would take generations and might not work, because the cognitive '
                'decline was developmental rather than purely genetic and the neural '
                'pathways that support language and abstract thought may not re-emerge even '
                'if the genes that originally built them are restored. Leave the '
                'descendants undisturbed and accept that they are now a non-human species '
                '-- an option that the ethics committees find philosophically untenable '
                'because the DNA is still human. Euthanise the population -- an option '
                'that nobody advocates publicly and that the ethics committees have '
                'rejected each time it appears in the classified discussion summaries.\n\n'
                'The confederation has chosen the fourth option: observe, study, and defer '
                'the decision. The monitoring teams document the descendants\' behaviour, '
                'their social structures, their hunting patterns, and the ongoing genetic '
                'drift that carries them further from baseline with each generation. The '
                'data is filed. The decision is deferred. The descendants do not know they '
                'are being observed and would not understand the observation if they did.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-3301-c',
            short_description='A gas giant -- surveyed, unused, orbiting a system that the confederation cannot develop because the quarantine cannot be lifted and the reason for the quarantine cannot be acknowledged.',
            long_description=(
                'PLX-3301-c is a gas giant in the outer system -- surveyed, suitable for '
                'fuel processing, and unused because the system is quarantined and the '
                'quarantine cannot be lifted without acknowledging what happened on the '
                'surface of PLX-3301-a. The gas giant represents the system\'s other loss '
                '-- not just the colonists but the resources, the strategic position, and '
                'the habitable world that the cluster cannot use because using it would '
                'require confronting what the colony became.\n\n'
                'MERIT uses PLX-3301 as its most effective anti-Pleiadian propaganda. The '
                'images -- overgrown settlements, abandoned equipment, and the creatures '
                'that were once human hunting in the ruins of the homes their ancestors '
                'built -- are broadcast across MERIT space as evidence of what biological '
                'modification produces when taken to its conclusion. The Pleiades does not '
                'respond to the propaganda because there is no response that makes the '
                'descendants human again. The confederation classifies PLX-3301 as an '
                'early-programme failure that current protocols would prevent. The '
                'classification is accurate. The images are still effective.'
            ),
            population=0,
        ),
    ],
    short_description='The failure -- a quarantined world where the colonists\' gene-splicing made them apex predators and took their humanity, leaving descendants that hunt in the ruins of the settlements their ancestors built.',
    long_description=(
        'PLX-3301 is the Pleiades\' worst outcome. Three centuries ago, colonists '
        'settled a habitable world and began the gene-splicing programme that the '
        'alien biosphere required. The splicing worked. Each generation was more '
        'adapted, more capable, more competitive with the native fauna. The cognitive '
        'modifications intended to help the colonists process the alien sensory '
        'environment instead prioritised it -- over generations, the brains optimised '
        'for predatory function at the expense of abstract thought, language, tool '
        'use, and the social cognition that makes a person rather than an animal.\n\n'
        'The decline was gradual. Schools closed because children stopped attending. '
        'Communications became intermittent, then stopped. An inspection team two '
        'centuries after founding found overgrown settlements, abandoned equipment, '
        'and descendants living in the wilderness who did not recognise the team as '
        'members of their species. The descendants hunted the inspection team.\n\n'
        'The system is quarantined. The descendants are the apex predators of their '
        'world -- fast, strong, hunting in packs using alien chemical communication. '
        'They breed. They raise young. They are superb animals. They are not people. '
        'The DNA in their cells is still recognisably human. Nothing else about them '
        'is. The confederation observes from orbit, debates intervention it cannot '
        'commit to, and defers the decision each cycle.\n\n'
        'MERIT broadcasts the images across the inner systems -- overgrown '
        'settlements, abandoned homes, and the creatures that were once human hunting '
        'in the ruins. The most effective anti-Pleiadian propaganda ever produced. '
        'The Pleiades does not respond because there is no response that makes the '
        'descendants human again.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_6610 = System(
    name='PLX-6610',
    star='Cataclysmic variable binary -- a white dwarf pulling material from a red giant companion through an accretion disc that periodically ignites in nova-like outbursts, flooding the system with radiation and superheated plasma at irregular intervals',
    population=0,
    distance_to_sol=500.0,
    stellar_objects=[
        StellarObject(
            name='PLX-6610-a',
            short_description='A world that dies and resurrects -- scoured by periodic nova outbursts that sterilise the surface, then recolonised by alien organisms that evolved to survive apocalypse as a routine.',
            long_description=(
                'PLX-6610-a is a rocky world in the habitable zone of the red giant '
                'component -- warm enough between outbursts to support liquid water and a '
                'biosphere, close enough to the binary that the nova outbursts reach it '
                'with lethal intensity. The outbursts are irregular -- years or decades '
                'apart -- and when they occur, the radiation and plasma wave scours the '
                'surface, boils the shallow seas, and kills every organism that has not '
                'prepared for the event.\n\n'
                'The alien life on PLX-6610-a has evolved for apocalypse. The organisms '
                'have developed dormancy mechanisms of extraordinary sophistication -- '
                'the ability to detect the precursor conditions of an outburst, shut down '
                'all metabolic activity, and enter a dormant state that can survive the '
                'radiation, the heat, and the atmospheric disruption that the outburst '
                'produces. The dormancy is not hibernation. It is a complete biological '
                'shutdown -- the organisms reduce to spore-like structures that are '
                'functionally inert and effectively indestructible on the timescales the '
                'outbursts require. When the outburst passes and the conditions return to '
                'habitable, the organisms reactivate -- emerging from dormancy into a '
                'sterilised landscape and recolonising the surface with a speed that '
                'the biologists on Deverne describe as the most impressive biological '
                'recovery mechanism known.\n\n'
                'The cycle has repeated for millions of years. The biosphere on PLX-6610-a '
                'is adapted for periodic total destruction in a way that no other known '
                'ecosystem is. The organisms do not merely survive the outbursts. They '
                'are optimised for them -- the recolonisation phase is the most '
                'biologically productive period in the cycle, and the organisms\' '
                'reproductive strategies are designed to exploit the resource-rich, '
                'competition-free environment that exists immediately after the surface '
                'has been sterilised. The outburst is not a catastrophe for this '
                'ecosystem. It is a harvest.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-6610-b',
            short_description='A frozen outer body beyond the outburst zone -- the research station where the dormancy organisms are studied in safety, analysing the biological shutdown that the Pleiades wants to splice into its people.',
            long_description=(
                'PLX-6610-b is a frozen body in the outer system -- far enough from the '
                'binary that the outbursts reach it as elevated radiation rather than '
                'lethal events. The research station on PLX-6610-b is where the dormancy '
                'organisms are studied -- specimens collected from PLX-6610-a between '
                'outbursts and maintained in controlled environments that the researchers '
                'can observe without the risk of being sterilised alongside their subjects.\n\n'
                'The dormancy mechanisms are the prize. The ability to detect a lethal '
                'event, shut down the body, and reactivate when the danger has passed is '
                'a capability that the Pleiades\' bioengineers want to translate into human '
                'gene-splicing. The applications are military and civilian: crews that can '
                'enter dormancy during a catastrophic hull breach, workers who can survive '
                'a radiation event by shutting down rather than dying, and the stabilisation '
                'application -- the dormancy genes may include mechanisms for preserving '
                'genetic stability during the shutdown that could improve the cluster\'s '
                'stabilisation compounds.\n\n'
                'The research is difficult. The dormancy mechanism is not a single gene '
                'sequence but a coordinated biological programme involving hundreds of '
                'genes that must activate in the correct sequence and deactivate in the '
                'correct sequence for the organism to survive. Splicing a partial sequence '
                'into a human subject would produce a partial shutdown -- which is to say, '
                'it would produce death. The challenge is splicing the complete programme '
                'or nothing. The researchers have been working on the problem for decades. '
                'The problem is not yet solved. The outbursts continue on their own '
                'schedule, and after each one the researchers return to PLX-6610-a to '
                'collect fresh specimens from an ecosystem that has just survived another '
                'apocalypse and does not understand why the researchers find this '
                'impressive.'
            ),
            population=0,
        ),
        StellarObject(
            name='The Accretion',
            short_description='The accretion disc itself -- the visible mechanism of the system\'s violence, a disc of stolen stellar material spiralling into the white dwarf and periodically detonating.',
            long_description=(
                'The Accretion is the disc of material that the white dwarf is pulling '
                'from its red giant companion -- a visible, luminous structure spiralling '
                'into the dense remnant star and periodically accumulating enough material '
                'to trigger the thermonuclear detonation that produces the nova-like '
                'outburst. The disc is the system\'s defining feature -- visible from every '
                'point in the system as a bright, hot spiral that the navigation charts '
                'mark as a hazard and that the researchers consider one of the most '
                'beautiful astronomical features in the cluster.\n\n'
                'The outbursts are monitored by the research station on PLX-6610-b. The '
                'precursor conditions -- the disc brightening, the accumulation rate '
                'increasing, the spectral signatures that indicate the thermonuclear '
                'threshold is approaching -- are detectable days to weeks before the '
                'outburst, giving the researchers time to withdraw from PLX-6610-a and '
                'shelter on PLX-6610-b. The monitoring is also the dormancy research\'s '
                'most valuable tool: the alien organisms on PLX-6610-a detect the same '
                'precursor conditions and begin their dormancy shutdown before the '
                'researchers\' instruments confirm the event. The organisms know. The '
                'instruments confirm. The researchers are studying how the organisms know, '
                'because that detection mechanism is itself a splicing candidate.'
            ),
            population=0,
        ),
    ],
    short_description='The apocalypse system -- a cataclysmic variable binary that periodically sterilises the inner world, where the alien life has evolved to survive destruction and the Pleiades wants to learn how.',
    long_description=(
        'PLX-6610 is a cataclysmic variable binary -- a white dwarf pulling material '
        'from a red giant companion through a luminous accretion disc that '
        'periodically ignites in nova-like outbursts. The outbursts are irregular and '
        'violent -- radiation and superheated plasma that reach the inner world with '
        'enough intensity to sterilise the surface, boil the seas, and kill every '
        'organism that has not prepared.\n\n'
        'The alien life has prepared. The organisms on PLX-6610-a have evolved '
        'dormancy mechanisms of extraordinary sophistication -- the ability to detect '
        'the precursor conditions, shut down all metabolic activity, and enter a '
        'spore-like state that survives the outburst. When conditions return to '
        'habitable, the organisms reactivate and recolonise the sterilised surface '
        'with a speed the biologists describe as the most impressive recovery '
        'mechanism known. The outburst is not a catastrophe for this ecosystem. It '
        'is a harvest -- the recolonisation phase is the most productive period.\n\n'
        'The Pleiades wants the dormancy. The ability to shut down and survive a '
        'lethal event has military, civilian, and stabilisation applications. The '
        'challenge: the dormancy is a coordinated programme of hundreds of genes '
        'that must activate and deactivate in the correct sequence. A partial splice '
        'produces death, not dormancy. The researchers have been working for decades. '
        'The problem is not yet solved. The outbursts continue on their own schedule, '
        'and the alien organisms detect the precursor conditions before the '
        'instruments confirm them -- a detection mechanism that is itself a splicing '
        'candidate the researchers are studying.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_8801 = System(
    name='PLX-8801',
    star='Red dwarf (M2V), approximately 0.08 times Sol luminosity -- a dim, cold star orbited by a world whose alien life could solve problems the cluster has been trying to solve for decades, if the testing ever produces clean results',
    population=0,
    distance_to_sol=470.0,
    stellar_objects=[
        StellarObject(
            name='PLX-8801-a',
            short_description='An alien biosphere under active study -- organisms adapted to cold, low-light conditions whose gene sequences could benefit multiple strains, if the animal testing stops producing failures.',
            long_description=(
                'PLX-8801-a is a cold, dim world in the habitable zone of a red dwarf -- '
                'conditions that have produced an alien biosphere adapted for low light, '
                'low temperature, and the metabolic efficiency that energy-scarce '
                'environments demand. The organisms on PLX-8801-a are slow, patient, and '
                'extraordinarily efficient -- biological systems that extract maximum '
                'nutrition from minimum input, cellular structures that function at '
                'temperatures where terrestrial biology shuts down, and sensory systems '
                'tuned for the dim red light that the star provides.\n\n'
                'The gene sequences are what the Pleiades wants. The cold-adaptation '
                'genes would benefit the populations on the cluster\'s colder worlds. The '
                'metabolic efficiency genes could improve the nutrition-to-function ratio '
                'for strains whose current splicing demands more caloric input than the '
                'local agriculture easily provides. The low-light visual adaptations would '
                'complement the military splicing programme on Almach. The applications '
                'are numerous, well-defined, and waiting on the testing.\n\n'
                'The testing is the problem. The animal testing facilities on PLX-8801-a '
                'have been operating for seven years, and the results are mixed in the way '
                'that researchers use the word mixed when they mean disappointing. The '
                'cold-adaptation sequences integrate cleanly in some subjects and produce '
                'cascading metabolic failures in others. The efficiency genes work in '
                'isolation but interact unpredictably with the existing modification '
                'packages that the cluster\'s strains carry. The visual adaptations are '
                'the closest to viable -- the testing subjects show functional low-light '
                'vision with manageable side effects -- but the other sequences are years '
                'from approval.\n\n'
                'The testing facilities house the failures alongside the successes. The '
                'subjects that integrated the cold-adaptation genes and suffered metabolic '
                'failure are maintained for study -- animals whose bodies produce less heat '
                'than the environment requires, slowly cooling, sustained by the laboratory '
                'conditions but unable to thermoregulate independently. The subjects are '
                'not in pain. The subjects are slowly, measurably, getting colder. The '
                'researchers monitor the cooling as data. The animal care staff monitor '
                'it as something else.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-8801-b',
            short_description='A frozen outer body hosting the research station -- where the scientists live between testing cycles and where the confederation\'s strain committees argue about which strain gets priority access to the results.',
            long_description=(
                'PLX-8801-b is a frozen body hosting the research station that supports '
                'the testing programme on PLX-8801-a. The station houses the research staff, '
                'the data processing facilities, and the communications equipment that '
                'transmits the results to Rendeven for analysis. The station also hosts the '
                'confederation\'s strain priority committees -- the representatives of the '
                'various strains who argue about which strain gets first access to the '
                'gene sequences when the testing is complete.\n\n'
                'The priority arguments are the political dimension of the research. The '
                'cold-adaptation genes are most relevant to the strains on the cluster\'s '
                'colder worlds, but the metabolic efficiency genes would benefit every '
                'strain, and the competition for priority access is fierce. The committees '
                'negotiate on PLX-8801-b in the same sealed-pod format as the Atrium -- '
                'representatives of biologically incompatible strains arguing about '
                'resources through airlocks. The researchers find the political process '
                'exhausting and the committees find the research timeline unacceptable '
                'and both are correct.'
            ),
            population=0,
        ),
        StellarObject(
            name='PLX-8801-c',
            short_description='A small gas giant -- fuel processing for the research traffic, in a system where the only visitors are scientists and the committee delegates who argue about their work.',
            long_description=(
                'PLX-8801-c is a small gas giant with fuel processing on its single moon '
                '-- supporting the modest traffic that the research programme generates. '
                'The fuel workers serve rotations that are quiet even by uninhabited-system '
                'standards -- the only traffic is the research supply ships and the '
                'committee delegates\' transports. The fuel workers have learned more about '
                'inter-strain politics than they expected or wanted, because the delegates '
                'talk during refuelling stops and the arguments are audible through the '
                'docking interfaces.'
            ),
            population=0,
        ),
    ],
    short_description='The testing ground -- an alien biosphere with gene sequences the cluster needs, held up by animal testing that keeps producing failures alongside the successes.',
    long_description=(
        'PLX-8801 is the Pleiades\' most promising and most frustrating research '
        'site. The alien biosphere on PLX-8801-a -- adapted for cold, dim, energy-'
        'scarce conditions -- contains gene sequences that would benefit multiple '
        'strains across the cluster: cold adaptation, metabolic efficiency, low-light '
        'vision. The applications are well-defined and the demand is established.\n\n'
        'The testing has been running for seven years. The results are mixed. Some '
        'sequences integrate cleanly. Some produce cascading metabolic failures. The '
        'efficiency genes work in isolation but interact unpredictably with existing '
        'modification packages. The testing facilities house the failures alongside '
        'the successes -- animals with cold-adaptation genes whose bodies produce '
        'less heat than the environment requires, slowly cooling, sustained by the '
        'laboratory but unable to thermoregulate. The researchers monitor the cooling '
        'as data. The animal care staff monitor it as something else.\n\n'
        'The politics add a layer: the strain priority committees argue on PLX-8801-b '
        'about which strain gets first access to the results, negotiating in sealed '
        'pods through airlocks the same way they negotiate everything. The researchers '
        'find the politics exhausting. The committees find the timeline unacceptable. '
        'The alien organisms on the surface continue to thrive in the cold and the '
        'dark, carrying the gene sequences the cluster wants, in bodies that the '
        'testing has not yet learned to translate into human biology without the '
        'translation going wrong.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_9901 = System(
    name='PLX-9901',
    star='Red dwarf (M3V), approximately 0.04 times Sol luminosity -- a dim, cold star marking the first waypoint on the route that the cluster cannot afford to lose',
    population=3_000_000,
    distance_to_sol=530.0,
    stellar_objects=[
        StellarObject(
            name='PLX-9901-a',
            short_description='A cold, rocky world with simple alien life in the subsurface -- catalogued, filed, and unremarkable, orbiting below the station that is the system\'s only reason to exist.',
            long_description=(
                'PLX-9901-a is a cold, rocky world with no atmosphere and no value. The '
                'local alien life is simple -- extremophile organisms in the rock\'s '
                'subsurface layers, feeding on chemical energy from the planetary interior. '
                'The organisms are resilient, slow-growing, and biologically uninteresting '
                'by Pleiadian standards -- the gene sequences have been catalogued and '
                'filed without urgency. The researchers have noted that the organisms\' '
                'radiation resistance is modest and their metabolic pathways are '
                'unremarkable. The organisms are the only permanent life in the system '
                'apart from the station crew above. They do not know they are guarding '
                'a supply route.'
            ),
            population=0,
        ),
        StellarObject(
            name='Waypoint One',
            short_description='The refuelling station -- a small orbital installation where the compound freighters dock, refuel, and continue the transit, crewed by a garrison one jump from Maia and one from nowhere.',
            long_description=(
                'Waypoint One is the orbital station that is PLX-9901\'s entire reason for '
                'existing -- the first refuelling stop on the Electra route, where the '
                'compound freighters dock between the Maia and PLX-9902 jumps. The station '
                'handles the fuel processing, the communications relay, and the garrison '
                'that protects both. The population is small -- a few million, rotating on '
                'hardship postings that the fleet assigns to crews who understand the '
                'assignment\'s importance and resent its isolation in equal measure.\n\n'
                'The station is functional in the way that military infrastructure is '
                'functional -- built for the job, maintained to the standard the job '
                'demands, and entirely without comfort beyond what keeps the crew '
                'operational. The docking bays are sized for compound freighters. The fuel '
                'storage is sized for the transit traffic. The weapons are sized for the '
                'knowledge that if someone attacks this station, they are attacking the '
                'cluster\'s most critical supply chain and the garrison must hold until '
                'Ardenne\'s forces arrive from Maia -- one jump and hours of transit away.\n\n'
                'The station maintains a backup fuel cache on PLX-9901-a\'s surface -- a '
                'contingency that provides enough fuel for the compound freighters to '
                'complete their transit to Maia if the station is damaged. The backup is '
                'checked monthly, restocked annually, and has never been used. The garrison '
                'considers this the ideal outcome and maintains the backup anyway, because '
                'the consequence of needing it and not having it is a disruption in the '
                'compound supply that the cluster cannot tolerate.'
            ),
            population=3_000_000,
        ),
    ],
    short_description='The first waypoint -- a refuelling station and garrison on the Electra route, watching the supply chain\'s most vulnerable link in a system that has nothing except its position.',
    long_description=(
        'PLX-9901 is the first waypoint on the four-jump route between Maia and '
        'Electra -- one jump from Maia, one jump from PLX-9902, and the point where '
        'the compound freighters refuel on their transit in both directions. The '
        'system has no habitable worlds, no significant resources, and no value '
        'except its position on the route that the cluster\'s stabilisation supply '
        'depends on.\n\n'
        'Waypoint One is the orbital station that makes the route functional -- a '
        'few million crew on hardship rotation, maintaining the fuel processing, the '
        'communications relay, and the garrison. The nearest help is the Maia '
        'garrison at Ardenne, one jump and hours of transit away. The crew knows '
        'that if an attack comes, they hold until help arrives, and that the attack '
        'would come because someone has decided to target the cluster\'s weakest '
        'point.\n\n'
        'The local alien life is simple extremophile organisms in the subsurface -- '
        'catalogued, filed, unremarkable. PLX-9901 and its twin waypoint PLX-9902 '
        'are the two most strategically important systems on the Electra route, '
        'and the garrisons that crew the stations carry the awareness that they are '
        'guarding something more important than themselves on a posting that nobody '
        'wants and everybody understands.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLX_9902 = System(
    name='PLX-9902',
    star='Orange dwarf (K5V), approximately 0.15 times Sol luminosity -- slightly warmer than its twin waypoint\'s star, hosting alien life that is slightly more interesting and a garrison that is equally nervous',
    population=2_000_000,
    distance_to_sol=560.0,
    stellar_objects=[
        StellarObject(
            name='PLX-9902-a',
            short_description='A cold world with more complex alien life than PLX-9901 -- surface-dwelling organisms with antifreeze compounds flagged as a splicing candidate and waiting in the queue.',
            long_description=(
                'PLX-9902-a is a cold world with a thin atmosphere that supports alien '
                'life more complex than PLX-9901\'s subsurface extremophiles. The '
                'organisms on PLX-9902-a include surface-dwelling species -- low, spreading '
                'organisms that cover the rocky plains in mats of alien biology, feeding '
                'on the dim starlight and the chemical energy from volcanic vents scattered '
                'across the surface. The mats are the base of a simple but functional '
                'ecosystem that includes small mobile organisms -- slow, cold-adapted '
                'creatures that graze the mats and that the researchers have catalogued '
                'with more interest than PLX-9901\'s subsurface life attracted.\n\n'
                'The gene sequences in PLX-9902-a\'s organisms have been catalogued and '
                'flagged for eventual study. The cold-adaptation mechanisms differ from '
                'PLX-8801\'s organisms\' approach -- where PLX-8801\'s life adapted through '
                'metabolic efficiency, PLX-9902\'s organisms adapted through chemical '
                'antifreeze compounds that prevent cellular ice formation at temperatures '
                'well below terrestrial survivability. The antifreeze mechanism is a '
                'splicing candidate but not a priority -- the testing queue at Rendeven is '
                'long, the resources are allocated to higher-priority programmes, and '
                'PLX-9902\'s organisms wait in the catalogue alongside dozens of other '
                'species whose gene sequences might be useful if the researchers ever have '
                'time.'
            ),
            population=0,
        ),
        StellarObject(
            name='Waypoint Two',
            short_description='The second refuelling station -- the last stop before Electra, crewed by the most isolated garrison on the route, one jump from the source and two jumps from help.',
            long_description=(
                'Waypoint Two is the orbital station that serves as the Electra route\'s '
                'last refuelling stop before the final jump -- the point where the '
                'compound freighters take on the fuel that must carry them to Electra\'s '
                'Oskelan and back, because the gap between PLX-9902 and Electra is the '
                'longest stretch on the route without a fuel source. The station verifies '
                'every departure\'s fuel status with the thoroughness of people who '
                'understand that a stranded freighter on the Electra gap is a freighter '
                'that is not carrying compounds back.\n\n'
                'The garrison on Waypoint Two is the most isolated on the route -- one '
                'jump from Electra, two jumps from Maia, and the furthest point from any '
                'reinforcement. An attack on PLX-9902 would cut the route between Electra '
                'and PLX-9901, and the garrison would need to hold until Maia\'s forces '
                'transit through PLX-9901 to reach them. The transit time is long enough '
                'that the garrison plans for self-sufficiency in a fight, and the crew '
                'rotations are shorter than Waypoint One\'s because the isolation is '
                'harder to sustain.\n\n'
                'The station mirrors Waypoint One in function -- fuel processing, '
                'communications relay, garrison -- and in character. The same functional '
                'construction, the same absence of comfort, the same awareness that the '
                'posting is the loneliest important job in the cluster. The backup fuel '
                'cache is maintained on PLX-9902-a\'s surface, checked and restocked on '
                'the same schedule as Waypoint One\'s. The two stations are twins -- same '
                'purpose, same isolation, same quiet importance, separated by one jump '
                'and connected by the freighters that carry the compounds the cluster '
                'cannot survive without.'
            ),
            population=2_000_000,
        ),
    ],
    short_description='The second waypoint -- the last refuelling station before Electra, one jump from the source and two from help, crewed by the most isolated garrison on the route.',
    long_description=(
        'PLX-9902 is the second waypoint on the Electra route -- one jump from '
        'Electra, two from Maia, and the most isolated garrison on the supply chain. '
        'Waypoint Two is the orbital station that serves as the last refuelling stop '
        'before the final jump -- the point where every departure\'s fuel status is '
        'verified because a stranded freighter on the Electra gap is a missed '
        'compound shipment.\n\n'
        'The alien life on PLX-9902-a is more complex than the first waypoint\'s -- '
        'surface-dwelling organisms in mats across the rocky plains, small mobile '
        'grazers, a simple but functional ecosystem. The gene sequences include '
        'chemical antifreeze compounds that prevent cellular ice formation -- a '
        'splicing candidate catalogued and waiting in the queue behind higher-'
        'priority programmes.\n\n'
        'PLX-9901 and PLX-9902 together are the Electra route\'s twin vulnerabilities '
        '-- the two points where the supply chain is thinnest, guarded by stations '
        'crewed by garrisons too small to stop a serious attack and too important to '
        'leave unguarded. The crew rotations are short because the isolation is hard. '
        'The fuel loads are verified because a stranded freighter is a missed '
        'shipment. The loneliest important job in the cluster, performed at two '
        'stations on a route that the cluster\'s stability depends on.'
    ),
    cluster=StarClusters.PLEIADES,
)

PLEIADES_SYSTEMS: list[System] = [
    ALCYONE,
    ATLAS,
    PLX_0010,
    MAIA,
    MEROPE,
    TAYGETA,
    CELAENO,
    PLEIONE,
    ASTEROPE,
    MIRACH,
    ALMACH,
    ALBIREO,
    SPICA,
    PLX_3301,
    PLX_6610,
    PLX_8801,
    PLX_9901,
    PLX_9902,
    ELECTRA,
]
