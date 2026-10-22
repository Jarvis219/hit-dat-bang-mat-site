#!/usr/bin/env python3
"""Generates every page of the site: landing (vi at /, en at /en/), privacy and support
(bilingual with #vi / #en anchors), 404, sitemap.xml and robots.txt.

    python3 scripts/build_pages.py

All copy lives in this file. Links are relative so the site works under /hit-dat-bang-mat-site/.
"""
import hashlib
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://jarvis219.github.io/hit-dat-bang-mat-site/"
EMAIL = "jarvis.219.studio@gmail.com"
EFFECTIVE_VI = "22/10/2026"
EFFECTIVE_EN = "October 22, 2026"
CSS_VERSION = hashlib.sha1((ROOT / "assets/style.css").read_bytes()).hexdigest()[:8]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700'
         '&family=Rubik:wght@700;800;900&display=swap" rel="stylesheet">')

TITLES = {
    "vi": ["Sấp mặt", "Mũi chạm sàn", "Má phính", "Mặt dày", "Mũi bẹp", "Trán sắt", "Người không cổ"],
    "en": ["Face Down", "Nose Touch", "Chubby Cheeks", "Thick Skin", "Flat Nose", "Iron Forehead", "The Neckless"],
}
THRESHOLDS = [0, 1, 5, 10, 20, 50, 100]

