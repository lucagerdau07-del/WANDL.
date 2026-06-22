const fs = require('fs');

// 1. Update checkout.html
let checkout = fs.readFileSync('checkout.html', 'utf8');
const oldShippingLogic =                 // Versandkosten (frei ab 50 Euro)
                let shipping = 0;
                if (total > 0 && total < 50) {
                    shipping = 4.90;
                };
const newShippingLogic =                 // Versandkosten (frei ab 50 Euro oder bei Starter Box)
                const hasStarterBox = cart.some(item => item.name === 'Starter Box');
                let shipping = 0;
                if (total > 0 && total < 50 && !hasStarterBox) {
                    shipping = 4.90;
                };
checkout = checkout.replace(oldShippingLogic, newShippingLogic);
fs.writeFileSync('checkout.html', checkout);

// 2. Update abos.html
let abos = fs.readFileSync('abos.html', 'utf8');
const oldFeatures =                         <ul class="price-features">
                            <li>6 Riegel (2x Original, 2x Dark, 2x Spice)</li>
                            <li>Einmalige Lieferung</li>
                            <li>Perfekt zum Testen</li>
                            <li>Alle 3 Sorten enthalten</li>
                        </ul>;
const newFeatures =                         <ul class="price-features">
                            <li>6 Riegel (2x Original, 2x Dark, 2x Spice)</li>
                            <li>Einmalige Lieferung</li>
                            <li>Perfekt zum Testen</li>
                            <li><strong>Kostenloser Versand</strong></li>
                        </ul>;
abos = abos.replace(oldFeatures, newFeatures);
fs.writeFileSync('abos.html', abos);

console.log('Fixed shipping logic');
