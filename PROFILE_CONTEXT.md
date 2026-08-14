# 个人主页说明

## 主页定位

这是张斌的 GitHub 个人主页，也是公开项目的简明导航入口。

当前研究重点是可信自主 AI 系统基础设施，以及 DCELL（数字细胞）研究方向：让自主系统拥有清晰身份，留下可验证的执行证据，保存有用经验，并在边界明确的前提下演化。

这个主页只负责帮助人和智能体快速理解研究方向、找到项目和识别边界。它不是任何项目的最终事实依据，也不创建运行权限、发布授权或外部认可。

## 核心公开入口

1. [GitHub 个人主页](https://github.com/joy7758)——面向人的总入口。
2. [Verifiable Agent Demo](https://github.com/joy7758/verifiable-agent-demo)——有边界的智能体执行证据示例。
3. [SAEE](https://github.com/joy7758/SAEE)——智能体健康评估与候选修改评估实验。
4. [TITMAS Agent Action Gate](https://github.com/joy7758/titmas-agent-action-gate)——证据感知的行动契约与授权边界。
5. [Persona Object Protocol](https://github.com/joy7758/persona-object-protocol)——带版本的身份与人格对象能力。
6. [Digital Biosphere Architecture](https://github.com/joy7758/digital-biosphere-architecture-specification)——项目群治理与架构依据。
7. [RedCrag](https://redcrag.cn/)——面向公众的网站入口。

## 精选论文入口

1. 论文一：
   `A Minimal UDI-DICOM Mapping Profile and Validation Artifact for
   Medical-Device Imaging Workflows`
   - journal: `Journal of Imaging Informatics in Medicine`
   - status: `ONLINE_PUBLISHED`
   - DOI: `10.1007/s10278-026-02019-6`
   - public_url: `https://doi.org/10.1007/s10278-026-02019-6`
   - view_only_full_text: `https://rdcu.be/fk6Qd`
2. 论文二：
   `A Bounded Public DICOM Metadata Audit for UDI-DICOM Evidence Readiness in
   Medical Imaging Workflows`
   - journal: `Journal of Imaging Informatics in Medicine`
   - status: `ONLINE_PUBLISHED`
   - DOI: `10.1007/s10278-026-02164-y`
   - public_url: `https://doi.org/10.1007/s10278-026-02164-y`
   - published_online: `2026-07-29`

相关公开参考实现：[UDI-DICOM Evidence Validator](https://github.com/joy7758/udi-dicom-evidence-validator)。该实现不创建临床验证、监管批准、医疗诊断或医院部署结论。

## 已合并的外部 PR 入口

- `microsoft/agent-governance-toolkit#1319`：外部操作责任证据映射说明；`MERGED`；2026-04-22。
- `microsoft/agent-governance-toolkit#1370`：基于 `AuditService / AuditEntry` 的最小责任证据导出示例；`MERGED`；2026-04-24。
- `agentrust-io/ca2a#76`：无效委托签名的 `ACTION-008` 必须级一致性测试；`MERGED`；2026-08-03。
- `langchain-ai/docs#2991`：`langchain-pop` 集成文档；`MERGED`；2026-08-05。
- `langchain-ai/docs#2992`：`langchain-aro` 集成文档；`MERGED`；2026-08-05。
- `langchain-ai/docs#3130`：Agent Evidence 集成入口；`MERGED`；2026-08-06。

以上 PR 的“已合并”只证明对应贡献进入了外部仓库，不证明这些仓库正式采用了张斌的全部项目、协议、研究主张或产品。

## 项目之间的关系

- `DBA` 负责项目群治理与架构规范。
- `DBOS` 研究身份、生命周期、执行记录、证据引用和验证边界。
- `SAEE` 研究可靠性、健康状态、风险、稳定性和候选修改评估。
- `TITMAS` 保留为早期工程实验，不是 DCELL 的中央控制器。
- `DCELL` 是当前研究方向，不是已经完成的平台或产品。

这些名称属于同一长期研究脉络，但各自保留独立的责任范围和事实来源。

```text
DBA 不等于 DBOS，也不等于 SAEE
证据不等于事实
评估不等于授权
建议不等于决定
决定不等于执行
能力不等于权限
```

## 信息成熟度

- **已实现（`IMPLEMENTED`）：** 有代码、测试或 CI 直接支持的有限技术能力。
- **已有实验支持（`EXPERIMENTALLY_SUPPORTED`）：** 有实验支持某个有限结论，但还不能推广到所有场景。
- **原型（`PROTOTYPE`）：** 可以用来探索和验证方向的早期工程实现。
- **研究方向（`RESEARCH_DIRECTION`）：** 正在研究的问题，不代表能力已经完成。
- **未来假设（`FUTURE_HYPOTHESIS`）：** 仍需要公开实验、失败案例和可复现结果验证的设想。

## 对外表述边界

- Demo 跑通，不等于生产就绪。
- 测试或 CI 通过，不等于系统获得行动授权。
- 规范存在，不等于对应实现已经完成。
- 仓库公开，不等于外部已经采用。
- 论文处于投稿、编辑处理或评审阶段，不等于已经接收或发表。
- 论文已接收，不等于已经分配 DOI 或在线发表。
- 外部 PR 已合并，不等于上游正式采用整套项目、协议或研究结论。
- 私有扩展支持的完整路径，不能描述成只凭公开仓库即可独立复现。

## 研究责任与 AI 使用

AI 编码智能体可以参与实现和复核，但研究问题、实验设计、验收标准、架构决策、证据解释、失败分析和授权决定仍由人负责。

公开结论应尽量附带可复现材料、失败案例、决策记录、适用范围和已知限制。仓库版本、依赖、CI 或公开范围发生变化后，相关结论需要重新核对。
