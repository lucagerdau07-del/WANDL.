const fs = require('fs');
// Simple pure JS to read dimensions from a JPEG file without extra dependencies
function getJpegSize(buffer) {
    let offset = 2; // skip FFD8
    while (offset < buffer.length) {
        if (buffer[offset] !== 0xFF) return;
        const marker = buffer[offset + 1];
        const length = buffer.readUInt16BE(offset + 2);
        if (marker === 0xC0 || marker === 0xC2) { // SOF0 or SOF2
            return {
                height: buffer.readUInt16BE(offset + 5),
                width: buffer.readUInt16BE(offset + 7)
            };
        }
        offset += length + 2;
    }
}
const buf = fs.readFileSync('assets/images/allergen-icons.jpg');
console.log(getJpegSize(buf));
