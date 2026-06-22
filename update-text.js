const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const targetText = 'Unsere Barriere-Verpackung schützt den Riegel perfekt und kommt komplett ohne Plastik aus. Auch wenn sie biologisch abbaubar ist: Nimm deinen Müll bitte wieder mit nach Hause, um die Natur sauber zu halten. Sie lässt sich rückstandslos kompostieren.';

// Find the <h3>100% biologisch abbaubar</h3> and replace the <p> immediately after it
const regex = /(<h3[^>]*>100% biologisch abbaubar<\/h3>\s*<p[^>]*>).*?(<\/p>)/s;

html = html.replace(regex, `$1${targetText}$2`);

fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated text successfully!');
