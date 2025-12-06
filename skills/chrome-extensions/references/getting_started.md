# Chrome-Extensions - Getting Started

**Pages:** 13

---

## 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/debug?hl=zh-cn

**Contents:**
- 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 准备工作
- 中断扩展程序
  - 调试清单
  - 调试服务工件
    - 查找日志
    - 定位错误
    - 检查 Service Worker 状态
  - 调试弹出式窗口
  - 调试内容脚本

扩展程序可以访问与网页相同的 Chrome 开发者工具。如需成为调试扩展程序的专家，您需要了解如何查找不同扩展程序组件的日志和错误。本教程介绍了调试扩展程序的基本方法。

本指南假定您具备基本的 Web 开发经验。建议您阅读开发基础知识，了解扩展程序开发工作流程。设计界面介绍了扩展程序中提供的界面元素。

本教程将一次破坏一个扩展程序组件，然后演示如何修复它。请务必先撤消某个部分引入的 bug，然后再继续下一部分。首先，在 GitHub 上下载“Broken Color”示例。

首先，我们将 "version" 键更改为 "versions"，以破坏清单文件：

现在，我们尝试在本地加载扩展程序。您会看到一个指明问题的错误对话框：

当清单键无效时，扩展程序会加载失败，但 Chrome 会提示您如何解决此问题。

撤消该更改，然后输入无效权限，看看会发生什么。 将 "activeTab" 权限更改为小写的 "activetab"：

保存扩展程序，然后尝试重新加载。这次应该能成功加载。在扩展程序管理页面中，您会看到三个按钮：详情、移除和错误。出现错误时，错误按钮标签会变为红色。点击错误按钮，您会看到以下错误：

在继续之前，请恢复权限，点击右上角的清除全部以清除日志，然后重新加载扩展程序。

服务工件会将默认颜色设置为存储，并将其记录到控制台。如需查看此日志，请选择检查视图旁边的蓝色链接，打开 Chrome 开发者工具面板。

我们将 onInstalled 更改为小写的 oninstalled，以破坏该服务工件：

刷新页面，然后点击错误以查看错误日志。第一个错误会告知您服务工件未能注册。这意味着启动过程中出了点问题：

还原我们引入的 bug，点击右上角的全部清除，然后重新加载扩展程序。

您可以按照以下步骤确定服务工件何时唤醒以执行任务：

前往 Service Workers 窗格。

如需测试代码，请使用状态旁边的链接启动或停止服务工件。

现在，扩展程序已正确初始化，接下来我们将注释掉下面突出显示的行，以中断弹出式窗口：

返回“扩展程序管理”页面。错误按钮会再次显示。点击该日志即可查看新日志。系统会显示以下错误消息：

您可以通过检查弹出式窗口来打开其 DevTools。

错误 tabs is undefined 表示扩展程序不知道在哪里注入内容脚本。如需更正此问题，请调用 tabs.query()，然后选择处于活动状态的标签页。

如需更新代码，请点击右上角的清除全部按钮，然后重新加载扩展程序。

现在，我们将变量“color”更改为“colors”，以破坏内容脚本：

刷新页面，打开弹出式窗口，然后点击绿色框。不会有任何反应。

如果您前往“扩展程序管理”页面，则不会看到错误按钮。这是因为“扩展程序管理”页面上只会记录运行时错误 console.warning 和 console.error。

内容脚本在网站内运行。因此，若要查找这些错误，我们必须检查扩展程序尝试更改的网页：

如需在内容脚本中使用开发者工具，请点击 top 旁边的下拉箭头，然后选择相应扩展程序。

错误消息指出 colors 未定义。扩展程序未正确传递变量。更正注入的脚本，以将颜色变量传递到代码中。

在最快的开发者能够打开 DevTools 之前，弹出式窗口通常会发出所有必要的网络请求。如需查看这些请求，请在“网络”面板中刷新。它会重新加载弹出式窗口，而不会关闭 DevTools 面板。

某些扩展程序 API 需要权限。请参阅权限一文和 Chrome API，确保扩展程序在manifest中请求的权限正确无误。

如需详细了解 Chrome 开发者工具，请参阅文档。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 2 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

Example 3 (unknown):
```unknown
{
  ...
  "permissions": ["activeTab", "scripting", "storage"],
  "permissions": ["activetab", "scripting", "storage"],
  ...
}
```

Example 4 (unknown):
```unknown
Permission 'activetab' is unknown or URL pattern is malformed.
```

---

## 使用 Service Worker 处理事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/service-worker-events?hl=zh-cn

**Contents:**
- 使用 Service Worker 处理事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：注册 service worker
  - 第 2 步：导入多个服务工作线程模块
  - 可选：调试 Service Worker
  - 第 4 步：初始化状态
  - 第 5 步：注册活动
  - 第 6 步：设置周期性活动

本教程简要介绍了 Chrome 扩展程序服务工作线程。在本教程中，您将构建一个扩展程序，让用户能够使用多功能框快速前往 Chrome API 参考页面。您将学习如何：

本指南假定您具备基本的 Web 开发经验。建议您查看扩展程序 101 和 Hello World，了解扩展程序开发入门知识。

首先，创建一个名为 quick-api-reference 的新目录来存放扩展程序文件，或者从我们的 GitHub 示例代码库下载源代码。

在项目根目录中创建 清单文件，并添加以下代码：

扩展程序会在清单中注册其服务工作线程，而清单仅采用单个 JavaScript 文件。无需像在网页中那样调用 navigator.serviceWorker.register()。

创建一个 images 文件夹，然后将图标下载到该文件夹中。

请查看“阅读时间”教程的第一步，详细了解清单中的扩展程序元数据和图标。

我们的 service worker 实现了两项功能。为了提高可维护性，我们将每个功能都实现为一个单独的模块。首先，我们需要在清单中将 Service Worker 声明为 ES 模块，这样我们就可以在 Service Worker 中导入模块：

创建 service-worker.js 文件并导入两个模块：

创建这些文件，并向每个文件添加控制台日志。

如需了解在 Service Worker 中导入多个文件的其他方法，请参阅导入脚本。

我将说明如何查找服务工作线程日志，以及如何知道服务工作线程何时终止。首先，按照说明加载未打包的扩展程序。

