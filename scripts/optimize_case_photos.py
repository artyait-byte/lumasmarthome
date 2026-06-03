"""Pick + resize + optimize the case-study photos for web."""
from PIL import Image, ImageOps
from pathlib import Path

ROOT = Path('/Users/artyait/Projects/usa-project/assets/photos/cases')

# Each entry: (case_dir, source_filename, output_slug, max_width, target_aspect)
# target_aspect None means keep original aspect; ratio means crop to that aspect
PLAN = [
    # ── Spacious Modern (Sonos focus) ──
    ('spacious-modern', '07-banner-van.jpg', 'hero',     1920, None),       # exterior wide
    ('spacious-modern', '02-luma-van.jpg',   'van',      1600, None),       # rebranded van shot
    ('spacious-modern', '03-equipment-rack.jpg', 'ceiling-speakers', 1600, None),
    ('spacious-modern', '04-scene-a.jpg',    'scene-a',  1400, None),
    ('spacious-modern', '06-scene-c.jpg',    'scene-b',  1400, None),

    # ── Urban Home (B&W + UniFi + 7.1.2) ──
    ('urban-home',      '06-scene-c.jpg',    'hero',     1920, (16, 9)),    # media room w/ B&W
    ('urban-home',      '04-scene-b.jpg',    'pool-audio', 1200, None),
    ('urban-home',      '03-scene-a.jpg',    'rack',       1200, None),
    ('urban-home',      '07-scene-d.jpg',    'speaker-detail', 1200, None),
    ('urban-home',      '08-scene-e.jpg',    'in-wall-speaker', 1200, None),

    # ── Huge Family House (Architectural lighting) ──
    ('huge-family',     '22.jpg',            'hero',     1920, (16, 7)),    # wide exterior banner
    ('huge-family',     '01.jpg',            'great-room', 1600, None),     # vaulted ceiling
    ('huge-family',     '04.jpg',            'led-cove',   1400, None),     # wall LEDs
    ('huge-family',     '05.jpg',            'led-detail', 1400, None),     # accent under wood
    ('huge-family',     '03.jpg',            'shower-niche', 1400, None),
]


def crop_to_aspect(img, target_w, target_h):
    """Center-crop the image to the requested w:h ratio, then return."""
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    tgt_ratio = target_w / target_h
    if src_ratio > tgt_ratio:
        # Source is wider — crop sides
        new_w = int(src_h * tgt_ratio)
        x0 = (src_w - new_w) // 2
        return img.crop((x0, 0, x0 + new_w, src_h))
    new_h = int(src_w / tgt_ratio)
    y0 = (src_h - new_h) // 2
    return img.crop((0, y0, src_w, y0 + new_h))


for (case, src_name, out_slug, max_w, aspect) in PLAN:
    src = ROOT / case / src_name
    if not src.exists():
        print(f'  ✗ missing {src}')
        continue
    img = Image.open(src)
    img = ImageOps.exif_transpose(img).convert('RGB')

    if aspect is not None:
        img = crop_to_aspect(img, *aspect)

    # Resize so longer dimension is at most max_w (for landscape) or that the
    # WIDTH does not exceed max_w. Tall photos keep their portrait shape.
    w, h = img.size
    if w > max_w:
        new_h = round(h * max_w / w)
        img = img.resize((max_w, new_h), Image.LANCZOS)

    out = ROOT / case / f'web-{out_slug}.jpg'
    img.save(out, 'JPEG', quality=82, optimize=True, progressive=True)
    print(f'  ✓ {out.relative_to(ROOT)}  {img.size}  {out.stat().st_size // 1024} KB')
