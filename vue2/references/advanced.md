# Vue2 - Advanced

**Pages:** 8

---

## 渲染函数 & JSX — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/render-function.html

**Contents:**
- 渲染函数 & JSX
- 基础
- 节点、树以及虚拟 DOM
  - 虚拟 DOM
- createElement 参数
  - 深入数据对象
  - 完整示例
  - 约束
    - VNode 必须唯一
- 使用 JavaScript 代替模板功能

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue 推荐在绝大多数情况下使用模板来创建你的 HTML。然而在一些场景中，你真的需要 JavaScript 的完全编程的能力。这时你可以用渲染函数，它比模板更接近编译器。

让我们深入一个简单的例子，这个例子里 render 函数很实用。假设我们要生成一些带锚点的标题：

对于上面的 HTML，你决定这样定义组件接口：

当开始写一个只能通过 level prop 动态生成标题 (heading) 的组件时，你可能很快想到这样实现：

这里用模板并不是最好的选择：不但代码冗长，而且在每一个级别的标题中重复书写了 <slot></slot>，在要插入锚点元素时还要再次重复。

虽然模板在大多数组件中都非常好用，但是显然在这里它就不合适了。那么，我们来尝试使用 render 函数重写上面的例子：

看起来简单多了！这样代码精简很多，但是需要非常熟悉 Vue 的实例 property。在这个例子中，你需要知道，向组件中传递不带 v-slot 指令的子节点时，比如 anchored-heading 中的 Hello world!，这些子节点被存储在组件实例中的 $slots.default 中。如果你还不了解，在深入渲染函数之前推荐阅读实例 property API。

在深入渲染函数之前，了解一些浏览器的工作原理是很重要的。以下面这段 HTML 为例：

当浏览器读到这些代码时，它会建立一个“DOM 节点”树来保持追踪所有内容，如同你会画一张家谱树来追踪家庭成员的发展一样。

上述 HTML 对应的 DOM 节点树如下图所示：

每个元素都是一个节点。每段文字也是一个节点。甚至注释也都是节点。一个节点就是页面的一个部分。就像家谱树一样，每个节点都可以有孩子节点 (也就是说每个部分可以包含其它的一些部分)。

高效地更新所有这些节点会是比较困难的，不过所幸你不必手动完成这个工作。你只需要告诉 Vue 你希望页面上的 HTML 是什么，这可以是在一个模板里：

在这两种情况下，Vue 都会自动保持页面的更新，即便 blogTitle 发生了改变。

Vue 通过建立一个虚拟 DOM 来追踪自己要如何改变真实 DOM。请仔细看这行代码：

createElement 到底会返回什么呢？其实不是一个实际的 DOM 元素。它更准确的名字可能是 createNodeDescription，因为它所包含的信息会告诉 Vue 页面上需要渲染什么样的节点，包括及其子节点的描述信息。我们把这样的节点描述为“虚拟节点 (virtual node)”，也常简写它为“VNode”。“虚拟 DOM”是我们对由 Vue 组件树建立起来的整个 VNode 树的称呼。

接下来你需要熟悉的是如何在 createElement 函数中使用模板中的那些功能。这里是 createElement 接受的参数：

有一点要注意：正如 v-bind:class 和 v-bind:style 在模板语法中会被特别对待一样，它们在 VNode 数据对象中也有对应的顶层字段。该对象也允许你绑定普通的 HTML attribute，也允许绑定如 innerHTML 这样的 DOM property (这会覆盖 v-html 指令)。

有了这些知识，我们现在可以完成我们最开始想实现的组件：

组件树中的所有 VNode 必须是唯一的。这意味着，下面的渲染函数是不合法的：

如果你真的需要重复很多次的元素/组件，你可以使用工厂函数来实现。例如，下面这渲染函数用完全合法的方式渲染了 20 个相同的段落：

只要在原生的 JavaScript 中可以轻松完成的操作，Vue 的渲染函数就不会提供专有的替代方法。比如，在模板中使用的 v-if 和 v-for：

这些都可以在渲染函数中用 JavaScript 的 if/else 和 map 来重写：

