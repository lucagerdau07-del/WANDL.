import sys
import re

path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Partner Marquee
track_pattern = re.compile(r'(<div class=\"logo-track\">)(.*?)(</div>\s*</div>)', re.DOTALL)
new_track = r'''\1
                    <div class="logo-item">Kitchen4Rent</div>
                    <div class="logo-item">jonatura</div>
                    <div class="logo-item">V Label Vegan</div>
                    <div class="logo-item">youstartN</div>
                    <div class="logo-item">Nutrikal</div>
                    <div class="logo-item">Kitchen4Rent</div>
                    <div class="logo-item">jonatura</div>
                    <div class="logo-item">V Label Vegan</div>
                    <div class="logo-item">youstartN</div>
                    <div class="logo-item">Nutrikal</div>
                \3'''
text = track_pattern.sub(new_track, text)

# 2. Update Finance Section
finance_old = re.compile(r'<h2 class=\"center-text\">Finanzierung & Kennzahlen</h2>.*?<div class=\"finance-card\">.*?Umsatz.*?</div>\s*</div>', re.DOTALL)
finance_new = '''<h2 class="center-text">Finanzierung & Kennzahlen</h2>
                <div class="finance-grid" style="grid-template-columns: 1fr;">
                    
                    <!-- Zeile 1: Startkapital & Prognose -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                        <div class="finance-card">
                            <h3>Startkapital</h3>
                            <p class="finance-value" style="font-size: 2.5rem; color: var(--color-earth-900);">1.886,00 €</p>
                            <p>Finanziert durch Eigenkapital der Gründer, Crowdfunding und die youstartN Förderung. Deckt Miete, Erstbestand an Zutaten, Verpackung und Zertifizierungen (wie das V Label).</p>
                        </div>
                        <div class="finance-card highlight">
                            <h3>Ein Jahres Prognose</h3>
                            <p class="finance-value" style="font-size: 2.5rem;">31.164,00 €</p>
                            <p style="font-weight: bold; margin-bottom: 0.5rem;">Umsatz bei Verkauf von 6.360 Riegeln.</p>
                            <p>Dies entspricht einem prognostizierten Nettogewinn von 18.541,00 € im ersten vollen Geschäftsjahr.</p>
                        </div>
                    </div>

                    <!-- Zeile 2: Transparenter Rechenweg (Break Even) -->
                    <div class="finance-card" style="margin-top: 1rem;">
                        <h3 style="margin-bottom: 1.5rem; border-bottom: 1px solid var(--color-earth-100); padding-bottom: 1rem;">Kalkulation und Gewinnschwelle</h3>
                        
                        <div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: space-between; margin-bottom: 2rem;">
                            <div style="flex: 1; min-width: 200px;">
                                <p style="font-size: 0.9rem; color: var(--color-earth-400); text-transform: uppercase; font-weight: bold;">Verkaufspreis</p>
                                <p style="font-size: 2rem; font-weight: 800; color: var(--color-earth-900);">4,90 €</p>
                                <p style="font-size: 0.85rem;">Regulärer Einzelpreis</p>
                            </div>
                            <div style="font-size: 2rem; color: var(--color-earth-300); font-weight: 300; display: flex; align-items: center;">minus</div>
                            <div style="flex: 1; min-width: 200px;">
                                <p style="font-size: 0.9rem; color: var(--color-earth-400); text-transform: uppercase; font-weight: bold;">Stückkosten</p>
                                <p style="font-size: 2rem; font-weight: 800; color: var(--color-earth-900);">1,77 €</p>
                                <p style="font-size: 0.85rem;">Rohstoffe, Verpackung, Etikett, Anteil Miete</p>
                            </div>
                            <div style="font-size: 2rem; color: var(--color-earth-300); font-weight: 300; display: flex; align-items: center;">ergibt</div>
                            <div style="flex: 1; min-width: 200px;">
                                <p style="font-size: 0.9rem; color: var(--color-earth-400); text-transform: uppercase; font-weight: bold;">Deckungsbeitrag</p>
                                <p style="font-size: 2rem; font-weight: 800; color: var(--color-olive-500);">3,13 €</p>
                                <p style="font-size: 0.85rem;">Solide Marge von knapp 64 Prozent</p>
                            </div>
                        </div>

                        <div style="background: var(--color-earth-50); padding: 1.5rem; border-radius: 15px;">
                            <p style="margin-bottom: 0.5rem; font-weight: bold;">Berechnung der Gewinnschwelle pro Monat:</p>
                            <p style="font-size: 1.2rem; margin-bottom: 0;">Fixkosten (114,50 €) geteilt durch Deckungsbeitrag (3,13 €) gleich <strong>37 Riegel</strong>.</p>
                            <p style="font-size: 0.9rem; color: var(--color-earth-500); margin-top: 0.5rem;">Bereits ab dem siebenunddreißigsten verkauften Riegel pro Monat arbeiten wir profitabel.</p>
                        </div>
                    </div>

                </div>'''
