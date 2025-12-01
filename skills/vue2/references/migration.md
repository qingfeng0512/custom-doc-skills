# Vue2 - Migration

**Pages:** 4

---

## 从 Vue 1.x 迁移 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/migration.html

**Contents:**
- 从 Vue 1.x 迁移
- FAQ
- 模板
  - 片段实例移除
    - 升级方式
- 生命周期钩子函数
  - beforeCompile 移除
    - 升级方式
  - compiled 替换
    - 升级方式

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

哇，非常长的一页！是否意味着 Vue 2.0 已经完全不同了呢，是否需要从头学起呢，Vue 1.0 的项目是不是没法迁移了？

非常开心地告诉你，并不是！几乎 90% 的 API 和核心概念都没有变。因为本节包含了很多详尽的阐述以及许多迁移的例子，所以显得有点长。不用担心，你不必从头到尾把本节读一遍！

首先，在当前项目下运行迁移工具。我们非常谨慎地把高级 Vue 升级过程简化为使用一个简单的命令行工具。当工具识别出旧有的特性后，就会告知你并给出建议，同时附上关于详细信息的链接。

然后，浏览本页面的侧边栏列出的内容。如果发现有的标题对你的项目有影响，但是迁移工具没有给出提示，请检查自己的项目。

如果你的项目有测试代码，运行并查看仍然失败的地方。如果没有测试代码，在浏览器中打开你的程序，通过导航环顾并留意那些报错或警告信息。

现在，你的应用程序应该已彻底完成迁移。如果你渴望了解更多，可以阅读本页面剩余部分 - 或者从介绍部分，从头开始深入新的文档和改进过的指南。由于你已经熟悉一些核心概念，所以许多部分已经被删除掉。

将 Vue 1.x 版本的应用程序迁移到 2.0 要花多长时间？

取决于你应用程序的规模 (中小型的基本上一天内就可以搞定)。

取决于你分心和开始 2.0 最酷的新功能的次数。😉 无法判断时间，我们构建 2.0 应用的时候也经常发生这种事！

取决于你使用了哪些旧有的特性。大部分可以通过查找和替换 (find-and-replace) 来实现升级，但有一些可能还是要花点时间。如果你没有遵循最佳实践，Vue 2.0 会尽力强迫你去遵循。这有利于项目的长期运行，但也可能意味着重大重构 (尽管有些需要重构的部分可能已经过时)。

如果我升级到到 Vue 2，我还必须同时升级 Vuex 和 Vue Router？

只有 Vue Router 2 与 Vue 2 保持兼容，所以 Vue Router 是需要升级的，你必须遵循 Vue Router 迁移方式来处理。幸运的是，大多数应用没有很多 router 相关代码，所以迁移可能不会超过一个小时。

对于 Vuex，版本 0.8+ 与 Vue 2 保持兼容，所以部分不必强制升级。可以促使你立即升级的唯一理由，是你想要使用那些 Vuex 2 中新的高级特性，比如模块 (modules) 和减少的样板文件 (reduced boilerplate)。

每个组件必须只有一个根元素。不再允许片段实例，如果你有这样的模板：

最好把整个内容都简单包裹到一个新的元素里，如下所示：

升级后运行端到端测试套件 (end-to-end test suite) 或运行应用程序，并查看控制台警告 (console warnings) 来找出那些模板中有多个根元素的地方。

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

使用其他钩子函数内置的 DOM 检测 (DOM check) 方法。例如，替换如下：

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

使用其他钩子函数内的 DOM 检测 (DOM check) 方法。例如，替换如下：

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

使用新的 beforeCreate 钩子函数替代，本质上 beforeCreate 和 init 完全相同。init 被重新命名是为了和其他的生命周期方法的命名方式保持一致。

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

使用新的 mounted 钩子函数替代。应该注意的是，使用 mounted 并不能保证钩子函数中的 this.$el 在 document 中。为此还应该引入 Vue.nextTick/vm.$nextTick。例如：

在代码库中运行迁移工具来找出所有使用此钩子函数的示例。

当包含 index 时，之前遍历数组时的参数顺序是 (index, value)。现在是 (value, index)，来和 JavaScript 的原生数组方法 (例如 forEach 和 map) 保持一致。

在代码库中运行迁移工具来找出那些使用旧有参数顺序的示例。注意，如果你将你的 index 参数命名为一些不通用的名字 (例如 position 或 num)，迁移工具将不会把它们标记出来。

当包含 property 名称/key 时，之前遍历对象的参数顺序是 (name, value)。现在是 (value, name)，来和常见的对象迭代器 (例如 lodash) 保持一致。

在代码库中运行迁移工具来找出那些使用旧有参数顺序的示例。注意，如果你将你的 key 参数命名为一些不通用的名字 (例如 name 或 property)，迁移工具将不会把它们标记出来。

已经移除了 $index 和 $key 这两个隐式声明变量，以便在 v-for 中显式定义。这可以使没有太多 Vue 开发经验的开发者更好地阅读代码，并且在处理嵌套循环时也能产生更清晰的行为。

