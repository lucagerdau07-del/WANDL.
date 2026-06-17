import sys
import re

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the specific CSS rules by exact CSS context to be perfectly safe
content = re.sub(r"\.comp-pros ul li::before\s*\{\s*content:\s*'[^']*';\s*color:", 
                 ".comp-pros ul li::before {\n    content: '✓';\n    color:", content)

content = re.sub(r"\.comp-cons ul li::before\s*\{\s*content:\s*'[^']*';\s*color:", 
                 ".comp-cons ul li::before {\n    content: '✗';\n    color:", content)

content = re.sub(r"\.usp-item::before\s*\{\s*content:\s*'[^']*';\s*position:",
                 ".usp-item::before {\n    content: '✓';\n    position:", content)

content = re.sub(r"\.allergen-icon::before\s*\{\s*content:\s*'[^']*';\s*color:",
                 ".allergen-icon::before {\n    content: '✓';\n    color:", content)

# Check if there are any other corrupted ones that contain â
content = content.replace('âœ“', '✓')
content = content.replace('âœ—', '✗')
content = content.replace('âœ”', '✓')
content = content.replace('âœ', '✓') 

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed encoding issues in style.css')
