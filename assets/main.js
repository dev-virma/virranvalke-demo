// Demo-sivuston kevyt vuorovaikutus. Mikään ei lähetä dataa minnekään.
(function () {
  var toastEl = document.getElementById('toast');
  var toastTimer;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 3500);
  }

  // Demo-banneri: suljettava, valinta muistetaan selaimessa
  var banner = document.getElementById('demo-banner');
  if (banner) {
    var bannerClosed = null;
    try { bannerClosed = localStorage.getItem('vv-demo-banner'); } catch (e) {}
    if (bannerClosed) banner.classList.add('hidden');
    var closeBtn = banner.querySelector('[data-demo-close]');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        banner.classList.add('hidden');
        try { localStorage.setItem('vv-demo-banner', 'closed'); } catch (e) {}
      });
    }
  }

  // Mobiilivalikko
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // Valikko sulkeutuu, kun linkkiä klikataan tai painetaan Esc
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); });
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); toggle.focus(); }
    });
  }

  // Evästebanneri (demo: tallentaa vain valinnan selaimeen)
  var cookie = document.getElementById('cookie');
  if (cookie) {
    var seen = null;
    try { seen = localStorage.getItem('vv-demo-cookie'); } catch (e) {}
    if (!seen) cookie.classList.add('show');
    cookie.querySelectorAll('[data-cookie]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        try { localStorage.setItem('vv-demo-cookie', btn.getAttribute('data-cookie')); } catch (e) {}
        cookie.classList.remove('show');
        toast('Demo: evästevalinta tallennettu vain tähän selaimeen.');
      });
    });
  }

  // Yhteydenottolomake (demo: ei lähetä mitään)
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      toast('Demo: lomake ei vielä lähetä viestiä. Soita +358 50 559 8200 tai lähetä sähköpostia.');
    });
  }

  // Kurssin tilauslomake (demo: ei maksua, ei lähetystä)
  var orderForm = document.getElementById('order-form');
  var orderDone = document.getElementById('order-done');
  if (orderForm && orderDone) {
    orderForm.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var e1 = orderForm.querySelector('#o-email'), e2 = orderForm.querySelector('#o-email2');
      e2.setCustomValidity(e1.value && e1.value !== e2.value ? 'Sähköpostiosoitteet eivät täsmää.' : '');
      if (!orderForm.checkValidity()) { orderForm.reportValidity(); return; }
      var target = document.getElementById('order-email');
      if (target) target.textContent = e1.value;
      orderForm.hidden = true;
      orderDone.hidden = false;
      orderDone.scrollIntoView({ block: 'nearest', behavior: reduceMotion ? 'auto' : 'smooth' });
      toast('Demo: tilausta ei käsitelty eikä maksua veloitettu.');
    });
    orderDone.querySelectorAll('[data-order-reset]').forEach(function (btn) {
      btn.addEventListener('click', function () { orderDone.hidden = true; orderForm.hidden = false; });
    });
  }

  // Muut demo-painikkeet
  document.querySelectorAll('[data-demo]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      ev.preventDefault();
      toast(el.getAttribute('data-demo'));
    });
  });

  // Evästeet-linkki footerissa avaa bannerin uudelleen
  document.querySelectorAll('[data-cookie-open]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      ev.preventDefault();
      if (cookie) cookie.classList.add('show');
    });
  });

  // Ylätunnisteen varjo vieritettäessä
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero: hiiren mukana liikkuva parallaksi (vesileima ja yhteystietokortti)
  var hero = document.getElementById('hero');
  var heroCard = hero && hero.querySelector('.hero-card');
  if (hero && !reduceMotion) {
    if (heroCard) {
      heroCard.addEventListener('animationend', function () { heroCard.classList.add('settled'); }, { once: true });
    }
    hero.addEventListener('mousemove', function (ev) {
      var r = hero.getBoundingClientRect();
      var mx = ((ev.clientX - r.left) / r.width - 0.5) * 2;
      var my = ((ev.clientY - r.top) / r.height - 0.5) * 2;
      hero.style.setProperty('--mx', mx.toFixed(3));
      hero.style.setProperty('--my', my.toFixed(3));
    });
    hero.addEventListener('mouseleave', function () {
      hero.style.setProperty('--mx', '0');
      hero.style.setProperty('--my', '0');
    });
  }

  // Lukujen laskuri heron avainluvuissa
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var to = parseInt(el.getAttribute('data-count'), 10);
    var from = parseInt(el.getAttribute('data-from') || '0', 10);
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduceMotion || isNaN(to)) { el.textContent = to + suffix; return; }
    var start = null, dur = 1400;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(from + (to - from) * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    setTimeout(function () { requestAnimationFrame(step); }, 500);
  });

  // Sisällön pehmeä ilmestyminen vieritettäessä
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    reveals.forEach(function (el, i) { el.style.transitionDelay = (i % 4) * 60 + 'ms'; io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }
})();
