const sharp = require('sharp');

async function run() {
    try {
        // Egg Free is at col 0, row 0. Let's crop x:0-120, y:80-180
        const img = sharp('assets/images/allergen-icons.jpg')
            .extract({ left: 5, top: 90, width: 110, height: 95 })
            .trim()
            .resize(256, 256, { kernel: 'lanczos3' })
            .composite([{
                input: Buffer.from('<svg><circle cx="128" cy="128" r="128" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png();
            
        await img.toFile('test-egg.png');
        const meta = await sharp('test-egg.png').metadata();
        console.log('Trimmed size:', meta.width, 'x', meta.height);
    } catch(e) {
        console.error(e);
    }
}
run();
