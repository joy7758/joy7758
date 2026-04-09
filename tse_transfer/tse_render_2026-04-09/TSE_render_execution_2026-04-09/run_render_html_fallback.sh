#!/bin/zsh
set -euo pipefail

ROOT="/Users/zhangbin/Desktop/TSE_render_handoff_2026-04-09"
WORK="/Users/zhangbin/Desktop/TSE_render_execution_2026-04-09"
PANDOC="/Users/zhangbin/.local/bin/pandoc"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CSL="/Users/zhangbin/.local/opt/ieee.csl"

python3 "$WORK/prepare_inputs.py"

"$PANDOC" \
  "$WORK/generated/main_body.md" \
  --standalone \
  --from markdown+raw_tex \
  --to html5 \
  --shift-heading-level-by=-1 \
  --metadata-file="$WORK/generated/main_metadata.yaml" \
  --bibliography "$ROOT/submission/58_references_tse.bib" \
  --csl "$CSL" \
  --citeproc \
  --template "$WORK/templates/main_template.html" \
  --css "$WORK/assets/ieee_like_main.css" \
  --output "$WORK/build/tse_main.html" \
  >"$WORK/logs/main_html.stdout.log" \
  2>"$WORK/logs/main_html.stderr.log"

"$PANDOC" \
  "$WORK/generated/appendix_body.md" \
  --standalone \
  --from markdown+raw_tex \
  --to html5 \
  --shift-heading-level-by=-1 \
  --metadata-file="$WORK/generated/appendix_metadata.yaml" \
  --template "$WORK/templates/main_template.html" \
  --css "$WORK/assets/ieee_like_appendix.css" \
  --output "$WORK/build/tse_appendix.html" \
  >"$WORK/logs/appendix_html.stdout.log" \
  2>"$WORK/logs/appendix_html.stderr.log"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --allow-file-access-from-files \
  --no-pdf-header-footer \
  --print-to-pdf="$WORK/build/tse_main.pdf" \
  "file://$WORK/build/tse_main.html" \
  >"$WORK/logs/chrome_main.stdout.log" \
  2>"$WORK/logs/chrome_main.stderr.log"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --allow-file-access-from-files \
  --no-pdf-header-footer \
  --print-to-pdf="$WORK/build/tse_appendix.pdf" \
  "file://$WORK/build/tse_appendix.html" \
  >"$WORK/logs/chrome_appendix.stdout.log" \
  2>"$WORK/logs/chrome_appendix.stderr.log"
