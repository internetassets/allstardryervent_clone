import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

OLD = 'class="h-6 opacity-70 hover:opacity-100 rounded-sm" alt="Better Business Bureau" width="50" height="50"'
NEW = 'class="h-6 w-auto opacity-70 hover:opacity-100 rounded-sm" alt="Better Business Bureau" width="auto" height="24"'

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    html = html.replace(OLD, NEW)
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Fixed: ' + rel)
        count += 1

print('Total: ' + str(count))
