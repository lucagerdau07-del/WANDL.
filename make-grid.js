const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const dir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/SKIZZE/Allergne';
const files = ['4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png'];

async function run() {
    const compositeArray = [];
    for(let i=0; i<files.length; i++) {
        const row = Math.floor(i / 4);
        const col = i % 4;
        
        // Resize them so the grid is small enough
        const buffer = await sharp(path.join(dir, files[i])).resize(100, 100).png().toBuffer();
        
        compositeArray.push({
            input: buffer,
            top: row * 120,
            left: col * 120
        });
    }
    
    await sharp({
        create: {
            width: 480,
            height: 360,
            channels: 4,
            background: { r: 255, g: 255, b: 255, alpha: 1 }
        }
    })
    .composite(compositeArray)
    .toFile('preview-grid.jpg');
}
run();
