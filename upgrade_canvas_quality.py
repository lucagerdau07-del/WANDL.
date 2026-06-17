import re

js_path = r'C:\Antigravity\2 in 1 Energieriegel Unternehmen\wandl-website\js\scroll-video.js'

js_content = '''
document.addEventListener("DOMContentLoaded", () => {
    if (!window.gsap || !window.ScrollTrigger) {
        console.warn("GSAP / ScrollTrigger not loaded.");
        return;
    }

    gsap.registerPlugin(ScrollTrigger);

    const canvas = document.getElementById("sv-canvas");
    if (!canvas) return;
    const context = canvas.getContext("2d");

    const frameCount = 300;
    const currentFrame = index => `assets/frames/ezgif-frame-${(index + 1).toString().padStart(3, '0')}.jpg`;
    
    const images = [];
    const airpods = { frame: 0 };
    let loaded = 0;

    // Resize canvas for High-DPI / Retina displays and calculate object-fit cover
    let cw, ch;
    function resizeCanvas() {
        const dpr = window.devicePixelRatio || 1;
        cw = window.innerWidth;
        ch = window.innerHeight;
        canvas.width = cw * dpr;
        canvas.height = ch * dpr;
        // The CSS still says width: 100%, height: 100%, but we no longer need object-fit: cover 
        // since we are calculating it manually, but leaving it doesn't hurt.
        context.scale(dpr, dpr);
        context.imageSmoothingEnabled = true;
        context.imageSmoothingQuality = 'high';
        render();
    }
    window.addEventListener("resize", resizeCanvas);

    // Load first frame immediately to display something
    const firstImg = new Image();
    firstImg.src = currentFrame(0);
    firstImg.onload = () => {
        resizeCanvas();
    };

    // Preload all frames
    for (let i = 0; i < frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
        images.push(img);
        img.onload = () => {
            loaded++;
            if (loaded === frameCount) {
                console.log("All frames loaded in high quality.");
            }
        };
    }

    // ScrollTrigger to scrub through frames
    gsap.to(airpods, {
        frame: frameCount - 1,
        snap: "frame",
        ease: "none",
        scrollTrigger: {
            trigger: ".sv-section",
            start: "top top",
            end: "bottom bottom",
            scrub: 0.5 // Smooth scrubbing
        },
        onUpdate: render
    });

    function render() {
        const img = images[airpods.frame];
        if (img && img.complete && img.naturalWidth) {
            
            // Calculate object-fit: cover manually to preserve high quality
            const canvasRatio = cw / ch;
            const imgRatio = img.naturalWidth / img.naturalHeight;
            
            let drawWidth, drawHeight, startX, startY;

            if (imgRatio > canvasRatio) {
                drawHeight = ch;
                drawWidth = img.naturalWidth * (ch / img.naturalHeight);
                startX = (cw - drawWidth) / 2;
                startY = 0;
            } else {
                drawWidth = cw;
                drawHeight = img.naturalHeight * (cw / img.naturalWidth);
                startX = 0;
                startY = (ch - drawHeight) / 2;
            }

            // Restore high quality setting just in case it got reset
            context.imageSmoothingEnabled = true;
            context.imageSmoothingQuality = 'high';
            
            context.clearRect(0, 0, cw, ch);
            context.drawImage(img, startX, startY, drawWidth, drawHeight);
        }
    }

    // Text Overlays Animations
    const tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".sv-section",
            start: "top top",
            end: "bottom bottom",
            scrub: 1
        }
    });

    tl.to(".sv-text-1", { opacity: 0, y: -50, duration: 1 }, 1) // Fade out text 1
      .fromTo(".sv-text-2", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 1.5) // Fade in text 2
      .to(".sv-text-2", { opacity: 0, y: -50, duration: 1, pointerEvents: "none" }, 4) // Fade out text 2
      .fromTo(".sv-text-3", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 4.5); // Fade in text 3

});
'''

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated scroll-video.js for maximum quality")
