#!/usr/bin/env python3
"""Generate crawlable HTML shells + sitemap for the LUMA SPA.

Google currently indexes only `/` because the live site is a client-rendered
SPA: every other view lives behind `?p=` or is 301'd back to the homepage.
This script writes a real HTML file per public URL (unique title, description,
canonical, Open Graph, JSON-LD, and a noscript fallback with real links) so
crawlers can discover and index each page even before JavaScript runs.

Re-run after changing titles/descriptions in ROUTES, or after editing the
shared head chrome. The SPA itself lives in css/spa.css + js/app.js.
"""
from __future__ import annotations

import json
from pathlib import Path

from seo_content import NAP, extra_routes, geo_payload

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://lumasmarthome.com"
PHONE = NAP["telephone"]
EMAIL = NAP["email"]
MAPS_URL = NAP["mapsUrl"]

# id → public path, title, description, h1 (noscript), og image, sitemap priority
ROUTES: list[dict] = [
    {
        "id": "home",
        "path": "/",
        "file": "index.html",
        "title": "LUMA Smart Home | Lighting, Shades & AV in Sarasota, FL",
        "description": "LUMA designs and installs lighting control, motorized shades, security, audio, and Wi-Fi for fine homes on Florida's Gulf Coast. Serving Sarasota, Manatee, Charlotte, Lee & Collier Counties.",
        "h1": "A home that suits the way you live.",
        "og_image": "/assets/photos/waterfront-lanai.jpg",
        "priority": 1.0,
        "changefreq": "weekly",
        "kind": "home",
        "index": True,
    },
    {
        "id": "lighting",
        "path": "/lighting",
        "file": "lighting.html",
        "title": "Smart Lighting Control | Lutron & Ketra | LUMA Smart Home",
        "description": "Decorative and architectural lighting under one control spec. Lutron RadioRA 3, Ketra, warm-dim scenes, and designer keypads for Gulf Coast homes.",
        "h1": "Your fixtures. Our controls.",
        "og_image": "/assets/photos/lighting-scene.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Smart lighting control",
        "index": True,
    },
    {
        "id": "shading",
        "path": "/shading",
        "file": "shading.html",
        "title": "Motorized Window Shades | Somfy & Lutron Sivoia | LUMA",
        "description": "Motorized shades and drapery for Gulf Coast sun: solar screens, blackout, and Lutron Sivoia QS / Somfy, programmed to the hour of the day.",
        "h1": "Three layers of shade.",
        "og_image": "/assets/photos/hero-shading.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Motorized window treatments",
        "index": True,
    },
    {
        "id": "theaters",
        "path": "/theaters",
        "file": "theaters.html",
        "title": "Home Theater Design & Installation | Sarasota | LUMA",
        "description": "Dedicated cinema rooms designed from the walls out — acoustics, sightlines, calibration, and seating for Gulf Coast residences.",
        "h1": "Designed for sound, not retrofitted.",
        "og_image": "/assets/photos/hero-theater.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Home theater design and installation",
        "index": True,
    },
    {
        "id": "automation",
        "path": "/automation",
        "file": "automation.html",
        "title": "Home Automation | Control4, Lutron, Josh.ai | LUMA Sarasota",
        "description": "One-press scenes that move lighting, shades, climate, audio, and security together. Open platforms — Control4, Lutron, Josh.ai — for Gulf Coast homes.",
        "h1": "One press, the right state.",
        "og_image": "/assets/photos/hero-automation.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Home automation",
        "index": True,
    },
    {
        "id": "audio",
        "path": "/audio",
        "file": "audio.html",
        "title": "Whole-Home Audio & Video | Sonos, Sonance | LUMA Smart Home",
        "description": "Invisible in-ceiling, in-wall, and outdoor audio tuned to each room, with one app across every zone. Sarasota to Naples.",
        "h1": "Sound that fills the room, not the architecture.",
        "og_image": "/assets/photos/hero-audio-hifi.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Whole-home audio and video",
        "index": True,
    },
    {
        "id": "security",
        "path": "/security",
        "file": "security.html",
        "title": "Home Security & Cameras | UniFi Protect | LUMA Sarasota",
        "description": "On-premise UniFi Protect cameras with no monthly cloud fees. Property-walked camera placement, NVR on site, optional alarm monitoring.",
        "h1": "Your footage. Your property.",
        "og_image": "/assets/photos/hero-security-v2.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Security and surveillance",
        "index": True,
    },
    {
        "id": "networking",
        "path": "/networking",
        "file": "networking.html",
        "title": "Wi-Fi 6/7 & Structured Cabling | UniFi | LUMA Smart Home",
        "description": "Enterprise-grade UniFi Wi-Fi and Cat6A structured cabling designed before drywall. Wired spine first, wireless where it belongs.",
        "h1": "A network your home is built on, not bolted to.",
        "og_image": "/assets/photos/hero-networking.jpg",
        "priority": 0.9,
        "changefreq": "monthly",
        "kind": "service",
        "service_name": "Residential networking and Wi-Fi",
        "index": True,
    },
    {
        "id": "designers",
        "path": "/designers",
        "file": "designers.html",
        "title": "For Designers & Builders | Trade Partner | LUMA Smart Home",
        "description": "One low-voltage trade for lighting, shades, AV, security, and networking. Trade pricing, submittal packages, and site coordination for ASID, AIA, and GCs on the Gulf Coast.",
        "h1": "Built to fit your workflow.",
        "og_image": "/assets/photos/hero-designers-new.jpg",
        "priority": 0.8,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "work",
        "path": "/work",
        "file": "work.html",
        "title": "Our Work & Testimonials | Gulf Coast Homes | LUMA",
        "description": "Selected residences and five-star reviews from homeowners, architects, and builders along Florida's Gulf Coast.",
        "h1": "Homes where the hour takes care of itself.",
        "og_image": "/assets/photos/gulf-sunset.jpg",
        "priority": 0.8,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "about",
        "path": "/about",
        "file": "about.html",
        "title": "About LUMA Smart Home | Sarasota Residential Technology Studio",
        "description": "LUMA is a Sarasota residential technology studio. Open platforms, line-item proposals, and ongoing care from Bradenton to Naples.",
        "h1": "We build homes around the Gulf Coast hour.",
        "og_image": "/assets/photos/sarasota-marina.jpg",
        "priority": 0.8,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "contact",
        "path": "/contact",
        "file": "contact.html",
        "title": "Start a Project | Contact LUMA Smart Home | Sarasota, FL",
        "description": "Book a consultation with LUMA Smart Home. Serving Sarasota, Manatee, Charlotte, Lee, and Collier Counties. Call +1 (941) 217-1616.",
        "h1": "Start Your Project",
        "og_image": "/assets/photos/waterfront-lanai.jpg",
        "priority": 0.8,
        "changefreq": "monthly",
        "kind": "contact",
        "index": True,
    },
    {
        "id": "budget-calculator",
        "path": "/budget",
        "file": "budget.html",
        "title": "Smart Home Budget Calculator | Gulf Coast Ranges | LUMA",
        "description": "Honest budget ranges for Gulf Coast smart homes — lighting, shades, audio, theater, security, and networking. Walk through it like we would on site.",
        "h1": "Three tiers. One honest range.",
        "og_image": "/assets/photos/hero-modern-home.jpg",
        "priority": 0.7,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "support",
        "path": "/support",
        "file": "support.html",
        "title": "LUMA Care | Smart Home Support Plans | Sarasota, FL",
        "description": "Ongoing stewardship for the systems we installed — remote diagnostics, scene tweaks, and technicians who already know your rack. LUMA Care memberships.",
        "h1": "Keep the house effortless — long after install.",
        "og_image": "/assets/photos/networking-rack.jpg",
        "priority": 0.7,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "smart-home-demo",
        "path": "/demo",
        "file": "demo.html",
        "title": "Interactive 3D Smart Home Demo | LUMA Smart Home",
        "description": "Explore a cutaway Gulf Coast home and see lighting, shades, audio, security, and networking in place — with packages and pricing.",
        "h1": "See every system in place.",
        "og_image": "/assets/smart-home-demo/dollhouse-premium.jpg",
        "priority": 0.7,
        "changefreq": "monthly",
        "kind": "page",
        "index": True,
    },
    {
        "id": "case-spacious",
        "path": "/work/spacious-modern",
        "file": "work/spacious-modern.html",
        "title": "Spacious Modern | Naples Port Royal Case Study | LUMA",
        "description": "A 7,400 sq ft Naples home with Sonos whole-home audio, UniFi networking, and WattBox managed power — calm in the rooms, organized in the rack.",
        "h1": "Spacious Modern",
        "og_image": "/assets/photos/cases/spacious-modern/web-hero.jpg",
        "priority": 0.6,
        "changefreq": "yearly",
        "kind": "case",
        "index": True,
    },
    {
        "id": "case-urban",
        "path": "/work/urban-home",
        "file": "work/urban-home.html",
        "title": "Urban Home | Sarasota Bird Key Case Study | LUMA",
        "description": "A Bird Key waterfront residence built around Bowers & Wilkins, a 7.1.2 Atmos array, landscape audio, and a UniFi network.",
        "h1": "Urban Home",
        "og_image": "/assets/photos/cases/urban-home/web-hero.jpg",
        "priority": 0.6,
        "changefreq": "yearly",
        "kind": "case",
        "index": True,
    },
    {
        "id": "case-family",
        "path": "/work/huge-family-house",
        "file": "work/huge-family-house.html",
        "title": "Huge Family House | Bonita Bay Lighting Case Study | LUMA",
        "description": "A 9,000+ sq ft Bonita Bay residence with hidden cove LEDs, layered Lutron RadioRA 3 scenes, and designer keypads in every room.",
        "h1": "Huge Family House",
        "og_image": "/assets/photos/cases/huge-family/web-hero.jpg",
        "priority": 0.6,
        "changefreq": "yearly",
        "kind": "case",
        "index": True,
    },
    {
        "id": "case-modern",
        "path": "/work/modern-residence",
        "file": "work/modern-residence.html",
        "title": "Modern Residence | Tampa Bay AV Case Study | LUMA",
        "description": "Five independent AV zones in a hillside home — entertainment room, living room, and three outdoor patios — unified under one control layer.",
        "h1": "Modern Residence",
        "og_image": "/assets/photos/proj-mr-exterior.jpg",
        "priority": 0.6,
        "changefreq": "yearly",
        "kind": "case",
        "index": True,
    },
    {
        "id": "case-bighouse",
        "path": "/work/big-modern-house",
        "file": "work/big-modern-house.html",
        "title": "Big Modern House | Whole-Home Integration Case Study | LUMA",
        "description": "16 audio zones, 6 video zones, a Dolby Atmos theater, and 80+ speakers from a single processor — documented for long-term ownership.",
        "h1": "Big Modern House",
        "og_image": "/assets/photos/proj-bm-exterior.jpg",
        "priority": 0.6,
        "changefreq": "yearly",
        "kind": "case",
        "index": True,
    },
]

