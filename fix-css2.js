const fs = require('fs');

// 1. Update CSS to 12px
let css = fs.readFileSync('css/style.css', 'utf8');
css = css.replace('transform: translateY(6px);', 'transform: translateY(12px);');
fs.writeFileSync('css/style.css', css, 'utf8');

// 2. Bust CSS cache in index.html
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(/href="css\/style\.css(\?v=[0-9]+)?"/g, 'href="css/style.css?v=' + Date.now() + '"');
fs.writeFileSync('index.html', html, 'utf8');

console.log('CSS fixed and cache busted!');
