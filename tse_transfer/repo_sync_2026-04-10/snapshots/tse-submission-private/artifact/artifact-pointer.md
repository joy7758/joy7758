# Artifact Pointer

Purpose: Point the manuscript package to the public artifact and the specific files that support paper claims.

## TODO

- [x] Record the public artifact location.
- [x] Map manuscript needs to artifact files.
- [ ] Add archival links beyond Zenodo if needed by the venue.

## Public Artifact

- Repository: `joy7758/agent-evidence`
- URL: `https://github.com/joy7758/agent-evidence`
- DOI: `10.5281/zenodo.19055948`
- Main line for this paper: `Execution Evidence and Operation Accountability Profile v0.1`

## Manuscript-Relevant Entry Points

- Overview and terminology: `README.md`
- Package inventory: `submission/package-manifest.md`
- Status and naming baseline: `docs/STATUS.md`
- Acceptance evidence: `docs/ACCEPTANCE-CHECKLIST.md`
- Handoff summary: `submission/final-handoff.md`
- Profile spec: `spec/execution-evidence-operation-accountability-profile-v0.1.md`
- Profile schema: `schema/execution-evidence-operation-accountability-profile-v0.1.schema.json`
- Example set: `examples/README.md`
- Demo guide: `demo/README.md`
- Demo scenario: `demo/scenario.md`
- Demo expected behavior: `demo/expected-output.md`
- Regression tests: `tests/test_operation_accountability_profile.py`

## Usage In The Manuscript

- Use the spec and schema to describe the object model and compliance boundary.
- Use the examples, expected output, and tests to support claims about validator behavior.
- Use the demo files to support the single-path end-to-end walkthrough.
- Use the status, acceptance checklist, and final handoff to support bounded delivery claims.
