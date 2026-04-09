# Submission Repo Guide

This repository now distinguishes the active TSE flagship manuscript from the
frozen JSS witness archive and keeps unrelated paper lines out of the active
submission path. The current TSE package is mechanically sealed at the source
level and now waits only on final build-dependent submission checks.

## Directory Layout

- `manuscript/tse_flagship/`
  active TSE manuscript line
- `manuscript/jss_witness_archive/`
  frozen JSS witness archive
- `manuscript/shared_control/`
  upload-baseline, line-index, and naming-risk notes
- `submission/`
  current TSE submission package plus pre-submission control notes
- `archive/legacy_drafts/`
  archived legacy manuscript surfaces that are no longer canonical
- `archive/dated_snapshots/`
  archival location for any future dated snapshot directories
- `notes/internal/`
  internal review and scratch notes

## Current Canonical Paths

- TSE flagship main manuscript:
  `manuscript/tse_flagship/tse_flagship_main.md`
- TSE flagship appendix:
  `manuscript/tse_flagship/tse_flagship_appendix.md`
- Frozen JSS witness manuscript archive:
  `manuscript/jss_witness_archive/jss_witness_main.md`

## Current Submission Package

- Cover letter:
  `submission/tse_cover_letter_current.md`
- Related-submission note:
  `submission/tse_difference_note_current.md`
- Submission metadata sheet:
  `submission/tse_submission_metadata_current.txt`
- Comments to editor:
  `submission/tse_comments_to_editor_current.txt`
- Upload manifest:
  `submission/tse_upload_manifest_current.md`
- Package readme:
  `submission/tse_submission_package_readme_current.md`
- TSE bibliography source:
  `submission/58_references_tse.bib`
- Citation source audit:
  `submission/57_reference_source_audit.md`
- Citation insertion log:
  `submission/59_citation_insertion_log.md`
- Page-truth note:
  `submission/60_page_truth_after_citations.md`
- Citation/bibliography consistency check:
  `submission/61_citation_bibliography_consistency_check.md`
- Cross-reference and numbering cleanup note:
  `submission/62_crossref_numbering_cleanup.md`
- Reviewer selection worksheet:
  `submission/63_reviewer_selection_worksheet.md`
- Final page-truth handoff:
  `submission/64_final_page_truth_handoff.md`
- Final submission baseline freeze:
  `submission/65_final_submission_baseline_freeze.md`

## Working Rule

Do not continue editing archived legacy files such as
`archive/legacy_drafts/manuscript/full-draft.md` when preparing the TSE
submission. Keep edits on the TSE side inside `manuscript/tse_flagship/` only,
leave the frozen JSS witness archive untouched, and treat any future dated
folders as snapshot-only. Build the current TSE submission package only from
the canonical TSE files and the `submission/tse_*_current.*` package files.
Citation maintenance for the TSE line should use the dedicated bibliography file
`submission/58_references_tse.bib` and the audit/log files created for the TSE
flagship line. Final manual submission work should follow the frozen baseline
declared in `submission/65_final_submission_baseline_freeze.md`.
