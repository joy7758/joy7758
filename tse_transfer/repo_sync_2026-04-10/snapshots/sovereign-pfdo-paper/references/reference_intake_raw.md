# Sovereign-pFDO Reference Intake Raw

## Intake Status

This file is a raw holding area for references extracted from the original
submission-package docx:

- source document:
  `docs/original_material/2026-04-06_sovereign_pfdo_submission_package_ready.docx`
- extraction status:
  first-pass raw intake only
- direct-use status:
  do not copy entries from this file directly into
  `references/sovereign_references_master.bib`

The list below contains mixed-quality material. It is useful as an intake
queue, not as a clean bibliography.

## Intake Rules

- Prefer primary sources, standards, RFCs, peer-reviewed papers, and official
  institutional documents.
- Replace mirrors with primary publication pages whenever possible.
- Exclude low-trust or informal sources from the final bibliography unless a
  strong justification is documented separately.
- Treat vendor blogs, Reddit, YouTube, Stack Overflow, and ResearchGate mirrors
  as intake leads only.

## Raw Extracted Candidates

### Potentially Retainable After Primary-Source Verification

- `Evaluation Report Security Level of Cryptography - SHA-256`
  url: `https://www.cryptrec.go.jp/exreport/cryptrec-ex-1045-2001.pdf`
  note: official institutional document; verify direct relevance to the final
  PID / collision argument
- `rfc9562.xml - RFC Editor`
  url: `https://www.rfc-editor.org/rfc/rfc9562.xml`
  note: official RFC source; verify exact use case before citation
- `Evaluating FAIR Digital Object and Linked Data as distributed object systems`
  url: `https://pmc.ncbi.nlm.nih.gov/articles/PMC11157569/`
  note: replace the PMC mirror with the primary journal or DOI landing page

### Replace With Better Primary Or Peer-Reviewed Sources

- `Drift No More? Context Equilibria in Multi-Turn LLM Interactions`
  url: `https://arxiv.org/html/2510.07777v1`
  note: preprint; replace with peer-reviewed or stronger primary source if the
  manuscript still needs this line
- `An Evidence-Grounded Research Assistant for Functional Genomics`
  url: `https://www.biorxiv.org/content/10.64898/2025.12.30.697073v1.full-text`
  note: preprint; relevance to this line is currently weak
- `Agent Drift: Quantifying Behavioral Degradation in Multi ...`
  url: `https://arxiv.org/abs/2601.04170`
  note: preprint; keep only if the final argument truly needs AI-drift support
- `Terabit Ethernet - Teledyne LeCroy Xena`
  url: `https://xenanetworks.com/solutions/tbps/`
  note: vendor material; replace with standards or peer-reviewed networking
  sources if retained
- `Looking at FAIR Digital Objects (FDOs) from a PID perspective`
  url: `https://blog.tib.eu/2022/11/10/its-all-about-the-message-to-be-finally-heard-looking-at-fair-digital-objects-fdos-from-a-pid-perspective/`
  note: blog source; replace with primary FDO / PID literature
- `Responsible AI in Marketing: AI Booing and AI Washing Cycle of AI`
  url: `https://research.sabanciuniv.edu/52576/1/Responsible.pdf`
  note: relevance to protocol/governance architecture is unclear
- `How 1.6T Ethernet will Enable the World's Fastest Datacenters`
  url: `https://www.eetimes.com/podcasts/how-1-6t-ethernet-will-enable-the-worlds-fastest-data-centers/`
  note: news/podcast source; replace with technical standards or engineering
  papers
- `Synopsys 1.6T Ethernet IP reduces interconnect power use by 50%`
  url: `https://www.embedded.com/synopsys-1-6t-ethernet-ip-reduces-interconnect-power-use-by-50/`
  note: industry press source; replace with stronger networking evidence

### Low-Trust Or Direct-Exclude For Formal Bibliography

- `x86 model memory latency, L1/L2 cache, and its effects on suitability`
  url: `https://www.reddit.com/r/networking/comments/btlg6v/x86_model_memory_latency_l1l2_cache_and_its/`
  reason: Reddit
- `Summary of existing collision attacks on SHA-3`
  url: `https://www.researchgate.net/figure/Summary-of-existing-collision-attacks-on-SHA-3_tbl1_363420820`
  reason: ResearchGate mirror / image snippet
- `How safe is XOR'ing cryptographic hashes?`
  url: `https://www.reddit.com/r/cryptography/comments/1cf0jkb/how_safe_is_xoring_cryptographic_hashes/`
  reason: Reddit
- `LPC2018 - Path to DPDK speeds for AF XDP`
  url: `https://www.youtube.com/watch?v=JmGfJok32Kw`
  reason: YouTube
- `The Synergistic Role of 1.6T and AI Networking | Celestica`
  url: `https://www.celestica.com/blog/article/the-synergistic-role-of-1.6t-and-ai-networking`
  reason: company blog
- `400G Ethernet RDMA Network Cards: Revolutionizing Data Center`
  url: `https://ascentoptics.com/blog/400g-ethernet-rdma-network-cards/`
  reason: company blog
- `Algorithm Implementation/Checksums - Wikibooks`
  url: `https://en.wikibooks.org/wiki/Algorithm_Implementation/Checksums`
  reason: tertiary wiki source
- `How should I be handling checksum collisions in my application?`
  url: `https://stackoverflow.com/questions/1903547/how-should-i-be-handling-checksum-collisions-in-my-application`
  reason: Stack Overflow
- `Machine Learning-Augmented Neurosymbolic Agenticops`
  url: `https://rsisinternational.org/journals/ijrsi/uploads/vol12-iss11-pg2306-2319-202512_pdf.pdf`
  reason: unclear venue quality and unclear relevance
- `How smart NICs, DPDK, and programmable chips are reshaping the`
  url: `https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-1358.pdf`
  reason: weak venue confidence
- `Drift No More? Context Equilibria in Multi-Turn LLM Interactions`
  url: `https://www.researchgate.net/publication/396373136_Drift_No_More_Context_Equilibria_in_Multi-Turn_LLM_Interactions`
  reason: ResearchGate mirror
- `(PDF) Solving a 112-bit prime elliptic curve discrete logarithm`
  url: `https://www.researchgate.net/publication/262201409_Solving_a_112-bit_prime_elliptic_curve_discrete_logarithm_problem_on_game_consoles_using_sloppy_reduction`
  reason: ResearchGate mirror and likely irrelevant to the current line

## Next Cleanup Step

Before any citation insertion round, convert this intake into:

- `references/sovereign_references_master.bib`
- `references/reference_source_audit.md`
- `references/citation_insertion_log.md`

Only primary or clearly credible sources should survive that cleanup.
