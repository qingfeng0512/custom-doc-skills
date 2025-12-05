# Chrome-Plugin-Dev - Debugging

**Pages:** 6

---

## 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/debug?hl=zh-cn

**Contents:**
- 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 准备工作
- 中断扩展程序
  - 调试清单
  - 调试服务工件
    - 查找日志
    - 定位错误
    - 检查 Service Worker 状态
  - 调试弹出式窗口
  - 调试内容脚本

扩展程序可以访问与网页相同的 Chrome 开发者工具。如需成为调试扩展程序的专家，您需要了解如何查找不同扩展程序组件的日志和错误。本教程介绍了调试扩展程序的基本方法。

本指南假定您具备基本的 Web 开发经验。建议您阅读开发基础知识，了解扩展程序开发工作流程。设计界面介绍了扩展程序中提供的界面元素。

本教程将一次破坏一个扩展程序组件，然后演示如何修复它。请务必先撤消某个部分引入的 bug，然后再继续下一部分。首先，在 GitHub 上下载“Broken Color”示例。

首先，我们将 "version" 键更改为 "versions"，以破坏清单文件：

现在，我们尝试在本地加载扩展程序。您会看到一个指明问题的错误对话框：

当清单键无效时，扩展程序会加载失败，但 Chrome 会提示您如何解决此问题。

撤消该更改，然后输入无效权限，看看会发生什么。 将 "activeTab" 权限更改为小写的 "activetab"：

保存扩展程序，然后尝试重新加载。这次应该能成功加载。在扩展程序管理页面中，您会看到三个按钮：详情、移除和错误。出现错误时，错误按钮标签会变为红色。点击错误按钮，您会看到以下错误：

在继续之前，请恢复权限，点击右上角的清除全部以清除日志，然后重新加载扩展程序。

服务工件会将默认颜色设置为存储，并将其记录到控制台。如需查看此日志，请选择检查视图旁边的蓝色链接，打开 Chrome 开发者工具面板。

我们将 onInstalled 更改为小写的 oninstalled，以破坏该服务工件：

刷新页面，然后点击错误以查看错误日志。第一个错误会告知您服务工件未能注册。这意味着启动过程中出了点问题：

还原我们引入的 bug，点击右上角的全部清除，然后重新加载扩展程序。

您可以按照以下步骤确定服务工件何时唤醒以执行任务：

前往 Service Workers 窗格。

如需测试代码，请使用状态旁边的链接启动或停止服务工件。

现在，扩展程序已正确初始化，接下来我们将注释掉下面突出显示的行，以中断弹出式窗口：

返回“扩展程序管理”页面。错误按钮会再次显示。点击该日志即可查看新日志。系统会显示以下错误消息：

您可以通过检查弹出式窗口来打开其 DevTools。

错误 tabs is undefined 表示扩展程序不知道在哪里注入内容脚本。如需更正此问题，请调用 tabs.query()，然后选择处于活动状态的标签页。

如需更新代码，请点击右上角的清除全部按钮，然后重新加载扩展程序。

现在，我们将变量“color”更改为“colors”，以破坏内容脚本：

刷新页面，打开弹出式窗口，然后点击绿色框。不会有任何反应。

如果您前往“扩展程序管理”页面，则不会看到错误按钮。这是因为“扩展程序管理”页面上只会记录运行时错误 console.warning 和 console.error。

内容脚本在网站内运行。因此，若要查找这些错误，我们必须检查扩展程序尝试更改的网页：

如需在内容脚本中使用开发者工具，请点击 top 旁边的下拉箭头，然后选择相应扩展程序。

错误消息指出 colors 未定义。扩展程序未正确传递变量。更正注入的脚本，以将颜色变量传递到代码中。

在最快的开发者能够打开 DevTools 之前，弹出式窗口通常会发出所有必要的网络请求。如需查看这些请求，请在“网络”面板中刷新。它会重新加载弹出式窗口，而不会关闭 DevTools 面板。

