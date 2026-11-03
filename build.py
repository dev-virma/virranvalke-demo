# -*- coding: utf-8 -*-
"""Generoi demo-sivuston HTML-sivut yhteisellä headerilla ja footerilla."""
import sys, os

OUT = sys.argv[1]

ICON = {
  "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l4-4h4l3 3"/><path d="M21 11l-4-4h-3"/><path d="M7 14l3 3a2 2 0 0 0 3 0l1-1"/><path d="M10 11l3 3a2 2 0 0 0 3 0"/><path d="M3 11v5h3"/><path d="M21 11v5h-3"/></svg>',
  "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 12h18"/></svg>',
  "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
  "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18"/><path d="M5 7h14"/><path d="M8 21h8"/><path d="M5 7l-3 7a3 3 0 0 0 6 0z"/><path d="M19 7l-3 7a3 3 0 0 0 6 0z"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
  "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
  "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
  "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/></svg>',
  "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19a2 2 0 0 1 2-2h13"/><path d="M8 7h7"/></svg>',
  "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h6"/></svg>',
  "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 12l3 3 5-6"/></svg>',
  "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M10 9l5 3-5 3z"/></svg>',
  "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6h11M9 12h11M9 18h11"/><circle cx="5" cy="6" r="1"/><circle cx="5" cy="12" r="1"/><circle cx="5" cy="18" r="1"/></svg>',
  "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/></svg>',
  "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
  "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
}
# Kiinteä koko ikoneille, jotta ne eivät piirry jättikokoisina, jos CSS ei ole vielä latautunut.
ICON = {k: v.replace('<svg ', '<svg width="24" height="24" ', 1) for k, v in ICON.items()}

def brand_mark(uid):
    """Virta-V-logomerkki. uid erottaa gradientin id:n, jos merkki on sivulla useasti."""
    return f'''<svg class="brand-mark" width="38" height="38" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="vv-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9d9b5"/><stop offset="1" stop-color="#b8892f"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="#122441"/><path d="M14 20 C 21 18, 26 32, 32 46 C 38 32, 43 18, 50 20" fill="none" stroke="url(#vv-{uid})" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M49 8 l1.7 4.3 4.3 1.7 -4.3 1.7 -1.7 4.3 -1.7 -4.3 -4.3 -1.7 4.3 -1.7z" fill="#e9d9b5"/></svg>'''

BRAND_MARK = brand_mark("h")
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%23122441'/%3E%3Cpath d='M14 20 C 21 18, 26 32, 32 46 C 38 32, 43 18, 50 20' fill='none' stroke='%23d6b86a' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M49 8 l1.7 4.3 4.3 1.7 -4.3 1.7 -1.7 4.3 -1.7 -4.3 -4.3 -1.7 4.3 -1.7z' fill='%23e9d9b5'/%3E%3C/svg%3E"

NAV = [
  ("index.html", "Koti"),
  ("index.html#palvelut", "Palvelut"),
  ("tietoa-meista.html", "Tietoa meistä"),
  ("tiimimme.html", "Tiimimme"),
  ("yhteydenotto.html", "Yhteydenotto"),
]

TRUST = '''<section class="trust" aria-label="Lyhyesti">
  <div class="container trust-grid">
    <div class="trust-item"><span class="trust-icon">''' + ICON["clock"] + '''</span><div><strong>Ensimmäiset 15 min ilmaiseksi</strong><span>Toimeksiannon selvittämistapaaminen ei maksa mitään</span></div></div>
    <div class="trust-item"><span class="trust-icon">''' + ICON["scale"] + '''</span><div><strong>Kiinteä hinta mahdollinen</strong><span>Palvelukohtainen hinta, jota ei ylitetä sopimatta</span></div></div>
    <div class="trust-item"><span class="trust-icon">''' + ICON["video"] + '''</span><div><strong>Online-virtuaalitoimisto</strong><span>Palaverit Skype- ja Teams-yhteyksin</span></div></div>
    <div class="trust-item"><span class="trust-icon">''' + ICON["pin"] + '''</span><div><strong>Joensuu ja pääkaupunkiseutu</strong><span>Toiminta-alue ensisijaisesti Joensuun seutu</span></div></div>
  </div>
</section>
'''

def wave_path(y, amp, width=1600, period=200):
    """Jaksollinen aaltopolku, jonka jakso on `period`, jotta animaatio kiertää saumattomasti."""
    half = period / 2
    d = f"M0 {y} Q{half/2:.0f} {y-amp} {half:.0f} {y}"
    x = half
    while x < width + period:
        d += f" T{x+half:.0f} {y}"
        x += half
    return d

HERO_BG = '''<div class="hero-bg" aria-hidden="true">
  <svg class="waves" viewBox="0 0 1600 200" preserveAspectRatio="none">
    <path class="wave" d="''' + wave_path(120, 18) + '''"/>
    <path class="wave" d="''' + wave_path(150, 14) + '''"/>
    <path class="wave" d="''' + wave_path(178, 10) + '''"/>
  </svg>
''' + "".join(
    f'  <span class="spark" style="--x:{x}%;--y:{y}%;--d:{d}s;--dl:{dl}s;--s:{s}"></span>\n'
    for x, y, d, dl, s in [
        (8, 22, 4.2, 0.0, 1.0), (19, 68, 5.1, 1.3, 0.7), (31, 14, 3.8, 2.1, 0.8), (44, 80, 4.6, 0.6, 1.1),
        (57, 30, 5.4, 1.8, 0.6), (66, 62, 4.0, 2.6, 0.9), (78, 18, 4.8, 0.9, 1.2), (87, 74, 3.6, 1.5, 0.7),
        (93, 42, 5.0, 2.9, 0.9), (26, 46, 4.4, 3.4, 0.6), (72, 88, 4.1, 2.3, 0.8), (50, 54, 3.9, 0.3, 0.5),
    ]
) + '''</div>
'''

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – Lakiasiaintoimisto Virranvälke (demo)</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{title} – Lakiasiaintoimisto Virranvälke">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fi_FI">
<meta name="theme-color" content="#122441">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v=11">
<link rel="icon" href="{FAVICON}">
</head>
<body>
<a class="skip-link" href="#main">Siirry sisältöön</a>
<div class="demo-banner" id="demo-banner"><span><strong>Demo</strong> Tämä on esittelyversio uudesta sivustosta. Lomakkeet ja painikkeet eivät vielä tee mitään oikeasti.</span><button class="demo-close" type="button" aria-label="Sulje demo-ilmoitus" data-demo-close>&times;</button></div>
'''

def header(current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    return f'''<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">{BRAND_MARK}<span class="brand-text"><small>Lakiasiaintoimisto</small><span>Virranvälke</span></span></a>
    <button class="nav-toggle" aria-label="Valikko" aria-expanded="false" aria-controls="nav">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav" id="nav">{links}<a class="btn btn-gold btn-sm" href="tel:+358505598200">{ICON["phone"]} 050 559 8200</a></nav>
  </div>
</header>
<main id="main">
'''

FOOTER = '''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand brand-footer" href="index.html">''' + brand_mark("f") + '''<span class="brand-text"><small>Lakiasiaintoimisto</small><span>Virranvälke</span></span></a>
        <p>Lakiasiantuntijat palveluksessasi. Online-virtuaalitoimisto Joensuusta, tapaamiset sopimuksen mukaan.</p>
        <p class="footer-meta">Y-tunnus 3192420-6</p>
      </div>
      <div>
        <h4>Yhteystiedot</h4>
        <ul>
          <li><a href="tel:+358505598200">+358 50 559 8200</a></li>
          <li><a href="mailto:ovirma@gmail.com">ovirma@gmail.com</a></li>
          <li><a href="yhteydenotto.html">Yhteydenottolomake</a></li>
        </ul>
      </div>
      <div>
        <h4>Sivusto</h4>
        <ul>
          <li><a href="index.html#kurssit">Minidigikurssit</a></li>
          <li><a href="tietoa-meista.html">Tietoa meistä</a></li>
          <li><a href="tiimimme.html">Tiimimme</a></li>
          <li><a href="tietosuojaseloste.html">Tietosuojaseloste</a></li>
          <li><a href="kayttoehdot.html">Käyttöehdot</a></li>
          <li><a href="tietosuojakaytanto.html">Tietosuojakäytäntö</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Lakiasiaintoimisto Virranvälke</span>
      <span>Demo-sivusto · <a href="#" data-cookie-open>Evästeet</a></span>
    </div>
  </div>
