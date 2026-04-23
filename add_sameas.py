import glob, os

base = r'C:\Users\rusty\allstardryervent_clone'
files = glob.glob(os.path.join(base, '**', '*.html'), recursive=True) + glob.glob(os.path.join(base, '*.html'))
files = sorted(set(files))

SAMEAS = (
    '"sameAs":['
    '"https://www.facebook.com/allstardryervent",'
    '"https://www.instagram.com/allstardryervent",'
    '"https://www.yelp.com/biz/_-NPdMpODALiSrDJF9JimA",'
    '"https://g.page/r/CbCW4WjBLs9_EBM/review",'
    '"https://www.bbb.org/us/nv/sparks/profile/dryer-vent-cleaning/all-star-dryer-vent-1166-90045613"'
    '],'
    '"hasMap":"https://www.google.com/maps/place/All+Star+Dryer+Vent",'
)

TARGET = '"aggregateRating":{"@type":"AggregateRating"'
REPLACEMENT = SAMEAS + TARGET

count = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    if TARGET in html and 'sameAs' not in html.split(TARGET)[0].split('"LocalBusiness"')[-1]:
        html = html.replace(TARGET, REPLACEMENT, 1)
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(base)+1:].replace('\\', '/')
        print('Updated: ' + rel)
        count += 1

print('Total updated: ' + str(count))
