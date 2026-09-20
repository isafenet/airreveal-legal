#!/usr/bin/env python3
"""
Builds the localized screenshot images used by the translated site pages.

    python3 tools/localize_screenshots.py <raw-dir> [panel,panel,...] [--english]

With a comma-separated panel list (flight,discover,journal,collection,profile)
only those panels' images are rebuilt, so one changed screen doesn't churn the
rest. `--english` also rebuilds the English images (`images/panel-*.webp`,
`images/ipad-*.webp`) from the raw `en` captures, using the ORIGINAL photo
panel from git (`git show HEAD:images/panel-<name>.webp`) as the template.

`<raw-dir>` holds captures made by the app's `LocalizedScreenshotUITests`
(see that file for the capture command), laid out as

    <raw-dir>/iphone/<lang>/<name>.png      (1206x2622, iPhone 17)
    <raw-dir>/ipad/<lang>/<name>.png        (2064x2752, iPad Pro 13")

with `<lang>` one of es, fr, de, it, pt-BR. Output goes to
`images/<folder>/` (folder = lower-cased lang, e.g. pt-br):

  * `panel-*.webp` — the iPhone capture composited into the *existing* photo
    panel (`images/panel-*.webp`). The photo, phone and bezel are untouched;
    only the screen is replaced, using an outline measured from each panel.
  * `ipad-*.webp`  — the iPad capture, downscaled to 900x1200.

`marketing-poster.webp` and `marketing-wide.webp` are designed graphics with
the tagline baked into the artwork, so they are not regenerated.
"""
from __future__ import annotations

from PIL import Image, ImageFilter, ImageDraw
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["es", "fr", "de", "it", "pt-BR"]
IPAD = {"flight": "01-Flight-LiveTracking", "discover": "02-Discover-WhichSideToLook", "journal": "03-Journal",
        "collection": "03b-Collection", "profile": "04-Profile-Top"}

PANELS = {  # panel -> raw screenshot name
    "flight": "01-Flight-LiveTracking",
    "discover": "02-Discover-WhichSideToLook",
    "journal": "03-Journal",
    "collection": "03b-Collection",
    "profile": "04-Profile-Top",
}
DARK = 55


def runs(flags):
    out, x, n = [], 0, len(flags)
    while x < n:
        if flags[x]:
            s = x
            while x < n and flags[x]:
                x += 1
            out.append((s, x))
        else:
            x += 1
    return out


def measure(panel: Image.Image):
    """Return (xl(y), xr(y), top) describing the screen outline."""
    W, H = panel.size
    px = panel.load()
    dark = lambda x, y: max(px[x, y]) < DARK
    Ls, Rs = [], []
    for y in range(500, 900, 7):
        rs = runs([dark(x, y) for x in range(W)])
        l = [r for r in rs if 5 <= r[0] <= 70 and r[1] - r[0] >= 5]
        r_ = [r for r in rs if r[1] >= W - 70 and r[1] - r[0] >= 5]
        if l: Ls.append(l[0][1])
        if r_: Rs.append(r_[-1][0])
    Ls.sort(); Rs.sort()
    li, ri = Ls[len(Ls) // 2], Rs[len(Rs) // 2]
    col = runs([dark(W // 2, y) for y in range(H)])
    top = [r for r in col if r[1] - r[0] >= 6][0][1]
    # Raw per-row edges (reliable once we are past the glossy bezel highlight).
    raw_l, raw_r = {}, {}
    for y in range(top, min(H, top + 160)):
        x = li
        if dark(x, y):
            while x < W // 2 and dark(x, y): x += 1
        raw_l[y] = x
        x = ri - 1
        if dark(x, y):
            while x > W // 2 and dark(x, y): x -= 1
        raw_r[y] = x + 1
    # Fit (top y0, corner radius r) of a rounded rect to the left/right edges.
    best = None
    for y0 in range(top - 10, top + 8):
        for r in range(40, 121):
            err = n = 0
            for y in range(y0 + 22, y0 + r - 4):
                dy = y0 + r - y
                off = r - (r * r - dy * dy) ** 0.5
                err += (raw_l[y] - (li + off)) ** 2 + (raw_r[y] - (ri - off)) ** 2
                n += 2
            if n and (best is None or err / n < best[0]):
                best = (err / n, y0, r)
    _, y0, r = best
    xl, xr = {}, {}
    for y in range(y0, H):
        dy = y0 + r - y
        off = r - (r * r - dy * dy) ** 0.5 if dy > 0 else 0
        xl[y] = li + off
        xr[y] = ri - off
    top = y0
    measure.fit = (y0, r)
    return li, ri, top, xl, xr


def composite(panel_path, shot_path, out_path, quality=88):
    panel = Image.open(panel_path).convert("RGB")
    W, H = panel.size
    li, ri, top, xl, xr = measure(panel)
    shot = Image.open(shot_path).convert("RGB")
    sw = ri - li
    sh = round(shot.height * sw / shot.width)
    shot = shot.resize((sw, sh), Image.LANCZOS)
    layer = Image.new("RGB", (W, H))
    layer.paste(shot, (li, top))
    # 4x supersampled outline mask for smooth corner edges
    S = 4
    mask = Image.new("L", (W * S, H * S), 0)
    d = ImageDraw.Draw(mask)
    for y in range(top, H):
        d.rectangle([round(xl[y] * S), y * S, round(xr[y] * S) - 1, y * S + S - 1], fill=255)
    mask = mask.resize((W, H), Image.LANCZOS)
    out = Image.composite(layer, panel, mask)
    out.save(out_path, "WEBP", quality=quality, method=6)
    return out


def main(raw: Path, only: list[str] | None = None, english: bool = False) -> None:
    import subprocess
    images = ROOT / "images"
    wanted = only or list(PANELS)
    for lang in LANGS:
        out = images / lang.lower()
        out.mkdir(exist_ok=True)
        for panel in wanted:
            composite(images / f"panel-{panel}.webp", raw / "iphone" / lang / f"{PANELS[panel]}.png", out / f"panel-{panel}.webp")
            ipad = Image.open(raw / "ipad" / lang / f"{IPAD[panel]}.png").convert("RGB").resize((900, 1200), Image.LANCZOS)
            ipad.save(out / f"ipad-{panel}.webp", "WEBP", quality=88, method=6)
        print(f"{lang}: {', '.join(wanted)} -> {out.relative_to(ROOT)}")
    if english:
        for panel in wanted:
            # Template = the original photo panel, not a previously composited one.
            template = images / f".template-panel-{panel}.webp"
            template.write_bytes(subprocess.check_output(["git", "show", f"HEAD:images/panel-{panel}.webp"], cwd=ROOT))
            try:
                composite(template, raw / "iphone" / "en" / f"{PANELS[panel]}.png", images / f"panel-{panel}.webp")
            finally:
                template.unlink()
            ipad = Image.open(raw / "ipad" / "en" / f"{IPAD[panel]}.png").convert("RGB").resize((900, 1200), Image.LANCZOS)
            ipad.save(images / f"ipad-{panel}.webp", "WEBP", quality=88, method=6)
        print(f"en: {', '.join(wanted)} -> images/")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or len(args) > 2:
        print(__doc__)
        sys.exit(2)
    main(Path(args[0]), args[1].split(",") if len(args) > 1 else None, "--english" in sys.argv)
