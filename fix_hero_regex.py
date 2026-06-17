import re

html_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Match the entire hero section and the ingredients animation section up to the next separator
old_block = r'<section id="hero".*?</section>\s*<!-- ============================================================\s*ZUTATEN ANIMATION\s*============================================================ -->\s*<section id="ingredients-animation">.*?</section>\s*<!-- ============================================================\s*HOW IT WORKS'

new_hero = '''<section id="sv-section" class="sv-section">
            <div class="sv-sticky">
                <canvas id="sv-canvas" class="sv-canvas"></canvas>
                <div class="sv-overlay"></div>
                
                <!-- Overlay Texts (like Standalone) -->
                <div class="sv-text sv-text-1">
                    <h1 class="hero-title" style="font-size: clamp(3rem, 8vw, 6rem);">Snack & Mahlzeit.</h1>
                    <p class="hero-subtitle">1 Riegel. 2 Funktionen.</p>
                </div>
                <div class="sv-text sv-text-2">
                    <h2>350 kcal pure Energie.</h2>
                    <p>100% kompostierbar. Rein pflanzlich.</p>
                </div>
                <div class="sv-text sv-text-3">
                    <h2>Das Outdoor-Upgrade.</h2>
                    <a href="shop.html" class="btn btn-primary" style="margin-top: 2rem;">Zum Shop</a>
                </div>
            </div>
        </section>

        <!-- ============================================================
             HOW IT WORKS'''

html = re.sub(old_block, new_hero, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero successfully replaced.")
