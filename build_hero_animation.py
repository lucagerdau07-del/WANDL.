import re
import os

# --- 1. Fix Partners ---
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_partners = r'<section id="partners"[^>]*>.*?</section>\s*<!-- ============================================================\s*FAQ'
new_partners = '''<section id="partners" style="overflow: hidden; padding: 4rem 0; background: var(--color-earth-50);">
            <div class="container center-text">
                <h2 style="margin-bottom: 2rem;">Unsere Partner</h2>
            </div>
            
            <!-- Infinite Marquee -->
            <div class="partner-marquee">
                <div class="marquee-track">
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                    <div class="marquee-item">🏕️ Globetrotter</div>
                    <div class="marquee-item">🛒 Bio-Markt</div>
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                    <div class="marquee-item">🏕️ Globetrotter</div>
                    <div class="marquee-item">🛒 Bio-Markt</div>
                    <div class="marquee-item">📦 jonatura</div>
                    <div class="marquee-item">🍳 Kitchen Town</div>
                </div>
            </div>
        </section>
        <!-- ============================================================
             FAQ'''
html = re.sub(old_partners, new_partners, html, flags=re.DOTALL)

# --- 2. Add GSAP to HTML ---
if 'gsap.min.js' not in html:
    gsap_scripts = '''<!-- GSAP & ScrollTrigger -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="js/scroll-video.js" defer></script>
</head>'''
    html = html.replace('</head>', gsap_scripts)

# --- 3. Replace Hero with Canvas ---
old_hero = r'<section id="hero".*?</section>\s*<!-- ============================================================\s*INFO BAR'
new_hero = '''<section id="sv-section" class="sv-section">
            <div class="sv-sticky">
                <canvas id="sv-canvas" class="sv-canvas"></canvas>
                <div class="sv-overlay"></div>
                
                <!-- Overlay Texts (like Standalone) -->
                <div class="sv-text sv-text-1">
                    <h1 class="hero-title" style="font-size: clamp(3rem, 8vw, 6rem);">Snack & Mahlzeit.</h1>
                    <p class="hero-subtitle">1 Riegel. 2 Funktionen.</p>
                </div>
                <div class="sv-text sv-text-2">
                    <h2>350 kcal pure Energie.</h2>
                    <p>100% kompostierbar. Rein pflanzlich.</p>
                </div>
                <div class="sv-text sv-text-3">
                    <h2>Das Outdoor-Upgrade.</h2>
                    <a href="shop.html" class="btn btn-primary" style="margin-top: 2rem;">Zum Shop</a>
                </div>
            </div>
        </section>
        <!-- ============================================================
             INFO BAR'''
if '<section id="sv-section"' not in html:
    html = re.sub(old_hero, new_hero, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# --- 4. CSS Updates ---
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.sv-section' not in css:
    sv_css = '''
/* ==========================================================================
   ScrollVideo (Hero Canvas)
   ========================================================================== */
.sv-section {
    position: relative;
    height: 400vh; /* Determines how long you have to scroll to play the animation */
    width: 100%;
    background: var(--color-black);
    margin-top: -80px; /* Offset for sticky nav */
}
.sv-sticky {
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
.sv-canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
}
.sv-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at center, transparent 40%, hsla(30,25%,5%,0.55) 100%);
    z-index: 2;
    pointer-events: none;
}
.sv-text {
    position: absolute;
    z-index: 3;
    text-align: center;
    color: var(--color-white);
    padding: 0 var(--spacing-md);
    max-width: 900px;
    will-change: transform, opacity;
    opacity: 0;
    pointer-events: none;
}
.sv-text-1 { opacity: 1; } /* Starts visible */
.sv-text.active { pointer-events: auto; }
'''
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(sv_css)

# --- 5. Create scroll-video.js ---
js_path = 'js/scroll-video.js'
sv_js = '''
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

    // Load first frame immediately to display something
    const firstImg = new Image();
    firstImg.src = currentFrame(0);
    firstImg.onload = () => {
        canvas.width = firstImg.naturalWidth || 1920;
        canvas.height = firstImg.naturalHeight || 1080;
        context.drawImage(firstImg, 0, 0);
    };

    // Preload all frames
    for (let i = 0; i < frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
        images.push(img);
        img.onload = () => {
            loaded++;
            if (loaded === frameCount) {
                console.log("All frames loaded.");
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
            // Keep canvas resolution synced to image
            if (canvas.width !== img.naturalWidth) canvas.width = img.naturalWidth;
            if (canvas.height !== img.naturalHeight) canvas.height = img.naturalHeight;
            context.clearRect(0, 0, canvas.width, canvas.height);
            context.drawImage(img, 0, 0);
        }
    }

    // Handle Window Resize for Object-Fit Cover emulation if needed
    // (object-fit: cover is applied in CSS, so canvas auto-scales visually while maintaining its internal rendering resolution)

    // Text Overlays Animations
    const tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".sv-section",
            start: "top top",
            end: "bottom bottom",
            scrub: 1
        }
    });

    // Animate texts based on timeline percentage
    // 0-30%: Text 1
    // 35-65%: Text 2
    // 70-100%: Text 3

    tl.to(".sv-text-1", { opacity: 0, y: -50, duration: 1 }, 1) // Fade out text 1
      .fromTo(".sv-text-2", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 1.5) // Fade in text 2
      .to(".sv-text-2", { opacity: 0, y: -50, duration: 1, pointerEvents: "none" }, 4) // Fade out text 2
      .fromTo(".sv-text-3", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 4.5); // Fade in text 3

});
'''
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(sv_js)

print("Hero animation implementation complete.")
