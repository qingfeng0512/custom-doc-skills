# Chrome-Extensions - Background Scripts

**Pages:** 8

---

## Service Worker 中的事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/events

**Contents:**
- Service Worker 中的事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 声明扩展程序事件
- 常见事件
- 过滤条件
- Web Service Worker 事件
  - ServiceWorkerGlobal.fetch
  - ServiceWorkerGlobal.message

扩展程序服务工支持标准服务工事件以及扩展程序 API 中的许多事件。本部分介绍了可用的功能，并提供了使用这些功能的提示。

服务工件中的事件处理脚本需要在全局范围内声明，这意味着它们应位于脚本的顶级，而不是嵌套在函数内。这样可确保在初始脚本执行时同步注册这些事件，从而让 Chrome 能够在服务工作器启动后立即向其分派事件。例如：

扩展程序服务工支持特定 API 中的事件。下面介绍了一些常见的错误。请注意，其中一些 API 需要权限才能使用，而另一些 API 可能包含某些版本的 Chrome 中并不支持的事件、方法或属性。如需了解详情，请参阅所链接的 API 文档，尤其是您要使用的事件、方法或属性。

若要将事件限定为特定用例或消除不必要的事件调用，请使用支持事件过滤器的 API。例如，假设有一个扩展程序监听 tabs.onUpdated 事件，以检测用户何时导航到特定网站。在每个标签页上每次导航时都会调用此事件。请改为将 webNavigation.onCompleted 与过滤条件搭配使用。例如：

扩展程序服务工作器支持的生命周期事件不仅仅是其他部分中所述的事件。

从扩展程序软件包检索任何内容或从扩展程序或弹出式窗口脚本调用 fetch() 和 XMLHttpRequest() 时触发。（服务工件 fetch 处理脚本不会拦截内容脚本的调用。）在后一种情况下，您需要将要提取的网页的网址添加到 manifest.json 中的 "host_permissions" 键。

除了扩展程序消息传递外，Service Worker 消息传递功能可用，但这两个系统无法互操作。这意味着，使用 sendMessage()（可通过多个扩展程序 API 获取）发送的消息不会被服务工件消息处理脚本拦截。同样，扩展程序消息处理脚本不会拦截使用 postMessage() 发送的消息。扩展程序 Service Worker 同时支持这两种消息处理程序（即 ServiceWorkerGlobal.message 和 chrome.runtime.onMessage）。

除非您有特殊原因要使用服务工件消息传递，否则应优先使用扩展程序消息传递。

**Examples:**

Example 1 (javascript):
```javascript
chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
  chrome.action.onClicked.addListener(handleActionClick);
});
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener(handleActionClick);

chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
});
```

Example 3 (javascript):
```javascript
const filter = {
  url: [
    {
      urlMatches: 'https://www.google.com/',
    },
  ],
};

chrome.webNavigation.onCompleted.addListener(() => {
  console.info("The user has loaded my favorite website!");
}, filter);
```

---

## chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/events

**Contents:**
- chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 声明式事件处理脚本
  - 规则
  - 事件对象
  - 添加规则
  - 移除规则
  - 检索规则
  - 性能
- 过滤出的活动

chrome.events 命名空间包含一些常用类型，API 会使用这些类型来调度事件，以便在发生值得注意的事情时通知您。

Event 是一个对象，可让您在发生有趣的事情时收到通知。这里有 使用 chrome.alarms.onAlarm 事件在闹钟经过时接收通知的示例：

如示例所示，您将使用 addListener() 注册接收通知。用于 addListener() 始终是您定义的用于处理事件的函数， 函数取决于您正在处理的事件。查看 alarms.onAlarm 的文档， 您会看到该函数只有一个形参：一个包含详细信息的 alarms.Alarm 对象 已播放的闹钟。

使用事件的示例 API：alarms、i18n、identity、runtime。大部分Chrome API 所做的任何修改。

声明式事件处理脚本提供了一种方法，用于定义由声明式条件组成的规则 和操作。条件是在浏览器而不是 JavaScript 引擎中评估的，这样可以减少 并实现极高的效率

例如，声明式 Web 请求 API 中就使用了声明式事件处理脚本， 声明式 Content API。本页介绍了所有声明式事件的基本概念 处理程序。

最简单的规则是包含一个或多个条件以及一项或多项操作：

除了条件和操作之外，您还可以为每条规则指定一个标识符，这样可以简化 取消注册先前注册的规则，以及定义规则优先级的优先级。 只有在规则之间相互冲突或需要在特定环境中执行时，系统才会考虑优先级 订单。操作按其规则优先级的降序执行。

