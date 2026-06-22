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

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace the mangled string using regex
    if (file === 'index.html') {
        content = content.replace(/<a href="#packaging">.*?<\/a>/g, '<a href="#packaging">M\u00FCllreduktion</a>');
    } else {
        content = content.replace(/<a href="index.html#packaging">.*?<\/a>/g, '<a href="index.html#packaging">M\u00FCllreduktion</a>');
    }
    
    fs.writeFileSync(file, content, 'utf8');
});

console.log('Fixed M\u00FCllreduktion in all files.');