</footer>

<div class="cookie" id="cookie" role="dialog" aria-label="Evästeet">
  <p>Käytämme evästeitä mahdollistaaksemme verkkosivustomme asianmukaisen toiminnan ja turvallisuuden sekä tarjotaksemme sinulle parhaan mahdollisen käyttökokemuksen.</p>
  <div class="cookie-actions">
    <button class="btn btn-primary btn-sm" data-cookie="necessary">Hyväksy vain tarpeelliset</button>
    <button class="btn btn-outline btn-sm" data-cookie="all">Hyväksy kaikki</button>
  </div>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/main.js?v=6"></script>
</body>
</html>
'''

def page_hero(eyebrow, title, text):
    return f'''<section class="page-hero">
  <div class="container">
    <nav class="crumbs" aria-label="Murupolku"><a href="index.html">Koti</a><span>/</span><span>{eyebrow}</span></nav>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>
'''

CTA = '''<section class="cta">
  <div class="container">
    <div>
      <h2>Ensimmäinen konsultaatio on ilmainen</h2>
      <p>Noin 15 minuutin toimeksiannon selvittämistapaaminen ei maksa mitään. Soita tai jätä yhteydenottopyyntö.</p>
    </div>
    <div class="hero-actions">
      <a class="btn btn-light" href="tel:+358505598200">Soita +358 50 559 8200</a>
      <a class="btn btn-outline-light" href="yhteydenotto.html">Jätä yhteydenottopyyntö</a>
    </div>
  </div>
</section>
'''

def service(icon, title, tagline, intro, items, forums):
    service.n = getattr(service, "n", 0) + 1
    lis = "".join(f"<li>{i}</li>" for i in items)
    tags = "".join(f'<span class="tag">{f}</span>' for f in forums)
    return f'''<article class="card service reveal">
  <div class="card-top"><div class="icon">{ICON[icon]}</div><span class="card-num">0{service.n}</span></div>
  <h3>{title}</h3>
  <p class="tagline">{tagline}</p>
  <p>{intro}</p>
  <ul>{lis}</ul>
  <div class="tags">{tags}</div>
</article>'''

def course(title, desc, price, url):
    return f'''<article class="card course reveal">
  <span class="badge">Lanseeraushinta</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <div class="price"><strong>{price} €</strong><span>lokakuun loppuun 2026 saakka</span></div>
  <a class="btn btn-primary btn-sm" href="{url}">Katso ja tilaa</a>
</article>'''

# ---------- ETUSIVU ----------
index = head("Lakiasiaintoimisto", "Lakiasiantuntijat palveluksessasi: yritys-, työ-, perhe- ja vero-oikeus sekä sosiaaliturva-asiat. Joensuu ja pääkaupunkiseutu.") + header("index.html") + '''
<section class="hero" id="hero">
''' + HERO_BG + '''  <div class="container hero-grid">
    <div class="hero-copy">
      <div class="eyebrow">Lakiasiaintoimisto Virranvälke · Joensuu</div>
      <h1>Lakiasiantuntijat <em>palveluksessasi</em></h1>
      <p class="lead">Palvelemme yrityksiä ja yksityishenkilöitä työ-, yritys-, perhe- ja vero-oikeudellisissa kysymyksissä. Nykyaikainen online-virtuaalitoimisto, jossa asiat hoidetaan tehokkaasti ja luottamuksellisesti.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="yhteydenotto.html">Jätä yhteydenottopyyntö</a>
        <a class="btn btn-outline-light" href="#palvelut">Tutustu palveluihin</a>
      </div>
      <div class="hero-facts">
        <div class="fact"><strong data-count="2020" data-from="1980">2020</strong><span>Toiminta alkoi</span></div>
        <div class="fact"><strong data-count="4">4</strong><span>Osaamisaluetta</span></div>
        <div class="fact"><strong data-count="15" data-suffix=" min">15 min</strong><span>Ilmainen aloitustapaaminen</span></div>
      </div>
    </div>
    <aside class="hero-card">
      <div class="hero-card-head">
        <span class="eyebrow">Ota yhteyttä</span>
        <h3>Ensimmäinen konsultaatio on ilmainen</h3>
      </div>
      <ul class="hero-card-list">
        <li>''' + ICON["phone"] + '''<div><strong><a href="tel:+358505598200">+358 50 559 8200</a></strong><span>Ma–pe 9.00–18.00</span></div></li>
        <li>''' + ICON["mail"] + '''<div><strong><a href="mailto:ovirma@gmail.com">ovirma@gmail.com</a></strong><span>Vastaamme niin pian kuin voimme</span></div></li>
        <li>''' + ICON["video"] + '''<div><strong>Skype ja Teams</strong><span>Tapaamiset sovitaan erikseen luottamuksellisessa paikassa</span></div></li>
      </ul>
      <a class="btn btn-primary" href="yhteydenotto.html">Jätä yhteydenottopyyntö</a>
    </aside>
  </div>
</section>
''' + TRUST + '''
<section class="section" id="palvelut">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Palvelumme</div>
      <h2>Neljä osaamisaluetta, yksi yhteyshenkilö</h2>
      <p>Tapaukset selvitetään tehokkaasti ja oikeutesi suojataan. Alla pääasialliset toimialueemme ja tuomioistuimet, joissa asioita hoidamme.</p>
    </div>
    <div class="grid grid-2">
''' + service("handshake", "Yrityserimielisyydet", "Tapaukset selvitetään tehokkaasti",
              "Palvelemme yksityistämis- ja yhtiöittämiskysymyksissä.",
              ["Kunnan yhtiöittämiset", "Osakassopimukset", "Liikkeen luovutukset", "Julkiset hankinnat"],
              ["Yleinen tuomioistuin", "Markkinaoikeus"]) + service("briefcase", "Työllisyyserimielisyydet", "Työsuhdeoikeutesi suojataan",
              "Palvelemme työ- ja virkamiesoikeudellisissa kysymyksissä.",
              ["Yhteistoimintamenettelyt", "Lomautukset", "Palvelussuhteen päättämiset", "Työsopimukset", "Liikkeen luovutukset"],
              ["Yleinen tuomioistuin", "Hallinto-oikeus"]) + service("home", "Perheoikeus", "Suhteet ylläpidetään",
              "Palvelemme perheoikeudellisissa kysymyksissä.",
              ["Edunvalvonta ja edunvalvontavaltakirjat", "Perunkirjoitukset", "Testamentit", "Ositukset ja perinnönjaot"],
              ["Yleinen tuomioistuin", "Hallinto-oikeus"]) + service("scale", "Vero-oikeus ja sosiaaliturva-asiat", "Yleiset oikeudet turvataan",
              "Palvelemme vero-oikeudessa ja sosiaaliturvakysymyksissä.",
              ["Henkilö- ja yritysverotus", "Työttömyysturva-asiat", "Toimeentuloturva-asiat"],
              ["Hallinto-oikeus", "SAMU-lautakunta", "Vakuutusoikeus"]) + '''
    </div>
  </div>
</section>

<section class="section courses" id="kurssit">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Minidigikurssit</div>
      <h2>Hoida tärkeä asia kuntoon omatoimisesti</h2>
      <p>Kaikki tarpeellinen tieto edunvalvontavaltakirjan, perukirjan ja testamentin laadinnasta tiiviinä verkkokursseina. Säästä omatoimisesti paljon rahaa.</p>
    </div>
    <div class="grid grid-3">