事件对象可能支持规则。当发生以下情况时，这些事件对象不会调用回调函数： 但会测试任何已注册规则是否至少包含一个满足条件并执行 与此规则相关的操作支持声明式 API 的事件对象具有三个 相关方法：events.Event.addRules、events.Event.removeRules 和 events.Event.getRules。

如需添加规则，请调用事件对象的 addRules() 函数。它接受一组规则实例 作为其第一个参数，并在完成时调用回调函数。

如果规则已成功插入，details 参数将包含一组插入的规则 显示顺序与传递的 rule_list 中的顺序相同，其中可选参数 id 和 已用生成的值填充 priority。如果任何规则无效，例如，由于该规则包含 条件或操作无效，则不添加任何规则和 runtime.lastError 变量 在调用回调函数时设置 。rule_list 中的每条规则都必须包含一个唯一的 当前未被其他规则使用的标识符或空标识符。

如需移除规则，请调用 removeRules() 函数。它接受一组规则标识符（可选） 作为其第一个参数，并将回调函数作为其第二个参数。

如果 rule_ids 是一个标识符数组，则所有在数组中列出标识符的规则都是 已移除。如果 rule_ids 列出了未知的标识符，系统会以静默方式忽略此标识符。如果 rule_ids 为 undefined，此扩展程序的所有已注册规则均已移除。callback() 函数会在规则被删除时调用。

如需检索当前已注册规则的列表，请调用 getRules() 函数。它接受 可选的规则标识符数组，其语义与 removeRules 相同，是一个回调函数。

传递给 callback() 函数的 details 形参引用了一组规则，包括 已填充的可选参数。

批量注册和取消注册规则。每次注册或取消注册后，Chrome 都需要 更新内部数据结构。此更新是一项成本高昂的操作。

在 events.UrlFilter 中，首选子字符串匹配而不是正则表达式。 基于子字符串的匹配极快。

如果多条规则共享相同的操作，请将这些规则合并为一条。 只要满足一个条件，规则就会触发其操作。这样可以加快 匹配并减少重复操作集的内存消耗。

过滤事件是一种机制，可让监听器指定它们属于 。不会针对未传递 过滤器，这使得监听代码更具声明性和效率。Service Worker 需求 被唤醒以处理其不关心的事件。

符合过滤条件的事件可让您从手动过滤代码过渡，如下所示：

事件支持对该事件有意义的特定过滤条件。事件可过滤的过滤条件的列表 支持将会在该事件的文档的“filters”部分中列出部分。

匹配网址时（如上例所示），事件过滤器支持同一网址匹配 可通过 events.UrlFilter 表达的功能（架构和端口匹配除外）。

一个对象，用于添加和移除 Chrome 事件监听器。

在事件发生时调用。此函数的参数取决于事件类型。

要注册的规则。这些规则不会取代以前注册的规则。

如果传递的是数组，则系统仅返回具有此数组所含标识符的规则。

如果为事件注册了回调函数，则为 true。

如果有任何事件监听器已注册到该事件，则为 true。

removeListener 函数如下所示：

如果传递了一个数组，则系统只会取消注册此数组中所含的标识符的规则。

标记可用于为规则添加注释，以及对规则集执行操作。

根据各种条件过滤网址。请参阅事件过滤。所有条件均区分大小写。

如果网址的主机部分是 IP 地址，并且包含在数组中指定的任何 CIDR 地址块中，则匹配。

如果网址的主机名包含指定字符串，则匹配。如需测试主机名组件是否具有前缀“foo”，请使用 hostcontains: “.foo”。这与“www.foobar.com”一致和“foo.com”，因为在主机名的开头添加了隐式点。同样，hostcontains 可用于匹配组件后缀（“foo.”）及与组件（“.foo.”）完全匹配。由于在主机名末尾未添加隐式点，因此最后组件的后缀和完全匹配需要使用 host 最终到达网址后缀 单独执行。

如果网址的主机名以指定字符串开头，则匹配。

如果网址的主机名以指定字符串结尾，则匹配。

如果不带查询片段和片段标识符的网址与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址的路径段以指定字符串开头，则匹配。

如果网址的路径段以指定字符串结尾，则匹配。

(number | number[])[] 选填

如果网址的端口包含在任何指定端口列表中，则匹配。例如，[80, 443, [1000, 1200]] 会匹配端口 80、443 上以及 1000-1200 范围内的所有请求。

如果网址的查询片段以指定字符串开头，则匹配。

如果网址的查询片段以指定字符串结尾，则匹配。

如果网址的架构等于数组中指定的任何架构，则匹配。

如果网址（不含片段标识符）包含指定字符串，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

