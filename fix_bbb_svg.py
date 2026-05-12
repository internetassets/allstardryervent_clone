import glob, os, re

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

OLD_SRC = 'https://m.bbb.org/prod/ProfileImages/2023/87cd1656-a649-4254-932a-50d6b34842b7.jpg'
NEW_SRC = '/images/ALL%20STAR%20DRYER%20VENT%20BBB.svg'

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    html = html.replace(OLD_SRC, NEW_SRC)
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Fixed: ' + rel)
        count += 1

print('Total: ' + str(count))
