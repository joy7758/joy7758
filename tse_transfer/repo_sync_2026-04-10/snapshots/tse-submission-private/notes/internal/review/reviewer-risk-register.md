# Reviewer Risk Register

Purpose: Anticipate likely reviewer objections and map each one to repository evidence and a conservative response.

## TODO

- [x] Record initial reviewer risks.
- [ ] Expand responses once a target venue is chosen.

## Risks

| likely objection | why it may arise | repository evidence | conservative response |
| --- | --- | --- | --- |
| The contribution is too small. | The artifact is intentionally minimal and avoids broad claims. | `docs/STATUS.md`; `submission/final-handoff.md`; `submission/package-manifest.md` | Emphasize that minimality is the design choice: the paper contributes a reproducible, reviewable specimen rather than a full platform. |
| The work does not show deployment evidence. | The repository does not claim external deployment. | `manuscript/claims/scope-and-non-goals.md`; `submission/final-handoff.md` | State clearly that deployment evidence is out of scope for v0.1 and is not claimed. |
| Evaluation breadth is limited. | The current evaluation uses examples, tests, demo, and acceptance materials rather than new experiments. | `examples/README.md`; `demo/expected-output.md`; `tests/test_operation_accountability_profile.py`; `docs/ACCEPTANCE-CHECKLIST.md` | Frame the evaluation as bounded artifact verification, not as broad empirical testing. |
| The paper may be confused with broader historical materials in the repo. | The repository retains earlier `Execution Evidence Object` and `Agent Evidence Profile` surfaces. | `README.md`; `docs/STATUS.md` | Keep terminology fixed on the current v0.1 package and explicitly separate historical surfaces from the main line. |
| The validator may appear underspecified. | Reviewers may want to know exactly what is checked. | `spec/execution-evidence-operation-accountability-profile-v0.1.md`; `demo/expected-output.md`; `tests/test_operation_accountability_profile.py` | Point to the documented compliance/failure conditions and the controlled error-code behavior. |
| The paper may overstate governance implications. | The topic area invites inflation. | `manuscript/claims/claim-evidence-map.md`; `manuscript/claims/contribution-boundary.md`; `manuscript/claims/scope-and-non-goals.md` | Keep framing method-centric and artifact-centric, and explicitly reject unsupported governance claims. |
