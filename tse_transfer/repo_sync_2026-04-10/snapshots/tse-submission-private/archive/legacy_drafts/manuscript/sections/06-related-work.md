# Related Work

Purpose: Position the paper against a small number of primary-source research lines without widening the thesis.

## TODO

- [x] Reframe related work around four narrow buckets.
- [x] Keep every comparison subordinate to the bounded profile/validator/demo contribution.
- [ ] Revisit wording only if the contribution boundary changes.

## 1. DOIP / Digital Object / FDO Foundations

Digital object work provides the broadest conceptual backdrop for the present
paper. Kahn and Wilensky define a distributed digital object architecture around
identification, repository access, and object-oriented service interactions
[@kahn2006framework]. DOIP 2.0 turns that lineage into an explicit protocol for
client interaction with digital objects and the services that manage them
[@dona2018doip]. More recent FAIR Digital Object work evaluates FDOs and linked
data as distributed object systems and discusses interoperability and machine
actionability at a much larger systems level [@soilandreyes2024evaluating].

These works matter because they establish that digital objects, protocols, and
machine-actionable object ecosystems are already active research and standards
lines. However, they operate at the level of object architectures,
interoperability protocols, or distributed object system evaluation. Our paper
does not propose another object architecture, another repository protocol, or a
general FDO implementation strategy. It assumes that a digital-object setting
exists and narrows the problem to how one operation can be represented as a
small accountability artifact with a validator and a runnable demonstration.

Unlike DOIP, the Digital Object Architecture, and broader FAIR Digital Object
evaluations, this paper only targets one operation accountability statement and
a bounded validation path.

## 2. Provenance Models And Validation Constraints

The W3C PROV family provides the main reference point for provenance modeling
and validity checking. PROV-Overview explains the family structure and locates
PROV-DM as the core data model, alongside PROV-Constraints as the document that
defines valid instances for implementors of validators
[@groth2013provoverview]. PROV-DM defines a general model for entities,
activities, and agents in provenance interchange [@moreau2013provdm].
PROV-Constraints then formalizes definitions, inferences, normalization,
equivalence, and constraint-based validity checking for provenance records
[@cheney2013provconstraints].

This line of work is important because it separates provenance representation
from provenance validation and makes explicit that consistency conditions can be
first-class specification material. That is the closest methodological ancestor
of the current repository path. At the same time, our paper is much narrower
than PROV. We do not claim a general provenance data model, a full
interchange family, or a complete validator for open-ended provenance
documents. We only define a fixed-shape profile for one operation accountability
statement and a validator that checks the limited conditions documented by that
profile.

Unlike PROV-DM and PROV-Constraints, this paper only targets one operation
accountability statement and a bounded validation path.

## 3. Adjacent Verifiable Provenance / Attestation Frameworks

Software supply-chain security offers adjacent examples of verifiable
provenance-like artifacts. in-toto describes a framework in which software
supply-chain steps, actors, and ordering constraints are made transparent and
verifiable, both in the research paper and in the stable specification
[@torresarias2019intoto; @intoto2023spec]. SLSA build provenance defines an
approved provenance format for describing how build artifacts were produced so
that downstream consumers can verify them against expectations and, when
possible, rebuild them [@slsa2026buildprovenance].

These frameworks are relevant because they show that structured provenance or
attestation documents can be operationalized for downstream verification. They
also show the value of explicit fields for actors, dependencies, builders,
outputs, and verifier expectations. But their problem setting is the software
supply chain, including end-to-end build or release integrity and trust in
builder identities. Our repository does not attempt to solve that broader
problem. It does not define a supply-chain layout, trust policy, or
builder-attestation ecosystem. Instead, it fixes one small statement form for
one operation over one subject object and checks that statement against schema,
reference, linkage, and digest rules.

Unlike in-toto and SLSA build provenance, this paper only targets one operation
accountability statement and a bounded validation path.

## 4. Artifact Evaluation And Reproducibility Norms In Computing

The current evaluation posture is best understood through artifact-review norms
rather than through large experimental evaluation. ACM's artifact review and
badging policy explicitly frames artifacts in terms such as documented,
consistent, complete, exercisable, and results validated
[@acm2020artifactbadging]. That language is directly useful for the present
paper because the core research object is a runnable artifact package: a
profile, a schema, a validator command, controlled valid and invalid examples,
and one demo path that can be re-executed in a fresh environment.

This norm is a better fit for the present contribution than benchmark-oriented
evaluation language. The value of the work is not that it outperforms competing
systems or demonstrates field deployment at scale. The value is that reviewers
can inspect a compact artifact, exercise a bounded set of commands, and confirm
that the observed behavior matches the claimed profile and validator boundary.
That is also why the evaluation in this paper remains limited to one valid
example, three single-failure invalid examples, and one demo path.

Unlike ACM artifact evaluation guidance for general computational results, this
paper only targets one operation accountability statement and a bounded
validation path.
