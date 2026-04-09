# Outline

Purpose: Fix the current paper structure, research questions, and bounded contributions before full prose refinement.

## TODO

- [x] Draft a conservative five-part outline.
- [x] Record bounded research questions.
- [x] Record bounded contributions.
- [ ] Refine section order against the target venue template.

## Working Thesis

The current paper should present `Execution Evidence and Operation
Accountability Profile v0.1` as a minimal, reproducible artifact for describing
and independently checking one operation accountability statement, rather than
as a broad governance framework.

## Five-Section Paper Outline

1. Introduction and Motivation
   - Describe the accountability gap left by runtime traces alone.
   - State the narrow problem addressed by the artifact.
   - Summarize the paper's bounded contributions.
2. Problem Statement and Scope
   - Define the questions the artifact is meant to answer for one operation.
   - Clarify the single-statement, single-operation boundary.
   - Separate supported scope from non-goals.
3. Profile and Validation Design
   - Present the profile object model and compliance conditions.
   - Explain the role of internal references, policy links, provenance, evidence, and integrity digests.
   - Describe the validator pathway and output shape.
4. Demonstration and Bounded Evaluation
   - Walk through the metadata enrichment demo.
   - Report the valid example, the three invalid examples, and the acceptance checks.
   - Explain what the artifact demonstrates and what it does not.
5. Discussion, Threats, and Conclusion
   - Discuss current validity threats and boundary limits.
   - Position the artifact as a reproducible specimen for future work.
   - Conclude with narrow next steps.

## Research Questions

1. Can a deliberately minimal profile capture enough information to make one agent operation independently reviewable?
2. Can a profile-aware validator provide a bounded verification path over structure, reference closure, linkage consistency, and integrity digests?
3. Can one runnable demo plus controlled valid and invalid examples provide a reproducible specimen for discussion without claiming broader deployment success?

## Bounded Contributions

1. A minimal profile for one `operation accountability statement`, with explicit policy, provenance, evidence, and validation sections.
2. A validator pathway exposed as `agent-evidence validate-profile <file>` that reports machine-readable outcomes and explicit failure codes.
3. A reproducible package consisting of one valid example, three single-failure invalid examples, one single-path demo, and status/acceptance handoff materials.
