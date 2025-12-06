# Chrome-Extensions - Popup Ui

**Pages:** 32

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
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.debugger.onEvent.addListener((source, method, params) => {
  if (method === "Target.attachedToTarget") {
    // `source` identifies the parent session, but we need to construct a new
    // identifier for the child session
    const session = { ...source, sessionId: params.sessionId };

    // Call any needed CDP commands for the child session
    await chrome.debugger.sendCommand(session, "Runtime.enable");
  }
});
```

Example 3 (unknown):
```unknown
await chrome.debugger.sendCommand({ tabId }, "Target.setAutoAttach", {
  autoAttach: true,
  waitForDebuggerOnStart: false,
  flatten: true,
  filter: [{ type: "iframe", exclude: false }]
});
```

Example 4 (unknown):
```unknown
chrome.debugger.attach(  target: Debuggee,  requiredVersion: string,): Promise<void>
```

---

## 添加弹出式窗口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/add-popup?hl=zh-cn

**Contents:**
- 添加弹出式窗口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

弹出式窗口是一种操作，用于显示一个窗口，以便用户调用多个扩展程序功能。该操作可通过键盘快捷键、点击扩展程序的操作图标或调用 chrome.action.openPopup() 触发。当用户将焦点移至弹出式窗口之外的浏览器某个部分时，弹出式窗口会自动关闭。在用户点击关闭后，弹出式窗口无法保持打开状态。

以下图片摘自喝水事件示例，显示了一个显示可用计时器选项的弹出式窗口。用户可以通过点击其中一个按钮设置闹钟。

在清单中的 "action" 键下注册一个弹出式窗口。

实现弹出式窗口的方式与实现几乎任何其他网页的方式一样。请注意，在弹出式窗口中使用的任何 JavaScript 都必须位于单独的文件中。

您还可以通过调用 action.setPopup() 动态创建弹出式窗口。

**Examples:**

Example 1 (unknown):
```unknown
{
 "name": "Drink Water Event",
 ...
 "action": {
   "default_popup": "popup.html"
 }
 ...
}
```

Example 2 (unknown):
```unknown
<html>
 <head>
   <title>Water Popup</title>
 </head>
 <body>
     <img src="./stay_hydrated.png" id="hydrateImage">
     <button id="sampleSecond" value="0.1">Sample Second</button>
     <button id="min15" value="15">15 Minutes</button>
     <button id="min30" value="30">30 Minutes</button>
     <button id="cancelAlarm">Cancel Alarm</button>
   <script src="popup.js"></script>
 </body>
</html>
```

Example 3 (javascript):
```javascript
chrome.storage.local.get('signed_in', (data) => {
  if (data.signed_in) {
    chrome.action.setPopup({popup: 'popup.html'});
  } else {
    chrome.action.setPopup({popup: 'popup_sign_in.html'});
  }
});
```

---

## 添加弹出式窗口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/add-popup

**Contents:**
- 添加弹出式窗口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

弹出式窗口是一种操作，用于显示一个窗口，以便用户调用多个扩展程序功能。该操作可通过键盘快捷键、点击扩展程序的操作图标或调用 chrome.action.openPopup() 触发。当用户将焦点移至弹出式窗口之外的浏览器某个部分时，弹出式窗口会自动关闭。在用户点击关闭后，弹出式窗口无法保持打开状态。

以下图片摘自喝水事件示例，显示了一个显示可用计时器选项的弹出式窗口。用户可以通过点击其中一个按钮设置闹钟。

在清单中的 "action" 键下注册一个弹出式窗口。

实现弹出式窗口的方式与实现几乎任何其他网页的方式一样。请注意，在弹出式窗口中使用的任何 JavaScript 都必须位于单独的文件中。

您还可以通过调用 action.setPopup() 动态创建弹出式窗口。

**Examples:**

Example 1 (unknown):
```unknown
{
 "name": "Drink Water Event",
 ...
 "action": {
   "default_popup": "popup.html"
 }
 ...
}
```

Example 2 (unknown):
```unknown
<html>
 <head>
   <title>Water Popup</title>
 </head>
 <body>
     <img src="./stay_hydrated.png" id="hydrateImage">
     <button id="sampleSecond" value="0.1">Sample Second</button>
     <button id="min15" value="15">15 Minutes</button>
     <button id="min30" value="30">30 Minutes</button>
     <button id="cancelAlarm">Cancel Alarm</button>
   <script src="popup.js"></script>
 </body>
</html>
```

Example 3 (javascript):
```javascript
chrome.storage.local.get('signed_in', (data) => {
  if (data.signed_in) {
    chrome.action.setPopup({popup: 'popup.html'});
  } else {
    chrome.action.setPopup({popup: 'popup_sign_in.html'});
  }
});
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
{
  "name": "My Awesome action Extension",
 ...
  "action": {
   ...
  }
 ...
}
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener((tab) => {
  chrome.action.setTitle({
    tabId: tab.id,
    title: `You are on tab: ${tab.id}`});
});
```

Example 3 (unknown):
```unknown
chrome.action.setBadgeText({text: 'ON'});
chrome.action.setBadgeBackgroundColor({color: '#4688F1'});
```

Example 4 (unknown):
```unknown
{
  "name": "Tab Flipper",
 ...
  "action": {
    "default_title": "Press Ctrl(Win)/Command(Mac)+Shift+Right/Left to flip tabs"
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

---

## chrome.processes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/processes?hl=zh-cn

**Contents:**
- chrome.processes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Cache
    - 属性
  - Process
    - 属性
  - ProcessType

使用 chrome.processes API 与浏览器的进程进行交互。

进程的最新 CPU 使用率测量值，以进程的所有线程使用的单个 CPU 核心总百分比表示。此值介于 0 到 CpuInfo.numOfProcessors*100 之间，在多线程进程中可能会超过 100%。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的 CSS 缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的映像缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程 JavaScript 已分配内存的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程 JavaScript 内存用量的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

Native Client 进程的调试端口。对于其他进程类型以及未启用调试功能的 NaCl 进程，该值为零。

进程网络使用情况的最新测量值，以每秒字节数为单位。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程私有内存用量的最新测量值（以字节为单位）。仅在通过 onUpdatedWithMemory 或 getProcessInfo（使用 includeMemory 标志）的回调接收对象时可用。

进程的脚本缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的 SQLite 内存用量的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

表示在此进程上运行的任务的 TaskInfo 数组。

“service_worker” 已过时，永远不会返回。

可选的标签页 ID（如果此任务表示在渲染器进程上运行的标签页）。

要返回其渲染器进程 ID 的标签页的 ID。

要返回进程信息的进程 ID 列表或单个进程 ID。空列表表示请求所有进程。

如果需要详细的内存用量，则为 True。请注意，收集内存使用情况信息会增加 CPU 使用量，因此仅应在需要时查询。

终止指定的渲染器进程。相当于访问 about:crash，但不会更改标签页的网址。

每次创建进程时触发，提供相应的 Process 对象。

每次进程变得无响应时触发，提供相应的 Process 对象。

每次任务管理器更新其进程统计信息时触发，提供按进程 ID 编入索引的已更新进程对象字典。

每次任务管理器更新其进程统计信息时触发，提供按进程 ID 编入索引的已更新进程对象字典。与 onUpdate 相同，但每个 Process 对象中还包含内存使用情况详细信息。请注意，收集内存使用情况信息会产生额外的 CPU 使用量，因此仅在需要时才应监听。

**Examples:**

Example 1 (unknown):
```unknown
chrome.processes.getProcessIdForTab(  tabId: number,): Promise<number>
```

Example 2 (unknown):
```unknown
chrome.processes.getProcessInfo(  processIds: number | number[],  includeMemory: boolean,): Promise<object>
```

Example 3 (unknown):
```unknown
chrome.processes.terminate(  processId: number,): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.processes.onCreated.addListener(  callback: function,)
```

---

## 通过多功能框触发操作 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/omnibox-triggers

**Contents:**
- 通过多功能框触发操作 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

您可以允许用户通过 Chrome 万能搜索框（通常称为地址栏）与您的扩展程序进行交互。当用户在万能搜索框中输入扩展程序定义的关键字时，您的扩展程序会控制用户在万能搜索框中看到的内容。多功能框新标签页搜索示例扩展程序使用“nt”作为关键字。当用户在 Omnibox 中输入“nt”时，该扩展程序就会启动。为了向用户发出此信号，它会将提供的 16 x 16 图标灰显，并在多功能搜索框中显示在扩展程序名称旁边。

输入的文本会导致 Chrome 向 omnibox.onInputEntered 事件处理脚本发送事件。在处理程序中，该扩展程序会打开一个新标签页，其中包含针对用户条目的 Google 搜索结果。

**Examples:**

Example 1 (javascript):
```javascript
chrome.omnibox.onInputEntered.addListener((text) => {
  // Encode user input for special characters , / ? : @ & = + $ #
  const newURL = `https://www.google.com/search?q=${encodeURIComponent(text)}`;
  chrome.tabs.create({ url: newURL });
});
```

---

## 通知用户 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/notify-users

**Contents:**
- 通知用户 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

使用扩展程序 Notifications API 将消息发布到用户的系统托盘。 首先，在 manifest.json 中声明 "notifications" 权限。

声明权限后，通过调用 notifications.create() 显示通知。以下示例摘自“喝水”事件弹出式窗口示例。它会使用闹钟来设置喝一杯水的提醒。此代码显示了闹钟的触发。点击上一个链接，了解如何设置此功能。

此代码会在 macOS 上创建如下所示的通知。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Drink Water Event Popup",
...
  "permissions": [
    "notifications",
  ],
...
}
```