某些扩展程序 API 需要权限。请参阅权限一文和 Chrome API，确保扩展程序在manifest中请求的权限正确无误。

如需详细了解 Chrome 开发者工具，请参阅文档。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 3 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

Example 4 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

---

## chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/debugger?hl=zh-cn

**Contents:**
- chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 目标
  - 受限网域
  - 使用帧
  - 附加到相关目标
- 示例
- 类型

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

您必须在扩展程序的清单中声明 "debugger" 权限，才能使用此 API。

附加后，chrome.debugger API 可让您向指定目标发送 Chrome DevTools Protocol (CDP) 命令。深入说明 CDP 超出了本文档的范围，如需详细了解 CDP，请参阅 CDP 官方文档。

目标表示正在调试的对象，可以包括标签页、iframe 或 worker。每个目标都由 UUID 标识，并具有关联的类型（例如 iframe、shared_worker 等）。

在一个目标中，可能存在多个执行上下文，例如，同一进程 iframe 不会获得唯一的目标，而是表示为可从单个目标访问的不同上下文。

出于安全考虑，chrome.debugger API 不提供对所有 Chrome DevTools 协议网域的访问权限。可用的网域包括：Accessibility、Audits、CacheStorage、Console、CSS、Database、Debugger、DOM、DOMDebugger、DOMSnapshot、Emulation、Fetch、IO、Input、Inspector、Log、Network、Overlay、Page、Performance、Profiler、Runtime、Storage、Target、Tracing、WebAudio 和 WebAuthn。

帧与目标之间不存在一对一的映射关系。在单个标签页中，多个相同进程的框架可能共享同一目标，但使用不同的执行上下文。另一方面，可能会为进程外 iframe 创建新目标。

如需附加到所有帧，您需要分别处理每种类型的帧：

监听 Runtime.executionContextCreated 事件，以识别与同一进程框架关联的新执行上下文。

按照附加到相关目标中的步骤操作，以识别进程外帧。

连接到目标后，您可能需要连接到更多相关目标，包括进程外子框架或关联的工作人员。

从 Chrome 125 开始，chrome.debugger API 支持扁平会话。这样一来，您就可以将其他目标作为子级添加到主调试器会话，并向它们发送消息，而无需再次调用 chrome.debugger.attach。不过，您可以在调用 chrome.debugger.sendCommand 时添加 sessionId 属性，以标识要向哪个子目标发送命令。

如需自动附加到进程外子框架，请先为 Target.attachedToTarget 事件添加监听器：

然后，通过发送 Target.setAutoAttach 命令并将 flatten 选项设置为 true 来启用自动附加：

自动附加仅附加到目标知道的帧，这些帧仅限于与其关联的帧的直接子帧。例如，如果框架层次结构为 A -> B -> C（其中所有框架均为跨源），则针对与 A 关联的目标调用 Target.setAutoAttach 会导致会话也附加到 B。不过，这并非递归调用，因此还需要为 B 调用 Target.setAutoAttach，才能将该会话附加到 C。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 debugger API 示例。

调试对象标识符。必须指定 tabId、extensionId 或 targetId

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

调试器会话标识符。必须指定 tabId、extensionId 或 targetId 中的一个。此外，还可以提供可选的 sessionId。如果为从 onEvent 发送的实参指定了 sessionId，则表示相应事件来自根调试对象会话中的子协议会话。如果传递给 sendCommand 时指定了 sessionId，则它会以根调试会话中的子协议会话为目标。

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

Chrome DevTools Protocol 会话的不透明 ID。用于标识由 tabId、extensionId 或 targetId 标识的根会话中的子会话。

扩展程序 ID，如果 type = 'background_page'，则定义该 ID。

标签页 ID，如果 type == 'page'，则定义该 ID。

必需的调试协议版本（“0.1”）。只能附加到主要版本匹配且次要版本大于或等于的调试对象。点击此处可查看协议版本列表。

