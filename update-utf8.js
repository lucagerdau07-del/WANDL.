const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const targetText = 'Unsere Barriere-Verpackung sch\u00FCtzt den Riegel perfekt und kommt komplett ohne Plastik aus. Auch wenn sie biologisch abbaubar ist: Nimm deinen M\u00FCll bitte wieder mit nach Hause, um die Natur sauber zu halten. Sie l\u00E4sst sich r\u00FCckstandslos kompostieren.';

// Replace anything starting with "Unsere Barriere-Verpackung" up to the end of the <p> tag
html = html.replace(/Unsere Barriere-Verpackung.*?<\/p>/, `${targetText}</p>`);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Fixed with unicode escapes!');
