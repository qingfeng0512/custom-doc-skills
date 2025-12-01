# Vue2 - Essentials

**Pages:** 5

---

## 自定义事件 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-custom-events.html

**Contents:**
- 自定义事件
- 事件名
- 自定义组件的 v-model
- 将原生事件绑定到组件
- .sync 修饰符

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

不同于组件和 prop，事件名不存在任何自动化的大小写转换。而是触发的事件名需要完全匹配监听这个事件所用的名称。举个例子，如果触发一个 camelCase 名字的事件：

则监听这个名字的 kebab-case 版本是不会有任何效果的：

不同于组件和 prop，事件名不会被用作一个 JavaScript 变量名或 property 名，所以就没有理由使用 camelCase 或 PascalCase 了。并且 v-on 事件监听器在 DOM 模板中会被自动转换为全小写 (因为 HTML 是大小写不敏感的)，所以 v-on:myEvent 将会变成 v-on:myevent——导致 myEvent 不可能被监听到。

因此，我们推荐你始终使用 kebab-case 的事件名。

一个组件上的 v-model 默认会利用名为 value 的 prop 和名为 input 的事件，但是像单选框、复选框等类型的输入控件可能会将 value attribute 用于不同的目的。model 选项可以用来避免这样的冲突：

现在在这个组件上使用 v-model 的时候：

这里的 lovingVue 的值将会传入这个名为 checked 的 prop。同时当 <base-checkbox> 触发一个 change 事件并附带一个新的值的时候，这个 lovingVue 的 property 将会被更新。

注意你仍然需要在组件的 props 选项里声明 checked 这个 prop。

你可能有很多次想要在一个组件的根元素上直接监听一个原生事件。这时，你可以使用 v-on 的 .native 修饰符：

在有的时候这是很有用的，不过在你尝试监听一个类似 <input> 的非常特定的元素时，这并不是个好主意。比如上述 <base-input> 组件可能做了如下重构，所以根元素实际上是一个 <label> 元素：

这时，父级的 .native 监听器将静默失败。它不会产生任何报错，但是 onFocus 处理函数不会如你预期地被调用。

为了解决这个问题，Vue 提供了一个 $listeners property，它是一个对象，里面包含了作用在这个组件上的所有监听器。例如：

有了这个 $listeners property，你就可以配合 v-on="$listeners" 将所有的事件监听器指向这个组件的某个特定的子元素。对于类似 <input> 的你希望它也可以配合 v-model 工作的组件来说，为这些监听器创建一个类似下述 inputListeners 的计算属性通常是非常有用的：

现在 <base-input> 组件是一个完全透明的包裹器了，也就是说它可以完全像一个普通的 <input> 元素一样使用了：所有跟它相同的 attribute 和监听器都可以工作，不必再使用 .native 监听器。

在有些情况下，我们可能需要对一个 prop 进行“双向绑定”。不幸的是，真正的双向绑定会带来维护上的问题，因为子组件可以变更父组件，且在父组件和子组件两侧都没有明显的变更来源。

这也是为什么我们推荐以 update:myPropName 的模式触发事件取而代之。举个例子，在一个包含 title prop 的假设的组件中，我们可以用以下方法表达对其赋新值的意图：

然后父组件可以监听那个事件并根据需要更新一个本地的数据 property。例如：

为了方便起见，我们为这种模式提供一个缩写，即 .sync 修饰符：

注意带有 .sync 修饰符的 v-bind 不能和表达式一起使用 (例如 v-bind:title.sync=”doc.title + ‘!’” 是无效的)。取而代之的是，你只能提供你想要绑定的 property 名，类似 v-model。

当我们用一个对象同时设置多个 prop 的时候，也可以将这个 .sync 修饰符和 v-bind 配合使用：

这样会把 doc 对象中的每一个 property (如 title) 都作为一个独立的 prop 传进去，然后各自添加用于更新的 v-on 监听器。

将 v-bind.sync 用在一个字面量的对象上，例如 v-bind.sync=”{ title: doc.title }”，是无法正常工作的，因为在解析一个像这样的复杂表达式的时候，有很多边缘情况需要考虑。

**Examples:**

Example 1 (unknown):
```unknown
this.$emit('myEvent')
```

