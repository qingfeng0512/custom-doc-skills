# Chrome-Plugin-Dev - Manifest

**Pages:** 99

---

## 更新代码 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/api-calls

**Contents:**
- 更新代码 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 将 tab.executeScript() 替换为 scripting.executeScript()
- 将 tabs.insertCSS() 和 tabs.removeCSS() 替换为 scripting.insertCSS() 和 scripting.removeCSS()
- 将浏览器操作和页面操作替换为操作
  - 将“browser_action”和“page_action”替换为“action”
  - 将 browserAction 和 pageAction API 替换为 action API
- 将回调替换为 Promise
- 替换预期使用 Manifest V2 后台上下文的函数
- 替换不受支持的 API

这是本教程的三个部分中的第一部分，介绍了对扩展程序服务工件之外的代码所需进行的更改。本部分针对的是与其他问题无关的代码更改必需更改。接下来的两个部分将介绍如何替换屏蔽网络请求和提高安全性。

在 Manifest V3 中，executeScript() 已从 tabs API 移至 scripting API。除了实际的代码更改之外，还需要更改清单文件中的权限。

对于 executeScript() 方法，您需要：

scripting.executeScript() 方法与 tabs.executeScript() 的使用方式类似。二者存在一些差异。

在扩展程序 Service Worker 中。

在清单 V3 中，insertCSS() 和 removeCSS() 从 tabs API 移到了 scripting API。这除了需要更改代码之外，还需要更改清单文件中的权限：

scripting API 中的函数与 tabs 中的函数类似。二者存在一些差异。

该示例展示了如何为 insertCSS() 执行此操作。removeCSS() 的过程是相同的。

在 Manifest V2 中，浏览器操作和页面操作是两个单独的概念。虽然他们起初的角色不同，但它们之间的差别逐渐缩小。在 Manifest V3 中，这些概念已整合到 Action API 中。这需要对您的 manifest.json 和扩展程序代码（不同于您在 Manifest V2 后台脚本中添加的内容）进行更改。

Manifest V3 中的 Action 与浏览器 Action 最为相似；不过，action API 不像 pageAction 那样提供 hide() 和 show()。如果您仍需要执行页面操作，则可以使用声明式内容模拟此类操作，或使用标签页 ID 调用 enable() 或 disable()。

在 manifest.json 中，将 "browser_action" 和 "page_action" 字段替换为 "action" 字段。如需了解 "action" 字段，请参阅参考文档。

在 Manifest V2 使用 browserAction 和 pageAction API 的地方，您现在应使用 action API。

在 Manifest V3 中，许多扩展 API 方法都会返回 promise。Promise 是异步方法返回的值的代理或占位符。如果您从未使用过 Promise，则可以在 MDN 上了解相关内容。本页介绍了在 Chrome 扩展程序中使用这些功能的须知事项。

为了实现向后兼容性，许多方法在添加 promise 支持后继续支持回调。请注意，您不能在同一函数调用中同时使用这两种方法。如果您传递回调，则该函数不会返回 promise；如果您希望返回 promise，则不要传递回调。某些 API 功能（例如事件监听器）仍需要回调。如需检查某个方法是否支持 Promise，请在其 API 参考文档中查找“Promise”标签。

如需从回调转换为 promise，请移除回调并处理返回的 promise。以下示例取自可选权限示例，具体而言是 newtab.js。回调版本显示了该示例使用回调对 request() 的调用是什么样的。请注意，可以使用 async 和 await 重写 promise 版本。

其他扩展程序上下文只能使用消息传递与扩展程序服务 worker 进行交互。因此，您需要替换预期使用后台上下文的调用，具体而言：

您的扩展程序脚本应使用消息传递在服务工件与扩展程序的其他部分之间进行通信。目前，这可通过在扩展程序 Service Worker 中使用 sendMessage() 并实现 chrome.runtime.onMessage 来实现。从长远来看，您应计划将这些调用替换为 postMessage() 和服务工件的消息事件处理脚本。

下列方法和属性需要在 Manifest V3 中更改。

**Examples:**

Example 1 (unknown):
```unknown
executeScript()
```

Example 2 (unknown):
```unknown
executeScript()
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"activeTab"
```

---

## 清单 - input_components 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/input-components

**Contents:**
- 清单 - input_components 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，支持将 input.ime API（输入法）用于 ChromeOS。这样一来，您的扩展程序便可以处理按键、设置合成和打开辅助窗口。开发者还必须在扩展程序的 "permissions" 数组中声明 "input" 权限。 该键接受一系列对象：name、id、language、layouts、input_view 和 options_page（请参阅下表）。

**Examples:**

Example 1 (unknown):
```unknown
"permissions"
```

Example 2 (unknown):
```unknown
options_page
```

Example 3 (unknown):
```unknown
options_page
```

Example 4 (unknown):
```unknown
{
  // ...
   "input_components": [{
     "name": "ToUpperIME",
    "id": "ToUpperIME",
    "language": "en",
    "layouts": ["us::eng"]
  }]
  // ...
}
```

---

## Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/checklist?hl=zh-cn

**Contents:**
- Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 更新清单
- 迁移到 Service Worker
- 更新 API 调用
- 替换屏蔽 Web 请求监听器
- 提高扩展程序的安全性
- 发布 Manifest V3 扩展程序

以下核对清单可帮助您跟踪迁移工作。它们定义了必须完成的任务以及指向说明的链接。如迁移摘要中所述，迁移工作大致分为五类。

Manifest V3 与 Manifest V2 manifest.json文件需要的格式略有不同。本页面介绍了仅影响 manifest.json 文件的更改。不过，对脚本和网页的许多更改还需要对清单进行更改。这些更改包含在需要它们的迁移任务中。

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码远离主线程。这样可以让扩展程序仅在需要时运行，从而节省资源。

在开始之前，请先了解后台脚本与扩展 Service Worker 之间的区别。

某些功能需要替换为 Manifest V3 等效项。还有一些扩展程序则需要彻底删除。

您的扩展程序不会像在 Manifest V2 中那样以编程方式读取网络请求并更改请求，而是指定规则来描述在满足一组给定条件时要执行的操作。

完成上述操作后，您可能需要查看一些常见用例：

为了提高扩展程序的安全性，必须进行更改。这包括移除不再受支持的远程托管代码。

扩展程序转换为清单版本 3 后，即可在 Chrome 应用商店中发布扩展程序。根据所做的更改，考虑逐步发布。通过这种方法，您可以确保自己的扩展程序在有限的受众群体范围内能够按预期运行，然后再面向整个用户群发布。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
XMLHttpRequest()
```

Example 4 (unknown):
```unknown
tabs.executeScript()
```

---

## 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/key

**Contents:**
- 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保持一致的扩展程序 ID
  - 将扩展程序上传到开发者信息中心
  - 比较 ID

此值用于在开发期间加载扩展程序或主题时维护其唯一 ID。以下是一些常见使用场景：

在开发过程中，保留单个 ID 至关重要。如需保持一致的 ID，请按以下步骤操作：

将扩展程序目录打包到 .zip 文件中，并将其上传到 Chrome 开发者信息中心，但不要发布：

将代码添加到 "key" 字段下的 manifest.json。这样，扩展程序将使用相同的 ID。

打开 chrome://extensions 中的“扩展程序管理”页面，确保已启用开发者模式，然后上传未打包的扩展程序目录。将扩展程序管理页面上的扩展程序 ID 与开发者信息中心内的商品 ID 进行比较。它们应保持一致。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
-----BEGIN PUBLIC KEY-----
```

Example 3 (unknown):
```unknown
-----END PUBLIC KEY-----
```

Example 4 (unknown):
```unknown
manifest.json
```

---

## 清单 - 默认语言区域 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/default-locale

**Contents:**
- 清单 - 默认语言区域 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

定义支持多个语言区域的扩展程序的默认语言。它是 _locales 中子目录的名称，包含此扩展程序的默认语言。例如，以下代码表示英语是默认语言：

对于已本地化的扩展程序（具有 _locales 目录的扩展程序），必需填写此字段，但 不含 _locales 目录的扩展程序。如需了解详情，请参阅国际化。

**Examples:**

Example 1 (unknown):
```unknown
"default_locale": "en"
```

Example 2 (unknown):
```unknown
"default_locale": "en"
```

---

## 更新清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/manifest

**Contents:**
- 更新清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 更改清单版本号
- 更新主持人权限
- 更新网络无障碍资源

manifest.json 文件的格式要求与 Manifest V2 略有不同。本页介绍了仅影响 manifest.json 文件的更改。但是，对脚本和网页进行的许多更改也需要对清单进行更改。这些更改会在需要时通过迁移任务进行处理。

将 "manifest_version" 字段的值从 2 更改为 3。

Manifest V3 中的主机权限是单独的字段；您无需在 "permissions" 或 "optional_permissions" 中指定这些权限。

内容脚本仍位于 "content_scripts.matches" 下。如需了解 "content_scripts.matches"，请参阅使用静态声明注入。

可通过网络访问的资源是指可供网页或其他扩展程序访问的扩展程序内的文件。在 Manifest V2 中实现的 "web_accessible_resources" 字段会使网站和攻击者能够检测到扩展程序（前提是扩展程序选择公开资源）。这带来了数字“指纹”收集或意外访问资源的机会。

Manifest V3 通过限制哪些网站和扩展程序可以访问扩展程序中的资源来限制扩展程序的公开范围。现在，您需要提供对象数组，而不是像以前那样提供文件列表，其中每个对象都会将一组资源映射到一组网址或扩展程序 ID。

以下示例比较了 Manifest V2 和 Manifest V3 之间的可访问 Web 资源。在清单 V2 中，默认情况下，所有网站都可以访问指定的资源。在下方显示的 Manifest V3 代码中，这些资源仅适用于 https://example.com，而只有某些图片适用于所有网站。

如需了解详情，请参阅可访问 Web 的资源和匹配模式。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
"manifest_version"
```

Example 4 (unknown):
```unknown
{
  ...
  "manifest_version": 2
  ...
}
```

---

## 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/to-service-workers?hl=zh-cn

**Contents:**
- 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 后台脚本与扩展程序 Service Worker 之间的区别
  - 来自后台页面的更改
  - 您需要进行的更改
- 更新清单中的“background”字段
- 将 DOM 和窗口调用移至屏幕外文档
- 将 localStorage 转换为其他类型
- 同步注册监听器
- 将 XMLHttpRequest() 替换为全局 fetch()
- 保留状态

将背景或事件页面替换为 Service Worker

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码脱离主线程。这样，扩展程序便会仅在需要时运行，从而节省资源。

自推出以来，后台页面一直是扩展程序的基本组成部分。简单来说，后台页面可提供一个独立于任何其他窗口或标签页的环境。这样，扩展程序就可以观察事件并采取相应行动来响应事件。

本页面介绍了将后台网页转换为扩展程序 Service Worker 的任务。如需详细了解扩展程序服务工的一般用法，请参阅教程使用服务工处理事件以及扩展程序服务工简介部分。

在某些情况下，您会看到称为“后台脚本”的扩展程序 Service Worker。虽然扩展程序服务工作线程确实在后台运行，但将其称为后台脚本有点误导性，因为这会暗示它们具有相同的功能。区别将在下面进行介绍。

Service Worker 与后台页面存在许多不同之处。

您需要进行一些代码调整，以应对后台脚本和服务工件运行方式之间的差异。首先，在清单文件中指定服务工件的做法与指定后台脚本的做法不同。此外：

在 Manifest V3 中，后台页面被 Service Worker 取代。下面列出了对清单的更改。

"service_worker" 字段接受单个字符串。只有在使用 ES 模块（使用 import 关键字）时，才需要 "type" 字段。其值始终为 "module"。如需了解详情，请参阅扩展程序服务工件基础知识

某些扩展程序需要访问 DOM 和窗口对象，但无需在视觉上打开新窗口或标签页。Offscreen API 通过打开和关闭与扩展程序打包的未显示文档来支持这些用例，而不会中断用户体验。除了消息传递之外，屏幕外文档不会与其他扩展程序上下文共享 API，而是作为扩展程序可以与之互动的完整网页。

如需使用 Offscreen API，请通过 Service Worker 创建屏幕外文档。

在屏幕外文档中，执行您之前在后台脚本中运行的任何操作。例如，您可以复制在托管网页上选择的文字。

使用消息传递功能在屏幕外文档和扩展程序 Service Worker 之间进行通信。

Web 平台的 Storage 接口（可通过 window.localStorage 访问）不能在 Service Worker 中使用。要解决此问题，请采取以下措施之一。首先，您可以将其替换为对其他存储机制的调用。chrome.storage.local 命名空间适用于大多数用例，但也提供了其他选项。

您还可以将其调用移至屏幕外文档。例如，如需将之前存储在 localStorage 中的数据迁移到其他机制，请使用以下命令：

Web 存储空间 API 在扩展程序中的运作方式也有一些细微之处。如需了解详情，请参阅存储空间和 Cookie。

异步注册监听器（例如在 promise 或回调内）在 Manifest V3 中不一定可行。请参考以下代码。

这适用于持续性后台页面，因为页面会持续运行且永远不会重新初始化。在 Manifest V3 中，系统会在分派事件时重新初始化服务工作器。这意味着，当事件触发时，监听器将不会注册（因为它们是异步添加的），并且系统会错过事件。

请改为将事件监听器注册移至脚本的顶层。这样可以确保 Chrome 能够立即找到并调用操作的点击处理脚本，即使您的扩展程序尚未完成其启动逻辑也是如此。

无法从 Service Worker、扩展程序或其他方式调用 XMLHttpRequest()。将后台脚本对 XMLHttpRequest() 的调用替换为对全局 fetch() 的调用。

Service Worker 是临时的，这意味着它们可能会在用户浏览器会话期间反复启动、运行和终止。这也意味着，由于之前的上下文已被拆解，因此全局变量中的数据无法立即使用。如需解决此问题，请使用存储空间 API 作为可信来源。下面的示例将展示如何执行此操作。

以下示例使用全局变量存储名称。在 Service Worker 中，此变量可能会在用户的浏览器会话期间重置多次。

对于 Manifest V3，将全局变量替换为对 Storage API 的调用。

通常，您可以使用 setTimeout() 或 setInterval() 方法使用延迟或周期性操作。不过，这些 API 在服务工件中可能会失败，因为每当服务工件终止时，计时器都会被取消。

请改用 Alarms API。与其他监听器一样，闹钟监听器应在脚本的顶层注册。

服务工件按定义是事件驱动的，并会在无活动时终止。这样，Chrome 就可以优化扩展程序的性能和内存用量。如需了解详情，请参阅我们的服务工件生命周期文档。在特殊情况下，可能需要采取额外措施来确保服务工件保持长时间活跃状态。

在长时间运行且不调用扩展程序 API 的 Service Worker 操作期间，Service Worker 可能会在操作中途关闭。例如：

在这些情况下，如需延长服务工件生命周期，您可以定期调用一个琐碎的扩展程序 API 来重置超时计数器。请注意，这仅适用于特殊情况，在大多数情况下，通常可以通过更好、符合平台习惯的方法来实现相同的结果。

以下示例展示了一个 waitUntil() 辅助函数，该函数会在给定 promise 解析之前保持服务工作器处于活动状态：

在极少数情况下，需要无限期延长生命周期。我们已将企业和教育领域确定为最大的用例，并在这些领域专门允许这样做，但我们通常不支持这样做。在这些特殊情况下，可以通过定期调用一个简单的扩展程序 API 来保持服务工件保持活跃状态。请务必注意，此建议仅适用于在受管理的设备上运行的企业或教育用例扩展程序。在其他情况下则是不允许的，Chrome 扩展程序团队保留日后对这些扩展程序采取措施的权利。

使用以下代码段可让您的服务工件保持活跃状态：

**Examples:**

Example 1 (unknown):
```unknown
XMLHttpRequest()
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
"background.scripts"
```

Example 4 (unknown):
```unknown
"background.service_worker"
```

---

## 原生消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/native-messaging?hl=zh-cn

**Contents:**
- 原生消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 原生消息传递主机
  - 原生消息传递主机位置
  - 原生消息传递协议
- 连接到原生应用
- 调试原生消息传递

扩展程序可以使用与其他消息传递 API 类似的 API 与原生应用交换消息。支持此功能的原生应用必须注册一个可以与扩展程序通信的原生消息传递主机。Chrome 会在单独的进程中启动主机，并使用标准输入和标准输出流与其通信。

如需注册原生消息传递主机，应用必须保存用于定义原生消息传递主机配置的文件。

原生消息传递主机清单文件必须是有效的 JSON，并且包含以下字段：

在 Windows 上，清单文件可以位于文件系统中的任意位置。应用安装程序必须创建一个注册表项（HKEY_LOCAL_MACHINE\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.my_company.my_application 或 HKEY_CURRENT_USER\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.my_company.my_application），并将该项的默认值设置为清单文件的完整路径。例如，使用以下命令：

当 Chrome 查找原生消息传递主机时，会先查询 32 位注册表，然后再查询 64 位注册表。

在 macOS 和 Linux 上，原生消息传递主机的清单文件的位置因浏览器（Google Chrome 或 Chromium）而异。系统级原生即时通讯主机在固定位置进行查找，而用户级原生即时通讯主机在用户个人资料目录的 NativeMessagingHosts/ 子目录中进行查找。

Chrome 会在单独的进程中启动每个原生消息传递主机，并使用标准输入 (stdin) 和标准输出 (stdout) 与其通信。发送消息时，双方使用相同的格式；每个消息都使用 JSON 进行序列化，编码为 UTF-8，并在前面附加 32 位消息长度（采用原生字节顺序）。来自原生消息主机的单个消息的大小上限为 1 MB，这主要是为了保护 Chrome 免受行为异常的原生应用的影响。发送到原生消息传递主机的消息大小上限为 64 MB。

原生消息传递主机的第一个参数是调用方的来源，通常为 chrome-extension://[ID of allowed extension]。这样一来，当原生消息传递主机清单中的 allowed_origins 键中指定多个扩展程序时，原生消息传递主机便可识别消息来源。

在 Windows 上，系统还会向原生消息传递主机传递一个命令行参数，其中包含对调用 Chrome 原生窗口的句柄：--parent-window=<decimal handle value>。这样，原生消息传递主机就可以创建具有正确父级的原生界面窗口。请注意，如果调用上下文是服务工件，则此值将为 0。

使用 runtime.connectNative() 创建消息传递端口时，Chrome 会启动原生消息传递主机进程，并使其保持运行状态，直到端口被销毁为止。另一方面，如果使用 runtime.sendNativeMessage() 发送消息，而未创建消息端口，Chrome 会为每条消息启动一个新的原生消息传递主机进程。在这种情况下，主机进程生成的第一个消息会被视为对原始请求的响应，Chrome 会将其传递给调用 runtime.sendNativeMessage() 时指定的响应回调。在这种情况下，系统会忽略本地消息传递主机生成的所有其他消息。

向原生应用发送和接收消息与跨扩展程序消息传递非常相似。主要区别在于，使用 runtime.connectNative() 而非 runtime.connect()，以及使用 runtime.sendNativeMessage() 而非 runtime.sendMessage()。

如需使用这些方法，必须在扩展程序的清单文件中声明“nativeMessaging”权限。

这些方法无法在内容脚本中使用，只能在扩展程序的页面和服务工件中使用。如果您希望从内容脚本与原生应用通信，请将消息发送到您的服务工件，以便将其传递给原生应用。

以下示例创建了一个连接到原生消息传递主机 com.my_company.my_application 的 runtime.Port 对象，开始监听该端口中的消息，并发送一条出站消息：

使用 runtime.sendNativeMessage 向原生应用发送消息，而无需创建端口，例如：

当发生某些原生消息传递失败时，输出会写入 Chrome 的错误日志。这包括原生即时通讯主机无法启动、写入 stderr 或违反通信协议的情况。在 Linux 和 macOS 上，您可以通过从命令行启动 Chrome 并在终端中查看其输出来访问此日志。在 Windows 上，请使用 --enable-logging，如如何启用日志记录中所述。

检查您是否有足够的权限来执行原生消息传递主机文件。

检查名称是否包含无效字符。仅允许使用小写字母数字字符、下划线和英文句点。名称不能以英文句点开头或结尾，英文句点后面也不能再跟英文句点。

在 Chrome 读取消息之前，指向原生消息传递主机的管道已断开。这很可能是从原生即时通讯主机发起的。

原生即时通讯主机主机名未注册。（仅限 Windows）

在 Windows 注册表中未找到原生即时通讯主机。使用 regedit 仔细检查密钥是否真的已创建，以及是否符合原生消息传递主机位置中所述的所需格式。

扩展程序的来源是否已列在 allowed_origins 中？

这表示原生消息传递主机中通信协议的实现有误。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "com.my_company.my_application",
  "description": "My Application",
  "path": "C:\\Program Files\\My Application\\chrome_native_messaging_host.exe",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"]
}
```

Example 2 (unknown):
```unknown
{
  "name": "com.my_company.my_application",
  "description": "My Application",
  "path": "C:\\Program Files\\My Application\\chrome_native_messaging_host.exe",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"]
}
```

Example 3 (unknown):
```unknown
runtime.connectNative()
```

Example 4 (unknown):
```unknown
runtime.sendNativeMessage()
```

---

## 更新清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/manifest?hl=zh-cn

**Contents:**
- 更新清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 更改清单版本号
- 更新主持人权限
- 更新网络无障碍资源

manifest.json 文件的格式要求与 Manifest V2 略有不同。本页介绍了仅影响 manifest.json 文件的更改。但是，对脚本和网页进行的许多更改也需要对清单进行更改。这些更改会在需要时通过迁移任务进行处理。

将 "manifest_version" 字段的值从 2 更改为 3。

Manifest V3 中的主机权限是单独的字段；您无需在 "permissions" 或 "optional_permissions" 中指定这些权限。

内容脚本仍位于 "content_scripts.matches" 下。如需了解 "content_scripts.matches"，请参阅使用静态声明注入。

可通过网络访问的资源是指可供网页或其他扩展程序访问的扩展程序内的文件。在 Manifest V2 中实现的 "web_accessible_resources" 字段会使网站和攻击者能够检测到扩展程序（前提是扩展程序选择公开资源）。这带来了数字“指纹”收集或意外访问资源的机会。

Manifest V3 通过限制哪些网站和扩展程序可以访问扩展程序中的资源来限制扩展程序的公开范围。现在，您需要提供对象数组，而不是像以前那样提供文件列表，其中每个对象都会将一组资源映射到一组网址或扩展程序 ID。

以下示例比较了 Manifest V2 和 Manifest V3 之间的可访问 Web 资源。在清单 V2 中，默认情况下，所有网站都可以访问指定的资源。在下方显示的 Manifest V3 代码中，这些资源仅适用于 https://example.com，而只有某些图片适用于所有网站。

