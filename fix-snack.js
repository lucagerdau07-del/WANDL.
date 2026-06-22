const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The text is "Zubereitung mit hei\u00DFem oder kaltem Wasser \u2013 oder direkt als Snack."
// Let's use a regex that handles any type of dash or hyphen just in case.
const regex = /Zubereitung mit hei\u00DFem oder kaltem Wasser\s*[\u2013-]?\s*oder direkt als Snack\./g;

const newText = "Zubereitung mit hei\u00DFem oder kaltem Wasser oder direkt als Snack.";

if (regex.test(html)) {
    html = html.replace(regex, newText);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Fixed Snack wording.');
} else {
    console.log('Text not found.');
}
