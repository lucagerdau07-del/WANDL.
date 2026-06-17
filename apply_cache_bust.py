import re
import time

timestamp = str(int(time.time()))

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Cache Busting for all images
html = re.sub(r'(\.png|\.jpg|\.svg)(\?v=\d+)?(["\'])', r'\1?v=' + timestamp + r'\3', html)

# 2. Fix Sustainability (Remove black background, ensure it just shows the image)
html = re.sub(
    r'<section id="sustainability" style="[^"]*">',
    '<section id="sustainability" style="width: 100%; display: block; line-height: 0; background: transparent; padding: 0;">',
    html
)

# 3. Partners Fade: make it much more pronounced
# I will use a pseudo element again but this time directly in the HTML via style block to guarantee it applies
html = html.replace(
    '<section id="partners" style="overflow: hidden; padding: 4rem 0; background: linear-gradient(to bottom, var(--color-white) 0%, var(--color-earth-50) 30%);">',
    '<section id="partners" style="position: relative; overflow: hidden; padding: 6rem 0 4rem 0; background: var(--color-earth-50);">'
)
# Add the pseudo element via inline style block right before #partners
fade_style = '''<style>
#partners::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 250px;
    background: linear-gradient(to bottom, #ffffff 0%, var(--color-earth-50) 100%);
    pointer-events: none;
    z-index: 1;
}
#partners .container {
    position: relative;
    z-index: 2;
}
</style>
'''
if '<style>\n#partners::before' not in html:
    html = html.replace('<section id="partners"', fade_style + '<section id="partners"')

# 4. Make sure logo is inverted if it's white text, but wait, I don't know if the logo is white.
# The user just said it's not there. Cache busting should fix it.

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
