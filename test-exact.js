const sharp = require('sharp');

async function run() {
    try {
        await sharp('assets/images/allergen-icons.jpg')
            .extract({ left: 15, top: 104, width: 90, height: 90 })
            .resize(256, 256, { kernel: 'lanczos3' })
            .composite([{
                input: Buffer.from('<svg><circle cx="128" cy="128" r="126" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png()
            .toFile('test-egg-exact.png');
    } catch(e) {
        console.error(e);
    }
}
run();
