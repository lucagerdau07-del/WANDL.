const fs = require('fs');
const path = require('path');

const srcDir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/SKIZZE/Allergne';
const destDir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/wandl-website/assets/images';

const map = {
    '4.png': 'allergen-gluten.png',
    '5.png': 'allergen-milch.png',
    '6.png': 'allergen-ei.png',
    '7.png': 'allergen-mais.png',
    '8.png': 'allergen-sesam.png',
    '9.png': 'allergen-erdnuss.png',
    '10.png': 'allergen-fisch.png',
    '11.png': 'allergen-soja.png',
    '12.png': 'allergen-meeresfruechte.png',
    '13.png': 'allergen-zucker.png',
    '14.png': 'allergen-gmo.png',
    '15.png': 'allergen-lupinen.png'
};

for (const [src, dest] of Object.entries(map)) {
    fs.copyFileSync(path.join(srcDir, src), path.join(destDir, dest));
}

// Bust cache again in index.html
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(/(\.png\?v=hq2)/g, '.png?v=hq3');
fs.writeFileSync('index.html', html, 'utf8');

console.log('Done mapping user icons!');
