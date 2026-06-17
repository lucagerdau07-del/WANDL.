import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. `#allergen-free` split layout
allergen_replacement = '''
        <section id="allergen-free">
            <div class="container split-layout">
                <div class="text-content">
                    <h2>0 % Allergen-Falle<br>bei 20 % Proteindichte</h2>
                    <p class="section-sub">Frei von allen 14 EU-Hauptallergenen (Vegane Linie)</p>
                    <div class="allergen-grid">
                        <div class="allergen-icon">
                            <span class="icon">🥜</span>
                            <span class="cross-line"></span>
                            <span class="label">Erdnussfrei</span>
                        </div>
                        <div class="allergen-icon">
                            <span class="icon">🌾</span>
                            <span class="cross-line"></span>
                            <span class="label">Glutenfrei</span>
                        </div>
                        <div class="allergen-icon">
                            <span class="icon">🌱</span>
                            <span class="cross-line"></span>
                            <span class="label">Sojafrei</span>
                        </div>
                        <div class="allergen-icon">
                            <span class="icon">🥛</span>
                            <span class="cross-line"></span>
                            <span class="label">Milchfrei</span>
                        </div>
                    </div>
                </div>
                <div class="image-content">
                    <img src="assets/images/allergen-bg.png" alt="Allergenfrei" class="floating-image">
                </div>
            </div>
        </section>
'''
html = re.sub(r'<section id="allergen-free">.*?</section>', allergen_replacement, html, flags=re.DOTALL)

# 2. `#transformation` image instead of video
transformation_img_replacement = '''
                <div class="image-container reveal">
                    <img src="assets/images/design-4.png" alt="Idee / Funktion" class="floating-image">
                </div>
'''
html = re.sub(r'<div class="video-container reveal">.*?</div>\s*</div>', transformation_img_replacement, html, flags=re.DOTALL)


# 3. Insert Zutaten-Animation after `#hero`
ingredients_html = '''
        <!-- ============================================================
             ZUTATEN ANIMATION
             ============================================================ -->
        <section id="ingredients-animation">
            <div class="container">
                <div class="animation-placeholder">
                    <h2>Frame Scroll Animation für Zutaten</h2>
                    <p>(Wird hier integriert)</p>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\n\n        <!-- ============================================================', '</section>\n' + ingredients_html + '\n        <!-- ============================================================', 1)

# 4. Insert Zielgruppe, Konkurrenz, Nachhaltigkeit after `#usp`
new_sections_html = '''
        <!-- ============================================================
             ZIELGRUPPE
             ============================================================ -->
        <section id="target-audience">
            <div class="container">
                <h2 class="center-text">Unsere Zielgruppe</h2>
                <div class="split-layout">
                    <div class="text-content reveal">
                        <h3>Welche Bedürfnisse haben diese Personen?</h3>
                        <ul class="benefit-list">
                            <li><strong>Outdoor-Enthusiasten:</strong> Suchen extrem leichte, nährstoffdichte und ungekühlt haltbare Nahrung für mehrtägige Touren.</li>
                            <li><strong>Büro-Krieger & Pendler:</strong> Brauchen eine schnelle, gesunde und sättigende Mahlzeit ohne Mittagstief.</li>
                            <li><strong>Sportler & Alpinisten:</strong> Benötigen Magen-schonende Energie und hochwertige Proteinquellen zur Regeneration.</li>
                        </ul>
                    </div>
                    <div class="image-content reveal">
                        <div class="target-card">
                            <span class="target-icon">🏔️</span>
                            <h4>Fokus: Zeit, Gewicht & Verträglichkeit</h4>
                            <p>WANDL. löst genau diese Schmerzpunkte durch die 2-in-1 Funktion und die allergenfreie Rezeptur.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================
             KONKURRENZANALYSE
             ============================================================ -->
        <section id="competition">
            <div class="container">
                <h2 class="center-text">Wettbewerb & USP</h2>
                <div class="competition-table-wrapper reveal">
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
        </section>

        <!-- ============================================================
             NACHHALTIGKEIT
             ============================================================ -->
        <section id="sustainability">
            <div class="container split-layout">
                <div class="image-content reveal">
                    <img src="assets/images/sustainability.png" alt="Unternehmerische Verantwortung" class="floating-image" style="border-radius: var(--radius-lg);">
                </div>
                <div class="text-content reveal">
                    <h2>Unternehmerische Verantwortung</h2>
                    <div class="sustain-items">
                        <div class="sustain-item">
                            <span class="sustain-icon">🌱</span>
                            <div>
                                <h4>Ökologisch</h4>
                                <p>Recyclebare Monomaterial-Barrierebeutel (jonatura), vegane Zutaten mit geringem CO2-Abdruck, regionale Rohstoffe wo möglich.</p>
                            </div>
                        </div>
                        <div class="sustain-item">
                            <span class="sustain-icon">💶</span>
                            <div>
                                <h4>Ökonomisch</h4>
                                <p>Fokus auf B2B-Pilotprojekte und Abo-Modell für planbare, wiederkehrende Umsätze und langfristige Stabilität.</p>
                            </div>
                        </div>
                        <div class="sustain-item">
                            <span class="sustain-icon">🤝</span>
                            <div>
                                <h4>Sozial</h4>
                                <p>Faire Produktion "Handgemacht in Hamburg". Langfristiges Ziel: Integration von Menschen mit Behinderung in die Verpackungsprozesse.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\n\n        <!-- ============================================================', '</section>\n' + new_sections_html + '\n        <!-- ============================================================', 1) # Note: this will insert after hero or somewhere, let's target exact place

