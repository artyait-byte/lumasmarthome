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
  'lighting-scene':   'https://images.unsplash.com/photo-1540932239986-30128078f3c5?auto=format&fit=crop&w=1600&q=80',
  'window-shades':    'https://images.unsplash.com/photo-1505692794403-34cb9f8c7bbe?auto=format&fit=crop&w=1600&q=80',
  'home-theater':     'https://images.unsplash.com/photo-1489599510096-6e16d4b2b3c8?auto=format&fit=crop&w=1600&q=80',
  'audio-system':     'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=1600&q=80',
  'security-camera':  'https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?auto=format&fit=crop&w=1600&q=80',
  'networking-rack':  'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1600&q=80',
  'gulf-sunset':      'https://images.unsplash.com/photo-1585771724684-38269d6639fd?auto=format&fit=crop&w=1600&q=80',

  // ---------- Hero / lifestyle -------------------------------------------
  'waterfront-lanai': 'https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1600&q=80',

  // ---------- Projects page (one key per unique photo) -------------------
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