text = finance_old.sub(finance_new, text)

# 3. Insert "Marktpotenzial" and "Go To Market" right before the Finance section
marketing_section = '''        </section>

        <!-- ============================================================
             MARKT & VERTRIEB (Neu aus PDF)
             ============================================================ -->
        <section style="padding: 5rem 0; background-color: var(--color-earth-50);">
            <div class="container">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 3rem;">
                    
                    <!-- Marktpotenzial -->
                    <div>
                        <h2 style="margin-bottom: 1.5rem;">Marktpotenzial</h2>
                        <p style="margin-bottom: 1rem; font-size: 1.1rem; line-height: 1.8;">Das Premium Segment für funktionelle Outdoor Nahrung wächst extrem stark. Kunden in dieser Nische sind qualitätsbewusst und suchen nach echten Problemlösern wie einer warmen Mahlzeit ohne schweres Kochgeschirr.</p>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Große Zielgruppe:</strong> In Deutschland wandern über vierzig Millionen Menschen regelmäßig. Der fokussierte DACH Raum umfasst hierbei circa zwei Millionen hochaffine Personen.</li>
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Milliardenmarkt:</strong> Der Markt für Sporternährung und Mahlzeitersatz in DACH liegt bei über 1,2 Milliarden Euro mit konstanten Zuwachsraten von acht bis zehn Prozent.</li>
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Pflanzlicher Trend:</strong> Circa acht Millionen Vegetarier und knapp zwei Millionen Veganer in Deutschland fordern zunehmend rein pflanzliche Innovationen.</li>
                        </ul>
                    </div>

                    <!-- Vertrieb & Go To Market -->
                    <div>
                        <h2 style="margin-bottom: 1.5rem;">Vertrieb und Marketing</h2>
                        <p style="margin-bottom: 1rem; font-size: 1.1rem; line-height: 1.8;">Wir setzen auf maximale Authentizität durch Dokumentation unserer Gründungsgeschichte auf Social Media.</p>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Transparente Gründung:</strong> Videoreihe auf TikTok und Instagram Reels. Wir geben transparente Einblicke in die Produktion, die Finanzen und auch in Rückschläge.</li>
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Virale Transformation:</strong> Hero Content Videos zeigen visuell beeindruckend die Verwandlung vom kompakten Riegel zum cremigen, warmen Porridge.</li>
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Influencer Kampagne:</strong> Direkter Versand von Probierboxen an ausgewählte Wander Blogger und vegane Fitness Creator.</li>
                            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><span style="position: absolute; left: 0; color: var(--color-olive-500);">✓</span> <strong>Vertriebsaufbau:</strong> Phase Eins startet über den eigenen Shopify Shop mit klarem Fokus auf das Abonnement Modell. Phase Zwei fokussiert sich auf B2B Listungen in Hamburger Fachgeschäften wie Globetrotter.</li>
                        </ul>
                    </div>

                </div>
            </div>
        </section>

        <!-- ============================================================
             FINANZIERUNG
             ============================================================ -->'''
text = text.replace('        <!-- ============================================================\n             FINANZIERUNG\n             ============================================================ -->', marketing_section)


with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
