import re

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\impressum.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

links = [
    "https://www.fortunebusinessinsights.com/de/markt-f-r-mahlzeiten-ersatz-111106",
    "https://kaja-ops.gymbeam.com/",
    "https://nutrikal.com/de",
    "https://kitchen4rent.de/",
    "https://www.stiftungbildung.org/youstartn/",
    "https://www.offenbach.ihk.de/recht-und-steuern/mustervertraege-und-formulare/gesellschaftsvertrag/",
    "https://www.lexware.de/tools/vorlage-gbr-vertrag/",
    "https://finanzamt.hessen.de/steuern/umsatzsteuer-kleinunternehmer",
    "https://www.finanzamt.nrw.de/steuerinfos/unternehmen/umsatzsteuer/kleinunternehmerinnen-und-kleinunternehmer",
    "https://www.ihk-muenchen.de/ratgeber/steuern/umsatzsteuer/kleinunternehmerregelung/",
    "https://proveg.org/de/news/vegan-trend-zahlen-und-fakten-zum-veggie-markt",
    "https://proveg.org/de/5-pros/anzahl-vegan-vegetarischer-menschen",
    "https://www.bte-tourismus.de/wp-content/uploads/2024/10/BTE-Wanderstudie-2024-1.pdf",
    "https://www.ifd-allensbach.de/fileadmin/AWA/AWA_Praesentationen/2025/04_AWA2025_Sommer_Gesundheit_und_Erna__hrung.pdf",
    "https://de.wikipedia.org/wiki/Allensbacher_Markt-_und_Werbetr%C3%A4ger-Analyse",
    "https://www.ifd-allensbach.de/awa/konzept/uebersicht.html",
    "https://food.ec.europa.eu/food-safety/chemical-safety/food-contact-materials/legislation_en",
    "https://foodpackagingforum.org/news/efsa-authorizes-iron-based-oxygen-absorbers-for-food-contact",
    "https://www.efsa.europa.eu/en/topics/active-and-intelligent-materials",
    "https://www.bfr.bund.de/cm/343/gras-und-blattprodukte-zum-verzehr-koennen-mit-krankmachenden-bakterien-verunreinigt-sein.pdf",
    "https://grubatec.ch/produkt/wie-beeinflusst-die-wasseraktivitaet-die-haltbarkeit-von-lebensmitteln/",
    "https://ucanr.edu/program/uc-master-food-preserver-program/article/water-activity-and-its-role-food-preservation",
    "https://www.processsensing.com/en-us/blog/aw-measurement.htm",
    "https://www.bmleh.de/DE/themen/ernaehrung/lebensmittel-kennzeichnung/pflichtangaben/naehrwertinformationen-health-claims.html",
    "https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32006R1924",
    "https://www.legislation.gov.uk/eur/2006/1924/annex/division/18"
]

links_html = '<div class="sources-list" style="word-break: break-all;">\n'
for link in links:
    links_html += f'            <a href="{link}" target="_blank" style="display: block; padding: 10px; background: white; margin-bottom: 5px; border-radius: 5px; text-decoration: none; color: var(--color-earth-800); border: 1px solid #ddd;">{link}</a>\n'
links_html += '        </div>'

# Regex to replace the sources-list div content
pattern = re.compile(r'<div class="sources-list">.*?</div>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(links_html, html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
