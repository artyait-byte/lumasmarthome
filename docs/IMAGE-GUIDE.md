# Image Guide — Workflow

Рабочий процесс: вы присылаете новое фото (файл или ссылку) → я кладу его в `assets/photos/` и обновляю URL в `js/images.js` в одной строке. Картинка меняется на всех страницах, где используется соответствующий ключ.

**Текущее состояние:** все 7 главных категорий + hero + designer-раздел хранятся локально (`/assets/photos/*.jpg`), отдаются с Netlify CDN. Projects page временно ещё на Unsplash hotlink — заменим на собственную съёмку по мере появления.

## Как прислать картинку

**Вариант A — ссылка на изображение:**
На странице vendor'а ПКМ по картинке → "Копировать адрес изображения" → пришлите URL + скажите, какой ключ заменить (например `lighting-scene`).

**Вариант B — свой файл:**
Положите `jpg/png/webp` в `assets/photos/` (создайте папку), пришлите имя файла. Я пропишу путь `/assets/photos/your-file.jpg` в реестре.

**Вариант C — скриншот:**
Если "хочу такое по настроению" — просто скриншот, я найду похожее и вставлю.

---

## 7 ключей mega-menu → рекомендованные vendor-источники

| Ключ в реестре     | Категория меню             | Где брать фото (vendor)                                                                                     |
|--------------------|----------------------------|-------------------------------------------------------------------------------------------------------------|
| `lighting-scene`   | Indoor & Outdoor Lighting  | [Lutron RadioRA 3](https://www.lutron.com/us/en/controls/systems/radiora3), [Sunnata keypads](https://www.lutron.com/us/en/controls/keypads/sunnata) |
| `window-shades`    | Window Treatments          | [Lutron Sivoia QS Triathlon](https://www.lutron.com/us/en/shades/systems/sivoiaqs-triathlon), [Somfy PRO shades](https://www.somfypro.com/products/window-treatments) |
| `home-theater`     | Home Theaters              | [Sonance Invisible Series](https://www.sonance.com/product-category/invisible-series/), [Sonos Arc / Arc Ultra](https://www.sonos.com/en-us/shop/arc-ultra) |
| `audio-system`     | Audio & Video              | [Sonos Era 300/100](https://www.sonos.com/en-us/shop/era-300), [Sonance outdoor](https://www.sonance.com/product-category/landscape-series/)             |
| `security-camera`  | Security & Surveillance    | [UniFi Protect G6 Pro Dome/Turret](https://store.ui.com/us/en/pro/category/cameras-dome-turret), [UniFi Doorbell](https://store.ui.com/us/en/category/doorbells) |
| `networking-rack`  | Networking                 | [UniFi Dream Machine Pro](https://store.ui.com/us/en/category/all-cloud-gateways), [UniFi Wi-Fi 7 APs](https://store.ui.com/us/en/category/all-wifi)    |
| `gulf-sunset`      | Home Automation            | [Josh.ai lifestyle gallery](https://www.josh.ai) или editorial-фото интерьера (для сцены "ритуал часа")      |

---

## Дополнительные ключи (hero, projects, lifestyle)

| Ключ                    | Где используется                                          |
|-------------------------|-----------------------------------------------------------|
| `waterfront-lanai`      | Hero слайд 2, split-lifestyle, один project-tile          |
| `project-bayfront`      | projects.html — Longboat Key Bayfront Estate              |
| `project-luxury-pool`   | projects.html                                             |
| `project-modern-villa`  | projects.html                                             |
| `project-warm-interior` | projects.html                                             |
| `project-architectural` | projects.html                                             |

Для проектов лучше всего — **своя съёмка** или editorial-фото Gulf Coast (Sarasota, Siesta Key, Naples, Longboat Key, Boca Grande).

---

## CSP уже разрешает эти домены

В `netlify.toml` `img-src` whitelist включает:
`*.lutron.com`, `lutron.imgix.net`, `*.ui.com`, `*.svc.ui.com`, `*.ctfassets.net`, `*.sonos.com`, `cf.sonos.com`, `*.somfysystems.com`, `*.somfy.com`, `*.josh.ai`, `*.sonance.com`, `images.unsplash.com`.

Если vendor'ский CDN окажется другим — я добавлю домен в CSP вместе с заменой URL.

---

## Важно про лицензию

- Использование product-фото vendor'ов допустимо для **авторизованных дилеров** (LUMA позиционируется как интегратор этих брендов). До публикации убедитесь, что у вас есть dealer authorization от Lutron / Ubiquiti / Somfy / Sonos / Sonance.
- Для press/editorial большинство брендов требует указания model/copyright в alt-тексте или footer — при необходимости добавим.
- **Hotlinking** (прямая ссылка на vendor CDN) работает, но ломается, если vendor меняет URL. Для продакшена лучше:
  1. Скачать фото в `assets/vendors/{vendor}/{product}.jpg`
  2. Обновить ключ в реестре на локальный путь
  3. Получаем скорость отдачи с Netlify CDN + стабильность
