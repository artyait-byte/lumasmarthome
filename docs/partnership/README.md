# Partnership memorandum — how this folder works / Как устроена эта папка

Bilingual trial-period partnership memorandum for launching the LUMA Smart Home service company in Sarasota County and adjacent counties. Двуязычный партнёрский меморандум на пробный период для запуска сервисной компании LUMA Smart Home в округе Sarasota и смежных округах.

## Files / Файлы

| File | What it is | Что это |
|---|---|---|
| `memorandum-en.md` | English memorandum — §1–20 body (two pages) + Annexes A–D | Английская версия — тело §1–20 (две страницы) + Приложения A–D |
| `memorandum-ru.md` | Russian memorandum — identical structure and blanks | Русская версия — та же структура и те же пропуски |
| `memorandum.html` | Print-ready build of both versions: language switch (EN / RU / EN+RU), A4 print styling, "Save as PDF" button | Готовый к печати файл с обеими версиями: переключатель языка, вёрстка A4, кнопка сохранения в PDF |
| `memorandum-en.pdf` / `memorandum-ru.pdf` | Ready-to-send PDF of the **blank** form, 6 A4 pages each: 2-page memorandum + 4 annex pages. Regenerate after filling anything in | PDF **незаполненной** формы, готовый к отправке: 6 страниц A4 — меморандум на 2 страницы + 4 страницы приложений. После заполнения пересоберите |
| `open-questions.md` | 50 questions to settle before signing, grouped, each with a suggested default | 50 вопросов, которые нужно закрыть до подписания, по группам, с предлагаемым вариантом по умолчанию |
| `questions-mapping-ru.md` | The partners' own 50-question checklist («Вопросы для партнеров»), mapped question-by-question to the section that answers it | Ваши «Вопросы для партнеров»: каждый из 50 вопросов сопоставлен с разделом меморандума, где он решается |

The Markdown files are the source of truth. `memorandum.html` is generated — do not edit it by hand. Markdown — источник истины. `memorandum.html` генерируется, править его руками не нужно.

## Working order / Порядок работы

1. Go through `open-questions.md` together — it is written so that each item can be answered with a number, a name, or "default is fine". Пройдите `open-questions.md` вместе: каждый пункт можно закрыть числом, именем или ответом «по умолчанию подходит».
2. Type the answers into the blanks (`______`) in both `memorandum-en.md` and `memorandum-ru.md`. Keep the two files in step — the blanks sit in the same sections. Впишите ответы в пропуски (`______`) в обоих файлах, синхронно: пропуски находятся в одних и тех же разделах.
3. Rebuild the print file. Пересоберите файл для печати:

```bash
python3 scripts/build-memorandum.py
```

4. Open `docs/partnership/memorandum.html` in a browser, pick the language, press **Print / Save as PDF**. Settings that matter: paper **A4**, margins **Default**, scale **100%**, and **“Headers and footers” off** — leaving them on steals a line and pushes the body onto a third page. Sections 1–20 print on two pages; each annex then starts on its own page. Откройте файл в браузере, выберите язык, нажмите кнопку печати. Важные настройки: **A4**, поля **по умолчанию**, масштаб **100%**, «колонтитулы» **выключены** — иначе тело меморандума уедет на третью страницу.
5. Sign both language versions (§20), keep a scan each, and put the annexes into a shared drive as living working documents — the time log and KPI dashboard are meant to be updated weekly. Подпишите обе версии (§20), сохраните по сканy каждому, а приложения положите в общий диск как живые рабочие документы: журнал времени и панель KPI обновляются еженедельно.

Two pages is a hard constraint, so the printed body is set at 7.25 pt — legible, but deliberately dense. If you would rather read it at a comfortable size and accept three pages, raise `font-size` in the `@media print` block of `scripts/build-memorandum.py` and rebuild. On screen the same text is shown at a normal size. Две страницы — жёсткое ограничение, поэтому в печати тело набрано 7.25 pt: читаемо, но плотно. Если хочется крупнее и не жаль третьей страницы — увеличьте `font-size` в блоке `@media print` в `scripts/build-memorandum.py` и пересоберите; на экране текст и так отображается обычным размером.

## Other output formats / Другие форматы

- **PDF** — via the print button above, or headless: `google-chrome --headless=new --print-to-pdf=memorandum.pdf --no-pdf-header-footer docs/partnership/memorandum.html`
- **Word / Google Docs** — if you need a version partners can redline: `pandoc docs/partnership/memorandum-en.md -o memorandum-en.docx` (same for `-ru`), then upload to Google Drive. Если нужна версия для правок в Word или Google Docs — используйте `pandoc`.
- **Plain email / messenger** — the Markdown body reads fine as text; paste §1–20 directly. Тело §1–20 нормально читается как обычный текст, его можно вставить в письмо.

## What the memorandum deliberately does and does not do

- It is a **trial-period memorandum through 31 December 2026**, not a definitive operating agreement. Only confidentiality/exclusivity (§15), brand and IP (§16) and governing law (§19) are written as binding; everything else is intent, so the Partners can move fast without creating obligations they have not tested. Это меморандум на пробный период до 31 декабря 2026 года, а не окончательный договор: обязывающими написаны только §15, §16 и §19.
- The working model is **asymmetric 80 / 20**: **Partner A pours in time and experience — the most expensive thing he has**; if there is no income he will be empty of cash. **Partner B pours in a very small amount of cash.** Artsiom: at least 25 hours per week in the first 4 weeks; Anatoliy: 6 hours a week. The trial **extends automatically** unless either Partner gives written notice of exit; either may **end it on 1 month's notice** at the start. If the Project is moving and making profit, this memo becomes the basis for a full agreement with **3-year vesting** (example: 20% → 6.66% per year); Artsiom's vesting applies only if the B Facility is repaid or he personally assumes the balance. After the trial, shares may be revised **by mutual consent** based on hours or involvement. Модель: А вливает время и опыт; Б — очень мало денег. Автопродление; выход за 1 месяц; вестинг 3 года при переходе в постоянное.
- It assumes **limited cash**: monthly spend is **only regular costs** (leads, marketing, AI tokens, GHL, subscriptions) — **September $500**; anything else only after Artsiom's written request (purpose + amount). B Facility cap **$10,000** at 6% simple. Hardware from client deposits. Месячная минималка сентябрь $500; остальное — по запросу А.
- The trial includes a joint **Accent Florida Home** department named **Accent Smart Home** (§2, §11, D.9): on Accent's website, services, handouts, brochures and all client- and team-facing materials. **LUMA Smart Home** is contractor to Accent Smart Home's direct client, keeps its own margin even when using subcontractors, and shows Accent inbound subcontractor costs and the amount invoiced to Accent. Accent's team does not shop other companies for the same smart-home services (§15). В пробный период входит совместный департамент **Accent Smart Home**: сайт, услуги, раздатки, брошюры и бриф команде Accent; LUMA — подрядчик со своей маржой и открытыми костами; команда Accent не шопится по конкурентам.
- It is **not legal, tax, accounting or insurance advice.** Before the definitive Operating Agreement, the client contract template and the subcontractor agreements are used commercially, have a Florida attorney and a CPA review them. Это не юридическая, налоговая, бухгалтерская или страховая консультация: окончательный договор, шаблон договора с клиентом и договоры субподряда до коммерческого использования нужно показать юристу во Флориде и CPA.
