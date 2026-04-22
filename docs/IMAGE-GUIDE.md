# Image Guide — Workflow

Рабочий процесс: вы присылаете новое фото (файл или ссылку) → я кладу его в `assets/photos/` и обновляю URL в `js/images.js` в одной строке. Картинка меняется на всех страницах, где используется соответствующий ключ.

**Текущее состояние:** все 7 главных категорий + hero + designer-раздел хранятся локально (`/assets/photos/*.jpg`), отдаются с Netlify CDN. Projects page временно ещё на Unsplash hotlink — заменим на собственную съёмку по мере появления.

## Визуальный ориентир (как в luxury integrator «technology & lifestyle guide»)

По **смыслу** (не копируя макет и не забирая картинки с чужих PDF/сайтов) такие буклеты обычно строят на одних и тех же **темах** — их и стоит отражать в стоке / прессе вендоров / своей съёмке:

| Тема | Что показывать в кадре (настроение) |
|------|--------------------------------------|
| **Lighting + control** | Слоистый свет, клавиатуры в стене, тёплый dim, «человеко-центричный» свет (рассвет/вечер), работа с дизайнером света и архитектором |
| **Shades** | Моторизованные полотна, ткань/римские, бесшумность, дневной свет как ресурс (не «просто шторы») |
| **Скрытая электроника** | TV из картины/зеркала, **invisible / in-ceiling** акустика, минимум «коробок на тумбе» |
| **Whole-home A/V** | Зоны, потолок/стена, ланай, «все в комнатах разное — вместе одной сценой» |
| **Theater** | Акустика, рассадка, проекция/тёмная комната (кинозал, не гостиная с одной колонкой) |
| **Outdoor** | Патио/бассейн, all-weather A/V, вечерний свет |
| **Network** | «Костяк» Wi‑Fi, предсказуемость, не гигиенический пластиковый роутер в кадре — лучше стойка/шкаф/диаграмма зоны покрытия (осторожно с брендами) |
| **Питание / wellness** | Батареи/кондиционирование питания, вентиляция, циркадные сценарии — только если это реально продаёте (иначе не вводить в заблуждение) |

**Чего не делать:** скачивать фотографии с **сайтов других integrator'ов** (портфолио, буклеты) — у них **авторское право на фото и дизайн**; риск претензий. Тот же *стиль* достигается **лицензионным** путём ниже.

**Легальные источники «как у премиум-интеграторов»:**

1. **Пресс-центр / for pros** у брендов, которые вы устанавливаете (Lutron, Sonance, Sonos Pro, Savant, Crestron, Ubiquiti, Ketra — у каждого свои правила, часто dealer-only).  
2. **Unsplash / Pexels** — поиск по словам: `architectural lighting`, `motorized shade living room`, `in ceiling speaker`, `home theater`, `network rack clean`, `smart home interior Florida` (следить за брендами в кадре).  
3. **Свой объект** — лучшее для доверия; даже 2–3 грамотных кадра с монтажника.

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
| *(CSS)* `luma-bg--audio` | Audio & Video (mega + главная) | **Не** `data-img` — фон в `css/styles.css` (`.luma-bg--audio` → `mega-audio-video.jpg`), чтобы кэш старого `images.js` не подставлял устаревшее фото. Сменить картинку: правка URL в CSS + `?v=` в том же правиле. |
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
