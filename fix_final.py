import glob

replacements = {
    'Grǟndung': 'Gründung',
    'Prǟsenz': 'Präsenz',
    'groǟen': 'großen',
    'ǽ?s': '€',
    'Grǟnder': 'Gründer',
    'Fǟrderung': 'Förderung',
    'Geschǟftsjahr': 'Geschäftsjahr',
    'Regulǟrer': 'Regulärer',
    'Stǟckkosten': 'Stückkosten',
    'siebenunddreiǟigsten': 'siebenunddreißigsten',
    'Hǟufige': 'Häufige',
    'gedǟrrte': 'gedörrte',
    'natǟrlichen': 'natürlichen',
    'vorrǟsten': 'vorrösten',
    'dǟrren': 'dörren',
    'kǟnnen': 'können',
    'heiǟes': 'heißes',
    'fǟr': 'für',
    'Energieriegel \' Handgemacht': 'Energieriegel · Handgemacht',
    'Energieriegel  Handgemacht': 'Energieriegel · Handgemacht',
    'ǟ.ǽ\'"\' TikTok': 'TikTok',
    'ǟ.ǽ\'"\' Instagram': 'Instagram',
    'MenǬ ffnen': 'Menü öffnen',
    'Men ffnen': 'Menü öffnen',
    'genieYen': 'genießen',
    'aufbrǬhen': 'aufbrühen',
    'KǬrbiskernen': 'Kürbiskernen',
    'KǬrbiskerne': 'Kürbiskerne',
    'FǬr': 'Für',
    'natǬrliche': 'natürliche',
    'AgavensǬYe': 'Agavensüße',
    'sttigend': 'sättigend',
    'ApfelstǬcke': 'Apfelstücke',
    'MandelstǬcken': 'Mandelstücken',
    's? Enthlt': '⚠️ Enthält',
    'NǬsse': 'Nüsse',
    'fǬr': 'für',
    'entltes': 'entöltes',
    'flǬssiger': 'flüssiger',
    'Kokosl': 'Kokosöl',
    'Nhrwerte': 'Nährwerte',
    'FrǬchten': 'Früchten',
    'GenieYe': 'Genieße',
    'kstlich': 'köstlich',
    'Whle': 'Wähle',
    'ffnen': 'öffnen',
    's?': '⚠️',
    'ЄYZ"': '✅'
}

files = glob.glob('**/*.html', recursive=True)
count = 0

for f in files:
    if 'recovered' in f or 'nocache' in f: continue
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    modified = False
    for k, v in replacements.items():
        if k in content:
            content = content.replace(k, v)
            modified = True
            
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed {f}')
        count += 1

print(f'Total files fixed: {count}')