30 秒后，您会看到“service worker (inactive)”，这意味着 service worker 已终止。点击“服务工作线程（不活跃）”链接以检查该服务工作线程。以下动画展示了这一点。

您是否注意到，检查服务工作线程会将其唤醒？在开发者工具中打开 service worker 会使其保持活跃状态。为确保扩展程序在 Service Worker 终止时正常运行，请务必关闭开发者工具。

现在，我们来破坏扩展程序，了解在哪里查找错误。一种方法是从 service-worker.js 文件中的 './sw-omnibox.js' 导入中删除“.js”。Chrome 将无法注册 Service Worker。

返回到 chrome://extensions 并刷新扩展程序。您会看到两个错误：

如需了解调试扩展程序服务工作线程的更多方法，请参阅调试扩展程序。

如果不需要，Chrome 会关闭服务工作线程。我们使用 chrome.storage API 来跨 Service Worker 会话保留状态。对于存储空间访问权限，我们需要在清单中请求权限：

首先，将默认建议保存到存储空间。我们可以在首次安装扩展程序时通过监听 runtime.onInstalled() 事件来初始化状态：

服务工作线程无法直接访问 window 对象，因此无法使用 window.localStorage 存储值。此外，Service Worker 是短暂的执行环境；它们会在用户浏览器会话期间反复终止，因此与全局变量不兼容。请改用 chrome.storage.local，它会将数据存储在本地机器上。

如需了解扩展程序服务工作线程的其他存储选项，请参阅持久保留数据，而不是使用全局变量。

所有事件监听器都需要在服务工作线程的全局范围内静态注册。换句话说，事件监听器不应嵌套在异步函数中。这样，Chrome 就可以确保在 Service Worker 重启时恢复所有事件处理程序。

在此示例中，我们将使用 chrome.omnibox API，但首先必须在清单中声明多功能框关键字触发器：

现在，在脚本的顶层注册信息框事件监听器。当用户在地址栏中输入多功能框关键字 (api) 后按 Tab 键或空格键时，Chrome 会根据存储中的关键字显示建议列表。onInputChanged() 事件（采用当前用户输入和 suggestResult 对象）负责填充这些建议。

用户选择建议后，onInputEntered() 将打开相应的 Chrome API 参考页面。

updateHistory() 函数会获取多功能框输入内容并将其保存到 storage.local。这样，最近的搜索字词便可稍后用作多功能框建议。

setTimeout() 或 setInterval() 方法通常用于执行延迟或周期性任务。不过，这些 API 可能会失败，因为当服务工作线程终止时，调度程序会取消计时器。扩展程序可以改用 chrome.alarms API。

首先，在清单中请求 "alarms" 权限：

扩展程序会提取所有提示，随机选择一个并将其保存到存储空间。我们将创建一个每天触发一次的闹钟，用于更新提示。关闭 Chrome 时，系统不会保存闹钟。因此，我们需要检查闹钟是否存在，如果不存在，则创建闹钟。

扩展程序使用内容脚本来读取和修改网页的内容。当用户访问 Chrome API 参考页面时，扩展程序的内容脚本会使用每日提示更新该页面。它发送消息，以从服务工作线程请求每日提示。

首先，在清单中声明内容脚本，并添加与 Chrome API 参考文档对应的匹配模式。

创建新的内容文件。以下代码会向服务工作线程发送消息，请求提示。然后，添加一个按钮，用于打开包含扩展程序提示的弹出式信息框。此代码使用新的 Web 平台 Popover API。

最后一步是将消息处理程序添加到我们的服务工作线程，该处理程序会向内容脚本发送包含每日提示的回复。

如需在开发者模式下加载未封装的扩展程序，请按照你好，世界中的步骤操作。

点击导航栏上的“提示”按钮，打开扩展程序提示。

根据您今天所学的内容，尝试完成以下任一任务：

恭喜您完成本教程 🎉。如需继续提升技能，请完成其他初级教程：

