# Problem And Scope

Purpose: Define the exact problem addressed by the artifact and make the paper boundary explicit.

## TODO

- [x] Describe the problem in bounded terms.
- [x] Enumerate supported scope and non-goals.
- [ ] Tighten venue-specific terminology if needed.

## Draft

The problem addressed by the current artifact is not "agent governance" in the
large. It is the narrower problem of producing one independently checkable
statement about one operation performed by an agent in an FDO-based setting.
The repository frames that statement around a few concrete questions: who
executed, what subject object was involved, what operation was invoked, which
policy and constraints governed the action, how input and output objects were
referenced, what evidence artifacts were emitted, and what validation path a
third party can apply.

This scope is intentionally compressed. The profile covers one statement, one
operation, and one bounded validation surface. The corresponding demo keeps the
scenario equally narrow: one metadata enrichment path over one client note
object under an explicit policy boundary. The example set is also controlled:
one valid profile instance and three invalid instances that each break one main
rule class.

Several common expansions are explicitly out of scope. The repository does not
attempt to define a general registry, a full governance platform, a full
cryptographic trust fabric, multi-agent orchestration semantics, or a complete
FDO interoperability layer. The paper should therefore avoid wording that
suggests end-to-end governance effectiveness, production adoption, or broad
operational assurance. Its proper scope is a minimal profile, a validator, a
demo, and bounded independent verification.
