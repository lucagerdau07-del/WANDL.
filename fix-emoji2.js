const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the block for Sesamfrei and replace the span class="icon" content
html = html.replace(
    /(<span class="icon">)??(<\/span>\s*<span class="cross-line"><\/span>\s*<span class="label">Sesamfrei<\/span>)/g,
    '$1??$2'
);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Replaced emoji successfully with ??!');
