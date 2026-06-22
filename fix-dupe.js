const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// I will just wipe out anything inside <span class="icon">...</span> right before the Sesamfrei label
html = html.replace(
    /<div class="allergen-icon">\s*<span class="icon">.*?<\/span>\s*<span class="cross-line"><\/span>\s*<span class="label">Sesamfrei<\/span>\s*<\/div>/g,
    '<div class="allergen-icon">\n                              <span class="icon"><span style="font-family: \'Noto Sans Egyptian Hieroglyphs\', sans-serif;">??</span></span>\n                              <span class="cross-line"></span>\n                              <span class="label">Sesamfrei</span>\n                          </div>'
);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed duplication successfully!');
