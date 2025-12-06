# Chrome-Extensions - Other

**Pages:** 127

---

## chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/windows/?hl=zh-cn

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

## Linux 的自托管 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/distribute/host-on-linux

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

## 分发扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/distribute

**Contents:**
- 分发扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如果您只想为自己构建扩展程序，可以加载未封装的扩展程序。未封装的扩展程序只能用于在开发过程中加载可信代码。

如果您不是要构建供个人使用的扩展程序，则最终需要分发该扩展程序。官方支持的分发机制只有两种。在这两种情况下，Chrome 都会定期检查扩展程序主机上已安装扩展程序的新版本，并自动更新这些扩展程序，无需用户干预。

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/develop?hl=zh-cn

**Contents:**
  - 开发
- 设计界面
  - 侧边栏
  - 操作
  - 菜单
- 控制浏览器
  - 覆盖 Chrome 网页和设置
  - 扩展开发者工具
  - 显示通知
  - 管理历史记录

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/reference?hl=zh-cn

**Contents:**
  - 参考
- API 参考文档
    - chrome.action
    - chrome.alarms
    - chrome.commands
    - chrome.declarativeNetRequest
    - chrome.offscreen
    - chrome.runtime
    - chrome.scripting
    - chrome.sidePanel

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to?hl=zh-cn

**Contents:**
  - 使用方法
- 类别
  - 设计界面
    - 支持无障碍功能
    - 使用网站图标
    - 将扩展程序本地化
    - 通知用户
    - 扩展开发者工具
  - 使用 Web 平台
    - 在 ChromeOS 中处理文件

---

## 内容过滤 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/content-filtering?hl=zh-cn

**Contents:**
- 内容过滤 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 过滤网络请求
  - 将过滤条件规则与扩展程序捆绑在一起
  - 在运行时动态添加过滤规则
- 根据观察到的请求调整规则
- 允许用户定义自己的过滤规则
- 过滤网页上的元素
- 过滤已安装政策的扩展程序中的网络请求
- 拦截导航请求

在 Chrome 扩展程序中，您可以通过不同的方式实现内容和网络过滤。本指南概述了可供扩展程序使用的内容过滤功能，以及 Chrome 扩展程序可以使用的不同过滤方法、技术和 API。

在 Chrome 扩展程序中过滤网络请求的主要方法是使用 chrome.declarativeNetRequest API。借助声明式网络请求，开发者可以通过指定声明式规则来阻止或修改网络请求。声明式网络请求规则格式基于大多数广告拦截器使用的过滤器列表语法的功能。

Chrome 支持与扩展程序捆绑在一起的规则，以及动态更新的规则（例如响应远程配置或用户输入的规则）。

扩展程序软件包中包含的规则称为“静态规则”。在安装或升级扩展程序时，系统会安装和更新这些规则。Chrome 会限制扩展程序可以声明的静态规则数量。

对于静态声明式网络请求规则，Chrome 有一个包含 30 万条规则的全局共享池，可供一组已安装的扩展程序共同使用。此外，还保证每个扩展程序最多可以创建 30, 000 条静态规则。例如，如果用户只安装了一个内容过滤扩展程序，则该扩展程序最多可以使用 330,000 条静态声明式网络请求规则。为便于您了解规则的数量，大多数广告拦截器常用的 EasyList 过滤器列表都包含大约 35,000 条网络规则。

静态声明式网络请求规则可整理为不同的规则集。一个扩展程序最多可以指定 100 个静态规则集，并且一次可以启用 50 个规则集。

部分规则不能与扩展程序捆绑在一起。相反，扩展程序需要在运行时添加它们。这些规则称为“动态规则”。

对于动态声明式网络请求规则，Chrome 允许每个扩展程序最多 30,000 条安全动态规则。大多数规则都被视为安全规则：block、allow、allowAllRequests 或 upgradeScheme。即使某条规则被视为不安全的规则（例如 redirect），仍然可以动态添加，但最大数量上限为 5,000 条，同时也会计入 30,000 条动态规则数量上限。更确切地说，在简易列表过滤条件列表中，有 98-99% 的规则都是安全规则。

内容过滤扩展程序可以分别使用静态和动态规则将已知的过滤规则与其扩展程序捆绑在一起，并根据需要使用来自服务器的新内容过滤规则更新其扩展程序。

广告生态系统在不断变化，内容过滤器也需要随之更新。通过结合使用 chrome.webRequest 和动态声明式网络请求规则，可以分析网络请求是否存在可能侵犯隐私权的行为，并在日后屏蔽此类请求。

这种方法的优势在于，分析过程是异步进行的，不会对网站性能产生负面影响。

您可以在扩展程序中提供过滤器配置界面，让用户自行定义内容过滤规则。将这些用户定义的规则转换为声明式网络请求规则，并将它们添加为动态规则。这些规则在浏览器会话和扩展程序升级之间保持不变，仍可供用户使用。使用此方法，用户最多可以添加 3 万条自定义规则。

过滤网络请求只是内容过滤的一个重要部分。另一项重要工作是直接从网页中移除不需要的内容。例如，超过 40% 的 easylist filter list 规则定义了客户端应如何隐藏页面元素。

这可以通过内容脚本来实现。内容脚本在网页环境中运行，可以使用 DOM 对网页进行更改。

Chrome 扩展程序无法执行远程托管代码。但是，来自服务器且与要隐藏的元素相关的数据不受影响，因为这些数据被视为配置数据，因此可以根据需要在运行时更新元素规则。

企业和教育用例通常对内容和网络过滤有极其严格的要求，例如根据内容过滤请求。为了启用这些用例，已安装政策的扩展程序提供了一种额外的方法来过滤和屏蔽网络请求。对 webRequest API 中的事件使用“屏蔽”选项时，可以实现一个程序化内容过滤器，以便针对每个请求执行自定义逻辑，以决定是否应屏蔽某个请求。这仅限于通过政策安装的扩展程序，因为这些扩展程序具有较高的信任级别。

可以使用声明式网络请求规则过滤导航请求。例如，您可能希望绕过将用户重定向到预期目标网址的跟踪网址。一种处理方法是将导航请求 https://tracker.com?redirect=https%3A%2F%2Fexample.com 重定向到扩展程序页面（需要配置为可通过 Web 访问的资源），然后系统会运行脚本来提取重定向目标，并使用 window.location.replace("https://example.com") 绕过链接跟踪器来重定向到目标位置。

---

## 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers?hl=zh-cn

**Contents:**
- 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

本部分介绍了在扩展程序中使用 Service Worker 需要了解的内容。无论您是否熟悉 Service Worker，都应该阅读本部分。扩展程序 Service Worker 是扩展程序的核心事件处理脚本。这使得它们与 Web Service Worker 明显不同，网络中成堆的 Service Worker 文章不一定有用。

Extension Service Worker 与 Web 扩展 Service Worker 有一些共同点。扩展 Service Worker 在需要时加载，并在其进入休眠状态时取消加载。只要扩展程序 Service Worker 在加载后还会主动接收事件，它就会运行，不过它可以关闭。与对应的 Web 应用一样，扩展 Service Worker 无法访问 DOM，不过您可以根据需要将其用于屏幕外文档。

扩展程序 Service Worker 不只是网络代理（因为经常会提到 Web Service Worker）。除了标准 Service Worker 事件之外，它们还会响应扩展程序事件，例如导航到新页面、点击通知或关闭标签页。它们的注册和更新方式也与 Web Service Worker 不同。

---

## Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/whatsnew?hl=zh-cn

**Contents:**
- Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 视频：解答有关 Chrome 应用商店可发现性的问题
- Chrome 140：新增了 sidePanel.getLayout() API
- 新指南：扩展程序更新生命周期
- Chrome 139：在 Chrome 品牌 build 中移除 --extensions-on-chrome-urls 和 --disable-extensions-except flag
- Chrome 138：对新标签页的更改
- 博文：在即将发生的书签变更之前更新扩展程序
- 博文：2025 年 6 月 Chrome 扩展程序的最新动态
- 视频：在浏览器中玩打地鼠游戏 - 这是真的吗？
- 视频：Chrome 的新扩展程序菜单说明

请经常查看此页面，了解 Chrome 扩展程序、扩展程序文档或相关政策或其他方面的变化。您可以在 Chrome 扩展程序邮寄名单中找到其他通知。Chrome 时间表列出了稳定版和 Beta 版的发布日期。

发布日期：2025 年 11 月 25 日

在最新视频中，我们会解答您在 Chrome 应用商店中发现应用方面的问题。

从 Chrome 140 开始，您可以使用新的 sidePanel.getLayout() API 来确定侧边栏位于屏幕的左侧还是右侧。如果您支持 RTL 语言，而新安装的 Chrome 的默认语言不同，此功能尤为有用。

我们发布了一份新指南，说明了 Chrome 中扩展程序的更新方式。

从 Chrome 139 开始，官方 Chrome 品牌 build 中将移除 --extensions-on-chrome-urls 和 --disable-extensions-except 命令行标志。详细了解邮寄名单。

从 Chrome 138 开始，我们将更新新标签页界面，添加新的页脚。 您可以访问邮寄名单页面了解详情。

我们将对书签同步功能进行一些更改，这可能会影响您的扩展程序。如需了解详情，请参阅这篇博文。

我们一直在忙碌，推出了 Google I/O 大会，并在 Chrome 和 Chrome 应用商店中推出了多项新功能。请参阅Chrome 扩展程序最新动态 - 2025 年 6 月，了解最新资讯！

观看我们的最新视频，了解如何在浏览器中制作游戏。

观看我们的最新视频“Chrome 的新扩展程序菜单详解” ，了解实验性的新扩展程序菜单。

在“扩展程序真棒”第 1 集中了解如何开始开发扩展程序，并在第 2 集中了解 Chrome 自定义功能的灵活性！

从 Chrome 135 开始，chrome.userScripts API 中提供了一个新的 userScripts.execute() 方法。您可以使用此方法在任意时间注入用户脚本一次，而无需永久注册该脚本。

从 Chrome 132 开始，您可以在开发者工具中查看和修改使用 chrome.storage API 存储的数据。如需了解详情，请参阅开发者工具文档中的新页面查看和修改扩展程序存储空间。

在 2024 年 Google I/O 大会上，我们分享了扩展程序菜单即将发生的一些早期设计变更，这些变更可让用户更好地控制扩展程序可以访问的网站。我们很快就会开始测试这些变更，首先会在 Canary 中面向一小部分用户进行测试，并希望将来能更广泛地推出这些变更。

我们还推出了 chrome.permissions.addHostAccessRequest() API。

发布日期：2024 年 11 月 19 日

从 Chrome 132 开始，Tabs API 中的 frozen 属性用于指示标签页是否已被浏览器冻结。发送到冻结标签页的消息将排队，并在标签页解除冻结后处理。

发布日期：2024 年 11 月 12 日

扩展程序专用 Prompt API 现已在初始源试用中提供，因此您可以在浏览器中构建使用 Gemini Nano（我们最高效的语言模型）的 Chrome 扩展程序。

加入 Prompt API 源试用（在 Chrome 131 至 136 中进行），并分享您的反馈。您的反馈可以直接影响我们构建和实现此 API 和所有内置 AI API 的未来版本的方式。

发布日期：2024 年 10 月 17 日

现在，我们又可以来盘点一下 Chrome 扩展程序方面的最新动态了：我们在 AI 集成、新 API、活动和视频方面都有令人兴奋的更新。如需了解详情，请参阅 Chrome 扩展程序 10 月刊！

发布日期：2024 年 10 月 17 日

Chrome 推出了内置 AI 挑战赛：诚邀您使用 Chrome 的集成 AI 模型和 API 创建创新的 Web 应用和 Chrome 扩展程序，赢取总计 65,000 美元的奖品。

如需注册并详细了解相关信息，请访问 Built-in AI Challenge 网站。我们迫不及待地想看看您在为 Web 注入 AI 后会创作出什么作品！

从 Chrome 130 开始，action.onUserSettingsChanged 事件可用。这是根据 WebExtensions 社区组中的一项提案实现的。感谢 Microsoft 为 Chromium 做出的贡献。

从 Chrome 130 开始，getKeys() 方法可在 chrome.storage API 使用的 StorageArea 接口上使用。这是根据 WebExtensions 社区组中的提案实现的。

从 Chrome 128 开始，我们将在 Declarative Net Request API 中添加对响应标头匹配的支持。这是一个常见的要求，尤其是在匹配 Content-Type 标头时，我们与 WebExtensions 社区组一起设计了一个合适的 API。

我们已更新 API 参考文档，以纳入新的 responseHeaders 和 excludedResponseHeaders 字段。您可以使用这些方法来检查指定标头的存在情况和值。

在此次更新中，我们在文档中添加了一个新的规则评估部分，其中介绍了规则的匹配方式。对于标头匹配，规则只能在收到响应标头后运行，因此它们的应用阶段比其他规则晚。这意味着，请求在被屏蔽或重定向之前确实到达了服务器。

了解 Chrome 扩展程序中的内容脚本，包括如何注册 CSS 和 JavaScript 以在特定网页上运行。观看完整视频。

Chrome 应用商店团队发布了一系列更新，对开发者计划政策页面进行了修改，旨在鼓励开发优质产品、防止欺骗性行为，并确保用户在知情的情况下同意。Chrome 应用商店政策经理 Rebecca Soares 在 Chrome 扩展程序：重要政策更新这篇博文中总结了所有更新。

在过去三个月内，我们推出了一些重大更新和新功能，包括开始逐步淘汰清单 V2。快来了解 Chrome 扩展程序 7 月刊中的最新动态！

Chrome 扩展程序团队的 Patrick 介绍了 Chrome 扩展程序中远程托管代码 (RHC) 的概念。了解为何不再允许使用 RHC、如何检测 RHC，以及如果您的扩展程序需要更新，该怎么做。观看完整视频。

从 Chrome 127 开始，所有扩展程序都可以使用 action.openPopup API。以前，它仅在 Canary 中或通过政策安装的扩展程序中可用。

Chrome 扩展程序 DevRel 团队与负责 Chrome 应用商店审核的 Trust & Safety 团队进行了交流，询问了您提出的问题。观看完整视频。

从 6 月 3 日开始，在 Chrome Beta 版、Dev 版和 Canary 版渠道中，如果用户仍安装了 Manifest V2 扩展程序，那么当他们访问扩展程序管理页面 (chrome://extensions) 时，部分用户会开始看到警告横幅，告知他们所安装的部分（Manifest V2）扩展程序很快将不再受支持。如需了解详情，请参阅官方公告

我们最近对侧边栏界面进行了一些更改，包括添加了固定图标并移除了全局侧边栏图标。如需了解详情，请参阅公开服务公告 (PSA)，并查看我们更新的文档和示例。

又一届 Google I/O 大会已经落幕，我们报道了所有令人兴奋的扩展程序更新！前往 YouTube 观看完整视频，并阅读我们的博文，了解一些精彩内容。

现在，当您使用 Declarative Net Request API 时，Chrome 应用商店允许您跳过对符合条件的更改的审核。如需详细了解资格要求以及如何选择启用，请参阅 Chrome 应用商店文档。

我们最近更新了 Chrome 应用商店 API 文档，添加了有关 deployPercentage 的信息。借助该 API，您可以分配部分发布部署的百分比。了解 deployPercentage。

Chrome 126 引入了一个新的 manifest.json 字段 - trial_tokens，让您可以在所有扩展程序界面中选择加入源试用和弃用试用。如需了解详情，请参阅指南。

我们发布了新一期Chrome 扩展程序动态。该帖子讨论了扩展程序团队在过去几个月中的工作。这包括：Chrome 应用商店中的版本回滚、更好的 Firebase Auth 支持以及更多 API 发布和更新。

将扩展程序回滚到 Chrome 应用商店中之前发布的版本，无需额外审核！如需了解详情，请参阅这篇博文和文档。

ChromeOS 上现已提供高级 documentScan API，用于发现和检索连接的文档扫描仪中的图片。

自 Chrome 124 起，服务工作线程支持 WebGPU。如需快速入门，请查看 WebGPU 扩展程序示例。

Events API 现在支持按无类别域间路由 (CIDR) 区块进行过滤。CIDR 块是共享相同网络前缀和相同位数的 IP 地址集合。以前，如果开发者需要过滤多个 IP 地址，则需要为屏蔽范围内的每个地址配置过滤规则。现在，当扩展程序调用 addListener() 时，传入的规则意味着只有当网址的主机部分是 IP 地址且包含在数组中指定的任何 CIDR 块中时，才会调用事件处理脚本。

在 Chrome 应用商店中，清单文件 (manifest.json) 中扩展程序的 "name" 字段现在有 75 个字符的通用限制。之前，英文的限制为 45 个字符，其他语言区域的 "name" 字段没有限制。

此功能最初旨在允许存在文化和语言差异，而这些差异可能无法用相同数量的字符来表达。遗憾的是，一小部分开发者滥用了此功能，向商店发送垃圾内容。因此，我们推出了新的通用限制，将字符数上限提高到 75 个。 此限制涵盖了目前商店中的几乎所有扩展程序，因此您很可能无需因这一变化而采取任何行动。如果您尝试上传的扩展程序的名称超过了上限，商店会阻止该上传操作。

在这篇由 eyeo 的扩展程序引擎团队撰写的博文中，我们将探讨测试扩展程序服务工作线程的问题。在 Manifest V2 中，扩展程序位于后台网页中，在整个扩展程序生命周期内都处于唤醒状态。Manifest V3 使用的是服务工作器，而服务工作器在不需要时会关闭，从而节省资源。这会带来一定的测试挑战。这篇博文介绍了 eyeo 如何应对这些挑战。

当设备进入休眠状态时，使用 chrome.alarms API 设置的闹钟不再延迟。当设备唤醒时，无论错过了多少闹钟，闹钟都会响一次。例如，假设闹钟设置为每小时响一次，而设备在凌晨 12:55 到凌晨 2:05 处于休眠状态，那么只有凌晨 2:00 的闹钟会触发 onAlarm 事件。它会在尽可能接近凌晨 2:00 时触发，如果设备处于休眠状态，则会在设备唤醒时立即触发。

此更改使 Chrome 符合 Web 扩展程序社区组中达成的行为一致性。

往返缓存 (bfcache) 是一种浏览器优化，可实现即时后退和前进导航。从 Chrome 123 开始，当具有开放扩展程序端口的网页存储在 bfcache 中时，消息渠道会关闭，这意味着不会向该网页发送任何消息。因此，扩展程序脚本应监听 onDisconnect 等生命周期事件，并在网页从 BFCache 恢复时设置新连接。

如需了解详情和查看示例代码，请参阅扩展消息端口对 BFCache 行为的更改。

我们已完成对所有异步扩展 API 方法的 Promise 支持实现。这样做是为了通过改进处理异步操作的人体工程学来使 API 方法现代化。少数方法（例如 desktopCapture.chooseDesktopMedia()）仍仅支持回调，因为其当前界面与 Promise 不兼容。为了实现向后兼容性，我们仍支持回调。如果您发现 Promise 失败，请提交 bug 报告。

我们刚刚发布了有关扩展程序中实时选项的指南。实时更新功能可提供从服务器直接到扩展程序安装的即时通信路径。此外，我们还针对使用 chrome.gcm、Web 推送提供了新的指南。

我们刚刚发布了一篇指南，介绍了如何使用 Puppeteer 测试 Service Worker 终止。随附的示例在 Puppeteer 和 Selenium 中演示了这一点。

我们刚刚发布了原生消息的更新版示例。此 API 允许您的扩展程序启动另一个应用并与之通信。感谢 GitHub 贡献者 Shubham-Rasal 为此做出的贡献。

向 tabs.Tab 对象添加了一个名为 lastAccessed 的新属性。此属性表示标签页上次处于活动状态的时间。返回的值以毫秒为单位，从纪元起算。

在从 Manifest V2 更改为 Manifest V3 的过程中，"background" 清单键的子项发生了更改，以适应将后台脚本替换为扩展程序服务工作线程。以前，如果将 Manifest V2 键 "scripts"、"page" 或 "persistent" 添加到 Manifest V3 扩展程序的 "background" 键中，系统会抛出错误。现在，如果存在这些键，系统会触发警告。

这样做是为了能够根据社区组中的提案，在多个浏览器中的扩展程序中使用单个清单文件。

发布日期：2023 年 12 月 14 日

从 Chrome 120 开始，Manifest V3 扩展程序可以使用延迟时间或周期为 30 秒的 chrome.alarms API，而无需使用 60 秒或更长的值。

发布时间：2023 年 11 月 16 日

Manifest V2 支持时间表已更新。如需了解详情，请参阅我们的2023 年 11 月博文。

发布日期：2023 年 11 月 15 日

如需了解我们如何在新博文中改进 declarativeNetRequest API，请参阅该博文。

Chrome 120 Beta 版已于最近发布。如需简要了解与扩展程序开发者相关的重要更新，请阅读我们的新博文：Chrome 120 中的扩展程序新功能。此版本还标志着一个重要里程碑，因为它从关键平台差距列表中移除了最后两项（userScripts、ChromeOS 上的文件处理程序）。

开发者信息中心内的隐私权政策现在是在商品级添加的。这样，您就可以为每个商品提供不同的隐私权政策。如需详细了解此变更，请参阅我们的PSA。

发布时间：2023 年 10 月 26 日

我们刚刚在 Chrome for Developers YouTube 频道上发布了一段新视频，其中与 Google 开发者专家兼作者 Matt Frisbie 进行了对话。点击此处观看。

我们刚刚发布了有关如何为扩展程序编写自动化测试的新指南，包括如何编写单元测试，以及有关端到端测试的一般指南和教程。

我们刚刚发布了第二期Chrome 扩展程序动态。这篇博文讨论了扩展程序团队在过去几个月内所做的工作，包括解决服务工作线程稳定性问题，以及在弥合所有 MV3 平台差距方面取得的良好进展。我们还分享了即将发布的令人期待的 API，例如 Reading List API 和 User Scripts API。

根据 Web Extensions 社区组中的反馈，我们将启用静态规则集的数量上限从 10 大幅提高到 50。此外，我们将允许的静态规则集总数从 50 个增加到 100 个。此功能目前已在 Canary 中推出。

Manifest V3 的一项要求是，扩展程序不得再使用远程托管的代码。虽然这从一开始就包含在我们的迁移指南中，但我们认为有必要改进有关此问题的指南。该页面现在提供了更多信息，介绍了在 Manifest V3 中仍然可以实现的功能，并提供了有关升级策略的更多信息。

我们还新增了一篇与排查 Chrome 应用商店违规行为相关的文章。新增了一个部分，介绍了具有远程托管代码的扩展程序被拒的常见原因。

发布日期：2023 年 10 月 11 日

从 Chrome 118 开始，chrome.declarativeNetRequest API 中的 isUrlFilterCaseSensitive 属性已更改为默认值为 false。如果您希望保留旧行为，可以在 declarativeNetRequest 规则中将 isUrlFilterCaseSensitive 明确设置为 true。

这遵循了 Web Extensions 社区组中的讨论。Firefox 和 Safari 已经实现了类似的更改。

我们发布了一份新指南，介绍了 Cookie 和 Web 存储 API 在 Chrome 扩展程序中的运作方式。 其中包含有关 Privacy Sandbox 中 Cookie 和存储分区变更的详细信息。Privacy Sandbox 是一个正在进行的项目，旨在通过创建一系列新的 Web 平台 API 来弃用第三方 Cookie，并详细说明这些 API 在扩展程序中的运作方式。

我们最近创建了一个页面，可让您搜索 Chrome 扩展程序示例。搜索页面上有多个选项。您可以使用搜索框搜索示例标题中的文字。您可以按权限或扩展程序 API 限制搜索范围。借助额外的过滤条件，您可以将搜索范围限制为 API 或功能（用例）示例。

这个新的示例网页由 Google Summer of Code 参与者薛舟戴构建，他还贡献了多个新示例。如需了解他们在去年夏天获得的体验，请参阅我们博客上的相关博文。

与之前一样，您仍然可以在 GitHub 上克隆或派生我们的代码示例。

从 Chrome 118 开始，扩展程序需要从 chrome://extensions 页面启用“允许访问文件网址”设置，才能使用 Tabs 或 Windows API 打开 file:// 方案网址。您可以通过调用 chrome.extension.isAllowedFileSchemeAccess() 以编程方式检查此访问权限。Firefox 已经限制了文件网址，而 Safari 支持此项更改。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

之前，通过扩展程序 API 调用触发的针对 tabs.update()、tabs.create() 和 windows.create() 的导航会针对某些 chrome:// 网址发出错误。此外，禁止使用 JavaScript 网址调用 tabs.update()。在 117 中，这些针对 JavaScript 网址的保护措施已扩展到 tabs.create() 方法，并且已将许多其他 chrome:// 网址添加到禁止的网址列表中，该列表适用于上述所有方法。

chrome.declarativeNetRequest API 通过指定声明式规则来阻止或修改网络请求。这样一来，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而为用户提供更高的隐私保护。而且使用起来也很棘手。鉴于此，我们重写了相关指南，以便更清晰地说明如何实现声明性规则集。请点击上方的链接，阅读新部分。

Chrome 应用商店与 Google Analytics 集成，因此除了开发者信息中心提供的视图之外，您还可以查看 Chrome 应用商店商品详情的分析数据。如需了解详情，请参阅将 Google Analytics 账号与 Chrome 应用商店搭配使用。

注入的内容脚本现在默认位于开发者工具的忽略列表中。这不会影响断点，但意味着在调试期间，系统会跳过内容脚本，并忽略这些脚本中的异常。当内容脚本在 Sources 标签页中打开时，如果此功能处于开启状态，系统会显示一条横幅提醒您，并提供用于从忽略列表中移除内容脚本的选项。如需关闭此行为，请打开开发者工具，前往设置，然后前往忽略列表。如需了解详情，请参阅开发者工具的新变化。

Chrome 116 是一个重要的扩展程序版本。您现在可以以编程方式打开侧边栏。借助一种新方法，您可以了解是否存在有效的屏幕外文档。Service Worker 得到了多项改进。116 版中包含的改进非常多，我们专门撰写了一篇博文来介绍这些改进。截至 7 月 19 日，Chrome 116 处于 Beta 版阶段。

我们刚刚发布了有关今年扩展程序变更和改进的概览。该博文讨论了本年度的新功能，包括侧边栏 API、服务工作线程增强功能和屏幕外文档。您还可以了解我们本季度正在开展的工作。该文章列出了更多内容，并提供了指向所有内容的链接。

我们发布了新的 Google Analytics 和地理位置信息指南及示例：

现在，您可以在调用 chrome.offscreen.createDocument() 时指定多个 reason 枚举。当屏幕外文档将用于多种不同用途时，请使用此方法。浏览器会使用提供的原因来确定屏幕外文档的生命周期。

我们刚刚发布了扩展程序更新测试工具，这是一个本地扩展程序更新服务器，可在本地开发期间用于测试 Chrome 扩展程序的更新，包括权限授予。该工具会显示用户的更新流程，包括在用户授予任何新请求的权限之前，保持扩展程序处于停用状态。此工具对于模拟将扩展程序从 Manifest V2 更新到 Manifest V3 时所请求的权限变更特别有用。

我们推出了新的 Side Panel API，这是一个配套界面，可让用户在浏览内容的同时访问工具。如需了解详情，请参阅边栏 API 参考文档。此外，我们还在 GitHub 示例代码库中添加了许多侧边栏示例。我们还在新博文使用新的侧边栏 API 设计出色的用户体验中详细介绍了侧边栏。我们还审核了质量指南政策和最佳实践，以便为创建高质量的侧边栏扩展程序提供更多指导。

您的反馈对于打造此 API 至关重要；请在 chromium-groups 中分享您的想法和功能请求。我们会继续改进侧边栏 API，敬请关注最新动态。

我们提供了两个新示例，演示了如何在扩展程序中使用 WASM：

特别感谢 GitHub 贡献者 @daidr 提供这些示例。

我们更新了 Manifest V3 迁移指南的已知问题部分，其中包含一份更新后的扩展平台差距列表，我们打算在宣布新的 Manifest V2 弃用时间表之前弥合这些差距。

我们刚刚发布了一篇新文章，名为音频录制和屏幕捕获，其中介绍了如何在 Manifest V3 中录制标签页、窗口或屏幕中的音频或视频。本文介绍了涉及 chrome.tabCapture API 和 getDisplayMedia() 函数的多种录制方法。

我们已将 storage.local 属性的配额增加到大约 10 MB。这是 Web Extensions Community Group 中达成的共识。这使得 storage.local 与 Chrome 112 中更改的 storage.session 保持一致。

Service Worker 是 Chrome 扩展程序不可或缺的一部分。我们刚刚发布了一篇教程，介绍了注册、调试和与 Service Worker 互动的基本知识。我们还添加了新的服务工作线程指南，其中更详细地介绍了重要概念。我们将在未来几个月内扩充此部分的内容。

为了帮助您在 Chrome 应用商店中发布内容，我们在以下两个方面添加了新指南。最基本的功能指南的重点在于为用户提供益处并丰富其浏览体验。联属营销广告指南旨在让用户了解广告客户使用联属营销链接或代码创收的扩展服务，并通过要求用户在添加之前执行操作来赋予用户一定程度的控制权。

我们重写了扩展程序清单转换器的 README，以便您更轻松地了解运行该工具后需要执行的操作。转换器可帮助将基于 Manifest V2 构建的扩展程序迁移到 Manifest V3。新版 README 使用与迁移指南的清单中非常相似的字词描述了该工具的功能。转换器并非万能，但确实可以省去许多不需要人工判断的任务。

我们为 Offscreen Documents API 添加了两种新的原因类型。使用 LOCAL_STORAGE 访问 Web 平台的 localStorage API。创建网页工作器时使用 WORKER。

Chrome 应用商店开发者信息中心现在支持 Google Analytics 4 (GA4)。我们简化了 Google Analytics 的设置流程，并使群组发布商的访问权限管理更加简单明了。如果您之前使用 Google Universal Analytics 跟踪您的商店详情活动，则需要在 2023 年 7 月 1 日之前采取行动，以确保您能够继续接收有关商店详情的数据。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

文件处理程序 API 可在 ChromeOS Canary 版中进行实验，适用于 112 和 113 版。它允许 ChromeOS 上的扩展程序打开具有指定 MIME 类型和文件扩展名的文件。如需实现文件处理，请向 manifest.json 添加一组规则。此功能的工作方式与渐进式 Web 应用相同。如需了解详情，请参阅本网站上的这篇文章。

我们希望在 6 月下旬推出 Chrome 115 时发布此功能。请关注此空间，了解最新动态。

我们为 chrome.scripting API 构建了一个新示例。它演示了动态声明（在运行时注册内容脚本）和程序化注入（在已打开的标签页中执行脚本）。

我们提供了三个新示例，用于演示声明式网络请求 API。每个示例都展示了单个用例的实现。第一个示例展示了如何屏蔽 Cookie。其余两个示例演示了如何屏蔽和重定向网址。

自 Chrome 112 起，storage.session 属性的配额已增加到大约 10 MB。Web Extensions Community Group 已就此达成一致：https://github.com/w3c/webextensions/issues/350

Manifest V3 扩展程序现在支持屏幕外文档。这些 API 可支持与 DOM 相关的功能，从而帮助您从后台网页过渡到扩展程序服务工作线程。如需了解详情，请阅读此博文。

chrome.action.isEnabled() 方法以编程方式检查是否已为特定标签页启用扩展程序。这样一来，您就无需维护标签页的启用状态。此新方法接受标签页 ID 和对回调的引用，并返回一个布尔值。但它有一个限制：使用 chrome.declarativeContent 创建的标签页始终返回 false。

（chrome.action 命名空间最近新增了一些用于控制扩展程序徽章外观的方法。如需了解详情，请参阅设置徽章颜色。）

以前，扩展程序服务工作线程通常会在 5 分钟时关闭。我们已更改此行为，使其更接近于 Web 上的 Service Worker 生命周期。扩展程序服务工作线程会在闲置 30 秒后关闭，或者在单个活动的处理时间超过 5 分钟时关闭。如需了解详情，请参阅延长扩展服务工作器的生命周期。

我们正在审核 Manifest V2 弃用时间表，并推迟原定于 2023 年初进行的实验。如需了解详情，请阅读 Chrome 扩展程序邮寄名单中的更新。

chrome.action 命名空间新增了两种方法，可让您更好地控制外观扩展程序徽章。setBadgeTextColor() 和 getBadgeTextColor() 方法允许扩展程序更改和查询其工具栏图标的徽章文本颜色。与 setBadgeBackgroundColor 和 getBadgeBackgroundColor 搭配使用时，这些新方法可让您强制保持设计和品牌的一致性。

我们明确了 Manifest V2 弃用时间表。Manifest V2 支持时间表也已更新，以反映此信息。

我们整理了一份目前正在开发中的主要功能和公开 bug 的列表。我们希望通过此页面帮助开发者更好地了解平台的当前状态，以及在为未来做准备时可以考虑哪些功能。

Chrome 应用商店已从开发者信息中心的商品详情标签页中移除了“大型宣传块”上传界面。由于这些图片未在消费者界面中使用，因此此次变更不会影响最终用户体验。如需了解详情，请参阅这篇 chromium-extensions 博文。

根据 crbug.com/1219825#c11，不透明源（例如沙盒 iframe 和动态导入）也应该能够访问可通过网络访问的资源。

之前，调用异步 API 的 Manifest V3 可以提供无效的最终实参，而 Chrome 不会出错。通过此修复，Chrome 现在可以正确报告错误，并指出没有匹配的签名。建议开发者在 Canary 上检查其扩展程序是否存在任何错误，以免因意外使用错误的签名进行 API 调用而导致此 bug 修复破坏扩展程序。

Chrome 应用商店为 Chrome 应用商店开发者信息中心推出了经过改进的商品分析体验。新信息中心可让您一目了然地了解情况，并提前整合最有用的信息。如需了解详情，请阅读这篇博文。

Identity API 上的函数现在支持基于 Promise 的调用。这会略微改变 identity.getAuthToken() 的界面，其中设置为基于 Promise 的调用的异步返回将具有“token”和“grantedScopes”作为单个对象上的参数（而不是回调版本将它们作为单独的实参接收到回调中）。

Manifest V3 扩展程序现在可以使用新的网址格式 chrome-extension://<id>/_favicon/ 访问收藏夹图标，其中 是扩展程序的 ID。这取代了 Manifest V2 平台的 chrome://favicons API。如需了解详情，请参阅 Favicon API 文档。

添加了交易者/非交易者开发者身份标识，可提醒开发者准确自行声明其交易者/非交易者身份。

Chrome 不再默认向扩展程序授予 script-src: wasm-unsafe-eval。使用 WebAssembly 的扩展程序现在必须在其 content_security_policy 声明中明确添加此指令和值到 extension_pages。

在 chrome://extensions/shortcuts 上更改 Manifest V3 扩展程序的键盘快捷键时，更新现在会立即应用。之前，必须重新加载扩展程序，更改才会生效。

动态注册的内容脚本现在可以指定要将资源注入到的 world。如需了解详情，请参阅 scripting.registerContentScripts()。

Manifest V3 扩展程序现在可以在 manifest.json 中指定 optional_host_permissions 键。这样一来，Manifest V3 扩展程序就可以像 Manifest V2 扩展程序那样，使用 optional_permissions 键来声明主机的可选匹配模式。

chrome.scripting.executeScript() 现在接受其 injection 实参中的可选 injectImmediately 属性。如果存在且设置为 true，脚本将尽快注入到目标中，而不是等待 document_idle。请注意，这并不能保证脚本会在网页加载之前注入，因为在进行 API 调用的同时，网页会继续加载。

现在，基于 Service Worker 的扩展程序可以使用 Omnibox API。之前，由于内部依赖于 DOM 功能，此 API 的某些方法会在调用时抛出异常。

Manifest V3 扩展程序现在可以在其 content_security_policy 声明中包含 wasm-unsafe-eval。此变更允许 Manifest V3 扩展程序使用 WebAssembly。

Manifest V3 扩展程序现在可以使用内存存储空间 storage.session。

在 Chrome 应用商店中发现内容一文概述了用户如何在 Chrome 应用商店中查找商品，以及我们的编辑如何选择要重点展示的商品。

declarativeNetRequest 规则条件已更新，以便扩展程序能够根据请求的“request”和“initiator”网域更好地定位请求。相关的条件属性为 initiatorDomains、excludedInitiatorDomains、requestDomains 和 excludedRequestDomains。另请参阅此 chromium-extensions 帖子。

修复了长期存在的问题：在新建的标签页或窗口上调用 scripting.executeScript() 可能会失败。

在扩展程序的服务工作线程中使用 chrome.runtime.connectNative() 连接到原生消息传递主机应使服务工作线程在端口打开期间保持活跃状态。

omnibox.setDefaultSuggestion() 方法现在会返回一个 promise 或接受一个回调，以允许开发者确定建议何时已正确设置。

扩展程序服务工作线程上下文现在支持 chrome.i18n.getMessage() API。

内容脚本现在可以指定 match_origin_as_fallback 键，以注入到与匹配框架相关的框架中，包括具有 about:、data:、blob: 和 filesystem: 网址的框架。如需了解详情，请参阅内容脚本文档。

发布时间：2021 年 12 月 30 日

基于 Service Worker 的 Manifest V2 和 Manifest V3 扩展程序现在可以使用 Fetch API 请求 file: 方案网址。访问 file: 方案网址仍需要用户在 chrome://extensions 页面中为扩展程序启用“允许访问文件网址”。

发布时间：2021 年 12 月 28 日

为基于 Manifest V3 构建的扩展程序向 tabs.sendMessage、runtime.sendMessage 和 runtime.sendNativeMessage 添加了 Promise 支持。

发布时间：2021 年 12 月 10 日

添加了新参考页面，其中概述了 Chrome 应用商店审核流程，并说明了如何处理开发者计划政策的违规行为。

脚本 API 的 executeScript() 和 insertCSS() 方法现在接受多个文件。以前，这些方法需要一个包含单个文件条目的数组。

发布日期：2021 年 10 月 27 日

我们更新了排查 Chrome 应用商店违规行为页面，为开发者提供了有关常见拒绝原因的更详细指南。

此版本包含的 promise 更新明显多于任何之前的版本。更新包括常规扩展程序 API 和 ChromeOS 专用扩展程序 API。展开即可下部分即可查看详细信息。

许多 API 现在在清单 V3 中支持 Promise。

此外，使用 ChromeSetting 原型的 API 现在也支持 promise。以下 API 会受到此项变更的影响。

chrome.scripting API 现在支持在运行时注册、更新、取消注册和获取列表内容脚本。以前，内容脚本只能在扩展程序的 manifest.json 中静态声明，或者在运行时通过 chrome.scripting.executeScript() 以编程方式注入。

这篇博文中公布了从 Manifest V2 到 V3 的过渡时间表，并发布了更详细的时间表页面。

借助新的 declarativeNetRequestWithHostAccess 权限，扩展程序可以在具有主机权限的网站上使用 chrome.declarativeNetRequest API。这还允许使用 webRequest、webRequestBlocking 和特定于网站的主机权限的现有 Manifest V2 扩展程序迁移到 chrome.declarativeNetRequest API，而无需用户批准新权限。

chrome.scripting API 的 executeScript() 方法现在可以直接将脚本注入到网页的主世界中。以前，扩展程序只能直接注入到扩展程序的隔离世界中。如需详细了解隔离的世界，请参阅有关内容脚本的文档。

Manifest V3 版 chrome.storage API 中的方法现在会返回 promise。

我们已更新 2021 年 6 月 29 日发布的政策更新博文，以更正两步验证部署时间表。

chrome.declarativeNetRequest 现在支持指定最多 50 个静态规则集 (MAX_NUMBER_OF_STATIC_RULESETS)，并同时启用最多 10 个规则集 (MAX_NUMBER_OF_ENABLED_STATIC_RULESETS)。

现在，Manifest V2 和 Manifest V3 扩展程序都可以选择启用跨源隔离。此功能可限制哪些跨源资源可以加载扩展程序的网页，并支持使用 SharedArrayBuffer 等低级 Web 平台功能。从 Chrome 95 版开始，必须选择启用。

我们更新了 Chrome 应用商店开发者计划政策，对欺骗性安装策略、垃圾内容和重复性内容政策进行了阐明。 此更新还新增了一项要求，即必须进行两步验证才能在 Chrome 应用商店中发布内容。如需了解详情，请阅读这篇博文。

Chrome 扩展程序多年来一直使用 chrome.browserAction 和 chrome.pageActions API，但 Manifest V3 将两者都替换为通用的 chrome.actions API。这篇博文探讨了这些 API 的历史记录以及 Manifest V3 中的变化。阅读帖子。

chrome.scripting API 是一项新的 Manifest V3 API，专注于脚本。在这篇博文中，我们将深入探讨此项变更的动机，并仔细了解其新功能。阅读帖子。

Chrome 现在支持在 Service Worker 中使用 JavaScript 模块。如需在清单中指定模块，请执行以下操作：

这会将 worker 脚本加载为 ES 模块，从而让您可以在 worker 的脚本中使用 import 关键字来导入其他模块。

新的 chrome.action.getUserSettings() 方法允许扩展程序确定用户是否已将扩展程序固定到主工具栏。

新的 chrome.scripting.removeCSS() 方法允许扩展程序移除之前通过 chrome.scripting.insertCSS() 插入的 CSS。它取代了 chrome.tabs.removeCSS()。

chrome.scripting.executeScript() 现在支持返回 promise。如果脚本执行的最终值是 Promise，Chrome 会等待 Promise 得到解决，并返回其最终值。

从 chrome.scripting.executeScript() 返回的结果现在包含 frameId。frameId 属性表示结果来自哪个框架，以便扩展程序在注入多个框架时轻松将结果与各个框架相关联。

新的 chrome.tabGroups API 和 chrome.tabs 中的新功能可让扩展程序读取和操纵标签页组。 需要使用 Manifest V3。

发布日期：2020 年 12 月 23 日

Manifest V3 中的可供 Web 访问的资源定义已发生变化，可让扩展程序根据请求者的来源或扩展程序 ID 限制资源访问权限。

Chrome 扩展程序团队已开源“扩展程序清单转换器”，这是一款 Python 工具，可自动执行将扩展程序转换为 Manifest V3 的部分机械性工作。请参阅公告博文，并从 GitHub 获取。

Manifest V3 是对扩展平台进行的一项重大更新；如需了解新功能和变更功能的摘要，请参阅 Manifest V3 概览。扩展程序目前可以继续使用 Manifest V2，但我们会在不久的将来逐步淘汰这一版本。我们强烈建议您为所有新扩展程序使用 Manifest V3，并尽快开始将现有扩展程序迁移到 Manifest V3。

**Examples:**

Example 1 (unknown):
```unknown
"background": {
  "service_worker": "script.js",
  "type": "module"
}
```

---

## chrome.accessibilityFeatures 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/accessibilityFeatures

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
REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_company.my_application" /ve /t REG_SZ /d "C:\path\to\nmh-manifest.json" /f
```

Example 3 (unknown):
```unknown
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\com.my_company.my_application]
@="C:\\path\\to\\nmh-manifest.json"
```

Example 4 (unknown):
```unknown
var port = chrome.runtime.connectNative('com.my_company.my_application');
port.onMessage.addListener(function (msg) {
  console.log('Received' + msg);
});
port.onDisconnect.addListener(function () {
  console.log('Disconnected');
});
port.postMessage({text: 'Hello, my_application'});
```

---

## 查找和跟踪错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/find-a-bug

**Contents:**
- 查找和跟踪错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

在提交扩展程序的 bug 或功能请求之前，您应先查看未解决的 Chromium 问题，确认是否已有人报告过该 bug 或功能请求。这些问题会记录在 Chromium 问题跟踪器中。借助此数据库，您可以搜索并跟踪针对 Chromium 报告的任何问题。

请勿通过回复“我也是”来回应任何 bug 或功能请求。请订阅 Chrome 扩展程序邮寄名单，及时了解 bug 的修复时间。不过，如果您有有价值的信息（例如更好的测试用例或建议的修复），请添加评论。

---

## 在 Service Worker 中使用 WebSocket 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/websockets

**Contents:**
- 在 Service Worker 中使用 WebSocket 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 背景
- 示例：WebSocket 保持连接

本教程演示了如何在 Chrome 扩展程序的服务工程中连接到 WebSocket。您可以在 GitHub 上找到有效示例。

从 Chrome 116 开始，扩展程序 Service Worker 可以更好地支持 WebSockets。以前，如果 30 秒内没有发生其他扩展事件，即使 WebSocket 连接处于活动状态，Service Worker 也可能会变为非活动状态。这会终止 Service Worker 并关闭 WebSocket 连接。如需详细了解扩展程序服务工件生命周期，请参阅扩展程序服务工件指南。

从 Chrome 116 开始，您可以通过在 30 秒的 Service Worker 活动窗口内交换消息，让具有 WebSocket 连接的 Service Worker 保持活跃状态。这些操作可以通过您的服务器或扩展程序发起。在以下示例中，我们将从 Chrome 扩展程序向服务器发送一条常规消息，以确保 Service Worker 保持活动状态。

首先，我们需要确保我们的扩展程序仅在支持服务工作器中的 WebSocket 的 Chrome 版本中运行，为此，请在清单中将最低 Chrome 版本设置为 116：

然后，我们可以通过每 20 秒发送一次 keepalive 消息来让服务工作器保持活跃状态。在 Service Worker 连接到 WebSocket 后，系统会启动 keepalive。以下示例 WebSocket 客户端会记录消息，并在 onopen 事件触发时调用 keepAlive()：

在 keepAlive() 中，我们使用 setInterval(...) 在有有效 WebSocket 连接时定期向服务器发送 ping：

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
  "minimum_chrome_version": "116",
  ...
}
```

