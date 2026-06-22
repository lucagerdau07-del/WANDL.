const fs = require('fs');
const sharp = require('sharp');
const path = require('path');

const src = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/SKIZZE/Allergne/design (1)-Picsart-BackgroundRemover.png';
const dest = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/wandl-website/assets/images/allergen-soja.png';

async function run() {
    await sharp(src)
        .trim() // Remove transparent padding
        .resize(256, 256, { fit: 'contain', background: {r:0,g:0,b:0,alpha:0} }) // Resize to exact dimensions
        .png()
        .toFile(dest);
        
    // Bust cache
    let html = fs.readFileSync('index.html', 'utf8');
    html = html.replace(/(\.png\?v=hq4)/g, '.png?v=hq5');
    fs.writeFileSync('index.html', html, 'utf8');
    
    console.log('Processed new soja logo successfully!');
}
run();
