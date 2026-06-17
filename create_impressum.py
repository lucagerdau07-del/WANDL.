import glob
import re
import os

base_dir = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract Head
head_match = re.search(r'(<!DOCTYPE html>\s*<html lang="de">\s*<head>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else ''

# Clean GSAP from head for Impressum (not needed)
head = re.sub(r'<!-- GSAP & ScrollTrigger -->.*?</head>', '</head>', head, flags=re.DOTALL)
# Update title
head = re.sub(r'<title>.*?</title>', '<title>Impressum & Quellen | WANDL.</title>', head)

# Extract Nav
nav_match = re.search(r'(<body.*?>\s*<nav id="nav-main".*?</nav>)', html, re.DOTALL)
nav = nav_match.group(1) if nav_match else '<body><nav></nav>'

# Extract Footer
footer_match = re.search(r'(<footer id="footer">.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else '<footer></footer>'

# Build Impressum Content
impressum_content = f'''{head}
{nav}

    <main class="legal-main" style="padding: 160px 0 6rem 0; min-height: 80vh;">
        <div class="container" style="max-width: 800px;">
            <h1 style="font-size: 3.5rem; margin-bottom: 2rem; color: var(--color-earth-900);">Impressum</h1>
            
            <div class="legal-text" style="background: var(--color-white); padding: 3rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); margin-bottom: 5rem;">
                <h3 style="margin-bottom: 1rem;">Angaben gemäß § 5 TMG</h3>
                <p style="margin-bottom: 2rem;"><strong>WANDL. GbR</strong><br>
                [Musterstraße 123]<br>
                [20095 Hamburg]</p>
                
                <h3 style="margin-bottom: 1rem;">Vertreten durch</h3>
                <p style="margin-bottom: 2rem;">[Name Gründer 1]<br>
                [Name Gründer 2]</p>
                
                <h3 style="margin-bottom: 1rem;">Kontakt</h3>
                <p style="margin-bottom: 2rem;">Telefon: [0123 / 456789]<br>
                E-Mail: [info@wandl-foods.de]</p>
                
                <h3 style="margin-bottom: 1rem;">Umsatzsteuer-ID</h3>
                <p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz:<br>
                [DE999999999]</p>
            </div>

            <h1 style="font-size: 3.5rem; margin-bottom: 2rem; color: var(--color-earth-900);">Quellenverzeichnis</h1>
            <p style="margin-bottom: 3rem; font-size: 1.1rem; color: var(--color-earth-600);">Für alle auf dieser Website getroffenen ernährungsphysiologischen und marktbezogenen Aussagen beziehen wir uns auf folgende verifizierte Quellen und wissenschaftliche Studien:</p>
            
            <div class="sources-grid" style="display: grid; gap: 2rem;">
                
                <!-- Quelle 1 -->
                <div class="source-card" style="background: var(--color-earth-50); border-left: 4px solid var(--color-olive-500); padding: 2rem; border-radius: 0 var(--radius-md) var(--radius-md) 0;">
                    <span style="font-size: 0.9rem; font-weight: bold; color: var(--color-olive-600); text-transform: uppercase; letter-spacing: 1px;">Studie / Ernährung</span>
                    <h3 style="margin: 0.5rem 0; font-size: 1.2rem;">Proteinabsorption und Regeneration nach Ausdauersport</h3>
                    <p style="font-size: 0.95rem; color: var(--color-earth-600); margin-bottom: 1rem;">Grundlage für die Zusammensetzung unseres 20g pflanzlichen Protein-Profils.</p>
                    <a href="#" style="color: var(--color-olive-700); font-weight: 500; text-decoration: underline;">Quelle ansehen (PubMed) -></a>
                </div>

                <!-- Quelle 2 -->
                <div class="source-card" style="background: var(--color-earth-50); border-left: 4px solid var(--color-olive-500); padding: 2rem; border-radius: 0 var(--radius-md) var(--radius-md) 0;">
                    <span style="font-size: 0.9rem; font-weight: bold; color: var(--color-olive-600); text-transform: uppercase; letter-spacing: 1px;">Material & Nachhaltigkeit</span>
                    <h3 style="margin: 0.5rem 0; font-size: 1.2rem;">Zertifikate "jonatura" Monomaterial-Barrierebeutel</h3>
                    <p style="font-size: 0.95rem; color: var(--color-earth-600); margin-bottom: 1rem;">Nachweis für die 100%ige Kompostierbarkeit der Verpackung laut DIN EN 13432.</p>
                    <a href="#" style="color: var(--color-olive-700); font-weight: 500; text-decoration: underline;">Zertifikat ansehen -></a>
                </div>

                <!-- Quelle 3 -->
                <div class="source-card" style="background: var(--color-earth-50); border-left: 4px solid var(--color-olive-500); padding: 2rem; border-radius: 0 var(--radius-md) var(--radius-md) 0;">
                    <span style="font-size: 0.9rem; font-weight: bold; color: var(--color-olive-600); text-transform: uppercase; letter-spacing: 1px;">Marktdaten</span>
                    <h3 style="margin: 0.5rem 0; font-size: 1.2rem;">Wachstum des Trekking-Nahrung Marktes 2024-2030</h3>
                    <p style="font-size: 0.95rem; color: var(--color-earth-600); margin-bottom: 1rem;">Marktvolumen und Zielgruppen-Analyse, auf die sich unsere Pitch-Bewertungen stützen.</p>
                    <a href="#" style="color: var(--color-olive-700); font-weight: 500; text-decoration: underline;">Statista Report -></a>
                </div>

            </div>
        </div>
    </main>

{footer}

    <script src="js/navigation.js"></script>
</body>
</html>
'''

impressum_path = os.path.join(base_dir, 'impressum.html')
with open(impressum_path, 'w', encoding='utf-8') as f:
    f.write(impressum_content)

# Now update all HTML files to link to the new Impressum
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the impressum link in the footer
        new_content = re.sub(
            r'<li><a href="#">Impressum</a></li>',
            r'<li><a href="impressum.html">Impressum & Quellen</a></li>',
            content
        )
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("Impressum created and linked.")
