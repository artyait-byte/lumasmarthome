# Redesign handoff — lumasmarthome.com on the Fusion pattern

State as of 2026-09-29. Branch `claude/sharp-shaw-baf08f`, last commit `6a75bb1`. Not deployed.

## Brief (owner's words, condensed)
- Copy https://fusionaudiovideo.com/ format, layout and section patterns literally; only colors and brand book are LUMA's.
- Must not look AI/Claude-made. Every inner page uses the same Fusion shell.
- Images must read as real live photos, Sarasota / Gulf Coast. Each zone follows the best real sites for that zone (see `docs/IMAGE-REFERENCES.md`).
- Nothing invented: no fake projects, reviews, numbers or claims. Real cases only, even if photos are mediocre.
- Don't burn Higgsfield credits. Check `higgsfield generate cost` first, name the price, prefer existing or real (geo-tagged Unsplash) photos. Balance 881.
- Service area: Sarasota & Manatee Counties only. Sarasota, Bradenton, Lakewood Ranch, Venice, Siesta Key, Longboat Key, Anna Maria Island, Palmetto.

## How it's built
- SPA: `js/app.js` (React 18 UMD + Babel standalone), `css/spa.css`, `js/images.js`.
- SEO shells: `python3 scripts/generate-seo-pages.py` from `scripts/seo_content.py` (cities, articles, hub, NAP). Generated HTML is never hand-edited.
- Cache busters: `lu = path + '?v=17'` in app.js; images.js `?v=8`. Bump on asset changes.
- Preview: `.claude/launch.json` → name `luma`, port 8766 (`scripts/devserver.py`, no-store).
- Photo grade for any generated frame: `scripts/photo_grade.sh in out [width]`.
- Browser-pane screenshots are unreliable; verify with JS measurements. Pane hover doesn't fire React events, so dispatch synthetic mouseover/mouseout.

## Done
- FX kit: header (hover Solutions menu, closes on leave/scroll/Esc), hero video + still, inner hero, panels, wave CTA, callout, map, brands strip (10 brands the owner named + brands from cases).
- Home: scene switcher (morning → night), "Selected work" = 3 real cases from `LUMA_CASES`. Quotes carousel hidden until `FX_QUOTES` gets real reviews.
- Service pages: "Where we have done this" rows from real cases only.
- Service Areas hub + 8 city pages on the Fusion /locations pattern, real geo-tagged photos (`assets/photos/places/CREDITS.md`). Naples, Fort Myers and Punta Gorda redirect 301 to the hub.
- Journal on the Fusion /blog pattern: weekly dates 08-24 → 09-24, categories, article page.
- "For the trade" renamed "Designers & builders" (= `/designers`).

## Open — needs the owner
1. Work page `TESTIMONIALS` (in code since May: Martina R./Naples, Jonathan K./Boca Grande, Sarah W., AIA …). Remove unless confirmed real.
2. Real Google reviews → `FX_QUOTES` (the carousel shows up automatically).
3. Deploy to Netlify — only after an explicit "yes".

## Next work
- Move About, Work, Designers, Contact onto the Fusion inner shell (`FxInnerHero` → prose/rows → `FxCta`). Support is "plus/minus OK"; only light tweaks.
- Brand SVG logos into `assets/brands/` and fill the `FX_BRAND_LOGOS` set (see `assets/brands/README.md`).
- Before deploy: full pass desktop + mobile (no horizontal overflow), console clean, regenerate SEO pages, check `_redirects`/sitemap.
