# Redesign handoff — lumasmarthome.com on the Fusion pattern

State as of 2026-09-29 (night). Branch `claude/sharp-shaw-baf08f`. Not deployed. Higgsfield balance 823.5.

## Brief (owner's words, condensed)
- Copy https://fusionaudiovideo.com/ format, layout and section patterns literally; only colors and brand book are LUMA's.
- Must not look AI/Claude-made. Every inner page uses the same Fusion shell.
- Images must read as real live photos, Sarasota / Gulf Coast. Each zone follows the best real sites for that zone (see `docs/IMAGE-REFERENCES.md`).
- Nothing invented: no fake projects, reviews, numbers or claims. Real cases only, even if photos are mediocre.
- Don't burn Higgsfield credits. Check `higgsfield generate cost` first, name the price, prefer existing or real (geo-tagged Unsplash) photos.
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
- Unconfirmed Work-page testimonials were removed on 2026-09-29; see the task plan below.

## Done on 2026-09-29
- About, Support, Work, Contact, Designers and all five case studies on the Fusion inner pattern.
- Contact form posts to Netlify Forms (hidden twin in contact.html). After deploy: turn on form notifications in Netlify.
- Branded LUMA van (assets/photos/luma-van.jpg); the mock-up van photo is out.
- Theater cards re-shot; service-area cards show the house each page describes (assets/photos/homes/).
- Cutaway diagrams with numbered pins (FxDiagram, `diagram` prop on ServicePageShell) on theater,
  lighting, shading, audio, security, networking, permanent lighting. Owner loves this format.
- Solutions menu: dark type, Permanent Lighting back in the list.
- Fixed a stray `}` in spa.css that leaked mobile rules to desktop.

## Task plan (owner's queue, in order)
1. **/designers still reads "old"** (owner, 2026-09-29). Rebuild it harder on the reference:
   likely a hero + image-and-text rows + a cutaway diagram of the trade process (plans ->
   rough-in -> trim-out -> handoff) instead of text cards and tabs. Ask for a screenshot if unclear.
2. Owner confirmation on kept claims: LUMA Care prices ($75/$119/$189), "12 months service
   included", "proposal in two business days", referral fee, "Florida licensed, insured".
3. Real Google reviews -> FX_QUOTES.
4. Brand SVG logos into assets/brands/.
5. Full desktop + mobile pass, then deploy only on the owner's explicit "yes".