Example 2 (unknown):
```unknown
<!-- 没有效果 --><my-component v-on:my-event="doSomething"></my-component>
```

Example 3 (unknown):
```unknown
Vue.component('base-checkbox', {  model: {    prop: 'checked',    event: 'change'  },  props: {    checked: Boolean  },  template: `    <input      type="checkbox"      v-bind:checked="checked"      v-on:change="$emit('change', $event.target.checked)"    >  `})
```

Example 4 (unknown):
```unknown
<base-checkbox v-model="lovingVue"></base-checkbox>
```

---

## 插槽 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-slots.html

**Contents:**
- 插槽
- 插槽内容
- 编译作用域
- 后备内容
- 具名插槽
- 作用域插槽
  - 独占默认插槽的缩写语法
  - 解构插槽 Prop
- 动态插槽名
- 具名插槽的缩写

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

在 2.6.0 中，我们为具名插槽和作用域插槽引入了一个新的统一的语法 (即 v-slot 指令)。它取代了 slot 和 slot-scope 这两个目前已被废弃但未被移除且仍在文档中的 attribute。新语法的由来可查阅这份 RFC。

Vue 实现了一套内容分发的 API，这套 API 的设计灵感源自 Web Components 规范草案，将 <slot> 元素作为承载分发内容的出口。

然后你在 <navigation-link> 的模板中可能会写为：

当组件渲染的时候，<slot></slot> 将会被替换为“Your Profile”。插槽内可以包含任何模板代码，包括 HTML：

如果 <navigation-link> 的 template 中没有包含一个 <slot> 元素，则该组件起始标签和结束标签之间的任何内容都会被抛弃。

该插槽跟模板的其它地方一样可以访问相同的实例 property (也就是相同的“作用域”)，而不能访问 <navigation-link> 的作用域。例如 url 是访问不到的：

父级模板里的所有内容都是在父级作用域中编译的；子模板里的所有内容都是在子作用域中编译的。

有时为一个插槽设置具体的后备 (也就是默认的) 内容是很有用的，它只会在没有提供内容的时候被渲染。例如在一个 <submit-button> 组件中：

我们可能希望这个 <button> 内绝大多数情况下都渲染文本“Submit”。为了将“Submit”作为后备内容，我们可以将它放在 <slot> 标签内：

现在当我在一个父级组件中使用 <submit-button> 并且不提供任何插槽内容时：

则这个提供的内容将会被渲染从而取代后备内容：

自 2.6.0 起有所更新。已废弃的使用 slot attribute 的语法在这里。

有时我们需要多个插槽。例如对于一个带有如下模板的 <base-layout> 组件：

对于这样的情况，<slot> 元素有一个特殊的 attribute：name。这个 attribute 可以用来定义额外的插槽：

一个不带 name 的 <slot> 出口会带有隐含的名字“default”。

在向具名插槽提供内容的时候，我们可以在一个 <template> 元素上使用 v-slot 指令，并以 v-slot 的参数的形式提供其名称：

现在 <template> 元素中的所有内容都将会被传入相应的插槽。任何没有被包裹在带有 v-slot 的 <template> 中的内容都会被视为默认插槽的内容。

然而，如果你希望更明确一些，仍然可以在一个 <template> 中包裹默认插槽的内容：

注意 v-slot 只能添加在 <template> 上 (只有一种例外情况)，这一点和已经废弃的 slot attribute 不同。

自 2.6.0 起有所更新。已废弃的使用 slot-scope attribute 的语法在这里。

有时让插槽内容能够访问子组件中才有的数据是很有用的。例如，设想一个带有如下模板的 <current-user> 组件：

我们可能想换掉备用内容，用名而非姓来显示。如下：

然而上述代码不会正常工作，因为只有 <current-user> 组件可以访问到 user，而我们提供的内容是在父级渲染的。

为了让 user 在父级的插槽内容中可用，我们可以将 user 作为 <slot> 元素的一个 attribute 绑定上去：

绑定在 <slot> 元素上的 attribute 被称为插槽 prop。现在在父级作用域中，我们可以使用带值的 v-slot 来定义我们提供的插槽 prop 的名字：

在这个例子中，我们选择将包含所有插槽 prop 的对象命名为 slotProps，但你也可以使用任意你喜欢的名字。

