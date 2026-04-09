# Figure 4 Demo And Failure Cases

Purpose: Specify a figure that contrasts the single successful demo path with the controlled invalid examples.

## TODO

- [x] Record purpose, sources, caption, and citation target.
- [ ] Convert this spec into final artwork if the figure is kept.

## Purpose

Connect the documented demo success path with the three controlled failure
cases used in evaluation.

## Exact Source Files

- `demo/scenario.md`
- `demo/expected-output.md`
- `examples/README.md`
- `tests/test_operation_accountability_profile.py`

## Proposed Figure Content

- One success lane for the metadata enrichment demo
- Three failure callouts:
  - missing required field
  - unresolved output reference
  - broken evidence-policy link
- Reported primary error code beside each invalid case

## Proposed Caption

`Bounded evaluation materials in the current repository: one successful demo path and three controlled invalid examples that each break one main rule class.`

## Where It Should Be Cited

- `04-validator-and-demo.md`
- `05-evaluation.md`
