# -*- coding: utf-8 -*-
import glob, os, re

base = r'C:\Users\rusty\allstardryervent_clone'

# WebP image pools by semantic category
# All images are Screenshot_20230129_XXXXXX.webp
def wp(t): return 'Screenshot_20230129_' + t + '.webp'

POOLS = {
    # Heavy lint clogs - cleaning before shots
    'clog': [wp('031657'), wp('031924'), wp('032301'), wp('032522'), wp('032542')],
    # Exterior vent issues
    'exterior': [wp('032318'), wp('032344'), wp('032301'), wp('031657'), wp('032601')],
    # Roof vent clogs
    'roof': [wp('032542'), wp('032601'), wp('031924'), wp('032318'), wp('031657')],
    # Inside dryer / appliance lint
    'interior': [wp('031844'), wp('031857'), wp('033001'), wp('033131'), wp('031844')],
    # After cleaning - debris result
    'result': [wp('032110'), wp('032821'), wp('032942'), wp('031818'), wp('032110')],
    # Damaged / improper ductwork - repair
    'repair': [wp('032145'), wp('032219'), wp('032246'), wp('032759'), wp('032901'), wp('033053'), wp('033036'), wp('032128')],
    # New installation / clean vent cap
    'install': [wp('032433'), wp('032457'), wp('032840'), wp('032433'), wp('032457')],
    # Inspection
    'inspect': [wp('032840'), wp('031747'), wp('032409'), wp('033016'), wp('032923')],
}

# Counters cycle independently per pool
counters = {k: 0 for k in POOLS}

def next_img(pool_name):
    pool = POOLS[pool_name]
    img = pool[counters[pool_name] % len(pool)]
    counters[pool_name] += 1
    return img

# JPEG → (pool, alt_service_cycle)
# alt_service_cycle: list of service labels to rotate through
JPEG_MAP = {
    'dryer-vent-roof-lint-clog.jpg':        ('roof',     ['Cleaning', 'Restoration', 'Cleaning', 'Inspection']),
    'duct-inspection-deep.jpg':             ('inspect',  ['Inspection', 'Repair', 'Cleaning', 'Inspection']),
    'vent-damage-repair.jpg':               ('repair',   ['Repair', 'Restoration', 'Repair', 'Restoration']),
    'dryer-vent-cover-clean-install-reno.jpg': ('install', ['Installation', 'Cleaning', 'Installation', 'Repair']),
    'dryer-vent-lint-buildup-interior.jpg': ('interior', ['Cleaning', 'Restoration', 'Cleaning', 'Inspection']),
    'clean-duct-restoration.jpg':           ('result',   ['Restoration', 'Cleaning', 'Restoration', 'Cleaning']),
    'dryer-vent-laundry-area-dirty.jpg':    ('exterior', ['Cleaning', 'Restoration', 'Cleaning', 'Inspection']),
    'vent-cover-new.jpg':                   ('install',  ['Installation', 'Cleaning', 'Installation', 'Repair']),
    'dryer-vent-damaged-before-repair.jpg': ('repair',   ['Repair', 'Restoration', 'Repair', 'Restoration']),
    'dryer-duct-inspection-dirty.jpg':      ('clog',     ['Cleaning', 'Inspection', 'Cleaning', 'Restoration']),
    'dryer-vent-exterior-damaged.jpg':      ('exterior', ['Restoration', 'Repair', 'Cleaning', 'Restoration']),
    'dryer-duct-after-cleaning-sparks.jpg': ('result',   ['Cleaning', 'Restoration', 'Cleaning', 'Inspection']),
}

# City detection from file path
CITY_MAP = {
    'reno-nv-dryer-vent-services':              'Reno',
    'sparks-nevada-dryer-vent-cleaning':        'Sparks',
    'incline-village-nevada-dryer-vent-cleaning': 'Incline Village',
    'minden-nevada-dryer-vent-cleaning':        'Minden',
    'cold-springs-nevada-dryer-vent-cleaning':  'Cold Springs',
    'hidden-valley-nevada-dryer-vent-cleaning': 'Hidden Valley',
    'lockwood-nv-dryer-vent-cleaning':          'Lockwood',
    'sun-valley-nv-dryer-vent-cleaning':        'Sun Valley',
    'washoe-valley-nv-dryer-vent-cleaning':     'Washoe Valley',
}

# Per-JPEG alt counters
alt_counters = {k: 0 for k in JPEG_MAP}

def get_alt(jpeg_name, city):
    _, services = JPEG_MAP[jpeg_name]
    svc = services[alt_counters[jpeg_name] % len(services)]
    alt_counters[jpeg_name] += 1
    return f'All-Star Dryer Vent {svc}, {city}, Nevada 775-224-4136'

def replace_img_tag(m, jpeg_name, city):
    tag = m.group(0)
    pool_name = JPEG_MAP[jpeg_name][0]
    new_webp = next_img(pool_name)
    new_alt = get_alt(jpeg_name, city)
    # Standardize path to /images/
    tag = re.sub(r'src=["\'][^"\']*?' + re.escape(jpeg_name) + r'["\']',
                 f'src="/images/{new_webp}"', tag)
    # Replace alt text
    tag = re.sub(r'alt=["\'][^"\']*["\']', f'alt="{new_alt}"', tag)
    return tag

files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

total_replacements = 0
for fp in files:
    # Skip BBB and other external-only files
    with open(fp, encoding='utf-8') as f:
        html = f.read()

    # Detect city for this file
    city = 'Reno'
    for slug, cname in CITY_MAP.items():
        if slug in fp:
            city = cname
            break

    orig = html
    rep_count = 0

    for jpeg_name in JPEG_MAP:
        if jpeg_name not in html:
            continue
        pattern = r'<img[^>]+' + re.escape(jpeg_name) + r'[^>]*>'
        def replacer(m, jn=jpeg_name, c=city):
            return replace_img_tag(m, jn, c)
        new_html = re.sub(pattern, replacer, html, flags=re.IGNORECASE)
        if new_html != html:
            rep_count += html.count(jpeg_name)
        html = new_html

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print(f'Updated ({rep_count} imgs): {rel}')
        total_replacements += rep_count

print(f'\nTotal image replacements: {total_replacements}')
