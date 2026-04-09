# Reproducibility

Purpose: Capture the reproducibility path supported by the public artifact without adding new experiments.

## TODO

- [x] Record a fresh local environment setup note.
- [x] Record the minimal dependency install path actually tested.
- [x] Record exact commands, outputs, exit statuses, and environment details from a clean rerun.
- [ ] Add venue-specific artifact instructions if required.

## Fresh Local Environment Setup Note

- Run timestamp: `2026-04-07 00:21:53 +0800 CST`
- Source repository: `joy7758/agent-evidence`
- Source commit: `80e7e78ab6cbd9befc24b56fbf9cdffabd99b5de`
- Host platform: `Darwin zhangbindeMacBook-Air-2.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:54:55 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8132 arm64`
- Python launcher used to create the environment: `Python 3.14.3`
- Fresh virtual environment: `/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full`
- Virtual environment Python: `3.14.3 (main, Mar 25 2026, 03:28:18) [Clang 22.1.1 ]`
- pip in the fresh environment: `pip 26.0.1`
- Site-packages root:
  `/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/lib/python3.14/site-packages`
- Full local log root: `/tmp/agent-evidence-repro-20260407-full`
- Agent repository working tree after the rerun: clean

## Minimal Dependency Install Actually Tested

This fresh rerun did not use `.[dev]`. The minimal installation path that was
actually tested was the base editable install:

```bash
python3 -m venv /Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python -m pip install --upgrade pip
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python -m pip install -e /Users/zhangbin/GitHub/agent-evidence
```

Create-venv command exit status: `0`

Exact output of the create-venv command:

```text
```

Upgrade-pip command exit status: `0`

Exact output of the pip upgrade command:

```text
Requirement already satisfied: pip in ./.repro-v0_1-20260407-full/lib/python3.14/site-packages (25.3)
Collecting pip
  Using cached pip-26.0.1-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-26.0.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.3
    Uninstalling pip-25.3:
      Successfully uninstalled pip-25.3
Successfully installed pip-26.0.1
```

Base install command exit status: `0`

Exact output of the base install command:

```text
Obtaining file:///Users/zhangbin/GitHub/agent-evidence
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Checking if build backend supports build_editable: started
  Checking if build backend supports build_editable: finished with status 'done'
  Getting requirements to build editable: started
  Getting requirements to build editable: finished with status 'done'
  Preparing editable metadata (pyproject.toml): started
  Preparing editable metadata (pyproject.toml): finished with status 'done'
Collecting click>=8.1 (from agent-evidence==0.2.0)
  Using cached click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
Collecting jsonschema>=4.23 (from agent-evidence==0.2.0)
  Using cached jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting pydantic>=2.7 (from agent-evidence==0.2.0)
  Using cached pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting attrs>=22.2.0 (from jsonschema>=4.23->agent-evidence==0.2.0)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.23->agent-evidence==0.2.0)
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.23->agent-evidence==0.2.0)
  Using cached referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.23->agent-evidence==0.2.0)
  Downloading rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.7->agent-evidence==0.2.0)
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.7->agent-evidence==0.2.0)
  Downloading pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl.metadata (7.3 kB)
Collecting typing-extensions>=4.14.1 (from pydantic>=2.7->agent-evidence==0.2.0)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.7->agent-evidence==0.2.0)
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Using cached click-8.3.2-py3-none-any.whl (108 kB)
Using cached jsonschema-4.26.0-py3-none-any.whl (90 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached pydantic-2.12.5-py3-none-any.whl (463 kB)
Using cached pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl (1.9 MB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached referencing-0.37.0-py3-none-any.whl (26 kB)
Using cached rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl (353 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Building wheels for collected packages: agent-evidence
  Building editable for agent-evidence (pyproject.toml): started
  Building editable for agent-evidence (pyproject.toml): finished with status 'done'
  Created wheel for agent-evidence: filename=agent_evidence-0.2.0-0.editable-py3-none-any.whl size=11203 sha256=5c16b895c60195be6e59e252b9795c7e34f1d86aec6ed7c69bda1e395b3fa099
  Stored in directory: /private/var/folders/rb/8ljcv7vj35z2z3m9k2k3n1000000gn/T/pip-ephem-wheel-cache-qfn_mqis/wheels/72/c7/5e/392707469bc9a120b02b3eda1b346b8ad448060fe57cb1c4e6
Successfully built agent-evidence
Installing collected packages: typing-extensions, rpds-py, click, attrs, annotated-types, typing-inspection, referencing, pydantic-core, pydantic, jsonschema-specifications, jsonschema, agent-evidence

Successfully installed agent-evidence-0.2.0 annotated-types-0.7.0 attrs-26.1.0 click-8.3.2 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 pydantic-2.12.5 pydantic-core-2.41.5 referencing-0.37.0 rpds-py-0.30.0 typing-extensions-4.15.0 typing-inspection-0.4.2
```

Installed package set from `pip freeze`:

```text
-e git+https://github.com/joy7758/agent-evidence.git@80e7e78ab6cbd9befc24b56fbf9cdffabd99b5de#egg=agent_evidence
annotated-types==0.7.0
attrs==26.1.0
click==8.3.2
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
pydantic==2.12.5
pydantic_core==2.41.5
referencing==0.37.0
rpds-py==0.30.0
typing-inspection==0.4.2
typing_extensions==4.15.0
```

No extra dependencies beyond the base install were required for the current
minimal profile/validator/demo path.

## Exact Rerun Log

### 1. Valid example

