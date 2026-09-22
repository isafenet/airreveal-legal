#!/usr/bin/env python3
"""
Generates the localized AirReveal site pages from `site_i18n.py`, adds
hreflang alternates and a language switcher to the hand-authored English
pages, and rebuilds sitemap.xml.

    python3 tools/build_localized_site.py

Run from the repository root. Output (all committed):
    <lang>/index.html, <lang>/what-am-i-flying-over.html, <lang>/support.html
    hreflang + switcher blocks inside the English pages (between the
    `<!--i18n-->` markers; safe to re-run)
    sitemap.xml
Privacy and Terms stay English-only by design.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

from site_i18n import LANGS, T

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://airreveal.isafenet.app/"
GUIDE = "what-am-i-flying-over.html"
LOCALIZED_PAGES = ["index.html", GUIDE, "support.html"]
ENGLISH_ONLY = ["privacy.html", "terms.html"]
LASTMOD = "2026-09-20"
MARK_OPEN, MARK_CLOSE = "<!--i18n-->", "<!--/i18n-->"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def attr(text: str) -> str:
    return html.escape(text, quote=True)


def url(lang: str | None, page: str) -> str:
    """Absolute URL of `page` in `lang` (None = English)."""
    path = "" if page == "index.html" else page
    return BASE + (f"{lang}/" if lang else "") + path


def hreflang_block(page: str) -> str:
    """<link rel=alternate> set for a page that exists in every language."""
    lines = [f'<link rel="alternate" hreflang="en" href="{url(None, page)}">']
    for folder, (lang, _, _) in LANGS.items():
        lines.append(f'<link rel="alternate" hreflang="{lang}" href="{url(folder, page)}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{url(None, page)}">')
    return "".join(lines)


def switcher(current: str | None, page: str, label: str, prefix: str) -> str:
    """Language menu. `prefix` is the relative path back to the site root
    ("" for English pages, "../" for localized ones). Pages without a
    translation (privacy, terms) link to each language's home page."""
    target = page if page in LOCALIZED_PAGES else "index.html"
    items = [("en", "English", f"{prefix}{target}", current is None)]
    for folder, (lang, _, name) in LANGS.items():
        items.append((lang, name, f"{prefix}{folder}/{target}", current == folder))
    current_attr = ' aria-current="true"'
    links = "".join(
        f'<a href="{href}" hreflang="{code}" lang="{code}"{current_attr if active else ""}>{esc(name)}</a>'
        for code, name, href, active in items
    )
    return f'<details class="lang"><summary aria-label="{attr(label)}">🌐 {esc(label)}</summary><div class="lang-menu">{links}</div></details>'


# --------------------------------------------------------------------- shared
def head(lang_code: str, title: str, desc: str, canonical: str, page: str, og_title: str, og_desc: str, og_locale: str, og_type: str = "website", image: str = "images/marketing-wide.webp") -> str:
    return (
        '<!doctype html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">'
        '<link rel="canonical" href="%s">%s<meta name="robots" content="index,follow">'
        '<meta property="og:type" content="%s"><meta property="og:site_name" content="AirReveal">'
        '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s"><meta property="og:locale" content="%s">'
        '<meta property="og:image" content="%s%s">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%s%s">'
        '<link rel="icon" href="../images/app-icon.png"><link rel="apple-touch-icon" href="../images/app-icon.png">'
        '<link rel="stylesheet" href="../styles.css">'
    ) % (lang_code, esc(title), attr(desc), canonical, hreflang_block(page), og_type,
         attr(og_title), attr(og_desc), canonical, og_locale, BASE, image, attr(og_title), attr(og_desc), BASE, image)


def jsonld(obj) -> str:
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)


def software_ld(t: dict, folder: str) -> dict:
    return {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "AirReveal",
            "description": t["home_desc"], "applicationCategory": "TravelApplication",
            "operatingSystem": "iOS, iPadOS", "url": url(folder, "index.html"), "inLanguage": LANGS[folder][0],
            "image": BASE + "images/app-icon.png",
            "publisher": {"@type": "Organization", "name": "iSafeNet", "url": "https://isafenet.app/"},
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"}}


def faq_ld(pairs) -> dict:
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in pairs]}


