# Chrome-Plugin-Dev - Permissions

**Pages:** 26

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/declare-permissions

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
"permissions"
```

Example 2 (unknown):
```unknown
"optional_permissions"
```

Example 3 (unknown):
```unknown
"content_scripts.matches"
```

Example 4 (unknown):
```unknown
"host_permissions"
```

---

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/permissions

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
chrome.permissions
```

Example 2 (unknown):
```unknown
optional_permissions
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

---

## 权限警告准则 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/permission_warnings?hl=zh-cn

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

**Examples:**

Example 1 (unknown):
```unknown
"<all_urls>"
```

Example 2 (unknown):
```unknown
npm install
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

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions?hl=zh-cn

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
chrome.permissions
```

Example 2 (unknown):
```unknown
optional_permissions
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
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
chrome.identity
```

Example 2 (unknown):
```unknown
ProfileUserInfo
```

Example 3 (unknown):
```unknown
identity.email
```

Example 4 (unknown):
```unknown
identity.email
```

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv3/declare_permissions?hl=zh-cn

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
"permissions"
```

Example 2 (unknown):
```unknown
"optional_permissions"
```

Example 3 (unknown):
```unknown
"content_scripts.matches"
```

Example 4 (unknown):
```unknown
"host_permissions"
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
permissions
```

Example 2 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 3 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 4 (unknown):
```unknown
optional_permissions
```

---

## chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/userScripts?hl=zh-cn

**Contents:**
- chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 启用 userScripts API 的使用
    - 138 之前的 Chrome 版本（开发者模式切换开关）
    - Chrome 138 及更高版本（“允许用户脚本”切换开关）
  - 检查 API 是否可用
  - 在隔离的世界中工作

使用 userScripts API 在用户脚本上下文中执行用户脚本。

如需使用用户脚本 API chrome.userScripts，请向 manifest.json 添加 "userScripts" 权限，并为要运行脚本的网站添加 "host_permissions"。

用户脚本是指注入到网页中的一小段代码，用于修改网页的外观或行为。与其他扩展功能（例如内容脚本和 chrome.scripting API）不同，用户脚本 API 可让您运行任意代码。如果扩展程序运行由用户提供的脚本，而这些脚本无法作为扩展程序软件包的一部分提供，则必须使用此 API。

在扩展程序获得使用 userScripts API 的权限后，用户必须启用特定切换开关，才能允许扩展程序使用该 API。所需的具体开关以及停用时的 API 行为因 Chrome 版本而异。

使用以下检查来确定用户需要启用哪个开关，例如在新用户引导期间：

以下部分介绍了不同的开关以及如何启用它们。

作为扩展程序开发者，您已在 Chrome 安装中启用开发者模式。您的用户还必须启用开发者模式。

您可以将以下说明复制并粘贴到扩展程序的用户文档中

点击开发者模式旁边的切换开关，以启用开发者模式。

允许用户脚本切换开关位于每个扩展程序的详情页面上（例如 chrome://extensions/?id=YOUR_EXTENSION_ID）。

您可以将以下说明复制并粘贴到扩展程序的用户文档中：

我们建议进行以下检查，以确定 userScripts API 是否已启用，因为该检查适用于所有 Chrome 版本。此检查会尝试调用 chrome.userScripts() 方法，当 API 可用时，该方法应始终成功。如果此调用抛出错误，则表示相应 API 不可用：

用户脚本和内容脚本都可以在隔离的世界或主世界中运行。隔离世界是主机页面或其他扩展程序无法访问的执行环境。这样一来，用户脚本就可以更改其 JavaScript 环境，而不会影响宿主页面或其他扩展程序的用户脚本和内容脚本。相反，用户脚本（和内容脚本）对宿主网页或其他扩展程序的用户脚本和内容脚本不可见。在主世界中运行的脚本可供宿主网页和其他扩展程序访问，并且对宿主网页和其他扩展程序可见。如需选择世界，请在调用 userScripts.register() 时传递 "USER_SCRIPT" 或 "MAIN"。

如需为 USER_SCRIPT 世界配置内容安全政策，请调用 userScripts.configureWorld()：

与内容脚本和离屏文档一样，用户脚本使用消息传递与其他扩展程序部分进行通信（这意味着它们可以像扩展程序的任何其他部分一样调用 runtime.sendMessage() 和 runtime.connect()）。不过，它们是使用专用事件处理程序（即不使用 onMessage 或 onConnect）接收的。这些处理程序分别称为 runtime.onUserScriptMessage 和 runtime.onUserScriptConnect。专用处理程序可让您更轻松地识别来自用户脚本（可信度较低的上下文）的消息。

在发送消息之前，您必须调用 configureWorld()，并将 messaging 实参设置为 true。请注意，您可以同时传递 csp 和 messaging 实参。

扩展程序更新时，用户脚本会被清除。您可以在扩展程序服务工作线程的 runtime.onInstalled 事件处理程序中运行代码，以重新添加它们。仅对传递给事件回调的 "update" 原因做出响应。

此示例来自我们示例代码库中的 userScript 示例。

以下示例展示了对 register() 的基本调用。第一个实参是一个对象数组，用于定义要注册的脚本。此处仅列出了部分选项。

用户脚本要在其中执行的 JavaScript 世界。

“MAIN” 指定 DOM 的执行环境，即与宿主网页的 JavaScript 共享的执行环境。

“USER_SCRIPT” 指定了用户脚本特有的执行环境，不受网页的 CSP 限制。

错误（如果有）。error 和 result 是互斥的。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

指定用户脚本不会注入到的网页的通配符模式。

排除此用户脚本原本会注入到的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的用户脚本的 ID。此属性不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

ScriptSource 对象的列表，用于定义要注入到匹配网页中的脚本的来源。必须为 ${ref:register} 指定此属性，并且指定时必须是一个非空数组。

指定此用户脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 ${ref:register} 指定此属性。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

用于运行脚本的 JavaScript 执行环境。默认值为 `USER_SCRIPT`。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

