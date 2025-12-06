# Chrome-Extensions - Permissions

**Pages:** 5

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/scripting

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Scripting Extension",
  "manifest_version": 3,
  "permissions": ["scripting", "activeTab"],
  ...
}
```

Example 2 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId()},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected"));
```

Example 3 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), allFrames : true},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected in all frames"));
```

Example 4 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), frameIds : [ frameId1, frameId2 ]},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected on target frames"));
```

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/scripting/?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Scripting Extension",
  "manifest_version": 3,
  "permissions": ["scripting", "activeTab"],
  ...
}
```

Example 2 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId()},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected"));
```

Example 3 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), allFrames : true},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected in all frames"));
```

Example 4 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), frameIds : [ frameId1, frameId2 ]},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected on target frames"));
```

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/scripting?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Scripting Extension",
  "manifest_version": 3,
  "permissions": ["scripting", "activeTab"],
  ...
}
```

Example 2 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId()},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected"));
```

Example 3 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), allFrames : true},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected in all frames"));
```

Example 4 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), frameIds : [ frameId1, frameId2 ]},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected on target frames"));
```

---

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/declarativeNetRequest

**Contents:**
- chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和使用
  - 动态规则集和会话级范围的规则集
  - 静态规则集
  - 启用和停用静态规则和规则集
  - 构建规则

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

declarativeNetRequestFeedbackhost_permissions

除了上述权限之外，某些类型的规则集（尤其是静态规则集）还需要声明 "declarative_net_request" 清单键，该键应是一个包含单个键（名为 "rule_resources"）的字典。此键是一个包含 Ruleset 类型字典的数组，如下所示。（请注意，由于“Ruleset”只是一个数组，因此不会显示在清单的 JSON 中。）本文档后面部分介绍了静态规则集。

如需使用此 API，请指定一个或多个规则集。规则集包含一个规则数组。单个规则可执行以下操作之一：

在使用扩展程序时，动态规则集和会话规则集通过 JavaScript 进行管理。

每种规则集类型只有一个。扩展程序可以通过调用 updateDynamicRules() 和 updateSessionRules() 动态添加或移除规则，前提是未超出规则限制。如需了解规则限制，请参阅规则限制。您可以在代码示例下查看相关示例。

与动态规则和会话规则不同，静态规则在安装或升级扩展程序时进行打包、安装和更新。它们以 JSON 格式存储在规则文件中，并使用 "declarative_net_request" 和 "rule_resources" 键（如上所述）以及一个或多个 Ruleset 字典向扩展程序指示。Ruleset 字典包含规则文件的路径、文件中包含的规则集的 ID，以及规则集是启用还是停用。当您以编程方式启用或停用规则集时，后两个属性非常重要。

如需测试规则文件，请以未打包的形式加载扩展程序。有关无效静态规则的错误和警告仅针对未打包的扩展程序显示。系统会忽略打包扩展程序中的无效静态规则。

在运行时，您可以启用或停用单个静态规则和完整的静态规则集。

已启用的静态规则和规则集的集合会在浏览器会话之间保持不变。这两者都不会在扩展程序更新后保留，这意味着只有您选择保留在规则文件中的规则会在更新后可用。

出于性能方面的原因，一次可启用的规则和规则集数量也有限制。调用 getAvailableStaticRuleCount() 以检查可启用的额外规则的数量。如需了解规则限制，请参阅规则限制。

如需启用或停用静态规则，请调用 updateStaticRules()。此方法接受一个 UpdateStaticRulesOptions 对象，其中包含要启用或停用的规则 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

如需启用或停用静态规则集，请调用 updateEnabledRulesets()。此方法接受一个 UpdateRulesetOptions 对象，其中包含要启用或停用的规则集 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

无论规则类型如何，规则都以四个字段开头，如下所示。虽然 "id" 和 "priority" 键采用的是数字，但 "action" 和 "condition" 键可以提供多个屏蔽和重定向条件。以下规则会屏蔽从 "foo.com" 发送到任何包含 "abc" 作为子字符串的网址的所有脚本请求。

