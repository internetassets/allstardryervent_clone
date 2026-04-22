import re, os

BASE = r'C:\Users\rusty\allstardryervent_clone\locations'

LOCATIONS = {
    'sparks-nevada-dryer-vent-cleaning': {
        'city': 'Sparks',
        'hero_para': "Sparks has grown fast over the past two decades, and the construction that came with that growth left thousands of homes with dryer vent systems already showing wear. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Sparks from Victorian Square to Wingfield Springs, working on aging flexible duct in older east Sparks homes and the longer rigid metal duct runs common in newer Spanish Springs and D'Andrea builds.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Sparks</strong>, NV across every neighborhood in the city. Older areas near Victorian Avenue and the Sparks Marina frequently have original accordion-style flexible duct that degrades over time, collapsing and trapping lint far faster than smooth rigid metal duct. Newer communities like Wingfield Springs and D\'Andrea have cleaner installations but vent runs that stretch 20 feet or more depending on laundry room placement. Bird nesting in exterior vent covers is also a consistent problem in Sparks during spring - a nest-blocked vent stops all exhaust airflow and is one of the fastest ways to create a dryer fire hazard. We clear nests and inspect exterior terminations on every dryer vent cleaning visit.',
        'local_seo_bottom': "We serve all of Sparks including Spanish Springs, Wingfield Springs, and the neighborhoods along McCarran Boulevard. Same-day dryer vent cleaning in Sparks is available most days. <strong>Call 775-224-4136</strong> for your free estimate.",
        'services_h2': 'Sparks Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to full vent system repair and dryer vent inspection, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> in Sparks and Washoe County.',
        'why_p1': "Since 2013, All Star Dryer Vent has handled dryer vent cleaning and repair in Sparks across every type of home the city has. We have worked inside the tight utility spaces of older Victorian Square-era homes, navigated two-story layouts in D'Andrea, and dealt with long horizontal vent runs that show up regularly in Spanish Springs construction. We know what Sparks building codes require and what configurations other contractors commonly leave in substandard condition.",
        'why_p2': 'All of our technicians are CSIA certified and direct employees of All Star Dryer Vent - no subcontracting. When you schedule <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Sparks</a></strong> with All Star, you get an experienced technician with commercial-grade rotary brush and compressed air equipment. Every visit includes a written 12-point safety inspection. If we find anything during dryer vent cleaning that needs repair, we document it and walk you through the options.',
        'why_p3': 'We cover all of Sparks and the surrounding Spanish Springs Valley. Most days we have same-day or next-day availability. Call 775-224-4136 or book online to get on the schedule.',
        'benefits': [
            ('Fire Prevention', "Lint is highly flammable - the U.S. Fire Administration estimates dryer fires cause roughly 2,900 home fires per year nationally. In Sparks's dry high-desert climate, lint packed into an exhaust duct is an accelerated fire risk. Annual dryer vent cleaning removes that hazard before it becomes a claim."),
            ('Air Quality & Safety', 'A blocked dryer vent does not just trap lint. For gas dryers it can push carbon monoxide back into living spaces. Clean exhaust duct airflow keeps combustion byproducts moving outside where they belong, protecting everyone in your Sparks home.'),
            ('Mold & Moisture Control', "Even in Sparks's arid climate, a blocked dryer vent traps moisture inside walls and crawlspaces. Over time that humidity creates conditions for mold growth that is costly to remediate. Proper dryer vent airflow is the first line of defense."),
            ('Energy Efficiency', "A restricted vent line forces your dryer through additional cycles to dry a single load. Sparks residents see measurable improvement in drying times and NV Energy bills after a professional dryer vent cleaning clears the restriction."),
            ('Appliance Longevity', 'Dryers working against restricted airflow run hotter and wear out faster - motors, heating elements, and drum bearings all degrade under thermal stress. Regular dryer vent cleaning in Sparks extends appliance life and defers replacement costs.'),
            ('Peace of Mind', 'A CSIA certified technician has inspected your vent, documented its condition in writing, and confirmed it is clear and exhausting properly. That is one less fire risk to carry in your Sparks home.'),
        ],
        'warnings': [
            ('Clothes Taking Multiple Cycles', "If a standard load needs more than one cycle to dry, restricted airflow in the exhaust duct is the most common cause. Sparks's high-altitude air is already thinner - a clogged vent line compounds the problem significantly."),
            ('Laundry Room Running Hot', 'An unusually warm laundry room or a dryer hot to the touch after a cycle means heat is not escaping through the exhaust duct. That trapped heat is a fire risk in any Sparks home.'),
            ('Dryer Shutting Off Mid-Cycle', 'Thermal overload shutoffs protect the appliance when it overheats. If your dryer stops before the cycle ends, check the vent before calling for appliance repair - most cases we see in Sparks are airflow problems, not mechanical failures.'),
            ('Damp Clothes or Musty Smell', 'Moisture that cannot exhaust through a blocked vent stays in your laundry. Clothes come out damp and develop a musty odor, and moisture sitting inside the duct promotes mold growth inside the vent line itself.'),
            ('Lint Accumulating Behind the Dryer', 'Lint escaping from joints or connections behind the dryer means back-pressure is building inside a clogged system. This is a visible warning that your Sparks home needs professional dryer vent cleaning immediately.'),
            ('No Lint on the Lint Screen', 'If the lint trap looks unusually clean after a full cycle, lint is bypassing the trap and packing into the exhaust duct. This counterintuitive sign is one of the more serious warnings we encounter.'),
            ('Burning Smell During Operation', 'Any burning odor during a drying cycle should be treated as urgent. Stop the dryer and call us. Lint in contact with a heating element or a hot duct wall is exactly how dryer fires start.'),
            ('Exterior Vent Flap Not Opening', 'Check your exterior vent cover during a cycle. If the flap is not opening fully, airflow is severely restricted. Bird nests are a frequent cause in Sparks - we clear them as part of every dryer vent cleaning visit.'),
            ('More Than One Year Since Last Service', 'Most manufacturers and fire safety organizations recommend annual dryer vent cleaning. If you cannot recall when your Sparks vent was last professionally serviced, it is overdue.'),
        ],
    },

    'incline-village-nevada-dryer-vent-cleaning': {
        'city': 'Incline Village',
        'hero_para': 'Incline Village sits at over 6,200 feet on the north shore of Lake Tahoe, and that elevation and forest environment create dryer vent conditions most homeowners underestimate. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Incline Village for full-time residents, seasonal homeowners, and vacation rental operators who need documented proof that their properties are safely maintained.',
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Incline Village</strong> with the specific Tahoe-environment knowledge the area demands. Pine needle debris and wildlife nesting in exterior vent covers are common causes of complete airflow blockage here. Winter ice can seal vent terminations shut, and the first loads of the season run against a frozen flap until it is cleared. Vacation rental and second-home owners often discover their vent has not been serviced in several years - sometimes never - with significant lint buildup accumulated in the exhaust duct. Homes in the Tyner and Ponderosa Ranch areas often have older vent configurations; newer builds near the country club tend to have longer runs routed around complex floor plans. We carry the equipment for all of it.',
        'local_seo_bottom': 'We service Incline Village, Crystal Bay, and the surrounding Lake Tahoe North Shore. Advance scheduling is recommended for vacation rental turnovers. <strong>Call 775-224-4136</strong> for your free estimate.',
        'services_h2': 'Incline Village Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to post-winter vent inspection and full system repair, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Incline Village and the Lake Tahoe North Shore.',
        'why_p1': 'Dryer vent cleaning in Incline Village requires knowing the specific conditions that affect Tahoe-area homes. We have worked on vent lines blocked by pine cone debris, bird and squirrel nests, and ice-sealed exterior terminations. We have cleaned systems in vacation rentals that had not been serviced in five or more years and required multiple passes to fully clear. We understand the seasonal ownership patterns here and regularly coordinate service calls with property managers for absent owners.',
        'why_p2': 'Every technician is CSIA certified and a direct employee of All Star Dryer Vent - no subcontractors. We use commercial-grade rotary brush and compressed air equipment that clears even heavily packed lint from long or complex vent runs. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Incline Village</a></strong> includes a written 12-point safety inspection. We document everything so property owners have maintenance records for insurance, HOA compliance, or rental property files.',
        'why_p3': 'We serve Incline Village, Crystal Bay, and the Lake Tahoe North Shore. Call 775-224-4136 or book online to schedule dryer vent cleaning or a safety inspection.',
        'benefits': [
            ('Fire Prevention', 'At Lake Tahoe elevations the surrounding forest makes dryer fire risk feel immediate. Lint buildup in exhaust duct lines is one of the leading causes of home fires nationally. Annual dryer vent cleaning in Incline Village removes that fuel load from your home.'),
            ('Air Quality & Carbon Monoxide', "For gas dryers, a blocked vent duct can allow carbon monoxide to backflow into living spaces. Incline Village's tight, well-insulated mountain homes can trap combustion gases quickly - clean exhaust airflow is not optional."),
            ('Wildlife & Debris Blockage', 'Bird and squirrel nesting in exterior vent covers is extremely common in the Tahoe basin. A nest completely stops airflow through the dryer vent. We inspect and clear exterior vent terminations on every cleaning visit as part of standard service.'),
            ('Winter & Ice Damage', 'Snow and ice can seal exterior vent flaps shut, causing complete airflow blockage. A post-winter dryer vent inspection confirms your termination is clear and undamaged before you run the first loads of the season.'),
            ('Vacation Rental Documentation', 'Vacation rental operators have liability exposure when appliances are not properly maintained. Annual dryer vent cleaning with a written inspection report creates a maintenance record that protects you and satisfies common HOA requirements.'),
            ('Appliance Performance at Altitude', 'High-altitude air is already thinner, which affects dryer efficiency. A restricted exhaust duct compounding that effect significantly shortens appliance life and increases operating costs. Clean vent lines restore design-rated performance.'),
        ],
        'warnings': [
            ('Longer Drying Times Than Usual', 'At Incline Village elevations, drying times are already slightly longer than at lower altitude. If loads are taking significantly more than one cycle, a blocked exhaust duct is the most likely cause.'),
            ('Laundry Room Overheating', 'A laundry room that feels noticeably warm during a cycle means heat is not escaping through the vent. In a well-insulated mountain home this heat buildup can be significant and is a dryer fire warning.'),
            ('Dryer Stopping Mid-Cycle', 'Thermal cutoff triggers protect the appliance when it overheats. Before replacing any parts, have the exhaust duct inspected - blocked dryer vents are the most common cause of this symptom in Incline Village homes.'),
            ('Musty or Off Odor on Dried Laundry', 'Any odor on dried clothes - musty, stale, or otherwise off - indicates the exhaust duct is not properly moving air and moisture away from the drum during the cycle.'),
            ('No Airflow at Exterior Vent', 'During a drying cycle, hold your hand near the exterior vent termination. Minimal or no airflow means the duct is blocked - possibly by lint, a nest, or an ice-damaged flap that is not opening.'),
            ('Visible Debris Around Vent Opening', 'Pine needles, seed pods, and bird nesting material around the exterior vent cover indicate debris has entered the termination. A dryer vent inspection determines how far into the duct it extends.'),
            ('Burning Smell During Operation', 'Any burning smell during a drying cycle is an emergency. Stop the dryer immediately and call us. Lint in contact with a hot duct surface is how dryer fires start.'),
            ('Unknown Service History on Seasonal Property', 'If you are opening a vacation home after months away, or taking over a rental property, assume the dryer vent needs inspection. We regularly find Incline Village properties where the vent has never been professionally cleaned.'),
            ('HOA or Insurance Maintenance Requirements', 'Some Incline Village communities require documented appliance maintenance. Annual dryer vent cleaning with a written inspection report satisfies those requirements and gives you records if they are ever requested.'),
        ],
    },

    'minden-nevada-dryer-vent-cleaning': {
        'city': 'Minden',
        'hero_para': "The Carson Valley is drier and windier than most people expect, and that combination works hard on dryer vent systems in Minden homes. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Minden and the surrounding Gardnerville area, working on older ranch homes with decades-old vent routing, rural properties with propane dryers, and newer construction along the US-395 corridor.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Minden</strong>, NV and the Carson Valley with an understanding of what makes this area different. Fine dust from hay fields and alfalfa operations accumulates inside vent lines faster than standard household lint alone. Strong easterly winds off the Sierra Nevada push debris against exterior vent covers and can force flap mechanisms shut. Many homes in the area still have original flexible accordion duct that has been in service 20 or more years - that material degrades and collapses, and its corrugated interior traps lint at a much higher rate than smooth rigid metal duct. Propane dryers are also more common in rural Carson Valley, and those systems need the same annual dryer vent cleaning attention as electric models.',
        'local_seo_bottom': 'We serve Minden, Gardnerville, and the Carson Valley. All Star is one of the few dryer vent specialists that regularly makes the drive south from Reno for residential service calls. <strong>Call 775-224-4136</strong> for your free estimate.',
        'services_h2': 'Minden Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to rigid metal duct replacement and full system repair, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Minden and the Carson Valley.',
        'why_p1': "Dryer vent cleaning in Minden means dealing with conditions that differ from the Reno-Sparks metro. We have cleaned vent lines packed with agricultural dust on top of standard lint, replaced decades-old accordion duct with code-compliant rigid metal duct, and serviced propane dryer systems on rural properties that had never received professional dryer vent cleaning. We know the Carson Valley housing stock and the environmental conditions that accelerate lint buildup here.",
        'why_p2': 'Every technician is CSIA certified and a direct All Star Dryer Vent employee - no subcontracting. We carry commercial-grade rotary brush and compressed air equipment that clears even densely packed exhaust duct lines. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Minden</a></strong> includes a written 12-point safety inspection with documentation of any conditions that need dryer vent repair or duct replacement.',
        'why_p3': 'We cover Minden, Gardnerville, and the surrounding Carson Valley. We make the trip south regularly and can usually schedule within a few days. Call 775-224-4136 or book online.',
        'benefits': [
            ('Fire Prevention', 'Agricultural dust from Carson Valley farming operations makes lint buildup in Minden vent lines more aggressive than in urban homes. Annual dryer vent cleaning removes the accumulated fuel load before it becomes a fire risk in your exhaust duct.'),
            ('Air Quality & Carbon Monoxide', 'Rural Minden properties with propane dryers face carbon monoxide backflow risk if the exhaust duct is blocked. Proper dryer vent airflow keeps combustion gases moving outside where they belong.'),
            ('Agricultural Dust Accumulation', 'Hay dust, alfalfa chaff, and fine agricultural particulate enter dryer vent lines through exterior covers and combine with lint to form dense blockages faster than in urban homes. Annual dryer vent cleaning is especially important for Carson Valley properties.'),
            ('Energy Efficiency', 'A clogged vent forces extra cycles to dry each load. Minden properties running propane or electricity at rural utility rates see direct savings when dryer vent cleaning restores proper exhaust airflow and drying efficiency.'),
            ('Wind Damage to Exterior Covers', "Strong Carson Valley winds damage exterior vent covers and flap mechanisms, preventing proper airflow. We inspect terminations on every dryer vent cleaning visit and replace damaged components during the same appointment."),
            ('Appliance Longevity', 'In a rural setting where appliance service calls involve a long drive, protecting your dryer with annual dryer vent cleaning is straightforward preventative maintenance that defers replacement costs by years.'),
        ],
        'warnings': [
            ('Clothes Taking More Than One Cycle', 'Restricted exhaust duct airflow is the most common reason a load needs multiple cycles to dry. In Minden where laundry rooms are often positioned deep inside a home, vent runs can be long and accumulate lint faster than homeowners expect.'),
            ('Laundry Room or Dryer Running Hot', 'Heat that cannot escape through the exhaust duct stays in the appliance and laundry room. A hot dryer exterior or an unusually warm laundry room after a cycle are direct fire warnings.'),
            ('Dryer Stopping Before the Cycle Ends', 'Thermal overload protection shuts the dryer down when it overheats. Before replacing heating elements or thermostats, have the exhaust duct inspected - blocked dryer vents cause this symptom more often than mechanical failure.'),
            ('Damp Laundry or Musty Smell', 'Moisture trapped by a blocked vent stays in your laundry. Clothes come out damp, develop an odor, and the blocked duct itself can develop mold growth over time.'),
            ('Lint Escaping Around the Dryer Connection', 'Lint appearing at the joint between the dryer and the wall duct indicates back-pressure from a clogged vent line. This is a visible sign the system needs professional dryer vent cleaning immediately.'),
            ('No Lint on the Lint Screen', 'If the lint trap is unusually clean after a full cycle, lint is bypassing the trap and packing into the exhaust duct. This counterintuitive sign is one of the more serious warnings we encounter.'),
            ('Burning Odor During Operation', 'Any burning smell during a drying cycle is an emergency. Stop the dryer and call us. Lint contacting a heating element or hot duct surface is how dryer fires start.'),
            ('Exterior Vent Flap Stuck or Damaged', "Minden's winds routinely damage exterior vent cover flaps. If the flap is stuck closed, bent, or missing, airflow is compromised. Check exterior vent covers after any strong wind event in the Carson Valley."),
            ('More Than One Year Since Last Cleaning', 'Annual dryer vent cleaning is the industry and manufacturer standard. If your Minden property has not had professional dryer vent service in over a year, it is overdue.'),
        ],
    },

    'cold-springs-nevada-dryer-vent-cleaning': {
        'city': 'Cold Springs',
        'hero_para': "Cold Springs has seen substantial growth as families move northwest of Reno for more space, and that newer construction comes with its own dryer vent challenges. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Cold Springs and the surrounding northwest Washoe County communities, covering tract homes, custom builds, and everything in between.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Cold Springs</strong>, NV and northwest Washoe County with the commercial equipment those longer vent runs demand. Cold Springs homes are mostly newer construction from the 2000s and 2010s, which means vent runs routed through interior walls that can stretch 20 feet or more to reach exterior terminations. A consumer brush kit from a hardware store does not reach the full length of those runs or dislodge packed lint effectively - commercial rotary brush equipment is required. The fine alkali dust common in the Cold Springs basin also works into vent lines through exterior covers, combining with lint to form denser blockages than you would find in urban Reno. We are one of the few dryer vent specialists that regularly services northwest Washoe County.',
        'local_seo_bottom': 'We serve all of Cold Springs and the northwest Washoe County corridor. Same-day and next-day dryer vent cleaning appointments are usually available. <strong>Call 775-224-4136</strong> for your free estimate.',
        'services_h2': 'Cold Springs Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to full vent system repair and safety inspection, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Cold Springs and northwest Washoe County.',
        'why_p1': "We have been doing dryer vent cleaning in Cold Springs since before the area's growth accelerated, and we know what the construction from that era looks like inside. Long interior vent runs, sometimes with added elbows to route around structural elements, are the norm out here. Those configurations require commercial rotary brush equipment to clean effectively. A consumer kit does not reach the full length of a 20-foot run and does not dislodge packed lint the way professional dryer vent cleaning equipment does.",
        'why_p2': 'All technicians are CSIA certified and direct All Star Dryer Vent employees. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Cold Springs</a></strong> includes a full 12-point safety inspection with written findings. If we find a damaged transition, a disconnected joint, or a vent that was routed incorrectly during construction, we document it and give you dryer vent repair options.',
        'why_p3': 'We cover Cold Springs and all of northwest Washoe County. Most jobs can be scheduled within a day or two. Call 775-224-4136 or book online.',
        'benefits': [
            ('Fire Prevention', 'Cold Springs homes with long interior vent runs accumulate lint faster and cannot be fully cleared without commercial equipment. Annual dryer vent cleaning removes the buildup that creates fire risk inside your exhaust duct.'),
            ('Air Quality & Safety', 'A blocked exhaust duct can force carbon monoxide from gas dryers back into your living space. Clean dryer vent airflow keeps combustion byproducts exhausting to the outside as designed.'),
            ('Alkali Dust Accumulation', 'The fine alkali dust in the Cold Springs basin enters vent lines through exterior covers and compounds normal lint buildup. Cold Springs homeowners often see heavier blockages than urban Reno residents because of this additional particulate in the exhaust duct.'),
            ('Energy Efficiency', 'Restricted vent airflow forces your dryer to run extra cycles for each load. After dryer vent cleaning restores proper exhaust flow, Cold Springs homeowners typically see immediate improvement in drying times and monthly energy costs.'),
            ('Appliance Longevity', 'Dryers running against restricted airflow overheat and wear out faster. Regular dryer vent cleaning in Cold Springs protects your appliance investment and delays the cost of replacement by years.'),
            ('Professional Service That Comes Out Here', 'Cold Springs is northwest of Reno and a lot of service providers simply do not make the drive. All Star does - with the same CSIA certified, fully insured, commercial-grade dryer vent cleaning service that Reno homeowners receive.'),
        ],
        'warnings': [
            ('Clothes Needing Multiple Cycles', 'If a standard load requires more than one cycle, restricted exhaust duct airflow is the most common cause. In Cold Springs where vent runs are often long, this symptom appears faster than homeowners expect.'),
            ('Unusually Warm Laundry Room', 'Heat that cannot escape through the exhaust duct builds in the appliance and laundry room. A warm room or a dryer hot to the touch after a cycle is a direct dryer fire warning.'),
            ('Dryer Shutting Off Before Finishing', 'Thermal overload protection stops the dryer when it overheats. Check the exhaust duct before scheduling appliance repair - blocked dryer vent lines cause this far more often than mechanical failure in Cold Springs homes.'),
            ('Damp Clothes After a Full Cycle', 'Moisture that cannot exhaust through a blocked vent stays in your laundry. Clothes come out still damp and develop a musty odor after sitting.'),
            ('Lint Around Vent Connection Points', 'Lint visible at joints or connection points in the vent system behind the dryer means pressure from a clogged line is forcing it out. Professional dryer vent cleaning is needed immediately.'),
            ('No Lint on the Lint Trap', 'If the lint screen looks surprisingly clean after a full load, lint is bypassing the trap and accumulating in the exhaust duct. This counterintuitive sign often precedes more serious blockage.'),
            ('Burning Smell During Drying', 'Any burning odor is an emergency. Stop the dryer and call us. Lint in contact with a hot duct surface or heating element is how dryer fires start.'),
            ('Exterior Cover Blocked by Debris', 'Cold Springs homes with alkali dust and desert debris should check regularly that the exterior vent cover flap opens freely during operation. A blocked termination stops all exhaust airflow through the dryer vent.'),
            ('More Than a Year Since Last Service', 'Annual professional dryer vent cleaning is the standard recommendation from manufacturers and fire safety organizations. If your Cold Springs home has not been serviced in over a year, schedule now.'),
        ],
    },

    'hidden-valley-nevada-dryer-vent-cleaning': {
        'city': 'Hidden Valley',
        'hero_para': "Hidden Valley sits on the southeast edge of Reno with custom homes, gated communities, and properties backing up to open desert - and that desert environment means wind, dust, and wildlife that all affect dryer vent performance. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Hidden Valley and the surrounding southeast Reno neighborhoods.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Hidden Valley</strong> with experience across every vent configuration the area presents. Hidden Valley homes sit on larger lots with more varied architecture than standard subdivisions, which means more variety in how dryer vents were originally routed. We have serviced properties where the vent exits through the crawlspace, through an interior wall to a side-wall termination, and through the roof - each configuration requires different equipment and technique. The proximity to open desert means exterior vent covers collect windblown debris and attract starlings and other cavity-nesting birds. Hidden Valley also sits in a higher wildfire risk zone, making lint removal from exhaust duct lines more urgent here than in lower-risk neighborhoods.',
        'local_seo_bottom': 'We serve Hidden Valley and southeast Reno. Same-day dryer vent cleaning appointments are usually available. <strong>Call 775-224-4136</strong> for your free estimate.',
        'services_h2': 'Hidden Valley Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to custom vent routing inspection and full system repair, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Hidden Valley and southeast Reno.',
        'why_p1': "Hidden Valley's custom home stock means we rarely see the same vent configuration twice. We have worked on vent runs routed through crawlspaces, around utility chases, and up through multi-story interior walls to rooftop exits. The ability to inspect, clean, and repair any of those configurations is what separates a dryer vent specialist from a handyman with a brush kit. Every technician on our crew has years of experience with non-standard vent routing.",
        'why_p2': 'CSIA certified, fully insured, and direct employees - no subcontracting. We carry commercial-grade rotary brush and compressed air equipment that works on any vent configuration. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Hidden Valley</a></strong> includes a written 12-point safety inspection. If your vent has a configuration that previous services called too difficult to clean properly, contact us.',
        'why_p3': 'We cover Hidden Valley and all of southeast Reno. Call 775-224-4136 or book online to schedule dryer vent cleaning, inspection, or repair.',
        'benefits': [
            ('Fire Prevention in a Wildfire Zone', 'Hidden Valley sits in elevated wildfire risk territory. Lint buildup inside your exhaust duct is an internal fire hazard independent of the outdoor environment. Annual dryer vent cleaning removes that risk from inside your home.'),
            ('Air Quality & Safety', 'A blocked vent duct can push carbon monoxide from gas dryers back into living spaces. In well-sealed Hidden Valley homes, combustion gases have nowhere to go if the exhaust path through the dryer vent is restricted.'),
            ('Wildlife & Nest Removal', 'Starlings and other cavity-nesting birds frequently block exterior vent covers in Hidden Valley. A nest-blocked dryer vent is a complete airflow stoppage and fire hazard. We inspect and clear exterior terminations on every visit.'),
            ('Complex Vent Configuration Service', 'Hidden Valley custom homes often have dryer vent routing through crawlspaces, around structural elements, or to rooftop exits. We carry the equipment and expertise to fully clean and inspect all of those configurations.'),
            ('Energy Efficiency', 'Restricted exhaust duct airflow forces your dryer through extra cycles. After dryer vent cleaning restores proper airflow, most Hidden Valley homeowners see immediate improvement in drying times and energy costs.'),
            ('Appliance Longevity', 'Custom homes often have premium appliances worth protecting. Regular dryer vent cleaning prevents the thermal stress and accelerated wear that a restricted exhaust duct causes to heating elements, motors, and electronic controls.'),
        ],
        'warnings': [
            ('Clothes Taking More Than One Cycle', 'Restricted exhaust duct airflow is the leading cause of extended drying times. In Hidden Valley where vent runs are often longer or more complex, this symptom can appear with relatively moderate lint buildup.'),
            ('Laundry Room Running Hot', 'Heat that cannot exit through the exhaust duct stays in the appliance and laundry room. An unusually warm room or dryer exterior after a cycle is a fire warning that should not be ignored.'),
            ('Dryer Overheating and Shutting Off', 'If the dryer stops before finishing a cycle, thermal overload protection is engaging. Have the dryer vent inspected before pursuing appliance repair - blocked exhaust ducts are the most common cause.'),
            ('Damp or Musty-Smelling Laundry', 'Moisture that cannot exhaust through the vent stays in your laundry. Damp clothes after a full cycle and a musty odor are both signs of blocked exhaust duct airflow.'),
            ('Lint or Debris Around Vent Connections', 'Lint visible at any connection point in the dryer vent system indicates pressure is building from a blockage further in the duct. This requires professional dryer vent cleaning immediately.'),
            ('No Airflow at Exterior Termination', 'During a cycle, check your exterior vent exit. No airflow or a flap stuck closed means the duct is blocked. Bird nests are the most common cause in Hidden Valley.'),
            ('Burning Smell During Operation', 'Any burning odor is an emergency. Stop the dryer and call us. Do not restart until the dryer vent has been professionally inspected and cleared.'),
            ('Desert Debris Around Exterior Cover', 'Windblown desert debris around your exterior vent cover can indicate debris has entered the termination. An inspection determines whether it has penetrated into the duct line.'),
            ('More Than One Year Since Last Service', 'Annual dryer vent cleaning is the industry standard. In Hidden Valley where configurations are more complex and wildlife activity is higher, staying on schedule is especially important.'),
        ],
    },

    'lockwood-nv-dryer-vent-cleaning': {
        'city': 'Lockwood',
        'hero_para': "Lockwood is a small community east of Sparks along the Truckee River corridor, and it has a housing stock unlike anywhere else in Washoe County. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Lockwood and the Painted Rock area, including manufactured homes, site-built homes, and rural properties that most service companies do not make the drive out to service.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Lockwood</strong>, NV with the knowledge and equipment that manufactured home vent systems specifically require. A significant portion of Lockwood\'s housing stock is manufactured homes, and those dryer vent systems differ from site-built construction in ways that matter during cleaning. Vent runs are often shorter but tightly routed through narrow cavities, and transitions are more likely to use flexible foil duct that degrades and collapses over time. Exterior terminations sit lower to the ground in manufactured homes, where debris accumulation and pest intrusion are more common. We replace degraded foil transition duct with code-compliant rigid metal duct during the same visit as cleaning. We also serve the site-built homes and rural properties throughout the area.',
        'local_seo_bottom': 'We make the drive to Lockwood and Painted Rock regularly. <strong>Call 775-224-4136</strong> to schedule your dryer vent cleaning or inspection.',
        'services_h2': 'Lockwood Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to foil duct replacement and full system inspection, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Lockwood and east Washoe County.',
        'why_p1': "Most dryer vent cleaning companies in the Reno-Sparks area do not regularly service Lockwood - it falls far enough east that many providers skip it. We make the drive because the homes here need the same professional service as anywhere else. Manufactured home dryer vents are often neglected because owners assume they are too simple to require professional cleaning. They are not. Compressed lint in a 10-foot foil transition duct is just as dangerous as a packed rigid duct run in a site-built home, and foil duct carries the additional risk of collapse that creates a complete airflow blockage.",
        'why_p2': 'CSIA certified technicians, commercial equipment, written 12-point safety inspection on every job. We are familiar with the vent configurations common in manufactured housing, including belly-exit routing and low-profile exterior terminations. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Lockwood</a></strong> includes a full system inspection from dryer connection to exterior termination. If the foil transition duct is degraded or crushed, we replace it with rigid metal duct during the same visit.',
        'why_p3': 'We cover Lockwood, Painted Rock, and the communities along the I-80 corridor east of Sparks. Call 775-224-4136 to get on the schedule.',
        'benefits': [
            ('Fire Prevention in Manufactured Homes', 'Manufactured homes have less fire-resistant construction than site-built homes, making a dryer fire more dangerous. Annual dryer vent cleaning eliminates the lint buildup in the exhaust duct that causes most dryer fires.'),
            ('Foil Duct Replacement', 'Flexible foil transition duct - common in manufactured homes - degrades over time and can collapse, creating a complete airflow blockage. We replace foil duct with rigid metal duct rated for dryer exhaust during the same visit as cleaning.'),
            ('Air Quality & Safety', "A blocked dryer vent can force carbon monoxide from propane or gas dryers back into a manufactured home's interior. Proper exhaust duct airflow keeps combustion byproducts exhausting outside as designed."),
            ('Pest & Debris Intrusion', 'Low-profile exterior vent terminations in manufactured homes are more accessible to rodents, insects, and debris than standard wall exits. We inspect and clear exterior terminations on every dryer vent cleaning visit.'),
            ('Energy Efficiency', 'A clogged vent forces extra cycles and longer run times. Lockwood homeowners see measurable improvement in drying performance and utility costs after dryer vent cleaning restores proper exhaust airflow.'),
            ('Service That Comes Out to Lockwood', 'Most Reno-area providers do not make the drive to Lockwood. All Star does, with the same CSIA certified, commercial-grade, fully insured dryer vent cleaning service available to Reno homeowners.'),
        ],
        'warnings': [
            ('Clothes Not Drying in One Cycle', 'Restricted exhaust duct airflow is the most common reason a standard load requires multiple cycles. In manufactured homes where vent runs are compact, even moderate lint buildup can significantly restrict dryer vent airflow.'),
            ('Dryer or Laundry Area Running Hot', 'Heat trapped by a blocked vent accumulates in the appliance and the surrounding space. In a manufactured home where spaces are smaller, this heat buildup can be more noticeable and more dangerous.'),
            ('Dryer Stopping Mid-Cycle', 'Thermal overload protection engages when the appliance overheats. Have the dryer vent inspected before any other repair - blocked exhaust ducts are the most common cause of this symptom in Lockwood manufactured homes.'),
            ('Damp Laundry After a Full Cycle', 'Moisture that cannot exhaust through a blocked dryer vent remains in your laundry. Persistent dampness after a full drying cycle is a reliable indicator of restricted exhaust duct airflow.'),
            ('Collapsed or Kinked Transition Duct', 'If the flexible duct connecting your dryer to the wall duct is kinked, crushed, or sagging, airflow is severely restricted. This is especially common in manufactured homes where the duct is routed through tight spaces.'),
            ('No Lint on the Lint Screen', 'If the lint trap looks unusually clean after a load, lint is bypassing it and packing into the exhaust duct. This counterintuitive sign often indicates a significant dryer vent blockage has already developed.'),
            ('Burning Smell During Operation', 'Any burning smell is an emergency. Stop the dryer immediately and call us. Lint contacting a hot surface inside the dryer vent system is how dryer fires start.'),
            ('Visible Pest Activity at Vent Opening', 'Rodent tracks, droppings, or chewed material near the exterior vent termination indicate pests have entered the duct. A dryer vent inspection will determine how far the intrusion extends.'),
            ('Unknown Service History', 'Manufactured homes are frequently resold or rented without maintenance documentation. If you do not know when the dryer vent was last professionally cleaned, schedule an inspection now.'),
        ],
    },

    'sun-valley-nv-dryer-vent-cleaning': {
        'city': 'Sun Valley',
        'hero_para': "Sun Valley stretches north of Sparks as an unincorporated community with older site-built homes, manufactured housing, and properties that see some of the dustiest conditions in Washoe County. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Sun Valley, covering the full range of housing types in the area with the same level of professional service.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Sun Valley</strong>, NV for every housing type the area has. Sun Valley\'s housing stock spans 1970s site-built homes with original flexible accordion duct, newer manufactured homes, and rural properties with longer vent runs. Many of the older homes still have original flexible duct that has never been replaced, and that material traps lint at a rate rigid metal duct does not. The area is also notably dusty, with dry desert conditions contributing fine particulate that enters vent lines through exterior covers and accelerates lint accumulation. Homes with dogs, cats, or other pets see even faster buildup - pet hair is a significant accelerant for lint blockage in dryer exhaust duct lines, and we recommend annual service for any household with pets.',
        'local_seo_bottom': 'We serve all of Sun Valley and the surrounding north Sparks unincorporated areas. <strong>Call 775-224-4136</strong> for your free estimate on dryer vent cleaning or inspection.',
        'services_h2': 'Sun Valley Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to duct replacement and full system inspection, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Sun Valley and north Washoe County.',
        'why_p1': "Sun Valley gives us a bit of everything: older site-built homes where the original dryer vent was not ideal to begin with, manufactured homes with foil transition duct past its service life, and rural properties where no one has looked at the vent since installation. We bring the same professional approach to all of it - commercial rotary brush equipment, compressed air, written safety inspection, and honest documentation of what we find inside the exhaust duct.",
        'why_p2': 'Every technician is CSIA certified and on our direct payroll. No subcontracting. When you schedule <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Sun Valley</a></strong> with All Star, you get an experienced technician who inspects the full vent system from dryer connection to exterior termination. If we find a foil transition that needs replacement or an exterior cover breached by wildlife, we handle it during the same appointment.',
        'why_p3': 'We cover Sun Valley and all of north Sparks and unincorporated Washoe County north of the city. Call 775-224-4136 or book online to schedule dryer vent cleaning or a safety inspection.',
        'benefits': [
            ('Fire Prevention', 'Dryers cause thousands of home fires annually, and lint buildup in exhaust duct lines is the primary cause. Annual dryer vent cleaning in Sun Valley removes the packed lint that creates that fire risk inside your home.'),
            ('Air Quality & Safety', 'Gas or propane dryers with blocked dryer vent lines can push carbon monoxide into living areas. Clean exhaust duct airflow keeps combustion gases moving outside as the appliance was designed to do.'),
            ('Dust and Pet Hair Buildup', "Sun Valley's dusty conditions and high rate of pet ownership mean exhaust duct lines accumulate lint, dust, and pet hair faster than in less exposed environments. Annual dryer vent cleaning keeps blockage from reaching hazardous levels."),
            ('Older Duct Material Replacement', 'Many Sun Valley homes still have original flexible accordion duct or foil transition hose that has degraded. We replace those materials with rigid metal duct rated for modern dryer output during the same visit as dryer vent cleaning.'),
            ('Energy Efficiency', 'A clogged dryer vent forces your appliance through additional cycles to dry each load. After dryer vent cleaning restores exhaust airflow, Sun Valley homeowners see direct improvement in drying times and utility costs.'),
            ('Service That Comes Out to Sun Valley', 'Sun Valley is north of Sparks and can feel off the map for some service providers. All Star makes the trip with fully certified, insured, commercial-grade dryer vent cleaning service on every visit.'),
        ],
        'warnings': [
            ('Clothes Needing More Than One Cycle', 'If a standard load does not dry in one cycle, restricted exhaust duct airflow is the most likely cause. In Sun Valley where dust and pet hair accelerate lint buildup, this symptom can develop faster than homeowners expect.'),
            ('Laundry Room or Dryer Overheating', 'Heat that cannot exhaust through the vent duct stays in the appliance and laundry room. A noticeably warm room or hot dryer exterior after a cycle is a fire warning that should not be ignored.'),
            ('Dryer Shutting Down Before Finishing', 'If the dryer stops mid-cycle, thermal overload protection is engaging because the appliance is overheating. Have the dryer vent inspected before calling for appliance repair.'),
            ('Damp Clothes After a Full Cycle', 'Moisture trapped by a blocked dryer vent remains in your laundry. Persistent dampness after a full drying cycle, or a musty smell on dried clothes, points to restricted exhaust duct airflow.'),
            ('Lint Around the Dryer or Connections', 'Lint escaping from behind the dryer or at connection points indicates back-pressure from a blocked vent line. This is a visible sign that professional dryer vent cleaning is needed.'),
            ('Exterior Vent Cover Blocked by Debris', 'Check that your exterior vent termination opens freely during operation. Desert dust, debris, and pest nesting can block the cover flap and stop all exhaust airflow through the dryer vent.'),
            ('Burning Smell During Operation', 'Any burning odor is an emergency. Stop the dryer and call us immediately. Lint in contact with a hot duct surface or heating element is how dryer fires start.'),
            ('Increased Pet Hair on Dried Clothes', 'If dried clothes are coming out with more pet hair than usual, exhaust airflow is not clearing the drum properly. Pet hair combined with lint can create dense blockages in dryer exhaust duct lines.'),
            ('More Than One Year Since Last Service', 'Annual dryer vent cleaning is the manufacturer and fire safety standard. In Sun Valley where dust and pet hair accelerate buildup, staying on an annual schedule is especially important.'),
        ],
    },

    'washoe-valley-nv-dryer-vent-cleaning': {
        'city': 'Washoe Valley',
        'hero_para': "Washoe Valley runs along US-395 between Reno and Carson City, with Washoe Lake at its center and some of the strongest sustained winds in Northern Nevada on its flanks. Since 2013, All Star Dryer Vent has provided dryer vent cleaning in Washoe Valley, serving the rural properties, ranchettes, and residential communities that line the valley floor.",
        'local_seo_para': 'All Star provides professional <strong class="text-slate-900">dryer vent cleaning in Washoe Valley</strong>, NV with an understanding of what the valley\'s unique wind environment does to dryer vent systems. Exterior vent covers take sustained battering that loosens flap mechanisms and allows debris entry. Properties oriented toward the prevailing wind can experience back-pressure in vent lines during high-wind events, reducing effective exhaust airflow even on a clean system. The valley\'s rural character means a mix of construction types, with propane dryers not uncommon on larger lots. Rooftop vent exits are more frequent here than in urban Reno due to home orientation on valley-floor lots, and those terminations are especially prone to ice and debris damage that requires post-winter dryer vent inspection.',
        'local_seo_bottom': 'We serve Washoe Valley, Eastlake, and the communities along the US-395 corridor between Reno and Carson City. <strong>Call 775-224-4136</strong> for your free estimate.',
        'services_h2': 'Washoe Valley Dryer Vent Cleaning &amp; Repair Services',
        'services_intro': 'From dryer vent cleaning to rooftop vent inspection and full system repair, we offer Northern Nevada\'s most comprehensive <a href="../../services" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent services</a> for Washoe Valley and the US-395 corridor.',
        'why_p1': "Washoe Valley properties often have dryer vent systems that show the effects of the local wind environment - damaged exterior covers, flap mechanisms forced open or sealed shut, and lint accumulation patterns affected by back-pressure from opposing gusts. We know what wind-related dryer vent damage looks like and how to address it. We have serviced properties throughout the valley, from the communities near Bowers Mansion to rural spreads on the eastern bench above Washoe Lake.",
        'why_p2': 'CSIA certified, direct employees, commercial rotary brush and compressed air equipment, written 12-point inspection on every job. Every <strong><a href="https://g.page/r/CbCW4WjBLs9_EBM/review" target="_blank" rel="noopener" class="text-blue-900 font-bold underline hover:text-red-600 transition">dryer vent cleaning in Washoe Valley</a></strong> includes an exterior termination check for wind damage and, for rooftop exits, ice damage inspection after winter. If your propane dryer system has never been professionally serviced or your foil transition duct is past its service life, we handle both during the same visit.',
        'why_p3': 'We cover all of Washoe Valley and the US-395 corridor between Reno and Carson City. Call 775-224-4136 or book online to schedule dryer vent cleaning, inspection, or repair.',
        'benefits': [
            ('Fire Prevention', 'Lint buildup in exhaust duct lines is the primary cause of dryer fires. Annual dryer vent cleaning in Washoe Valley removes that fuel source before it becomes a hazard inside your home.'),
            ('Wind Damage to Exterior Covers', "Washoe Valley's sustained winds regularly damage exterior vent covers and flap mechanisms. A damaged flap restricts exhaust airflow or allows debris entry into the dryer vent line. We inspect and replace exterior terminations on every cleaning visit."),
            ('Air Quality & Carbon Monoxide', 'Rural Washoe Valley properties with propane dryers face carbon monoxide backflow risk if the exhaust duct is blocked. Clean dryer vent airflow is essential for combustion safety in any gas or propane dryer installation.'),
            ('Rooftop Vent Inspection', 'Rooftop vent exits are more common in Washoe Valley due to home orientation on valley-floor lots. Those terminations are prone to ice sealing and debris accumulation after winter and should be inspected as part of annual dryer vent service.'),
            ('Energy Efficiency', 'Restricted exhaust airflow forces extra cycles for each load. After dryer vent cleaning restores proper airflow, Washoe Valley homeowners see direct improvement in drying performance and monthly utility costs.'),
            ('Appliance Longevity', 'Dryers running against restricted airflow overheat and fail sooner. In a rural setting where appliance delivery and repair involve extra time and cost, protecting your equipment with annual dryer vent maintenance is straightforward preventative care.'),
        ],
        'warnings': [
            ('Clothes Not Drying Fully in One Cycle', 'Restricted exhaust duct airflow is the most common cause of extended drying times. In Washoe Valley where wind can create back-pressure in vent lines, this symptom can appear even before significant lint buildup has occurred.'),
            ('Laundry Room Running Hot', 'Heat trapped by a blocked dryer vent accumulates in the appliance and laundry room. A warm room or a dryer hot to the touch after a cycle is a direct fire warning.'),
            ('Dryer Stopping Mid-Cycle', 'Thermal overload protection shuts down the dryer when it overheats. Have the dryer vent inspected before scheduling appliance repair - blocked exhaust ducts are the most common cause of this symptom.'),
            ('Damp Laundry or Musty Smell', 'Moisture that cannot exhaust through a blocked dryer vent remains in your laundry. Clothes that are still damp after a full cycle, or carry a musty odor, point to restricted exhaust duct airflow.'),
            ('Lint Escaping at Vent Connections', 'Lint visible at connection points in the dryer vent system indicates back-pressure from a clogged duct. This requires professional dryer vent cleaning immediately.'),
            ('Damaged or Missing Exterior Cover', 'High winds in Washoe Valley routinely break exterior vent cover flaps or blow covers off completely. A missing or broken cover allows unrestricted debris entry into the dryer vent duct and needs replacement.'),
            ('Burning Smell During Operation', 'Any burning odor is an emergency. Stop the dryer and call us. Lint in contact with a hot duct surface or heating element is how dryer fires start.'),
            ('Post-Winter Rooftop Vent Check', 'If your home has a rooftop dryer vent exit, inspect it after each winter season. Ice can seal the termination shut, and winter debris accumulation may partially block the opening even after ice clears.'),
            ('More Than One Year Since Last Service', 'Annual dryer vent cleaning is the manufacturer and fire safety standard. If your Washoe Valley property has not been professionally serviced in over a year, schedule now.'),
        ],
    },
}


