# Custom Doc Skills

一个收集和整理编程框架技能文档的项目，提供开发者快速参考和学习资料。

## 📋 项目概览

本项目旨在为开发者提供常用的前端和后端框架的完整技能文档，包括：

- **React 技能** - 现代前端框架的完整开发指南
- **Vue2 技能** - 渐进式前端框架的详细文档
- **Chrome Extensions 技能** - 浏览器扩展开发完整指南
- **LangChain 技能** - LLM 应用开发框架指南
- **可扩展** - 支持添加更多框架和技能文档

## 🚀 可用技能

### React 技能 (`skills/react/`)
总计 **47页** 完整文档，涵盖：

- **API 参考** - React 核心API文档 (2页)
- **组件** - 组件开发最佳实践 (13页)
- **入门指南** - 快速上手教程 (2页)
- **Hooks** - React Hooks 完整指南 (4页)
- **状态管理** - 状态管理模式和方案 (10页)
- **其他** - 高级特性和最佳实践 (16页)

### Vue2 技能 (`skills/vue2/`)
总计 **38页** 详细文档，包含：

- **高级特性** - Vue2 高级用法 (8页)
- **API 参考** - Vue2 核心API (1页)
- **核心概念** - 基础知识详解 (5页)
- **入门指南** - 快速开始教程 (1页)
- **迁移指南** - 从其他框架迁移 (4页)
- **其他** - 生态和工具介绍 (20页)

### Chrome Extensions 技能 (`skills/chrome-extensions/`)
总计 **11页** 完整文档，涵盖：

- **入门指南** - 扩展开发快速上手 (getting_started.md)
- **清单配置** - Manifest V3 配置详解 (manifest.md)
- **后台脚本** - Background Scripts 开发 (background_scripts.md)
- **内容脚本** - Content Scripts 注入与通信 (content_scripts.md)
- **弹出界面** - Popup UI 开发指南 (popup_ui.md)
- **存储管理** - Chrome Storage API (storage.md)
- **权限管理** - 扩展权限配置 (permissions.md)
- **调试技巧** - 扩展调试方法 (debugging.md)
- **Web Extensions** - 跨浏览器扩展开发 (web_extensions.md)

### LangChain 技能 (`skills/langchain/`)
总计 **6页**详细文档，包含 ：

- **入门指南** - LangChain 快速上手 (getting_started.md)
- **核心概念** - LangChain 基础概念 (concepts.md)
- **Chain 链** - Chain 组合与使用 (chains.md)
- **Agent 代理** - 智能代理开发 (agents.md)
- **教程指南** - 实战教程集合 (tutorials.md)
- **索引文档** - 文档检索系统 (index.md)

## 📁 项目结构

```
custom-doc-skills/
├── skills/
│   ├── react/              # React 技能文档
│   │   ├── SKILL.md        # 技能元数据
│   │   └── references/     # 详细参考文档
│   │       ├── api.md
│   │       ├── components.md
│   │       ├── getting_started.md
│   │       ├── hooks.md
│   │       ├── other.md
│   │       └── state.md
│   │
│   ├── vue2/               # Vue2 技能文档
│   │   ├── SKILL.md        # 技能元数据
│   │   └── references/     # 详细参考文档
│   │       ├── advanced.md
│   │       ├── api.md
│   │       ├── essentials.md
│   │       ├── getting_started.md
│   │       ├── migration.md
│   │       └── other.md
│   │
│   ├── chrome-extensions/  # Chrome Extensions 技能文档
│       ├── SKILL.md        # 技能元数据
│       └── references/     # 详细参考文档
│           ├── getting_started.md
│           ├── manifest.md
│           ├── background_scripts.md
│           ├── content_scripts.md
│           ├── popup_ui.md
│           ├── storage.md
│           ├── permissions.md
│           ├── debugging.md
│           └── web_extensions.md
│
│   └── langchain/          # LangChain 技能文档
│       ├── SKILL.md        # 技能元数据
│       └── references/     # 详细参考文档
│           ├── getting_started.md
│           ├── concepts.md
│           ├── chains.md
│           ├── agents.md
│           ├── tutorials.md
│           └── index.md
│
├── README.md               # 项目说明文档
└── LICENSE                 # 许可证文件
```

## 🎯 技能特性

- ✅ **官方文档来源** - 基于框架官方文档整理
- ✅ **快速参考** - 便于快速查找常用API和方法
- ✅ **代码示例** - 提供丰富的代码实例和使用场景
- ✅ **完整覆盖** - 涵盖从入门到高级的完整内容
- ✅ **统一格式** - 标准化的文档结构和索引
- ✅ **易于扩展** - 可方便地添加新的技能文档

## 📖 使用方法

### 查找文档
1. 根据你的技术栈选择对应的技能文件夹（`skills/react/` 或 `skills/vue2/`）
2. 查看 `references/` 目录下的具体文档
3. 使用目录索引快速定位需要的内容

### 技能触发
每个技能都包含完整的元数据配置，支持：
- 关键词搜索和匹配
- 上下文感知的文档推荐
- 智能代码补全和提示

### 快速参考
- 入门指南：适合初学者快速上手
- API 参考：开发者查阅具体API用法
- 最佳实践：解决常见问题和优化方案

## 🤝 贡献指南

### 添加新技能
1. 在 `skills/` 目录下创建新的技能文件夹
2. 复制并修改 `SKILL.md` 模板文件
3. 在技能文件夹下创建 `references/` 目录
4. 按照统一格式整理文档内容
5. 提交 PR 或直接推送

### 文档格式要求
- 使用 Markdown 格式
- 包含清晰的目录结构
- 提供代码示例和说明
- 保持与现有技能文档的一致性

## 📄 许可证

本项目采用开源许可证，详情请查看 [LICENSE](LICENSE) 文件。

## 🔧 维护说明

- 技能文档定期更新，与官方文档保持同步
- 支持版本管理和向后兼容
- 欢迎提交 Issue 和 Pull Request

---

**让开发更高效，让学习更简单！** 🚀
