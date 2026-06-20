import os
import glob

replacements = {
    'â‚¬': '€',
    'Â·': '·',
    'Ã¢â‚¬': '€'
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
        pass

print(f'Total files fixed: {count}')
