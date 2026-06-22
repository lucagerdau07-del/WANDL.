document.addEventListener("DOMContentLoaded", () => {
    if (!window.gsap || !window.ScrollTrigger) {
        console.warn("GSAP / ScrollTrigger not loaded.");
        return;
    }

    gsap.registerPlugin(ScrollTrigger);

    const canvas = document.getElementById("sv-canvas");
    if (!canvas) return;
    const context = canvas.getContext("2d");

    const frameCount = 239;
    const currentFrame = index => `assets/frames/frame_${(index + 1).toString().padStart(3, '0')}.webp`;
    
    const images = [];
    const animation = { frame: 0 };
    let loaded = 0;

    // Use native image resolution for the canvas — no DPR scaling needed
    // The canvas element fills the viewport via CSS, and we draw at native image size
    // to avoid any quality loss from upscaling/downscaling
    function render() {
        const idx = Math.round(animation.frame);
        const img = images[idx];
        if (!img || !img.complete || !img.naturalWidth) return;
        
        // Set canvas to the native image dimensions (only changes on first frame or resolution change)
        if (canvas.width !== img.naturalWidth || canvas.height !== img.naturalHeight) {
            canvas.width = img.naturalWidth;
            canvas.height = img.naturalHeight;
        }
        
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.drawImage(img, 0, 0);
    }

    // Load first frame immediately
    const firstImg = new Image();
    firstImg.src = currentFrame(0);
    firstImg.onload = () => {
        canvas.width = firstImg.naturalWidth;
        canvas.height = firstImg.naturalHeight;
        context.drawImage(firstImg, 0, 0);
    };

    // Preload all frames
    for (let i = 0; i < frameCount; i++) {
        const img = new Image();
        img.src = currentFrame(i);
        images.push(img);
        img.onload = () => {
            loaded++;
        };
    }

    // ScrollTrigger to scrub through frames
    gsap.to(animation, {
        frame: frameCount - 1,
        snap: "frame",
        ease: "none",
        scrollTrigger: {
            trigger: ".sv-section",
            start: "top top",
            end: "85% bottom",
            scrub: 0.5
        },
        onUpdate: render
    });

    // Text Overlays Animations
    const tl = gsap.timeline({
        scrollTrigger: {
            trigger: ".sv-section",
            start: "top top",
            end: "85% bottom",
            scrub: 1
        }
    });

    tl.to(".sv-text-1", { opacity: 0, y: -50, duration: 1 }, 1)
      .fromTo(".sv-text-2", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 1.5)
      .to(".sv-text-2", { opacity: 0, y: -50, duration: 1, pointerEvents: "none" }, 4)
      .fromTo(".sv-text-3", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 1, pointerEvents: "auto" }, 4.5);
});
