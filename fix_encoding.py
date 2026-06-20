import os
import glob

replacements = {
    'Ã¼': 'ü',
    'Ã¶': 'ö',
    'Ã¤': 'ä',
    'ÃŸ': 'ß',
    'Ãœ': 'Ü',
    'Ã–': 'Ö',
    'Ã„': 'Ä',
    'Ã©': 'é',
    'ï¿½': 'ü' # Sometimes replacement character is used if data was totally lost, but I'll only replace the known utf8 mojibake.
}

files = glob.glob('**/*.html', recursive=True) + glob.glob('**/*.css', recursive=True) + glob.glob('**/*.js', recursive=True)
count = 0

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
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
    except Exception as e:
        print(f'Error reading {f}: {e}')

print(f'Total files fixed: {count}')
