import re

# 1. HTML Updates
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Allergen Image Cache issue & Grid spacing
html = html.replace('assets/images/allergen-bg.png', 'assets/images/allergen-bg-v2.png')

# Competition UI Upgrade
old_comp = r'<section id="competition">.*?</section>\s*<!-- ============================================================\s*NACHHALTIGKEIT'
new_comp = '''<section id="competition">
            <div class="container">
                <h2 class="center-text" style="margin-bottom: 3rem;">Konkurrenzanalyse</h2>
                <div class="competition-cards">
                    
                    <div class="comp-card" style="border-top: 4px solid var(--color-earth-300);">
                        <div class="comp-header">
                            <h3>Clif Bar</h3>
                            <span class="comp-badge">Der Klassiker</span>
                        </div>
                        <div class="comp-body">
                            <div class="comp-pros">
                                <strong>Stärken:</strong>
                                <ul>
                                    <li>Hohe Bekanntheit</li>
                                    <li>Günstiger Preis (~2,49 €)</li>
                                </ul>
                            </div>
                            <div class="comp-cons">
                                <strong>Schwächen:</strong>
                                <ul>
                                    <li>Nicht allergenfrei (Soja, Nüsse)</li>
                                    <li>Klebrig bei Kälte</li>
                                    <li>Viel industrieller Zucker</li>
                                    <li>Nicht als Porridge nutzbar</li>
                                </ul>
                            </div>
                        </div>
                        <div class="comp-usp">
                            <strong>WANDL. Vorteil:</strong><br>
                            100% Allergenfrei & warm essbar.
                        </div>
                    </div>

                    <div class="comp-card" style="border-top: 4px solid var(--color-earth-500);">
                        <div class="comp-header">
                            <h3>Radix Nutrition</h3>
                            <span class="comp-badge">Trekking-Nahrung</span>
                        </div>
                        <div class="comp-body">
                            <div class="comp-pros">
                                <strong>Stärken:</strong>
                                <ul>
                                    <li>Hochfunktionell</li>
                                    <li>Wissenschaftlich optimiert</li>
                                </ul>
                            </div>
                            <div class="comp-cons">
                                <strong>Schwächen:</strong>
                                <ul>
                                    <li>Sehr teuer (6,50 - 8,00 €)</li>
                                    <li>Nur als Pulver transportierbar</li>
                                    <li>Nicht direkt als Riegel essbar</li>
                                </ul>
                            </div>
                        </div>
                        <div class="comp-usp">
                            <strong>WANDL. Vorteil:</strong><br>
                            Kalt als kompakter Snack unterwegs essbar.
                        </div>
                    </div>

                    <div class="comp-card" style="border-top: 4px solid var(--color-earth-300);">
                        <div class="comp-header">
                            <h3>Barebells</h3>
                            <span class="comp-badge">Fitness-Marktführer</span>
                        </div>
                        <div class="comp-body">
                            <div class="comp-pros">
                                <strong>Stärken:</strong>
                                <ul>
                                    <li>Sehr guter Geschmack</li>
                                    <li>Überall verfügbar</li>
                                </ul>
                            </div>
                            <div class="comp-cons">
                                <strong>Schwächen:</strong>
                                <ul>
                                    <li>Milchprotein (nicht vegan)</li>
                                    <li>Chemische Süßstoffe</li>
                                    <li>Kein Outdoor-Fokus</li>
                                </ul>
                            </div>
                        </div>
                        <div class="comp-usp">
                            <strong>WANDL. Vorteil:</strong><br>
                            Rein pflanzlich, Clean Label, echte Mahlzeit.
                        </div>
                    </div>

                </div>
            </div>
        </section>
        <!-- ============================================================
             NACHHALTIGKEIT'''
html = re.sub(old_comp, new_comp, html, flags=re.DOTALL)


# Sustainability Fullscreen Raw Image
old_sust = r'<section id="sustainability">.*?</section>\s*<!-- ============================================================\s*ALLERGEN-FREI'
new_sust = '''<section id="sustainability" style="width: 100%; height: 100vh; overflow: hidden; display: flex; justify-content: center; align-items: center; background: black;">
            <img src="assets/images/sustainability.png" alt="Unternehmerische Verantwortung" style="width: 100%; height: 100%; object-fit: cover;">
        </section>
        <!-- ============================================================
             ALLERGEN-FREI'''
html = re.sub(old_sust, new_sust, html, flags=re.DOTALL)


# Legal Centering
html = html.replace('<div class="legal-box" style="font-size: 1.5rem; font-weight: 600;">', '<div class="legal-box" style="font-size: 1.5rem; font-weight: 600; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 2rem;">')


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. CSS Updates
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Partners cut off text
css = css.replace(
    '#partners::before {\n    content: \'\';\n    position: absolute;\n    top: 0; left: 0; right: 0;\n    height: 150px;\n    background: linear-gradient(to bottom, var(--color-white), var(--color-earth-50));\n    pointer-events: none;\n    z-index: 1;\n}',
    '#partners::before {\n    content: \'\';\n    position: absolute;\n    top: 0; left: 0; right: 0;\n    height: 150px;\n    background: linear-gradient(to bottom, var(--color-white), var(--color-earth-50));\n    pointer-events: none;\n    z-index: 0;\n}\n#partners .container {\n    position: relative;\n    z-index: 2;\n    padding-top: 2rem;\n}'
)

# Fix Allergen grid spacing
css = css.replace(
    '#allergen-free .allergen-grid {\n    grid-template-columns: repeat(2, 1fr);\n    gap: 1.5rem;\n    margin-top: 2rem;\n}',
    '#allergen-free .allergen-grid {\n    display: flex;\n    flex-wrap: wrap;\n    justify-content: flex-start;\n    gap: 3rem !important;\n    margin-top: 3rem;\n}'
)

css += '''
/* Competition Cards Layout */
.competition-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}
.comp-card {
    background: var(--color-white);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
.comp-header {
    padding: 1.5rem;
    background: var(--color-earth-50);
    text-align: center;
    border-bottom: 1px solid var(--color-earth-100);
}
.comp-header h3 {
    margin: 0;
    font-size: 1.8rem;
    color: var(--color-earth-900);
}
.comp-badge {
    display: inline-block;
    background: var(--color-olive-100);
    color: var(--color-olive-700);
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-top: 0.5rem;
}
.comp-body {
    padding: 1.5rem;
    flex: 1;
}
.comp-pros, .comp-cons {
    margin-bottom: 1.5rem;
}
.comp-pros strong {
    color: var(--color-olive-600);
}
.comp-cons strong {
    color: #a83232;
}
.comp-body ul {
    list-style-type: none;
    padding: 0;
    margin-top: 0.5rem;
}
.comp-body ul li {
    padding-left: 1.5rem;
    position: relative;
    margin-bottom: 0.5rem;
}
.comp-pros ul li::before {
    content: '✓';
    color: var(--color-olive-500);
    position: absolute;
    left: 0;
}
.comp-cons ul li::before {
    content: '✗';
    color: #a83232;
    position: absolute;
    left: 0;
}
.comp-usp {
    padding: 1.5rem;
    background: var(--color-olive-500);
    color: var(--color-white);
    text-align: center;
    font-size: 1.1rem;
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied fixes.")
