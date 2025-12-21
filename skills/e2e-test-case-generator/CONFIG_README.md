# 配置说明

本文档说明E2E测试案例生成器的配置文件使用方法。

## 配置文件位置

配置文件位于项目根目录：`config.yaml`

## 配置文件结构

### 1. AI配置 (ai_config)

```yaml
ai_config:
  api_key: "your-api-key"           # OpenAI API密钥
  api_base: "https://api.siliconflow.cn/v1"  # API基础URL
  model: "MiniMaxAI/MiniMax-M2"     # 使用的模型名称
  temperature: 0.1                  # 模型温度参数（可选）
  max_tokens: 2000                  # 最大令牌数（可选）
```

**说明：**
- `api_key`: 必需的API密钥
- `api_base`: API服务器地址
- `model`: 使用的AI模型
- `temperature`: 控制输出随机性，0.0-2.0之间（默认0.1）
- `max_tokens`: 生成的最大令牌数（默认2000）

### 2. MCP服务配置 (mcp_config)

```yaml
mcp_config:
  base_url: "http://localhost:8000"  # MCP服务地址
  auth_token: null                   # 认证token（可选）
```

**说明：**
- `base_url`: MCP服务器地址
- `auth_token`: 如果MCP服务需要认证，设置token；否则设为null

### 3. 模板配置 (template_config)

```yaml
template_config:
  templates_dir: "assets/templates"   # 模板文件目录
  match_weights:                      # 模板匹配权重
    business_type: 0.5                # 业务类型权重
    participants: 0.3                 # 参与者权重
    flow_steps: 0.2                   # 流程步骤权重
```

**说明：**
- `templates_dir`: 包含业务模板的目录路径
- `match_weights`: 模板匹配算法的权重配置
  - 所有权重之和应该为1.0
  - 业务类型匹配权重最高，因为最关键

### 4. 输出配置 (output_config)

```yaml
output_config:
  output_dir: "output"               # 输出目录
  execute_immediately: false         # 是否立即执行测试
```

**说明：**
- `output_dir`: 生成的测试案例文件保存目录
- `execute_immediately`: 是否在生成后立即执行测试案例

### 5. 日志配置 (logging_config)

```yaml
logging_config:
  level: "INFO"                      # 日志级别
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

**说明：**
- `level`: 日志级别（DEBUG, INFO, WARNING, ERROR）
- `format`: 日志输出格式

## 使用方法

### 1. 修改配置

编辑项目根目录的`config.yaml`文件：

```bash
# 编辑配置文件
vim config.yaml
# 或者使用其他编辑器
nano config.yaml
```

### 2. 加载配置

配置会在程序启动时自动加载，无需手动调用：

```python
from scripts.config_manager import config

# 获取AI配置
ai_config = config.get_ai_config()

# 获取单个配置值
api_key = config.get("ai_config.api_key")
```

### 3. 动态修改配置

如果需要运行时修改配置：

```python
from scripts.config_manager import config

# 重新加载配置文件
config.reload()

# 或者直接修改配置字典（不推荐）
config._config["ai_config"]["api_key"] = "new-key"
```

## 配置验证

### 检查配置文件是否正确

```python
from scripts.config_manager import config

try:
    # 测试加载配置
    ai_config = config.get_ai_config()
    print("✅ 配置加载成功")
    print(f"API密钥: {ai_config['api_key'][:10]}...")
except Exception as e:
    print(f"❌ 配置加载失败: {e}")
```

### 验证必需的字段

```python
required_fields = [
    "ai_config.api_key",
    "ai_config.api_base",
    "ai_config.model",
    "template_config.templates_dir"
]

for field in required_fields:
    value = config.get(field)
    if not value:
        print(f"⚠️  缺少配置: {field}")
    else:
        print(f"✅ {field}: {value}")
```

## 最佳实践

### 1. API密钥安全

- **不要将API密钥提交到代码仓库**
- 使用环境变量或安全的密钥管理服务
- 定期轮换API密钥

### 2. 环境隔离

为不同环境创建不同的配置文件：

```bash
# 开发环境
cp config.yaml config.dev.yaml

# 测试环境
cp config.yaml config.test.yaml

# 生产环境
cp config.yaml config.prod.yaml
```

### 3. 配置验证

在应用启动时验证关键配置：

```python
def validate_config():
    """验证配置"""
    errors = []

    # 检查API密钥
    if not config.get("ai_config.api_key"):
        errors.append("缺少API密钥")

    # 检查模板目录
    template_dir = config.get("template_config.templates_dir")
    if not template_dir or not Path(template_dir).exists():
        errors.append("模板目录不存在")

    if errors:
        raise ValueError(f"配置验证失败: {', '.join(errors)}")

# 在应用启动时调用
validate_config()
```

### 4. 默认值处理

使用`get`方法的默认值参数：

```python
# 获取配置，提供默认值
temperature = config.get("ai_config.temperature", 0.1)
output_dir = config.get("output_config.output_dir", "output")

# 检查配置是否存在
if not config.get("ai_config.api_key"):
    raise ValueError("请在config.yaml中配置API密钥")
```

## 故障排除

### 1. 配置文件找不到

```
FileNotFoundError: 配置文件不存在: /path/to/config.yaml
```

**解决方案：**
- 确保`config.yaml`文件在项目根目录
- 检查文件路径是否正确

### 2. YAML格式错误

```
ValueError: 配置文件格式错误: ...
```

**解决方案：**
- 使用YAML验证工具检查语法
- 确保缩进使用空格（不是制表符）
- 检查引号和冒号的使用

### 3. 配置值类型错误

```
TypeError: 配置值类型错误
```

**解决方案：**
- 确保字符串值用引号包围
- 布尔值使用`true/false`（小写）
- 数字不要用引号

### 4. 缺少必需配置

```
KeyError: 'api_key'
```

**解决方案：**
- 检查配置文件是否包含所有必需字段
- 使用配置验证工具检查

## 示例配置

完整的示例配置：

```yaml
# E2E测试案例生成器配置文件

ai_config:
  api_key: "sk-your-api-key-here"
  api_base: "https://api.siliconflow.cn/v1"
  model: "MiniMaxAI/MiniMax-M2"
  temperature: 0.1
  max_tokens: 2000

mcp_config:
  base_url: "http://localhost:8000"
  auth_token: null

template_config:
  templates_dir: "assets/templates"
  match_weights:
    business_type: 0.5
    participants: 0.3
    flow_steps: 0.2

output_config:
  output_dir: "output"
  execute_immediately: false

logging_config:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```