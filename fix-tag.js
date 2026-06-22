const fs = require('fs');
let html = fs.readFileSync('impressum.html', 'utf8');
html = html.replace(
    '<div class="source-title">https://unsplash.com/de/fotos/person-die-im-begriff-ist-die-barbe-zu-heben-WvDYdXDzkhs</div>\r\n            <a href="https://unsplash.com/de/fotos/pochiertes-ei-mit-gemuse-und-tomaten-auf-blauem-teller-jUPOXXRNdcA"',
    '<div class="source-title">https://unsplash.com/de/fotos/person-die-im-begriff-ist-die-barbe-zu-heben-WvDYdXDzkhs</div>\r\n            </a>\r\n            <a href="https://unsplash.com/de/fotos/pochiertes-ei-mit-gemuse-und-tomaten-auf-blauem-teller-jUPOXXRNdcA"'
);
fs.writeFileSync('impressum.html', html, 'utf8');
