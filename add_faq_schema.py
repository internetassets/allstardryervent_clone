# -*- coding: utf-8 -*-
import os, json

base = r'C:\Users\rusty\allstardryervent_clone'

FAQ_DATA = {
    'reno-nv-dryer-vent-services': {
        'city': 'Reno',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Reno?',
                'a': "Reno's high desert climate means dryer vents should be cleaned every 12-18 months. Homes near Caughlin Ranch and south Reno often have longer vent runs due to ranch-style layouts, which accumulate lint faster. Households with pets or heavy laundry use should schedule annual service."
            },
            {
                'q': 'What does dryer vent cleaning cost in Reno, NV?',
                'a': 'Dryer vent cleaning in Reno typically costs $89-$149. Price varies based on vent length, roof versus wall termination, and whether significant buildup requires additional time. All Star Dryer Vent provides upfront pricing before any work begins.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Reno?',
                'a': 'Most Reno dryer vent cleanings take 45-90 minutes. Longer vent runs common in Reno ranch homes or multi-story properties may take slightly longer. Our CSIA-certified technicians work efficiently to minimize disruption to your day.'
            },
            {
                'q': 'Can a clogged dryer vent cause a fire in Reno homes?',
                'a': "Yes. Lint is highly flammable, and Reno's dry climate increases ignition risk. The U.S. Fire Administration reports nearly 3,000 dryer fires annually nationwide. Annual professional cleaning is the most effective prevention, and All Star Dryer Vent has served Reno since 2013."
            },
            {
                'q': 'What are the signs of a clogged dryer vent?',
                'a': 'Key signs include clothes taking two or more cycles to dry, the dryer exterior running hot to the touch, a burning smell during operation, excessive lint around the exterior vent flap, or the dryer shutting off mid-cycle due to overheating. If you notice any of these, call All Star Dryer Vent at 775-224-4136.'
            }
        ]
    },
    'sparks-nevada-dryer-vent-cleaning': {
        'city': 'Sparks',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Sparks?',
                'a': 'Sparks homes, especially in Spanish Springs and newer subdivisions, often have longer vent runs due to two-story construction. We recommend professional dryer vent cleaning every 12 months for most Sparks households, and more frequently for homes with pets or large families.'
            },
            {
                'q': 'What does dryer vent cleaning cost in Sparks, NV?',
                'a': 'Dryer vent cleaning in Sparks is typically $89-$149. Homes with roof terminations or extended duct runs in Spanish Springs two-story builds may be at the higher end of the range. All Star Dryer Vent offers transparent, upfront pricing with no surprises.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Sparks?',
                'a': 'Most Sparks dryer vent cleanings are completed in 45-90 minutes. Newer two-story construction in Spanish Springs may run longer depending on how the duct is routed through the home.'
            },
            {
                'q': 'Can a clogged dryer vent cause a fire in Sparks homes?',
                'a': "Yes. Sparks shares Reno's high-desert fire risk. Lint buildup in longer duct runs found in Spanish Springs and newer Sparks subdivisions can become a serious hazard if not cleaned annually. Our CSIA-certified technicians eliminate that risk."
            },
            {
                'q': 'What are signs my dryer vent needs cleaning in Sparks?',
                'a': 'Watch for clothes still damp after a full cycle, a laundry room that feels unusually warm, a burning or musty smell during operation, or visible lint buildup around the exterior vent cover. These are all signs the vent is restricted and needs professional attention.'
            }
        ]
    },
    'incline-village-nevada-dryer-vent-cleaning': {
        'city': 'Incline Village',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Incline Village?',
                'a': 'Incline Village homes near Lake Tahoe often have complex vent routing due to alpine construction styles. We recommend cleaning every 12 months. Lint accumulates faster in longer or angled duct runs common in Tahoe-area properties.'
            },
            {
                'q': 'What does dryer vent cleaning cost in Incline Village?',
                'a': 'Dryer vent cleaning in Incline Village typically costs $89-$149. Tight attic spaces or roof terminations common in Tahoe-area construction may affect the final price. All Star Dryer Vent provides a clear quote before beginning any work.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Incline Village?',
                'a': 'Expect 60-90 minutes for most Incline Village homes. Alpine construction styles often feature more complex duct configurations than flatland properties, so our technicians take the time to do the job thoroughly.'
            },
            {
                'q': 'Is a clogged dryer vent a fire hazard in Incline Village?',
                'a': 'Absolutely. In a forested alpine environment like Incline Village, any interior fire risk is especially serious. Regular dryer vent cleaning is a critical safety step for Tahoe-area homeowners. All Star Dryer Vent is CSIA certified and serves Incline Village year-round.'
            },
            {
                'q': 'What are signs of a clogged dryer vent in Incline Village?',
                'a': 'If your dryer takes multiple cycles to dry a single load, if you notice a musty or burning odor during operation, or if the dryer cabinet feels hot to the touch after a cycle, your vent likely needs cleaning. Call 775-224-4136 to schedule service.'
            }
        ]
    },
    'minden-nevada-dryer-vent-cleaning': {
        'city': 'Minden',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Minden?',
                'a': "Carson Valley homes in Minden typically have straightforward single-story vent configurations, but the high desert conditions and agricultural dust mean annual dryer vent cleaning is still recommended. Most Minden homeowners schedule service once a year."
            },
            {
                'q': 'What does dryer vent cleaning cost in Minden, NV?',
                'a': 'Dryer vent cleaning in Minden typically costs $89-$149. Single-story ranch homes with short duct runs are often at the lower end of the range. All Star Dryer Vent serves Minden with the same transparent pricing offered throughout Northern Nevada.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Minden?',
                'a': 'Most Minden dryer vent cleanings are completed in 45-75 minutes. Carson Valley ranch homes with straightforward vent runs are among the more efficient jobs our technicians perform.'
            },
            {
                'q': 'Can a clogged dryer vent cause a fire in Minden?',
                'a': "Yes. Minden's dry Carson Valley climate increases combustion risk. Lint is highly flammable, and even a short duct run can accumulate dangerous buildup within a year. All Star Dryer Vent's CSIA-certified technicians serve Minden and the surrounding Carson Valley."
            },
            {
                'q': 'What are signs of a clogged dryer vent in Minden?',
                'a': 'Signs include longer drying times, a hot dryer exterior cabinet after a cycle, lint collecting around the exterior termination cap, or a burning smell during operation. These indicate restricted airflow that needs professional attention.'
            }
        ]
    },
    'cold-springs-nevada-dryer-vent-cleaning': {
        'city': 'Cold Springs',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Cold Springs?',
                'a': 'Cold Springs homes, many built in the 1990s and 2000s with longer interior duct runs, should have dryer vents cleaned every 12 months. Older vent systems in Cold Springs may have flexible foil ducting that restricts airflow and needs more frequent attention.'
            },
            {
                'q': 'What does dryer vent cleaning cost in Cold Springs, NV?',
                'a': 'Dryer vent cleaning in Cold Springs is typically $89-$149. Tract homes with side-wall terminations are generally straightforward to service and fall toward the lower end of the range. All Star Dryer Vent provides upfront pricing before starting any work.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Cold Springs?',
                'a': 'Most Cold Springs dryer vent cleanings take 45-75 minutes. Our CSIA-certified technicians handle the job efficiently so you can get back to your day.'
            },
            {
                'q': 'Is a clogged dryer vent dangerous in Cold Springs?',
                'a': "Yes. Lint buildup is the leading cause of residential dryer fires. Cold Springs' rapid residential growth means many homes have dryer vents that have never been professionally cleaned. All Star Dryer Vent has served Cold Springs since 2013."
            },
            {
                'q': 'What are signs I need dryer vent cleaning in Cold Springs?',
                'a': 'Look for damp clothes after a full drying cycle, a laundry area that is warmer than usual, visible lint accumulation at the exterior vent, or a burning smell when the dryer runs. Any of these signals restricted airflow that needs immediate attention.'
            }
        ]
    },
    'hidden-valley-nevada-dryer-vent-cleaning': {
        'city': 'Hidden Valley',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Hidden Valley?',
                'a': "Hidden Valley's hillside homes often have longer or angled duct runs to reach exterior walls. Annual dryer vent cleaning is recommended to prevent lint buildup in these configurations. Homes with pets or heavy laundry use should schedule service every 12 months without exception."
            },
            {
                'q': 'What does dryer vent cleaning cost in Hidden Valley?',
                'a': 'Dryer vent cleaning in Hidden Valley typically costs $89-$149. Homes with roof terminations or more complex duct routing through hillside construction may be at the higher end. All Star Dryer Vent gives you a clear price upfront before any work begins.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Hidden Valley?',
                'a': "Expect 60-90 minutes depending on duct length and routing. Hidden Valley's hillside construction often means longer or angled runs compared to flatland neighborhoods, so our technicians take the time to clear the entire system thoroughly."
            },
            {
                'q': 'Can a clogged dryer vent cause a fire in Hidden Valley homes?',
                'a': 'Yes. Hillside homes with longer vent runs are at elevated risk because lint accumulates in bends and transitions in the ductwork. Regular professional cleaning is especially important for Hidden Valley properties. All Star Dryer Vent is CSIA certified and serves Hidden Valley year-round.'
            },
            {
                'q': 'What are signs of a clogged dryer vent in Hidden Valley?',
                'a': 'Multiple drying cycles needed for one load, a dryer exterior that is hot to the touch after a cycle, or lint building up around the outdoor vent cover are all signs of restriction. Call All Star Dryer Vent at 775-224-4136 to schedule a cleaning.'
            }
        ]
    },
    'lockwood-nv-dryer-vent-cleaning': {
        'city': 'Lockwood',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Lockwood?',
                'a': "Lockwood's rural properties and manufactured homes often have unique dryer vent configurations. Annual inspection and cleaning is recommended for all Lockwood households. Manufactured homes in particular can have shorter but more restrictive duct paths."
            },
            {
                'q': 'What does dryer vent cleaning cost in Lockwood, NV?',
                'a': 'Dryer vent cleaning in Lockwood is typically $89-$149. Manufactured homes may have shorter duct runs at the lower end, while larger rural properties can vary based on configuration. All Star Dryer Vent serves Lockwood with straightforward, transparent pricing.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Lockwood?',
                'a': 'Most Lockwood dryer vent cleanings are completed in 45-75 minutes. Our CSIA-certified technicians travel to Lockwood and handle the service efficiently from start to finish.'
            },
            {
                'q': 'Is dryer vent cleaning especially important for Lockwood manufactured homes?',
                'a': 'Yes. Manufactured homes can be especially vulnerable to dryer fires due to construction materials and tighter duct configurations. Keeping the vent clear and unobstructed is a critical safety measure for Lockwood homeowners. All Star Dryer Vent has the specialized experience to handle manufactured home vent systems.'
            },
            {
                'q': 'What are signs my dryer vent is clogged in Lockwood?',
                'a': 'Watch for damp clothes after a full cycle, a burning smell during operation, the dryer shutting off mid-cycle due to overheating, or lint visible at the exterior vent termination. These are all warning signs that need prompt attention.'
            }
        ]
    },
    'sun-valley-nv-dryer-vent-cleaning': {
        'city': 'Sun Valley',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Sun Valley?',
                'a': 'Sun Valley homes, many of which are single-story with side-wall terminations, should have dryer vents cleaned every 12-18 months. Households with pets, large families, or frequent laundry use should schedule annual service to maintain safe airflow.'
            },
            {
                'q': 'What does dryer vent cleaning cost in Sun Valley, NV?',
                'a': 'Dryer vent cleaning in Sun Valley is typically $89-$149. Straightforward single-story configurations common in Sun Valley are generally at the lower end of the range. All Star Dryer Vent provides upfront pricing with no hidden fees.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Sun Valley?',
                'a': 'Most Sun Valley dryer vent cleanings take 45-75 minutes. Single-story homes with standard side-wall venting are among the more efficient service calls our CSIA-certified technicians handle.'
            },
            {
                'q': 'Can a clogged dryer vent cause a fire in Sun Valley?',
                'a': "Yes. Lint is highly flammable regardless of home size or vent length. Sun Valley's dry high-desert climate makes regular dryer vent cleaning especially important. The U.S. Fire Administration reports nearly 3,000 dryer fires annually, and All Star Dryer Vent has kept Northern Nevada homes safe since 2013."
            },
            {
                'q': 'What are signs of a clogged dryer vent in Sun Valley?',
                'a': 'If drying takes two cycles instead of one, the dryer exterior feels hot after a cycle, or lint is visible around the exterior vent opening, it is time for a professional cleaning. Call All Star Dryer Vent at 775-224-4136 to schedule service in Sun Valley.'
            }
        ]
    },
    'washoe-valley-nv-dryer-vent-cleaning': {
        'city': 'Washoe Valley',
        'faqs': [
            {
                'q': 'How often should dryer vents be cleaned in Washoe Valley?',
                'a': "Washoe Valley's rural properties and custom homes often have longer or non-standard vent runs. Annual dryer vent cleaning is strongly recommended. Properties near Washoe Lake or in the valley foothills may have unique configurations that benefit from inspection each year."
            },
            {
                'q': 'What does dryer vent cleaning cost in Washoe Valley?',
                'a': 'Dryer vent cleaning in Washoe Valley typically costs $89-$149. Rural properties with extended duct runs or custom home configurations may be at the higher end of the range. All Star Dryer Vent serves Washoe Valley with the same transparent pricing offered throughout Northern Nevada.'
            },
            {
                'q': 'How long does dryer vent cleaning take in Washoe Valley?',
                'a': 'Expect 60-90 minutes for most Washoe Valley properties. Custom homes can have more complex dryer vent configurations than standard residential builds, and our CSIA-certified technicians take the time to clear the entire system.'
            },
            {
                'q': 'Is dryer vent cleaning especially important in rural Washoe Valley?',
                'a': "Yes. In a rural area like Washoe Valley where fire response times can be longer than in urban Reno or Sparks, preventing dryer fires through regular maintenance is especially critical. All Star Dryer Vent has served Washoe Valley homeowners since 2013."
            },
            {
                'q': 'What are signs of a clogged dryer vent in Washoe Valley?',
                'a': 'Watch for extended drying times requiring multiple cycles, a burning smell during operation, the dryer overheating and shutting off, or lint accumulation at the exterior termination cap. These are warning signs that should not be ignored. Call 775-224-4136 to schedule service.'
            }
        ]
    }
}

def build_faq_schema(faqs):
    entities = []
    for item in faqs:
        entities.append({
            '@type': 'Question',
            'name': item['q'],
            'acceptedAnswer': {
                '@type': 'Answer',
                'text': item['a']
            }
        })
    schema = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': entities
    }
    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

TARGET_SUFFIX = '"worstRating":"1"}}]</script>'

updated = 0
for slug, data in FAQ_DATA.items():
    fp = os.path.join(base, 'locations', slug, 'index.html')
    if not os.path.exists(fp):
        print('NOT FOUND: ' + fp)
        continue

    with open(fp, encoding='utf-8') as f:
        html = f.read()

    if 'FAQPage' in html:
        print('SKIP (already has FAQPage): ' + slug)
        continue

    faq_json = build_faq_schema(data['faqs'])
    new_suffix = '"worstRating":"1"}},' + faq_json + ']</script>'
    new_html = html.replace(TARGET_SUFFIX, new_suffix, 1)

    if new_html == html:
        print('PATTERN NOT FOUND: ' + slug)
        continue

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Updated: ' + slug)
    updated += 1

print('Total updated: ' + str(updated))
