# Lakiasiaintoimisto Virranvälke – demo-sivusto

Esittelyversio uudesta sivustosta Lakiasiaintoimisto Virranvälkkeelle. Sisältö ja toiminnot
vastaavat nykyistä sivustoa (https://virranvalke.webnode.fi/), mutta ulkoasu on tehty uusiksi.

**Tämä on demo.** Lomakkeet ja evästevalinnat eivät lähetä tai tallenna mitään palvelimelle;
ne näyttävät vain ilmoituksen. Jokaisen sivun yläreunassa on demo-banneri.

## Sivut

| Tiedosto | Sisältö |
|---|---|
| `index.html` | Etusivu: palvelut, minidigikurssit, asioinnin eteneminen, yhteydenotto-CTA |
| `tietoa-meista.html` | Yrityksen esittely ja laskutushinnat |
| `tiimimme.html` | Tiimi ja avoimet paikat |
| `yhteydenotto.html` | Yhteystiedot ja yhteydenottolomake (demo) |
| `tietosuojaseloste.html` | Tietosuojaseloste |
| `kayttoehdot.html` | Käyttöehdot (alkuperäisen sivuston malliteksti) |
| `tietosuojakaytanto.html` | Tietosuojakäytäntö (alkuperäisen sivuston malliteksti) |
| `logo.html` | Logokonseptit (sisäinen arviointisivu, linkki footerissa) |

## Logo

Sivustolla on käytössä konsepti A, "Virta-V": kaksi virtaavaa linjaa yhtyvät V-kirjaimeksi ja
oikeassa yläkulmassa on pieni välke. Tiedostot:

- `assets/logo.svg` – logomerkki tummansinisellä laatalla
- `assets/logo-wordmark.svg` – vaakalogo tekstillä (fontit Fraunces ja Inter; ilman niitä
  käytetään Georgia/Arial-varafontteja)

Vaihtoehtoiset konseptit B ja C ovat nähtävissä sivulla `logo.html`.

## Rakenne

- `assets/style.css` – kaikki tyylit (ei frameworkia, ei build-vaihetta)
- `assets/main.js` – mobiilivalikko, demo-evästebanneri ja demo-lomake
- `build.py` – generoi HTML-sivut yhteisellä headerilla ja footerilla

HTML-sivut on generoitu skriptillä. Jos muokkaat sisältöä, tee muutos `build.py`-tiedostoon ja aja:

```bash
python build.py .
```

## Paikallinen esikatselu

```bash
python -m http.server 8787
```

ja avaa http://localhost:8787/.

## Huomioita

- Hinnat ja alv-prosentit on kopioitu alkuperäiseltä sivustolta sellaisenaan.
- Tiimin kuvia ei ole mukana; tilalla on nimikirjaimet.
- Minidigikurssien linkit vievät alkuperäiseen Campwire-kauppaan.
