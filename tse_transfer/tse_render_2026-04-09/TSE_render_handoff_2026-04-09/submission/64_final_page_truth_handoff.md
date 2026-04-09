# Final Page-Truth Handoff

## Current Status

Final citation-complete page-truth has not been achieved locally because the
current repo environment still lacks a suitable document assembly toolchain.

Unavailable local tools in the current environment:

- `pandoc`
- `pdflatex`
- `xelatex`
- `tectonic`

Because of that, no reliable final compiled page count is available from this
round.

## Exact Human Handoff Steps

1. Compile from the canonical TSE baselines:
   - `manuscript/tse_flagship/tse_flagship_main.md`
   - `manuscript/tse_flagship/tse_flagship_appendix.md`
   - `submission/58_references_tse.bib`
2. Use the actual journal-facing rendering path or template that will be used
   for submission.
3. Verify abstract length in the rendered version.
   - Current manuscript-side count remains within target discipline.
4. Verify final references count in the rendered bibliography.
5. Verify that references are numbered in order of first appearance in the
   rendered manuscript.
6. Verify total page count after bibliography rendering.
7. Verify how the appendix is handled in the final package:
   - included in the main PDF
   - uploaded as supplement
   - or otherwise handled according to venue workflow
8. Recheck any page pressure created by:
   - `Related Work`
   - `Evaluation`
   - the rendered references section
9. Re-run the final inspection after any last cross-reference or numbering
   cleanup in the actual template.

## What Is Already Ready

- Real citations are already inserted in the canonical TSE manuscript.
- The dedicated bibliography file is already prepared.
- Citation/bibliography consistency is already checked in
  `submission/61_citation_bibliography_consistency_check.md`.

## What Must Still Be Confirmed By A Human

- final rendered bibliography appearance
- final citation numbering in venue format
- final total page count including abstract and references
- final appendix handling in the upload package