规则的 "condition" 键允许使用 "urlFilter" 键来处理指定网域下的网址。您可以使用模式匹配令牌创建模式。下面列举了一些示例。

规则由网页发送的请求触发。如果多条规则与特定请求匹配，则必须确定这些规则的优先级。本部分将介绍如何确定这些通知的优先级。确定优先顺序分为两个阶段。

您可以这样考虑匹配：特定扩展程序优先考虑的任何规则都将优先于其他扩展程序的规则。

在单个扩展服务中，优先级是通过以下流程确定的：

如果有多条规则具有最高的开发者定义优先级，则使用 "action" 字段按以下顺序确定规则的优先级：

如果操作类型不是 block 或 redirect，则评估任何匹配的 modifyHeaders 规则。请注意，如果存在任何开发者定义的优先级低于为 allow 和 allowAllRequests 指定的优先级的规则，则会忽略这些规则。

如果多条规则修改了同一标头，则修改由开发者定义的 "priority" 字段和指定的操作决定。

如果只有一个扩展程序的规则与请求匹配，则应用该规则。不过，如果有多个扩展程序与请求匹配，系统会使用以下流程：

系统会使用 "action" 字段按以下顺序确定规则的优先级：

如果有多个规则匹配，则最近安装的扩展程序优先。

在浏览器中加载和评估规则会产生性能开销，因此使用该 API 时会受到一些限制。限制取决于您使用的规则类型。

静态规则是指在清单文件中声明的规则文件中指定的规则。扩展程序最多可以在 "rule_resources" 清单键中指定 50 个静态规则集，但一次只能启用其中的 10 个规则集。后者称为 MAX_NUMBER_OF_ENABLED_STATIC_RULESETS。这些规则集总共至少包含 30,000 条规则。这称为 GUARANTEED_MINIMUM_STATIC_RULES。

之后可用的规则数量取决于用户浏览器上安装的所有扩展程序启用的规则数量。您可以在运行时通过调用 getAvailableStaticRuleCount() 找到此数字。您可以在代码示例下查看相关示例。

应用于动态规则和会话规则的限制比静态规则更简单。两者的总数不得超过 5,000。这称为 MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES。

所有类型的规则都可以使用正则表达式；不过，每种类型的正则表达式规则总数不得超过 1000 条。这称为 MAX_NUMBER_OF_REGEX_RULES。

此外，每条规则在编译后的大小必须小于 2KB。这与规则的复杂程度大致相关。如果您尝试加载超出此限制的规则，系统会显示如下警告，并忽略该规则。

declarativeNetRequest 仅适用于到达网络堆栈的请求。这包括来自 HTTP 缓存的响应，但不一定包括通过服务工作线程的 onfetch 处理程序的响应。declarativeNetRequest 不会影响由服务工作线程生成的响应或从 CacheStorage 检索的响应，但会影响在服务工作线程中对 fetch() 的调用。

declarativeNetRequest 规则无法将公开资源请求重定向到无法通过网络访问的资源。这样做会触发错误。即使指定的 Web 可访问资源归重定向扩展程序所有，也是如此。如需为 declarativeNetRequest 声明资源，请使用清单的 "web_accessible_resources" 数组。

以下示例展示了如何调用 updateDynamicRules()。updateSessionRules() 的流程相同。

以下示例展示了如何在考虑可用静态规则集数量和已启用静态规则集数量上限的情况下启用和停用规则集。当您需要的静态规则数量超出允许的数量时，可以这样做。为此，您应安装部分规则集，并停用部分规则集（在清单文件中将 "Enabled" 设置为 false）。

以下示例说明了 Chrome 如何确定扩展程序中规则的优先级。在查看这些规则时，您可能需要在单独的窗口中打开优先级规则。

这些示例需要 host 权限才能访问 *://*.example.com/*。

如需确定特定网址的优先级，请查看（开发者定义的）"priority" 键、"action" 键和 "urlFilter" 键。这些示例引用了下方显示的示例规则文件。