如需继续学习扩展程序的服务工作线程，建议您浏览以下文章：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Open extension API reference",
  "version": "1.0.0",
  "icons": {
    "16": "images/icon-16.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

Example 2 (unknown):
```unknown
{
 "background": {
    "service_worker": "service-worker.js",
    "type": "module"
  },
}
```

Example 3 (unknown):
```unknown
import './sw-omnibox.js';
import './sw-tips.js';
```

Example 4 (unknown):
```unknown
console.log("sw-omnibox.js");
```

---

## 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/debug

**Contents:**
- 调试扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 准备工作
- 中断扩展程序
  - 调试清单
  - 调试服务工件
    - 查找日志
    - 定位错误
    - 检查 Service Worker 状态
  - 调试弹出式窗口
  - 调试内容脚本

扩展程序可以访问与网页相同的 Chrome 开发者工具。如需成为调试扩展程序的专家，您需要了解如何查找不同扩展程序组件的日志和错误。本教程介绍了调试扩展程序的基本方法。

本指南假定您具备基本的 Web 开发经验。建议您阅读开发基础知识，了解扩展程序开发工作流程。设计界面介绍了扩展程序中提供的界面元素。

本教程将一次破坏一个扩展程序组件，然后演示如何修复它。请务必先撤消某个部分引入的 bug，然后再继续下一部分。首先，在 GitHub 上下载“Broken Color”示例。

首先，我们将 "version" 键更改为 "versions"，以破坏清单文件：

现在，我们尝试在本地加载扩展程序。您会看到一个指明问题的错误对话框：

当清单键无效时，扩展程序会加载失败，但 Chrome 会提示您如何解决此问题。

撤消该更改，然后输入无效权限，看看会发生什么。 将 "activeTab" 权限更改为小写的 "activetab"：

保存扩展程序，然后尝试重新加载。这次应该能成功加载。在扩展程序管理页面中，您会看到三个按钮：详情、移除和错误。出现错误时，错误按钮标签会变为红色。点击错误按钮，您会看到以下错误：

在继续之前，请恢复权限，点击右上角的清除全部以清除日志，然后重新加载扩展程序。

服务工件会将默认颜色设置为存储，并将其记录到控制台。如需查看此日志，请选择检查视图旁边的蓝色链接，打开 Chrome 开发者工具面板。

我们将 onInstalled 更改为小写的 oninstalled，以破坏该服务工件：

刷新页面，然后点击错误以查看错误日志。第一个错误会告知您服务工件未能注册。这意味着启动过程中出了点问题：

还原我们引入的 bug，点击右上角的全部清除，然后重新加载扩展程序。

您可以按照以下步骤确定服务工件何时唤醒以执行任务：

前往 Service Workers 窗格。

如需测试代码，请使用状态旁边的链接启动或停止服务工件。

现在，扩展程序已正确初始化，接下来我们将注释掉下面突出显示的行，以中断弹出式窗口：

返回“扩展程序管理”页面。错误按钮会再次显示。点击该日志即可查看新日志。系统会显示以下错误消息：

您可以通过检查弹出式窗口来打开其 DevTools。

错误 tabs is undefined 表示扩展程序不知道在哪里注入内容脚本。如需更正此问题，请调用 tabs.query()，然后选择处于活动状态的标签页。

如需更新代码，请点击右上角的清除全部按钮，然后重新加载扩展程序。

现在，我们将变量“color”更改为“colors”，以破坏内容脚本：

刷新页面，打开弹出式窗口，然后点击绿色框。不会有任何反应。

如果您前往“扩展程序管理”页面，则不会看到错误按钮。这是因为“扩展程序管理”页面上只会记录运行时错误 console.warning 和 console.error。

内容脚本在网站内运行。因此，若要查找这些错误，我们必须检查扩展程序尝试更改的网页：

如需在内容脚本中使用开发者工具，请点击 top 旁边的下拉箭头，然后选择相应扩展程序。

错误消息指出 colors 未定义。扩展程序未正确传递变量。更正注入的脚本，以将颜色变量传递到代码中。

在最快的开发者能够打开 DevTools 之前，弹出式窗口通常会发出所有必要的网络请求。如需查看这些请求，请在“网络”面板中刷新。它会重新加载弹出式窗口，而不会关闭 DevTools 面板。

某些扩展程序 API 需要权限。请参阅权限一文和 Chrome API，确保扩展程序在manifest中请求的权限正确无误。

如需详细了解 Chrome 开发者工具，请参阅文档。

**Examples:**

Example 1 (unknown):
```unknown
{
  "name": "Broken Background Color",
  "version": "1.0",
  "versions": "1.0",
  "description": "Fix an Extension!",
  ...
}
```

Example 2 (unknown):
```unknown
Failed to load extension
Required value version is missing or invalid. It must be between 1-4 dot-separated integers each between 0 and 65536.
Could not load manifest.
```

Example 3 (unknown):
```unknown
{
  ...
  "permissions": ["activeTab", "scripting", "storage"],
  "permissions": ["activetab", "scripting", "storage"],
  ...
}
```

Example 4 (unknown):
```unknown
Permission 'activetab' is unknown or URL pattern is malformed.
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

## 使用 Service Worker 处理事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/service-worker-events

**Contents:**
- 使用 Service Worker 处理事件 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：注册 service worker
  - 第 2 步：导入多个服务工作线程模块
  - 可选：调试 Service Worker
  - 第 4 步：初始化状态
  - 第 5 步：注册活动
  - 第 6 步：设置周期性活动

本教程简要介绍了 Chrome 扩展程序服务工作线程。在本教程中，您将构建一个扩展程序，让用户能够使用多功能框快速前往 Chrome API 参考页面。您将学习如何：

本指南假定您具备基本的 Web 开发经验。建议您查看扩展程序 101 和 Hello World，了解扩展程序开发入门知识。

首先，创建一个名为 quick-api-reference 的新目录来存放扩展程序文件，或者从我们的 GitHub 示例代码库下载源代码。

在项目根目录中创建 清单文件，并添加以下代码：

扩展程序会在清单中注册其服务工作线程，而清单仅采用单个 JavaScript 文件。无需像在网页中那样调用 navigator.serviceWorker.register()。

创建一个 images 文件夹，然后将图标下载到该文件夹中。

请查看“阅读时间”教程的第一步，详细了解清单中的扩展程序元数据和图标。

我们的 service worker 实现了两项功能。为了提高可维护性，我们将每个功能都实现为一个单独的模块。首先，我们需要在清单中将 Service Worker 声明为 ES 模块，这样我们就可以在 Service Worker 中导入模块：

创建 service-worker.js 文件并导入两个模块：

创建这些文件，并向每个文件添加控制台日志。

如需了解在 Service Worker 中导入多个文件的其他方法，请参阅导入脚本。

我将说明如何查找服务工作线程日志，以及如何知道服务工作线程何时终止。首先，按照说明加载未打包的扩展程序。

30 秒后，您会看到“service worker (inactive)”，这意味着 service worker 已终止。点击“服务工作线程（不活跃）”链接以检查该服务工作线程。以下动画展示了这一点。

您是否注意到，检查服务工作线程会将其唤醒？在开发者工具中打开 service worker 会使其保持活跃状态。为确保扩展程序在 Service Worker 终止时正常运行，请务必关闭开发者工具。

现在，我们来破坏扩展程序，了解在哪里查找错误。一种方法是从 service-worker.js 文件中的 './sw-omnibox.js' 导入中删除“.js”。Chrome 将无法注册 Service Worker。

返回到 chrome://extensions 并刷新扩展程序。您会看到两个错误：

如需了解调试扩展程序服务工作线程的更多方法，请参阅调试扩展程序。

如果不需要，Chrome 会关闭服务工作线程。我们使用 chrome.storage API 来跨 Service Worker 会话保留状态。对于存储空间访问权限，我们需要在清单中请求权限：

首先，将默认建议保存到存储空间。我们可以在首次安装扩展程序时通过监听 runtime.onInstalled() 事件来初始化状态：

服务工作线程无法直接访问 window 对象，因此无法使用 window.localStorage 存储值。此外，Service Worker 是短暂的执行环境；它们会在用户浏览器会话期间反复终止，因此与全局变量不兼容。请改用 chrome.storage.local，它会将数据存储在本地机器上。

如需了解扩展程序服务工作线程的其他存储选项，请参阅持久保留数据，而不是使用全局变量。

所有事件监听器都需要在服务工作线程的全局范围内静态注册。换句话说，事件监听器不应嵌套在异步函数中。这样，Chrome 就可以确保在 Service Worker 重启时恢复所有事件处理程序。

在此示例中，我们将使用 chrome.omnibox API，但首先必须在清单中声明多功能框关键字触发器：

现在，在脚本的顶层注册信息框事件监听器。当用户在地址栏中输入多功能框关键字 (api) 后按 Tab 键或空格键时，Chrome 会根据存储中的关键字显示建议列表。onInputChanged() 事件（采用当前用户输入和 suggestResult 对象）负责填充这些建议。

用户选择建议后，onInputEntered() 将打开相应的 Chrome API 参考页面。

updateHistory() 函数会获取多功能框输入内容并将其保存到 storage.local。这样，最近的搜索字词便可稍后用作多功能框建议。

setTimeout() 或 setInterval() 方法通常用于执行延迟或周期性任务。不过，这些 API 可能会失败，因为当服务工作线程终止时，调度程序会取消计时器。扩展程序可以改用 chrome.alarms API。

首先，在清单中请求 "alarms" 权限：

扩展程序会提取所有提示，随机选择一个并将其保存到存储空间。我们将创建一个每天触发一次的闹钟，用于更新提示。关闭 Chrome 时，系统不会保存闹钟。因此，我们需要检查闹钟是否存在，如果不存在，则创建闹钟。

扩展程序使用内容脚本来读取和修改网页的内容。当用户访问 Chrome API 参考页面时，扩展程序的内容脚本会使用每日提示更新该页面。它发送消息，以从服务工作线程请求每日提示。

首先，在清单中声明内容脚本，并添加与 Chrome API 参考文档对应的匹配模式。

创建新的内容文件。以下代码会向服务工作线程发送消息，请求提示。然后，添加一个按钮，用于打开包含扩展程序提示的弹出式信息框。此代码使用新的 Web 平台 Popover API。

最后一步是将消息处理程序添加到我们的服务工作线程，该处理程序会向内容脚本发送包含每日提示的回复。

如需在开发者模式下加载未封装的扩展程序，请按照你好，世界中的步骤操作。

点击导航栏上的“提示”按钮，打开扩展程序提示。

根据您今天所学的内容，尝试完成以下任一任务：

恭喜您完成本教程 🎉。如需继续提升技能，请完成其他初级教程：

如需继续学习扩展程序的服务工作线程，建议您浏览以下文章：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Open extension API reference",
  "version": "1.0.0",
  "icons": {
    "16": "images/icon-16.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

Example 2 (unknown):
```unknown
{
 "background": {
    "service_worker": "service-worker.js",
    "type": "module"
  },
}
```

Example 3 (unknown):
```unknown
import './sw-omnibox.js';
import './sw-tips.js';
```

Example 4 (unknown):
```unknown
console.log("sw-omnibox.js");
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

## 管理标签页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/popup-tabs-manager

**Contents:**
- 管理标签页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展程序数据和图标
  - 第 2 步：创建并设置弹出式窗口的样式
  - 第 3 步：管理标签页
    - 请求权限
    - 查询标签页
    - 将焦点置于标签页

本教程将构建一个标签页管理器，用于整理 Chrome 扩展程序和 Chrome 应用商店文档标签页。

本指南假定您具备基本的 Web 开发经验。我们建议您查看 Hello World，了解扩展程序开发工作流程。

首先，创建一个名为 tabs-manager 的新目录来存放扩展程序的文件。如果您愿意，可以前往 GitHub 下载完整的源代码。

创建一个名为 manifest.json 的文件，并添加以下代码：

如需详细了解这些清单键，请参阅“阅读时间”教程，其中详细介绍了扩展程序的metadata和图标。

创建一个 images 文件夹，然后将下载的图标下载到该文件夹中。

Action API 用于控制扩展程序操作（工具栏图标）。当用户点击扩展程序操作时，扩展程序会运行一些代码或打开一个弹出式窗口（如本例所示）。首先，在 manifest.json 中声明弹出式窗口：

弹出式窗口与网页类似，但有一个例外情况：它无法运行内嵌 JavaScript。创建一个 popup.html 文件，并添加以下代码。

接下来，您将为弹出式窗口设置样式。创建一个 popup.css 文件，并添加以下代码。

借助 Tabs API，扩展程序可以在浏览器中创建、查询、修改和重新排列标签页。

无需请求任何权限，即可使用 Tabs API 中的许多方法。不过，我们需要访问标签页的 title 和 URL；这些敏感属性需要权限。我们可以请求 "tabs" 权限，但这会授予对所有标签页的敏感属性的访问权限。由于我们只管理特定网站的标签页，因此我们将请求获得有限的主机权限。

通过限制主机权限，我们可以向特定网站授予提升后的权限，从而保护用户隐私。这将授予对 title 和 URL 属性以及其他功能的访问权限。将突出显示的代码添加到 manifest.json 文件中：

💡? 标签页权限和主机权限之间的主要区别是什么？

"tabs" 权限可让扩展程序读取所有标签页中的敏感数据。随着时间的推移，这些信息可能会被用于收集用户的浏览记录。因此，如果您请求此权限，Chrome 会在安装时显示以下警告消息：

借助主机权限，扩展程序可以读取和查询匹配标签页的敏感属性，还可以在这些标签页中注入脚本。用户在安装时会看到以下警告消息：

这些警告可能会让用户感到担忧。为了提供更好的新手入门体验，我们建议您实现可选权限。

您可以使用 tabs.query() 方法从特定网址检索标签页。创建一个 popup.js 文件，并添加以下代码：

💡? 我可以在弹出式窗口中直接使用 Chrome API 吗？

弹出式窗口和其他扩展程序页面可以调用任何 Chrome API，因为它们是从 Chrome 架构中提供的。例如 chrome-extension://EXTENSION_ID/popup.html。

首先，该扩展程序会按字母顺序对标签页名称（包含的 HTML 网页的标题）进行排序。然后，当点击某个列表项时，它会使用 tabs.update() 将焦点移至该标签页，并使用 windows.update() 将窗口置于前台。将以下代码添加到 popup.js 文件中：

💡? 此代码中使用的有趣 JavaScript

借助 TabGroups API，扩展程序可以为分组命名并选择背景颜色。添加突出显示的代码，将 "tabGroups" 权限添加到清单中：

在 popup.js 中，添加以下代码以创建一个按钮，该按钮将使用 tabs.group() 对所有标签页进行分组，并将其移至当前窗口。

如需在开发者模式下加载未封装的扩展程序，请按照 Hello World 中的步骤操作。

根据您今天学到的内容，尝试实现以下任一操作：

恭喜您完成本教程 🎉?。请继续学习本系列的其他教程，不断提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待您继续学习 Chrome 开发。我们建议您采用以下学习路径：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Tab Manager for Chrome Dev Docs",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 2 (unknown):
```unknown
{
  "action": {
    "default_popup": "popup.html"
  }
}
```

Example 3 (unknown):
```unknown
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./popup.css" />
  </head>
  <body>
    <template id="li_template">
      <li>
        <a>
          <h3 class="title">Tab Title</h3>
          <p class="pathname">Tab Pathname</p>
        </a>
      </li>
    </template>

    <h1>Google Dev Docs</h1>
    <button>Group Tabs</button>
    <ul></ul>

    <script src="./popup.js" type="module"></script>
  </body>
</html>
```

Example 4 (unknown):
```unknown
body {
  width: 20rem;
}

ul {
  list-style-type: none;
  padding-inline-start: 0;
  margin: 1rem 0;
}

li {
  padding: 0.25rem;
}
li:nth-child(odd) {
  background: #80808030;
}
li:nth-child(even) {
  background: #ffffff;
}

h3,
p {
  margin: 0;
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

---

## 在每个网页上运行脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/scripts-on-every-tab?hl=zh-cn

**Contents:**
- 在每个网页上运行脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展程序的相关信息
  - 第 2 步：提供图标
  - 第 3 步：声明内容脚本
  - 第 4 步：计算并插入阅读时间
  - 第 5 步：监听更改
- 测试是否生效

本教程将构建一个扩展程序，用于向任何 Chrome 扩展程序和 Chrome 应用商店文档页面添加预计阅读时间。

本指南假定您具备基本的 Web 开发经验。我们建议您查看 Hello World 教程，了解扩展程序开发工作流程。

首先，创建一个名为 reading-time 的新目录来存放扩展程序的文件。如果您愿意，可以从 GitHub 下载完整源代码。

清单 JSON 文件是唯一的必需文件。其中包含有关扩展程序的重要信息。在项目的根目录中创建一个 manifest.json 文件，并添加以下代码：

这些键包含扩展程序的基本元数据。这些信息用于控制扩展程序在“扩展程序”页面上以及在发布后在 Chrome 应用商店中的显示方式。如需深入了解，请参阅清单概览页面上的 "name"、"version" 和 "description" 键。

那么，为什么需要图标？虽然在开发过程中图标是可选的，但如果您打算在 Chrome 应用商店中分发扩展程序，则必须提供图标。它们还会显示在扩展程序管理页面等其他位置。

创建一个 images 文件夹，并将图标放入其中。您可以在 GitHub 上下载图标。接下来，将突出显示的代码添加到清单中以声明图标：

我们建议使用 PNG 文件，但也允许使用其他文件格式（SVG 文件除外）。

扩展程序可以运行脚本，以读取和修改网页内容。这些脚本称为内容脚本。它们位于隔离的世界中，这意味着它们可以更改自己的 JavaScript 环境，而不会与其托管页面或其他扩展程序的内容脚本发生冲突。

将以下代码添加到 manifest.json 以注册名为 content.js 的内容脚本。

"matches" 字段可以有一个或多个匹配模式。这些标记可让浏览器确定要将内容脚本注入哪些网站。匹配模式由以下三个部分组成：<scheme>://<host><path>。可以包含“*”字符。

当用户安装扩展程序时，浏览器会告知用户该扩展程序的功能。内容脚本会请求在符合匹配模式条件的网站上运行的权限。

如需详细了解扩展程序权限，请参阅声明权限并向用户发出警告。

内容脚本可以使用标准文档对象模型 (DOM) 读取和更改网页内容。该扩展程序首先会检查网页是否包含 <article> 元素。然后，它会统计此元素中的所有字词，并创建一个段落来显示总阅读时间。

在名为 scripts 的文件夹中创建一个名为 content.js 的文件，然后添加以下代码：

💡 此代码中使用的有趣 JavaScript

使用当前代码时，如果您使用左侧导航栏切换文章，阅读时间不会添加到新文章中。这是因为我们的网站是作为单页应用 (SPA) 实现的，该应用使用 History API 执行软导航。

为解决此问题，我们可以使用 MutationObserver 监听更改，并将阅读时间添加到新文章。

为此，请将以下代码添加到 content.js 底部：

如需在开发者模式下加载未封装的扩展程序，请按照开发基础知识中的步骤操作。

下面列出了几个网页，您可以打开这些网页，看看每篇文章需要多长时间才能读完。

根据您今天学到的内容，尝试实现以下任一操作：

恭喜您完成本教程 🎉。请继续学习本系列的其他教程，不断提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待您继续学习 Chrome 开发。我们建议您采用以下学习路径：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Reading time",
  "version": "1.0",
  "description": "Add the reading time to Chrome Extension documentation articles"
}
```

Example 2 (unknown):
```unknown
{
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "content_scripts": [
    {
      "js": ["scripts/content.js"],
      "matches": [
        "https://developer.chrome.com/docs/extensions/*",
        "https://developer.chrome.com/docs/webstore/*"
      ]
    }
  ]
}
```

Example 4 (javascript):
```javascript
function renderReadingTime(article) {
  // If we weren't provided an article, we don't need to render anything.
  if (!article) {
    return;
  }

  const text = article.textContent;
  const wordMatchRegExp = /[^\s]+/g; // Regular expression
  const words = text.matchAll(wordMatchRegExp);
  // matchAll returns an iterator, convert to array to get word count
  const wordCount = [...words].length;
  const readingTime = Math.round(wordCount / 200);
  const badge = document.createElement("p");
  // Use the same styling as the publish information in an article's header
  badge.classList.add("color-secondary-text", "type--caption");
  badge.textContent = `⏱️ ${readingTime} min read`;

  // Support for API reference docs
  const heading = article.querySelector("h1");
  // Support for article docs with date
  const date = article.querySelector("time")?.parentNode;

  (date ?? heading).insertAdjacentElement("afterend", badge);
}

renderReadingTime(document.querySelector("article"));
```

---

## 将脚本注入到当前活动的标签页中 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/scripts-activetab

**Contents:**
- 将脚本注入到当前活动的标签页中 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展数据和图标
  - 第 2 步：初始化扩展程序
  - 第 3 步：启用扩展程序操作
    - 使用 activeTab 权限保护用户隐私
  - 第 4 步：跟踪当前标签页的状态
  - 第 5 步：添加或移除样式表
  - （可选）分配键盘快捷键

本教程将构建一个扩展程序，用于简化 Chrome 扩展程序和 Chrome 应用商店文档页面的样式，以便更轻松地阅读这些页面。

本指南假定您具备基本的 Web 开发经验。如需了解扩展程序开发工作流程，请参阅 Hello World。

首先，创建一个名为 focus-mode 的新目录来存放扩展程序文件。您可以在 GitHub 上下载完整源代码。

创建 manifest.json 文件，复制并粘贴以下代码：

创建一个 images 文件夹，然后将图标下载到该文件夹中。

扩展程序可以使用扩展程序的服务工作器在后台监控浏览器事件。服务工作线程是一种特殊的 JavaScript 环境，用于处理事件，并在不需要时终止。

首先，在 manifest.json 文件中注册 Service Worker：

创建一个名为 background.js 的文件，并添加以下代码：

我们的服务工作线程将侦听的第一个事件是 runtime.onInstalled()。此方法允许扩展程序在安装时设置初始状态或完成某些任务。扩展程序可以使用 Storage API 和 IndexedDB 来存储应用状态。在本例中，由于我们只处理两种状态，因此使用操作的徽章文本来跟踪扩展程序是处于“开启”还是“关闭”状态。

扩展程序操作用于控制扩展程序的工具栏图标。当用户选择扩展程序图标时，扩展程序会运行代码（如本例所示）或显示弹出式窗口。

在 manifest.json 文件中添加以下代码，以声明扩展程序操作：

activeTab 权限授予扩展程序在有效标签页上执行代码的临时能力。它还允许访问当前标签页的敏感属性。

当用户调用扩展程序时，系统会启用此权限。在这种情况下，用户通过点击扩展程序操作来调用扩展程序。

💡 在我的扩展程序中，还有哪些用户互动会启用 activeTab 权限？

"activeTab" 权限允许用户有目的地选择在聚焦的标签页上运行扩展程序；这样可以保护用户隐私。另一个好处是，它不会触发权限警告。

如需使用 "activeTab" 权限，请将其添加到清单的权限数组中：

用户点击扩展程序操作后，扩展程序会检查网址是否与文档页面匹配。接下来，它会检查当前标签页的状态并设置下一个状态。将以下代码添加到 background.js：

现在，您可以更改页面布局了。创建一个名为 focus-mode.css 的文件，并添加以下代码：

使用 Scripting API 插入或移除样式表。首先，在清单中声明 "scripting" 权限：

最后，在 background.js 中添加以下代码以更改页面布局：

为了好玩，添加了一个快捷方式，以便更轻松地启用或停用专注模式。 将 "commands" 键添加到清单中。

"_execute_action" 键运行的代码与 action.onClicked() 事件运行的代码相同，因此无需添加其他代码。

如需在开发者模式下加载未封装的扩展程序，请按照 Hello World 中的步骤操作。

然后，点击扩展程序操作。如果您设置了键盘快捷键，可以按 Ctrl+B 或 Cmd+B 对其进行测试。

根据您今天所学的内容，尝试完成以下任一任务：

恭喜您完成本教程 🎉。继续完成本系列中的其他教程，提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待继续您的扩展程序开发学习之旅。我们推荐以下学习路线：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Focus Mode",
  "description": "Enable focus mode on Chrome's official Extensions and Chrome Web Store documentation.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 2 (unknown):
```unknown
{
  ...
  "background": {
    "service_worker": "background.js"
  },
  ...
}
```

Example 3 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "OFF",
  });
});
```

Example 4 (unknown):
```unknown
{
  ...
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  ...
}
```

---

## 将脚本注入到当前活动的标签页中 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/scripts-activetab?hl=zh-cn

**Contents:**
- 将脚本注入到当前活动的标签页中 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展数据和图标
  - 第 2 步：初始化扩展程序
  - 第 3 步：启用扩展程序操作
    - 使用 activeTab 权限保护用户隐私
  - 第 4 步：跟踪当前标签页的状态
  - 第 5 步：添加或移除样式表
  - （可选）分配键盘快捷键

本教程将构建一个扩展程序，用于简化 Chrome 扩展程序和 Chrome 应用商店文档页面的样式，以便更轻松地阅读这些页面。

本指南假定您具备基本的 Web 开发经验。如需了解扩展程序开发工作流程，请参阅 Hello World。

首先，创建一个名为 focus-mode 的新目录来存放扩展程序文件。您可以在 GitHub 上下载完整源代码。

创建 manifest.json 文件，复制并粘贴以下代码：

创建一个 images 文件夹，然后将图标下载到该文件夹中。

扩展程序可以使用扩展程序的服务工作器在后台监控浏览器事件。服务工作线程是一种特殊的 JavaScript 环境，用于处理事件，并在不需要时终止。

首先，在 manifest.json 文件中注册 Service Worker：

创建一个名为 background.js 的文件，并添加以下代码：

我们的服务工作线程将侦听的第一个事件是 runtime.onInstalled()。此方法允许扩展程序在安装时设置初始状态或完成某些任务。扩展程序可以使用 Storage API 和 IndexedDB 来存储应用状态。在本例中，由于我们只处理两种状态，因此使用操作的徽章文本来跟踪扩展程序是处于“开启”还是“关闭”状态。

扩展程序操作用于控制扩展程序的工具栏图标。当用户选择扩展程序图标时，扩展程序会运行代码（如本例所示）或显示弹出式窗口。

在 manifest.json 文件中添加以下代码，以声明扩展程序操作：

activeTab 权限授予扩展程序在有效标签页上执行代码的临时能力。它还允许访问当前标签页的敏感属性。

当用户调用扩展程序时，系统会启用此权限。在这种情况下，用户通过点击扩展程序操作来调用扩展程序。

💡 在我的扩展程序中，还有哪些用户互动会启用 activeTab 权限？

"activeTab" 权限允许用户有目的地选择在聚焦的标签页上运行扩展程序；这样可以保护用户隐私。另一个好处是，它不会触发权限警告。

如需使用 "activeTab" 权限，请将其添加到清单的权限数组中：

用户点击扩展程序操作后，扩展程序会检查网址是否与文档页面匹配。接下来，它会检查当前标签页的状态并设置下一个状态。将以下代码添加到 background.js：

现在，您可以更改页面布局了。创建一个名为 focus-mode.css 的文件，并添加以下代码：

使用 Scripting API 插入或移除样式表。首先，在清单中声明 "scripting" 权限：

最后，在 background.js 中添加以下代码以更改页面布局：

为了好玩，添加了一个快捷方式，以便更轻松地启用或停用专注模式。 将 "commands" 键添加到清单中。

"_execute_action" 键运行的代码与 action.onClicked() 事件运行的代码相同，因此无需添加其他代码。

如需在开发者模式下加载未封装的扩展程序，请按照 Hello World 中的步骤操作。

然后，点击扩展程序操作。如果您设置了键盘快捷键，可以按 Ctrl+B 或 Cmd+B 对其进行测试。

根据您今天所学的内容，尝试完成以下任一任务：

恭喜您完成本教程 🎉。继续完成本系列中的其他教程，提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待继续您的扩展程序开发学习之旅。我们推荐以下学习路线：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Focus Mode",
  "description": "Enable focus mode on Chrome's official Extensions and Chrome Web Store documentation.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 2 (unknown):
```unknown
{
  ...
  "background": {
    "service_worker": "background.js"
  },
  ...
}
```

Example 3 (javascript):
```javascript
chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "OFF",
  });
});
```

Example 4 (unknown):
```unknown
{
  ...
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  ...
}
```

---

## 管理标签页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/popup-tabs-manager?hl=zh-cn

**Contents:**
- 管理标签页 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展程序数据和图标
  - 第 2 步：创建并设置弹出式窗口的样式
  - 第 3 步：管理标签页
    - 请求权限
    - 查询标签页
    - 将焦点置于标签页

本教程将构建一个标签页管理器，用于整理 Chrome 扩展程序和 Chrome 应用商店文档标签页。

本指南假定您具备基本的 Web 开发经验。我们建议您查看 Hello World，了解扩展程序开发工作流程。

首先，创建一个名为 tabs-manager 的新目录来存放扩展程序的文件。如果您愿意，可以前往 GitHub 下载完整的源代码。

创建一个名为 manifest.json 的文件，并添加以下代码：

如需详细了解这些清单键，请参阅“阅读时间”教程，其中详细介绍了扩展程序的metadata和图标。

创建一个 images 文件夹，然后将下载的图标下载到该文件夹中。

Action API 用于控制扩展程序操作（工具栏图标）。当用户点击扩展程序操作时，扩展程序会运行一些代码或打开一个弹出式窗口（如本例所示）。首先，在 manifest.json 中声明弹出式窗口：

弹出式窗口与网页类似，但有一个例外情况：它无法运行内嵌 JavaScript。创建一个 popup.html 文件，并添加以下代码。

接下来，您将为弹出式窗口设置样式。创建一个 popup.css 文件，并添加以下代码。

借助 Tabs API，扩展程序可以在浏览器中创建、查询、修改和重新排列标签页。

无需请求任何权限，即可使用 Tabs API 中的许多方法。不过，我们需要访问标签页的 title 和 URL；这些敏感属性需要权限。我们可以请求 "tabs" 权限，但这会授予对所有标签页的敏感属性的访问权限。由于我们只管理特定网站的标签页，因此我们将请求获得有限的主机权限。

通过限制主机权限，我们可以向特定网站授予提升后的权限，从而保护用户隐私。这将授予对 title 和 URL 属性以及其他功能的访问权限。将突出显示的代码添加到 manifest.json 文件中：

💡? 标签页权限和主机权限之间的主要区别是什么？

"tabs" 权限可让扩展程序读取所有标签页中的敏感数据。随着时间的推移，这些信息可能会被用于收集用户的浏览记录。因此，如果您请求此权限，Chrome 会在安装时显示以下警告消息：

借助主机权限，扩展程序可以读取和查询匹配标签页的敏感属性，还可以在这些标签页中注入脚本。用户在安装时会看到以下警告消息：

这些警告可能会让用户感到担忧。为了提供更好的新手入门体验，我们建议您实现可选权限。

您可以使用 tabs.query() 方法从特定网址检索标签页。创建一个 popup.js 文件，并添加以下代码：

💡? 我可以在弹出式窗口中直接使用 Chrome API 吗？

弹出式窗口和其他扩展程序页面可以调用任何 Chrome API，因为它们是从 Chrome 架构中提供的。例如 chrome-extension://EXTENSION_ID/popup.html。

首先，该扩展程序会按字母顺序对标签页名称（包含的 HTML 网页的标题）进行排序。然后，当点击某个列表项时，它会使用 tabs.update() 将焦点移至该标签页，并使用 windows.update() 将窗口置于前台。将以下代码添加到 popup.js 文件中：

💡? 此代码中使用的有趣 JavaScript

借助 TabGroups API，扩展程序可以为分组命名并选择背景颜色。添加突出显示的代码，将 "tabGroups" 权限添加到清单中：

在 popup.js 中，添加以下代码以创建一个按钮，该按钮将使用 tabs.group() 对所有标签页进行分组，并将其移至当前窗口。

如需在开发者模式下加载未封装的扩展程序，请按照 Hello World 中的步骤操作。

根据您今天学到的内容，尝试实现以下任一操作：

恭喜您完成本教程 🎉?。请继续学习本系列的其他教程，不断提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待您继续学习 Chrome 开发。我们建议您采用以下学习路径：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Tab Manager for Chrome Dev Docs",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 2 (unknown):
```unknown
{
  "action": {
    "default_popup": "popup.html"
  }
}
```

Example 3 (unknown):
```unknown
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./popup.css" />
  </head>
  <body>
    <template id="li_template">
      <li>
        <a>
          <h3 class="title">Tab Title</h3>
          <p class="pathname">Tab Pathname</p>
        </a>
      </li>
    </template>

    <h1>Google Dev Docs</h1>
    <button>Group Tabs</button>
    <ul></ul>

    <script src="./popup.js" type="module"></script>
  </body>
