import os

replacements = {
    '2-in-1': 'Zwei in Eins',
    'Outdoor-Upgrade': 'Upgrade für Outdoor',
    'Kalt-Prinzip': 'Prinzip für kaltes Wasser',
    'Kalt-Porridge': 'kaltes Porridge',
    'Magen-Stress': 'Probleme mit dem Magen',
    'Hanf- und Kürbiskernprotein': 'Hanfprotein und Kürbiskernprotein',
    'Outdoor-Enthusiasten': 'Outdoor Enthusiasten',
    'Trekking-Nahrung': 'Trekking Nahrung',
    'Fitness-Marktführer': 'Fitness Marktführer',
    'Energie-Effizienz': 'Energie Effizienz',
    '„ungebacken“-Herstellung': 'Herstellung ohne Backen',
    'Backofen-Energie': 'Ofenenergie',
    'Porridge-Löslichkeit': 'Löslichkeit als Porridge',
    'Monomaterial-Barriere': 'Monomaterial Barriere'
}

for root, dirs, files in os.walk(r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            for k, v in replacements.items():
                text = text.replace(k, v)
            text = text.replace('üü', 'ü')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
