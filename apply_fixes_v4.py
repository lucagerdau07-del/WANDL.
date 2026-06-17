import re
import shutil
import time

# 1. Copy images using python to be absolutely safe
try:
    shutil.copy2(r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\SKIZZE\ChatGPT Image 16. Juni 2026, 22_57_48.png', r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\assets\images\sustainability-v3.png')
    shutil.copy2(r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\SKIZZE\Design ohne Titel (4).png', r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\assets\images\design-4-v3.png')
    shutil.copy2(r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\SKIZZE\Design ohne Titel (3).png', r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\assets\images\logo-v3.png')
except Exception as e:
    print("Copy error:", e)

# 2. Rewrite HTML
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

ts = str(int(time.time()))

# --- Fix Logo ---
# The logo might be white, so we apply a brightness filter so it shows up black on the white navbar
html = re.sub(
    r'<a href="#hero" class="logo"><img src="[^"]+" alt="WANDL\. Logo"></a>',
    f'<a href="#hero" class="logo"><img src="assets/images/logo-v3.png?v={ts}" alt="WANDL. Logo" style="height: 45px; filter: brightness(0); display: block;"></a>',
    html
)

# --- Fix Transformation (Force Side-by-Side Flexbox) ---
old_trans = r'<section id="transformation">.*?</section>\s*<!-- ============================================================\s*USP'
new_trans = f'''<section id="transformation" style="padding: 4rem 0;">
            <div class="container" style="display: flex; flex-direction: row; flex-wrap: nowrap; align-items: center; justify-content: center; gap: 4rem;">
                <div class="image-content" style="flex: 1; display: flex; justify-content: center; align-items: center; min-width: 300px;">
                    <img src="assets/images/design-4-v3.png?v={ts}" alt="Idee / Funktion" class="floating-image" style="width: 100%; max-width: 600px; height: auto; object-fit: contain; display: block;">
                </div>
                <div class="text-content" style="flex: 1; min-width: 300px;">
                    <h2 style="margin-bottom: 1rem; color: var(--color-olive-700);">Idee / Funktion</h2>
                    <h2 style="font-size: 2.5rem; margin-bottom: 2rem;">Vom Riegel<br>zur Mahlzeit.</h2>
                    <div class="steps-grid">
                        <div class="step-card">
                            <div class="step-icon">1</div>
                            <h3>Zerbröseln</h3>
                            <p>Den Riegel grob in eine Schale oder Tasse brechen.</p>
                        </div>
                        <div class="step-card">
                            <div class="step-icon">2</div>
                            <h3>Aufgießen</h3>
                            <p>Mit kochendem Wasser übergießen, bis die Stückchen bedeckt sind.</p>
                        </div>
                        <div class="step-card">
                            <div class="step-icon">3</div>
                            <h3>Genießen</h3>
                            <p>90 Sekunden quellen lassen und umrühren – fertig ist das Porridge.</p>
                        </div>
                    </div>
                    <div class="cold-notice" style="margin-top: 2rem; background: var(--color-earth-100); padding: 1.5rem; border-radius: var(--radius-md);">
                        <p><strong>Das Kalt-Prinzip:</strong> Keine Zeit? Gieße kaltes Wasser auf für ein erfrischendes Kalt-Porridge – oder genieße den Riegel direkt auf der Hand.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- ============================================================
             USP'''
html = re.sub(old_trans, new_trans, html, flags=re.DOTALL)

# --- Fix Sustainability Image (Full Screen Scroll) ---
# The user wants it in 9:16 format scrolling down. Meaning it's a huge portrait image.
old_sust = r'<section id="sustainability"[^>]*>.*?</section>\s*<!-- ============================================================\s*ALLERGEN-FREI'
new_sust = f'''<section id="sustainability" style="width: 100%; display: block; padding: 0; margin: 0; background-color: #ffffff;">
            <img src="assets/images/sustainability-v3.png?v={ts}" alt="Unternehmerische Verantwortung" style="width: 100%; max-width: 1000px; height: auto; display: block; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
        </section>
        <!-- ============================================================
             ALLERGEN-FREI'''
html = re.sub(old_sust, new_sust, html, flags=re.DOTALL)

# --- Fix Partners Fade (Use explicit div instead of pseudo element) ---
old_partners = r'<section id="partners"[^>]*>.*?</section>\s*<!-- ============================================================\s*FAQ'
new_partners = '''<section id="partners" style="position: relative; overflow: hidden; padding: 6rem 0 4rem 0; background: var(--color-earth-50);">
            <!-- Explicit Fade Element -->
            <div style="position: absolute; top: 0; left: 0; right: 0; height: 150px; background: linear-gradient(to bottom, #ffffff 0%, #f4f5f0 100%); z-index: 1; pointer-events: none;"></div>
            
            <div class="container center-text" style="position: relative; z-index: 2;">
                <h2 style="margin-bottom: 2rem;">Unsere Partner</h2>
            </div>
            
            <!-- Infinite Marquee -->
            <div class="partner-marquee" style="position: relative; z-index: 2;">
                <div class="marquee-track">
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                    <div class="marquee-item">🏕️ Globetrotter</div>
                    <div class="marquee-item">🛒 Bio-Markt</div>
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                    <div class="marquee-item">🏕️ Globetrotter</div>
                    <div class="marquee-item">🛒 Bio-Markt</div>
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                </div>
            </div>
        </section>
        <!-- ============================================================
             FAQ'''
html = re.sub(old_partners, new_partners, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied robust UI fixes V4.")
