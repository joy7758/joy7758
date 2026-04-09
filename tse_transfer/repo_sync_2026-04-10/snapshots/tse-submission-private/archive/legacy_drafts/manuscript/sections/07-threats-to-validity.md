# Threats To Validity

Purpose: Make the paper's current limits explicit and reviewer-facing.

## TODO

- [x] Record the main boundary threats.
- [ ] Revisit after any scope expansion.

## Draft

The most important validity threat is scope narrowness. The artifact validates
one profile for one statement shape and demonstrates one single-path metadata
enrichment scenario. This is appropriate for a minimal specimen, but it limits
how far the paper can generalize beyond the documented path.

A second threat is evaluation breadth. The repository documents one valid
example, three invalid examples, a single demo, and acceptance checks. These
materials are strong enough to support claims about internal coherence and
bounded verification behavior, but they do not support claims about large-scale
coverage, production reliability, or cross-framework deployment behavior.

A third threat is surrounding system coverage. The profile explicitly avoids
registry design, multi-agent orchestration, full FDO mapping, and a full
cryptographic trust fabric. Reviewers could reasonably ask whether the artifact
scales to those settings, but the current paper should answer that those
questions are deferred rather than solved.

A fourth threat is repository context. The public repository still contains
historical `Execution Evidence Object` and `Agent Evidence Profile` materials.
The status documentation separates those historical surfaces from the current
v0.1 path, but the manuscript should maintain that separation carefully to
avoid terminology drift.
