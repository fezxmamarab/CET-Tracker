#!/usr/bin/env python3
"""
Export a Carousel Pillar System HTML file to 1080x1350 PNGs.

Slides are authored at NATIVE 1080x1350 and previewed via a CSS transform:scale()
on each .slide. This script neutralises that preview transform so every slide
renders at true size, waits for web fonts, then screenshots each .slide *element*
(pixel-perfect, no clip rectangle).

Usage:
  python export_carousel.py INPUT.html OUTPUT_DIR [--selector .slide]
"""
import argparse, os, sys, pathlib

# Browser-path fallback: use Claude's pre-installed Chromium when present,
# otherwise rely on the default Playwright cache (user's own `playwright install chromium`).
if not os.environ.get("PLAYWRIGHT_BROWSERS_PATH") and os.path.isdir("/opt/pw-browsers"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"

from playwright.sync_api import sync_playwright

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output_dir")
    ap.add_argument("--selector", default=".slide")
    args = ap.parse_args()

    html_path = pathlib.Path(args.input).resolve()
    out_dir = pathlib.Path(args.output_dir); out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox","--force-color-profile=srgb"])
        page = browser.new_page(viewport={"width":1600,"height":1600}, device_scale_factor=1)
        page.goto(html_path.as_uri())

        # wait for fonts, then a settle delay
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(1200)

        # neutralise preview-only layout so each .slide renders at native 1080x1350
        page.add_style_tag(content=f"""
            {args.selector} {{
                transform: none !important;
                margin: 0 !important;
                box-shadow: none !important;
            }}
            body {{ gap: 0 !important; padding: 0 !important; background:#fff !important; }}
        """)
        page.wait_for_timeout(300)

        slides = page.query_selector_all(args.selector)
        if not slides:
            print(f"ERROR: no elements match '{args.selector}'"); browser.close(); sys.exit(1)

        n = len(slides)
        for i, el in enumerate(slides, 1):
            el.scroll_into_view_if_needed()
            box = el.bounding_box()
            path = out_dir / f"slide_{i:02d}.png"
            el.screenshot(path=str(path))
            print(f"  slide_{i:02d}.png  ({int(box['width'])}x{int(box['height'])} css px)")
        browser.close()
        print(f"Exported {n} slides -> {out_dir}")

if __name__ == "__main__":
    main()
