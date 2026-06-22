const https = require('https');
const fs = require('fs');

const images = [
    { url: 'https://images.unsplash.com/photo-1551632811-561732d1e306?q=80&w=800', filename: 'assets/images/target-audience/outdoor.jpg' },
    { url: 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=800', filename: 'assets/images/target-audience/performers.jpg' },
    { url: 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?q=80&w=800', filename: 'assets/images/target-audience/sportler.jpg' },
    { url: 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=800', filename: 'assets/images/target-audience/allergiker.jpg' },
    { url: 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800', filename: 'assets/images/target-audience/veganer.jpg' }
];

function download(url, dest) {
    return new Promise((resolve, reject) => {
        const file = fs.createWriteStream(dest);
        https.get(url, response => {
            if (response.statusCode !== 200) {
                reject(new Error(`Failed to download ${url}: ${response.statusCode}`));
                return;
            }
            response.pipe(file);
            file.on('finish', () => {
                file.close();
                resolve();
            });
        }).on('error', err => {
            fs.unlink(dest, () => {});
            reject(err);
        });
    });
}

async function run() {
    try {
        for (const img of images) {
            console.log(`Downloading ${img.filename}...`);
            await download(img.url, img.filename);
        }
        console.log('All downloads finished.');
        
        // Update index.html
        let html = fs.readFileSync('index.html', 'utf8');
        for (const img of images) {
            html = html.replace(img.url.replace(/&/g, '&amp;'), img.filename);
        }
        fs.writeFileSync('index.html', html, 'utf8');
        console.log('index.html updated.');
    } catch (err) {
        console.error('Error:', err);
    }
}

run();
