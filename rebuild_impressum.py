import re
import os

base_dir = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website'
html_path = os.path.join(base_dir, 'impressum.html')

# We'll create a completely clean HTML structure for the sources
content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quellenverzeichnis | WANDL.</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
        .sources-main {
            padding: 150px 20px 100px 20px;
            max-width: 900px;
            margin: 0 auto;
            min-height: 100vh;
        }
        .sources-header {
            margin-bottom: 3rem;
        }
        .sources-header h1 {
            font-size: 3rem;
            color: var(--color-earth-900);
            margin-bottom: 1rem;
        }
        .sources-header p {
            font-size: 1.2rem;
            color: var(--color-earth-600);
            line-height: 1.6;
        }
        .sources-list {
            list-style: none;
            padding: 0;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        .source-item {
            background: var(--color-white);
            border: 1px solid var(--color-earth-200);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
            display: block;
            text-decoration: none;
            color: inherit;
        }
        .source-item:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
            border-color: var(--color-olive-500);
        }
        .source-category {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--color-olive-600);
            font-weight: 700;
            margin-bottom: 0.5rem;
            display: block;
        }
        .source-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--color-earth-900);
            margin-bottom: 0.5rem;
        }
        .source-desc {
            font-size: 1rem;
            color: var(--color-earth-600);
            line-height: 1.5;
        }
    </style>
</head>
<body style="background: var(--color-earth-50);">

    <!-- Simple Nav -->
    <nav id="nav-main" style="background: var(--color-earth-50); border-bottom: 1px solid var(--color-earth-200);">
        <div class="nav-container">
            <a href="index.html" class="logo"><img src="assets/images/logo-v4.png?v=1781718409" alt="WANDL. Logo" style="height: 35px; filter: brightness(0); display: block;"></a>
            <ul class="nav-links">
                <li><a href="index.html#how-it-works">Idee</a></li>
                <li><a href="index.html#usp">Unser Riegel</a></li>
                <li><a href="shop.html">Shop</a></li>
                <li><a href="abos.html">Abos</a></li>
            </ul>
            <a href="shop.html" class="btn-primary nav-cta">Zum Shop</a>
        </div>
    </nav>

    <main class="sources-main">
        <div class="sources-header">
            <h1>Quellenverzeichnis</h1>
            <p>Hier findest du alle wissenschaftlichen Studien, Marktanalysen und Zertifikate, auf die sich unsere Aussagen, Versprechen und Produkt-Entwicklungen stützen.</p>
        </div>

        <div class="sources-list">
            
            <a href="#" class="source-item">
                <span class="source-category">Studie / Ernährung</span>
                <div class="source-title">Proteinbedarf im Ausdauersport</div>
                <div class="source-desc">Eine umfassende Meta-Analyse zur optimalen Proteinzufuhr (20g-Fenster) während und nach intensiven Trekking-Touren.</div>
            </a>

            <a href="#" class="source-item">
                <span class="source-category">Zertifikat / Verpackung</span>
                <div class="source-title">DIN EN 13432 - Industrielle Kompostierbarkeit</div>
                <div class="source-desc">Offizieller Nachweis zur 100%igen Kompostierbarkeit unserer jonatura Monomaterial-Barrierebeutel.</div>
            </a>

            <a href="#" class="source-item">
                <span class="source-category">Marktdaten</span>
                <div class="source-title">Global Trekking Nutrition Market Report 2024</div>
                <div class="source-desc">Marktforschung und Zielgruppen-Analyse, welche das enorme Wachstumspotenzial von 2-in-1 Mahlzeiten belegt.</div>
            </a>

            <a href="#" class="source-item">
                <span class="source-category">Wissenschaft / Allergene</span>
                <div class="source-title">Prävalenz der 14 EU-Hauptallergene</div>
                <div class="source-desc">Studie des Europäischen Instituts für Lebensmittelallergien über die steigende Relevanz allergenfreier Notfallnahrung.</div>
            </a>

            <a href="#" class="source-item">
                <span class="source-category">Ernährung</span>
                <div class="source-title">Thermische Energie & Verdauung</div>
                <div class="source-desc">Studie darüber, wie warme Mahlzeiten (unser Porridge-Konzept) die Nährstoffaufnahme in kalten Umgebungen (Alpenismus) im Vergleich zu kalten Snacks verbessern.</div>
            </a>
            
        </div>
    </main>

    <footer id="footer" style="margin-top: 0;">
        <div class="container">
            <div class="bottom-bar" style="border-top: none; padding-top: 0;">
                <p>&copy; 2026 WANDL. GbR, Hamburg. Alle Rechte vorbehalten. | <a href="index.html" style="color: var(--color-earth-600);">Zurück zur Startseite</a></p>
            </div>
        </div>
    </footer>

    <script src="js/navigation.js"></script>
</body>
</html>
'''

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("impressum.html completely rebuilt as a clean links list.")
