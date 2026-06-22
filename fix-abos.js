const fs = require('fs');

let html = fs.readFileSync('abos.html', 'utf8');

// Replace for Monthly
html = html.replace(
    /<li><strong>Spare 18 %<\/strong><\/li>/g,
    ''
);
html = html.replace(
    /<h3>WANDL\. Monthly<\/h3>/g,
    '<div class="save-badge">Spare 18 %</div>\n                        <h3>WANDL. Monthly</h3>'
);

// Replace for Expedition
html = html.replace(
    /<li><strong>Spare 22 %<\/strong><\/li>/g,
    ''
);
html = html.replace(
    /<h3>WANDL\. Expedition<\/h3>/g,
    '<div class="save-badge">Spare 22 %</div>\n                        <h3>WANDL. Expedition</h3>'
);

fs.writeFileSync('abos.html', html);
console.log('Fixed abos.html');
