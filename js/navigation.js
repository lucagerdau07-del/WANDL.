/**
 * ============================================================
 *  WANDL. — Navigation System
 * ============================================================
 *  Handles:
 *    1. Sticky navigation background on scroll
 *    2. Mobile hamburger menu with overlay
 *    3. Smooth-scroll anchor links (80 px header offset)
 *    4. Active-section highlighting via IntersectionObserver
 *    5. Keyboard "Pitch Mode" (Arrow / Space navigation)
 *    6. Auto-close mobile menu on link click & outside click
 * ============================================================
 */

(() => {
  'use strict';

  /* ----------------------------------------------------------
   *  DOM References
   * -------------------------------------------------------- */
  const nav         = document.getElementById('nav-main');
  const hamburger   = document.querySelector('.hamburger');
  const navLinks    = document.querySelector('.nav-links');
  const navAnchors  = navLinks ? [...navLinks.querySelectorAll('a[href^="#"]')] : [];
  const allAnchors  = [...document.querySelectorAll('a[href^="#"]')];
  const sections    = [...document.querySelectorAll('section[id]')];

  /** Pixel threshold before the nav receives a solid background */
  const SCROLL_THRESHOLD = 50;

  /** Offset (px) subtracted when smooth-scrolling to a section */
  const HEADER_OFFSET = 80;

  /* ----------------------------------------------------------
   *  1. Sticky Navigation Background
   * -------------------------------------------------------- */
  const handleStickyNav = () => {
    if (!nav) return;
    if (window.scrollY > SCROLL_THRESHOLD) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  };

  /* ----------------------------------------------------------
   *  2. Mobile Menu Toggle & Overlay
   * -------------------------------------------------------- */

  // Create the mobile overlay element once
  const overlay = document.createElement('div');
  overlay.className = 'mobile-menu-overlay';
  overlay.setAttribute('aria-hidden', 'true');
  document.body.appendChild(overlay);

  /**
   * Open / close the mobile navigation drawer.
   * @param {boolean} [forceState] – If supplied, true = open, false = close.
   */
  const toggleMobileMenu = (forceState) => {
    if (!hamburger || !navLinks) return;

    const shouldOpen = typeof forceState === 'boolean'
      ? forceState
      : !hamburger.classList.contains('active');

    hamburger.classList.toggle('active', shouldOpen);
    navLinks.classList.toggle('active', shouldOpen);
    overlay.classList.toggle('active', shouldOpen);
    overlay.setAttribute('aria-hidden', String(!shouldOpen));

    // Prevent body scroll while menu is open
    document.body.style.overflow = shouldOpen ? 'hidden' : '';

    // Update ARIA on hamburger
    hamburger.setAttribute('aria-expanded', String(shouldOpen));
  };

  const closeMobileMenu = () => toggleMobileMenu(false);

  if (hamburger) {
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMobileMenu();
    });
  }

  /* ----------------------------------------------------------
   *  3. Smooth Scroll
   * -------------------------------------------------------- */

  /**
   * Smoothly scroll to an element, accounting for the fixed header.
   * @param {HTMLElement} target
   */
  const smoothScrollTo = (target) => {
    if (!target) return;
    const top = target.getBoundingClientRect().top + window.scrollY - HEADER_OFFSET;
    window.scrollTo({ top, behavior: 'smooth' });
  };

  allAnchors.forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (!href || href === '#') return;

      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();
      smoothScrollTo(target);

      // 6. Close mobile menu when clicking a nav link
      closeMobileMenu();

      // Update URL hash without jumping
      history.pushState(null, '', href);
    });
  });

  /* ----------------------------------------------------------
   *  4. Active Section Highlighting (IntersectionObserver)
   * -------------------------------------------------------- */

  /** Map of section-id → nav link element for quick lookup */
  const navLinkMap = new Map();
  navAnchors.forEach((link) => {
    const id = link.getAttribute('href')?.replace('#', '');
    if (id) navLinkMap.set(id, link);
  });

  const activateNavLink = (id) => {
    navAnchors.forEach((link) => link.classList.remove('active'));
    const active = navLinkMap.get(id);
    if (active) active.classList.add('active');
  };

  if (sections.length && navLinkMap.size) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            activateNavLink(entry.target.id);
          }
        });
      },
      {
        // Trigger when the top ~40 % of the section is visible
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0,
      }
    );

    sections.forEach((section) => sectionObserver.observe(section));
  }

  /* ----------------------------------------------------------
   *  5. Keyboard Navigation — "Pitch Mode"
   * -------------------------------------------------------- */

  /** Ordered list of navigable sections */
  const pitchSections = sections.length ? sections : [];
  let currentSectionIndex = 0;

  /**
   * Determine the index of the section closest to the current scroll
   * position so pitch-mode always starts from the right place.
   */
  const syncCurrentIndex = () => {
    const scrollY = window.scrollY + HEADER_OFFSET + 10;
    for (let i = pitchSections.length - 1; i >= 0; i--) {
      if (pitchSections[i].offsetTop <= scrollY) {
        currentSectionIndex = i;
        return;
      }
    }
    currentSectionIndex = 0;
  };

  /**
   * Navigate by direction.
   * @param {'next' | 'prev'} direction
   */
  const navigateSection = (direction) => {
    syncCurrentIndex();

    if (direction === 'next' && currentSectionIndex < pitchSections.length - 1) {
      currentSectionIndex++;
    } else if (direction === 'prev' && currentSectionIndex > 0) {
      currentSectionIndex--;
    }

    smoothScrollTo(pitchSections[currentSectionIndex]);
  };

  document.addEventListener('keydown', (e) => {
    // Only activate pitch-mode when no input / textarea is focused
    const tag = document.activeElement?.tagName.toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select') return;

    switch (e.key) {
      case 'ArrowDown':
      case ' ':            // Space bar
        e.preventDefault();
        navigateSection('next');
        break;
      case 'ArrowUp':
        e.preventDefault();
        navigateSection('prev');
        break;
      default:
        break;
    }
  });

  /* ----------------------------------------------------------
   *  6 & 7. Close mobile menu on link click & outside click
   * -------------------------------------------------------- */

  // Link-click closing is handled inside the smooth-scroll handler above.

  // Close when tapping the overlay backdrop
  overlay.addEventListener('click', closeMobileMenu);

  // Close on any click outside the nav when menu is open
  document.addEventListener('click', (e) => {
    if (
      navLinks &&
      navLinks.classList.contains('active') &&
      !navLinks.contains(e.target) &&
      !hamburger?.contains(e.target)
    ) {
      closeMobileMenu();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMobileMenu();
  });

  /* ----------------------------------------------------------
   *  Scroll Listener (throttled)
   * -------------------------------------------------------- */
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        handleStickyNav();
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  // Run once on load
  handleStickyNav();
})();
