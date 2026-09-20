#!/usr/bin/env python3
"""
Localizes the five-panel marketing artwork (`marketing-wide`) for the
translated site pages.

    python3 tools/localize_wide_art.py <source.png> <raw-dir> [<out-dir>]
    python3 tools/localize_wide_art.py <source.png> <raw-dir> --english [panel,...]

With `--english`, the English artwork is rebuilt in place: no text is touched, only
the named phones' screens (default: profile) are replaced with the `en` captures,
written to `images/marketing-wide.webp`.

  <source.png>  the flat 1536x1024 artwork (English text baked in)
  <raw-dir>     localized app captures, as for `localize_screenshots.py`
                (`<raw-dir>/iphone/<lang>/<name>.png`)
  <out-dir>     defaults to the repo's `images/`; writes
                `images/<folder>/marketing-wide.webp` per language

For each language it (1) erases the English panel headings, subtitles,
bottom captions and footer tagline, (2) draws the translated text in their
place, and (3) replaces each phone's screen with the real capture in that
language. The handwritten "Same Sky, A Brighter Perspective" line and the
App Store badge are part of the artwork and stay as they are.

Needs numpy, Pillow and opencv (`pip install numpy pillow opencv-python-headless`).
Positions were measured from this specific artwork; if the artwork changes,
re-measure `PANELS`, `CAPTIONS` and `FOOTER`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_i18n import T  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FONT = "/System/Library/Fonts/Avenir Next.ttc"
BOLD, DEMI, MEDIUM, REGULAR = 0, 2, 5, 7  # face indexes in Avenir Next.ttc
LANGS = ["es", "fr", "de", "it", "pt-BR"]

# Measured from the artwork. Each panel: outer x-range, phone-screen rect
# (x0, x1, y0, y1) and the raw capture shown on it.
PANELS = [
    dict(x=(12, 322),   screen=(48, 288, 245, 742),    raw="01-Flight-LiveTracking"),
    dict(x=(331, 617),  screen=(354, 596, 245, 758),   raw="02-Discover-WhichSideToLook"),
    dict(x=(626, 911),  screen=(648, 890, 245, 743),   raw="03-Journal"),
    dict(x=(920, 1204), screen=(943, 1184, 245, 740),  raw="03b-Collection"),
    dict(x=(1214, 1525), screen=(1247, 1488, 245, 750), raw="04-Profile-Top"),
]
HEAD_Y = (84, 234)            # heading + subtitle band, same in every panel
# Bottom captions: erase rect (x0, x1, y0, y1) and the left edge / vertical
# centre the new text is anchored to, plus the max text width.
CAPTIONS = [
    dict(erase=(176, 300, 900, 942),  x=180,  cy=921, w=122),
    dict(erase=(447, 580, 894, 942),  x=452,  cy=918, w=140),
    dict(erase=(748, 892, 894, 942),  x=752,  cy=921, w=142),
    dict(erase=(1043, 1190, 894, 942), x=1049, cy=922, w=140),
    dict(erase=(1325, 1500, 894, 942), x=1330, cy=921, w=160),
]
FOOTER = dict(erase=(686, 908, 994, 1018), x=689, cy=1006, w=214)

# Panel captions and footer tagline per language (the headings and subtitles
# are the same strings as the site's feature cards).
TEXT = {
    "es": dict(captions=["PRIMERO SIN CONEXIÓN", "LUGARES REALES\nHISTORIAS REALES", "DE VUELOS\nA RECUERDOS", "+5.000\nLUGARES", "LOGROS\nY MÁS"],
               tagline="Más que volar. Un mundo más luminoso."),
    "fr": dict(captions=["HORS CONNEXION D'ABORD", "LIEUX RÉELS\nHISTOIRES RÉELLES", "DES VOLS\nAUX SOUVENIRS", "5 000+\nSITES", "SUCCÈS\nET PLUS"],
               tagline="Plus qu'un vol. Un monde plus lumineux."),
    "de": dict(captions=["ERST OFFLINE", "ECHTE ORTE\nECHTE GESCHICHTEN", "AUS FLÜGEN\nWERDEN ERINNERUNGEN", "5.000+\nSEHENSWÜRDIGKEITEN", "ERFOLGE\nUND MEHR"],
               tagline="Mehr als ein Flug. Eine hellere Welt."),
    "it": dict(captions=["PRIMA DI TUTTO OFFLINE", "LUOGHI REALI\nSTORIE REALI", "DAI VOLI\nAI RICORDI", "5.000+\nLUOGHI", "TRAGUARDI\nE ALTRO"],
               tagline="Più di un volo. Un mondo più luminoso."),
    "pt-BR": dict(captions=["OFFLINE EM PRIMEIRO LUGAR", "LUGARES REAIS\nHISTÓRIAS REAIS", "DE VOOS\nA MEMÓRIAS", "5.000+\nPONTOS TURÍSTICOS", "CONQUISTAS\nE MAIS"],
                  tagline="Mais que voar. Um mundo mais luminoso."),
}
FOLDER = {"es": "es", "fr": "fr", "de": "de", "it": "it", "pt-BR": "pt-br"}
SS = 4  # supersampling for text and masks


def font(face: int, size: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, round(size * SS), index=face)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap honouring explicit newlines."""
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_w * SS:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def fit(draw, text, face, max_w, max_lines, start, floor, spacing=1.18):
    """Largest font size (start..floor) whose wrapped text fits."""
    size = start
    while size >= floor:
        f = font(face, size)
        lines = wrap(draw, text, f, max_w)
        widest = max(draw.textlength(l, font=f) for l in lines) / SS
        if len(lines) <= max_lines and widest <= max_w + 0.5:
            return f, lines, size * spacing
        size -= 0.5
    f = font(face, floor)
    return f, wrap(draw, text, f, max_w), floor * spacing


