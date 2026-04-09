# Abstract

Purpose: Hold the conservative one-paragraph abstract for the current submission line.

## TODO

- [x] Draft one bounded abstract.
- [ ] Adjust wording to match the final venue style guide.

## Draft

Runtime traces help explain what an AI system did during execution, but they do
not by themselves provide a compact, independently checkable statement of who
performed an operation, which object was acted on, which policy constrained the
action, what evidence was emitted, and how a third party can verify the result.
This paper presents `Execution Evidence and Operation Accountability Profile
v0.1`, a deliberately minimal artifact for one operation accountability
statement in an FDO-based agent setting. The artifact consists of a profile
specification, a JSON Schema, a profile-aware validator exposed through
`agent-evidence validate-profile <file>`, one valid example, three invalid
examples that each break one main rule class, and one runnable metadata
enrichment demo that produces a `validation report`. The validator checks the
bounded properties documented by the repository: schema conformance, reference
closure, consistency across policy/provenance/evidence links, and integrity
digest recomputation. The contribution is intentionally narrow. It does not
claim registry design, multi-agent governance coverage, formal deployment
evidence, or broad effectiveness guarantees. Instead, it offers a reproducible
specimen for discussing execution evidence and operation accountability through
a concrete, validated path centered on a minimal profile, a validator, and a
single end-to-end demo.