在代码库中运行迁移工具来找出使用这些移除变量的示例。如果你没有找到，也可以在控制台错误中查找 (例如 Uncaught ReferenceError: $index is not defined)。

track-by 已经替换为 key，它的工作方式与其他 attribute 一样，没有 v-bind 或者 : 前缀，它会被作为一个字符串处理。多数情况下，你需要使用具有完整表达式的动态绑定 (dynamic binding) 来替换静态的 key。例如，替换：

在代码库中运行迁移工具来找出那些使用track-by的示例。

之前，v-for="number in 10" 的 number 从 0 开始到 9 结束，现在从 1 开始，到 10 结束。

在代码库中使用正则 /\w+ in \d+/搜索。当出现在 v-for 中，请检查是否受到影响。

如果需要检查 prop 的值，创建一个内部的 computed 值，而不再在 props 内部去定义，例如：

运行迁移工具找出包含 coerce 选项的实例。

Props 现在只能单向传递。为了对父组件产生反向影响，子组件需要显式地传递一个事件而不是依赖于隐式地双向绑定。详见：

运行 迁移工具，找出含有 twoWay 选项的实例。

Props 现在只能单向传递。为了对父组件产生反向影响，子组件需要显式地传递一个事件而不是依赖于隐式地双向绑定。详见：

运行迁移工具找到使用 .once 和 .sync 修饰符的实例。

组件内变更 prop 是反模式 (不推荐的) 的。比如，先声明一个 prop，然后在组件中通过 this.myProp = 'someOtherValue' 改变 prop 的值。根据渲染机制，当父组件重新渲染时，子组件的内部 prop 值也将被覆盖。

大多数情况下，变更 prop 值可以用以下选项替代：

运行端对端测试，查看关于 prop 变更的控制台警告信息。

对于一个根实例来说 (比如：用 new Vue({ ... }) 创建的实例)，只能用 propsData 而不是 props。

运行端对端测试，将会弹出 failed tests 来通知你使用 props 的根实例已经失效。

在 Vue 未来的大版本中，计算属性的缓存验证将会被移除。把不缓存的计算属性转换为方法可以得到和之前相同的结果。

运行迁移工具找到 cache: false 的选项。

在 2.0 中使用 v-bind 时，只有 null，undefined，和 false 被看作是假。这意味着，0 和空字符串将被作为真值渲染。比如 v-bind:draggable="''" 将被渲染为 draggable="true"。

对于枚举 attribute，除了以上假值之外，字符串 "false" 也会被渲染为 attr="false"。

注意，对于其它钩子函数 (如 v-if 和 v-show)，他们依然遵循 js 对真假值判断的一般规则。

运行端到端测试，如果你 app 的任何部分有可能被这个升级影响到，将会弹出failed tests

现在在组件上使用 v-on 只会监听自定义事件 (组件用 $emit 触发的事件)。如果要监听根元素的原生事件，可以使用 .native 修饰符，比如：

运行端对端测试，如果你 app 的任何部分有可能被这个升级影响到，将会弹出failed tests

Debouncing 曾经被用来控制 Ajax 请求及其它高耗任务的频率。Vue 中 v-model 的 debounce property 参数使得在一些简单情况下非常容易实现这种控制。但实际上，这是控制了状态更新的频率，而不是控制高耗时任务本身。这是个微小的差别，但是会随着应用增长而显现出局限性。

使用 debounce attribute，便无法观察“Typing”的状态。因为无法对输入状态进行实时检测。然而，通过将 debounce 与 Vue 解耦，可以仅仅只延迟我们想要控制的操作，从而避开这些局限性：

这种方式的另外一个优点是：当包裹函数执行时间与延时时间相当时，将会等待较长时间。比如，当给出搜索建议时，要等待用户输入停止一段时间后才给出建议，这个体验非常差。其实，这时候更适合用 throttling 函数。因为现在你可以自由的使用类似 lodash 之类的库，所以很快就可以用 throttling 重构项目。

运行迁移工具找出使用 debounce attribute 的实例。

lazy 和 number 参数现在以修饰符的形式使用，这样看起来更加清晰，而不是这样：

v-model 不再以 value attribute 方式初始化的初值了，显然他将以实例的 data 相应的 property 作为真正的初值。

将渲染 model 为“bar”而不是“foo”。同样，对 <textarea> 已有的值来说：

必须保证 text 初值为“hello world”

升级后运行端对端测试，注意关于 v-model 的内联 value attribute 的 console warnings

因为 <input> 将被编译成类似下面的 js 代码：

这样，v-model 的双向绑定在这里就失效了。把 str 赋值给迭代器里的另一个值也没有用，因为它仅仅是函数内部的一个变量。

替代方案是，你可以使用对象数组，这样 v-model 就可以同步更新对象里面的字段了，例如：

