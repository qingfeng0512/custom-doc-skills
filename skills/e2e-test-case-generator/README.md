# E2E测试案例生成器

基于AI智能分析的业务测试案例生成工具，支持全链路测试平台的自动化案例创建、执行和验证。

## ✨ 核心特性

- 🧠 **智能意图分析** - 使用MiniMax-M2模型深度理解业务场景
- 🎯 **精准模板匹配** - 多维度智能匹配最佳案例模板
- 📝 **标准化生成** - 自动生成符合规范的案例信息和断言
- 🔗 **MCP无缝集成** - 与e2e-mcp-server完美集成
- 🚀 **端到端自动化** - 完整的测试流程自动化

## 📁 目录结构

```
e2e-test-case-generator/
├── SKILL.md                      # 技能说明文档
├── README.md                     # 项目说明
├── scripts/                      # 核心脚本
│   ├── ai_intent_analyzer.py     # AI意图分析器
│   ├── case_generator.py         # 案例生成器
│   ├── mcp_integration.py        # MCP服务集成
│   ├── e2e_generator.py          # 主程序
│   └── test_skill.py             # 功能测试
├── assets/
│   ├── templates/                # 案例模板
│   │   ├── 快捷支付.md
│   │   └── 转账汇款.md
│   └── examples/                 # 示例文件
│       └── business_examples.md
└── references/                   # 参考文档（预留）
```

## 🚀 快速开始

### 1. 基本使用

```python
from scripts.e2e_generator import E2EGenerator

# 创建生成器实例
generator = E2EGenerator()

# 从业务描述生成案例
result = generator.generate_case_from_description(
    case_id="epcc_201_0110_Z_AI_001",
    description="支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。"
)

print(f"业务类型: {result['intent_analysis']['business_type']}")
print(f"参与者: {', '.join(result['intent_analysis']['participants'])}")
print(f"断言数量: {len(result['assertions'])}")
```

### 2. 批量生成

```python
test_cases = [
    {
        "case_id": "epcc_201_0110_Z_AI_001",
        "description": "支付机构发起快捷支付..."
    },
    {
        "case_id": "epcc_201_0120_Z_AI_002",
        "description": "用户发起转账汇款请求..."
    }
]

results = generator.batch_generate(test_cases)
```

### 3. 完整流程（包含执行）

```python
result = generator.generate_case_from_description(
    case_id="epcc_201_0110_Z_AI_001",
    description="业务描述...",
    execute_immediately=True  # 立即执行案例
)
```

## 🔧 配置说明

### AI分析器配置

在 `scripts/ai_intent_analyzer.py` 中修改API配置：

```python
API_CONFIG = {
    "api_key": "your-api-key",
    "api_base": "https://api.siliconflow.cn/v1",
    "model": "MiniMaxAI/MiniMax-M2"
}
```

### MCP服务配置

在 `scripts/mcp_integration.py` 中修改服务配置：

```python
MCP_CONFIG = {
    "base_url": "http://localhost:8000",
    "auth_token": None
}
```

## 📊 生成示例

### 输入：业务描述

```
案例编号: epcc_201_0110_Z_AI_001
业务描述: 支付机构发起快捷支付，网联平台受理后转发给银行处理，银行返回处理并支付成功，平台接收后响应支付机构业务处理成功。
```

### 输出：案例信息

```json
{
  "caseId": "epcc_201_0110_Z_AI_001",
  "caseSummary": "支付机构、网联平台、银行执行支付业务，流程：发起 → 受理 → 转发 → 处理 → 成功",
  "caseData": {
    "transType": "quickpay",
    "amount": "100.00",
    "orderId": "ORDER_1640995200000"
  },
  "participants": ["支付机构", "网联平台", "银行"],
  "flowSteps": ["发起", "受理", "转发", "处理", "成功"]
}
```

### 输出：断言信息

```json
[
  {
    "assertType": "MSG",
    "assertKey": "responseCode",
    "assertValue": "00",
    "assertRule": "REQUIRED",
    "createBy": "AI",
    "description": "验证交易响应码为成功"
  }
]
```

## 🧪 测试

运行功能测试：

```bash
cd scripts
python3 test_skill.py
```

测试包括：
- ✅ 技能结构测试
- ✅ 意图分析测试
- ✅ 模板加载测试
- ✅ 输出生成测试

## 📚 支持的业务类型

- 💳 **支付业务** - 快捷支付、网银支付、扫码支付
- 💸 **转账汇款** - 行内转账、跨行转账、实时转账
- 🔍 **查询业务** - 余额查询、交易查询、账单查询
- 💰 **退款业务** - 全额退款、部分退款、实时退款

## 🤝 扩展指南

### 添加新业务类型

1. 在 `assets/templates/` 中创建新的模板文件
2. 在 `scripts/case_generator.py` 中更新模板匹配逻辑
3. 添加对应的示例文件

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

## ⚠️ 注意事项

1. **API密钥安全** - 请妥善保管API密钥，不要提交到代码仓库
2. **网络连接** - AI分析需要稳定的网络连接
3. **MCP服务** - 确保e2e-mcp-server服务正常运行
4. **模板质量** - 模板文件的完整性直接影响生成案例的质量

## 📄 许可证

本项目采用MIT许可证。

## 🙋‍♂️ 支持

如有问题或建议，请提交Issue或联系开发团队。