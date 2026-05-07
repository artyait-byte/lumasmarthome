// ==========================================================================
//  LUMA Smart Home — central image registry
// ==========================================================================
//  Single source of truth for every photo on the site.  Swap a URL here
//  once → every page that uses the key picks it up automatically.
//
//  How it works:
//    • HTML elements opt in with `data-img="key"` (no inline background-image).
//    • On DOMContentLoaded we read all [data-img] elements and set their
//      inline `background-image` from this map.
//    • Keys are *content-based* (e.g. `gulf-sunset`), not position-based, so
//      renaming one slot doesn't force us to rename the key.
// ==========================================================================

window.LUMA_IMAGES = {
  // ---------- Smart Home Solutions — 7 menu categories -------------------
  'lighting-scene':   '/assets/photos/lighting-scene.jpg?v=5',
  'window-shades':    '/assets/photos/window-shades.jpg?v=5',
  'home-theater':     '/assets/photos/home-theater.jpg?v=5',
  'security-camera':  '/assets/photos/security-camera.jpg?v=5',
  'networking-rack':  '/assets/photos/networking-rack.jpg?v=5',
  'gulf-sunset':      '/assets/photos/gulf-sunset.jpg?v=5',

  // ---------- Lighting page — feature rows (RadioRA 3, designers) ---------
  'lighting-lutron-hero': '/assets/photos/lighting-lutron-hero.jpg?v=5',

  // ---------- Hero / lifestyle -------------------------------------------
  'waterfront-lanai': '/assets/photos/waterfront-lanai.jpg?v=5',

  // ---------- Designers page (architectural lighting portrait) -----------
  'designers-chandelier': '/assets/photos/designers-chandelier.jpg?v=5',

  // ---------- Projects page — local assets (same pool as SPA index.html) ---
  'project-bayfront':      '/assets/photos/waterfront-lanai.jpg?v=5',
  'project-luxury-pool':   '/assets/photos/gulf-sunset.jpg?v=5',
  'project-modern-villa':  '/assets/photos/waterfront-lanai.jpg?v=5',
  'project-warm-interior': '/assets/photos/lighting-scene.jpg?v=5',
  'project-architectural': '/assets/photos/designers-chandelier.jpg?v=5'
};

// --------------------------------------------------------------------------
//  Loader — applies LUMA_IMAGES to every [data-img] element.
// --------------------------------------------------------------------------
(function () {
  'use strict';

  function apply() {
    var map = window.LUMA_IMAGES || {};
    var els = document.querySelectorAll('[data-img]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      var key = el.getAttribute('data-img');
      var url = map[key];
      if (url) {
        el.style.backgroundImage = "url('" + url + "')";
      } else if (key) {
        console.warn('[LUMA_IMAGES] missing key:', key);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();