渲染函数中没有与 v-model 的直接对应——你必须自己实现相应的逻辑：

这就是深入底层的代价，但与 v-model 相比，这可以让你更好地控制交互细节。

对于 .passive、.capture 和 .once 这些事件修饰符，Vue 提供了相应的前缀可以用于 on：

对于所有其它的修饰符，私有前缀都不是必须的，因为你可以在事件处理函数中使用事件方法：

你可以通过 this.$slots 访问静态插槽的内容，每个插槽都是一个 VNode 数组：

也可以通过 this.$scopedSlots 访问作用域插槽，每个作用域插槽都是一个返回若干 VNode 的函数：

如果要用渲染函数向子组件中传递作用域插槽，可以利用 VNode 数据对象中的 scopedSlots 字段：

如果你写了很多 render 函数，可能会觉得下面这样的代码写起来很痛苦：

这就是为什么会有一个 Babel 插件，用于在 Vue 中使用 JSX 语法，它可以让我们回到更接近于模板的语法上。

将 h 作为 createElement 的别名是 Vue 生态系统中的一个通用惯例，实际上也是 JSX 所要求的。从 Vue 的 Babel 插件的 3.4.0 版本开始，我们会在以 ES2015 语法声明的含有 JSX 的任何方法和 getter 中 (不是函数或箭头函数中) 自动注入 const h = this.$createElement，这样你就可以去掉 (h) 参数了。对于更早版本的插件，如果 h 在当前作用域中不可用，应用会抛错。

要了解更多关于 JSX 如何映射到 JavaScript，请阅读使用文档。

之前创建的锚点标题组件是比较简单，没有管理任何状态，也没有监听任何传递给它的状态，也没有生命周期方法。实际上，它只是一个接受一些 prop 的函数。在这样的场景下，我们可以将组件标记为 functional，这意味它无状态 (没有响应式数据)，也没有实例 (没有 this 上下文)。一个函数式组件就像这样：

注意：在 2.3.0 之前的版本中，如果一个函数式组件想要接收 prop，则 props 选项是必须的。在 2.3.0 或以上的版本中，你可以省略 props 选项，所有组件上的 attribute 都会被自动隐式解析为 prop。

当使用函数式组件时，该引用将会是 HTMLElement，因为他们是无状态的也是无实例的。

在 2.5.0 及以上版本中，如果你使用了单文件组件，那么基于模板的函数式组件可以这样声明：

组件需要的一切都是通过 context 参数传递，它是一个包括如下字段的对象：

在添加 functional: true 之后，需要更新我们的锚点标题组件的渲染函数，为其增加 context 参数，并将 this.$slots.default 更新为 context.children，然后将 this.level 更新为 context.props.level。

因为函数式组件只是函数，所以渲染开销也低很多。

在作为包装组件时它们也同样非常有用。比如，当你需要做这些时：

下面是一个 smart-list 组件的例子，它能根据传入 prop 的值来代为渲染更具体的组件：

在普通组件中，没有被定义为 prop 的 attribute 会自动添加到组件的根元素上，将已有的同名 attribute 进行替换或与其进行智能合并。

通过向 createElement 传入 context.data 作为第二个参数，我们就把 my-functional-button 上面所有的 attribute 和事件监听器都传递下去了。事实上这是非常透明的，以至于那些事件甚至并不要求 .native 修饰符。

如果你使用基于模板的函数式组件，那么你还需要手动添加 attribute 和监听器。因为我们可以访问到其独立的上下文内容，所以我们可以使用 data.attrs 传递任何 HTML attribute，也可以使用 listeners (即 data.on 的别名) 传递任何事件监听器。

你可能想知道为什么同时需要 slots() 和 children。slots().default 不是和 children 类似的吗？在一些场景中，是这样——但如果是如下的带有子节点的函数式组件呢？

对于这个组件，children 会给你两个段落标签，而 slots().default 只会传递第二个匿名段落标签，slots().foo 会传递第一个具名段落标签。同时拥有 children 和 slots()，因此你可以选择让组件感知某个插槽机制，还是简单地通过传递 children，移交给其它组件去处理。

