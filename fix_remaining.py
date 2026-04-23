import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html

    # Fix local-path logo alt text
    html = html.replace(
        'src="/images/allstar-logo.png" class="h-10 w-auto" alt=""',
        'src="/images/allstar-logo.png" class="h-10 w-auto" alt="All Star Dryer Vent Logo"'
    )

    # Fix footer relative links on non-location pages (services, faq, contact, etc.)
    # Only replace bare relative hrefs - location pages were already fixed
    html = html.replace('href="locations/', 'href="/locations/')

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\\\', '/').replace('\\', '/')
        print('Fixed: ' + rel)

print('Done')
