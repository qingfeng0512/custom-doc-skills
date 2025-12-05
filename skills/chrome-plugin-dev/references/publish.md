# Chrome-Plugin-Dev - Publish

**Pages:** 11

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
chrome://extensions/
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

Example 4 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

---

## 使用其他安装方法 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/external_extensions?hl=zh-cn

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
https://clients2.google.com/service/update2/crx
```

Example 2 (unknown):
```unknown
chrome://extensions
```

Example 3 (unknown):
```unknown
chrome://extensions
```

Example 4 (unknown):
```unknown
chrome://extensions
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/publish-mv3

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

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
chrome://extensions/
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

Example 4 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
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
manifest.json
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
```unknown
service-worker.js
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
https://clients2.google.com/service/update2/crx
```

Example 2 (unknown):
```unknown
chrome://extensions
```

Example 3 (unknown):
```unknown
chrome://extensions
```

Example 4 (unknown):
```unknown
chrome://extensions
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/migrate/publish-mv3?hl=zh-cn

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

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
https://clients2.google.com/service/update2/crx
```

Example 2 (unknown):
```unknown
chrome://extensions
```

Example 3 (unknown):
```unknown
chrome://extensions
```

Example 4 (unknown):
```unknown
chrome://extensions
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
manifest.json
```

Example 2 (unknown):
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

Example 3 (unknown):
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

Example 4 (unknown):
```unknown
service-worker.js
```

---

## 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/migrating/publish-mv3?hl=zh-cn

**Contents:**
- 发布扩展程序 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 发布 Beta 版测试版本
  - 为 Beta 版添加标签
  - 通过电子邮件分发给测试人员
  - 分发给 Google 群组的成员
  - 使用直接链接分发给测试人员
- 逐步发布版本
- 根据审核时间调整计划
  - 分阶段发布
  - 查看商品状态

将扩展程序转换为清单版本 3 后，下一步是将其发布到 Chrome 网上应用店。根据您所做的更改程度，建议您先面向一小部分受众群体测试 Manifest V3 扩展程序，以确保其能按预期运行，然后再分阶段发布。

本文介绍了分阶段发布新版本的几种方法。例如，向测试人员发布 Beta 版，然后逐步面向用户群发布。我们还建议您监控扩展程序审核状态并留意用户反馈，以便根据需要快速发布任何 bug 修复程序。

发布 Beta 版扩展程序后，您可以先向一组测试人员收集反馈并排查问题，然后再将扩展程序发布给其他用户。Beta 版还需要经过 Chrome 应用商店审核流程。

首先，您必须按照以下步骤在 manifest.json 中将 Beta 版标记为测试版本：

现在，您的 Beta 版已明确标记，您可以将其分发给指定的电子邮件地址、Google 群组的成员，也可以作为直接链接进行分享。

如需向少量测试人员分发，请按以下步骤操作：

从 Beta 版测试人员那里收到足够的反馈后，您可以将分发范围扩大到您拥有或管理的某个 Google 群组的成员。

前往分发标签页，将公开范围设为“不公开”，然后从下拉菜单中选择您的 Beta 版测试人员 Google 群组。

另一种方法是将公开范围设为不公开列出。这样一来，只有拥有商品详情项直接链接的用户才能安装该扩展程序。

为确保任何意外问题的影响降到最低，您可以按照以下步骤逐步发布更新。此功能仅适用于活跃用户数超过 1 万的扩展程序。

如需继续逐步发布，请前往商品的文件包标签页，然后提高已发布部分中的百分比。请注意，此百分比只能增加，并且不会触发额外的审核。

我们建议您为商品留出足够的审核时间，因为审核时间可能会因不同因素而异。大多数扩展程序的审核会在 3 天内完成。考虑分阶段发布资源，并定期查看资源的状态，以便在必要时快速进行更改。

Chrome 应用商店提供了一种提前提交发布版本以供审核的方式来分阶段发布版本。这样一来，当您准备就绪时，就可以正式发布了。

为此，您可以在提交内容时取消选中“自动发布”复选框。

或者，您也可以稍后在右上角的三点状菜单中选择推迟发布。

当您的资源通过审核或被发现存在违规问题时，您通常会在 3 天内收到一封通知电子邮件。如果您在一周内未收到电子邮件，请在状态标签页的已发布部分查看商品的状态。

如果您的扩展程序在审核中的时间已超过两周，请与开发者支持团队联系以寻求帮助。

如果您发布的扩展程序更新存在 bug，并且想要立即回滚到较低版本，请使用 Chrome 应用商店回滚功能。

为了及时了解用户反馈，您可以在扩展程序详情页的“支持”标签页下添加指向专用支持网站的链接。

---

## Linux 的自托管 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/linux_hosting?hl=zh-cn

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
chrome://extensions/
```

Example 2 (unknown):
```unknown
manifest.json
```

Example 3 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

Example 4 (unknown):
```unknown
{
  ...
  "version": "1.5",
  ...
  }
}
```

---
