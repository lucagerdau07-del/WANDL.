import re
import os

# --- 1. CSS Updates ---
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Allergen background update
css = css.replace(
    'background: linear-gradient(135deg, var(--color-earth-900) 0%, var(--color-olive-800) 100%);',
    'background: linear-gradient(135deg, #111d11 0%, #2a402a 100%);'
)

css += '''
/* ==========================================================================
   NEW UPDATES FROM PLAN
   ========================================================================== */

/* Partner fade-in */
#partners {
    position: relative;
    background: var(--color-earth-50);
}
#partners::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 150px;
    background: linear-gradient(to bottom, var(--color-white), var(--color-earth-50));
    pointer-events: none;
    z-index: 1;
}

/* Allergen Grid Spacing & Contrast */
#allergen-free .allergen-grid {
    gap: 3rem !important;
}
#allergen-free h2, #allergen-free .section-sub, #allergen-free .label {
    color: #ffffff !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8) !important;
}
#allergen-free .allergen-icon {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
}

/* Zielgruppe Vertical Bars */
.target-vertical-grid {
    display: flex;
    gap: 2rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 3rem;
}
.target-bar {
    flex: 1;
    min-width: 250px;
    background: var(--color-earth-50);
    border-radius: var(--radius-lg);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: var(--shadow-sm);
    /* Initial state for animation */
    opacity: 0;
    transform: translateX(-50px);
    transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.target-bar.animate-in {
    opacity: 1;
    transform: translateX(0);
}
/* Staggered delays */
.target-bar:nth-child(1) { transition-delay: 0s; }
.target-bar:nth-child(2) { transition-delay: 0.2s; }
.target-bar:nth-child(3) { transition-delay: 0.4s; }

.target-placeholder {
    height: 250px;
    background: var(--color-earth-200);
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 4px solid var(--color-olive-500);
    font-size: 3rem;
    color: var(--color-earth-500);
}
.target-info {
    padding: 2rem;
    text-align: left;
}
.target-info h3 {
    margin-bottom: 1rem;
    font-size: 1.3rem;
    color: var(--color-olive-700);
}
.target-info p {
    font-size: 1rem;
    line-height: 1.6;
}

/* Sustainability Fullscreen Fix */
#sustainability {
    position: relative;
    color: var(--color-white);
    padding: var(--spacing-xxl) 0;
    background-image: url('../assets/images/sustainability.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
#sustainability::before {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    z-index: 1;
}
#sustainability .container {
    position: relative;
    z-index: 2;
}
#sustainability .sustain-item {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 1.5rem;
    border-radius: var(--radius-md);
    border: 1px solid rgba(255, 255, 255, 0.2);
}
#sustainability h4 {
    color: var(--color-white);
    margin-bottom: 0.5rem;
}
'''
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# --- 2. HTML Updates ---
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Zielgruppe
old_target = '''        <section id="target-audience">
            <div class="container">
                <h2 class="center-text">Unsere Zielgruppe</h2>
                <div class="split-layout">
                    <div class="text-content">
                        <h3>Welche Bedürfnisse haben diese Personen?</h3>
                        <ul class="benefit-list">
                            <li><strong>Outdoor-Enthusiasten:</strong> Suchen extrem leichte, nährstoffdichte und ungekühlt haltbare Nahrung für mehrtägige Touren.</li>
                            <li><strong>Büro-Krieger & Pendler:</strong> Brauchen eine schnelle, gesunde und sättigende Mahlzeit ohne Mittagstief.</li>
                            <li><strong>Sportler & Alpinisten:</strong> Benötigen Magen-schonende Energie und hochwertige Proteinquellen zur Regeneration.</li>
                        </ul>
                    </div>
                    <div class="image-content">
                        <div class="target-card" style="background: var(--color-earth-100); padding: 2rem; border-radius: var(--radius-lg); text-align: center;">
                            <span class="target-icon" style="font-size: 4rem; display: block; margin-bottom: 1rem;">🏔️</span>
                            <h4>Fokus: Zeit, Gewicht & Verträglichkeit</h4>
                            <p>WANDL. löst genau diese Schmerzpunkte durch die 2-in-1 Funktion und die allergenfreie Rezeptur.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
new_target = '''        <section id="target-audience">
            <div class="container">
                <h2 class="center-text">Unsere Zielgruppe</h2>
                <p class="center-text section-sub" style="margin-bottom: 3rem;">Welche Bedürfnisse haben diese Personen?</p>
                <div class="target-vertical-grid" id="target-anim-container">
                    
                    <div class="target-bar anim-target">
                        <div class="target-placeholder">🏔️</div>
                        <div class="target-info">
                            <h3>Outdoor-Enthusiasten</h3>
                            <p>Weitwanderer, Trekker, Bushcrafter und Camper suchen extrem leichte, nährstoffdichte Nahrung. <strong>Der Fokus:</strong> Wegfall von Gaskocher, Topf und schwerem Brennstoff.</p>
                        </div>
                    </div>
                    
                    <div class="target-bar anim-target">
                        <div class="target-placeholder">💼</div>
                        <div class="target-info">
                            <h3>Performers & Professionals</h3>
                            <p>Berufspendler und Studierende im stressigen Alltag brauchen eine schnelle, gesunde Mahlzeit. <strong>Der Fokus:</strong> Zubereitung in Sekunden ohne Mikrowelle – und langanhaltende Energie ohne Mittagstief.</p>
                        </div>
                    </div>
                    
                    <div class="target-bar anim-target">
                        <div class="target-placeholder">🧗‍♂️</div>
                        <div class="target-info">
                            <h3>Sportler & Alpinisten</h3>
                            <p>Maximale körperliche Belastung erfordert Regeneration. <strong>Der Fokus:</strong> 20g hochwertiges Protein, komplexe Kohlenhydrate und hundertprozentige Magenverträglichkeit ohne Allergene.</p>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''
