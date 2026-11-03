// Demo-sivuston kevyt vuorovaikutus. Mikään ei lähetä dataa minnekään.
(function () {
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
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

  // Ajanvaraus (demo: kalenteri ja ajat ovat esimerkkejä, mitään ei tallenneta)
  var bk = document.getElementById('booking-form');
  if (bk) {
    var MONTHS = ['tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesäkuu', 'heinäkuu', 'elokuu', 'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu'];
    var DAYS = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su'];
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var view = new Date(today.getFullYear(), today.getMonth(), 1);
    var minView = new Date(view), maxView = new Date(today.getFullYear(), today.getMonth() + 3, 1);
    var selDay = null, selSlot = null;
    var grid = document.getElementById('cal-grid'), calTitle = document.getElementById('cal-title');
    var slotsEl = document.getElementById('slots'), slotsTitle = document.getElementById('slots-title');
    var errEl = document.getElementById('bk-error');
    var done = document.getElementById('booking-done');

    function sameDay(a, b) { return a && b && a.getTime() === b.getTime(); }
    function fmtDate(d) { return DAYS[(d.getDay() + 6) % 7] + ' ' + d.getDate() + '.' + (d.getMonth() + 1) + '.' + d.getFullYear(); }
    // Näennäissatunnaiset varatut ajat, samat joka latauksella
    function taken(d, i) { return ((d.getDate() * 31 + (d.getMonth() + 1) * 7 + i * 13) % 10) < 3; }

    function renderCal() {
      calTitle.textContent = MONTHS[view.getMonth()] + ' ' + view.getFullYear();
      grid.innerHTML = '';
      var y = view.getFullYear(), m = view.getMonth();
      var offset = (new Date(y, m, 1).getDay() + 6) % 7;
      for (var i = 0; i < offset; i++) grid.appendChild(document.createElement('span'));
      var days = new Date(y, m + 1, 0).getDate();
      for (var d = 1; d <= days; d++) {
        (function (d) {
          var date = new Date(y, m, d);
          var b = document.createElement('button');
          b.type = 'button'; b.className = 'cal-day'; b.textContent = d;
          var wknd = date.getDay() === 0 || date.getDay() === 6;
          if (wknd || date <= today) b.disabled = true;
          if (sameDay(date, today)) b.classList.add('today');
          if (sameDay(date, selDay)) { b.classList.add('selected'); b.setAttribute('aria-pressed', 'true'); }
          b.setAttribute('aria-label', fmtDate(date) + (b.disabled ? ', ei varattavissa' : ''));
          b.addEventListener('click', function () { selDay = date; selSlot = null; renderCal(); renderSlots(); update(); });
          grid.appendChild(b);
        })(d);
      }
      bk.querySelectorAll('.cal-nav').forEach(function (n) {
        var dir = parseInt(n.getAttribute('data-cal'), 10);
        n.disabled = dir < 0 ? view <= minView : view >= maxView;
      });
    }
    function renderSlots() {
      slotsEl.innerHTML = '';
      if (!selDay) { slotsTitle.textContent = 'Valitse ensin päivä kalenterista.'; return; }
      slotsTitle.textContent = 'Vapaat ajat ' + fmtDate(selDay);
      for (var i = 0; i < 18; i++) {
        (function (i) {
          var t = (9 + Math.floor(i / 2)) + '.' + (i % 2 ? '30' : '00');
          var b = document.createElement('button');
          b.type = 'button'; b.className = 'slot'; b.textContent = t;
          if (taken(selDay, i)) { b.disabled = true; b.classList.add('taken'); b.setAttribute('aria-label', t + ', varattu'); }
          if (selSlot === t) { b.classList.add('selected'); b.setAttribute('aria-pressed', 'true'); }
          b.addEventListener('click', function () { selSlot = t; renderSlots(); update(); });
          slotsEl.appendChild(b);
        })(i);
      }
    }
    function checked(name) { var el = bk.querySelector('input[name="' + name + '"]:checked'); return el ? el.value : ''; }
    function update() {
      document.getElementById('s-topic').textContent = checked('topic') || '–';
      document.getElementById('s-method').textContent = checked('method') || '–';
      document.getElementById('s-time').textContent = selDay && selSlot ? fmtDate(selDay) + ' klo ' + selSlot : '–';
      if (errEl) errEl.hidden = true;
    }
    bk.querySelectorAll('.choice input').forEach(function (inp) {
      inp.addEventListener('change', function () {
        bk.querySelectorAll('input[name="' + inp.name + '"]').forEach(function (o) { o.closest('.choice').classList.toggle('selected', o.checked); });
        update();
      });
    });
    bk.querySelectorAll('.cal-nav').forEach(function (n) {
      n.addEventListener('click', function () {
        view = new Date(view.getFullYear(), view.getMonth() + parseInt(n.getAttribute('data-cal'), 10), 1);
        renderCal();
      });
    });
    function fail(msg, focusEl) {
      errEl.textContent = msg; errEl.hidden = false;
      if (focusEl) focusEl.scrollIntoView({ block: 'center', behavior: reduceMotion ? 'auto' : 'smooth' });
    }
    bk.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!checked('topic')) return fail('Valitse ensin asian aihe (kohta 1).', bk.querySelector('.choices'));
      if (!checked('method')) return fail('Valitse tapaamistapa (kohta 2).', bk.querySelector('.choices-3'));
      if (!selDay || !selSlot) return fail('Valitse päivä ja kellonaika (kohta 3).', bk.querySelector('.cal'));
      if (!bk.checkValidity()) { bk.reportValidity(); return; }
      document.getElementById('done-time').textContent = fmtDate(selDay) + ' klo ' + selSlot + ' (' + checked('method').toLowerCase() + ')';
      document.getElementById('done-email').textContent = bk.querySelector('#b-email').value;
      bk.hidden = true; done.hidden = false;
      done.scrollIntoView({ block: 'center', behavior: reduceMotion ? 'auto' : 'smooth' });
      toast('Demo: varausta ei tallennettu eikä kutsua lähetetty.');
    });
    done.querySelectorAll('[data-booking-reset]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        bk.reset(); selDay = null; selSlot = null;
        bk.querySelectorAll('.choice').forEach(function (c) { c.classList.remove('selected'); });
        done.hidden = true; bk.hidden = false;
        renderCal(); renderSlots(); update();
        bk.scrollIntoView({ block: 'start', behavior: reduceMotion ? 'auto' : 'smooth' });
      });
    });
    renderCal(); renderSlots(); update();
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