以下示例需要对 *://*.example.com/* 具有主机权限。

以下示例展示了如何将来自 example.com 的请求重定向到扩展程序本身中的网页。扩展程序路径 /a.jpg 解析为 chrome-extension://EXTENSION_ID/a.jpg，其中 EXTENSION_ID 是扩展程序的 ID。为此，清单应将 /a.jpg 声明为可供 Web 访问的资源。

以下示例使用 "transform" 键重定向到 example.com 的子网域。它使用域名锚点 (“||”) 拦截来自 example.com 的任何方案的请求。"transform" 中的 "scheme" 键指定重定向到子网域时将始终使用“https”。

以下示例使用正则表达式将用户从 https://www.abc.xyz.com/path 重定向到 https://abc.xyz.com/path。在 "regexFilter" 键中，请注意句点是如何转义的，以及捕获组如何选择“abc”或“def”。"regexSubstitution" 键使用“\1”指定正则表达式的第一个返回匹配项。在这种情况下，系统会从重定向的网址中捕获“abc”，并将其放置在替换项中。

以下示例会从主框架和所有子框架中移除所有 Cookie。

用于描述相应请求是第一方请求还是第三方请求（相对于发起该请求的框架而言）。如果请求与发起请求的框架具有相同的网域 (eTLD+1)，则该请求称为第一方请求。

“firstParty” 网络请求是发起该请求的框架的第一方。

“thirdParty” 网络请求是发起该请求的框架的第三方。

是否自动将网页的操作次数显示为扩展程序的徽章文字。此偏好设置会在各个会话中保留。

TabActionCountUpdate 可选

如果指定，则仅包含具有匹配 ID 的规则。

如果指定了此条件，则当标头存在但其值包含此列表中的至少一个元素时，系统不会匹配此条件。此属性使用的匹配模式语法与 values 相同。

标头的名称。仅当未指定 values 和 excludedValues 时，此条件才会匹配名称。

如果指定了此条件，则当标头的值与此列表中的至少一个模式匹配时，此条件即为匹配。此功能支持不区分大小写的标头值匹配以及以下构造：

可以使用反斜杠对“*”和“?”进行转义，例如“\*”和“\?”

此表描述了“modifyHeaders”规则的可能操作。

“append” 为指定的标头添加新条目。修改请求的标头时，此操作仅支持特定标头。

“set” 为指定标头设置新值，并移除具有相同名称的所有现有标头。

“remove” 移除指定标头的所有条目。

UnsupportedRegexReason 可选

指定不支持正则表达式的原因。仅当 isSupported 为 false 时提供。

相应规则所属的 Ruleset 的 ID。对于源自动态规则集的规则，此值将等于 DYNAMIC_RULESET_ID。

如果标签页仍处于活动状态，则为发起请求的标签页的 tabId。否则为 -1。

匹配规则的时间。时间戳将符合 JavaScript 的时间惯例，即自纪元以来的毫秒数。

如果指定，则仅匹配给定标签页的规则。如果设置为 -1，则匹配未与任何有效标签页相关联的规则。

标头的新值。必须为 append 和 set 操作指定。

如果为 true，则仅当查询键已存在时才替换该键。否则，如果缺少该键，系统也会添加该键。默认值为 false。

相对于扩展程序目录的路径。应以“/”开头。

指定了 regexFilter 的规则的替换模式。网址中首次匹配到的 regexFilter 将替换为此模式。在 regexSubstitution 中，可以使用通过反斜杠转义的数字（\1 至 \9）来插入相应的捕获组。“\0”表示整个匹配文本。

重定向网址。不允许重定向到 JavaScript 网址。

指定的 regex 是否区分大小写。默认值为 true。

指定的 regex 是否需要捕获。只有指定了 regexSubstition 操作的重定向规则才需要捕获。默认值为 false。

相应框架的文档的唯一标识符（如果此请求是针对框架的）。

相应框架的文档的生命周期（如果此请求是针对框架的）。

