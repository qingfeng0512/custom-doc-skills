# Chrome-Extensions - Storage

**Pages:** 14

---

## chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/runtime/?hl=zh-cn

**Contents:**
- chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和使用
  - 未打包的扩展程序的行为
- 使用场景
  - 向网页添加图片
  - 将数据从内容脚本发送到服务工作线程
  - 收集有关卸载的反馈
- 示例
- 类型

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

此 API 的大多数成员都不需要任何权限。connectNative()、sendNativeMessage() 和 onNativeConnect 需要此权限。

以下示例展示了如何在清单中声明 "nativeMessaging" 权限：

运行时 API 提供了一些方法来支持扩展程序可以使用的多个领域：

当未打包的扩展程序被重新加载时，系统会将其视为更新。这意味着，系统将以 "update" 原因触发 chrome.runtime.onInstalled 事件。这包括使用 chrome.runtime.reload() 重新加载扩展程序的情况。

网页要访问托管在其他网域中的资源，必须指定该资源的完整网址（例如 <img src="https://example.com/logo.png">）。在网页上包含扩展程序资源也是如此。两者的区别在于，扩展程序的资源必须作为可供网页访问的资源公开，并且通常由内容脚本负责注入扩展程序资源。

在此示例中，扩展程序将使用 runtime.getURL() 将 logo.png 添加到内容脚本正在注入的网页，以创建完全限定的网址。但首先，必须在清单中将该素材资源声明为可通过网络访问的资源。

扩展程序的内容脚本通常需要由扩展程序的另一部分（例如服务工作器）管理的数据。与打开到同一网页的两个浏览器窗口非常相似，这两个上下文无法直接访问彼此的值。相反，扩展程序可以使用消息传递在这些不同的上下文之间进行协调。

在此示例中，内容脚本需要扩展程序的服务工作线程中的一些数据来初始化其界面。为了获取此数据，它会将开发者定义的 get-user-data 消息传递给服务工作器，然后服务工作器会返回用户信息的副本。

许多扩展程序会使用卸载后调查问卷来了解如何更好地为用户提供服务并提高用户留存率。以下示例展示了如何添加此功能。

如需查看更多 Runtime API 示例，请参阅 Manifest V3 - Web Accessible Resources 演示。

用于匹配特定扩展程序上下文的过滤条件。匹配的上下文必须与所有指定的过滤条件匹配；任何未指定的过滤条件都与所有可用的上下文匹配。因此，过滤条件 `{}` 将匹配所有可用的上下文。

“POPUP” 将上下文类型指定为扩展程序弹出式窗口

“BACKGROUND” 将上下文类型指定为服务工作线程。

“OFFSCREEN_DOCUMENT” 将上下文类型指定为离屏文档。

“SIDE_PANEL” 将上下文类型指定为侧边栏。

“DEVELOPER_TOOLS” 将上下文类型指定为开发者工具。

与此上下文相关联的文档的 UUID；如果此上下文不是托管在文档中，则为 undefined。

与相应上下文相关联的文档的来源；如果上下文未托管在文档中，则为 undefined。

与此上下文相关联的文档的网址；如果上下文未托管在文档中，则为 undefined。

相应上下文的框架 ID；如果相应上下文未托管在框架中，则为 -1。

相应上下文是否与无痕式浏览配置文件相关联。

相应上下文所处标签页的 ID；如果相应上下文未托管在标签页中，则为 -1。

相应上下文的窗口 ID；如果相应上下文未托管在窗口中，则返回 -1。

一个对象，其中包含有关发送消息或请求的脚本上下文的信息。

打开连接的文档在创建端口时的生命周期。请注意，自移植创建以来，文档的生命周期状态可能已发生变化。

打开连接的框架。0 表示顶级框架，正数表示子框架。仅当设置了 tab 时，才会设置此字段。

打开连接的网页或框架的来源。它可以不同于网址属性（例如 about:blank），也可以是不透明的（例如沙盒 iframe）。如果我们无法立即从网址中判断来源是否可信，此信息有助于我们进行判断。

打开连接的 tabs.Tab（如果有）。只有在连接是从标签页（包括内容脚本）打开时，并且只有在接收者是扩展程序而非应用时，此属性才会存在。

打开连接的网页或框架的 TLS 渠道 ID（如果扩展程序请求且可用）。

打开连接的网页或框架的网址。如果发件人位于 iframe 中，则为 iframe 的网址，而不是托管 iframe 的网页的网址。

“install” 将事件原因指定为安装。

“update” 将事件原因指定为扩展程序更新。

“chrome_update” 将事件原因指定为 Chrome 更新。

“shared_module_update” 将事件原因指定为对共享模块的更新。

调度相应事件的原因。当应用更新到较新版本时，需要重启，此时使用“app_update”。当浏览器/操作系统更新到较新版本时，需要重启，此时会使用“os_update”。当系统运行时间超过企业政策中设置的允许正常运行时间时，使用“periodic”。

“app_update” 将事件原因指定为应用更新。

“os_update” 将事件原因指定为操作系统更新。

“periodic” 将事件原因指定为应用的定期重启。

“arm64” 将处理器架构指定为 arm64。

“x86-32” 将处理器架构指定为 x86-32。

“x86-64” 将处理器架构指定为 x86-64。

“mips” 将处理器架构指定为 mips。

“mips64” 将处理器架构指定为 mips64。

“riscv64” 将处理器架构指定为 riscv64。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

“arm” 将原生客户端架构指定为 arm。

“x86-32” 将原生客户端架构指定为 x86-32。

“x86-64” 将原生客户端架构指定为 x86-64。

“mips” 将原生客户端架构指定为 mips。

“mips64” 将原生客户端架构指定为 mips64。

“win” 指定 Windows 操作系统。

“android” 指定 Android 操作系统。

“cros” 指定 Chrome 操作系统。

“linux” 指定 Linux 操作系统。

“openbsd” 指定 OpenBSD 操作系统。

一个允许与其他网页进行双向通信的对象。如需了解详情，请参阅长期连接。

端口的名称，如对 runtime.connect 的调用中所指定。

Event<functionvoidvoid>

当端口与另一端断开连接时触发。如果端口因错误而断开连接，则可能会设置 runtime.lastError。如果通过 disconnect 关闭端口，则此事件仅在另一端触发。此事件最多触发一次（另请参阅端口生命周期）。

onDisconnect.addListener 函数如下所示：

Event<functionvoidvoid>

当端口的另一端调用 postMessage 时，系统会触发此事件。

onMessage.addListener 函数如下所示：

此属性将仅存在于传递给 onConnect / onConnectExternal / onConnectNative 监听器的端口上。

立即断开端口连接。对已断开连接的端口调用 disconnect() 不会产生任何影响。当端口断开连接时，系统不会向该端口调度任何新事件。

向端口的另一端发送消息。如果端口已断开连接，则会抛出错误。

要发送的消息。此对象应可转换为 JSON。

“throttled” 指定状态检查已受到限制。这种情况可能会在短时间内反复检查后发生。

“no_update” 指定没有可安装的更新。

“update_available” 指定有可安装的更新。

如果调用 API 函数失败，则填充错误消息；否则为未定义。此变量仅在该函数的回调范围内定义。如果产生错误，但在回调中未访问 runtime.lastError，系统会将一条消息记录到控制台，其中列出了产生错误的 API 函数。返回 Promise 的 API 函数不会设置此属性。

尝试连接扩展程序（例如后台网页）或其他扩展程序/应用中的监听器。这对于连接到扩展程序进程的内容脚本、应用/扩展程序间通信和网页消息传递非常有用。请注意，这不会连接到内容脚本中的任何监听器。扩展程序可以通过 tabs.connect 连接到嵌入在标签页中的内容脚本。

要连接的扩展服务的 ID。如果省略，系统将尝试与您自己的扩展程序建立连接。如果从网页发送消息以进行网页消息传递，则为必需。

是否将 TLS 渠道 ID 传递到 onConnectExternal 中，以供监听连接事件的进程使用。

将传递到正在监听连接事件的进程的 onConnect 中。

可用于发送和接收消息的端口。如果扩展程序不存在，则会触发端口的 onDisconnect 事件。

连接到宿主机中的原生应用。此方法需要 "nativeMessaging" 权限。如需了解详情，请参阅原生消息传递。

检索当前扩展程序/应用内运行的后台网页的 JavaScript“window”对象。如果后台网页是事件网页，系统将确保在调用回调之前加载该网页。如果没有后台网页，则会设置错误。

Promise<Window | undefined>

获取与此扩展程序关联的有效上下文的相关信息

用于查找匹配上下文的过滤条件。如果上下文与过滤条件中的所有指定字段都匹配，则视为匹配。过滤器中任何未指定的字段都与所有上下文匹配。

Promise<ExtensionContext[]>

从清单中返回有关应用或扩展程序的详细信息。返回的对象是完整清单文件的序列化。

返回软件包目录的 DirectoryEntry。

Promise<DirectoryEntry>

Promise<PlatformInfo>

将应用/扩展程序安装目录中的相对路径转换为完全限定网址。

应用/扩展程序中相对于其安装目录的资源路径。

具体行为可能取决于清单的 options_ui 或 options_page 键，或者 Chrome 在当时支持的内容。例如，该网页可能会在新的标签页中、chrome://extensions 中、应用内打开，或者只是聚焦于已打开的选项页面。它永远不会导致调用者页面重新加载。

如果您的扩展程序未声明选项页面，或者 Chrome 因其他原因而未能创建选项页面，则回调将设置 lastError。

重新加载应用或扩展程序。自助服务终端模式不支持此方法。对于自助服务终端模式，请使用 chrome.runtime.restart() 方法。

重要提示：大多数扩展程序/应用都不应使用此方法，因为 Chrome 已经每隔几个小时自动检查一次，并且您可以监听 runtime.onUpdateAvailable 事件，而无需调用 requestUpdateCheck。

此方法仅在极少数情况下适合调用，例如，如果您的扩展程序与后端服务通信，并且后端服务已确定客户端扩展程序版本非常过时，而您想提示用户进行更新，则适合调用此方法。requestUpdateCheck 的大多数其他用途（例如，基于重复计时器无条件调用它）可能只会浪费客户端、网络和服务器资源。

注意：如果使用回调调用此函数，此函数不会返回对象，而是将这两个属性作为单独的实参传递给回调。

当应用在自助服务终端模式下运行时，重新启动 ChromeOS 设备。否则，不执行任何操作。

当应用在自助服务终端模式下运行达到指定秒数后，重新启动 ChromeOS 设备。如果在时间结束之前再次调用，则重新启动将延迟。如果使用值 -1 调用，则会取消重新启动。在非自助服务终端模式下，此方法不执行任何操作。只有第一个调用此 API 的扩展程序可以重复调用此 API。

重新启动设备前等待的时间（以秒为单位），或使用 -1 取消预定的重新启动。

向扩展程序内或不同扩展程序/应用中的事件监听器发送一条消息。与 runtime.connect 类似，但仅发送一条消息，并可选择性地发送响应。如果发送到您的扩展程序，则 runtime.onMessage 事件将在扩展程序的每个帧（发送者的帧除外）中触发，如果是其他扩展程序，则为 runtime.onMessageExternal。请注意，扩展程序无法使用此方法向内容脚本发送消息。如需向内容脚本发送消息，请使用 tabs.sendMessage。

要向其发送消息的扩展程序的 ID。如果省略，消息将发送到您自己的扩展程序/应用。如果从网页发送消息以进行网页消息传递，则必须提供此参数。

要发送的消息。此消息应为可 JSON 化的对象。

是否将 TLS 渠道 ID 传递到正在监听连接事件的进程的 onMessageExternal 中。

向原生应用发送单条消息。此方法需要 "nativeMessaging" 权限。

设置卸载时要访问的网址。这可用于清理服务器端数据、进行分析和实施调查。最多 1023 个字符。

扩展程序卸载后要打开的网址。此网址必须采用 http: 或 https: 协议。设置为空字符串，以便在卸载时不打开新标签页。

请使用 runtime.onRestartRequired。

当有 Chrome 更新可用但未立即安装时触发，因为需要重新启动浏览器。

当从扩展程序进程或内容脚本（通过 runtime.connect）建立连接时触发。

当从其他扩展程序（通过 runtime.connect）或从可外部连接的网站建立连接时触发。

当从原生应用建立连接时触发。此活动需要 "nativeMessaging" 权限。仅在 ChromeOS 上受支持。

在首次安装扩展程序、将扩展程序更新到新版本以及将 Chrome 更新到新版本时触发。

指明已更新的导入的共享模块扩展广告的 ID。仅当“reason”为“shared_module_update”时，此字段才会存在。

表示刚刚更新的扩展程序的先前版本。仅当“reason”为“update”时，此字段才会存在。

当消息从扩展程序进程（通过 runtime.sendMessage）或内容脚本（通过 tabs.sendMessage）发送时触发。

sendResponse 参数的格式如下：

当消息通过 runtime.sendMessage 从其他扩展程序发送时触发。无法在内容脚本中使用。

sendResponse 参数的格式如下：

当应用或运行该应用的设备需要重启时触发。应用应在最早的方便时间关闭其所有窗口，以便进行重启。如果应用未执行任何操作，则在 24 小时的宽限期过后，系统将强制执行重启。目前，此事件仅针对 Chrome OS 自助服务终端应用触发。

OnRestartRequiredReason

当安装了此扩展程序的个人资料首次启动时触发。即使此扩展程序在“分离式”无痕模式下运行，当无痕配置文件启动时，也不会触发此事件。

在事件网页卸载之前发送到该网页。这样，扩展程序便有机会执行一些清理操作。请注意，由于页面正在卸载，因此在处理此事件时启动的任何异步操作都无法保证完成。如果事件网页在卸载之前有更多活动，系统会发送 onSuspendCanceled 事件，并且不会卸载该网页。

在 onSuspend 之后发送，表示应用最终不会被卸载。

当有可用更新但未立即安装（因为应用正在运行）时触发。如果您不执行任何操作，系统会在下次卸载后台网页时安装更新；如果您希望尽快安装更新，可以明确调用 chrome.runtime.reload()。如果您的扩展程序使用的是持久性后台网页，那么后台网页当然永远不会被卸载，因此除非您手动调用 chrome.runtime.reload() 来响应此事件，否则系统不会安装更新，直到下次 Chrome 本身重启时才会安装。如果没有处理脚本在监听此事件，并且您的扩展程序具有持久性后台页面，则其行为就像是调用了 chrome.runtime.reload() 来响应此事件。

当与同一扩展程序关联的用户脚本发送消息时触发。