ROUTES.extend(extra_routes())

NAV_LINKS = [
    ("/", "Home"),
    ("/lighting", "Lighting"),
    ("/shading", "Shading"),
    ("/theaters", "Home theaters"),
    ("/audio", "Audio & video"),
    ("/security", "Security"),
    ("/networking", "Networking"),
    ("/automation", "Automation"),
    ("/service-areas", "Service areas"),
    ("/journal", "Journal"),
    ("/luma-smart-home-sarasota", "LUMA Smart Home Sarasota"),
    ("/work", "Our work"),
    ("/budget", "Budget calculator"),
    ("/designers", "For designers & builders"),
    ("/about", "About"),
    ("/support", "Customer support"),
    ("/demo", "3D demo"),
    ("/contact", "Contact"),
]

AREA_SERVED = [
    "Sarasota County, FL",
    "Manatee County, FL",
    "Charlotte County, FL",
    "Lee County, FL",
    "Collier County, FL",
]

AREA_CITIES = [
    "Sarasota, FL",
    "Bradenton, FL",
    "Lakewood Ranch, FL",
    "Venice, FL",
    "Siesta Key, FL",
    "Longboat Key, FL",
    "Fort Myers, FL",
    "Naples, FL",
]


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def abs_url(path: str) -> str:
    if path.startswith("http"):
        return path
    return SITE + path


