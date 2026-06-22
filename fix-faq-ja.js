const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The file contains "Ja! Dank der Vorr\u00F6stung"
html = html.replace('<p>Ja! Dank der Vorr\u00F6stung', '<p>Ja, dank der Vorr\u00F6stung');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed Ja! to Ja, dank');
