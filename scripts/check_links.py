#!/usr/bin/env python3
"""Every local href/src exists; no absolute links to the site itself (they break the sub-path), except 404.html."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
bad = []
for page in ROOT.rglob("*.html"):
    if page.name == "404.html":
        continue
    text = page.read_text(encoding="utf-8")
    for ref in re.findall(r'(?:href|src)="([^"]+)"', text):
        if ref.startswith(("http", "mailto:", "#", "data:")):
            continue
        target = (page.parent / ref.split("#")[0].split("?")[0])
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            bad.append(f"{page.relative_to(ROOT)} → {ref}")
    for css_ref in re.findall(r'url\("([^"]+)"\)', (ROOT / "assets/style.css").read_text()):
        if not (ROOT / "assets" / css_ref).exists():
            bad.append(f"style.css → {css_ref}")
print("\n".join(sorted(set(bad))) or "links ok")
sys.exit(1 if bad else 0)
