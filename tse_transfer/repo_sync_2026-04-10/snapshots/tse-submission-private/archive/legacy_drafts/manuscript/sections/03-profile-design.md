# Profile Design

Purpose: Describe the profile object model, compliance conditions, and intended verification surface.

## TODO

- [x] Summarize the profile structure.
- [x] Summarize compliance and failure conditions.
- [ ] Add figure/table cross-references during paper assembly.

## Draft

`Execution Evidence and Operation Accountability Profile v0.1` defines a
minimal JSON profile for one `operation accountability statement`. The top-level
structure contains eleven sections: `profile`, `statement_id`, `timestamp`,
`actor`, `subject`, `operation`, `policy`, `constraints`, `provenance`,
`evidence`, and `validation`. This structure is reflected both in the profile
specification and in the accompanying JSON Schema.

The design keeps the required information centered on four review questions.
First, the statement must identify the actor, subject, and operation. Second,
it must name the governing policy and the referenced constraints. Third, it
must preserve cross-section linkage through subject, operation, policy, input,
and output references. Fourth, it must expose enough integrity material for a
bounded recomputation of statement, reference, and artifact digests.

The compliance conditions documented in the profile are correspondingly narrow.
A statement is compliant only if the profile identity matches the fixed v0.1
name and version, the JSON instance satisfies the schema, internal references
close correctly, input and output references resolve to the appropriate roles,
policy/provenance/evidence linkages remain consistent, and the documented
integrity digests recompute to the expected values. The failure conditions are
the symmetric negatives of these checks: missing required fields, schema shape
violations, unclosed references, role mismatches, inconsistent linkages, or
digest recomputation failures.

This profile shape is intentionally smaller than a general evidence or
governance model. The paper should present that narrowness as a design choice:
the artifact aims to make one accountability statement concrete and reviewable,
not to solve the full surrounding system problem in v0.1.
