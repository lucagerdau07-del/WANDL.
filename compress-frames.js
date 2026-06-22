const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const dir = 'assets/frames';

async function processFrames() {
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.png'));
    let savedBytes = 0;
    
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const newPath = path.join(dir, file.replace(/\.png$/, '.webp'));
        const size = fs.statSync(fullPath).size;
        
        await sharp(fullPath).webp({ quality: 85 }).toFile(newPath);
        const newSize = fs.statSync(newPath).size;
        
        savedBytes += (size - newSize);
        fs.unlinkSync(fullPath); // Delete the original PNG
        console.log(`Processed ${file} -> saved ${( (size - newSize) / 1024 / 1024 ).toFixed(2)} MB`);
    }
    
    console.log(`Total saved on frames: ${(savedBytes / 1024 / 1024).toFixed(2)} MB`);
    
    // Update JS reference
    let js = fs.readFileSync('js/scroll-video.js', 'utf8');
    js = js.replace(/\.png/g, '.webp');
    fs.writeFileSync('js/scroll-video.js', js, 'utf8');
}

processFrames().catch(console.error);
