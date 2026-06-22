const QRCode = require('qrcode');

QRCode.toFile('assets/images/qr-code.png', 'https://lucagerdau07-del.github.io/WANDL./', {
  color: {
    dark: '#5C7C33',  // Green dots
    light: '#00000000' // Transparent background
  },
  width: 150,
  margin: 1
}, function (err) {
  if (err) throw err;
  console.log('QR code generated.');
});
