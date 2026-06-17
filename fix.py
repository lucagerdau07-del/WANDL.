import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'Ǭ': 'ü',
    'Y': 'ß',
    'o"': '✅',
    'o-': '❌',
    '?"': '–',
    '?': '€',
    'C': '°C',
    'heiem': 'heißem',
    'geniee': 'genieße',
    'Auenseite': 'Außenseite',
    'lslichkeit': 'löslichkeit',
    'Drrtemperatur': 'Dörrtemperatur',
    'hchsten': 'höchsten',
    'Qualittsstandards': 'Qualitätsstandards',
    'fr': 'für',
    'natrliche': 'natürliche',
    'Se': 'Süße',
    'sttigend': 'sättigend',
    'kstlich': 'köstlich',
    'Stcke': 'Stücke',
    'Nsse': 'Nüsse',
    'Hufige': 'Häufige',
    'kndbar': 'kündbar',
    'groen': 'großen',
    'Whle': 'Wähle',
    'Ernhrungsbereich': 'Ernährungsbereich',
    'Krbiskernen': 'Kürbiskernen',
    'geschtzt': 'geschützt',
    'Mietkche': 'Mietküche',
    'ber': 'über',
    'Geschften': 'Geschäften',
    'Stckkosten': 'Stückkosten',
    'Grndern': 'Gründern',
    'volljhrigen': 'volljährigen',
    'brgerlichen': 'bürgerlichen',
    'gegrndet': 'gegründet',
    '': 'ä'  # Use unicode replacement character directly if it's there
}

for k, v in replacements.items():
    text = text.replace(k, v)

# Specifically target the bad sequences
text = text.replace('fÃ¼r', 'für').replace('ðŸ¤', '🤝')
text = text.replace('?', '€').replace('C', '°C').replace('', 'ä') # Generic fallback

# Clean up multiple ä
text = text.replace('ä"', '–').replace('ä-', '❌')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed.')
