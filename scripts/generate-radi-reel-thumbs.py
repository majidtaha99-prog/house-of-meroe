from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(r"C:/Users/TAHA/Desktop/house of meroe")
SITE = ROOT / "site"
OUT = SITE / "radi"
SRC = ROOT / "radi-outreach-pack" / "radi-circle.png"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 900, 1600
GOLD = (216, 166, 100)
GOLD_BRIGHT = (255, 224, 141)
BONE = (246, 239, 225)
INK = (6, 4, 10)
MUTED = (154, 151, 136)

try:
    font_big = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 116)
    font_serif = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 92)
    font_mid = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 58)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 34)
    font_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 24)
except Exception:
    font_big = font_serif = font_mid = font_mono = font_small = ImageFont.load_default()

profile = Image.open(SRC).convert("RGBA")
# Use the profile image as a blurred oversized backdrop, then as a crisp circular portrait.
backdrop = profile.resize((H, H), Image.Resampling.LANCZOS).crop(((H-W)//2, 0, (H+W)//2, H))
backdrop = backdrop.filter(ImageFilter.GaussianBlur(34))

labels = [
    ("REEL · 01", "MENA LIFESTYLE", "Radi", "Barakat"),
    ("REEL · 02", "COMEDY", "Street", "Stories"),
    ("REEL · 03", "PODCAST HOST", "Creator", "Moments"),
    ("REEL · 04", "BRAND FIT", "Audience", "Proof"),
]

for idx, (kicker, theme, line1, line2) in enumerate(labels, 1):
    img = Image.new("RGB", (W, H), INK)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # Slightly different crop/position per card from the same local asset.
    bg = backdrop.copy().convert("RGBA")
    bg = bg.rotate((idx - 2) * 2, resample=Image.Resampling.BICUBIC, expand=False)
    bg.putalpha(86)
    layer.alpha_composite(bg, (0, 0))
    d = ImageDraw.Draw(layer)
    # Dark overlay + gold wash.
    d.rectangle((0, 0, W, H), fill=(6, 4, 10, 168))
    d.ellipse((-320, 180 + idx * 75, 560, 1040 + idx * 75), fill=(201, 162, 83, 30))
    d.ellipse((360, -120, 1080, 640), fill=(255, 224, 141, 22))
    d.rectangle((55, 70, W - 55, H - 70), outline=(201, 162, 83, 74), width=2)
    d.line((90, 170, W - 90, 170), fill=(201, 162, 83, 65), width=2)
    d.line((90, H - 190, W - 90, H - 190), fill=(201, 162, 83, 65), width=2)

    # Portrait circle.
    circle_size = 430
    portrait = profile.resize((circle_size, circle_size), Image.Resampling.LANCZOS)
    mask = Image.new("L", (circle_size, circle_size), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse((0, 0, circle_size - 1, circle_size - 1), fill=255)
    px = (W - circle_size) // 2
    py = 250 + (idx % 2) * 18
    d.ellipse((px - 10, py - 10, px + circle_size + 10, py + circle_size + 10), outline=GOLD + (150,), width=4)
    layer.paste(portrait, (px, py), mask)

    # Text stack.
    def center_text(y, text, font, fill):
        box = d.textbbox((0, 0), text, font=font)
        tw = box[2] - box[0]
        d.text(((W - tw) / 2, y), text, font=font, fill=fill)

    center_text(92, kicker, font_mono, MUTED + (255,))
    center_text(770, line1, font_big if idx == 1 else font_mid, BONE + (255,))
    center_text(895, line2, font_serif if idx == 1 else font_big, GOLD + (255,))
    center_text(1080, theme, font_mono, MUTED + (255,))
    center_text(1185, "WATCH ON IG", font_mono, GOLD_BRIGHT + (255,))

    # Play button.
    cx, cy, r = W // 2, 1325, 82
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=GOLD_BRIGHT + (180,), width=4, fill=(6, 4, 10, 92))
    d.polygon([(cx-24, cy-40), (cx-24, cy+40), (cx+46, cy)], fill=GOLD_BRIGHT + (230,))
    center_text(1480, "@RADIBARAKAT", font_small, MUTED + (255,))

    final = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    final.save(OUT / f"radi-reel-{idx}.jpg", quality=90, optimize=True, progressive=True)
    print(OUT / f"radi-reel-{idx}.jpg")