Example 2 (javascript):
```javascript
chrome.alarms.onAlarm.addListener(() => {
  chrome.action.setBadgeText({ text: '' });
  chrome.notifications.create({
    type: 'basic',
    iconUrl: 'stay_hydrated.png',
    title: 'Time to Hydrate',
    message: "Everyday I'm Guzzlin'!",
    buttons: [{ title: 'Keep it Flowing.' }],
    priority: 0
  });
});
```

---

## 构建上下文菜单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/context-menu

**Contents:**
- 构建上下文菜单 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

鼠标的交替点击（通常称为右键点击）会显示上下文菜单。如需构建上下文菜单，请先向 manifest.json 文件添加 "contextMenus" 权限。

（可选）如果您想在菜单项旁边显示图标，可以使用 "icons" 键。在本例中，“Global Google Search”（全球 Google 搜索）对应的菜单项扩展程序使用 16x16 的图标。

此示例的其余部分取自全球 Google 搜索上下文菜单示例，该示例提供了多个上下文菜单选项。当一个扩展程序包含多个上下文菜单时，Chrome 会自动将它们折叠为一个父级菜单，如下所示：

该示例通过在 Extension Service Worker 中调用 contextMenus.create() 展示了这种情况。子菜单项是从 locales.js 文件导入的。然后，runtime.onInstalled 会迭代它们。

**Examples:**

Example 1 (unknown):
```unknown
"permissions": [
    "contextMenus"
  ],
```

Example 2 (javascript):
```javascript
const tldLocales = {
  'com.au': 'Australia',
  'com.br': 'Brazil',
  ...
}

chrome.runtime.onInstalled.addListener(async () => {
  for (let [tld, locale] of Object.entries(tldLocales)) {
    chrome.contextMenus.create({
      id: tld,
      title: locale,
      type: 'normal',
      contexts: ['selection'],
    });
  }
});
```

---

## 使用 Notifications API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/notifications

**Contents:**
- 使用 Notifications API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 显示方式
- 行为方式
- 开发方法
  - 创建基本通知
  - 使用图片
  - 创建列表通知
- 监听和响应事件

借助 chrome.notifications API，您可以使用模板创建通知并显示这些通知 通知：

内容丰富的通知有四种不同的类型：基本通知、图片通知、列表通知和进度通知。全部 通知包括标题、消息和显示在通知左侧的小图标 消息和一个 contextMessage 字段（以浅色字体显示为第三个文本字段）。

在 ChromeOS 中，通知会显示在用户的系统任务栏中，并且在系统任务栏中 用户将其关闭系统任务栏会保留所有新通知的计数。用户看到 通知，计数会重置为零。

可以为通知指定 -2 到 2 之间的优先级。小于 0 的优先级会显示在 ChromeOS 中 并在其他平台上产生错误。默认优先级为 0。 优先级大于 0 时，系统会根据增加的时长显示优先级；系统可能会显示更多高优先级通知 。

priority 设置不会影响 macOS 上的通知顺序。

除了显示信息外，所有通知类型还可以包含最多两个操作项。 当用户点击待办项时，您的扩展程序可以使用适当的操作作为响应。例如： 当用户点击回复时，电子邮件应用会打开，并且用户可以完成回复：

如需使用此 API，请调用 notifications.create() 方法，并使用 options 参数：

notifications.NotificationOptions 必须包含 notifications.TemplateType， 定义了可用的通知详情以及这些详情的显示方式。

所有模板类型（basic、image、list 和 progress）都必须包含通知 title，并且 message，以及 iconUrl（指向显示在 通知消息。

image 模板类型还包含 imageUrl，它是指向预览图片的链接 。请注意，使用 macOS 的用户不会看到映像。

list 模板以列表格式显示 items。请注意，macOS 用户只会看到第一项。

所有通知都可以包含响应用户操作的事件监听器和事件处理程序（请参阅 chrome.events）。例如，您可以编写一个事件处理脚本来响应 notifications.onButtonClicked 事件。

考虑在 Service Worker 中加入事件监听器和处理程序， 。

**Examples:**

Example 1 (unknown):
```unknown
await chrome.notifications.create(id, options);
```

Example 2 (unknown):
```unknown
var opt = {
  type: "basic",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon"
}
```

Example 3 (unknown):
```unknown
var opt = {
  type: "image",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  imageUrl: "url_to_preview_image"
}
```

Example 4 (unknown):
```unknown
var opt = {
  type: "list",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  items: [{ title: "Item1", message: "This is item 1."},
          { title: "Item2", message: "This is item 2."},
          { title: "Item3", message: "This is item 3."}]
}```

### Create progress notification {: #progress }

The `progress` template displays a progress bar where current progress ranges from 0 to 100. On macOS the progress bar displays as a percentage value in the notification title instead of in the progress bar.

```js
var opt = {
  type: "progress",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  progress: 42
}
```

---

## 使用 Notifications API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/notifications?hl=zh-cn

**Contents:**
- 使用 Notifications API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 显示方式
- 行为方式
- 开发方法
  - 创建基本通知
  - 使用图片
  - 创建列表通知
- 监听和响应事件

借助 chrome.notifications API，您可以使用模板创建通知并显示这些通知 通知：