sendResponse 参数的格式如下：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "nativeMessaging"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "logo.png" ],
      "matches": [ "https://*/*" ]
    }
  ],
  ...
}
```

Example 3 (javascript):
```javascript
{ // Block used to avoid setting global variables
  const img = document.createElement('img');
  img.src = chrome.runtime.getURL('logo.png');
  document.body.append(img);
}
```

Example 4 (javascript):
```javascript
// 1. Send a message to the service worker requesting the user's data
chrome.runtime.sendMessage('get-user-data', (response) => {
  // 3. Got an asynchronous response with the data from the service worker
  console.log('received user data', response);
  initializeUI(response);
});
```

---

## chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/downloads

**Contents:**
- chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
- 示例
- 类型
  - BooleanDelta
    - 属性
  - DangerType
    - 枚举

使用 chrome.downloads API 以编程方式启动、监控、操纵和搜索下载。

您必须在扩展程序清单中声明 "downloads" 权限，才能使用此 API。

您可以在 examples/api/downloads 目录中找到使用 chrome.downloads API 的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

“content” 下载的文件已知为恶意文件。

“不常见” 相应下载内容的网址不常被下载，可能具有危险性。

“主机” 下载内容来自已知会分发恶意二进制文件的主机，可能存在危险。

“垃圾” 下载内容可能是垃圾内容或不安全。例如，它可能会更改浏览器或计算机设置。

“安全” 下载不会对用户的计算机造成已知危险。

“allowlistedByPolicy” 与企业相关的值。

"asyncLocalPasswordScanning"

"sensitiveContentWarning"

"sensitiveContentBlock"

"deepScannedOpenedDangerous"

"promptForLocalPasswordScanning"

“forceSaveToGdrive” 供安全企业浏览器扩展程序使用。在需要时，Chrome 会阻止下载到磁盘，并将文件直接下载到 Google 云端硬盘。

发生变化的 DownloadItem 的 id。

如果相应下载是由扩展程序发起的，则为发起相应下载的扩展程序的标识符。一经设置便无法更改。

如果此下载是由扩展程序发起的，则为发起此下载的扩展程序的本地化名称。如果扩展程序更改其名称或用户更改其语言区域，则可能会发生变化。

如果下载正在进行且已暂停，或者下载已中断且可以从中断处恢复，则为 true。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.endTime) console.log(new Date(item.endTime))})})

下载中断的原因。多种 HTTP 错误可能会归为以 SERVER_ 开头的某个错误。与网络相关的错误以 NETWORK_ 开头，与将文件写入文件系统的过程相关的错误以 FILE_ 开头，用户发起的中断以 USER_ 开头。

下载预计完成时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.estimatedEndTime) console.log(new Date(item.estimatedEndTime))})})

下载的文件是否仍然存在。由于 Chrome 不会自动监控文件移除情况，因此此信息可能已过时。调用 search() 以触发文件存在性检查。当存在性检查完成时，如果文件已被删除，则会触发 onChanged 事件。请注意，search() 不会等待存在性检查完成才返回，因此 search() 的结果可能无法准确反映文件系统。此外，search() 可以根据需要经常调用，但检查文件是否存在的时间间隔不会短于 10 秒。

整个文件解压缩后的字节数，如果未知，则为 -1。

如果相应下载记录在历史记录中，则为 False；如果未记录，则为 True。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

下载开始时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){console.log(new Date(item.startTime))})})

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

发起相应下载的绝对网址（在任何重定向之前）。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

相对于“下载”目录的文件路径，用于包含下载的文件，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径会导致错误。onDeterminingFilename 允许在确定文件的 MIME 类型和临时文件名后建议文件名。

HeaderNameValuePair[] 可选

如果网址使用 HTTP[s] 协议，则要随请求发送的额外 HTTP 标头。每个标头都表示为一个字典，其中包含键 name 和 value 或 binaryValue，且仅限于 XMLHttpRequest 允许的标头。

如果网址使用 HTTP[S] 协议，则要使用的 HTTP 方法。

使用文件选择器允许用户选择文件名，无论 filename 是否已设置或已存在。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后结束的 DownloadItem（采用 ISO 8601 格式）

将结果限制为在指定毫秒数之前结束的 DownloadItem（采用 ISO 8601 格式）。

整个文件解压缩后的字节数，如果未知，则为 -1。

将结果限制为 DownloadItem，其中 filename 与给定的正则表达式匹配。

将结果限制为 DownloadItem，其中 finalUrl 与给定的正则表达式匹配。

要查询的 DownloadItem 的 id。

返回的匹配 DownloadItem 的数量上限。默认值为 1000。设置为 0 可返回所有匹配的 DownloadItem。如需了解如何将结果分页，请参阅 search。

将此数组的元素设置为 DownloadItem 属性，以便对搜索结果进行排序。例如，设置 orderBy=['startTime'] 会按开始时间升序对 DownloadItem 进行排序。如需指定降序，请在前面加上连字符：“-startTime”。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

此搜索字词数组会将结果限制为 DownloadItem，其 filename 或 url 或 finalUrl 包含所有不以短划线“-”开头的搜索字词，但不包含任何以短划线开头的搜索字词。

下载开始时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后开始的 DownloadItem（采用 ISO 8601 格式）。

将结果限制为在指定毫秒数之前开始的 DownloadItem（采用 ISO 8601 格式）。

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

将结果限制为 totalBytes 大于指定整数的 DownloadItem。

将结果限制为 totalBytes 小于指定整数的 DownloadItem。

发起相应下载的绝对网址（在任何重定向之前）。

将结果限制为 DownloadItem，其中 url 与给定的正则表达式匹配。

为避免重复，系统会更改 filename，在文件扩展名前面添加计数器。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

DownloadItem 的新目标 DownloadItem.filename，作为相对于用户默认下载目录的路径，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径将被忽略。如果有任何扩展程序注册了 onDeterminingFilename 监听器，系统会忽略 filename。

返回的图标的大小。图标将为正方形，尺寸为 size * size 像素。图标的默认尺寸和最大尺寸均为 32x32 像素。唯一支持的大小是 16 和 32。指定任何其他大小都是错误的。

"FILE_VIRUS_INFECTED"

"FILE_TRANSIENT_ERROR"

"FILE_SECURITY_CHECK_FAILED"

"FILE_SAME_AS_SOURCE"

"NETWORK_DISCONNECTED"

"NETWORK_SERVER_DOWN"

"NETWORK_INVALID_REQUEST"

"SERVER_UNAUTHORIZED"

"SERVER_CERT_PROBLEM"

"SERVER_CONTENT_LENGTH_MISMATCH"

"SERVER_CROSS_ORIGIN_REDIRECT"

发生了错误，导致与文件托管服务的连接中断。

提示用户接受危险下载。只能从可见的上下文（标签页、窗口或页面/浏览器操作弹出式窗口）中调用。不会自动接受危险的下载内容。如果接受下载，系统会触发 onChanged 事件，否则不会发生任何情况。当所有数据都提取到临时文件中，并且下载不危险或危险已被接受时，临时文件会被重命名为目标文件名，state 更改为“complete”，并触发 onChanged。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

取消下载。当 callback 运行时，下载已取消、完成、中断或不再存在。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

下载网址。如果网址使用 HTTP[S] 协议，则请求将包含当前为其主机名设置的所有 Cookie。如果同时指定了 filename 和 saveAs，系统将显示“另存为”对话框，并预先填充指定的 filename。如果下载成功开始，系统将使用新的 DownloadItem 的 downloadId 调用 callback。如果启动下载时出错，系统将使用 downloadId=undefined 调用 callback，并且 runtime.lastError 将包含描述性字符串。我们不保证错误字符串在不同版本之间保持向后兼容。扩展程序不得解析该属性。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

从历史记录中清除匹配的 DownloadItem，而不删除已下载的文件。对于与 query 匹配的每个 DownloadItem，系统都会触发 onErased 事件，然后调用 callback。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检索指定下载的图标。对于新下载的文件，在收到 onCreated 事件后，系统会显示文件图标。在下载进行期间，此函数返回的图片可能与下载完成后返回的图片不同。图标检索是通过查询底层操作系统或工具包（具体取决于平台）完成的。因此，返回的图标将取决于多种因素，包括下载状态、平台、注册的文件类型和视觉主题。如果无法确定文件图标，runtime.lastError 将包含一条错误消息。

GetFileIconOptions 可选

Promise<string | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

如果 DownloadItem 完成，则立即打开下载的文件；否则通过 runtime.lastError 返回错误。此方法除了需要 "downloads" 权限之外，还需要 "downloads.open" 权限。当商品首次打开时，系统会触发 onChanged 事件。此方法只能在响应用户手势时调用。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

暂停下载。如果请求成功，下载将处于暂停状态。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

如果下载的文件存在且 DownloadItem 已完成，则移除下载的文件；否则通过 runtime.lastError 返回错误。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

恢复已暂停的下载。如果请求成功，则下载正在进行且未暂停。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

查找 DownloadItem。将 query 设置为空对象，以获取所有 DownloadItem。如需获取特定的 DownloadItem，请仅设置 id 字段。如需翻阅大量商品，请设置 orderBy: ['-startTime']，将 limit 设置为每页的商品数量，并将 startedAfter 设置为上一页中最后一项的 startTime。

Promise<DownloadItem[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

启用或停用与当前浏览器个人资料关联的每个窗口底部的灰色搁架。只要至少有一个扩展程序停用了搁架，搁架就会处于停用状态。如果至少有一个其他扩展程序已停用功能架，则启用功能架会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.shelf" 权限。

更改与当前浏览器个人资料关联的每个窗口的下载界面。只要至少有一个扩展程序将 UiOptions.enabled 设置为 false，下载界面就会隐藏。如果将 UiOptions.enabled 设置为 true，但至少有一个其他扩展程序已将其停用，则会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.ui" 权限。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

在文件管理器中，在相应文件夹中显示下载的文件。

当 DownloadItem 的任何属性（bytesReceived 和 estimatedEndTime 除外）发生更改时，系统会触发此事件，并提供 downloadId 和一个包含已更改属性的对象。

此事件会在下载开始时触发，并附带 DownloadItem 对象。

在确定文件名的过程中，扩展程序将有机会替换目标 DownloadItem.filename。每个扩展程序不得为此事件注册多个监听器。每个监听器都必须同步或异步调用 suggest 一次。如果监听器异步调用 suggest，则必须返回 true。如果监听器既不同步调用 suggest，也不返回 true，则系统会自动调用 suggest。在所有监听器都调用 suggest 之前，DownloadItem 不会完成。监听器可以调用不带任何实参的 suggest，以允许下载使用 downloadItem.filename 作为其文件名，也可以将 suggestion 对象传递给 suggest 以替换目标文件名。如果多个扩展程序替换了文件名，则最后一个安装的扩展程序（其监听器将 suggestion 对象传递给 suggest）胜出。为避免混淆哪个扩展程序会胜出，用户不应安装可能会发生冲突的扩展程序。如果下载是由 download 发起的，并且在确定 MIME 类型和临时文件名之前已知目标文件名，请改为将 filename 传递给 download。

FilenameSuggestion（可选）

当下载从历史记录中清除时，会触发并附带 downloadId。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "downloads"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
chrome.downloads.acceptDanger(  downloadId: number,  callback?: function,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.downloads.cancel(  downloadId: number,  callback?: function,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.downloads.download(  options: DownloadOptions,  callback?: function,): Promise<number>
```

---

## chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/storage?hl=zh-cn

**Contents:**
- chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 扩展程序可以使用 Web 存储 API 吗？
  - 存储区域
  - 存储空间和限流限制
- 使用场景
  - 响应存储空间更新
  - 从存储空间异步预加载

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

如需使用存储 API，请在扩展程序清单中声明 "storage" 权限。例如：

Storage API 提供了一种特定于扩展程序的方式来持久保留用户数据和状态。它类似于 Web 平台的存储 API（IndexedDB 和 Storage），但旨在满足扩展程序的存储需求。以下是一些关键功能：

虽然扩展程序可以在某些上下文（弹出式窗口和其他 HTML 页面）中使用 Storage 接口（可从 window.localStorage 访问），但我们不建议这样做，原因如下：

如需从服务工作线程将数据从 Web 存储 API 移至扩展程序存储 API，请执行以下操作：

此外，Web 存储 API 在扩展程序中的工作方式也存在一些细微差别。如需了解详情，请参阅存储和 Cookie 一文。

Storage API 具有以下用量限制：

如需详细了解存储区域限制以及超出限制后会出现什么情况，请参阅 sync、local 和 session 的配额信息。

以下各部分展示了 Storage API 的常见用例。

如需跟踪对存储空间所做的更改，请向其 onChanged 事件添加监听器。当存储空间中的任何内容发生变化时，系统都会触发该事件。示例代码会监听以下更改：

我们可以进一步拓展这个想法。在此示例中，我们有一个选项页面，可让用户切换“调试模式”（此处未显示实现）。选项页面会立即将新设置保存到 storage.sync，并且服务工作线程会使用 storage.onChanged 尽快应用该设置。

由于服务工作线程并非始终处于运行状态，因此 Manifest V3 扩展程序有时需要先从存储空间异步加载数据，然后才能执行其事件处理程序。为此，以下代码段使用异步 action.onClicked 事件处理程序，该处理程序会等待 storageCache 全局变量填充完毕，然后再执行其逻辑。

您可以在开发者工具中查看和修改使用该 API 存储的数据。如需了解详情，请参阅开发者工具文档中的查看和修改扩展程序存储空间页面。

以下示例展示了 local、sync 和 session 存储区：

如需查看存储 API 的其他演示，请探索以下任一示例：

“TRUSTED_CONTEXTS” 指定源自扩展程序本身的上下文。

"TRUSTED_AND_UNTRUSTED_CONTEXTS" 指定来自扩展程序外部的上下文。

Event<functionvoidvoid>

onChanged.addListener 函数如下所示：

要获取的单个键、要获取的键列表，或指定默认值的字典（请参阅对象说明）。空列表或空对象将返回空结果对象。传入 null 可获取存储空间的全部内容。

获取一个或多个内容所用的空间量（以字节为单位）。

getBytesInUse 函数如下所示：

单个键或键列表，用于获取总使用量。如果列表为空，则返回 0。传入 null 可获取所有存储空间的总用量。

一个对象，用于提供要更新存储空间的每个键值对。存储空间中的任何其他键值对都不会受到影响。

数字等原始值将按预期序列化。具有 typeof "object" 和 "function" 的值通常会序列化为 {}，但 Array（按预期序列化）、Date 和 Regex 除外（使用其 String 表示形式进行序列化）。

为存储区设置所需的访问权限级别。默认情况下，session 存储空间仅限受信任的上下文（扩展程序页面和服务工作器）访问，而 managed、local 和 sync 存储空间允许受信任和不受信任的上下文访问。

setAccessLevel 函数如下所示：

local 存储区中的内容是每个机器本地的。

可存储在本地存储空间中的数据量上限（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果扩展程序具有 unlimitedStorage 权限，系统将忽略此值。如果更新会导致超出此限制，则会立即失败，并在使用回调时设置 runtime.lastError，或者在使用 async/await 时设置被拒绝的 Promise。

managed 存储区域中的项由网域管理员配置的企业政策设置，并且对扩展程序是只读的；尝试修改此命名空间会导致错误。如需了解如何配置政策，请参阅存储区域的清单。

session 存储区域中的内容项存储在内存中，不会持久保存到磁盘。

可存储在内存中的最大数据量（以字节为单位），通过估算每个值和键的动态分配内存用量来衡量。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

sync 存储区域中的内容会使用 Chrome 同步功能进行同步。

同步存储空间中可存储的最大项数。如果更新会导致超出此限制，则更新会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

storage.sync API 不再具有持续写入操作配额。

每小时可执行的 set、remove 或 clear 操作数上限。此限制为每 2 秒 1 次，低于短期内每分钟较高的写入次数限制。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

