const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const anchor = 'arbeiten wir profitabel.</p>\n                          </div>';

const newContent = `
                          <div class="faq-accordion" style="margin-top: 2rem;">
                              <div class="accordion-item">
                                  <button type="button" class="accordion-header" style="font-size: 1rem; padding: 1rem 0;">
                                      Zusammensetzung: Startkapital (1.886,00 \u20AC)
                                      <span class="accordion-icon">+</span>
                                  </button>
                                  <div class="accordion-content">
                                      <ul style="margin: 0; padding-left: 1.5rem; padding-bottom: 1rem; list-style-type: disc;">
                                          <li>Produkthaftpflichtversicherung (1. Jahr): 600,00 \u20AC</li>
                                          <li>Erstbestellung Rohstoffe & Verpackung (f\u00FCr 500 Riegel): 615,00 \u20AC</li>
                                          <li>V-Label Lizenz & Rezeptrechner PRO (1. Jahr): 270,00 \u20AC</li>
                                          <li>Mietk\u00FCche Testtag & Branding/Layout: 210,00 \u20AC</li>
                                          <li>Hygiene-Schulung & Gewerbe-GbR-Anmeldung: 104,00 \u20AC</li>
                                          <li>Puffer f\u00FCr Unvorhergesehenes: 87,00 \u20AC</li>
                                      </ul>
                                  </div>
                              </div>
                              <div class="accordion-item">
                                  <button type="button" class="accordion-header" style="font-size: 1rem; padding: 1rem 0;">
                                      Zusammensetzung: St\u00FCckkosten pro Riegel (1,77 \u20AC)
                                      <span class="accordion-icon">+</span>
                                  </button>
                                  <div class="accordion-content">
                                      <ul style="margin: 0; padding-left: 1.5rem; padding-bottom: 1rem; list-style-type: disc;">
                                          <li>Rohstoffe: 0,85 \u20AC</li>
                                          <li>K\u00FCchenmiete anteilig: 0,33 \u20AC</li>
                                          <li>Standbeutel: 0,28 \u20AC</li>
                                          <li>Etikett: 0,18 \u20AC</li>
                                          <li>Versandkarton-Anteil: 0,08 \u20AC</li>
                                          <li>Sauerstoff-Absorber: 0,05 \u20AC</li>
                                      </ul>
                                  </div>
                              </div>
                              <div class="accordion-item">
                                  <button type="button" class="accordion-header" style="font-size: 1rem; padding: 1rem 0;">
                                      Zusammensetzung: Fixkosten pro Monat (114,50 \u20AC)
                                      <span class="accordion-icon">+</span>
                                  </button>
                                  <div class="accordion-content">
                                      <ul style="margin: 0; padding-left: 1.5rem; padding-bottom: 1rem; list-style-type: disc;">
                                          <li>Produkthaftpflicht: 50,00 \u20AC</li>
                                          <li>Shopify & Apps: 29,00 \u20AC</li>
                                          <li>Sonstiges / Domain: 13,00 \u20AC</li>
                                          <li>Rezeptrechner PRO anteilig: 12,50 \u20AC</li>
                                          <li>V-Label anteilig: 10,00 \u20AC</li>
                                      </ul>
                                  </div>
                              </div>
                          </div>`;

if (html.includes(anchor)) {
    html = html.replace(anchor, anchor + newContent);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Successfully inserted finance accordion.');
} else {
    console.log('Anchor not found. Try regex.');
    const regex = /arbeiten wir profitabel\.<\/p>\s*<\/div>/;
    if (regex.test(html)) {
        html = html.replace(regex, match => match + newContent);
        fs.writeFileSync('index.html', html, 'utf8');
        console.log('Successfully inserted finance accordion via regex.');
    } else {
        console.log('Regex anchor also failed.');
    }
}