COPY = {
    "vi": {
        "lang": "vi", "name": "Hít Đất Bằng Mặt", "path": "",
        "title": "Hít Đất Bằng Mặt · Sấp mặt xuống, app đếm hộ",
        "description": "Đặt iPhone ngửa trên sàn dưới mũi, cảm biến tiệm cận đếm hộ số cái hít đất. Bẹp đếm thành tiếng, hỏi \"ngủ à?\" và đóng dấu CÓ MÙI GIAN LẬN nếu bạn dùng tay. Miễn phí, offline.",
        "eyebrow": "App iOS · miễn phí",
        "h1": "Hít Đất<br>Bằng Mặt",
        "tagline": "Không cần đếm. Cứ sấp mặt xuống. Cảm biến lo phần đếm, Bẹp lo phần cà khịa.",
        "store": "Sắp có trên App Store", "store_small": "iPhone & iPad · iOS 17+",
        "support": "Hỗ trợ",
        "pills": ["Không quảng cáo", "Không tài khoản", "Không xin camera", "Tiếng Việt · English"],
        "nose": "Mũi", "nose_hint": "Giữ nút Mũi một chút rồi thả = 1 cái",
        "quip_half": "nửa cái thôi", "quip_fast": "tay hay mặt đấy?", "quip_ten": "Mười cái. Mặt dày rồi đấy.",
        "steps_title": "Cách hít",
        "steps": [
            ("onb_place", "Đặt máy xuống sàn", "Ngửa màn hình, ngay dưới mũi, cách ngực một gang tay. Không cần cầm gì."),
            ("mascot_plank", "Nằm xuống", "Bấm Nằm xuống, đếm ngược 5 giây. Máy phải yên trên sàn thì số mới chạy."),
            ("mascot_down", "Sấp mặt", "Mặt cúi sát màn hình rồi ngẩng lên là một cái. Màn hình đen lúc gần là bình thường, Bẹp vẫn đếm thành tiếng."),
        ],
        "features_title": "Vô tri nhưng đếm thật",
        "features": [
            ("mascot_question", "\"Ngủ à?\"", "Nằm im quá 4 giây là bị hỏi, 20 giây là bị ghi \"gục\". Thả quá nhanh thì chỉ được nửa cái."),
            ("mascot_armscrossed", "Nhấc máy là dừng", "Gia tốc kế biết khi bạn nhấc máy lên. Bẹp khoanh tay chờ, đặt xuống yên 2 giây là đếm tiếp."),
            ("fx_star", "Thử thách 1 phút", "60 giây, bao nhiêu cái? Có kỷ lục riêng và thẻ share riêng để thách cả nhóm."),
            ("rank_5", "Cấp bậc & 19 thành tựu", "Từ Lính mới tới Huyền thoại sấp mặt. Có thành tựu cho người nằm 0 cái."),
            ("mascot_flex", "Mục tiêu, chuỗi, thử thách tháng", "Mục tiêu ngày 10 đến 100 cái, chuỗi ngày liên tiếp, 300 đến 1.000 cái mỗi tháng."),
            ("mascot_cheer", "Widget & nhắc nhở", "Widget có nút Nằm xuống vào thẳng buổi tập. Nhắc một lần mỗi ngày, ngày đã đủ thì im."),
        ],
        "titles_title": "Danh hiệu mỗi buổi", "titles_sub": "Đếm xong là được phong, theo số cái trong một buổi.",
        "cheat_title": "Có mùi gian lận", "stamp": "Có mùi gian lận",
        "cheat_body": "Ba lần liên tiếp nhanh hơn 2 cái một giây là Bẹp nghi bạn dùng tay. Ba lần nghi thì buổi đó bị đóng dấu đỏ, vẫn tính cho ngày nhưng không tính kỷ lục và cấp bậc. Dấu còn hiện trên thẻ share, cho cả nhóm cười.",
        "voices_title": "5 giọng đếm", "voices_sub": "Mở dần theo tổng số cái sạch. Đọc bằng giọng máy ngay trên iPhone, không cần mạng.",
        "voices": [("bep", "Bẹp", "\"Hự. Được đấy.\""), ("coach", "Huấn luyện viên", "\"Nữa! Đừng bỏ!\""),
                   ("mom", "Mẹ", "\"Con ăn cơm chưa?\""), ("boss", "Sếp", "\"Deadline đâu?\""), ("robot", "Robot", "\"Rep hai. Hiệu suất thấp.\"")],
        "share_title": "Thách cả nhóm", "share_sub": "Mỗi buổi một thẻ rực rỡ, story 9:16 hoặc vuông 1:1. Bật \"Thách bạn bè\" để có dòng \"Tôi 23 cái, bạn mấy?\".",
        "widgets_title": "Ngay trên màn hình chính",
        "widgets_sub": "Số cái hôm nay, vòng mục tiêu, chuỗi ngày, thanh thử thách tháng, và nút Nằm xuống.",
        "shots_title": "Trong app",
        "shots": [("home", "Hôm nay"), ("session", "Đang đếm"), ("summary", "Tổng kết")],
        "promise_title": "Lời hứa của Bẹp",
        "promise_sub": "Không gì rời khỏi máy bạn. Không bán gì cho bạn.",
        "promise": ["Miễn phí mãi mãi", "Không mua trong app", "Không quảng cáo", "Không theo dõi", "Không camera, không micro", "Dữ liệu chỉ trên máy"],
        "faq_title": "Hỏi nhanh",
        "faq": [
            ("App đếm bằng cách nào?", "Bằng cảm biến tiệm cận ở cạnh trên iPhone, cái làm tắt màn hình khi bạn áp máy lên tai. Mặt lại gần là cảm biến bật, ngẩng lên là tắt, mỗi vòng là một cái."),
            ("Có cần camera không?", "Không. App không xin camera, không xin micro. Quyền duy nhất có thể hỏi là thông báo, và chỉ hỏi sau buổi tập đầu tiên."),
            ("Dùng trên iPad được không?", "Được. iPad không có cảm biến tiệm cận, nên trên iPad chính màn hình là cảm biến: đặt iPad nằm ngửa dưới mặt, mũi chạm màn hình là một cái. Vẫn đủ luật nửa cái, \"ngủ à?\" và dấu gian lận."),
            ("App có tốn tiền không?", "Không. Miễn phí hoàn toàn, không mua trong app, không quảng cáo. Giọng đếm mới mở bằng số cái bạn hít."),
        ],
        "privacy": "Quyền riêng tư", "other_lang": "English", "other_href": "en/",
        "rights": "© 2026 Jarvis 219 Studio. Ảnh minh hoạ và nội dung thuộc về Hít Đất Bằng Mặt.",
    },
    "en": {
        "lang": "en", "name": "Face Push-Up", "path": "en/",
        "title": "Face Push-Up · Face down, the phone counts",
        "description": "Put your iPhone face up on the floor under your nose and the proximity sensor counts your push-ups. Bep the pug counts out loud, asks \"asleep?\" and stamps SMELLS LIKE CHEATING on hand-made reps. Free, offline.",
        "eyebrow": "iOS app · free",
        "h1": "Face<br>Push-Up",
        "tagline": "No counting. Just face down. The sensor does the counting, Bep the pug does the trash talk.",
        "store": "Coming to the App Store", "store_small": "iPhone & iPad · iOS 17+",
        "support": "Support",
        "pills": ["No ads", "No account", "No camera", "English · Tiếng Việt"],
        "nose": "Nose", "nose_hint": "Hold the Nose button a moment, let go = 1 rep",
        "quip_half": "half a rep", "quip_fast": "hand or face?", "quip_ten": "Ten. Officially thick-skinned.",
        "steps_title": "How it works",
        "steps": [
            ("onb_place", "Phone on the floor", "Screen up, right under your nose, about a hand's width from your chest. Nothing to hold."),
            ("mascot_plank", "Get down", "Tap Get down and a 5-second countdown starts. The numbers only run once the phone is still."),
            ("mascot_down", "Face down", "Lower your face to the screen and come back up: one rep. The screen goes dark while you're close; Bep keeps counting out loud."),
        ],
        "features_title": "Pointless, but it really counts",
        "features": [
            ("mascot_question", "\"Asleep?\"", "Stay down for 4 seconds and you get asked; 20 seconds and it's logged as a floor nap. Too quick counts as half a rep."),
            ("mascot_armscrossed", "Lift it, it pauses", "The accelerometer knows when the phone leaves the floor. Bep crosses his arms; two still seconds and counting resumes."),
            ("fx_star", "One-minute challenge", "Sixty seconds, how many? Its own record and its own share card to dare the group chat."),
            ("rank_5", "Ranks & 19 badges", "From Rookie to Face-Down Legend. There's even a badge for a set of zero."),
            ("mascot_flex", "Goals, streaks, monthly challenge", "A daily goal from 10 to 100, a day streak, and 300 to 1,000 reps a month."),
            ("mascot_cheer", "Widgets & reminders", "A widget with a Get down button straight into a set. One nudge a day, silent once you're done."),
        ],
        "titles_title": "Every set gets a title", "titles_sub": "Earned by the number of reps in one set.",
        "cheat_title": "Smells like cheating", "stamp": "Smells like cheating",
        "cheat_body": "Three reps in a row faster than two a second and Bep suspects a hand. Three suspicions and the set gets a red stamp: it still counts for the day, never for records or ranks. The stamp shows up on the share card too, for the group chat's enjoyment.",
        "voices_title": "5 counting voices", "voices_sub": "Unlocked by lifetime clean reps. Spoken by the iPhone's own voice, no network needed.",
        "voices": [("bep", "Bep", "\"Oof. Not bad.\""), ("coach", "Coach", "\"More! Don't quit!\""),
                   ("mom", "Mom", "\"Have you eaten?\""), ("boss", "Boss", "\"Where's the deadline?\""), ("robot", "Robot", "\"Rep two. Low efficiency.\"")],
        "share_title": "Dare the group chat", "share_sub": "A loud card for every set, as a 9:16 story or a 1:1 square. Turn on \"Challenge a friend\" for \"I did 23. You?\".",
        "widgets_title": "Right on your home screen",
        "widgets_sub": "Today's reps, the goal ring, your streak, the monthly bar, and a Get down button.",
        "shots_title": "Inside the app",
        "shots": [("home", "Today"), ("session", "Counting"), ("summary", "Summary")],
        "promise_title": "Bep's promise",
        "promise_sub": "Nothing leaves your phone. Nothing is for sale.",
        "promise": ["Free forever", "No in-app purchases", "No ads", "No tracking", "No camera, no microphone", "Data stays on device"],
        "faq_title": "Quick answers",
        "faq": [
            ("How does it count?", "With the proximity sensor at the top edge of the iPhone, the one that turns the screen off when you hold the phone to your ear. Face close switches it on, face up switches it off; each cycle is one rep."),
            ("Does it need the camera?", "No. No camera, no microphone. The only permission it may ask for is notifications, and only after your first set."),
            ("Does it work on iPad?", "Yes. iPads have no proximity sensor, so on iPad the screen itself is the sensor: lay it face up under your face and a nose touch is a rep. Half reps, \"asleep?\" and the cheat stamp all still apply."),
            ("Does it cost anything?", "No. Completely free, no in-app purchases, no ads. New voices unlock with the reps you do."),
        ],
        "privacy": "Privacy", "other_lang": "Tiếng Việt", "other_href": "../",
        "rights": "© 2026 Jarvis 219 Studio. Artwork and copy belong to Face Push-Up / Hít Đất Bằng Mặt.",
    },
}