如需了解详情，请参阅可访问 Web 的资源和匹配模式。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
"manifest_version"
```

Example 4 (unknown):
```unknown
{
  ...
  "manifest_version": 2
  ...
}
```

---

## 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/to-service-workers?hl=zh-cn

**Contents:**
- 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 后台脚本与扩展程序 Service Worker 之间的区别
  - 来自后台页面的更改
  - 您需要进行的更改
- 更新清单中的“background”字段
- 将 DOM 和窗口调用移至屏幕外文档
- 将 localStorage 转换为其他类型
- 同步注册监听器
- 将 XMLHttpRequest() 替换为全局 fetch()
- 保留状态

将背景或事件页面替换为 Service Worker

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码脱离主线程。这样，扩展程序便会仅在需要时运行，从而节省资源。

自推出以来，后台页面一直是扩展程序的基本组成部分。简单来说，后台页面可提供一个独立于任何其他窗口或标签页的环境。这样，扩展程序就可以观察事件并采取相应行动来响应事件。

本页面介绍了将后台网页转换为扩展程序 Service Worker 的任务。如需详细了解扩展程序服务工的一般用法，请参阅教程使用服务工处理事件以及扩展程序服务工简介部分。

在某些情况下，您会看到称为“后台脚本”的扩展程序 Service Worker。虽然扩展程序服务工作线程确实在后台运行，但将其称为后台脚本有点误导性，因为这会暗示它们具有相同的功能。区别将在下面进行介绍。

Service Worker 与后台页面存在许多不同之处。

您需要进行一些代码调整，以应对后台脚本和服务工件运行方式之间的差异。首先，在清单文件中指定服务工件的做法与指定后台脚本的做法不同。此外：

在 Manifest V3 中，后台页面被 Service Worker 取代。下面列出了对清单的更改。

"service_worker" 字段接受单个字符串。只有在使用 ES 模块（使用 import 关键字）时，才需要 "type" 字段。其值始终为 "module"。如需了解详情，请参阅扩展程序服务工件基础知识

某些扩展程序需要访问 DOM 和窗口对象，但无需在视觉上打开新窗口或标签页。Offscreen API 通过打开和关闭与扩展程序打包的未显示文档来支持这些用例，而不会中断用户体验。除了消息传递之外，屏幕外文档不会与其他扩展程序上下文共享 API，而是作为扩展程序可以与之互动的完整网页。

如需使用 Offscreen API，请通过 Service Worker 创建屏幕外文档。

在屏幕外文档中，执行您之前在后台脚本中运行的任何操作。例如，您可以复制在托管网页上选择的文字。

使用消息传递功能在屏幕外文档和扩展程序 Service Worker 之间进行通信。

Web 平台的 Storage 接口（可通过 window.localStorage 访问）不能在 Service Worker 中使用。要解决此问题，请采取以下措施之一。首先，您可以将其替换为对其他存储机制的调用。chrome.storage.local 命名空间适用于大多数用例，但也提供了其他选项。

您还可以将其调用移至屏幕外文档。例如，如需将之前存储在 localStorage 中的数据迁移到其他机制，请使用以下命令：

Web 存储空间 API 在扩展程序中的运作方式也有一些细微之处。如需了解详情，请参阅存储空间和 Cookie。

异步注册监听器（例如在 promise 或回调内）在 Manifest V3 中不一定可行。请参考以下代码。

这适用于持续性后台页面，因为页面会持续运行且永远不会重新初始化。在 Manifest V3 中，系统会在分派事件时重新初始化服务工作器。这意味着，当事件触发时，监听器将不会注册（因为它们是异步添加的），并且系统会错过事件。

请改为将事件监听器注册移至脚本的顶层。这样可以确保 Chrome 能够立即找到并调用操作的点击处理脚本，即使您的扩展程序尚未完成其启动逻辑也是如此。

无法从 Service Worker、扩展程序或其他方式调用 XMLHttpRequest()。将后台脚本对 XMLHttpRequest() 的调用替换为对全局 fetch() 的调用。

Service Worker 是临时的，这意味着它们可能会在用户浏览器会话期间反复启动、运行和终止。这也意味着，由于之前的上下文已被拆解，因此全局变量中的数据无法立即使用。如需解决此问题，请使用存储空间 API 作为可信来源。下面的示例将展示如何执行此操作。

以下示例使用全局变量存储名称。在 Service Worker 中，此变量可能会在用户的浏览器会话期间重置多次。

对于 Manifest V3，将全局变量替换为对 Storage API 的调用。

通常，您可以使用 setTimeout() 或 setInterval() 方法使用延迟或周期性操作。不过，这些 API 在服务工件中可能会失败，因为每当服务工件终止时，计时器都会被取消。

请改用 Alarms API。与其他监听器一样，闹钟监听器应在脚本的顶层注册。

服务工件按定义是事件驱动的，并会在无活动时终止。这样，Chrome 就可以优化扩展程序的性能和内存用量。如需了解详情，请参阅我们的服务工件生命周期文档。在特殊情况下，可能需要采取额外措施来确保服务工件保持长时间活跃状态。

在长时间运行且不调用扩展程序 API 的 Service Worker 操作期间，Service Worker 可能会在操作中途关闭。例如：

在这些情况下，如需延长服务工件生命周期，您可以定期调用一个琐碎的扩展程序 API 来重置超时计数器。请注意，这仅适用于特殊情况，在大多数情况下，通常可以通过更好、符合平台习惯的方法来实现相同的结果。

以下示例展示了一个 waitUntil() 辅助函数，该函数会在给定 promise 解析之前保持服务工作器处于活动状态：

在极少数情况下，需要无限期延长生命周期。我们已将企业和教育领域确定为最大的用例，并在这些领域专门允许这样做，但我们通常不支持这样做。在这些特殊情况下，可以通过定期调用一个简单的扩展程序 API 来保持服务工件保持活跃状态。请务必注意，此建议仅适用于在受管理的设备上运行的企业或教育用例扩展程序。在其他情况下则是不允许的，Chrome 扩展程序团队保留日后对这些扩展程序采取措施的权利。

使用以下代码段可让您的服务工件保持活跃状态：

**Examples:**

Example 1 (unknown):
```unknown
XMLHttpRequest()
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
"background.scripts"
```

Example 4 (unknown):
```unknown
"background.service_worker"
```

---

## 实现操作 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/implement-action

**Contents:**
- 实现操作 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 注册操作
- 响应操作
- 有条件地启用操作
- 操作标记
- 提示

操作是指用户点击工具栏图标（通常称为扩展程序的操作图标）时发生的情况。操作使用 Action API 调用扩展程序功能或打开弹出式窗口。本页介绍了如何调用扩展程序功能。如需使用弹出式窗口，请参阅添加弹出式窗口。

如需使用 chrome.action API，请将 "action" 键添加到扩展程序的清单文件中。如需详细了解此字段的可选属性，请参阅 chrome.action API 参考文档的清单部分。

为用户点击操作图标时注册 onClicked 处理脚本。如果在 manifest.json 文件中注册了弹出式窗口，系统不会触发此事件。

借助 chrome.declarativeContent API，您可以根据网页网址或当 CSS 选择器与网页上的元素匹配时启用扩展程序的操作图标。当扩展程序的操作图标被停用时，该图标会灰显。如果用户点击已停用的图标，系统会显示扩展程序的上下文菜单。

徽章是放置在操作图标上方的格式化文本，用于指示扩展程序状态或用户需要执行的操作等。为了演示这一点，Drink Water 示例会显示带有“ON”的标记，以向用户表明他们已成功设置闹钟，并且在扩展程序处于空闲状态时不会显示任何内容。徽章最多可包含 4 个字符。

通过调用 chrome.action.setBadgeText() 设置徽章的文本，并通过调用 chrome.action.setBadgeBackgroundColor()` 设置背景颜色。

在 manifest.json 文件的 "action" 键下的 "default_title" 字段中注册提示。

您还可以通过调用 action.setTitle()` 来设置或更新提示。如果未设置任何提示，系统会显示扩展程序的名称。

**Examples:**

Example 1 (unknown):
```unknown
chrome.action
```

Example 2 (unknown):
```unknown
chrome.action
```

Example 3 (unknown):
```unknown
{
  "name": "My Awesome action Extension",
 ...
  "action": {
   ...
  }
 ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My Awesome action Extension",
 ...
  "action": {
   ...
  }
 ...
}
```

---

## 配置扩展程序图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/configure-icons

**Contents:**
- 配置扩展程序图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

扩展程序需要至少一个图标来在工具栏中表示它。提供 以获得最佳视觉效果的图标，尽管任何光栅格式 支持的存储类型其中包括 BMP、GIF、ICO 和 JPEG。

确保您的图标遵循 扩展程序图标最佳做法。 所有图标都应为正方形，否则可能会有失真。如果未提供图标， Chrome 会使用 扩展程序名称。

**Examples:**

Example 1 (unknown):
```unknown
{
 "name": "My Awesome Extension",
 ...
 "icons": {
   "16": "extension_icon16.png",
   "32": "extension_icon32.png",
   "48": "extension_icon48.png",
   "128": "extension_icon128.png"
 }
 ...
}```
```

Example 2 (unknown):
```unknown
{
 "name": "My Awesome Extension",
 ...
 "icons": {
   "16": "extension_icon16.png",
   "32": "extension_icon32.png",
   "48": "extension_icon48.png",
   "128": "extension_icon128.png"
 }
 ...
}```
```

---

## 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/known-issues?hl=zh-cn

**Contents:**
- 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 缩小平台差距
- Manifest V3 常见问题解答

最近，我们宣布了对 Manifest V2 弃用时间表的变更。虽然我们仍会坚定地努力推出 Manifest V3，但也深知我们这方面还有很多工作要做。

我们致力于在宣布新的 Manifest V2 弃用时间表之前弥补以下缺口：

问题是根据合作伙伴、bug 报告和开发者的反馈收集的。我们将继续不断努力，以提高扩展程序平台的稳定性和整体性能。

问：我们计划支持持久性 Service Worker 吗？ 答：从后台脚本迁移到 Service Worker 的一个主要原因是，事件驱动型编程模型的内存效率更高，因为 Service Worker 具有短暂性。因此，我们不打算支持持久性 Service Worker。不过，为了满足扩展程序开发者的具体需求，我们将继续对 Service Worker 进行许多改进。具体而言：

问：有没有办法访问 Service Worker 中的 DOM？ 答：我们遵循 Web 平台的做法，即不在 Web 工作器（包括 Service Worker）中包含 DOM 访问权限。为了支持需要从 Service Worker 进行后台 DOM 访问的用例，我们引入了将后台工作委托给提供完整 DOM 访问权限的短期屏幕外文档的可能性。

问：Manifest V3 是否可以支持远程代码？ 答：为了提高 Chrome 扩展程序的安全性，我们将继续禁止在 Chrome 扩展程序中执行任意远程托管代码。不过，这并不意味着我们会禁止执行各种类型的动态代码。我们仍然支持在 Chrome 扩展程序中动态执行代码的不同选项：

问：我的 Manifest V2 扩展程序依赖于 webRequestBlocking，而 Manifest V3 不支持该技术。我如何继续在 Manifest V3 中提供相同的功能？ 答：我们相信，大多数请求阻塞用例都可以通过新的 declarativeNetRequest API 解决。它还能带来以下好处：避免进程间通信的性能开销、对每个请求执行代码，或者在发送请求时需要活跃的扩展进程。不过，对于复杂的企业（或教育）用例，系统仍然支持动态请求屏蔽。

**Examples:**

Example 1 (unknown):
```unknown
chrome.fileBrowserHandler
```

Example 2 (unknown):
```unknown
permissions.request()
```

Example 3 (unknown):
```unknown
desktopCapture.chooseDesktopMedia()
```

Example 4 (unknown):
```unknown
identity.launchWebAuthFlow()
```

---

## 清单版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/manifest-version

**Contents:**
- 清单版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

一个整数，用于指定您的软件包所需的清单文件格式版本。必须提供此键。例如：

当前版本为 Manifest V3。Chrome 应用商店不再接受 Manifest V2 扩展程序 （如需了解详情，请参阅 Manifest V2 支持时间表）。系统还会提供 版本（V4 及更高版本），但这些映像尚未制定发布计划。

**Examples:**

Example 1 (unknown):
```unknown
"manifest_version": 3
```

Example 2 (unknown):
```unknown
"manifest_version": 3
```

---

## 清单 - 名称 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/name

**Contents:**
- 清单 - 名称 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"name" 键（必需）是一个简短的纯文本字符串（最多 75 个字符） 字符）。例如：

您可以指定特定于语言区域的字符串；请参阅国际化 了解详情。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension name"
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension name"
}
```

---

## 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/known-issues?hl=zh-cn

**Contents:**
- 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 缩小平台差距
- Manifest V3 常见问题解答

最近，我们宣布了对 Manifest V2 弃用时间表的变更。虽然我们仍会坚定地努力推出 Manifest V3，但也深知我们这方面还有很多工作要做。

我们致力于在宣布新的 Manifest V2 弃用时间表之前弥补以下缺口：

问题是根据合作伙伴、bug 报告和开发者的反馈收集的。我们将继续不断努力，以提高扩展程序平台的稳定性和整体性能。

问：我们计划支持持久性 Service Worker 吗？ 答：从后台脚本迁移到 Service Worker 的一个主要原因是，事件驱动型编程模型的内存效率更高，因为 Service Worker 具有短暂性。因此，我们不打算支持持久性 Service Worker。不过，为了满足扩展程序开发者的具体需求，我们将继续对 Service Worker 进行许多改进。具体而言：

问：有没有办法访问 Service Worker 中的 DOM？ 答：我们遵循 Web 平台的做法，即不在 Web 工作器（包括 Service Worker）中包含 DOM 访问权限。为了支持需要从 Service Worker 进行后台 DOM 访问的用例，我们引入了将后台工作委托给提供完整 DOM 访问权限的短期屏幕外文档的可能性。

问：Manifest V3 是否可以支持远程代码？ 答：为了提高 Chrome 扩展程序的安全性，我们将继续禁止在 Chrome 扩展程序中执行任意远程托管代码。不过，这并不意味着我们会禁止执行各种类型的动态代码。我们仍然支持在 Chrome 扩展程序中动态执行代码的不同选项：

问：我的 Manifest V2 扩展程序依赖于 webRequestBlocking，而 Manifest V3 不支持该技术。我如何继续在 Manifest V3 中提供相同的功能？ 答：我们相信，大多数请求阻塞用例都可以通过新的 declarativeNetRequest API 解决。它还能带来以下好处：避免进程间通信的性能开销、对每个请求执行代码，或者在发送请求时需要活跃的扩展进程。不过，对于复杂的企业（或教育）用例，系统仍然支持动态请求屏蔽。

**Examples:**

Example 1 (unknown):
```unknown
chrome.fileBrowserHandler
```

Example 2 (unknown):
```unknown
permissions.request()
```

Example 3 (unknown):
```unknown
desktopCapture.chooseDesktopMedia()
```

Example 4 (unknown):
```unknown
identity.launchWebAuthFlow()
```

---

## 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/known-issues

**Contents:**
- 迁移到 Manifest V3 时的已知问题 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 缩小平台差距
- Manifest V3 常见问题解答

最近，我们宣布了对 Manifest V2 弃用时间表的变更。虽然我们仍会坚定地努力推出 Manifest V3，但也深知我们这方面还有很多工作要做。

我们致力于在宣布新的 Manifest V2 弃用时间表之前弥补以下缺口：

问题是根据合作伙伴、bug 报告和开发者的反馈收集的。我们将继续不断努力，以提高扩展程序平台的稳定性和整体性能。

问：我们计划支持持久性 Service Worker 吗？ 答：从后台脚本迁移到 Service Worker 的一个主要原因是，事件驱动型编程模型的内存效率更高，因为 Service Worker 具有短暂性。因此，我们不打算支持持久性 Service Worker。不过，为了满足扩展程序开发者的具体需求，我们将继续对 Service Worker 进行许多改进。具体而言：

问：有没有办法访问 Service Worker 中的 DOM？ 答：我们遵循 Web 平台的做法，即不在 Web 工作器（包括 Service Worker）中包含 DOM 访问权限。为了支持需要从 Service Worker 进行后台 DOM 访问的用例，我们引入了将后台工作委托给提供完整 DOM 访问权限的短期屏幕外文档的可能性。

问：Manifest V3 是否可以支持远程代码？ 答：为了提高 Chrome 扩展程序的安全性，我们将继续禁止在 Chrome 扩展程序中执行任意远程托管代码。不过，这并不意味着我们会禁止执行各种类型的动态代码。我们仍然支持在 Chrome 扩展程序中动态执行代码的不同选项：

问：我的 Manifest V2 扩展程序依赖于 webRequestBlocking，而 Manifest V3 不支持该技术。我如何继续在 Manifest V3 中提供相同的功能？ 答：我们相信，大多数请求阻塞用例都可以通过新的 declarativeNetRequest API 解决。它还能带来以下好处：避免进程间通信的性能开销、对每个请求执行代码，或者在发送请求时需要活跃的扩展进程。不过，对于复杂的企业（或教育）用例，系统仍然支持动态请求屏蔽。

**Examples:**

Example 1 (unknown):
```unknown
chrome.fileBrowserHandler
```

Example 2 (unknown):
```unknown
permissions.request()
```

Example 3 (unknown):
```unknown
desktopCapture.chooseDesktopMedia()
```

Example 4 (unknown):
```unknown
identity.launchWebAuthFlow()
```

---

## 清单 - 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/content-scripts

**Contents:**
- 清单 - 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 文件
- 匹配网址
  - glob 和网址匹配示例
    - "include_globs"
    - "exclude_globs"
    - 高级自定义示例
- 帧
- 运行时和执行环境

"content_scripts" 键用于指定每次打开网页时使用符合特定网址格式的静态加载 JavaScript 或 CSS 文件。扩展程序还可以以编程方式注入内容脚本。如需了解详情，请参阅注入脚本。

以下是 "content_scripts" 支持的键。只有 "matches" 键以及 "js" 或 "css" 是必需项。

每个文件都必须包含指向扩展程序根目录中资源的相对路径。系统会自动剪除前导斜杠 (/)。"run_at" 键指定每个文件的注入时间。

只有 "matches" 属性是必需的。然后，您可以使用 "exclude_matches"、"include_globs" 和 "exclude_globs" 自定义要将代码注入到的网址。按 "matches" 键将触发警告。

glob 网址是包含“通配符”的网址* 和问号。通配符 * 可匹配任何长度的字符串（包括空字符串），而问号 ?匹配任何单个字符。

"all_frames" 键用于指定是否应将内容脚本注入符合指定网址要求的所有帧。如果设置为 false，则它将仅注入到最顶层的帧。它可与 "match_about_blank" 结合使用，以注入到 about:blank 帧中。

如需注入其他帧（如 data:、blob: 和 filesystem:），请将 "match_origin_as_fallback" 设置为 true。如需了解详情，请参阅在相关帧中注入

默认情况下，系统会在文档及所有资源加载完毕后注入内容脚本，并将其置于网页或其他扩展程序无法访问的专用隔离执行环境中。您可以通过以下键更改这些默认值：

如需构建可在清单中注入内容脚本的扩展程序，请参阅在每个网页上运行教程。

**Examples:**

Example 1 (unknown):
```unknown
"content_scripts"
```

Example 2 (unknown):
```unknown
"content_scripts"
```

Example 3 (unknown):
```unknown
{
 "name": "My extension",
 ...
 "content_scripts": [
   {
     "matches": ["https://*.example.com/*"],
     "css": ["my-styles.css"],
     "js": ["content-script.js"],
     "exclude_matches": ["*://*/*foo*"],
     "include_globs": ["*example.com/???s/*"],
     "exclude_globs": ["*bar*"],     
     "all_frames": false,
     "match_origin_as_fallback": false,
     "match_about_blank": false,
     "run_at": "document_idle",
     "world": "ISOLATED",
   }
 ],
 ...
}
```

Example 4 (unknown):
```unknown
{
 "name": "My extension",
 ...
 "content_scripts": [
   {
     "matches": ["https://*.example.com/*"],
     "css": ["my-styles.css"],
     "js": ["content-script.js"],
     "exclude_matches": ["*://*/*foo*"],
     "include_globs": ["*example.com/???s/*"],
     "exclude_globs": ["*bar*"],     
     "all_frames": false,
     "match_origin_as_fallback": false,
     "match_about_blank": false,
     "run_at": "document_idle",
     "world": "ISOLATED",
   }
 ],
 ...
}
```

---

## 原生消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/native-messaging

**Contents:**
- 原生消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 原生消息传递主机
  - 原生消息传递主机位置
  - 原生消息传递协议
- 连接到原生应用
- 调试原生消息传递

扩展程序可以使用与其他消息传递 API 类似的 API 与原生应用交换消息。支持此功能的原生应用必须注册一个可以与扩展程序通信的原生消息传递主机。Chrome 会在单独的进程中启动主机，并使用标准输入和标准输出流与其通信。

如需注册原生消息传递主机，应用必须保存用于定义原生消息传递主机配置的文件。

原生消息传递主机清单文件必须是有效的 JSON，并且包含以下字段：

在 Windows 上，清单文件可以位于文件系统中的任意位置。应用安装程序必须创建一个注册表项（HKEY_LOCAL_MACHINE\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.my_company.my_application 或 HKEY_CURRENT_USER\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.my_company.my_application），并将该项的默认值设置为清单文件的完整路径。例如，使用以下命令：

当 Chrome 查找原生消息传递主机时，会先查询 32 位注册表，然后再查询 64 位注册表。

在 macOS 和 Linux 上，原生消息传递主机的清单文件的位置因浏览器（Google Chrome 或 Chromium）而异。系统级原生即时通讯主机在固定位置进行查找，而用户级原生即时通讯主机在用户个人资料目录的 NativeMessagingHosts/ 子目录中进行查找。

Chrome 会在单独的进程中启动每个原生消息传递主机，并使用标准输入 (stdin) 和标准输出 (stdout) 与其通信。发送消息时，双方使用相同的格式；每个消息都使用 JSON 进行序列化，编码为 UTF-8，并在前面附加 32 位消息长度（采用原生字节顺序）。来自原生消息主机的单个消息的大小上限为 1 MB，这主要是为了保护 Chrome 免受行为异常的原生应用的影响。发送到原生消息传递主机的消息大小上限为 64 MB。

原生消息传递主机的第一个参数是调用方的来源，通常为 chrome-extension://[ID of allowed extension]。这样一来，当原生消息传递主机清单中的 allowed_origins 键中指定多个扩展程序时，原生消息传递主机便可识别消息来源。

在 Windows 上，系统还会向原生消息传递主机传递一个命令行参数，其中包含对调用 Chrome 原生窗口的句柄：--parent-window=<decimal handle value>。这样，原生消息传递主机就可以创建具有正确父级的原生界面窗口。请注意，如果调用上下文是服务工件，则此值将为 0。

使用 runtime.connectNative() 创建消息传递端口时，Chrome 会启动原生消息传递主机进程，并使其保持运行状态，直到端口被销毁为止。另一方面，如果使用 runtime.sendNativeMessage() 发送消息，而未创建消息端口，Chrome 会为每条消息启动一个新的原生消息传递主机进程。在这种情况下，主机进程生成的第一个消息会被视为对原始请求的响应，Chrome 会将其传递给调用 runtime.sendNativeMessage() 时指定的响应回调。在这种情况下，系统会忽略本地消息传递主机生成的所有其他消息。

向原生应用发送和接收消息与跨扩展程序消息传递非常相似。主要区别在于，使用 runtime.connectNative() 而非 runtime.connect()，以及使用 runtime.sendNativeMessage() 而非 runtime.sendMessage()。

如需使用这些方法，必须在扩展程序的清单文件中声明“nativeMessaging”权限。

这些方法无法在内容脚本中使用，只能在扩展程序的页面和服务工件中使用。如果您希望从内容脚本与原生应用通信，请将消息发送到您的服务工件，以便将其传递给原生应用。

以下示例创建了一个连接到原生消息传递主机 com.my_company.my_application 的 runtime.Port 对象，开始监听该端口中的消息，并发送一条出站消息：

使用 runtime.sendNativeMessage 向原生应用发送消息，而无需创建端口，例如：

当发生某些原生消息传递失败时，输出会写入 Chrome 的错误日志。这包括原生即时通讯主机无法启动、写入 stderr 或违反通信协议的情况。在 Linux 和 macOS 上，您可以通过从命令行启动 Chrome 并在终端中查看其输出来访问此日志。在 Windows 上，请使用 --enable-logging，如如何启用日志记录中所述。

检查您是否有足够的权限来执行原生消息传递主机文件。

检查名称是否包含无效字符。仅允许使用小写字母数字字符、下划线和英文句点。名称不能以英文句点开头或结尾，英文句点后面也不能再跟英文句点。

在 Chrome 读取消息之前，指向原生消息传递主机的管道已断开。这很可能是从原生即时通讯主机发起的。

原生即时通讯主机主机名未注册。（仅限 Windows）

在 Windows 注册表中未找到原生即时通讯主机。使用 regedit 仔细检查密钥是否真的已创建，以及是否符合原生消息传递主机位置中所述的所需格式。

扩展程序的来源是否已列在 allowed_origins 中？

这表示原生消息传递主机中通信协议的实现有误。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "com.my_company.my_application",
  "description": "My Application",
  "path": "C:\\Program Files\\My Application\\chrome_native_messaging_host.exe",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"]
}
```

Example 2 (unknown):
```unknown
{
  "name": "com.my_company.my_application",
  "description": "My Application",
  "path": "C:\\Program Files\\My Application\\chrome_native_messaging_host.exe",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"]
}
```

Example 3 (unknown):
```unknown
runtime.connectNative()
```

Example 4 (unknown):
```unknown
runtime.sendNativeMessage()
```

---

## 清单 - 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/content-scripts?hl=zh-cn

**Contents:**
- 清单 - 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 文件
- 匹配网址
  - glob 和网址匹配示例
    - "include_globs"
    - "exclude_globs"
    - 高级自定义示例
- 帧
- 运行时和执行环境

"content_scripts" 键用于指定每次打开网页时使用符合特定网址格式的静态加载 JavaScript 或 CSS 文件。扩展程序还可以以编程方式注入内容脚本。如需了解详情，请参阅注入脚本。

以下是 "content_scripts" 支持的键。只有 "matches" 键以及 "js" 或 "css" 是必需项。

每个文件都必须包含指向扩展程序根目录中资源的相对路径。系统会自动剪除前导斜杠 (/)。"run_at" 键指定每个文件的注入时间。

只有 "matches" 属性是必需的。然后，您可以使用 "exclude_matches"、"include_globs" 和 "exclude_globs" 自定义要将代码注入到的网址。按 "matches" 键将触发警告。

glob 网址是包含“通配符”的网址* 和问号。通配符 * 可匹配任何长度的字符串（包括空字符串），而问号 ?匹配任何单个字符。

"all_frames" 键用于指定是否应将内容脚本注入符合指定网址要求的所有帧。如果设置为 false，则它将仅注入到最顶层的帧。它可与 "match_about_blank" 结合使用，以注入到 about:blank 帧中。

如需注入其他帧（如 data:、blob: 和 filesystem:），请将 "match_origin_as_fallback" 设置为 true。如需了解详情，请参阅在相关帧中注入

默认情况下，系统会在文档及所有资源加载完毕后注入内容脚本，并将其置于网页或其他扩展程序无法访问的专用隔离执行环境中。您可以通过以下键更改这些默认值：

如需构建可在清单中注入内容脚本的扩展程序，请参阅在每个网页上运行教程。

**Examples:**

Example 1 (unknown):
```unknown
"content_scripts"
```

Example 2 (unknown):
```unknown
"content_scripts"
```

Example 3 (unknown):
```unknown
{
 "name": "My extension",
 ...
 "content_scripts": [
   {
     "matches": ["https://*.example.com/*"],
     "css": ["my-styles.css"],
     "js": ["content-script.js"],
     "exclude_matches": ["*://*/*foo*"],
     "include_globs": ["*example.com/???s/*"],
     "exclude_globs": ["*bar*"],     
     "all_frames": false,
     "match_origin_as_fallback": false,
     "match_about_blank": false,
     "run_at": "document_idle",
     "world": "ISOLATED",
   }
 ],
 ...
}
```

Example 4 (unknown):
```unknown
{
 "name": "My extension",
 ...
 "content_scripts": [
   {
     "matches": ["https://*.example.com/*"],
     "css": ["my-styles.css"],
     "js": ["content-script.js"],
     "exclude_matches": ["*://*/*foo*"],
     "include_globs": ["*example.com/???s/*"],
     "exclude_globs": ["*bar*"],     
     "all_frames": false,
     "match_origin_as_fallback": false,
     "match_about_blank": false,
     "run_at": "document_idle",
     "world": "ISOLATED",
   }
 ],
 ...
}
```

---

## 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest?hl=zh-cn

**Contents:**
- 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 示例
  - 最小清单
  - 注册内容脚本
  - 注入内容脚本
  - 带权限的弹出式窗口
  - 侧边栏
- 清单键
  - 扩展程序平台所需的密钥
  - Chrome 应用商店所需的密钥

每个扩展程序的根目录中都必须有一个 manifest.json 文件，其中列出了与该扩展程序的结构和行为相关的重要信息。本页介绍了扩展程序清单的结构以及它们可以包含的功能。

以下示例清单展示了基本清单结构和一些常用功能，可作为创建您自己的清单的起点：

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Run script automatically",
  "description": "Runs a script on www.example.com automatically when user installs the extension",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "content_scripts": [
    {
      "js": [
        "content-script.js"
      ],
      "matches": [
        "http://*.example.com//"
      ]
    }
  ]
}
```

---

## 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest

**Contents:**
- 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 示例
  - 最小清单
  - 注册内容脚本
  - 注入内容脚本
  - 带权限的弹出式窗口
  - 侧边栏
- 清单键
  - 扩展程序平台所需的密钥
  - Chrome 应用商店所需的密钥

每个扩展程序的根目录中都必须有一个 manifest.json 文件，其中列出了与该扩展程序的结构和行为相关的重要信息。本页介绍了扩展程序清单的结构以及它们可以包含的功能。

