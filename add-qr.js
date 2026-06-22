const fs = require('fs');

const files = [
    'index.html',
    'shop.html',
    'checkout.html',
    'success.html',
    'abos.html',
    'impressum.html',
    'product-original.html',
    'product-dark.html',
    'product-spice.html',
    'product-classic.html'
];

const qrCodeDiv = `
                <div class="qr">
                    <h4>Website</h4>
                    <img src="assets/images/qr-code.png" alt="QR Code" style="width: 120px; height: 120px; border-radius: 8px; opacity: 0.9; margin-top: 0.5rem; filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.3));">
                </div>
            </div>`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Only add if not already present
    if (!content.includes('assets/images/qr-code.png')) {
        content = content.replace('</ul>\n                  </div>\n              </div>', '</ul>\n                  </div>\n' + qrCodeDiv);
        content = content.replace('</ul>\r\n                  </div>\r\n              </div>', '</ul>\r\n                  </div>\r\n' + qrCodeDiv);
        content = content.replace('</ul>\n                  </div>\n              </div>\n              <div class="bottom-bar">', '</ul>\n                  </div>\n' + qrCodeDiv + '\n              <div class="bottom-bar">');
        
        // Let's use a regex to be more robust
        content = content.replace(/<\/ul>\s*<\/div>\s*<\/div>\s*<div class="bottom-bar">/, '</ul>\n                  </div>\n' + qrCodeDiv + '\n              <div class="bottom-bar">');
        
        fs.writeFileSync(file, content, 'utf8');
    }
});

console.log('Added QR code to footers.');