内容丰富的通知有四种不同的类型：基本通知、图片通知、列表通知和进度通知。全部 通知包括标题、消息和显示在通知左侧的小图标 消息和一个 contextMessage 字段（以浅色字体显示为第三个文本字段）。

在 ChromeOS 中，通知会显示在用户的系统任务栏中，并且在系统任务栏中 用户将其关闭系统任务栏会保留所有新通知的计数。用户看到 通知，计数会重置为零。

可以为通知指定 -2 到 2 之间的优先级。小于 0 的优先级会显示在 ChromeOS 中 并在其他平台上产生错误。默认优先级为 0。 优先级大于 0 时，系统会根据增加的时长显示优先级；系统可能会显示更多高优先级通知 。

priority 设置不会影响 macOS 上的通知顺序。

除了显示信息外，所有通知类型还可以包含最多两个操作项。 当用户点击待办项时，您的扩展程序可以使用适当的操作作为响应。例如： 当用户点击回复时，电子邮件应用会打开，并且用户可以完成回复：

如需使用此 API，请调用 notifications.create() 方法，并使用 options 参数：

notifications.NotificationOptions 必须包含 notifications.TemplateType， 定义了可用的通知详情以及这些详情的显示方式。

所有模板类型（basic、image、list 和 progress）都必须包含通知 title，并且 message，以及 iconUrl（指向显示在 通知消息。

image 模板类型还包含 imageUrl，它是指向预览图片的链接 。请注意，使用 macOS 的用户不会看到映像。

list 模板以列表格式显示 items。请注意，macOS 用户只会看到第一项。

所有通知都可以包含响应用户操作的事件监听器和事件处理程序（请参阅 chrome.events）。例如，您可以编写一个事件处理脚本来响应 notifications.onButtonClicked 事件。

考虑在 Service Worker 中加入事件监听器和处理程序， 。

**Examples:**

Example 1 (unknown):
```unknown
await chrome.notifications.create(id, options);
```

Example 2 (unknown):
```unknown
var opt = {
  type: "basic",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon"
}
```

Example 3 (unknown):
```unknown
var opt = {
  type: "image",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  imageUrl: "url_to_preview_image"
}
```

Example 4 (unknown):
```unknown
var opt = {
  type: "list",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  items: [{ title: "Item1", message: "This is item 1."},
          { title: "Item2", message: "This is item 2."},
          { title: "Item3", message: "This is item 3."}]
}```

### Create progress notification {: #progress }

The `progress` template displays a progress bar where current progress ranges from 0 to 100. On macOS the progress bar displays as a percentage value in the notification title instead of in the progress bar.

```js
var opt = {
  type: "progress",
  title: "Primary Title",
  message: "Primary message to display",
  iconUrl: "url_to_small_icon",
  progress: 42
}
```

---

## 本地化消息格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/localization-message-formats?hl=zh-cn

**Contents:**
- 本地化消息格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 字段摘要
- 示例
- 字段详情
  - name
  - 消息
  - 说明
  - 占位符

每个经过国际化扩展程序都至少有一个名为 messages.json 的文件，用于提供特定于语言区域的字符串。本页面介绍了 messages.json 文件的格式。如需了解 请参阅国际化页面。

以下代码显示了 messages.json 支持的字段。只有“name”和“message”字段是必填字段。

下面是一个 messages.json 文件，其中定义了三条名为“prompt_for_name”“hello”和 "再见"：

本部分介绍了可以出现在 messages.json 文件中的各个字段。如需详细了解 消息文件 - 例如，当语言区域未定义所有消息时会出现什么情况，请参阅 国际化。

抱歉，没有名为“name”的字段。此字段的名称是消息的名称，即您在 __MSG__name___ 或 getMessage("_name_") 中看到的名称。

该名称是一个不区分大小写的键，可让您检索本地化的消息文本。该名称 中包含以下字符：

以下是 Example 部分中的三个名称示例：

如需查看使用姓名的更多示例，请参阅国际化页面。

已翻译的消息，采用字符串形式，其中可以包含占位符。使用 $_placeholder_name_$（不区分大小写），用于表示特定占位符。例如，您可以 会引用名为“our_site”的占位符为 $our_site$、$OUR_SITE$ 或 $oUR_sITe$。

以下是 Example 部分中的三个消息示例：

如需在字符串中添加美元符号 ($)，请使用 $$. For example, use the following code to specify the message Amount (in $):

尽管占位符（如 $USER$）是指代替换字符串的首选方式 （使用 i18n.getMessage 的 substitutions 参数指定的字符串）您还可以参考 直接在消息中替换字符串。例如，以下消息引用传入 getMessage() 的前三个替换字符串：

尽管如此，我们建议您在消息中始终使用占位符，而不是 $_n_ 字符串。您可以将占位符视为合适的变量名称。在编写代码一周后，您可能就会忘记 $1 的含义，但您会知道占位符的含义。如需详细了解占位符和替换字符串，请参阅占位符部分。

可选。邮件的说明，旨在提供背景信息或详细信息，以帮助译者尽可能提供最准确的译文。

可选。定义要在消息中使用的一个或多个子字符串。以下是您可能需要使用占位符的两个原因：

每个占位符都有一个名称、“content”项和一个可选的“example”项。占位符的名称 不区分大小写，且包含与消息名称相同的字符。

“内容”商品的值是一个字符串，可引用指定的替换字符串 使用 i18n.getMessage 方法的 substitutions 参数。“内容”值项目是 通常为“Example.com”或“$1”。如果您引用了不存在的替换字符串，则会收到空字符串。下表显示了 $_n_ 字符串与字符串的对应关系 由 substitutions 参数指定。

“示例”项（可选，但强烈建议提供）可显示内容在最终用户眼中的呈现方式，从而帮助译者。例如，美元金额的占位符应该有如下示例： "$23.45"。