每分钟可执行的 set、remove 或 clear 操作次数上限。即每秒 2 次，在较短的时间内提供比每小时写入次数更高的吞吐量。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中可存储的最大数据总量（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中每个单独项的最大大小（以字节为单位），计算方式为相应值的 JSON 字符串化长度加上键长度。如果更新包含的项大于此限制，则会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "storage"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.storage.onChanged.addListener((changes, namespace) => {
  for (let [key, { oldValue, newValue }] of Object.entries(changes)) {
    console.log(
      `Storage key "${key}" in namespace "${namespace}" changed.`,
      `Old value was "${oldValue}", new value is &quot;${newValue}".`
    );
  }
});
```

Example 3 (unknown):
```unknown
<!-- type="module" allows you to use top leve>l< await --
script defer src="options.js><" >t<ype="module">;/s<cript
form id=&qu>ot;op<tionsForm"
  label for="debug">
    input type="che<ckbox&>q<uot; >name="debug" id="debug"
    Enable debug mode
  /label
/form
```

Example 4 (javascript):
```javascript
// In-page cache of the user's options
const options = {};
const optionsForm = document.getElementById("optionsForm");

// Immediately persist options changes
optionsForm.debug.addEventListener(">;change", (event) = {
  options.debug = event.target.checked;
  chrome.storage.sync.set({ options });
});

// Initialize the form with the user's option settings
const data = await chrome.storage.sync.get("options");
Object.assign(options, data.options);
optionsForm.debug.checked = Boolean(options.debug);
```

---

## chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/runtime?hl=zh-cn

**Contents:**
- chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和使用
  - 未打包的扩展程序的行为
- 使用场景
  - 向网页添加图片
  - 将数据从内容脚本发送到服务工作线程
  - 收集有关卸载的反馈
- 示例
- 类型

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

此 API 的大多数成员都不需要任何权限。connectNative()、sendNativeMessage() 和 onNativeConnect 需要此权限。

以下示例展示了如何在清单中声明 "nativeMessaging" 权限：

运行时 API 提供了一些方法来支持扩展程序可以使用的多个领域：

当未打包的扩展程序被重新加载时，系统会将其视为更新。这意味着，系统将以 "update" 原因触发 chrome.runtime.onInstalled 事件。这包括使用 chrome.runtime.reload() 重新加载扩展程序的情况。

网页要访问托管在其他网域中的资源，必须指定该资源的完整网址（例如 <img src="https://example.com/logo.png">）。在网页上包含扩展程序资源也是如此。两者的区别在于，扩展程序的资源必须作为可供网页访问的资源公开，并且通常由内容脚本负责注入扩展程序资源。

在此示例中，扩展程序将使用 runtime.getURL() 将 logo.png 添加到内容脚本正在注入的网页，以创建完全限定的网址。但首先，必须在清单中将该素材资源声明为可通过网络访问的资源。

扩展程序的内容脚本通常需要由扩展程序的另一部分（例如服务工作器）管理的数据。与打开到同一网页的两个浏览器窗口非常相似，这两个上下文无法直接访问彼此的值。相反，扩展程序可以使用消息传递在这些不同的上下文之间进行协调。

在此示例中，内容脚本需要扩展程序的服务工作线程中的一些数据来初始化其界面。为了获取此数据，它会将开发者定义的 get-user-data 消息传递给服务工作器，然后服务工作器会返回用户信息的副本。

许多扩展程序会使用卸载后调查问卷来了解如何更好地为用户提供服务并提高用户留存率。以下示例展示了如何添加此功能。

如需查看更多 Runtime API 示例，请参阅 Manifest V3 - Web Accessible Resources 演示。

用于匹配特定扩展程序上下文的过滤条件。匹配的上下文必须与所有指定的过滤条件匹配；任何未指定的过滤条件都与所有可用的上下文匹配。因此，过滤条件 `{}` 将匹配所有可用的上下文。

“POPUP” 将上下文类型指定为扩展程序弹出式窗口

“BACKGROUND” 将上下文类型指定为服务工作线程。

“OFFSCREEN_DOCUMENT” 将上下文类型指定为离屏文档。

“SIDE_PANEL” 将上下文类型指定为侧边栏。

“DEVELOPER_TOOLS” 将上下文类型指定为开发者工具。

与此上下文相关联的文档的 UUID；如果此上下文不是托管在文档中，则为 undefined。

与相应上下文相关联的文档的来源；如果上下文未托管在文档中，则为 undefined。

与此上下文相关联的文档的网址；如果上下文未托管在文档中，则为 undefined。

相应上下文的框架 ID；如果相应上下文未托管在框架中，则为 -1。

相应上下文是否与无痕式浏览配置文件相关联。

相应上下文所处标签页的 ID；如果相应上下文未托管在标签页中，则为 -1。

相应上下文的窗口 ID；如果相应上下文未托管在窗口中，则返回 -1。

一个对象，其中包含有关发送消息或请求的脚本上下文的信息。

打开连接的文档在创建端口时的生命周期。请注意，自移植创建以来，文档的生命周期状态可能已发生变化。

打开连接的框架。0 表示顶级框架，正数表示子框架。仅当设置了 tab 时，才会设置此字段。

打开连接的网页或框架的来源。它可以不同于网址属性（例如 about:blank），也可以是不透明的（例如沙盒 iframe）。如果我们无法立即从网址中判断来源是否可信，此信息有助于我们进行判断。

打开连接的 tabs.Tab（如果有）。只有在连接是从标签页（包括内容脚本）打开时，并且只有在接收者是扩展程序而非应用时，此属性才会存在。

打开连接的网页或框架的 TLS 渠道 ID（如果扩展程序请求且可用）。

打开连接的网页或框架的网址。如果发件人位于 iframe 中，则为 iframe 的网址，而不是托管 iframe 的网页的网址。

“install” 将事件原因指定为安装。

“update” 将事件原因指定为扩展程序更新。

“chrome_update” 将事件原因指定为 Chrome 更新。

“shared_module_update” 将事件原因指定为对共享模块的更新。

调度相应事件的原因。当应用更新到较新版本时，需要重启，此时使用“app_update”。当浏览器/操作系统更新到较新版本时，需要重启，此时会使用“os_update”。当系统运行时间超过企业政策中设置的允许正常运行时间时，使用“periodic”。

“app_update” 将事件原因指定为应用更新。

“os_update” 将事件原因指定为操作系统更新。

“periodic” 将事件原因指定为应用的定期重启。

“arm64” 将处理器架构指定为 arm64。

“x86-32” 将处理器架构指定为 x86-32。

“x86-64” 将处理器架构指定为 x86-64。

“mips” 将处理器架构指定为 mips。

“mips64” 将处理器架构指定为 mips64。

“riscv64” 将处理器架构指定为 riscv64。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

“arm” 将原生客户端架构指定为 arm。

“x86-32” 将原生客户端架构指定为 x86-32。

“x86-64” 将原生客户端架构指定为 x86-64。

“mips” 将原生客户端架构指定为 mips。

“mips64” 将原生客户端架构指定为 mips64。

“win” 指定 Windows 操作系统。

“android” 指定 Android 操作系统。

“cros” 指定 Chrome 操作系统。

“linux” 指定 Linux 操作系统。

“openbsd” 指定 OpenBSD 操作系统。

一个允许与其他网页进行双向通信的对象。如需了解详情，请参阅长期连接。

端口的名称，如对 runtime.connect 的调用中所指定。

Event<functionvoidvoid>

当端口与另一端断开连接时触发。如果端口因错误而断开连接，则可能会设置 runtime.lastError。如果通过 disconnect 关闭端口，则此事件仅在另一端触发。此事件最多触发一次（另请参阅端口生命周期）。

onDisconnect.addListener 函数如下所示：

Event<functionvoidvoid>

当端口的另一端调用 postMessage 时，系统会触发此事件。

onMessage.addListener 函数如下所示：

此属性将仅存在于传递给 onConnect / onConnectExternal / onConnectNative 监听器的端口上。

立即断开端口连接。对已断开连接的端口调用 disconnect() 不会产生任何影响。当端口断开连接时，系统不会向该端口调度任何新事件。

向端口的另一端发送消息。如果端口已断开连接，则会抛出错误。

要发送的消息。此对象应可转换为 JSON。

“throttled” 指定状态检查已受到限制。这种情况可能会在短时间内反复检查后发生。

“no_update” 指定没有可安装的更新。

“update_available” 指定有可安装的更新。

如果调用 API 函数失败，则填充错误消息；否则为未定义。此变量仅在该函数的回调范围内定义。如果产生错误，但在回调中未访问 runtime.lastError，系统会将一条消息记录到控制台，其中列出了产生错误的 API 函数。返回 Promise 的 API 函数不会设置此属性。

尝试连接扩展程序（例如后台网页）或其他扩展程序/应用中的监听器。这对于连接到扩展程序进程的内容脚本、应用/扩展程序间通信和网页消息传递非常有用。请注意，这不会连接到内容脚本中的任何监听器。扩展程序可以通过 tabs.connect 连接到嵌入在标签页中的内容脚本。

要连接的扩展服务的 ID。如果省略，系统将尝试与您自己的扩展程序建立连接。如果从网页发送消息以进行网页消息传递，则为必需。

是否将 TLS 渠道 ID 传递到 onConnectExternal 中，以供监听连接事件的进程使用。

将传递到正在监听连接事件的进程的 onConnect 中。

可用于发送和接收消息的端口。如果扩展程序不存在，则会触发端口的 onDisconnect 事件。

连接到宿主机中的原生应用。此方法需要 "nativeMessaging" 权限。如需了解详情，请参阅原生消息传递。

检索当前扩展程序/应用内运行的后台网页的 JavaScript“window”对象。如果后台网页是事件网页，系统将确保在调用回调之前加载该网页。如果没有后台网页，则会设置错误。

Promise<Window | undefined>

获取与此扩展程序关联的有效上下文的相关信息

用于查找匹配上下文的过滤条件。如果上下文与过滤条件中的所有指定字段都匹配，则视为匹配。过滤器中任何未指定的字段都与所有上下文匹配。

Promise<ExtensionContext[]>

从清单中返回有关应用或扩展程序的详细信息。返回的对象是完整清单文件的序列化。

返回软件包目录的 DirectoryEntry。

Promise<DirectoryEntry>

Promise<PlatformInfo>

将应用/扩展程序安装目录中的相对路径转换为完全限定网址。

应用/扩展程序中相对于其安装目录的资源路径。

具体行为可能取决于清单的 options_ui 或 options_page 键，或者 Chrome 在当时支持的内容。例如，该网页可能会在新的标签页中、chrome://extensions 中、应用内打开，或者只是聚焦于已打开的选项页面。它永远不会导致调用者页面重新加载。

如果您的扩展程序未声明选项页面，或者 Chrome 因其他原因而未能创建选项页面，则回调将设置 lastError。

重新加载应用或扩展程序。自助服务终端模式不支持此方法。对于自助服务终端模式，请使用 chrome.runtime.restart() 方法。

重要提示：大多数扩展程序/应用都不应使用此方法，因为 Chrome 已经每隔几个小时自动检查一次，并且您可以监听 runtime.onUpdateAvailable 事件，而无需调用 requestUpdateCheck。

此方法仅在极少数情况下适合调用，例如，如果您的扩展程序与后端服务通信，并且后端服务已确定客户端扩展程序版本非常过时，而您想提示用户进行更新，则适合调用此方法。requestUpdateCheck 的大多数其他用途（例如，基于重复计时器无条件调用它）可能只会浪费客户端、网络和服务器资源。

注意：如果使用回调调用此函数，此函数不会返回对象，而是将这两个属性作为单独的实参传递给回调。

当应用在自助服务终端模式下运行时，重新启动 ChromeOS 设备。否则，不执行任何操作。

当应用在自助服务终端模式下运行达到指定秒数后，重新启动 ChromeOS 设备。如果在时间结束之前再次调用，则重新启动将延迟。如果使用值 -1 调用，则会取消重新启动。在非自助服务终端模式下，此方法不执行任何操作。只有第一个调用此 API 的扩展程序可以重复调用此 API。

重新启动设备前等待的时间（以秒为单位），或使用 -1 取消预定的重新启动。

向扩展程序内或不同扩展程序/应用中的事件监听器发送一条消息。与 runtime.connect 类似，但仅发送一条消息，并可选择性地发送响应。如果发送到您的扩展程序，则 runtime.onMessage 事件将在扩展程序的每个帧（发送者的帧除外）中触发，如果是其他扩展程序，则为 runtime.onMessageExternal。请注意，扩展程序无法使用此方法向内容脚本发送消息。如需向内容脚本发送消息，请使用 tabs.sendMessage。

要向其发送消息的扩展程序的 ID。如果省略，消息将发送到您自己的扩展程序/应用。如果从网页发送消息以进行网页消息传递，则必须提供此参数。

要发送的消息。此消息应为可 JSON 化的对象。

是否将 TLS 渠道 ID 传递到正在监听连接事件的进程的 onMessageExternal 中。

向原生应用发送单条消息。此方法需要 "nativeMessaging" 权限。

设置卸载时要访问的网址。这可用于清理服务器端数据、进行分析和实施调查。最多 1023 个字符。

扩展程序卸载后要打开的网址。此网址必须采用 http: 或 https: 协议。设置为空字符串，以便在卸载时不打开新标签页。

请使用 runtime.onRestartRequired。

当有 Chrome 更新可用但未立即安装时触发，因为需要重新启动浏览器。

当从扩展程序进程或内容脚本（通过 runtime.connect）建立连接时触发。

当从其他扩展程序（通过 runtime.connect）或从可外部连接的网站建立连接时触发。

当从原生应用建立连接时触发。此活动需要 "nativeMessaging" 权限。仅在 ChromeOS 上受支持。

在首次安装扩展程序、将扩展程序更新到新版本以及将 Chrome 更新到新版本时触发。

指明已更新的导入的共享模块扩展广告的 ID。仅当“reason”为“shared_module_update”时，此字段才会存在。

表示刚刚更新的扩展程序的先前版本。仅当“reason”为“update”时，此字段才会存在。

当消息从扩展程序进程（通过 runtime.sendMessage）或内容脚本（通过 tabs.sendMessage）发送时触发。

sendResponse 参数的格式如下：

当消息通过 runtime.sendMessage 从其他扩展程序发送时触发。无法在内容脚本中使用。

sendResponse 参数的格式如下：

当应用或运行该应用的设备需要重启时触发。应用应在最早的方便时间关闭其所有窗口，以便进行重启。如果应用未执行任何操作，则在 24 小时的宽限期过后，系统将强制执行重启。目前，此事件仅针对 Chrome OS 自助服务终端应用触发。

OnRestartRequiredReason

当安装了此扩展程序的个人资料首次启动时触发。即使此扩展程序在“分离式”无痕模式下运行，当无痕配置文件启动时，也不会触发此事件。

在事件网页卸载之前发送到该网页。这样，扩展程序便有机会执行一些清理操作。请注意，由于页面正在卸载，因此在处理此事件时启动的任何异步操作都无法保证完成。如果事件网页在卸载之前有更多活动，系统会发送 onSuspendCanceled 事件，并且不会卸载该网页。

在 onSuspend 之后发送，表示应用最终不会被卸载。

当有可用更新但未立即安装（因为应用正在运行）时触发。如果您不执行任何操作，系统会在下次卸载后台网页时安装更新；如果您希望尽快安装更新，可以明确调用 chrome.runtime.reload()。如果您的扩展程序使用的是持久性后台网页，那么后台网页当然永远不会被卸载，因此除非您手动调用 chrome.runtime.reload() 来响应此事件，否则系统不会安装更新，直到下次 Chrome 本身重启时才会安装。如果没有处理脚本在监听此事件，并且您的扩展程序具有持久性后台页面，则其行为就像是调用了 chrome.runtime.reload() 来响应此事件。

当与同一扩展程序关联的用户脚本发送消息时触发。

sendResponse 参数的格式如下：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "nativeMessaging"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "logo.png" ],
      "matches": [ "https://*/*" ]
    }
  ],
  ...
}
```

