const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The text has special characters "für" so we use a simple script to avoid powershell encoding issues.
html = html.replace('Keinerlei Eignung', 'Keine Eignung');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed outdoor wording.');
