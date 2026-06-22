const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(/allergen-([^.]+)\.png/g, 'allergen-$1.png?v=hq2');
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added cache buster successfully');
