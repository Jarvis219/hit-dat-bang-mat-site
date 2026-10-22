#!/usr/bin/env python3
"""Builds every image and sound the site uses into assets/.

Inputs (override with env vars):
  APP_DIR   the app repo (asset catalog, sounds, fonts)            default ../hit-dat-bang-mat
  SHOTS_DIR simulator screenshots <lang>-<home|session|summary>.png default raw-shots
  CARDS_DIR share cards from the app's RenderTests (TEST_RUNNER_SHARE_DIR)  default raw-cards
  WIDGETS_DIR widget renders from RenderTests (TEST_RUNNER_WIDGET_DIR)     default raw-widgets
"""
import os
import pathlib
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = pathlib.Path(os.environ.get("APP_DIR", ROOT.parent / "hit-dat-bang-mat"))
SHOTS = pathlib.Path(os.environ.get("SHOTS_DIR", ROOT / "raw-shots"))
CARDS = pathlib.Path(os.environ.get("CARDS_DIR", ROOT / "raw-cards"))
WIDGETS = pathlib.Path(os.environ.get("WIDGETS_DIR", ROOT / "raw-widgets"))
OUT = ROOT / "assets"
CAT = APP / "HitDat/Resources/Assets.xcassets"
CREAM = (251, 241, 220)
NAVY = (30, 39, 66)
ORANGE = (242, 103, 46)
YELLOW = (245, 197, 66)

MASCOTS = ["idle", "wave", "plank", "down", "cheer", "sweat", "question", "suspicious", "armscrossed",
           "faint", "flat", "champion", "flex", "sleep"]

def art(name):
    for path in [*CAT.glob(f"*/{name}.imageset/{name}.png"), *CAT.glob(f"*/{name}.imageset/{name}.jpg")]:
        return Image.open(path)
    raise FileNotFoundError(name)

def trim(image):
    image = image.convert("RGBA")
    box = image.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
    return image.crop(box) if box else image

def webp(image, path, longest, quality=86):
    image = image.copy()
    image.thumbnail((longest, longest), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "WEBP", quality=quality, method=6)

def font(size, weight="SemiBold"):
    return ImageFont.truetype(str(APP / f"HitDat/Resources/Fonts/BeVietnamPro-{weight}.ttf"), size)

def og(lang):
    """1200×630 poster: orange field, cream sunburst, the plank pug and the title."""
    W, H = 1200, 630
    canvas = Image.new("RGB", (W, H), ORANGE)
    d = ImageDraw.Draw(canvas)
    import math
    cx, cy = 880, 330
    for i in range(0, 24, 2):
        a0, a1 = i / 24 * 2 * math.pi, (i + 1) / 24 * 2 * math.pi
        d.polygon([(cx, cy), (cx + 1400 * math.cos(a0), cy + 1400 * math.sin(a0)),
                   (cx + 1400 * math.cos(a1), cy + 1400 * math.sin(a1))], fill=(246, 132, 84))
    d.rectangle([0, H - 70, W, H], fill=NAVY)
    pug = trim(art("mascot_plank"))
    pug.thumbnail((560, 400))
    canvas.paste(pug, (cx - pug.width // 2, H - 70 - pug.height + 20), pug)
    title = "Hít Đất\nBằng Mặt" if lang == "vi" else "Face\nPush-Up"
    sub = "Sấp mặt xuống, app đếm hộ." if lang == "vi" else "Face down. The phone counts."
    d.multiline_text((72, 90), title, font=font(96), fill=CREAM, spacing=4)
    d.text((76, 330), sub, font=font(36, "Medium"), fill=NAVY)
    d.rounded_rectangle([76, 410, 380, 470], radius=16, fill=NAVY)
    d.text((100, 421), "App Store · iOS", font=font(30), fill=CREAM)
    d.text((76, H - 52), "Miễn phí · offline · không quảng cáo" if lang == "vi" else "Free · offline · no ads",
           font=font(26, "Medium"), fill=CREAM)
    canvas.save(OUT / f"og-{lang}.png", optimize=True)

def main():
    icon = Image.open(CAT / "AppIcon.appiconset/AppIcon.png").convert("RGB")
    webp(icon, OUT / "img/icon.webp", 256)
    icon.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png")
    icon.resize((32, 32), Image.LANCZOS).save(OUT / "favicon-32.png")
    for mood in MASCOTS:
        webp(trim(art(f"mascot_{mood}")), OUT / f"img/mascot_{mood}.webp", 520)
    for name in [f"rank_{i}" for i in range(6)] + [f"voice_{v}" for v in ["bep", "coach", "mom", "boss", "robot"]] \
            + ["onb_place", "onb_fix", "fx_star", "fx_confetti", "fx_sweat"]:
        webp(trim(art(name)), OUT / f"img/{name}.webp", 420)
    webp(art("bg_gym").convert("RGB"), OUT / "img/bg_gym.webp", 1400, quality=78)
    for path in sorted(SHOTS.glob("*.png")):
        webp(ImageOps.exif_transpose(Image.open(path)).convert("RGB"), OUT / f"shots/{path.stem}.webp", 900, quality=82)
    for path in sorted(WIDGETS.glob("*.png")):
        webp(Image.open(path).convert("RGBA"), OUT / f"widgets/{path.stem}.webp", 720, quality=88)
    # <kind>.<id>_story_<lang>.png → cards/<kind>_<lang>.webp (a flagged session overwrites nothing: keep the first of each)
    for path in sorted(CARDS.glob("*_story_*.png")):
        kind, lang = path.stem.split(".")[0], path.stem.rsplit("_", 1)[1]
        target = OUT / f"cards/{kind}_{lang}.webp"
        if not target.exists():
            webp(Image.open(path).convert("RGB"), target, 720, quality=84)
    # The landing page's "Mũi" button plays the app's rep thud.
    (OUT / "audio").mkdir(parents=True, exist_ok=True)
    for name in ["snd_rep", "snd_half"]:
        src = APP / f"HitDat/Resources/Sounds/{name}.wav"
        subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "96000", str(src), str(OUT / f"audio/{name}.m4a")], check=True)
    og("vi")
    og("en")
    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"assets: {total / 1_000_000:.1f} MB")

if __name__ == "__main__":
    main()
