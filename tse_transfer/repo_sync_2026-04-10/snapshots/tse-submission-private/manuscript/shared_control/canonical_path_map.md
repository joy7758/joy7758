# Canonical Path Map

This file records the only active manuscript paths that may participate in the
current TSE submission workflow.

## Active Canonical Path

- TSE flagship line
  - active canonical directory: `manuscript/tse_flagship/`
  - active canonical files:
    - `manuscript/tse_flagship/tse_flagship_main.md`
    - `manuscript/tse_flagship/tse_flagship_appendix.md`
  - build and submission eligibility: yes
  - status: active

## Frozen Archive Path

- JSS-aligned witness archive
  - canonical archive directory: `manuscript/jss_witness_archive/`
  - canonical archive file:
    - `manuscript/jss_witness_archive/jss_witness_main.md`
  - build and submission eligibility for the TSE package: no
  - status: frozen

## Excluded Line

- Sovereign-pFDO
  - canonical directory in this repository: none
  - build and submission eligibility for the TSE package: no
  - status: unrelated

## Detected Snapshot Paths

No dated snapshot directories were detected under `manuscript/` for the
checked patterns:

- `*2026-04-07*`
- `*20260407*`
- `*0407*`
- `*2026_04_07*`

## Snapshot-Only Rule

- Any dated directory created later under `manuscript/` must be marked
  `snapshot_only` and `do_not_edit`.
- Snapshot-only directories must not be used in:
  - build
  - submission
  - manuscript line index
  - page-truth
  - citation handoff

## Non-Canonical Retained Surfaces

- `archive/legacy_drafts/manuscript/full-draft.md`
- `archive/legacy_drafts/manuscript/abstract.md`
- `archive/legacy_drafts/manuscript/sections/`
- `archive/legacy_drafts/manuscript/claims/`
- `archive/legacy_drafts/manuscript/figures/`
- `archive/legacy_drafts/manuscript/tables/`
- `archive/legacy_drafts/manuscript/refs/`

These surfaces may remain in the repository for history, assembly, or support,
but they are not active canonical submission sources.
