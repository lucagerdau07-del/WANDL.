import re
import time
from PIL import Image

# 1. Crop Logo
input_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\assets\images\logo-v3.png'
output_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\assets\images\logo-v4.png'

try:
    img = Image.open(input_path).convert("RGBA")
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        cropped_img = img.crop(bbox)
        cropped_img.save(output_path)
        print("Cropped logo successfully:", bbox)
    else:
        # If it's completely transparent, just copy it (unlikely based on extrema)
        img.save(output_path)
        print("Logo was fully transparent or empty.")
except Exception as e:
    print("Error cropping logo:", e)

# 2. Update HTML
html_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

ts = str(int(time.time()))

# Update logo path and slightly increase height now that it's cropped
html = re.sub(
    r'<img src="assets/images/logo-v3\.png[^"]*" alt="WANDL\. Logo" style="height: 45px; filter: brightness\(0\); display: block;">',
    f'<img src="assets/images/logo-v4.png?v={ts}" alt="WANDL. Logo" style="height: 35px; filter: brightness(0); display: block;">',
    html
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update CSS
css_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Change .sv-section background to earth-50 so the black bar disappears
css = css.replace('background: var(--color-black);', 'background: var(--color-earth-50);')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
