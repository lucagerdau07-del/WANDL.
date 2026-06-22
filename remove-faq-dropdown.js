const fs = require('fs');

const files = [
    'index.html',
    'shop.html',
    'checkout.html',
    'success.html',
    'abos.html',
    'impressum.html',
    'product-original.html',
    'product-dark.html',
    'product-spice.html',
    'product-classic.html',
    'lieferant.html'
];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        content = content.replace(/\s*<a href="[^"]*#faq">FAQ<\/a>/g, '');
        fs.writeFileSync(file, content, 'utf8');
    }
});

console.log('Removed FAQ from dropdowns.');