运行测试，如果你的 app 有地方被这个更新影响到的话将会弹出failed tests提示。

如果确实需要覆盖其它的 !important，最好用字符串形式去写：

运行 迁移帮助工具。找到含有 !important 的 style 绑定对象。

简单起见，v-el 和 v-ref 合并为一个 ref attribute 了，可以在组件实例中通过 $refs 来调用。这意味着 v-el:my-element 将写成这样：ref="myElement"，v-ref:my-component 变成了这样：ref="myComponent"。绑定在一般元素上时，ref 指 DOM 元素，绑定在组件上时，ref 为一组件实例。

因为 v-ref 不再是一个指令了而是一个特殊的 attribute，它也可以被动态定义了。这样在和 v-for 结合的时候是很有用的：

以前 v-el/v-ref 和 v-for 一起使用将产生一个 DOM 数组或者组件数组，因为没法给每个元素一个特定名字。现在你还仍然可以这样做，给每个元素一个同样的 ref：

和 1.x 中不同，$refs 不是响应的，因为它们在渲染过程中注册/更新。只有监听变化并重复渲染才能使它们响应。

另一方面，设计 $refs 主要是提供给 js 程序访问的，并不建议在模板中过度依赖使用它。因为这意味着在实例之外去访问实例状态，违背了 Vue 数据驱动的思想。

运行迁移工具找出实例中的 v-el 和 v-ref 。

v-else 不能再跟在 v-show 后面使用。请在 v-if 的否定分支中使用 v-show 来替代。例如：

运行迁移工具找出实例中存在的 v-else 以及 v-show。

在新版中，指令的使用范围已经大大减小了：现在指令仅仅被用于低级的 DOM 操作。大多数情况下，最好是使用组件作为代码复用的抽象层。

幸运的是，新钩子更加简单，更加容易掌握。详见自定义指令指南。

运行迁移工具找到定义指令的地方。在 helper 工具会把这些地方标记出来，因为很有可能这些地方需要重构。

.literal 修饰符已经被移除，为了获取一样的功能，可以简单地提供字符串修饰符作为值。

运行迁移工具找到实例中使用 `.literal` 修饰符的地方。

Vue 的过渡系统有了彻底的改变，现在通过使用 <transition> 和 <transition-group> 来包裹元素实现过渡效果，而不再使用 transition attribute。详见 Transitions guide。

运行迁移工具找到使用 transition attribute 的地方。

在新的过渡系统中，可以通过模板复用过渡效果。

运行迁移工具找到使用 transition attribute 的地方。

如果希望在列表渲染中使用渐近过渡，可以通过设置元素的 data-index (或类似 attribute) 来控制时间。请参考这个例子。

运行迁移工具找到使用 transition attribute 的地方。升级期间，你可以“过渡”到新的过渡策略。

events 选项被弃用。事件处理器现在在 created 钩子中被注册。参考详细示例 $dispatch and $broadcast 迁移指南

新的简明配置 keyCodes 的方式是通过 Vue.config.keyCodes 例如：

运行迁移工具找到过时的 keyCode 配置

$dispatch 和 $broadcast 已经被弃用。请使用更多简明清晰的组件间通信和更好的状态管理方案，如：Vuex。

因为基于组件树结构的事件流方式实在是让人难以理解，并且在组件结构扩展的过程中会变得越来越脆弱。这种事件方式确实不太好，我们也不希望在以后让开发者们太痛苦。并且 $dispatch 和 $broadcast 也没有解决兄弟组件间的通信问题。

对于 $dispatch 和 $broadcast 最简单的升级方式就是：通过使用事件中心，允许组件自由交流，无论组件处于组件树的哪一层。由于 Vue 实例实现了一个事件分发接口，你可以通过实例化一个空的 Vue 实例来实现这个目的。

这些方法的最常见用途之一是父子组件的相互通信。在这些情况下，你可以使用 v-on 监听子组件上 $emit 的变化。这可以允许你很方便的添加事件显性。

然而，如果是跨多层父子组件通信的话，$emit 并没有什么用。相反，用集中式的事件中间件可以做到简单的升级。这会让组件之间的通信非常顺利，即使是兄弟组件。因为 Vue 通过事件发射器接口执行实例，实际上你可以使用一个空的 Vue 实例。

比如，假设我们有个 todo 的应用结构如下：

然后在组件中，可以使用 $emit，$on，$off 分别来分发、监听、取消监听事件：

在简单的情况下这样做可以替代 $dispatch 和 $broadcast，但是对于大多数复杂情况，更推荐使用一个专用的状态管理层如：Vuex。

运行迁移工具找出使用 $dispatch 和 $broadcast的实例。

现在过滤器只能用在插入文本中 ({{ }} tags)。我们发现在指令 (如：v-model，v-on 等) 中使用过滤器使事情变得更复杂。像 v-for 这样的列表过滤器最好把处理逻辑作为一个计算属性放在 js 里面，这样就可以在整个模板中复用。

