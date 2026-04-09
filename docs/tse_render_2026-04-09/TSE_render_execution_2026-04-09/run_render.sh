#!/bin/zsh
set -euo pipefail

ROOT="/Users/zhangbin/Desktop/TSE_render_handoff_2026-04-09"
WORK="/Users/zhangbin/Desktop/TSE_render_execution_2026-04-09"
PANDOC="/Users/zhangbin/.local/bin/pandoc"
TECTONIC="/Users/zhangbin/.local/bin/tectonic"
CSL="/Users/zhangbin/.local/opt/ieee.csl"

python3 "$WORK/prepare_inputs.py"

"$PANDOC" \
  "$WORK/generated/main_body.md" \
  --standalone \
  --from markdown+raw_tex \
  --shift-heading-level-by=-1 \
  --metadata-file="$WORK/generated/main_metadata.yaml" \
  --bibliography "$ROOT/submission/58_references_tse.bib" \
  --csl "$CSL" \
  --citeproc \
  --pdf-engine="$TECTONIC" \
  --output "$WORK/build/tse_main.pdf" \
  >"$WORK/logs/main.stdout.log" \
  2>"$WORK/logs/main.stderr.log"

"$PANDOC" \
  "$WORK/generated/appendix_body.md" \
  --standalone \
  --from markdown+raw_tex \
  --shift-heading-level-by=-1 \
  --metadata-file="$WORK/generated/appendix_metadata.yaml" \
  --pdf-engine="$TECTONIC" \
  --output "$WORK/build/tse_appendix.pdf" \
  >"$WORK/logs/appendix.stdout.log" \
  2>"$WORK/logs/appendix.stderr.log"
