const fs = require('fs');

let indexHtml = fs.readFileSync('index.html', 'utf8');
indexHtml = indexHtml.replace('<section style="padding: 5rem 0; background-color: transparent;">', '<section id="marketing" style="padding: 5rem 0; background-color: transparent;">');
fs.writeFileSync('index.html', indexHtml);

const dropdownIndex = `
                        <a href="#sv-section">Start</a>
                        <a href="#transformation">Idee / Funktion</a>
                        <a href="#usp">Kompromisslose Nahrung</a>
                        <a href="#allergen-free">0% Allergene</a>
                        <a href="#production">Schonend Zubereitet</a>
                        <a href="#shelf-life">Haltbarkeit</a>
                        <a href="#packaging">Müllreduktion</a>
                        <a href="#target-audience">Zielgruppen</a>
                        <a href="#sustainability">Verantwortung</a>
                        <a href="#competition">Konkurrenzanalyse</a>
                        <a href="#marketing">Vertrieb & Marketing</a>
                        <a href="#finance">Finanzen</a>
                        <a href="#legal">Rechtsform</a>
                        <a href="#vision">Vision</a>
                        <a href="#partners">Partner</a>
                        <a href="#faq">FAQ</a>
`;

const dropdownOther = `
                        <a href="index.html#sv-section">Start</a>
                        <a href="index.html#transformation">Idee / Funktion</a>
                        <a href="index.html#usp">Kompromisslose Nahrung</a>
                        <a href="index.html#allergen-free">0% Allergene</a>
                        <a href="index.html#production">Schonend Zubereitet</a>
                        <a href="index.html#shelf-life">Haltbarkeit</a>
                        <a href="index.html#packaging">Müllreduktion</a>
                        <a href="index.html#target-audience">Zielgruppen</a>
                        <a href="index.html#sustainability">Verantwortung</a>
                        <a href="index.html#competition">Konkurrenzanalyse</a>
                        <a href="index.html#marketing">Vertrieb & Marketing</a>
                        <a href="index.html#finance">Finanzen</a>
                        <a href="index.html#legal">Rechtsform</a>
                        <a href="index.html#vision">Vision</a>
                        <a href="index.html#partners">Partner</a>
                        <a href="index.html#faq">FAQ</a>
`;

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
    const regex = /<div class="dropdown-content">([\s\S]*?)<\/div>/;
    
    if (file === 'index.html') {
        content = content.replace(regex, '<div class="dropdown-content">' + dropdownIndex + '                    </div>');
    } else {
        content = content.replace(regex, '<div class="dropdown-content">' + dropdownOther + '                    </div>');
    }
    
    fs.writeFileSync(file, content);
});

console.log('Dropdown updated in all HTML files.');