在网址（不含片段标识符）等于指定字符串时匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（不带片段标识符）与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址（不带片段标识符）以指定字符串开头，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（无片段标识符）以指定字符串结尾，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

**Examples:**

Example 1 (unknown):
```unknown
chrome.alarms.onAlarm.addListener(function(alarm) {
  appendToLog('alarms.onAlarm --'
              + ' name: '          + alarm.name
              + ' scheduledTime: ' + alarm.scheduledTime);
});
```

Example 2 (unknown):
```unknown
var rule = {
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 3 (unknown):
```unknown
var rule = {
  id: "my rule",  // optional, will be generated if not set.
  priority: 100,  // optional, defaults to 100.
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 4 (unknown):
```unknown
var rule_list = [rule1, rule2, ...];
function addRules(rule_list, function callback(details) {...});
```

---

## chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/events/?hl=zh-cn

**Contents:**
- chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 声明式事件处理脚本
    - 规则
    - 事件对象
    - 添加规则
    - 移除规则
    - 检索规则
    - 性能

chrome.events 命名空间包含一些常用类型，API 会使用这些类型来调度事件，以便在发生值得注意的事情时通知您。

Event 是一个对象，可让您在发生有趣的事情时收到通知。这里有 使用 chrome.alarms.onAlarm 事件在闹钟经过时接收通知的示例：

如示例所示，您将使用 addListener() 注册接收通知。用于 addListener() 始终是您定义的用于处理事件的函数， 函数取决于您正在处理的事件。查看 alarms.onAlarm 的文档， 您会看到该函数只有一个形参：一个包含详细信息的 alarms.Alarm 对象 已播放的闹钟。

使用事件的示例 API：alarms、i18n、identity、runtime。大部分Chrome API 所做的任何修改。

声明式事件处理脚本提供了一种方法，用于定义由声明式条件组成的规则 和操作。条件是在浏览器而不是 JavaScript 引擎中评估的，这样可以减少 并实现极高的效率

声明式事件处理脚本用于 声明式 Content API。本页介绍了所有声明式事件的基本概念 处理程序。

最简单的规则是包含一个或多个条件以及一项或多项操作：

除了条件和操作之外，您还可以为每条规则指定一个标识符，这样可以简化 取消注册先前注册的规则，以及定义规则优先级的优先级。 只有在规则之间相互冲突或需要在特定环境中执行时，系统才会考虑优先级 订单。操作按其规则优先级的降序执行。

事件对象可能支持规则。当发生以下情况时，这些事件对象不会调用回调函数： 但会测试任何已注册规则是否至少包含一个满足条件并执行 与此规则相关的操作支持声明式 API 的事件对象具有三个 相关方法：events.Event.addRules()、events.Event.removeRules() 和 events.Event.getRules()。

如需添加规则，请调用事件对象的 addRules() 函数。它接受一组规则实例 作为其第一个参数，并在完成时调用回调函数。

如果规则已成功插入，details 参数将包含一组插入的规则 显示顺序与传递的 rule_list 中的顺序相同，其中可选参数 id 和 已用生成的值填充 priority。如果有任何规则无效，例如 条件或操作无效，则不添加任何规则和 runtime.lastError 变量 在调用回调函数时设置 。rule_list 中的每条规则都必须包含一个唯一的 其他规则尚未使用的标识符或空标识符。

如需移除规则，请调用 removeRules() 函数。它接受一组规则标识符（可选） 作为其第一个参数，并将回调函数作为其第二个参数。

如果 rule_ids 是一个标识符数组，则所有在数组中列出标识符的规则都是 已移除。如果 rule_ids 列出了未知的标识符，系统会以静默方式忽略此标识符。如果 rule_ids 为 undefined，此扩展程序的所有已注册规则均已移除。callback() 函数会在规则被删除时调用。

如需检索已注册规则的列表，请调用 getRules() 函数。它接受 可选的规则标识符数组，其语义与 removeRules() 相同，是一个回调函数。

传递给 callback() 函数的 details 形参引用了一组规则，包括 已填充的可选参数。

批量注册和取消注册规则。每次注册或取消注册后，Chrome 都需要 更新内部数据结构。此更新是一项成本高昂的操作。

在 events.UrlFilter 中，首选子字符串匹配而不是正则表达式。 基于子字符串的匹配极快。

如果多条规则共享相同的操作，请将这些规则合并为一条。 只要满足一个条件，规则就会触发其操作。这样可以加快 匹配并减少重复操作集的内存消耗。

过滤事件是一种机制，可让监听器指定它们属于 。不会针对未传递 过滤器，这使得监听代码更具声明性和效率。Service Worker 需求 被唤醒以处理其不关心的事件。

事件支持对该事件有意义的特定过滤条件。事件可过滤的过滤条件的列表 支持将会在该事件的文档的“filters”部分中列出部分。

匹配网址时（如上例所示），事件过滤器支持同一网址匹配 可通过 events.UrlFilter 表达的功能（架构和端口匹配除外）。

一个对象，用于添加和移除 Chrome 事件监听器。

在事件发生时调用。此函数的参数取决于事件类型。

要注册的规则。这些规则不会取代以前注册的规则。

如果传递的是数组，则系统仅返回具有此数组所含标识符的规则。

如果为事件注册了回调函数，则为 true。

如果有任何事件监听器已注册到该事件，则为 true。

removeListener 函数如下所示：

如果传递了一个数组，则系统只会取消注册此数组中所含的标识符的规则。

标记可用于为规则添加注释，以及对规则集执行操作。

根据各种条件过滤网址。请参阅事件过滤。所有条件均区分大小写。

如果网址的主机部分是 IP 地址，并且包含在数组中指定的任何 CIDR 地址块中，则匹配。

如果网址的主机名包含指定字符串，则匹配。如需测试主机名组件是否具有前缀“foo”，请使用 hostcontains: “.foo”。这与“www.foobar.com”一致和“foo.com”，因为在主机名的开头添加了隐式点。同样，hostcontains 可用于匹配组件后缀（“foo.”）及与组件（“.foo.”）完全匹配。由于在主机名末尾未添加隐式点，因此最后组件的后缀和完全匹配需要使用 host 最终到达网址后缀 单独执行。

如果网址的主机名以指定字符串开头，则匹配。

如果网址的主机名以指定字符串结尾，则匹配。

如果不带查询片段和片段标识符的网址与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址的路径段以指定字符串开头，则匹配。

如果网址的路径段以指定字符串结尾，则匹配。

(number | number[])[] 选填

如果网址的端口包含在任何指定端口列表中，则匹配。例如，[80, 443, [1000, 1200]] 会匹配端口 80、443 上以及 1000-1200 范围内的所有请求。

如果网址的查询片段以指定字符串开头，则匹配。

如果网址的查询片段以指定字符串结尾，则匹配。

如果网址的架构等于数组中指定的任何架构，则匹配。

如果网址（不含片段标识符）包含指定字符串，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

在网址（不含片段标识符）等于指定字符串时匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（不带片段标识符）与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址（不带片段标识符）以指定字符串开头，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（无片段标识符）以指定字符串结尾，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

**Examples:**

Example 1 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  appendToLog(`alarms.onAlarm -- name: ${alarm.name}, scheduledTime: ${alarm.scheduledTime}`);
});
```

Example 2 (javascript):
```javascript
const rule = {
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 3 (javascript):
```javascript
const rule = {
  id: "my rule",  // optional, will be generated if not set.
  priority: 100,  // optional, defaults to 100.
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 4 (javascript):
```javascript
const rule_list = [rule1, rule2, ...];
addRules(rule_list, (details) => {...});
```

---

## chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/events?hl=zh-cn

**Contents:**
- chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 声明式事件处理脚本
    - 规则
    - 事件对象
    - 添加规则
    - 移除规则
    - 检索规则
    - 性能

chrome.events 命名空间包含一些常用类型，API 会使用这些类型来调度事件，以便在发生值得注意的事情时通知您。

Event 是一个对象，可让您在发生有趣的事情时收到通知。这里有 使用 chrome.alarms.onAlarm 事件在闹钟经过时接收通知的示例：

如示例所示，您将使用 addListener() 注册接收通知。用于 addListener() 始终是您定义的用于处理事件的函数， 函数取决于您正在处理的事件。查看 alarms.onAlarm 的文档， 您会看到该函数只有一个形参：一个包含详细信息的 alarms.Alarm 对象 已播放的闹钟。

使用事件的示例 API：alarms、i18n、identity、runtime。大部分Chrome API 所做的任何修改。

声明式事件处理脚本提供了一种方法，用于定义由声明式条件组成的规则 和操作。条件是在浏览器而不是 JavaScript 引擎中评估的，这样可以减少 并实现极高的效率

声明式事件处理脚本用于 声明式 Content API。本页介绍了所有声明式事件的基本概念 处理程序。

最简单的规则是包含一个或多个条件以及一项或多项操作：

除了条件和操作之外，您还可以为每条规则指定一个标识符，这样可以简化 取消注册先前注册的规则，以及定义规则优先级的优先级。 只有在规则之间相互冲突或需要在特定环境中执行时，系统才会考虑优先级 订单。操作按其规则优先级的降序执行。

事件对象可能支持规则。当发生以下情况时，这些事件对象不会调用回调函数： 但会测试任何已注册规则是否至少包含一个满足条件并执行 与此规则相关的操作支持声明式 API 的事件对象具有三个 相关方法：events.Event.addRules()、events.Event.removeRules() 和 events.Event.getRules()。

如需添加规则，请调用事件对象的 addRules() 函数。它接受一组规则实例 作为其第一个参数，并在完成时调用回调函数。

如果规则已成功插入，details 参数将包含一组插入的规则 显示顺序与传递的 rule_list 中的顺序相同，其中可选参数 id 和 已用生成的值填充 priority。如果有任何规则无效，例如 条件或操作无效，则不添加任何规则和 runtime.lastError 变量 在调用回调函数时设置 。rule_list 中的每条规则都必须包含一个唯一的 其他规则尚未使用的标识符或空标识符。

如需移除规则，请调用 removeRules() 函数。它接受一组规则标识符（可选） 作为其第一个参数，并将回调函数作为其第二个参数。

如果 rule_ids 是一个标识符数组，则所有在数组中列出标识符的规则都是 已移除。如果 rule_ids 列出了未知的标识符，系统会以静默方式忽略此标识符。如果 rule_ids 为 undefined，此扩展程序的所有已注册规则均已移除。callback() 函数会在规则被删除时调用。

如需检索已注册规则的列表，请调用 getRules() 函数。它接受 可选的规则标识符数组，其语义与 removeRules() 相同，是一个回调函数。

传递给 callback() 函数的 details 形参引用了一组规则，包括 已填充的可选参数。

批量注册和取消注册规则。每次注册或取消注册后，Chrome 都需要 更新内部数据结构。此更新是一项成本高昂的操作。

在 events.UrlFilter 中，首选子字符串匹配而不是正则表达式。 基于子字符串的匹配极快。

如果多条规则共享相同的操作，请将这些规则合并为一条。 只要满足一个条件，规则就会触发其操作。这样可以加快 匹配并减少重复操作集的内存消耗。

过滤事件是一种机制，可让监听器指定它们属于 。不会针对未传递 过滤器，这使得监听代码更具声明性和效率。Service Worker 需求 被唤醒以处理其不关心的事件。

事件支持对该事件有意义的特定过滤条件。事件可过滤的过滤条件的列表 支持将会在该事件的文档的“filters”部分中列出部分。

匹配网址时（如上例所示），事件过滤器支持同一网址匹配 可通过 events.UrlFilter 表达的功能（架构和端口匹配除外）。

一个对象，用于添加和移除 Chrome 事件监听器。

在事件发生时调用。此函数的参数取决于事件类型。

要注册的规则。这些规则不会取代以前注册的规则。

如果传递的是数组，则系统仅返回具有此数组所含标识符的规则。

如果为事件注册了回调函数，则为 true。

如果有任何事件监听器已注册到该事件，则为 true。

removeListener 函数如下所示：

如果传递了一个数组，则系统只会取消注册此数组中所含的标识符的规则。

标记可用于为规则添加注释，以及对规则集执行操作。

根据各种条件过滤网址。请参阅事件过滤。所有条件均区分大小写。

如果网址的主机部分是 IP 地址，并且包含在数组中指定的任何 CIDR 地址块中，则匹配。

如果网址的主机名包含指定字符串，则匹配。如需测试主机名组件是否具有前缀“foo”，请使用 hostcontains: “.foo”。这与“www.foobar.com”一致和“foo.com”，因为在主机名的开头添加了隐式点。同样，hostcontains 可用于匹配组件后缀（“foo.”）及与组件（“.foo.”）完全匹配。由于在主机名末尾未添加隐式点，因此最后组件的后缀和完全匹配需要使用 host 最终到达网址后缀 单独执行。

如果网址的主机名以指定字符串开头，则匹配。

如果网址的主机名以指定字符串结尾，则匹配。

如果不带查询片段和片段标识符的网址与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址的路径段以指定字符串开头，则匹配。

如果网址的路径段以指定字符串结尾，则匹配。

(number | number[])[] 选填

如果网址的端口包含在任何指定端口列表中，则匹配。例如，[80, 443, [1000, 1200]] 会匹配端口 80、443 上以及 1000-1200 范围内的所有请求。

如果网址的查询片段以指定字符串开头，则匹配。

如果网址的查询片段以指定字符串结尾，则匹配。

如果网址的架构等于数组中指定的任何架构，则匹配。

如果网址（不含片段标识符）包含指定字符串，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

在网址（不含片段标识符）等于指定字符串时匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（不带片段标识符）与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址（不带片段标识符）以指定字符串开头，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（无片段标识符）以指定字符串结尾，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

**Examples:**

Example 1 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  appendToLog(`alarms.onAlarm -- name: ${alarm.name}, scheduledTime: ${alarm.scheduledTime}`);
});
```

Example 2 (javascript):
```javascript
const rule = {
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 3 (javascript):
```javascript
const rule = {
  id: "my rule",  // optional, will be generated if not set.
  priority: 100,  // optional, defaults to 100.
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 4 (javascript):
```javascript
const rule_list = [rule1, rule2, ...];
addRules(rule_list, (details) => {...});
```

---

## Service Worker 中的事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/events?hl=zh-cn

**Contents:**
- Service Worker 中的事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 声明扩展程序事件
- 常见事件
- 过滤条件
- Web Service Worker 事件
  - ServiceWorkerGlobal.fetch
  - ServiceWorkerGlobal.message

扩展程序服务工支持标准服务工事件以及扩展程序 API 中的许多事件。本部分介绍了可用的功能，并提供了使用这些功能的提示。

服务工件中的事件处理脚本需要在全局范围内声明，这意味着它们应位于脚本的顶级，而不是嵌套在函数内。这样可确保在初始脚本执行时同步注册这些事件，从而让 Chrome 能够在服务工作器启动后立即向其分派事件。例如：

扩展程序服务工支持特定 API 中的事件。下面介绍了一些常见的错误。请注意，其中一些 API 需要权限才能使用，而另一些 API 可能包含某些版本的 Chrome 中并不支持的事件、方法或属性。如需了解详情，请参阅所链接的 API 文档，尤其是您要使用的事件、方法或属性。

若要将事件限定为特定用例或消除不必要的事件调用，请使用支持事件过滤器的 API。例如，假设有一个扩展程序监听 tabs.onUpdated 事件，以检测用户何时导航到特定网站。在每个标签页上每次导航时都会调用此事件。请改为将 webNavigation.onCompleted 与过滤条件搭配使用。例如：

扩展程序服务工作器支持的生命周期事件不仅仅是其他部分中所述的事件。

从扩展程序软件包检索任何内容或从扩展程序或弹出式窗口脚本调用 fetch() 和 XMLHttpRequest() 时触发。（服务工件 fetch 处理脚本不会拦截内容脚本的调用。）在后一种情况下，您需要将要提取的网页的网址添加到 manifest.json 中的 "host_permissions" 键。

除了扩展程序消息传递外，Service Worker 消息传递功能可用，但这两个系统无法互操作。这意味着，使用 sendMessage()（可通过多个扩展程序 API 获取）发送的消息不会被服务工件消息处理脚本拦截。同样，扩展程序消息处理脚本不会拦截使用 postMessage() 发送的消息。扩展程序 Service Worker 同时支持这两种消息处理程序（即 ServiceWorkerGlobal.message 和 chrome.runtime.onMessage）。

除非您有特殊原因要使用服务工件消息传递，否则应优先使用扩展程序消息传递。

**Examples:**

Example 1 (javascript):
```javascript
chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
  chrome.action.onClicked.addListener(handleActionClick);
});
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener(handleActionClick);

chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
});
```

Example 3 (javascript):
```javascript
const filter = {
  url: [
    {
      urlMatches: 'https://www.google.com/',
    },
  ],
};

chrome.webNavigation.onCompleted.addListener(() => {
  console.info("The user has loaded my favorite website!");
}, filter);
```

---

## Extension Service Worker 基础知识 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/basics?hl=zh-cn

**Contents:**
- Extension Service Worker 基础知识 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 注册 Service Worker
- 导入脚本
- 更新

扩展程序 Service Worker 的安装和更新方式与 Web Service Worker 不同。本页将介绍这些差异。

如需注册扩展程序服务工作器，请在 manifest.json 文件的 "background" 字段中指定该服务工作器。使用 "service_worker" 键，用于指定单个 JavaScript 文件。网页或 Web 应用中的 Service Worker 会通过以下方式注册 Service Worker：首先对 navigator 中的 serviceWorker 进行特征检测，然后在功能检测内调用 register()。这不适用于扩展程序。

您可以通过以下两种方法将脚本导入到服务工件中：import 语句和 importScripts() 方法。请注意，不支持 import()（通常称为动态导入）。

如需使用 import 语句，请将 "type" 字段添加到清单并指定 "module"。例如：

然后，照常使用 import。请注意，不支持导入断言。

使用 importScripts() 的方式与在 Web 服务工作器中一样。

如需更新服务工件，请将扩展程序的新版本发布到 Chrome 应用商店。您无法通过从服务器加载扩展程序来解决此问题。出于安全原因，Manifest V3 不支持远程托管的代码。您的 Service Worker 必须是扩展程序软件包的一部分。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Awesome Test Extension",
  ...
  "background": {
    "service_worker": "service-worker.js"
  },
  ...
}
```

Example 2 (unknown):
```unknown
"background": {
    "service_worker": "service-worker.js",
    "type": "module"
  }
```

Example 3 (python):
```python
import { tldLocales } from './locales.js';
```

Example 4 (unknown):
```unknown
importScripts('locales.js');
```

---

## chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/events

**Contents:**
- chrome.events 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 声明式事件处理脚本
    - 规则
    - 事件对象
    - 添加规则
    - 移除规则
    - 检索规则
    - 性能

chrome.events 命名空间包含一些常用类型，API 会使用这些类型来调度事件，以便在发生值得注意的事情时通知您。

Event 是一个对象，可让您在发生有趣的事情时收到通知。这里有 使用 chrome.alarms.onAlarm 事件在闹钟经过时接收通知的示例：

如示例所示，您将使用 addListener() 注册接收通知。用于 addListener() 始终是您定义的用于处理事件的函数， 函数取决于您正在处理的事件。查看 alarms.onAlarm 的文档， 您会看到该函数只有一个形参：一个包含详细信息的 alarms.Alarm 对象 已播放的闹钟。

使用事件的示例 API：alarms、i18n、identity、runtime。大部分Chrome API 所做的任何修改。

声明式事件处理脚本提供了一种方法，用于定义由声明式条件组成的规则 和操作。条件是在浏览器而不是 JavaScript 引擎中评估的，这样可以减少 并实现极高的效率

声明式事件处理脚本用于 声明式 Content API。本页介绍了所有声明式事件的基本概念 处理程序。

最简单的规则是包含一个或多个条件以及一项或多项操作：

除了条件和操作之外，您还可以为每条规则指定一个标识符，这样可以简化 取消注册先前注册的规则，以及定义规则优先级的优先级。 只有在规则之间相互冲突或需要在特定环境中执行时，系统才会考虑优先级 订单。操作按其规则优先级的降序执行。

事件对象可能支持规则。当发生以下情况时，这些事件对象不会调用回调函数： 但会测试任何已注册规则是否至少包含一个满足条件并执行 与此规则相关的操作支持声明式 API 的事件对象具有三个 相关方法：events.Event.addRules()、events.Event.removeRules() 和 events.Event.getRules()。

如需添加规则，请调用事件对象的 addRules() 函数。它接受一组规则实例 作为其第一个参数，并在完成时调用回调函数。

如果规则已成功插入，details 参数将包含一组插入的规则 显示顺序与传递的 rule_list 中的顺序相同，其中可选参数 id 和 已用生成的值填充 priority。如果有任何规则无效，例如 条件或操作无效，则不添加任何规则和 runtime.lastError 变量 在调用回调函数时设置 。rule_list 中的每条规则都必须包含一个唯一的 其他规则尚未使用的标识符或空标识符。

如需移除规则，请调用 removeRules() 函数。它接受一组规则标识符（可选） 作为其第一个参数，并将回调函数作为其第二个参数。

如果 rule_ids 是一个标识符数组，则所有在数组中列出标识符的规则都是 已移除。如果 rule_ids 列出了未知的标识符，系统会以静默方式忽略此标识符。如果 rule_ids 为 undefined，此扩展程序的所有已注册规则均已移除。callback() 函数会在规则被删除时调用。

如需检索已注册规则的列表，请调用 getRules() 函数。它接受 可选的规则标识符数组，其语义与 removeRules() 相同，是一个回调函数。

传递给 callback() 函数的 details 形参引用了一组规则，包括 已填充的可选参数。

批量注册和取消注册规则。每次注册或取消注册后，Chrome 都需要 更新内部数据结构。此更新是一项成本高昂的操作。

在 events.UrlFilter 中，首选子字符串匹配而不是正则表达式。 基于子字符串的匹配极快。

如果多条规则共享相同的操作，请将这些规则合并为一条。 只要满足一个条件，规则就会触发其操作。这样可以加快 匹配并减少重复操作集的内存消耗。

过滤事件是一种机制，可让监听器指定它们属于 。不会针对未传递 过滤器，这使得监听代码更具声明性和效率。Service Worker 需求 被唤醒以处理其不关心的事件。

事件支持对该事件有意义的特定过滤条件。事件可过滤的过滤条件的列表 支持将会在该事件的文档的“filters”部分中列出部分。

匹配网址时（如上例所示），事件过滤器支持同一网址匹配 可通过 events.UrlFilter 表达的功能（架构和端口匹配除外）。

一个对象，用于添加和移除 Chrome 事件监听器。

在事件发生时调用。此函数的参数取决于事件类型。

要注册的规则。这些规则不会取代以前注册的规则。

如果传递的是数组，则系统仅返回具有此数组所含标识符的规则。

如果为事件注册了回调函数，则为 true。

如果有任何事件监听器已注册到该事件，则为 true。

removeListener 函数如下所示：

如果传递了一个数组，则系统只会取消注册此数组中所含的标识符的规则。

标记可用于为规则添加注释，以及对规则集执行操作。

根据各种条件过滤网址。请参阅事件过滤。所有条件均区分大小写。

如果网址的主机部分是 IP 地址，并且包含在数组中指定的任何 CIDR 地址块中，则匹配。

如果网址的主机名包含指定字符串，则匹配。如需测试主机名组件是否具有前缀“foo”，请使用 hostcontains: “.foo”。这与“www.foobar.com”一致和“foo.com”，因为在主机名的开头添加了隐式点。同样，hostcontains 可用于匹配组件后缀（“foo.”）及与组件（“.foo.”）完全匹配。由于在主机名末尾未添加隐式点，因此最后组件的后缀和完全匹配需要使用 host 最终到达网址后缀 单独执行。

如果网址的主机名以指定字符串开头，则匹配。

如果网址的主机名以指定字符串结尾，则匹配。

如果不带查询片段和片段标识符的网址与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址的路径段以指定字符串开头，则匹配。

如果网址的路径段以指定字符串结尾，则匹配。

(number | number[])[] 选填

如果网址的端口包含在任何指定端口列表中，则匹配。例如，[80, 443, [1000, 1200]] 会匹配端口 80、443 上以及 1000-1200 范围内的所有请求。

如果网址的查询片段以指定字符串开头，则匹配。

如果网址的查询片段以指定字符串结尾，则匹配。

如果网址的架构等于数组中指定的任何架构，则匹配。

如果网址（不含片段标识符）包含指定字符串，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

在网址（不含片段标识符）等于指定字符串时匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（不带片段标识符）与指定的正则表达式匹配，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。正则表达式使用 RE2 语法。

如果网址（不带片段标识符）以指定字符串开头，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

如果网址（无片段标识符）以指定字符串结尾，则匹配。如果端口号与默认端口号匹配，则会从网址中删除。

**Examples:**

Example 1 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  appendToLog(`alarms.onAlarm -- name: ${alarm.name}, scheduledTime: ${alarm.scheduledTime}`);
});
```

Example 2 (javascript):
```javascript
const rule = {
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 3 (javascript):
```javascript
const rule = {
  id: "my rule",  // optional, will be generated if not set.
  priority: 100,  // optional, defaults to 100.
  conditions: [ /* my conditions */ ],
  actions: [ /* my actions */ ]
};
```

Example 4 (javascript):
```javascript
const rule_list = [rule1, rule2, ...];
addRules(rule_list, (details) => {...});
```

---

## Extension Service Worker 基础知识 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/basics

**Contents:**
- Extension Service Worker 基础知识 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 注册 Service Worker
- 导入脚本
- 更新

扩展程序 Service Worker 的安装和更新方式与 Web Service Worker 不同。本页将介绍这些差异。

如需注册扩展程序服务工作器，请在 manifest.json 文件的 "background" 字段中指定该服务工作器。使用 "service_worker" 键，用于指定单个 JavaScript 文件。网页或 Web 应用中的 Service Worker 会通过以下方式注册 Service Worker：首先对 navigator 中的 serviceWorker 进行特征检测，然后在功能检测内调用 register()。这不适用于扩展程序。

您可以通过以下两种方法将脚本导入到服务工件中：import 语句和 importScripts() 方法。请注意，不支持 import()（通常称为动态导入）。

如需使用 import 语句，请将 "type" 字段添加到清单并指定 "module"。例如：

然后，照常使用 import。请注意，不支持导入断言。

使用 importScripts() 的方式与在 Web 服务工作器中一样。

如需更新服务工件，请将扩展程序的新版本发布到 Chrome 应用商店。您无法通过从服务器加载扩展程序来解决此问题。出于安全原因，Manifest V3 不支持远程托管的代码。您的 Service Worker 必须是扩展程序软件包的一部分。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Awesome Test Extension",
  ...
  "background": {
    "service_worker": "service-worker.js"
  },
  ...
}
```

Example 2 (unknown):
```unknown
"background": {
    "service_worker": "service-worker.js",
    "type": "module"
  }
```

Example 3 (python):
```python
import { tldLocales } from './locales.js';
```

Example 4 (unknown):
```unknown
importScripts('locales.js');
```

---