包含要注入的 JavaScript 代码的字符串。必须指定 file 或 code 中的一个。

要注入的 JavaScript 文件的路径（相对于扩展程序的根目录）。必须指定 file 或 code 中的一个。

getScripts 仅返回具有此列表中指定 ID 的脚本。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

ScriptSource 对象列表，用于定义要注入到目标中的脚本的来源。

运行脚本的 JavaScript“世界”。默认值为 USER_SCRIPT。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

指定全球 CSP。默认值为 `ISOLATED` 全球 csp。

指定是否公开消息传递 API。默认值为 false。

指定要更新的特定用户脚本世界的 ID。如果未提供，则更新默认用户脚本世界的属性。以英文下划线 (_) 开头的值是预留值。

配置 `USER_SCRIPT` 执行环境。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回相应扩展程序的所有动态注册的用户脚本。

如果指定，此方法仅返回与之匹配的用户脚本。

Promise<RegisteredUserScript[]>

Promise<WorldProperties[]>

RegisteredUserScript[]

重置用户脚本世界的配置。任何注入到具有指定 ID 的世界中的脚本都将使用默认世界配置。

要重置的用户脚本世界的 ID。如果省略，则重置默认世界的配置。

取消注册相应扩展程序的所有动态注册的用户脚本。

如果指定了此参数，此方法将仅取消注册与之匹配的用户脚本。

RegisteredUserScript[]

包含要更新的用户脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
userScripts
```

Example 2 (unknown):
```unknown
userScripts
```

Example 3 (unknown):
```unknown
chrome.userScripts
```

Example 4 (unknown):
```unknown
"userScripts"
```

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/scripting

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
chrome.scripting
```

Example 2 (unknown):
```unknown
chrome.scripting
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"host_permissions"
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
permissions
```

Example 2 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 3 (unknown):
```unknown
{
  "name": "Very Secure Extension",
  "version": "1.0",
  "description": "Example of a Secure Extension",
  "permissions": ["activeTab"],
  "manifest_version": 3
}
```

Example 4 (unknown):
```unknown
optional_permissions
```

---

## 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions-list

**Contents:**
- 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如需访问大多数扩展程序 API 和功能，您必须在扩展程序的清单中声明权限。某些权限会触发警告，用户必须允许才能继续使用扩展程序。

如需详细了解权限的运作方式，请参阅声明权限。如需了解有关在有警告的情况下使用权限的最佳实践，请参阅权限警告指南。

以下列出了所有可用权限以及特定权限触发的所有警告。

**Examples:**

Example 1 (unknown):
```unknown
"accessibilityFeatures.modify"
```

Example 2 (unknown):
```unknown
chrome.accessibilityFeatures
```

Example 3 (unknown):
```unknown
"accessibilityFeatures.read"
```

Example 4 (unknown):
```unknown
chrome.accessibilityFeatures
```

---

## chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/management?hl=zh-cn

**Contents:**
- chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ExtensionDisabledReason
    - 枚举
  - ExtensionInfo
    - 属性
  - ExtensionInstallType
    - 枚举

chrome.management API 提供了管理安装式应用和扩展程序的方式。

必须在扩展程序清单中声明“管理”权限，才能使用 Management API。例如：

management.getPermissionWarningsByManifest()、management.uninstallSelf() 和 management.getSelf() 不需要管理权限。

"permissions_increase"

与已安装的扩展程序、应用或主题相关的信息。

ExtensionDisabledReason 可选

图标信息列表。请注意，这仅反映清单中声明的内容，实际图片尺寸可能与声明不符，建议在引用这些图像的 img 标签中显式指定宽度和高度属性。详见图标清单文档。

请使用 management.ExtensionInfo.type。

用户是否可以启用此扩展程序。仅对未启用的扩展程序返回此值。

扩展程序、应用或主题是否声明支持离线功能。

扩展程序、应用或主题的版本名称（如清单中已指定）。

扩展程序的安装方式。可能值包括 admin：因管理政策而安装； development：在开发者模式下以解压方式加载； normal：通过 .crx 文件正常安装； sideload：由机器上的其他软件安装； other：通过其他方式安装。

"legacy_packaged_app"

"login_screen_extension"

表示图标宽度和高度的数字。可能的值包括（但不限于）128、48、24 和 16。

图标图像的网址。如需显示图标的灰度版本（例如，指示扩展程序已禁用），可在网之后附加 ?grayscale=true。

"OPEN_AS_REGULAR_TAB"

是否应提示用户显示确认卸载对话框。自行卸载时，默认值为 false。如果扩展程序卸载其他扩展程序，系统会忽略此参数，并始终显示对话框。

显示为应用创建快捷方式的选项。在 Mac 上仅支持为打包应用创建。

应为 management.ExtensionInfo 应用项中的 ID。

网页的网址。网址的架构只能为“http”或“https”。

Promise<ExtensionInfo>

返回有关具有指定 ID 的已安装扩展程序、应用或主题的信息。

management.ExtensionInfo 项目的 ID。

Promise<ExtensionInfo>

返回有关已安装的扩展程序和应用的信息列表。

Promise<ExtensionInfo[]>

返回给定扩展程序清单字符串的权限警告列表。注意：使用此函数时，无需在清单中请求“管理”权限。

返回有关调用扩展程序、应用或主题的信息。注意：使用此函数时，无需在清单中请求“管理”权限。

Promise<ExtensionInfo>

启动清单中指定的 replacement_web_app。若未安装，提示用户安装。

启用或停用应用或扩展程序。在大多数情况下，此函数必须在用户手势（如按钮的 onclick 处理程序）上下文中调用，并且可能会向用户展示原生确认界面以防止滥用。

此值应为 management.ExtensionInfo 中某个项目的 ID。

应为 management.ExtensionInfo 应用项中的 ID。

目标启动类型。请务必检查并确保此启动类型位于 ExtensionInfo.availableLaunchTypes 中，因为可用的启动类型因平台和配置而异。

