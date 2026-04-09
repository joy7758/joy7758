# Citation Insertion Targets

This note maps where human citation insertion or citation verification is still
needed in the TSE flagship manuscript. It does not invent citations and does
not introduce placeholder references.

## Essential Citations

| Manuscript section | Paragraph or topic | Why a citation is needed | Type of source needed |
| --- | --- | --- | --- |
| `Abstract` | opening claim that runtime traces alone do not provide a compact independently checkable account | the problem statement should be anchored in prior accountability, provenance, or traceability literature rather than left as a naked assertion | prior research or standards source on auditability, provenance, or trace limitations |
| `1. Introduction` | motivation for moving from runtime traces to a checkable operation statement | this is the conceptual bridge into the paper's main contribution and should be situated against existing trace/provenance/accountability work | primary-source research or standards documents on provenance, accountability, or verifiable execution records |
| `2. Problem and Scope` | framing of one-operation accountability and bounded independent verification | the paper's boundary argument benefits from showing that narrower statement-level verification is a deliberate choice relative to broader adjacent work | primary-source research or standards documents defining broader provenance or digital-object settings |
| `3. Profile Design` | compliance conditions, reference closure, linkage consistency, and digest recomputation as validation dimensions | these conditions are central to the profile's verification boundary and should be tied to specification or validation-model precedents | formal specification, schema-validation, provenance-constraint, or integrity-checking source |
| `4. Validator and Demo Path` | interpretation of the controlled valid/invalid example set as a bounded verification surface | the paper should justify why a controlled example set is an acceptable evidence form for this kind of artifact contribution | artifact-evaluation or software-validation methodology source |
| `5. Evaluation` | claim that the evaluation is intentionally artifact-bounded rather than benchmark-oriented | this evaluation posture should be anchored in publication norms for artifact-centered work | artifact-evaluation, reproducibility, or software engineering review-policy source |
| `7. Threats to Validity` | discussion of narrow scope and limited evaluation breadth | threat framing is stronger when aligned with established validity or reproducibility discourse | methodology source on threats to validity, bounded evaluation, or artifact review |

## Supportive Citations

| Manuscript section | Paragraph or topic | Why a citation is needed | Type of source needed |
| --- | --- | --- | --- |
| `1. Introduction` | description of digital-object-informed agent setting | useful for readers who need orientation on the surrounding technical context, but not strictly required for the narrow claim | digital object, DOIP, or FAIR Digital Object background source |
| `2. Problem and Scope` | explicit non-goals such as registry design, multi-agent orchestration, and full cryptographic trust fabric | supportive citations can help show that these are established adjacent problem spaces rather than newly invented contrasts | survey, standard, or systems paper representing those broader problem areas |
| `4. Demo Scenario` | metadata-enrichment walkthrough as the chosen witness scenario | a citation can help explain why a single end-to-end witness is acceptable as an explanatory specimen | methodology or artifact-demonstration source |
| `5. Fresh Clean Rerun` | reproducibility posture and clean-environment rerun framing | a supportive citation helps align the rerun narrative with reproducibility expectations | reproducibility guideline, artifact policy, or software engineering norms source |
| `6. Related Work` | bridge sentences that explain why adjacent lines are broader than this paper | some bridge sentences may need targeted citations beyond the subsection anchors if a final pass shows unsupported comparison language | the same primary sources already used in related work, plus any needed review article |
| `8. Conclusion` | framing the paper as a smallest working witness and bounded verification artifact | a concluding citation is optional but can reinforce that this framing follows established artifact or reproducibility practice | artifact-evaluation or methodology source |