以下代码段摘自示例部分，显示了一个“占位符”项，其中包含两个名为“our_site”和“user”的占位符。“our_site”占位符没有“example” 项，因为从“content”级别可以明显看出它的值字段。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": {
    "message": "Message text, with optional placeholders.",
    "description": "Translator-aimed description of the message.",
    "placeholders": {
      "placeholder_name": {
        "content": "A string to be placed within the message.",
        "example": "Translator-aimed example of the placeholder string."
      },
      ...
    }
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  "prompt_for_name": {
    "message": "What's your name?",
    "description": "Ask for the user's name"
  },
  "hello": {
    "message": "Hello, $USER$",
    "description": "Greet the user",
    "placeholders": {
      "user": {
        "content": "$1",
        "example": "Cira"
      }
    }
  },
  "bye": {
    "message": "Goodbye, $USER$. Come back to $OUR_SITE$ soon!",
    "description": "Say goodbye to the user",
    "placeholders": {
      "our_site": {
        "content": "Example.com",
      },
      "user": {
        "content": "$1",
        "example": "Cira"
      }
    }
  }
}
```

Example 3 (unknown):
```unknown
"prompt_for_name": {
  ...
},
"hello": {
  ...
},
"bye": {
  ...
}
```

Example 4 (unknown):
```unknown
"message": "What's your name?"
...
"message": "Hello, $USER$"
...
"message": "Goodbye, $USER$. Come back to $OUR_SITE$ soon!"
```

---

## 本地化消息格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/localization-message-formats

**Contents:**
- 本地化消息格式 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 字段摘要
- 示例
- 字段详情
  - name
  - 消息
  - 说明
  - 占位符

每个经过国际化扩展程序都至少有一个名为 messages.json 的文件，用于提供特定于语言区域的字符串。本页面介绍了 messages.json 文件的格式。如需了解 请参阅国际化页面。

以下代码显示了 messages.json 支持的字段。只有“name”和“message”字段是必填字段。

下面是一个 messages.json 文件，其中定义了三条名为“prompt_for_name”“hello”和 "再见"：

本部分介绍了可以出现在 messages.json 文件中的各个字段。如需详细了解 消息文件 - 例如，当语言区域未定义所有消息时会出现什么情况，请参阅 国际化。

抱歉，没有名为“name”的字段。此字段的名称是消息的名称，即您在 __MSG__name___ 或 getMessage("_name_") 中看到的名称。

该名称是一个不区分大小写的键，可让您检索本地化的消息文本。该名称 中包含以下字符：

以下是 Example 部分中的三个名称示例：

如需查看使用姓名的更多示例，请参阅国际化页面。

已翻译的消息，采用字符串形式，其中可以包含占位符。使用 $_placeholder_name_$（不区分大小写），用于表示特定占位符。例如，您可以 会引用名为“our_site”的占位符为 $our_site$、$OUR_SITE$ 或 $oUR_sITe$。

以下是 Example 部分中的三个消息示例：

如需在字符串中添加美元符号 ($)，请使用 $$. For example, use the following code to specify the message Amount (in $):

尽管占位符（如 $USER$）是指代替换字符串的首选方式 （使用 i18n.getMessage 的 substitutions 参数指定的字符串）您还可以参考 直接在消息中替换字符串。例如，以下消息引用传入 getMessage() 的前三个替换字符串：

尽管如此，我们建议您在消息中始终使用占位符，而不是 $_n_ 字符串。您可以将占位符视为合适的变量名称。在编写代码一周后，您可能就会忘记 $1 的含义，但您会知道占位符的含义。如需详细了解占位符和替换字符串，请参阅占位符部分。

可选。邮件的说明，旨在提供背景信息或详细信息，以帮助译者尽可能提供最准确的译文。

可选。定义要在消息中使用的一个或多个子字符串。以下是您可能需要使用占位符的两个原因：

每个占位符都有一个名称、“content”项和一个可选的“example”项。占位符的名称 不区分大小写，且包含与消息名称相同的字符。

“内容”商品的值是一个字符串，可引用指定的替换字符串 使用 i18n.getMessage 方法的 substitutions 参数。“内容”值项目是 通常为“Example.com”或“$1”。如果您引用了不存在的替换字符串，则会收到空字符串。下表显示了 $_n_ 字符串与字符串的对应关系 由 substitutions 参数指定。

“示例”项（可选，但强烈建议提供）可显示内容在最终用户眼中的呈现方式，从而帮助译者。例如，美元金额的占位符应该有如下示例： "$23.45"。

以下代码段摘自示例部分，显示了一个“占位符”项，其中包含两个名为“our_site”和“user”的占位符。“our_site”占位符没有“example” 项，因为从“content”级别可以明显看出它的值字段。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": {
    "message": "Message text, with optional placeholders.",
    "description": "Translator-aimed description of the message.",
    "placeholders": {
      "placeholder_name": {
        "content": "A string to be placed within the message.",
        "example": "Translator-aimed example of the placeholder string."
      },
      ...
    }
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  "prompt_for_name": {
    "message": "What's your name?",
    "description": "Ask for the user's name"
  },
  "hello": {
    "message": "Hello, $USER$",
    "description": "Greet the user",
    "placeholders": {
      "user": {
        "content": "$1",
        "example": "Cira"
      }
    }
  },
  "bye": {
    "message": "Goodbye, $USER$. Come back to $OUR_SITE$ soon!",
    "description": "Say goodbye to the user",
    "placeholders": {
      "our_site": {
        "content": "Example.com",
      },
      "user": {
        "content": "$1",
        "example": "Cira"
      }
    }
  }
}
```

Example 3 (unknown):
```unknown
"prompt_for_name": {
  ...
},
"hello": {
  ...
},
"bye": {
  ...
}
```

Example 4 (unknown):
```unknown
"message": "What's your name?"
...
"message": "Hello, $USER$"
...
"message": "Goodbye, $USER$. Come back to $OUR_SITE$ soon!"
```

---

## 为用户提供选项 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/options-page?hl=zh-cn

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

## chrome.pageCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/pageCapture

**Contents:**
- chrome.pageCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 方法
  - saveAsMHTML()
    - 参数
    - 返回

使用 chrome.pageCapture API 将标签页另存为 MHTML。

MHTML 是一种标准格式，大多数浏览器都支持这种格式。它将网页及其所有资源（CSS 文件、图片等）封装在一个文件中。

请注意，出于安全考虑，MHTML 文件只能从文件系统加载，并且只能在主框架中加载。

您必须在扩展程序清单中声明“pageCapture”权限，才能使用 pageCapture API。例如：

将具有指定 ID 的标签页的内容保存为 MHTML。