''' + course("Edunvalvontavaltakirja: mielenrauhaa arkeen", "Kaikki tarpeellinen tieto edunvalvontavaltakirjan laadinnasta.", "59", "kurssi-edunvalvontavaltakirja.html") + course("Perukirjan laatiminen – askel askeleelta", "Kaikki tarpeellinen tieto perunkirjoituksesta.", "79", "kurssi-perukirja.html") + course("Testamenttikurssi: hoida tärkeä asia kuntoon", "Mielenrauhaa ja selkeyttä helposti. Kaikki tarpeellinen tieto testamentin laadinnasta.", "59", "kurssi-testamentti.html") + '''
    </div>
    <p class="note">Minidigikursseissa on käytetty myös tekoälysisältöjä.</p>
  </div>
</section>

<section class="section process">
  <div class="container split">
    <div class="prose reveal">
      <div class="eyebrow">Näin asiointi etenee</div>
      <h2>Selkeä polku ensimmäisestä yhteydenotosta ratkaisuun</h2>
      <ol class="steps">
        <li><span class="step-num">1</span><div><strong>Ilmainen selvittämistapaaminen</strong><p>Noin 15 minuutin keskustelu, jossa käymme asiasi läpi ja arvioimme, miten sitä kannattaa viedä eteenpäin.</p></div></li>
        <li><span class="step-num">2</span><div><strong>Sovitaan hinnoittelusta</strong><p>Tuntihinta tai palvelukohtainen kiinteä hinta, jota ei ylitetä ilman erillistä sopimista kanssasi.</p></div></li>
        <li><span class="step-num">3</span><div><strong>Asia hoidetaan</strong><p>Palaverit verkossa Skype- tai Teams-yhteyksin. Henkilökohtaiset tapaamiset sovitaan erikseen luottamuksellisessa paikassa.</p></div></li>
      </ol>
      <a class="btn btn-outline" href="tietoa-meista.html#hinnasto">Katso hinnasto</a>
    </div>
    <aside class="aside aside-dark reveal">
      <div class="aside-person">
        <img class="photo" src="assets/img/olli-virmajoki.jpg" alt="Olli Virmajoki" width="960" height="960" loading="lazy">
        <div><strong>Olli Virmajoki</strong><span>Toimitusjohtaja · Lakimies, OTM</span></div>
      </div>
      <div class="eyebrow">Tietoa meistä</div>
      <h3>Online-virtuaalitoimisto Joensuusta</h3>
      <p class="muted">Lakiasiaintoimisto Virranvälke aloitti toimintansa maaliskuussa 2020 ja palvelee asiakkaitaan täysin verkossa ilman kiinteää toimitilaa. Toiminta-alue on ensisijaisesti Joensuun seutu, tarvittaessa myös pääkaupunkiseutu.</p>
      <p class="muted">Toimintaa johtaa lakimies, OTM <strong>Olli Virmajoki</strong>. Yritys myös kokeilee ja hyödyntää tekoälyä sekä asiakaspalvelussa että lakiasiainpalvelussa.</p>
      <div class="hero-actions"><a class="btn btn-gold btn-sm" href="tietoa-meista.html">Lue lisää</a><a class="btn btn-outline-light btn-sm" href="tiimimme.html">Tiimimme</a></div>
    </aside>
  </div>
</section>
''' + CTA + FOOTER

# ---------- TIETOA MEISTÄ ----------
def price_card(title, hourly, vat_line, extra=""):
    return f'''<div class="price-card reveal">
  <h3>{title}</h3>
  <div class="big">{hourly} €<small> / tunti (alv 0 %)</small></div>
  <div class="vat">{vat_line}</div>
  {f"<p>{extra}</p>" if extra else ""}
</div>'''

about = head("Tietoa meistä", "Lakiasiaintoimisto Virranvälke on vuonna 2020 perustettu online-virtuaalitoimisto. Parasta lainopillista apua Joensuun seudulla ja pääkaupunkiseudulla.") + header("tietoa-meista.html") + page_hero("Tietoa meistä", "Parasta lainopillista apua vuodesta 2020", "Nykyaikainen, täysin online-pohjainen lakiasiaintoimisto, jonka toiminta kohdistuu erityisesti työ- ja virkamiesoikeudellisiin kysymyksiin.") + '''
<section class="section">
  <div class="container split">
    <div class="prose">
      <h2>Toimisto ilman seiniä</h2>
      <p><strong>Lakiasiaintoimisto Virranvälke</strong> aloitti toimintansa maaliskuun alussa 2020 ja sen tarkoitus on vähitellen laajentaa toimintaansa valitsemillaan päätoiminta-aloillaan. Heti pian, jo toimintansa alussa, yritys siirtyi, osin koronaepidemian takia, palvelemaan asiakkaitaan nykyaikaisena täysin puhtaana online-virtuaalitoimistona ilman kiinteää toimitilaa. Palaverit ja neuvottelut tapahtuvat jatkossakin verkossa Skype- ja Teams-yhteyksin. Kaikki henkilökohtaiset tapaamiset sovitaan erikseen luottamuksellisessa paikassa tapahtuviksi.</p>
      <p>Yrityksen toiminnassa on erityisesti myös tarkoitus kokeilla, kehittää ja hyödyntää tekoälyä sekä asiakaspalvelussa että varsinaisessa lakiasiainpalvelussa. Yrityksen ohjelmistojen käyttöehdoista pyydämme tutustumaan <a href="tietosuojaseloste.html#tietosuojarikoslauseke">tietosuojaselosteen asiakohtaan 9, Tietosuojarikoslauseke</a>.</p>
      <p>Lakiasiaintoimisto Virranvälkkeen pääasiallinen toiminta kohdistuu työ- ja virkamiesoikeudellisiin kysymyksiin. Mutta myös yritystoimintaan, perheoikeuteen, vero-oikeuteen ja työttömyys- ja sosiaaliturvan piiriin kuuluvat asiat sisältyvät toiminta-ajatukseen.</p>
      <p>Toiminta-alue on ensisijaisesti Joensuun seutu, mutta myös pääkaupunkiseudun alueella olevia asiakkaita palvellaan tarvittaessa mahdollisuuksien mukaan.</p>
    </div>
    <aside class="aside">
      <h3>Lyhyesti</h3>
      <dl>
        <dt>Perustettu</dt><dd>Maaliskuu 2020</dd>
        <dt>Toimitusjohtaja</dt><dd><a class="dd-person" href="tiimimme.html"><img class="photo photo-xs" src="assets/img/olli-virmajoki.jpg" alt="" width="960" height="960" loading="lazy">Olli Virmajoki</a></dd>
        <dt>Toimintatapa</dt><dd>Online-virtuaalitoimisto, ei kiinteää toimitilaa</dd>
        <dt>Palaverit</dt><dd>Skype ja Teams, tapaamiset sopimuksen mukaan</dd>
        <dt>Toiminta-alue</dt><dd>Joensuun seutu, tarvittaessa pääkaupunkiseutu</dd>
        <dt>Y-tunnus</dt><dd>3192420-6</dd>
      </dl>
    </aside>
  </div>
</section>

<section class="section" style="padding-top:0" id="hinnasto">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Laskutushintamme</div>
      <h2>Selkeä hinnoittelu</h2>
      <p>Ensimmäinen noin 15 minuuttia kestävä toimeksiannon selvittämistapaaminen on ilmainen.</p>
    </div>
    <div class="pricing">