以下示例清单展示了基本清单结构和一些常用功能，可作为创建您自己的清单的起点：

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Run script automatically",
  "description": "Runs a script on www.example.com automatically when user installs the extension",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "content_scripts": [
    {
      "js": [
        "content-script.js"
      ],
      "matches": [
        "http://*.example.com//"
      ]
    }
  ]
}
```

---

## chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/action?hl=zh-cn

**Contents:**
- chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 清单
- 概念和用法
  - 界面组成部分
    - 图标
    - 提示（标题）
    - 徽章
    - 弹出式窗口

使用 chrome.action API 控制 Google Chrome 工具栏中的扩展程序图标。

如需使用此 API，必须在清单中声明以下键。

如需使用 chrome.action API，请指定 "manifest_version" 为 3，并在清单文件中添加 "action" 密钥。

"action" 键（及其子键）是可选的。如果未包含此元素，扩展程序仍会显示在工具栏中，以便用户访问扩展程序的菜单。因此，我们建议您始终至少包含 "action" 和 "default_icon" 键。

该图标是扩展程序工具栏上的主要图片，由清单的 "action" 键中的 "default_icon" 键设置。图标的宽度和高度必须为 16 个与设备无关的像素 (DIP)。

"default_icon" 键是一个包含大小到图片路径的字典。Chrome 会使用这些图标来选择要使用的图片缩放比例。如果找不到完全匹配的图片，Chrome 会选择最接近的可用图片并将其缩放为适合的尺寸，这可能会影响图片质量。

由于具有 1.5 倍或 1.2 倍等不太常见缩放比例的设备越来越普遍，我们建议您为图标提供多种尺寸。这还可以确保您的扩展程序在未来能够应对潜在的图标显示大小变化。不过，如果只提供一种尺寸，也可以将 "default_icon" 键设置为指向单个图标路径的字符串，而不是字典。

您还可以通过指定其他图片路径或使用 HTML canvas 元素（如果从扩展程序服务工作线程进行设置，则使用 offscreen canvas API）提供动态生成的图标，以通过编程方式调用 action.setIcon() 来设置扩展程序的图标。

对于打包的扩展程序（从 .crx 文件安装），图片可以采用 Blink 渲染引擎可以显示的大多数格式，包括 PNG、JPEG、BMP、ICO 等。不支持 SVG。 未打包的扩展程序必须使用 PNG 图片。

当用户将鼠标指针悬停在工具栏中的扩展程序图标上时，系统会显示提示或标题。当按钮获得焦点时，屏幕阅读器朗读的无障碍文本中也会包含该文本。

默认提示是通过 manifest.json 中 "action" 键的 "default_title" 字段设置的。您还可以通过调用 action.setTitle() 以编程方式进行设置。

操作可以选择性地显示“徽章”，即叠加在图标上的一小段文字。这样，您就可以更新操作，以显示有关扩展程序状态的少量信息，例如计数器。徽章包含文本组件和背景颜色。由于空间有限，我们建议徽章文字不超过 4 个字符。

如需创建徽章，请通过调用 action.setBadgeBackgroundColor() 和 action.setBadgeText() 以编程方式进行设置。清单中没有默认的徽章设置。徽章颜色值可以是介于 0 到 255 之间的四个整数组成的数组，用于构成徽章的 RGBA 颜色，也可以是具有 CSS 颜色值的字符串。

当用户点击工具栏中的扩展程序操作按钮时，系统会显示相应操作的弹出式窗口。弹出式窗口可以包含您喜欢的任何 HTML 内容，并且会自动调整大小以适应其内容。弹出式窗口的尺寸必须介于 25x25 像素和 800x600 像素之间。

弹出式窗口最初由 manifest.json 文件中 "action" 键内的 "default_popup" 属性设置。如果存在，此属性应指向扩展程序目录中的相对路径。您还可以使用 action.setPopup() 方法动态更新该属性，使其指向其他相对路径。

扩展操作在每个标签页中可以处于不同的状态。如需为各个标签页设置值，请使用 action API 设置方法中的 tabId 属性。例如，如需为特定标签页设置徽章文字，请执行类似以下操作：

如果省略 tabId 属性，则该设置会被视为全局设置。标签页专用设置优先于全局设置。

默认情况下，工具栏操作在每个标签页上均处于启用状态（可点击）。您可以在清单的 action 键中设置 default_state 属性，以更改此默认设置。如果 default_state 设置为 "disabled"，则该操作默认处于停用状态，必须以编程方式启用才能点击。如果 default_state 设置为 "enabled"（默认值），则默认情况下操作处于启用状态且可点击。

您可以使用 action.enable() 和 action.disable() 方法以编程方式控制状态。这只会影响是否向扩展程序发送弹出式窗口（如果有）或 action.onClicked 事件；不会影响工具栏中操作的存在。

以下示例展示了在扩展程序中使用操作的一些常见方式。如需试用此 API，请从 chrome-extension-samples 代码库安装 Action API 示例。

扩展程序通常会在用户点击扩展程序的操作时显示弹出式窗口。如需在您自己的扩展程序中实现此功能，请在 manifest.json 中声明弹出式窗口，并指定 Chrome 应在弹出式窗口中显示的内容。

扩展程序的常见模式是使用扩展程序的操作公开其主要功能。以下示例演示了此模式。当用户点击操作时，扩展程序会将内容脚本注入到当前网页中。然后，内容脚本会显示一个提醒，以验证一切是否按预期运行。

此示例展示了扩展程序的后台逻辑如何 (a) 默认停用某项操作，以及 (b) 使用 declarativeContent 在特定网站上启用该操作。

要在其中打开操作弹出式窗口的窗口的 ID。如果未指定，则默认为当前活跃窗口。

要查询状态的标签页的 ID。如果未指定任何标签页，则返回非标签页专用状态。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

为标签页启用操作。默认情况下，操作处于启用状态。

Promise<extensionTypes.ColorArray>

获取操作的徽章文本。如果未指定任何标签页，则返回非标签页特定的徽章文字。如果启用了 displayActionCountAsBadgeText，则除非存在 declarativeNetRequestFeedback 权限或提供了标签页专用徽章文本，否则系统会返回占位文本。

Promise<extensionTypes.ColorArray>

获取设置为相应操作的弹出式窗口的 HTML 文档。

Promise<UserSettings>

指示扩展程序操作是否已针对某个标签页启用（如果未提供 tabId，则表示已全局启用）。仅使用 declarativeContent 启用的操作始终返回 false。

打开扩展程序的弹出式窗口。在 Chrome 118 和 Chrome 126 之间，此功能仅适用于根据政策安装的扩展程序。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

可以传递任意数量的字符，但空间中只能容纳大约 4 个字符。如果传递的是空字符串 ('')，则会清除标记文本。如果指定了 tabId，但 text 为 null，则指定标签页的文字会被清除，并默认设为全局徽章文字。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。如果不设置此值，系统会自动选择与徽章背景颜色形成对比的颜色，以便显示文字。如果颜色的 Alpha 值相当于 0，则不会设置该颜色，并且会返回错误。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

为操作设置图标。图标可以指定为图片文件的路径、画布元素的像素数据，也可以指定为包含其中任一信息的字典。必须指定 path 或 imageData 属性。

要设置的图标，可以是 ImageData 对象，也可以是表示图标的字典 {size -> ImageData}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.imageData = foo”等同于“details.imageData = {'16': foo}”

相对图片路径或指向要设置的图标的字典 {size -> relative image path}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.path = foo”等同于“details.path = {'16': foo}”

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

设置 HTML 文档，以便在用户点击操作的图标时将其作为弹出式窗口打开。

要在弹出式窗口中显示的 HTML 文件的相对路径。如果设置为空字符串 ('')，则不显示任何弹出式窗口。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

在用户点击操作图标时触发。如果操作具有弹出式窗口，则不会触发此事件。

在与扩展程序操作相关的用户指定设置发生更改时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.action
```

Example 2 (unknown):
```unknown
chrome.action
```

Example 3 (unknown):
```unknown
"manifest_version"
```

Example 4 (unknown):
```unknown
{
  "name": "Action Extension",
  ...
  "action": {
    "default_icon": {              // optional
      "16": "images/icon16.png",   // optional
      "24": "images/icon24.png",   // optional
      "32": "images/icon32.png"    // optional
    },
    "default_title": "Click Me",   // optional, shown in tooltip
    "default_popup": "popup.html"  // optional
  },
  ...
}
```

---

## 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/improve-security?hl=zh-cn

**Contents:**
- 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 移除执行任意字符串
- 移除远程托管的代码
  - 配置驱动型功能和逻辑
  - 使用远程服务的外部化逻辑
  - 在沙盒化 iframe 中嵌入远程托管的代码
  - 捆绑第三方库
  - 在标签页注入的脚本中使用外部库
  - 注入函数
  - 寻找其他解决方法

这是介绍不属于扩展程序服务工作线程的代码所需更改的第三部分。其中介绍了提高扩展程序安全性所需的更改。另外两个部分介绍了升级到 Manifest V3 所需的更新代码和替换屏蔽 Web 请求。

您无法再使用 executeScript()、eval() 和 new Function() 执行外部逻辑。

executeScript() 方法现在位于 scripting 命名空间中，而不是 tabs 命名空间中。如需了解如何更新通话，请参阅移动 executeScript()。

在少数特殊情况下，仍然可以执行任意字符串：

在 Manifest V3 中，扩展程序的所有逻辑都必须包含在扩展程序软件包中。根据 Chrome 应用商店政策，您将无法再加载和执行远程托管的文件。例如：

您可以采用其他方法，具体取决于您的用例和远程托管的原因。本部分介绍了可考虑的方法。如果您在处理远程托管代码时遇到问题，可参阅相关指南。

您的扩展程序会在运行时加载并缓存远程配置（例如 JSON 文件）。缓存的配置决定了启用了哪些功能。

您的扩展程序调用远程 Web 服务。这样，您就可以将代码保持私密状态，并根据需要进行更改，同时避免重新提交到 Chrome 应用商店的额外开销。

沙盒化 iframe 支持远程托管的代码。请注意，如果代码需要访问嵌入页面的 DOM，则此方法不起作用。

如果您使用的是之前从外部服务器加载的流行框架（例如 React 或 Bootstrap），则可以下载缩小的文件，将其添加到您的项目并在本地导入。例如：

如需在 Service Worker 中加入库，请在清单中将 "background.type" 键设置为 "module"，并使用 import 语句。

您还可以在运行时加载外部库，只需在调用 scripting.executeScript() 时将外部库添加到 files 数组即可。您仍然可以在运行时远程加载数据。

如果您需要更加生动，可以使用 scripting.executeScript() 中的新 func 属性来注入作为内容脚本的函数，并使用 args 属性传递变量。

在后台 Service Worker 中。

Chrome 扩展程序示例代码库包含一个函数注入示例，您可以逐步演示该示例。如需查看 getCurrentTab() 的示例，请参阅该函数的参考文档。

如果上述方法对您的用例没有帮助，您可能需要寻找替代解决方案（例如迁移到其他库），或者寻找其他方法来使用该库的功能。例如，对于 Google Analytics，您可以改用 Google Measurement Protocol，而不是使用 Google Analytics 4 指南中所述的官方远程托管 JavaScript 版本。

"content_security_policy" 尚未从 manifest.json 文件中移除，但它现在是一个支持两个属性的字典："extension_pages" 和 "sandbox"。

extension_pages：是指扩展程序中的上下文，包括 HTML 文件和 Service Worker。

sandbox：是指您的扩展程序使用的任何沙盒化扩展程序页面。

Manifest V3 不允许在 "extension_pages" 字段中使用 Manifest V2 允许使用的某些内容安全政策值。具体而言，Manifest V3 禁止使用允许远程执行的代码。script-src, object-src 和 worker-src 指令只能具有以下值：

sandbox 的内容安全政策值没有此类新限制。

**Examples:**

Example 1 (unknown):
```unknown
executeScript()
```

Example 2 (unknown):
```unknown
new Function()
```

Example 3 (unknown):
```unknown
chrome.runtime.getURL()
```

Example 4 (unknown):
```unknown
new Function(...)
```

---

## 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/web_accessible_resources?hl=zh-cn

**Contents:**
- 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明
- 资源的导航性
- 示例

可通过网络访问的资源是指可供网页或其他扩展程序访问的扩展程序内的文件。附加信息通常会使用此功能显示需要 但扩展程序捆绑包中包含的任何资源均可设为网页可访问。

默认情况下，所有资源都无法在网络上访问，因为恶意网站可以利用这一点指纹用户已安装的扩展程序 或利用已安装的扩展程序中的漏洞（例如 XSS bug）。仅从扩展程序的来源加载的网页或脚本 可以访问该扩展程序的资源。

使用 web_accessible_resources 清单属性声明要公开哪些资源以及要公开到哪些来源。此属性是一个对象数组，用于声明资源访问规则。每个对象都会将一组扩展程序资源映射到一组可访问这些资源的网址和/或扩展程序 ID。

每个元素都必须包含一个 "resources" 元素以及一个 "matches" 或 "extension_ids" 元素。这会建立一个映射，以将指定资源公开到与该格式匹配的网页或到具有匹配 ID 的扩展程序。"use_dynamic_url" 元素是可选的。

可通过网址在网页中获取资源 chrome-extension://[PACKAGE ID]/[PATH]，可使用 runtime.getURL() 生成 方法。这些资源会附带适当的 CORS 标头提供，因此可通过 fetch() 使用。

系统会禁止从网站源导航到扩展程序资源，除非相应资源 列为可通过网络访问请注意以下特殊情况：

网络无障碍资源示例演示了如何在有效的扩展程序中使用此元素。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 4 (unknown):
```unknown
"resources"
```

---

## event_rules 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/event-rules

**Contents:**
- event_rules 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 将规则从 JavaScript 转换为清单

event_rules 清单属性提供了一种机制来添加用于拦截、屏蔽或 使用 declarativeWebRequest 修改正在运行的网络请求，或根据 而无需使用 declarativeContent。

下面定义了一个规则，如果当前网页的 JavaScript：

**Examples:**

Example 1 (unknown):
```unknown
event_rules
```

Example 2 (unknown):
```unknown
chrome.declarativeContent.onPageChanged.addRules([{
  actions: [
    new chrome.declarativeContent.ShowPageAction()
  ],
  conditions: [
    new chrome.declarativeContent.PageStateMatcher(
        {css: ["video"]}
    )
  ]
}]);
```

Example 3 (unknown):
```unknown
chrome.declarativeContent.onPageChanged.addRules([{
  actions: [
    new chrome.declarativeContent.ShowPageAction()
  ],
  conditions: [
    new chrome.declarativeContent.PageStateMatcher(
        {css: ["video"]}
    )
  ]
}]);
```

Example 4 (unknown):
```unknown
{
  "name": "Sample extension",
  "event_rules": [{
    "event": "declarativeContent.onPageChanged",
    "actions": [{
      "type": "declarativeContent.ShowPageAction"
    }],
    "conditions": [{
      "type": "declarativeContent.PageStateMatcher",
      "css": ["video"]
    }]
  }],
  ...
}
```

---

## 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/web-accessible-resources?hl=zh-cn

**Contents:**
- 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明
- 资源的导航性
- 示例

可通过网络访问的资源是指可供网页或其他扩展程序访问的扩展程序内的文件。附加信息通常会使用此功能显示需要 但扩展程序捆绑包中包含的任何资源均可设为网页可访问。

默认情况下，所有资源都无法在网络上访问，因为恶意网站可以利用这一点指纹用户已安装的扩展程序 或利用已安装的扩展程序中的漏洞（例如 XSS bug）。仅从扩展程序的来源加载的网页或脚本 可以访问该扩展程序的资源。

使用 web_accessible_resources 清单属性声明要公开哪些资源以及要公开到哪些来源。此属性是一个对象数组，用于声明资源访问规则。每个对象都会将一组扩展程序资源映射到一组可访问这些资源的网址和/或扩展程序 ID。

每个元素都必须包含一个 "resources" 元素以及一个 "matches" 或 "extension_ids" 元素。这会建立一个映射，以将指定资源公开到与该格式匹配的网页或到具有匹配 ID 的扩展程序。"use_dynamic_url" 元素是可选的。

可通过网址在网页中获取资源 chrome-extension://[PACKAGE ID]/[PATH]，可使用 runtime.getURL() 生成 方法。这些资源会附带适当的 CORS 标头提供，因此可通过 fetch() 使用。

系统会禁止从网站源导航到扩展程序资源，除非相应资源 列为可通过网络访问请注意以下特殊情况：

网络无障碍资源示例演示了如何在有效的扩展程序中使用此元素。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 4 (unknown):
```unknown
"resources"
```

---

## 跨源 opener 政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/cross_origin_opener_policy?hl=zh-cn

**Contents:**
- 跨源 opener 政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明

借助 cross_origin_opener_policy 清单键，扩展程序可以指定 针对扩展程序的请求的 Cross-Origin-Opener-Policy (COOP) 响应标头 来源。这包括扩展程序的 Service Worker、弹出式窗口、选项页面、打开某个扩展程序资源的标签页等。

此密钥与 cross_origin_embedder_policy 结合使用，可允许扩展程序选择启用 跨域隔离

cross_origin_opener_policy 清单键包含一个对象，该对象包含一个 名为 value 的属性，该属性接受字符串。Chrome 会将此字符串用作 Cross-Origin-Opener-Policy 标头。例如：

**Examples:**

Example 1 (unknown):
```unknown
cross_origin_opener_policy
```

Example 2 (unknown):
```unknown
cross_origin_opener_policy
```

Example 3 (unknown):
```unknown
Cross-Origin-Opener-Policy
```

Example 4 (unknown):
```unknown
{
    ...
    "cross_origin_opener_policy": {
      "value": "same-origin"
    },
    ...
}
```

---

## 共享模块 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/shared-modules

**Contents:**
- 共享模块 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
  - 导出
  - 导入
- 访问资源
- 安装 / 卸载

共享模块是无需权限的资源集合，可在 。共享模块的常见用途包括：

通过两个清单字段使用共享模块："export" 和 "import"。

export 字段表示扩展程序是导出其资源的共享模块：

扩展程序和应用使用 import 字段来声明它们依赖于 共享模块：

共享模块资源由根目录中的预留路径 _modules/SHARED_MODULE_ID 访问 。例如，若要添加来自共享模块 foo.js 的脚本， ID 为“cccccccccccccccccccccccccccccc”，请使用您的扩展程序根目录中的以下路径：

如果导入扩展程序的 ID 为“aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa”，则资源的完整网址 为：

请注意，由于共享模块中的资源会叠加到 扩展程序，授予导入扩展程序的所有权限都适用于“共享”中的代码 模块。此外，共享模块可以使用 绝对路径。

共享模块会在相关扩展程序需要时从 Chrome 应用商店自动安装，并会在引用它的最后一个扩展程序卸载时自动卸载。 要上传使用共享模块的扩展程序，必须在以下位置发布共享模块： Chrome 应用商店和扩展程序不得通过其 许可名单。

在开发过程中，您需要手动安装您的扩展程序使用的所有共享模块。 对于旁加载或解压出来的扩展程序，系统不会自动安装 。对于本地安装的未封装共享模块，您必须使用 key 字段 确保共享模块使用正确的 ID。

**Examples:**

Example 1 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Shared Module",
  "export": {
    // Optional list of extension IDs explicitly allowed to
    // import this Shared Module's resources.  If no allowlist
    // is given, all extensions are allowed to import it.
    "allowlist": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ]
  }
  // Note: no permissions are allowed in Shared Modules
}
```

Example 2 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Shared Module",
  "export": {
    // Optional list of extension IDs explicitly allowed to
    // import this Shared Module's resources.  If no allowlist
    // is given, all extensions are allowed to import it.
    "allowlist": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ]
  }
  // Note: no permissions are allowed in Shared Modules
}
```

Example 3 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Importing Extension",
  ...
  "import": [
    {"id": "cccccccccccccccccccccccccccccccc"},
    {"id": "dddddddddddddddddddddddddddddddd"
     "minimum_version": "0.5" // optional
    },
  ]
}
```

Example 4 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Importing Extension",
  ...
  "import": [
    {"id": "cccccccccccccccccccccccccccccccc"},
    {"id": "dddddddddddddddddddddddddddddddd"
     "minimum_version": "0.5" // optional
    },
  ]
}
```

---

## Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/hello-world

**Contents:**
- Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- Hello World
- 加载未打包的扩展程序
- 固定扩展程序
- 重新加载扩展程序
  - 何时重新加载扩展程序
- 查找控制台日志和错误
  - 控制台日志
  - 错误日志

通过构建您的第一个“Hello World”扩展程序，了解 Chrome 扩展程序开发的基础知识。

您将创建一个“Hello World”示例，在本地加载扩展程序，查找日志，并探索其他建议。

当用户点击扩展程序工具栏图标时，此扩展程序将显示“Hello Extensions”。

首先，创建一个用于存储扩展程序文件的新目录。如果您愿意，也可以从 GitHub 下载完整源代码。

接下来，在此目录中创建一个名为 manifest.json 的新文件。此 JSON 文件描述了扩展程序的功能和配置。例如，大多数清单文件都包含 "action" 键，用于声明 Chrome 应将哪张图片用作扩展程序的操作图标，以及在用户点击扩展程序的操作图标时在弹出式窗口中显示的 HTML 网页。

将图标下载到您的目录中，并务必更改其名称，使其与 "default_icon" 键中的名称一致。

针对弹出式窗口，创建一个名为 hello.html 的文件，并添加以下代码：

现在，当用户点击扩展程序的操作图标（工具栏图标）时，该扩展程序会显示一个弹出式窗口。您可以通过在本地加载该测试页面来测试它。确保所有文件均已保存。

如需在开发者模式下加载未封装的扩展程序，请执行以下操作：

大功告成！扩展程序已成功安装。如果清单中未包含任何扩展程序图标，系统会为扩展程序创建一个通用图标。

默认情况下，当您在本地加载扩展程序时，它会显示在扩展程序菜单 () 中。将扩展程序固定到工具栏，以便在开发过程中快速访问扩展程序。

点击扩展程序的操作图标（工具栏图标）；您应该会看到一个弹出式窗口。

返回代码，然后在清单中将扩展程序的名称更改为“Hello Extensions of the world!”。

保存文件后，您还必须刷新扩展程序，才能在浏览器中看到此更改。前往“附加信息”页面，然后点击开启/关闭切换开关旁边的刷新图标：

下表显示了哪些组件需要重新加载才能看到更改：

在开发期间，您可以通过访问浏览器控制台日志来调试代码。在本例中，我们将找到弹出式窗口的日志。首先，将脚本标记添加到 hello.html。

创建一个 popup.js 文件，并添加以下代码。

如需在控制台中查看系统记录的这条消息，请执行以下操作：

现在，我们来破坏一下扩展程序。为此，我们可以移除 popup.js 中的闭引号：

前往“扩展程序”页面，然后打开弹出式窗口。系统随即会显示一个错误按钮。

如需详细了解如何调试服务工件、选项页面和内容脚本，请参阅调试扩展程序。

您可以通过多种方式构建扩展程序项目；不过，唯一的前提是将 manifest.json 文件放在扩展程序的根目录中，如以下示例所示：

如果您使用代码编辑器进行开发，则可以使用 npm 软件包 chrome-types 来利用 Chrome API 的自动补全功能。当 Chromium 源代码发生变化时，此 npm 软件包会自动更新。

选择以下任一教程，开始您的扩展程序学习之旅。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 4 (unknown):
```unknown
"default_icon"
```

---

## 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/to-service-workers

**Contents:**
- 迁移到 Service Worker 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 后台脚本与扩展程序 Service Worker 之间的区别
  - 来自后台页面的更改
  - 您需要进行的更改
- 更新清单中的“background”字段
- 将 DOM 和窗口调用移至屏幕外文档
- 将 localStorage 转换为其他类型
- 同步注册监听器
- 将 XMLHttpRequest() 替换为全局 fetch()
- 保留状态

将背景或事件页面替换为 Service Worker

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码脱离主线程。这样，扩展程序便会仅在需要时运行，从而节省资源。

自推出以来，后台页面一直是扩展程序的基本组成部分。简单来说，后台页面可提供一个独立于任何其他窗口或标签页的环境。这样，扩展程序就可以观察事件并采取相应行动来响应事件。

本页面介绍了将后台网页转换为扩展程序 Service Worker 的任务。如需详细了解扩展程序服务工的一般用法，请参阅教程使用服务工处理事件以及扩展程序服务工简介部分。

在某些情况下，您会看到称为“后台脚本”的扩展程序 Service Worker。虽然扩展程序服务工作线程确实在后台运行，但将其称为后台脚本有点误导性，因为这会暗示它们具有相同的功能。区别将在下面进行介绍。

Service Worker 与后台页面存在许多不同之处。

您需要进行一些代码调整，以应对后台脚本和服务工件运行方式之间的差异。首先，在清单文件中指定服务工件的做法与指定后台脚本的做法不同。此外：

在 Manifest V3 中，后台页面被 Service Worker 取代。下面列出了对清单的更改。

"service_worker" 字段接受单个字符串。只有在使用 ES 模块（使用 import 关键字）时，才需要 "type" 字段。其值始终为 "module"。如需了解详情，请参阅扩展程序服务工件基础知识

某些扩展程序需要访问 DOM 和窗口对象，但无需在视觉上打开新窗口或标签页。Offscreen API 通过打开和关闭与扩展程序打包的未显示文档来支持这些用例，而不会中断用户体验。除了消息传递之外，屏幕外文档不会与其他扩展程序上下文共享 API，而是作为扩展程序可以与之互动的完整网页。

如需使用 Offscreen API，请通过 Service Worker 创建屏幕外文档。

在屏幕外文档中，执行您之前在后台脚本中运行的任何操作。例如，您可以复制在托管网页上选择的文字。

使用消息传递功能在屏幕外文档和扩展程序 Service Worker 之间进行通信。

Web 平台的 Storage 接口（可通过 window.localStorage 访问）不能在 Service Worker 中使用。要解决此问题，请采取以下措施之一。首先，您可以将其替换为对其他存储机制的调用。chrome.storage.local 命名空间适用于大多数用例，但也提供了其他选项。

您还可以将其调用移至屏幕外文档。例如，如需将之前存储在 localStorage 中的数据迁移到其他机制，请使用以下命令：

Web 存储空间 API 在扩展程序中的运作方式也有一些细微之处。如需了解详情，请参阅存储空间和 Cookie。

