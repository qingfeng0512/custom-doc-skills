# Vue2 - Other

**Pages:** 20

---

## 测试 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/testing.html

**Contents:**
- 测试
- 介绍
- 单元测试
  - 介绍
  - 选择框架
    - 一流的错误报告
    - 活跃的社区和团队
  - 框架
    - Jest
    - Mocha

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

当构建可靠的应用时，测试在个人或团队构建新特性、重构代码、修复 bug 等工作中扮演了关键的角色。尽管测试的流派有很多，它们在 web 应用这个领域里主要有三大类：

本章节致力于引导大家了解测试的生态系统并为 Vue 应用或组件库选择适合的工具。

单元测试允许你将独立单元的代码进行隔离测试，其目的是为开发者提供对代码的信心。通过编写细致且有意义的测试，你能够有信心在构建新特性或重构已有代码的同时，保持应用的功能和稳定。

为一个 Vue 应用做单元测试并没有和为其它类型的应用做测试有什么明显的区别。

因为单元测试的建议通常是框架无关的，所以下面只是当你在评估应用的单元测试工具时需要的一些基本指引。

当测试失败时，提供有用的错误信息对于单元测试框架来说至关重要。这是断言库应尽的职责。一个具有高质量错误信息的断言能够最小化调试问题所需的时间。除了简单地告诉你什么测试失败了，断言库还应额外提供上下文以及测试失败的原因，例如预期结果 vs. 实际得到的结果。

一些诸如 Jest 这样的单元测试框架会包含断言库。另一些诸如 Mocha 需要你单独安装断言库 (通常会用 Chai)。

因为主流的单元测试框架都是开源的，所以对于一些旨在长期维护其测试且确保项目本身保持活跃的团队来说，拥有一个活跃的社区是至关重要的。额外的好处是，在任何时候遇到问题时，一个活跃的社区会为你提供更多的支持。

尽管生态系统里有很多工具，这里我们列出一些在 Vue 生态系统中常用的单元测试工具。

Jest 是一个专注于简易性的 JavaScript 测试框架。一个其独特的功能是可以为测试生成快照 (snapshot)，以提供另一种验证应用单元的方法。

Mocha 是一个专注于灵活性的 JavaScript 测试框架。因为其灵活性，它允许你选择不同的库来满足诸如侦听 (如 Sinon) 和断言 (如 Chai) 等其它常见的功能。另一个 Mocha 独特的功能是它不止可以在 Node.js 里运行测试，还可以在浏览器里运行测试。

测试大多数 Vue 组件时都必须将它们挂载到 DOM (虚拟或真实) 上，才能完全断言它们正在工作。这是另一个与框架无关的概念。因此组件测试框架的诞生，是为了让用户能够以可靠的方式完成这项工作，同时还提供了 Vue 特有的诸如对 Vuex、Vue Router 和其他 Vue 插件的集成的便利性。

以下章节提供了在评估最适合你的应用的组件测试框架时需要记住的事项。

毋容置疑，最重要的标准之一就是组件测试库应该尽可能与 Vue 生态系统兼容。虽然这看起来很全面，但需要记住的一些关键集成领域包括单文件组件 (SFC)、Vuex、Vue Router 以及应用所依赖的任何其他特定于 Vue 的插件。

当测试失败时，提供有用的错误日志以最小化调试问题所需的时间对于组件测试框架来说至关重要。除了简单地告诉你什么测试失败了，他们还应额外提供上下文以及测试失败的原因，例如预期结果 vs. 实际得到的结果。

Vue Testing Library 是一组专注于测试组件而不依赖实现细节的工具。由于在设计时就充分考虑了可访问性，它采用的方案也使重构变得轻而易举。

它的指导原则是，与软件使用方式相似的测试越多，它们提供的可信度就越高。

Vue Test Utils 是官方的偏底层的组件测试库，它是为用户提供对 Vue 特定 API 的访问而编写的。如果你对测试 Vue 应用不熟悉，我们建议你使用 Vue Testing Library，它是 Vue Test Utils 的抽象。

虽然单元测试为开发者提供了一定程度的信心，但是单元测试和组件测试在部署到生产环境时提供应用整体覆盖的能力是有限的。因此，端到端测试可以说从应用最重要的方面进行测试覆盖：当用户实际使用应用时会发生什么。

换句话说，端到端测试验证应用中的所有层。这不仅包括你的前端代码，还包括所有相关的后端服务和基础设施，它们更能代表你的用户所处的环境。通过测试用户操作如何影响应用，端到端测试通常是提高应用是否正常运行的信心的关键。

虽然 web 上的端到端测试因不可信赖 (片面的) 测试和减慢开发过程而得到负面的声誉，但现代端到端工具在创建更可靠的、交互的和实用的测试方面取得了长足进步。在选择端到端测试框架时，以下章节在你为应用选择测试框架时提供了一些指导。

端到端测试的一个主要优点是它能够跨多个浏览器测试应用。尽管 100% 的跨浏览器覆盖看上去很诱人，但需要注意的是，因为持续运行这些跨浏览器测试需要额外的时间和机器消耗，它会降低团队的资源回报。因此，在选择应用需要的跨浏览器测试数量时，必须注意这种权衡。

针对 E2E 浏览器特定问题的一个最新进展是，针对不常用的浏览器 (如：< IE11、旧版 Safari 等) 使用应用监视和错误报告工具 (如：Sentry、LogRocket 等)。

端到端测试和开发的主要问题之一是运行整个套件需要很长时间。通常，这只在持续集成和部署 (CI/CD) 管道中完成。现代的端到端测试框架通过添加类似并行化的特性来帮助解决这个问题，这使得 CI/CD 管道的运行速度通常比以前快。此外，在本地开发时，有选择地为正在处理的页面运行单个测试的能力，同时还提供测试的热重载，将有助于提高开发者的工作流程和工作效率。

虽然开发者传统上依赖于在终端窗口中扫描日志来帮助确定测试中出了什么问题，但现代端到端测试框架允许开发者利用他们已经熟悉的工具，例如浏览器开发工具。

虽然生态系统中有许多工具，但以下是一些 Vue.js 生态系统中常用的端到端测试框架。

Cypress.io 是一个测试框架，旨在通过使开发者能够可靠地测试他们的应用，同时提供一流的开发者体验，来提高开发者的生产率。

Nightwatch.js 是一个端到端测试框架，可用于测试 web 应用和网站，以及 Node.js 单元测试和集成测试。

Puppeteer 是一个 Node.js 库，它提供高阶 API 来控制浏览器，并可以与其他测试运行程序 (例如 Jest) 配对来测试应用。

TestCafe 是一个基于端到端的 Node.js 框架，旨在提供简单的设置，以便开发者能够专注于创建易于编写和可靠的测试。

---

## 组件基础 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components.html

**Contents:**
- 组件基础
- 基本示例
- 组件的复用
  - data 必须是一个函数
- 组件的组织
- 通过 Prop 向子组件传递数据
- 单个根元素
- 监听子组件事件
  - 使用事件抛出一个值
  - 在组件上使用 v-model

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

组件是可复用的 Vue 实例，且带有一个名字：在这个例子中是 <button-counter>。我们可以在一个通过 new Vue 创建的 Vue 根实例中，把这个组件作为自定义元素来使用：

因为组件是可复用的 Vue 实例，所以它们与 new Vue 接收相同的选项，例如 data、computed、watch、methods 以及生命周期钩子等。仅有的例外是像 el 这样根实例特有的选项。

注意当点击按钮时，每个组件都会各自独立维护它的 count。因为你每用一次组件，就会有一个它的新实例被创建。

当我们定义这个 <button-counter> 组件时，你可能会发现它的 data 并不是像这样直接提供一个对象：

取而代之的是，一个组件的 data 选项必须是一个函数，因此每个实例可以维护一份被返回对象的独立的拷贝：

如果 Vue 没有这条规则，点击一个按钮就可能会像如下代码一样影响到其它所有实例：

通常一个应用会以一棵嵌套的组件树的形式来组织：

例如，你可能会有页头、侧边栏、内容区等组件，每个组件又包含了其它的像导航链接、博文之类的组件。

为了能在模板中使用，这些组件必须先注册以便 Vue 能够识别。这里有两种组件的注册类型：全局注册和局部注册。至此，我们的组件都只是通过 Vue.component 全局注册的：

全局注册的组件可以用在其被注册之后的任何 (通过 new Vue) 新创建的 Vue 根实例，也包括其组件树中的所有子组件的模板中。

到目前为止，关于组件注册你需要了解的就这些了，如果你阅读完本页内容并掌握了它的内容，我们会推荐你再回来把组件注册读完。

早些时候，我们提到了创建一个博文组件的事情。问题是如果你不能向这个组件传递某一篇博文的标题或内容之类的我们想展示的数据的话，它是没有办法使用的。这也正是 prop 的由来。

Prop 是你可以在组件上注册的一些自定义 attribute。当一个值传递给一个 prop attribute 的时候，它就变成了那个组件实例的一个 property。为了给博文组件传递一个标题，我们可以用一个 props 选项将其包含在该组件可接受的 prop 列表中：

一个组件默认可以拥有任意数量的 prop，任何值都可以传递给任何 prop。在上述模板中，你会发现我们能够在组件实例中访问这个值，就像访问 data 中的值一样。

一个 prop 被注册之后，你就可以像这样把数据作为一个自定义 attribute 传递进来：

然而在一个典型的应用中，你可能在 data 里有一个博文的数组：

如上所示，你会发现我们可以使用 v-bind 来动态传递 prop。这在你一开始不清楚要渲染的具体内容，比如从一个 API 获取博文列表的时候，是非常有用的。

到目前为止，关于 prop 你需要了解的大概就这些了，如果你阅读完本页内容并掌握了它的内容，我们会推荐你再回来把 prop 读完。

当构建一个 <blog-post> 组件时，你的模板最终会包含的东西远不止一个标题：

然而如果你在模板中尝试这样写，Vue 会显示一个错误，并解释道 every component must have a single root element (每个组件必须只有一个根元素)。你可以将模板的内容包裹在一个父元素内，来修复这个问题，例如：

看起来当组件变得越来越复杂的时候，我们的博文不只需要标题和内容，还需要发布日期、评论等等。为每个相关的信息定义一个 prop 会变得很麻烦：

所以是时候重构一下这个 <blog-post> 组件了，让它变成接受一个单独的 post prop：

上述的这个和一些接下来的示例使用了 JavaScript 的模板字符串来让多行的模板更易读。它们在 IE 下并没有被支持，所以如果你需要在不 (经过 Babel 或 TypeScript 之类的工具) 编译的情况下支持 IE，请使用折行转义字符取而代之。

现在，不论何时为 post 对象添加一个新的 property，它都会自动地在 <blog-post> 内可用。

在我们开发 <blog-post> 组件时，它的一些功能可能要求我们和父级组件进行沟通。例如我们可能会引入一个辅助功能来放大博文的字号，同时让页面的其它部分保持默认的字号。

在其父组件中，我们可以通过添加一个 postFontSize 数据 property 来支持这个功能：

现在我们在每篇博文正文之前添加一个按钮来放大字号：

当点击这个按钮时，我们需要告诉父级组件放大所有博文的文本。幸好 Vue 实例提供了一个自定义事件的系统来解决这个问题。父级组件可以像处理 native DOM 事件一样通过 v-on 监听子组件实例的任意事件：

同时子组件可以通过调用内建的 $emit 方法并传入事件名称来触发一个事件：

有了这个 v-on:enlarge-text="postFontSize += 0.1" 监听器，父级组件就会接收该事件并更新 postFontSize 的值。

有的时候用一个事件来抛出一个特定的值是非常有用的。例如我们可能想让 <blog-post> 组件决定它的文本要放大多少。这时可以使用 $emit 的第二个参数来提供这个值：

然后当在父级组件监听这个事件的时候，我们可以通过 $event 访问到被抛出的这个值：

那么这个值将会作为第一个参数传入这个方法：

自定义事件也可以用于创建支持 v-model 的自定义输入组件。记住：

当用在组件上时，v-model 则会这样：

为了让它正常工作，这个组件内的 <input> 必须：

现在 v-model 就应该可以在这个组件上完美地工作起来了：

到目前为止，关于组件自定义事件你需要了解的大概就这些了，如果你阅读完本页内容并掌握了它的内容，我们会推荐你再回来把自定义事件读完。

和 HTML 元素一样，我们经常需要向一个组件传递内容，像这样：

幸好，Vue 自定义的 <slot> 元素让这变得非常简单：

如你所见，我们只要在需要的地方加入插槽就行了——就这么简单！

到目前为止，关于插槽你需要了解的大概就这些了，如果你阅读完本页内容并掌握了它的内容，我们会推荐你再回来把插槽读完。

有的时候，在不同组件之间进行动态切换是非常有用的，比如在一个多标签的界面里：

上述内容可以通过 Vue 的 <component> 元素加一个特殊的 is attribute 来实现：

在上述示例中，currentTabComponent 可以包括

你可以在这里查阅并体验完整的代码，或在这个版本了解绑定组件选项对象，而不是已注册组件名的示例。

请留意，这个 attribute 可以用于常规 HTML 元素，但这些元素将被视为组件，这意味着所有的 attribute 都会作为 DOM attribute 被绑定。对于像 value 这样的 property，若想让其如预期般工作，你需要使用 .prop 修饰器。

到目前为止，关于动态组件你需要了解的大概就这些了，如果你阅读完本页内容并掌握了它的内容，我们会推荐你再回来把动态和异步组件读完。

有些 HTML 元素，诸如 <ul>、<ol>、<table> 和 <select>，对于哪些元素可以出现在其内部是有严格限制的。而有些元素，诸如 <li>、<tr> 和 <option>，只能出现在其它某些特定的元素内部。

这会导致我们使用这些有约束条件的元素时遇到一些问题。例如：

这个自定义组件 <blog-post-row> 会被作为无效的内容提升到外部，并导致最终渲染结果出错。幸好这个特殊的 is attribute 给了我们一个变通的办法：

需要注意的是如果我们从以下来源使用模板的话，这条限制是不存在的：

到这里，你需要了解的解析 DOM 模板时的注意事项——实际上也是 Vue 的全部必要内容，大概就是这些了。恭喜你！接下来还有很多东西要去学习，不过首先，我们推荐你先休息一下，试用一下 Vue，自己随意做些好玩的东西。

