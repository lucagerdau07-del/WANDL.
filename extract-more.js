const sharp = require('sharp');

const size = 84;
const offsetX = 18;
const offsetY = 100;
const colW = 120;
const rowH = 126;

const icons = [
    { name: 'fisch', col: 0, row: 1 },
    { name: 'senf', col: 4, row: 2 },
    { name: 'meeresfruechte', col: 1, row: 3 },
    { name: 'sesam', col: 3, row: 3 },
    { name: 'lupinen', col: 4, row: 3 }
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
