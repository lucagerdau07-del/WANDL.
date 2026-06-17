import re
import time

html_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the classes for the partner section
html = html.replace('class="partner-marquee"', 'class="logo-carousel"')
html = html.replace('class="marquee-track"', 'class="logo-track"')
html = html.replace('class="marquee-item"', 'class="logo-item"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Partner classes fixed.")
