// LUMA Smart Home — v2 interactions
//   • mobile nav toggle
//   • active link highlight
//   • mega-menu hover/click (desktop) + accordion (mobile)
//   • hero carousel (Ken Burns fade)
//   • IntersectionObserver reveal
//   • contact form demo handler
//   • budget calculator (multi-step → results table)

(function () {
  'use strict';

  // ---------- Mobile nav toggle ----------
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      menu.classList.toggle('is-open');
      var expanded = menu.classList.contains('is-open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // ---------- Active link ----------
  var path = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-menu a').forEach(function (a) {
    var href = (a.getAttribute('href') || '').toLowerCase().split('#')[0];
    if (href === path || (path === '' && href === 'index.html')) {
      a.classList.add('is-active');
    }
  });

  // ---------- Mega-menu ----------
  // Behavior: click the chevron to open — panel stays open until user clicks
  // outside it, presses Escape, or picks a link. Hover is intentionally NOT
  // used to open/close, so moving the mouse around can't accidentally dismiss it.
  var megaItems = document.querySelectorAll('.nav-item[data-mega]');
  megaItems.forEach(function (item) {
    var btn = item.querySelector('button');

    if (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        // Close any other open mega before toggling this one
        megaItems.forEach(function (other) {
          if (other !== item) {
            other.classList.remove('is-open');
            var ob = other.querySelector('button');
            if (ob) ob.setAttribute('aria-expanded', 'false');
          }
        });
        var isOpen = item.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    }

    // Swap preview image on hover / focus of each link
    var stage = item.querySelector('[data-preview-stage]');
    var title = item.querySelector('[data-preview-title]');
    var slides = stage ? stage.querySelectorAll('.slide') : [];
    var links = item.querySelectorAll('.mega-link');

    function showPreview(key, titleText) {
      if (!stage) return;
      slides.forEach(function (s) {
        s.classList.toggle('is-on', s.getAttribute('data-for') === key);
      });
      links.forEach(function (l) { l.classList.toggle('is-hot', l.getAttribute('data-preview') === key); });
      if (title && titleText) title.textContent = titleText;
    }

    links.forEach(function (link) {
      var key = link.getAttribute('data-preview');
      var titleEl = link.querySelector('h5');
      var titleText = titleEl ? titleEl.textContent : '';
      link.addEventListener('mouseenter', function () { showPreview(key, titleText); });
      link.addEventListener('focus',      function () { showPreview(key, titleText); });
    });
  });

  // Click outside closes any open mega
  document.addEventListener('click', function (e) {
    megaItems.forEach(function (item) {
      if (item.classList.contains('is-open') && !item.contains(e.target)) {
        item.classList.remove('is-open');
        var b = item.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
  });
  // Escape closes mega
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      megaItems.forEach(function (item) { item.classList.remove('is-open'); });
    }
  });

  // ---------- Hero carousel ----------
  var hero = document.querySelector('[data-hero]');
  var dots = document.querySelector('[data-hero-dots]');
  var captionEl = document.querySelector('[data-hero-caption]');
  if (hero) {
    var slides = Array.prototype.slice.call(hero.querySelectorAll('.slide'));
    var dotBtns = dots ? Array.prototype.slice.call(dots.querySelectorAll('button')) : [];
    var idx = 0;

    function show(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach(function (s, si) { s.classList.toggle('is-on', si === idx); });
      dotBtns.forEach(function (b, bi) { b.classList.toggle('is-on', bi === idx); });
      if (captionEl) {
        var cap = slides[idx].getAttribute('data-caption') || '';
        captionEl.innerHTML = '<span>Now playing</span>' + cap;
      }
    }

    dotBtns.forEach(function (b) {
      b.addEventListener('click', function () { show(parseInt(b.getAttribute('data-idx'), 10) || 0); reset(); });
    });

    var timer;
    function reset() { clearInterval(timer); timer = setInterval(function () { show(idx + 1); }, 5500); }
    reset();
  }

  // ---------- Reveal on scroll ----------
  if ('IntersectionObserver' in window) {
    var els = document.querySelectorAll('[data-reveal]');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.transition = 'opacity 600ms ease, transform 600ms ease';
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.08 });
    els.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(14px)';
      io.observe(el);
    });
  }

  // ---------- Footer year ----------
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();

  // ---------- Netlify Forms AJAX helper ----------
  // Posts a <form> via fetch() to Netlify's endpoint so the user stays on page.
  // Requires: data-netlify="true" + a hidden <input name="form-name" …/>.
  function encodeFormData(formEl) {
    var data = new FormData(formEl);
    var pairs = [];
    data.forEach(function (v, k) {
      pairs.push(encodeURIComponent(k) + '=' + encodeURIComponent(v));
    });
    return pairs.join('&');
  }

  function submitToNetlify(formEl, onSuccess, onError) {
    fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: encodeFormData(formEl)
    }).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      if (onSuccess) onSuccess();
    }).catch(function (err) {
      if (onError) onError(err);
    });
  }

  // ---------- Contact form (Netlify Forms) ----------
  document.querySelectorAll('[data-contact-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('[data-form-status]');
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.dataset.orig = btn.innerHTML; btn.innerHTML = 'Sending…'; }
      if (status) { status.textContent = ''; }

      submitToNetlify(form, function () {
        if (status) {
          status.textContent = 'Thank you. We will be in touch within 2 business hours.';
          status.style.color = '#1A6B60';
        }
        form.reset();
        if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.orig || 'Send'; }
      }, function () {
        if (status) {
          status.textContent = 'Something went wrong. Please call +1 (941) 217-1616 or email hello@lumasmarthome.com.';
          status.style.color = '#B56B3A';
        }
        if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.orig || 'Send'; }
      });
    });
  });

  // ============================================================
  //  Budget calculator
  // ============================================================
  var calc = document.querySelector('[data-calc]');
  if (calc) {
    var steps = calc.querySelectorAll('.calc-step');
    var progress = calc.querySelector('[data-progress]');
    var counter  = calc.querySelector('[data-step-count]');
    var btnNext  = calc.querySelector('[data-next]');
    var btnPrev  = calc.querySelector('[data-prev]');
    var btnSubmit = calc.querySelector('[data-submit]');
    var result   = calc.querySelector('[data-result]');
    var body     = calc.querySelector('[data-body]');
    var actions  = calc.querySelector('[data-actions]');
    var answers  = {};
    var cur = 0;
    var total = steps.length;

    function renderStep() {
      steps.forEach(function (s, i) { s.classList.toggle('is-active', i === cur); });
      if (progress) progress.style.width = ((cur + 1) / total * 100).toFixed(1) + '%';
      if (counter)  counter.textContent = 'Step ' + (cur + 1) + ' / ' + total;
      if (btnPrev)  btnPrev.style.visibility = (cur === 0) ? 'hidden' : 'visible';
      if (btnNext)  btnNext.style.display = (cur === total - 1) ? 'none' : '';
      if (btnSubmit) btnSubmit.style.display = (cur === total - 1) ? '' : 'none';
    }
    renderStep();

    // Selection logic
    calc.querySelectorAll('.calc-opt').forEach(function (opt) {
      opt.addEventListener('click', function () {
        var step = opt.closest('.calc-step');
        var key = step.getAttribute('data-key');
        step.querySelectorAll('.calc-opt').forEach(function (o) { o.classList.remove('is-selected'); });
        opt.classList.add('is-selected');
        answers[key] = {
          label: opt.getAttribute('data-label') || opt.querySelector('strong').textContent,
          low:   parseFloat(opt.getAttribute('data-low'))  || 0,
          high:  parseFloat(opt.getAttribute('data-high')) || 0,
          pick:  parseFloat(opt.getAttribute('data-pick')) || 0
        };
      });
    });

    function next() { if (cur < total - 1) { cur++; renderStep(); } }
    function prev() { if (cur > 0) { cur--; renderStep(); } }

    if (btnNext)  btnNext.addEventListener('click', next);
    if (btnPrev)  btnPrev.addEventListener('click', prev);

    if (btnSubmit) btnSubmit.addEventListener('click', function () {
      // Build result
      var rows = '';
      var summaryLines = [];
      var lowT = 0, highT = 0, pickT = 0;
      Object.keys(answers).forEach(function (k) {
        var a = answers[k];
        rows += '<tr>' +
          '<td>' + prettyKey(k) + '</td>' +
          '<td>' + a.label + '</td>' +
          '<td class="num">$' + fmt(a.low)  + '</td>' +
          '<td class="num">$' + fmt(a.high) + '</td>' +
          '<td class="num"><strong>$' + fmt(a.pick) + '</strong></td>' +
          '</tr>';
        summaryLines.push(prettyKey(k) + ': ' + a.label + ' — $' + fmt(a.pick));
        lowT  += a.low;
        highT += a.high;
        pickT += a.pick;
      });
      rows += '<tr class="total">' +
        '<td colspan="2">Your estimated investment</td>' +
        '<td class="num">$' + fmt(lowT)  + '</td>' +
        '<td class="num">$' + fmt(highT) + '</td>' +
        '<td class="num">$' + fmt(pickT) + '</td>' +
        '</tr>';

      if (result) {
        result.querySelector('tbody').innerHTML = rows;
        result.classList.add('is-active');
      }
      if (body) body.style.display = 'none';
      if (actions) actions.style.display = 'none';

      var sel  = calc.querySelector('[data-selections]');
      var tLow = calc.querySelector('[data-total-low]');
      var tHi  = calc.querySelector('[data-total-high]');
      var tPk  = calc.querySelector('[data-total-pick]');
      if (sel)  sel.value  = summaryLines.join('\n');
      if (tLow) tLow.value = fmt(lowT);
      if (tHi)  tHi.value  = fmt(highT);
      if (tPk)  tPk.value  = fmt(pickT);

      window.scrollTo({ top: calc.offsetTop - 60, behavior: 'smooth' });
    });

    function prettyKey(k) {
      return k.replace(/[-_]/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
    }
    function fmt(n) {
      return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }

    // Email capture inside result (Netlify Forms)
    var emailForm = calc.querySelector('[data-email-form]');
    if (emailForm) {
      emailForm.addEventListener('submit', function (e) {
        e.preventDefault();
        var status = emailForm.querySelector('[data-email-status]');
        var btn = emailForm.querySelector('button[type="submit"]');
        if (btn) { btn.disabled = true; btn.dataset.orig = btn.innerHTML; btn.innerHTML = 'Sending…'; }
        submitToNetlify(emailForm, function () {
          if (status) {
            status.textContent = 'Estimate sent. Check your inbox within 1 minute.';
            status.style.color = '#1A6B60';
          }
          var emailInput = emailForm.querySelector('input[type="email"]');
          if (emailInput) emailInput.value = '';
          if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.orig || 'Send PDF'; }
        }, function () {
          if (status) {
            status.textContent = 'Could not send. Please try again or email hello@lumasmarthome.com.';
            status.style.color = '#B56B3A';
          }
          if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.orig || 'Send PDF'; }
        });
      });
    }
  }
})();