Command:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/minimal-valid-evidence.json
```

Exit status: `0`

Exact output:

```json
{
  "issue_count": 0,
  "ok": true,
  "profile": "execution-evidence-operation-accountability-profile@0.1",
  "source": "examples/minimal-valid-evidence.json",
  "stages": [
    {
      "issues": [],
      "name": "schema",
      "ok": true
    },
    {
      "issues": [],
      "name": "references",
      "ok": true
    },
    {
      "issues": [],
      "name": "consistency",
      "ok": true
    },
    {
      "issues": [],
      "name": "integrity",
      "ok": true
    }
  ],
  "summary": [
    "PASS execution-evidence-operation-accountability-profile@0.1 examples/minimal-valid-evidence.json"
  ]
}
```

### 2. Invalid example: missing required field

Command:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-missing-required.json
```

Exit status: `1`

Exact output:

```json
{
  "issue_count": 1,
  "ok": false,
  "profile": "execution-evidence-operation-accountability-profile@0.1",
  "source": "examples/invalid-missing-required.json",
  "stages": [
    {
      "issues": [
        {
          "code": "schema_violation",
          "message": "'method' is a required property",
          "path": "validation",
          "stage": "schema"
        }
      ],
      "name": "schema",
      "ok": false
    },
    {
      "issues": [],
      "name": "references",
      "ok": true
    },
    {
      "issues": [],
      "name": "consistency",
      "ok": true
    },
    {
      "issues": [],
      "name": "integrity",
      "ok": true
    }
  ],
  "summary": [
    "FAIL execution-evidence-operation-accountability-profile@0.1 examples/invalid-missing-required.json (1 issue(s))",
    "[schema_violation] validation: 'method' is a required property"
  ]
}
```

### 3. Invalid example: unclosed reference

Command:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-unclosed-reference.json
```

Exit status: `1`

Exact output:

```json
{
  "issue_count": 1,
  "ok": false,
  "profile": "execution-evidence-operation-accountability-profile@0.1",
  "source": "examples/invalid-unclosed-reference.json",
  "stages": [
    {
      "issues": [],
      "name": "schema",
      "ok": true
    },
    {
      "issues": [
        {
          "code": "unresolved_output_ref",
          "message": "operation output ref does not resolve to evidence.references[].ref_id.",
          "path": "operation.output_refs[0]",
          "stage": "references"
        }
      ],
      "name": "references",
      "ok": false
    },
    {
      "issues": [],
      "name": "consistency",
      "ok": true
    },
    {
      "issues": [],
      "name": "integrity",
      "ok": true
    }
  ],
  "summary": [
    "FAIL execution-evidence-operation-accountability-profile@0.1 examples/invalid-unclosed-reference.json (1 issue(s))",
    "[unresolved_output_ref] operation.output_refs[0]: operation output ref does not resolve to evidence.references[].ref_id."
  ]
}
```

### 4. Invalid example: broken policy link

Command:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/agent-evidence validate-profile examples/invalid-policy-link-broken.json
```

Exit status: `1`

Exact output:

```json
{
  "issue_count": 1,
  "ok": false,
  "profile": "execution-evidence-operation-accountability-profile@0.1",
  "source": "examples/invalid-policy-link-broken.json",
  "stages": [
    {
      "issues": [],
      "name": "schema",
      "ok": true
    },
    {
      "issues": [
        {
          "code": "unresolved_evidence_policy_ref",
          "message": "evidence.policy_ref must resolve to policy.id.",
          "path": "evidence.policy_ref",
          "stage": "references"
        }
      ],
      "name": "references",
      "ok": false
    },
    {
      "issues": [],
      "name": "consistency",
      "ok": true
    },
    {
      "issues": [],
      "name": "integrity",
      "ok": true
    }
  ],
  "summary": [
    "FAIL execution-evidence-operation-accountability-profile@0.1 examples/invalid-policy-link-broken.json (1 issue(s))",
    "[unresolved_evidence_policy_ref] evidence.policy_ref: evidence.policy_ref must resolve to policy.id."
  ]
}
```

### 5. Demo

Command:

```bash
/Users/zhangbin/GitHub/agent-evidence/.repro-v0_1-20260407-full/bin/python demo/run_operation_accountability_demo.py
```

Exit status: `0`

Exact output:

```text
Step 1: object load or creation
- loaded obj:client-note-001
Step 2: profile precheck
- source object is ready for the minimal profile
Step 3: operation call
- emitted obj:client-note-001-derived
Step 4: evidence generation
- wrote minimal-profile-evidence.json
Step 5: validator verification
- PASS execution-evidence-operation-accountability-profile@0.1 /Users/zhangbin/GitHub/agent-evidence/demo/artifacts/minimal-profile-evidence.json
Step 6: output verification result
- evidence: /Users/zhangbin/GitHub/agent-evidence/demo/artifacts/minimal-profile-evidence.json
- report:   /Users/zhangbin/GitHub/agent-evidence/demo/artifacts/validation-report.json
```

## Outcome

- The fresh clean rerun matched the current minimal v0.1 profile/validator/demo path.
- The valid example and demo exited `0`.
- The three invalid examples exited `1` and produced the expected primary error codes.
- No installation failure occurred in the clean environment, so no code fix was required for this rerun.

## Minimal Fix Guidance

No fix was needed for this clean rerun.

If a future local rerun fails before command execution, the minimal first fix is
to recreate a fresh virtual environment and install the base package with:

```bash
python3 -m venv <fresh-venv>
<fresh-venv>/bin/python -m pip install -e /path/to/agent-evidence
```

That base install was sufficient for the current v0.1 path in this check.

## Boundary

This manuscript package should report the validated path already documented by
the public repository. It should not introduce new benchmark runs, deployment
claims, or broader empirical results that are absent from the artifact.
