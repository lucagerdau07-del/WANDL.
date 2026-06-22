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
        content = content.replace(/href="css\/style\.css\?v=1\.0\.4"/g, 'href="css/style.css?v=1.0.5"');
        fs.writeFileSync(file, content, 'utf8');
    }
});
console.log('Fixed CSS cache busting to 1.0.5.');
