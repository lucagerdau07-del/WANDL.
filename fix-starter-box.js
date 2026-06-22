const fs = require('fs');
let html = fs.readFileSync('abos.html', 'utf8');

html = html.replace('<li>Alle 3 Sorten enthalten</li>', '<li><strong>Kostenloser Versand</strong></li>');

fs.writeFileSync('abos.html', html);
console.log('Fixed starter box text in abos.html');
