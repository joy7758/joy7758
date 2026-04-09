# Cross-Line Contamination Audit

## Audit Scope

This audit checks the active TSE flagship manuscript, the rebuilt TSE
submission package, and nearby repo surfaces for cross-line contamination risk.
The frozen witness archive stored under the current `jss_witness_archive` path
was inspected only for existence and immutability, not for content editing.

Files checked directly as the current TSE submission package:

- `manuscript/tse_flagship/tse_flagship_main.md`
- `manuscript/tse_flagship/tse_flagship_appendix.md`
- `submission/tse_cover_letter_current.md`
- `submission/tse_difference_note_current.md`
- `submission/tse_submission_metadata_current.txt`
- `submission/tse_comments_to_editor_current.txt`
- `submission/tse_upload_manifest_current.md`
- `submission/tse_submission_package_readme_current.md`

## Canonical-Path Normalization Result

- Active canonical manuscript directory:
  `manuscript/tse_flagship/`
- Frozen archive directory:
  `manuscript/jss_witness_archive/`
- Dated snapshot directories detected under `manuscript/`:
  none in the checked formats `2026-04-07`, `20260407`, `0407`, and
  `2026_04_07`
- Snapshot-only rule:
  any future dated directory under `manuscript/` is `snapshot_only` and must
  not participate in build, submission, line index, page-truth, or citation
  handoff
- Excluded unrelated line:
  `Sovereign-pFDO` has no canonical manuscript path under `manuscript/` in
  this repository and remains outside the current TSE submission line

## Line-Separation Status

- TSE flagship files exist in their canonical paths.
- The frozen witness-archive file exists at
  `manuscript/jss_witness_archive/jss_witness_main.md`.
- The frozen witness-archive copy still matches
  `archive/legacy_drafts/manuscript/full-draft.md`.
- The frozen witness archive was not edited in this round.

## Direct Checks On The Current TSE Files And Rebuilt Submission Package

- References to `full-draft.md` inside the current TSE flagship files:
  not found.
- References to `full-draft.md` inside the rebuilt TSE submission package:
  found only in `submission/tse_upload_manifest_current.md` and
  `submission/tse_submission_package_readme_current.md` as explicit
  do-not-use / do-not-upload warnings.
- Lingering references to the missing legacy `41/42/43/44` path assumptions
  inside the current TSE flagship files:
  not found.
- Lingering references to the missing legacy `41/42/43/44` path assumptions
  inside the rebuilt TSE submission package:
  found only in `submission/tse_submission_package_readme_current.md` as a
  warning not to use that older naming pattern.
- Stale editor-facing wording that described a current TOSEM submission:
  removed from the active TSE submission disclosure files.
- Current editor-facing disclosure status:
  the active TSE submission package now discloses a related manuscript under
  review at JSS, while the `manuscript/jss_witness_archive/` path remains only
  a
  frozen historical archive path.

## Unrelated-Paper Marker Check

The following markers were checked against the current TSE flagship files and
the rebuilt TSE submission package:

- `Sovereign-pFDO`
- `Digital Territory`
- `Snapp System`
- `BLAKE3`
- `1.6T`
- `MCP gateway`
- `KL Divergence`

Result:

- No unrelated-paper contamination markers were found inside the current TSE
  flagship manuscript files.
- No unrelated-paper contamination markers were found inside the rebuilt TSE
  submission package files.

Repo-wide contextual note:

- `Sovereign-pFDO` appears in `notes/internal/review/internal-redline.md` as a historical
  review note, not as part of the current TSE flagship manuscript or rebuilt
  submission package.
- No repo-wide hits were found for `Digital Territory`, `Snapp System`,
  `BLAKE3`, `1.6T`, `MCP gateway`, or `KL Divergence` during this audit.

## Remaining Ambiguous Filename Risk

The repo still contains ambiguous or assembly-oriented manuscript filenames
outside the canonical TSE submission package:

- `archive/legacy_drafts/manuscript/full-draft.md`
- `archive/legacy_drafts/manuscript/abstract.md`
- `archive/legacy_drafts/manuscript/sections/`
- `archive/legacy_drafts/manuscript/venue/cover-letter.md`

These files should not be used as the live TSE upload baseline.

## Audit Conclusion

The current TSE flagship manuscript and rebuilt TSE submission package are
clean with respect to unrelated-paper markers and old upload-baseline path
assumptions, except for explicit warning text that names old or ambiguous files
in order to prevent accidental use. The frozen witness archive remains
separate and untouched. The new category/path control files
`paper_category_matrix.md` and `canonical_path_map.md` now harden the rule
that only `manuscript/tse_flagship/` is active, the historical witness path is
frozen, and any future dated folders are snapshot-only.