你可能会有兴趣知道，Vue 的模板实际上被编译成了渲染函数。这是一个实现细节，通常不需要关心。但如果你想看看模板的功能具体是怎样被编译的，可能会发现会非常有意思。下面是一个使用 Vue.compile 来实时编译模板字符串的简单示例：

**Examples:**

Example 1 (unknown):
```unknown
<h1>  <a name="hello-world" href="#hello-world">    Hello world!  </a></h1>
```

Example 2 (unknown):
```unknown
<anchored-heading :level="1">Hello world!</anchored-heading>
```

Example 3 (unknown):
```unknown
<script type="text/x-template" id="anchored-heading-template">  <h1 v-if="level === 1">    <slot></slot>  </h1>  <h2 v-else-if="level === 2">    <slot></slot>  </h2>  <h3 v-else-if="level === 3">    <slot></slot>  </h3>  <h4 v-else-if="level === 4">    <slot></slot>  </h4>  <h5 v-else-if="level === 5">    <slot></slot>  </h5>  <h6 v-else-if="level === 6">    <slot></slot>  </h6></script>
```

Example 4 (unknown):
```unknown
Vue.component('anchored-heading', {  template: '#anchored-heading-template',  props: {    level: {      type: Number,      required: true    }  }})
```

---

## 过滤器 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/filters.html

**Contents:**
- 过滤器

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue.js 允许你自定义过滤器，可被用于一些常见的文本格式化。过滤器可以用在两个地方：双花括号插值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：

你可以在一个组件的选项中定义本地的过滤器：

或者在创建 Vue 实例之前全局定义过滤器：

当全局过滤器和局部过滤器重名时，会采用局部过滤器。

下面这个例子用到了 capitalize 过滤器：

{{ message | capitalize }}

过滤器函数总接收表达式的值 (之前的操作链的结果) 作为第一个参数。在上述例子中，capitalize 过滤器函数将会收到 message 的值作为第一个参数。

在这个例子中，filterA 被定义为接收单个参数的过滤器函数，表达式 message 的值将作为参数传入到函数中。然后继续调用同样被定义为接收单个参数的过滤器函数 filterB，将 filterA 的结果传递到 filterB 中。

过滤器是 JavaScript 函数，因此可以接收参数：

这里，filterA 被定义为接收三个参数的过滤器函数。其中 message 的值作为第一个参数，普通字符串 'arg1' 作为第二个参数，表达式 arg2 的值作为第三个参数。

**Examples:**

Example 1 (unknown):
```unknown
<!-- 在双花括号中 -->{{ message | capitalize }}<!-- 在 `v-bind` 中 --><div v-bind:id="rawId | formatId"></div>
```

Example 2 (unknown):
```unknown
filters: {  capitalize: function (value) {    if (!value) return ''    value = value.toString()    return value.charAt(0).toUpperCase() + value.slice(1)  }}
```

Example 3 (unknown):
```unknown
Vue.filter('capitalize', function (value) {  if (!value) return ''  value = value.toString()  return value.charAt(0).toUpperCase() + value.slice(1)})new Vue({  // ...})
```

Example 4 (unknown):
```unknown
{{ message | filterA | filterB }}
```

---

## 路由 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/routing.html

**Contents:**
- 路由
- 官方路由
- 从零开始简单的路由
- 整合第三方路由

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

对于大多数单页面应用，都推荐使用官方支持的 vue-router 库。更多细节可以移步 vue-router 文档。

如果你只需要非常简单的路由而不想引入一个功能完整的路由库，可以像这样动态渲染一个页面级的组件：

结合 HTML5 History API，你可以建立一个麻雀虽小但是五脏俱全的客户端路由器。可以直接看实例应用。

如果你有更偏爱的第三方路由，如 Page.js 或者 Director，整合起来也一样简单。这里有一个使用了 Page.js 的完整示例。

**Examples:**

Example 1 (javascript):
```javascript
const NotFound = { template: '<p>Page not found</p>' }const Home = { template: '<p>home page</p>' }const About = { template: '<p>about page</p>' }const routes = {  '/': Home,  '/about': About}new Vue({  el: '#app',  data: {    currentRoute: window.location.pathname  },  computed: {    ViewComponent () {      return routes[this.currentRoute] || NotFound    }  },  render (h) { return h(this.ViewComponent) }})
```

