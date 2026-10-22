# Hít Đất Bằng Mặt · Face Push-Up — site

Static GitHub Pages site for the Hít Đất Bằng Mặt iOS app: landing page (`index.html` Vietnamese, `en/` English),
privacy policy (`privacy/`) and support (`support/`), both bilingual with `#vi` / `#en` anchors.

Live: https://jarvis219.github.io/hit-dat-bang-mat-site/

- No analytics, no trackers, no external JavaScript. Fonts from Google Fonts (Rubik, Be Vietnam Pro). The landing page has
  one small inline script: the "Mũi" button that counts reps with the app's rules (hold ≥ 150 ms, ≥ 400 ms apart).
- Links are relative so the site works under `/hit-dat-bang-mat-site/`; only `404.html` uses root paths.

## Rebuild

```sh
python3 scripts/build_assets.py   # images and sounds from the app repo + screenshots + share cards + widgets
python3 scripts/build_pages.py    # every page, sitemap.xml, robots.txt (all copy lives in this script)
python3 scripts/check_links.py    # every local href/src exists
```

`build_assets.py` reads `APP_DIR` (default `../hit-dat-bang-mat`), `SHOTS_DIR` (simulator screenshots
`<lang>-<home|session|summary>.png`), `CARDS_DIR` and `WIDGETS_DIR` (PNGs from the app's `RenderTests` with
`TEST_RUNNER_SHARE_DIR` / `TEST_RUNNER_WIDGET_DIR`).
