const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace('Marge von knapp 64 Prozent', 'Marge von ca. 64 Prozent');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed Marge text.');
