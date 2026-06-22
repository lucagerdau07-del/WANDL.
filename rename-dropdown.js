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
    
    // For index.html
    content = content.replace('<a href="#sv-section">Idee &amp; Funktion</a>', '<a href="#sv-section">Start</a>');
    content = content.replace('<a href="#sv-section">Idee & Funktion</a>', '<a href="#sv-section">Start</a>'); // fallback
    
    // For other files
    content = content.replace('<a href="index.html#sv-section">Idee &amp; Funktion</a>', '<a href="index.html#sv-section">Start</a>');
    content = content.replace('<a href="index.html#sv-section">Idee & Funktion</a>', '<a href="index.html#sv-section">Start</a>'); // fallback
    
    fs.writeFileSync(file, content);
});

console.log('Fixed dropdown items in all HTML files.');