在上述情况下，当被提供的内容只有默认插槽时，组件的标签才可以被当作插槽的模板来使用。这样我们就可以把 v-slot 直接用在组件上：

这种写法还可以更简单。就像假定未指明的内容对应默认插槽一样，不带参数的 v-slot 被假定对应默认插槽：

注意默认插槽的缩写语法不能和具名插槽混用，因为它会导致作用域不明确：

只要出现多个插槽，请始终为所有的插槽使用完整的基于 <template> 的语法：

作用域插槽的内部工作原理是将你的插槽内容包裹在一个拥有单个参数的函数里：

这意味着 v-slot 的值实际上可以是任何能够作为函数定义中的参数的 JavaScript 表达式。所以在支持的环境下 (单文件组件或现代浏览器)，你也可以使用 ES2015 解构来传入具体的插槽 prop，如下：

这样可以使模板更简洁，尤其是在该插槽提供了多个 prop 的时候。它同样开启了 prop 重命名等其它可能，例如将 user 重命名为 person：

你甚至可以定义后备内容，用于插槽 prop 是 undefined 的情形：

动态指令参数也可以用在 v-slot 上，来定义动态的插槽名：

跟 v-on 和 v-bind 一样，v-slot 也有缩写，即把参数之前的所有内容 (v-slot:) 替换为字符 #。例如 v-slot:header 可以被重写为 #header：

然而，和其它指令一样，该缩写只在其有参数的时候才可用。这意味着以下语法是无效的：

如果你希望使用缩写的话，你必须始终以明确插槽名取而代之：

插槽 prop 允许我们将插槽转换为可复用的模板，这些模板可以基于输入的 prop 渲染出不同的内容。这在设计封装数据逻辑同时允许父级组件自定义部分布局的可复用组件时是最有用的。

例如，我们要实现一个 <todo-list> 组件，它是一个列表且包含布局和过滤逻辑：

我们可以将每个 todo 作为父级组件的插槽，以此通过父级组件对其进行控制，然后将 todo 作为一个插槽 prop 进行绑定：

现在当我们使用 <todo-list> 组件的时候，我们可以选择为 todo 定义一个不一样的 <template> 作为替代方案，并且可以从子组件获取数据：

这只是作用域插槽用武之地的冰山一角。想了解更多现实生活中的作用域插槽的用法，我们推荐浏览诸如 Vue Virtual Scroller、Vue Promised 和 Portal Vue 等库。

v-slot 指令自 Vue 2.6.0 起被引入，提供更好的支持 slot 和 slot-scope attribute 的 API 替代方案。v-slot 完整的由来参见这份 RFC。在接下来所有的 2.x 版本中 slot 和 slot-scope attribute 仍会被支持，但已经被官方废弃且不会出现在 Vue 3 中。

自 2.6.0 起被废弃。新推荐的语法请查阅这里。

在 <template> 上使用特殊的 slot attribute，可以将内容从父级传给具名插槽 (把这里提到过的 <base-layout> 组件作为示例)：

或者直接把 slot attribute 用在一个普通元素上：

这里其实还有一个未命名插槽，也就是默认插槽，捕获所有未被匹配的内容。上述两个示例的 HTML 渲染结果均为：

自 2.6.0 起被废弃。新推荐的语法请查阅这里。

在 <template> 上使用特殊的 slot-scope attribute，可以接收传递给插槽的 prop (把这里提到过的 <slot-example> 组件作为示例)：

这里的 slot-scope 声明了被接收的 prop 对象会作为 slotProps 变量存在于 <template> 作用域中。你可以像命名 JavaScript 函数参数一样随意命名 slotProps。

这里的 slot="default" 可以被忽略为隐性写法：

slot-scope attribute 也可以直接用于非 <template> 元素 (包括组件)：

slot-scope 的值可以接收任何有效的可以出现在函数定义的参数位置上的 JavaScript 表达式。这意味着在支持的环境下 (单文件组件或现代浏览器)，你也可以在表达式中使用 ES2015 解构，如下：

使用这里描述过的 <todo-list> 作为示例，与它等价的使用 slot-scope 的代码是：

**Examples:**

Example 1 (unknown):
```unknown
<navigation-link url="/profile">  Your Profile</navigation-link>
```

