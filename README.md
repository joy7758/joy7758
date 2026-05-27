# 张斌 / Bin Zhang

我研究智能体执行证据与操作问责配置文件。  
I work on Agent Evidence / Operation Accountability Profile.

重点不是让 AI（Artificial Intelligence，人工智能）多回答一句，而是让智能体执行之后留下可验证、可复核、可审计的证据。

My focus is not only making agents useful, but making their execution traceable, reviewable, and verifiable after work has been done.

## 最新论文 / Recent Publication

- **A Minimal UDI-DICOM Mapping Profile and Validation Artifact for Medical-Device Imaging Workflows** has been published online in *Journal of Imaging Informatics in Medicine*. DOI: [10.1007/s10278-026-02019-6](https://doi.org/10.1007/s10278-026-02019-6). Springer Nature SharedIt view-only link: [https://rdcu.be/fk6Qd](https://rdcu.be/fk6Qd).

## 主线入口 / Mainline

这条主线关注智能体执行后的证据闭环：执行记录、校验、回放、receipt、review pack，以及跨仓库可复核的最小路径。

This line is about evidence left by agent execution: records, validation, replay, receipts, review packs, and a short cross-repository verification path.

1. [agent-evidence](https://github.com/joy7758/agent-evidence) - Agent Evidence / Operation Accountability Profile 的核心证据对象、schema、validator 和示例。
2. [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk) - MVK（Minimal Verification Kernel，最小验证内核），用于确定性执行、checkpoint、checksum 和篡改检测。
3. [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo) - 面向审阅者的最小可运行演示，展示 intent、trace、evidence bundle、replay verdict 和 audit receipt。
4. [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) - 架构 hub，说明主线仓之间的证据流转、AI discovery surface 和引用路径。
5. [token-governor](https://github.com/joy7758/token-governor) - 智能体运行前的预算、策略、fallback 和风险治理。
6. [aro-audit](https://github.com/joy7758/aro-audit) - 智能体执行后的 receipt 生成、验证、review 和 conformance 检查。

## 快速理解 / Short Summary

```text
agent execution
-> structured evidence
-> validation / replay
-> audit receipt
-> review pack
-> accountable operation profile
```

我关心的是：当一个智能体完成任务后，其他人能不能检查它到底做了什么、证据有没有被改过、结果能不能离线复核。

The question I work on is: after an agent finishes a task, can another person inspect what happened, detect tampering, and review the evidence offline?

## 场景试点与论文产物 / Pilots and Paper Artifacts

- [redcrag-aep](https://github.com/joy7758/redcrag-aep) - RedCrag 场景下的 Agent Evidence Profile（智能体证据配置文件）试点。
- [agent-accountability-evidence-layer](https://github.com/joy7758/agent-accountability-evidence-layer) - 操作问责证据层的论文与实验材料。
- [pd-oap-icsme2026-artifact](https://github.com/joy7758/pd-oap-icsme2026-artifact) - ICSME（International Conference on Software Maintenance and Evolution，软件维护与演化国际会议）2026 相关产物仓。

## 给读者和智能体 / For Readers and Agents

这个 profile 是公开身份和项目路由入口，不是执行规则仓。更轻量的导航上下文见 [PROFILE_CONTEXT.md](PROFILE_CONTEXT.md)。

- 从 [agent-evidence](https://github.com/joy7758/agent-evidence) 理解规范证据对象、schema 和 validator。
- 从 [verifiable-agent-demo](https://github.com/joy7758/verifiable-agent-demo) 走最短可运行审阅路径。
- 从 [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture) 看架构地图、跨仓引用和历史治理索引。

## 历史与侧线 / Historical and Side Lines

部分早期实验、fork（派生镜像）和侧线仓库正在通过“回收站”索引整理。该索引不是删除声明，只记录迁移、归档候选、观察和人工复核状态。

Some early experiments, forks, and side-line repositories are being organized behind a recycle-bin index. The index is not a deletion statement; it records migration, archive-candidate, observation, and human-review status.

- [digital-biosphere-architecture/回收站](https://github.com/joy7758/digital-biosphere-architecture/tree/main/%E5%9B%9E%E6%94%B6%E7%AB%99)

## Contact

Email: joy7759@gmail.com<br>
GitHub: [github.com/joy7758](https://github.com/joy7758)<br>
ORCID: [0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