def benefits_html(items):
    cards = []
    for title, desc in items:
        cards.append(
            '                <div class="bg-slate-50 p-8 rounded-3xl border border-slate-100">\n'
            f'                    <h4 class="text-xl font-black text-blue-900 uppercase mb-3">{title}</h4>\n'
            f'                    <p class="text-slate-600 leading-relaxed">{desc}</p>\n'
            '                </div>'
        )
    return '\n'.join(cards)


def warnings_html(items):
    cards = []
    for title, desc in items:
        cards.append(
            '                <div class="bg-white/10 backdrop-blur p-6 rounded-2xl border border-white/20">\n'
            '                    <div class="flex items-start gap-4">\n'
            '                        <div>\n'
            f'                            <h4 class="text-lg font-black text-white uppercase mb-2">{title}</h4>\n'
            f'                            <p class="text-slate-300 text-sm">{desc}</p>\n'
            '                        </div>\n'
            '                    </div>\n'
            '                </div>'
        )
    return '\n'.join(cards)


def process(slug, data):
    path = os.path.join(BASE, slug, 'index.html')
    with open(path, encoding='utf-8') as f:
        html = f.read()
    orig = html
    city = data['city']

    # 1. Remove trophy emoji
    html = html.replace('\U0001f3c6 Locally Owned & Operated', 'Locally Owned & Operated')

    # 2. Fix rolling text - Cleaning first
    html = re.sub(
        r'(<div class="rolling-text[^"]*"[^>]*>\s*\n\s*)<span>Restoration</span>(\s*\n\s*<span>Cleaning</span>)',
        r'\1<span>Cleaning</span>\2'.replace('Cleaning</span>', 'Restoration</span>'),
        html
    )
    # safer rolling text fix
    html = re.sub(
        r'<span>Restoration</span>(\s*\n\s*)<span>Cleaning</span>(\s*\n\s*<span>Repairs</span>)',
        r'<span>Cleaning</span>\1<span>Restoration</span>\2<span>Repairs</span>',
        html
    )

    # 3. Hero paragraph
    html = re.sub(
        r'<p class="text-xl text-slate-600 leading-relaxed max-w-xl font-medium">\s*.*?\s*</p>',
        (f'<p class="text-xl text-slate-600 leading-relaxed max-w-xl font-medium">\n'
         f'                    {data["hero_para"]}\n'
         f'                </p>'),
        html, flags=re.DOTALL, count=1
    )

    # 4. Local SEO paragraph (first text-lg paragraph)
    html = re.sub(
        r'<p class="text-lg text-slate-600 leading-relaxed">.*?</p>',
        f'<p class="text-lg text-slate-600 leading-relaxed">{data["local_seo_para"]}</p>',
        html, flags=re.DOTALL, count=1
    )

    # 5. Local SEO bottom paragraph
    html = re.sub(
        r'<p class="text-slate-600">(?:Serving|We carry|We serve)[^<]*(?:<strong>[^<]*</strong>[^<]*)?\s*</p>',
        f'<p class="text-slate-600">{data["local_seo_bottom"]}</p>',
        html, flags=re.DOTALL, count=1
    )

    # 6. Services H2
    html = re.sub(
        r'<h2 class="text-4xl md:text-5xl font-black text-blue-900 tracking-tighter uppercase font-black font-black">[^<]+(?:Premier Restoration Experts|Restoration Experts)[^<]*</h2>',
        f'<h2 class="text-4xl md:text-5xl font-black text-blue-900 tracking-tighter uppercase font-black font-black">{data["services_h2"]}</h2>',
        html
    )

    # 7. Services intro paragraph
    html = re.sub(
        r'<p class="text-slate-600 max-w-2xl mx-auto mt-4 font-black">From professional cleaning.*?</p>',
        f'<p class="text-slate-600 max-w-2xl mx-auto mt-4 font-black">{data["services_intro"]}</p>',
        html, flags=re.DOTALL, count=1
    )

    # 8. Benefits cards (grid gap-8 inside benefits section)
    new_benefits = '\n' + benefits_html(data['benefits']) + '\n            '
    html = re.sub(
        r'(<!-- BENEFITS SECTION -->.*?<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">)'
        r'.*?'
        r'(</div>\s*</div>\s*</section>\s*<!-- WARNING)',
        lambda m: m.group(1) + new_benefits + m.group(2),
        html, flags=re.DOTALL, count=1
    )

    # 9. Warning sign cards (grid gap-6)
    new_warnings = '\n' + warnings_html(data['warnings']) + '\n            '
    html = re.sub(
        r'(<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">)'
        r'.*?'
        r'(</div>\s*<div class="text-center mt-12">)',
        lambda m: m.group(1) + new_warnings + m.group(2),
        html, flags=re.DOTALL, count=1
    )

    # 10. Why [City] Trusts Us paragraphs
    html = re.sub(
        r'(<div class="space-y-4 text-slate-600 leading-relaxed">)'
        r'.*?'
        r'(</div>\s*<div class="mt-8 flex gap-8">)',
        lambda m: (
            m.group(1) + '\n'
            f'                    <p>{data["why_p1"]}</p>\n'
            f'                    <p>{data["why_p2"]}</p>\n'
            f'                    <p>{data["why_p3"]}</p>\n'
            '                ' + m.group(2)
        ),
        html, flags=re.DOTALL, count=1
    )

    if html != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


results = {}
for slug, data in LOCATIONS.items():
    try:
        changed = process(slug, data)
        results[slug] = 'UPDATED' if changed else 'NO CHANGE'
    except Exception as e:
        results[slug] = f'ERROR: {e}'

out_path = r'C:\Users\rusty\allstardryervent_clone\location_update_results.txt'
with open(out_path, 'w', encoding='utf-8') as f:
    for slug, status in results.items():
        f.write(f'{slug}: {status}\n')

print('Done')
