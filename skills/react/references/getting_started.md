# React - Getting Started

**Pages:** 2

---

## Installation

**URL:** https://react.dev/learn/installation

**Contents:**
- Installation
- Try React
- Creating a React App
- Build a React App from Scratch
- Add React to an existing project
  - Note
    - Should I use Create React App?
- Next steps

React has been designed from the start for gradual adoption. You can use as little or as much React as you need. Whether you want to get a taste of React, add some interactivity to an HTML page, or start a complex React-powered app, this section will help you get started.

You don’t need to install anything to play with React. Try editing this sandbox!

You can edit it directly or open it in a new tab by pressing the “Fork” button in the upper right corner.

Most pages in the React documentation contain sandboxes like this. Outside of the React documentation, there are many online sandboxes that support React: for example, CodeSandbox, StackBlitz, or CodePen.

To try React locally on your computer, download this HTML page. Open it in your editor and in your browser!

If you want to start a new React app, you can create a React app using a recommended framework.

If a framework is not a good fit for your project, you prefer to build your own framework, or you just want to learn the basics of a React app you can build a React app from scratch.

If want to try using React in your existing app or a website, you can add React to an existing project.

No. Create React App has been deprecated. For more information, see Sunsetting Create React App.

Head to the Quick Start guide for a tour of the most important React concepts you will encounter every day.

---

## Installation

**URL:** https://react.dev/learn/react-compiler/installation

**Contents:**
- Installation
  - You will learn
- Prerequisites
- Installation
- Basic Setup
  - Pitfall
  - Babel
  - Vite
  - Next.js
  - React Router

This guide will help you install and configure React Compiler in your React application.

React Compiler is designed to work best with React 19, but it also supports React 17 and 18. Learn more about React version compatibility.

Install React Compiler as a devDependency:

React Compiler is designed to work by default without any configuration. However, if you need to configure it in special circumstances (for example, to target React versions below 19), refer to the compiler options reference.

The setup process depends on your build tool. React Compiler includes a Babel plugin that integrates with your build pipeline.

React Compiler must run first in your Babel plugin pipeline. The compiler needs the original source information for proper analysis, so it must process your code before other transformations.

Create or update your babel.config.js:

If you use Vite, you can add the plugin to vite-plugin-react:

Alternatively, if you prefer a separate Babel plugin for Vite:

Please refer to the Next.js docs for more information.

Install vite-plugin-babel, and add the compiler’s Babel plugin to it:

A community webpack loader is now available here.

Please refer to Expo’s docs to enable and use the React Compiler in Expo apps.

React Native uses Babel via Metro, so refer to the Usage with Babel section for installation instructions.

Please refer to Rspack’s docs to enable and use the React Compiler in Rspack apps.

Please refer to Rsbuild’s docs to enable and use the React Compiler in Rsbuild apps.

React Compiler includes an ESLint rule that helps identify code that can’t be optimized. When the ESLint rule reports an error, it means the compiler will skip optimizing that specific component or hook. This is safe: the compiler will continue optimizing other parts of your codebase. You don’t need to fix all violations immediately. Address them at your own pace to gradually increase the number of optimized components.

Install the ESLint plugin:

If you haven’t already configured eslint-plugin-react-hooks, follow the installation instructions in the readme. The compiler rules are available in the recommended-latest preset.

The ESLint rule will:

After installation, verify that React Compiler is working correctly.

Components optimized by React Compiler will show a “Memo ✨” badge in React DevTools:

If the compiler is working:

You can also verify the compiler is running by checking your build output. The compiled code will include automatic memoization logic that the compiler adds automatically.

If a component is causing issues after compilation, you can temporarily opt it out using the "use no memo" directive:

This tells the compiler to skip optimization for this specific component. You should fix the underlying issue and remove the directive once resolved.

For more troubleshooting help, see the debugging guide.

Now that you have React Compiler installed, learn more about:

**Examples:**

Example 1 (unknown):
```unknown
npm install -D babel-plugin-react-compiler@latest
```

Example 2 (unknown):
```unknown
yarn add -D babel-plugin-react-compiler@latest
```

Example 3 (unknown):
```unknown
pnpm install -D babel-plugin-react-compiler@latest
```

Example 4 (unknown):
```unknown
module.exports = {  plugins: [    'babel-plugin-react-compiler', // must run first!    // ... other plugins  ],  // ... other config};
```

---
