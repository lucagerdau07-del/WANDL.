const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const regex = /<div class="accordion-item">\s*<button type="button" class="accordion-header">\s*Ist die Verpackung umweltfreundlich\?[\s\S]*?<\/div>\s*<\/div>/;

const newFaq = `                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Schmeckt das Porridge auch, wenn man es nur mit kaltem Wasser aufgie\u00Dft?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Ja! Dank der Vorr\u00F6stung der Haferflocken schmeckt es auch kalt hervorragend. Es ist die perfekte Erfrischung an hei\u00DFen Tagen oder wenn gerade kein Kocher zur Hand ist.</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Wie s\u00FC\u00DF ist der Riegel? Wird S\u00FC\u00DFstoff verwendet?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>WANDL. setzt komplett auf Naturprodukte. Wir verwenden keine k\u00FCnstlichen S\u00FC\u00DFstoffe. Die dezente und nat\u00FCrliche S\u00FC\u00DFe kommt rein aus den pflanzlichen Zutaten (wie z.B. Trockenfr\u00FCchten oder nat\u00FCrlichem Getreide).</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Schmilzt die Verpackung nicht, wenn ich kochendes Wasser hineingie\u00DFe?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Nein, die bio-basierte Barriere-Verpackung ist speziell daf\u00FCr entwickelt, hohen Temperaturen standzuhalten. Du kannst das hei\u00DFe Wasser v\u00F6llig bedenkenlos direkt hineinf\u00FCllen.</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Wie viel Wasser muss ich genau dazugeben, wenn ich kein Messger\u00E4t habe?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Gie\u00DFe einfach so viel Wasser in die Verpackung oder die Schale, bis die zerbr\u00F6selten St\u00FCckchen gerade so vollst\u00E4ndig bedeckt sind. Nach 90 Sekunden R\u00FChren hat es die perfekte, cremige Konsistenz.</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Woher kommt das Protein im Riegel, wenn kein Whey verwendet wird?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Wir nutzen hochwertiges, rein pflanzliches Erbsenprotein. Das liefert die vollen 20 % Proteindichte, ist extrem leicht bek\u00F6mmlich und schont im Vergleich zu tierischem Eiwei\u00DF extrem die Umwelt.</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Ist der Riegel auch f\u00FCr Menschen mit einer Histaminintoleranz geeignet?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Da wir konsequent auf die 14 EU-Hauptallergenen (inklusive N\u00FCssen und Soja) verzichten und auf minimalistische, Naturzutaten setzen, ist das Risiko sehr gering. Bei hochgradigen Unvertr\u00E4glichkeiten empfehlen wir trotzdem einen kurzen Blick auf die Zutatenliste.</p>
                        </div>
                    </div>
                    <div class="accordion-item">
                        <button type="button" class="accordion-header">
                            Warum setzt ihr auf ein Abo-Modell?
                            <span class="accordion-icon">+</span>
                        </button>
                        <div class="accordion-content">
                            <p>Das Abo-Modell hilft uns, \u00DCberproduktion komplett zu vermeiden. Wir wissen genau, wie viele Riegel wir im n\u00E4chsten Monat produzieren m\u00FCssen, sparen dadurch Ressourcen und k\u00F6nnen die Frische der Riegel garantieren.</p>
                        </div>
                    </div>`;

if (regex.test(html)) {
    html = html.replace(regex, newFaq);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Successfully updated FAQ.');
} else {
    console.log('Target FAQ not found!');
}
