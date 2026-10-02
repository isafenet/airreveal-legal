"""
The AirReveal 2.0 home page in each language: the hand-built English index.html (marked `<!--standalone-->`)
with its text swapped for the translations in site_v2_strings.py. Plans, prices and the older questions come
from site_i18n so they read the same as the rest of the localized site. Called by build_localized_site.py.
"""

from __future__ import annotations

import html
import json
import re

from site_i18n import LANGS, T
from site_v2_strings import NEW_FAQ, STRINGS

# Pages that exist in every language folder; anything else is linked back to the English root.
BEST = ' class="best"'
KEEP = {"AirReveal", "App Store", "Apple Watch", "Watch"}  # names, the same in every language
LOCAL_PAGES = {"what-am-i-flying-over.html", "support.html"}


def render(folder: str, english: str, *, base: str, hreflang: str, spacing) -> tuple[str, list[str]]:
    """Return the page for `folder` and the English text nodes that had no translation."""
    strings = STRINGS[folder]
    new_faq = NEW_FAQ[folder]
    t = T[folder]
    if folder == "fr":
        strings, new_faq = spacing(strings), spacing(new_faq)
    lang_code, og_locale, _ = LANGS[folder]
    page_url = f"{base}{folder}/"
    missing: list[str] = []

    def tr(text: str) -> str | None:
        return strings.get(html.unescape(text).strip())

    head, body = english.split("<body>", 1)

    # ---- pricing: Free and Pro from site_i18n, tier names in place of pounds, and the currency note
    pr = t["pricing"]
    (free_h, free_p, free_li), (pro_h, pro_p, pro_li) = pr["free"], pr["pro"]
    li = "".join(f"<li>{html.escape(x)}</li>" for x in free_li)
    tiers = "".join(f'<div{BEST if i == 2 else ""}><b>{html.escape(x)}</b></div>' for i, x in enumerate(pro_li))
    prices = (f'<div class="prices">\n      <div class="plan"><h3>{html.escape(free_h)}</h3><p style="color:var(--soft)">{html.escape(free_p)}</p><ul>{li}</ul></div>\n'
              f'      <div class="plan pro"><h3>{html.escape(pro_h)}</h3><p style="color:var(--soft)">{html.escape(pro_p)}</p>\n'
              f'        <div class="tiers">{tiers}</div></div>\n    </div>\n'
              f'    <p style="color:var(--soft);font-size:14px;margin-top:16px">{html.escape(pr["note"])}</p>')
    body, n = re.subn(r'<div class="prices">.*?</div>\n    </div>', lambda m: '\x00prices\x00', body, count=1, flags=re.S)
    assert n == 1, "pricing block not found"

    # ---- questions: the English page's order, the older ones from site_i18n
    old = t["faq"]["items"]
    pairs = [old[0], *new_faq, old[1], old[2], old[3], old[6]]
    faq = "\n".join(f'      <details{" open" if i == 0 else ""}><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
                    for i, (q, a) in enumerate(pairs))
    body, n = re.subn(r'(<div class="faq">\n).*?(\n    </div>)', lambda m: m.group(1) + '\x00faq\x00' + m.group(2), body, count=1, flags=re.S)
    assert n == 1, "faq block not found"

    # ---- footer languages: the other four plus English
    others = [(f"../{f}/", code, name) for f, (code, _, name) in LANGS.items() if f != folder] + [("../", "en", "English")]
    also = " · ".join(f'<a href="{h}" hreflang="{c}" lang="{c}">{html.escape(nm)}</a>' for h, c, nm in others)
    body, n = re.subn(r'<p class="links" lang="en">.*?</p>', lambda m: '\x00also\x00', body, count=1, flags=re.S)
    assert n == 1, "language links not found"

    blocks = {"\x00prices\x00": prices, "\x00faq\x00": faq,
              "\x00also\x00": f'<p class="links">{html.escape(strings["Also in"])} {also}</p>'}

    # ---- body: text nodes (outside <script>), then alt and aria-label attributes
    parts = re.split(r"(<script\b.*?</script>)", body, flags=re.S)

    def text_node(m: re.Match) -> str:
        raw = m.group(1)
        stripped = raw.strip()
        if not stripped or "\x00" in stripped or not re.search(r"[A-Za-z]{2}", stripped):
            return m.group(0)
        out = tr(stripped)
        if out is None:
            if stripped not in KEEP and not re.fullmatch(r"AR\d+", stripped):
                missing.append(html.unescape(stripped))
            return m.group(0)
        lead, trail = raw[: len(raw) - len(raw.lstrip())], raw[len(raw.rstrip()):]
        return ">" + lead + html.escape(out, quote=False) + trail + "<"

    def attribute(m: re.Match) -> str:
        out = tr(m.group(2))
        if out is None:
            if m.group(2):
                missing.append(html.unescape(m.group(2)))
            return m.group(0)
        return f'{m.group(1)}="{html.escape(out, quote=True)}"'

    for i in range(0, len(parts), 2):
        p = re.sub(r">([^<>]+)<", text_node, parts[i])
        parts[i] = re.sub(r'\b(alt|aria-label)="([^"]*)"', attribute, p)
    body = "".join(parts)
    for token, block in blocks.items():
        body = body.replace(token, block)

    # ---- head: language, title, descriptions, addresses, alternates and the structured data
    title = strings["AirReveal: What Am I Flying Over? Flight Map & Sky Radar"]
    desc = strings[next(k for k in strings if k.startswith("See what you're flying over"))]
    og_title = "AirReveal 2.0: " + strings["Discover what's above and below"]
    head = head.replace('<html lang="en">', f'<html lang="{lang_code}">', 1)
    head = re.sub(r"<title>.*?</title>", lambda m: f"<title>{html.escape(title, quote=False)}</title>", head, count=1)
    head = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*"', lambda m: m.group(1) + html.escape(desc) + '"', head)
    head = re.sub(r'(<meta (?:property|name)="(?:og:title|twitter:title)" content=")[^"]*"', lambda m: m.group(1) + html.escape(og_title) + '"', head)
    head = head.replace('<meta property="og:locale" content="en_GB">', f'<meta property="og:locale" content="{og_locale}">', 1)
    head = head.replace(f'<link rel="canonical" href="{base}">', f'<link rel="canonical" href="{page_url}">', 1)
    head = head.replace(f'<meta property="og:url" content="{base}">', f'<meta property="og:url" content="{page_url}">', 1)
    head = re.sub(r"<!--i18n-->.*?<!--/i18n-->", "", head, flags=re.S)
    head = head.replace("</head>", hreflang + "</head>", 1)

    def ld(m: re.Match) -> str:
        data = json.loads(m.group(1))
        for node in data["@graph"]:
            if node["@type"] == "MobileApplication":
                node["url"] = page_url
                node["inLanguage"] = lang_code
                node["description"] = desc
            elif node["@type"] == "FAQPage":
                node["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in pairs]
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"

    head, n = re.subn(r'<script type="application/ld\+json">(.*?)</script>', ld, head, count=1, flags=re.S)
    assert n == 1, "structured data not found"

    page = head + "<body>" + body

    # ---- paths: shared files live one level up; the localized screenshots in images/v2/<folder>/
    page = re.sub(r'(src|href)="images/v2/(panel|screen)-(\d\d)\.webp"', rf'\1="../images/v2/{folder}/\2-\3.webp"', page)
    page = re.sub(r'(src|href)="(images/|fonts/)', r'\1="../\2', page)
    page = re.sub(r"url\((images/|fonts/)", r"url(../\1", page)

    def local(m: re.Match) -> str:
        target = m.group(1)
        return m.group(0) if target in LOCAL_PAGES else f'href="../{target}"'

    page = re.sub(r'href="([a-z0-9-]+\.html)"', local, page)
    return page, missing
