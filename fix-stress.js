const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /Vollwertige Mahlzeit trotz hektischer, urbaner Zeitpl\u00E4ne\./g;
const newText = "Vollwertige Mahlzeit trotz stressiger Zeitpl\u00E4ne.";

if (regex.test(html)) {
    html = html.replace(regex, newText);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Fixed stress wording.');
} else {
    console.log('Text not found.');
}
