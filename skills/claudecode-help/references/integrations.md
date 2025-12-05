# Claudecode-Help - Integrations

**Pages:** 5

---

## JetBrains IDEs

**URL:** https://code.claude.com/docs/en/jetbrains

**Contents:**
- JetBrains IDEs
- ​Supported IDEs
- ​Features
- ​Installation
  - ​Marketplace Installation
  - ​Auto-Installation
- ​Usage
  - ​From Your IDE
  - ​From External Terminals
- ​Configuration

Use Claude Code with JetBrains IDEs including IntelliJ, PyCharm, WebStorm, and more

**Examples:**

Example 1 (unknown):
```unknown
claude
> /ide
```

---

## Plugins reference

**URL:** https://code.claude.com/docs/en/plugins-reference

**Contents:**
- Plugins reference
- ​Plugin components reference
  - ​Commands
  - ​Agents
  - ​Skills
  - ​Hooks
  - ​MCP servers
- ​Plugin manifest schema
  - ​Complete schema
  - ​Required fields

Complete technical reference for Claude Code plugin system, including schemas, CLI commands, and component specifications.

**Examples:**

Example 1 (unknown):
```unknown
---
description: What this agent specializes in
capabilities: ["task1", "task2", "task3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities
- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and examples
Provide examples of when this agent should be used and what kinds of problems it solves.
```

Example 2 (unknown):
```unknown
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (optional)
│   └── scripts/ (optional)
└── code-reviewer/
    └── SKILL.md
```

Example 3 (unknown):
```unknown
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

Example 4 (unknown):
```unknown
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

---

## Plugins

**URL:** https://code.claude.com/docs/en/plugins

**Contents:**
- Plugins
- ​Quickstart
  - ​Prerequisites
  - ​Create your first plugin
  - ​Plugin structure overview
- ​Install and manage plugins
  - ​Prerequisites
  - ​Add marketplaces
  - ​Install plugins
    - ​Via interactive menu (recommended for discovery)

Extend Claude Code with custom commands, agents, hooks, Skills, and MCP servers through the plugin system.

Create the marketplace structure

Create the plugin directory

Create the plugin manifest

Create the marketplace manifest

Install and test your plugin

Set up your development structure

Create the marketplace manifest

Iterate on your plugin

**Examples:**

Example 1 (unknown):
```unknown
mkdir test-marketplace
cd test-marketplace
```

Example 2 (unknown):
```unknown
mkdir my-first-plugin
cd my-first-plugin
```

Example 3 (unknown):
```unknown
mkdir .claude-plugin
cat > .claude-plugin/plugin.json << 'EOF'
{
"name": "my-first-plugin",
"description": "A simple greeting plugin to learn the basics",
"version": "1.0.0",
"author": {
"name": "Your Name"
}
}
EOF
```

Example 4 (unknown):
```unknown
mkdir commands
cat > commands/hello.md << 'EOF'
---
description: Greet the user with a personalized message
---

# Hello Command

Greet the user warmly and ask how you can help them today. Make the greeting personal and encouraging.
EOF
```

---

## Plugin marketplaces

**URL:** https://code.claude.com/docs/en/plugin-marketplaces

**Contents:**
- Plugin marketplaces
- ​Overview
  - ​Prerequisites
- ​Add and use marketplaces
  - ​Add GitHub marketplaces
  - ​Add Git repositories
  - ​Add local marketplaces for development
  - ​Install plugins from marketplaces
  - ​Verify marketplace installation
  - ​Example plugin marketplace

Create and manage plugin marketplaces to distribute Claude Code extensions across teams and communities.

**Examples:**

Example 1 (unknown):
```unknown
/plugin marketplace add owner/repo
```

Example 2 (unknown):
```unknown
/plugin marketplace add https://gitlab.com/company/plugins.git
```

Example 3 (unknown):
```unknown
/plugin marketplace add ./my-marketplace
```

Example 4 (unknown):
```unknown
/plugin marketplace add ./path/to/marketplace.json
```

---

## Visual Studio Code

**URL:** https://code.claude.com/docs/en/vs-code

**Contents:**
- Visual Studio Code
- ​VS Code Extension (Beta)
  - ​Features
  - ​Requirements
  - ​Installation
  - ​How It Works
  - ​Using Third-Party Providers
    - ​Environment Variables
  - ​Not Yet Implemented
- ​Security Considerations

Use Claude Code with Visual Studio Code through our native extension or CLI integration

---