值 0 表示请求发生在主框架中；正值表示请求发生的子框架的 ID。如果加载了（子）框架的文档（type 为 main_frame 或 sub_frame），则 frameId 表示此框架的 ID，而不是外部框架的 ID。框架 ID 在标签页中是唯一的。

发起请求的来源。此值不会因重定向而改变。如果这是不透明来源，则将使用字符串“null”。

相应框架的父文档的唯一标识符（如果此请求是针对框架且具有父文档）。

封装了发送请求的帧的帧的 ID。如果没有父框架，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。

发出请求的标签页的 ID。如果请求与标签页无关，则设置为 -1。

唯一标识规则的 ID。必需，且应大于等于 1。

规则优先级。默认为1。如果指定，则应 >= 1。

说明应如何执行重定向。仅对重定向规则有效。

ModifyHeaderInfo[] 可选

要针对请求修改的请求标头。仅在 RuleActionType 为“modifyHeaders”时有效。

ModifyHeaderInfo[] 可选

要针对请求修改的响应标头。仅在 RuleActionType 为“modifyHeaders”时有效。

描述在给定的 RuleCondition 匹配时要采取的操作类型。

“允许” 允许网络请求。如果存在与请求匹配的允许规则，则不会拦截该请求。

“upgradeScheme” 如果网络请求网址的架构为 http 或 ftp，则将其升级为 https。

“modifyHeaders” 修改来自网络请求的请求/响应标头。

“allowAllRequests” 允许框架层次结构中的所有请求，包括框架请求本身。

指定网络请求对于其来源网域是第一方还是第三方。如果省略，则接受所有请求。

该规则只会匹配源自 domains 列表中的网络请求。

请改用 excludedInitiatorDomains

该规则将不匹配源自 excludedDomains 列表的网络请求。

该规则将不匹配源自 excludedInitiatorDomains 列表的网络请求。如果此列表为空或被省略，则表示不排除任何网域。此属性的优先级高于 initiatorDomains。

如果网域与 excludedRequestDomains 列表中的某个网域匹配，相应规则将不会匹配网络请求。如果此列表为空或被省略，则表示不排除任何网域。此属性的优先级高于 requestDomains。

规则不会匹配的请求方法列表。应仅指定 requestMethods 和 excludedRequestMethods 中的一项。如果两者均未指定，则匹配所有请求方法。

规则不会匹配的资源类型列表。应仅指定 resourceTypes 和 excludedResourceTypes 中的一项。如果未指定任何一种，则除了“main_frame”之外的所有资源类型都会被屏蔽。

如果请求与此列表中的任何响应标头条件（如果指定）匹配，则规则不匹配。如果同时指定了 excludedResponseHeaders 和 responseHeaders，则 excludedResponseHeaders 属性优先。

规则不应匹配的 tabs.Tab.id 列表。ID 为 tabs.TAB_ID_NONE 会排除并非源自标签页的请求。仅支持会话范围的规则。

该规则将仅匹配源自 initiatorDomains 列表中的网络请求。如果省略此列表，则规则将应用于来自所有网域的请求。不允许使用空列表。

urlFilter 或 regexFilter（以指定者为准）是否区分大小写。默认值为 false。

用于与网络请求网址匹配的正则表达式。此语法遵循 RE2 语法。

注意：只能指定 urlFilter 和 regexFilter 中的一个。

注意：regexFilter 必须仅由 ASCII 字符组成。此格式与以下网址匹配：主机以 Punycode 格式编码（如果是国际化网域），任何其他非 ASCII 字符都以 UTF-8 格式进行网址编码。

仅当网域与 requestDomains 列表中的某个网域匹配时，该规则才会匹配网络请求。如果省略此列表，则规则将应用于来自所有网域的请求。不允许使用空列表。

规则可以匹配的 HTTP 请求方法列表。不允许使用空列表。

注意：指定 requestMethods 规则条件也会排除非 HTTP(s) 请求，而指定 excludedRequestMethods 则不会。