异步注册监听器（例如在 promise 或回调内）在 Manifest V3 中不一定可行。请参考以下代码。

这适用于持续性后台页面，因为页面会持续运行且永远不会重新初始化。在 Manifest V3 中，系统会在分派事件时重新初始化服务工作器。这意味着，当事件触发时，监听器将不会注册（因为它们是异步添加的），并且系统会错过事件。

请改为将事件监听器注册移至脚本的顶层。这样可以确保 Chrome 能够立即找到并调用操作的点击处理脚本，即使您的扩展程序尚未完成其启动逻辑也是如此。

无法从 Service Worker、扩展程序或其他方式调用 XMLHttpRequest()。将后台脚本对 XMLHttpRequest() 的调用替换为对全局 fetch() 的调用。

Service Worker 是临时的，这意味着它们可能会在用户浏览器会话期间反复启动、运行和终止。这也意味着，由于之前的上下文已被拆解，因此全局变量中的数据无法立即使用。如需解决此问题，请使用存储空间 API 作为可信来源。下面的示例将展示如何执行此操作。

以下示例使用全局变量存储名称。在 Service Worker 中，此变量可能会在用户的浏览器会话期间重置多次。

对于 Manifest V3，将全局变量替换为对 Storage API 的调用。

通常，您可以使用 setTimeout() 或 setInterval() 方法使用延迟或周期性操作。不过，这些 API 在服务工件中可能会失败，因为每当服务工件终止时，计时器都会被取消。

请改用 Alarms API。与其他监听器一样，闹钟监听器应在脚本的顶层注册。

服务工件按定义是事件驱动的，并会在无活动时终止。这样，Chrome 就可以优化扩展程序的性能和内存用量。如需了解详情，请参阅我们的服务工件生命周期文档。在特殊情况下，可能需要采取额外措施来确保服务工件保持长时间活跃状态。

在长时间运行且不调用扩展程序 API 的 Service Worker 操作期间，Service Worker 可能会在操作中途关闭。例如：

在这些情况下，如需延长服务工件生命周期，您可以定期调用一个琐碎的扩展程序 API 来重置超时计数器。请注意，这仅适用于特殊情况，在大多数情况下，通常可以通过更好、符合平台习惯的方法来实现相同的结果。

以下示例展示了一个 waitUntil() 辅助函数，该函数会在给定 promise 解析之前保持服务工作器处于活动状态：

在极少数情况下，需要无限期延长生命周期。我们已将企业和教育领域确定为最大的用例，并在这些领域专门允许这样做，但我们通常不支持这样做。在这些特殊情况下，可以通过定期调用一个简单的扩展程序 API 来保持服务工件保持活跃状态。请务必注意，此建议仅适用于在受管理的设备上运行的企业或教育用例扩展程序。在其他情况下则是不允许的，Chrome 扩展程序团队保留日后对这些扩展程序采取措施的权利。

使用以下代码段可让您的服务工件保持活跃状态：

**Examples:**

Example 1 (unknown):
```unknown
XMLHttpRequest()
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
"background.scripts"
```

Example 4 (unknown):
```unknown
"background.service_worker"
```

---

## 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate

**Contents:**
- 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保留当前的功能集
- 新的扩展程序平台功能

将 Manifest V2 扩展程序转换为 Manifest V3 扩展程序的指南。

此部分可帮助您将扩展程序从 Manifest V2 升级到 Manifest V3（Chrome 扩展程序平台的最新版本）。迁移工作大致分为以下几类。为帮助您跟踪工作进度，我们提供了一份核对清单，总结了这些文档的内容。您可以通过核对清单查看相关内容，也可以深入了解相关内容。两个路径均以升级版附加信息结尾。

我们还提供 Extension Manifest Converter。它无法为您提供一切服务，但可帮助您入门。转换器的 README 文件中介绍了工具更改的内容。

为了降低出现意外问题或 bug 的可能性，我们建议不要在迁移时添加新功能。例如，添加需要新权限的功能可能会触发权限警告，这会导致您的扩展程序停用，直到用户接受新权限。请参阅权限警告最佳做法，了解如何在不显示警告的情况下添加权限。

Chrome 88 或更高版本通常支持 Manifest V3。更新 API 调用时，您可能会发现替换功能可能要到版本 88 之后才在 Chrome 中推出。API 参考页面包含各 API 成员的支持信息。如果您发现需要使用其中某项功能，可以在清单文件中指定最低 Chrome 版本。

自 Manifest V3 发布以来，我们不断添加新功能，其中许多功能在 Manifest V2 和 Manifest V3 中均可使用。在转换时，您并不需要使用这些组件；但是，当它们取代旧功能时，您应优先使用这些功能而不是它们所取代的功能，并且预计被替换的功能最终会被弃用和移除。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

---

## 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/web-accessible-resources

**Contents:**
- 清单 - 网络可访问的资源 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明
- 资源的导航性
- 示例

可通过网络访问的资源是指可供网页或其他扩展程序访问的扩展程序内的文件。附加信息通常会使用此功能显示需要 但扩展程序捆绑包中包含的任何资源均可设为网页可访问。

默认情况下，所有资源都无法在网络上访问，因为恶意网站可以利用这一点指纹用户已安装的扩展程序 或利用已安装的扩展程序中的漏洞（例如 XSS bug）。仅从扩展程序的来源加载的网页或脚本 可以访问该扩展程序的资源。

使用 web_accessible_resources 清单属性声明要公开哪些资源以及要公开到哪些来源。此属性是一个对象数组，用于声明资源访问规则。每个对象都会将一组扩展程序资源映射到一组可访问这些资源的网址和/或扩展程序 ID。

每个元素都必须包含一个 "resources" 元素以及一个 "matches" 或 "extension_ids" 元素。这会建立一个映射，以将指定资源公开到与该格式匹配的网页或到具有匹配 ID 的扩展程序。"use_dynamic_url" 元素是可选的。

可通过网址在网页中获取资源 chrome-extension://[PACKAGE ID]/[PATH]，可使用 runtime.getURL() 生成 方法。这些资源会附带适当的 CORS 标头提供，因此可通过 fetch() 使用。

系统会禁止从网站源导航到扩展程序资源，除非相应资源 列为可通过网络访问请注意以下特殊情况：

网络无障碍资源示例演示了如何在有效的扩展程序中使用此元素。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "test1.png", "test2.png" ],
      "matches": [ "https://web-accessible-resources-1.glitch.me/*" ]
    }, {
      "resources": [ "test3.png", "test4.png" ],
      "matches": [ "https://web-accessible-resources-2.glitch.me/*" ],
      "use_dynamic_url": true
    }
  ],
  ...
}
```

Example 4 (unknown):
```unknown
"resources"
```

---

## 清单 - 版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/version

**Contents:**
- 清单 - 版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 版本名称

一到四个以英文句点分隔的整数，用于标识此扩展程序的版本。下面几条规则适用于整数：

如果已发布的扩展程序的版本字符串比已安装的扩展程序更新，则该扩展程序会自动更新。

比较从最左边的整数开始。然后，如果这些整数相等，则比较右侧的整数，依此类推。例如，1.2.0 是比 1.1.9.9999 更新的版本。

缺少的整数等于零。例如，1.1.9.9999 比 1.1 更新，1.1.9.9999 低于 1.2。

除了用于更新的 "version" 字段之外，"version_name" 还可设置为描述性的版本字符串，并将用于显示目的（如果存在）。

如果不存在 version_name，则版本字段也将用于显示。

**Examples:**

Example 1 (unknown):
```unknown
"version": "1"
```

Example 2 (unknown):
```unknown
"version": "1.0"
```

Example 3 (unknown):
```unknown
"version": "2.10.2"
```

Example 4 (unknown):
```unknown
"version": "3.1.2.4567"
```

---

## 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/sandbox?hl=zh-cn

**Contents:**
- 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

定义要在沙盒化的唯一源中提供的一组扩展程序页面。通过 扩展程序的沙盒化页面使用的内容安全政策是在 "content_security_policy" 键。

例如，以下代码展示了如何指定在具有 自定义 CSP：

如果未指定，则默认的 "content_security_policy" 值为 sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';。

您可以指定 CSP 值进一步限制沙盒，但该值必须包含 "sandbox" 指令，且不得包含 allow-same-origin 令牌（请参阅 HTML5 规范。

请注意，您只需列出预期会在窗口或框架中加载的网页即可。资源 而不需要出现在 pages 列表，因为它们将使用嵌入它们的框架的沙盒。

“在 Chrome 扩展程序中使用 eval()”一文详细介绍了如何实现 有了这个沙盒工作流，您可以使用在 SDK 环境下执行时发生错误的库， 扩展程序的默认内容安全政策。

**Examples:**

Example 1 (unknown):
```unknown
"content_security_policy"
```

Example 2 (unknown):
```unknown
postMessage()
```

Example 3 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

---

## 更新代码 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/api-calls?hl=zh-cn

**Contents:**
- 更新代码 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 将 tab.executeScript() 替换为 scripting.executeScript()
- 将 tabs.insertCSS() 和 tabs.removeCSS() 替换为 scripting.insertCSS() 和 scripting.removeCSS()
- 将浏览器操作和页面操作替换为操作
  - 将“browser_action”和“page_action”替换为“action”
  - 将 browserAction 和 pageAction API 替换为 action API
- 将回调替换为 Promise
- 替换预期使用 Manifest V2 后台上下文的函数
- 替换不受支持的 API

这是本教程的三个部分中的第一部分，介绍了对扩展程序服务工件之外的代码所需进行的更改。本部分针对的是与其他问题无关的代码更改必需更改。接下来的两个部分将介绍如何替换屏蔽网络请求和提高安全性。

在 Manifest V3 中，executeScript() 已从 tabs API 移至 scripting API。除了实际的代码更改之外，还需要更改清单文件中的权限。

对于 executeScript() 方法，您需要：

scripting.executeScript() 方法与 tabs.executeScript() 的使用方式类似。二者存在一些差异。

在扩展程序 Service Worker 中。

在清单 V3 中，insertCSS() 和 removeCSS() 从 tabs API 移到了 scripting API。这除了需要更改代码之外，还需要更改清单文件中的权限：

scripting API 中的函数与 tabs 中的函数类似。二者存在一些差异。

该示例展示了如何为 insertCSS() 执行此操作。removeCSS() 的过程是相同的。

在 Manifest V2 中，浏览器操作和页面操作是两个单独的概念。虽然他们起初的角色不同，但它们之间的差别逐渐缩小。在 Manifest V3 中，这些概念已整合到 Action API 中。这需要对您的 manifest.json 和扩展程序代码（不同于您在 Manifest V2 后台脚本中添加的内容）进行更改。

Manifest V3 中的 Action 与浏览器 Action 最为相似；不过，action API 不像 pageAction 那样提供 hide() 和 show()。如果您仍需要执行页面操作，则可以使用声明式内容模拟此类操作，或使用标签页 ID 调用 enable() 或 disable()。

在 manifest.json 中，将 "browser_action" 和 "page_action" 字段替换为 "action" 字段。如需了解 "action" 字段，请参阅参考文档。

在 Manifest V2 使用 browserAction 和 pageAction API 的地方，您现在应使用 action API。

在 Manifest V3 中，许多扩展 API 方法都会返回 promise。Promise 是异步方法返回的值的代理或占位符。如果您从未使用过 Promise，则可以在 MDN 上了解相关内容。本页介绍了在 Chrome 扩展程序中使用这些功能的须知事项。

为了实现向后兼容性，许多方法在添加 promise 支持后继续支持回调。请注意，您不能在同一函数调用中同时使用这两种方法。如果您传递回调，则该函数不会返回 promise；如果您希望返回 promise，则不要传递回调。某些 API 功能（例如事件监听器）仍需要回调。如需检查某个方法是否支持 Promise，请在其 API 参考文档中查找“Promise”标签。

如需从回调转换为 promise，请移除回调并处理返回的 promise。以下示例取自可选权限示例，具体而言是 newtab.js。回调版本显示了该示例使用回调对 request() 的调用是什么样的。请注意，可以使用 async 和 await 重写 promise 版本。

其他扩展程序上下文只能使用消息传递与扩展程序服务 worker 进行交互。因此，您需要替换预期使用后台上下文的调用，具体而言：

您的扩展程序脚本应使用消息传递在服务工件与扩展程序的其他部分之间进行通信。目前，这可通过在扩展程序 Service Worker 中使用 sendMessage() 并实现 chrome.runtime.onMessage 来实现。从长远来看，您应计划将这些调用替换为 postMessage() 和服务工件的消息事件处理脚本。

下列方法和属性需要在 Manifest V3 中更改。

**Examples:**

Example 1 (unknown):
```unknown
executeScript()
```

Example 2 (unknown):
```unknown
executeScript()
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"activeTab"
```

---

## 清单 - 要求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/requirements

**Contents:**
- 清单 - 要求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

扩展程序所需的技术。Chrome 应用商店等托管网站可能会使用此列表 阻止用户安装无法在其计算机上正常运行的扩展程序。我们可能会添加额外的要求检查， 未来。

"3D" 要求表示 GPU 硬件加速，并采用 "webgl" 或 "css3d" 作为有效值。"webgl" 要求是指 WebGL API。有关 Chrome 浏览器 3D 图形支持的详情，请参见关于 WebGL 和 3D 的帮助文章。 图形。您可以列出扩展程序所需的 3D 相关功能，如 示例：

自 Chrome 45 版起，我们已停止为扩展程序提供 NPAPI 插件支持。在此过程中，“插件” 要求已被弃用，无法再在清单文件中使用。

**Examples:**

Example 1 (unknown):
```unknown
"requirements": {
  "3D": {
    "features": ["webgl"]
  }
}
```

Example 2 (unknown):
```unknown
"requirements": {
  "3D": {
    "features": ["webgl"]
  }
}
```

---

## ChromeOS 上的文件处理 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/file-handling-chromeos?hl=zh-cn

**Contents:**
- ChromeOS 上的文件处理 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的适用范围
- 权限
- 清单
- 支持上下文
- 配置文件处理程序
- 处理文件
- 示例

借助文件处理功能，您可以配置 ChromeOS，以便扩展程序使用文件菜单的“打开”菜单或上下文菜单的“打开方式”菜单打开文件。文件打开后，您需要使用网络平台的 Launch Handler API 来处理文件的数据。然后，您将使用标准网络平台 API 来显示或处理文件。

您需要将 "file_handlers" 数组添加到 manifest.json 文件中。

此 API 可用于扩展程序 Service Worker、弹出式窗口、侧边栏或内容脚本。

"file_handlers" 的每个成员（即每个文件处理程序）都指定要由特定扩展程序页面处理的一个或多个文件类型。

您指定的处理程序会被添加到 ChromeOS 的“文件”窗口，即具体到“打开”和“打开方式”菜单。只有在用户选择具有特定扩展名的文件时，它们才会显示在这些菜单中。例如，如果文件处理程序指定 .txt，则 ChromeOS 菜单只会在用户选择具有该扩展名的文件时显示该处理程序。

文件处理程序是扩展程序中包含的 HTML 文件。当用户从菜单中选择您的处理程序时，HTML 文件会在新标签页中打开。处理文件（无论是显示文件还是以其他方式使用文件）都是通过 JavaScript 和适当的网络平台 API 完成的。处理代码必须位于单独的 JavaScript 文件中，通过 <script> 标记添加，而且还必须包含在您的扩展程序中。脚本文件使用 Launch Handler API 的 LaunchQueue 接口获取 FileSystemFileHandle 对象。

以下示例演示了如何使用 LaunchQueue 接口获取 FileSystemFileHandle 对象。如需查看文件处理的实际效果，请安装文件处理演示。

**Examples:**

Example 1 (unknown):
```unknown
"file_handlers"
```

Example 2 (unknown):
```unknown
"file_handlers"
```

Example 3 (unknown):
```unknown
LaunchQueue
```

Example 4 (unknown):
```unknown
FileSystemFileHandle
```

---

## 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/background?hl=zh-cn

**Contents:**
- 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，用于将 JavaScript 文件指定为扩展程序 Service Worker。Service Worker 是充当扩展程序的主要事件处理程序的后台脚本。如需了解详情，请参阅更全面的 Service Worker 简介。

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

---

## externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/externally-connectable

**Contents:**
- externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在没有外部连接的情况下连接
- 清单
- 参考

"externally_connectable" 清单属性用于声明哪些扩展程序和网页可以 使用 runtime.connect() 和 runtime.sendMessage() 连接到您的扩展程序。

有关消息传递的教程，请参阅跨扩展程序消息传递和发送消息 来自网页。

如果externally_connectable键没有在扩展程序的清单中声明，则所有扩展程序都可以连接，但是没有网页可以连接。因此，当您更新清单以使用 externally_connectable，如果未指定 "ids": ["*"]，则其他扩展程序 将无法再连接到您的扩展程序这可能是意想不到的后果，因此请及时告知 。

"externally_connectable" 清单键包含以下可选属性：

**Examples:**

Example 1 (unknown):
```unknown
"externally_connectable"
```

Example 2 (unknown):
```unknown
runtime.connect()
```

Example 3 (unknown):
```unknown
runtime.sendMessage()
```

Example 4 (unknown):
```unknown
externally_connectable
```

---

## 清单 - 无痕模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/incognito?hl=zh-cn

**Contents:**
- 清单 - 无痕模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 跨越模式
- 分离模式
- 不允许
- 如何选择

将 "incognito" 清单键与 "spanning" 或 "split" 一起使用，指定此扩展程序在允许在无痕模式下运行时的行为。使用 "not_allowed" 防止在无痕模式下启用此扩展程序。

默认模式为 "spanning"，表示扩展程序将在单个共享进程中运行。来自无痕式标签页的任何事件或消息都将发送到共享进程，并使用 无痕模式标志来指示它们的来源。由于无痕式标签页无法使用此共享进程，因此使用 "spanning" 无痕模式的扩展程序将无法将其扩展程序软件包中的页面加载到无痕式标签页的主框架中。

"split" 模式意味着无痕式窗口中的所有网页都将在自己的无痕进程中运行。如果扩展程序包含后台网页，该网页也会在无痕模式进程中运行。 此无痕模式进程与常规进程一起运行，但具有单独的内存纯 Cookie 存储。每个进程都只能查看来自自身上下文的事件和消息（例如，无痕模式进程只会看到无痕式标签页更新）。这些进程无法相互通信。

在无痕模式下无法启用此扩展程序。适用于 Chrome 47。

一般来讲，如果您的扩展程序需要在无痕模式浏览器中加载标签页，请使用 split 无痕模式行为。如果您的扩展程序需要登录到远程服务器，请使用 spanning 无痕模式。

chrome.storage.sync 和 chrome.storage.local 始终在常规进程和无痕模式进程之间共享。建议您使用它们来保留扩展程序的设置。

**Examples:**

Example 1 (unknown):
```unknown
"incognito"
```

Example 2 (unknown):
```unknown
"not_allowed"
```

---

## 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/background

**Contents:**
- 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，用于将 JavaScript 文件指定为扩展程序 Service Worker。Service Worker 是充当扩展程序的主要事件处理程序的后台脚本。如需了解详情，请参阅更全面的 Service Worker 简介。

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

---

## 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/sandbox

**Contents:**
- 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

定义要在沙盒化的唯一源中提供的一组扩展程序页面。通过 扩展程序的沙盒化页面使用的内容安全政策是在 "content_security_policy" 键。

例如，以下代码展示了如何指定在具有 自定义 CSP：

如果未指定，则默认的 "content_security_policy" 值为 sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';。

您可以指定 CSP 值进一步限制沙盒，但该值必须包含 "sandbox" 指令，且不得包含 allow-same-origin 令牌（请参阅 HTML5 规范。

请注意，您只需列出预期会在窗口或框架中加载的网页即可。资源 而不需要出现在 pages 列表，因为它们将使用嵌入它们的框架的沙盒。

“在 Chrome 扩展程序中使用 eval()”一文详细介绍了如何实现 有了这个沙盒工作流，您可以使用在 SDK 环境下执行时发生错误的库， 扩展程序的默认内容安全政策。

**Examples:**

Example 1 (unknown):
```unknown
"content_security_policy"
```

Example 2 (unknown):
```unknown
postMessage()
```

Example 3 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

---

## Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/hello-world?hl=zh-cn

**Contents:**
- Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- Hello World
- 加载未打包的扩展程序
- 固定扩展程序
- 重新加载扩展程序
  - 何时重新加载扩展程序
- 查找控制台日志和错误
  - 控制台日志
  - 错误日志

通过构建您的第一个“Hello World”扩展程序，了解 Chrome 扩展程序开发的基础知识。

您将创建一个“Hello World”示例，在本地加载扩展程序，查找日志，并探索其他建议。

当用户点击扩展程序工具栏图标时，此扩展程序将显示“Hello Extensions”。

首先，创建一个用于存储扩展程序文件的新目录。如果您愿意，也可以从 GitHub 下载完整源代码。

接下来，在此目录中创建一个名为 manifest.json 的新文件。此 JSON 文件描述了扩展程序的功能和配置。例如，大多数清单文件都包含 "action" 键，用于声明 Chrome 应将哪张图片用作扩展程序的操作图标，以及在用户点击扩展程序的操作图标时在弹出式窗口中显示的 HTML 网页。

将图标下载到您的目录中，并务必更改其名称，使其与 "default_icon" 键中的名称一致。

针对弹出式窗口，创建一个名为 hello.html 的文件，并添加以下代码：

现在，当用户点击扩展程序的操作图标（工具栏图标）时，该扩展程序会显示一个弹出式窗口。您可以通过在本地加载该测试页面来测试它。确保所有文件均已保存。

如需在开发者模式下加载未封装的扩展程序，请执行以下操作：

大功告成！扩展程序已成功安装。如果清单中未包含任何扩展程序图标，系统会为扩展程序创建一个通用图标。

默认情况下，当您在本地加载扩展程序时，它会显示在扩展程序菜单 () 中。将扩展程序固定到工具栏，以便在开发过程中快速访问扩展程序。

点击扩展程序的操作图标（工具栏图标）；您应该会看到一个弹出式窗口。

返回代码，然后在清单中将扩展程序的名称更改为“Hello Extensions of the world!”。

保存文件后，您还必须刷新扩展程序，才能在浏览器中看到此更改。前往“附加信息”页面，然后点击开启/关闭切换开关旁边的刷新图标：

下表显示了哪些组件需要重新加载才能看到更改：

在开发期间，您可以通过访问浏览器控制台日志来调试代码。在本例中，我们将找到弹出式窗口的日志。首先，将脚本标记添加到 hello.html。

创建一个 popup.js 文件，并添加以下代码。

如需在控制台中查看系统记录的这条消息，请执行以下操作：

现在，我们来破坏一下扩展程序。为此，我们可以移除 popup.js 中的闭引号：

前往“扩展程序”页面，然后打开弹出式窗口。系统随即会显示一个错误按钮。

如需详细了解如何调试服务工件、选项页面和内容脚本，请参阅调试扩展程序。

您可以通过多种方式构建扩展程序项目；不过，唯一的前提是将 manifest.json 文件放在扩展程序的根目录中，如以下示例所示：

如果您使用代码编辑器进行开发，则可以使用 npm 软件包 chrome-types 来利用 Chrome API 的自动补全功能。当 Chromium 源代码发生变化时，此 npm 软件包会自动更新。

选择以下任一教程，开始您的扩展程序学习之旅。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 4 (unknown):
```unknown
"default_icon"
```

---

## 清单 - 内容安全政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/content-security-policy?hl=zh-cn

**Contents:**
- 清单 - 内容安全政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 默认政策
- 最低和自定义内容安全政策
  - “扩展程序页面”政策
  - 沙盒页面政策

可选的清单键，包含网络平台内容安全政策，用于指定对扩展程序可以使用的脚本、样式和其他资源的限制。在此清单键中，您可以为扩展程序页面和沙盒化扩展程序页面分别定义可选政策。

“扩展程序页面”政策会应用于扩展程序中的网页上下文和工作器上下文。这包括扩展程序弹出式窗口、后台工作器，以及扩展程序打开的包含 HTML 网页或 iframe 的标签页。沙盒政策适用于在清单中指定为沙盒页面的所有网页。

如果用户未在清单中定义内容安全政策，则扩展程序页面和沙盒化扩展程序页面将使用默认属性。

在这种情况下，该扩展程序将仅从自己的打包资源加载本地脚本和对象。WebAssembly 将被停用，该扩展程序将无法运行内嵌 JavaScript，也无法将字符串评估为可执行代码。如果添加了沙盒页面，它将拥有更宽松的权限，可以更宽松地评估扩展程序外部的脚本。

开发者可以根据其项目需求为其扩展程序添加或移除规则，或使用最低的内容安全政策。

Chrome 会对扩展程序页面强制执行最低内容安全政策。这相当于在清单中指定以下政策：

extension_pages 政策不能超过此最小值。换言之，您不能向指令添加其他脚本源，例如将 'unsafe-eval' 添加到 script-src。如果您向扩展程序的政策中添加了禁止的来源，Chrome 会在安装时抛出如下错误：

沙盒页面的默认政策比扩展程序页面要宽松得多，因为沙盒页面无法访问扩展程序 API，也无法直接访问未经过沙盒化的网页。您可以根据需要自定义沙盒内容安全政策。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self';",
    "sandbox": "sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';"
  }
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self';",
    "sandbox": "sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';"
  }
  // ...
}
```

Example 3 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

Example 4 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

---

## 跨源 opener 政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/cross-origin-opener-policy

**Contents:**
- 跨源 opener 政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明

借助 cross_origin_opener_policy 清单键，扩展程序可以指定 针对扩展程序的请求的 Cross-Origin-Opener-Policy (COOP) 响应标头 来源。这包括扩展程序的 Service Worker、弹出式窗口、选项页面、打开某个扩展程序资源的标签页等。

此密钥与 cross_origin_embedder_policy 结合使用，可允许扩展程序选择启用 跨域隔离

cross_origin_opener_policy 清单键包含一个对象，该对象包含一个 名为 value 的属性，该属性接受字符串。Chrome 会将此字符串用作 Cross-Origin-Opener-Policy 标头。例如：

**Examples:**

Example 1 (unknown):
```unknown
cross_origin_opener_policy
```

Example 2 (unknown):
```unknown
cross_origin_opener_policy
```

Example 3 (unknown):
```unknown
Cross-Origin-Opener-Policy
```

Example 4 (unknown):
```unknown
{
    ...
    "cross_origin_opener_policy": {
      "value": "same-origin"
    },
    ...
}
```