---

## 混入 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/mixins.html

**Contents:**
- 混入
- 基础
- 选项合并
- 全局混入
- 自定义选项合并策略

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

混入 (mixin) 提供了一种非常灵活的方式，来分发 Vue 组件中的可复用功能。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。

当组件和混入对象含有同名选项时，这些选项将以恰当的方式进行“合并”。

比如，数据对象在内部会进行递归合并，并在发生冲突时以组件数据优先。

同名钩子函数将合并为一个数组，因此都将被调用。另外，混入对象的钩子将在组件自身钩子之前调用。

值为对象的选项，例如 methods、components 和 directives，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对。

注意：Vue.extend() 也使用同样的策略进行合并。

混入也可以进行全局注册。使用时格外小心！一旦使用全局混入，它将影响每一个之后创建的 Vue 实例。使用恰当时，这可以用来为自定义选项注入处理逻辑。

请谨慎使用全局混入，因为它会影响每个单独创建的 Vue 实例 (包括第三方组件)。大多数情况下，只应当应用于自定义选项，就像上面示例一样。推荐将其作为插件发布，以避免重复应用混入。

自定义选项将使用默认策略，即简单地覆盖已有值。如果想让自定义选项以自定义逻辑合并，可以向 Vue.config.optionMergeStrategies 添加一个函数：

对于多数值为对象的选项，可以使用与 methods 相同的合并策略：

可以在 Vuex 1.x 的混入策略里找到一个更高级的例子：

**Examples:**

Example 1 (javascript):
```javascript
// 定义一个混入对象var myMixin = {  created: function () {    this.hello()  },  methods: {    hello: function () {      console.log('hello from mixin!')    }  }}// 定义一个使用混入对象的组件var Component = Vue.extend({  mixins: [myMixin]})var component = new Component() // => "hello from mixin!"
```

Example 2 (javascript):
```javascript
var mixin = {  data: function () {    return {      message: 'hello',      foo: 'abc'    }  }}new Vue({  mixins: [mixin],  data: function () {    return {      message: 'goodbye',      bar: 'def'    }  },  created: function () {    console.log(this.$data)    // => { message: "goodbye", foo: "abc", bar: "def" }  }})
```

Example 3 (javascript):
```javascript
var mixin = {  created: function () {    console.log('混入对象的钩子被调用')  }}new Vue({  mixins: [mixin],  created: function () {    console.log('组件钩子被调用')  }})// => "混入对象的钩子被调用"// => "组件钩子被调用"
```

Example 4 (javascript):
```javascript
var mixin = {  methods: {    foo: function () {      console.log('foo')    },    conflicting: function () {      console.log('from mixin')    }  }}var vm = new Vue({  mixins: [mixin],  methods: {    bar: function () {      console.log('bar')    },    conflicting: function () {      console.log('from self')    }  }})vm.foo() // => "foo"vm.bar() // => "bar"vm.conflicting() // => "from self"
```

---

## 插件 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/plugins.html

**Contents:**
- 插件
- 使用插件
- 开发插件

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

插件通常用来为 Vue 添加全局功能。插件的功能范围没有严格的限制——一般有下面几种：

添加全局方法或者 property。如：vue-custom-element

添加全局资源：指令/过滤器/过渡等。如 vue-touch

通过全局混入来添加一些组件选项。如 vue-router

添加 Vue 实例方法，通过把它们添加到 Vue.prototype 上实现。

一个库，提供自己的 API，同时提供上面提到的一个或多个功能。如 vue-router

通过全局方法 Vue.use() 使用插件。它需要在你调用 new Vue() 启动应用之前完成：

Vue.use 会自动阻止多次注册相同插件，届时即使多次调用也只会注册一次该插件。

Vue.js 官方提供的一些插件 (例如 vue-router) 在检测到 Vue 是可访问的全局变量时会自动调用 Vue.use()。然而在像 CommonJS 这样的模块环境中，你应该始终显式地调用 Vue.use()：

