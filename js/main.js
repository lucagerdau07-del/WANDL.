/**
 * ============================================================
 *  WANDL. — Main Application Logic
 * ============================================================
 *  Handles:
 *    1. Scroll-reveal animations with staggered delays
 *    2. Animated counters (integers & decimals)
 *    3. FAQ accordion (single-open mode)
 *    4. Recipe ingredient reveal
 *    5. Horizontal drag-to-scroll for target groups
 *    6. Financing chart animations (pie + bar)
 *    7. Partner logo carousel (infinite scroll)
 *    8. Lazy loading for images
 *    9. Smooth section background transitions
 * ============================================================
 */

(() => {
  'use strict';

  /* ===========================================================
   *  1. Scroll-Reveal Animation
   * ========================================================= */

  const REVEAL_SELECTORS = [
    '.step',
    '.usp-item',
    '.price-card',
    '.product-card',
    '.sus-card',
    '.timeline-item',
    '.target-card',
    '.badge',
    '.allergen-icon',
    '.chart-box',
    'h2',
    '.idea-grid',
    '.split-layout',
  ];

  /** Gather every element that should animate on scroll */
  const revealElements = document.querySelectorAll(REVEAL_SELECTORS.join(', '));

  /**
   * Apply staggered --delay custom property to children of grid/flex containers.
   * This lets CSS use  transition-delay: var(--delay, 0s)  for a cascade effect.
   */
  const applyStaggerDelays = (parent) => {
    const children = parent.children;
    [...children].forEach((child, index) => {
      child.style.setProperty('--delay', `${index * 0.1}s`);
    });
  };

  // Tag every element and prepare grids
  revealElements.forEach((el) => {
    el.classList.add('reveal');

    // If the element is a grid / flex parent, stagger its children
    const computed = getComputedStyle(el);
    if (
      computed.display === 'grid' ||
      computed.display === 'flex' ||
      el.classList.contains('idea-grid')
    ) {
      applyStaggerDelays(el);
    }
  });

  // Apply stagger delays specifically to grid containers whose children are revealed
  document.querySelectorAll('.allergen-grid').forEach(applyStaggerDelays);

  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target); // animate only once
        }
      });
    },
    {
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px',
    }
  );

  revealElements.forEach((el) => revealObserver.observe(el));

  /* ===========================================================
   *  2. Counter Animation
   * ========================================================= */

  const counters = document.querySelectorAll('.counter');

  /**
   * Ease-out quadratic: decelerates towards the end.
   * @param {number} t – progress 0 → 1
   * @returns {number}
   */
  const easeOutQuad = (t) => t * (2 - t);

  /**
   * Animate a single counter element from 0 → target over duration ms.
   * @param {HTMLElement} el
   */
  const animateCounter = (el) => {
    const target   = parseFloat(el.dataset.target) || 0;
    const decimals = parseInt(el.dataset.decimals, 10) || 0;
    const duration = 2000; // ms
    const start    = performance.now();

    const tick = (now) => {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased    = easeOutQuad(progress);
      const current  = eased * target;

      el.textContent = current.toFixed(decimals);

      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        // Ensure the final value is exact
        el.textContent = target.toFixed(decimals);
      }
    };

    requestAnimationFrame(tick);
  };

  if (counters.length) {
    const counterObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    counters.forEach((c) => counterObserver.observe(c));
  }

  /* ===========================================================
   *  3. FAQ Accordion (single-open mode)
   * ========================================================= */

  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach((header) => {
    header.addEventListener('click', () => {
      const parentItem  = header.closest('.accordion-item');
      const isActive    = parentItem?.classList.contains('active');

      // Close all siblings first (single-open)
      const container = parentItem?.parentElement;
      if (container) {
        container.querySelectorAll('.accordion-item.active').forEach((item) => {
          item.classList.remove('active');
          // Collapse content
          const body = item.querySelector('.accordion-body, .accordion-content');
          if (body) body.style.maxHeight = null;
        });
      }

      // Toggle the clicked item (open if it wasn't already active)
      if (!isActive && parentItem) {
        parentItem.classList.add('active');
        const body = parentItem.querySelector('.accordion-body, .accordion-content');
        if (body) body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });

  /* ===========================================================
   *  4. Recipe Ingredients Reveal
   * ========================================================= */

  const recipeSection       = document.getElementById('recipe');
  const ingredientsShowcase = document.querySelector('.ingredients-showcase');

  if (recipeSection && ingredientsShowcase) {
    // Pre-assign staggered delays to each ingredient
    const ingredients = ingredientsShowcase.querySelectorAll(
      '.ingredient, .ingredient-item, [class*="ingredient"]'
    );
    ingredients.forEach((el, i) => {
      el.style.setProperty('--delay', `${i * 0.12}s`);
    });

    const recipeObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            ingredientsShowcase.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.2 }
    );

    recipeObserver.observe(recipeSection);
  }

  /* ===========================================================
   *  5. Horizontal Drag-to-Scroll for Target Groups
   * ========================================================= */

  const horizontalContainers = document.querySelectorAll('.horizontal-scroll-container');

  horizontalContainers.forEach((container) => {
    let isDown    = false;
    let startX    = 0;
    let scrollLeft = 0;

    // Add a grab cursor
    container.style.cursor = 'grab';

    container.addEventListener('mousedown', (e) => {
      isDown     = true;
      startX     = e.pageX - container.offsetLeft;
      scrollLeft = container.scrollLeft;
      container.style.cursor     = 'grabbing';
      container.style.userSelect = 'none';
    });

    container.addEventListener('mouseleave', () => {
      isDown = false;
      container.style.cursor = 'grab';
    });

    container.addEventListener('mouseup', () => {
      isDown = false;
      container.style.cursor = 'grab';
    });

    container.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x    = e.pageX - container.offsetLeft;
      const walk = (x - startX) * 1.5; // scroll speed multiplier
      container.scrollLeft = scrollLeft - walk;
    });

    // ── Scroll indicator dots ──
    const createScrollIndicator = () => {
      const track       = container.querySelector('.scroll-track, .card-track') || container;
      const totalWidth  = track.scrollWidth;
      const visibleWidth = container.clientWidth;
      if (totalWidth <= visibleWidth) return; // no overflow

      const dotCount = Math.ceil(totalWidth / visibleWidth);
      const indicator = document.createElement('div');
      indicator.className = 'scroll-dots';
      indicator.setAttribute('aria-hidden', 'true');

      for (let i = 0; i < dotCount; i++) {
        const dot = document.createElement('span');
        dot.className = 'scroll-dot';
        if (i === 0) dot.classList.add('active');
        indicator.appendChild(dot);
      }

      container.parentElement?.appendChild(indicator);

      // Update active dot on scroll
      container.addEventListener('scroll', () => {
        const progress   = container.scrollLeft / (totalWidth - visibleWidth);
        const activeIdx  = Math.round(progress * (dotCount - 1));
        indicator.querySelectorAll('.scroll-dot').forEach((d, idx) => {
          d.classList.toggle('active', idx === activeIdx);
        });
      }, { passive: true });
    };

    // Build dots after a short delay so layout is settled
    requestAnimationFrame(createScrollIndicator);
  });

  /* ===========================================================
   *  6. Financing Charts Animation
   * ========================================================= */

  // ── 6a. Pie Chart (conic-gradient via CSS custom properties) ──
  const pieChart = document.querySelector('.pie-chart, [data-chart="pie"]');

  if (pieChart) {
    const segments = pieChart.querySelectorAll('[data-value]');
    const animatePie = () => {
      let cumulative = 0;
      segments.forEach((seg) => {
        const value = parseFloat(seg.dataset.value) || 0;
        seg.style.setProperty('--seg-start', `${cumulative}%`);
        seg.style.setProperty('--seg-end', `${cumulative + value}%`);
        cumulative += value;
      });

      // If the pie is built with a single conic-gradient on the parent:
      pieChart.style.setProperty('--pie-progress', '100%');
      pieChart.classList.add('animated');
    };

    const pieObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animatePie();
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.3 }
    );

    pieObserver.observe(pieChart);
  }

  // ── 6b. Bar Chart ──
  const barCharts = document.querySelectorAll('.bar-chart, [data-chart="bar"]');

  barCharts.forEach((chart) => {
    const bars = chart.querySelectorAll('.bar, [data-bar-value]');

    const animateBars = () => {
      bars.forEach((bar, index) => {
        const target = parseFloat(bar.dataset.barValue || bar.dataset.value) || 0;
        // Staggered entrance
        setTimeout(() => {
          bar.style.height = `${target}%`;
          bar.style.setProperty('--bar-height', `${target}%`);
          bar.classList.add('animated');
        }, index * 150);
      });
    };

    const barObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateBars();
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.3 }
    );

    barObserver.observe(chart);
  });

  /* ===========================================================
   *  7. Partner Logo Carousel — Infinite Scroll
   * ========================================================= */

  const logoTracks = document.querySelectorAll('.logo-track');

  logoTracks.forEach((track) => {
    // Duplicate children for seamless looping
    const clone = track.innerHTML;
    track.innerHTML += clone; // double the content

    // Pause animation on hover
    const carousel = track.closest('.logo-carousel, .partner-logos');
    if (carousel) {
      carousel.addEventListener('mouseenter', () => {
        track.style.animationPlayState = 'paused';
      });
      carousel.addEventListener('mouseleave', () => {
        track.style.animationPlayState = 'running';
      });
    }
  });

  /* ===========================================================
   *  8. Lazy Loading for Images
   * ========================================================= */

  /**
   * Add native lazy loading to all images that don't already have it,
   * then set up a fallback IntersectionObserver for browsers / cases
   * where we want more control (e.g. blurred placeholder swap).
   */
  const lazyImages = document.querySelectorAll('img:not([loading])');

  lazyImages.forEach((img) => {
    img.setAttribute('loading', 'lazy');
  });

  // Custom observer for data-src pattern (if used)
  const dataSrcImages = document.querySelectorAll('img[data-src]');

  if (dataSrcImages.length) {
    const lazyObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const img = entry.target;
            if (img.dataset.src) {
              img.src = img.dataset.src;
              img.removeAttribute('data-src');
            }
            if (img.dataset.srcset) {
              img.srcset = img.dataset.srcset;
              img.removeAttribute('data-srcset');
            }
            img.classList.add('loaded');
            observer.unobserve(img);
          }
        });
      },
      { rootMargin: '200px 0px' } // start loading 200 px before visible
    );

    dataSrcImages.forEach((img) => lazyObserver.observe(img));
  }

  /* ===========================================================
   *  9. Smooth Section Background Transitions
   * ========================================================= */

  /**
   * As the user scrolls, we read each section's data-bg attribute
   * (if present) and smoothly transition document / body background
   * to match the section currently dominant in the viewport.
   */
  const bgSections = document.querySelectorAll('section[data-bg]');

  if (bgSections.length) {
    const bgObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const color = entry.target.dataset.bg;
            if (color) {
              document.body.style.transition = 'background-color 0.6s ease';
              document.body.style.backgroundColor = color;
            }
          }
        });
      },
      {
        rootMargin: '-40% 0px -40% 0px',
        threshold: 0,
      }
    );

    bgSections.forEach((s) => bgObserver.observe(s));
  }

  /* ===========================================================
   *  Initialisation Log
   * ========================================================= */
  console.log('%c[WANDL.] Main app initialised ✓', 'color:#8BC34A; font-weight:bold;');
})();

// Animierte Zielgruppen Balken
document.addEventListener("DOMContentLoaded", () => {
    const targetAnimContainer = document.getElementById("target-anim-container");
    if(targetAnimContainer) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    const bars = targetAnimContainer.querySelectorAll(".anim-target");
                    bars.forEach((bar, i) => {
                        setTimeout(() => {
                            bar.classList.add("animate-in");
                        }, i * 150);
                    });
                    observer.unobserve(targetAnimContainer);
                }
            });
        }, { threshold: 0.2 });
        observer.observe(targetAnimContainer);
    }
});
