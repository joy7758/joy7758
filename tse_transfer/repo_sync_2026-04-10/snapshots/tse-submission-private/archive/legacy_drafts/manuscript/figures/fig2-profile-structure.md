# Figure 2 Profile Structure

Purpose: Specify a figure that visualizes the top-level profile sections and their key link relationships.

## TODO

- [x] Record purpose, sources, caption, and citation target.
- [ ] Convert this spec into final artwork if the figure is kept.

## Purpose

Show the eleven top-level sections of the profile and the core reference links
between operation, policy, provenance, evidence, and validation.

## Exact Source Files

- `spec/execution-evidence-operation-accountability-profile-v0.1.md`
- `schema/execution-evidence-operation-accountability-profile-v0.1.schema.json`

## Proposed Figure Content

- Box for each top-level section
- Arrows from `operation.subject_ref` to `subject.id`
- Arrows from `operation.policy_ref` and `validation.policy_ref` to `policy.id`
- Arrows linking `operation`/`provenance`/`evidence`/`validation`
- Callout for `evidence.integrity` digests

## Proposed Caption

`Top-level structure of Execution Evidence and Operation Accountability Profile v0.1, showing the minimal section set and the internal links required for conformance.`

## Where It Should Be Cited

- `03-profile-design.md`
- `05-evaluation.md`