e = html.escape

def head(title, description, canonical, prefix, lang, og, alternates=""):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canonical}">
{alternates}<meta name="theme-color" content="#F2672E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hít Đất Bằng Mặt · Face Push-Up">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}assets/og-{og}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}assets/og-{og}.png">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css?v={CSS_VERSION}">
</head>
"""

def topbar(prefix, name, lang_links):
    links = "".join(f'<a href="{href}" hreflang="{code}"{" aria-current=\"true\"" if current else ""}>{label}</a>'
                    for code, label, href, current in lang_links)
    return f"""<div class="wrap top">
  <a class="brand" href="{prefix}"><img src="{prefix}assets/img/icon.webp" width="44" height="44" alt=""><span>{e(name)}</span></a>
  <nav class="lang-switch" aria-label="Language">{links}</nav>
</div>
"""

def footer(prefix, c):
    return f"""<footer>
  <div class="wrap">
    <nav>
      <a href="{prefix}privacy/#{c['lang']}">{c['privacy']}</a>
      <a href="{prefix}support/#{c['lang']}">{c['support']}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </nav>
    <div>{e(c['rights'])}</div>
  </div>
</footer>
"""

def landing(c):
    lang = c["lang"]
    prefix = "" if lang == "vi" else "../"
    canonical = BASE + c["path"]
    alternates = (f'<link rel="alternate" hreflang="vi" href="{BASE}">\n'
                  f'<link rel="alternate" hreflang="en" href="{BASE}en/">\n'
                  f'<link rel="alternate" hreflang="x-default" href="{BASE}">\n')
    langs = [("vi", "Tiếng Việt", prefix, lang == "vi"), ("en", "English", f"{prefix}en/", lang == "en")]
    pills = "".join(f'<span class="pill">{e(p)}</span>' for p in c["pills"])
    steps = "".join(f"""
      <div class="card step"><img src="{prefix}assets/img/{img}.webp" alt="" loading="lazy"><div class="n">0{i + 1}</div><h3>{e(t)}</h3><p class="muted">{e(d)}</p></div>"""
                    for i, (img, t, d) in enumerate(c["steps"]))
    features = "".join(f"""
      <div class="card feature"><img src="{prefix}assets/img/{img}.webp" alt="" loading="lazy"><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>"""
                       for img, t, d in c["features"])
    ladder = "".join(f"<div><b>{n}{'+' if i == len(THRESHOLDS) - 1 else ''}</b><span>{e(t)}</span></div>"
                     for i, (n, t) in enumerate(zip(THRESHOLDS, TITLES[lang])))
    voices = "".join(f"""<figure><img src="{prefix}assets/img/voice_{k}.webp" alt="" loading="lazy"><figcaption><b>{e(n)}</b><span>{e(q)}</span></figcaption></figure>"""
                     for k, n, q in c["voices"])
    cards = "".join(f'<img src="{prefix}assets/cards/{k}_{lang}.webp" alt="" loading="lazy">' for k in ["session", "challenge", "rank", "month"])
    shots = "".join(f'<img src="{prefix}assets/shots/{lang}-{k}.webp" alt="{e(n)}" loading="lazy">' for k, n in c["shots"])
    widgets = (f'<div class="widgets">'
               f'<img class="w-small" src="{prefix}assets/widgets/{lang}-small.webp" alt="" loading="lazy">'
               f'<img class="w-medium" src="{prefix}assets/widgets/{lang}-medium.webp" alt="" loading="lazy">'
               f'</div>')
    promise = "".join(f"<li>{e(p)}</li>" for p in c["promise"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    data = json.dumps({"titles": TITLES[lang], "thresholds": THRESHOLDS, "half": c["quip_half"],
                       "fast": c["quip_fast"], "ten": c["quip_ten"]}, ensure_ascii=False)
    return head(c["title"], c["description"], canonical, prefix, lang, lang, alternates) + f"""<body>
{topbar(prefix, c['name'], langs)}
<main>
  <div class="hero-band">
    <div class="wrap hero">
      <div>
        <div class="eyebrow">{e(c['eyebrow'])}</div>
        <h1>{c['h1']}</h1>
        <p class="tagline">{e(c['tagline'])}</p>
        <div class="cta">
          <span class="btn primary" aria-disabled="true"><span>{e(c['store'])}<small>{e(c['store_small'])}</small></span></span>
          <a class="btn ghost" href="{prefix}support/#{lang}">{e(c['support'])}</a>
        </div>
        <div class="pills">{pills}</div>
      </div>
      <div class="stage" id="stage">
        <div class="quip" id="quip" aria-live="polite"></div>
        <div class="counter"><b id="count">0</b><div class="title" id="title">{e(TITLES[lang][0])}</div></div>
        <img class="pug" id="pug" src="{prefix}assets/img/mascot_plank.webp" alt="">
        <button type="button" class="nose" id="nose">{e(c['nose'])}</button>
        <div class="hint">{e(c['nose_hint'])}</div>
      </div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <h2>{e(c['steps_title'])}</h2>
      <div class="grid3">{steps}
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <h2>{e(c['features_title'])}</h2>
      <div class="grid2">{features}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['titles_title'])}</h2>
      <p class="muted">{e(c['titles_sub'])}</p>
      <div class="ladder">{ladder}</div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap cheat">
      <img src="{prefix}assets/img/mascot_suspicious.webp" alt="" loading="lazy">
      <div>
        <h2>{e(c['cheat_title'])}</h2>
        <p><span class="stamp">{e(c['stamp'])}</span></p>
        <p>{e(c['cheat_body'])}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['voices_title'])}</h2>
      <p class="muted">{e(c['voices_sub'])}</p>
      <div class="voices">{voices}</div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <h2>{e(c['share_title'])}</h2>
      <p class="muted">{e(c['share_sub'])}</p>
      <div class="shots cards">{cards}</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['widgets_title'])}</h2>
      <p class="muted">{e(c['widgets_sub'])}</p>
      {widgets}
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <h2>{e(c['shots_title'])}</h2>
      <div class="shots">{shots}</div>
    </div>
  </section>

  <section class="promise">
    <div class="wrap">
      <img src="{prefix}assets/img/mascot_champion.webp" alt="" width="190" style="margin:0 auto 10px" loading="lazy">
      <h2>{e(c['promise_title'])}</h2>
      <p class="muted">{e(c['promise_sub'])}</p>
      <ul>{promise}</ul>
    </div>
  </section>

  <section>
    <div class="wrap" style="max-width:780px">
      <h2>{e(c['faq_title'])}</h2>
      {faq}
    </div>
  </section>