def local_business_node() -> dict:
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": f"{SITE}/#business",
        "name": "LUMA Smart Home",
        "legalName": "LUMA Home Systems LLC",
        "url": f"{SITE}/",
        "telephone": PHONE,
        "email": EMAIL,
        "priceRange": "$$$",
        "image": abs_url("/assets/photos/waterfront-lanai.jpg"),
        "logo": abs_url("/assets/favicon.svg"),
        "address": {
            "@type": "PostalAddress",
            "addressLocality": NAP["locality"],
            "addressRegion": NAP["region"],
            "addressCountry": NAP["country"],
        },
        "hasMap": MAPS_URL,
        "areaServed": [
            {"@type": "AdministrativeArea", "name": name} for name in AREA_SERVED
        ]
        + [{"@type": "City", "name": name} for name in AREA_CITIES],
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                ],
                "opens": "09:00",
                "closes": "18:00",
            }
        ],
    }


def crumb_list(elements: list[tuple[str, str]]) -> dict:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": abs_url(path),
            }
            for i, (name, path) in enumerate(elements, start=1)
        ],
    }


def json_ld(route: dict) -> str:
    page_url = abs_url(route["path"])
    kind = route.get("kind")
    graph: list[dict] = [local_business_node()]
    graph.append(
        {
            "@type": "WebSite",
            "@id": f"{SITE}/#website",
            "url": f"{SITE}/",
            "name": "LUMA Smart Home",
            "publisher": {"@id": f"{SITE}/#business"},
            "inLanguage": "en-US",
        }
    )
    webpage_type = "WebPage"
    if kind == "article":
        webpage_type = ["WebPage", "Article"]
    elif kind == "contact":
        webpage_type = "ContactPage"
    elif kind == "brand":
        webpage_type = "AboutPage"
    webpage: dict = {
        "@type": webpage_type,
        "@id": f"{page_url}#webpage",
        "url": page_url,
        "name": route["title"],
        "description": route["description"],
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#business"},
        "inLanguage": "en-US",
    }
    if route["path"] != "/":
        crumbs: list[tuple[str, str]] = [("Home", "/")]
        if kind in ("areas-hub", "city", "city-service"):
            crumbs.append(("Service Areas", "/service-areas"))
            if kind == "city":
                crumbs.append((route.get("city_name") or route["h1"], route["path"]))
            elif kind == "city-service":
                crumbs.append(
                    (route.get("city_name") or "City", f"/service-areas/{route['city']}")
                )
                crumbs.append((route["h1"], route["path"]))
        elif kind in ("journal-hub", "article"):
            crumbs.append(("Journal", "/journal"))
            if kind == "article":
                crumbs.append((route["h1"], route["path"]))
        elif kind == "brand":
            crumbs.append((route["h1"], route["path"]))
        else:
            crumbs.append((route["h1"], route["path"]))
        webpage["breadcrumb"] = crumb_list(crumbs)
    graph.append(webpage)

    if kind == "service":
        graph.append(
            {
                "@type": "Service",
                "name": route.get("service_name") or route["h1"],
                "description": route["description"],
                "provider": {"@id": f"{SITE}/#business"},
                "areaServed": [
                    {"@type": "AdministrativeArea", "name": name}
                    for name in AREA_SERVED
                ],
                "url": page_url,
            }
        )
    if kind == "city-service":
        graph.append(
            {
                "@type": "Service",
                "name": f"{route.get('service_name') or route['h1']} in {route.get('city_name')}",
                "description": route["description"],
                "provider": {"@id": f"{SITE}/#business"},
                "areaServed": {
                    "@type": "City",
                    "name": f"{route.get('city_name')}, FL",
                },
                "url": page_url,
            }
        )
    if kind == "article":
        graph.append(
            {
                "@type": "Article",
                "headline": route["h1"],
                "description": route["description"],
                "image": abs_url(route["og_image"]),
                "datePublished": route.get("datePublished", "2026-08-24"),
                "dateModified": route.get("datePublished", "2026-08-24"),
                "author": {"@id": f"{SITE}/#business"},
                "publisher": {"@id": f"{SITE}/#business"},
                "mainEntityOfPage": {"@id": f"{page_url}#webpage"},
                "inLanguage": "en-US",
            }
        )
    if kind == "brand":
        graph.append(
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "Is LUMA Smart Home the same as luma.com?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "No. luma.com is an events platform. LUMA Smart Home (lumasmarthome.com) is a Sarasota, Florida residential technology studio.",
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Is this Luma AI or Luma Labs?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "No. Luma AI (lumalabs.ai) builds generative video tools. LUMA Smart Home installs lighting, shades, audio, security, and Wi-Fi in Gulf Coast homes.",
                        },
                    },
                    {
                        "@type": "Question",
                        "name": "Do you sell Snap One Luma cameras?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "No. Snap One's Luma is a camera hardware line. When LUMA Smart Home specs cameras, we use on-premise UniFi Protect.",
                        },
                    },
                ],
            }
        )
    payload = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def noscript_block(route: dict) -> str:
    links = "\n".join(
        f'      <li><a href="{esc(href)}">{esc(label)}</a></li>'
        for href, label in NAV_LINKS
    )
    extra = ""
    for para in route.get("paragraphs") or []:
        extra += f"    <p>{esc(para)}</p>\n"
    nap = (
        f'    <p><a href="{esc(MAPS_URL)}" rel="noopener">{esc(NAP["mapsLabel"])}</a></p>\n'
    )
    return f"""<noscript>
  <header class="seo-noscript">
    <p><a href="/">LUMA Smart Home</a> · Sarasota, FL · {esc(NAP["telephoneDisplay"])} · {esc(EMAIL)}</p>
    <h1>{esc(route["h1"])}</h1>
    <p>{esc(route["description"])}</p>
{extra}{nap}    <nav aria-label="Site">
      <ul>
{links}
      </ul>
    </nav>
  </header>
</noscript>"""


