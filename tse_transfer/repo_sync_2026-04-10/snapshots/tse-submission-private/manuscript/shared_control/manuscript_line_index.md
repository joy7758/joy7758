# Manuscript Line Index

This file records the canonical manuscript lines after the line-separation and
canonical-path normalization rounds completed on `2026-04-08`.

## Canonical Lines

| Line name | Current role | Canonical title | Canonical main file | Canonical appendix file | Current TSE upload baseline |
| --- | --- | --- | --- | --- | --- |
| TSE flagship | Active manuscript line for final submission preparation | `Operation Accountability as a First-Class Verification Boundary for Machine-Actionable Object Systems` | `manuscript/tse_flagship/tse_flagship_main.md` | `manuscript/tse_flagship/tse_flagship_appendix.md` | `yes` |
| Frozen witness archive | Frozen JSS-aligned witness archive | `Execution Evidence as a Verifiable Workflow Object: A Minimal Profile and Validator for Operation Accountability` | `manuscript/jss_witness_archive/jss_witness_main.md` | `none` | `no` |

## Canonical Path Status

- Active canonical manuscript directory: `manuscript/tse_flagship/`
- Frozen archive directory: `manuscript/jss_witness_archive/`
- Dated snapshot directories detected under `manuscript/`: none
- Snapshot rule: any future dated directory under `manuscript/` is
  `snapshot_only` and must not participate in build, submission, line index,
  page-truth, or citation handoff
- Unrelated line exclusion: the `Sovereign-pFDO` line has no canonical
  manuscript path under `manuscript/` in this repository and is excluded from
  the current TSE submission workflow

## Source Classification

### Frozen witness archive

- Canonical frozen copy: `manuscript/jss_witness_archive/jss_witness_main.md`
- Archived legacy source: `archive/legacy_drafts/manuscript/full-draft.md`
- Editing status: frozen archival line; do not revise manuscript content in
  this line
- Related-manuscript status: the active related submission disclosure now
  points to the separate JSS manuscript, while this historical path remains a
  frozen archive only

### TSE flagship line

- Canonical main manuscript: `manuscript/tse_flagship/tse_flagship_main.md`
- Canonical appendix: `manuscript/tse_flagship/tse_flagship_appendix.md`
- Archived assembly sources:
  - `archive/legacy_drafts/manuscript/abstract.md`
  - `archive/legacy_drafts/manuscript/sections/01-introduction.md`
  - `archive/legacy_drafts/manuscript/sections/02-problem-and-scope.md`
  - `archive/legacy_drafts/manuscript/sections/03-profile-design.md`
  - `archive/legacy_drafts/manuscript/sections/04-validator-and-demo.md`
  - `archive/legacy_drafts/manuscript/sections/05-evaluation.md`
  - `archive/legacy_drafts/manuscript/sections/06-related-work.md`
  - `archive/legacy_drafts/manuscript/sections/07-threats-to-validity.md`
  - `archive/legacy_drafts/manuscript/sections/08-conclusion.md`
  - `archive/legacy_drafts/manuscript/refs/references.bib`

### Shared submission-control files

- `manuscript/shared_control/manuscript_line_index.md`
- `manuscript/shared_control/upload_baseline_decision.md`
- `manuscript/shared_control/name_collision_audit.md`
- `manuscript/shared_control/paper_category_matrix.md`
- `manuscript/shared_control/canonical_path_map.md`
- `submission/55_citation_insertion_targets.md`
- `submission/56_pre_submission_readiness_note.md`
- `README_submission_repo.md`

### Stale or ambiguous filenames

- `archive/legacy_drafts/manuscript/full-draft.md`
- `archive/legacy_drafts/manuscript/abstract.md`
- `archive/legacy_drafts/manuscript/sections/`

These surfaces remain available as archived legacy material, but they are not
the canonical TSE upload baseline.

## Explicit Warning

`archive/legacy_drafts/manuscript/full-draft.md` is not the TSE flagship
manuscript.

The expected legacy TSE filenames `manuscript/41_full_draft_tse_en.md` and
`manuscript/42_appendix_validation_tse_en.md` were not present in the current
repository state. This round therefore established the TSE canonical baseline
from the available sectioned manuscript sources and left the frozen witness
archive separate.

Any dated folders created later under `manuscript/` are archival snapshots
only and must not become active manuscript lines.
