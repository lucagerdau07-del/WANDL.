const sharp = require('sharp');
async function run() {
    await sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 12, top: 100, width: 88, height: 88 }) 
        .resize(256, 256, { kernel: 'lanczos3' })
        .composite([{
            input: Buffer.from('<svg><circle cx="128" cy="128" r="128" fill="black"/></svg>'),
            blend: 'dest-in'
        }])
        .png()
        .toFile('test-egg-perfect.png');
}
run();