卸载当前安装式应用或扩展程序。注意：在用户未被授权卸载指定扩展程序/应用的受管理环境中，此功能将无法执行。若卸载失败（如用户取消对话框），系统将拒绝 promise 或回调将被调用，同时设置 runtime.lastError。

此值应为 management.ExtensionInfo 中某个项目的 ID。

卸载调用扩展程序。注意：使用此函数时，无需在清单中请求“管理”权限。但若用户无法卸载指定的扩展程序/应用，此函数在受管理环境中将无法执行。

**Examples:**

Example 1 (unknown):
```unknown
chrome.management
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "management"
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
    "management"
  ],
  ...
}
```

Example 4 (unknown):
```unknown
management.getPermissionWarningsByManifest()
```

---

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/scripting/?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
chrome.scripting
```

Example 2 (unknown):
```unknown
chrome.scripting
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"host_permissions"
```

---

## chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/userScripts

**Contents:**
- chrome.userScripts 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 概念和用法
  - 启用 userScripts API 的使用
    - 138 之前的 Chrome 版本（开发者模式切换开关）
    - Chrome 138 及更高版本（“允许用户脚本”切换开关）
  - 检查 API 是否可用
  - 在隔离的世界中工作

使用 userScripts API 在用户脚本上下文中执行用户脚本。

如需使用用户脚本 API chrome.userScripts，请向 manifest.json 添加 "userScripts" 权限，并为要运行脚本的网站添加 "host_permissions"。

用户脚本是指注入到网页中的一小段代码，用于修改网页的外观或行为。与其他扩展功能（例如内容脚本和 chrome.scripting API）不同，用户脚本 API 可让您运行任意代码。如果扩展程序运行由用户提供的脚本，而这些脚本无法作为扩展程序软件包的一部分提供，则必须使用此 API。

在扩展程序获得使用 userScripts API 的权限后，用户必须启用特定切换开关，才能允许扩展程序使用该 API。所需的具体开关以及停用时的 API 行为因 Chrome 版本而异。

使用以下检查来确定用户需要启用哪个开关，例如在新用户引导期间：

以下部分介绍了不同的开关以及如何启用它们。

作为扩展程序开发者，您已在 Chrome 安装中启用开发者模式。您的用户还必须启用开发者模式。

您可以将以下说明复制并粘贴到扩展程序的用户文档中

点击开发者模式旁边的切换开关，以启用开发者模式。

允许用户脚本切换开关位于每个扩展程序的详情页面上（例如 chrome://extensions/?id=YOUR_EXTENSION_ID）。

您可以将以下说明复制并粘贴到扩展程序的用户文档中：

我们建议进行以下检查，以确定 userScripts API 是否已启用，因为该检查适用于所有 Chrome 版本。此检查会尝试调用 chrome.userScripts() 方法，当 API 可用时，该方法应始终成功。如果此调用抛出错误，则表示相应 API 不可用：

用户脚本和内容脚本都可以在隔离的世界或主世界中运行。隔离世界是主机页面或其他扩展程序无法访问的执行环境。这样一来，用户脚本就可以更改其 JavaScript 环境，而不会影响宿主页面或其他扩展程序的用户脚本和内容脚本。相反，用户脚本（和内容脚本）对宿主网页或其他扩展程序的用户脚本和内容脚本不可见。在主世界中运行的脚本可供宿主网页和其他扩展程序访问，并且对宿主网页和其他扩展程序可见。如需选择世界，请在调用 userScripts.register() 时传递 "USER_SCRIPT" 或 "MAIN"。

如需为 USER_SCRIPT 世界配置内容安全政策，请调用 userScripts.configureWorld()：

与内容脚本和离屏文档一样，用户脚本使用消息传递与其他扩展程序部分进行通信（这意味着它们可以像扩展程序的任何其他部分一样调用 runtime.sendMessage() 和 runtime.connect()）。不过，它们是使用专用事件处理程序（即不使用 onMessage 或 onConnect）接收的。这些处理程序分别称为 runtime.onUserScriptMessage 和 runtime.onUserScriptConnect。专用处理程序可让您更轻松地识别来自用户脚本（可信度较低的上下文）的消息。

在发送消息之前，您必须调用 configureWorld()，并将 messaging 实参设置为 true。请注意，您可以同时传递 csp 和 messaging 实参。

扩展程序更新时，用户脚本会被清除。您可以在扩展程序服务工作线程的 runtime.onInstalled 事件处理程序中运行代码，以重新添加它们。仅对传递给事件回调的 "update" 原因做出响应。

此示例来自我们示例代码库中的 userScript 示例。

以下示例展示了对 register() 的基本调用。第一个实参是一个对象数组，用于定义要注册的脚本。此处仅列出了部分选项。

用户脚本要在其中执行的 JavaScript 世界。

“MAIN” 指定 DOM 的执行环境，即与宿主网页的 JavaScript 共享的执行环境。

“USER_SCRIPT” 指定了用户脚本特有的执行环境，不受网页的 CSP 限制。

错误（如果有）。error 和 result 是互斥的。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

指定用户脚本不会注入到的网页的通配符模式。

排除此用户脚本原本会注入到的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的用户脚本的 ID。此属性不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

ScriptSource 对象的列表，用于定义要注入到匹配网页中的脚本的来源。必须为 ${ref:register} 指定此属性，并且指定时必须是一个非空数组。

指定此用户脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 ${ref:register} 指定此属性。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

用于运行脚本的 JavaScript 执行环境。默认值为 `USER_SCRIPT`。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

包含要注入的 JavaScript 代码的字符串。必须指定 file 或 code 中的一个。

要注入的 JavaScript 文件的路径（相对于扩展程序的根目录）。必须指定 file 或 code 中的一个。

getScripts 仅返回具有此列表中指定 ID 的脚本。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

ScriptSource 对象列表，用于定义要注入到目标中的脚本的来源。

运行脚本的 JavaScript“世界”。默认值为 USER_SCRIPT。

指定要执行的用户脚本世界 ID。如果省略，脚本将在默认的用户脚本世界中执行。仅在省略 world 或 world 为 USER_SCRIPT 时有效。以英文下划线 (_) 开头的值是预留值。

指定全球 CSP。默认值为 `ISOLATED` 全球 csp。

指定是否公开消息传递 API。默认值为 false。

指定要更新的特定用户脚本世界的 ID。如果未提供，则更新默认用户脚本世界的属性。以英文下划线 (_) 开头的值是预留值。

配置 `USER_SCRIPT` 执行环境。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回相应扩展程序的所有动态注册的用户脚本。

如果指定，此方法仅返回与之匹配的用户脚本。

Promise<RegisteredUserScript[]>

Promise<WorldProperties[]>

RegisteredUserScript[]

重置用户脚本世界的配置。任何注入到具有指定 ID 的世界中的脚本都将使用默认世界配置。

要重置的用户脚本世界的 ID。如果省略，则重置默认世界的配置。

取消注册相应扩展程序的所有动态注册的用户脚本。

如果指定了此参数，此方法将仅取消注册与之匹配的用户脚本。

RegisteredUserScript[]

包含要更新的用户脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
userScripts
```

