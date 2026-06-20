import os
import glob
import codecs

replacements = {
    'Ã¼': 'ü',
    'Ã¶': 'ö',
    'Ã¤': 'ä',
    'ÃŸ': 'ß',
    'Ãœ': 'Ü',
    'Ã–': 'Ö',
    'Ã„': 'Ä',
    'Ã©': 'é',
    'â‚¬': '€',
    'Â·': '·',
    'Ã¢â‚¬': '€'
}

files = glob.glob('**/*.html', recursive=True)

for f in files:
    try:
        with open(f, 'rb') as file:
            raw = file.read()
        
        # Try UTF-8 first
        try:
            content = raw.decode('utf-8')
        except UnicodeDecodeError:
            # Fallback to Windows-1252
            content = raw.decode('cp1252')
            
        modified = False
        for k, v in replacements.items():
            if k in content:
                content = content.replace(k, v)
                modified = True
                
        if modified:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Fixed {f}')
    except Exception as e:
        print(f'Error processing {f}: {e}')