---

## 清单 - 要求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/requirements?hl=zh-cn

**Contents:**
- 清单 - 要求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

扩展程序所需的技术。Chrome 应用商店等托管网站可能会使用此列表 阻止用户安装无法在其计算机上正常运行的扩展程序。我们可能会添加额外的要求检查， 未来。

"3D" 要求表示 GPU 硬件加速，并采用 "webgl" 或 "css3d" 作为有效值。"webgl" 要求是指 WebGL API。有关 Chrome 浏览器 3D 图形支持的详情，请参见关于 WebGL 和 3D 的帮助文章。 图形。您可以列出扩展程序所需的 3D 相关功能，如 示例：

自 Chrome 45 版起，我们已停止为扩展程序提供 NPAPI 插件支持。在此过程中，“插件” 要求已被弃用，无法再在清单文件中使用。

**Examples:**

Example 1 (unknown):
```unknown
"requirements": {
  "3D": {
    "features": ["webgl"]
  }
}
```

Example 2 (unknown):
```unknown
"requirements": {
  "3D": {
    "features": ["webgl"]
  }
}
```

---

## 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/minimum-chrome-version

**Contents:**
- 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 强制执行
  - 新安装次数
  - 现有安装

可选的清单键，包含一个字符串，该字符串定义了 Chrome 可以安装该扩展程序。为此字符串设置的值必须是现有 Chrome 浏览器版本字符串的子字符串。使用完整版 数字可指定 Chrome 的特定更新，也可使用 字符串以指定特定的主要版本。

在低于最低版本的 Chrome 版本中，Chrome 应用商店会显示“不兼容”消息，而不是安装按钮。这些用户 版本将无法安装您的扩展程序。

您的扩展程序的现有用户 minimum_chrome_version版本高于目前的浏览器版本。此操作会以静默方式进行，因此您应谨慎行事，并考虑如何让现有用户知道他们不再收到更新。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 3 (unknown):
```unknown
minimum_chrome_version
```

Example 4 (unknown):
```unknown
minimum_chrome_version
```

---

## ChromeOS 上的文件处理 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/file-handling-chromeos

**Contents:**
- ChromeOS 上的文件处理 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的适用范围
- 权限
- 清单
- 支持上下文
- 配置文件处理程序
- 处理文件
- 示例

借助文件处理功能，您可以配置 ChromeOS，以便扩展程序使用文件菜单的“打开”菜单或上下文菜单的“打开方式”菜单打开文件。文件打开后，您需要使用网络平台的 Launch Handler API 来处理文件的数据。然后，您将使用标准网络平台 API 来显示或处理文件。

您需要将 "file_handlers" 数组添加到 manifest.json 文件中。

此 API 可用于扩展程序 Service Worker、弹出式窗口、侧边栏或内容脚本。

"file_handlers" 的每个成员（即每个文件处理程序）都指定要由特定扩展程序页面处理的一个或多个文件类型。

您指定的处理程序会被添加到 ChromeOS 的“文件”窗口，即具体到“打开”和“打开方式”菜单。只有在用户选择具有特定扩展名的文件时，它们才会显示在这些菜单中。例如，如果文件处理程序指定 .txt，则 ChromeOS 菜单只会在用户选择具有该扩展名的文件时显示该处理程序。

文件处理程序是扩展程序中包含的 HTML 文件。当用户从菜单中选择您的处理程序时，HTML 文件会在新标签页中打开。处理文件（无论是显示文件还是以其他方式使用文件）都是通过 JavaScript 和适当的网络平台 API 完成的。处理代码必须位于单独的 JavaScript 文件中，通过 <script> 标记添加，而且还必须包含在您的扩展程序中。脚本文件使用 Launch Handler API 的 LaunchQueue 接口获取 FileSystemFileHandle 对象。

以下示例演示了如何使用 LaunchQueue 接口获取 FileSystemFileHandle 对象。如需查看文件处理的实际效果，请安装文件处理演示。

**Examples:**

Example 1 (unknown):
```unknown
"file_handlers"
```

Example 2 (unknown):
```unknown
"file_handlers"
```

Example 3 (unknown):
```unknown
LaunchQueue
```

Example 4 (unknown):
```unknown
FileSystemFileHandle
```

---

## 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate?hl=zh-cn

**Contents:**
- 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保留当前的功能集
- 新的扩展程序平台功能

将 Manifest V2 扩展程序转换为 Manifest V3 扩展程序的指南。

此部分可帮助您将扩展程序从 Manifest V2 升级到 Manifest V3（Chrome 扩展程序平台的最新版本）。迁移工作大致分为以下几类。为帮助您跟踪工作进度，我们提供了一份核对清单，总结了这些文档的内容。您可以通过核对清单查看相关内容，也可以深入了解相关内容。两个路径均以升级版附加信息结尾。

我们还提供 Extension Manifest Converter。它无法为您提供一切服务，但可帮助您入门。转换器的 README 文件中介绍了工具更改的内容。

为了降低出现意外问题或 bug 的可能性，我们建议不要在迁移时添加新功能。例如，添加需要新权限的功能可能会触发权限警告，这会导致您的扩展程序停用，直到用户接受新权限。请参阅权限警告最佳做法，了解如何在不显示警告的情况下添加权限。

Chrome 88 或更高版本通常支持 Manifest V3。更新 API 调用时，您可能会发现替换功能可能要到版本 88 之后才在 Chrome 中推出。API 参考页面包含各 API 成员的支持信息。如果您发现需要使用其中某项功能，可以在清单文件中指定最低 Chrome 版本。

自 Manifest V3 发布以来，我们不断添加新功能，其中许多功能在 Manifest V2 和 Manifest V3 中均可使用。在转换时，您并不需要使用这些组件；但是，当它们取代旧功能时，您应优先使用这些功能而不是它们所取代的功能，并且预计被替换的功能最终会被弃用和移除。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

---

## file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/file-handlers

**Contents:**
- file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"file_handlers" 清单键用于指定 ChromeOS 扩展程序要处理的文件类型。如需处理文件，请使用 Web 平台的 Launch Handler API。如需了解特定于扩展程序的信息，请参阅文件处理。

**Examples:**

Example 1 (unknown):
```unknown
"file_handlers"
```

Example 2 (unknown):
```unknown
"file_handlers": [
  {
    "action": "/open_text.html",
    "name": "Plain text",
    "accept": {
      "text/plain": [".txt"]
    }
    "launch_type": "single-client"
  }
]
```

Example 3 (unknown):
```unknown
"file_handlers": [
  {
    "action": "/open_text.html",
    "name": "Plain text",
    "accept": {
      "text/plain": [".txt"]
    }
    "launch_type": "single-client"
  }
]
```

Example 4 (unknown):
```unknown
"file_handlers"
```

---

## Manifest V2 支持时间表 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/mv2-deprecation-timeline

**Contents:**
- Manifest V2 支持时间表 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
  - 2025 年 7 月 24 日：在所有位置停用 Manifest V2
  - 2025 年 3 月 31 日：停用 Manifest V2，但可以选择重新启用扩展程序
  - 2024 年 10 月 9 日：关于 Manifest V2 淘汰的最新动态。
  - 2024 年 6 月 3 日：开始逐步淘汰 Manifest V2。
  - 2022 年 6 月：Chrome 应用商店 - 不再接受新的专用扩展程序
  - 2022 年 1 月：Chrome 应用商店 - 无新的公开 / 不公开列出的扩展程序

了解 Manifest V2 何时会停止支持扩展程序

在 Chrome 138 中，所有 Chrome 渠道的所有用户现在都已停用 Manifest V2 扩展程序。用户无法再重新启用这些功能。

对于企业，ExtensionManifestV2Availability 政策将在 Chrome 139 中移除。此项变更将同时影响 Chrome 139 上的所有用户。

因此，对于升级到 Chrome 139 及后续版本的任何用户，Manifest V2 扩展程序都将无法再正常运行。 Chromium 发布时间表提供了更多发布信息。

现在，所有 Chrome 渠道的所有用户默认情况下都已停用 Manifest V2 扩展程序，但用户仍然可以重新启用 Manifest V2 扩展程序。第二阶段（用户无法再重新启用这些功能）已开始向 Canary 中的部分用户推出。这项变更将继续缓慢地向更多用户推出。

与之前一样，使用 ExtensionManifestV2Availability 政策的企业将继续不受任何浏览器变更的影响，至少到 2025 年 6 月为止。从 6 月开始，Chrome 139 分支将开始，届时 Chrome 将不再支持 Manifest V2 扩展程序。与之前逐步向用户推出的停用 Manifest V2 扩展程序的变更不同，此变更将立即影响 Chrome 139 上的所有用户。因此，Chrome 138 是支持 Manifest V2 扩展程序（与 ExtensionManifestV2Availability 键搭配使用时）的最后一个 Chrome 版本。您可以在 Chromium 发布时间表中找到有关 Chrome 138 和 139 的发布信息，包括 ChromeOS 的 LTS 支持。

在过去几个月里，我们一直在逐步淘汰清单 V2。 目前，chrome://extensions 页面会向 Manifest V2 扩展程序的所有用户显示警告横幅。此外，我们已开始在预稳定版渠道中停用 Manifest V2 扩展程序。

我们现在将开始在 Chrome 稳定版中停用仍在使用 Manifest V2 的已安装扩展程序。这项变更将在未来几周内逐步推出。 用户将被引导至 Chrome 应用商店，系统会向他们推荐已停用扩展程序的 Manifest V3 替代方案。在短时间内，用户仍可重新启用 Manifest V2 扩展程序。使用 ExtensionManifestV2Availability 政策的企业将不受任何浏览器变更的影响，直到 2025 年 6 月。如需了解更多背景信息，请参阅我们的2024 年 5 月博客。

从 6 月 3 日开始，在 Chrome Beta 版、Dev 版和 Canary 版渠道中，如果用户仍安装了 Manifest V2 扩展程序，那么当他们访问扩展程序管理页面 (chrome://extensions) 时，部分用户会开始看到警告横幅，告知他们所安装的部分（Manifest V2）扩展程序很快将不再受支持。与此同时，仍在使用 Manifest V2 的获“精选”徽章的扩展程序将失去其徽章。

Chrome 应用商店已停止接受将公开范围设置为“专用”的新 Manifest V2 扩展程序。

Chrome 网上应用店已停止接受新的 Manifest V2 扩展程序，且这些扩展程序的公开范围设置为“公开”或“不公开”。移除了将 Manifest V2 扩展程序从“不公开”更改为“公开”或“不公开列出”的功能。

**Examples:**

Example 1 (unknown):
```unknown
ExtensionManifestV2Availability
```

---

## 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/sandbox?hl=zh-cn

**Contents:**
- 清单 - 沙盒 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

定义要在沙盒化的唯一源中提供的一组扩展程序页面。通过 扩展程序的沙盒化页面使用的内容安全政策是在 "content_security_policy" 键。

例如，以下代码展示了如何指定在具有 自定义 CSP：

如果未指定，则默认的 "content_security_policy" 值为 sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';。

您可以指定 CSP 值进一步限制沙盒，但该值必须包含 "sandbox" 指令，且不得包含 allow-same-origin 令牌（请参阅 HTML5 规范。

请注意，您只需列出预期会在窗口或框架中加载的网页即可。资源 而不需要出现在 pages 列表，因为它们将使用嵌入它们的框架的沙盒。

“在 Chrome 扩展程序中使用 eval()”一文详细介绍了如何实现 有了这个沙盒工作流，您可以使用在 SDK 环境下执行时发生错误的库， 扩展程序的默认内容安全政策。

**Examples:**

Example 1 (unknown):
```unknown
"content_security_policy"
```

Example 2 (unknown):
```unknown
postMessage()
```

Example 3 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  ...
  "content_security_policy": {
    "sandbox": "sandbox allow-scripts; script-src 'self' https://example.com"
  },
  "sandbox": {
    "pages": [
      "page1.html",
      "directory/page2.html"
    ]
  },
  ...
}
```

---

## 清单 - input_components 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/input-components?hl=zh-cn

**Contents:**
- 清单 - input_components 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，支持将 input.ime API（输入法）用于 ChromeOS。这样一来，您的扩展程序便可以处理按键、设置合成和打开辅助窗口。开发者还必须在扩展程序的 "permissions" 数组中声明 "input" 权限。 该键接受一系列对象：name、id、language、layouts、input_view 和 options_page（请参阅下表）。

**Examples:**

Example 1 (unknown):
```unknown
"permissions"
```

Example 2 (unknown):
```unknown
options_page
```

Example 3 (unknown):
```unknown
options_page
```

Example 4 (unknown):
```unknown
{
  // ...
   "input_components": [{
     "name": "ToUpperIME",
    "id": "ToUpperIME",
    "language": "en",
    "layouts": ["us::eng"]
  }]
  // ...
}
```

---

## 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/intro/mv3-overview?hl=zh-cn

**Contents:**
- 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保留当前的功能集
- 新的扩展程序平台功能

将 Manifest V2 扩展程序转换为 Manifest V3 扩展程序的指南。

此部分可帮助您将扩展程序从 Manifest V2 升级到 Manifest V3（Chrome 扩展程序平台的最新版本）。迁移工作大致分为以下几类。为帮助您跟踪工作进度，我们提供了一份核对清单，总结了这些文档的内容。您可以通过核对清单查看相关内容，也可以深入了解相关内容。两个路径均以升级版附加信息结尾。

我们还提供 Extension Manifest Converter。它无法为您提供一切服务，但可帮助您入门。转换器的 README 文件中介绍了工具更改的内容。

为了降低出现意外问题或 bug 的可能性，我们建议不要在迁移时添加新功能。例如，添加需要新权限的功能可能会触发权限警告，这会导致您的扩展程序停用，直到用户接受新权限。请参阅权限警告最佳做法，了解如何在不显示警告的情况下添加权限。

Chrome 88 或更高版本通常支持 Manifest V3。更新 API 调用时，您可能会发现替换功能可能要到版本 88 之后才在 Chrome 中推出。API 参考页面包含各 API 成员的支持信息。如果您发现需要使用其中某项功能，可以在清单文件中指定最低 Chrome 版本。

自 Manifest V3 发布以来，我们不断添加新功能，其中许多功能在 Manifest V2 和 Manifest V3 中均可使用。在转换时，您并不需要使用这些组件；但是，当它们取代旧功能时，您应优先使用这些功能而不是它们所取代的功能，并且预计被替换的功能最终会被弃用和移除。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

---

## 跨源网络请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/network-requests

**Contents:**
- 跨源网络请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 扩展程序来源
- 请求跨源权限
- Fetch() 与 XMLHttpRequest()
- 安全注意事项
  - 避免跨站脚本漏洞
  - 限制内容脚本对跨源请求的访问权限
  - 优先使用 HTTPS（而非 HTTP）
  - 调整内容安全政策

常规网页可以使用 fetch() 或 XMLHttpRequest API 与远程服务器发送和接收数据，但受到同源政策的限制。内容脚本代表内容脚本注入到的 Web 来源发起请求，因此内容脚本也受同源政策的约束。扩展程序来源并非如此受限。在扩展程序 Service Worker 或前台标签页中执行的脚本可以与其来源之外的远程服务器通信，前提是该扩展程序请求了主机权限。

每个正在运行的扩展程序都位于自己的单独安全源中。无需请求其他特权，扩展程序即可调用 fetch() 来获取其安装中的资源。例如，如果某个扩展程序在 config_resources/ 文件夹中包含名为 config.json 的 JSON 配置文件，则该扩展程序可以按如下方式检索该文件的内容：

如果扩展程序尝试从自身以外的安全源（例如 https://www.google.com）请求内容，除非该扩展程序具有主机权限，否则系统会将其视为跨源请求。在内容脚本中，跨源请求始终会被视为跨源请求，即使扩展程序具有主机权限也是如此。

如需请求访问扩展程序来源之外的远程服务器，请将主机、匹配模式或二者添加到manifest文件的 host_permissions 部分。

匹配模式“https://*/”允许通过 HTTPS 访问所有可访问的网域。请注意，此处的匹配模式与内容脚本匹配模式类似，但系统会忽略主机后面的任何路径信息。

另请注意，系统会按主机和架构授予访问权限。如果扩展程序同时需要对给定主机或一组主机拥有安全和不安全的 HTTP 访问权限，则必须单独声明这些权限：

fetch() 专为服务工件而创建，遵循了远离同步操作的更广泛 Web 趋势。扩展程序在 Service Worker 之外支持 XMLHttpRequest() API，调用该 API 会触发扩展程序 Service Worker 的提取处理脚本。新工作应尽可能采用 fetch()。

使用通过 fetch() 检索的资源时，您的屏幕外文档、侧边栏或弹出式窗口应注意不要遭到跨网站脚本攻击。具体而言，请避免使用 innerHTML 等危险 API。例如：

相反，请优先使用不会运行脚本的更安全的 API：

代表内容脚本执行跨源请求时，请务必防范可能尝试冒充内容脚本的恶意网页。特别是，请勿允许内容脚本请求任意网址。

请考虑以下示例：一个扩展程序执行跨源请求，以便内容脚本发现商品的价格。一种不太安全的方法是让内容脚本指定后台页面要提取的确切资源。

在上述方法中，内容脚本可以请求扩展程序提取扩展程序有权访问的任何网址。恶意网页可能会伪造此类消息，并诱骗扩展程序授予对跨源资源的访问权限。

而是设计消息处理脚本，以限制可提取的资源。在下面的示例中，内容脚本仅提供 itemId，而非完整网址。

此外，请特别注意通过 HTTP 检索的资源。如果您的扩展程序在恶意网络上使用，网络攻击者（也称为"man-in-the-middle"）可能会修改响应，并可能攻击您的扩展程序。相反，请尽可能使用 HTTPS。

如果您通过向清单添加 content_security_policy 属性来修改扩展程序的默认内容安全政策，则需要确保您要连接的所有主机都已获准。虽然默认政策不会限制与主机的连接，但在明确添加 connect-src 或 default-src 指令时，请务必小心。

**Examples:**

Example 1 (unknown):
```unknown
XMLHttpRequest
```

Example 2 (unknown):
```unknown
config_resources/
```

Example 3 (unknown):
```unknown
config.json
```

Example 4 (javascript):
```javascript
const response = await fetch('/config_resources/config.json');
const jsonData = await response.json();
```

---

## chrome.enterprise.networkingAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/enterprise/networkingAttributes

**Contents:**
- chrome.enterprise.networkingAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - NetworkDetails
    - 属性
- 方法
  - getNetworkDetails()
    - 参数

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

设备的本地 IPv4 地址（如果未配置，则为未定义）。

设备的本地 IPv6 地址（如果未配置，则为未定义）。

检索设备的默认网络的网络详细信息。如果用户没有关联或设备未连接到网络，系统将设置 runtime.lastError 并附上失败原因。

Promise<NetworkDetails>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.networkingAttributes
```

Example 2 (unknown):
```unknown
enterprise.networkingAttributes
```

Example 3 (unknown):
```unknown
chrome.enterprise.networkingAttributes.getNetworkDetails(  callback?: function,): Promise<NetworkDetails>
```

Example 4 (unknown):
```unknown
runtime.lastError
```

---

## 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest?hl=zh-cn

**Contents:**
- 清单文件格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 示例
  - 最小清单
  - 注册内容脚本
  - 注入内容脚本
  - 带权限的弹出式窗口
  - 侧边栏
- 清单键
  - 扩展程序平台所需的密钥
  - Chrome 应用商店所需的密钥

每个扩展程序的根目录中都必须有一个 manifest.json 文件，其中列出了与该扩展程序的结构和行为相关的重要信息。本页介绍了扩展程序清单的结构以及它们可以包含的功能。

以下示例清单展示了基本清单结构和一些常用功能，可作为创建您自己的清单的起点：

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Run script automatically",
  "description": "Runs a script on www.example.com automatically when user installs the extension",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "content_scripts": [
    {
      "js": [
        "content-script.js"
      ],
      "matches": [
        "http://*.example.com//"
      ]
    }
  ]
}
```

---

## externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/externally_connectable?hl=zh-cn

**Contents:**
- externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在没有外部连接的情况下连接
- 清单
- 参考

"externally_connectable" 清单属性用于声明哪些扩展程序和网页可以 使用 runtime.connect() 和 runtime.sendMessage() 连接到您的扩展程序。

有关消息传递的教程，请参阅跨扩展程序消息传递和发送消息 来自网页。

如果externally_connectable键没有在扩展程序的清单中声明，则所有扩展程序都可以连接，但是没有网页可以连接。因此，当您更新清单以使用 externally_connectable，如果未指定 "ids": ["*"]，则其他扩展程序 将无法再连接到您的扩展程序这可能是意想不到的后果，因此请及时告知 。

"externally_connectable" 清单键包含以下可选属性：

**Examples:**

Example 1 (unknown):
```unknown
"externally_connectable"
```

Example 2 (unknown):
```unknown
runtime.connect()
```

Example 3 (unknown):
```unknown
runtime.sendMessage()
```

Example 4 (unknown):
```unknown
externally_connectable
```

---

## 共享模块 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/shared-modules?hl=zh-cn

**Contents:**
- 共享模块 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
  - 导出
  - 导入
- 访问资源
- 安装 / 卸载

共享模块是无需权限的资源集合，可在 。共享模块的常见用途包括：

通过两个清单字段使用共享模块："export" 和 "import"。

export 字段表示扩展程序是导出其资源的共享模块：

扩展程序和应用使用 import 字段来声明它们依赖于 共享模块：

共享模块资源由根目录中的预留路径 _modules/SHARED_MODULE_ID 访问 。例如，若要添加来自共享模块 foo.js 的脚本， ID 为“cccccccccccccccccccccccccccccc”，请使用您的扩展程序根目录中的以下路径：

如果导入扩展程序的 ID 为“aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa”，则资源的完整网址 为：

请注意，由于共享模块中的资源会叠加到 扩展程序，授予导入扩展程序的所有权限都适用于“共享”中的代码 模块。此外，共享模块可以使用 绝对路径。

共享模块会在相关扩展程序需要时从 Chrome 应用商店自动安装，并会在引用它的最后一个扩展程序卸载时自动卸载。 要上传使用共享模块的扩展程序，必须在以下位置发布共享模块： Chrome 应用商店和扩展程序不得通过其 许可名单。

在开发过程中，您需要手动安装您的扩展程序使用的所有共享模块。 对于旁加载或解压出来的扩展程序，系统不会自动安装 。对于本地安装的未封装共享模块，您必须使用 key 字段 确保共享模块使用正确的 ID。

**Examples:**

Example 1 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Shared Module",
  "export": {
    // Optional list of extension IDs explicitly allowed to
    // import this Shared Module's resources.  If no allowlist
    // is given, all extensions are allowed to import it.
    "allowlist": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ]
  }
  // Note: no permissions are allowed in Shared Modules
}
```

Example 2 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Shared Module",
  "export": {
    // Optional list of extension IDs explicitly allowed to
    // import this Shared Module's resources.  If no allowlist
    // is given, all extensions are allowed to import it.
    "allowlist": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ]
  }
  // Note: no permissions are allowed in Shared Modules
}
```

Example 3 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Importing Extension",
  ...
  "import": [
    {"id": "cccccccccccccccccccccccccccccccc"},
    {"id": "dddddddddddddddddddddddddddddddd"
     "minimum_version": "0.5" // optional
    },
  ]
}
```

Example 4 (unknown):
```unknown
{
  "version": "1.0",
  "name": "My Importing Extension",
  ...
  "import": [
    {"id": "cccccccccccccccccccccccccccccccc"},
    {"id": "dddddddddddddddddddddddddddddddd"
     "minimum_version": "0.5" // optional
    },
  ]
}
```

---

## 清单 - 无痕模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/incognito

**Contents:**
- 清单 - 无痕模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 跨越模式
- 分离模式
- 不允许
- 如何选择

将 "incognito" 清单键与 "spanning" 或 "split" 一起使用，指定此扩展程序在允许在无痕模式下运行时的行为。使用 "not_allowed" 防止在无痕模式下启用此扩展程序。

默认模式为 "spanning"，表示扩展程序将在单个共享进程中运行。来自无痕式标签页的任何事件或消息都将发送到共享进程，并使用 无痕模式标志来指示它们的来源。由于无痕式标签页无法使用此共享进程，因此使用 "spanning" 无痕模式的扩展程序将无法将其扩展程序软件包中的页面加载到无痕式标签页的主框架中。

"split" 模式意味着无痕式窗口中的所有网页都将在自己的无痕进程中运行。如果扩展程序包含后台网页，该网页也会在无痕模式进程中运行。 此无痕模式进程与常规进程一起运行，但具有单独的内存纯 Cookie 存储。每个进程都只能查看来自自身上下文的事件和消息（例如，无痕模式进程只会看到无痕式标签页更新）。这些进程无法相互通信。

在无痕模式下无法启用此扩展程序。适用于 Chrome 47。

一般来讲，如果您的扩展程序需要在无痕模式浏览器中加载标签页，请使用 split 无痕模式行为。如果您的扩展程序需要登录到远程服务器，请使用 spanning 无痕模式。

chrome.storage.sync 和 chrome.storage.local 始终在常规进程和无痕模式进程之间共享。建议您使用它们来保留扩展程序的设置。

**Examples:**

Example 1 (unknown):
```unknown
"incognito"
```

Example 2 (unknown):
```unknown
"not_allowed"
```

---

## Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/checklist?hl=zh-cn

**Contents:**
- Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 更新清单
- 迁移到 Service Worker
- 更新 API 调用
- 替换屏蔽 Web 请求监听器
- 提高扩展程序的安全性
- 发布 Manifest V3 扩展程序

以下核对清单可帮助您跟踪迁移工作。它们定义了必须完成的任务以及指向说明的链接。如迁移摘要中所述，迁移工作大致分为五类。

Manifest V3 与 Manifest V2 manifest.json文件需要的格式略有不同。本页面介绍了仅影响 manifest.json 文件的更改。不过，对脚本和网页的许多更改还需要对清单进行更改。这些更改包含在需要它们的迁移任务中。

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码远离主线程。这样可以让扩展程序仅在需要时运行，从而节省资源。

在开始之前，请先了解后台脚本与扩展 Service Worker 之间的区别。

某些功能需要替换为 Manifest V3 等效项。还有一些扩展程序则需要彻底删除。

您的扩展程序不会像在 Manifest V2 中那样以编程方式读取网络请求并更改请求，而是指定规则来描述在满足一组给定条件时要执行的操作。

