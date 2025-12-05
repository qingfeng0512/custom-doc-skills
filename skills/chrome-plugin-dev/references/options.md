# Chrome-Plugin-Dev - Options

**Pages:** 3

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
chrome://extensions
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
```unknown
options.html
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
chrome://extensions
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
```unknown
options.html
```

---

## 为用户提供选项 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/options?hl=zh-cn

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
chrome://extensions
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
```unknown
options.html
```

---
