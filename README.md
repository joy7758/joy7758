# 张斌 / Bin Zhang

让 AI Agent 的每一步都可记录、可验证、可复核。<br>
I build auditable AI agent workflows.

Independent research on governable, verifiable AI agents for FDO / dataspace environments.

我做的工具，重点不是让 AI 多回答一句，而是让别人能检查 AI 到底做过什么。

English: I build tools that help people verify what AI systems actually did.

## 我是做什么的

我聚焦可信 AI / Trustworthy AI、Agent Evidence、LangChain / LangGraph 工作流，以及 FDO Operation Evidence。

我的工作不是让模型回答得更像人，而是把 AI 从“能回答的工具”升级为“可控、可追踪、可审计、可交付的研究与业务流程”。

我关注的是 Agent 执行之后还能留下什么：结构化 evidence、hash、schema、validator、audit trail、review result，以及可以被技术团队复核的最小闭环。

## 代表项目：Execution Evidence Bridge

**一句话：MVK 证明 AI 做过什么；Agent Evidence 把这些证明打包并验证；Verifiable Agent Demo 给审阅者一条最短的演示路径。**

English: MVK proves what happened; Agent Evidence packages and verifies the proof; Verifiable Agent Demo gives reviewers the shortest walkthrough across the stack.

我做了一条可以实际跑通的 AI Agent 执行证据链。  
它解决的问题很简单：AI 系统执行完之后，别人能不能检查它到底做了什么、有没有被改过、证据能不能被带走复核。

这条链分成几层：

- [`fdo-kernel-mvk`](https://github.com/joy7758/fdo-kernel-mvk)：负责证明执行过程。它验证确定性执行、重放结果、checksum/checkpoint 完整性和篡改检测。
- [`agent-evidence`](https://github.com/joy7758/agent-evidence)：负责把证明变成可交付证据。它支持离线验证、receipt、signed export 和 review pack。
- [`verifiable-agent-demo`](https://github.com/joy7758/verifiable-agent-demo)：给审阅者一条最短的演示路径，不需要先读完整架构。
- [`digital-biosphere-architecture`](https://github.com/joy7758/digital-biosphere-architecture)：说明整个架构关系和证据流转路径。

证据路径：

```text
MVK execution
-> audit_bundle.json
-> AEP-compatible bundle
-> offline verification
-> signed export / review pack workflows
-> guided demo
```

建议从这里开始看：

- [一页式审阅者说明](https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/briefs/execution-evidence-bridge-one-pager.md)
- [架构桥接地图](https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/execution-evidence-bridge-map.md)
- [面向审阅者的说明](https://github.com/joy7758/digital-biosphere-architecture/blob/main/docs/announcements/execution-evidence-bridge.md)

这个项目展示了：

- 如何生成确定性的执行记录
- 如何做 replay / integrity verification
- 如何发现 audit bundle 是否被篡改
- 如何把 MVK 证明导出成 AEP-compatible evidence bundle
- 如何做离线验证
- 如何给审阅者一条能跑通的演示路径

边界说明：这不是法律意义上的不可抵赖，不是合规认证，也不是官方 FDO 标准采纳声明。

## Main navigation

- Evidence entry -> [agent-evidence](https://github.com/joy7758/agent-evidence)
- Walkthrough demo -> [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo)
- Architecture hub -> [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture)
- Governance layer -> [token-governor](https://github.com/joy7758/token-governor)
- Audit plane -> [aro-audit](https://github.com/joy7758/aro-audit)

## 我能解决什么问题

- 让企业 AI / Agent 工作流留下结构化证据，而不是只剩聊天记录或零散日志
- 让 LangChain / LangGraph 流程更适合高责任、可审计场景
- 让研究流程中的选题、写作、审稿、复核可追踪、可回放、可交付
- 帮团队把 ChatGPT / Gemini 从工具使用升级为工作流和智能体试点
- 把 agent trace、policy reference、validator、audit receipt 组织成 HR 和技术经理都能看懂的项目交付物

## 先看这 5 个仓库

1. [agent-evidence](https://github.com/joy7758/agent-evidence) — 把 Agent / service operation 转换成可验证 evidence object，包含 profile、schema、validator、examples 和 demo。
2. [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo) — 一个最小可运行演示，展示从 intent 到 trace、evidence bundle、replay verdict、audit receipt 的闭环。
3. [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) — 可信 AI / Agent Evidence 的架构总图，用来解释项目之间如何组成一条工作流。
4. [token-governor](https://github.com/joy7758/token-governor) — 面向 Agent 运行前的预算、策略、fallback 和风险治理设计。
5. [aro-audit](https://github.com/joy7758/aro-audit) — 面向执行后的 receipt 生成、验证、review 和 conformance 检查。

## 当前重点

- `FDO_OPERATION_EVIDENCE_PROFILE_V0_1`
- `agent-evidence` validator / schema / registration pack
- FDO Testbed 最小注册演示
- ResearchFlow-Agent v0.1：面向论文与研究流程的多角色 Agent 工作流

## 技术关键词

Trustworthy AI · Agent Evidence · LangChain · LangGraph · Tool Calling · Multi-Agent Workflow · Audit Trail · JSON Schema · Validator · FDO Operation Evidence · AI Governance · Research Workflow

## English Summary

I work on Trustworthy AI, Agent Evidence, and auditable AI workflow design.

My focus is not only making agents useful, but making their execution traceable, reviewable, and verifiable.

The main project line connects LangChain / LangGraph workflows, structured evidence objects, JSON Schema validation, audit receipts, and FDO-style operation evidence.

For hiring and collaboration, start with `agent-evidence` and `verifiable-agent-demo`: they show the runnable evidence path before the broader architecture.

## Historical / lineage

- [persona-object-protocol](https://github.com/joy7758/persona-object-protocol)
- [agent-intent-protocol](https://github.com/joy7758/agent-intent-protocol)
- [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk)

## Contact

Email: 35353456@qq.com<br>
GitHub: [github.com/joy7758](https://github.com/joy7758)<br>
ORCID: [0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
