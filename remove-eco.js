const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const lines = html.split('\n');
const newLines = lines.filter(line => !line.includes('Eco-Friendly:'));
html = newLines.join('\n');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Removed Eco-Friendly list item safely.');
