# Partnership memorandum — how this folder works / Как устроена эта папка

Bilingual trial-period partnership memorandum for launching the LUMA Smart Home service company in Sarasota County and adjacent counties. Двуязычный партнёрский меморандум на пробный период для запуска сервисной компании LUMA Smart Home в округе Sarasota и смежных округах.

## Files / Файлы

| File | What it is | Что это |
|---|---|---|
| `memorandum-en.md` | English memorandum — §1–20 body (two pages) + Annexes A–D | Английская версия — тело §1–20 (две страницы) + Приложения A–D |
| `memorandum-ru.md` | Russian memorandum — identical structure and blanks | Русская версия — та же структура и те же пропуски |
| `memorandum.html` | Print-ready build of both versions: language switch (EN / RU / EN+RU), A4 print styling, "Save as PDF" button | Готовый к печати файл с обеими версиями: переключатель языка, вёрстка A4, кнопка сохранения в PDF |
| `open-questions.md` | 50 questions to settle before signing, grouped, each with a suggested default | 50 вопросов, которые нужно закрыть до подписания, по группам, с предлагаемым вариантом по умолчанию |

The Markdown files are the source of truth. `memorandum.html` is generated — do not edit it by hand. Markdown — источник истины. `memorandum.html` генерируется, править его руками не нужно.

## Working order / Порядок работы

1. Go through `open-questions.md` together — it is written so that each item can be answered with a number, a name, or "default is fine". Пройдите `open-questions.md` вместе: каждый пункт можно закрыть числом, именем или ответом «по умолчанию подходит».
2. Type the answers into the blanks (`______`) in both `memorandum-en.md` and `memorandum-ru.md`. Keep the two files in step — the blanks sit in the same sections. Впишите ответы в пропуски (`______`) в обоих файлах, синхронно: пропуски находятся в одних и тех же разделах.
3. Rebuild the print file. Пересоберите файл для печати:

```bash
python3 scripts/build-memorandum.py
```

4. Open `docs/partnership/memorandum.html` in a browser, pick the language, press **Print / Save as PDF**. Use A4, default margins, background graphics off. Sections 1–20 print on two pages; each annex starts on its own page. Откройте файл в браузере, выберите язык, нажмите кнопку печати: A4, поля по умолчанию, фоновая графика выключена.
5. Sign both language versions (§20), keep a scan each, and put the annexes into a shared drive as living working documents — the time log and KPI dashboard are meant to be updated weekly. Подпишите обе версии (§20), сохраните по сканy каждому, а приложения положите в общий диск как живые рабочие документы: журнал времени и панель KPI обновляются еженедельно.

## Other output formats / Другие форматы

- **PDF** — via the print button above, or headless: `google-chrome --headless=new --print-to-pdf=memorandum.pdf --no-pdf-header-footer docs/partnership/memorandum.html`
- **Word / Google Docs** — if you need a version partners can redline: `pandoc docs/partnership/memorandum-en.md -o memorandum-en.docx` (same for `-ru`), then upload to Google Drive. Если нужна версия для правок в Word или Google Docs — используйте `pandoc`.
- **Plain email / messenger** — the Markdown body reads fine as text; paste §1–20 directly. Тело §1–20 нормально читается как обычный текст, его можно вставить в письмо.

## What the memorandum deliberately does and does not do

- It is a **trial-period memorandum through 31 December 2026**, not a definitive operating agreement. Only confidentiality/exclusivity (§15), brand and IP (§16) and governing law (§19) are written as binding; everything else is intent, so the Partners can move fast without creating obligations they have not tested. Это меморандум на пробный период до 31 декабря 2026 года, а не окончательный договор: обязывающими написаны только §15, §16 и §19.
- It assumes **minimal cash at the start**: capped Seed Cap per partner (§7), client deposits funding project hardware, loss exposure capped at the Seed Cap (§8). Он исходит из минимальных денег на старте: лимит взноса на партнёра, оборудование за счёт авансов клиентов, потолок по убыткам.
- It covers the questions that break partnerships later: participation in losses (§8), how a third partner enters (§13), who owns process improvements (§14), lead ownership and non-circumvention (§11, §15), who keeps the brand and client data if it ends (§16, §17), and the Florida licensing route before any client contract is signed (§18). Он закрывает вопросы, которые обычно ломают партнёрства позже: участие в убытках, вход третьего партнёра, владение улучшениями, правила по лидам, судьба бренда и данных при расхождении, путь лицензирования во Флориде.
- It is **not legal, tax, accounting or insurance advice.** Before the definitive Operating Agreement, the client contract template and the subcontractor agreements are used commercially, have a Florida attorney and a CPA review them. Это не юридическая, налоговая, бухгалтерская или страховая консультация: окончательный договор, шаблон договора с клиентом и договоры субподряда до коммерческого использования нужно показать юристу во Флориде и CPA.
