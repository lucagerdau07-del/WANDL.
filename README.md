# WANDL. — Premium 2-in-1 Energieriegel Website

Eine interaktive, scroll-animierte Pitch-Website für **WANDL.** — den ersten veganen 2-in-1 Outdoor-Mahlzeit-Riegel.

## Quick Start

1. Öffne `index.html` in einem modernen Browser
2. Oder nutze einen lokalen Server: `npx serve .`

## Features

- 🎬 Scroll-getriebene Animationen (Riegel-Rotation, Transformation)
- 📊 Interaktive Finanz-Charts (CSS-only)
- 🎯 Tastatur-Navigation für Pitch-Präsentationen (Pfeiltasten)
- 📱 Vollständig responsive (Mobile + Smartboard 16:9)
- 🌿 Premium Outdoor-Design mit Erdfarben & Glassmorphism
- ♿ Semantisches HTML5 mit ARIA-Labels

## Struktur

```
wandl-website/
├── index.html          ← Komplette Single-Page Website
├── css/
│   └── style.css       ← Design-System + alle Styles
├── js/
│   ├── main.js         ← Scroll-Engine + Animationen
│   ├── scroll-video.js ← Frame-by-Frame Scroll-Animation
│   └── navigation.js   ← Sticky Nav + Smooth Scroll
└── assets/
    └── images/         ← Bilder (werden später ergänzt)
```

## Pitch-Modus

Für Smartboard-Präsentationen:
- **Leertaste / Pfeil Runter** → Nächste Sektion
- **Pfeil Hoch** → Vorherige Sektion
- Optimiert für 1920×1080 (16:9)

## Technologie

- Vanilla HTML5, CSS3, JavaScript (ES6+)
- Google Fonts (Outfit, Inter)
- Keine externen Abhängigkeiten
- GitHub Pages kompatibel

---

© 2026 WANDL. GbR, Hamburg
