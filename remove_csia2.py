# -*- coding: utf-8 -*-
import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

OLD = 'href="https://www.csia.org"'
NEW = 'href="https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Safeguard-Your-Family-From-Fire/Clothes-Dryer-Fire-Safety"'

total = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    html = html.replace(OLD, NEW)
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Updated: ' + rel)
        total += 1

print('Total: ' + str(total))
