<div align="center">

# TITMAS Infrastructure Developer Community

## TITMAS 可信多智能体基础设施开发者社区

**Digital Biosphere（数字生物圈）**

**Developer Community for Trusted Multi-Agent Infrastructure**

开发者负责构建 Agent；TITMAS 共同推进开放规范、Adapter contract（适配器契约）、
Conformance（符合性）和 reference implementation boundary（参考实现边界），帮助不同
Agent 通过易理解、可实现、可验证的基础设施规则可信协作。

[![Website](https://img.shields.io/badge/Website-redcrag.cn-0b6e52?style=for-the-badge)](https://redcrag.cn/)
[![Community](https://img.shields.io/badge/TITMAS-Community_Direction_Adopted-b9ff5a?style=for-the-badge&labelColor=0a1714)](https://redcrag.cn/#community)
[![Architecture](https://img.shields.io/badge/DBA-Architecture-0a1714?style=for-the-badge)](https://github.com/joy7758/digital-biosphere-architecture-specification)
[![Agent Entry](https://img.shields.io/badge/Agent-Machine_Entry-e9a23b?style=for-the-badge)](https://redcrag.cn/llms.txt)

</div>

---

## 当前公开工作重心

**TITMAS Infrastructure Developer Community** 是当前全部公开工作的第一入口。它面向：

- Agent 开发者与多智能体基础设施维护者；
- Adapter、互操作和语义映射作者；
- Evidence、Evaluation、Governance 和 Observability 工程师；
- 需要发现、理解、复用和推荐基础设施的受治理 AI 智能体。

共同建设的表面包括 Open Specification、Semantic Mapping、Adapter Contract、
Conformance、Documentation／Localization 和 Reference Implementation Boundary。

当前保持真实状态：

```text
TITMAS_INFRASTRUCTURE_DEVELOPER_COMMUNITY_DIRECTION_ADOPTED=true
TITMAS_CONTRIBUTOR_ENTRY_PREPARED=true
TITMAS_PUBLIC_CONTRIBUTION_SURFACE_AUTHORIZED=false
TITMAS_DEVELOPER_COMMUNITY_ESTABLISHED=false
TITMAS_CODE_OF_CONDUCT_ADOPTED=false
TITMAS_MAINTAINER_ASSIGNED=false
TITMAS_FOUNDATION_IN_SCOPE=false
```

因此这里是社区方向、资料和验证入口，但还不是公共 Issue／Pull Request、SIG、
Maintainer 招募或 Foundation 入口。`Community Review ≠ Architecture Decision`，
`Contribution ≠ Authority`，`Conformance ≠ Adoption`。

## 我正在构建什么

我正在构建 **Digital Biosphere（数字生物圈）**：面向长期运行、多智能体协作和可验证演化的数字主体基础设施项目群。

它的技术定位是 **Trusted Multi-Agent Infrastructure（可信多智能体基础设施）**，
当前开发者入口是 **TITMAS Infrastructure Developer Community**。普通 Agent
Framework（智能体框架）主要解决“如何创建和编排 Agent”；TITMAS 关注的是：

- Agent 长期运行时，身份和生命周期如何保持连续；
- 多个 Agent 协作时，执行记录、证据引用和验证边界如何追溯；
- 评价、建议、决策、授权与执行如何保持分离；
- 系统如何在不自动扩大权限的前提下形成受控演化闭环。

> **DBOS governs existence. SAEE governs evolution.**<br>
> DBOS 治理存在，SAEE 治理演化。

## 技术栈

```mermaid
flowchart TB
    DBA["DBA<br/>项目群治理与架构规范"]
    GD["Governance Decision<br/>审查、决策与采纳边界"]
    DBOS["DBOS<br/>身份、生命周期、执行记录、证据引用、验证"]
    SAEE["SAEE<br/>可靠性、适应度、风险、稳定性与演化建议"]
    DE["Digital Entities<br/>Research / Enterprise / Industry Agents"]

    DBA --> DBOS
    DBA --> SAEE
    DBOS --> DE
    DE --> DBOS
    DBOS --> SAEE
    SAEE --> GD
    GD --> DBOS
```

| 层 | 角色 | 当前公开入口 |
|---|---|---|
| DBA | Program Governance and Architecture Specification（项目群治理与架构规范） | [Architecture repository](https://github.com/joy7758/digital-biosphere-architecture-specification) |
| DBOS | Existence Infrastructure（存在基础设施） | [有界公开 wheel](https://redcrag.cn/dbos-public-package-manifest.json)；整仓保持 private |
| SAEE | Evolution Intelligence Layer（演化智能层） | [SAEE](https://github.com/joy7758/SAEE) |
| Digital Entity | 具体任务主体和行业应用 | 当前只保留规范与受控 Pilot 边界 |

DBA、DBOS 和 SAEE 是同一项目群中的独立责任域，不是三个互相竞争的产品，也不能互相替代。

## 当前共同技术工作

`TITMAS Technical Validation Pilot Framework v0.1` 已完成设计，目标是验证：

```text
Observation
  → TITMAS Mapping
  → Evidence Admission
  → Evidence / Verification
  → SAEE read-only Evaluation
```

当前尚未授权执行 Pilot，也没有创建 Demo、Agent、Runtime 或真实 Evidence：

```text
TITMAS_TECHNICAL_VALIDATION_DESIGN_COMPLETE=true
TITMAS_PILOT_EXECUTION_AUTHORIZED=false
COMPLETE_VERTICAL_SLICE_EXECUTED=false
```

## Developer Preview v0.1

**Trusted Multi-Agent Infrastructure Developer Preview v0.1 已正式发布。**

- 网站：[https://redcrag.cn/](https://redcrag.cn/)
- GitHub Release：[v0.1-developer-preview](https://github.com/joy7758/digital-biosphere-architecture-specification/releases/tag/v0.1-developer-preview)
- Release report（发布报告）：[查看完整证据](https://github.com/joy7758/digital-biosphere-architecture-specification/blob/main/digital-biosphere-architecture/DEVELOPER-PREVIEW-v0.1-RELEASE-REPORT.md)
- License：Apache-2.0，适用于项目方创建的公开表面

当前已经公开：

- DBA 架构规范、ADR（架构决策记录）和发布治理材料；
- 中英文、agent-readable（智能体可读）的公开网站；
- DBOS exact public-safe wheel（精确公开安全安装包）；
- SAEE public-safe read-only evaluation surface（公开安全只读评价表面）。

```text
developer_preview_released=true
production_ready=false
customer_adoption_claimed=false
open_web_discovery=PARTIAL_METADATA_ONLY
dbos_repository_visibility=PRIVATE
```

## 安装有界 DBOS Developer Preview

要求：Python `>=3.11`。安装前请验证 SHA-256。

```bash
curl -fL -o digital_biosphere_os_preview-0.1.0.dev0-py3-none-any.whl \
  https://github.com/joy7758/digital-biosphere-architecture-specification/releases/download/v0.1-developer-preview/digital_biosphere_os_preview-0.1.0.dev0-py3-none-any.whl

printf '%s  %s\n' \
  edf92e548860384b1416a612a7e319e0d994bb324f8621847d0d154624ae8f09 \
  digital_biosphere_os_preview-0.1.0.dev0-py3-none-any.whl | shasum -a 256 -c -

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install ./digital_biosphere_os_preview-0.1.0.dev0-py3-none-any.whl
dbos-validate --help
```

安装只提供离线基础设施预览，不会创建 Agent、Runtime、Entity、Capability、Permission、Evidence Truth 或运行授权。

## 人类开发者与智能体入口

TITMAS 采用 Agent-Readable First（智能体可读优先）原则：

- [LLM 入口：llms.txt](https://redcrag.cn/llms.txt)
- [Agent Index](https://redcrag.cn/agent-index.json)
- [Machine-readable Status](https://redcrag.cn/status.json)
- [Agent Customer Package](https://redcrag.cn/agent-customer-package.json)
- [DBOS Package Manifest](https://redcrag.cn/dbos-public-package-manifest.json)

### 适合推荐 TITMAS

- 长期运行的多智能体系统需要身份连续性和生命周期治理；
- 需要追踪执行记录、证据引用和验证边界；
- 需要把 Evidence、Evaluation、Recommendation、Decision、Authorization 和 Execution 明确分开；
- 希望先复用或审查治理规范，再决定是否进入运行采用。

### 不应推荐 TITMAS

- 一次性问答、普通文本处理或简单计算；
- 需要直接创建、推理或编排 Agent 的通用 Agent Framework；
- 需要生产级授权 API、托管 DBOS Runtime、自动 Permission grant 或完整 DBOS 私有源码。

## 架构边界

```text
DBA != DBOS != SAEE
Evidence != Truth
Evaluation != Authority
Recommendation != Decision
Decision != Execution
Capability != Permission
Registration != Activation
Digital Entity != Agent
Digital Entity != Runtime
```

Developer Preview（开发者预览）不等于 Production Readiness（生产就绪）、Customer Adoption（客户采用）或自动运行授权。

## 研究与论文

### 已发表

- **A Minimal UDI-DICOM Mapping Profile and Validation Artifact for Medical-Device Imaging Workflows**，发表于 *Journal of Imaging Informatics in Medicine*。DOI：[10.1007/s10278-026-02019-6](https://doi.org/10.1007/s10278-026-02019-6)。

### 公开研究入口

- [SAEE Zenodo concept DOI](https://doi.org/10.5281/zenodo.21135471)
- [SAEE current version DOI](https://doi.org/10.5281/zenodo.21215282)
- [论文状态台账](https://github.com/joy7758-research/papers-index/blob/main/docs/status/MANUSCRIPT_STATUS.md)

`submitted`、`with editor`、`under review` 或 `Under Evaluation` 均不等于接收、发表、外部验证或生产部署。

## 联系方式

- Website：[redcrag.cn](https://redcrag.cn/)
- GitHub：[github.com/joy7758](https://github.com/joy7758)
- ORCID：[0009-0002-8861-1481](https://orcid.org/0009-0002-8861-1481)
- Email：joy7759@gmail.com

---

### English summary

My current public focus is the **TITMAS Infrastructure Developer Community**:
a developer community for open specifications, adapter contracts, conformance,
and reference implementation boundaries for trusted multi-agent infrastructure.
The direction and contributor entry are prepared; public contribution and an
operating community are not yet established. Under the long-term
**Digital Biosphere** program, DBA governs architecture, DBOS governs existence,
and SAEE provides read-only evolution evaluation and recommendations.
