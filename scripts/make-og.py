"""Build the link-preview cards (Open Graph, 1200x630) for the main pages.

What a person sees when a lumasmarthome.com link is pasted into iMessage,
WhatsApp, Telegram, Slack or Facebook: the page's own photo, the LUMA mark,
the page's headline in the site's serif, and one line of what and where.
Run: python3 scripts/make-og.py  ->  assets/og/<route-id>.jpg
Fonts are the site's (Google Fonts, OFL) and live in scripts/fonts/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
DARK = (20, 19, 30)
CREAM = (252, 250, 246)
ACCENT = (197, 114, 56)
PEACH = (240, 195, 155)

CARDS = {
    # route id: (photo, headline, focus x 0..1)
    "home": ("assets/photos/hero-automation.jpg", "Smart Home Installation", 0.55),
    "lighting": ("assets/photos/live/sc-l-party.jpg", "Your fixtures. Our controls.", 0.5),
    "shading": ("assets/photos/live/sc-s-wake.jpg", "Three layers of shade.", 0.5),
    "theaters": ("assets/photos/theater-cinema.jpg", "Designed for sound, not retrofitted.", 0.5),
    "automation": ("assets/photos/hero-automation.jpg", "One press, the right state.", 0.6),
    "audio": ("assets/photos/hero-audio-hifi.jpg", "Sound that fills the room, not the architecture.", 0.5),
    "security": ("assets/photos/live/sc-sec-night.jpg", "Your footage. Your property.", 0.5),
    "networking": ("assets/photos/hero-networking.jpg", "A network your home is built on, not bolted to.", 0.5),
    "permanent-lighting": ("assets/photos/outdoor/all.jpg", "The roofline, drawn in light.", 0.5),
    "designers": ("assets/photos/hero-designers-new.jpg", "Your vision. Our wiring.", 0.5),
    "work": ("assets/photos/cases/urban-home/web-hero.jpg", "Our work", 0.5),
    "about": ("assets/photos/sarasota-marina.jpg", "Built around the Gulf Coast hour.", 0.5),
    "contact": ("assets/photos/hero-automation.jpg", "Start your project.", 0.6),
    "support": ("assets/video/luma-care-poster.jpg", "Keep the house effortless, long after install.", 0.5),
    "service-areas": ("assets/photos/places/sarasota.jpg", "Sarasota & Manatee Counties.", 0.5),
}
LINE = "Lighting · Shades · Audio & Video · Security · Networking"
PLACE = "Sarasota & Manatee Counties, Florida"


def font(name, size, axes):
    f = ImageFont.truetype(str(ROOT / "scripts/fonts" / name), size)
    try:
        f.set_variation_by_axes(axes)
    except Exception:
        pass
    return f


def cover(img, fx):
    r = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * r), round(img.height * r)), Image.LANCZOS)
    x = min(max(0, round(img.width * fx - W / 2)), img.width - W)
    y = (img.height - H) // 2
    return img.crop((x, y, x + W, y + H))


def wrap(draw, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def card(photo, headline, fx):
    img = cover(Image.open(ROOT / photo).convert("RGB"), fx)
    # a bright, busy patch under the type needs a deeper scrim than a dusk photo
    lum = img.crop((0, H // 2, int(W * 0.75), H)).convert("L").resize((1, 1)).getpixel((0, 0)) / 255
    k = 1.0 + max(0.0, lum - 0.28) * 1.6
    # the reference's 132deg scrim: darker at the lower left where the type sits
    size = 72 if len(headline) < 34 else 60
    hf = font("Cormorant.ttf", size, [500])
    lines = wrap(ImageDraw.Draw(img), headline, hf, 820)
    y0 = H - 118 - len(lines) * size * 1.08
    start = max(0.0, (y0 - 130) / H)
    shade = Image.new("L", (W, H))
    px = shade.load()
    for y in range(H):
        for x in range(W):
            b = min(1.0, max(0.0, (y / H - start) / 0.22))        # full by the headline's first line
            l = max(0.0, 1 - x / (W * 0.75)) ** 1.6              # and toward the left edge
            top = max(0.0, 1 - y / (H * 0.3)) * max(0.0, 1 - x / (W * 0.4))  # behind the mark
            t = min(1.0, (0.85 * b * (0.45 + 0.55 * l)) * k + 0.55 * top)
            px[x, y] = int(10 + 200 * t)
    img = Image.composite(Image.new("RGB", (W, H), DARK), img, shade)
    d = ImageDraw.Draw(img)
    # mark: dot + LUMA + SMART HOME, as in the site header
    luma = font("Cormorant.ttf", 44, [700])
    small = font("DMSans.ttf", 15, [14, 500])
    d.ellipse((64, 72, 80, 88), fill=ACCENT)
    d.text((92, 56), "LUMA", font=luma, fill=CREAM)
    d.text((94, 106), "S M A R T   H O M E", font=small, fill=(220, 214, 204))
    # headline
    # a soft shadow under the headline, for photos with light behind it
    sh = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(sh)
    y = y0
    for ln in lines:
        sd.text((64, y + 2), ln, font=hf, fill=170)
        y += size * 1.08
    img = Image.composite(Image.new("RGB", (W, H), DARK), img, sh.filter(ImageFilter.GaussianBlur(9)))
    d = ImageDraw.Draw(img)
    d.ellipse((64, 72, 80, 88), fill=ACCENT)
    d.text((92, 56), "LUMA", font=luma, fill=CREAM)
    d.text((94, 106), "S M A R T   H O M E", font=small, fill=(220, 214, 204))
    y = y0
    for ln in lines:
        d.text((64, y), ln, font=hf, fill=CREAM)
        y += size * 1.08
    d.rectangle((64, H - 96, 164, H - 93), fill=ACCENT)
    d.text((64, H - 76), "Sarasota & Manatee  ·  lumasmarthome.com", font=font("DMSans.ttf", 24, [14, 500]), fill=PEACH)
    return img


if __name__ == "__main__":
    out = ROOT / "assets/og"
    out.mkdir(exist_ok=True)
    for rid, (photo, headline, fx) in CARDS.items():
        card(photo, headline, fx).save(out / f"{rid}.jpg", quality=86, optimize=True, progressive=True)
        print("og", rid)