如果你感觉已经掌握了这些知识，我们推荐你再回来把完整的组件指南，包括侧边栏中组件深入章节的所有页面读完。

**Examples:**

Example 1 (unknown):
```unknown
// 定义一个名为 button-counter 的新组件Vue.component('button-counter', {  data: function () {    return {      count: 0    }  },  template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'})
```

Example 2 (unknown):
```unknown
<div id="components-demo">  <button-counter></button-counter></div>
```

Example 3 (unknown):
```unknown
new Vue({ el: '#components-demo' })
```

Example 4 (unknown):
```unknown
<div id="components-demo">  <button-counter></button-counter>  <button-counter></button-counter>  <button-counter></button-counter></div>
```

---

## 处理边界情况 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-edge-cases.html

**Contents:**
- 处理边界情况
- 访问元素 & 组件
  - 访问根实例
  - 访问父级组件实例
  - 访问子组件实例或子元素
  - 依赖注入
- 程序化的事件侦听器
- 循环引用
  - 递归组件
  - 组件之间的循环引用

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

这里记录的都是和处理边界情况有关的功能，即一些需要对 Vue 的规则做一些小调整的特殊情况。不过注意这些功能都是有劣势或危险的场景的。我们会在每个案例中注明，所以当你使用每个功能的时候请稍加留意。

在绝大多数情况下，我们最好不要触达另一个组件实例内部或手动操作 DOM 元素。不过也确实在一些情况下做这些事情是合适的。

在每个 new Vue 实例的子组件中，其根实例可以通过 $root property 进行访问。例如，在这个根实例中：

所有的子组件都可以将这个实例作为一个全局 store 来访问或使用。

对于 demo 或非常小型的有少量组件的应用来说这是很方便的。不过这个模式扩展到中大型应用来说就不然了。因此在绝大多数情况下，我们强烈推荐使用 Vuex 来管理应用的状态。

和 $root 类似，$parent property 可以用来从一个子组件访问父组件的实例。它提供了一种机会，可以在后期随时触达父级组件，以替代将数据以 prop 的方式传入子组件的方式。

在绝大多数情况下，触达父级组件会使得你的应用更难调试和理解，尤其是当你变更了父级组件的数据的时候。当我们稍后回看那个组件的时候，很难找出那个变更是从哪里发起的。

另外在一些可能适当的时候，你需要特别地共享一些组件库。举个例子，在和 JavaScript API 进行交互而不渲染 HTML 的抽象组件内，诸如这些假设性的 Google 地图组件一样：

这个 <google-map> 组件可以定义一个 map property，所有的子组件都需要访问它。在这种情况下 <google-map-markers> 可能想要通过类似 this.$parent.getMap 的方式访问那个地图，以便为其添加一组标记。你可以在这里查阅这种模式。

请留意，尽管如此，通过这种模式构建出来的那个组件的内部仍然是容易出现问题的。比如，设想一下我们添加一个新的 <google-map-region> 组件，当 <google-map-markers> 在其内部出现的时候，只会渲染那个区域内的标记：

那么在 <google-map-markers> 内部你可能发现自己需要一些类似这样的 hack：

很快它就会失控。这也是我们针对需要向任意更深层级的组件提供上下文信息时推荐依赖注入的原因。

尽管存在 prop 和事件，有的时候你仍可能需要在 JavaScript 里直接访问一个子组件。为了达到这个目的，你可以通过 ref 这个 attribute 为子组件赋予一个 ID 引用。例如：

现在在你已经定义了这个 ref 的组件里，你可以使用：

来访问这个 <base-input> 实例，以便不时之需。比如程序化地从一个父级组件聚焦这个输入框。在刚才那个例子中，该 <base-input> 组件也可以使用一个类似的 ref 提供对内部这个指定元素的访问，例如：

这样就允许父级组件通过下面的代码聚焦 <base-input> 里的输入框：

当 ref 和 v-for 一起使用的时候，你得到的 ref 将会是一个包含了对应数据源的这些子组件的数组。

$refs 只会在组件渲染完成之后生效，并且它们不是响应式的。这仅作为一个用于直接操作子组件的“逃生舱”——你应该避免在模板或计算属性中访问 $refs。

在此之前，在我们描述访问父级组件实例的时候，展示过一个类似这样的例子：

在这个组件里，所有 <google-map> 的后代都需要访问一个 getMap 方法，以便知道要跟哪个地图进行交互。不幸的是，使用 $parent property 无法很好的扩展到更深层级的嵌套组件上。这也是依赖注入的用武之地，它用到了两个新的实例选项：provide 和 inject。

provide 选项允许我们指定我们想要提供给后代组件的数据/方法。在这个例子中，就是 <google-map> 内部的 getMap 方法：

然后在任何后代组件里，我们都可以使用 inject 选项来接收指定的我们想要添加在这个实例上的 property：

你可以在这里看到完整的示例。相比 $parent 来说，这个用法可以让我们在任意后代组件中访问 getMap，而不需要暴露整个 <google-map> 实例。这允许我们更好的持续研发该组件，而不需要担心我们可能会改变/移除一些子组件依赖的东西。同时这些组件之间的接口是始终明确定义的，就和 props 一样。

实际上，你可以把依赖注入看作一部分“大范围有效的 prop”，除了：

然而，依赖注入还是有负面影响的。它将你应用程序中的组件与它们当前的组织方式耦合起来，使重构变得更加困难。同时所提供的 property 是非响应式的。这是出于设计的考虑，因为使用它们来创建一个中心化规模化的数据跟使用 $root做这件事都是不够好的。如果你想要共享的这个 property 是你的应用特有的，而不是通用化的，或者如果你想在祖先组件中更新所提供的数据，那么这意味着你可能需要换用一个像 Vuex 这样真正的状态管理方案了。

你可以在 API 参考文档学习更多关于依赖注入的知识。

现在，你已经知道了 $emit 的用法，它可以被 v-on 侦听，但是 Vue 实例同时在其事件接口中提供了其它的方法。我们可以：

你通常不会用到这些，但是当你需要在一个组件实例上手动侦听事件时，它们是派得上用场的。它们也可以用于代码组织工具。例如，你可能经常看到这种集成一个第三方库的模式：

你应该通过一个程序化的侦听器解决这两个问题：

使用了这个策略，我甚至可以让多个输入框元素同时使用不同的 Pikaday，每个新的实例都程序化地在后期清理它自己：

查阅这个示例可以了解到完整的代码。注意，即便如此，如果你发现自己不得不在单个组件里做很多建立和清理的工作，最好的方式通常还是创建更多的模块化组件。在这个例子中，我们推荐创建一个可复用的 <input-datepicker> 组件。

想了解更多程序化侦听器的内容，请查阅实例方法 / 事件相关的 API。

注意 Vue 的事件系统不同于浏览器的 EventTarget API。尽管它们工作起来是相似的，但是 $emit、$on, 和 $off 并不是 dispatchEvent、addEventListener 和 removeEventListener 的别名。

组件是可以在它们自己的模板中调用自身的。不过它们只能通过 name 选项来做这件事：

当你使用 Vue.component 全局注册一个组件时，这个全局的 ID 会自动设置为该组件的 name 选项。

类似上述的组件将会导致“max stack size exceeded”错误，所以请确保递归调用是条件性的 (例如使用一个最终会得到 false 的 v-if)。

假设你需要构建一个文件目录树，像访达或资源管理器那样的。你可能有一个 <tree-folder> 组件，模板是这样的：

还有一个 <tree-folder-contents> 组件，模板是这样的：

当你仔细观察的时候，你会发现这些组件在渲染树中互为对方的后代和祖先——一个悖论！当通过 Vue.component 全局注册组件的时候，这个悖论会被自动解开。如果你是这样做的，那么你可以跳过这里。

然而，如果你使用一个模块系统依赖/导入组件，例如通过 webpack 或 Browserify，你会遇到一个错误：

为了解释这里发生了什么，我们先把两个组件称为 A 和 B。模块系统发现它需要 A，但是首先 A 依赖 B，但是 B 又依赖 A，但是 A 又依赖 B，如此往复。这变成了一个循环，不知道如何不经过其中一个组件而完全解析出另一个组件。为了解决这个问题，我们需要给模块系统一个点，在那里“A 反正是需要 B 的，但是我们不需要先解析 B。”

在我们的例子中，把 <tree-folder> 组件设为了那个点。我们知道那个产生悖论的子组件是 <tree-folder-contents> 组件，所以我们会等到生命周期钩子 beforeCreate 时去注册它：

或者，在本地注册组件的时候，你可以使用 webpack 的异步 import：

当 inline-template 这个特殊的 attribute 出现在一个子组件上时，这个组件将会使用其里面的内容作为模板，而不是将其作为被分发的内容。这使得模板的撰写工作更加灵活。

内联模板需要定义在 Vue 所属的 DOM 元素内。

不过，inline-template 会让模板的作用域变得更加难以理解。所以作为最佳实践，请在组件内优先选择 template 选项或 .vue 文件里的一个 <template> 元素来定义模板。

另一个定义模板的方式是在一个 <script> 元素中，并为其带上 text/x-template 的类型，然后通过一个 id 将模板引用过去。例如：

x-template 需要定义在 Vue 所属的 DOM 元素外。

这些可以用于模板特别大的 demo 或极小型的应用，但是其它情况下请避免使用，因为这会将模板和该组件的其它定义分离开。

感谢 Vue 的响应式系统，它始终知道何时进行更新 (如果你用对了的话)。不过还是有一些边界情况，你想要强制更新，尽管表面上看响应式的数据没有发生改变。也有一些情况是你想阻止不必要的更新。

如果你发现你自己需要在 Vue 中做一次强制更新，99.9% 的情况，是你在某个地方做错了事。

你可能还没有留意到数组或对象的变更检测注意事项，或者你可能依赖了一个未被 Vue 的响应式系统追踪的状态。

然而，如果你已经做到了上述的事项仍然发现在极少数的情况下需要手动强制更新，那么你可以通过 $forceUpdate 来做这件事。

渲染普通的 HTML 元素在 Vue 中是非常快速的，但有的时候你可能有一个组件，这个组件包含了大量静态内容。在这种情况下，你可以在根元素上添加 v-once attribute 以确保这些内容只计算一次然后缓存起来，就像这样：

再说一次，试着不要过度使用这个模式。当你需要渲染大量静态内容时，极少数的情况下它会给你带来便利，除非你非常留意渲染变慢了，不然它完全是没有必要的——再加上它在后期会带来很多困惑。例如，设想另一个开发者并不熟悉 v-once 或漏看了它在模板中，他们可能会花很多个小时去找出模板为什么无法正确更新。

**Examples:**

Example 1 (unknown):
```unknown
// Vue 根实例new Vue({  data: {    foo: 1  },  computed: {    bar: function () { /* ... */ }  },  methods: {    baz: function () { /* ... */ }  }})
```

Example 2 (unknown):
```unknown
// 获取根组件的数据this.$root.foo// 写入根组件的数据this.$root.foo = 2// 访问根组件的计算属性this.$root.bar// 调用根组件的方法this.$root.baz()
```

Example 3 (unknown):
```unknown
<google-map>  <google-map-markers v-bind:places="iceCreamShops"></google-map-markers></google-map>
```

Example 4 (unknown):
```unknown
<google-map>  <google-map-region v-bind:shape="cityBoundaries">    <google-map-markers v-bind:places="iceCreamShops"></google-map-markers>  </google-map-region></google-map>
```

---

## 生产环境部署 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/deployment.html

**Contents:**
- 生产环境部署
- 开启生产环境模式
  - 不使用构建工具
  - 使用构建工具
    - webpack
    - Browserify
    - Rollup
- 模板预编译
- 提取组件的 CSS
- 跟踪运行时错误

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

以下大多数内容在你使用 Vue CLI 时都是默认开启的。该章节仅跟你自定义的构建设置有关。

开发环境下，Vue 会提供很多警告来帮你对付常见的错误与陷阱。而在生产环境下，这些警告语句却没有用，反而会增加应用的体积。此外，有些警告检查还有一些小的运行时开销，这在生产环境模式下是可以避免的。

如果用 Vue 完整独立版本，即直接用 <script> 元素引入 Vue 而不提前进行构建，请记得在生产环境下使用压缩后的版本 (vue.min.js)。两种版本都可以在安装指导中找到。

当使用 webpack 或 Browserify 类似的构建工具时，Vue 源码会根据 process.env.NODE_ENV 决定是否启用生产环境模式，默认情况为开发环境模式。在 webpack 与 Browserify 中都有方法来覆盖此变量，以启用 Vue 的生产环境模式，同时在构建过程中警告语句也会被压缩工具去除。所有这些在 vue-cli 模板中都预先配置好了，但了解一下怎样配置会更好。

在 webpack 4+ 中，你可以使用 mode 选项：

但是在 webpack 3 及其更低版本中，你需要使用 DefinePlugin：

或者配合 Grunt 和 grunt-browserify 使用 envify：

使用 @rollup/plugin-replace：

当使用 DOM 内模板或 JavaScript 内的字符串模板时，模板会在运行时被编译为渲染函数。通常情况下这个过程已经足够快了，但对性能敏感的应用还是最好避免这种用法。

预编译模板最简单的方式就是使用单文件组件——相关的构建设置会自动把预编译处理好，所以构建好的代码已经包含了编译出来的渲染函数而不是原始的模板字符串。

如果你使用 webpack，并且喜欢分离 JavaScript 和模板文件，你可以使用 vue-template-loader，它也可以在构建过程中把模板文件转换成为 JavaScript 渲染函数。

当使用单文件组件时，组件内的 CSS 会以 <style> 标签的方式通过 JavaScript 动态注入。这有一些小小的运行时开销，如果你使用服务端渲染，这会导致一段“无样式内容闪烁 (fouc)”。将所有组件的 CSS 提取到同一个文件可以避免这个问题，也会让 CSS 更好地进行压缩和缓存。

如果在组件渲染时出现运行错误，错误将会被传递至全局 Vue.config.errorHandler 配置函数 (如果已设置)。利用这个钩子函数来配合错误跟踪服务是个不错的主意。比如 Sentry，它为 Vue 提供了官方集成。

**Examples:**

Example 1 (unknown):
```unknown
module.exports = {  mode: 'production'}
```