Promise<TargetInfo[]>

方法名称。应该是 远程调试协议定义的方法之一。

包含请求参数的 JSON 对象。此对象必须符合给定方法的远程调试参数方案。

Promise<object | undefined>

当浏览器终止标签页的调试会话时触发。当标签页正在关闭或 Chrome 开发者工具正在为附加的标签页调用时，会发生这种情况。

**Examples:**

Example 1 (unknown):
```unknown
chrome.debugger
```

Example 2 (unknown):
```unknown
chrome.debugger
```

Example 3 (unknown):
```unknown
sendCommand
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

---

## chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/debugger

**Contents:**
- chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 安全注意事项
- 清单
- 示例
- 类型
  - Debuggee
    - 属性
  - DebuggerSession

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

出于安全考虑，chrome.debugger API 不提供对所有 Chrome DevTools 协议网域的访问权限。可用的网域包括：Accessibility、Audits、CacheStorage、Console、CSS、Database、Debugger、DOM、DOMDebugger、DOMSnapshot、Emulation、Fetch、IO、Input、Inspector、Log、Network、Overlay、Page、Performance、Profiler、Runtime、Storage、Target、Tracing、WebAudio 和 WebAuthn。

您必须在扩展程序的清单中声明 "debugger" 权限才能使用此 API。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 debugger API 示例。

调试对象标识符。必须指定 tabId、extensionId 或 targetId

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

调试器会话标识符。必须指定 tabId、extensionId 或 targetId 中的一个。此外，还可以提供可选的 sessionId。如果为从 onEvent 发送的实参指定了 sessionId，则表示相应事件来自根调试对象会话中的子协议会话。如果传递给 sendCommand 时指定了 sessionId，则它会以根调试会话中的子协议会话为目标。

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

Chrome DevTools Protocol 会话的不透明 ID。用于标识由 tabId、extensionId 或 targetId 标识的根会话中的子会话。

扩展程序 ID，如果 type = 'background_page'，则定义该 ID。

标签页 ID，如果 type == 'page'，则定义该 ID。

必需的调试协议版本（“0.1”）。只能附加到主要版本匹配且次要版本大于或等于的调试对象。点击此处可查看协议版本列表。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

与可用的调试目标对应的 TargetInfo 对象数组。

Promise<TargetInfo[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

方法名称。应该是 远程调试协议定义的方法之一。

包含请求参数的 JSON 对象。此对象必须符合给定方法的远程调试参数方案。

包含响应的 JSON 对象。响应的结构因方法名称而异，由远程调试协议中命令说明的“returns”属性定义。

Promise<object | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

当浏览器终止标签页的调试会话时触发。当标签页正在关闭或 Chrome 开发者工具正在为附加的标签页调用时，会发生这种情况。

**Examples:**

Example 1 (unknown):
```unknown
chrome.debugger
```

Example 2 (unknown):
```unknown
chrome.debugger
```

Example 3 (unknown):
```unknown
sendCommand
```

Example 4 (unknown):
```unknown
chrome.debugger
```

---

## 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/debug

**Contents:**
- 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 准备工作
- 中断扩展程序
  - 调试清单
  - 调试服务工件
    - 查找日志
    - 定位错误
    - 检查 Service Worker 状态
  - 调试弹出式窗口
  - 调试内容脚本

扩展程序可以访问与网页相同的 Chrome 开发者工具。如需成为调试扩展程序的专家，您需要了解如何查找不同扩展程序组件的日志和错误。本教程介绍了调试扩展程序的基本方法。

本指南假定您具备基本的 Web 开发经验。建议您阅读开发基础知识，了解扩展程序开发工作流程。设计界面介绍了扩展程序中提供的界面元素。

本教程将一次破坏一个扩展程序组件，然后演示如何修复它。请务必先撤消某个部分引入的 bug，然后再继续下一部分。首先，在 GitHub 上下载“Broken Color”示例。

首先，我们将 "version" 键更改为 "versions"，以破坏清单文件：

现在，我们尝试在本地加载扩展程序。您会看到一个指明问题的错误对话框：

当清单键无效时，扩展程序会加载失败，但 Chrome 会提示您如何解决此问题。

撤消该更改，然后输入无效权限，看看会发生什么。 将 "activeTab" 权限更改为小写的 "activetab"：

保存扩展程序，然后尝试重新加载。这次应该能成功加载。在扩展程序管理页面中，您会看到三个按钮：详情、移除和错误。出现错误时，错误按钮标签会变为红色。点击错误按钮，您会看到以下错误：

在继续之前，请恢复权限，点击右上角的清除全部以清除日志，然后重新加载扩展程序。

服务工件会将默认颜色设置为存储，并将其记录到控制台。如需查看此日志，请选择检查视图旁边的蓝色链接，打开 Chrome 开发者工具面板。

我们将 onInstalled 更改为小写的 oninstalled，以破坏该服务工件：

刷新页面，然后点击错误以查看错误日志。第一个错误会告知您服务工件未能注册。这意味着启动过程中出了点问题：

还原我们引入的 bug，点击右上角的全部清除，然后重新加载扩展程序。

您可以按照以下步骤确定服务工件何时唤醒以执行任务：

前往 Service Workers 窗格。

如需测试代码，请使用状态旁边的链接启动或停止服务工件。

现在，扩展程序已正确初始化，接下来我们将注释掉下面突出显示的行，以中断弹出式窗口：

返回“扩展程序管理”页面。错误按钮会再次显示。点击该日志即可查看新日志。系统会显示以下错误消息：

您可以通过检查弹出式窗口来打开其 DevTools。

错误 tabs is undefined 表示扩展程序不知道在哪里注入内容脚本。如需更正此问题，请调用 tabs.query()，然后选择处于活动状态的标签页。

如需更新代码，请点击右上角的清除全部按钮，然后重新加载扩展程序。

现在，我们将变量“color”更改为“colors”，以破坏内容脚本：

刷新页面，打开弹出式窗口，然后点击绿色框。不会有任何反应。

如果您前往“扩展程序管理”页面，则不会看到错误按钮。这是因为“扩展程序管理”页面上只会记录运行时错误 console.warning 和 console.error。

内容脚本在网站内运行。因此，若要查找这些错误，我们必须检查扩展程序尝试更改的网页：

如需在内容脚本中使用开发者工具，请点击 top 旁边的下拉箭头，然后选择相应扩展程序。

错误消息指出 colors 未定义。扩展程序未正确传递变量。更正注入的脚本，以将颜色变量传递到代码中。

在最快的开发者能够打开 DevTools 之前，弹出式窗口通常会发出所有必要的网络请求。如需查看这些请求，请在“网络”面板中刷新。它会重新加载弹出式窗口，而不会关闭 DevTools 面板。

某些扩展程序 API 需要权限。请参阅权限一文和 Chrome API，确保扩展程序在manifest中请求的权限正确无误。

如需详细了解 Chrome 开发者工具，请参阅文档。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 3 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

Example 4 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

---

## chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/debugger

**Contents:**
- chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 目标
  - 受限网域
  - 使用帧
  - 附加到相关目标
- 示例
- 类型

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

您必须在扩展程序的清单中声明 "debugger" 权限，才能使用此 API。

附加后，chrome.debugger API 可让您向指定目标发送 Chrome DevTools Protocol (CDP) 命令。深入说明 CDP 超出了本文档的范围，如需详细了解 CDP，请参阅 CDP 官方文档。

目标表示正在调试的对象，可以包括标签页、iframe 或 worker。每个目标都由 UUID 标识，并具有关联的类型（例如 iframe、shared_worker 等）。

在一个目标中，可能存在多个执行上下文，例如，同一进程 iframe 不会获得唯一的目标，而是表示为可从单个目标访问的不同上下文。

出于安全考虑，chrome.debugger API 不提供对所有 Chrome DevTools 协议网域的访问权限。可用的网域包括：Accessibility、Audits、CacheStorage、Console、CSS、Database、Debugger、DOM、DOMDebugger、DOMSnapshot、Emulation、Fetch、IO、Input、Inspector、Log、Network、Overlay、Page、Performance、Profiler、Runtime、Storage、Target、Tracing、WebAudio 和 WebAuthn。

帧与目标之间不存在一对一的映射关系。在单个标签页中，多个相同进程的框架可能共享同一目标，但使用不同的执行上下文。另一方面，可能会为进程外 iframe 创建新目标。

如需附加到所有帧，您需要分别处理每种类型的帧：

监听 Runtime.executionContextCreated 事件，以识别与同一进程框架关联的新执行上下文。

按照附加到相关目标中的步骤操作，以识别进程外帧。

连接到目标后，您可能需要连接到更多相关目标，包括进程外子框架或关联的工作人员。

从 Chrome 125 开始，chrome.debugger API 支持扁平会话。这样一来，您就可以将其他目标作为子级添加到主调试器会话，并向它们发送消息，而无需再次调用 chrome.debugger.attach。不过，您可以在调用 chrome.debugger.sendCommand 时添加 sessionId 属性，以标识要向哪个子目标发送命令。

如需自动附加到进程外子框架，请先为 Target.attachedToTarget 事件添加监听器：

然后，通过发送 Target.setAutoAttach 命令并将 flatten 选项设置为 true 来启用自动附加：

自动附加仅附加到目标知道的帧，这些帧仅限于与其关联的帧的直接子帧。例如，如果框架层次结构为 A -> B -> C（其中所有框架均为跨源），则针对与 A 关联的目标调用 Target.setAutoAttach 会导致会话也附加到 B。不过，这并非递归调用，因此还需要为 B 调用 Target.setAutoAttach，才能将该会话附加到 C。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 debugger API 示例。

调试对象标识符。必须指定 tabId、extensionId 或 targetId

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

调试器会话标识符。必须指定 tabId、extensionId 或 targetId 中的一个。此外，还可以提供可选的 sessionId。如果为从 onEvent 发送的实参指定了 sessionId，则表示相应事件来自根调试对象会话中的子协议会话。如果传递给 sendCommand 时指定了 sessionId，则它会以根调试会话中的子协议会话为目标。

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

Chrome DevTools Protocol 会话的不透明 ID。用于标识由 tabId、extensionId 或 targetId 标识的根会话中的子会话。

扩展程序 ID，如果 type = 'background_page'，则定义该 ID。

标签页 ID，如果 type == 'page'，则定义该 ID。

必需的调试协议版本（“0.1”）。只能附加到主要版本匹配且次要版本大于或等于的调试对象。点击此处可查看协议版本列表。

Promise<TargetInfo[]>

方法名称。应该是 远程调试协议定义的方法之一。

包含请求参数的 JSON 对象。此对象必须符合给定方法的远程调试参数方案。

Promise<object | undefined>

当浏览器终止标签页的调试会话时触发。当标签页正在关闭或 Chrome 开发者工具正在为附加的标签页调用时，会发生这种情况。

**Examples:**

Example 1 (unknown):
```unknown
chrome.debugger
```

Example 2 (unknown):
```unknown
chrome.debugger
```

Example 3 (unknown):
```unknown
sendCommand
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

