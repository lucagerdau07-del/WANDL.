import re

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

old_card_pattern = re.compile(r'<div class="need-card">\s*<p class="need-text">Der Notgroschen.*?</div>', re.DOTALL)

new_card = '''<div class="need-card" style="text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1.5rem;">
                        <img src="assets/images/packaging.png" alt="100% Biologisch abbaubare Verpackung" style="height: 100px; width: auto; object-fit: contain; margin-bottom: 1rem;">
                        <h3 style="margin-bottom: 0.5rem; color: var(--color-earth-900);">Clevere Verpackung</h3>
                        <p style="color: var(--color-earth-600); line-height: 1.6; font-size: 0.95rem;">100% biologisch abbaubar. Die warme Zubereitung ist problemlos direkt in der Verpackung möglich.</p>
                    </div>'''

if old_card_pattern.search(html):
    html = old_card_pattern.sub(new_card, html)
else:
    print('Pattern not found')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