Promise<Blob | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "pageCapture"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.pageCapture.saveAsMHTML(  details: object,): Promise<Blob | undefined>
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
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.debugger.onEvent.addListener((source, method, params) => {
  if (method === "Target.attachedToTarget") {
    // `source` identifies the parent session, but we need to construct a new
    // identifier for the child session
    const session = { ...source, sessionId: params.sessionId };

    // Call any needed CDP commands for the child session
    await chrome.debugger.sendCommand(session, "Runtime.enable");
  }
});
```

Example 3 (unknown):
```unknown
await chrome.debugger.sendCommand({ tabId }, "Target.setAutoAttach", {
  autoAttach: true,
  waitForDebuggerOnStart: false,
  flatten: true,
  filter: [{ type: "iframe", exclude: false }]
});
```

Example 4 (unknown):
```unknown
chrome.debugger.attach(  target: Debuggee,  requiredVersion: string,): Promise<void>
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
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.debugger.onEvent.addListener((source, method, params) => {
  if (method === "Target.attachedToTarget") {
    // `source` identifies the parent session, but we need to construct a new
    // identifier for the child session
    const session = { ...source, sessionId: params.sessionId };

    // Call any needed CDP commands for the child session
    await chrome.debugger.sendCommand(session, "Runtime.enable");
  }
});
```

Example 3 (unknown):
```unknown
await chrome.debugger.sendCommand({ tabId }, "Target.setAutoAttach", {
  autoAttach: true,
  waitForDebuggerOnStart: false,
  flatten: true,
  filter: [{ type: "iframe", exclude: false }]
});
```

Example 4 (unknown):
```unknown
chrome.debugger.attach(  target: Debuggee,  requiredVersion: string,): Promise<void>
```

---

## 国际化接口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/i18n

**Contents:**
- 国际化接口 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

使用 chrome.i18nAPI 执行以下操作： 国际化您的扩展程序首先创建要存储的目录 _locales/ 文件夹中特定语言的消息文件。例如：

每个 messages.json 文件都将包含由键标识的本地化字符串。对于 例如，以下代码会对 _locales/en/messages.json 的提示进行本地化。 此字符串的键为 __MSG_tooltip__。

您将在 manifest.json 内使用此密钥代替 "default_title"。

**Examples:**

Example 1 (unknown):
```unknown
_locales/en/messages.json
_locales/es/messages.json
```

Example 2 (unknown):
```unknown
{
  "__MSG_tooltip__": {
   "message": "Hello!",
   "description": "Tooltip"
 }
}
```

Example 3 (unknown):
```unknown
{
  "name": "Tab Flipper",
 ...
  "action": {
    "default_title": "__MSG_tooltip__"
  },
  "default_locale": "en"
 ...
}
```

---

## 什么是主题？ 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/themes?hl=zh-cn

**Contents:**
- 什么是主题？ 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
  - 颜色
  - 图片
  - 媒体资源
  - 色调

主题背景是一种用于更改浏览器外观的特殊扩展程序。主题为 与常规扩展程序一样打包，但不包含 JavaScript 或 HTML 代码。

您可通过与扩展程序相同的过程将主题上传到 Chrome 应用商店。在上传过程中，系统会要求您选择一个类别。您可在 Chrome 应用商店文档中的最佳实践下找到主题类别列表。

您可在 Chrome 应用商店中找到并试用各种主题背景。

以下是主题的 manifest.json 文件示例：

颜色采用 RGB 格式。要查找字符串，您可以在“colors”字段，请参阅 kOverwritableColorTable。

图片资源使用相对于扩展程序根目录的路径。您可以替换任何映像 由 kPersistingImages 中的字符串指定。所有图片都必须以 PNG 格式存储 格式的网址，否则它们将无法正常呈现。

通过此字段，您可以指定背景对齐、背景重复和 备用徽标。如需查看它们可以采用的属性和值，请参阅 kDisplayProperties。

您可以指定要应用于界面的各个部分（例如按钮、画面和 背景标签页。Google Chrome 支持色调调节，但不支持图片，因为图片无法跨平台使用 因为添加新按钮时会变得很脆弱要查找字符串，您可以在 “色调”字段，请参阅 kTintTable。

着色采用色相-饱和度-亮度 (HSL) 格式，使用 0 - 范围内的浮点数 1.0：

或者，您也可以将 -1.0 用于任何 HSL 值，以指定没有变化。

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "version": "2.6",
  "name": "camo theme",
  "theme": {
    "images" : {
      "theme_frame" : "images/theme_frame_camo.png",
      "theme_frame_overlay" : "images/theme_frame_stripe.png",
      "theme_toolbar" : "images/theme_toolbar_camo.png",
      "theme_ntp_background" : "images/theme_ntp_background_norepeat.png",
      "theme_ntp_attribution" : "images/attribution.png"
    },
    "colors" : {
      "frame" : [71, 105, 91],
      "toolbar" : [207, 221, 192],
      "ntp_text" : [20, 40, 0],
      "ntp_link" : [36, 70, 0],
      "ntp_section" : [207, 221, 192],
      "button_background" : [255, 255, 255]
    },
    "tints" : {
      "buttons" : [0.33, 0.5, 0.47]
    },
    "properties" : {
      "ntp_background_alignment" : "bottom"
    }
  }
}
```

---

## 支持无障碍功能 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/a11y?hl=zh-cn

**Contents:**
- 支持无障碍功能 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 集成无障碍界面控件
  - 标准控件
  - 自定义控件中的 WAI-ARIA
  - 专注于自定义控件
- 支持键盘访问
  - 导航
  - 快捷键
- 提供无障碍内容
  - 文本

扩展程序可让用户根据个人的使用需求打造理想的浏览体验 能力和偏好。扩展程序应包含可鼓励 可以帮助有视力障碍、听力障碍、精细动作失能和 其他残障人士也可以访问该扩展程序。

所有人，不只是有特殊需求的用户，都可以从无障碍功能中受益。视力 残疾、灵敏度低和高级用户都可以从键盘快捷键中受益。字幕和 转写文稿对失聪用户必不可少，但对语言学习者也有帮助。

用户可通过多种方式与扩展程序互动。有些用户使用的是标准显示器 键盘和鼠标 - 或者可能需要屏幕放大镜，也可能是屏幕阅读器。 虽然无法预测用户会使用哪些工具访问扩展程序，但还是可以采取一些步骤 使扩展程序尽可能易于访问。

如果用户无法访问界面控件，则无法使用扩展程序。最简单 创建无障碍界面的方法是使用标准 HTML 控件。

请尽可能使用标准 HTML 界面控件。标准 HTML 控件是键盘 易于访问、易于扩展，并且通常能被屏幕阅读器理解。

网络无障碍计划 - 无障碍丰富互联网应用 (WAI-ARIA) 是一项 关于让屏幕阅读器可通过一组标准的 DOM 访问界面控件的规范 属性。这些属性可向屏幕阅读器提供有关函数和当前的信息 控件状态

要向自定义控件添加 WAI-ARIA 支持，扩展程序的 DOM 元素必须为 已修改为包含 Chrome 在用户互动期间引发事件的属性。屏幕阅读器 并说明这些控件的功能。DOM 属性 WAI-ARIA 分为角色、状态和属性。

aria-activedescendant 属性指定在 获得焦点。代码 tabindex="0" 指定工具栏在 文档顺序。

将 WAI-ARIA 角色、状态和属性添加到控件的 DOM 后， 将相应的事件提供给屏幕阅读器。由于 WAI-ARIA 支持仍在进行中， Google Chrome 可能不会为每个 WAI-ARIA 属性都引发事件，屏幕阅读器也可能不会 并识别所有引发的事件。

有关将 WAI-ARIA 控件添加到自定义控件的快速教程，请参阅 Dave Raggett 的 来自 WWW2010 的演示文稿。

对于不使用鼠标浏览网页的用户，键盘焦点至关重要。请确保操作和 导航控件（例如按钮、列表框和菜单栏）可以获得键盘焦点。

默认情况下，HTML DOM 中能接收键盘焦点的唯一元素是锚点、按钮、 和表单控件不过，将 HTML 属性 tabIndex 设置为 0 会将 DOM 元素放置在 默认 Tab 键序列，使其能够接收到键盘焦点。

设置 tabIndex = -1 会从标签页序列中移除该元素，但仍允许该元素执行以下操作： 以编程方式接收键盘焦点。

扩展程序应该只通过键盘即可使用，方便无法使用鼠标的用户，而且 那些根本不想访问应用的用户。

检查用户能否在不使用鼠标的情况下在扩展程序的不同部分之间导航。 检查确保使用任何弹出式窗口时都可通过键盘导航。使用 Chrome 键盘快捷键执行以下操作： 确定扩展程序是否可导航。

确保用户能够轻松查看界面的哪些部分获得键盘焦点。通常是焦点轮廓 但如果过度使用 CSS，轮廓就可能被隐藏 把对比度降低。

最常用的键盘导航策略是使用 Tab 键来旋转焦点 但这并不总是最简单或最高效的选项。

一个简单的 JavaScript 键盘处理程序可能如下所示。请注意 WAI-ARIA 属性 aria-activedescendant 会根据用户输入进行更新，以反映当前处于活动状态的工具栏 按钮。

扩展程序可以为重要的扩展程序界面元素创建明确的键盘快捷键。为了实现 这些快捷键可将键盘事件监听器连接到控件。让用户知道 在选项页面中提供快捷方式。

提供方便用户查看的内容对所有用户而言都至关重要。以下指南中有很多可能听起来 因为它们反映了适用于所有网络内容的最佳实践。

字体选择和文字大小会影响扩展程序内容的可读性。有视力障碍的用户 可能需要增加扩展程序的文字大小。如果使用键盘快捷键，请确保这些快捷键不是 干扰 Chrome 中内置的缩放快捷方式。

采用 200% 测试作为扩展程序界面灵活性的指标；文字大小或 网页缩放增加了 200%，是否仍然可用？

