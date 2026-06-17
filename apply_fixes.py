import re

# --- 1. style.css changes ---
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make #vision text stand out more
css = css.replace('color: var(--color-white);', 'color: var(--color-white);\n    text-shadow: 0 2px 10px rgba(0,0,0,0.5);')

# Make #transformation video gap smaller by resetting height
css += '''
#transformation {
    height: auto !important;
    min-height: auto !important;
    padding-bottom: var(--spacing-xl) !important;
}

/* Hover effects for price cards */
.price-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.price-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

/* Make abo benefits larger */
.abo-benefits {
    font-size: 1.2rem;
}
.abo-benefit {
    padding: 0.75rem 1.5rem;
    font-size: 1.1rem;
    box-shadow: var(--shadow-sm);
    transform: scale(1.1);
    margin: 0.5rem;
}

/* Allergen-Free Section High Contrast Background */
#allergen-free {
    background: url('../assets/images/allergen-bg.png') center/cover no-repeat;
    position: relative;
    color: var(--color-white);
}
#allergen-free::before {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(30, 40, 20, 0.75); /* High contrast dark olive overlay */
    z-index: 1;
}
#allergen-free .container {
    position: relative;
    z-index: 2;
}
#allergen-free h2, #allergen-free .section-sub, #allergen-free .label {
    color: var(--color-white);
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}
#allergen-free .allergen-icon {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Increase font size for #legal text */
.legal-box {
    font-size: 1.2rem;
}
.legal-item h4 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
'''
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# --- 2. index.html changes ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Legal section: remove "& IP"
html = html.replace('<h2>Rechtsform & IP</h2>', '<h2>Rechtsform</h2>')

# Production section: aw-Wert and oxygen absorber
html = html.replace('<span>aw-Wert unter 0,65</span>', '<span>aw-Wert unter 0,65 (Wasseraktivität)</span>')
html = re.sub(r'<div class=\"detail-item\">\s*<span class=\"detail-icon\">🛡️</span>\s*<span>Sauerstoffabsorber \(0,05 €\)</span>\s*</div>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