规则可以匹配的资源类型列表。不允许使用空列表。

注意：必须为 allowAllRequests 规则指定此参数，并且只能包含 sub_frame 和 main_frame 资源类型。

如果请求与此列表中的任何响应标头条件（如果指定）匹配，则规则匹配。

规则应匹配的 tabs.Tab.id 列表。ID 为 tabs.TAB_ID_NONE 的请求与不是从标签页发起的请求相匹配。不允许使用空列表。仅支持会话范围的规则。

“|”：左/右锚点：如果用于模式的任一端，则分别指定网址的开头/结尾。

“||”：域名锚点：如果用于模式的开头，则指定网址的（子）网域的开头。

“^”：分隔符字符：匹配除字母、数字或以下字符以外的任何内容：_、-、. 或 %。这也匹配网址的末尾。

因此，urlFilter 由以下部分组成：（可选的左侧/域名锚点）+ 模式 +（可选的右侧锚点）。

如果省略，则匹配所有网址。不允许使用空字符串。

不允许使用以 ||* 开头的格式。请改用 *。

注意：只能指定 urlFilter 和 regexFilter 中的一个。

注意：urlFilter 必须仅由 ASCII 字符组成。此格式与以下网址匹配：主机以 Punycode 格式编码（如果是国际化网域），任何其他非 ASCII 字符都以 UTF-8 格式进行网址编码。例如，当请求网址为 http://abc.рф?q=ф 时，urlFilter 将与网址 http://abc.xn--p1ai/?q=%D1%84 进行匹配。

唯一标识规则集的非空字符串。以“_”开头的 ID 预留供内部使用。

JSON 规则集相对于扩展程序目录的路径。

要将标签页的操作次数增加的量。负值会递减计数。

假设请求的标准 HTTP 方法。对于 HTTP 请求，默认为“get”；对于非 HTTP 请求，则忽略此属性。

假设请求在发送之前未被阻止或重定向，则假设响应提供的标头。表示为将标头名称映射到字符串值列表的对象。如果未指定，假设响应将返回空的响应标头，这可以匹配根据标头不存在情况进行匹配的规则。例如 {"content-type": ["text/html; charset=utf-8", "multipart/form-data"]}

假设请求发生的标签页的 ID。无需与实际标签页 ID 对应。默认值为 -1，表示请求与任何标签页无关。

“syntaxError” 正则表达式的语法不正确，或者使用了 RE2 语法中不提供的功能。

“memoryLimitExceeded” 正则表达式超出了内存上限。

要移除的规则的 ID。系统会忽略所有无效 ID。

与应停用的静态 Ruleset 对应的一组 ID。

与应启用的静态 Ruleset 相对应的一组 ID。

一组与 Ruleset 中的规则对应的 ID，用于停用规则。

要启用的 Ruleset 中规则对应的一组 ID。

请求的新 fragment。应为空（在这种情况下，系统会清除现有 fragment），或以“#”开头。

相应请求的新端口。如果为空，则清除现有端口。

相应请求的新查询。应为空（在这种情况下，系统会清除现有查询），或以“?”开头。

请求的新方案。允许的值包括“http”“https”“ftp”和“chrome-extension”。

可以进行 MAX_GETMATCHEDRULES_CALLS_PER_INTERVAL getMatchedRules 次调用的时间间隔（以分钟为单位）。其他调用会立即失败，并设置 runtime.lastError。注意：与用户手势关联的 getMatchedRules 调用不受配额限制。

扩展程序在其已启用的静态规则集中保证的静态规则的最低数量。超出此限制的任何规则都将计入全局静态规则限制。

在 GETMATCHEDRULES_QUOTA_INTERVAL 时间段内，getMatchedRules 可被调用的次数。

扩展程序一次可启用的静态 Rulesets 数量上限。

扩展程序可添加的正则表达式规则数量上限。此限制会针对动态规则集和规则资源文件中指定的规则分别进行评估。

扩展程序可以指定为 "rule_resources" 清单键的一部分的静态 Rulesets 的最大数量。

