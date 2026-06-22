const fs = require('fs');

const files = [
    'lieferant.html'
];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        content = content.replace(/<a href="#">Versandinformationen<\/a>/g, '<a href="lieferant.html">Versandinformationen</a>');
        fs.writeFileSync(file, content, 'utf8');
    }
});

console.log('Fixed shipping link in lieferant.html.');
