<!-- language-switch:start -->
<p>
  <a href="./README.md">
    <img src="https://img.shields.io/badge/%E8%8B%B1%E6%96%87-%E5%88%87%E6%8D%A2-0f172a?style=for-the-badge" alt="英文">
  </a>
  <a href="./README.zh-CN.md">
    <img src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E5%BD%93%E5%89%8D-1f883d?style=for-the-badge" alt="中文">
  </a>
</p>
<!-- language-switch:end -->

# 张斌

独立研究者，正在构建一套面向可验证自治系统的五层架构。

## 身份定位

我是一名独立研究者，主要研究面向持续增强自治人工智能系统的协议、治理与验证架构。当前主线是数字生物圈架构，它是一套覆盖人格、交互、治理、执行完整性和审计的五层体系。

这项工作并不围绕单一智能体产品展开。重点在于可持续的架构层、协议边界、运行时控制、可回放验证的完整性，以及适合审计的证据体系。

## 核心理论入口

- [`digital-biosphere-architecture`](https://github.com/joy7758/digital-biosphere-architecture) 是当前五层体系唯一的规范解释入口。

## 个人介绍页

- [个人介绍文案页](./docs/profile-bio-finalists.zh-CN.md)

## 核心层仓库

### 人格对象协议

仓库：[`persona-object-protocol`](https://github.com/joy7758/persona-object-protocol)

负责人格可移植性与人格对象结构，不负责治理、执行或审计。

### 智能体意图协议

仓库：[`agent-intent-protocol`](https://github.com/joy7758/agent-intent-protocol)

负责意图、动作与结果对象之间的交互语义，不负责传输、治理或基准测试。

### 令牌治理器

仓库：[`token-governor`](https://github.com/joy7758/token-governor)

负责运行时治理、策略检查与预算约束决策控制，不负责架构总览、基准套件或审计平面。

### 执行完整性内核

仓库：[`fdo-kernel-mvk`](https://github.com/joy7758/fdo-kernel-mvk)

负责可回放验证的执行完整性与运行时真值界面，不负责策略治理或执行后审计。

### 审计层

仓库：[`aro-audit`](https://github.com/joy7758/aro-audit)

负责执行后的审查、验证、导出与审计控制平面输出，不负责理论总览、基准套件或运行时治理实现。

## 支撑补充层

- [`agent-evidence`](https://github.com/joy7758/agent-evidence) 提供语义化证据底座与开发接口。
- [`agent-object-protocol`](https://github.com/joy7758/agent-object-protocol) 提供相邻互操作协议与补充协议工作。

较薄的适配器与特定实现集成不会放在首页入口中。

## 演示与评测

- [`verifiable-agent-demo`](https://github.com/joy7758/verifiable-agent-demo) 是贯穿整套体系的引导演示入口，不是规范理论入口，也不是规范运行时实现。
- [`agent-governance-benchmark`](https://github.com/joy7758/agent-governance-benchmark) 是场景与指标的评测入口，不是规范理论入口，也不是规范运行时实现。

## 历史谱系

- [`pFDO-Specification`](https://github.com/joy7758/pFDO-Specification) 是更早期 DPP 工作的历史背景，不属于当前核心体系。
- [`redrock-opendpp-core`](https://github.com/joy7758/redrock-opendpp-core) 是更早期 DPP 实现路线的前序工作，不属于当前核心体系。
- [`MCP-Legal-China`](https://github.com/joy7758/MCP-Legal-China) 是相关法律与工具方向的历史背景，不属于当前核心体系。
- [`Kinetic-Robotics-FDO-Sovereignty`](https://github.com/joy7758/Kinetic-Robotics-FDO-Sovereignty) 是主权与 K-RFS 探索方向的历史背景，不属于当前核心体系。
- [`AASP-Core`](https://github.com/joy7758/AASP-Core) 是更早期谱系仓库，不属于当前核心体系。
- [`ISAS-Core`](https://github.com/joy7758/ISAS-Core) 是更早期谱系仓库，不属于当前核心体系。
- [`edo-architecture-index`](https://github.com/joy7758/edo-architecture-index) 是历史索引材料，不属于当前核心体系。

## 五层映射

```mermaid
flowchart LR
    Persona["人格层"] --> Interaction["交互层"]
    Interaction --> Governance["治理层"]
    Governance --> Execution["执行完整性层"]
    Execution --> Audit["审计层"]
```

| 层级 | 仓库 |
| --- | --- |
| 人格层 | `persona-object-protocol` |
| 交互层 | `agent-intent-protocol` |
| 治理层 | `token-governor` |
| 执行完整性层 | `fdo-kernel-mvk` |
| 审计层 | `aro-audit` |

支撑证据底座：`agent-evidence`

演示入口：`verifiable-agent-demo`

## 研究方向

- 协议化数字对象
- 运行时治理
- 可回放验证的执行完整性
- 面向审查与审计的证据体系

## 身份与链接

- [ORCID](https://orcid.org/0009-0002-8861-1481)
- [digital-biosphere-architecture](https://github.com/joy7758/digital-biosphere-architecture)
- [persona-object-protocol](https://github.com/joy7758/persona-object-protocol)
- [agent-intent-protocol](https://github.com/joy7758/agent-intent-protocol)
- [token-governor](https://github.com/joy7758/token-governor)
- [fdo-kernel-mvk](https://github.com/joy7758/fdo-kernel-mvk)
- [aro-audit](https://github.com/joy7758/aro-audit)

## 当前状态

- 公开研究界面
- 五层体系仍在持续整合中
- 历史仓库作为谱系保留，不再作为主入口

<!-- profile-render-refresh -->
<!-- render-refresh: 20260323T000000Z -->