总之，能在原生 js 中实现的东西，我们尽量避免引入一个新的符号去重复处理同样的问题。下面是如何替换 Vue 内置过滤器：

请使用 lodash’s debounce (也有可能是 throttle) 来直接控制高耗任务。可以这样来实现上面的功能：

这种写法的更多优点详见：v-model 示例。

在计算属性中使用 js 内置方法：.slice method：

在计算属性中使用 js 内置方法 .filter method：

js 原生的 .filter 同样能实现很多复杂的过滤器操作，因为可以在计算计算属性中使用所有 js 方法。比如，想要通过匹配用户名字和电子邮箱地址 (不区分大小写) 找到用户：

而是在计算属性中使用 lodash’s orderBy (或者可能是 sortBy)：

运行迁移工具找到指令中使用的过滤器。如果有些没找到，看看控制台错误信息。

现在过滤器参数形式可以更好地与 js 函数调用方式一致，因此不用再用空格分隔参数：

运行迁移工具找到老式的调用符号，如果有遗漏，请看控制台错误信息。

尽管插入文本内部的过滤器依然有效，但是所有内置过滤器已经移除了。取代的是，推荐在每个区域使用更专业的库来解决。(比如用 date-fns 来格式化日期，用 accounting 来格式化货币)。

对于每个内置过滤器，我们大概总结了下该怎么替换。代码示例可能写在自定义 helper 函数，方法或计算属性中。

不用一个个改，因为 Vue 已经帮你自动格式化好了，无论是字符串，数字还是数组，对象。如果想用 js 的 JSON.stringify 功能去实现，你也可以把它写在方法或者计算属性里面。

npm 上的 pluralize 库可以很好的实现这个功能。如果仅仅想将特定的词格式化成复数形式或者想给特定的值 (0) 指定特定的输出，也可以很容易地自定义复数格式化过滤器：

大多数情况下，仍然会有奇怪的现象 (比如 0.035.toFixed(2) 向上取舍得到 0.04，但是 0.045 向下取舍却也得到 0.04)。解决这些问题可以使用 accounting 库来实现更多可靠的货币格式化。

运行迁移工具找到舍弃的过滤器。如果有些遗漏，请参考控制台错误信息。

有些用户已经乐于通过 v-model 使用双向过滤器，以很少的代码创建有趣的输入。尽管表面上很简单，双向过滤器也会暗藏一些巨大的复杂性——甚至促使状态更新变得迟钝影响用户体验。推荐用包裹一个输入的组件取而代之，这样以更显性且功能更丰富的方式创建自定义的输入。

我们现在做一次双向汇率过滤器的迁移作为示范：

它基本工作良好，但是拖延的状态更新会导致奇怪的行为。比如试着在其中一个输入框中输入 9.999。当输入框失去焦点的时候，其值将会更新到 $10.00。然而当我们从整个计算器的角度看时，你会发现存储的数据是 9.999。用户看到的已经不是真实的同步了！

为了过渡到一个更加健壮的 Vue 2.0 的方案，让我们首先在一个新的 <currency-input> 组件中包裹这个过滤器：

它允许我们添加独立过滤器无法封装的行为，比如选择输入框聚焦的内容。下一步我们从过滤器中提取业务逻辑。接下来是我们把所有的东西放到一个外部的 currencyValidator 对象中：

这会更加模块化，不只是更容易的迁移到 Vue 2，同时也允许汇率间隙和格式化：

把这个验证器提取出来之后，我们也可以更舒适的把它构建到更健壮的解决方案中。那些古怪的状态也消除了，用户不再可能会输入错误，就像浏览器原生的数字输入框一样。

然而在 Vue 1.0 的过滤器中，我们仍然是受限的，所以还是完全升级到 Vue 2.0 吧：

运行迁移工具找到在例如 v-model 的指令中使用过滤器的例子。如果你错过了，则应该会收到命令行报错。

同一模板中的重名 <slot> 已经弃用。当一个插槽已经被渲染过了，那么就不能在同一模板其它地方被再次渲染了。如果要在不同位置渲染同一内容，可以用 prop 来传递。

更新后运行测试，查看控制台警告信息 关于重名 slots 的提示 v-model。

通过具名 <slot> 插入的片段不再保持 slot 的 attribute。请用一个包裹元素来控制样式。或者用更高级方法：通过编程方式修改内容：render functions。

运行迁移工具找到选择 slots 标签 CSS 选择器 (例如：[slot="my-slot-name"])。

keep-alive 不再是一个特殊 attribute 而是一个包裹组件，类似于 <transition> 比如：

这样可以在含多种状态子组件中使用 <keep-alive>：

当 <keep-alive> 含有不同子组件时，应该分别影响到每一个子组件。不仅是第一个而是所有的子组件都将被忽略。

和 <transition> 一起使用时，确保把内容包裹在内：

运行迁移工具找到keep-alive attribute。

Attribute 内部的计算插值已经不能再使用了：

