# Bin Zhang

## Digital Biosphere Architecture for Verifiable AI Systems

Researcher-builder working on protocol drafts and infrastructure components for multimodal and agentic AI systems.

My focus is on portable AI objects, execution integrity, resource governance, and machine-checkable evidence. The work sits between research and infrastructure: turning protocol ideas into specifications, repositories, and operational tooling.

## Entry Points

* [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) - architecture overview for the Digital Biosphere ecosystem.
* [verifiable-dpp-agent-demo](https://github.com/joy7758/digital-biosphere-architecture/tree/main/demo/verifiable-dpp-agent-demo) - runnable end-to-end demo: DPP object -> agent result -> audit record -> MVK input -> public evidence summary.
* Narrative spine: `Digital Biosphere -> Verifiable Digital Objects -> Execution Integrity`

## Architecture Layers

```text
Persona Layer    -> Persona Object Protocol (POP)
Agent Layer      -> Agent Object Protocol (AOP)
Data Space Layer -> RedRock OpenDPP
Audit Layer      -> ARO-Audit
Proof Kernel     -> MVK
```

Supporting governance:

```text
Resource Governance -> Token Governor
```

## Core Repositories

* [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) - architecture overview and ecosystem entry point.
* [redrock-opendpp-core](https://github.com/joy7758/redrock-opendpp-core) - DPP-style object model and integrity core.
* [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk) - minimal verification kernel.
* [token-governor](https://github.com/joy7758/token-governor) - token, cost, and resource governance tooling for AI systems.
* [persona-object-protocol](https://github.com/joy7758/persona-object-protocol) - POP for portable persona objects in multimodal and agentic AI systems.
* [agent-object-protocol](https://github.com/joy7758/agent-object-protocol) - AOP for portable and executable agent objects.
* [aro-audit](https://github.com/joy7758/aro-audit) - audit, provenance, and execution integrity for AI runs.

## Ecosystem Direction

The direction is not a set of isolated repositories, but an infrastructure path:

`protocol -> SDK -> plugin -> framework integration -> ecosystem visibility`

Current and planned ecosystem touchpoints include:

* LangChain
* LangGraph
* future framework adapters

## Evidence and Research

* ORCID: [https://orcid.org/0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
* Concept DOI: [https://doi.org/10.5281/zenodo.18898251](https://doi.org/10.5281/zenodo.18898251)
* Version DOI: [https://doi.org/10.5281/zenodo.18898252](https://doi.org/10.5281/zenodo.18898252)

## Current Focus

* POP integration in the LangChain ecosystem
* protocol-by-artifacts and machine-checkable evidence
* runtime integrity and governance for AI agents