Example 2 (javascript):
```javascript
let webSocket = null;

function connect() {
  webSocket = new WebSocket('wss://example.com/ws');

  webSocket.onopen = (event) => {
    console.log('websocket open');
    keepAlive();
  };

  webSocket.onmessage = (event) => {
    console.log(`websocket received message: ${event.data}`);
  };

  webSocket.onclose = (event) => {
    console.log('websocket connection closed');
    webSocket = null;
  };
}

function disconnect() {
  if (webSocket == null) {
    return;
  }
  webSocket.close();
}
```

Example 3 (javascript):
```javascript
function keepAlive() {
  const keepAliveIntervalId = setInterval(
    () => {
      if (webSocket) {
        webSocket.send('keepalive');
      } else {
        clearInterval(keepAliveIntervalId);
      }
    },
    // Set the interval to 20 seconds to prevent the service worker from becoming inactive.
    20 * 1000 
  );
}
```

---

## 提交功能请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/request-feature?hl=zh-cn

**Contents:**
- 提交功能请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如果您认为某项功能有助于改进扩展程序平台，请按照以下说明提交请求。

在问题跟踪器中提交问题。填写功能请求时，请尽可能明确说明。

我们越了解您的用例和需求，就越能轻松满足您的需求。

等待 bug 更新。大多数请求会在一周内分类处理，但有时可能需要更长时间。请勿回复请求更新的工单。如果您的工单在两周后仍未修改，请向 Chrome 扩展程序邮寄名单发送邮件，并附上请求的链接。

如果您最初是在讨论群组中发布了请求，并被重定向到了此处，请发布指向您创建或在讨论群组会话中找到的问题的链接。这样，其他有相同请求的用户便能更轻松地找到正确的工单。

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/reference

**Contents:**
  - 参考
- API 参考文档
    - chrome.action
    - chrome.alarms
    - chrome.commands
    - chrome.declarativeNetRequest
    - chrome.offscreen
    - chrome.runtime
    - chrome.scripting
    - chrome.sidePanel

---

## chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/declarativeContent/?hl=zh-cn

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

## chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/browsingData

**Contents:**
- chrome.browsingData 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
- 用法
- 特定来源
- 来源类型
- 示例
- 类型
  - DataTypeSet

使用 chrome.browsingData API 从用户的本地个人资料中移除浏览数据。

必须在扩展程序清单中声明“browsingData”权限，才能使用此 API。

此 API 最简单的使用场景是用于清除用户浏览数据的基于时间的机制。您的代码应提供一个时间戳，用于指明历史日期，在此日期之后的用户浏览数据应被移除。此时间戳的格式为自 Unix 纪元以来经过的毫秒数（可通过 JavaScript Date 对象的 getTime 方法检索）。

例如，如需清除用户过去一周的所有浏览数据，您可以编写如下代码：

借助 chrome.browsingData.remove 方法，您只需一次调用即可移除各种类型的浏览数据，这比调用多个更具体的方法要快得多。不过，如果您只想清除一种特定的浏览数据（例如 Cookie），那么更精细的方法可提供一种可读的替代方案，而无需使用包含 JSON 的调用。

如果用户正在同步数据，chrome.browsingData.remove 可能会在清除同步账号的 Cookie 后自动重建该 Cookie。这是为了确保同步功能可以继续正常运行，以便最终在服务器上删除数据。不过，更具体的 chrome.browsingData.removeCookies 可用于清除同步账号的 Cookie，在这种情况下，同步会暂停。

如需移除特定来源的数据或排除一组来源而不进行删除，您可以使用 RemovalOptions.origins 和 RemovalOptions.excludeOrigins 参数。它们只能应用于 Cookie、缓存和存储空间（CacheStorage、FileSystems、IndexedDB、LocalStorage、ServiceWorkers 和 WebSQL）。

通过向 API 的 options 对象添加 originTypes 属性，您可以指定应影响哪些类型的来源。目前，来源分为三类：

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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

清除在特定时间范围内修改的浏览器 Cookie 和服务器绑定证书。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

清除浏览器中的已下载文件列表（不清除已下载的文件本身）。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

已移除通过扩展程序删除密码的功能。此函数无效。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

已移除对 Flash 的支持。此函数无效。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

报告“清除浏览数据”设置界面中当前选择的数据类型。注意：此 API 中包含的某些数据类型在设置界面中不可用，并且某些界面设置可控制此处列出的多种数据类型。

所有类型都会显示在结果中，如果允许移除这些类型（例如，通过企业政策），则值为 true；否则值为 false。

所有类型都将显示在结果中，如果同时选择移除和允许移除，则值为 true，否则为 false。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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

## 保护用户隐私 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/security-privacy/user-privacy?hl=zh-cn

**Contents:**
- 保护用户隐私 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 减少所需权限
  - activeTab
- 选择授予可选权限
- 限制和保护用户信息
- 正在节省数据流量和无痕模式

如果扩展程序侵犯用户隐私或要求用户提供更多必要的权限，则用户不会安装该扩展程序。向用户提出的权限请求必须合理，且仅限于实施扩展程序所需的关键信息。收集或传输任何用户数据的扩展程序都必须遵守保护用户隐私下的政策。

采取这些预防措施来保护并尊重扩展程序用户的身份信息。

扩展程序可以访问的 API 在清单的 permissions 字段中指定。授予的权限越多，攻击者拦截信息的途径就越多。应仅列出扩展程序所依赖的 API，并考虑使用侵入性较低的选项。扩展程序请求的权限越少，向用户显示的权限警告就越少。用户更有可能安装收到有限警告的扩展程序。

扩展程序不应“满足未来需求”通过请求用户目前不需要但将来可能会实现的权限来访问用户数据。通过扩展程序更新添加新权限，并考虑将其设为可选权限。

使用主机权限注入脚本的扩展程序通常可以改用 activeTab。activeTab 权限将仅在用户调用扩展程序时，授予扩展程序对当前活动标签页的临时访问权限。当用户离开或关闭当前标签页时，访问权限会被切断。它可以作为 <all_urls> 的许多用途的替代方案。

在安装过程中，activeTab 权限不会显示警告消息。

通过添加可选权限，让用户能够选择自己需要的扩展程序功能和权限。如果某个功能对扩展程序的核心功能而言并不是至关重要的，请将其设为可选，并将相应 API 或网域移至 optional_permissions 字段。

添加可选权限可让扩展程序说明其需要特定权限的原因 当用户启用相关功能时触发。该扩展程序可以为用户提供一个启用 功能。

点击 Ok! 将在 Service Worker 中触发以下事件。

可选权限也可以在扩展程序更新中实现。这样做会创建新的 用户无需停用扩展程序即可使用这项功能，因为使用新版 Chrome 更新 所需权限。

请仅请求扩展程序所需的最少数据量。扩展程序向用户索取的信息越少，在扩展程序遭到入侵后，曝光率也越低。

应谨慎处理所请求的所有用户数据。在安全的服务器上存储和检索数据： 注册域名。始终使用 HTTPS 连接，并避免将敏感用户数据保留在客户端中 因为扩展程序存储未加密。

扩展程序可以使用 storage API 或通过发出 省数据当扩展程序需要保存内容时，请先考虑保存的内容是否来自 隐身窗口。默认情况下，扩展程序不会在无痕式窗口中运行。

无痕模式会保证该窗口不会留下任何痕迹。当处理来自 无痕式窗口，扩展程序应遵守这一承诺。如果扩展程序通常会保存浏览数据 历史记录，不保存无痕式窗口中的历史记录。不过，扩展程序可以存储设置 设置。

要检测某个窗口是否处于无痕模式，请检查相关窗口的 incognito 属性， tabs.Tab 或 windows.Window 对象。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 2 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  ...
  "optional_permissions": [ "tabs", ],
  "optional_host_permissions": ["https://www.google.com/" ],
  ...
}
```

Example 3 (javascript):
```javascript
chrome.action.onClicked.addListener((event) => {
  // Permissions must be requested from inside a user gesture, like a button's
  // click handler.
  chrome.permissions.request(
    {
      permissions: ["tabs", "scripting"],
      origins: ['https://www.google.com/']
    },
    function (granted) {
      // The callback argument will be true if the user granted the permissions.
      if (granted) {
        // doSomething();
      } else {
        // doSomethingElse();
      }
    }
  );
});
```

Example 4 (unknown):
```unknown
function saveTabData(tab) {
  if (tab.incognito) {
    return;
  } else {
    chrome.storage.local.set({data: tab.url});
  }
}
```

---

## 将 Firebase Cloud Messaging (FCM) 与 chrome.gcm 搭配使用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/chrome.gcm

**Contents:**
- 将 Firebase Cloud Messaging (FCM) 与 chrome.gcm 搭配使用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前提条件
- 配置 chrome.gcm
- 监听消息
- 不使用 Firebase 的 Firebase
- 针对频道和主题

您可以通过以下应用向最终用户发送和接收消息： chrome.gcm。因为它是基于 Firebase Cloud Messaging (FCM)，它依赖于您需要的外部服务 进行设置。本方法指南将引导您完成获取该工具的所有必要步骤 。

虽然 chrome.gcm 仍受支持，但它是十多年前创建的 推送标准一般来说，最好的做法始终是 标准 API，而不是扩展程序专用的 API。除非您有特定需求 要使用 chrome.gcm，我们建议使用推送。

如需使用 chrome.gcm，您需要设置 Firebase 。

创建账号后，您需要打开 Firebase 控制台，然后选择要使用的现有项目，或创建一个新项目 。

继续前往 Cloud Messaging 的设置页面。

如果您已经拥有此项目的云消息传递账号，则需要 复制列出的发送者 ID（用数字表示）。

如果未启用云消息传递，则需要启用 Firebase Google Cloud 内部项目的 Cloud Messaging API。在以下 您可以看到 Firebase 中此页面的 设置。

启用后，返回 Cloud 的设置页面 发送消息，然后复制发送者 ID。

现在您已从 Firebase 获得发送者 ID，接下来可以配置扩展程序了 监听消息。首先，请确保您已添加 gcm 对您的扩展程序的 manifest.json 的权限

您现在可以访问 chrome.gcm API 了。您可以注册监听推送消息 通过调用 chrome.gcm.register 发送的消息

扩展程序注册发送者 ID 后，您需要添加代码来处理 消息。

虽然 chrome.gcm 始终通过 Firebase 运行，但 Firebase 可以配置为 充当外部推送消息传递供应商的代理。通常情况下，供应商会 明确列出了对 Chrome 扩展程序的支持， Firebase 的旧版推送通知应该正常运行。如果您的提供商列出 支持 Firebase 的旧版推送通知，欢迎体验一下。如果您遇到 提供商支持人员应能够澄清 应用场景

chrome.gcm 使用的是旧版 Firebase Messaging API。这很重要 因为旧版 API 不支持消息通道。每封邮件 将传送到每个客户端如果用户的扩展程序只对 部分邮件，您需要自行进行过滤。

Firebase 最初是作为免费账号使用，但超出配额后，您需要 特定使用量阈值。如果您打算向特定群组发送邮件 那么客户端过滤功能最终所耗费的成本可能会超过预期您可以 为了解决这个问题，可以创建多个项目来复制各个渠道 （每个渠道一个项目和一个发送者 ID）。任何给定的扩展程序都可以 注册多个发送者 ID（最多 100 个）。

或者，如果您需要频道支持，或者想要使用推送通知 您可以使用 Push API。

**Examples:**

Example 1 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["gcm"]
```

---

## 提交功能请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/request-feature

**Contents:**
- 提交功能请求 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如果您认为某项功能有助于改进扩展程序平台，请按照以下说明提交请求。

在问题跟踪器中提交问题。填写功能请求时，请尽可能明确说明。

我们越了解您的用例和需求，就越能轻松满足您的需求。

等待 bug 更新。大多数请求会在一周内分类处理，但有时可能需要更长时间。请勿回复请求更新的工单。如果您的工单在两周后仍未修改，请向 Chrome 扩展程序邮寄名单发送邮件，并附上请求的链接。

如果您最初是在讨论群组中发布了请求，并被重定向到了此处，请发布指向您创建或在讨论群组会话中找到的问题的链接。这样，其他有相同请求的用户便能更轻松地找到正确的工单。

---

## chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/devtools/recorder

**Contents:**
- chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 可用性
- 概览
- 自定义导出功能
- 导出插件示例
- 自定义重放按钮
- Replay 插件示例
- 类型
  - RecorderExtensionPlugin

使用 chrome.devtools.recorder API 自定义开发者工具中的“Recorder”面板。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

devtools.recorder API 是一项预览版功能，可让您扩展 Chrome 开发者工具中的 Recorder 面板。 从 Chrome M105 开始，您可以扩展导出功能。从 Chrome M112 开始，您可以延长重放按钮。

如需注册扩展插件，请使用 registerRecorderExtensionPlugin 函数。此函数需要插件实例、name 和 mediaType 作为参数。插件实例必须实现两种方法：stringify 和 stringifyStep。

该扩展程序提供的 name 会显示在 Recorder 面板的 Export 菜单中。

根据用户的导出环境，当用户点击该扩展程序提供的导出选项时， Recorder 面板会调用以下两个函数之一：

mediaType 参数允许该扩展程序指定其使用 stringify 和 stringifyStep 函数。例如，如果结果是 JavaScript，则返回 application/javascript 计划。

以下代码会实现一个扩展程序插件，该插件会使用 JSON.stringify 将录制转换为字符串：

如需在 Recorder 中自定义“重放”按钮，请使用 registerRecorderExtensionPlugin 函数。插件必须实现 replay 方法，自定义设置才能生效。 如果检测到该方法，Recorder 中会显示重放按钮。 点击此按钮后，系统会将当前录制对象作为第一个参数传递给 replay 方法。

此时，该扩展程序可以显示用于处理重放的 RecorderView，或使用其他扩展程序 API 来处理重放请求。如需创建新的 RecorderView，请调用 chrome.devtools.recorder.createView。

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

## chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/tabs/?hl=zh-cn

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

## 注册您的扩展程序以参与源代码试用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/origin-trials?hl=zh-cn

**Contents:**
- 注册您的扩展程序以参与源代码试用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 查找正在进行的源试用
- 确定您的扩展程序 ID
- 注册扩展程序
- 使用试用令牌
  - 扩展程序来源
  - 内容脚本

Origin 试用计划面向所有开发者开放，是限时性计划，可让开发者抢先体验实验性平台功能。在默认启用之前，您可以使用这些标志来测试新的扩展程序 API 或平台行为。由于试用期是有期限的，因此您应确保即使试用期结束，您的扩展程序也能继续正常运行。

查看 Chrome Origin 试用版的完整列表。积极征求开发者反馈的源代码试用版通常会通过博文或社交媒体主动分享。

如需注册来源试用，您需要提供扩展程序 ID。

为确保您的扩展程序 ID 在开发期间和发布扩展程序时保持不变，请按照保持一致的扩展程序 ID 中的步骤操作。如果您的扩展程序已在 Chrome 应用商店中发布，您可以按照以下步骤操作，为现有扩展程序详情添加付费版本，而无需创建新的详情。

在特定试验的页面上，点击注册。请记住可试用的 Chrome 版本和试用结束日期。

在“Web Origin”（网站来源）字段中提供您的 Chrome 扩展程序来源，例如 chrome-extension://abcdefghijklmnopqrstuvwxyz。

您将收到一个令牌，需要使用该令牌在扩展程序中启用试用版。

您可以在扩展程序源或内容脚本中为源启用源试用。

部分功能可能还需要 API 权限。如需了解详情，请参阅特定试用版的文档。

如需查看是否已启用试用版，请在检查 chrome-extension:// 架构页面时，查看开发者工具中“应用”面板的 Frames > Top 标签页。

内容脚本会在注入到的网页情境中运行，而不是在扩展程序源代码中运行。因此，即使您已向扩展程序清单添加令牌，内容脚本中也不会启用 Web 功能的源试用。

请改为在创建试用令牌时选择第三方匹配选项：

您注入的来源可能未设计为在启用此来源试用版时运行。因此，请谨慎注入，并考虑这样做可能产生的影响。

**Examples:**

Example 1 (unknown):
```unknown
"trial_tokens": [
  "[TOKEN_HERE]"
]
```

Example 2 (javascript):
```javascript
const otMeta = document.createElement('meta');
otMeta.httpEquiv = 'origin-trial';
otMeta.content = 'TOKEN_GOES_HERE';
document.head.append(otMeta);
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started

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
REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.my_company.my_application" /ve /t REG_SZ /d "C:\path\to\nmh-manifest.json" /f
```

Example 3 (unknown):
```unknown
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\com.my_company.my_application]
@="C:\\path\\to\\nmh-manifest.json"
```

Example 4 (unknown):
```unknown
var port = chrome.runtime.connectNative('com.my_company.my_application');
port.onMessage.addListener(function (msg) {
  console.log('Received' + msg);
});
port.onDisconnect.addListener(function () {
  console.log('Disconnected');
});
port.postMessage({text: 'Hello, my_application'});
```

---

## 消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/messaging?hl=zh-cn

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

## chrome.devtools.recorder 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/devtools_recorder?hl=zh-cn

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

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/declarativeNetRequest?hl=zh-cn

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

## chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/webNavigation?hl=zh-cn

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

## 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/cross-origin-isolation?hl=zh-cn

**Contents:**
- 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

跨源隔离使网页能够使用 SharedArrayBuffer 等强大功能。扩展程序可以通过为 cross_origin_embedder_policy 和 cross_origin_opener_policy 清单键指定适当的值来选择启用跨源隔离。例如，以下清单会将扩展程序的来源选择加入跨源隔离。

选择启用跨域隔离后，扩展程序便可在其跨域隔离的情境中使用 SharedArrayBuffers 等强大的 API。不过，它也会带来一些副作用。如需了解详情，请参阅使用 COOP 和 COEP 使您的网站“跨源隔离”。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "CrossOriginIsolation example",
  "manifest_version": 3,
  "version": "1.1",
  "cross_origin_embedder_policy": {
    "value": "require-corp"
  },
  "cross_origin_opener_policy": {
    "value": "same-origin"
  },
  ...
}
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/ai

**Contents:**
  - 扩展程序和 AI
  - 利用 AI 赋能的扩展程序提升浏览体验
    - 控制 Web 内容
    - 让浏览器更实用
    - 自定义浏览器
  - 使用 Gemini 构建 AI 赋能的 Chrome 扩展程序
  - 更多用例
- 将 AI 与扩展程序集成
  - 客户端 AI
  - Cloud AI

---

## 消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/messaging

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

## 使用 WebUSB 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/webusb?hl=zh-cn

**Contents:**
- 使用 WebUSB 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的可用性
- 权限
- 清单
- 支持的上下文
- Chrome 扩展程序差异

WebUSB API 可将非标准通用串行总线 (USB) 兼容设备公开到网络。本页介绍了扩展程序专有的 API 方面。如需了解 WebUSB API 的完整详情，请参阅 MDN。

不需要清单文件权限；但 WebUSB 会触发浏览器的用户权限流程。

此 API 几乎可在任何上下文中使用；WebUSB.requestDevice() 方法无法在扩展程序服务工作器中使用。有关详情，请参见下文。

在扩展程序 Service Worker 中使用此 API 时，设备连接会话会使 Service Worker 保持活跃状态。

虽然 WebUSB 可供扩展程序 Service Worker 使用，但无法在扩展程序 Service Worker 中调用 WebUSB.requestDevice()，它会返回使用 USBDevice 实例进行解析的 promise。如需解决此问题，请从扩展程序页面（而非扩展程序服务 worker）调用 requestDevice()，并向扩展程序服务 worker 发送消息。

以下代码遵循典型模式，在需要用户手势的权限流程中调用 requestDevice()。获取设备后，它会向 Service Worker 发送消息，然后 Service Worker 可以使用 getDevices() 检索设备。

**Examples:**

Example 1 (javascript):
```javascript
myButton.addEventListener("click", async () => {
  await navigator.usb.requestDevice({
    filters: [{ vendorId: 0x1234, productId: 0x5678 }],
  });
  chrome.runtime.sendMessage("newDevice");
});
```