awesome-vue 集合了大量由社区贡献的插件和库。

Vue.js 的插件应该暴露一个 install 方法。这个方法的第一个参数是 Vue 构造器，第二个参数是一个可选的选项对象：

**Examples:**

Example 1 (unknown):
```unknown
// 调用 `MyPlugin.install(Vue)`Vue.use(MyPlugin)new Vue({  // ...组件选项})
```

Example 2 (unknown):
```unknown
Vue.use(MyPlugin, { someOption: true })
```

Example 3 (unknown):
```unknown
// 用 Browserify 或 webpack 提供的 CommonJS 模块环境时var Vue = require('vue')var VueRouter = require('vue-router')// 不要忘了调用此方法Vue.use(VueRouter)
```

Example 4 (unknown):
```unknown
MyPlugin.install = function (Vue, options) {  // 1. 添加全局方法或 property  Vue.myGlobalMethod = function () {    // 逻辑...  }  // 2. 添加全局资源  Vue.directive('my-directive', {    bind (el, binding, vnode, oldVnode) {      // 逻辑...    }    ...  })  // 3. 注入组件选项  Vue.mixin({    created: function () {      // 逻辑...    }    ...  })  // 4. 添加实例方法  Vue.prototype.$myMethod = function (methodOptions) {    // 逻辑...  }}
```

---

## TypeScript 支持 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/typescript.html

**Contents:**
- TypeScript 支持
- 发布为 NPM 包的官方声明文件
- 推荐配置
- 开发工具链
  - 工程创建
  - 编辑器支持
- 基本用法
- 基于类的 Vue 组件
- 增强类型以配合插件使用
- 标注返回值

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue CLI 提供了内建的 TypeScript 工具支持。

静态类型系统能帮助你有效防止许多潜在的运行时错误，而且随着你的应用日渐丰满会更加显著。这就是为什么 Vue 不仅仅为 Vue core 提供了针对 TypeScript 的官方类型声明，还为 Vue Router 和 Vuex 也提供了相应的声明文件。

而且，我们已经把它们发布到了 NPM，最新版本的 TypeScript 也知道该如何自己从 NPM 包里解析类型声明。这意味着只要你成功地通过 NPM 安装了，就不再需要任何额外的工具辅助，即可在 Vue 中使用 TypeScript 了。

注意你需要引入 strict: true (或者至少 noImplicitThis: true，这是 strict 模式的一部分) 以利用组件方法中 this 的类型检查，否则它会始终被看作 any 类型。

参阅 TypeScript 编译器选项文档 (英) 了解更多。

Vue CLI 3 可以使用 TypeScript 生成新工程。创建方式：

要使用 TypeScript 开发 Vue 应用程序，我们强烈建议您使用 Visual Studio Code，它为 TypeScript 提供了极好的“开箱即用”支持。如果你正在使用单文件组件 (SFC)，可以安装提供 SFC 支持以及其他更多实用功能的 Vetur 插件。

WebStorm 同样为 TypeScript 和 Vue 提供了“开箱即用”的支持。

要让 TypeScript 正确推断 Vue 组件选项中的类型，您需要使用 Vue.component 或 Vue.extend 定义组件：

如果您在声明组件时更喜欢基于类的 API，则可以使用官方维护的 vue-class-component 装饰器：

插件可以增加 Vue 的全局/实例 property 和组件选项。在这些情况下，在 TypeScript 中制作插件需要类型声明。庆幸的是，TypeScript 有一个特性来补充现有的类型，叫做模块补充 (module augmentation)。

例如，声明一个 string 类型的实例 property $myProperty：

在你的项目中包含了上述作为声明文件的代码之后 (像 my-property.d.ts)，你就可以在 Vue 实例上使用 $myProperty 了。

你也可以声明额外的 property 和组件选项：

因为 Vue 的声明文件天生就具有循环性，TypeScript 可能在推断某个方法的类型的时候存在困难。因此，你可能需要在 render 或 computed 里的方法上标注返回值。

如果你发现类型推导或成员补齐不工作了，标注某个方法也许可以帮助你解决这个问题。使用 --noImplicitAny 选项将会帮助你找到这些未标注的方法。

