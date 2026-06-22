const fs = require('fs');

let html = fs.readFileSync('abos.html', 'utf8');
html = html.replace('<div class="save-badge">Spare 18 %</div>', '<div class="save-badge">-18%</div>');
html = html.replace('<div class="save-badge">Spare 22 %</div>', '<div class="save-badge">-22%</div>');
fs.writeFileSync('abos.html', html);

let css = fs.readFileSync('css/style.css', 'utf8');
const badgeTopRule = '.badge-top {';
const newBadgeCSS = `
.save-badge {
    position: absolute;
    top: -25px;
    right: -15px;
    color: #e53935; /* Strong red */
    font-weight: 900;
    font-size: 2.8rem;
    transform: rotate(15deg);
    z-index: 10;
    font-family: var(--font-display);
    text-shadow: 2px 2px 0px var(--color-white), -1px -1px 0px var(--color-white), 1px -1px 0px var(--color-white), -1px 1px 0px var(--color-white), 1px 1px 0px var(--color-white);
    pointer-events: none;
}

@media (max-width: 767px) {
    .save-badge {
        right: -10px;
        top: -20px;
        font-size: 2.2rem;
    }
}
`;

if (!css.includes('.save-badge {')) {
    css = css.replace(badgeTopRule, newBadgeCSS + '\n' + badgeTopRule);
    fs.writeFileSync('css/style.css', css);
}

console.log('Fixed red text');