避免将文本烘焙成图片。用户无法修改尺寸，屏幕阅读器也无法修改 来解读图像。您可以选用自定样式的网页字体，例如 Google Font API。网络字体可以缩放到不同的大小，并且可供使用屏幕的人访问 读者。

附加信息中的背景颜色和文字颜色之间应有足够明显的对比。使用 对比度检查工具，用于测试背景颜色和前景色是否提供 采用适当的对比度

评估对比度时，请验证附加信息中依赖图形来传达的各个部分 信息。对于特定图片，可使用Coblis - 色盲等工具 模拟器可用于查看图片在各种形式的色缺陷下的显示效果。

考虑提供不同的颜色主题，或允许用户自定义颜色 以便形成更好的对比度

如果扩展程序依靠声音或视频传达信息，请确保相应扩展程序 有转写文稿。有关详情，请参阅描述和带字幕的媒体计划准则 了解有关图片说明的信息。

使用替代文本来陈述图片的用途，而不是对内容进行文字说明 图像。间隔图片或纯装饰性图片应使用空白的 "" 替代文本，否则应将其移除 并放入 CSS 中。

如果扩展程序必须使用图片中的文字，请在替代文字中添加图片文字。实用资源 参阅有关相应替代文本的 WebAIM 文章。

如需详细了解 Chrome 中的无障碍功能，请访问 A11ycasts 频道并阅读 参阅 Chromium 无障碍功能技术文档。

**Examples:**

Example 1 (unknown):
```unknown
<div role="toolbar">
```

Example 2 (unknown):
```unknown
<div role="toolbar" tabindex="0" aria-activedescendant="button1">
  <img src="buttoncut.png" role="button" alt="cut" id="button1">
  <img src="buttoncopy.png" role="button" alt="copy" id="button2">
  <img src="buttonpaste.png" role="button" alt="paste" id="button3">
</div>
```

Example 3 (unknown):
```unknown
element.tabIndex = 0
```

Example 4 (unknown):
```unknown
element.focus();
```

---

## 为用户提供选项 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/options-page

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

## 界面组件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui

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

## chrome.processes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/processes

**Contents:**
- chrome.processes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Cache
    - 属性
  - Process
    - 属性
  - ProcessType

使用 chrome.processes API 与浏览器的进程进行交互。

进程的最新 CPU 使用率测量值，以进程的所有线程使用的单个 CPU 核心总百分比表示。此值介于 0 到 CpuInfo.numOfProcessors*100 之间，在多线程进程中可能会超过 100%。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的 CSS 缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的映像缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程 JavaScript 已分配内存的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程 JavaScript 内存用量的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

Native Client 进程的调试端口。对于其他进程类型以及未启用调试功能的 NaCl 进程，该值为零。

进程网络使用情况的最新测量值，以每秒字节数为单位。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程私有内存用量的最新测量值（以字节为单位）。仅在通过 onUpdatedWithMemory 或 getProcessInfo（使用 includeMemory 标志）的回调接收对象时可用。

进程的脚本缓存的最新信息。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

进程的 SQLite 内存用量的最新测量值（以字节为单位）。仅在通过 onUpdated 或 onUpdatedWithMemory 的回调接收对象时可用。

表示在此进程上运行的任务的 TaskInfo 数组。

“service_worker” 已过时，永远不会返回。

可选的标签页 ID（如果此任务表示在渲染器进程上运行的标签页）。

要返回其渲染器进程 ID 的标签页的 ID。

要返回进程信息的进程 ID 列表或单个进程 ID。空列表表示请求所有进程。

如果需要详细的内存用量，则为 True。请注意，收集内存使用情况信息会增加 CPU 使用量，因此仅应在需要时查询。

终止指定的渲染器进程。相当于访问 about:crash，但不会更改标签页的网址。

每次创建进程时触发，提供相应的 Process 对象。

每次进程变得无响应时触发，提供相应的 Process 对象。

每次任务管理器更新其进程统计信息时触发，提供按进程 ID 编入索引的已更新进程对象字典。

每次任务管理器更新其进程统计信息时触发，提供按进程 ID 编入索引的已更新进程对象字典。与 onUpdate 相同，但每个 Process 对象中还包含内存使用情况详细信息。请注意，收集内存使用情况信息会产生额外的 CPU 使用量，因此仅在需要时才应监听。

**Examples:**

Example 1 (unknown):
```unknown
chrome.processes.getProcessIdForTab(  tabId: number,): Promise<number>
```

Example 2 (unknown):
```unknown
chrome.processes.getProcessInfo(  processIds: number | number[],  includeMemory: boolean,): Promise<object>
```

Example 3 (unknown):
```unknown
chrome.processes.terminate(  processId: number,): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.processes.onCreated.addListener(  callback: function,)
```

---

## 使您的扩展程序可供访问 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/a11y?hl=zh-cn

**Contents:**
- 使您的扩展程序可供访问 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

对许多用户而言，无障碍功能实际上就是界面，而对于那些不需要将无障碍功能作为与扩展程序互动的主要途径的用户而言，无障碍功能往往非常实用。这些技术多种多样。至少要有高对比度文字。视频应带有字幕。图片应包含 alt 属性。

不过，正如我们前面所说，这只是最低要求。下文介绍了其他方法。

有几种方法可以实现无障碍功能，但最简单的方法是使用标准 HTML 控件，尤其是输入元素。下图显示了这些控件。

如需使其他元素可供访问，请使用 ARIA 属性。这些属性可向屏幕阅读器提供有关网页上控件的功能和当前状态的信息。这里给出了一个示例，

默认情况下，在 HTML DOM 中，唯一可以接收键盘焦点的元素为锚点、按钮和表单控件。幸运的是，在 HTML 元素上设置 tabIndex 属性可使其获得键盘焦点。例如：

如需了解如何实现这些技巧以及其他内容，请参阅支持无障碍功能。

**Examples:**

Example 1 (unknown):
```unknown
<div role="toolbar" tabindex="0" aria-activedescendant="button1">
  <img src="buttoncut.png" role="button" alt="cut" id="button1">
  <img src="buttoncopy.png" role="button" alt="copy" id="button2">
  <img src="buttonpaste.png" role="button" alt="paste" id="button3">
</div>
```

Example 2 (unknown):
```unknown
<div tabindex="0">I can receive focus with the tab key.</div>
```

---

## 响应命令 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/respond-to-commands

**Contents:**
- 响应命令 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

命令是调用扩展程序功能的按键组合。注册命令 （位于清单中的 "commands" 键下）。例如：

此组合键会触发 commands.onCommand 事件中的 Service Worker。

