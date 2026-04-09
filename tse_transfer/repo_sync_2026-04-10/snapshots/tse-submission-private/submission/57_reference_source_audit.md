# Reference Source Audit

This audit records the real sources selected for actual citation insertion into
the canonical TSE flagship manuscript. All selected sources are primary or
official sources directly relevant to digital objects, provenance, validation,
attestation, or artifact methodology.

## Selected Sources

| Citation key | Full source title | Source type | Why it is relevant | Supported manuscript section(s) | Priority |
| --- | --- | --- | --- | --- | --- |
| `moreau2013provdm` | `PROV-DM: The PROV Data Model` | W3C Recommendation | anchors the paper's use of provenance concepts, entities, activities, agents, and checkable provenance records | `1`, `2`, `6` | essential |
| `cheney2013provconstraints` | `Constraints of the PROV Data Model` | W3C Recommendation | anchors the idea that provenance representations can carry explicit validity and constraint-checking conditions | `1`, `3`, `6` | essential |
| `torresarias2019intoto` | `in-toto: Providing farm-to-table guarantees for bits and bytes` | peer-reviewed conference paper | provides an adjacent verification/attestation line with explicit step records and downstream verification | `1`, `2`, `6` | essential |
| `kahn2006framework` | `A framework for distributed digital object services` | peer-reviewed journal paper | anchors the digital-object architecture lineage referenced by the manuscript | `1`, `6` | supportive |
| `dona2018doip` | `Digital Object Interface Protocol Specification, Version 2.0` | official protocol specification | supports the manuscript's digital-object interaction framing while remaining broader than the paper's own scope | `1`, `2`, `6` | essential |
| `soilandreyes2024evaluating` | `Evaluating FAIR Digital Object and Linked Data as distributed object systems` | peer-reviewed journal paper | supports the FAIR Digital Object comparison point and helps bound what the paper is not claiming | `1`, `2`, `6` | supportive |
| `intoto2023spec` | `in-toto Specification` | official stable specification | supports the manuscript's claim that in-toto has an operational specification with layout, link-metadata, and verification concepts | `3`, `6` | supportive |
| `slsaProvenance` | `Provenance` | official SLSA specification page | supports the manuscript's adjacent discussion of verifiable provenance information for software artifacts | `2`, `6` | supportive |
| `slsaBuildProvenance` | `Build: Provenance` | official SLSA specification page | supports the manuscript's adjacent discussion of build-provenance predicates and downstream verification expectations | `3`, `6` | supportive |
| `groth2013provoverview` | `PROV-Overview: An Overview of the PROV Family of Documents` | W3C Working Group Note | supports the overview sentence in related work that positions PROV-DM within the broader PROV family | `6` | supportive |
| `acm2020artifactbadging` | `Artifact Review and Badging - Current` | official society policy document | supports the artifact-centered evaluation posture and the reviewer-facing framing of documented, exercisable research objects | `4`, `5`, `8` | essential |

## Rejected Candidates

- IEEE Computer Society author guidelines:
  rejected for manuscript-body insertion because they are submission-process
  guidance rather than substantive scholarly support for the paper's research
  argument. They remain relevant only to page-truth and submission checks.
- The old local `slsa2026buildprovenance` metadata pattern:
  rejected as-is because it no longer matched the current official SLSA source
  surfaces. It was replaced with current official SLSA provenance pages and a
  more conservative manuscript wording.
- ResearchGate mirrors or other secondary mirrors of primary papers:
  rejected because primary W3C, USENIX, DOI, DONA, PeerJ, ACM, GitHub, and
  SLSA sources were available.
- Any source list or material from the unrelated `Sovereign-pFDO` line:
  rejected as cross-line contamination risk and not used in the TSE flagship
  manuscript.
- Internal repo notes such as `notes/internal/review/internal-redline.md`:
  rejected because internal editing notes are not external scholarly or
  standards sources.
