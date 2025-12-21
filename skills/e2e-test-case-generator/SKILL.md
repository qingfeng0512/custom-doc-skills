---
name: E2E测试案例生成器
description: 基于业务描述智能生成E2E自动化测试案例和断言，支持全链路测试平台的案例创建、执行和验证。使用AI意图分析技术理解业务场景，自动匹配模板生成标准化的测试案例数据，并与MCP服务无缝集成实现完整的测试流程自动化。
---

# E2E测试案例生成器

## 快速开始

### 核心功能

1. **智能意图分析** - 使用AI模型分析业务描述，提取关键信息
2. **模板匹配** - 根据业务类型智能匹配对应的案例模板
3. **案例生成** - 自动生成标准化的案例信息和断言信息JSON
4. **MCP集成** - 无缝集成e2e-mcp-server完成案例保存和执行
5. **流程验证** - 端到端的案例执行和结果验证

### 使用场景

- **业务测试案例生成**: 从业务描述快速生成专业测试用例
- **测试流程自动化**: 完整的案例创建→保存→执行→验证流程
- **多业务类型支持**: 支持支付、转账、查询、退款等全业务范围
- **标准化测试**: 确保测试案例的一致性和规范性

## 功能详解

### 1. 意图分析

使用AI模型（MiniMax-M2）分析业务描述，提取：
- 业务类型和子类型
- 参与者信息（支付机构、银行、用户等）
- 流程步骤（发起、受理、处理、返回等）
- 关键参数（金额、时间、状态等）
- 成功标准和风险点

### 2. 模板匹配

- **智能匹配**: 基于业务类型、参与者、流程步骤的多维度匹配
- **置信度评分**: 为每个模板计算匹配分数，选择最佳匹配
- **模板管理**: 支持按业务类型组织的模板库
- **参数化**: 动态替换模板中的变量参数

### 3. 案例生成

生成的案例信息包括：
- **案例信息** (CaseInfo): 案例ID、摘要、案例数据、模拟响应、消息模板
- **断言信息** (AssertInfo): 断言类型、键值、规则、描述等
- **参与者信息**: 业务参与者列表
- **流程步骤**: 完整的业务流程步骤
- **业务类型**: 标准化的业务类型分类

### 4. MCP集成

与e2e-mcp-server集成提供：
- 案例保存 (`add_case`)
- 断言添加 (`add_assertion`)
- 案例执行 (`execute_case`)
- 结果查询 (`get_execution_result`)
- 案例验证 (`validate_case`)

## 使用方法

### 基本流程

```python
from scripts.ai_intent_analyzer import AIIntentAnalyzer
from scripts.case_generator import CaseGenerator
from scripts.mcp_integration import E2ETestOrchestrator

# 1. 初始化AI分析器
analyzer = AIIntentAnalyzer(
    api_key="sk-ayllmfdkqjsvuaubhgnvhbosnoekacdzldbanzbmzohexxef",
    api_base="https://api.siliconflow.cn/v1",
    model="MiniMaxAI/MiniMax-M2"
)

# 2. 分析业务意图
intent = analyzer.analyze_business_intent(
    case_id="epcc_201_0110_Z_AI_001",
    description="支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。"
)

# 3. 生成案例
generator = CaseGenerator(templates_dir="assets/templates")
case_info = generator.generate_case("epcc_201_0110_Z_AI_001", intent)
assertions = generator.generate_assertions(intent, template)

# 4. 执行完整流程
orchestrator = E2ETestOrchestrator(mcp_integration)
result = orchestrator.create_and_execute_case(
    case_info=asdict(case_info),
    assertions=[asdict(a) for a in assertions],
    execute_params={}
)
```

### 高级用法

#### 自定义模板匹配
```python
# 调整匹配权重
generator = CaseGenerator(templates_dir="assets/templates")
generator.match_weights = {
    'business_type': 0.5,
    'participants': 0.3,
    'flow_steps': 0.2
}
```

#### 批量案例生成
```python
# 批量处理多个业务描述
business_descriptions = [
    {"case_id": "case_001", "description": "..."},
    {"case_id": "case_002", "description": "..."}
]

results = []
for item in business_descriptions:
    intent = analyzer.analyze_business_intent(**item)
    case_info = generator.generate_case(item['case_id'], intent)
    results.append(case_info)
```

## 资源文件

### 模板文件 (assets/templates/)

按业务类型组织的模板文件，包含：
- 案例信息模板 (CaseInfo)
- 断言信息模板 (AssertInfo)
- 参与者定义
- 流程步骤定义

### 示例文件 (assets/examples/)

业务描述示例和对应的生成结果：
- 快捷支付案例
- 转账汇款案例
- 查询业务案例
- 退款业务案例

### 参考文档 (references/)

- [API文档](references/api_docs.md) - 详细API使用说明
- [业务场景参考](references/business_scenarios.md) - 常见业务场景和模板
- [最佳实践](references/best_practices.md) - 案例生成最佳实践

## 配置说明

### AI分析器配置

```python
API_CONFIG = {
    "api_key": "sk-ayllmfdkqjsvuaubhgnvhbosnoekacdzldbanzbmzohexxef",
    "api_base": "https://api.siliconflow.cn/v1",
    "model": "MiniMaxAI/MiniMax-M2"
}
```

### MCP服务配置

```python
MCP_CONFIG = {
    "base_url": "http://localhost:8000",
    "auth_token": None  # 如果需要认证
}
```

## 注意事项

1. **API密钥安全**: 请妥善保管API密钥，不要提交到代码仓库
2. **模板质量**: 模板文件的完整性直接影响生成案例的质量
3. **网络连接**: AI分析需要稳定的网络连接
4. **MCP服务**: 确保e2e-mcp-server服务正常运行
5. **异常处理**: 建议添加适当的异常处理和重试机制

## 扩展指南

### 添加新业务类型

1. 在 `assets/templates/` 中创建新的模板文件
2. 更新模板匹配逻辑以支持新业务类型
3. 添加对应的示例和文档

### 自定义断言规则

修改 `scripts/case_generator.py` 中的 `_generate_dynamic_assertions` 方法：
```python
def _generate_dynamic_assertions(self, intent: IntentAnalysis) -> List[AssertInfo]:
    assertions = []

    # 添加自定义断言逻辑
    if intent.business_type == "新业务类型":
        assertions.append(AssertInfo(...))

    return assertions
```

## 故障排除

### 常见问题

1. **AI分析失败**
   - 检查API密钥是否正确
   - 确认网络连接正常
   - 验证模型名称是否正确

2. **模板匹配失败**
   - 检查模板文件是否存在
   - 验证模板格式是否正确
   - 确认业务类型是否支持

3. **MCP服务连接失败**
   - 检查MCP服务地址是否正确
   - 确认服务是否启动
   - 验证认证信息

### 日志和调试

启用详细日志输出：
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```