''' + price_card("Yksityisasiakkaat", "200", "200,00 € / tunti + alv 24 % = 248,00 € / tunti") + price_card("Yritysasiakkaat", "230", "230,00 € / tunti + alv 24 % = 285,20 € / tunti") + price_card("Konsultointi", "150", "150,00 € / tunti + alv 24 % = 186,00 € / tunti", "Myös sovittelu.") + '''
    </div>
    <div class="pricing-extra">
      <div class="callout">
        <strong>Vaikeat toimeksiannot ja hankalissa olosuhteissa tehty työ: + 10 %</strong>
        <p>Laskutushintoja voidaan korottaa 10 % perushinnoista.</p>
      </div>
      <div class="callout">
        <strong>Palvelukohtainen hinnoittelu</strong>
        <p>Voidaan sopia myös palvelukohtainen kiinteä hinnoittelu, jota ei ylitetä ilman asiakkaan kanssa sopimista. Esimerkkihintoja alkaen: testamentti 250 €, edunvalvontavaltakirja 250 €, perunkirjoitus 500 € ja ositus 700 €.</p>
      </div>
    </div>
  </div>
</section>
''' + CTA + FOOTER

# ---------- TIIMIMME ----------
team = head("Tiimimme", "Olemme sitoutuneet auttamaan sinua. Tutustu Lakiasiaintoimisto Virranvälkkeen tiimiin.") + header("tiimimme.html") + page_hero("Tiimimme", "Olemme sitoutuneet auttamaan sinua", "Kokenut lakimies ja kasvava tiimi. Etsimme joukkoomme uusia osaajia.") + '''
<section class="section">
  <div class="container">
    <article class="card person featured reveal">
      <div class="featured-side">
        <img class="photo photo-lg" src="assets/img/olli-virmajoki.jpg" alt="Olli Virmajoki" width="960" height="960" loading="lazy">
        <h3>Olli Virmajoki</h3>
        <p class="role">Toimitusjohtaja · Lakimies, OTM</p>
        <div class="tags">
          <span class="tag">Asianajaja-tutkinto 2019</span><span class="tag">DI</span><span class="tag">FL</span><span class="tag">FT</span><span class="tag">HTK</span><span class="tag">Opettajan ammatillinen tutkinto</span>
        </div>
      </div>
      <div class="featured-body">
        <p>Olli on yrityksen perustajajäsen. Lakimies, OTM ja asianajaja-tutkinto vuonna 2019.</p>
        <p>Hänellä on laaja ja monipuolinen koulutus: DI, opettajan ammatillinen tutkinto, FL, FT ja HTK.</p>
        <p>Ollilla on monipuolinen työkokemus kattaen yritysmaailman, kunnallishallinnon sekä myös koulutussektorin, joissa hän on perehtynyt laajasti myös työelämän ongelmiin.</p>
        <div class="hero-actions"><a class="btn btn-primary btn-sm" href="http://cvapp.fi/r/H6uUn2Vmu" target="_blank" rel="noopener">Katso CV</a><a class="btn btn-outline btn-sm" href="yhteydenotto.html">Ota yhteyttä</a></div>
      </div>
    </article>
    <div class="section-head" style="margin-top:56px">
      <div class="eyebrow">Avoimet paikat</div>
      <h2>Etsimme tiimiimme uusia osaajia</h2>
    </div>
    <div class="grid grid-2">
      <article class="card person reveal">
        <div class="avatar open" aria-hidden="true">?</div>
        <span class="open-badge">Avoin paikka</span>
        <h3>Hanna Eskola</h3>
        <p class="role">Lakimies</p>
        <p>Etsimme tiimiimme uutta ”Hannaa”.</p>
        <div class="tags"><a class="btn btn-outline btn-sm" href="yhteydenotto.html">Ota yhteyttä</a></div>
      </article>
      <article class="card person reveal">
        <div class="avatar open" aria-hidden="true">?</div>
        <span class="open-badge">Avoin paikka</span>
        <h3>Petri Korhonen</h3>
        <p class="role">Lakimies</p>
        <p>Etsimme tiimiimme uutta ”Petriä”.</p>
        <div class="tags"><a class="btn btn-outline btn-sm" href="yhteydenotto.html">Ota yhteyttä</a></div>
      </article>
    </div>
  </div>
</section>
''' + CTA + FOOTER

# ---------- YHTEYDENOTTO ----------
def info(icon, title, body):
    return f'''<div class="info"><div class="icon">{ICON[icon]}</div><div><strong>{title}</strong><p>{body}</p></div></div>'''

contact = head("Ota yhteyttä", "Ensimmäinen konsultaatio on ilmainen. Ota yhteyttä Lakiasiaintoimisto Virranvälkkeeseen puhelimitse, sähköpostilla tai lomakkeella.") + header("yhteydenotto.html") + page_hero("Yhteydenotto", "Ota yhteyttä", "Ensimmäinen konsultaatio on ilmainen. Jätä yhteystietosi, niin otamme sinuun yhteyttä niin pian kuin voimme.") + '''
<section class="section">
  <div class="container contact-grid">
    <div class="info-list">
''' + info("pin", "Postiosoite", "Lakiasiaintoimisto Virranvälke<br>Torikatu 3 B 12, 80110 Joensuu") + info("video", "Tapaamiset", "Palvelemme sinua nykyaikaisena täysin puhtaana online-virtuaalitoimistona ilman kiinteää toimitilaa. Palaverit ja neuvottelut tapahtuvat verkossa Skype- ja Teams-yhteyksin. Kaikki tapaamiset sovitaan erikseen luottamuksellisessa paikassa tapahtuviksi.") + info("clock", "Aukioloajat", "Maanantai – perjantai 9.00 – 18.00") + info("phone", "Puhelin", '<a href="tel:+358505598200">+358 50 559 8200</a><br><span class="muted">+358 xxxxx xxxx (maksullinen puhelinneuvonta 4,00 € / minuutti)</span>') + info("mail", "Sähköposti", '<a href="mailto:ovirma@gmail.com">ovirma@gmail.com</a>') + '''
    </div>
    <form class="form reveal" id="contact-form" novalidate>
      <h3>Jätä yhteydenottopyyntö</h3>
      <p class="hint">Ole hyvä ja jätä yhteystietosi niin otamme sinuun yhteyttä niin pian kuin voimme. (*) pakollinen kenttä.</p>
      <div class="field">
        <label for="f-name">Nimi (*)</label>
        <input id="f-name" name="name" type="text" required autocomplete="name">
      </div>
      <div class="fields-2">
        <div class="field">
          <label for="f-email">Sähköposti (*)</label>
          <input id="f-email" name="email" type="email" required autocomplete="email">
        </div>
        <div class="field">
          <label for="f-phone">Puhelin (*)</label>
          <input id="f-phone" name="phone" type="tel" required autocomplete="tel">
        </div>
      </div>
      <div class="field">
        <label for="f-interest">Olen kiinnostunut (*)</label>
        <select id="f-interest" name="interest" required>
          <option value="">Valitse…</option>
          <option>Konsultaatio</option>
          <option>Oikeudellinen palvelu</option>
          <option>Sovittelu</option>
          <option>Muu vaihtoehto</option>
        </select>
      </div>
      <div class="field">
        <label for="f-msg">Kerro asiasi lyhyesti</label>
        <textarea id="f-msg" name="message"></textarea>
      </div>
      <button class="btn btn-primary" type="submit">Lähetä</button>
      <p class="form-demo">Demo: lomake ei vielä lähetä viestiä mihinkään.</p>
    </form>
  </div>