如果你发现校验器并没有得到类型推导或命名补全不工作，用预期的类型标注参数可能会助你解决这类问题。

**Examples:**

Example 1 (unknown):
```unknown
// tsconfig.json{  "compilerOptions": {    // 与 Vue 的浏览器支持保持一致    "target": "es5",    // 这可以对 `this` 上的数据 property 进行更严格的推断    "strict": true,    // 如果使用 webpack 2+ 或 rollup，可以利用 tree-shake:    "module": "es2015",    "moduleResolution": "node"  }}
```

Example 2 (unknown):
```unknown
# 1. 如果没有安装 Vue CLI 就先安装npm install --global @vue/cli# 2. 创建一个新工程，并选择 "Manually select features (手动选择特性)" 选项vue create my-project-name
```

Example 3 (python):
```python
import Vue from 'vue'const Component = Vue.extend({  // 类型推断已启用})const Component = {  // 这里不会有类型推断，  // 因为 TypeScript 不能确认这是 Vue 组件的选项}
```

Example 4 (python):
```python
import Vue from 'vue'import Component from 'vue-class-component'// @Component 修饰符注明了此类为一个 Vue 组件@Component({  // 所有的组件选项都可以放在这里  template: '<button @click="onClick">Click!</button>'})export default class MyComponent extends Vue {  // 初始数据可以直接声明为实例的 property  message: string = 'Hello!'  // 组件方法也可以直接声明为实例的方法  onClick (): void {    window.alert(this.message)  }}
```

---

## 状态管理 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/state-management.html

**Contents:**
- 状态管理
- 类 Flux 状态管理的官方实现
  - React 的开发者请参考以下信息
- 简单状态管理起步使用

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

由于状态零散地分布在许多组件和组件之间的交互中，大型应用复杂度也经常逐渐增长。为了解决这个问题，Vue 提供 vuex：我们有受到 Elm 启发的状态管理库。vuex 甚至集成到 vue-devtools，无需配置即可进行时光旅行调试 (time travel debugging)。

如果你是来自 React 的开发者，你可能会对 Vuex 和 Redux 间的差异表示关注，Redux 是 React 生态环境中最流行的 Flux 实现。Redux 事实上无法感知视图层，所以它能够轻松的通过一些简单绑定和 Vue 一起使用。Vuex 区别在于它是一个专门为 Vue 应用所设计。这使得它能够更好地和 Vue 进行整合，同时提供简洁的 API 和改善过的开发体验。

经常被忽略的是，Vue 应用中原始 data 对象的实际来源——当访问数据对象时，一个 Vue 实例只是简单的代理访问。所以，如果你有一处需要被多个实例间共享的状态，可以简单地通过维护一份数据来实现共享：

现在当 sourceOfTruth 发生变更，vmA 和 vmB 都将自动地更新它们的视图。子组件们的每个实例也会通过 this.$root.$data 去访问。现在我们有了唯一的数据来源，但是，调试将会变为噩梦。任何时间，我们应用中的任何部分，在任何数据改变后，都不会留下变更过的记录。

为了解决这个问题，我们采用一个简单的 store 模式：

需要注意，所有 store 中 state 的变更，都放置在 store 自身的 action 中去管理。这种集中式状态管理能够被更容易地理解哪种类型的变更将会发生，以及它们是如何被触发。当错误出现时，我们现在也会有一个 log 记录 bug 之前发生了什么。

此外，每个实例/组件仍然可以拥有和管理自己的私有状态：

重要的是，注意你不应该在 action 中 替换原始的状态对象 - 组件和 store 需要引用同一个共享对象，变更才能够被观察到。

接着我们继续延伸约定，组件不允许直接变更属于 store 实例的 state，而应执行 action 来分发 (dispatch) 事件通知 store 去改变，我们最终达成了 Flux 架构。这样约定的好处是，我们能够记录所有 store 中发生的 state 变更，同时实现能做到记录变更、保存状态快照、历史回滚/时光旅行的先进的调试工具。

说了一圈其实又回到了 Vuex，如果你已经读到这儿，或许可以去尝试一下！

