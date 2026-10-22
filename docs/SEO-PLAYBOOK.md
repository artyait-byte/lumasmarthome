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
- Prices: only the ranges already published on `/budget` and the LUMA Care page, plus the owner-approved camera packages (2026-10-22: Home 4 from $2,900, Office 8 from $5,900, Business Pro 12+ from $12,900, all + tax; source of truth `CAMERA_PACKAGES` in `js/app.js`). Don't create new prices; flag in the report if an article needs one.
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

## Six-month plan: Sarasota top 10 by 2027-04-15

Written 2026-10-15 from the Search Console export of 2026-10-13 (last 3 months) and the live site.

### Baseline (GSC, 2026-07-15 → 2026-10-13)

- 2 clicks, ~450 impressions, average position ~42. Impressions only start 2026-09-29, so the site is about two weeks old in Google's eyes.
- 44 of 50 known URLs indexed. Not indexed: http/www variants (correct), `/networking.html` and `/service-areas/palmetto` (canonical report, validation started 2026-10-15), one new article (indexing requested).
- Desktop 367 impressions, mobile 81. US 428 of 450.
- Head terms are far away: smart home installation sarasota 37, smart home sarasota 61, home automation sarasota fl 45, home theater sarasota 44, smart home company sarasota 58.
- Already close to page 1: house/home security cameras sarasota fl 7–13, home theater longboat key 7.5, smart home installation venice 9, lutron homeworks near me 9, lutron integrator fl 5, longboat key fl outdoor motorized shades 7, longboat key fl motorized window treatments 14.
- Largest demand cluster by count: motorized shades × place × type (Longboat Key, Siesta Key, south Sarasota, Palmetto, Whitfield, Ridgewood Heights; exterior, blackout, roman, roller, blinds). Last 7 days the top queries were all Longboat Key and Siesta Key shades.
- Noise to ignore: Sonoma, Santa Monica, Gulf Shores AL, Alamo, Boca, Tampa — national Lutron/Sonance terms where we have no local intent.

### Problems found