Example 2 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message === "newDevice") {
    const devices = await navigator.usb.getDevices();
    for (const device of devices) {
      // open device connection.
      await device.open();
    }
  }
});
```

---

## chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/alarms

**Contents:**
- chrome.alarms 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
- 示例
  - 设置闹钟
  - 响应闹钟
- 类型
  - Alarm
    - 属性

使用 chrome.alarms API 安排代码在指定时间或未来某个时间定期运行。

如需使用 chrome.alarms API，请在清单中声明 "alarms" 权限：

以下示例展示了如何使用和响应闹钟。如需试用此 API，请从 chrome-extension-samples 代码库中安装 Alarm API 示例。

以下示例在安装扩展程序时在 Service Worker 中设置闹钟：

以下示例根据响铃闹钟的名称设置操作工具栏图标。

如果不为 null，则表示闹钟为重复闹钟，将在 periodInMinutes 分钟后再次触发。

相应闹钟计划触发的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。出于性能方面的考虑，闹钟可能会延迟任意时长。

onAlarm 事件应触发的时间长度（以分钟为单位）。

如果设置了该值，则在 when 或 delayInMinutes 指定的初始事件之后，每隔 periodInMinutes 分钟应触发一次 onAlarm 事件。如果未设置，闹钟将仅响铃一次。

闹钟应响铃的时间，以自纪元以来的毫秒数表示（例如 Date.now() + n）。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

创建闹钟。在 alarmInfo 指定的时间附近，系统会触发 onAlarm 事件。如果存在另一个同名（或未指定名称）的闹钟，则该闹钟将被取消并替换为此闹钟。

为了减轻用户机器的负载，Chrome 将闹钟限制为最多每 30 秒响一次，但可能会将闹钟延迟任意时长。也就是说，如果将 delayInMinutes 或 periodInMinutes 设置为小于 0.5 的值，系统将不会接受该值，并会发出警告。when 可以设置为“现在”之后的不到 30 秒，而不会发出警告，但实际上至少要过 30 秒才会触发闹钟。

为了帮助您调试应用或扩展程序，当您以未打包的方式加载应用或扩展程序时，闹钟的触发频率不受限制。

用于标识相应闹钟的可选名称。默认为空字符串。

描述闹钟应在何时响铃。必须通过 when 或 delayInMinutes（但不能同时通过两者）指定初始时间。如果设置了 periodInMinutes，闹钟会在初始事件发生后每隔 periodInMinutes 分钟重复一次。如果未为重复闹钟设置 when 或 delayInMinutes，则 periodInMinutes 会用作 delayInMinutes 的默认值。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

Promise<Alarm | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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

Example 3 (javascript):
```javascript
chrome.alarms.onAlarm.addListener((alarm) => {
  chrome.action.setIcon({
    path: getIconPath(alarm.name),
  });
});
```

Example 4 (unknown):
```unknown
chrome.alarms.clear(  name?: string,  callback?: function,): Promise<boolean>
```

---

## 保护用户隐私 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/security-privacy/user-privacy

**Contents:**
- 保护用户隐私 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 减少所需权限
  - activeTab
- 选择授予可选权限
- 限制和保护用户信息
- 正在节省数据流量和无痕模式

如果扩展程序侵犯用户隐私或要求用户提供更多必要的权限，则用户不会安装该扩展程序。向用户提出的权限请求必须合理，且仅限于实施扩展程序所需的关键信息。收集或传输任何用户数据的扩展程序都必须遵守保护用户隐私下的政策。

采取这些预防措施来保护并尊重扩展程序用户的身份信息。

扩展程序可以访问的 API 在清单的 permissions 字段中指定。授予的权限越多，攻击者拦截信息的途径就越多。应仅列出扩展程序所依赖的 API，并考虑使用侵入性较低的选项。扩展程序请求的权限越少，向用户显示的权限警告就越少。用户更有可能安装收到有限警告的扩展程序。

扩展程序不应“满足未来需求”通过请求用户目前不需要但将来可能会实现的权限来访问用户数据。通过扩展程序更新添加新权限，并考虑将其设为可选权限。

使用主机权限注入脚本的扩展程序通常可以改用 activeTab。activeTab 权限将仅在用户调用扩展程序时，授予扩展程序对当前活动标签页的临时访问权限。当用户离开或关闭当前标签页时，访问权限会被切断。它可以作为 <all_urls> 的许多用途的替代方案。

在安装过程中，activeTab 权限不会显示警告消息。

通过添加可选权限，让用户能够选择自己需要的扩展程序功能和权限。如果某个功能对扩展程序的核心功能而言并不是至关重要的，请将其设为可选，并将相应 API 或网域移至 optional_permissions 字段。

添加可选权限可让扩展程序说明其需要特定权限的原因 当用户启用相关功能时触发。该扩展程序可以为用户提供一个启用 功能。

点击 Ok! 将在 Service Worker 中触发以下事件。

可选权限也可以在扩展程序更新中实现。这样做会创建新的 用户无需停用扩展程序即可使用这项功能，因为使用新版 Chrome 更新 所需权限。

请仅请求扩展程序所需的最少数据量。扩展程序向用户索取的信息越少，在扩展程序遭到入侵后，曝光率也越低。

应谨慎处理所请求的所有用户数据。在安全的服务器上存储和检索数据： 注册域名。始终使用 HTTPS 连接，并避免将敏感用户数据保留在客户端中 因为扩展程序存储未加密。

扩展程序可以使用 storage API 或通过发出 省数据当扩展程序需要保存内容时，请先考虑保存的内容是否来自 隐身窗口。默认情况下，扩展程序不会在无痕式窗口中运行。

无痕模式会保证该窗口不会留下任何痕迹。当处理来自 无痕式窗口，扩展程序应遵守这一承诺。如果扩展程序通常会保存浏览数据 历史记录，不保存无痕式窗口中的历史记录。不过，扩展程序可以存储设置 设置。

要检测某个窗口是否处于无痕模式，请检查相关窗口的 incognito 属性， tabs.Tab 或 windows.Window 对象。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 2 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  ...
  "optional_permissions": [ "tabs", ],
  "optional_host_permissions": ["https://www.google.com/" ],
  ...
}
```

Example 3 (javascript):
```javascript
chrome.action.onClicked.addListener((event) => {
  // Permissions must be requested from inside a user gesture, like a button's
  // click handler.
  chrome.permissions.request(
    {
      permissions: ["tabs", "scripting"],
      origins: ['https://www.google.com/']
    },
    function (granted) {
      // The callback argument will be true if the user granted the permissions.
      if (granted) {
        // doSomething();
      } else {
        // doSomethingElse();
      }
    }
  );
});
```

Example 4 (unknown):
```unknown
function saveTabData(tab) {
  if (tab.incognito) {
    return;
  } else {
    chrome.storage.local.set({data: tab.url});
  }
}
```

---

## 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/content-scripts

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

## chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/devtools/network

**Contents:**
- chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概览
- 示例
- 类型
  - Request
    - 属性
- 方法
  - getHAR()

使用 chrome.devtools.network API 检索由开发者工具在“Network”面板中显示的网络请求的相关信息。

必须在清单中声明以下键才能使用此 API。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

网络请求信息以 HTTP 归档格式 (HAR) 表示。以下各项的说明： HAR 不在本文档的介绍范围内，请参阅 HAR v1.2 规范。

对于 HAR，chrome.devtools.network.getHAR() 方法会返回整个 HAR 日志，而 chrome.devtools.network.onRequestFinished 事件提供 HAR 条目作为事件的参数 回调。

请注意，出于效率方面的原因，请求内容未包含在 HAR 中。您可以拨打 请求的 getContent() 方法来检索内容。

如果在网页加载后打开“开发者工具”窗口， 由 getHAR() 返回的条目数组。请重新加载页面以获取所有请求。一般来说， getHAR() 返回的请求列表应与“Network”面板中显示的请求列表一致。

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

## chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/contextMenus

**Contents:**
- chrome.contextMenus 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 用法
- 清单
- 示例
- 类型
  - ContextType
    - 枚举
  - CreateProperties

使用 chrome.contextMenus API 可向 Google Chrome 的上下文菜单添加项。您可以选择上下文菜单添加项所适用的对象类型，例如图片、超链接和网页。

上下文菜单项可以显示在任何文档（或文档中的框架）中，即使是具有 file:// 或 chrome:// 网址的文档也不例外。如需控制您的项可以显示在哪些文档中，请在调用 create() 或 update() 方法时指定 documentUrlPatterns 字段。

您可以根据需要创建任意数量的上下文菜单项，但如果您的扩展程序中有多个上下文菜单项同时显示，Google Chrome 会自动将它们收起到一个父菜单中。

您必须在扩展程序的清单中声明“contextMenus”权限，才能使用该 API。此外，您还应指定一个 16x16 像素的图标，以便在菜单项旁边显示。例如：

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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

要更新的属性。接受与 contextMenus.create 函数相同的值。

[ContextType, ...ContextType[]] 可选

要设为相应商品父级的商品的 ID。注意：您无法将某个项目设置为其自身后代的子项。

发生点击的标签页的详细信息。平台应用没有此参数。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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
chrome.contextMenus.remove(  menuItemId: string | number,  callback?: function,): Promise<void>
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

## 使用 Puppeteer 测试 Chrome 扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/puppeteer?hl=zh-cn

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

## chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/devtools/inspectedWindow

**Contents:**
- chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概览
- 在检查窗口中执行代码
- 示例
- 类型
  - Resource
    - 属性
- 属性

使用 chrome.devtools.inspectedWindow API 与检查的窗口进行交互：获取被检查页面的标签页 ID、在被检查的窗口中评估代码、重新加载页面或者获取页面中的资源列表。

必须在清单中声明以下键才能使用此 API。

使用 chrome.devtools.inspectedWindow 与检查的窗口进行交互：获取用于 在检查窗口中评估代码、重新加载页面或获取 该页面内的资源列表。

有关使用开发者工具 API 的一般说明，请参阅 DevTools API 摘要。

tabId 属性提供可与 chrome.tabs.* 一起使用的标签页标识符 API 调用。但请注意，chrome.tabs.* API 不会提供给开发者工具 扩展程序网页 - 您需要将标签页 ID 传递到后台 页面并从中调用 chrome.tabs.* API 函数。

reload 方法可用于重新加载被检查的网页。此外，调用方还可以指定 用户代理字符串的替换值、在网页加载时提前注入的脚本，或 用于强制重新加载缓存资源的选项。

使用 getResources 调用和 onResourceContent 事件获取资源列表 （文档、样式表、脚本、图片等）。getContent 和 Resource 类的 setContent 方法以及 onResourceContentCommitted 事件可以 可用于支持资源内容的修改，例如由外部编辑者修改。

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

如果错误发生在对表达式求值之前，开发者工具端出现，就设置此字段。

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

## chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/declarativeContent

**Contents:**
- chrome.declarativeContent 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 用法
- 规则
- 网页网址匹配
- CSS 匹配
- 书签状态匹配
- 类型
  - ImageDataType

使用 chrome.declarativeContent API 可根据网页内容执行操作，而无需读取网页内容的权限。

声明式 Content API 可让您根据 或者 CSS 选择器与页面上的某个元素匹配，无需 添加主机权限或注入内容脚本。

使用 activeTab 权限，以在用户点击 操作。

规则由条件和操作组成。如果满足任一条件，则所有操作 。这些操作包括 setIcon 和 showAction。

当且仅当所有网页都列出时，PageStateMatcher 才与网页匹配 条件。可与网页网址、CSS 复合选择器匹配 或网页的已添加书签状态。以下规则启用 当有密码字段存在时，扩展程序在 Google 网页上执行的操作：

如果还要为包含视频的 Google 网站启用该扩展程序的操作， 条件，因为每个条件足以触发所有指定操作：

onPageChanged 事件测试是否有任何规则至少满足一条规则 条件并执行操作。浏览会话时，规则会保留下来；因此，在 则首先应使用 removeRules 清除 然后使用 addRules 注册新的规则。

如果有 activeTab 权限，您的扩展程序将不会显示任何权限 警告，并且当用户点击该扩展程序操作时，该扩展程序只会在相关网页上运行。

当满足网址条件时，PageStateMatcher.pageurl 即为匹配。通过 最常见的条件是主机、路径或网址串联，后接包含、等于、前缀或 后缀。下表包含几个示例：

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

## 使用 WebUSB 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/webusb

**Contents:**
- 使用 WebUSB 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的可用性
- 权限
- 清单
- 支持的上下文
- Chrome 扩展程序差异

WebUSB API 可将非标准通用串行总线 (USB) 兼容设备公开到网络。本页介绍了扩展程序专有的 API 方面。如需了解 WebUSB API 的完整详情，请参阅 MDN。

不需要清单文件权限；但 WebUSB 会触发浏览器的用户权限流程。

此 API 几乎可在任何上下文中使用；WebUSB.requestDevice() 方法无法在扩展程序服务工作器中使用。有关详情，请参见下文。

在扩展程序 Service Worker 中使用此 API 时，设备连接会话会使 Service Worker 保持活跃状态。

虽然 WebUSB 可供扩展程序 Service Worker 使用，但无法在扩展程序 Service Worker 中调用 WebUSB.requestDevice()，它会返回使用 USBDevice 实例进行解析的 promise。如需解决此问题，请从扩展程序页面（而非扩展程序服务 worker）调用 requestDevice()，并向扩展程序服务 worker 发送消息。

以下代码遵循典型模式，在需要用户手势的权限流程中调用 requestDevice()。获取设备后，它会向 Service Worker 发送消息，然后 Service Worker 可以使用 getDevices() 检索设备。

**Examples:**

Example 1 (javascript):
```javascript
myButton.addEventListener("click", async () => {
  await navigator.usb.requestDevice({
    filters: [{ vendorId: 0x1234, productId: 0x5678 }],
  });
  chrome.runtime.sendMessage("newDevice");
});
```

Example 2 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message === "newDevice") {
    const devices = await navigator.usb.getDevices();
    for (const device of devices) {
      // open device connection.
      await device.open();
    }
  }
});
```

---

## chrome.i18n 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/i18n?hl=zh-cn

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

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/samples?text=override&hl=zh-cn

**Contents:**
  - 示例

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/

**Contents:**
  - 欢迎使用扩展程序！
  - 扩展程序和 AI
    - Chrome 扩展程序中的 Prompt API
    - AI 赋能的扩展程序示例
    - 早期预览版计划
    - 加入 内置 AI 挑战
  - 新功能
    - 视频：解答有关 Chrome 应用商店可发现性的问题
    - 新指南：说明扩展程序更新周期
    - Chrome 140：新的 `sidePanel.getLayout()` API

---

## chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/enterprise/platformKeys

**Contents:**
- chrome.enterprise.platformKeys 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 用法
- 类型
  - Algorithm
    - 枚举
  - ChallengeKeyOptions
    - 属性

使用 chrome.enterprise.platformKeys API 生成密钥并为这些密钥安装证书。这些证书将由平台管理，可用于 TLS 身份验证、网络访问或通过 chrome.platformKeys 由其他扩展程序使用。

使用此 API 注册客户端证书的典型步骤如下：

使用 enterprise.platformKeys.getTokens 获取所有可用令牌。

查找 id 等于 "user" 的令牌。随后使用此令牌。

使用 generateKey Token 方法（在 SubtleCrypto 中定义）生成密钥对。这将返回密钥的句柄。

使用 exportKey 令牌方法（在 SubtleCrypto 中定义）导出公钥。

使用 sign Token 方法（在 SubtleCrypto 中定义）创建认证请求数据的签名。

如果收到证书，请使用 enterprise.platformKeys.importCertificate 导入证书

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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

对由硬件支持的企业机器密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业设备政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证功能发出的任何设备身份都与当前设备的硬件紧密绑定。此函数受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业设备政策未明确为调用方启用此操作，则此函数将失败。企业机器密钥不位于 "system" 令牌中，并且无法通过任何其他 API 进行访问。

由 Verified Access Web API 发出的质询。

如果已设置，则当前企业机器密钥会注册为 "system" 令牌，并放弃企业机器密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业机器密钥。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

对硬件支持的企业用户密钥发起质询，并根据远程证明协议发出响应。仅在 ChromeOS 上有用，并且需要与 Verified Access Web API 结合使用，该 API 既会发出质询，也会验证响应。如果经过验证的访问权限 Web API 成功验证，则强烈表明以下所有情况：* 当前设备是合法的 ChromeOS 设备。* 当前设备由验证期间指定的网域管理。* 当前登录的用户由验证期间指定的网域管理。* 当前设备状态符合企业用户政策。例如，某项政策可能规定设备不得处于开发者模式。* 验证所发出的公钥与当前设备的硬件和当前登录用户紧密绑定。此功能受到严格限制，如果当前设备不受管理、当前用户不受管理，或者企业用户政策未明确为调用方启用此操作，则此功能将失败。企业用户密钥不位于 "user" 令牌中，任何其他 API 都无法访问该密钥。

由 Verified Access Web API 发出的质询。

如果设置，则当前企业用户密钥会注册到 "user" 令牌，并放弃企业用户密钥角色。然后，该密钥可以与证书相关联，并像任何其他签名密钥一样使用。此密钥为 2048 位 RSA 密钥。随后对该函数的调用将生成新的企业用户密钥。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回指定令牌中的所有可用客户端证书的列表。可用于检查可用于特定身份验证的客户端证书是否存在以及是否过期。

证书列表，每个证书都采用 X.509 证书的 DER 编码。

Promise<ArrayBuffer[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回可用令牌。在常规用户的会话中，该列表将始终包含用户的令牌，且该令牌具有 id "user"。如果存在系统级 TPM token，则返回的列表还将包含具有 id "system" 的系统级 token。对于相应设备（例如 Chromebook）上的所有会话，系统级令牌都将相同。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

如果认证密钥已存储在相应令牌中，则将 certificate 导入到相应令牌。成功发出认证请求后，应使用此函数存储获得的证书，并使其可供操作系统和浏览器用于身份验证。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

从给定令牌中移除 certificate（如果存在）。应使用此方法移除过时的证书，以免在身份验证期间考虑这些证书，并避免证书选择过程过于杂乱。应使用此方法释放证书存储区中的存储空间。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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
chrome.enterprise.platformKeys.challengeKey(  options: ChallengeKeyOptions,  callback?: function,): Promise<ArrayBuffer>
```

Example 3 (javascript):
```javascript
(response: ArrayBuffer) => void
```

Example 4 (unknown):
```unknown
chrome.enterprise.platformKeys.challengeMachineKey(  challenge: ArrayBuffer,  registerKey?: boolean,  callback?: function,): Promise<ArrayBuffer>
```

---

## 示例 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/samples?hl=zh-cn

**Contents:**
- 示例 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

GitHub 上提供了 Chrome 扩展程序的示例。

---

## 确保安全 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/security-privacy/stay-secure

**Contents:**
- 确保安全 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保护开发者账号
  - 选择性地创建群组
- 永不使用 HTTP
- 请求最小权限
  - 跨源 fetch()
- 限制清单字段
  - 可从外部连接
  - 可通过网络访问的资源
- 添加明确的内容安全政策

扩展程序在浏览器中获得特殊权限，因此成为攻击者的理想目标。如果某个扩展程序遭到入侵，该扩展程序的所有用户都可能会受到恶意和不必要的入侵。通过采用以下做法，确保扩展程序的安全性并保护其用户。

扩展程序代码需通过 Google 账号上传和更新。如果开发者的账号遭到入侵，攻击者可能会直接向所有用户推送恶意代码。请启用双重验证（最好使用安全密钥）来保护这些账号。

如果使用群组发布功能，请将群组成员仅限于可信开发者。请勿接受不明身份人员提出的加入申请。

请求或发送数据时，请避免使用 HTTP 连接。假设任何 HTTP 连接都会有窃听者或包含修改内容。应始终优先使用 HTTPS，因为它具有内置的安全功能，可规避大多数中间人攻击。

Chrome 浏览器会限制扩展程序对在manifest中明确请求的权限的访问权限。扩展程序应仅注册其依赖的 API 和网站，从而最大限度地减少其权限。

限制扩展程序的权限可限制潜在攻击者可以利用的功能。

扩展程序只能使用 fetch() 和 XMLHttpRequest() 从扩展程序以及权限中指定的网域获取资源。请注意，对这两者的调用会被 Service Worker 中的 fetch 处理程序拦截。

上面示例中的扩展程序在权限中列出了 "https://developer.chrome.com/*" 和 "https://*.google.com/*"，以请求访问 developer.chrome.com 和 Google 子网域上的所有内容。即使扩展程序遭到入侵，它仍然只能与符合匹配模式的网站互动。攻击者只能有限地访问 "https://user_bank_info.com" 或与 "https://malicious_website.com" 互动。

在清单中添加不必要的密钥和权限会导致漏洞，并使扩展程序更易于检测。将清单字段限制为扩展程序依赖的字段。

使用 "externally_connectable" 字段声明该扩展程序将与哪些外部扩展程序和网页交换信息。限制扩展程序可以与哪些可信来源进行外部连接。

在 "web_accessible_resources" 下使资源可供 Web 访问，会导致网站和攻击者能够检测到扩展程序。

可通过网络访问的资源越多，潜在攻击者可以利用的途径就越多。请尽量减少这些文件。

在清单中为扩展程序添加内容安全政策，以防范跨网站脚本攻击。如果扩展程序仅从自身加载资源，请注册以下内容：

如果扩展程序需要使用 Web Assembly，或需要对沙盒化网页增加限制，可以通过以下方式添加：

虽然使用 document.write() 和 innerHTML 动态创建 HTML 元素可能更简单，但这会使扩展程序及其依赖的网页容易受到攻击者插入恶意脚本的攻击。请改为手动创建 DOM 节点，然后使用 innerText 插入动态内容。

虽然内容脚本位于隔离的世界中，但也并非完全不受攻击：

使用敏感数据（例如用户的私密信息）或有权访问浏览器功能的 Chrome API 的操作应在扩展程序的服务工件中执行。避免意外向内容脚本泄露扩展程序权限：

通过将监听器限制为仅监听扩展程序预期的内容、验证传入数据的发送方以及对所有输入进行排错，保护扩展程序免受恶意脚本的侵害。

只有在预期收到来自外部网站或扩展程序的通信时，扩展程序才应注册 runtime.onMessageExternal。始终验证发件人是否与受信任的来源匹配。

即使是扩展程序本身通过 runtime.onMessage 事件发送的消息，也应仔细检查，以确保 MessageSender 不是来自已遭到入侵的内容脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "host_permissions": [
    "https://developer.chrome.com/*",
    "https://*.google.com/*"
  ],
  "manifest_version": 3
}
```

Example 2 (unknown):
```unknown
{
  "name": "Super Safe Extension",
  "externally_connectable": {
    "ids": [
      "iamafriendlyextensionhereisdatas"
    ],
    "matches": [
      "https://developer.chrome.com/*",
      "https://*.google.com/*"
    ],
    "accepts_tls_channel_id": false
  },
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
    }
  ]
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
   "content_security_policy": {
    "extension_pages": "default-src 'self'"
  },
  "manifest_version": 3
}
```

---

## chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/cookies?hl=zh-cn

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

## chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/bookmarks

**Contents:**
- chrome.bookmarks 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检索指定的 BookmarkTreeNode。

字符串 | [字符串, ...字符串 []]

单个字符串值 ID 或字符串值 ID 数组

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检索指定 BookmarkTreeNode ID 的子级。

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检索书签层次结构的一部分，从指定节点开始。

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

将指定的 BookmarkTreeNode 移动到提供的位置。

Promise<BookmarkTreeNode>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

搜索与给定查询匹配的 BookmarkTreeNodes。使用对象指定的查询会生成与所有指定属性匹配的 BookmarkTreeNodes。

一个字符串（包含与书签网址和标题匹配的字词和带引号的短语）或一个对象。如果为对象，则可以指定属性 query、url 和 title，系统将生成与所有指定属性匹配的书签。

一个字符串，包含要与书签网址和标题进行匹配的字词和带引号的短语。

书签的网址；完全匹配。请注意，文件夹没有网址。

Promise<BookmarkTreeNode[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

更新书签或文件夹的属性。仅指定要更改的属性；未指定的属性将保持不变。注意：目前仅支持“title”和“url”。

Promise<BookmarkTreeNode>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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
chrome.bookmarks.create(  bookmark: CreateDetails,  callback?: function,): Promise<BookmarkTreeNode>
```

---

## chrome.tabs 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/tabs?hl=zh-cn

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

## 将 Firebase Cloud Messaging (FCM) 与 chrome.gcm 搭配使用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/chrome.gcm?hl=zh-cn

**Contents:**
- 将 Firebase Cloud Messaging (FCM) 与 chrome.gcm 搭配使用 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前提条件
- 配置 chrome.gcm
- 监听消息
- 不使用 Firebase 的 Firebase
- 针对频道和主题

您可以通过以下应用向最终用户发送和接收消息： chrome.gcm。因为它是基于 Firebase Cloud Messaging (FCM)，它依赖于您需要的外部服务 进行设置。本方法指南将引导您完成获取该工具的所有必要步骤 。

虽然 chrome.gcm 仍受支持，但它是十多年前创建的 推送标准一般来说，最好的做法始终是 标准 API，而不是扩展程序专用的 API。除非您有特定需求 要使用 chrome.gcm，我们建议使用推送。

如需使用 chrome.gcm，您需要设置 Firebase 。

创建账号后，您需要打开 Firebase 控制台，然后选择要使用的现有项目，或创建一个新项目 。

继续前往 Cloud Messaging 的设置页面。

如果您已经拥有此项目的云消息传递账号，则需要 复制列出的发送者 ID（用数字表示）。

如果未启用云消息传递，则需要启用 Firebase Google Cloud 内部项目的 Cloud Messaging API。在以下 您可以看到 Firebase 中此页面的 设置。

启用后，返回 Cloud 的设置页面 发送消息，然后复制发送者 ID。

现在您已从 Firebase 获得发送者 ID，接下来可以配置扩展程序了 监听消息。首先，请确保您已添加 gcm 对您的扩展程序的 manifest.json 的权限

您现在可以访问 chrome.gcm API 了。您可以注册监听推送消息 通过调用 chrome.gcm.register 发送的消息

扩展程序注册发送者 ID 后，您需要添加代码来处理 消息。

虽然 chrome.gcm 始终通过 Firebase 运行，但 Firebase 可以配置为 充当外部推送消息传递供应商的代理。通常情况下，供应商会 明确列出了对 Chrome 扩展程序的支持， Firebase 的旧版推送通知应该正常运行。如果您的提供商列出 支持 Firebase 的旧版推送通知，欢迎体验一下。如果您遇到 提供商支持人员应能够澄清 应用场景

chrome.gcm 使用的是旧版 Firebase Messaging API。这很重要 因为旧版 API 不支持消息通道。每封邮件 将传送到每个客户端如果用户的扩展程序只对 部分邮件，您需要自行进行过滤。

Firebase 最初是作为免费账号使用，但超出配额后，您需要 特定使用量阈值。如果您打算向特定群组发送邮件 那么客户端过滤功能最终所耗费的成本可能会超过预期您可以 为了解决这个问题，可以创建多个项目来复制各个渠道 （每个渠道一个项目和一个发送者 ID）。任何给定的扩展程序都可以 注册多个发送者 ID（最多 100 个）。

或者，如果您需要频道支持，或者想要使用推送通知 您可以使用 Push API。

**Examples:**

Example 1 (unknown):
```unknown
{
    "manifest_version": 3,
    ...
    "permissions": ["gcm"]
```

---

## 权限警告准则 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/permission-warnings?hl=zh-cn

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

## 使用 Puppeteer 测试 Service Worker 的终止情况 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/test-serviceworker-termination-with-puppeteer?hl=zh-cn

**Contents:**
- 使用 Puppeteer 测试 Service Worker 的终止情况 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前期准备
- 第 1 步：启动 Node.js 项目
- 第 2 步：安装依赖项
- 第 3 步：编写基本测试
- 第 4 步：终止 Service Worker
- 第 5 步：运行测试
- 第 6 步：修复 Service Worker
- 第 7 步：再次运行测试
- 后续步骤

本指南介绍了如何通过测试服务构建更强大的扩展程序 使用 Puppeteer 终止工作器。已做好随时处理账号终止的准备 时间很重要，因为这可能会在没有警告的情况下 发生，导致 Service Worker。因此，扩展程序必须保存重要的状态和 如果存在以下情况，则能够在再次启动后立即处理请求： 事件进行处理。

克隆或下载 chrome-extensions-samples 代码库。 我们将在 /functional-samples/tutorial.terminate-sw/test-extension：用于发送消息 向 Service Worker 发送一个按钮并将文本添加到页面 如果收到响应。

您还需要安装 Node.JS，这是 Puppeteer 的构建运行时。

在新目录中创建以下文件。它们共同创造了 Node.js 项目并提供 Puppeteer 测试套件的基本结构 使用 Jest 作为测试运行程序。如需详细了解此设置，请参阅使用 Puppeteer 测试 Chrome 扩展程序。

请注意，我们的测试会从示例代码库加载 test-extension。chrome.runtime.onMessage 的处理脚本依赖于 chrome.runtime.onInstalled 事件处理脚本中设置的状态。因此，当服务工件终止时，data 的内容将丢失，并且无法响应任何未来的消息。我们会在编写测试后解决此问题。

service-worker-broken.js:

运行 npm install 以安装所需的依赖项。

将以下测试添加到 index.test.js 的底部。开始测试 页面中，点击按钮元素并等待响应 从 Service Worker 加载。

您可以使用 npm start 运行测试，并且应该会看到测试成功完成。

添加以下可终止 Service Worker 的辅助函数：

最后，使用以下代码更新您的测试。现在，终止服务工作器，然后再次点击该按钮，检查您是否收到了响应。

运行 npm start。您的测试应该会失败，这表示服务工件在终止后未响应。

接下来，通过取消对临时状态的依赖来修复 Service Worker。更新 测试扩展程序以使用存储在 代码库中的 service-worker-fixed.js。

service-worker-fixed.js：

在这里，我们将版本保存到 chrome.storage.local，而不是全局变量 在 Service Worker 的生命周期之间保留状态。由于只能异步访问存储空间，因此我们还会从 onMessage 监听器返回 true，以确保 sendResponse 回调保持活跃状态。

使用 npm start 再次运行测试。现在它应该会通过。

现在，您可以将相同的方法应用于自己的扩展程序。请考虑以下事项：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "puppeteer-demo",
  "version": "1.0",
  "dependencies": {
    "jest": "^29.7.0",
    "puppeteer": "^24.8.1"
  },
  "scripts": {
    "start": "jest ."
  },
  "devDependencies": {
    "@jest/globals": "^29.7.0"
  }
}
```

Example 2 (javascript):
```javascript
const puppeteer = require('puppeteer');

const SAMPLES_REPO_PATH = 'PATH_TO_SAMPLES_REPOSITORY';
const EXTENSION_PATH = `${SAMPLES_REPO_PATH}/functional-samples/tutorial.terminate-sw/test-extension`;
const EXTENSION_ID = 'gjgkofgpcmpfpggbgjgdfaaifcmoklbl';

let browser;