Example 2 (unknown):
```unknown
userScripts
```

Example 3 (unknown):
```unknown
chrome.userScripts
```

Example 4 (unknown):
```unknown
"userScripts"
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
chrome.identity
```

Example 2 (unknown):
```unknown
ProfileUserInfo
```

Example 3 (unknown):
```unknown
identity.email
```

Example 4 (unknown):
```unknown
identity.email
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

**Examples:**

Example 1 (unknown):
```unknown
"<all_urls>"
```

Example 2 (unknown):
```unknown
npm install
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

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/scripting?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
chrome.scripting
```

Example 2 (unknown):
```unknown
chrome.scripting
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"host_permissions"
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
"activeTab"
```

Example 2 (unknown):
```unknown
"<all_urls>"
```

Example 3 (unknown):
```unknown
"activeTab"
```

Example 4 (unknown):
```unknown
"activeTab"
```

---

## chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/mv2/reference/declarativeNetRequest

**Contents:**
- chrome.declarativeNetRequest 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和使用
  - 动态规则集和会话级范围的规则集
  - 静态规则集
  - 启用和停用静态规则和规则集
  - 构建规则

chrome.declarativeNetRequest API 用于通过指定声明性规则来屏蔽或修改网络请求。这样，扩展程序就可以修改网络请求，而无需拦截这些请求并查看其内容，从而提供更高的隐私保护。

declarativeNetRequestFeedbackhost_permissions

除了上述权限之外，某些类型的规则集（尤其是静态规则集）还需要声明 "declarative_net_request" 清单键，该键应是一个包含单个键（名为 "rule_resources"）的字典。此键是一个包含 Ruleset 类型字典的数组，如下所示。（请注意，由于“Ruleset”只是一个数组，因此不会显示在清单的 JSON 中。）本文档后面部分介绍了静态规则集。

如需使用此 API，请指定一个或多个规则集。规则集包含一个规则数组。单个规则可执行以下操作之一：

在使用扩展程序时，动态规则集和会话规则集通过 JavaScript 进行管理。

每种规则集类型只有一个。扩展程序可以通过调用 updateDynamicRules() 和 updateSessionRules() 动态添加或移除规则，前提是未超出规则限制。如需了解规则限制，请参阅规则限制。您可以在代码示例下查看相关示例。

与动态规则和会话规则不同，静态规则在安装或升级扩展程序时进行打包、安装和更新。它们以 JSON 格式存储在规则文件中，并使用 "declarative_net_request" 和 "rule_resources" 键（如上所述）以及一个或多个 Ruleset 字典向扩展程序指示。Ruleset 字典包含规则文件的路径、文件中包含的规则集的 ID，以及规则集是启用还是停用。当您以编程方式启用或停用规则集时，后两个属性非常重要。

如需测试规则文件，请以未打包的形式加载扩展程序。有关无效静态规则的错误和警告仅针对未打包的扩展程序显示。系统会忽略打包扩展程序中的无效静态规则。

在运行时，您可以启用或停用单个静态规则和完整的静态规则集。

已启用的静态规则和规则集的集合会在浏览器会话之间保持不变。这两者都不会在扩展程序更新后保留，这意味着只有您选择保留在规则文件中的规则会在更新后可用。

出于性能方面的原因，一次可启用的规则和规则集数量也有限制。调用 getAvailableStaticRuleCount() 以检查可启用的额外规则的数量。如需了解规则限制，请参阅规则限制。

如需启用或停用静态规则，请调用 updateStaticRules()。此方法接受一个 UpdateStaticRulesOptions 对象，其中包含要启用或停用的规则 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

如需启用或停用静态规则集，请调用 updateEnabledRulesets()。此方法接受一个 UpdateRulesetOptions 对象，其中包含要启用或停用的规则集 ID 数组。ID 使用 Ruleset 字典的 "id" 键进行定义。

无论规则类型如何，规则都以四个字段开头，如下所示。虽然 "id" 和 "priority" 键采用的是数字，但 "action" 和 "condition" 键可以提供多个屏蔽和重定向条件。以下规则会屏蔽从 "foo.com" 发送到任何包含 "abc" 作为子字符串的网址的所有脚本请求。

规则的 "condition" 键允许使用 "urlFilter" 键来处理指定网域下的网址。您可以使用模式匹配令牌创建模式。下面列举了一些示例。

规则由网页发送的请求触发。如果多条规则与特定请求匹配，则必须确定这些规则的优先级。本部分将介绍如何确定这些通知的优先级。确定优先顺序分为两个阶段。

您可以这样考虑匹配：特定扩展程序优先考虑的任何规则都将优先于其他扩展程序的规则。

在单个扩展服务中，优先级是通过以下流程确定的：

如果有多条规则具有最高的开发者定义优先级，则使用 "action" 字段按以下顺序确定规则的优先级：

如果操作类型不是 block 或 redirect，则评估任何匹配的 modifyHeaders 规则。请注意，如果存在任何开发者定义的优先级低于为 allow 和 allowAllRequests 指定的优先级的规则，则会忽略这些规则。

如果多条规则修改了同一标头，则修改由开发者定义的 "priority" 字段和指定的操作决定。

如果只有一个扩展程序的规则与请求匹配，则应用该规则。不过，如果有多个扩展程序与请求匹配，系统会使用以下流程：

系统会使用 "action" 字段按以下顺序确定规则的优先级：

如果有多个规则匹配，则最近安装的扩展程序优先。

在浏览器中加载和评估规则会产生性能开销，因此使用该 API 时会受到一些限制。限制取决于您使用的规则类型。

静态规则是指在清单文件中声明的规则文件中指定的规则。扩展程序最多可以在 "rule_resources" 清单键中指定 50 个静态规则集，但一次只能启用其中的 10 个规则集。后者称为 MAX_NUMBER_OF_ENABLED_STATIC_RULESETS。这些规则集总共至少包含 30,000 条规则。这称为 GUARANTEED_MINIMUM_STATIC_RULES。

之后可用的规则数量取决于用户浏览器上安装的所有扩展程序启用的规则数量。您可以在运行时通过调用 getAvailableStaticRuleCount() 找到此数字。您可以在代码示例下查看相关示例。

应用于动态规则和会话规则的限制比静态规则更简单。两者的总数不得超过 5,000。这称为 MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES。

所有类型的规则都可以使用正则表达式；不过，每种类型的正则表达式规则总数不得超过 1000 条。这称为 MAX_NUMBER_OF_REGEX_RULES。

此外，每条规则在编译后的大小必须小于 2KB。这与规则的复杂程度大致相关。如果您尝试加载超出此限制的规则，系统会显示如下警告，并忽略该规则。

declarativeNetRequest 仅适用于到达网络堆栈的请求。这包括来自 HTTP 缓存的响应，但不一定包括通过服务工作线程的 onfetch 处理程序的响应。declarativeNetRequest 不会影响由服务工作线程生成的响应或从 CacheStorage 检索的响应，但会影响在服务工作线程中对 fetch() 的调用。

declarativeNetRequest 规则无法将公开资源请求重定向到无法通过网络访问的资源。这样做会触发错误。即使指定的 Web 可访问资源归重定向扩展程序所有，也是如此。如需为 declarativeNetRequest 声明资源，请使用清单的 "web_accessible_resources" 数组。

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

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回给定 Ruleset 中当前已停用的静态规则列表。

GetDisabledRuleIdsOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回扩展程序的当前动态规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回与扩展程序匹配的所有规则。调用方可以选择性地通过指定 filter 来过滤匹配规则的列表。此方法仅适用于具有 "declarativeNetRequestFeedback" 权限或已针对 filter 中指定的 tabId 授予 "activeTab" 权限的扩展程序。注意：如果规则未与有效文档相关联，且匹配时间超过 5 分钟，则不会返回该规则。

MatchedRulesFilter 可选

Promise<RulesMatchedDetails>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

返回扩展程序的当前会话范围规则集。来电者可以选择指定 filter 来过滤提取的规则列表。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检查给定的正则表达式是否会作为 regexFilter 规则条件受到支持。

IsRegexSupportedResult

Promise<IsRegexSupportedResult>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

配置是否应将标签页的操作次数显示为扩展程序操作的徽章文本，并提供一种递增该操作次数的方法。

ExtensionActionOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

检查扩展程序的任何 declarativeNetRequest 规则是否会与假设的请求匹配。注意：此方法仅适用于未打包的扩展程序，因为此方法仅用于扩展程序开发期间。

TestMatchRequestDetails

TestMatchOutcomeResult

Promise<TestMatchOutcomeResult>

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

修改扩展程序的当前动态规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

更新扩展程序的已启用静态规则集。系统会先移除 options.disableRulesetIds 中列出的 ID 对应的规则集，然后再添加 options.enableRulesetIds 中列出的规则集。请注意，已启用的静态规则集会在会话之间保持不变，但不会在扩展程序更新之间保持不变，也就是说，rule_resources 清单键将决定每次扩展程序更新时已启用的静态规则集。

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

修改扩展程序的当前会话范围规则集。系统会先移除 options.removeRuleIds 中列出的 ID 对应的规则，然后再添加 options.addRules 中给出的规则。注意：

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

停用和启用 Ruleset 中的各个静态规则。对已停用的 Ruleset 所属规则做出的更改将在该 Ruleset 下次启用时生效。

UpdateStaticRulesOptions

仅 Manifest V3 及更高版本支持 Promise，其他平台需要使用回调。

当规则与请求匹配时触发。仅适用于具有 "declarativeNetRequestFeedback" 权限的未打包扩展程序，因为此 API 仅用于调试目的。

**Examples:**

Example 1 (unknown):
```unknown
chrome.declarativeNetRequest
```

Example 2 (unknown):
```unknown
declarativeNetRequest
```

Example 3 (unknown):
```unknown
declarativeNetRequestWithHostAccess
```

Example 4 (unknown):
```unknown
declarativeNetRequestFeedback
```

---

## chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/management

**Contents:**
- chrome.management 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 类型
  - ExtensionDisabledReason
    - 枚举
  - ExtensionInfo
    - 属性
  - ExtensionInstallType
    - 枚举

chrome.management API 提供了管理安装式应用和扩展程序的方式。

必须在扩展程序清单中声明“管理”权限，才能使用 Management API。例如：

management.getPermissionWarningsByManifest()、management.uninstallSelf() 和 management.getSelf() 不需要管理权限。

"permissions_increase"

与已安装的扩展程序、应用或主题相关的信息。

ExtensionDisabledReason 可选

图标信息列表。请注意，这仅反映清单中声明的内容，实际图片尺寸可能与声明不符，建议在引用这些图像的 img 标签中显式指定宽度和高度属性。详见图标清单文档。

请使用 management.ExtensionInfo.type。

用户是否可以启用此扩展程序。仅对未启用的扩展程序返回此值。

扩展程序、应用或主题是否声明支持离线功能。

扩展程序、应用或主题的版本名称（如清单中已指定）。

扩展程序的安装方式。可能值包括 admin：因管理政策而安装； development：在开发者模式下以解压方式加载； normal：通过 .crx 文件正常安装； sideload：由机器上的其他软件安装； other：通过其他方式安装。

"legacy_packaged_app"

"login_screen_extension"

表示图标宽度和高度的数字。可能的值包括（但不限于）128、48、24 和 16。

图标图像的网址。如需显示图标的灰度版本（例如，指示扩展程序已禁用），可在网之后附加 ?grayscale=true。

"OPEN_AS_REGULAR_TAB"

是否应提示用户显示确认卸载对话框。自行卸载时，默认值为 false。如果扩展程序卸载其他扩展程序，系统会忽略此参数，并始终显示对话框。

显示为应用创建快捷方式的选项。在 Mac 上仅支持为打包应用创建。

应为 management.ExtensionInfo 应用项中的 ID。

网页的网址。网址的架构只能为“http”或“https”。

Promise<ExtensionInfo>

返回有关具有指定 ID 的已安装扩展程序、应用或主题的信息。

management.ExtensionInfo 项目的 ID。

Promise<ExtensionInfo>

返回有关已安装的扩展程序和应用的信息列表。

Promise<ExtensionInfo[]>

返回给定扩展程序清单字符串的权限警告列表。注意：使用此函数时，无需在清单中请求“管理”权限。

返回有关调用扩展程序、应用或主题的信息。注意：使用此函数时，无需在清单中请求“管理”权限。

Promise<ExtensionInfo>

启动清单中指定的 replacement_web_app。若未安装，提示用户安装。

启用或停用应用或扩展程序。在大多数情况下，此函数必须在用户手势（如按钮的 onclick 处理程序）上下文中调用，并且可能会向用户展示原生确认界面以防止滥用。

此值应为 management.ExtensionInfo 中某个项目的 ID。

应为 management.ExtensionInfo 应用项中的 ID。

目标启动类型。请务必检查并确保此启动类型位于 ExtensionInfo.availableLaunchTypes 中，因为可用的启动类型因平台和配置而异。

卸载当前安装式应用或扩展程序。注意：在用户未被授权卸载指定扩展程序/应用的受管理环境中，此功能将无法执行。若卸载失败（如用户取消对话框），系统将拒绝 promise 或回调将被调用，同时设置 runtime.lastError。

此值应为 management.ExtensionInfo 中某个项目的 ID。

卸载调用扩展程序。注意：使用此函数时，无需在清单中请求“管理”权限。但若用户无法卸载指定的扩展程序/应用，此函数在受管理环境中将无法执行。

**Examples:**

Example 1 (unknown):
```unknown
chrome.management
```

Example 2 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "permissions": [
    "management"
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
    "management"
  ],
  ...
}
```

