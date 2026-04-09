# Paper Category Matrix

This control file fixes one rule for the current repository state:

`one paper line = one contribution category = one canonical path = one evaluation logic`

The matrix below is the canonical category boundary for work in and around this
repository after canonical-path normalization on `2026-04-08`.

## TSE Flagship

- Paper line: TSE flagship
- Canonical path: `manuscript/tse_flagship/`
- Snapshot paths: none detected under `manuscript/` in the checked dated-folder
  patterns
- Category: problem-defining / verification-boundary flagship paper
- Core question: why operation accountability should be treated as a
  first-class verification boundary
- Contribution center:
  - operation accountability problem definition
  - minimal verification boundary
  - failure taxonomy
  - same-case comparison
  - evidence-bounded validation framing
- Forbidden borrowed terms as contribution center:
  - minimal profile
  - validator CLI
  - runnable demo
  - controlled invalid examples
- Status: active

## JSS Witness Line

- Paper line: JSS witness line
- Canonical path: `manuscript/jss_witness_archive/`
- Snapshot paths: none detected under `manuscript/` in the checked dated-folder
  patterns
- Category: witness / artifact / minimal implementation paper
- Core question: whether a minimal profile + validator + controlled examples
  form a reproducible witness path
- Contribution center:
  - minimal profile
  - JSON Schema
  - validator
  - controlled examples
  - runnable demo
- Forbidden borrowed terms as contribution center:
  - first-class verification boundary
  - failure taxonomy
  - same-case comparison
  - flagship framing
- Status: frozen

## Sovereign-pFDO

- Paper line: Sovereign-pFDO
- Canonical path: none in this repository's `manuscript/` tree
- Snapshot paths: none detected under `manuscript/` in the checked dated-folder
  patterns
- Category: protocol / distributed governance architecture paper
- Core question: how protocol-layer mechanisms support distributed governance
  and sovereignty
- Contribution center:
  - protocol-driven framework
  - distributed governance architecture
  - PID construction
  - governance gateway
  - scalability / hardware-offload logic
- Forbidden borrowed terms as contribution center:
  - operation accountability
  - witness line
  - validator-centered minimal artifact
  - execution evidence profile framing
- Status: unrelated

## Additional Control Notes

- `archive/legacy_drafts/manuscript/full-draft.md` is a retained legacy source,
  not a canonical paper path.
- Dated folders, if created later under `manuscript/`, are `snapshot_only` and
  `do_not_edit`.
- Snapshot-only paths must not participate in build, submission, line index,
  page-truth, or citation handoff.