beforeEach(async () => {
  browser = await puppeteer.launch({
    // Set to 'new' to hide Chrome if running as part of an automated build.
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

Example 3 (javascript):
```javascript
let data;

chrome.runtime.onInstalled.addListener(() => {
  data = { version: chrome.runtime.getManifest().version };
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  sendResponse(data.version);
});
```

Example 4 (javascript):
```javascript
test('can message service worker', async () => {
  const page = await browser.newPage();
  await page.goto(`chrome-extension://${EXTENSION_ID}/page.html`);

  // Message without terminating service worker
  await page.click('button');
  await page.waitForSelector('#response-0');
});
```

---

## 获取 Chrome 扩展程序方面的帮助 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/get-help

**Contents:**
- 获取 Chrome 扩展程序方面的帮助 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 用于扩展程序开发
- 对于 Chrome 应用商店

我们会尽力改进本网站和 Chrome 应用商店帮助的内容。部分用户可能会遇到我们未涵盖的问题。幸运的是，您还可以通过其他方式获得帮助。

如果您在 Chrome 应用商店账号或商品方面遇到问题，请访问我们的一站式支持页面寻求帮助。

---

## chrome.history 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/history/?hl=zh-cn

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

## 确保安全 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/security-privacy/stay-secure?hl=zh-cn

**Contents:**
- 确保安全 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 保护开发者账号
  - 选择性地创建群组
- 永不使用 HTTP
- 请求最小权限
  - 跨源 fetch()
- 限制清单字段
  - 可从外部连接
  - 可通过网络访问的资源
- 添加明确的内容安全政策

扩展程序在浏览器中获得特殊权限，因此成为攻击者的理想目标。如果某个扩展程序遭到入侵，该扩展程序的所有用户都可能会受到恶意和不必要的入侵。通过采用以下做法，确保扩展程序的安全性并保护其用户。

扩展程序代码需通过 Google 账号上传和更新。如果开发者的账号遭到入侵，攻击者可能会直接向所有用户推送恶意代码。请启用双重验证（最好使用安全密钥）来保护这些账号。

如果使用群组发布功能，请将群组成员仅限于可信开发者。请勿接受不明身份人员提出的加入申请。

请求或发送数据时，请避免使用 HTTP 连接。假设任何 HTTP 连接都会有窃听者或包含修改内容。应始终优先使用 HTTPS，因为它具有内置的安全功能，可规避大多数中间人攻击。

Chrome 浏览器会限制扩展程序对在manifest中明确请求的权限的访问权限。扩展程序应仅注册其依赖的 API 和网站，从而最大限度地减少其权限。

限制扩展程序的权限可限制潜在攻击者可以利用的功能。

扩展程序只能使用 fetch() 和 XMLHttpRequest() 从扩展程序以及权限中指定的网域获取资源。请注意，对这两者的调用会被 Service Worker 中的 fetch 处理程序拦截。

上面示例中的扩展程序在权限中列出了 "https://developer.chrome.com/*" 和 "https://*.google.com/*"，以请求访问 developer.chrome.com 和 Google 子网域上的所有内容。即使扩展程序遭到入侵，它仍然只能与符合匹配模式的网站互动。攻击者只能有限地访问 "https://user_bank_info.com" 或与 "https://malicious_website.com" 互动。

在清单中添加不必要的密钥和权限会导致漏洞，并使扩展程序更易于检测。将清单字段限制为扩展程序依赖的字段。

使用 "externally_connectable" 字段声明该扩展程序将与哪些外部扩展程序和网页交换信息。限制扩展程序可以与哪些可信来源进行外部连接。

在 "web_accessible_resources" 下使资源可供 Web 访问，会导致网站和攻击者能够检测到扩展程序。

可通过网络访问的资源越多，潜在攻击者可以利用的途径就越多。请尽量减少这些文件。

在清单中为扩展程序添加内容安全政策，以防范跨网站脚本攻击。如果扩展程序仅从自身加载资源，请注册以下内容：

如果扩展程序需要使用 Web Assembly，或需要对沙盒化网页增加限制，可以通过以下方式添加：

虽然使用 document.write() 和 innerHTML 动态创建 HTML 元素可能更简单，但这会使扩展程序及其依赖的网页容易受到攻击者插入恶意脚本的攻击。请改为手动创建 DOM 节点，然后使用 innerText 插入动态内容。

虽然内容脚本位于隔离的世界中，但也并非完全不受攻击：

使用敏感数据（例如用户的私密信息）或有权访问浏览器功能的 Chrome API 的操作应在扩展程序的服务工件中执行。避免意外向内容脚本泄露扩展程序权限：

通过将监听器限制为仅监听扩展程序预期的内容、验证传入数据的发送方以及对所有输入进行排错，保护扩展程序免受恶意脚本的侵害。

只有在预期收到来自外部网站或扩展程序的通信时，扩展程序才应注册 runtime.onMessageExternal。始终验证发件人是否与受信任的来源匹配。

即使是扩展程序本身通过 runtime.onMessage 事件发送的消息，也应仔细检查，以确保 MessageSender 不是来自已遭到入侵的内容脚本。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "host_permissions": [
    "https://developer.chrome.com/*",
    "https://*.google.com/*"
  ],
  "manifest_version": 3
}
```

Example 2 (unknown):
```unknown
{
  "name": "Super Safe Extension",
  "externally_connectable": {
    "ids": [
      "iamafriendlyextensionhereisdatas"
    ],
    "matches": [
      "https://developer.chrome.com/*",
      "https://*.google.com/*"
    ],
    "accepts_tls_channel_id": false
  },
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
    }
  ]
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
   "content_security_policy": {
    "extension_pages": "default-src 'self'"
  },
  "manifest_version": 3
}
```

---

## chrome.declarativeWebRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/declarativeWebRequest

**Contents:**
- chrome.declarativeWebRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 规则
- 条件和操作的评估
- 使用优先级覆盖规则
- 类型
  - AddRequestCookie

注意：此 API 已废弃。不妨改用 declarativeNetRequest API。使用 chrome.declarativeWebRequest API 拦截、阻止或修改传输中的请求。它比 chrome.webRequest API 快得多，因为您可以注册在浏览器（而不是 JavaScript 引擎）中评估的规则，从而减少往返延迟时间并提高效率。

您必须声明“declarativeWebRequest”扩展程序清单中授予此权限，才能使用它 API 以及主机权限。

请注意，某些类型的非敏感操作不需要主机权限：

必须具备网络请求的所有主机的主机权限，才能执行 SendMessageToExtension() 操作 您希望根据哪个条件触发消息

例如，如果 "https://*.google.com/*" 是扩展程序具有的唯一主机权限，则此类 扩展程序可能会设置规则来：

该扩展程序无法设置将 https://www.google.com 重定向到 https://mail.google.com 的规则。

声明式 Web 请求 API 遵循声明式 API 的概念。您可以注册 为 chrome.declarativeWebRequest.onRequest 事件对象添加规则。

声明式 Web 请求 API 支持一种类型的匹配条件，即 RequestMatcher。通过 当且仅当满足列出的所有条件时，RequestMatcher 才会匹配网络请求。以下 当用户在RequestMatcherhttps://www.example.com 多功能框：

由于 scheme，RequestMatcher 会拒绝对 https://www.example.com 的请求。 此外，所有对嵌入式 iframe 的请求都会因为 resourceType 而被拒绝。

要取消对“example.com”的所有请求，您可以按如下方式定义规则：

如需取消对 example.com 和 foobar.com 的所有请求，您可以添加第二个条件， 因为每个条件足以触发所有指定的操作：

声明式网络请求 API 遵循网络请求的生命周期模型 请求 API。这意味着只能在 Web 请求的特定阶段测试条件 同样，操作只能在特定阶段执行下表列出了 与条件和操作兼容的请求阶段。

规则可以与优先级相关联，如 Events API 中所述。这种机制可以 用于表示例外情况。以下示例会屏蔽对名为 evil.jpg 的映像的所有请求 但位于服务器“myserver.com”上

请务必注意，IgnoreRules 操作在请求中不会持久保留 阶段。系统会在网络请求的每个阶段评估所有规则的所有条件。如果 已执行 IgnoreRules 操作，但它仅适用于针对同一网页执行的其他操作 Web 请求。

向请求添加 Cookie 或覆盖 Cookie，以防已存在其他同名的 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

要添加到请求的 Cookie。没有可以未定义的字段。

向响应添加一个 Cookie，如果已存在另一个同名的 Cookie，则覆盖一个 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

要添加到响应的 Cookie。必须指定名称和值。

将响应标头添加到 Web 请求的响应中。由于多个响应标头可能具有相同的名称，因此要替换一个响应标头，您需要先移除该标头，然后再添加新的响应标头。

修改一个或多个请求的 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

过滤出要修改的 Cookie。所有空条目都会被忽略。

应在构建过滤器的 Cookie 中覆盖的属性。设置为空字符串的属性会被移除。

修改一个或多个响应 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

过滤出要修改的 Cookie。所有空条目都会被忽略。

应在构建过滤器的 Cookie 中覆盖的属性。设置为空字符串的属性会被移除。

HTTP 响应中 Cookie 的过滤器。

包含 Cookie 生命周期下限（指定在当前时间之后的秒数内）。仅限失效日期时间设置为“now + ageLowerBound”的 Cookie或之后满足此条件。会话 Cookie 不符合此过滤器的条件。Cookie 生命周期通过“max-age”或“expires”Cookie 属性。如果两个都指定了，则为“max-age”计算 Cookie 生命周期。

包含 Cookie 生命周期的上限（以当前时间之后的秒数指定）。只有失效日期在 [now, now + ageUpperBound] 这一间隔内的 Cookie 才符合此条件。会话 Cookie 和有效期为过去时间的 Cookie 不符合此过滤器的条件。Cookie 生命周期通过“max-age”或“expires”Cookie 属性。如果两个都指定了，则为“max-age”计算 Cookie 生命周期。

是否存在 HttpOnly Cookie 属性。

过滤会话 Cookie。会话 Cookie 在任一“max-age”中未指定生命周期或“expires”属性。

Cookie 的值，可以用英文双引号填充。

针对各种条件的过滤器请求标头。多个条件会作为一个连接进行求值。

如果设置，系统会忽略具有指定标记的规则。这种忽略不会持久存在，它只影响同一网络请求阶段的规则及其操作。请注意，规则按其优先级的降序执行。此操作会影响优先级低于当前规则的规则。相同优先级的规则不一定会被忽略。

如果设置，系统会忽略优先级低于指定值的规则。此边界不会持久保留，它只影响同一网络请求阶段的规则及其操作。

通过在网址上应用正则表达式来重定向请求。正则表达式使用 RE2 语法。

可能包含捕获组的匹配模式。捕获组使用 Perl 语法（$1、$2, ...）而不是 RE2 语法（\1、\2...）引用，以便更接近 JavaScript 正则表达式。

将网络请求重定向到空文档的声明式事件操作。

RedirectToEmptyDocument

RedirectToEmptyDocument

将网络请求重定向到透明图片的声明性事件操作。

RedirectToTransparentImage

RedirectToTransparentImage

移除一个或多个请求的 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

过滤出将被移除的 Cookie。所有空条目都会被忽略。

移除指定名称的请求标头。请勿在同一请求中使用相同标头名称的 SetRequestHeader 和 RemoveRequestHeader。每个请求标头名称在每个请求中仅出现一次。

移除一个或多个响应 Cookie。请注意，最好使用 Cookies API，因为此 API 的计算开销较低。

过滤出将被移除的 Cookie。所有空条目都会被忽略。

HTTP 请求中 Cookie 的过滤器或规范。

Cookie 的值，可以用英文双引号填充。

如果响应的 MIME 媒体类型（来自 HTTP Content-Type 标头）包含在列表中，则匹配。

如果响应的 MIME 媒体类型（来自 HTTP Content-Type 标头）未包含在列表中，则匹配。

如果没有任何请求标头与任何 HeaderFilters 匹配，则匹配。

如果没有任何响应标头与任何 HeaderFilters 匹配，则匹配。

如果“第一方”满足 UrlFilter 的条件，则匹配请求的网址。“第一方”请求的网址（如果存在）可以与请求的目标网址不同，并说明什么是“第一方”以便进行第三方 Cookie 检查。

如果某些请求标头与其中一个 HeaderFilters 匹配，则匹配。

如果请求的请求类型包含在列表中，则匹配。与任何类型均不匹配的请求将被滤除。

如果某些响应标头与其中一个 HeaderFilters 匹配，则匹配。

包含描述阶段的字符串列表。允许的值为“onBeforeRequest”、“onBeforeSendHeaders”、“onHeadersReceived”、“onAuthRequired”。如果此属性存在，则其适用阶段仅局限于所列阶段。请注意，整个条件仅适用于与所有属性都兼容的阶段。

如果设置为 true，则匹配受第三方 Cookie 政策约束的请求。如果设置为 false，匹配所有其他请求。

如果请求的网址满足 UrlFilter 的条件，则匹配。

是否存在 HttpOnly Cookie 属性。

Cookie 的值，可以用英文双引号填充。

触发 declarativeWebRequest.onMessage 事件。

SendMessageToExtension

SendMessageToExtension

系统将在传递给事件处理脚本的字典的 message 属性中传递该值。

将指定名称的请求标头设置为指定的值。如果之前不存在具有指定名称的标头，则系统会新建一个。标头名称比较始终不区分大小写。每个请求标头名称在每个请求中仅出现一次。

"onBeforeSendHeaders"

通过声明式网络请求 API 的操作通过 declarativeWebRequest.SendMessageToExtension 发送消息时触发。

extensionTypes.DocumentLifecycle

值 0 表示请求发生在主帧中；正值表示请求发生所在的子帧的 ID。如果（子）帧的文档已加载（type 为 main_frame 或 sub_frame），则 frameId 表示此帧的 ID，而不是外帧的 ID。帧 ID 在标签页中是唯一的。

extensionTypes.FrameType

拥有此框架的父文档的 UUID。如果没有父级，则不会设置此字段。

封装发送请求的帧的帧的 ID。如果不存在父帧，则设置为 -1。

请求的 ID。请求 ID 在浏览器会话中是唯一的。因此，它们可用于将同一请求的不同事件相关联。

发生请求的标签页的 ID。如果请求与标签页无关，请将其设为 -1。

触发此信号的时间（以毫秒为单位，从 Epoch 起算）。

webRequest.ResourceType

提供由 addRules、removeRules 和 getRules 组成的声明式事件 API。

RedirectToTransparentImage

RedirectToEmptyDocument

SendMessageToExtension

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "declarativeWebRequest",
    "*://*/*"
  ],
  ...
}
```

Example 2 (unknown):
```unknown
var matcher = new chrome.declarativeWebRequest.RequestMatcher({
  url: { hostSuffix: 'example.com', schemes: ['http'] },
  resourceType: ['main_frame']
});
```

Example 3 (unknown):
```unknown
var rule = {
  conditions: [
    new chrome.declarativeWebRequest.RequestMatcher({
      url: { hostSuffix: 'example.com' } })
  ],
  actions: [
    new chrome.declarativeWebRequest.CancelRequest()
  ]
};
```

Example 4 (unknown):
```unknown
var rule2 = {
  conditions: [
    new chrome.declarativeWebRequest.RequestMatcher({
      url: { hostSuffix: 'example.com' } }),
    new chrome.declarativeWebRequest.RequestMatcher({
      url: { hostSuffix: 'foobar.com' } })
  ],
  actions: [
    new chrome.declarativeWebRequest.CancelRequest()
  ]
};
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

Example 1 (javascript):
```javascript
if ('launchQueue' in window) {
  launchQueue.setConsumer(async launchParams => {
    if (!launchParams.files || !launchParams.files.length) { return; }
    const fileHandle = launchParams.files[0];
  });
}
``````
```

---

## 消息传递 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/messaging?hl=zh-cn

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

## chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/contentSettings

**Contents:**
- chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
- 内容设置模式
  - 模式优先级
- 主要模式和次要模式
- 资源标识符
- 示例
- 类型

使用 chrome.contentSettings API 更改用于控制网站是否可以使用 Cookie、JavaScript 和插件等功能的设置。更一般地说，内容设置允许您按网站自定义 Chrome 的行为，而不是全局自定义。

您必须在扩展程序的清单中声明“contentSettings”权限，才能使用该 API。例如：

您可以使用模式来指定每项内容设置所影响的网站。例如，https://*.youtube.com/* 指定了 youtube.com 及其所有子网域。内容设置模式的语法与匹配模式的语法相同，但存在以下几点差异：

如果有多条内容设置规则适用于特定网站，则具有更具体模式的规则优先适用。

如果一个模式在某个部分比另一个模式更具体，但在另一部分则不太具体，系统会按以下顺序检查不同的部分：主机名、方案、端口。例如，以下格式按优先级排序：

在决定应用哪项内容设置时，系统会考虑哪个网址取决于内容类型。 例如，对于 contentSettings.notifications，设置基于多功能框中显示的网址。此网址称为“主要”网址。

某些类型的内容可以考虑使用其他网址。例如，是否允许网站设置 contentSettings.cookies 取决于 HTTP 请求的网址（在本例中为主要网址）以及多功能框中显示的网址（称为“次要”网址）。

如果多条规则都具有主要模式和次要模式，则主要模式更具体的规则优先。如果多条规则具有相同的主要模式，则具有更具体的次要模式的规则优先。例如，以下主/次模式对列表按优先级排序：

借助资源标识符，您可以为内容类型的特定子类型指定内容设置。目前，唯一支持资源标识符的内容类型是 contentSettings.plugins，其中资源标识符用于标识特定插件。应用内容设置时，系统会先检查特定插件的设置。如果未找到特定插件的设置，系统会检查插件的一般内容设置。

例如，如果某项内容设置规则的资源标识符为 adobe-flash-player，模式为 <all_urls>，则即使模式 https://www.example.com/* 更具体，该规则也会优先于没有资源标识符且模式为 https://www.example.com/* 的规则。

您可以通过调用 contentSettings.ContentSetting.getResourceIdentifiers 方法获取内容类型的资源标识符列表。返回的列表可能会因用户机器上安装的插件集而异，但 Chrome 会尽量在插件更新期间保持标识符稳定。

如需试用此 API，请从 chrome-extension-samples 代码库中安装 contentSettings API 示例。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

是否检查隐身会话的内容设置。（默认值为 false）

应检索内容设置的主要网址。请注意，主网址的含义取决于内容类型。

ResourceIdentifier 可选

应检索内容设置的辅助网址。默认为主要网址。请注意，辅助网址的含义取决于内容类型，并非所有内容类型都使用辅助网址。

内容设置。如需查看可能的值，请参阅各个 ContentSetting 对象的说明。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

getResourceIdentifiers 函数如下所示：

ResourceIdentifier[] 可选

相应内容类型的资源标识符列表；如果相应内容类型不使用资源标识符，则为 undefined。

Promise<ResourceIdentifier[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

主要网址的格式。如需详细了解模式的格式，请参阅内容设置模式。

ResourceIdentifier 可选

辅助网址的格式。默认情况下，系统会匹配所有网址。如需详细了解格式，请参阅内容设置格式。

相应规则所应用的设置。如需查看可能的值，请参阅各个 ContentSetting 对象的说明。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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
(details: object, callback?: function) => {...}
```

Example 3 (javascript):
```javascript
(details: object, callback?: function) => {...}
```

Example 4 (javascript):
```javascript
(details: object) => void
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to

**Contents:**
  - 使用方法
- 类别
  - 设计界面
    - 支持无障碍功能
    - 使用网站图标
    - 将扩展程序本地化
    - 通知用户
    - 扩展开发者工具
  - 使用 Web 平台
    - 在 ChromeOS 中处理文件

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started?hl=zh-cn

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

## Linux 的自托管 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/distribute/host-extensions?hl=zh-cn

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

## chrome.types 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/types/?hl=zh-cn

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

## chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/devtools/panels

**Contents:**
- chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 概览
- 示例
- 类型
  - Button
    - 属性
  - ElementsPanel
    - 属性

使用 chrome.devtools.panels API 将扩展程序集成到开发者工具窗口界面中：创建自己的面板、访问现有面板和添加边栏。

如需使用此 API，必须在清单中声明以下键。

如需大致了解如何使用开发者工具 API，请参阅开发者工具 API 摘要。

每个扩展程序面板和边栏都显示为单独的 HTML 页面。在开发者工具窗口中显示的所有扩展程序页面都可以访问 chrome.devtools API 中的所有模块，以及 chrome.extension API。其他扩展程序 API 不适用于开发者工具窗口中的网页，但您可以向扩展程序的后台网页发送请求来调用它们，这与在内容脚本中执行的操作类似。

您可以使用 devtools.panels.setOpenResourceHandler 方法安装一个回调函数，该函数用于处理用户打开资源（通常是在开发者工具窗口中点击资源链接）的请求。最多只能调用一个已安装的处理程序；用户可以使用“开发者工具设置”对话框指定默认行为或扩展程序来处理资源打开请求。如果扩展程序多次调用 setOpenResourceHandler()，则仅保留最后一个处理程序。

以下代码添加了一个包含在 Panel.html 中的面板，该面板在开发者工具栏上以 FontPicker.png 表示，并标记为 Font Picker：

以下代码向“元素”面板添加了一个包含在 Sidebar.html 中且标题为字体属性的侧边栏窗格，然后将其高度设置为 8ex：

此屏幕截图展示了上述示例对开发者工具窗口的影响：

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

## 录音和屏幕截图 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/screen-capture

**Contents:**
- 录音和屏幕截图 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 屏幕录制
- 基于用户手势的标签页截取功能
  - 在后台录制音频和视频
  - 在新标签页中录制音频和视频
  - 在弹出式窗口中录制音频
- 其他注意事项

本指南介绍了通过标签页、窗口或 使用 chrome.tabCapture 或 getDisplayMedia()。

对于屏幕录制，请调用 getDisplayMedia()，以触发对话框 如下所示。这让用户能够选择所需的标签页、窗口或屏幕 并清楚地表明录音正在进行。

如果在内容脚本中调用，录制将在用户导航到新值时自动结束 页面。要在后台和跨导航录音，请使用 包含 DISPLAY_MEDIA 原因的屏幕外文档。

调用 getDisplayMedia() 会使浏览器显示一个对话框，询问 向用户提供他们想要分享的内容不过，在某些情况下，用户只是点击了 操作按钮来调用特定标签页的扩展程序，而您希望 立即开始捕获标签页，而不显示此提示。

从 Chrome 116 开始，您可以在 Service Worker 中调用 chrome.tabCapture API 来获取用户手势后的数据流 ID。然后，可以将该字符串传递给屏幕外文档， 开始录制。

在您的 Service Worker 中：

如需查看完整示例，请参阅标签页捕获 - 录音机示例。

在 Chrome 116 之前，您无法在chrome.tabCapture Service Worker 或通过在屏幕外的文档中使用该 API 创建的流 ID。以上两者皆可 是上述方法的要求。

不过，您可以在新标签页或窗口中打开扩展程序页面，并直接获取数据流。设置 targetTabId 属性捕获正确的标签页。

首先打开一个扩展程序页面（可能在弹出式窗口或 Service Worker 中）：

或者，请考虑使用屏幕录制方法，以便 使用屏幕外的文档在后台录制，但向用户显示了一个用于选择标签页的对话框 录制录制窗口或屏幕

如果您只需要录制音频，可以使用以下代码，在扩展程序弹出式窗口中直接获取音频流： chrome.tabCapture.capture。关闭弹出式窗口后，系统会停止录制。

如果您需要在导航之间保留录音，请考虑使用上述方法 上一节中的“说明”部分。

如需详细了解如何录制流，请参阅 MediaRecorder API。

**Examples:**

Example 1 (javascript):
```javascript
const stream = await navigator.mediaDevices.getDisplayMedia({ audio: true, video: true });
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener(async (tab) => {
  const existingContexts = await chrome.runtime.getContexts({});

  const offscreenDocument = existingContexts.find(
    (c) => c.contextType === 'OFFSCREEN_DOCUMENT'
  );

  // If an offscreen document is not already open, create one.
  if (!offscreenDocument) {
    // Create an offscreen document.
    await chrome.offscreen.createDocument({
      url: 'offscreen.html',
      reasons: ['USER_MEDIA'],
      justification: 'Recording from chrome.tabCapture API',
    });
  }

  // Get a MediaStream for the active tab.
  const streamId = await chrome.tabCapture.getMediaStreamId({
    targetTabId: tab.id
  });

  // Send the stream ID to the offscreen document to start recording.
  chrome.runtime.sendMessage({
    type: 'start-recording',
    target: 'offscreen',
    data: streamId
  });
});
```

Example 3 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message.target !== 'offscreen') return;
  
  if (message.type === 'start-recording') {
    const media = await navigator.mediaDevices.getUserMedia({
      audio: {
        mandatory: {
          chromeMediaSource: "tab",
          chromeMediaSourceId: message.data,
        },
      },
      video: {
        mandatory: {
          chromeMediaSource: "tab",
          chromeMediaSourceId: message.data,
        },
      },
    });

    // Continue to play the captured audio to the user.
    const output = new AudioContext();
    const source = output.createMediaStreamSource(media);
    source.connect(output.destination);

    // TODO: Do something to recording the MediaStream.
  }
});
```

Example 4 (unknown):
```unknown
chrome.windows.create({ url: chrome.runtime.getURL("recorder.html") });
```

---

## chrome.tabGroups 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/tabGroups/?hl=zh-cn

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

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/declarativeNetRequest/?hl=zh-cn

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

## 录音和屏幕截图 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/screen-capture?hl=zh-cn

**Contents:**
- 录音和屏幕截图 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 屏幕录制
- 基于用户手势的标签页截取功能
  - 在后台录制音频和视频
  - 在新标签页中录制音频和视频
  - 在弹出式窗口中录制音频
- 其他注意事项

本指南介绍了通过标签页、窗口或 使用 chrome.tabCapture 或 getDisplayMedia()。

对于屏幕录制，请调用 getDisplayMedia()，以触发对话框 如下所示。这让用户能够选择所需的标签页、窗口或屏幕 并清楚地表明录音正在进行。

如果在内容脚本中调用，录制将在用户导航到新值时自动结束 页面。要在后台和跨导航录音，请使用 包含 DISPLAY_MEDIA 原因的屏幕外文档。

调用 getDisplayMedia() 会使浏览器显示一个对话框，询问 向用户提供他们想要分享的内容不过，在某些情况下，用户只是点击了 操作按钮来调用特定标签页的扩展程序，而您希望 立即开始捕获标签页，而不显示此提示。

从 Chrome 116 开始，您可以在 Service Worker 中调用 chrome.tabCapture API 来获取用户手势后的数据流 ID。然后，可以将该字符串传递给屏幕外文档， 开始录制。

在您的 Service Worker 中：

如需查看完整示例，请参阅标签页捕获 - 录音机示例。

在 Chrome 116 之前，您无法在chrome.tabCapture Service Worker 或通过在屏幕外的文档中使用该 API 创建的流 ID。以上两者皆可 是上述方法的要求。

不过，您可以在新标签页或窗口中打开扩展程序页面，并直接获取数据流。设置 targetTabId 属性捕获正确的标签页。

首先打开一个扩展程序页面（可能在弹出式窗口或 Service Worker 中）：

或者，请考虑使用屏幕录制方法，以便 使用屏幕外的文档在后台录制，但向用户显示了一个用于选择标签页的对话框 录制录制窗口或屏幕

如果您只需要录制音频，可以使用以下代码，在扩展程序弹出式窗口中直接获取音频流： chrome.tabCapture.capture。关闭弹出式窗口后，系统会停止录制。

如果您需要在导航之间保留录音，请考虑使用上述方法 上一节中的“说明”部分。

如需详细了解如何录制流，请参阅 MediaRecorder API。

**Examples:**

Example 1 (javascript):
```javascript
const stream = await navigator.mediaDevices.getDisplayMedia({ audio: true, video: true });
```

Example 2 (javascript):
```javascript
chrome.action.onClicked.addListener(async (tab) => {
  const existingContexts = await chrome.runtime.getContexts({});

  const offscreenDocument = existingContexts.find(
    (c) => c.contextType === 'OFFSCREEN_DOCUMENT'
  );

  // If an offscreen document is not already open, create one.
  if (!offscreenDocument) {
    // Create an offscreen document.
    await chrome.offscreen.createDocument({
      url: 'offscreen.html',
      reasons: ['USER_MEDIA'],
      justification: 'Recording from chrome.tabCapture API',
    });
  }

  // Get a MediaStream for the active tab.
  const streamId = await chrome.tabCapture.getMediaStreamId({
    targetTabId: tab.id
  });

  // Send the stream ID to the offscreen document to start recording.
  chrome.runtime.sendMessage({
    type: 'start-recording',
    target: 'offscreen',
    data: streamId
  });
});
```

Example 3 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message.target !== 'offscreen') return;
  
  if (message.type === 'start-recording') {
    const media = await navigator.mediaDevices.getUserMedia({
      audio: {
        mandatory: {
          chromeMediaSource: "tab",
          chromeMediaSourceId: message.data,
        },
      },
      video: {
        mandatory: {
          chromeMediaSource: "tab",
          chromeMediaSourceId: message.data,
        },
      },
    });

    // Continue to play the captured audio to the user.
    const output = new AudioContext();
    const source = output.createMediaStreamSource(media);
    source.connect(output.destination);

    // TODO: Do something to recording the MediaStream.
  }
});
```

Example 4 (unknown):
```unknown
chrome.windows.create({ url: chrome.runtime.getURL("recorder.html") });
```

---

## OAuth 2.0：向 Google 验证用户身份 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/oauth?hl=zh-cn

**Contents:**
- OAuth 2.0：向 Google 验证用户身份 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 开始使用
  - manifest.json
  - service-worker.js
  - index.html
- 保持扩展程序 ID 不变
  - 将扩展程序上传到开发者信息中心
  - 比较 ID
- 创建 OAuth 客户端 ID
- 在清单中注册 OAuth

OAuth2 是业界标准的授权协议。它提供了一种机制，让用户可以向 Web 应用和桌面应用授予对私密信息的访问权限，而无需共享其用户名、密码和其他私密凭据。

本教程将构建一个使用 Google People API 和 Chrome Identity API 访问用户 Google 通讯录的扩展程序。由于扩展程序不会通过 HTTPS 加载，也无法执行重定向或设置 Cookie，因此它们依赖于 Chrome Identity API 来使用 OAuth2。

通过创建名为 manifest.json 的文件并添加以下代码来添加清单。

通过创建名为 service-worker.js 的文件并添加以下代码，来添加扩展程序服务工作器。

添加一个名为 index.html 的 HTML 文件，并添加以下代码。

在开发过程中，保留单个 ID 至关重要。如需保持 ID 不变，请按以下步骤操作：

将扩展程序目录打包为 .zip 文件，然后将其上传到 Chrome 开发者信息中心，但不要发布：

将代码添加到 "key" 字段下的 manifest.json。这样，扩展程序将使用相同的 ID。

在 chrome://extensions 中打开“扩展程序管理”页面，确保开发者模式已启用，然后上传未打包的扩展程序目录。将扩展程序管理页面上的扩展程序 ID 与开发者信息中心内的商品 ID 进行比较。二者应一致。

任何使用 OAuth 2.0 访问 Google API 的应用都必须具有授权凭据，以向 Google 的 OAuth 2.0 服务器表明应用的身份。以下步骤介绍了如何为项目创建凭据。 然后，您的应用可以使用这些凭据来访问您为相应项目启用的 API。

首先，前往 Google API 控制台，如果您还没有项目，请创建一个新项目。按照以下说明创建 OAuth 客户端并获取客户端 ID。

在扩展程序清单中添加 "oauth2" 字段。将生成的 OAuth 客户端 ID 放在 "client_id" 下。为了获取用户的账号信息，我们需要请求相关的 "scope"、"https://www.googleapis.com/auth/userinfo.email"。

创建一个名为 oauth.js 的文件来管理 OAuth 流程，并添加以下代码。

在 index.html 的头部放置一个 oauth.js 的脚本标记。

重新加载扩展程序，然后点击浏览器图标以打开 index.html。打开控制台，然后点击“FriendBlock Contacts”（FriendBlock 联系人）按钮。控制台中将显示一个 OAuth 令牌。

返回 Google API 控制台，然后从边栏中选择库。搜索“Google People API”，点击正确的搜索结果并启用该 API。

在扩展程序清单中，将 Google People API 客户端库添加到 "scopes"。

返回 Google API 控制台，然后重新前往“凭据”页面。点击“创建凭据”，然后从下拉菜单中选择“API 密钥”。

现在，扩展程序已获得适当的权限和凭据，并且可以授权 Google 用户，因此可以通过 People API 请求数据。更新 oauth.js 中的代码，使其与以下代码一致。

将 API_KEY 替换为从 Google API 控制台生成的 API 密钥。扩展程序应记录一个 JSON 对象，该对象在 memberResourceNames 字段下包含一个 people/account_id 数组。

现在，扩展程序会返回用户联系人的列表，因此可以发出更多请求来检索这些联系人的个人资料和信息。扩展程序将使用 memberResourceNames 来检索用户联系人的照片信息。更新 oauth.js 以包含以下代码。

重新加载并返回到扩展程序。点击 FriendBlock 按钮，大功告成！以方块形式显示联系人的面孔。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "OAuth Tutorial FriendBlock",
  "version": "1.0",
  "description": "Uses OAuth to connect to Google's People API and display contacts photos.",
  "manifest_version": 3,
  "action": {
    "default_title": "FriendBlock, friends face's in a block."
  },
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

Example 2 (unknown):
```unknown
chrome.action.onClicked.addListener(function() {
  chrome.tabs.create({url: 'index.html'});
});
```

Example 3 (unknown):
```unknown
<html>
  <head>
    <title>FriendBlock</title>
    <style>
      button {
        padding: 10px;
        background-color: #3C79F8;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <button>FriendBlock Contacts</button>
    <div id="friendDiv"></div>
  </body>
</html>
```

Example 4 (unknown):
```unknown
{ // manifest.json
  "manifest_version": 3,
...
  "key": "ThisKeyIsGoingToBeVeryLong/go8GGC2u3UD9WI3MkmBgyiDPP2OreImEQhPvwpliioUMJmERZK3zPAx72z8MDvGp7Fx7ZlzuZpL4yyp4zXBI+MUhFGoqEh32oYnm4qkS4JpjWva5Ktn4YpAWxd4pSCVs8I4MZms20+yx5OlnlmWQEwQiiIwPPwG1e1jRw0Ak5duPpE3uysVGZXkGhC5FyOFM+oVXwc1kMqrrKnQiMJ3lgh59LjkX4z1cDNX3MomyUMJ+I+DaWC2VdHggB74BNANSd+zkPQeNKg3o7FetlDJya1bk8ofdNBARxHFMBtMXu/ONfCT3Q2kCY9gZDRktmNRiHG/1cXhkIcN1RWrbsCkwIDAQAB",
}
```

---

## “activeTab”权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/activeTab

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

## 查找和跟踪错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/find-a-bug?hl=zh-cn

**Contents:**
- 查找和跟踪错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

在提交扩展程序的 bug 或功能请求之前，您应先查看未解决的 Chromium 问题，确认是否已有人报告过该 bug 或功能请求。这些问题会记录在 Chromium 问题跟踪器中。借助此数据库，您可以搜索并跟踪针对 Chromium 报告的任何问题。

请勿通过回复“我也是”来回应任何 bug 或功能请求。请订阅 Chrome 扩展程序邮寄名单，及时了解 bug 的修复时间。不过，如果您有有价值的信息（例如更好的测试用例或建议的修复），请添加评论。

---

## chrome.devtools.panels 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/devtools_panels?hl=zh-cn

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

Example 1 (javascript):
```javascript
if ('launchQueue' in window) {
  launchQueue.setConsumer(async launchParams => {
    if (!launchParams.files || !launchParams.files.length) { return; }
    const fileHandle = launchParams.files[0];
  });
}
``````
```

---

## chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/certificateProvider

**Contents:**
- chrome.certificateProvider 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 用法
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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

向用户请求 PIN 码。一次只能有一个正在进行的请求。在另一个流程正在进行时发出的请求会被拒绝。如果另一个流程正在进行中，扩展程序应负责稍后重试。

PinResponseDetails 可选

Promise<PinResponseDetails | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

扩展程序应在初始化后以及当前可用证书集发生每次更改时调用此函数。扩展程序还应在每次收到此事件时，调用此函数以响应 onCertificatesUpdateRequested。

SetCertificatesDetails

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

停止由 requestPin 函数启动的 PIN 码请求。

StopPinRequestDetails

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

请改用 onCertificatesUpdateRequested。

每当浏览器请求此扩展程序提供的当前证书列表时，都会触发此事件。扩展程序必须使用当前证书列表调用 reportCallback 一次。

reportCallback 参数如下所示：

如果通过 setCertificates 设置的证书不足，或者浏览器请求更新后的信息，则会触发此事件。扩展程序必须使用更新后的证书列表和收到的 certificatesRequestId 调用 setCertificates。

CertificatesUpdateRequest

