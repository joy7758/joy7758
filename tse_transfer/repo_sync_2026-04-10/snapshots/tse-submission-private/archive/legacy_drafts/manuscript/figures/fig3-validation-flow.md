# Figure 3 Validation Flow

Purpose: Specify a figure that shows the documented validation stages and report outcomes.

## TODO

- [x] Record purpose, sources, caption, and citation target.
- [ ] Convert this spec into final artwork if the figure is kept.

## Purpose

Show how the repository presents the validator pathway from input file to
passing or failing `validation report`.

## Exact Source Files

- `spec/execution-evidence-operation-accountability-profile-v0.1.md`
- `demo/expected-output.md`
- `tests/test_operation_accountability_profile.py`
- `docs/STATUS.md`

## Proposed Figure Content

- Input profile file
- Schema check
- Reference closure check
- Linkage consistency check
- Integrity recomputation
- Output report with `ok`, issue count, error code, and summary

## Proposed Caption

`Documented validation flow for the current profile: the validator applies bounded checks and emits a machine-readable validation report with explicit success or failure outcomes.`

## Where It Should Be Cited

- `04-validator-and-demo.md`
- `05-evaluation.md`
