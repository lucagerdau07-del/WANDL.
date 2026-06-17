import sys
path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'Energie-Effizienz': 'Energie Effizienz',
    '„ungebacken“-Herstellung': 'Herstellung ohne Backen',
    'Backofen-Energie': 'Ofenenergie',
    'Porridge-Löslichkeit': 'Löslichkeit als Porridge',
    'Monomaterial-Barriere': 'Monomaterial Barriere',
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
