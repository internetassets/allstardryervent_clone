import glob, os, re

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

refs = {}
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    found = re.findall(r'src=["\'][^"\']*?([^/"\' ]+\.jpg)["\']', html, re.IGNORECASE)
    for img in found:
        if img not in refs:
            refs[img] = []
        rel = fp[len(base)+1:].replace('\\', '/')
        refs[img].append(rel)

for img, pages in sorted(refs.items()):
    print(img)
    for p in pages:
        print('  -> ' + p)