Example 2 (unknown):
```unknown
<a  v-bind:href="url"  class="nav-link">  <slot></slot></a>
```

Example 3 (unknown):
```unknown
<navigation-link url="/profile">  <!-- 添加一个 Font Awesome 图标 -->  <span class="fa fa-user"></span>  Your Profile</navigation-link>
```

Example 4 (unknown):
```unknown
<navigation-link url="/profile">  <!-- 添加一个图标的组件 -->  <font-awesome-icon name="user"></font-awesome-icon>  Your Profile</navigation-link>
```

---

## 组件注册 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-registration.html

**Contents:**
- 组件注册
- 组件名
  - 组件名大小写
    - 使用 kebab-case
    - 使用 PascalCase
- 全局注册
- 局部注册
- 模块系统
  - 在模块系统中局部注册
  - 基础组件的自动化全局注册

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

在注册一个组件的时候，我们始终需要给它一个名字。比如在全局注册的时候我们已经看到了：

该组件名就是 Vue.component 的第一个参数。

你给予组件的名字可能依赖于你打算拿它来做什么。当直接在 DOM 中使用一个组件 (而不是在字符串模板或单文件组件) 的时候，我们强烈推荐遵循 W3C 规范中的自定义组件名 (字母全小写且必须包含一个连字符)。这会帮助你避免和当前以及未来的 HTML 元素相冲突。

你可以在风格指南中查阅到关于组件名的其它建议。

当使用 kebab-case (短横线分隔命名) 定义一个组件时，你也必须在引用这个自定义元素时使用 kebab-case，例如 <my-component-name>。

当使用 PascalCase (首字母大写命名) 定义一个组件时，你在引用这个自定义元素时两种命名法都可以使用。也就是说 <my-component-name> 和 <MyComponentName> 都是可接受的。注意，尽管如此，直接在 DOM (即非字符串的模板) 中使用时只有 kebab-case 是有效的。

到目前为止，我们只用过 Vue.component 来创建组件：

这些组件是全局注册的。也就是说它们在注册之后可以用在任何新创建的 Vue 根实例 (new Vue) 的模板中。比如：

在所有子组件中也是如此，也就是说这三个组件在各自内部也都可以相互使用。

全局注册往往是不够理想的。比如，如果你使用一个像 webpack 这样的构建系统，全局注册所有的组件意味着即便你已经不再使用一个组件了，它仍然会被包含在你最终的构建结果中。这造成了用户下载的 JavaScript 的无谓的增加。

在这些情况下，你可以通过一个普通的 JavaScript 对象来定义组件：

然后在 components 选项中定义你想要使用的组件：

对于 components 对象中的每个 property 来说，其 property 名就是自定义元素的名字，其 property 值就是这个组件的选项对象。

注意局部注册的组件在其子组件中不可用。例如，如果你希望 ComponentA 在 ComponentB 中可用，则你需要这样写：

或者如果你通过 Babel 和 webpack 使用 ES2015 模块，那么代码看起来更像：

注意在 ES2015+ 中，在对象中放一个类似 ComponentA 的变量名其实是 ComponentA: ComponentA 的缩写，即这个变量名同时是：

如果你没有通过 import/require 使用一个模块系统，也许可以暂且跳过这个章节。如果你使用了，那么我们会为你提供一些特殊的使用说明和注意事项。

如果你还在阅读，说明你使用了诸如 Babel 和 webpack 的模块系统。在这些情况下，我们推荐创建一个 components 目录，并将每个组件放置在其各自的文件中。

然后你需要在局部注册之前导入每个你想使用的组件。例如，在一个假设的 ComponentB.js 或 ComponentB.vue 文件中：

现在 ComponentA 和 ComponentC 都可以在 ComponentB 的模板中使用了。

可能你的许多组件只是包裹了一个输入框或按钮之类的元素，是相对通用的。我们有时候会把它们称为基础组件，它们会在各个组件中被频繁的用到。

所以会导致很多组件里都会有一个包含基础组件的长列表：

如果你恰好使用了 webpack (或在内部使用了 webpack 的 Vue CLI 3+)，那么就可以使用 require.context 只全局注册这些非常通用的基础组件。这里有一份可以让你在应用入口文件 (比如 src/main.js) 中全局导入基础组件的示例代码：

