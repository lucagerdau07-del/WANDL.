import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

clean_html = '''        <section id="production" class="fullscreen-image-section">
            <div class="overlay">
                <h2>Schonend zubereitet.</h2>
                <p>Um den Porridge Vorteil zu erhalten, wird WANDL. <strong>nicht klassisch gebacken</strong>. Die Haferflocken werden trocken vorgeröstet und die Riegel bei <strong>50-60 °C schonend gedörrt</strong>. Das entzieht Feuchtigkeit für eine feste Außenseite, gibt aber die volle Löslichkeit als Porridge.</p>
                <div class="production-details">
                    <div class="detail-item">
                        <span class="detail-icon">&#127777;</span>
                        <span>50-60 °C Dörrtemperatur</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-icon">&#128167;</span>
                        <span>aw-Wert unter 0,65 (Wasseraktivität)</span>
                    </div>
                </div>
            </div>
        </section>'''

# Regex to match the section block even with weird characters
pattern = re.compile(r'<section id="production" class="fullscreen-image-section">.*?</section>', re.DOTALL)
content = pattern.sub(clean_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
