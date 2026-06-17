import sys

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\css\style.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I know EXACTLY what is in the file now
str_pros = '''.comp-pros ul li::before {
    content: 'V';'''
rep_pros = '''.comp-pros ul li::before {
    content: '✓';'''

str_cons = '''.comp-cons ul li::before {
    content: '?';'''
rep_cons = '''.comp-cons ul li::before {
    content: '✗';'''

# And the other ones might still be âœ“ because PowerShell crashed before fixing them
content = content.replace('âœ“', '✓')
content = content.replace('âœ—', '✗')
content = content.replace('âœ”', '✓')
content = content.replace('âœ', '✓') 
content = content.replace('o"', '✓')
content = content.replace('o-', '✗')

content = content.replace(str_pros, rep_pros)
content = content.replace(str_cons, rep_cons)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed completely')