Example 3 (javascript):
```javascript
{ // Block used to avoid setting global variables
  const img = document.createElement('img');
  img.src = chrome.runtime.getURL('logo.png');
  document.body.append(img);
}
```

Example 4 (javascript):
```javascript
// 1. Send a message to the service worker requesting the user's data
chrome.runtime.sendMessage('get-user-data', (response) => {
  // 3. Got an asynchronous response with the data from the service worker
  console.log('received user data', response);
  initializeUI(response);
});
```

---

## chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/storage

**Contents:**
- chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 扩展程序可以使用 Web 存储 API 吗？
  - 存储区域
  - 存储空间和限流限制
- 使用场景
  - 响应存储空间更新
  - 从存储空间异步预加载

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

如需使用存储 API，请在扩展程序清单中声明 "storage" 权限。例如：

Storage API 提供了一种特定于扩展程序的方式来持久保留用户数据和状态。它类似于 Web 平台的存储 API（IndexedDB 和 Storage），但旨在满足扩展程序的存储需求。以下是一些关键功能：

虽然扩展程序可以在某些上下文（弹出式窗口和其他 HTML 页面）中使用 Storage 接口（可从 window.localStorage 访问），但我们不建议这样做，原因如下：

如需从服务工作线程将数据从 Web 存储 API 移至扩展程序存储 API，请执行以下操作：

此外，Web 存储 API 在扩展程序中的工作方式也存在一些细微差别。如需了解详情，请参阅存储和 Cookie 一文。

Storage API 具有以下用量限制：

如需详细了解存储区域限制以及超出限制后会出现什么情况，请参阅 sync、local 和 session 的配额信息。

以下各部分展示了 Storage API 的常见用例。

如需跟踪对存储空间所做的更改，请向其 onChanged 事件添加监听器。当存储空间中的任何内容发生变化时，系统都会触发该事件。示例代码会监听以下更改：

我们可以进一步拓展这个想法。在此示例中，我们有一个选项页面，可让用户切换“调试模式”（此处未显示实现）。选项页面会立即将新设置保存到 storage.sync，并且服务工作线程会使用 storage.onChanged 尽快应用该设置。

由于服务工作线程并非始终处于运行状态，因此 Manifest V3 扩展程序有时需要先从存储空间异步加载数据，然后才能执行其事件处理程序。为此，以下代码段使用异步 action.onClicked 事件处理程序，该处理程序会等待 storageCache 全局变量填充完毕，然后再执行其逻辑。

您可以在开发者工具中查看和修改使用该 API 存储的数据。如需了解详情，请参阅开发者工具文档中的查看和修改扩展程序存储空间页面。

以下示例展示了 local、sync 和 session 存储区：

如需查看存储 API 的其他演示，请探索以下任一示例：

“TRUSTED_CONTEXTS” 指定源自扩展程序本身的上下文。

"TRUSTED_AND_UNTRUSTED_CONTEXTS" 指定来自扩展程序外部的上下文。

Event<functionvoidvoid>

onChanged.addListener 函数如下所示：

要获取的单个键、要获取的键列表，或指定默认值的字典（请参阅对象说明）。空列表或空对象将返回空结果对象。传入 null 可获取存储空间的全部内容。

获取一个或多个内容所用的空间量（以字节为单位）。

getBytesInUse 函数如下所示：

单个键或键列表，用于获取总使用量。如果列表为空，则返回 0。传入 null 可获取所有存储空间的总用量。

一个对象，用于提供要更新存储空间的每个键值对。存储空间中的任何其他键值对都不会受到影响。

数字等原始值将按预期序列化。具有 typeof "object" 和 "function" 的值通常会序列化为 {}，但 Array（按预期序列化）、Date 和 Regex 除外（使用其 String 表示形式进行序列化）。

为存储区设置所需的访问权限级别。默认情况下，session 存储空间仅限受信任的上下文（扩展程序页面和服务工作器）访问，而 managed、local 和 sync 存储空间允许受信任和不受信任的上下文访问。

setAccessLevel 函数如下所示：

local 存储区中的内容是每个机器本地的。

可存储在本地存储空间中的数据量上限（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果扩展程序具有 unlimitedStorage 权限，系统将忽略此值。如果更新会导致超出此限制，则会立即失败，并在使用回调时设置 runtime.lastError，或者在使用 async/await 时设置被拒绝的 Promise。

managed 存储区域中的项由网域管理员配置的企业政策设置，并且对扩展程序是只读的；尝试修改此命名空间会导致错误。如需了解如何配置政策，请参阅存储区域的清单。

session 存储区域中的内容项存储在内存中，不会持久保存到磁盘。

可存储在内存中的最大数据量（以字节为单位），通过估算每个值和键的动态分配内存用量来衡量。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

sync 存储区域中的内容会使用 Chrome 同步功能进行同步。

同步存储空间中可存储的最大项数。如果更新会导致超出此限制，则更新会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

storage.sync API 不再具有持续写入操作配额。

每小时可执行的 set、remove 或 clear 操作数上限。此限制为每 2 秒 1 次，低于短期内每分钟较高的写入次数限制。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

每分钟可执行的 set、remove 或 clear 操作次数上限。即每秒 2 次，在较短的时间内提供比每小时写入次数更高的吞吐量。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中可存储的最大数据总量（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中每个单独项的最大大小（以字节为单位），计算方式为相应值的 JSON 字符串化长度加上键长度。如果更新包含的项大于此限制，则会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "storage"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.storage.onChanged.addListener((changes, namespace) => {
  for (let [key, { oldValue, newValue }] of Object.entries(changes)) {
    console.log(
      `Storage key "${key}" in namespace "${namespace}" changed.`,
      `Old value was "${oldValue}", new value is &quot;${newValue}".`
    );
  }
});
```

Example 3 (unknown):
```unknown
<!-- type="module" allows you to use top leve>l< await --
script defer src="options.js><" >t<ype="module">;/s<cript
form id=&qu>ot;op<tionsForm"
  label for="debug">
    input type="che<ckbox&>q<uot; >name="debug" id="debug"
    Enable debug mode
  /label
/form
```

Example 4 (javascript):
```javascript
// In-page cache of the user's options
const options = {};
const optionsForm = document.getElementById("optionsForm");

// Immediately persist options changes
optionsForm.debug.addEventListener(">;change", (event) = {
  options.debug = event.target.checked;
  chrome.storage.sync.set({ options });
});

