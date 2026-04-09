# Validator And Demo

Purpose: Explain the validator path and the single end-to-end demo supported by the artifact.

## TODO

- [x] Draft the validator and demo walkthrough.
- [ ] Add final figure references after figure selection.

## Draft

The repository exposes the verification path through the CLI entry
`agent-evidence validate-profile <file>`. The output is described throughout
the package as a `validation report`: machine-readable JSON with an `ok` flag,
issue counts, explicit error codes when validation fails, and a short summary
line. The repository documents four bounded categories of checking across the
specification, brief, abstract, expected output, and tests: schema conformance,
internal reference closure, consistency across policy/provenance/evidence
linkages, and integrity digest recomputation.

The example set makes that validator behavior inspectable. The valid example is
expected to return `ok: true` with zero issues. The three invalid examples each
target one primary failure surface already named by the repository: missing
required field, unresolved output reference, and broken evidence-to-policy
link. The regression tests check that the appropriate error codes appear in the
validator report for each invalid case.

The demo keeps the operational story equally bounded. According to the demo
documentation, it implements one policy-constrained metadata enrichment path:
load one source object, run a minimal profile precheck, apply one constrained
operation, generate one `operation accountability statement`, validate it, and
write artifacts under `demo/artifacts/`. The scenario constrains the operation
to adding approved metadata fields while keeping the note body unchanged. The
paper should describe this demo as a single illustrative walkthrough, not as a
benchmark or deployment study.
