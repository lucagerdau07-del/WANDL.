import os
import glob
import re

base_dir = r"C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website"

# 1. Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_text = f.read()

# Replace the protein text
index_text = index_text.replace(
    "Volle Power durch natürliche Proteinquellen (Hanfprotein und Kürbiskernprotein) ohne künstliche Pulverzusätze.",
    "Volle Power durch natürliche Proteinquellen."
)
# Also try without full stop if it was missing
index_text = index_text.replace(
    "Volle Power durch natürliche Proteinquellen (Hanfprotein und Kürbiskernprotein) ohne künstliche Pulverzusätze",
    "Volle Power durch natürliche Proteinquellen"
)

# Remove the 'Notgroschen' block
# Find the exact HTML structure containing this block. It's probably a grid item.
# I'll just remove the strings, and if it leaves an empty block, I'll remove the whole block.
notgroschen_regex = re.compile(r'<div[^>]*>\s*<h3[^>]*>Der Notgroschen.*?</div>\s*</div>', re.DOTALL)
if notgroschen_regex.search(index_text):
    index_text = notgroschen_regex.sub('', index_text)
else:
    # If regex doesn't match the div structure, just remove the text and its h3/p tags
    index_text = re.sub(r'<h3[^>]*>Der Notgroschen für den Rucksack.*?</h3>', '', index_text, flags=re.DOTALL)
    index_text = re.sub(r'<p[^>]*>Egal ob auf dem Trail, im Büro oder auf Reisen.*?</p>', '', index_text, flags=re.DOTALL)


with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_text)

# 2. Add ingredients to product pages
ingredients_map = {
    "product.html": "Zarthafer (feine Haferflocken), Erbsenprotein Isolat, gehackte Kürbiskerne, gefriergetrocknete Heidelbeeren, Meersalz, Agavendicksaft, Sonnenblumenkernbutter, kaltgepresstes Kokosöl.",
    "product-original.html": "Zarthafer (feine Haferflocken), Erbsenprotein Isolat, gehackte Kürbiskerne, gefriergetrocknete Heidelbeeren, Meersalz, Agavendicksaft, Sonnenblumenkernbutter, kaltgepresstes Kokosöl.",
    "product-dark.html": "Zarthafer (feine Haferflocken), Erbsenprotein Isolat, stark entöltes Kakaopulver, gehackte Kürbiskerne, Meersalz, flüssiger Vanilleextrakt, Agavendicksaft, Sonnenblumenkernbutter, kaltgepresstes Kokosöl.",
    "product-spice.html": "Zarthafer (feine Haferflocken), Erbsenprotein Isolat, gefriergetrocknetes Apfelpulver, gemahlener Ceylon Zimt, gemahlener Kardamom, Meersalz, Agavendicksaft, Sonnenblumenkernbutter, kaltgepresstes Kokosöl.",
    "product-classic.html": "Zarthafer (feine Haferflocken), neutrales Molkenprotein Isolat (Whey), Vollmilchpulver, gehackte Mandeln, Meersalz, Agavendicksaft, feines Mandelmus (ohne Zuckerzusatz), kaltgepresstes Kokosöl."
}

for filename, ingredients in ingredients_map.items():
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
        
        # We need to insert the Zutaten block right above <h3>Nährwerte
        if "<h3>Zutaten</h3>" not in html:
            insert_str = f"<h3>Zutaten</h3>\n                    <p style=\"margin-bottom: 2rem; color: var(--color-earth-600); line-height: 1.6;\">{ingredients}</p>\n\n                    <h3>Nährwerte"
            html = html.replace("<h3>Nährwerte", insert_str)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
