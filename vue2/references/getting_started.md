# Vue2 - Getting Started

**Pages:** 1

---

## 安装 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/installation.html

**Contents:**
- 安装
  - 兼容性
  - 语义化版本控制
  - 更新日志
- Vue Devtools
- 直接用 <script> 引入
  - CDN
- NPM
- 命令行工具 (CLI)
- 对不同构建版本的解释

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue 不支持 IE8 及以下版本，因为 Vue 使用了 IE8 无法模拟的 ECMAScript 5 特性。但它支持所有兼容 ECMAScript 5 的浏览器。

Vue 在其所有项目中公布的功能和行为都遵循语义化版本控制。对于未公布的或内部暴露的行为，其变更会描述在发布说明中。

在使用 Vue 时，我们推荐在你的浏览器上安装 Vue Devtools。它允许你在一个更友好的界面中审查和调试 Vue 应用。

直接下载并用 <script> 标签引入，Vue 会被注册为一个全局变量。

在开发环境下不要使用压缩版本，不然你就失去了所有常见错误相关的警告!

对于制作原型或学习，你可以这样使用最新版本：

对于生产环境，我们推荐链接到一个明确的版本号和构建文件，以避免新版本造成的不可预期的破坏：

如果你使用原生 ES Modules，这里也有一个兼容 ES Module 的构建文件：

你可以在 cdn.jsdelivr.net/npm/vue 浏览 NPM 包的源代码。

Vue 也可以在 unpkg 和 cdnjs 上获取 (cdnjs 的版本更新可能略滞后)。

请确认了解不同构建版本并在你发布的站点中使用生产环境版本，把 vue.js 换成 vue.min.js。这是一个更小的构建，可以带来比开发环境下更快的速度体验。

在用 Vue 构建大型应用时推荐使用 NPM 安装[1]。NPM 能很好地和诸如 webpack 或 Browserify 模块打包器配合使用。同时 Vue 也提供配套工具来开发单文件组件。

Vue 提供了一个官方的 CLI，为单页面应用 (SPA) 快速搭建繁杂的脚手架。它为现代前端工作流提供了开箱即用的构建设置。只需要几分钟的时间就可以运行起来并带有热重载、保存时 lint 校验，以及生产环境可用的构建版本。更多详情可查阅 Vue CLI 的文档。

CLI 工具假定用户对 Node.js 和相关构建工具有一定程度的了解。如果你是新手，我们强烈建议先在不用构建工具的情况下通读指南，在熟悉 Vue 本身之后再使用 CLI。

在 NPM 包的 dist/ 目录你将会找到很多不同的 Vue.js 构建版本。这里列出了它们之间的差别：

编译器：用来将模板字符串编译成为 JavaScript 渲染函数的代码。

运行时：用来创建 Vue 实例、渲染并处理虚拟 DOM 等的代码。基本上就是除去编译器的其它一切。

UMD：UMD 版本可以通过 <script> 标签直接用在浏览器中。jsDelivr CDN 的 https://cdn.jsdelivr.net/npm/vue@2.7.16 默认文件就是运行时 + 编译器的 UMD 版本 (vue.js)。

CommonJS：CommonJS 版本用来配合老的打包工具比如 Browserify 或 webpack 1。这些打包工具的默认文件 (pkg.main) 是只包含运行时的 CommonJS 版本 (vue.runtime.common.js)。

ES Module：从 2.6 开始 Vue 会提供两个 ES Modules (ESM) 构建文件：

为打包工具提供的 ESM：为诸如 webpack 2 或 Rollup 提供的现代打包工具。ESM 格式被设计为可以被静态分析，所以打包工具可以利用这一点来进行“tree-shaking”并将用不到的代码排除出最终的包。为这些打包工具提供的默认文件 (pkg.module) 是只有运行时的 ES Module 构建 (vue.runtime.esm.js)。

为浏览器提供的 ESM (2.6+)：用于在现代浏览器中通过 <script type="module"> 直接导入。

如果你需要在客户端编译模板 (比如传入一个字符串给 template 选项，或挂载到一个元素上并以其 DOM 内部的 HTML 作为模板)，就将需要加上编译器，即完整版：

当使用 vue-loader 或 vueify 的时候，*.vue 文件内部的模板会在构建时预编译成 JavaScript。你在最终打好的包里实际上是不需要编译器的，所以只用运行时版本即可。

因为运行时版本相比完整版体积要小大约 30%，所以应该尽可能使用这个版本。如果你仍然希望使用完整版，则需要在打包工具里配置一个别名：

添加到你项目的 package.json：

在你项目的 package.json 中添加：

对于 UMD 版本来说，开发环境/生产环境模式是硬编码好的：开发环境下用未压缩的代码，生产环境下使用压缩后的代码。

CommonJS 和 ES Module 版本是用于打包工具的，因此我们不提供压缩后的版本。你需要自行将最终的包进行压缩。

CommonJS 和 ES Module 版本同时保留原始的 process.env.NODE_ENV 检测，以决定它们应该运行在什么模式下。你应该使用适当的打包工具配置来替换这些环境变量以便控制 Vue 所运行的模式。把 process.env.NODE_ENV 替换为字符串字面量同时可以让 UglifyJS 之类的压缩工具完全丢掉仅供开发环境的代码块，以减少最终的文件尺寸。

在 webpack 4+ 中，你可以使用 mode 选项：

但是在 webpack 3 及其更低版本中，你需要使用 DefinePlugin：

使用 rollup-plugin-replace：

为你的包应用一次全局的 envify 转换。

有些环境，如 Google Chrome Apps，会强制应用内容安全策略 (CSP)，不能使用 new Function() 对表达式求值。这时可以用 CSP 兼容版本。完整版本依赖于该功能来编译模板，所以无法在这些环境下使用。

另一方面，运行时版本则是完全兼容 CSP 的。当通过 webpack + vue-loader 或者 Browserify + vueify 构建时，模板将被预编译为 render 函数，可以在 CSP 环境中完美运行。

重要：GitHub 仓库的 /dist 文件夹只有在新版本发布时才会提交。如果想要使用 GitHub 上 Vue 最新的源码，你需要自己构建！

所有 UMD 版本都可以直接用作 AMD 模块。

译者注[1] 对于中国大陆用户，建议将 NPM 源设置为国内的镜像，可以大幅提升安装速度。

**Examples:**

Example 1 (unknown):
```unknown
<script src="https://cdn.jsdelivr.net/npm/vue@2.7.16/dist/vue.js"></script>
```

Example 2 (unknown):
```unknown
<script src="https://cdn.jsdelivr.net/npm/vue@2.7.16"></script>
```

Example 3 (python):
```python
<script type="module">  import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.7.16/dist/vue.esm.browser.js'</script>
```

Example 4 (unknown):
```unknown
# 最新稳定版$ npm install vue@^2
```

---
