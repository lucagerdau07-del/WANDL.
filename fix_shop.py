import re

with open('shop.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Original
text = re.sub(
    r'<div class="product-image-placeholder">.*?</div>\s*<div class="product-info">\s*<span class="product-code">WANDL-01</span>\s*<h3>Original</h3>',
    '<a href="product.html?id=original"><img src="https://placehold.co/600x600/e2e8f0/64748b?text=WANDL.+Original" alt="Original" style="width: 100%; border-radius: 8px; margin-bottom: 1rem;"></a>\n                        <div class="product-info">\n                            <span class="product-code">WANDL-01</span>\n                            <h3><a href="product.html?id=original" style="color: inherit; text-decoration: none;">Original</a></h3>',
    text, flags=re.DOTALL
)

# Replace Dark
text = re.sub(
    r'<div class="product-image-placeholder">.*?</div>\s*<div class="product-info">\s*<span class="product-code">WANDL-02</span>\s*<h3>Dark</h3>',
    '<a href="product.html?id=dark"><img src="https://placehold.co/600x600/e2e8f0/64748b?text=WANDL.+Dark" alt="Dark" style="width: 100%; border-radius: 8px; margin-bottom: 1rem;"></a>\n                        <div class="product-info">\n                            <span class="product-code">WANDL-02</span>\n                            <h3><a href="product.html?id=dark" style="color: inherit; text-decoration: none;">Dark</a></h3>',
    text, flags=re.DOTALL
)

# Replace Spice
text = re.sub(
    r'<div class="product-image-placeholder">.*?</div>\s*<div class="product-info">\s*<span class="product-code">WANDL-03</span>\s*<h3>Spice</h3>',
    '<a href="product.html?id=spice"><img src="https://placehold.co/600x600/e2e8f0/64748b?text=WANDL.+Spice" alt="Spice" style="width: 100%; border-radius: 8px; margin-bottom: 1rem;"></a>\n                        <div class="product-info">\n                            <span class="product-code">WANDL-03</span>\n                            <h3><a href="product.html?id=spice" style="color: inherit; text-decoration: none;">Spice</a></h3>',
    text, flags=re.DOTALL
)

# Replace Classic
text = re.sub(
    r'<div class="product-image-placeholder">.*?</div>\s*<div class="product-info">\s*<span class="product-code">WANDL-04</span>\s*<h3>Classic Creamy.*?</h3>',
    '<a href="product.html?id=classic"><img src="https://placehold.co/600x600/e2e8f0/64748b?text=WANDL.+Classic" alt="Classic" style="width: 100%; border-radius: 8px; margin-bottom: 1rem;"></a>\n                        <div class="product-info">\n                            <span class="product-code">WANDL-04</span>\n                            <h3><a href="product.html?id=classic" style="color: inherit; text-decoration: none;">Classic Creamy</a></h3>',
    text, flags=re.DOTALL
)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Replaced in shop.html')
