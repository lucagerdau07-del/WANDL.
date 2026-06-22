const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace "schmeckt es auch kalt hervorragend" with "schmeckt es auch kalt gut"
html = html.replace('schmeckt es auch kalt hervorragend', 'schmeckt es auch kalt gut');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed hervorragend to gut');
