#!/usr/bin/env python3
"""Render the bilingual partnership memorandum into one print-ready HTML file.

Source of truth is the Markdown in docs/partnership/. This script renders both
language versions into docs/partnership/memorandum.html with a language switch
on screen and A4 print styling (the numbered memorandum body is tuned to fit
two pages; each annex starts on its own page).

Usage:  python3 scripts/build-memorandum.py
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "partnership"
OUT = SRC / "memorandum.html"

PAGEBREAK = "<!-- pagebreak -->"

LANGS = [
    {"code": "en", "file": "memorandum-en.md", "label": "English", "html_lang": "en"},
    {"code": "ru", "file": "memorandum-ru.md", "label": "Русский", "html_lang": "ru"},
]

UI = {
    "en": {
        "print": "Print / Save as PDF",
        "hint": "Print at A4, margins “Default”, background graphics off. Sections 1–20 fit two pages; annexes follow.",
    },
    "ru": {
        "print": "Печать / Сохранить в PDF",
        "hint": "Печать A4, поля «по умолчанию», фоновая графика выключена. Разделы 1–20 занимают две страницы, далее приложения.",
    },
}


def inline(text: str) -> str:
    """Escape, then apply the small subset of inline Markdown the docs use."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*(.+?)\*", r"<em>\1</em>", out)
    # Runs of underscores are fill-in blanks: render them as ruled lines whose
    # width tracks the number of underscores in the source.
    def blank(m: re.Match) -> str:
        width = min(max(len(m.group(0)) * 0.42, 2.2), 17)
        return f'<span class="fill" style="width:{width:.1f}em"></span>'

    return re.sub(r"_{3,}", blank, out)


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render(md: str) -> str:
    lines = md.replace(PAGEBREAK, "\n@@PAGEBREAK@@\n").split("\n")
    parts: list[str] = []
    para: list[str] = []
    list_items: list[str] = []
    list_tag = ""

    def flush_para() -> None:
        if para:
            parts.append("<p>" + "<br>".join(inline(l) for l in para) + "</p>")
            para.clear()

    def flush_list() -> None:
        nonlocal list_tag
        if list_items:
            body = "".join(f"<li>{inline(i)}</li>" for i in list_items)
            parts.append(f"<{list_tag}>{body}</{list_tag}>")
            list_items.clear()
            list_tag = ""

    def flush() -> None:
        flush_para()
        flush_list()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush()
        elif stripped == "@@PAGEBREAK@@":
            flush()
            parts.append('<div class="pagebreak"></div>')
        elif stripped == "---":
            flush()
            parts.append("<hr>")
        elif stripped.startswith("#"):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            parts.append(f"<h{level}>{inline(stripped[level:].strip())}</h{level}>")
        elif stripped.startswith("|"):
            flush()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            i -= 1
            head = split_row(block[0])
            body = [split_row(r) for r in block[2:]] if len(block) > 2 else []
            thead = "".join(f"<th>{inline(c)}</th>" for c in head)
            rows = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                for r in body
            )
            parts.append(
                f"<table><thead><tr>{thead}</tr></thead><tbody>{rows}</tbody></table>"
            )
        elif re.match(r"^\d+\.\s", stripped):
            flush_para()
            if list_tag != "ol":
                flush_list()
                list_tag = "ol"
            list_items.append(re.sub(r"^\d+\.\s+", "", stripped))
        elif stripped.startswith("- "):
            flush_para()
            if list_tag != "ul":
                flush_list()
                list_tag = "ul"
            list_items.append(stripped[2:])
        else:
            flush_list()
            para.append(stripped)
        i += 1

    flush()
    return "\n".join(parts)