要查看响应命令的实际效果，请下载 Tab Flipper 示例并将其加载（解压缩）。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Open developer.chrome.com",
  "version": "0.1",
  "manifest_version": 3,
  "description": "Opens developer.chrome.com when you use Cmd/Ctrl + Shift + Z",
  "background": {
    "service_worker": "background.js"
  },
  "commands": {
   "open-tab": {
     "suggested_key": {
       "default": "Ctrl+Shift+Z",
       "mac": "Command+Shift+Z"
     },
     "description": "Open developer.chrome.com"
   }
  }
}
```

Example 2 (javascript):
```javascript
chrome.commands.onCommand.addListener((command) => {
  if (command !== "open-tab") return;
  chrome.tabs.create({ url: "https://developer.chrome.com" });
});
```

---

## 支持无障碍功能 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/ui/a11y

**Contents:**
- 支持无障碍功能 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 集成无障碍界面控件
  - 标准控件
  - 自定义控件中的 WAI-ARIA
  - 专注于自定义控件
- 支持键盘访问
  - 导航
  - 快捷键
- 提供无障碍内容
  - 文本

扩展程序可让用户根据个人的使用需求打造理想的浏览体验 能力和偏好。扩展程序应包含可鼓励 可以帮助有视力障碍、听力障碍、精细动作失能和 其他残障人士也可以访问该扩展程序。

所有人，不只是有特殊需求的用户，都可以从无障碍功能中受益。视力 残疾、灵敏度低和高级用户都可以从键盘快捷键中受益。字幕和 转写文稿对失聪用户必不可少，但对语言学习者也有帮助。

用户可通过多种方式与扩展程序互动。有些用户使用的是标准显示器 键盘和鼠标 - 或者可能需要屏幕放大镜，也可能是屏幕阅读器。 虽然无法预测用户会使用哪些工具访问扩展程序，但还是可以采取一些步骤 使扩展程序尽可能易于访问。

如果用户无法访问界面控件，则无法使用扩展程序。最简单 创建无障碍界面的方法是使用标准 HTML 控件。

请尽可能使用标准 HTML 界面控件。标准 HTML 控件是键盘 易于访问、易于扩展，并且通常能被屏幕阅读器理解。

网络无障碍计划 - 无障碍丰富互联网应用 (WAI-ARIA) 是一项 关于让屏幕阅读器可通过一组标准的 DOM 访问界面控件的规范 属性。这些属性可向屏幕阅读器提供有关函数和当前的信息 控件状态

要向自定义控件添加 WAI-ARIA 支持，扩展程序的 DOM 元素必须为 已修改为包含 Chrome 在用户互动期间引发事件的属性。屏幕阅读器 并说明这些控件的功能。DOM 属性 WAI-ARIA 分为角色、状态和属性。

aria-activedescendant 属性指定在 获得焦点。代码 tabindex="0" 指定工具栏在 文档顺序。

将 WAI-ARIA 角色、状态和属性添加到控件的 DOM 后， 将相应的事件提供给屏幕阅读器。由于 WAI-ARIA 支持仍在进行中， Google Chrome 可能不会为每个 WAI-ARIA 属性都引发事件，屏幕阅读器也可能不会 并识别所有引发的事件。

有关将 WAI-ARIA 控件添加到自定义控件的快速教程，请参阅 Dave Raggett 的 来自 WWW2010 的演示文稿。

对于不使用鼠标浏览网页的用户，键盘焦点至关重要。请确保操作和 导航控件（例如按钮、列表框和菜单栏）可以获得键盘焦点。

默认情况下，HTML DOM 中能接收键盘焦点的唯一元素是锚点、按钮、 和表单控件不过，将 HTML 属性 tabIndex 设置为 0 会将 DOM 元素放置在 默认 Tab 键序列，使其能够接收到键盘焦点。

设置 tabIndex = -1 会从标签页序列中移除该元素，但仍允许该元素执行以下操作： 以编程方式接收键盘焦点。

扩展程序应该只通过键盘即可使用，方便无法使用鼠标的用户，而且 那些根本不想访问应用的用户。

检查用户能否在不使用鼠标的情况下在扩展程序的不同部分之间导航。 检查确保使用任何弹出式窗口时都可通过键盘导航。使用 Chrome 键盘快捷键执行以下操作： 确定扩展程序是否可导航。

确保用户能够轻松查看界面的哪些部分获得键盘焦点。通常是焦点轮廓 但如果过度使用 CSS，轮廓就可能被隐藏 把对比度降低。

最常用的键盘导航策略是使用 Tab 键来旋转焦点 但这并不总是最简单或最高效的选项。

一个简单的 JavaScript 键盘处理程序可能如下所示。请注意 WAI-ARIA 属性 aria-activedescendant 会根据用户输入进行更新，以反映当前处于活动状态的工具栏 按钮。

扩展程序可以为重要的扩展程序界面元素创建明确的键盘快捷键。为了实现 这些快捷键可将键盘事件监听器连接到控件。让用户知道 在选项页面中提供快捷方式。

提供方便用户查看的内容对所有用户而言都至关重要。以下指南中有很多可能听起来 因为它们反映了适用于所有网络内容的最佳实践。

字体选择和文字大小会影响扩展程序内容的可读性。有视力障碍的用户 可能需要增加扩展程序的文字大小。如果使用键盘快捷键，请确保这些快捷键不是 干扰 Chrome 中内置的缩放快捷方式。

采用 200% 测试作为扩展程序界面灵活性的指标；文字大小或 网页缩放增加了 200%，是否仍然可用？

避免将文本烘焙成图片。用户无法修改尺寸，屏幕阅读器也无法修改 来解读图像。您可以选用自定样式的网页字体，例如 Google Font API。网络字体可以缩放到不同的大小，并且可供使用屏幕的人访问 读者。

附加信息中的背景颜色和文字颜色之间应有足够明显的对比。使用 对比度检查工具，用于测试背景颜色和前景色是否提供 采用适当的对比度

评估对比度时，请验证附加信息中依赖图形来传达的各个部分 信息。对于特定图片，可使用Coblis - 色盲等工具 模拟器可用于查看图片在各种形式的色缺陷下的显示效果。

考虑提供不同的颜色主题，或允许用户自定义颜色 以便形成更好的对比度

如果扩展程序依靠声音或视频传达信息，请确保相应扩展程序 有转写文稿。有关详情，请参阅描述和带字幕的媒体计划准则 了解有关图片说明的信息。

使用替代文本来陈述图片的用途，而不是对内容进行文字说明 图像。间隔图片或纯装饰性图片应使用空白的 "" 替代文本，否则应将其移除 并放入 CSS 中。

如果扩展程序必须使用图片中的文字，请在替代文字中添加图片文字。实用资源 参阅有关相应替代文本的 WebAIM 文章。

如需详细了解 Chrome 中的无障碍功能，请访问 A11ycasts 频道并阅读 参阅 Chromium 无障碍功能技术文档。

**Examples:**

Example 1 (unknown):
```unknown
<div role="toolbar">
```

Example 2 (unknown):
```unknown
<div role="toolbar" tabindex="0" aria-activedescendant="button1">
  <img src="buttoncut.png" role="button" alt="cut" id="button1">
  <img src="buttoncopy.png" role="button" alt="copy" id="button2">
  <img src="buttonpaste.png" role="button" alt="paste" id="button3">
</div>
```

Example 3 (unknown):
```unknown
element.tabIndex = 0
```

Example 4 (unknown):
```unknown
element.focus();
```

---

## 使您的扩展程序可供访问 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/a11y

**Contents:**
- 使您的扩展程序可供访问 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

对许多用户而言，无障碍功能实际上就是界面，而对于那些不需要将无障碍功能作为与扩展程序互动的主要途径的用户而言，无障碍功能往往非常实用。这些技术多种多样。至少要有高对比度文字。视频应带有字幕。图片应包含 alt 属性。

不过，正如我们前面所说，这只是最低要求。下文介绍了其他方法。

有几种方法可以实现无障碍功能，但最简单的方法是使用标准 HTML 控件，尤其是输入元素。下图显示了这些控件。

如需使其他元素可供访问，请使用 ARIA 属性。这些属性可向屏幕阅读器提供有关网页上控件的功能和当前状态的信息。这里给出了一个示例，

默认情况下，在 HTML DOM 中，唯一可以接收键盘焦点的元素为锚点、按钮和表单控件。幸运的是，在 HTML 元素上设置 tabIndex 属性可使其获得键盘焦点。例如：

如需了解如何实现这些技巧以及其他内容，请参阅支持无障碍功能。

**Examples:**

Example 1 (unknown):
```unknown
<div role="toolbar" tabindex="0" aria-activedescendant="button1">
  <img src="buttoncut.png" role="button" alt="cut" id="button1">
  <img src="buttoncopy.png" role="button" alt="copy" id="button2">
  <img src="buttonpaste.png" role="button" alt="paste" id="button3">
