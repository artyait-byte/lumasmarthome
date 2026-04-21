#!/usr/bin/env python3
"""One-shot migration: inline `background-image:url(unsplash)` -> `data-img="key"`.

Why:  the prototype hard-codes the same ~13 photos 104 times across 13 HTML
pages.  Changing an image required 8-12 edits.  This migration rewrites every
offending element to reference a content key (see js/images.js), so a swap is
now a one-line edit in the registry.

Safety:
    * Idempotent — elements that already have `data-img` are skipped.
    * Only touches inline styles that match the Unsplash photo pattern —
      other inline styles (if any) are left alone.
    * Preserves non-background-image declarations inside the same `style=""`
      (e.g. `background-size:cover`).
    * If a style attribute becomes empty after stripping, the attribute is
      removed cleanly.

After running once, every <script src="js/main.js..."> gets a sibling
<script src="js/images.js..."> loaded *before* it, so the loader runs first.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# photo-ID -> semantic key (matches js/images.js)
KEYS: dict[str, str] = {
    "photo-1540932239986-30128078f3c5": "lighting-scene",
    "photo-1505692794403-34cb9f8c7bbe": "window-shades",
    "photo-1489599510096-6e16d4b2b3c8": "home-theater",
    "photo-1558618666-fcd25c85cd64":  "audio-system",
    "photo-1557324232-b8917d3c3dcb":  "security-camera",
    "photo-1544197150-b99a580bb7a8":  "networking-rack",
    "photo-1585771724684-38269d6639fd": "gulf-sunset",
    "photo-1600566753376-12c8ab7fb75b": "waterfront-lanai",
    "photo-1613490493576-7fde63acd811": "project-bayfront",
    "photo-1600566753190-17f0baf2a6c3": "project-luxury-pool",
    "photo-1605146769289-440113cc3d00": "project-modern-villa",
    "photo-1512917774080-9991f1c4c750": "project-warm-interior",
    "photo-1600210492486-724fe5c67fb0": "project-architectural",
}

# Match a full HTML element's opening tag that contains a `style="..."` with
# background-image:url('https://images.unsplash.com/photo-XXX...').
ELEMENT_RE = re.compile(
    r"""(<[a-zA-Z][^<>]*?)                     # group1: opening up to space before style
        (\s+style\s*=\s*"(?P<style>[^"]*)")    # group 2 full style attr, style text in 'style'
        ([^<>]*/?>)                            # group 4: rest of the opening tag
    """,
    re.VERBOSE,
)

BG_RE = re.compile(
    r"""background-image\s*:\s*url\(
        (['"])https://images\.unsplash\.com/(?P<pid>photo-[a-z0-9-]+)\?[^)]*\1
        \)\s*;?""",
    re.VERBOSE | re.IGNORECASE,
)


def migrate_element(match: re.Match[str]) -> str:
    pre, full_style_attr, rest = match.group(1), match.group(2), match.group(4)
    style_text = match.group("style")

    # Already migrated? leave alone.
    if "data-img=" in pre or "data-img=" in rest:
        return match.group(0)

    bg_match = BG_RE.search(style_text)
    if not bg_match:
        return match.group(0)

    pid = bg_match.group("pid")
    key = KEYS.get(pid)
    if not key:
        # unknown photo — leave it untouched so we notice in a diff
        return match.group(0)

    # Strip the background-image:url(...) declaration (including trailing ;)
    cleaned = BG_RE.sub("", style_text).strip()
    cleaned = re.sub(r";\s*;", ";", cleaned).strip("; ").strip()

    if cleaned:
        new_style_attr = f' style="{cleaned}"'
    else:
        new_style_attr = ""  # drop the style attr altogether

    return f'{pre} data-img="{key}"{new_style_attr}{rest}'


SCRIPT_MAIN_RE = re.compile(
    r'(<script\s+src=["\']js/main\.js[^"\']*["\'][^>]*></script>)',
    re.IGNORECASE,
)
SCRIPT_IMAGES_TAG = '<script src="js/images.js?v=1"></script>'


def ensure_loader(html: str) -> str:
    if "js/images.js" in html:
        return html
    m = SCRIPT_MAIN_RE.search(html)
    if not m:
        return html  # page doesn't include main.js — skip (e.g. thank-you pre-main)
    return html[: m.start()] + SCRIPT_IMAGES_TAG + "\n" + html[m.start():]


def process(path: Path) -> tuple[int, int]:
    src = path.read_text(encoding="utf-8")
    # Count elements BEFORE so we can report what changed.
    before = len(BG_RE.findall(src))
    new = ELEMENT_RE.sub(migrate_element, src)
    new = ensure_loader(new)
    remaining = len(BG_RE.findall(new))
    if new != src:
        path.write_text(new, encoding="utf-8")
    return (before - remaining, remaining)


def main() -> int:
    html_files = sorted(ROOT.glob("*.html"))
    total_migrated = 0
    total_remaining = 0
    for p in html_files:
        migrated, remaining = process(p)
        total_migrated += migrated
        total_remaining += remaining
        tag = "ok" if remaining == 0 else "warn"
        print(f"[{tag}] {p.name}: migrated {migrated}, remaining {remaining}")
    print(f"\nTotal migrated: {total_migrated}, still inline: {total_remaining}")
    return 0 if total_remaining == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
