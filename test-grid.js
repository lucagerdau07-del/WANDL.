const sharp = require('sharp');
async function run() {
    await sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 0, top: 85, width: 120, height: 125 })
        .toFile('test-grid.jpg');
}
run();
