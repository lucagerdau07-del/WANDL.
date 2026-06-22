const sharp = require('sharp');
async function run() {
    await sharp('assets/images/allergen-icons.jpg')
        .extract({ left: 5, top: 90, width: 110, height: 110 }) // generous box avoiding text
        .trim({ threshold: 40 })
        .toFile('test-trim-auto.png');
}
run();