**Examples:**

Example 1 (unknown):
```unknown
var sourceOfTruth = {}var vmA = new Vue({  data: sourceOfTruth})var vmB = new Vue({  data: sourceOfTruth})
```

Example 2 (unknown):
```unknown
var store = {  debug: true,  state: {    message: 'Hello!'  },  setMessageAction (newValue) {    if (this.debug) console.log('setMessageAction triggered with', newValue)    this.state.message = newValue  },  clearMessageAction () {    if (this.debug) console.log('clearMessageAction triggered')    this.state.message = ''  }}
```

Example 3 (unknown):
```unknown
var vmA = new Vue({  data: {    privateState: {},    sharedState: store.state  }})var vmB = new Vue({  data: {    privateState: {},    sharedState: store.state  }})
```

---

## 自定义指令 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/custom-directive.html

**Contents:**
- 自定义指令
- 简介
- 钩子函数
- 钩子函数参数
  - 动态指令参数
- 函数简写
- 对象字面量

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

除了核心功能默认内置的指令 (v-model 和 v-show)，Vue 也允许注册自定义指令。注意，在 Vue2.0 中，代码复用和抽象的主要形式是组件。然而，有的情况下，你仍然需要对普通 DOM 元素进行底层操作，这时候就会用到自定义指令。举个聚焦输入框的例子，如下：

当页面加载时，该元素将获得焦点 (注意：autofocus 在移动版 Safari 上不工作)。事实上，只要你在打开这个页面后还没点击过任何内容，这个输入框就应当还是处于聚焦状态。现在让我们用指令来实现这个功能：

如果想注册局部指令，组件中也接受一个 directives 的选项：

然后你可以在模板中任何元素上使用新的 v-focus property，如下：

一个指令定义对象可以提供如下几个钩子函数 (均为可选)：

bind：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置。

inserted：被绑定元素插入父节点时调用 (仅保证父节点存在，但不一定已被插入文档中)。

update：所在组件的 VNode 更新时调用，但是可能发生在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 (详细的钩子函数参数见下)。

我们会在稍后讨论渲染函数时介绍更多 VNodes 的细节。

componentUpdated：指令所在组件的 VNode 及其子 VNode 全部更新后调用。

unbind：只调用一次，指令与元素解绑时调用。

接下来我们来看一下钩子函数的参数 (即 el、binding、vnode 和 oldVnode)。

除了 el 之外，其它参数都应该是只读的，切勿进行修改。如果需要在钩子之间共享数据，建议通过元素的 dataset 来进行。

这是一个使用了这些 property 的自定义钩子样例：

指令的参数可以是动态的。例如，在 v-mydirective:[argument]="value" 中，argument 参数可以根据组件实例数据进行更新！这使得自定义指令可以在应用中被灵活使用。

例如你想要创建一个自定义指令，用来通过固定布局将元素固定在页面上。我们可以像这样创建一个通过指令值来更新竖直位置像素值的自定义指令：

这会把该元素固定在距离页面顶部 200 像素的位置。但如果场景是我们需要把元素固定在左侧而不是顶部又该怎么办呢？这时使用动态参数就可以非常方便地根据每个组件实例来进行更新。

这样这个自定义指令现在的灵活性就足以支持一些不同的用例了。

在很多时候，你可能想在 bind 和 update 时触发相同行为，而不关心其它的钩子。比如这样写：

如果指令需要多个值，可以传入一个 JavaScript 对象字面量。记住，指令函数能够接受所有合法的 JavaScript 表达式。

**Examples:**

Example 1 (unknown):
```unknown
// 注册一个全局自定义指令 `v-focus`Vue.directive('focus', {  // 当被绑定的元素插入到 DOM 中时……  inserted: function (el) {    // 聚焦元素    el.focus()  }})
```

Example 2 (unknown):
```unknown
directives: {  focus: {    // 指令的定义    inserted: function (el) {      el.focus()    }  }}
```

Example 3 (unknown):
```unknown
<input v-focus>
```

Example 4 (unknown):
```unknown
<div id="hook-arguments-example" v-demo:foo.a.b="message"></div>
```

---
