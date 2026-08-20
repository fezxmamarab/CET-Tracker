#!/usr/bin/env python3
"""
export_poster.py — render poster HTML to pixel-perfect PNG(s).

Sibling to the carousel skill's export_carousel.py. Same mechanism
(Playwright screenshots the target element after neutralising the preview
transform), generalised to any poster format via --format / --width / --height.

Usage:
    python export_poster.py INPUT.html OUTPUT_DIR [--format tall]
    python export_poster.py INPUT.html OUTPUT_DIR --width 1080 --height 1350
    python export_poster.py INPUT.html OUTPUT_DIR --selector ".poster"

Formats (width x height):
    square    1080 x 1080   (1:1)
    portrait  1080 x 1350   (4:5)
    tall      1080 x 1440   (3:4)   [default — grid-safe]
    story     1080 x 1920   (9:16)
"""
import argparse, os, sys, pathlib
from playwright.sync_api import sync_playwright

PRESETS = {
    "square":   (1080, 1080),
    "portrait": (1080, 1350),
    "tall":     (1080, 1440),
    "story":    (1080, 1920),
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output_dir")
    ap.add_argument("--format", choices=PRESETS.keys(), default="tall")
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    ap.add_argument("--selector", default=".poster")
    args = ap.parse_args()

    if args.width and args.height:
        exp_w, exp_h = args.width, args.height
    else:
        exp_w, exp_h = PRESETS[args.format]

    in_path = pathlib.Path(args.input).resolve()
    if not in_path.exists():
        sys.exit(f"Input not found: {in_path}")
    os.makedirs(args.output_dir, exist_ok=True)
    url = in_path.as_uri()

    with sync_playwright() as p:
        # Prefer Claude's pre-installed Chromium when present; else default.
        try:
            browser = p.chromium.launch()
        except Exception:
            browser = p.chromium.launch(channel="chromium")
        page = browser.new_page(
            viewport={"width": exp_w + 240, "height": exp_h + 240},
            device_scale_factor=1,
        )
        page.goto(url, wait_until="networkidle")
        # wait for web fonts before capture
        try:
            page.evaluate("document.fonts && document.fonts.ready")
            page.wait_for_function("document.fonts ? document.fonts.status === 'loaded' : true", timeout=8000)
        except Exception:
            pass
        page.wait_for_timeout(600)

        els = page.query_selector_all(args.selector)
        if not els:
            browser.close()
            sys.exit(f"No elements match selector {args.selector!r}")

        multi = len(els) > 1
        for i, el in enumerate(els, start=1):
            # neutralise the preview transform so the element renders at native size
            el.evaluate("e => { e.style.transform = 'none'; }")
            page.wait_for_timeout(150)
            box = el.bounding_box()
            name = f"poster_{i:02d}.png" if multi else "poster.png"
            out = os.path.join(args.output_dir, name)
            el.screenshot(path=out)
            w = round(box["width"]); h = round(box["height"])
            ok = "OK" if (w == exp_w and h == exp_h) else f"WARN expected {exp_w}x{exp_h}"
            print(f"{name}: {w}x{h}  [{ok}]")

        browser.close()
    print(f"Done -> {args.output_dir}")

if __name__ == "__main__":
    main()