Example 2 (unknown):
```unknown
var webpack = require('webpack')module.exports = {  // ...  plugins: [    // ...    new webpack.DefinePlugin({      'process.env.NODE_ENV': JSON.stringify('production')    })  ]}
```

Example 3 (unknown):
```unknown
NODE_ENV=production browserify -g envify -e main.js | uglifyjs -c -m > build.js
```

Example 4 (unknown):
```unknown
// 使用 envify 自定义模块指定环境变量var envify = require('envify/custom')browserify(browserifyOptions)  .transform(vueify)  .transform(    // 必填项，以处理 node_modules 里的文件    { global: true },    envify({ NODE_ENV: 'production' })  )  .bundle()
```

---

## 进入/离开 & 列表过渡 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/transitions.html

**Contents:**
- 进入/离开 & 列表过渡
- 概述
- 单元素/组件的过渡
  - 过渡的类名
  - CSS 过渡
  - CSS 动画
  - 自定义过渡的类名
  - 同时使用过渡和动画
  - 显性的过渡持续时间
  - JavaScript 钩子

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue 在插入、更新或者移除 DOM 时，提供多种不同方式的应用过渡效果。包括以下工具：

在这里，我们只会讲到进入、离开和列表的过渡，你也可以看下一节的管理过渡状态。

Vue 提供了 transition 的封装组件，在下列情形中，可以给任何元素和组件添加进入/离开过渡

当插入或删除包含在 transition 组件中的元素时，Vue 将会做以下处理：

自动嗅探目标元素是否应用了 CSS 过渡或动画，如果是，在恰当的时机添加/删除 CSS 类名。

如果过渡组件提供了 JavaScript 钩子函数，这些钩子函数将在恰当的时机被调用。

如果没有找到 JavaScript 钩子并且也没有检测到 CSS 过渡/动画，DOM 操作 (插入/删除) 在下一帧中立即执行。(注意：此指浏览器逐帧动画机制，和 Vue 的 nextTick 概念不同)

在进入/离开的过渡中，会有 6 个 class 切换。

v-enter：定义进入过渡的开始状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。

v-enter-active：定义进入过渡生效时的状态。在整个进入过渡的阶段中应用，在元素被插入之前生效，在过渡/动画完成之后移除。这个类可以被用来定义进入过渡的过程时间，延迟和曲线函数。

v-enter-to：2.1.8 版及以上定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 v-enter 被移除)，在过渡/动画完成之后移除。

v-leave：定义离开过渡的开始状态。在离开过渡被触发时立刻生效，下一帧被移除。

v-leave-active：定义离开过渡生效时的状态。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。

v-leave-to：2.1.8 版及以上定义离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 v-leave 被删除)，在过渡/动画完成之后移除。

对于这些在过渡中切换的类名来说，如果你使用一个没有名字的 <transition>，则 v- 是这些类名的默认前缀。如果你使用了 <transition name="my-transition">，那么 v-enter 会替换为 my-transition-enter。

v-enter-active 和 v-leave-active 可以控制进入/离开过渡的不同的缓和曲线，在下面章节会有个示例说明。

CSS 动画用法同 CSS 过渡，区别是在动画中 v-enter 类名在节点插入 DOM 后不会立即删除，而是在 animationend 事件触发时删除。

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris facilisis enim libero, at lacinia diam fermentum id. Pellentesque habitant morbi tristique senectus et netus.

我们可以通过以下 attribute 来自定义过渡类名：

他们的优先级高于普通的类名，这对于 Vue 的过渡系统和其他第三方 CSS 动画库，如 Animate.css 结合使用十分有用。

Vue 为了知道过渡的完成，必须设置相应的事件监听器。它可以是 transitionend 或 animationend，这取决于给元素应用的 CSS 规则。如果你使用其中任何一种，Vue 能自动识别类型并设置监听。

但是，在一些场景中，你需要给同一个元素同时设置两种过渡动效，比如 animation 很快的被触发并完成了，而 transition 效果还没结束。在这种情况中，你就需要使用 type attribute 并设置 animation 或 transition 来明确声明你需要 Vue 监听的类型。

在很多情况下，Vue 可以自动得出过渡效果的完成时机。默认情况下，Vue 会等待其在过渡效果的根元素的第一个 transitionend 或 animationend 事件。然而也可以不这样设定——比如，我们可以拥有一个精心编排的一系列过渡效果，其中一些嵌套的内部元素相比于过渡效果的根元素有延迟的或更长的过渡效果。

在这种情况下你可以用 <transition> 组件上的 duration prop 定制一个显性的过渡持续时间 (以毫秒计)：

可以在 attribute 中声明 JavaScript 钩子

这些钩子函数可以结合 CSS transitions/animations 使用，也可以单独使用。

当只用 JavaScript 过渡的时候，在 enter 和 leave 中必须使用 done 进行回调。否则，它们将被同步调用，过渡会立即完成。

推荐对于仅使用 JavaScript 过渡的元素添加 v-bind:css="false"，Vue 会跳过 CSS 的检测。这也可以避免过渡过程中 CSS 的影响。

一个使用 Velocity.js 的简单例子：

可以通过 appear attribute 设置节点在初始渲染的过渡

这里默认和进入/离开过渡一样，同样也可以自定义 CSS 类名。

在上面的例子中，无论是 appear attribute 还是 v-on:appear 钩子都会生成初始渲染过渡。

我们之后讨论多个组件的过渡，对于原生标签可以使用 v-if/v-else。最常见的多标签过渡是一个列表和描述这个列表为空消息的元素：

当有相同标签名的元素切换时，需要通过 key attribute 设置唯一的值来标记以让 Vue 区分它们，否则 Vue 为了效率只会替换相同标签内部的内容。即使在技术上没有必要，给在 <transition> 组件中的多个元素设置 key 是一个更好的实践。

在一些场景中，也可以通过给同一个元素的 key attribute 设置不同的状态来代替 v-if 和 v-else，上面的例子可以重写为：

使用多个 v-if 的多个元素的过渡可以重写为绑定了动态 property 的单个元素过渡。例如：

在“on”按钮和“off”按钮的过渡中，两个按钮都被重绘了，一个离开过渡的时候另一个开始进入过渡。这是 <transition> 的默认行为 - 进入和离开同时发生。

然后，我们加上 translate 让它们运动像滑动过渡：

同时生效的进入和离开的过渡不能满足所有要求，所以 Vue 提供了过渡模式

in-out：新元素先进行过渡，完成之后当前元素过渡离开。

out-in：当前元素先进行过渡，完成之后新元素过渡进入。

用 out-in 重写之前的开关按钮过渡：

只用添加一个简单的 attribute，就解决了之前的过渡问题而无需任何额外的代码。

in-out 模式不是经常用到，但对于一些稍微不同的过渡效果还是有用的。将之前滑动淡出的例子结合：

多个组件的过渡简单很多 - 我们不需要使用 key attribute。相反，我们只需要使用动态组件：

那么怎么同时渲染整个列表，比如使用 v-for？在这种场景中，使用 <transition-group> 组件。在我们深入例子之前，先了解关于这个组件的几个特点：

现在让我们由一个简单的例子深入，进入和离开的过渡使用之前一样的 CSS 类名。

这个例子有个问题，当添加和移除元素的时候，周围的元素会瞬间移动到他们的新布局的位置，而不是平滑的过渡，我们下面会解决这个问题。

<transition-group> 组件还有一个特殊之处。不仅可以进入和离开动画，还可以改变定位。要使用这个新功能只需了解新增的 v-move class，它会在元素的改变定位的过程中应用。像之前的类名一样，可以通过 name attribute 来自定义前缀，也可以通过 move-class attribute 手动设置。

v-move 对于设置过渡的切换时机和过渡曲线非常有用，你会看到如下的例子：

这个看起来很神奇，内部的实现，Vue 使用了一个叫 FLIP 简单的动画队列使用 transforms 将元素从之前的位置平滑过渡新的位置。

我们将之前实现的例子和这个技术结合，使我们列表的一切变动都会有动画过渡。<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.14.1/lodash.min.js"></script><div id="list-complete-demo" class="demo"> <button v-on:click="shuffle">Shuffle</button> <button v-on:click="add">Add</button> <button v-on:click="remove">Remove</button> <transition-group name="list-complete" tag="p"> <span v-for="item in items" v-bind:key="item" class="list-complete-item" > {{ item }} </span> </transition-group></div>

需要注意的是使用 FLIP 过渡的元素不能设置为 display: inline 。作为替代方案，可以设置为 display: inline-block 或者放置于 flex 中

FLIP 动画不仅可以实现单列过渡，多维网格也同样可以过渡：

Keep hitting the shuffle button until you win.

通过 data attribute 与 JavaScript 通信，就可以实现列表的交错过渡：

过渡可以通过 Vue 的组件系统实现复用。要创建一个可复用过渡组件，你需要做的就是将 <transition> 或者 <transition-group> 作为根组件，然后将任何子组件放置在其中就可以了。

在 Vue 中即使是过渡也是数据驱动的！动态过渡最基本的例子是通过 name attribute 来绑定动态值。

当你想用 Vue 的过渡系统来定义的 CSS 过渡/动画在不同过渡间切换会非常有用。

所有过渡 attribute 都可以动态绑定，但我们不仅仅只有 attribute 可以利用，还可以通过事件钩子获取上下文中的所有数据，因为事件钩子都是方法。这意味着，根据组件的状态不同，你的 JavaScript 过渡会有不同的表现。

最后，创建动态过渡的最终方案是组件通过接受 props 来动态修改之前的过渡。一句老话，唯一的限制是你的想象力。

**Examples:**

Example 1 (unknown):
```unknown
<div id="demo">  <button v-on:click="show = !show">    Toggle  </button>  <transition name="fade">    <p v-if="show">hello</p>  </transition></div>
```

Example 2 (unknown):
```unknown
new Vue({  el: '#demo',  data: {    show: true  }})
```

Example 3 (unknown):
```unknown
.fade-enter-active, .fade-leave-active {  transition: opacity .5s;}.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {  opacity: 0;}
```

Example 4 (unknown):
```unknown
<div id="example-1">  <button @click="show = !show">    Toggle render  </button>  <transition name="slide-fade">    <p v-if="show">hello</p>  </transition></div>
```

---

## 模板语法 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/syntax.html

**Contents:**
- 模板语法
- 插值
  - 文本
  - 原始 HTML
  - Attribute
  - 使用 JavaScript 表达式
- 指令
  - 参数
  - 动态参数
    - 对动态参数的值的约束

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue.js 使用了基于 HTML 的模板语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。所有 Vue.js 的模板都是合法的 HTML，所以能被遵循规范的浏览器和 HTML 解析器解析。

在底层的实现上，Vue 将模板编译成虚拟 DOM 渲染函数。结合响应系统，Vue 能够智能地计算出最少需要重新渲染多少组件，并把 DOM 操作次数减到最少。

如果你熟悉虚拟 DOM 并且偏爱 JavaScript 的原始力量，你也可以不用模板，直接写渲染 (render) 函数，使用可选的 JSX 语法。

数据绑定最常见的形式就是使用“Mustache”语法 (双大括号) 的文本插值：

Mustache 标签将会被替代为对应数据对象上 msg property 的值。无论何时，绑定的数据对象上 msg property 发生了改变，插值处的内容都会更新。

通过使用 v-once 指令，你也能执行一次性地插值，当数据改变时，插值处的内容不会更新。但请留心这会影响到该节点上的其它数据绑定：

双大括号会将数据解释为普通文本，而非 HTML 代码。为了输出真正的 HTML，你需要使用 v-html 指令：

Using mustaches: {{ rawHtml }}

Using v-html directive:

这个 span 的内容将会被替换成为 property 值 rawHtml，直接作为 HTML——会忽略解析 property 值中的数据绑定。注意，你不能使用 v-html 来复合局部模板，因为 Vue 不是基于字符串的模板引擎。反之，对于用户界面 (UI)，组件更适合作为可重用和可组合的基本单位。

你的站点上动态渲染的任意 HTML 可能会非常危险，因为它很容易导致 XSS 攻击。请只对可信内容使用 HTML 插值，绝不要对用户提供的内容使用插值。

Mustache 语法不能作用在 HTML attribute 上，遇到这种情况应该使用 v-bind 指令：

对于布尔 attribute (它们只要存在就意味着值为 true)，v-bind 工作起来略有不同，在这个例子中：

如果 isButtonDisabled 的值是 null、undefined 或 false，则 disabled attribute 甚至不会被包含在渲染出来的 <button> 元素中。

迄今为止，在我们的模板中，我们一直都只绑定简单的 property 键值。但实际上，对于所有的数据绑定，Vue.js 都提供了完全的 JavaScript 表达式支持。

这些表达式会在所属 Vue 实例的数据作用域下作为 JavaScript 被解析。有个限制就是，每个绑定都只能包含单个表达式，所以下面的例子都不会生效。

模板表达式都被放在沙盒中，只能访问全局变量的一个白名单，如 Math 和 Date 。你不应该在模板表达式中试图访问用户定义的全局变量。

指令 (Directives) 是带有 v- 前缀的特殊 attribute。指令 attribute 的值预期是单个 JavaScript 表达式 (v-for 是例外情况，稍后我们再讨论)。指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。回顾我们在介绍中看到的例子：

这里，v-if 指令将根据表达式 seen 的值的真假来插入/移除 <p> 元素。

一些指令能够接收一个“参数”，在指令名称之后以冒号表示。例如，v-bind 指令可以用于响应式地更新 HTML attribute：

在这里 href 是参数，告知 v-bind 指令将该元素的 href attribute 与表达式 url 的值绑定。

另一个例子是 v-on 指令，它用于监听 DOM 事件：

在这里参数是监听的事件名。我们也会更详细地讨论事件处理。

从 2.6.0 开始，可以用方括号括起来的 JavaScript 表达式作为一个指令的参数：

这里的 attributeName 会被作为一个 JavaScript 表达式进行动态求值，求得的值将会作为最终的参数来使用。例如，如果你的 Vue 实例有一个 data property attributeName，其值为 "href"，那么这个绑定将等价于 v-bind:href。

同样地，你可以使用动态参数为一个动态的事件名绑定处理函数：

在这个示例中，当 eventName 的值为 "focus" 时，v-on:[eventName] 将等价于 v-on:focus。