</section>
''' + FOOTER

# ---------- TIETOSUOJASELOSTE ----------
privacy = head("Tietosuojaseloste", "Lakiasiaintoimisto Virranvälkkeen tietosuojaseloste.") + header("tietosuojaseloste.html") + page_hero("Tietosuoja", "Tietosuojaseloste", "Tämä tietosuojaseloste kertoo, kuinka Lakiasiaintoimisto Virranvälke kerää, käsittelee ja luovuttaa henkilötietoja lakiasiaintoimeksiannon hoitamisen ja siihen liittyvien lakisääteisten velvoitteiden täyttämisen ja markkinoinnin yhteydessä.") + '''
<section class="section">
  <div class="container legal">
    <h2>1. Rekisterinpitäjä</h2>
    <address>Lakiasiaintoimisto Virranvälke<br>Osoite: Huhtilammentie 401a, 82180 Huhtilampi (Joensuu)<br>Puhelin: <a href="tel:+358505598200">+358 50 559 8200</a><br>Sähköposti: <a href="mailto:ovirma@gmail.com">ovirma@gmail.com</a><br>Y-tunnus: 3192420-6</address>

    <h2>2. Henkilötietojen käsittelyn tarkoitus</h2>
    <p>Lakiasiaintoimeksiannon hoitaminen ja siihen liittyvien lakisääteisten velvoitteiden täyttäminen. Rekisteröidyn suostumuksen perusteella hänen yhteystietojaan voidaan käyttää myös markkinointia varten.</p>

    <h2>3. Käsittelyn oikeusperusteet</h2>
    <p>Lakiasiaintoimeksiantosopimus, lakiasiaintoimintaan liittyvät lakisääteiset velvoitteet ja rekisteröidyn antama suostumus. Annettu suostumus voidaan peruuttaa milloin tahansa eikä tietoja käytetä enää tämän jälkeen markkinointiin.</p>

    <h2>4. Henkilötietojen vastaanottajat</h2>
    <p>Henkilötietoja käytetään pääasiassa pelkästään toimiston sisäisesti. Mikäli toimeksiannon luonne sitä edellyttää, henkilötietoja saatetaan kuitenkin toimittaa vastapuolelle, tuomioistuimelle tai muulle viranomaiselle. Henkilötietoja ei toimiteta kolmanteen maahan tai kansainväliselle järjestölle.</p>

    <h2>5. Henkilötietojen säilytysaika</h2>
    <p>Henkilötietoja säilytetään toimeksiannon voimassaoloajan, kuitenkin vähintään 10 vuotta. Asianajajan esteellisyyden selvittämiseksi tarpeelliset tiedot säilytetään pysyvästi.</p>

    <h2>6. Rekisteröidyn oikeudet</h2>
    <p>Rekisteröidyllä on oikeus tutustua omiin henkilötietoihinsa ja pyytää kyseisten tietojen oikaisemista sekä niiden poistamista, mikäli tietojen käsittelemiseen ei ole enää hyväksyttävää syytä. Tietyin edellytyksin rekisteröity voi myös pyytää henkilötietojen käsittelyn rajoittamista tai vastustaa niiden käsittelyä. Edellä kerrotusta huolimatta tietoja voidaan edelleen käsitellä lakisääteisten velvoitteiden toteuttamiseksi. Rekisteröidyllä on oikeus tehdä valitus tietosuojavaltuutetulle, mikäli hän katsoo, että hänen henkilötietojensa käsittelyssä on rikottu tietosuojalainsäädäntöä. Löydät tietosuojavaltuutetun yhteystiedot tietosuojavaltuutetun verkkosivuilta: <a href="https://www.tietosuoja.fi/etusivu/" target="_blank" rel="noopener">tietosuoja.fi</a>.</p>

    <h2>7. Henkilötietojen toimittamatta jättäminen</h2>
    <p>Henkilötiedot ovat tarpeen toimeksiannon hoitamiseksi lakimiestä velvoittavien säännösten mukaisesti. Toimeksiantoa ei voida vastaanottaa tai siitä voidaan joutua luopumaan, mikäli riittäviä henkilötietoja ei toimiteta tai niiden käsittelyä rajoitetaan tai vastustetaan tavalla, joka estää toimeksiannon hoitamisen.</p>

    <h2>8. Automaattinen päätöksenteko</h2>
    <p>Henkilötietoja ei käytetä profiloinnissa tai muussa automatisoidussa päätöksenteossa.</p>

    <h2 id="tietosuojarikoslauseke">9. Tietosuojarikoslauseke</h2>
    <p>Yrityksen ohjelmistot ovat tarkoitettu vain tavanomaiseen käyttöön verkkoselaimella. Tämä tarkoittaa asiointia Lakiasiaintoimisto Virranvälkkeen lakipalveluja saavana asiakkaana.</p>
    <p>Yrityksen ohjelmistojen kaikenlainen luvaton ja asiaton käyttö on tietoturvarikoslainsäädännön alaista toimintaa ja tällaista tekoa tullaan arvioimaan tietoturvarikoksena.</p>
    <p>Kiellettyä on siten ohjelmistojen hakkerointi, tietojärjestelmäkoodeihin tunkeutuminen, koodien kaappaaminen, kopioiminen ja niiden julkinen esittäminen.</p>
    <p>Ohjelmistot ovat myös kaikilta oikeuksiltaan tekijänoikeuslainsäädännön mukaisesti suojattuja.</p>
  </div>
</section>
''' + FOOTER

# ---------- KÄYTTÖEHDOT ----------
terms = head("Käyttöehdot", "Lakiasiaintoimisto Virranvälkkeen käyttöehdot.") + header("kayttoehdot.html") + page_hero("Ehdot", "Käyttöehdot", "Sivuston käyttöehdot.") + '''
<section class="section">
  <div class="container legal">
    <div class="disclaimer"><p><strong>Huomio:</strong> alkuperäisellä sivustolla tämä sivu sisältää vielä sivustotyökalun mallitekstin. Teksti on kopioitu sellaisenaan ja odottaa varsinaisia käyttöehtoja.</p></div>
    <p>Vastuuvapauslauseke: Verkkokaupan omistajana sinun tulisi julkaista sivustosi Käyttöehdot. Asiakirjassa olisi määriteltävä sinun ja asiakkaasi välinen suhde ja selittää hyvitys- ja peruutusehdot. Verkosta on löydettävissä valmiita esimerkkejä ja malleja Käyttöehtoja varten, voit etsiä hakusanoilla ”Käyttöehdot generaattori”. Joka tapauksessa, suosittelemme vahvasti pyytämään oikeudellisia neuvoja ja muokkaamaan mallia yrityksesi tarpeisiin.</p>
  </div>