</html>
```

Example 4 (unknown):
```unknown
body {
  width: 20rem;
}

ul {
  list-style-type: none;
  padding-inline-start: 0;
  margin: 1rem 0;
}

li {
  padding: 0.25rem;
}
li:nth-child(odd) {
  background: #80808030;
}
li:nth-child(even) {
  background: #ffffff;
}

h3,
p {
  margin: 0;
}
```

---

## 在每个网页上运行脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/get-started/tutorial/scripts-on-every-tab

**Contents:**
- 在每个网页上运行脚本 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 概览
- 前期准备
- 构建扩展程序
  - 第 1 步：添加扩展程序的相关信息
  - 第 2 步：提供图标
  - 第 3 步：声明内容脚本
  - 第 4 步：计算并插入阅读时间
  - 第 5 步：监听更改
- 测试是否生效

本教程将构建一个扩展程序，用于向任何 Chrome 扩展程序和 Chrome 应用商店文档页面添加预计阅读时间。

本指南假定您具备基本的 Web 开发经验。我们建议您查看 Hello World 教程，了解扩展程序开发工作流程。

首先，创建一个名为 reading-time 的新目录来存放扩展程序的文件。如果您愿意，可以从 GitHub 下载完整源代码。

清单 JSON 文件是唯一的必需文件。其中包含有关扩展程序的重要信息。在项目的根目录中创建一个 manifest.json 文件，并添加以下代码：

这些键包含扩展程序的基本元数据。这些信息用于控制扩展程序在“扩展程序”页面上以及在发布后在 Chrome 应用商店中的显示方式。如需深入了解，请参阅清单概览页面上的 "name"、"version" 和 "description" 键。

那么，为什么需要图标？虽然在开发过程中图标是可选的，但如果您打算在 Chrome 应用商店中分发扩展程序，则必须提供图标。它们还会显示在扩展程序管理页面等其他位置。

创建一个 images 文件夹，并将图标放入其中。您可以在 GitHub 上下载图标。接下来，将突出显示的代码添加到清单中以声明图标：

我们建议使用 PNG 文件，但也允许使用其他文件格式（SVG 文件除外）。

扩展程序可以运行脚本，以读取和修改网页内容。这些脚本称为内容脚本。它们位于隔离的世界中，这意味着它们可以更改自己的 JavaScript 环境，而不会与其托管页面或其他扩展程序的内容脚本发生冲突。

将以下代码添加到 manifest.json 以注册名为 content.js 的内容脚本。

"matches" 字段可以有一个或多个匹配模式。这些标记可让浏览器确定要将内容脚本注入哪些网站。匹配模式由以下三个部分组成：<scheme>://<host><path>。可以包含“*”字符。

当用户安装扩展程序时，浏览器会告知用户该扩展程序的功能。内容脚本会请求在符合匹配模式条件的网站上运行的权限。

如需详细了解扩展程序权限，请参阅声明权限并向用户发出警告。

内容脚本可以使用标准文档对象模型 (DOM) 读取和更改网页内容。该扩展程序首先会检查网页是否包含 <article> 元素。然后，它会统计此元素中的所有字词，并创建一个段落来显示总阅读时间。

在名为 scripts 的文件夹中创建一个名为 content.js 的文件，然后添加以下代码：

💡 此代码中使用的有趣 JavaScript

使用当前代码时，如果您使用左侧导航栏切换文章，阅读时间不会添加到新文章中。这是因为我们的网站是作为单页应用 (SPA) 实现的，该应用使用 History API 执行软导航。

为解决此问题，我们可以使用 MutationObserver 监听更改，并将阅读时间添加到新文章。

为此，请将以下代码添加到 content.js 底部：

如需在开发者模式下加载未封装的扩展程序，请按照开发基础知识中的步骤操作。

下面列出了几个网页，您可以打开这些网页，看看每篇文章需要多长时间才能读完。

根据您今天学到的内容，尝试实现以下任一操作：

恭喜您完成本教程 🎉。请继续学习本系列的其他教程，不断提升您的技能：

希望您喜欢构建此 Chrome 扩展程序，并期待您继续学习 Chrome 开发。我们建议您采用以下学习路径：

**Examples:**

Example 1 (unknown):
```unknown
{
  "manifest_version": 3,
  "name": "Reading time",
  "version": "1.0",
  "description": "Add the reading time to Chrome Extension documentation articles"
}
```

Example 2 (unknown):
```unknown
{
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

Example 3 (unknown):
```unknown
{
  "content_scripts": [
    {
      "js": ["scripts/content.js"],
      "matches": [
        "https://developer.chrome.com/docs/extensions/*",
        "https://developer.chrome.com/docs/webstore/*"
      ]
    }
  ]
}
```

Example 4 (javascript):
```javascript
function renderReadingTime(article) {
  // If we weren't provided an article, we don't need to render anything.
  if (!article) {
    return;
  }

  const text = article.textContent;
  const wordMatchRegExp = /[^\s]+/g; // Regular expression
  const words = text.matchAll(wordMatchRegExp);
  // matchAll returns an iterator, convert to array to get word count
  const wordCount = [...words].length;
  const readingTime = Math.round(wordCount / 200);
  const badge = document.createElement("p");
  // Use the same styling as the publish information in an article's header
  badge.classList.add("color-secondary-text", "type--caption");
  badge.textContent = `⏱️ ${readingTime} min read`;

  // Support for API reference docs
  const heading = article.querySelector("h1");
  // Support for article docs with date
  const date = article.querySelector("time")?.parentNode;

  (date ?? heading).insertAdjacentElement("afterend", badge);
}

renderReadingTime(document.querySelector("article"));
```

---