Example 4 (unknown):
```unknown
management.getPermissionWarningsByManifest()
```

---

## 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/permissions-list?hl=zh-cn

**Contents:**
- 权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

如需访问大多数扩展程序 API 和功能，您必须在扩展程序的清单中声明权限。某些权限会触发警告，用户必须允许才能继续使用扩展程序。

如需详细了解权限的运作方式，请参阅声明权限。如需了解有关在有警告的情况下使用权限的最佳实践，请参阅权限警告指南。

以下列出了所有可用权限以及特定权限触发的所有警告。

**Examples:**

Example 1 (unknown):
```unknown
"accessibilityFeatures.modify"
```

Example 2 (unknown):
```unknown
chrome.accessibilityFeatures
```

Example 3 (unknown):
```unknown
"accessibilityFeatures.read"
```

Example 4 (unknown):
```unknown
chrome.accessibilityFeatures
```

---

## 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/develop/concepts/declare-permissions?hl=zh-cn

**Contents:**
- 声明权限 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 清单
- 主机权限
- 收到警告的权限
- 允许使用
  - 允许访问文件网址和无痕模式网页

如需使用大多数扩展程序 API 和功能，您必须在清单的权限字段中声明扩展程序的 intent。扩展程序可以请求使用相应清单键指定的以下类别的权限：

