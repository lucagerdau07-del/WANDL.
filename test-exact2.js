const sharp = require('sharp');
async function run() {
    await sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 17, top: 105, width: 86, height: 86 }) // top is 85 + 20 = 105
        .resize(256, 256, { kernel: 'lanczos3' })
        .composite([{
            input: Buffer.from('<svg><circle cx="128" cy="128" r="128" fill="black"/></svg>'),
            blend: 'dest-in'
        }])
        .png()
        .toFile('test-egg-final.png');
}
run();
