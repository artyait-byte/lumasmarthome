"""Rebrand Smartnova van photo as LUMA SMART HOME for case-study use."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# If a fresh Smartnova source is present we use it; otherwise we re-paint over our
# previously-rebranded copy (the panel is fully opaque, so it stays clean).
_DIR = Path('/Users/artyait/Projects/usa-project/assets/photos/cases/spacious-modern')
SRC = _DIR / '02-kitchen.jpg'
if not SRC.exists():
    SRC = _DIR / '02-luma-van.jpg'
OUT = _DIR / '02-luma-van.jpg'

LUMA_INK    = (27, 26, 40)
LUMA_ACCENT = (197, 114, 56)
LUMA_MID    = (90, 90, 100)

img = Image.open(SRC).convert('RGB')
W, H = img.size
print(f'Source size: {W}x{H}')

# The van's left panel paint sits in the (180, 182, 186) range.
van_paint = (181, 183, 188)
print(f'Using van paint: {van_paint}')

# The original SMARTNOVA branding occupies a roughly rectangular area on the
# rear side panel of the van (driver side). Coordinates measured against the
# 1672x2160 source image — careful not to overflow onto the rear door / tail-
# light area, and wide enough to cover the entire Smartnova content (logo,
# bullets, phone, email, web, and QR-code patch).
panel = (550, 1050, 1140, 1555)  # left, top, right, bottom

draw = ImageDraw.Draw(img)
draw.rectangle(panel, fill=van_paint)

# Soften the rectangle edges into the surrounding paint so the patch blends in.
for inset in range(1, 5):
    shade = tuple(max(0, min(255, c - 2 * inset)) for c in van_paint)
    draw.rectangle(
        (panel[0] - inset, panel[1] - inset, panel[2] + inset, panel[3] + inset),
        outline=shade,
    )

# ── Typography ──────────────────────────────────────────────────────────────
def font(name, size, bold=False):
    candidates = []
    if bold:
        candidates += [f'/System/Library/Fonts/Supplemental/Arial Bold.ttf']
    candidates += [f'/System/Library/Fonts/Supplemental/Arial.ttf',
                   '/System/Library/Fonts/Helvetica.ttc']
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()

f_brand   = font('Arial', 96, bold=True)
f_tag     = font('Arial', 32)
f_service = font('Arial', 26)
f_phone   = font('Arial', 42, bold=True)
f_meta    = font('Arial', 26)

# Inner content origin (px inset from panel)
ox = panel[0] + 28
oy = panel[1] + 22

# Copper dot accent
dot_r = 12
draw.ellipse((ox, oy + 24, ox + 2 * dot_r, oy + 24 + 2 * dot_r), fill=LUMA_ACCENT)

# LUMA wordmark
draw.text((ox + 2 * dot_r + 16, oy), 'LUMA', fill=LUMA_INK, font=f_brand)

# SMART HOME tagline
draw.text((ox + 2 * dot_r + 18, oy + 96), 'S M A R T   H O M E', fill=LUMA_MID, font=f_tag)

# Services bullets
services = [
    'Smart-home design & install',
    'Lighting · shading · climate',
    'Audio · video · networking',
    'Security · ongoing care',
]
y = oy + 154
for s in services:
    draw.ellipse((ox + 2, y + 9, ox + 14, y + 21), fill=LUMA_ACCENT)
    draw.text((ox + 26, y), s, fill=LUMA_INK, font=f_service)
    y += 36

# Phone (prominent)
draw.text((ox, y + 18), '+1 (941) 217-1616', fill=LUMA_INK, font=f_phone)

# Email + website
draw.text((ox, y + 76), 'hello@lumasmarthome.com', fill=LUMA_MID, font=f_meta)
draw.text((ox, y + 114), 'lumasmarthome.com', fill=LUMA_MID, font=f_meta)

img.save(OUT, 'JPEG', quality=88)
print(f'Wrote {OUT} ({OUT.stat().st_size // 1024} KB)')
