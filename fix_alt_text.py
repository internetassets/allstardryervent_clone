import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    html = html.replace(
        'src="https://www.allstardryervent.com/images/allstar-logo.png" class="h-10 w-auto" alt=""',
        'src="https://www.allstardryervent.com/images/allstar-logo.png" class="h-10 w-auto" alt="All Star Dryer Vent Logo"'
    )
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Fixed: ' + rel)
        count += 1

print('Total files fixed: ' + str(count))
