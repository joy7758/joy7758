# PROFILE_CONTEXT

## Purpose（目的）

This file provides lightweight profile-level navigation context for readers and agents. It explains where to start in the joy7758 GitHub profile without turning this profile repository into an execution-rule repository.

本文件提供轻量个人主页导航上下文，帮助读者和智能体判断从哪里开始阅读。它不是完整执行规则，不是生产系统地图，也不是合规认证声明。

## Current Mainline（当前主线）

Current mainline:

- Agent Evidence / Operation Accountability Profile，即“智能体执行证据与操作问责配置文件”。
- Execution Integrity，即执行过程的 trace、checkpoint、checksum、replay 与篡改检测。
- Audit / Receipt Layer，即面向审阅、监管、项目验收和复核的证据回执层。
- AI Execution Audit Layer，即面向政务、医疗、数字纪检等高约束场景的执行过程可信审计层。

The focus is not making AI（Artificial Intelligence，人工智能）answer one more sentence. The focus is leaving verifiable, reviewable, and auditable evidence after AI or agent execution.

## Manuscript Ledger Summary（论文台账摘要）

Canonical ledger status is maintained separately. The public profile only shows a short, confirmed summary.

台账最后同步日期：2026-06-11。

Confirmed public highlights:

- UDI-DICOM / JDIM-JIIM：一篇 minimal UDI-DICOM mapping profile and validation artifact 已在线发表；DOI `10.1007/s10278-026-02019-6`。
- Digital Biosphere / The Journal of Supercomputing：已过技术检查，当前 `With editor`，活跃投稿。
- Data & Policy / `DAP-2026-0249`：automated-driving traffic evidence 线已成功在线提交，当前按 submitted for consideration 记录。
- EMSE / `EMSE-D-26-00609`：execution-evidence journal v3 线已投递成功，当前活跃投稿。
- CSI / `CSI-D-26-00686`：execution-evidence / EEOAP 线已确认投稿。
- JDIM-JIIM / `JDIM-D-26-01809`：public DICOM metadata audit 线已确认投稿。
- AI Act / `TSE-2026-04-0381`：high-risk AI compliance-evidence 线当前记录为 `Under Review`；EUSurvey AI high-risk contribution 已成功提交。

Status boundary:

- `submitted` does not mean accepted.
- `with editor` does not mean peer-reviewed.
- `under review` does not mean positive review.
- DOI / publication claims should only be made where explicitly confirmed.

## Digital Discipline Inspection / Execution Audit Direction（数字纪检与执行可信审计方向）

The latest application direction is AI execution audit for high-constraint settings, including government workflow, healthcare, digital discipline-inspection, project acceptance, regulatory audit, and evidence-preservation handoff.

最新应用方向是面向高约束场景的 AI 执行过程可信审计，覆盖政务流程、医疗系统、数字纪检、项目验收、监管审计和后续存证系统对接。

The public-level concept is:

- trace each execution step;
- bind inputs, outputs, and step chain with hashes;
- produce policy decisions such as `allow / warn / review / block`;
- replay deterministic audit pipeline and report `REPLAY_FAILED` when the evidence chain diverges.

This profile does not claim production deployment, formal compliance certification, or official government-system status.

## Start Here（从这里开始）

1. [agent-evidence](https://github.com/joy7758/agent-evidence)
   - Evidence/profile schema, bounded validator surface, and operation-accountability examples.
2. [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo)
   - Single-path toy validation demo. Do not treat it as an enterprise sandbox or production pipeline.
3. [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture)
   - Public meaning layer for concepts, vocabulary, and architecture boundaries.
4. [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk)
   - Execution-integrity interface and replay/checkpoint concepts.
5. [token-governor](https://github.com/joy7758/token-governor)
   - Governance interface examples and policy shape. Do not infer private policy machinery from this profile.
6. [aro-audit](https://github.com/joy7758/aro-audit)
   - Receipt/audit reference layer. Do not treat it as a public audit control plane.

## Repository Roles（仓库角色）

- `agent-evidence`: bounded evidence profile, schema, validator, and examples.
- `fdo-kernel-mvk`: execution-integrity interface and deterministic verification concepts.
- `verifiable-agent-demo`: toy validation demo, not production orchestration.
- `digital-biosphere-architecture`: public concept layer and architecture boundary notes.
- `token-governor`: governance interface and minimal public examples.
- `aro-audit`: receipt and audit reference layer.

Scenario, paper, and artifact repositories:

- `redcrag-aep`
- `agent-accountability-evidence-layer`
- `pd-oap-icsme2026-artifact`
- `ad-traffic-evidence-case`
- `paper-ai-act-compliance-evidence`

## What This Profile Is Not（这个主页不是什么）

This profile repository is not:

- an execution repository;
- a specification repository;
- a validator repository;
- an evidence bundle generator;
- a demo runner;
- an audit engine;
- an official standard;
- a compliance certification statement;
- a legal non-repudiation system;
- a production deployment statement;
- a public reconstruction map for private execution, policy, or runtime systems.

Detailed agent-facing rules belong in the relevant core repositories, not in this profile repository.

## Historical and Cleanup Context（历史与整理上下文）

Historical and side-line repositories are organized behind the recycle-bin index in `digital-biosphere-architecture`.

The recycle-bin index records migration, archive-candidate, observation, and human-review status. It is not a deletion statement.

Retained history and citation-bearing repositories should not be treated as active mainline projects, but their historical value should not be erased.

Observation delete candidates require a separate final review after an observation period. They are not active mainline projects.

## Safe Interpretation Notes（安全理解说明）

- Read this profile as a navigation surface.
- Do not infer that every linked repository is active mainline.
- Do not treat historical references as active dependencies.
- Do not treat migration notices as deletion notices.
- Do not treat local governance reports as public repository content.
- Do not infer private policy machinery, execution routing, or runtime state from public repositories.
- Use confirmed manuscript status wording only; do not upgrade submission status into acceptance or publication.