CSS = """
:root{
  --ink:#14181c; --mid:#5b6670; --line:#c9d0d6; --rule:#9aa5ad;
  --accent:#0f6f74; --paper:#fff; --shell:#eceff1;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--shell);color:var(--ink);
  font-family:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",sans-serif;
  font-size:15px;line-height:1.5;-webkit-print-color-adjust:exact}

.bar{position:sticky;top:0;z-index:10;display:flex;flex-wrap:wrap;gap:10px;
  align-items:center;justify-content:center;padding:12px 16px;
  background:#101619;color:#f4f6f7;box-shadow:0 1px 6px rgba(0,0,0,.25)}
.bar .sw{display:flex;border:1px solid #3a464c;border-radius:999px;overflow:hidden}
.bar button{font:inherit;font-size:13px;letter-spacing:.02em;padding:7px 16px;
  background:transparent;color:#cfd6da;border:0;cursor:pointer}
.bar button+button{border-left:1px solid #3a464c}
.bar button[aria-pressed=true]{background:var(--accent);color:#fff}
.bar .print{border:1px solid #3a464c;border-radius:999px;padding:7px 16px}
.bar .print:hover{background:#1d262b}
.bar .hint{flex:1 1 100%;text-align:center;font-size:11.5px;color:#8b979e;margin:0}

.doc{display:none;max-width:820px;margin:24px auto 60px;padding:52px 60px;
  background:var(--paper);box-shadow:0 2px 18px rgba(20,24,28,.14)}
body[data-lang=en] #doc-en,body[data-lang=ru] #doc-ru,
body[data-lang=both] .doc{display:block}

h1{font-size:20px;line-height:1.25;margin:0 0 10px;letter-spacing:-.01em}
h2{font-size:12.5px;line-height:1.3;margin:15px 0 5px;letter-spacing:.005em;
  padding-bottom:3px;border-bottom:1px solid var(--line)}
h3{font-size:11.5px;margin:12px 0 4px}
p{margin:0 0 6px;text-align:justify;hyphens:auto}
ol,ul{margin:0 0 6px;padding-left:19px}
li{margin:0 0 2px}
hr{border:0;border-top:1.5px solid var(--rule);margin:10px 0 12px}
strong{font-weight:700}
em{font-style:italic;color:var(--mid)}

.doc h1+p,.doc p:first-of-type{color:var(--mid)}
h1{border-bottom:2px solid var(--accent);padding-bottom:8px}

table{width:100%;border-collapse:collapse;margin:5px 0 8px;font-size:9.4px;
  line-height:1.32}
th,td{border:1px solid var(--line);padding:3px 5px;text-align:left;
  vertical-align:top;word-wrap:break-word;overflow-wrap:anywhere}
th{background:#f2f5f6;font-weight:700;font-size:9px;letter-spacing:.02em}

.fill{display:inline-block;border-bottom:1px solid var(--rule);
  height:.95em;vertical-align:baseline;min-width:2.2em}
/* A blank alone in a table cell becomes a full-width line to write on. */
td>.fill:only-child{width:100%!important}

.pagebreak{height:0}

@media screen{
  .doc{font-size:12.5px}
  .doc h1{font-size:23px}
  .doc h2{font-size:14px}
  .doc table{font-size:11px}
  body[data-lang=both] #doc-ru{margin-top:0}
}

@media print{
  @page{size:A4;margin:8mm 9mm}
  body{background:#fff;font-size:7.25pt;line-height:1.24}
  .bar{display:none}
  .doc{display:block!important;max-width:none;margin:0;padding:0;box-shadow:none}
  body[data-lang=en] #doc-ru,body[data-lang=ru] #doc-en{display:none!important}
  body[data-lang=both] #doc-ru{break-before:page}
  h1{font-size:11.5pt;margin:0 0 3.5pt;padding-bottom:2.5pt}
  h2{font-size:7.5pt;margin:4.3pt 0 1.4pt;padding-bottom:1pt;break-after:avoid}
  h3{font-size:7.3pt;margin:4.2pt 0 1.3pt;break-after:avoid}
  p{margin:0 0 2pt;orphans:2;widows:2}
  ol,ul{margin:0 0 2pt;padding-left:11pt}
  li{margin:0 0 .6pt}
  hr{margin:3.4pt 0 3.8pt}
  table{font-size:6.1pt;line-height:1.18;margin:1.8pt 0 2.6pt}
  th,td{padding:1.1pt 2pt}
  th{font-size:5.9pt}
  .fill{height:.88em}
  .pagebreak{break-before:page}
}
"""

JS = """
(function(){
  var body=document.body;
  var btns=[].slice.call(document.querySelectorAll('.bar .sw button'));
  function set(l){
    body.setAttribute('data-lang',l);
    btns.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.lang===l));});
    try{localStorage.setItem('memo-lang',l);}catch(e){}
  }
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.lang);});});
  var saved=null;try{saved=localStorage.getItem('memo-lang');}catch(e){}
  set(saved||'en');
  document.querySelector('.bar .print').addEventListener('click',function(){window.print();});
})();
"""


def main() -> None:
    docs = []
    for lang in LANGS:
        md = (SRC / lang["file"]).read_text(encoding="utf-8")
        docs.append(
            f'<article class="doc" id="doc-{lang["code"]}" lang="{lang["html_lang"]}">\n'
            f'{render(md)}\n</article>'
        )

    switch = "".join(
        f'<button type="button" data-lang="{l["code"]}" aria-pressed="false">{l["label"]}</button>'
        for l in LANGS
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Partnership Memorandum · LUMA Smart Home</title>
<meta name="robots" content="noindex,nofollow">
<style>{CSS}</style>
</head>
<body data-lang="en">
<nav class="bar">
  <div class="sw">{switch}<button type="button" data-lang="both" aria-pressed="false">EN + RU</button></div>
  <button type="button" class="print">{UI["en"]["print"]} · {UI["ru"]["print"]}</button>
  <p class="hint">{UI["en"]["hint"]}<br>{UI["ru"]["hint"]}</p>
</nav>
{chr(10).join(docs)}
<script>{JS}</script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page):,} bytes)")


if __name__ == "__main__":
    main()
