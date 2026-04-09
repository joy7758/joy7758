# Revision Log

Purpose: Record manuscript-side changes and rationale over time.

## TODO

- [x] Create the initial log.
- [ ] Add an entry for each substantive manuscript revision.

## Entries

- `2026-04-06`: Created the initial manuscript scaffold and first-draft package from the public `agent-evidence` v0.1 materials.
- `2026-04-07`: Ran a fresh reproducibility check against `agent-evidence` commit `80e7e78ab6cbd9befc24b56fbf9cdffabd99b5de` in a new virtual environment at `/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full`. The minimal tested install path was the base editable install `pip install -e /Users/zhangbin/GitHub/agent-evidence`, which corresponds to `pip install -e .` when run from the repository root. `validate-profile` returned exit `0` for the valid example, exit `1` for each of the three controlled invalid examples with the expected primary error codes, and the demo returned exit `0` with a final `PASS execution-evidence-operation-accountability-profile@0.1 ...` line. Updated `artifact/reproducibility.md` and `archive/legacy_drafts/manuscript/sections/05-evaluation.md` to reflect the clean rerun.
