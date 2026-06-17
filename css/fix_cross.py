import sys

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Revert all accidental ✗ back to o-
content = content.replace('✗', 'o-')

# Restore the correct ✗ only in content property
content = content.replace("content: 'o-';", "content: '✗';")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored all accidental o- replacements.")
