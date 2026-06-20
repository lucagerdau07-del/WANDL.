import glob

files = glob.glob('**/*.html', recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    if 'style.cs⚠️v=' in content:
        content = content.replace('style.cs⚠️v=', 'style.css?v=')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Fixed CSS link in {f}')
