import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<!-- ============================================================\s*OUR STORY\s*============================================================ -->\s*<section id="our-story">.*?</section>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
