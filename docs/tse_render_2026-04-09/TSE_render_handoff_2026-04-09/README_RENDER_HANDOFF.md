# TSE Render Handoff

This bundle is an external journal-facing render handoff for the current TSE
canonical line.

## Canonical Manuscript Files

- `manuscript/tse_flagship/tse_flagship_main.md`
- `manuscript/tse_flagship/tse_flagship_appendix.md`

## Canonical Bibliography

- `submission/58_references_tse.bib`

## Current Editor-Facing Submission Files

- `submission/tse_cover_letter_current.md`
- `submission/tse_difference_note_current.md`
- `submission/tse_submission_metadata_current.txt`
- `submission/tse_comments_to_editor_current.txt`
- `submission/tse_upload_manifest_current.md`

## Render Constraints

- The source repo does not define a canonical executable build path.
- The current machine does not have a local document toolchain.
- This bundle must therefore be rendered only in a real journal-facing
  TSE/IEEE template environment.

## Do Not Do

- Do not use old `SIDS2026` or other `conference` bundles as render truth for
  this handoff.
- Do not place the appendix into the main PDF.

## Render-Dependent Mechanical Checks

- main PDF render success
- supplement PDF render success
- main page count
- supplement page count
- bibliography appearance
- reference numbering
- missing citation
- broken cross-reference
- template/build warnings
- separated upload shape

This handoff bundle preserves source truth only. Portal upload should occur
only after render-dependent checks are completed in a real journal-facing
environment.