---

## chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/debugger?hl=zh-cn

**Contents:**
- chrome.debugger 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 目标
  - 受限网域
  - 使用帧
  - 附加到相关目标
- 示例
- 类型

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

您必须在扩展程序的清单中声明 "debugger" 权限，才能使用此 API。

附加后，chrome.debugger API 可让您向指定目标发送 Chrome DevTools Protocol (CDP) 命令。深入说明 CDP 超出了本文档的范围，如需详细了解 CDP，请参阅 CDP 官方文档。

目标表示正在调试的对象，可以包括标签页、iframe 或 worker。每个目标都由 UUID 标识，并具有关联的类型（例如 iframe、shared_worker 等）。

在一个目标中，可能存在多个执行上下文，例如，同一进程 iframe 不会获得唯一的目标，而是表示为可从单个目标访问的不同上下文。

出于安全考虑，chrome.debugger API 不提供对所有 Chrome DevTools 协议网域的访问权限。可用的网域包括：Accessibility、Audits、CacheStorage、Console、CSS、Database、Debugger、DOM、DOMDebugger、DOMSnapshot、Emulation、Fetch、IO、Input、Inspector、Log、Network、Overlay、Page、Performance、Profiler、Runtime、Storage、Target、Tracing、WebAudio 和 WebAuthn。

