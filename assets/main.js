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

  // Mobiilivalikko
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
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