完成上述操作后，您可能需要查看一些常见用例：

为了提高扩展程序的安全性，必须进行更改。这包括移除不再受支持的远程托管代码。

扩展程序转换为清单版本 3 后，即可在 Chrome 应用商店中发布扩展程序。根据所做的更改，考虑逐步发布。通过这种方法，您可以确保自己的扩展程序在有限的受众群体范围内能够按预期运行，然后再面向整个用户群发布。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
XMLHttpRequest()
```

Example 4 (unknown):
```unknown
tabs.executeScript()
```

---

## “activeTab”权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/activeTab?hl=zh-cn

**Contents:**
- “activeTab”权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 示例
- 设计初衷
- 什么是“activeTab”允许
- 调用 activityTab

"activeTab" 权限允许扩展程序在 用户调用该扩展程序 - 例如，点击其操作。访问该标签页 有效期在用户位于相应页面时有效，在用户离开页面或关闭标签页时失效。 例如，如果用户通过 https://example.com 调用扩展程序，然后 转到 https://example.com/foo，该扩展程序仍能继续访问该网页。如果 当用户前往 https://chromium.org 时，相关访问权限会被撤消。

这是 "<all_urls>" 的多种用法，但会显示无警告消息。 ：

请参阅 Page Redder 扩展程序示例：

假设有一个包含操作和上下文菜单项的网页剪辑扩展程序。这个 可能只需要在用户点击其操作或 。

如果没有 "activeTab"，此扩展程序将需要请求对每个网站的完整、永久访问权限， 这样，在用户调用它时，它就可以正常运行。这里有很多 如果扩展程序遭到入侵，攻击者 获取该扩展程序拥有的所有内容

相比之下，具有 "activeTab" 权限的扩展程序仅在响应时获取对标签页的访问权限 显式用户手势。如果扩展程序遭到入侵，攻击者将需要等待 用户在获得访问权限之前调用该扩展程序。并且该访问权限仅在相应标签页 已导航或已关闭。

为标签页启用 "activeTab" 权限后，扩展程序可以：

以下用户手势可启用 "activeTab" 权限：

**Examples:**

Example 1 (unknown):
```unknown
"activeTab"
```

Example 2 (unknown):
```unknown
"<all_urls>"
```

Example 3 (unknown):
```unknown
"activeTab"
```

Example 4 (unknown):
```unknown
"activeTab"
```

---

## 清单 - 试用令牌 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/trial_tokens

**Contents:**
- 清单 - 试用令牌 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

一组试用令牌，用于在扩展程序上下文中启用源试用和弃用试用功能。您可以在有效试验页面上浏览和注册参与中的试验。

如需同时参与多次试验，请将每个令牌作为单独的数组条目添加。

如需详细了解如何在扩展程序中注册和使用令牌，请参阅官方指南。

**Examples:**

Example 1 (unknown):
```unknown
"trial_tokens": ["AnlT7gRo/750gGKtoI/A3D2rL5yAQA9wISlLqHGE6vJQinPfk0HiIij5LhWs+iuB7mTeotXmEXkvdpOAC1YjAgAAAG97Im9yaWdpbiI6ImNocm9tZS1leHRlbnNpb246Ly9sampoamFha21uY2lib25uanBhb2dsYmhjamVvbGhrayIsImZlYXR1cmUiOiJJQ2Fubm90QmVsaWV2ZVlvdVdhc3RlZFlvdXJUaW1lRGVjb2RpbmdUaGlzIiwiZXhwaXJ5Ijo1NzI1NDA3OTk5fQ=="]
```

Example 2 (unknown):
```unknown
"trial_tokens": ["AnlT7gRo/750gGKtoI/A3D2rL5yAQA9wISlLqHGE6vJQinPfk0HiIij5LhWs+iuB7mTeotXmEXkvdpOAC1YjAgAAAG97Im9yaWdpbiI6ImNocm9tZS1leHRlbnNpb246Ly9sampoamFha21uY2lib25uanBhb2dsYmhjamVvbGhrayIsImZlYXR1cmUiOiJJQ2Fubm90QmVsaWV2ZVlvdVdhc3RlZFlvdXJUaW1lRGVjb2RpbmdUaGlzIiwiZXhwaXJ5Ijo1NzI1NDA3OTk5fQ=="]
```

---

## Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/checklist

**Contents:**
- Manifest V3 迁移核对清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 更新清单
- 迁移到 Service Worker
- 更新 API 调用
- 替换屏蔽 Web 请求监听器
- 提高扩展程序的安全性
- 发布 Manifest V3 扩展程序

以下核对清单可帮助您跟踪迁移工作。它们定义了必须完成的任务以及指向说明的链接。如迁移摘要中所述，迁移工作大致分为五类。

Manifest V3 与 Manifest V2 manifest.json文件需要的格式略有不同。本页面介绍了仅影响 manifest.json 文件的更改。不过，对脚本和网页的许多更改还需要对清单进行更改。这些更改包含在需要它们的迁移任务中。

Service Worker 会替换扩展程序的后台或事件页面，以确保后台代码远离主线程。这样可以让扩展程序仅在需要时运行，从而节省资源。

在开始之前，请先了解后台脚本与扩展 Service Worker 之间的区别。

某些功能需要替换为 Manifest V3 等效项。还有一些扩展程序则需要彻底删除。

您的扩展程序不会像在 Manifest V2 中那样以编程方式读取网络请求并更改请求，而是指定规则来描述在满足一组给定条件时要执行的操作。

完成上述操作后，您可能需要查看一些常见用例：

为了提高扩展程序的安全性，必须进行更改。这包括移除不再受支持的远程托管代码。

扩展程序转换为清单版本 3 后，即可在 Chrome 应用商店中发布扩展程序。根据所做的更改，考虑逐步发布。通过这种方法，您可以确保自己的扩展程序在有限的受众群体范围内能够按预期运行，然后再面向整个用户群发布。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
XMLHttpRequest()
```

Example 4 (unknown):
```unknown
tabs.executeScript()
```

---

## 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/improve-security?hl=zh-cn

**Contents:**
- 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 移除执行任意字符串
- 移除远程托管的代码
  - 配置驱动型功能和逻辑
  - 使用远程服务的外部化逻辑
  - 在沙盒化 iframe 中嵌入远程托管的代码
  - 捆绑第三方库
  - 在标签页注入的脚本中使用外部库
  - 注入函数
  - 寻找其他解决方法

这是介绍不属于扩展程序服务工作线程的代码所需更改的第三部分。其中介绍了提高扩展程序安全性所需的更改。另外两个部分介绍了升级到 Manifest V3 所需的更新代码和替换屏蔽 Web 请求。

您无法再使用 executeScript()、eval() 和 new Function() 执行外部逻辑。

executeScript() 方法现在位于 scripting 命名空间中，而不是 tabs 命名空间中。如需了解如何更新通话，请参阅移动 executeScript()。

在少数特殊情况下，仍然可以执行任意字符串：

在 Manifest V3 中，扩展程序的所有逻辑都必须包含在扩展程序软件包中。根据 Chrome 应用商店政策，您将无法再加载和执行远程托管的文件。例如：

您可以采用其他方法，具体取决于您的用例和远程托管的原因。本部分介绍了可考虑的方法。如果您在处理远程托管代码时遇到问题，可参阅相关指南。

您的扩展程序会在运行时加载并缓存远程配置（例如 JSON 文件）。缓存的配置决定了启用了哪些功能。

您的扩展程序调用远程 Web 服务。这样，您就可以将代码保持私密状态，并根据需要进行更改，同时避免重新提交到 Chrome 应用商店的额外开销。

沙盒化 iframe 支持远程托管的代码。请注意，如果代码需要访问嵌入页面的 DOM，则此方法不起作用。

如果您使用的是之前从外部服务器加载的流行框架（例如 React 或 Bootstrap），则可以下载缩小的文件，将其添加到您的项目并在本地导入。例如：

如需在 Service Worker 中加入库，请在清单中将 "background.type" 键设置为 "module"，并使用 import 语句。

您还可以在运行时加载外部库，只需在调用 scripting.executeScript() 时将外部库添加到 files 数组即可。您仍然可以在运行时远程加载数据。

如果您需要更加生动，可以使用 scripting.executeScript() 中的新 func 属性来注入作为内容脚本的函数，并使用 args 属性传递变量。

在后台 Service Worker 中。

Chrome 扩展程序示例代码库包含一个函数注入示例，您可以逐步演示该示例。如需查看 getCurrentTab() 的示例，请参阅该函数的参考文档。

如果上述方法对您的用例没有帮助，您可能需要寻找替代解决方案（例如迁移到其他库），或者寻找其他方法来使用该库的功能。例如，对于 Google Analytics，您可以改用 Google Measurement Protocol，而不是使用 Google Analytics 4 指南中所述的官方远程托管 JavaScript 版本。

"content_security_policy" 尚未从 manifest.json 文件中移除，但它现在是一个支持两个属性的字典："extension_pages" 和 "sandbox"。

extension_pages：是指扩展程序中的上下文，包括 HTML 文件和 Service Worker。

sandbox：是指您的扩展程序使用的任何沙盒化扩展程序页面。

Manifest V3 不允许在 "extension_pages" 字段中使用 Manifest V2 允许使用的某些内容安全政策值。具体而言，Manifest V3 禁止使用允许远程执行的代码。script-src, object-src 和 worker-src 指令只能具有以下值：

sandbox 的内容安全政策值没有此类新限制。

**Examples:**

Example 1 (unknown):
```unknown
executeScript()
```

Example 2 (unknown):
```unknown
new Function()
```

Example 3 (unknown):
```unknown
chrome.runtime.getURL()
```

Example 4 (unknown):
```unknown
new Function(...)
```

---

## Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/getstarted/development-basics?hl=zh-cn

**Contents:**
- Hello World 扩展 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- Hello World
- 加载未打包的扩展程序
- 固定扩展程序
- 重新加载扩展程序
  - 何时重新加载扩展程序
- 查找控制台日志和错误
  - 控制台日志
  - 错误日志

通过构建您的第一个“Hello World”扩展程序，了解 Chrome 扩展程序开发的基础知识。

您将创建一个“Hello World”示例，在本地加载扩展程序，查找日志，并探索其他建议。

当用户点击扩展程序工具栏图标时，此扩展程序将显示“Hello Extensions”。

首先，创建一个用于存储扩展程序文件的新目录。如果您愿意，也可以从 GitHub 下载完整源代码。

接下来，在此目录中创建一个名为 manifest.json 的新文件。此 JSON 文件描述了扩展程序的功能和配置。例如，大多数清单文件都包含 "action" 键，用于声明 Chrome 应将哪张图片用作扩展程序的操作图标，以及在用户点击扩展程序的操作图标时在弹出式窗口中显示的 HTML 网页。

将图标下载到您的目录中，并务必更改其名称，使其与 "default_icon" 键中的名称一致。

针对弹出式窗口，创建一个名为 hello.html 的文件，并添加以下代码：

现在，当用户点击扩展程序的操作图标（工具栏图标）时，该扩展程序会显示一个弹出式窗口。您可以通过在本地加载该测试页面来测试它。确保所有文件均已保存。

如需在开发者模式下加载未封装的扩展程序，请执行以下操作：

大功告成！扩展程序已成功安装。如果清单中未包含任何扩展程序图标，系统会为扩展程序创建一个通用图标。

默认情况下，当您在本地加载扩展程序时，它会显示在扩展程序菜单 () 中。将扩展程序固定到工具栏，以便在开发过程中快速访问扩展程序。

点击扩展程序的操作图标（工具栏图标）；您应该会看到一个弹出式窗口。

返回代码，然后在清单中将扩展程序的名称更改为“Hello Extensions of the world!”。

保存文件后，您还必须刷新扩展程序，才能在浏览器中看到此更改。前往“附加信息”页面，然后点击开启/关闭切换开关旁边的刷新图标：

下表显示了哪些组件需要重新加载才能看到更改：

在开发期间，您可以通过访问浏览器控制台日志来调试代码。在本例中，我们将找到弹出式窗口的日志。首先，将脚本标记添加到 hello.html。

创建一个 popup.js 文件，并添加以下代码。

如需在控制台中查看系统记录的这条消息，请执行以下操作：

现在，我们来破坏一下扩展程序。为此，我们可以移除 popup.js 中的闭引号：

前往“扩展程序”页面，然后打开弹出式窗口。系统随即会显示一个错误按钮。

如需详细了解如何调试服务工件、选项页面和内容脚本，请参阅调试扩展程序。

您可以通过多种方式构建扩展程序项目；不过，唯一的前提是将 manifest.json 文件放在扩展程序的根目录中，如以下示例所示：

如果您使用代码编辑器进行开发，则可以使用 npm 软件包 chrome-types 来利用 Chrome API 的自动补全功能。当 Chromium 源代码发生变化时，此 npm 软件包会自动更新。

选择以下任一教程，开始您的扩展程序学习之旅。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

Example 2 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "name": "Hello Extensions",
  "description": "Base Level Extension",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "hello.html",
    "default_icon": "hello_extensions.png"
  }
}
```

Example 4 (unknown):
```unknown
"default_icon"
```

---

## 代管式存储空间的清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/storage?hl=zh-cn

**Contents:**
- 代管式存储空间的清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- manifest.json 示例
- 架构格式
- 示例架构

与 local 和 sync 存储区域不同，managed 存储区域的结构必须为 声明为 JSON 架构，并经过 Chrome 的严格验证。此架构必须存储在 （由 "storage" 清单键的 "managed_schema" 属性指示）文件，并声明 支持的企业政策。

政策类似于选项 由系统管理员配置 针对安装了政策的扩展程序，允许针对 组织内的所有用户有关示例，请参阅 Chrome 如何处理政策 。

声明政策后，您可以通过 storage.managed API 读取政策。这取决于 扩展程序以强制执行管理员配置的政策。

storage.managed_schema 属性表示扩展名中包含该政策的文件 架构。

然后，Chrome 会从基础操作系统和 Google Apps for Business 加载这些政策。 已登录的用户只要检测到政策更改，就会触发 storage.onChanged 事件。 您可以访问 chrome://policy 验证 Chrome 已加载的政策。

对于 JSON 架构格式，Chrome 还需遵循一些额外要求：

如果架构无效，则 Chrome 不会加载该扩展程序，并会说明 架构未经过验证。如果政策值不符合架构，则不会 由 storage.managed API 发布。

**Examples:**

Example 1 (unknown):
```unknown
"managed_schema"
```

Example 2 (unknown):
```unknown
storage.managed_schema
```

Example 3 (unknown):
```unknown
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

---

## 跨源嵌入器政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/cross_origin_embedder_policy?hl=zh-cn

**Contents:**
- 跨源嵌入器政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明

借助 cross_origin_embedder_policy 清单键，扩展程序可以指定 针对扩展程序的请求的 Cross-Origin-Embedder-Policy (COEP) 响应标头 来源。这包括扩展程序的 Service Worker、弹出式窗口、选项页面、打开某个扩展程序资源的标签页等。

此键与 cross_origin_opener_policy 结合使用，可允许扩展程序 跨域隔离

cross_origin_embedder_policy 清单键包含一个对象，该对象包含一个 名为 value 的属性，该属性接受字符串。Chrome 会将此字符串用作 Cross-Origin-Embedder-Policy 标头。例如：

**Examples:**

Example 1 (unknown):
```unknown
cross_origin_embedder_policy
```

Example 2 (unknown):
```unknown
cross_origin_embedder_policy
```

Example 3 (unknown):
```unknown
Cross-Origin-Embedder-Policy
```

Example 4 (unknown):
```unknown
{
    ...
    "cross_origin_embedder_policy": {
      "value": "require-corp"
    },
    ...
}
```

---

## 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating?hl=zh-cn

**Contents:**
- 迁移到 Manifest V3 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保留当前的功能集
- 新的扩展程序平台功能

将 Manifest V2 扩展程序转换为 Manifest V3 扩展程序的指南。

此部分可帮助您将扩展程序从 Manifest V2 升级到 Manifest V3（Chrome 扩展程序平台的最新版本）。迁移工作大致分为以下几类。为帮助您跟踪工作进度，我们提供了一份核对清单，总结了这些文档的内容。您可以通过核对清单查看相关内容，也可以深入了解相关内容。两个路径均以升级版附加信息结尾。

我们还提供 Extension Manifest Converter。它无法为您提供一切服务，但可帮助您入门。转换器的 README 文件中介绍了工具更改的内容。

为了降低出现意外问题或 bug 的可能性，我们建议不要在迁移时添加新功能。例如，添加需要新权限的功能可能会触发权限警告，这会导致您的扩展程序停用，直到用户接受新权限。请参阅权限警告最佳做法，了解如何在不显示警告的情况下添加权限。

Chrome 88 或更高版本通常支持 Manifest V3。更新 API 调用时，您可能会发现替换功能可能要到版本 88 之后才在 Chrome 中推出。API 参考页面包含各 API 成员的支持信息。如果您发现需要使用其中某项功能，可以在清单文件中指定最低 Chrome 版本。

自 Manifest V3 发布以来，我们不断添加新功能，其中许多功能在 Manifest V2 和 Manifest V3 中均可使用。在转换时，您并不需要使用这些组件；但是，当它们取代旧功能时，您应优先使用这些功能而不是它们所取代的功能，并且预计被替换的功能最终会被弃用和移除。

**Examples:**

Example 1 (unknown):
```unknown
manifest.json
```

---

## Manifest V2 支持时间表 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/mv2-deprecation-timeline?hl=zh-cn

**Contents:**
- Manifest V2 支持时间表 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
  - 2025 年 7 月 24 日：在所有位置停用 Manifest V2
  - 2025 年 3 月 31 日：停用 Manifest V2，但可以选择重新启用扩展程序
  - 2024 年 10 月 9 日：关于 Manifest V2 淘汰的最新动态。
  - 2024 年 6 月 3 日：开始逐步淘汰 Manifest V2。
  - 2022 年 6 月：Chrome 应用商店 - 不再接受新的专用扩展程序
  - 2022 年 1 月：Chrome 应用商店 - 无新的公开 / 不公开列出的扩展程序

了解 Manifest V2 何时会停止支持扩展程序

在 Chrome 138 中，所有 Chrome 渠道的所有用户现在都已停用 Manifest V2 扩展程序。用户无法再重新启用这些功能。

对于企业，ExtensionManifestV2Availability 政策将在 Chrome 139 中移除。此项变更将同时影响 Chrome 139 上的所有用户。

因此，对于升级到 Chrome 139 及后续版本的任何用户，Manifest V2 扩展程序都将无法再正常运行。 Chromium 发布时间表提供了更多发布信息。

现在，所有 Chrome 渠道的所有用户默认情况下都已停用 Manifest V2 扩展程序，但用户仍然可以重新启用 Manifest V2 扩展程序。第二阶段（用户无法再重新启用这些功能）已开始向 Canary 中的部分用户推出。这项变更将继续缓慢地向更多用户推出。

与之前一样，使用 ExtensionManifestV2Availability 政策的企业将继续不受任何浏览器变更的影响，至少到 2025 年 6 月为止。从 6 月开始，Chrome 139 分支将开始，届时 Chrome 将不再支持 Manifest V2 扩展程序。与之前逐步向用户推出的停用 Manifest V2 扩展程序的变更不同，此变更将立即影响 Chrome 139 上的所有用户。因此，Chrome 138 是支持 Manifest V2 扩展程序（与 ExtensionManifestV2Availability 键搭配使用时）的最后一个 Chrome 版本。您可以在 Chromium 发布时间表中找到有关 Chrome 138 和 139 的发布信息，包括 ChromeOS 的 LTS 支持。

在过去几个月里，我们一直在逐步淘汰清单 V2。 目前，chrome://extensions 页面会向 Manifest V2 扩展程序的所有用户显示警告横幅。此外，我们已开始在预稳定版渠道中停用 Manifest V2 扩展程序。

我们现在将开始在 Chrome 稳定版中停用仍在使用 Manifest V2 的已安装扩展程序。这项变更将在未来几周内逐步推出。 用户将被引导至 Chrome 应用商店，系统会向他们推荐已停用扩展程序的 Manifest V3 替代方案。在短时间内，用户仍可重新启用 Manifest V2 扩展程序。使用 ExtensionManifestV2Availability 政策的企业将不受任何浏览器变更的影响，直到 2025 年 6 月。如需了解更多背景信息，请参阅我们的2024 年 5 月博客。

从 6 月 3 日开始，在 Chrome Beta 版、Dev 版和 Canary 版渠道中，如果用户仍安装了 Manifest V2 扩展程序，那么当他们访问扩展程序管理页面 (chrome://extensions) 时，部分用户会开始看到警告横幅，告知他们所安装的部分（Manifest V2）扩展程序很快将不再受支持。与此同时，仍在使用 Manifest V2 的获“精选”徽章的扩展程序将失去其徽章。

Chrome 应用商店已停止接受将公开范围设置为“专用”的新 Manifest V2 扩展程序。

Chrome 网上应用店已停止接受新的 Manifest V2 扩展程序，且这些扩展程序的公开范围设置为“公开”或“不公开”。移除了将 Manifest V2 扩展程序从“不公开”更改为“公开”或“不公开列出”的功能。

**Examples:**

Example 1 (unknown):
```unknown
ExtensionManifestV2Availability
```

---

## 清单 - 版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/version?hl=zh-cn

**Contents:**
- 清单 - 版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 版本名称

一到四个以英文句点分隔的整数，用于标识此扩展程序的版本。下面几条规则适用于整数：

如果已发布的扩展程序的版本字符串比已安装的扩展程序更新，则该扩展程序会自动更新。

比较从最左边的整数开始。然后，如果这些整数相等，则比较右侧的整数，依此类推。例如，1.2.0 是比 1.1.9.9999 更新的版本。

缺少的整数等于零。例如，1.1.9.9999 比 1.1 更新，1.1.9.9999 低于 1.2。

除了用于更新的 "version" 字段之外，"version_name" 还可设置为描述性的版本字符串，并将用于显示目的（如果存在）。

如果不存在 version_name，则版本字段也将用于显示。

**Examples:**

Example 1 (unknown):
```unknown
"version": "1"
```

Example 2 (unknown):
```unknown
"version": "1.0"
```

Example 3 (unknown):
```unknown
"version": "2.10.2"
```

Example 4 (unknown):
```unknown
"version": "3.1.2.4567"
```

---

## 清单 - 名称 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/name?hl=zh-cn

**Contents:**
- 清单 - 名称 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"name" 键（必需）是一个简短的纯文本字符串（最多 75 个字符） 字符）。例如：

您可以指定特定于语言区域的字符串；请参阅国际化 了解详情。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension name"
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension name"
}
```

---

## 代管式存储空间的清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/storage

**Contents:**
- 代管式存储空间的清单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- manifest.json 示例
- 架构格式
- 示例架构

与 local 和 sync 存储区域不同，managed 存储区域的结构必须为 声明为 JSON 架构，并经过 Chrome 的严格验证。此架构必须存储在 （由 "storage" 清单键的 "managed_schema" 属性指示）文件，并声明 支持的企业政策。

政策类似于选项 由系统管理员配置 针对安装了政策的扩展程序，允许针对 组织内的所有用户有关示例，请参阅 Chrome 如何处理政策 。

声明政策后，您可以通过 storage.managed API 读取政策。这取决于 扩展程序以强制执行管理员配置的政策。

storage.managed_schema 属性表示扩展名中包含该政策的文件 架构。

然后，Chrome 会从基础操作系统和 Google Apps for Business 加载这些政策。 已登录的用户只要检测到政策更改，就会触发 storage.onChanged 事件。 您可以访问 chrome://policy 验证 Chrome 已加载的政策。

对于 JSON 架构格式，Chrome 还需遵循一些额外要求：

如果架构无效，则 Chrome 不会加载该扩展程序，并会说明 架构未经过验证。如果政策值不符合架构，则不会 由 storage.managed API 发布。

**Examples:**

Example 1 (unknown):
```unknown
"managed_schema"
```

Example 2 (unknown):
```unknown
storage.managed_schema
```

Example 3 (unknown):
```unknown
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

---

## 清单 - 说明 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/description

**Contents:**
- 清单 - 说明 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

纯文本字符串（无 HTML 或其他格式；不超过 132 个字符），用于描述 。例如：