帧与目标之间不存在一对一的映射关系。在单个标签页中，多个相同进程的框架可能共享同一目标，但使用不同的执行上下文。另一方面，可能会为进程外 iframe 创建新目标。

如需附加到所有帧，您需要分别处理每种类型的帧：

监听 Runtime.executionContextCreated 事件，以识别与同一进程框架关联的新执行上下文。

按照附加到相关目标中的步骤操作，以识别进程外帧。

连接到目标后，您可能需要连接到更多相关目标，包括进程外子框架或关联的工作人员。

从 Chrome 125 开始，chrome.debugger API 支持扁平会话。这样一来，您就可以将其他目标作为子级添加到主调试器会话，并向它们发送消息，而无需再次调用 chrome.debugger.attach。不过，您可以在调用 chrome.debugger.sendCommand 时添加 sessionId 属性，以标识要向哪个子目标发送命令。

如需自动附加到进程外子框架，请先为 Target.attachedToTarget 事件添加监听器：

然后，通过发送 Target.setAutoAttach 命令并将 flatten 选项设置为 true 来启用自动附加：

自动附加仅附加到目标知道的帧，这些帧仅限于与其关联的帧的直接子帧。例如，如果框架层次结构为 A -> B -> C（其中所有框架均为跨源），则针对与 A 关联的目标调用 Target.setAutoAttach 会导致会话也附加到 B。不过，这并非递归调用，因此还需要为 B 调用 Target.setAutoAttach，才能将该会话附加到 C。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 debugger API 示例。

