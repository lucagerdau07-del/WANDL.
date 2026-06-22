const sharp = require('sharp');

const size = 86;
const offsetX = 17;
const offsetY = 105;
const colW = 120;
const rowH = 125;

const icons = [
    { name: 'zucker', col: 0, row: 3 },
    { name: 'soja', col: 2, row: 1 },
    { name: 'erdnuss', col: 3, row: 2 },
    { name: 'milch', col: 1, row: 1 },
    { name: 'gluten', col: 3, row: 0 },
    { name: 'gmo', col: 2, row: 2 },
    { name: 'ei', col: 0, row: 0 },
    { name: 'mais', col: 2, row: 0 }
];

async function run() {
    for (let icon of icons) {
        let left = Math.round(icon.col * colW + offsetX);
        let top = Math.round(icon.row * rowH + offsetY);
        
        await sharp('assets/images/allergen-icons.jpg')
            .extract({ left: left, top: top, width: size, height: size })
            .resize(256, 256, { kernel: 'lanczos3' })
            .composite([{
                input: Buffer.from('<svg><circle cx="128" cy="128" r="126" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png()
            .toFile('assets/images/allergen-' + icon.name + '.png');
    }
}
run();
