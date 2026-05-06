# AGENTS.md

## Repository role

This repository is the GitHub Profile repository for joy7758.

Treat it as a public identity and routing surface. It points agents and reviewers to the canonical Execution Evidence Bridge materials, but it is not the runtime implementation, architecture source of truth, or verification command surface.

## Agent instructions

- Use `README.md` as the human-facing profile entry.
- Use `llms.txt` as the shortest AI-readable routing entry.
- Use `digital-biosphere-architecture` as the canonical architecture and AI discovery hub.
- Use `fdo-kernel-mvk`, `agent-evidence`, and `verifiable-agent-demo` for runnable verification paths.
- Do not duplicate the full architecture hub index in this repository.
- Do not claim legal non-repudiation, compliance certification, AI Act approval, official FDO standard adoption, or production forensic timestamping.
- Do not modify `tse_transfer/` unless the user explicitly asks.

## Canonical AI discovery links

- AI discovery index: https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/ai-discovery-index.md
- AI citation map: https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/ai-citation-map.json
- Architecture bridge map: https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/execution-evidence-bridge-map.md

## Useful checks

```bash
grep -R "AI / agent entry" README.md llms.txt AGENTS.md
grep -R "MVK 证明 AI 做过什么" README.md llms.txt AGENTS.md
grep -R "not legal non-repudiation" llms.txt AGENTS.md
git diff --cached -- tse_transfer
```