// Initialize the form with the user's option settings
const data = await chrome.storage.sync.get("options");
Object.assign(options, data.options);
optionsForm.debug.checked = Boolean(options.debug);
```

---

## 存储空间和 Cookie 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/storage-and-cookies

**Contents:**
- 存储空间和 Cookie 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 存储
  - 持久性
  - Service Worker 中的访问权限
  - 分区
- Cookie
  - 安全 Cookie
  - 分区和 SameSite 行为

扩展程序可以像常规网站一样存储 Cookie 和访问网络存储 API。但在某些情况下，它们在扩展程序中的行为有所不同。

如需了解该扩展程序 API，请参阅 chrome.storage。

通常情况下，开发者建议您在扩展程序中使用网络平台存储 API。本部分探讨这些 API 在扩展程序上下文中的行为，这些行为有时可能会因其在网页上的行为方式而异。

当用户清除浏览数据时，扩展程序存储空间不会被清除。 这适用于使用 Web 存储 API（例如本地存储空间和 IndexedDB）存储的所有数据。

默认情况下，扩展程序受常规的存储空间配额限制，您可以调用 navigator.storage.estimate() 进行检查。在内存紧张时，也可能会逐出存储，不过这种情况很少见。为避免发生这种情况，请执行以下操作：

扩展程序存储空间可供扩展程序的所有来源共享，包括扩展程序 Service Worker、所有扩展程序页面（包括弹出式窗口和侧边栏）和屏幕外文档。在内容脚本中，调用 Web Storage API 会访问注入了内容脚本的主机页面（而不是扩展程序）中的数据。

可以在 Service Worker 中访问 IndexedDB 和 Cache Storage API。但本地存储和会话存储不适用。

如果您需要通过 Service Worker 访问本地存储空间或会话存储空间，请使用屏幕外文档。

分区是为存储的数据引入键的地方，以限制可以访问这些数据的位置。一直以来，存储都由源进行键控。

从 Chrome 115 开始，存储分区引入了对分区键的定义方式的更改，以防止某些类型的跨网站跟踪。也就是说，如果网站 A 嵌入了包含网站 B 的 iframe，网站 B 将无法访问直接导航到网站 B 时通常具有的存储空间。

为减轻这种扩展程序在延期中造成的影响，需遵循以下两种豁免规则：

Cookie 提供了一种存储与特定网域和路径相关联的键值对的方法。扩展程序在扩展程序方面的价值有限，但如果您有特定用例或捆绑了第三方脚本来使用扩展程序，了解它们的行为会很有帮助。

只有 https:// 方案支持 Secure Cookie 属性。因此，chrome-extension:// 网页无法使用此属性设置 Cookie。

这也意味着，扩展程序页面无法使用需要 Secure 属性的其他 Cookie 属性：

在 chrome-extension:// 页面上设置的 Cookie 始终使用 SameSite=Lax。 因此，扩展程序在其自身来源上设置的 Cookie 永远无法在框架中访问，并且分区也无关紧要。

对于与第三方网站关联的 Cookie（例如，对于在扩展程序页面上的框架中加载的第三方网站，或者从扩展程序页面向第三方来源发出的请求），Cookie 的行为与网站相同，但存在以下两个方面：

请注意，第三方 Cookie 的相关设置受 Privacy Sandbox 工作的影响，并根据其时间表进行调整。

chrome.cookies API 可让您控制要与每种 API 方法搭配使用的分区键。如需了解详情，请参阅 API 参考文档。

---

## chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/runtime?hl=zh-cn

**Contents:**
- chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和使用
  - 未打包的扩展程序的行为
- 使用场景
  - 向网页添加图片
  - 将数据从内容脚本发送到服务工作线程
  - 收集有关卸载的反馈
- 示例
- 类型

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

此 API 的大多数成员都不需要任何权限。connectNative()、sendNativeMessage() 和 onNativeConnect 需要此权限。

以下示例展示了如何在清单中声明 "nativeMessaging" 权限：

运行时 API 提供了一些方法来支持扩展程序可以使用的多个领域：

当未打包的扩展程序被重新加载时，系统会将其视为更新。这意味着，系统将以 "update" 原因触发 chrome.runtime.onInstalled 事件。这包括使用 chrome.runtime.reload() 重新加载扩展程序的情况。

网页要访问托管在其他网域中的资源，必须指定该资源的完整网址（例如 <img src="https://example.com/logo.png">）。在网页上包含扩展程序资源也是如此。两者的区别在于，扩展程序的资源必须作为可供网页访问的资源公开，并且通常由内容脚本负责注入扩展程序资源。

在此示例中，扩展程序将使用 runtime.getURL() 将 logo.png 添加到内容脚本正在注入的网页，以创建完全限定的网址。但首先，必须在清单中将该素材资源声明为可通过网络访问的资源。

扩展程序的内容脚本通常需要由扩展程序的另一部分（例如服务工作器）管理的数据。与打开到同一网页的两个浏览器窗口非常相似，这两个上下文无法直接访问彼此的值。相反，扩展程序可以使用消息传递在这些不同的上下文之间进行协调。

在此示例中，内容脚本需要扩展程序的服务工作线程中的一些数据来初始化其界面。为了获取此数据，它会将开发者定义的 get-user-data 消息传递给服务工作器，然后服务工作器会返回用户信息的副本。

许多扩展程序会使用卸载后调查问卷来了解如何更好地为用户提供服务并提高用户留存率。以下示例展示了如何添加此功能。

如需查看更多 Runtime API 示例，请参阅 Manifest V3 - Web Accessible Resources 演示。

用于匹配特定扩展程序上下文的过滤条件。匹配的上下文必须与所有指定的过滤条件匹配；任何未指定的过滤条件都与所有可用的上下文匹配。因此，过滤条件 `{}` 将匹配所有可用的上下文。

“POPUP” 将上下文类型指定为扩展程序弹出式窗口

“BACKGROUND” 将上下文类型指定为服务工作线程。

“OFFSCREEN_DOCUMENT” 将上下文类型指定为离屏文档。

“SIDE_PANEL” 将上下文类型指定为侧边栏。

“DEVELOPER_TOOLS” 将上下文类型指定为开发者工具。

与此上下文相关联的文档的 UUID；如果此上下文不是托管在文档中，则为 undefined。

与相应上下文相关联的文档的来源；如果上下文未托管在文档中，则为 undefined。

与此上下文相关联的文档的网址；如果上下文未托管在文档中，则为 undefined。

相应上下文的框架 ID；如果相应上下文未托管在框架中，则为 -1。

相应上下文是否与无痕式浏览配置文件相关联。

相应上下文所处标签页的 ID；如果相应上下文未托管在标签页中，则为 -1。

相应上下文的窗口 ID；如果相应上下文未托管在窗口中，则返回 -1。

一个对象，其中包含有关发送消息或请求的脚本上下文的信息。

打开连接的文档在创建端口时的生命周期。请注意，自移植创建以来，文档的生命周期状态可能已发生变化。

打开连接的框架。0 表示顶级框架，正数表示子框架。仅当设置了 tab 时，才会设置此字段。

打开连接的网页或框架的来源。它可以不同于网址属性（例如 about:blank），也可以是不透明的（例如沙盒 iframe）。如果我们无法立即从网址中判断来源是否可信，此信息有助于我们进行判断。

打开连接的 tabs.Tab（如果有）。只有在连接是从标签页（包括内容脚本）打开时，并且只有在接收者是扩展程序而非应用时，此属性才会存在。

打开连接的网页或框架的 TLS 渠道 ID（如果扩展程序请求且可用）。

打开连接的网页或框架的网址。如果发件人位于 iframe 中，则为 iframe 的网址，而不是托管 iframe 的网页的网址。

“install” 将事件原因指定为安装。

“update” 将事件原因指定为扩展程序更新。

“chrome_update” 将事件原因指定为 Chrome 更新。

“shared_module_update” 将事件原因指定为对共享模块的更新。

调度相应事件的原因。当应用更新到较新版本时，需要重启，此时使用“app_update”。当浏览器/操作系统更新到较新版本时，需要重启，此时会使用“os_update”。当系统运行时间超过企业政策中设置的允许正常运行时间时，使用“periodic”。

“app_update” 将事件原因指定为应用更新。

“os_update” 将事件原因指定为操作系统更新。

“periodic” 将事件原因指定为应用的定期重启。

“arm64” 将处理器架构指定为 arm64。

“x86-32” 将处理器架构指定为 x86-32。

“x86-64” 将处理器架构指定为 x86-64。

“mips” 将处理器架构指定为 mips。

“mips64” 将处理器架构指定为 mips64。

“riscv64” 将处理器架构指定为 riscv64。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

“arm” 将原生客户端架构指定为 arm。

“x86-32” 将原生客户端架构指定为 x86-32。

“x86-64” 将原生客户端架构指定为 x86-64。

“mips” 将原生客户端架构指定为 mips。

“mips64” 将原生客户端架构指定为 mips64。

“win” 指定 Windows 操作系统。

“android” 指定 Android 操作系统。

“cros” 指定 Chrome 操作系统。

“linux” 指定 Linux 操作系统。

“openbsd” 指定 OpenBSD 操作系统。

一个允许与其他网页进行双向通信的对象。如需了解详情，请参阅长期连接。

端口的名称，如对 runtime.connect 的调用中所指定。

Event<functionvoidvoid>

当端口与另一端断开连接时触发。如果端口因错误而断开连接，则可能会设置 runtime.lastError。如果通过 disconnect 关闭端口，则此事件仅在另一端触发。此事件最多触发一次（另请参阅端口生命周期）。

onDisconnect.addListener 函数如下所示：

Event<functionvoidvoid>

当端口的另一端调用 postMessage 时，系统会触发此事件。

onMessage.addListener 函数如下所示：

此属性将仅存在于传递给 onConnect / onConnectExternal / onConnectNative 监听器的端口上。

立即断开端口连接。对已断开连接的端口调用 disconnect() 不会产生任何影响。当端口断开连接时，系统不会向该端口调度任何新事件。

向端口的另一端发送消息。如果端口已断开连接，则会抛出错误。

要发送的消息。此对象应可转换为 JSON。

“throttled” 指定状态检查已受到限制。这种情况可能会在短时间内反复检查后发生。

“no_update” 指定没有可安装的更新。

“update_available” 指定有可安装的更新。

如果调用 API 函数失败，则填充错误消息；否则为未定义。此变量仅在该函数的回调范围内定义。如果产生错误，但在回调中未访问 runtime.lastError，系统会将一条消息记录到控制台，其中列出了产生错误的 API 函数。返回 Promise 的 API 函数不会设置此属性。

尝试连接扩展程序（例如后台网页）或其他扩展程序/应用中的监听器。这对于连接到扩展程序进程的内容脚本、应用/扩展程序间通信和网页消息传递非常有用。请注意，这不会连接到内容脚本中的任何监听器。扩展程序可以通过 tabs.connect 连接到嵌入在标签页中的内容脚本。

要连接的扩展服务的 ID。如果省略，系统将尝试与您自己的扩展程序建立连接。如果从网页发送消息以进行网页消息传递，则为必需。

是否将 TLS 渠道 ID 传递到 onConnectExternal 中，以供监听连接事件的进程使用。

将传递到正在监听连接事件的进程的 onConnect 中。

可用于发送和接收消息的端口。如果扩展程序不存在，则会触发端口的 onDisconnect 事件。

连接到宿主机中的原生应用。此方法需要 "nativeMessaging" 权限。如需了解详情，请参阅原生消息传递。

检索当前扩展程序/应用内运行的后台网页的 JavaScript“window”对象。如果后台网页是事件网页，系统将确保在调用回调之前加载该网页。如果没有后台网页，则会设置错误。

Promise<Window | undefined>

获取与此扩展程序关联的有效上下文的相关信息

用于查找匹配上下文的过滤条件。如果上下文与过滤条件中的所有指定字段都匹配，则视为匹配。过滤器中任何未指定的字段都与所有上下文匹配。

Promise<ExtensionContext[]>

从清单中返回有关应用或扩展程序的详细信息。返回的对象是完整清单文件的序列化。

返回软件包目录的 DirectoryEntry。

Promise<DirectoryEntry>

Promise<PlatformInfo>

将应用/扩展程序安装目录中的相对路径转换为完全限定网址。

应用/扩展程序中相对于其安装目录的资源路径。

具体行为可能取决于清单的 options_ui 或 options_page 键，或者 Chrome 在当时支持的内容。例如，该网页可能会在新的标签页中、chrome://extensions 中、应用内打开，或者只是聚焦于已打开的选项页面。它永远不会导致调用者页面重新加载。

如果您的扩展程序未声明选项页面，或者 Chrome 因其他原因而未能创建选项页面，则回调将设置 lastError。

重新加载应用或扩展程序。自助服务终端模式不支持此方法。对于自助服务终端模式，请使用 chrome.runtime.restart() 方法。

重要提示：大多数扩展程序/应用都不应使用此方法，因为 Chrome 已经每隔几个小时自动检查一次，并且您可以监听 runtime.onUpdateAvailable 事件，而无需调用 requestUpdateCheck。

此方法仅在极少数情况下适合调用，例如，如果您的扩展程序与后端服务通信，并且后端服务已确定客户端扩展程序版本非常过时，而您想提示用户进行更新，则适合调用此方法。requestUpdateCheck 的大多数其他用途（例如，基于重复计时器无条件调用它）可能只会浪费客户端、网络和服务器资源。

注意：如果使用回调调用此函数，此函数不会返回对象，而是将这两个属性作为单独的实参传递给回调。

当应用在自助服务终端模式下运行时，重新启动 ChromeOS 设备。否则，不执行任何操作。

当应用在自助服务终端模式下运行达到指定秒数后，重新启动 ChromeOS 设备。如果在时间结束之前再次调用，则重新启动将延迟。如果使用值 -1 调用，则会取消重新启动。在非自助服务终端模式下，此方法不执行任何操作。只有第一个调用此 API 的扩展程序可以重复调用此 API。

重新启动设备前等待的时间（以秒为单位），或使用 -1 取消预定的重新启动。

向扩展程序内或不同扩展程序/应用中的事件监听器发送一条消息。与 runtime.connect 类似，但仅发送一条消息，并可选择性地发送响应。如果发送到您的扩展程序，则 runtime.onMessage 事件将在扩展程序的每个帧（发送者的帧除外）中触发，如果是其他扩展程序，则为 runtime.onMessageExternal。请注意，扩展程序无法使用此方法向内容脚本发送消息。如需向内容脚本发送消息，请使用 tabs.sendMessage。

要向其发送消息的扩展程序的 ID。如果省略，消息将发送到您自己的扩展程序/应用。如果从网页发送消息以进行网页消息传递，则必须提供此参数。

要发送的消息。此消息应为可 JSON 化的对象。

是否将 TLS 渠道 ID 传递到正在监听连接事件的进程的 onMessageExternal 中。

向原生应用发送单条消息。此方法需要 "nativeMessaging" 权限。

设置卸载时要访问的网址。这可用于清理服务器端数据、进行分析和实施调查。最多 1023 个字符。

扩展程序卸载后要打开的网址。此网址必须采用 http: 或 https: 协议。设置为空字符串，以便在卸载时不打开新标签页。

请使用 runtime.onRestartRequired。

当有 Chrome 更新可用但未立即安装时触发，因为需要重新启动浏览器。

当从扩展程序进程或内容脚本（通过 runtime.connect）建立连接时触发。

当从其他扩展程序（通过 runtime.connect）或从可外部连接的网站建立连接时触发。

当从原生应用建立连接时触发。此活动需要 "nativeMessaging" 权限。仅在 ChromeOS 上受支持。

在首次安装扩展程序、将扩展程序更新到新版本以及将 Chrome 更新到新版本时触发。

指明已更新的导入的共享模块扩展广告的 ID。仅当“reason”为“shared_module_update”时，此字段才会存在。

表示刚刚更新的扩展程序的先前版本。仅当“reason”为“update”时，此字段才会存在。

当消息从扩展程序进程（通过 runtime.sendMessage）或内容脚本（通过 tabs.sendMessage）发送时触发。

sendResponse 参数的格式如下：

当消息通过 runtime.sendMessage 从其他扩展程序发送时触发。无法在内容脚本中使用。

sendResponse 参数的格式如下：

当应用或运行该应用的设备需要重启时触发。应用应在最早的方便时间关闭其所有窗口，以便进行重启。如果应用未执行任何操作，则在 24 小时的宽限期过后，系统将强制执行重启。目前，此事件仅针对 Chrome OS 自助服务终端应用触发。

OnRestartRequiredReason

当安装了此扩展程序的个人资料首次启动时触发。即使此扩展程序在“分离式”无痕模式下运行，当无痕配置文件启动时，也不会触发此事件。

在事件网页卸载之前发送到该网页。这样，扩展程序便有机会执行一些清理操作。请注意，由于页面正在卸载，因此在处理此事件时启动的任何异步操作都无法保证完成。如果事件网页在卸载之前有更多活动，系统会发送 onSuspendCanceled 事件，并且不会卸载该网页。

在 onSuspend 之后发送，表示应用最终不会被卸载。

当有可用更新但未立即安装（因为应用正在运行）时触发。如果您不执行任何操作，系统会在下次卸载后台网页时安装更新；如果您希望尽快安装更新，可以明确调用 chrome.runtime.reload()。如果您的扩展程序使用的是持久性后台网页，那么后台网页当然永远不会被卸载，因此除非您手动调用 chrome.runtime.reload() 来响应此事件，否则系统不会安装更新，直到下次 Chrome 本身重启时才会安装。如果没有处理脚本在监听此事件，并且您的扩展程序具有持久性后台页面，则其行为就像是调用了 chrome.runtime.reload() 来响应此事件。

当与同一扩展程序关联的用户脚本发送消息时触发。

sendResponse 参数的格式如下：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "nativeMessaging"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "logo.png" ],
      "matches": [ "https://*/*" ]
    }
  ],
  ...
}
```

Example 3 (javascript):
```javascript
{ // Block used to avoid setting global variables
  const img = document.createElement('img');
  img.src = chrome.runtime.getURL('logo.png');
  document.body.append(img);
}
```

Example 4 (javascript):
```javascript
// 1. Send a message to the service worker requesting the user's data
chrome.runtime.sendMessage('get-user-data', (response) => {
  // 3. Got an asynchronous response with the data from the service worker
  console.log('received user data', response);
  initializeUI(response);
});
```

---

## chrome.system.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/storage

**Contents:**
- chrome.system.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - EjectDeviceResultCode
    - 枚举
  - StorageAvailableCapacityInfo
    - 属性
  - StorageUnitInfo
    - 属性

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

“success” 弹出命令成功执行 - 应用可以提示用户移除设备。

“in_use” 设备正被其他应用使用。弹出失败；在其他应用完成对设备的操作之前，用户不应移除设备。

"no_such_device" 没有已知的此类设备。

复制的 getAvailableCapacity 函数形参 id 的 id。

唯一标识存储设备的临时 ID。此 ID 在单个应用的同一运行期间将保持不变。它不会成为应用的不同运行之间或不同应用之间的持久性标识符。

“固定” 存储介质固定，例如硬盘或 SSD。

“可移除” 存储设备可移除，例如 U 盘。

Promise<EjectDeviceResultCode>

获取指定 id 存储设备的可用容量。id 是 StorageUnitInfo 中的临时设备 ID。

Promise<StorageAvailableCapacityInfo>

从系统获取存储空间信息。传递给回调的实参是一个 StorageUnitInfo 对象数组。

