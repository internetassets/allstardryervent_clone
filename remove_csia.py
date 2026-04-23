# -*- coding: utf-8 -*-
import glob, os, re

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

# Ordered replacements - more specific phrases first
REPLACEMENTS = [
    # Meta description variants
    ('CSIA certified specialists', 'experienced dryer vent specialists'),
    ('CSIA certified technicians', 'experienced dryer vent technicians'),
    ('CSIA-certified technicians', 'experienced dryer vent technicians'),
    ('CSIA-certified specialists', 'experienced dryer vent specialists'),
    ('Our CSIA-certified technicians', 'Our experienced technicians'),
    ('our CSIA-certified technicians', 'our experienced technicians'),
    # Trust/body copy variants
    ('CSIA certified', 'experienced professionals'),
    ('CSIA-certified', 'experienced'),
    ('CSIA Certified', 'experienced dryer vent professionals'),
    # Standalone references
    ('CSIA certification', 'professional expertise'),
    ('CSIA cert', 'professional training'),
    ('CSIA', 'dryer vent'),
]

total_files = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html

    for old, new in REPLACEMENTS:
        html = html.replace(old, new)

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Updated: ' + rel)
        total_files += 1

print('Total files updated: ' + str(total_files))