</main>
{footer(prefix, c)}
<audio id="thud" src="{prefix}assets/audio/snd_rep.m4a" preload="auto"></audio>
<audio id="droop" src="{prefix}assets/audio/snd_half.m4a" preload="auto"></audio>
<script>
(() => {{
  // The app's rep rules in miniature: hold ≥ 150 ms, reps ≥ 400 ms apart, three gaps < 500 ms = suspicious.
  const T = {data}, img = "{prefix}assets/img/";
  const stage = document.getElementById("stage"), nose = document.getElementById("nose"), count = document.getElementById("count"),
        title = document.getElementById("title"), pug = document.getElementById("pug"), quip = document.getElementById("quip"),
        thud = document.getElementById("thud"), droop = document.getElementById("droop");
  let n = 0, downAt = 0, last = 0, gaps = [], quipTimer = 0, isDown = false;
  const play = (a) => {{ try {{ a.currentTime = 0; a.play(); }} catch (e) {{}} }};
  const say = (text, bad) => {{
    quip.textContent = text; quip.className = "quip show" + (bad ? " bad" : "");
    clearTimeout(quipTimer); quipTimer = setTimeout(() => quip.className = "quip", 1600);
  }};
  const mood = (m) => pug.src = img + "mascot_" + m + ".webp";
  const down = (ev) => {{ if (isDown) return; isDown = true; ev.preventDefault(); downAt = performance.now(); stage.classList.add("down"); mood("down"); }};
  const up = () => {{
    if (!isDown) return; isDown = false; stage.classList.remove("down");
    const now = performance.now();
    if (now - downAt < 150) {{ play(droop); say(T.half); mood("question"); return; }}
    if (last && now - last < 400) {{ mood("plank"); return; }}
    if (last) {{ gaps.push(now - last); if (gaps.length > 3) gaps.shift(); }}
    last = now; n += 1; play(thud);
    count.textContent = n.toLocaleString(document.documentElement.lang);
    let i = 0; T.thresholds.forEach((t, k) => {{ if (n >= t) i = k; }});
    title.textContent = T.titles[i];
    if (gaps.length === 3 && gaps.every(g => g < 500)) {{ say(T.fast, true); mood("suspicious"); gaps = []; return; }}
    if (n === 10) say(T.ten);
    mood(n % 10 === 0 ? "cheer" : "plank");
  }};
  nose.addEventListener("pointerdown", down);
  window.addEventListener("pointerup", up);
  window.addEventListener("pointercancel", up);
  nose.addEventListener("keydown", (ev) => {{ if ((ev.key === " " || ev.key === "Enter") && !ev.repeat) down(ev); }});
  nose.addEventListener("keyup", (ev) => {{ if (ev.key === " " || ev.key === "Enter") up(); }});
}})();
</script>
</body>
</html>
"""

PRIVACY = {
    "vi": f"""