每次浏览器需要使用此扩展程序通过 setCertificates 提供的证书对消息进行签名时，都会触发此事件。

扩展程序必须使用适当的算法和私钥对来自 request 的输入数据进行签名，并通过使用收到的 signRequestId 调用 reportSignature 来返回签名。

请改用 onSignatureRequested。

每当浏览器需要使用此扩展程序提供的证书对 onCertificatesRequested 事件进行签名时，此事件都会触发。扩展程序必须使用适当的算法和私钥对 request 中的数据进行签名，并通过调用 reportCallback 返回签名。reportCallback 必须只调用一次。

reportCallback 参数如下所示：

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
chrome.certificateProvider.reportSignature(  details: ReportSignatureDetails,  callback?: function,): Promise<void>
```

Example 3 (unknown):
```unknown
chrome.certificateProvider.requestPin(  details: RequestPinDetails,  callback?: function,): Promise<PinResponseDetails | undefined>
```

Example 4 (javascript):
```javascript
(details?: PinResponseDetails) => void
```

---

## 替换 Chrome 网页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/override?hl=zh-cn

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

## chrome.windows 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/windows?hl=zh-cn

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

## 使用 Puppeteer 测试 Chrome 扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/puppeteer

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

## chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/documentScan

**Contents:**
- chrome.documentScan 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- Document Scan API
- 类型
  - CancelScanResponse
    - 属性
  - CloseScannerResponse
    - 属性

使用 chrome.documentScan API 从连接的文档扫描仪中发现和检索图片。

文档扫描 API 旨在允许应用和扩展程序查看连接的文档扫描仪上的纸质文档的内容。

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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

使用传入的句柄关闭扫描器，并返回一个 Promise，该 Promise 会解析为 CloseScannerResponse 对象。如果使用回调，则会将对象传递给回调。即使响应不成功，所提供的句柄也会失效，不应再用于后续操作。

指定之前从对 openScanner 的调用返回的开放扫描器的句柄。

Promise<CloseScannerResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

从之前通过 openScanner 打开的扫描器获取群组名称和成员选项。此方法会返回一个 Promise，该 Promise 会解析为一个 GetOptionGroupsResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

通过调用 openScanner 返回的已打开扫描器的句柄。

GetOptionGroupsResponse

Promise<GetOptionGroupsResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

获取可用扫描器的列表，并返回一个 Promise，该 Promise 会解析为 GetScannerListResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

一个 DeviceFilter，用于指示应返回哪些类型的扫描器。

GetScannerListResponse

Promise<GetScannerListResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

打开扫描器以进行独占访问，并返回一个 Promise，该 Promise 会解析为 OpenScannerResponse 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

要打开的扫描器的 ID。此值是从之前对 getScannerList 的调用返回的值之一。

Promise<OpenScannerResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

从有效作业句柄读取下一块可用的图片数据，并返回一个 Promise，该 Promise 会解析为 ReadScanDataResponse 对象。如果使用回调，则会将对象传递给回调。

**注意：**响应结果为 SUCCESS 且 data 成员的长度为零是有效的。这意味着扫描器仍在工作，但尚未准备好其他数据。来电者应稍等片刻，然后重试。

扫描作业完成后，响应将包含结果值 EOF。此响应可能包含一个最终的非零 data 成员。

之前从 startScan 返回的有效作业句柄。

Promise<ReadScanDataResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

执行文档扫描，并返回一个 Promise，该 Promise 会解析为 ScanResults 对象。如果向此函数传递了回调，则返回的数据会传递给该回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

为指定扫描器设置选项，并返回一个 Promise，该 Promise 会解析为一个 SetOptionsResponse 对象，其中包含尝试按传入的 OptionSetting 对象中的顺序设置每个值的结果。如果使用回调，则会将对象传递给回调。

要设置选项的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

要应用于扫描器的 OptionSetting 对象列表。

Promise<SetOptionsResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

在指定的扫描器上开始扫描，并返回一个 Promise，该 Promise 会解析为 StartScanResponse。如果使用回调，则会将对象传递给回调。如果调用成功，响应会包含一个作业句柄，可在后续调用中使用该句柄来读取扫描数据或取消扫描。

打开的扫描器的句柄。此值应为之前从对 openScanner 的调用返回的值。

一个 StartScanOptions 对象，用于指示扫描时要使用的选项。StartScanOptions.format 属性必须与扫描器 ScannerInfo 中返回的某个条目匹配。

Promise<StartScanResponse>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

**Examples:**

Example 1 (unknown):
```unknown
chrome.documentScan.cancelScan(  job: string,  callback?: function,): Promise<CancelScanResponse>
```

Example 2 (javascript):
```javascript
(response: CancelScanResponse) => void
```

Example 3 (unknown):
```unknown
chrome.documentScan.closeScanner(  scannerHandle: string,  callback?: function,): Promise<CloseScannerResponse>
```

Example 4 (javascript):
```javascript
(response: CloseScannerResponse) => void
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/samples?text=sidePanel&hl=zh-cn

**Contents:**
  - 示例

---

## chrome.dom 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/dom

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

## 扩展程序中的实时更新 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/real-time?hl=zh-cn

**Contents:**
- 扩展程序中的实时更新 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 常见方案
  - 让用户及时了解更改。
  - 向用户发送通知。
  - 即时通讯
- 使用 Push API 实现推送通知
- 使用 chrome.gcm 接收推送通知
- 使用 WebSocket 实现实时消息
  - 不适合推送通知
  - 仅限活跃连接

实时更新提供了从服务器直接到扩展程序安装的即时通信路径。您可以在事件发生时发送和接收数据。无论您是将它用于即时通讯、触发后台任务或同步设备数据，它都是涉及许多现代服务的关键操作。您可以通过多种方式在 Chrome 扩展程序中进行实时通信。

以下是实时通信至关重要的 Chrome 扩展程序中的一些常见场景：

如果您要在多个用户之间同步文件、设置或其他信息，那么 Web Push 是向您的扩展程序发送静默更新以告知其从服务器更新状态的理想方式。

您是否允许用户报告 bug 或问题？您可以集成推送提供程序，以便在您有要共享的更新时，直接在您的扩展程序中通知他们。

虽然您可以完全在客户端发送通知，但如果服务器端逻辑确定发送通知的对象、内容、位置或时间，那么与 Web 推送相比，Web Push 将是最能满足未来需求的方案。

如果仅向一部分用户发送消息，则推送是最佳选择。 虽然 Firebase Cloud Messaging 确实提供 Topics（也称为“渠道”），但只能在 HTTP Cloud Messaging API 中使用。这与 chrome.gcm 使用的旧版不同。如果您希望向所有用户发送广泛消息，包括使用旧版 Chrome（Chrome 121 以下版本）的用户，chrome.gcm 是理想之选。chrome.gcm 基于旧版 Firebase 消息传递 API 而构建，十多年来一直受到 Chrome 的支持。

您可以使用网页推送或 chrome.gcm，在发生对用户帐号的重要情况时（例如收到新消息或共享文件时）向用户发送通知。

需要频繁的双向通信？那么 Web Socket 可能是您的最佳选择。它会在您的扩展程序和服务器（甚至直接连至其他用户）之间打开双向连接。您可以实时交换数据和消息。虽然它们一般是 Web 应用的理想选择，但它们存在一些扩展程序限制，如果您打算使用它们，请务必注意。

在本指南的其余部分，我们将详细了解可用的选项。

借助 Push API，您可以使用任何推送提供程序发送推送通知和消息。一旦收到 Push API 推送，您的 Service Worker 就会对其进行处理。如果扩展程序已暂停，通过 Push 会重新将其唤醒。在扩展程序中使用它的过程与在开放网络中使用完全相同。

chrome.gcm API 提供与 Firebase Cloud Messaging (FCM) 的直接连接，Firebase Cloud Messaging (FCM) 服务用于向 Web 应用和移动应用发送实时更新。这是 Chrome 专用的扩展程序 API，在浏览器推出推送功能之前已有数年增加。它是使用 Firebase（现已弃用）的旧版 HTTP API 构建的。虽然这些 API 已在其他地方弃用，但它们在扩展程序中不会弃用。在可预见的未来，它们将继续工作。但是，由于这是旧版推送后端，因此它缺少 Topics 等功能。

虽然必须使用 FCM 后端服务才能在 Chrome 中收到通知，但您无需使用 chrome.gcm 即可发送消息。所有推送提供方都可以使用网页推送向 Firebase 帐号发送和接收消息和事件。虽然这仍然是一个完全受支持的 Chrome Extension API，但最佳做法是优先采用 Push API 等网络标准，而不是像这样的扩展程序专用标准。如果您的用例最好使用 chrome.gcm，请查看有关如何从头开始设置 chrome.gcm 的详细操作方法。

十多年来，WebSockets 一直是 Web 实时消息传递的基石。它们已成为网络上实时事件的首选方案，可以提供连续的双向对话。WebSocket 适用于各种扩展程序组件，包括内容脚本、弹出式窗口、侧边栏和/或后台 Service Worker。虽然它们一般是 Web 应用的理想选择，但它们在扩展程序方面存在一些限制，如果您打算使用它们，需要注意。

由于 WebSocket 在 Web 平台中运行，而不是使用 chrome.gcm 等扩展程序平台 API，因此在扩展程序外部启动 Websocket 连接时，Chrome 无法唤醒您的扩展程序。

Chrome 会在 30 秒后暂停未使用的扩展程序。Chrome 会通过许多启发法来确定是否“正在使用”扩展程序，其中一个就是有效的 WebSocket 连接。Chrome 不会暂停在过去 30 秒内发送或接收 WebSocket 消息的扩展程序。如果您在扩展程序中使用 WebSocket，并且需要确保 WebSocket 不会过早关闭，您可以发送检测信号来保持连接。这包括定期向服务器发送消息，让服务器和 Chrome 知道您仍处于活跃状态。如需查看有关如何无限期地让 websocket 保持活动状态的示例，请参阅我们的 WebSocket 文档。

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

## 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers

**Contents:**
- 扩展程序 Service Worker 简介 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

本部分介绍了在扩展程序中使用 Service Worker 需要了解的内容。无论您是否熟悉 Service Worker，都应该阅读本部分。扩展程序 Service Worker 是扩展程序的核心事件处理脚本。这使得它们与 Web Service Worker 明显不同，网络中成堆的 Service Worker 文章不一定有用。

Extension Service Worker 与 Web 扩展 Service Worker 有一些共同点。扩展 Service Worker 在需要时加载，并在其进入休眠状态时取消加载。只要扩展程序 Service Worker 在加载后还会主动接收事件，它就会运行，不过它可以关闭。与对应的 Web 应用一样，扩展 Service Worker 无法访问 DOM，不过您可以根据需要将其用于屏幕外文档。

扩展程序 Service Worker 不只是网络代理（因为经常会提到 Web Service Worker）。除了标准 Service Worker 事件之外，它们还会响应扩展程序事件，例如导航到新页面、点击通知或关闭标签页。它们的注册和更新方式也与 Web Service Worker 不同。

---

## chrome.sidePanel 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/sidePanel?hl=zh-cn

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

## 扩展 Service Worker 生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/lifecycle?hl=zh-cn

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

## 使用其他安装方法 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/distribute/install-extensions?hl=zh-cn

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

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/ai?hl=zh-cn

**Contents:**
  - 扩展程序和 AI
  - 利用 AI 赋能的扩展程序提升浏览体验
    - 控制 Web 内容
    - 让浏览器更实用
    - 自定义浏览器
  - 使用 Gemini 构建 AI 赋能的 Chrome 扩展程序
  - 更多用例
- 将 AI 与扩展程序集成
  - 客户端 AI
  - Cloud AI

---

## 扩展开发者工具 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/devtools/extend-devtools?hl=zh-cn

**Contents:**
- 扩展开发者工具 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- “开发者工具”页面
- 创建 DevTools 扩展程序
- 开发者工具界面元素：面板和侧边栏窗格
- 在扩展程序组件之间通信
  - 注入内容脚本
  - 在被检查的窗口中评估 JavaScript
  - 将所选元素传递给内容脚本
  - 获取参考面板的 window
  - 将消息从注入的脚本发送到 DevTools 页面

开发者工具扩展程序通过向扩展程序添加的开发者工具页面访问特定于开发者工具的扩展程序 API，从而向 Chrome 开发者工具添加功能。

特定于 DevTools 的扩展程序 API 包括：

开发者工具窗口打开时，开发者工具扩展程序会创建其开发者工具页面的实例，该实例会在窗口打开期间一直存在。此页面可以访问 DevTools API 和扩展程序 API，并且可以执行以下操作：

开发者工具页面可以直接访问扩展程序 API。这包括能够使用消息传递与 Service Worker 通信。

如需为您的扩展程序创建 DevTools 页面，请在扩展程序清单中添加 devtools_page 字段：

devtools_page 字段必须指向 HTML 页面。由于 DevTools 页面必须是扩展程序的本地页面，因此我们建议您使用相对网址指定该页面。

chrome.devtools API 的成员仅适用于在开发者工具窗口打开时在该窗口中加载的页面。内容脚本和其他扩展程序页面无权访问这些 API。

除了常见的扩展程序界面元素（例如浏览器操作、上下文菜单和弹出式窗口）之外，DevTools 扩展程序还可以向 DevTools 窗口添加界面元素：

每个面板都是自己的 HTML 文件，其中可以包含其他资源（JavaScript、CSS、图片等）。如需创建基本面板，请使用以下代码：

在面板或边栏窗格中执行的 JavaScript 具有与 DevTools 页面相同的 API 访问权限。

您可以通过以下几种方式在边栏窗格中显示内容：

对于 setObject() 和 setExpression()，该窗格会显示与 DevTools 控制台中显示的值相同的值。不过，setExpression() 允许您显示 DOM 元素和任意 JavaScript 对象，而 setObject() 仅支持 JSON 对象。

以下部分介绍了一些有助于让 DevTools 扩展程序组件相互通信的实用方法。

如需注入内容脚本，请使用 scripting.executeScript()：

您可以使用 inspectedWindow.tabId 属性检索被检查窗口的标签页 ID。

如果已注入内容脚本，您可以使用消息传递 API 与其通信。

您可以使用 inspectedWindow.eval() 方法在被检查网页的上下文中执行 JavaScript 代码。您可以从 DevTools 页面、面板或边栏窗格中调用 eval() 方法。

默认情况下，系统会在网页的主框架上下文中对表达式求值。inspectedWindow.eval() 使用的脚本执行上下文和选项与在开发者工具控制台中输入的代码相同，这使得在使用 eval() 时可以访问开发者工具 Console Utilities API 功能。例如，您可以使用它来检查 HTML 文档的 <head> 部分中的第一个脚本元素：

您还可以在调用 inspectedWindow.eval() 时将 useContentScriptContext 设置为 true，以便在与内容脚本相同的上下文中评估表达式。如需使用此选项，请在调用 eval() 之前使用静态内容脚本声明，方法是调用 executeScript() 或在 manifest.json 文件中指定内容脚本。上下文脚本上下文加载后，您还可以使用此选项注入其他内容脚本。

内容脚本无法直接访问当前所选元素。不过，您使用 inspectedWindow.eval() 执行的任何代码都具有对 DevTools 控制台和控制台实用程序 API 的访问权限。例如，在已评估的代码中，您可以使用 $0 访问所选元素。

如需将所选元素传递给内容脚本，请执行以下操作：

在内容脚本中创建一个方法，将所选元素作为参数。

使用 inspectedWindow.eval() 和 useContentScriptContext: true 选项从 DevTools 页面调用该方法。

useContentScriptContext: true 选项指定表达式必须在与内容脚本相同的上下文中进行求值，以便它可以访问 setSelectedElement 方法。

如需从 devtools 面板调用 postMessage()，您需要引用其 window 对象。从 panel.onShown 事件处理脚本中获取面板的 iframe 窗口：

直接注入到网页中且不使用内容脚本的代码（包括通过附加 <script> 标记或调用 inspectedWindow.eval() 注入的代码）无法使用 runtime.sendMessage() 向 DevTools 页面发送消息。相反，我们建议您将注入的脚本与可用作中介的内容脚本结合使用，并使用 window.postMessage() 方法。以下示例使用上一部分中的后台脚本：

如需了解其他替代消息传递技术，请访问 GitHub。

如需跟踪开发者工具窗口是否处于打开状态，请向服务工件添加 onConnect 监听器，并从开发者工具页面调用 connect()。由于每个标签页都可以打开自己的 DevTools 窗口，因此您可能会收到多个连接事件。如需跟踪是否有任何 DevTools 窗口处于打开状态，请统计连接和断开连接事件，如下例所示：

DevTools 页面会创建如下所示的连接：

如需了解扩展程序可以使用的标准 API，请参阅 chrome.* API 和Web API。

欢迎提供反馈！您的意见和建议有助于我们改进 API。

您可以在示例中找到使用 DevTools API 的示例。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": ...
  "version": "1.0",
  "devtools_page": "devtools.html",
  ...
}
```

Example 2 (unknown):
```unknown
chrome.devtools.panels.create("My Panel",
    "MyPanelIcon.png",
    "Panel.html",
    function(panel) {
      // code invoked on panel creation
    }
);
```

Example 3 (unknown):
```unknown
chrome.devtools.panels.elements.createSidebarPane("My Sidebar",
    function(sidebar) {
        // sidebar initialization code here
        sidebar.setObject({ some_data: "Some data to show" });
});
```

Example 4 (unknown):
```unknown
// DevTools page -- devtools.js
chrome.scripting.executeScript({
  target: {
    tabId: chrome.devtools.inspectedWindow.tabId
  },
  files: ["content_script.js"]
});
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/develop

**Contents:**
  - 开发
- 设计界面
  - 侧边栏
  - 操作
  - 菜单
- 控制浏览器
  - 覆盖 Chrome 网页和设置
  - 扩展开发者工具
  - 显示通知
  - 管理历史记录

---

## 使用其他安装方法 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/distribute/install-extensions

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

## OAuth 2.0：向 Google 验证用户身份 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/integrate/oauth

**Contents:**
- OAuth 2.0：向 Google 验证用户身份 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 开始使用
  - manifest.json
  - service-worker.js
  - index.html
- 保持扩展程序 ID 不变
  - 将扩展程序上传到开发者信息中心
  - 比较 ID
- 创建 OAuth 客户端 ID
- 在清单中注册 OAuth

OAuth2 是业界标准的授权协议。它提供了一种机制，让用户可以向 Web 应用和桌面应用授予对私密信息的访问权限，而无需共享其用户名、密码和其他私密凭据。

本教程将构建一个使用 Google People API 和 Chrome Identity API 访问用户 Google 通讯录的扩展程序。由于扩展程序不会通过 HTTPS 加载，也无法执行重定向或设置 Cookie，因此它们依赖于 Chrome Identity API 来使用 OAuth2。

通过创建名为 manifest.json 的文件并添加以下代码来添加清单。

通过创建名为 service-worker.js 的文件并添加以下代码，来添加扩展程序服务工作器。

添加一个名为 index.html 的 HTML 文件，并添加以下代码。

在开发过程中，保留单个 ID 至关重要。如需保持 ID 不变，请按以下步骤操作：

将扩展程序目录打包为 .zip 文件，然后将其上传到 Chrome 开发者信息中心，但不要发布：

将代码添加到 "key" 字段下的 manifest.json。这样，扩展程序将使用相同的 ID。

在 chrome://extensions 中打开“扩展程序管理”页面，确保开发者模式已启用，然后上传未打包的扩展程序目录。将扩展程序管理页面上的扩展程序 ID 与开发者信息中心内的商品 ID 进行比较。二者应一致。

任何使用 OAuth 2.0 访问 Google API 的应用都必须具有授权凭据，以向 Google 的 OAuth 2.0 服务器表明应用的身份。以下步骤介绍了如何为项目创建凭据。 然后，您的应用可以使用这些凭据来访问您为相应项目启用的 API。

首先，前往 Google API 控制台，如果您还没有项目，请创建一个新项目。按照以下说明创建 OAuth 客户端并获取客户端 ID。

在扩展程序清单中添加 "oauth2" 字段。将生成的 OAuth 客户端 ID 放在 "client_id" 下。为了获取用户的账号信息，我们需要请求相关的 "scope"、"https://www.googleapis.com/auth/userinfo.email"。

创建一个名为 oauth.js 的文件来管理 OAuth 流程，并添加以下代码。

在 index.html 的头部放置一个 oauth.js 的脚本标记。

重新加载扩展程序，然后点击浏览器图标以打开 index.html。打开控制台，然后点击“FriendBlock Contacts”（FriendBlock 联系人）按钮。控制台中将显示一个 OAuth 令牌。

返回 Google API 控制台，然后从边栏中选择库。搜索“Google People API”，点击正确的搜索结果并启用该 API。

在扩展程序清单中，将 Google People API 客户端库添加到 "scopes"。

返回 Google API 控制台，然后重新前往“凭据”页面。点击“创建凭据”，然后从下拉菜单中选择“API 密钥”。

现在，扩展程序已获得适当的权限和凭据，并且可以授权 Google 用户，因此可以通过 People API 请求数据。更新 oauth.js 中的代码，使其与以下代码一致。

将 API_KEY 替换为从 Google API 控制台生成的 API 密钥。扩展程序应记录一个 JSON 对象，该对象在 memberResourceNames 字段下包含一个 people/account_id 数组。

现在，扩展程序会返回用户联系人的列表，因此可以发出更多请求来检索这些联系人的个人资料和信息。扩展程序将使用 memberResourceNames 来检索用户联系人的照片信息。更新 oauth.js 以包含以下代码。

重新加载并返回到扩展程序。点击 FriendBlock 按钮，大功告成！以方块形式显示联系人的面孔。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "OAuth Tutorial FriendBlock",
  "version": "1.0",
  "description": "Uses OAuth to connect to Google's People API and display contacts photos.",
  "manifest_version": 3,
  "action": {
    "default_title": "FriendBlock, friends face's in a block."
  },
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

Example 2 (unknown):
```unknown
chrome.action.onClicked.addListener(function() {
  chrome.tabs.create({url: 'index.html'});
});
```

Example 3 (unknown):
```unknown
<html>
  <head>
    <title>FriendBlock</title>
    <style>
      button {
        padding: 10px;
        background-color: #3C79F8;
        display: inline-block;
      }
    </style>
  </head>
  <body>
    <button>FriendBlock Contacts</button>
    <div id="friendDiv"></div>
  </body>
</html>
```

Example 4 (unknown):
```unknown
{ // manifest.json
  "manifest_version": 3,
...
  "key": "ThisKeyIsGoingToBeVeryLong/go8GGC2u3UD9WI3MkmBgyiDPP2OreImEQhPvwpliioUMJmERZK3zPAx72z8MDvGp7Fx7ZlzuZpL4yyp4zXBI+MUhFGoqEh32oYnm4qkS4JpjWva5Ktn4YpAWxd4pSCVs8I4MZms20+yx5OlnlmWQEwQiiIwPPwG1e1jRw0Ak5duPpE3uysVGZXkGhC5FyOFM+oVXwc1kMqrrKnQiMJ3lgh59LjkX4z1cDNX3MomyUMJ+I+DaWC2VdHggB74BNANSd+zkPQeNKg3o7FetlDJya1bk8ofdNBARxHFMBtMXu/ONfCT3Q2kCY9gZDRktmNRiHG/1cXhkIcN1RWrbsCkwIDAQAB",
}
```

---

## 提交扩展程序错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/file-a-bug

**Contents:**
- 提交扩展程序错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

在开发扩展程序时，您可能会发现某些行为与扩展程序的文档不符，或者出乎意料。这可能是 Chrome bug 导致的，也可能是我们应添加到文档中的内容。无论如何，请提交相应的问题报告来告知我们。请按照以下步骤操作，提供足够的信息来重现问题：

---

## 使用 WebHID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/webhid?hl=zh-cn

**Contents:**
- 使用 WebHID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的可用性
- 权限
- 清单
- 支持的上下文
- Chrome 扩展程序差异

人机接口设备 (HID) 可从人接受输入或向人提供输出。它还指 HID 协议，该协议是一种用于在主机和设备之间实现双向通信的标准，旨在简化安装过程。

本页介绍了扩展程序专有的 API 方面。如需详细了解 WebHID API，请参阅 MDN。

您可以在我们的示例代码库中找到 WebHID 示例应用。

无需清单文件权限；不过，WebHID 会触发浏览器的用户权限流程。

此 API 几乎可在任何上下文中使用。WebHID.requestDevice() 方法无法在扩展程序服务工作器中使用。有关详情，请参见下文。

在扩展程序 Service Worker 中使用此 API 时，设备连接会话会使 Service Worker 保持活跃状态。

虽然 WebHID 可供扩展程序 Service Worker 使用，但无法在扩展程序 Service Worker 中调用 WebHID.requestDevice()，该函数会返回一个可解析为 HIDDevice 实例的 Promise。为解决此问题，请从扩展程序 Service Worker 以外的扩展程序页面调用 requestDevice()，并向扩展程序 Service Worker 发送消息。

以下代码遵循典型模式，在需要用户手势的权限流程中调用 requestDevice()。获取设备后，它会向服务工件发送消息，然后服务工件可以使用 getDevices() 检索设备。

**Examples:**

Example 1 (javascript):
```javascript
myButton.addEventListener("click", async () => {
  await navigator.hid.requestDevice({
    filters: [{ vendorId: 0x1234, productId: 0x5678 }],
  });
  chrome.runtime.sendMessage("newDevice");
});
```

Example 2 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message === "newDevice") {
    const devices = await navigator.hid.getDevices();
    for (const device of devices) {
      // open device connection.
      await device.open();
    }
  }
});
```

---

## chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/commands

**Contents:**
- chrome.commands 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 清单
- 用法
  - 支持的键
  - 组合键要求
  - 处理命令事件
  - 操作命令
- 范围
- 示例

使用 Commands API 添加键盘快捷键，以触发扩展程序中的操作，例如打开浏览器操作或向扩展程序发送命令的操作。

如需使用此 API，必须在清单中声明以下键。

Commands API 允许扩展程序开发者定义特定命令，并将其绑定到默认的按键组合。扩展程序接受的每个命令都必须在扩展程序的清单中声明为 "commands" 对象的属性。

属性键用作命令的名称。命令对象可以包含两个属性。

一个可选属性，用于声明命令的默认键盘快捷键。如果省略，则命令将处于未绑定状态。此属性可以采用字符串值或对象值。

字符串值，用于指定应在所有平台上使用的默认键盘快捷键。

对象值允许扩展程序开发者为每个平台自定义键盘快捷键。提供特定于平台的快捷方式时，有效的对象属性为 default、chromeos、linux、mac 和 windows。

用于向用户简要说明命令用途的字符串。此字符串显示在扩展程序键盘快捷键管理界面中。标准命令需要说明，但操作命令会忽略说明。

扩展程序可以包含许多命令，但最多只能指定四个建议的键盘快捷键。用户可以从 chrome://extensions/shortcuts 对话框中手动添加更多快捷方式。

以下键可用作命令快捷键。键定义区分大小写。尝试加载密钥大小写不正确的扩展程序会导致安装时出现清单解析错误。

常规 - Comma、Period、Home、End、PageUp、PageDown、Space、Insert、Delete

箭头键 - Up、Down、Left、Right

媒体键 - MediaNextTrack、MediaPlayPause、MediaPrevTrack、MediaStop

Ctrl、Alt（macOS 上为 Option）、Shift、MacCtrl（仅限 macOS）、Command（仅限 macOS）、Search（仅限 ChromeOS）

扩展命令快捷方式必须包含 Ctrl 或 Alt。

在 macOS 上，Ctrl 会自动转换为 Command。

如需在 macOS 上使用 Control 键，请在定义 "mac" 快捷方式时将 Ctrl 替换为 MacCtrl。

在其他平台的组合中使用 MacCtrl 会导致验证错误，并阻止安装扩展程序。

Search 是 ChromeOS 独有的可选修饰符。

某些操作系统和 Chrome 快捷键（例如窗口管理）始终优先于扩展程序命令快捷键，并且无法被覆盖。

在服务工作器中，您可以使用 onCommand.addListener 将处理程序绑定到清单中定义的每个命令。例如：

_execute_action (Manifest V3)、_execute_browser_action (Manifest V2) 和 _execute_page_action (Manifest V2) 命令分别预留用于触发操作、浏览器操作或网页操作。这些命令不会像标准命令那样调度 command.onCommand 事件。

如果您需要根据弹出式窗口的打开情况采取行动，请考虑在弹出式窗口的 JavaScript 中监听 DOMContentLoaded 事件。

默认情况下，命令的范围限定为 Chrome 浏览器。这意味着，当浏览器未处于焦点状态时，命令快捷键处于非活动状态。从 Chrome 35 开始，扩展程序开发者可以选择将命令标记为“全局”。即使 Chrome 未处于焦点状态，全局命令也能正常运行。

全局命令的键盘快捷键建议数量上限为 Ctrl+Shift+[0..9]。这是一项保护措施，旨在最大限度地降低覆盖其他应用中的快捷方式的风险，因为如果允许 Alt+P 作为全局快捷方式，那么用于打开打印对话框的键盘快捷键可能无法在其他应用中正常使用。

最终用户可以使用 chrome://extensions/shortcuts 中显示的界面将全局命令重新映射到自己喜欢的组合键。

以下示例展示了 Commands API 的核心功能。

命令允许扩展程序将逻辑映射到可由用户调用的键盘快捷键。最基本的命令只需要在扩展程序的清单中声明命令并注册监听器，如以下示例所示。

如使用部分中所述，您还可以将命令映射到扩展程序的动作。以下示例注入了一个内容脚本，当用户点击扩展程序的操作或触发键盘快捷键时，该脚本会在当前页面上显示一个提醒。

如果某个扩展程序尝试注册的快捷键已被另一个扩展程序使用，则第二个扩展程序的快捷键将无法按预期注册。通过预料到这种可能性并在安装时检查冲突，您可以提供更可靠的最终用户体验。

相应命令的有效快捷键，如果无有效快捷键，则为空白。

返回相应扩展程序的所有已注册的扩展程序命令及其快捷方式（如果处于有效状态）。在 Chrome 110 之前，此命令不会返回 _execute_action。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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

## 使用 Puppeteer 测试 Service Worker 的终止情况 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/test/test-serviceworker-termination-with-puppeteer

**Contents:**
- 使用 Puppeteer 测试 Service Worker 的终止情况 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前期准备
- 第 1 步：启动 Node.js 项目
- 第 2 步：安装依赖项
- 第 3 步：编写基本测试
- 第 4 步：终止 Service Worker
- 第 5 步：运行测试
- 第 6 步：修复 Service Worker
- 第 7 步：再次运行测试
- 后续步骤

本指南介绍了如何通过测试服务构建更强大的扩展程序 使用 Puppeteer 终止工作器。已做好随时处理账号终止的准备 时间很重要，因为这可能会在没有警告的情况下 发生，导致 Service Worker。因此，扩展程序必须保存重要的状态和 如果存在以下情况，则能够在再次启动后立即处理请求： 事件进行处理。

克隆或下载 chrome-extensions-samples 代码库。 我们将在 /functional-samples/tutorial.terminate-sw/test-extension：用于发送消息 向 Service Worker 发送一个按钮并将文本添加到页面 如果收到响应。

您还需要安装 Node.JS，这是 Puppeteer 的构建运行时。

在新目录中创建以下文件。它们共同创造了 Node.js 项目并提供 Puppeteer 测试套件的基本结构 使用 Jest 作为测试运行程序。如需详细了解此设置，请参阅使用 Puppeteer 测试 Chrome 扩展程序。

请注意，我们的测试会从示例代码库加载 test-extension。chrome.runtime.onMessage 的处理脚本依赖于 chrome.runtime.onInstalled 事件处理脚本中设置的状态。因此，当服务工件终止时，data 的内容将丢失，并且无法响应任何未来的消息。我们会在编写测试后解决此问题。

service-worker-broken.js:

运行 npm install 以安装所需的依赖项。

将以下测试添加到 index.test.js 的底部。开始测试 页面中，点击按钮元素并等待响应 从 Service Worker 加载。

您可以使用 npm start 运行测试，并且应该会看到测试成功完成。

添加以下可终止 Service Worker 的辅助函数：

最后，使用以下代码更新您的测试。现在，终止服务工作器，然后再次点击该按钮，检查您是否收到了响应。

运行 npm start。您的测试应该会失败，这表示服务工件在终止后未响应。

接下来，通过取消对临时状态的依赖来修复 Service Worker。更新 测试扩展程序以使用存储在 代码库中的 service-worker-fixed.js。

service-worker-fixed.js：

在这里，我们将版本保存到 chrome.storage.local，而不是全局变量 在 Service Worker 的生命周期之间保留状态。由于只能异步访问存储空间，因此我们还会从 onMessage 监听器返回 true，以确保 sendResponse 回调保持活跃状态。

使用 npm start 再次运行测试。现在它应该会通过。

现在，您可以将相同的方法应用于自己的扩展程序。请考虑以下事项：

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "puppeteer-demo",
  "version": "1.0",
  "dependencies": {
    "jest": "^29.7.0",
    "puppeteer": "^24.8.1"
  },
  "scripts": {
    "start": "jest ."
  },
  "devDependencies": {
    "@jest/globals": "^29.7.0"
  }
}
```

