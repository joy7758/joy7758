# Name Collision Audit

## Ambiguous Or Stale Filenames Found

The current repository state contained several naming surfaces that could cause
line confusion:

- `manuscript/full-draft.md`
- `manuscript/abstract.md`
- `manuscript/sections/`
- missing but expected legacy TSE names:
  - `manuscript/41_full_draft_tse_en.md`
  - `manuscript/42_appendix_validation_tse_en.md`

The most dangerous collision was `manuscript/full-draft.md`. It was a generic
single-file manuscript name with no line label, no venue label, and no warning
that it belongs to the witness line rather than the active TSE flagship line.

## Concrete Submission Risks

- Wrong manuscript uploaded:
  a generic `full-draft.md` could be mistaken for the current TSE submission
  file.
- Wrong line edited:
  a contributor could continue polishing the frozen witness manuscript instead
  of the active TSE flagship manuscript.
- Stale file mistaken as baseline:
  the absence of explicit canonical TSE filenames made it easy to treat
  section-source files or the witness draft as the latest upload baseline.
- Witness paper confused with flagship paper:
  the repository did not previously enforce a directory-level separation
  between the minimal implementation witness line and the TSE flagship line.

## Canonical Names Now Enforced

- TSE main manuscript:
  `manuscript/tse_flagship/tse_flagship_main.md`
- TSE appendix:
  `manuscript/tse_flagship/tse_flagship_appendix.md`
- Frozen JSS witness archive manuscript:
  `manuscript/jss_witness_archive/jss_witness_main.md`

The old ambiguous manuscript surfaces have now been moved into
`archive/legacy_drafts/manuscript/`, including:

- `archive/legacy_drafts/manuscript/full-draft.md`
- `archive/legacy_drafts/manuscript/abstract.md`
- `archive/legacy_drafts/manuscript/sections/`

Those archived surfaces are retained for history only and are not current
upload baselines.
