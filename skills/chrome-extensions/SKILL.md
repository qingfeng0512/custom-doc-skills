---
name: chrome-extensions
description: Chrome extension development. Use for creating browser extensions, Manifest V3, content scripts, background scripts, popup development, Chrome API integration, extension packaging, or any Chrome extension-specific questions.
---

# Chrome-Extensions Skill

Comprehensive assistance with chrome-extensions development, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with chrome-extensions
- Asking about chrome-extensions features or APIs
- Implementing chrome-extensions solutions
- Debugging chrome-extensions code
- Learning chrome-extensions best practices

## Quick Reference

### Common Patterns

**Pattern 1:** Chrome 的扩展程序系统会强制执行相当严格的默认内容安全政策 (CSP)。 政策限制非常简单：脚本必须移出线，放入单独的 JavaScript 文件中，内嵌事件处理脚本必须转换为使用 addEventListener，并且 eval() 处于停用状态。 不过，我们也了解到，许多库都使用 eval() 和 eval 类构造（例如 new Function()）来优化性能和简化表达。模板库特别容易出现这种实现方式。虽然某些环境（如 Angular.js）支持 CSP out 许多热门框架尚未更新为与 Android Studio 兼容的 扩展程序的少了 eval 的世界。因此，我们发现移除对该功能的支持对开发者而言造成的问题比预期多。 本文档介绍了沙盒作为一种安全机制，可让您在项目中添加这些库，而不会影响安全性。 为什么要使用沙盒？ 在扩展程序中使用 eval 是危险的，因为它执行的代码可以访问扩展程序的高权限环境中的所有内容。提供了大量功能强大的 chrome.* API， 严重影响用户的安全和隐私；我们最担心的是简单的数据渗漏问题。 提供的解决方案是一个沙盒，在此沙盒中，eval 无需访问 或扩展程序的高价值 API。没有数据、不使用 API，也没有关系。 为此，我们会将扩展程序软件包内的特定 HTML 文件列为已沙盒化。 每当有沙盒机制加载网页时，系统都会将其移动到唯一来源，并会被拒绝 对 chrome.* API 的访问权限。如果通过 iframe 将此沙盒化页面加载到扩展程序中， 然后向其传递消息，让其以某种方式处理这些消息，然后等待它为我们传回 结果。通过这种简单的消息传递机制，我们可以安全地在扩展程序的工作流中包含 eval 驱动的代码。 创建和使用沙盒 如果您希望直接查看代码，请下载沙盒示例扩展程序 关闭。这是一个基于 Handlebars 构建的小型消息传递 API 的有效示例 模板库，它应该会为您提供开始操作所需的一切。对于希望了解更多说明的用户，我们来一起详细了解一下该示例。 列出清单中的文件 应该在沙盒中运行的每个文件都必须在扩展程序清单中列出，方法是添加 sandbox 属性。这是非常重要的一步，而且很容易被忘记，因此请仔细检查 您的沙盒文件会在清单中列出在此示例中，我们将对名为“sandbox.html”的文件进行沙盒化处理。清单条目如下所示： { ..., "sandbox": { "pages": ["sandbox.html"] }, ... } 加载沙盒文件 为了对沙盒化文件执行一些有趣的操作，我们需要在 可以通过该扩展程序的代码进行处理在这里，sandbox.html 已通过 iframe 加载到扩展程序页面中。网页的 JavaScript 文件包含以下代码：每当用户点击浏览器操作时，该代码都会通过查找网页上的 iframe 并对其 contentWindow 调用 postMessage()，将消息发送到沙盒。消息是一个包含以下三个属性的对象：context、templateName 和 command。我们稍后会深入探讨 context 和 command。 service-worker.js： chrome.action.onClicked.addListener(() => { chrome.tabs.create({ url: 'mainpage.html' }); console.log('Opened a tab with a sandboxed page!'); }); extension-page.js： let counter = 0; document.addEventListener('DOMContentLoaded', () => { document.getElementById('reset').addEventListener('click', function () { counter = 0; document.querySelector('#result').innerHTML = ''; }); document.getElementById('sendMessage').addEventListener('click', function () { counter++; let message = { command: 'render', templateName: 'sample-template-' + counter, context: { counter: counter } }; document.getElementById('theFrame').contentWindow.postMessage(message, '*'); }); 注意：如需有关 <code>postMessage()</code> 的一般信息，请参阅 MDN 上的 <a href="https://developer.mozilla.org/en/DOM/window.postMessage"><code>postMessage()</code> 文档 </a>。该文档非常详尽，值得阅读。特别要注意，只有可序列化的数据才能来回传递。例如，函数不可序列化。 执行危险操作 加载 sandbox.html 后，它会加载 Handlebars 库，创建并编译内嵌的 这就像 Handlebars 建议那样： extension-page.html： <!DOCTYPE html> <html> <head> <script src="mainpage.js"></script> <link href="styles/main.css" rel="stylesheet" /> </head> <body> <div id="buttons"> <button id="sendMessage">Click me</button> <button id="reset">Reset counter</button> </div> <div id="result"></div> <iframe id="theFrame" src="sandbox.html" style="display: none"></iframe> </body> </html> sandbox.html： <script id="sample-template-1" type="text/x-handlebars-template"> <div class='entry'> <h1>Hello</h1> <p>This is a Handlebar template compiled inside a hidden sandboxed iframe.</p> <p>The counter parameter from postMessage() (outer frame) is: </p> </div> </script> <script id="sample-template-2" type="text/x-handlebars-template"> <div class='entry'> <h1>Welcome back</h1> <p>This is another Handlebar template compiled inside a hidden sandboxed iframe.</p> <p>The counter parameter from postMessage() (outer frame) is: </p> </div> </script> 不会失败！即使 Handlebars.compile 最终使用了 new Function，但一切都按预期运行，最终在 templates['hello'] 中生成了编译后的模板。 传回结果 我们将设置一个消息监听器来接受来自扩展程序页面的命令，以便使用此模板。我们将使用传入的 command 来确定应执行的操作（您可以 想想不仅仅进行渲染创建模板？或许以某种方式管理它们？），并且 context 将直接传递到模板进行渲染。呈现的 HTML 将传回给扩展程序页面，以便扩展程序稍后可以对其执行一些有用操作： <script> const templatesElements = document.querySelectorAll( "script[type='text/x-handlebars-template']" ); let templates = {}, source, name; // precompile all templates in this page for (let i = 0; i < templatesElements.length; i++) { source = templatesElements[i].innerHTML; name = templatesElements[i].id; templates[name] = Handlebars.compile(source); } // Set up message event handler: window.addEventListener('message', function (event) { const command = event.data.command; const template = templates[event.data.templateName]; let result = 'invalid request'; // if we don't know the templateName requested, return an error message if (template) { switch (command) { case 'render': result = template(event.data.context); break; // you could even do dynamic compilation, by accepting a command // to compile a new template instead of using static ones, for example: // case 'new': // template = Handlebars.compile(event.data.templateSource); // result = template(event.data.context); // break; } } else { result = 'Unknown template: ' + event.data.templateName; } event.source.postMessage({ result: result }, event.origin); }); </script> 返回到扩展程序页面，我们会收到此消息，并使用 html 执行一些有趣的操作 传递的数据。在本例中，我们只会通过通知来回显它，但完全可以将此 HTML 安全地用作扩展程序界面的一部分。通过 innerHTML 插入它不会构成重大安全风险，因为我们信任在沙盒中呈现的内容。 这种机制使模板化变得简单，但它当然不仅限于模板化。在严格的内容安全政策下，任何无法直接运行的代码都可以放入沙盒中；事实上，将扩展程序中会正确运行的组件放入沙盒中通常很有用，这样可以将程序的每个部分限制为仅拥有执行所需的最少特权集。2012 年 Google I/O 大会上的 Writing Secure Web Apps and Chrome Extensions 演示提供了一些很好的示例，展示了这些技术的实际运用，值得您花 56 分钟的时间观看。

```
addEventListener
```

**Pattern 2:** 重要提示： 此 API 仅在 ChromeOS 上有效。 说明 使用此 API 向平台公开证书，平台可以使用这些证书进行 TLS 身份验证。 权限 certificateProvider 可用性 Chrome 46 及更高版本 仅限 ChromeOS 概念和用法 使用此 API 向 ChromeOS 公开客户端证书的典型步骤如下： 扩展程序注册了 onCertificatesUpdateRequested 和 onSignatureRequested 事件。 扩展程序在初始化后调用 setCertificates() 以提供初始证书列表。 扩展程序会监控可用证书列表中的更改，并调用 setCertificates() 来通知浏览器有关每项此类更改的信息。 在 TLS 握手期间，浏览器会收到客户端证书请求。对于 onCertificatesUpdateRequested 事件，浏览器会要求扩展程序报告其当前提供的所有证书。 扩展程序使用 setCertificates() 方法报告当前可用的证书。 浏览器将所有可用的证书与远程主机的客户端证书请求进行匹配。系统会在选择对话框中向用户显示匹配项。 用户可以选择证书，从而批准身份验证或中止身份验证。 证书选择对话框。 如果用户中止身份验证或没有证书与请求匹配，则 TLS 客户端身份验证会中止。 否则，如果用户批准使用此扩展程序提供的证书进行身份验证，浏览器会请求扩展程序对数据进行签名，以继续进行 TLS 握手。该请求会以 onSignatureRequested 事件的形式发送。 此事件包含输入数据，声明必须使用哪种算法来生成签名，并引用了此扩展程序报告的证书之一。扩展程序必须使用与所引用证书关联的私钥为指定数据创建签名。创建签名可能需要先添加 DigestInfo 并填充结果，然后再进行实际签名。 扩展程序使用 reportSignature() 方法将签名发送回浏览器。如果无法计算签名，则必须在不带签名的情况下调用该方法。 如果提供了签名，浏览器会完成 TLS 握手。 实际步骤顺序可能会有所不同。例如，如果使用自动选择证书的企业政策，系统就不会要求用户选择证书（请参阅 AutoSelectCertificateForUrls 和面向用户的 Chrome 政策）。 在扩展程序中，这可能类似于以下代码段： function collectAvailableCertificates() { // Return all certificates that this Extension can currently provide. // For example: return [{ certificateChain: [new Uint8Array(...)], supportedAlgorithms: ['RSASSA_PKCS1_v1_5_SHA256'] }]; } // The Extension calls this function every time the currently available list of // certificates changes, and also once after the Extension's initialization. function onAvailableCertificatesChanged() { chrome.certificateProvider.setCertificates({ clientCertificates: collectAvailableCertificates() }); } function handleCertificatesUpdateRequest(request) { // Report the currently available certificates as a response to the request // event. This is important for supporting the case when the Extension is // unable to detect the changes proactively. chrome.certificateProvider.setCertificates({ certificatesRequestId: request.certificatesRequestId, clientCertificates: collectAvailableCertificates() }); } // Returns a private key handle for the given DER-encoded certificate. // |certificate| is an ArrayBuffer. function getPrivateKeyHandle(certificate) {...} // Digests and signs |input| with the given private key. |input| is an // ArrayBuffer. |algorithm| is an Algorithm. // Returns the signature as ArrayBuffer. function signUnhashedData(privateKey, input, algorithm) {...} function handleSignatureRequest(request) { // Look up the handle to the private key of |request.certificate|. const key = getPrivateKeyHandle(request.certificate); if (!key) { // Handle if the key isn't available. console.error('Key for requested certificate no available.'); // Abort the request by reporting the error to the API. chrome.certificateProvider.reportSignature({ signRequestId: request.signRequestId, error: 'GENERAL_ERROR' }); return; } const signature = signUnhashedData(key, request.input, request.algorithm); chrome.certificateProvider.reportSignature({ signRequestId: request.signRequestId, signature: signature }); } chrome.certificateProvider.onCertificatesUpdateRequested.addListener( handleCertificatesUpdateRequest); chrome.certificateProvider.onSignatureRequested.addListener( handleSignatureRequest); 类型 Algorithm Chrome 86 及更高版本 支持的加密签名算法的类型。 枚举 "RSASSA_PKCS1_v1_5_MD5_SHA1" 指定采用 MD5-SHA-1 哈希的 RSASSA PKCS#1 v1.5 签名算法。扩展程序不得预先添加 DigestInfo 前缀，而只能添加 PKCS#1 填充。此算法已被弃用，自版本 109 起，Chrome 将不再请求使用此算法。"RSASSA_PKCS1_v1_5_SHA1" 指定使用 SHA-1 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。"RSASSA_PKCS1_v1_5_SHA256" 指定使用 SHA-256 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。"RSASSA_PKCS1_v1_5_SHA384" 指定使用 SHA-384 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。"RSASSA_PKCS1_v1_5_SHA512" 指定使用 SHA-512 哈希函数的 RSASSA PKCS#1 v1.5 签名算法。“RSASSA_PSS_SHA256” 指定 RSASSA PSS 签名算法，使用 SHA-256 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。"RSASSA_PSS_SHA384" 指定 RSASSA PSS 签名算法，该算法使用 SHA-384 哈希函数、MGF1 掩码生成函数和与哈希大小相同的盐。“RSASSA_PSS_SHA512” 指定 RSASSA PSS 签名算法，该算法使用 SHA-512 哈希函数、MGF1 掩码生成函数以及与哈希大小相同的盐。 CertificateInfo 属性 证书 ArrayBuffer 必须是 X.509 证书的 DER 编码。目前仅支持使用 RSA 密钥的证书。 supportedHashes 哈希[] 必须设置为相应证书支持的所有哈希。此扩展程序只会要求对使用这些哈希算法之一计算出的摘要进行签名。应按哈希偏好程度降序排列。 CertificatesUpdateRequest Chrome 86 及更高版本 属性 certificatesRequestId 数值 要传递给 setCertificates 的请求标识符。 ClientCertificateInfo Chrome 86 及更高版本 属性 certificateChain ArrayBuffer[] 该数组必须包含 X.509 客户端证书的 DER 编码作为其第一个元素。 必须只包含一个证书。 supportedAlgorithms Algorithm[] 相应证书支持的所有算法。系统只会要求扩展程序使用这些算法之一进行签名。 Error Chrome 86 及更高版本 扩展程序可以报告的错误类型。 值 "GENERAL_ERROR" Hash 已弃用。已替换为 Algorithm。 枚举 “MD5_SHA1” 指定 MD5 和 SHA1 哈希算法。“SHA1” 指定 SHA1 哈希算法。“SHA256” 指定 SHA256 哈希处理算法。“SHA384” 指定 SHA384 哈希处理算法。“SHA512” 指定 SHA512 哈希算法。 PinRequestErrorType Chrome 57 及更高版本 可通过 requestPin 函数向用户显示的错误类型。 枚举 “INVALID_PIN” 指定 PIN 码无效。“INVALID_PUK” 指定 PUK 无效。“MAX_ATTEMPTS_EXCEEDED” 指定已超出最大尝试次数。“UNKNOWN_ERROR” 指定错误无法用上述类型表示。 PinRequestType Chrome 57 及更高版本 扩展程序通过 requestPin 函数请求的代码类型。 枚举 “PIN 码” 指定所请求的代码是 PIN 码。“PUK” 指定所请求的代码是 PUK。 PinResponseDetails Chrome 57 及更高版本 属性 userInput 字符串（选填） 用户提供的代码。如果用户关闭了对话框或发生了其他错误，则为空。 ReportSignatureDetails Chrome 86 及更高版本 属性 错误 "GENERAL_ERROR" 可选 生成签名时发生的错误（如果有）。 signRequestId 数值 通过 onSignatureRequested 事件接收到的请求标识符。 签名 ArrayBuffer 可选 成功生成的签名。 RequestPinDetails Chrome 57 及更高版本 属性 attemptsLeft number 可选 剩余尝试次数。提供此信息是为了让任何界面都能向用户显示此信息。Chrome 不会强制执行此操作，而是当 PIN 码请求数超出时，扩展程序应调用 stopPinRequest 并将 errorType 设置为 MAX_ATTEMPTS_EXCEEDED。 errorType PinRequestErrorType 可选 向用户显示的错误模板。如果之前的请求失败，则应设置此参数，以将失败原因通知给用户。 requestType PinRequestType 可选 所请求的验证码类型。默认值为 PIN 码。 signRequestId 数值 Chrome 在 SignRequest 中提供的 ID。 SetCertificatesDetails Chrome 86 及更高版本 属性 certificatesRequestId number 可选 在响应 onCertificatesUpdateRequested 时调用，应包含收到的 certificatesRequestId 值。否则，应取消设置。 clientCertificates ClientCertificateInfo[] 当前可用的客户端证书列表。 错误 "GENERAL_ERROR" 可选 提取证书时发生的错误（如果有）。系统会在适当的时候向用户显示此错误。 SignatureRequest Chrome 86 及更高版本 属性 算法 Algorithm 要使用的签名算法。 证书 ArrayBuffer X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 input 进行签名。 输入 ArrayBuffer 要签名的数据。请注意，数据未经过哈希处理。 signRequestId 数值 要传递给 reportSignature 的请求标识符。 SignRequest 属性 证书 ArrayBuffer X.509 证书的 DER 编码。扩展程序必须使用关联的私钥对 digest 进行签名。 摘要 ArrayBuffer 必须签名的摘要。 哈希 哈希 指用于创建 digest 的哈希算法。 signRequestId 数值 Chrome 57 及更高版本 供扩展程序使用的唯一 ID，如果扩展程序需要调用需要此 ID 的方法（例如 requestPin），则应使用此 ID。 StopPinRequestDetails Chrome 57 及更高版本 属性 errorType PinRequestErrorType 可选 错误模板。如果存在，则会向用户显示。旨在包含因错误而停止流程的原因，例如 MAX_ATTEMPTS_EXCEEDED。 signRequestId 数值 Chrome 在 SignRequest 中提供的 ID。 方法 reportSignature() Chrome 86 及更高版本 chrome.certificateProvider.reportSignature( details: ReportSignatureDetails,): Promise<void> 应作为对 onSignatureRequested 的响应进行调用。 扩展程序必须最终为每个 onSignatureRequested 事件调用此函数；API 实现会在一段时间后停止等待此调用，并在调用此函数时以超时错误进行响应。 参数 详细信息 ReportSignatureDetails 返回 Promise<void> Chrome 96 及更高版本 requestPin() Chrome 57 及更高版本 chrome.certificateProvider.requestPin( details: RequestPinDetails,): Promise<PinResponseDetails | undefined> 向用户请求 PIN 码。一次只能有一个正在进行的请求。在另一个流程正在进行时发出的请求会被拒绝。如果另一个流程正在进行中，扩展程序应负责稍后重试。 参数 详细信息 RequestPinDetails 包含有关所请求对话框的详细信息。 返回 Promise<PinResponseDetails | undefined> Chrome 96 及更高版本 setCertificates() Chrome 86 及更高版本 chrome.certificateProvider.setCertificates( details: SetCertificatesDetails,): Promise<void> 设置要在浏览器中使用的证书列表。 扩展程序应在初始化后以及当前可用证书集发生每次更改时调用此函数。扩展程序还应在每次收到此事件时，调用此函数以响应 onCertificatesUpdateRequested。 参数 详细信息 SetCertificatesDetails 要设置的证书。系统会忽略无效证书。 返回 Promise<void> Chrome 96 及更高版本 stopPinRequest() Chrome 57 及更高版本 chrome.certificateProvider.stopPinRequest( details: StopPinRequestDetails,): Promise<void> 停止由 requestPin 函数启动的 PIN 码请求。 参数 详细信息 StopPinRequestDetails 包含有关停止请求流的原因的详细信息。 返回 Promise<void> Chrome 96 及更高版本 事件 onCertificatesUpdateRequested Chrome 86 及更高版本 chrome.certificateProvider.onCertificatesUpdateRequested.addListener( callback: function,) 如果通过 setCertificates 设置的证书不足，或者浏览器请求更新后的信息，则会触发此事件。扩展程序必须使用更新后的证书列表和收到的 certificatesRequestId 调用 setCertificates。 参数 callback 函数 callback 参数如下所示： (request: CertificatesUpdateRequest) => void request CertificatesUpdateRequest onSignatureRequested Chrome 86 及更高版本 chrome.certificateProvider.onSignatureRequested.addListener( callback: function,) 每次浏览器需要使用此扩展程序通过 setCertificates 提供的证书对消息进行签名时，都会触发此事件。 扩展程序必须使用适当的算法和私钥对来自 request 的输入数据进行签名，并通过使用收到的 signRequestId 调用 reportSignature 来返回签名。 参数 callback 函数 callback 参数如下所示： (request: SignatureRequest) => void request SignatureRequest

```
certificateProvider
```

### Example Code Patterns

**Example 1** (javascript):
```javascript
async function getCurrentTab() {/* ... */}
let tab = await getCurrentTab();

chrome.tabs.executeScript(
  tab.id,
  {
    file: 'content-script.js'
  }
);
```

**Example 2** (javascript):
```javascript
async function getCurrentTab()
let tab = await getCurrentTab();

chrome.scripting.executeScript({
  target: {tabId: tab.id},
  files: ['content-script.js']
});
```

**Example 3** (javascript):
```javascript
chrome.webRequest.onBeforeRequest.addListener((e) => {
    return { cancel: true };
}, { urls: ["https://www.example.com/*"] }, ["blocking"]);
```

**Example 4** (javascript):
```javascript
chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
  chrome.action.onClicked.addListener(handleActionClick);
});
```

**Example 5** (javascript):
```javascript
chrome.action.onClicked.addListener(handleActionClick);

chrome.storage.local.get(["badgeText"], ({ badgeText }) => {
  chrome.action.setBadgeText({ text: badgeText });
});
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **background_scripts.md** - Background Scripts documentation
- **content_scripts.md** - Content Scripts documentation
- **debugging.md** - Debugging documentation
- **getting_started.md** - Getting Started documentation
- **manifest.md** - Manifest documentation
- **other.md** - Other documentation
- **permissions.md** - Permissions documentation
- **popup_ui.md** - Popup Ui documentation
- **storage.md** - Storage documentation
- **web_extensions.md** - Web Extensions documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
Start with the getting_started or tutorials reference files for foundational concepts.

### For Specific Features
Use the appropriate category reference file (api, guides, etc.) for detailed information.

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

### scripts/
Add helper scripts here for common automation tasks.

### assets/
Add templates, boilerplate, or example projects here.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
