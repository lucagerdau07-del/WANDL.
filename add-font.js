const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Insert the font link in the <head> if not already there
if (!html.includes('Noto+Sans+Egyptian+Hieroglyphs')) {
    html = html.replace('</head>', '    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs&display=swap" rel="stylesheet">\n</head>');
}

// Update the Sesam span to use the font
html = html.replace(
    /(<span class="icon">)??(<\/span>\s*<span class="cross-line"><\/span>\s*<span class="label">Sesamfrei<\/span>)/g,
    '$1<span style="font-family: \'Noto Sans Egyptian Hieroglyphs\', sans-serif;">??</span>$2'
);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Added font successfully!');
