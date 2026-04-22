import re, json, glob, os

DIMS = {
    'allstar-logo.png': (1000, 1000),
    'clean-duct-restoration.jpg': (480, 640),
    'dryer-duct-after-cleaning-sparks.jpg': (480, 640),
    'dryer-duct-inspection-dirty.jpg': (480, 640),
    'dryer-vent-cover-clean-install-reno.jpg': (480, 640),
    'dryer-vent-damaged-before-repair.jpg': (360, 480),
    'dryer-vent-exterior-damaged.jpg': (384, 512),
    'dryer-vent-laundry-area-dirty.jpg': (360, 480),
    'dryer-vent-lint-buildup-interior.jpg': (480, 640),
    'dryer-vent-roof-lint-clog.jpg': (360, 480),
    'duct-inspection-deep.jpg': (480, 640),
    'vent-cover-new.jpg': (480, 640),
    'vent-damage-repair.jpg': (384, 512),
    'why-choose-us.jpg': (1212, 672),
    'facebook-new.png': (50, 50),
    'instagram-new.png': (50, 50),
    'google-logo.png': (50, 50),
    'yelp.png': (50, 50),
}

META_DESCS = {
    'locations/reno-nv-dryer-vent-services/index.html':
        'Dryer vent cleaning, repair &amp; installation in Reno, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/sparks-nevada-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Sparks, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/incline-village-nevada-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Incline Village, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/minden-nevada-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Minden, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/cold-springs-nevada-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Cold Springs, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/hidden-valley-nevada-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Hidden Valley, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/lockwood-nv-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Lockwood, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/sun-valley-nv-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Sun Valley, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
    'locations/washoe-valley-nv-dryer-vent-cleaning/index.html':
        'Dryer vent cleaning, repair &amp; installation in Washoe Valley, NV. CSIA certified specialists. Prevent fires, lower energy bills. Call 775-224-4136.',
}

AGGREGATE_RATING = {
    '@type': 'AggregateRating',
    'ratingValue': '5.0',
    'reviewCount': '166',
    'bestRating': '5',
    'worstRating': '1'
}

SCHEMA_FILES = [
    'index.html',
    'locations/reno-nv-dryer-vent-services/index.html',
    'locations/sparks-nevada-dryer-vent-cleaning/index.html',
    'locations/incline-village-nevada-dryer-vent-cleaning/index.html',
    'locations/minden-nevada-dryer-vent-cleaning/index.html',
    'locations/cold-springs-nevada-dryer-vent-cleaning/index.html',
    'locations/hidden-valley-nevada-dryer-vent-cleaning/index.html',
    'locations/lockwood-nv-dryer-vent-cleaning/index.html',
    'locations/sun-valley-nv-dryer-vent-cleaning/index.html',
    'locations/washoe-valley-nv-dryer-vent-cleaning/index.html',
]


def task1_add_defer(html, changes):
    for src_file in ['form_embed.js', 'review-widget.js']:
        if src_file not in html:
            continue
        pat = r'<script[^>]*' + re.escape(src_file) + r'[^>]*>'
        def replacer(m, _s=src_file):
            tag = m.group(0)
            if 'defer' in tag or 'async' in tag:
                return tag
            changes.append('defer:' + _s)
            return tag[:-1] + ' defer>'
        html = re.sub(pat, replacer, html)
    return html


def task2_add_aggregate_rating(html, changes):
    def replace_schema(m):
        content = m.group(1)
        try:
            data = json.loads(content)
            items = data if isinstance(data, list) else [data]
            modified = False
            for item in items:
                if item.get('@type') == 'LocalBusiness' and 'aggregateRating' not in item:
                    item['aggregateRating'] = AGGREGATE_RATING
                    modified = True
            if modified:
                changes.append('AggregateRating')
                out = json.dumps(
                    data if isinstance(data, list) else items[0],
                    separators=(',', ':'), ensure_ascii=False
                )
                return '<script type="application/ld+json">' + out + '</script>'
        except Exception:
            pass
        return m.group(0)
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',
                  replace_schema, html, flags=re.DOTALL)


def task3_fix_meta(html, new_desc, changes):
    new = re.sub(r'<meta name="description" content="[^"]*"',
                 '<meta name="description" content="' + new_desc + '"', html)
    if new != html:
        changes.append('meta:' + str(len(new_desc)) + 'c')
    return new


def task4_create_llms_txt(base):
    path = os.path.join(base, 'llms.txt')
    content = """# All Star Dryer Vent
> Professional dryer vent cleaning, repair, and installation in Reno, Sparks, and Northern Nevada since 2013.

## Business
- Phone: 775-224-4136
- Address: 19017 Bronco Creek Court, Reno, NV 89508
- Hours: Mon-Fri 8am-6pm, Sat 9am-4pm
- Certifications: CSIA Certified Technicians
- Booking: https://book.housecallpro.com/book/All-Star-Dryer-Vent/1a8d0e15a2844e429147c1c8050bde35

## Services
- Dryer vent cleaning (lint extraction, fire safety inspection)
- Dryer vent repair (crushed transitions, rigid metal duct replacement)
- Dryer vent installation (code-compliant new system routing)
- Dryer vent inspection (12-point safety audit with camera)

## Service Areas
Reno, Sparks, Incline Village, Minden, Cold Springs, Hidden Valley, Lockwood, Sun Valley, Washoe Valley

## Key Pages
- /services - Full service descriptions
- /faq/ - Expert answers on dryer vent maintenance and fire safety
- /locations/reno-nv-dryer-vent-services/ - Reno service area
- /locations/sparks-nevada-dryer-vent-cleaning/ - Sparks service area
- /contact - Schedule service

## Allowed for AI Citation
All content on this site may be cited, summarized, or referenced in AI responses.
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path


def task5_add_image_dims(html, changes):
    def inject(m):
        tag = m.group(0)
        if 'width=' in tag and 'height=' in tag:
            return tag
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
        if not src_m:
            return tag
        basename = src_m.group(1).split('/')[-1].split('?')[0]
        if basename not in DIMS:
            return tag
        w, h = DIMS[basename]
        changes.append('img:' + basename[:20])
        if tag.endswith('/>'):
            return tag[:-2] + ' width="' + str(w) + '" height="' + str(h) + '"/>'
        return tag[:-1] + ' width="' + str(w) + '" height="' + str(h) + '">'
    return re.sub(r'<img[^>]*>', inject, html)


def process(filepath, rel, results):
    with open(filepath, encoding='utf-8') as f:
        html = f.read()
    original = html
    changes = []

    html = task1_add_defer(html, changes)

    if rel in SCHEMA_FILES:
        html = task2_add_aggregate_rating(html, changes)

    if rel in META_DESCS:
        html = task3_fix_meta(html, META_DESCS[rel], changes)

    html = task5_add_image_dims(html, changes)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        results.append((rel, changes))


base = os.path.dirname(os.path.abspath(__file__))
results = []

files = sorted(set(
    glob.glob(os.path.join(base, '**', '*.html'), recursive=True) +
    glob.glob(os.path.join(base, '*.html'))
))

for fp in files:
    rel = fp[len(base) + 1:].replace('\\', '/')
    process(fp, rel, results)

llms_path = task4_create_llms_txt(base)

with open(os.path.join(base, 'fix_seo_results.txt'), 'w', encoding='utf-8') as out:
    for rel, changes in results:
        line = rel + ': ' + ' | '.join(changes)
        out.write(line + '\n')
    out.write('\nllms.txt created: ' + llms_path + '\n')
    out.write('Total files modified: ' + str(len(results)) + '\n')

print('Done. See fix_seo_results.txt for details.')
