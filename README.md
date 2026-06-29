# 张斌 / Bin Zhang

我研究 AI 智能体执行证据、操作问责、执行完整性、审计回执，以及面向高约束场景的可复核证据层。

重点不是让 AI（Artificial Intelligence，人工智能）多回答一句，而是让智能体或 AI 系统完成任务后，留下可追踪、可复核、可审计的证据。

## 当前主线

- **Agent Evidence / Operation Accountability Profile**：智能体执行证据与操作问责配置文件。
- **Execution Integrity**：执行过程的 trace、checkpoint、checksum、replay 与篡改检测。
- **Audit / Receipt Layer**：面向审阅者、编辑、监管或项目验收的证据回执。
- **AI Execution Audit Layer**：面向政务、医疗、数字纪检等高约束场景的执行过程可信审计层。

这个 profile 是公开身份和项目路由入口，不是执行规则仓，也不是生产系统地图。

## 最新论文与论文台账摘要

GitHub 可读台账入口：

- [Manuscript status ledger](https://github.com/joy7758-research/papers-index/blob/main/docs/status/MANUSCRIPT_STATUS.md)
- [Research direction index](https://github.com/joy7758-research/papers-index/blob/main/docs/status/MANUSCRIPT_STATUS.md#%E7%A0%94%E7%A9%B6%E6%96%B9%E5%90%91%E7%B4%A2%E5%BC%95)

论文台账最后同步日期：**2026-06-29**。

### 已发表

- **A Minimal UDI-DICOM Mapping Profile and Validation Artifact for Medical-Device Imaging Workflows**，已在线发表于 *Journal of Imaging Informatics in Medicine*。DOI: [10.1007/s10278-026-02019-6](https://doi.org/10.1007/s10278-026-02019-6)。Springer Nature SharedIt view-only link: [https://rdcu.be/fk6Qd](https://rdcu.be/fk6Qd)。

### 当前活跃或可公开跟踪状态

- **Digital Biosphere / The Journal of Supercomputing**：已过技术检查，当前 `With editor`，活跃投稿。
- **Data & Policy / DAP-2026-0249**：`Computable Evidence Objects for Automated-Driving Traffic Events: A Human-Review Validator under Synthetic Evaluation` 已成功在线提交，当前按 submitted for consideration 记录。
- **Journal of Systems & Software / ECL execution IR**：`ECL: A Deterministic Cross-Runtime Execution IR with Replayable Semantics and Dependency Interface` 已由用户确认提交成功，当前为 `active_submission_pending_formal_confirmation`；`JSSOFTWARE-S-26-01977` 只作为 proof/build staging reference。
- **Software: Practice and Experience / 4563331**：`Practical experience building agent-evidence: a Python tool for validating AI agent operation evidence` 已成功提交并送达 editorial office，当前按 `submitted_to_editorial_office / active_submission` 记录。
- **Empirical Software Engineering / EMSE-D-26-00609**：`A Minimal Execution-Evidence Profile for Bounded Reviewability of Agentic Software Runs` 已投递成功，当前活跃投稿。
- **Computer Standards & Interfaces / CSI-D-26-00686**：execution-evidence / EEOAP 线稿件已确认投稿，当前按 submission received / being processed 记录。
- **Journal of Imaging Informatics in Medicine / JDIM-D-26-01809**：public DICOM metadata audit 线稿件已确认投稿，当前活跃投稿。
- **AI Act / TSE-2026-04-0381**：high-risk AI compliance-evidence 线当前记录为 `Under Review`；European Commission EUSurvey AI high-risk contribution 已成功提交。

近期拒稿 / 关闭 / 改投来路保留在台账的 `论文来路树` 和 `研究方向索引` 中，不在首页摘要中写作活跃状态。以上状态只按已确认台账口径展示。`submitted`、`submitted_to_editorial_office`、`with editor`、`under review` 不等于接收、录用、发表或 DOI。

## 最新应用方向：数字纪检与执行可信审计

最新应用线聚焦 **AI 执行过程可信审计 SDK / Execution Audit Layer**。

面向场景包括：政务流程、医疗系统、数字纪检、项目验收、监管审计与后续存证系统。核心问题是：AI 在运行时具体做了什么，输入输出是否被篡改，结果是否可复现，责任链是否可验收。

当前抽象能力包括：

- `trace.jsonl`：记录执行步骤、输入、输出和时间。
- `hash_chain.json`：为输入、输出和步骤链生成 SHA256 hash chain。
- `policy_decision.json`：输出 `allow / warn / review / block` 与人工复核标记。
- `replay_report.json`：回放确定性审计管线，发现不一致时返回 `REPLAY_FAILED`。

该方向目前作为执行可信审计层和应用场景说明展示，不在本 profile 中声明为生产部署、合规认证或正式政务系统。

## 公开仓库导航

请把以下入口理解为轻量导航，不要把它们拼成公开可复刻的生产执行链。

1. [agent-evidence](https://github.com/joy7758/agent-evidence) - 智能体执行证据与操作问责的 profile、schema、validator 和 bounded reference surface。
2. [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo) - 单路径 toy validation demo，不是 enterprise sandbox 或 production pipeline。
3. [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) - public meaning layer，提供概念、词汇和架构边界。
4. [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk) - execution-integrity interface 与 replay/checkpoint 概念层。
5. [token-governor](https://github.com/joy7758/token-governor) - governance interface、policy shape 和最小公开示例。
6. [aro-audit](https://github.com/joy7758/aro-audit) - receipt / audit reference layer，不是公开审计控制面。

## 给读者和智能体

更轻量的导航上下文见 [PROFILE_CONTEXT.md](PROFILE_CONTEXT.md)。

阅读顺序建议：

1. 先看本 profile 的研究主线和论文台账摘要。
2. 再看 `agent-evidence` 的 evidence/profile 公开接口。
3. 需要理解架构边界时，再看 `digital-biosphere-architecture`。
4. 不要从 profile 反推出生产执行系统、私有策略引擎、运行时状态或完整闭环实现。

## 历史与侧线

部分早期实验、fork（派生镜像）和侧线仓库正在通过“回收站”索引整理。该索引不是删除声明，只记录迁移、归档候选、观察和人工复核状态。

- [digital-biosphere-architecture/回收站](https://github.com/joy7758/digital-biosphere-architecture/tree/main/%E5%9B%9E%E6%94%B6%E7%AB%99)

## Contact

Email: joy7759@gmail.com<br>
GitHub: [github.com/joy7758](https://github.com/joy7758)<br>
ORCID: [0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
