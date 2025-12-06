# Chrome-Extensions - Manifest

**Pages:** 137

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

Example 1 (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

chrome.tabs.executeScript(
  tab.id,
  {
    file: 'content-script.js'
  }
);
```

Example 2 (javascript):
```javascript
async function getCurrentTab()
let tab = await getCurrentTab();

chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['content-script.js']
});
```

Example 3 (javascript):
```javascript
chrome.tabs.insertCSS(tabId, injectDetails, () => {
  // callback code
});
```

Example 4 (javascript):
```javascript
const insertPromise = await chrome.scripting.insertCSS({
  files: ["style.css"],
  target: { tabId: tab.id }
});
// Remaining code.
```

---

## 替换屏蔽型 Web 请求监听器 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/blocking-web-requests

**Contents:**
- 替换屏蔽型 Web 请求监听器 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 简介
- 更新权限
- 创建声明式网络请求规则
- 常见使用场景
  - 屏蔽单个网址
  - 重定向多个网址
  - 屏蔽 Cookie

Manifest V3 更改了扩展程序处理网络请求修改的方式。扩展程序不是使用 chrome.webRequest 在运行时拦截网络请求并对其进行更改，而是指定规则来描述在满足给定的一组条件时要执行的操作。使用声明式网络请求 API 执行此操作。

Web 请求 API 和声明式 Net 请求 API 存在显著差异。您需要根据使用情形重写代码，而不是将一个函数调用替换为另一个函数调用。本部分将引导您完成该过程。

如果您的扩展程序是通过政策安装的，则无需进行这些更改。对于通过政策安装的扩展程序，Manifest V3 中仍提供 webRequestBlocking 权限。

这是三个部分中的第二部分，介绍了非扩展服务工作线程的代码所需的更改。本文介绍了如何将 Manifest V2 使用的阻塞式网络请求转换为 Manifest V3 使用的声明式网络请求。其他两个部分介绍了迁移到 Manifest V3 所需的代码更新以及提高安全性。

在清单 V2 中，屏蔽 Web 请求可能会严重降低扩展程序的性能以及它们所处理的网页的性能。webRequest 命名空间支持 9 个可能会阻塞的事件，每个事件都可接受无限数量的事件处理程序。更糟糕的是，每个网页都可能被多个扩展程序屏蔽，而实现此目的所需的权限具有侵入性。Manifest V3 通过将回调替换为声明性规则来防范此问题。

对 manifest.json 中的 "permissions" 字段进行以下更改。

您需要根据自己的使用场景添加其他权限。这些权限及其支持的用例如下所述。

创建声明式网络请求规则需要在 manifest.json 中添加 "declarative_net_request" 对象。"declarative_net_request" 块包含指向规则文件的 "rule_resource" 对象数组。规则文件包含一个对象数组，用于指定操作以及调用这些操作的条件。

以下部分介绍了声明性网络请求的常见用例。以下说明仅提供简要概述。如需详细了解此处的全部信息，请参阅 API 参考文档中的 chrome.declarativeNetRequest

在清单 V2 中，一种常见的用例是在后台脚本中使用 onBeforeRequest 事件来阻止 Web 请求。

对于清单 V3，请使用 "block" 操作类型创建新的 declarativeNetRequest 规则。请注意示例规则中的 "condition" 对象。其 "urlFilter" 会替换传递给 webRequest 监听器的 urls 选项。"resourceTypes" 数组用于指定要屏蔽的资源类别。此示例仅屏蔽主 HTML 网页，但您也可以仅屏蔽字体。

为了使此功能正常运行，您需要更新扩展程序的权限。在 manifest.json 中，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。请注意，网址已从 "permissions" 字段中移除，因为屏蔽内容不需要主机权限。如上所示，规则文件指定了声明性网络请求所应用的主机。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

在清单 V2 中，另一个常见用例是使用 BeforeRequest 事件来重定向 Web 请求。

对于 Manifest V3，请使用 "redirect" 操作类型。与之前一样，"urlFilter" 会替换传递给 webRequest 监听器的 url 选项。请注意，在此示例中，规则文件的 "action" 对象包含一个 "redirect" 字段，其中包含要返回的网址，而不是要过滤的网址。

此方案还需要更改扩展程序的权限。与之前一样，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。网址再次从 manifest.json 移至规则文件。请注意，除了主机权限之外，重定向还需要 "declarativeNetRequestWithHostAccess" 权限。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

在 Manifest V2 中，屏蔽 Cookie 需要在发送网页请求标头之前拦截它们，并移除特定标头。

Manifest V3 也会通过规则文件中的规则执行此操作。这次操作类型为 "modifyHeaders"。该文件采用 "requestHeaders" 对象数组，用于指定要修改的标头以及修改方式。请注意，"condition" 对象仅包含一个 "resourceTypes" 数组。它支持与之前示例相同的值。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

此方案还需要更改扩展程序的权限。与之前一样，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。

**Examples:**

Example 1 (javascript):
```javascript
chrome.webRequest.onBeforeRequest.addListener((e) => {
    return { cancel: true };
}, { urls: ["https://www.example.com/*"] }, ["blocking"]);
```

Example 2 (unknown):
```unknown
[
  {
    "id" : 1,
    "priority": 1,
    "action" : { "type" : "block" },
    "condition" : {
      "urlFilter" : "||example.com",
      "resourceTypes" : ["main_frame"]
    }
  }
]
```

Example 3 (unknown):
```unknown
"permissions": [
    "webRequestBlocking",
    "https://*.example.com/*"
  ]
```

Example 4 (unknown):
```unknown
"permissions": [
    "declarativeNetRequest",
  ]