记住全局注册的行为必须在根 Vue 实例 (通过 new Vue) 创建之前发生。这里有一个真实项目情景下的示例。

**Examples:**

Example 1 (unknown):
```unknown
Vue.component('my-component-name', { /* ... */ })
```

Example 2 (unknown):
```unknown
Vue.component('my-component-name', { /* ... */ })
```

Example 3 (unknown):
```unknown
Vue.component('MyComponentName', { /* ... */ })
```

Example 4 (unknown):
```unknown
Vue.component('my-component-name', {  // ... 选项 ...})
```

---

## Prop — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/components-props.html

**Contents:**
- Prop
- Prop 的大小写 (camelCase vs kebab-case)
- Prop 类型
- 传递静态或动态 Prop
  - 传入一个数字
  - 传入一个布尔值
  - 传入一个数组
  - 传入一个对象
  - 传入一个对象的所有 property
- 单向数据流

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

该页面假设你已经阅读过了组件基础。如果你还对组件不太了解，推荐你先阅读它。

HTML 中的 attribute 名是大小写不敏感的，所以浏览器会把所有大写字符解释为小写字符。这意味着当你使用 DOM 中的模板时，camelCase (驼峰命名法) 的 prop 名需要使用其等价的 kebab-case (短横线分隔命名) 命名：

重申一次，如果你使用字符串模板，那么这个限制就不存在了。

到这里，我们只看到了以字符串数组形式列出的 prop：

但是，通常你希望每个 prop 都有指定的值类型。这时，你可以以对象形式列出 prop，这些 property 的名称和值分别是 prop 各自的名称和类型：

这不仅为你的组件提供了文档，还会在它们遇到错误的类型时从浏览器的 JavaScript 控制台提示用户。你会在这个页面接下来的部分看到类型检查和其它 prop 验证。

像这样，你已经知道了可以像这样给 prop 传入一个静态的值：

你也知道 prop 可以通过 v-bind 动态赋值，例如：

在上述两个示例中，我们传入的值都是字符串类型的，但实际上任何类型的值都可以传给一个 prop。

如果你想要将一个对象的所有 property 都作为 prop 传入，你可以使用不带参数的 v-bind (取代 v-bind:prop-name)。例如，对于一个给定的对象 post：

所有的 prop 都使得其父子 prop 之间形成了一个单向下行绑定：父级 prop 的更新会向下流动到子组件中，但是反过来则不行。这样会防止从子组件意外变更父级组件的状态，从而导致你的应用的数据流向难以理解。

额外的，每次父级组件发生变更时，子组件中所有的 prop 都将会刷新为最新的值。这意味着你不应该在一个子组件内部改变 prop。如果你这样做了，Vue 会在浏览器的控制台中发出警告。

这里有两种常见的试图变更一个 prop 的情形：

这个 prop 用来传递一个初始值；这个子组件接下来希望将其作为一个本地的 prop 数据来使用。在这种情况下，最好定义一个本地的 data property 并将这个 prop 用作其初始值：

这个 prop 以一种原始的值传入且需要进行转换。在这种情况下，最好使用这个 prop 的值来定义一个计算属性：

注意在 JavaScript 中对象和数组是通过引用传入的，所以对于一个数组或对象类型的 prop 来说，在子组件中改变变更这个对象或数组本身将会影响到父组件的状态。

我们可以为组件的 prop 指定验证要求，例如你知道的这些类型。如果有一个需求没有被满足，则 Vue 会在浏览器控制台中警告你。这在开发一个会被别人用到的组件时尤其有帮助。

为了定制 prop 的验证方式，你可以为 props 中的值提供一个带有验证需求的对象，而不是一个字符串数组。例如：

当 prop 验证失败的时候，(开发环境构建版本的) Vue 将会产生一个控制台的警告。

注意那些 prop 会在一个组件实例创建之前进行验证，所以实例的 property (如 data、computed 等) 在 default 或 validator 函数中是不可用的。

type 可以是下列原生构造函数中的一个：

额外的，type 还可以是一个自定义的构造函数，并且通过 instanceof 来进行检查确认。例如，给定下列现成的构造函数：

