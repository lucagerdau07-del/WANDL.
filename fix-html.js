const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const zuckerRegex = / *<div class="symbol-item">\s*<img src="assets\/images\/allergen-zucker\.png\?v=hq[0-9]+" alt="Ohne Zucker">\s*<span>Ohne Zucker<\/span>\s*<\/div>\s*/g;
const laktoseRegex = / *<div class="symbol-item">\s*<img src="assets\/images\/allergen-milch\.png\?v=hq[0-9]+" alt="Laktosefrei">\s*<span>Laktosefrei<\/span>\s*<\/div>\s*/g;

html = html.replace(zuckerRegex, '');
html = html.replace(laktoseRegex, '');
html = html.replace(/(\.png\?v=hq3)/g, '.png?v=hq4');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed HTML successfully');