</section>
''' + FOOTER

# ---------- TIETOSUOJAKÄYTÄNTÖ ----------
policy = head("Tietosuojakäytäntö", "Lakiasiaintoimisto Virranvälkkeen tietosuojakäytäntö.") + header("tietosuojakaytanto.html") + page_hero("Tietosuoja", "Tietosuojakäytäntö", "Henkilötietojen käsittelyn yleiset säännöt.") + '''
<section class="section">
  <div class="container legal">
    <div class="disclaimer"><p><strong>Huomio:</strong> alkuperäisellä sivustolla tämä sivu sisältää sivustotyökalun mallitekstin, jossa on täyttämättömiä kohtia [….]. Teksti on kopioitu sellaisenaan. Varsinainen tietosuojaseloste on <a href="tietosuojaseloste.html">omalla sivullaan</a>.</p></div>
    <p>Vastuuvapauslauseke: Tämä asiakirja luotiin malliksi vain tiedotustarkoituksiin. Käyttämällä sitä hyväksyt tämän vastuuvapauslausekkeen ja otat huomioon että Webnode ei ole vastuussa toimenpiteistä tai sisällöstä jota tällä kotisivulla on. Suosittelemme, että käytät lainopillista apua ja muokkaat tästä asiakirjasta sellaisen, että se sopii yrityksesi tarpeisiin.</p>
    <p>Verkkokauppa [….] kotisivulla [….] Y-tunnus […] paikassa […] käsittelee asiakkaan toimittamia henkilötietoja, jotka täyttävät ja vahvistavat käyttöehtojen, sähköisten tilausten ja toimitusten käsittelyn sekä tarvittavan tiedonvälityksen lain edellyttämän ajan kuluessa.</p>

    <h2>Yleiset säännökset</h2>
    <ol>
      <li>Henkilötietojen rekisterinpitäjä, joka noudattaa GDPR-asetusta (jäljempänä ”asetus”) on [….], Y-tunnus [….], paikassa [….] (jäljempänä ”Rekisterinpitäjä”);</li>
      <li>Rekisterinpitäjän yhteystiedot ovat: sähköposti: [……], puh.: [………];</li>
      <li>Henkilötietoja ovat kaikki tiedot, jotka liittyvät tunnistettuun tai tunnistettavissa olevaan luonnolliseen henkilöön.</li>
    </ol>

    <h2>Henkilötietojen lähde</h2>
    <ol>
      <li>Rekisterinpitäjä käsittelee asiakkaan suostumuksella saamiaan henkilötietoja, jotka on kerätty sopimuksella verkkokaupan sähköisen tilauksen hankkimiseksi ja täyttämiseksi [….];</li>
      <li>Rekisterinpitäjä käsittelee vain asiakkaan tunnistetiedot ja yhteystiedot, jotka ovat välttämättömiä ostosopimuksen täyttämiseksi;</li>
      <li>Rekisterinpitäjä käsittelee henkilötietoja lähetys- ja kirjanpitotarkoituksiin sekä sopimuspuolten tarvittavan tiedon välittämiseen lain edellyttämän ajan verran. Henkilötietoja ei julkisteta eikä niitä siirretä muihin maihin.</li>
    </ol>

    <h2>Tietojenkäsittelyn tarkoitus</h2>
    <p>Rekisterinpitäjä käsittelee Asiakkaan henkilötietoja seuraavissa tarkoituksissa:</p>
    <ol>
      <li>Kotisivun rekisteröinti [….] GDPR:n luvun 4 jakson 2 mukaisesti;</li>
      <li>Asiakkaan luoma sähköinen tilaus (nimi, osoite, sähköposti, puhelinnumero);</li>
      <li>Noudattaa Asiakkaan ja Rekisterinpitäjän välisestä sopimussuhteesta johtuvaa lakia ja määräyksiä;</li>
      <li>Henkilötiedot ovat välttämättömiä ostosopimuksen täyttämiseksi. Sopimusta ei voida tehdä ilman henkilökohtaisia tietoja.</li>
    </ol>

    <h2>Henkilötietojen tallennuksen kesto</h2>
    <ol>
      <li>Rekisterinpitäjä tallentaa henkilötietoja niin kauan kuin on tarpeen Rekisterinpitäjän ja Asiakkaan välisestä sopimussuhteesta johtuvien oikeuksien ja velvoitteiden täyttämiseksi ja kolmen vuoden ajan sopimussuhteen päättymisen jälkeen;</li>
      <li>Rekisterinpitäjän on poistettava kaikki henkilökohtaiset tiedot henkilötietojen säilyttämiseen tarvittavan ajan kuluttua.</li>
    </ol>

    <h2>Henkilötietojen vastaanottajat ja käsittelijät</h2>
    <p>Asiakkaan henkilötietoja käsittelevät kolmannet osapuolet ovat Rekisterinpitäjän alihankkijoita. Näiden alihankkijoiden palvelut ovat välttämättömiä, jotta sopimus sähköisen tilauksen hankkimisesta ja käsittelystä Rekisterinpitäjän ja Asiakkaan välisessä sopimuksessa voidaan toteuttaa.</p>
    <p>Rekisterinpitäjän alihankkijoita ovat:</p>
    <ul>
      <li>Webnode AG (verkkokauppajärjestelmä);</li>
      <li>Rahtiyhtiö;</li>
      <li>Google Analytics (kotisivun analytiikka);</li>
    </ul>

    <h2>Asiakkaan oikeudet</h2>
    <p>Asetuksen mukaisesti Asiakkaalla on oikeus:</p>
    <ol>
      <li>oikeus tutustua henkilötietoihin;</li>
      <li>oikeus henkilötietojen oikaisuun;</li>
      <li>oikeus henkilötietojen poistamiseen;</li>
      <li>oikeus vastustaa henkilötietojen käsittelyä;</li>
      <li>oikeus tietojen siirrettävyyteen;</li>
      <li>oikeus peruuttaa suostumuksensa henkilötietojen käsittelyyn kirjallisesti tai sähköpostitse osoitteeseen: [….];</li>
      <li>oikeus esittää valitus valvontaviranomaiselle, jos epäillään Asetuksen rikkomista.</li>
    </ol>

    <h2>Henkilötietojen turvallisuus</h2>
    <ol>
      <li>Rekisterinpitäjä sitoutuu toteuttamaan kaikki tekniset ja organisatoriset varotoimet, jotka ovat tarpeen henkilötietojen suojaamiseksi.</li>
      <li>Rekisterinpitäjä on tehnyt teknisiä varotoimenpiteitä tietojen tallennustilojen turvaamiseksi, erityisesti varmistanut pääsyn tietokoneelle salasanan avulla, käyttänyt virustentorjuntaohjelmistoa ja ylläpitänyt tietokoneita säännöllisesti.</li>
    </ol>

    <h2>Loppusäännökset</h2>
    <ol>
      <li>Tekemällä sähköisen tilauksen verkkosivustolla [….] Asiakas vakuuttaa olevansa tietoinen kaikista henkilötietosuojaehdoista ja hyväksyy ne täysimittaisesti;</li>
      <li>Asiakas hyväksyy nämä säännöt valitsemalla valintaruudun tilauskaavakkeessa;</li>
      <li>Rekisterinpitäjä voi päivittää nämä Säännöt milloin tahansa. Uusi, päivitetty versio on julkaistava tällä verkkosivulla.</li>
    </ol>
    <p>Nämä säännöt tulevat voimaan [päivämäärä].</p>
  </div>
</section>
''' + FOOTER

# ---------- MINIDIGIKURSSIT ----------
def course_page(c):
    includes = "".join(
        f'<li><span class="inc-icon">{ICON[i]}</span><div><strong>{t}</strong><p>{d}</p></div></li>'
        for i, t, d in c["includes"]
    )
    intro = "".join(f"<p>{p}</p>" for p in c["intro"])
    author = "".join(f"<p>{p}</p>" for p in c["author"])
    why = "".join(f"<p>{p}</p>" for p in c["why"])
    outcomes = "".join(f"<li>{o}</li>" for o in c["outcomes"])
    return head(c["title"], c["hook"]) + header("index.html#kurssit") + page_hero("Minidigikurssit", c["title"], c["hook"]) + f'''