如果您的扩展程序遭到恶意软件入侵，权限有助于限制损害。系统会先向用户显示一些权限警告以征求用户同意 详情请参阅权限，但出现警告。

对于扩展程序的功能，请考虑使用可选权限 让用户在知情的情况下控制对资源和数据的访问权限。

如果 API 需要某项权限，请参阅其文档，了解如何声明该权限。对于 示例，请参阅 Storage API。

主机权限允许扩展程序与网址的匹配格式互动。有些 Chrome API 除了拥有自己的 API 权限外，还需要主机权限，详见各个参考页面。下面是一些示例：

当某个扩展程序请求多项权限，并且其中许多权限都显示时 在安装时出现警告，用户将看到警告列表，如下例所示：

如果扩展程序收到了有限的警告或附有相关说明，用户会更有可能信任该扩展程序 。请考虑实现可选权限或功能较低的 API 以避免收到警报 警告。如需了解警告的最佳实践，请参阅权限警告指南。特定 警告及其适用的权限 权限参考列表。

在 "host_permissions" 和 "content_scripts.matches" 中添加或更改匹配模式 字段也会触发警告。如需了解详情，请参阅 更新权限。

如果您的扩展程序需要在 file:// 个网址上运行或在无痕模式下运行，用户必须在其详情页面上向扩展程序授予访问权限。有关打开详情页面的说明，请参阅管理扩展程序。

向下滚动以启用文件网址访问权限或无痕模式。

如需检测用户是否授予了访问权限，您可以调用 extension.isAllowedIncognitoAccess() 或 extension.isAllowedFileSchemeAccess()。

**Examples:**

Example 1 (unknown):
```unknown
"permissions"
```

Example 2 (unknown):
```unknown
"optional_permissions"
```

