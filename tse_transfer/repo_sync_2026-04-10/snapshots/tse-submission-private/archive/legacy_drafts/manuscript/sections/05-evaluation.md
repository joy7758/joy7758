# Evaluation

Purpose: Record the bounded evaluation story that is already supported by the repository.

## TODO

- [x] Keep evaluation limited to documented validator and demo behavior.
- [x] Record the fresh clean rerun explicitly.
- [ ] Add exact table references once the manuscript layout stabilizes.

## Draft

The current evaluation is intentionally artifact-bounded. It does not introduce
new datasets, external deployments, or broad comparative experiments. It is
limited to one valid example, three single-failure invalid examples, and one
single-path demo for `Execution Evidence and Operation Accountability Profile
v0.1`.

### Fresh Clean Rerun

A fresh local rerun was performed on `2026-04-07` against public repository
commit `80e7e78ab6cbd9befc24b56fbf9cdffabd99b5de` in a new virtual environment
at `/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full`. The
environment used Python `3.14.3` on macOS arm64. The minimal tested install
path was the base editable install; no extra dependencies beyond that base
install were required for the current minimal profile/validator/demo path.

Install command:

```bash
python3 -m venv /Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python -m pip install --upgrade pip
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python -m pip install -e /Users/zhangbin/GitHub/agent-evidence
```

Exact command list:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/minimal-valid-evidence.json
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-missing-required.json
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-unclosed-reference.json
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-policy-link-broken.json
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python demo/run_operation_accountability_demo.py
```

Observed command outcomes:

| command target | expected exit | observed exit | observed result |
| --- | --- | --- | --- |
| `examples/minimal-valid-evidence.json` | `0` | `0` | `ok: true`, `issue_count: 0` |
| `examples/invalid-missing-required.json` | `1` | `1` | primary error code `schema_violation` |
| `examples/invalid-unclosed-reference.json` | `1` | `1` | primary error code `unresolved_output_ref` |
| `examples/invalid-policy-link-broken.json` | `1` | `1` | primary error code `unresolved_evidence_policy_ref` |
| `demo/run_operation_accountability_demo.py` | `0` | `0` | final `PASS execution-evidence-operation-accountability-profile@0.1 ...` summary line |

The clean rerun therefore matched the current claimed behavior: one passing
example, three controlled failing examples with one main error code each, and
one passing demo path that writes `minimal-profile-evidence.json` and
`validation-report.json` under `demo/artifacts/`.

### Evaluation Boundary

This rerun strengthens the paper's evaluation narrative, but it does not widen
the evaluation scope. The paper still evaluates only the current minimal path:
schema conformance, internal reference closure, linkage consistency across
policy/provenance/evidence, integrity digest recomputation, and one runnable
demo scenario. The raw local logs for the fresh rerun were recorded under
`/tmp/agent-evidence-repro-20260407-full`, and the manuscript-side summary is
captured in `artifact/reproducibility.md`.

### Relationship To Repository Acceptance

The repository's existing `docs/STATUS.md` and `docs/ACCEPTANCE-CHECKLIST.md`
remain useful as package-level corroboration, but the main evaluation claim in
this paper should now rest on the fresh rerun described above rather than on
acceptance text alone.