说明应同时适用于浏览器的“扩展程序”页面 (chrome://extensions) 和 Chrome 应用商店。您可以为此字段指定特定于语言区域的字符串；请参阅 国际化。

**Examples:**

Example 1 (unknown):
```unknown
"description": "A description of my extension"
```

Example 2 (unknown):
```unknown
"description": "A description of my extension"
```

---

## 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/key?hl=zh-cn

**Contents:**
- 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保持一致的扩展程序 ID
  - 将扩展程序上传到开发者信息中心
  - 比较 ID

此值用于在开发期间加载扩展程序或主题时维护其唯一 ID。以下是一些常见使用场景：

在开发过程中，保留单个 ID 至关重要。如需保持一致的 ID，请按以下步骤操作：

将扩展程序目录打包到 .zip 文件中，并将其上传到 Chrome 开发者信息中心，但不要发布：

将代码添加到 "key" 字段下的 manifest.json。这样，扩展程序将使用相同的 ID。

打开 chrome://extensions 中的“扩展程序管理”页面，确保已启用开发者模式，然后上传未打包的扩展程序目录。将扩展程序管理页面上的扩展程序 ID 与开发者信息中心内的商品 ID 进行比较。它们应保持一致。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
-----BEGIN PUBLIC KEY-----
```

Example 3 (unknown):
```unknown
-----END PUBLIC KEY-----
```

Example 4 (unknown):
```unknown
manifest.json
```

---

## 跨源网络请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/xhr?hl=zh-cn

**Contents:**
- 跨源网络请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 扩展程序来源
- 请求跨源权限
- Fetch() 与 XMLHttpRequest()
- 安全注意事项
  - 避免跨站脚本漏洞
  - 限制内容脚本对跨源请求的访问权限
  - 优先使用 HTTPS（而非 HTTP）
  - 调整内容安全政策

常规网页可以使用 fetch() 或 XMLHttpRequest API 与远程服务器发送和接收数据，但受到同源政策的限制。内容脚本代表内容脚本注入到的 Web 来源发起请求，因此内容脚本也受同源政策的约束。扩展程序来源并非如此受限。在扩展程序 Service Worker 或前台标签页中执行的脚本可以与其来源之外的远程服务器通信，前提是该扩展程序请求了主机权限。

每个正在运行的扩展程序都位于自己的单独安全源中。无需请求其他特权，扩展程序即可调用 fetch() 来获取其安装中的资源。例如，如果某个扩展程序在 config_resources/ 文件夹中包含名为 config.json 的 JSON 配置文件，则该扩展程序可以按如下方式检索该文件的内容：

如果扩展程序尝试从自身以外的安全源（例如 https://www.google.com）请求内容，除非该扩展程序具有主机权限，否则系统会将其视为跨源请求。在内容脚本中，跨源请求始终会被视为跨源请求，即使扩展程序具有主机权限也是如此。

如需请求访问扩展程序来源之外的远程服务器，请将主机、匹配模式或二者添加到manifest文件的 host_permissions 部分。

匹配模式“https://*/”允许通过 HTTPS 访问所有可访问的网域。请注意，此处的匹配模式与内容脚本匹配模式类似，但系统会忽略主机后面的任何路径信息。

另请注意，系统会按主机和架构授予访问权限。如果扩展程序同时需要对给定主机或一组主机拥有安全和不安全的 HTTP 访问权限，则必须单独声明这些权限：

fetch() 专为服务工件而创建，遵循了远离同步操作的更广泛 Web 趋势。扩展程序在 Service Worker 之外支持 XMLHttpRequest() API，调用该 API 会触发扩展程序 Service Worker 的提取处理脚本。新工作应尽可能采用 fetch()。

使用通过 fetch() 检索的资源时，您的屏幕外文档、侧边栏或弹出式窗口应注意不要遭到跨网站脚本攻击。具体而言，请避免使用 innerHTML 等危险 API。例如：

相反，请优先使用不会运行脚本的更安全的 API：

代表内容脚本执行跨源请求时，请务必防范可能尝试冒充内容脚本的恶意网页。特别是，请勿允许内容脚本请求任意网址。

请考虑以下示例：一个扩展程序执行跨源请求，以便内容脚本发现商品的价格。一种不太安全的方法是让内容脚本指定后台页面要提取的确切资源。

在上述方法中，内容脚本可以请求扩展程序提取扩展程序有权访问的任何网址。恶意网页可能会伪造此类消息，并诱骗扩展程序授予对跨源资源的访问权限。

而是设计消息处理脚本，以限制可提取的资源。在下面的示例中，内容脚本仅提供 itemId，而非完整网址。

此外，请特别注意通过 HTTP 检索的资源。如果您的扩展程序在恶意网络上使用，网络攻击者（也称为"man-in-the-middle"）可能会修改响应，并可能攻击您的扩展程序。相反，请尽可能使用 HTTPS。

如果您通过向清单添加 content_security_policy 属性来修改扩展程序的默认内容安全政策，则需要确保您要连接的所有主机都已获准。虽然默认政策不会限制与主机的连接，但在明确添加 connect-src 或 default-src 指令时，请务必小心。

**Examples:**

Example 1 (unknown):
```unknown
XMLHttpRequest
```

Example 2 (unknown):
```unknown
config_resources/
```

Example 3 (unknown):
```unknown
config.json
```

Example 4 (javascript):
```javascript
const response = await fetch('/config_resources/config.json');
const jsonData = await response.json();
```

---

## 清单 - short_name 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/short-name

**Contents:**
- 清单 - short_name 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，用于定义扩展程序名称的简短版本（建议不超过 12 个字符）。如果未指定此键，将使用 "name" 键的截断版本。简称通常用于因空间不足而无法显示全称的地方。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "short_name": "Short Name"
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "short_name": "Short Name"
  // ...
}
```

---

## 覆盖 Chrome 设置 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/chrome-settings-override?hl=zh-cn

**Contents:**
- 覆盖 Chrome 设置 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 首页、搜索服务提供商和启动页
- 自定义值
- 参考

设置覆盖是扩展程序覆盖所选 Chrome 设置的一种方式。API 是 。

下面的示例展示了如何修改首页、搜索服务提供商和启动页 在扩展程序清单中。Settings API 中使用的任何网域都必须经过验证（通过 Google Search Console）。请注意，如果 验证对某个网域（例如 https://example.com）的所有权 可以使用任何子网域或网页 （例如 https://app.example.com 或 https://example.com/page.html）。

如果使用设置覆盖权限来请求获取任何其他功能或权限，这不符合我们的单一用途政策。当 Chrome 检测到某项内容可能违反了我们的单一用途政策时，会向用户显示确认对话框。只修改某项设置而不寻求其他功能或权限的扩展程序不会显示确认对话框。

这适用于 Chrome 107 及更高版本。

对于外部扩展程序，search_provider、homepage 和 startup_pages 网址值可以 并使用注册表项参数化。在 "update_url" 键（请参阅此处的说明）。键名为 "install_parameter"，值为 是任意字符串：

清单网址中出现的子字符串 "__PARAM__" 都将替换为 "install_parameter" 值。如果 "install_parameter" 不存在，则 "__PARAM__" 的出现次数为 已移除。请注意，"__PARAM__" 不能是主机名的一部分。它必须在 第一个“/”。

扩展程序可以替换清单中的以下一个或多个属性：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "chrome_settings_overrides": {
    "homepage": "https://www.homepage.com",
    "search_provider": {
        "name": "name.__MSG_url_domain__",
        "keyword": "keyword.__MSG_url_domain__",
        "search_url": "https://www.foo.__MSG_url_domain__/s?q={searchTerms}",
        "favicon_url": "https://www.foo.__MSG_url_domain__/favicon.ico",
        "suggest_url": "https://www.foo.__MSG_url_domain__/suggest?q={searchTerms}",
        "instant_url": "https://www.foo.__MSG_url_domain__/instant?q={searchTerms}",
        "image_url": "https://www.foo.__MSG_url_domain__/image?q={searchTerms}",
        "search_url_post_params": "search_lang=__MSG_url_domain__",
        "suggest_url_post_params": "suggest_lang=__MSG_url_domain__",
        "instant_url_post_params": "instant_lang=__MSG_url_domain__",
        "image_url_post_params": "image_lang=__MSG_url_domain__",
        "alternate_urls": [
          "https://www.moo.__MSG_url_domain__/s?q={searchTerms}",
          "https://www.noo.__MSG_url_domain__/s?q={searchTerms}"
        ],
        "encoding": "UTF-8",
        "is_default": true
    },
    "startup_pages": ["https://www.startup.com"]
   },
   "default_locale": "de",
   ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "chrome_settings_overrides": {
    "homepage": "https://www.homepage.com",
    "search_provider": {
        "name": "name.__MSG_url_domain__",
        "keyword": "keyword.__MSG_url_domain__",
        "search_url": "https://www.foo.__MSG_url_domain__/s?q={searchTerms}",
        "favicon_url": "https://www.foo.__MSG_url_domain__/favicon.ico",
        "suggest_url": "https://www.foo.__MSG_url_domain__/suggest?q={searchTerms}",
        "instant_url": "https://www.foo.__MSG_url_domain__/instant?q={searchTerms}",
        "image_url": "https://www.foo.__MSG_url_domain__/image?q={searchTerms}",
        "search_url_post_params": "search_lang=__MSG_url_domain__",
        "suggest_url_post_params": "suggest_lang=__MSG_url_domain__",
        "instant_url_post_params": "instant_lang=__MSG_url_domain__",
        "image_url_post_params": "image_lang=__MSG_url_domain__",
        "alternate_urls": [
          "https://www.moo.__MSG_url_domain__/s?q={searchTerms}",
          "https://www.noo.__MSG_url_domain__/s?q={searchTerms}"
        ],
        "encoding": "UTF-8",
        "is_default": true
    },
    "startup_pages": ["https://www.startup.com"]
   },
   "default_locale": "de",
   ...
}
```

Example 3 (unknown):
```unknown
search_provider
```

Example 4 (unknown):
```unknown
startup_pages
```

---

## 清单版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/manifest-version?hl=zh-cn

**Contents:**
- 清单版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

一个整数，用于指定您的软件包所需的清单文件格式版本。必须提供此键。例如：

当前版本为 Manifest V3。Chrome 应用商店不再接受 Manifest V2 扩展程序 （如需了解详情，请参阅 Manifest V2 支持时间表）。系统还会提供 版本（V4 及更高版本），但这些映像尚未制定发布计划。

**Examples:**

Example 1 (unknown):
```unknown
"manifest_version": 3
```

Example 2 (unknown):
```unknown
"manifest_version": 3
```

---

## 清单 - 图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/icons

**Contents:**
- 清单 - 图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

代表扩展程序或主题的一个或多个图标。您应始终提供 128x128 的图标； 安装期间以及由 Chrome 应用商店使用。附加信息还应提供 48x48 像素 图标，该图标在扩展程序管理页面 (chrome://extensions) 中使用。您还可以指定一个 16x16 的图标，用作扩展程序页面的网站图标。

图标通常应采用 PNG 格式，因为 PNG 可最有效地支持透明度。他们 不过，可以采用 Blink 支持的任何光栅格式，包括 BMP、GIF、ICO 和 JPEG。

如需详细了解 Chrome 应用商店的要求和最佳实践，请参阅扩展程序图标。

**Examples:**

Example 1 (unknown):
```unknown
"icons": {
    "16": "icon16.png",
    "32": "icon32.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
```

Example 2 (unknown):
```unknown
"icons": {
    "16": "icon16.png",
    "32": "icon32.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
```

---

## 清单 - 图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/icons?hl=zh-cn

**Contents:**
- 清单 - 图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

代表扩展程序或主题的一个或多个图标。您应始终提供 128x128 的图标； 安装期间以及由 Chrome 应用商店使用。附加信息还应提供 48x48 像素 图标，该图标在扩展程序管理页面 (chrome://extensions) 中使用。您还可以指定一个 16x16 的图标，用作扩展程序页面的网站图标。

图标通常应采用 PNG 格式，因为 PNG 可最有效地支持透明度。他们 不过，可以采用 Blink 支持的任何光栅格式，包括 BMP、GIF、ICO 和 JPEG。

如需详细了解 Chrome 应用商店的要求和最佳实践，请参阅扩展程序图标。

**Examples:**

Example 1 (unknown):
```unknown
"icons": {
    "16": "icon16.png",
    "32": "icon32.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
```

Example 2 (unknown):
```unknown
"icons": {
    "16": "icon16.png",
    "32": "icon32.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
```

---

## 清单 - 说明 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/description?hl=zh-cn

**Contents:**
- 清单 - 说明 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

纯文本字符串（无 HTML 或其他格式；不超过 132 个字符），用于描述 。例如：

说明应同时适用于浏览器的“扩展程序”页面 (chrome://extensions) 和 Chrome 应用商店。您可以为此字段指定特定于语言区域的字符串；请参阅 国际化。

**Examples:**

Example 1 (unknown):
```unknown
"description": "A description of my extension"
```

Example 2 (unknown):
```unknown
"description": "A description of my extension"
```

---

## 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/improve-security

**Contents:**
- 提高扩展程序的安全性 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 移除执行任意字符串
- 移除远程托管的代码
  - 配置驱动型功能和逻辑
  - 使用远程服务的外部化逻辑
  - 在沙盒化 iframe 中嵌入远程托管的代码
  - 捆绑第三方库
  - 在标签页注入的脚本中使用外部库
  - 注入函数
  - 寻找其他解决方法

这是介绍不属于扩展程序服务工作线程的代码所需更改的第三部分。其中介绍了提高扩展程序安全性所需的更改。另外两个部分介绍了升级到 Manifest V3 所需的更新代码和替换屏蔽 Web 请求。

您无法再使用 executeScript()、eval() 和 new Function() 执行外部逻辑。

executeScript() 方法现在位于 scripting 命名空间中，而不是 tabs 命名空间中。如需了解如何更新通话，请参阅移动 executeScript()。

在少数特殊情况下，仍然可以执行任意字符串：

在 Manifest V3 中，扩展程序的所有逻辑都必须包含在扩展程序软件包中。根据 Chrome 应用商店政策，您将无法再加载和执行远程托管的文件。例如：

您可以采用其他方法，具体取决于您的用例和远程托管的原因。本部分介绍了可考虑的方法。如果您在处理远程托管代码时遇到问题，可参阅相关指南。

您的扩展程序会在运行时加载并缓存远程配置（例如 JSON 文件）。缓存的配置决定了启用了哪些功能。

您的扩展程序调用远程 Web 服务。这样，您就可以将代码保持私密状态，并根据需要进行更改，同时避免重新提交到 Chrome 应用商店的额外开销。

沙盒化 iframe 支持远程托管的代码。请注意，如果代码需要访问嵌入页面的 DOM，则此方法不起作用。

如果您使用的是之前从外部服务器加载的流行框架（例如 React 或 Bootstrap），则可以下载缩小的文件，将其添加到您的项目并在本地导入。例如：

如需在 Service Worker 中加入库，请在清单中将 "background.type" 键设置为 "module"，并使用 import 语句。

您还可以在运行时加载外部库，只需在调用 scripting.executeScript() 时将外部库添加到 files 数组即可。您仍然可以在运行时远程加载数据。

如果您需要更加生动，可以使用 scripting.executeScript() 中的新 func 属性来注入作为内容脚本的函数，并使用 args 属性传递变量。

在后台 Service Worker 中。

Chrome 扩展程序示例代码库包含一个函数注入示例，您可以逐步演示该示例。如需查看 getCurrentTab() 的示例，请参阅该函数的参考文档。

如果上述方法对您的用例没有帮助，您可能需要寻找替代解决方案（例如迁移到其他库），或者寻找其他方法来使用该库的功能。例如，对于 Google Analytics，您可以改用 Google Measurement Protocol，而不是使用 Google Analytics 4 指南中所述的官方远程托管 JavaScript 版本。

"content_security_policy" 尚未从 manifest.json 文件中移除，但它现在是一个支持两个属性的字典："extension_pages" 和 "sandbox"。

extension_pages：是指扩展程序中的上下文，包括 HTML 文件和 Service Worker。

sandbox：是指您的扩展程序使用的任何沙盒化扩展程序页面。

Manifest V3 不允许在 "extension_pages" 字段中使用 Manifest V2 允许使用的某些内容安全政策值。具体而言，Manifest V3 禁止使用允许远程执行的代码。script-src, object-src 和 worker-src 指令只能具有以下值：

sandbox 的内容安全政策值没有此类新限制。

**Examples:**

Example 1 (unknown):
```unknown
executeScript()
```

Example 2 (unknown):
```unknown
new Function()
```

Example 3 (unknown):
```unknown
chrome.runtime.getURL()
```

Example 4 (unknown):
```unknown
new Function(...)
```

---

## 清单 - oauth2 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/oauth2

**Contents:**
- 清单 - oauth2 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

一个可选的清单密钥，支持在扩展程序中使用 OAuth 2.0 安全 ID。此键接受包含两个必需子属性的对象："client_id" 和 "scopes"。在开发使用 "oauth2" 键的扩展程序时，还应考虑设置扩展程序的 "key" 以保持一致的扩展程序 ID。

如需更详细的实现说明，请访问完整的 OAuth 2.0 教程。

**Examples:**

Example 1 (unknown):
```unknown
"client_id"
```

Example 2 (unknown):
```unknown
{
  // ...
     "oauth2": {
      "client_id": "YOUR_EXTENSION_OAUTH_CLIENT_ID.apps.googleusercontent.com",
      "scopes": ["https://www.googleapis.com/auth/contacts.readonly"]
    },
    "key": "EXTENSION_PUBLIC_KEY",
  // ...
}
```
```

Example 3 (unknown):
```unknown
{
  // ...
     "oauth2": {
      "client_id": "YOUR_EXTENSION_OAUTH_CLIENT_ID.apps.googleusercontent.com",
      "scopes": ["https://www.googleapis.com/auth/contacts.readonly"]
    },
    "key": "EXTENSION_PUBLIC_KEY",
  // ...
}
```
```

---

## 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/background?hl=zh-cn

**Contents:**
- 清单 - 背景 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，用于将 JavaScript 文件指定为扩展程序 Service Worker。Service Worker 是充当扩展程序的主要事件处理程序的后台脚本。如需了解详情，请参阅更全面的 Service Worker 简介。

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
   "background": {
      "service_worker": "service-worker.js",
      "type": "module"
    },
  ...
}
```

---

## 使用 Web 推送 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/web-push?hl=zh-cn

**Contents:**
- 使用 Web 推送 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
  - 获取使用 Push API 的权限
  - 推送提供程序和推送服务
  - 自行托管推送提供商
  - 静默推送

在扩展程序中，您可以使用任何推送提供程序发送推送通知和 消息。来自 Push API 的推送将作为 并在收到请求后立即处理如果 Service Worker 已被挂起，则 Push 将 再唤醒它。在扩展程序中使用它的流程与 可以在开放网络中使用

在普通网站上注册推送服务器时，用户会看到一个 授予或拒绝它的权限提示。如果使用扩展程序， 。要在您的扩展程序中使用 Push API，您需要将 manifest.json 中的 notifications 权限

如果您缺少此权限，那么与 registration.pushManager 将导致立即发生错误，结果与 如果用户拒绝了该权限，则会发生此错误。另请注意， notifications 权限将导致权限警告 在安装时显示Chrome 还会停用 现有安装，直到用户批准新权限请求。您可以 请参阅 权限警告指南。

将权限添加到 manifest.json 后，您需要 配置后端与扩展程序之间的连接。此连接 可以分为两部分：推送提供程序和推送服务。答 provider 是您用来向推送服务发送消息的 SDK。 有许多不同的选项，任何推送提供程序都可以用于推送 API（尽管它们可能不会提供可以轻松集成的 SDK）。您 需要对您的提供商的 SDK 进行实验，看看能否实现。推 服务是最终用户设备注册时使用的服务，因此系统可以 发送到推送提供程序发送的任何推送消息。您并不需要 因为它已硬编码到各个浏览器中。对于 Chrome，Firebase Cloud Messaging 是一项推送服务。推送到 Chrome 的任何消息 用户将通过它进行路由

任何推送提供程序都可以运行，但并非所有提供程序都提供有效的 SDK Service Worker 中的资源。如果您遇到问题，需要咨询您的提供商 确保它正常运行不过，您无需使用公共提供商。使用 web-push 等库，您可以托管自己的后端。

您可以使用 web-push-codelab.glitch.me.具体来说，您需要 复制推送服务器的 VAPID 公钥，以便生成推送 订阅。此公钥实际上是 base64 需要解码并转换为 Uint8Array，以便向浏览器的推送功能注册 管理员。有一些库可用于执行此逻辑 只需执行以下操作即可。

subscribe 函数会返回 PushSubscription， 对象，该对象包含推送服务器的元数据。由于您使用的是 web-push-codelab.glitch.me，则需要将此值复制到 页面的“推送订阅”部分

有了 PushSubscription 后，您就可以为 在我们的扩展程序的 Service Worker 中推送消息。

安装好监听器后，您就可以通过 web-push-codelab.glitch.me，然后系统就会将消息记录到 Service Worker 的控制台。

由于它是一种开放式网络标准， 如何实现网络推送，包括在 Chrome 博客上。对于 该示例的完整版本， 扩展程序示例代码库。

您过去可以在 Manifest V3 扩展程序中收到推送通知 从 Chrome 88 中引入 Manifest V3。不过，过去一直有 要求通知显示某种用户可见提示， （如网络通知）。这就会大幅降低 希望将命令或数据更新推送到您的扩展程序，而不费心 提供不必要的信息自 Chrome 121 起，扩展程序 能够将 userVisibleOnly 设为 false。您现在可以发送 不向用户显示的静默推送通知。要使用这项功能 在调用 pushManager.subscribe 时，将 userVisibleOnly 设置为 false。

**Examples:**

Example 1 (unknown):
```unknown
notifications
```

Example 2 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 3 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 4 (unknown):
```unknown
registration.pushManager
```

---

## 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/minimum-chrome-version?hl=zh-cn

**Contents:**
- 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 强制执行
  - 新安装次数
  - 现有安装

可选的清单键，包含一个字符串，该字符串定义了 Chrome 可以安装该扩展程序。为此字符串设置的值必须是现有 Chrome 浏览器版本字符串的子字符串。使用完整版 数字可指定 Chrome 的特定更新，也可使用 字符串以指定特定的主要版本。

在低于最低版本的 Chrome 版本中，Chrome 应用商店会显示“不兼容”消息，而不是安装按钮。这些用户 版本将无法安装您的扩展程序。

您的扩展程序的现有用户 minimum_chrome_version版本高于目前的浏览器版本。此操作会以静默方式进行，因此您应谨慎行事，并考虑如何让现有用户知道他们不再收到更新。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 3 (unknown):
```unknown
minimum_chrome_version
```

Example 4 (unknown):
```unknown
minimum_chrome_version
```

---

## file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/file-handlers?hl=zh-cn

**Contents:**
- file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"file_handlers" 清单键用于指定 ChromeOS 扩展程序要处理的文件类型。如需处理文件，请使用 Web 平台的 Launch Handler API。如需了解特定于扩展程序的信息，请参阅文件处理。

**Examples:**

Example 1 (unknown):
```unknown
"file_handlers"
```

Example 2 (unknown):
```unknown
"file_handlers": [
  {
    "action": "/open_text.html",
    "name": "Plain text",
    "accept": {
      "text/plain": [".txt"]
    }
    "launch_type": "single-client"
  }
]
```

Example 3 (unknown):
```unknown
"file_handlers": [
  {
    "action": "/open_text.html",
    "name": "Plain text",
    "accept": {
      "text/plain": [".txt"]
    }
    "launch_type": "single-client"
  }
]
```

Example 4 (unknown):
```unknown
"file_handlers"
```

---

## 跨源嵌入器政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/cross-origin-embedder-policy

**Contents:**
- 跨源嵌入器政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单声明

借助 cross_origin_embedder_policy 清单键，扩展程序可以指定 针对扩展程序的请求的 Cross-Origin-Embedder-Policy (COEP) 响应标头 来源。这包括扩展程序的 Service Worker、弹出式窗口、选项页面、打开某个扩展程序资源的标签页等。

此键与 cross_origin_opener_policy 结合使用，可允许扩展程序 跨域隔离

cross_origin_embedder_policy 清单键包含一个对象，该对象包含一个 名为 value 的属性，该属性接受字符串。Chrome 会将此字符串用作 Cross-Origin-Embedder-Policy 标头。例如：

**Examples:**

Example 1 (unknown):
```unknown
cross_origin_embedder_policy
```

Example 2 (unknown):
```unknown
cross_origin_embedder_policy
```

Example 3 (unknown):
```unknown
Cross-Origin-Embedder-Policy
```

Example 4 (unknown):
```unknown
{
    ...
    "cross_origin_embedder_policy": {
      "value": "require-corp"
    },
    ...
}
```

---

## 使用 Web 推送 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/web-push

**Contents:**
- 使用 Web 推送 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
  - 获取使用 Push API 的权限
  - 推送提供程序和推送服务
  - 自行托管推送提供商
  - 静默推送

在扩展程序中，您可以使用任何推送提供程序发送推送通知和 消息。来自 Push API 的推送将作为 并在收到请求后立即处理如果 Service Worker 已被挂起，则 Push 将 再唤醒它。在扩展程序中使用它的流程与 可以在开放网络中使用

在普通网站上注册推送服务器时，用户会看到一个 授予或拒绝它的权限提示。如果使用扩展程序， 。要在您的扩展程序中使用 Push API，您需要将 manifest.json 中的 notifications 权限

如果您缺少此权限，那么与 registration.pushManager 将导致立即发生错误，结果与 如果用户拒绝了该权限，则会发生此错误。另请注意， notifications 权限将导致权限警告 在安装时显示Chrome 还会停用 现有安装，直到用户批准新权限请求。您可以 请参阅 权限警告指南。

将权限添加到 manifest.json 后，您需要 配置后端与扩展程序之间的连接。此连接 可以分为两部分：推送提供程序和推送服务。答 provider 是您用来向推送服务发送消息的 SDK。 有许多不同的选项，任何推送提供程序都可以用于推送 API（尽管它们可能不会提供可以轻松集成的 SDK）。您 需要对您的提供商的 SDK 进行实验，看看能否实现。推 服务是最终用户设备注册时使用的服务，因此系统可以 发送到推送提供程序发送的任何推送消息。您并不需要 因为它已硬编码到各个浏览器中。对于 Chrome，Firebase Cloud Messaging 是一项推送服务。推送到 Chrome 的任何消息 用户将通过它进行路由

任何推送提供程序都可以运行，但并非所有提供程序都提供有效的 SDK Service Worker 中的资源。如果您遇到问题，需要咨询您的提供商 确保它正常运行不过，您无需使用公共提供商。使用 web-push 等库，您可以托管自己的后端。

您可以使用 web-push-codelab.glitch.me.具体来说，您需要 复制推送服务器的 VAPID 公钥，以便生成推送 订阅。此公钥实际上是 base64 需要解码并转换为 Uint8Array，以便向浏览器的推送功能注册 管理员。有一些库可用于执行此逻辑 只需执行以下操作即可。

subscribe 函数会返回 PushSubscription， 对象，该对象包含推送服务器的元数据。由于您使用的是 web-push-codelab.glitch.me，则需要将此值复制到 页面的“推送订阅”部分

有了 PushSubscription 后，您就可以为 在我们的扩展程序的 Service Worker 中推送消息。

安装好监听器后，您就可以通过 web-push-codelab.glitch.me，然后系统就会将消息记录到 Service Worker 的控制台。

由于它是一种开放式网络标准， 如何实现网络推送，包括在 Chrome 博客上。对于 该示例的完整版本， 扩展程序示例代码库。

您过去可以在 Manifest V3 扩展程序中收到推送通知 从 Chrome 88 中引入 Manifest V3。不过，过去一直有 要求通知显示某种用户可见提示， （如网络通知）。这就会大幅降低 希望将命令或数据更新推送到您的扩展程序，而不费心 提供不必要的信息自 Chrome 121 起，扩展程序 能够将 userVisibleOnly 设为 false。您现在可以发送 不向用户显示的静默推送通知。要使用这项功能 在调用 pushManager.subscribe 时，将 userVisibleOnly 设置为 false。

**Examples:**

Example 1 (unknown):
```unknown
notifications
```

Example 2 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 3 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 4 (unknown):
```unknown
registration.pushManager
```

---

## externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/externally-connectable?hl=zh-cn

**Contents:**
- externally_connectable 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在没有外部连接的情况下连接
- 清单
- 参考

"externally_connectable" 清单属性用于声明哪些扩展程序和网页可以 使用 runtime.connect() 和 runtime.sendMessage() 连接到您的扩展程序。

有关消息传递的教程，请参阅跨扩展程序消息传递和发送消息 来自网页。

如果externally_connectable键没有在扩展程序的清单中声明，则所有扩展程序都可以连接，但是没有网页可以连接。因此，当您更新清单以使用 externally_connectable，如果未指定 "ids": ["*"]，则其他扩展程序 将无法再连接到您的扩展程序这可能是意想不到的后果，因此请及时告知 。

"externally_connectable" 清单键包含以下可选属性：

**Examples:**

Example 1 (unknown):
```unknown
"externally_connectable"
```

Example 2 (unknown):
```unknown
runtime.connect()
```

Example 3 (unknown):
```unknown
runtime.sendMessage()
```

Example 4 (unknown):
```unknown
externally_connectable
```

---

## chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/action?hl=zh-cn

**Contents:**
- chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 清单
- 概念和用法
  - 界面组成部分
    - 图标
    - 提示（标题）
    - 徽章
    - 弹出式窗口

使用 chrome.action API 控制 Google Chrome 工具栏中的扩展程序图标。

如需使用此 API，必须在清单中声明以下键。

如需使用 chrome.action API，请指定 "manifest_version" 为 3，并在清单文件中添加 "action" 密钥。

"action" 键（及其子键）是可选的。如果未包含此元素，扩展程序仍会显示在工具栏中，以便用户访问扩展程序的菜单。因此，我们建议您始终至少包含 "action" 和 "default_icon" 键。

该图标是扩展程序工具栏上的主要图片，由清单的 "action" 键中的 "default_icon" 键设置。图标的宽度和高度必须为 16 个与设备无关的像素 (DIP)。

"default_icon" 键是一个包含大小到图片路径的字典。Chrome 会使用这些图标来选择要使用的图片缩放比例。如果找不到完全匹配的图片，Chrome 会选择最接近的可用图片并将其缩放为适合的尺寸，这可能会影响图片质量。

由于具有 1.5 倍或 1.2 倍等不太常见缩放比例的设备越来越普遍，我们建议您为图标提供多种尺寸。这还可以确保您的扩展程序在未来能够应对潜在的图标显示大小变化。不过，如果只提供一种尺寸，也可以将 "default_icon" 键设置为指向单个图标路径的字符串，而不是字典。

您还可以通过指定其他图片路径或使用 HTML canvas 元素（如果从扩展程序服务工作线程进行设置，则使用 offscreen canvas API）提供动态生成的图标，以通过编程方式调用 action.setIcon() 来设置扩展程序的图标。

对于打包的扩展程序（从 .crx 文件安装），图片可以采用 Blink 渲染引擎可以显示的大多数格式，包括 PNG、JPEG、BMP、ICO 等。不支持 SVG。 未打包的扩展程序必须使用 PNG 图片。

当用户将鼠标指针悬停在工具栏中的扩展程序图标上时，系统会显示提示或标题。当按钮获得焦点时，屏幕阅读器朗读的无障碍文本中也会包含该文本。

默认提示是通过 manifest.json 中 "action" 键的 "default_title" 字段设置的。您还可以通过调用 action.setTitle() 以编程方式进行设置。

操作可以选择性地显示“徽章”，即叠加在图标上的一小段文字。这样，您就可以更新操作，以显示有关扩展程序状态的少量信息，例如计数器。徽章包含文本组件和背景颜色。由于空间有限，我们建议徽章文字不超过 4 个字符。

如需创建徽章，请通过调用 action.setBadgeBackgroundColor() 和 action.setBadgeText() 以编程方式进行设置。清单中没有默认的徽章设置。徽章颜色值可以是介于 0 到 255 之间的四个整数组成的数组，用于构成徽章的 RGBA 颜色，也可以是具有 CSS 颜色值的字符串。

当用户点击工具栏中的扩展程序操作按钮时，系统会显示相应操作的弹出式窗口。弹出式窗口可以包含您喜欢的任何 HTML 内容，并且会自动调整大小以适应其内容。弹出式窗口的尺寸必须介于 25x25 像素和 800x600 像素之间。

弹出式窗口最初由 manifest.json 文件中 "action" 键内的 "default_popup" 属性设置。如果存在，此属性应指向扩展程序目录中的相对路径。您还可以使用 action.setPopup() 方法动态更新该属性，使其指向其他相对路径。

扩展操作在每个标签页中可以处于不同的状态。如需为各个标签页设置值，请使用 action API 设置方法中的 tabId 属性。例如，如需为特定标签页设置徽章文字，请执行类似以下操作：

如果省略 tabId 属性，则该设置会被视为全局设置。标签页专用设置优先于全局设置。

默认情况下，工具栏操作在每个标签页上均处于启用状态（可点击）。您可以在清单的 action 键中设置 default_state 属性，以更改此默认设置。如果 default_state 设置为 "disabled"，则该操作默认处于停用状态，必须以编程方式启用才能点击。如果 default_state 设置为 "enabled"（默认值），则默认情况下操作处于启用状态且可点击。

您可以使用 action.enable() 和 action.disable() 方法以编程方式控制状态。这只会影响是否向扩展程序发送弹出式窗口（如果有）或 action.onClicked 事件；不会影响工具栏中操作的存在。

以下示例展示了在扩展程序中使用操作的一些常见方式。如需试用此 API，请从 chrome-extension-samples 代码库安装 Action API 示例。

扩展程序通常会在用户点击扩展程序的操作时显示弹出式窗口。如需在您自己的扩展程序中实现此功能，请在 manifest.json 中声明弹出式窗口，并指定 Chrome 应在弹出式窗口中显示的内容。

扩展程序的常见模式是使用扩展程序的操作公开其主要功能。以下示例演示了此模式。当用户点击操作时，扩展程序会将内容脚本注入到当前网页中。然后，内容脚本会显示一个提醒，以验证一切是否按预期运行。

此示例展示了扩展程序的后台逻辑如何 (a) 默认停用某项操作，以及 (b) 使用 declarativeContent 在特定网站上启用该操作。

要在其中打开操作弹出式窗口的窗口的 ID。如果未指定，则默认为当前活跃窗口。

要查询状态的标签页的 ID。如果未指定任何标签页，则返回非标签页专用状态。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

为标签页启用操作。默认情况下，操作处于启用状态。

Promise<extensionTypes.ColorArray>

获取操作的徽章文本。如果未指定任何标签页，则返回非标签页特定的徽章文字。如果启用了 displayActionCountAsBadgeText，则除非存在 declarativeNetRequestFeedback 权限或提供了标签页专用徽章文本，否则系统会返回占位文本。

Promise<extensionTypes.ColorArray>

获取设置为相应操作的弹出式窗口的 HTML 文档。

Promise<UserSettings>

指示扩展程序操作是否已针对某个标签页启用（如果未提供 tabId，则表示已全局启用）。仅使用 declarativeContent 启用的操作始终返回 false。

打开扩展程序的弹出式窗口。在 Chrome 118 和 Chrome 126 之间，此功能仅适用于根据政策安装的扩展程序。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

可以传递任意数量的字符，但空间中只能容纳大约 4 个字符。如果传递的是空字符串 ('')，则会清除标记文本。如果指定了 tabId，但 text 为 null，则指定标签页的文字会被清除，并默认设为全局徽章文字。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。如果不设置此值，系统会自动选择与徽章背景颜色形成对比的颜色，以便显示文字。如果颜色的 Alpha 值相当于 0，则不会设置该颜色，并且会返回错误。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

为操作设置图标。图标可以指定为图片文件的路径、画布元素的像素数据，也可以指定为包含其中任一信息的字典。必须指定 path 或 imageData 属性。

要设置的图标，可以是 ImageData 对象，也可以是表示图标的字典 {size -> ImageData}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.imageData = foo”等同于“details.imageData = {'16': foo}”

相对图片路径或指向要设置的图标的字典 {size -> relative image path}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.path = foo”等同于“details.path = {'16': foo}”

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

设置 HTML 文档，以便在用户点击操作的图标时将其作为弹出式窗口打开。

要在弹出式窗口中显示的 HTML 文件的相对路径。如果设置为空字符串 ('')，则不显示任何弹出式窗口。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

在用户点击操作图标时触发。如果操作具有弹出式窗口，则不会触发此事件。

在与扩展程序操作相关的用户指定设置发生更改时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.action
```

Example 2 (unknown):
```unknown
chrome.action
```

Example 3 (unknown):
```unknown
"manifest_version"
```

Example 4 (unknown):
```unknown
{
  "name": "Action Extension",
  ...
  "action": {
    "default_icon": {              // optional
      "16": "images/icon16.png",   // optional
      "24": "images/icon24.png",   // optional
      "32": "images/icon32.png"    // optional
    },
    "default_title": "Click Me",   // optional, shown in tooltip
    "default_popup": "popup.html"  // optional
  },
  ...
}
```

---

## 清单 - 内容安全政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/content-security-policy

**Contents:**
- 清单 - 内容安全政策 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 默认政策
- 最低和自定义内容安全政策
  - “扩展程序页面”政策
  - 沙盒页面政策

可选的清单键，包含网络平台内容安全政策，用于指定对扩展程序可以使用的脚本、样式和其他资源的限制。在此清单键中，您可以为扩展程序页面和沙盒化扩展程序页面分别定义可选政策。

“扩展程序页面”政策会应用于扩展程序中的网页上下文和工作器上下文。这包括扩展程序弹出式窗口、后台工作器，以及扩展程序打开的包含 HTML 网页或 iframe 的标签页。沙盒政策适用于在清单中指定为沙盒页面的所有网页。

如果用户未在清单中定义内容安全政策，则扩展程序页面和沙盒化扩展程序页面将使用默认属性。

在这种情况下，该扩展程序将仅从自己的打包资源加载本地脚本和对象。WebAssembly 将被停用，该扩展程序将无法运行内嵌 JavaScript，也无法将字符串评估为可执行代码。如果添加了沙盒页面，它将拥有更宽松的权限，可以更宽松地评估扩展程序外部的脚本。

开发者可以根据其项目需求为其扩展程序添加或移除规则，或使用最低的内容安全政策。

Chrome 会对扩展程序页面强制执行最低内容安全政策。这相当于在清单中指定以下政策：

extension_pages 政策不能超过此最小值。换言之，您不能向指令添加其他脚本源，例如将 'unsafe-eval' 添加到 script-src。如果您向扩展程序的政策中添加了禁止的来源，Chrome 会在安装时抛出如下错误：

沙盒页面的默认政策比扩展程序页面要宽松得多，因为沙盒页面无法访问扩展程序 API，也无法直接访问未经过沙盒化的网页。您可以根据需要自定义沙盒内容安全政策。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self';",
    "sandbox": "sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';"
  }
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self';",
    "sandbox": "sandbox allow-scripts allow-forms allow-popups allow-modals; script-src 'self' 'unsafe-inline' 'unsafe-eval'; child-src 'self';"
  }
  // ...
}
```

Example 3 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

Example 4 (unknown):
```unknown
{
  // ...
  "content_security_policy": {
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

---

## 清单 - 首页网址 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/homepage-url

**Contents:**
- 清单 - 首页网址 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

可选的清单键，包含有效首页网址的字符串。开发者可以选择将扩展程序的首页设为其个人或公司的网站。如果未定义此参数，则默认主页将是扩展程序管理页面 (chrome://extensions) 上所列出的扩展程序的 Chrome 应用商店页面。如果您在自己的网站上托管该扩展程序，此字段会特别有用。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "homepage_url": "https://example.com,",
  // ...
}
```
```

Example 2 (unknown):
```unknown
{
  // ...
  "homepage_url": "https://example.com,",
  // ...
}
```
```

---

## 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/minimum_chrome_version?hl=zh-cn

**Contents:**
- 清单 - Chrome 最低版本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 强制执行
  - 新安装次数
  - 现有安装

可选的清单键，包含一个字符串，该字符串定义了 Chrome 可以安装该扩展程序。为此字符串设置的值必须是现有 Chrome 浏览器版本字符串的子字符串。使用完整版 数字可指定 Chrome 的特定更新，也可使用 字符串以指定特定的主要版本。

在低于最低版本的 Chrome 版本中，Chrome 应用商店会显示“不兼容”消息，而不是安装按钮。这些用户 版本将无法安装您的扩展程序。

您的扩展程序的现有用户 minimum_chrome_version版本高于目前的浏览器版本。此操作会以静默方式进行，因此您应谨慎行事，并考虑如何让现有用户知道他们不再收到更新。

**Examples:**

Example 1 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 2 (unknown):
```unknown
{
  // ...
  "minimum_chrome_version": "126",
  // ...
}
```

Example 3 (unknown):
```unknown
minimum_chrome_version
```

Example 4 (unknown):
```unknown
minimum_chrome_version
```

---

## 覆盖 Chrome 设置 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/chrome-settings-override

**Contents:**
- 覆盖 Chrome 设置 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 首页、搜索服务提供商和启动页
- 自定义值
- 参考

设置覆盖是扩展程序覆盖所选 Chrome 设置的一种方式。API 是 。

下面的示例展示了如何修改首页、搜索服务提供商和启动页 在扩展程序清单中。Settings API 中使用的任何网域都必须经过验证（通过 Google Search Console）。请注意，如果 验证对某个网域（例如 https://example.com）的所有权 可以使用任何子网域或网页 （例如 https://app.example.com 或 https://example.com/page.html）。

如果使用设置覆盖权限来请求获取任何其他功能或权限，这不符合我们的单一用途政策。当 Chrome 检测到某项内容可能违反了我们的单一用途政策时，会向用户显示确认对话框。只修改某项设置而不寻求其他功能或权限的扩展程序不会显示确认对话框。

这适用于 Chrome 107 及更高版本。

对于外部扩展程序，search_provider、homepage 和 startup_pages 网址值可以 并使用注册表项参数化。在 "update_url" 键（请参阅此处的说明）。键名为 "install_parameter"，值为 是任意字符串：

清单网址中出现的子字符串 "__PARAM__" 都将替换为 "install_parameter" 值。如果 "install_parameter" 不存在，则 "__PARAM__" 的出现次数为 已移除。请注意，"__PARAM__" 不能是主机名的一部分。它必须在 第一个“/”。

扩展程序可以替换清单中的以下一个或多个属性：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "chrome_settings_overrides": {
    "homepage": "https://www.homepage.com",
    "search_provider": {
        "name": "name.__MSG_url_domain__",
        "keyword": "keyword.__MSG_url_domain__",
        "search_url": "https://www.foo.__MSG_url_domain__/s?q={searchTerms}",
        "favicon_url": "https://www.foo.__MSG_url_domain__/favicon.ico",
        "suggest_url": "https://www.foo.__MSG_url_domain__/suggest?q={searchTerms}",
        "instant_url": "https://www.foo.__MSG_url_domain__/instant?q={searchTerms}",
        "image_url": "https://www.foo.__MSG_url_domain__/image?q={searchTerms}",
        "search_url_post_params": "search_lang=__MSG_url_domain__",
        "suggest_url_post_params": "suggest_lang=__MSG_url_domain__",
        "instant_url_post_params": "instant_lang=__MSG_url_domain__",
        "image_url_post_params": "image_lang=__MSG_url_domain__",
        "alternate_urls": [
          "https://www.moo.__MSG_url_domain__/s?q={searchTerms}",
          "https://www.noo.__MSG_url_domain__/s?q={searchTerms}"
        ],
        "encoding": "UTF-8",
        "is_default": true
    },
    "startup_pages": ["https://www.startup.com"]
   },
   "default_locale": "de",
   ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "chrome_settings_overrides": {
    "homepage": "https://www.homepage.com",
    "search_provider": {
        "name": "name.__MSG_url_domain__",
        "keyword": "keyword.__MSG_url_domain__",
        "search_url": "https://www.foo.__MSG_url_domain__/s?q={searchTerms}",
        "favicon_url": "https://www.foo.__MSG_url_domain__/favicon.ico",
        "suggest_url": "https://www.foo.__MSG_url_domain__/suggest?q={searchTerms}",
        "instant_url": "https://www.foo.__MSG_url_domain__/instant?q={searchTerms}",
        "image_url": "https://www.foo.__MSG_url_domain__/image?q={searchTerms}",
        "search_url_post_params": "search_lang=__MSG_url_domain__",
        "suggest_url_post_params": "suggest_lang=__MSG_url_domain__",
        "instant_url_post_params": "instant_lang=__MSG_url_domain__",
        "image_url_post_params": "image_lang=__MSG_url_domain__",
        "alternate_urls": [
          "https://www.moo.__MSG_url_domain__/s?q={searchTerms}",
          "https://www.noo.__MSG_url_domain__/s?q={searchTerms}"
        ],
        "encoding": "UTF-8",
        "is_default": true
    },
    "startup_pages": ["https://www.startup.com"]
   },
   "default_locale": "de",
   ...
}
```

Example 3 (unknown):
```unknown
search_provider
```

Example 4 (unknown):
```unknown
startup_pages
```

---

## chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/action

**Contents:**
- chrome.action 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 清单
- 概念和用法
  - 界面组成部分
    - 图标
    - 提示（标题）
    - 徽章
    - 弹出式窗口

使用 chrome.action API 控制 Google Chrome 工具栏中的扩展程序图标。

如需使用此 API，必须在清单中声明以下键。

如需使用 chrome.action API，请指定 "manifest_version" 为 3，并在清单文件中添加 "action" 密钥。

"action" 键（及其子键）是可选的。如果未包含此元素，扩展程序仍会显示在工具栏中，以便用户访问扩展程序的菜单。因此，我们建议您始终至少包含 "action" 和 "default_icon" 键。

该图标是扩展程序工具栏上的主要图片，由清单的 "action" 键中的 "default_icon" 键设置。图标的宽度和高度必须为 16 个与设备无关的像素 (DIP)。

"default_icon" 键是一个包含大小到图片路径的字典。Chrome 会使用这些图标来选择要使用的图片缩放比例。如果找不到完全匹配的图片，Chrome 会选择最接近的可用图片并将其缩放为适合的尺寸，这可能会影响图片质量。

由于具有 1.5 倍或 1.2 倍等不太常见缩放比例的设备越来越普遍，我们建议您为图标提供多种尺寸。这还可以确保您的扩展程序在未来能够应对潜在的图标显示大小变化。不过，如果只提供一种尺寸，也可以将 "default_icon" 键设置为指向单个图标路径的字符串，而不是字典。

您还可以通过指定其他图片路径或使用 HTML canvas 元素（如果从扩展程序服务工作线程进行设置，则使用 offscreen canvas API）提供动态生成的图标，以通过编程方式调用 action.setIcon() 来设置扩展程序的图标。

对于打包的扩展程序（从 .crx 文件安装），图片可以采用 Blink 渲染引擎可以显示的大多数格式，包括 PNG、JPEG、BMP、ICO 等。不支持 SVG。 未打包的扩展程序必须使用 PNG 图片。

当用户将鼠标指针悬停在工具栏中的扩展程序图标上时，系统会显示提示或标题。当按钮获得焦点时，屏幕阅读器朗读的无障碍文本中也会包含该文本。

默认提示是通过 manifest.json 中 "action" 键的 "default_title" 字段设置的。您还可以通过调用 action.setTitle() 以编程方式进行设置。

操作可以选择性地显示“徽章”，即叠加在图标上的一小段文字。这样，您就可以更新操作，以显示有关扩展程序状态的少量信息，例如计数器。徽章包含文本组件和背景颜色。由于空间有限，我们建议徽章文字不超过 4 个字符。

如需创建徽章，请通过调用 action.setBadgeBackgroundColor() 和 action.setBadgeText() 以编程方式进行设置。清单中没有默认的徽章设置。徽章颜色值可以是介于 0 到 255 之间的四个整数组成的数组，用于构成徽章的 RGBA 颜色，也可以是具有 CSS 颜色值的字符串。

当用户点击工具栏中的扩展程序操作按钮时，系统会显示相应操作的弹出式窗口。弹出式窗口可以包含您喜欢的任何 HTML 内容，并且会自动调整大小以适应其内容。弹出式窗口的尺寸必须介于 25x25 像素和 800x600 像素之间。

弹出式窗口最初由 manifest.json 文件中 "action" 键内的 "default_popup" 属性设置。如果存在，此属性应指向扩展程序目录中的相对路径。您还可以使用 action.setPopup() 方法动态更新该属性，使其指向其他相对路径。

扩展操作在每个标签页中可以处于不同的状态。如需为各个标签页设置值，请使用 action API 设置方法中的 tabId 属性。例如，如需为特定标签页设置徽章文字，请执行类似以下操作：

如果省略 tabId 属性，则该设置会被视为全局设置。标签页专用设置优先于全局设置。

默认情况下，工具栏操作在每个标签页上均处于启用状态（可点击）。您可以在清单的 action 键中设置 default_state 属性，以更改此默认设置。如果 default_state 设置为 "disabled"，则该操作默认处于停用状态，必须以编程方式启用才能点击。如果 default_state 设置为 "enabled"（默认值），则默认情况下操作处于启用状态且可点击。

您可以使用 action.enable() 和 action.disable() 方法以编程方式控制状态。这只会影响是否向扩展程序发送弹出式窗口（如果有）或 action.onClicked 事件；不会影响工具栏中操作的存在。

以下示例展示了在扩展程序中使用操作的一些常见方式。如需试用此 API，请从 chrome-extension-samples 代码库安装 Action API 示例。

扩展程序通常会在用户点击扩展程序的操作时显示弹出式窗口。如需在您自己的扩展程序中实现此功能，请在 manifest.json 中声明弹出式窗口，并指定 Chrome 应在弹出式窗口中显示的内容。

扩展程序的常见模式是使用扩展程序的操作公开其主要功能。以下示例演示了此模式。当用户点击操作时，扩展程序会将内容脚本注入到当前网页中。然后，内容脚本会显示一个提醒，以验证一切是否按预期运行。

此示例展示了扩展程序的后台逻辑如何 (a) 默认停用某项操作，以及 (b) 使用 declarativeContent 在特定网站上启用该操作。

要在其中打开操作弹出式窗口的窗口的 ID。如果未指定，则默认为当前活跃窗口。

要查询状态的标签页的 ID。如果未指定任何标签页，则返回非标签页专用状态。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

扩展程序的 action 图标是否显示在浏览器窗口的顶级工具栏上（即，用户是否已“固定”该扩展程序）。

为标签页启用操作。默认情况下，操作处于启用状态。

Promise<extensionTypes.ColorArray>

获取操作的徽章文本。如果未指定任何标签页，则返回非标签页特定的徽章文字。如果启用了 displayActionCountAsBadgeText，则除非存在 declarativeNetRequestFeedback 权限或提供了标签页专用徽章文本，否则系统会返回占位文本。

Promise<extensionTypes.ColorArray>

获取设置为相应操作的弹出式窗口的 HTML 文档。

Promise<UserSettings>

指示扩展程序操作是否已针对某个标签页启用（如果未提供 tabId，则表示已全局启用）。仅使用 declarativeContent 启用的操作始终返回 false。

打开扩展程序的弹出式窗口。在 Chrome 118 和 Chrome 126 之间，此功能仅适用于根据政策安装的扩展程序。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

可以传递任意数量的字符，但空间中只能容纳大约 4 个字符。如果传递的是空字符串 ('')，则会清除标记文本。如果指定了 tabId，但 text 为 null，则指定标签页的文字会被清除，并默认设为全局徽章文字。

一个包含四个整数的数组，这些整数的范围为 [0,255]，用于构成徽章的 RGBA 颜色。例如，不透明的红色为 [255, 0, 0, 255]。也可以是具有 CSS 值的字符串，其中不透明的红色为 #FF0000 或 #F00。如果不设置此值，系统会自动选择与徽章背景颜色形成对比的颜色，以便显示文字。如果颜色的 Alpha 值相当于 0，则不会设置该颜色，并且会返回错误。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

为操作设置图标。图标可以指定为图片文件的路径、画布元素的像素数据，也可以指定为包含其中任一信息的字典。必须指定 path 或 imageData 属性。

要设置的图标，可以是 ImageData 对象，也可以是表示图标的字典 {size -> ImageData}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.imageData = foo”等同于“details.imageData = {'16': foo}”

相对图片路径或指向要设置的图标的字典 {size -> relative image path}。如果图标指定为字典，则会根据屏幕的像素密度选择要使用的实际图片。如果一个屏幕空间单位可容纳的图片像素数为 scale，则系统会选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.path = foo”等同于“details.path = {'16': foo}”

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

设置 HTML 文档，以便在用户点击操作的图标时将其作为弹出式窗口打开。

要在弹出式窗口中显示的 HTML 文件的相对路径。如果设置为空字符串 ('')，则不显示任何弹出式窗口。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

在用户点击操作图标时触发。如果操作具有弹出式窗口，则不会触发此事件。

在与扩展程序操作相关的用户指定设置发生更改时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.action
```

Example 2 (unknown):
```unknown
chrome.action
```

Example 3 (unknown):
```unknown
"manifest_version"
```

Example 4 (unknown):
```unknown
{
  "name": "Action Extension",
  ...
  "action": {
    "default_icon": {              // optional
      "16": "images/icon16.png",   // optional
      "24": "images/icon24.png",   // optional
      "32": "images/icon32.png"    // optional
    },
    "default_title": "Click Me",   // optional, shown in tooltip
    "default_popup": "popup.html"  // optional
  },
  ...
}
```

---

## 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/key?hl=zh-cn

**Contents:**
- 清单 - 键 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保持一致的扩展程序 ID
  - 将扩展程序上传到开发者信息中心
  - 比较 ID

此值用于在开发期间加载扩展程序或主题时维护其唯一 ID。以下是一些常见使用场景：

在开发过程中，保留单个 ID 至关重要。如需保持一致的 ID，请按以下步骤操作：

将扩展程序目录打包到 .zip 文件中，并将其上传到 Chrome 开发者信息中心，但不要发布：

将代码添加到 "key" 字段下的 manifest.json。这样，扩展程序将使用相同的 ID。

打开 chrome://extensions 中的“扩展程序管理”页面，确保已启用开发者模式，然后上传未打包的扩展程序目录。将扩展程序管理页面上的扩展程序 ID 与开发者信息中心内的商品 ID 进行比较。它们应保持一致。

**Examples:**

Example 1 (unknown):
```unknown
web_accessible_resources
```

Example 2 (unknown):
```unknown
-----BEGIN PUBLIC KEY-----
```

Example 3 (unknown):
```unknown
-----END PUBLIC KEY-----
```

Example 4 (unknown):
```unknown
manifest.json
```

---
