# Pre-Submission Readiness Note

## Current Status

The manuscript repository now has an explicit line split. The active TSE
flagship baseline is `manuscript/tse_flagship/tse_flagship_main.md` together
with `manuscript/tse_flagship/tse_flagship_appendix.md`. The TSE side was
cleaned to reduce repository-management language in the paper body, preserve
the bounded verification argument, present a reviewer-facing appendix with
relative-path guidance, and now includes real citations plus a dedicated TSE
bibliography file at `submission/58_references_tse.bib`. Citation/bibliography
consistency has been checked, final cross-reference language has been cleaned
lightly, and final handoff control files have been prepared for reviewer
selection and page-truth completion.

The JSS witness line was frozen in
`manuscript/jss_witness_archive/jss_witness_main.md` and was not edited after
the copy into its canonical frozen location.

Citation-complete local compilation and final page-truth were not achieved in
this round because no local `pandoc`, `pdflatex`, `xelatex`, or `tectonic`
toolchain was available in the current environment.

The current TSE package should therefore be treated as mechanically sealed,
with only final build-dependent checks still pending before human submission.

## Remaining True Blockers Before Submission

- final rendered bibliography check in the actual journal-facing output path
- final numbering check in the actual journal-facing output path
- reviewer suggestions and exclusions finalized for the submission system
- citation-complete final page-truth check before upload

The current manual next-step page-truth checklist is recorded in
`submission/64_final_page_truth_handoff.md`.
