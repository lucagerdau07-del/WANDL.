const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

const startStr = '<p class="section-sub" style="color: var(--color-earth-100);">Frei von allen 14 EU-Hauptallergenen</p>';
const endStr = '</div>\n                </div>\n            </div>\n\n    <!-- Symbol Track Animation -->';

const startIndex = content.indexOf(startStr);
const endIndex = content.indexOf(endStr);

if (startIndex !== -1 && endIndex !== -1) {
    const before = content.substring(0, startIndex + startStr.length);
    const after = content.substring(endIndex);
    
    const newGrid = `
                    <div class="allergen-grid" style="display: flex; gap: 1.5rem; flex-wrap: wrap; justify-content: center; margin-top: 2rem;">
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-erdnuss.png" alt="Erdnussfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Erdnussfrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-gluten.png" alt="Glutenfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Glutenfrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-soja.png" alt="Sojafrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Sojafrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-milch.png" alt="Milchfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Milchfrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-ei.png" alt="Eifrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Eifrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-fisch.png" alt="Fischfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Fischfrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-meeresfruechte.png" alt="Krebstierfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Krebstiere</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-senf.png" alt="Senffrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Senffrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-sesam.png" alt="Sesamfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Sesamfrei</span>
                        </div>
                        <div class="allergen-icon" style="text-align: center;">
                            <img src="assets/images/allergen-lupinen.png" alt="Lupinenfrei" style="width: 55px; height: 55px; display: block; margin: 0 auto 0.5rem; border-radius: 50%;">
                            <span class="label" style="font-size: 0.85rem; font-weight: 500; color: white;">Lupinen</span>
                        </div>
                    </div>`;
                    
    fs.writeFileSync('index.html', before + '\n' + newGrid + '\n' + after, 'utf8');
    console.log('Replaced grid successfully.');
} else {
    console.log('Could not find start or end string.');
}