运行迁移工具找到property内部的计算插值

HTML 的计算插值 ({{{ foo }}}) 已经移除，取代的是 v-html 指令。

单次绑定 ({{* foo }}) 已经被新的 v-once directive 取代。

通过 vm.$watch 创建的观察器现在将在组件渲染时被激活。这样可以让你在组件渲染前更新状态，不用做不必要的更新。比如可以通过观察组件的 prop 变化来更新组件本身的值。

如果以前通过 vm.$watch 在组件更新后与 DOM 交互，现在就可以通过 updated 生命周期钩子来做这些。

运行测试，如果有依赖于老方法的观察器将弹出 failed tests。

vm.$set 只是 Vue.set 的别名。

vm.$delete 现在只是：Vue.delete 别名。

运行迁移工具找到数组上的.$set。如有遗漏请参考控制台错误信息。

用 Array.prototype.splice 替代，例如：

或者更好的方法，直接给除去的方法一个 index 参数：

运行迁移工具找到数组上的.$remove。如有遗漏请参考控制台错误信息

Vue.set 和 Vue.delete 在实例上将不再起作用。现在都强制在实例的 data 选项中声明所有顶级响应值。如果删除实例 property 或实例 $data 上的某个值，直接将它设置为 null 即可。

运行迁移工具找到实例中的 Vue.set 或 Vue.delete 。如有遗漏请参考控制台错误信息。

现在禁止替换实例的 $data。这样防止了响应系统的一些极端情况并且让组件状态更加可控可预测 (特别是对于存在类型检查的系统)。

运行迁移工具找到覆盖 vm.$data的位置。如有遗漏请参考控制台警告信息。

运行 迁移工具找到 vm.$get 的位置。如有遗漏请参考 控制台错误信息。

运行迁移工具找到 vm.$appendTo 的位置。如果有遗漏可以参考控制台错误信息。

运行 迁移工具找到 vm.$before。如有遗漏，请参考 控制台错误信息。

如果 myElement 是最后一个节点也可以这样写：

运行迁移工具找到 vm.$after 的位置。如有遗漏，请参考控制台错误信息。

运行 迁移工具找到vm.$remove。如有遗漏，请参考控制台错误信息。

尽量不要使用，如果必须使用该功能并且不肯定如何使用请参考 the forum。

运行迁移工具找到使用 vm.$eval 的位置。如有遗漏请参考控制台错误信息。

尽量不要使用，如果必须使用该功能并且不肯定如何使用请参考 the forum。

运行迁移工具找到vm.$interpolate。如有遗漏请参考控制台错误信息.

请使用 Vue Devtools 感受最佳 debug 体验。

运行迁移工具找到 vm.$log。如有遗漏请参考控制台错误信息.

现在组件总是会替换掉他们被绑定的元素。为了模仿 replace: false 的行为，可以用一个和将要替换元素类似的元素将根组件包裹起来：

运行迁移工具找到 replace: false使用的位置。

不再需要，因为警告信息将默认在堆栈信息里输出。

运行迁移工具找到包含Vue.config.debug的地方。

运行 迁移工具找到使用Vue.config.async的实例。

以模板选项的方式使用。这样可以在使用自定义分隔符时避免影响第三方模板。

运行迁移工具找到使用Vue.config.delimiters的实例。

运行迁移工具找到 Vue.config.unsafeDelimiters。然后 helper 工具也会找到 HTML 插入的实例，可以用`v-html`来替换。

el 选项不再在 Vue.extend 中使用。仅在实例创建参数中可用。

更新后运行测试在控制台警告信息中找到关于带有Vue.extend的el。

运行迁移工具找到包含Vue.elementDirective的实例。

Partials 已被移除，取而代之的是更明确的组件之间的数据流–props。除非你正在使用一个部分性能关键型区域，否则建议只使用一个 normal component 来代替。如果你是动态绑定部分的 name，您可以使用 dynamic component。

如果你碰巧在你的应用程序的性能关键部分使用 partials，那么你应该升级到函数式组件。它们必须在纯 JS / JSX 文件中 (而不是在 .vue 文件中)，并且是无状态的和无实例的，就像 partials。这使得渲染极快。

函数式组件相对于 partials 一个好处是它们可以更具动态性，因为它们允许您访问 JavaScript 的全部功能。然而，这是有成本的。如果你从来没有使用过渲染式的组件框架，你可能需要花费更长的时间来学习它们。

运行迁移工具找到包含 Vue.partial的实例

**Examples:**

Example 1 (unknown):
```unknown
<p>foo</p><p>bar</p>
```

Example 2 (unknown):
```unknown
<div>  <p>foo</p>  <p>bar</p></div>
```

Example 3 (unknown):
```unknown
attached: function () {  doSomething()}
```

Example 4 (unknown):
```unknown
mounted: function () {  this.$nextTick(function () {    doSomething()  })}
```

---

## 从 Vue Router 0.7.x 迁移 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/migration-vue-router.html

