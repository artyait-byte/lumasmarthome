# LUMA Smart Home — SEO Playbook

Source of truth for the weekly SEO routine and anyone writing content for lumasmarthome.com.
Audit and competitor scan: 2026-09-30.

## Where content lives

- Content: `scripts/seo_content.py` (`SERVICES`, `CITIES`, `CITY_SERVICES`, `ARTICLES`, `NAP`).
- Build: `python3 scripts/generate-seo-pages.py` writes the HTML shells, `sitemap.xml`, `js/seo-data.js`. Never hand-edit generated HTML.
- Prod = `main`. Netlify site `lumasmarthome` builds from `main` automatically. Only the owner merges to `main`. We push a branch and open a PR.

## Hard rules

- Never invent reviews, star ratings, install counts, years in business, licence numbers or certifications. Certifications are not shown on the site (owner decision 2026-09-29).
- Case studies only from the real cases already on `/work`.
- Prices: only the ranges already published on `/budget` and the LUMA Care page. Don't create new prices; flag in the report if an article needs one.
- Brand canon: Lutron (RadioRA 3, HomeWorks, Ketra, Sivoia), Somfy, UniFi (Protect, Wi-Fi 6/7), Sonos, Control4, Savant, Josh.ai.
- English only. Voice: calm, specific, technical, no hype.

## Competitors on page 1 (Sarasota, Sept 2026)

| Competitor | Wins with | Weak spot |
|---|---|---|
| wickedsmarthomes.com | City homepage title, 8 brand pages (/partners/lutron), blog 1–2/week | Generic posts, templated city pages, no pricing or FAQ |
| sarasotasmarthomes.com | Exact-match domain, 13 service pages | Wix, undated blog, no city pages |
| skylinesmarthomes.us | City×service matrix, ~2,000 words, FAQ on every page | Template leftovers (placeholder text, wrong address), no blog |
| daisyco.com | National franchise, 3,500+ word market hub, neighbourhood lists | Not local, franchise voice |
| havensmart.com, advanced-esi.net, castle-protect.com, premieresav.com | Location pages, dealer tiers, FAQ | Thin or no blogs |

Directories (Yelp, Houzz, Angi, Thumbtack) take 2–4 page-1 slots on every local query, and the Map Pack is almost certainly shown. **The Google Business Profile matters as much as the site.**

## What page-1 winners have that we lack

1. Keyword in the H1. Our service H1s are slogans ("Your fixtures. Our controls."). Fix: "Lutron Lighting Control in Sarasota, FL" as H1, slogan as the subhead.
2. Depth: 1,200–2,500 words on money pages. Ours: 300–550 rendered words. Articles: 170–450 words.
3. FAQ blocks with FAQPage schema.
4. Brand pages: /lutron, /control4, /savant, /sonos, /unifi.
5. A verified Google Business Profile with reviews. Our `hasMap` is a search URL, not a CID.

## Keyword clusters

**A. Money pages** (existing service pages + Sarasota city×service pages)
smart home installation Sarasota · home automation Sarasota · home theater installation Sarasota · whole home audio Sarasota · lighting control Sarasota · UniFi / Wi-Fi installer Sarasota · security camera installation Sarasota · motorized shades Sarasota · permanent outdoor lighting Sarasota · smart home integrator Sarasota

**B. Cities** (existing: Sarasota, Bradenton, Lakewood Ranch, Venice, Siesta Key, Longboat Key, Anna Maria Island, Palmetto; to add: Osprey, Nokomis, Parrish, North Port, Punta Gorda, Englewood)
home automation Lakewood Ranch · smart home Longboat Key · smart home Siesta Key · home automation Venice FL · home automation Bradenton · home theater Lakewood Ranch

**C. Brands**
Lutron dealer Sarasota · Lutron RadioRA 3 installer · Lutron shades Sarasota · Somfy motorized shades Sarasota · Control4 dealer Sarasota · Savant dealer Sarasota · Josh.ai installer Florida · Sonos installer Sarasota

**D. Informational (the journal)**
home automation cost Florida · motorized shades cost · RadioRA 3 vs HomeWorks · Control4 vs Savant · home theater cost · smart home hurricane preparation · UniFi vs eero large homes · smart home for seasonal residents Florida

## Article queue (the routine takes the top unpublished item)

| # | Working title | Target keyword | Cluster |
|---|---|---|---|
| 1 | Hurricane-ready smart home: power, shades and remote eyes | smart home hurricane preparation Florida | D |
| 2 | What Lutron lighting control costs in a Sarasota home | Lutron RadioRA 3 cost | C/D |
| 3 | Running a seasonal home from up north | smart home for snowbirds Florida | D |
| 4 | Pre-wiring a new build in Lakewood Ranch | smart home pre-wire Lakewood Ranch | B |
| 5 | Lutron vs Somfy motorized shades in Gulf Coast sun | Lutron vs Somfy shades | C |
| 6 | Home theater cost in Sarasota, 2026 | home theater cost Sarasota | A/D |
| 7 | Wi-Fi in concrete-block homes and lanais | Wi-Fi dead zones Florida home | A |
| 8 | Control4 vs Savant vs Josh.ai on the Gulf Coast | Control4 vs Savant Florida | C |
| 9 | Longboat Key condos: automation within HOA rules | smart home condo Longboat Key | B |
| 10 | Outdoor audio that survives salt air | outdoor speakers coastal Florida | A |
| 11 | Wired PoE cameras vs Ring in Florida heat | wired security cameras vs wireless Florida | A |
| 12 | Smart lighting without opening walls | Lutron retrofit existing home | C |
| 13 | Permanent roofline lighting vs a seasonal install | permanent outdoor lighting cost Sarasota | A |
| 14 | UniFi vs eero for large homes | UniFi for large homes | C |
| 15 | What a smart-home service plan should cover | smart home maintenance plan | D |

Also expand the six thin articles already published to 1,200+ words, one per month, oldest first.

## Article standard

- 1,200–1,800 words. One H1 with the target keyword. 4–7 H2s. A short FAQ (3–5 Q&A) at the end.
- Local specifics: named neighbourhoods, Florida climate (sun, salt, humidity, hurricanes, seasonal occupancy), real product names.
- Title ≤ 60 chars, description 120–155 chars, unique.
- Links: 2–4 internal links out (service page + city page + /contact), and at least 2 existing pages link back (related map or body copy). No orphans.
- Schema: Article + BreadcrumbList (generator does this); FAQPage when the generator supports it.
- Every link in a `[text](page-id)` form must resolve to an existing page id.

## Site fix backlog (one-time, by priority)

1. Keyword-first H1 on the 8 service pages and the home page.
2. Google Business Profile: verify, set the CID in `NAP.mapsUrl` and schema `hasMap`, add `sameAs`.
3. Search Console + GA4 (or Plausible): confirm verification, submit the sitemap, watch indexing.
4. Depth on the service pages: 1,000+ words each, FAQ, process, price range, related cases.
5. FAQPage schema in the generator.
6. Brand pages: Lutron, Control4/Savant, Sonos, UniFi, Somfy.
7. Alt text on every image (about half on /lighting are empty).
8. New cities: Osprey, Nokomis, Parrish, North Port, Punta Gorda, Englewood.
9. Profiles with identical NAP: Houzz, Yelp, Angi, Thumbtack, BBB, Nextdoor, Apple Maps, Bing Places.
10. Links: Lutron / Somfy / Ubiquiti dealer locators, local designers and builders, Sarasota chamber, CEDIA.
