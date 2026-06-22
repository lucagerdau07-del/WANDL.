const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// The HTML contains: <strong>Agiler Start:</strong> Keine notarielle Beurkundung oder langwierige Formalit\u00E4ten n\u00F6tig \u2013 ideal f\u00FCr schnelle Entscheidungswege in der Gr\u00FCndungsphase.
// Replace with: Keine notarielle Beurkundung oder langwierige Formalit\u00E4ten n\u00F6tig. Das ist ideal f\u00FCr schnelle Entscheidungswege in der Gr\u00FCndungsphase.

const regex = /<strong>Agiler Start:<\/strong>\s*Keine\s*notarielle\s*Beurkundung\s*oder\s*langwierige\s*Formalit\u00E4ten\s*n\u00F6tig\s*[\u2013-]\s*ideal\s*f\u00FCr\s*schnelle\s*Entscheidungswege\s*in\s*der\s*Gr\u00FCndungsphase\./g;

const newText = "Keine notarielle Beurkundung oder langwierige Formalit\u00E4ten n\u00F6tig. Das ist ideal f\u00FCr schnelle Entscheidungswege in der Gr\u00FCndungsphase.";

if (regex.test(html)) {
    html = html.replace(regex, newText);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Fixed Agiler Start text.');
} else {
    console.log('Regex did not match!');
}
