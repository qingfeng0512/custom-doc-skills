# Chrome-Extensions - Web Extensions

**Pages:** 151

---

## chrome.desktopCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/desktopCapture

**Contents:**
- chrome.desktopCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - DesktopCaptureSourceType
    - 枚举
  - SelfCapturePreferenceEnum
    - 枚举
  - SystemAudioPreferenceEnum
    - 枚举

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

用于定义 chooseDesktopMedia() 中所用的一组桌面媒体源的枚举。

镜像 SelfCapturePreferenceEnum。

镜像 SystemAudioPreferenceEnum。

镜像 WindowAudioPreferenceEnum。

隐藏由 chooseDesktopMedia() 显示的桌面媒体选择器对话框。

chooseDesktopMedia() 返回的 ID

DesktopCaptureSourceType[]

应向用户显示的一组来源。集合中的来源顺序决定了选择器中的标签页顺序。

创建数据流所针对的可选标签页。如果未指定，则只有调用扩展程序可以使用生成的流。该数据流只能由给定标签页中安全来源与 tab.url 相匹配的帧使用。标签页的来源必须是安全来源，例如 HTTPS。

一个不透明的字符串，可传递给 getUserMedia() API 以生成与用户选择的来源对应的媒体流。如果用户未选择任何来源（即取消了提示），则系统会使用空的 streamId 调用回调。创建的 streamId 只能使用一次，如果未使用，会在几秒后过期。

如果“audio”包含在参数来源中，并且最终用户未取消选中“分享音频”复选框，则为 true。否则为 false，在这种情况下，不应通过 getUserMedia 调用请求音频流。

一个 ID，如果需要取消提示，可以将其传递给 cancelChooseDesktopMedia()。

**Examples:**

Example 1 (unknown):
```unknown
chrome.desktopCapture.cancelChooseDesktopMedia(  desktopMediaRequestId: number,): void
```

Example 2 (unknown):
```unknown
chrome.desktopCapture.chooseDesktopMedia(  sources: DesktopCaptureSourceType[],  targetTab?: Tab,  callback: function,): number
```

Example 3 (javascript):
```javascript
(streamId: string, options: object) => void
```

---

## chrome.omnibox 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/omnibox?hl=zh-cn

**Contents:**
- chrome.omnibox 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - DefaultSuggestResult
    - 属性
  - DescriptionStyleType
    - 枚举
  - OnInputEnteredDisposition

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

当用户输入扩展程序的关键字后，便开始仅与您的扩展程序互动。每次按键操作都会发送到您的扩展程序，您可以提供建议作为响应。

建议可以采用多种方式进行丰富格式设置。当用户接受建议时，您的扩展程序会收到通知，并可以采取相应行动。

如需使用此 API，必须在清单中声明以下键。

您必须在清单中包含 "omnibox.keyword" 字段，才能使用多功能框 API。您还应指定一个 16x16 像素的图标，该图标会在建议用户进入关键字模式时显示在地址栏中。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 omnibox API 示例。

网址下拉菜单中显示的文字。可以包含用于设置样式的 XML 样式标记。支持的标记包括“url”（用于表示字面网址）、“match”（用于突出显示与用户查询匹配的文本）和“dim”（用于表示暗淡的辅助文本）。样式可以嵌套，例如“变暗的匹配项”。

多功能框查询的窗口处置。这是显示结果的推荐上下文。例如，如果多功能框命令是导航到某个网址，则“newForegroundTab”处置方式表示导航应在新选中的标签页中进行。

放入网址栏中的文本，当用户选择此条目时，该文本会发送给扩展程序。

网址下拉菜单中显示的文字。可以包含用于设置样式的 XML 样式标记。支持的标记包括“url”（用于表示字面网址）、“match”（用于突出显示与用户查询匹配的文本）和“dim”（用于表示暗淡的辅助文本）。样式可以嵌套，例如，调暗的匹配项。您必须转义这五个预定义实体，才能将其显示为文本：stackoverflow.com/a/1091953/89484

为默认建议设置说明和样式。默认建议是指显示在网址栏下方的第一个建议行中的文字。

不含“content”参数的部分 SuggestResult 对象。

OnInputEnteredDisposition

用户已通过输入扩展程序的关键字启动了关键字输入会话。保证在每个输入会话中发送一次，并且在任何 onInputChanged 事件之前发送。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Aaron's omnibox extension",
  "version": "1.0",
  "omnibox": { "keyword" : "aaron" },
  "icons": {
    "16": "16-full-color.png"
  },
  "background": {
    "persistent": false,
    "scripts": ["background.js"]
  }
}
```

Example 2 (unknown):
```unknown
chrome.omnibox.setDefaultSuggestion(  suggestion: DefaultSuggestResult,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.omnibox.onDeleteSuggestion.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(text: string) => void
```

---

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/declarativeNetRequest?hl=zh-cn

**Contents:**
- chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 规则和规则集
  - 动态规则集和会话级范围的规则集
  - 静态规则集
- 加急审核
- 启用和停用静态规则和规则集

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

“declarativeNetRequest”和“declarativeNetRequestWithHostAccess”权限提供相同的功能。它们之间的区别在于何时请求或授予权限。

除了前面所述的权限之外，某些类型的规则集（尤其是静态规则集）还需要声明 "declarative_net_request" 清单键，该键应是一个包含单个键（名为 "rule_resources"）的字典。此键是一个包含 Ruleset 类型字典的数组，如下所示。（请注意，由于“Ruleset”只是一个数组，因此不会显示在清单的 JSON 中。）本文档后面部分介绍了静态规则集。

如需使用此 API，请指定一个或多个规则集。规则集包含一个规则数组。单个规则可执行以下操作之一：

在使用扩展程序时，动态规则集和会话规则集通过 JavaScript 进行管理。

每种规则集类型只有一个。扩展程序可以通过调用 updateDynamicRules() 和 updateSessionRules() 动态添加或移除规则，前提是未超出规则限制。如需了解规则限制，请参阅规则限制。您可以在代码示例下查看相关示例。

与动态规则和会话规则不同，静态规则在安装或升级扩展程序时进行打包、安装和更新。它们以 JSON 格式存储在规则文件中，并使用 "declarative_net_request" 和 "rule_resources" 键（如上所述）以及一个或多个 Ruleset 字典向扩展程序指示。Ruleset 字典包含规则文件的路径、文件中包含的规则集的 ID，以及规则集是启用还是停用。当您以编程方式启用或停用规则集时，后两个属性非常重要。

如需测试规则文件，请以未打包的形式加载扩展程序。有关无效静态规则的错误和警告仅针对未打包的扩展程序显示。系统会忽略打包扩展程序中的无效静态规则。

对静态规则集的更改可能符合快速审核条件。请参阅符合条件的更改的加急审核。

在运行时，您可以启用或停用单个静态规则和完整的静态规则集。

已启用的静态规则和规则集的集合会在浏览器会话之间保持不变。这两者都不会在扩展程序更新后保留，这意味着只有您选择保留在规则文件中的规则会在更新后可用。

出于性能方面的原因，一次可启用的规则和规则集数量也有限制。调用 getAvailableStaticRuleCount() 以检查可启用的额外规则的数量。如需了解规则限制，请参阅规则限制。

如需启用或停用静态规则，请调用 updateStaticRules()。此方法接受一个 UpdateStaticRulesOptions 对象，其中包含要启用或停用的规则 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。停用的静态规则数量上限为 5,000 条。

如需启用或停用静态规则集，请调用 updateEnabledRulesets()。此方法接受一个 UpdateRulesetOptions 对象，其中包含要启用或停用的规则集 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

无论规则类型如何，规则都以四个字段开头，如下所示。虽然 "id" 和 "priority" 键采用的是数字，但 "action" 和 "condition" 键可以提供多个屏蔽和重定向条件。以下规则会屏蔽从 "foo.com" 发送到任何包含 "abc" 作为子字符串的网址的所有脚本请求。

Declarative Net Request 提供了使用模式匹配语法或正则表达式匹配网址的功能。

规则的 "condition" 键允许使用 "urlFilter" 键来处理指定网域下的网址。您可以使用模式匹配令牌创建模式。以下是一些示例。

条件也可以使用正则表达式。请参阅 "regexFilter" 键。如需了解适用于这些条件的限制，请参阅使用正则表达式的规则。

编写规则时，请务必确保规则始终与整个网域匹配。否则，您的规则可能会在意外情况下匹配。例如，使用模式匹配语法时：

同样，您可以使用 ^ 和 / 字符来锚定正则表达式。例如，^https:\/\/www\.google\.com\/ 与 https://www.google.com 上的任何路径匹配。

浏览器会在网络请求生命周期的各个阶段应用 DNR 规则。

在发出请求之前，扩展程序可以根据匹配的规则阻止或重定向（包括将方案从 HTTP 升级到 HTTPS）该请求。

对于每个扩展程序，浏览器都会确定一个匹配规则列表。此处未包含具有 modifyHeaders 操作的规则，因为这些规则将在稍后处理。此外，具有 responseHeaders 条件的规则将在稍后（当响应标头可用时）考虑，因此不包含在内。

然后，对于每个扩展程序，Chrome 每次请求最多选择一个候选对象。Chrome 会按优先级对所有匹配的规则进行排序，以找到匹配的规则。优先级相同的规则按操作排序（allow 或 allowAllRequests > block > upgradeScheme > redirect）。

如果候选规则是 allow 或 allowAllRequests 规则，或者发出请求的框架之前已匹配到此扩展程序中优先级更高或相同的 allowAllRequests 规则，则该请求会被“允许”，并且扩展程序不会对该请求产生任何影响。

如果有多个扩展程序想要阻止或重定向此请求，系统会选择要采取的单个操作。Chrome 会按 block > redirect 或 upgradeScheme > allow 或 allowAllRequests 的顺序对规则进行排序。如果两个规则属于同一类型，Chrome 会选择来自最近安装的扩展程序的规则。

在 Chrome 将请求标头发送到服务器之前，系统会根据匹配的 modifyHeaders 规则更新标头。

在单个扩展程序中，Chrome 会通过查找所有匹配的 modifyHeaders 规则来构建要执行的修改列表。与之前类似，仅包含优先级高于任何匹配的 allow 或 allowAllRequests 规则的规则。

Chrome 会按一定顺序应用这些规则，以便始终先评估最近安装的扩展程序的规则，然后再评估较旧的扩展程序的规则。此外，一个扩展程序中优先级较高的规则始终会先于同一扩展程序中优先级较低的规则应用。值得注意的是，即使在扩展程序之间：

收到响应标头后，Chrome 会评估具有 responseHeaders 条件的规则。

按 action 和 priority 对这些规则进行排序，并排除因匹配的 allow 或 allowAllRequests 规则而变得冗余的任何规则（此过程与“请求之前”中的步骤完全相同）后，Chrome 可能会代表扩展程序阻止或重定向请求。

请注意，如果请求到达此阶段，则表示该请求已发送到服务器，并且服务器已收到请求正文等数据。具有响应标头条件的屏蔽或重定向规则仍会运行，但实际上无法屏蔽或重定向请求。

对于屏蔽规则，发出请求的网页会收到屏蔽响应，并且 Chrome 会提前终止请求，从而处理这种情况。对于重定向规则，Chrome 会向重定向的网址发出新请求。请务必考虑这些行为是否符合您扩展程序的隐私权预期。

如果请求未被阻止或重定向，Chrome 会应用任何 modifyHeaders 规则。对响应标头应用修改的方式与“在发送请求标头之前”中所述的方式相同。由于请求已发出，因此对请求标头应用修改不会产生任何影响。

安全规则是指操作为 block、allow、allowAllRequests 或 upgradeScheme 的规则。这些规则受动态规则配额增加的限制。

在浏览器中加载和评估规则会产生性能开销，因此使用该 API 时会受到一些限制。限制取决于您使用的规则类型。

静态规则是指在清单文件中声明的规则文件中指定的规则。扩展程序最多可以在 "rule_resources" 清单键中指定 100 个静态规则集，但一次只能启用其中的 50 个规则集。后者称为 MAX_NUMBER_OF_ENABLED_STATIC_RULESETS。这些规则集总共至少包含 30,000 条规则。这称为 GUARANTEED_MINIMUM_STATIC_RULES。

之后可用的规则数量取决于用户浏览器上安装的所有扩展程序启用的规则数量。您可以在运行时通过调用 getAvailableStaticRuleCount() 找到此数字。您可以在代码示例下查看相关示例。

一个扩展程序最多可以有 5,000 条会话规则。这会作为 MAX_NUMBER_OF_SESSION_RULES 公开。

在 Chrome 120 之前，动态规则和会话规则的总数上限为 5, 000。

扩展程序可以至少有 5,000 条动态规则。这会作为 MAX_NUMBER_OF_UNSAFE_DYNAMIC_RULES 公开。

从 Chrome 121 开始，安全动态规则（以 MAX_NUMBER_OF_DYNAMIC_RULES 形式公开）的上限增加到 30,000 条。在 5000 条规则的限制范围内添加的任何不安全规则也会计入此限制。

在 Chrome 120 之前，动态规则和会话规则的总数上限为 5, 000。

所有类型的规则都可以使用正则表达式；不过，每种类型的正则表达式规则总数不得超过 1000 条。这称为 MAX_NUMBER_OF_REGEX_RULES。

此外，每条规则在编译后的大小必须小于 2KB。这与规则的复杂程度大致相关。如果您尝试加载超出此限制的规则，系统会显示如下警告，并忽略该规则。

declarativeNetRequest 仅适用于到达网络堆栈的请求。这包括来自 HTTP 缓存的响应，但不一定包括通过服务工作线程的 onfetch 处理程序的响应。declarativeNetRequest 不会影响由服务工作线程生成的响应或从 CacheStorage 检索的响应，但会影响在服务工作线程中对 fetch() 的调用。

declarativeNetRequest 规则无法将公开资源请求重定向到无法通过网络访问的资源。这样做会触发错误。即使指定的 Web 可访问资源归重定向扩展程序所有，也是如此。如需为 declarativeNetRequest 声明资源，请使用清单的 "web_accessible_resources" 数组。

仅支持对以下请求标头执行附加操作：accept、accept-encoding、accept-language、access-control-request-headers、cache-control、connection、content-language、cookie、forwarded、if-match、if-none-match、keep-alive、range、te、trailer、transfer-encoding、upgrade、user-agent、via、want-digest、x-forwarded-for。此许可名单区分大小写（bug 449152902）。

在附加到请求或响应标头时，浏览器会尽可能使用适当的分隔符。

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

返回给定 Ruleset 中当前已停用的静态规则列表。

GetDisabledRuleIdsOptions

返回扩展程序的当前动态规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

返回与扩展程序匹配的所有规则。调用方可以选择性地通过指定 filter 来过滤匹配规则的列表。此方法仅适用于具有 "declarativeNetRequestFeedback" 权限或已针对 filter 中指定的 tabId 授予 "activeTab" 权限的扩展程序。注意：如果规则未与有效文档相关联，且匹配时间超过 5 分钟，则不会返回该规则。

MatchedRulesFilter 可选

Promise<RulesMatchedDetails>

返回扩展程序的当前会话范围规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

检查给定的正则表达式是否会作为 regexFilter 规则条件受到支持。

Promise<IsRegexSupportedResult>

配置是否应将标签页的操作次数显示为扩展程序操作的徽章文本，并提供一种递增该操作次数的方法。

ExtensionActionOptions

检查扩展程序的任何 declarativeNetRequest 规则是否会与假设的请求匹配。注意：此方法仅适用于未打包的扩展程序，因为此方法仅用于扩展程序开发期间。

TestMatchRequestDetails

Promise<TestMatchOutcomeResult>

修改扩展程序的当前动态规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

更新扩展程序的已启用静态规则集。系统会先移除 options.disableRulesetIds 中列出的 ID 对应的规则集，然后再添加 options.enableRulesetIds 中列出的规则集。请注意，已启用的静态规则集会在会话之间保持不变，但不会在扩展程序更新之间保持不变，也就是说，rule_resources 清单键将决定每次扩展程序更新时已启用的静态规则集。

修改扩展程序的当前会话范围规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

停用和启用 Ruleset 中的各个静态规则。对已停用的 Ruleset 所属规则做出的更改将在该 Ruleset 下次启用时生效。

UpdateStaticRulesOptions

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
    "declarativeNetRequestFeedback"
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
rules_1.json: Rule with id 1 specified a more complex regex than allowed
as part of the "regexFilter" key.
```

---

## chrome.loginState 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/loginState?hl=zh-cn

**Contents:**
- chrome.loginState 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ProfileType
    - 枚举
  - SessionState
    - 枚举
- 方法

使用 chrome.loginState API 读取和监控登录状态。

“SIGNIN_PROFILE” 指定扩展程序位于登录资料中。

“USER_PROFILE” 指定扩展程序位于用户个人资料中。

“LOCK_PROFILE” 指定扩展程序位于锁定屏幕配置文件中。

“IN_OOBE_SCREEN” 指定用户处于开箱即用体验屏幕中。

“IN_LOGIN_SCREEN” 指定用户位于登录界面。

“IN_SESSION” 指定用户处于会话中。

“IN_LOCK_SCREEN” 指定用户处于锁定屏幕中。

“IN_RMA_SCREEN” 指定设备处于 RMA 模式，正在完成维修。

Promise<SessionState>

在会话状态发生变化时调度。sessionState 是新的会话状态。

**Examples:**

Example 1 (unknown):
```unknown
chrome.loginState.getProfileType(): Promise<ProfileType>
```

Example 2 (unknown):
```unknown
chrome.loginState.getSessionState(): Promise<SessionState>
```

Example 3 (unknown):
```unknown
chrome.loginState.onSessionStateChanged.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(sessionState: SessionState) => void
```

---

## chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/contextMenus?hl=zh-cn

**Contents:**
- chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - ContextType
    - 枚举
  - CreateProperties
    - 属性

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

您必须在扩展程序的清单中声明 "contextMenus" 权限才能使用该 API。此外，您还应指定一个 16x16 像素的图标，以便在菜单项旁边显示。例如：

上下文菜单项可以显示在任何文档（或文档中的框架）中，即使是具有 file:// 或 chrome:// 网址的文档也不例外。如需控制您的项可以显示在哪些文档中，请在调用 create() 或 update() 方法时指定 documentUrlPatterns 字段。

您可以根据需要创建任意数量的上下文菜单项，但如果您的扩展程序中有多个上下文菜单项同时显示，Google Chrome 会自动将它们收起到一个父菜单中。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 contextMenus API 示例。

菜单可显示的各种不同情境。指定“all”相当于指定除“launcher”之外的所有其他上下文的组合。“启动器”上下文仅受应用支持，用于向上下文菜单添加菜单项，该上下文菜单会在点击启动器/任务栏/Dock/等中的应用图标时显示。不同平台可能会对启动器上下文菜单中实际支持的内容施加限制。

复选框或单选按钮的初始状态：true 表示选中，false 表示未选中。在给定的组中，一次只能选择一个单选按钮。

[ContextType, ...ContextType[]] 可选

相应菜单项将显示在其中的上下文列表。默认为 ['page']。

将相应项限制为仅适用于网址与指定格式之一匹配的文档或框架。如需详细了解格式，请参阅匹配模式。

此上下文菜单项处于启用还是停用状态。默认为 true。

要分配给相应商品的唯一 ID。对于活动网页，此属性为必需属性。不能与此扩展程序的其他 ID 相同。

父菜单项的 ID；这会使相应项成为之前添加的项的子项。

与 documentUrlPatterns 类似，基于 img、audio 和 video 标记的 src 属性以及 a 标记的 href 属性的过滤条件。

要在商品中显示的文字；除非 type 为 separator，否则此属性为必需属性。当上下文为 selection 时，请在字符串中使用 %s 来显示所选文本。例如，如果此参数的值为“将‘%s’翻译为 Pig Latin”，并且用户选择了“cool”一词，则所选内容的上下文菜单项为“将‘cool’翻译为 Pig Latin”。

点击菜单项时调用的回调函数。此属性在 Service Worker 内不可用；您应改为为 contextMenus.onClicked 注册监听器。

有关所点击商品以及点击发生时所处情境的信息。

发生点击的标签页的详细信息。平台应用没有此参数。

一个标志，用于指示复选框或单选项目在点击后的状态。

一个标志，用于指示元素是否可编辑（文本输入、文本区域等）。

点击上下文菜单的元素的框架的 ID（如果该元素位于框架中）。

点击上下文菜单的元素的框架的网址（如果该元素位于框架中）。

如果上下文菜单是在以下类型的元素上激活的，则为“image”“video”或“audio”之一。

点击菜单项的网页的网址。如果点击发生在没有当前页面的情境中（例如在启动器上下文菜单中），则不会设置此属性。

对于具有“src”网址的元素，此属性将存在。

一个标志，用于指示复选框或单选按钮在被点击之前的状态。

可添加到扩展操作上下文菜单中的顶级扩展项的最大数量。超出此上限的任何内容都会被忽略。

创建新的上下文菜单项。如果在创建过程中发生错误，可能要等到创建回调触发时才能检测到；详细信息将包含在 runtime.lastError 中。

要更新的属性。接受与 contextMenus.create 函数相同的值。

[ContextType, ...ContextType[]] 可选

要设为相应商品父级的商品的 ID。注意：您无法将某个项目设置为其自身后代的子项。

发生点击的标签页的详细信息。平台应用没有此参数。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "contextMenus"
  ],
  "icons": {
    "16": "icon-bitty.png",
    "48": "icon-small.png",
    "128": "icon-large.png"
  },
  ...
}
```

Example 2 (javascript):
```javascript
(info: OnClickData, tab: Tab) => {...}
```

Example 3 (unknown):
```unknown
chrome.contextMenus.create(  createProperties: CreateProperties,  callback?: function,): number | string
```

Example 4 (unknown):
```unknown
chrome.contextMenus.remove(  menuItemId: string | number,): Promise<void>
```

---

## chrome.topSites 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/topSites

**Contents:**
- chrome.topSites 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 示例
- 类型
  - MostVisitedURL
    - 属性
- 方法
  - get()
    - 返回

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

您必须在扩展程序的清单中声明“topSites”权限，才能使用此 API。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 topSites API 示例。

封装最常访问网址的对象，例如新标签页上的默认快捷方式。

Promise<MostVisitedURL[]>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "topSites",
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.topSites.get(): Promise<MostVisitedURL[]>
```

---

## chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webNavigation

**Contents:**
- chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 活动顺序
  - 与 webRequest 事件的关系
  - 标签页 ID
  - 时间戳
  - 框架 ID
  - 过渡类型和限定符

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

所有 chrome.webNavigation 方法和事件都需要您在扩展程序清单中声明 "webNavigation" 权限。例如：

对于成功完成的导航，系统会按以下顺序触发事件：

如果在此过程中发生任何错误，系统会生成 onErrorOccurred 事件。对于特定导航，在 onErrorOccurred 之后不会再触发其他事件。

如果导航框架包含子框架，则其 onCommitted 会在任何子框架的 onBeforeNavigate 之前触发；而 onCompleted 会在所有子框架的 onCompleted 之后触发。

如果帧的参考 fragment 发生更改，则会触发 onReferenceFragmentUpdated 事件。此事件可以在 onDOMContentLoaded 之后的任何时间触发，甚至在 onCompleted 之后触发。

如果使用 History API 修改帧的状态（例如，使用 history.pushState()），系统会触发 onHistoryStateUpdated 事件。此事件可在 onDOMContentLoaded 之后的任何时间触发。

如果导航从往返缓存中恢复了网页，则不会触发 onDOMContentLoaded 事件。由于内容在首次访问网页时已完成加载，因此不会触发该事件。

如果导航是使用 Chrome Instant 或 Instant Pages 触发的，则会将完全加载的网页替换到当前标签页中。在这种情况下，系统会触发 onTabReplaced 事件。

webRequest API 的事件与 webNavigation API 的事件之间没有明确的顺序。对于已开始新导航的框架，仍有可能收到 webRequest 事件；或者，只有在网络资源已完全加载后，导航才会继续。

一般来说，webNavigation 事件与界面中显示的导航状态密切相关，而 webRequest 事件则对应于网络堆栈的状态，该状态通常对用户是不透明的。

并非所有导航标签页都对应于 Chrome 界面中的实际标签页，例如正在预渲染的标签页。您无法使用 tabs API 访问此类标签页，也无法通过调用 webNavigation.getFrame() 或 webNavigation.getAllFrames() 请求有关此类标签页的信息。一旦此类标签页被换入，系统就会触发 onTabReplaced 事件，并且可以通过这些 API 访问它们。

请务必注意，操作系统在处理不同的 Chrome 进程时存在一些技术上的怪异之处，可能会导致浏览器本身与扩展程序进程之间的时钟出现偏差。这意味着，WebNavigation 事件的 timeStamp 属性的 timeStamp 属性仅保证内部一致性。将一个事件与另一个事件进行比较会得出它们之间的正确偏移量，但将它们与扩展程序内的当前时间（例如使用 (new Date()).getTime()）进行比较可能会得出意外结果。

标签页中的框架可以通过框架 ID 来标识。主框架的框架 ID 始终为 0，子框架的 ID 为正数。在框架中构建文档后，其框架 ID 在文档的整个生命周期内保持不变。自 Chrome 49 起，此 ID 在框架的整个生命周期内（跨多次导航）也保持不变。

由于 Chrome 采用多进程架构，标签页可能会使用不同的进程来呈现网页的来源和目标。因此，如果导航在新进程中进行，您可能会同时收到来自新网页和旧网页的事件，直到新导航提交（即针对新的主框架发送 onCommitted 事件）为止。换句话说，可能会有多个具有相同 frameId 的待处理 webNavigation 事件序列。可以通过 processId 键区分序列。

另请注意，在临时加载期间，该进程可能会切换多次。当负载重定向到其他网站时，就会发生这种情况。在这种情况下，您会反复收到 onBeforeNavigate 和 onErrorOccurred 事件，直到收到最终的 onCommitted 事件。

扩展程序存在的另一个问题是框架的生命周期。框架托管文档（与已提交的网址相关联）。文档可能会发生变化（例如通过导航），但 frameId 不会变化，因此很难仅通过 frameId 将特定文档中发生的事情关联起来。我们引入了 documentId 的概念，它是每个文档的唯一标识符。如果框架被导航并打开新文档，标识符将会更改。此字段在确定网页何时更改其生命周期状态（在预渲染/有效/缓存之间）时非常有用，因为它保持不变。

webNavigation onCommitted 事件具有 transitionType 和 transitionQualifiers 属性。过渡类型与 History API 中使用的类型相同，用于描述浏览器如何导航到此特定网址。此外，还可以返回多个进一步定义导航的过渡限定符。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 webNavigation API 示例。

导航的原因。使用与 History API 中定义的相同的过渡类型。这些过渡类型与历史记录 API 中定义的过渡类型相同，只是将 "auto_toplevel" 替换为 "start_page"（为了实现向后兼容性）。

Promise<object[] | undefined>

检索有关指定帧的信息。框架是指网页的 <iframe> 或 <frame>，由标签页 ID 和框架 ID 标识。

相应文档的 UUID。如果提供了 frameId 和/或 tabId，系统会验证它们是否与通过提供的文档 ID 找到的文档相匹配。

现在，框架由其标签页 ID 和框架 ID 进行唯一标识；不再需要进程 ID，因此会忽略进程 ID。

Promise<object | undefined>

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。对于给定的标签页和进程，框架 ID 是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

此事件不再设置 processId，因为在 onCommit 之前，无法知道将呈现结果文档的进程。

浏览器即将开始导航的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在导航提交时触发。文档（以及其引用的资源，例如图片和子框架）可能仍在下载，但至少已从服务器收到部分文档，并且浏览器已决定切换到新文档。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当文档（包括其引用的资源）已完全加载并初始化时触发。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

文档完成加载的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当创建新窗口或现有窗口中的新标签页来托管导航时触发。

触发导航的具有 sourceTabId 的框架的 ID。0 表示主框架。

浏览器即将创建新视图的时间（以自纪元以来的毫秒数表示）。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当网页的 DOM 完全构建完毕时触发，但引用的资源可能尚未完成加载。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

网页的 DOM 完全构建的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在发生错误并中止导航时触发。如果发生网络错误或用户中止了导航，则可能会出现这种情况。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

发生错误的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当帧的历史记录更新为新网址时触发。相应框架的所有未来事件都将使用更新后的网址。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在帧的引用 fragment 更新时触发。相应框架的所有未来事件都将使用更新后的网址。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当标签页的内容被另一个（通常是之前预渲染的）标签页替换时触发。

替换发生的时间，以自纪元以来的毫秒数表示。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "webNavigation"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
onBeforeNavigate -> onCommitted -> [onDOMContentLoaded] -> onCompleted
```

Example 3 (unknown):
```unknown
chrome.webNavigation.getAllFrames(  details: object,): Promise<object[] | undefined>
```

Example 4 (unknown):
```unknown
chrome.webNavigation.getFrame(  details: object,): Promise<object | undefined>
```

---

## chrome.systemLog 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/systemLog?hl=zh-cn

**Contents:**
- chrome.systemLog 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - MessageOptions
    - 属性
- 方法
  - add()
    - 参数

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

**Examples:**

Example 1 (unknown):
```unknown
chrome.systemLog.add(  options: MessageOptions,): Promise<void>
```

---

## 在沙盒化 iframe 中使用 eval() 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/security/sandboxing-eval

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

## chrome.devtools.performance 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/performance

**Contents:**
- chrome.devtools.performance 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 概念和用法
- 示例
- 事件
  - onProfilingStarted
    - 参数
  - onProfilingStopped
    - 参数

使用 chrome.devtools.performance API 监听开发者工具“性能”面板中的录制状态更新。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

借助 chrome.devtools.performance API，开发者可以与 Chrome DevTools 中 Performance 面板的录制功能进行互动。您可以使用此 API 在录制开始或停止时收到通知。

通过监听这些事件，开发者可以创建会响应性能面板中的录制状态的扩展程序，在性能分析期间提供额外的自动化功能。

您可以通过以下方式使用此 API 监听录制状态更新

**Examples:**

Example 1 (javascript):
```javascript
chrome.devtools.performance.onProfilingStarted.addListener(() => {
  // Profiling started listener implementation
});

chrome.devtools.performance.onProfilingStopped.addListener(() => {
  // Profiling stopped listener implementation
})
```

Example 2 (unknown):
```unknown
chrome.devtools.performance.onProfilingStarted.addListener(  callback: function,)
```

Example 3 (unknown):
```unknown
chrome.devtools.performance.onProfilingStopped.addListener(  callback: function,)
```

---

## chrome.input.ime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/input/ime?hl=zh-cn

**Contents:**
- chrome.input.ime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
- 类型
  - AssistiveWindowButton
    - 枚举
  - AssistiveWindowProperties
    - 属性

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

您必须在扩展程序清单中声明“input”权限，才能使用 input.ime API。例如：

以下代码创建了一个将输入的字母转换为大写的 IME。

设置为 true 可显示 AssistiveWindow，设置为 false 可隐藏。

用于指定文本字段操作的目标。一旦调用 onBlur，此 ID 就会失效。

是否应使用输入到文本字段中的文本来改进用户的输入建议。

相应文本字段所编辑的值的类型（文本、数字、网址等）

相应文本字段所编辑的值的类型（文本、数字、网址等）

请参阅 http://www.w3.org/TR/DOM-Level-3-Events/#events-KeyboardEvent

所按实体键的值。该值不受当前键盘布局或修饰键状态的影响。

已弃用的 HTML keyCode，这是一个与所按键相关联的未修改标识符的数值代码，具体取决于系统和实现。

（已弃用）请求的 ID。请改用 onKeyEvent 事件中的 requestId 参数。

输入法使用的一种菜单项，用于通过语言菜单与用户互动。

将传递给引用此 MenuItem 的回调的字符串。

菜单项的类型。分隔符之间的单选按钮被视为一组。

要添加或更新的 MenuItem。它们将按在数组中的顺序添加。

候选字词窗口的显示位置。如果设置为“cursor”，窗口会跟随光标。如果设置为“composition”，则窗口锁定到合成的开头。

清除当前乐曲。如果此扩展服务不拥有有效的 IME，则会失败。

从光标位置开始删除的偏移量。此值可以为负数。

隐藏由系统自动弹出的输入视图窗口。如果输入视图窗口已隐藏，此函数将不执行任何操作。

表示 onKeyEvent 收到的按键事件已得到处理。仅当 onKeyEvent 监听器为异步时才应调用此方法。

已处理的事件的请求 ID。此值应来自 keyEvent.requestId

如果按键操作已处理，则为 true；否则为 false

发送按键事件。此函数预计将由虚拟键盘使用。当用户按下虚拟键盘上的某个键时，此函数用于将该事件传播到系统。

将发送按键事件的上下文的 ID，如果为零，则将按键事件发送到非输入字段。

AssistiveWindowButton

AssistiveWindowProperties

设置当前候选字词列表。如果此扩展程序不拥有有效的 IME，则此方法会失败

显示在候选对象旁边的短字符串，通常是快捷键或索引

设置候选窗口的属性。如果扩展程序不拥有活跃的 IME，则此方法会失败

如果为 true，则显示辅助文本；如果为 false，则隐藏辅助文本。

设置为 true 可显示光标，设置为 false 可隐藏光标。

如果候选窗口应垂直呈现，则为 True；如果应水平呈现，则为 False。

如果为 true，则显示候选字窗口；如果为 false，则隐藏候选字窗口。

设置当前合成。如果此扩展服务不拥有有效的 IME，则会失败。

设置候选字窗口中光标的位置。如果此扩展程序不拥有有效的 IME，则此方法不执行任何操作。

当此 IME 处于活动状态时，将提供的菜单项添加到语言菜单。

此事件在 IME 处于活动状态时发送。它表示 IME 将接收 onKeyPress 事件。

当辅助窗口中的按钮被点击时，系统会发送此事件。

AssistiveWindowButton

此事件在焦点离开文本框时发送。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

如果此扩展程序拥有有效的 IME，则会发送此事件。

此事件在 IME 被停用时发送。表示 IME 将不再接收 onKeyPress 事件。

当焦点进入文本框时，系统会发送此事件。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

当当前 InputContext 的属性（例如类型）发生更改时，系统会发送此事件。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

当操作系统发送按键事件时触发。如果扩展程序拥有有效的 IME，则事件将发送到该扩展程序。如果事件已处理，监听器函数应返回 true；如果未处理，则应返回 false。如果事件将异步评估，则此函数必须返回未定义的值，并且 IME 必须稍后使用结果调用 keyEventHandled()。

当 Chrome 终止正在进行的文本输入会话时，系统会发送此事件。

当插入符号周围的可编辑字符串发生变化或插入符号位置发生变化时调用。每个来回方向的文字长度上限为 100 个字符。

所选内容的起始位置。此值表示光标位置（如果没有选择内容）。

所选内容的结束位置。此值表示光标位置（如果没有选择内容）。

text 的偏移位置。由于 text 仅包含光标周围的部分文本，因此 offset 表示 text 的第一个字符的绝对位置。

光标周围的文本。这只是输入字段中所有文本的一部分。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "input"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var context_id = -1;

chrome.input.ime.onFocus.addListener(function(context) {
  context_id = context.contextID;
});

chrome.input.ime.onKeyEvent.addListener(
  function(engineID, keyData) {
    if (keyData.type == "keydown" && keyData.key.match(/^[a-z]$/)) {
      chrome.input.ime.commitText({"contextID": context_id,
                                    "text": keyData.key.toUpperCase()});
      return true;
    } else {
      return false;
    }
  }
);
```

Example 3 (unknown):
```unknown
chrome.input.ime.clearComposition(  parameters: object,): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.input.ime.commitText(  parameters: object,): Promise<boolean>
```

---

## chrome.enterprise.hardwarePlatform 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/hardwarePlatform

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
    - 返回

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

获取硬件平台的制造商和型号，并在扩展程序获得授权后通过 callback 返回。

Promise<HardwarePlatformInfo>

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.hardwarePlatform.getHardwarePlatformInfo(): Promise<HardwarePlatformInfo>
```

---

## chrome.dom 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/dom?hl=zh-cn

**Contents:**
- chrome.dom 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 方法
  - openOrClosedShadowRoot()
    - 参数
    - 返回

使用 chrome.dom API 访问适用于扩展程序的特殊 DOM API

获取由指定元素托管的打开的影子根或封闭的影子根。如果该元素未附加影子根，它将返回 null。

请参阅 https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot

**Examples:**

Example 1 (unknown):
```unknown
chrome.dom.openOrClosedShadowRoot(  element: HTMLElement,): object
```

---

## chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/commands

**Contents:**
- chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概念和使用
  - 支持的键
  - 组合键要求
  - 处理命令事件
  - 操作命令
  - 范围
- 示例

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

如需使用此 API，必须在清单中声明以下键。

Commands API 允许扩展程序开发者定义特定命令，并将其绑定到默认的按键组合。扩展程序接受的每个命令都必须在扩展程序的清单中声明为 "commands" 对象的属性。

属性键用作命令的名称。命令对象可以采用两个属性。

一个可选属性，用于声明命令的默认键盘快捷键。如果省略，则命令将处于未绑定状态。此属性可以采用字符串值或对象值。

字符串值，用于指定应在所有平台上使用的默认键盘快捷键。

扩展程序可以包含许多命令，但最多只能指定四个建议的键盘快捷键。用户可以从 chrome://extensions/shortcuts 对话框中手动添加更多快捷方式。

以下键可用作命令快捷键。键定义区分大小写。尝试加载具有错误大小写键的扩展程序会导致安装时出现清单解析错误。

常规 - Comma、Period、Home、End、PageUp、PageDown、Space、Insert、Delete

箭头键 - Up、Down、Left、Right

媒体键 - MediaNextTrack、MediaPlayPause、MediaPrevTrack、MediaStop

Ctrl、Alt、Shift、MacCtrl（仅限 macOS）、Option（仅限 macOS）、Command（仅限 macOS）、Search（仅限 ChromeOS）

扩展命令快捷方式必须包含 Ctrl 或 Alt。

在许多 macOS 键盘上，Alt 指的是 Option 键。

在 macOS 上，您还可以使用 Command 或 MacCtrl 代替 Ctrl，并使用 Option 键代替 Alt（请参阅下一个项目符号）。

在 macOS 上，Ctrl 会自动转换为 Command。

Command 还可用于 "mac" 快捷方式，以明确指代 Command 键。

如需在 macOS 上使用 Control 键，请在定义 "mac" 快捷方式时将 Ctrl 替换为 MacCtrl。

在其他平台的组合中使用 MacCtrl 会导致验证错误，并阻止安装扩展程序。

Search 是 ChromeOS 专用的可选修饰符。

某些操作系统和 Chrome 快捷键（例如窗口管理）始终优先于扩展程序命令快捷键，并且无法被覆盖。

在服务工作器中，您可以使用 onCommand.addListener 将处理程序绑定到清单中定义的每个命令。例如：

_execute_action (Manifest V3)、_execute_browser_action (Manifest V2) 和 _execute_page_action (Manifest V2) 命令分别预留用于触发操作、浏览器操作或网页操作。这些命令不会像标准命令那样调度 command.onCommand 事件。

如果您需要根据弹出式窗口的打开情况采取行动，请考虑在弹出式窗口的 JavaScript 中监听 DOMContentLoaded 事件。

默认情况下，命令的范围限定为 Chrome 浏览器。这意味着，当浏览器未处于焦点状态时，命令快捷键处于非活动状态。从 Chrome 35 开始，扩展程序开发者可以选择将命令标记为“全局”。即使 Chrome 未处于焦点状态，全局命令也能正常运行。

全局命令的键盘快捷键建议数量上限为 Ctrl+Shift+[0..9]。这是一项保护措施，旨在最大限度地降低覆盖其他应用中的快捷方式的风险，因为如果允许 Alt+P 作为全局快捷方式，那么在其他应用中，用于打开打印对话框的键盘快捷方式可能无法正常使用。

最终用户可以使用 chrome://extensions/shortcuts 中显示的界面，将全局命令重新映射到自己喜欢的按键组合。

以下示例展示了 Commands API 的核心功能。

命令允许扩展程序将逻辑映射到可由用户调用的键盘快捷键。最基本的命令只需要在扩展程序的清单中声明命令并注册监听器，如以下示例所示。

如概念和使用情况部分中所述，您还可以将命令映射到扩展程序的动作。以下示例注入了一个内容脚本，当用户点击扩展程序的操作或触发键盘快捷键时，该脚本会在当前页面上显示提醒。

如果某个扩展程序尝试注册的快捷键已被另一个扩展程序使用，则第二个扩展程序的快捷键将无法按预期注册。您可以预料到这种可能性，并在安装时检查是否存在冲突，从而提供更可靠的最终用户体验。

相应命令的有效快捷键，如果无有效快捷键，则为空白。

返回相应扩展程序的所有已注册的扩展程序命令及其快捷方式（如果处于有效状态）。在 Chrome 110 之前，此命令不会返回 _execute_action。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "commands": {
    "run-foo": {
      "suggested_key": {
        "default": "Ctrl+Shift+Y",
        "mac": "Command+Shift+Y"
      },
      "description": "Run \"foo\" on the current page."
    },
    "_execute_action": {
      "suggested_key": {
        "windows": "Ctrl+Shift+Y",
        "mac": "Command+Shift+Y",
        "chromeos": "Ctrl+Shift+U",
        "linux": "Ctrl+Shift+J"
      }
    }
  },
  ...
}
```

Example 2 (javascript):
```javascript
chrome.commands.onCommand.addListener((command) => {
  console.log(`Command: ${command}`);
});
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "commands": {
    "toggle-feature-foo": {
      "suggested_key": {
        "default": "Ctrl+Shift+5"
      },
      "description": "Toggle feature foo",
      "global": true
    }
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "Command demo - basic",
  "version": "1.0",
  "manifest_version": 3,
  "background": {
    "service_worker": "service-worker.js"
  },
  "commands": {
    "inject-script": {
      "suggested_key": "Ctrl+Shift+Y",
      "description": "Inject a script on the page"
    }
  }
}
```

---

## chrome.types 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/types

**Contents:**
- chrome.types 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- Chrome 浏览器设置
  - 范围和生命周期
  - 优先级
- 类型
  - ChromeSetting
    - 属性
  - ChromeSettingScope
    - 枚举

chrome.types API 包含 Chrome 的类型声明。

ChromeSetting 类型提供了一组通用函数（get()、set() 和 clear()），以及 Chrome 浏览器设置的事件发布者 (onChange)。代理设置示例演示了这些函数的预期使用方式。

Chrome 会区分三种不同的浏览器设置范围：

Chrome 会在不同层级管理设置。以下列表按优先级升序介绍了可能会影响有效设置的层。

正如列表所示，政策可能会取代您通过扩展程序指定的任何更改。您可以使用 get() 函数来确定扩展程序是否能够提供设置，或者此设置是否会被覆盖。

如前所述，Chrome 允许为常规窗口和无痕式窗口使用不同的设置。以下示例说明了此行为。假设没有政策会替换这些设置，并且扩展程序可以为常规窗口 (R) 设置设置，也可以为无痕式窗口 (I) 设置设置。

如果有两个或更多扩展程序想要将同一设置设为不同的值，则最近安装的扩展程序优先于其他扩展程序。如果最近安装的扩展程序仅设置了 (I)，则常规窗口的设置可以由之前安装的扩展程序定义。

设置的有效值是指根据优先规则得出的值。它由 Chrome 使用。

允许访问 Chrome 浏览器设置的界面。相关示例请参见 accessibilityFeatures。

Event<functionvoidvoid>

onChange.addListener 函数如下所示：

更改后的值是否仅适用于无痕式浏览会话。 仅当用户在无痕模式下启用了扩展程序时，此属性才会存在。

ChromeSettingScope 可选

是否返回适用于无痕会话的值（默认值为 false）。

ChromeSettingScope 可选

相应设置的值。 请注意，每项设置都有特定的值类型，该类型会与设置一起说明。扩展程序不应设置其他类型的值。

ChromeSetting 的范围。以下权限之一：

"incognito_persistent"

"incognito_session_only"

"controlled_by_other_extensions"

"controllable_by_this_extension"

"controlled_by_this_extension"

**Examples:**

Example 1 (javascript):
```javascript
(callback: function) => {...}
```

Example 2 (javascript):
```javascript
(details: object) => void
```

Example 3 (javascript):
```javascript
(details: object) => {...}
```

Example 4 (javascript):
```javascript
(details: object) => {...}
```

---

## chrome.power 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/power?hl=zh-cn

**Contents:**
- chrome.power 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 类型
  - Level
    - 枚举
- 方法
  - releaseKeepAwake()
  - reportActivity()

使用 chrome.power API 可替换系统的电源管理功能。

默认情况下，操作系统会在用户处于非活动状态时调暗屏幕，并最终暂停系统。借助电源 API，应用或扩展程序可以使系统保持唤醒状态。

使用此 API，您可以指定停用电源管理的级别。"system" 级别可让系统保持活跃状态，但允许屏幕变暗或关闭。例如，即使屏幕处于关闭状态，通信应用也可以继续接收消息。"display" 级别可让屏幕和系统保持活跃状态。例如，电子书应用和演示应用可以在用户阅读时保持屏幕和系统处于活动状态。

当用户同时运行多个应用或扩展程序时，每个应用或扩展程序都有自己的能耗级别，此时系统会采用优先级最高的级别；"display" 的优先级始终高于 "system"。例如，如果应用 A 请求 "system" 电源管理，而应用 B 请求 "display"，则在应用 B 卸载或释放其请求之前，系统会使用 "display"。如果应用 A 仍处于活跃状态，则使用 "system"。

“system” 防止系统因用户不活动而进入休眠状态。

“display” 防止显示屏因用户不活动而关闭或变暗，或防止系统进入休眠状态。

释放之前通过 requestKeepAwake() 发出的请求。

报告用户活动，以便从屏幕变暗或关闭状态或从屏保唤醒屏幕。如果屏保当前处于活动状态，则退出屏保。

请求暂时停用电源管理。level 描述了应停用电源管理的程度。如果同一应用之前发出的请求仍处于有效状态，则会被新请求替换。

**Examples:**

Example 1 (unknown):
```unknown
chrome.power.releaseKeepAwake(): void
```

Example 2 (unknown):
```unknown
chrome.power.reportActivity(): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.power.requestKeepAwake(  level: Level,): void
```

---

## chrome.printerProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printerProvider?hl=zh-cn

**Contents:**
- chrome.printerProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - PrinterInfo
    - 属性
  - PrintError
    - 枚举
  - PrintJob

chrome.printerProvider API 公开了打印管理器用于查询由扩展程序控制的打印机、查询其功能以及向这些打印机提交打印作业的事件。

为响应 onPrintRequested 事件而返回的错误代码。

"INVALID_TICKET" 指定打印票券无效。例如，支持服务工单与某些功能不一致，或者扩展程序无法处理工单中的所有设置。

"INVALID_DATA" 指定文档无效。例如，数据可能已损坏，或者格式与扩展程序不兼容。

文档内容类型。支持的格式为 "application/pdf" 和 "image/pwg-raster"。

包含要打印的文档数据的 Blob。格式必须与“contentType”一致。

CJT 引用被标记为已弃用。此功能仅可用于 Google 云打印。未针对 ChromeOS 打印而弃用。

resultCallback 参数如下所示：

打印管理器请求扩展程序提供的打印机时会触发事件。

resultCallback 参数如下所示：

打印管理器请求有关可能是打印机的 USB 设备的信息时会触发事件。

注意：应用不应期望此事件在每台设备上触发多次。如果已连接的设备受支持，则应在 onGetPrintersRequested 事件中返回相应设备。

resultCallback 参数如下所示：

resultCallback 参数如下所示：

**Examples:**

Example 1 (unknown):
```unknown
chrome.printerProvider.onGetCapabilityRequested.addListener(  callback: function,)
```

Example 2 (javascript):
```javascript
(printerId: string, resultCallback: function) => void
```

Example 3 (javascript):
```javascript
(capabilities: object) => void
```

Example 4 (unknown):
```unknown
chrome.printerProvider.onGetPrintersRequested.addListener(  callback: function,)
```

---

## chrome.tabGroups 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabGroups?hl=zh-cn

**Contents:**
- chrome.tabGroups 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Color
    - 枚举
  - TabGroup
    - 属性
- 属性

使用 chrome.tabGroups API 与浏览器的标签页分组系统进行交互。您可以使用此 API 修改和重新排列浏览器中的标签页组。如需对标签页进行分组和取消分组，或查询哪些标签页位于分组中，请使用 chrome.tabs API。

群组是否已收起。收起的群组是指标签页处于隐藏状态的群组。

群组的 ID。组 ID 在浏览器会话中是唯一的。

将相应标签页组及其窗口中的所有标签页移至新窗口。

要将群组移至的位置。使用 -1 将群组放置在窗口末尾。

要将群组移至的窗口。默认为群组当前所在的窗口。请注意，群组只能在 windows.WindowType 类型为 "normal" 的窗口之间移动。

Promise<TabGroup | undefined>

获取具有指定属性的所有群组，如果未指定任何属性，则获取所有群组。

父窗口的 ID，或windows.WINDOW_ID_CURRENT（表示当前窗口）。

修改群组的属性。不会修改未在 updateProperties 中指定的属性。

Promise<TabGroup | undefined>

当群组在窗口内移动时触发。系统仍会针对群组中的各个标签页以及群组本身触发移动事件。当群组在窗口之间移动时，不会触发此事件；相反，系统会从一个窗口中移除该群组，并在另一个窗口中创建该群组。

当群组关闭时触发，无论是用户直接关闭还是因群组中不包含任何标签页而自动关闭。

**Examples:**

Example 1 (unknown):
```unknown
chrome.tabGroups.get(  groupId: number,): Promise<TabGroup>
```

Example 2 (unknown):
```unknown
chrome.tabGroups.move(  groupId: number,  moveProperties: object,): Promise<TabGroup | undefined>
```

Example 3 (unknown):
```unknown
chrome.tabGroups.query(  queryInfo: object,): Promise<TabGroup[]>
```

Example 4 (unknown):
```unknown
chrome.tabGroups.update(  groupId: number,  updateProperties: object,): Promise<TabGroup | undefined>
```

---

## chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/bookmarks

**Contents:**
- chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 对象和属性
  - 示例
- 类型
  - BookmarkTreeNode
    - 属性
  - BookmarkTreeNodeUnmodifiable

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

您必须在扩展程序清单中声明“书签”权限，才能使用书签 API。 例如：

书签以树状结构整理，树中的每个节点要么是书签，要么是文件夹（有时称为“组”）。树中的每个节点都由一个 bookmarks.BookmarkTreeNode 对象表示。

BookmarkTreeNode 属性在整个 chrome.bookmarks API 中使用。例如，当您调用 bookmarks.create 时，您会传入新节点的父节点 (parentId)，还可以选择性地传入节点的 index、title 和 url 属性。如需了解节点可以拥有的属性，请参阅 bookmarks.BookmarkTreeNode。

以下代码创建了一个标题为“扩展程序书签”的文件夹。create() 的第一个实参用于指定新文件夹的属性。第二个实参定义了在创建文件夹后要执行的函数。

以下代码段创建了一个指向扩展程序开发者文档的书签。由于创建书签失败不会造成任何不良后果，因此此代码无需定义回调函数。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 Bookmarks API 示例。

书签树中的节点（书签或文件夹）。子节点在其父文件夹中按顺序排列。

BookmarkTreeNode[] 可选

相应节点创建的时间，以自纪元 (new Date(dateAdded)) 以来的毫秒数表示。

相应文件夹的内容上次更改的时间（以自纪元以来经过的毫秒数表示）。

相应节点上次打开的时间（以自纪元以来经过的毫秒数表示）。未针对文件夹设置。

如果存在，则表示浏览器添加的文件夹，用户或扩展程序无法修改。如果此节点未设置 unmodifiable 属性，则可以修改子节点。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

每种文件夹类型的节点数量可能为零、一个或多个。浏览器可能会添加或移除文件夹，但无法通过扩展程序 API 执行此操作。

节点的唯一标识符。ID 在当前个人资料中是唯一的，即使在浏览器重启后仍保持有效。

相应节点是否已由浏览器与用户的远程账号存储空间同步。这可用于区分同一 FolderType 的账号级版本和仅限本地版本。现有节点上此属性的值可能会发生变化，例如，因用户操作而发生变化。

注意：此属性反映了节点是否已保存到浏览器的内置账号提供程序。即使此值为 false，节点也可能通过第三方进行同步。

对于受管节点（unmodifiable 设置为 true 的节点），此属性将始终为 false。

指明相应节点不可修改的原因。managed 值表示相应节点是由系统管理员或受监督用户的监护人配置的。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

用户点击书签时导航到的网址。对于文件夹，此属性会被省略。

指明相应节点不可修改的原因。值 managed 表示相应节点由系统管理员配置。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

“bookmarks-bar” 内容显示在浏览器窗口顶部的文件夹。

“其他” 在所有平台的完整书签列表中显示的书签。

“移动设备” 用户移动设备上通常可用的书签，但可通过扩展程序或在书签管理器中修改。

“受管理” 如果受监督用户的系统管理员或监护人已配置书签，则可能会显示此顶级文件夹。

在指定的 parentId 下创建书签或文件夹。如果网址为 NULL 或缺失，则为文件夹。

Promise<BookmarkTreeNode>

检索指定的 BookmarkTreeNode。

字符串 | [字符串, ...字符串 []]

单个字符串值 ID 或字符串值 ID 数组

Promise<BookmarkTreeNode[]>

检索指定 BookmarkTreeNode ID 的子级。

Promise<BookmarkTreeNode[]>

Promise<BookmarkTreeNode[]>

检索书签层次结构的一部分，从指定节点开始。

Promise<BookmarkTreeNode[]>

Promise<BookmarkTreeNode[]>

将指定的 BookmarkTreeNode 移动到提供的位置。

Promise<BookmarkTreeNode>

搜索与给定查询匹配的 BookmarkTreeNodes。使用对象指定的查询会生成与所有指定属性匹配的 BookmarkTreeNodes。

一个字符串（包含与书签网址和标题匹配的字词和带引号的短语）或一个对象。如果为对象，则可以指定属性 query、url 和 title，系统将生成与所有指定属性匹配的书签。

一个字符串，包含要与书签网址和标题进行匹配的字词和带引号的短语。

书签的网址；完全匹配。请注意，文件夹没有网址。

Promise<BookmarkTreeNode[]>

更新书签或文件夹的属性。仅指定要更改的属性；未指定的属性将保持不变。注意：目前仅支持“title”和“url”。

Promise<BookmarkTreeNode>

在书签或文件夹发生更改时触发。注意：目前，只有标题和网址更改会触发此操作。

当文件夹的子项因在界面中排序而更改顺序时触发。不会因调用 move() 而调用。

在开始书签导入会话时触发。在 onImportEnded 触发之前，开销大的观测器应忽略 onCreated 更新。观察者仍应立即处理其他通知。

当书签或文件夹被移至其他父级文件夹时触发。

在移除书签或文件夹时触发。以递归方式移除文件夹时，系统会针对该文件夹触发一次通知，而不会针对其内容触发通知。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "bookmarks"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.bookmarks.create(
  {'parentId': bookmarkBar.id, 'title': 'Extension bookmarks'},
  function(newFolder) {
    console.log("added folder: " + newFolder.title);
  },
);
```

Example 3 (unknown):
```unknown
chrome.bookmarks.create({
  'parentId': extensionsFolderId,
  'title': 'Extensions doc',
  'url': 'https://developer.chrome.com/docs/extensions',
});
```

Example 4 (unknown):
```unknown
chrome.bookmarks.create(  bookmark: CreateDetails,): Promise<BookmarkTreeNode>
```

---

## chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/sessions

**Contents:**
- chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - Device
    - 属性
  - Filter
    - 属性
  - Session
    - 属性

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

外部设备的打开窗口会话列表，按会话的修改时间从最近到最远排序。

相应列表中要提取的条目数上限。省略此参数可提取最大条目数 (sessions.MAX_SESSION_RESULTS)。

窗口或标签页关闭或修改的时间，以自纪元开始算起的秒数表示。

如果相应条目描述的是标签页，则为 tabs.Tab。系统会设置此值或 sessions.Session.window。

如果相应条目描述的是窗口，则为 windows.Window。系统会设置此值或 sessions.Session.tab。

请求的列表中将包含的 sessions.Session 的数量上限。

重新打开 windows.Window 或 tabs.Tab，并提供一个可选的回调函数，用于在条目恢复后运行。

要恢复的 windows.Window.sessionId 或 tabs.Tab.sessionId。如果未指定此参数，系统会恢复最近关闭的会话。

当最近关闭的标签页和/或窗口发生更改时触发。此事件不会监控同步会话更改。

**Examples:**

Example 1 (unknown):
```unknown
chrome.sessions.getDevices(  filter?: Filter,): Promise<Device[]>
```

Example 2 (unknown):
```unknown
chrome.sessions.getRecentlyClosed(  filter?: Filter,): Promise<Session[]>
```

Example 3 (unknown):
```unknown
chrome.sessions.restore(  sessionId?: string,): Promise<Session>
```

Example 4 (unknown):
```unknown
chrome.sessions.onChanged.addListener(  callback: function,)
```

---

## chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/alarms

**Contents:**
- chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 设备休眠
  - 持久性
- 示例
  - 设置闹钟
  - 响应闹钟
- 类型

使用 chrome.alarms API 可安排代码在指定时间或未来某个时间定期运行。

如需使用 chrome.alarms API，请在清单中声明 "alarms" 权限：

为确保可靠的行为，了解 API 的行为方式很有帮助。

设备处于休眠状态时，闹钟会继续运行。不过，闹钟不会唤醒设备。当设备唤醒时，所有错过的闹钟都会响铃。 重复闹钟最多会响一次，然后会根据指定周期重新安排闹钟，从设备唤醒时开始计时，不考虑自最初设置闹钟运行以来已经过去的时间。

警报通常会一直存在，直到扩展程序更新为止。不过，这无法保证，并且在浏览器重启时闹钟可能会被清除。因此，请确保每次服务工作线程启动时，该变量都存在。例如：

以下示例展示了如何使用闹钟以及如何响应闹钟。如需试用此 API，请从 chrome-extension-samples 代码库中安装 Alarm API 示例。

以下示例展示了如何在安装扩展程序时在 service worker 中设置闹钟：

以下示例根据响铃闹钟的名称设置操作工具栏图标。

如果不为 null，则表示闹钟为重复闹钟，将在 periodInMinutes 分钟后再次响铃。

相应闹钟预定触发的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。出于性能方面的考虑，闹钟可能会延迟任意时长。

在多长时间（以分钟为单位）后应触发 onAlarm 事件。

如果设置了该值，则在 when 或 delayInMinutes 指定的初始事件之后，每隔 periodInMinutes 分钟应触发一次 onAlarm 事件。如果未设置，闹钟将仅响铃一次。

闹钟应响铃的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。

创建闹钟。在 alarmInfo 指定的时间附近，系统会触发 onAlarm 事件。如果存在另一个同名（或未指定名称时为无名称）的闹钟，则该闹钟将被取消并替换为此闹钟。

为了减轻用户机器的负载，Chrome 将闹钟限制为最多每 30 秒触发一次，但可能会将闹钟延迟任意时长。也就是说，如果将 delayInMinutes 或 periodInMinutes 设置为小于 0.5 的值，系统将不会接受该值，并会发出警告。when 可以设置为“现在”之后的不到 30 秒，系统不会发出警告，但实际上至少要过 30 秒才会触发闹钟。

为了帮助您调试应用或扩展程序，当您以未打包的形式加载应用或扩展程序时，闹钟的触发频率不受限制。

用于标识相应闹钟的可选名称。默认为空字符串。

描述闹钟应在何时响铃。必须通过 when 或 delayInMinutes（但不能同时通过两者）指定初始时间。如果设置了 periodInMinutes，闹钟会在初始事件发生后每隔 periodInMinutes 分钟重复一次。如果未为重复闹钟设置 when 或 delayInMinutes，则 periodInMinutes 会用作 delayInMinutes 的默认值。

Promise<Alarm | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "alarms"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
async function checkAlarmState() {
  const alarm = await chrome.alarms.get("my-alarm");

  if (!alarm) {
    await chrome.alarms.create("my-alarm", { periodInMinutes: 1 });
  }
}

checkAlarmState();
```

Example 3 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(async ({ reason }) => {
  if (reason !== 'install') {
    return;
  }

  // Create an alarm so we have something to look at in the demo
  await chrome.alarms.create('demo-default-alarm', {
    delayInMinutes: 1,
    periodInMinutes: 1
  });
});
```

Example 4 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  chrome.action.setIcon({
    path: getIconPath(alarm.name),
  });
});
```

---

## chrome.instanceID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/instanceID?hl=zh-cn

**Contents:**
- chrome.instanceID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - deleteID()
    - 返回
  - deleteToken()
    - 参数
    - 返回

使用 chrome.instanceID 访问实例 ID 服务。

重置应用实例标识符并撤消与其关联的所有令牌。

检索生成 InstanceID 的时间。创建时间将由 callback 返回。

检索应用实例的标识符。实例 ID 将由 callback 返回。只要应用身份未被撤消或过期，就会返回相同的 ID。

返回一个令牌，允许经过授权的实体访问由范围定义的服务。

标识有权访问与此实例 ID 关联的资源的实体。可以是 Google 开发者控制台中的项目 ID。

允许包含少量将与令牌关联的字符串键值对，这些键值对可用于处理请求。

标识授权实体可以执行的授权操作。例如，对于发送 GCM 消息，应使用 GCM 范围。

**Examples:**

Example 1 (unknown):
```unknown
chrome.instanceID.deleteID(): Promise<void>
```

Example 2 (unknown):
```unknown
chrome.instanceID.deleteToken(  deleteTokenParams: object,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.instanceID.getCreationTime(): Promise<number>
```

Example 4 (unknown):
```unknown
chrome.instanceID.getID(): Promise<string>
```

---

## chrome.fontSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fontSettings?hl=zh-cn

**Contents:**
- chrome.fontSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - FontName
    - 属性
  - GenericFamily
    - 枚举

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

如需使用字体设置 API，您必须在扩展程序清单中声明 "fontSettings" 权限。例如：

Chrome 允许某些字体设置取决于某些通用字体系列和语言文字。例如，用于无衬线简体中文字体的字体可能与用于衬线日文字体的字体不同。

Chrome 支持的通用字体系列基于 CSS 通用字体系列，并列在 GenericReference 下。当网页指定了通用字体系列时，Chrome 会根据相应设置选择字体。如果未指定任何通用字体系列，Chrome 会使用“标准”通用字体系列的设置。

当网页指定语言时，Chrome 会根据相应语言文字的设置选择字体。如果未指定语言，Chrome 会使用默认脚本或全局脚本的设置。

受支持的语言文字由 ISO 15924 文字代码指定，并列在 ScriptCode 下。从技术上讲，Chrome 设置并非严格按脚本进行，还取决于语言。例如，当网页指定俄语时，Chrome 会选择西里尔文字体（ISO 15924 文字代码“Cyrl”），并且不仅将此字体用于西里尔文字，还会用于该字体涵盖的所有内容，例如拉丁文字。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 fontSettings API 示例。

以下值之一： not\_controllable：无法由任何扩展程序控制 controlled\_by\_other\_extensions：由优先级较高的扩展程序控制 controllable\_by\_this\_extension：可由此扩展程序控制 controlled\_by\_this\_extension：由此扩展程序控制

"controlled_by_other_extensions"

"controllable_by_this_extension"

"controlled_by_this_extension"

ISO 15924 文字代码。默认脚本（即全局脚本）由脚本代码“Zyyy”表示。

清除此扩展程序设置的默认固定字体大小（如果有）。

应清除字体的脚本。如果省略，则会清除全局脚本字体设置。

应检索字体的脚本。如果省略，则检索全局脚本（脚本代码“Zyyy”）的字体设置。

字体 ID。空字符串表示回退到全局脚本字体设置。

应设置的字体所对应的脚本代码。如果省略，则会设置全局脚本（脚本代码“Zyyy”）的字体设置。

字体 ID。请参阅 getFont 中的说明。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My Font Settings Extension",
  "description": "Customize your fonts",
  "version": "0.2",
  "permissions": [
    "fontSettings"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.fontSettings.getFont(
  { genericFamily: 'standard', script: 'Arab' },
  function(details) { console.log(details.fontId); }
);
```

Example 3 (unknown):
```unknown
chrome.fontSettings.setFont(
  { genericFamily: 'sansserif', script: 'Jpan', fontId: 'MS PGothic' }
);
```

Example 4 (unknown):
```unknown
chrome.fontSettings.clearDefaultFixedFontSize(  details?: object,): Promise<void>
```

---

## chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/cookies

**Contents:**
- chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 分区
- 示例
- 类型
  - Cookie
    - 属性
  - CookieDetails
    - 属性

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

如需使用 Cookie API，请在清单中声明 "cookies" 权限，并为要访问其 Cookie 的任何主机声明主机权限。例如：

借助分区 Cookie，网站可以标记某些 Cookie 应以顶级框架的来源为键。这意味着，举例来说，如果网站 A 通过 iframe 嵌入到网站 B 和网站 C 中，则来自 A 的分区 Cookie 的嵌入版本在 B 和 C 上可以具有不同的值。

默认情况下，所有 API 方法都针对未分区的 Cookie 运行。您可以使用 partitionKey 属性替换此行为。

如需详细了解分区对扩展程序的一般影响，请参阅存储空间和 Cookie。

您可以在 examples/api/cookies 目录中找到使用 Cookie API 的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

表示 HTTP Cookie 的相关信息。

Cookie 的网域（例如“www.google.com”“example.com”）。

Cookie 的过期日期，以自 UNIX 纪元以来的秒数表示。不适用于会话 Cookie。

如果 Cookie 是仅限主机使用的 Cookie（即请求的主机必须与 Cookie 的网域完全一致），则为 True。

如果 Cookie 被标记为 HttpOnly（即客户端脚本无法访问该 Cookie），则为 True。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

Cookie 的同站点状态（即是否随跨站请求发送 Cookie）。

如果 Cookie 被标记为“Secure”（即其范围仅限于安全渠道，通常为 HTTPS），则为 True。

如果 Cookie 是会话 Cookie（而非具有过期日期的持久性 Cookie），则为 True。

包含相应 Cookie 的 Cookie 存储区的 ID，如 getAllCookieStores() 中所提供。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

要查找 Cookie 的 Cookie 存储区的 ID。默认情况下，系统会使用当前执行上下文的 Cookie 存储区。

与要访问的 Cookie 关联的网址。此实参可以是完整网址，在这种情况下，网址路径后面的任何数据（例如查询字符串）都会被忽略。如果未在清单文件中指定相应网址的主机权限，API 调用将会失败。

指示 Cookie 是否是在跨网站情境中设置的。这样可以防止在跨网站情境中嵌入的顶级网站访问在同网站情境中由该顶级网站设置的 Cookie。

表示浏览器中的 Cookie 存储区。例如，无痕模式窗口使用的 Cookie 存储区与非无痕窗口使用的 Cookie 存储区不同。

共享此 Cookie 存储区的所有浏览器标签页的标识符。

相应文档的唯一标识符。如果提供了 frameId 和/或 tabId，系统会验证它们是否与通过提供的文档 ID 找到的文档相匹配。

Cookie 更改的根本原因。如果通过显式调用“chrome.cookies.remove”插入或移除了 Cookie，“cause”将为“explicit”。如果 Cookie 因过期而被自动移除，“原因”将为“已过期”。如果某个 Cookie 因被已过期的过期日期覆盖而遭到移除，“原因”将设置为“expired_overwrite”。如果 Cookie 因垃圾回收而自动移除，“原因”将为“逐出”。如果因“set”调用覆盖了某个 Cookie 而导致该 Cookie 被自动移除，“原因”将为“覆盖”。请相应地规划您的回答。

Cookie 的“SameSite”状态 (https://tools.ietf.org/html/draft-west-first-party-cookies)。“no_restriction”对应于使用“SameSite=None”设置的 Cookie，“lax”对应于“SameSite=Lax”，“strict”对应于“SameSite=Strict”。“未指定”对应于未设置 SameSite 属性的 Cookie。

检索单个 Cookie 的相关信息。如果指定网址存在多个同名 Cookie，则返回路径最长的那个。对于路径长度相同的 Cookie，系统会返回创建时间最早的 Cookie。

Promise<Cookie | undefined>

从单个 Cookie 存储区检索与给定信息匹配的所有 Cookie。返回的 Cookie 将按路径长度进行排序，路径最长的 Cookie 排在最前面。如果多个 Cookie 的路径长度相同，则创建时间最早的 Cookie 会排在前面。此方法仅检索扩展程序具有主机权限的网域的 Cookie。

将检索到的 Cookie 限制为网域与此网域匹配或为此网域的子网域的 Cookie。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

将检索到的 Cookie 限制为路径与此字符串完全匹配的 Cookie。

按 Secure 属性过滤 Cookie。

过滤掉会话 Cookie 与永久性 Cookie。

要从中检索 Cookie 的 Cookie 存储区。如果省略，则使用当前执行上下文的 Cookie 存储区。

将检索到的 Cookie 限制为与指定网址匹配的 Cookie。

Promise<CookieStore[]>

Promise<object | undefined>

使用给定的 Cookie 数据设置 Cookie；如果存在等效的 Cookie，可能会覆盖这些 Cookie。

有关正在设置的 Cookie 的详细信息。

相应 Cookie 的网域。如果省略，相应 Cookie 将成为仅限主机使用的 Cookie。

Cookie 的过期日期，以自 UNIX 纪元以来的秒数表示。如果省略，相应 Cookie 将成为会话 Cookie。

Cookie 是否应标记为 HttpOnly。默认值为 false。

相应 Cookie 的名称。如果省略，则默认为空。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

Cookie 的路径。默认为网址参数的路径部分。

Cookie 的同网站状态。默认为“unspecified”，即如果省略，则设置 Cookie 时不指定 SameSite 属性。

是否应将 Cookie 标记为“Secure”。默认值为 false。

要在其中设置 Cookie 的 Cookie 存储区的 ID。默认情况下，Cookie 会设置在当前执行上下文的 Cookie 存储区中。

要与 Cookie 设置相关联的 request-URI。此值可能会影响所创建 Cookie 的默认网域和路径值。如果未在清单文件中指定相应网址的主机权限，API 调用将会失败。

相应 Cookie 的值。如果省略，则默认为空。

Promise<Cookie | undefined>

在设置或移除 Cookie 时触发。作为一种特殊情况，请注意，更新 Cookie 的属性是通过两步流程实现的：首先完全移除要更新的 Cookie，生成“原因”为“覆盖”的通知。之后，系统会写入包含更新值的新 Cookie，并生成第二个通知，其中“原因”为“显式”。

有关已设置或已移除的 Cookie 的信息。

如果已移除 Cookie，则为 True。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "*://*.google.com/"
  ],
  "permissions": [
    "cookies"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.cookies.get(  details: CookieDetails,): Promise<Cookie | undefined>
```

Example 3 (unknown):
```unknown
chrome.cookies.getAll(  details: object,): Promise<Cookie[]>
```

Example 4 (unknown):
```unknown
chrome.cookies.getAllCookieStores(): Promise<CookieStore[]>
```

---

## chrome.enterprise.networkingAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/networkingAttributes

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
    - 返回

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

设备的本地 IPv4 地址（如果未配置，则为未定义）。

设备的本地 IPv6 地址（如果未配置，则为未定义）。

检索设备的默认网络的网络详细信息。如果用户没有关联或设备未连接到网络，系统将设置 runtime.lastError 并附上失败原因。

Promise<NetworkDetails>

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.networkingAttributes.getNetworkDetails(): Promise<NetworkDetails>
```

---

## chrome.accessibilityFeatures 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/accessibilityFeatures?hl=zh-cn

**Contents:**
- chrome.accessibilityFeatures 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 属性
  - animationPolicy
    - 类型
  - autoclick
    - 类型
  - caretHighlight
    - 类型

请使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 ChromeSetting 类型 API 原型来获取和设置各项无障碍功能。如需获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，该扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不隐含 accessibilityFeatures.read 权限。

get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<"allowed" | "once" | "none" >

鼠标停止移动后自动点击鼠标。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标颜色。该值用于指明功能是否已启用，并不表示其颜色。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

语音输入。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

固定放大镜。该值用于指明是否已启用停靠的放大镜功能。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

焦点突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

高对比度渲染模式。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

已放大的光标。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

全屏放大。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

随选朗读。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

语音反馈（文字转语音）。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

固定辅助键（例如 shift 或 alt）。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

“开关控制”。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

虚拟屏幕键盘。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

---

## chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/contentSettings?hl=zh-cn

**Contents:**
- chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 内容设置模式
  - 模式优先级
  - 主要模式和次要模式
  - 资源标识符
- 示例
- 类型

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

您必须在扩展程序的清单中声明 "contentSettings" 权限，才能使用该 API。例如：

您可以使用模式来指定每项内容设置所影响的网站。例如，https://*.youtube.com/* 指定了 youtube.com 及其所有子网域。内容设置模式的语法与匹配模式的语法相同，但存在以下几点差异：

如果有多条内容设置规则适用于特定网站，则具有更具体模式的规则优先适用。

如果一个模式在某个部分比另一个模式更具体，但在另一部分则不太具体，系统会按以下顺序检查不同的部分：主机名、方案、端口。例如，以下格式按优先级排序：

在决定应用哪项内容设置时，系统会考虑哪个网址取决于内容类型。 例如，对于 contentSettings.notifications，设置基于多功能框中显示的网址。此网址称为“主要”网址。

某些类型的内容可以考虑使用其他网址。例如，是否允许网站设置 contentSettings.cookies 取决于 HTTP 请求的网址（在本例中为主要网址）以及多功能框中显示的网址（称为“次要”网址）。

如果多条规则都具有主要模式和次要模式，则主要模式更具体的规则优先。如果多条规则具有相同的主要模式，则具有更具体的次要模式的规则优先。例如，以下主/次模式对列表按优先级排序：

借助资源标识符，您可以为内容类型的特定子类型指定内容设置。目前，唯一支持资源标识符的内容类型是 contentSettings.plugins，其中资源标识符用于标识特定插件。应用内容设置时，系统会先检查特定插件的设置。如果未找到特定插件的设置，系统会检查插件的一般内容设置。

例如，如果某项内容设置规则的资源标识符为 adobe-flash-player，模式为 <all_urls>，则即使模式 https://www.example.com/* 更具体，该规则也会优先于没有资源标识符且模式为 https://www.example.com/* 的规则。

您可以通过调用 contentSettings.ContentSetting.getResourceIdentifiers() 方法获取内容类型的资源标识符列表。返回的列表可能会因用户机器上安装的插件集而异，但 Chrome 会尽量在插件更新期间保持标识符稳定。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 contentSettings API 示例。

是否检查隐身会话的内容设置。（默认值为 false）

应检索内容设置的主要网址。请注意，主网址的含义取决于内容类型。

ResourceIdentifier 可选

应检索内容设置的辅助网址。默认为主要网址。请注意，辅助网址的含义取决于内容类型，并非所有内容类型都使用辅助网址。

getResourceIdentifiers 函数如下所示：

Promise<ResourceIdentifier[]>

主要网址的格式。如需详细了解模式的格式，请参阅内容设置模式。

ResourceIdentifier 可选

辅助网址的格式。默认情况下，系统会匹配所有网址。如需详细了解格式，请参阅内容设置格式。

相应规则所应用的设置。如需查看可能的值，请参阅各个 ContentSetting 对象的说明。

唯一使用资源标识符的内容类型是 contentSettings.plugins。如需了解详情，请参阅资源标识符。

ContentSetting 的范围。regular 之一：常规个人资料的设置（如果未在其他位置被覆盖，则无痕式个人资料会继承此设置）；incognito\_session\_only：无痕式个人资料的设置，只能在无痕式会话期间设置，并在无痕式会话结束时删除（会覆盖常规设置）。

"incognito_session_only"

是否允许网站自动下载多个文件。以下值之一：allow：允许网站自动下载多个文件；block：不允许网站自动下载多个文件；ask：在网站想要自动下载第一个文件后的其他文件时，询问用户。 默认值为 ask。主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<MultipleAutomaticDownloadsContentSetting>

是否允许网站使用 Private State Tokens API。allow 之一：允许网站使用 Private State Tokens API；block：禁止网站使用 Private State Tokens API。 默认值为 allow。调用 set() 时，主要网址格式必须为 <all_urls>。不使用辅助网址。

ContentSetting<AutoVerifyContentSetting>

是否允许网站访问摄像头。以下值之一：allow：允许网站访问摄像头；block：不允许网站访问摄像头；ask：当网站想要访问摄像头时进行询问。 默认值为 ask。主网址是请求相机访问权限的文档的网址。不使用辅助网址。 注意：如果两个模式均为“<all_urls>”，则“allow”设置无效。

ContentSetting<CameraContentSetting>

是否允许网站通过 Async Clipboard API 的高级功能访问剪贴板。“高级”功能包括在用户手势之后写入内置格式以外的任何内容，即读取能力、写入自定义格式的能力以及在没有用户手势的情况下写入的能力。以下值之一：allow：允许网站使用高级剪贴板功能；block：不允许网站使用高级剪贴板功能；ask：当网站想要使用高级剪贴板功能时进行询问。 默认值为 ask。主网址是指请求剪贴板访问权限的文档的网址。不使用辅助网址。

ContentSetting<ClipboardContentSetting>

是否允许网站设置 Cookie 和其他本地数据。以下值之一：allow：接受 Cookie；block：阻止 Cookie；session\_only：仅接受当前会话的 Cookie。 默认值为 allow。主网址是指表示 Cookie 源站的网址。辅助网址是顶级框架的网址。

ContentSetting<CookiesContentSetting>

已弃用。不再有任何效果。系统现在会自动为所有网站授予全屏权限。值始终为 allow。

ContentSetting<FullscreenContentSetting>

是否显示图片。以下值之一： allow：显示图片 block：不显示图片。 默认值为 allow。 主网址是顶级框架的网址。辅助网址是图片的网址。

ContentSetting<ImagesContentSetting>

是否运行 JavaScript。以下值之一：allow：运行 JavaScript；block：不运行 JavaScript。默认值为 allow。 主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<JavascriptContentSetting>

是否允许地理定位。allow：允许网站跟踪您的实际位置。 block：不允许网站跟踪您的实际位置。 ask：在允许网站跟踪您的实际位置之前先询问。 默认值为 ask。主网址是请求位置数据的文档的网址。辅助网址是顶级框架的网址（可能与请求网址相同，也可能不同）。

ContentSetting<LocationContentSetting>

是否允许网站使用麦克风。以下选项之一：allow：允许网站访问麦克风；block：不允许网站访问麦克风；ask：在网站想要访问麦克风时进行询问。 默认值为 ask。主网址是指请求麦克风访问权限的文档的网址。不使用辅助网址。 注意：如果两个模式均为“<all_urls>”，则“allow”设置无效。

ContentSetting<MicrophoneContentSetting>

已弃用。不再有任何效果。现在，系统会自动为所有网站授予鼠标锁定权限。值始终为 allow。

ContentSetting<MouselockContentSetting>

是否允许网站显示桌面通知。以下值之一：allow：允许网站显示桌面通知；block：不允许网站显示桌面通知；ask：当网站想要显示桌面通知时进行询问。 默认值为 ask。主网址是指想要显示通知的文档的网址。不使用辅助网址。

ContentSetting<NotificationsContentSetting>

已弃用。由于 Chrome 88 中移除了 Flash 支持，此权限不再有任何作用。值始终为 block。对 set() 和 clear() 的调用将被忽略。

ContentSetting<PluginsContentSetting>

是否允许网站显示弹出式窗口。以下值之一：allow：允许网站显示弹出式窗口；block：不允许网站显示弹出式窗口。 默认值为 block。 主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<PopupsContentSetting>

已弃用。之前，此权限用于控制是否允许网站在沙盒外运行插件，不过，随着 Chrome 88 中移除了 Flash 代理进程，此权限不再有任何作用。值始终为 block。对 set() 和 clear() 的调用将被忽略。

ContentSetting<PpapiBrokerContentSetting>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "contentSettings"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
(details: object) => {...}
```

Example 3 (javascript):
```javascript
(details: object) => {...}
```

Example 4 (javascript):
```javascript
() => {...}
```

---

## chrome.identity 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/identity

**Contents:**
- chrome.identity 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - AccountInfo
    - 属性
  - AccountStatus
    - 枚举
  - GetAuthTokenResult
    - 属性

使用 chrome.identity API 获取 OAuth2 访问令牌。

相应账号的唯一标识符。此 ID 在账号的整个生命周期内都不会发生变化。

“ANY” 指定是否存在主账号（如果有）。

已登录到相应个人资料的主账号的状态，应返回该状态的 ProfileUserInfo。默认为 SYNC 账号状态。

当前配置文件中登录的用户账号的电子邮件地址。如果用户未登录或未指定 identity.email 清单权限，则为空。

相应账号的唯一标识符。此 ID 在账号的整个生命周期内都不会发生变化。如果用户未登录，或者（在 M41 及更高版本中）未指定 identity.email 清单权限，则为空。

应返回其令牌的账号 ID。如果未指定，该函数将使用 Chrome 个人资料中的账号：如果有同步账号，则使用该账号；否则，使用第一个 Google Web 账号。

借助 enableGranularPermissions 标志，扩展程序可以提前选择启用精细的权限请求页面，在该页面中，系统会单独授予或拒绝所请求的权限。

获取令牌可能需要用户登录 Chrome 或批准应用请求的范围。如果互动标志为 true，getAuthToken 将根据需要提示用户。当标志为 false 或省略时，每当需要提示时，getAuthToken 都会返回失败。

如果存在 scopes 字段，则该字段会替换 manifest.json 中指定的范围列表。

是否在页面加载后终止非交互式请求的 launchWebAuthFlow。此参数不会影响互动式流程。

如果设置为 true（默认值），则流程会在网页加载后立即终止。如果设置为 false，则只有在 timeoutMsForNonInteractive 通过后，流程才会终止。对于使用 JavaScript 在网页加载后执行重定向的身份提供方，此功能非常有用。

由于某些授权流程可能会立即重定向到结果网址，因此 launchWebAuthFlow 会隐藏其 WebView，直到第一次导航重定向到最终网址，或完成加载要显示的网页。

如果 interactive 标志为 true，则在页面加载完成后显示窗口。如果标志为 false 或被省略，如果初始导航未完成流程，launchWebAuthFlow 将返回错误。

对于使用 JavaScript 进行重定向的流程，可以将 abortOnLoadForNonInteractive 设置为 false，同时设置 timeoutMsForNonInteractive，以便网页有机会执行任何重定向。

以毫秒为单位，launchWebAuthFlow 是允许在非互动模式下运行的总时长上限。仅当 interactive 为 false 时才有效。

检索描述相应个人资料中存在的账号的 AccountInfo 对象列表。

getAccounts 仅在开发版渠道中受支持。

Promise<AccountInfo[]>

使用 manifest.json 的 oauth2 部分中指定的客户端 ID 和范围获取 OAuth2 访问令牌。

Identity API 会在内存中缓存访问令牌，因此可以在需要令牌时随时以非互动方式调用 getAuthToken。令牌缓存会自动处理过期问题。

为了提供良好的用户体验，请务必在应用中通过界面发起互动式令牌请求，说明授权的用途。如果不这样做，您的用户会收到授权请求，或者如果他们未登录，则会看到 Chrome 登录界面，但没有任何上下文。尤其是，请勿在应用首次启动时以交互方式使用 getAuthToken。

注意：如果使用回调调用此函数，此函数不会返回对象，而是会将这两个属性作为单独的实参传递给回调。

Promise<GetAuthTokenResult>

检索已登录个人资料的用户的电子邮件地址和经过混淆处理的 GAIA ID。

需要 identity.email 清单权限。否则，返回空结果。

此 API 在以下两个方面与 identity.getAccounts 不同。返回的信息可离线使用，并且仅适用于相应个人资料的主要账号。

Promise<ProfileUserInfo>

生成要在 launchWebAuthFlow 中使用的重定向网址。

生成的网址与格式 https://<app-id>.chromiumapp.org/* 相匹配。

此方法通过启动 WebView 并将其导航到提供商的身份验证流程中的第一个网址，来实现与非 Google 身份提供商的身份验证流程。当提供方重定向到与模式 https://<app-id>.chromiumapp.org/* 匹配的网址时，窗口将关闭，并且最终重定向网址将传递给 callback 函数。

为了提供良好的用户体验，请务必在应用中通过界面启动互动式授权流程，说明授权的用途。如果不这样做，您的用户将收到没有上下文的授权请求。尤其是，请勿在应用首次启动时启动互动式身份验证流程。

Promise<string | undefined>

从 Identity API 的令牌缓存中移除 OAuth2 访问令牌。

如果发现访问令牌无效，应将其传递给 removeCachedAuthToken 以从缓存中移除。然后，应用可以使用 getAuthToken 检索新令牌。

当用户个人资料中某个账号的登录状态发生变化时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.identity.clearAllCachedAuthTokens(): Promise<void>
```

Example 2 (unknown):
```unknown
chrome.identity.getAccounts(): Promise<AccountInfo[]>
```

Example 3 (unknown):
```unknown
chrome.identity.getAuthToken(  details?: TokenDetails,): Promise<GetAuthTokenResult>
```

Example 4 (unknown):
```unknown
chrome.identity.getProfileUserInfo(  details?: ProfileDetails,): Promise<ProfileUserInfo>
```

---

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/declarativeNetRequest

**Contents:**
- chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 规则和规则集
  - 动态规则集和会话级范围的规则集
  - 静态规则集
- 加急审核
- 启用和停用静态规则和规则集

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

“declarativeNetRequest”和“declarativeNetRequestWithHostAccess”权限提供相同的功能。它们之间的区别在于何时请求或授予权限。

除了前面所述的权限之外，某些类型的规则集（尤其是静态规则集）还需要声明 "declarative_net_request" 清单键，该键应是一个包含单个键（名为 "rule_resources"）的字典。此键是一个包含 Ruleset 类型字典的数组，如下所示。（请注意，由于“Ruleset”只是一个数组，因此不会显示在清单的 JSON 中。）本文档后面部分介绍了静态规则集。

如需使用此 API，请指定一个或多个规则集。规则集包含一个规则数组。单个规则可执行以下操作之一：

在使用扩展程序时，动态规则集和会话规则集通过 JavaScript 进行管理。

每种规则集类型只有一个。扩展程序可以通过调用 updateDynamicRules() 和 updateSessionRules() 动态添加或移除规则，前提是未超出规则限制。如需了解规则限制，请参阅规则限制。您可以在代码示例下查看相关示例。

与动态规则和会话规则不同，静态规则在安装或升级扩展程序时进行打包、安装和更新。它们以 JSON 格式存储在规则文件中，并使用 "declarative_net_request" 和 "rule_resources" 键（如上所述）以及一个或多个 Ruleset 字典向扩展程序指示。Ruleset 字典包含规则文件的路径、文件中包含的规则集的 ID，以及规则集是启用还是停用。当您以编程方式启用或停用规则集时，后两个属性非常重要。

如需测试规则文件，请以未打包的形式加载扩展程序。有关无效静态规则的错误和警告仅针对未打包的扩展程序显示。系统会忽略打包扩展程序中的无效静态规则。

对静态规则集的更改可能符合快速审核条件。请参阅符合条件的更改的加急审核。

在运行时，您可以启用或停用单个静态规则和完整的静态规则集。

已启用的静态规则和规则集的集合会在浏览器会话之间保持不变。这两者都不会在扩展程序更新后保留，这意味着只有您选择保留在规则文件中的规则会在更新后可用。

出于性能方面的原因，一次可启用的规则和规则集数量也有限制。调用 getAvailableStaticRuleCount() 以检查可启用的额外规则的数量。如需了解规则限制，请参阅规则限制。

如需启用或停用静态规则，请调用 updateStaticRules()。此方法接受一个 UpdateStaticRulesOptions 对象，其中包含要启用或停用的规则 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。停用的静态规则数量上限为 5,000 条。

如需启用或停用静态规则集，请调用 updateEnabledRulesets()。此方法接受一个 UpdateRulesetOptions 对象，其中包含要启用或停用的规则集 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

无论规则类型如何，规则都以四个字段开头，如下所示。虽然 "id" 和 "priority" 键采用的是数字，但 "action" 和 "condition" 键可以提供多个屏蔽和重定向条件。以下规则会屏蔽从 "foo.com" 发送到任何包含 "abc" 作为子字符串的网址的所有脚本请求。

Declarative Net Request 提供了使用模式匹配语法或正则表达式匹配网址的功能。

规则的 "condition" 键允许使用 "urlFilter" 键来处理指定网域下的网址。您可以使用模式匹配令牌创建模式。以下是一些示例。

条件也可以使用正则表达式。请参阅 "regexFilter" 键。如需了解适用于这些条件的限制，请参阅使用正则表达式的规则。

编写规则时，请务必确保规则始终与整个网域匹配。否则，您的规则可能会在意外情况下匹配。例如，使用模式匹配语法时：

同样，您可以使用 ^ 和 / 字符来锚定正则表达式。例如，^https:\/\/www\.google\.com\/ 与 https://www.google.com 上的任何路径匹配。

浏览器会在网络请求生命周期的各个阶段应用 DNR 规则。

在发出请求之前，扩展程序可以根据匹配的规则阻止或重定向（包括将方案从 HTTP 升级到 HTTPS）该请求。

对于每个扩展程序，浏览器都会确定一个匹配规则列表。此处未包含具有 modifyHeaders 操作的规则，因为这些规则将在稍后处理。此外，具有 responseHeaders 条件的规则将在稍后（当响应标头可用时）考虑，因此不包含在内。

然后，对于每个扩展程序，Chrome 每次请求最多选择一个候选对象。Chrome 会按优先级对所有匹配的规则进行排序，以找到匹配的规则。优先级相同的规则按操作排序（allow 或 allowAllRequests > block > upgradeScheme > redirect）。

如果候选规则是 allow 或 allowAllRequests 规则，或者发出请求的框架之前已匹配到此扩展程序中优先级更高或相同的 allowAllRequests 规则，则该请求会被“允许”，并且扩展程序不会对该请求产生任何影响。

如果有多个扩展程序想要阻止或重定向此请求，系统会选择要采取的单个操作。Chrome 会按 block > redirect 或 upgradeScheme > allow 或 allowAllRequests 的顺序对规则进行排序。如果两个规则属于同一类型，Chrome 会选择来自最近安装的扩展程序的规则。

在 Chrome 将请求标头发送到服务器之前，系统会根据匹配的 modifyHeaders 规则更新标头。

在单个扩展程序中，Chrome 会通过查找所有匹配的 modifyHeaders 规则来构建要执行的修改列表。与之前类似，仅包含优先级高于任何匹配的 allow 或 allowAllRequests 规则的规则。

Chrome 会按一定顺序应用这些规则，以便始终先评估最近安装的扩展程序的规则，然后再评估较旧的扩展程序的规则。此外，一个扩展程序中优先级较高的规则始终会先于同一扩展程序中优先级较低的规则应用。值得注意的是，即使在扩展程序之间：

收到响应标头后，Chrome 会评估具有 responseHeaders 条件的规则。

按 action 和 priority 对这些规则进行排序，并排除因匹配的 allow 或 allowAllRequests 规则而变得冗余的任何规则（此过程与“请求之前”中的步骤完全相同）后，Chrome 可能会代表扩展程序阻止或重定向请求。

请注意，如果请求到达此阶段，则表示该请求已发送到服务器，并且服务器已收到请求正文等数据。具有响应标头条件的屏蔽或重定向规则仍会运行，但实际上无法屏蔽或重定向请求。

对于屏蔽规则，发出请求的网页会收到屏蔽响应，并且 Chrome 会提前终止请求，从而处理这种情况。对于重定向规则，Chrome 会向重定向的网址发出新请求。请务必考虑这些行为是否符合您扩展程序的隐私权预期。

如果请求未被阻止或重定向，Chrome 会应用任何 modifyHeaders 规则。对响应标头应用修改的方式与“在发送请求标头之前”中所述的方式相同。由于请求已发出，因此对请求标头应用修改不会产生任何影响。

安全规则是指操作为 block、allow、allowAllRequests 或 upgradeScheme 的规则。这些规则受动态规则配额增加的限制。

在浏览器中加载和评估规则会产生性能开销，因此使用该 API 时会受到一些限制。限制取决于您使用的规则类型。

静态规则是指在清单文件中声明的规则文件中指定的规则。扩展程序最多可以在 "rule_resources" 清单键中指定 100 个静态规则集，但一次只能启用其中的 50 个规则集。后者称为 MAX_NUMBER_OF_ENABLED_STATIC_RULESETS。这些规则集总共至少包含 30,000 条规则。这称为 GUARANTEED_MINIMUM_STATIC_RULES。

之后可用的规则数量取决于用户浏览器上安装的所有扩展程序启用的规则数量。您可以在运行时通过调用 getAvailableStaticRuleCount() 找到此数字。您可以在代码示例下查看相关示例。

一个扩展程序最多可以有 5,000 条会话规则。这会作为 MAX_NUMBER_OF_SESSION_RULES 公开。

在 Chrome 120 之前，动态规则和会话规则的总数上限为 5, 000。

扩展程序可以至少有 5,000 条动态规则。这会作为 MAX_NUMBER_OF_UNSAFE_DYNAMIC_RULES 公开。

从 Chrome 121 开始，安全动态规则（以 MAX_NUMBER_OF_DYNAMIC_RULES 形式公开）的上限增加到 30,000 条。在 5000 条规则的限制范围内添加的任何不安全规则也会计入此限制。

在 Chrome 120 之前，动态规则和会话规则的总数上限为 5, 000。

所有类型的规则都可以使用正则表达式；不过，每种类型的正则表达式规则总数不得超过 1000 条。这称为 MAX_NUMBER_OF_REGEX_RULES。

此外，每条规则在编译后的大小必须小于 2KB。这与规则的复杂程度大致相关。如果您尝试加载超出此限制的规则，系统会显示如下警告，并忽略该规则。

declarativeNetRequest 仅适用于到达网络堆栈的请求。这包括来自 HTTP 缓存的响应，但不一定包括通过服务工作线程的 onfetch 处理程序的响应。declarativeNetRequest 不会影响由服务工作线程生成的响应或从 CacheStorage 检索的响应，但会影响在服务工作线程中对 fetch() 的调用。

declarativeNetRequest 规则无法将公开资源请求重定向到无法通过网络访问的资源。这样做会触发错误。即使指定的 Web 可访问资源归重定向扩展程序所有，也是如此。如需为 declarativeNetRequest 声明资源，请使用清单的 "web_accessible_resources" 数组。

仅支持对以下请求标头执行附加操作：accept、accept-encoding、accept-language、access-control-request-headers、cache-control、connection、content-language、cookie、forwarded、if-match、if-none-match、keep-alive、range、te、trailer、transfer-encoding、upgrade、user-agent、via、want-digest、x-forwarded-for。此许可名单区分大小写（bug 449152902）。

在附加到请求或响应标头时，浏览器会尽可能使用适当的分隔符。

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

返回给定 Ruleset 中当前已停用的静态规则列表。

GetDisabledRuleIdsOptions

返回扩展程序的当前动态规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

返回与扩展程序匹配的所有规则。调用方可以选择性地通过指定 filter 来过滤匹配规则的列表。此方法仅适用于具有 "declarativeNetRequestFeedback" 权限或已针对 filter 中指定的 tabId 授予 "activeTab" 权限的扩展程序。注意：如果规则未与有效文档相关联，且匹配时间超过 5 分钟，则不会返回该规则。

MatchedRulesFilter 可选

Promise<RulesMatchedDetails>

返回扩展程序的当前会话范围规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

检查给定的正则表达式是否会作为 regexFilter 规则条件受到支持。

Promise<IsRegexSupportedResult>

配置是否应将标签页的操作次数显示为扩展程序操作的徽章文本，并提供一种递增该操作次数的方法。

ExtensionActionOptions

检查扩展程序的任何 declarativeNetRequest 规则是否会与假设的请求匹配。注意：此方法仅适用于未打包的扩展程序，因为此方法仅用于扩展程序开发期间。

TestMatchRequestDetails

Promise<TestMatchOutcomeResult>

修改扩展程序的当前动态规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

更新扩展程序的已启用静态规则集。系统会先移除 options.disableRulesetIds 中列出的 ID 对应的规则集，然后再添加 options.enableRulesetIds 中列出的规则集。请注意，已启用的静态规则集会在会话之间保持不变，但不会在扩展程序更新之间保持不变，也就是说，rule_resources 清单键将决定每次扩展程序更新时已启用的静态规则集。

修改扩展程序的当前会话范围规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

停用和启用 Ruleset 中的各个静态规则。对已停用的 Ruleset 所属规则做出的更改将在该 Ruleset 下次启用时生效。

UpdateStaticRulesOptions

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
    "declarativeNetRequestFeedback"
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
rules_1.json: Rule with id 1 specified a more complex regex than allowed
as part of the "regexFilter" key.
```

---

## chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/inspectedWindow

**Contents:**
- chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 在检查的窗口中执行代码
- 示例
- 类型
  - Resource
    - 属性
- 属性
  - tabId

使用 chrome.devtools.inspectedWindow API 与检查的窗口进行交互：获取被检查页面的标签页 ID、在被检查的窗口中评估代码、重新加载页面或者获取页面中的资源列表。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

tabId 属性提供可与 chrome.tabs.* 一起使用的标签页标识符 API 调用。但请注意，chrome.tabs.* API 不会提供给开发者工具 扩展程序网页 - 您需要将标签页 ID 传递到后台 页面并从中调用 chrome.tabs.* API 函数。

reload 方法可用于重新加载被检查的网页。此外，调用方还可以指定 用户代理字符串的替换值、在网页加载时提前注入的脚本，或 用于强制重新加载缓存资源的选项。

使用 getResources 调用和 onResourceContent 事件获取资源列表 （文档、样式表、脚本、图片等）。getContent 和 Resource 类的 setContent 方法以及 onResourceContentCommitted 事件可以 可用于支持资源内容的修改，例如由外部编辑者修改。

必须在清单中声明以下键才能使用此 API。

eval 方法可让扩展程序在 所检查的网页。此方法在合适的上下文中使用时功能强大，使用时则有危险 不当。请使用 tabs.executeScript 方法，除非您需要特定功能 由 eval 方法提供的函数定义。

eval 和 tabs.executeScript 方法之间的主要区别如下：

请注意，一个页面可以包含多个不同的 JavaScript 执行上下文。每个帧都有 以及运行内容脚本的每个扩展程序的其他上下文， 帧。

默认情况下，eval 方法在所检查页面的主框架上下文中执行。

eval 方法带有一个可选的第二个参数，您可以使用此参数来指定 代码评估时间。此 options 对象可以包含以下一个或多个键：

以下代码可检查被检查的网页所使用的 jQuery 版本：

若要试用此 API，请安装 chrome-extension-samples 中的 chrome-extension-samples 存储库

所检查页面中的资源，例如文档、脚本或图片。

如果内容未编码，则为空，否则对名称进行编码。目前只支持 base64。

如果用户已完成资源修改，并且资源的新内容应保留，则为 true；如果是在用户修改资源过程中发送的微小更改，则为 false。

如果资源内容设置成功，则设为“undefined”；否则会描述错误。

要检查的标签页的 ID。此 ID 可能会与 chrome.tabs 配合使用。*Compute Engine API 来创建虚拟机实例。

在被检查页面的主框架上下文中评估 JavaScript 表达式。表达式的计算结果必须是与 JSON 兼容的对象，否则会抛出异常。评估函数可以报告开发者工具端错误或评估期间发生的 JavaScript 异常。无论是哪种情况，回调的 result 参数都是 undefined。如果开发者工具端出现错误，isException 参数为非 null 值，并且 isError 设为 true，code 设为错误代码。如果发生 JavaScript 错误，系统会将 isException 设置为 true，并将 value 设置为抛出的对象的字符串值。

options 参数可以包含一个或多个选项。

如果指定，则系统会在网址与指定网址匹配的 iframe 上计算表达式。默认情况下，表达式将在所检查页面的顶部帧进行求值。

在与指定来源匹配的扩展程序的内容脚本上下文中评估表达式。如果指定，scriptExecutionContext 会覆盖“true”对 useContentScriptContext 进行设置。

在调用扩展程序的内容脚本的上下文中评估表达式，前提是内容脚本已注入检查的网页。否则，系统不会对表达式求值，并且会在调用回调函数时将异常参数设置为 isError 字段设置为 true 且 code 字段设置为 E_NOTFOUND 的对象。

在计算表达式时出现异常时提供详细信息的对象。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果在对表达式求值之前开发者工具端发生错误，则设置此字段。包含可以替换到说明字符串中的值数组，以提供有关错误原因的更多信息。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果为 true，加载器将对所有在 load 事件触发之前加载的已检查页面资源绕过缓存。具体效果类似于在所检查的窗口或开发者工具窗口中按 Ctrl+Shift+R 的效果。

如果已指定，该脚本将在加载时立即注入到所检查网页的每一帧中，先于该帧的任何脚本。此脚本在后续重新加载后将不再注入（例如，如果用户按 Ctrl+R）。

如果已指定，该字符串将替换在加载所检查网页的资源时发送的 User-Agent HTTP 标头的值。该字符串还将覆盖 navigator.userAgent 属性的值，该值会返回到在检查页面中运行的任何脚本。

在提交资源的新修订版本时触发（例如，用户在开发者工具中保存了某个已修改的资源版本）。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.inspectedWindow.eval(
  "jQuery.fn.jquery",
  function(result, isException) {
    if (isException) {
      console.log("the page is not using jQuery");
    } else {
      console.log("The page is using jQuery v" + result);
    }
  }
);
```

Example 2 (javascript):
```javascript
(callback: function) => {...}
```

Example 3 (javascript):
```javascript
(content: string, encoding: string) => void
```

Example 4 (javascript):
```javascript
(content: string, commit: boolean, callback?: function) => {...}
```

---

## chrome.ttsEngine 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/ttsEngine?hl=zh-cn

**Contents:**
- chrome.ttsEngine 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 处理语音事件
- 类型
  - AudioBuffer
    - 属性
  - AudioStreamOptions
    - 属性

使用 chrome.ttsEngine API 通过扩展程序实现文本转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序将会收到包含要朗读的语音和其他参数的事件。然后，您的扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

扩展程序可以将自己注册为语音引擎。这样，它就可以拦截对 tts.speak() 和 tts.stop() 等函数的部分或全部调用，并提供替代实现。扩展程序可以自由使用任何可用的 Web 技术来提供语音，包括从服务器流式传输音频、HTML5 音频。扩展程序甚至可以对这些语音内容执行其他操作，例如在弹出式窗口中显示字幕，或将其作为日志消息发送到远程服务器。

如需实现 TTS 引擎，扩展程序必须声明“ttsEngine”权限，然后在扩展程序清单中声明它提供的所有语音，如下所示：

voice_name 为必需参数，名称应具有足够的描述性，能够指明语音的名称和所使用的引擎。在极少数情况下，如果两个扩展程序注册了同名的语音，客户端可以指定应执行合成的扩展程序的 ID。

lang 参数是可选的，但强烈建议您使用。几乎在所有情况下，一个语音只能合成一种语言的语音。当引擎支持多种语言时，它可以轻松为每种语言注册单独的声音。在极少数情况下，单个语音可以处理多种语言，最简单的方法就是列出两个单独的语音，并在内部使用相同的逻辑进行处理。不过，如果您想创建一个可处理任何语言的语音，请从扩展程序的清单中省略 lang 参数。

最后，如果引擎可以发送事件来更新客户端的语音合成进度，则必须使用 event_types 参数。强烈建议至少支持 'end' 事件类型，以指示语音何时结束，否则 Chrome 将无法调度已排队的语音指令。

加载后，扩展程序可以通过调用 chrome.ttsEngine.updateVoices 替换声明的语音列表。（请注意，对 updateVoices 进行程序化调用时使用的参数采用驼峰式命名法：例如voiceName，而清单文件使用 voice_name。）

您可以发送的可能事件类型与 speak() 方法收到的事件类型相对应：

'interrupted' 和 'cancelled' 事件并非由语音引擎发送；而是由 Chrome 自动生成的。

假设您已按照下文所述注册语音事件监听器，文本转语音客户端可以通过调用 tts.getVoices 从扩展程序的清单中获取语音信息。

如需根据客户端请求生成语音，您的扩展程序必须为 onSpeak 和 onStop 注册监听器，如下所示：

是否向扩展程序发送给定语音请求的决定完全取决于扩展程序是否支持其清单中的给定语音参数，以及是否已为 onSpeak 和 onStop 注册监听器。换句话说，扩展程序无法接收语音请求并动态决定是否处理该请求。

文字转语音引擎中的音频缓冲区。其长度应与 audioStreamOptions.bufferSize 完全相同，并以音频流选项的采样率编码为单声道，以及线性 PCM、32 位有符号浮点，即 JavaScript 中的 Float32Array 类型。

如果此音频缓冲区是正在朗读的文本的最后一个缓冲区，则为 true。

有关安装失败的详细信息。如果语言安装失败，则可选择填充。

LanguageInstallStatus

语言字符串，采用语言代码-地区代码的形式，其中地区代码可以省略。例如 en、en-AU、zh-CH。

如果 TTS 客户端希望立即卸载语言，则为 True。引擎可能会根据此参数和请求方信息选择是否以及何时卸载语言。如果为 false，则系统可能会使用其他条件（例如近期使用情况）来确定何时卸载。

向 tts.speak() 方法指定的选项。

要用于合成的语言，格式为语言-地区。示例：“en”“en-US”“en-GB”“zh-CN”。

语音音调介于 0 到 2 之间（包括这两个数值），其中 0 表示最低，2 表示最高。1.0 对应于此语音的默认音调。

与此语音的默认语速相比的语速。1.0 是默认速率，通常为每分钟 180 到 220 个字左右。2.0 表示快一倍的速度，0.5 则表示原有速度的一半。此值保证介于 0.1 到 10.0 之间（包括这两个数值）。如果某个语音不支持此完整速率范围，请勿返回错误。而是将速率剪裁到语音支持的范围。

讲话音量，介于 0 到 1 之间（包括这两个数值），其中 0 表示最低音量，1 表示最高音量，默认值为 1.0。

发出语言管理请求的客户端。对于扩展程序，这是唯一的扩展程序 ID。对于 Chrome 功能，此字段是该功能的直观易懂的名称。

在尝试安装语言和卸载语言时由引擎调用。也用于响应来自客户的状态请求。安装或卸载语音时，引擎还应调用 ttsEngine.updateVoices 以注册语音。

由引擎调用以更新其语音列表。此列表会替换此扩展程序清单中声明的所有语音。

表示可用于语音合成的可用语音的 tts.TtsVoice 对象数组。

当 TTS 客户端请求安装新语言时触发。引擎应尝试下载并安装语言，并使用结果调用 ttsEngine.updateLanguage。成功后，引擎还应调用 ttsEngine.updateVoices 以注册新推出的语音。

当 TTS 客户端请求语言的安装状态时触发。

可选：如果引擎支持暂停事件，则应暂停正在说出的当前语音（如果有），直到收到恢复事件或停止事件。请注意，停止事件也应清除暂停状态。

可选：如果引擎支持暂停事件，则也应支持恢复事件，以继续说出当前的语音（如果有）。请注意，停止事件也应清除暂停状态。

当用户调用 tts.speak() 且此扩展程序清单中的某个语音最先与 options 对象匹配时调用。

来自文本转语音引擎的事件，用于指示此语音的状态。

当用户调用 tts.speak() 且此扩展程序清单中的某个语音最先与 options 对象匹配时调用。与 ttsEngine.onSpeak 不同，Chrome 提供音频播放服务并处理调度 TTS 事件。

当对 tts.stop 进行调用且此扩展程序可能正在说话时触发。如果扩展程序收到对 onStop 的调用，并且语音已停止，则应不执行任何操作（不引发错误）。如果语音处于暂停状态，此操作应取消暂停状态。

当 TTS 客户端指示不再需要某种语言时触发。

LanguageUninstallOptions

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My TTS Engine",
  "version": "1.0",
  "permissions": ["ttsEngine"],
  "tts_engine": {
    "voices": [
      {
        "voice_name": "Alice",
        "lang": "en-US",
        "event_types": ["start", "marker", "end"]
      },
      {
        "voice_name": "Pat",
        "lang": "en-US",
        "event_types": ["end"]
      }
    ]
  },
  "background": {
    "page": "background.html",
    "persistent": false
  }
}
```

Example 2 (javascript):
```javascript
const speakListener = (utterance, options, sendTtsEvent) => {
  sendTtsEvent({type: 'start', charIndex: 0})

  // (start speaking)

  sendTtsEvent({type: 'end', charIndex: utterance.length})
};

const stopListener = () => {
  // (stop all speech)
};

chrome.ttsEngine.onSpeak.addListener(speakListener);
chrome.ttsEngine.onStop.addListener(stopListener);
```

Example 3 (unknown):
```unknown
chrome.ttsEngine.updateLanguage(  status: LanguageStatus,): void
```

Example 4 (unknown):
```unknown
chrome.ttsEngine.updateVoices(  voices: TtsVoice[],): void
```

---

## chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/cookies?hl=zh-cn

**Contents:**
- chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 分区
- 示例
- 类型
  - Cookie
    - 属性
  - CookieDetails
    - 属性

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

如需使用 Cookie API，请在清单中声明 "cookies" 权限，并为要访问其 Cookie 的任何主机声明主机权限。例如：

借助分区 Cookie，网站可以标记某些 Cookie 应以顶级框架的来源为键。这意味着，举例来说，如果网站 A 通过 iframe 嵌入到网站 B 和网站 C 中，则来自 A 的分区 Cookie 的嵌入版本在 B 和 C 上可以具有不同的值。

默认情况下，所有 API 方法都针对未分区的 Cookie 运行。您可以使用 partitionKey 属性替换此行为。

如需详细了解分区对扩展程序的一般影响，请参阅存储空间和 Cookie。

您可以在 examples/api/cookies 目录中找到使用 Cookie API 的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

表示 HTTP Cookie 的相关信息。

Cookie 的网域（例如“www.google.com”“example.com”）。

Cookie 的过期日期，以自 UNIX 纪元以来的秒数表示。不适用于会话 Cookie。

如果 Cookie 是仅限主机使用的 Cookie（即请求的主机必须与 Cookie 的网域完全一致），则为 True。

如果 Cookie 被标记为 HttpOnly（即客户端脚本无法访问该 Cookie），则为 True。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

Cookie 的同站点状态（即是否随跨站请求发送 Cookie）。

如果 Cookie 被标记为“Secure”（即其范围仅限于安全渠道，通常为 HTTPS），则为 True。

如果 Cookie 是会话 Cookie（而非具有过期日期的持久性 Cookie），则为 True。

包含相应 Cookie 的 Cookie 存储区的 ID，如 getAllCookieStores() 中所提供。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

要查找 Cookie 的 Cookie 存储区的 ID。默认情况下，系统会使用当前执行上下文的 Cookie 存储区。

与要访问的 Cookie 关联的网址。此实参可以是完整网址，在这种情况下，网址路径后面的任何数据（例如查询字符串）都会被忽略。如果未在清单文件中指定相应网址的主机权限，API 调用将会失败。

指示 Cookie 是否是在跨网站情境中设置的。这样可以防止在跨网站情境中嵌入的顶级网站访问在同网站情境中由该顶级网站设置的 Cookie。

表示浏览器中的 Cookie 存储区。例如，无痕模式窗口使用的 Cookie 存储区与非无痕窗口使用的 Cookie 存储区不同。

共享此 Cookie 存储区的所有浏览器标签页的标识符。

相应文档的唯一标识符。如果提供了 frameId 和/或 tabId，系统会验证它们是否与通过提供的文档 ID 找到的文档相匹配。

Cookie 更改的根本原因。如果通过显式调用“chrome.cookies.remove”插入或移除了 Cookie，“cause”将为“explicit”。如果 Cookie 因过期而被自动移除，“原因”将为“已过期”。如果某个 Cookie 因被已过期的过期日期覆盖而遭到移除，“原因”将设置为“expired_overwrite”。如果 Cookie 因垃圾回收而自动移除，“原因”将为“逐出”。如果因“set”调用覆盖了某个 Cookie 而导致该 Cookie 被自动移除，“原因”将为“覆盖”。请相应地规划您的回答。

Cookie 的“SameSite”状态 (https://tools.ietf.org/html/draft-west-first-party-cookies)。“no_restriction”对应于使用“SameSite=None”设置的 Cookie，“lax”对应于“SameSite=Lax”，“strict”对应于“SameSite=Strict”。“未指定”对应于未设置 SameSite 属性的 Cookie。

检索单个 Cookie 的相关信息。如果指定网址存在多个同名 Cookie，则返回路径最长的那个。对于路径长度相同的 Cookie，系统会返回创建时间最早的 Cookie。

Promise<Cookie | undefined>

从单个 Cookie 存储区检索与给定信息匹配的所有 Cookie。返回的 Cookie 将按路径长度进行排序，路径最长的 Cookie 排在最前面。如果多个 Cookie 的路径长度相同，则创建时间最早的 Cookie 会排在前面。此方法仅检索扩展程序具有主机权限的网域的 Cookie。

将检索到的 Cookie 限制为网域与此网域匹配或为此网域的子网域的 Cookie。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

将检索到的 Cookie 限制为路径与此字符串完全匹配的 Cookie。

按 Secure 属性过滤 Cookie。

过滤掉会话 Cookie 与永久性 Cookie。

要从中检索 Cookie 的 Cookie 存储区。如果省略，则使用当前执行上下文的 Cookie 存储区。

将检索到的 Cookie 限制为与指定网址匹配的 Cookie。

Promise<CookieStore[]>

Promise<object | undefined>

使用给定的 Cookie 数据设置 Cookie；如果存在等效的 Cookie，可能会覆盖这些 Cookie。

有关正在设置的 Cookie 的详细信息。

相应 Cookie 的网域。如果省略，相应 Cookie 将成为仅限主机使用的 Cookie。

Cookie 的过期日期，以自 UNIX 纪元以来的秒数表示。如果省略，相应 Cookie 将成为会话 Cookie。

Cookie 是否应标记为 HttpOnly。默认值为 false。

相应 Cookie 的名称。如果省略，则默认为空。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

Cookie 的路径。默认为网址参数的路径部分。

Cookie 的同网站状态。默认为“unspecified”，即如果省略，则设置 Cookie 时不指定 SameSite 属性。

是否应将 Cookie 标记为“Secure”。默认值为 false。

要在其中设置 Cookie 的 Cookie 存储区的 ID。默认情况下，Cookie 会设置在当前执行上下文的 Cookie 存储区中。

要与 Cookie 设置相关联的 request-URI。此值可能会影响所创建 Cookie 的默认网域和路径值。如果未在清单文件中指定相应网址的主机权限，API 调用将会失败。

相应 Cookie 的值。如果省略，则默认为空。

Promise<Cookie | undefined>

在设置或移除 Cookie 时触发。作为一种特殊情况，请注意，更新 Cookie 的属性是通过两步流程实现的：首先完全移除要更新的 Cookie，生成“原因”为“覆盖”的通知。之后，系统会写入包含更新值的新 Cookie，并生成第二个通知，其中“原因”为“显式”。

有关已设置或已移除的 Cookie 的信息。

如果已移除 Cookie，则为 True。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "*://*.google.com/"
  ],
  "permissions": [
    "cookies"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.cookies.get(  details: CookieDetails,): Promise<Cookie | undefined>
```

Example 3 (unknown):
```unknown
chrome.cookies.getAll(  details: object,): Promise<Cookie[]>
```

Example 4 (unknown):
```unknown
chrome.cookies.getAllCookieStores(): Promise<CookieStore[]>
```

---

## chrome.sidePanel 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/sidePanel?hl=zh-cn

**Contents:**
- chrome.sidePanel 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和使用
  - 使用场景
    - 在每个网站上显示相同的侧边栏
    - 在特定网站上启用侧边栏
    - 点击工具栏图标，打开侧边栏
    - 以程序化方式在用户互动时打开侧边栏

使用 chrome.sidePanel API 在浏览器的侧边栏中托管内容，与网页的主要内容并排显示。

如需使用 Side Panel API，请在扩展程序清单文件中添加 "sidePanel" 权限：

借助侧边栏 API，扩展程序可以在侧边栏中显示自己的界面，从而提供持久的体验，以补充用户的浏览历程。

以下部分展示了 Side Panel API 的一些常见用例。如需查看完整的扩展程序示例，请参阅扩展程序示例。

侧边栏最初可以从清单的 "side_panel" 键中的 "default_path" 属性进行设置，以便在每个网站上显示相同的侧边栏。此路径应指向扩展程序目录中的相对路径。

扩展程序可以使用 sidepanel.setOptions() 在特定标签页上启用侧边栏。此示例使用 chrome.tabs.onUpdated() 监听对标签页所做的任何更新。它会检查网址是否为 www.google.com，并启用侧边栏。否则，系统会停用该功能。

当用户暂时切换到未启用侧边栏的标签页时，侧边栏会隐藏。当用户切换到之前打开过该标签页的标签页时，该标签页会自动重新显示。

当用户前往未启用侧边栏的网站时，侧边栏会关闭，并且扩展程序不会显示在侧边栏下拉菜单中。

如需查看完整示例，请参阅特定于标签页的侧边栏示例。

开发者可以使用 sidePanel.setPanelBehavior() 让用户在点击操作工具栏图标时打开侧边栏。首先，在清单中声明 "action" 键：

Chrome 116 引入了 sidePanel.open()。它允许扩展程序通过扩展程序用户手势（例如点击操作图标）打开侧边栏。或者用户在扩展程序页面或内容脚本上的互动，例如点击按钮。如需查看完整演示，请参阅打开侧边栏示例扩展程序。

以下代码展示了如何在用户点击上下文菜单时在当前窗口中打开全局侧边栏。使用 sidePanel.open() 时，您必须选择应在哪个上下文中打开它。使用 windowId 打开全局侧边栏。或者，您也可以将 tabId 设置为仅在特定标签页中打开侧边栏。

扩展程序可以使用 sidepanel.getOptions() 检索当前的侧边栏。以下示例在 runtime.onInstalled() 上设置了欢迎侧边栏。然后，当用户导航到其他标签页时，该标签页会被替换为主侧边栏。

用户将首先看到 Chrome 的内置侧边栏。每个侧边栏都会在侧边栏菜单中显示扩展程序的图标。如果未添加任何图标，系统会显示一个占位符图标，其中包含扩展程序名称的首字母。

如需允许用户打开侧边栏，请将操作图标与 sidePanel.setPanelBehavior() 结合使用。或者，在用户互动后调用 sidePanel.open()，例如：

当侧边栏处于打开状态时，侧边栏工具栏会显示一个图钉图标。 点击该图标可固定扩展程序的操作图标。点击固定后的操作图标将执行操作图标的默认操作，并且只有在明确配置的情况下才会打开侧边栏。

如需查看更多侧边栏 API 扩展演示，请探索以下任一扩展：

要关闭侧边栏的标签页。如果指定标签页中打开了标签页专用的侧边栏，系统会关闭该侧边栏。必须提供此参数或 windowId 中的至少一个。

用于关闭侧边栏的窗口。如果指定窗口中打开了全局侧边栏，则对于该窗口中未激活任何标签页专用面板的所有标签页，系统都会关闭该全局侧边栏。必须提供此参数或 tabId 中的至少一个。

如果指定，则返回指定标签页的侧边栏选项。否则，返回默认的侧边栏选项（用于没有任何特定设置的任何标签页）。

用于打开侧边栏的标签页。如果相应标签页具有特定于该标签页的侧边栏，则该侧边栏仅会针对该标签页打开。如果没有特定于标签页的面板，则全局面板将在指定标签页以及当前未打开任何特定于标签页的面板的其他标签页中打开。此操作会替换相应标签页中当前处于活动状态的任何侧边栏（全局或标签页专用）。必须提供此参数或 windowId 中的至少一个。

用于打开侧边栏的窗口。仅当扩展程序具有全局（非标签页专用）侧边栏或还指定了 tabId 时，此属性才适用。此方法将替换用户在指定窗口中打开的任何当前有效的全局侧边栏。必须提供此参数或 tabId 中的至少一个。

点击扩展程序的图标是否会切换侧边栏中扩展程序条目的显示状态。默认值为 false。

扩展程序软件包中要在面板中显示内容的本地资源的路径。

侧边栏关闭时所在的标签页的可选 ID。仅当面板是特定于标签页时提供。

侧边栏关闭时所在的窗口的 ID。此功能适用于全局面板和标签页专用面板。

扩展程序软件包中要在面板中显示内容的本地资源的路径。

打开侧边栏的标签页的可选 ID。仅当面板是特定于标签页时提供。

打开侧边栏的窗口的 ID。此功能适用于全局面板和标签页专用面板。

侧边栏是否应处于启用状态。您可以选择是否创建 PIN 码。默认值为 true。

要使用的侧边栏 HTML 文件的路径。这必须是扩展程序包中的本地资源。

如果指定，侧边栏选项将仅适用于具有此 ID 的标签页。如果省略，这些选项会设置默认行为（用于没有任何特定设置的任何标签页）。注意：如果为相应 tabId 和默认 tabId 设置了相同的路径，则相应 tabId 的面板将是与默认 tabId 的面板不同的实例。

Promise<PanelOptions>

Promise<PanelBehavior>

打开扩展程序的侧边栏。此方法只能在响应用户操作时调用。

配置扩展程序的侧边栏行为。这是一项更新插入操作。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My side panel extension",
  ...
  "permissions": [
    "sidePanel"
  ]
}
```

Example 2 (unknown):
```unknown
{
  "name": "My side panel extension",
  ...
  "side_panel": {
    "default_path": "sidepanel.html"
  }
  ...
}
```

Example 3 (unknown):
```unknown
<!DOCTYPE html>
<html>
  <head>
    <title>My Sidepanel</title>
  </head>
  <body>
    <h1>All sites sidepanel extension</h1>
    <p>This side panel is enabled on all sites</p>
  </body>
</html>
```

Example 4 (javascript):
```javascript
const GOOGLE_ORIGIN = 'https://www.google.com';

chrome.tabs.onUpdated.addListener(async (tabId, info, tab) => {
  if (!tab.url) return;
  const url = new URL(tab.url);
  // Enables the side panel on google.com
  if (url.origin === GOOGLE_ORIGIN) {
    await chrome.sidePanel.setOptions({
      tabId,
      path: 'sidepanel.html',
      enabled: true
    });
  } else {
    // Disables the side panel on all other sites
    await chrome.sidePanel.setOptions({
      tabId,
      enabled: false
    });
  }
});
```

---

## chrome.desktopCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/desktopCapture?hl=zh-cn

**Contents:**
- chrome.desktopCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - DesktopCaptureSourceType
    - 枚举
  - SelfCapturePreferenceEnum
    - 枚举
  - SystemAudioPreferenceEnum
    - 枚举

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

用于定义 chooseDesktopMedia() 中所用的一组桌面媒体源的枚举。

镜像 SelfCapturePreferenceEnum。

镜像 SystemAudioPreferenceEnum。

镜像 WindowAudioPreferenceEnum。

隐藏由 chooseDesktopMedia() 显示的桌面媒体选择器对话框。

chooseDesktopMedia() 返回的 ID

DesktopCaptureSourceType[]

应向用户显示的一组来源。集合中的来源顺序决定了选择器中的标签页顺序。

创建数据流所针对的可选标签页。如果未指定，则只有调用扩展程序可以使用生成的流。该数据流只能由给定标签页中安全来源与 tab.url 相匹配的帧使用。标签页的来源必须是安全来源，例如 HTTPS。

一个不透明的字符串，可传递给 getUserMedia() API 以生成与用户选择的来源对应的媒体流。如果用户未选择任何来源（即取消了提示），则系统会使用空的 streamId 调用回调。创建的 streamId 只能使用一次，如果未使用，会在几秒后过期。

如果“audio”包含在参数来源中，并且最终用户未取消选中“分享音频”复选框，则为 true。否则为 false，在这种情况下，不应通过 getUserMedia 调用请求音频流。

一个 ID，如果需要取消提示，可以将其传递给 cancelChooseDesktopMedia()。

**Examples:**

Example 1 (unknown):
```unknown
chrome.desktopCapture.cancelChooseDesktopMedia(  desktopMediaRequestId: number,): void
```

Example 2 (unknown):
```unknown
chrome.desktopCapture.chooseDesktopMedia(  sources: DesktopCaptureSourceType[],  targetTab?: Tab,  callback: function,): number
```

Example 3 (javascript):
```javascript
(streamId: string, options: object) => void
```

---

## chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/extensionTypes/?hl=zh-cn

**Contents:**
- chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 类型
  - ColorArray
    - 类型
  - CSSOrigin
    - 枚举
  - DeleteInjectionDetails
    - 属性
  - DocumentLifecycle

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

[number, number, number, number]

要移除的 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示应从当前页面的所有框架中移除 CSS。默认值为 false，并且仅从顶部框架中移除。如果设置了 true 和 frameId，则从所选帧及其所有子帧中移除代码。

要移除的 CSS 的来源。默认设置为 "author"。

应从中移除 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问其父文档时，该代码也会从 about:blank 和 about:srcdoc 框架中移除。默认值为 false。

脚本要在其中执行的 JavaScript 世界。可以是此扩展程序独有的隔离世界、与网页的 JavaScript 共享的 DOM 主世界，也可以是仅适用于通过 User Scripts API 注册的脚本的用户脚本世界。

图片的像素数据。必须是 ImageData 对象；例如，来自 canvas 元素。

当格式为 "jpeg" 时，控制生成图片的质量。对于 PNG 图片，系统会忽略此值。随着质量的降低，生成的图片会出现更多视觉伪影，并且存储所需的字节数也会减少。

要注入的脚本或 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示 JavaScript 或 CSS 应注入到当前页面的所有框架中。默认值为 false，并且仅注入到顶部框架中。如果设置了 true 和 frameId，则代码会插入到所选帧及其所有子帧中。

要注入的 JavaScript 或 CSS 代码。

警告：请谨慎使用 code 参数。如果使用不当，可能会导致您的扩展程序遭受跨站脚本攻击

要注入的 CSS 的来源。此值只能为 CSS 指定，不能为 JavaScript 指定。默认设置为 "author"。

要注入的 JavaScript 或 CSS 文件。

应注入脚本或 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问 about:blank 和 about:srcdoc 框架的父文档时，代码也会注入到这些框架中。代码无法插入到顶级 about:-frames 中。默认值为 false。

JavaScript 或 CSS 将注入到标签页中的最早时间。默认值为“document_idle”。

JavaScript 或 CSS 将注入到标签页中的最早时间。

“document_start” 脚本在任何 CSS 文件之后注入，但在构建任何其他 DOM 或运行任何其他脚本之前注入。

“document_end” 在 DOM 完成后立即注入脚本，但在图片和框架等子资源加载之前注入。

“document_idle” 浏览器会选择一个时间在“document_end”和 window.onload 事件触发后立即注入脚本。注入的确切时间取决于文档的复杂程度和加载所需的时间，并针对网页加载速度进行了优化。以“document_idle”运行的内容脚本无需监听 window.onload 事件；它们保证在 DOM 完成后运行。如果脚本确实需要在 window.onload 之后运行，扩展程序可以使用 document.readyState 属性检查 onload 是否已触发。

---

## chrome.vpnProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/vpnProvider

**Contents:**
- chrome.vpnProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Parameters
    - 属性
  - PlatformMessage
    - 枚举

使用 chrome.vpnProvider API 实现 VPN 客户端。

chrome.vpnProvider 的典型用法如下：

通过调用 createConfig() 创建 VPN 配置。VPN 配置是指在 ChromeOS 界面中向用户显示的持久性条目。用户可以从列表中选择 VPN 配置，并连接或断开连接。

为 onPlatformMessage、onPacketReceived 和 onConfigRemoved 事件添加监听器。

当用户连接到 VPN 配置时，系统会收到 onPlatformMessage，并显示消息 "connected"。"connected" 消息和 "disconnected" 消息之间的时段称为“VPN 会话”。在此时间段内，接收消息的扩展程序被视为拥有 VPN 会话。

启动与 VPN 服务器的连接并启动 VPN 客户端。

通过调用 setParameters() 设置连接的参数。

通过调用 notifyConnectionStateChanged() 将连接状态通知为 "connected"。

如果上述步骤顺利完成，系统会为 ChromeOS 的网络堆栈创建一个虚拟隧道。通过调用 sendPacket()，IP 数据包可以通过隧道发送；ChromeOS 设备上发出的任何数据包都将通过 onPacketReceived 事件处理程序接收。

当用户断开与 VPN 配置的连接时，系统会触发 onPlatformMessage 并显示消息 "disconnected"。

如果不再需要 VPN 配置，可以通过调用 destroyConfig() 将其销毁。

VPN 接口的 IP 地址（采用 CIDR 表示法）。目前，唯一支持的模式是 IPv4。

VPN 接口的广播地址。（默认值：根据 IP 地址和掩码推断得出）

从隧道中排除以 CIDR 表示法表示的 IP 块列表的网络流量。这可用于绕过 VPN 服务器的传入和传出流量。如果多条规则与某个目的地匹配，则匹配前缀最长的规则胜出。对应于同一 CIDR 块的条目会被视为重复条目。系统会消除汇总列表（exclusionList + inclusionList）中的此类重复项，但具体消除哪个完全相同的重复条目是不确定的。

将网络流量（采用 CIDR 表示法）添加到隧道 IP 块列表中。此参数可用于设置拆分隧道。默认情况下，没有流量会定向到隧道。将条目“0.0.0.0/0”添加到此列表后，所有用户流量都会重定向到隧道。如果多条规则与某个目的地匹配，则匹配前缀最长的规则胜出。对应于同一 CIDR 块的条目会被视为重复条目。系统会消除汇总列表（exclusionList + inclusionList）中的此类重复项，但具体消除哪个完全相同的重复条目是不确定的。

VPN 接口的 MTU 设置。（默认值：1500 字节）

如果为 true，则 linkDown、linkUp、linkChanged、suspend 和 resume 平台消息将用于发出相应事件的信号。如果为 false，当网络拓扑发生变化时，系统会强制断开 VPN 连接，用户需要手动重新连接。（默认值：false）

此属性是 Chrome 51 中的新属性；在更早的版本中，它会生成异常。try/catch 可用于根据浏览器支持情况有条件地启用该功能。

平台使用此枚举来通知客户端 VPN 会话状态。

“已断开连接” 表示 VPN 配置已断开连接。

“error” 表示 VPN 连接中发生了错误，例如超时。错误说明作为 onPlatformMessage 的 error 实参提供。

“linkDown” 表示默认物理网络连接已断开。

“linkUp” 表示默认的物理网络连接已恢复。

“linkChanged” 表示默认的物理网络连接已更改，例如从 WLAN 更改为移动网络。

“暂停” 表示操作系统正在准备暂停，因此 VPN 应断开连接。无法保证扩展程序在暂停之前收到此事件。

“resume” 表示操作系统已恢复，用户已重新登录，因此 VPN 应尝试重新连接。

平台使用此枚举来指明触发 onUIEvent 的事件。

“showAddDialog” 请求 VPN 客户端向用户显示添加配置对话框。

“showConfigureDialog” 请求 VPN 客户端向用户显示配置设置对话框。

VPN 客户端使用此枚举向平台告知其当前状态。这有助于向用户提供有意义的消息。

创建新的 VPN 配置，该配置在用户的多个登录会话中保持不变。

向平台通知 VPN 会话状态。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

通过为 VPN 会话创建的隧道发送 IP 数据包。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

设置 VPN 会话的参数。应在从平台收到 "connected" 后立即调用此方法。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

当通过隧道接收到扩展程序所拥有的 VPN 会话的 IP 数据包时触发。

当从平台收到扩展程序所拥有的 VPN 配置的消息时触发。

当扩展程序发生界面事件时触发。界面事件是来自平台的信号，用于向应用表明需要向用户显示界面对话框。

**Examples:**

Example 1 (unknown):
```unknown
chrome.vpnProvider.createConfig(  name: string,): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.vpnProvider.destroyConfig(  id: string,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.vpnProvider.notifyConnectionStateChanged(  state: VpnConnectionState,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.vpnProvider.sendPacket(  data: ArrayBuffer,): Promise<void>
```

---

## chrome.gcm 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/gcm?hl=zh-cn

**Contents:**
- chrome.gcm 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 属性
  - MAX_MESSAGE_SIZE
    - 值
- 方法
  - register()
    - 参数
    - 返回

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

消息中所有键值对的大小上限（以字节为单位）。

向 FCM 注册应用。注册 ID 将由 callback 返回。如果使用相同的 senderIds 列表再次调用 register，则会返回相同的注册 ID。

允许向应用发送消息的服务器 ID 的列表。应包含至少一个且不超过 100 个发件人 ID。

要发送到服务器的消息数据。不区分大小写的 goog. 和 google 以及区分大小写的 collapse_key 不允许用作键前缀。所有键/值对的总和不应超过 gcm.MAX_MESSAGE_SIZE。

要向其发送消息的服务器的 ID，由 Google API 控制台分配。

消息的 ID。在应用范围内，每个消息都必须具有唯一的 ID。如需有关选择和处理 ID 的建议，请参阅 Cloud Messaging 文档。

消息的存留时间（以秒为单位）。如果无法在该时间段内发送消息，系统将引发 onSendError 事件。生命周期为 0 表示消息应立即发送，如果无法发送，则应失败。生命周期的默认值为 86,400 秒（1 天），最大值为 2,419,200 秒（28 天）。

消息的折叠键。如需了解详情，请参阅不可折叠消息和可折叠消息。

当 FCM 服务器必须删除应用服务器发送给应用的消息时触发。如需详细了解如何处理此事件，请参阅消息的生命周期。

出现此错误的消息的 ID（如果错误与特定消息相关）。

**Examples:**

Example 1 (unknown):
```unknown
chrome.gcm.register(  senderIds: string[],): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.gcm.send(  message: object,): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.gcm.unregister(): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.gcm.onMessage.addListener(  callback: function,)
```

---

## chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/browsingData?hl=zh-cn

**Contents:**
- chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 特定来源
  - 来源类型
- 示例
- 类型
  - DataTypeSet
    - 属性

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

您必须在扩展程序清单中声明 "browsingData" 权限，才能使用此 API。

此 API 最简单的使用场景是用于清除用户浏览数据的基于时间的机制。您的代码应提供一个时间戳，用于指明历史日期，在此日期之后的用户浏览数据应被移除。此时间戳的格式为自 Unix 纪元以来的毫秒数（可以使用 getTime() 方法从 JavaScript Date 对象中检索）。

例如，如需清除用户过去一周的所有浏览数据，您可以编写如下代码：

借助 chrome.browsingData.remove() 方法，您只需一次调用即可移除各种类型的浏览数据，这比调用多个更具体的方法要快得多。不过，如果您只想清除一种特定的浏览数据（例如 Cookie），那么更精细的方法可提供一种可读的替代方案，而无需使用包含 JSON 的调用。

如果用户正在同步数据，chrome.browsingData.remove() 可能会在清除同步账号的 Cookie 后自动重建该 Cookie。这是为了确保同步功能可以继续正常运行，以便最终在服务器上删除数据。不过，更具体的 chrome.browsingData.removeCookies() 可用于清除同步账号的 Cookie，在这种情况下，同步会暂停。

如需移除特定来源的数据或排除一组来源而不进行删除，您可以使用 RemovalOptions.origins 和 RemovalOptions.excludeOrigins 参数。它们只能应用于 Cookie、缓存和存储空间（CacheStorage、FileSystems、IndexedDB、LocalStorage、ServiceWorkers 和 WebSQL）。

通过向 API 的 options 对象添加 originTypes 属性，您可以指定应影响哪些类型的来源。来源分为三类：

我们可以调整上一个示例，以便仅移除受保护网站中的数据，如下所示：

如需试用此 API，请从 chrome-extension-samples 代码库中安装 browsingData API 示例。

一组数据类型。缺失的数据类型会被解读为 false。

已移除通过扩展程序删除密码的功能。系统会忽略此数据类型。

已移除对 Flash 的支持。系统会忽略此数据类型。

已移除对服务器绑定证书的支持。系统会忽略此数据类型。

如果存在，则此列表中的来源对应的数据不会被删除。不能与 origins 结合使用。仅支持 Cookie、存储空间和缓存。整个可注册网域都会排除 Cookie。

一个对象，其属性用于指定应清除哪些来源类型。如果未指定此对象，则默认仅清除“不受保护”的来源。在添加“protectedWeb”或“extensions”之前，请确保您确实要移除应用数据。

用户已安装的扩展程序和打包应用（请务必谨慎使用！）。

[string, ...string[]] 可选

如果存在，则仅删除此列表中的来源的数据。仅支持 Cookie、存储空间和缓存。系统会清除整个可注册网域的 Cookie。

移除自相应日期（以自纪元开始算起的毫秒数表示，可通过 JavaScript Date 对象的 getTime 方法访问）起累积的数据。如果未提供，则默认为 0（这将移除所有浏览数据）。

清除用户个人资料中存储的各种类型的浏览数据。

清除在特定时间范围内修改的浏览器 Cookie 和服务器绑定证书。

清除浏览器中的已下载文件列表（不清除已下载的文件本身）。

已移除通过扩展程序删除密码的功能。此函数无效。

已移除对 Flash 的支持。此函数无效。

报告“清除浏览数据”设置界面中当前选择的数据类型。注意：此 API 中包含的某些数据类型在设置界面中不可用，并且某些界面设置可控制此处列出的多种数据类型。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "browsingData",
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var callback = function () {
  // Do something clever here once data has been removed.
};

var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;
var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
chrome.browsingData.remove({
  "since": oneWeekAgo
}, {
  "appcache": true,
  "cache": true,
  "cacheStorage": true,
  "cookies": true,
  "downloads": true,
  "fileSystems": true,
  "formData": true,
  "history": true,
  "indexedDB": true,
  "localStorage": true,
  "passwords": true,
  "serviceWorkers": true,
  "webSQL": true
}, callback);
```

Example 3 (unknown):
```unknown
var callback = function () {
  // Do something clever here once data has been removed.
};

var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;
var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
chrome.browsingData.removeCookies({
  "since": oneWeekAgo
}, callback);
```

Example 4 (unknown):
```unknown
chrome.browsingData.remove({
  "origins": ["https://www.example.com"]
}, {
  "cacheStorage": true,
  "cookies": true,
  "fileSystems": true,
  "indexedDB": true,
  "localStorage": true,
  "serviceWorkers": true,
  "webSQL": true
}, callback);
```

---

## chrome.search 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/search?hl=zh-cn

**Contents:**
- chrome.search 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Disposition
    - 枚举
  - QueryInfo
    - 属性
- 方法

使用 chrome.search API 通过默认提供程序进行搜索。

“CURRENT_TAB” 指定搜索结果显示在调用标签页或活动浏览器中的标签页中。

“NEW_TAB” 指定搜索结果显示在新标签页中。

“NEW_WINDOW” 指定搜索结果显示在新窗口中。

应显示搜索结果的位置。默认为 CURRENT_TAB。

应显示搜索结果的位置。tabId 无法与 disposition 搭配使用。

用于查询默认搜索服务提供商。如果出现错误，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
chrome.search.query(  queryInfo: QueryInfo,): Promise<void>
```

---

## chrome.i18n 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/i18n?hl=zh-cn

**Contents:**
- chrome.i18n 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概念和用法
  - 支持多种语言
  - 预定义的消息
  - 语言区域
  - 搜索邮件
  - 设置浏览器的语言区域
    - Windows

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

如果扩展程序具有 /_locales 目录，则清单必须定义 "default_locale"。

您需要将其所有面向用户的字符串都放入名为 messages.json 的文件中。每次添加新的语言区域时，您都会在名为 /_locales/_localeCode_ 的目录下添加一个消息文件，其中 localeCode 是一个代码，例如 en 表示英语。

以下是支持英语 (en)、西班牙语 (es) 和韩语 (ko) 的国际化扩展程序的文件夹层次结构：

假设您有一个扩展程序，其中包含下图所示的文件：

为了实现此扩展程序的国际化，您需要为每个面向用户的字符串命名，并将其放入消息文件中。扩展程序的清单、CSS 文件和 JavaScript 代码使用每个字符串的名称来获取其本地化版本。

以下是国际化后的扩展程序（请注意，它仍然只有英文字符串）：

在 manifest.json 和 CSS 文件中，按如下方式引用名为 messagename 的字符串：

在扩展程序或应用的 JavaScript 代码中，按如下方式引用名为 messagename 的字符串：

在每次对 getMessage() 的调用中，您最多可以提供 9 个要包含在消息中的字符串。如需了解详情，请参阅 示例：getMessage。

某些消息（例如 @@bidi_dir 和 @@ui_locale）由国际化系统提供。如需查看预定义消息名称的完整列表，请参阅预定义消息部分。

在 messages.json 中，每个面向用户的字符串都有一个名称、一个“message”项和一个可选的“description”项。该名称是一个键，例如“extName”或“search_string”，用于标识字符串。“message”指定相应语言区域中字符串的值。可选的“说明”可为翻译人员提供帮助，因为他们可能无法了解字符串在扩展程序中的使用方式。例如：

如需了解详情，请参阅格式：特定于语言区域的消息。

扩展程序国际化后，翻译起来非常简单。您复制 messages.json，对其进行翻译，然后将副本放入 /_locales 下的新目录中。例如，如需支持西班牙语，只需将 messages.json 的翻译副本放在 /_locales/es 下即可。下图显示了之前添加了新的西班牙语翻译的扩展程序。

国际化系统提供了一些预定义的消息，可帮助您进行本地化。这些资源包括 @@ui_locale，因此您可以检测当前界面语言区域，以及一些 @@bidi_... 消息，让您可以检测文字方向。后一种消息的名称与 gadgets BIDI（双向）API 中的常量类似。

无论扩展程序或应用是否已本地化，都可以在 CSS 和 JavaScript 文件中使用特殊消息 @@extension_id。此消息不适用于清单文件。

以下示例展示了如何在 CSS 文件中使用 @@extension_id 构建网址：

如果扩展程序 ID 为 abcdefghijklmnopqrstuvwxyzabcdef，则上一个代码段中的粗体行将变为：

以下示例展示了如何在 CSS 文件中使用 @@bidi_* 消息：

对于从左到右书写的语言（例如英语），粗体行变为：

您可以从多种语言区域中进行选择，包括一些（例如 en）允许单个翻译支持多种语言变体（例如 en_GB 和 en_US）。

您可以将扩展程序本地化为 Chrome 应用商店支持的任何语言区域。如果此处未列出您的语言区域，请选择最接近的替代选项。例如，如果扩展程序的默认语言区域设置是 "de_CH"，请在 Chrome 应用商店中选择 "de"。

您不必为每个受支持的语言区域都定义每个字符串。只要默认语言区域的 messages.json 文件中包含每个字符串的值，无论翻译有多稀疏，扩展程序或应用都会运行。扩展程序系统会按以下方式搜索消息：

在下图中，名为“colores”的消息位于扩展程序支持的所有三种语言区域中，但“extName”仅位于两种语言区域中。在美国境内使用英语版 Google Chrome 的用户看到的是“Colors”标签，而使用英式英语的用户看到的是“Colours”。美国英语用户和英国英语用户都会看到扩展程序名称“Hello World”。由于默认语言为西班牙语，因此以任何非英语语言运行 Google Chrome 的用户都会看到“Colores”标签和“Hola mundo”扩展程序名称。

如需测试翻译，您可能需要设置浏览器的语言区域。本部分介绍了如何在 Windows、Mac OS、Linux 和 ChromeOS 中设置语言区域。

您可以使用特定于语言区域的快捷方式或 Google Chrome 界面来更改语言区域。快捷方式方法在设置完毕后速度更快，并且可让您同时使用多种语言。

如需创建和使用可启动 Google Chrome 并指定特定语言区域的快捷方式，请执行以下操作：

更改快捷方式的属性，使“目标”字段指定 --lang 和 --user-data-dir 标志。目标应如下所示：

双击快捷方式启动 Google Chrome。

例如，如需创建以西班牙语 (es) 启动 Google Chrome 的快捷方式，您可以创建一个名为 chrome-es 的快捷方式，其目标如下：

您可以根据需要创建任意数量的快捷方式，以便轻松进行多语言测试。例如：

以下是在 Google Chrome（Windows 版）上使用界面更改语言区域的方法：

如需在 Mac 上更改语言区域，请使用系统偏好设置。

如需在 Linux 上更改语言区域，请先退出 Google Chrome。然后，在一行中设置 LANGUAGE 环境变量并启动 Google Chrome。例如：

如需在 ChromeOS 上更改语言区域，请执行以下操作：

您可以在 examples/api/i18n 目录中找到国际化示例。如需查看完整示例，请参阅 examples/extensions/news。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

以下代码从浏览器获取本地化消息，并将其显示为字符串。它会将消息中的两个占位符替换为字符串“string1”和“string2”。

如需详细了解占位符，请参阅特定于语言区域的消息页面。如需详细了解如何调用 getMessage()，请参阅 API 参考文档。

以下代码从浏览器获取 accept-languages，并通过用“,”分隔每个 accept-language 将它们显示为字符串。

如需详细了解如何调用 getAcceptLanguages()，请参阅 API 参考文档。

以下代码可从给定的字符串中检测最多 3 种语言，并以换行符分隔的字符串形式显示结果。

如需详细了解如何调用 detectLanguage(inputText)，请参阅 API 参考文档。

ISO 语言代码，例如 en 或 fr。如需查看此方法支持的语言的完整列表，请参阅 kLanguageInfoTable。对于未知语言，系统将返回 und，这意味着 CLD 无法识别 [百分比] 的文本

获取浏览器的 accept-languages。这与浏览器使用的语言区域不同；如需获取语言区域，请使用 i18n.getUILanguage。

Promise<LanguageCode[]>

获取指定消息的本地化字符串。如果缺少消息，此方法会返回空字符串 ('')。如果 getMessage() 调用的格式有误（例如，messageName 不是字符串，或者 substitutions 数组的元素超过 9 个），此方法会返回 undefined。

消息的名称，如 messages.json 文件中所指定。

在翻译为 &lt; 时，转义 <。这仅适用于消息本身，而不适用于占位符。如果翻译内容用于 HTML 上下文中，开发者可能需要使用此方法。与 Closure 编译器搭配使用的 Closure 模板会自动生成此文件。

获取浏览器的浏览器界面语言。这与返回首选用户语言的 i18n.getAcceptLanguages 不同。

浏览器界面语言代码，例如 en-US 或 fr-FR。

**Examples:**

Example 1 (unknown):
```unknown
__MSG_messagename__
```

Example 2 (unknown):
```unknown
chrome.i18n.getMessage("messagename")
```

Example 3 (unknown):
```unknown
{
  "search_string": {
    "message": "hello%20world",
    "description": "The string we search for. Put %20 between words that go together."
  },
  ...
}
```

Example 4 (unknown):
```unknown
body {
  background-image:url('chrome-extension://__MSG_@@extension_id__/background.png');
}
```

---

## chrome.proxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/proxy?hl=zh-cn

**Contents:**
- chrome.proxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 代理模式
  - 代理规则
  - 代理服务器对象
  - 绕过列表
- 示例
- 类型

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖 ChromeSetting 类型 API 原型来获取和设置代理配置。

您必须声明“代理”权限，以使用代理设置 API。例如：

代理设置在 proxy.ProxyConfig 对象中定义。根据 Chrome 的代理设置， 这些设置可能包含 proxy.ProxyRules 或 proxy.PacScript。

ProxyConfig 对象的 mode 属性决定了 Chrome 的整体行为 代理用量。它可以采用以下值：

proxy.ProxyRules 对象可以包含 singleProxy 属性或 proxyForHttp、proxyForHttps、proxyForFtp 和 fallbackProxy。

在第一种情况下，系统会通过指定的代理服务器代理 HTTP、HTTPS 和 FTP 流量。其他 直接发送流量对于后一种情况，其行为略微巧妙：如果代理服务器 针对 HTTP、HTTPS 或 FTP 协议进行了配置，则相应流量将通过 指定服务器如果未指定此类代理服务器或流量使用的协议 HTTP、HTTPS 或 FTP，使用 fallbackProxy。如果未指定 fallbackProxy，则系统会发送流量 而无需代理服务器。

代理服务器是在 proxy.ProxyServer 对象中配置的。与代理服务器的连接 （由 host 属性定义）使用 scheme 属性定义的协议。如果拒绝 已指定 scheme，则代理连接默认为 http。

如果 proxy.ProxyServer 对象中未定义 port，则系统会从架构派生端口。 默认端口为：

可以使用 bypassList 来排除各个服务器。此列表可能包含 以下条目：

匹配与 HOST_PATTERN 格式匹配的所有主机名。前导 "." 会被解释为 "*."。

示例："foobar.com", "*foobar.com", "*.foobar.com", "*foobar.com:99", "https://x.*.y.com:99"。

匹配作为 IP 地址字面量的网址。从概念上讲，这与第一种情况类似， 特殊情况来处理 IP 字面量规范化。例如，匹配“[0:0:0::1]” 与匹配“[::1]”相同因为 IPv6 规范化是在内部完成的

示例：127.0.1、[0:0::1]、[::1]:80、https://[::1]:443

匹配给定参数中任何包含 IP 字面量 (IP_LITERAL) 的网址 范围。IP 范围 (PREFIX_LENGTH_IN_BITS) 使用 CIDR 指定 表示法。

匹配给定范围内包含 IP 字面量的任何网址。IP 范围是使用 CIDR 指定的 标记。 示例："192.168.1.1/16", "fefe:13::abc/33"

字面量字符串 <local> 与简单的主机名匹配。简单的主机名是不包含 而不是 IP 字面量。例如，example 和 localhost 是简单的主机名， 而 example.com、example. 和 [::1] 则不行。

以下代码设置了 SOCKS 5 代理，用于与 foobar.com 以外的所有服务器的 HTTP 连接，并使用 直接连接（适用于所有其他协议）。这些设置会应用于常规窗口和无痕式窗口， 无痕式窗口会沿用常规窗口的设置。另请参阅 Types API 文档。

下一个代码段会查询当前的有效代理设置。有效的代理设置可以是 由其他扩展程序或政策决定。如需了解详情，请参阅 Types API 文档。

请注意，传递到 set() 的 value 对象与传递到 的 value 对象不同 回调函数 get()。后者将包含 rules.proxyForHttp.port 元素。

包含代理自动配置信息的对象。必须有一个字段为非空字段。

如果为 true，无效的 PAC 脚本将阻止网络堆栈回退到直接连接。默认值为 false。

“direct”= 从不使用代理 “auto_detect”= 自动检测代理设置 “pac_script”= 使用指定的 PAC 脚本 “fixed_servers”= 手动指定代理服务器 “system”= 使用系统代理设置

此配置的代理自动配置 (PAC) 脚本。将此用于“pac_script”模式。

描述此配置的代理规则。将此用于“fixed_servers”模式。

用于封装所有协议的一组代理规则的对象。使用“singleProxy”或“proxyForHttp”“proxyForHttps”“proxyForFtp”的子集和“fallbackProxy”

要在没有代理服务器的情况下连接的服务器列表。

用于其他任何用途或未指定任何特定 agentFor... 的代理服务器。

要用于所有 Per-网址 请求（即 http、https 和 ftp）的代理服务器。

代理服务器的主机名或 IP 地址。主机名必须采用 ASCII（Punycode 格式）。目前尚不支持 IDNA。

代理服务器的端口。默认为取决于 scheme 的端口。

代理服务器本身的架构（协议）。默认值为“http”。

要使用的代理设置。此设置的值为 ProxyConfig 对象。

types.ChromeSetting&lt;ProxyConfig&gt;

有关错误的其他详细信息，例如 JavaScript 运行时错误。

如果为 true，则错误为严重，网络事务已中止。否则，系统会改用直接连接。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "proxy"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var config = {
  mode: "fixed_servers",
  rules: {
    proxyForHttp: {
      scheme: "socks5",
      host: "1.2.3.4"
    },
    bypassList: ["foobar.com"]
  }
};
chrome.proxy.settings.set(
  {value: config, scope: 'regular'},
  function() {}
);
```

Example 3 (unknown):
```unknown
var config = {
  mode: "pac_script",
  pacScript: {
    data: "function FindProxyForURL(url, host) {\n" +
          "  if (host == 'foobar.com')\n" +
          "    return 'PROXY blackhole:80';\n" +
          "  return 'DIRECT';\n" +
          "}"
  }
};
chrome.proxy.settings.set(
  {value: config, scope: 'regular'},
  function() {}
);
```

Example 4 (unknown):
```unknown
chrome.proxy.settings.get(
  {'incognito': false},
  function(config) {
    console.log(JSON.stringify(config));
  }
);
```

---

## API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference?hl=zh-cn

**Contents:**
- API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

大多数扩展程序都需要访问一个或多个 Chrome 扩展程序 API 才能正常运行。 此 API 参考文档介绍了可在扩展程序中使用的 API，并提供了用例示例。

使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 API 类型的 ChromeSetting 原型来获取和设置各个无障碍功能。为了获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不意味着拥有 accessibilityFeatures.read 权限。

使用 chrome.alarms API 安排代码在指定时间或未来某个时间定期运行。

chrome.audio API 可供用户获取有关连接到系统的音频设备的信息并控制这些设备。此 API 目前仅在 ChromeOS 的自助服务终端模式下可用。

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

使用浏览器操作将图标放置在主 Google Chrome 工具栏中的地址栏右侧。除了图标之外，浏览器操作还可以具有提示、标记和弹出式窗口。

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

使用 chrome.declarativeContent API 根据网页内容采取行动，而无需获得读取网页内容的权限。

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

注意：此 API 已弃用。请改用 declarativeNetRequest API。使用 chrome.declarativeWebRequest API 拦截、阻止或修改正在处理的请求。它比 chrome.webRequest API 快得多，因为您可以注册在浏览器（而非 JavaScript 引擎）中评估的规则，从而减少往返延迟时间并提高效率。

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

使用 chrome.devtools.inspectedWindow API 与检查的窗口互动：获取检查的网页的标签页 ID、在检查的窗口的上下文中评估代码、重新加载网页或获取网页中的资源列表。

使用 chrome.devtools.network API 检索开发者工具在“网络”面板中显示的网络请求的相关信息。

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

使用 chrome.devtools.performance API 监听开发者工具中“性能”面板的录制状态更新。

使用 chrome.devtools.recorder API 自定义开发者工具中的“记录器”面板。

使用 chrome.dns API 进行 DNS 解析。

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

使用 chrome.dom API 访问扩展程序的特殊 DOM API

使用 chrome.downloads API 以编程方式发起、监控、操纵和搜索下载。

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

chrome.events 命名空间包含 API 在调度事件时使用的常见类型，用于在发生值得注意的事情时通知您。

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

使用 chrome.fileBrowserHandler API 扩展 Chrome OS 文件浏览器。例如，您可以使用此 API 让用户将文件上传到您的网站。

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

使用 chrome.identity API 获取 OAuth2 访问令牌。

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

使用 chrome.instanceID 访问实例 ID 服务。

使用 chrome.loginState API 读取和监控登录状态。

chrome.management API 提供了一些方法来管理已安装的应用和扩展程序。

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

使用 chrome.pageAction API 可在主 Google Chrome 工具栏中的地址栏右侧放置图标。网页操作是指可在当前网页上执行的操作，但并非适用于所有网页。不活动时，网页操作会显示为灰色。

使用 chrome.pageCapture API 将标签页另存为 MHTML。

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

使用 chrome.power API 可替换系统的电源管理功能。

chrome.printerProvider API 会公开打印管理器使用的事件，以便查询受扩展程序控制的打印机、查询这些打印机的功能，以及向这些打印机提交打印作业。

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

使用 chrome.processes API 与浏览器的进程进行交互。

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置代理配置。

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

使用 chrome.search API 通过默认提供程序进行搜索。

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

使用 system.cpu API 查询 CPU 元数据。

使用 system.display API 查询展示元数据。

chrome.system.memory API。

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

使用 chrome.tabCapture API 与标签页媒体流进行互动。

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

使用 chrome.ttsEngine API 通过扩展程序实现文字转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序都会收到包含要朗读的发言内容和其他参数的事件。然后，扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

chrome.types API 包含 Chrome 的类型声明。

使用 chrome.vpnProvider API 实现 VPN 客户端。

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

使用 chrome.webRequest API 观察和分析流量，并拦截、屏蔽或修改正在处理的请求。

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

---

## API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api?hl=zh-cn

**Contents:**
- API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- Common Extensions API 功能
- Chrome 扩展程序 API

大多数扩展程序都需要访问一个或多个 Chrome 扩展程序 API 才能正常运行。此 API 参考文档介绍了可在扩展程序中使用的 API，并提供了示例用例。

扩展程序 API 由一个命名空间组成，其中包含用于执行扩展程序工作的方法和属性，并且通常（但不一定）包含 manifest.json 文件的清单字段。例如，chrome.action 命名空间需要在清单中包含 "action" 对象。许多 API 还要求在清单中添加权限。

除非另有说明，否则扩展 API 中的方法是异步的。异步方法会立即返回，而无需等待调用它们的操作完成。使用 Promise 获取这些异步方法的结果。

使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 API 类型的 ChromeSetting 原型来获取和设置各个无障碍功能。为了获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不意味着拥有 accessibilityFeatures.read 权限。

使用 chrome.action API 控制 Google Chrome 工具栏中的扩展程序图标。

使用 chrome.alarms API 安排代码在指定时间或未来某个时间定期运行。

chrome.audio API 可供用户获取有关连接到系统的音频设备的信息并控制这些设备。此 API 目前仅在 ChromeOS 的自助服务终端模式下可用。

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

使用 chrome.declarativeContent API 根据网页内容采取行动，而无需获得读取网页内容的权限。

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

使用 chrome.devtools.inspectedWindow API 与检查的窗口互动：获取检查的网页的标签页 ID、在检查的窗口的上下文中评估代码、重新加载网页或获取网页中的资源列表。

使用 chrome.devtools.network API 检索开发者工具在“网络”面板中显示的网络请求的相关信息。

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

使用 chrome.devtools.performance API 监听开发者工具中“性能”面板的录制状态更新。

使用 chrome.devtools.recorder API 自定义开发者工具中的“记录器”面板。

使用 chrome.dns API 进行 DNS 解析。

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

使用 chrome.dom API 访问扩展程序的特殊 DOM API

使用 chrome.downloads API 以编程方式发起、监控、操纵和搜索下载。

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

chrome.events 命名空间包含 API 在调度事件时使用的常见类型，用于在发生值得注意的事情时通知您。

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

使用 chrome.fileBrowserHandler API 扩展 Chrome OS 文件浏览器。例如，您可以使用此 API 让用户将文件上传到您的网站。

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

使用 chrome.identity API 获取 OAuth2 访问令牌。

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

使用 chrome.instanceID 访问实例 ID 服务。

使用 chrome.loginState API 读取和监控登录状态。

chrome.management API 提供了一些方法来管理已安装的应用和扩展程序。

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

使用 offscreen API 创建和管理屏幕外文档。

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

使用 chrome.pageCapture API 将标签页另存为 MHTML。

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

使用 chrome.power API 可替换系统的电源管理功能。

chrome.printerProvider API 会公开打印管理器使用的事件，以便查询受扩展程序控制的打印机、查询这些打印机的功能，以及向这些打印机提交打印作业。

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

使用 chrome.processes API 与浏览器的进程进行交互。

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置代理配置。

使用 chrome.readingList API 读取和修改阅读清单中的内容。

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

使用 chrome.scripting API 在不同上下文中执行脚本。

使用 chrome.search API 通过默认提供程序进行搜索。

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

使用 chrome.sidePanel API 在浏览器的侧边栏中托管内容，与网页的主要内容并排显示。

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

使用 system.cpu API 查询 CPU 元数据。

使用 system.display API 查询展示元数据。

chrome.system.memory API。

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

使用 chrome.tabCapture API 与标签页媒体流进行互动。

使用 chrome.tabGroups API 与浏览器的标签页分组系统进行交互。您可以使用此 API 修改和重新排列浏览器中的标签页组。如需对标签页进行分组和取消分组，或查询哪些标签页位于分组中，请使用 chrome.tabs API。

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

使用 chrome.ttsEngine API 通过扩展程序实现文字转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序都会收到包含要朗读的发言内容和其他参数的事件。然后，扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

chrome.types API 包含 Chrome 的类型声明。

使用 userScripts API 在用户脚本上下文中执行用户脚本。

使用 chrome.vpnProvider API 实现 VPN 客户端。

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

借助 chrome.webAuthenticationProxy API，在远程主机上运行的远程桌面软件可以拦截 Web 身份验证 API (WebAuthn) 请求，以便在本地客户端上处理这些请求。

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

使用 chrome.webRequest API 观察和分析流量，并拦截、屏蔽或修改正在处理的请求。

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

---

## chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/panels

**Contents:**
- chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - Button
    - 属性
  - ElementsPanel
    - 属性
  - ExtensionPanel

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

每个扩展程序面板和边栏都显示为单独的 HTML 页面。开发者工具窗口中显示的所有扩展程序页面都可以访问 chrome.devtools API 的所有部分以及所有其他扩展程序 API。

您可以使用 devtools.panels.setOpenResourceHandler 方法安装一个回调函数，该函数用于处理用户打开资源（通常是在开发者工具窗口中点击资源链接）的请求。最多只能调用一个已安装的处理程序；用户可以使用“开发者工具设置”对话框指定默认行为或扩展程序来处理资源打开请求。如果扩展程序多次调用 setOpenResourceHandler()，则仅保留最后一个处理程序。

如需大致了解如何使用开发者工具 API，请参阅开发者工具 API 摘要。

如需使用此 API，必须在清单中声明以下键。

以下代码添加了一个包含在 Panel.html 中的面板，该面板在开发者工具栏上以 FontPicker.png 表示，并标记为 Font Picker：

以下代码向“元素”面板添加了一个包含在 Sidebar.html 中且标题为字体属性的侧边栏窗格，然后将其高度设置为 8ex：

此屏幕截图展示了此示例对开发者工具窗口的影响：

如需试用此 API，请从 chrome-extension-samples 代码库中安装 devtools panels API 示例。

Event<functionvoidvoid>

onClicked.addListener 函数如下所示：

更新按钮的属性。如果省略了部分实参或将部分实参设为 null，则不会更新相应的属性。

当用户将鼠标悬停在按钮上时，以提示形式显示的文字。

Event<functionvoidvoid>

onSelectionChanged.addListener 函数如下所示：

createSidebarPane 函数如下所示：

已创建的侧边栏窗格的 ExtensionSidebarPane 对象。

Event<functionvoidvoid>

onHidden.addListener 函数如下所示：

Event<functionvoidvoid>

在发生搜索操作（开始新搜索、导航到搜索结果或取消搜索）时触发。

onSearch.addListener 函数如下所示：

Event<functionvoidvoid>

onShown.addListener 函数如下所示：

createStatusBarButton 函数如下所示：

按钮图标的路径。该文件应包含一张 64x24 像素的图片，该图片由两个 32x24 的图标组成。左侧图标用于按钮处于非活动状态时；右侧图标用于按钮处于按下状态时。

当用户将鼠标悬停在按钮上时，以提示形式显示的文字。

Event<functionvoidvoid>

当用户切换到托管侧边栏窗格的面板时，侧边栏窗格变为隐藏状态时触发。

onHidden.addListener 函数如下所示：

Event<functionvoidvoid>

当用户切换到托管侧边栏窗格的面板时，侧边栏窗格变为可见状态时触发。

onShown.addListener 函数如下所示：

设置在检查的网页中求值的表达式。结果会显示在侧边栏窗格中。

setExpression 函数如下所示：

要在检查的页面上下文中求值的表达式。JavaScript 对象和 DOM 节点会显示在可展开的树中，类似于控制台/监视。

类似 CSS 的尺寸规范，例如 '100px' 或 '12ex'。

设置要在边栏窗格中显示的 JSON 兼容对象。

要在检查的网页上下文中显示的对象。在调用方（API 客户端）的上下文中进行评估。

设置要在边栏窗格中显示的 HTML 网页。

Event<functionvoidvoid>

onSelectionChanged.addListener 函数如下所示：

createSidebarPane 函数如下所示：

已创建的侧边栏窗格的 ExtensionSidebarPane 对象。

“default” 默认的 DevTools 主题。始终为浅色主题。

用户在开发者工具设置中设置的颜色主题的名称。可能的值：default（默认）和 dark。

在开发者工具栏中扩展程序图标旁边显示的标题。

面板 HTML 页面相对于扩展程序目录的路径。

表示所创建面板的 ExtensionPanel 对象。

请求开发者工具在开发者工具面板中打开网址。

指定当用户点击开发者工具窗口中的资源链接时要调用的函数。如需取消设置处理程序，请调用不带参数的方法，或传递 null 作为参数。

所点击资源的 devtools.inspectedWindow.Resource 对象。

指定在开发者工具中当前主题发生更改时要调用的函数。如需取消设置处理程序，请调用不带参数的方法，或传递 null 作为参数。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.panels.create("Font Picker",
                              "FontPicker.png",
                              "Panel.html",
                              function(panel) { ... });
```

Example 2 (unknown):
```unknown
chrome.devtools.panels.elements.createSidebarPane("Font Properties",
  function(sidebar) {
    sidebar.setPage("Sidebar.html");
    sidebar.setHeight("8ex");
  }
);
```

Example 3 (javascript):
```javascript
(callback: function) => {...}
```

Example 4 (javascript):
```javascript
(iconPath?: string, tooltipText?: string, disabled?: boolean) => {...}
```

---

## chrome.printerProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printerProvider

**Contents:**
- chrome.printerProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - PrinterInfo
    - 属性
  - PrintError
    - 枚举
  - PrintJob

chrome.printerProvider API 公开了打印管理器用于查询由扩展程序控制的打印机、查询其功能以及向这些打印机提交打印作业的事件。

为响应 onPrintRequested 事件而返回的错误代码。

"INVALID_TICKET" 指定打印票券无效。例如，支持服务工单与某些功能不一致，或者扩展程序无法处理工单中的所有设置。

"INVALID_DATA" 指定文档无效。例如，数据可能已损坏，或者格式与扩展程序不兼容。

文档内容类型。支持的格式为 "application/pdf" 和 "image/pwg-raster"。

包含要打印的文档数据的 Blob。格式必须与“contentType”一致。

CJT 引用被标记为已弃用。此功能仅可用于 Google 云打印。未针对 ChromeOS 打印而弃用。

resultCallback 参数如下所示：

打印管理器请求扩展程序提供的打印机时会触发事件。

resultCallback 参数如下所示：

打印管理器请求有关可能是打印机的 USB 设备的信息时会触发事件。

注意：应用不应期望此事件在每台设备上触发多次。如果已连接的设备受支持，则应在 onGetPrintersRequested 事件中返回相应设备。

resultCallback 参数如下所示：

resultCallback 参数如下所示：

**Examples:**

Example 1 (unknown):
```unknown
chrome.printerProvider.onGetCapabilityRequested.addListener(  callback: function,)
```

Example 2 (javascript):
```javascript
(printerId: string, resultCallback: function) => void
```

Example 3 (javascript):
```javascript
(capabilities: object) => void
```

Example 4 (unknown):
```unknown
chrome.printerProvider.onGetPrintersRequested.addListener(  callback: function,)
```

---

## chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabs/?hl=zh-cn

**Contents:**
- chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 使用场景
  - 在新标签页中打开扩展程序页面
  - 获取当前标签页
  - 将指定标签页静音
  - 点击时将当前标签页移至第一个位置
  - 将消息传递给所选标签页的内容脚本
- 扩展示例

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

Tabs API 不仅提供用于操纵和管理标签页的功能，还可以检测标签页的语言、截取屏幕截图，以及与标签页的内容脚本通信。

大多数功能无需任何权限即可使用。例如：创建新标签页、重新加载标签页、前往其他网址等。

开发者在使用 Tabs API 时应注意以下三种权限。

此权限不授予对 chrome.tabs 命名空间的访问权限。相反，它会授予扩展程序针对 tabs.Tab 实例上的四个敏感属性（url、pendingUrl、title 和 favIconUrl）调用 tabs.query() 的能力。

主机权限允许扩展程序读取和查询匹配标签页的四项敏感 tabs.Tab 属性。它们还可以使用 tabs.captureVisibleTab()、scripting.executeScript()、scripting.insertCSS() 和 scripting.removeCSS() 等方法直接与匹配的标签页互动。

activeTab 会在用户调用时授予扩展程序当前标签页的临时主机权限。与主机权限不同，activeTab 不会触发任何警告。

扩展程序的一个常见模式是在安装时在新标签页中打开初始配置页面。以下示例展示了如何执行此操作。

此示例演示了扩展程序的服务工作线程如何从当前聚焦的窗口（如果没有聚焦任何 Chrome 窗口，则从最近聚焦的窗口）检索活动标签页。这通常可以视为用户的当前标签页。

此示例展示了扩展程序如何切换指定标签页的静音状态。

此示例展示了如何在拖动可能正在进行或可能未在进行时移动标签页。虽然此示例使用 chrome.tabs.move，但您也可以将相同的等待模式用于在拖动过程中修改标签页的其他调用。

此示例演示了扩展程序的服务工作线程如何使用 tabs.sendMessage() 与特定浏览器标签页中的内容脚本进行通信。

如需查看更多 Tabs API 扩展程序演示，请探索以下任一内容：

相应标签页的静音状态以及上次状态更改的原因。

更改静音状态的扩展程序的 ID。如果扩展程序不是静音状态上次更改的原因，则不设置。

标签页是否处于静音状态（无法播放声音）。即使标签页尚未播放或当前未播放声音，也可能会处于静音状态。相当于是否显示“静音”音频指示器。

相应标签页静音或取消静音的原因。如果相应标签页的静音状态从未更改过，则不设置。

“user” 用户输入操作设置了静音状态。

“捕获” 标签页捕获已开始，强制更改为静音状态。

“extension” 由 extensionId 字段标识的扩展程序，用于设置静音状态。

相应标签页在其窗口中是否处于活动状态。不一定表示窗口已聚焦。

相应标签页在过去几秒内是否发出过声音（但如果同时处于静音状态，则可能听不到声音）。相当于“扬声器音频”指示器是否显示。

当资源不足时，浏览器是否可以自动舍弃相应标签页。

标签页是否已舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

相应标签页的网站图标的网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页正在加载，该值也可能为空字符串。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页的 ID。标签页 ID 在浏览器会话中是唯一的。在某些情况下，标签页可能未分配 ID；例如，使用 sessions API 查询外部标签页时，可能会出现会话 ID。对于应用和开发者工具窗口，标签页 ID 也可以设置为 chrome.tabs.TAB_ID_NONE。

相应标签页上次在其窗口中变为活动状态的时间（以自纪元以来经过的毫秒数表示）。

相应标签页的静音状态以及上次状态更改的原因。

打开此标签页的标签页的 ID（如果有）。仅当打开程序标签页仍然存在时，此属性才会存在。

标签页正在前往的网址（在提交之前）。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限，并且存在待处理的导航时，才会显示此属性。

请使用 tabs.Tab.highlighted。

用于唯一标识从 sessions API 获取的标签页的会话 ID。

标签页的标题。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，此属性才会存在。

相应标签页主框架的上次已提交网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页尚未提交，则可能为空字符串。另请参阅 Tab.pendingUrl。

定义如何处理标签页中的缩放更改以及在什么范围内处理。

用于在对 tabs.getZoomSettings 的调用中返回当前标签页的默认缩放级别。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

“手动” 替换自动处理缩放更改。系统仍会调度 onZoomChange 事件，扩展程序有责任监听此事件并手动缩放网页。此模式不支持 per-origin 缩放，因此会忽略 scope 缩放设置并假定为 per-tab。

“已停用” 停用标签页中的所有缩放功能。相应标签页会恢复为默认缩放级别，并且系统会忽略所有尝试进行的缩放更改。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

“按来源” 缩放更改会保留在缩放网页的来源中，也就是说，导航到同一来源的所有其他标签页也会缩放。此外，per-origin 缩放更改会与来源一起保存，这意味着当导航到同一来源中的其他网页时，这些网页都会缩放到相同的缩放系数。per-origin 范围仅在 automatic 模式下可用。

“按标签页” 缩放更改仅在此标签页中生效，其他标签页中的缩放更改不会影响此标签页的缩放。此外，per-tab 缩放比例会在导航时重置；导航标签页始终会加载具有 per-origin 缩放因子的网页。

每秒可调用 captureVisibleTab 的次数上限。captureVisibleTab 的开销很大，不应过于频繁地调用。

表示 tab_strip 中没有标签页索引的索引。

捕获指定窗口中当前活动标签页的可见区域。如需调用此方法，扩展程序必须拥有 <all_urls> 权限或 activeTab 权限。除了扩展程序通常可以访问的网站之外，此方法还允许扩展程序捕获其他受限的敏感网站，包括 chrome:-scheme 网页、其他扩展程序的网页和 data: 网址。只有拥有 activeTab 权限才能捕获这些敏感网站。只有在扩展程序获得文件访问权限后，才能捕获文件网址。

连接到指定标签页中的内容脚本。runtime.onConnect 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。如需了解详情，请参阅内容脚本消息传递。

打开由 documentId 标识的特定文档的端口，而不是标签页中的所有框架。

打开由 frameId 标识的特定框架的端口，而不是标签页中的所有框架。

传递给正在监听连接事件的内容脚本的 onConnect。

可用于与指定标签页中运行的内容脚本通信的端口。如果标签页关闭或不存在，则会触发端口的 runtime.Port 事件。

标签页是否应成为窗口中的活动标签页。不影响窗口是否处于聚焦状态（请参阅 windows.update）。默认值为 true。

标签页在窗口中应占据的位置。提供的值会限制在 0 到窗口中的标签页数量之间。

打开此标签页的标签页的 ID。如果指定，则打开程序标签页必须与新创建的标签页位于同一窗口中。

相应标签页是否应固定。默认设置为 false

相应标签页是否应成为窗口中的所选标签页。默认设置为 true

标签页最初导航到的网址。完全限定网址必须包含方案（即“http://www.google.com”，而不是“www.google.com”）。相对网址相对于扩展程序中的当前网页。默认为“新标签页”。

从内存中舍弃标签页。舍弃的标签页仍会显示在标签栏中，并在激活时重新加载。

要舍弃的标签页的 ID。如果指定了该参数，则除非标签页处于活动状态或已舍弃，否则会舍弃该标签页。如果省略，浏览器会舍弃最不重要的标签页。如果没有可舍弃的标签页，此操作可能会失败。

Promise<Tab | undefined>

Promise<Tab | undefined>

获取发出此脚本调用的标签页。如果从非标签页上下文（例如，后台网页或弹出式窗口视图）调用，则返回 undefined。

Promise<Tab | undefined>

要从中获取当前缩放系数的标签页的 ID；默认为当前窗口的活动标签页。

要从中获取当前缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

Promise<ZoomSettings>

要返回的标签页的 ID；默认为当前窗口的所选标签页。

要向前导航的标签页的 ID；默认为当前窗口的所选标签页。

将一个或多个标签页添加到指定的分组；如果未指定分组，则将给定的标签页添加到新创建的分组。

用于创建群组的配置。如果已指定 groupId，则无法使用此属性。

要将标签页添加到的群组的 ID。如果未指定，系统会创建一个新组。

number | [number, ...number[]]

要添加到指定群组的标签页 ID 或标签页 ID 列表。

突出显示给定的标签页，并将焦点放在第一个标签页上。如果指定标签页当前处于活动状态，则看起来不会执行任何操作。

Promise<windows.Window>

将一个或多个标签页移动到其窗口中的新位置，或移动到新窗口。请注意，标签页只能在普通窗口（window.type === "normal"）之间移动。

要移动的标签页 ID 或标签页 ID 列表。

要将窗口移至的位置。使用 -1 将标签页放置在窗口末尾。

获取具有指定属性的所有标签页，如果未指定属性，则获取所有标签页。

浏览器是否可以在资源不足时自动舍弃标签页。

标签页是否被舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页所在群组的 ID，或 tabGroups.TAB_GROUP_ID_NONE（对于未分组的标签页）。

标签页所在的拆分视图的 ID；如果标签页不在拆分视图中，则为 tabs.SPLIT_VIEW_ID_NONE。

根据某种模式匹配网页标题。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

根据一个或多个 网址 格式匹配标签页。片段标识符不匹配。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

父窗口的 ID，或windows.WINDOW_ID_CURRENT（表示当前窗口）。

要重新加载的标签页的 ID；默认为当前窗口的所选标签页。

要关闭的标签页 ID 或标签页 ID 列表。

向指定标签页中的内容脚本发送一条消息，并提供一个可选的回调函数，用于在收到响应时运行。runtime.onMessage 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。

要发送的消息。此消息应为可 JSON 化的对象。

向由 documentId 标识的特定文档发送消息，而不是向标签页中的所有框架发送消息。

向由 frameId 标识的特定帧发送消息，而不是向标签页中的所有帧发送消息。

要缩放的标签页的 ID；默认为当前窗口的活动标签页。

新的缩放比例。值为 0 时，标签页将设置为其当前的默认缩放比例。大于 0 的值指定了相应标签页的缩放比例（可能不是默认值）。

为指定标签页设置缩放设置，以定义如何处理缩放更改。在标签页之间切换时，这些设置会重置为默认值。

要更改缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

定义如何处理缩放更改以及在哪个范围内处理。

从相应群组中移除一个或多个标签页。如果任何组变为空组，系统会将其删除。

number | [number, ...number[]]

要从相应群组中移除的标签页 ID 或标签页 ID 列表。

修改标签页的属性。不会修改未在 updateProperties 中指定的属性。

相应标签页是否应处于有效状态。不影响窗口是否处于聚焦状态（请参阅 windows.update）。

当资源不足时，浏览器是否应自动舍弃相应标签页。

打开此标签页的标签页的 ID。如果指定，打开的标签页必须与当前标签页位于同一窗口中。

要将标签页导航到的网址。不支持 JavaScript 网址；请改用 scripting.executeScript。

Promise<Tab | undefined>

当窗口中的有效标签页发生变化时触发。请注意，此事件触发时，标签页的网址可能尚未设置，但您可以监听 onUpdated 事件，以便在网址设置时收到通知。

当标签页附加到窗口时触发；例如，当标签页在窗口之间移动时。

在创建标签页时触发。请注意，触发此事件时，标签页的网址和标签页分组会员资格可能尚未设置，但您可以监听 onUpdated 事件，以便在设置网址或将标签页添加到标签页分组时收到通知。

当标签页从窗口分离时触发；例如，当标签页在窗口之间移动时。

当窗口中突出显示或选定的标签页发生变化时触发。

当标签页在窗口内移动时触发。系统只会触发一个移动事件，表示用户直接移动的标签页。对于必须响应手动移动的标签页而移动的其他标签页，不会触发移动事件。当标签页在窗口之间移动时，不会触发此事件；如需了解详情，请参阅 tabs.onDetached。

如果标签页因其父窗口关闭而关闭，则为 True。

在标签页因预渲染或即时而替换为另一个标签页时触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "tabs"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "http://*/*",
    "https://*/*"
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "activeTab"
  ],
  ...
}
```

Example 4 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(({reason}) => {
  if (reason === 'install') {
    chrome.tabs.create({
      url: "onboarding.html"
    });
  }
});
```

---

## chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/windows?hl=zh-cn

**Contents:**
- chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 当前窗口
- 示例
- 类型
  - CreateType
    - 枚举
  - QueryOptions

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

如果请求了 windows.Window，则该对象包含一个 tabs.Tab 对象数组。如果您需要访问 tabs.Tab 的 url、pendingUrl、title 或 favIconUrl 属性，则必须在清单中声明 "tabs" 权限。例如：

扩展系统中的许多函数都接受一个可选的 windowId 实参，该实参默认为当前窗口。

当前窗口是指包含当前正在执行的代码的窗口。请务必注意，此窗口可能与最上层或聚焦窗口不同。

例如，假设某个扩展程序通过单个 HTML 文件创建了几个标签页或窗口，并且该 HTML 文件包含对 tabs.query() 的调用。当前窗口是指包含发出调用的网页的窗口，无论最顶层的窗口是什么。

对于 service worker，当前窗口的值会回退到上一个有效窗口。在某些情况下，后台网页可能没有当前窗口。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 Windows API 示例。

指定要创建的浏览器窗口的类型。“panel”已被弃用，仅适用于 ChromeOS 上已列入许可名单的现有扩展程序。

如果为 true，则 windows.Window 对象具有 tabs 属性，其中包含 tabs.Tab 对象的列表。仅当扩展程序的清单文件包含 "tabs" 权限时，Tab 对象才包含 url、pendingUrl、title 和 favIconUrl 属性。

WindowTypeWindowType[] 可选

如果已设置，则返回的 windows.Window 会根据其类型进行过滤。如果未设置，则默认过滤器设置为 ['normal', 'popup']。

窗口的高度（包括框架），以像素为单位。在某些情况下，窗口可能未分配 height 属性；例如，当通过 sessions API 查询已关闭的窗口时。

窗口的 ID。窗口 ID 在浏览器会话中是唯一的。在某些情况下，窗口可能未分配 ID 属性；例如，当使用 sessions API 查询窗口时，在这种情况下，可能会存在会话 ID。

窗口与屏幕左边缘的偏移量（以像素为单位）。在某些情况下，窗口可能未分配 left 属性；例如，当通过 sessions API 查询已关闭的窗口时。

用于唯一标识窗口的会话 ID，通过 sessions API 获取。

一个 tabs.Tab 对象数组，表示窗口中的当前标签页。

窗口距离屏幕顶部边缘的偏移量（以像素为单位）。在某些情况下，窗口可能未分配 top 属性；例如，当通过 sessions API 查询已关闭的窗口时。

窗口的宽度（包括边框），以像素为单位。在某些情况下，窗口可能未分配 width 属性；例如，当通过 sessions API 查询已关闭的窗口时。

相应浏览器窗口的状态。在某些情况下，窗口可能未分配 state 属性；例如，当通过 sessions API 查询已关闭的窗口时。

“normal” 正常窗口状态（未最小化、最大化或全屏）。

“locked-fullscreen” 锁定全屏窗口状态。用户无法通过操作退出此全屏状态，并且此状态仅适用于 Chrome 操作系统上已列入许可名单的扩展程序。

相应浏览器窗口的类型。在某些情况下，窗口可能未分配 type 属性；例如，通过 sessions API 查询已关闭的窗口时。

“panel” 此 API 中已弃用。Chrome 应用面板样式的窗口。扩展程序只能看到自己的面板窗口。

“app” 此 API 中已弃用。Chrome 应用窗口。扩展程序只能看到其应用自己的窗口。

表示没有 Chrome 浏览器窗口的 windowId 值。

使用提供的任何可选尺寸、位置或默认网址创建（打开）新的浏览器窗口。

如果值为 true，则打开一个活动窗口。如果值为 false，则打开一个闲置窗口。

新窗口的高度（以像素为单位），包括边框。如果未指定，则默认为自然高度。

新窗口与屏幕左边缘之间的像素数。如果未指定，新窗口会自然地从上次聚焦的窗口偏移。对于面板，此值会被忽略。

如果值为 true，则新创建的窗口的“window.opener”会设置为调用方，并且与调用方位于同一相关浏览上下文单元中。

窗口的初始状态。minimized、maximized 和 fullscreen 状态不能与 left、top、width 或 height 状态组合使用。

新窗口与屏幕上边缘的距离（以像素为单位）。如果未指定，新窗口会自然地从上次聚焦的窗口偏移。对于面板，此值会被忽略。

要在窗口中作为标签页打开的网址或网址数组。完全限定网址必须包含架构，例如 “http://www.google.com”，而不是“www.google.com”。非完全限定网址会被视为扩展程序中的相对网址。默认为“新标签页”。

新窗口的宽度（以像素为单位），包括框架。如果未指定，则默认为自然宽度。

Promise<Window | undefined>

获取最近聚焦的窗口，通常是“最上层”的窗口。

更新窗口的属性。仅指定要更改的属性；未指定的属性保持不变。

如果值为 true，则会导致窗口以吸引用户注意的方式显示，而不会更改聚焦窗口。此效果会一直持续，直到用户将焦点移至相应窗口。如果窗口已获得焦点，此选项不会产生任何影响。设置为 false 可取消之前的 drawAttention 请求。

如果为 true，则将窗口置于前台；不能与“最小化”状态组合使用。如果值为 false，则将 z 顺序中的下一个窗口移到前面；不能与“全屏”或“最大化”状态结合使用。

要将窗口调整为的高度（以像素为单位）。对于面板，此值会被忽略。

窗口要移动到的位置与屏幕左边缘的偏移量（以像素为单位）。对于面板，此值会被忽略。

窗口的新状态。“minimized”“maximized”和“fullscreen”状态不能与“left”“top”“width”或“height”结合使用。

窗口要移动到的位置与屏幕上边缘的偏移量（以像素为单位）。对于面板，此值会被忽略。

要将窗口调整为的宽度（以像素为单位）。对于面板，此值会被忽略。

在窗口调整大小后触发；仅当提交新边界时（而不是在进行中的更改时）才调度此事件。

正在创建的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

在当前聚焦的窗口发生变化时触发。如果所有 Chrome 窗口都已失去焦点，则返回 chrome.windows.WINDOW_ID_NONE。注意：在某些 Linux 窗口管理器中，WINDOW_ID_NONE 始终在从一个 Chrome 窗口切换到另一个 Chrome 窗口之前立即发送。

要移除的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

要移除的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": ["tabs"],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.windows.create(  createData?: object,): Promise<Window | undefined>
```

Example 3 (unknown):
```unknown
chrome.windows.get(  windowId: number,  queryOptions?: QueryOptions,): Promise<Window>
```

Example 4 (unknown):
```unknown
chrome.windows.getAll(  queryOptions?: QueryOptions,): Promise<Window[]>
```

---

## chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/windows

**Contents:**
- chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 当前窗口
- 示例
- 类型
  - CreateType
    - 枚举
  - QueryOptions

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

如果请求了 windows.Window，则该对象包含一个 tabs.Tab 对象数组。如果您需要访问 tabs.Tab 的 url、pendingUrl、title 或 favIconUrl 属性，则必须在清单中声明 "tabs" 权限。例如：

扩展系统中的许多函数都接受一个可选的 windowId 实参，该实参默认为当前窗口。

当前窗口是指包含当前正在执行的代码的窗口。请务必注意，此窗口可能与最上层或聚焦窗口不同。

例如，假设某个扩展程序通过单个 HTML 文件创建了几个标签页或窗口，并且该 HTML 文件包含对 tabs.query() 的调用。当前窗口是指包含发出调用的网页的窗口，无论最顶层的窗口是什么。

对于 service worker，当前窗口的值会回退到上一个有效窗口。在某些情况下，后台网页可能没有当前窗口。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 Windows API 示例。

指定要创建的浏览器窗口的类型。“panel”已被弃用，仅适用于 ChromeOS 上已列入许可名单的现有扩展程序。

如果为 true，则 windows.Window 对象具有 tabs 属性，其中包含 tabs.Tab 对象的列表。仅当扩展程序的清单文件包含 "tabs" 权限时，Tab 对象才包含 url、pendingUrl、title 和 favIconUrl 属性。

WindowTypeWindowType[] 可选

如果已设置，则返回的 windows.Window 会根据其类型进行过滤。如果未设置，则默认过滤器设置为 ['normal', 'popup']。

窗口的高度（包括框架），以像素为单位。在某些情况下，窗口可能未分配 height 属性；例如，当通过 sessions API 查询已关闭的窗口时。

窗口的 ID。窗口 ID 在浏览器会话中是唯一的。在某些情况下，窗口可能未分配 ID 属性；例如，当使用 sessions API 查询窗口时，在这种情况下，可能会存在会话 ID。

窗口与屏幕左边缘的偏移量（以像素为单位）。在某些情况下，窗口可能未分配 left 属性；例如，当通过 sessions API 查询已关闭的窗口时。

用于唯一标识窗口的会话 ID，通过 sessions API 获取。

一个 tabs.Tab 对象数组，表示窗口中的当前标签页。

窗口距离屏幕顶部边缘的偏移量（以像素为单位）。在某些情况下，窗口可能未分配 top 属性；例如，当通过 sessions API 查询已关闭的窗口时。

窗口的宽度（包括边框），以像素为单位。在某些情况下，窗口可能未分配 width 属性；例如，当通过 sessions API 查询已关闭的窗口时。

相应浏览器窗口的状态。在某些情况下，窗口可能未分配 state 属性；例如，当通过 sessions API 查询已关闭的窗口时。

“normal” 正常窗口状态（未最小化、最大化或全屏）。

“locked-fullscreen” 锁定全屏窗口状态。用户无法通过操作退出此全屏状态，并且此状态仅适用于 Chrome 操作系统上已列入许可名单的扩展程序。

相应浏览器窗口的类型。在某些情况下，窗口可能未分配 type 属性；例如，通过 sessions API 查询已关闭的窗口时。

“panel” 此 API 中已弃用。Chrome 应用面板样式的窗口。扩展程序只能看到自己的面板窗口。

“app” 此 API 中已弃用。Chrome 应用窗口。扩展程序只能看到其应用自己的窗口。

表示没有 Chrome 浏览器窗口的 windowId 值。

使用提供的任何可选尺寸、位置或默认网址创建（打开）新的浏览器窗口。

如果值为 true，则打开一个活动窗口。如果值为 false，则打开一个闲置窗口。

新窗口的高度（以像素为单位），包括边框。如果未指定，则默认为自然高度。

新窗口与屏幕左边缘之间的像素数。如果未指定，新窗口会自然地从上次聚焦的窗口偏移。对于面板，此值会被忽略。

如果值为 true，则新创建的窗口的“window.opener”会设置为调用方，并且与调用方位于同一相关浏览上下文单元中。

窗口的初始状态。minimized、maximized 和 fullscreen 状态不能与 left、top、width 或 height 状态组合使用。

新窗口与屏幕上边缘的距离（以像素为单位）。如果未指定，新窗口会自然地从上次聚焦的窗口偏移。对于面板，此值会被忽略。

要在窗口中作为标签页打开的网址或网址数组。完全限定网址必须包含架构，例如 “http://www.google.com”，而不是“www.google.com”。非完全限定网址会被视为扩展程序中的相对网址。默认为“新标签页”。

新窗口的宽度（以像素为单位），包括框架。如果未指定，则默认为自然宽度。

Promise<Window | undefined>

获取最近聚焦的窗口，通常是“最上层”的窗口。

更新窗口的属性。仅指定要更改的属性；未指定的属性保持不变。

如果值为 true，则会导致窗口以吸引用户注意的方式显示，而不会更改聚焦窗口。此效果会一直持续，直到用户将焦点移至相应窗口。如果窗口已获得焦点，此选项不会产生任何影响。设置为 false 可取消之前的 drawAttention 请求。

如果为 true，则将窗口置于前台；不能与“最小化”状态组合使用。如果值为 false，则将 z 顺序中的下一个窗口移到前面；不能与“全屏”或“最大化”状态结合使用。

要将窗口调整为的高度（以像素为单位）。对于面板，此值会被忽略。

窗口要移动到的位置与屏幕左边缘的偏移量（以像素为单位）。对于面板，此值会被忽略。

窗口的新状态。“minimized”“maximized”和“fullscreen”状态不能与“left”“top”“width”或“height”结合使用。

窗口要移动到的位置与屏幕上边缘的偏移量（以像素为单位）。对于面板，此值会被忽略。

要将窗口调整为的宽度（以像素为单位）。对于面板，此值会被忽略。

在窗口调整大小后触发；仅当提交新边界时（而不是在进行中的更改时）才调度此事件。

正在创建的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

在当前聚焦的窗口发生变化时触发。如果所有 Chrome 窗口都已失去焦点，则返回 chrome.windows.WINDOW_ID_NONE。注意：在某些 Linux 窗口管理器中，WINDOW_ID_NONE 始终在从一个 Chrome 窗口切换到另一个 Chrome 窗口之前立即发送。

要移除的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

要移除的窗口类型必须满足的条件。默认情况下，它满足 ['normal', 'popup']。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": ["tabs"],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.windows.create(  createData?: object,): Promise<Window | undefined>
```

Example 3 (unknown):
```unknown
chrome.windows.get(  windowId: number,  queryOptions?: QueryOptions,): Promise<Window>
```

Example 4 (unknown):
```unknown
chrome.windows.getAll(  queryOptions?: QueryOptions,): Promise<Window[]>
```

---

## chrome.system.display 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/display

**Contents:**
- chrome.system.display 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ActiveState
    - 枚举
  - Bounds
    - 属性
  - DisplayLayout
    - 属性

使用 system.display API 查询展示元数据。

一个枚举，用于指示显示屏是否被系统检测到并使用。如果显示屏未被系统检测到（可能已断开连接，或因休眠模式等原因而被视为已断开连接），则会被视为“不活跃”。此状态用于在所有显示屏断开连接时保留现有显示屏，例如。

显示屏沿连接边缘的偏移量。0 表示最上角或最左角对齐。

父显示屏的唯一标识符。如果这是根，则为空。

此显示相对于父级的布局位置。对于根，此属性将被忽略。

显示模式高度（以设备无关的像素为单位，用户可见）。

如果此模式为隔行扫描模式，则为 true；如果未提供，则为 false。

如果模式是显示屏的原生模式，则为 true。

如果当前选择了相应显示模式，则为 true。

显示模式宽度（以设备无关的 [用户可见] 像素为单位）。

如果设置，则更新显示屏沿 x 轴的逻辑边界原点。与 boundsOriginY 一起应用。如果未设置且设置了 boundsOriginY，则默认为当前值。请注意，更新显示原点时，系统会应用一些限制，因此最终的边界原点可能与设置的原点不同。可以使用 getInfo 检索最终边界。无法在主显示屏上更改边界原点。

如果设置，则更新显示屏沿 y 轴的逻辑边界原点。请参阅 boundsOriginX 参数的文档。

如果设置了此值，则将显示模式更新为与此值匹配的模式。如果其他参数无效，则不会应用此参数。如果显示模式无效，系统将不会应用该模式，并会设置错误，但仍会应用其他属性。

如果已设置，则更新与显示屏关联的缩放。此缩放功能会重新布局和重绘，因此与仅执行逐像素拉伸放大相比，可实现更高质量的缩放。

如果设为 true，则将显示屏设为主显示屏。如果设置为 false，则不执行任何操作。注意：如果设置了此属性，则显示屏会被视为所有其他属性的主要显示屏（即，可以设置 isUnified，但可能无法设置边界原点）。

仅限 ChromeOS。如果设置为 true，则将显示模式更改为统一桌面（有关详情，请参阅 enableUnifiedDesktop）。如果此政策设为 false，系统将停用统一桌面模式。此设置仅对主显示屏有效。如果提供了 mirroringSourceId，则不得提供 sourceId，并且系统会忽略其他属性。如果未提供，则不会产生任何影响。

仅限 ChromeOS。如果已设置且不为空，则仅为此显示屏启用镜像。否则，会针对所有显示屏停用镜像功能。此值应指明要镜像的源显示屏的 ID，不得与传递给 setDisplayProperties 的 ID 相同。如果设置了该属性，则不得设置任何其他属性。

如果设置，则将显示屏的过扫描边衬区设置为提供的值。请注意，过扫描值不得为负数，也不得大于屏幕尺寸的一半。无法在内置显示器上更改过扫描。

如果已设置，则更新显示屏的旋转。合法值为 [0, 90, 180, 270]。旋转方向设置为顺时针，相对于显示屏的竖屏位置。

显示屏的当前缩放比例与默认缩放比例之间的比率。例如，值 1 相当于 100% 缩放，值 1.5 相当于 150% 缩放。

注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

如果此显示屏关联了触摸输入设备，则为 True。

如果相应显示处于启用状态，则为 true。

在统一桌面模式下，所有显示屏均为 true。请参阅 enableUnifiedDesktop 的文档。

仅限 ChromeOS。来源显示屏所镜像到的显示屏的标识符。如果未镜像任何显示屏，则为空。所有显示屏的此属性都将设置为相同的值。不得包含 mirroringSourceId。

仅限 ChromeOS。如果启用了镜像，则为正在镜像的显示屏的标识符；否则为空。此设置将应用于所有显示屏（包括正在镜像的显示屏）。

可用显示模式的列表。当前模式的 isSelected 将为 true。仅适用于 ChromeOS。在其他平台上，此属性将设置为一个空数组。

易记名称（例如“HP LCD 显示器”）。

显示屏在其屏幕边界内的边衬区。目前仅在 ChromeOS 上公开。在其他平台上将设置为空边衬区。

显示屏相对于竖屏位置的顺时针旋转角度（以度为单位）。目前仅在 ChromeOS 上公开。在其他平台上将设置为 0。如果值为 -1，则表示当设备处于实体平板电脑状态时，自动旋转屏幕。

显示屏边界内的可用工作区。工作区不包括为操作系统预留的显示区域，例如任务栏和启动器。

3 字符制造商代码。请参阅第 3.4.1 节第 21 页。在 v1.4 中为必需。

2 字节制造商分配的代码，第 3.4.2 节，第 21 页。在 v1.4 中为必需。

制造商年份，第 3.4.4 条，第 22 页。在 v1.4 中为必需。

如果设置为 true，则在统一桌面模式下，getInfo 将仅返回一个 DisplayUnitInfo（请参阅 enableUnifiedDesktop）。默认值为 false。

布局位置，即显示屏所连接到的父元素的边缘。

镜像模式，即显示屏镜像到其他显示屏的不同方式。

“关闭” 指定默认模式（扩展桌面或统一桌面）。

“normal” 指定默认来源显示将镜像到所有其他显示屏。

“混合” 指定将指定的来源显示屏镜像到所提供的目标显示屏。所有其他已连接的显示屏将显示扩展内容。

镜像目标显示屏的 ID。此值仅适用于“混合”。

镜像源显示屏的 ID。此值仅适用于“混合”。

通过清除与显示屏关联的所有触控校准数据，重置显示屏的触控校准并将其恢复为默认状态。

为显示屏设置触控校准对。这些 pairs 将用于校准触摸屏，以在 startCustomTouchCalibration() 中调用 id 时进行显示。请务必在调用此方法之前调用 startCustomTouchCalibration。如果已在进行其他触控校准，则会抛出错误。

TouchCalibrationPairQuad

执行触控校准时的显示屏边界。系统会忽略 bounds.left 和 bounds.top 值。

启用/停用统一桌面功能。如果在镜像处于有效状态时启用，桌面模式将不会更改，直到镜像关闭。否则，桌面模式将立即切换到统一模式。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

请求所有显示屏的布局信息。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

Promise<DisplayLayout[]>

Promise<DisplayUnitInfo[]>

调整显示器的当前过扫描边衬区。通常，这应该会使显示沿某个轴移动（例如，左侧和右侧具有相同的值），或者沿某个轴缩放（例如，顶部和底部具有相反的值）。自开始以来，每次 Adjust 调用都会累积之前调用的结果。

通过保存当前值并隐藏叠加层，完成显示屏的过扫描调整。

将显示屏的过扫描边衬区重置为上次保存的值（即在调用 Start 之前的值）。

为显示屏启动过扫描校准。这会在屏幕上显示一个叠加层，指示当前过扫描边衬区。如果显示屏 id 的过扫描校准正在进行，此方法将重置校准。

为所有显示屏设置布局。未包含的任何显示屏都将使用默认布局。如果布局会重叠或以其他方式无效，系统会将其调整为有效布局。布局解析完毕后，系统会触发 onDisplayChanged 事件。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

布局信息，除主显示屏之外的所有显示屏都需要此信息。

根据 info 中提供的信息，更新 id 指定的显示屏的属性。如果失败，系统会设置 runtime.lastError。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

应更改的显示属性的相关信息。只有当 info 中指定了属性的新值时，该属性才会发生变化。

将显示模式设置为指定的镜像模式。每次调用都会重置之前调用中的状态。对于镜像目标显示屏，调用 setDisplayProperties() 将会失败。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

显示以 id 为显示屏 ID 的显示屏的原生触控校准用户体验。屏幕上会显示一个叠加层，其中包含有关如何继续操作的必要说明。只有在校准成功时才会调用回调。如果校准失败，则会抛出错误。

为显示屏启动自定义触控校准。当使用自定义用户体验来收集校准数据时，应调用此方法。如果已在进行其他触控校准，则会抛出错误。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.display.clearTouchCalibration(  id: string,): void
```

Example 2 (unknown):
```unknown
chrome.system.display.completeCustomTouchCalibration(  pairs: TouchCalibrationPairQuad,  bounds: Bounds,): void
```

Example 3 (unknown):
```unknown
chrome.system.display.enableUnifiedDesktop(  enabled: boolean,): void
```

Example 4 (unknown):
```unknown
chrome.system.display.getDisplayLayout(): Promise<DisplayLayout[]>
```

---

## chrome.printingMetrics 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printingMetrics?hl=zh-cn

**Contents:**
- chrome.printingMetrics 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ColorMode
    - 枚举
  - DuplexMode
    - 枚举
  - MediaSize

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

“BLACK_AND_WHITE” 指定使用了黑白模式。

“ONE_SIDED” 指定使用了单面打印。

"TWO_SIDED_LONG_EDGE" 指定使用了双面打印，并沿长边翻转。

"TWO_SIDED_SHORT_EDGE" 指定使用了双面打印，并沿短边翻转。

供应商提供的 ID，例如“iso_a3_297x420mm”或“na_index-3x5_3x5in”。可能的值是“media”IPP 属性的值，可在 IANA 页面上找到。

打印机的完整路径。包含协议、主机名、端口和队列。

“POLICY” 指定打印机是通过政策添加的。

作业完成时间（自 Unix 纪元以来经过的毫秒数）。

作业创建时间（以毫秒为单位，从 Unix 纪元开始计算）。

来源的 ID。如果来源为 PRINT_PREVIEW 或 ANDROID_APP，则为 null。

“PRINT_PREVIEW” 指定作业是从用户启动的“打印预览”页面创建的。

“ANDROID_APP” 指定作业是从 Android 应用创建的。

“EXTENSION” 指定作业是由扩展程序通过 Chrome API 创建的。

“ISOLATED_WEB_APP” 指定作业是由独立式 Web 应用通过 API 创建的。

“FAILED” 指定打印作业因某些错误而中断。

“CANCELED” 表示打印作业已由用户或通过 API 取消。

“PRINTED” 表示打印作业已完成打印，未出现任何错误。

Promise<PrintJobInfo[]>

打印作业完成时触发的事件。这包括任何终止状态：FAILED、CANCELED 和 PRINTED。

**Examples:**

Example 1 (unknown):
```unknown
chrome.printingMetrics.getPrintJobs(): Promise<PrintJobInfo[]>
```

Example 2 (unknown):
```unknown
chrome.printingMetrics.onPrintJobFinished.addListener(  callback: function,)
```

Example 3 (javascript):
```javascript
(jobInfo: PrintJobInfo) => void
```

---

## chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/alarms?hl=zh-cn

**Contents:**
- chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 设备休眠
  - 持久性
- 示例
  - 设置闹钟
  - 响应闹钟
- 类型

使用 chrome.alarms API 可安排代码在指定时间或未来某个时间定期运行。

如需使用 chrome.alarms API，请在清单中声明 "alarms" 权限：

为确保可靠的行为，了解 API 的行为方式很有帮助。

设备处于休眠状态时，闹钟会继续运行。不过，闹钟不会唤醒设备。当设备唤醒时，所有错过的闹钟都会响铃。 重复闹钟最多会响一次，然后会根据指定周期重新安排闹钟，从设备唤醒时开始计时，不考虑自最初设置闹钟运行以来已经过去的时间。

警报通常会一直存在，直到扩展程序更新为止。不过，这无法保证，并且在浏览器重启时闹钟可能会被清除。因此，请确保每次服务工作线程启动时，该变量都存在。例如：

以下示例展示了如何使用闹钟以及如何响应闹钟。如需试用此 API，请从 chrome-extension-samples 代码库中安装 Alarm API 示例。

以下示例展示了如何在安装扩展程序时在 service worker 中设置闹钟：

以下示例根据响铃闹钟的名称设置操作工具栏图标。

如果不为 null，则表示闹钟为重复闹钟，将在 periodInMinutes 分钟后再次响铃。

相应闹钟预定触发的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。出于性能方面的考虑，闹钟可能会延迟任意时长。

在多长时间（以分钟为单位）后应触发 onAlarm 事件。

如果设置了该值，则在 when 或 delayInMinutes 指定的初始事件之后，每隔 periodInMinutes 分钟应触发一次 onAlarm 事件。如果未设置，闹钟将仅响铃一次。

闹钟应响铃的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。

创建闹钟。在 alarmInfo 指定的时间附近，系统会触发 onAlarm 事件。如果存在另一个同名（或未指定名称时为无名称）的闹钟，则该闹钟将被取消并替换为此闹钟。

为了减轻用户机器的负载，Chrome 将闹钟限制为最多每 30 秒触发一次，但可能会将闹钟延迟任意时长。也就是说，如果将 delayInMinutes 或 periodInMinutes 设置为小于 0.5 的值，系统将不会接受该值，并会发出警告。when 可以设置为“现在”之后的不到 30 秒，系统不会发出警告，但实际上至少要过 30 秒才会触发闹钟。

为了帮助您调试应用或扩展程序，当您以未打包的形式加载应用或扩展程序时，闹钟的触发频率不受限制。

用于标识相应闹钟的可选名称。默认为空字符串。

描述闹钟应在何时响铃。必须通过 when 或 delayInMinutes（但不能同时通过两者）指定初始时间。如果设置了 periodInMinutes，闹钟会在初始事件发生后每隔 periodInMinutes 分钟重复一次。如果未为重复闹钟设置 when 或 delayInMinutes，则 periodInMinutes 会用作 delayInMinutes 的默认值。

Promise<Alarm | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "alarms"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
async function checkAlarmState() {
  const alarm = await chrome.alarms.get("my-alarm");

  if (!alarm) {
    await chrome.alarms.create("my-alarm", { periodInMinutes: 1 });
  }
}

checkAlarmState();
```

Example 3 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(async ({ reason }) => {
  if (reason !== 'install') {
    return;
  }

  // Create an alarm so we have something to look at in the demo
  await chrome.alarms.create('demo-default-alarm', {
    delayInMinutes: 1,
    periodInMinutes: 1
  });
});
```

Example 4 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  chrome.action.setIcon({
    path: getIconPath(alarm.name),
  });
});
```

---

## chrome.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/platformKeys?hl=zh-cn

**Contents:**
- chrome.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ClientCertificateRequest
    - 属性
  - ClientCertificateType
    - 枚举
  - Match

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

服务器允许的证书授权机构的标识名列表。每个条目都必须是 DER 编码的 X.509 DistinguishedName。

ClientCertificateType[]

此字段是所请求证书类型的列表，按服务器的偏好排序。系统只会检索此列表中包含的类型的证书。不过，如果 certificateTypes 是空列表，则会返回任何类型的证书。

经过认证的密钥的 KeyAlgorithm。这包含证书密钥固有的算法参数（例如密钥长度）。其他参数（例如 sign 函数使用的哈希函数）未包含在内。

如果指定，则 selectClientCertificates 会对该列表进行操作。否则，从平台可供此扩展程序使用的证书存储区中获取所有证书的列表。系统会移除扩展程序无权访问或与请求不匹配的条目。

如果为 true，系统会向用户显示过滤后的列表，以便用户手动选择证书，从而授予扩展程序对证书和密钥的访问权限。系统只会返回所选证书。如果为 false，则列表会缩减为扩展程序已获得访问权限（自动或手动）的所有证书。

ClientCertificateRequest

要验证证书的服务器的主机名，例如提供 serverCertificateChain 的服务器。

每个链条条目都必须是 X.509 证书的 DER 编码，第一个条目必须是服务器证书，并且每个条目都必须证明其前面的条目。

如果信任验证失败，此数组会包含底层网络层报告的错误。否则，此数组为空。

注意：此列表仅用于调试，可能未包含所有相关错误。返回的错误可能会在此 API 的未来修订版本中发生变化，并且无法保证向前或向后兼容。

信任验证的结果：如果能够建立对指定验证详细信息的信任，则为 true；如果因任何原因拒绝信任，则为 false。

将 certificate 的密钥对传递给 callback，以便与 platformKeys.subtleCrypto 搭配使用。

由 selectClientCertificates 返回的 Match 的证书。

除了密钥本身固定的参数之外，还确定签名/哈希算法参数。接受与 WebCrypto 的 importKey 函数相同的参数，例如 RSASSA-PKCS1-v1_5 密钥的 RsaHashedImportParams 和 EC 密钥的 EcKeyImportParams。此外，对于 RSASSA-PKCS1-v1_5 密钥，可以使用以下值之一指定哈希算法名称参数：“none”“SHA-1”“SHA-256”“SHA-384”或“SHA-512”，例如 {"hash": { "name": "none" } }。然后，签名函数将应用 PKCS#1 v1.5 填充，但不会对指定数据进行哈希处理。

目前，此方法仅支持“RSASSA-PKCS1-v1_5”和“ECDSA”算法。

如果相应扩展程序无权访问该属性，则可能为 null。

将 publicKeySpkiDer 标识的密钥对传递给 callback，以供 platformKeys.subtleCrypto 使用。

以 DER 编码的 X.509 SubjectPublicKeyInfo，例如通过调用 WebCrypto 的 exportKey 函数并指定 format="spki" 来获取。

除了密钥本身固定的参数之外，还提供签名和哈希算法参数。接受与 WebCrypto 的 importKey 函数相同的参数，例如 RSASSA-PKCS1-v1_5 密钥的 RsaHashedImportParams。对于 RSASSA-PKCS1-v1_5 密钥，我们还需要传递一个“哈希”参数 { "hash": { "name": string } }。“hash”参数表示在签名之前用于摘要操作的哈希算法的名称。您可以将“none”作为哈希名称进行传递，在这种情况下，签名函数将应用 PKCS#1 v1.5 填充，但不会对指定数据进行哈希处理。

目前，此方法支持以下算法：“ECDSA”算法（采用命名曲线 P-256）和“RSASSA-PKCS1-v1_5”算法（采用哈希算法“none”“SHA-1”“SHA-256”“SHA-384”和“SHA-512”之一）。

如果相应扩展程序无权访问该属性，则可能为 null。

此方法会从客户端证书列表中过滤出平台已知的、与 request 匹配的证书，以及扩展程序有权访问这些证书及其私钥的证书。如果 interactive 为 true，系统会向用户显示一个对话框，用户可以在其中选择匹配的证书，并授予扩展程序对该证书的访问权限。所选/过滤的客户端证书将传递给 callback。

WebCrypto 的 SubtleCrypto 的一种实现，允许对可供此扩展程序使用的客户端证书的密钥执行加密操作。

根据平台的信任设置，检查 details.serverCertificateChain 是否可信，以用于 details.hostname。注意：信任验证的实际行为并未完全指定，未来可能会发生变化。API 实现会验证证书失效情况、验证证书路径，并通过已知 CA 检查信任情况。该实现应遵循 EKU serverAuth 并支持主题备用名称。

Promise<VerificationResult>

**Examples:**

Example 1 (unknown):
```unknown
chrome.platformKeys.getKeyPair(  certificate: ArrayBuffer,  parameters: object,  callback: function,): void
```

Example 2 (javascript):
```javascript
(publicKey: object, privateKey?: object) => void
```

Example 3 (unknown):
```unknown
chrome.platformKeys.getKeyPairBySpki(  publicKeySpkiDer: ArrayBuffer,  parameters: object,  callback: function,): void
```

Example 4 (javascript):
```javascript
(publicKey: object, privateKey?: object) => void
```

---

## chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/dns?hl=zh-cn

**Contents:**
- chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 用法
- 类型
  - ResolveCallbackResolveInfo
    - 属性
- 方法
  - resolve()

使用 chrome.dns API 进行 DNS 解析。

如需使用此 API，您必须在清单中声明 "dns" 权限。

以下代码调用 resolve() 以检索 example.com 的 IP 地址。

表示 IP 地址字面值的字符串。仅当 resultCode 指示成功时才提供。

Promise<ResolveCallbackResolveInfo>

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
chrome.dns.resolve(  hostname: string,): Promise<ResolveCallbackResolveInfo>
```

---

## chrome.tts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tts

**Contents:**
- chrome.tts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 生成语音
  - 监听事件
  - SSML 标记
  - 选择一种语音
- 类型
  - EventType

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

Chrome 在 Windows（使用 SAPI 5）、Mac OS X 和 ChromeOS 上提供此功能，使用操作系统提供的语音合成功能。在所有平台上，用户都可以安装将自己注册为替代语音引擎的扩展程序。

从扩展程序调用 speak() 以进行语音对话。例如：

如需立即停止朗读，只需调用 stop()：

您可以提供用于控制语音各种属性（例如语速、音高等）的选项。例如：

最好还指定语言，以便选择支持该语言（以及地区方言，如果适用）的合成器。

默认情况下，每次调用 speak() 都会中断任何正在进行的语音并立即发声。如需确定通话是否会中断任何内容，您可以调用 isSpeaking()。此外，您还可以使用 enqueue 选项将此话语添加到话语队列中，以便在当前话语说完后说出此话语。

如需查看所有选项的完整说明，请参阅 tts.speak()。并非所有语音引擎都支持所有选项。

为了捕获错误并确保您正确调用 speak()，请传递一个不带任何实参的回调函数。在回调内部，检查 runtime.lastError 以查看是否存在任何错误。

回调会立即返回，在引擎开始生成语音之前。回调的目的是提醒您在使用 TTS API 时出现的语法错误，而不是捕获在合成和输出语音过程中可能发生的所有错误。如需捕获这些错误，您还需要使用下一部分中介绍的事件监听器。

如需获取有关合成语音状态的更多实时信息，请在选项中向 speak() 传递事件监听器，如下所示：

每个事件都包含事件类型、当前语音相对于话语的字符索引，以及（对于错误事件）可选的错误消息。事件类型包括：

有四种事件类型（'end'、'interrupted'、'cancelled' 和 'error'）是最终事件类型。收到上述任一事件后，此话语将不再发声，并且不会再收到来自此话语的新事件。

某些语音可能不支持所有事件类型，而某些语音可能根本不会发送任何事件。如果您不希望使用语音，除非它发送某些事件，请在选项对象的 requiredEventTypes 成员中传递所需的事件，或使用 getVoices() 选择符合您要求的语音。下文将介绍这两种方法。

此 API 中使用的发音可能包含使用语音合成标记语言 (SSML) 的标记。如果您使用 SSML，则 speak() 的第一个实参应为包含 XML 标头和顶级 <speak> 标记的完整 SSML 文档，而不是文档片段。

并非所有语音引擎都支持所有 SSML 标记，有些可能根本不支持 SSML，但所有引擎都必须忽略它们不支持的任何 SSML，并仍能朗读基础文本。

默认情况下，Chrome 会根据语言为要朗读的每个话语选择最合适的语音。在大多数 Windows、Mac OS X 和 ChromeOS 系统上，操作系统提供的语音合成功能应该能够以至少一种语言朗读任何文本。不过，某些用户可能可以使用来自操作系统和由其他 Chrome 扩展程序实现的语音引擎的各种语音。在这些情况下，您可以实现自定义代码来选择合适的语音，或者向用户显示选择列表。

如需获取所有语音的列表，请调用 getVoices() 并向其传递一个以 TtsVoice 对象数组作为实参的函数：

来自 TTS 引擎的事件，用于传达朗读的状态。

话语中当前字符的索引。对于字词事件，该事件会在一个字词结束时触发，并在下一个字词开始之前触发。charIndex 表示文本中下一个要朗读的字词的开头位置。

如果事件类型为 error，则为错误说明。

话语下一部分的长度。例如，在 word 事件中，这是接下来要朗读的字词的长度。如果语音引擎未设置此值，则会将其设置为 -1。

类型可以是 start（语音开始后立即）、word（到达字词边界时）、sentence（到达句子边界时）、marker（到达 SSML mark 元素时）、end（到达话语末尾时）、interrupted（在到达末尾之前停止或中断话语时）、cancelled（在合成之前从队列中移除时）或 error（发生任何其他错误时）。暂停语音时，如果特定话语在中间暂停，则会触发 pause 事件；如果话语恢复语音，则会触发 resume 事件。请注意，如果在话语之间暂停语音，可能不会触发暂停和恢复事件。

您感兴趣的要监听的 TTS 事件类型。如果缺少此参数，则可能会发送所有事件类型。

如果为 true，则在 TTS 正在进行时将此话语加入队列。如果为 false（默认值），则在说出此新话语之前，会中断任何当前语音并清空语音队列。

要使用的语音引擎的扩展程序 ID（如果已知）。

用于合成的语言，格式为语言-地区。示例：“en”“en-US”“en-GB”“zh-CN”。

说话音调介于 0 到 2 之间（含），其中 0 为最低，2 为最高。1.0 对应于语音的默认音高。

相对于此语音的默认语速的语速。1.0 是默认速率，通常约为每分钟 180 到 220 个字。2.0 表示快一倍的速度，0.5 则表示原有速度的一半。严格禁止使用低于 0.1 或高于 10.0 的值，但许多语音会进一步限制最低和最高速率，例如，即使您指定的值大于 3.0，特定语音实际上也可能不会以超过正常速度 3 倍的速度说话。

要用于合成的语音的名称。如果为空，则使用任何可用的声音。

说话音量，介于 0 到 1 之间（含 0 和 1），其中 0 为最低音量，1 为最高音量，默认值为 1.0。

此函数会随说出话语的过程中发生的事件一起调用。

来自文字转语音引擎的更新事件，用于指示相应朗读的状态。

EventTypeEventType[] 可选

相应语音支持的语言，格式为 language-region。示例：“en”“en-US”“en-GB”“zh-CN”。

如果为 true，则表示合成引擎是远程网络资源。延迟时间可能会更长，并且可能会产生带宽费用。

检查引擎当前是否正在说话。在 Mac OS X 上，只要系统语音引擎正在说话，结果就为 true，即使语音不是由 Chrome 发起的也是如此。

暂停语音合成，可能会在话语中间暂停。调用以恢复或停止将取消暂停语音。

如果语音之前处于暂停状态，则从上次中断的位置继续朗读。

要朗读的文本，可以是纯文本，也可以是完整且格式正确的 SSML 文档。不支持 SSML 的语音引擎会去除标记并朗读文本。文本的长度上限为 32,768 个字符。

停止任何当前语音，并清空所有待处理话语的队列。此外，如果之前暂停了语音，现在会取消暂停，以便在下次调用 speak 时继续朗读。

当 getVoices 将返回的 tts.TtsVoice 列表发生变化时调用。

**Examples:**

Example 1 (unknown):
```unknown
chrome.tts.speak('Hello, world.');
```

Example 2 (unknown):
```unknown
chrome.tts.stop();
```

Example 3 (unknown):
```unknown
chrome.tts.speak('Hello, world.', {'rate': 2.0});
```

Example 4 (unknown):
```unknown
chrome.tts.speak('Hello, world.', {'lang': 'en-US', 'rate': 2.0});
```

---

## chrome.input.ime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/input/ime

**Contents:**
- chrome.input.ime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
- 类型
  - AssistiveWindowButton
    - 枚举
  - AssistiveWindowProperties
    - 属性

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

您必须在扩展程序清单中声明“input”权限，才能使用 input.ime API。例如：

以下代码创建了一个将输入的字母转换为大写的 IME。

设置为 true 可显示 AssistiveWindow，设置为 false 可隐藏。

用于指定文本字段操作的目标。一旦调用 onBlur，此 ID 就会失效。

是否应使用输入到文本字段中的文本来改进用户的输入建议。

相应文本字段所编辑的值的类型（文本、数字、网址等）

相应文本字段所编辑的值的类型（文本、数字、网址等）

请参阅 http://www.w3.org/TR/DOM-Level-3-Events/#events-KeyboardEvent

所按实体键的值。该值不受当前键盘布局或修饰键状态的影响。

已弃用的 HTML keyCode，这是一个与所按键相关联的未修改标识符的数值代码，具体取决于系统和实现。

（已弃用）请求的 ID。请改用 onKeyEvent 事件中的 requestId 参数。

输入法使用的一种菜单项，用于通过语言菜单与用户互动。

将传递给引用此 MenuItem 的回调的字符串。

菜单项的类型。分隔符之间的单选按钮被视为一组。

要添加或更新的 MenuItem。它们将按在数组中的顺序添加。

候选字词窗口的显示位置。如果设置为“cursor”，窗口会跟随光标。如果设置为“composition”，则窗口锁定到合成的开头。

清除当前乐曲。如果此扩展服务不拥有有效的 IME，则会失败。

从光标位置开始删除的偏移量。此值可以为负数。

隐藏由系统自动弹出的输入视图窗口。如果输入视图窗口已隐藏，此函数将不执行任何操作。

表示 onKeyEvent 收到的按键事件已得到处理。仅当 onKeyEvent 监听器为异步时才应调用此方法。

已处理的事件的请求 ID。此值应来自 keyEvent.requestId

如果按键操作已处理，则为 true；否则为 false

发送按键事件。此函数预计将由虚拟键盘使用。当用户按下虚拟键盘上的某个键时，此函数用于将该事件传播到系统。

将发送按键事件的上下文的 ID，如果为零，则将按键事件发送到非输入字段。

AssistiveWindowButton

AssistiveWindowProperties

设置当前候选字词列表。如果此扩展程序不拥有有效的 IME，则此方法会失败

显示在候选对象旁边的短字符串，通常是快捷键或索引

设置候选窗口的属性。如果扩展程序不拥有活跃的 IME，则此方法会失败

如果为 true，则显示辅助文本；如果为 false，则隐藏辅助文本。

设置为 true 可显示光标，设置为 false 可隐藏光标。

如果候选窗口应垂直呈现，则为 True；如果应水平呈现，则为 False。

如果为 true，则显示候选字窗口；如果为 false，则隐藏候选字窗口。

设置当前合成。如果此扩展服务不拥有有效的 IME，则会失败。

设置候选字窗口中光标的位置。如果此扩展程序不拥有有效的 IME，则此方法不执行任何操作。

当此 IME 处于活动状态时，将提供的菜单项添加到语言菜单。

此事件在 IME 处于活动状态时发送。它表示 IME 将接收 onKeyPress 事件。

当辅助窗口中的按钮被点击时，系统会发送此事件。

AssistiveWindowButton

此事件在焦点离开文本框时发送。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

如果此扩展程序拥有有效的 IME，则会发送此事件。

此事件在 IME 被停用时发送。表示 IME 将不再接收 onKeyPress 事件。

当焦点进入文本框时，系统会发送此事件。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

当当前 InputContext 的属性（例如类型）发生更改时，系统会发送此事件。它会发送给所有正在监听此事件且已由用户启用的扩展程序。

当操作系统发送按键事件时触发。如果扩展程序拥有有效的 IME，则事件将发送到该扩展程序。如果事件已处理，监听器函数应返回 true；如果未处理，则应返回 false。如果事件将异步评估，则此函数必须返回未定义的值，并且 IME 必须稍后使用结果调用 keyEventHandled()。

当 Chrome 终止正在进行的文本输入会话时，系统会发送此事件。

当插入符号周围的可编辑字符串发生变化或插入符号位置发生变化时调用。每个来回方向的文字长度上限为 100 个字符。

所选内容的起始位置。此值表示光标位置（如果没有选择内容）。

所选内容的结束位置。此值表示光标位置（如果没有选择内容）。

text 的偏移位置。由于 text 仅包含光标周围的部分文本，因此 offset 表示 text 的第一个字符的绝对位置。

光标周围的文本。这只是输入字段中所有文本的一部分。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "input"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var context_id = -1;

chrome.input.ime.onFocus.addListener(function(context) {
  context_id = context.contextID;
});

chrome.input.ime.onKeyEvent.addListener(
  function(engineID, keyData) {
    if (keyData.type == "keydown" && keyData.key.match(/^[a-z]$/)) {
      chrome.input.ime.commitText({"contextID": context_id,
                                    "text": keyData.key.toUpperCase()});
      return true;
    } else {
      return false;
    }
  }
);
```

Example 3 (unknown):
```unknown
chrome.input.ime.clearComposition(  parameters: object,): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.input.ime.commitText(  parameters: object,): Promise<boolean>
```

---

## chrome.tabGroups 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabGroups

**Contents:**
- chrome.tabGroups 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Color
    - 枚举
  - TabGroup
    - 属性
- 属性

使用 chrome.tabGroups API 与浏览器的标签页分组系统进行交互。您可以使用此 API 修改和重新排列浏览器中的标签页组。如需对标签页进行分组和取消分组，或查询哪些标签页位于分组中，请使用 chrome.tabs API。

群组是否已收起。收起的群组是指标签页处于隐藏状态的群组。

群组的 ID。组 ID 在浏览器会话中是唯一的。

将相应标签页组及其窗口中的所有标签页移至新窗口。

要将群组移至的位置。使用 -1 将群组放置在窗口末尾。

要将群组移至的窗口。默认为群组当前所在的窗口。请注意，群组只能在 windows.WindowType 类型为 "normal" 的窗口之间移动。

Promise<TabGroup | undefined>

获取具有指定属性的所有群组，如果未指定任何属性，则获取所有群组。

父窗口的 ID，或windows.WINDOW_ID_CURRENT（表示当前窗口）。

修改群组的属性。不会修改未在 updateProperties 中指定的属性。

Promise<TabGroup | undefined>

当群组在窗口内移动时触发。系统仍会针对群组中的各个标签页以及群组本身触发移动事件。当群组在窗口之间移动时，不会触发此事件；相反，系统会从一个窗口中移除该群组，并在另一个窗口中创建该群组。

当群组关闭时触发，无论是用户直接关闭还是因群组中不包含任何标签页而自动关闭。

**Examples:**

Example 1 (unknown):
```unknown
chrome.tabGroups.get(  groupId: number,): Promise<TabGroup>
```

Example 2 (unknown):
```unknown
chrome.tabGroups.move(  groupId: number,  moveProperties: object,): Promise<TabGroup | undefined>
```

Example 3 (unknown):
```unknown
chrome.tabGroups.query(  queryInfo: object,): Promise<TabGroup[]>
```

Example 4 (unknown):
```unknown
chrome.tabGroups.update(  groupId: number,  updateProperties: object,): Promise<TabGroup | undefined>
```

---

## chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/network

**Contents:**
- chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - Request
    - 属性
- 方法
  - getHAR()
    - 参数

使用 chrome.devtools.network API 检索由开发者工具在“Network”面板中显示的网络请求的相关信息。

网络请求信息以 HTTP 归档格式 (HAR) 表示。以下各项的说明： HAR 不在本文档的讨论范围内，请参阅 HAR v1.2 规范。

对于 HAR，chrome.devtools.network.getHAR() 方法会返回整个 HAR 日志，而 chrome.devtools.network.onRequestFinished 事件提供 HAR 条目作为事件的参数 回调。

请注意，出于效率方面的原因，请求内容未包含在 HAR 中。您可以拨打 请求的 getContent() 方法来检索内容。

如果在网页加载后打开“开发者工具”窗口， 由 getHAR() 返回的条目数组。请重新加载页面以获取所有请求。一般来说， getHAR() 返回的请求列表应与“Network”面板中显示的请求列表一致。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

必须在清单中声明以下键才能使用此 API。

以下代码会在加载时记录所有超过 40KB 的图片的网址：

若要试用此 API，请安装 chrome-extension-samples 中的 chrome-extension-samples 存储库

表示对文档资源（脚本、图片等）的网络请求。有关参考信息，请参阅 HAR 规范。

如果内容未经编码，则为空，否则为名称编码。目前只支持 base64。

返回包含所有已知网络请求的 HAR 日志。

HAR 日志。如需了解详情，请参阅 HAR 规范。

在网络请求完成且所有请求数据都可用时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.network.onRequestFinished.addListener(
  function(request) {
    if (request.response.bodySize > 40*1024) {
      chrome.devtools.inspectedWindow.eval(
          'console.log("Large image: " + unescape("' +
          escape(request.request.url) + '"))');
    }
  }
);
```

Example 2 (javascript):
```javascript
(callback: function) => {...}
```

Example 3 (javascript):
```javascript
(content: string, encoding: string) => void
```

Example 4 (unknown):
```unknown
chrome.devtools.network.getHAR(  callback: function,): void
```

---

## chrome.tabCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabCapture?hl=zh-cn

**Contents:**
- chrome.tabCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 保留系统音频
  - 数据流 ID
  - 使用限制
  - 了解详情
- 类型
  - CaptureInfo

使用 chrome.tabCapture API 与标签页媒体流进行互动。

借助 chrome.tabCapture API，您可以访问包含当前标签页的视频和音频的 MediaStream。只有在用户调用扩展程序后（例如通过点击扩展程序的操作按钮），才能调用此方法。这类似于 "activeTab" 权限的行为。

当标签页获得 MediaStream 时，该标签页中的音频将不再向用户播放。这类似于当 suppressLocalAudioPlayback 标志设为 true 时 getDisplayMedia() 函数的行为。

这会创建一个新的 AudioContext，并将标签页 MediaStream 的音频连接到默认目的地。

调用 chrome.tabCapture.getMediaStreamId() 将返回一个流 ID。如需稍后通过 ID 访问 MediaStream，请使用以下代码：

调用 getMediaStreamId() 后，返回的流 ID 的使用范围会受到限制：

在 Chrome 116 之前，如果未指定 consumerTabId，则流 ID 会同时受调用方的安全来源、渲染进程和渲染框架的限制。

如需详细了解如何使用 chrome.tabCapture API，请参阅音频录制和屏幕捕获。此示例演示了如何使用 tabCapture 及相关 API 来解决一些常见用例。

MediaStreamConstraint 可选

MediaStreamConstraint 可选

稍后将调用 getUserMedia() 来使用该流的标签页的可选标签页 ID。如果未指定，则生成的流只能由调用扩展程序使用。该数据流只能由给定标签页中安全来源与消费者标签页来源相匹配的框架使用。标签页的来源必须是安全来源，例如 HTTPS。

要捕获的标签页的可选标签页 ID。如果未指定，则选择当前活动标签页。只有扩展程序已获得 activeTab 权限的标签页才能用作目标标签页。

捕获当前活动标签页的可见区域。只有在扩展程序被调用后，才能在当前活跃标签页上开始捕获，这与 activeTab 的工作方式类似。在标签页内进行网页导航时，捕获会一直保持，直到标签页关闭或扩展程序关闭媒体流时才会停止。

返回已请求捕获或正在捕获的标签页的列表，即状态不为“已停止”且状态不为“错误”的标签页。这样一来，扩展程序就可以告知用户当前存在标签页捕获，这会阻止新的标签页捕获成功完成（或防止对同一标签页发出冗余请求）。

Promise<CaptureInfo[]>

创建用于捕获目标标签页的流 ID。与 chrome.tabCapture.capture() 方法类似，但会向消费者标签页返回媒体流 ID，而不是媒体流。

GetMediaStreamOptions 可选

当标签页的捕获状态发生变化时触发的事件。这样，扩展程序作者就可以跟踪标签页的捕获状态，以使界面元素（例如网页操作）保持同步。

**Examples:**

Example 1 (javascript):
```javascript
const output = new AudioContext();
const source = output.createMediaStreamSource(stream);
source.connect(output.destination);
```

Example 2 (unknown):
```unknown
navigator.mediaDevices.getUserMedia({
  audio: {
    mandatory: {
      chromeMediaSource: "tab",
      chromeMediaSourceId: id,
    },
  },
  video: {
    mandatory: {
      chromeMediaSource: "tab",
      chromeMediaSourceId: id,
    },
  },
});
```

Example 3 (unknown):
```unknown
chrome.tabCapture.capture(  options: CaptureOptions,  callback: function,): void
```

Example 4 (javascript):
```javascript
(stream: LocalMediaStream) => void
```

---

## chrome.webAuthenticationProxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webAuthenticationProxy?hl=zh-cn

**Contents:**
- chrome.webAuthenticationProxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - CreateRequest
    - 属性
  - CreateResponseDetails
    - 属性
  - DOMExceptionDetails

借助 chrome.webAuthenticationProxy API，在远程主机上运行的远程桌面软件可以拦截 Web 身份验证 API (WebAuthn) 请求，以便在本地客户端上处理这些请求。

传递给 navigator.credentials.create() 的 PublicKeyCredentialCreationOptions，序列化为 JSON 字符串。序列化格式与 PublicKeyCredential.parseCreationOptionsFromJSON() 兼容。

DOMExceptionDetails 可选

远程请求产生的 DOMException（如果有）。

CreateRequest 的 requestId。

远程请求生成的 PublicKeyCredential（如果有），通过调用 href="https://w3c.github.io/webauthn/#dom-publickeycredential-tojson"> PublicKeyCredential.toJSON() 序列化为 JSON 字符串。

传递给 navigator.credentials.get() 的 PublicKeyCredentialRequestOptions，序列化为 JSON 字符串。序列化格式与 PublicKeyCredential.parseRequestOptionsFromJSON() 兼容。

DOMExceptionDetails 可选

远程请求产生的 DOMException（如果有）。

CreateRequest 的 requestId。

远程请求生成的 PublicKeyCredential（如果有），通过调用 href="https://w3c.github.io/webauthn/#dom-publickeycredential-tojson"> PublicKeyCredential.toJSON() 序列化为 JSON 字符串。

使此扩展程序成为有效的 Web 身份验证 API 请求代理。

远程桌面扩展程序通常会在检测到远程会话附加到此主机后调用此方法。一旦此方法在未出错的情况下返回，系统就会暂停对 WebAuthn 请求的常规处理，并引发来自此扩展 API 的事件。

如果已附加其他扩展服务，此方法会因错误而失败。

附加的扩展程序必须在远程桌面会话结束后调用 detach()，以便恢复常规 WebAuthn 请求处理。如果扩展程序被卸载，则会自动变为分离状态。

请参阅 onRemoteSessionStateChange 事件，了解如何将远程会话附加从原生应用更改为（可能已暂停的）扩展程序。

Promise<string | undefined>

报告 navigator.credentials.create() 调用的结果。扩展程序必须针对收到的每个 onCreateRequest 事件调用此方法，除非请求已取消（在这种情况下，系统会触发 onRequestCanceled 事件）。

CreateResponseDetails

报告 navigator.credentials.get() 调用的结果。扩展程序必须针对收到的每个 onGetRequest 事件调用此方法，除非请求已取消（在这种情况下，系统会触发 onRequestCanceled 事件）。

报告 PublicKeyCredential.isUserVerifyingPlatformAuthenticator() 调用的结果。扩展程序必须针对收到的每个 onIsUvpaaRequest 事件调用此方法。

IsUvpaaResponseDetails

移除此扩展程序，使其不再作为有效的 Web 身份验证 API 请求代理。

当扩展程序检测到远程桌面会话已终止时，通常会调用此方法。此方法返回后，扩展程序将不再是有效的 Web 身份验证 API 请求代理。

请参阅 onRemoteSessionStateChange 事件，了解如何将远程会话附加从原生应用更改为（可能已暂停的）扩展程序。

Promise<string | undefined>

在发生 WebAuthn navigator.credentials.create() 调用时触发。扩展程序必须通过调用 completeCreateRequest() 并使用 requestInfo 中的 requestId 来提供响应。

在发生 WebAuthn navigator.credentials.get() 调用时触发。扩展程序必须通过调用 completeGetRequest() 并使用 requestInfo 中的 requestId 来提供响应

在发生 PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable() 调用时触发。扩展程序必须通过调用 completeIsUvpaaRequest() 并使用 requestInfo 中的 requestId 来提供响应

与此扩展程序关联的原生应用可以通过以下方式触发此事件：在默认用户数据目录内的名为 WebAuthenticationProxyRemoteSessionStateChange 的目录中写入名称等于扩展程序 ID 的文件

文件内容应为空。也就是说，无需更改文件内容即可触发此事件。

原生宿主应用可以使用此事件机制来指示可能发生的远程会话状态变化（即从分离到附加，或从附加到分离），而扩展程序服务工作线程可能处于暂停状态。在此事件的处理程序中，扩展程序可以相应地调用 attach() 或 detach() API 方法。

当 onCreateRequest 或 onGetRequest 事件被取消时（因为 WebAuthn 请求被调用方中止，或者因为超时）触发。当收到此事件时，扩展程序应取消在客户端上对相应请求的处理。扩展服务在请求取消后无法完成该请求。

**Examples:**

Example 1 (unknown):
```unknown
chrome.webAuthenticationProxy.attach(): Promise<string | undefined>
```

Example 2 (unknown):
```unknown
chrome.webAuthenticationProxy.completeCreateRequest(  details: CreateResponseDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.webAuthenticationProxy.completeGetRequest(  details: GetResponseDetails,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.webAuthenticationProxy.completeIsUvpaaRequest(  details: IsUvpaaResponseDetails,): Promise<void>
```

---

## chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/recorder?hl=zh-cn

**Contents:**
- chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 概念和用法
  - 自定义导出功能
  - 自定义重放按钮
- 示例
  - 导出插件
  - 重放插件
- 类型

使用 chrome.devtools.recorder API 自定义开发者工具中的“Recorder”面板。

devtools.recorder API 是一项预览版功能，可让您扩展 Chrome 开发者工具中的 Recorder 面板。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

如需注册扩展插件，请使用 registerRecorderExtensionPlugin 函数。此函数需要插件实例、name 和 mediaType 作为参数。插件实例必须实现两种方法：stringify 和 stringifyStep。

该扩展程序提供的 name 会显示在 Recorder 面板的 Export 菜单中。

根据用户的导出环境，当用户点击该扩展程序提供的导出选项时， Recorder 面板会调用以下两个函数之一：

mediaType 参数允许该扩展程序指定其使用 stringify 和 stringifyStep 函数。例如，如果结果是 JavaScript，则返回 application/javascript 计划。

如需在 Recorder 中自定义“重放”按钮，请使用 registerRecorderExtensionPlugin 函数。插件必须实现 replay 方法，自定义设置才能生效。 如果检测到该方法，Recorder 中会显示重放按钮。 点击此按钮后，系统会将当前录制对象作为第一个参数传递给 replay 方法。

此时，该扩展程序可以显示用于处理重放的 RecorderView，或使用其他扩展程序 API 来处理重放请求。如需创建新的 RecorderView，请调用 chrome.devtools.recorder.createView。

以下代码会实现一个扩展程序插件，该插件会使用 JSON.stringify 将录制转换为字符串：

以下代码会实现一个扩展程序插件，该插件会创建虚拟录音机视图并在收到重放请求时显示该视图：

在 GitHub 上查找完整的扩展程序示例。

“Recorder”面板调用以自定义“Recorder”面板的插件接口。

用户与网页互动的记录。这应与 Puppeteer 的录制架构匹配。

将录音从“Recorder”面板格式转换为字符串。

用户与网页互动的记录。这应与 Puppeteer 的录制架构匹配。

将录音步骤从“Recorder”面板格式转换为字符串。

stringifyStep 函数如下所示：

记录用户与网页互动的步骤。此架构应与 Puppeteer 的步骤架构匹配。

表示扩展程序创建的要嵌入“Recorder”面板的视图。

onHidden.addListener 函数如下所示：

onShown.addListener 函数如下所示：

表示扩展程序希望在“记录器”面板中显示此视图。

创建可以处理重放的视图。此视图将嵌入到“记录器”面板中。

在开发者工具工具栏中的扩展程序图标旁边显示的标题。

面板的 HTML 页面相对于扩展程序目录的路径。

RecorderExtensionPlugin

实现 RecorderExtensionPlugin 接口的实例。

**Examples:**

Example 1 (unknown):
```unknown
class MyPlugin {
  stringify(recording) {
    return Promise.resolve(JSON.stringify(recording));
  }
  stringifyStep(step) {
    return Promise.resolve(JSON.stringify(step));
  }
}

chrome.devtools.recorder.registerRecorderExtensionPlugin(
  new MyPlugin(),
  /*name=*/'MyPlugin',
  /*mediaType=*/'application/json'
);
```

Example 2 (javascript):
```javascript
const view = await chrome.devtools.recorder.createView(
  /* name= */ 'ExtensionName',
  /* pagePath= */ 'Replay.html'
);

let latestRecording;

view.onShown.addListener(() => {
  // Recorder has shown the view. Send additional data to the view if needed.
  chrome.runtime.sendMessage(JSON.stringify(latestRecording));
});

view.onHidden.addListener(() => {
  // Recorder has hidden the view.
});

export class RecorderPlugin {
  replay(recording) {
    // Share the data with the view.
    latestRecording = recording;
    // Request to show the view.
    view.show();
  }
}

chrome.devtools.recorder.registerRecorderExtensionPlugin(
  new RecorderPlugin(),
  /* name=*/ 'CoffeeTest'
);
```

Example 3 (javascript):
```javascript
(recording: object) => {...}
```

Example 4 (javascript):
```javascript
(recording: object) => {...}
```

---

## chrome.offscreen 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/offscreen?hl=zh-cn

**Contents:**
- chrome.offscreen 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 原因
- 示例
  - 维护屏幕外文档的生命周期
  - 在 Chrome 116 之前：检查屏幕外文档是否已打开
- 类型

使用 offscreen API 创建和管理屏幕外文档。

如需使用 Offscreen API，请在扩展程序清单中声明 "offscreen" 权限。例如：

Service worker 没有 DOM 访问权限，并且许多网站都有内容安全政策来限制内容脚本的功能。借助 Offscreen API，扩展程序可以在隐藏文档中使用 DOM API，而不会通过打开新窗口或标签页来中断用户体验。runtime API 是离屏文档支持的唯一扩展程序 API。

作为屏幕外文档加载的页面与其他类型的扩展程序页面不同，其处理方式也不同。 扩展程序的权限会沿用到离屏文档，但对扩展程序 API 的访问权限有限制。例如，由于 chrome.runtime API 是离屏文档支持的唯一扩展服务 API，因此必须使用该 API 的成员来处理消息传递。

使用 chrome.offscreen.createDocument() 和 chrome.offscreen.closeDocument() 创建并关闭屏幕外文档。createDocument() 需要提供文档的 url、原因和理由：

如需查看有效原因的列表，请参阅原因部分。原因是在创建文档时设置的，用于确定文档的有效期。AUDIO_PLAYBACK 原因会将文档设置为在 30 秒后关闭，且不播放音频。所有其他原因都不会设置使用期限限制。

以下示例展示了如何确保存在屏幕外文档。setupOffscreenDocument() 函数会调用 runtime.getContexts() 来查找现有的屏幕外文档，或者在文档尚不存在时创建该文档。

在向屏幕外文档发送消息之前，请调用 setupOffscreenDocument() 以确保该文档存在，如以下示例所示。

如需查看完整示例，请参阅 GitHub 上的 offscreen-clipboard 和 offscreen-dom 演示。

runtime.getContexts() 已在 Chrome 116 中添加。在旧版 Chrome 中，使用 clients.matchAll() 检查是否存在屏幕外文档：

开发者提供的字符串，用于更详细地说明需要背景信息的原因。用户代理 _可以_在向用户显示时使用此属性。

“AUDIO_PLAYBACK” 指定离屏文档负责播放音频。

"IFRAME_SCRIPTING" 指定离屏文档需要嵌入 iframe 并通过脚本修改 iframe 的内容。

“DOM_SCRAPING” 指定离屏文档需要嵌入 iframe 并抓取其 DOM 以提取信息。

“BLOBS” 指定离屏文档需要与 Blob 对象（包括 URL.createObjectURL()）互动。

“DOM_PARSER” 指定离屏文档需要使用 DOMParser API。

“USER_MEDIA” 指定离屏文档需要与来自用户媒体（例如 getUserMedia()）的媒体流进行交互。

“DISPLAY_MEDIA” 指定离屏文档需要与来自展示媒体（例如 getDisplayMedia()）的媒体流进行互动。

“WEB_RTC” 指定了离屏文档需要使用 WebRTC API。

“CLIPBOARD” 指定屏幕外文档需要与 Clipboard API 互动。

"LOCAL_STORAGE" 指定屏幕外文档需要访问 localStorage。

“WORKERS” 指定了离屏文档需要衍生工作器。

“BATTERY_STATUS” 指定了离屏文档需要使用 navigator.getBattery。

“MATCH_MEDIA” 指定离屏文档需要使用 window.matchMedia。

“GEOLOCATION” 指定离屏文档需要使用 navigator.geolocation。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "offscreen"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: 'off_screen.html',
  reasons: ['CLIPBOARD'],
  justification: 'reason for needing the document',
});
```

Example 3 (javascript):
```javascript
let creating; // A global promise to avoid concurrency issues
async function setupOffscreenDocument(path) {
  // Check all windows controlled by the service worker to see if one
  // of them is the offscreen document with the given path
  const offscreenUrl = chrome.runtime.getURL(path);
  const existingContexts = await chrome.runtime.getContexts({
    contextTypes: ['OFFSCREEN_DOCUMENT'],
    documentUrls: [offscreenUrl]
  });

  if (existingContexts.length > 0) {
    return;
  }

  // create offscreen document
  if (creating) {
    await creating;
  } else {
    creating = chrome.offscreen.createDocument({
      url: path,
      reasons: ['CLIPBOARD'],
      justification: 'reason for needing the document',
    });
    await creating;
    creating = null;
  }
}
```

Example 4 (javascript):
```javascript
chrome.action.onClicked.addListener(async () => {
  await setupOffscreenDocument('off_screen.html');

  // Send message to offscreen document
  chrome.runtime.sendMessage({
    type: '...',
    target: 'offscreen',
    data: '...'
  });
});
```

---

## chrome.wallpaper 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/wallpaper

**Contents:**
- chrome.wallpaper 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
- 类型
  - WallpaperLayout
    - 枚举
- 方法
  - setWallpaper()

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

您必须在应用的清单中声明“壁纸”权限，才能使用壁纸 API。例如：

例如，如需将壁纸设置为 https://example.com/a_file.png 中的图片，您可以按如下方式调用 chrome.wallpaper.setWallpaper：

将壁纸设置为 url 或 wallpaperData 中的图片，并采用指定的布局

以 ArrayBuffer 形式表示的 JPEG 或 PNG 编码壁纸图片。

如果应生成 128x60 缩略图，则为 True。尚不支持布局和宽高比。

Promise<ArrayBuffer | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "wallpaper"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.wallpaper.setWallpaper(
  {
    'url': 'https://example.com/a_file.jpg',
    'layout': 'CENTER_CROPPED',
    'filename': 'test_wallpaper'
  },
  function() {}
);
```

Example 3 (unknown):
```unknown
chrome.wallpaper.setWallpaper(  details: object,): Promise<ArrayBuffer | undefined>
```

---

## Prompt API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/ai/prompt-api?hl=zh-cn

**Contents:**
- Prompt API 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
  - 查看硬件要求
- 使用 Prompt API
  - 在 localhost 上使用
  - 模型参数
  - 创建会话
  - 通过初始提示添加上下文
    - 使用前缀限制回答
  - 添加预期输入和输出
    - 多模态功能

发布时间：2025 年 5 月 20 日，上次更新时间：2025 年 9 月 21 日

借助 Prompt API，您可以在浏览器中向 Gemini Nano 发送自然语言请求。

您可以通过多种方式使用 Prompt API。例如，您可以构建：

以上只是几个示例，我们期待看到您的创作成果。

开发者和在 Chrome 中使用这些 API 运行功能的用户必须满足以下要求。其他浏览器可能有不同的运行要求。

Language Detector API 和 Translator API 适用于桌面版 Chrome。这些 API 不适用于移动设备。当满足以下条件时，Prompt API、Summarizer API、Writer API、Rewriter API 和 Proofreader API 可在 Chrome 中正常运行：

随着浏览器更新模型，Gemini Nano 的确切大小可能会有所不同。如需确定当前大小，请访问 chrome://on-device-internals。

Prompt API 使用 Chrome 中的 Gemini Nano 模型。虽然该 API 已内置到 Chrome 中，但模型会在来源首次使用该 API 时单独下载。在使用此 API 之前，请确认您已了解《Google 生成式 AI 使用限制政策》。

如需确定模型是否已准备就绪，请调用 LanguageModel.availability()。

为了触发下载并实例化语言模型，请检查是否存在用户激活。然后，调用 create() 函数。

如果对 availability() 的响应为 downloading，请监听下载进度并告知用户，因为下载可能需要一些时间。

所有内置 AI API 都可在 Chrome 中的 localhost 上使用。将以下标志设置为 Enabled：

然后，点击重新启动或重启 Chrome。如果您遇到错误，请排查本地主机问题。

params() 函数会告知您语言模型的参数。该对象具有以下字段：

Prompt API 可以运行后，您可以使用 create() 函数创建会话。

您可以使用可选的 options 对象，通过 topK 和 temperature 自定义每个会话。这些形参的默认值是从 LanguageModel.params() 返回的。

create() 函数的可选选项对象还包含一个 signal 字段，可用于传递 AbortSignal 以销毁会话。

借助初始提示，您可以为语言模型提供有关之前互动的上下文，例如，允许用户在浏览器重启后继续之前存储的会话。

除了之前的角色之外，您还可以添加 "assistant" 角色，以详细说明模型之前的回答。例如：

在某些情况下，您可能希望预先填充部分 "assistant" 角色响应消息，而不是请求新的响应。这有助于引导语言模型使用特定的回答格式。为此，请将 prefix: true 添加到末尾的 "assistant" 角色消息中。例如：

Prompt API 具有多模态功能，并支持多种语言。创建会话时，设置 expectedInputs 和 expectedOutputs 模态和语言。

如果模型遇到不受支持的输入或输出，您可能会收到 "NotSupportedError" DOMException。

如需了解如何将 Prompt API 与音频输入搭配使用，请参阅 Mediarecorder 音频提示演示；如需了解如何将 Prompt API 与图片输入搭配使用，请参阅 Canvas 图片提示演示。

推理可能需要一些时间，尤其是在使用多模态输入进行提示时。 预先发送预定的提示来填充会话可能很有用，这样模型就可以提前开始处理。

虽然 initialPrompts 在会话创建时很有用，但除了 prompt() 或 promptStreaming() 方法之外，还可以使用 append() 方法在会话创建后提供额外的上下文提示。

在提示经过验证、处理并附加到会话后，append() 返回的 promise 会实现。如果无法附加提示，则拒绝相应 promise。

向 prompt() 或 promptStreaming() 方法添加 responseConstraint 字段，以传递 JSON 架构作为值。然后，您可以将结构化输出与 Prompt API 搭配使用。

在以下示例中，JSON 架构可确保模型使用 true 或 false 来响应，以对给定的消息是否与陶艺相关进行分类。

您的实现可以包含 JSON 架构或正则表达式，作为发送给模型的消息的一部分。这会使用一些输入配额。您可以将 responseConstraint 选项传递给 session.measureInputUsage()，以衡量该模型将使用多少输入配额。

您可以使用 omitResponseConstraintInput 选项避免此行为。如果您这样做，建议您在提示中添加一些指导：

您可以使用 prompt() 或 promptStreaming() 函数提示模型。

如果您希望获得简短的结果，可以使用 prompt() 函数，该函数会在获得回答后立即返回回答。

如果您希望获得更长的回答，则应使用 promptStreaming() 函数，该函数可让您在模型返回部分结果时显示这些结果。promptStreaming() 函数会返回一个 ReadableStream。

prompt() 和 promptStreaming() 都接受带有 signal 字段的可选第二个参数，该参数可让您停止运行提示。

每个会话都会跟踪对话的上下文。在会话的上下文窗口已满之前，系统会在后续互动中考虑之前的互动。

每个会话可处理的令牌数量上限。您可以通过以下方式查看自己距离此限制还差多少：

如需保留资源，您可以使用 clone() 函数克隆现有会话。对话上下文会重置，但初始提示会保持不变。clone() 函数接受一个带有 signal 字段的可选 options 对象，该字段可让您传递 AbortSignal 来销毁克隆的会话。

如果您不再需要会话，请调用 destroy() 以释放资源。当会话被销毁时，它将无法再使用，并且任何正在进行的执行都会中止。如果您打算经常提示模型，可能需要保持会话处于活动状态，因为创建会话可能需要一些时间。

我们构建了多个演示，以探索 Prompt API 的众多应用场景。以下演示是 Web 应用：

如需在 Chrome 扩展程序中测试 Prompt API，请安装演示扩展程序。扩展程序源代码可在 GitHub 上获取。

适用于 Web 的 Prompt API 仍在开发中。在构建此 API 期间，请参阅我们有关会话管理的最佳实践，以获得最佳性能。

默认情况下，Prompt API 仅适用于顶级窗口及其同源 iframe。可以使用权限政策 allow="" 属性将 API 访问权限委托给跨源 iframe：

由于需要为每个 worker 建立负责任的文档以检查权限政策状态，因此 Prompt API 目前在 Web Worker 中不可用。

您的反馈可以直接影响我们构建和实现此 API 和所有内置 AI API 的未来版本的方式。

**Examples:**

Example 1 (javascript):
```javascript
const availability = await LanguageModel.availability();
```

Example 2 (javascript):
```javascript
const session = await LanguageModel.create({
  monitor(m) {
    m.addEventListener('downloadprogress', (e) => {
      console.log(`Downloaded ${e.loaded * 100}%`);
    });
  },
});
```

Example 3 (unknown):
```unknown
await LanguageModel.params();
// {defaultTopK: 3, maxTopK: 128, defaultTemperature: 1, maxTemperature: 2}
```

Example 4 (javascript):
```javascript
const params = await LanguageModel.params();
// Initializing a new session must either specify both `topK` and
// `temperature` or neither of them.
const slightlyHighTemperatureSession = await LanguageModel.create({
  temperature: Math.max(params.defaultTemperature * 1.2, 2.0),
  topK: params.defaultTopK,
});
```

---

## API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api

**Contents:**
- API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- Common Extensions API 功能
- Chrome 扩展程序 API

大多数扩展程序都需要访问一个或多个 Chrome 扩展程序 API 才能正常运行。此 API 参考文档介绍了可在扩展程序中使用的 API，并提供了示例用例。

扩展程序 API 由一个命名空间组成，其中包含用于执行扩展程序工作的方法和属性，并且通常（但不一定）包含 manifest.json 文件的清单字段。例如，chrome.action 命名空间需要在清单中包含 "action" 对象。许多 API 还要求在清单中添加权限。

除非另有说明，否则扩展 API 中的方法是异步的。异步方法会立即返回，而无需等待调用它们的操作完成。使用 Promise 获取这些异步方法的结果。

使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 API 类型的 ChromeSetting 原型来获取和设置各个无障碍功能。为了获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不意味着拥有 accessibilityFeatures.read 权限。

使用 chrome.action API 控制 Google Chrome 工具栏中的扩展程序图标。

使用 chrome.alarms API 安排代码在指定时间或未来某个时间定期运行。

chrome.audio API 可供用户获取有关连接到系统的音频设备的信息并控制这些设备。此 API 目前仅在 ChromeOS 的自助服务终端模式下可用。

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

使用 chrome.declarativeContent API 根据网页内容采取行动，而无需获得读取网页内容的权限。

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

使用 chrome.devtools.inspectedWindow API 与检查的窗口互动：获取检查的网页的标签页 ID、在检查的窗口的上下文中评估代码、重新加载网页或获取网页中的资源列表。

使用 chrome.devtools.network API 检索开发者工具在“网络”面板中显示的网络请求的相关信息。

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

使用 chrome.devtools.performance API 监听开发者工具中“性能”面板的录制状态更新。

使用 chrome.devtools.recorder API 自定义开发者工具中的“记录器”面板。

使用 chrome.dns API 进行 DNS 解析。

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

使用 chrome.dom API 访问扩展程序的特殊 DOM API

使用 chrome.downloads API 以编程方式发起、监控、操纵和搜索下载。

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

chrome.events 命名空间包含 API 在调度事件时使用的常见类型，用于在发生值得注意的事情时通知您。

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

使用 chrome.fileBrowserHandler API 扩展 Chrome OS 文件浏览器。例如，您可以使用此 API 让用户将文件上传到您的网站。

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

使用 chrome.identity API 获取 OAuth2 访问令牌。

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

使用 chrome.instanceID 访问实例 ID 服务。

使用 chrome.loginState API 读取和监控登录状态。

chrome.management API 提供了一些方法来管理已安装的应用和扩展程序。

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

使用 offscreen API 创建和管理屏幕外文档。

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

使用 chrome.pageCapture API 将标签页另存为 MHTML。

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

使用 chrome.power API 可替换系统的电源管理功能。

chrome.printerProvider API 会公开打印管理器使用的事件，以便查询受扩展程序控制的打印机、查询这些打印机的功能，以及向这些打印机提交打印作业。

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

使用 chrome.processes API 与浏览器的进程进行交互。

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置代理配置。

使用 chrome.readingList API 读取和修改阅读清单中的内容。

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

使用 chrome.scripting API 在不同上下文中执行脚本。

使用 chrome.search API 通过默认提供程序进行搜索。

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

使用 chrome.sidePanel API 在浏览器的侧边栏中托管内容，与网页的主要内容并排显示。

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

使用 system.cpu API 查询 CPU 元数据。

使用 system.display API 查询展示元数据。

chrome.system.memory API。

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

使用 chrome.tabCapture API 与标签页媒体流进行互动。

使用 chrome.tabGroups API 与浏览器的标签页分组系统进行交互。您可以使用此 API 修改和重新排列浏览器中的标签页组。如需对标签页进行分组和取消分组，或查询哪些标签页位于分组中，请使用 chrome.tabs API。

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

使用 chrome.ttsEngine API 通过扩展程序实现文字转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序都会收到包含要朗读的发言内容和其他参数的事件。然后，扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

chrome.types API 包含 Chrome 的类型声明。

使用 userScripts API 在用户脚本上下文中执行用户脚本。

使用 chrome.vpnProvider API 实现 VPN 客户端。

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

借助 chrome.webAuthenticationProxy API，在远程主机上运行的远程桌面软件可以拦截 Web 身份验证 API (WebAuthn) 请求，以便在本地客户端上处理这些请求。

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

使用 chrome.webRequest API 观察和分析流量，并拦截、屏蔽或修改正在处理的请求。

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

---

## chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/documentScan?hl=zh-cn

**Contents:**
- chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 简单扫描
  - 复杂扫描
    - 发现
    - 扫描器配置
    - 扫描

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

文档扫描 API 旨在允许应用和扩展程序查看连接的文档扫描仪上的纸质文档的内容。

此 API 支持两种扫描文档的方式。如果您的使用情形适用于任何扫描器，并且不需要控制配置，请使用 scan() 方法。更复杂的用例需要结合使用多种方法，而这些方法仅在 Chrome 124 及更高版本中受支持。

对于简单用例（即可以使用任何扫描器且不需要控制配置的用例），请调用 scan()。此方法接受一个 ScanOptions 对象，并返回一个 Promise，该 Promise 会解析为一个 ScanResults 对象。此选项的功能仅限于扫描次数和调用方将接受的 MIME 类型。扫描结果以网址的形式返回，以便在用户界面的 <img> 标记中显示。

复杂扫描分三个阶段完成，如本部分所述。 此概要并未介绍每种方法实参或响应中返回的每种属性。它仅旨在为您提供有关编写扫描器代码的一般指南。

调用 getScannerList()。可用扫描器在 Promise 中返回，该 Promise 会解析为 GetScannerListResponse。

从返回的数组中选择一个扫描器，并保存其 scannerId 属性的值。

使用各个 ScannerInfo 对象的属性来区分同一扫描器的多个对象。来自同一扫描器的对象将具有相同的 deviceUuid 属性值。ScannerInfo 还包含一个 imageFormats 属性，其中包含一个支持的图片类型数组。

调用 openScanner()，并传入已保存的扫描器 ID。它会返回一个 Promise，该 Promise 会解析为 OpenScannerResponse。响应对象包含：

一个 scannerHandle 属性，您需要保存该属性。

一个包含扫描器专用属性的 options 属性，您需要设置这些属性。如需了解详情，请参阅“检索扫描器选项”。

（可选）如果您需要用户为扫描器选项提供值，请构建一个界面。您将需要上一步提供的扫描器选项，并且需要检索扫描器提供的选项组。如需了解详情，请参阅构建界面。

使用程序化值或用户提供的值构建 OptionSetting 对象数组。如需了解详情，请参阅“设置扫描程序选项”。

将 OptionSetting 对象的数组传递给 setOptions() 以设置扫描器的选项。它会返回一个 Promise，该 Promise 会解析为 SetOptionsResponse。此对象包含在扫描器配置的第 1 步中检索到的扫描器选项的更新版本。

由于更改一个选项可能会改变另一个选项的限制，因此您可能需要多次重复这些步骤。

构造一个 StartScanOptions 对象并将其传递给 startScan()。它会返回一个 Promise，该 Promise 会解析为 StartScanResponse。其 job 属性是一个句柄，您将使用该句柄来读取扫描数据或取消扫描。

将作业句柄传递给 readScanData()。它会返回一个 Promise，该 Promise 会解析为一个 ReadScanDataResponse 对象。如果数据读取成功，则其 result 属性等于 SUCCESS，并且其 data 属性包含扫描的一部分 ArrayBuffer。请注意，estimatedCompletion 包含截至目前已传送的总数据的估计百分比。

重复上一步，直到 result 属性等于 EOF 或出现错误。

当扫描结束时，使用在第 3 步中保存的扫描器句柄调用 closeScanner()。它会返回一个 Promise，该 Promise 会解析为 CloseScannerResponse。在创建作业后的任何时间调用 cancelScan() 都会结束扫描。

所有方法都会返回一个 Promise，该 Promise 会解析为某种类型的响应对象。其中大多数都包含一个 result 属性，其值是 OperationResult 的成员。除非 result 的值是特定值，否则响应对象的某些属性不会包含值。这些关系在每个响应对象的参考文档中都有说明。

例如，只有当 OpenScannerResponse.result 等于 SUCCESS 时，OpenScannerResponse.scannerHandle 才会有值。

扫描器选项因设备而异。因此，无法直接在 documentScan API 中反映扫描器选项。为了解决此问题，OpenScannerResponse（使用 openScanner() 检索）和 SetOptionsResponse（setOptions() 的响应对象）包含一个 options 属性，该属性是一个包含扫描器特定选项的对象。每个选项都是一个键值映射，其中键是特定于设备的选项，值是 ScannerOption 的实例。

例如，假设某个扫描器返回了名为“source”和“resolution”的选项。返回的 options 对象的结构将类似于以下示例。为简单起见，我们仅显示了部分 ScannerOption 响应。

虽然使用此 API 时不需要这样做，但您可能希望用户选择特定选项的值。这需要用户界面。使用 OpenScannerResponse（通过 openScanner() 打开）检索所连接扫描仪的选项，如上一部分中所述。

有些扫描器会以设备特定的方式对选项进行分组。它们不会影响选项行为，但由于扫描仪的产品文档中可能会提及这些群组，因此应向用户显示这些群组。您可以通过调用 getOptionGroups() 来检索这些群组。此方法会返回一个 Promise，该 Promise 会解析为一个 GetOptionGroupsResponse 对象。其 groups 属性包含一个特定于扫描器的群组数组。使用这些组中的信息来整理 OpenScannerResponse 中的选项以供显示。

如“扫描器配置”中所述，更改一个选项可能会改变另一个选项的限制。因此，setOptionsResponse（setOptions() 的响应对象）包含另一个 options 属性。使用此方法更新界面。然后，根据需要重复上述步骤，直到设置完所有选项。

通过将 OptionSetting 对象数组传递给 setOptions() 来设置扫描器选项。如需查看示例，请参阅下文中的扫描一页信纸大小的纸张部分。

此示例展示了一种从扫描器中检索页面作为 blob 的方法，并演示了如何使用 OperationResult 的值来使用 startScan() 和 readScanData()。

此示例展示了如何选择扫描器、设置其选项并打开它。然后，它会检索单个网页的内容并关闭扫描器。此流程演示了如何使用 getScannerList()、openScanner()、setOptions() 和 closeScanner()。请注意，网页的内容是通过调用上一个示例中的 pageAsBlob() 函数检索的。

如其他位置所述，向用户显示扫描器的配置选项需要调用 getOptionGroups()，此外还需要调用 openScanner() 返回的扫描器选项。这样，选项就可以向制造商定义组中的用户显示。此示例展示了如何执行此操作。

提供传递给 cancelScan() 的相同作业句柄。

后端的取消扫描结果。如果结果为 OperationResult.SUCCESS 或 OperationResult.CANCELLED，则表示扫描已取消，扫描器已准备好开始新的扫描。如果结果为 OperationResult.DEVICE_BUSY，则扫描器仍在处理请求的取消操作；调用者应等待一小段时间，然后再次尝试该请求。其他结果值表示不应重试的永久性错误。

关闭扫描器的结果。即使此值不是 SUCCESS，句柄也会无效，不应将其用于任何进一步的操作。

与传递给 closeScanner 的扫描器句柄相同。

“NOT_CONFIGURABLE” 相应选项为只读。

“SOFTWARE_CONFIGURABLE” 该选项可在软件中设置。

“HARDWARE_CONFIGURABLE” 用户可以通过切换扫描器上的按钮来设置此选项。

由 OptionConstraint 表示的限制条件的数据类型。

“INT_RANGE” 对一系列 OptionType.INT 值的限制。OptionConstraint 的 min、max 和 quant 属性将为 long，而其 list 属性将处于未设置状态。

“FIXED_RANGE” 对一系列 OptionType.FIXED 值的限制。OptionConstraint 的 min、max 和 quant 属性将为 double，而其 list 属性将处于未设置状态。

“INT_LIST” 对特定 OptionType.INT 值列表的限制。OptionConstraint.list 属性将包含 long 值，而其他属性将处于未设置状态。

“FIXED_LIST” 对特定 OptionType.FIXED 值列表的限制。OptionConstraint.list 属性将包含 double 值，而其他属性将处于未设置状态。

“STRING_LIST” 对特定 OptionType.STRING 值列表的限制。OptionConstraint.list 属性将包含 DOMString 值，而其他属性将处于未设置状态。

仅返回使用安全传输方式（例如 USB 或 TLS）的扫描器。

如果 result 为 SUCCESS，则提供扫描器驱动程序提供的选项组列表（按顺序）。

获取选项组的结果。如果此属性的值为 SUCCESS，系统将填充 groups 属性。

与传递给 getOptionGroups 的扫描器句柄相同。

枚举结果。请注意，即使此值指示存在错误，也可能会返回部分结果。

与所提供的 DeviceFilter 相匹配的扫描器列表（可能为空）。

如果 result 为 SUCCESS，则提供键值映射，其中键是设备专用选项，值是 ScannerOption 的实例。

打开扫描器的结果。如果此属性的值为 SUCCESS，则系统会填充 scannerHandle 和 options 属性。

如果 result 为 SUCCESS，则表示扫描器的句柄，可用于进一步操作。

传递给 openScanner() 的扫描器 ID。

“UNKNOWN” 发生了未知或一般性故障。

“INVALID” 数据或传递给方法的实参无效。

“WRONG_TYPE” 提供的值对于底层选项而言是错误的数据类型。

“COVER_OPEN” 平板扫描仪盖已打开。

“IO_ERROR” 与设备通信时发生错误。

“ACCESS_DENIED” 设备需要进行身份验证。

“NO_MEMORY” Chromebook 上的内存不足，无法完成操作。

“UNREACHABLE” 设备无法连接。

“INTERNAL_ERROR” 在调用应用之外的其他位置发生了错误。

string[] | number[] 可选

表示选项的数据类型。所请求的数据类型必须与底层选项的实际数据类型相匹配。

字符串 | 数值 | 布尔值 | 数值数组 可选

表示要设置的值。如果将此字段留空，系统将自动为已启用 autoSettable 的选项设置值。为 value 提供的数据类型必须与 type 一致。

“UNKNOWN” 相应选项的数据类型未知。value 属性将被取消设置。

“BOOL” value 属性将为 truefalse 之一。

“INT” 有符号 32 位整数。value 属性将为 long 或 long[]，具体取决于相应选项是否采用多个值。

“FIXED” 范围为 -32768 到 32767.9999 的双精度浮点数，分辨率为 1/65535。value 属性将为 double 或 double[]，具体取决于相应选项是否接受多个值。无法精确表示的双精度值将四舍五入到可用范围和精度。

“STRING” 任意字节序列，但不能包含 NUL ('\0')。value 属性将为 DOMString。

“BUTTON” 此类选项没有值。相反，设置此类选项会在扫描器驱动程序中产生特定于选项的副作用。例如，扫描器驱动程序可以使用按钮类型的选项来提供选择默认值的方法，或者指示自动进纸器前进到下一张纸。

“GROUP” 分组选项。没有值。包含此值是为了实现兼容性，但通常不会在 ScannerOption 值中返回此值。使用 getOptionGroups() 可检索包含成员选项的群组列表。

指明 ScannerOption.unit 的数据类型。

“UNITLESS” 相应值是一个无单位的数字。例如，它可以是阈值。

“PIXEL” 该值是像素数，例如扫描尺寸。

“MM” 该值以毫米为单位，例如扫描尺寸。

“DPI” 该值以每英寸的点数（例如分辨率）为单位进行衡量。

“PERCENT” 值是百分比，例如亮度。

“MICROSECOND” 该值以微秒为单位，例如曝光时间。

如果 result 为 SUCCESS，则包含扫描的图片数据的下一个块。如果 result 为 EOF，则包含扫描的图片数据的最后一块。

如果 result 为 SUCCESS，则表示到目前为止已传送的扫描数据占总扫描数据的百分比估计值，范围为 0 到 100。

提供传递给 readScanData() 的作业句柄。

读取数据的结果。如果其值为 SUCCESS，则 data 包含准备好读取的下一个（可能为零长度）图片数据块。如果其值为 EOF，则 data 包含图像数据的最后一个块。

用于与其他指向同一物理设备的 ScannerInfo 条目进行匹配。

可为返回的扫描结果请求的 MIME 类型数组。

用于访问扫描仪的协议或驱动程序的人类可读说明，例如 Mopria、WSD 或 epsonds。如果设备支持多种协议，此属性主要用于允许用户在这些协议之间进行选择。

如果为 true，扫描器连接的传输无法被被动监听器（例如 TLS 或 USB）拦截。

在当前扫描器选项上定义 OptionConstraint。

表示相应选项处于有效状态，可以设置或检索。如果为 false，则不会设置 value 属性。

如果为 true，则由扫描器驱动程序进行模拟。

使用小写 ASCII 字母、数字和短划线的选项名称。不允许使用变音符号。

value 属性中包含的数据类型，设置此选项时需要用到该数据类型。

字符串 | 数值 | 布尔值 | 数值数组 可选

选项的当前值（如果相关）。请注意，此属性的数据类型必须与 type 中指定的数据类型一致。

一个数据图片网址数组，其格式可作为“src”值传递给图片标记。

一个更新后的键值映射，其中包含从选项名称到 ScannerOption 值的映射，这些值包含尝试设置所有提供的选项后的新配置。此属性的结构与 OpenScannerResponse 中的 options 属性相同。

即使某些选项未成功设置，系统也会设置此属性；但如果检索更新后的配置失败（例如，扫描器在扫描过程中断开连接），系统将取消设置此属性。

一个结果数组，每个传入的 OptionSetting 对应一个结果。

提供传递给 setOptions() 的扫描器句柄。

如果指定了非零值，则将单个 readScanData 响应中返回的最大扫描字节数限制为该值。允许的最小值是 32768（32 KB）。如果未指定此属性，则返回的块的大小可能与整个扫描的图片一样大。

如果 result 为 SUCCESS，则提供可用于读取扫描数据或取消作业的句柄。

启动扫描的结果。如果此属性的值为 SUCCESS，系统将填充 job 属性。

提供传递给 startScan() 的相同扫描器句柄。

取消已开始的扫描，并返回一个 Promise，该 Promise 会解析为 CancelScanResponse 对象。如果使用回调，则会将对象传递给回调。

之前从对 startScan 的调用返回的有效扫描作业的句柄。

Promise<CancelScanResponse>

使用传入的句柄关闭扫描器，并返回一个 Promise，该 Promise 会解析为 CloseScannerResponse 对象。如果使用回调，则会将对象传递给回调。即使响应不成功，所提供的句柄也会失效，不应再用于后续操作。

指定之前从对 openScanner 的调用返回的开放扫描器的句柄。

Promise<CloseScannerResponse>

从之前通过 openScanner 打开的扫描器获取群组名称和成员选项。此方法会返回一个 Promise，该 Promise 会解析为一个 GetOptionGroupsResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

通过调用 openScanner 返回的已打开扫描器的句柄。

Promise<GetOptionGroupsResponse>

获取可用扫描器的列表，并返回一个 Promise，该 Promise 会解析为 GetScannerListResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

一个 DeviceFilter，用于指示应返回哪些类型的扫描器。

Promise<GetScannerListResponse>

打开扫描器以进行独占访问，并返回一个 Promise，该 Promise 会解析为 OpenScannerResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

要打开的扫描器的 ID。此值是从之前对 getScannerList 的调用返回的值之一。

Promise<OpenScannerResponse>

从有效作业句柄读取下一块可用的图片数据，并返回一个 Promise，该 Promise 会解析为 ReadScanDataResponse 对象。如果使用回调，则会将对象传递给回调。

**注意：**响应结果为 SUCCESS 且 data 成员的长度为零是有效的。这意味着扫描器仍在工作，但尚未准备好其他数据。来电者应稍等片刻，然后重试。

扫描作业完成后，响应将包含结果值 EOF。此响应可能包含一个最终的非零 data 成员。

之前从 startScan 返回的有效作业句柄。

Promise<ReadScanDataResponse>

执行文档扫描，并返回一个 Promise，该 Promise 会解析为 ScanResults 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

为指定扫描器设置选项，并返回一个 Promise，该 Promise 会解析为一个 SetOptionsResponse 对象，其中包含尝试按传入的 OptionSetting 对象中的顺序设置每个值的结果。如果使用回调，则会将对象传递给回调。

要设置选项的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

要应用于扫描器的 OptionSetting 对象列表。

Promise<SetOptionsResponse>

在指定的扫描器上开始扫描，并返回一个 Promise，该 Promise 会解析为 StartScanResponse。如果使用回调，则会将对象传递给回调。如果调用成功，响应会包含一个作业句柄，可在后续调用中使用该句柄来读取扫描数据或取消扫描。

打开的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

一个 StartScanOptions 对象，用于指示扫描时要使用的选项。StartScanOptions.format 属性必须与扫描器 ScannerInfo 中返回的某个条目匹配。

Promise<StartScanResponse>

**Examples:**

Example 1 (unknown):
```unknown
{
  "key1": { scannerOptionInstance }
  "key2": { scannerOptionInstance }
}
```

Example 2 (unknown):
```unknown
{
  "source": {
    "name": "source",
    "type": OptionType.STRING,
...
},
  "resolution": {
    "name": "resolution",
    "type": OptionType.INT,
...
  },
...
}
```

Example 3 (unknown):
```unknown
{
  scannerHandle: "123456",
  result: SUCCESS,
  groups: [
    {
      title: "Standard",
      members: [ "resolution", "mode", "source" ]
    }
  ]
}
```

Example 4 (javascript):
```javascript
async function pageAsBlob(handle) {
  let response = await chrome.documentScan.startScan(
      handle, {format: "image/jpeg"});
  if (response.result != chrome.documentScan.OperationResult.SUCCESS) {
    return null;
  }
  const job = response.job;

  let imgParts = [];
  response = await chrome.documentScan.readScanData(job);
  while (response.result == chrome.documentScan.OperationResult.SUCCESS) {
    if (response.data && response.data.byteLength > 0) {
        imgParts.push(response.data);
    } else {
      // Delay so hardware can make progress.
      await new Promise(r => setTimeout(r, 100));
    }
    response = await chrome.documentScan.readScanData(job);
  }
  if (response.result != chrome.documentScan.OperationResult.EOF) {
    return null;
  }
  if (response.data && response.data.byteLength > 0) {
    imgParts.push(response.data);
  }
  return new Blob(imgParts, { type: "image/jpeg" });
}
```

---

## chrome.enterprise.login 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/login?hl=zh-cn

**Contents:**
- chrome.enterprise.login 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - exitCurrentManagedGuestSession()
    - 返回

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.login.exitCurrentManagedGuestSession(): Promise<void>
```

---

## chrome.identity 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/identity?hl=zh-cn

**Contents:**
- chrome.identity 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - AccountInfo
    - 属性
  - AccountStatus
    - 枚举
  - GetAuthTokenResult
    - 属性

使用 chrome.identity API 获取 OAuth2 访问令牌。

相应账号的唯一标识符。此 ID 在账号的整个生命周期内都不会发生变化。

“ANY” 指定是否存在主账号（如果有）。

已登录到相应个人资料的主账号的状态，应返回该状态的 ProfileUserInfo。默认为 SYNC 账号状态。

当前配置文件中登录的用户账号的电子邮件地址。如果用户未登录或未指定 identity.email 清单权限，则为空。

相应账号的唯一标识符。此 ID 在账号的整个生命周期内都不会发生变化。如果用户未登录，或者（在 M41 及更高版本中）未指定 identity.email 清单权限，则为空。

应返回其令牌的账号 ID。如果未指定，该函数将使用 Chrome 个人资料中的账号：如果有同步账号，则使用该账号；否则，使用第一个 Google Web 账号。

借助 enableGranularPermissions 标志，扩展程序可以提前选择启用精细的权限请求页面，在该页面中，系统会单独授予或拒绝所请求的权限。

获取令牌可能需要用户登录 Chrome 或批准应用请求的范围。如果互动标志为 true，getAuthToken 将根据需要提示用户。当标志为 false 或省略时，每当需要提示时，getAuthToken 都会返回失败。

如果存在 scopes 字段，则该字段会替换 manifest.json 中指定的范围列表。

是否在页面加载后终止非交互式请求的 launchWebAuthFlow。此参数不会影响互动式流程。

如果设置为 true（默认值），则流程会在网页加载后立即终止。如果设置为 false，则只有在 timeoutMsForNonInteractive 通过后，流程才会终止。对于使用 JavaScript 在网页加载后执行重定向的身份提供方，此功能非常有用。

由于某些授权流程可能会立即重定向到结果网址，因此 launchWebAuthFlow 会隐藏其 WebView，直到第一次导航重定向到最终网址，或完成加载要显示的网页。

如果 interactive 标志为 true，则在页面加载完成后显示窗口。如果标志为 false 或被省略，如果初始导航未完成流程，launchWebAuthFlow 将返回错误。

对于使用 JavaScript 进行重定向的流程，可以将 abortOnLoadForNonInteractive 设置为 false，同时设置 timeoutMsForNonInteractive，以便网页有机会执行任何重定向。

以毫秒为单位，launchWebAuthFlow 是允许在非互动模式下运行的总时长上限。仅当 interactive 为 false 时才有效。

检索描述相应个人资料中存在的账号的 AccountInfo 对象列表。

getAccounts 仅在开发版渠道中受支持。

Promise<AccountInfo[]>

使用 manifest.json 的 oauth2 部分中指定的客户端 ID 和范围获取 OAuth2 访问令牌。

Identity API 会在内存中缓存访问令牌，因此可以在需要令牌时随时以非互动方式调用 getAuthToken。令牌缓存会自动处理过期问题。

为了提供良好的用户体验，请务必在应用中通过界面发起互动式令牌请求，说明授权的用途。如果不这样做，您的用户会收到授权请求，或者如果他们未登录，则会看到 Chrome 登录界面，但没有任何上下文。尤其是，请勿在应用首次启动时以交互方式使用 getAuthToken。

注意：如果使用回调调用此函数，此函数不会返回对象，而是会将这两个属性作为单独的实参传递给回调。

Promise<GetAuthTokenResult>

检索已登录个人资料的用户的电子邮件地址和经过混淆处理的 GAIA ID。

需要 identity.email 清单权限。否则，返回空结果。

此 API 在以下两个方面与 identity.getAccounts 不同。返回的信息可离线使用，并且仅适用于相应个人资料的主要账号。

Promise<ProfileUserInfo>

生成要在 launchWebAuthFlow 中使用的重定向网址。

生成的网址与格式 https://<app-id>.chromiumapp.org/* 相匹配。

此方法通过启动 WebView 并将其导航到提供商的身份验证流程中的第一个网址，来实现与非 Google 身份提供商的身份验证流程。当提供方重定向到与模式 https://<app-id>.chromiumapp.org/* 匹配的网址时，窗口将关闭，并且最终重定向网址将传递给 callback 函数。

为了提供良好的用户体验，请务必在应用中通过界面启动互动式授权流程，说明授权的用途。如果不这样做，您的用户将收到没有上下文的授权请求。尤其是，请勿在应用首次启动时启动互动式身份验证流程。

Promise<string | undefined>

从 Identity API 的令牌缓存中移除 OAuth2 访问令牌。

如果发现访问令牌无效，应将其传递给 removeCachedAuthToken 以从缓存中移除。然后，应用可以使用 getAuthToken 检索新令牌。

当用户个人资料中某个账号的登录状态发生变化时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.identity.clearAllCachedAuthTokens(): Promise<void>
```

Example 2 (unknown):
```unknown
chrome.identity.getAccounts(): Promise<AccountInfo[]>
```

Example 3 (unknown):
```unknown
chrome.identity.getAuthToken(  details?: TokenDetails,): Promise<GetAuthTokenResult>
```

Example 4 (unknown):
```unknown
chrome.identity.getProfileUserInfo(  details?: ProfileDetails,): Promise<ProfileUserInfo>
```

---

## chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/documentScan

**Contents:**
- chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 简单扫描
  - 复杂扫描
    - 发现
    - 扫描器配置
    - 扫描

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

文档扫描 API 旨在允许应用和扩展程序查看连接的文档扫描仪上的纸质文档的内容。

此 API 支持两种扫描文档的方式。如果您的使用情形适用于任何扫描器，并且不需要控制配置，请使用 scan() 方法。更复杂的用例需要结合使用多种方法，而这些方法仅在 Chrome 124 及更高版本中受支持。

对于简单用例（即可以使用任何扫描器且不需要控制配置的用例），请调用 scan()。此方法接受一个 ScanOptions 对象，并返回一个 Promise，该 Promise 会解析为一个 ScanResults 对象。此选项的功能仅限于扫描次数和调用方将接受的 MIME 类型。扫描结果以网址的形式返回，以便在用户界面的 <img> 标记中显示。

复杂扫描分三个阶段完成，如本部分所述。 此概要并未介绍每种方法实参或响应中返回的每种属性。它仅旨在为您提供有关编写扫描器代码的一般指南。

调用 getScannerList()。可用扫描器在 Promise 中返回，该 Promise 会解析为 GetScannerListResponse。

从返回的数组中选择一个扫描器，并保存其 scannerId 属性的值。

使用各个 ScannerInfo 对象的属性来区分同一扫描器的多个对象。来自同一扫描器的对象将具有相同的 deviceUuid 属性值。ScannerInfo 还包含一个 imageFormats 属性，其中包含一个支持的图片类型数组。

调用 openScanner()，并传入已保存的扫描器 ID。它会返回一个 Promise，该 Promise 会解析为 OpenScannerResponse。响应对象包含：

一个 scannerHandle 属性，您需要保存该属性。

一个包含扫描器专用属性的 options 属性，您需要设置这些属性。如需了解详情，请参阅“检索扫描器选项”。

（可选）如果您需要用户为扫描器选项提供值，请构建一个界面。您将需要上一步提供的扫描器选项，并且需要检索扫描器提供的选项组。如需了解详情，请参阅构建界面。

使用程序化值或用户提供的值构建 OptionSetting 对象数组。如需了解详情，请参阅“设置扫描程序选项”。

将 OptionSetting 对象的数组传递给 setOptions() 以设置扫描器的选项。它会返回一个 Promise，该 Promise 会解析为 SetOptionsResponse。此对象包含在扫描器配置的第 1 步中检索到的扫描器选项的更新版本。

由于更改一个选项可能会改变另一个选项的限制，因此您可能需要多次重复这些步骤。

构造一个 StartScanOptions 对象并将其传递给 startScan()。它会返回一个 Promise，该 Promise 会解析为 StartScanResponse。其 job 属性是一个句柄，您将使用该句柄来读取扫描数据或取消扫描。

将作业句柄传递给 readScanData()。它会返回一个 Promise，该 Promise 会解析为一个 ReadScanDataResponse 对象。如果数据读取成功，则其 result 属性等于 SUCCESS，并且其 data 属性包含扫描的一部分 ArrayBuffer。请注意，estimatedCompletion 包含截至目前已传送的总数据的估计百分比。

重复上一步，直到 result 属性等于 EOF 或出现错误。

当扫描结束时，使用在第 3 步中保存的扫描器句柄调用 closeScanner()。它会返回一个 Promise，该 Promise 会解析为 CloseScannerResponse。在创建作业后的任何时间调用 cancelScan() 都会结束扫描。

所有方法都会返回一个 Promise，该 Promise 会解析为某种类型的响应对象。其中大多数都包含一个 result 属性，其值是 OperationResult 的成员。除非 result 的值是特定值，否则响应对象的某些属性不会包含值。这些关系在每个响应对象的参考文档中都有说明。

例如，只有当 OpenScannerResponse.result 等于 SUCCESS 时，OpenScannerResponse.scannerHandle 才会有值。

扫描器选项因设备而异。因此，无法直接在 documentScan API 中反映扫描器选项。为了解决此问题，OpenScannerResponse（使用 openScanner() 检索）和 SetOptionsResponse（setOptions() 的响应对象）包含一个 options 属性，该属性是一个包含扫描器特定选项的对象。每个选项都是一个键值映射，其中键是特定于设备的选项，值是 ScannerOption 的实例。

例如，假设某个扫描器返回了名为“source”和“resolution”的选项。返回的 options 对象的结构将类似于以下示例。为简单起见，我们仅显示了部分 ScannerOption 响应。

虽然使用此 API 时不需要这样做，但您可能希望用户选择特定选项的值。这需要用户界面。使用 OpenScannerResponse（通过 openScanner() 打开）检索所连接扫描仪的选项，如上一部分中所述。

有些扫描器会以设备特定的方式对选项进行分组。它们不会影响选项行为，但由于扫描仪的产品文档中可能会提及这些群组，因此应向用户显示这些群组。您可以通过调用 getOptionGroups() 来检索这些群组。此方法会返回一个 Promise，该 Promise 会解析为一个 GetOptionGroupsResponse 对象。其 groups 属性包含一个特定于扫描器的群组数组。使用这些组中的信息来整理 OpenScannerResponse 中的选项以供显示。

如“扫描器配置”中所述，更改一个选项可能会改变另一个选项的限制。因此，setOptionsResponse（setOptions() 的响应对象）包含另一个 options 属性。使用此方法更新界面。然后，根据需要重复上述步骤，直到设置完所有选项。

通过将 OptionSetting 对象数组传递给 setOptions() 来设置扫描器选项。如需查看示例，请参阅下文中的扫描一页信纸大小的纸张部分。

此示例展示了一种从扫描器中检索页面作为 blob 的方法，并演示了如何使用 OperationResult 的值来使用 startScan() 和 readScanData()。

此示例展示了如何选择扫描器、设置其选项并打开它。然后，它会检索单个网页的内容并关闭扫描器。此流程演示了如何使用 getScannerList()、openScanner()、setOptions() 和 closeScanner()。请注意，网页的内容是通过调用上一个示例中的 pageAsBlob() 函数检索的。

如其他位置所述，向用户显示扫描器的配置选项需要调用 getOptionGroups()，此外还需要调用 openScanner() 返回的扫描器选项。这样，选项就可以向制造商定义组中的用户显示。此示例展示了如何执行此操作。

提供传递给 cancelScan() 的相同作业句柄。

后端的取消扫描结果。如果结果为 OperationResult.SUCCESS 或 OperationResult.CANCELLED，则表示扫描已取消，扫描器已准备好开始新的扫描。如果结果为 OperationResult.DEVICE_BUSY，则扫描器仍在处理请求的取消操作；调用者应等待一小段时间，然后再次尝试该请求。其他结果值表示不应重试的永久性错误。

关闭扫描器的结果。即使此值不是 SUCCESS，句柄也会无效，不应将其用于任何进一步的操作。

与传递给 closeScanner 的扫描器句柄相同。

“NOT_CONFIGURABLE” 相应选项为只读。

“SOFTWARE_CONFIGURABLE” 该选项可在软件中设置。

“HARDWARE_CONFIGURABLE” 用户可以通过切换扫描器上的按钮来设置此选项。

由 OptionConstraint 表示的限制条件的数据类型。

“INT_RANGE” 对一系列 OptionType.INT 值的限制。OptionConstraint 的 min、max 和 quant 属性将为 long，而其 list 属性将处于未设置状态。

“FIXED_RANGE” 对一系列 OptionType.FIXED 值的限制。OptionConstraint 的 min、max 和 quant 属性将为 double，而其 list 属性将处于未设置状态。

“INT_LIST” 对特定 OptionType.INT 值列表的限制。OptionConstraint.list 属性将包含 long 值，而其他属性将处于未设置状态。

“FIXED_LIST” 对特定 OptionType.FIXED 值列表的限制。OptionConstraint.list 属性将包含 double 值，而其他属性将处于未设置状态。

“STRING_LIST” 对特定 OptionType.STRING 值列表的限制。OptionConstraint.list 属性将包含 DOMString 值，而其他属性将处于未设置状态。

仅返回使用安全传输方式（例如 USB 或 TLS）的扫描器。

如果 result 为 SUCCESS，则提供扫描器驱动程序提供的选项组列表（按顺序）。

获取选项组的结果。如果此属性的值为 SUCCESS，系统将填充 groups 属性。

与传递给 getOptionGroups 的扫描器句柄相同。

枚举结果。请注意，即使此值指示存在错误，也可能会返回部分结果。

与所提供的 DeviceFilter 相匹配的扫描器列表（可能为空）。

如果 result 为 SUCCESS，则提供键值映射，其中键是设备专用选项，值是 ScannerOption 的实例。

打开扫描器的结果。如果此属性的值为 SUCCESS，则系统会填充 scannerHandle 和 options 属性。

如果 result 为 SUCCESS，则表示扫描器的句柄，可用于进一步操作。

传递给 openScanner() 的扫描器 ID。

“UNKNOWN” 发生了未知或一般性故障。

“INVALID” 数据或传递给方法的实参无效。

“WRONG_TYPE” 提供的值对于底层选项而言是错误的数据类型。

“COVER_OPEN” 平板扫描仪盖已打开。

“IO_ERROR” 与设备通信时发生错误。

“ACCESS_DENIED” 设备需要进行身份验证。

“NO_MEMORY” Chromebook 上的内存不足，无法完成操作。

“UNREACHABLE” 设备无法连接。

“INTERNAL_ERROR” 在调用应用之外的其他位置发生了错误。

string[] | number[] 可选

表示选项的数据类型。所请求的数据类型必须与底层选项的实际数据类型相匹配。

字符串 | 数值 | 布尔值 | 数值数组 可选

表示要设置的值。如果将此字段留空，系统将自动为已启用 autoSettable 的选项设置值。为 value 提供的数据类型必须与 type 一致。

“UNKNOWN” 相应选项的数据类型未知。value 属性将被取消设置。

“BOOL” value 属性将为 truefalse 之一。

“INT” 有符号 32 位整数。value 属性将为 long 或 long[]，具体取决于相应选项是否采用多个值。

“FIXED” 范围为 -32768 到 32767.9999 的双精度浮点数，分辨率为 1/65535。value 属性将为 double 或 double[]，具体取决于相应选项是否接受多个值。无法精确表示的双精度值将四舍五入到可用范围和精度。

“STRING” 任意字节序列，但不能包含 NUL ('\0')。value 属性将为 DOMString。

“BUTTON” 此类选项没有值。相反，设置此类选项会在扫描器驱动程序中产生特定于选项的副作用。例如，扫描器驱动程序可以使用按钮类型的选项来提供选择默认值的方法，或者指示自动进纸器前进到下一张纸。

“GROUP” 分组选项。没有值。包含此值是为了实现兼容性，但通常不会在 ScannerOption 值中返回此值。使用 getOptionGroups() 可检索包含成员选项的群组列表。

指明 ScannerOption.unit 的数据类型。

“UNITLESS” 相应值是一个无单位的数字。例如，它可以是阈值。

“PIXEL” 该值是像素数，例如扫描尺寸。

“MM” 该值以毫米为单位，例如扫描尺寸。

“DPI” 该值以每英寸的点数（例如分辨率）为单位进行衡量。

“PERCENT” 值是百分比，例如亮度。

“MICROSECOND” 该值以微秒为单位，例如曝光时间。

如果 result 为 SUCCESS，则包含扫描的图片数据的下一个块。如果 result 为 EOF，则包含扫描的图片数据的最后一块。

如果 result 为 SUCCESS，则表示到目前为止已传送的扫描数据占总扫描数据的百分比估计值，范围为 0 到 100。

提供传递给 readScanData() 的作业句柄。

读取数据的结果。如果其值为 SUCCESS，则 data 包含准备好读取的下一个（可能为零长度）图片数据块。如果其值为 EOF，则 data 包含图像数据的最后一个块。

用于与其他指向同一物理设备的 ScannerInfo 条目进行匹配。

可为返回的扫描结果请求的 MIME 类型数组。

用于访问扫描仪的协议或驱动程序的人类可读说明，例如 Mopria、WSD 或 epsonds。如果设备支持多种协议，此属性主要用于允许用户在这些协议之间进行选择。

如果为 true，扫描器连接的传输无法被被动监听器（例如 TLS 或 USB）拦截。

在当前扫描器选项上定义 OptionConstraint。

表示相应选项处于有效状态，可以设置或检索。如果为 false，则不会设置 value 属性。

如果为 true，则由扫描器驱动程序进行模拟。

使用小写 ASCII 字母、数字和短划线的选项名称。不允许使用变音符号。

value 属性中包含的数据类型，设置此选项时需要用到该数据类型。

字符串 | 数值 | 布尔值 | 数值数组 可选

选项的当前值（如果相关）。请注意，此属性的数据类型必须与 type 中指定的数据类型一致。

一个数据图片网址数组，其格式可作为“src”值传递给图片标记。

一个更新后的键值映射，其中包含从选项名称到 ScannerOption 值的映射，这些值包含尝试设置所有提供的选项后的新配置。此属性的结构与 OpenScannerResponse 中的 options 属性相同。

即使某些选项未成功设置，系统也会设置此属性；但如果检索更新后的配置失败（例如，扫描器在扫描过程中断开连接），系统将取消设置此属性。

一个结果数组，每个传入的 OptionSetting 对应一个结果。

提供传递给 setOptions() 的扫描器句柄。

如果指定了非零值，则将单个 readScanData 响应中返回的最大扫描字节数限制为该值。允许的最小值是 32768（32 KB）。如果未指定此属性，则返回的块的大小可能与整个扫描的图片一样大。

如果 result 为 SUCCESS，则提供可用于读取扫描数据或取消作业的句柄。

启动扫描的结果。如果此属性的值为 SUCCESS，系统将填充 job 属性。

提供传递给 startScan() 的相同扫描器句柄。

取消已开始的扫描，并返回一个 Promise，该 Promise 会解析为 CancelScanResponse 对象。如果使用回调，则会将对象传递给回调。

之前从对 startScan 的调用返回的有效扫描作业的句柄。

Promise<CancelScanResponse>

使用传入的句柄关闭扫描器，并返回一个 Promise，该 Promise 会解析为 CloseScannerResponse 对象。如果使用回调，则会将对象传递给回调。即使响应不成功，所提供的句柄也会失效，不应再用于后续操作。

指定之前从对 openScanner 的调用返回的开放扫描器的句柄。

Promise<CloseScannerResponse>

从之前通过 openScanner 打开的扫描器获取群组名称和成员选项。此方法会返回一个 Promise，该 Promise 会解析为一个 GetOptionGroupsResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

通过调用 openScanner 返回的已打开扫描器的句柄。

Promise<GetOptionGroupsResponse>

获取可用扫描器的列表，并返回一个 Promise，该 Promise 会解析为 GetScannerListResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

一个 DeviceFilter，用于指示应返回哪些类型的扫描器。

Promise<GetScannerListResponse>

打开扫描器以进行独占访问，并返回一个 Promise，该 Promise 会解析为 OpenScannerResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

要打开的扫描器的 ID。此值是从之前对 getScannerList 的调用返回的值之一。

Promise<OpenScannerResponse>

从有效作业句柄读取下一块可用的图片数据，并返回一个 Promise，该 Promise 会解析为 ReadScanDataResponse 对象。如果使用回调，则会将对象传递给回调。

**注意：**响应结果为 SUCCESS 且 data 成员的长度为零是有效的。这意味着扫描器仍在工作，但尚未准备好其他数据。来电者应稍等片刻，然后重试。

扫描作业完成后，响应将包含结果值 EOF。此响应可能包含一个最终的非零 data 成员。

之前从 startScan 返回的有效作业句柄。

Promise<ReadScanDataResponse>

执行文档扫描，并返回一个 Promise，该 Promise 会解析为 ScanResults 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

为指定扫描器设置选项，并返回一个 Promise，该 Promise 会解析为一个 SetOptionsResponse 对象，其中包含尝试按传入的 OptionSetting 对象中的顺序设置每个值的结果。如果使用回调，则会将对象传递给回调。

要设置选项的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

要应用于扫描器的 OptionSetting 对象列表。

Promise<SetOptionsResponse>

在指定的扫描器上开始扫描，并返回一个 Promise，该 Promise 会解析为 StartScanResponse。如果使用回调，则会将对象传递给回调。如果调用成功，响应会包含一个作业句柄，可在后续调用中使用该句柄来读取扫描数据或取消扫描。

打开的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

一个 StartScanOptions 对象，用于指示扫描时要使用的选项。StartScanOptions.format 属性必须与扫描器 ScannerInfo 中返回的某个条目匹配。

Promise<StartScanResponse>

**Examples:**

Example 1 (unknown):
```unknown
{
  "key1": { scannerOptionInstance }
  "key2": { scannerOptionInstance }
}
```

Example 2 (unknown):
```unknown
{
  "source": {
    "name": "source",
    "type": OptionType.STRING,
...
},
  "resolution": {
    "name": "resolution",
    "type": OptionType.INT,
...
  },
...
}
```

Example 3 (unknown):
```unknown
{
  scannerHandle: "123456",
  result: SUCCESS,
  groups: [
    {
      title: "Standard",
      members: [ "resolution", "mode", "source" ]
    }
  ]
}
```

Example 4 (javascript):
```javascript
async function pageAsBlob(handle) {
  let response = await chrome.documentScan.startScan(
      handle, {format: "image/jpeg"});
  if (response.result != chrome.documentScan.OperationResult.SUCCESS) {
    return null;
  }
  const job = response.job;

  let imgParts = [];
  response = await chrome.documentScan.readScanData(job);
  while (response.result == chrome.documentScan.OperationResult.SUCCESS) {
    if (response.data && response.data.byteLength > 0) {
        imgParts.push(response.data);
    } else {
      // Delay so hardware can make progress.
      await new Promise(r => setTimeout(r, 100));
    }
    response = await chrome.documentScan.readScanData(job);
  }
  if (response.result != chrome.documentScan.OperationResult.EOF) {
    return null;
  }
  if (response.data && response.data.byteLength > 0) {
    imgParts.push(response.data);
  }
  return new Blob(imgParts, { type: "image/jpeg" });
}
```

---

## chrome.dom 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/dom

**Contents:**
- chrome.dom 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 方法
  - openOrClosedShadowRoot()
    - 参数
    - 返回

使用 chrome.dom API 访问适用于扩展程序的特殊 DOM API

获取由指定元素托管的打开的影子根或封闭的影子根。如果该元素未附加影子根，它将返回 null。

请参阅 https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot

**Examples:**

Example 1 (unknown):
```unknown
chrome.dom.openOrClosedShadowRoot(  element: HTMLElement,): object
```

---

## chrome.history 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/history?hl=zh-cn

**Contents:**
- chrome.history 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 过渡类型
- 示例
- 类型
  - HistoryItem
    - 属性
  - TransitionType

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

如需与用户的浏览器历史记录互动，请使用 History API。

如需使用 History API，请在扩展程序清单中声明 "history" 权限。例如：

History API 使用过渡类型来描述浏览器在特定访问会话中如何导航到特定网址。例如，如果用户通过点击另一网页上的链接来访问某个网页，则过渡类型为“link”。如需查看过渡类型的列表，请参阅参考内容。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 history API 示例。

相应网页上次加载的时间（以自纪元以来经历的毫秒数表示）。

“链接” 用户通过点击其他网页上的链接到达此网页。

“已输入” 用户通过在地址栏中输入网址到达此网页。此属性还用于其他明确的导航操作。

“auto_bookmark” 用户通过界面中的建议（例如通过菜单项）到达此页面。

“auto_subframe” 用户是通过他们未请求的子框架导航到达此网页的，例如通过在上一网页的框架中加载的广告到达此网页。这些操作不一定会生成“后退”和“前进”菜单中的新导航条目。

“manual_subframe” 用户通过在子框架中选择内容到达此网页。

“generated” 用户在地址栏中输入内容并选择看起来不像网址的条目（例如 Google 搜索建议）后到达此网页。例如，匹配项可能包含 Google 搜索结果页面的网址，但向用户显示为“在 Google 上搜索…”。这些与输入型导航不同，因为用户没有输入或看到目标网址。它们还与关键字导航相关。

“auto_toplevel” 网页是在命令行中指定的，或者是起始网页。

“form_submit” 用户通过填写表单中的值并提交表单来访问此网页。并非所有表单提交都使用此过渡类型。

“重新加载” 用户重新加载了网页，可能是通过点击重新加载按钮或在地址栏中按 Enter 键完成的。会话恢复和“重新打开关闭的标签页”功能也使用此过渡类型。

“keyword” 此网页的网址是从可替换的关键字（而非默认搜索服务提供商）生成的。

“keyword_generated” 与为关键字生成的访问相对应。

相应操作的网址。必须采用从对 history.search() 的调用返回的格式。

相应 history.HistoryItem 的唯一标识符。

如果相应访问源自此设备，则为 True。如果该内容是从其他设备同步的，则为 False。

相应访问发生的时间，以自纪元开始计算的毫秒数表示。

在当前时间向历史记录添加一个网址，并指定“link”的过渡类型。

从历史记录中移除指定日期范围内的所有内容。除非所有访问都位于该范围内，否则网页不会从历史记录中移除。

在此日期之前添加到历史记录中的项目（以毫秒为单位，从 Epoch 起算）。

在此日期之后添加到历史记录中的项目（以自纪元开始算起的毫秒数表示）。

搜索历史记录，查找与查询匹配的每个网页的上次访问时间。

将结果限制为在此日期之前访问过的结果，以自纪元以来的毫秒数表示。

将结果限制为在此日期之后访问过的网页，以自纪元开始算起的毫秒数表示。如果未指定该属性，则默认值为 24 小时。

针对历史记录服务的自由文本查询。留空可检索所有网页。

Promise<HistoryItem[]>

在访问网址时触发，并提供相应网址的 HistoryItem 数据。此事件在网页加载之前触发。

当从历史记录中移除一个或多个网址时触发。移除所有访问记录后，相应网址会从历史记录中清除。

如果所有历史记录均已移除，则为 True。如果为 true，则网址将为空。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "history"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.history.addUrl(  details: UrlDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.history.deleteAll(): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.history.deleteRange(  range: object,): Promise<void>
```

---

## chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/inspectedWindow?hl=zh-cn

**Contents:**
- chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 在检查的窗口中执行代码
- 示例
- 类型
  - Resource
    - 属性
- 属性
  - tabId

使用 chrome.devtools.inspectedWindow API 与检查的窗口进行交互：获取被检查页面的标签页 ID、在被检查的窗口中评估代码、重新加载页面或者获取页面中的资源列表。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

tabId 属性提供可与 chrome.tabs.* 一起使用的标签页标识符 API 调用。但请注意，chrome.tabs.* API 不会提供给开发者工具 扩展程序网页 - 您需要将标签页 ID 传递到后台 页面并从中调用 chrome.tabs.* API 函数。

reload 方法可用于重新加载被检查的网页。此外，调用方还可以指定 用户代理字符串的替换值、在网页加载时提前注入的脚本，或 用于强制重新加载缓存资源的选项。

使用 getResources 调用和 onResourceContent 事件获取资源列表 （文档、样式表、脚本、图片等）。getContent 和 Resource 类的 setContent 方法以及 onResourceContentCommitted 事件可以 可用于支持资源内容的修改，例如由外部编辑者修改。

必须在清单中声明以下键才能使用此 API。

eval 方法可让扩展程序在 所检查的网页。此方法在合适的上下文中使用时功能强大，使用时则有危险 不当。请使用 tabs.executeScript 方法，除非您需要特定功能 由 eval 方法提供的函数定义。

eval 和 tabs.executeScript 方法之间的主要区别如下：

请注意，一个页面可以包含多个不同的 JavaScript 执行上下文。每个帧都有 以及运行内容脚本的每个扩展程序的其他上下文， 帧。

默认情况下，eval 方法在所检查页面的主框架上下文中执行。

eval 方法带有一个可选的第二个参数，您可以使用此参数来指定 代码评估时间。此 options 对象可以包含以下一个或多个键：

以下代码可检查被检查的网页所使用的 jQuery 版本：

若要试用此 API，请安装 chrome-extension-samples 中的 chrome-extension-samples 存储库

所检查页面中的资源，例如文档、脚本或图片。

如果内容未编码，则为空，否则对名称进行编码。目前只支持 base64。

如果用户已完成资源修改，并且资源的新内容应保留，则为 true；如果是在用户修改资源过程中发送的微小更改，则为 false。

如果资源内容设置成功，则设为“undefined”；否则会描述错误。

要检查的标签页的 ID。此 ID 可能会与 chrome.tabs 配合使用。*Compute Engine API 来创建虚拟机实例。

在被检查页面的主框架上下文中评估 JavaScript 表达式。表达式的计算结果必须是与 JSON 兼容的对象，否则会抛出异常。评估函数可以报告开发者工具端错误或评估期间发生的 JavaScript 异常。无论是哪种情况，回调的 result 参数都是 undefined。如果开发者工具端出现错误，isException 参数为非 null 值，并且 isError 设为 true，code 设为错误代码。如果发生 JavaScript 错误，系统会将 isException 设置为 true，并将 value 设置为抛出的对象的字符串值。

options 参数可以包含一个或多个选项。

如果指定，则系统会在网址与指定网址匹配的 iframe 上计算表达式。默认情况下，表达式将在所检查页面的顶部帧进行求值。

在与指定来源匹配的扩展程序的内容脚本上下文中评估表达式。如果指定，scriptExecutionContext 会覆盖“true”对 useContentScriptContext 进行设置。

在调用扩展程序的内容脚本的上下文中评估表达式，前提是内容脚本已注入检查的网页。否则，系统不会对表达式求值，并且会在调用回调函数时将异常参数设置为 isError 字段设置为 true 且 code 字段设置为 E_NOTFOUND 的对象。

在计算表达式时出现异常时提供详细信息的对象。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果在对表达式求值之前开发者工具端发生错误，则设置此字段。包含可以替换到说明字符串中的值数组，以提供有关错误原因的更多信息。

如果错误发生在对表达式求值之前，DevTools 端是否发生。

如果为 true，加载器将对所有在 load 事件触发之前加载的已检查页面资源绕过缓存。具体效果类似于在所检查的窗口或开发者工具窗口中按 Ctrl+Shift+R 的效果。

如果已指定，该脚本将在加载时立即注入到所检查网页的每一帧中，先于该帧的任何脚本。此脚本在后续重新加载后将不再注入（例如，如果用户按 Ctrl+R）。

如果已指定，该字符串将替换在加载所检查网页的资源时发送的 User-Agent HTTP 标头的值。该字符串还将覆盖 navigator.userAgent 属性的值，该值会返回到在检查页面中运行的任何脚本。

在提交资源的新修订版本时触发（例如，用户在开发者工具中保存了某个已修改的资源版本）。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.inspectedWindow.eval(
  "jQuery.fn.jquery",
  function(result, isException) {
    if (isException) {
      console.log("the page is not using jQuery");
    } else {
      console.log("The page is using jQuery v" + result);
    }
  }
);
```

Example 2 (javascript):
```javascript
(callback: function) => {...}
```

Example 3 (javascript):
```javascript
(content: string, encoding: string) => void
```

Example 4 (javascript):
```javascript
(content: string, commit: boolean, callback?: function) => {...}
```

---

## chrome.ttsEngine 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/ttsEngine

**Contents:**
- chrome.ttsEngine 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 处理语音事件
- 类型
  - AudioBuffer
    - 属性
  - AudioStreamOptions
    - 属性

使用 chrome.ttsEngine API 通过扩展程序实现文本转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序将会收到包含要朗读的语音和其他参数的事件。然后，您的扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

扩展程序可以将自己注册为语音引擎。这样，它就可以拦截对 tts.speak() 和 tts.stop() 等函数的部分或全部调用，并提供替代实现。扩展程序可以自由使用任何可用的 Web 技术来提供语音，包括从服务器流式传输音频、HTML5 音频。扩展程序甚至可以对这些语音内容执行其他操作，例如在弹出式窗口中显示字幕，或将其作为日志消息发送到远程服务器。

如需实现 TTS 引擎，扩展程序必须声明“ttsEngine”权限，然后在扩展程序清单中声明它提供的所有语音，如下所示：

voice_name 为必需参数，名称应具有足够的描述性，能够指明语音的名称和所使用的引擎。在极少数情况下，如果两个扩展程序注册了同名的语音，客户端可以指定应执行合成的扩展程序的 ID。

lang 参数是可选的，但强烈建议您使用。几乎在所有情况下，一个语音只能合成一种语言的语音。当引擎支持多种语言时，它可以轻松为每种语言注册单独的声音。在极少数情况下，单个语音可以处理多种语言，最简单的方法就是列出两个单独的语音，并在内部使用相同的逻辑进行处理。不过，如果您想创建一个可处理任何语言的语音，请从扩展程序的清单中省略 lang 参数。

最后，如果引擎可以发送事件来更新客户端的语音合成进度，则必须使用 event_types 参数。强烈建议至少支持 'end' 事件类型，以指示语音何时结束，否则 Chrome 将无法调度已排队的语音指令。

加载后，扩展程序可以通过调用 chrome.ttsEngine.updateVoices 替换声明的语音列表。（请注意，对 updateVoices 进行程序化调用时使用的参数采用驼峰式命名法：例如voiceName，而清单文件使用 voice_name。）

您可以发送的可能事件类型与 speak() 方法收到的事件类型相对应：

'interrupted' 和 'cancelled' 事件并非由语音引擎发送；而是由 Chrome 自动生成的。

假设您已按照下文所述注册语音事件监听器，文本转语音客户端可以通过调用 tts.getVoices 从扩展程序的清单中获取语音信息。

如需根据客户端请求生成语音，您的扩展程序必须为 onSpeak 和 onStop 注册监听器，如下所示：

是否向扩展程序发送给定语音请求的决定完全取决于扩展程序是否支持其清单中的给定语音参数，以及是否已为 onSpeak 和 onStop 注册监听器。换句话说，扩展程序无法接收语音请求并动态决定是否处理该请求。

文字转语音引擎中的音频缓冲区。其长度应与 audioStreamOptions.bufferSize 完全相同，并以音频流选项的采样率编码为单声道，以及线性 PCM、32 位有符号浮点，即 JavaScript 中的 Float32Array 类型。

如果此音频缓冲区是正在朗读的文本的最后一个缓冲区，则为 true。

有关安装失败的详细信息。如果语言安装失败，则可选择填充。

LanguageInstallStatus

语言字符串，采用语言代码-地区代码的形式，其中地区代码可以省略。例如 en、en-AU、zh-CH。

如果 TTS 客户端希望立即卸载语言，则为 True。引擎可能会根据此参数和请求方信息选择是否以及何时卸载语言。如果为 false，则系统可能会使用其他条件（例如近期使用情况）来确定何时卸载。

向 tts.speak() 方法指定的选项。

要用于合成的语言，格式为语言-地区。示例：“en”“en-US”“en-GB”“zh-CN”。

语音音调介于 0 到 2 之间（包括这两个数值），其中 0 表示最低，2 表示最高。1.0 对应于此语音的默认音调。

与此语音的默认语速相比的语速。1.0 是默认速率，通常为每分钟 180 到 220 个字左右。2.0 表示快一倍的速度，0.5 则表示原有速度的一半。此值保证介于 0.1 到 10.0 之间（包括这两个数值）。如果某个语音不支持此完整速率范围，请勿返回错误。而是将速率剪裁到语音支持的范围。

讲话音量，介于 0 到 1 之间（包括这两个数值），其中 0 表示最低音量，1 表示最高音量，默认值为 1.0。

发出语言管理请求的客户端。对于扩展程序，这是唯一的扩展程序 ID。对于 Chrome 功能，此字段是该功能的直观易懂的名称。

在尝试安装语言和卸载语言时由引擎调用。也用于响应来自客户的状态请求。安装或卸载语音时，引擎还应调用 ttsEngine.updateVoices 以注册语音。

由引擎调用以更新其语音列表。此列表会替换此扩展程序清单中声明的所有语音。

表示可用于语音合成的可用语音的 tts.TtsVoice 对象数组。

当 TTS 客户端请求安装新语言时触发。引擎应尝试下载并安装语言，并使用结果调用 ttsEngine.updateLanguage。成功后，引擎还应调用 ttsEngine.updateVoices 以注册新推出的语音。

当 TTS 客户端请求语言的安装状态时触发。

可选：如果引擎支持暂停事件，则应暂停正在说出的当前语音（如果有），直到收到恢复事件或停止事件。请注意，停止事件也应清除暂停状态。

可选：如果引擎支持暂停事件，则也应支持恢复事件，以继续说出当前的语音（如果有）。请注意，停止事件也应清除暂停状态。

当用户调用 tts.speak() 且此扩展程序清单中的某个语音最先与 options 对象匹配时调用。

来自文本转语音引擎的事件，用于指示此语音的状态。

当用户调用 tts.speak() 且此扩展程序清单中的某个语音最先与 options 对象匹配时调用。与 ttsEngine.onSpeak 不同，Chrome 提供音频播放服务并处理调度 TTS 事件。

当对 tts.stop 进行调用且此扩展程序可能正在说话时触发。如果扩展程序收到对 onStop 的调用，并且语音已停止，则应不执行任何操作（不引发错误）。如果语音处于暂停状态，此操作应取消暂停状态。

当 TTS 客户端指示不再需要某种语言时触发。

LanguageUninstallOptions

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My TTS Engine",
  "version": "1.0",
  "permissions": ["ttsEngine"],
  "tts_engine": {
    "voices": [
      {
        "voice_name": "Alice",
        "lang": "en-US",
        "event_types": ["start", "marker", "end"]
      },
      {
        "voice_name": "Pat",
        "lang": "en-US",
        "event_types": ["end"]
      }
    ]
  },
  "background": {
    "page": "background.html",
    "persistent": false
  }
}
```

Example 2 (javascript):
```javascript
const speakListener = (utterance, options, sendTtsEvent) => {
  sendTtsEvent({type: 'start', charIndex: 0})

  // (start speaking)

  sendTtsEvent({type: 'end', charIndex: utterance.length})
};

const stopListener = () => {
  // (stop all speech)
};

chrome.ttsEngine.onSpeak.addListener(speakListener);
chrome.ttsEngine.onStop.addListener(stopListener);
```

Example 3 (unknown):
```unknown
chrome.ttsEngine.updateLanguage(  status: LanguageStatus,): void
```

Example 4 (unknown):
```unknown
chrome.ttsEngine.updateVoices(  voices: TtsVoice[],): void
```

---

## chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/contextMenus

**Contents:**
- chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - ContextType
    - 枚举
  - CreateProperties
    - 属性

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

您必须在扩展程序的清单中声明 "contextMenus" 权限才能使用该 API。此外，您还应指定一个 16x16 像素的图标，以便在菜单项旁边显示。例如：

上下文菜单项可以显示在任何文档（或文档中的框架）中，即使是具有 file:// 或 chrome:// 网址的文档也不例外。如需控制您的项可以显示在哪些文档中，请在调用 create() 或 update() 方法时指定 documentUrlPatterns 字段。

您可以根据需要创建任意数量的上下文菜单项，但如果您的扩展程序中有多个上下文菜单项同时显示，Google Chrome 会自动将它们收起到一个父菜单中。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 contextMenus API 示例。

菜单可显示的各种不同情境。指定“all”相当于指定除“launcher”之外的所有其他上下文的组合。“启动器”上下文仅受应用支持，用于向上下文菜单添加菜单项，该上下文菜单会在点击启动器/任务栏/Dock/等中的应用图标时显示。不同平台可能会对启动器上下文菜单中实际支持的内容施加限制。

复选框或单选按钮的初始状态：true 表示选中，false 表示未选中。在给定的组中，一次只能选择一个单选按钮。

[ContextType, ...ContextType[]] 可选

相应菜单项将显示在其中的上下文列表。默认为 ['page']。

将相应项限制为仅适用于网址与指定格式之一匹配的文档或框架。如需详细了解格式，请参阅匹配模式。

此上下文菜单项处于启用还是停用状态。默认为 true。

要分配给相应商品的唯一 ID。对于活动网页，此属性为必需属性。不能与此扩展程序的其他 ID 相同。

父菜单项的 ID；这会使相应项成为之前添加的项的子项。

与 documentUrlPatterns 类似，基于 img、audio 和 video 标记的 src 属性以及 a 标记的 href 属性的过滤条件。

要在商品中显示的文字；除非 type 为 separator，否则此属性为必需属性。当上下文为 selection 时，请在字符串中使用 %s 来显示所选文本。例如，如果此参数的值为“将‘%s’翻译为 Pig Latin”，并且用户选择了“cool”一词，则所选内容的上下文菜单项为“将‘cool’翻译为 Pig Latin”。

点击菜单项时调用的回调函数。此属性在 Service Worker 内不可用；您应改为为 contextMenus.onClicked 注册监听器。

有关所点击商品以及点击发生时所处情境的信息。

发生点击的标签页的详细信息。平台应用没有此参数。

一个标志，用于指示复选框或单选项目在点击后的状态。

一个标志，用于指示元素是否可编辑（文本输入、文本区域等）。

点击上下文菜单的元素的框架的 ID（如果该元素位于框架中）。

点击上下文菜单的元素的框架的网址（如果该元素位于框架中）。

如果上下文菜单是在以下类型的元素上激活的，则为“image”“video”或“audio”之一。

点击菜单项的网页的网址。如果点击发生在没有当前页面的情境中（例如在启动器上下文菜单中），则不会设置此属性。

对于具有“src”网址的元素，此属性将存在。

一个标志，用于指示复选框或单选按钮在被点击之前的状态。

可添加到扩展操作上下文菜单中的顶级扩展项的最大数量。超出此上限的任何内容都会被忽略。

创建新的上下文菜单项。如果在创建过程中发生错误，可能要等到创建回调触发时才能检测到；详细信息将包含在 runtime.lastError 中。

要更新的属性。接受与 contextMenus.create 函数相同的值。

[ContextType, ...ContextType[]] 可选

要设为相应商品父级的商品的 ID。注意：您无法将某个项目设置为其自身后代的子项。

发生点击的标签页的详细信息。平台应用没有此参数。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "contextMenus"
  ],
  "icons": {
    "16": "icon-bitty.png",
    "48": "icon-small.png",
    "128": "icon-large.png"
  },
  ...
}
```

Example 2 (javascript):
```javascript
(info: OnClickData, tab: Tab) => {...}
```

Example 3 (unknown):
```unknown
chrome.contextMenus.create(  createProperties: CreateProperties,  callback?: function,): number | string
```

Example 4 (unknown):
```unknown
chrome.contextMenus.remove(  menuItemId: string | number,): Promise<void>
```

---

## chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabs

**Contents:**
- chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 使用场景
  - 在新标签页中打开扩展程序页面
  - 获取当前标签页
  - 将指定标签页静音
  - 点击时将当前标签页移至第一个位置
  - 将消息传递给所选标签页的内容脚本
- 扩展示例

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

Tabs API 不仅提供用于操纵和管理标签页的功能，还可以检测标签页的语言、截取屏幕截图，以及与标签页的内容脚本通信。

大多数功能无需任何权限即可使用。例如：创建新标签页、重新加载标签页、前往其他网址等。

开发者在使用 Tabs API 时应注意以下三种权限。

此权限不授予对 chrome.tabs 命名空间的访问权限。相反，它会授予扩展程序针对 tabs.Tab 实例上的四个敏感属性（url、pendingUrl、title 和 favIconUrl）调用 tabs.query() 的能力。

主机权限允许扩展程序读取和查询匹配标签页的四项敏感 tabs.Tab 属性。它们还可以使用 tabs.captureVisibleTab()、scripting.executeScript()、scripting.insertCSS() 和 scripting.removeCSS() 等方法直接与匹配的标签页互动。

activeTab 会在用户调用时授予扩展程序当前标签页的临时主机权限。与主机权限不同，activeTab 不会触发任何警告。

扩展程序的一个常见模式是在安装时在新标签页中打开初始配置页面。以下示例展示了如何执行此操作。

此示例演示了扩展程序的服务工作线程如何从当前聚焦的窗口（如果没有聚焦任何 Chrome 窗口，则从最近聚焦的窗口）检索活动标签页。这通常可以视为用户的当前标签页。

此示例展示了扩展程序如何切换指定标签页的静音状态。

此示例展示了如何在拖动可能正在进行或可能未在进行时移动标签页。虽然此示例使用 chrome.tabs.move，但您也可以将相同的等待模式用于在拖动过程中修改标签页的其他调用。

此示例演示了扩展程序的服务工作线程如何使用 tabs.sendMessage() 与特定浏览器标签页中的内容脚本进行通信。

如需查看更多 Tabs API 扩展程序演示，请探索以下任一内容：

相应标签页的静音状态以及上次状态更改的原因。

更改静音状态的扩展程序的 ID。如果扩展程序不是静音状态上次更改的原因，则不设置。

标签页是否处于静音状态（无法播放声音）。即使标签页尚未播放或当前未播放声音，也可能会处于静音状态。相当于是否显示“静音”音频指示器。

相应标签页静音或取消静音的原因。如果相应标签页的静音状态从未更改过，则不设置。

“user” 用户输入操作设置了静音状态。

“捕获” 标签页捕获已开始，强制更改为静音状态。

“extension” 由 extensionId 字段标识的扩展程序，用于设置静音状态。

相应标签页在其窗口中是否处于活动状态。不一定表示窗口已聚焦。

相应标签页在过去几秒内是否发出过声音（但如果同时处于静音状态，则可能听不到声音）。相当于“扬声器音频”指示器是否显示。

当资源不足时，浏览器是否可以自动舍弃相应标签页。

标签页是否已舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

相应标签页的网站图标的网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页正在加载，该值也可能为空字符串。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页的 ID。标签页 ID 在浏览器会话中是唯一的。在某些情况下，标签页可能未分配 ID；例如，使用 sessions API 查询外部标签页时，可能会出现会话 ID。对于应用和开发者工具窗口，标签页 ID 也可以设置为 chrome.tabs.TAB_ID_NONE。

相应标签页上次在其窗口中变为活动状态的时间（以自纪元以来经过的毫秒数表示）。

相应标签页的静音状态以及上次状态更改的原因。

打开此标签页的标签页的 ID（如果有）。仅当打开程序标签页仍然存在时，此属性才会存在。

标签页正在前往的网址（在提交之前）。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限，并且存在待处理的导航时，才会显示此属性。

请使用 tabs.Tab.highlighted。

用于唯一标识从 sessions API 获取的标签页的会话 ID。

标签页的标题。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，此属性才会存在。

相应标签页主框架的上次已提交网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页尚未提交，则可能为空字符串。另请参阅 Tab.pendingUrl。

定义如何处理标签页中的缩放更改以及在什么范围内处理。

用于在对 tabs.getZoomSettings 的调用中返回当前标签页的默认缩放级别。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

“手动” 替换自动处理缩放更改。系统仍会调度 onZoomChange 事件，扩展程序有责任监听此事件并手动缩放网页。此模式不支持 per-origin 缩放，因此会忽略 scope 缩放设置并假定为 per-tab。

“已停用” 停用标签页中的所有缩放功能。相应标签页会恢复为默认缩放级别，并且系统会忽略所有尝试进行的缩放更改。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

“按来源” 缩放更改会保留在缩放网页的来源中，也就是说，导航到同一来源的所有其他标签页也会缩放。此外，per-origin 缩放更改会与来源一起保存，这意味着当导航到同一来源中的其他网页时，这些网页都会缩放到相同的缩放系数。per-origin 范围仅在 automatic 模式下可用。

“按标签页” 缩放更改仅在此标签页中生效，其他标签页中的缩放更改不会影响此标签页的缩放。此外，per-tab 缩放比例会在导航时重置；导航标签页始终会加载具有 per-origin 缩放因子的网页。

每秒可调用 captureVisibleTab 的次数上限。captureVisibleTab 的开销很大，不应过于频繁地调用。

表示 tab_strip 中没有标签页索引的索引。

捕获指定窗口中当前活动标签页的可见区域。如需调用此方法，扩展程序必须拥有 <all_urls> 权限或 activeTab 权限。除了扩展程序通常可以访问的网站之外，此方法还允许扩展程序捕获其他受限的敏感网站，包括 chrome:-scheme 网页、其他扩展程序的网页和 data: 网址。只有拥有 activeTab 权限才能捕获这些敏感网站。只有在扩展程序获得文件访问权限后，才能捕获文件网址。

连接到指定标签页中的内容脚本。runtime.onConnect 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。如需了解详情，请参阅内容脚本消息传递。

打开由 documentId 标识的特定文档的端口，而不是标签页中的所有框架。

打开由 frameId 标识的特定框架的端口，而不是标签页中的所有框架。

传递给正在监听连接事件的内容脚本的 onConnect。

可用于与指定标签页中运行的内容脚本通信的端口。如果标签页关闭或不存在，则会触发端口的 runtime.Port 事件。

标签页是否应成为窗口中的活动标签页。不影响窗口是否处于聚焦状态（请参阅 windows.update）。默认值为 true。

标签页在窗口中应占据的位置。提供的值会限制在 0 到窗口中的标签页数量之间。

打开此标签页的标签页的 ID。如果指定，则打开程序标签页必须与新创建的标签页位于同一窗口中。

相应标签页是否应固定。默认设置为 false

相应标签页是否应成为窗口中的所选标签页。默认设置为 true

标签页最初导航到的网址。完全限定网址必须包含方案（即“http://www.google.com”，而不是“www.google.com”）。相对网址相对于扩展程序中的当前网页。默认为“新标签页”。

从内存中舍弃标签页。舍弃的标签页仍会显示在标签栏中，并在激活时重新加载。

要舍弃的标签页的 ID。如果指定了该参数，则除非标签页处于活动状态或已舍弃，否则会舍弃该标签页。如果省略，浏览器会舍弃最不重要的标签页。如果没有可舍弃的标签页，此操作可能会失败。

Promise<Tab | undefined>

Promise<Tab | undefined>

获取发出此脚本调用的标签页。如果从非标签页上下文（例如，后台网页或弹出式窗口视图）调用，则返回 undefined。

Promise<Tab | undefined>

要从中获取当前缩放系数的标签页的 ID；默认为当前窗口的活动标签页。

要从中获取当前缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

Promise<ZoomSettings>

要返回的标签页的 ID；默认为当前窗口的所选标签页。

要向前导航的标签页的 ID；默认为当前窗口的所选标签页。

将一个或多个标签页添加到指定的分组；如果未指定分组，则将给定的标签页添加到新创建的分组。

用于创建群组的配置。如果已指定 groupId，则无法使用此属性。

要将标签页添加到的群组的 ID。如果未指定，系统会创建一个新组。

number | [number, ...number[]]

要添加到指定群组的标签页 ID 或标签页 ID 列表。

突出显示给定的标签页，并将焦点放在第一个标签页上。如果指定标签页当前处于活动状态，则看起来不会执行任何操作。

Promise<windows.Window>

将一个或多个标签页移动到其窗口中的新位置，或移动到新窗口。请注意，标签页只能在普通窗口（window.type === "normal"）之间移动。

要移动的标签页 ID 或标签页 ID 列表。

要将窗口移至的位置。使用 -1 将标签页放置在窗口末尾。

获取具有指定属性的所有标签页，如果未指定属性，则获取所有标签页。

浏览器是否可以在资源不足时自动舍弃标签页。

标签页是否被舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页所在群组的 ID，或 tabGroups.TAB_GROUP_ID_NONE（对于未分组的标签页）。

标签页所在的拆分视图的 ID；如果标签页不在拆分视图中，则为 tabs.SPLIT_VIEW_ID_NONE。

根据某种模式匹配网页标题。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

根据一个或多个 网址 格式匹配标签页。片段标识符不匹配。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

父窗口的 ID，或windows.WINDOW_ID_CURRENT（表示当前窗口）。

要重新加载的标签页的 ID；默认为当前窗口的所选标签页。

要关闭的标签页 ID 或标签页 ID 列表。

向指定标签页中的内容脚本发送一条消息，并提供一个可选的回调函数，用于在收到响应时运行。runtime.onMessage 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。

要发送的消息。此消息应为可 JSON 化的对象。

向由 documentId 标识的特定文档发送消息，而不是向标签页中的所有框架发送消息。

向由 frameId 标识的特定帧发送消息，而不是向标签页中的所有帧发送消息。

要缩放的标签页的 ID；默认为当前窗口的活动标签页。

新的缩放比例。值为 0 时，标签页将设置为其当前的默认缩放比例。大于 0 的值指定了相应标签页的缩放比例（可能不是默认值）。

为指定标签页设置缩放设置，以定义如何处理缩放更改。在标签页之间切换时，这些设置会重置为默认值。

要更改缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

定义如何处理缩放更改以及在哪个范围内处理。

从相应群组中移除一个或多个标签页。如果任何组变为空组，系统会将其删除。

number | [number, ...number[]]

要从相应群组中移除的标签页 ID 或标签页 ID 列表。

修改标签页的属性。不会修改未在 updateProperties 中指定的属性。

相应标签页是否应处于有效状态。不影响窗口是否处于聚焦状态（请参阅 windows.update）。

当资源不足时，浏览器是否应自动舍弃相应标签页。

打开此标签页的标签页的 ID。如果指定，打开的标签页必须与当前标签页位于同一窗口中。

要将标签页导航到的网址。不支持 JavaScript 网址；请改用 scripting.executeScript。

Promise<Tab | undefined>

当窗口中的有效标签页发生变化时触发。请注意，此事件触发时，标签页的网址可能尚未设置，但您可以监听 onUpdated 事件，以便在网址设置时收到通知。

当标签页附加到窗口时触发；例如，当标签页在窗口之间移动时。

在创建标签页时触发。请注意，触发此事件时，标签页的网址和标签页分组会员资格可能尚未设置，但您可以监听 onUpdated 事件，以便在设置网址或将标签页添加到标签页分组时收到通知。

当标签页从窗口分离时触发；例如，当标签页在窗口之间移动时。

当窗口中突出显示或选定的标签页发生变化时触发。

当标签页在窗口内移动时触发。系统只会触发一个移动事件，表示用户直接移动的标签页。对于必须响应手动移动的标签页而移动的其他标签页，不会触发移动事件。当标签页在窗口之间移动时，不会触发此事件；如需了解详情，请参阅 tabs.onDetached。

如果标签页因其父窗口关闭而关闭，则为 True。

在标签页因预渲染或即时而替换为另一个标签页时触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "tabs"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "http://*/*",
    "https://*/*"
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "activeTab"
  ],
  ...
}
```

Example 4 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(({reason}) => {
  if (reason === 'install') {
    chrome.tabs.create({
      url: "onboarding.html"
    });
  }
});
```

---

## chrome.system.display 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/display?hl=zh-cn

**Contents:**
- chrome.system.display 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ActiveState
    - 枚举
  - Bounds
    - 属性
  - DisplayLayout
    - 属性

使用 system.display API 查询展示元数据。

一个枚举，用于指示显示屏是否被系统检测到并使用。如果显示屏未被系统检测到（可能已断开连接，或因休眠模式等原因而被视为已断开连接），则会被视为“不活跃”。此状态用于在所有显示屏断开连接时保留现有显示屏，例如。

显示屏沿连接边缘的偏移量。0 表示最上角或最左角对齐。

父显示屏的唯一标识符。如果这是根，则为空。

此显示相对于父级的布局位置。对于根，此属性将被忽略。

显示模式高度（以设备无关的像素为单位，用户可见）。

如果此模式为隔行扫描模式，则为 true；如果未提供，则为 false。

如果模式是显示屏的原生模式，则为 true。

如果当前选择了相应显示模式，则为 true。

显示模式宽度（以设备无关的 [用户可见] 像素为单位）。

如果设置，则更新显示屏沿 x 轴的逻辑边界原点。与 boundsOriginY 一起应用。如果未设置且设置了 boundsOriginY，则默认为当前值。请注意，更新显示原点时，系统会应用一些限制，因此最终的边界原点可能与设置的原点不同。可以使用 getInfo 检索最终边界。无法在主显示屏上更改边界原点。

如果设置，则更新显示屏沿 y 轴的逻辑边界原点。请参阅 boundsOriginX 参数的文档。

如果设置了此值，则将显示模式更新为与此值匹配的模式。如果其他参数无效，则不会应用此参数。如果显示模式无效，系统将不会应用该模式，并会设置错误，但仍会应用其他属性。

如果已设置，则更新与显示屏关联的缩放。此缩放功能会重新布局和重绘，因此与仅执行逐像素拉伸放大相比，可实现更高质量的缩放。

如果设为 true，则将显示屏设为主显示屏。如果设置为 false，则不执行任何操作。注意：如果设置了此属性，则显示屏会被视为所有其他属性的主要显示屏（即，可以设置 isUnified，但可能无法设置边界原点）。

仅限 ChromeOS。如果设置为 true，则将显示模式更改为统一桌面（有关详情，请参阅 enableUnifiedDesktop）。如果此政策设为 false，系统将停用统一桌面模式。此设置仅对主显示屏有效。如果提供了 mirroringSourceId，则不得提供 sourceId，并且系统会忽略其他属性。如果未提供，则不会产生任何影响。

仅限 ChromeOS。如果已设置且不为空，则仅为此显示屏启用镜像。否则，会针对所有显示屏停用镜像功能。此值应指明要镜像的源显示屏的 ID，不得与传递给 setDisplayProperties 的 ID 相同。如果设置了该属性，则不得设置任何其他属性。

如果设置，则将显示屏的过扫描边衬区设置为提供的值。请注意，过扫描值不得为负数，也不得大于屏幕尺寸的一半。无法在内置显示器上更改过扫描。

如果已设置，则更新显示屏的旋转。合法值为 [0, 90, 180, 270]。旋转方向设置为顺时针，相对于显示屏的竖屏位置。

显示屏的当前缩放比例与默认缩放比例之间的比率。例如，值 1 相当于 100% 缩放，值 1.5 相当于 150% 缩放。

注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

如果此显示屏关联了触摸输入设备，则为 True。

如果相应显示处于启用状态，则为 true。

在统一桌面模式下，所有显示屏均为 true。请参阅 enableUnifiedDesktop 的文档。

仅限 ChromeOS。来源显示屏所镜像到的显示屏的标识符。如果未镜像任何显示屏，则为空。所有显示屏的此属性都将设置为相同的值。不得包含 mirroringSourceId。

仅限 ChromeOS。如果启用了镜像，则为正在镜像的显示屏的标识符；否则为空。此设置将应用于所有显示屏（包括正在镜像的显示屏）。

可用显示模式的列表。当前模式的 isSelected 将为 true。仅适用于 ChromeOS。在其他平台上，此属性将设置为一个空数组。

易记名称（例如“HP LCD 显示器”）。

显示屏在其屏幕边界内的边衬区。目前仅在 ChromeOS 上公开。在其他平台上将设置为空边衬区。

显示屏相对于竖屏位置的顺时针旋转角度（以度为单位）。目前仅在 ChromeOS 上公开。在其他平台上将设置为 0。如果值为 -1，则表示当设备处于实体平板电脑状态时，自动旋转屏幕。

显示屏边界内的可用工作区。工作区不包括为操作系统预留的显示区域，例如任务栏和启动器。

3 字符制造商代码。请参阅第 3.4.1 节第 21 页。在 v1.4 中为必需。

2 字节制造商分配的代码，第 3.4.2 节，第 21 页。在 v1.4 中为必需。

制造商年份，第 3.4.4 条，第 22 页。在 v1.4 中为必需。

如果设置为 true，则在统一桌面模式下，getInfo 将仅返回一个 DisplayUnitInfo（请参阅 enableUnifiedDesktop）。默认值为 false。

布局位置，即显示屏所连接到的父元素的边缘。

镜像模式，即显示屏镜像到其他显示屏的不同方式。

“关闭” 指定默认模式（扩展桌面或统一桌面）。

“normal” 指定默认来源显示将镜像到所有其他显示屏。

“混合” 指定将指定的来源显示屏镜像到所提供的目标显示屏。所有其他已连接的显示屏将显示扩展内容。

镜像目标显示屏的 ID。此值仅适用于“混合”。

镜像源显示屏的 ID。此值仅适用于“混合”。

通过清除与显示屏关联的所有触控校准数据，重置显示屏的触控校准并将其恢复为默认状态。

为显示屏设置触控校准对。这些 pairs 将用于校准触摸屏，以在 startCustomTouchCalibration() 中调用 id 时进行显示。请务必在调用此方法之前调用 startCustomTouchCalibration。如果已在进行其他触控校准，则会抛出错误。

TouchCalibrationPairQuad

执行触控校准时的显示屏边界。系统会忽略 bounds.left 和 bounds.top 值。

启用/停用统一桌面功能。如果在镜像处于有效状态时启用，桌面模式将不会更改，直到镜像关闭。否则，桌面模式将立即切换到统一模式。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

请求所有显示屏的布局信息。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

Promise<DisplayLayout[]>

Promise<DisplayUnitInfo[]>

调整显示器的当前过扫描边衬区。通常，这应该会使显示沿某个轴移动（例如，左侧和右侧具有相同的值），或者沿某个轴缩放（例如，顶部和底部具有相反的值）。自开始以来，每次 Adjust 调用都会累积之前调用的结果。

通过保存当前值并隐藏叠加层，完成显示屏的过扫描调整。

将显示屏的过扫描边衬区重置为上次保存的值（即在调用 Start 之前的值）。

为显示屏启动过扫描校准。这会在屏幕上显示一个叠加层，指示当前过扫描边衬区。如果显示屏 id 的过扫描校准正在进行，此方法将重置校准。

为所有显示屏设置布局。未包含的任何显示屏都将使用默认布局。如果布局会重叠或以其他方式无效，系统会将其调整为有效布局。布局解析完毕后，系统会触发 onDisplayChanged 事件。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

布局信息，除主显示屏之外的所有显示屏都需要此信息。

根据 info 中提供的信息，更新 id 指定的显示屏的属性。如果失败，系统会设置 runtime.lastError。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

应更改的显示属性的相关信息。只有当 info 中指定了属性的新值时，该属性才会发生变化。

将显示模式设置为指定的镜像模式。每次调用都会重置之前调用中的状态。对于镜像目标显示屏，调用 setDisplayProperties() 将会失败。注意：此功能仅适用于 ChromeOS Kiosk 应用和 Web 界面。

显示以 id 为显示屏 ID 的显示屏的原生触控校准用户体验。屏幕上会显示一个叠加层，其中包含有关如何继续操作的必要说明。只有在校准成功时才会调用回调。如果校准失败，则会抛出错误。

为显示屏启动自定义触控校准。当使用自定义用户体验来收集校准数据时，应调用此方法。如果已在进行其他触控校准，则会抛出错误。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.display.clearTouchCalibration(  id: string,): void
```

Example 2 (unknown):
```unknown
chrome.system.display.completeCustomTouchCalibration(  pairs: TouchCalibrationPairQuad,  bounds: Bounds,): void
```

Example 3 (unknown):
```unknown
chrome.system.display.enableUnifiedDesktop(  enabled: boolean,): void
```

Example 4 (unknown):
```unknown
chrome.system.display.getDisplayLayout(): Promise<DisplayLayout[]>
```

---

## chrome.notifications 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/notifications

**Contents:**
- chrome.notifications 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - NotificationBitmap
  - NotificationButton
    - 属性
  - NotificationItem
    - 属性
  - NotificationOptions

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

应用图标遮罩不会向 Mac OS X 用户显示。

应用图标遮罩的网址。网址的限制与 iconUrl 相同。

应用图标遮罩应位于 Alpha 渠道中，因为系统只会考虑图片的 Alpha 渠道。

NotificationButton[] 可选

与通知关联的时间戳，以自纪元以来经过的毫秒数表示（例如 Date.now() + n）。

指向发件人头像、应用图标或图片通知缩略图的网址。

网址可以是数据网址、Blob 网址，也可以是相对于此扩展程序的 .crx 文件中资源的网址

**注意：**notifications.create() 方法需要此值。

指向图片类型通知的图片缩略图的网址。网址的限制与 iconUrl 相同。

自 Chrome 67 起，此界面提示会被忽略

NotificationItem[] 可选

用于多项通知的商品。Mac OS X 用户只能看到第一个项目。

**注意：**notifications.create() 方法需要此值。

优先级范围为 -2 到 2。-2 是最低优先级。2 为最高值。默认值为零。在不支持通知中心的平台（Windows、Linux 和 Mac）上，-2 和 -1 会导致错误，因为具有这些优先级的通知根本不会显示。

表示通知应一直显示在屏幕上，直到用户激活或关闭通知。此属性的默认值为 false。

表示在显示通知时不应发出任何声音或振动。此属性的默认值为 false。

**注意：**notifications.create() 方法需要此值。

要显示的通知类型。notifications.create 方法的必需参数。

“granted” 指定用户已选择显示来自应用或扩展程序的通知。这是安装时的默认设置。

“拒绝” 指定用户已选择不显示来自应用或扩展程序的通知。

“基本” 包含图标、标题、消息、expandedMessage 和最多两个按钮。

“image” 包含一个图标、标题、消息、expandedMessage、图片和最多两个按钮。

“list” 包含图标、标题、消息、项和最多两个按钮。Mac OS X 用户只能看到第一项。

“progress” 包含图标、标题、消息、进度和最多两个按钮。

要清除的通知的 ID。由 notifications.create 方法返回。

通知的标识符。如果未设置或为空，系统会自动生成 ID。如果与现有通知匹配，此方法会先清除该通知，然后再继续执行创建操作。标识符的长度不得超过 500 个字符。

在 Chrome 42 之前，notificationId 参数是必需的。

检索用户是否已启用来自相应应用或扩展程序的通知。

Promise<PermissionLevel>

要更新的通知的 ID。由 notifications.create 方法返回。

用户更改了权限级别。自 Chrome 47 起，只有 ChromeOS 具有可调度此事件的界面。

用户点击了应用通知设置的链接。自 Chrome 47 起，只有 ChromeOS 具有可调度此事件的界面。自 Chrome 65 起，该界面也已从 ChromeOS 中移除。

**Examples:**

Example 1 (unknown):
```unknown
chrome.notifications.clear(  notificationId: string,): Promise<boolean>
```

Example 2 (unknown):
```unknown
chrome.notifications.create(  notificationId?: string,  options: NotificationOptions,): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.notifications.getAll(): Promise<object>
```

Example 4 (unknown):
```unknown
chrome.notifications.getPermissionLevel(): Promise<PermissionLevel>
```

---

## chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/sessions?hl=zh-cn

**Contents:**
- chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - Device
    - 属性
  - Filter
    - 属性
  - Session
    - 属性

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

外部设备的打开窗口会话列表，按会话的修改时间从最近到最远排序。

相应列表中要提取的条目数上限。省略此参数可提取最大条目数 (sessions.MAX_SESSION_RESULTS)。

窗口或标签页关闭或修改的时间，以自纪元开始算起的秒数表示。

如果相应条目描述的是标签页，则为 tabs.Tab。系统会设置此值或 sessions.Session.window。

如果相应条目描述的是窗口，则为 windows.Window。系统会设置此值或 sessions.Session.tab。

请求的列表中将包含的 sessions.Session 的数量上限。

重新打开 windows.Window 或 tabs.Tab，并提供一个可选的回调函数，用于在条目恢复后运行。

要恢复的 windows.Window.sessionId 或 tabs.Tab.sessionId。如果未指定此参数，系统会恢复最近关闭的会话。

当最近关闭的标签页和/或窗口发生更改时触发。此事件不会监控同步会话更改。

**Examples:**

Example 1 (unknown):
```unknown
chrome.sessions.getDevices(  filter?: Filter,): Promise<Device[]>
```

Example 2 (unknown):
```unknown
chrome.sessions.getRecentlyClosed(  filter?: Filter,): Promise<Session[]>
```

Example 3 (unknown):
```unknown
chrome.sessions.restore(  sessionId?: string,): Promise<Session>
```

Example 4 (unknown):
```unknown
chrome.sessions.onChanged.addListener(  callback: function,)
```

---

## chrome.extension 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/extension

**Contents:**
- chrome.extension 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 类型
  - ViewType
    - 枚举
- 属性
  - inIncognitoContext
    - 类型
- 方法
  - getBackgroundPage()

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

对于在无痕式标签页中运行的内容脚本以及在无痕式进程中运行的扩展程序网页，此属性为 true。后者仅适用于具有“split”incognito_behavior 的扩展程序。

返回在当前扩展程序内运行的后台网页的 JavaScript“window”对象。如果扩展程序没有背景页面，则返回 null。

返回一个 JavaScript“window”对象数组，其中包含当前扩展程序中运行的每个网页。

根据标签页 ID 查找视图。如果省略此字段，则返回所有视图。

要获取的视图的类型。如果省略，则返回所有视图（包括后台网页和标签页）。

限制搜索范围的窗口。如果省略，则返回所有视图。

检索扩展程序对“file://”方案的访问状态。此设置对应于用户控制的“允许访问文件网址”设置，可通过 chrome://extensions 页面访问。

检索扩展程序对无痕模式的访问权限状态。此设置对应于用户控制的“允许在无痕模式下运行”扩展程序级设置，可通过 chrome://extensions 页面访问。

设置扩展程序更新网址中使用的 ap CGI 参数的值。对于托管在 Chrome 扩展程序库中的扩展程序，系统会忽略此值。

**Examples:**

Example 1 (unknown):
```unknown
chrome.extension.getBackgroundPage(): Window | undefined
```

Example 2 (unknown):
```unknown
chrome.extension.getViews(  fetchProperties?: object,): Window[]
```

Example 3 (unknown):
```unknown
chrome.extension.isAllowedFileSchemeAccess(): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.extension.isAllowedIncognitoAccess(): Promise<boolean>
```

---

## chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/certificateProvider?hl=zh-cn

**Contents:**
- chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Algorithm
    - 枚举
  - CertificateInfo
    - 属性

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用此 API 向 ChromeOS 公开客户端证书的典型步骤如下：

实际步骤顺序可能会有所不同。例如，如果使用自动选择证书的企业政策，系统就不会要求用户选择证书（请参阅 AutoSelectCertificateForUrls 和面向用户的 Chrome 政策）。

"RSASSA_PKCS1_v1_5_MD5_SHA1" 指定采用 MD5-SHA-1 哈希的 RSASSA PKCS#1 v1.5 签名算法。扩展程序不得预先添加 DigestInfo 前缀，而只能添加 PKCS#1 填充。此算法已被弃用，自版本 109 起，Chrome 将不再请求使用此算法。

"RSASSA_PKCS1_v1_5_SHA1" 指定使用 SHA-1 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA256" 指定使用 SHA-256 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA384" 指定使用 SHA-384 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA512" 指定使用 SHA-512 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

“RSASSA_PSS_SHA256” 指定 RSASSA PSS 签名算法，使用 SHA-256 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。

"RSASSA_PSS_SHA384" 指定 RSASSA PSS 签名算法，该算法使用 SHA-384 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。

“RSASSA_PSS_SHA512” 指定 RSASSA PSS 签名算法，该算法使用 SHA-512 哈希函数、MGF1 掩码生成函数以及与哈希大小相同的盐。

必须是 X.509 证书的 DER 编码。目前仅支持使用 RSA 密钥的证书。

必须设置为相应证书支持的所有哈希。此扩展程序只会要求对使用这些哈希算法之一计算出的摘要进行签名。应按哈希偏好程度降序排列。

要传递给 setCertificates 的请求标识符。

该数组必须包含 X.509 客户端证书的 DER 编码作为其第一个元素。

相应证书支持的所有算法。系统只会要求扩展程序使用这些算法之一进行签名。

“MD5_SHA1” 指定 MD5 和 SHA1 哈希算法。

“SHA256” 指定 SHA256 哈希处理算法。

“SHA384” 指定 SHA384 哈希处理算法。

“SHA512” 指定 SHA512 哈希算法。

可通过 requestPin 函数向用户显示的错误类型。

“INVALID_PIN” 指定 PIN 码无效。

“INVALID_PUK” 指定 PUK 无效。

“MAX_ATTEMPTS_EXCEEDED” 指定已超出最大尝试次数。

“UNKNOWN_ERROR” 指定错误无法用上述类型表示。

扩展程序通过 requestPin 函数请求的代码类型。

“PIN 码” 指定所请求的代码是 PIN 码。

用户提供的代码。如果用户关闭了对话框或发生了其他错误，则为空。

通过 onSignatureRequested 事件接收到的请求标识符。

剩余尝试次数。提供此信息是为了让任何界面都能向用户显示此信息。Chrome 不会强制执行此操作，而是当 PIN 码请求数超出时，扩展程序应调用 stopPinRequest 并将 errorType 设置为 MAX_ATTEMPTS_EXCEEDED。

PinRequestErrorType 可选

向用户显示的错误模板。如果之前的请求失败，则应设置此参数，以将失败原因通知给用户。

所请求的验证码类型。默认值为 PIN 码。

Chrome 在 SignRequest 中提供的 ID。

在响应 onCertificatesUpdateRequested 时调用，应包含收到的 certificatesRequestId 值。否则，应取消设置。

ClientCertificateInfo[]

提取证书时发生的错误（如果有）。系统会在适当的时候向用户显示此错误。

X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 input 进行签名。

要签名的数据。请注意，数据未经过哈希处理。

要传递给 reportSignature 的请求标识符。

X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 digest 进行签名。

供扩展程序使用的唯一 ID，如果扩展程序需要调用需要此 ID 的方法（例如 requestPin），则应使用此 ID。

PinRequestErrorType 可选

错误模板。如果存在，则会向用户显示。旨在包含因错误而停止流程的原因，例如 MAX_ATTEMPTS_EXCEEDED。

Chrome 在 SignRequest 中提供的 ID。

应作为对 onSignatureRequested 的响应进行调用。

扩展程序必须最终为每个 onSignatureRequested 事件调用此函数；API 实现会在一段时间后停止等待此调用，并在调用此函数时以超时错误进行响应。

ReportSignatureDetails

向用户请求 PIN 码。一次只能有一个正在进行的请求。在另一个流程正在进行时发出的请求会被拒绝。如果另一个流程正在进行中，扩展程序应负责稍后重试。

Promise<PinResponseDetails | undefined>

扩展程序应在初始化后以及当前可用证书集发生每次更改时调用此函数。扩展程序还应在每次收到此事件时，调用此函数以响应 onCertificatesUpdateRequested。

SetCertificatesDetails

停止由 requestPin 函数启动的 PIN 码请求。

StopPinRequestDetails

如果通过 setCertificates 设置的证书不足，或者浏览器请求更新后的信息，则会触发此事件。扩展程序必须使用更新后的证书列表和收到的 certificatesRequestId 调用 setCertificates。

CertificatesUpdateRequest

每次浏览器需要使用此扩展程序通过 setCertificates 提供的证书对消息进行签名时，都会触发此事件。

扩展程序必须使用适当的算法和私钥对来自 request 的输入数据进行签名，并通过使用收到的 signRequestId 调用 reportSignature 来返回签名。

**Examples:**

Example 1 (javascript):
```javascript
function collectAvailableCertificates() {
  // Return all certificates that this Extension can currently provide.
  // For example:
  return [{
    certificateChain: [new Uint8Array(...)],
    supportedAlgorithms: ['RSASSA_PKCS1_v1_5_SHA256']
  }];
}

// The Extension calls this function every time the currently available list of
// certificates changes, and also once after the Extension's initialization.
function onAvailableCertificatesChanged() {
  chrome.certificateProvider.setCertificates({
    clientCertificates: collectAvailableCertificates()
  });
}

function handleCertificatesUpdateRequest(request) {
  // Report the currently available certificates as a response to the request
  // event. This is important for supporting the case when the Extension is
  // unable to detect the changes proactively.
  chrome.certificateProvider.setCertificates({
    certificatesRequestId: request.certificatesRequestId,
    clientCertificates: collectAvailableCertificates()
  });
}

// Returns a private key handle for the given DER-encoded certificate.
// |certificate| is an ArrayBuffer.
function getPrivateKeyHandle(certificate) {...}

// Digests and signs |input| with the given private key. |input| is an
// ArrayBuffer. |algorithm| is an Algorithm.
// Returns the signature as ArrayBuffer.
function signUnhashedData(privateKey, input, algorithm) {...}

function handleSignatureRequest(request) {
  // Look up the handle to the private key of |request.certificate|.
  const key = getPrivateKeyHandle(request.certificate);
  if (!key) {
    // Handle if the key isn't available.
    console.error('Key for requested certificate no available.');

    // Abort the request by reporting the error to the API.
    chrome.certificateProvider.reportSignature({
      signRequestId: request.signRequestId,
      error: 'GENERAL_ERROR'
    });
    return;
  }

  const signature = signUnhashedData(key, request.input, request.algorithm);
  chrome.certificateProvider.reportSignature({
    signRequestId: request.signRequestId,
    signature: signature
  });
}

chrome.certificateProvider.onCertificatesUpdateRequested.addListener(
    handleCertificatesUpdateRequest);
chrome.certificateProvider.onSignatureRequested.addListener(
    handleSignatureRequest);
```

Example 2 (unknown):
```unknown
chrome.certificateProvider.reportSignature(  details: ReportSignatureDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.certificateProvider.requestPin(  details: RequestPinDetails,): Promise<PinResponseDetails | undefined>
```

Example 4 (unknown):
```unknown
chrome.certificateProvider.setCertificates(  details: SetCertificatesDetails,): Promise<void>
```

---

## chrome.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/platformKeys

**Contents:**
- chrome.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ClientCertificateRequest
    - 属性
  - ClientCertificateType
    - 枚举
  - Match

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

服务器允许的证书授权机构的标识名列表。每个条目都必须是 DER 编码的 X.509 DistinguishedName。

ClientCertificateType[]

此字段是所请求证书类型的列表，按服务器的偏好排序。系统只会检索此列表中包含的类型的证书。不过，如果 certificateTypes 是空列表，则会返回任何类型的证书。

经过认证的密钥的 KeyAlgorithm。这包含证书密钥固有的算法参数（例如密钥长度）。其他参数（例如 sign 函数使用的哈希函数）未包含在内。

如果指定，则 selectClientCertificates 会对该列表进行操作。否则，从平台可供此扩展程序使用的证书存储区中获取所有证书的列表。系统会移除扩展程序无权访问或与请求不匹配的条目。

如果为 true，系统会向用户显示过滤后的列表，以便用户手动选择证书，从而授予扩展程序对证书和密钥的访问权限。系统只会返回所选证书。如果为 false，则列表会缩减为扩展程序已获得访问权限（自动或手动）的所有证书。

ClientCertificateRequest

要验证证书的服务器的主机名，例如提供 serverCertificateChain 的服务器。

每个链条条目都必须是 X.509 证书的 DER 编码，第一个条目必须是服务器证书，并且每个条目都必须证明其前面的条目。

如果信任验证失败，此数组会包含底层网络层报告的错误。否则，此数组为空。

注意：此列表仅用于调试，可能未包含所有相关错误。返回的错误可能会在此 API 的未来修订版本中发生变化，并且无法保证向前或向后兼容。

信任验证的结果：如果能够建立对指定验证详细信息的信任，则为 true；如果因任何原因拒绝信任，则为 false。

将 certificate 的密钥对传递给 callback，以便与 platformKeys.subtleCrypto 搭配使用。

由 selectClientCertificates 返回的 Match 的证书。

除了密钥本身固定的参数之外，还确定签名/哈希算法参数。接受与 WebCrypto 的 importKey 函数相同的参数，例如 RSASSA-PKCS1-v1_5 密钥的 RsaHashedImportParams 和 EC 密钥的 EcKeyImportParams。此外，对于 RSASSA-PKCS1-v1_5 密钥，可以使用以下值之一指定哈希算法名称参数：“none”“SHA-1”“SHA-256”“SHA-384”或“SHA-512”，例如 {"hash": { "name": "none" } }。然后，签名函数将应用 PKCS#1 v1.5 填充，但不会对指定数据进行哈希处理。

目前，此方法仅支持“RSASSA-PKCS1-v1_5”和“ECDSA”算法。

如果相应扩展程序无权访问该属性，则可能为 null。

将 publicKeySpkiDer 标识的密钥对传递给 callback，以供 platformKeys.subtleCrypto 使用。

以 DER 编码的 X.509 SubjectPublicKeyInfo，例如通过调用 WebCrypto 的 exportKey 函数并指定 format="spki" 来获取。

除了密钥本身固定的参数之外，还提供签名和哈希算法参数。接受与 WebCrypto 的 importKey 函数相同的参数，例如 RSASSA-PKCS1-v1_5 密钥的 RsaHashedImportParams。对于 RSASSA-PKCS1-v1_5 密钥，我们还需要传递一个“哈希”参数 { "hash": { "name": string } }。“hash”参数表示在签名之前用于摘要操作的哈希算法的名称。您可以将“none”作为哈希名称进行传递，在这种情况下，签名函数将应用 PKCS#1 v1.5 填充，但不会对指定数据进行哈希处理。

目前，此方法支持以下算法：“ECDSA”算法（采用命名曲线 P-256）和“RSASSA-PKCS1-v1_5”算法（采用哈希算法“none”“SHA-1”“SHA-256”“SHA-384”和“SHA-512”之一）。

如果相应扩展程序无权访问该属性，则可能为 null。

此方法会从客户端证书列表中过滤出平台已知的、与 request 匹配的证书，以及扩展程序有权访问这些证书及其私钥的证书。如果 interactive 为 true，系统会向用户显示一个对话框，用户可以在其中选择匹配的证书，并授予扩展程序对该证书的访问权限。所选/过滤的客户端证书将传递给 callback。

WebCrypto 的 SubtleCrypto 的一种实现，允许对可供此扩展程序使用的客户端证书的密钥执行加密操作。

根据平台的信任设置，检查 details.serverCertificateChain 是否可信，以用于 details.hostname。注意：信任验证的实际行为并未完全指定，未来可能会发生变化。API 实现会验证证书失效情况、验证证书路径，并通过已知 CA 检查信任情况。该实现应遵循 EKU serverAuth 并支持主题备用名称。

Promise<VerificationResult>

**Examples:**

Example 1 (unknown):
```unknown
chrome.platformKeys.getKeyPair(  certificate: ArrayBuffer,  parameters: object,  callback: function,): void
```

Example 2 (javascript):
```javascript
(publicKey: object, privateKey?: object) => void
```

Example 3 (unknown):
```unknown
chrome.platformKeys.getKeyPairBySpki(  publicKeySpkiDer: ArrayBuffer,  parameters: object,  callback: function,): void
```

Example 4 (javascript):
```javascript
(publicKey: object, privateKey?: object) => void
```

---

## chrome.wallpaper 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/wallpaper?hl=zh-cn

**Contents:**
- chrome.wallpaper 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
- 类型
  - WallpaperLayout
    - 枚举
- 方法
  - setWallpaper()

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

您必须在应用的清单中声明“壁纸”权限，才能使用壁纸 API。例如：

例如，如需将壁纸设置为 https://example.com/a_file.png 中的图片，您可以按如下方式调用 chrome.wallpaper.setWallpaper：

将壁纸设置为 url 或 wallpaperData 中的图片，并采用指定的布局

以 ArrayBuffer 形式表示的 JPEG 或 PNG 编码壁纸图片。

如果应生成 128x60 缩略图，则为 True。尚不支持布局和宽高比。

Promise<ArrayBuffer | undefined>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "wallpaper"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.wallpaper.setWallpaper(
  {
    'url': 'https://example.com/a_file.jpg',
    'layout': 'CENTER_CROPPED',
    'filename': 'test_wallpaper'
  },
  function() {}
);
```

Example 3 (unknown):
```unknown
chrome.wallpaper.setWallpaper(  details: object,): Promise<ArrayBuffer | undefined>
```

---

## chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/browsingData

**Contents:**
- chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 特定来源
  - 来源类型
- 示例
- 类型
  - DataTypeSet
    - 属性

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

您必须在扩展程序清单中声明 "browsingData" 权限，才能使用此 API。

此 API 最简单的使用场景是用于清除用户浏览数据的基于时间的机制。您的代码应提供一个时间戳，用于指明历史日期，在此日期之后的用户浏览数据应被移除。此时间戳的格式为自 Unix 纪元以来的毫秒数（可以使用 getTime() 方法从 JavaScript Date 对象中检索）。

例如，如需清除用户过去一周的所有浏览数据，您可以编写如下代码：

借助 chrome.browsingData.remove() 方法，您只需一次调用即可移除各种类型的浏览数据，这比调用多个更具体的方法要快得多。不过，如果您只想清除一种特定的浏览数据（例如 Cookie），那么更精细的方法可提供一种可读的替代方案，而无需使用包含 JSON 的调用。

如果用户正在同步数据，chrome.browsingData.remove() 可能会在清除同步账号的 Cookie 后自动重建该 Cookie。这是为了确保同步功能可以继续正常运行，以便最终在服务器上删除数据。不过，更具体的 chrome.browsingData.removeCookies() 可用于清除同步账号的 Cookie，在这种情况下，同步会暂停。

如需移除特定来源的数据或排除一组来源而不进行删除，您可以使用 RemovalOptions.origins 和 RemovalOptions.excludeOrigins 参数。它们只能应用于 Cookie、缓存和存储空间（CacheStorage、FileSystems、IndexedDB、LocalStorage、ServiceWorkers 和 WebSQL）。

通过向 API 的 options 对象添加 originTypes 属性，您可以指定应影响哪些类型的来源。来源分为三类：

我们可以调整上一个示例，以便仅移除受保护网站中的数据，如下所示：

如需试用此 API，请从 chrome-extension-samples 代码库中安装 browsingData API 示例。

一组数据类型。缺失的数据类型会被解读为 false。

已移除通过扩展程序删除密码的功能。系统会忽略此数据类型。

已移除对 Flash 的支持。系统会忽略此数据类型。

已移除对服务器绑定证书的支持。系统会忽略此数据类型。

如果存在，则此列表中的来源对应的数据不会被删除。不能与 origins 结合使用。仅支持 Cookie、存储空间和缓存。整个可注册网域都会排除 Cookie。

一个对象，其属性用于指定应清除哪些来源类型。如果未指定此对象，则默认仅清除“不受保护”的来源。在添加“protectedWeb”或“extensions”之前，请确保您确实要移除应用数据。

用户已安装的扩展程序和打包应用（请务必谨慎使用！）。

[string, ...string[]] 可选

如果存在，则仅删除此列表中的来源的数据。仅支持 Cookie、存储空间和缓存。系统会清除整个可注册网域的 Cookie。

移除自相应日期（以自纪元开始算起的毫秒数表示，可通过 JavaScript Date 对象的 getTime 方法访问）起累积的数据。如果未提供，则默认为 0（这将移除所有浏览数据）。

清除用户个人资料中存储的各种类型的浏览数据。

清除在特定时间范围内修改的浏览器 Cookie 和服务器绑定证书。

清除浏览器中的已下载文件列表（不清除已下载的文件本身）。

已移除通过扩展程序删除密码的功能。此函数无效。

已移除对 Flash 的支持。此函数无效。

报告“清除浏览数据”设置界面中当前选择的数据类型。注意：此 API 中包含的某些数据类型在设置界面中不可用，并且某些界面设置可控制此处列出的多种数据类型。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "browsingData",
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var callback = function () {
  // Do something clever here once data has been removed.
};

var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;
var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
chrome.browsingData.remove({
  "since": oneWeekAgo
}, {
  "appcache": true,
  "cache": true,
  "cacheStorage": true,
  "cookies": true,
  "downloads": true,
  "fileSystems": true,
  "formData": true,
  "history": true,
  "indexedDB": true,
  "localStorage": true,
  "passwords": true,
  "serviceWorkers": true,
  "webSQL": true
}, callback);
```

Example 3 (unknown):
```unknown
var callback = function () {
  // Do something clever here once data has been removed.
};

var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;
var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
chrome.browsingData.removeCookies({
  "since": oneWeekAgo
}, callback);
```

Example 4 (unknown):
```unknown
chrome.browsingData.remove({
  "origins": ["https://www.example.com"]
}, {
  "cacheStorage": true,
  "cookies": true,
  "fileSystems": true,
  "indexedDB": true,
  "localStorage": true,
  "serviceWorkers": true,
  "webSQL": true
}, callback);
```

---

## chrome.system.cpu 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/cpu

**Contents:**
- chrome.system.cpu 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - CpuInfo
    - 属性
  - CpuTime
    - 属性
  - ProcessorInfo
    - 属性

使用 system.cpu API 查询 CPU 元数据。

一组表示处理器部分功能的特征码。目前支持的代码包括“mmx”“sse”“sse2”“sse3”“ssse3”“sse4_1”“sse4_2”和“avx”。

来自 CPU 各个散热区的 CPU 温度读数列表。温度以摄氏度为单位。

相应处理器的总累计时间。此值等于用户 + 内核 + 空闲。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.cpu.getInfo(): Promise<CpuInfo>
```

---

## chrome.tabCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabCapture

**Contents:**
- chrome.tabCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 保留系统音频
  - 数据流 ID
  - 使用限制
  - 了解详情
- 类型
  - CaptureInfo

使用 chrome.tabCapture API 与标签页媒体流进行互动。

借助 chrome.tabCapture API，您可以访问包含当前标签页的视频和音频的 MediaStream。只有在用户调用扩展程序后（例如通过点击扩展程序的操作按钮），才能调用此方法。这类似于 "activeTab" 权限的行为。

当标签页获得 MediaStream 时，该标签页中的音频将不再向用户播放。这类似于当 suppressLocalAudioPlayback 标志设为 true 时 getDisplayMedia() 函数的行为。

这会创建一个新的 AudioContext，并将标签页 MediaStream 的音频连接到默认目的地。

调用 chrome.tabCapture.getMediaStreamId() 将返回一个流 ID。如需稍后通过 ID 访问 MediaStream，请使用以下代码：

调用 getMediaStreamId() 后，返回的流 ID 的使用范围会受到限制：

在 Chrome 116 之前，如果未指定 consumerTabId，则流 ID 会同时受调用方的安全来源、渲染进程和渲染框架的限制。

如需详细了解如何使用 chrome.tabCapture API，请参阅音频录制和屏幕捕获。此示例演示了如何使用 tabCapture 及相关 API 来解决一些常见用例。

MediaStreamConstraint 可选

MediaStreamConstraint 可选

稍后将调用 getUserMedia() 来使用该流的标签页的可选标签页 ID。如果未指定，则生成的流只能由调用扩展程序使用。该数据流只能由给定标签页中安全来源与消费者标签页来源相匹配的框架使用。标签页的来源必须是安全来源，例如 HTTPS。

要捕获的标签页的可选标签页 ID。如果未指定，则选择当前活动标签页。只有扩展程序已获得 activeTab 权限的标签页才能用作目标标签页。

捕获当前活动标签页的可见区域。只有在扩展程序被调用后，才能在当前活跃标签页上开始捕获，这与 activeTab 的工作方式类似。在标签页内进行网页导航时，捕获会一直保持，直到标签页关闭或扩展程序关闭媒体流时才会停止。

返回已请求捕获或正在捕获的标签页的列表，即状态不为“已停止”且状态不为“错误”的标签页。这样一来，扩展程序就可以告知用户当前存在标签页捕获，这会阻止新的标签页捕获成功完成（或防止对同一标签页发出冗余请求）。

Promise<CaptureInfo[]>

创建用于捕获目标标签页的流 ID。与 chrome.tabCapture.capture() 方法类似，但会向消费者标签页返回媒体流 ID，而不是媒体流。

GetMediaStreamOptions 可选

当标签页的捕获状态发生变化时触发的事件。这样，扩展程序作者就可以跟踪标签页的捕获状态，以使界面元素（例如网页操作）保持同步。

**Examples:**

Example 1 (javascript):
```javascript
const output = new AudioContext();
const source = output.createMediaStreamSource(stream);
source.connect(output.destination);
```

Example 2 (unknown):
```unknown
navigator.mediaDevices.getUserMedia({
  audio: {
    mandatory: {
      chromeMediaSource: "tab",
      chromeMediaSourceId: id,
    },
  },
  video: {
    mandatory: {
      chromeMediaSource: "tab",
      chromeMediaSourceId: id,
    },
  },
});
```

Example 3 (unknown):
```unknown
chrome.tabCapture.capture(  options: CaptureOptions,  callback: function,): void
```

Example 4 (javascript):
```javascript
(stream: LocalMediaStream) => void
```

---

## chrome.system.memory 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/memory?hl=zh-cn

**Contents:**
- chrome.system.memory 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - MemoryInfo
    - 属性
- 方法
  - getInfo()
    - 返回

chrome.system.memory API。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.memory.getInfo(): Promise<MemoryInfo>
```

---

## chrome.history 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/history

**Contents:**
- chrome.history 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 过渡类型
- 示例
- 类型
  - HistoryItem
    - 属性
  - TransitionType

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

如需与用户的浏览器历史记录互动，请使用 History API。

如需使用 History API，请在扩展程序清单中声明 "history" 权限。例如：

History API 使用过渡类型来描述浏览器在特定访问会话中如何导航到特定网址。例如，如果用户通过点击另一网页上的链接来访问某个网页，则过渡类型为“link”。如需查看过渡类型的列表，请参阅参考内容。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 history API 示例。

相应网页上次加载的时间（以自纪元以来经历的毫秒数表示）。

“链接” 用户通过点击其他网页上的链接到达此网页。

“已输入” 用户通过在地址栏中输入网址到达此网页。此属性还用于其他明确的导航操作。

“auto_bookmark” 用户通过界面中的建议（例如通过菜单项）到达此页面。

“auto_subframe” 用户是通过他们未请求的子框架导航到达此网页的，例如通过在上一网页的框架中加载的广告到达此网页。这些操作不一定会生成“后退”和“前进”菜单中的新导航条目。

“manual_subframe” 用户通过在子框架中选择内容到达此网页。

“generated” 用户在地址栏中输入内容并选择看起来不像网址的条目（例如 Google 搜索建议）后到达此网页。例如，匹配项可能包含 Google 搜索结果页面的网址，但向用户显示为“在 Google 上搜索…”。这些与输入型导航不同，因为用户没有输入或看到目标网址。它们还与关键字导航相关。

“auto_toplevel” 网页是在命令行中指定的，或者是起始网页。

“form_submit” 用户通过填写表单中的值并提交表单来访问此网页。并非所有表单提交都使用此过渡类型。

“重新加载” 用户重新加载了网页，可能是通过点击重新加载按钮或在地址栏中按 Enter 键完成的。会话恢复和“重新打开关闭的标签页”功能也使用此过渡类型。

“keyword” 此网页的网址是从可替换的关键字（而非默认搜索服务提供商）生成的。

“keyword_generated” 与为关键字生成的访问相对应。

相应操作的网址。必须采用从对 history.search() 的调用返回的格式。

相应 history.HistoryItem 的唯一标识符。

如果相应访问源自此设备，则为 True。如果该内容是从其他设备同步的，则为 False。

相应访问发生的时间，以自纪元开始计算的毫秒数表示。

在当前时间向历史记录添加一个网址，并指定“link”的过渡类型。

从历史记录中移除指定日期范围内的所有内容。除非所有访问都位于该范围内，否则网页不会从历史记录中移除。

在此日期之前添加到历史记录中的项目（以毫秒为单位，从 Epoch 起算）。

在此日期之后添加到历史记录中的项目（以自纪元开始算起的毫秒数表示）。

搜索历史记录，查找与查询匹配的每个网页的上次访问时间。

将结果限制为在此日期之前访问过的结果，以自纪元以来的毫秒数表示。

将结果限制为在此日期之后访问过的网页，以自纪元开始算起的毫秒数表示。如果未指定该属性，则默认值为 24 小时。

针对历史记录服务的自由文本查询。留空可检索所有网页。

Promise<HistoryItem[]>

在访问网址时触发，并提供相应网址的 HistoryItem 数据。此事件在网页加载之前触发。

当从历史记录中移除一个或多个网址时触发。移除所有访问记录后，相应网址会从历史记录中清除。

如果所有历史记录均已移除，则为 True。如果为 true，则网址将为空。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "history"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.history.addUrl(  details: UrlDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.history.deleteAll(): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.history.deleteRange(  range: object,): Promise<void>
```

---

## chrome.extension 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/extension?hl=zh-cn

**Contents:**
- chrome.extension 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 类型
  - ViewType
    - 枚举
- 属性
  - inIncognitoContext
    - 类型
- 方法
  - getBackgroundPage()

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

对于在无痕式标签页中运行的内容脚本以及在无痕式进程中运行的扩展程序网页，此属性为 true。后者仅适用于具有“split”incognito_behavior 的扩展程序。

返回在当前扩展程序内运行的后台网页的 JavaScript“window”对象。如果扩展程序没有背景页面，则返回 null。

返回一个 JavaScript“window”对象数组，其中包含当前扩展程序中运行的每个网页。

根据标签页 ID 查找视图。如果省略此字段，则返回所有视图。

要获取的视图的类型。如果省略，则返回所有视图（包括后台网页和标签页）。

限制搜索范围的窗口。如果省略，则返回所有视图。

检索扩展程序对“file://”方案的访问状态。此设置对应于用户控制的“允许访问文件网址”设置，可通过 chrome://extensions 页面访问。

检索扩展程序对无痕模式的访问权限状态。此设置对应于用户控制的“允许在无痕模式下运行”扩展程序级设置，可通过 chrome://extensions 页面访问。

设置扩展程序更新网址中使用的 ap CGI 参数的值。对于托管在 Chrome 扩展程序库中的扩展程序，系统会忽略此值。

**Examples:**

Example 1 (unknown):
```unknown
chrome.extension.getBackgroundPage(): Window | undefined
```

Example 2 (unknown):
```unknown
chrome.extension.getViews(  fetchProperties?: object,): Window[]
```

Example 3 (unknown):
```unknown
chrome.extension.isAllowedFileSchemeAccess(): Promise<boolean>
```

Example 4 (unknown):
```unknown
chrome.extension.isAllowedIncognitoAccess(): Promise<boolean>
```

---

## chrome.fileBrowserHandler 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fileBrowserHandler

**Contents:**
- chrome.fileBrowserHandler 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
- 权限
- 可用性
  - 实现文件浏览器处理程序
- 类型
  - FileHandlerExecuteEventDetails
    - 属性
- 事件

使用 chrome.fileBrowserHandler API 扩展 Chrome 操作系统的文件浏览器。例如，您可以使用此 API 让用户向您的网站上传文件。

当用户按 Alt+Shift+M 或连接外部存储设备（例如 SD 卡、USB 密钥、外部驱动器或数码相机）时，ChromeOS 文件浏览器将会启动。除了显示外部设备上的文件外，文件浏览器还可以显示用户之前保存到系统的文件。

当用户选择一个或多个文件时，文件浏览器会添加按钮，用于表示这些文件的有效处理程序。例如，在下面的屏幕截图中，选择包含“.png”的文件后缀的结果是“保存到图库”按钮。

您必须在扩展程序清单中声明 "fileBrowserHandler" 权限。

您必须使用 "file_browser_handlers" 字段将扩展程序注册为至少一种文件类型的处理程序。您还应提供 16x16 的图标，以显示在按钮上。例如：

要使用此 API，您必须实现一个用于处理 chrome.fileBrowserHandler 的 onExecute 事件的函数。每当用户点击代表您的文件浏览器处理程序的按钮时，系统就会调用您的函数。在您的函数中，使用 File System API 来获取对文件内容的访问权限。示例如下：

fileBrowserHandler.onExecute 事件的事件详情载荷。

表示相应操作目标文件的 Entry 实例数组（在 ChromeOS 文件浏览器中选择）。

引发此事件的标签页的 ID。标签页 ID 在浏览器会话中是唯一的。

通过 ChromeOS 文件浏览器执行文件系统操作时触发。

FileHandlerExecuteEventDetails

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "file_browser_handlers": [
    {
      "id": "upload",
      "default_title": "Save to Gallery", // What the button will display
      "file_filters": [
        "filesystem:*.jpg",  // To match all files, use "filesystem:*.*"
        "filesystem:*.jpeg",
        "filesystem:*.png"
      ]
    }
  ],
  "permissions" : [
    "fileBrowserHandler"
  ],
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  ...
}
```

Example 2 (javascript):
```javascript
chrome.fileBrowserHandler.onExecute.addListener(async (id, details) => {
  if (id !== 'upload') {
    return;  // check if you have multiple file_browser_handlers
  }

  for (const entry of detail.entries) {
    // the FileSystemFileEntry doesn't have a Promise API, wrap in one
    const file = await new Promise((resolve, reject) => {
      entry.file(resolve, reject);
    });
    const buffer = await file.arrayBuffer();
    // do something with buffer
  }
});
```

Example 3 (unknown):
```unknown
chrome.fileBrowserHandler.onExecute.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(id: string, details: FileHandlerExecuteEventDetails) => void
```

---

## chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/contentSettings

**Contents:**
- chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和使用
  - 内容设置模式
  - 模式优先级
  - 主要模式和次要模式
  - 资源标识符
- 示例
- 类型

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

您必须在扩展程序的清单中声明 "contentSettings" 权限，才能使用该 API。例如：

您可以使用模式来指定每项内容设置所影响的网站。例如，https://*.youtube.com/* 指定了 youtube.com 及其所有子网域。内容设置模式的语法与匹配模式的语法相同，但存在以下几点差异：

如果有多条内容设置规则适用于特定网站，则具有更具体模式的规则优先适用。

如果一个模式在某个部分比另一个模式更具体，但在另一部分则不太具体，系统会按以下顺序检查不同的部分：主机名、方案、端口。例如，以下格式按优先级排序：

在决定应用哪项内容设置时，系统会考虑哪个网址取决于内容类型。 例如，对于 contentSettings.notifications，设置基于多功能框中显示的网址。此网址称为“主要”网址。

某些类型的内容可以考虑使用其他网址。例如，是否允许网站设置 contentSettings.cookies 取决于 HTTP 请求的网址（在本例中为主要网址）以及多功能框中显示的网址（称为“次要”网址）。

如果多条规则都具有主要模式和次要模式，则主要模式更具体的规则优先。如果多条规则具有相同的主要模式，则具有更具体的次要模式的规则优先。例如，以下主/次模式对列表按优先级排序：

借助资源标识符，您可以为内容类型的特定子类型指定内容设置。目前，唯一支持资源标识符的内容类型是 contentSettings.plugins，其中资源标识符用于标识特定插件。应用内容设置时，系统会先检查特定插件的设置。如果未找到特定插件的设置，系统会检查插件的一般内容设置。

例如，如果某项内容设置规则的资源标识符为 adobe-flash-player，模式为 <all_urls>，则即使模式 https://www.example.com/* 更具体，该规则也会优先于没有资源标识符且模式为 https://www.example.com/* 的规则。

您可以通过调用 contentSettings.ContentSetting.getResourceIdentifiers() 方法获取内容类型的资源标识符列表。返回的列表可能会因用户机器上安装的插件集而异，但 Chrome 会尽量在插件更新期间保持标识符稳定。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 contentSettings API 示例。

是否检查隐身会话的内容设置。（默认值为 false）

应检索内容设置的主要网址。请注意，主网址的含义取决于内容类型。

ResourceIdentifier 可选

应检索内容设置的辅助网址。默认为主要网址。请注意，辅助网址的含义取决于内容类型，并非所有内容类型都使用辅助网址。

getResourceIdentifiers 函数如下所示：

Promise<ResourceIdentifier[]>

主要网址的格式。如需详细了解模式的格式，请参阅内容设置模式。

ResourceIdentifier 可选

辅助网址的格式。默认情况下，系统会匹配所有网址。如需详细了解格式，请参阅内容设置格式。

相应规则所应用的设置。如需查看可能的值，请参阅各个 ContentSetting 对象的说明。

唯一使用资源标识符的内容类型是 contentSettings.plugins。如需了解详情，请参阅资源标识符。

ContentSetting 的范围。regular 之一：常规个人资料的设置（如果未在其他位置被覆盖，则无痕式个人资料会继承此设置）；incognito\_session\_only：无痕式个人资料的设置，只能在无痕式会话期间设置，并在无痕式会话结束时删除（会覆盖常规设置）。

"incognito_session_only"

是否允许网站自动下载多个文件。以下值之一：allow：允许网站自动下载多个文件；block：不允许网站自动下载多个文件；ask：在网站想要自动下载第一个文件后的其他文件时，询问用户。 默认值为 ask。主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<MultipleAutomaticDownloadsContentSetting>

是否允许网站使用 Private State Tokens API。allow 之一：允许网站使用 Private State Tokens API；block：禁止网站使用 Private State Tokens API。 默认值为 allow。调用 set() 时，主要网址格式必须为 <all_urls>。不使用辅助网址。

ContentSetting<AutoVerifyContentSetting>

是否允许网站访问摄像头。以下值之一：allow：允许网站访问摄像头；block：不允许网站访问摄像头；ask：当网站想要访问摄像头时进行询问。 默认值为 ask。主网址是请求相机访问权限的文档的网址。不使用辅助网址。 注意：如果两个模式均为“<all_urls>”，则“allow”设置无效。

ContentSetting<CameraContentSetting>

是否允许网站通过 Async Clipboard API 的高级功能访问剪贴板。“高级”功能包括在用户手势之后写入内置格式以外的任何内容，即读取能力、写入自定义格式的能力以及在没有用户手势的情况下写入的能力。以下值之一：allow：允许网站使用高级剪贴板功能；block：不允许网站使用高级剪贴板功能；ask：当网站想要使用高级剪贴板功能时进行询问。 默认值为 ask。主网址是指请求剪贴板访问权限的文档的网址。不使用辅助网址。

ContentSetting<ClipboardContentSetting>

是否允许网站设置 Cookie 和其他本地数据。以下值之一：allow：接受 Cookie；block：阻止 Cookie；session\_only：仅接受当前会话的 Cookie。 默认值为 allow。主网址是指表示 Cookie 源站的网址。辅助网址是顶级框架的网址。

ContentSetting<CookiesContentSetting>

已弃用。不再有任何效果。系统现在会自动为所有网站授予全屏权限。值始终为 allow。

ContentSetting<FullscreenContentSetting>

是否显示图片。以下值之一： allow：显示图片 block：不显示图片。 默认值为 allow。 主网址是顶级框架的网址。辅助网址是图片的网址。

ContentSetting<ImagesContentSetting>

是否运行 JavaScript。以下值之一：allow：运行 JavaScript；block：不运行 JavaScript。默认值为 allow。 主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<JavascriptContentSetting>

是否允许地理定位。allow：允许网站跟踪您的实际位置。 block：不允许网站跟踪您的实际位置。 ask：在允许网站跟踪您的实际位置之前先询问。 默认值为 ask。主网址是请求位置数据的文档的网址。辅助网址是顶级框架的网址（可能与请求网址相同，也可能不同）。

ContentSetting<LocationContentSetting>

是否允许网站使用麦克风。以下选项之一：allow：允许网站访问麦克风；block：不允许网站访问麦克风；ask：在网站想要访问麦克风时进行询问。 默认值为 ask。主网址是指请求麦克风访问权限的文档的网址。不使用辅助网址。 注意：如果两个模式均为“<all_urls>”，则“allow”设置无效。

ContentSetting<MicrophoneContentSetting>

已弃用。不再有任何效果。现在，系统会自动为所有网站授予鼠标锁定权限。值始终为 allow。

ContentSetting<MouselockContentSetting>

是否允许网站显示桌面通知。以下值之一：allow：允许网站显示桌面通知；block：不允许网站显示桌面通知；ask：当网站想要显示桌面通知时进行询问。 默认值为 ask。主网址是指想要显示通知的文档的网址。不使用辅助网址。

ContentSetting<NotificationsContentSetting>

已弃用。由于 Chrome 88 中移除了 Flash 支持，此权限不再有任何作用。值始终为 block。对 set() 和 clear() 的调用将被忽略。

ContentSetting<PluginsContentSetting>

是否允许网站显示弹出式窗口。以下值之一：allow：允许网站显示弹出式窗口；block：不允许网站显示弹出式窗口。 默认值为 block。 主网址是顶级框架的网址。不使用辅助网址。

ContentSetting<PopupsContentSetting>

已弃用。之前，此权限用于控制是否允许网站在沙盒外运行插件，不过，随着 Chrome 88 中移除了 Flash 代理进程，此权限不再有任何作用。值始终为 block。对 set() 和 clear() 的调用将被忽略。

ContentSetting<PpapiBrokerContentSetting>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "contentSettings"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
(details: object) => {...}
```

Example 3 (javascript):
```javascript
(details: object) => {...}
```

Example 4 (javascript):
```javascript
() => {...}
```

---

## chrome.loginState 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/loginState

**Contents:**
- chrome.loginState 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ProfileType
    - 枚举
  - SessionState
    - 枚举
- 方法

使用 chrome.loginState API 读取和监控登录状态。

“SIGNIN_PROFILE” 指定扩展程序位于登录资料中。

“USER_PROFILE” 指定扩展程序位于用户个人资料中。

“LOCK_PROFILE” 指定扩展程序位于锁定屏幕配置文件中。

“IN_OOBE_SCREEN” 指定用户处于开箱即用体验屏幕中。

“IN_LOGIN_SCREEN” 指定用户位于登录界面。

“IN_SESSION” 指定用户处于会话中。

“IN_LOCK_SCREEN” 指定用户处于锁定屏幕中。

“IN_RMA_SCREEN” 指定设备处于 RMA 模式，正在完成维修。

Promise<SessionState>

在会话状态发生变化时调度。sessionState 是新的会话状态。

**Examples:**

Example 1 (unknown):
```unknown
chrome.loginState.getProfileType(): Promise<ProfileType>
```

Example 2 (unknown):
```unknown
chrome.loginState.getSessionState(): Promise<SessionState>
```

Example 3 (unknown):
```unknown
chrome.loginState.onSessionStateChanged.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(sessionState: SessionState) => void
```

---

## chrome.notifications 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/notifications?hl=zh-cn

**Contents:**
- chrome.notifications 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - NotificationBitmap
  - NotificationButton
    - 属性
  - NotificationItem
    - 属性
  - NotificationOptions

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

应用图标遮罩不会向 Mac OS X 用户显示。

应用图标遮罩的网址。网址的限制与 iconUrl 相同。

应用图标遮罩应位于 Alpha 渠道中，因为系统只会考虑图片的 Alpha 渠道。

NotificationButton[] 可选

与通知关联的时间戳，以自纪元以来经过的毫秒数表示（例如 Date.now() + n）。

指向发件人头像、应用图标或图片通知缩略图的网址。

网址可以是数据网址、Blob 网址，也可以是相对于此扩展程序的 .crx 文件中资源的网址

**注意：**notifications.create() 方法需要此值。

指向图片类型通知的图片缩略图的网址。网址的限制与 iconUrl 相同。

自 Chrome 67 起，此界面提示会被忽略

NotificationItem[] 可选

用于多项通知的商品。Mac OS X 用户只能看到第一个项目。

**注意：**notifications.create() 方法需要此值。

优先级范围为 -2 到 2。-2 是最低优先级。2 为最高值。默认值为零。在不支持通知中心的平台（Windows、Linux 和 Mac）上，-2 和 -1 会导致错误，因为具有这些优先级的通知根本不会显示。

表示通知应一直显示在屏幕上，直到用户激活或关闭通知。此属性的默认值为 false。

表示在显示通知时不应发出任何声音或振动。此属性的默认值为 false。

**注意：**notifications.create() 方法需要此值。

要显示的通知类型。notifications.create 方法的必需参数。

“granted” 指定用户已选择显示来自应用或扩展程序的通知。这是安装时的默认设置。

“拒绝” 指定用户已选择不显示来自应用或扩展程序的通知。

“基本” 包含图标、标题、消息、expandedMessage 和最多两个按钮。

“image” 包含一个图标、标题、消息、expandedMessage、图片和最多两个按钮。

“list” 包含图标、标题、消息、项和最多两个按钮。Mac OS X 用户只能看到第一项。

“progress” 包含图标、标题、消息、进度和最多两个按钮。

要清除的通知的 ID。由 notifications.create 方法返回。

通知的标识符。如果未设置或为空，系统会自动生成 ID。如果与现有通知匹配，此方法会先清除该通知，然后再继续执行创建操作。标识符的长度不得超过 500 个字符。

在 Chrome 42 之前，notificationId 参数是必需的。

检索用户是否已启用来自相应应用或扩展程序的通知。

Promise<PermissionLevel>

要更新的通知的 ID。由 notifications.create 方法返回。

用户更改了权限级别。自 Chrome 47 起，只有 ChromeOS 具有可调度此事件的界面。

用户点击了应用通知设置的链接。自 Chrome 47 起，只有 ChromeOS 具有可调度此事件的界面。自 Chrome 65 起，该界面也已从 ChromeOS 中移除。

**Examples:**

Example 1 (unknown):
```unknown
chrome.notifications.clear(  notificationId: string,): Promise<boolean>
```

Example 2 (unknown):
```unknown
chrome.notifications.create(  notificationId?: string,  options: NotificationOptions,): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.notifications.getAll(): Promise<object>
```

Example 4 (unknown):
```unknown
chrome.notifications.getPermissionLevel(): Promise<PermissionLevel>
```

---

## chrome.power 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/power

**Contents:**
- chrome.power 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 类型
  - Level
    - 枚举
- 方法
  - releaseKeepAwake()
  - reportActivity()

使用 chrome.power API 可替换系统的电源管理功能。

默认情况下，操作系统会在用户处于非活动状态时调暗屏幕，并最终暂停系统。借助电源 API，应用或扩展程序可以使系统保持唤醒状态。

使用此 API，您可以指定停用电源管理的级别。"system" 级别可让系统保持活跃状态，但允许屏幕变暗或关闭。例如，即使屏幕处于关闭状态，通信应用也可以继续接收消息。"display" 级别可让屏幕和系统保持活跃状态。例如，电子书应用和演示应用可以在用户阅读时保持屏幕和系统处于活动状态。

当用户同时运行多个应用或扩展程序时，每个应用或扩展程序都有自己的能耗级别，此时系统会采用优先级最高的级别；"display" 的优先级始终高于 "system"。例如，如果应用 A 请求 "system" 电源管理，而应用 B 请求 "display"，则在应用 B 卸载或释放其请求之前，系统会使用 "display"。如果应用 A 仍处于活跃状态，则使用 "system"。

“system” 防止系统因用户不活动而进入休眠状态。

“display” 防止显示屏因用户不活动而关闭或变暗，或防止系统进入休眠状态。

释放之前通过 requestKeepAwake() 发出的请求。

报告用户活动，以便从屏幕变暗或关闭状态或从屏保唤醒屏幕。如果屏保当前处于活动状态，则退出屏保。

请求暂时停用电源管理。level 描述了应停用电源管理的程度。如果同一应用之前发出的请求仍处于有效状态，则会被新请求替换。

**Examples:**

Example 1 (unknown):
```unknown
chrome.power.releaseKeepAwake(): void
```

Example 2 (unknown):
```unknown
chrome.power.reportActivity(): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.power.requestKeepAwake(  level: Level,): void
```

---

## chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/commands?hl=zh-cn

**Contents:**
- chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概念和使用
  - 支持的键
  - 组合键要求
  - 处理命令事件
  - 操作命令
  - 范围
- 示例

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

如需使用此 API，必须在清单中声明以下键。

Commands API 允许扩展程序开发者定义特定命令，并将其绑定到默认的按键组合。扩展程序接受的每个命令都必须在扩展程序的清单中声明为 "commands" 对象的属性。

属性键用作命令的名称。命令对象可以采用两个属性。

一个可选属性，用于声明命令的默认键盘快捷键。如果省略，则命令将处于未绑定状态。此属性可以采用字符串值或对象值。

字符串值，用于指定应在所有平台上使用的默认键盘快捷键。

扩展程序可以包含许多命令，但最多只能指定四个建议的键盘快捷键。用户可以从 chrome://extensions/shortcuts 对话框中手动添加更多快捷方式。

以下键可用作命令快捷键。键定义区分大小写。尝试加载具有错误大小写键的扩展程序会导致安装时出现清单解析错误。

常规 - Comma、Period、Home、End、PageUp、PageDown、Space、Insert、Delete

箭头键 - Up、Down、Left、Right

媒体键 - MediaNextTrack、MediaPlayPause、MediaPrevTrack、MediaStop

Ctrl、Alt、Shift、MacCtrl（仅限 macOS）、Option（仅限 macOS）、Command（仅限 macOS）、Search（仅限 ChromeOS）

扩展命令快捷方式必须包含 Ctrl 或 Alt。

在许多 macOS 键盘上，Alt 指的是 Option 键。

在 macOS 上，您还可以使用 Command 或 MacCtrl 代替 Ctrl，并使用 Option 键代替 Alt（请参阅下一个项目符号）。

在 macOS 上，Ctrl 会自动转换为 Command。

Command 还可用于 "mac" 快捷方式，以明确指代 Command 键。

如需在 macOS 上使用 Control 键，请在定义 "mac" 快捷方式时将 Ctrl 替换为 MacCtrl。

在其他平台的组合中使用 MacCtrl 会导致验证错误，并阻止安装扩展程序。

Search 是 ChromeOS 专用的可选修饰符。

某些操作系统和 Chrome 快捷键（例如窗口管理）始终优先于扩展程序命令快捷键，并且无法被覆盖。

在服务工作器中，您可以使用 onCommand.addListener 将处理程序绑定到清单中定义的每个命令。例如：

_execute_action (Manifest V3)、_execute_browser_action (Manifest V2) 和 _execute_page_action (Manifest V2) 命令分别预留用于触发操作、浏览器操作或网页操作。这些命令不会像标准命令那样调度 command.onCommand 事件。

如果您需要根据弹出式窗口的打开情况采取行动，请考虑在弹出式窗口的 JavaScript 中监听 DOMContentLoaded 事件。

默认情况下，命令的范围限定为 Chrome 浏览器。这意味着，当浏览器未处于焦点状态时，命令快捷键处于非活动状态。从 Chrome 35 开始，扩展程序开发者可以选择将命令标记为“全局”。即使 Chrome 未处于焦点状态，全局命令也能正常运行。

全局命令的键盘快捷键建议数量上限为 Ctrl+Shift+[0..9]。这是一项保护措施，旨在最大限度地降低覆盖其他应用中的快捷方式的风险，因为如果允许 Alt+P 作为全局快捷方式，那么在其他应用中，用于打开打印对话框的键盘快捷方式可能无法正常使用。

最终用户可以使用 chrome://extensions/shortcuts 中显示的界面，将全局命令重新映射到自己喜欢的按键组合。

以下示例展示了 Commands API 的核心功能。

命令允许扩展程序将逻辑映射到可由用户调用的键盘快捷键。最基本的命令只需要在扩展程序的清单中声明命令并注册监听器，如以下示例所示。

如概念和使用情况部分中所述，您还可以将命令映射到扩展程序的动作。以下示例注入了一个内容脚本，当用户点击扩展程序的操作或触发键盘快捷键时，该脚本会在当前页面上显示提醒。

如果某个扩展程序尝试注册的快捷键已被另一个扩展程序使用，则第二个扩展程序的快捷键将无法按预期注册。您可以预料到这种可能性，并在安装时检查是否存在冲突，从而提供更可靠的最终用户体验。

相应命令的有效快捷键，如果无有效快捷键，则为空白。

返回相应扩展程序的所有已注册的扩展程序命令及其快捷方式（如果处于有效状态）。在 Chrome 110 之前，此命令不会返回 _execute_action。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "commands": {
    "run-foo": {
      "suggested_key": {
        "default": "Ctrl+Shift+Y",
        "mac": "Command+Shift+Y"
      },
      "description": "Run \"foo\" on the current page."
    },
    "_execute_action": {
      "suggested_key": {
        "windows": "Ctrl+Shift+Y",
        "mac": "Command+Shift+Y",
        "chromeos": "Ctrl+Shift+U",
        "linux": "Ctrl+Shift+J"
      }
    }
  },
  ...
}
```

Example 2 (javascript):
```javascript
chrome.commands.onCommand.addListener((command) => {
  console.log(`Command: ${command}`);
});
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "commands": {
    "toggle-feature-foo": {
      "suggested_key": {
        "default": "Ctrl+Shift+5"
      },
      "description": "Toggle feature foo",
      "global": true
    }
  },
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "Command demo - basic",
  "version": "1.0",
  "manifest_version": 3,
  "background": {
    "service_worker": "service-worker.js"
  },
  "commands": {
    "inject-script": {
      "suggested_key": "Ctrl+Shift+Y",
      "description": "Inject a script on the page"
    }
  }
}
```

---

## chrome.readingList 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/readingList

**Contents:**
- chrome.readingList 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 商品排序
  - 商品的唯一性
- 使用场景
  - 添加项目
  - 展示商品

使用 chrome.readingList API 读取和修改阅读清单中的内容。

如需使用 Reading List API，请在扩展程序清单文件中添加 "readingList" 权限：

Chrome 具有位于侧边栏中的阅读清单。它可让用户保存网页以供日后阅读或离线阅读。 使用 Reading List API 检索现有项，并向列表添加项或从中移除项。

以下部分展示了 Reading List API 的一些常见用例。如需查看完整的扩展程序示例，请参阅扩展程序示例。

如需将内容添加到阅读清单，请使用 chrome.readingList.addEntry()：

如需显示阅读清单中的内容，请使用 chrome.readingList.query() 方法检索这些内容。

您可以使用 chrome.readingList.updateEntry() 更新标题、网址和阅读状态。以下代码将某项标记为已读：

如需移除某项内容，请使用 chrome.readingList.removeEntry()：

如需查看更多 Reading List API 扩展演示，请参阅 Reading List API 示例。

指示是搜索已读 (true) 还是未读 (false) 项目。

条目的创建时间。以自 1970 年 1 月 1 日以来的毫秒数记录。

相应条目的上次更新时间。此值以自 1970 年 1 月 1 日以来的毫秒数表示。

更新后的已读状态。如果未提供值，则保留现有状态。

如果阅读清单中不存在相应条目，则添加该条目。

检索与 QueryInfo 属性匹配的所有条目。系统不会匹配未提供的属性。

Promise<ReadingListEntry[]>

当向阅读清单添加 ReadingListEntry 时触发。

当从阅读清单中移除 ReadingListEntry 时触发。

当阅读清单中的 ReadingListEntry 更新时触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My reading list extension",
  ...
  "permissions": [
    "readingList"
  ]
}
```

Example 2 (unknown):
```unknown
chrome.readingList.addEntry({
  title: "New to the web platform in September | web.dev",
  url: "https://developer.chrome.com/",
  hasBeenRead: false
});
```

Example 3 (javascript):
```javascript
const items = await chrome.readingList.query({});

for (const item of items) {
  // Do something do display the item
}
```

Example 4 (unknown):
```unknown
chrome.readingList.updateEntry({
  url: "https://developer.chrome.com/",
  hasBeenRead: true
});
```

---

## chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tabs?hl=zh-cn

**Contents:**
- chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 使用场景
  - 在新标签页中打开扩展程序页面
  - 获取当前标签页
  - 将指定标签页静音
  - 点击时将当前标签页移至第一个位置
  - 将消息传递给所选标签页的内容脚本
- 扩展示例

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

Tabs API 不仅提供用于操纵和管理标签页的功能，还可以检测标签页的语言、截取屏幕截图，以及与标签页的内容脚本通信。

大多数功能无需任何权限即可使用。例如：创建新标签页、重新加载标签页、前往其他网址等。

开发者在使用 Tabs API 时应注意以下三种权限。

此权限不授予对 chrome.tabs 命名空间的访问权限。相反，它会授予扩展程序针对 tabs.Tab 实例上的四个敏感属性（url、pendingUrl、title 和 favIconUrl）调用 tabs.query() 的能力。

主机权限允许扩展程序读取和查询匹配标签页的四项敏感 tabs.Tab 属性。它们还可以使用 tabs.captureVisibleTab()、scripting.executeScript()、scripting.insertCSS() 和 scripting.removeCSS() 等方法直接与匹配的标签页互动。

activeTab 会在用户调用时授予扩展程序当前标签页的临时主机权限。与主机权限不同，activeTab 不会触发任何警告。

扩展程序的一个常见模式是在安装时在新标签页中打开初始配置页面。以下示例展示了如何执行此操作。

此示例演示了扩展程序的服务工作线程如何从当前聚焦的窗口（如果没有聚焦任何 Chrome 窗口，则从最近聚焦的窗口）检索活动标签页。这通常可以视为用户的当前标签页。

此示例展示了扩展程序如何切换指定标签页的静音状态。

此示例展示了如何在拖动可能正在进行或可能未在进行时移动标签页。虽然此示例使用 chrome.tabs.move，但您也可以将相同的等待模式用于在拖动过程中修改标签页的其他调用。

此示例演示了扩展程序的服务工作线程如何使用 tabs.sendMessage() 与特定浏览器标签页中的内容脚本进行通信。

如需查看更多 Tabs API 扩展程序演示，请探索以下任一内容：

相应标签页的静音状态以及上次状态更改的原因。

更改静音状态的扩展程序的 ID。如果扩展程序不是静音状态上次更改的原因，则不设置。

标签页是否处于静音状态（无法播放声音）。即使标签页尚未播放或当前未播放声音，也可能会处于静音状态。相当于是否显示“静音”音频指示器。

相应标签页静音或取消静音的原因。如果相应标签页的静音状态从未更改过，则不设置。

“user” 用户输入操作设置了静音状态。

“捕获” 标签页捕获已开始，强制更改为静音状态。

“extension” 由 extensionId 字段标识的扩展程序，用于设置静音状态。

相应标签页在其窗口中是否处于活动状态。不一定表示窗口已聚焦。

相应标签页在过去几秒内是否发出过声音（但如果同时处于静音状态，则可能听不到声音）。相当于“扬声器音频”指示器是否显示。

当资源不足时，浏览器是否可以自动舍弃相应标签页。

标签页是否已舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

相应标签页的网站图标的网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页正在加载，该值也可能为空字符串。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页的 ID。标签页 ID 在浏览器会话中是唯一的。在某些情况下，标签页可能未分配 ID；例如，使用 sessions API 查询外部标签页时，可能会出现会话 ID。对于应用和开发者工具窗口，标签页 ID 也可以设置为 chrome.tabs.TAB_ID_NONE。

相应标签页上次在其窗口中变为活动状态的时间（以自纪元以来经过的毫秒数表示）。

相应标签页的静音状态以及上次状态更改的原因。

打开此标签页的标签页的 ID（如果有）。仅当打开程序标签页仍然存在时，此属性才会存在。

标签页正在前往的网址（在提交之前）。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限，并且存在待处理的导航时，才会显示此属性。

请使用 tabs.Tab.highlighted。

用于唯一标识从 sessions API 获取的标签页的会话 ID。

标签页的标题。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，此属性才会存在。

相应标签页主框架的上次已提交网址。仅当扩展程序具有 "tabs" 权限或具有网页的宿主权限时，才会显示此属性。如果标签页尚未提交，则可能为空字符串。另请参阅 Tab.pendingUrl。

定义如何处理标签页中的缩放更改以及在什么范围内处理。

用于在对 tabs.getZoomSettings 的调用中返回当前标签页的默认缩放级别。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

定义如何处理缩放更改，即哪个实体负责网页的实际缩放；默认值为 automatic。

“手动” 替换自动处理缩放更改。系统仍会调度 onZoomChange 事件，扩展程序有责任监听此事件并手动缩放网页。此模式不支持 per-origin 缩放，因此会忽略 scope 缩放设置并假定为 per-tab。

“已停用” 停用标签页中的所有缩放功能。相应标签页会恢复为默认缩放级别，并且系统会忽略所有尝试进行的缩放更改。

定义缩放更改是针对网页的来源保持不变，还是仅在此标签页中生效；在 automatic 模式下默认为 per-origin，否则为 per-tab。

“按来源” 缩放更改会保留在缩放网页的来源中，也就是说，导航到同一来源的所有其他标签页也会缩放。此外，per-origin 缩放更改会与来源一起保存，这意味着当导航到同一来源中的其他网页时，这些网页都会缩放到相同的缩放系数。per-origin 范围仅在 automatic 模式下可用。

“按标签页” 缩放更改仅在此标签页中生效，其他标签页中的缩放更改不会影响此标签页的缩放。此外，per-tab 缩放比例会在导航时重置；导航标签页始终会加载具有 per-origin 缩放因子的网页。

每秒可调用 captureVisibleTab 的次数上限。captureVisibleTab 的开销很大，不应过于频繁地调用。

表示 tab_strip 中没有标签页索引的索引。

捕获指定窗口中当前活动标签页的可见区域。如需调用此方法，扩展程序必须拥有 <all_urls> 权限或 activeTab 权限。除了扩展程序通常可以访问的网站之外，此方法还允许扩展程序捕获其他受限的敏感网站，包括 chrome:-scheme 网页、其他扩展程序的网页和 data: 网址。只有拥有 activeTab 权限才能捕获这些敏感网站。只有在扩展程序获得文件访问权限后，才能捕获文件网址。

连接到指定标签页中的内容脚本。runtime.onConnect 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。如需了解详情，请参阅内容脚本消息传递。

打开由 documentId 标识的特定文档的端口，而不是标签页中的所有框架。

打开由 frameId 标识的特定框架的端口，而不是标签页中的所有框架。

传递给正在监听连接事件的内容脚本的 onConnect。

可用于与指定标签页中运行的内容脚本通信的端口。如果标签页关闭或不存在，则会触发端口的 runtime.Port 事件。

标签页是否应成为窗口中的活动标签页。不影响窗口是否处于聚焦状态（请参阅 windows.update）。默认值为 true。

标签页在窗口中应占据的位置。提供的值会限制在 0 到窗口中的标签页数量之间。

打开此标签页的标签页的 ID。如果指定，则打开程序标签页必须与新创建的标签页位于同一窗口中。

相应标签页是否应固定。默认设置为 false

相应标签页是否应成为窗口中的所选标签页。默认设置为 true

标签页最初导航到的网址。完全限定网址必须包含方案（即“http://www.google.com”，而不是“www.google.com”）。相对网址相对于扩展程序中的当前网页。默认为“新标签页”。

从内存中舍弃标签页。舍弃的标签页仍会显示在标签栏中，并在激活时重新加载。

要舍弃的标签页的 ID。如果指定了该参数，则除非标签页处于活动状态或已舍弃，否则会舍弃该标签页。如果省略，浏览器会舍弃最不重要的标签页。如果没有可舍弃的标签页，此操作可能会失败。

Promise<Tab | undefined>

Promise<Tab | undefined>

获取发出此脚本调用的标签页。如果从非标签页上下文（例如，后台网页或弹出式窗口视图）调用，则返回 undefined。

Promise<Tab | undefined>

要从中获取当前缩放系数的标签页的 ID；默认为当前窗口的活动标签页。

要从中获取当前缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

Promise<ZoomSettings>

要返回的标签页的 ID；默认为当前窗口的所选标签页。

要向前导航的标签页的 ID；默认为当前窗口的所选标签页。

将一个或多个标签页添加到指定的分组；如果未指定分组，则将给定的标签页添加到新创建的分组。

用于创建群组的配置。如果已指定 groupId，则无法使用此属性。

要将标签页添加到的群组的 ID。如果未指定，系统会创建一个新组。

number | [number, ...number[]]

要添加到指定群组的标签页 ID 或标签页 ID 列表。

突出显示给定的标签页，并将焦点放在第一个标签页上。如果指定标签页当前处于活动状态，则看起来不会执行任何操作。

Promise<windows.Window>

将一个或多个标签页移动到其窗口中的新位置，或移动到新窗口。请注意，标签页只能在普通窗口（window.type === "normal"）之间移动。

要移动的标签页 ID 或标签页 ID 列表。

要将窗口移至的位置。使用 -1 将标签页放置在窗口末尾。

获取具有指定属性的所有标签页，如果未指定属性，则获取所有标签页。

浏览器是否可以在资源不足时自动舍弃标签页。

标签页是否被舍弃。舍弃的标签页是指其内容已从内存中卸载，但仍显示在标签页栏中的标签页。下次激活时，其内容会重新加载。

标签页是否处于冻结状态。冻结的标签页无法执行任务，包括事件处理脚本或计时器。它会显示在标签页栏中，并且其内容会加载到内存中。激活后，会员资格将恢复正常。

标签页所在群组的 ID，或 tabGroups.TAB_GROUP_ID_NONE（对于未分组的标签页）。

标签页所在的拆分视图的 ID；如果标签页不在拆分视图中，则为 tabs.SPLIT_VIEW_ID_NONE。

根据某种模式匹配网页标题。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

根据一个或多个 网址 格式匹配标签页。片段标识符不匹配。如果扩展程序没有 "tabs" 权限或网页的宿主权限，则系统会忽略此属性。

父窗口的 ID，或windows.WINDOW_ID_CURRENT（表示当前窗口）。

要重新加载的标签页的 ID；默认为当前窗口的所选标签页。

要关闭的标签页 ID 或标签页 ID 列表。

向指定标签页中的内容脚本发送一条消息，并提供一个可选的回调函数，用于在收到响应时运行。runtime.onMessage 事件会在当前扩展程序中指定标签页内运行的每个内容脚本中触发。

要发送的消息。此消息应为可 JSON 化的对象。

向由 documentId 标识的特定文档发送消息，而不是向标签页中的所有框架发送消息。

向由 frameId 标识的特定帧发送消息，而不是向标签页中的所有帧发送消息。

要缩放的标签页的 ID；默认为当前窗口的活动标签页。

新的缩放比例。值为 0 时，标签页将设置为其当前的默认缩放比例。大于 0 的值指定了相应标签页的缩放比例（可能不是默认值）。

为指定标签页设置缩放设置，以定义如何处理缩放更改。在标签页之间切换时，这些设置会重置为默认值。

要更改缩放设置的标签页的 ID；默认为当前窗口的活动标签页。

定义如何处理缩放更改以及在哪个范围内处理。

从相应群组中移除一个或多个标签页。如果任何组变为空组，系统会将其删除。

number | [number, ...number[]]

要从相应群组中移除的标签页 ID 或标签页 ID 列表。

修改标签页的属性。不会修改未在 updateProperties 中指定的属性。

相应标签页是否应处于有效状态。不影响窗口是否处于聚焦状态（请参阅 windows.update）。

当资源不足时，浏览器是否应自动舍弃相应标签页。

打开此标签页的标签页的 ID。如果指定，打开的标签页必须与当前标签页位于同一窗口中。

要将标签页导航到的网址。不支持 JavaScript 网址；请改用 scripting.executeScript。

Promise<Tab | undefined>

当窗口中的有效标签页发生变化时触发。请注意，此事件触发时，标签页的网址可能尚未设置，但您可以监听 onUpdated 事件，以便在网址设置时收到通知。

当标签页附加到窗口时触发；例如，当标签页在窗口之间移动时。

在创建标签页时触发。请注意，触发此事件时，标签页的网址和标签页分组会员资格可能尚未设置，但您可以监听 onUpdated 事件，以便在设置网址或将标签页添加到标签页分组时收到通知。

当标签页从窗口分离时触发；例如，当标签页在窗口之间移动时。

当窗口中突出显示或选定的标签页发生变化时触发。

当标签页在窗口内移动时触发。系统只会触发一个移动事件，表示用户直接移动的标签页。对于必须响应手动移动的标签页而移动的其他标签页，不会触发移动事件。当标签页在窗口之间移动时，不会触发此事件；如需了解详情，请参阅 tabs.onDetached。

如果标签页因其父窗口关闭而关闭，则为 True。

在标签页因预渲染或即时而替换为另一个标签页时触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "tabs"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "host_permissions": [
    "http://*/*",
    "https://*/*"
  ],
  ...
}
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "activeTab"
  ],
  ...
}
```

Example 4 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(({reason}) => {
  if (reason === 'install') {
    chrome.tabs.create({
      url: "onboarding.html"
    });
  }
});
```

---

## chrome.system.cpu 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/cpu?hl=zh-cn

**Contents:**
- chrome.system.cpu 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - CpuInfo
    - 属性
  - CpuTime
    - 属性
  - ProcessorInfo
    - 属性

使用 system.cpu API 查询 CPU 元数据。

一组表示处理器部分功能的特征码。目前支持的代码包括“mmx”“sse”“sse2”“sse3”“ssse3”“sse4_1”“sse4_2”和“avx”。

来自 CPU 各个散热区的 CPU 温度读数列表。温度以摄氏度为单位。

相应处理器的总累计时间。此值等于用户 + 内核 + 空闲。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.cpu.getInfo(): Promise<CpuInfo>
```

---

## chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/declarativeContent

**Contents:**
- chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 规则
  - 网页网址匹配
  - CSS 匹配
  - 书签状态匹配
- 类型
  - ImageDataType

使用 chrome.declarativeContent API 可根据网页内容执行操作，而无需读取网页内容的权限。

声明式 Content API 可让您根据 或者 CSS 选择器与页面上的某个元素匹配，无需 添加主机权限或注入内容脚本。

使用 activeTab 权限，以在用户点击 操作。

规则由条件和操作组成。如果满足任一条件，则所有操作 。这些操作包括 setIcon() 和 showAction()。

当且仅当所有网页都列出时，PageStateMatcher 才与网页匹配 条件。可与网页网址、CSS 复合选择器匹配 或网页的已添加书签状态。以下规则启用 当有密码字段存在时，扩展程序在 Google 网页上执行的操作：

如果还要为包含视频的 Google 网站启用该扩展程序的操作， 条件，因为每个条件足以触发所有指定操作：

onPageChanged 事件测试是否有任何规则至少满足一条规则 条件并执行操作。浏览会话时，规则会保留下来；因此，在 则首先应使用 removeRules 清除 然后使用 addRules 注册新的规则。

如果有 activeTab 权限，您的扩展程序不会显示任何权限 警告，并且当用户点击该扩展程序操作时，该扩展程序只会在相关网页上运行。

当满足网址条件时，PageStateMatcher.pageurl 即为匹配。通过 最常见的条件是主机、路径或网址串联，后跟包含、等于、前缀或 后缀。下表包含几个示例：

所有条件均区分大小写。如需条件的完整列表，请参阅 UrlFilter。

PageStateMatcher.css 条件必须是复合选择器， 也就是说，您不能包含空格或“>”等组合词在您的 。这有助于 Chrome 更高效地匹配选择器。

CSS 条件仅匹配显示的元素：如果与选择器匹配的元素 display:none 或其父元素之一为 display:none，但不会导致条件 匹配。使用 visibility:hidden 设置样式的元素、位于屏幕外或被其他元素隐藏的元素 仍然可以匹配您的条件

PageStateMatcher.isBookmarked 条件允许匹配 用户个人资料中当前网址的书签状态。要使用此条件 "书签"权限必须在扩展程序清单中声明。

请参阅 https://developer.mozilla.org/en-US/docs/Web/API/ImageData。

如果数组中的所有 CSS 选择器都与与页面主框架同源的框架中的显示元素相匹配，则匹配。为了加快匹配速度，此数组中的所有选择器都必须是复合选择器。注意：列出数百个 CSS 选择器或列出每个网页匹配数百次的 CSS 选择器可能会降低网站的加载速度。

如果网页的书签状态等于指定值，则匹配。需要书签权限。

如果网页的顶级网址满足 UrlFilter 的条件，则匹配。

警告：此操作仍处在实验阶段，不支持 Chrome 稳定版。

内容脚本是在匹配网页的所有帧中运行，还是仅在顶部帧中运行。默认值为 false。

要作为内容脚本的一部分注入的 CSS 文件的名称。

作为内容脚本的一部分注入的 JavaScript 文件的名称。

是否在 about:blank 和 about:srcdoc 中插入内容脚本。默认值为 false。

声明式事件操作，在满足相应条件时，为扩展程序的网页操作或浏览器操作设置 n-dip 方形图标。此操作无需主机权限即可使用，但必须对扩展程序执行网页或浏览器操作。

必须且只能指定 imageData 和 path 中的一个。两者都是将多个像素映射到图像表示的字典。imageData 中的图片表示形式是一个 ImageData 对象；，而 path 中的图片表示形式是图片文件相对于扩展程序清单的路径。canvas如果 scale 屏幕像素适合设备无关像素，则系统会使用 scale * n 图标。如果该比例缺失，则将另一张图片调整为所需的大小。

ImageData 对象或字典 {size ->ImageData}，表示要设置的图标。如果将图标指定为字典，则系统会根据屏幕的像素密度选择使用的图片。如果适合一个屏幕空间单元的图片像素数等于 scale，则会选择尺寸为 scale * n 的图片，其中 n 是界面中图标的尺寸。必须至少指定一张图片。请注意，details.imageData = foo 相当于 details.imageData = {'16': foo}。

一种声明式事件操作，可在满足相应条件时将扩展程序的工具栏操作设置为启用状态。此操作无需主机权限即可执行。如果扩展程序具有 activeTab 权限，点击网页操作即可授予对活动标签页的访问权限。

在不符合这些条件的网页上，扩展程序的工具栏操作会变为灰度模式，点击该按钮会打开上下文菜单，而不会触发操作。

请使用 declarativeContent.ShowAction。

一种声明式事件操作，可在满足相应条件时将扩展程序的网页操作设为启用状态。此操作无需主机权限也可使用，但扩展程序必须包含网页操作。如果扩展程序具有 activeTab 权限，点击网页操作即可授予对活动标签页的访问权限。

在不符合这些条件的网页上，扩展程序的工具栏操作会变为灰度模式，点击该按钮会打开上下文菜单，而不会触发操作。

提供由 addRules、removeRules 和 getRules 组成的声明式事件 API。

**Examples:**

Example 1 (javascript):
```javascript
let rule1 = {
  conditions: [
    new chrome.declarativeContent.PageStateMatcher({
      pageUrl: { hostSuffix: '.google.com', schemes: ['https'] },
      css: ["input[type='password']"]
    })
  ],
  actions: [ new chrome.declarativeContent.ShowAction() ]
};
```

Example 2 (javascript):
```javascript
let rule2 = {
  conditions: [
    new chrome.declarativeContent.PageStateMatcher({
      pageUrl: { hostSuffix: '.google.com', schemes: ['https'] },
      css: ["input[type='password']"]
    }),
    new chrome.declarativeContent.PageStateMatcher({
      css: ["video"]
    })
  ],
  actions: [ new chrome.declarativeContent.ShowAction() ]
};
```

Example 3 (unknown):
```unknown
chrome.runtime.onInstalled.addListener(function(details) {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([rule2]);
  });
});
```

Example 4 (javascript):
```javascript
(arg: PageStateMatcher) => {...}
```

---

## chrome.systemLog 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/systemLog

**Contents:**
- chrome.systemLog 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - MessageOptions
    - 属性
- 方法
  - add()
    - 参数

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

**Examples:**

Example 1 (unknown):
```unknown
chrome.systemLog.add(  options: MessageOptions,): Promise<void>
```

---

## chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webNavigation?hl=zh-cn

**Contents:**
- chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 活动顺序
  - 与 webRequest 事件的关系
  - 标签页 ID
  - 时间戳
  - 框架 ID
  - 过渡类型和限定符

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

所有 chrome.webNavigation 方法和事件都需要您在扩展程序清单中声明 "webNavigation" 权限。例如：

对于成功完成的导航，系统会按以下顺序触发事件：

如果在此过程中发生任何错误，系统会生成 onErrorOccurred 事件。对于特定导航，在 onErrorOccurred 之后不会再触发其他事件。

如果导航框架包含子框架，则其 onCommitted 会在任何子框架的 onBeforeNavigate 之前触发；而 onCompleted 会在所有子框架的 onCompleted 之后触发。

如果帧的参考 fragment 发生更改，则会触发 onReferenceFragmentUpdated 事件。此事件可以在 onDOMContentLoaded 之后的任何时间触发，甚至在 onCompleted 之后触发。

如果使用 History API 修改帧的状态（例如，使用 history.pushState()），系统会触发 onHistoryStateUpdated 事件。此事件可在 onDOMContentLoaded 之后的任何时间触发。

如果导航从往返缓存中恢复了网页，则不会触发 onDOMContentLoaded 事件。由于内容在首次访问网页时已完成加载，因此不会触发该事件。

如果导航是使用 Chrome Instant 或 Instant Pages 触发的，则会将完全加载的网页替换到当前标签页中。在这种情况下，系统会触发 onTabReplaced 事件。

webRequest API 的事件与 webNavigation API 的事件之间没有明确的顺序。对于已开始新导航的框架，仍有可能收到 webRequest 事件；或者，只有在网络资源已完全加载后，导航才会继续。

一般来说，webNavigation 事件与界面中显示的导航状态密切相关，而 webRequest 事件则对应于网络堆栈的状态，该状态通常对用户是不透明的。

并非所有导航标签页都对应于 Chrome 界面中的实际标签页，例如正在预渲染的标签页。您无法使用 tabs API 访问此类标签页，也无法通过调用 webNavigation.getFrame() 或 webNavigation.getAllFrames() 请求有关此类标签页的信息。一旦此类标签页被换入，系统就会触发 onTabReplaced 事件，并且可以通过这些 API 访问它们。

请务必注意，操作系统在处理不同的 Chrome 进程时存在一些技术上的怪异之处，可能会导致浏览器本身与扩展程序进程之间的时钟出现偏差。这意味着，WebNavigation 事件的 timeStamp 属性的 timeStamp 属性仅保证内部一致性。将一个事件与另一个事件进行比较会得出它们之间的正确偏移量，但将它们与扩展程序内的当前时间（例如使用 (new Date()).getTime()）进行比较可能会得出意外结果。

标签页中的框架可以通过框架 ID 来标识。主框架的框架 ID 始终为 0，子框架的 ID 为正数。在框架中构建文档后，其框架 ID 在文档的整个生命周期内保持不变。自 Chrome 49 起，此 ID 在框架的整个生命周期内（跨多次导航）也保持不变。

由于 Chrome 采用多进程架构，标签页可能会使用不同的进程来呈现网页的来源和目标。因此，如果导航在新进程中进行，您可能会同时收到来自新网页和旧网页的事件，直到新导航提交（即针对新的主框架发送 onCommitted 事件）为止。换句话说，可能会有多个具有相同 frameId 的待处理 webNavigation 事件序列。可以通过 processId 键区分序列。

另请注意，在临时加载期间，该进程可能会切换多次。当负载重定向到其他网站时，就会发生这种情况。在这种情况下，您会反复收到 onBeforeNavigate 和 onErrorOccurred 事件，直到收到最终的 onCommitted 事件。

扩展程序存在的另一个问题是框架的生命周期。框架托管文档（与已提交的网址相关联）。文档可能会发生变化（例如通过导航），但 frameId 不会变化，因此很难仅通过 frameId 将特定文档中发生的事情关联起来。我们引入了 documentId 的概念，它是每个文档的唯一标识符。如果框架被导航并打开新文档，标识符将会更改。此字段在确定网页何时更改其生命周期状态（在预渲染/有效/缓存之间）时非常有用，因为它保持不变。

webNavigation onCommitted 事件具有 transitionType 和 transitionQualifiers 属性。过渡类型与 History API 中使用的类型相同，用于描述浏览器如何导航到此特定网址。此外，还可以返回多个进一步定义导航的过渡限定符。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 webNavigation API 示例。

导航的原因。使用与 History API 中定义的相同的过渡类型。这些过渡类型与历史记录 API 中定义的过渡类型相同，只是将 "auto_toplevel" 替换为 "start_page"（为了实现向后兼容性）。

Promise<object[] | undefined>

检索有关指定帧的信息。框架是指网页的 <iframe> 或 <frame>，由标签页 ID 和框架 ID 标识。

相应文档的 UUID。如果提供了 frameId 和/或 tabId，系统会验证它们是否与通过提供的文档 ID 找到的文档相匹配。

现在，框架由其标签页 ID 和框架 ID 进行唯一标识；不再需要进程 ID，因此会忽略进程 ID。

Promise<object | undefined>

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。对于给定的标签页和进程，框架 ID 是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

此事件不再设置 processId，因为在 onCommit 之前，无法知道将呈现结果文档的进程。

浏览器即将开始导航的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在导航提交时触发。文档（以及其引用的资源，例如图片和子框架）可能仍在下载，但至少已从服务器收到部分文档，并且浏览器已决定切换到新文档。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当文档（包括其引用的资源）已完全加载并初始化时触发。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

文档完成加载的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当创建新窗口或现有窗口中的新标签页来托管导航时触发。

触发导航的具有 sourceTabId 的框架的 ID。0 表示主框架。

浏览器即将创建新视图的时间（以自纪元以来的毫秒数表示）。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当网页的 DOM 完全构建完毕时触发，但引用的资源可能尚未完成加载。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

网页的 DOM 完全构建的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在发生错误并中止导航时触发。如果发生网络错误或用户中止了导航，则可能会出现这种情况。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

发生错误的时间，以自纪元以来的毫秒数表示。

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当帧的历史记录更新为新网址时触发。相应框架的所有未来事件都将使用更新后的网址。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

在帧的引用 fragment 更新时触发。相应框架的所有未来事件都将使用更新后的网址。

extensionTypes.DocumentLifecycle

0 表示导航发生在标签页内容窗口中；正值表示导航发生在子框架中。框架 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有相应框架的父文档的 UUID。如果没有父级，则不设置此字段。

父框架的 ID，如果这是主框架，则为 -1。

导航提交的时间，以自纪元以来的毫秒数表示。

TransitionQualifier[]

正在导航到的网址必须满足的条件。对于此事件，系统会忽略 UrlFilter 的“schemes”和“ports”字段。

当标签页的内容被另一个（通常是之前预渲染的）标签页替换时触发。

替换发生的时间，以自纪元以来的毫秒数表示。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "webNavigation"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
onBeforeNavigate -> onCommitted -> [onDOMContentLoaded] -> onCompleted
```

Example 3 (unknown):
```unknown
chrome.webNavigation.getAllFrames(  details: object,): Promise<object[] | undefined>
```

Example 4 (unknown):
```unknown
chrome.webNavigation.getFrame(  details: object,): Promise<object | undefined>
```

---

## chrome.printingMetrics 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printingMetrics

**Contents:**
- chrome.printingMetrics 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - ColorMode
    - 枚举
  - DuplexMode
    - 枚举
  - MediaSize

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

“BLACK_AND_WHITE” 指定使用了黑白模式。

“ONE_SIDED” 指定使用了单面打印。

"TWO_SIDED_LONG_EDGE" 指定使用了双面打印，并沿长边翻转。

"TWO_SIDED_SHORT_EDGE" 指定使用了双面打印，并沿短边翻转。

供应商提供的 ID，例如“iso_a3_297x420mm”或“na_index-3x5_3x5in”。可能的值是“media”IPP 属性的值，可在 IANA 页面上找到。

打印机的完整路径。包含协议、主机名、端口和队列。

“POLICY” 指定打印机是通过政策添加的。

作业完成时间（自 Unix 纪元以来经过的毫秒数）。

作业创建时间（以毫秒为单位，从 Unix 纪元开始计算）。

来源的 ID。如果来源为 PRINT_PREVIEW 或 ANDROID_APP，则为 null。

“PRINT_PREVIEW” 指定作业是从用户启动的“打印预览”页面创建的。

“ANDROID_APP” 指定作业是从 Android 应用创建的。

“EXTENSION” 指定作业是由扩展程序通过 Chrome API 创建的。

“ISOLATED_WEB_APP” 指定作业是由独立式 Web 应用通过 API 创建的。

“FAILED” 指定打印作业因某些错误而中断。

“CANCELED” 表示打印作业已由用户或通过 API 取消。

“PRINTED” 表示打印作业已完成打印，未出现任何错误。

Promise<PrintJobInfo[]>

打印作业完成时触发的事件。这包括任何终止状态：FAILED、CANCELED 和 PRINTED。

**Examples:**

Example 1 (unknown):
```unknown
chrome.printingMetrics.getPrintJobs(): Promise<PrintJobInfo[]>
```

Example 2 (unknown):
```unknown
chrome.printingMetrics.onPrintJobFinished.addListener(  callback: function,)
```

Example 3 (javascript):
```javascript
(jobInfo: PrintJobInfo) => void
```

---

## chrome.readingList 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/readingList?hl=zh-cn

**Contents:**
- chrome.readingList 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 商品排序
  - 商品的唯一性
- 使用场景
  - 添加项目
  - 展示商品

使用 chrome.readingList API 读取和修改阅读清单中的内容。

如需使用 Reading List API，请在扩展程序清单文件中添加 "readingList" 权限：

Chrome 具有位于侧边栏中的阅读清单。它可让用户保存网页以供日后阅读或离线阅读。 使用 Reading List API 检索现有项，并向列表添加项或从中移除项。

以下部分展示了 Reading List API 的一些常见用例。如需查看完整的扩展程序示例，请参阅扩展程序示例。

如需将内容添加到阅读清单，请使用 chrome.readingList.addEntry()：

如需显示阅读清单中的内容，请使用 chrome.readingList.query() 方法检索这些内容。

您可以使用 chrome.readingList.updateEntry() 更新标题、网址和阅读状态。以下代码将某项标记为已读：

如需移除某项内容，请使用 chrome.readingList.removeEntry()：

如需查看更多 Reading List API 扩展演示，请参阅 Reading List API 示例。

指示是搜索已读 (true) 还是未读 (false) 项目。

条目的创建时间。以自 1970 年 1 月 1 日以来的毫秒数记录。

相应条目的上次更新时间。此值以自 1970 年 1 月 1 日以来的毫秒数表示。

更新后的已读状态。如果未提供值，则保留现有状态。

如果阅读清单中不存在相应条目，则添加该条目。

检索与 QueryInfo 属性匹配的所有条目。系统不会匹配未提供的属性。

Promise<ReadingListEntry[]>

当向阅读清单添加 ReadingListEntry 时触发。

当从阅读清单中移除 ReadingListEntry 时触发。

当阅读清单中的 ReadingListEntry 更新时触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My reading list extension",
  ...
  "permissions": [
    "readingList"
  ]
}
```

Example 2 (unknown):
```unknown
chrome.readingList.addEntry({
  title: "New to the web platform in September | web.dev",
  url: "https://developer.chrome.com/",
  hasBeenRead: false
});
```

Example 3 (javascript):
```javascript
const items = await chrome.readingList.query({});

for (const item of items) {
  // Do something do display the item
}
```

Example 4 (unknown):
```unknown
chrome.readingList.updateEntry({
  url: "https://developer.chrome.com/",
  hasBeenRead: true
});
```

---

## chrome.enterprise.networkingAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/networkingAttributes?hl=zh-cn

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
    - 返回

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

设备的本地 IPv4 地址（如果未配置，则为未定义）。

设备的本地 IPv6 地址（如果未配置，则为未定义）。

检索设备的默认网络的网络详细信息。如果用户没有关联或设备未连接到网络，系统将设置 runtime.lastError 并附上失败原因。

Promise<NetworkDetails>

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.networkingAttributes.getNetworkDetails(): Promise<NetworkDetails>
```

---

## chrome.omnibox 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/omnibox

**Contents:**
- chrome.omnibox 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - DefaultSuggestResult
    - 属性
  - DescriptionStyleType
    - 枚举
  - OnInputEnteredDisposition

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

当用户输入扩展程序的关键字后，便开始仅与您的扩展程序互动。每次按键操作都会发送到您的扩展程序，您可以提供建议作为响应。

建议可以采用多种方式进行丰富格式设置。当用户接受建议时，您的扩展程序会收到通知，并可以采取相应行动。

如需使用此 API，必须在清单中声明以下键。

您必须在清单中包含 "omnibox.keyword" 字段，才能使用多功能框 API。您还应指定一个 16x16 像素的图标，该图标会在建议用户进入关键字模式时显示在地址栏中。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 omnibox API 示例。

网址下拉菜单中显示的文字。可以包含用于设置样式的 XML 样式标记。支持的标记包括“url”（用于表示字面网址）、“match”（用于突出显示与用户查询匹配的文本）和“dim”（用于表示暗淡的辅助文本）。样式可以嵌套，例如“变暗的匹配项”。

多功能框查询的窗口处置。这是显示结果的推荐上下文。例如，如果多功能框命令是导航到某个网址，则“newForegroundTab”处置方式表示导航应在新选中的标签页中进行。

放入网址栏中的文本，当用户选择此条目时，该文本会发送给扩展程序。

网址下拉菜单中显示的文字。可以包含用于设置样式的 XML 样式标记。支持的标记包括“url”（用于表示字面网址）、“match”（用于突出显示与用户查询匹配的文本）和“dim”（用于表示暗淡的辅助文本）。样式可以嵌套，例如，调暗的匹配项。您必须转义这五个预定义实体，才能将其显示为文本：stackoverflow.com/a/1091953/89484

为默认建议设置说明和样式。默认建议是指显示在网址栏下方的第一个建议行中的文字。

不含“content”参数的部分 SuggestResult 对象。

OnInputEnteredDisposition

用户已通过输入扩展程序的关键字启动了关键字输入会话。保证在每个输入会话中发送一次，并且在任何 onInputChanged 事件之前发送。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Aaron's omnibox extension",
  "version": "1.0",
  "omnibox": { "keyword" : "aaron" },
  "icons": {
    "16": "16-full-color.png"
  },
  "background": {
    "persistent": false,
    "scripts": ["background.js"]
  }
}
```

Example 2 (unknown):
```unknown
chrome.omnibox.setDefaultSuggestion(  suggestion: DefaultSuggestResult,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.omnibox.onDeleteSuggestion.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(text: string) => void
```

---

## 在沙盒化 iframe 中使用 eval() 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/security/sandboxing-eval?hl=zh-cn

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

## chrome.audio 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/audio

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

指定应处于活跃状态的设备的 ID。如果未设置输入列表或输出列表，相应类别的设备不受影响。

为流类型设置静音状态。静音状态将应用于具有指定音频流类型的所有音频设备。

在音频设备发生更改时触发，无论是添加新设备还是移除现有设备。

当音频输入或输出的静音状态发生变化时触发。请注意，静音状态是系统范围的，新值适用于具有指定音频流类型的每个音频设备。

**Examples:**

Example 1 (unknown):
```unknown
chrome.audio.getDevices(  filter?: DeviceFilter,): Promise<AudioDeviceInfo[]>
```

Example 2 (unknown):
```unknown
chrome.audio.getMute(  streamType: StreamType,): Promise<boolean>
```

Example 3 (unknown):
```unknown
chrome.audio.setActiveDevices(  ids: DeviceIdLists,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.audio.setMute(  streamType: StreamType,  isMuted: boolean,): Promise<void>
```

---

## chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/deviceAttributes?hl=zh-cn

**Contents:**
- chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - getDeviceAnnotatedLocation()
    - 返回
  - getDeviceAssetId()
    - 返回
  - getDeviceHostname()

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

获取管理员注释的位置信息。如果当前用户没有关联的组织，或者管理员未设置带注释的位置，则返回空字符串。

获取管理员注释的资产 ID。如果当前用户没有关联的资产，或者管理员未设置任何资产 ID，则返回空字符串。

获取由 DeviceHostnameTemplate 政策设置的设备主机名。如果当前用户未关联或企业政策未设置主机名，则返回空字符串。

获取设备的序列号。请注意，此 API 的目的是管理设备（例如，为设备级证书生成证书签名请求）。未经设备管理员同意，不得使用此 API 跟踪设备。如果当前用户没有关联的商家，则返回空字符串。

获取 Directory API 的设备标识符的值，该值由服务器生成，用于标识设备在 Cloud Directory API 中的云记录，以便在 Cloud Directory API 中进行查询。如果当前用户没有关联的商家，则返回空字符串。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAnnotatedLocation(): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAssetId(): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceHostname(): Promise<string>
```

Example 4 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceSerialNumber(): Promise<string>
```

---

## chrome.privacy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/privacy?hl=zh-cn

**Contents:**
- chrome.privacy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - IPHandlingPolicy
    - 枚举
- 属性
  - network

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

您必须在扩展程序的清单中声明“隐私权”权限，才能使用该 API。例如：

读取 Chrome 设置的当前值非常简单。您需要先找到感兴趣的属性，然后对该对象调用 get()，以便检索其当前值和扩展程序的控制级别。例如，如需确定 Chrome 的信用卡自动填充功能是否已启用，您可以编写以下代码：

更改设置的值稍微复杂一些，因为您必须先验证扩展程序是否可以控制该设置。如果您的扩展程序切换的设置要么通过企业政策锁定为特定值（levelOfControl 将设置为“not_controllable”），要么由其他扩展程序控制该值（levelOfControl 将设置为“controlled_by_other_extensions”），那么用户不会看到其设置有任何变化。set() 调用将成功，但设置会立即被覆盖。由于这可能会让用户感到困惑，因此建议在用户选择的设置实际上未应用时提醒用户。

这意味着，您应该使用 get() 方法来确定您的访问权限级别，然后仅当扩展程序可以控制相应设置时才调用 set()（实际上，如果扩展程序无法控制相应设置，最好在视觉上停用该功能，以免用户感到困惑）：

如果您对设置值的变化感兴趣，请为其 onChange 事件添加监听器。除了其他用途之外，此功能还允许您在最近安装的扩展程序获取设置控制权或企业政策替换您的控制权时警告用户。如需监听信用卡自动填充状态的变化，例如，以下代码就足够了：

如需试用此 API，请从 chrome-extension-samples 代码库中安装隐私权 API 示例。

"default_public_and_private_interfaces"

"default_public_interface_only"

"disable_non_proxied_udp"

影响 Chrome 一般网络连接处理方式的设置。

types.ChromeSetting<boolean>

如果启用，Chrome 会尝试预先解析 DNS 条目并抢先打开与服务器的 TCP 和 SSL 连接，从而加快您的网页浏览速度。此偏好设置仅影响 Chrome 内部预测服务采取的操作。它不会影响网页发起的预取或预连接。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<IPHandlingPolicy>

允许用户指定媒体性能/隐私权权衡，这会影响 WebRTC 流量的路由方式以及公开的本地地址信息量。此偏好的值为 IPHandlingPolicy 类型，默认值为 default。

用于启用或停用需要 Google 和默认搜索引擎提供的第三方网络服务的功能的设置。

types.ChromeSetting<boolean>

如果启用，Chrome 会使用网络服务来帮助解决导航错误。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会建议自动填充地址和其他表单数据。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会提供自动填写信用卡表单的功能。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

请改用 privacy.services.autofillAddressEnabled 和 privacy.services.autofillCreditCardEnabled。此属性保留在此版本中是为了实现向后兼容性，但未来会移除。

如果启用此设置，Chrome 会提供自动填写表单的选项。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

启用此项后，密码管理工具会询问您是否要保存密码。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会尽最大努力保护您免遭钓鱼式攻击和恶意软件的侵害。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果此政策处于启用状态，当安全浏览功能阻止某个网页时，Chrome 会向 Google 发送额外信息，例如被阻止网页的内容。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会将您在多功能框中输入的文字发送给您的默认搜索引擎，后者会根据您目前输入的文字预测可能的网站和搜索补全选项。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会使用网络服务来帮助修正拼写错误。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果启用此政策，Chrome 会询问是否翻译非您所用语言的网页。此偏好的值为布尔值，默认值为 true。

用于确定 Chrome 向网站提供哪些信息的设置。

types.ChromeSetting<boolean>

如果停用，Attribution Reporting API 和 Private Aggregation API 将被停用。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用这些 API。如果您尝试将这些 API 设置为 true，系统会抛出错误。

types.ChromeSetting<boolean>

如果启用，Chrome 会在您的请求中发送“请勿跟踪”标头 (DNT: 1)。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果停用，Fledge API 将处于停用状态。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

types.ChromeSetting<boolean>

如果启用，Chrome 会在网站请求时发送审核 ping (<a ping>)。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

仅适用于 Windows 和 ChromeOS：如果启用，Chrome 会向插件提供一个唯一 ID，以便运行受保护的内容。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会随请求发送 referer 标头。是的，此偏好的名称与拼写错误的标头不一致。不会，我们不会更改。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果停用，Related Website Sets 会被停用。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

types.ChromeSetting<boolean>

如果停用，Chrome 会阻止第三方网站设置 Cookie。此偏好的值为布尔值，默认值为 true。扩展程序不得在无痕模式下启用此 API。在无痕模式下，第三方 Cookie 会被屏蔽，并且只能在网站级别允许使用。如果您尝试在无痕模式下将此 API 设置为 true，则会抛出错误。

注意：如果个别网站具有有效的豁免，或者它们改用 Storage Access API，则即使此 API 返回 false，它们可能仍能访问第三方 Cookie。

types.ChromeSetting<boolean>

如果停用，Topics API 将处于停用状态。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "privacy"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.get({}, function(details) {
  if (details.value) {
    console.log('Autofill is on!');
  } else {
    console.log('Autofill is off!');
  }
});
```

Example 3 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.get({}, function(details) {
  if (details.levelOfControl === 'controllable_by_this_extension') {
    chrome.privacy.services.autofillCreditCardEnabled.set({ value: true }, function() {
      if (chrome.runtime.lastError === undefined) {
        console.log("Hooray, it worked!");
      } else {
        console.log("Sadness!", chrome.runtime.lastError);
      }
    });
  }
});
```

Example 4 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.onChange.addListener(
  function (details) {
    // The new value is stored in `details.value`, the new level of control
    // in `details.levelOfControl`, and `details.incognitoSpecific` will be
    // `true` if the value is specific to Incognito mode.
  }
);
```

---

## chrome.gcm 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/gcm

**Contents:**
- chrome.gcm 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 属性
  - MAX_MESSAGE_SIZE
    - 值
- 方法
  - register()
    - 参数
    - 返回

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

消息中所有键值对的大小上限（以字节为单位）。

向 FCM 注册应用。注册 ID 将由 callback 返回。如果使用相同的 senderIds 列表再次调用 register，则会返回相同的注册 ID。

允许向应用发送消息的服务器 ID 的列表。应包含至少一个且不超过 100 个发件人 ID。

要发送到服务器的消息数据。不区分大小写的 goog. 和 google 以及区分大小写的 collapse_key 不允许用作键前缀。所有键/值对的总和不应超过 gcm.MAX_MESSAGE_SIZE。

要向其发送消息的服务器的 ID，由 Google API 控制台分配。

消息的 ID。在应用范围内，每个消息都必须具有唯一的 ID。如需有关选择和处理 ID 的建议，请参阅 Cloud Messaging 文档。

消息的存留时间（以秒为单位）。如果无法在该时间段内发送消息，系统将引发 onSendError 事件。生命周期为 0 表示消息应立即发送，如果无法发送，则应失败。生命周期的默认值为 86,400 秒（1 天），最大值为 2,419,200 秒（28 天）。

消息的折叠键。如需了解详情，请参阅不可折叠消息和可折叠消息。

当 FCM 服务器必须删除应用服务器发送给应用的消息时触发。如需详细了解如何处理此事件，请参阅消息的生命周期。

出现此错误的消息的 ID（如果错误与特定消息相关）。

**Examples:**

Example 1 (unknown):
```unknown
chrome.gcm.register(  senderIds: string[],): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.gcm.send(  message: object,): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.gcm.unregister(): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.gcm.onMessage.addListener(  callback: function,)
```

---

## chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/dns

**Contents:**
- chrome.dns 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 用法
- 类型
  - ResolveCallbackResolveInfo
    - 属性
- 方法
  - resolve()

使用 chrome.dns API 进行 DNS 解析。

如需使用此 API，您必须在清单中声明 "dns" 权限。

以下代码调用 resolve() 以检索 example.com 的 IP 地址。

表示 IP 地址字面值的字符串。仅当 resultCode 指示成功时才提供。

Promise<ResolveCallbackResolveInfo>

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
chrome.dns.resolve(  hostname: string,): Promise<ResolveCallbackResolveInfo>
```

---

## chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/declarativeContent?hl=zh-cn

**Contents:**
- chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 规则
  - 网页网址匹配
  - CSS 匹配
  - 书签状态匹配
- 类型
  - ImageDataType

使用 chrome.declarativeContent API 可根据网页内容执行操作，而无需读取网页内容的权限。

声明式 Content API 可让您根据 或者 CSS 选择器与页面上的某个元素匹配，无需 添加主机权限或注入内容脚本。

使用 activeTab 权限，以在用户点击 操作。

规则由条件和操作组成。如果满足任一条件，则所有操作 。这些操作包括 setIcon() 和 showAction()。

当且仅当所有网页都列出时，PageStateMatcher 才与网页匹配 条件。可与网页网址、CSS 复合选择器匹配 或网页的已添加书签状态。以下规则启用 当有密码字段存在时，扩展程序在 Google 网页上执行的操作：

如果还要为包含视频的 Google 网站启用该扩展程序的操作， 条件，因为每个条件足以触发所有指定操作：

onPageChanged 事件测试是否有任何规则至少满足一条规则 条件并执行操作。浏览会话时，规则会保留下来；因此，在 则首先应使用 removeRules 清除 然后使用 addRules 注册新的规则。

如果有 activeTab 权限，您的扩展程序不会显示任何权限 警告，并且当用户点击该扩展程序操作时，该扩展程序只会在相关网页上运行。

当满足网址条件时，PageStateMatcher.pageurl 即为匹配。通过 最常见的条件是主机、路径或网址串联，后跟包含、等于、前缀或 后缀。下表包含几个示例：

所有条件均区分大小写。如需条件的完整列表，请参阅 UrlFilter。

PageStateMatcher.css 条件必须是复合选择器， 也就是说，您不能包含空格或“>”等组合词在您的 。这有助于 Chrome 更高效地匹配选择器。

CSS 条件仅匹配显示的元素：如果与选择器匹配的元素 display:none 或其父元素之一为 display:none，但不会导致条件 匹配。使用 visibility:hidden 设置样式的元素、位于屏幕外或被其他元素隐藏的元素 仍然可以匹配您的条件

PageStateMatcher.isBookmarked 条件允许匹配 用户个人资料中当前网址的书签状态。要使用此条件 "书签"权限必须在扩展程序清单中声明。

请参阅 https://developer.mozilla.org/en-US/docs/Web/API/ImageData。

如果数组中的所有 CSS 选择器都与与页面主框架同源的框架中的显示元素相匹配，则匹配。为了加快匹配速度，此数组中的所有选择器都必须是复合选择器。注意：列出数百个 CSS 选择器或列出每个网页匹配数百次的 CSS 选择器可能会降低网站的加载速度。

如果网页的书签状态等于指定值，则匹配。需要书签权限。

如果网页的顶级网址满足 UrlFilter 的条件，则匹配。

警告：此操作仍处在实验阶段，不支持 Chrome 稳定版。

内容脚本是在匹配网页的所有帧中运行，还是仅在顶部帧中运行。默认值为 false。

要作为内容脚本的一部分注入的 CSS 文件的名称。

作为内容脚本的一部分注入的 JavaScript 文件的名称。

是否在 about:blank 和 about:srcdoc 中插入内容脚本。默认值为 false。

声明式事件操作，在满足相应条件时，为扩展程序的网页操作或浏览器操作设置 n-dip 方形图标。此操作无需主机权限即可使用，但必须对扩展程序执行网页或浏览器操作。

必须且只能指定 imageData 和 path 中的一个。两者都是将多个像素映射到图像表示的字典。imageData 中的图片表示形式是一个 ImageData 对象；，而 path 中的图片表示形式是图片文件相对于扩展程序清单的路径。canvas如果 scale 屏幕像素适合设备无关像素，则系统会使用 scale * n 图标。如果该比例缺失，则将另一张图片调整为所需的大小。

ImageData 对象或字典 {size ->ImageData}，表示要设置的图标。如果将图标指定为字典，则系统会根据屏幕的像素密度选择使用的图片。如果适合一个屏幕空间单元的图片像素数等于 scale，则会选择尺寸为 scale * n 的图片，其中 n 是界面中图标的尺寸。必须至少指定一张图片。请注意，details.imageData = foo 相当于 details.imageData = {'16': foo}。

一种声明式事件操作，可在满足相应条件时将扩展程序的工具栏操作设置为启用状态。此操作无需主机权限即可执行。如果扩展程序具有 activeTab 权限，点击网页操作即可授予对活动标签页的访问权限。

在不符合这些条件的网页上，扩展程序的工具栏操作会变为灰度模式，点击该按钮会打开上下文菜单，而不会触发操作。

请使用 declarativeContent.ShowAction。

一种声明式事件操作，可在满足相应条件时将扩展程序的网页操作设为启用状态。此操作无需主机权限也可使用，但扩展程序必须包含网页操作。如果扩展程序具有 activeTab 权限，点击网页操作即可授予对活动标签页的访问权限。

在不符合这些条件的网页上，扩展程序的工具栏操作会变为灰度模式，点击该按钮会打开上下文菜单，而不会触发操作。

提供由 addRules、removeRules 和 getRules 组成的声明式事件 API。

**Examples:**

Example 1 (javascript):
```javascript
let rule1 = {
  conditions: [
    new chrome.declarativeContent.PageStateMatcher({
      pageUrl: { hostSuffix: '.google.com', schemes: ['https'] },
      css: ["input[type='password']"]
    })
  ],
  actions: [ new chrome.declarativeContent.ShowAction() ]
};
```

Example 2 (javascript):
```javascript
let rule2 = {
  conditions: [
    new chrome.declarativeContent.PageStateMatcher({
      pageUrl: { hostSuffix: '.google.com', schemes: ['https'] },
      css: ["input[type='password']"]
    }),
    new chrome.declarativeContent.PageStateMatcher({
      css: ["video"]
    })
  ],
  actions: [ new chrome.declarativeContent.ShowAction() ]
};
```

Example 3 (unknown):
```unknown
chrome.runtime.onInstalled.addListener(function(details) {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([rule2]);
  });
});
```

Example 4 (javascript):
```javascript
(arg: PageStateMatcher) => {...}
```

---

## chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/network?hl=zh-cn

**Contents:**
- chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - Request
    - 属性
- 方法
  - getHAR()
    - 参数

使用 chrome.devtools.network API 检索由开发者工具在“Network”面板中显示的网络请求的相关信息。

网络请求信息以 HTTP 归档格式 (HAR) 表示。以下各项的说明： HAR 不在本文档的讨论范围内，请参阅 HAR v1.2 规范。

对于 HAR，chrome.devtools.network.getHAR() 方法会返回整个 HAR 日志，而 chrome.devtools.network.onRequestFinished 事件提供 HAR 条目作为事件的参数 回调。

请注意，出于效率方面的原因，请求内容未包含在 HAR 中。您可以拨打 请求的 getContent() 方法来检索内容。

如果在网页加载后打开“开发者工具”窗口， 由 getHAR() 返回的条目数组。请重新加载页面以获取所有请求。一般来说， getHAR() 返回的请求列表应与“Network”面板中显示的请求列表一致。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

必须在清单中声明以下键才能使用此 API。

以下代码会在加载时记录所有超过 40KB 的图片的网址：

若要试用此 API，请安装 chrome-extension-samples 中的 chrome-extension-samples 存储库

表示对文档资源（脚本、图片等）的网络请求。有关参考信息，请参阅 HAR 规范。

如果内容未经编码，则为空，否则为名称编码。目前只支持 base64。

返回包含所有已知网络请求的 HAR 日志。

HAR 日志。如需了解详情，请参阅 HAR 规范。

在网络请求完成且所有请求数据都可用时触发。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.network.onRequestFinished.addListener(
  function(request) {
    if (request.response.bodySize > 40*1024) {
      chrome.devtools.inspectedWindow.eval(
          'console.log("Large image: " + unescape("' +
          escape(request.request.url) + '"))');
    }
  }
);
```

Example 2 (javascript):
```javascript
(callback: function) => {...}
```

Example 3 (javascript):
```javascript
(content: string, encoding: string) => void
```

Example 4 (unknown):
```unknown
chrome.devtools.network.getHAR(  callback: function,): void
```

---

## chrome.fontSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fontSettings

**Contents:**
- chrome.fontSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - FontName
    - 属性
  - GenericFamily
    - 枚举

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

如需使用字体设置 API，您必须在扩展程序清单中声明 "fontSettings" 权限。例如：

Chrome 允许某些字体设置取决于某些通用字体系列和语言文字。例如，用于无衬线简体中文字体的字体可能与用于衬线日文字体的字体不同。

Chrome 支持的通用字体系列基于 CSS 通用字体系列，并列在 GenericReference 下。当网页指定了通用字体系列时，Chrome 会根据相应设置选择字体。如果未指定任何通用字体系列，Chrome 会使用“标准”通用字体系列的设置。

当网页指定语言时，Chrome 会根据相应语言文字的设置选择字体。如果未指定语言，Chrome 会使用默认脚本或全局脚本的设置。

受支持的语言文字由 ISO 15924 文字代码指定，并列在 ScriptCode 下。从技术上讲，Chrome 设置并非严格按脚本进行，还取决于语言。例如，当网页指定俄语时，Chrome 会选择西里尔文字体（ISO 15924 文字代码“Cyrl”），并且不仅将此字体用于西里尔文字，还会用于该字体涵盖的所有内容，例如拉丁文字。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 fontSettings API 示例。

以下值之一： not\_controllable：无法由任何扩展程序控制 controlled\_by\_other\_extensions：由优先级较高的扩展程序控制 controllable\_by\_this\_extension：可由此扩展程序控制 controlled\_by\_this\_extension：由此扩展程序控制

"controlled_by_other_extensions"

"controllable_by_this_extension"

"controlled_by_this_extension"

ISO 15924 文字代码。默认脚本（即全局脚本）由脚本代码“Zyyy”表示。

清除此扩展程序设置的默认固定字体大小（如果有）。

应清除字体的脚本。如果省略，则会清除全局脚本字体设置。

应检索字体的脚本。如果省略，则检索全局脚本（脚本代码“Zyyy”）的字体设置。

字体 ID。空字符串表示回退到全局脚本字体设置。

应设置的字体所对应的脚本代码。如果省略，则会设置全局脚本（脚本代码“Zyyy”）的字体设置。

字体 ID。请参阅 getFont 中的说明。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My Font Settings Extension",
  "description": "Customize your fonts",
  "version": "0.2",
  "permissions": [
    "fontSettings"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.fontSettings.getFont(
  { genericFamily: 'standard', script: 'Arab' },
  function(details) { console.log(details.fontId); }
);
```

Example 3 (unknown):
```unknown
chrome.fontSettings.setFont(
  { genericFamily: 'sansserif', script: 'Jpan', fontId: 'MS PGothic' }
);
```

Example 4 (unknown):
```unknown
chrome.fontSettings.clearDefaultFixedFontSize(  details?: object,): Promise<void>
```

---

## chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/platformKeys?hl=zh-cn

**Contents:**
- chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Algorithm
    - 枚举
  - ChallengeKeyOptions
    - 属性

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

使用此 API 注册客户端证书的典型步骤如下：

使用 enterprise.platformKeys.getTokens() 获取所有可用令牌。

查找 id 等于 "user" 的令牌。随后使用此令牌。

使用 generateKey() Token 方法（在 SubtleCrypto 中定义）生成密钥对。这将返回密钥的句柄。

使用 exportKey() 令牌方法（在 SubtleCrypto 中定义）导出公钥。

使用 sign() Token 方法（在 SubtleCrypto 中定义）创建认证请求数据的签名。

如果收到证书，请使用 [enterprise.platformKeys.importCertificate()`[3]

以下示例展示了除构建和发送认证请求之外的主要 API 互动：

由 Verified Access Web API 发出的质询。

RegisterKeyOptions 可选

如果存在，则使用指定的 scope 的令牌注册受质询的密钥。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。随后对该函数的调用将在指定的 scope 中生成新的企业密钥。

静态 ID 为 "user" 和 "system"，分别是指平台的用户专用硬件令牌和系统范围的硬件令牌。任何其他令牌（带有其他标识符）都可能由 enterprise.platformKeys.getTokens 返回。

实现 WebCrypto 的 SubtleCrypto 接口。加密操作（包括密钥生成）由软件支持。密钥的保护以及不可提取属性的实现是在软件中完成的，因此密钥的保护程度不如硬件支持的密钥。

只能生成不可提取的密钥。支持的密钥类型为 RSASSA-PKCS1-V1_5 和 RSA-OAEP（在 Chrome 版本 135 及更高版本中），密钥长度为 modulusLength，最高可达 2048。每个 RSASSA-PKCS1-V1_5 密钥最多只能用于一次数据签名，除非通过 KeyPermissions 政策将相应扩展程序列入许可名单，在这种情况下，该密钥可以无限期使用。自 Chrome 版本 135 起，RSA-OAEP 密钥受到支持，并且通过同一政策列入许可名单的扩展程序可以使用这些密钥来解封装其他密钥。

在特定 Token 上生成的密钥不能用于任何其他令牌，也不能用于 window.crypto.subtle。同样，使用 window.crypto.subtle 创建的 Key 对象不能与此接口搭配使用。

实现 WebCrypto 的 SubtleCrypto 接口。加密操作（包括密钥生成）由硬件支持。

只能生成不可提取的密钥。支持的密钥类型包括 RSASSA-PKCS1-V1_5 和 RSA-OAEP（在 Chrome 版本 135 及更高版本中）以及 modulusLength 最多 2048 位的 ECDSA 和 namedCurve P-256。每个 RSASSA-PKCS1-V1_5 和 ECDSA 密钥最多只能用于一次数据签名，除非通过 KeyPermissions 政策将相应扩展程序列入许可名单，在这种情况下，密钥可以无限期使用。自 Chrome 版本 135 起，RSA-OAEP 密钥受到支持，并且通过同一政策列入许可名单的扩展程序可以使用这些密钥来解封装其他密钥。

在特定 Token 上生成的密钥不能用于任何其他令牌，也不能用于 window.crypto.subtle。同样，使用 window.crypto.subtle 创建的 Key 对象不能与此接口搭配使用。

与 challengeMachineKey 和 challengeUserKey 类似，但允许指定已注册密钥的算法。对由硬件支持的企业机器密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。

如果 Verified Access Web API 成功完成验证，则表明当前设备是合法的 ChromeOS 设备，当前设备受验证期间指定的网域管理，当前登录的用户受验证期间指定的网域管理，并且当前设备状态符合企业设备政策。例如，某项政策可能规定设备不得处于开发者模式。验证所发出的任何设备身份都与当前设备的硬件紧密绑定。如果指定了 "user" 范围，则身份也会与当前登录的用户紧密绑定。

此函数受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业设备政策未明确为调用方启用此操作，则此函数将失败。受质询的密钥不位于 "system" 或 "user" 令牌中，并且无法通过任何其他 API 进行访问。

包含 ChallengeKeyOptions 中定义的字段的对象。

对由硬件支持的企业机器密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业设备政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证功能发出的任何设备身份都与当前设备的硬件紧密绑定。此函数受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业设备政策未明确为调用方启用此操作，则此函数将失败。企业机器密钥不位于 "system" 令牌中，并且无法通过任何其他 API 进行访问。

由 Verified Access Web API 发出的质询。

如果已设置，则当前企业机器密钥会注册为 "system" 令牌，并放弃企业机器密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业机器密钥。

对硬件支持的企业用户密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业用户政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证所发出的公钥与当前设备的硬件和当前登录用户紧密绑定。此功能受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业用户政策未明确为调用方启用此操作，则此功能将失败。企业用户密钥不位于 "user" 令牌中，任何其他 API 都无法访问该密钥。

由 Verified Access Web API 发出的质询。

如果设置，则当前企业用户密钥会注册到 "user" 令牌，并放弃企业用户密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业用户密钥。

返回指定令牌中的所有可用客户端证书的列表。可用于检查可用于特定身份验证的客户端证书是否存在以及是否过期。

Promise<ArrayBuffer[]>

返回可用令牌。在常规用户的会话中，该列表将始终包含用户的令牌，且该令牌具有 id "user"。如果存在系统级 TPM token，则返回的列表还将包含具有 id "system" 的系统级 token。对于相应设备（例如 Chromebook）上的所有会话，系统级令牌都将相同。

如果认证密钥已存储在相应令牌中，则将 certificate 导入到相应令牌。成功发出认证请求后，应使用此函数存储获得的证书，并使其可供操作系统和浏览器用于身份验证。

从给定令牌中移除 certificate（如果存在）。应使用此方法移除过时的证书，以免在身份验证期间考虑这些证书，并避免证书选择过程过于杂乱。应使用此方法释放证书存储区中的存储空间。

**Examples:**

Example 1 (unknown):
```unknown
function getUserToken(callback) {
  chrome.enterprise.platformKeys.getTokens(function(tokens) {
    for (var i = 0; i < tokens.length; i++) {
      if (tokens[i].id == "user") {
        callback(tokens[i]);
        return;
      }
    }
    callback(undefined);
  });
}

function generateAndSign(userToken) {
  var data = new Uint8Array([0, 5, 1, 2, 3, 4, 5, 6]);
  var algorithm = {
    name: "RSASSA-PKCS1-v1_5",
    // RsaHashedKeyGenParams
    modulusLength: 2048,
    publicExponent:
        new Uint8Array([0x01, 0x00, 0x01]),  // Equivalent to 65537
    hash: {
      name: "SHA-256",
    }
  };
  var cachedKeyPair;
  userToken.subtleCrypto.generateKey(algorithm, false, ["sign"])
    .then(function(keyPair) {
            cachedKeyPair = keyPair;
            return userToken.subtleCrypto.exportKey("spki", keyPair.publicKey);
          },
          console.log.bind(console))
    .then(function(publicKeySpki) {
            // Build the Certification Request using the public key.
            return userToken.subtleCrypto.sign(
                {name : "RSASSA-PKCS1-v1_5"}, cachedKeyPair.privateKey, data);
          },
          console.log.bind(console))
    .then(function(signature) {
              // Complete the Certification Request with |signature|.
              // Send out the request to the CA, calling back
              // onClientCertificateReceived.
          },
          console.log.bind(console));
}

function onClientCertificateReceived(userToken, certificate) {
  chrome.enterprise.platformKeys.importCertificate(userToken.id, certificate);
}

getUserToken(generateAndSign);
```

Example 2 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeKey(  options: ChallengeKeyOptions,): Promise<ArrayBuffer>
```

Example 3 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeMachineKey(  challenge: ArrayBuffer,  registerKey?: boolean,): Promise<ArrayBuffer>
```

Example 4 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeUserKey(  challenge: ArrayBuffer,  registerKey: boolean,): Promise<ArrayBuffer>
```

---

## chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/certificateProvider

**Contents:**
- chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Algorithm
    - 枚举
  - CertificateInfo
    - 属性

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用此 API 向 ChromeOS 公开客户端证书的典型步骤如下：

实际步骤顺序可能会有所不同。例如，如果使用自动选择证书的企业政策，系统就不会要求用户选择证书（请参阅 AutoSelectCertificateForUrls 和面向用户的 Chrome 政策）。

"RSASSA_PKCS1_v1_5_MD5_SHA1" 指定采用 MD5-SHA-1 哈希的 RSASSA PKCS#1 v1.5 签名算法。扩展程序不得预先添加 DigestInfo 前缀，而只能添加 PKCS#1 填充。此算法已被弃用，自版本 109 起，Chrome 将不再请求使用此算法。

"RSASSA_PKCS1_v1_5_SHA1" 指定使用 SHA-1 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA256" 指定使用 SHA-256 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA384" 指定使用 SHA-384 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

"RSASSA_PKCS1_v1_5_SHA512" 指定使用 SHA-512 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。

“RSASSA_PSS_SHA256” 指定 RSASSA PSS 签名算法，使用 SHA-256 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。

"RSASSA_PSS_SHA384" 指定 RSASSA PSS 签名算法，该算法使用 SHA-384 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。

“RSASSA_PSS_SHA512” 指定 RSASSA PSS 签名算法，该算法使用 SHA-512 哈希函数、MGF1 掩码生成函数以及与哈希大小相同的盐。

必须是 X.509 证书的 DER 编码。目前仅支持使用 RSA 密钥的证书。

必须设置为相应证书支持的所有哈希。此扩展程序只会要求对使用这些哈希算法之一计算出的摘要进行签名。应按哈希偏好程度降序排列。

要传递给 setCertificates 的请求标识符。

该数组必须包含 X.509 客户端证书的 DER 编码作为其第一个元素。

相应证书支持的所有算法。系统只会要求扩展程序使用这些算法之一进行签名。

“MD5_SHA1” 指定 MD5 和 SHA1 哈希算法。

“SHA256” 指定 SHA256 哈希处理算法。

“SHA384” 指定 SHA384 哈希处理算法。

“SHA512” 指定 SHA512 哈希算法。

可通过 requestPin 函数向用户显示的错误类型。

“INVALID_PIN” 指定 PIN 码无效。

“INVALID_PUK” 指定 PUK 无效。

“MAX_ATTEMPTS_EXCEEDED” 指定已超出最大尝试次数。

“UNKNOWN_ERROR” 指定错误无法用上述类型表示。

扩展程序通过 requestPin 函数请求的代码类型。

“PIN 码” 指定所请求的代码是 PIN 码。

用户提供的代码。如果用户关闭了对话框或发生了其他错误，则为空。

通过 onSignatureRequested 事件接收到的请求标识符。

剩余尝试次数。提供此信息是为了让任何界面都能向用户显示此信息。Chrome 不会强制执行此操作，而是当 PIN 码请求数超出时，扩展程序应调用 stopPinRequest 并将 errorType 设置为 MAX_ATTEMPTS_EXCEEDED。

PinRequestErrorType 可选

向用户显示的错误模板。如果之前的请求失败，则应设置此参数，以将失败原因通知给用户。

所请求的验证码类型。默认值为 PIN 码。

Chrome 在 SignRequest 中提供的 ID。

在响应 onCertificatesUpdateRequested 时调用，应包含收到的 certificatesRequestId 值。否则，应取消设置。

ClientCertificateInfo[]

提取证书时发生的错误（如果有）。系统会在适当的时候向用户显示此错误。

X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 input 进行签名。

要签名的数据。请注意，数据未经过哈希处理。

要传递给 reportSignature 的请求标识符。

X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 digest 进行签名。

供扩展程序使用的唯一 ID，如果扩展程序需要调用需要此 ID 的方法（例如 requestPin），则应使用此 ID。

PinRequestErrorType 可选

错误模板。如果存在，则会向用户显示。旨在包含因错误而停止流程的原因，例如 MAX_ATTEMPTS_EXCEEDED。

Chrome 在 SignRequest 中提供的 ID。

应作为对 onSignatureRequested 的响应进行调用。

扩展程序必须最终为每个 onSignatureRequested 事件调用此函数；API 实现会在一段时间后停止等待此调用，并在调用此函数时以超时错误进行响应。

ReportSignatureDetails

向用户请求 PIN 码。一次只能有一个正在进行的请求。在另一个流程正在进行时发出的请求会被拒绝。如果另一个流程正在进行中，扩展程序应负责稍后重试。

Promise<PinResponseDetails | undefined>

扩展程序应在初始化后以及当前可用证书集发生每次更改时调用此函数。扩展程序还应在每次收到此事件时，调用此函数以响应 onCertificatesUpdateRequested。

SetCertificatesDetails

停止由 requestPin 函数启动的 PIN 码请求。

StopPinRequestDetails

如果通过 setCertificates 设置的证书不足，或者浏览器请求更新后的信息，则会触发此事件。扩展程序必须使用更新后的证书列表和收到的 certificatesRequestId 调用 setCertificates。

CertificatesUpdateRequest

每次浏览器需要使用此扩展程序通过 setCertificates 提供的证书对消息进行签名时，都会触发此事件。

扩展程序必须使用适当的算法和私钥对来自 request 的输入数据进行签名，并通过使用收到的 signRequestId 调用 reportSignature 来返回签名。

**Examples:**

Example 1 (javascript):
```javascript
function collectAvailableCertificates() {
  // Return all certificates that this Extension can currently provide.
  // For example:
  return [{
    certificateChain: [new Uint8Array(...)],
    supportedAlgorithms: ['RSASSA_PKCS1_v1_5_SHA256']
  }];
}

// The Extension calls this function every time the currently available list of
// certificates changes, and also once after the Extension's initialization.
function onAvailableCertificatesChanged() {
  chrome.certificateProvider.setCertificates({
    clientCertificates: collectAvailableCertificates()
  });
}

function handleCertificatesUpdateRequest(request) {
  // Report the currently available certificates as a response to the request
  // event. This is important for supporting the case when the Extension is
  // unable to detect the changes proactively.
  chrome.certificateProvider.setCertificates({
    certificatesRequestId: request.certificatesRequestId,
    clientCertificates: collectAvailableCertificates()
  });
}

// Returns a private key handle for the given DER-encoded certificate.
// |certificate| is an ArrayBuffer.
function getPrivateKeyHandle(certificate) {...}

// Digests and signs |input| with the given private key. |input| is an
// ArrayBuffer. |algorithm| is an Algorithm.
// Returns the signature as ArrayBuffer.
function signUnhashedData(privateKey, input, algorithm) {...}

function handleSignatureRequest(request) {
  // Look up the handle to the private key of |request.certificate|.
  const key = getPrivateKeyHandle(request.certificate);
  if (!key) {
    // Handle if the key isn't available.
    console.error('Key for requested certificate no available.');

    // Abort the request by reporting the error to the API.
    chrome.certificateProvider.reportSignature({
      signRequestId: request.signRequestId,
      error: 'GENERAL_ERROR'
    });
    return;
  }

  const signature = signUnhashedData(key, request.input, request.algorithm);
  chrome.certificateProvider.reportSignature({
    signRequestId: request.signRequestId,
    signature: signature
  });
}

chrome.certificateProvider.onCertificatesUpdateRequested.addListener(
    handleCertificatesUpdateRequest);
chrome.certificateProvider.onSignatureRequested.addListener(
    handleSignatureRequest);
```

Example 2 (unknown):
```unknown
chrome.certificateProvider.reportSignature(  details: ReportSignatureDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.certificateProvider.requestPin(  details: RequestPinDetails,): Promise<PinResponseDetails | undefined>
```

Example 4 (unknown):
```unknown
chrome.certificateProvider.setCertificates(  details: SetCertificatesDetails,): Promise<void>
```

---

## chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/deviceAttributes

**Contents:**
- chrome.enterprise.deviceAttributes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - getDeviceAnnotatedLocation()
    - 返回
  - getDeviceAssetId()
    - 返回
  - getDeviceHostname()

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

获取管理员注释的位置信息。如果当前用户没有关联的组织，或者管理员未设置带注释的位置，则返回空字符串。

获取管理员注释的资产 ID。如果当前用户没有关联的资产，或者管理员未设置任何资产 ID，则返回空字符串。

获取由 DeviceHostnameTemplate 政策设置的设备主机名。如果当前用户未关联或企业政策未设置主机名，则返回空字符串。

获取设备的序列号。请注意，此 API 的目的是管理设备（例如，为设备级证书生成证书签名请求）。未经设备管理员同意，不得使用此 API 跟踪设备。如果当前用户没有关联的商家，则返回空字符串。

获取 Directory API 的设备标识符的值，该值由服务器生成，用于标识设备在 Cloud Directory API 中的云记录，以便在 Cloud Directory API 中进行查询。如果当前用户没有关联的商家，则返回空字符串。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAnnotatedLocation(): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceAssetId(): Promise<string>
```

Example 3 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceHostname(): Promise<string>
```

Example 4 (unknown):
```unknown
chrome.enterprise.deviceAttributes.getDeviceSerialNumber(): Promise<string>
```

---

## chrome.search 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/search

**Contents:**
- chrome.search 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - Disposition
    - 枚举
  - QueryInfo
    - 属性
- 方法

使用 chrome.search API 通过默认提供程序进行搜索。

“CURRENT_TAB” 指定搜索结果显示在调用标签页或活动浏览器中的标签页中。

“NEW_TAB” 指定搜索结果显示在新标签页中。

“NEW_WINDOW” 指定搜索结果显示在新窗口中。

应显示搜索结果的位置。默认为 CURRENT_TAB。

应显示搜索结果的位置。tabId 无法与 disposition 搭配使用。

用于查询默认搜索服务提供商。如果出现错误，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
chrome.search.query(  queryInfo: QueryInfo,): Promise<void>
```

---

## chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/bookmarks?hl=zh-cn

**Contents:**
- chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 对象和属性
  - 示例
- 类型
  - BookmarkTreeNode
    - 属性
  - BookmarkTreeNodeUnmodifiable

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

您必须在扩展程序清单中声明“书签”权限，才能使用书签 API。 例如：

书签以树状结构整理，树中的每个节点要么是书签，要么是文件夹（有时称为“组”）。树中的每个节点都由一个 bookmarks.BookmarkTreeNode 对象表示。

BookmarkTreeNode 属性在整个 chrome.bookmarks API 中使用。例如，当您调用 bookmarks.create 时，您会传入新节点的父节点 (parentId)，还可以选择性地传入节点的 index、title 和 url 属性。如需了解节点可以拥有的属性，请参阅 bookmarks.BookmarkTreeNode。

以下代码创建了一个标题为“扩展程序书签”的文件夹。create() 的第一个实参用于指定新文件夹的属性。第二个实参定义了在创建文件夹后要执行的函数。

以下代码段创建了一个指向扩展程序开发者文档的书签。由于创建书签失败不会造成任何不良后果，因此此代码无需定义回调函数。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 Bookmarks API 示例。

书签树中的节点（书签或文件夹）。子节点在其父文件夹中按顺序排列。

BookmarkTreeNode[] 可选

相应节点创建的时间，以自纪元 (new Date(dateAdded)) 以来的毫秒数表示。

相应文件夹的内容上次更改的时间（以自纪元以来经过的毫秒数表示）。

相应节点上次打开的时间（以自纪元以来经过的毫秒数表示）。未针对文件夹设置。

如果存在，则表示浏览器添加的文件夹，用户或扩展程序无法修改。如果此节点未设置 unmodifiable 属性，则可以修改子节点。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

每种文件夹类型的节点数量可能为零、一个或多个。浏览器可能会添加或移除文件夹，但无法通过扩展程序 API 执行此操作。

节点的唯一标识符。ID 在当前个人资料中是唯一的，即使在浏览器重启后仍保持有效。

相应节点是否已由浏览器与用户的远程账号存储空间同步。这可用于区分同一 FolderType 的账号级版本和仅限本地版本。现有节点上此属性的值可能会发生变化，例如，因用户操作而发生变化。

注意：此属性反映了节点是否已保存到浏览器的内置账号提供程序。即使此值为 false，节点也可能通过第三方进行同步。

对于受管节点（unmodifiable 设置为 true 的节点），此属性将始终为 false。

指明相应节点不可修改的原因。managed 值表示相应节点是由系统管理员或受监督用户的监护人配置的。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

用户点击书签时导航到的网址。对于文件夹，此属性会被省略。

指明相应节点不可修改的原因。值 managed 表示相应节点由系统管理员配置。如果节点可由用户和扩展程序修改，则省略此属性（默认）。

“bookmarks-bar” 内容显示在浏览器窗口顶部的文件夹。

“其他” 在所有平台的完整书签列表中显示的书签。

“移动设备” 用户移动设备上通常可用的书签，但可通过扩展程序或在书签管理器中修改。

“受管理” 如果受监督用户的系统管理员或监护人已配置书签，则可能会显示此顶级文件夹。

在指定的 parentId 下创建书签或文件夹。如果网址为 NULL 或缺失，则为文件夹。

Promise<BookmarkTreeNode>

检索指定的 BookmarkTreeNode。

字符串 | [字符串, ...字符串 []]

单个字符串值 ID 或字符串值 ID 数组

Promise<BookmarkTreeNode[]>

检索指定 BookmarkTreeNode ID 的子级。

Promise<BookmarkTreeNode[]>

Promise<BookmarkTreeNode[]>

检索书签层次结构的一部分，从指定节点开始。

Promise<BookmarkTreeNode[]>

Promise<BookmarkTreeNode[]>

将指定的 BookmarkTreeNode 移动到提供的位置。

Promise<BookmarkTreeNode>

搜索与给定查询匹配的 BookmarkTreeNodes。使用对象指定的查询会生成与所有指定属性匹配的 BookmarkTreeNodes。

一个字符串（包含与书签网址和标题匹配的字词和带引号的短语）或一个对象。如果为对象，则可以指定属性 query、url 和 title，系统将生成与所有指定属性匹配的书签。

一个字符串，包含要与书签网址和标题进行匹配的字词和带引号的短语。

书签的网址；完全匹配。请注意，文件夹没有网址。

Promise<BookmarkTreeNode[]>

更新书签或文件夹的属性。仅指定要更改的属性；未指定的属性将保持不变。注意：目前仅支持“title”和“url”。

Promise<BookmarkTreeNode>

在书签或文件夹发生更改时触发。注意：目前，只有标题和网址更改会触发此操作。

当文件夹的子项因在界面中排序而更改顺序时触发。不会因调用 move() 而调用。

在开始书签导入会话时触发。在 onImportEnded 触发之前，开销大的观测器应忽略 onCreated 更新。观察者仍应立即处理其他通知。

当书签或文件夹被移至其他父级文件夹时触发。

在移除书签或文件夹时触发。以递归方式移除文件夹时，系统会针对该文件夹触发一次通知，而不会针对其内容触发通知。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "bookmarks"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.bookmarks.create(
  {'parentId': bookmarkBar.id, 'title': 'Extension bookmarks'},
  function(newFolder) {
    console.log("added folder: " + newFolder.title);
  },
);
```

Example 3 (unknown):
```unknown
chrome.bookmarks.create({
  'parentId': extensionsFolderId,
  'title': 'Extensions doc',
  'url': 'https://developer.chrome.com/docs/extensions',
});
```

Example 4 (unknown):
```unknown
chrome.bookmarks.create(  bookmark: CreateDetails,): Promise<BookmarkTreeNode>
```

---

## chrome.proxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/proxy

**Contents:**
- chrome.proxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 代理模式
  - 代理规则
  - 代理服务器对象
  - 绕过列表
- 示例
- 类型

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖 ChromeSetting 类型 API 原型来获取和设置代理配置。

您必须声明“代理”权限，以使用代理设置 API。例如：

代理设置在 proxy.ProxyConfig 对象中定义。根据 Chrome 的代理设置， 这些设置可能包含 proxy.ProxyRules 或 proxy.PacScript。

ProxyConfig 对象的 mode 属性决定了 Chrome 的整体行为 代理用量。它可以采用以下值：

proxy.ProxyRules 对象可以包含 singleProxy 属性或 proxyForHttp、proxyForHttps、proxyForFtp 和 fallbackProxy。

在第一种情况下，系统会通过指定的代理服务器代理 HTTP、HTTPS 和 FTP 流量。其他 直接发送流量对于后一种情况，其行为略微巧妙：如果代理服务器 针对 HTTP、HTTPS 或 FTP 协议进行了配置，则相应流量将通过 指定服务器如果未指定此类代理服务器或流量使用的协议 HTTP、HTTPS 或 FTP，使用 fallbackProxy。如果未指定 fallbackProxy，则系统会发送流量 而无需代理服务器。

代理服务器是在 proxy.ProxyServer 对象中配置的。与代理服务器的连接 （由 host 属性定义）使用 scheme 属性定义的协议。如果拒绝 已指定 scheme，则代理连接默认为 http。

如果 proxy.ProxyServer 对象中未定义 port，则系统会从架构派生端口。 默认端口为：

可以使用 bypassList 来排除各个服务器。此列表可能包含 以下条目：

匹配与 HOST_PATTERN 格式匹配的所有主机名。前导 "." 会被解释为 "*."。

示例："foobar.com", "*foobar.com", "*.foobar.com", "*foobar.com:99", "https://x.*.y.com:99"。

匹配作为 IP 地址字面量的网址。从概念上讲，这与第一种情况类似， 特殊情况来处理 IP 字面量规范化。例如，匹配“[0:0:0::1]” 与匹配“[::1]”相同因为 IPv6 规范化是在内部完成的

示例：127.0.1、[0:0::1]、[::1]:80、https://[::1]:443

匹配给定参数中任何包含 IP 字面量 (IP_LITERAL) 的网址 范围。IP 范围 (PREFIX_LENGTH_IN_BITS) 使用 CIDR 指定 表示法。

匹配给定范围内包含 IP 字面量的任何网址。IP 范围是使用 CIDR 指定的 标记。 示例："192.168.1.1/16", "fefe:13::abc/33"

字面量字符串 <local> 与简单的主机名匹配。简单的主机名是不包含 而不是 IP 字面量。例如，example 和 localhost 是简单的主机名， 而 example.com、example. 和 [::1] 则不行。

以下代码设置了 SOCKS 5 代理，用于与 foobar.com 以外的所有服务器的 HTTP 连接，并使用 直接连接（适用于所有其他协议）。这些设置会应用于常规窗口和无痕式窗口， 无痕式窗口会沿用常规窗口的设置。另请参阅 Types API 文档。

下一个代码段会查询当前的有效代理设置。有效的代理设置可以是 由其他扩展程序或政策决定。如需了解详情，请参阅 Types API 文档。

请注意，传递到 set() 的 value 对象与传递到 的 value 对象不同 回调函数 get()。后者将包含 rules.proxyForHttp.port 元素。

包含代理自动配置信息的对象。必须有一个字段为非空字段。

如果为 true，无效的 PAC 脚本将阻止网络堆栈回退到直接连接。默认值为 false。

“direct”= 从不使用代理 “auto_detect”= 自动检测代理设置 “pac_script”= 使用指定的 PAC 脚本 “fixed_servers”= 手动指定代理服务器 “system”= 使用系统代理设置

此配置的代理自动配置 (PAC) 脚本。将此用于“pac_script”模式。

描述此配置的代理规则。将此用于“fixed_servers”模式。

用于封装所有协议的一组代理规则的对象。使用“singleProxy”或“proxyForHttp”“proxyForHttps”“proxyForFtp”的子集和“fallbackProxy”

要在没有代理服务器的情况下连接的服务器列表。

用于其他任何用途或未指定任何特定 agentFor... 的代理服务器。

要用于所有 Per-网址 请求（即 http、https 和 ftp）的代理服务器。

代理服务器的主机名或 IP 地址。主机名必须采用 ASCII（Punycode 格式）。目前尚不支持 IDNA。

代理服务器的端口。默认为取决于 scheme 的端口。

代理服务器本身的架构（协议）。默认值为“http”。

要使用的代理设置。此设置的值为 ProxyConfig 对象。

types.ChromeSetting&lt;ProxyConfig&gt;

有关错误的其他详细信息，例如 JavaScript 运行时错误。

如果为 true，则错误为严重，网络事务已中止。否则，系统会改用直接连接。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "proxy"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var config = {
  mode: "fixed_servers",
  rules: {
    proxyForHttp: {
      scheme: "socks5",
      host: "1.2.3.4"
    },
    bypassList: ["foobar.com"]
  }
};
chrome.proxy.settings.set(
  {value: config, scope: 'regular'},
  function() {}
);
```

Example 3 (unknown):
```unknown
var config = {
  mode: "pac_script",
  pacScript: {
    data: "function FindProxyForURL(url, host) {\n" +
          "  if (host == 'foobar.com')\n" +
          "    return 'PROXY blackhole:80';\n" +
          "  return 'DIRECT';\n" +
          "}"
  }
};
chrome.proxy.settings.set(
  {value: config, scope: 'regular'},
  function() {}
);
```

Example 4 (unknown):
```unknown
chrome.proxy.settings.get(
  {'incognito': false},
  function(config) {
    console.log(JSON.stringify(config));
  }
);
```

---

## chrome.vpnProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/vpnProvider?hl=zh-cn

**Contents:**
- chrome.vpnProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Parameters
    - 属性
  - PlatformMessage
    - 枚举

使用 chrome.vpnProvider API 实现 VPN 客户端。

chrome.vpnProvider 的典型用法如下：

通过调用 createConfig() 创建 VPN 配置。VPN 配置是指在 ChromeOS 界面中向用户显示的持久性条目。用户可以从列表中选择 VPN 配置，并连接或断开连接。

为 onPlatformMessage、onPacketReceived 和 onConfigRemoved 事件添加监听器。

当用户连接到 VPN 配置时，系统会收到 onPlatformMessage，并显示消息 "connected"。"connected" 消息和 "disconnected" 消息之间的时段称为“VPN 会话”。在此时间段内，接收消息的扩展程序被视为拥有 VPN 会话。

启动与 VPN 服务器的连接并启动 VPN 客户端。

通过调用 setParameters() 设置连接的参数。

通过调用 notifyConnectionStateChanged() 将连接状态通知为 "connected"。

如果上述步骤顺利完成，系统会为 ChromeOS 的网络堆栈创建一个虚拟隧道。通过调用 sendPacket()，IP 数据包可以通过隧道发送；ChromeOS 设备上发出的任何数据包都将通过 onPacketReceived 事件处理程序接收。

当用户断开与 VPN 配置的连接时，系统会触发 onPlatformMessage 并显示消息 "disconnected"。

如果不再需要 VPN 配置，可以通过调用 destroyConfig() 将其销毁。

VPN 接口的 IP 地址（采用 CIDR 表示法）。目前，唯一支持的模式是 IPv4。

VPN 接口的广播地址。（默认值：根据 IP 地址和掩码推断得出）

从隧道中排除以 CIDR 表示法表示的 IP 块列表的网络流量。这可用于绕过 VPN 服务器的传入和传出流量。如果多条规则与某个目的地匹配，则匹配前缀最长的规则胜出。对应于同一 CIDR 块的条目会被视为重复条目。系统会消除汇总列表（exclusionList + inclusionList）中的此类重复项，但具体消除哪个完全相同的重复条目是不确定的。

将网络流量（采用 CIDR 表示法）添加到隧道 IP 块列表中。此参数可用于设置拆分隧道。默认情况下，没有流量会定向到隧道。将条目“0.0.0.0/0”添加到此列表后，所有用户流量都会重定向到隧道。如果多条规则与某个目的地匹配，则匹配前缀最长的规则胜出。对应于同一 CIDR 块的条目会被视为重复条目。系统会消除汇总列表（exclusionList + inclusionList）中的此类重复项，但具体消除哪个完全相同的重复条目是不确定的。

VPN 接口的 MTU 设置。（默认值：1500 字节）

如果为 true，则 linkDown、linkUp、linkChanged、suspend 和 resume 平台消息将用于发出相应事件的信号。如果为 false，当网络拓扑发生变化时，系统会强制断开 VPN 连接，用户需要手动重新连接。（默认值：false）

此属性是 Chrome 51 中的新属性；在更早的版本中，它会生成异常。try/catch 可用于根据浏览器支持情况有条件地启用该功能。

平台使用此枚举来通知客户端 VPN 会话状态。

“已断开连接” 表示 VPN 配置已断开连接。

“error” 表示 VPN 连接中发生了错误，例如超时。错误说明作为 onPlatformMessage 的 error 实参提供。

“linkDown” 表示默认物理网络连接已断开。

“linkUp” 表示默认的物理网络连接已恢复。

“linkChanged” 表示默认的物理网络连接已更改，例如从 WLAN 更改为移动网络。

“暂停” 表示操作系统正在准备暂停，因此 VPN 应断开连接。无法保证扩展程序在暂停之前收到此事件。

“resume” 表示操作系统已恢复，用户已重新登录，因此 VPN 应尝试重新连接。

平台使用此枚举来指明触发 onUIEvent 的事件。

“showAddDialog” 请求 VPN 客户端向用户显示添加配置对话框。

“showConfigureDialog” 请求 VPN 客户端向用户显示配置设置对话框。

VPN 客户端使用此枚举向平台告知其当前状态。这有助于向用户提供有意义的消息。

创建新的 VPN 配置，该配置在用户的多个登录会话中保持不变。

向平台通知 VPN 会话状态。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

通过为 VPN 会话创建的隧道发送 IP 数据包。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

设置 VPN 会话的参数。应在从平台收到 "connected" 后立即调用此方法。只有当 VPN 会话归扩展程序所有时，此方法才会成功。

当通过隧道接收到扩展程序所拥有的 VPN 会话的 IP 数据包时触发。

当从平台收到扩展程序所拥有的 VPN 配置的消息时触发。

当扩展程序发生界面事件时触发。界面事件是来自平台的信号，用于向应用表明需要向用户显示界面对话框。

**Examples:**

Example 1 (unknown):
```unknown
chrome.vpnProvider.createConfig(  name: string,): Promise<string>
```

Example 2 (unknown):
```unknown
chrome.vpnProvider.destroyConfig(  id: string,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.vpnProvider.notifyConnectionStateChanged(  state: VpnConnectionState,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.vpnProvider.sendPacket(  data: ArrayBuffer,): Promise<void>
```

---

## chrome.accessibilityFeatures 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/accessibilityFeatures

**Contents:**
- chrome.accessibilityFeatures 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 属性
  - animationPolicy
    - 类型
  - autoclick
    - 类型
  - caretHighlight
    - 类型

请使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 ChromeSetting 类型 API 原型来获取和设置各项无障碍功能。如需获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，该扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不隐含 accessibilityFeatures.read 权限。

get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<"allowed" | "once" | "none" >

鼠标停止移动后自动点击鼠标。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标颜色。该值用于指明功能是否已启用，并不表示其颜色。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

光标突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

语音输入。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

固定放大镜。该值用于指明是否已启用停靠的放大镜功能。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

焦点突出显示。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

高对比度渲染模式。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

已放大的光标。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

全屏放大。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

随选朗读。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

语音反馈（文字转语音）。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

固定辅助键（例如 shift 或 alt）。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

“开关控制”。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

虚拟屏幕键盘。该值用于指明相应功能是否已启用。get() 需要 accessibilityFeatures.read 权限。set() 和 clear() 需要 accessibilityFeatures.modify 权限。

types.ChromeSetting<boolean>

---

## chrome.system.memory 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/memory

**Contents:**
- chrome.system.memory 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - MemoryInfo
    - 属性
- 方法
  - getInfo()
    - 返回

chrome.system.memory API。

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.memory.getInfo(): Promise<MemoryInfo>
```

---

## chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/extensionTypes

**Contents:**
- chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 类型
  - ColorArray
    - 类型
  - CSSOrigin
    - 枚举
  - DeleteInjectionDetails
    - 属性
  - DocumentLifecycle

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

[number, number, number, number]

要移除的 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示应从当前页面的所有框架中移除 CSS。默认值为 false，并且仅从顶部框架中移除。如果设置了 true 和 frameId，则从所选帧及其所有子帧中移除代码。

要移除的 CSS 的来源。默认设置为 "author"。

应从中移除 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问其父文档时，该代码也会从 about:blank 和 about:srcdoc 框架中移除。默认值为 false。

脚本要在其中执行的 JavaScript 世界。可以是此扩展程序独有的隔离世界、与网页的 JavaScript 共享的 DOM 主世界，也可以是仅适用于通过 User Scripts API 注册的脚本的用户脚本世界。

图片的像素数据。必须是 ImageData 对象；例如，来自 canvas 元素。

当格式为 "jpeg" 时，控制生成图片的质量。对于 PNG 图片，系统会忽略此值。随着质量的降低，生成的图片会出现更多视觉伪影，并且存储所需的字节数也会减少。

要注入的脚本或 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示 JavaScript 或 CSS 应注入到当前页面的所有框架中。默认值为 false，并且仅注入到顶部框架中。如果设置了 true 和 frameId，则代码会插入到所选帧及其所有子帧中。

要注入的 JavaScript 或 CSS 代码。

警告：请谨慎使用 code 参数。如果使用不当，可能会导致您的扩展程序遭受跨站脚本攻击

要注入的 CSS 的来源。此值只能为 CSS 指定，不能为 JavaScript 指定。默认设置为 "author"。

要注入的 JavaScript 或 CSS 文件。

应注入脚本或 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问 about:blank 和 about:srcdoc 框架的父文档时，代码也会注入到这些框架中。代码无法插入到顶级 about:-frames 中。默认值为 false。

JavaScript 或 CSS 将注入到标签页中的最早时间。默认值为“document_idle”。

JavaScript 或 CSS 将注入到标签页中的最早时间。

“document_start” 脚本在任何 CSS 文件之后注入，但在构建任何其他 DOM 或运行任何其他脚本之前注入。

“document_end” 在 DOM 完成后立即注入脚本，但在图片和框架等子资源加载之前注入。

“document_idle” 浏览器会选择一个时间在“document_end”和 window.onload 事件触发后立即注入脚本。注入的确切时间取决于文档的复杂程度和加载所需的时间，并针对网页加载速度进行了优化。以“document_idle”运行的内容脚本无需监听 window.onload 事件；它们保证在 DOM 完成后运行。如果脚本确实需要在 window.onload 之后运行，扩展程序可以使用 document.readyState 属性检查 onload 是否已触发。

---

## chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/platformKeys

**Contents:**
- chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
- 类型
  - Algorithm
    - 枚举
  - ChallengeKeyOptions
    - 属性

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

使用此 API 注册客户端证书的典型步骤如下：

使用 enterprise.platformKeys.getTokens() 获取所有可用令牌。

查找 id 等于 "user" 的令牌。随后使用此令牌。

使用 generateKey() Token 方法（在 SubtleCrypto 中定义）生成密钥对。这将返回密钥的句柄。

使用 exportKey() 令牌方法（在 SubtleCrypto 中定义）导出公钥。

使用 sign() Token 方法（在 SubtleCrypto 中定义）创建认证请求数据的签名。

如果收到证书，请使用 [enterprise.platformKeys.importCertificate()`[3]

以下示例展示了除构建和发送认证请求之外的主要 API 互动：

由 Verified Access Web API 发出的质询。

RegisterKeyOptions 可选

如果存在，则使用指定的 scope 的令牌注册受质询的密钥。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。随后对该函数的调用将在指定的 scope 中生成新的企业密钥。

静态 ID 为 "user" 和 "system"，分别是指平台的用户专用硬件令牌和系统范围的硬件令牌。任何其他令牌（带有其他标识符）都可能由 enterprise.platformKeys.getTokens 返回。

实现 WebCrypto 的 SubtleCrypto 接口。加密操作（包括密钥生成）由软件支持。密钥的保护以及不可提取属性的实现是在软件中完成的，因此密钥的保护程度不如硬件支持的密钥。

只能生成不可提取的密钥。支持的密钥类型为 RSASSA-PKCS1-V1_5 和 RSA-OAEP（在 Chrome 版本 135 及更高版本中），密钥长度为 modulusLength，最高可达 2048。每个 RSASSA-PKCS1-V1_5 密钥最多只能用于一次数据签名，除非通过 KeyPermissions 政策将相应扩展程序列入许可名单，在这种情况下，该密钥可以无限期使用。自 Chrome 版本 135 起，RSA-OAEP 密钥受到支持，并且通过同一政策列入许可名单的扩展程序可以使用这些密钥来解封装其他密钥。

在特定 Token 上生成的密钥不能用于任何其他令牌，也不能用于 window.crypto.subtle。同样，使用 window.crypto.subtle 创建的 Key 对象不能与此接口搭配使用。

实现 WebCrypto 的 SubtleCrypto 接口。加密操作（包括密钥生成）由硬件支持。

只能生成不可提取的密钥。支持的密钥类型包括 RSASSA-PKCS1-V1_5 和 RSA-OAEP（在 Chrome 版本 135 及更高版本中）以及 modulusLength 最多 2048 位的 ECDSA 和 namedCurve P-256。每个 RSASSA-PKCS1-V1_5 和 ECDSA 密钥最多只能用于一次数据签名，除非通过 KeyPermissions 政策将相应扩展程序列入许可名单，在这种情况下，密钥可以无限期使用。自 Chrome 版本 135 起，RSA-OAEP 密钥受到支持，并且通过同一政策列入许可名单的扩展程序可以使用这些密钥来解封装其他密钥。

在特定 Token 上生成的密钥不能用于任何其他令牌，也不能用于 window.crypto.subtle。同样，使用 window.crypto.subtle 创建的 Key 对象不能与此接口搭配使用。

与 challengeMachineKey 和 challengeUserKey 类似，但允许指定已注册密钥的算法。对由硬件支持的企业机器密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。

如果 Verified Access Web API 成功完成验证，则表明当前设备是合法的 ChromeOS 设备，当前设备受验证期间指定的网域管理，当前登录的用户受验证期间指定的网域管理，并且当前设备状态符合企业设备政策。例如，某项政策可能规定设备不得处于开发者模式。验证所发出的任何设备身份都与当前设备的硬件紧密绑定。如果指定了 "user" 范围，则身份也会与当前登录的用户紧密绑定。

此函数受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业设备政策未明确为调用方启用此操作，则此函数将失败。受质询的密钥不位于 "system" 或 "user" 令牌中，并且无法通过任何其他 API 进行访问。

包含 ChallengeKeyOptions 中定义的字段的对象。

对由硬件支持的企业机器密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业设备政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证功能发出的任何设备身份都与当前设备的硬件紧密绑定。此函数受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业设备政策未明确为调用方启用此操作，则此函数将失败。企业机器密钥不位于 "system" 令牌中，并且无法通过任何其他 API 进行访问。

由 Verified Access Web API 发出的质询。

如果已设置，则当前企业机器密钥会注册为 "system" 令牌，并放弃企业机器密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业机器密钥。

对硬件支持的企业用户密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业用户政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证所发出的公钥与当前设备的硬件和当前登录用户紧密绑定。此功能受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业用户政策未明确为调用方启用此操作，则此功能将失败。企业用户密钥不位于 "user" 令牌中，任何其他 API 都无法访问该密钥。

由 Verified Access Web API 发出的质询。

如果设置，则当前企业用户密钥会注册到 "user" 令牌，并放弃企业用户密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业用户密钥。

返回指定令牌中的所有可用客户端证书的列表。可用于检查可用于特定身份验证的客户端证书是否存在以及是否过期。

Promise<ArrayBuffer[]>

返回可用令牌。在常规用户的会话中，该列表将始终包含用户的令牌，且该令牌具有 id "user"。如果存在系统级 TPM token，则返回的列表还将包含具有 id "system" 的系统级 token。对于相应设备（例如 Chromebook）上的所有会话，系统级令牌都将相同。

如果认证密钥已存储在相应令牌中，则将 certificate 导入到相应令牌。成功发出认证请求后，应使用此函数存储获得的证书，并使其可供操作系统和浏览器用于身份验证。

从给定令牌中移除 certificate（如果存在）。应使用此方法移除过时的证书，以免在身份验证期间考虑这些证书，并避免证书选择过程过于杂乱。应使用此方法释放证书存储区中的存储空间。

**Examples:**

Example 1 (unknown):
```unknown
function getUserToken(callback) {
  chrome.enterprise.platformKeys.getTokens(function(tokens) {
    for (var i = 0; i < tokens.length; i++) {
      if (tokens[i].id == "user") {
        callback(tokens[i]);
        return;
      }
    }
    callback(undefined);
  });
}

function generateAndSign(userToken) {
  var data = new Uint8Array([0, 5, 1, 2, 3, 4, 5, 6]);
  var algorithm = {
    name: "RSASSA-PKCS1-v1_5",
    // RsaHashedKeyGenParams
    modulusLength: 2048,
    publicExponent:
        new Uint8Array([0x01, 0x00, 0x01]),  // Equivalent to 65537
    hash: {
      name: "SHA-256",
    }
  };
  var cachedKeyPair;
  userToken.subtleCrypto.generateKey(algorithm, false, ["sign"])
    .then(function(keyPair) {
            cachedKeyPair = keyPair;
            return userToken.subtleCrypto.exportKey("spki", keyPair.publicKey);
          },
          console.log.bind(console))
    .then(function(publicKeySpki) {
            // Build the Certification Request using the public key.
            return userToken.subtleCrypto.sign(
                {name : "RSASSA-PKCS1-v1_5"}, cachedKeyPair.privateKey, data);
          },
          console.log.bind(console))
    .then(function(signature) {
              // Complete the Certification Request with |signature|.
              // Send out the request to the CA, calling back
              // onClientCertificateReceived.
          },
          console.log.bind(console));
}

function onClientCertificateReceived(userToken, certificate) {
  chrome.enterprise.platformKeys.importCertificate(userToken.id, certificate);
}

getUserToken(generateAndSign);
```

Example 2 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeKey(  options: ChallengeKeyOptions,): Promise<ArrayBuffer>
```

Example 3 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeMachineKey(  challenge: ArrayBuffer,  registerKey?: boolean,): Promise<ArrayBuffer>
```

Example 4 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeUserKey(  challenge: ArrayBuffer,  registerKey: boolean,): Promise<ArrayBuffer>
```

---

## chrome.enterprise.hardwarePlatform 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/hardwarePlatform?hl=zh-cn

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
    - 返回

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

获取硬件平台的制造商和型号，并在扩展程序获得授权后通过 callback 返回。

Promise<HardwarePlatformInfo>

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.hardwarePlatform.getHardwarePlatformInfo(): Promise<HardwarePlatformInfo>
```

---

## chrome.i18n 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/i18n

**Contents:**
- chrome.i18n 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概念和用法
  - 支持多种语言
  - 预定义的消息
  - 语言区域
  - 搜索邮件
  - 设置浏览器的语言区域
    - Windows

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

如果扩展程序具有 /_locales 目录，则清单必须定义 "default_locale"。

您需要将其所有面向用户的字符串都放入名为 messages.json 的文件中。每次添加新的语言区域时，您都会在名为 /_locales/_localeCode_ 的目录下添加一个消息文件，其中 localeCode 是一个代码，例如 en 表示英语。

以下是支持英语 (en)、西班牙语 (es) 和韩语 (ko) 的国际化扩展程序的文件夹层次结构：

假设您有一个扩展程序，其中包含下图所示的文件：

为了实现此扩展程序的国际化，您需要为每个面向用户的字符串命名，并将其放入消息文件中。扩展程序的清单、CSS 文件和 JavaScript 代码使用每个字符串的名称来获取其本地化版本。

以下是国际化后的扩展程序（请注意，它仍然只有英文字符串）：

在 manifest.json 和 CSS 文件中，按如下方式引用名为 messagename 的字符串：

在扩展程序或应用的 JavaScript 代码中，按如下方式引用名为 messagename 的字符串：

在每次对 getMessage() 的调用中，您最多可以提供 9 个要包含在消息中的字符串。如需了解详情，请参阅 示例：getMessage。

某些消息（例如 @@bidi_dir 和 @@ui_locale）由国际化系统提供。如需查看预定义消息名称的完整列表，请参阅预定义消息部分。

在 messages.json 中，每个面向用户的字符串都有一个名称、一个“message”项和一个可选的“description”项。该名称是一个键，例如“extName”或“search_string”，用于标识字符串。“message”指定相应语言区域中字符串的值。可选的“说明”可为翻译人员提供帮助，因为他们可能无法了解字符串在扩展程序中的使用方式。例如：

如需了解详情，请参阅格式：特定于语言区域的消息。

扩展程序国际化后，翻译起来非常简单。您复制 messages.json，对其进行翻译，然后将副本放入 /_locales 下的新目录中。例如，如需支持西班牙语，只需将 messages.json 的翻译副本放在 /_locales/es 下即可。下图显示了之前添加了新的西班牙语翻译的扩展程序。

国际化系统提供了一些预定义的消息，可帮助您进行本地化。这些资源包括 @@ui_locale，因此您可以检测当前界面语言区域，以及一些 @@bidi_... 消息，让您可以检测文字方向。后一种消息的名称与 gadgets BIDI（双向）API 中的常量类似。

无论扩展程序或应用是否已本地化，都可以在 CSS 和 JavaScript 文件中使用特殊消息 @@extension_id。此消息不适用于清单文件。

以下示例展示了如何在 CSS 文件中使用 @@extension_id 构建网址：

如果扩展程序 ID 为 abcdefghijklmnopqrstuvwxyzabcdef，则上一个代码段中的粗体行将变为：

以下示例展示了如何在 CSS 文件中使用 @@bidi_* 消息：

对于从左到右书写的语言（例如英语），粗体行变为：

您可以从多种语言区域中进行选择，包括一些（例如 en）允许单个翻译支持多种语言变体（例如 en_GB 和 en_US）。

您可以将扩展程序本地化为 Chrome 应用商店支持的任何语言区域。如果此处未列出您的语言区域，请选择最接近的替代选项。例如，如果扩展程序的默认语言区域设置是 "de_CH"，请在 Chrome 应用商店中选择 "de"。

您不必为每个受支持的语言区域都定义每个字符串。只要默认语言区域的 messages.json 文件中包含每个字符串的值，无论翻译有多稀疏，扩展程序或应用都会运行。扩展程序系统会按以下方式搜索消息：

在下图中，名为“colores”的消息位于扩展程序支持的所有三种语言区域中，但“extName”仅位于两种语言区域中。在美国境内使用英语版 Google Chrome 的用户看到的是“Colors”标签，而使用英式英语的用户看到的是“Colours”。美国英语用户和英国英语用户都会看到扩展程序名称“Hello World”。由于默认语言为西班牙语，因此以任何非英语语言运行 Google Chrome 的用户都会看到“Colores”标签和“Hola mundo”扩展程序名称。

如需测试翻译，您可能需要设置浏览器的语言区域。本部分介绍了如何在 Windows、Mac OS、Linux 和 ChromeOS 中设置语言区域。

您可以使用特定于语言区域的快捷方式或 Google Chrome 界面来更改语言区域。快捷方式方法在设置完毕后速度更快，并且可让您同时使用多种语言。

如需创建和使用可启动 Google Chrome 并指定特定语言区域的快捷方式，请执行以下操作：

更改快捷方式的属性，使“目标”字段指定 --lang 和 --user-data-dir 标志。目标应如下所示：

双击快捷方式启动 Google Chrome。

例如，如需创建以西班牙语 (es) 启动 Google Chrome 的快捷方式，您可以创建一个名为 chrome-es 的快捷方式，其目标如下：

您可以根据需要创建任意数量的快捷方式，以便轻松进行多语言测试。例如：

以下是在 Google Chrome（Windows 版）上使用界面更改语言区域的方法：

如需在 Mac 上更改语言区域，请使用系统偏好设置。

如需在 Linux 上更改语言区域，请先退出 Google Chrome。然后，在一行中设置 LANGUAGE 环境变量并启动 Google Chrome。例如：

如需在 ChromeOS 上更改语言区域，请执行以下操作：

您可以在 examples/api/i18n 目录中找到国际化示例。如需查看完整示例，请参阅 examples/extensions/news。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

以下代码从浏览器获取本地化消息，并将其显示为字符串。它会将消息中的两个占位符替换为字符串“string1”和“string2”。

如需详细了解占位符，请参阅特定于语言区域的消息页面。如需详细了解如何调用 getMessage()，请参阅 API 参考文档。

以下代码从浏览器获取 accept-languages，并通过用“,”分隔每个 accept-language 将它们显示为字符串。

如需详细了解如何调用 getAcceptLanguages()，请参阅 API 参考文档。

以下代码可从给定的字符串中检测最多 3 种语言，并以换行符分隔的字符串形式显示结果。

如需详细了解如何调用 detectLanguage(inputText)，请参阅 API 参考文档。

ISO 语言代码，例如 en 或 fr。如需查看此方法支持的语言的完整列表，请参阅 kLanguageInfoTable。对于未知语言，系统将返回 und，这意味着 CLD 无法识别 [百分比] 的文本

获取浏览器的 accept-languages。这与浏览器使用的语言区域不同；如需获取语言区域，请使用 i18n.getUILanguage。

Promise<LanguageCode[]>

获取指定消息的本地化字符串。如果缺少消息，此方法会返回空字符串 ('')。如果 getMessage() 调用的格式有误（例如，messageName 不是字符串，或者 substitutions 数组的元素超过 9 个），此方法会返回 undefined。

消息的名称，如 messages.json 文件中所指定。

在翻译为 &lt; 时，转义 <。这仅适用于消息本身，而不适用于占位符。如果翻译内容用于 HTML 上下文中，开发者可能需要使用此方法。与 Closure 编译器搭配使用的 Closure 模板会自动生成此文件。

获取浏览器的浏览器界面语言。这与返回首选用户语言的 i18n.getAcceptLanguages 不同。

浏览器界面语言代码，例如 en-US 或 fr-FR。

**Examples:**

Example 1 (unknown):
```unknown
__MSG_messagename__
```

Example 2 (unknown):
```unknown
chrome.i18n.getMessage("messagename")
```

Example 3 (unknown):
```unknown
{
  "search_string": {
    "message": "hello%20world",
    "description": "The string we search for. Put %20 between words that go together."
  },
  ...
}
```

Example 4 (unknown):
```unknown
body {
  background-image:url('chrome-extension://__MSG_@@extension_id__/background.png');
}
```

---

## chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/panels?hl=zh-cn

**Contents:**
- chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 示例
- 类型
  - Button
    - 属性
  - ElementsPanel
    - 属性
  - ExtensionPanel

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

每个扩展程序面板和边栏都显示为单独的 HTML 页面。开发者工具窗口中显示的所有扩展程序页面都可以访问 chrome.devtools API 的所有部分以及所有其他扩展程序 API。

您可以使用 devtools.panels.setOpenResourceHandler 方法安装一个回调函数，该函数用于处理用户打开资源（通常是在开发者工具窗口中点击资源链接）的请求。最多只能调用一个已安装的处理程序；用户可以使用“开发者工具设置”对话框指定默认行为或扩展程序来处理资源打开请求。如果扩展程序多次调用 setOpenResourceHandler()，则仅保留最后一个处理程序。

如需大致了解如何使用开发者工具 API，请参阅开发者工具 API 摘要。

如需使用此 API，必须在清单中声明以下键。

以下代码添加了一个包含在 Panel.html 中的面板，该面板在开发者工具栏上以 FontPicker.png 表示，并标记为 Font Picker：

以下代码向“元素”面板添加了一个包含在 Sidebar.html 中且标题为字体属性的侧边栏窗格，然后将其高度设置为 8ex：

此屏幕截图展示了此示例对开发者工具窗口的影响：

如需试用此 API，请从 chrome-extension-samples 代码库中安装 devtools panels API 示例。

Event<functionvoidvoid>

onClicked.addListener 函数如下所示：

更新按钮的属性。如果省略了部分实参或将部分实参设为 null，则不会更新相应的属性。

当用户将鼠标悬停在按钮上时，以提示形式显示的文字。

Event<functionvoidvoid>

onSelectionChanged.addListener 函数如下所示：

createSidebarPane 函数如下所示：

已创建的侧边栏窗格的 ExtensionSidebarPane 对象。

Event<functionvoidvoid>

onHidden.addListener 函数如下所示：

Event<functionvoidvoid>

在发生搜索操作（开始新搜索、导航到搜索结果或取消搜索）时触发。

onSearch.addListener 函数如下所示：

Event<functionvoidvoid>

onShown.addListener 函数如下所示：

createStatusBarButton 函数如下所示：

按钮图标的路径。该文件应包含一张 64x24 像素的图片，该图片由两个 32x24 的图标组成。左侧图标用于按钮处于非活动状态时；右侧图标用于按钮处于按下状态时。

当用户将鼠标悬停在按钮上时，以提示形式显示的文字。

Event<functionvoidvoid>

当用户切换到托管侧边栏窗格的面板时，侧边栏窗格变为隐藏状态时触发。

onHidden.addListener 函数如下所示：

Event<functionvoidvoid>

当用户切换到托管侧边栏窗格的面板时，侧边栏窗格变为可见状态时触发。

onShown.addListener 函数如下所示：

设置在检查的网页中求值的表达式。结果会显示在侧边栏窗格中。

setExpression 函数如下所示：

要在检查的页面上下文中求值的表达式。JavaScript 对象和 DOM 节点会显示在可展开的树中，类似于控制台/监视。

类似 CSS 的尺寸规范，例如 '100px' 或 '12ex'。

设置要在边栏窗格中显示的 JSON 兼容对象。

要在检查的网页上下文中显示的对象。在调用方（API 客户端）的上下文中进行评估。

设置要在边栏窗格中显示的 HTML 网页。

Event<functionvoidvoid>

onSelectionChanged.addListener 函数如下所示：

createSidebarPane 函数如下所示：

已创建的侧边栏窗格的 ExtensionSidebarPane 对象。

“default” 默认的 DevTools 主题。始终为浅色主题。

用户在开发者工具设置中设置的颜色主题的名称。可能的值：default（默认）和 dark。

在开发者工具栏中扩展程序图标旁边显示的标题。

面板 HTML 页面相对于扩展程序目录的路径。

表示所创建面板的 ExtensionPanel 对象。

请求开发者工具在开发者工具面板中打开网址。

指定当用户点击开发者工具窗口中的资源链接时要调用的函数。如需取消设置处理程序，请调用不带参数的方法，或传递 null 作为参数。

所点击资源的 devtools.inspectedWindow.Resource 对象。

指定在开发者工具中当前主题发生更改时要调用的函数。如需取消设置处理程序，请调用不带参数的方法，或传递 null 作为参数。

**Examples:**

Example 1 (unknown):
```unknown
chrome.devtools.panels.create("Font Picker",
                              "FontPicker.png",
                              "Panel.html",
                              function(panel) { ... });
```

Example 2 (unknown):
```unknown
chrome.devtools.panels.elements.createSidebarPane("Font Properties",
  function(sidebar) {
    sidebar.setPage("Sidebar.html");
    sidebar.setHeight("8ex");
  }
);
```

Example 3 (javascript):
```javascript
(callback: function) => {...}
```

Example 4 (javascript):
```javascript
(iconPath?: string, tooltipText?: string, disabled?: boolean) => {...}
```

---

## chrome.webAuthenticationProxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/webAuthenticationProxy

**Contents:**
- chrome.webAuthenticationProxy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 类型
  - CreateRequest
    - 属性
  - CreateResponseDetails
    - 属性
  - DOMExceptionDetails

借助 chrome.webAuthenticationProxy API，在远程主机上运行的远程桌面软件可以拦截 Web 身份验证 API (WebAuthn) 请求，以便在本地客户端上处理这些请求。

传递给 navigator.credentials.create() 的 PublicKeyCredentialCreationOptions，序列化为 JSON 字符串。序列化格式与 PublicKeyCredential.parseCreationOptionsFromJSON() 兼容。

DOMExceptionDetails 可选

远程请求产生的 DOMException（如果有）。

CreateRequest 的 requestId。

远程请求生成的 PublicKeyCredential（如果有），通过调用 href="https://w3c.github.io/webauthn/#dom-publickeycredential-tojson"> PublicKeyCredential.toJSON() 序列化为 JSON 字符串。

传递给 navigator.credentials.get() 的 PublicKeyCredentialRequestOptions，序列化为 JSON 字符串。序列化格式与 PublicKeyCredential.parseRequestOptionsFromJSON() 兼容。

DOMExceptionDetails 可选

远程请求产生的 DOMException（如果有）。

CreateRequest 的 requestId。

远程请求生成的 PublicKeyCredential（如果有），通过调用 href="https://w3c.github.io/webauthn/#dom-publickeycredential-tojson"> PublicKeyCredential.toJSON() 序列化为 JSON 字符串。

使此扩展程序成为有效的 Web 身份验证 API 请求代理。

远程桌面扩展程序通常会在检测到远程会话附加到此主机后调用此方法。一旦此方法在未出错的情况下返回，系统就会暂停对 WebAuthn 请求的常规处理，并引发来自此扩展 API 的事件。

如果已附加其他扩展服务，此方法会因错误而失败。

附加的扩展程序必须在远程桌面会话结束后调用 detach()，以便恢复常规 WebAuthn 请求处理。如果扩展程序被卸载，则会自动变为分离状态。

请参阅 onRemoteSessionStateChange 事件，了解如何将远程会话附加从原生应用更改为（可能已暂停的）扩展程序。

Promise<string | undefined>

报告 navigator.credentials.create() 调用的结果。扩展程序必须针对收到的每个 onCreateRequest 事件调用此方法，除非请求已取消（在这种情况下，系统会触发 onRequestCanceled 事件）。

CreateResponseDetails

报告 navigator.credentials.get() 调用的结果。扩展程序必须针对收到的每个 onGetRequest 事件调用此方法，除非请求已取消（在这种情况下，系统会触发 onRequestCanceled 事件）。

报告 PublicKeyCredential.isUserVerifyingPlatformAuthenticator() 调用的结果。扩展程序必须针对收到的每个 onIsUvpaaRequest 事件调用此方法。

IsUvpaaResponseDetails

移除此扩展程序，使其不再作为有效的 Web 身份验证 API 请求代理。

当扩展程序检测到远程桌面会话已终止时，通常会调用此方法。此方法返回后，扩展程序将不再是有效的 Web 身份验证 API 请求代理。

请参阅 onRemoteSessionStateChange 事件，了解如何将远程会话附加从原生应用更改为（可能已暂停的）扩展程序。

Promise<string | undefined>

在发生 WebAuthn navigator.credentials.create() 调用时触发。扩展程序必须通过调用 completeCreateRequest() 并使用 requestInfo 中的 requestId 来提供响应。

在发生 WebAuthn navigator.credentials.get() 调用时触发。扩展程序必须通过调用 completeGetRequest() 并使用 requestInfo 中的 requestId 来提供响应

在发生 PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable() 调用时触发。扩展程序必须通过调用 completeIsUvpaaRequest() 并使用 requestInfo 中的 requestId 来提供响应

与此扩展程序关联的原生应用可以通过以下方式触发此事件：在默认用户数据目录内的名为 WebAuthenticationProxyRemoteSessionStateChange 的目录中写入名称等于扩展程序 ID 的文件

文件内容应为空。也就是说，无需更改文件内容即可触发此事件。

原生宿主应用可以使用此事件机制来指示可能发生的远程会话状态变化（即从分离到附加，或从附加到分离），而扩展程序服务工作线程可能处于暂停状态。在此事件的处理程序中，扩展程序可以相应地调用 attach() 或 detach() API 方法。

当 onCreateRequest 或 onGetRequest 事件被取消时（因为 WebAuthn 请求被调用方中止，或者因为超时）触发。当收到此事件时，扩展程序应取消在客户端上对相应请求的处理。扩展服务在请求取消后无法完成该请求。

**Examples:**

Example 1 (unknown):
```unknown
chrome.webAuthenticationProxy.attach(): Promise<string | undefined>
```

Example 2 (unknown):
```unknown
chrome.webAuthenticationProxy.completeCreateRequest(  details: CreateResponseDetails,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.webAuthenticationProxy.completeGetRequest(  details: GetResponseDetails,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.webAuthenticationProxy.completeIsUvpaaRequest(  details: IsUvpaaResponseDetails,): Promise<void>
```

---

## chrome.fileSystemProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fileSystemProvider

**Contents:**
- chrome.fileSystemProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概览
- 装载文件系统
- 配置文件系统
- 生命周期
- 类型
  - AbortRequestedOptions

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

您必须在扩展程序清单中声明“fileSystemProvider”权限和部分，才能使用文件系统提供程序 API。例如：

必须按如下方式声明 file_system_provider 部分：

“文件”应用会使用上述信息来正确呈现相关界面元素。例如，如果 configurable 设置为 true，系统将呈现用于配置音量的菜单项。同样，如果 multiple_mounts 设置为 true，则“文件”应用将允许通过界面添加多个装载点。如果 watchable 为 false，则系统会呈现刷新按钮。请注意，如果可能，您应添加对监听器的支持，以便文件系统上的更改可以立即自动反映出来。

文件系统提供程序 API 允许扩展程序支持虚拟文件系统，这些文件系统可在 ChromeOS 的文件管理器中使用。应用场景包括解压缩归档文件和访问云端硬盘以外的云服务中的文件。

提供扩展程序可以从外部来源（例如远程服务器或 USB 设备）提供文件系统内容，也可以使用本地文件（例如归档文件）作为其输入。

为了编写作为文件处理程序（来源为 "file"）的文件系统，提供程序必须是打包的应用，因为扩展程序无法使用 onLaunched 事件。

如果来源是网络或设备，则应在调用 onMountRequested 事件时装载文件系统。

提供的文件系统一旦装载，就可以通过 onConfigureRequested 事件进行配置。对于通过网络提供内容的文件系统，此方法尤其有用，可用于设置适当的凭据。您可以选择是否处理此事件。

Chrome 会记住已装载的文件系统，并在重启或重新启动后自动重新装载。因此，一旦文件系统被提供扩展程序装载，它就会一直存在，直到扩展程序被卸载或扩展程序调用 unmount 方法。

操作的标识符。对于常见操作，可以是任意字符串或 CommonActionId。

操作的标题。对于常见操作，可以忽略此属性。

观察是否应以递归方式包含所有子条目。只能针对目录设为 true。

与文件相关的信息（如果文件由云文件系统提供支持）。

云存储服务提供商的标识符（例如“drive.google.com”）。

常见操作列表。"SHARE" 用于与他人共享文件。"SAVE_FOR_OFFLINE"，用于固定（保存以供离线访问）。"OFFLINE_NOT_NECESSARY" 用于通知系统相应文件不再需要存储以供离线访问。由 onGetActionsRequested 和 onExecuteActionRequested 使用。

"OFFLINE_NOT_NECESSARY"

用于标识底层云文件系统中的特定文件的信息。如果 options 中请求了此参数，并且相应文件由 Cloud Storage 提供支持，则必须提供此参数。

相应条目的 Cloud Storage 表示形式。如果 options 中请求了此参数，并且相应文件由云存储提供支持，则必须提供此参数。对于没有云存储空间支持的本地文件，在请求时应为未定义。

如果它是目录，则为 True。如果 options 中有相应要求，则必须提供。

相应条目的 MIME 类型。始终为可选，但如果 options 中有要求，则应提供。

相应条目的上次修改时间。如果 options 中有相应要求，则必须提供。

相应条目的名称（非完整路径名称）。不得包含“/”。对于根，必须为空。如果 options 中有相应要求，则必须提供。

文件大小（以字节为单位）。如果 options 中有相应要求，则必须提供。

缩略图（采用 PNG、JPEG 或 WEBP 格式的数据 URI，大小不超过 32 KB）。可选，但只能在 onGetMetadataRequested 事件明确请求时提供。

一次可以打开的文件数上限。如果为 0，则表示不受限制。

文件系统是否支持用于观察目录的 tag 字段。

文件系统是否支持可能会更改文件系统内容的操作（例如创建、删除或写入文件）。

如果请求 cloudFileInfo 值，则设置为 true。

如果请求 cloudIdentifier 值，则设置为 true。

如果请求 is_directory 值，则设置为 true。

如果请求 mimeType 值，则设置为 true。

如果请求 modificationTime 值，则设置为 true。

如果请求 name 值，则设置为 true。

如果请求 size 值，则设置为 true。

如果请求 thumbnail 值，则设置为 true。

文件系统的字符串标识符。对于每个扩展程序来说都必须是唯一的。

一次可以打开的文件数上限。如果未指定或为 0，则表示不受限制。

框架是否应在下次登录会话时恢复文件系统。默认情况下为 true。

文件系统是否支持观测目录的 tag 字段。

文件系统是否支持可能会更改文件系统内容的操作（例如创建、删除或写入文件）。

观测到的条目发生的更改类型。如果为 DELETED，则系统会自动从观测到的条目列表中移除观测到的条目。

通知的标记。如果文件系统是使用 supportsNotifyTag 选项装载的，则此权限是必需的。请注意，此标志是必要的，可用于提供有关即使在系统关闭时也已更改的更改的通知。

供连续读取/写入和关闭请求使用的请求 ID。

打开文件的模式。由 onOpenFileRequested 使用。

将由后续读取/写入和关闭请求使用的请求 ID。

提供扩展程序时，在响应请求时以及在调用 API 方法时发生错误时使用的错误代码。若要成功，必须使用 "OK"。

如果请求 is_directory 值，则设置为 true。

如果请求 mimeType 值，则设置为 true。

如果请求 modificationTime 值，则设置为 true。

如果请求 name 值，则设置为 true。

如果请求 size 值，则设置为 true。

如果请求 thumbnail 值，则设置为 true。

观看是否应以递归方式包含所有子条目。只能针对目录设为 true。

返回有关具有所传递 fileSystemId 的文件系统的信息。

Promise<FileSystemInfo>

Promise<FileSystemInfo[]>

使用给定的 fileSystemId 和 displayName 装载文件系统。displayName 将显示在“文件”应用的左侧面板中。displayName 可以包含任何字符（包括“/”），但不能是空字符串。displayName 必须具有描述性，但不一定必须是唯一的。fileSystemId 不得为空字符串。

根据要装载的文件系统的类型，必须相应地设置 source 选项。

如果出现错误，系统会使用相应的错误代码设置 runtime.lastError。

在 recursive 模式下，通知有关所监控目录（位于 observedPath）中的更改。如果文件系统以 supportsNotifyTag 挂载，则必须提供 tag，并且始终报告自上次通知以来的所有更改，即使系统已关闭。可以使用 getAll 获取最后一个标记。

如需使用，必须将 file_system_provider.notify 清单选项设置为 true。

tag 的值可以是每次调用都唯一的任何字符串，因此可以识别上次注册的通知。例如，如果提供扩展服务在重新启动后启动，并且上次注册的通知的标记等于“123”，则它应针对自标记为“123”的更改以来发生的所有更改调用 notify。不能是空字符串。

并非所有提供方都能提供标记，但如果文件系统有更改日志，则标记可以是更改编号或修订版本号。

请注意，如果移除了父目录，则所有后代条目也会一并移除，并且如果这些条目受到监控，则必须将此事实告知 API。此外，如果某个目录被重命名，则所有后代条目实际上都会被移除，因为它们在原始路径下不再有条目。

如果出现错误，系统会为 runtime.lastError 设置相应的错误代码。

卸载具有指定 fileSystemId 的文件系统。必须在调用 onUnmountRequested 之后调用。此外，提供扩展程序可以决定在未请求的情况下执行卸载（例如，在连接丢失或出现文件错误时）。

如果出现错误，系统会使用相应的错误代码设置 runtime.lastError。

当请求使用 operationRequestId 中止操作时引发。必须立即停止使用 operationRequestId 执行的操作，并执行此中止请求的 successCallback。如果中止失败，则必须调用 errorCallback。请注意，不得调用已中止操作的回调，因为这些回调会被忽略。即使调用了 errorCallback，请求也可能会被强制中止。

AbortRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求设置新的目录监听器时引发。如果发生错误，则必须调用 errorCallback。

AddWatcherRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求关闭之前使用 openRequestId 打开的文件时引发。

CloseFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求显示 fileSystemId 的配置对话框时引发。如果已处理，则必须将 file_system_provider.configurable 清单选项设置为 true。

ConfigureRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求复制条目（如果是目录，则以递归方式复制）时引发。如果发生错误，则必须调用 errorCallback。

CopyEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求创建目录时引发。如果目标目录已存在，则操作必须因 EXISTS 错误而失败。如果 recursive 为 true，则必须创建目录路径中所有缺失的目录。

CreateDirectoryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求创建文件时引发。如果该文件已存在，则必须使用 "EXISTS" 错误代码调用 errorCallback。

CreateFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求删除条目时引发。如果 recursive 为 true，且相应条目是目录，则必须以递归方式删除其中的所有条目。

DeleteEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求对一组文件或目录执行操作时引发。操作完成后，必须调用 successCallback。如果发生错误，必须调用 errorCallback。

ExecuteActionRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求获取 entryPaths 中一组文件或目录的操作列表时引发。返回的所有操作都必须适用于每个条目。如果没有此类操作，则应返回一个空数组。必须通过 successCallback 调用返回操作。如果出现错误，必须调用 errorCallback。

GetActionsRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求 entryPath 处的文件或目录的元数据时引发。元数据必须通过 successCallback 调用返回。如果出现错误，必须调用 errorCallback。

GetMetadataRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求显示用于装载新文件系统的对话框时引发。如果扩展程序/应用是文件处理程序，则不应处理此事件。应处理 app.runtime.onLaunched，以便在打开文件时装载新的文件系统。对于多个装载，必须将 file_system_provider.multiple_mounts 清单选项设置为 true。

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求移动条目（如果是目录，则以递归方式移动）时引发。如果发生错误，则必须调用 errorCallback。

MoveEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求打开 filePath 中的文件时引发。如果文件不存在，则操作必须失败。可以使用 MountOptions 指定一次打开的文件数上限。

OpenFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求 directoryPath 处目录的内容时引发。必须通过多次调用 successCallback 来分块返回结果。如果出现错误，必须调用 errorCallback。

ReadDirectoryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求读取之前使用 openRequestId 打开的文件的内容时引发。必须通过多次调用 successCallback 来分块返回结果。如果出现错误，必须调用 errorCallback。

ReadFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当应移除监听器时引发。如果发生错误，则必须调用 errorCallback。

RemoveWatcherRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求将文件截断为所需长度时引发。如果发生错误，则必须调用 errorCallback。

TruncateRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求卸载具有 fileSystemId 标识符的文件系统时引发。在响应中，unmount API 方法必须与 successCallback 一起调用。如果无法卸载（例如，由于有待处理的操作），则必须调用 errorCallback。

UnmountRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求将内容写入之前使用 openRequestId 打开的文件时引发。

WriteFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "fileSystemProvider"
  ],
  ...
  "file_system_provider_capabilities": {
    "configurable": true,
    "watchable": false,
    "multiple_mounts": true,
    "source": "network"
  },
  ...
}
```

Example 2 (unknown):
```unknown
chrome.fileSystemProvider.get(  fileSystemId: string,): Promise<FileSystemInfo>
```

Example 3 (unknown):
```unknown
chrome.fileSystemProvider.getAll(): Promise<FileSystemInfo[]>
```

Example 4 (unknown):
```unknown
chrome.fileSystemProvider.mount(  options: MountOptions,): Promise<void>
```

---

## chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/extensionTypes?hl=zh-cn

**Contents:**
- chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 类型
  - ColorArray
    - 类型
  - CSSOrigin
    - 枚举
  - DeleteInjectionDetails
    - 属性
  - DocumentLifecycle

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

[number, number, number, number]

要移除的 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示应从当前页面的所有框架中移除 CSS。默认值为 false，并且仅从顶部框架中移除。如果设置了 true 和 frameId，则从所选帧及其所有子帧中移除代码。

要移除的 CSS 的来源。默认设置为 "author"。

应从中移除 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问其父文档时，该代码也会从 about:blank 和 about:srcdoc 框架中移除。默认值为 false。

脚本要在其中执行的 JavaScript 世界。可以是此扩展程序独有的隔离世界、与网页的 JavaScript 共享的 DOM 主世界，也可以是仅适用于通过 User Scripts API 注册的脚本的用户脚本世界。

图片的像素数据。必须是 ImageData 对象；例如，来自 canvas 元素。

当格式为 "jpeg" 时，控制生成图片的质量。对于 PNG 图片，系统会忽略此值。随着质量的降低，生成的图片会出现更多视觉伪影，并且存储所需的字节数也会减少。

要注入的脚本或 CSS 的详细信息。必须设置代码或文件属性，但不能同时设置这两者。

如果 allFrames 为 true，则表示 JavaScript 或 CSS 应注入到当前页面的所有框架中。默认值为 false，并且仅注入到顶部框架中。如果设置了 true 和 frameId，则代码会插入到所选帧及其所有子帧中。

要注入的 JavaScript 或 CSS 代码。

警告：请谨慎使用 code 参数。如果使用不当，可能会导致您的扩展程序遭受跨站脚本攻击

要注入的 CSS 的来源。此值只能为 CSS 指定，不能为 JavaScript 指定。默认设置为 "author"。

要注入的 JavaScript 或 CSS 文件。

应注入脚本或 CSS 的框架。默认值为 0（顶级框架）。

如果 matchAboutBlank 为 true，则当扩展程序有权访问 about:blank 和 about:srcdoc 框架的父文档时，代码也会注入到这些框架中。代码无法插入到顶级 about:-frames 中。默认值为 false。

JavaScript 或 CSS 将注入到标签页中的最早时间。默认值为“document_idle”。

JavaScript 或 CSS 将注入到标签页中的最早时间。

“document_start” 脚本在任何 CSS 文件之后注入，但在构建任何其他 DOM 或运行任何其他脚本之前注入。

“document_end” 在 DOM 完成后立即注入脚本，但在图片和框架等子资源加载之前注入。

“document_idle” 浏览器会选择一个时间在“document_end”和 window.onload 事件触发后立即注入脚本。注入的确切时间取决于文档的复杂程度和加载所需的时间，并针对网页加载速度进行了优化。以“document_idle”运行的内容脚本无需监听 window.onload 事件；它们保证在 DOM 完成后运行。如果脚本确实需要在 window.onload 之后运行，扩展程序可以使用 document.readyState 属性检查 onload 是否已触发。

---

## chrome.browserAction 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/browserAction

**Contents:**
- chrome.browserAction 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 清单
- 界面组成部分
  - 图标
  - 提示
  - 徽章
  - 弹出式窗口
- 提示

使用浏览器操作将图标放置在主 Google Chrome 工具栏中的地址栏右侧。除了图标之外，浏览器操作还可以具有提示、标记和弹出式窗口。

在下图中，地址栏右侧的多色方块是浏览器操作的图标。图标下方会显示一个弹出式窗口。

如果您想创建并非始终处于活动状态的图标，请使用网页操作，而不是浏览器操作。

在扩展程序清单中注册浏览器操作，如下所示：

您可以提供任何尺寸的图标以在 Chrome 中使用，Chrome 会选择最接近的图标并将其缩放到适当的尺寸，以填充 16-dip 的空间。不过，如果未提供确切尺寸，这种缩放可能会导致图标丢失细节或看起来模糊不清。

由于具有不太常见缩放比例（例如 1.5 倍或 1.2 倍）的设备越来越常见，因此建议您为图标提供多种尺寸。这样一来，即使图标显示尺寸发生变化，您也不需要再做任何工作来提供不同的图标！

浏览器操作可以包含图标、提示、标记和弹出式窗口。

Chrome 中的浏览器操作图标的宽度和高度均为 16 dip（与设备无关的像素）。系统会调整较大的图标以使其适合，但为获得最佳效果，请使用 16-dip 的方形图标。

您可以通过两种方式设置图标：使用静态图片或使用 HTML5 canvas 元素。对于简单的应用，使用静态图片会更轻松，但您可以使用 canvas 元素创建更动态的界面，例如流畅的动画。

静态图片可以是 WebKit 可以显示的任何格式，包括 BMP、GIF、ICO、JPEG 或 PNG。对于未打包的扩展程序，图片必须采用 PNG 格式。

如需设置图标，请使用 清单中 default_icon 的 default_icon 字段，或调用 browserAction.setIcon 方法。

为了在屏幕像素密度（比率 size_in_pixel / size_in_dip）不等于 1 时正确显示图标，可以将图标定义为一组不同尺寸的图片。系统会从该组中选择最适合 16 dip 像素大小的实际图片进行显示。图标集可以包含任何尺寸的图标规范，Chrome 会选择最合适的图标。

如需设置提示，请使用清单中 default_title 的 default_title 字段，或调用 browserAction.setTitle 方法。您可以为 default_title 字段指定特定于语言区域的字符串；有关详情，请参阅国际化。

浏览器操作可以选择性地显示徽章，即叠加在图标上的一小段文字。 借助徽章，您可以轻松更新浏览器操作，以显示有关扩展程序状态的少量信息。

由于徽章空间有限，因此应不超过 4 个字符。

分别使用 browserAction.setBadgeText 和 browserAction.setBadgeBackgroundColor 设置徽章的文字和颜色。

如果浏览器操作具有弹出式窗口，则当用户点击扩展程序的图标时，系统会显示该弹出式窗口。弹出式窗口可以包含您喜欢的任何 HTML 内容，并且会自动调整大小以适应其内容。 弹出式窗口的大小不得小于 25x25，也不得大于 800x600。

如需向浏览器操作添加弹出式窗口，请创建一个包含弹出式窗口内容的 HTML 文件。在 清单的 default_popup 中的 default_popup 字段中指定 HTML 文件，或调用 browserAction.setPopup 方法。

您可以在 examples/api/browserAction 目录中找到使用浏览器操作的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

要查询状态的标签页的 ID。如果未指定任何标签页，则返回非标签页专用状态。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

为标签页启用浏览器操作。默认值为 enabled。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

Promise<extensionTypes.ColorArray>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取浏览器操作的徽章文本。如果未指定任何标签页，则返回非标签页特定的徽章文字。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取设置为相应浏览器操作的弹出式窗口的 HTML 文档。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

一个包含四个整数的数组，这些整数的范围为 0-255，共同构成徽章的 RGBA 颜色。也可以是包含 CSS 十六进制颜色值的字符串；例如，#FF0000 或 #F00（红色）。以完全不透明度呈现颜色。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

为浏览器操作设置徽章文本。徽章显示在图标上方。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

可以传递任意数量的字符，但空间只能容纳大约四个字符。如果传递的是空字符串 ('')，则会清除标记文本。如果指定了 tabId，但 text 为 null，则指定标签页的文字会被清除，并默认设为全局徽章文字。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

为浏览器操作设置图标。图标可以指定为图片文件的路径、画布元素的像素数据，也可以指定为其中一种的字典。必须指定 path 或 imageData 属性。

ImageData 对象或表示要设置的图标的字典 {size -> ImageData}。如果图标指定为字典，则所用图片会根据屏幕的像素密度来选择。如果一个屏幕空间单位可容纳的图片像素数为 scale，则选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.imageData = foo”等同于“details.imageData = {'16': foo}”

相对图片路径或指向要设置的图标的字典 {size -> relative image path}。如果图标指定为字典，则所用图片会根据屏幕的像素密度来选择。如果一个屏幕空间单位可容纳的图片像素数为 scale，则选择大小为 scale * n 的图片，其中 n 是界面中图标的大小。必须至少指定一张图片。请注意，“details.path = foo”等同于“details.path = {'16': foo}”

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

设置当用户点击浏览器操作图标时要作为弹出式窗口打开的 HTML 文档。

要在弹出式窗口中显示的 HTML 文件的相对路径。如果设置为空字符串 ('')，则不显示任何弹出式窗口。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

设置浏览器操作的标题。此标题会显示在提示中。

将更改限制为仅在选择特定标签页时生效。在关闭标签页时自动重置。

当鼠标悬停在浏览器操作上时，浏览器操作应显示的字符串。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

在浏览器操作图标被点击时触发。如果浏览器操作具有弹出式窗口，则不会触发。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "browser_action": {
    "default_icon": {                // optional
      "16": "images/icon16.png",     // optional
      "24": "images/icon24.png",     // optional
      "32": "images/icon32.png"      // optional
    },
    "default_title": "Google Mail",  // optional, shown in tooltip
    "default_popup": "popup.html"    // optional
  },
  ...
}
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "browser_action": {
    ...
    "default_icon": "images/icon32.png"  // optional
    // equivalent to "default_icon": { "32": "images/icon32.png" }
  },
  ...
}
```

Example 3 (unknown):
```unknown
chrome.browserAction.disable(  tabId?: number,  callback?: function,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.browserAction.enable(  tabId?: number,  callback?: function,): Promise<void>
```

---

## chrome.fileSystemProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fileSystemProvider?hl=zh-cn

**Contents:**
- chrome.fileSystemProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概览
- 装载文件系统
- 配置文件系统
- 生命周期
- 类型
  - AbortRequestedOptions

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

您必须在扩展程序清单中声明“fileSystemProvider”权限和部分，才能使用文件系统提供程序 API。例如：

必须按如下方式声明 file_system_provider 部分：

“文件”应用会使用上述信息来正确呈现相关界面元素。例如，如果 configurable 设置为 true，系统将呈现用于配置音量的菜单项。同样，如果 multiple_mounts 设置为 true，则“文件”应用将允许通过界面添加多个装载点。如果 watchable 为 false，则系统会呈现刷新按钮。请注意，如果可能，您应添加对监听器的支持，以便文件系统上的更改可以立即自动反映出来。

文件系统提供程序 API 允许扩展程序支持虚拟文件系统，这些文件系统可在 ChromeOS 的文件管理器中使用。应用场景包括解压缩归档文件和访问云端硬盘以外的云服务中的文件。

提供扩展程序可以从外部来源（例如远程服务器或 USB 设备）提供文件系统内容，也可以使用本地文件（例如归档文件）作为其输入。

为了编写作为文件处理程序（来源为 "file"）的文件系统，提供程序必须是打包的应用，因为扩展程序无法使用 onLaunched 事件。

如果来源是网络或设备，则应在调用 onMountRequested 事件时装载文件系统。

提供的文件系统一旦装载，就可以通过 onConfigureRequested 事件进行配置。对于通过网络提供内容的文件系统，此方法尤其有用，可用于设置适当的凭据。您可以选择是否处理此事件。

Chrome 会记住已装载的文件系统，并在重启或重新启动后自动重新装载。因此，一旦文件系统被提供扩展程序装载，它就会一直存在，直到扩展程序被卸载或扩展程序调用 unmount 方法。

操作的标识符。对于常见操作，可以是任意字符串或 CommonActionId。

操作的标题。对于常见操作，可以忽略此属性。

观察是否应以递归方式包含所有子条目。只能针对目录设为 true。

与文件相关的信息（如果文件由云文件系统提供支持）。

云存储服务提供商的标识符（例如“drive.google.com”）。

常见操作列表。"SHARE" 用于与他人共享文件。"SAVE_FOR_OFFLINE"，用于固定（保存以供离线访问）。"OFFLINE_NOT_NECESSARY" 用于通知系统相应文件不再需要存储以供离线访问。由 onGetActionsRequested 和 onExecuteActionRequested 使用。

"OFFLINE_NOT_NECESSARY"

用于标识底层云文件系统中的特定文件的信息。如果 options 中请求了此参数，并且相应文件由 Cloud Storage 提供支持，则必须提供此参数。

相应条目的 Cloud Storage 表示形式。如果 options 中请求了此参数，并且相应文件由云存储提供支持，则必须提供此参数。对于没有云存储空间支持的本地文件，在请求时应为未定义。

如果它是目录，则为 True。如果 options 中有相应要求，则必须提供。

相应条目的 MIME 类型。始终为可选，但如果 options 中有要求，则应提供。

相应条目的上次修改时间。如果 options 中有相应要求，则必须提供。

相应条目的名称（非完整路径名称）。不得包含“/”。对于根，必须为空。如果 options 中有相应要求，则必须提供。

文件大小（以字节为单位）。如果 options 中有相应要求，则必须提供。

缩略图（采用 PNG、JPEG 或 WEBP 格式的数据 URI，大小不超过 32 KB）。可选，但只能在 onGetMetadataRequested 事件明确请求时提供。

一次可以打开的文件数上限。如果为 0，则表示不受限制。

文件系统是否支持用于观察目录的 tag 字段。

文件系统是否支持可能会更改文件系统内容的操作（例如创建、删除或写入文件）。

如果请求 cloudFileInfo 值，则设置为 true。

如果请求 cloudIdentifier 值，则设置为 true。

如果请求 is_directory 值，则设置为 true。

如果请求 mimeType 值，则设置为 true。

如果请求 modificationTime 值，则设置为 true。

如果请求 name 值，则设置为 true。

如果请求 size 值，则设置为 true。

如果请求 thumbnail 值，则设置为 true。

文件系统的字符串标识符。对于每个扩展程序来说都必须是唯一的。

一次可以打开的文件数上限。如果未指定或为 0，则表示不受限制。

框架是否应在下次登录会话时恢复文件系统。默认情况下为 true。

文件系统是否支持观测目录的 tag 字段。

文件系统是否支持可能会更改文件系统内容的操作（例如创建、删除或写入文件）。

观测到的条目发生的更改类型。如果为 DELETED，则系统会自动从观测到的条目列表中移除观测到的条目。

通知的标记。如果文件系统是使用 supportsNotifyTag 选项装载的，则此权限是必需的。请注意，此标志是必要的，可用于提供有关即使在系统关闭时也已更改的更改的通知。

供连续读取/写入和关闭请求使用的请求 ID。

打开文件的模式。由 onOpenFileRequested 使用。

将由后续读取/写入和关闭请求使用的请求 ID。

提供扩展程序时，在响应请求时以及在调用 API 方法时发生错误时使用的错误代码。若要成功，必须使用 "OK"。

如果请求 is_directory 值，则设置为 true。

如果请求 mimeType 值，则设置为 true。

如果请求 modificationTime 值，则设置为 true。

如果请求 name 值，则设置为 true。

如果请求 size 值，则设置为 true。

如果请求 thumbnail 值，则设置为 true。

观看是否应以递归方式包含所有子条目。只能针对目录设为 true。

返回有关具有所传递 fileSystemId 的文件系统的信息。

Promise<FileSystemInfo>

Promise<FileSystemInfo[]>

使用给定的 fileSystemId 和 displayName 装载文件系统。displayName 将显示在“文件”应用的左侧面板中。displayName 可以包含任何字符（包括“/”），但不能是空字符串。displayName 必须具有描述性，但不一定必须是唯一的。fileSystemId 不得为空字符串。

根据要装载的文件系统的类型，必须相应地设置 source 选项。

如果出现错误，系统会使用相应的错误代码设置 runtime.lastError。

在 recursive 模式下，通知有关所监控目录（位于 observedPath）中的更改。如果文件系统以 supportsNotifyTag 挂载，则必须提供 tag，并且始终报告自上次通知以来的所有更改，即使系统已关闭。可以使用 getAll 获取最后一个标记。

如需使用，必须将 file_system_provider.notify 清单选项设置为 true。

tag 的值可以是每次调用都唯一的任何字符串，因此可以识别上次注册的通知。例如，如果提供扩展服务在重新启动后启动，并且上次注册的通知的标记等于“123”，则它应针对自标记为“123”的更改以来发生的所有更改调用 notify。不能是空字符串。

并非所有提供方都能提供标记，但如果文件系统有更改日志，则标记可以是更改编号或修订版本号。

请注意，如果移除了父目录，则所有后代条目也会一并移除，并且如果这些条目受到监控，则必须将此事实告知 API。此外，如果某个目录被重命名，则所有后代条目实际上都会被移除，因为它们在原始路径下不再有条目。

如果出现错误，系统会为 runtime.lastError 设置相应的错误代码。

卸载具有指定 fileSystemId 的文件系统。必须在调用 onUnmountRequested 之后调用。此外，提供扩展程序可以决定在未请求的情况下执行卸载（例如，在连接丢失或出现文件错误时）。

如果出现错误，系统会使用相应的错误代码设置 runtime.lastError。

当请求使用 operationRequestId 中止操作时引发。必须立即停止使用 operationRequestId 执行的操作，并执行此中止请求的 successCallback。如果中止失败，则必须调用 errorCallback。请注意，不得调用已中止操作的回调，因为这些回调会被忽略。即使调用了 errorCallback，请求也可能会被强制中止。

AbortRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求设置新的目录监听器时引发。如果发生错误，则必须调用 errorCallback。

AddWatcherRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求关闭之前使用 openRequestId 打开的文件时引发。

CloseFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求显示 fileSystemId 的配置对话框时引发。如果已处理，则必须将 file_system_provider.configurable 清单选项设置为 true。

ConfigureRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求复制条目（如果是目录，则以递归方式复制）时引发。如果发生错误，则必须调用 errorCallback。

CopyEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求创建目录时引发。如果目标目录已存在，则操作必须因 EXISTS 错误而失败。如果 recursive 为 true，则必须创建目录路径中所有缺失的目录。

CreateDirectoryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求创建文件时引发。如果该文件已存在，则必须使用 "EXISTS" 错误代码调用 errorCallback。

CreateFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求删除条目时引发。如果 recursive 为 true，且相应条目是目录，则必须以递归方式删除其中的所有条目。

DeleteEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求对一组文件或目录执行操作时引发。操作完成后，必须调用 successCallback。如果发生错误，必须调用 errorCallback。

ExecuteActionRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求获取 entryPaths 中一组文件或目录的操作列表时引发。返回的所有操作都必须适用于每个条目。如果没有此类操作，则应返回一个空数组。必须通过 successCallback 调用返回操作。如果出现错误，必须调用 errorCallback。

GetActionsRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求 entryPath 处的文件或目录的元数据时引发。元数据必须通过 successCallback 调用返回。如果出现错误，必须调用 errorCallback。

GetMetadataRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求显示用于装载新文件系统的对话框时引发。如果扩展程序/应用是文件处理程序，则不应处理此事件。应处理 app.runtime.onLaunched，以便在打开文件时装载新的文件系统。对于多个装载，必须将 file_system_provider.multiple_mounts 清单选项设置为 true。

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求移动条目（如果是目录，则以递归方式移动）时引发。如果发生错误，则必须调用 errorCallback。

MoveEntryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求打开 filePath 中的文件时引发。如果文件不存在，则操作必须失败。可以使用 MountOptions 指定一次打开的文件数上限。

OpenFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求 directoryPath 处目录的内容时引发。必须通过多次调用 successCallback 来分块返回结果。如果出现错误，必须调用 errorCallback。

ReadDirectoryRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求读取之前使用 openRequestId 打开的文件的内容时引发。必须通过多次调用 successCallback 来分块返回结果。如果出现错误，必须调用 errorCallback。

ReadFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当应移除监听器时引发。如果发生错误，则必须调用 errorCallback。

RemoveWatcherRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

在请求将文件截断为所需长度时引发。如果发生错误，则必须调用 errorCallback。

TruncateRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求卸载具有 fileSystemId 标识符的文件系统时引发。在响应中，unmount API 方法必须与 successCallback 一起调用。如果无法卸载（例如，由于有待处理的操作），则必须调用 errorCallback。

UnmountRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

当请求将内容写入之前使用 openRequestId 打开的文件时引发。

WriteFileRequestedOptions

successCallback 参数如下所示：

errorCallback 参数如下所示：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "fileSystemProvider"
  ],
  ...
  "file_system_provider_capabilities": {
    "configurable": true,
    "watchable": false,
    "multiple_mounts": true,
    "source": "network"
  },
  ...
}
```

Example 2 (unknown):
```unknown
chrome.fileSystemProvider.get(  fileSystemId: string,): Promise<FileSystemInfo>
```

Example 3 (unknown):
```unknown
chrome.fileSystemProvider.getAll(): Promise<FileSystemInfo[]>
```

Example 4 (unknown):
```unknown
chrome.fileSystemProvider.mount(  options: MountOptions,): Promise<void>
```

---

## chrome.enterprise.login 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/enterprise/login

**Contents:**
- chrome.enterprise.login 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - exitCurrentManagedGuestSession()
    - 返回

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

**Examples:**

Example 1 (unknown):
```unknown
chrome.enterprise.login.exitCurrentManagedGuestSession(): Promise<void>
```

---

## chrome.printing 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printing

**Contents:**
- chrome.printing 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
  - cancelJob()
  - getPrinters() and getPrinterInfo()
  - submitJob()
  - 卷筒纸打印
- 类型

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

所有 chrome.printing 方法和事件都需要您在扩展程序清单中声明 "printing" 权限。例如：

以下示例演示了如何使用打印命名空间中的每种方法。此代码是从 extensions-samples GitHub 代码库中的 api-samples/printing 复制或基于该代码编写的。

此示例使用 onJobStatusChanged 处理程序在 jobStatus 既不是 PENDING 也不是 IN_PROGRESS 时隐藏“取消”按钮。请注意，在某些网络上或当 Chromebook 直接连接到打印机时，这些状态可能会过快地传递，以至于取消按钮无法显示足够长的时间来供用户调用。这是一个经过大幅简化的打印示例。

这些函数仅使用一个示例，因为获取打印机信息需要打印机 ID，而打印机 ID 是通过调用 getPrinters() 检索到的。此示例会将默认打印机的名称和说明记录到控制台。这是简化版的打印示例。

submitJob() 方法需要满足以下三个条件。

调用 submitJob() 会触发一个对话框，要求用户确认是否要打印。使用 PrintingAPIExtensionsAllowlist 可绕过确认。

这是简化版的打印示例。请注意，ticket 附加到 SubmitJobRequest 结构（第 8 行），并且要打印的数据会转换为 blob（第 10 行）。在示例中，获取打印机 ID（第 1 行）比此处所示的要复杂得多。

此示例展示了如何为连续（或卷筒）打印构建打印票证，这通常用于收据打印。卷筒纸打印的 submitJobRequest 对象与 submitJob() 示例中所示的对象相同。

如果您需要更改纸张切割的默认值，请使用 vendor_ticket_item 键。（默认值因打印机而异。）如需更改值，请提供一个包含一个成员的数组：一个 id 为 'finishings' 的对象。该值可以是 'trim'（对于在打印结束时切割卷筒纸的打印机）或 'none'（对于需要撕下打印作业的打印机）。

部分打印机不支持 "finishings" 选项。如需确定打印机是否支持此功能，请调用 getPrinterInfo() 并查找值为 "finishings/11" 的 "display_name"。

工单的 media_size 键中的值因打印机而异。如需选择合适的大小，请调用 getPrinterInfo()。返回的 GetPrinterResponse 包含 "media_size"."option" 处支持的媒体尺寸数组。选择 "is_continuous_feed" 值为 true 的选项。使用其高度和宽度值作为票券的高度和宽度值。

CDD 格式的打印机功能。该属性可能缺失。

“PENDING” Chrome 接收到打印作业，但尚未处理。

“IN_PROGRESS” 打印作业已发送以供打印。

“CANCELED” 打印作业已被用户或通过 API 取消。

"PRINTED" 打印作业已打印，未出现任何错误。

打印机的标识符；保证在设备上的打印机中是唯一的。

用于显示打印机是否符合 DefaultPrinterSelection 规则的标志。请注意，可能会有多个打印机被标记。

显示最近一次使用打印机通过 Chrome 进行打印的时间。值越低，表示打印机最近一次使用的时间越近。最小值为 0。如果缺少值，则表示打印机最近未使用过。此值保证在打印机之间是唯一的。

打印机 URI。扩展程序可以使用此属性为用户选择打印机。

"DOOR_OPEN" 打印机的机盖未关好。打印机仍接受打印作业。

“TRAY_MISSING” 打印机的托盘缺失。打印机仍接受打印作业。

“OUT_OF_INK” 打印机墨尽。打印机仍接受打印作业。

“OUT_OF_PAPER” 打印机缺纸。打印机仍接受打印作业。

“OUTPUT_FULL” 打印机的出纸区域（例如出纸盘）已满。打印机仍接受打印作业。

“PAPER_JAM” 打印机卡纸。打印机仍接受打印作业。

“GENERIC_ISSUE” 某些一般性问题。打印机仍接受打印作业。

“已停止” 打印机已停止，无法打印，但仍可接受打印作业。

“UNREACHABLE” 打印机无法连接，且不接受打印作业。

“EXPIRED_CERTIFICATE” SSL 证书已过期。打印机接受作业，但作业失败。

要提交的打印作业。支持的内容类型为“application/pdf”和“image/png”。云作业票证不应包含 FitToPageTicketItem、PageRangeTicketItem 和 ReverseOrderTicketItem 字段，因为这些字段与本机打印无关。VendorTicketItem 为可选项。必须提供所有其他字段。

已创建的打印作业的 ID。这是设备上所有打印作业的唯一标识符。如果状态不是“OK”，jobId 将为 null。

“USER_REJECTED” 发送的打印作业请求被用户拒绝。

每分钟可调用 getPrinterInfo 的次数上限。

每分钟可调用 submitJob 的次数上限。

要取消的打印作业的 ID。此值应与在 SubmitJobResponse 中收到的 ID 相同。

返回打印作业的状态。如果具有指定 jobId 的打印作业不存在，此调用将失败并显示运行时错误。jobId：要返回状态的打印作业的 ID。此值应与在 SubmitJobResponse 中收到的 ID 相同。

以 CDD 格式返回打印机的状态和功能。如果没有安装具有指定 ID 的打印机，此调用将失败并显示运行时错误。

Promise<GetPrinterInfoResponse>

返回设备上可用打印机的列表。包括手动添加的打印机、企业打印机和发现的打印机。

提交打印作业。如果扩展程序未列在 PrintingAPIExtensionsAllowlist 政策中，系统会提示用户接受打印作业。 在 Chrome 120 之前，此函数不返回 promise。

Promise<SubmitJobResponse>

当作业的状态发生变化时触发的事件。仅针对此扩展程序创建的作业触发此事件。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "printing"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.printing.onJobStatusChanged.addListener((jobId, status) => {
  const cancelButton = document.getElementById("cancelButton");
  cancelButton.addEventListener('click', () => {
    chrome.printing.cancelJob(jobId).then((response) => {
      if (response !== undefined) {
        console.log(response.status);
      }
      if (chrome.runtime.lastError !== undefined) {
        console.log(chrome.runtime.lastError.message);
      }
    });
  });
  if (status !== "PENDING" && status !== "IN_PROGRESS") {
    cancelButton.style.visibility = 'hidden';
  } else {
    cancelButton.style.visibility = 'visible';
  }
}
```

Example 3 (javascript):
```javascript
​​const printers = await chrome.printing.getPrinters();
const defaultPrinter = printers.find((printer) => {
  const printerInfo = await chrome.printing.getPrinterInfo(printer.id);
  return printerInfo.isDefault;
}
console.log(`Default printer: ${defaultPrinter.name}.\n\t${defaultPrinter.description}`);
```

Example 4 (javascript):
```javascript
const defaultPrinter = getDefaultPrinter();
const ticket = getPrinterTicket(defaultPrinter);
const arrayBuffer = getPrintData();
const submitJobRequest = {
  job: {
    printerId: defaultPrinter,
    title: 'test job',
    ticket: ticket,
    contentType: 'application/pdf',
    document: new Blob([new Uint8Array(arrayBuffer)], {
      type: 'application/pdf'
    });
  }
};

chrome.printing.submitJob(submitJobRequest, (response) => {
  if (response !== undefined) {
    console.log(response.status);
  }
  if (chrome.runtime.lastError !== undefined) {
    console.log(chrome.runtime.lastError.message);
  }
});
```

---

## chrome.idle 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/idle?hl=zh-cn

**Contents:**
- chrome.idle 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - IdleState
    - 枚举
- 方法
  - getAutoLockDelay()
    - 返回
  - queryState()

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

您必须在扩展程序的清单中声明 "idle" 权限，才能使用空闲 API。例如：

获取屏幕在空闲时自动锁定的时间（以秒为单位）。如果屏幕从不自动锁定，则返回零时长。目前仅在 ChromeOS 上受支持。

如果系统已锁定，则返回“locked”；如果用户在指定秒数内未生成任何输入，则返回“idle”；否则返回“active”。

如果自检测到上次用户输入以来已过去 detectionIntervalInSeconds 秒，则系统被视为处于空闲状态。

设置用于确定系统何时处于 onStateChanged 事件的空闲状态的时间间隔（以秒为单位）。默认间隔为 60 秒。

用于确定系统何时处于空闲状态的阈值（以秒为单位）。

当系统更改为活动、空闲或锁定状态时触发。如果屏幕已锁定或屏幕保护程序已激活，则触发的事件为“locked”；如果系统已解锁，但用户在指定秒数内未生成任何输入，则触发的事件为“idle”；当用户在闲置的系统上生成输入时，触发的事件为“active”。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "idle"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.idle.getAutoLockDelay(): Promise<number>
```

Example 3 (unknown):
```unknown
chrome.idle.queryState(  detectionIntervalInSeconds: number,): Promise<IdleState>
```

Example 4 (unknown):
```unknown
chrome.idle.setDetectionInterval(  intervalInSeconds: number,): void
```

---

## chrome.fileBrowserHandler 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/fileBrowserHandler?hl=zh-cn

**Contents:**
- chrome.fileBrowserHandler 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
- 权限
- 可用性
  - 实现文件浏览器处理程序
- 类型
  - FileHandlerExecuteEventDetails
    - 属性
- 事件

使用 chrome.fileBrowserHandler API 扩展 Chrome 操作系统的文件浏览器。例如，您可以使用此 API 让用户向您的网站上传文件。

当用户按 Alt+Shift+M 或连接外部存储设备（例如 SD 卡、USB 密钥、外部驱动器或数码相机）时，ChromeOS 文件浏览器将会启动。除了显示外部设备上的文件外，文件浏览器还可以显示用户之前保存到系统的文件。

当用户选择一个或多个文件时，文件浏览器会添加按钮，用于表示这些文件的有效处理程序。例如，在下面的屏幕截图中，选择包含“.png”的文件后缀的结果是“保存到图库”按钮。

您必须在扩展程序清单中声明 "fileBrowserHandler" 权限。

您必须使用 "file_browser_handlers" 字段将扩展程序注册为至少一种文件类型的处理程序。您还应提供 16x16 的图标，以显示在按钮上。例如：

要使用此 API，您必须实现一个用于处理 chrome.fileBrowserHandler 的 onExecute 事件的函数。每当用户点击代表您的文件浏览器处理程序的按钮时，系统就会调用您的函数。在您的函数中，使用 File System API 来获取对文件内容的访问权限。示例如下：

fileBrowserHandler.onExecute 事件的事件详情载荷。

表示相应操作目标文件的 Entry 实例数组（在 ChromeOS 文件浏览器中选择）。

引发此事件的标签页的 ID。标签页 ID 在浏览器会话中是唯一的。

通过 ChromeOS 文件浏览器执行文件系统操作时触发。

FileHandlerExecuteEventDetails

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "file_browser_handlers": [
    {
      "id": "upload",
      "default_title": "Save to Gallery", // What the button will display
      "file_filters": [
        "filesystem:*.jpg",  // To match all files, use "filesystem:*.*"
        "filesystem:*.jpeg",
        "filesystem:*.png"
      ]
    }
  ],
  "permissions" : [
    "fileBrowserHandler"
  ],
  "icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  ...
}
```

Example 2 (javascript):
```javascript
chrome.fileBrowserHandler.onExecute.addListener(async (id, details) => {
  if (id !== 'upload') {
    return;  // check if you have multiple file_browser_handlers
  }

  for (const entry of detail.entries) {
    // the FileSystemFileEntry doesn't have a Promise API, wrap in one
    const file = await new Promise((resolve, reject) => {
      entry.file(resolve, reject);
    });
    const buffer = await file.arrayBuffer();
    // do something with buffer
  }
});
```

Example 3 (unknown):
```unknown
chrome.fileBrowserHandler.onExecute.addListener(  callback: function,)
```

Example 4 (javascript):
```javascript
(id: string, details: FileHandlerExecuteEventDetails) => void
```

---

## chrome.audio 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/audio?hl=zh-cn

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

指定应处于活跃状态的设备的 ID。如果未设置输入列表或输出列表，相应类别的设备不受影响。

为流类型设置静音状态。静音状态将应用于具有指定音频流类型的所有音频设备。

在音频设备发生更改时触发，无论是添加新设备还是移除现有设备。

当音频输入或输出的静音状态发生变化时触发。请注意，静音状态是系统范围的，新值适用于具有指定音频流类型的每个音频设备。

**Examples:**

Example 1 (unknown):
```unknown
chrome.audio.getDevices(  filter?: DeviceFilter,): Promise<AudioDeviceInfo[]>
```

Example 2 (unknown):
```unknown
chrome.audio.getMute(  streamType: StreamType,): Promise<boolean>
```

Example 3 (unknown):
```unknown
chrome.audio.setActiveDevices(  ids: DeviceIdLists,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.audio.setMute(  streamType: StreamType,  isMuted: boolean,): Promise<void>
```

---

## chrome.privacy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/privacy

**Contents:**
- chrome.privacy 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
- 示例
- 类型
  - IPHandlingPolicy
    - 枚举
- 属性
  - network

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

您必须在扩展程序的清单中声明“隐私权”权限，才能使用该 API。例如：

读取 Chrome 设置的当前值非常简单。您需要先找到感兴趣的属性，然后对该对象调用 get()，以便检索其当前值和扩展程序的控制级别。例如，如需确定 Chrome 的信用卡自动填充功能是否已启用，您可以编写以下代码：

更改设置的值稍微复杂一些，因为您必须先验证扩展程序是否可以控制该设置。如果您的扩展程序切换的设置要么通过企业政策锁定为特定值（levelOfControl 将设置为“not_controllable”），要么由其他扩展程序控制该值（levelOfControl 将设置为“controlled_by_other_extensions”），那么用户不会看到其设置有任何变化。set() 调用将成功，但设置会立即被覆盖。由于这可能会让用户感到困惑，因此建议在用户选择的设置实际上未应用时提醒用户。

这意味着，您应该使用 get() 方法来确定您的访问权限级别，然后仅当扩展程序可以控制相应设置时才调用 set()（实际上，如果扩展程序无法控制相应设置，最好在视觉上停用该功能，以免用户感到困惑）：

如果您对设置值的变化感兴趣，请为其 onChange 事件添加监听器。除了其他用途之外，此功能还允许您在最近安装的扩展程序获取设置控制权或企业政策替换您的控制权时警告用户。如需监听信用卡自动填充状态的变化，例如，以下代码就足够了：

如需试用此 API，请从 chrome-extension-samples 代码库中安装隐私权 API 示例。

"default_public_and_private_interfaces"

"default_public_interface_only"

"disable_non_proxied_udp"

影响 Chrome 一般网络连接处理方式的设置。

types.ChromeSetting<boolean>

如果启用，Chrome 会尝试预先解析 DNS 条目并抢先打开与服务器的 TCP 和 SSL 连接，从而加快您的网页浏览速度。此偏好设置仅影响 Chrome 内部预测服务采取的操作。它不会影响网页发起的预取或预连接。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<IPHandlingPolicy>

允许用户指定媒体性能/隐私权权衡，这会影响 WebRTC 流量的路由方式以及公开的本地地址信息量。此偏好的值为 IPHandlingPolicy 类型，默认值为 default。

用于启用或停用需要 Google 和默认搜索引擎提供的第三方网络服务的功能的设置。

types.ChromeSetting<boolean>

如果启用，Chrome 会使用网络服务来帮助解决导航错误。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会建议自动填充地址和其他表单数据。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会提供自动填写信用卡表单的功能。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

请改用 privacy.services.autofillAddressEnabled 和 privacy.services.autofillCreditCardEnabled。此属性保留在此版本中是为了实现向后兼容性，但未来会移除。

如果启用此设置，Chrome 会提供自动填写表单的选项。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

启用此项后，密码管理工具会询问您是否要保存密码。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会尽最大努力保护您免遭钓鱼式攻击和恶意软件的侵害。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果此政策处于启用状态，当安全浏览功能阻止某个网页时，Chrome 会向 Google 发送额外信息，例如被阻止网页的内容。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果启用此设置，Chrome 会将您在多功能框中输入的文字发送给您的默认搜索引擎，后者会根据您目前输入的文字预测可能的网站和搜索补全选项。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会使用网络服务来帮助修正拼写错误。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果启用此政策，Chrome 会询问是否翻译非您所用语言的网页。此偏好的值为布尔值，默认值为 true。

用于确定 Chrome 向网站提供哪些信息的设置。

types.ChromeSetting<boolean>

如果停用，Attribution Reporting API 和 Private Aggregation API 将被停用。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用这些 API。如果您尝试将这些 API 设置为 true，系统会抛出错误。

types.ChromeSetting<boolean>

如果启用，Chrome 会在您的请求中发送“请勿跟踪”标头 (DNT: 1)。此偏好的值为布尔值，默认值为 false。

types.ChromeSetting<boolean>

如果停用，Fledge API 将处于停用状态。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

types.ChromeSetting<boolean>

如果启用，Chrome 会在网站请求时发送审核 ping (<a ping>)。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

仅适用于 Windows 和 ChromeOS：如果启用，Chrome 会向插件提供一个唯一 ID，以便运行受保护的内容。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果启用，Chrome 会随请求发送 referer 标头。是的，此偏好的名称与拼写错误的标头不一致。不会，我们不会更改。此偏好的值为布尔值，默认值为 true。

types.ChromeSetting<boolean>

如果停用，Related Website Sets 会被停用。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

types.ChromeSetting<boolean>

如果停用，Chrome 会阻止第三方网站设置 Cookie。此偏好的值为布尔值，默认值为 true。扩展程序不得在无痕模式下启用此 API。在无痕模式下，第三方 Cookie 会被屏蔽，并且只能在网站级别允许使用。如果您尝试在无痕模式下将此 API 设置为 true，则会抛出错误。

注意：如果个别网站具有有效的豁免，或者它们改用 Storage Access API，则即使此 API 返回 false，它们可能仍能访问第三方 Cookie。

types.ChromeSetting<boolean>

如果停用，Topics API 将处于停用状态。此偏好的值为布尔值，默认值为 true。扩展程序只能通过将值设置为 false 来停用此 API。如果您尝试将此 API 设置为 true，则会抛出错误。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "privacy"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.get({}, function(details) {
  if (details.value) {
    console.log('Autofill is on!');
  } else {
    console.log('Autofill is off!');
  }
});
```

Example 3 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.get({}, function(details) {
  if (details.levelOfControl === 'controllable_by_this_extension') {
    chrome.privacy.services.autofillCreditCardEnabled.set({ value: true }, function() {
      if (chrome.runtime.lastError === undefined) {
        console.log("Hooray, it worked!");
      } else {
        console.log("Sadness!", chrome.runtime.lastError);
      }
    });
  }
});
```

Example 4 (unknown):
```unknown
chrome.privacy.services.autofillCreditCardEnabled.onChange.addListener(
  function (details) {
    // The new value is stored in `details.value`, the new level of control
    // in `details.levelOfControl`, and `details.incognitoSpecific` will be
    // `true` if the value is specific to Incognito mode.
  }
);
```

---

## chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/sessions/?hl=zh-cn

**Contents:**
- chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - Device
    - 属性
  - Filter
    - 属性
  - Session
    - 属性

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

外部设备的打开窗口会话列表，按会话的修改时间从最近到最远排序。

相应列表中要提取的条目数上限。省略此参数可提取最大条目数 (sessions.MAX_SESSION_RESULTS)。

窗口或标签页关闭或修改的时间，以自纪元开始算起的秒数表示。

如果相应条目描述的是标签页，则为 tabs.Tab。系统会设置此值或 sessions.Session.window。

如果相应条目描述的是窗口，则为 windows.Window。系统会设置此值或 sessions.Session.tab。

请求的列表中将包含的 sessions.Session 的数量上限。

重新打开 windows.Window 或 tabs.Tab，并提供一个可选的回调函数，用于在条目恢复后运行。

要恢复的 windows.Window.sessionId 或 tabs.Tab.sessionId。如果未指定此参数，系统会恢复最近关闭的会话。

当最近关闭的标签页和/或窗口发生更改时触发。此事件不会监控同步会话更改。

**Examples:**

Example 1 (unknown):
```unknown
chrome.sessions.getDevices(  filter?: Filter,): Promise<Device[]>
```

Example 2 (unknown):
```unknown
chrome.sessions.getRecentlyClosed(  filter?: Filter,): Promise<Session[]>
```

Example 3 (unknown):
```unknown
chrome.sessions.restore(  sessionId?: string,): Promise<Session>
```

Example 4 (unknown):
```unknown
chrome.sessions.onChanged.addListener(  callback: function,)
```

---

## chrome.idle 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/idle

**Contents:**
- chrome.idle 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - IdleState
    - 枚举
- 方法
  - getAutoLockDelay()
    - 返回
  - queryState()

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

您必须在扩展程序的清单中声明 "idle" 权限，才能使用空闲 API。例如：

获取屏幕在空闲时自动锁定的时间（以秒为单位）。如果屏幕从不自动锁定，则返回零时长。目前仅在 ChromeOS 上受支持。

如果系统已锁定，则返回“locked”；如果用户在指定秒数内未生成任何输入，则返回“idle”；否则返回“active”。

如果自检测到上次用户输入以来已过去 detectionIntervalInSeconds 秒，则系统被视为处于空闲状态。

设置用于确定系统何时处于 onStateChanged 事件的空闲状态的时间间隔（以秒为单位）。默认间隔为 60 秒。

用于确定系统何时处于空闲状态的阈值（以秒为单位）。

当系统更改为活动、空闲或锁定状态时触发。如果屏幕已锁定或屏幕保护程序已激活，则触发的事件为“locked”；如果系统已解锁，但用户在指定秒数内未生成任何输入，则触发的事件为“idle”；当用户在闲置的系统上生成输入时，触发的事件为“active”。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "idle"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.idle.getAutoLockDelay(): Promise<number>
```

Example 3 (unknown):
```unknown
chrome.idle.queryState(  detectionIntervalInSeconds: number,): Promise<IdleState>
```

Example 4 (unknown):
```unknown
chrome.idle.setDetectionInterval(  intervalInSeconds: number,): void
```

---

## chrome.topSites 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/topSites?hl=zh-cn

**Contents:**
- chrome.topSites 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 示例
- 类型
  - MostVisitedURL
    - 属性
- 方法
  - get()
    - 返回

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

您必须在扩展程序的清单中声明“topSites”权限，才能使用此 API。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 topSites API 示例。

封装最常访问网址的对象，例如新标签页上的默认快捷方式。

Promise<MostVisitedURL[]>

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "topSites",
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.topSites.get(): Promise<MostVisitedURL[]>
```

---

## chrome.devtools.performance 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/performance?hl=zh-cn

**Contents:**
- chrome.devtools.performance 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 概念和用法
- 示例
- 事件
  - onProfilingStarted
    - 参数
  - onProfilingStopped
    - 参数

使用 chrome.devtools.performance API 监听开发者工具“性能”面板中的录制状态更新。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

借助 chrome.devtools.performance API，开发者可以与 Chrome DevTools 中 Performance 面板的录制功能进行互动。您可以使用此 API 在录制开始或停止时收到通知。

通过监听这些事件，开发者可以创建会响应性能面板中的录制状态的扩展程序，在性能分析期间提供额外的自动化功能。

您可以通过以下方式使用此 API 监听录制状态更新

**Examples:**

Example 1 (javascript):
```javascript
chrome.devtools.performance.onProfilingStarted.addListener(() => {
  // Profiling started listener implementation
});

chrome.devtools.performance.onProfilingStopped.addListener(() => {
  // Profiling stopped listener implementation
})
```

Example 2 (unknown):
```unknown
chrome.devtools.performance.onProfilingStarted.addListener(  callback: function,)
```

Example 3 (unknown):
```unknown
chrome.devtools.performance.onProfilingStopped.addListener(  callback: function,)
```

---

## chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/devtools/recorder

**Contents:**
- chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 概念和用法
  - 自定义导出功能
  - 自定义重放按钮
- 示例
  - 导出插件
  - 重放插件
- 类型

使用 chrome.devtools.recorder API 自定义开发者工具中的“Recorder”面板。

devtools.recorder API 是一项预览版功能，可让您扩展 Chrome 开发者工具中的 Recorder 面板。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

如需注册扩展插件，请使用 registerRecorderExtensionPlugin 函数。此函数需要插件实例、name 和 mediaType 作为参数。插件实例必须实现两种方法：stringify 和 stringifyStep。

该扩展程序提供的 name 会显示在 Recorder 面板的 Export 菜单中。

根据用户的导出环境，当用户点击该扩展程序提供的导出选项时， Recorder 面板会调用以下两个函数之一：

mediaType 参数允许该扩展程序指定其使用 stringify 和 stringifyStep 函数。例如，如果结果是 JavaScript，则返回 application/javascript 计划。

如需在 Recorder 中自定义“重放”按钮，请使用 registerRecorderExtensionPlugin 函数。插件必须实现 replay 方法，自定义设置才能生效。 如果检测到该方法，Recorder 中会显示重放按钮。 点击此按钮后，系统会将当前录制对象作为第一个参数传递给 replay 方法。

此时，该扩展程序可以显示用于处理重放的 RecorderView，或使用其他扩展程序 API 来处理重放请求。如需创建新的 RecorderView，请调用 chrome.devtools.recorder.createView。

以下代码会实现一个扩展程序插件，该插件会使用 JSON.stringify 将录制转换为字符串：

以下代码会实现一个扩展程序插件，该插件会创建虚拟录音机视图并在收到重放请求时显示该视图：

在 GitHub 上查找完整的扩展程序示例。

“Recorder”面板调用以自定义“Recorder”面板的插件接口。

用户与网页互动的记录。这应与 Puppeteer 的录制架构匹配。

将录音从“Recorder”面板格式转换为字符串。

用户与网页互动的记录。这应与 Puppeteer 的录制架构匹配。

将录音步骤从“Recorder”面板格式转换为字符串。

stringifyStep 函数如下所示：

记录用户与网页互动的步骤。此架构应与 Puppeteer 的步骤架构匹配。

表示扩展程序创建的要嵌入“Recorder”面板的视图。

onHidden.addListener 函数如下所示：

onShown.addListener 函数如下所示：

表示扩展程序希望在“记录器”面板中显示此视图。

创建可以处理重放的视图。此视图将嵌入到“记录器”面板中。

在开发者工具工具栏中的扩展程序图标旁边显示的标题。

面板的 HTML 页面相对于扩展程序目录的路径。

RecorderExtensionPlugin

实现 RecorderExtensionPlugin 接口的实例。

**Examples:**

Example 1 (unknown):
```unknown
class MyPlugin {
  stringify(recording) {
    return Promise.resolve(JSON.stringify(recording));
  }
  stringifyStep(step) {
    return Promise.resolve(JSON.stringify(step));
  }
}

chrome.devtools.recorder.registerRecorderExtensionPlugin(
  new MyPlugin(),
  /*name=*/'MyPlugin',
  /*mediaType=*/'application/json'
);
```

Example 2 (javascript):
```javascript
const view = await chrome.devtools.recorder.createView(
  /* name= */ 'ExtensionName',
  /* pagePath= */ 'Replay.html'
);

let latestRecording;

view.onShown.addListener(() => {
  // Recorder has shown the view. Send additional data to the view if needed.
  chrome.runtime.sendMessage(JSON.stringify(latestRecording));
});

view.onHidden.addListener(() => {
  // Recorder has hidden the view.
});

export class RecorderPlugin {
  replay(recording) {
    // Share the data with the view.
    latestRecording = recording;
    // Request to show the view.
    view.show();
  }
}

chrome.devtools.recorder.registerRecorderExtensionPlugin(
  new RecorderPlugin(),
  /* name=*/ 'CoffeeTest'
);
```

Example 3 (javascript):
```javascript
(recording: object) => {...}
```

Example 4 (javascript):
```javascript
(recording: object) => {...}
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

Example 2 (javascript):
```javascript
const canvas = new OffscreenCanvas(16, 16);
const context = canvas.getContext('2d');
context.clearRect(0, 0, 16, 16);
context.fillStyle = '#00FF00';  // Green
context.fillRect(0, 0, 16, 16);
const imageData = context.getImageData(0, 0, 16, 16);
chrome.action.setIcon({imageData: imageData}, () => { /* ... */ });
```

Example 3 (javascript):
```javascript
chrome.action.setBadgeBackgroundColor(
  {color: [0, 255, 0, 0]},  // Green
  () => { /* ... */ },
);

chrome.action.setBadgeBackgroundColor(
  {color: '#00FF00'},  // Also green
  () => { /* ... */ },
);

chrome.action.setBadgeBackgroundColor(
  {color: 'green'},  // Also, also green
  () => { /* ... */ },
);
```

Example 4 (javascript):
```javascript
function getTabId() { /* ... */}
function getTabBadge() { /* ... */}

chrome.action.setBadgeText(
  {
    text: getTabBadge(tabId),
    tabId: getTabId(),
  },
  () => { ... }
);
```

---

## chrome.tts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/tts?hl=zh-cn

**Contents:**
- chrome.tts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 生成语音
  - 监听事件
  - SSML 标记
  - 选择一种语音
- 类型
  - EventType

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

Chrome 在 Windows（使用 SAPI 5）、Mac OS X 和 ChromeOS 上提供此功能，使用操作系统提供的语音合成功能。在所有平台上，用户都可以安装将自己注册为替代语音引擎的扩展程序。

从扩展程序调用 speak() 以进行语音对话。例如：

如需立即停止朗读，只需调用 stop()：

您可以提供用于控制语音各种属性（例如语速、音高等）的选项。例如：

最好还指定语言，以便选择支持该语言（以及地区方言，如果适用）的合成器。

默认情况下，每次调用 speak() 都会中断任何正在进行的语音并立即发声。如需确定通话是否会中断任何内容，您可以调用 isSpeaking()。此外，您还可以使用 enqueue 选项将此话语添加到话语队列中，以便在当前话语说完后说出此话语。

如需查看所有选项的完整说明，请参阅 tts.speak()。并非所有语音引擎都支持所有选项。

为了捕获错误并确保您正确调用 speak()，请传递一个不带任何实参的回调函数。在回调内部，检查 runtime.lastError 以查看是否存在任何错误。

回调会立即返回，在引擎开始生成语音之前。回调的目的是提醒您在使用 TTS API 时出现的语法错误，而不是捕获在合成和输出语音过程中可能发生的所有错误。如需捕获这些错误，您还需要使用下一部分中介绍的事件监听器。

如需获取有关合成语音状态的更多实时信息，请在选项中向 speak() 传递事件监听器，如下所示：

每个事件都包含事件类型、当前语音相对于话语的字符索引，以及（对于错误事件）可选的错误消息。事件类型包括：

有四种事件类型（'end'、'interrupted'、'cancelled' 和 'error'）是最终事件类型。收到上述任一事件后，此话语将不再发声，并且不会再收到来自此话语的新事件。

某些语音可能不支持所有事件类型，而某些语音可能根本不会发送任何事件。如果您不希望使用语音，除非它发送某些事件，请在选项对象的 requiredEventTypes 成员中传递所需的事件，或使用 getVoices() 选择符合您要求的语音。下文将介绍这两种方法。

此 API 中使用的发音可能包含使用语音合成标记语言 (SSML) 的标记。如果您使用 SSML，则 speak() 的第一个实参应为包含 XML 标头和顶级 <speak> 标记的完整 SSML 文档，而不是文档片段。

并非所有语音引擎都支持所有 SSML 标记，有些可能根本不支持 SSML，但所有引擎都必须忽略它们不支持的任何 SSML，并仍能朗读基础文本。

默认情况下，Chrome 会根据语言为要朗读的每个话语选择最合适的语音。在大多数 Windows、Mac OS X 和 ChromeOS 系统上，操作系统提供的语音合成功能应该能够以至少一种语言朗读任何文本。不过，某些用户可能可以使用来自操作系统和由其他 Chrome 扩展程序实现的语音引擎的各种语音。在这些情况下，您可以实现自定义代码来选择合适的语音，或者向用户显示选择列表。

如需获取所有语音的列表，请调用 getVoices() 并向其传递一个以 TtsVoice 对象数组作为实参的函数：

来自 TTS 引擎的事件，用于传达朗读的状态。

话语中当前字符的索引。对于字词事件，该事件会在一个字词结束时触发，并在下一个字词开始之前触发。charIndex 表示文本中下一个要朗读的字词的开头位置。

如果事件类型为 error，则为错误说明。

话语下一部分的长度。例如，在 word 事件中，这是接下来要朗读的字词的长度。如果语音引擎未设置此值，则会将其设置为 -1。

类型可以是 start（语音开始后立即）、word（到达字词边界时）、sentence（到达句子边界时）、marker（到达 SSML mark 元素时）、end（到达话语末尾时）、interrupted（在到达末尾之前停止或中断话语时）、cancelled（在合成之前从队列中移除时）或 error（发生任何其他错误时）。暂停语音时，如果特定话语在中间暂停，则会触发 pause 事件；如果话语恢复语音，则会触发 resume 事件。请注意，如果在话语之间暂停语音，可能不会触发暂停和恢复事件。

您感兴趣的要监听的 TTS 事件类型。如果缺少此参数，则可能会发送所有事件类型。

如果为 true，则在 TTS 正在进行时将此话语加入队列。如果为 false（默认值），则在说出此新话语之前，会中断任何当前语音并清空语音队列。

要使用的语音引擎的扩展程序 ID（如果已知）。

用于合成的语言，格式为语言-地区。示例：“en”“en-US”“en-GB”“zh-CN”。

说话音调介于 0 到 2 之间（含），其中 0 为最低，2 为最高。1.0 对应于语音的默认音高。

相对于此语音的默认语速的语速。1.0 是默认速率，通常约为每分钟 180 到 220 个字。2.0 表示快一倍的速度，0.5 则表示原有速度的一半。严格禁止使用低于 0.1 或高于 10.0 的值，但许多语音会进一步限制最低和最高速率，例如，即使您指定的值大于 3.0，特定语音实际上也可能不会以超过正常速度 3 倍的速度说话。

要用于合成的语音的名称。如果为空，则使用任何可用的声音。

说话音量，介于 0 到 1 之间（含 0 和 1），其中 0 为最低音量，1 为最高音量，默认值为 1.0。

此函数会随说出话语的过程中发生的事件一起调用。

来自文字转语音引擎的更新事件，用于指示相应朗读的状态。

EventTypeEventType[] 可选

相应语音支持的语言，格式为 language-region。示例：“en”“en-US”“en-GB”“zh-CN”。

如果为 true，则表示合成引擎是远程网络资源。延迟时间可能会更长，并且可能会产生带宽费用。

检查引擎当前是否正在说话。在 Mac OS X 上，只要系统语音引擎正在说话，结果就为 true，即使语音不是由 Chrome 发起的也是如此。

暂停语音合成，可能会在话语中间暂停。调用以恢复或停止将取消暂停语音。

如果语音之前处于暂停状态，则从上次中断的位置继续朗读。

要朗读的文本，可以是纯文本，也可以是完整且格式正确的 SSML 文档。不支持 SSML 的语音引擎会去除标记并朗读文本。文本的长度上限为 32,768 个字符。

停止任何当前语音，并清空所有待处理话语的队列。此外，如果之前暂停了语音，现在会取消暂停，以便在下次调用 speak 时继续朗读。

当 getVoices 将返回的 tts.TtsVoice 列表发生变化时调用。

**Examples:**

Example 1 (unknown):
```unknown
chrome.tts.speak('Hello, world.');
```

Example 2 (unknown):
```unknown
chrome.tts.stop();
```

Example 3 (unknown):
```unknown
chrome.tts.speak('Hello, world.', {'rate': 2.0});
```

Example 4 (unknown):
```unknown
chrome.tts.speak('Hello, world.', {'lang': 'en-US', 'rate': 2.0});
```

---

## chrome.offscreen 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/offscreen

**Contents:**
- chrome.offscreen 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 原因
- 示例
  - 维护屏幕外文档的生命周期
  - 在 Chrome 116 之前：检查屏幕外文档是否已打开
- 类型

使用 offscreen API 创建和管理屏幕外文档。

如需使用 Offscreen API，请在扩展程序清单中声明 "offscreen" 权限。例如：

Service worker 没有 DOM 访问权限，并且许多网站都有内容安全政策来限制内容脚本的功能。借助 Offscreen API，扩展程序可以在隐藏文档中使用 DOM API，而不会通过打开新窗口或标签页来中断用户体验。runtime API 是离屏文档支持的唯一扩展程序 API。

作为屏幕外文档加载的页面与其他类型的扩展程序页面不同，其处理方式也不同。 扩展程序的权限会沿用到离屏文档，但对扩展程序 API 的访问权限有限制。例如，由于 chrome.runtime API 是离屏文档支持的唯一扩展服务 API，因此必须使用该 API 的成员来处理消息传递。

使用 chrome.offscreen.createDocument() 和 chrome.offscreen.closeDocument() 创建并关闭屏幕外文档。createDocument() 需要提供文档的 url、原因和理由：

如需查看有效原因的列表，请参阅原因部分。原因是在创建文档时设置的，用于确定文档的有效期。AUDIO_PLAYBACK 原因会将文档设置为在 30 秒后关闭，且不播放音频。所有其他原因都不会设置使用期限限制。

以下示例展示了如何确保存在屏幕外文档。setupOffscreenDocument() 函数会调用 runtime.getContexts() 来查找现有的屏幕外文档，或者在文档尚不存在时创建该文档。

在向屏幕外文档发送消息之前，请调用 setupOffscreenDocument() 以确保该文档存在，如以下示例所示。

如需查看完整示例，请参阅 GitHub 上的 offscreen-clipboard 和 offscreen-dom 演示。

runtime.getContexts() 已在 Chrome 116 中添加。在旧版 Chrome 中，使用 clients.matchAll() 检查是否存在屏幕外文档：

开发者提供的字符串，用于更详细地说明需要背景信息的原因。用户代理 _可以_在向用户显示时使用此属性。

“AUDIO_PLAYBACK” 指定离屏文档负责播放音频。

"IFRAME_SCRIPTING" 指定离屏文档需要嵌入 iframe 并通过脚本修改 iframe 的内容。

“DOM_SCRAPING” 指定离屏文档需要嵌入 iframe 并抓取其 DOM 以提取信息。

“BLOBS” 指定离屏文档需要与 Blob 对象（包括 URL.createObjectURL()）互动。

“DOM_PARSER” 指定离屏文档需要使用 DOMParser API。

“USER_MEDIA” 指定离屏文档需要与来自用户媒体（例如 getUserMedia()）的媒体流进行交互。

“DISPLAY_MEDIA” 指定离屏文档需要与来自展示媒体（例如 getDisplayMedia()）的媒体流进行互动。

“WEB_RTC” 指定了离屏文档需要使用 WebRTC API。

“CLIPBOARD” 指定屏幕外文档需要与 Clipboard API 互动。

"LOCAL_STORAGE" 指定屏幕外文档需要访问 localStorage。

“WORKERS” 指定了离屏文档需要衍生工作器。

“BATTERY_STATUS” 指定了离屏文档需要使用 navigator.getBattery。

“MATCH_MEDIA” 指定离屏文档需要使用 window.matchMedia。

“GEOLOCATION” 指定离屏文档需要使用 navigator.geolocation。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "offscreen"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.offscreen.createDocument({
  url: 'off_screen.html',
  reasons: ['CLIPBOARD'],
  justification: 'reason for needing the document',
});
```

Example 3 (javascript):
```javascript
let creating; // A global promise to avoid concurrency issues
async function setupOffscreenDocument(path) {
  // Check all windows controlled by the service worker to see if one
  // of them is the offscreen document with the given path
  const offscreenUrl = chrome.runtime.getURL(path);
  const existingContexts = await chrome.runtime.getContexts({
    contextTypes: ['OFFSCREEN_DOCUMENT'],
    documentUrls: [offscreenUrl]
  });

  if (existingContexts.length > 0) {
    return;
  }

  // create offscreen document
  if (creating) {
    await creating;
  } else {
    creating = chrome.offscreen.createDocument({
      url: path,
      reasons: ['CLIPBOARD'],
      justification: 'reason for needing the document',
    });
    await creating;
    creating = null;
  }
}
```

Example 4 (javascript):
```javascript
chrome.action.onClicked.addListener(async () => {
  await setupOffscreenDocument('off_screen.html');

  // Send message to offscreen document
  chrome.runtime.sendMessage({
    type: '...',
    target: 'offscreen',
    data: '...'
  });
});
```

---

## chrome.types 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/types?hl=zh-cn

**Contents:**
- chrome.types 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- Chrome 浏览器设置
  - 范围和生命周期
  - 优先级
- 类型
  - ChromeSetting
    - 属性
  - ChromeSettingScope
    - 枚举

chrome.types API 包含 Chrome 的类型声明。

ChromeSetting 类型提供了一组通用函数（get()、set() 和 clear()），以及 Chrome 浏览器设置的事件发布者 (onChange)。代理设置示例演示了这些函数的预期使用方式。

Chrome 会区分三种不同的浏览器设置范围：

Chrome 会在不同层级管理设置。以下列表按优先级升序介绍了可能会影响有效设置的层。

正如列表所示，政策可能会取代您通过扩展程序指定的任何更改。您可以使用 get() 函数来确定扩展程序是否能够提供设置，或者此设置是否会被覆盖。

如前所述，Chrome 允许为常规窗口和无痕式窗口使用不同的设置。以下示例说明了此行为。假设没有政策会替换这些设置，并且扩展程序可以为常规窗口 (R) 设置设置，也可以为无痕式窗口 (I) 设置设置。

如果有两个或更多扩展程序想要将同一设置设为不同的值，则最近安装的扩展程序优先于其他扩展程序。如果最近安装的扩展程序仅设置了 (I)，则常规窗口的设置可以由之前安装的扩展程序定义。

设置的有效值是指根据优先规则得出的值。它由 Chrome 使用。

允许访问 Chrome 浏览器设置的界面。相关示例请参见 accessibilityFeatures。

Event<functionvoidvoid>

onChange.addListener 函数如下所示：

更改后的值是否仅适用于无痕式浏览会话。 仅当用户在无痕模式下启用了扩展程序时，此属性才会存在。

ChromeSettingScope 可选

是否返回适用于无痕会话的值（默认值为 false）。

ChromeSettingScope 可选

相应设置的值。 请注意，每项设置都有特定的值类型，该类型会与设置一起说明。扩展程序不应设置其他类型的值。

ChromeSetting 的范围。以下权限之一：

"incognito_persistent"

"incognito_session_only"

"controlled_by_other_extensions"

"controllable_by_this_extension"

"controlled_by_this_extension"

**Examples:**

Example 1 (javascript):
```javascript
(callback: function) => {...}
```

Example 2 (javascript):
```javascript
(details: object) => void
```

Example 3 (javascript):
```javascript
(details: object) => {...}
```

Example 4 (javascript):
```javascript
(details: object) => {...}
```

---

## chrome.instanceID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/instanceID

**Contents:**
- chrome.instanceID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 方法
  - deleteID()
    - 返回
  - deleteToken()
    - 参数
    - 返回

使用 chrome.instanceID 访问实例 ID 服务。

重置应用实例标识符并撤消与其关联的所有令牌。

检索生成 InstanceID 的时间。创建时间将由 callback 返回。

检索应用实例的标识符。实例 ID 将由 callback 返回。只要应用身份未被撤消或过期，就会返回相同的 ID。

返回一个令牌，允许经过授权的实体访问由范围定义的服务。

标识有权访问与此实例 ID 关联的资源的实体。可以是 Google 开发者控制台中的项目 ID。

允许包含少量将与令牌关联的字符串键值对，这些键值对可用于处理请求。

标识授权实体可以执行的授权操作。例如，对于发送 GCM 消息，应使用 GCM 范围。

**Examples:**

Example 1 (unknown):
```unknown
chrome.instanceID.deleteID(): Promise<void>
```

Example 2 (unknown):
```unknown
chrome.instanceID.deleteToken(  deleteTokenParams: object,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.instanceID.getCreationTime(): Promise<number>
```

Example 4 (unknown):
```unknown
chrome.instanceID.getID(): Promise<string>
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

Example 2 (javascript):
```javascript
const canvas = new OffscreenCanvas(16, 16);
const context = canvas.getContext('2d');
context.clearRect(0, 0, 16, 16);
context.fillStyle = '#00FF00';  // Green
context.fillRect(0, 0, 16, 16);
const imageData = context.getImageData(0, 0, 16, 16);
chrome.action.setIcon({imageData: imageData}, () => { /* ... */ });
```

Example 3 (javascript):
```javascript
chrome.action.setBadgeBackgroundColor(
  {color: [0, 255, 0, 0]},  // Green
  () => { /* ... */ },
);

chrome.action.setBadgeBackgroundColor(
  {color: '#00FF00'},  // Also green
  () => { /* ... */ },
);

chrome.action.setBadgeBackgroundColor(
  {color: 'green'},  // Also, also green
  () => { /* ... */ },
);
```

Example 4 (javascript):
```javascript
function getTabId() { /* ... */}
function getTabBadge() { /* ... */}

chrome.action.setBadgeText(
  {
    text: getTabBadge(tabId),
    tabId: getTabId(),
  },
  () => { ... }
);
```

---

## chrome.printing 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/printing?hl=zh-cn

**Contents:**
- chrome.printing 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 示例
  - cancelJob()
  - getPrinters() and getPrinterInfo()
  - submitJob()
  - 卷筒纸打印
- 类型

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

所有 chrome.printing 方法和事件都需要您在扩展程序清单中声明 "printing" 权限。例如：

以下示例演示了如何使用打印命名空间中的每种方法。此代码是从 extensions-samples GitHub 代码库中的 api-samples/printing 复制或基于该代码编写的。

此示例使用 onJobStatusChanged 处理程序在 jobStatus 既不是 PENDING 也不是 IN_PROGRESS 时隐藏“取消”按钮。请注意，在某些网络上或当 Chromebook 直接连接到打印机时，这些状态可能会过快地传递，以至于取消按钮无法显示足够长的时间来供用户调用。这是一个经过大幅简化的打印示例。

这些函数仅使用一个示例，因为获取打印机信息需要打印机 ID，而打印机 ID 是通过调用 getPrinters() 检索到的。此示例会将默认打印机的名称和说明记录到控制台。这是简化版的打印示例。

submitJob() 方法需要满足以下三个条件。

调用 submitJob() 会触发一个对话框，要求用户确认是否要打印。使用 PrintingAPIExtensionsAllowlist 可绕过确认。

这是简化版的打印示例。请注意，ticket 附加到 SubmitJobRequest 结构（第 8 行），并且要打印的数据会转换为 blob（第 10 行）。在示例中，获取打印机 ID（第 1 行）比此处所示的要复杂得多。

此示例展示了如何为连续（或卷筒）打印构建打印票证，这通常用于收据打印。卷筒纸打印的 submitJobRequest 对象与 submitJob() 示例中所示的对象相同。

如果您需要更改纸张切割的默认值，请使用 vendor_ticket_item 键。（默认值因打印机而异。）如需更改值，请提供一个包含一个成员的数组：一个 id 为 'finishings' 的对象。该值可以是 'trim'（对于在打印结束时切割卷筒纸的打印机）或 'none'（对于需要撕下打印作业的打印机）。

部分打印机不支持 "finishings" 选项。如需确定打印机是否支持此功能，请调用 getPrinterInfo() 并查找值为 "finishings/11" 的 "display_name"。

工单的 media_size 键中的值因打印机而异。如需选择合适的大小，请调用 getPrinterInfo()。返回的 GetPrinterResponse 包含 "media_size"."option" 处支持的媒体尺寸数组。选择 "is_continuous_feed" 值为 true 的选项。使用其高度和宽度值作为票券的高度和宽度值。

CDD 格式的打印机功能。该属性可能缺失。

“PENDING” Chrome 接收到打印作业，但尚未处理。

“IN_PROGRESS” 打印作业已发送以供打印。

“CANCELED” 打印作业已被用户或通过 API 取消。

"PRINTED" 打印作业已打印，未出现任何错误。

打印机的标识符；保证在设备上的打印机中是唯一的。

用于显示打印机是否符合 DefaultPrinterSelection 规则的标志。请注意，可能会有多个打印机被标记。

显示最近一次使用打印机通过 Chrome 进行打印的时间。值越低，表示打印机最近一次使用的时间越近。最小值为 0。如果缺少值，则表示打印机最近未使用过。此值保证在打印机之间是唯一的。

打印机 URI。扩展程序可以使用此属性为用户选择打印机。

"DOOR_OPEN" 打印机的机盖未关好。打印机仍接受打印作业。

“TRAY_MISSING” 打印机的托盘缺失。打印机仍接受打印作业。

“OUT_OF_INK” 打印机墨尽。打印机仍接受打印作业。

“OUT_OF_PAPER” 打印机缺纸。打印机仍接受打印作业。

“OUTPUT_FULL” 打印机的出纸区域（例如出纸盘）已满。打印机仍接受打印作业。

“PAPER_JAM” 打印机卡纸。打印机仍接受打印作业。

“GENERIC_ISSUE” 某些一般性问题。打印机仍接受打印作业。

“已停止” 打印机已停止，无法打印，但仍可接受打印作业。

“UNREACHABLE” 打印机无法连接，且不接受打印作业。

“EXPIRED_CERTIFICATE” SSL 证书已过期。打印机接受作业，但作业失败。

要提交的打印作业。支持的内容类型为“application/pdf”和“image/png”。云作业票证不应包含 FitToPageTicketItem、PageRangeTicketItem 和 ReverseOrderTicketItem 字段，因为这些字段与本机打印无关。VendorTicketItem 为可选项。必须提供所有其他字段。

已创建的打印作业的 ID。这是设备上所有打印作业的唯一标识符。如果状态不是“OK”，jobId 将为 null。

“USER_REJECTED” 发送的打印作业请求被用户拒绝。

每分钟可调用 getPrinterInfo 的次数上限。

每分钟可调用 submitJob 的次数上限。

要取消的打印作业的 ID。此值应与在 SubmitJobResponse 中收到的 ID 相同。

返回打印作业的状态。如果具有指定 jobId 的打印作业不存在，此调用将失败并显示运行时错误。jobId：要返回状态的打印作业的 ID。此值应与在 SubmitJobResponse 中收到的 ID 相同。

以 CDD 格式返回打印机的状态和功能。如果没有安装具有指定 ID 的打印机，此调用将失败并显示运行时错误。

Promise<GetPrinterInfoResponse>

返回设备上可用打印机的列表。包括手动添加的打印机、企业打印机和发现的打印机。

提交打印作业。如果扩展程序未列在 PrintingAPIExtensionsAllowlist 政策中，系统会提示用户接受打印作业。 在 Chrome 120 之前，此函数不返回 promise。

Promise<SubmitJobResponse>

当作业的状态发生变化时触发的事件。仅针对此扩展程序创建的作业触发此事件。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "printing"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.printing.onJobStatusChanged.addListener((jobId, status) => {
  const cancelButton = document.getElementById("cancelButton");
  cancelButton.addEventListener('click', () => {
    chrome.printing.cancelJob(jobId).then((response) => {
      if (response !== undefined) {
        console.log(response.status);
      }
      if (chrome.runtime.lastError !== undefined) {
        console.log(chrome.runtime.lastError.message);
      }
    });
  });
  if (status !== "PENDING" && status !== "IN_PROGRESS") {
    cancelButton.style.visibility = 'hidden';
  } else {
    cancelButton.style.visibility = 'visible';
  }
}
```

Example 3 (javascript):
```javascript
​​const printers = await chrome.printing.getPrinters();
const defaultPrinter = printers.find((printer) => {
  const printerInfo = await chrome.printing.getPrinterInfo(printer.id);
  return printerInfo.isDefault;
}
console.log(`Default printer: ${defaultPrinter.name}.\n\t${defaultPrinter.description}`);
```

Example 4 (javascript):
```javascript
const defaultPrinter = getDefaultPrinter();
const ticket = getPrinterTicket(defaultPrinter);
const arrayBuffer = getPrintData();
const submitJobRequest = {
  job: {
    printerId: defaultPrinter,
    title: 'test job',
    ticket: ticket,
    contentType: 'application/pdf',
    document: new Blob([new Uint8Array(arrayBuffer)], {
      type: 'application/pdf'
    });
  }
};

chrome.printing.submitJob(submitJobRequest, (response) => {
  if (response !== undefined) {
    console.log(response.status);
  }
  if (chrome.runtime.lastError !== undefined) {
    console.log(chrome.runtime.lastError.message);
  }
});
```

---

## chrome.sidePanel 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/sidePanel

**Contents:**
- chrome.sidePanel 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和使用
  - 使用场景
    - 在每个网站上显示相同的侧边栏
    - 在特定网站上启用侧边栏
    - 点击工具栏图标，打开侧边栏
    - 以程序化方式在用户互动时打开侧边栏

使用 chrome.sidePanel API 在浏览器的侧边栏中托管内容，与网页的主要内容并排显示。

如需使用 Side Panel API，请在扩展程序清单文件中添加 "sidePanel" 权限：

借助侧边栏 API，扩展程序可以在侧边栏中显示自己的界面，从而提供持久的体验，以补充用户的浏览历程。

以下部分展示了 Side Panel API 的一些常见用例。如需查看完整的扩展程序示例，请参阅扩展程序示例。

侧边栏最初可以从清单的 "side_panel" 键中的 "default_path" 属性进行设置，以便在每个网站上显示相同的侧边栏。此路径应指向扩展程序目录中的相对路径。

扩展程序可以使用 sidepanel.setOptions() 在特定标签页上启用侧边栏。此示例使用 chrome.tabs.onUpdated() 监听对标签页所做的任何更新。它会检查网址是否为 www.google.com，并启用侧边栏。否则，系统会停用该功能。

当用户暂时切换到未启用侧边栏的标签页时，侧边栏会隐藏。当用户切换到之前打开过该标签页的标签页时，该标签页会自动重新显示。

当用户前往未启用侧边栏的网站时，侧边栏会关闭，并且扩展程序不会显示在侧边栏下拉菜单中。

如需查看完整示例，请参阅特定于标签页的侧边栏示例。

开发者可以使用 sidePanel.setPanelBehavior() 让用户在点击操作工具栏图标时打开侧边栏。首先，在清单中声明 "action" 键：

Chrome 116 引入了 sidePanel.open()。它允许扩展程序通过扩展程序用户手势（例如点击操作图标）打开侧边栏。或者用户在扩展程序页面或内容脚本上的互动，例如点击按钮。如需查看完整演示，请参阅打开侧边栏示例扩展程序。

以下代码展示了如何在用户点击上下文菜单时在当前窗口中打开全局侧边栏。使用 sidePanel.open() 时，您必须选择应在哪个上下文中打开它。使用 windowId 打开全局侧边栏。或者，您也可以将 tabId 设置为仅在特定标签页中打开侧边栏。

扩展程序可以使用 sidepanel.getOptions() 检索当前的侧边栏。以下示例在 runtime.onInstalled() 上设置了欢迎侧边栏。然后，当用户导航到其他标签页时，该标签页会被替换为主侧边栏。

用户将首先看到 Chrome 的内置侧边栏。每个侧边栏都会在侧边栏菜单中显示扩展程序的图标。如果未添加任何图标，系统会显示一个占位符图标，其中包含扩展程序名称的首字母。

如需允许用户打开侧边栏，请将操作图标与 sidePanel.setPanelBehavior() 结合使用。或者，在用户互动后调用 sidePanel.open()，例如：

当侧边栏处于打开状态时，侧边栏工具栏会显示一个图钉图标。 点击该图标可固定扩展程序的操作图标。点击固定后的操作图标将执行操作图标的默认操作，并且只有在明确配置的情况下才会打开侧边栏。

如需查看更多侧边栏 API 扩展演示，请探索以下任一扩展：

要关闭侧边栏的标签页。如果指定标签页中打开了标签页专用的侧边栏，系统会关闭该侧边栏。必须提供此参数或 windowId 中的至少一个。

用于关闭侧边栏的窗口。如果指定窗口中打开了全局侧边栏，则对于该窗口中未激活任何标签页专用面板的所有标签页，系统都会关闭该全局侧边栏。必须提供此参数或 tabId 中的至少一个。

如果指定，则返回指定标签页的侧边栏选项。否则，返回默认的侧边栏选项（用于没有任何特定设置的任何标签页）。

用于打开侧边栏的标签页。如果相应标签页具有特定于该标签页的侧边栏，则该侧边栏仅会针对该标签页打开。如果没有特定于标签页的面板，则全局面板将在指定标签页以及当前未打开任何特定于标签页的面板的其他标签页中打开。此操作会替换相应标签页中当前处于活动状态的任何侧边栏（全局或标签页专用）。必须提供此参数或 windowId 中的至少一个。

用于打开侧边栏的窗口。仅当扩展程序具有全局（非标签页专用）侧边栏或还指定了 tabId 时，此属性才适用。此方法将替换用户在指定窗口中打开的任何当前有效的全局侧边栏。必须提供此参数或 tabId 中的至少一个。

点击扩展程序的图标是否会切换侧边栏中扩展程序条目的显示状态。默认值为 false。

扩展程序软件包中要在面板中显示内容的本地资源的路径。

侧边栏关闭时所在的标签页的可选 ID。仅当面板是特定于标签页时提供。

侧边栏关闭时所在的窗口的 ID。此功能适用于全局面板和标签页专用面板。

扩展程序软件包中要在面板中显示内容的本地资源的路径。

打开侧边栏的标签页的可选 ID。仅当面板是特定于标签页时提供。

打开侧边栏的窗口的 ID。此功能适用于全局面板和标签页专用面板。

侧边栏是否应处于启用状态。您可以选择是否创建 PIN 码。默认值为 true。

要使用的侧边栏 HTML 文件的路径。这必须是扩展程序包中的本地资源。

如果指定，侧边栏选项将仅适用于具有此 ID 的标签页。如果省略，这些选项会设置默认行为（用于没有任何特定设置的任何标签页）。注意：如果为相应 tabId 和默认 tabId 设置了相同的路径，则相应 tabId 的面板将是与默认 tabId 的面板不同的实例。

Promise<PanelOptions>

Promise<PanelBehavior>

打开扩展程序的侧边栏。此方法只能在响应用户操作时调用。

配置扩展程序的侧边栏行为。这是一项更新插入操作。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My side panel extension",
  ...
  "permissions": [
    "sidePanel"
  ]
}
```

Example 2 (unknown):
```unknown
{
  "name": "My side panel extension",
  ...
  "side_panel": {
    "default_path": "sidepanel.html"
  }
  ...
}
```

Example 3 (unknown):
```unknown
<!DOCTYPE html>
<html>
  <head>
    <title>My Sidepanel</title>
  </head>
  <body>
    <h1>All sites sidepanel extension</h1>
    <p>This side panel is enabled on all sites</p>
  </body>
</html>
```

Example 4 (javascript):
```javascript
const GOOGLE_ORIGIN = 'https://www.google.com';

chrome.tabs.onUpdated.addListener(async (tabId, info, tab) => {
  if (!tab.url) return;
  const url = new URL(tab.url);
  // Enables the side panel on google.com
  if (url.origin === GOOGLE_ORIGIN) {
    await chrome.sidePanel.setOptions({
      tabId,
      path: 'sidepanel.html',
      enabled: true
    });
  } else {
    // Disables the side panel on all other sites
    await chrome.sidePanel.setOptions({
      tabId,
      enabled: false
    });
  }
});
```

---

## API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference

**Contents:**
- API 参考 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

大多数扩展程序都需要访问一个或多个 Chrome 扩展程序 API 才能正常运行。 此 API 参考文档介绍了可在扩展程序中使用的 API，并提供了用例示例。

使用 chrome.accessibilityFeatures API 管理 Chrome 的无障碍功能。此 API 依赖于 API 类型的 ChromeSetting 原型来获取和设置各个无障碍功能。为了获取功能状态，扩展程序必须请求 accessibilityFeatures.read 权限。如需修改功能状态，扩展程序需要 accessibilityFeatures.modify 权限。请注意，accessibilityFeatures.modify 并不意味着拥有 accessibilityFeatures.read 权限。

使用 chrome.alarms API 安排代码在指定时间或未来某个时间定期运行。

chrome.audio API 可供用户获取有关连接到系统的音频设备的信息并控制这些设备。此 API 目前仅在 ChromeOS 的自助服务终端模式下可用。

使用 chrome.bookmarks API 可创建、整理和以其他方式操作书签。另请参阅替换网页，您可以使用该功能创建自定义书签管理器页面。

使用浏览器操作将图标放置在主 Google Chrome 工具栏中的地址栏右侧。除了图标之外，浏览器操作还可以具有提示、标记和弹出式窗口。

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

chrome.debugger API 可作为 Chrome 远程调试协议的替代传输方式。使用 chrome.debugger 附加到一个或多个标签页，以检测网络互动、调试 JavaScript、更改 DOM 和 CSS 等。使用 Debuggee 属性 tabId 以 sendCommand 为目标标签页，并通过 onEvent 回调中的 tabId 路由事件。

使用 chrome.declarativeContent API 根据网页内容采取行动，而无需获得读取网页内容的权限。

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

注意：此 API 已弃用。请改用 declarativeNetRequest API。使用 chrome.declarativeWebRequest API 拦截、阻止或修改正在处理的请求。它比 chrome.webRequest API 快得多，因为您可以注册在浏览器（而非 JavaScript 引擎）中评估的规则，从而减少往返延迟时间并提高效率。

Desktop Capture API 可捕获屏幕、单个窗口或单个标签页的内容。

使用 chrome.devtools.inspectedWindow API 与检查的窗口互动：获取检查的网页的标签页 ID、在检查的窗口的上下文中评估代码、重新加载网页或获取网页中的资源列表。

使用 chrome.devtools.network API 检索开发者工具在“网络”面板中显示的网络请求的相关信息。

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

使用 chrome.devtools.performance API 监听开发者工具中“性能”面板的录制状态更新。

使用 chrome.devtools.recorder API 自定义开发者工具中的“记录器”面板。

使用 chrome.dns API 进行 DNS 解析。

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

使用 chrome.dom API 访问扩展程序的特殊 DOM API

使用 chrome.downloads API 以编程方式发起、监控、操纵和搜索下载。

使用 chrome.enterprise.deviceAttributes API 读取设备属性。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.hardwarePlatform API 获取浏览器运行的硬件平台的制造商和型号。注意：此 API 仅适用于由企业政策安装的扩展程序。

使用 chrome.enterprise.login API 退出受管理的访客会话。注意：此 API 仅适用于在 ChromeOS 受管理的访客会话中由企业政策安装的扩展程序。

使用 chrome.enterprise.networkingAttributes API 读取有关当前网络的信息。注意：此 API 仅适用于根据企业政策强制安装的扩展程序。

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

chrome.events 命名空间包含 API 在调度事件时使用的常见类型，用于在发生值得注意的事情时通知您。

chrome.extension API 具有可供任何扩展程序页面使用的实用程序。它支持在扩展程序及其内容脚本之间或在扩展程序之间交换消息，如消息传递中所述。

chrome.extensionTypes API 包含 Chrome 扩展程序的类型声明。

使用 chrome.fileBrowserHandler API 扩展 Chrome OS 文件浏览器。例如，您可以使用此 API 让用户将文件上传到您的网站。

使用 chrome.fileSystemProvider API 创建可通过 ChromeOS 上的文件管理器访问的文件系统。

使用 chrome.fontSettings API 管理 Chrome 的字体设置。

使用 chrome.gcm 可让应用和扩展程序通过 Firebase Cloud Messaging (FCM) 发送和接收消息。

使用 chrome.history API 与浏览器记录的已访问页面进行互动。您可以在浏览器的历史记录中添加、移除和查询网址。如需使用您自己的版本替换历史记录页面，请参阅替换页面。

使用 chrome.i18n 基础架构在整个应用或扩展程序中实现国际化。

使用 chrome.identity API 获取 OAuth2 访问令牌。

使用 chrome.idle API 检测机器的空闲状态何时发生变化。

使用 chrome.input.ime API 为 Chrome OS 实现自定义 IME。这样，扩展程序就可以处理按键、设置组合并管理候选字窗口。

使用 chrome.instanceID 访问实例 ID 服务。

使用 chrome.loginState API 读取和监控登录状态。

chrome.management API 提供了一些方法来管理已安装的应用和扩展程序。

使用 chrome.notifications API 通过模板创建丰富通知，并在系统托盘中向用户显示这些通知。

借助多功能框 API，您可以向 Google Chrome 的地址栏（也称为多功能框）注册关键字。

使用 chrome.pageAction API 可在主 Google Chrome 工具栏中的地址栏右侧放置图标。网页操作是指可在当前网页上执行的操作，但并非适用于所有网页。不活动时，网页操作会显示为灰色。

使用 chrome.pageCapture API 将标签页另存为 MHTML。

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

使用 chrome.platformKeys API 访问由平台管理的客户端证书。如果用户或政策授予了相应权限，扩展程序便可在其自定义身份验证协议中使用此类证书。例如，这允许在第三方 VPN 中使用平台管理的证书（请参阅 chrome.vpnProvider）。

使用 chrome.power API 可替换系统的电源管理功能。

chrome.printerProvider API 会公开打印管理器使用的事件，以便查询受扩展程序控制的打印机、查询这些打印机的功能，以及向这些打印机提交打印作业。

使用 chrome.printing API 将打印作业发送到 Chromebook 上安装的打印机。

使用 chrome.printingMetrics API 获取有关打印使用情况的数据。

使用 chrome.privacy API 来控制 Chrome 中可能会影响用户隐私的功能的使用情况。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置 Chrome 的配置。

使用 chrome.processes API 与浏览器的进程进行交互。

使用 chrome.proxy API 管理 Chrome 的代理设置。此 API 依赖于 ChromeSetting 类型的 API 原型来获取和设置代理配置。

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

使用 chrome.search API 通过默认提供程序进行搜索。

使用 chrome.sessions API 查询和恢复浏览会话中的标签页和窗口。

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

使用 system.cpu API 查询 CPU 元数据。

使用 system.display API 查询展示元数据。

chrome.system.memory API。

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

使用 chrome.systemLog API 记录来自扩展程序的 Chrome 系统日志。

使用 chrome.tabCapture API 与标签页媒体流进行互动。

使用 chrome.tabs API 与浏览器的标签页系统进行交互。您可以使用此 API 在浏览器中创建、修改和重新排列标签页。

使用 chrome.topSites API 访问新标签页上显示的顶级网站（即访问次数最多的网站）。这些快捷方式不包括用户自定义的快捷方式。

使用 chrome.tts API 播放合成的文字转语音 (TTS)。另请参阅相关的 ttsEngine API，该 API 允许扩展程序实现语音引擎。

使用 chrome.ttsEngine API 通过扩展程序实现文字转语音(TTS) 引擎。如果您的扩展程序使用此 API 进行注册，那么当任何扩展程序或 Chrome 应用使用 tts API 生成语音时，该扩展程序都会收到包含要朗读的发言内容和其他参数的事件。然后，扩展程序可以使用任何可用的 Web 技术来合成和输出语音，并将事件发送回调用函数以报告状态。

chrome.types API 包含 Chrome 的类型声明。

使用 chrome.vpnProvider API 实现 VPN 客户端。

使用 chrome.wallpaper API 更改 ChromeOS 壁纸。

使用 chrome.webNavigation API 接收有关正在处理的导航请求的状态的通知。

使用 chrome.webRequest API 观察和分析流量，并拦截、屏蔽或修改正在处理的请求。

使用 chrome.windows API 与浏览器窗口互动。您可以使用此 API 在浏览器中创建、修改和重新排列窗口。

---
