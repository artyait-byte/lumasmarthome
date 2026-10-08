#!/usr/bin/env node
/* Compile js/app.js and prerender every page into its HTML shell.

   Runs after scripts/generate-seo-pages.py (see package.json "build").
   1. esbuild turns the JSX in js/app.js into js/app.min.js, so the browser
      no longer downloads @babel/standalone and compiles 230 KB on every visit.
   2. For each generated shell (it carries window.__LUMA_PAGE="<id>"), the app
      is run in a Node sandbox with that page's URL and rendered with
      ReactDOMServer. The markup goes into <div id="root">, so Google and
      visitors get the full page (H1, copy, images with alt) without JS.
      The browser then hydrates it (see the bottom of js/app.js).
   Any failure exits non-zero: Netlify keeps the previous deploy. */
import { readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';
import * as esbuild from 'esbuild';
import React from 'react';
import ReactDOMServer from 'react-dom/server';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SKIP = new Set(['_archive', 'node_modules', '.git', '.claude', 'assets', 'images', 'scripts', 'docs']);

const source = readFileSync(join(ROOT, 'js/app.js'), 'utf8');
const compiled = esbuild.transformSync(source, { loader: 'jsx', target: 'es2018', jsx: 'transform' }).code;
const minified = esbuild.transformSync(source, { loader: 'jsx', target: 'es2018', jsx: 'transform', minify: true }).code;
writeFileSync(join(ROOT, 'js/app.min.js'), '/* Built from js/app.js by scripts/prerender.mjs — do not edit. */\n' + minified);
console.log(`[ok] js/app.min.js  ${(minified.length / 1024).toFixed(0)} KB`);

const seoData = readFileSync(join(ROOT, 'js/seo-data.js'), 'utf8');
const appScript = new vm.Script(compiled, { filename: 'app.js' });
const seoScript = new vm.Script(seoData, { filename: 'seo-data.js' });

function shells(dir) {
  const out = [];
  for (const name of readdirSync(dir)) {
    if (SKIP.has(name)) continue;
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...shells(p));
    else if (name.endsWith('.html')) out.push(p);
  }
  return out;
}

function render(id) {
  const ctx = { React, console, URLSearchParams, setTimeout, clearTimeout };
  ctx.window = ctx;
  ctx.__LUMA_PAGE = id;
  vm.createContext(ctx);
  seoScript.runInContext(ctx);
  const route = ctx.LUMA_SEO.routes[id];
  if (!route) throw new Error(`no route for page id "${id}"`);
  ctx.location = { pathname: route.path, search: '', hash: '', href: ctx.LUMA_SEO.siteUrl + route.path };
  appScript.runInContext(ctx);
  return ReactDOMServer.renderToString(React.createElement(ctx.__LUMA_APP));
}

const PAGE_RE = /<script>window\.__LUMA_PAGE=("[^"]+");<\/script>/;
const ROOT_RE = /<div id="root">[\s\S]*?<\/div>\n?(?=<form |<script>window\.__LUMA_PAGE)/;
const NOSCRIPT_RE = /<noscript>\s*<header class="seo-noscript">[\s\S]*?<\/noscript>\n?/;
const BABEL_RE = /<script src="https:\/\/unpkg\.com\/@babel\/standalone[^>]*><\/script>\n?/;
const APP_RE = /<script type="text\/babel" data-presets="react" src="\/js\/app\.js"><\/script>/;

let count = 0;
for (const file of shells(ROOT)) {
  let html = readFileSync(file, 'utf8');
  const m = html.match(PAGE_RE);
  if (!m) continue;
  const id = JSON.parse(m[1]);
  const markup = render(id);
  if (!ROOT_RE.test(html)) throw new Error(`${relative(ROOT, file)}: no <div id="root"> before the page script`);
  html = html
    .replace(ROOT_RE, () => `<div id="root">${markup}</div>\n`)
    .replace(NOSCRIPT_RE, '')
    .replace(BABEL_RE, '')
    .replace(APP_RE, '<script src="/js/app.min.js"></script>');
  writeFileSync(file, html);
  const words = markup.replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
  console.log(`[ok] ${relative(ROOT, file)}  →  ${id}  (${words} words)`);
  count++;
}
if (!count) throw new Error('no page shells found');
console.log(`prerendered ${count} pages`);