def header(folder: str, t: dict, nav: list[tuple[str, str]], page: str = "index.html") -> str:
    links = "".join(f'<a href="{href}">{esc(label)}</a>' for href, label in nav)
    return ('<header class="site-header"><div class="bar"><a class="brand" href="index.html"><img src="../images/app-icon.png" alt="AirReveal">AirReveal</a>'
            f'<nav class="site-nav">{links}{switcher(folder, page, t["switcher"], "../")}</nav></div></header>')


def footer(t: dict, extra_links: str = "") -> str:
    f = t["footer"]
    return ('<footer class="site-footer"><div class="wrap"><span>© 2026 iSafeNet · AirReveal</span><nav>'
            f'<a href="{GUIDE}">{esc(f["guide"])}</a><a href="../privacy.html">{esc(f["privacy"])}</a>'
            f'<a href="../terms.html">{esc(f["terms"])}</a><a href="support.html">{esc(f["support"])}</a>'
            '<a href="mailto:info@isafenet.app">info@isafenet.app</a></nav></div>'
            f'<div class="wrap legal-note">{esc(t["legal_note"])}</div></footer>')


# ---------------------------------------------------------------------- home
def render_home(folder: str) -> str:
    t = T[folder]; lang_code, og_locale, _ = LANGS[folder]
    n, h, fe, ga, fl, fq, pr, st = t["nav"], t["hero"], t["features"], t["gallery"], t["flying"], t["faq"], t["pricing"], t["store"]
    # Screenshots are localized per language: images/<folder>/panel-*.webp and ipad-*.webp
    # (tools/localize_screenshots.py). The poster and wide banner are designed art and stay shared.
    imgs = ["plan", "flight", "discover", "journal", "collection", "profile"]
    cards = "".join(
        f'<article class="feature"><h3>{esc(a)}</h3><p>{esc(b)}</p><img src="../images/{folder}/panel-{im}.webp" alt="{attr(alt)}" loading="lazy" width="596" height="1260"></article>'
        for (a, b, alt), im in zip(fe["cards"], imgs))
    fly = "".join(f'<article class="feature"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in fl["cards"])
    faq = "".join(f'<section class="support-card"><h2>{esc(q)}</h2><p>{esc(a)}</p></section>' for q, a in fq["items"])
    free_h, free_p, free_li = pr["free"]; pro_h, pro_p, pro_li = pr["pro"]
    li = lambda xs: "".join(f"<li>{esc(x)}</li>" for x in xs)
    legal = "".join(f'<a class="legal-card" href="{href}"><strong>{esc(a)}</strong><span>{esc(b)}</span></a>'
                    for (a, b), href in zip(st["cards"], ["../privacy.html", "../terms.html", "support.html"]))
    body = (
        header(folder, t, [("#features", n["features"]), ("#gallery", n["gallery"]), ("#pricing", n["pro"]), ("#faq", n["faq"]), ("support.html", n["support"]), ("../privacy.html", n["privacy"])])
        + f'<main><section class="hero"><div class="wrap hero-grid"><div><div class="eyebrow">{esc(h["eyebrow"])}</div><h1>{esc(h["h1"])}</h1><p>{esc(h["p"])}</p>'
          f'<div class="cta-row"><a class="btn btn-primary" href="#features">{esc(h["cta1"])}</a><a class="btn btn-secondary" href="#app-store">{esc(h["cta2"])}</a></div>'
          f'<div class="trust">{"".join(f"<span>{esc(x)}</span>" for x in h["trust"])}</div></div>'
          f'<div class="hero-art"><img src="../images/{folder}/marketing-wide.webp" alt="{attr(ga["wide_alt"])}" width="1536" height="1024"></div></div></section>'
        f'<section class="section" id="features"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(fe["eyebrow"])}</div><h2>{esc(fe["h2"])}</h2><p>{esc(fe["p"])}</p></div><div class="features">{cards}</div></div></section>'
        f'<section class="section band" id="gallery"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(ga["eyebrow"])}</div><h2>{esc(ga["h2"])}</h2><p>{esc(ga["p"])}</p></div>'
          f'<div class="gallery">'
          + "".join(f'<img src="../images/{folder}/ipad-{im}.webp" alt="{attr(a)}">' for im, a in zip(["flight", "discover", "collection"], ga["ipad_alts"]))
          + '</div></div></section>'
        f'<section class="section" id="flying-over"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(fl["eyebrow"])}</div><h2>{esc(fl["h2"])}</h2><p>{esc(fl["p"])}</p></div>'
          f'<div class="features features-4">{fly}</div><p style="text-align:center;margin-top:28px"><a class="btn btn-primary" href="{GUIDE}">{esc(fl["button"])}</a></p></div></section>'
        f'<section class="section band" id="faq"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(fq["eyebrow"])}</div><h2>{esc(fq["h2"])}</h2></div><div class="support-grid">{faq}</div></div></section>'
        f'<section class="section" id="pricing"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(pr["eyebrow"])}</div><h2>{esc(pr["h2"])}</h2></div>'
          f'<div class="pricing"><div class="price-card"><h3>{esc(free_h)}</h3><p>{esc(free_p)}</p><ul>{li(free_li)}</ul></div>'
          f'<div class="price-card pro"><h3>{esc(pro_h)}</h3><p>{esc(pro_p)}</p><ul>{li(pro_li)}</ul></div></div><p class="price-note">{esc(pr["note"])}</p></div></section>'
        f'<section class="section" id="app-store"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(st["eyebrow"])}</div><h2>{esc(st["h2"])}</h2><p>{esc(st["p"])}</p></div><div class="legal-links">{legal}</div></div></section></main>'
        + footer(t)
    )
    return (head(lang_code, t["home_title"], t["home_desc"], url(folder, "index.html"), "index.html", t["og_title"], t["home_desc"], og_locale, image=f"images/{folder}/marketing-wide.webp")
            + jsonld(software_ld(t, folder)) + jsonld(faq_ld(fq["items"])) + "</head><body>\n" + body + "</body></html>\n")


# --------------------------------------------------------------------- guide
def render_guide(folder: str) -> str:
    t = T[folder]; g = t["guide"]; lang_code, og_locale, _ = LANGS[folder]
    n = t["nav"]
    bullets = "".join(f"<li><strong>{esc(b)}</strong> {esc(r)}</li>" for b, r in g["bullets"])
    faq = "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in g["faq"])
    sec = lambda sid, pair, extra="": f'<section class="clause" id="{sid}"><h2 class="clause-title">{esc(pair[0])}</h2><p>{esc(pair[1])}</p>{extra}</section>'
    body = (
        header(folder, t, [("index.html#features", n["features"]), ("index.html#faq", n["faq"]), ("support.html", n["support"]), ("../privacy.html", n["privacy"])], GUIDE)
        + '<div class="doc-wrap">'
          f'<header class="doc-head"><p class="eyebrow">{esc(g["eyebrow"])}</p><h1 class="doc-title">{esc(g["h1"])}</h1><p class="doc-meta">{esc(g["meta"])}</p><div class="lede">{g["lede"]}</div></header>'
        + sec("seatback", g["opt1"]) + sec("route", g["opt2"])
        + f'<section class="clause" id="gps"><h2 class="clause-title">{esc(g["opt3"][0])}</h2><p>{g["opt3"][1]}</p><ul>{bullets}</ul></section>'
        + f'<section class="clause" id="faq"><h2 class="clause-title">{esc(g["faq_h"])}</h2>{faq}<p>{esc(g["disclaimer"])}</p></section>'
        + f'<section class="clause"><p><a class="btn btn-primary" href="index.html#app-store">{esc(g["cta"])}</a></p></section></div>'
        + footer(t)
    )
    return (head(lang_code, g["title"], g["desc"], url(folder, GUIDE), GUIDE, g["og_title"], g["og_desc"], og_locale, "article")
            + jsonld(faq_ld(g["faq"])) + "</head><body>\n" + body + "</body></html>\n")


# ------------------------------------------------------------------- support
def render_support(folder: str) -> str:
    t = T[folder]; s = t["support"]; lang_code, og_locale, _ = LANGS[folder]
    n = t["nav"]
    cards = "".join(f'<section class="support-card"><h2>{esc(a)}</h2><p>{b}</p></section>' for a, b in s["cards"])
    body = (
        header(folder, t, [("index.html#features", n["features"]), ("index.html#pricing", n["pro"]), ("support.html", n["support"]), ("../privacy.html", n["privacy"])], "support.html")
        + f'<main class="doc-wrap"><header class="doc-head"><p class="eyebrow">{esc(s["eyebrow"])}</p><h1 class="doc-title">{esc(s["h1"])}</h1><p class="doc-meta">{esc(s["meta"])}</p><div class="lede">{s["lede"]}</div></header>'
          f'<div class="support-grid">{cards}</div></main>'
        + footer(t)
    )
    title = f'AirReveal — {s["title"]}'
    return (head(lang_code, title, s["desc"], url(folder, "support.html"), "support.html", title, s["desc"], og_locale)
            + "</head><body>\n" + body + "</body></html>\n")


# ------------------------------------------------------------- English pages
def patch_english(page: str) -> None:
    """Idempotently add hreflang alternates and the switcher to an English page."""
    path = ROOT / page
    s = path.read_text(encoding="utf-8")
    s = re.sub(re.escape(MARK_OPEN) + r".*?" + re.escape(MARK_CLOSE), "", s, flags=re.S)
    alt = hreflang_block(page) if page in LOCALIZED_PAGES else ""
    if alt:
        assert "</head>" in s, page
        s = s.replace("</head>", f"{MARK_OPEN}{alt}{MARK_CLOSE}</head>", 1)
    sw = switcher(None, page, "Language", "")
    m = re.search(r'<nav class="site-nav">.*?</nav>', s, flags=re.S)
    assert m, f"no site-nav in {page}"
    nav = m.group(0)
    s = s.replace(nav, nav[: -len("</nav>")] + f"{MARK_OPEN}{sw}{MARK_CLOSE}</nav>", 1)
    path.write_text(s, encoding="utf-8")


CSS_MARK = "/* i18n:language-switcher */"
CSS = f"""
{CSS_MARK}
.lang{{position:relative;margin-left:12px}}
.lang summary{{list-style:none;cursor:pointer;padding:8px 12px;border:1px solid var(--line);border-radius:999px;font-weight:700;font-size:14px;color:var(--ink);background:#fff;white-space:nowrap}}
.lang summary::-webkit-details-marker{{display:none}}
.lang-menu{{position:absolute;right:0;top:calc(100% + 8px);z-index:50;min-width:200px;padding:8px;background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:0 18px 40px #1232}}
.lang-menu a{{display:block;padding:9px 12px;border-radius:10px;color:var(--ink);text-decoration:none;font-weight:600}}
.lang-menu a:hover,.lang-menu a[aria-current]{{background:var(--ice)}}
@media(max-width:900px){{.site-nav{{display:flex}}.site-nav>a{{display:none}}.lang{{margin-left:0}}}}
.legal-note{{margin-top:10px;font-size:13px;opacity:.75}}
.price-note{{margin-top:18px;color:var(--muted);font-size:14px}}
"""


def write_css() -> None:
    p = ROOT / "styles.css"
    s = p.read_text(encoding="utf-8")
    if CSS_MARK in s:
        s = s[: s.index(CSS_MARK)].rstrip("\n") + "\n"
    p.write_text(s + CSS, encoding="utf-8")


def write_sitemap() -> None:
    def entry(page: str, langs: bool) -> str:
        def one(folder):
            alts = ""
            if langs:
                alts = f'<xhtml:link rel="alternate" hreflang="en" href="{url(None, page)}"/>'
                alts += "".join(f'<xhtml:link rel="alternate" hreflang="{LANGS[f][0]}" href="{url(f, page)}"/>' for f in LANGS)
                alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url(None, page)}"/>'
            return f"  <url><loc>{url(folder, page)}</loc><lastmod>{LASTMOD}</lastmod>{alts}</url>\n"
        return "".join(one(f) for f in [None, *LANGS]) if langs else one(None)

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "".join(entry(p, True) for p in LOCALIZED_PAGES) + "".join(entry(p, False) for p in ENGLISH_ONLY) + "</urlset>\n")
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def main() -> None:
    for folder in LANGS:
        out = ROOT / folder
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(render_home(folder), encoding="utf-8")
        (out / GUIDE).write_text(render_guide(folder), encoding="utf-8")
        (out / "support.html").write_text(render_support(folder), encoding="utf-8")
    for page in [*LOCALIZED_PAGES, *ENGLISH_ONLY]:
        patch_english(page)
    write_css()
    write_sitemap()
    print(f"built {len(LANGS)} languages x {len(LOCALIZED_PAGES)} pages; patched {len(LOCALIZED_PAGES) + len(ENGLISH_ONLY)} English pages")


if __name__ == "__main__":
    main()