Promise<StorageUnitInfo[]>

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.storage.ejectDevice(  id: string,): Promise<EjectDeviceResultCode>
```

Example 2 (unknown):
```unknown
chrome.system.storage.getAvailableCapacity(  id: string,): Promise<StorageAvailableCapacityInfo>
```

Example 3 (unknown):
```unknown
chrome.system.storage.getInfo(): Promise<StorageUnitInfo[]>
```

Example 4 (unknown):
```unknown
chrome.system.storage.onAttached.addListener(  callback: function,)
```

---

## chrome.system.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/system/storage?hl=zh-cn

**Contents:**
- chrome.system.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - EjectDeviceResultCode
    - 枚举
  - StorageAvailableCapacityInfo
    - 属性
  - StorageUnitInfo
    - 属性

使用 chrome.system.storage API 查询存储设备信息，并在可移除存储设备连接和断开连接时收到通知。

“success” 弹出命令成功执行 - 应用可以提示用户移除设备。

“in_use” 设备正被其他应用使用。弹出失败；在其他应用完成对设备的操作之前，用户不应移除设备。

"no_such_device" 没有已知的此类设备。

复制的 getAvailableCapacity 函数形参 id 的 id。

唯一标识存储设备的临时 ID。此 ID 在单个应用的同一运行期间将保持不变。它不会成为应用的不同运行之间或不同应用之间的持久性标识符。

“固定” 存储介质固定，例如硬盘或 SSD。

“可移除” 存储设备可移除，例如 U 盘。

Promise<EjectDeviceResultCode>

获取指定 id 存储设备的可用容量。id 是 StorageUnitInfo 中的临时设备 ID。

Promise<StorageAvailableCapacityInfo>

从系统获取存储空间信息。传递给回调的实参是一个 StorageUnitInfo 对象数组。

Promise<StorageUnitInfo[]>

**Examples:**

Example 1 (unknown):
```unknown
chrome.system.storage.ejectDevice(  id: string,): Promise<EjectDeviceResultCode>
```

Example 2 (unknown):
```unknown
chrome.system.storage.getAvailableCapacity(  id: string,): Promise<StorageAvailableCapacityInfo>
```

Example 3 (unknown):
```unknown
chrome.system.storage.getInfo(): Promise<StorageUnitInfo[]>
```

Example 4 (unknown):
```unknown
chrome.system.storage.onAttached.addListener(  callback: function,)
```

---

## chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/runtime

**Contents:**
- chrome.runtime 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和使用
  - 未打包的扩展程序的行为
- 使用场景
  - 向网页添加图片
  - 将数据从内容脚本发送到服务工作线程
  - 收集有关卸载的反馈
- 示例
- 类型

使用 chrome.runtime API 可检索服务工作线程、返回清单的相关详细信息，以及监听和响应扩展程序生命周期中的事件。您还可以使用此 API 将网址的相对路径转换为完全限定网址。

此 API 的大多数成员都不需要任何权限。connectNative()、sendNativeMessage() 和 onNativeConnect 需要此权限。

以下示例展示了如何在清单中声明 "nativeMessaging" 权限：

运行时 API 提供了一些方法来支持扩展程序可以使用的多个领域：

当未打包的扩展程序被重新加载时，系统会将其视为更新。这意味着，系统将以 "update" 原因触发 chrome.runtime.onInstalled 事件。这包括使用 chrome.runtime.reload() 重新加载扩展程序的情况。

网页要访问托管在其他网域中的资源，必须指定该资源的完整网址（例如 <img src="https://example.com/logo.png">）。在网页上包含扩展程序资源也是如此。两者的区别在于，扩展程序的资源必须作为可供网页访问的资源公开，并且通常由内容脚本负责注入扩展程序资源。

在此示例中，扩展程序将使用 runtime.getURL() 将 logo.png 添加到内容脚本正在注入的网页，以创建完全限定的网址。但首先，必须在清单中将该素材资源声明为可通过网络访问的资源。

扩展程序的内容脚本通常需要由扩展程序的另一部分（例如服务工作器）管理的数据。与打开到同一网页的两个浏览器窗口非常相似，这两个上下文无法直接访问彼此的值。相反，扩展程序可以使用消息传递在这些不同的上下文之间进行协调。

在此示例中，内容脚本需要扩展程序的服务工作线程中的一些数据来初始化其界面。为了获取此数据，它会将开发者定义的 get-user-data 消息传递给服务工作器，然后服务工作器会返回用户信息的副本。

许多扩展程序会使用卸载后调查问卷来了解如何更好地为用户提供服务并提高用户留存率。以下示例展示了如何添加此功能。

如需查看更多 Runtime API 示例，请参阅 Manifest V3 - Web Accessible Resources 演示。

用于匹配特定扩展程序上下文的过滤条件。匹配的上下文必须与所有指定的过滤条件匹配；任何未指定的过滤条件都与所有可用的上下文匹配。因此，过滤条件 `{}` 将匹配所有可用的上下文。

“POPUP” 将上下文类型指定为扩展程序弹出式窗口

“BACKGROUND” 将上下文类型指定为服务工作线程。

“OFFSCREEN_DOCUMENT” 将上下文类型指定为离屏文档。

“SIDE_PANEL” 将上下文类型指定为侧边栏。

“DEVELOPER_TOOLS” 将上下文类型指定为开发者工具。

与此上下文相关联的文档的 UUID；如果此上下文不是托管在文档中，则为 undefined。

与相应上下文相关联的文档的来源；如果上下文未托管在文档中，则为 undefined。

与此上下文相关联的文档的网址；如果上下文未托管在文档中，则为 undefined。

相应上下文的框架 ID；如果相应上下文未托管在框架中，则为 -1。

相应上下文是否与无痕式浏览配置文件相关联。

相应上下文所处标签页的 ID；如果相应上下文未托管在标签页中，则为 -1。

相应上下文的窗口 ID；如果相应上下文未托管在窗口中，则返回 -1。

一个对象，其中包含有关发送消息或请求的脚本上下文的信息。

打开连接的文档在创建端口时的生命周期。请注意，自移植创建以来，文档的生命周期状态可能已发生变化。

打开连接的框架。0 表示顶级框架，正数表示子框架。仅当设置了 tab 时，才会设置此字段。

打开连接的网页或框架的来源。它可以不同于网址属性（例如 about:blank），也可以是不透明的（例如沙盒 iframe）。如果我们无法立即从网址中判断来源是否可信，此信息有助于我们进行判断。

打开连接的 tabs.Tab（如果有）。只有在连接是从标签页（包括内容脚本）打开时，并且只有在接收者是扩展程序而非应用时，此属性才会存在。

打开连接的网页或框架的 TLS 渠道 ID（如果扩展程序请求且可用）。

打开连接的网页或框架的网址。如果发件人位于 iframe 中，则为 iframe 的网址，而不是托管 iframe 的网页的网址。

“install” 将事件原因指定为安装。

“update” 将事件原因指定为扩展程序更新。

“chrome_update” 将事件原因指定为 Chrome 更新。

“shared_module_update” 将事件原因指定为对共享模块的更新。

调度相应事件的原因。当应用更新到较新版本时，需要重启，此时使用“app_update”。当浏览器/操作系统更新到较新版本时，需要重启，此时会使用“os_update”。当系统运行时间超过企业政策中设置的允许正常运行时间时，使用“periodic”。

“app_update” 将事件原因指定为应用更新。

“os_update” 将事件原因指定为操作系统更新。

“periodic” 将事件原因指定为应用的定期重启。

“arm64” 将处理器架构指定为 arm64。

“x86-32” 将处理器架构指定为 x86-32。

“x86-64” 将处理器架构指定为 x86-64。

“mips” 将处理器架构指定为 mips。

“mips64” 将处理器架构指定为 mips64。

“riscv64” 将处理器架构指定为 riscv64。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

原生客户端架构。在某些平台上，此值可能与 arch 不同。

“arm” 将原生客户端架构指定为 arm。

“x86-32” 将原生客户端架构指定为 x86-32。

“x86-64” 将原生客户端架构指定为 x86-64。

“mips” 将原生客户端架构指定为 mips。

“mips64” 将原生客户端架构指定为 mips64。

“win” 指定 Windows 操作系统。

“android” 指定 Android 操作系统。

“cros” 指定 Chrome 操作系统。

“linux” 指定 Linux 操作系统。

“openbsd” 指定 OpenBSD 操作系统。

一个允许与其他网页进行双向通信的对象。如需了解详情，请参阅长期连接。

端口的名称，如对 runtime.connect 的调用中所指定。

Event<functionvoidvoid>

当端口与另一端断开连接时触发。如果端口因错误而断开连接，则可能会设置 runtime.lastError。如果通过 disconnect 关闭端口，则此事件仅在另一端触发。此事件最多触发一次（另请参阅端口生命周期）。

onDisconnect.addListener 函数如下所示：

Event<functionvoidvoid>

当端口的另一端调用 postMessage 时，系统会触发此事件。

onMessage.addListener 函数如下所示：

此属性将仅存在于传递给 onConnect / onConnectExternal / onConnectNative 监听器的端口上。

立即断开端口连接。对已断开连接的端口调用 disconnect() 不会产生任何影响。当端口断开连接时，系统不会向该端口调度任何新事件。

向端口的另一端发送消息。如果端口已断开连接，则会抛出错误。

要发送的消息。此对象应可转换为 JSON。

“throttled” 指定状态检查已受到限制。这种情况可能会在短时间内反复检查后发生。

“no_update” 指定没有可安装的更新。

“update_available” 指定有可安装的更新。

如果调用 API 函数失败，则填充错误消息；否则为未定义。此变量仅在该函数的回调范围内定义。如果产生错误，但在回调中未访问 runtime.lastError，系统会将一条消息记录到控制台，其中列出了产生错误的 API 函数。返回 Promise 的 API 函数不会设置此属性。

尝试连接扩展程序（例如后台网页）或其他扩展程序/应用中的监听器。这对于连接到扩展程序进程的内容脚本、应用/扩展程序间通信和网页消息传递非常有用。请注意，这不会连接到内容脚本中的任何监听器。扩展程序可以通过 tabs.connect 连接到嵌入在标签页中的内容脚本。

要连接的扩展服务的 ID。如果省略，系统将尝试与您自己的扩展程序建立连接。如果从网页发送消息以进行网页消息传递，则为必需。

是否将 TLS 渠道 ID 传递到 onConnectExternal 中，以供监听连接事件的进程使用。

将传递到正在监听连接事件的进程的 onConnect 中。

可用于发送和接收消息的端口。如果扩展程序不存在，则会触发端口的 onDisconnect 事件。

连接到宿主机中的原生应用。此方法需要 "nativeMessaging" 权限。如需了解详情，请参阅原生消息传递。

检索当前扩展程序/应用内运行的后台网页的 JavaScript“window”对象。如果后台网页是事件网页，系统将确保在调用回调之前加载该网页。如果没有后台网页，则会设置错误。

Promise<Window | undefined>

获取与此扩展程序关联的有效上下文的相关信息

用于查找匹配上下文的过滤条件。如果上下文与过滤条件中的所有指定字段都匹配，则视为匹配。过滤器中任何未指定的字段都与所有上下文匹配。

Promise<ExtensionContext[]>

从清单中返回有关应用或扩展程序的详细信息。返回的对象是完整清单文件的序列化。

返回软件包目录的 DirectoryEntry。

Promise<DirectoryEntry>

Promise<PlatformInfo>

将应用/扩展程序安装目录中的相对路径转换为完全限定网址。

应用/扩展程序中相对于其安装目录的资源路径。

具体行为可能取决于清单的 options_ui 或 options_page 键，或者 Chrome 在当时支持的内容。例如，该网页可能会在新的标签页中、chrome://extensions 中、应用内打开，或者只是聚焦于已打开的选项页面。它永远不会导致调用者页面重新加载。

如果您的扩展程序未声明选项页面，或者 Chrome 因其他原因而未能创建选项页面，则回调将设置 lastError。

重新加载应用或扩展程序。自助服务终端模式不支持此方法。对于自助服务终端模式，请使用 chrome.runtime.restart() 方法。

重要提示：大多数扩展程序/应用都不应使用此方法，因为 Chrome 已经每隔几个小时自动检查一次，并且您可以监听 runtime.onUpdateAvailable 事件，而无需调用 requestUpdateCheck。

此方法仅在极少数情况下适合调用，例如，如果您的扩展程序与后端服务通信，并且后端服务已确定客户端扩展程序版本非常过时，而您想提示用户进行更新，则适合调用此方法。requestUpdateCheck 的大多数其他用途（例如，基于重复计时器无条件调用它）可能只会浪费客户端、网络和服务器资源。

注意：如果使用回调调用此函数，此函数不会返回对象，而是将这两个属性作为单独的实参传递给回调。

当应用在自助服务终端模式下运行时，重新启动 ChromeOS 设备。否则，不执行任何操作。

当应用在自助服务终端模式下运行达到指定秒数后，重新启动 ChromeOS 设备。如果在时间结束之前再次调用，则重新启动将延迟。如果使用值 -1 调用，则会取消重新启动。在非自助服务终端模式下，此方法不执行任何操作。只有第一个调用此 API 的扩展程序可以重复调用此 API。

重新启动设备前等待的时间（以秒为单位），或使用 -1 取消预定的重新启动。

向扩展程序内或不同扩展程序/应用中的事件监听器发送一条消息。与 runtime.connect 类似，但仅发送一条消息，并可选择性地发送响应。如果发送到您的扩展程序，则 runtime.onMessage 事件将在扩展程序的每个帧（发送者的帧除外）中触发，如果是其他扩展程序，则为 runtime.onMessageExternal。请注意，扩展程序无法使用此方法向内容脚本发送消息。如需向内容脚本发送消息，请使用 tabs.sendMessage。

要向其发送消息的扩展程序的 ID。如果省略，消息将发送到您自己的扩展程序/应用。如果从网页发送消息以进行网页消息传递，则必须提供此参数。

要发送的消息。此消息应为可 JSON 化的对象。

是否将 TLS 渠道 ID 传递到正在监听连接事件的进程的 onMessageExternal 中。

向原生应用发送单条消息。此方法需要 "nativeMessaging" 权限。

设置卸载时要访问的网址。这可用于清理服务器端数据、进行分析和实施调查。最多 1023 个字符。

扩展程序卸载后要打开的网址。此网址必须采用 http: 或 https: 协议。设置为空字符串，以便在卸载时不打开新标签页。

请使用 runtime.onRestartRequired。

当有 Chrome 更新可用但未立即安装时触发，因为需要重新启动浏览器。

当从扩展程序进程或内容脚本（通过 runtime.connect）建立连接时触发。

当从其他扩展程序（通过 runtime.connect）或从可外部连接的网站建立连接时触发。

当从原生应用建立连接时触发。此活动需要 "nativeMessaging" 权限。仅在 ChromeOS 上受支持。

在首次安装扩展程序、将扩展程序更新到新版本以及将 Chrome 更新到新版本时触发。

指明已更新的导入的共享模块扩展广告的 ID。仅当“reason”为“shared_module_update”时，此字段才会存在。

表示刚刚更新的扩展程序的先前版本。仅当“reason”为“update”时，此字段才会存在。

当消息从扩展程序进程（通过 runtime.sendMessage）或内容脚本（通过 tabs.sendMessage）发送时触发。

sendResponse 参数的格式如下：

当消息通过 runtime.sendMessage 从其他扩展程序发送时触发。无法在内容脚本中使用。

sendResponse 参数的格式如下：

当应用或运行该应用的设备需要重启时触发。应用应在最早的方便时间关闭其所有窗口，以便进行重启。如果应用未执行任何操作，则在 24 小时的宽限期过后，系统将强制执行重启。目前，此事件仅针对 Chrome OS 自助服务终端应用触发。

OnRestartRequiredReason

当安装了此扩展程序的个人资料首次启动时触发。即使此扩展程序在“分离式”无痕模式下运行，当无痕配置文件启动时，也不会触发此事件。

在事件网页卸载之前发送到该网页。这样，扩展程序便有机会执行一些清理操作。请注意，由于页面正在卸载，因此在处理此事件时启动的任何异步操作都无法保证完成。如果事件网页在卸载之前有更多活动，系统会发送 onSuspendCanceled 事件，并且不会卸载该网页。

在 onSuspend 之后发送，表示应用最终不会被卸载。

当有可用更新但未立即安装（因为应用正在运行）时触发。如果您不执行任何操作，系统会在下次卸载后台网页时安装更新；如果您希望尽快安装更新，可以明确调用 chrome.runtime.reload()。如果您的扩展程序使用的是持久性后台网页，那么后台网页当然永远不会被卸载，因此除非您手动调用 chrome.runtime.reload() 来响应此事件，否则系统不会安装更新，直到下次 Chrome 本身重启时才会安装。如果没有处理脚本在监听此事件，并且您的扩展程序具有持久性后台页面，则其行为就像是调用了 chrome.runtime.reload() 来响应此事件。

当与同一扩展程序关联的用户脚本发送消息时触发。

sendResponse 参数的格式如下：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "nativeMessaging"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
{
  ...
  "web_accessible_resources": [
    {
      "resources": [ "logo.png" ],
      "matches": [ "https://*/*" ]
    }
  ],
  ...
}
```

Example 3 (javascript):
```javascript
{ // Block used to avoid setting global variables
  const img = document.createElement('img');
  img.src = chrome.runtime.getURL('logo.png');
  document.body.append(img);
}
```

Example 4 (javascript):
```javascript
// 1. Send a message to the service worker requesting the user's data
chrome.runtime.sendMessage('get-user-data', (response) => {
  // 3. Got an asynchronous response with the data from the service worker
  console.log('received user data', response);
  initializeUI(response);
});
```

---

## chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/downloads?hl=zh-cn

**Contents:**
- chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 示例
- 类型
  - BooleanDelta
    - 属性
  - DangerType
    - 枚举
  - DoubleDelta

使用 chrome.downloads API 以编程方式启动、监控、操纵和搜索下载。

您必须在扩展程序清单中声明 "downloads" 权限，才能使用此 API。

您可以在 examples/api/downloads 目录中找到使用 chrome.downloads API 的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

“content” 下载的文件已知为恶意文件。

“不常见” 相应下载内容的网址不常被下载，可能具有危险性。

“主机” 下载内容来自已知会分发恶意二进制文件的主机，可能存在危险。

“垃圾” 下载内容可能是垃圾内容或不安全。例如，它可能会更改浏览器或计算机设置。

“安全” 下载不会对用户的计算机造成已知危险。

“allowlistedByPolicy” 与企业相关的值。

"asyncLocalPasswordScanning"

"sensitiveContentWarning"

"sensitiveContentBlock"

"deepScannedOpenedDangerous"

"promptForLocalPasswordScanning"

“forceSaveToGdrive” 供安全企业浏览器扩展程序使用。在需要时，Chrome 会阻止下载到磁盘，并将文件直接下载到 Google 云端硬盘。

发生变化的 DownloadItem 的 id。

如果相应下载是由扩展程序发起的，则为发起相应下载的扩展程序的标识符。一经设置便无法更改。

如果此下载是由扩展程序发起的，则为发起此下载的扩展程序的本地化名称。如果扩展程序更改其名称或用户更改其语言区域，则可能会发生变化。