动态参数预期会求出一个字符串，异常情况下值为 null。这个特殊的 null 值可以被显性地用于移除绑定。任何其它非字符串类型的值都将会触发一个警告。

动态参数表达式有一些语法约束，因为某些字符，如空格和引号，放在 HTML attribute 名里是无效的。例如：

变通的办法是使用没有空格或引号的表达式，或用计算属性替代这种复杂表达式。

在 DOM 中使用模板时 (直接在一个 HTML 文件里撰写模板)，还需要避免使用大写字符来命名键名，因为浏览器会把 attribute 名全部强制转为小写：

修饰符 (modifier) 是以半角句号 . 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。例如，.prevent 修饰符告诉 v-on 指令对于触发的事件调用 event.preventDefault()：

在接下来对 v-on 和 v-for 等功能的探索中，你会看到修饰符的其它例子。

v- 前缀作为一种视觉提示，用来识别模板中 Vue 特定的 attribute。当你在使用 Vue.js 为现有标签添加动态行为 (dynamic behavior) 时，v- 前缀很有帮助，然而，对于一些频繁用到的指令来说，就会感到使用繁琐。同时，在构建由 Vue 管理所有模板的单页面应用程序 (SPA - single page application) 时，v- 前缀也变得没那么重要了。因此，Vue 为 v-bind 和 v-on 这两个最常用的指令，提供了特定简写：

它们看起来可能与普通的 HTML 略有不同，但 : 与 @ 对于 attribute 名来说都是合法字符，在所有支持 Vue 的浏览器都能被正确地解析。而且，它们不会出现在最终渲染的标记中。缩写语法是完全可选的，但随着你更深入地了解它们的作用，你会庆幸拥有它们。

**Examples:**

Example 1 (unknown):
```unknown
<span>Message: {{ msg }}</span>
```

Example 2 (unknown):
```unknown
<span v-once>这个将不会改变: {{ msg }}</span>
```

Example 3 (unknown):
```unknown
<p>Using mustaches: {{ rawHtml }}</p><p>Using v-html directive: <span v-html="rawHtml"></span></p>
```

Example 4 (unknown):
```unknown
<div v-bind:id="dynamicId"></div>
```

---

## 状态过渡 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/transitioning-state.html

**Contents:**
- 状态过渡
- 状态动画与侦听器
- 动态状态过渡
- 把过渡放到组件里
- 赋予设计以生命

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue 的过渡系统提供了非常多简单的方法设置进入、离开和列表的动效。那么对于数据元素本身的动效呢，比如：

这些数据要么本身就以数值形式存储，要么可以转换为数值。有了这些数值后，我们就可以结合 Vue 的响应式和组件系统，使用第三方库来实现切换元素的过渡状态。

通过侦听器我们能监听到任何数值 property 的数值更新。可能听起来很抽象，所以让我们先来看看使用 GreenSock 一个例子：

当你把数值更新时，就会触发动画。这个是一个不错的演示，但是对于不能直接像数字一样存储的值，比如 CSS 中的 color 的值，通过下面的例子我们来通过 Tween.js 和 Color.js 实现一个例子：

{{ tweenedCSSColor }}

就像 Vue 的过渡组件一样，数据背后状态过渡会实时更新，这对于原型设计十分有用。当你修改一些变量，即使是一个简单的 SVG 多边形也可实现很多难以想象的效果。

上述 demo 背后的代码可以通过这个示例进行详阅。

管理太多的状态过渡会很快的增加 Vue 实例或者组件的复杂性，幸好很多的动画可以提取到专用的子组件。我们来将之前的示例改写一下：

我们能在组件中结合使用这一节讲到各种过渡策略和 Vue 内建的过渡系统。总之，对于完成各种过渡动效几乎没有阻碍。

只要一个动画，就可以带来生命。不幸的是，当设计师创建图标、logo 和吉祥物的时候，他们交付的通常都是图片或静态的 SVG。所以，虽然 GitHub 的章鱼猫、Twitter 的小鸟以及其它许多 logo 类似于生灵，它们看上去实际上并不是活着的。

Vue 可以帮到你。因为 SVG 的本质是数据，我们只需要这些动物兴奋、思考或警戒的样例。然后 Vue 就可以辅助完成这几种状态之间的过渡动画，来制作你的欢迎页面、加载指示、以及更加带有情感的提示。

Sarah Drasner 展示了下面这个 demo，这个 demo 结合了时间和交互相关的状态改变：

查看 CodePen 上 Sarah Drasner (@sdras) 的例子 Vue-controlled Wall-E.

查看 CodePen 上 Sarah Drasner (@sdras) 的例子 Vue-controlled Wall-E.

**Examples:**

Example 1 (unknown):
```unknown
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.2.4/gsap.min.js"></script><div id="animated-number-demo">  <input v-model.number="number" type="number" step="20">  <p>{{ animatedNumber }}</p></div>
```

Example 2 (unknown):
```unknown
new Vue({  el: '#animated-number-demo',  data: {    number: 0,    tweenedNumber: 0  },  computed: {    animatedNumber: function() {      return this.tweenedNumber.toFixed(0);    }  },  watch: {    number: function(newValue) {      gsap.to(this.$data, { duration: 0.5, tweenedNumber: newValue });    }  }})
```

Example 3 (unknown):
```unknown
<script src="https://cdn.jsdelivr.net/npm/tween.js@16.3.4"></script><script src="https://cdn.jsdelivr.net/npm/color-js@1.0.3"></script><div id="example-7">  <input    v-model="colorQuery"    v-on:keyup.enter="updateColor"    placeholder="Enter a color"  >  <button v-on:click="updateColor">Update</button>  <p>Preview:</p>  <span    v-bind:style="{ backgroundColor: tweenedCSSColor }"    class="example-7-color-preview"  ></span>  <p>{{ tweenedCSSColor }}</p></div>
```

Example 4 (unknown):
```unknown
var Color = net.brehaut.Colornew Vue({  el: '#example-7',  data: {    colorQuery: '',    color: {      red: 0,      green: 0,      blue: 0,      alpha: 1    },    tweenedColor: {}  },  created: function () {    this.tweenedColor = Object.assign({}, this.color)  },  watch: {    color: function () {      function animate () {        if (TWEEN.update()) {          requestAnimationFrame(animate)        }      }      new TWEEN.Tween(this.tweenedColor)        .to(this.color, 750)        .start()      animate()    }  },  computed: {    tweenedCSSColor: function () {      return new Color({        red: this.tweenedColor.red,        green: this.tweenedColor.green,        blue: this.tweenedColor.blue,        alpha: this.tweenedColor.alpha      }).toCSS()    }  },  methods: {    updateColor: function () {      this.color = new Color(this.colorQuery).toRGB()      this.colorQuery = ''    }  }})
```

---

## 列表渲染 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/list.html

**Contents:**
- 列表渲染
- 用 v-for 把一个数组对应为一组元素
- 在 v-for 里使用对象
- 维护状态
- 数组更新检测
  - 变更方法
  - 替换数组
  - 注意事项
- 显示过滤/排序后的结果
- 在 v-for 里使用范围值

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

我们可以用 v-for 指令基于一个数组来渲染一个列表。v-for 指令需要使用 item in items 形式的特殊语法，其中 items 是源数据数组，而 item 则是被迭代的数组元素的别名。

在 v-for 块中，我们可以访问所有父作用域的 property。v-for 还支持一个可选的第二个参数，即当前项的索引。

你也可以用 of 替代 in 作为分隔符，因为它更接近 JavaScript 迭代器的语法：

你也可以用 v-for 来遍历一个对象的 property。

你也可以提供第二个的参数为 property 名称 (也就是键名)：

在遍历对象时，会按 Object.keys() 的结果遍历，但是不能保证它的结果在不同的 JavaScript 引擎下都一致。

当 Vue 正在更新使用 v-for 渲染的元素列表时，它默认使用“就地更新”的策略。如果数据项的顺序被改变，Vue 将不会移动 DOM 元素来匹配数据项的顺序，而是就地更新每个元素，并且确保它们在每个索引位置正确渲染。这个类似 Vue 1.x 的 track-by="$index"。

这个默认的模式是高效的，但是只适用于不依赖子组件状态或临时 DOM 状态 (例如：表单输入值) 的列表渲染输出。

为了给 Vue 一个提示，以便它能跟踪每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一 key attribute：

建议尽可能在使用 v-for 时提供 key attribute，除非遍历输出的 DOM 内容非常简单，或者是刻意依赖默认行为以获取性能上的提升。

因为它是 Vue 识别节点的一个通用机制，key 并不仅与 v-for 特别关联。后面我们将在指南中看到，它还具有其它用途。

不要使用对象或数组之类的非基本类型值作为 v-for 的 key。请用字符串或数值类型的值。

更多 key attribute 的细节用法请移步至 key 的 API 文档。

Vue 将被侦听的数组的变更方法进行了包裹，所以它们也将会触发视图更新。这些被包裹过的方法包括：

你可以打开控制台，然后对前面例子的 items 数组尝试调用变更方法。比如 example1.items.push({ message: 'Baz' })。

变更方法，顾名思义，会变更调用了这些方法的原始数组。相比之下，也有非变更方法，例如 filter()、concat() 和 slice()。它们不会变更原始数组，而总是返回一个新数组。当使用非变更方法时，可以用新数组替换旧数组：

你可能认为这将导致 Vue 丢弃现有 DOM 并重新渲染整个列表。幸运的是，事实并非如此。Vue 为了使得 DOM 元素得到最大范围的重用而实现了一些智能的启发式方法，所以用一个含有相同元素的数组去替换原来的数组是非常高效的操作。

由于 JavaScript 的限制，Vue 不能检测数组和对象的变化。深入响应式原理中有相关的讨论。

有时，我们想要显示一个数组经过过滤或排序后的版本，而不实际变更或重置原始数据。在这种情况下，可以创建一个计算属性，来返回过滤或排序后的数组。

在计算属性不适用的情况下 (例如，在嵌套 v-for 循环中) 你可以使用一个方法：

v-for 也可以接受整数。在这种情况下，它会把模板重复对应次数。

类似于 v-if，你也可以利用带有 v-for 的 <template> 来循环渲染一段包含多个元素的内容。比如：

注意我们不推荐在同一元素上使用 v-if 和 v-for。更多细节可查阅风格指南。

当它们处于同一节点，v-for 的优先级比 v-if 更高，这意味着 v-if 将分别重复运行于每个 v-for 循环中。当你只想为部分项渲染节点时，这种优先级的机制会十分有用，如下：

而如果你的目的是有条件地跳过循环的执行，那么可以将 v-if 置于外层元素 (或 <template>) 上。如：

这部分内容假定你已经了解组件相关知识。你也完全可以先跳过它，以后再回来查看。

在自定义组件上，你可以像在任何普通元素上一样使用 v-for。

2.2.0+ 的版本里，当在组件上使用 v-for 时，key 现在是必须的。

然而，任何数据都不会被自动传递到组件里，因为组件有自己独立的作用域。为了把迭代数据传递到组件里，我们要使用 prop：

不自动将 item 注入到组件里的原因是，这会使得组件与 v-for 的运作紧密耦合。明确组件数据的来源能够使组件在其他场合重复使用。

下面是一个简单的 todo 列表的完整例子：

注意这里的 is="todo-item" attribute。这种做法在使用 DOM 模板时是十分必要的，因为在 <ul> 元素内只有 <li> 元素会被看作有效内容。这样做实现的效果与 <todo-item> 相同，但是可以避开一些潜在的浏览器解析错误。查看 DOM 模板解析说明 来了解更多信息。

**Examples:**

Example 1 (unknown):
```unknown
<ul id="example-1">  <li v-for="item in items" :key="item.message">    {{ item.message }}  </li></ul>
```

Example 2 (unknown):
```unknown
var example1 = new Vue({  el: '#example-1',  data: {    items: [      { message: 'Foo' },      { message: 'Bar' }    ]  }})
```

Example 3 (unknown):
```unknown
<ul id="example-2">  <li v-for="(item, index) in items">    {{ parentMessage }} - {{ index }} - {{ item.message }}  </li></ul>
```

Example 4 (unknown):
```unknown
var example2 = new Vue({  el: '#example-2',  data: {    parentMessage: 'Parent',    items: [      { message: 'Foo' },      { message: 'Bar' }    ]  }})
```

---

## 对比其他框架 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/comparison.html

**Contents:**
- 对比其他框架
- React
  - 运行时性能
    - 优化
  - HTML & CSS
    - JSX vs Templates
    - 组件作用域内的 CSS
  - 规模
    - 向上扩展
    - 向下扩展

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

这个页面无疑是最难编写的，但我们认为它也是非常重要的。或许你曾遇到了一些问题并且已经用其他的框架解决了。你来这里的目的是看看 Vue 是否有更好的解决方案。这也是我们在此想要回答的。

客观来说，作为核心团队成员，显然我们会更偏爱 Vue，认为对于某些问题来讲用 Vue 解决会更好。如果没有这点信念，我们也就不会整天为此忙活了。但是在此，我们想尽可能地公平和准确地来描述一切。其他的框架也有显著的优点，例如 React 庞大的生态系统，或者像是 Knockout 对浏览器的支持覆盖到了 IE6。我们会尝试着把这些内容全部列出来。

我们也希望得到你的帮助，来使文档保持最新状态，因为 JavaScript 的世界进步得太快。如果你注意到一个不准确或似乎不太正确的地方，请提交问题让我们知道。

React 和 Vue 有许多相似之处，它们都有：

由于有着众多的相似处，我们会用更多的时间在这一块进行比较。这里我们不只保证技术内容的准确性，同时也兼顾了平衡的考量。我们需要承认 React 比 Vue 更好的地方，比如更丰富的生态系统。

下列部分章节会略微有些过时，因为最近 React 16+ 的发布，我们计划在不久的将来和 React 社区一起重写这部分内容。

React 和 Vue 都是非常快的，所以速度并不是在它们之中做选择的决定性因素。对于具体的数据表现，可以移步这个第三方 benchmark，它专注于渲染/更新非常简单的组件树的真实性能。

在 React 应用中，当某个组件的状态发生变化时，它会以该组件为根，重新渲染整个组件子树。

如要避免不必要的子组件的重渲染，你需要在所有可能的地方使用 PureComponent，或是手动实现 shouldComponentUpdate 方法。同时你可能会需要使用不可变的数据结构来使得你的组件更容易被优化。

