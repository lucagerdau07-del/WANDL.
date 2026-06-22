const sharp = require('sharp');

const size = 84;
const offsetX = 18;
const offsetY = 100;
const colW = 120;
const rowH = 126;

const icons = [
    { name: 'zucker', col: 0, row: 3 },
    { name: 'mais', col: 2, row: 0 },
    { name: 'gmo', col: 2, row: 2 }
];

async function run() {
    for (let icon of icons) {
        let left = Math.round(icon.col * colW + offsetX);
        let top = Math.round(icon.row * rowH + offsetY);
        
        await sharp('assets/images/allergen-icons.jpg')
            .extract({ left: left, top: top, width: size, height: size })
            .composite([{
                input: Buffer.from('<svg><circle cx="42" cy="42" r="42" fill="black"/></svg>'),
                blend: 'dest-in'
            }])
            .png()
            .toFile('assets/images/allergen-' + icon.name + '.png');
    }
}
run();