如果下载正在进行且已暂停，或者下载已中断且可以从中断处恢复，则为 true。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.endTime) console.log(new Date(item.endTime))})})

下载中断的原因。多种 HTTP 错误可能会归为以 SERVER_ 开头的某个错误。与网络相关的错误以 NETWORK_ 开头，与将文件写入文件系统的过程相关的错误以 FILE_ 开头，用户发起的中断以 USER_ 开头。

下载预计完成时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.estimatedEndTime) console.log(new Date(item.estimatedEndTime))})})

下载的文件是否仍然存在。由于 Chrome 不会自动监控文件移除情况，因此此信息可能已过时。调用 search() 以触发文件存在性检查。当存在性检查完成时，如果文件已被删除，则会触发 onChanged 事件。请注意，search() 不会等待存在性检查完成才返回，因此 search() 的结果可能无法准确反映文件系统。此外，search() 可以根据需要经常调用，但检查文件是否存在的时间间隔不会短于 10 秒。

整个文件解压缩后的字节数，如果未知，则为 -1。

如果相应下载记录在历史记录中，则为 False；如果未记录，则为 True。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

下载开始时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){console.log(new Date(item.startTime))})})

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

发起相应下载的绝对网址（在任何重定向之前）。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

相对于“下载”目录的文件路径，用于包含下载的文件，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径会导致错误。onDeterminingFilename 允许在确定文件的 MIME 类型和临时文件名后建议文件名。

HeaderNameValuePair[] 可选

如果网址使用 HTTP[s] 协议，则要随请求发送的额外 HTTP 标头。每个标头都表示为一个字典，其中包含键 name 和 value 或 binaryValue，且仅限于 XMLHttpRequest 允许的标头。

如果网址使用 HTTP[S] 协议，则要使用的 HTTP 方法。

使用文件选择器允许用户选择文件名，无论 filename 是否已设置或已存在。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后结束的 DownloadItem（采用 ISO 8601 格式）

将结果限制为在指定毫秒数之前结束的 DownloadItem（采用 ISO 8601 格式）。

整个文件解压缩后的字节数，如果未知，则为 -1。

将结果限制为 DownloadItem，其中 filename 与给定的正则表达式匹配。

将结果限制为 DownloadItem，其中 finalUrl 与给定的正则表达式匹配。

要查询的 DownloadItem 的 id。

返回的匹配 DownloadItem 的数量上限。默认值为 1000。设置为 0 可返回所有匹配的 DownloadItem。如需了解如何将结果分页，请参阅 search。

将此数组的元素设置为 DownloadItem 属性，以便对搜索结果进行排序。例如，设置 orderBy=['startTime'] 会按开始时间升序对 DownloadItem 进行排序。如需指定降序，请在前面加上连字符：“-startTime”。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

此搜索字词数组会将结果限制为 DownloadItem，其 filename 或 url 或 finalUrl 包含所有不以短划线“-”开头的搜索字词，但不包含任何以短划线开头的搜索字词。

下载开始时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后开始的 DownloadItem（采用 ISO 8601 格式）。

将结果限制为在指定毫秒数之前开始的 DownloadItem（采用 ISO 8601 格式）。

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

将结果限制为 totalBytes 大于指定整数的 DownloadItem。

将结果限制为 totalBytes 小于指定整数的 DownloadItem。

发起相应下载的绝对网址（在任何重定向之前）。

将结果限制为 DownloadItem，其中 url 与给定的正则表达式匹配。

为避免重复，系统会更改 filename，在文件扩展名前面添加计数器。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

DownloadItem 的新目标 DownloadItem.filename，作为相对于用户默认下载目录的路径，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径将被忽略。如果有任何扩展程序注册了 onDeterminingFilename 监听器，系统会忽略 filename。

返回的图标的大小。图标将为正方形，尺寸为 size * size 像素。图标的默认尺寸和最大尺寸均为 32x32 像素。唯一支持的大小是 16 和 32。指定任何其他大小都是错误的。

"FILE_VIRUS_INFECTED"

"FILE_TRANSIENT_ERROR"

"FILE_SECURITY_CHECK_FAILED"

"FILE_SAME_AS_SOURCE"

"NETWORK_DISCONNECTED"

"NETWORK_SERVER_DOWN"

"NETWORK_INVALID_REQUEST"

"SERVER_UNAUTHORIZED"

"SERVER_CERT_PROBLEM"

"SERVER_CONTENT_LENGTH_MISMATCH"

"SERVER_CROSS_ORIGIN_REDIRECT"

发生了错误，导致与文件托管服务的连接中断。

提示用户接受危险下载。只能从可见的上下文（标签页、窗口或页面/浏览器操作弹出式窗口）中调用。不会自动接受危险的下载内容。如果接受下载，系统会触发 onChanged 事件，否则不会发生任何情况。当所有数据都提取到临时文件中，并且下载不危险或危险已被接受时，临时文件会被重命名为目标文件名，state 更改为“complete”，并触发 onChanged。

取消下载。当 callback 运行时，下载已取消、完成、中断或不再存在。

下载网址。如果网址使用 HTTP[S] 协议，则请求将包含当前为其主机名设置的所有 Cookie。如果同时指定了 filename 和 saveAs，系统将显示“另存为”对话框，并预先填充指定的 filename。如果下载成功开始，系统将使用新的 DownloadItem 的 downloadId 调用 callback。如果启动下载时出错，系统将使用 downloadId=undefined 调用 callback，并且 runtime.lastError 将包含描述性字符串。我们不保证错误字符串在不同版本之间保持向后兼容。扩展程序不得解析该属性。

从历史记录中清除匹配的 DownloadItem，而不删除已下载的文件。对于与 query 匹配的每个 DownloadItem，系统都会触发 onErased 事件，然后调用 callback。

检索指定下载的图标。对于新下载的文件，在收到 onCreated 事件后，系统会显示文件图标。在下载进行期间，此函数返回的图片可能与下载完成后返回的图片不同。图标检索是通过查询底层操作系统或工具包（具体取决于平台）完成的。因此，返回的图标将取决于多种因素，包括下载状态、平台、注册的文件类型和视觉主题。如果无法确定文件图标，runtime.lastError 将包含一条错误消息。

GetFileIconOptions 可选

Promise<string | undefined>

如果 DownloadItem 完成，则立即打开下载的文件；否则通过 runtime.lastError 返回错误。此方法除了需要 "downloads" 权限之外，还需要 "downloads.open" 权限。当商品首次打开时，系统会触发 onChanged 事件。此方法只能在响应用户手势时调用。

暂停下载。如果请求成功，下载将处于暂停状态。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

如果下载的文件存在且 DownloadItem 已完成，则移除下载的文件；否则通过 runtime.lastError 返回错误。

恢复已暂停的下载。如果请求成功，则下载正在进行且未暂停。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

查找 DownloadItem。将 query 设置为空对象，以获取所有 DownloadItem。如需获取特定的 DownloadItem，请仅设置 id 字段。如需翻阅大量商品，请设置 orderBy: ['-startTime']，将 limit 设置为每页的商品数量，并将 startedAfter 设置为上一页中最后一项的 startTime。

Promise<DownloadItem[]>

启用或停用与当前浏览器个人资料关联的每个窗口底部的灰色搁架。只要至少有一个扩展程序停用了搁架，搁架就会处于停用状态。如果至少有一个其他扩展程序已停用功能架，则启用功能架会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.shelf" 权限。

更改与当前浏览器个人资料关联的每个窗口的下载界面。只要至少有一个扩展程序将 UiOptions.enabled 设置为 false，下载界面就会隐藏。如果将 UiOptions.enabled 设置为 true，但至少有一个其他扩展程序已将其停用，则会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.ui" 权限。

在文件管理器中，在相应文件夹中显示下载的文件。

当 DownloadItem 的任何属性（bytesReceived 和 estimatedEndTime 除外）发生更改时，系统会触发此事件，并提供 downloadId 和一个包含已更改属性的对象。

此事件会在下载开始时触发，并附带 DownloadItem 对象。

在确定文件名的过程中，扩展程序将有机会替换目标 DownloadItem.filename。每个扩展程序不得为此事件注册多个监听器。每个监听器都必须同步或异步调用 suggest 一次。如果监听器异步调用 suggest，则必须返回 true。如果监听器既不同步调用 suggest，也不返回 true，则系统会自动调用 suggest。在所有监听器都调用 suggest 之前，DownloadItem 不会完成。监听器可以调用不带任何实参的 suggest，以允许下载使用 downloadItem.filename 作为其文件名，也可以将 suggestion 对象传递给 suggest 以替换目标文件名。如果多个扩展程序替换了文件名，则最后一个安装的扩展程序（其监听器将 suggestion 对象传递给 suggest）胜出。为避免混淆哪个扩展程序会胜出，用户不应安装可能会发生冲突的扩展程序。如果下载是由 download 发起的，并且在确定 MIME 类型和临时文件名之前已知目标文件名，请改为将 filename 传递给 download。

FilenameSuggestion（可选）

当下载从历史记录中清除时，会触发并附带 downloadId。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "downloads"
  ],
}
```

Example 2 (unknown):
```unknown
chrome.downloads.acceptDanger(  downloadId: number,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.downloads.cancel(  downloadId: number,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.downloads.download(  options: DownloadOptions,): Promise<number>
```

---

## chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/storage?hl=zh-cn

**Contents:**
- chrome.storage 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 概念和用法
  - 扩展程序可以使用 Web 存储 API 吗？
  - 存储区域
  - 存储空间和限流限制
- 使用场景
  - 响应存储空间更新
  - 从存储空间异步预加载

使用 chrome.storage API 来存储、检索和跟踪用户数据的更改。

如需使用存储 API，请在扩展程序清单中声明 "storage" 权限。例如：

Storage API 提供了一种特定于扩展程序的方式来持久保留用户数据和状态。它类似于 Web 平台的存储 API（IndexedDB 和 Storage），但旨在满足扩展程序的存储需求。以下是一些关键功能：

虽然扩展程序可以在某些上下文（弹出式窗口和其他 HTML 页面）中使用 Storage 接口（可从 window.localStorage 访问），但我们不建议这样做，原因如下：

如需从服务工作线程将数据从 Web 存储 API 移至扩展程序存储 API，请执行以下操作：

此外，Web 存储 API 在扩展程序中的工作方式也存在一些细微差别。如需了解详情，请参阅存储和 Cookie 一文。

Storage API 具有以下用量限制：

如需详细了解存储区域限制以及超出限制后会出现什么情况，请参阅 sync、local 和 session 的配额信息。

以下各部分展示了 Storage API 的常见用例。

如需跟踪对存储空间所做的更改，请向其 onChanged 事件添加监听器。当存储空间中的任何内容发生变化时，系统都会触发该事件。示例代码会监听以下更改：

我们可以进一步拓展这个想法。在此示例中，我们有一个选项页面，可让用户切换“调试模式”（此处未显示实现）。选项页面会立即将新设置保存到 storage.sync，并且服务工作线程会使用 storage.onChanged 尽快应用该设置。

由于服务工作线程并非始终处于运行状态，因此 Manifest V3 扩展程序有时需要先从存储空间异步加载数据，然后才能执行其事件处理程序。为此，以下代码段使用异步 action.onClicked 事件处理程序，该处理程序会等待 storageCache 全局变量填充完毕，然后再执行其逻辑。

您可以在开发者工具中查看和修改使用该 API 存储的数据。如需了解详情，请参阅开发者工具文档中的查看和修改扩展程序存储空间页面。

以下示例展示了 local、sync 和 session 存储区：

如需查看存储 API 的其他演示，请探索以下任一示例：

“TRUSTED_CONTEXTS” 指定源自扩展程序本身的上下文。

"TRUSTED_AND_UNTRUSTED_CONTEXTS" 指定来自扩展程序外部的上下文。

Event<functionvoidvoid>

onChanged.addListener 函数如下所示：

要获取的单个键、要获取的键列表，或指定默认值的字典（请参阅对象说明）。空列表或空对象将返回空结果对象。传入 null 可获取存储空间的全部内容。

获取一个或多个内容所用的空间量（以字节为单位）。

getBytesInUse 函数如下所示：

单个键或键列表，用于获取总使用量。如果列表为空，则返回 0。传入 null 可获取所有存储空间的总用量。

一个对象，用于提供要更新存储空间的每个键值对。存储空间中的任何其他键值对都不会受到影响。

数字等原始值将按预期序列化。具有 typeof "object" 和 "function" 的值通常会序列化为 {}，但 Array（按预期序列化）、Date 和 Regex 除外（使用其 String 表示形式进行序列化）。

为存储区设置所需的访问权限级别。默认情况下，session 存储空间仅限受信任的上下文（扩展程序页面和服务工作器）访问，而 managed、local 和 sync 存储空间允许受信任和不受信任的上下文访问。

setAccessLevel 函数如下所示：

local 存储区中的内容是每个机器本地的。

可存储在本地存储空间中的数据量上限（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果扩展程序具有 unlimitedStorage 权限，系统将忽略此值。如果更新会导致超出此限制，则会立即失败，并在使用回调时设置 runtime.lastError，或者在使用 async/await 时设置被拒绝的 Promise。

managed 存储区域中的项由网域管理员配置的企业政策设置，并且对扩展程序是只读的；尝试修改此命名空间会导致错误。如需了解如何配置政策，请参阅存储区域的清单。

session 存储区域中的内容项存储在内存中，不会持久保存到磁盘。

可存储在内存中的最大数据量（以字节为单位），通过估算每个值和键的动态分配内存用量来衡量。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

sync 存储区域中的内容会使用 Chrome 同步功能进行同步。

同步存储空间中可存储的最大项数。如果更新会导致超出此限制，则更新会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

storage.sync API 不再具有持续写入操作配额。

每小时可执行的 set、remove 或 clear 操作数上限。此限制为每 2 秒 1 次，低于短期内每分钟较高的写入次数限制。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

每分钟可执行的 set、remove 或 clear 操作次数上限。即每秒 2 次，在较短的时间内提供比每小时写入次数更高的吞吐量。

如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中可存储的最大数据总量（以字节为单位），计算方式为每个值的 JSON 字符串化长度加上每个键的长度。如果更新会导致超出此限制，则会立即失败，并在使用回调时或在 Promise 被拒绝时设置 runtime.lastError。

同步存储空间中每个单独项的最大大小（以字节为单位），计算方式为相应值的 JSON 字符串化长度加上键长度。如果更新包含的项大于此限制，则会立即失败，并在使用回调时或 Promise 被拒绝时设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "storage"
  ],
  ...
}
```

Example 2 (javascript):
```javascript
chrome.storage.onChanged.addListener((changes, namespace) => {
  for (let [key, { oldValue, newValue }] of Object.entries(changes)) {
    console.log(
      `Storage key "${key}" in namespace "${namespace}" changed.`,
      `Old value was "${oldValue}", new value is &quot;${newValue}".`
    );
  }
});
```

Example 3 (unknown):
```unknown
<!-- type="module" allows you to use top leve>l< await --
script defer src="options.js><" >t<ype="module">;/s<cript
form id=&qu>ot;op<tionsForm"
  label for="debug">
    input type="che<ckbox&>q<uot; >name="debug" id="debug"
    Enable debug mode
  /label
/form
```

Example 4 (javascript):
```javascript
// In-page cache of the user's options
const options = {};
const optionsForm = document.getElementById("optionsForm");