html = html.replace(old_target, new_target)

# Replace Konkurrenz
old_comp = '''        <section id="competition">
            <div class="container">
                <h2 class="center-text">Konkurrenzanalyse</h2>
                <div class="competition-table-wrapper">
                    <table class="competition-table">
                        <thead>
                            <tr>
                                <th>Kriterium</th>
                                <th>WANDL.</th>
                                <th>Klassische Riegel</th>
                                <th>Trekking-Mahlzeiten</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Funktion</td>
                                <td><strong>Snack & Mahlzeit (2-in-1)</strong></td>
                                <td>Nur Snack</td>
                                <td>Nur Mahlzeit</td>
                            </tr>
                            <tr>
                                <td>Zubereitungszeit</td>
                                <td><strong>0s (kalt) / 90s (warm)</strong></td>
                                <td>0s</td>
                                <td>5-15 Min</td>
                            </tr>
                            <tr>
                                <td>Magenverträglichkeit</td>
                                <td><strong>Sehr hoch (Allergenfrei)</strong></td>
                                <td>Mittel (oft Nüsse/Soja)</td>
                                <td>Mittel (oft stark gewürzt)</td>
                            </tr>
                            <tr>
                                <td>Gewicht/Nutzen</td>
                                <td><strong>Extrem hoch</strong></td>
                                <td>Hoch</td>
                                <td>Mittel (viel Verpackung)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>'''
new_comp = '''        <section id="competition">
            <div class="container">
                <h2 class="center-text">Konkurrenzanalyse</h2>
                <div class="competition-table-wrapper">
                    <table class="competition-table">
                        <thead>
                            <tr>
                                <th>Marke / Kategorie</th>
                                <th>Stärken</th>
                                <th>Schwächen</th>
                                <th>WANDL. Vorteil (USP)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Clif Bar</strong></td>
                                <td>Hohe Bekanntheit, günstiger Preis (~2,49 €).</td>
                                <td>Nicht allergenfrei (Soja, Nüsse), klebrig bei Kälte, viel Zucker, nicht als Porridge nutzbar.</td>
                                <td><strong>100% Allergenfrei & 2-in-1 warm essbar.</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Radix Nutrition</strong><br><small>(Trekking-Nahrung)</small></td>
                                <td>Hochfunktionell, wissenschaftlich optimiert.</td>
                                <td>Sehr teuer (6,50-8€), nur als Pulver transportierbar (nicht als Riegel essbar).</td>
                                <td><strong>Kalt als Snack direkt auf der Hand verzehrbar.</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Barebells</strong></td>
                                <td>Marktführer im Fitnessbereich, sehr guter Geschmack.</td>
                                <td>Milchprotein (nicht vegan), chemische Süßstoffe, kein Outdoor-Fokus.</td>
                                <td><strong>Rein pflanzlich, Clean Label, echte Mahlzeit.</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>'''
html = html.replace(old_comp, new_comp)

