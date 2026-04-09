# Table 2 Valid Invalid Cases

Purpose: Specify the table that summarizes the documented validator outcomes for the example set.

## TODO

- [x] Record columns, rows, sources, and rationale.
- [ ] Convert into final manuscript table format later.

## Table Columns

- input file
- intended condition
- expected outcome
- primary code or summary

## Rows To Populate

- `examples/minimal-valid-evidence.json` | valid profile instance | `ok: true` | `issue_count: 0`
- `examples/invalid-missing-required.json` | missing required field | `ok: false` | `schema_violation`
- `examples/invalid-unclosed-reference.json` | unresolved output reference | `ok: false` | `unresolved_output_ref`
- `examples/invalid-policy-link-broken.json` | broken evidence-policy link | `ok: false` | `unresolved_evidence_policy_ref`

## Source Files

- `examples/README.md`
- `demo/expected-output.md`
- `tests/test_operation_accountability_profile.py`
- `docs/STATUS.md`

## Why This Table Matters

It gives a compact view of the controlled validation surface and supports the
paper's bounded evaluation story.
