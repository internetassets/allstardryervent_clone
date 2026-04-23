import re

fp = r'C:\Users\rusty\allstardryervent_clone\index.html'
with open(fp, encoding='utf-8') as f:
    html = f.read()

orig = html

# Remove the commented-out pricing section (the entire <!-- ... --> block containing the pricing section)
html = re.sub(r'\s*<!--\s*<section id="pricing".*?-->', '', html, flags=re.DOTALL)

if html != orig:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Pricing section removed')
else:
    print('No change - pattern not found')