Example 3 (unknown):
```unknown
"content_scripts.matches"
```

Example 4 (unknown):
```unknown
"host_permissions"
```

---

## chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/api/permissions?hl=zh-cn

**Contents:**
- chrome.permissions 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 概念和用法
  - 实现可选权限
    - 第 1 步：确定哪些权限是必需的，哪些是可选的
    - 第 2 步：在清单中声明可选权限
    - 第 3 步：请求可选权限
    - 第 4 步：检查扩展程序的当前权限
    - 第 5 步：移除权限
- 类型

使用 chrome.permissions API 在运行时（而非安装时）请求已声明为可选的权限，以便用户了解需要这些权限的原因，并仅授予必要的权限。

权限警告旨在说明 API 授予的功能，但其中一些警告可能并不明显。借助 Permissions API，开发者可以说明权限警告并逐步推出新功能，让用户在无风险的情况下了解扩展程序。这样，用户就可以指定愿意授予的访问权限以及想要启用的功能。

例如，可选权限扩展程序的核心功能是替换新标签页。其中一项功能是显示用户的每日目标。此功能仅需要存储空间权限，该权限不包含警告。该扩展程序还提供了一项附加功能，用户可以点击以下按钮来启用该功能：

显示用户的热门网站需要 topSites 权限，该权限具有以下警告。

扩展程序可以声明必需权限和可选权限。一般情况下，您应：

在扩展程序清单中使用 optional_permissions 键声明可选权限，格式与 permissions 字段相同：

如果您想请求仅在运行时发现的主机，请在扩展程序的 optional_host_permissions 字段中添加 "https://*/*"。这样，您就可以指定 "Permissions.origins" 中的任何来源，只要该来源具有匹配的方案即可。

大多数 Chrome 扩展程序权限都可以指定为可选，但以下权限除外。

如需详细了解可用权限及其警告，请参阅声明权限。

使用 permissions.request() 在用户手势中请求权限：

如果添加权限后显示的警告消息与用户已看到并接受的警告消息不同，Chrome 会提示用户。例如，上述代码可能会生成如下提示：

如需检查扩展程序是否具有特定权限或一组权限，请使用 permission.contains()：

当您不再需要权限时，应移除相应权限。移除权限后，调用 permissions.request() 通常会重新添加该权限，而不会提示用户。

主机权限列表，包括清单中 optional_permissions 或 permissions 键中指定的权限，以及与内容脚本关联的权限。

添加主机访问权限请求。仅当扩展程序可以获得请求中主机的访问权限时，才会向用户发出请求信号。在跨源导航时，请求将被重置。接受后，授予对网站顶级来源的持久访问权限

可显示主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。如果提供此参数，则请求会显示在指定文档的标签页中，并在文档导航到新来源时移除。添加新请求将覆盖针对 tabId 的所有现有请求。必须指定此参数或 tabId。

可显示主机访问权限请求的网址格式。如果提供，则仅在与此模式匹配的网址上显示主机访问权限请求。

可显示主机访问权限请求的标签页的 ID。如果提供，请求将显示在指定标签页上，并在该标签页导航到新来源时移除。添加新请求将覆盖针对“documentId”的现有请求。必须指定此参数或 documentId。

移除对指定权限的访问权限。如果移除权限时遇到任何问题，系统会设置 runtime.lastError。

要移除主机访问权限请求的文档的 ID。必须是标签页中的顶级文档。必须指定此参数或 tabId。

将移除主机访问权限请求的网址格式。如果提供，则必须与现有主机访问权限请求的模式完全匹配。

要移除主机访问权限请求的标签页的 ID。必须指定此参数或 documentId。

请求访问指定权限，并在必要时向用户显示提示。这些权限必须在清单的 optional_permissions 字段中定义，或者是由用户拒绝的必需权限。源格式中的路径会被忽略。您可以请求可选来源权限的子集；例如，如果您在清单的 optional_permissions 部分中指定 *://*\/*，则可以请求 http://example.com/。如果请求权限时出现任何问题，系统会设置 runtime.lastError。

**Examples:**

Example 1 (unknown):
```unknown
chrome.permissions
```

Example 2 (unknown):
```unknown
optional_permissions
```

Example 3 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
```

Example 4 (unknown):
```unknown
{
  "name": "My extension",
  ...
  "optional_permissions": ["tabs"],
  "optional_host_permissions": ["https://www.google.com/"],
  ...
}
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
"activeTab"
```

Example 2 (unknown):
```unknown
"<all_urls>"
```

Example 3 (unknown):
```unknown
"activeTab"
```

Example 4 (unknown):
```unknown
"activeTab"
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

**Examples:**

Example 1 (unknown):
```unknown
"<all_urls>"
```

