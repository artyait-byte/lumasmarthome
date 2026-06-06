"""Downscale + recompress all photos in /assets/photos/ for fast web delivery.

Rules:
  - Max width 1600px (downscaled with LANCZOS).
  - Auto-rotate by EXIF.
  - JPEG q=82, progressive, optimized.
  - Skips /cases/ subfolder (already optimized).
  - Skips files already smaller than 1600px wide AND under 250 KB (no-op).
"""
from PIL import Image, ImageOps
from pathlib import Path

ROOT = Path('/Users/artyait/Projects/usa-project/assets/photos')
MAX_W = 1600
JPEG_Q = 82
SMALL_KB = 250

skipped = 0
saved = 0
total_before = 0
total_after = 0

for src in sorted(ROOT.glob('*.jpg')):
    size_before = src.stat().st_size
    total_before += size_before
    try:
        img = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    except Exception as e:
        print(f'  ✗ {src.name}: {e}')
        continue

    w, h = img.size
    needs_resize = w > MAX_W
    needs_recompress = size_before > SMALL_KB * 1024

    if not needs_resize and not needs_recompress:
        skipped += 1
        total_after += size_before
        continue

    if needs_resize:
        new_h = round(h * MAX_W / w)
        img = img.resize((MAX_W, new_h), Image.LANCZOS)

    img.save(src, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
    size_after = src.stat().st_size
    total_after += size_after
    saved += 1
    delta_pct = (1 - size_after / size_before) * 100
    print(f'  ✓ {src.name:<40s} {w}x{h} → {img.size[0]}x{img.size[1]}  '
          f'{size_before//1024:>4} KB → {size_after//1024:>4} KB  ({delta_pct:+.0f}%)')

print()
print(f'Optimized:  {saved}')
print(f'Skipped:    {skipped}')
print(f'Total before: {total_before/1024/1024:.1f} MB')
print(f'Total after:  {total_after/1024/1024:.1f} MB')
print(f'Saved:        {(total_before - total_after)/1024/1024:.1f} MB '
      f'({(1 - total_after/total_before)*100:.0f}% smaller)')
