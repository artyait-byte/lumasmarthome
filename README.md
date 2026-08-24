# LUMA Smart Home — Marketing Site

Статический мультистраничный сайт студии интеграции резидентциальных технологий на побережье Мексиканского залива во Флориде (Sarasota · Manatee · Charlotte · Lee · Collier).

Стек специально минимальный: **HTML + CSS + JS**, без сборки. Всё, что нужно — статический хостинг. По умолчанию проект настроен под **Netlify** (формы, pretty-URL редиректы, заголовки кэша/безопасности).

---

## Быстрый старт

```bash
# локальный просмотр
python3 -m http.server 8000
# → http://localhost:8000
```

или

```bash
npx serve .
```

---

## Структура

```
.
├── index.html            # Home shell (unique <head>) — SPA mounts into #root
├── lighting.html         # and the other public URLs: about, work, contact, …
├── css/spa.css           # SPA styles
├── js/app.js             # React SPA (Babel standalone)
├── js/seo-data.js        # Route map for title/canonical (generated)
├── sitemap.xml           # Every public URL
├── robots.txt
├── netlify.toml          # pretty URLs, legacy redirects, CSP
├── scripts/generate-seo-pages.py  # HTML shells + sitemap + robots
└── docs/IMAGE-GUIDE.md
```

After editing titles/descriptions in `scripts/generate-seo-pages.py` (`ROUTES`), run:

```bash
python3 scripts/generate-seo-pages.py
```

## Работа с картинками

Все картинки сайта (104 места использования, 13 уникальных) перенесены в единый реестр `js/images.js`:

```js
window.LUMA_IMAGES = {
  'lighting-scene':  'https://...',
  'window-shades':   'https://...',
  // ...
};
```

В HTML элементы ссылаются по ключу:

```html
<div class="cat-bg" data-img="lighting-scene"></div>
```

JS-лоадер (`js/images.js`) на `DOMContentLoaded` пробегает по всем `[data-img]` и проставляет `background-image` из реестра.

**Поменять картинку:** найти ключ в `js/images.js`, заменить URL, сохранить. Изменение применится на всех страницах, где используется этот ключ.

Подробности — `docs/IMAGE-GUIDE.md`.

---

## Формы (Netlify Forms)

Три формы настроены на Netlify Forms (auto-detect по `data-netlify="true"`):

| Форма               | `form-name`         | Где                |
|---------------------|---------------------|--------------------|
| Home consultation   | `home-consultation` | `index.html` (финальный CTA-блок) |
| Contact             | `contact`           | `contact.html`     |
| Budget estimate     | `budget-estimate`   | `budget.html` (после результатов калькулятора) |

**Поведение:** AJAX-отправка через `fetch('/')` к Netlify (`js/main.js` → `submitToNetlify`). Пользователь остаётся на странице, видит inline-статус. Если JS отключён, форма имеет `action="/thank-you.html"` и отработает нативным submit.

**Где смотреть заявки:** Netlify Dashboard → Forms → выбрать форму → CSV-экспорт / email-уведомления настраиваются в UI.

**Защита от ботов:** honeypot-поле `bot-field` (скрыто, `hidden` атрибут). При желании можно включить reCAPTCHA через `data-netlify-recaptcha="true"` + widget.

---

## SEO

The site is a React SPA, but **each public view is a real HTML file** (`/lighting`, `/about`, `/work`, …) so Google can index more than the homepage.

Every public `<head>` includes:

- unique `<title>` and `<meta name="description">`
- `<link rel="canonical">` on the apex host `https://lumasmarthome.com/...`
- Open Graph + Twitter Card (JPEG photos, not SVG)
- JSON-LD `LocalBusiness` + `WebSite` + `WebPage` (service pages also get `Service`)
- a `<noscript>` block with the page H1 and internal links

Nav and footer use real `<a href="/lighting">` links, not buttons. `sitemap.xml` lists every URL. `brochure.html` and `/_archive/` are `noindex`.

After deploy: in Google Search Console submit the new sitemap and request indexing for the key URLs. The old 301s that sent `/lighting` (and similar) back to `/` are removed.

---

## Что настроить перед продакшеном

1. **Домен.** Canonical host is the apex `https://lumasmarthome.com` (www already 301s there). URLs live in `scripts/generate-seo-pages.py`.
2. **Телефон и email.** В шапках/футерах и в JSON-LD сейчас плейсхолдеры `+1 (941) 217-1616` и `hello@lumasmarthome.com`.
3. **OG-обложка.** `assets/og-cover.svg` — векторный плейсхолдер. Для лучшей совместимости с Facebook/LinkedIn экспортируйте в PNG/JPG 1200×630 и обновите путь в `inject-seo.py` (`OG_IMAGE`) + перезапустите скрипт.
4. **`apple-touch-icon.png`.** Пока отсутствует — либо добавьте 180×180 PNG, либо уберите `<link rel="apple-touch-icon">` из `inject-seo.py`.
5. **Фото проектов.** Unsplash-плейсхолдеры на продакшн не пойдут (лицензия + бренд). Замените на собственную съёмку и положите в `assets/projects/`.
6. **Netlify Forms в dashboard.** При первом деплое откройте Forms → убедитесь, что три формы обнаружены. Подключите email-уведомления.
7. **Google Business Profile** на 5 округов SWFL (см. JSON-LD `areaServed`).
8. **Analytics.** Добавить GA4 / Plausible / Fathom в `<head>` вручную или через второй шаг `inject-seo.py`.

---

## Деплой на Netlify

Вариант 1 — через CLI:

```bash
npm i -g netlify-cli
netlify login
netlify init              # свяжет репо с новым сайтом
netlify deploy --prod     # публикация
```

Вариант 2 — через dashboard:

1. New site → Import from Git → подключить репо
2. Build command: `echo 'No build step — static site'`
3. Publish directory: `.`
4. Deploy

После первого деплоя в разделе **Forms** появятся три формы. Включите email-нотификации.

---

## CSP-заметка

В `netlify.toml` Content-Security-Policy разрешает:

- `img-src`: self + `images.unsplash.com` (текущие плейсхолдер-фото)
- `style-src`: self + Google Fonts (CSS)
- `font-src`: self + Google Fonts (файлы шрифтов)
- `script-src`: self + inline (используется в `main.js` через атрибуты и инлайн в виджете карусели)

Если будете добавлять аналитику, менеджер тегов или виджет чата — обновите `connect-src` и `script-src` в `netlify.toml`.