Example 2 (unknown):
```unknown
npm install
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

## chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。

**URL:** https://developer.chrome.google.cn/docs/extensions/reference/scripting?hl=zh-cn

**Contents:**
- chrome.scripting 使用集合让一切井井有条 根据您的偏好保存内容并对其进行分类。
- 说明
- 权限
- 可用性
- 清单
- 概念和用法
  - 注入目标
  - 注入的代码
    - 文件
    - 运行时函数

使用 chrome.scripting API 在不同上下文中执行脚本。

如需使用 chrome.scripting API，请在清单中声明 "scripting" 权限，并声明要注入脚本的网页的主机权限。使用 "host_permissions" 密钥或 "activeTab" 权限，该权限可授予临时主机权限。以下示例使用 activeTab 权限。

您可以使用 chrome.scripting API 将 JavaScript 和 CSS 注入网站。这与您可以使用内容脚本执行的操作类似。但通过使用 chrome.scripting 命名空间，扩展程序可以在运行时做出决策。

您可以使用 target 参数指定要将 JavaScript 或 CSS 注入到的目标。

唯一的必填字段是 tabId。默认情况下，注入将在指定标签页的主框架中运行。

如需在指定标签页的所有框架中运行，您可以将 allFrames 布尔值设置为 true。

您还可以通过指定各个框架 ID 将代码注入到标签页的特定框架中。如需详细了解框架 ID，请参阅 chrome.webNavigation API。

扩展程序可以通过外部文件或运行时变量指定要注入的代码。

文件以字符串形式指定，这些字符串是相对于扩展程序根目录的路径。以下代码会将文件 script.js 注入到标签页的主框架中。

使用 scripting.executeScript() 注入 JavaScript 时，您可以指定要执行的函数，而不是文件。此函数应为可用于当前扩展程序上下文的函数变量。

如果在网页中注入 CSS，您还可以指定要在 css 属性中使用的字符串。此选项仅适用于 scripting.insertCSS()；您无法使用 scripting.executeScript() 执行字符串。

执行 JavaScript 的结果会传递给扩展程序。每个帧中包含一个结果。主帧保证是结果数组中的第一个索引；所有其他帧的顺序不确定。

scripting.insertCSS() 不会返回任何结果。

如果脚本执行的最终值是一个 promise，Chrome 将等待该 promise 确定，然后返回最终值。

以下代码段包含一个函数，用于取消注册扩展程序之前注册的所有动态内容脚本。

如需试用 chrome.scripting API，请从 Chrome 扩展程序示例代码库中安装脚本示例。

如果指定了此参数，getRegisteredContentScripts 将仅返回 ID 包含在此列表中的脚本。

包含要注入的 CSS 的字符串。必须指定 files 和 css 中的一个（且只能指定其中一个）。

要注入的 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 和 css 中的一个（且只能指定其中一个）。

注入的样式来源。默认为 'AUTHOR'。

用于指定要将 CSS 插入到的目标的详细信息。

脚本要在其中执行的 JavaScript 世界。

“ISOLATED” 指定隔离的世界，即此扩展程序独有的执行环境。

“MAIN” 指定 DOM 的主要世界，即与宿主网页的 JavaScript 共享的执行环境。

脚本是否应注入到标签页中的所有框架。默认值为 false。如果指定了 frameIds，则此值不得为 true。

要注入到的特定 documentId 的 ID。如果设置了 frameIds，则不得设置此字段。

如果指定为 true，则会注入到所有框架中，即使该框架不是标签页中最顶层的框架也是如此。系统会针对每个框架单独检查网址要求；如果不满足网址要求，则不会注入到子框架中。默认值为 false，表示仅匹配顶部框架。

要注入到匹配页面中的 CSS 文件列表。这些脚本会按其在此数组中出现的顺序注入，在为网页构建或显示任何 DOM 之前注入。

排除此内容脚本本应注入的网页。如需详细了解这些字符串的语法，请参阅匹配模式。

API 调用中指定的内容脚本的 ID。不得以“_”开头，因为该字符预留为生成的脚本 ID 的前缀。

要注入到匹配网页中的 JavaScript 文件列表。这些参数会按照它们在此数组中显示的顺序注入。

指示脚本是否可以注入到网址包含不受支持的方案（具体而言，是 about:、data:、blob: 或 filesystem:）的框架中。在这种情况下，系统会检查网址的来源，以确定是否应注入脚本。如果来源为 null（例如 data: 网址），则所用来源为创建当前框架的框架或启动对此框架的导航的框架。请注意，这可能不是父框架。

指定此内容脚本将注入到哪些网页中。如需详细了解这些字符串的语法，请参阅匹配模式。必须为 registerContentScripts 指定。

指定此内容脚本是否会保留到未来的会话中。默认值为 true。

指定何时将 JavaScript 文件注入到网页中。首选值和默认值为 document_idle。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要传递给所提供函数的实参。仅当指定了 func 参数时，此参数才有效。这些实参必须可进行 JSON 序列化。

要注入的 JS 或 CSS 文件的路径（相对于扩展程序的根目录）。必须指定 files 或 func 中的一个。

是否应尽快在目标中触发注入。请注意，这并不保证注入会在网页加载之前发生，因为当脚本到达目标时，网页可能已经加载完毕。

运行脚本的 JavaScript“世界”。默认为 ISOLATED。

要注入的 JavaScript 函数。此函数将被序列化，然后反序列化以进行注入。这意味着所有绑定参数和执行上下文都将丢失。必须指定 files 或 func 中的一个。

样式更改的来源。如需了解详情，请参阅样式来源。

将脚本注入到目标上下文。默认情况下，脚本将在 document_idle 运行，如果网页已加载，则立即运行。如果设置了 injectImmediately 属性，即使网页尚未完成加载，脚本也会立即注入。如果脚本的评估结果为 promise，浏览器将等待 promise 确定，然后返回结果值。

Promise<InjectionResult[]>

返回此扩展程序的所有与指定过滤条件匹配的动态注册的内容脚本。

ContentScriptFilter 可选

Promise<RegisteredContentScript[]>

将 CSS 样式表插入到目标上下文中。如果指定了多个帧，系统会忽略注入失败的情况。

RegisteredContentScript[]

包含要注册的脚本列表。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 已存在，则不会注册任何脚本。

从目标上下文中移除之前由相应扩展程序插入的 CSS 样式表。

要移除的样式的详细信息。请注意，css、files 和 origin 属性必须与通过 insertCSS 插入的样式表完全匹配。尝试移除不存在的样式表是一项空操作。

ContentScriptFilter 可选

如果指定，则仅取消注册与过滤条件匹配的动态内容脚本。否则，系统会取消注册扩展程序的所有动态内容脚本。

RegisteredContentScript[]

包含要更新的脚本的列表。仅当属性在此对象中指定时，才会针对现有脚本更新该属性。如果在脚本解析/文件验证期间出现错误，或者指定的 ID 与完全注册的脚本不对应，则不会更新任何脚本。

**Examples:**

Example 1 (unknown):
```unknown
chrome.scripting
```

Example 2 (unknown):
```unknown
chrome.scripting
```

Example 3 (unknown):
```unknown
"scripting"
```

Example 4 (unknown):
```unknown
"host_permissions"
```

---
