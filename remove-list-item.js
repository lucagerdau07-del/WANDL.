const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The exact html uses unicode encoded \u00E4 etc since we put it there in the last step
// Let's just use a regex to match the <li> containing "Keine notarielle Beurkundung"
const regex = /<li style="color: var\(--color-earth-100\);">Keine notarielle Beurkundung[\s\S]*?<\/li>/;

if (regex.test(html)) {
    html = html.replace(regex, '');
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Successfully removed the list item.');
} else {
    console.log('List item not found.');
}
