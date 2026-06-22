const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Note the quotes around Desk-Lunch in the html: "Desk-Lunch" or something else? Let's use regex.
const regex = /Zubereitung als bequemer ["\u201C\u201E]Desk-Lunch["\u201D\u201C] ohne langes Sp\u00FClen\./g;
const newText = "Zubereitung als bequemes und schnelles Essen ohne langes Sp\u00FClen.";

if (regex.test(html)) {
    html = html.replace(regex, newText);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Fixed Desk-Lunch wording.');
} else {
    // try exact string if there are no smart quotes
    const fallbackRegex = /Zubereitung als bequemer Desk-Lunch ohne langes Sp\u00FClen\./g;
    if (fallbackRegex.test(html)) {
        html = html.replace(fallbackRegex, newText);
        fs.writeFileSync('index.html', html, 'utf8');
        console.log('Fixed Desk-Lunch wording (fallback).');
    } else {
        // try finding without quotes
        const finalRegex = /Zubereitung als bequemer.*?Desk-Lunch.*?ohne langes Sp\u00FClen\./g;
        if (finalRegex.test(html)) {
            html = html.replace(finalRegex, newText);
            fs.writeFileSync('index.html', html, 'utf8');
            console.log('Fixed Desk-Lunch wording (final fallback).');
        } else {
            console.log('Text not found.');
        }
    }
}
