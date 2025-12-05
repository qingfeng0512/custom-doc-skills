# Chrome-Plugin-Dev - Content Scripts

**Pages:** 3

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

Example 1 (unknown):
```unknown
runtime.connect()
```

Example 2 (unknown):
```unknown
runtime.getManifest()
```

Example 3 (unknown):
```unknown
runtime.getURL()
```

Example 4 (unknown):
```unknown
runtime.onConnect
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

Example 1 (unknown):
```unknown
runtime.connect()
```

Example 2 (unknown):
```unknown
runtime.getManifest()
```

Example 3 (unknown):
```unknown
runtime.getURL()
```

Example 4 (unknown):
```unknown
runtime.onConnect
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

Example 1 (unknown):
```unknown
runtime.connect()
```

Example 2 (unknown):
```unknown
runtime.getManifest()
```

Example 3 (unknown):
```unknown
runtime.getURL()
```

Example 4 (unknown):
```unknown
runtime.onConnect
```

---