<section class="section">
  <div class="container course-layout">
    <div class="course-body">
      <div class="prose">
        {intro}
      </div>

      <div class="author-box reveal">
        <img class="photo" src="assets/img/olli-virmajoki.jpg" alt="Olli Virmajoki" width="960" height="960" loading="lazy">
        <div>
          <div class="eyebrow">Kurssin tekijä</div>
          <h3>Olli Virmajoki, OTM</h3>
          {author}
        </div>
      </div>

      <h2>Mitä saat?</h2>
      <p class="lead">{c["includes_lead"]}</p>
      <ul class="includes reveal">{includes}</ul>

      <div class="outcome-box reveal">
        <h3>Kun olet käynyt materiaalin läpi, sinulla on</h3>
        <ul>{outcomes}</ul>
      </div>

      <h2>Miksi tämä toimii?</h2>
      <div class="prose">{why}</div>

      <div class="guarantee reveal">
        <span class="inc-icon">{ICON["shield"]}</span>
        <div>
          <h3>14 päivän Mielenrauha-takuu</h3>
          <p>{c["guarantee"]}</p>
          <p class="muted">Kurssi on käytettävissä 100 vuorokautta kurssille kirjautumisesta lukien, joten sisällön voi käydä läpi kaikessa rauhassa ja siihen voi palata myöhemmin uudestaan.</p>
        </div>
      </div>
    </div>

    <aside class="order-card reveal" id="order">
      <div class="order-head">
        <span class="badge">Lanseeraushinta</span>
        <h3>{c["title"]}</h3>
        <div class="price-row">
          <strong>{c["price"]},00 €</strong>
          <s>{c["normal"]},00 €</s>
        </div>
        <p class="muted">sis. alv 25,5 % · lanseeraushinta voimassa lokakuun 2026 loppuun</p>
      </div>
      <form class="order-form" id="order-form" novalidate>
        <div class="fields-2">
          <div class="field"><label for="o-first">Etunimi *</label><input id="o-first" name="first" type="text" required autocomplete="given-name"></div>
          <div class="field"><label for="o-last">Sukunimi *</label><input id="o-last" name="last" type="text" required autocomplete="family-name"></div>
        </div>
        <div class="field"><label for="o-email">Sähköpostiosoite *</label><input id="o-email" name="email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="o-email2">Vahvista sähköpostiosoite *</label><input id="o-email2" name="email2" type="email" required autocomplete="email"></div>
        <label class="check"><input type="checkbox" required><span>Olen lukenut ja hyväksyn <a href="kayttoehdot.html">käyttöehdot</a> sekä <a href="tietosuojaseloste.html">tietosuojaselosteen</a>. *</span></label>
        <button class="btn btn-gold" type="submit">Jatka maksuun</button>
        <p class="form-demo">Demo: tilausta ei käsitellä eikä maksua veloiteta. Oikea tilaus tehdään toistaiseksi <a href="{c["campwire"]}" target="_blank" rel="noopener">Campwiren kaupassa</a>.</p>
        <p class="pay-note">{ICON["shield"]} Kortti-, mobiili-, verkkopankki-, lasku- ja osamaksu</p>
      </form>
      <div class="order-done" id="order-done" hidden>
        <span class="inc-icon">{ICON["check"]}</span>
        <h3>Kiitos tilauksestasi! (demo)</h3>
        <p>Oikeassa versiossa siirtyisit nyt maksuvaiheeseen ja saisit kurssin kirjautumistiedot sähköpostiisi osoitteeseen <strong id="order-email"></strong>.</p>
        <p class="muted">Tämä on esittelyversio: mitään ei lähetetty eikä veloitettu.</p>
        <button class="btn btn-outline btn-sm" type="button" data-order-reset>Palaa lomakkeeseen</button>
      </div>
    </aside>
  </div>