Example 2 (javascript):
```javascript
const puppeteer = require('puppeteer');

const SAMPLES_REPO_PATH = 'PATH_TO_SAMPLES_REPOSITORY';
const EXTENSION_PATH = `${SAMPLES_REPO_PATH}/functional-samples/tutorial.terminate-sw/test-extension`;
const EXTENSION_ID = 'gjgkofgpcmpfpggbgjgdfaaifcmoklbl';

let browser;

beforeEach(async () => {
  browser = await puppeteer.launch({
    // Set to 'new' to hide Chrome if running as part of an automated build.
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

Example 3 (javascript):
```javascript
let data;

chrome.runtime.onInstalled.addListener(() => {
  data = { version: chrome.runtime.getManifest().version };
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  sendResponse(data.version);
});
```

Example 4 (javascript):
```javascript
test('can message service worker', async () => {
  const page = await browser.newPage();
  await page.goto(`chrome-extension://${EXTENSION_ID}/page.html`);

  // Message without terminating service worker
  await page.click('button');
  await page.waitForSelector('#response-0');
});
```

---

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/samples?hl=zh-cn

**Contents:**
  - 示例

---

## 使用 WebHID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/webhid

**Contents:**
- 使用 WebHID 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 在扩展程序中的可用性
- 权限
- 清单
- 支持的上下文
- Chrome 扩展程序差异

人机接口设备 (HID) 可从人接受输入或向人提供输出。它还指 HID 协议，该协议是一种用于在主机和设备之间实现双向通信的标准，旨在简化安装过程。

本页介绍了扩展程序专有的 API 方面。如需详细了解 WebHID API，请参阅 MDN。

您可以在我们的示例代码库中找到 WebHID 示例应用。

无需清单文件权限；不过，WebHID 会触发浏览器的用户权限流程。

此 API 几乎可在任何上下文中使用。WebHID.requestDevice() 方法无法在扩展程序服务工作器中使用。有关详情，请参见下文。

在扩展程序 Service Worker 中使用此 API 时，设备连接会话会使 Service Worker 保持活跃状态。

虽然 WebHID 可供扩展程序 Service Worker 使用，但无法在扩展程序 Service Worker 中调用 WebHID.requestDevice()，该函数会返回一个可解析为 HIDDevice 实例的 Promise。为解决此问题，请从扩展程序 Service Worker 以外的扩展程序页面调用 requestDevice()，并向扩展程序 Service Worker 发送消息。

以下代码遵循典型模式，在需要用户手势的权限流程中调用 requestDevice()。获取设备后，它会向服务工件发送消息，然后服务工件可以使用 getDevices() 检索设备。

**Examples:**

Example 1 (javascript):
```javascript
myButton.addEventListener("click", async () => {
  await navigator.hid.requestDevice({
    filters: [{ vendorId: 0x1234, productId: 0x5678 }],
  });
  chrome.runtime.sendMessage("newDevice");
});
```

Example 2 (javascript):
```javascript
chrome.runtime.onMessage.addListener(async (message) => {
  if (message === "newDevice") {
    const devices = await navigator.hid.getDevices();
    for (const device of devices) {
      // open device connection.
      await device.open();
    }
  }
});
```

---

## chrome.offscreen 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/offscreen?hl=zh-cn

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

## 在 Service Worker 中使用 WebSocket 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/web-platform/websockets?hl=zh-cn

**Contents:**
- 在 Service Worker 中使用 WebSocket 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 背景
- 示例：WebSocket 保持连接

本教程演示了如何在 Chrome 扩展程序的服务工程中连接到 WebSocket。您可以在 GitHub 上找到有效示例。

从 Chrome 116 开始，扩展程序 Service Worker 可以更好地支持 WebSockets。以前，如果 30 秒内没有发生其他扩展事件，即使 WebSocket 连接处于活动状态，Service Worker 也可能会变为非活动状态。这会终止 Service Worker 并关闭 WebSocket 连接。如需详细了解扩展程序服务工件生命周期，请参阅扩展程序服务工件指南。

从 Chrome 116 开始，您可以通过在 30 秒的 Service Worker 活动窗口内交换消息，让具有 WebSocket 连接的 Service Worker 保持活跃状态。这些操作可以通过您的服务器或扩展程序发起。在以下示例中，我们将从 Chrome 扩展程序向服务器发送一条常规消息，以确保 Service Worker 保持活动状态。

首先，我们需要确保我们的扩展程序仅在支持服务工作器中的 WebSocket 的 Chrome 版本中运行，为此，请在清单中将最低 Chrome 版本设置为 116：

然后，我们可以通过每 20 秒发送一次 keepalive 消息来让服务工作器保持活跃状态。在 Service Worker 连接到 WebSocket 后，系统会启动 keepalive。以下示例 WebSocket 客户端会记录消息，并在 onopen 事件触发时调用 keepAlive()：

在 keepAlive() 中，我们使用 setInterval(...) 在有有效 WebSocket 连接时定期向服务器发送 ping：

**Examples:**

Example 1 (unknown):
```unknown
{
  ...
  "minimum_chrome_version": "116",
  ...
}
```

Example 2 (javascript):
```javascript
let webSocket = null;

function connect() {
  webSocket = new WebSocket('wss://example.com/ws');

  webSocket.onopen = (event) => {
    console.log('websocket open');
    keepAlive();
  };

  webSocket.onmessage = (event) => {
    console.log(`websocket received message: ${event.data}`);
  };

  webSocket.onclose = (event) => {
    console.log('websocket connection closed');
    webSocket = null;
  };
}

function disconnect() {
  if (webSocket == null) {
    return;
  }
  webSocket.close();
}
```

Example 3 (javascript):
```javascript
function keepAlive() {
  const keepAliveIntervalId = setInterval(
    () => {
      if (webSocket) {
        webSocket.send('keepalive');
      } else {
        clearInterval(keepAliveIntervalId);
      }
    },
    // Set the interval to 20 seconds to prevent the service worker from becoming inactive.
    20 * 1000 
  );
}
```

---

## chrome.webNavigation 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/webNavigation/?hl=zh-cn

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

## chrome.contentSettings 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/contentSettings/?hl=zh-cn

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

## 内容过滤 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/content-filtering

**Contents:**
- 内容过滤 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 过滤网络请求
  - 将过滤条件规则与扩展程序捆绑在一起
  - 在运行时动态添加过滤规则
- 根据观察到的请求调整规则
- 允许用户定义自己的过滤规则
- 过滤网页上的元素
- 过滤已安装政策的扩展程序中的网络请求
- 拦截导航请求

在 Chrome 扩展程序中，您可以通过不同的方式实现内容和网络过滤。本指南概述了可供扩展程序使用的内容过滤功能，以及 Chrome 扩展程序可以使用的不同过滤方法、技术和 API。

在 Chrome 扩展程序中过滤网络请求的主要方法是使用 chrome.declarativeNetRequest API。借助声明式网络请求，开发者可以通过指定声明式规则来阻止或修改网络请求。声明式网络请求规则格式基于大多数广告拦截器使用的过滤器列表语法的功能。

Chrome 支持与扩展程序捆绑在一起的规则，以及动态更新的规则（例如响应远程配置或用户输入的规则）。

扩展程序软件包中包含的规则称为“静态规则”。在安装或升级扩展程序时，系统会安装和更新这些规则。Chrome 会限制扩展程序可以声明的静态规则数量。

对于静态声明式网络请求规则，Chrome 有一个包含 30 万条规则的全局共享池，可供一组已安装的扩展程序共同使用。此外，还保证每个扩展程序最多可以创建 30, 000 条静态规则。例如，如果用户只安装了一个内容过滤扩展程序，则该扩展程序最多可以使用 330,000 条静态声明式网络请求规则。为便于您了解规则的数量，大多数广告拦截器常用的 EasyList 过滤器列表都包含大约 35,000 条网络规则。

静态声明式网络请求规则可整理为不同的规则集。一个扩展程序最多可以指定 100 个静态规则集，并且一次可以启用 50 个规则集。

部分规则不能与扩展程序捆绑在一起。相反，扩展程序需要在运行时添加它们。这些规则称为“动态规则”。

对于动态声明式网络请求规则，Chrome 允许每个扩展程序最多 30,000 条安全动态规则。大多数规则都被视为安全规则：block、allow、allowAllRequests 或 upgradeScheme。即使某条规则被视为不安全的规则（例如 redirect），仍然可以动态添加，但最大数量上限为 5,000 条，同时也会计入 30,000 条动态规则数量上限。更确切地说，在简易列表过滤条件列表中，有 98-99% 的规则都是安全规则。

内容过滤扩展程序可以分别使用静态和动态规则将已知的过滤规则与其扩展程序捆绑在一起，并根据需要使用来自服务器的新内容过滤规则更新其扩展程序。

广告生态系统在不断变化，内容过滤器也需要随之更新。通过结合使用 chrome.webRequest 和动态声明式网络请求规则，可以分析网络请求是否存在可能侵犯隐私权的行为，并在日后屏蔽此类请求。

这种方法的优势在于，分析过程是异步进行的，不会对网站性能产生负面影响。

您可以在扩展程序中提供过滤器配置界面，让用户自行定义内容过滤规则。将这些用户定义的规则转换为声明式网络请求规则，并将它们添加为动态规则。这些规则在浏览器会话和扩展程序升级之间保持不变，仍可供用户使用。使用此方法，用户最多可以添加 3 万条自定义规则。

过滤网络请求只是内容过滤的一个重要部分。另一项重要工作是直接从网页中移除不需要的内容。例如，超过 40% 的 easylist filter list 规则定义了客户端应如何隐藏页面元素。

这可以通过内容脚本来实现。内容脚本在网页环境中运行，可以使用 DOM 对网页进行更改。

Chrome 扩展程序无法执行远程托管代码。但是，来自服务器且与要隐藏的元素相关的数据不受影响，因为这些数据被视为配置数据，因此可以根据需要在运行时更新元素规则。

企业和教育用例通常对内容和网络过滤有极其严格的要求，例如根据内容过滤请求。为了启用这些用例，已安装政策的扩展程序提供了一种额外的方法来过滤和屏蔽网络请求。对 webRequest API 中的事件使用“屏蔽”选项时，可以实现一个程序化内容过滤器，以便针对每个请求执行自定义逻辑，以决定是否应屏蔽某个请求。这仅限于通过政策安装的扩展程序，因为这些扩展程序具有较高的信任级别。

可以使用声明式网络请求规则过滤导航请求。例如，您可能希望绕过将用户重定向到预期目标网址的跟踪网址。一种处理方法是将导航请求 https://tracker.com?redirect=https%3A%2F%2Fexample.com 重定向到扩展程序页面（需要配置为可通过 Web 访问的资源），然后系统会运行脚本来提取重定向目标，并使用 window.location.replace("https://example.com") 绕过链接跟踪器来重定向到目标位置。

---

## chrome.devtools.inspectedWindow 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/devtools_inspectedWindow?hl=zh-cn

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

## 扩展程序中的实时更新 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/real-time

**Contents:**
- 扩展程序中的实时更新 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 常见方案
  - 让用户及时了解更改。
  - 向用户发送通知。
  - 即时通讯
- 使用 Push API 实现推送通知
- 使用 chrome.gcm 接收推送通知
- 使用 WebSocket 实现实时消息
  - 不适合推送通知
  - 仅限活跃连接

实时更新提供了从服务器直接到扩展程序安装的即时通信路径。您可以在事件发生时发送和接收数据。无论您是将它用于即时通讯、触发后台任务或同步设备数据，它都是涉及许多现代服务的关键操作。您可以通过多种方式在 Chrome 扩展程序中进行实时通信。

以下是实时通信至关重要的 Chrome 扩展程序中的一些常见场景：

如果您要在多个用户之间同步文件、设置或其他信息，那么 Web Push 是向您的扩展程序发送静默更新以告知其从服务器更新状态的理想方式。

您是否允许用户报告 bug 或问题？您可以集成推送提供程序，以便在您有要共享的更新时，直接在您的扩展程序中通知他们。

虽然您可以完全在客户端发送通知，但如果服务器端逻辑确定发送通知的对象、内容、位置或时间，那么与 Web 推送相比，Web Push 将是最能满足未来需求的方案。

如果仅向一部分用户发送消息，则推送是最佳选择。 虽然 Firebase Cloud Messaging 确实提供 Topics（也称为“渠道”），但只能在 HTTP Cloud Messaging API 中使用。这与 chrome.gcm 使用的旧版不同。如果您希望向所有用户发送广泛消息，包括使用旧版 Chrome（Chrome 121 以下版本）的用户，chrome.gcm 是理想之选。chrome.gcm 基于旧版 Firebase 消息传递 API 而构建，十多年来一直受到 Chrome 的支持。

您可以使用网页推送或 chrome.gcm，在发生对用户帐号的重要情况时（例如收到新消息或共享文件时）向用户发送通知。

需要频繁的双向通信？那么 Web Socket 可能是您的最佳选择。它会在您的扩展程序和服务器（甚至直接连至其他用户）之间打开双向连接。您可以实时交换数据和消息。虽然它们一般是 Web 应用的理想选择，但它们存在一些扩展程序限制，如果您打算使用它们，请务必注意。

在本指南的其余部分，我们将详细了解可用的选项。

借助 Push API，您可以使用任何推送提供程序发送推送通知和消息。一旦收到 Push API 推送，您的 Service Worker 就会对其进行处理。如果扩展程序已暂停，通过 Push 会重新将其唤醒。在扩展程序中使用它的过程与在开放网络中使用完全相同。

chrome.gcm API 提供与 Firebase Cloud Messaging (FCM) 的直接连接，Firebase Cloud Messaging (FCM) 服务用于向 Web 应用和移动应用发送实时更新。这是 Chrome 专用的扩展程序 API，在浏览器推出推送功能之前已有数年增加。它是使用 Firebase（现已弃用）的旧版 HTTP API 构建的。虽然这些 API 已在其他地方弃用，但它们在扩展程序中不会弃用。在可预见的未来，它们将继续工作。但是，由于这是旧版推送后端，因此它缺少 Topics 等功能。

虽然必须使用 FCM 后端服务才能在 Chrome 中收到通知，但您无需使用 chrome.gcm 即可发送消息。所有推送提供方都可以使用网页推送向 Firebase 帐号发送和接收消息和事件。虽然这仍然是一个完全受支持的 Chrome Extension API，但最佳做法是优先采用 Push API 等网络标准，而不是像这样的扩展程序专用标准。如果您的用例最好使用 chrome.gcm，请查看有关如何从头开始设置 chrome.gcm 的详细操作方法。

十多年来，WebSockets 一直是 Web 实时消息传递的基石。它们已成为网络上实时事件的首选方案，可以提供连续的双向对话。WebSocket 适用于各种扩展程序组件，包括内容脚本、弹出式窗口、侧边栏和/或后台 Service Worker。虽然它们一般是 Web 应用的理想选择，但它们在扩展程序方面存在一些限制，如果您打算使用它们，需要注意。

由于 WebSocket 在 Web 平台中运行，而不是使用 chrome.gcm 等扩展程序平台 API，因此在扩展程序外部启动 Websocket 连接时，Chrome 无法唤醒您的扩展程序。

Chrome 会在 30 秒后暂停未使用的扩展程序。Chrome 会通过许多启发法来确定是否“正在使用”扩展程序，其中一个就是有效的 WebSocket 连接。Chrome 不会暂停在过去 30 秒内发送或接收 WebSocket 消息的扩展程序。如果您在扩展程序中使用 WebSocket，并且需要确保 WebSocket 不会过早关闭，您可以发送检测信号来保持连接。这包括定期向服务器发送消息，让服务器和 Chrome 知道您仍处于活跃状态。如需查看有关如何无限期地让 websocket 保持活动状态的示例，请参阅我们的 WebSocket 文档。

---

## 扩展开发者工具 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/how-to/devtools/extend-devtools

**Contents:**
- 扩展开发者工具 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- “开发者工具”页面
- 创建 DevTools 扩展程序
- 开发者工具界面元素：面板和侧边栏窗格
- 在扩展程序组件之间通信
  - 注入内容脚本
  - 在被检查的窗口中评估 JavaScript
  - 将所选元素传递给内容脚本
  - 获取参考面板的 window
  - 将消息从注入的脚本发送到 DevTools 页面

开发者工具扩展程序通过向扩展程序添加的开发者工具页面访问特定于开发者工具的扩展程序 API，从而向 Chrome 开发者工具添加功能。

特定于 DevTools 的扩展程序 API 包括：

开发者工具窗口打开时，开发者工具扩展程序会创建其开发者工具页面的实例，该实例会在窗口打开期间一直存在。此页面可以访问 DevTools API 和扩展程序 API，并且可以执行以下操作：

开发者工具页面可以直接访问扩展程序 API。这包括能够使用消息传递与 Service Worker 通信。

如需为您的扩展程序创建 DevTools 页面，请在扩展程序清单中添加 devtools_page 字段：

devtools_page 字段必须指向 HTML 页面。由于 DevTools 页面必须是扩展程序的本地页面，因此我们建议您使用相对网址指定该页面。

chrome.devtools API 的成员仅适用于在开发者工具窗口打开时在该窗口中加载的页面。内容脚本和其他扩展程序页面无权访问这些 API。

除了常见的扩展程序界面元素（例如浏览器操作、上下文菜单和弹出式窗口）之外，DevTools 扩展程序还可以向 DevTools 窗口添加界面元素：

每个面板都是自己的 HTML 文件，其中可以包含其他资源（JavaScript、CSS、图片等）。如需创建基本面板，请使用以下代码：

在面板或边栏窗格中执行的 JavaScript 具有与 DevTools 页面相同的 API 访问权限。

您可以通过以下几种方式在边栏窗格中显示内容：

对于 setObject() 和 setExpression()，该窗格会显示与 DevTools 控制台中显示的值相同的值。不过，setExpression() 允许您显示 DOM 元素和任意 JavaScript 对象，而 setObject() 仅支持 JSON 对象。

以下部分介绍了一些有助于让 DevTools 扩展程序组件相互通信的实用方法。

如需注入内容脚本，请使用 scripting.executeScript()：

您可以使用 inspectedWindow.tabId 属性检索被检查窗口的标签页 ID。

如果已注入内容脚本，您可以使用消息传递 API 与其通信。

您可以使用 inspectedWindow.eval() 方法在被检查网页的上下文中执行 JavaScript 代码。您可以从 DevTools 页面、面板或边栏窗格中调用 eval() 方法。

默认情况下，系统会在网页的主框架上下文中对表达式求值。inspectedWindow.eval() 使用的脚本执行上下文和选项与在开发者工具控制台中输入的代码相同，这使得在使用 eval() 时可以访问开发者工具 Console Utilities API 功能。例如，您可以使用它来检查 HTML 文档的 <head> 部分中的第一个脚本元素：

您还可以在调用 inspectedWindow.eval() 时将 useContentScriptContext 设置为 true，以便在与内容脚本相同的上下文中评估表达式。如需使用此选项，请在调用 eval() 之前使用静态内容脚本声明，方法是调用 executeScript() 或在 manifest.json 文件中指定内容脚本。上下文脚本上下文加载后，您还可以使用此选项注入其他内容脚本。

内容脚本无法直接访问当前所选元素。不过，您使用 inspectedWindow.eval() 执行的任何代码都具有对 DevTools 控制台和控制台实用程序 API 的访问权限。例如，在已评估的代码中，您可以使用 $0 访问所选元素。

如需将所选元素传递给内容脚本，请执行以下操作：

在内容脚本中创建一个方法，将所选元素作为参数。

使用 inspectedWindow.eval() 和 useContentScriptContext: true 选项从 DevTools 页面调用该方法。

useContentScriptContext: true 选项指定表达式必须在与内容脚本相同的上下文中进行求值，以便它可以访问 setSelectedElement 方法。

如需从 devtools 面板调用 postMessage()，您需要引用其 window 对象。从 panel.onShown 事件处理脚本中获取面板的 iframe 窗口：

直接注入到网页中且不使用内容脚本的代码（包括通过附加 <script> 标记或调用 inspectedWindow.eval() 注入的代码）无法使用 runtime.sendMessage() 向 DevTools 页面发送消息。相反，我们建议您将注入的脚本与可用作中介的内容脚本结合使用，并使用 window.postMessage() 方法。以下示例使用上一部分中的后台脚本：

如需了解其他替代消息传递技术，请访问 GitHub。

如需跟踪开发者工具窗口是否处于打开状态，请向服务工件添加 onConnect 监听器，并从开发者工具页面调用 connect()。由于每个标签页都可以打开自己的 DevTools 窗口，因此您可能会收到多个连接事件。如需跟踪是否有任何 DevTools 窗口处于打开状态，请统计连接和断开连接事件，如下例所示：

DevTools 页面会创建如下所示的连接：

如需了解扩展程序可以使用的标准 API，请参阅 chrome.* API 和Web API。

欢迎提供反馈！您的意见和建议有助于我们改进 API。

您可以在示例中找到使用 DevTools API 的示例。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": ...
  "version": "1.0",
  "devtools_page": "devtools.html",
  ...
}
```

Example 2 (unknown):
```unknown
chrome.devtools.panels.create("My Panel",
    "MyPanelIcon.png",
    "Panel.html",
    function(panel) {
      // code invoked on panel creation
    }
);
```

Example 3 (unknown):
```unknown
chrome.devtools.panels.elements.createSidebarPane("My Sidebar",
    function(sidebar) {
        // sidebar initialization code here
        sidebar.setObject({ some_data: "Some data to show" });
});
```

Example 4 (unknown):
```unknown
// DevTools page -- devtools.js
chrome.scripting.executeScript({
  target: {
    tabId: chrome.devtools.inspectedWindow.tabId
  },
  files: ["content_script.js"]
});
```

---

## “activeTab”权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/activeTab?hl=zh-cn

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

## 内容脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/content-scripts?hl=zh-cn

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

## Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/whats-new?hl=zh-cn

**Contents:**
- Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 视频：解答有关 Chrome 应用商店可发现性的问题
- Chrome 140：新增了 sidePanel.getLayout() API
- 新指南：扩展程序更新生命周期
- Chrome 139：在 Chrome 品牌 build 中移除 --extensions-on-chrome-urls 和 --disable-extensions-except flag
- Chrome 138：对新标签页的更改
- 博文：在即将发生的书签变更之前更新扩展程序
- 博文：2025 年 6 月 Chrome 扩展程序的最新动态
- 视频：在浏览器中玩打地鼠游戏 - 这是真的吗？
- 视频：Chrome 的新扩展程序菜单说明

请经常查看此页面，了解 Chrome 扩展程序、扩展程序文档或相关政策或其他方面的变化。您可以在 Chrome 扩展程序邮寄名单中找到其他通知。Chrome 时间表列出了稳定版和 Beta 版的发布日期。

发布日期：2025 年 11 月 25 日

在最新视频中，我们会解答您在 Chrome 应用商店中发现应用方面的问题。

从 Chrome 140 开始，您可以使用新的 sidePanel.getLayout() API 来确定侧边栏位于屏幕的左侧还是右侧。如果您支持 RTL 语言，而新安装的 Chrome 的默认语言不同，此功能尤为有用。

我们发布了一份新指南，说明了 Chrome 中扩展程序的更新方式。

从 Chrome 139 开始，官方 Chrome 品牌 build 中将移除 --extensions-on-chrome-urls 和 --disable-extensions-except 命令行标志。详细了解邮寄名单。

从 Chrome 138 开始，我们将更新新标签页界面，添加新的页脚。 您可以访问邮寄名单页面了解详情。

我们将对书签同步功能进行一些更改，这可能会影响您的扩展程序。如需了解详情，请参阅这篇博文。

我们一直在忙碌，推出了 Google I/O 大会，并在 Chrome 和 Chrome 应用商店中推出了多项新功能。请参阅Chrome 扩展程序最新动态 - 2025 年 6 月，了解最新资讯！

观看我们的最新视频，了解如何在浏览器中制作游戏。

观看我们的最新视频“Chrome 的新扩展程序菜单详解” ，了解实验性的新扩展程序菜单。

在“扩展程序真棒”第 1 集中了解如何开始开发扩展程序，并在第 2 集中了解 Chrome 自定义功能的灵活性！

从 Chrome 135 开始，chrome.userScripts API 中提供了一个新的 userScripts.execute() 方法。您可以使用此方法在任意时间注入用户脚本一次，而无需永久注册该脚本。

从 Chrome 132 开始，您可以在开发者工具中查看和修改使用 chrome.storage API 存储的数据。如需了解详情，请参阅开发者工具文档中的新页面查看和修改扩展程序存储空间。

在 2024 年 Google I/O 大会上，我们分享了扩展程序菜单即将发生的一些早期设计变更，这些变更可让用户更好地控制扩展程序可以访问的网站。我们很快就会开始测试这些变更，首先会在 Canary 中面向一小部分用户进行测试，并希望将来能更广泛地推出这些变更。

我们还推出了 chrome.permissions.addHostAccessRequest() API。

发布日期：2024 年 11 月 19 日

从 Chrome 132 开始，Tabs API 中的 frozen 属性用于指示标签页是否已被浏览器冻结。发送到冻结标签页的消息将排队，并在标签页解除冻结后处理。

发布日期：2024 年 11 月 12 日

扩展程序专用 Prompt API 现已在初始源试用中提供，因此您可以在浏览器中构建使用 Gemini Nano（我们最高效的语言模型）的 Chrome 扩展程序。

加入 Prompt API 源试用（在 Chrome 131 至 136 中进行），并分享您的反馈。您的反馈可以直接影响我们构建和实现此 API 和所有内置 AI API 的未来版本的方式。

发布日期：2024 年 10 月 17 日

现在，我们又可以来盘点一下 Chrome 扩展程序方面的最新动态了：我们在 AI 集成、新 API、活动和视频方面都有令人兴奋的更新。如需了解详情，请参阅 Chrome 扩展程序 10 月刊！

发布日期：2024 年 10 月 17 日

Chrome 推出了内置 AI 挑战赛：诚邀您使用 Chrome 的集成 AI 模型和 API 创建创新的 Web 应用和 Chrome 扩展程序，赢取总计 65,000 美元的奖品。

如需注册并详细了解相关信息，请访问 Built-in AI Challenge 网站。我们迫不及待地想看看您在为 Web 注入 AI 后会创作出什么作品！

从 Chrome 130 开始，action.onUserSettingsChanged 事件可用。这是根据 WebExtensions 社区组中的一项提案实现的。感谢 Microsoft 为 Chromium 做出的贡献。

从 Chrome 130 开始，getKeys() 方法可在 chrome.storage API 使用的 StorageArea 接口上使用。这是根据 WebExtensions 社区组中的提案实现的。

从 Chrome 128 开始，我们将在 Declarative Net Request API 中添加对响应标头匹配的支持。这是一个常见的要求，尤其是在匹配 Content-Type 标头时，我们与 WebExtensions 社区组一起设计了一个合适的 API。

我们已更新 API 参考文档，以纳入新的 responseHeaders 和 excludedResponseHeaders 字段。您可以使用这些方法来检查指定标头的存在情况和值。

在此次更新中，我们在文档中添加了一个新的规则评估部分，其中介绍了规则的匹配方式。对于标头匹配，规则只能在收到响应标头后运行，因此它们的应用阶段比其他规则晚。这意味着，请求在被屏蔽或重定向之前确实到达了服务器。

了解 Chrome 扩展程序中的内容脚本，包括如何注册 CSS 和 JavaScript 以在特定网页上运行。观看完整视频。

Chrome 应用商店团队发布了一系列更新，对开发者计划政策页面进行了修改，旨在鼓励开发优质产品、防止欺骗性行为，并确保用户在知情的情况下同意。Chrome 应用商店政策经理 Rebecca Soares 在 Chrome 扩展程序：重要政策更新这篇博文中总结了所有更新。

在过去三个月内，我们推出了一些重大更新和新功能，包括开始逐步淘汰清单 V2。快来了解 Chrome 扩展程序 7 月刊中的最新动态！

Chrome 扩展程序团队的 Patrick 介绍了 Chrome 扩展程序中远程托管代码 (RHC) 的概念。了解为何不再允许使用 RHC、如何检测 RHC，以及如果您的扩展程序需要更新，该怎么做。观看完整视频。

从 Chrome 127 开始，所有扩展程序都可以使用 action.openPopup API。以前，它仅在 Canary 中或通过政策安装的扩展程序中可用。

Chrome 扩展程序 DevRel 团队与负责 Chrome 应用商店审核的 Trust & Safety 团队进行了交流，询问了您提出的问题。观看完整视频。