**Contents:**
- 从 Vue Router 0.7.x 迁移
- Router 初始化
  - router.start 替换
    - 升级路径
- Route 定义
  - router.map 替换
    - 升级路径
  - router.on 移除
    - 升级路径
  - router.beforeEach changed

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

只有 Vue Router 2 是与 Vue 2 相互兼容的，所以如果你更新了 Vue，你也需要更新 Vue Router。这也是我们在主文档中将迁移路径的详情添加进来的原因。有关使用 Vue Router 2 的完整教程，请参阅 Vue Router 文档。

不再会有一个特殊的 API 用来初始化包含 Vue Router 的 app，这意味着不再是：

你只需要传一个路由 property 给 Vue 实例：

或者，如果你使用的是运行时构建 (runtime-only) 方式：

运行 迁移助手 找到 router.start 被调用的示例。

路由现在被定义为一个在 router 实例里的一个 routes 选项数组。所以这些路由：

考虑到不同浏览器中遍历对象不能保证会使用相同的 property 顺序，这种数组的语法可以保证更多可预测的路由匹配。

运行 迁移助手 找到 router.map 被调用的示例。

如果你需要在启动的 app 时通过代码生成路由，你可以动态地向路由数组推送定义来完成这个操作。举个例子：

如果你需要在 router 被实例化后增加新的路由，你可以把 router 原来的匹配方式换成一个包括你新添的加路由的匹配方式：

运行 迁移助手 找到 router.on 被调用的示例。

router.beforeEach 现在是异步工作的，并且携带一个 next 函数作为其第三个参数。

出于 Vue Router 和其他路由库一致性的考虑，重命名为 children

运行 迁移助手 找到 subRoutes 选项的示例。

现在用一个路由定义的选项作为代替。举个例子，你将会更新：

成像下面的 routes 配置里定义的样子：

运行 迁移助手 找到 router.redirect 被调用的示例。

现在是你进行 alias 操作的路由定义里的一个选项。举个例子，你需要在你的 routes 定义里将：

如果你需要进行多次 alias 操作，你也可以使用一个数组语法去实现：

运行迁移助手找到 router.alias 被调用的示例。

现在任意的 route property 必须在新 meta property 的作用域内，以避免和以后的新特性发生冲突。举个例子，如果你以前这样定义：

如果在一个路由上访问一个 property，你仍然会通过 meta。举个例子：

运行 迁移助手 找到任意的路由不在 meta 作用域下的示例。

当传递数组给 query 参数时，URL 语法不再是 /foo?users[]=Tom&users[]=Jerry，取而代之，新语法是 /foo?users=Tom&users=Jerry，此时 $route.query.users 将仍旧是一个数组，不过如果在该 query 中只有一个参数：/foo?users=Tom，当直接访问该路由时，vue-router 将无法知道我们期待的 users 是个数组。因此，可以考虑添加一个计算属性并且在每个使用 $route.query.users 的地方以该计算属性代替：

路由匹配现在使用 path-to-regexp 这个包，这将会使得工作与之前相比更加灵活。

