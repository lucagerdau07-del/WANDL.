const sharp = require('sharp');
async function run() {
    // White rectangle to cover text
    const cover = Buffer.from('<svg><rect width="120" height="40" fill="white"/></svg>');
    
    let img = sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 0, top: 85, width: 120, height: 125 })
        .composite([{ input: cover, top: 85, left: 0 }])
        
    let buf = await img.toBuffer();
    
    await sharp(buf)
        .trim({ threshold: 20 })
        .resize(256, 256, { kernel: 'lanczos3' })
        .composite([{
            input: Buffer.from('<svg><circle cx="128" cy="128" r="126" fill="black"/></svg>'),
            blend: 'dest-in'
        }])
        .png()
        .toFile('test-egg-trim.png');
}
run();
