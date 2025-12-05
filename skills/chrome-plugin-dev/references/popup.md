# Chrome-Plugin-Dev - Popup

**Pages:** 4

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
chrome.action.openPopup()
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
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
chrome.action.openPopup()
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
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
tabs-manager
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
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

Example 4 (unknown):
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
tabs-manager
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
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

Example 4 (unknown):
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

---