扩展程序可以添加的“不安全”动态规则的数量上限。

扩展程序可以添加的“不安全”会话范围规则的数量上限。

由扩展程序添加的会话范围规则的规则集 ID。

返回扩展程序在达到全局静态规则限制之前可以启用的静态规则数量。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回给定 Ruleset 中当前已停用的静态规则列表。

GetDisabledRuleIdsOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回扩展程序的当前动态规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回与扩展程序匹配的所有规则。调用方可以选择性地通过指定 filter 来过滤匹配规则的列表。此方法仅适用于具有 "declarativeNetRequestFeedback" 权限或已针对 filter 中指定的 tabId 授予 "activeTab" 权限的扩展程序。注意：如果规则未与有效文档相关联，且匹配时间超过 5 分钟，则不会返回该规则。

MatchedRulesFilter 可选

Promise<RulesMatchedDetails>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回扩展程序的当前会话范围规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检查给定的正则表达式是否会作为 regexFilter 规则条件受到支持。

IsRegexSupportedResult

Promise<IsRegexSupportedResult>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

配置是否应将标签页的操作次数显示为扩展程序操作的徽章文本，并提供一种递增该操作次数的方法。

ExtensionActionOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检查扩展程序的任何 declarativeNetRequest 规则是否会与假设的请求匹配。注意：此方法仅适用于未打包的扩展程序，因为此方法仅用于扩展程序开发期间。

TestMatchRequestDetails

TestMatchOutcomeResult

Promise<TestMatchOutcomeResult>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

修改扩展程序的当前动态规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

更新扩展程序的已启用静态规则集。系统会先移除 options.disableRulesetIds 中列出的 ID 对应的规则集，然后再添加 options.enableRulesetIds 中列出的规则集。请注意，已启用的静态规则集会在会话之间保持不变，但不会在扩展程序更新之间保持不变，也就是说，rule_resources 清单键将决定每次扩展程序更新时已启用的静态规则集。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

修改扩展程序的当前会话范围规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

停用和启用 Ruleset 中的各个静态规则。对已停用的 Ruleset 所属规则做出的更改将在该 Ruleset 下次启用时生效。

UpdateStaticRulesOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

当规则与请求匹配时触发。仅适用于具有 "declarativeNetRequestFeedback" 权限的未打包扩展程序，因为此 API 仅用于调试目的。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...

  "declarative_net_request" : {
    "rule_resources" : [{
      "id": "ruleset_1",
      "enabled": true,
      "path": "rules_1.json"
    }, {
      "id": "ruleset_2",
      "enabled": false,
      "path": "rules_2.json"
    }]
  },
  "permissions": [
    "declarativeNetRequest",
    "declarativeNetRequestFeedback",
  ],
  "host_permissions": [
    "http://www.blogger.com/*",
    "http://*.google.com/*"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "declarative_net_request" : {
    "rule_resources" : [{
      "id": "ruleset_1",
      "enabled": true,
      "path": "rules_1.json"
    },
    ...
    ]
  }
  ...
}
```

Example 3 (unknown):
```unknown
{
  "id" : 1,
  "priority": 1,
  "action" : { "type" : "block" },
  "condition" : {
    "urlFilter" : "abc",
    "initiatorDomains" : ["foo.com"],
    "resourceTypes" : ["script"]
  }
}
```

Example 4 (unknown):
```unknown
rules_1.json: Rule with id 1 specified a more complext regex than allowed
as part of the "regexFilter" key.
```

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/scripting?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Scripting Extension",
  "manifest_version": 3,
  "permissions": ["scripting", "activeTab"],
  ...
}
```

Example 2 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId()},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected"));
```

Example 3 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), allFrames : true},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected in all frames"));
```

Example 4 (javascript):
```javascript
function getTabId() { ... }

chrome.scripting
    .executeScript({
      target : {tabId : getTabId(), frameIds : [ frameId1, frameId2 ]},
      files : [ "script.js" ],
    })
    .then(() => console.log("script injected on target frames"));
```

---