<h2>Tóm tắt</h2>
<p><span class="seal">Không thu thập dữ liệu</span></p>
<p>Hít Đất Bằng Mặt không thu thập, không gửi đi và không bán bất kỳ dữ liệu nào của bạn. App không có tài khoản, không có máy chủ, không quảng cáo, không công cụ phân tích hay theo dõi của bên thứ ba, và không có code kết nối mạng.</p>
<h3>Dữ liệu nằm ở đâu</h3>
<ul>
<li>Lịch sử buổi tập (số cái, thời gian, nhịp, danh hiệu, dấu gian lận), chuỗi ngày, thành tựu và cài đặt được lưu trong bộ nhớ của app trên chính thiết bị của bạn.</li>
<li>Widget đọc một bản tóm tắt nhỏ (số cái hôm nay, chuỗi ngày, tiến độ tháng) qua vùng chia sẻ giữa app và widget trên cùng thiết bị.</li>
</ul>
<h3>Cảm biến app sử dụng</h3>
<ul>
<li><strong>Cảm biến tiệm cận:</strong> để đếm mỗi lần mặt bạn lại gần màn hình. Chỉ bật trong lúc tập, chỉ cho biết "gần" hay "xa", không có hình ảnh. Không lưu, không gửi đi.</li>
<li><strong>Chuyển động (Motion):</strong> để biết khi máy bị nhấc khỏi sàn và tạm dừng buổi tập. Chỉ bật trong lúc tập, xử lý ngay trên máy, không lưu, không gửi đi.</li>
<li><strong>Giọng đếm:</strong> do bộ đọc văn bản có sẵn của iOS phát ngay trên máy. App không dùng micro.</li>
<li>App <strong>không</strong> dùng camera, micro, vị trí, danh bạ hay dữ liệu Sức khoẻ.</li>
</ul>
<h3>Thông báo</h3>
<p>Nếu bạn cho phép (app chỉ hỏi sau buổi tập đầu tiên), app lên lịch nhắc tập và nhắc giữ chuỗi. Đây là thông báo cục bộ trên máy, không qua máy chủ. Tắt được trong Cài đặt của app hoặc của iOS.</p>
<h3>Sao lưu</h3>
<p>Chỉ khi bạn bấm Xuất bản sao lưu, app tạo một file JSON và mở bảng chia sẻ của iOS để bạn tự chọn nơi lưu.</p>
<h3>Trẻ em</h3>
<p>App phù hợp mọi lứa tuổi và không thu thập dữ liệu của bất kỳ ai, kể cả trẻ em.</p>
<h3>Xoá dữ liệu</h3>
<p>Vào Cài đặt → Xoá hết dữ liệu, hoặc xoá app.</p>
<h3>Thay đổi chính sách</h3>
<p>Nếu chính sách thay đổi, trang này sẽ được cập nhật kèm ngày hiệu lực mới.</p>
<h3>Liên hệ</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
    "en": f"""
<h2>Summary</h2>
<p><span class="seal">Data Not Collected</span></p>
<p>Face Push-Up (Hít Đất Bằng Mặt) does not collect, transmit or sell any of your data. There is no account, no server, no advertising, no third-party analytics or tracking, and no networking code.</p>
<h3>Where your data lives</h3>
<ul>
<li>Your set history (reps, time, pace, titles, cheat stamps), streak, achievements and settings are stored in the app's own storage on your device.</li>
<li>The widget reads a small summary (today's reps, streak, monthly progress) through the app group shared between the app and its widget on the same device.</li>
</ul>
<h3>Sensors</h3>
<ul>
<li><strong>Proximity sensor:</strong> to count each time your face comes close to the screen. On only during a set; it only reports "near" or "far", with no image. Never stored or sent.</li>
<li><strong>Motion:</strong> to notice when the phone is lifted off the floor and pause the set. On only during a set, processed on the device, never stored or sent.</li>
<li><strong>Counting voice:</strong> spoken by iOS's built-in speech synthesizer on the device. The app does not use the microphone.</li>
<li>The app does <strong>not</strong> use the camera, microphone, location, contacts or Health data.</li>
</ul>
<h3>Notifications</h3>
<p>If you allow them (the app only asks after your first set), it schedules a workout nudge and a streak reminder. These are local notifications on the device, with no server involved. Turn them off in the app's or iOS Settings.</p>
<h3>Backups</h3>
<p>Only when you tap Export backup, the app creates a JSON file and opens the iOS share sheet so you choose where it goes.</p>
<h3>Children</h3>
<p>The app is suitable for all ages and collects no data from anyone, including children.</p>
<h3>Deleting your data</h3>
<p>Use Settings → Erase everything, or delete the app.</p>
<h3>Changes</h3>
<p>If this policy changes, this page will be updated with a new effective date.</p>
<h3>Contact</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
}

SUPPORT = {
    "vi": [
        ("Máy không đếm", "Cảm biến tiệm cận nằm ở cạnh trên màn hình, cạnh loa thoại. Ốp lưng dày hoặc một số miếng dán màn hình có thể che mất, thử tháo ốp. Vào Cài đặt → Thử lại cảm biến để kiểm tra: chấm tròn xanh là máy đã nhận."),
        ("Màn hình tắt đen khi cúi xuống", "Bình thường. iOS tự tắt màn hình khi có vật lại gần cảm biến, giống lúc bạn nghe điện thoại. Vì vậy Bẹp đếm thành tiếng và rung mỗi cái."),
        ("Không nghe giọng đếm", "Kiểm tra Cài đặt → Đếm bằng giọng và âm lượng. Giọng phát cả khi gạt im lặng. Nếu máy chưa có giọng tiếng Việt: Cài đặt iOS → Trợ năng → Nội dung đọc → Giọng nói → Tiếng Việt, rồi tải một giọng."),
        ("Bị đóng dấu \"Có mùi gian lận\" dù tập thật", "Dấu chỉ hiện khi ba lần liên tiếp nhanh hơn 2 cái một giây. Mỗi cái hãy cúi xuống hẳn và ngẩng lên hẳn. Buổi bị dấu vẫn tính cho ngày và chuỗi."),
        ("Buổi tập cứ tạm dừng", "Gia tốc kế nghĩ máy bị nhấc. Đặt máy trên sàn cứng, đừng tập trên giường hay đệm mềm, và đừng chạm vào máy khi đang tập."),
        ("Nửa cái là gì?", "Mặt chỉ lướt qua cảm biến dưới 0,15 giây thì không tính. Giữ mặt sát một nhịp rồi mới ngẩng lên."),
        ("Mất chuỗi ngày", "Chuỗi tính theo ngày đủ mục tiêu. Hạ mục tiêu ngày trong Cài đặt nếu bạn hay lỡ. Mất chuỗi không bị phạt gì."),
        ("Đổi máy mới", "Cài đặt → Xuất bản sao lưu trên máy cũ, gửi file sang máy mới rồi Nhập bản sao lưu. File có chữ ký chống sửa, hãy dùng đúng file gốc."),
        ("Dùng trên iPad thế nào?", "iPad không có cảm biến tiệm cận nên đếm bằng màn hình: đặt iPad nằm ngửa trên sàn, mũi chạm màn hình rồi nhấc lên là một cái. Lúc mũi đang chạm, nền chuyển xanh. Nút Xong vẫn giữ 1 giây như iPhone."),
    ],
    "en": [
        ("It doesn't count", "The proximity sensor sits at the top edge of the screen, next to the earpiece. Thick cases and some screen protectors cover it; try without the case. Settings → Test the sensor checks it: the dot turns green when the phone sees you."),
        ("The screen goes black when I go down", "That's normal. iOS turns the screen off when something is close to the sensor, as during a phone call. That's why Bep counts out loud and buzzes for every rep."),
        ("I can't hear the count", "Check Settings → Count out loud and the volume. The voice plays even with the silent switch on. No Vietnamese voice? iOS Settings → Accessibility → Spoken Content → Voices, and download one."),
        ("I got \"Smells like cheating\" for real reps", "The stamp only appears after three runs faster than two reps a second. Go all the way down and all the way up each time. A stamped set still counts for the day and the streak."),
        ("The set keeps pausing", "The accelerometer thinks the phone was lifted. Put it on a hard floor, not a bed or soft mat, and don't touch it during the set."),
        ("What's a half rep?", "A face that only brushes the sensor for under 0.15 seconds doesn't count. Hold close for a beat, then come up."),
        ("I lost my streak", "A streak counts days you reach the goal. Lower the daily goal in Settings if you miss it often. Losing a streak costs nothing."),
        ("Moving to a new phone", "Settings → Export backup on the old phone, send the file over and Import backup. Backups are signed; use the original file."),
        ("How does it work on iPad?", "iPads have no proximity sensor, so the screen counts: lay the iPad face up on the floor, touch the screen with your nose and come back up. The screen turns green while your nose is on it. Hold Done for one second, as on iPhone."),
    ],
}

def doc_page(kind):
    prefix = "../"
    is_privacy = kind == "privacy"
    title = ("Chính sách quyền riêng tư · Privacy Policy — Hít Đất Bằng Mặt" if is_privacy
             else "Hỗ trợ · Support — Hít Đất Bằng Mặt")
    description = ("Hít Đất Bằng Mặt không thu thập dữ liệu: không tài khoản, không máy chủ, không camera. · Face Push-Up collects no data."
                   if is_privacy else "Câu hỏi thường gặp và liên hệ hỗ trợ cho Hít Đất Bằng Mặt (Face Push-Up).")
    mascot = "mascot_sleep" if is_privacy else "mascot_wave"
    langs = [("vi", "Tiếng Việt", "#vi", False), ("en", "English", "#en", False)]
    sections = []
    for lang in ("vi", "en"):
        heading = {"vi": ("Chính sách quyền riêng tư" if is_privacy else "Hỗ trợ"),
                   "en": ("Privacy Policy" if is_privacy else "Support")}[lang]
        if is_privacy:
            date = f"Hiệu lực từ {EFFECTIVE_VI}" if lang == "vi" else f"Effective {EFFECTIVE_EN}"
            inner = f'<p class="date">{date}</p>{PRIVACY[lang]}'
        else:
            faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in SUPPORT[lang])
            contact = ("Không thấy câu trả lời? Gửi email, kèm phiên bản app (Cài đặt → Giới thiệu) và đời iPhone:"
                       if lang == "vi" else "Didn't find it? Email us with the app version (Settings → About) and your iPhone model:")
            inner = (f'{faq}<h3>{"Liên hệ" if lang == "vi" else "Contact"}</h3><p>{contact} '
                     f'<a href="mailto:{EMAIL}?subject=H%C3%ADt%20%C4%90%E1%BA%A5t">{EMAIL}</a></p>')
        sections.append(f'<article class="card" id="{lang}" lang="{lang}"><h2>{heading}</h2>{inner}</article>')
    canonical = BASE + kind + "/"
    return head(title, description, canonical, prefix, "vi", "vi") + f"""<body>
{topbar(prefix, "Hít Đất Bằng Mặt", langs)}
<main class="wrap doc">
  <header>
    <img class="mascot" src="{prefix}assets/img/{mascot}.webp" alt="">
    <h1 style="font-size:clamp(34px,6vw,54px)">{"Quyền riêng tư · Privacy" if is_privacy else "Hỗ trợ · Support"}</h1>
    <p class="muted">Hít Đất Bằng Mặt · Face Push-Up</p>
  </header>
  {"".join(sections)}
</main>
{footer(prefix, COPY['vi'])}
</body>
</html>
"""

def not_found():
    root = "/hit-dat-bang-mat-site/"
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 · Hít Đất Bằng Mặt</title>
{FONTS}
<link rel="stylesheet" href="{root}assets/style.css?v={CSS_VERSION}">
</head>
<body>
<main class="wrap doc" style="text-align:center;padding-top:60px">
  <img src="{root}assets/img/mascot_flat.webp" alt="" width="240" style="margin:0 auto">
  <h1 style="font-size:52px">404</h1>
  <p>Trang này gục rồi. · This page is face down.</p>
  <p><a class="btn primary" href="{root}">Về trang chủ · Home</a></p>
</main>
</body>
</html>
"""

def main():
    (ROOT / "index.html").write_text(landing(COPY["vi"]), encoding="utf-8")
    (ROOT / "en/index.html").write_text(landing(COPY["en"]), encoding="utf-8")
    (ROOT / "privacy/index.html").write_text(doc_page("privacy"), encoding="utf-8")
    (ROOT / "support/index.html").write_text(doc_page("support"), encoding="utf-8")
    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")
    urls = ["", "en/", "privacy/", "support/"]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    print("pages written")

if __name__ == "__main__":
    main()
