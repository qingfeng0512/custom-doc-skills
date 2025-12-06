# Chrome-Extensions - Debugging

**Pages:** 5

---

## 针对 Chrome 扩展程序的端到端测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/end-to-end-testing

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

## 针对 Chrome 扩展程序的端到端测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/end-to-end-testing?hl=zh-cn

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
{
  "name": "My extension",
  ...
  "permissions": [
    "debugger",
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.debugger.attach(  target: Debuggee,  requiredVersion: string,  callback?: function,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.debugger.detach(  target: Debuggee,  callback?: function,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.debugger.getTargets(  callback?: function,): Promise<TargetInfo[]>
```

---

## 对 Chrome 扩展程序进行单元测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/unit-testing?hl=zh-cn

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

## 对 Chrome 扩展程序进行单元测试 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/unit-testing

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
