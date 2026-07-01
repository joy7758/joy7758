# External Citation Front Door - 2026-06-28

## Agent-readable status

- purpose: route external readers to the smallest problem-shaped public surface.
- status: local profile routing candidate, not pushed, not posted.
- current_truth_surface: local `joy7758` profile worktree only.
- current_profile_changes_public: false.
- do_not_report_as: published, released, posted, merged, externally cited, externally validated.
- publish_dependency: review this profile branch against the intended public profile branch before any push or PR.

## Why this exists

External readers do not need the full architecture first. They need one
problem, one repo, and one artifact they can copy, run, or cite. This profile
route compresses the public front door into four problem-shaped choices.

## Problem-to-entry routing

| External problem | First route | Public URL | Citation/reuse unit |
| --- | --- | --- | --- |
| Verify one agent tool call outside the original runtime | `verifiable-tool-invocation-flow` | `https://github.com/joy7758/verifiable-tool-invocation-flow` | guarded tool call -> signed receipt -> independent verifier |
| Review one post-execution receipt or conformance artifact | `aro-audit` | `https://github.com/joy7758/aro-audit` | receipt fixture -> verifier -> audit/review status |
| Reuse a persona object as framework-readable agent config | `persona-object-protocol` | `https://github.com/joy7758/persona-object-protocol` | persona object -> config export -> framework trial |
| Show a before/after artifact from a runnable agent workflow | `verifiable-agent-demo` | `https://github.com/joy7758/verifiable-agent-demo` | agent run -> evidence bundle -> audit JSON |

Machine-readable route manifest: `docs/external-citation-route-manifest.json`.

## Recommended share order

1. Share `verifiable-tool-invocation-flow` when the other party asks about
   tool calls, transaction logs, callbacks, auditability, or MCP-compatible
   verification.
2. Share `aro-audit` when the other party asks about post-execution review,
   conformance, or receipt verification as a separate audit layer.
3. Share `persona-object-protocol` when the other party asks about reusable
   roles, personas, agent YAML, or framework-neutral agent identity.
4. Share `verifiable-agent-demo` when the other party wants one runnable
   before/after artifact instead of an architecture discussion.

## Boundary

Use this file as routing metadata only. It does not claim:

- official LangChain, CrewAI, AutoGen, MCP, FDO, or standards-body adoption.
- legal non-repudiation.
- compliance certification.
- production forensic timestamping.
- semantic correctness of agent output.
- new external citations, replies, or validation for the local profile changes.

## Local gate

Before any public profile action, run:

```bash
cd path/to/joy7758
python3 scripts/check_external_citation_profile_surface.py
```

Expected output:

```text
PROFILE_EXTERNAL_CITATION_SURFACE_OK
```
