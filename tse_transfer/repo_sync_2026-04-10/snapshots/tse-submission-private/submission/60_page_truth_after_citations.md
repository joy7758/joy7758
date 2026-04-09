# Page-Truth After Citations

## Summary

Citation-complete page-truth has not yet been fully verified because no
suitable local assembly toolchain is available in the current repository
environment. This file therefore records what has been verified already and
what still requires a final build. It now functions as a sealed status note
for the current TSE package, while the step-by-step human handoff remains in
`submission/64_final_page_truth_handoff.md`.

## Already Verified

- The canonical TSE manuscript contains real citations in the body.
- A dedicated bibliography file exists at `submission/58_references_tse.bib`.
- The citation keys used in the manuscript match the entries in the dedicated
  TSE bibliography file.
- The current abstract remains within the target abstract-length discipline at
  `200` words.
- The sections most likely to create page pressure after bibliography
  rendering remain:
  1. `6. Related Work` at about `615` words
  2. `5. Evaluation` at about `361` words
  3. `4. Validator and Demo Path` at about `319` words
  4. `3. Profile Design` at about `300` words
  5. `2. Problem and Scope` at about `295` words

## Pending Final Build Verification

- actual compiled page count after bibliography rendering
- final numbering order of references in the journal-facing output
- final appearance and count of rendered bibliography entries
- final appendix handling in the upload package
- any page pressure introduced by the rendered references section

## Current Tooling Limitation

The following commands were checked in the current repo environment and were
not found in `PATH`:

- `pandoc`
- `pdflatex`
- `xelatex`
- `tectonic`

Because of that, no reliable final compiled page count can be reported yet.

## Final Build Handoff Checklist

1. Compile `manuscript/tse_flagship/tse_flagship_main.md` together with
   `submission/58_references_tse.bib` using the actual journal-facing
   rendering path or template.
2. Verify the final rendered reference order against first appearance in the
   manuscript.
3. Verify the total page count including abstract and references.
4. Verify how the appendix is handled in the final package.
5. Confirm that no archived source under `archive/legacy_drafts/` or frozen
   witness file under `manuscript/jss_witness_archive/` was pulled into the
   final build.
6. Run one final inspection after any last numbering or cross-reference cleanup.
