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
  //  Curated from licensed stock (Unsplash / Pexels) in the same visual lane as
  //  premium U.S. integrator sites — not hotlinked from third-party commercial sites.
  'lighting-scene':   '/assets/photos/lighting-scene.jpg?v=4',
  'window-shades':    '/assets/photos/window-shades.jpg?v=4',
  'home-theater':     '/assets/photos/home-theater.jpg?v=4',
  // Audio & Video: background is set in styles.css class `.luma-bg--audio` (bypasses stale images.js)
  'security-camera':  '/assets/photos/security-camera.jpg?v=4',
  'networking-rack':  '/assets/photos/networking-rack.jpg?v=4',
  'gulf-sunset':      '/assets/photos/gulf-sunset.jpg?v=4',

  // ---------- Lighting page — feature rows (RadioRA 3, designers) ---------
  'lighting-lutron-hero': '/assets/photos/lighting-lutron-hero.jpg?v=4',

  // ---------- Hero / lifestyle -------------------------------------------
  'waterfront-lanai': '/assets/photos/waterfront-lanai.jpg?v=4',

  // ---------- Designers page (architectural lighting portrait) -----------
  'designers-chandelier': '/assets/photos/designers-chandelier.jpg?v=4',

  // ---------- Projects page (one key per unique photo) -------------------
  //   Still on Unsplash hotlink — will migrate to local when we have
  //   LUMA's own project photography.
  'project-bayfront':      'https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=1200&q=80',
  'project-luxury-pool':   'https://images.unsplash.com/photo-1600566753190-17f0baf2a6c3?auto=format&fit=crop&w=1200&q=80',
  'project-modern-villa':  'https://images.unsplash.com/photo-1605146769289-440113cc3d00?auto=format&fit=crop&w=1200&q=80',
  'project-warm-interior': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80',
  'project-architectural': 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80'
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
