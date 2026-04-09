# Appendix: Bounded Artifact Review Notes

All file paths in this appendix are relative to the root of the public artifact
repository.

This appendix summarizes the concrete artifact surfaces that bound the paper's
claims. It is reviewer-facing and intentionally limited to the bounded artifact
surface used to support the TSE verification-boundary argument. The appendix
does not add new evidence, new experiments, or new scenarios beyond the
material already described in the main paper and the public artifact.

## A. Public Artifact Baseline

The public artifact baseline for the present paper is the repository
`joy7758/agent-evidence` at commit
`80e7e78ab6cbd9befc24b56fbf9cdffabd99b5de`. The currently recorded artifact DOI
is `10.5281/zenodo.19055948`. The paper's bounded claims are tied to
`Execution Evidence and Operation Accountability Profile v0.1` and its
documented validator/demo path.

## B. Artifact Entry Points Used By The Paper

The main manuscript relies on a small set of artifact entry points:

| Purpose | Artifact file(s) |
| --- | --- |
| Profile definition | `spec/execution-evidence-operation-accountability-profile-v0.1.md` |
| Schema boundary | `schema/execution-evidence-operation-accountability-profile-v0.1.schema.json` |
| Example set overview | `examples/README.md` |
| Runnable demo overview | `demo/README.md` |
| Demo scenario | `demo/scenario.md` |
| Demo expected behavior | `demo/expected-output.md` |
| Validator regression coverage | `tests/test_operation_accountability_profile.py` |

These files define the bounded evidence surface for the paper's factual claims
about object shape, validator behavior, controlled failure cases, and the
single demo walkthrough.

## C. Fresh Clean Rerun

A fresh local rerun was recorded on `2026-04-07` using Python `3.14.3` on
macOS arm64. The minimal tested install path was the base editable install from
the artifact repository root:

```bash
python3 -m venv .repro-v0_1-20260407-full
.repro-v0_1-20260407-full/bin/python -m pip install --upgrade pip
.repro-v0_1-20260407-full/bin/python -m pip install -e .
```

The rerun command list was:

```bash
.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/minimal-valid-evidence.json
.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-missing-required.json
.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-unclosed-reference.json
.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-policy-link-broken.json
.repro-v0_1-20260407-full/bin/python demo/run_operation_accountability_demo.py
```

The observed outcomes matched the bounded expectations already described by the
artifact:

| Command target | Observed exit | Bounded outcome |
| --- | --- | --- |
| `examples/minimal-valid-evidence.json` | `0` | passing validation report with `ok: true` and `issue_count: 0` |
| `examples/invalid-missing-required.json` | `1` | primary error code `schema_violation` |
| `examples/invalid-unclosed-reference.json` | `1` | primary error code `unresolved_output_ref` |
| `examples/invalid-policy-link-broken.json` | `1` | primary error code `unresolved_evidence_policy_ref` |
| `demo/run_operation_accountability_demo.py` | `0` | final PASS summary line and emitted demo artifacts |

This rerun supports a narrow claim only: the current minimal path can be
re-executed cleanly and reproduces the documented pass/fail behavior for the
controlled examples and the single demo walkthrough.

## D. Controlled Example Set

The example set is intentionally small and role-specific:

| Example file | Intended role | Main failure or success surface |
| --- | --- | --- |
| `examples/minimal-valid-evidence.json` | valid profile specimen | full bounded pass |
| `examples/invalid-missing-required.json` | invalid specimen | schema failure |
| `examples/invalid-unclosed-reference.json` | invalid specimen | reference-closure failure |
| `examples/invalid-policy-link-broken.json` | invalid specimen | evidence-to-policy linkage failure |

The purpose of this structure is not exhaustive rule coverage. It is to give a
reviewer one passing specimen, three single-failure specimens, and one compact
view of the current validator boundary.

## E. Demo Boundary And Non-Goals

The demo is a single metadata-enrichment walkthrough over one source object
under an explicit policy boundary. It is included to show that the current
profile and validator path can close an end-to-end loop and emit reviewable
artifacts. It is not presented as a benchmark, deployment study, or large-scale
evaluation.

The same boundary applies to the paper as a whole. The contribution does not
extend to registry design, multi-agent accountability composition, full FDO
mapping, formal deployment assurance, or a complete cryptographic trust fabric.
