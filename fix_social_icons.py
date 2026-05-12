import glob, os, re

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

# Icons8 social icons: add w-auto, fix width/height attributes
ICONS = ['facebook-new.png', 'instagram-new.png', 'google-logo.png', 'yelp.png']

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html

    for icon in ICONS:
        if icon not in html:
            continue
        # Add w-auto to class (after h-6)
        html = re.sub(
            r'(<img[^>]+' + re.escape(icon) + r'[^>]+class=")h-6 opacity-70',
            r'\1h-6 w-auto opacity-70',
            html
        )
        # Fix width/height attributes to 24x24
        html = re.sub(
            r'(<img[^>]+' + re.escape(icon) + r'[^>]+)width="50"([^>]+)height="50"',
            r'\g<1>width="24"\2height="24"',
            html
        )

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Fixed: ' + rel)
        count += 1

print('Total: ' + str(count))
