const fs = require('fs');
const sharp = require('sharp');
const path = require('path');

const dir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/wandl-website/assets/images';

async function run() {
    const files = fs.readdirSync(dir).filter(f => f.startsWith('allergen-') && f.endsWith('.png') && !f.includes('transparent'));
    
    for (const f of files) {
        const fullPath = path.join(dir, f);
        const buffer = fs.readFileSync(fullPath);
        
        await sharp(buffer)
            // Trim the white background first so it fills the square perfectly
            .trim({ threshold: 10 })
            .resize(256, 256, { fit: 'contain', background: {r:255,g:255,b:255,alpha:0} })
            .composite([{
                input: Buffer.from('<svg><circle cx="128" cy="128" r="126" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png()
            .toFile(path.join(dir, 'tmp-' + f));
            
        fs.renameSync(path.join(dir, 'tmp-' + f), fullPath);
    }
    console.log('Masked all images!');
}
run();