来验证 author prop 的值是否是通过 new Person 创建的。

一个非 prop 的 attribute 是指传向一个组件，但是该组件并没有相应 prop 定义的 attribute。

因为显式定义的 prop 适用于向一个子组件传入信息，然而组件库的作者并不总能预见组件会被用于怎样的场景。这也是为什么组件可以接受任意的 attribute，而这些 attribute 会被添加到这个组件的根元素上。

例如，想象一下你通过一个 Bootstrap 插件使用了一个第三方的 <bootstrap-date-input> 组件，这个插件需要在其 <input> 上用到一个 data-date-picker attribute。我们可以将这个 attribute 添加到你的组件实例上：

然后这个 data-date-picker="activated" attribute 就会自动添加到 <bootstrap-date-input> 的根元素上。

想象一下 <bootstrap-date-input> 的模板是这样的：

为了给我们的日期选择器插件定制一个主题，我们可能需要像这样添加一个特别的类名：

在这种情况下，我们定义了两个不同的 class 的值：

对于绝大多数 attribute 来说，从外部提供给组件的值会替换掉组件内部设置好的值。所以如果传入 type="text" 就会替换掉 type="date" 并把它破坏！庆幸的是，class 和 style attribute 会稍微智能一些，即两边的值会被合并起来，从而得到最终的值：form-control date-picker-theme-dark。

如果你不希望组件的根元素继承 attribute，你可以在组件的选项中设置 inheritAttrs: false。例如：

这尤其适合配合实例的 $attrs property 使用，该 property 包含了传递给一个组件的 attribute 名和 attribute 值，例如：

有了 inheritAttrs: false 和 $attrs，你就可以手动决定这些 attribute 会被赋予哪个元素。在撰写基础组件的时候是常会用到的：

注意 inheritAttrs: false 选项不会影响 style 和 class 的绑定。

这个模式允许你在使用基础组件的时候更像是使用原始的 HTML 元素，而不会担心哪个元素是真正的根元素：

**Examples:**

Example 1 (unknown):
```unknown
Vue.component('blog-post', {  // 在 JavaScript 中是 camelCase 的  props: ['postTitle'],  template: '<h3>{{ postTitle }}</h3>'})
```

Example 2 (unknown):
```unknown
<!-- 在 HTML 中是 kebab-case 的 --><blog-post post-title="hello!"></blog-post>
```

Example 3 (unknown):
```unknown
props: ['title', 'likes', 'isPublished', 'commentIds', 'author']
```

Example 4 (unknown):
```unknown
props: {  title: String,  likes: Number,  isPublished: Boolean,  commentIds: Array,  author: Object,  callback: Function,  contactsPromise: Promise // or any other constructor}
```

---

## 深入响应式原理 — Vue.js

**URL:** https://v2.cn.vuejs.org/v2/guide/reactivity.html

**Contents:**
- 深入响应式原理
- 如何追踪变化
- 检测变化的注意事项
  - 对于对象
  - 对于数组
- 声明响应式 property
- 异步更新队列

您正在浏览的是 Vue 2.x 的文档。Vue 3 的文档在这里。

现在是时候深入一下了！Vue 最独特的特性之一，是其非侵入性的响应式系统。数据模型仅仅是普通的 JavaScript 对象。而当你修改它们时，视图会进行更新。这使得状态管理非常简单直接，不过理解其工作原理同样重要，这样你可以避开一些常见的问题。在这个章节，我们将研究一下 Vue 响应式系统的底层的细节。

当你把一个普通的 JavaScript 对象传入 Vue 实例作为 data 选项，Vue 将遍历此对象所有的 property，并使用 Object.defineProperty 把这些 property 全部转为 getter/setter。Object.defineProperty 是 ES5 中一个无法 shim 的特性，这也就是 Vue 不支持 IE8 以及更低版本浏览器的原因。

这些 getter/setter 对用户来说是不可见的，但是在内部它们让 Vue 能够追踪依赖，在 property 被访问和修改时通知变更。这里需要注意的是不同浏览器在控制台打印数据对象时对 getter/setter 的格式化并不同，所以建议安装 vue-devtools 来获取对检查数据更加友好的用户界面。