语法稍微有些许改变，所以以 /category/*tags 为例，应该被更新为 /category/:tags+。

v-link 指令已经被一个新的 <router-link> 组件指令替代，这一部分的工作已经被 Vue 2 中的组件完成。这将意味着在任何情况下，如果你拥有这样一个链接：

注意：<router-link> 不支持 target="_blank"，如果你想打开一个新标签页，你必须用 <a> 标签。

运行 迁移助手 找到 v-link 指令的示例。

v-link-active 也因为指定了一个在 <router-link> 组件上的 tag attribute 而被弃用了。举个例子，你需要更新：

<a> 标签将会成为真实的链接 (并且可以获取到正确的跳转)，但是激活的类将会被应用在外部的 <li> 标签上。

运行 迁移助手 找到 v-link-active 指令的示例

为了与 HTML5 History API 保持一致性，router.go 已经被用来作为后退/前进导航，router.push 用来导向特殊页面。

运行 迁移助手 ，找到 router.go 和 router.push 指令被调用的示例。

Hashbangs 将不再为谷歌需要去爬去一个网址，所以他们将不再成为哈希策略的默认选项。

运行 迁移助手 找到 hashbang: false 选项的示。

所有路由模型选项将被简化成一个单个的 mode 选项。你需要更新：

运行 迁移助手 找到 history: true 选项的示。

所有路由模型选项将被简化成一个单个的 mode 选项。你需要更新：

运行 迁移助手 找到 abstract: true 选项的示例。

它已经被替换为可以接受一个函数的 scrollBehavior 选项，所以滑动行为可以完全的被定制化处理 - 甚至为每次路由进行定制也可以满足。这将会开启很多新的可能，但是简单的复制旧的行为：

运行 迁移路径 找到 saveScrollPosition: true 选项的示例。

为了与 HTML 的 <base> 标签保持一致性，重命名为 base。

运行 迁移路径 找到 root 选项的示例。

由于 Vue 的过渡系统 appear transition control 的存在，这个选项将不再需要。

运行 迁移路径 找到 transitionOnLoad: true 选项的示例。

出于简化钩子的考虑被移除。如果你真的需要抑制过渡错误，你可以使用 try…catch 作为替代。

运行 迁移指令 找到 suppressTransitionError: true 选项的示例。

使用 beforeRouteEnter 这一组件进行替代。

运行 迁移路径 找到 activate 钩子的示例。

使用 beforeEnter 在路由中作为替代。

运行 迁移路径 找到 canActivate 钩子的示例。

使用 beforeDestroy 或者 destroyed 钩子作为替代。

运行 迁移路径 找到 deactivate 钩子的示例。

在组件中使用 beforeRouteLeave 作为替代。

运行 迁移路径 找到 canDeactivate 钩子的示例。

运行 迁移助手 找到 canReuse: false 选项的示例。

$route property 是响应式的，所以你可以就使用一个 watcher 去响应路由的改变，就像这样：

运行 迁移助手 找到 data 钩子的示例。

定义你自己的 property (例如：isLoading)，然后在路由上的 watcher 中更新加载状态。举个例子，如果使用 axios 获取数据：

**Examples:**

Example 1 (unknown):
```unknown
router.start({  template: '<router-view></router-view>'}, '#app')
```

Example 2 (unknown):
```unknown
new Vue({  el: '#app',  router: router,  template: '<router-view></router-view>'})
```

Example 3 (javascript):
```javascript
new Vue({  el: '#app',  router: router,  render: h => h('router-view')})
```

Example 4 (unknown):
```unknown
router.map({  '/foo': {    component: Foo  },  '/bar': {    component: Bar  }})
```

---

## 迁移至 Vue 2.7 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/migration-vue-2-7.html

**Contents:**
- 迁移至 Vue 2.7
- 移植回来的特性
  - 关于被导出的 API 的注意事项
  - 与 Vue 3 的行为差异
- 升级指南
  - Vue CLI / webpack
  - Vite
  - Volar 兼容性
  - 开发者工具支持
- 2.7 发布的后续

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vue 2.7 是 Vue 2 最新的次级版本。其提供了内置的组合式 API 支持。

尽管 Vue 3 是当前的默认主版本，我们非常理解许多由于依赖的兼容性、浏览器的兼容性需求、或精力有限不足以完成升级等因素，仍然留在 Vue 2 的用户。在 Vue 2.7 中，我们从 Vue 3 移植回了最重要的一些特性，使得 Vue 2 用户也可以享有这些便利。

支持 emits 选项，但仅以类型检查为目的 (并不会影响运行时的行为)

2.7 也在模板表达式中支持了 ESNext 语法。当配合构建系统使用时，编译后的模板渲染函数将会经过和处理普通 JavaScript 相同配置的 loader / 插件。这意味着如果你为 .js 文件配置了 Babel，这些配置也会应用在单文件组件的模板表达式中。

在 ESM 构建版本中，这些 API 会 (且仅会) 被导出为具名 API：

在 UMD 和 CJS 构建版本里，这些 API 会被导出为全局对象 Vue 的属性。

当调用外置的 CJS 版本进行打包时，打包工具应该有能力处理与 ESM 模块的互操作 (ESM interop)。

组合式 API 使用了 Vue 2 中基于 getter/setter 的响应式系统，以确保浏览器的兼容性。这意味着其行为和 Vue 3 中基于代理的系统相比有一些重要的区别：

所有 Vue 2 检测变化的注意事项依然存在。

reactive()、ref() 和 shallowReactive() 会直接转换原始的对象而不是创建代理。这意味着：

readonly() 会创建一个独立的对象，但是其不会追踪新添加的属性，也不会对数组生效。

避免将数组作为 reactive() 的根值。因为无法访问属性，数组的变更不会被追踪到 (这样做会产生一则警告)。

响应式 API 会忽略以 symbol 作为 key 的属性。

将本地的 @vue/cli-xxx 依赖升级至所在主版本范围内的最新版本 (如有)：

将 vue 升级至 ^2.7.0。同时你可以从依赖中移除 vue-template-compiler——它在 2.7 中已经不再需要了。

注意：如果你在使用 @vue/test-utils，那么 vue-template-compiler 需要保留，因为该测试工具集依赖了一些只有这个包会暴露的 API。

检查包管理工具的版本锁定文件，以确保以下依赖的版本符合要求。它们可能是间接依赖所以未必罗列在了 package.json 中。

否则，你需要移除整个 node_modules 和版本锁定文件，然后重新安装，以确保它们都升到了最新版本。

如果你曾经使用了 @vue/composition-api，将其导入语句切换至 vue 即可。注意有些之前通过插件暴露的 API，例如 createApp，并没有被移植回 2.7。

如果你在 <script setup> 中遇到了未使用变量的 lint 错误，请更新 eslint-plugin-vue 至最新版本 (9+)。

2.7 的单文件组件编译器使用了 PostCSS 8 (从 7 升级而来)。PostCSS 8 应该向下兼容了绝大多数插件，但是该升级可能在你使用了一些只支持 PostCSS 7 的自定义插件时遇到问题。这种情况下，你需要升级相应的插件至其兼容 PostCSS 8 的版本。

2.7 通过一个新的插件提供对 Vite 的支持：@vitejs/plugin-vue2。这个新的插件需要 Vue 2.7 或更高版本，并取代了已有的 vite-plugin-vue2。

注意这个新插件刻意不会处理 Vue 特有的 JSX / TSX 转换。在 Vite 中，Vue 2 的 JSX / TSX 转换是通过一个独立的插件进行处理的：@vitejs/plugin-vue2-jsx。

2.7 的发布改进了类型定义，所以我们不必再只为支持 Volar 的模板类型推断而安装 @vue/runtime-dom。你现在只需要在 tsconfig.json 中进行以下配置：

Vue Devtools 6.2.0 已经支持了 2.7 组合式 API 状态的审查，但该扩展可能仍然需要几天时间在各自的发布平台上通过审核。

如我们之前所提到的，2.7 是 Vue 2.x 的最后一个次级版本。在此发布之后，Vue 2 将会进入长期技术支持 (LTS：long-term support) 状态，该状态从现在起计算会持续 18 个月，且不再提供新特性。

这意味着 Vue 2 的终止支持时间将会是 2023 年 12 月 31 日。我们相信这将为生态系统的绝大部分提供充足的时间迁移至 Vue 3。然而，我们也理解有些团队或项目可能无法在这个时间段内升级，同时还要满足安全和合规等要求。如果你的团队希望在 2023 年底之后继续使用Vue 2，请确保提前做好计划并了解你的可选项：了解更多关于 Vue 2 LTS 及其延长版服务。

**Examples:**

Example 1 (python):
```python
import Vue, { ref } from "vue";Vue.ref; // undefined，请换为使用具名导出的 API
```

Example 2 (unknown):
```unknown
// 2.7 中为 true，3.x 中为 falsereactive(foo) === foo;
```

Example 3 (unknown):
```unknown
{  // ...  "vueCompilerOptions": {    "target": 2.7  }}
```

---

## 从 Vuex 0.6.x 迁移到 1.0 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/migration-vuex.html

**Contents:**
- 从 Vuex 0.6.x 迁移到 1.0
- 带字符串 property 路径的 store.watch 替换
    - 升级方法
- Store 的事件触发器移除
    - 升级方式
- 中间件替换
    - 升级方法

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

Vuex 2.0 已经发布了，但是这份指南只涵盖迁移到 1.0？这是打错了吗？此外，似乎 Vuex 1.0 和 2.0 也同时发布。这是怎么回事？我该用哪一个并且哪一个兼容 Vue 2.0 呢？

Vuex 2.0 从根本上重新设计并且提供简洁的 API，用于帮助正在开始一个新项目的用户，或想要用客户端状态管理前沿技术的用户。此迁移指南不涵盖 Vuex 2.0 相关内容，因此如果你想了解更多，请查阅 Vuex 2.0 文档。

Vuex 1.0 主要是向下兼容，所以升级只需要很小的改动。推荐拥有大量现存代码库的用户，或只想尽可能平滑升级 Vue 2.0 的用户。这份指南致力促进这一过程，但仅包括迁移说明。完整使用指南请查阅 Vuex 1.0 文档。

store.watch 现在只接受函数。因此，下面例子你需要替换：

这帮助你更加完善的控制那些需要监听的响应式 property。

在代码库运行迁移工具，查找在 store.watch 中使用字符串作为第一个参数的事例。

store 实例不再暴露事件触发器 (event emitter) 接口 (on、off、emit)。如果你之前使用 store 作为全局的 event bus，迁移说明相关内容请查阅此章节。

为了替换正在使用观察 store 自身触发事件的这些接口，(例如：store.on('mutation', callback))，我们引入新的方法 store.subscribe。在插件中的典型使用方式如下：

在代码库运行迁移工具，查找使用了 store.on, store.off, store.emit 的事例。

中间件被替换为插件。插件是接收 store 作为仅有参数的基本函数，能够监听 store 中的 mutation 事件：

在代码库运行迁移工具，查找使用了 middlewares 选项的事例。

**Examples:**

Example 1 (unknown):
```unknown
store.watch('user.notifications', callback)
```

Example 2 (unknown):
```unknown
store.watch(  // 当返回结果改变...  function (state) {    return state.user.notifications  },  // 执行回调函数  callback)
```

Example 3 (javascript):
```javascript
var myPlugin = store => {  store.subscribe(function (mutation, state) {    // Do something...  })}
```

Example 4 (javascript):
```javascript
const myPlugins = store => {  store.subscribe('mutation', (mutation, state) => {    // Do something...  })}
```

---
