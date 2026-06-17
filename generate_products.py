import re

with open('product.html', 'r', encoding='utf-8') as f:
    template = f.read()

products = [
    {
        'id': 'original',
        'title': 'Original',
        'desc': 'Die perfekte Balance aus nahrhaftem Bio-Hafer, cremigem Sonnenblumenkernmus und fruchtigen Waldheidelbeeren. Verfeinert mit Kürbiskernen und Meersalz.',
        'energy': '410 kcal',
        'protein': '20 g',
        'carbs': '45 g',
        'sugar': '12 g',
        'fat': '15 g',
        'fiber': '7 g'
    },
    {
        'id': 'dark',
        'title': 'Dark',
        'desc': 'Für Schokoladen-Liebhaber. Edler Bio-Kakao trifft auf die natürliche, karamellige Süße reiner Agavendicksaft. Kraftvoll, herb und langanhaltend sättigend.',
        'energy': '415 kcal',
        'protein': '20 g',
        'carbs': '44 g',
        'sugar': '13 g',
        'fat': '16 g',
        'fiber': '8 g'
    },
    {
        'id': 'spice',
        'title': 'Spice',
        'desc': 'Perfekt für kalte Tage und besonders köstlich als warmes Porridge. Saftige Apfelstücke harmonieren mit edlem Ceylon-Zimt. Schmeckt wie frischer Apfelkuchen.',
        'energy': '405 kcal',
        'protein': '20 g',
        'carbs': '47 g',
        'sugar': '14 g',
        'fat': '14 g',
        'fiber': '7 g'
    },
    {
        'id': 'classic',
        'title': 'Classic Creamy',
        'desc': 'Das ultimative Geschmackserlebnis. Molkenprotein und Vollmilchpulver für cremig-milchige Konsistenz, verfeinert mit Mandelmus und knackigen Mandelstücken.',
        'energy': '425 kcal',
        'protein': '22 g',
        'carbs': '42 g',
        'sugar': '11 g',
        'fat': '18 g',
        'fiber': '5 g'
    }
]

for p in products:
    html = template.replace('WANDL. Detailansicht', f"WANDL. {p['title']}")
    html = html.replace('WANDL.+Produkt', f"WANDL.+{p['title'].replace(' ', '+')}")
    
    # Description
    html = re.sub(r'<p class="product-description">.*?</p>', f'<p class="product-description">{p["desc"]}</p>', html, flags=re.DOTALL)
    
    # Nutrition
    html = re.sub(r'<th>Energie</th>\s*<td>.*?</td>', f'<th>Energie</th>\n                            <td>{p["energy"]}</td>', html, flags=re.DOTALL)
    html = re.sub(r'<th>Protein</th>\s*<td>.*?</td>', f'<th>Protein</th>\n                            <td>{p["protein"]}</td>', html, flags=re.DOTALL)
    html = re.sub(r'<th>Kohlenhydrate</th>\s*<td>.*?</td>', f'<th>Kohlenhydrate</th>\n                            <td>{p["carbs"]}</td>', html, flags=re.DOTALL)
    html = re.sub(r'<th>davon Zucker</th>\s*<td>.*?</td>', f'<th>davon Zucker</th>\n                            <td>{p["sugar"]}</td>', html, flags=re.DOTALL)
    html = re.sub(r'<th>Fett</th>\s*<td>.*?</td>', f'<th>Fett</th>\n                            <td>{p["fat"]}</td>', html, flags=re.DOTALL)
    html = re.sub(r'<th>Ballaststoffe</th>\s*<td>.*?</td>', f'<th>Ballaststoffe</th>\n                            <td>{p["fiber"]}</td>', html, flags=re.DOTALL)

    with open(f"product-{p['id']}.html", 'w', encoding='utf-8') as f:
        f.write(html)

print('Generated product pages.')