每个组件实例都对应一个 watcher 实例，它会在组件渲染的过程中把“接触”过的数据 property 记录为依赖。之后当依赖项的 setter 触发时，会通知 watcher，从而使它关联的组件重新渲染。

由于 JavaScript 的限制，Vue 不能检测数组和对象的变化。尽管如此我们还是有一些办法来回避这些限制并保证它们的响应性。

Vue 无法检测 property 的添加或移除。由于 Vue 会在初始化实例时对 property 执行 getter/setter 转化，所以 property 必须在 data 对象上存在才能让 Vue 将它转换为响应式的。例如：

对于已经创建的实例，Vue 不允许动态添加根级别的响应式 property。但是，可以使用 Vue.set(object, propertyName, value) 方法向嵌套对象添加响应式 property。例如，对于：

您还可以使用 vm.$set 实例方法，这也是全局 Vue.set 方法的别名：

有时你可能需要为已有对象赋值多个新 property，比如使用 Object.assign() 或 _.extend()。但是，这样添加到对象上的新 property 不会触发更新。在这种情况下，你应该用原对象与要混合进去的对象的 property 一起创建一个新的对象。

为了解决第一类问题，以下两种方式都可以实现和 vm.items[indexOfItem] = newValue 相同的效果，同时也将在响应式系统内触发状态更新：

你也可以使用 vm.$set 实例方法，该方法是全局方法 Vue.set 的一个别名：

为了解决第二类问题，你可以使用 splice：

由于 Vue 不允许动态添加根级响应式 property，所以你必须在初始化实例前声明所有根级响应式 property，哪怕只是一个空值：

如果你未在 data 选项中声明 message，Vue 将警告你渲染函数正在试图访问不存在的 property。

这样的限制在背后是有其技术原因的，它消除了在依赖项跟踪系统中的一类边界情况，也使 Vue 实例能更好地配合类型检查系统工作。但与此同时在代码可维护性方面也有一点重要的考虑：data 对象就像组件状态的结构 (schema)。提前声明所有的响应式 property，可以让组件代码在未来修改或给其他开发人员阅读时更易于理解。

可能你还没有注意到，Vue 在更新 DOM 时是异步执行的。只要侦听到数据变化，Vue 将开启一个队列，并缓冲在同一事件循环中发生的所有数据变更。如果同一个 watcher 被多次触发，只会被推入到队列中一次。这种在缓冲时去除重复数据对于避免不必要的计算和 DOM 操作是非常重要的。然后，在下一个的事件循环“tick”中，Vue 刷新队列并执行实际 (已去重的) 工作。Vue 在内部对异步队列尝试使用原生的 Promise.then、MutationObserver 和 setImmediate，如果执行环境不支持，则会采用 setTimeout(fn, 0) 代替。

例如，当你设置 vm.someData = 'new value'，该组件不会立即重新渲染。当刷新队列时，组件会在下一个事件循环“tick”中更新。多数情况我们不需要关心这个过程，但是如果你想基于更新后的 DOM 状态来做点什么，这就可能会有些棘手。虽然 Vue.js 通常鼓励开发人员使用“数据驱动”的方式思考，避免直接接触 DOM，但是有时我们必须要这么做。为了在数据变化之后等待 Vue 完成更新 DOM，可以在数据变化之后立即使用 Vue.nextTick(callback)。这样回调函数将在 DOM 更新完成后被调用。例如：

在组件内使用 vm.$nextTick() 实例方法特别方便，因为它不需要全局 Vue，并且回调函数中的 this 将自动绑定到当前的 Vue 实例上：

因为 $nextTick() 返回一个 Promise 对象，所以你可以使用新的 ES2017 async/await 语法完成相同的事情：

**Examples:**

Example 1 (unknown):
```unknown
var vm = new Vue({  data:{    a:1  }})// `vm.a` 是响应式的vm.b = 2// `vm.b` 是非响应式的
```

Example 2 (unknown):
```unknown
Vue.set(vm.someObject, 'b', 2)
```

Example 3 (unknown):
```unknown
this.$set(this.someObject,'b',2)
```

Example 4 (unknown):
```unknown
// 代替 `Object.assign(this.someObject, { a: 1, b: 2 })`this.someObject = Object.assign({}, this.someObject, { a: 1, b: 2 })
```

---
