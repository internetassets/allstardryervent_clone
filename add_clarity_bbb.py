import glob, os, re

BASE = r'C:\Users\rusty\allstardryervent_clone'

CLARITY = """<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wd8gr20qb5");
</script>
</head>"""

BBB_LINK = '<a href="https://www.bbb.org/us/nv/sparks/profile/dryer-vent-cleaning/all-star-dryer-vent-1166-90045613" target="_blank" rel="noopener" class="hover:scale-110 transition"><img src="https://m.bbb.org/prod/ProfileImages/2023/87cd1656-a649-4254-932a-50d6b34842b7.jpg" class="h-6 opacity-70 hover:opacity-100 rounded-sm" alt="Better Business Bureau" width="50" height="50"></a>'

YELP_ANCHOR = '<a href="https://www.yelp.com/biz/_-NPdMpODALiSrDJF9JimA" class="hover:scale-110 transition"><img src="https://img.icons8.com/ios-filled/50/ffffff/yelp.png" class="h-6 opacity-70 hover:opacity-100" alt="Yelp" width="50" height="50"></a>'

files = sorted(set(
    glob.glob(os.path.join(BASE, '**', '*.html'), recursive=True) +
    glob.glob(os.path.join(BASE, '*.html'))
))

results = []

for fp in files:
    with open(fp, encoding='utf-8') as f:
        html = f.read()
    orig = html
    changes = []

    # 1. Add Clarity before </head> (skip if already present or no </head>)
    if '</head>' in html and 'clarity.ms/tag' not in html:
        html = html.replace('</head>', CLARITY, 1)
        changes.append('clarity')

    # 2. Add BBB link after Yelp icon (skip if already present)
    if YELP_ANCHOR in html and 'bbb.org' not in html:
        html = html.replace(YELP_ANCHOR, YELP_ANCHOR + BBB_LINK, 1)
        changes.append('bbb')

    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        rel = fp[len(BASE)+1:].replace('\\', '/')
        results.append(rel + ': ' + ', '.join(changes))

out = os.path.join(BASE, 'clarity_bbb_results.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results) + '\n')
    f.write('Total files modified: ' + str(len(results)) + '\n')

print('Done')
