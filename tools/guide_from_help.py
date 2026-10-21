"""Rebuilds user-guide.html's sections from the app's in-app Help, so the website guide and the app never drift.

    python3 tools/guide_from_help.py [path/to/AirReveal/Scripts/help/en.json] [version]

Reads the Help's English source (default: ../AirReveal/Scripts/help/en.json) and rewrites, in user-guide.html,
the version line, the lede, the contents list and every section between the contents and </main>. The page's
head, header and footer are left as they are. Help's own markup: **bold**, paragraphs starting "• " become a
list, and paragraphs starting "1. " become a numbered list.
"""

import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "..", "user-guide.html")
HELP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "AirReveal", "Scripts", "help", "en.json")
VERSION = sys.argv[2] if len(sys.argv) > 2 else "3.0"

LEDE = ("<strong>New to AirReveal? You only need four steps.</strong> Add your flight, let it download while you have "
        "Wi-Fi, start Live at the airport, then look out of the window. On the ground, the map shows the planes flying "
        "over you, the places around you and every airport. Everything below is optional extra. The same guide is in "
        "the app, under Profile › Settings › Help.")


def inline(text):
    """Help's **bold** as <strong>, everything else escaped."""
    parts = re.split(r"\*\*(.+?)\*\*", text)
    return "".join(f"<strong>{html.escape(p, quote=False)}</strong>" if i % 2 else html.escape(p, quote=False)
                   for i, p in enumerate(parts))


def section(number, key, topic):
    out = [f'  <section class="clause" id="{key}">',
           f'    <h2 class="clause-title"><span class="num">{number}</span>{html.escape(topic["title"])}</h2>']
    run, kind = [], None

    def flush():
        nonlocal run, kind
        if run:
            tag = "ol" if kind == "ol" else "ul"
            out.append(f"    <{tag}>")
            out.extend(f"      <li>{inline(item)}</li>" for item in run)
            out.append(f"    </{tag}>")
        run, kind = [], None

    for paragraph in topic["paragraphs"]:
        bullet = re.match(r"^[•·]\s*(.*)", paragraph, re.S)
        numbered = re.match(r"^\d+\.\s+(.*)", paragraph, re.S)
        if bullet or numbered:
            this = "ul" if bullet else "ol"
            if kind and kind != this:
                flush()
            kind = this
            run.append((bullet or numbered).group(1))
        else:
            flush()
            out.append(f"    <p>{inline(paragraph)}</p>")
    flush()
    out.append("  </section>")
    return "\n".join(out)


def main():
    topics = json.load(open(HELP, encoding="utf-8"))
    page = open(PAGE, encoding="utf-8").read()
    page = re.sub(r'<p class="doc-meta">For AirReveal [^ ]+ on', f'<p class="doc-meta">For AirReveal {VERSION} on', page)
    page = re.sub(r'(<div class="lede">\s*).*?(\s*</div>)', lambda m: m.group(1) + LEDE + m.group(2), page, count=1, flags=re.S)
    toc = "\n".join(f'      <li><a href="#{k}">{html.escape(t["title"])}</a></li>' for k, t in topics.items())
    page = re.sub(r'(<nav class="toc"[^>]*>\s*<p>[^<]*</p>\s*<ol>\n).*?(\s*</ol>)', lambda m: m.group(1) + toc + m.group(2),
                  page, count=1, flags=re.S)
    body = "\n\n".join(section(n, k, t) for n, (k, t) in enumerate(topics.items(), start=1))
    start = page.index("</nav>", page.index('<nav class="toc"')) + len("</nav>")
    end = page.index("</main>")
    page = page[:start] + "\n\n" + body + "\n\n" + page[end:]
    open(PAGE, "w", encoding="utf-8").write(page)
    print(f"user-guide.html: {len(topics)} sections from {os.path.relpath(HELP)} (AirReveal {VERSION})")


if __name__ == "__main__":
    main()
