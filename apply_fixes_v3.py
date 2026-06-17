import re

# 1. Update HTML Files
html_files = ['index.html', 'shop.html', 'abos.html']

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update Logo
        html = html.replace('assets/images/logo.png', 'assets/images/logo-v2.png')

        # Only index.html specific updates
        if file_path == 'index.html':
            # --- Transformation (Idee/Funktion) to Split Layout ---
            old_trans = r'<section id="transformation">.*?</section>\s*<!-- ============================================================\s*USP'
            new_trans = '''<section id="transformation">
            <div class="container split-layout">
                <div class="image-content" style="display: flex; justify-content: center; align-items: center;">
                    <img src="assets/images/design-4-v2.png" alt="Idee / Funktion" class="floating-image" style="width: 100%; max-width: 600px; height: auto; object-fit: contain; display: block;">
                </div>
                <div class="text-content">
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

            # --- Sustainability (9:16 Full Scroll Image) ---
            old_sust = r'<section id="sustainability".*?</section>\s*<!-- ============================================================\s*ALLERGEN-FREI'
            new_sust = '''<section id="sustainability" style="width: 100%; background: black;">
            <img src="assets/images/sustainability-v2.png" alt="Unternehmerische Verantwortung" style="width: 100%; height: auto; display: block;">
        </section>
        <!-- ============================================================
             ALLERGEN-FREI'''
            html = re.sub(old_sust, new_sust, html, flags=re.DOTALL)

            # --- Partners Background Fade ---
            # Remove inline style background: var(--color-earth-50); and add gradient
            html = html.replace(
                '<section id="partners" style="overflow: hidden; padding: 4rem 0; background: var(--color-earth-50);">',
                '<section id="partners" style="overflow: hidden; padding: 4rem 0; background: linear-gradient(to bottom, var(--color-white) 0%, var(--color-earth-50) 30%);">'
            )
            html = html.replace(
                '<section id="partners" style="overflow: hidden; padding: 4rem 0; background: linear-gradient(to bottom, var(--color-white), var(--color-earth-50));">',
                '<section id="partners" style="overflow: hidden; padding: 4rem 0; background: linear-gradient(to bottom, var(--color-white) 0%, var(--color-earth-50) 30%);">'
            )


        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception as e:
        print(f"Failed {file_path}: {e}")

# 2. Update CSS
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Allergen grid spacing to be 6rem (double)
css = css.replace(
    'gap: 3rem !important;',
    'gap: 6rem !important;'
)

# Fix Allergen sub shadow (stronger shadow)
css = css.replace(
    '#allergen-free h2, #allergen-free .section-sub, #allergen-free .label {\n    color: #ffffff !important;\n    text-shadow: 0 2px 10px rgba(0,0,0,0.8) !important;\n}',
    '#allergen-free h2, #allergen-free .label {\n    color: #ffffff !important;\n    text-shadow: 0 2px 10px rgba(0,0,0,0.8) !important;\n}\n#allergen-free .section-sub {\n    color: #ffffff !important;\n    text-shadow: 0 4px 15px rgba(0,0,0,1) !important;\n    font-weight: bold !important;\n}'
)

# Remove the old ::before pseudo element for partners to not conflict
css = css.replace(
    '#partners::before {\n    content: \'\';\n    position: absolute;\n    top: 0; left: 0; right: 0;\n    height: 150px;\n    background: linear-gradient(to bottom, var(--color-white), var(--color-earth-50));\n    pointer-events: none;\n    z-index: 0;\n}',
    '/* partners before removed */'
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied V3 fixes.")
