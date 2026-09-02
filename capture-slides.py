"""Render each sheet of the deck to a PNG in ./Slides.

Run:  python capture-slides.py [width] [height]
"""
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

W = int(sys.argv[1]) if len(sys.argv) > 1 else 1920
H = int(sys.argv[2]) if len(sys.argv) > 2 else 1080

ROOT = pathlib.Path(__file__).resolve().parent
DECK = ROOT / "index.html"
OUT = ROOT / "Slides"
OUT.mkdir(exist_ok=True)


def slug(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "sheet"


with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
    page.goto(DECK.as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")

    titles = page.evaluate(
        "[...document.querySelectorAll('.slide')].map(s => s.dataset.title)"
    )

    for i, title in enumerate(titles):
        # drive the deck the way the deck itself does, then let the
        # reveal transitions finish before the shutter
        page.evaluate(
            """(i) => {
                const deck = document.getElementById('deck');
                deck.scrollTop = i * deck.clientHeight;
                deck.dispatchEvent(new Event('scroll'));
            }""",
            i,
        )
        page.wait_for_timeout(3400)

        name = f"{i:02d}-{slug(title)}.png"
        # fast-forward any transition still in flight to its end state
        page.screenshot(path=str(OUT / name), animations="disabled")
        print(f"  {name}")

    browser.close()

print(f"\n{len(titles)} sheets -> {OUT}  ({W}x{H} @2x)")
