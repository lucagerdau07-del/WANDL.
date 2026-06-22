const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Fix Müllreduktion text
html = html.replace('recyclebaren jonatura Barriere-Beuteln', 'recyclebaren Barriere-Beuteln');

// Fix Lokales Engagement (removing the whole <li> safely)
// We split by newline, filter out the line containing "Lokales Engagement:", and join back.
const lines = html.split('\n');
const newLines = lines.filter(line => !line.includes('Lokales Engagement:'));
html = newLines.join('\n');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed both items safely.');
