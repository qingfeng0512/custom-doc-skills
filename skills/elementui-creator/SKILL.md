---
name: elementui-creator
description: 用于创建 Element UI 组件和页面的技能。基于 Element UI 2.x 版本的完整文档，包含组件使用指南、API 文档和最佳实践。
---

# Element UI Creator Skill

Comprehensive assistance with Element UI 2.x development based on the official documentation. This skill provides guidance for creating Vue.js applications using Element UI components.

## When to Use This Skill

This skill should be triggered when:
- Working with Element UI in Vue.js applications
- Asking about Element UI components, APIs, or features
- Implementing UI solutions using Element UI components
- Debugging Element UI code or styling
- Learning Element UI best practices and patterns

## Quick Reference

### Common Patterns

#### Basic Component Setup
```vue
<template>
  <el-button @click="handleClick">Click me</el-button>
</template>

<script>
export default {
  methods: {
    handleClick() {
      this.$message('Button clicked!')
    }
  }
}
</script>
```

#### Form with Validation
```vue
<template>
  <el-form :model="form" :rules="rules" ref="form">
    <el-form-item label="Username" prop="username">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: ''
      },
      rules: {
        username: [
          { required: true, message: 'Please input username', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.$message.success('Form submitted successfully!')
        }
      })
    }
  }
}
</script>
```

#### Table with Pagination
```vue
<template>
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column prop="date" label="Date" width="180"></el-table-column>
    <el-table-column prop="name" label="Name" width="180"></el-table-column>
    <el-table-column prop="address" label="Address"></el-table-column>
  </el-table>
  <el-pagination
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    :current-page="currentPage"
    :page-sizes="[10, 20, 50, 100]"
    :page-size="pageSize"
    layout="total, sizes, prev, pager, next, jumper"
    :total="total">
  </el-pagination>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      currentPage: 1,
      pageSize: 10,
      total: 0
    }
  },
  methods: {
    handleSizeChange(val) {
      this.pageSize = val
      this.fetchData()
    },
    handleCurrentChange(val) {
      this.currentPage = val
      this.fetchData()
    },
    fetchData() {
      // API call to fetch data
    }
  }
}
</script>
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **getting_started.md** - Getting Started documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
Start with getting started concepts and basic component usage. Focus on:
- Basic component structure and props
- Form handling and validation
- Layout components (Container, Row, Col)
- Basic UI elements (Button, Input, Select)

### For Specific Features
Use the appropriate component category for detailed information:
- **Form Components**: Form, FormItem, Input, Select, Radio, Checkbox, DatePicker
- **Data Display**: Table, Pagination, Tag, Badge, Progress
- **Navigation**: Menu, Tabs, Breadcrumb, Steps
- **Feedback**: Dialog, Message, Notification, Loading
- **Layout**: Container, Row, Col, Card, Divider

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs. Key patterns include form validation, table handling, and basic component setup.

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

## Key Component Categories

### Layout Components
- **Container**: Layout container, supports 24-column grid
- **Row/Col**: Row and column grid layout
- **Divider**: Divider line component

### Form Components
- **Form**: Form component, supports data verification
- **FormItem**: Form item component
- **Input**: Input box component
- **Select**: Select dropdown component
- **Radio/RadioGroup**: Radio selection component
- **Checkbox/CheckboxGroup**: Checkbox component
- **DatePicker**: Date picker component

### Data Display
- **Table**: Table component, supports sorting, filtering, and selection
- **Pagination**: Pagination component
- **Tag**: Tag component
- **Badge**: Badge component
- **Progress**: Progress bar component

### Navigation
- **Menu**: Navigation menu
- **Tabs**: Tabbed navigation
- **Breadcrumb**: Breadcrumb navigation
- **Steps**: Step-by-step navigation

### Feedback
- **Dialog**: Dialog box component
- **Message**: Message prompt component
- **Notification**: Notification component
- **Loading**: Loading component

### Basic Elements
- **Button**: Button component with multiple types and sizes
- **Card**: Card container component
- **Alert**: Alert message component
- **Tooltip**: Tooltip component

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information

## Getting Help

For the most current documentation and API references, visit:
- Official documentation: https://element.eleme.cn/#/zh-CN/component/
- GitHub repository: https://github.com/ElemeFE/element