然而，使用 PureComponent 和 shouldComponentUpdate 时，需要保证该组件的整个子树的渲染输出都是由该组件的 props 所决定的。如果不符合这个情况，那么此类优化就会导致难以察觉的渲染结果不一致。这使得 React 中的组件优化伴随着相当的心智负担。

在 Vue 应用中，组件的依赖是在渲染过程中自动追踪的，所以系统能精确知晓哪个组件确实需要被重渲染。你可以理解为每一个组件都已经自动获得了 shouldComponentUpdate，并且没有上述的子树问题限制。

Vue 的这个特点使得开发者不再需要考虑此类优化，从而能够更好地专注于应用本身。

在 React 中，一切都是 JavaScript。不仅仅是 HTML 可以用 JSX 来表达，现在的潮流也越来越多地将 CSS 也纳入到 JavaScript 中来处理。这类方案有其优点，但也存在一些不是每个开发者都能接受的取舍。

Vue 的整体思想是拥抱经典的 Web 技术，并在其上进行扩展。我们下面会详细分析一下。

在 React 中，所有的组件的渲染功能都依靠 JSX。JSX 是使用 XML 语法编写 JavaScript 的一种语法糖。

你可以使用完整的编程语言 JavaScript 功能来构建你的视图页面。比如你可以使用临时变量、JS 自带的流程控制、以及直接引用当前 JS 作用域中的值等等。

开发工具对 JSX 的支持相比于现有可用的其他 Vue 模板还是比较先进的 (比如，linting、类型检查、编辑器的自动完成)。

事实上 Vue 也提供了渲染函数，甚至支持 JSX。然而，我们默认推荐的还是模板。任何合乎规范的 HTML 都是合法的 Vue 模板，这也带来了一些特有的优势：

对于很多习惯了 HTML 的开发者来说，模板比起 JSX 读写起来更自然。这里当然有主观偏好的成分，但如果这种区别会导致开发效率的提升，那么它就有客观的价值存在。

基于 HTML 的模板使得将已有的应用逐步迁移到 Vue 更为容易。

这也使得设计师和新人开发者更容易理解和参与到项目中。

你甚至可以使用其他模板预处理器，比如 Pug 来书写 Vue 的模板。

有些开发者认为模板意味着需要学习额外的 DSL (Domain-Specific Language 领域特定语言) 才能进行开发——我们认为这种区别是比较肤浅的。首先，JSX 并不是没有学习成本的——它是基于 JS 之上的一套额外语法。同时，正如同熟悉 JS 的人学习 JSX 会很容易一样，熟悉 HTML 的人学习 Vue 的模板语法也是很容易的。最后，DSL 的存在使得我们可以让开发者用更少的代码做更多的事，比如 v-on 的各种修饰符，在 JSX 中实现对应的功能会需要多得多的代码。

更抽象一点来看，我们可以把组件区分为两类：一类是偏视图表现的 (presentational)，一类则是偏逻辑的 (logical)。我们推荐在前者中使用模板，在后者中使用 JSX 或渲染函数。这两类组件的比例会根据应用类型的不同有所变化，但整体来说我们发现表现类的组件远远多于逻辑类组件。

除非你把组件分布在多个文件上 (例如 CSS Modules)，CSS 作用域在 React 中是通过 CSS-in-JS 的方案实现的 (比如 styled-components 和 emotion)。这引入了一个新的面向组件的样式范例，它和普通的 CSS 撰写过程是有区别的。另外，虽然在构建时将 CSS 提取到一个单独的样式表是支持的，但 bundle 里通常还是需要一个运行时程序来让这些样式生效。当你能够利用 JavaScript 灵活处理样式的同时，也需要权衡 bundle 的尺寸和运行时的开销。

如果你是一个 CSS-in-JS 的爱好者，许多主流的 CSS-in-JS 库也都支持 Vue (比如 styled-components-vue 和 vue-emotion)。这里 React 和 Vue 主要的区别是，Vue 设置样式的默认方法是单文件组件里类似 style 的标签。

单文件组件让你可以在同一个文件里完全控制 CSS，将其作为组件代码的一部分。

这个可选 scoped attribute 会自动添加一个唯一的 attribute (比如 data-v-21e5b78) 为组件内 CSS 指定作用域，编译的时候 .list-container:hover 会被编译成类似 .list-container[data-v-21e5b78]:hover。

最后，Vue 的单文件组件里的样式设置是非常灵活的。通过 vue-loader，你可以使用任意预处理器、后处理器，甚至深度集成 CSS Modules——全部都在 <style> 标签内。

Vue 和 React 都提供了强大的路由来应对大型应用。React 社区在状态管理方面非常有创新精神 (比如 Flux、Redux)，而这些状态管理模式甚至 Redux 本身也可以非常容易的集成在 Vue 应用中。实际上，Vue 更进一步地采用了这种模式 (Vuex)，更加深入集成 Vue 的状态管理解决方案 Vuex 相信能为你带来更好的开发体验。

两者另一个重要差异是，Vue 的路由库和状态管理库都是由官方维护支持且与核心库同步更新的。React 则是选择把这些问题交给社区维护，因此创建了一个更分散的生态系统。但相对的，React 的生态系统相比 Vue 更加繁荣。

最后，Vue 提供了 CLI 脚手架，能让你通过交互式的脚手架引导非常容易地构建项目。你甚至可以使用它快速开发组件的原型。React 在这方面也提供了 create-react-app，但是现在还存在一些局限性：

而要注意的是这些限制是故意设计的，这有它的优势。例如，如果你的项目需求非常简单，你就不需要自定义生成过程。你能把它作为一个依赖来更新。如果阅读更多关于不同的设计理念。

React 学习曲线陡峭，在你开始学 React 前，你需要知道 JSX 和 ES2015，因为许多示例用的是这些语法。你需要学习构建系统，虽然你在技术上可以用 Babel 来实时编译代码，但是这并不推荐用于生产环境。

就像 Vue 向上扩展好比 React 一样，Vue 向下扩展后就类似于 jQuery。你只要把如下标签放到页面就可以运行：

然后你就可以编写 Vue 代码并应用到生产中，你只要用 min 版 Vue 文件替换掉就不用担心其他的性能问题。

由于起步阶段不需学 JSX，ES2015 以及构建系统，所以开发者只需不到一天的时间阅读指南就可以建立简单的应用程序。

React Native 能使你用相同的组件模型编写有本地渲染能力的 APP (iOS 和 Android)。能同时跨多平台开发，对开发者是非常棒的。相应地，Vue 和 Weex 会进行官方合作，Weex 是阿里巴巴发起的跨平台用户界面开发框架，同时也正在 Apache 基金会进行项目孵化，Weex 允许你使用 Vue 语法开发不仅仅可以运行在浏览器端，还能被用于开发 iOS 和 Android 上的原生应用的组件。

在现在，Weex 还在积极发展，成熟度也不能和 React Native 相抗衡。但是，Weex 的发展是由世界上最大的电子商务企业的需求在驱动，Vue 团队也会和 Weex 团队积极合作确保为开发者带来良好的开发体验。

另一个选择是 NativeScript-Vue，一个用 Vue.js 构建完全原生应用的 NativeScript 插件。

Mobx 在 React 社区很流行，实际上在 Vue 也采用了几乎相同的反应系统。在有限程度上，React + Mobx 也可以被认为是更繁琐的 Vue，所以如果你习惯组合使用它们，那么选择 Vue 会更合理。

类 React 的库们往往尽可能地与 React 共享 API 和生态。因此上述比较对它们来说也同样适用。它们和 React 的不同往往在于更小的生态。因为这些库无法 100% 兼容 React 生态中的全部，部分工具和辅助库也可能无法使用。或者即使看上去能工作，但也有可能随时发生不兼容，除非你用的这个类 React 库官方与 React 保持严格一致。

Vue 的一些语法和 AngularJS 的很相似 (例如 v-if vs ng-if)。因为 AngularJS 是 Vue 早期开发的灵感来源。然而，AngularJS 中存在的许多问题，在 Vue 中已经得到解决。

在 API 与设计两方面上 Vue.js 都比 AngularJS 简单得多，因此你可以快速地掌握它的全部特性并投入开发。

Vue.js 是一个更加灵活开放的解决方案。它允许你以希望的方式组织应用程序，而不是在任何时候都必须遵循 AngularJS 制定的规则，这让 Vue 能适用于各种项目。我们知道把决定权交给你是非常必要的。

这也是为什么我们提供了一个基于 Vue.js 进行快速开发的完整系统。Vue CLI 旨在成为 Vue 生态系统中标准的基础工具。它使得多样化的构建工具通过妥善的默认配置无缝协作在一起。这样你就可以专注在应用本身，而不会在配置上花费太多时间。同时，它也提供了根据实际需求调整每个工具配置的灵活性。

AngularJS 使用双向绑定，Vue 在不同组件间强制使用单向数据流。这使应用中的数据流更加清晰易懂。

在 Vue 中指令和组件分得更清晰。指令只封装 DOM 操作，而组件代表一个自给自足的独立单元——有自己的视图和数据逻辑。在 AngularJS 中，每件事都由指令来做，而组件只是一种特殊的指令。

Vue 有更好的性能，并且非常非常容易优化，因为它不使用脏检查。

在 AngularJS 中，当 watcher 越来越多时会变得越来越慢，因为作用域内的每一次变化，所有 watcher 都要重新计算。并且，如果一些 watcher 触发另一个更新，脏检查循环 (digest cycle) 可能要运行多次。AngularJS 用户常常要使用深奥的技术，以解决脏检查循环的问题。有时没有简单的办法来优化有大量 watcher 的作用域。

Vue 则根本没有这个问题，因为它使用基于依赖追踪的观察系统并且异步队列更新，所有的数据变化都是独立触发，除非它们之间有明确的依赖关系。

有意思的是，Angular 和 Vue 用相似的设计解决了一些 AngularJS 中存在的问题。

我们将新的 Angular 独立开来讨论，因为它是一个和 AngularJS 完全不同的框架。例如：它具有优秀的组件系统，并且许多实现已经完全重写，API 也完全改变了。

Angular 事实上必须用 TypeScript 来开发，因为它的文档和学习资源几乎全部是面向 TS 的。TS 有很多好处——静态类型检查在大规模的应用中非常有用，同时对于 Java 和 C# 背景的开发者也是非常提升开发效率的。

然而，并不是所有人都想用 TS——在中小型规模的项目中，引入 TS 可能并不会带来太多明显的优势。在这些情况下，用 Vue 会是更好的选择，因为在不用 TS 的情况下使用 Angular 会很有挑战性。

最后，虽然 Vue 和 TS 的整合可能不如 Angular 那么深入，我们也提供了官方的类型声明和组件装饰器，并且知道有大量用户在生产环境中使用 Vue + TS 的组合。我们也和微软的 TS / VSCode 团队进行着积极的合作，目标是为 Vue + TS 用户提供更好的类型检查和 IDE 开发体验。

这两个框架都很快，有非常类似的 benchmark 数据。你可以浏览具体的数据做更细粒度的对比，不过速度应该不是决定性的因素。

在体积方面，最近的 Angular 版本中在使用了 AOT 和 tree-shaking 技术后使得最终的代码体积减小了许多。但即使如此，一个包含了 Vuex + Vue Router 的 Vue 项目 (gzip 之后 30kB) 相比使用了这些优化的 angular-cli 生成的默认项目尺寸 (~65KB) 还是要小得多。

Vue 相比于 Angular 更加灵活，Vue 官方提供了构建工具来协助你构建项目，但它并不限制你去如何组织你的应用代码。有人可能喜欢有严格的代码组织规范，但也有开发者喜欢更灵活自由的方式。

要学习 Vue，你只需要有良好的 HTML 和 JavaScript 基础。有了这些基本的技能，你就可以非常快速地通过阅读指南投入开发。

Angular 的学习曲线是非常陡峭的——作为一个框架，它的 API 面积比起 Vue 要大得多，你也因此需要理解更多的概念才能开始有效率地工作。当然，Angular 本身的复杂度是因为它的设计目标就是只针对大型的复杂应用；但不可否认的是，这也使得它对于经验不甚丰富的开发者相当的不友好。

Ember 是一个全能框架。它提供了大量的约定，一旦你熟悉了它们，开发会变得很高效。不过，这也意味着学习曲线较高，而且并不灵活。这意味着在框架和库 (加上一系列松散耦合的工具) 之间做权衡选择。后者会更自由，但是也要求你做更多架构上的决定。

也就是说，我们最好比较的是 Vue 内核和 Ember 的模板与数据模型层：

Vue 在普通 JavaScript 对象上建立响应，提供自动化的计算属性。在 Ember 中需要将所有东西放在 Ember 对象内，并且手工为计算属性声明依赖。

Vue 的模板语法可以用全功能的 JavaScript 表达式，而 Handlebars 的语法和帮助函数相比来说非常受限。

在性能上，Vue 比 Ember 好很多，即使是 Ember 3.x 的最新 Glimmer 引擎。Vue 能够自动批量更新，而 Ember 在性能敏感的场景时需要手动管理。

Knockout 是 MVVM 领域内的先驱，并且追踪依赖。它的响应系统和 Vue 也很相似。它在浏览器支持以及其他方面的表现也是让人印象深刻的。它最低能支持到 IE6，而 Vue 最低只能支持到 IE9。

随着时间的推移，Knockout 的发展已有所放缓，并且略显有点老旧了。比如，它的组件系统缺少完备的生命周期事件方法，尽管这些在现在是非常常见的。以及相比于 Vue 调用子组件的接口它的方法显得有点笨重。

如果你有兴趣研究，你还会发现二者在接口设计的理念上是不同的。这可以通过各自创建的 simple Todo List 体现出来。或许有点主观，但是很多人认为 Vue 的 API 接口更简单结构更优雅。

Polymer 是另一个由谷歌赞助的项目，事实上也是 Vue 的一个灵感来源。Vue 的组件可以粗略的类比于 Polymer 的自定义元素，并且两者具有相似的开发风格。最大的不同之处在于，Polymer 是基于最新版的 Web Components 标准之上，并且需要重量级的 polyfills 来帮助工作 (性能下降)，浏览器本身并不支持这些功能。相比而言，Vue 在支持到 IE9 的情况下并不需要依赖 polyfills 来工作。