调试对象标识符。必须指定 tabId、extensionId 或 targetId

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

调试器会话标识符。必须指定 tabId、extensionId 或 targetId 中的一个。此外，还可以提供可选的 sessionId。如果为从 onEvent 发送的实参指定了 sessionId，则表示相应事件来自根调试对象会话中的子协议会话。如果传递给 sendCommand 时指定了 sessionId，则它会以根调试会话中的子协议会话为目标。

您要调试的扩展程序的 ID。只有在使用 --silent-debugger-extension-api 命令行开关时，才能附加到扩展程序后台页面。

Chrome DevTools Protocol 会话的不透明 ID。用于标识由 tabId、extensionId 或 targetId 标识的根会话中的子会话。

扩展程序 ID，如果 type = 'background_page'，则定义该 ID。

标签页 ID，如果 type == 'page'，则定义该 ID。

必需的调试协议版本（“0.1”）。只能附加到主要版本匹配且次要版本大于或等于的调试对象。点击此处可查看协议版本列表。

Promise<TargetInfo[]>

方法名称。应该是 远程调试协议定义的方法之一。

包含请求参数的 JSON 对象。此对象必须符合给定方法的远程调试参数方案。

Promise<object | undefined>

当浏览器终止标签页的调试会话时触发。当标签页正在关闭或 Chrome 开发者工具正在为附加的标签页调用时，会发生这种情况。

**Examples:**

Example 1 (unknown):
```unknown
chrome.debugger
```

Example 2 (unknown):
```unknown
chrome.debugger
```

Example 3 (unknown):
```unknown
sendCommand
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

---
