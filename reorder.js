const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('index.html', 'utf8');
const $ = cheerio.load(html, { decodeEntities: false });

const order = [
    '#hero',
    '#sv-section',
    '#transformation',
    '#usp',
    '#allergen-free',
    '#production',
    '#shelf-life',
    '#packaging', // Müllreduktion
    '#target-audience', // Unsere Zielgruppen
    '#sustainability',
    '#competition',
    'section:not([id])', // Vertrieb und Marketing
    '#finance',
    '#legal',
    '#vision',
    '#partners',
    '#faq'
];

const main = $('main');
const sections = [];

order.forEach(sel => {
    const el = $(sel);
    if (el.length > 0) {
        sections.push(el.clone());
        el.remove();
    }
});

// Any remaining sections?
$('main > section').each((i, el) => {
    sections.push($(el).clone());
    $(el).remove();
});

sections.forEach(sec => {
    main.append(sec);
});

// Fix newlines between sections for readability
let output = $.html();
output = output.replace(/<\/section><section/g, '<\/section>\n\n    <section');
fs.writeFileSync('index.html', output);
console.log('Done!');
