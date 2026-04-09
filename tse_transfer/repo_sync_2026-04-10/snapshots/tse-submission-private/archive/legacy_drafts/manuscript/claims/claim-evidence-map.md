# Claim-Evidence Map

Purpose: Tie each manuscript claim to specific public artifact files and pre-approved wording.

## TODO

- [x] Map core claims to supporting files.
- [x] Separate shipped artifact claims from non-goals.
- [ ] Re-check wording before external submission.

## Claim Map

| claim | evidence file(s) | allowed wording |
| --- | --- | --- |
| The repository ships a minimal v0.1 package centered on `Execution Evidence and Operation Accountability Profile v0.1`. | `README.md`; `docs/STATUS.md`; `submission/package-manifest.md`; `submission/final-handoff.md` | "The current package is a minimal v0.1 handoff centered on Execution Evidence and Operation Accountability Profile v0.1." |
| The shipped package includes a profile spec, schema, example set, validator entry point, demo, and handoff documents. | `submission/package-manifest.md`; `docs/STATUS.md`; `README.md` | "The artifact package includes the profile specification, JSON Schema, example set, validator CLI path, demo materials, and handoff documents." |
| The validator path is exposed as `agent-evidence validate-profile <file>`, and its output is treated as a `validation report`. | `docs/STATUS.md`; `README.md`; `spec/execution-evidence-operation-accountability-profile-v0.1.md` | "The repository exposes a profile-aware validator at agent-evidence validate-profile <file>, which produces a validation report." |
| The validated behavior currently covers one valid example and three invalid examples, each with one primary failure class. | `examples/README.md`; `demo/expected-output.md`; `tests/test_operation_accountability_profile.py`; `docs/ACCEPTANCE-CHECKLIST.md`; `docs/STATUS.md` | "The current package documents one passing example and three controlled failing examples that each target one main rule class." |
| The runnable demo is a single metadata-enrichment path that emits artifacts and ends with a PASS summary line when the documented path succeeds. | `demo/README.md`; `demo/scenario.md`; `demo/expected-output.md`; `submission/final-handoff.md`; `docs/STATUS.md` | "The demo implements one policy-constrained metadata enrichment path and produces artifacts plus a PASS validation summary on the documented success path." |
| The artifact supports bounded independent verification of one operation accountability statement. | `spec/execution-evidence-operation-accountability-profile-v0.1.md`; `submission/final-handoff.md`; `docs/STATUS.md`; `README.md` | "The artifact supports a bounded independent verification path for one operation accountability statement." |
| The validator checks schema conformance, internal reference closure, cross-section linkage consistency, and integrity digest recomputation. | `spec/execution-evidence-operation-accountability-profile-v0.1.md`; `demo/expected-output.md`; `tests/test_operation_accountability_profile.py`; `docs/STATUS.md` | "The validator checks the bounded conditions defined by the profile, including schema conformance, reference closure, linkage consistency, and integrity digest recomputation." |
| The current work does not claim registry design, multi-agent orchestration coverage, full FDO mapping, or a full cryptographic trust fabric. | `spec/execution-evidence-operation-accountability-profile-v0.1.md`; `submission/final-handoff.md`; `docs/STATUS.md` | "The current contribution is intentionally narrow and does not cover registry design, multi-agent orchestration, full FDO mapping, or full cryptographic infrastructure." |

## Unsupported Claim Patterns

- Do not claim external deployment evidence.
- Do not claim broad AI governance effectiveness.
- Do not claim sovereignty guarantees.
- Do not claim large-scale performance or security properties not present in the repository.