1. **Cannibalization.** "smart home installation sarasota" was split across 10 URLs (city hub, 6 city×service pages, About), none of them the home page, because the home title did not contain the phrase. Lutron terms split between `/service-areas/sarasota/lighting`, `/lighting` and the Lutron article; "sonance whole home audio florida" between `/audio` and `/service-areas/sarasota/audio`.
2. Slogan H1s on the 8 service pages (backlog #1).
3. Thin money pages: 35 of 48 under 600 words.
4. No page for the demand Google is already sending: Longboat Key and Siesta Key shades.
5. Schema and site text named a company that does not exist (LUMA Home Systems LLC) and claimed a contractor licence. Fixed: Tegra-Media LLC, licensed partner wording.
6. Off-site: no verified Google Business Profile, no reviews, Yelp phone and hours differ from the site, almost no backlinks.

### One keyword, one page (do not create a second page for the same phrase)

| Primary phrase | Page |
|---|---|
| smart home installation sarasota · smart home sarasota · smart home company sarasota | `/` (home) |
| smart home projects by neighborhood (Bird Key, Lido, Palmer Ranch…) | `/service-areas/sarasota` |
| lutron installer sarasota · lutron lighting sarasota | `/service-areas/sarasota/lighting` |
| lighting control systems (regional, brand detail) | `/lighting` |
| motorized shades sarasota · electric blinds sarasota · exterior shades sarasota | `/service-areas/sarasota/shading` |
| motorized shades longboat key (exterior, blackout, window treatments) | `/service-areas/longboat-key/shading` |
| motorized shades siesta key (blinds, roller, roman, screens) | `/service-areas/siesta-key/shading` |
| security camera installation sarasota · house security cameras sarasota fl | `/service-areas/sarasota/security` |
| home automation sarasota fl | `/service-areas/sarasota/automation` |
| office / business security cameras sarasota fl · office surveillance camera system sarasota · business security camera systems sarasota | `/service-areas/sarasota/business-security` (hub for the business section) |
| commercial security cameras bradenton · office surveillance camera system bradenton fl | `/service-areas/bradenton/business-security` |
| retail store security cameras sarasota | `/service-areas/sarasota/retail-security-cameras` |
| restaurant security cameras sarasota | `/service-areas/sarasota/restaurant-security-cameras` |
| warehouse security cameras sarasota | `/service-areas/sarasota/warehouse-security-cameras` |
| hoa / condo security cameras sarasota | `/service-areas/sarasota/hoa-security-cameras` |
| whole home audio sarasota · sonance sarasota | `/service-areas/sarasota/audio` |
| home theater sarasota · home theater installation sarasota | `/service-areas/sarasota/theaters` |
| smart home venice / bradenton / lakewood ranch / longboat key / siesta key | the city page |
| RadioRA 3 vs HomeWorks, costs, comparisons | journal articles |

Internal links use these phrases as anchor text and point at the page in the right column. Service pages (`/lighting`, `/shading`…) carry the regional H1 "· Sarasota & Manatee" and link down to the city×service page.

### Keyword targets for the Sarasota top 10 (GSC 2026-10-13, last 3 months)

Position = average position in Search Console (impressions in brackets). "—" = no impressions yet. Priority: P1 = within reach this quarter (pos ≤ 25 or new page with a weak SERP), P2 = needs depth + GBP, P3 = needs reviews and links. Recheck every month on the Tuesday routine and update this table.

| Keyword | Page | GSC pos (impr) | Cluster | Priority |
|---|---|---|---|---|
| house security cameras sarasota fl | `/service-areas/sarasota/security` | 11.8 (6) | A cameras | P1 |
| house surveillance camera(s) sarasota fl | `/service-areas/sarasota/security` | 11–13.7 (7) | A cameras | P1 |
| home security camera sarasota fl | `/service-areas/sarasota/security` | 10 (2) | A cameras | P1 |
| security camera sarasota fl · surveillance cameras sarasota fl | `/service-areas/sarasota/security` | 11–12 (2) | A cameras | P1 |
| security camera installation sarasota (fl) | `/service-areas/sarasota/security` | 64 (2) | A cameras | P2 |
| security cameras sarasota | `/service-areas/sarasota/security` | 30 (3) | A cameras | P2 |
| home security sarasota fl | `/service-areas/sarasota/security` | 23 (5) | A cameras | P2 |
| video doorbell camera sarasota · doorbell camera sarasota | `/service-areas/sarasota/security` | 31.5–74 (3) | A cameras | P3 |
| office security camera(s) system(s) sarasota fl | `/service-areas/sarasota/business-security` | 12–17 (9) | A business cameras | P1 |
| office surveillance camera system(s) sarasota fl | `/service-areas/sarasota/business-security` | 12–23 (8) | A business cameras | P1 |
| business security camera systems sarasota | `/service-areas/sarasota/business-security` | — | A business cameras | P1 |
| security cameras supplier sarasota fl | `/service-areas/sarasota/business-security` | 11 (1) | A business cameras | P2 |
| commercial security cameras bradenton · office surveillance camera system bradenton fl | `/service-areas/bradenton/business-security` | 25 (2) | A business cameras | P1 |
| retail store security cameras sarasota | `/service-areas/sarasota/retail-security-cameras` | — | A business cameras | P2 |
| restaurant security cameras sarasota | `/service-areas/sarasota/restaurant-security-cameras` | — | A business cameras | P2 |
| warehouse security cameras sarasota | `/service-areas/sarasota/warehouse-security-cameras` | — | A business cameras | P2 |
| hoa / condo security cameras sarasota | `/service-areas/sarasota/hoa-security-cameras` | — | A business cameras | P2 |
| smart home installation sarasota | `/` | 37 (14) | A general | P2 |
| smart home sarasota · smart house sarasota | `/` | 61 (6) | A general | P3 |
| smart home company sarasota | `/` | 58.5 (4) | A general | P3 |
| smart home integration sarasota · smart home price sarasota fl | `/` | — | A general | P3 |
| home automation sarasota fl | `/service-areas/sarasota/automation` | 45 (5) | A general | P2 |
| home automation system bradenton fl | `/service-areas/bradenton` | 32 (5) | B cities | P2 |
| smart home installation venice | `/service-areas/venice` | 9.2 (5) | B cities | P1 |
| motorized shades sarasota · motorized blinds sarasota · roller shades sarasota | `/service-areas/sarasota/shading` | ~55 (cluster) | A shades | P2 |
| motorized shades longboat key (exterior, blackout, window treatments) | `/service-areas/longboat-key/shading` | 7–14 | A shades | P1 |
| motorized shades siesta key (blinds, roller, screens) | `/service-areas/siesta-key/shading` | ~50 (cluster) | A shades | P1 |
| lutron installer sarasota · lutron sarasota | `/service-areas/sarasota/lighting` | ~55 (cluster) | C brands | P2 |
| lutron homeworks near me · lutron integrator fl | `/lighting` | 5–9 | C brands | P1 |
| home theater sarasota · home theater installation sarasota | `/service-areas/sarasota/theaters` | 44 (4) | A theater | P2 |
| home theater longboat key | `/service-areas/longboat-key` | 7.5 (4) | B cities | P1 |
| sonance whole home audio florida · whole home audio sarasota | `/service-areas/sarasota/audio` | 30 (16) | A audio | P2 |
| permanent outdoor lighting sarasota | `/permanent-lighting` | — | A lighting | P3 |

Ignore: Sonoma, Santa Monica, Gulf Shores, Tampa, LA and other out-of-area queries (weighted avg ~57); national brand terms with no local intent.

### Done on 2026-10-15 (branch claude/seo-keyword-plan)

- Home title "Smart Home Installation Sarasota, FL | LUMA Smart Home" and a matching description.
- Sarasota city page re-aimed at neighbourhoods, with a link up to the home page as "smart home installation in Sarasota".
- Keyword H1 on 8 service pages (the slogan stays as the visible headline; the H1 is set as the kicker line, same look as before).
- Sections + FAQ (FAQPage schema) on Sarasota lighting, shading, security and automation: 440–490 → 740–850 words.
- New pages: `/service-areas/longboat-key/shading`, `/service-areas/siesta-key/shading`, linked from the shades article, the Sarasota shades page and their city pages.
- Security page title and H1 moved to "security camera installation".
- Legal name fixed site-wide.

### Done on 2026-10-15 (branch claude/business-cameras)

- Business cameras section, hub = `/service-areas/sarasota/business-security` (URL kept, it already ranks 12–17): 700 → ~1,460 words, camera-by-position table with current UniFi models (G6 Dome / Mini Dome / Turret / Pro Bullet / PTZ / 180, AI Theta Pro, AI LPR), recorder sizing table (UNVR Instant / UNVR / UNVR Pro / UNVR G2 Pro), links to business-type pages, 8 FAQ.
- New pages (unique layouts and FAQ each, 890–970 words): `/service-areas/bradenton/business-security`, `/service-areas/sarasota/retail-security-cameras`, `…/restaurant-security-cameras`, `…/warehouse-security-cameras`, `…/hoa-security-cameras`. Medical/dental and marinas are a line on the hub only (weak search demand).
- Links in: `/security` "For offices and shops" band lists all five, new band on `/networking`, Sarasota and Bradenton city hubs, related links between all business pages.
- After merge, request indexing in this order: the hub, Bradenton, retail, restaurant, warehouse, HOA, then `/security` and `/networking` (changed).
- Not done, owner to confirm: UniFi Access door control (not on the pages), prices (none on the pages), credential badges on `/security` and `/networking`.

### Done on 2026-10-22 (branch claude/camera-packages)

Conversion pass on the camera pages. The unmerged `claude/business-cameras` work (above) is carried on this branch, rebuilt on top of the canonical guard (PR #16), so merging this branch merges both.

- **Pages:** `/security`, `/service-areas/sarasota/security`, `/service-areas/sarasota/business-security`, `/service-areas/bradenton/business-security`, `/service-areas/sarasota/{retail,restaurant,warehouse,hoa}-security-cameras`. A row is a camera page when it has `"camera"` in `CITY_SERVICES` (`home`, `business` or `pro` decides which package leads).
- **Packages block** (owner-approved, "from" prices, "+ tax"):
  - Home 4 — from $2,900: 4 UniFi G6 turret/bullet, UNVR, 8 TB drive, PoE switch, installation and app setup.
  - Office 8 — from $5,900: 6 G6 turret/bullet + 2 G6 Dome (entrance, register), UNVR Pro, 2 drives, cameras on their own network segment.
  - Business Pro 12+ — from $12,900: G6 Pro vandal-resistant, AI LPR with an overview camera, G6 180, UNVR G2 Pro, 4 drives.
  - Every package: no monthly subscription, footage on site, NDAA-compliant UniFi hardware, work carried out with our Florida-licensed low-voltage partner, final fixed price after the free walk. Options: video doorbell, extra cameras, plate camera for gates, alarm.
  - Lead card: Home 4 on `/security` and `/service-areas/sarasota/security`; Office 8 on the business hub, Bradenton, retail, restaurant; Business Pro on warehouse and HOA. No LUMA Care plan, no warranty terms, reviews, install counts or certifications.
- **Inline form** "Free camera plan in 48 hours" on every camera page: name, phone, email (optional), home or business, number of cameras, city, message, plus hidden `page` and `package`. Netlify form name `camera-quote` (hidden twin written by `netlify_form()` in `scripts/generate-seo-pages.py`). Thank-you state in place. Picking a package card fills the form.
- **Mobile call bar** (under 768 px, camera pages only): "Call (941) 431-4640" + "Get a free plan". The "Talk to LUMA" launcher is lifted above the bar; the corner lead card does not auto-open on these pages.
- **Money questions** in copy and FAQ (FAQPage schema is built from the visible FAQ): cost (points to the packages), how many cameras, monthly fee (no), audio (off by default, Fla. Stat. 934.03). Each page words the cost question differently.
- **Keywords:** `/service-areas/sarasota/security` keeps "security camera installation Sarasota FL" (title, H1) and adds home / house security cameras in H2s ("Home security camera packages in Sarasota", "How many cameras a Sarasota house needs", "How we install house security cameras"). `/service-areas/sarasota/business-security` keeps office / business security camera systems ("Business security camera system packages in Sarasota"). Cross-links: "Office and business security camera systems in Sarasota" → hub, "Home and house security cameras in Sarasota" → `/service-areas/sarasota/security`.
- **Photos:** 4 Unsplash-licence stock photos in `/assets/photos/stock/` (sources and authors in `assets/photos/stock/SOURCES.md`), alt text only, never captioned as our installs.
- **Netlify, blocker:** on 2026-10-22 the site had form detection OFF (`processing_settings.ignore_html_forms: true`, no forms registered, not even `contact`). Until the owner turns on Forms → "Enable form detection" and redeploys, neither the contact form, the lead card nor `camera-quote` is stored; visitors see the "did not go through, please call" message. After enabling: check `contact` and `camera-quote` appear and set notifications to hello@lumasmarthome.com.
- **Request indexing after merge, in this order:** `/service-areas/sarasota/security`, `/service-areas/sarasota/business-security`, `/security`, `/service-areas/bradenton/business-security`, `/service-areas/sarasota/retail-security-cameras`, `/service-areas/sarasota/restaurant-security-cameras`, `/service-areas/sarasota/warehouse-security-cameras`, `/service-areas/sarasota/hoa-security-cameras`, then `/networking`, `/service-areas/sarasota`, `/service-areas/bradenton` (changed links).
- **Owner to confirm:** "Installation and app setup" is listed on all three cards (the brief had it on Home 4 only); `/security` still has an install photo strip ("What a LUMA install looks like", e.g. "Dock camera on Sarasota Bay") — if those are not photos of real LUMA jobs, recaption or remove them.

### Month by month (one gate per month; do not move on if the gate fails)

| Month | Site (the Tuesday routine does this) | Owner, off-site | Gate at month end |
|---|---|---|---|
| 1 · Oct 15–Nov 15 | Merge this branch; request indexing for the 2 new pages and the 6 changed money pages. Sections + FAQ on Sarasota audio, theaters, networking. Articles #1–#2 from the queue. | **Verify the Google Business Profile** (category "Home automation company", service area Sarasota + Manatee, no street address shown). Fix Yelp phone and hours to match the site. Ask the first 3 real clients for a Google review. | All 48 URLs indexed; home page shows for "smart home installation sarasota"; GBP verified |
| 2 · Nov 15–Dec 15 | Put the GBP CID into `NAP.mapsUrl` and schema `hasMap`/`sameAs`. Expand `/shading`, `/security`, `/audio` to 1,000+ words. City×service pages where GSC already shows demand: Venice automation, Longboat Key theaters, Palmetto shades. | Citations with identical NAP: Apple Business Connect, Bing Places, Houzz, Angi, Thumbtack, BBB, Nextdoor, Sarasota and Manatee chambers. Ask Lutron, Somfy and Ubiquiti about dealer/installer locator listings. | 10+ citations live; 5+ reviews; positions 5–15 on the close-in terms above |
| 3 · Dec 15–Jan 15 | Brand pages: `/lutron`, `/somfy`, `/unifi` (backlog #6). Two articles. Update the shades and cameras articles to 1,200+ words. | 2–3 links from local partners: interior designers, builders, architects we work with (a "trade partner" page on their site or ours). | Page 1 for 3+ city×service phrases |
| 4 · Jan 15–Feb 15 | Critical CSS for LCP. New cities only if GSC shows impressions there (Osprey, Nokomis, Parrish, North Port). Two articles. | One real case study with photos per month on `/work`, shared on GBP. Local press pitch (Sarasota Magazine, Herald-Tribune home section, YourObserver) around hurricane prep or seasonal homes. | Home page top 20 for "smart home installation sarasota" |
| 5 · Feb 15–Mar 15 | Refresh every money page with the GSC queries it now gets (add the phrases people actually use). Two articles. | Reviews 10+; GBP posts weekly; Q&A on GBP. | Top 10 on 5+ money phrases |
| 6 · Mar 15–Apr 15 | Prune or merge anything with no impressions after 90 days. Plan the next half-year from GSC. | Keep reviews and posts going. | **Top 10 for "smart home installation sarasota" and "motorized shades sarasota"; Map Pack appearances** |

### Being cited by AI answers (ChatGPT, Perplexity, Google AI Overviews)

- Same name, phone and service area everywhere (site, GBP, Yelp, Houzz, BBB). Inconsistent NAP is the main reason an AI answer picks a competitor.
- Short, direct answers on the page (the FAQ blocks), with a named place and product in the first sentence.
- The "not luma.com / Luma AI" page stays; it is what disambiguates the brand for crawlers.
- Third-party mentions (directories, partners, press) matter more than anything on our own site for citations.

### Honest expectations

Long-tail and island phrases (Longboat Key and Siesta Key shades, cameras in Sarasota, Venice) can reach page 1 in 1–3 months. "smart home installation sarasota" against Wicked, Sarasota Smart Homes and the directories needs the verified GBP, reviews and local links; without them, six months is unlikely regardless of what the site does. Track every month against the gate, not against a feeling.

### Open questions for the owner

1. ~~Office / light commercial camera jobs?~~ Yes (owner, 2026-10-15): `/service-areas/sarasota/business-security` added.
2. Google Business Profile (checked 2026-10-15 in artyait@gmail.com): 3 profiles, 0 verified — Luma Smart Home (shows old address 4656 Ashton Rd as a storefront) and two duplicate Luma Christmas Lighting profiles. No rejection email in that inbox. Owner fixes within a week.
3. Yelp shows (941) 217-1616 and different hours; the site shows (941) 431-4640, Mon–Sat 9–6. Which is right?

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

0. Static content in HTML: precompile `js/app.js` (no `@babel/standalone` in the browser) and render each page's H1, main copy, images with alt and FAQ into the generated HTML, so Google sees the content without running JS. Biggest technical lever (see Technical checklist). **Done 2026-10-08** (branch claude/seo-prerender): `npm run build` prerenders all pages via scripts/prerender.mjs; raw HTML now 360–1,180 words. Next lever is depth: most pages are still under 600 words.
1. Keyword-first H1 on the 8 service pages and the home page. **Done 2026-10-15** (branch claude/seo-keyword-plan).
2. Google Business Profile: verify, set the CID in `NAP.mapsUrl` and schema `hasMap`, add `sameAs`.
3. Search Console + GA4 (or Plausible): confirm verification, submit the sitemap, watch indexing.
4. Depth on the service pages: 1,000+ words each, FAQ, process, price range, related cases.
5. FAQPage schema in the generator.
6. Brand pages: Lutron, Control4/Savant, Sonos, UniFi, Somfy.
7. Alt text on every image (about half on /lighting are empty). Convert assets to WebP, max 400 KB (30 files are over).
7a. Titles ≤60 and descriptions 110–155 on the pages flagged by `seo-health-check.py`.
8. New cities: Osprey, Nokomis, Parrish, North Port, Punta Gorda, Englewood.
9. Profiles with identical NAP: Houzz, Yelp, Angi, Thumbtack, BBB, Nextdoor, Apple Maps, Bing Places.
10. Links: Lutron / Somfy / Ubiquiti dealer locators, local designers and builders, Sarasota chamber, CEDIA.

## Technical checklist (run every week)

`python3 scripts/seo-health-check.py` checks production against the "why Google doesn't see my site" list (source: ika.explains reel, 2026-10-08). Run it at the start of every routine and against the local build before the PR. Any FAIL is fixed first, before the article.

| # | Item | How it is checked | Status 2026-10-08 (after branch claude/seo-prerender) |
|---|---|---|---|
| 1 | sitemap.xml | generated, listed in robots.txt, every URL 200 | PASS, 46 URLs |
| 2 | robots.txt | does not block `/`, lists sitemap | PASS |
| 3 | noindex | meta robots + `X-Robots-Tag` on every page | PASS, none |
| 4 | canonical | self-referencing, apex host, never localhost/preview | PASS |
| 5 | meta title | ≤60 chars, unique | PASS (9 shortened) |
| 6 | meta description | 110–155 chars, unique | PASS (9 rewritten) |
| 7 | one H1 per page | exactly one `<h1>` in the rendered HTML | PASS (H1 is still a slogan on service pages: backlog #1) |
| 8 | header hierarchy H1→H2→H3 | H1 first, no skipped level | PASS (nav h4s and h1→h3 jumps fixed) |
| 9 | alt text | every visible `<img>`; aria-hidden state layers excluded | PASS |
| 10 | schema markup | JSON-LD parses; LocalBusiness everywhere, Breadcrumb, Article, Service, FAQPage | PASS (FAQPage auto-built from visible FAQ) |
| 11 | internal links | no orphans, ≥2 inbound per page | PASS |
| 12 | broken links | internal hrefs, images on pages, external | PASS (2 dead image refs removed) |
| 13 | compress images | WebP, ≤400 KB on pages | PASS, 159/159 WebP (`scripts/make-webp.py`) |
| 14 | Core Web Vitals | Lighthouse mobile: LCP ≤2.5 s, TBT/INP, CLS ≤0.1 | Improved: perf 39–40 → 71–92, TBT 770 → 0–20 ms, CLS 0. LCP 3.2–5.0 s (lab), still over 2.5 s. Next: inline critical CSS |
| 15 | mobile responsive | 375 px, no horizontal scroll | PASS, 46/46 |
| 16 | HTTPS forced | http→https, www→apex 301, HSTS, no mixed content | PASS |
| 17 | URL slugs | clean paths, no `?p=`, no `#/` | PASS |
| 18 | og:image | 1200×630 card on every page | PASS (19 pages got cards via `scripts/make-og.py`) |
| 19 | Search Console | verified, sitemap submitted, indexing requested | owner: request reindexing after merge (~10 URLs/day) |
| 20 | backlinks | backlog #9–10 | owner: directories, dealer locators, local partners |

Edge cases from the same list, and where we stand:

- **Client-side rendering — fixed 2026-10-08 by prerendering, keep it that way.** Before the fix: The real page content (copy, images, cases) is rendered by React from `js/app.js`, compiled in the browser by `@babel/standalone`. Raw HTML has ~55 words per page outside the noscript nav. Google renders JS, but later and less reliably, and the in-browser Babel compile hurts LCP/INP. Fix (backlog #0): precompile JSX at build time and put each page's main copy, H1, images with alt and FAQ into the static HTML.
- Cloudflare blocking Googlebot ("Under Attack" mode or an aggressive WAF): not used (Netlify). If a CDN/WAF is ever added, allow verified bots.
- Hash routing `/#/about`: the SPA falls back to `location.hash` only if `pushState` throws; no `#/` links in HTML. OK.
- Soft 404: unknown URLs return a real 404. OK.
- Canonical pointing to localhost from a dev build: checked on every run.
- noindex header on preview deploys: Netlify deploy previews (`--alias`) must never be linked publicly; production must never carry `X-Robots-Tag: noindex`.
- Geo-blocking: Googlebot crawls from the US; never geo-restrict the site.