# Since I already did a replace, let's be more specific for insertion after #usp
html_parts = html.split('<section id="allergen-free">')
if len(html_parts) > 1:
    html = html_parts[0] + new_sections_html + '<section id="allergen-free">' + html_parts[1]


# 5. Insert Finanzierung & Partner after #legal
finance_partner_html = '''
        <!-- ============================================================
             FINANZIERUNG
             ============================================================ -->
        <section id="finance">
            <div class="container">
                <h2 class="center-text">Finanzierung & Kennzahlen</h2>
                <div class="finance-grid">
                    <div class="finance-card reveal">
                        <div class="finance-icon">💰</div>
                        <h3>Investitionen (Beginn)</h3>
                        <p class="finance-value">5.000 €</p>
                        <p>Für Gewerbeküche-Miete, Erstbestand an Zutaten, Verpackungsmaschine und Markenanmeldung. Finanziert aus Eigenmitteln (Bootstrapping).</p>
                    </div>
                    <div class="finance-card reveal">
                        <div class="finance-icon">🔄</div>
                        <h3>Laufende Ausgaben</h3>
                        <p class="finance-value">1,50 € / Riegel</p>
                        <p>Zutaten, Verpackung, Miete und Marketing. Kalkuliert für die Anfangsphase im Geschäftsbetrieb.</p>
                    </div>
                    <div class="finance-card reveal highlight">
                        <div class="finance-icon">🏷️</div>
                        <h3>Produktpreis</h3>
                        <p class="finance-value">4,90 €</p>
                        <p>UVP im Einzelverkauf. Im Abo vergünstigt bis zu 22% (ab 3,82 €).</p>
                    </div>
                    <div class="finance-card reveal">
                        <div class="finance-icon">📈</div>
                        <h3>Umsatz (Jahr 1)</h3>
                        <p class="finance-value">50.000 €</p>
                        <p>Konservative Schätzung basierend auf B2B-Vorbestellungen und D2C Online-Launch.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================
             PARTNER
             ============================================================ -->
        <section id="partners">
            <div class="container center-text">
                <h2>Unsere Partner</h2>
                <div class="partner-grid reveal">
                    <div class="partner-card">
                        <span class="partner-icon">📦</span>
                        <h4>jonatura</h4>
                        <p>Lieferant für nachhaltige Barriere-Beutel</p>
                    </div>
                    <div class="partner-card">
                        <span class="partner-icon">🍳</span>
                        <h4>Kitchen Town Hamburg</h4>
                        <p>Zentrale Produktionsstätte (Mietküche)</p>
                    </div>
                    <div class="partner-card">
                        <span class="partner-icon">🏕️</span>
                        <h4>Globetrotter (Geplant)</h4>
                        <p>Strategischer B2B-Vertriebspartner</p>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\n\n        <!-- ============================================================\n             VISION', '</section>\n' + finance_partner_html + '\n        <!-- ============================================================\n             VISION')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# --- 6. style.css changes ---
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '''
/* ==========================================================================
   NEW PITCH SECTIONS
   ========================================================================== */
.split-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.floating-image {
    width: 100%;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 20px 30px rgba(0,0,0,0.15));
}

#allergen-free {
    background: var(--color-earth-900);
    padding: var(--spacing-xl) 0;
}
#allergen-free::before {
    display: none;
}
#allergen-free .text-content {
    color: var(--color-white);
    text-align: left;
}
#allergen-free h2, #allergen-free .section-sub {
    text-shadow: none;
}
#allergen-free .allergen-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-top: 2rem;
}
#allergen-free .allergen-icon {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.animation-placeholder {
    width: 100%;
    height: 60vh;
    border: 3px dashed var(--color-earth-300);
    border-radius: var(--radius-xl);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--color-earth-50);
    color: var(--color-earth-500);
    margin: var(--spacing-lg) 0;
}

/* Timeline text contrast */
.timeline-content {
    background: var(--color-white) !important;
    color: var(--color-earth-900) !important;
    box-shadow: var(--shadow-md) !important;
}
.timeline-content h3 {
    color: var(--color-olive-700) !important;
}

/* Competition Table */
.competition-table-wrapper {
    overflow-x: auto;
    background: var(--color-white);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-md);
    margin-top: 2rem;
}
.competition-table {
    width: 100%;
    border-collapse: collapse;
}
.competition-table th, .competition-table td {
    padding: 1.5rem;
    text-align: left;
    border-bottom: 1px solid var(--color-earth-100);
}
.competition-table th {
    background: var(--color-earth-50);
    font-weight: 600;
    color: var(--color-earth-900);
}

/* Finance Grid */
.finance-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}
.finance-card {
    background: var(--color-white);
    padding: 2rem;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    text-align: center;
}
.finance-card.highlight {
    border: 2px solid var(--color-olive-500);
    transform: scale(1.05);
}
.finance-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--color-olive-700);
    margin: 1rem 0;
    font-family: var(--font-display);
}

/* Partner Grid */
.partner-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}
.partner-card {
    background: var(--color-earth-50);
    padding: 2rem;
    border-radius: var(--radius-md);
}
.partner-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
}

/* Sustainability */
.sustain-item {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
}
.sustain-icon {
    font-size: 2.5rem;
}

@media (max-width: 768px) {
    .split-layout {
        grid-template-columns: 1fr;
    }
}

/* Removing Gap in #transformation */
.image-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.image-container img {
    max-width: 100%;
    height: auto;
}
'''
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied new sections and CSS.")
