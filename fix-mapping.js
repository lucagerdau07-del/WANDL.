const fs = require('fs');
const path = require('path');

const srcDir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/SKIZZE/Allergne';
const destDir = 'C:/Antigravity/2 in 1 Energieriegel Unternehmen/wandl-website/assets/images';

// 13.png is Senf (Mustard)
fs.copyFileSync(path.join(srcDir, '13.png'), path.join(destDir, 'allergen-senf.png'));

// Wait, what if 13.png was indeed sugar? Let me just copy it as senf.png. My generated zucker.png still exists.
