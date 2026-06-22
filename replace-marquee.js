const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/assets\/images\/symbols\/icon_1\.png/g, 'assets/images/allergen-zucker.png');
html = html.replace(/assets\/images\/symbols\/icon_2\.png/g, 'assets/images/allergen-soja.png');
html = html.replace(/assets\/images\/symbols\/icon_3\.png/g, 'assets/images/allergen-erdnuss.png');
html = html.replace(/assets\/images\/symbols\/icon_4\.png/g, 'assets/images/allergen-milch.png');
html = html.replace(/assets\/images\/symbols\/icon_5\.png/g, 'assets/images/allergen-milch.png'); // Actually I could just replace both Laktose & Milch with Milchfrei
html = html.replace(/assets\/images\/symbols\/icon_6\.png/g, 'assets/images/allergen-gluten.png');
html = html.replace(/assets\/images\/symbols\/icon_7\.png/g, 'assets/images/allergen-gmo.png');
html = html.replace(/assets\/images\/symbols\/icon_8\.png/g, 'assets/images/allergen-ei.png');
html = html.replace(/assets\/images\/symbols\/icon_9\.png/g, 'assets/images/allergen-mais.png');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Replaced symbols in marquee');
