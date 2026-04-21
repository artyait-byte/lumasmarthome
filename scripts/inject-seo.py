#!/usr/bin/env python3
"""One-shot enrichment of every HTML page with SEO/OG/Twitter/JSON-LD tags.

Why a script and not a template engine?  The site is intentionally buildless
static HTML (requirement: deploy-ready, no toolchain).  A one-shot script keeps
per-page `<head>` consistent without introducing a framework.

Re-running is idempotent: the injected block is wrapped in a marker comment so
a second run replaces the block rather than duplicating it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://www.lumasmarthome.com"
OG_IMAGE = f"{SITE_URL}/assets/og-cover.svg"

MARK_START = "<!-- SEO:injected START -->"
MARK_END = "<!-- SEO:injected END -->"

# LocalBusiness JSON-LD only on the highest-intent pages.
PAGES_WITH_LD = {"index.html", "contact.html", "about.html"}

# Auxiliary pages that already declare their own `robots` directives (e.g.
# noindex) — we leave them alone to avoid conflicting meta tags.
SKIP_PAGES = {"thank-you.html"}

LOCAL_BUSINESS_LD = """
<script type=\"application/ld+json\">
{
  \"@context\": \"https://schema.org\",
  \"@type\": [\"LocalBusiness\", \"HomeAndConstructionBusiness\"],
  \"name\": \"LUMA Smart Home\",
  \"legalName\": \"LUMA Home Systems LLC\",
  \"description\": \"Residential technology studio on Florida's Gulf Coast — lighting, shading, security, audio, and network integration.\",
  \"url\": \"SITE_URL/\",
  \"logo\": \"SITE_URL/assets/logo.svg\",
  \"image\": \"SITE_URL/assets/og-cover.svg\",
  \"telephone\": \"+1-941-555-1234\",
  \"email\": \"hello@lumasmarthome.com\",
  \"priceRange\": \"$15,000 - $50,000+\",
  \"address\": {
    \"@type\": \"PostalAddress\",
    \"addressRegion\": \"FL\",
    \"addressCountry\": \"US\",
    \"addressLocality\": \"Sarasota\"
  },
  \"areaServed\": [
    {\"@type\": \"AdministrativeArea\", \"name\": \"Sarasota County, FL\"},
    {\"@type\": \"AdministrativeArea\", \"name\": \"Manatee County, FL\"},
    {\"@type\": \"AdministrativeArea\", \"name\": \"Charlotte County, FL\"},
    {\"@type\": \"AdministrativeArea\", \"name\": \"Lee County, FL\"},
    {\"@type\": \"AdministrativeArea\", \"name\": \"Collier County, FL\"}
  ],
  \"openingHoursSpecification\": [{
    \"@type\": \"OpeningHoursSpecification\",
    \"dayOfWeek\": [\"Monday\",\"Tuesday\",\"Wednesday\",\"Thursday\",\"Friday\",\"Saturday\"],
    \"opens\": \"09:00\",
    \"closes\": \"18:00\"
  }],
  \"sameAs\": []
}
</script>
""".strip().replace("SITE_URL", SITE_URL)


def build_head_block(html_path: Path, title: str, description: str) -> str:
    page_path = "" if html_path.name == "index.html" else html_path.name
    canonical = f"{SITE_URL}/{page_path}"

    lines = [
        MARK_START,
        f'<link rel="canonical" href="{canonical}" />',
        '<meta name="robots" content="index,follow,max-image-preview:large" />',
        '<meta name="theme-color" content="#1A6B60" />',
        '<meta name="author" content="LUMA Home Systems LLC" />',
        '<meta property="og:site_name" content="LUMA Smart Home" />',
        '<meta property="og:type" content="website" />',
        f'<meta property="og:title" content="{escape_attr(title)}" />',
        f'<meta property="og:description" content="{escape_attr(description)}" />',
        f'<meta property="og:url" content="{canonical}" />',
        f'<meta property="og:image" content="{OG_IMAGE}" />',
        '<meta property="og:locale" content="en_US" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        f'<meta name="twitter:title" content="{escape_attr(title)}" />',
        f'<meta name="twitter:description" content="{escape_attr(description)}" />',
        f'<meta name="twitter:image" content="{OG_IMAGE}" />',
        '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />',
        '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />',
    ]

    if html_path.name in PAGES_WITH_LD:
        lines.append(LOCAL_BUSINESS_LD)

    lines.append(MARK_END)
    return "\n".join(lines)


def escape_attr(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


TITLE_RE = re.compile(r"<title>([^<]*)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\'][^>]*/?>',
    re.IGNORECASE,
)
STYLES_LINK_RE = re.compile(
    r'(<link\s+rel=["\']stylesheet["\'][^>]*href=["\']css/styles\.css[^"\']*["\'][^>]*/?>)',
    re.IGNORECASE,
)
BLOCK_RE = re.compile(
    re.escape(MARK_START) + r".*?" + re.escape(MARK_END),
    re.DOTALL,
)


def process_file(path: Path) -> bool:
    if path.name in SKIP_PAGES:
        print(f"[skip] {path.name}: in SKIP_PAGES")
        return False

    src = path.read_text(encoding="utf-8")

    title_m = TITLE_RE.search(src)
    desc_m = DESC_RE.search(src)
    if not title_m:
        print(f"[skip] {path.name}: no <title>")
        return False
    title = title_m.group(1).strip()
    description = (desc_m.group(1).strip() if desc_m else title)

    block = build_head_block(path, title, description)

    if MARK_START in src:
        new = BLOCK_RE.sub(block, src)
    else:
        link_m = STYLES_LINK_RE.search(src)
        if not link_m:
            print(f"[skip] {path.name}: no stylesheet link anchor")
            return False
        injection = link_m.group(1) + "\n" + block
        new = src[: link_m.start()] + injection + src[link_m.end():]

    if new != src:
        path.write_text(new, encoding="utf-8")
        print(f"[ok]   {path.name}")
        return True
    print(f"[noop] {path.name}")
    return False


def main() -> int:
    html_files = sorted(p for p in ROOT.glob("*.html"))
    if not html_files:
        print("No HTML files found at repo root", file=sys.stderr)
        return 1
    changed = sum(1 for p in html_files if process_file(p))
    print(f"\nDone. Updated {changed} / {len(html_files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
