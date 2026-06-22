const sharp = require('sharp');
async function run() {
    await sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 10, top: 96, width: 90, height: 90 }) 
        .resize(256, 256, { kernel: 'lanczos3' })
        .composite([{
            input: Buffer.from('<svg><circle cx="128" cy="128" r="128" fill="black"/></svg>'),
            blend: 'dest-in'
        }])
        .png()
        .toFile('test-egg-final2.png');
}
run();
