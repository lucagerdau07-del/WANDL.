const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The HTML contains: <p style="font-size: 0.85rem;">Rohstoffe, Verpackung, Etikett, Anteil Miete</p>
// Replace with: <p style="font-size: 0.85rem;">Rohstoffe, Verpackung, Etikett</p>

html = html.replace('Rohstoffe, Verpackung, Etikett, Anteil Miete', 'Rohstoffe, Verpackung, Etikett');
html = html.replace('Rohstoffe, Verpackung, Etikett, Anteil', 'Rohstoffe, Verpackung, Etikett'); // Just in case

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed unit costs label.');
