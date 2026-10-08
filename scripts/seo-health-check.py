#!/usr/bin/env python3
"""Technical SEO health check for lumasmarthome.com (or a local/preview base URL).

Runs the "why Google doesn't see my site" checklist against every URL in the
sitemap and prints PASS / WARN / FAIL lines. The weekly SEO routine runs this
before and after its changes; any FAIL goes to the top of the report.

    python3 scripts/seo-health-check.py                      # production
    python3 scripts/seo-health-check.py http://localhost:8000 # local build

Checks: HTTPS + www/http redirects, robots.txt, sitemap, noindex (meta and
X-Robots-Tag), canonical (self, no localhost), title/description length,
one H1, JSON-LD parses, og:image, real 404 (no soft 404), hash links,
broken internal links, Googlebot not challenged, raw-HTML content depth
(client-side rendering risk), image weight/format in the repo.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from html import unescape
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://lumasmarthome.com").rstrip("/")
PROD = BASE.startswith("https://lumasmarthome.com")
GOOGLEBOT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
MIN_RAW_WORDS = 600  # money pages should carry real copy in the HTML itself

fails = warns = 0


def report(level: str, msg: str) -> None:
    global fails, warns
    fails += level == "FAIL"
    warns += level == "WARN"
    print(f"{level:4}  {msg}")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch(url: str, method: str = "GET", follow: bool = True):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": GOOGLEBOT})
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(req, timeout=20) as r:
            body = r.read().decode("utf8", "ignore") if method == "GET" else ""
            return r.status, {k.lower(): v for k, v in r.headers.items()}, body
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}, ""
    except Exception as e:  # network, TLS
        return 0, {}, str(e)


def site_checks() -> None:
    if PROD:
        for src in ("http://lumasmarthome.com/", "https://www.lumasmarthome.com/"):
            st, h, _ = fetch(src, "HEAD", follow=False)
            loc = h.get("location", "")
            ok = st in (301, 308) and loc.startswith("https://lumasmarthome.com")
            report("PASS" if ok else "FAIL", f"redirect {src} -> {st} {loc}")
        st, h, _ = fetch(BASE + "/", "HEAD")
        report("PASS" if "strict-transport-security" in h else "WARN", "HSTS header")
        if "cf-mitigated" in h or h.get("server", "").lower() == "cloudflare":
            report("WARN", "Cloudflare in front: confirm Googlebot is not challenged")

    st, _, robots = fetch(BASE + "/robots.txt")
    if st != 200:
        report("FAIL", f"robots.txt -> {st}")
    else:
        blocked = re.search(r"^Disallow:\s*/\s*$", robots, re.M)
        report("FAIL" if blocked else "PASS", "robots.txt does not block the site")
        report("PASS" if "Sitemap:" in robots else "WARN", "robots.txt lists the sitemap")

    st, _, body = fetch(BASE + "/definitely-not-a-page-404-check")
    report("PASS" if st == 404 else "FAIL", f"unknown URL returns {st} (soft-404 check)")


def page_checks() -> None:
    st, _, sm = fetch(BASE + "/sitemap.xml")
    if st != 200:
        report("FAIL", f"sitemap.xml -> {st}")
        return
    urls = re.findall(r"<loc>(.*?)</loc>", sm)
    report("PASS", f"sitemap.xml: {len(urls)} URLs")
    titles: dict[str, str] = {}
    links: set[str] = set()
    thin = []
    for prod_url in urls:
        path = urlparse(prod_url).path or "/"
        url = BASE + path
        st, h, t = fetch(url)
        tag = path
        if st != 200:
            report("FAIL", f"{tag}: HTTP {st}")
            continue
        robots_meta = re.search(r'<meta name="robots" content="([^"]*)"', t)
        if "noindex" in h.get("x-robots-tag", "") or (robots_meta and "noindex" in robots_meta.group(1)):
            report("FAIL", f"{tag}: noindex")
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', t)
        canon = canon.group(1) if canon else ""
        if not canon:
            report("FAIL", f"{tag}: no canonical")
        elif "localhost" in canon or "127.0.0.1" in canon or canon != prod_url:
            report("FAIL", f"{tag}: canonical -> {canon}")
        title = re.search(r"<title>(.*?)</title>", t, re.S)
        title = unescape(title.group(1).strip()) if title else ""
        if not title or len(title) > 60:
            report("WARN", f"{tag}: title {len(title)} chars")
        if title in titles:
            report("FAIL", f"{tag}: duplicate title with {titles[title]}")
        titles[title] = tag
        desc = re.search(r'<meta name="description" content="([^"]*)"', t)
        dlen = len(unescape(desc.group(1))) if desc else 0
        if not 110 <= dlen <= 160:
            report("WARN", f"{tag}: description {dlen} chars")
        h1 = len(re.findall(r"<h1[\s>]", t))
        if h1 != 1:
            report("FAIL", f"{tag}: {h1} H1 tags")
        if "og:image" not in t:
            report("WARN", f"{tag}: no og:image")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try:
                json.loads(block)
            except ValueError:
                report("FAIL", f"{tag}: JSON-LD does not parse")
        if re.search(r'href="[^"]*#/', t):
            report("FAIL", f"{tag}: hash-route links (#/...) in HTML")
        raw = re.sub(r"<script.*?</script>|<style.*?</style>|<noscript>|</noscript>", " ", t, flags=re.S)
        raw = re.sub(r"<nav.*?</nav>", " ", raw, flags=re.S)
        words = len(re.sub(r"<[^>]+>", " ", raw).split())
        if words < MIN_RAW_WORDS:
            thin.append((tag, words))
        for a in re.findall(r'href="([^"#?]+)', t):
            a = urljoin(url, a)
            if a.startswith(BASE):
                links.add(a)
    if thin:
        report("WARN", f"{len(thin)}/{len(urls)} pages have < {MIN_RAW_WORDS} words in raw HTML "
                       f"(content depends on JS rendering): " + ", ".join(f"{p}={w}" for p, w in thin[:8]) + " ...")
    asset_ext = (".css", ".js", ".png", ".jpg", ".jpeg", ".webp", ".svg", ".ico", ".woff2", ".mp4", ".webm", ".pdf")
    broken = []
    for a in sorted(links):
        if a.lower().endswith(asset_ext):
            continue
        st, _, _ = fetch(a, "HEAD")
        if st >= 400 or st == 0:
            broken.append(f"{st} {a}")
    report("FAIL" if broken else "PASS", f"internal links: {len(links)} checked, {len(broken)} broken")
    for b in broken:
        print("        " + b)


def repo_checks() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf8", errors="ignore")
    if "babel" in index.lower() and 'type="text/babel"' in index:
        report("WARN", "JSX is compiled in the browser by @babel/standalone: slow LCP/TBT and "
                       "Google must render JS to see content. Precompile app.js at build time.")
    imgs = [p for p in (ROOT / "assets").rglob("*") if p.suffix.lower() in (".jpg", ".jpeg", ".png")]
    modern = [p for p in (ROOT / "assets").rglob("*") if p.suffix.lower() in (".webp", ".avif")]
    heavy = [p for p in imgs if p.stat().st_size > 400_000]
    report("WARN" if heavy else "PASS", f"images: {len(imgs)} jpg/png, {len(modern)} webp/avif, {len(heavy)} over 400 KB")


if __name__ == "__main__":
    print(f"SEO health check: {BASE}\n")
    site_checks()
    page_checks()
    repo_checks()
    print(f"\n{fails} FAIL, {warns} WARN")
    sys.exit(1 if fails else 0)