def head_for(route: dict) -> str:
    canonical = abs_url(route["path"])
    og_image = abs_url(route["og_image"])
    robots = "index,follow,max-image-preview:large" if route.get("index", True) else "noindex,follow"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(route["title"])}</title>
<meta name="description" content="{esc(route["description"])}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1B1A28">
<meta name="author" content="LUMA Home Systems LLC">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="Sarasota">
<meta property="og:site_name" content="LUMA Smart Home">
<meta property="og:type" content="{'article' if route.get('kind') == 'article' else 'website'}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(route["title"])}">
<meta property="og:description" content="{esc(route["description"])}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(og_image)}">
<meta property="og:image:alt" content="{esc(route["h1"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(route["title"])}">
<meta name="twitter:description" content="{esc(route["description"])}">
<meta name="twitter:image" content="{esc(og_image)}">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/spa.css">
<script type="application/ld+json">
{json_ld(route)}
</script>
<script src="https://unpkg.com/react@18.3.1/umd/react.development.js" integrity="sha384-hD6/rw4ppMLGNu3tX5cjIb+uRZ7UkRJ6BPkLpg4hAu/6onKUg4lLsHAs9EBPT82L" crossorigin="anonymous"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js" integrity="sha384-u6aeetuaXnQ38mYT8rp6sbXaQe3NL9t+IBXmnYxwkUI2Hw4bsp2Wvmx4yRQF1uAm" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@babel/standalone@7.29.0/babel.min.js" integrity="sha384-m08KidiNqLdpJqLq95G/LEi8Qvjl/xUYll3QILypMoQ65QorJ9Lvtp2RXYGBFj1y" crossorigin="anonymous"></script>
<script src="/js/seo-data.js"></script>
</head>
<body>
{noscript_block(route)}
<div id="root"></div>
<script>window.__LUMA_PAGE={json.dumps(route["id"])};</script>
<script type="text/babel" data-presets="react" src="/js/app.js"></script>
</body>
</html>
"""


def write_seo_data() -> None:
    payload = {
        "siteUrl": SITE,
        "routes": {
            r["id"]: {
                "id": r["id"],
                "path": r["path"],
                "title": r["title"],
                "description": r["description"],
                "kind": r.get("kind"),
                "city": r.get("city"),
                "service": r.get("service"),
                "h1": r.get("h1"),
            }
            for r in ROUTES
        },
    }
    # Also map legacy aliases so old ?p= and hash URLs still resolve.
    aliases = {
        "budget": "budget-calculator",
        "projects": "work",
        "our-work": "work",
        "serviceplans": "support",
        "service-plans": "support",
        "customer-support": "support",
        "smart-home-demo": "smart-home-demo",
        "builders": "designers",
    }
    text = (
        "/* Generated by scripts/generate-seo-pages.py — do not edit by hand. */\n"
        "window.LUMA_SEO = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n"
        "window.LUMA_SEO_ALIASES = "
        + json.dumps(aliases, ensure_ascii=False)
        + ";\n"
        "window.LUMA_GEO = "
        + json.dumps(geo_payload(), ensure_ascii=False, indent=2)
        + ";\n"
    )
    (ROOT / "js" / "seo-data.js").write_text(text, encoding="utf-8")


def write_sitemap() -> None:
    urls = []
    for r in ROUTES:
        if not r.get("index", True):
            continue
        urls.append(
            "  <url>\n"
            f"    <loc>{esc(abs_url(r['path']))}</loc>\n"
            f"    <changefreq>{esc(r['changefreq'])}</changefreq>\n"
            f"    <priority>{r['priority']:.1f}</priority>\n"
            "  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /_archive/\n"
        "Disallow: /thank-you.html\n"
        "Disallow: /brochure.html\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )


def write_pages() -> None:
    # Shared SPA is loaded from /js/app.js so each HTML shell stays small.
    # Babel standalone fetches that file (connect-src 'self' in netlify.toml).
    for r in ROUTES:
        dest = ROOT / r["file"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(head_for(r), encoding="utf-8")
        print(f"[ok] {r['file']}  →  {r['path']}")


def main() -> None:
    write_seo_data()
    write_pages()
    write_sitemap()
    write_robots()
    print(f"[ok] wrote {len(ROUTES)} HTML shells, sitemap.xml, robots.txt, js/seo-data.js")


if __name__ == "__main__":
    main()