def balance(probe, text, fnt, lines):
    """For a two-line heading, move the break so the lines are as even as
    possible (avoids a lone short word on the second line)."""
    if len(lines) != 2:
        return lines
    words = text.split()
    best = lines
    best_w = max(probe.textlength(l, font=fnt) for l in lines)
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        w = max(probe.textlength(a, font=fnt), probe.textlength(b, font=fnt))
        if w < best_w - 1:
            best, best_w = [a, b], w
    return best


TEXT_TOP, TEXT_BOTTOM = 90, 226   # heading + subtitle must fit between these y values


def fit_block(probe, title, sub, inner):
    """Pick the largest heading/subtitle sizes whose stacked height fits the
    band above the phone. Heading shrinks first, down to a floor, then the
    subtitle; the heading keeps priority since it carries the message."""
    for hs in [x / 2 for x in range(64, 43, -1)]:            # 32 .. 22
        hf, hl, hh = fit(probe, title, DEMI, inner, 2, hs, hs, 1.08)
        if max(probe.textlength(l, font=hf) for l in hl) / SS > inner + 0.5 or len(hl) > 2:
            continue
        hl = balance(probe, title, hf, hl)
        for ss in [x / 2 for x in range(33, 24, -1)]:         # 16.5 .. 12.5
            sf, sl, sh = fit(probe, sub, MEDIUM, inner + 6, 3, ss, ss, 1.22)
            widest = max(probe.textlength(l, font=sf) for l in sl) / SS
            if len(sl) <= 3 and widest <= inner + 6.5 and len(hl) * hh + 7 + len(sl) * sh <= TEXT_BOTTOM - TEXT_TOP:
                return hf, hl, hh, sf, sl, sh
    hf, hl, hh = fit(probe, title, DEMI, inner, 2, 22, 22, 1.08)
    sf, sl, sh = fit(probe, sub, MEDIUM, inner + 6, 4, 12, 12, 1.2)
    return hf, hl, hh, sf, sl, sh


def erase(img: np.ndarray, rect, thresh=222, dilate=7, luma_gap=14, dark_text=False) -> np.ndarray:
    """Inpaint text pixels inside rect. White text by default; dark text
    (footer tagline) with dark_text=True."""
    x0, x1, y0, y1 = rect
    roi = img[y0:y1, x0:x1]
    gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY).astype(np.float32)
    local = cv2.GaussianBlur(gray, (0, 0), 9)
    if dark_text:
        mask = (local - gray) > luma_gap
    else:
        mask = ((roi.min(axis=2) > thresh) & ((gray - local) > luma_gap * 0.4)) | ((gray - local) > 38)
    mask = cv2.dilate(mask.astype(np.uint8) * 255, np.ones((dilate, dilate), np.uint8))
    full = np.zeros(img.shape[:2], np.uint8)
    full[y0:y1, x0:x1] = mask
    return cv2.inpaint(img, full, 6, cv2.INPAINT_TELEA)


def draw_lines(overlay, lines, fnt, x, y_top, line_h, align, color, anchor_w=0):
    d = ImageDraw.Draw(overlay)
    for i, line in enumerate(lines):
        w = d.textlength(line, font=fnt)
        px = x - w / 2 if align == "center" else x
        d.text((px, y_top + i * line_h * SS), line, font=fnt, fill=color)


def text_layer(size, jobs, shadow=(0, 40, 90, 95)):
    """Render jobs onto a supersampled RGBA layer with a soft shadow; return
    it downsampled to `size`."""
    W, H = size
    top = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    for job in jobs:
        draw_lines(top, **job)
    if shadow:
        sh = Image.new("RGBA", top.size, (0, 0, 0, 0))
        alpha = top.split()[3].filter(ImageFilter.GaussianBlur(2.2 * SS))
        sh_col = Image.new("RGBA", top.size, shadow)
        sh = Image.composite(sh_col, sh, alpha.point(lambda a: min(255, int(a * 0.9))))
        sh = ImageChops_offset(sh, 0, int(1.5 * SS))
        top = Image.alpha_composite(sh, top)
    return top.resize((W, H), Image.LANCZOS)


def ImageChops_offset(im, dx, dy):
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    out.paste(im, (dx, dy))
    return out


def rounded_mask(size, rect, radius):
    W, H = size
    x0, x1, y0, y1 = rect
    m = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(m).rounded_rectangle([x0 * SS, y0 * SS, x1 * SS - 1, y1 * SS - 1], radius=radius * SS, fill=255)
    return m.resize((W, H), Image.LANCZOS)