</div>
```

Example 2 (unknown):
```unknown
<div tabindex="0">I can receive focus with the tab key.</div>
```

---

## 替换 Chrome 网页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/override-chrome-pages?hl=zh-cn

**Contents:**
- 替换 Chrome 网页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 无痕式窗口行为
- 清单
- 最佳做法
- 示例

扩展程序可以使用 HTML 替换网页来替换 Google Chrome 通常提供的网页。扩展程序可以包含对以下任一网页的替换，但每个扩展程序只能替换一个网页：

以下屏幕截图显示了默认的新标签页，然后显示了自定义的新标签页。

在无痕式窗口中，扩展程序无法替换“新标签页”。如果 incognito 清单属性设置为“split”（默认值），其他网页仍可正常运行。如需详细了解如何处理无痕式窗口，请参阅节省数据流量和无痕模式。

使用以下代码在扩展程序清单中注册替换网页：

对于 PAGE_TO_OVERRIDE，请替换为以下内容之一：

提高网页速度并缩减网页大小。用户希望内置浏览器页面能够立即打开。避免执行可能需要很长时间的操作。具体而言，应避免同步访问数据库资源。发出网络请求时，请优先使用 fetch() 而不是 XMLHttpRequest()。

为避免用户混淆，请为您的网页添加标题。 如果没有标题，网页标题会默认为网址。使用 HTML 文件中的 <title> 标记指定标题。

请注意，新标签页会先将键盘焦点移至地址栏。不要依赖于键盘焦点默认移至网页的其他部分。

打造您自己的新标签页。避免创建用户可能会与 Chrome 的默认新标签页混淆的新标签页。

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "My extension",
  ...

  "chrome_url_overrides" : {
    "PAGE_TO_OVERRIDE": "myPage.html"
  },
  ...
}
```

---

## 替换 Chrome 网页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/override-chrome-pages

**Contents:**
- 替换 Chrome 网页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 无痕式窗口行为
- 清单
- 最佳做法
- 示例

扩展程序可以使用 HTML 替换网页来替换 Google Chrome 通常提供的网页。扩展程序可以包含对以下任一网页的替换，但每个扩展程序只能替换一个网页：

以下屏幕截图显示了默认的新标签页，然后显示了自定义的新标签页。

在无痕式窗口中，扩展程序无法替换“新标签页”。如果 incognito 清单属性设置为“split”（默认值），其他网页仍可正常运行。如需详细了解如何处理无痕式窗口，请参阅节省数据流量和无痕模式。

使用以下代码在扩展程序清单中注册替换网页：

对于 PAGE_TO_OVERRIDE，请替换为以下内容之一：

提高网页速度并缩减网页大小。用户希望内置浏览器页面能够立即打开。避免执行可能需要很长时间的操作。具体而言，应避免同步访问数据库资源。发出网络请求时，请优先使用 fetch() 而不是 XMLHttpRequest()。

为避免用户混淆，请为您的网页添加标题。 如果没有标题，网页标题会默认为网址。使用 HTML 文件中的 <title> 标记指定标题。

请注意，新标签页会先将键盘焦点移至地址栏。不要依赖于键盘焦点默认移至网页的其他部分。

打造您自己的新标签页。避免创建用户可能会与 Chrome 的默认新标签页混淆的新标签页。

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "My extension",
  ...

  "chrome_url_overrides" : {
    "PAGE_TO_OVERRIDE": "myPage.html"
  },
  ...
}
```

---

## 什么是主题？ 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui/themes

**Contents:**
- 什么是主题？ 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
  - 颜色
  - 图片
  - 媒体资源
  - 色调

主题背景是一种用于更改浏览器外观的特殊扩展程序。主题为 与常规扩展程序一样打包，但不包含 JavaScript 或 HTML 代码。

您可通过与扩展程序相同的过程将主题上传到 Chrome 应用商店。在上传过程中，系统会要求您选择一个类别。您可在 Chrome 应用商店文档中的最佳实践下找到主题类别列表。

您可在 Chrome 应用商店中找到并试用各种主题背景。

以下是主题的 manifest.json 文件示例：

颜色采用 RGB 格式。要查找字符串，您可以在“colors”字段，请参阅 kOverwritableColorTable。

图片资源使用相对于扩展程序根目录的路径。您可以替换任何映像 由 kPersistingImages 中的字符串指定。所有图片都必须以 PNG 格式存储 格式的网址，否则它们将无法正常呈现。

通过此字段，您可以指定背景对齐、背景重复和 备用徽标。如需查看它们可以采用的属性和值，请参阅 kDisplayProperties。

您可以指定要应用于界面的各个部分（例如按钮、画面和 背景标签页。Google Chrome 支持色调调节，但不支持图片，因为图片无法跨平台使用 因为添加新按钮时会变得很脆弱要查找字符串，您可以在 “色调”字段，请参阅 kTintTable。

着色采用色相-饱和度-亮度 (HSL) 格式，使用 0 - 范围内的浮点数 1.0：

或者，您也可以将 -1.0 用于任何 HSL 值，以指定没有变化。

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "version": "2.6",
  "name": "camo theme",
  "theme": {
    "images" : {
      "theme_frame" : "images/theme_frame_camo.png",
      "theme_frame_overlay" : "images/theme_frame_stripe.png",
      "theme_toolbar" : "images/theme_toolbar_camo.png",
      "theme_ntp_background" : "images/theme_ntp_background_norepeat.png",
      "theme_ntp_attribution" : "images/attribution.png"
    },
    "colors" : {
      "frame" : [71, 105, 91],
      "toolbar" : [207, 221, 192],
      "ntp_text" : [20, 40, 0],
      "ntp_link" : [36, 70, 0],
      "ntp_section" : [207, 221, 192],
      "button_background" : [255, 255, 255]
    },
    "tints" : {
      "buttons" : [0.33, 0.5, 0.47]
    },
    "properties" : {
      "ntp_background_alignment" : "bottom"
    }
  }
}
```

---

## 界面组件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/ui?hl=zh-cn

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

## chrome.pageCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/pageCapture?hl=zh-cn

**Contents:**
- chrome.pageCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 方法
  - saveAsMHTML()
    - 参数
    - 返回

使用 chrome.pageCapture API 将标签页另存为 MHTML。

MHTML 是一种标准格式，大多数浏览器都支持这种格式。它将网页及其所有资源（CSS 文件、图片等）封装在一个文件中。

请注意，出于安全考虑，MHTML 文件只能从文件系统加载，并且只能在主框架中加载。

您必须在扩展程序清单中声明“pageCapture”权限，才能使用 pageCapture API。例如：

将具有指定 ID 的标签页的内容保存为 MHTML。

Promise<Blob | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "pageCapture"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.pageCapture.saveAsMHTML(  details: object,): Promise<Blob | undefined>
```

---
