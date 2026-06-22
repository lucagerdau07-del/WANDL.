const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/alt="Ohne Gentechnik"/g, 'alt="Sulfitfrei"');
html = html.replace(/<span>Ohne Gentechnik<\/span>/g, '<span>Sulfitfrei</span>');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Ohne Gentechnik to Sulfitfrei');
