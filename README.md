# Bin Zhang

Building runtime controls for AI agents: budget windows, trust gates, and execution receipts.

Researcher-builder turning protocol ideas into operational controls for agentic AI systems. Current public work emphasizes runtime components that teams can adopt directly, with protocol and research threads kept as background context.

## Main Repositories

* [token-governor](https://github.com/joy7758/token-governor) - budget windows and cost governance for agent runs.
* [aro-audit](https://github.com/joy7758/aro-audit) - execution receipts and evidence for verifiable agent runs.
* [god-spear](https://github.com/joy7758/god-spear) - trust gates for tools, files, and runtime environments.

## Current Demo Entry Points

Three small and composable runtime control demos for AI agents.

* [Token Governor - Budget Window Demo](https://github.com/joy7758/token-governor/blob/main/docs/demos/budget-window-demo.md)
* [ARO Audit - Execution Receipt Demo](https://github.com/joy7758/aro-audit/blob/main/docs/demos/execution-receipt-demo.md)
* [God Spear - Trust Gate Demo](https://github.com/joy7758/god-spear/blob/main/docs/demos/trust-gate-demo.md)

## First External Adapter

* [God Spear MCP Gate - minimal preflight trust gate for MCP-style requests](https://github.com/joy7758/god-spear-mcp-gate)

## Protocol and Research Background

* [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) - architecture overview for the broader ecosystem.
* [verifiable-dpp-agent-demo](https://github.com/joy7758/digital-biosphere-architecture/tree/main/demo/verifiable-dpp-agent-demo) - runnable end-to-end demo: DPP object -> agent result -> audit record -> MVK input -> public evidence summary.
* [persona-object-protocol](https://github.com/joy7758/persona-object-protocol) - POP for portable persona objects in multimodal and agentic AI systems.
* [agent-object-protocol](https://github.com/joy7758/agent-object-protocol) - AOP for portable and executable agent objects.
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

## Supporting Repositories

* [redrock-opendpp-core](https://github.com/joy7758/redrock-opendpp-core) - DPP-style object model and integrity core.
* [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk) - minimal verification kernel.

## Ecosystem Direction

The direction is an adoption path rather than a set of isolated repositories:

`protocol -> SDK -> plugin -> framework integration -> ecosystem visibility`

Current and planned ecosystem touchpoints include:

* LangChain
* LangGraph
* MCP
* future framework adapters

## Evidence and Research

* ORCID: [https://orcid.org/0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
* Concept DOI: [https://doi.org/10.5281/zenodo.18898251](https://doi.org/10.5281/zenodo.18898251)
* Version DOI: [https://doi.org/10.5281/zenodo.18898252](https://doi.org/10.5281/zenodo.18898252)

## Current Focus

* runtime controls and governance for AI agents
* protocol-by-artifacts and machine-checkable evidence
* framework adapters and workflow integrations
