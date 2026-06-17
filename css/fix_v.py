import sys
import re

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the V and ? corruptions
content = re.sub(r"\.comp-pros ul li::before\s*\{\s*content:\s*'[^']*';", 
                 ".comp-pros ul li::before {\n    content: '✓';", content)

content = re.sub(r"\.comp-cons ul li::before\s*\{\s*content:\s*'[^']*';", 
                 ".comp-cons ul li::before {\n    content: '✗';", content)

# Check if there are other 'V's. The python script earlier didn't crash on execution but PowerShell did, 
# so V and ? might not be the only ones. Let's fix USP items:
content = re.sub(r"\.usp-item::before\s*\{\s*content:\s*'[^']*';",
                 ".usp-item::before {\n    content: '✓';", content)

content = re.sub(r"\.allergen-icon::before\s*\{\s*content:\s*'[^']*';",
                 ".allergen-icon::before {\n    content: '✓';", content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed V and ? corruptions in style.css')