# Replace Sustainability
old_sust = '''        <section id="sustainability">
            <div class="container split-layout">
                <div class="image-content">
                    <img src="assets/images/sustainability.png" alt="Unternehmerische Verantwortung" class="floating-image" style="border-radius: var(--radius-lg);">
                </div>
                <div class="text-content">
                    <h2 style="margin-bottom: 2rem;">Unternehmerische Verantwortung</h2>
                    <div class="sustain-items">
                        <div class="sustain-item">
                            <span class="sustain-icon">🌱</span>
                            <div>
                                <h4>Ökologische Nachhaltigkeit</h4>
                                <p>Recyclebare Monomaterial-Barrierebeutel (jonatura), vegane Zutaten mit geringem CO2-Abdruck, regionale Rohstoffe wo möglich.</p>
                            </div>
                        </div>
                        <div class="sustain-item">
                            <span class="sustain-icon">💶</span>
                            <div>
                                <h4>Ökonomische Nachhaltigkeit</h4>
                                <p>Fokus auf B2B-Pilotprojekte und Abo-Modell für planbare, wiederkehrende Umsätze und langfristige Stabilität.</p>
                            </div>
                        </div>
                        <div class="sustain-item">
                            <span class="sustain-icon">🤝</span>
                            <div>
                                <h4>Soziale Nachhaltigkeit</h4>
                                <p>Faire Produktion "Handgemacht in Hamburg". Langfristiges Ziel: Integration von Menschen mit Behinderung in die Verpackungsprozesse.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
new_sust = '''        <section id="sustainability">
            <div class="container">
                <h2 style="margin-bottom: 3rem; text-align: center; font-size: 3rem; text-shadow: 0 4px 15px rgba(0,0,0,0.8);">Unternehmerische Verantwortung</h2>
                <div class="sustain-items" style="max-width: 800px; margin: 0 auto;">
                    <div class="sustain-item">
                        <span class="sustain-icon">🌱</span>
                        <div>
                            <h4>Ökologische Nachhaltigkeit</h4>
                            <p>Recyclebare Monomaterial-Barrierebeutel (jonatura), vegane Zutaten mit geringem CO2-Abdruck, regionale Rohstoffe wo möglich.</p>
                        </div>
                    </div>
                    <div class="sustain-item">
                        <span class="sustain-icon">💶</span>
                        <div>
                            <h4>Ökonomische Nachhaltigkeit</h4>
                            <p>Fokus auf B2B-Pilotprojekte und Abo-Modell für planbare, wiederkehrende Umsätze und langfristige Stabilität.</p>
                        </div>
                    </div>
                    <div class="sustain-item">
                        <span class="sustain-icon">🤝</span>
                        <div>
                            <h4>Soziale Nachhaltigkeit</h4>
                            <p>Faire Produktion "Handgemacht in Hamburg". Langfristiges Ziel: Integration von Menschen mit Behinderung in die Verpackungsprozesse.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
html = html.replace(old_sust, new_sust)

# Force the Allergen Image to display correctly with width 100%
html = html.replace(
    '<img src="assets/images/allergen-bg.png" alt="Allergenfrei" class="floating-image" style="border-radius: var(--radius-lg); border: 2px solid rgba(255,255,255,0.1);">',
    '<img src="assets/images/allergen-bg.png" alt="Allergenfrei" class="floating-image" style="border-radius: var(--radius-lg); border: 2px solid rgba(255,255,255,0.1); width: 100%; height: auto; display: block;">'
)

# Force Design-4 Image to display correctly
html = html.replace(
    '<img src="assets/images/design-4.png" alt="Idee / Funktion: Design ohne Titel (4)" class="floating-image" style="max-height: 400px; object-fit: contain;">',
    '<img src="assets/images/design-4.png" alt="Idee / Funktion: Design ohne Titel (4)" class="floating-image" style="width: 100%; max-width: 600px; height: auto; object-fit: contain; margin: 0 auto; display: block;">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# --- 3. JS Update for Zielgruppe Animation ---
js_path = 'js/main.js'
js_addition = '''
// Animierte Zielgruppen Balken
document.addEventListener("DOMContentLoaded", () => {
    const targetAnimContainer = document.getElementById("target-anim-container");
    if(targetAnimContainer) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    const bars = targetAnimContainer.querySelectorAll(".anim-target");
                    bars.forEach(bar => bar.classList.add("animate-in"));
                    observer.unobserve(targetAnimContainer);
                }
            });
        }, { threshold: 0.2 });
        observer.observe(targetAnimContainer);
    }
});
'''
with open(js_path, 'a', encoding='utf-8') as f:
    f.write(js_addition)

print("Execution complete.")
