const fs = require('fs');
let css = fs.readFileSync('css/style.css', 'utf8');

css += `\n/* Fix emoji vertical alignment in allergen grid */\n#allergen-free .allergen-icon .icon {\n    transform: translateY(6px);\n}\n`;

fs.writeFileSync('css/style.css', css, 'utf8');
console.log('Added CSS successfully!');
