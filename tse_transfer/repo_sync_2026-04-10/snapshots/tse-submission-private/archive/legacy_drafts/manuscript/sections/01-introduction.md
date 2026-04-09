# Introduction

Purpose: Introduce the accountability problem, motivate the artifact, and state the paper's bounded contribution.

## TODO

- [x] Draft the introduction around the validated artifact.
- [ ] Tune the opening for the final venue.

## Draft

Runtime traces and logs are useful for debugging agent executions, but they do
not automatically provide a compact statement that an external reviewer can
check later. For the current research line, the missing question is deliberately
bounded: for one operation, can a reviewer determine who executed it, which
object was acted on, which policy constrained it, what evidence was emitted,
and how the statement can be independently verified? The public artifact in
`agent-evidence` addresses that narrow gap with a small reproducible package
rather than a broad governance platform.

The package centers on `Execution Evidence and Operation Accountability Profile
v0.1`. The profile defines one `operation accountability statement` with
explicit sections for actor, subject, operation, policy, constraints,
provenance, evidence, and validation. The repository also exposes a
profile-aware validator through `agent-evidence validate-profile <file>`,
provides one passing example and three controlled failing examples, and includes
a runnable metadata-enrichment demo that ends in a `validation report`.

The contribution claimed in this paper is intentionally narrow. We do not claim
registry design, multi-agent accountability composition, full FDO mapping,
external deployment evidence, or broad AI governance effectiveness. Instead, we
present a reproducible specimen that makes the current minimum accountability
loop concrete and reviewable. That specimen is sufficient for a paper focused
on artifact shape, validation boundary, and conservative independent
verification.