从 6 月 3 日开始，在 Chrome Beta 版、Dev 版和 Canary 版渠道中，如果用户仍安装了 Manifest V2 扩展程序，那么当他们访问扩展程序管理页面 (chrome://extensions) 时，部分用户会开始看到警告横幅，告知他们所安装的部分（Manifest V2）扩展程序很快将不再受支持。如需了解详情，请参阅官方公告

我们最近对侧边栏界面进行了一些更改，包括添加了固定图标并移除了全局侧边栏图标。如需了解详情，请参阅公开服务公告 (PSA)，并查看我们更新的文档和示例。

又一届 Google I/O 大会已经落幕，我们报道了所有令人兴奋的扩展程序更新！前往 YouTube 观看完整视频，并阅读我们的博文，了解一些精彩内容。

现在，当您使用 Declarative Net Request API 时，Chrome 应用商店允许您跳过对符合条件的更改的审核。如需详细了解资格要求以及如何选择启用，请参阅 Chrome 应用商店文档。

我们最近更新了 Chrome 应用商店 API 文档，添加了有关 deployPercentage 的信息。借助该 API，您可以分配部分发布部署的百分比。了解 deployPercentage。

Chrome 126 引入了一个新的 manifest.json 字段 - trial_tokens，让您可以在所有扩展程序界面中选择加入源试用和弃用试用。如需了解详情，请参阅指南。

我们发布了新一期Chrome 扩展程序动态。该帖子讨论了扩展程序团队在过去几个月中的工作。这包括：Chrome 应用商店中的版本回滚、更好的 Firebase Auth 支持以及更多 API 发布和更新。

将扩展程序回滚到 Chrome 应用商店中之前发布的版本，无需额外审核！如需了解详情，请参阅这篇博文和文档。

ChromeOS 上现已提供高级 documentScan API，用于发现和检索连接的文档扫描仪中的图片。

自 Chrome 124 起，服务工作线程支持 WebGPU。如需快速入门，请查看 WebGPU 扩展程序示例。

Events API 现在支持按无类别域间路由 (CIDR) 区块进行过滤。CIDR 块是共享相同网络前缀和相同位数的 IP 地址集合。以前，如果开发者需要过滤多个 IP 地址，则需要为屏蔽范围内的每个地址配置过滤规则。现在，当扩展程序调用 addListener() 时，传入的规则意味着只有当网址的主机部分是 IP 地址且包含在数组中指定的任何 CIDR 块中时，才会调用事件处理脚本。

在 Chrome 应用商店中，清单文件 (manifest.json) 中扩展程序的 "name" 字段现在有 75 个字符的通用限制。之前，英文的限制为 45 个字符，其他语言区域的 "name" 字段没有限制。

此功能最初旨在允许存在文化和语言差异，而这些差异可能无法用相同数量的字符来表达。遗憾的是，一小部分开发者滥用了此功能，向商店发送垃圾内容。因此，我们推出了新的通用限制，将字符数上限提高到 75 个。 此限制涵盖了目前商店中的几乎所有扩展程序，因此您很可能无需因这一变化而采取任何行动。如果您尝试上传的扩展程序的名称超过了上限，商店会阻止该上传操作。

在这篇由 eyeo 的扩展程序引擎团队撰写的博文中，我们将探讨测试扩展程序服务工作线程的问题。在 Manifest V2 中，扩展程序位于后台网页中，在整个扩展程序生命周期内都处于唤醒状态。Manifest V3 使用的是服务工作器，而服务工作器在不需要时会关闭，从而节省资源。这会带来一定的测试挑战。这篇博文介绍了 eyeo 如何应对这些挑战。

当设备进入休眠状态时，使用 chrome.alarms API 设置的闹钟不再延迟。当设备唤醒时，无论错过了多少闹钟，闹钟都会响一次。例如，假设闹钟设置为每小时响一次，而设备在凌晨 12:55 到凌晨 2:05 处于休眠状态，那么只有凌晨 2:00 的闹钟会触发 onAlarm 事件。它会在尽可能接近凌晨 2:00 时触发，如果设备处于休眠状态，则会在设备唤醒时立即触发。

此更改使 Chrome 符合 Web 扩展程序社区组中达成的行为一致性。

往返缓存 (bfcache) 是一种浏览器优化，可实现即时后退和前进导航。从 Chrome 123 开始，当具有开放扩展程序端口的网页存储在 bfcache 中时，消息渠道会关闭，这意味着不会向该网页发送任何消息。因此，扩展程序脚本应监听 onDisconnect 等生命周期事件，并在网页从 BFCache 恢复时设置新连接。

如需了解详情和查看示例代码，请参阅扩展消息端口对 BFCache 行为的更改。

我们已完成对所有异步扩展 API 方法的 Promise 支持实现。这样做是为了通过改进处理异步操作的人体工程学来使 API 方法现代化。少数方法（例如 desktopCapture.chooseDesktopMedia()）仍仅支持回调，因为其当前界面与 Promise 不兼容。为了实现向后兼容性，我们仍支持回调。如果您发现 Promise 失败，请提交 bug 报告。

我们刚刚发布了有关扩展程序中实时选项的指南。实时更新功能可提供从服务器直接到扩展程序安装的即时通信路径。此外，我们还针对使用 chrome.gcm、Web 推送提供了新的指南。

我们刚刚发布了一篇指南，介绍了如何使用 Puppeteer 测试 Service Worker 终止。随附的示例在 Puppeteer 和 Selenium 中演示了这一点。

我们刚刚发布了原生消息的更新版示例。此 API 允许您的扩展程序启动另一个应用并与之通信。感谢 GitHub 贡献者 Shubham-Rasal 为此做出的贡献。

向 tabs.Tab 对象添加了一个名为 lastAccessed 的新属性。此属性表示标签页上次处于活动状态的时间。返回的值以毫秒为单位，从纪元起算。

在从 Manifest V2 更改为 Manifest V3 的过程中，"background" 清单键的子项发生了更改，以适应将后台脚本替换为扩展程序服务工作线程。以前，如果将 Manifest V2 键 "scripts"、"page" 或 "persistent" 添加到 Manifest V3 扩展程序的 "background" 键中，系统会抛出错误。现在，如果存在这些键，系统会触发警告。

这样做是为了能够根据社区组中的提案，在多个浏览器中的扩展程序中使用单个清单文件。

发布日期：2023 年 12 月 14 日

从 Chrome 120 开始，Manifest V3 扩展程序可以使用延迟时间或周期为 30 秒的 chrome.alarms API，而无需使用 60 秒或更长的值。

发布时间：2023 年 11 月 16 日

Manifest V2 支持时间表已更新。如需了解详情，请参阅我们的2023 年 11 月博文。

发布日期：2023 年 11 月 15 日

如需了解我们如何在新博文中改进 declarativeNetRequest API，请参阅该博文。

Chrome 120 Beta 版已于最近发布。如需简要了解与扩展程序开发者相关的重要更新，请阅读我们的新博文：Chrome 120 中的扩展程序新功能。此版本还标志着一个重要里程碑，因为它从关键平台差距列表中移除了最后两项（userScripts、ChromeOS 上的文件处理程序）。

开发者信息中心内的隐私权政策现在是在商品级添加的。这样，您就可以为每个商品提供不同的隐私权政策。如需详细了解此变更，请参阅我们的PSA。

发布时间：2023 年 10 月 26 日

我们刚刚在 Chrome for Developers YouTube 频道上发布了一段新视频，其中与 Google 开发者专家兼作者 Matt Frisbie 进行了对话。点击此处观看。

我们刚刚发布了有关如何为扩展程序编写自动化测试的新指南，包括如何编写单元测试，以及有关端到端测试的一般指南和教程。

我们刚刚发布了第二期Chrome 扩展程序动态。这篇博文讨论了扩展程序团队在过去几个月内所做的工作，包括解决服务工作线程稳定性问题，以及在弥合所有 MV3 平台差距方面取得的良好进展。我们还分享了即将发布的令人期待的 API，例如 Reading List API 和 User Scripts API。

根据 Web Extensions 社区组中的反馈，我们将启用静态规则集的数量上限从 10 大幅提高到 50。此外，我们将允许的静态规则集总数从 50 个增加到 100 个。此功能目前已在 Canary 中推出。

Manifest V3 的一项要求是，扩展程序不得再使用远程托管的代码。虽然这从一开始就包含在我们的迁移指南中，但我们认为有必要改进有关此问题的指南。该页面现在提供了更多信息，介绍了在 Manifest V3 中仍然可以实现的功能，并提供了有关升级策略的更多信息。

我们还新增了一篇与排查 Chrome 应用商店违规行为相关的文章。新增了一个部分，介绍了具有远程托管代码的扩展程序被拒的常见原因。

发布日期：2023 年 10 月 11 日

从 Chrome 118 开始，chrome.declarativeNetRequest API 中的 isUrlFilterCaseSensitive 属性已更改为默认值为 false。如果您希望保留旧行为，可以在 declarativeNetRequest 规则中将 isUrlFilterCaseSensitive 明确设置为 true。

这遵循了 Web Extensions 社区组中的讨论。Firefox 和 Safari 已经实现了类似的更改。

我们发布了一份新指南，介绍了 Cookie 和 Web 存储 API 在 Chrome 扩展程序中的运作方式。 其中包含有关 Privacy Sandbox 中 Cookie 和存储分区变更的详细信息。Privacy Sandbox 是一个正在进行的项目，旨在通过创建一系列新的 Web 平台 API 来弃用第三方 Cookie，并详细说明这些 API 在扩展程序中的运作方式。

我们最近创建了一个页面，可让您搜索 Chrome 扩展程序示例。搜索页面上有多个选项。您可以使用搜索框搜索示例标题中的文字。您可以按权限或扩展程序 API 限制搜索范围。借助额外的过滤条件，您可以将搜索范围限制为 API 或功能（用例）示例。

这个新的示例网页由 Google Summer of Code 参与者薛舟戴构建，他还贡献了多个新示例。如需了解他们在去年夏天获得的体验，请参阅我们博客上的相关博文。

与之前一样，您仍然可以在 GitHub 上克隆或派生我们的代码示例。

从 Chrome 118 开始，扩展程序需要从 chrome://extensions 页面启用“允许访问文件网址”设置，才能使用 Tabs 或 Windows API 打开 file:// 方案网址。您可以通过调用 chrome.extension.isAllowedFileSchemeAccess() 以编程方式检查此访问权限。Firefox 已经限制了文件网址，而 Safari 支持此项更改。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

之前，通过扩展程序 API 调用触发的针对 tabs.update()、tabs.create() 和 windows.create() 的导航会针对某些 chrome:// 网址发出错误。此外，禁止使用 JavaScript 网址调用 tabs.update()。在 117 中，这些针对 JavaScript 网址的保护措施已扩展到 tabs.create() 方法，并且已将许多其他 chrome:// 网址添加到禁止的网址列表中，该列表适用于上述所有方法。

chrome.declarativeNetRequest API 通过指定声明式规则来阻止或修改网络请求。这样一来，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而为用户提供更高的隐私保护。而且使用起来也很棘手。鉴于此，我们重写了相关指南，以便更清晰地说明如何实现声明性规则集。请点击上方的链接，阅读新部分。

Chrome 应用商店与 Google Analytics 集成，因此除了开发者信息中心提供的视图之外，您还可以查看 Chrome 应用商店商品详情的分析数据。如需了解详情，请参阅将 Google Analytics 账号与 Chrome 应用商店搭配使用。

注入的内容脚本现在默认位于开发者工具的忽略列表中。这不会影响断点，但意味着在调试期间，系统会跳过内容脚本，并忽略这些脚本中的异常。当内容脚本在 Sources 标签页中打开时，如果此功能处于开启状态，系统会显示一条横幅提醒您，并提供用于从忽略列表中移除内容脚本的选项。如需关闭此行为，请打开开发者工具，前往设置，然后前往忽略列表。如需了解详情，请参阅开发者工具的新变化。

Chrome 116 是一个重要的扩展程序版本。您现在可以以编程方式打开侧边栏。借助一种新方法，您可以了解是否存在有效的屏幕外文档。Service Worker 得到了多项改进。116 版中包含的改进非常多，我们专门撰写了一篇博文来介绍这些改进。截至 7 月 19 日，Chrome 116 处于 Beta 版阶段。

我们刚刚发布了有关今年扩展程序变更和改进的概览。该博文讨论了本年度的新功能，包括侧边栏 API、服务工作线程增强功能和屏幕外文档。您还可以了解我们本季度正在开展的工作。该文章列出了更多内容，并提供了指向所有内容的链接。

我们发布了新的 Google Analytics 和地理位置信息指南及示例：

现在，您可以在调用 chrome.offscreen.createDocument() 时指定多个 reason 枚举。当屏幕外文档将用于多种不同用途时，请使用此方法。浏览器会使用提供的原因来确定屏幕外文档的生命周期。

我们刚刚发布了扩展程序更新测试工具，这是一个本地扩展程序更新服务器，可在本地开发期间用于测试 Chrome 扩展程序的更新，包括权限授予。该工具会显示用户的更新流程，包括在用户授予任何新请求的权限之前，保持扩展程序处于停用状态。此工具对于模拟将扩展程序从 Manifest V2 更新到 Manifest V3 时所请求的权限变更特别有用。

我们推出了新的 Side Panel API，这是一个配套界面，可让用户在浏览内容的同时访问工具。如需了解详情，请参阅边栏 API 参考文档。此外，我们还在 GitHub 示例代码库中添加了许多侧边栏示例。我们还在新博文使用新的侧边栏 API 设计出色的用户体验中详细介绍了侧边栏。我们还审核了质量指南政策和最佳实践，以便为创建高质量的侧边栏扩展程序提供更多指导。

您的反馈对于打造此 API 至关重要；请在 chromium-groups 中分享您的想法和功能请求。我们会继续改进侧边栏 API，敬请关注最新动态。

我们提供了两个新示例，演示了如何在扩展程序中使用 WASM：

特别感谢 GitHub 贡献者 @daidr 提供这些示例。

我们更新了 Manifest V3 迁移指南的已知问题部分，其中包含一份更新后的扩展平台差距列表，我们打算在宣布新的 Manifest V2 弃用时间表之前弥合这些差距。

我们刚刚发布了一篇新文章，名为音频录制和屏幕捕获，其中介绍了如何在 Manifest V3 中录制标签页、窗口或屏幕中的音频或视频。本文介绍了涉及 chrome.tabCapture API 和 getDisplayMedia() 函数的多种录制方法。

我们已将 storage.local 属性的配额增加到大约 10 MB。这是 Web Extensions Community Group 中达成的共识。这使得 storage.local 与 Chrome 112 中更改的 storage.session 保持一致。

Service Worker 是 Chrome 扩展程序不可或缺的一部分。我们刚刚发布了一篇教程，介绍了注册、调试和与 Service Worker 互动的基本知识。我们还添加了新的服务工作线程指南，其中更详细地介绍了重要概念。我们将在未来几个月内扩充此部分的内容。

为了帮助您在 Chrome 应用商店中发布内容，我们在以下两个方面添加了新指南。最基本的功能指南的重点在于为用户提供益处并丰富其浏览体验。联属营销广告指南旨在让用户了解广告客户使用联属营销链接或代码创收的扩展服务，并通过要求用户在添加之前执行操作来赋予用户一定程度的控制权。

我们重写了扩展程序清单转换器的 README，以便您更轻松地了解运行该工具后需要执行的操作。转换器可帮助将基于 Manifest V2 构建的扩展程序迁移到 Manifest V3。新版 README 使用与迁移指南的清单中非常相似的字词描述了该工具的功能。转换器并非万能，但确实可以省去许多不需要人工判断的任务。

我们为 Offscreen Documents API 添加了两种新的原因类型。使用 LOCAL_STORAGE 访问 Web 平台的 localStorage API。创建网页工作器时使用 WORKER。

Chrome 应用商店开发者信息中心现在支持 Google Analytics 4 (GA4)。我们简化了 Google Analytics 的设置流程，并使群组发布商的访问权限管理更加简单明了。如果您之前使用 Google Universal Analytics 跟踪您的商店详情活动，则需要在 2023 年 7 月 1 日之前采取行动，以确保您能够继续接收有关商店详情的数据。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

文件处理程序 API 可在 ChromeOS Canary 版中进行实验，适用于 112 和 113 版。它允许 ChromeOS 上的扩展程序打开具有指定 MIME 类型和文件扩展名的文件。如需实现文件处理，请向 manifest.json 添加一组规则。此功能的工作方式与渐进式 Web 应用相同。如需了解详情，请参阅本网站上的这篇文章。

我们希望在 6 月下旬推出 Chrome 115 时发布此功能。请关注此空间，了解最新动态。

我们为 chrome.scripting API 构建了一个新示例。它演示了动态声明（在运行时注册内容脚本）和程序化注入（在已打开的标签页中执行脚本）。

我们提供了三个新示例，用于演示声明式网络请求 API。每个示例都展示了单个用例的实现。第一个示例展示了如何屏蔽 Cookie。其余两个示例演示了如何屏蔽和重定向网址。

自 Chrome 112 起，storage.session 属性的配额已增加到大约 10 MB。Web Extensions Community Group 已就此达成一致：https://github.com/w3c/webextensions/issues/350

Manifest V3 扩展程序现在支持屏幕外文档。这些 API 可支持与 DOM 相关的功能，从而帮助您从后台网页过渡到扩展程序服务工作线程。如需了解详情，请阅读此博文。

chrome.action.isEnabled() 方法以编程方式检查是否已为特定标签页启用扩展程序。这样一来，您就无需维护标签页的启用状态。此新方法接受标签页 ID 和对回调的引用，并返回一个布尔值。但它有一个限制：使用 chrome.declarativeContent 创建的标签页始终返回 false。

（chrome.action 命名空间最近新增了一些用于控制扩展程序徽章外观的方法。如需了解详情，请参阅设置徽章颜色。）

以前，扩展程序服务工作线程通常会在 5 分钟时关闭。我们已更改此行为，使其更接近于 Web 上的 Service Worker 生命周期。扩展程序服务工作线程会在闲置 30 秒后关闭，或者在单个活动的处理时间超过 5 分钟时关闭。如需了解详情，请参阅延长扩展服务工作器的生命周期。

我们正在审核 Manifest V2 弃用时间表，并推迟原定于 2023 年初进行的实验。如需了解详情，请阅读 Chrome 扩展程序邮寄名单中的更新。

chrome.action 命名空间新增了两种方法，可让您更好地控制外观扩展程序徽章。setBadgeTextColor() 和 getBadgeTextColor() 方法允许扩展程序更改和查询其工具栏图标的徽章文本颜色。与 setBadgeBackgroundColor 和 getBadgeBackgroundColor 搭配使用时，这些新方法可让您强制保持设计和品牌的一致性。

我们明确了 Manifest V2 弃用时间表。Manifest V2 支持时间表也已更新，以反映此信息。

我们整理了一份目前正在开发中的主要功能和公开 bug 的列表。我们希望通过此页面帮助开发者更好地了解平台的当前状态，以及在为未来做准备时可以考虑哪些功能。

Chrome 应用商店已从开发者信息中心的商品详情标签页中移除了“大型宣传块”上传界面。由于这些图片未在消费者界面中使用，因此此次变更不会影响最终用户体验。如需了解详情，请参阅这篇 chromium-extensions 博文。

根据 crbug.com/1219825#c11，不透明源（例如沙盒 iframe 和动态导入）也应该能够访问可通过网络访问的资源。

之前，调用异步 API 的 Manifest V3 可以提供无效的最终实参，而 Chrome 不会出错。通过此修复，Chrome 现在可以正确报告错误，并指出没有匹配的签名。建议开发者在 Canary 上检查其扩展程序是否存在任何错误，以免因意外使用错误的签名进行 API 调用而导致此 bug 修复破坏扩展程序。

Chrome 应用商店为 Chrome 应用商店开发者信息中心推出了经过改进的商品分析体验。新信息中心可让您一目了然地了解情况，并提前整合最有用的信息。如需了解详情，请阅读这篇博文。

Identity API 上的函数现在支持基于 Promise 的调用。这会略微改变 identity.getAuthToken() 的界面，其中设置为基于 Promise 的调用的异步返回将具有“token”和“grantedScopes”作为单个对象上的参数（而不是回调版本将它们作为单独的实参接收到回调中）。

Manifest V3 扩展程序现在可以使用新的网址格式 chrome-extension://<id>/_favicon/ 访问收藏夹图标，其中 是扩展程序的 ID。这取代了 Manifest V2 平台的 chrome://favicons API。如需了解详情，请参阅 Favicon API 文档。

添加了交易者/非交易者开发者身份标识，可提醒开发者准确自行声明其交易者/非交易者身份。

Chrome 不再默认向扩展程序授予 script-src: wasm-unsafe-eval。使用 WebAssembly 的扩展程序现在必须在其 content_security_policy 声明中明确添加此指令和值到 extension_pages。

在 chrome://extensions/shortcuts 上更改 Manifest V3 扩展程序的键盘快捷键时，更新现在会立即应用。之前，必须重新加载扩展程序，更改才会生效。

动态注册的内容脚本现在可以指定要将资源注入到的 world。如需了解详情，请参阅 scripting.registerContentScripts()。

Manifest V3 扩展程序现在可以在 manifest.json 中指定 optional_host_permissions 键。这样一来，Manifest V3 扩展程序就可以像 Manifest V2 扩展程序那样，使用 optional_permissions 键来声明主机的可选匹配模式。

chrome.scripting.executeScript() 现在接受其 injection 实参中的可选 injectImmediately 属性。如果存在且设置为 true，脚本将尽快注入到目标中，而不是等待 document_idle。请注意，这并不能保证脚本会在网页加载之前注入，因为在进行 API 调用的同时，网页会继续加载。

现在，基于 Service Worker 的扩展程序可以使用 Omnibox API。之前，由于内部依赖于 DOM 功能，此 API 的某些方法会在调用时抛出异常。

Manifest V3 扩展程序现在可以在其 content_security_policy 声明中包含 wasm-unsafe-eval。此变更允许 Manifest V3 扩展程序使用 WebAssembly。

Manifest V3 扩展程序现在可以使用内存存储空间 storage.session。

在 Chrome 应用商店中发现内容一文概述了用户如何在 Chrome 应用商店中查找商品，以及我们的编辑如何选择要重点展示的商品。

declarativeNetRequest 规则条件已更新，以便扩展程序能够根据请求的“request”和“initiator”网域更好地定位请求。相关的条件属性为 initiatorDomains、excludedInitiatorDomains、requestDomains 和 excludedRequestDomains。另请参阅此 chromium-extensions 帖子。

修复了长期存在的问题：在新建的标签页或窗口上调用 scripting.executeScript() 可能会失败。

在扩展程序的服务工作线程中使用 chrome.runtime.connectNative() 连接到原生消息传递主机应使服务工作线程在端口打开期间保持活跃状态。

omnibox.setDefaultSuggestion() 方法现在会返回一个 promise 或接受一个回调，以允许开发者确定建议何时已正确设置。

扩展程序服务工作线程上下文现在支持 chrome.i18n.getMessage() API。

内容脚本现在可以指定 match_origin_as_fallback 键，以注入到与匹配框架相关的框架中，包括具有 about:、data:、blob: 和 filesystem: 网址的框架。如需了解详情，请参阅内容脚本文档。

发布时间：2021 年 12 月 30 日

基于 Service Worker 的 Manifest V2 和 Manifest V3 扩展程序现在可以使用 Fetch API 请求 file: 方案网址。访问 file: 方案网址仍需要用户在 chrome://extensions 页面中为扩展程序启用“允许访问文件网址”。

发布时间：2021 年 12 月 28 日

为基于 Manifest V3 构建的扩展程序向 tabs.sendMessage、runtime.sendMessage 和 runtime.sendNativeMessage 添加了 Promise 支持。

发布时间：2021 年 12 月 10 日

添加了新参考页面，其中概述了 Chrome 应用商店审核流程，并说明了如何处理开发者计划政策的违规行为。

脚本 API 的 executeScript() 和 insertCSS() 方法现在接受多个文件。以前，这些方法需要一个包含单个文件条目的数组。

发布日期：2021 年 10 月 27 日

我们更新了排查 Chrome 应用商店违规行为页面，为开发者提供了有关常见拒绝原因的更详细指南。

此版本包含的 promise 更新明显多于任何之前的版本。更新包括常规扩展程序 API 和 ChromeOS 专用扩展程序 API。展开即可下部分即可查看详细信息。

许多 API 现在在清单 V3 中支持 Promise。

此外，使用 ChromeSetting 原型的 API 现在也支持 promise。以下 API 会受到此项变更的影响。

chrome.scripting API 现在支持在运行时注册、更新、取消注册和获取列表内容脚本。以前，内容脚本只能在扩展程序的 manifest.json 中静态声明，或者在运行时通过 chrome.scripting.executeScript() 以编程方式注入。

这篇博文中公布了从 Manifest V2 到 V3 的过渡时间表，并发布了更详细的时间表页面。

借助新的 declarativeNetRequestWithHostAccess 权限，扩展程序可以在具有主机权限的网站上使用 chrome.declarativeNetRequest API。这还允许使用 webRequest、webRequestBlocking 和特定于网站的主机权限的现有 Manifest V2 扩展程序迁移到 chrome.declarativeNetRequest API，而无需用户批准新权限。

chrome.scripting API 的 executeScript() 方法现在可以直接将脚本注入到网页的主世界中。以前，扩展程序只能直接注入到扩展程序的隔离世界中。如需详细了解隔离的世界，请参阅有关内容脚本的文档。

Manifest V3 版 chrome.storage API 中的方法现在会返回 promise。

我们已更新 2021 年 6 月 29 日发布的政策更新博文，以更正两步验证部署时间表。

chrome.declarativeNetRequest 现在支持指定最多 50 个静态规则集 (MAX_NUMBER_OF_STATIC_RULESETS)，并同时启用最多 10 个规则集 (MAX_NUMBER_OF_ENABLED_STATIC_RULESETS)。

现在，Manifest V2 和 Manifest V3 扩展程序都可以选择启用跨源隔离。此功能可限制哪些跨源资源可以加载扩展程序的网页，并支持使用 SharedArrayBuffer 等低级 Web 平台功能。从 Chrome 95 版开始，必须选择启用。

我们更新了 Chrome 应用商店开发者计划政策，对欺骗性安装策略、垃圾内容和重复性内容政策进行了阐明。 此更新还新增了一项要求，即必须进行两步验证才能在 Chrome 应用商店中发布内容。如需了解详情，请阅读这篇博文。

Chrome 扩展程序多年来一直使用 chrome.browserAction 和 chrome.pageActions API，但 Manifest V3 将两者都替换为通用的 chrome.actions API。这篇博文探讨了这些 API 的历史记录以及 Manifest V3 中的变化。阅读帖子。

chrome.scripting API 是一项新的 Manifest V3 API，专注于脚本。在这篇博文中，我们将深入探讨此项变更的动机，并仔细了解其新功能。阅读帖子。

Chrome 现在支持在 Service Worker 中使用 JavaScript 模块。如需在清单中指定模块，请执行以下操作：

这会将 worker 脚本加载为 ES 模块，从而让您可以在 worker 的脚本中使用 import 关键字来导入其他模块。

新的 chrome.action.getUserSettings() 方法允许扩展程序确定用户是否已将扩展程序固定到主工具栏。

新的 chrome.scripting.removeCSS() 方法允许扩展程序移除之前通过 chrome.scripting.insertCSS() 插入的 CSS。它取代了 chrome.tabs.removeCSS()。

chrome.scripting.executeScript() 现在支持返回 promise。如果脚本执行的最终值是 Promise，Chrome 会等待 Promise 得到解决，并返回其最终值。

从 chrome.scripting.executeScript() 返回的结果现在包含 frameId。frameId 属性表示结果来自哪个框架，以便扩展程序在注入多个框架时轻松将结果与各个框架相关联。

新的 chrome.tabGroups API 和 chrome.tabs 中的新功能可让扩展程序读取和操纵标签页组。 需要使用 Manifest V3。

发布日期：2020 年 12 月 23 日

Manifest V3 中的可供 Web 访问的资源定义已发生变化，可让扩展程序根据请求者的来源或扩展程序 ID 限制资源访问权限。

Chrome 扩展程序团队已开源“扩展程序清单转换器”，这是一款 Python 工具，可自动执行将扩展程序转换为 Manifest V3 的部分机械性工作。请参阅公告博文，并从 GitHub 获取。

Manifest V3 是对扩展平台进行的一项重大更新；如需了解新功能和变更功能的摘要，请参阅 Manifest V3 概览。扩展程序目前可以继续使用 Manifest V2，但我们会在不久的将来逐步淘汰这一版本。我们强烈建议您为所有新扩展程序使用 Manifest V3，并尽快开始将现有扩展程序迁移到 Manifest V3。

**Examples:**

Example 1 (unknown):
```unknown
"background": {
  "service_worker": "script.js",
  "type": "module"
}
```

---

## chrome.sessions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/sessions/?hl=zh-cn

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

## Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/whats-new

**Contents:**
- Chrome 扩展程序的新变化 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 视频：解答有关 Chrome 应用商店可发现性的问题
- Chrome 140：新增了 sidePanel.getLayout() API
- 新指南：扩展程序更新生命周期
- Chrome 139：在 Chrome 品牌 build 中移除 --extensions-on-chrome-urls 和 --disable-extensions-except flag
- Chrome 138：对新标签页的更改
- 博文：在即将发生的书签变更之前更新扩展程序
- 博文：2025 年 6 月 Chrome 扩展程序的最新动态
- 视频：在浏览器中玩打地鼠游戏 - 这是真的吗？
- 视频：Chrome 的新扩展程序菜单说明

请经常查看此页面，了解 Chrome 扩展程序、扩展程序文档或相关政策或其他方面的变化。您可以在 Chrome 扩展程序邮寄名单中找到其他通知。Chrome 时间表列出了稳定版和 Beta 版的发布日期。

发布日期：2025 年 11 月 25 日

在最新视频中，我们会解答您在 Chrome 应用商店中发现应用方面的问题。

从 Chrome 140 开始，您可以使用新的 sidePanel.getLayout() API 来确定侧边栏位于屏幕的左侧还是右侧。如果您支持 RTL 语言，而新安装的 Chrome 的默认语言不同，此功能尤为有用。

我们发布了一份新指南，说明了 Chrome 中扩展程序的更新方式。

从 Chrome 139 开始，官方 Chrome 品牌 build 中将移除 --extensions-on-chrome-urls 和 --disable-extensions-except 命令行标志。详细了解邮寄名单。

从 Chrome 138 开始，我们将更新新标签页界面，添加新的页脚。 您可以访问邮寄名单页面了解详情。

我们将对书签同步功能进行一些更改，这可能会影响您的扩展程序。如需了解详情，请参阅这篇博文。

我们一直在忙碌，推出了 Google I/O 大会，并在 Chrome 和 Chrome 应用商店中推出了多项新功能。请参阅Chrome 扩展程序最新动态 - 2025 年 6 月，了解最新资讯！

观看我们的最新视频，了解如何在浏览器中制作游戏。

观看我们的最新视频“Chrome 的新扩展程序菜单详解” ，了解实验性的新扩展程序菜单。

在“扩展程序真棒”第 1 集中了解如何开始开发扩展程序，并在第 2 集中了解 Chrome 自定义功能的灵活性！

从 Chrome 135 开始，chrome.userScripts API 中提供了一个新的 userScripts.execute() 方法。您可以使用此方法在任意时间注入用户脚本一次，而无需永久注册该脚本。

从 Chrome 132 开始，您可以在开发者工具中查看和修改使用 chrome.storage API 存储的数据。如需了解详情，请参阅开发者工具文档中的新页面查看和修改扩展程序存储空间。

在 2024 年 Google I/O 大会上，我们分享了扩展程序菜单即将发生的一些早期设计变更，这些变更可让用户更好地控制扩展程序可以访问的网站。我们很快就会开始测试这些变更，首先会在 Canary 中面向一小部分用户进行测试，并希望将来能更广泛地推出这些变更。

我们还推出了 chrome.permissions.addHostAccessRequest() API。

发布日期：2024 年 11 月 19 日

从 Chrome 132 开始，Tabs API 中的 frozen 属性用于指示标签页是否已被浏览器冻结。发送到冻结标签页的消息将排队，并在标签页解除冻结后处理。

发布日期：2024 年 11 月 12 日

扩展程序专用 Prompt API 现已在初始源试用中提供，因此您可以在浏览器中构建使用 Gemini Nano（我们最高效的语言模型）的 Chrome 扩展程序。

加入 Prompt API 源试用（在 Chrome 131 至 136 中进行），并分享您的反馈。您的反馈可以直接影响我们构建和实现此 API 和所有内置 AI API 的未来版本的方式。

发布日期：2024 年 10 月 17 日

现在，我们又可以来盘点一下 Chrome 扩展程序方面的最新动态了：我们在 AI 集成、新 API、活动和视频方面都有令人兴奋的更新。如需了解详情，请参阅 Chrome 扩展程序 10 月刊！

发布日期：2024 年 10 月 17 日

Chrome 推出了内置 AI 挑战赛：诚邀您使用 Chrome 的集成 AI 模型和 API 创建创新的 Web 应用和 Chrome 扩展程序，赢取总计 65,000 美元的奖品。

如需注册并详细了解相关信息，请访问 Built-in AI Challenge 网站。我们迫不及待地想看看您在为 Web 注入 AI 后会创作出什么作品！

从 Chrome 130 开始，action.onUserSettingsChanged 事件可用。这是根据 WebExtensions 社区组中的一项提案实现的。感谢 Microsoft 为 Chromium 做出的贡献。

从 Chrome 130 开始，getKeys() 方法可在 chrome.storage API 使用的 StorageArea 接口上使用。这是根据 WebExtensions 社区组中的提案实现的。

从 Chrome 128 开始，我们将在 Declarative Net Request API 中添加对响应标头匹配的支持。这是一个常见的要求，尤其是在匹配 Content-Type 标头时，我们与 WebExtensions 社区组一起设计了一个合适的 API。

我们已更新 API 参考文档，以纳入新的 responseHeaders 和 excludedResponseHeaders 字段。您可以使用这些方法来检查指定标头的存在情况和值。

在此次更新中，我们在文档中添加了一个新的规则评估部分，其中介绍了规则的匹配方式。对于标头匹配，规则只能在收到响应标头后运行，因此它们的应用阶段比其他规则晚。这意味着，请求在被屏蔽或重定向之前确实到达了服务器。

了解 Chrome 扩展程序中的内容脚本，包括如何注册 CSS 和 JavaScript 以在特定网页上运行。观看完整视频。

Chrome 应用商店团队发布了一系列更新，对开发者计划政策页面进行了修改，旨在鼓励开发优质产品、防止欺骗性行为，并确保用户在知情的情况下同意。Chrome 应用商店政策经理 Rebecca Soares 在 Chrome 扩展程序：重要政策更新这篇博文中总结了所有更新。

在过去三个月内，我们推出了一些重大更新和新功能，包括开始逐步淘汰清单 V2。快来了解 Chrome 扩展程序 7 月刊中的最新动态！

Chrome 扩展程序团队的 Patrick 介绍了 Chrome 扩展程序中远程托管代码 (RHC) 的概念。了解为何不再允许使用 RHC、如何检测 RHC，以及如果您的扩展程序需要更新，该怎么做。观看完整视频。

从 Chrome 127 开始，所有扩展程序都可以使用 action.openPopup API。以前，它仅在 Canary 中或通过政策安装的扩展程序中可用。

Chrome 扩展程序 DevRel 团队与负责 Chrome 应用商店审核的 Trust & Safety 团队进行了交流，询问了您提出的问题。观看完整视频。

从 6 月 3 日开始，在 Chrome Beta 版、Dev 版和 Canary 版渠道中，如果用户仍安装了 Manifest V2 扩展程序，那么当他们访问扩展程序管理页面 (chrome://extensions) 时，部分用户会开始看到警告横幅，告知他们所安装的部分（Manifest V2）扩展程序很快将不再受支持。如需了解详情，请参阅官方公告

我们最近对侧边栏界面进行了一些更改，包括添加了固定图标并移除了全局侧边栏图标。如需了解详情，请参阅公开服务公告 (PSA)，并查看我们更新的文档和示例。

又一届 Google I/O 大会已经落幕，我们报道了所有令人兴奋的扩展程序更新！前往 YouTube 观看完整视频，并阅读我们的博文，了解一些精彩内容。

现在，当您使用 Declarative Net Request API 时，Chrome 应用商店允许您跳过对符合条件的更改的审核。如需详细了解资格要求以及如何选择启用，请参阅 Chrome 应用商店文档。

我们最近更新了 Chrome 应用商店 API 文档，添加了有关 deployPercentage 的信息。借助该 API，您可以分配部分发布部署的百分比。了解 deployPercentage。

Chrome 126 引入了一个新的 manifest.json 字段 - trial_tokens，让您可以在所有扩展程序界面中选择加入源试用和弃用试用。如需了解详情，请参阅指南。

我们发布了新一期Chrome 扩展程序动态。该帖子讨论了扩展程序团队在过去几个月中的工作。这包括：Chrome 应用商店中的版本回滚、更好的 Firebase Auth 支持以及更多 API 发布和更新。

将扩展程序回滚到 Chrome 应用商店中之前发布的版本，无需额外审核！如需了解详情，请参阅这篇博文和文档。

ChromeOS 上现已提供高级 documentScan API，用于发现和检索连接的文档扫描仪中的图片。

自 Chrome 124 起，服务工作线程支持 WebGPU。如需快速入门，请查看 WebGPU 扩展程序示例。

Events API 现在支持按无类别域间路由 (CIDR) 区块进行过滤。CIDR 块是共享相同网络前缀和相同位数的 IP 地址集合。以前，如果开发者需要过滤多个 IP 地址，则需要为屏蔽范围内的每个地址配置过滤规则。现在，当扩展程序调用 addListener() 时，传入的规则意味着只有当网址的主机部分是 IP 地址且包含在数组中指定的任何 CIDR 块中时，才会调用事件处理脚本。

在 Chrome 应用商店中，清单文件 (manifest.json) 中扩展程序的 "name" 字段现在有 75 个字符的通用限制。之前，英文的限制为 45 个字符，其他语言区域的 "name" 字段没有限制。

此功能最初旨在允许存在文化和语言差异，而这些差异可能无法用相同数量的字符来表达。遗憾的是，一小部分开发者滥用了此功能，向商店发送垃圾内容。因此，我们推出了新的通用限制，将字符数上限提高到 75 个。 此限制涵盖了目前商店中的几乎所有扩展程序，因此您很可能无需因这一变化而采取任何行动。如果您尝试上传的扩展程序的名称超过了上限，商店会阻止该上传操作。

在这篇由 eyeo 的扩展程序引擎团队撰写的博文中，我们将探讨测试扩展程序服务工作线程的问题。在 Manifest V2 中，扩展程序位于后台网页中，在整个扩展程序生命周期内都处于唤醒状态。Manifest V3 使用的是服务工作器，而服务工作器在不需要时会关闭，从而节省资源。这会带来一定的测试挑战。这篇博文介绍了 eyeo 如何应对这些挑战。

当设备进入休眠状态时，使用 chrome.alarms API 设置的闹钟不再延迟。当设备唤醒时，无论错过了多少闹钟，闹钟都会响一次。例如，假设闹钟设置为每小时响一次，而设备在凌晨 12:55 到凌晨 2:05 处于休眠状态，那么只有凌晨 2:00 的闹钟会触发 onAlarm 事件。它会在尽可能接近凌晨 2:00 时触发，如果设备处于休眠状态，则会在设备唤醒时立即触发。

此更改使 Chrome 符合 Web 扩展程序社区组中达成的行为一致性。

往返缓存 (bfcache) 是一种浏览器优化，可实现即时后退和前进导航。从 Chrome 123 开始，当具有开放扩展程序端口的网页存储在 bfcache 中时，消息渠道会关闭，这意味着不会向该网页发送任何消息。因此，扩展程序脚本应监听 onDisconnect 等生命周期事件，并在网页从 BFCache 恢复时设置新连接。

如需了解详情和查看示例代码，请参阅扩展消息端口对 BFCache 行为的更改。

我们已完成对所有异步扩展 API 方法的 Promise 支持实现。这样做是为了通过改进处理异步操作的人体工程学来使 API 方法现代化。少数方法（例如 desktopCapture.chooseDesktopMedia()）仍仅支持回调，因为其当前界面与 Promise 不兼容。为了实现向后兼容性，我们仍支持回调。如果您发现 Promise 失败，请提交 bug 报告。

我们刚刚发布了有关扩展程序中实时选项的指南。实时更新功能可提供从服务器直接到扩展程序安装的即时通信路径。此外，我们还针对使用 chrome.gcm、Web 推送提供了新的指南。

我们刚刚发布了一篇指南，介绍了如何使用 Puppeteer 测试 Service Worker 终止。随附的示例在 Puppeteer 和 Selenium 中演示了这一点。

我们刚刚发布了原生消息的更新版示例。此 API 允许您的扩展程序启动另一个应用并与之通信。感谢 GitHub 贡献者 Shubham-Rasal 为此做出的贡献。

向 tabs.Tab 对象添加了一个名为 lastAccessed 的新属性。此属性表示标签页上次处于活动状态的时间。返回的值以毫秒为单位，从纪元起算。

在从 Manifest V2 更改为 Manifest V3 的过程中，"background" 清单键的子项发生了更改，以适应将后台脚本替换为扩展程序服务工作线程。以前，如果将 Manifest V2 键 "scripts"、"page" 或 "persistent" 添加到 Manifest V3 扩展程序的 "background" 键中，系统会抛出错误。现在，如果存在这些键，系统会触发警告。

这样做是为了能够根据社区组中的提案，在多个浏览器中的扩展程序中使用单个清单文件。

发布日期：2023 年 12 月 14 日

从 Chrome 120 开始，Manifest V3 扩展程序可以使用延迟时间或周期为 30 秒的 chrome.alarms API，而无需使用 60 秒或更长的值。

发布时间：2023 年 11 月 16 日

Manifest V2 支持时间表已更新。如需了解详情，请参阅我们的2023 年 11 月博文。

发布日期：2023 年 11 月 15 日

如需了解我们如何在新博文中改进 declarativeNetRequest API，请参阅该博文。

Chrome 120 Beta 版已于最近发布。如需简要了解与扩展程序开发者相关的重要更新，请阅读我们的新博文：Chrome 120 中的扩展程序新功能。此版本还标志着一个重要里程碑，因为它从关键平台差距列表中移除了最后两项（userScripts、ChromeOS 上的文件处理程序）。

开发者信息中心内的隐私权政策现在是在商品级添加的。这样，您就可以为每个商品提供不同的隐私权政策。如需详细了解此变更，请参阅我们的PSA。

发布时间：2023 年 10 月 26 日

我们刚刚在 Chrome for Developers YouTube 频道上发布了一段新视频，其中与 Google 开发者专家兼作者 Matt Frisbie 进行了对话。点击此处观看。

我们刚刚发布了有关如何为扩展程序编写自动化测试的新指南，包括如何编写单元测试，以及有关端到端测试的一般指南和教程。

我们刚刚发布了第二期Chrome 扩展程序动态。这篇博文讨论了扩展程序团队在过去几个月内所做的工作，包括解决服务工作线程稳定性问题，以及在弥合所有 MV3 平台差距方面取得的良好进展。我们还分享了即将发布的令人期待的 API，例如 Reading List API 和 User Scripts API。

根据 Web Extensions 社区组中的反馈，我们将启用静态规则集的数量上限从 10 大幅提高到 50。此外，我们将允许的静态规则集总数从 50 个增加到 100 个。此功能目前已在 Canary 中推出。

Manifest V3 的一项要求是，扩展程序不得再使用远程托管的代码。虽然这从一开始就包含在我们的迁移指南中，但我们认为有必要改进有关此问题的指南。该页面现在提供了更多信息，介绍了在 Manifest V3 中仍然可以实现的功能，并提供了有关升级策略的更多信息。

我们还新增了一篇与排查 Chrome 应用商店违规行为相关的文章。新增了一个部分，介绍了具有远程托管代码的扩展程序被拒的常见原因。

发布日期：2023 年 10 月 11 日

从 Chrome 118 开始，chrome.declarativeNetRequest API 中的 isUrlFilterCaseSensitive 属性已更改为默认值为 false。如果您希望保留旧行为，可以在 declarativeNetRequest 规则中将 isUrlFilterCaseSensitive 明确设置为 true。

这遵循了 Web Extensions 社区组中的讨论。Firefox 和 Safari 已经实现了类似的更改。

我们发布了一份新指南，介绍了 Cookie 和 Web 存储 API 在 Chrome 扩展程序中的运作方式。 其中包含有关 Privacy Sandbox 中 Cookie 和存储分区变更的详细信息。Privacy Sandbox 是一个正在进行的项目，旨在通过创建一系列新的 Web 平台 API 来弃用第三方 Cookie，并详细说明这些 API 在扩展程序中的运作方式。

我们最近创建了一个页面，可让您搜索 Chrome 扩展程序示例。搜索页面上有多个选项。您可以使用搜索框搜索示例标题中的文字。您可以按权限或扩展程序 API 限制搜索范围。借助额外的过滤条件，您可以将搜索范围限制为 API 或功能（用例）示例。

这个新的示例网页由 Google Summer of Code 参与者薛舟戴构建，他还贡献了多个新示例。如需了解他们在去年夏天获得的体验，请参阅我们博客上的相关博文。

与之前一样，您仍然可以在 GitHub 上克隆或派生我们的代码示例。

从 Chrome 118 开始，扩展程序需要从 chrome://extensions 页面启用“允许访问文件网址”设置，才能使用 Tabs 或 Windows API 打开 file:// 方案网址。您可以通过调用 chrome.extension.isAllowedFileSchemeAccess() 以编程方式检查此访问权限。Firefox 已经限制了文件网址，而 Safari 支持此项更改。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

之前，通过扩展程序 API 调用触发的针对 tabs.update()、tabs.create() 和 windows.create() 的导航会针对某些 chrome:// 网址发出错误。此外，禁止使用 JavaScript 网址调用 tabs.update()。在 117 中，这些针对 JavaScript 网址的保护措施已扩展到 tabs.create() 方法，并且已将许多其他 chrome:// 网址添加到禁止的网址列表中，该列表适用于上述所有方法。

chrome.declarativeNetRequest API 通过指定声明式规则来阻止或修改网络请求。这样一来，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而为用户提供更高的隐私保护。而且使用起来也很棘手。鉴于此，我们重写了相关指南，以便更清晰地说明如何实现声明性规则集。请点击上方的链接，阅读新部分。

Chrome 应用商店与 Google Analytics 集成，因此除了开发者信息中心提供的视图之外，您还可以查看 Chrome 应用商店商品详情的分析数据。如需了解详情，请参阅将 Google Analytics 账号与 Chrome 应用商店搭配使用。

注入的内容脚本现在默认位于开发者工具的忽略列表中。这不会影响断点，但意味着在调试期间，系统会跳过内容脚本，并忽略这些脚本中的异常。当内容脚本在 Sources 标签页中打开时，如果此功能处于开启状态，系统会显示一条横幅提醒您，并提供用于从忽略列表中移除内容脚本的选项。如需关闭此行为，请打开开发者工具，前往设置，然后前往忽略列表。如需了解详情，请参阅开发者工具的新变化。

Chrome 116 是一个重要的扩展程序版本。您现在可以以编程方式打开侧边栏。借助一种新方法，您可以了解是否存在有效的屏幕外文档。Service Worker 得到了多项改进。116 版中包含的改进非常多，我们专门撰写了一篇博文来介绍这些改进。截至 7 月 19 日，Chrome 116 处于 Beta 版阶段。

我们刚刚发布了有关今年扩展程序变更和改进的概览。该博文讨论了本年度的新功能，包括侧边栏 API、服务工作线程增强功能和屏幕外文档。您还可以了解我们本季度正在开展的工作。该文章列出了更多内容，并提供了指向所有内容的链接。

我们发布了新的 Google Analytics 和地理位置信息指南及示例：

现在，您可以在调用 chrome.offscreen.createDocument() 时指定多个 reason 枚举。当屏幕外文档将用于多种不同用途时，请使用此方法。浏览器会使用提供的原因来确定屏幕外文档的生命周期。

我们刚刚发布了扩展程序更新测试工具，这是一个本地扩展程序更新服务器，可在本地开发期间用于测试 Chrome 扩展程序的更新，包括权限授予。该工具会显示用户的更新流程，包括在用户授予任何新请求的权限之前，保持扩展程序处于停用状态。此工具对于模拟将扩展程序从 Manifest V2 更新到 Manifest V3 时所请求的权限变更特别有用。

我们推出了新的 Side Panel API，这是一个配套界面，可让用户在浏览内容的同时访问工具。如需了解详情，请参阅边栏 API 参考文档。此外，我们还在 GitHub 示例代码库中添加了许多侧边栏示例。我们还在新博文使用新的侧边栏 API 设计出色的用户体验中详细介绍了侧边栏。我们还审核了质量指南政策和最佳实践，以便为创建高质量的侧边栏扩展程序提供更多指导。

您的反馈对于打造此 API 至关重要；请在 chromium-groups 中分享您的想法和功能请求。我们会继续改进侧边栏 API，敬请关注最新动态。

我们提供了两个新示例，演示了如何在扩展程序中使用 WASM：

特别感谢 GitHub 贡献者 @daidr 提供这些示例。

我们更新了 Manifest V3 迁移指南的已知问题部分，其中包含一份更新后的扩展平台差距列表，我们打算在宣布新的 Manifest V2 弃用时间表之前弥合这些差距。

我们刚刚发布了一篇新文章，名为音频录制和屏幕捕获，其中介绍了如何在 Manifest V3 中录制标签页、窗口或屏幕中的音频或视频。本文介绍了涉及 chrome.tabCapture API 和 getDisplayMedia() 函数的多种录制方法。

我们已将 storage.local 属性的配额增加到大约 10 MB。这是 Web Extensions Community Group 中达成的共识。这使得 storage.local 与 Chrome 112 中更改的 storage.session 保持一致。

Service Worker 是 Chrome 扩展程序不可或缺的一部分。我们刚刚发布了一篇教程，介绍了注册、调试和与 Service Worker 互动的基本知识。我们还添加了新的服务工作线程指南，其中更详细地介绍了重要概念。我们将在未来几个月内扩充此部分的内容。

为了帮助您在 Chrome 应用商店中发布内容，我们在以下两个方面添加了新指南。最基本的功能指南的重点在于为用户提供益处并丰富其浏览体验。联属营销广告指南旨在让用户了解广告客户使用联属营销链接或代码创收的扩展服务，并通过要求用户在添加之前执行操作来赋予用户一定程度的控制权。

我们重写了扩展程序清单转换器的 README，以便您更轻松地了解运行该工具后需要执行的操作。转换器可帮助将基于 Manifest V2 构建的扩展程序迁移到 Manifest V3。新版 README 使用与迁移指南的清单中非常相似的字词描述了该工具的功能。转换器并非万能，但确实可以省去许多不需要人工判断的任务。

我们为 Offscreen Documents API 添加了两种新的原因类型。使用 LOCAL_STORAGE 访问 Web 平台的 localStorage API。创建网页工作器时使用 WORKER。

Chrome 应用商店开发者信息中心现在支持 Google Analytics 4 (GA4)。我们简化了 Google Analytics 的设置流程，并使群组发布商的访问权限管理更加简单明了。如果您之前使用 Google Universal Analytics 跟踪您的商店详情活动，则需要在 2023 年 7 月 1 日之前采取行动，以确保您能够继续接收有关商店详情的数据。如需了解详情，请参阅 Chrome 扩展程序邮寄名单中的帖子。

文件处理程序 API 可在 ChromeOS Canary 版中进行实验，适用于 112 和 113 版。它允许 ChromeOS 上的扩展程序打开具有指定 MIME 类型和文件扩展名的文件。如需实现文件处理，请向 manifest.json 添加一组规则。此功能的工作方式与渐进式 Web 应用相同。如需了解详情，请参阅本网站上的这篇文章。

我们希望在 6 月下旬推出 Chrome 115 时发布此功能。请关注此空间，了解最新动态。

我们为 chrome.scripting API 构建了一个新示例。它演示了动态声明（在运行时注册内容脚本）和程序化注入（在已打开的标签页中执行脚本）。

我们提供了三个新示例，用于演示声明式网络请求 API。每个示例都展示了单个用例的实现。第一个示例展示了如何屏蔽 Cookie。其余两个示例演示了如何屏蔽和重定向网址。

自 Chrome 112 起，storage.session 属性的配额已增加到大约 10 MB。Web Extensions Community Group 已就此达成一致：https://github.com/w3c/webextensions/issues/350

Manifest V3 扩展程序现在支持屏幕外文档。这些 API 可支持与 DOM 相关的功能，从而帮助您从后台网页过渡到扩展程序服务工作线程。如需了解详情，请阅读此博文。

chrome.action.isEnabled() 方法以编程方式检查是否已为特定标签页启用扩展程序。这样一来，您就无需维护标签页的启用状态。此新方法接受标签页 ID 和对回调的引用，并返回一个布尔值。但它有一个限制：使用 chrome.declarativeContent 创建的标签页始终返回 false。

（chrome.action 命名空间最近新增了一些用于控制扩展程序徽章外观的方法。如需了解详情，请参阅设置徽章颜色。）

以前，扩展程序服务工作线程通常会在 5 分钟时关闭。我们已更改此行为，使其更接近于 Web 上的 Service Worker 生命周期。扩展程序服务工作线程会在闲置 30 秒后关闭，或者在单个活动的处理时间超过 5 分钟时关闭。如需了解详情，请参阅延长扩展服务工作器的生命周期。

我们正在审核 Manifest V2 弃用时间表，并推迟原定于 2023 年初进行的实验。如需了解详情，请阅读 Chrome 扩展程序邮寄名单中的更新。

chrome.action 命名空间新增了两种方法，可让您更好地控制外观扩展程序徽章。setBadgeTextColor() 和 getBadgeTextColor() 方法允许扩展程序更改和查询其工具栏图标的徽章文本颜色。与 setBadgeBackgroundColor 和 getBadgeBackgroundColor 搭配使用时，这些新方法可让您强制保持设计和品牌的一致性。

我们明确了 Manifest V2 弃用时间表。Manifest V2 支持时间表也已更新，以反映此信息。

我们整理了一份目前正在开发中的主要功能和公开 bug 的列表。我们希望通过此页面帮助开发者更好地了解平台的当前状态，以及在为未来做准备时可以考虑哪些功能。

Chrome 应用商店已从开发者信息中心的商品详情标签页中移除了“大型宣传块”上传界面。由于这些图片未在消费者界面中使用，因此此次变更不会影响最终用户体验。如需了解详情，请参阅这篇 chromium-extensions 博文。

根据 crbug.com/1219825#c11，不透明源（例如沙盒 iframe 和动态导入）也应该能够访问可通过网络访问的资源。

之前，调用异步 API 的 Manifest V3 可以提供无效的最终实参，而 Chrome 不会出错。通过此修复，Chrome 现在可以正确报告错误，并指出没有匹配的签名。建议开发者在 Canary 上检查其扩展程序是否存在任何错误，以免因意外使用错误的签名进行 API 调用而导致此 bug 修复破坏扩展程序。

Chrome 应用商店为 Chrome 应用商店开发者信息中心推出了经过改进的商品分析体验。新信息中心可让您一目了然地了解情况，并提前整合最有用的信息。如需了解详情，请阅读这篇博文。

Identity API 上的函数现在支持基于 Promise 的调用。这会略微改变 identity.getAuthToken() 的界面，其中设置为基于 Promise 的调用的异步返回将具有“token”和“grantedScopes”作为单个对象上的参数（而不是回调版本将它们作为单独的实参接收到回调中）。

Manifest V3 扩展程序现在可以使用新的网址格式 chrome-extension://<id>/_favicon/ 访问收藏夹图标，其中 是扩展程序的 ID。这取代了 Manifest V2 平台的 chrome://favicons API。如需了解详情，请参阅 Favicon API 文档。

添加了交易者/非交易者开发者身份标识，可提醒开发者准确自行声明其交易者/非交易者身份。

Chrome 不再默认向扩展程序授予 script-src: wasm-unsafe-eval。使用 WebAssembly 的扩展程序现在必须在其 content_security_policy 声明中明确添加此指令和值到 extension_pages。

在 chrome://extensions/shortcuts 上更改 Manifest V3 扩展程序的键盘快捷键时，更新现在会立即应用。之前，必须重新加载扩展程序，更改才会生效。

动态注册的内容脚本现在可以指定要将资源注入到的 world。如需了解详情，请参阅 scripting.registerContentScripts()。

Manifest V3 扩展程序现在可以在 manifest.json 中指定 optional_host_permissions 键。这样一来，Manifest V3 扩展程序就可以像 Manifest V2 扩展程序那样，使用 optional_permissions 键来声明主机的可选匹配模式。

chrome.scripting.executeScript() 现在接受其 injection 实参中的可选 injectImmediately 属性。如果存在且设置为 true，脚本将尽快注入到目标中，而不是等待 document_idle。请注意，这并不能保证脚本会在网页加载之前注入，因为在进行 API 调用的同时，网页会继续加载。

现在，基于 Service Worker 的扩展程序可以使用 Omnibox API。之前，由于内部依赖于 DOM 功能，此 API 的某些方法会在调用时抛出异常。

Manifest V3 扩展程序现在可以在其 content_security_policy 声明中包含 wasm-unsafe-eval。此变更允许 Manifest V3 扩展程序使用 WebAssembly。

Manifest V3 扩展程序现在可以使用内存存储空间 storage.session。

在 Chrome 应用商店中发现内容一文概述了用户如何在 Chrome 应用商店中查找商品，以及我们的编辑如何选择要重点展示的商品。

declarativeNetRequest 规则条件已更新，以便扩展程序能够根据请求的“request”和“initiator”网域更好地定位请求。相关的条件属性为 initiatorDomains、excludedInitiatorDomains、requestDomains 和 excludedRequestDomains。另请参阅此 chromium-extensions 帖子。

修复了长期存在的问题：在新建的标签页或窗口上调用 scripting.executeScript() 可能会失败。

在扩展程序的服务工作线程中使用 chrome.runtime.connectNative() 连接到原生消息传递主机应使服务工作线程在端口打开期间保持活跃状态。

omnibox.setDefaultSuggestion() 方法现在会返回一个 promise 或接受一个回调，以允许开发者确定建议何时已正确设置。

扩展程序服务工作线程上下文现在支持 chrome.i18n.getMessage() API。

内容脚本现在可以指定 match_origin_as_fallback 键，以注入到与匹配框架相关的框架中，包括具有 about:、data:、blob: 和 filesystem: 网址的框架。如需了解详情，请参阅内容脚本文档。

发布时间：2021 年 12 月 30 日

基于 Service Worker 的 Manifest V2 和 Manifest V3 扩展程序现在可以使用 Fetch API 请求 file: 方案网址。访问 file: 方案网址仍需要用户在 chrome://extensions 页面中为扩展程序启用“允许访问文件网址”。

发布时间：2021 年 12 月 28 日

为基于 Manifest V3 构建的扩展程序向 tabs.sendMessage、runtime.sendMessage 和 runtime.sendNativeMessage 添加了 Promise 支持。

发布时间：2021 年 12 月 10 日

添加了新参考页面，其中概述了 Chrome 应用商店审核流程，并说明了如何处理开发者计划政策的违规行为。

脚本 API 的 executeScript() 和 insertCSS() 方法现在接受多个文件。以前，这些方法需要一个包含单个文件条目的数组。

发布日期：2021 年 10 月 27 日

我们更新了排查 Chrome 应用商店违规行为页面，为开发者提供了有关常见拒绝原因的更详细指南。

此版本包含的 promise 更新明显多于任何之前的版本。更新包括常规扩展程序 API 和 ChromeOS 专用扩展程序 API。展开即可下部分即可查看详细信息。

许多 API 现在在清单 V3 中支持 Promise。

此外，使用 ChromeSetting 原型的 API 现在也支持 promise。以下 API 会受到此项变更的影响。

chrome.scripting API 现在支持在运行时注册、更新、取消注册和获取列表内容脚本。以前，内容脚本只能在扩展程序的 manifest.json 中静态声明，或者在运行时通过 chrome.scripting.executeScript() 以编程方式注入。

这篇博文中公布了从 Manifest V2 到 V3 的过渡时间表，并发布了更详细的时间表页面。

借助新的 declarativeNetRequestWithHostAccess 权限，扩展程序可以在具有主机权限的网站上使用 chrome.declarativeNetRequest API。这还允许使用 webRequest、webRequestBlocking 和特定于网站的主机权限的现有 Manifest V2 扩展程序迁移到 chrome.declarativeNetRequest API，而无需用户批准新权限。

chrome.scripting API 的 executeScript() 方法现在可以直接将脚本注入到网页的主世界中。以前，扩展程序只能直接注入到扩展程序的隔离世界中。如需详细了解隔离的世界，请参阅有关内容脚本的文档。

Manifest V3 版 chrome.storage API 中的方法现在会返回 promise。

我们已更新 2021 年 6 月 29 日发布的政策更新博文，以更正两步验证部署时间表。

chrome.declarativeNetRequest 现在支持指定最多 50 个静态规则集 (MAX_NUMBER_OF_STATIC_RULESETS)，并同时启用最多 10 个规则集 (MAX_NUMBER_OF_ENABLED_STATIC_RULESETS)。

现在，Manifest V2 和 Manifest V3 扩展程序都可以选择启用跨源隔离。此功能可限制哪些跨源资源可以加载扩展程序的网页，并支持使用 SharedArrayBuffer 等低级 Web 平台功能。从 Chrome 95 版开始，必须选择启用。

我们更新了 Chrome 应用商店开发者计划政策，对欺骗性安装策略、垃圾内容和重复性内容政策进行了阐明。 此更新还新增了一项要求，即必须进行两步验证才能在 Chrome 应用商店中发布内容。如需了解详情，请阅读这篇博文。

Chrome 扩展程序多年来一直使用 chrome.browserAction 和 chrome.pageActions API，但 Manifest V3 将两者都替换为通用的 chrome.actions API。这篇博文探讨了这些 API 的历史记录以及 Manifest V3 中的变化。阅读帖子。

chrome.scripting API 是一项新的 Manifest V3 API，专注于脚本。在这篇博文中，我们将深入探讨此项变更的动机，并仔细了解其新功能。阅读帖子。

Chrome 现在支持在 Service Worker 中使用 JavaScript 模块。如需在清单中指定模块，请执行以下操作：

这会将 worker 脚本加载为 ES 模块，从而让您可以在 worker 的脚本中使用 import 关键字来导入其他模块。

新的 chrome.action.getUserSettings() 方法允许扩展程序确定用户是否已将扩展程序固定到主工具栏。

新的 chrome.scripting.removeCSS() 方法允许扩展程序移除之前通过 chrome.scripting.insertCSS() 插入的 CSS。它取代了 chrome.tabs.removeCSS()。

chrome.scripting.executeScript() 现在支持返回 promise。如果脚本执行的最终值是 Promise，Chrome 会等待 Promise 得到解决，并返回其最终值。

从 chrome.scripting.executeScript() 返回的结果现在包含 frameId。frameId 属性表示结果来自哪个框架，以便扩展程序在注入多个框架时轻松将结果与各个框架相关联。

新的 chrome.tabGroups API 和 chrome.tabs 中的新功能可让扩展程序读取和操纵标签页组。 需要使用 Manifest V3。

发布日期：2020 年 12 月 23 日

Manifest V3 中的可供 Web 访问的资源定义已发生变化，可让扩展程序根据请求者的来源或扩展程序 ID 限制资源访问权限。

Chrome 扩展程序团队已开源“扩展程序清单转换器”，这是一款 Python 工具，可自动执行将扩展程序转换为 Manifest V3 的部分机械性工作。请参阅公告博文，并从 GitHub 获取。

Manifest V3 是对扩展平台进行的一项重大更新；如需了解新功能和变更功能的摘要，请参阅 Manifest V3 概览。扩展程序目前可以继续使用 Manifest V2，但我们会在不久的将来逐步淘汰这一版本。我们强烈建议您为所有新扩展程序使用 Manifest V3，并尽快开始将现有扩展程序迁移到 Manifest V3。

**Examples:**

Example 1 (unknown):
```unknown
"background": {
  "service_worker": "script.js",
  "type": "module"
}
```

---

## chrome.extensionTypes 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/extensionTypes/?hl=zh-cn

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

## 

**URL:** https://developer.chrome.google.cn/docs/extensions/samples

**Contents:**
  - 示例

---

## 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/cross-origin-isolation

**Contents:**
- 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

跨源隔离使网页能够使用 SharedArrayBuffer 等强大功能。扩展程序可以通过为 cross_origin_embedder_policy 和 cross_origin_opener_policy 清单键指定适当的值来选择启用跨源隔离。例如，以下清单会将扩展程序的来源选择加入跨源隔离。

选择启用跨域隔离后，扩展程序便可在其跨域隔离的情境中使用 SharedArrayBuffers 等强大的 API。不过，它也会带来一些副作用。如需了解详情，请参阅使用 COOP 和 COEP 使您的网站“跨源隔离”。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "CrossOriginIsolation example",
  "manifest_version": 3,
  "version": "1.1",
  "cross_origin_embedder_policy": {
    "value": "require-corp"
  },
  "cross_origin_opener_policy": {
    "value": "same-origin"
  },
  ...
}
```

---

## 提交扩展程序错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/file-a-bug?hl=zh-cn

**Contents:**
- 提交扩展程序错误 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

在开发扩展程序时，您可能会发现某些行为与扩展程序的文档不符，或者出乎意料。这可能是 Chrome bug 导致的，也可能是我们应添加到文档中的内容。无论如何，请提交相应的问题报告来告知我们。请按照以下步骤操作，提供足够的信息来重现问题：

---

## 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/cross-origin-isolation?hl=zh-cn

**Contents:**
- 跨域隔离 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

跨源隔离可让网页使用 SharedArrayBuffer 等强大功能。扩展程序可以通过为 cross_origin_embedder_policy 和 cross_origin_opener_policy 清单键指定适当的值来选择启用跨域隔离。例如，以下清单会选择将扩展程序的来源纳入跨源隔离范围。

选择启用跨源隔离后，扩展程序便可以在其跨源隔离情境中使用 SharedArrayBuffer 等强大的 API。不过，它也有一些副作用。如需详细了解，请参阅使用 COOP 和 COEP 使您的网站实现“跨源隔离”。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "CrossOriginIsolation example",
  "manifest_version": 2,
  "version": "1.1",
  "cross_origin_embedder_policy": {
    "value": "require-corp"
  },
  "cross_origin_opener_policy": {
    "value": "same-origin"
  },
  ...
}
```

---

## 权限警告准则 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/permission-warnings

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

## chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/cookies

**Contents:**
- chrome.cookies 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 清单
- 分区
- 示例
- 类型
  - Cookie
    - 属性
  - CookieDetails

使用 chrome.cookies API 可查询和修改 Cookie，并在 Cookie 发生更改时收到通知。

如需使用 Cookie API，您必须在清单中声明“cookies”权限，同时声明您要访问其 Cookie 的任何主机的主机权限。例如：

借助分区 Cookie，网站可以标记某些 Cookie 应以顶级框架的来源为键。这意味着，如果网站 A 使用 iframe 嵌入到网站 B 和网站 C 中，则分区 Cookie 在每个网站中的值可能不同。

chrome.cookies 不支持分区，这意味着所有方法都会从所有分区读取和写入 Cookie。cookies.set() 方法将 Cookie 存储在默认分区中。

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

包含有关 Cookie 的详细信息。如果未找到此类 Cookie，则此参数为 null。

Promise<Cookie | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

从单个 Cookie 存储区检索与给定信息匹配的所有 Cookie。返回的 Cookie 将按路径长度进行排序，路径最长的 Cookie 排在最前面。如果多个 Cookie 的路径长度相同，则创建时间最早的 Cookie 会排在前面。此方法仅检索扩展程序具有主机权限的网域的 Cookie。

将检索到的 Cookie 限制为网域与此网域匹配或为此网域的子网域的 Cookie。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

将检索到的 Cookie 限制为路径与此字符串完全匹配的 Cookie。

按 Secure 属性过滤 Cookie。

过滤掉会话 Cookie 与永久性 Cookie。

要从中检索 Cookie 的 Cookie 存储区。如果省略，则使用当前执行上下文的 Cookie 存储区。

将检索到的 Cookie 限制为与指定网址匹配的 Cookie。

与给定 Cookie 信息匹配的所有现有未过期 Cookie。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

Promise<CookieStore[]>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

包含有关已移除的 Cookie 的详细信息。如果因任何原因而移除失败，此属性将为“null”，并且会设置 runtime.lastError。

CookiePartitionKey 可选

用于读取或修改具有 Partitioned 属性的 Cookie 的分区键。

从中移除了 Cookie 的 Cookie 存储区的 ID。

Promise<object | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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

包含有关已设置 Cookie 的详细信息。如果因任何原因而设置失败，此值将为“null”，并且会设置 runtime.lastError。

Promise<Cookie | undefined>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

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
chrome.cookies.get(  details: CookieDetails,  callback?: function,): Promise<Cookie | undefined>
```

Example 3 (javascript):
```javascript
(cookie?: Cookie) => void
```

Example 4 (unknown):
```unknown
chrome.cookies.getAll(  details: object,  callback?: function,): Promise<Cookie[]>
```

---

## chrome.desktopCapture 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/desktopCapture

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
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 2 (javascript):
```javascript
function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');

  const rawData = atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}
