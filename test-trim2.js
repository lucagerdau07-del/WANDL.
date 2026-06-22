const sharp = require('sharp');

async function run() {
    try {
        const img = sharp('assets/images/allergen-icons.jpg')
            .extract({ left: 0, top: 85, width: 120, height: 95 })
            .trim()
        
        const buffer = await img.toBuffer();
        const meta = await sharp(buffer).metadata();
        console.log('Trimmed size:', meta.width, 'x', meta.height);
        
        await sharp(buffer)
            .resize(256, 256, { fit: 'contain', background: {r:255,g:255,b:255,alpha:0} })
            .composite([{
                input: Buffer.from('<svg><circle cx="128" cy="128" r="126" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png()
            .toFile('test-egg2.png');
            
    } catch(e) {
        console.error(e);
    }
}
run();