def localize(src: Image.Image, raw: Path, lang: str) -> Image.Image:
    t = TEXT[lang]
    cards = T[FOLDER[lang]]["features"]["cards"]
    arr = np.array(src.convert("RGB"))
    # 1. erase English text
    for p in PANELS:
        arr = erase(arr, (p["x"][0] + 14, p["x"][1] - 14, HEAD_Y[0], HEAD_Y[1]))
    for c in CAPTIONS:
        arr = erase(arr, c["erase"], thresh=208, luma_gap=10)
    arr = erase(arr, FOOTER["erase"], dark_text=True, luma_gap=12, dilate=5)
    img = Image.fromarray(arr)

    # 2. phone screens: real captures in this language
    for p in PANELS:
        x0, x1, y0, y1 = p["screen"]
        shot = Image.open(raw / "iphone" / lang / f"{p['raw']}.png").convert("RGB").resize((x1 - x0, y1 - y0), Image.LANCZOS)
        layer = Image.new("RGB", img.size)
        layer.paste(shot, (x0, y0))
        img = Image.composite(layer, img, rounded_mask(img.size, p["screen"], 31))

    # 3. new text
    probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    jobs = []
    for p, (title, sub, _alt) in zip(PANELS, cards):
        cx = (p["x"][0] + p["x"][1]) / 2
        inner = p["x"][1] - p["x"][0] - 40
        hf, hl, hh, sf, sl, sh = fit_block(probe, title, sub, inner)
        y = TEXT_TOP
        jobs.append(dict(lines=hl, fnt=hf, x=cx * SS, y_top=y * SS, line_h=hh, align="center", color=(255, 255, 255, 255)))
        y_sub = y + len(hl) * hh + 7
        jobs.append(dict(lines=sl, fnt=sf, x=cx * SS, y_top=y_sub * SS, line_h=sh, align="center", color=(255, 255, 255, 240)))
    for c, text in zip(CAPTIONS, t["captions"]):
        f, lines, lh = fit(probe, text, MEDIUM, c["w"], 2, 14.5, 9.5, 1.18)
        top = c["cy"] - len(lines) * lh / 2 + (lh - 14.5) / 2 - 1
        jobs.append(dict(lines=lines, fnt=f, x=c["x"] * SS, y_top=top * SS, line_h=lh, align="left", color=(255, 255, 255, 255)))
    img = Image.alpha_composite(img.convert("RGBA"), text_layer(img.size, jobs)).convert("RGB")

    # footer tagline (dark text on cloud photo: no shadow)
    f, lines, lh = fit(probe, t["tagline"], MEDIUM, FOOTER["w"], 1, 13.5, 9.5, 1.1)
    foot = text_layer(img.size, [dict(lines=lines, fnt=f, x=FOOTER["x"] * SS, y_top=(FOOTER["cy"] - lh / 2 - 1) * SS, line_h=lh, align="left", color=(64, 84, 118, 255))], shadow=None)
    return Image.alpha_composite(img.convert("RGBA"), foot).convert("RGB")


def english_screens(src: Image.Image, raw: Path, which: list[str]) -> Image.Image:
    """The English artwork with only some phones' screens replaced (text untouched)."""
    names = {"flight": 0, "discover": 1, "journal": 2, "collection": 3, "profile": 4}
    img = src.convert("RGB")
    for key in which:
        p = PANELS[names[key]]
        x0, x1, y0, y1 = p["screen"]
        shot = Image.open(raw / "iphone" / "en" / f"{p['raw']}.png").convert("RGB").resize((x1 - x0, y1 - y0), Image.LANCZOS)
        layer = Image.new("RGB", img.size)
        layer.paste(shot, (x0, y0))
        img = Image.composite(layer, img, rounded_mask(img.size, p["screen"], 31))
    return img


def main(src: Path, raw: Path, out: Path) -> None:
    source = Image.open(src)
    assert source.size == (1536, 1024), f"unexpected artwork size {source.size}"
    for lang in LANGS:
        folder = out / FOLDER[lang]
        folder.mkdir(parents=True, exist_ok=True)
        localize(source, raw, lang).save(folder / "marketing-wide.webp", "WEBP", quality=90, method=6)
        print(f"{lang}: {folder.relative_to(ROOT) if folder.is_relative_to(ROOT) else folder}/marketing-wide.webp")


if __name__ == "__main__":
    if "--english" in sys.argv:
        rest = [a for a in sys.argv[1:] if a != "--english"]
        which = rest[2].split(",") if len(rest) > 2 else ["profile"]
        art = english_screens(Image.open(rest[0]), Path(rest[1]), which)
        art.save(ROOT / "images" / "marketing-wide.webp", "WEBP", quality=90, method=6)
        print(f"en: replaced {', '.join(which)} in images/marketing-wide.webp")
        sys.exit(0)
    if len(sys.argv) not in (3, 4):
        print(__doc__)
        sys.exit(2)
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]) if len(sys.argv) == 4 else ROOT / "images")