```

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/declare-permissions

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Permissions Extension",
  ...
  "permissions": [
    "activeTab",
    "contextMenus",
    "storage"
  ],
  "optional_permissions": [
    "topSites",
  ],
  "host_permissions": [
    "https://www.developer.chrome.com/*"
  ],
  "optional_host_permissions":[
    "https://*/*",
    "http://*/*"
  ],
  ...
  "manifest_version": 3
}
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
{ // manifest.json
  "manifest_version": 3,
...
  "key": "ThisKeyIsGoingToBeVeryLong/go8GGC2u3UD9WI3MkmBgyiDPP2OreImEQhPvwpliioUMJmERZK3zPAx72z8MDvGp7Fx7ZlzuZpL4yyp4zXBI+MUhFGoqEh32oYnm4qkS4JpjWva5Ktn4YpAWxd4pSCVs8I4MZms20+yx5OlnlmWQEwQiiIwPPwG1e1jRw0Ak5duPpE3uysVGZXkGhC5FyOFM+oVXwc1kMqrrKnQiMJ3lgh59LjkX4z1cDNX3MomyUMJ+I+DaWC2VdHggB74BNANSd+zkPQeNKg3o7FetlDJya1bk8ofdNBARxHFMBtMXu/ONfCT3Q2kCY9gZDRktmNRiHG/1cXhkIcN1RWrbsCkwIDAQAB",
}
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

---

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/permissions

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 2 (javascript):
```javascript
document.querySelector('#my-button').addEventListener('click', (event) => {
  // Permissions must be requested from inside a user gesture, like a button's
  // click handler.
  chrome.permissions.request({
    permissions: ['tabs'],
    origins: ['https://www.google.com/']
  }, (granted) => {
    // The callback argument will be true if the user granted the permissions.
    if (granted) {
      doSomething();
    } else {
      doSomethingElse();
    }
  });
});
```

Example 3 (javascript):
```javascript
chrome.permissions.contains({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (result) => {
  if (result) {
    // The extension has the permissions.
  } else {
    // The extension doesn't have the permissions.
  }
});
```

Example 4 (javascript):
```javascript
chrome.permissions.remove({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (removed) => {
  if (removed) {
    // The permissions have been removed.
  } else {
    // The permissions have not been removed (e.g., you tried to remove
    // required permissions).
  }
});
```

---

## 正在获取网站图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/favicons

**Contents:**
- 正在获取网站图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 访问网站的图标
  - 第 1 步：更新清单
  - 第 2 步：构建网址
- 扩展程序示例

网站图标（简称“收藏夹图标”）是显示在浏览器地址栏中的一个小图标。favicon 通常用于识别和区分网站。本文介绍了如何在 Manifest V3 扩展程序中检索网站的网站图标。

如需检索网站的 Favicon，您需要构建以下网址：

以下步骤介绍了如何在 Chrome 扩展程序中构建此网址：

首先，您必须在清单中请求 "favicon" 权限。

此外，在内容脚本中提取网站图标时，必须将 "_favicon/*" 文件夹声明为网页访问资源。例如：

以下函数使用 runtime.getURL() 创建指向 "_favicon/" 文件夹的完全限定网址。然后，它会返回一个新字符串，表示包含多个查询参数的网址。最后，该扩展程序会将图片附加到正文。

以下示例是一个包含随机扩展程序 ID 的 www.google.com 32 像素的 Favicon 网址：

chrome-extension-samples 代码库中有两个网站图标示例：

**Examples:**

Example 1 (unknown):
```unknown
chrome-extension://EXTENSION_ID/_favicon/?pageUrl=EXAMPLE_URL&size=FAV_SIZE
```

Example 2 (unknown):
```unknown
{
  "name": "Favicon API in a popup",
  "manifest_version": 3,
  ...
  "permissions": ["favicon"],
  ...
}
```

Example 3 (unknown):
```unknown
{
  "name": "Favicon API in content scripts",
  "manifest_version": 3,
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "permissions": ["favicon"],
  "web_accessible_resources": [
    {
      "resources": ["_favicon/*"],
      "matches": ["<all_urls>"],
      "extension_ids": ["*"]
    }
  ]
  ...
}
```

Example 4 (javascript):
```javascript
function faviconURL(u) {
  const url = new URL(chrome.runtime.getURL("/_favicon/"));
  url.searchParams.set("pageUrl", u);
  url.searchParams.set("size", "32");
  return url.toString();
}

const img = document.createElement('img');
img.src = faviconURL("https://www.google.com") 
document.body.appendChild(img);
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
{
  ...
  "manifest_version": 2
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "manifest_version": 3
  ...
}
```

Example 3 (unknown):
```unknown
{
  ...
  "permissions": [
    "tabs",
    "bookmarks",
    "https://www.blogger.com/"
  ],
  "optional_permissions": [
    "unlimitedStorage",
    "*://*/*"
  ]
  ...
}
```

Example 4 (unknown):
```unknown
{
  ...
  "permissions": [
    "tabs",
    "bookmarks"
  ],
  "optional_permissions": [
    "unlimitedStorage"
  ],
  "host_permissions": [
    "https://www.blogger.com/"
  ],
  "optional_host_permissions": [
    "*://*/*"
  ]
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
{
  ...
  "background": {
    "scripts": [
      "backgroundContextMenus.js",
      "backgroundOauth.js"
    ],
    "persistent": false
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "background": {
    "service_worker": "service_worker.js",
    "type": "module"
  }
  ...
}
```

Example 3 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: chrome.runtime.getURL('offscreen.html'),
  reasons: ['CLIPBOARD'],
  justification: 'testing the offscreen API',
});
```

Example 4 (javascript):
```javascript
let textEl = document.querySelector('#text');
textEl.value = data;
textEl.select();
document.execCommand('copy');
```

---

## 权限警告准则 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/permission_warnings?hl=zh-cn

**Contents:**
- 权限警告准则 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 最佳实践
- 查看警告
  - 使用扩展程序更新测试工具
  - 通过手动打包扩展程序
- 更新权限
  - 使用扩展程序更新测试工具进行更新
  - 手动更新扩展程序

Chrome 扩展程序可提升用户的浏览器体验。为此，请使用需要特定权限的 Chrome API。有些权限侵扰性较低，并且不会显示警告。其他权限会触发用户必须授予的警告。本页面提供了有关如何处理权限警告的指南。权限中注明了具体警告适用的权限。

添加会触发警告的新权限后，扩展程序将被停用，直到用户接受新权限。如需了解如何测试此行为，请参阅更新权限。

某些权限在与其他权限配对时可能不会显示警告。例如，如果扩展程序也请求 "<all_urls>"，则系统不会显示 "tabs" 警告。

权限警告描述了 API 授予的功能，但有些警告比其他警告更难理解。用户更有可能安装遵循以下准则的扩展程序：

如要查看扩展程序的权限警告，您有以下两种选择：

Chrome 将创建两个文件：.crx 文件和 .pem 文件。.pem 文件包含用于为扩展程序签名的私钥。请务必记住这些文件保存的目录。

请将 .pem 文件保存在安全可靠的位置；更新扩展程序时需要使用此文件。

将 .crx 文件拖放到该扩展程序的“管理”页面即可安装。

丢弃 .crx 文件后，浏览器会询问是否可以添加该扩展程序并显示警告。

当扩展程序添加一项会触发警告的新权限时，可能会暂时停用该权限。只有在用户同意接受新权限后，该扩展程序才会重新启用。

若要检查扩展程序在添加新权限时是否会被停用，有以下选项可供选择：

以下步骤假定您按照使用扩展程序更新测试工具中的说明启动了服务器。

---

## 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/content_scripts?hl=zh-cn

**Contents:**
- 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 了解内容脚本功能
- 在隔离的世界中工作
- 注入脚本
  - 通过静态声明进行注入
  - 通过动态声明注入
  - 以编程方式注入
  - 排除匹配项和 glob
  - 运行时间
  - 指定帧

内容脚本是在网页上下文中运行的文件。通过标准文档对象模型 (DOM)，它们能够读取浏览器访问的网页的详细信息、对其进行更改，并将信息传递给其父扩展程序。

内容脚本可以直接访问以下扩展程序 API：

内容脚本无法直接访问其他 API。不过，它们可以通过与扩展程序的其他部分交换消息来间接访问这些变量。

您还可以使用 fetch() 等 API 从内容脚本访问扩展程序中的其他文件。为此，您需要将它们声明为可供 Web 访问的资源。请注意，这也会将资源公开给在同一网站上运行的任何第一方或第三方脚本。

内容脚本位于隔离的世界中，因此内容脚本可以更改其 JavaScript 环境，而不会与网页或其他扩展程序的内容脚本发生冲突。

扩展程序可以在网页中运行，其代码类似于以下示例。

该扩展程序可以使用注入脚本部分中介绍的某种技术来注入以下内容脚本。

此次更改后，当点击按钮时，两个提醒会依次显示。

内容脚本可以静态声明、动态声明或以编程方式注入。

对于应在已知的一组网页上自动运行的脚本，请在 manifest.json 中使用静态内容脚本声明。

静态声明的脚本在清单中通过 "content_scripts" 键进行注册。它们可以包含 JavaScript 文件、CSS 文件或同时包含这两种文件。所有自动运行的内容脚本都必须指定匹配模式。

如果内容脚本的匹配模式不太明确，或者不应始终在已知主机上注入内容脚本，那么动态内容脚本会很有用。

动态声明是在 Chrome 96 中引入的，与静态声明类似，但内容脚本对象是使用 chrome.scripting 命名空间中的方法（而不是在 manifest.json 中）向 Chrome 注册的。借助 Scripting API，扩展程序开发者还可以：

与静态声明一样，动态声明可以包含 JavaScript 文件、CSS 文件或两者兼而有之。

对于需要响应事件或在特定情况下运行的内容脚本，请使用程序化注入。

如需以编程方式注入内容脚本，您的扩展程序需要获得其尝试注入脚本的网页的主机权限。可以通过在扩展程序清单中请求宿主权限来授予宿主权限，也可以使用 "activeTab" 临时授予宿主权限。

以下是基于 activeTab 的扩展程序的另一个版本。

或者，函数正文可以作为内容脚本注入并执行。

请注意，注入的函数是 chrome.scripting.executeScript() 调用中引用的函数的副本，而不是原始函数本身。因此，函数的正文必须是独立的；对函数外部变量的引用会导致内容脚本抛出 ReferenceError。

以函数形式注入时，您还可以向函数传递实参。

如需自定义指定的网页匹配，请在声明性注册中添加以下字段。

如果同时满足以下两个条件，内容脚本将被注入到网页中：

以下扩展程序会将内容脚本注入 https://www.nytimes.com/health，但不会注入 https://www.nytimes.com/business。

与匹配模式相比，glob 属性采用的语法不同，也更灵活。可接受的 glob 字符串是可能包含“通配符”星号和问号的网址。星号 (*) 可匹配任意长度的任何字符串（包括空字符串），而问号 (?) 可匹配任何单个字符。

例如，glob https://???.example.com/foo/\* 可与以下任何内容匹配：

此扩展程序会将内容脚本注入 https://www.nytimes.com/arts/index.html 和 https://www.nytimes.com/jobs/index.htm*，但不会注入 https://www.nytimes.com/sports/index.html：

此扩展程序会将内容脚本注入 https://history.nytimes.com 和 https://.nytimes.com/history，但不会注入 https://science.nytimes.com 或 https://www.nytimes.com/science：

您可以包含其中一个、全部或部分范围，以实现正确的范围。

run_at 字段用于控制何时将 JavaScript 文件注入到网页中。首选值和默认值为 "document_idle"。如需了解其他可能的值，请参阅 RunAt 类型。

对于清单中声明的内容脚本，扩展程序可以通过 "all_frames" 字段指定是否应将 JavaScript 和 CSS 文件注入到符合指定网址要求的所有框架中，还是仅注入到标签页中的最顶层框架中：

使用 chrome.scripting.registerContentScripts(...) 以编程方式注册内容脚本时，可以使用 allFrames 参数来指定内容脚本应注入到符合指定网址要求的所有框架中，还是仅注入到标签页中的最顶层框架中。此参数只能与 tabId 一起使用，如果指定了 frameIds 或 documentIds，则无法使用此参数：

扩展程序可能需要在与匹配框架相关的框架中运行脚本，但这些框架本身并不匹配。如果出现这种情况，一个常见的情景是：框架的网址是由匹配的框架创建的，但这些网址本身与脚本指定的格式不匹配。

当扩展程序想要注入具有 about:、data:、blob: 和 filesystem: 方案的网址的框架时，就会出现这种情况。在这些情况下，网址将与内容脚本的模式不匹配（并且，对于 about: 和 data:，网址甚至根本不包含父网址或来源，如 about:blank 或 data:text/html,<html>Hello, World!</html> 中所示）。不过，这些框架仍可与创建框架相关联。

如需注入到这些框架中，扩展程序可以在清单中针对内容脚本规范指定 "match_origin_as_fallback" 属性。

如果指定了该属性并将其设置为 true，Chrome 将查看框架启动器的来源，以确定框架是否匹配，而不是查看框架本身的网址。请注意，这可能也不同于目标框架的来源（例如，data: 网址具有 null 源）。

框架的启动器是创建或导航目标框架的框架。虽然这通常是直接父级或打开程序，但也有可能不是（例如，在框架导航 iframe 内的 iframe 的情况下）。

由于此方法会比较发起方框架的来源，因此发起方框架可能位于该来源的任何路径上。为了明确这一含义，Chrome 要求任何将 "match_origin_as_fallback" 设置为 true 的内容脚本也指定 * 的路径。

如果同时指定了 "match_origin_as_fallback" 和 "match_about_blank"，则以 "match_origin_as_fallback" 为准。

虽然内容脚本的执行环境与托管它们的网页的执行环境相互隔离，但它们共享对网页 DOM 的访问权限。如果网页希望通过内容脚本与内容脚本或扩展程序通信，则必须通过共享 DOM 进行通信。

以下示例可使用 window.postMessage() 完成：

非扩展程序网页 example.html 会向自身发布消息。此消息会被内容脚本拦截并检查，然后发布到扩展程序进程。这样一来，网页便与扩展程序进程建立了一条通信线路。也可以通过类似方式实现反向操作。

如需从内容脚本访问扩展程序文件，您可以调用 chrome.runtime.getURL() 来获取扩展程序资源的绝对网址，如以下示例 (content.js) 所示：

如需在 CSS 文件中使用字体或图片，您可以使用 @@extension_id 构建网址，如以下示例 (content.css) 所示：

所有资源都必须在 manifest.json 文件中声明为可供网页访问的资源：

在隔离的世界中运行的内容脚本具有以下内容安全政策 (CSP)：

与其他扩展程序上下文应用的限制类似，此限制可防止使用 eval() 以及加载外部脚本。

对于未打包的扩展程序，CSP 还包括本地主机：

当内容脚本注入到主世界时，网页的 CSP 会生效。

虽然隔离的世界提供了一层保护，但使用内容脚本可能会在扩展程序和网页中造成漏洞。如果内容脚本从其他网站接收内容（例如通过调用 fetch()），请务必先过滤内容，以防范跨站脚本攻击，然后再注入内容。仅通过 HTTPS 进行通信，以避免遭受"man-in-the-middle"攻击。

请务必过滤恶意网页。例如，以下模式很危险，在清单 V3 中是不允许的：

建议改用更安全的 API，这些 API 不会运行脚本：

**Examples:**

Example 1 (javascript):
```javascript
<html>
  <button id="mybutton">click me</button>
  <script>
    var greeting = "hello, ";
    var button = document.getElementById("mybutton");
    button.person_name = "Bob";
    button.addEventListener(
        "click", () => alert(greeting + button.person_name + "."), false);
  </script>
</html>
```

Example 2 (javascript):
```javascript
var greeting = "hola, ";
var button = document.getElementById("mybutton");
button.person_name = "Roberto";
button.addEventListener(
    "click", () => alert(greeting + button.person_name + "."), false);
```

Example 3 (unknown):
```unknown
{
 "name": "My extension",
 ...
 "content_scripts": [
   {
     "matches": ["https://*.nytimes.com/*"],
     "css": ["my-styles.css"],
     "js": ["content-script.js"]
   }
 ],
 ...
}
```

Example 4 (javascript):
```javascript
chrome.scripting
  .registerContentScripts([{
    id: "session-script",
    js: ["content.js"],
    persistAcrossSessions: false,
    matches: ["*://example.com/*"],
    runAt: "document_start",
  }])
  .then(() => console.log("registration complete"))
  .catch((err) => console.warn("unexpected error", err))
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
{
  ...
  "manifest_version": 2
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "manifest_version": 3
  ...
}
```

Example 3 (unknown):
```unknown
{
  ...
  "permissions": [
    "tabs",
    "bookmarks",
    "https://www.blogger.com/"
  ],
  "optional_permissions": [
    "unlimitedStorage",
    "*://*/*"
  ]
  ...
}
```

Example 4 (unknown):
```unknown
{
  ...
  "permissions": [
    "tabs",
    "bookmarks"
  ],
  "optional_permissions": [
    "unlimitedStorage"
  ],
  "host_permissions": [
    "https://www.blogger.com/"
  ],
  "optional_host_permissions": [
    "*://*/*"
  ]
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
{
  ...
  "background": {
    "scripts": [
      "backgroundContextMenus.js",
      "backgroundOauth.js"
    ],
    "persistent": false
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "background": {
    "service_worker": "service_worker.js",
    "type": "module"
  }
  ...
}
```

Example 3 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: chrome.runtime.getURL('offscreen.html'),
  reasons: ['CLIPBOARD'],
  justification: 'testing the offscreen API',
});
```

Example 4 (javascript):
```javascript
let textEl = document.querySelector('#text');
textEl.value = data;
textEl.select();
document.execCommand('copy');
```

---

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions?hl=zh-cn

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 2 (javascript):
```javascript
document.querySelector('#my-button').addEventListener('click', (event) => {
  // Permissions must be requested from inside a user gesture, like a button's
  // click handler.
  chrome.permissions.request({
    permissions: ['tabs'],
    origins: ['https://www.google.com/']
  }, (granted) => {
    // The callback argument will be true if the user granted the permissions.
    if (granted) {
      doSomething();
    } else {
      doSomethingElse();
    }
  });
});
```

Example 3 (javascript):
```javascript
chrome.permissions.contains({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (result) => {
  if (result) {
    // The extension has the permissions.
  } else {
    // The extension doesn't have the permissions.
  }
});
```

Example 4 (javascript):
```javascript
chrome.permissions.remove({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (removed) => {
  if (removed) {
    // The permissions have been removed.
  } else {
    // The permissions have not been removed (e.g., you tried to remove
    // required permissions).
  }
});
```

---

## 分发扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/hosting?hl=zh-cn

**Contents:**
- 分发扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如果您只想为自己构建扩展程序，可以加载未封装的扩展程序。未封装的扩展程序只能用于在开发过程中加载可信代码。

如果您不是要构建供个人使用的扩展程序，则最终需要分发该扩展程序。官方支持的分发机制只有两种。在这两种情况下，Chrome 都会定期检查扩展程序主机上已安装扩展程序的新版本，并自动更新这些扩展程序，无需用户干预。

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/what-is-mv3

**Contents:**
  - Manifest V3
- 我们的目标
- 有哪些变化？
  - 迁移到 Service Worker
  - 不再需要远程托管代码
  - 网络请求修改方面的变更
  - 其他变更
- 接下来该怎么做？
  - 迁移
  - 已知问题

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/declare_permissions?hl=zh-cn

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Permissions Extension",
  ...
  "permissions": [
    "activeTab",
    "contextMenus",
    "storage"
  ],
  "optional_permissions": [
    "topSites",
  ],
  "host_permissions": [
    "https://www.developer.chrome.com/*"
  ],
  "optional_host_permissions":[
    "https://*/*",
    "http://*/*"
  ],
  ...
  "manifest_version": 3
}
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

---

## chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/userScripts?hl=zh-cn

**Contents:**
- chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 启用 userScripts API 的使用
    - 138 之前的 Chrome 版本（开发者模式切换开关）
    - Chrome 138 及更高版本（“允许用户脚本”切换开关）
  - 检查 API 是否可用
  - 在隔离的世界中工作

使用 userScripts API 在用户脚本上下文中执行用户脚本。

如需使用用户脚本 API chrome.userScripts，请向 manifest.json 添加 "userScripts" 权限，并为要运行脚本的网站添加 "host_permissions"。

用户脚本是指注入到网页中的一小段代码，用于修改网页的外观或行为。与其他扩展功能（例如内容脚本和 chrome.scripting API）不同，用户脚本 API 可让您运行任意代码。如果扩展程序运行由用户提供的脚本，而这些脚本无法作为扩展程序软件包的一部分提供，则必须使用此 API。

在扩展程序获得使用 userScripts API 的权限后，用户必须启用特定切换开关，才能允许扩展程序使用该 API。所需的具体开关以及停用时的 API 行为因 Chrome 版本而异。

使用以下检查来确定用户需要启用哪个开关，例如在新用户引导期间：

以下部分介绍了不同的开关以及如何启用它们。

作为扩展程序开发者，您已在 Chrome 安装中启用开发者模式。您的用户还必须启用开发者模式。

您可以将以下说明复制并粘贴到扩展程序的用户文档中

点击开发者模式旁边的切换开关，以启用开发者模式。

允许用户脚本切换开关位于每个扩展程序的详情页面上（例如 chrome://extensions/?id=YOUR_EXTENSION_ID）。

您可以将以下说明复制并粘贴到扩展程序的用户文档中：

我们建议进行以下检查，以确定 userScripts API 是否已启用，因为该检查适用于所有 Chrome 版本。此检查会尝试调用 chrome.userScripts() 方法，当 API 可用时，该方法应始终成功。如果此调用抛出错误，则表示相应 API 不可用：

用户脚本和内容脚本都可以在隔离的世界或主世界中运行。隔离世界是主机页面或其他扩展程序无法访问的执行环境。这样一来，用户脚本就可以更改其 JavaScript 环境，而不会影响宿主页面或其他扩展程序的用户脚本和内容脚本。相反，用户脚本（和内容脚本）对宿主网页或其他扩展程序的用户脚本和内容脚本不可见。在主世界中运行的脚本可供宿主网页和其他扩展程序访问，并且对宿主网页和其他扩展程序可见。如需选择世界，请在调用 userScripts.register() 时传递 "USER_SCRIPT" 或 "MAIN"。

如需为 USER_SCRIPT 世界配置内容安全政策，请调用 userScripts.configureWorld()：

与内容脚本和离屏文档一样，用户脚本使用消息传递与其他扩展程序部分进行通信（这意味着它们可以像扩展程序的任何其他部分一样调用 runtime.sendMessage() 和 runtime.connect()）。不过，它们是使用专用事件处理程序（即不使用 onMessage 或 onConnect）接收的。这些处理程序分别称为 runtime.onUserScriptMessage 和 runtime.onUserScriptConnect。专用处理程序可让您更轻松地识别来自用户脚本（可信度较低的上下文）的消息。

在发送消息之前，您必须调用 configureWorld()，并将 messaging 实参设置为 true。请注意，您可以同时传递 csp 和 messaging 实参。

扩展程序更新时，用户脚本会被清除。您可以在扩展程序服务工作线程的 runtime.onInstalled 事件处理程序中运行代码，以重新添加它们。仅对传递给事件回调的 "update" 原因做出响应。

此示例来自我们示例代码库中的 userScript 示例。

以下示例展示了对 register() 的基本调用。第一个实参是一个对象数组，用于定义要注册的脚本。此处仅列出了部分选项。

用户脚本要在其中执行的 JavaScript 世界。

“MAIN” 指定 DOM 的执行环境，即与宿主网页的 JavaScript 共享的执行环境。

“USER_SCRIPT” 指定了用户脚本特有的执行环境，不受网页的 CSP 限制。

错误（如果有）。error 和 result 是互斥的。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

指定用户脚本不会注入到的网页的通配符模式。

排除此用户脚本原本会注入到的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的用户脚本的 ID。此属性不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

ScriptSource 对象的列表，用于定义要注入到匹配网页中的脚本的来源。必须为 ${ref:register} 指定此属性，并且指定时必须是一个非空数组。

指定此用户脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 ${ref:register} 指定此属性。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

用于运行脚本的 JavaScript 执行环境。默认值为 `USER_SCRIPT`。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

包含要注入的 JavaScript 代码的字符串。必须指定 file 或 code 中的一个。

要注入的 JavaScript 文件的路径（相对于扩展程序的根目录）。必须指定 file 或 code 中的一个。

getScripts 仅返回具有此列表中指定 ID 的脚本。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

ScriptSource 对象列表，用于定义要注入到目标中的脚本的来源。

运行脚本的 JavaScript“世界”。默认值为 USER_SCRIPT。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

指定全球 CSP。默认值为 `ISOLATED` 全球 csp。

指定是否公开消息传递 API。默认值为 false。

指定要更新的特定用户脚本世界的 ID。如果未提供，则更新默认用户脚本世界的属性。以英文下划线 (_) 开头的值是预留值。

配置 `USER_SCRIPT` 执行环境。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回相应扩展程序的所有动态注册的用户脚本。

如果指定，此方法仅返回与之匹配的用户脚本。

Promise<RegisteredUserScript[]>

Promise<WorldProperties[]>

RegisteredUserScript[]

重置用户脚本世界的配置。任何注入到具有指定 ID 的世界中的脚本都将使用默认世界配置。

要重置的用户脚本世界的 ID。如果省略，则重置默认世界的配置。

取消注册相应扩展程序的所有动态注册的用户脚本。

如果指定了此参数，此方法将仅取消注册与之匹配的用户脚本。

RegisteredUserScript[]

包含要更新的用户脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "User script test extension",
  "manifest_version": 3,
  "minimum_chrome_version": "120",
  "permissions": [
    "userScripts"
  ],
  "host_permissions": [
    "*://example.com/*"
  ]
}
```

Example 2 (javascript):
```javascript
let version = Number(navigator.userAgent.match(/(Chrome|Chromium)\/([0-9]+)/)?.[2]);
if (version >= 138) {
  // Allow User Scripts toggle will be used.
} else {
  // Developer mode toggle will be used.
}
```

Example 3 (unknown):
```unknown
function isUserScriptsAvailable() {
  try {
    // Method call which throws if API permission or toggle is not enabled.
    chrome.userScripts.getScripts();
    return true;
  } catch {
    // Not available.
    return false;
  }
}
```

Example 4 (unknown):
```unknown
chrome.userScripts.configureWorld({
  csp: "script-src 'self'"
});
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

---

## 使用其他安装方法 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/external_extensions?hl=zh-cn

**Contents:**
- 使用其他安装方法 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 准备工作
  - 从 Chrome 应用商店安装
  - 从本地 CRX 文件安装
  - 从个人服务器安装
- 使用偏好设置文件
  - macOS
    - 排查 Mac OS 权限问题
  - Linux
  - 支持的语言区域

通常，Chrome 用户是通过访问 Chrome 应用商店中的扩展程序列表来安装扩展程序的 并直接从该页面安装扩展程序。但在某些情况下 会更合适。例如：

对于上述情况，Google Chrome 支持以下扩展程序安装方法：

这两种方式都支持安装托管在 update_URL 上的扩展程序。在 Windows 和 macOS 上， update_URL 必须指向 Chrome 应用商店。使用这些方法安装扩展程序时 Windows 和 macOS 用户必须使用以下确认对话框启用该扩展程序：

在 Linux 上，偏好设置文件可以指向 Chrome 应用商店扩展程序，即外部托管的 扩展程序或 CRX 扩展程序文件。Linux 用户 提示您启用相应扩展程序；系统会自动安装它

如果您要分发托管在 Chrome 应用商店中的扩展程序，必须先发布 扩展程序。然后，记下以下内容：

如果您是通过本地文件向 Linux 用户分发应用，则需要将 CRX 打包 文件，并记下以下信息：

扩展程序 ID - 可以在扩展程序管理页面 chrome://extensions 中找到。

扩展程序版本 - 显示在扩展程序管理页面 chrome://extensions 或 。

如果您要为 Linux 用户分发托管在个人服务器上的扩展程序，则需要执行以下操作： 请按照在 Linux 上安装扩展程序的说明进行操作，并注意以下几点： 信息：

扩展程序 ID - 可以在扩展程序管理页面 chrome://extensions 中找到。

update_url XML 文件路径：必须与 清单 JSON 文件中声明的 update_url 字段。

以下示例假定版本为 1.0，扩展程序 ID 为 aaabbbcccdddeeefff。

请使用字段名称“external_update_url”指定更新网址。例如：json { "external_update_url": "https://clients2.google.com/service/update2/crx" }。

启动 Google Chrome，然后转到 chrome://extensions；您应该会看到该扩展程序已列出

在 macOS 上，仅当文件系统权限设置时，系统才会读取所有用户的外部扩展程序文件 以防止无特权的用户更改权限如果您在安装外部扩展程序时没有看到 Chrome 已启动，外部扩展程序偏好设置可能存在权限问题 文件。要检查是否是这个原因，请按以下步骤操作：

以下列表介绍了通过 Chrome 应用商店安装扩展程序、CRX 文件或 个人服务器：

启动 Google Chrome，然后转到 chrome://extensions；您应该会看到该扩展程序已列出

如果您只想为某些浏览器语言区域安装扩展程序，可以列出受支持的语言区域 在字段名称“supported_locales”中访问。语言区域可以指定父级语言区域，例如“en”，在这种情况下， 将针对所有英语语言区域（如“en-US”、“en-GB”等）进行安装。如果其他浏览器 该扩展程序不支持所选的语言区域，则外部扩展程序将 已卸载。如果“supported_locales”列表缺失，则会针对所有语言区域安装该扩展程序。 例如：

在 Extensions 密钥下创建一个与您的 ID 相同的新密钥（文件夹） 。例如：aaabbbcccdddeeefff。

在扩展程序密钥中，创建一个“update_url”属性，并将其设置为以下值： json { "update_url": "https://clients2.google.com/service/update2/crx" }

前往 chrome://extensions；您应该会看到该扩展程序已列出

Google Chrome 每次浏览器都会扫描偏好设置和注册表中的元数据条目 启动，并对 Chrome 中托管的已安装外部扩展程序进行必要的更改 应用商店。

要将本地 CRX 文件扩展名更新为新版本，请更新文件，然后更新版本 。

若要卸载扩展程序（例如软件已卸载），请移除偏好设置 文件（例如 aaabbbcccdddeeefff.json）或注册表中的元数据。

这一部分解答了有关外部扩展程序的常见问题。

可以，但只能作为从 Chrome 应用商店 update_url 安装，而不是通过本地 CRX 路径安装。如需了解详情，请参阅应用和扩展程序政策。

如果用户通过界面卸载扩展程序，系统将不会再在以下位置安装或更新扩展程序： 也就是说，外部扩展程序已被列入屏蔽名单。

如果用户卸载了您的扩展程序，您应该尊重用户的决定。但是，如果您（ 开发者）不小心通过界面卸载了您的扩展程序，您可以移除屏蔽名单标记 正常通过界面安装扩展程序，然后将其卸载。

**Examples:**

Example 1 (unknown):
```unknown
{
  "external_update_url": "https://clients2.google.com/service/update2/crx",
  "supported_locales": [ "en", "fr", "de" ]
}
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

Example 2 (unknown):
```unknown
{
  ...
  "content_scripts": [
    {
      "matches": ["https://*.example.com/*"],
      "include_globs": ["https://???.example.com/foo/*"],
      "js": ["content-script.js"]
    }
  ],
  ...
}
```

Example 3 (unknown):
```unknown
https://www.example.com/foo/bar
https://the.example.com/foo/
```

Example 4 (unknown):
```unknown
https://my.example.com/foo/bar
https://example.com/foo/*
https://www.example.com/foo
```

---

## 匹配模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/match_patterns?hl=zh-cn

**Contents:**
- 匹配模式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 特殊情况
- 示例格式

匹配模式是一种具有以下结构的网址，用于指定一组网址：

scheme：必须是以下各项之一，并使用英文冒号后跟双斜线 (://) 与模式的其余部分分隔：

如需了解如何将内容脚本注入不受支持的架构（例如 about: 和 data:），请参阅在相关帧中注入。

host：主机名 (www.example.com)。主机名前面的 * 用于匹配子网域 (*.example.com)，或者仅使用通配符 *。 - 如果您在主机模式中使用通配符，则通配符必须是第一个字符或唯一字符，并且必须紧跟英文句点 (.) 或正斜线 (/)。

path：网址路径 (/example)。对于主机权限，路径是必需的，但会被忽略。应遵循惯例使用通配符 (/*)。

**Examples:**

Example 1 (unknown):
```unknown
<scheme>://<host>/<path>
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

Example 2 (unknown):
```unknown
{
  ...
  "content_scripts": [
    {
      "matches": ["https://*.example.com/*"],
      "include_globs": ["https://???.example.com/foo/*"],
      "js": ["content-script.js"]
    }
  ],
  ...
}
```

Example 3 (unknown):
```unknown
https://www.example.com/foo/bar
https://the.example.com/foo/
```

Example 4 (unknown):
```unknown
https://my.example.com/foo/bar
https://example.com/foo/*
https://www.example.com/foo
```

---

## 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/google-analytics-4?hl=zh-cn

**Contents:**
- 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 要求
- 使用 Google Analytics Measurement Protocol
  - 设置 API 凭据
  - 生成 client_id
  - 发送分析事件
  - 使用建议的参数 session_id 和 engagement_time_msec
- 跟踪弹出式窗口、侧边栏和扩展程序页面中的网页浏览量
- 在 Service Worker 中跟踪分析事件
- 调试

本教程演示如何使用 Google Analytics 跟踪扩展程序的使用情况。您可以在 GitHub 上找到有效的 Google Analytics 4 示例，其中 google-analytics.js 包含所有 Google Analytics 相关代码。

本教程假定您熟悉编写 Chrome 扩展程序。如果您需要了解如何编写扩展程序，请参阅入门教程。

此外，您还必须设置 Google Analytics 4 账号才能跟踪您的扩展程序。请注意，在设置账号时，您可以使用“网站网址”字段中的任何值，因为您的扩展程序不会有自己的网址。

从 Manifest V3 开始，Chrome 扩展程序不得执行远程托管的代码。也就是说，您必须使用 Google Analytics Measurement Protocol 来跟踪扩展程序事件。利用 Measurement Protocol，您可以通过 HTTP 请求直接将事件发送到 Google Analytics 服务器。这种方法的一大优势在于，它允许您从扩展程序中的任何位置（包括 Service Worker）发送分析事件。

第一步是获取 api_secret 和 measurement_id。请参阅 Measurement Protocol 文档，了解如何为您的 Google Analytics 账号获取这些数据。

第二步是为特定设备/用户生成唯一标识符，即 client_id。只要扩展程序安装在用户浏览器中，ID 就应保持不变。它可以是任意字符串，但对客户端而言应该是唯一的。您可以通过调用 self.crypto.randomUUID() 生成一个。将 client_id 存储在 chrome.storage.local 中，以确保其在安装扩展程序期间保持不变。

要使用 chrome.storage.local，您需要在清单文件中拥有 storage 权限：

然后，您可以使用 chrome.storage.local 存储 client_id：

借助 API 凭据和 client_id，您可以通过 fetch 请求向 Google Analytics 发送事件：

这样会发送 button_clicked 事件，该事件会显示在您的 Google Analytics 事件报告中。如果您想在 Google Analytics 实时报告中查看事件，则需要提供两个额外的参数：session_id 和 engagement_time_msec。

session_id 和 engagement_time_msec 都是使用 Google Analytics Measurement Protocol 时的推荐参数，因为它们在实时等标准报告中显示用户活动时必不可少。

session_id 描述了用户持续与您的扩展程序互动的时间段。默认情况下，会话会在用户处于不活动状态 30 分钟后结束。会话无持续时间限制。

与常规网站不同，Chrome 扩展程序中没有明确的用户会话概念。因此，您必须在扩展程序中定义用户会话的含义。例如，每次新的用户互动都可能是一次新会话。在这种情况下，您只需为每个事件生成一个新的会话 ID（即使用时间戳）。

以下示例演示了一种方法，该方法会在没有报告任何事件 30 分钟后使新会话超时（您可以自定义此时间，以更好地适应您的扩展程序的用户行为）。该示例使用 chrome.storage.session 来存储浏览器运行时的活动会话。我们将与会话一起存储上次触发事件的时间。我们可以通过以下方法判断当前会话是否已过期：

以下示例将 session_id 和 engagement_time_msec 添加到了上一个按钮点击事件请求中。对于 engagement_time_msec，您可以提供默认值 100 ms。

该事件在 Google Analytics 实时报告中将按如下方式显示。

Google Analytics Measurement Protocol 支持用于跟踪网页浏览量的特殊 page_view 事件。使用此方法跟踪访问新标签页、侧边栏或扩展程序页面（新标签页中）的用户。page_view 事件还需要 page_title 和 page_location 参数。以下示例会在文档 load 事件中针对扩展程序弹出式窗口触发网页浏览事件：

popup.js 脚本需要导入到弹出式窗口的 HTML 文件中，并且应在执行任何其他脚本之前运行：

弹出式视图将像 Google Analytics 实时报告中的任何其他网页浏览一样显示：

使用 Google Analytics Measurement Protocol 可以跟踪扩展程序 Service Worker 中的分析事件。例如，通过监听 Service Worker 中的 unhandledrejection event，您可以将 Service Worker 中任何未捕获的异常记录到 Google Analytics，这在很大程度上有助于调试用户可能报告的问题。

现在，您可以在 Google Analytics 报告中查看错误事件：

Google Analytics 提供了两项实用功能，用于在扩展程序中调试 Analytics 事件：

**Examples:**

Example 1 (unknown):
```unknown
{
  …
  "permissions": ["storage"],
  …
}
```

Example 2 (javascript):
```javascript
async function getOrCreateClientId() {
  const result = await chrome.storage.local.get('clientId');
  let clientId = result.clientId;
  if (!clientId) {
    // Generate a unique client ID, the actual value is not relevant
    clientId = self.crypto.randomUUID();
    await chrome.storage.local.set({clientId});
  }
  return clientId;
}
```

Example 3 (javascript):
```javascript
const GA_ENDPOINT = 'https://www.google-analytics.com/mp/collect';
const MEASUREMENT_ID = `G-...`;
const API_SECRET = `...`;

fetch(
  `${GA_ENDPOINT}?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`,
  {
    method: 'POST',
    body: JSON.stringify({
      client_id: await getOrCreateClientId(),
      events: [
        {
          name: 'button_clicked',
          params: {
            id: 'my-button',
          },
        },
      ],
    }),
  }
);
```

Example 4 (javascript):
```javascript
const SESSION_EXPIRATION_IN_MIN = 30;

async function getOrCreateSessionId() {
  // Store session in memory storage
  let {sessionData} = await chrome.storage.session.get('sessionData');
  // Check if session exists and is still valid
  const currentTimeInMs = Date.now();
  if (sessionData && sessionData.timestamp) {
    // Calculate how long ago the session was last updated
    const durationInMin = (currentTimeInMs - sessionData.timestamp) / 60000;
    // Check if last update lays past the session expiration threshold
    if (durationInMin > SESSION_EXPIRATION_IN_MIN) {
      // Delete old session id to start a new session
      sessionData = null;
    } else {
      // Update timestamp to keep session alive
      sessionData.timestamp = currentTimeInMs;
      await chrome.storage.session.set({sessionData});
    }
  }
  if (!sessionData) {
    // Create and store a new session
    sessionData = {
      session_id: currentTimeInMs.toString(),
      timestamp: currentTimeInMs.toString(),
    };
    await chrome.storage.session.set({sessionData});
  }
  return sessionData.session_id;
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

Example 2 (unknown):
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

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Click to run",
  "description": "Runs a script when the user clicks the action toolbar icon.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  "permissions": ["scripting", "activeTab"]
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Popup extension that requests permissions",
  "description": "Extension that includes a popup and requests host permissions and storage permissions .",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "action": {
    "default_popup": "popup.html"
  },
  "host_permissions": [
    "https://*.example.com/"
  ],
  "permissions": [
    "storage"
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

Example 2 (unknown):
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

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Click to run",
  "description": "Runs a script when the user clicks the action toolbar icon.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  "permissions": ["scripting", "activeTab"]
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Popup extension that requests permissions",
  "description": "Extension that includes a popup and requests host permissions and storage permissions .",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "action": {
    "default_popup": "popup.html"
  },
  "host_permissions": [
    "https://*.example.com/"
  ],
  "permissions": [
    "storage"
  ]
}
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/publish-mv3

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

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
<script src="./react-dom.production.min.js"></script>
<link href="./bootstrap.min.css" rel="stylesheet">
```

Example 2 (unknown):
```unknown
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['jquery-min.js', 'content-script.js']
});
```

Example 3 (javascript):
```javascript
let name = 'World!';
chrome.tabs.executeScript({
  code: `alert('Hello, ${name}!')`
});
```

Example 4 (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

function showAlert(givenName) {
  alert(`Hello, ${givenName}`);
}

let name = 'World';
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  func: showAlert,
  args: [name],
});
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

---

## 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions-list

**Contents:**
- 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如需访问大多数扩展程序 API 和功能，您必须在扩展程序的清单中声明权限。某些权限会触发警告，用户必须允许才能继续使用扩展程序。

如需详细了解权限的运作方式，请参阅声明权限。如需了解有关在有警告的情况下使用权限的最佳实践，请参阅权限警告指南。

以下列出了所有可用权限以及特定权限触发的所有警告。

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

Example 2 (unknown):
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

## chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/management?hl=zh-cn

**Contents:**
- chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ExtensionDisabledReason
    - 枚举
  - ExtensionInfo
    - 属性
  - ExtensionInstallType
    - 枚举

chrome.management API 提供了管理安装式应用和扩展程序的方式。

必须在扩展程序清单中声明“管理”权限，才能使用 Management API。例如：

management.getPermissionWarningsByManifest()、management.uninstallSelf() 和 management.getSelf() 不需要管理权限。

"permissions_increase"

与已安装的扩展程序、应用或主题相关的信息。

ExtensionDisabledReason 可选

图标信息列表。请注意，这仅反映清单中声明的内容，实际图片尺寸可能与声明不符，建议在引用这些图像的 img 标签中显式指定宽度和高度属性。详见图标清单文档。

请使用 management.ExtensionInfo.type。

用户是否可以启用此扩展程序。仅对未启用的扩展程序返回此值。

扩展程序、应用或主题是否声明支持离线功能。

扩展程序、应用或主题的版本名称（如清单中已指定）。

扩展程序的安装方式。可能值包括 admin：因管理政策而安装； development：在开发者模式下以解压方式加载； normal：通过 .crx 文件正常安装； sideload：由机器上的其他软件安装； other：通过其他方式安装。

"legacy_packaged_app"

"login_screen_extension"

表示图标宽度和高度的数字。可能的值包括（但不限于）128、48、24 和 16。

图标图像的网址。如需显示图标的灰度版本（例如，指示扩展程序已禁用），可在网之后附加 ?grayscale=true。

"OPEN_AS_REGULAR_TAB"

是否应提示用户显示确认卸载对话框。自行卸载时，默认值为 false。如果扩展程序卸载其他扩展程序，系统会忽略此参数，并始终显示对话框。

显示为应用创建快捷方式的选项。在 Mac 上仅支持为打包应用创建。

应为 management.ExtensionInfo 应用项中的 ID。

网页的网址。网址的架构只能为“http”或“https”。

Promise<ExtensionInfo>

返回有关具有指定 ID 的已安装扩展程序、应用或主题的信息。

management.ExtensionInfo 项目的 ID。

Promise<ExtensionInfo>

返回有关已安装的扩展程序和应用的信息列表。

Promise<ExtensionInfo[]>

返回给定扩展程序清单字符串的权限警告列表。注意：使用此函数时，无需在清单中请求“管理”权限。

返回有关调用扩展程序、应用或主题的信息。注意：使用此函数时，无需在清单中请求“管理”权限。

Promise<ExtensionInfo>

启动清单中指定的 replacement_web_app。若未安装，提示用户安装。

启用或停用应用或扩展程序。在大多数情况下，此函数必须在用户手势（如按钮的 onclick 处理程序）上下文中调用，并且可能会向用户展示原生确认界面以防止滥用。

此值应为 management.ExtensionInfo 中某个项目的 ID。

应为 management.ExtensionInfo 应用项中的 ID。

目标启动类型。请务必检查并确保此启动类型位于 ExtensionInfo.availableLaunchTypes 中，因为可用的启动类型因平台和配置而异。

卸载当前安装式应用或扩展程序。注意：在用户未被授权卸载指定扩展程序/应用的受管理环境中，此功能将无法执行。若卸载失败（如用户取消对话框），系统将拒绝 promise 或回调将被调用，同时设置 runtime.lastError。

此值应为 management.ExtensionInfo 中某个项目的 ID。

卸载调用扩展程序。注意：使用此函数时，无需在清单中请求“管理”权限。但若用户无法卸载指定的扩展程序/应用，此函数在受管理环境中将无法执行。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "management"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.management.createAppShortcut(  id: string,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.management.generateAppForLink(  url: string,  title: string,): Promise<ExtensionInfo>
```

Example 4 (unknown):
```unknown
chrome.management.get(  id: string,): Promise<ExtensionInfo>
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

Example 3 (unknown):
```unknown
<script src="_modules/cccccccccccccccccccccccccccccccc/foo.js">
```

Example 4 (unknown):
```unknown
chrome-extension://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/_modules/cccccccccccccccccccccccccccccccc/
```

---

## 使用 Puppeteer 测试 Chrome 扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/tut_puppeteer-testing?hl=zh-cn

**Contents:**
- 使用 Puppeteer 测试 Chrome 扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前期准备
- 编写测试
  - 第 1 步：启动 Node.JS 项目
  - 第 2 步：安装 Puppeteer 和 Jest
  - 第 3 步：创建入口点
  - 第 4 步：启动浏览器
  - 第 5 步：添加别名
  - 第 6 步：打开弹出式窗口
  - 第 7 步：断言当前状态

Puppeteer 提供了一个用于构建网站自动化测试的框架，还包括测试 Chrome 扩展程序的功能。这些是高级端到端测试，用于测试网站或扩展程序在最终产品中构建后是否正常运行。在本教程中，我们将演示如何针对示例代码库中的扩展程序编写基本测试。

克隆或下载 chrome-extensions-samples 代码库。我们将使用 api-samples/history/showHistory 中的 History API 演示作为测试扩展程序。

您还需要安装 Node.JS，它是 Puppeteer 的构建基础运行时。

我们需要设置一个基本的 Node.JS 项目。在新文件夹中，创建一个包含以下内容的 package.json 文件：

与扩展程序的 manifest.json 文件类似，所有 Node 项目都需要此文件。

运行 npm install puppeteer jest 以将 Puppeteer 和 Jest 添加为依赖项。系统会自动将它们添加到您的 package.json 文件中。

您可以编写独立的 Puppeteer 测试，但我们将使用 Jest 作为测试运行程序，为代码提供一些额外的结构。

创建一个名为 index.test.js 的新文件，并添加以下代码：

更新了 beforeEach 和 afterEach，以启动和关闭浏览器。运行多项测试时，您不妨考虑使用同一浏览器。不过，通常不建议这样做，因为这会降低测试之间的隔离性，并可能会导致一项测试影响另一项测试的结果。

为了更轻松地运行测试，请向 package.json 文件添加别名：

这将运行当前目录中以 .test.js 结尾的所有文件。

我们来添加一个基本测试，以便在新页面中打开弹出式窗口。我们需要执行此操作，因为 Puppeteer 不支持从弹出式窗口访问扩展程序弹出式窗口。添加以下代码：

我们来断言一下，以便在扩展程序的行为不符合预期时测试失败。我们知道我们的弹出式窗口应显示最近访问过的网页，因此我们来检查一下是否看到了：

如需运行测试，请使用 npm start。您应该会看到指示测试已通过的输出。

您可以在我们的 chrome-extensions-samples 代码库中查看完整项目。

掌握基本知识后，尝试为您自己的扩展程序构建测试套件。Puppeteer API 参考文档详细介绍了 Puppeteer 的各种功能，其中包含许多未在此处介绍的功能。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "puppeteer-demo",
  "version": "1.0"
}
```

Example 2 (javascript):
```javascript
const puppeteer = require('puppeteer');

const EXTENSION_PATH = '../../api-samples/history/showHistory';
const EXTENSION_ID = 'jkomgjfbbjocikdmilgaehbfpllalmia';

let browser;

beforeEach(async () => {
  // TODO: Launch the browser.
});

afterEach(async () => {
  // TODO: Close the browser.
});
```

Example 3 (javascript):
```javascript
beforeEach(async () => {
  browser = await puppeteer.launch({
    headless: false,
    pipe: true,
    enableExtensions: [EXTENSION_PATH]
  });
});

afterEach(async () => {
  await browser.close();
  browser = undefined;
});
```

Example 4 (unknown):
```unknown
{
  "name": "puppeteer-demo",
  "version": "1.0",
  "dependencies": {
    "puppeteer": "^24.8.1"
  },
  "scripts": {
    "start": "jest ."
  }
}
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
{
  ...
  "background": {
    "scripts": [
      "backgroundContextMenus.js",
      "backgroundOauth.js"
    ],
    "persistent": false
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "background": {
    "service_worker": "service_worker.js",
    "type": "module"
  }
  ...
}
```

Example 3 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: chrome.runtime.getURL('offscreen.html'),
  reasons: ['CLIPBOARD'],
  justification: 'testing the offscreen API',
});
```

Example 4 (javascript):
```javascript
let textEl = document.querySelector('#text');
textEl.value = data;
textEl.select();
document.execCommand('copy');
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

---

## chrome.webRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webRequest

**Contents:**
- chrome.webRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 请求的生命周期
  - 请求 ID
  - 注册事件监听器
  - 处理身份验证
  - 实现细节
    - web_accessible_resources

使用 chrome.webRequest API 观察和分析流量，并拦截、阻止或修改正在处理的请求。

您必须在扩展程序清单中声明 "webRequest" 权限，才能使用 Web 请求 API，同时还需声明必要的主机权限。如需拦截子资源请求，扩展程序必须有权访问所请求的网址及其发起者。例如：

注册阻塞事件处理脚本时需要此权限。从 Manifest V3 开始，此功能仅适用于通过政策安装的扩展程序。

webRequestAuthProvider

使用 onAuthRequired 方法时必需。请参阅处理身份验证。

Web 请求 API 定义了一组遵循 Web 请求生命周期的事件。您可以使用这些事件来观察和分析流量。某些同步事件可让您拦截、阻止或修改请求。

下图显示了成功请求的事件生命周期，随后是事件定义：

Web 请求 API 保证，对于每个请求，onCompleted 或 onErrorOccurred 都会作为最终事件触发，但有一种例外情况：如果请求重定向到 data:// 网址，onBeforeRedirect 将是最后报告的事件。

* 请注意，Web 请求 API 向扩展程序呈现了网络堆栈的抽象。在内部，一个网址请求可以拆分为多个 HTTP 请求（例如，从大文件中提取各个字节范围），也可以由网络堆栈处理，而无需与网络通信。因此，该 API 不会提供发送到网络的最终 HTTP 标头。例如，与缓存相关的所有标头对扩展程序都是不可见的。

目前未向 onBeforeSendHeaders 事件提供以下标头。此列表不能保证完整或稳定。

从 Chrome 79 开始，请求标头修改会影响跨源资源共享 (CORS) 检查。如果跨源请求的修改后标头不符合条件，则会导致发送 CORS 预检，以询问服务器是否可以接受此类标头。如果您确实需要以违反 CORS 协议的方式修改标头，则需要在 opt_extraInfoSpec 中指定 'extraHeaders'。另一方面，响应标头修改无法欺骗 CORS 检查。如果您需要欺骗 CORS 协议，还需要为响应修改指定 'extraHeaders'。

从 Chrome 79 开始，webRequest API 默认不会拦截 CORS 预检请求和响应。如果扩展程序在 opt_extraInfoSpec 中为请求网址指定了 'extraHeaders' 的监听器，则该扩展程序可以查看相应请求网址的 CORS 预检。onBeforeRequest 还可以从 Chrome 79 中获取 'extraHeaders'。

从 Chrome 79 开始，以下请求标头不会提供，并且在未在 opt_extraInfoSpec 中指定 'extraHeaders' 的情况下，无法修改或移除该标头：

从 Chrome 72 开始，如果您需要在 Cross Origin Read Blocking (CORB) 屏蔽响应之前修改响应，则需要在 opt_extraInfoSpec 中指定 'extraHeaders'。

从 Chrome 72 开始，以下请求标头不会提供，并且在 opt_extraInfoSpec 中未指定 'extraHeaders' 的情况下，无法修改或移除这些标头：

从 Chrome 72 开始，Set-Cookie 响应标头未提供，并且无法在 opt_extraInfoSpec 中不指定 'extraHeaders' 的情况下修改或移除。

从 Chrome 89 开始，如果不指定 opt_extraInfoSpec 中的 'extraHeaders'，则无法有效修改或移除 X-Frame-Options 响应标头。

webRequest API 仅公开扩展程序有权查看的请求（根据其主机权限）。此外，只有以下方案可供访问：http://、https://、ftp://、file://、ws://（自 Chrome 58 起）、wss://（自 Chrome 58 起）、urn:（自 Chrome 91 起）或 chrome-extension://。此外，即使某些请求的网址使用上述方案之一，也会被隐藏。这些请求包括 chrome-extension://other_extension_id（其中 other_extension_id 不是要处理请求的扩展程序的 ID）、https://www.google.com/chrome 以及对浏览器功能至关重要的其他敏感请求。此外，来自扩展程序的同步 XMLHttpRequests 会对阻塞事件处理脚本隐藏，以防止出现死锁。请注意，对于某些受支持的方案，由于相应协议的性质，可用事件的集合可能受到限制。例如，对于文件方案，只能调度 onBeforeRequest、onResponseStarted、onCompleted 和 onErrorOccurred。

从 Chrome 58 开始，webRequest API 支持拦截 WebSocket 握手请求。由于握手是通过 HTTP 升级请求完成的，因此其流程符合面向 HTTP 的 webRequest 模型。请注意，该 API 不会拦截：

从 Chrome 72 开始，扩展程序只有在同时拥有所请求网址和请求发起者的主机权限时，才能拦截请求。

从 Chrome 96 开始，webRequest API 支持拦截通过 HTTP/3 进行的 WebTransport 握手请求。由于握手是通过 HTTP CONNECT 请求完成的，因此其流程符合面向 HTTP 的 webRequest 模型。请注意：

每个请求都通过请求 ID 进行标识。此 ID 在浏览器会话和扩展程序上下文中是唯一的。在请求的生命周期内保持不变，可用于匹配同一请求的事件。请注意，在 HTTP 重定向或 HTTP 身份验证的情况下，多个 HTTP 请求会映射到一个 Web 请求。

如需为 Web 请求注册事件监听器，您可以使用常用的 addListener() 函数的变体。除了指定回调函数之外，您还必须指定过滤条件实参，并且可以指定可选的额外信息实参。

Web 请求 API 的 addListener() 的三个实参具有以下定义：

以下示例展示了如何监听 onBeforeRequest 事件：

每个 addListener() 调用都将一个必需的回调函数作为第一个参数。此回调函数会传递一个字典，其中包含有关当前网址请求的信息。此字典中的信息取决于具体事件类型以及 opt_extraInfoSpec 的内容。

如果可选的 opt_extraInfoSpec 数组包含字符串 'blocking'（仅允许用于特定事件），则回调函数会同步处理。这意味着，在回调函数返回之前，请求会被阻塞。在这种情况下，回调可以返回一个 webRequest.BlockingResponse，用于确定请求的后续生命周期。根据上下文，此响应允许取消或重定向请求 (onBeforeRequest)、取消请求或修改标头 (onBeforeSendHeaders、onHeadersReceived)，以及取消请求或提供身份验证凭据 (onAuthRequired)。

如果可选的 opt_extraInfoSpec 数组包含字符串 'asyncBlocking'（仅允许用于 onAuthRequired），则扩展程序可以异步生成 webRequest.BlockingResponse。

webRequest.RequestFilter filter 允许在各种维度上限制触发事件的请求：

根据事件类型，您可以在 opt_extraInfoSpec 中指定字符串，以请求有关请求的更多信息。仅在明确要求时，才用于提供有关请求数据的详细信息。

如需处理 HTTP 身份验证请求，请将 "webRequestAuthProvider" 权限添加到清单文件中：

请注意，对于具有 "webRequestBlocking" 权限的已安装政策扩展程序，此权限不是必需的。

在开发使用 Web 请求 API 的扩展程序时，了解以下几个实现细节非常重要：

如果扩展程序使用 webRequest API 将公共资源请求重定向到无法通过网络访问的资源，则该请求会被阻止，并导致错误。即使无法通过网络访问的资源归重定向扩展程序所有，上述情况也适用。如需声明用于声明性 WebRequest API 的资源，必须在清单中声明并填充 "web_accessible_resources" 数组，如此处所述。

在当前的网络请求 API 实现中，如果至少有一个扩展程序指示取消请求，则该请求会被视为已取消。如果某个扩展程序取消了请求，系统会通过 onErrorOccurred 事件通知所有扩展程序。一次只能有一个扩展程序重定向请求或修改标头。如果多个扩展程序尝试修改请求，则最近安装的扩展程序会胜出，而所有其他扩展程序都会被忽略。如果扩展程序修改或重定向的指令被忽略，系统不会通知该扩展程序。

Chrome 使用两种缓存：磁盘缓存和速度极快的内存缓存。内存缓存的生命周期与渲染进程的生命周期相关联，大致相当于一个标签页。从内存中缓存应答的请求对 Web 请求 API 不可见。如果请求处理程序更改了其行为（例如，根据哪些请求进行屏蔽的行为），简单的网页刷新可能不会遵循此更改后的行为。为确保行为变更生效，请调用 handlerBehaviorChanged() 以刷新内存中缓存。但不要经常这样做；刷新缓存是一项成本非常高昂的操作。注册或取消注册事件监听器后，您无需调用 handlerBehaviorChanged()。

Web 请求事件的 timestamp 属性仅保证内部一致性。比较一个事件与另一个事件会得出它们之间的正确偏移量，但将它们与扩展程序内的当前时间（例如通过 (new Date()).getTime()）进行比较可能会得出意外结果。

如果您尝试使用无效实参注册事件，系统会抛出 JavaScript 错误，并且不会注册事件处理脚本。如果在处理事件时抛出错误，或者事件处理程序返回无效的阻塞响应，则系统会将错误消息记录到扩展程序的控制台中，并针对相应请求忽略该处理程序。

以下示例展示了如何屏蔽对 www.evil.com 的所有请求：

由于此函数使用阻塞事件处理程序，因此需要在清单文件中添加 "webRequest" 和 "webRequestBlocking" 权限。

以下示例以更高效的方式实现了相同的目标，因为未定位到 www.evil.com 的请求无需传递给扩展程序：

以下示例说明了如何从所有请求中删除 User-Agent 标头：

如需试用 chrome.webRequest API，请从 chrome-extension-samples 代码库安装 webRequest 示例。

返回应用了“blocking”extraInfoSpec 的事件处理脚本的值。允许事件处理程序修改网络请求。

仅用作对 onAuthRequired 事件的响应。如果设置，则使用提供的凭据发出请求。

如果为 true，则取消请求。这样可以防止发送请求。此属性可用作对 onBeforeRequest、onBeforeSendHeaders、onHeadersReceived 和 onAuthRequired 事件的响应。

仅用作对 onBeforeRequest 和 onHeadersReceived 事件的响应。如果设置了此属性，则系统会阻止发送/完成原始请求，而是将其重定向到指定的网址。允许重定向到非 HTTP 方案（例如 data:）。由重定向操作发起的重定向会使用原始请求方法进行重定向，但有一种例外情况：如果重定向是在 onHeadersReceived 阶段发起的，则会使用 GET 方法发出重定向。系统会忽略来自具有 ws:// 和 wss:// 方案的网址的重定向。

仅用作对 onBeforeSendHeaders 事件的响应。如果设置了此字段，则会使用这些请求标头发出请求。

仅用作对 onHeadersReceived 事件的响应。如果设置了此属性，则假定服务器已使用这些响应标头进行响应。只有在您确实想要修改标头以限制冲突数量时（每个请求只能有一个扩展程序修改 responseHeaders），才返回 responseHeaders。

包含在表单数据中传递的数据。对于网址编码的表单，如果数据是 UTF-8 字符串，则存储为字符串；否则存储为 ArrayBuffer。对于表单数据，它是 ArrayBuffer。如果 form-data 表示上传文件，则为包含文件名的字符串（如果提供了文件名）。

HTTP 标头的数组。每个标头都表示为一个字典，其中包含键 name 以及 value 或 binaryValue。

如果 HTTP 标头的值无法用 UTF-8 表示，则以单个字节值 (0..255) 存储。

HTTP 标头的值（如果可以用 UTF-8 表示）。

“responseHeaders” 指定应在事件中包含响应标头。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

"asyncBlocking" 指定回调函数以异步方式处理。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“requestBody” 指定请求正文应包含在事件中。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“requestHeaders” 指定应在事件中包含请求标头。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“securityInfo” 指定应在事件中包含 SecurityInfo。

"securityInfoRawDer" 指定应在事件中包含具有证书原始字节的 SecurityInfo。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“requestHeaders” 指定应在事件中包含请求标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

一个对象，用于描述要应用于 webRequest 事件的过滤条件。

请求类型列表。无法与任何类型匹配的请求会被过滤掉。

网址或网址格式的列表。无法与任何网址匹配的请求会被过滤掉。

“main_frame” 将资源指定为主框架。

“sub_frame” 将资源指定为子框架。

“stylesheet” 将资源指定为样式表。

“xmlhttprequest” 将资源指定为 XMLHttpRequest。

“csp_report” 将资源指定为内容安全政策 (CSP) 报告。

“websocket” 将资源指定为 WebSocket。

“webbundle” 将资源指定为 WebBundle。

“其他” 将资源指定为未包含在所列类型中的类型。

连接的状态。安全、不安全、已损坏中的一个。

在持续 10 分钟的时间间隔内，handlerBehaviorChanged 可被调用的次数上限。handlerBehaviorChanged 是一个开销很大的函数调用，不应经常调用。

当 webRequest 处理程序的行为发生变化时需要调用，以防止因缓存而导致处理不正确。此函数调用开销较大。不要经常调用。

当扩展程序对网络请求的建议修改被忽略时触发。如果与其他扩展程序发生冲突，就会出现这种情况。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

在收到身份验证失败消息时触发。监听器有三种选择：提供身份验证凭据、取消请求并显示错误页面，或者对质询不采取任何操作。如果提供的用户凭据无效，则可能会针对同一请求多次调用此方法。请注意，extraInfoSpec 参数中只能指定 'blocking' 或 'asyncBlocking' 模式中的一种。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

对于 Proxy-Authenticate 为 True，对于 WWW-Authenticate 为 False。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

身份验证方案，例如 Basic 或 Digest。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

asyncCallback 参数的格式如下：

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnAuthRequiredOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

随此重定向一起收到的 HTTP 响应标头。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnBeforeRedirectOptions[] 可选

extensionTypes.DocumentLifecycle 可选

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType 可选

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

包含 HTTP 请求正文数据。仅当 extraInfoSpec 包含“requestBody”时才提供。

如果请求方法为 POST，并且正文是采用 UTF8 编码的键值对序列，编码格式为 multipart/form-data 或 application/x-www-form-urlencoded，则此字典存在，并且对于每个键，都包含该键的所有值列表。如果数据属于其他媒体类型或格式有误，则不存在字典。此字典的一个示例值为 {'key': ['value1', 'value2']}。

如果请求方法为 PUT 或 POST，并且正文尚未在 formData 中解析，则此数组包含未解析的请求正文元素。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnBeforeRequestOptions[] 可选

在发送 HTTP 请求之前（请求标头可用时）触发。这种情况可能发生在与服务器建立 TCP 连接之后，但在发送任何 HTTP 数据之前。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

将随此请求一起发送的 HTTP 请求标头。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnBeforeSendHeadersOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnCompletedOptions[] 可选

发出请求的文档的 UUID。如果请求是框架的导航，则此值不存在。

extensionTypes.DocumentLifecycle

错误说明。我们不保证此字符串在不同版本之间保持向后兼容。您不得解析并根据其内容采取行动。

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnErrorOccurredOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

有关用于底层连接的 TLS/QUIC 连接的信息。仅当 extraInfoSpec 参数中指定了 securityInfo 时才提供。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnHeadersReceivedOptions[] 可选

在收到响应正文的第一个字节时触发。对于 HTTP 请求，这意味着状态行和响应标头可用。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnResponseStartedOptions[] 可选

在即将向服务器发送请求之前触发（在 onSendHeaders 触发时，之前 onBeforeSendHeaders 回调的修改可见）。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnSendHeadersOptions[] 可选

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "webRequest"
  ],
  "host_permissions": [
    "*://*.google.com/*"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var callback = function(details) {...};
var filter = {...};
var opt_extraInfoSpec = [...];
```

Example 3 (unknown):
```unknown
chrome.webRequest.onBeforeRequest.addListener(
    callback, filter, opt_extraInfoSpec);
```

Example 4 (unknown):
```unknown
{
  "permissions": [
    "webRequest",
    "webRequestAuthProvider"
  ]
}
```

---

## 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/google-analytics-4

**Contents:**
- 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 要求
- 使用 Google Analytics Measurement Protocol
  - 设置 API 凭据
  - 生成 client_id
  - 发送分析事件
  - 使用建议的参数 session_id 和 engagement_time_msec
- 跟踪弹出式窗口、侧边栏和扩展程序页面中的网页浏览量
- 在 Service Worker 中跟踪分析事件
- 调试

本教程演示如何使用 Google Analytics 跟踪扩展程序的使用情况。您可以在 GitHub 上找到有效的 Google Analytics 4 示例，其中 google-analytics.js 包含所有 Google Analytics 相关代码。

本教程假定您熟悉编写 Chrome 扩展程序。如果您需要了解如何编写扩展程序，请参阅入门教程。

此外，您还必须设置 Google Analytics 4 账号才能跟踪您的扩展程序。请注意，在设置账号时，您可以使用“网站网址”字段中的任何值，因为您的扩展程序不会有自己的网址。

从 Manifest V3 开始，Chrome 扩展程序不得执行远程托管的代码。也就是说，您必须使用 Google Analytics Measurement Protocol 来跟踪扩展程序事件。利用 Measurement Protocol，您可以通过 HTTP 请求直接将事件发送到 Google Analytics 服务器。这种方法的一大优势在于，它允许您从扩展程序中的任何位置（包括 Service Worker）发送分析事件。

第一步是获取 api_secret 和 measurement_id。请参阅 Measurement Protocol 文档，了解如何为您的 Google Analytics 账号获取这些数据。

第二步是为特定设备/用户生成唯一标识符，即 client_id。只要扩展程序安装在用户浏览器中，ID 就应保持不变。它可以是任意字符串，但对客户端而言应该是唯一的。您可以通过调用 self.crypto.randomUUID() 生成一个。将 client_id 存储在 chrome.storage.local 中，以确保其在安装扩展程序期间保持不变。

要使用 chrome.storage.local，您需要在清单文件中拥有 storage 权限：

然后，您可以使用 chrome.storage.local 存储 client_id：

借助 API 凭据和 client_id，您可以通过 fetch 请求向 Google Analytics 发送事件：

这样会发送 button_clicked 事件，该事件会显示在您的 Google Analytics 事件报告中。如果您想在 Google Analytics 实时报告中查看事件，则需要提供两个额外的参数：session_id 和 engagement_time_msec。

session_id 和 engagement_time_msec 都是使用 Google Analytics Measurement Protocol 时的推荐参数，因为它们在实时等标准报告中显示用户活动时必不可少。

session_id 描述了用户持续与您的扩展程序互动的时间段。默认情况下，会话会在用户处于不活动状态 30 分钟后结束。会话无持续时间限制。

与常规网站不同，Chrome 扩展程序中没有明确的用户会话概念。因此，您必须在扩展程序中定义用户会话的含义。例如，每次新的用户互动都可能是一次新会话。在这种情况下，您只需为每个事件生成一个新的会话 ID（即使用时间戳）。

以下示例演示了一种方法，该方法会在没有报告任何事件 30 分钟后使新会话超时（您可以自定义此时间，以更好地适应您的扩展程序的用户行为）。该示例使用 chrome.storage.session 来存储浏览器运行时的活动会话。我们将与会话一起存储上次触发事件的时间。我们可以通过以下方法判断当前会话是否已过期：

以下示例将 session_id 和 engagement_time_msec 添加到了上一个按钮点击事件请求中。对于 engagement_time_msec，您可以提供默认值 100 ms。

该事件在 Google Analytics 实时报告中将按如下方式显示。

Google Analytics Measurement Protocol 支持用于跟踪网页浏览量的特殊 page_view 事件。使用此方法跟踪访问新标签页、侧边栏或扩展程序页面（新标签页中）的用户。page_view 事件还需要 page_title 和 page_location 参数。以下示例会在文档 load 事件中针对扩展程序弹出式窗口触发网页浏览事件：

popup.js 脚本需要导入到弹出式窗口的 HTML 文件中，并且应在执行任何其他脚本之前运行：

弹出式视图将像 Google Analytics 实时报告中的任何其他网页浏览一样显示：

使用 Google Analytics Measurement Protocol 可以跟踪扩展程序 Service Worker 中的分析事件。例如，通过监听 Service Worker 中的 unhandledrejection event，您可以将 Service Worker 中任何未捕获的异常记录到 Google Analytics，这在很大程度上有助于调试用户可能报告的问题。

现在，您可以在 Google Analytics 报告中查看错误事件：

Google Analytics 提供了两项实用功能，用于在扩展程序中调试 Analytics 事件：

**Examples:**

Example 1 (unknown):
```unknown
{
  …
  "permissions": ["storage"],
  …
}
```

Example 2 (javascript):
```javascript
async function getOrCreateClientId() {
  const result = await chrome.storage.local.get('clientId');
  let clientId = result.clientId;
  if (!clientId) {
    // Generate a unique client ID, the actual value is not relevant
    clientId = self.crypto.randomUUID();
    await chrome.storage.local.set({clientId});
  }
  return clientId;
}
```

Example 3 (javascript):
```javascript
const GA_ENDPOINT = 'https://www.google-analytics.com/mp/collect';
const MEASUREMENT_ID = `G-...`;
const API_SECRET = `...`;

fetch(
  `${GA_ENDPOINT}?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`,
  {
    method: 'POST',
    body: JSON.stringify({
      client_id: await getOrCreateClientId(),
      events: [
        {
          name: 'button_clicked',
          params: {
            id: 'my-button',
          },
        },
      ],
    }),
  }
);
```

Example 4 (javascript):
```javascript
const SESSION_EXPIRATION_IN_MIN = 30;

async function getOrCreateSessionId() {
  // Store session in memory storage
  let {sessionData} = await chrome.storage.session.get('sessionData');
  // Check if session exists and is still valid
  const currentTimeInMs = Date.now();
  if (sessionData && sessionData.timestamp) {
    // Calculate how long ago the session was last updated
    const durationInMin = (currentTimeInMs - sessionData.timestamp) / 60000;
    // Check if last update lays past the session expiration threshold
    if (durationInMin > SESSION_EXPIRATION_IN_MIN) {
      // Delete old session id to start a new session
      sessionData = null;
    } else {
      // Update timestamp to keep session alive
      sessionData.timestamp = currentTimeInMs;
      await chrome.storage.session.set({sessionData});
    }
  }
  if (!sessionData) {
    // Create and store a new session
    sessionData = {
      session_id: currentTimeInMs.toString(),
      timestamp: currentTimeInMs.toString(),
    };
    await chrome.storage.session.set({sessionData});
  }
  return sessionData.session_id;
}
```

---

## chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/userScripts

**Contents:**
- chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 启用 userScripts API 的使用
    - 138 之前的 Chrome 版本（开发者模式切换开关）
    - Chrome 138 及更高版本（“允许用户脚本”切换开关）
  - 检查 API 是否可用
  - 在隔离的世界中工作

使用 userScripts API 在用户脚本上下文中执行用户脚本。

如需使用用户脚本 API chrome.userScripts，请向 manifest.json 添加 "userScripts" 权限，并为要运行脚本的网站添加 "host_permissions"。

用户脚本是指注入到网页中的一小段代码，用于修改网页的外观或行为。与其他扩展功能（例如内容脚本和 chrome.scripting API）不同，用户脚本 API 可让您运行任意代码。如果扩展程序运行由用户提供的脚本，而这些脚本无法作为扩展程序软件包的一部分提供，则必须使用此 API。

在扩展程序获得使用 userScripts API 的权限后，用户必须启用特定切换开关，才能允许扩展程序使用该 API。所需的具体开关以及停用时的 API 行为因 Chrome 版本而异。

使用以下检查来确定用户需要启用哪个开关，例如在新用户引导期间：

以下部分介绍了不同的开关以及如何启用它们。

作为扩展程序开发者，您已在 Chrome 安装中启用开发者模式。您的用户还必须启用开发者模式。

您可以将以下说明复制并粘贴到扩展程序的用户文档中

点击开发者模式旁边的切换开关，以启用开发者模式。

允许用户脚本切换开关位于每个扩展程序的详情页面上（例如 chrome://extensions/?id=YOUR_EXTENSION_ID）。

您可以将以下说明复制并粘贴到扩展程序的用户文档中：

我们建议进行以下检查，以确定 userScripts API 是否已启用，因为该检查适用于所有 Chrome 版本。此检查会尝试调用 chrome.userScripts() 方法，当 API 可用时，该方法应始终成功。如果此调用抛出错误，则表示相应 API 不可用：

用户脚本和内容脚本都可以在隔离的世界或主世界中运行。隔离世界是主机页面或其他扩展程序无法访问的执行环境。这样一来，用户脚本就可以更改其 JavaScript 环境，而不会影响宿主页面或其他扩展程序的用户脚本和内容脚本。相反，用户脚本（和内容脚本）对宿主网页或其他扩展程序的用户脚本和内容脚本不可见。在主世界中运行的脚本可供宿主网页和其他扩展程序访问，并且对宿主网页和其他扩展程序可见。如需选择世界，请在调用 userScripts.register() 时传递 "USER_SCRIPT" 或 "MAIN"。

如需为 USER_SCRIPT 世界配置内容安全政策，请调用 userScripts.configureWorld()：

与内容脚本和离屏文档一样，用户脚本使用消息传递与其他扩展程序部分进行通信（这意味着它们可以像扩展程序的任何其他部分一样调用 runtime.sendMessage() 和 runtime.connect()）。不过，它们是使用专用事件处理程序（即不使用 onMessage 或 onConnect）接收的。这些处理程序分别称为 runtime.onUserScriptMessage 和 runtime.onUserScriptConnect。专用处理程序可让您更轻松地识别来自用户脚本（可信度较低的上下文）的消息。

在发送消息之前，您必须调用 configureWorld()，并将 messaging 实参设置为 true。请注意，您可以同时传递 csp 和 messaging 实参。

扩展程序更新时，用户脚本会被清除。您可以在扩展程序服务工作线程的 runtime.onInstalled 事件处理程序中运行代码，以重新添加它们。仅对传递给事件回调的 "update" 原因做出响应。

此示例来自我们示例代码库中的 userScript 示例。

以下示例展示了对 register() 的基本调用。第一个实参是一个对象数组，用于定义要注册的脚本。此处仅列出了部分选项。

用户脚本要在其中执行的 JavaScript 世界。

“MAIN” 指定 DOM 的执行环境，即与宿主网页的 JavaScript 共享的执行环境。

“USER_SCRIPT” 指定了用户脚本特有的执行环境，不受网页的 CSP 限制。

错误（如果有）。error 和 result 是互斥的。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

指定用户脚本不会注入到的网页的通配符模式。

排除此用户脚本原本会注入到的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的用户脚本的 ID。此属性不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

ScriptSource 对象的列表，用于定义要注入到匹配网页中的脚本的来源。必须为 ${ref:register} 指定此属性，并且指定时必须是一个非空数组。

指定此用户脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 ${ref:register} 指定此属性。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

用于运行脚本的 JavaScript 执行环境。默认值为 `USER_SCRIPT`。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

包含要注入的 JavaScript 代码的字符串。必须指定 file 或 code 中的一个。

要注入的 JavaScript 文件的路径（相对于扩展程序的根目录）。必须指定 file 或 code 中的一个。

getScripts 仅返回具有此列表中指定 ID 的脚本。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

ScriptSource 对象列表，用于定义要注入到目标中的脚本的来源。

运行脚本的 JavaScript“世界”。默认值为 USER_SCRIPT。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

指定全球 CSP。默认值为 `ISOLATED` 全球 csp。

指定是否公开消息传递 API。默认值为 false。

指定要更新的特定用户脚本世界的 ID。如果未提供，则更新默认用户脚本世界的属性。以英文下划线 (_) 开头的值是预留值。

配置 `USER_SCRIPT` 执行环境。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回相应扩展程序的所有动态注册的用户脚本。

如果指定，此方法仅返回与之匹配的用户脚本。

Promise<RegisteredUserScript[]>

Promise<WorldProperties[]>

RegisteredUserScript[]

重置用户脚本世界的配置。任何注入到具有指定 ID 的世界中的脚本都将使用默认世界配置。

要重置的用户脚本世界的 ID。如果省略，则重置默认世界的配置。

取消注册相应扩展程序的所有动态注册的用户脚本。

如果指定了此参数，此方法将仅取消注册与之匹配的用户脚本。

RegisteredUserScript[]

包含要更新的用户脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "User script test extension",
  "manifest_version": 3,
  "minimum_chrome_version": "120",
  "permissions": [
    "userScripts"
  ],
  "host_permissions": [
    "*://example.com/*"
  ]
}
```

Example 2 (javascript):
```javascript
let version = Number(navigator.userAgent.match(/(Chrome|Chromium)\/([0-9]+)/)?.[2]);
if (version >= 138) {
  // Allow User Scripts toggle will be used.
} else {
  // Developer mode toggle will be used.
}
```

Example 3 (unknown):
```unknown
function isUserScriptsAvailable() {
  try {
    // Method call which throws if API permission or toggle is not enabled.
    chrome.userScripts.getScripts();
    return true;
  } catch {
    // Not available.
    return false;
  }
}
```

Example 4 (unknown):
```unknown
chrome.userScripts.configureWorld({
  csp: "script-src 'self'"
});
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

## chrome.webRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webRequest?hl=zh-cn

**Contents:**
- chrome.webRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 请求的生命周期
  - 请求 ID
  - 注册事件监听器
  - 处理身份验证
  - 实现细节
    - web_accessible_resources

使用 chrome.webRequest API 观察和分析流量，并拦截、阻止或修改正在处理的请求。

您必须在扩展程序清单中声明 "webRequest" 权限，才能使用 Web 请求 API，同时还需声明必要的主机权限。如需拦截子资源请求，扩展程序必须有权访问所请求的网址及其发起者。例如：

注册阻塞事件处理脚本时需要此权限。从 Manifest V3 开始，此功能仅适用于通过政策安装的扩展程序。

webRequestAuthProvider

使用 onAuthRequired 方法时必需。请参阅处理身份验证。

Web 请求 API 定义了一组遵循 Web 请求生命周期的事件。您可以使用这些事件来观察和分析流量。某些同步事件可让您拦截、阻止或修改请求。

下图显示了成功请求的事件生命周期，随后是事件定义：

Web 请求 API 保证，对于每个请求，onCompleted 或 onErrorOccurred 都会作为最终事件触发，但有一种例外情况：如果请求重定向到 data:// 网址，onBeforeRedirect 将是最后报告的事件。

* 请注意，Web 请求 API 向扩展程序呈现了网络堆栈的抽象。在内部，一个网址请求可以拆分为多个 HTTP 请求（例如，从大文件中提取各个字节范围），也可以由网络堆栈处理，而无需与网络通信。因此，该 API 不会提供发送到网络的最终 HTTP 标头。例如，与缓存相关的所有标头对扩展程序都是不可见的。

目前未向 onBeforeSendHeaders 事件提供以下标头。此列表不能保证完整或稳定。

从 Chrome 79 开始，请求标头修改会影响跨源资源共享 (CORS) 检查。如果跨源请求的修改后标头不符合条件，则会导致发送 CORS 预检，以询问服务器是否可以接受此类标头。如果您确实需要以违反 CORS 协议的方式修改标头，则需要在 opt_extraInfoSpec 中指定 'extraHeaders'。另一方面，响应标头修改无法欺骗 CORS 检查。如果您需要欺骗 CORS 协议，还需要为响应修改指定 'extraHeaders'。

从 Chrome 79 开始，webRequest API 默认不会拦截 CORS 预检请求和响应。如果扩展程序在 opt_extraInfoSpec 中为请求网址指定了 'extraHeaders' 的监听器，则该扩展程序可以查看相应请求网址的 CORS 预检。onBeforeRequest 还可以从 Chrome 79 中获取 'extraHeaders'。

从 Chrome 79 开始，以下请求标头不会提供，并且在未在 opt_extraInfoSpec 中指定 'extraHeaders' 的情况下，无法修改或移除该标头：

从 Chrome 72 开始，如果您需要在 Cross Origin Read Blocking (CORB) 屏蔽响应之前修改响应，则需要在 opt_extraInfoSpec 中指定 'extraHeaders'。

从 Chrome 72 开始，以下请求标头不会提供，并且在 opt_extraInfoSpec 中未指定 'extraHeaders' 的情况下，无法修改或移除这些标头：

从 Chrome 72 开始，Set-Cookie 响应标头未提供，并且无法在 opt_extraInfoSpec 中不指定 'extraHeaders' 的情况下修改或移除。

从 Chrome 89 开始，如果不指定 opt_extraInfoSpec 中的 'extraHeaders'，则无法有效修改或移除 X-Frame-Options 响应标头。

webRequest API 仅公开扩展程序有权查看的请求（根据其主机权限）。此外，只有以下方案可供访问：http://、https://、ftp://、file://、ws://（自 Chrome 58 起）、wss://（自 Chrome 58 起）、urn:（自 Chrome 91 起）或 chrome-extension://。此外，即使某些请求的网址使用上述方案之一，也会被隐藏。这些请求包括 chrome-extension://other_extension_id（其中 other_extension_id 不是要处理请求的扩展程序的 ID）、https://www.google.com/chrome 以及对浏览器功能至关重要的其他敏感请求。此外，来自扩展程序的同步 XMLHttpRequests 会对阻塞事件处理脚本隐藏，以防止出现死锁。请注意，对于某些受支持的方案，由于相应协议的性质，可用事件的集合可能受到限制。例如，对于文件方案，只能调度 onBeforeRequest、onResponseStarted、onCompleted 和 onErrorOccurred。

从 Chrome 58 开始，webRequest API 支持拦截 WebSocket 握手请求。由于握手是通过 HTTP 升级请求完成的，因此其流程符合面向 HTTP 的 webRequest 模型。请注意，该 API 不会拦截：

从 Chrome 72 开始，扩展程序只有在同时拥有所请求网址和请求发起者的主机权限时，才能拦截请求。

从 Chrome 96 开始，webRequest API 支持拦截通过 HTTP/3 进行的 WebTransport 握手请求。由于握手是通过 HTTP CONNECT 请求完成的，因此其流程符合面向 HTTP 的 webRequest 模型。请注意：

每个请求都通过请求 ID 进行标识。此 ID 在浏览器会话和扩展程序上下文中是唯一的。在请求的生命周期内保持不变，可用于匹配同一请求的事件。请注意，在 HTTP 重定向或 HTTP 身份验证的情况下，多个 HTTP 请求会映射到一个 Web 请求。

如需为 Web 请求注册事件监听器，您可以使用常用的 addListener() 函数的变体。除了指定回调函数之外，您还必须指定过滤条件实参，并且可以指定可选的额外信息实参。

Web 请求 API 的 addListener() 的三个实参具有以下定义：

以下示例展示了如何监听 onBeforeRequest 事件：

每个 addListener() 调用都将一个必需的回调函数作为第一个参数。此回调函数会传递一个字典，其中包含有关当前网址请求的信息。此字典中的信息取决于具体事件类型以及 opt_extraInfoSpec 的内容。

如果可选的 opt_extraInfoSpec 数组包含字符串 'blocking'（仅允许用于特定事件），则回调函数会同步处理。这意味着，在回调函数返回之前，请求会被阻塞。在这种情况下，回调可以返回一个 webRequest.BlockingResponse，用于确定请求的后续生命周期。根据上下文，此响应允许取消或重定向请求 (onBeforeRequest)、取消请求或修改标头 (onBeforeSendHeaders、onHeadersReceived)，以及取消请求或提供身份验证凭据 (onAuthRequired)。

如果可选的 opt_extraInfoSpec 数组包含字符串 'asyncBlocking'（仅允许用于 onAuthRequired），则扩展程序可以异步生成 webRequest.BlockingResponse。

webRequest.RequestFilter filter 允许在各种维度上限制触发事件的请求：

根据事件类型，您可以在 opt_extraInfoSpec 中指定字符串，以请求有关请求的更多信息。仅在明确要求时，才用于提供有关请求数据的详细信息。

如需处理 HTTP 身份验证请求，请将 "webRequestAuthProvider" 权限添加到清单文件中：

请注意，对于具有 "webRequestBlocking" 权限的已安装政策扩展程序，此权限不是必需的。

在开发使用 Web 请求 API 的扩展程序时，了解以下几个实现细节非常重要：

如果扩展程序使用 webRequest API 将公共资源请求重定向到无法通过网络访问的资源，则该请求会被阻止，并导致错误。即使无法通过网络访问的资源归重定向扩展程序所有，上述情况也适用。如需声明用于声明性 WebRequest API 的资源，必须在清单中声明并填充 "web_accessible_resources" 数组，如此处所述。

在当前的网络请求 API 实现中，如果至少有一个扩展程序指示取消请求，则该请求会被视为已取消。如果某个扩展程序取消了请求，系统会通过 onErrorOccurred 事件通知所有扩展程序。一次只能有一个扩展程序重定向请求或修改标头。如果多个扩展程序尝试修改请求，则最近安装的扩展程序会胜出，而所有其他扩展程序都会被忽略。如果扩展程序修改或重定向的指令被忽略，系统不会通知该扩展程序。

Chrome 使用两种缓存：磁盘缓存和速度极快的内存缓存。内存缓存的生命周期与渲染进程的生命周期相关联，大致相当于一个标签页。从内存中缓存应答的请求对 Web 请求 API 不可见。如果请求处理程序更改了其行为（例如，根据哪些请求进行屏蔽的行为），简单的网页刷新可能不会遵循此更改后的行为。为确保行为变更生效，请调用 handlerBehaviorChanged() 以刷新内存中缓存。但不要经常这样做；刷新缓存是一项成本非常高昂的操作。注册或取消注册事件监听器后，您无需调用 handlerBehaviorChanged()。

Web 请求事件的 timestamp 属性仅保证内部一致性。比较一个事件与另一个事件会得出它们之间的正确偏移量，但将它们与扩展程序内的当前时间（例如通过 (new Date()).getTime()）进行比较可能会得出意外结果。

如果您尝试使用无效实参注册事件，系统会抛出 JavaScript 错误，并且不会注册事件处理脚本。如果在处理事件时抛出错误，或者事件处理程序返回无效的阻塞响应，则系统会将错误消息记录到扩展程序的控制台中，并针对相应请求忽略该处理程序。

以下示例展示了如何屏蔽对 www.evil.com 的所有请求：

由于此函数使用阻塞事件处理程序，因此需要在清单文件中添加 "webRequest" 和 "webRequestBlocking" 权限。

以下示例以更高效的方式实现了相同的目标，因为未定位到 www.evil.com 的请求无需传递给扩展程序：

以下示例说明了如何从所有请求中删除 User-Agent 标头：

如需试用 chrome.webRequest API，请从 chrome-extension-samples 代码库安装 webRequest 示例。

返回应用了“blocking”extraInfoSpec 的事件处理脚本的值。允许事件处理程序修改网络请求。

仅用作对 onAuthRequired 事件的响应。如果设置，则使用提供的凭据发出请求。

如果为 true，则取消请求。这样可以防止发送请求。此属性可用作对 onBeforeRequest、onBeforeSendHeaders、onHeadersReceived 和 onAuthRequired 事件的响应。

仅用作对 onBeforeRequest 和 onHeadersReceived 事件的响应。如果设置了此属性，则系统会阻止发送/完成原始请求，而是将其重定向到指定的网址。允许重定向到非 HTTP 方案（例如 data:）。由重定向操作发起的重定向会使用原始请求方法进行重定向，但有一种例外情况：如果重定向是在 onHeadersReceived 阶段发起的，则会使用 GET 方法发出重定向。系统会忽略来自具有 ws:// 和 wss:// 方案的网址的重定向。

仅用作对 onBeforeSendHeaders 事件的响应。如果设置了此字段，则会使用这些请求标头发出请求。

仅用作对 onHeadersReceived 事件的响应。如果设置了此属性，则假定服务器已使用这些响应标头进行响应。只有在您确实想要修改标头以限制冲突数量时（每个请求只能有一个扩展程序修改 responseHeaders），才返回 responseHeaders。

包含在表单数据中传递的数据。对于网址编码的表单，如果数据是 UTF-8 字符串，则存储为字符串；否则存储为 ArrayBuffer。对于表单数据，它是 ArrayBuffer。如果 form-data 表示上传文件，则为包含文件名的字符串（如果提供了文件名）。

HTTP 标头的数组。每个标头都表示为一个字典，其中包含键 name 以及 value 或 binaryValue。

如果 HTTP 标头的值无法用 UTF-8 表示，则以单个字节值 (0..255) 存储。

HTTP 标头的值（如果可以用 UTF-8 表示）。

“responseHeaders” 指定应在事件中包含响应标头。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

"asyncBlocking" 指定回调函数以异步方式处理。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“requestBody” 指定请求正文应包含在事件中。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“requestHeaders” 指定应在事件中包含请求标头。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“阻塞” 指定请求会被阻塞，直到回调函数返回。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“securityInfo” 指定应在事件中包含 SecurityInfo。

"securityInfoRawDer" 指定应在事件中包含具有证书原始字节的 SecurityInfo。

“responseHeaders” 指定应在事件中包含响应标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

“requestHeaders” 指定应在事件中包含请求标头。

“extraHeaders” 指定标头可以违反跨域资源共享 (CORS) 规则。

一个对象，用于描述要应用于 webRequest 事件的过滤条件。

请求类型列表。无法与任何类型匹配的请求会被过滤掉。

网址或网址格式的列表。无法与任何网址匹配的请求会被过滤掉。

“main_frame” 将资源指定为主框架。

“sub_frame” 将资源指定为子框架。

“stylesheet” 将资源指定为样式表。

“xmlhttprequest” 将资源指定为 XMLHttpRequest。

“csp_report” 将资源指定为内容安全政策 (CSP) 报告。

“websocket” 将资源指定为 WebSocket。

“webbundle” 将资源指定为 WebBundle。

“其他” 将资源指定为未包含在所列类型中的类型。

连接的状态。安全、不安全、已损坏中的一个。

在持续 10 分钟的时间间隔内，handlerBehaviorChanged 可被调用的次数上限。handlerBehaviorChanged 是一个开销很大的函数调用，不应经常调用。

当 webRequest 处理程序的行为发生变化时需要调用，以防止因缓存而导致处理不正确。此函数调用开销较大。不要经常调用。

当扩展程序对网络请求的建议修改被忽略时触发。如果与其他扩展程序发生冲突，就会出现这种情况。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

在收到身份验证失败消息时触发。监听器有三种选择：提供身份验证凭据、取消请求并显示错误页面，或者对质询不采取任何操作。如果提供的用户凭据无效，则可能会针对同一请求多次调用此方法。请注意，extraInfoSpec 参数中只能指定 'blocking' 或 'asyncBlocking' 模式中的一种。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

对于 Proxy-Authenticate 为 True，对于 WWW-Authenticate 为 False。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

身份验证方案，例如 Basic 或 Digest。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

asyncCallback 参数的格式如下：

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnAuthRequiredOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

随此重定向一起收到的 HTTP 响应标头。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnBeforeRedirectOptions[] 可选

extensionTypes.DocumentLifecycle 可选

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType 可选

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

包含 HTTP 请求正文数据。仅当 extraInfoSpec 包含“requestBody”时才提供。

如果请求方法为 POST，并且正文是采用 UTF8 编码的键值对序列，编码格式为 multipart/form-data 或 application/x-www-form-urlencoded，则此字典存在，并且对于每个键，都包含该键的所有值列表。如果数据属于其他媒体类型或格式有误，则不存在字典。此字典的一个示例值为 {'key': ['value1', 'value2']}。

如果请求方法为 PUT 或 POST，并且正文尚未在 formData 中解析，则此数组包含未解析的请求正文元素。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnBeforeRequestOptions[] 可选

在发送 HTTP 请求之前（请求标头可用时）触发。这种情况可能发生在与服务器建立 TCP 连接之后，但在发送任何 HTTP 数据之前。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

将随此请求一起发送的 HTTP 请求标头。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnBeforeSendHeadersOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnCompletedOptions[] 可选

发出请求的文档的 UUID。如果请求是框架的导航，则此值不存在。

extensionTypes.DocumentLifecycle

错误说明。我们不保证此字符串在不同版本之间保持向后兼容。您不得解析并根据其内容采取行动。

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnErrorOccurredOptions[] 可选

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

有关用于底层连接的 TLS/QUIC 连接的信息。仅当 extraInfoSpec 参数中指定了 securityInfo 时才提供。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

BlockingResponse | undefined

如果在“extraInfoSpec”参数中指定了“blocking”，则事件监听器应返回此类型的对象。

OnHeadersReceivedOptions[] 可选

在收到响应正文的第一个字节时触发。对于 HTTP 请求，这意味着状态行和响应标头可用。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

请求实际发送到的服务器 IP 地址。请注意，它可能是 IPv6 字面地址。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

响应的 HTTP 状态行，或 HTTP/0.9 响应（即缺少状态行的响应）的“HTTP/0.9 200 OK”字符串，如果没有标头，则为空字符串。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnResponseStartedOptions[] 可选

在即将向服务器发送请求之前触发（在 onSendHeaders 触发时，之前 onBeforeSendHeaders 回调的修改可见）。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示相应框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

发起请求的来源。此值不会因重定向而改变。如果这是不透明源，则将使用字符串“null”。

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此属性。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于关联同一请求的不同事件。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

触发相应信号的时间，以自纪元以来的毫秒数表示。

OnSendHeadersOptions[] 可选

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "webRequest"
  ],
  "host_permissions": [
    "*://*.google.com/*"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var callback = function(details) {...};
var filter = {...};
var opt_extraInfoSpec = [...];
```

Example 3 (unknown):
```unknown
chrome.webRequest.onBeforeRequest.addListener(
    callback, filter, opt_extraInfoSpec);
```

Example 4 (unknown):
```unknown
{
  "permissions": [
    "webRequest",
    "webRequestAuthProvider"
  ]
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

Example 1 (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

chrome.tabs.executeScript(
  tab.id,
  {
    file: 'content-script.js'
  }
);
```

Example 2 (javascript):
```javascript
async function getCurrentTab()
let tab = await getCurrentTab();

chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['content-script.js']
});
```

Example 3 (javascript):
```javascript
chrome.tabs.insertCSS(tabId, injectDetails, () => {
  // callback code
});
```

Example 4 (javascript):
```javascript
const insertPromise = await chrome.scripting.insertCSS({
  files: ["style.css"],
  target: { tabId: tab.id }
});
// Remaining code.
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/what-is-mv3?hl=zh-cn

**Contents:**
  - Manifest V3
- 我们的目标
- 有哪些变化？
  - 迁移到 Service Worker
  - 不再需要远程托管代码
  - 网络请求修改方面的变更
  - 其他变更
- 接下来该怎么做？
  - 迁移
  - 已知问题

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

---

## 使用地理定位 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/geolocation?hl=zh-cn

**Contents:**
- 使用地理定位 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在 MV3 扩展中使用地理定位
  - 在 Service Worker 中使用地理定位
  - 在弹出式窗口或侧边栏中使用地理定位
  - 在内容脚本中使用地理定位

如果您想在 Chrome 扩展程序中获取地理定位信息，请使用任何网站通常使用的 navigator.geolocation Web 平台 API。本文之所以存在，是因为 Chrome 扩展程序处理敏感数据访问权限的方式与处理网站权限的方式不同。地理定位是非常敏感的数据，因此浏览器需要确保用户完全了解并控制共享其确切位置的时间和位置。

在 Web 上，浏览器可以保护用户地理定位数据。同一权限模型并不总是适合扩展程序。

权限不是唯一的区别。如上所述，navigator.geolocation 是一个 DOM API，亦即构成网站的 API 的一部分。因此，它无法在 Worker 上下文中访问，例如作为 Manifest V3 扩展程序的支柱的“Extension Service Worker”。不过，您完全可以使用 geolocation。但只是使用方式和使用位置略有不同。

Service Worker 内部没有 navigator 对象。它只能在有权访问页面 document 对象的上下文中使用。如需在 Service Worker 内部获取访问权限，请使用 Offscreen Document，它可提供对可与扩展程序捆绑的 HTML 文件的访问权限。

首先，将 "offscreen" 添加到清单的 "permissions" 部分。

添加 "offscreen" 权限后，请向包含屏幕外文档的扩展程序添加一个 HTML 文件。此案例没有使用网页上的任何内容，因此该文件可能是几乎空白的文件。它只需是一个在您的脚本中加载的 HTML 小文件。

将此文件在项目的根目录中保存为 offscreen.html。

如前所述，您需要一个名为 offscreen.js 的脚本。您还需要将它与您的扩展程序绑定。它将是 Service Worker 的地理定位信息来源。您可以在它与 Service Worker 之间传递消息。

设置完成后，您就可以在 Service Worker 中访问 Offscreen Document 了。

请注意，当您访问屏幕外文档时，需要添加 reason。geolocation 原因最初不可用，因此请指定 DOM_SCRAPING 的回退，并在 justification 部分中说明代码的实际用途。Chrome 应用商店的审核流程会使用这些信息，以确保屏幕外的文档被用于有效用途。

一旦您引用了屏幕外文档，就可以向其发送消息，要求它为您提供更新后的地理定位信息。

因此，现在每当您想要从 Service Worker 获取地理定位时，只需调用：

在弹出式窗口或侧边栏中使用地理定位非常简单。弹出式窗口和侧边栏只是网络文档，因此可以访问常规 DOM API。您可以直接访问 navigator.geolocation。与标准网站的唯一区别在于，您需要使用 manifest.json "permission" 字段来请求 "geolocation" 权限。如果您不添加此权限，您将仍然拥有“navigator.geolocation”的访问权限。但是，任何试图使用它将导致立即的错误，就像用户拒绝了请求一样。您可以在弹出式窗口示例中查看相关信息。

与弹出式窗口一样，内容脚本也具有 DOM API 的完整访问权限；不过，用户将需要执行常规的用户权限流程。也就是说，将 "geolocation" 添加到您的 "permissions" 将不会自动授予您对用户的访问权限地理定位信息。如需查看相关信息，请参阅内容脚本示例。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
    ...
  "permissions": [
    ...
   "offscreen"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
<!doctype html>
<title>offscreenDocument</title>
<script src="offscreen.js"></script>
```

Example 3 (javascript):
```javascript
chrome.runtime.onMessage.addListener(handleMessages);
function handleMessages(message, sender, sendResponse) {
  // Return early if this message isn't meant for the offscreen document.
  if (message.target !== 'offscreen') {
    return;
  }

  if (message.type !== 'get-geolocation') {
    console.warn(`Unexpected message type received: '${message.type}'.`);
    return;
  }

  // You can directly respond to the message from the service worker with the
  // provided `sendResponse()` callback. But in order to be able to send an async
  // response, you need to explicitly return `true` in the onMessage handler
  // As a result, you can't use async/await here. You'd implicitly return a Promise.
  getLocation().then((loc) => sendResponse(loc));

  return true;
}

// getCurrentPosition() returns a prototype-based object, so the properties
// end up being stripped off when sent to the service worker. To get
// around this, create a deep clone.
function clone(obj) {
  const copy = {};
  // Return the value of any non true object (typeof(null) is "object") directly.
  // null will throw an error if you try to for/in it. Just return
  // the value early.
  if (obj === null || !(obj instanceof Object)) {
    return obj;
  } else {
    for (const p in obj) {
      copy[p] = clone(obj[p]);
    }
  }
  return copy;
}

async function getLocation() {
  // Use a raw Promise here so you can pass `resolve` and `reject` into the
  // callbacks for getCurrentPosition().
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(
      (loc) => resolve(clone(loc)),
      // in case the user doesnt have/is blocking `geolocation`
      (err) => reject(err)
    );
  });
}
```

Example 4 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: 'offscreen.html',
  reasons: [chrome.offscreen.Reason.GEOLOCATION || chrome.offscreen.Reason.DOM_SCRAPING],
  justification: 'geolocation access',
});
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
{
  "name": "My externally connectable extension",
  "externally_connectable": {
    "ids": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      ...
    ],
    // If this field is not specified, no web pages can connect.
    "matches": [
      "https://*.google.com/*",
      "*://*.chromium.org/*",
      ...
    ],
    "accepts_tls_channel_id": false
  },
  ...
}
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

## chrome.enterprise.hardwarePlatform 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/enterprise/hardwarePlatform

**Contents:**
- chrome.enterprise.hardwarePlatform 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - HardwarePlatformInfo
    - 属性
- 方法
  - getHardwarePlatformInfo()
    - 参数

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

获取硬件平台的制造商和型号，并在扩展程序获得授权后通过 callback 返回。

Promise<HardwarePlatformInfo>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.hardwarePlatform.getHardwarePlatformInfo(  callback?: function,): Promise<HardwarePlatformInfo>
```

Example 2 (javascript):
```javascript
(info: HardwarePlatformInfo) => void
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
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

Example 3 (unknown):
```unknown
'content_security_policy.extension_pages': Insecure CSP value "'unsafe-eval'" in directive 'script-src'.
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

---

## chrome.audio 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/audio

**Contents:**
- chrome.audio 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - AudioDeviceInfo
    - 属性
  - DeviceFilter
    - 属性
  - DeviceIdLists

chrome.audio API 可供用户获取有关连接到系统的音频设备的信息并控制这些设备。此 API 目前仅在 ChromeOS 的自助服务终端模式下可用。

简单易懂的名称（例如“USB 麦克风”）。

稳定/持久的设备 ID 字符串（如果有）。

如果设置，则只有活动状态与此值匹配的音频设备才会满足过滤条件。

如果设置了此属性，则只有流类型包含在此列表中的音频设备才会满足过滤条件。

如需表明输入设备应不受影响，请将此属性保持未设置状态。

如需表明输出设备应不受影响，请将此属性保持未设置状态。

音频设备的所需音量。默认为设备的当前音量。

如果与音频输入设备搭配使用，则表示音频设备增益。

如果与音频输出设备搭配使用，则表示音频设备音量。

静音值发生更改的数据流的类型。更新后的静音值适用于具有相应媒体流类型的所有设备。

获取根据 filter 过滤的音频设备列表。

用于过滤返回的音频设备列表的设备属性。如果未设置过滤条件或将其设置为 {}，则返回的设备列表将包含所有可用的音频设备。

Promise<AudioDeviceInfo[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

指定应处于活跃状态的设备的 ID。如果未设置输入列表或输出列表，相应类别的设备不受影响。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

为流类型设置静音状态。静音状态将应用于具有指定音频流类型的所有音频设备。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

在音频设备发生更改时触发，无论是添加新设备还是移除现有设备。

当音频输入或输出的静音状态发生变化时触发。请注意，静音状态是系统范围的，新值适用于具有指定音频流类型的每个音频设备。

**Examples:**

Example 1 (unknown):
```unknown
chrome.audio.getDevices(  filter?: DeviceFilter,  callback?: function,): Promise<AudioDeviceInfo[]>
```

Example 2 (javascript):
```javascript
(devices: AudioDeviceInfo[]) => void
```

Example 3 (unknown):
```unknown
chrome.audio.getMute(  streamType: StreamType,  callback?: function,): Promise<boolean>
```

Example 4 (javascript):
```javascript
(value: boolean) => void
```

---

## 正在获取网站图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/favicons?hl=zh-cn

**Contents:**
- 正在获取网站图标 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 访问网站的图标
  - 第 1 步：更新清单
  - 第 2 步：构建网址
- 扩展程序示例

网站图标（简称“收藏夹图标”）是显示在浏览器地址栏中的一个小图标。favicon 通常用于识别和区分网站。本文介绍了如何在 Manifest V3 扩展程序中检索网站的网站图标。

如需检索网站的 Favicon，您需要构建以下网址：

以下步骤介绍了如何在 Chrome 扩展程序中构建此网址：

首先，您必须在清单中请求 "favicon" 权限。

此外，在内容脚本中提取网站图标时，必须将 "_favicon/*" 文件夹声明为网页访问资源。例如：

以下函数使用 runtime.getURL() 创建指向 "_favicon/" 文件夹的完全限定网址。然后，它会返回一个新字符串，表示包含多个查询参数的网址。最后，该扩展程序会将图片附加到正文。

以下示例是一个包含随机扩展程序 ID 的 www.google.com 32 像素的 Favicon 网址：

chrome-extension-samples 代码库中有两个网站图标示例：

**Examples:**

Example 1 (unknown):
```unknown
chrome-extension://EXTENSION_ID/_favicon/?pageUrl=EXAMPLE_URL&size=FAV_SIZE
```

Example 2 (unknown):
```unknown
{
  "name": "Favicon API in a popup",
  "manifest_version": 3,
  ...
  "permissions": ["favicon"],
  ...
}
```

Example 3 (unknown):
```unknown
{
  "name": "Favicon API in content scripts",
  "manifest_version": 3,
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ],
  "permissions": ["favicon"],
  "web_accessible_resources": [
    {
      "resources": ["_favicon/*"],
      "matches": ["<all_urls>"],
      "extension_ids": ["*"]
    }
  ]
  ...
}
```

Example 4 (javascript):
```javascript
function faviconURL(u) {
  const url = new URL(chrome.runtime.getURL("/_favicon/"));
  url.searchParams.set("pageUrl", u);
  url.searchParams.set("size", "32");
  return url.toString();
}

const img = document.createElement('img');
img.src = faviconURL("https://www.google.com") 
document.body.appendChild(img);
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

---

## file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/file-handlers

**Contents:**
- file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"file_handlers" 清单键用于指定 ChromeOS 扩展程序要处理的文件类型。如需处理文件，请使用 Web 平台的 Launch Handler API。如需了解特定于扩展程序的信息，请参阅文件处理。

**Examples:**

Example 1 (unknown):
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

## 处理远程托管代码违规行为 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/remote-hosted-code?hl=zh-cn

**Contents:**
- 处理远程托管代码违规行为 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 为什么不再接受 RHC 了？
- 我被告知我的扩展程序含有 RHC。这是怎么回事？
- 如何识别 RHC
- 如果库请求代码，该怎么办
- 等不及要更新库怎么办？
  - 审核代码
  - 摇树
  - 自动编辑文件
  - 手动修改文件

远程托管的代码 (RHC) 是 Chrome 应用商店中任何 由从 扩展程序自己的文件例如 JavaScript 和 WASM。它不包括 或 CSS 文件

对于 Manifest V3 扩展程序，现在需要捆绑其在内部使用的所有代码 扩展程序本身过去，您可以从 。

如果您的扩展程序在审核过程中因出现 Blue Argon 错误而被拒，则： 我们的审核人员认为您的扩展程序使用了远程托管代码。这是 这通常是由于扩展程序试图使用遥控器添加脚本标记而导致的 （即来自开放网络，而不是来自 扩展程序），或提取资源以直接执行。

当您知道要寻找什么后，发现 RHC 并不特别困难。首先， 检查字符串“http://”或“https://”。如果您有 那么就有可能找出违规情况。如果 拥有完整的构建系统，或者使用 npm 或其他第三方 请确保你搜索的是经过编译的代码， 因为商店会评估这些内容如果您仍然无法 那么下一步就是联系一站式支持团队。他们 能够概述具体的违规行为，以及获得 扩展程序。

无论代码来自何处，都不允许带有 RHC。这个 包含并非由您编写，但正好在测试中用作依赖项的代码 项目。使用 Firebase 的一些开发者在远程访问 代码已添加到 Firebase Authentication 中。尽管这是一个 第一方（即 Google 自有）库，RHC 除外。您需要 将代码配置为移除 RHC 或将您的目标更新为 添加起始代码如果您遇到不是您的代码的问题 但加载的是 RHC 库，但您使用的是一个库 联系库作者告诉他们您正在经历一些事情， 并要求我们提供解决方法或更新代码来将其移除。

有些库会在收到通知后立即发布更新， 或需要一些时间才能解决问题。根据什么 您可能不需要等待用户 即可取消屏蔽并顺利通过审核这里有许多 快速恢复运行

您是否确定需要发起请求的代码？如果可以 或者删除导致该错误的库，然后删除 这样工作就完成了

或者，是否有其他库可以提供相同功能？试试看 检查 npmjs.com、GitHub 或其他网站，了解其他满足 相同的应用场景

如果导致 RHC 违规的代码实际并未使用，则可能是 无法通过工具自动删除现代构建工具 webpack、Rollup 和 Vite（仅举几例）具有一项功能 称为摇树优化。在构建系统中启用后，Tree shaking 应移除所有未使用的代码路径。这可能意味着您不仅拥有 合规版的代码，同时又能打造出更精简、更快捷的版本！请务必注意 请注意，并非所有库都可以执行摇树优化，但许多库却能进行摇树优化。部分 Rollup 和 Vite 等工具默认启用摇树优化功能。Webpack 需要进行配置才能启用。如果您使用的不是 build 作为扩展程序的一部分，但使用了代码库， 强烈建议您考虑向工作流中添加构建工具。构建 可帮助您编写更安全、更可靠且更易于维护的项目。

具体如何实现摇树优化取决于您的具体项目。 举一个简单的例子，使用 Rollup 创建 编译项目代码。例如，如果您有一个只登录 Firebase Auth，名为 main.js：

然后，您只需告诉 Rollup 输入文件，所需的插件 加载节点文件 @rollup/plugin-node-resolve 以及输出的名称 文件。

在终端窗口中运行该命令后，你将收到生成的版本 main.js 文件，全部编译成一个名为 compiled.js 的单个文件。

汇总操作可能很简单，但也可以极大地配置。您可以添加所有种类 复杂的逻辑和配置，请查看相应文档。 添加这样的构建工具将使代码更小、更高效， 在本例中，我们修复了远程托管代码的问题

远程托管代码进入代码库的一种日益常见的方式是 作为您要包含的库的子依赖项。如果库X想要 import库Y，那么您仍然需要更新它， 而是从本地来源加载借助现代构建系统，你可以轻松 插件来提取远程引用，并将其直接内嵌到代码中。

使用新插件运行 build 后，每个远程 import 网址都会 无论它是我们的代码、一个子依赖项， 子依赖项或其他地方。

最简单的方法是删除引发 RHC 的代码。打开方式 选择文本编辑器，删除违规代码行。这通常是 不不建议采用，因为它脆弱，可能会被忘记。它使 有一个名为“library.min.js”的文件时，不是 实际上是 library.min.js。与修改原始文件相比 可维护的选项是使用 patch-package 等工具。这是一个超级 一种强大的选项，可让您将修改保存到文件，而不是 文件本身。它基于补丁文件构建而成 为 Git 或 Subversion 等版本控制系统提供支持。您只需要 您可以手动修改违规代码、保存差异文件 包含您要应用的更改的补丁软件包您可以阅读完整的教程 针对项目的自述文件。如果您正在修补项目，我们真的 建议您与项目联系，申请做出更改 上游。虽然补丁软件包可以大大简化补丁的管理， 那就没有什么比这更棒的了

随着代码库的增长，依赖项（或某个依赖项的依赖项） 可以保留不再使用的代码路径。如果上述任一版块 包含用于加载或执行 RHC 的代码，则必须移除此类代码。它 无论其已失效还是未使用都无关紧要。如果未使用，则应该 移除，具体方法是摇树，或者修补库以将其移除。

一般来说不会。不允许使用 RHC。然而，有少数 在允许的情况下使用。在这些情况下 是任何其他选项都无法实现的

用户脚本是一小段代码，通常由 user，适用于 TamperMonkey 和 Violentmonkey。这些管理器无法将 是由用户编写的，因此 User Script API 提供了执行代码的方式， 由用户提供这不能替代 chrome.scripting.executeScript 或其他代码执行环境。 用户必须启用开发者模式才能执行任何内容。如果 Chrome 网页版 商店评价团队认为这些信息以其他方式使用， （即用户提供的代码），则可能会被拒绝或 已从商店下架。

借助 chrome.debugger API，扩展程序能够 Chrome Devtools 协议。该协议与 Chrome 的开发者工具以及数量惊人的其他工具。有了它 可以请求和执行远程代码。与用户脚本一样， 可取代 chrome.scripting，并显著改善用户体验。 在使用它时，用户会在 窗口。如果关闭或关闭横幅，则调试会话将 已终止。

如果您需要将字符串评估为代码，并且位于 DOM 环境（例如 内容脚本，而不是扩展程序 Service Worker），那么另一个选项 那就是使用沙盒化 iframe。扩展程序不支持 默认为 eval()（出于安全考虑）。恶意代码可能会给用户安全 和安全性风险。但是，如果代码仅在已知的 比如与网络其余部分隔离的 iframe 那么这些风险就会大大降低在这种情况下，内容安全协议 阻止使用 eval 的政策可以解除，让您可以运行任何 有效的 JavaScript 代码。

如果您的用例未涵盖在内，请随时与我们的团队联系 使用 chromium-extensions 邮寄名单来获取反馈，或打开一个新的 用于向一站式支持团队寻求指导的工单

政策的执行可能会发生细微的差别，审核过程需要手动输入内容，这意味着 Chrome 应用商店团队有时可能会同意更改审核决定。如果 如果您认为审核过程中有误，可以对被拒提出申诉 使用一站式支持

**Examples:**

Example 1 (python):
```python
import { GoogleAuthProvider, initializeAuth } from "firebase/auth";

chrome.identity.getAuthToken({ 'interactive': true }, async (token) => {
  const credential = GoogleAuthProvider.credential(null, token);
  try {
    const app = initializeApp({ ... });
    const auth = initializeAuth(app, { popupRedirectResolver: undefined, persistence: indexDBLocalPersistence });
    const { user } = await auth.signInWithCredential(credential)
    console.log(user)
  } catch (e) {
    console.error(error);
  }
});
```

Example 2 (unknown):
```unknown
npx rollup --input main.js --plugin '@rollup/plugin-node-resolve' --file compiled.js
```

Example 3 (python):
```python
import moment from "https://unpkg.com/moment@2.29.4/moment.js"
console.log(moment())
```

Example 4 (python):
```python
import { existsSync } from 'fs';
import fetch from 'node-fetch';

export default {
  plugins: [{
    load: async function transform(id, options, outputOptions) {
      // this code runs over all of out javascript, so we check every import
      // to see if it resolves as a local file, if that fails, we grab it from
      // the network using fetch, and return the contents of that file directly inline
      if (!existsSync(id)) {
        const response = await fetch(id);
        const code = await response.text();

        return code
      }
      return null
    }
  }]
};
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
chrome.enterprise.networkingAttributes.getNetworkDetails(  callback?: function,): Promise<NetworkDetails>
```

Example 2 (javascript):
```javascript
(networkAddresses: NetworkDetails) => void
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

Example 2 (unknown):
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

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Click to run",
  "description": "Runs a script when the user clicks the action toolbar icon.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  "permissions": ["scripting", "activeTab"]
}
```

Example 4 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Popup extension that requests permissions",
  "description": "Extension that includes a popup and requests host permissions and storage permissions .",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "action": {
    "default_popup": "popup.html"
  },
  "host_permissions": [
    "https://*.example.com/"
  ],
  "permissions": [
    "storage"
  ]
}
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/publish-mv3?hl=zh-cn

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

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
{
  "name": "My externally connectable extension",
  "externally_connectable": {
    "ids": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      ...
    ],
    // If this field is not specified, no web pages can connect.
    "matches": [
      "https://*.google.com/*",
      "*://*.chromium.org/*",
      ...
    ],
    "accepts_tls_channel_id": false
  },
  ...
}
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

Example 3 (unknown):
```unknown
<script src="_modules/cccccccccccccccccccccccccccccccc/foo.js">
```

Example 4 (unknown):
```unknown
chrome-extension://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/_modules/cccccccccccccccccccccccccccccccc/
```

---

## 界面组件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/user_interface?hl=zh-cn

**Contents:**
- 界面组件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 操作
- 操作图标
- 徽章
- 命令
- 上下文菜单
- 多功能框
- 替换页面
- 弹出式窗口
- 侧板

此目录列出了扩展程序中可用的界面元素。每个条目都包含：

这些元素是调用扩展功能的不同方式。您无需实现所有这些功能。事实上，某些使用情形可能根本不会使用任何一种。例如，链接缩短器可以使用键盘快捷键对显示的网址执行操作，并以编程方式将缩短的链接放入剪贴板。

操作是指用户点击扩展程序的操作图标时发生的情况。操作可以使用 Action API 调用扩展功能，也可以打开一个弹出式窗口，让用户调用多项扩展功能。使用提示告知用户相应操作的作用。

如需了解如何构建操作，请参阅实现操作，或查看操作示例。

扩展程序需要至少一个图标来表示。用户点击该图标即可调用操作，无论该操作是使用 Action API 调用扩展程序功能，还是打开弹出式窗口。

您还可以向图标添加标签（此处称为“徽章”），以传达扩展程序状态或用户需要执行操作等信息。

如需了解如何构建操作，请参阅实现操作，或查看操作示例。

徽章是放置在操作图标顶部的格式化文本，用于指示扩展程序状态或用户需要执行的操作等。您可以通过调用 chrome.action.setBadgeText() 设置徽章的文字，并通过调用 chrome.action.setBadgeBackgroundColor() 设置横幅颜色。

如需了解如何构建操作，请参阅实现操作或喝水示例。

命令是用于调用扩展程序功能的按键组合。在 manifest.json 文件中定义按键组合，并使用 Commands API 对其做出响应。如需了解如何实现命令，请参阅 API 参考或 chrome.commands 示例。

显示鼠标的替代点击（通常称为右键点击）的上下文菜单。使用 Context Menus API 定义上下文菜单。

如需了解如何实现上下文菜单，请参阅上下文菜单示例。

您可以使用 Chrome 多功能框与用户互动。当用户在地址栏中输入扩展程序定义的关键字时，您的扩展程序会控制用户在地址栏中看到的内容。在 manifest.json 中定义关键字，并使用 Omnibox API 对这些关键字做出响应。

如需了解如何替换多功能框，请参阅“从多功能框触发操作”或快速 API 参考示例。

扩展程序可以替换以下某个 Chrome 内置网页：

如需了解如何替换 Chrome 网页，请参阅替换 Chrome 网页或替换示例。

弹出式窗口是一种操作，可显示一个窗口，让用户调用多项扩展功能。如果用户点击操作图标、使用键盘快捷键或调用 chrome.action.openPopup()，则可以打开弹出式窗口。

如需了解如何构建弹出式窗口，请参阅添加弹出式窗口。您还可以通过某个操作示例下载某个步骤。

借助侧边栏，用户可以在网页旁边调用扩展程序功能（请参见图片）。侧边栏可以附加到单个标签页或整个窗口。侧边栏使用 Side Panel API 进行控制。

如需了解如何构建侧边栏，请参阅侧边栏使用情形，或查看侧边栏示例。

借助提示，您可以在用户将鼠标悬停在扩展程序的操作图标上时，显示扩展程序的操作。默认情况下，提示会显示扩展程序的名称。

如需了解如何添加提示，请使用清单文件的 "action" 键的 "default_title" 成员。

您可以使用 DevTools 面板 API 向 DevTools 添加自定义面板（在 DevTools 中称为标签页）。其他开发者工具 API 可让您监控窗口和网络流量。您还可以自定义开发者工具的记录器面板。Chrome 开发者工具自带的 Lighthouse 面板最初是一个开发者工具扩展程序。

使用扩展程序 Notifications API 或 Web 平台 Notifications API 将消息发布到用户的系统托盘。

主题背景是一种特殊类型的扩展程序，可更改浏览器的外观。主题的打包方式与常规扩展程序类似，但不包含 JavaScript 或 HTML 代码。

如需了解如何构建主题，请参阅什么是主题？。

本部分介绍了扩展程序与用户互动的其他方式。虽然对于基本扩展服务来说并非绝对必要，但它们可能是扩展服务的重要组成部分。对于许多用户来说，这些功能对于使用扩展程序至关重要。

对于许多用户来说，无障碍功能实际上就是用户界面，而其功能通常对那些并非主要通过无障碍功能与扩展程序互动的用户也很有用。了解使扩展程序易于访问的基础知识。

用用户自己的语言与他们交流。了解如何实现界面国际化。

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

---

## chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/management

**Contents:**
- chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ExtensionDisabledReason
    - 枚举
  - ExtensionInfo
    - 属性
  - ExtensionInstallType
    - 枚举

chrome.management API 提供了管理安装式应用和扩展程序的方式。

必须在扩展程序清单中声明“管理”权限，才能使用 Management API。例如：

management.getPermissionWarningsByManifest()、management.uninstallSelf() 和 management.getSelf() 不需要管理权限。

"permissions_increase"

与已安装的扩展程序、应用或主题相关的信息。

ExtensionDisabledReason 可选

图标信息列表。请注意，这仅反映清单中声明的内容，实际图片尺寸可能与声明不符，建议在引用这些图像的 img 标签中显式指定宽度和高度属性。详见图标清单文档。

请使用 management.ExtensionInfo.type。

用户是否可以启用此扩展程序。仅对未启用的扩展程序返回此值。

扩展程序、应用或主题是否声明支持离线功能。

扩展程序、应用或主题的版本名称（如清单中已指定）。

扩展程序的安装方式。可能值包括 admin：因管理政策而安装； development：在开发者模式下以解压方式加载； normal：通过 .crx 文件正常安装； sideload：由机器上的其他软件安装； other：通过其他方式安装。

"legacy_packaged_app"

"login_screen_extension"

表示图标宽度和高度的数字。可能的值包括（但不限于）128、48、24 和 16。

图标图像的网址。如需显示图标的灰度版本（例如，指示扩展程序已禁用），可在网之后附加 ?grayscale=true。

"OPEN_AS_REGULAR_TAB"

是否应提示用户显示确认卸载对话框。自行卸载时，默认值为 false。如果扩展程序卸载其他扩展程序，系统会忽略此参数，并始终显示对话框。

显示为应用创建快捷方式的选项。在 Mac 上仅支持为打包应用创建。

应为 management.ExtensionInfo 应用项中的 ID。

网页的网址。网址的架构只能为“http”或“https”。

Promise<ExtensionInfo>

返回有关具有指定 ID 的已安装扩展程序、应用或主题的信息。

management.ExtensionInfo 项目的 ID。

Promise<ExtensionInfo>

返回有关已安装的扩展程序和应用的信息列表。

Promise<ExtensionInfo[]>

返回给定扩展程序清单字符串的权限警告列表。注意：使用此函数时，无需在清单中请求“管理”权限。

返回有关调用扩展程序、应用或主题的信息。注意：使用此函数时，无需在清单中请求“管理”权限。

Promise<ExtensionInfo>

启动清单中指定的 replacement_web_app。若未安装，提示用户安装。

启用或停用应用或扩展程序。在大多数情况下，此函数必须在用户手势（如按钮的 onclick 处理程序）上下文中调用，并且可能会向用户展示原生确认界面以防止滥用。

此值应为 management.ExtensionInfo 中某个项目的 ID。

应为 management.ExtensionInfo 应用项中的 ID。

目标启动类型。请务必检查并确保此启动类型位于 ExtensionInfo.availableLaunchTypes 中，因为可用的启动类型因平台和配置而异。

卸载当前安装式应用或扩展程序。注意：在用户未被授权卸载指定扩展程序/应用的受管理环境中，此功能将无法执行。若卸载失败（如用户取消对话框），系统将拒绝 promise 或回调将被调用，同时设置 runtime.lastError。

此值应为 management.ExtensionInfo 中某个项目的 ID。

卸载调用扩展程序。注意：使用此函数时，无需在清单中请求“管理”权限。但若用户无法卸载指定的扩展程序/应用，此函数在受管理环境中将无法执行。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "management"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.management.createAppShortcut(  id: string,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.management.generateAppForLink(  url: string,  title: string,): Promise<ExtensionInfo>
```

Example 4 (unknown):
```unknown
chrome.management.get(  id: string,): Promise<ExtensionInfo>
```

---

## 在沙盒化 iframe 中使用 eval() 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/sandboxingEval?hl=zh-cn

**Contents:**
- 在沙盒化 iframe 中使用 eval() 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 为什么要使用沙盒？
- 创建和使用沙盒
  - 列出清单中的文件
  - 加载沙盒文件
  - 执行危险操作
  - 传回结果

Chrome 的扩展程序系统会强制执行相当严格的默认内容安全政策 (CSP)。 政策限制非常简单：脚本必须移出线，放入单独的 JavaScript 文件中，内嵌事件处理脚本必须转换为使用 addEventListener，并且 eval() 处于停用状态。

不过，我们也了解到，许多库都使用 eval() 和 eval 类构造（例如 new Function()）来优化性能和简化表达。模板库特别容易出现这种实现方式。虽然某些环境（如 Angular.js）支持 CSP out 许多热门框架尚未更新为与 Android Studio 兼容的 扩展程序的少了 eval 的世界。因此，我们发现移除对该功能的支持对开发者而言造成的问题比预期多。

本文档介绍了沙盒作为一种安全机制，可让您在项目中添加这些库，而不会影响安全性。

在扩展程序中使用 eval 是危险的，因为它执行的代码可以访问扩展程序的高权限环境中的所有内容。提供了大量功能强大的 chrome.* API， 严重影响用户的安全和隐私；我们最担心的是简单的数据渗漏问题。 提供的解决方案是一个沙盒，在此沙盒中，eval 无需访问 或扩展程序的高价值 API。没有数据、不使用 API，也没有关系。

为此，我们会将扩展程序软件包内的特定 HTML 文件列为已沙盒化。 每当有沙盒机制加载网页时，系统都会将其移动到唯一来源，并会被拒绝 对 chrome.* API 的访问权限。如果通过 iframe 将此沙盒化页面加载到扩展程序中， 然后向其传递消息，让其以某种方式处理这些消息，然后等待它为我们传回 结果。通过这种简单的消息传递机制，我们可以安全地在扩展程序的工作流中包含 eval 驱动的代码。

如果您希望直接查看代码，请下载沙盒示例扩展程序 关闭。这是一个基于 Handlebars 构建的小型消息传递 API 的有效示例 模板库，它应该会为您提供开始操作所需的一切。对于希望了解更多说明的用户，我们来一起详细了解一下该示例。

应该在沙盒中运行的每个文件都必须在扩展程序清单中列出，方法是添加 sandbox 属性。这是非常重要的一步，而且很容易被忘记，因此请仔细检查 您的沙盒文件会在清单中列出在此示例中，我们将对名为“sandbox.html”的文件进行沙盒化处理。清单条目如下所示：

为了对沙盒化文件执行一些有趣的操作，我们需要在 可以通过该扩展程序的代码进行处理在这里，sandbox.html 已通过 iframe 加载到扩展程序页面中。网页的 JavaScript 文件包含以下代码：每当用户点击浏览器操作时，该代码都会通过查找网页上的 iframe 并对其 contentWindow 调用 postMessage()，将消息发送到沙盒。消息是一个包含以下三个属性的对象：context、templateName 和 command。我们稍后会深入探讨 context 和 command。

加载 sandbox.html 后，它会加载 Handlebars 库，创建并编译内嵌的 这就像 Handlebars 建议那样：

不会失败！即使 Handlebars.compile 最终使用了 new Function，但一切都按预期运行，最终在 templates['hello'] 中生成了编译后的模板。

我们将设置一个消息监听器来接受来自扩展程序页面的命令，以便使用此模板。我们将使用传入的 command 来确定应执行的操作（您可以 想想不仅仅进行渲染创建模板？或许以某种方式管理它们？），并且 context 将直接传递到模板进行渲染。呈现的 HTML 将传回给扩展程序页面，以便扩展程序稍后可以对其执行一些有用操作：

返回到扩展程序页面，我们会收到此消息，并使用 html 执行一些有趣的操作 传递的数据。在本例中，我们只会通过通知来回显它，但完全可以将此 HTML 安全地用作扩展程序界面的一部分。通过 innerHTML 插入它不会构成重大安全风险，因为我们信任在沙盒中呈现的内容。

这种机制使模板化变得简单，但它当然不仅限于模板化。在严格的内容安全政策下，任何无法直接运行的代码都可以放入沙盒中；事实上，将扩展程序中会正确运行的组件放入沙盒中通常很有用，这样可以将程序的每个部分限制为仅拥有执行所需的最少特权集。2012 年 Google I/O 大会上的 Writing Secure Web Apps and Chrome Extensions 演示提供了一些很好的示例，展示了这些技术的实际运用，值得您花 56 分钟的时间观看。

**Examples:**

Example 1 (unknown):
```unknown
{
  ...,
  "sandbox": {
     "pages": ["sandbox.html"]
  },
  ...
}
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener(() => {
  chrome.tabs.create({
    url: 'mainpage.html'
  });
  console.log('Opened a tab with a sandboxed page!');
});
```

Example 3 (javascript):
```javascript
let counter = 0;
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('reset').addEventListener('click', function () {
    counter = 0;
    document.querySelector('#result').innerHTML = '';
  });

  document.getElementById('sendMessage').addEventListener('click', function () {
    counter++;
    let message = {
      command: 'render',
      templateName: 'sample-template-' + counter,
      context: { counter: counter }
    };
    document.getElementById('theFrame').contentWindow.postMessage(message, '*');
  });
```

Example 4 (unknown):
```unknown
<!DOCTYPE html>
<html>
  <head>
    <script src="mainpage.js"></script>
    <link href="styles/main.css" rel="stylesheet" />
  </head>
  <body>
    <div id="buttons">
      <button id="sendMessage">Click me</button>
      <button id="reset">Reset counter</button>
    </div>

    <div id="result"></div>

    <iframe id="theFrame" src="sandbox.html" style="display: none"></iframe>
  </body>
</html>
```

---

## 消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/messaging?hl=zh-cn

**Contents:**
- 消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 一次性请求
  - 响应
- 长期连接
- 序列化
  - 端口生命周期
- 跨扩展程序消息传递
- 从网页发送消息
- 原生消息传递
- 安全注意事项

借助消息传递 API，您可以在与扩展程序关联的上下文中运行的不同脚本之间进行通信。这包括服务工作线程、chrome-extension://页面和内容脚本之间的通信。例如，RSS 阅读器扩展程序可以使用内容脚本来检测网页上是否存在 RSS Feed，然后通知服务工作线程更新相应网页的操作图标。

有两种消息传递 API：一种用于一次性请求，另一种更复杂，用于长期连接，可发送多条消息。

如需了解如何在扩展程序之间发送消息，请参阅跨扩展程序消息部分。

如需向扩展程序的另一部分发送单条消息，并选择性地获取响应，请调用 runtime.sendMessage() 或 tabs.sendMessage()。借助这些方法，您可以从内容脚本向扩展程序发送一次性 JSON 可序列化消息，也可以从扩展程序向内容脚本发送一次性 JSON 可序列化消息。这两个 API 都会返回一个 Promise，该 Promise 会解析为收件人提供的响应。

如需监听消息，请使用 chrome.runtime.onMessage 事件：

当调用事件监听器时，系统会传递一个 sendResponse 函数作为第三个参数。这是一个可调用的函数，用于提供响应。默认情况下，必须同步调用 sendResponse 回调。如果您想执行异步工作来获取传递给 sendResponse 的值，则必须从事件监听器返回字面值 true（而不仅仅是真值）。这样做会使消息通道对另一端保持开放状态，直到调用 sendResponse。

如果您在不带任何参数的情况下调用 sendResponse，系统会发送 null 作为响应。

如果多个网页都在监听 onMessage 事件，则只有第一个针对特定事件调用 sendResponse() 的网页才能成功发送响应。系统会忽略对该活动的所有其他回复。

如需创建可重复使用的长期消息传递渠道，请调用：

您可以通过传递带有 name 键的 options 参数来命名频道，以区分不同类型的连接：

长效连接的一个潜在用例是自动表单填充扩展程序。内容脚本可能会为特定登录会话打开与扩展程序页面的通道，并为页面上的每个输入元素向扩展程序发送消息，以请求要填充的表单数据。共享连接允许扩展程序在扩展程序组件之间共享状态。

建立连接时，系统会为每个端点分配一个 runtime.Port 对象，用于通过该连接发送和接收消息。

使用以下代码从内容脚本打开渠道，并发送和监听消息：

如需从扩展程序向内容脚本发送请求，请将上例中对 runtime.connect() 的调用替换为 tabs.connect()。

如需处理内容脚本或扩展程序网页的传入连接，请设置 runtime.onConnect 事件监听器。当扩展程序的其他部分调用 connect() 时，它会激活此事件和 runtime.Port 对象。用于响应传入连接的代码如下所示：

在 Chrome 中，消息传递 API 使用 JSON 序列化。这意味着，消息（以及收件人提供的回复）可以包含任何有效的 JSON 值（null、布尔值、数字、字符串、数组或对象）。其他值将被强制转换为可序列化的值。

值得注意的是，这与其他使用结构化克隆算法实现相同 API 的浏览器不同。

端口旨在作为扩展程序不同部分之间的双向通信机制。当扩展程序的一部分调用 tabs.connect()、runtime.connect() 或 runtime.connectNative() 时，它会创建一个 Port，该 Port 可以立即使用 postMessage() 发送消息。

如果某个标签页中有多个框架，则调用 tabs.connect() 会针对该标签页中的每个框架调用一次 runtime.onConnect 事件。同样，如果调用 runtime.connect()，则 onConnect 事件可以在扩展程序进程中的每个帧触发一次。

您可能需要了解连接何时关闭，例如，如果您要为每个打开的端口维护单独的状态。为此，请监听 runtime.Port.onDisconnect 事件。当渠道另一端没有有效端口时，系统会触发此事件，这可能是由以下任何原因造成的：

除了在扩展程序的不同组件之间发送消息之外，您还可以使用 Messaging API 与其他扩展程序进行通信。这样一来，您就可以公开一个 API，供其他扩展程序使用。

如需侦听来自其他扩展程序的传入请求和连接，请使用 runtime.onMessageExternal 或 runtime.onConnectExternal 方法。以下是每种类型的示例：

如需向其他扩展程序发送消息，请传递要与之通信的扩展程序的 ID，如下所示：

扩展程序还可以接收和回复来自网页的消息。如需从网页向扩展程序发送消息，请在 manifest.json 中使用 "externally_connectable" 清单键指定您要允许哪些网站发送消息。例如：

这会将消息传递 API 公开给与您指定的网址模式匹配的任何网页。网址模式必须至少包含一个二级网域；也就是说，不支持“*”“*.com”“*.co.uk”和“*.appspot.com”等主机名模式。您可以使用 <all_urls> 访问所有网域。

使用 runtime.sendMessage() 或 runtime.connect() API 向特定扩展程序发送消息。例如：

在扩展程序中，使用 runtime.onMessageExternal 或 runtime.onConnectExternal API 监听来自网页的消息，如跨扩展程序的消息传递中所述。示例如下：

扩展程序可以与注册为原生消息传递主机的原生应用交换消息。如需详细了解此功能，请参阅原生消息传递。

与扩展程序服务工作线程相比，内容脚本的可信度较低。例如，恶意网页可能能够入侵运行内容脚本的渲染进程。假设来自内容脚本的消息可能由攻击者精心制作，并确保验证和清理所有输入。假设发送到内容脚本的任何数据都可能会泄露到网页。 限制可由从内容脚本接收的消息触发的特权操作的范围。

请务必保护您的脚本免受跨站脚本攻击。从不可信的来源（例如用户输入、通过内容脚本访问的其他网站或 API）接收数据时，请注意避免将这些数据解读为 HTML 或以可能导致意外代码运行的方式使用这些数据。

避免使用以下会使扩展程序容易受到攻击的方法：

**Examples:**

Example 1 (javascript):
```javascript
(async () => {
  const response = await chrome.runtime.sendMessage({greeting: "hello"});
  // do something with response here, not outside the function
  console.log(response);
})();
```

Example 2 (javascript):
```javascript
// Event listener
function handleMessages(message, sender, sendResponse) {
  fetch(message.url)
    .then((response) => sendResponse({statusCode: response.status}))

  // Since `fetch` is asynchronous, must return an explicit `true`
  return true;
}

chrome.runtime.onMessage.addListener(handleMessages);

// From the sender's context...
const {statusCode} = await chrome.runtime.sendMessage({
  url: 'https://example.com'
});
```

Example 3 (javascript):
```javascript
const port = chrome.runtime.connect({name: "example"});
```

Example 4 (javascript):
```javascript
const port = chrome.runtime.connect({name: "knockknock"});
port.onMessage.addListener(function(msg) {
  if (msg.question === "Who's there?") {
    port.postMessage({answer: "Madame"});
  } else if (msg.question === "Madame who?") {
    port.postMessage({answer: "Madame... Bovary"});
  }
});
port.postMessage({joke: "Knock knock"});
```

---

## 对 Chrome 扩展程序进行单元测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/unit-testing?hl=zh-cn

**Contents:**
- 对 Chrome 扩展程序进行单元测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 示例：通过 Jest 使用模拟
- 后续步骤

通过单元测试，您可以独立于其余部分对小段代码进行测试 以及浏览器之外。例如，您可以编写单元测试 辅助方法正确地将值写入存储空间。

可以使用如下框架照常测试未使用扩展 API 编写的代码： Jest。为了让代码更易于以这种方式进行测试，不妨考虑使用 依赖项注入：有助于消除对 Chrome 的依赖 命名空间中。

如果您需要测试包含扩展程序 API 的代码，请考虑使用模拟对象。

创建一个 jest.config.js 文件，用于声明将在所有测试之前运行的设置文件：

在 mock-extension-apis.js 中，为您要调用的特定函数添加实现：

mock-extension-apis.js:

然后，使用 jest.spy 在测试中模拟返回值：

为确保您的扩展程序能按预期运行，我们建议您添加端到端测试。如需查看完整的教程，请参阅使用 Puppeteer 测试 Chrome 扩展程序。

**Examples:**

Example 1 (unknown):
```unknown
module.exports = {
  setupFiles: ['<rootDir>/mock-extension-apis.js']
};
```

Example 2 (javascript):
```javascript
global.chrome = {
  tabs: {
    query: async () => { throw new Error("Unimplemented.") };
  }
};
```

Example 3 (javascript):
```javascript
test("getActiveTabId returns active tab ID", async () => {
  jest.spyOn(chrome.tabs, "query").mockResolvedValue([{
    id: 3,
    active: true,
    currentWindow: true
  }]);
  expect(await getActiveTabId()).toBe(3);
});
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

---

## Chrome 扩展程序的更新生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/extensions-update-lifecycle?hl=zh-cn

**Contents:**
- Chrome 扩展程序的更新生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 标准更新周期
- 监控扩展程序更新分发
- 手动更新扩展程序
- 检查扩展程序是否有更新
  - 按需检查更新
  - 监听可用更新
- 通过企业政策控制更新
  - 强制安装
  - 固定扩展程序版本

本指南详细介绍了完整的扩展程序更新流程，涵盖标准更新流程、手动替换、开发者 API 以及企业政策的重大影响。

Chrome 旨在自动将已安装的扩展程序更新到最新版本，确保用户能够使用新功能和安全修复程序。默认情况下，Chrome 会在启动时以及每隔几个小时检查一次扩展程序更新。

更新过程的一个关键方面是，只有当扩展程序被视为空闲时，才会安装更新。扩展程序要处于空闲状态，其组件不得处于活跃使用状态。在 Manifest V3 的上下文中，这主要意味着扩展程序的 Service Worker 未运行。Service Worker 采用事件驱动型设计，在一段时间不活动后会终止。此外，任何打开的扩展程序页面（例如侧边栏、弹出式窗口或选项页面）都会阻止扩展程序被视为处于空闲状态。有效的内容脚本不会影响扩展程序是否被视为处于空闲状态。

此闲置要求可能会导致频繁处于活动状态的扩展程序更新延迟。如果扩展程序的服务工作线程不断被事件触发，则可能永远无法达到空闲状态，并且更新会延迟到浏览器重启后进行。

如需了解有多少用户使用的是扩展程序的最新版本，请使用 Chrome 应用商店分析信息中心。前往 Chrome 应用商店开发者信息中心，然后选择您已发布的一款扩展程序。在侧边导航栏中，依次前往分析 -> 用户，然后向下滚动到按商品划分的每日用户数图表。您可以在此处查看有多少用户已在使用最新版本。

如果用户希望立即收到最新更新，Chrome 提供了一种手动更新机制。在测试更新时，这也是一个有用的工具。

个人用户可以按照以下步骤强制更新所有已安装的扩展程序：

此操作会促使 Chrome 立即从 Chrome 应用商店中提取所有已安装扩展程序的最新版本。

chrome.runtime API 为扩展程序提供了与更新机制互动的工具。

扩展程序可以使用 chrome.runtime.requestUpdateCheck() 函数以编程方式启动更新检查。对于严重依赖于后端服务且需要确保运行最新兼容版本的扩展程序，此功能尤其有用。

调用此函数时，Chrome 会向 Chrome 应用商店查询新版本，并在有新版本可用时下载该版本。该函数的回调会接收一个状态，指示检查结果。

当更新已下载并准备好安装时，系统会触发 chrome.runtime.onUpdateAvailable 事件。此事件会在其详细信息中提供新版本号。通过监听此事件，扩展程序可以确定有更新可用，并考虑在适当的时候进入空闲状态或使用 chrome.runtime.reload() 导致重新加载。

在特殊情况下，可以使用 chrome.runtime.requestUpdateCheck() 强制浏览器检查扩展程序更新：

请务必注意，频繁调用 requestUpdateCheck() 会受到浏览器的限制。仅在您知道有更新可用时才使用此函数。例如，当更新后的后端需要较新版本的扩展程序时。

在受管理的企业环境中，标准扩展程序更新流程受系统管理员设置的政策的约束。这些政策可以替换默认行为，以强制执行安全性和稳定性。

借助 ExtensionInstallForcelist 政策，管理员可以为用户静默安装特定扩展程序。用户无法停用或卸载通过此政策安装的扩展程序。

不过，企业通常需要控制所用扩展程序的具体版本，以确保与其他软件的兼容性。为此，管理员可以将扩展程序“固定”到特定版本。此操作通过 Google 管理控制台完成，管理员可以在其中为组织部门选择所需的版本。扩展程序固定后，Chrome 将不会将其更新到高于指定版本的版本。

出于安全或自定义方面的原因，企业可以托管自己的扩展程序分叉版本。为此，请使用 ExtensionSettings 政策，并将 override_update_url 属性设置为 true。o此政策会强制 Chrome 从指定网址（而非 Chrome 应用商店）提取扩展程序及其更新。

您可以在扩展程序的清单文件中指定 minimum_chrome_version。这样可确保扩展程序仅安装在支持其所用 API 的 Chrome 版本上。

对于新安装，Chrome 应用商店会阻止使用旧版 Chrome 的用户安装该扩展程序，并显示“不兼容”消息。对于现有用户，如果扩展程序的更新将 minimum_chrome_version 提高到高于用户已安装的 Chrome 版本，他们将静默停止接收该扩展程序的更新。开发者应注意这一点，并告知用户群中可能受到影响的很大一部分用户。

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
{
  "name": "Page Redder",
  "version": "2.0",
  "permissions": [
    "activeTab",
    "scripting"
  ],
  "background": {
    "service_worker": "service-worker.js"
  },
  "action": {
    "default_title": "Make this page red"
  },
  "manifest_version": 3
}
```

Example 2 (javascript):
```javascript
function reddenPage() {
  document.body.style.backgroundColor = 'red';
}

chrome.action.onClicked.addListener((tab) => {
  if (!tab.url.includes('chrome://')) {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: reddenPage
    });
  }
});
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

---

## 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions-list?hl=zh-cn

**Contents:**
- 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如需访问大多数扩展程序 API 和功能，您必须在扩展程序的清单中声明权限。某些权限会触发警告，用户必须允许才能继续使用扩展程序。

如需详细了解权限的运作方式，请参阅声明权限。如需了解有关在有警告的情况下使用权限的最佳实践，请参阅权限警告指南。

以下列出了所有可用权限以及特定权限触发的所有警告。

---

## chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/dns

**Contents:**
- chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
  - 用法
- 类型
  - ResolveCallbackResolveInfo
    - 属性
- 方法

使用 chrome.dns API 进行 DNS 解析。

如需使用此 API，您必须在清单中声明 "dns" 权限。

以下代码调用 resolve() 以检索 example.com 的 IP 地址。

表示 IP 地址字面值的字符串。仅当 resultCode 指示成功时才提供。

ResolveCallbackResolveInfo

Promise<ResolveCallbackResolveInfo>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "dns"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
const resolveDNS = async () => {
    let record = await chrome.dns.resolve('example.com');
    console.log(record.address); // "192.0.2.172"
};

resolveDNS();
```

Example 3 (unknown):
```unknown
chrome.dns.resolve(  hostname: string,  callback?: function,): Promise<ResolveCallbackResolveInfo>
```

Example 4 (javascript):
```javascript
(resolveInfo: ResolveCallbackResolveInfo) => void
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

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/getstarted?hl=zh-cn

**Contents:**
  - 开始使用
- 概览
  - 什么是扩展程序？
  - 它们是如何构建的？
  - 他们可以做些什么？
- 扩展程序术语
  - 清单
  - Service Worker
  - 内容脚本
  - 工具栏操作

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
<script src="./react-dom.production.min.js"></script>
<link href="./bootstrap.min.css" rel="stylesheet">
```

Example 2 (unknown):
```unknown
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['jquery-min.js', 'content-script.js']
});
```

Example 3 (javascript):
```javascript
let name = 'World!';
chrome.tabs.executeScript({
  code: `alert('Hello, ${name}!')`
});
```

Example 4 (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

function showAlert(givenName) {
  alert(`Hello, ${givenName}`);
}

let name = 'World';
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  func: showAlert,
  args: [name],
});
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

Example 2 (unknown):
```unknown
<html>
  <body>
    <h1>Hello Extensions</h1>
  </body>
</html>
```

Example 3 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Hello Extensions of the world!",
  ...
}
```

Example 4 (unknown):
```unknown
<html>
  <body>
    <h1>Hello Extensions</h1>
    <script src="popup.js"></script>
  </body>
</html>
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
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  "type": "object",

  // "properties" maps an optional key of this object to its schema. At the
  // top-level object, these keys are the policy names supported.
  "properties": {

    // The policy name "AutoSave" is mapped to its schema, which in this case
    // declares it as a simple boolean value.
    // "title" and "description" are optional and are used to show a
    // user-friendly name and documentation to the administrator.
    "AutoSave": {
      "title": "Automatically save changes.",
      "description": "If set to true then changes will be automatically saved.",
      "type": "boolean"
    },

    // Other simple types supported include "integer", "string" and "number".
    "PollRefreshRate": {
      "type": "integer"
    },

    "DefaultServiceUrl": {
      "type": "string"
    },

    // "array" is a list of items that conform to another schema, described
    // in "items". An example to this schema is [ "one", "two" ].
    "ServiceUrls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    // A more complex example that describes a list of bookmarks. Each bookmark
    // has a "title", and can have a "url" or a list of "children" bookmarks.
    // The "id" attribute is used to name a schema, and other schemas can reuse
    // it using the "$ref" attribute.
    "Bookmarks": {
      "type": "array",
      "id": "ListOfBookmarks",
      "items": {
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "url": { "type": "string" },
          "children": { "$ref": "ListOfBookmarks" }
        }
      }
    },

    // An "object" can have known properties listed as "properties", and can
    // optionally have "additionalProperties" indicating a schema to apply to
    // keys that aren't found in "properties".
    // This example policy could map a URL to its settings. An example value:
    // {
    //   "youtube.com": {
    //     "blocklisted": true
    //   },
    //   "google.com": {
    //     "bypass_proxy": true
    //   }
    // }
    "SettingsForUrls": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "blocklisted": { "type": "boolean" },
          "bypass_proxy": { "type": "boolean" }
        }
      }
    }
  }
}
```

---

## 使用地理定位 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/geolocation

**Contents:**
- 使用地理定位 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在 MV3 扩展中使用地理定位
  - 在 Service Worker 中使用地理定位
  - 在弹出式窗口或侧边栏中使用地理定位
  - 在内容脚本中使用地理定位

如果您想在 Chrome 扩展程序中获取地理定位信息，请使用任何网站通常使用的 navigator.geolocation Web 平台 API。本文之所以存在，是因为 Chrome 扩展程序处理敏感数据访问权限的方式与处理网站权限的方式不同。地理定位是非常敏感的数据，因此浏览器需要确保用户完全了解并控制共享其确切位置的时间和位置。

在 Web 上，浏览器可以保护用户地理定位数据。同一权限模型并不总是适合扩展程序。

权限不是唯一的区别。如上所述，navigator.geolocation 是一个 DOM API，亦即构成网站的 API 的一部分。因此，它无法在 Worker 上下文中访问，例如作为 Manifest V3 扩展程序的支柱的“Extension Service Worker”。不过，您完全可以使用 geolocation。但只是使用方式和使用位置略有不同。

Service Worker 内部没有 navigator 对象。它只能在有权访问页面 document 对象的上下文中使用。如需在 Service Worker 内部获取访问权限，请使用 Offscreen Document，它可提供对可与扩展程序捆绑的 HTML 文件的访问权限。

首先，将 "offscreen" 添加到清单的 "permissions" 部分。

添加 "offscreen" 权限后，请向包含屏幕外文档的扩展程序添加一个 HTML 文件。此案例没有使用网页上的任何内容，因此该文件可能是几乎空白的文件。它只需是一个在您的脚本中加载的 HTML 小文件。

将此文件在项目的根目录中保存为 offscreen.html。

如前所述，您需要一个名为 offscreen.js 的脚本。您还需要将它与您的扩展程序绑定。它将是 Service Worker 的地理定位信息来源。您可以在它与 Service Worker 之间传递消息。

设置完成后，您就可以在 Service Worker 中访问 Offscreen Document 了。

请注意，当您访问屏幕外文档时，需要添加 reason。geolocation 原因最初不可用，因此请指定 DOM_SCRAPING 的回退，并在 justification 部分中说明代码的实际用途。Chrome 应用商店的审核流程会使用这些信息，以确保屏幕外的文档被用于有效用途。

一旦您引用了屏幕外文档，就可以向其发送消息，要求它为您提供更新后的地理定位信息。

因此，现在每当您想要从 Service Worker 获取地理定位时，只需调用：

在弹出式窗口或侧边栏中使用地理定位非常简单。弹出式窗口和侧边栏只是网络文档，因此可以访问常规 DOM API。您可以直接访问 navigator.geolocation。与标准网站的唯一区别在于，您需要使用 manifest.json "permission" 字段来请求 "geolocation" 权限。如果您不添加此权限，您将仍然拥有“navigator.geolocation”的访问权限。但是，任何试图使用它将导致立即的错误，就像用户拒绝了请求一样。您可以在弹出式窗口示例中查看相关信息。

与弹出式窗口一样，内容脚本也具有 DOM API 的完整访问权限；不过，用户将需要执行常规的用户权限流程。也就是说，将 "geolocation" 添加到您的 "permissions" 将不会自动授予您对用户的访问权限地理定位信息。如需查看相关信息，请参阅内容脚本示例。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
    ...
  "permissions": [
    ...
   "offscreen"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
<!doctype html>
<title>offscreenDocument</title>
<script src="offscreen.js"></script>
```

Example 3 (javascript):
```javascript
chrome.runtime.onMessage.addListener(handleMessages);
function handleMessages(message, sender, sendResponse) {
  // Return early if this message isn't meant for the offscreen document.
  if (message.target !== 'offscreen') {
    return;
  }

  if (message.type !== 'get-geolocation') {
    console.warn(`Unexpected message type received: '${message.type}'.`);
    return;
  }

  // You can directly respond to the message from the service worker with the
  // provided `sendResponse()` callback. But in order to be able to send an async
  // response, you need to explicitly return `true` in the onMessage handler
  // As a result, you can't use async/await here. You'd implicitly return a Promise.
  getLocation().then((loc) => sendResponse(loc));

  return true;
}

// getCurrentPosition() returns a prototype-based object, so the properties
// end up being stripped off when sent to the service worker. To get
// around this, create a deep clone.
function clone(obj) {
  const copy = {};
  // Return the value of any non true object (typeof(null) is "object") directly.
  // null will throw an error if you try to for/in it. Just return
  // the value early.
  if (obj === null || !(obj instanceof Object)) {
    return obj;
  } else {
    for (const p in obj) {
      copy[p] = clone(obj[p]);
    }
  }
  return copy;
}

async function getLocation() {
  // Use a raw Promise here so you can pass `resolve` and `reject` into the
  // callbacks for getCurrentPosition().
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(
      (loc) => resolve(clone(loc)),
      // in case the user doesnt have/is blocking `geolocation`
      (err) => reject(err)
    );
  });
}
```

Example 4 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: 'offscreen.html',
  reasons: [chrome.offscreen.Reason.GEOLOCATION || chrome.offscreen.Reason.DOM_SCRAPING],
  justification: 'geolocation access',
});
```

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/declare-permissions?hl=zh-cn

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Permissions Extension",
  ...
  "permissions": [
    "activeTab",
    "contextMenus",
    "storage"
  ],
  "optional_permissions": [
    "topSites",
  ],
  "host_permissions": [
    "https://www.developer.chrome.com/*"
  ],
  "optional_host_permissions":[
    "https://*/*",
    "http://*/*"
  ],
  ...
  "manifest_version": 3
}
```

---

## 扩展 Service Worker 生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/service_workers/service-worker-lifecycle?hl=zh-cn

**Contents:**
- 扩展 Service Worker 生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 安装
  - ServiceWorkerRegistration.install
  - chrome.runtime.onInstalled
  - ServiceWorkerRegistration.active
- 扩展程序启动
- 空闲和关机
  - 持久保留数据，而不是使用全局变量
  - 选择最低 Chrome 版本
    - Chrome 120

扩展程序服务工作器会响应标准服务工作器事件和扩展程序命名空间中的事件。之所以将它们放在一起介绍，是因为在扩展程序的使用过程中，一种类型通常会紧随另一种类型。

当用户从 Chrome 应用商店安装或更新服务工作线程时，或者当用户使用 chrome://extensions 页面加载或更新未打包的扩展程序时，系统会进行安装。依次发生以下三个事件：

安装期间触发的第一个事件是 Web 服务工作线程的 install 事件。

接下来是扩展程序的 onInstalled 事件，该事件会在首次安装扩展程序（而非服务工作线程）时、扩展程序更新到新版本时以及 Chrome 更新到新版本时触发。您可以使用此事件来设置状态或进行一次性初始化，例如上下文菜单。

最后，系统会触发 service worker 的 activate 事件。请注意，与 Web Service Worker 不同，此事件会在扩展程序安装后立即触发，因为扩展程序中没有与页面重新加载类似的操作。

当用户个人资料启动时，系统会触发 chrome.runtime.onStartup 事件，但不会调用任何 Service Worker 事件。

通常，当满足以下条件之一时，Chrome 会终止服务工作线程：

事件和对扩展程序 API 的调用会重置这些计时器，如果服务工作线程已进入休眠状态，则传入的事件会唤醒它们。不过，您应将 Service Worker 设计为能够抵御意外终止。

为了优化扩展程序的资源消耗，请尽可能避免让服务工作线程无限期保持活跃状态。测试您的扩展程序，确保您不是无意中这样做的。

如果 Service Worker 关闭，您设置的任何全局变量都将丢失。请勿使用全局变量，而是将值保存到存储空间。系统会列出可供选择的选项。

自发布清单 V3 以来，我们对服务工作线程生命周期进行了一些改进。这意味着，如果您的 Manifest V3 扩展程序支持旧版 Chrome，您需要了解一些条件。如果这些条件不会影响您的扩展程序，您可以跳过此部分。如果需要，请考虑在清单中指定最低 Chrome 版本。

现在，闹钟可以设置为最短 30 秒的周期，以匹配 service worker 生命周期。如需了解详情，请参阅 chrome.alarms。

使用 chrome.debugger API 创建的有效调试器会话现在可使 service worker 保持有效状态。这样可防止服务工作线程在此 API 的调用期间超时。

Chrome 116 引入了以下服务工作线程生命周期改进：

活跃的 WebSocket 连接现在会延长扩展服务工作线程的生命周期。在扩展服务工作器中通过 WebSocket 发送或接收消息会重置服务工作器的空闲计时器。

允许其他扩展程序 API 超过扩展程序服务工作线程的五分钟超时时间。这些 API 会显示用户提示，因此合理情况下可能需要超过 5 分钟才能解决。其中包括 desktopCapture.chooseDesktopMedia()、identity.launchWebAuthFlow()、management.uninstall() 和 permissions.request()。

使用持久消息传递发送消息可使 service worker 保持活跃状态。打开端口不再重置计时器。

扩展程序 API 调用会重置计时器。在此之前，只有正在运行的事件处理程序才能使服务工作线程保持活跃状态。任何已排队但尚未调用处理程序的事件都不会导致重置。

使用 chrome.runtime.connectNative() 连接到原生消息传递主机将使服务工作线程保持活动状态。如果宿主进程崩溃或关闭，端口会关闭，并且服务工作线程会在计时器完成后终止。为防止出现这种情况，请在端口的 onDisconnect 事件处理程序中调用 chrome.runtime.connectNative()。

**Examples:**

Example 1 (javascript):
```javascript
chrome.runtime.onInstalled.addListener((details) => {
  if(details.reason !== "install" && details.reason !== "update") return;
  chrome.contextMenus.create({
    "id": "sampleContextMenu",
    "title": "Sample Context Menu",
    "contexts": ["selection"]
  });
});
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
{
    ...
    "cross_origin_embedder_policy": {
      "value": "require-corp"
    },
    ...
}
```

---

## Manifest V2 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2?hl=zh-cn

**Contents:**
- Manifest V2 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

这些页面包含面向想要为 Chrome 浏览器创建扩展程序的开发者的指南和参考信息。如果您不确定从何处着手，请查看以下起始页面：

此外，您可能还会在以下页面中找到有用的入口点：

除了此处的文档之外，许多开发者还会在以下位置找到实用的社区内容：

感谢您成为扩展程序开发者社区的一员。很高兴您与我们联系！

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
{
  "name": "My enterprise extension",
  "storage": {
    "managed_schema": "schema.json"
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  "type": "object",

  // "properties" maps an optional key of this object to its schema. At the
  // top-level object, these keys are the policy names supported.
  "properties": {

    // The policy name "AutoSave" is mapped to its schema, which in this case
    // declares it as a simple boolean value.
    // "title" and "description" are optional and are used to show a
    // user-friendly name and documentation to the administrator.
    "AutoSave": {
      "title": "Automatically save changes.",
      "description": "If set to true then changes will be automatically saved.",
      "type": "boolean"
    },

    // Other simple types supported include "integer", "string" and "number".
    "PollRefreshRate": {
      "type": "integer"
    },

    "DefaultServiceUrl": {
      "type": "string"
    },

    // "array" is a list of items that conform to another schema, described
    // in "items". An example to this schema is [ "one", "two" ].
    "ServiceUrls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    // A more complex example that describes a list of bookmarks. Each bookmark
    // has a "title", and can have a "url" or a list of "children" bookmarks.
    // The "id" attribute is used to name a schema, and other schemas can reuse
    // it using the "$ref" attribute.
    "Bookmarks": {
      "type": "array",
      "id": "ListOfBookmarks",
      "items": {
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "url": { "type": "string" },
          "children": { "$ref": "ListOfBookmarks" }
        }
      }
    },

    // An "object" can have known properties listed as "properties", and can
    // optionally have "additionalProperties" indicating a schema to apply to
    // keys that aren't found in "properties".
    // This example policy could map a URL to its settings. An example value:
    // {
    //   "youtube.com": {
    //     "blocklisted": true
    //   },
    //   "google.com": {
    //     "bypass_proxy": true
    //   }
    // }
    "SettingsForUrls": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "blocklisted": { "type": "boolean" },
          "bypass_proxy": { "type": "boolean" }
        }
      }
    }
  }
}
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/publish-mv3?hl=zh-cn

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

---

## 针对 Chrome 扩展程序的端到端测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/end-to-end-testing?hl=zh-cn

**Contents:**
- 针对 Chrome 扩展程序的端到端测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 使用浏览器测试库
- 在无头 Chrome 中运行测试
- 设置扩展程序 ID
- 测试扩展程序页面
- 测试扩展程序弹出式窗口
- 检查扩展程序状态
- 测试 Service Worker 终止

端到端测试涉及构建扩展程序软件包并将其加载到浏览器中。测试工具会与浏览器通信，以自动执行互动并测试用户要经历的相同流程。支持端到端测试的库通常会提供控制浏览器、模拟用户输入和观察任何打开的网页的当前状态的方法。

如需查看教程，请参阅使用 Puppeteer 测试 Chrome 扩展程序；如需详细了解如何为 Chrome 扩展程序编写单元测试，请参阅单元测试。

在自动化工作流中运行测试时，通常需要在没有屏幕的机器上加载您的扩展程序。借助 Chrome 的全新无头模式，Chrome 可以在这种无人值守的环境中运行。使用 --headless=new 标志启动 Chrome（无头模式目前默认为“旧版”，不支持加载扩展程序）。根据您选择的自动化工具，其中可能有一个设置可自动为您添加此标志。

在测试中，通常需要使用固定的扩展程序 ID。这样，许多常见任务都变得更加轻松，例如在扩展程序需要与之通信的服务器上将扩展程序的来源列入许可名单，或在测试中打开扩展程序页面。为此，请按照保持一致的扩展程序 ID 下的步骤操作。

您可以使用相应的网址（例如 chrome-extension://<id>/index.html）访问扩展程序页面。使用您选择的自动化工具中提供的常规导航方法导航到这些网址。

目前无法在其他网页中打开扩展程序弹出式窗口。请改为在新标签页中打开弹出式窗口的网址。如果弹出式窗口使用活动标签页，请考虑实现一个替换机制，这样就可以将标签页 ID 显式传递到弹出式窗口。例如：

为避免在更改扩展程序的内部行为时测试失败，一般而言，最佳做法是避免在集成测试中访问内部状态。相反，您应根据用户可见的内容进行测试。但是，有时需要直接从扩展程序访问数据。在这些情况下，请考虑在扩展程序页面上下文中执行代码。

如需了解如何测试 Service Worker 终止，请参阅使用 Puppeteer 测试 Service Worker 终止。我们还提供了一个适用于 Puppeteer 和 Selenium 的示例。

请注意，使用某些测试框架时，服务工件可能不会像在正常使用中那样自动终止。在 Selenium 中就是如此。它依赖于 ChromeDriver，后者会将一个调试程序连接到所有 Service Worker，以防止它们停止。

**Examples:**

Example 1 (javascript):
```javascript
const URL_PARAMS  = new URLSearchParams(window.location.search);

async function getActiveTab() {
  // Open popup.html?tab=5 to use tab ID 5, etc.
  if (URL_PARAMS.has("tab")) {
    return await chrome.tabs.get(parseInt(URL_PARAMS.get("tab")));
  }

  const tabs = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  return tabs[0];
}
```

Example 2 (javascript):
```javascript
const workerTarget = await browser.waitForTarget(
  target => target.type() === 'service_worker'
);
const worker = await workerTarget.worker();

const value = await worker.evaluate(() => {
  chrome.storage.local.get('foo');
});
```

Example 3 (javascript):
```javascript
// Selenium doesn't allow us to access the service worker, so we need to open an extension page where we can execute the code
await driver.get('chrome-extension://<id>/popup.html');
await driver.executeAsyncScript(
  'const callback = arguments[arguments.length - 1];' +
  'chrome.storage.local.get(\'foo\').then(callback);'
);
```

---

## 处理远程托管代码违规行为 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/remote-hosted-code

**Contents:**
- 处理远程托管代码违规行为 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 为什么不再接受 RHC 了？
- 我被告知我的扩展程序含有 RHC。这是怎么回事？
- 如何识别 RHC
- 如果库请求代码，该怎么办
- 等不及要更新库怎么办？
  - 审核代码
  - 摇树
  - 自动编辑文件
  - 手动修改文件

远程托管的代码 (RHC) 是 Chrome 应用商店中任何 由从 扩展程序自己的文件例如 JavaScript 和 WASM。它不包括 或 CSS 文件

对于 Manifest V3 扩展程序，现在需要捆绑其在内部使用的所有代码 扩展程序本身过去，您可以从 。

如果您的扩展程序在审核过程中因出现 Blue Argon 错误而被拒，则： 我们的审核人员认为您的扩展程序使用了远程托管代码。这是 这通常是由于扩展程序试图使用遥控器添加脚本标记而导致的 （即来自开放网络，而不是来自 扩展程序），或提取资源以直接执行。

当您知道要寻找什么后，发现 RHC 并不特别困难。首先， 检查字符串“http://”或“https://”。如果您有 那么就有可能找出违规情况。如果 拥有完整的构建系统，或者使用 npm 或其他第三方 请确保你搜索的是经过编译的代码， 因为商店会评估这些内容如果您仍然无法 那么下一步就是联系一站式支持团队。他们 能够概述具体的违规行为，以及获得 扩展程序。

无论代码来自何处，都不允许带有 RHC。这个 包含并非由您编写，但正好在测试中用作依赖项的代码 项目。使用 Firebase 的一些开发者在远程访问 代码已添加到 Firebase Authentication 中。尽管这是一个 第一方（即 Google 自有）库，RHC 除外。您需要 将代码配置为移除 RHC 或将您的目标更新为 添加起始代码如果您遇到不是您的代码的问题 但加载的是 RHC 库，但您使用的是一个库 联系库作者告诉他们您正在经历一些事情， 并要求我们提供解决方法或更新代码来将其移除。

有些库会在收到通知后立即发布更新， 或需要一些时间才能解决问题。根据什么 您可能不需要等待用户 即可取消屏蔽并顺利通过审核这里有许多 快速恢复运行

您是否确定需要发起请求的代码？如果可以 或者删除导致该错误的库，然后删除 这样工作就完成了

或者，是否有其他库可以提供相同功能？试试看 检查 npmjs.com、GitHub 或其他网站，了解其他满足 相同的应用场景

如果导致 RHC 违规的代码实际并未使用，则可能是 无法通过工具自动删除现代构建工具 webpack、Rollup 和 Vite（仅举几例）具有一项功能 称为摇树优化。在构建系统中启用后，Tree shaking 应移除所有未使用的代码路径。这可能意味着您不仅拥有 合规版的代码，同时又能打造出更精简、更快捷的版本！请务必注意 请注意，并非所有库都可以执行摇树优化，但许多库却能进行摇树优化。部分 Rollup 和 Vite 等工具默认启用摇树优化功能。Webpack 需要进行配置才能启用。如果您使用的不是 build 作为扩展程序的一部分，但使用了代码库， 强烈建议您考虑向工作流中添加构建工具。构建 可帮助您编写更安全、更可靠且更易于维护的项目。

具体如何实现摇树优化取决于您的具体项目。 举一个简单的例子，使用 Rollup 创建 编译项目代码。例如，如果您有一个只登录 Firebase Auth，名为 main.js：

然后，您只需告诉 Rollup 输入文件，所需的插件 加载节点文件 @rollup/plugin-node-resolve 以及输出的名称 文件。

在终端窗口中运行该命令后，你将收到生成的版本 main.js 文件，全部编译成一个名为 compiled.js 的单个文件。

汇总操作可能很简单，但也可以极大地配置。您可以添加所有种类 复杂的逻辑和配置，请查看相应文档。 添加这样的构建工具将使代码更小、更高效， 在本例中，我们修复了远程托管代码的问题

远程托管代码进入代码库的一种日益常见的方式是 作为您要包含的库的子依赖项。如果库X想要 import库Y，那么您仍然需要更新它， 而是从本地来源加载借助现代构建系统，你可以轻松 插件来提取远程引用，并将其直接内嵌到代码中。

使用新插件运行 build 后，每个远程 import 网址都会 无论它是我们的代码、一个子依赖项， 子依赖项或其他地方。

最简单的方法是删除引发 RHC 的代码。打开方式 选择文本编辑器，删除违规代码行。这通常是 不不建议采用，因为它脆弱，可能会被忘记。它使 有一个名为“library.min.js”的文件时，不是 实际上是 library.min.js。与修改原始文件相比 可维护的选项是使用 patch-package 等工具。这是一个超级 一种强大的选项，可让您将修改保存到文件，而不是 文件本身。它基于补丁文件构建而成 为 Git 或 Subversion 等版本控制系统提供支持。您只需要 您可以手动修改违规代码、保存差异文件 包含您要应用的更改的补丁软件包您可以阅读完整的教程 针对项目的自述文件。如果您正在修补项目，我们真的 建议您与项目联系，申请做出更改 上游。虽然补丁软件包可以大大简化补丁的管理， 那就没有什么比这更棒的了

随着代码库的增长，依赖项（或某个依赖项的依赖项） 可以保留不再使用的代码路径。如果上述任一版块 包含用于加载或执行 RHC 的代码，则必须移除此类代码。它 无论其已失效还是未使用都无关紧要。如果未使用，则应该 移除，具体方法是摇树，或者修补库以将其移除。

一般来说不会。不允许使用 RHC。然而，有少数 在允许的情况下使用。在这些情况下 是任何其他选项都无法实现的

用户脚本是一小段代码，通常由 user，适用于 TamperMonkey 和 Violentmonkey。这些管理器无法将 是由用户编写的，因此 User Script API 提供了执行代码的方式， 由用户提供这不能替代 chrome.scripting.executeScript 或其他代码执行环境。 用户必须启用开发者模式才能执行任何内容。如果 Chrome 网页版 商店评价团队认为这些信息以其他方式使用， （即用户提供的代码），则可能会被拒绝或 已从商店下架。

借助 chrome.debugger API，扩展程序能够 Chrome Devtools 协议。该协议与 Chrome 的开发者工具以及数量惊人的其他工具。有了它 可以请求和执行远程代码。与用户脚本一样， 可取代 chrome.scripting，并显著改善用户体验。 在使用它时，用户会在 窗口。如果关闭或关闭横幅，则调试会话将 已终止。

如果您需要将字符串评估为代码，并且位于 DOM 环境（例如 内容脚本，而不是扩展程序 Service Worker），那么另一个选项 那就是使用沙盒化 iframe。扩展程序不支持 默认为 eval()（出于安全考虑）。恶意代码可能会给用户安全 和安全性风险。但是，如果代码仅在已知的 比如与网络其余部分隔离的 iframe 那么这些风险就会大大降低在这种情况下，内容安全协议 阻止使用 eval 的政策可以解除，让您可以运行任何 有效的 JavaScript 代码。

如果您的用例未涵盖在内，请随时与我们的团队联系 使用 chromium-extensions 邮寄名单来获取反馈，或打开一个新的 用于向一站式支持团队寻求指导的工单

政策的执行可能会发生细微的差别，审核过程需要手动输入内容，这意味着 Chrome 应用商店团队有时可能会同意更改审核决定。如果 如果您认为审核过程中有误，可以对被拒提出申诉 使用一站式支持

**Examples:**

Example 1 (python):
```python
import { GoogleAuthProvider, initializeAuth } from "firebase/auth";

chrome.identity.getAuthToken({ 'interactive': true }, async (token) => {
  const credential = GoogleAuthProvider.credential(null, token);
  try {
    const app = initializeApp({ ... });
    const auth = initializeAuth(app, { popupRedirectResolver: undefined, persistence: indexDBLocalPersistence });
    const { user } = await auth.signInWithCredential(credential)
    console.log(user)
  } catch (e) {
    console.error(error);
  }
});
```

Example 2 (unknown):
```unknown
npx rollup --input main.js --plugin '@rollup/plugin-node-resolve' --file compiled.js
```

Example 3 (python):
```python
import moment from "https://unpkg.com/moment@2.29.4/moment.js"
console.log(moment())
```

Example 4 (python):
```python
import { existsSync } from 'fs';
import fetch from 'node-fetch';

export default {
  plugins: [{
    load: async function transform(id, options, outputOptions) {
      // this code runs over all of out javascript, so we check every import
      // to see if it resolves as a local file, if that fails, we grab it from
      // the network using fetch, and return the contents of that file directly inline
      if (!existsSync(id)) {
        const response = await fetch(id);
        const code = await response.text();

        return code
      }
      return null
    }
  }]
};
```

---

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/permissions?hl=zh-cn

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 2 (javascript):
```javascript
document.querySelector('#my-button').addEventListener('click', (event) => {
  // Permissions must be requested from inside a user gesture, like a button's
  // click handler.
  chrome.permissions.request({
    permissions: ['tabs'],
    origins: ['https://www.google.com/']
  }, (granted) => {
    // The callback argument will be true if the user granted the permissions.
    if (granted) {
      doSomething();
    } else {
      doSomethingElse();
    }
  });
});
```

Example 3 (javascript):
```javascript
chrome.permissions.contains({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (result) => {
  if (result) {
    // The extension has the permissions.
  } else {
    // The extension doesn't have the permissions.
  }
});
```

Example 4 (javascript):
```javascript
chrome.permissions.remove({
  permissions: ['tabs'],
  origins: ['https://www.google.com/']
}, (removed) => {
  if (removed) {
    // The permissions have been removed.
  } else {
    // The permissions have not been removed (e.g., you tried to remove
    // required permissions).
  }
});
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

---

## 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/service_workers?hl=zh-cn

**Contents:**
- 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

本部分介绍了在扩展程序中使用 Service Worker 需要了解的内容。无论您是否熟悉 Service Worker，都应该阅读本部分。扩展程序 Service Worker 是扩展程序的核心事件处理脚本。这使得它们与 Web Service Worker 明显不同，网络中成堆的 Service Worker 文章不一定有用。

Extension Service Worker 与 Web 扩展 Service Worker 有一些共同点。扩展 Service Worker 在需要时加载，并在其进入休眠状态时取消加载。只要扩展程序 Service Worker 在加载后还会主动接收事件，它就会运行，不过它可以关闭。与对应的 Web 应用一样，扩展 Service Worker 无法访问 DOM，不过您可以根据需要将其用于屏幕外文档。

扩展程序 Service Worker 不只是网络代理（因为经常会提到 Web Service Worker）。除了标准 Service Worker 事件之外，它们还会响应扩展程序事件，例如导航到新页面、点击通知或关闭标签页。它们的注册和更新方式也与 Web Service Worker 不同。

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
{ // manifest.json
  "manifest_version": 3,
...
  "key": "ThisKeyIsGoingToBeVeryLong/go8GGC2u3UD9WI3MkmBgyiDPP2OreImEQhPvwpliioUMJmERZK3zPAx72z8MDvGp7Fx7ZlzuZpL4yyp4zXBI+MUhFGoqEh32oYnm4qkS4JpjWva5Ktn4YpAWxd4pSCVs8I4MZms20+yx5OlnlmWQEwQiiIwPPwG1e1jRw0Ak5duPpE3uysVGZXkGhC5FyOFM+oVXwc1kMqrrKnQiMJ3lgh59LjkX4z1cDNX3MomyUMJ+I+DaWC2VdHggB74BNANSd+zkPQeNKg3o7FetlDJya1bk8ofdNBARxHFMBtMXu/ONfCT3Q2kCY9gZDRktmNRiHG/1cXhkIcN1RWrbsCkwIDAQAB",
}
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

Example 1 (javascript):
```javascript
const response = await fetch('/config_resources/config.json');
const jsonData = await response.json();
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "https://www.google.com/"
  ],
  ...
}
```

Example 3 (unknown):
```unknown
"host_permissions": [
  "http://www.google.com/",
  "https://www.google.com/"
]
```

Example 4 (javascript):
```javascript
const response = await fetch("https://api.example.com/data.json");
const jsonData = await response.json();
// WARNING! Might be injecting a malicious script!
document.getElementById("resp").innerHTML = jsonData;
    ...
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
  "update_url": "https://clients2.google.com/service/update2/crx",
  "install_parameter": "Value"
}
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

---

## 替换屏蔽型 Web 请求监听器 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/blocking-web-requests?hl=zh-cn

**Contents:**
- 替换屏蔽型 Web 请求监听器 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 简介
- 更新权限
- 创建声明式网络请求规则
- 常见使用场景
  - 屏蔽单个网址
  - 重定向多个网址
  - 屏蔽 Cookie

Manifest V3 更改了扩展程序处理网络请求修改的方式。扩展程序不是使用 chrome.webRequest 在运行时拦截网络请求并对其进行更改，而是指定规则来描述在满足给定的一组条件时要执行的操作。使用声明式网络请求 API 执行此操作。

Web 请求 API 和声明式 Net 请求 API 存在显著差异。您需要根据使用情形重写代码，而不是将一个函数调用替换为另一个函数调用。本部分将引导您完成该过程。

如果您的扩展程序是通过政策安装的，则无需进行这些更改。对于通过政策安装的扩展程序，Manifest V3 中仍提供 webRequestBlocking 权限。

这是三个部分中的第二部分，介绍了非扩展服务工作线程的代码所需的更改。本文介绍了如何将 Manifest V2 使用的阻塞式网络请求转换为 Manifest V3 使用的声明式网络请求。其他两个部分介绍了迁移到 Manifest V3 所需的代码更新以及提高安全性。

在清单 V2 中，屏蔽 Web 请求可能会严重降低扩展程序的性能以及它们所处理的网页的性能。webRequest 命名空间支持 9 个可能会阻塞的事件，每个事件都可接受无限数量的事件处理程序。更糟糕的是，每个网页都可能被多个扩展程序屏蔽，而实现此目的所需的权限具有侵入性。Manifest V3 通过将回调替换为声明性规则来防范此问题。

对 manifest.json 中的 "permissions" 字段进行以下更改。

您需要根据自己的使用场景添加其他权限。这些权限及其支持的用例如下所述。

创建声明式网络请求规则需要在 manifest.json 中添加 "declarative_net_request" 对象。"declarative_net_request" 块包含指向规则文件的 "rule_resource" 对象数组。规则文件包含一个对象数组，用于指定操作以及调用这些操作的条件。

以下部分介绍了声明性网络请求的常见用例。以下说明仅提供简要概述。如需详细了解此处的全部信息，请参阅 API 参考文档中的 chrome.declarativeNetRequest

在清单 V2 中，一种常见的用例是在后台脚本中使用 onBeforeRequest 事件来阻止 Web 请求。

对于清单 V3，请使用 "block" 操作类型创建新的 declarativeNetRequest 规则。请注意示例规则中的 "condition" 对象。其 "urlFilter" 会替换传递给 webRequest 监听器的 urls 选项。"resourceTypes" 数组用于指定要屏蔽的资源类别。此示例仅屏蔽主 HTML 网页，但您也可以仅屏蔽字体。

为了使此功能正常运行，您需要更新扩展程序的权限。在 manifest.json 中，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。请注意，网址已从 "permissions" 字段中移除，因为屏蔽内容不需要主机权限。如上所示，规则文件指定了声明性网络请求所应用的主机。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

在清单 V2 中，另一个常见用例是使用 BeforeRequest 事件来重定向 Web 请求。

对于 Manifest V3，请使用 "redirect" 操作类型。与之前一样，"urlFilter" 会替换传递给 webRequest 监听器的 url 选项。请注意，在此示例中，规则文件的 "action" 对象包含一个 "redirect" 字段，其中包含要返回的网址，而不是要过滤的网址。

此方案还需要更改扩展程序的权限。与之前一样，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。网址再次从 manifest.json 移至规则文件。请注意，除了主机权限之外，重定向还需要 "declarativeNetRequestWithHostAccess" 权限。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

在 Manifest V2 中，屏蔽 Cookie 需要在发送网页请求标头之前拦截它们，并移除特定标头。

Manifest V3 也会通过规则文件中的规则执行此操作。这次操作类型为 "modifyHeaders"。该文件采用 "requestHeaders" 对象数组，用于指定要修改的标头以及修改方式。请注意，"condition" 对象仅包含一个 "resourceTypes" 数组。它支持与之前示例相同的值。

如果您想尝试此操作，可以在我们的示例代码库中找到以下代码。

此方案还需要更改扩展程序的权限。与之前一样，将 "webRequestBlocking" 权限替换为 "declarativeNetRequest" 权限。

**Examples:**

Example 1 (javascript):
```javascript
chrome.webRequest.onBeforeRequest.addListener((e) => {
    return { cancel: true };
}, { urls: ["https://www.example.com/*"] }, ["blocking"]);
```

Example 2 (unknown):
```unknown
[
  {
    "id" : 1,
    "priority": 1,
    "action" : { "type" : "block" },
    "condition" : {
      "urlFilter" : "||example.com",
      "resourceTypes" : ["main_frame"]
    }
  }
]
```

Example 3 (unknown):
```unknown
"permissions": [
    "webRequestBlocking",
    "https://*.example.com/*"
  ]
```

Example 4 (unknown):
```unknown
"permissions": [
    "declarativeNetRequest",
  ]
```

---

## file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/manifest/file_handlers?hl=zh-cn

**Contents:**
- file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"file_handlers" 清单键用于指定 ChromeOS 扩展程序要处理的文件类型。如需处理文件，请使用 Web 平台的 Launch Handler API。如需了解特定于扩展程序的信息，请参阅文件处理。

**Examples:**

Example 1 (unknown):
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

---

## 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/tut_analytics?hl=zh-cn

**Contents:**
- 使用 Google Analytics（分析）4 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 要求
- 使用 Google Analytics Measurement Protocol
  - 设置 API 凭据
  - 生成 client_id
  - 发送分析事件
  - 使用建议的参数 session_id 和 engagement_time_msec
- 跟踪弹出式窗口、侧边栏和扩展程序页面中的网页浏览量
- 在 Service Worker 中跟踪分析事件
- 调试

本教程演示如何使用 Google Analytics 跟踪扩展程序的使用情况。您可以在 GitHub 上找到有效的 Google Analytics 4 示例，其中 google-analytics.js 包含所有 Google Analytics 相关代码。

本教程假定您熟悉编写 Chrome 扩展程序。如果您需要了解如何编写扩展程序，请参阅入门教程。

此外，您还必须设置 Google Analytics 4 账号才能跟踪您的扩展程序。请注意，在设置账号时，您可以使用“网站网址”字段中的任何值，因为您的扩展程序不会有自己的网址。

从 Manifest V3 开始，Chrome 扩展程序不得执行远程托管的代码。也就是说，您必须使用 Google Analytics Measurement Protocol 来跟踪扩展程序事件。利用 Measurement Protocol，您可以通过 HTTP 请求直接将事件发送到 Google Analytics 服务器。这种方法的一大优势在于，它允许您从扩展程序中的任何位置（包括 Service Worker）发送分析事件。

第一步是获取 api_secret 和 measurement_id。请参阅 Measurement Protocol 文档，了解如何为您的 Google Analytics 账号获取这些数据。

第二步是为特定设备/用户生成唯一标识符，即 client_id。只要扩展程序安装在用户浏览器中，ID 就应保持不变。它可以是任意字符串，但对客户端而言应该是唯一的。您可以通过调用 self.crypto.randomUUID() 生成一个。将 client_id 存储在 chrome.storage.local 中，以确保其在安装扩展程序期间保持不变。

要使用 chrome.storage.local，您需要在清单文件中拥有 storage 权限：

然后，您可以使用 chrome.storage.local 存储 client_id：

借助 API 凭据和 client_id，您可以通过 fetch 请求向 Google Analytics 发送事件：

这样会发送 button_clicked 事件，该事件会显示在您的 Google Analytics 事件报告中。如果您想在 Google Analytics 实时报告中查看事件，则需要提供两个额外的参数：session_id 和 engagement_time_msec。

session_id 和 engagement_time_msec 都是使用 Google Analytics Measurement Protocol 时的推荐参数，因为它们在实时等标准报告中显示用户活动时必不可少。

session_id 描述了用户持续与您的扩展程序互动的时间段。默认情况下，会话会在用户处于不活动状态 30 分钟后结束。会话无持续时间限制。

与常规网站不同，Chrome 扩展程序中没有明确的用户会话概念。因此，您必须在扩展程序中定义用户会话的含义。例如，每次新的用户互动都可能是一次新会话。在这种情况下，您只需为每个事件生成一个新的会话 ID（即使用时间戳）。

以下示例演示了一种方法，该方法会在没有报告任何事件 30 分钟后使新会话超时（您可以自定义此时间，以更好地适应您的扩展程序的用户行为）。该示例使用 chrome.storage.session 来存储浏览器运行时的活动会话。我们将与会话一起存储上次触发事件的时间。我们可以通过以下方法判断当前会话是否已过期：

以下示例将 session_id 和 engagement_time_msec 添加到了上一个按钮点击事件请求中。对于 engagement_time_msec，您可以提供默认值 100 ms。

该事件在 Google Analytics 实时报告中将按如下方式显示。

Google Analytics Measurement Protocol 支持用于跟踪网页浏览量的特殊 page_view 事件。使用此方法跟踪访问新标签页、侧边栏或扩展程序页面（新标签页中）的用户。page_view 事件还需要 page_title 和 page_location 参数。以下示例会在文档 load 事件中针对扩展程序弹出式窗口触发网页浏览事件：

popup.js 脚本需要导入到弹出式窗口的 HTML 文件中，并且应在执行任何其他脚本之前运行：

弹出式视图将像 Google Analytics 实时报告中的任何其他网页浏览一样显示：

使用 Google Analytics Measurement Protocol 可以跟踪扩展程序 Service Worker 中的分析事件。例如，通过监听 Service Worker 中的 unhandledrejection event，您可以将 Service Worker 中任何未捕获的异常记录到 Google Analytics，这在很大程度上有助于调试用户可能报告的问题。

现在，您可以在 Google Analytics 报告中查看错误事件：

Google Analytics 提供了两项实用功能，用于在扩展程序中调试 Analytics 事件：

**Examples:**

Example 1 (unknown):
```unknown
{
  …
  "permissions": ["storage"],
  …
}
```

Example 2 (javascript):
```javascript
async function getOrCreateClientId() {
  const result = await chrome.storage.local.get('clientId');
  let clientId = result.clientId;
  if (!clientId) {
    // Generate a unique client ID, the actual value is not relevant
    clientId = self.crypto.randomUUID();
    await chrome.storage.local.set({clientId});
  }
  return clientId;
}
```

Example 3 (javascript):
```javascript
const GA_ENDPOINT = 'https://www.google-analytics.com/mp/collect';
const MEASUREMENT_ID = `G-...`;
const API_SECRET = `...`;

fetch(
  `${GA_ENDPOINT}?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`,
  {
    method: 'POST',
    body: JSON.stringify({
      client_id: await getOrCreateClientId(),
      events: [
        {
          name: 'button_clicked',
          params: {
            id: 'my-button',
          },
        },
      ],
    }),
  }
);
```

Example 4 (javascript):
```javascript
const SESSION_EXPIRATION_IN_MIN = 30;

async function getOrCreateSessionId() {
  // Store session in memory storage
  let {sessionData} = await chrome.storage.session.get('sessionData');
  // Check if session exists and is still valid
  const currentTimeInMs = Date.now();
  if (sessionData && sessionData.timestamp) {
    // Calculate how long ago the session was last updated
    const durationInMin = (currentTimeInMs - sessionData.timestamp) / 60000;
    // Check if last update lays past the session expiration threshold
    if (durationInMin > SESSION_EXPIRATION_IN_MIN) {
      // Delete old session id to start a new session
      sessionData = null;
    } else {
      // Update timestamp to keep session alive
      sessionData.timestamp = currentTimeInMs;
      await chrome.storage.session.set({sessionData});
    }
  }
  if (!sessionData) {
    // Create and store a new session
    sessionData = {
      session_id: currentTimeInMs.toString(),
      timestamp: currentTimeInMs.toString(),
    };
    await chrome.storage.session.set({sessionData});
  }
  return sessionData.session_id;
}
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
<script src="./react-dom.production.min.js"></script>
<link href="./bootstrap.min.css" rel="stylesheet">
```

Example 2 (unknown):
```unknown
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['jquery-min.js', 'content-script.js']
});
```

Example 3 (javascript):
```javascript
let name = 'World!';
chrome.tabs.executeScript({
  code: `alert('Hello, ${name}!')`
});
```

Example 4 (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

function showAlert(givenName) {
  alert(`Hello, ${givenName}`);
}

let name = 'World';
chrome.scripting.executeScript({
  target: {tabId: tab.id},
  func: showAlert,
  args: [name],
});
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

---

## file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/manifest/file-handlers?hl=zh-cn

**Contents:**
- file_handlers 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

"file_handlers" 清单键用于指定 ChromeOS 扩展程序要处理的文件类型。如需处理文件，请使用 Web 平台的 Launch Handler API。如需了解特定于扩展程序的信息，请参阅文件处理。

**Examples:**

Example 1 (unknown):
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
{
    ...
    "cross_origin_embedder_policy": {
      "value": "require-corp"
    },
    ...
}
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
{
  "name": "My externally connectable extension",
  "externally_connectable": {
    "ids": [
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
      ...
    ],
    // If this field is not specified, no web pages can connect.
    "matches": [
      "https://*.google.com/*",
      "*://*.chromium.org/*",
      ...
    ],
    "accepts_tls_channel_id": false
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
    "extension_pages": "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';"
  }
  // ...
}
```

Example 3 (unknown):
```unknown
'content_security_policy.extension_pages': Insecure CSP value "'unsafe-eval'" in directive 'script-src'.
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

---

## chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/enterprise/deviceAttributes

**Contents:**
- chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - getDeviceAnnotatedLocation()
    - 参数
    - 返回
  - getDeviceAssetId()
    - 参数

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

获取管理员注释的位置信息。如果当前用户没有关联的组织，或者管理员未设置带注释的位置，则返回空字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取管理员注释的资产 ID。如果当前用户没有关联的资产，或者管理员未设置任何资产 ID，则返回空字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取由 DeviceHostnameTemplate 政策设置的设备主机名。如果当前用户未关联或企业政策未设置主机名，则返回空字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取设备的序列号。请注意，此 API 的目的是管理设备（例如，为设备级证书生成证书签名请求）。未经设备管理员同意，不得使用此 API 跟踪设备。如果当前用户没有关联的商家，则返回空字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取 Directory API 的设备标识符的值，该值由服务器生成，用于标识设备在 Cloud Directory API 中的云记录，以便在 Cloud Directory API 中进行查询。如果当前用户没有关联的商家，则返回空字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAnnotatedLocation(  callback?: function,): Promise<string>
```

Example 2 (javascript):
```javascript
(annotatedLocation: string) => void
```

Example 3 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAssetId(  callback?: function,): Promise<string>
```

Example 4 (javascript):
```javascript
(assetId: string) => void
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

---

## Linux 的自托管 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/linux_hosting?hl=zh-cn

**Contents:**
- Linux 的自托管 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 软件包
  - 从 Chrome 应用商店下载 .crx
  - 在本地创建 .crx
  - 更新 .crx 软件包
  - 通过命令行打包
- 主机
- 更新
  - 更新网址
  - 更新清单

Chrome 用户只能通过 Linux 安装 Chrome 应用商店。本文介绍了如何打包、托管和更新 crx 来自通用网络服务器的文件。如果您仅分发扩展程序或主题 访问 Chrome 应用商店，请查阅应用商店托管和 正在更新。

扩展程序和主题以 .crx 文件的形式提供。通过 Chrome 开发者工具上传 信息中心，则信息中心会自动创建 crx 文件。如果已发布 在个人服务器上，则需要在本地创建 crx 文件，或者从 Chrome 中下载该文件 应用商店。

如果扩展程序托管在 Chrome 应用商店中，则可从以下网址下载 .crx 文件： 开发者信息中心。在“您的商品详情”下方找到相应扩展程序然后点击“详情”在 弹出式窗口，点击蓝色的 main.crx 链接即可下载。

下载的文件可以托管在个人服务器上。这是托管 因为 Chrome 应用商店会对扩展程序的内容进行签名。这个 有助于检测潜在的攻击和篡改。

扩展程序目录会在“扩展程序管理”页面上转换为 .crx 文件。导航到 chrome://extensions/，或者点击 Chrome 菜单，然后将鼠标指针悬停在“更多工具”上然后 选择“扩展程序”。

在“扩展程序管理”页面上，点击“扩展程序”旁边的切换开关 开发者模式。然后选择软件包扩展按钮。

在“扩展程序根目录”字段中指定扩展程序文件夹的路径，然后点击 软件包扩展按钮。对于首次使用的文件包，请忽略私钥字段。

Chrome 会创建两个文件：.crx 文件和 .pem 文件，其中包含扩展程序的 私钥。

切勿丢失私钥！将 .pem 文件保存在秘密安全的位置；时间将是 需要更新该扩展程序。

通过增加 manifest.json 中的版本号来更新扩展程序的 .crx 文件。

返回“扩展程序管理”页面，然后点击扩展程序包按钮。指定 扩展程序目录的路径以及私钥的位置。

通过调用 chrome.exe 在命令行中打包扩展程序。使用 --pack-extension 标志用于指定扩展程序文件夹的位置，将 --pack-extension-key 标志用于 指定扩展程序私钥文件的位置。

托管 .crx 文件的服务器必须使用相应的 HTTP 标头，以允许用户安装 从而创建相应的扩展程序

如果文件符合下列任一条件，Google Chrome 便会将其视为可安装：

无法识别可安装文件的最常见原因是，服务器发送了 标题 X-Content-Type-Options: nosniff。第二种最常见的原因是 未知内容类型 - 不在前一个列表中的内容类型。要修复 HTTP 标头问题，您可以将 服务器配置，或尝试在其他服务器上托管 .crx 文件。

浏览器每隔几小时就会检查已安装的扩展程序是否有更新网址。对于每一个事件，都会生成一个 请求，以查找更新清单 XML 文件。

如果更新清单提及的版本高于安装的版本， 下载并安装新版本。与手动更新一样，必须为新的 .crx 文件签名 拥有与当前安装的版本相同的私钥。

如果扩展程序托管在 Chrome 应用商店之外的服务器上，则必须在update_url 其 manifest.json 文件。

此 XML 格式借用了 Google 的更新基础架构 Omaha 所使用的格式。通过 扩展系统为 <app> 和 <updatecheck> 元素 更新清单：

更新清单 XML 文件可能包含关于多个扩展名的信息 <app> 元素。

默认的更新检查频率为几小时，但可以使用更新 扩展程序管理页面上的“立即扩展程序”按钮。

基本的自动更新机制旨在使服务器端工作变得简单，就像直接丢弃一个 将静态 XML 文件复制到任何普通 Web 服务器（如 Apache）上，然后将该 XML 文件更新为新的 扩展程序版本发布。

托管多个扩展程序的开发者可能会检查请求参数，这些参数表示扩展程序 ID 和版本信息添加这些参数可让扩展程序从 运行动态服务器端代码而不是静态 XML 文件的相同网址。

其中，EXTENSION_DATA 是以下格式的网址编码字符串：

id=EXTENSION_ID&v=EXTENSION_VERSION

例如，两个扩展程序指向同一个更新网址 (https://test.com/extension_updates.php)：

对于每个唯一的更新网址，一个请求中可以列出多个扩展程序。对于上一个 例如，如果用户安装了这两个扩展程序，那么这两个请求会合并为 单个请求：

如果使用同一更新网址的已安装扩展程序数量足够多，可以发出 GET 请求 网址太长（超过 2000 个字符），更新检查会发出额外的 GET 请求，如下所示 。

随着越来越多的 API 添加到扩展程序系统中，扩展程序的更新版本也会 但只有较新版本的浏览器才能发布虽然 Chrome 浏览器是自动更新的 绝大多数用户可能需要几天时间才会更新到任何特定的新版本。接收者 确保特定更新仅适用于 添加“prodversionmin”属性添加到更新响应中的 <app> 元素。

这样可以确保用户只有在运行 Google Chrome 时才会自动更新到版本 2 3.0.193.0 或更高版本。

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

Example 2 (unknown):
```unknown
{
  ...
  "version": "1.6",
  ...
  }
}
```

Example 3 (unknown):
```unknown
chrome.exe --pack-extension=C:\myext --pack-extension-key=C:\myext.pem
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "update_url": "https://myhost.com/mytestextension/updates.xml",
  ...
}
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
  "update_url": "https://clients2.google.com/service/update2/crx",
  "install_parameter": "Value"
}
```

---

## 为用户提供选项 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/options?hl=zh-cn

**Contents:**
- 为用户提供选项 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 找到选项页面
- 编写选项页面
- 声明选项页面行为
  - 整页选项
  - 嵌入式选项
- 考虑不同之处
  - 指向选项页面的链接
  - Tabs API
  - Messaging API

就像扩展程序可让用户自定义 Chrome 浏览器一样，通过选项页面 自定义扩展程序使用选项来启用功能并允许用户进行选择 哪些功能适合他们的需求

用户可以通过以下两种方式访问选项页面：直接链接，或右键点击工具栏中的扩展程序图标，然后选择选项。此外，用户还可以通过以下方式导航到选项页面：首先打开 chrome://extensions，找到所需的扩展程序，点击 Details，然后选择选项链接。

下面是一个选项脚本示例。将其保存到 options.html 所在的文件夹中。 这样就能使用 storage.sync API 在不同设备上保存用户的首选选项。

最后，将 "storage" 权限添加到扩展程序的清单文件中：

附加信息选项网页分为两类：完整网页和嵌入式。类型 取决于其在清单中的声明方式。

系统会在新标签页中显示整页选项页面。在清单中的 "options_page" 字段中注册选项 HTML 文件。

通过嵌入式选项页，用户无需离开 嵌入框中的扩展程序管理页面。要声明嵌入选项，请注册 HTML 文件（位于扩展程序清单中的 "options_ui" 字段下），并将 "open_in_tab" 键设为 false。

嵌入在 chrome://extensions 内的选项页面在行为上与标签页中的选项页面存在细微差异。

扩展程序可通过调用 chrome.runtime.openOptionsPage()。例如，可将其添加到弹出式窗口中：

由于嵌入选项代码并非托管在标签页中，因此无法使用 Tabs API。 请改用 runtime.connect() 和 runtime.sendMessage()。 。

如果扩展程序的选项页面使用 runtime.connect() 或 runtime.sendMessage()，系统将不设置发件人的标签页，但会设置发件人的网址 是选项页面网址。

嵌入的选项应根据网页内容自动确定自己的大小。不过， 嵌入式框可能找不到适合某些类型的内容的尺寸。此问题最常见于 可根据窗口大小调整内容形状的选项页面。

如果这是一个问题，请为选项页提供固定的尺寸下限，以确保 嵌入式页面会找到合适的尺寸。

**Examples:**

Example 1 (unknown):
```unknown
<!DOCTYPE html>
<html>
  <head>
    <title>My Test Extension Options</title>
  </head>
  <body>
    <select id="color">
      <option value="red">red</option>
      <option value="green">green</option>
      <option value="blue">blue</option>
      <option value="yellow">yellow</option>
    </select>

    <label>
      <input type="checkbox" id="like" />
      I like colors.
    </label>

    <div id="status"></div>
    <button id="save">Save</button>

    <script src="options.js"></script>
  </body>
</html>
```

Example 2 (javascript):
```javascript
// Saves options to chrome.storage
const saveOptions = () => {
  const color = document.getElementById('color').value;
  const likesColor = document.getElementById('like').checked;

  chrome.storage.sync.set(
    { favoriteColor: color, likesColor: likesColor },
    () => {
      // Update status to let user know options were saved.
      const status = document.getElementById('status');
      status.textContent = 'Options saved.';
      setTimeout(() => {
        status.textContent = '';
      }, 750);
    }
  );
};

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
const restoreOptions = () => {
  chrome.storage.sync.get(
    { favoriteColor: 'red', likesColor: true },
    (items) => {
      document.getElementById('color').value = items.favoriteColor;
      document.getElementById('like').checked = items.likesColor;
    }
  );
};

document.addEventListener('DOMContentLoaded', restoreOptions);
document.getElementById('save').addEventListener('click', saveOptions);
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "storage"
  ]
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "options_page": "options.html",
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
{ // manifest.json
  "manifest_version": 3,
...
  "key": "ThisKeyIsGoingToBeVeryLong/go8GGC2u3UD9WI3MkmBgyiDPP2OreImEQhPvwpliioUMJmERZK3zPAx72z8MDvGp7Fx7ZlzuZpL4yyp4zXBI+MUhFGoqEh32oYnm4qkS4JpjWva5Ktn4YpAWxd4pSCVs8I4MZms20+yx5OlnlmWQEwQiiIwPPwG1e1jRw0Ak5duPpE3uysVGZXkGhC5FyOFM+oVXwc1kMqrrKnQiMJ3lgh59LjkX4z1cDNX3MomyUMJ+I+DaWC2VdHggB74BNANSd+zkPQeNKg3o7FetlDJya1bk8ofdNBARxHFMBtMXu/ONfCT3Q2kCY9gZDRktmNRiHG/1cXhkIcN1RWrbsCkwIDAQAB",
}
```

---
