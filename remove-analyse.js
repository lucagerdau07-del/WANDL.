const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /<p[^>]*>Qualitative Analyse der Zielgruppen und Bedarfstreiber<\/p>\s*/;

if (regex.test(html)) {
    html = html.replace(regex, '');
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Removed target paragraph.');
} else {
    // try line by line match just in case
    const lines = html.split('\n');
    const newLines = lines.filter(line => !line.includes('Qualitative Analyse der Zielgruppen und Bedarfstreiber'));
    if (lines.length !== newLines.length) {
        fs.writeFileSync('index.html', newLines.join('\n'), 'utf8');
        console.log('Removed target line.');
    } else {
        console.log('Text not found.');
    }
}
