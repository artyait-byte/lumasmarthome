#!/usr/bin/env python3
"""Write a .webp next to every .jpg/.jpeg/.png under assets/.

The site serves the WebP (see `lu()` in js/app.js and url() in css/spa.css);
the originals stay for og:image, schema and the brochure. Re-run after adding
or replacing photos, then commit the .webp files:

    python3 scripts/make-webp.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
MAX_SIDE = 2400


def main() -> None:
    made = saved = 0
    for src in sorted((ROOT / "assets").rglob("*")):
        if src.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        dest = src.with_suffix(".webp")
        if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
            continue
        im = Image.open(src)
        alpha = im.mode in ("RGBA", "LA", "P")
        im = im.convert("RGBA" if alpha else "RGB")
        if max(im.size) > MAX_SIDE:
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        im.save(dest, "WEBP", quality=90 if alpha else 80, method=6)
        made += 1
        saved += src.stat().st_size - dest.stat().st_size
    print(f"[ok] {made} webp written, {saved / 1e6:.1f} MB smaller than the originals")


if __name__ == "__main__":
    main()