```

Example 3 (javascript):
```javascript
const SERVER_PUBLIC_KEY = '_INSERT_VALUE_HERE_';
const applicationServerKey = urlB64ToUint8Array(SERVER_PUBLIC_KEY);

async function subscribe() {
  try {
    let subscription = await self.registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey
    });

    console.log(`Subscribed: ${JSON.stringify(subscription,0,2)}`);

    return subscription
  } catch (error) {
    console.error('Subscribe error: ', error);
  }
}

const subscription = await subscribe();
```

Example 4 (unknown):
```unknown
self.addEventListener('push', function (event) {
  console.log(`Push had this data/text: "${event.data.text()}"`);
});
```

---

## 支持与反馈 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support

**Contents:**
- 支持与反馈 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

沟通有助于您和我们打造更好的产品。Chrome 扩展程序团队致力于帮助您高效工作。您的反馈有助于我们不断改进。

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
{
    "manifest_version": 3,
    ...
    "permissions": ["notifications"]
```

Example 2 (javascript):
```javascript
function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');

  const rawData = atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}
```

Example 3 (javascript):
```javascript
const SERVER_PUBLIC_KEY = '_INSERT_VALUE_HERE_';
const applicationServerKey = urlB64ToUint8Array(SERVER_PUBLIC_KEY);

async function subscribe() {
  try {
    let subscription = await self.registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey
    });

    console.log(`Subscribed: ${JSON.stringify(subscription,0,2)}`);

    return subscription
  } catch (error) {
    console.error('Subscribe error: ', error);
  }
}

const subscription = await subscribe();
```

Example 4 (unknown):
```unknown
self.addEventListener('push', function (event) {
  console.log(`Push had this data/text: "${event.data.text()}"`);
});
```

---

## chrome.devtools.network 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/devtools_network?hl=zh-cn

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

## 获取 Chrome 扩展程序方面的帮助 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/support/get-help?hl=zh-cn

**Contents:**
- 获取 Chrome 扩展程序方面的帮助 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 用于扩展程序开发
- 对于 Chrome 应用商店

我们会尽力改进本网站和 Chrome 应用商店帮助的内容。部分用户可能会遇到我们未涵盖的问题。幸运的是，您还可以通过其他方式获得帮助。

如果您在 Chrome 应用商店账号或商品方面遇到问题，请访问我们的一站式支持页面寻求帮助。

---

## 扩展 Service Worker 生命周期 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/service-workers/lifecycle

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