在 Polymer 版本中，为了弥补性能，团队非常有限的使用数据绑定系统。例如，在 Polymer 中唯一支持的表达式只有布尔值否定和单一的方法调用，它的 computed 方法的实现也并不是很灵活。

Riot 3.0 提供了一个类似于基于组件的开发模型 (在 Riot 中称之为 Tag)，它提供了小巧精美的 API。Riot 和 Vue 在设计理念上可能有许多相似处。尽管相比 Riot，Vue 要显得重一点，Vue 还是有很多显著优势的：

**Examples:**

Example 1 (unknown):
```unknown
<style scoped>  @media (min-width: 250px) {    .list-container:hover {      background: orange;    }  }</style>
```

Example 2 (unknown):
```unknown
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

---

## 服务端渲染 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/ssr.html

**Contents:**
- 服务端渲染
- SSR 完全指南
- Nuxt.js
- Quasar Framework SSR + PWA

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

在 2.3 发布后我们发布了一份完整的构建 Vue 服务端渲染应用的指南。这份指南非常深入，适合已经熟悉 Vue、webpack 和 Node.js 开发的开发者阅读。请移步 v2.ssr.vuejs.org。

从头搭建一个服务端渲染的应用是相当复杂的。幸运的是，我们有一个优秀的社区项目 Nuxt.js 让这一切变得非常简单。Nuxt 是一个基于 Vue 生态的更高层的框架，为开发服务端渲染的 Vue 应用提供了极其便利的开发体验。更酷的是，你甚至可以用它来做为静态站生成器。推荐尝试。

Quasar Framework 可以通过其一流的构建系统、合理的配置和开发者扩展性生成 (可选地和 PWA 互通的) SSR 应用，让你的想法的设计和构建变得轻而易举。你可以在服务端挑选执行超过上百款遵循“Material Design 2.0”的组件，并在浏览器端可用。你甚至可以管理网站的 <meta> 标签。Quasar 是一个基于 Node.js 和 webpack 的开发环境，它可以通过一套代码完成 SPA、PWA、SSR、Electron、Capacitor 和 Cordova 应用的快速开发。

---

## Class 与 Style 绑定 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/class-and-style.html

**Contents:**
- Class 与 Style 绑定
- 绑定 HTML Class
  - 对象语法
  - 数组语法
  - 用在组件上
- 绑定内联样式
  - 对象语法
  - 数组语法
  - 自动添加前缀
  - 多重值

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

操作元素的 class 列表和内联样式是数据绑定的一个常见需求。因为它们都是 attribute，所以我们可以用 v-bind 处理它们：只需要通过表达式计算出字符串结果即可。不过，字符串拼接麻烦且易错。因此，在将 v-bind 用于 class 和 style 时，Vue.js 做了专门的增强。表达式结果的类型除了字符串之外，还可以是对象或数组。

我们可以传给 v-bind:class 一个对象，以动态地切换 class：

上面的语法表示 active 这个 class 存在与否将取决于数据 property isActive 的 truthiness。

你可以在对象中传入更多字段来动态切换多个 class。此外，v-bind:class 指令也可以与普通的 class attribute 共存。当有如下模板：

当 isActive 或者 hasError 变化时，class 列表将相应地更新。例如，如果 hasError 的值为 true，class 列表将变为 "static active text-danger"。

渲染的结果和上面一样。我们也可以在这里绑定一个返回对象的计算属性。这是一个常用且强大的模式：

我们可以把一个数组传给 v-bind:class，以应用一个 class 列表：

如果你也想根据条件切换列表中的 class，可以用三元表达式：

这样写将始终添加 errorClass，但是只有在 isActive 是 truthy[1] 时才添加 activeClass。

不过，当有多个条件 class 时这样写有些繁琐。所以在数组语法中也可以使用对象语法：

这个章节假设你已经对 Vue 组件有一定的了解。当然你也可以先跳过这里，稍后再回过头来看。

当在一个自定义组件上使用 class property 时，这些 class 将被添加到该组件的根元素上面。这个元素上已经存在的 class 不会被覆盖。

当 isActive 为 truthy[1] 时，HTML 将被渲染成为：

v-bind:style 的对象语法十分直观——看着非常像 CSS，但其实是一个 JavaScript 对象。CSS property 名可以用驼峰式 (camelCase) 或短横线分隔 (kebab-case，记得用引号括起来) 来命名：

直接绑定到一个样式对象通常更好，这会让模板更清晰：

同样的，对象语法常常结合返回对象的计算属性使用。

v-bind:style 的数组语法可以将多个样式对象应用到同一个元素上：

当 v-bind:style 使用需要添加浏览器引擎前缀的 CSS property 时，如 transform，Vue.js 会自动侦测并添加相应的前缀。

从 2.3.0 起你可以为 style 绑定中的 property 提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：

这样写只会渲染数组中最后一个被浏览器支持的值。在本例中，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 display: flex。

译者注[1] truthy 不是 true，详见 MDN 的解释。

**Examples:**

Example 1 (unknown):
```unknown
<div v-bind:class="{ active: isActive }"></div>
```

Example 2 (unknown):
```unknown
<div  class="static"  v-bind:class="{ active: isActive, 'text-danger': hasError }"></div>
```

Example 3 (unknown):
```unknown
data: {  isActive: true,  hasError: false}
```

Example 4 (unknown):
```unknown
<div class="static active"></div>
```

---

## 事件处理 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/events.html

**Contents:**
- 事件处理
- 监听事件
- 事件处理方法
- 内联处理器中的方法
- 事件修饰符
- 按键修饰符
  - 按键码
- 系统修饰键
  - .exact 修饰符
  - 鼠标按钮修饰符

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

可以用 v-on 指令监听 DOM 事件，并在触发时运行一些 JavaScript 代码。

The button above has been clicked {{ counter }} times.

然而许多事件处理逻辑会更为复杂，所以直接把 JavaScript 代码写在 v-on 指令中是不可行的。因此 v-on 还可以接收一个需要调用的方法名称。

除了直接绑定到一个方法，也可以在内联 JavaScript 语句中调用方法：

有时也需要在内联语句处理器中访问原始的 DOM 事件。可以用特殊变量 $event 把它传入方法：

在事件处理程序中调用 event.preventDefault() 或 event.stopPropagation() 是非常常见的需求。尽管我们可以在方法中轻松实现这点，但更好的方式是：方法只有纯粹的数据逻辑，而不是去处理 DOM 事件细节。

为了解决这个问题，Vue.js 为 v-on 提供了事件修饰符。之前提过，修饰符是由点开头的指令后缀来表示的。

使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用 v-on:click.prevent.self 会阻止所有的点击，而 v-on:click.self.prevent 只会阻止对元素自身的点击。

不像其它只能对原生的 DOM 事件起作用的修饰符，.once 修饰符还能被用到自定义的组件事件上。如果你还没有阅读关于组件的文档，现在大可不必担心。

Vue 还对应 addEventListener 中的 passive 选项提供了 .passive 修饰符。

这个 .passive 修饰符尤其能够提升移动端的性能。

不要把 .passive 和 .prevent 一起使用，因为 .prevent 将会被忽略，同时浏览器可能会向你展示一个警告。请记住，.passive 会告诉浏览器你不想阻止事件的默认行为。

在监听键盘事件时，我们经常需要检查详细的按键。Vue 允许为 v-on 在监听键盘事件时添加按键修饰符：

你可以直接将 KeyboardEvent.key 暴露的任意有效按键名转换为 kebab-case 来作为修饰符。

在上述示例中，处理函数只会在 $event.key 等于 PageDown 时被调用。

keyCode 的事件用法已经被废弃了并可能不会被最新的浏览器支持。

使用 keyCode attribute 也是允许的：

为了在必要的情况下支持旧浏览器，Vue 提供了绝大多数常用的按键码的别名：

有一些按键 (.esc 以及所有的方向键) 在 IE9 中有不同的 key 值, 如果你想支持 IE9，这些内置的别名应该是首选。

你还可以通过全局 config.keyCodes 对象自定义按键修饰符别名：

可以用如下修饰符来实现仅在按下相应按键时才触发鼠标或键盘事件的监听器。

注意：在 Mac 系统键盘上，meta 对应 command 键 (⌘)。在 Windows 系统键盘 meta 对应 Windows 徽标键 (⊞)。在 Sun 操作系统键盘上，meta 对应实心宝石键 (◆)。在其他特定键盘上，尤其在 MIT 和 Lisp 机器的键盘、以及其后继产品，比如 Knight 键盘、space-cadet 键盘，meta 被标记为“META”。在 Symbolics 键盘上，meta 被标记为“META”或者“Meta”。

请注意修饰键与常规按键不同，在和 keyup 事件一起用时，事件触发时修饰键必须处于按下状态。换句话说，只有在按住 ctrl 的情况下释放其它按键，才能触发 keyup.ctrl。而单单释放 ctrl 也不会触发事件。如果你想要这样的行为，请为 ctrl 换用 keyCode：keyup.17。

.exact 修饰符允许你控制由精确的系统修饰符组合触发的事件。

这些修饰符会限制处理函数仅响应特定的鼠标按钮。

你可能注意到这种事件监听的方式违背了关注点分离 (separation of concern) 这个长期以来的优良传统。但不必担心，因为所有的 Vue.js 事件处理方法和表达式都严格绑定在当前视图的 ViewModel 上，它不会导致任何维护上的困难。实际上，使用 v-on 有几个好处：

扫一眼 HTML 模板便能轻松定位在 JavaScript 代码里对应的方法。

因为你无须在 JavaScript 里手动绑定事件，你的 ViewModel 代码可以是非常纯粹的逻辑，和 DOM 完全解耦，更易于测试。

当一个 ViewModel 被销毁时，所有的事件处理器都会自动被删除。你无须担心如何清理它们。

**Examples:**

Example 1 (unknown):
```unknown
<div id="example-1">  <button v-on:click="counter += 1">Add 1</button>  <p>The button above has been clicked {{ counter }} times.</p></div>
```

Example 2 (unknown):
```unknown
var example1 = new Vue({  el: '#example-1',  data: {    counter: 0  }})
```

Example 3 (unknown):
```unknown
<div id="example-2">  <!-- `greet` 是在下面定义的方法名 -->  <button v-on:click="greet">Greet</button></div>
```

Example 4 (javascript):
```javascript
var example2 = new Vue({  el: '#example-2',  data: {    name: 'Vue.js'  },  // 在 `methods` 对象中定义方法  methods: {    greet: function (event) {      // `this` 在方法里指向当前 Vue 实例      alert('Hello ' + this.name + '!')      // `event` 是原生 DOM 事件      if (event) {        alert(event.target.tagName)      }    }  }})// 也可以用 JavaScript 直接调用方法example2.greet() // => 'Hello Vue.js!'
```

---

## 动态组件 & 异步组件 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-dynamic-async.html

**Contents:**
- 动态组件 & 异步组件
- 在动态组件上使用 keep-alive
- 异步组件
  - 处理加载状态

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

我们之前在一个多标签的界面中使用 is attribute 来切换不同的组件：

当在这些组件之间切换的时候，你有时会想保持这些组件的状态，以避免反复重新渲染导致的性能问题。例如我们来展开说一说这个多标签界面：

你会注意到，如果你选择了一篇文章，切换到 Archive 标签，然后再切换回 Posts，是不会继续展示你之前选择的文章的。这是因为你每次切换新标签的时候，Vue 都创建了一个新的 currentTabComponent 实例。

重新创建动态组件的行为通常是非常有用的，但是在这个案例中，我们更希望那些标签的组件实例能够被在它们第一次被创建的时候缓存下来。为了解决这个问题，我们可以用一个 <keep-alive> 元素将其动态组件包裹起来。

现在这个 Posts 标签保持了它的状态 (被选中的文章) 甚至当它未被渲染时也是如此。你可以在这个示例查阅到完整的代码。

注意这个 <keep-alive> 要求被切换到的组件都有自己的名字，不论是通过组件的 name 选项还是局部/全局注册。

你可以在 API 参考文档查阅更多关于 <keep-alive> 的细节。

在大型应用中，我们可能需要将应用分割成小一些的代码块，并且只在需要的时候才从服务器加载一个模块。为了简化，Vue 允许你以一个工厂函数的方式定义你的组件，这个工厂函数会异步解析你的组件定义。Vue 只有在这个组件需要被渲染的时候才会触发该工厂函数，且会把结果缓存起来供未来重渲染。例如：

如你所见，这个工厂函数会收到一个 resolve 回调，这个回调函数会在你从服务器得到组件定义的时候被调用。你也可以调用 reject(reason) 来表示加载失败。这里的 setTimeout 是为了演示用的，如何获取组件取决于你自己。一个推荐的做法是将异步组件和 webpack 的 code-splitting 功能一起配合使用：

你也可以在工厂函数中返回一个 Promise，所以把 webpack 2 和 ES2015 语法加在一起，我们可以这样使用动态导入：

当使用局部注册的时候，你也可以直接提供一个返回 Promise 的函数：

如果你是一个 Browserify 用户同时喜欢使用异步组件，很不幸这个工具的作者明确表示异步加载“并不会被 Browserify 支持”，至少官方不会。Browserify 社区已经找到了一些变通方案，这些方案可能会对已存在的复杂应用有帮助。对于其它的场景，我们推荐直接使用 webpack，以拥有内置的头等异步支持。

这里的异步组件工厂函数也可以返回一个如下格式的对象：

注意如果你希望在 Vue Router 的路由组件中使用上述语法的话，你必须使用 Vue Router 2.4.0+ 版本。

**Examples:**

Example 1 (unknown):
```unknown
<component v-bind:is="currentTabComponent"></component>
```

Example 2 (unknown):
```unknown
<!-- 失活的组件将会被缓存！--><keep-alive>  <component v-bind:is="currentTabComponent"></component></keep-alive>
```

Example 3 (unknown):
```unknown
Vue.component('async-example', function (resolve, reject) {  setTimeout(function () {    // 向 `resolve` 回调传递组件定义    resolve({      template: '<div>I am async!</div>'    })  }, 1000)})
```

Example 4 (unknown):
```unknown
Vue.component('async-webpack-example', function (resolve) {  // 这个特殊的 `require` 语法将会告诉 webpack  // 自动将你的构建代码切割成多个包，这些包  // 会通过 Ajax 请求加载  require(['./my-async-component'], resolve)})
```

---

## 条件渲染 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/conditional.html

**Contents:**
- 条件渲染
- v-if
  - 在 <template> 元素上使用 v-if 条件渲染分组
  - v-else
  - v-else-if
  - 用 key 管理可复用的元素
- v-show
- v-if vs v-show
- v-if 与 v-for 一起使用

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

v-if 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回 truthy 值的时候被渲染。

也可以用 v-else 添加一个“else 块”：

因为 v-if 是一个指令，所以必须将它添加到一个元素上。但是如果想切换多个元素呢？此时可以把一个 <template> 元素当做不可见的包裹元素，并在上面使用 v-if。最终的渲染结果将不包含 <template> 元素。

你可以使用 v-else 指令来表示 v-if 的“else 块”：

v-else 元素必须紧跟在带 v-if 或者 v-else-if 的元素的后面，否则它将不会被识别。

v-else-if，顾名思义，充当 v-if 的“else-if 块”，可以连续使用：

类似于 v-else，v-else-if 也必须紧跟在带 v-if 或者 v-else-if 的元素之后。

Vue 会尽可能高效地渲染元素，通常会复用已有元素而不是从头开始渲染。这么做除了使 Vue 变得非常快之外，还有其它一些好处。例如，如果你允许用户在不同的登录方式之间切换：

那么在上面的代码中切换 loginType 将不会清除用户已经输入的内容。因为两个模板使用了相同的元素，<input> 不会被替换掉——仅仅是替换了它的 placeholder。

自己动手试一试，在输入框中输入一些文本，然后按下切换按钮：

这样也不总是符合实际需求，所以 Vue 为你提供了一种方式来表达“这两个元素是完全独立的，不要复用它们”。只需添加一个具有唯一值的 key attribute 即可：

现在，每次切换时，输入框都将被重新渲染。请看：

注意，<label> 元素仍然会被高效地复用，因为它们没有添加 key attribute。

另一个用于根据条件展示元素的选项是 v-show 指令。用法大致一样：

不同的是带有 v-show 的元素始终会被渲染并保留在 DOM 中。v-show 只是简单地切换元素的 CSS property display。

注意，v-show 不支持 <template> 元素，也不支持 v-else。

v-if 是“真正”的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。

v-if 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。

相比之下，v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。

一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

不推荐同时使用 v-if 和 v-for。请查阅风格指南以获取更多信息。

当 v-if 与 v-for 一起使用时，v-for 具有比 v-if 更高的优先级。请查阅列表渲染指南以获取详细信息。

**Examples:**

Example 1 (unknown):
```unknown
<h1 v-if="awesome">Vue is awesome!</h1>
```

Example 2 (unknown):
```unknown
<h1 v-if="awesome">Vue is awesome!</h1><h1 v-else>Oh no 😢</h1>
```

Example 3 (unknown):
```unknown
<template v-if="ok">  <h1>Title</h1>  <p>Paragraph 1</p>  <p>Paragraph 2</p></template>
```

Example 4 (unknown):
```unknown
<div v-if="Math.random() > 0.5">  Now you see me</div><div v-else>  Now you don't</div>
```

---

## 介绍 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/index.html

**Contents:**
- 介绍
- Vue.js 是什么
- 起步
- 声明式渲染
- 条件与循环
- 处理用户输入
- 组件化应用构建
  - 与自定义元素的关系
- 准备好了吗？

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue (读音 /vjuː/，类似于 view) 是一套用于构建用户界面的渐进式框架。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

如果你想在深入学习 Vue 之前对它有更多了解，我们制作了一个视频，带您了解其核心概念和一个示例工程。

如果你已经是有经验的前端开发者，想知道 Vue 与其它库/框架有哪些区别，请查看对比其它框架。

官方指南假设你已了解关于 HTML、CSS 和 JavaScript 的中级知识。如果你刚开始学习前端开发，将框架作为你的第一步可能不是最好的主意——掌握好基础知识再来吧！之前有其它框架的使用经验会有帮助，但这不是必需的。

尝试 Vue.js 最简单的方法是使用 Hello World 例子。你可以在浏览器新标签页中打开它，跟着例子学习一些基础用法。或者你也可以创建一个 .html 文件，然后通过如下方式引入 Vue：

安装教程给出了更多安装 Vue 的方式。请注意我们不推荐新手直接使用 vue-cli，尤其是在你还不熟悉基于 Node.js 的构建工具时。

如果你喜欢交互式的东西，你也可以查阅这个 Scrimba 上的系列教程，它揉合了录屏和代码试验田，并允许你随时暂停和播放。

Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：

我们已经成功创建了第一个 Vue 应用！看起来这跟渲染一个字符串模板非常类似，但是 Vue 在背后做了大量工作。现在数据和 DOM 已经被建立了关联，所有东西都是响应式的。我们要怎么确认呢？打开你的浏览器的 JavaScript 控制台 (就在这个页面打开)，并修改 app.message 的值，你将看到上例相应地更新。

注意我们不再和 HTML 直接交互了。一个 Vue 应用会将其挂载到一个 DOM 元素上 (对于这个例子是 #app) 然后对其进行完全控制。那个 HTML 是我们的入口，但其余都会发生在新创建的 Vue 实例内部。

除了文本插值，我们还可以像这样来绑定元素 attribute：

这里我们遇到了一点新东西。你看到的 v-bind attribute 被称为指令。指令带有前缀 v-，以表示它们是 Vue 提供的特殊 attribute。可能你已经猜到了，它们会在渲染的 DOM 上应用特殊的响应式行为。在这里，该指令的意思是：“将这个元素节点的 title attribute 和 Vue 实例的 message property 保持一致”。

如果你再次打开浏览器的 JavaScript 控制台，输入 app2.message = '新消息'，就会再一次看到这个绑定了 title attribute 的 HTML 已经进行了更新。

继续在控制台输入 app3.seen = false，你会发现之前显示的消息消失了。

这个例子演示了我们不仅可以把数据绑定到 DOM 文本或 attribute，还可以绑定到 DOM 结构。此外，Vue 也提供一个强大的过渡效果系统，可以在 Vue 插入/更新/移除元素时自动应用过渡效果。

还有其它很多指令，每个都有特殊的功能。例如，v-for 指令可以绑定数组的数据来渲染一个项目列表：

在控制台里，输入 app4.todos.push({ text: '新项目' })，你会发现列表最后添加了一个新项目。

为了让用户和你的应用进行交互，我们可以用 v-on 指令添加一个事件监听器，通过它调用在 Vue 实例中定义的方法：

注意在 reverseMessage 方法中，我们更新了应用的状态，但没有触碰 DOM——所有的 DOM 操作都由 Vue 来处理，你编写的代码只需要关注逻辑层面即可。

Vue 还提供了 v-model 指令，它能轻松实现表单输入和应用状态之间的双向绑定。

组件系统是 Vue 的另一个重要概念，因为它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用。仔细想想，几乎任意类型的应用界面都可以抽象为一个组件树：

在 Vue 里，一个组件本质上是一个拥有预定义选项的一个 Vue 实例。在 Vue 中注册组件很简单：

但是这样会为每个待办项渲染同样的文本，这看起来并不炫酷。我们应该能从父作用域将数据传到子组件才对。让我们来修改一下组件的定义，使之能够接受一个 prop：

现在，我们可以使用 v-bind 指令将待办项传到循环输出的每个组件中：

尽管这只是一个刻意设计的例子，但是我们已经设法将应用分割成了两个更小的单元。子单元通过 prop 接口与父单元进行了良好的解耦。我们现在可以进一步改进 <todo-item> 组件，提供更为复杂的模板和逻辑，而不会影响到父单元。

在一个大型应用中，有必要将整个应用程序划分为组件，以使开发更易管理。在后续教程中我们将详述组件，不过这里有一个 (假想的) 例子，以展示使用了组件的应用模板是什么样的：

你可能已经注意到 Vue 组件非常类似于自定义元素——它是 Web 组件规范的一部分，这是因为 Vue 的组件语法部分参考了该规范。例如 Vue 组件实现了 Slot API 与 is attribute。但是，还是有几个关键差别：

Web Components 规范已经完成并通过，但未被所有浏览器原生实现。目前 Safari 10.1+、Chrome 54+ 和 Firefox 63+ 原生支持 Web Components。相比之下，Vue 组件不需要任何 polyfill，并且在所有支持的浏览器 (IE9 及更高版本) 之下表现一致。必要时，Vue 组件也可以包装于原生自定义元素之内。

Vue 组件提供了纯自定义元素所不具备的一些重要功能，最突出的是跨组件数据流、自定义事件通信以及构建工具集成。

虽然 Vue 内部没有使用自定义元素，不过在应用使用自定义元素、或以自定义元素形式发布时，依然有很好的互操作性。Vue CLI 也支持将 Vue 组件构建成为原生的自定义元素。

我们刚才简单介绍了 Vue 核心最基本的功能——本教程的其余部分将更加详细地涵盖这些功能以及其它高级功能，所以请务必读完整个教程！

**Examples:**

Example 1 (unknown):
```unknown
<!-- 开发环境版本，包含了有帮助的命令行警告 --><script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

Example 2 (unknown):
```unknown
<!-- 生产环境版本，优化了尺寸和速度 --><script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

Example 3 (unknown):
```unknown
<div id="app">  {{ message }}</div>
```

Example 4 (unknown):
```unknown
var app = new Vue({  el: '#app',  data: {    message: 'Hello Vue!'  }})
```

---

## 介绍 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/

**Contents:**
- 介绍
- Vue.js 是什么
- 起步
- 声明式渲染
- 条件与循环
- 处理用户输入
- 组件化应用构建
  - 与自定义元素的关系
- 准备好了吗？

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue (读音 /vjuː/，类似于 view) 是一套用于构建用户界面的渐进式框架。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

如果你想在深入学习 Vue 之前对它有更多了解，我们制作了一个视频，带您了解其核心概念和一个示例工程。

如果你已经是有经验的前端开发者，想知道 Vue 与其它库/框架有哪些区别，请查看对比其它框架。

官方指南假设你已了解关于 HTML、CSS 和 JavaScript 的中级知识。如果你刚开始学习前端开发，将框架作为你的第一步可能不是最好的主意——掌握好基础知识再来吧！之前有其它框架的使用经验会有帮助，但这不是必需的。

尝试 Vue.js 最简单的方法是使用 Hello World 例子。你可以在浏览器新标签页中打开它，跟着例子学习一些基础用法。或者你也可以创建一个 .html 文件，然后通过如下方式引入 Vue：

安装教程给出了更多安装 Vue 的方式。请注意我们不推荐新手直接使用 vue-cli，尤其是在你还不熟悉基于 Node.js 的构建工具时。

如果你喜欢交互式的东西，你也可以查阅这个 Scrimba 上的系列教程，它揉合了录屏和代码试验田，并允许你随时暂停和播放。

Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：

我们已经成功创建了第一个 Vue 应用！看起来这跟渲染一个字符串模板非常类似，但是 Vue 在背后做了大量工作。现在数据和 DOM 已经被建立了关联，所有东西都是响应式的。我们要怎么确认呢？打开你的浏览器的 JavaScript 控制台 (就在这个页面打开)，并修改 app.message 的值，你将看到上例相应地更新。

注意我们不再和 HTML 直接交互了。一个 Vue 应用会将其挂载到一个 DOM 元素上 (对于这个例子是 #app) 然后对其进行完全控制。那个 HTML 是我们的入口，但其余都会发生在新创建的 Vue 实例内部。

除了文本插值，我们还可以像这样来绑定元素 attribute：

这里我们遇到了一点新东西。你看到的 v-bind attribute 被称为指令。指令带有前缀 v-，以表示它们是 Vue 提供的特殊 attribute。可能你已经猜到了，它们会在渲染的 DOM 上应用特殊的响应式行为。在这里，该指令的意思是：“将这个元素节点的 title attribute 和 Vue 实例的 message property 保持一致”。

如果你再次打开浏览器的 JavaScript 控制台，输入 app2.message = '新消息'，就会再一次看到这个绑定了 title attribute 的 HTML 已经进行了更新。

继续在控制台输入 app3.seen = false，你会发现之前显示的消息消失了。

这个例子演示了我们不仅可以把数据绑定到 DOM 文本或 attribute，还可以绑定到 DOM 结构。此外，Vue 也提供一个强大的过渡效果系统，可以在 Vue 插入/更新/移除元素时自动应用过渡效果。

还有其它很多指令，每个都有特殊的功能。例如，v-for 指令可以绑定数组的数据来渲染一个项目列表：

在控制台里，输入 app4.todos.push({ text: '新项目' })，你会发现列表最后添加了一个新项目。

为了让用户和你的应用进行交互，我们可以用 v-on 指令添加一个事件监听器，通过它调用在 Vue 实例中定义的方法：

注意在 reverseMessage 方法中，我们更新了应用的状态，但没有触碰 DOM——所有的 DOM 操作都由 Vue 来处理，你编写的代码只需要关注逻辑层面即可。

Vue 还提供了 v-model 指令，它能轻松实现表单输入和应用状态之间的双向绑定。

组件系统是 Vue 的另一个重要概念，因为它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用。仔细想想，几乎任意类型的应用界面都可以抽象为一个组件树：

在 Vue 里，一个组件本质上是一个拥有预定义选项的一个 Vue 实例。在 Vue 中注册组件很简单：

但是这样会为每个待办项渲染同样的文本，这看起来并不炫酷。我们应该能从父作用域将数据传到子组件才对。让我们来修改一下组件的定义，使之能够接受一个 prop：

现在，我们可以使用 v-bind 指令将待办项传到循环输出的每个组件中：

尽管这只是一个刻意设计的例子，但是我们已经设法将应用分割成了两个更小的单元。子单元通过 prop 接口与父单元进行了良好的解耦。我们现在可以进一步改进 <todo-item> 组件，提供更为复杂的模板和逻辑，而不会影响到父单元。

在一个大型应用中，有必要将整个应用程序划分为组件，以使开发更易管理。在后续教程中我们将详述组件，不过这里有一个 (假想的) 例子，以展示使用了组件的应用模板是什么样的：

你可能已经注意到 Vue 组件非常类似于自定义元素——它是 Web 组件规范的一部分，这是因为 Vue 的组件语法部分参考了该规范。例如 Vue 组件实现了 Slot API 与 is attribute。但是，还是有几个关键差别：

Web Components 规范已经完成并通过，但未被所有浏览器原生实现。目前 Safari 10.1+、Chrome 54+ 和 Firefox 63+ 原生支持 Web Components。相比之下，Vue 组件不需要任何 polyfill，并且在所有支持的浏览器 (IE9 及更高版本) 之下表现一致。必要时，Vue 组件也可以包装于原生自定义元素之内。

Vue 组件提供了纯自定义元素所不具备的一些重要功能，最突出的是跨组件数据流、自定义事件通信以及构建工具集成。

虽然 Vue 内部没有使用自定义元素，不过在应用使用自定义元素、或以自定义元素形式发布时，依然有很好的互操作性。Vue CLI 也支持将 Vue 组件构建成为原生的自定义元素。

我们刚才简单介绍了 Vue 核心最基本的功能——本教程的其余部分将更加详细地涵盖这些功能以及其它高级功能，所以请务必读完整个教程！

**Examples:**

Example 1 (unknown):
```unknown
<!-- 开发环境版本，包含了有帮助的命令行警告 --><script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

Example 2 (unknown):
```unknown
<!-- 生产环境版本，优化了尺寸和速度 --><script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

Example 3 (unknown):
```unknown
<div id="app">  {{ message }}</div>
```

Example 4 (unknown):
```unknown
var app = new Vue({  el: '#app',  data: {    message: 'Hello Vue!'  }})
```

---

## 计算属性和侦听器 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/computed.html

**Contents:**
- 计算属性和侦听器
- 计算属性
  - 基础例子
  - 计算属性缓存 vs 方法
  - 计算属性 vs 侦听属性
  - 计算属性的 setter
- 侦听器

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

模板内的表达式非常便利，但是设计它们的初衷是用于简单运算的。在模板中放入太多的逻辑会让模板过重且难以维护。例如：

在这个地方，模板不再是简单的声明式逻辑。你必须看一段时间才能意识到，这里是想要显示变量 message 的翻转字符串。当你想要在模板中的多处包含此翻转字符串时，就会更加难以处理。

所以，对于任何复杂逻辑，你都应当使用计算属性。

Original message: "{{ message }}"

Computed reversed message: "{{ reversedMessage }}"

这里我们声明了一个计算属性 reversedMessage。我们提供的函数将用作 property vm.reversedMessage 的 getter 函数：

你可以打开浏览器的控制台，自行修改例子中的 vm。vm.reversedMessage 的值始终取决于 vm.message 的值。

你可以像绑定普通 property 一样在模板中绑定计算属性。Vue 知道 vm.reversedMessage 依赖于 vm.message，因此当 vm.message 发生改变时，所有依赖 vm.reversedMessage 的绑定也会更新。而且最妙的是我们已经以声明的方式创建了这种依赖关系：计算属性的 getter 函数是没有副作用 (side effect) 的，这使它更易于测试和理解。

你可能已经注意到我们可以通过在表达式中调用方法来达到同样的效果：

我们可以将同一函数定义为一个方法而不是一个计算属性。两种方式的最终结果确实是完全相同的。然而，不同的是计算属性是基于它们的响应式依赖进行缓存的。只在相关响应式依赖发生改变时它们才会重新求值。这就意味着只要 message 还没有发生改变，多次访问 reversedMessage 计算属性会立即返回之前的计算结果，而不必再次执行函数。

这也同样意味着下面的计算属性将不再更新，因为 Date.now() 不是响应式依赖：

相比之下，每当触发重新渲染时，调用方法将总会再次执行函数。

我们为什么需要缓存？假设我们有一个性能开销比较大的计算属性 A，它需要遍历一个巨大的数组并做大量的计算。然后我们可能有其他的计算属性依赖于 A。如果没有缓存，我们将不可避免的多次执行 A 的 getter！如果你不希望有缓存，请用方法来替代。

Vue 提供了一种更通用的方式来观察和响应 Vue 实例上的数据变动：侦听属性。当你有一些数据需要随着其它数据变动而变动时，你很容易滥用 watch——特别是如果你之前使用过 AngularJS。然而，通常更好的做法是使用计算属性而不是命令式的 watch 回调。细想一下这个例子：

上面代码是命令式且重复的。将它与计算属性的版本进行比较：

计算属性默认只有 getter，不过在需要时你也可以提供一个 setter：

现在再运行 vm.fullName = 'John Doe' 时，setter 会被调用，vm.firstName 和 vm.lastName 也会相应地被更新。

虽然计算属性在大多数情况下更合适，但有时也需要一个自定义的侦听器。这就是为什么 Vue 通过 watch 选项提供了一个更通用的方法，来响应数据的变化。当需要在数据变化时执行异步或开销较大的操作时，这个方式是最有用的。

Ask a yes/no question:

在这个示例中，使用 watch 选项允许我们执行异步操作 (访问一个 API)，限制我们执行该操作的频率，并在我们得到最终结果前，设置中间状态。这些都是计算属性无法做到的。

除了 watch 选项之外，您还可以使用命令式的 vm.$watch API。

**Examples:**

Example 1 (unknown):
```unknown
<div id="example">  {{ message.split('').reverse().join('') }}</div>
```

Example 2 (unknown):
```unknown
<div id="example">  <p>Original message: "{{ message }}"</p>  <p>Computed reversed message: "{{ reversedMessage }}"</p></div>
```

Example 3 (unknown):
```unknown
var vm = new Vue({  el: '#example',  data: {    message: 'Hello'  },  computed: {    // 计算属性的 getter    reversedMessage: function () {      // `this` 指向 vm 实例      return this.message.split('').reverse().join('')    }  }})
```

Example 4 (javascript):
```javascript
console.log(vm.reversedMessage) // => 'olleH'vm.message = 'Goodbye'console.log(vm.reversedMessage) // => 'eybdooG'
```

---

## 加入 Vue.js 社区 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/join.html

**Contents:**
- 加入 Vue.js 社区
- 您将享有的资源
  - 行为规范
  - 获取帮助
  - 探索生态
- 您可以参与的方式
  - 贡献代码
  - 分享 (并积累) 您的经验
  - 翻译文档
  - 成为社区领袖

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue.js 的社区正在急速增长中，如果你正在阅读本文，这说明你大概已经准备好加入 Vue.js 社区了。欢迎！

现在让我们来解答你能从社区中获得什么以及你能为社区做什么。

这份行为规范是一个指南，它易于让我们所参与的技术社区更加繁荣。

和所有的项目一样，贡献代码需要遵循规范。为了保证我们能尽快地帮助你解决问题或者接受你的 pull request，请先阅读这份贡献指南。

阅读之后，你应该已经准备好向 Vue 的核心仓库贡献代码了：

除了在论坛或聊天室回答问题、分享资源外，还有一些其它的方式可以分享并增长你的见识：

Vue 已经在全球范围内传播开来，核心团队成员甚至来自至少 6 个时区。论坛已有 7 种语言，数字还在持续增长。我们许多文档都有积极维护的翻译。我们非常为 Vue 的国际影响力骄傲，但我们还能做得更好。

我希望现在你正在使用你的首选语言阅读这篇文档，如果不是，你愿意帮助我们翻译它吗？

如果你愿意的话，请随时 fork 这些文档或者官方维护的其他文档的仓库，然后开始翻译吧。只要你取得了进展，就请在主仓库开一个 issue 或者 pull request，我们将号召更多的贡献者来进行帮助。

在社区中，你可以做很多事情来帮助 Vue 的发展：

对于如何参与当地的 Vue 社区，如果你有任何问题，请联系 @Vuejs_Events！

---

## 单文件组件 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/single-file-components.html

**Contents:**
- 单文件组件
- 介绍
  - 怎么看待关注点分离？
- 起步
  - 例子沙箱
  - 针对刚接触 JavaScript 模块开发系统的用户
  - 针对高级用户

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

在很多 Vue 项目中，我们使用 Vue.component 来定义全局组件，紧接着用 new Vue({ el: '#container '}) 在每个页面内指定一个容器元素。

这种方式在很多中小规模的项目中运作的很好，在这些项目里 JavaScript 只被用来加强特定的视图。但当在更复杂的项目中，或者你的前端完全由 JavaScript 驱动的时候，下面这些缺点将变得非常明显：

文件扩展名为 .vue 的 single-file components (单文件组件) 为以上所有问题提供了解决方法，并且还可以使用 webpack 或 Browserify 等构建工具。

这是一个文件名为 Hello.vue 的简单实例：

正如我们说过的，我们可以使用预处理器来构建简洁和功能更丰富的组件，比如 Pug，Babel (with ES2015 modules)，和 Stylus。

这些特定的语言只是例子，你可以只是简单地使用 Babel，TypeScript，SCSS，PostCSS - 或者其他任何能够帮助你提高生产力的预处理器。如果搭配 vue-loader 使用 webpack，它也能为 CSS Modules 提供头等支持。

一个重要的事情值得注意，关注点分离不等于文件类型分离。在现代 UI 开发中，我们已经发现相比于把代码库分离成三个大的层次并将其相互交织起来，把它们划分为松散耦合的组件再将其组合起来更合理一些。在一个组件里，其模板、逻辑和样式是内部耦合的，并且把他们搭配在一起实际上使得组件更加内聚且更可维护。

即便你不喜欢单文件组件，你仍然可以把 JavaScript、CSS 分离成独立的文件然后做到热重载和预编译。

如果你希望深入了解并开始使用单文件组件，请来 CodeSandbox 看看这个简单的 todo 应用。

有了 .vue 组件，我们就进入了高级 JavaScript 应用领域。如果你没有准备好的话，意味着还需要学会使用一些附加的工具：

Node Package Manager (NPM)：阅读 Getting Started guide 中关于如何从注册地 (registry) 获取包的章节。

Modern JavaScript with ES2015/16：阅读 Babel 的 Learn ES2015 guide。你不需要立刻记住每一个方法，但是你可以保留这个页面以便后期参考。

在你花一天时间了解这些资源之后，我们建议你参考 Vue CLI 3。只要遵循指示，你就能很快地运行一个带有 .vue 组件、ES2015、webpack 和热重载 (hot-reloading) 的 Vue 项目！

CLI 会为你搞定大多数工具的配置问题，同时也支持细粒度自定义配置项。

有时你会想从零搭建你自己的构建工具，这时你需要通过 Vue Loader 手动配置 webpack。关于学习更多 webpack 的内容，请查阅其官方文档和 Webpack Academy。

**Examples:**

Example 1 (unknown):
```unknown
<!-- my-component.vue --><template>  <div>This will be pre-compiled</div></template><script src="./my-component.js"></script><style src="./my-component.css"></style>
```

---

## 表单输入绑定 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/forms.html

**Contents:**
- 表单输入绑定
- 基础用法
  - 文本
  - 多行文本
  - 复选框
  - 单选按钮
  - 选择框
- 值绑定
  - 复选框
  - 单选按钮

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

你可以用 v-model 指令在表单 <input>、<textarea> 及 <select> 元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。尽管有些神奇，但 v-model 本质上不过是语法糖。它负责监听用户的输入事件以更新数据，并对一些极端场景进行一些特殊处理。

v-model 会忽略所有表单元素的 value、checked、selected attribute 的初始值而总是将 Vue 实例的数据作为数据来源。你应该通过 JavaScript 在组件的 data 选项中声明初始值。

v-model 在内部为不同的输入元素使用不同的 property 并抛出不同的事件：

对于需要使用输入法 (如中文、日文、韩文等) 的语言，你会发现 v-model 不会在输入法组合文字过程中得到更新。如果你也想处理这个过程，请使用 input 事件。

Message is: {{ message }}

在文本区域插值 (<textarea>{{text}}</textarea>) 并不会生效，应用 v-model 来代替。

如果 v-model 表达式的初始值未能匹配任何选项，<select> 元素将被渲染为“未选中”状态。在 iOS 中，这会使用户无法选择第一个选项。因为这样的情况下，iOS 不会触发 change 事件。因此，更推荐像上面这样提供一个值为空的禁用选项。

对于单选按钮，复选框及选择框的选项，v-model 绑定的值通常是静态字符串 (对于复选框也可以是布尔值)：

但是有时我们可能想把值绑定到 Vue 实例的一个动态 property 上，这时可以用 v-bind 实现，并且这个 property 的值可以不是字符串。

这里的 true-value 和 false-value attribute 并不会影响输入控件的 value attribute，因为浏览器在提交表单时并不会包含未被选中的复选框。如果要确保表单中这两个值中的一个能够被提交，(即“yes”或“no”)，请换用单选按钮。

在默认情况下，v-model 在每次 input 事件触发后将输入框的值与数据进行同步 (除了上述输入法组合文字时)。你可以添加 lazy 修饰符，从而转为在 change 事件之后进行同步：

如果想自动将用户的输入值转为数值类型，可以给 v-model 添加 number 修饰符：

这通常很有用，因为即使在 type="number" 时，HTML 输入元素的值也总会返回字符串。如果这个值无法被 parseFloat() 解析，则会返回原始的值。

如果要自动过滤用户输入的首尾空白字符，可以给 v-model 添加 trim 修饰符：

如果你还不熟悉 Vue 的组件，可以暂且跳过这里。

HTML 原生的输入元素类型并不总能满足需求。幸好，Vue 的组件系统允许你创建具有完全自定义行为且可复用的输入组件。这些输入组件甚至可以和 v-model 一起使用！

要了解更多，请参阅组件指南中的自定义输入组件。

**Examples:**

Example 1 (unknown):
```unknown
<input v-model="message" placeholder="edit me"><p>Message is: {{ message }}</p>
```

Example 2 (unknown):
```unknown
<span>Multiline message is:</span><p style="white-space: pre-line;">{{ message }}</p><br><textarea v-model="message" placeholder="add multiple lines"></textarea>
```

Example 3 (unknown):
```unknown
<input type="checkbox" id="checkbox" v-model="checked"><label for="checkbox">{{ checked }}</label>
```

Example 4 (unknown):
```unknown
<input type="checkbox" id="jack" value="Jack" v-model="checkedNames"><label for="jack">Jack</label><input type="checkbox" id="john" value="John" v-model="checkedNames"><label for="john">John</label><input type="checkbox" id="mike" value="Mike" v-model="checkedNames"><label for="mike">Mike</label><br><span>Checked names: {{ checkedNames }}</span>
```

---