// Immediately persist options changes
optionsForm.debug.addEventListener(">;change", (event) = {
  options.debug = event.target.checked;
  chrome.storage.sync.set({ options });
});

// Initialize the form with the user's option settings
const data = await chrome.storage.sync.get("options");
Object.assign(options, data.options);
optionsForm.debug.checked = Boolean(options.debug);
```

---

## chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/downloads

**Contents:**
- chrome.downloads 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 示例
- 类型
  - BooleanDelta
    - 属性
  - DangerType
    - 枚举
  - DoubleDelta

使用 chrome.downloads API 以编程方式启动、监控、操纵和搜索下载。

您必须在扩展程序清单中声明 "downloads" 权限，才能使用此 API。

您可以在 examples/api/downloads 目录中找到使用 chrome.downloads API 的简单示例。如需查看其他示例以及有关查看源代码的帮助，请参阅示例。

“content” 下载的文件已知为恶意文件。

“不常见” 相应下载内容的网址不常被下载，可能具有危险性。

“主机” 下载内容来自已知会分发恶意二进制文件的主机，可能存在危险。

“垃圾” 下载内容可能是垃圾内容或不安全。例如，它可能会更改浏览器或计算机设置。

“安全” 下载不会对用户的计算机造成已知危险。

“allowlistedByPolicy” 与企业相关的值。

"asyncLocalPasswordScanning"

"sensitiveContentWarning"

"sensitiveContentBlock"

"deepScannedOpenedDangerous"

"promptForLocalPasswordScanning"

“forceSaveToGdrive” 供安全企业浏览器扩展程序使用。在需要时，Chrome 会阻止下载到磁盘，并将文件直接下载到 Google 云端硬盘。

发生变化的 DownloadItem 的 id。

如果相应下载是由扩展程序发起的，则为发起相应下载的扩展程序的标识符。一经设置便无法更改。

如果此下载是由扩展程序发起的，则为发起此下载的扩展程序的本地化名称。如果扩展程序更改其名称或用户更改其语言区域，则可能会发生变化。

如果下载正在进行且已暂停，或者下载已中断且可以从中断处恢复，则为 true。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.endTime) console.log(new Date(item.endTime))})})

下载中断的原因。多种 HTTP 错误可能会归为以 SERVER_ 开头的某个错误。与网络相关的错误以 NETWORK_ 开头，与将文件写入文件系统的过程相关的错误以 FILE_ 开头，用户发起的中断以 USER_ 开头。

下载预计完成时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){if (item.estimatedEndTime) console.log(new Date(item.estimatedEndTime))})})

下载的文件是否仍然存在。由于 Chrome 不会自动监控文件移除情况，因此此信息可能已过时。调用 search() 以触发文件存在性检查。当存在性检查完成时，如果文件已被删除，则会触发 onChanged 事件。请注意，search() 不会等待存在性检查完成才返回，因此 search() 的结果可能无法准确反映文件系统。此外，search() 可以根据需要经常调用，但检查文件是否存在的时间间隔不会短于 10 秒。

整个文件解压缩后的字节数，如果未知，则为 -1。

如果相应下载记录在历史记录中，则为 False；如果未记录，则为 True。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

下载开始时间，采用 ISO 8601 格式。可直接传递给 Date 构造函数：chrome.downloads.search({}, function(items){items.forEach(function(item){console.log(new Date(item.startTime))})})

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

发起相应下载的绝对网址（在任何重定向之前）。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

相对于“下载”目录的文件路径，用于包含下载的文件，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径会导致错误。onDeterminingFilename 允许在确定文件的 MIME 类型和临时文件名后建议文件名。

HeaderNameValuePair[] 可选

如果网址使用 HTTP[s] 协议，则要随请求发送的额外 HTTP 标头。每个标头都表示为一个字典，其中包含键 name 和 value 或 binaryValue，且仅限于 XMLHttpRequest 允许的标头。

如果网址使用 HTTP[S] 协议，则要使用的 HTTP 方法。

使用文件选择器允许用户选择文件名，无论 filename 是否已设置或已存在。

指示相应下载内容是否被认为是安全的，或者是否已知是可疑的。

下载结束时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后结束的 DownloadItem（采用 ISO 8601 格式）

将结果限制为在指定毫秒数之前结束的 DownloadItem（采用 ISO 8601 格式）。

整个文件解压缩后的字节数，如果未知，则为 -1。

将结果限制为 DownloadItem，其中 filename 与给定的正则表达式匹配。

将结果限制为 DownloadItem，其中 finalUrl 与给定的正则表达式匹配。

要查询的 DownloadItem 的 id。

返回的匹配 DownloadItem 的数量上限。默认值为 1000。设置为 0 可返回所有匹配的 DownloadItem。如需了解如何将结果分页，请参阅 search。

将此数组的元素设置为 DownloadItem 属性，以便对搜索结果进行排序。例如，设置 orderBy=['startTime'] 会按开始时间升序对 DownloadItem 进行排序。如需指定降序，请在前面加上连字符：“-startTime”。

如果下载已停止从主机读取数据，但保持连接处于打开状态，则为 True。

此搜索字词数组会将结果限制为 DownloadItem，其 filename 或 url 或 finalUrl 包含所有不以短划线“-”开头的搜索字词，但不包含任何以短划线开头的搜索字词。

下载开始时间，采用 ISO 8601 格式。

将结果限制为在指定毫秒数之后开始的 DownloadItem（采用 ISO 8601 格式）。

将结果限制为在指定毫秒数之前开始的 DownloadItem（采用 ISO 8601 格式）。

整个文件中的字节数，不考虑文件压缩，如果未知则为 -1。

将结果限制为 totalBytes 大于指定整数的 DownloadItem。

将结果限制为 totalBytes 小于指定整数的 DownloadItem。

发起相应下载的绝对网址（在任何重定向之前）。

将结果限制为 DownloadItem，其中 url 与给定的正则表达式匹配。

为避免重复，系统会更改 filename，在文件扩展名前面添加计数器。

FilenameConflictAction 可选

如果 filename 已存在，则执行的操作。

DownloadItem 的新目标 DownloadItem.filename，作为相对于用户默认下载目录的路径，可能包含子目录。绝对路径、空路径和包含反向引用“..”的路径将被忽略。如果有任何扩展程序注册了 onDeterminingFilename 监听器，系统会忽略 filename。

返回的图标的大小。图标将为正方形，尺寸为 size * size 像素。图标的默认尺寸和最大尺寸均为 32x32 像素。唯一支持的大小是 16 和 32。指定任何其他大小都是错误的。

"FILE_VIRUS_INFECTED"

"FILE_TRANSIENT_ERROR"

"FILE_SECURITY_CHECK_FAILED"

"FILE_SAME_AS_SOURCE"

"NETWORK_DISCONNECTED"

"NETWORK_SERVER_DOWN"

"NETWORK_INVALID_REQUEST"

"SERVER_UNAUTHORIZED"

"SERVER_CERT_PROBLEM"

"SERVER_CONTENT_LENGTH_MISMATCH"

"SERVER_CROSS_ORIGIN_REDIRECT"

发生了错误，导致与文件托管服务的连接中断。

提示用户接受危险下载。只能从可见的上下文（标签页、窗口或页面/浏览器操作弹出式窗口）中调用。不会自动接受危险的下载内容。如果接受下载，系统会触发 onChanged 事件，否则不会发生任何情况。当所有数据都提取到临时文件中，并且下载不危险或危险已被接受时，临时文件会被重命名为目标文件名，state 更改为“complete”，并触发 onChanged。

取消下载。当 callback 运行时，下载已取消、完成、中断或不再存在。

下载网址。如果网址使用 HTTP[S] 协议，则请求将包含当前为其主机名设置的所有 Cookie。如果同时指定了 filename 和 saveAs，系统将显示“另存为”对话框，并预先填充指定的 filename。如果下载成功开始，系统将使用新的 DownloadItem 的 downloadId 调用 callback。如果启动下载时出错，系统将使用 downloadId=undefined 调用 callback，并且 runtime.lastError 将包含描述性字符串。我们不保证错误字符串在不同版本之间保持向后兼容。扩展程序不得解析该属性。

从历史记录中清除匹配的 DownloadItem，而不删除已下载的文件。对于与 query 匹配的每个 DownloadItem，系统都会触发 onErased 事件，然后调用 callback。

检索指定下载的图标。对于新下载的文件，在收到 onCreated 事件后，系统会显示文件图标。在下载进行期间，此函数返回的图片可能与下载完成后返回的图片不同。图标检索是通过查询底层操作系统或工具包（具体取决于平台）完成的。因此，返回的图标将取决于多种因素，包括下载状态、平台、注册的文件类型和视觉主题。如果无法确定文件图标，runtime.lastError 将包含一条错误消息。

GetFileIconOptions 可选

Promise<string | undefined>

如果 DownloadItem 完成，则立即打开下载的文件；否则通过 runtime.lastError 返回错误。此方法除了需要 "downloads" 权限之外，还需要 "downloads.open" 权限。当商品首次打开时，系统会触发 onChanged 事件。此方法只能在响应用户手势时调用。

暂停下载。如果请求成功，下载将处于暂停状态。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

如果下载的文件存在且 DownloadItem 已完成，则移除下载的文件；否则通过 runtime.lastError 返回错误。

恢复已暂停的下载。如果请求成功，则下载正在进行且未暂停。否则，runtime.lastError 会包含错误消息。如果下载未处于有效状态，则请求会失败。

查找 DownloadItem。将 query 设置为空对象，以获取所有 DownloadItem。如需获取特定的 DownloadItem，请仅设置 id 字段。如需翻阅大量商品，请设置 orderBy: ['-startTime']，将 limit 设置为每页的商品数量，并将 startedAfter 设置为上一页中最后一项的 startTime。

Promise<DownloadItem[]>

启用或停用与当前浏览器个人资料关联的每个窗口底部的灰色搁架。只要至少有一个扩展程序停用了搁架，搁架就会处于停用状态。如果至少有一个其他扩展程序已停用功能架，则启用功能架会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.shelf" 权限。

更改与当前浏览器个人资料关联的每个窗口的下载界面。只要至少有一个扩展程序将 UiOptions.enabled 设置为 false，下载界面就会隐藏。如果将 UiOptions.enabled 设置为 true，但至少有一个其他扩展程序已将其停用，则会通过 runtime.lastError 返回错误。除了 "downloads" 权限之外，还需要 "downloads.ui" 权限。

在文件管理器中，在相应文件夹中显示下载的文件。

当 DownloadItem 的任何属性（bytesReceived 和 estimatedEndTime 除外）发生更改时，系统会触发此事件，并提供 downloadId 和一个包含已更改属性的对象。

此事件会在下载开始时触发，并附带 DownloadItem 对象。

在确定文件名的过程中，扩展程序将有机会替换目标 DownloadItem.filename。每个扩展程序不得为此事件注册多个监听器。每个监听器都必须同步或异步调用 suggest 一次。如果监听器异步调用 suggest，则必须返回 true。如果监听器既不同步调用 suggest，也不返回 true，则系统会自动调用 suggest。在所有监听器都调用 suggest 之前，DownloadItem 不会完成。监听器可以调用不带任何实参的 suggest，以允许下载使用 downloadItem.filename 作为其文件名，也可以将 suggestion 对象传递给 suggest 以替换目标文件名。如果多个扩展程序替换了文件名，则最后一个安装的扩展程序（其监听器将 suggestion 对象传递给 suggest）胜出。为避免混淆哪个扩展程序会胜出，用户不应安装可能会发生冲突的扩展程序。如果下载是由 download 发起的，并且在确定 MIME 类型和临时文件名之前已知目标文件名，请改为将 filename 传递给 download。

FilenameSuggestion（可选）

当下载从历史记录中清除时，会触发并附带 downloadId。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "downloads"
  ],
}
```

Example 2 (unknown):
```unknown
chrome.downloads.acceptDanger(  downloadId: number,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.downloads.cancel(  downloadId: number,): Promise<void>
```

Example 4 (unknown):
```unknown
chrome.downloads.download(  options: DownloadOptions,): Promise<number>
```

---

## 存储空间和 Cookie 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/storage-and-cookies?hl=zh-cn

**Contents:**
- 存储空间和 Cookie 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 存储
  - 持久性
  - Service Worker 中的访问权限
  - 分区
- Cookie
  - 安全 Cookie
  - 分区和 SameSite 行为

扩展程序可以像常规网站一样存储 Cookie 和访问网络存储 API。但在某些情况下，它们在扩展程序中的行为有所不同。

如需了解该扩展程序 API，请参阅 chrome.storage。

通常情况下，开发者建议您在扩展程序中使用网络平台存储 API。本部分探讨这些 API 在扩展程序上下文中的行为，这些行为有时可能会因其在网页上的行为方式而异。

当用户清除浏览数据时，扩展程序存储空间不会被清除。 这适用于使用 Web 存储 API（例如本地存储空间和 IndexedDB）存储的所有数据。

默认情况下，扩展程序受常规的存储空间配额限制，您可以调用 navigator.storage.estimate() 进行检查。在内存紧张时，也可能会逐出存储，不过这种情况很少见。为避免发生这种情况，请执行以下操作：

扩展程序存储空间可供扩展程序的所有来源共享，包括扩展程序 Service Worker、所有扩展程序页面（包括弹出式窗口和侧边栏）和屏幕外文档。在内容脚本中，调用 Web Storage API 会访问注入了内容脚本的主机页面（而不是扩展程序）中的数据。

可以在 Service Worker 中访问 IndexedDB 和 Cache Storage API。但本地存储和会话存储不适用。

如果您需要通过 Service Worker 访问本地存储空间或会话存储空间，请使用屏幕外文档。

分区是为存储的数据引入键的地方，以限制可以访问这些数据的位置。一直以来，存储都由源进行键控。

从 Chrome 115 开始，存储分区引入了对分区键的定义方式的更改，以防止某些类型的跨网站跟踪。也就是说，如果网站 A 嵌入了包含网站 B 的 iframe，网站 B 将无法访问直接导航到网站 B 时通常具有的存储空间。

为减轻这种扩展程序在延期中造成的影响，需遵循以下两种豁免规则：

Cookie 提供了一种存储与特定网域和路径相关联的键值对的方法。扩展程序在扩展程序方面的价值有限，但如果您有特定用例或捆绑了第三方脚本来使用扩展程序，了解它们的行为会很有帮助。

只有 https:// 方案支持 Secure Cookie 属性。因此，chrome-extension:// 网页无法使用此属性设置 Cookie。

这也意味着，扩展程序页面无法使用需要 Secure 属性的其他 Cookie 属性：

在 chrome-extension:// 页面上设置的 Cookie 始终使用 SameSite=Lax。 因此，扩展程序在其自身来源上设置的 Cookie 永远无法在框架中访问，并且分区也无关紧要。

对于与第三方网站关联的 Cookie（例如，对于在扩展程序页面上的框架中加载的第三方网站，或者从扩展程序页面向第三方来源发出的请求），Cookie 的行为与网站相同，但存在以下两个方面：

请注意，第三方 Cookie 的相关设置受 Privacy Sandbox 工作的影响，并根据其时间表进行调整。

chrome.cookies API 可让您控制要与每种 API 方法搭配使用的分区键。如需了解详情，请参阅 API 参考文档。

---
