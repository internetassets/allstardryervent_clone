import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

OLD_ALTS = [
    'alt="All Star Dryer Vent Logo"',
    'alt=""',  # catch any remaining empty alts on the logo
]
NEW_ALT = 'alt="All Star Dryer Vent, Reno, Nevada 775-224-4136"'

# The logo img tags to target (both URL forms)
LOGO_SRCS = [
    'src="https://www.allstardryervent.com/images/allstar-logo.png"',
    'src="/images/allstar-logo.png"',
]

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html

    for src in LOGO_SRCS:
        for old_alt in OLD_ALTS:
            html = html.replace(src + ' class="h-10 w-auto" ' + old_alt,
                                src + ' class="h-10 w-auto" ' + NEW_ALT)

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Updated: ' + rel)
        count += 1

print('Total updated: ' + str(count))
