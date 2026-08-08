# Bin Zhang — Trustworthy Infrastructure for Autonomous AI Systems

I am a **Research Engineer building trustworthy infrastructure for autonomous AI systems**.

My work focuses on execution evidence, evaluation, identity and provenance, failure analysis, and bounded agent actions for **autonomous experimental loops**: the infrastructure required to understand what an autonomous system did, under which conditions, whether the result can be checked independently, and whether a proposed change should be adopted.

My current research direction is **DCELL**:

> How can autonomous AI systems become minimal, independently identifiable, evidence-producing, experience-preserving, and evolvable digital entities?

**Status: `RESEARCH_DIRECTION`.** DCELL is an organizing research question, not a finished platform. Complete autonomous adaptation, cross-generation experience inheritance, and multi-system capability growth remain unverified hypotheses.

## Selected public evidence

### [Verifiable Agent Demo](https://github.com/joy7758/verifiable-agent-demo)

A bounded public path for observing an agent execution and producing evidence that can be inspected and checked.

- **Status:** minimal public path `EXPERIMENTALLY_SUPPORTED`; broader path `PROTOTYPE`.
- **Evidence:** the minimal path ran in the 2026-08-08 audit, and public build/verification checks were visible at the audited revision.
- **Limit:** full and enterprise paths depend on private extensions and are not independently reproducible from the public repository alone.

### [SAEE](https://github.com/joy7758/SAEE)

Experimental infrastructure for agent health assessment and candidate-change evaluation.

- **Status:** `EXPERIMENTALLY_SUPPORTED`.
- **Evidence:** the audited revision passed 84 local unit tests, a consolidation smoke path, and a bounded public demo.
- **Limit:** the audited revision did not expose source-test CI; this is experimental evidence, not a claim of autonomous self-improvement or production readiness.

### [TITMAS Agent Action Gate](https://github.com/joy7758/titmas-agent-action-gate)

Evidence-aware contracts for bounded agent actions, negative evidence, and explicit authorization boundaries.

- **Status:** tested contract surface `IMPLEMENTED`; broader runtime governance `EXPERIMENTALLY_SUPPORTED`.
- **Evidence:** current public contract checks passed at the audited revision.
- **Limit:** passing contract checks does not establish a complete autonomous runtime or independent decision authority.

## Evidence maturity

### Implemented

- The tested contract surface in `titmas-agent-action-gate`.
- Tested, versioned identity and persona-object surfaces in [Persona Object Protocol](https://github.com/joy7758/persona-object-protocol).

`IMPLEMENTED` refers only to the bounded technical surfaces directly supported by code, tests, or CI.

### Experimentally Supported

- The minimal public execution-evidence path in `verifiable-agent-demo`.
- Agent health and candidate-change evaluation paths in `SAEE`.
- Broader evidence-aware governance patterns around the tested action-gate contracts.

`EXPERIMENTALLY_SUPPORTED` means that a runnable experiment supports a limited claim; it does not imply generality or operational readiness.

### Prototype

- [TITMAS Demo](https://github.com/joy7758/titmas-demo), an **early engineering seed and first experimental instance of the DCELL research direction**. It is a deterministic prototype for observable, verifiable, and health-assessable agent execution.
- The broader public/private integration path around `verifiable-agent-demo`.
- [TEK](https://github.com/joy7758/tek-system), a seeded stress and candidate-change evaluation prototype.

TITMAS is not the central controller of DCELL. It is retained as an early engineering experiment that should remain observable, replaceable, evolvable, and bypassable. The public demo does not establish a complete Cell lifecycle.

### Research Direction

- **DCELL:** evidence-driven, bounded, replaceable, and evolvable autonomous systems.
- Experience continuity: preserving validated success and failure records with provenance, scope, expiry, and revocation.
- Evaluation before adoption: comparing baseline and candidate behavior before a change becomes actionable.

These are active technical questions, not completion claims.

### Future Hypothesis

- Evidence-backed experience can transfer safely across agents or generations without propagating stale or unsupported conclusions.
- A bounded autonomous component can be replaced or bypassed without losing experiment lineage, verification, or rollback capability.
- Multiple bounded systems can create increasing capability without depending on one irreplaceable controller.

These hypotheses require public experiments, baselines, negative cases, and reproducible results.

## Problems I want to solve in autonomous discovery systems

- Who performed an experiment, and under which model, tools, environment, and configuration?
- What happened during execution, and can another system verify it independently?
- Can results be reproduced after dependencies or environments change?
- Did a candidate modification improve the system relative to a locked baseline?
- Can failed experiments become scoped, revocable, reusable experience?
- How should evidence, evaluation, authorization, and action remain separate?

My strongest public evidence is in **agents, infrastructure, and evaluations**. Environment capture is partial: I have not yet demonstrated a complete portable environment capsule or multi-environment conformance suite.

## Engineering approach

I prefer:

- source-locked, reproducible artifacts;
- explicit positive and negative tests;
- content-addressed evidence and versioned identities;
- visible failures and known limitations;
- evaluation before adoption;
- fail-closed behavior when evidence or authority is missing;
- clear separation between technical verification and authorization.

```text
observation != evidence
evidence != verification
verification != evaluation
evaluation != authorization
authorization != decision
decision != execution
specification != implementation
```

A passing test, CI run, release, DOI, or successful demo supports only the artifact and scope it directly checks. It does not by itself establish scientific truth, production readiness, external adoption, or permission to act.

## Research ownership and AI-assisted implementation

I use AI coding agents as implementation and review tools. Research questions, experiment design, acceptance criteria, architectural decisions, evidence interpretation, failure analysis, and authorization decisions remain human-owned.

I use reproducible artifacts, negative cases, decision records, and explicit limitations to make that ownership inspectable.

---

Audit snapshot: 2026-08-08. Claims should be rechecked when repository revisions, dependencies, CI, or visibility change.