</section>
''' + FOOTER

COURSES = [
  dict(
    slug="kurssi-edunvalvontavaltakirja.html",
    title="Edunvalvontavaltakirja: mielenrauhaa arkeen",
    hook="Tee edunvalvontavaltakirja nyt – ja elä eläkepäiväsi mielenrauhassa tietäen, että asiasi ovat turvassa.",
    price=59, normal=79,
    campwire="https://lakitstoviva.campwire.com/checkout/edunvalvontavaltakirja-mielenrauhaa-arkeen-1237f954",
    intro=[
      "Moni eläkkeelle jäävä miettii, mitä tapahtuu sitten, jos oma toimintakyky heikkenee eikä enää itse pysty hoitamaan asioitaan. Jos mitään ei ole etukäteen sovittu, läheiset joutuvat selvittämään asioita viranomaisten kautta, usein aikaa vievästi ja raskaasti.",
      "Monet lykkäävät edunvalvontavaltakirjan tekemistä, koska kuvittelevat sen olevan vaikeaa, kallista tai vain juristien tehtävä. Tämä ei pidä paikkaansa. On olemassa selkeä, helppo ja edullinen tapa tehdä edunvalvontavaltakirja itse – oikein ja turvallisesti.",
      "<strong>Kuvittele hetki elämää, jossa tämä asia on jo hoidettu.</strong> Sinulla on asiakirja, joka turvaa sinun ja läheistesi tulevaisuuden. Et enää murehdi ”mitä jos” -tilanteita. Se tunne on mielenrauha.",
    ],
    author=[
      "Olen Olli Virmajoki, oikeustieteen maisteri ja lupalakimies. Työssäni olen huomannut, että ihmiset lykkäävät edunvalvontavaltakirjan tekemistä, vaikka tietävät sen olevan tärkeää. Juridiikka tuntuu vaikealta, ohjeet ovat epäselviä ja lopulta asia jää tekemättä.",
      "Siksi olen tehnyt tästä aiheesta oppaan, mallipohjan ja tarkistuslistan, jotka ohjaavat sinut vaihe vaiheelta niin, että voit itse laatia edunvalvontavaltakirjasi turvallisesti ja luottavaisin mielin.",
    ],
    includes_lead="Tämä ei ole vain opas, vaan kokonaisuus, joka vie sinut epävarmuudesta mielenrauhaan vaihe vaiheelta.",
    includes=[
      ("book", "Selkeä, ladattava opas", "Yksinkertainen ja ymmärrettävä selitys siitä, mikä edunvalvontavaltakirja on ja miksi se on tärkeä. Ei vaikeaa juristikieltä, vaan käytännönläheistä ohjeistusta."),
      ("doc", "Mallipohja valmiiksi täytettäväksi", "Seuraa ohjeita ja täytä oma valtakirjasi. Varmistat, että asiakirjasi on lainvoimainen ja oikein laadittu."),
      ("check", "Tarkistuslista", "Käy kohta kohdalta läpi ja varmista, että mikään ei jää huomaamatta."),
      ("play", "Video- tai audio-ohjeet", "Käytännönläheiset ohjeet, joita voit kuunnella tai katsella omaan tahtiisi – kuin asiantuntija olisi rinnallasi."),
    ],
    outcomes=["valmiiksi laadittu edunvalvontavaltakirja", "tieto ja ymmärrys sen merkityksestä", "rauhallinen mieli, kun tiedät, että asiasi ovat järjestyksessä"],
    why=[
      "Ilman edunvalvontavaltakirjaa läheisesi joutuvat hakemaan edunvalvojan käräjäoikeuden kautta. Prosessi voi kestää kuukausia ja aiheuttaa sekä vaivaa että ylimääräisiä kustannuksia. Oikein laadittu edunvalvontavaltakirja varmistaa, että juuri sinä päätät, kuka hoitaa asioitasi ja miten.",
      "Paketti perustuu vuosien asiantuntemukseen juridisista asiakirjoista ja käytännön kokemukseen siitä, mitkä kohdat aiheuttavat ihmisille eniten epävarmuutta. Se purkaa vaikeat asiat ymmärrettäviksi ja varmistaa, että lopputulos on turvallinen.",
    ],
    guarantee="Jos et koe tämän paketin auttavan sinua edunvalvontavaltakirjan laatimisessa 14 päivän sisällä, saat veloituksetta puolen tunnin henkilökohtaisen lisäneuvonnan (arvo yli 100 €).",
  ),
  dict(
    slug="kurssi-perukirja.html",
    title="Perukirjan laatiminen – askel askeleelta",
    hook="Perukirjan laatiminen ei tarvitse olla painajainen, vaan selkeä, hallittava prosessi.",
    price=79, normal=99,
    campwire="https://lakitstoviva.campwire.com/checkout/perukirjan-laatiminen-askel-askeleelta-3d7a720c",
    intro=[
      "Kun läheinen on menehtynyt, surun keskellä viimeinen asia, jonka haluaisit kohdata, on epävarmuus ja kaaos perukirjan kanssa. Silti juuri siinä tilanteessa monet joutuvat ensimmäistä kertaa tekemään tämän vaativan asiakirjan – yksin, ilman kokemusta ja peläten, että jokin tärkeä unohtuu.",
      "Perukirja on mahdollista laatia itse oikein ja huolellisesti, mutta vain, jos käytössäsi on selkeä reitti, joka vie sinut vaihe vaiheelta alusta loppuun ilman arvailuja.",
      "<strong>Kuvittele tilanne, jossa</strong> tiedät tarkalleen, mitä tehdä ja missä järjestyksessä, voit luottaa siihen, ettei mikään tärkeä jää huomaamatta, ja saat rauhaa ja aikaa käsitellä surua sen sijaan, että hukut byrokratian pyörteisiin.",
    ],
    author=[
      "Minäkin olen ollut tilanteessa, jossa perukirjan laatiminen osui keskelle suurta surua. Muistan yhä, kuinka epävarma olo oli: mistä aloittaa, mitä asiakirjoja tarvitaan ja mitä kaikkea laki vaatii.",
      "Lakimiehenä löysin lopulta järjestelmällisen tavan tehdä asiat oikein. Olen paketoinut ratkaisun selkeäksi oppaaksi, jotta sinä voit säästää hermojasi, saada varmuuden oikeista askelista ja ennen kaikkea aikaa surulle.",
    ],
    includes_lead="Opas vie sinut kuudessa vaiheessa pisteestä A (täysin epätietoinen, mistä edes aloittaa) pisteeseen B (valmis perukirja, jonka voit toimittaa viranomaisille luottavaisin mielin).",
    includes=[
      ("list", "Kuuden vaiheen muutosmatka", "Aloitus ja valmistelut, pesän osakkaiden selvittäminen, varojen ja velkojen kartoittaminen, perunkirjoitustilaisuuden järjestäminen, perukirjan laatiminen sekä toimittaminen verottajalle."),
      ("book", "PDF-tekstiopas", "Luettavissa läppäriltä tai tulostettavissa."),
      ("play", "Videot", "Käyn asiat läpi rauhallisesti ja käytännönläheisesti."),
      ("doc", "Mallipohjat", "Täyttäminen on helppoa valmiiden pohjien avulla."),
      ("check", "Tarkistuslistat", "Varmistat, että kaikki asiat on tehty oikeassa järjestyksessä."),
    ],
    outcomes=["valmis perukirja, jonka voit toimittaa viranomaisille", "vältät yleisimmät virheet, jotka aiheuttavat lisäselvityksiä ja viivästyksiä", "säästät rahaa, kun sinun ei tarvitse heti turvautua kalliiseen asiantuntijaan"],
    why=[
      "<strong>Asiantuntijuus:</strong> oppaan on koonnut Olli Virmajoki, OTM, luvan saanut oikeudenkäyntiavustaja, joka on auttanut lukuisia ihmisiä perintöoikeudellisissa asioissa. <strong>Käytännön kokemus:</strong> olen itsekin joutunut laatimaan perukirjan omassa perheessäni.",
      "<strong>Selkeä menetelmä:</strong> kuuden vaiheen rakenne varmistaa, ettei mitään tärkeää jää välistä ja että asiat etenevät loogisesti alusta loppuun. Sama prosessi on auttanut monia ensikertalaisia laatimaan perukirjan onnistuneesti ilman turhaa stressiä.",
    ],
    guarantee="Jos huomaat oppaan käytön jälkeen, ettei se sovikaan sinulle tai et koe saavasi siitä apua, lähetä viesti 14 päivän sisällä ostosta, niin saat henkilökohtaista neuvontaa puoli tuntia maksutta (arvo yli 100 €).",
  ),
  dict(
    slug="kurssi-testamentti.html",
    title="Testamenttikurssi: hoida tärkeä asia kuntoon",
    hook="Tee tärkein paperi elämässäsi selkeästi ja varmasti – saat mielenrauhan, kun oma tahto on turvattu.",
    price=59, normal=79,
    campwire="https://lakitstoviva.campwire.com/checkout/testamenttikurssi-hoida-tarkea-asia-kuntoon-mielenrauhaa-ja-selkeytta-8a8e5426",
    intro=[
      "Olet ehkä miettinyt testamenttia jo pitkään. Ehkä olet avannut muutaman mallipohjan netistä, mutta sulkenut selaimen turhautuneena. Mitä pidempään lykkää päätöstä, sitä enemmän epävarmuus painaa mieltä: miten käy mökille, säästöille tai tavaroille, kun minua ei enää ole?",
      "Moni yrittää selvittää kaiken itse tai käyttää vanhentunutta mallia, joka ei enää ole lainvoimainen. Toiset maksavat satoja euroja juristille, vaikka haluaisivat vain yksinkertaisen ja selkeän testamentin.",
      "<strong>Entä jos sen voisi tehdä helposti, varmasti ja rauhassa</strong> – askel askeleelta, ilman monimutkaista juristikieltä? Paperi on valmis, allekirjoitettu ja tallessa. Tiedät, että oma tahto on turvattu ja läheisesi saavat selkeät ohjeet.",
    ],
    author=[
      "Olen Olli Virmajoki, oikeustieteen maisteri ja luvan saanut oikeudenkäyntiavustaja. Työssäni olen nähnyt, miten paljon epäselvyydet testamentissa voivat aiheuttaa surua, ristiriitoja ja pitkiä prosesseja, vaikka kaikki olisi voitu välttää selkeällä ennakkosuunnittelulla.",
      "Haluan auttaa tavallisia ihmisiä hoitamaan tärkeän asian kuntoon ilman juristikieltä, stressiä ja kalliita laskuja. Jokaisella on oikeus selkeyteen ja mielenrauhaan.",
    ],
    includes_lead="Kurssi vie sinut selkeän ja varman testamentin laatimiseen askel askeleelta, ilman lakikoulutusta tai turhaa byrokratiaa. Etenet omassa tahdissasi.",
    includes=[
      ("book", "Johdanto: mitä testamentti oikeasti tekee", "Selkeä selitys eri testamenttilajeista ja niiden merkityksistä."),
      ("list", "Askel askeleelta -ohjeistus", "Kurssin ydin: etenet luonnostelusta valmiiseen testamenttiin. Mukana täytettävä testamenttipohja (PDF/Word)."),
      ("check", "Muistilista ja tarkistuslista", "Tulostettavat listat varmistavat, että yksikään tärkeä kohta ei jää huomaamatta."),
      ("doc", "Käytännön esimerkit ja erityistilanteet", "Avio- ja avoparit, mökki, sijoitusasunto, uusperhe, lapsettomuus ja muut elämäntilanteet."),
      ("chat", "Tuki ja kysymysosio", "Voit esittää kysymyksiä kurssialustalla. Vastaan itse kysymyksiin kerran viikossa."),
      ("user", "Henkilökohtainen sparraus (valinnainen)", "Puolen tunnin henkilökohtainen neuvonta, jossa testamenttisi käydään läpi yksityiskohtaisesti."),
    ],
    outcomes=["valmis testamentti, joka on laadittu oikein ja toimii juuri sinun tilanteessasi", "selkeä ymmärrys eri vaihtoehdoista ja usein epäselviksi jäävistä kohdista", "mielenrauha, koska tärkeä paperi on tehty varmasti ja oikein"],
    why=[
      "Testamenttikurssi perustuu voimassa olevaan lainsäädäntöön ja käytännön kokemukseen todellisista tilanteista. Ohjeet ovat testattuja, selkeitä ja ymmärrettäviä.",
      "Kaikki materiaali on tekstimuotoista, helposti luettavaa ja selkeästi jäsenneltyä. Voit edetä omaan tahtiin, palata kohtiin myöhemmin ja tallentaa kaiken itsellesi pysyvästi.",
    ],
    guarantee="Jos tunnet, ettei kurssi auttanut sinua eteenpäin, saat puolen tunnin henkilökohtaisen neuvonnan veloituksetta (arvo yli 100 €). Et jää yksin etkä ilman apua.",
  ),
]

pages = {
  "index.html": index,
  "tietoa-meista.html": about,
  "tiimimme.html": team,
  "yhteydenotto.html": contact,
  "tietosuojaseloste.html": privacy,
  "kayttoehdot.html": terms,
  "tietosuojakaytanto.html": policy,
}
for c in COURSES:
    pages[c["slug"]] = course_page(c)
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", name, len(html))
