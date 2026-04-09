# Sovereign-pFDO Reference Source Audit

## Scope

This file records the current whitelist for
`references/sovereign_references_master.bib`.

The master bibliography is intentionally narrow. It only contains sources that
are appropriate for the manuscript's current active claims:

- protocol-layer digital-object background
- hash-primitive background for a bounded PID construction template
- CRC32c as a low-cost integrity surface
- standards-trajectory background for high-throughput Ethernet
- official product background for DPU / SmartNIC deployment relevance
- one formal information-theory anchor for KL divergence

## Whitelist Entries Added To Master Bib

### Core Standards And Official Sources

- `dona2018doip`
  - source: DONA Foundation
  - title: `Digital Object Interface Protocol Specification, Version 2.0`
  - role: primary source for digital-object protocol background
  - supported claims:
    - distributed digital-object environments
    - protocol-layer interaction background

- `aumasson2024blake3`
  - source: IETF Internet-Draft
  - title: `The BLAKE3 Hashing Framework`
  - role: primary source for BLAKE3 as a fast, highly parallelizable hashing primitive
  - supported claims:
    - bounded PID construction template
    - hash-based identifier composition language

- `stewart2022rfc9260`
  - source: RFC 9260
  - title: `Stream Control Transmission Protocol`
  - role: primary source for CRC32c in transport-level usage
  - supported claims:
    - CRC32c-style low-cost integrity surface
    - data corruption protection / transport integrity context

- `ieee8022025p8023dj`
  - source: IEEE 802.3 Ethernet Working Group
  - title: `IEEE P802.3dj 200 Gb/s, 400 Gb/s, 800 Gb/s, and 1.6 Tb/s Ethernet Task Force`
  - role: official standards-trajectory background
  - supported claims:
    - 1.6 Tb/s as standards and ecosystem pressure
    - not a local empirical proof point

- `nvidiaBlueField3`
  - source: NVIDIA
  - title: `NVIDIA BlueField-3 DPU`
  - role: official deployment-relevance source
  - supported claims:
    - DPU / SmartNIC deployment relevance
    - official 400Gb/s product capability background

### Background Sources Kept For Context

- `kahn2006framework`
  - source: International Journal on Digital Libraries
  - role: digital-object architecture background
  - supported claims:
    - conceptual digital-object lineage

- `soilandreyes2024evaluating`
  - source: PeerJ Computer Science
  - role: current FAIR Digital Object / distributed object background
  - supported claims:
    - FDO-related context
    - distributed object framing background

- `kullback1951information`
  - source: The Annals of Mathematical Statistics
  - role: formal information-theory anchor
  - supported claims:
    - KL divergence as a mathematical quantity
    - not AI-drift performance claims

## Current Manuscript Usage Status

The current active manuscript uses every entry in
`references/sovereign_references_master.bib`.

- `dona2018doip`
  - used in: `Abstract`, `1. Introduction`
- `aumasson2024blake3`
  - used in: `Abstract`, `4. Bounded PID Construction Template`
- `stewart2022rfc9260`
  - used in: `4. Bounded PID Construction Template`
- `ieee8022025p8023dj`
  - used in: `6. Offload-Oriented Deployment Considerations`
- `nvidiaBlueField3`
  - used in: `6. Offload-Oriented Deployment Considerations`
- `kahn2006framework`
  - used in: `Abstract`, `1. Introduction`
- `soilandreyes2024evaluating`
  - used in: `Abstract`, `1. Introduction`
- `kullback1951information`
  - used in: `5. Divergence-Triggered Gateway Intervention`

Unused master-bib entries:

- none

## Intake Entries Explicitly Excluded From Master Bib

The following classes of entries remain excluded from the formal bibliography:

- Reddit discussions
- ResearchGate mirrors and image snippets
- YouTube videos
- Stack Overflow discussions
- vendor blogs and marketing posts
- weak or unclear venue PDFs
- preprints that are not necessary for the current bounded claims

Concrete excluded examples from `reference_intake_raw.md`:

- `x86 model memory latency, L1/L2 cache, and its effects on suitability`
- `Summary of existing collision attacks on SHA-3`
- `How safe is XOR'ing cryptographic hashes?`
- `LPC2018 - Path to DPDK speeds for AF XDP`
- `The Synergistic Role of 1.6T and AI Networking | Celestica`
- `400G Ethernet RDMA Network Cards: Revolutionizing Data Center`
- `Algorithm Implementation/Checksums - Wikibooks`
- `How should I be handling checksum collisions in my application?`
- `How smart NICs, DPDK, and programmable chips are reshaping the`
- ResearchGate mirrors of `Drift No More?` and unrelated ECC material

## Residual Source Gaps

- No single formal source for the manuscript's gateway-policy operational
  choices has been selected yet; the manuscript currently keeps that part at
  architecture level.
- No formal source has been added yet for empirical deployment results, because
  the current manuscript deliberately does not make completed throughput-proof
  claims.
- Any future citation of product capability or standards trajectory should stay
  within the bounded roles already listed above.
