const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/Subscription-Modell/g, 'Abo-Modell');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed Subscription wording.');
