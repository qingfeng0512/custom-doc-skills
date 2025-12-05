# Claudecode-Help - Configuration

**Pages:** 10

---

## Claude Code settings

**URL:** https://code.claude.com/docs/en/settings

**Contents:**
- Claude Code settings
- ​Settings files
  - ​Available settings
  - ​Permission settings
  - ​Sandbox settings
  - ​Settings precedence
  - ​Key points about the configuration system
  - ​System prompt availability
  - ​Excluding sensitive files
- ​Subagent configuration

Configure Claude Code with global and project-level settings, and environment variables.

**Examples:**

Example 1 (unknown):
```unknown
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  },
  "companyAnnouncements": [
    "Welcome to Acme Corp! Review our code guidelines at docs.acme.com",
    "Reminder: Code reviews required for all PRs",
    "New security policy in effect"
  ]
}
```

Example 2 (unknown):
```unknown
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker"],
    "network": {
      "allowUnixSockets": [
        "/var/run/docker.sock"
      ],
      "allowLocalBinding": true
    }
  },
  "permissions": {
    "deny": [
      "Read(.envrc)",
      "Read(~/.aws/**)"
    ]
  }
}
```

Example 3 (unknown):
```unknown
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}
```

Example 4 (unknown):
```unknown
{
  "enabledPlugins": {
    "formatter@company-tools": true,
    "deployer@company-tools": true,
    "analyzer@security-plugins": false
  },
  "extraKnownMarketplaces": {
    "company-tools": {
      "source": "github",
      "repo": "company/claude-plugins"
    }
  }
}
```

---

## LLM gateway configuration

**URL:** https://code.claude.com/docs/en/llm-gateway

**Contents:**
- LLM gateway configuration
- ​Gateway requirements
- ​Configuration
  - ​Model selection
- ​LiteLLM configuration
  - ​Prerequisites
  - ​Basic LiteLLM setup
    - ​Authentication methods
      - Static API key
      - Dynamic API key with helper

Learn how to configure Claude Code to work with LLM gateway solutions. Covers gateway requirements, authentication configuration, model selection, and provider-specific endpoint setup.

**Examples:**

Example 1 (unknown):
```unknown
# Set in environment
export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key

# Or in Claude Code settings
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
  }
}
```

Example 2 (unknown):
```unknown
#!/bin/bash
# ~/bin/get-litellm-key.sh

# Example: Fetch key from vault
vault kv get -field=api_key secret/litellm/claude-code

# Example: Generate JWT token
jwt encode \
  --secret="${JWT_SECRET}" \
  --exp="+1h" \
  '{"user":"'${USER}'","team":"engineering"}'
```

Example 3 (unknown):
```unknown
{
  "apiKeyHelper": "~/bin/get-litellm-key.sh"
}
```

Example 4 (unknown):
```unknown
# Refresh every hour (3600000 ms)
export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000
```

---

## Model configuration

**URL:** https://code.claude.com/docs/en/model-config

**Contents:**
- Model configuration
- ​Available models
  - ​Model aliases
  - ​Setting your model
- ​Special model behavior
  - ​default model setting
  - ​opusplan model setting
  - ​Extended context with [1m]
- ​Checking your current model
- ​Environment variables

Learn about the Claude Code model configuration, including model aliases like opusplan

**Examples:**

Example 1 (unknown):
```unknown
# Start with Opus
claude --model opus

# Switch to Sonnet during session
/model sonnet
```

Example 2 (unknown):
```unknown
{
    "permissions": {
        ...
    },
    "model": "opus"
}
```

Example 3 (unknown):
```unknown
# Example of using a full model name with the [1m] suffix
/model anthropic.claude-sonnet-4-5-20250929-v1:0[1m]
```

---

## Hooks reference

**URL:** https://code.claude.com/docs/en/hooks

**Contents:**
- Hooks reference
- ​Configuration
  - ​Structure
  - ​Project-Specific Hook Scripts
  - ​Plugin hooks
- ​Prompt-Based Hooks
  - ​How prompt-based hooks work
  - ​Configuration
  - ​Response schema
  - ​Supported hook events

This page provides reference documentation for implementing hooks in Claude Code.

**Examples:**

Example 1 (unknown):
```unknown
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

Example 2 (unknown):
```unknown
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/prompt-validator.py"
          }
        ]
      }
    ]
  }
}
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
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-style.sh"
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
  "description": "Automatic code formatting",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

---

## Output styles

**URL:** https://code.claude.com/docs/en/output-styles

**Contents:**
- Output styles
- ​Built-in output styles
- ​How output styles work
- ​Change your output style
- ​Create a custom output style
  - ​Frontmatter
- ​Comparisons to related features
  - ​Output Styles vs. CLAUDE.md vs. —append-system-prompt
  - ​Output Styles vs. Agents
  - ​Output Styles vs. Custom Slash Commands

Adapt Claude Code for uses beyond software engineering

**Examples:**

Example 1 (unknown):
```unknown
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

---

## Enterprise network configuration

**URL:** https://code.claude.com/docs/en/network-config

**Contents:**
- Enterprise network configuration
- ​Proxy configuration
  - ​Environment variables
  - ​Basic authentication
- ​Custom CA certificates
- ​mTLS authentication
- ​Network access requirements
- ​Additional resources

Configure Claude Code for enterprise environments with proxy servers, custom Certificate Authorities (CA), and mutual Transport Layer Security (mTLS) authentication.

**Examples:**

Example 1 (unknown):
```unknown
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

Example 2 (unknown):
```unknown
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Example 3 (unknown):
```unknown
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

Example 4 (unknown):
```unknown
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

---

## Get started with Claude Code hooks

**URL:** https://code.claude.com/docs/en/hooks-guide

**Contents:**
- Get started with Claude Code hooks
- ​Hook Events Overview
- ​Quickstart
  - ​Prerequisites
  - ​Step 1: Open hooks configuration
  - ​Step 2: Add a matcher
  - ​Step 3: Add the hook
  - ​Step 4: Save your configuration
  - ​Step 5: Verify your hook
  - ​Step 6: Test your hook

Learn how to customize and extend Claude Code’s behavior by registering shell commands

**Examples:**

Example 1 (unknown):
```unknown
jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-command-log.txt
```

Example 2 (unknown):
```unknown
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-command-log.txt"
          }
        ]
      }
    ]
  }
}
```

Example 3 (unknown):
```unknown
cat ~/.claude/bash-command-log.txt
```

Example 4 (unknown):
```unknown
ls - Lists files and directories
```

---

## Status line configuration

**URL:** https://code.claude.com/docs/en/statusline

**Contents:**
- Status line configuration
- ​Create a custom status line
- ​How it Works
- ​JSON Input Structure
- ​Example Scripts
  - ​Simple Status Line
  - ​Git-Aware Status Line
  - ​Python Example
  - ​Node.js Example
  - ​Helper Function Approach

Create a custom status line for Claude Code to display contextual information

**Examples:**

Example 1 (javascript):
```javascript
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0 // Optional: set to 0 to let status line go to edge
  }
}
```

Example 2 (unknown):
```unknown
{
  "hook_event_name": "Status",
  "session_id": "abc123...",
  "transcript_path": "/path/to/transcript.json",
  "cwd": "/current/working/directory",
  "model": {
    "id": "claude-opus-4-1",
    "display_name": "Opus"
  },
  "workspace": {
    "current_dir": "/current/working/directory",
    "project_dir": "/original/project/directory"
  },
  "version": "1.0.80",
  "output_style": {
    "name": "default"
  },
  "cost": {
    "total_cost_usd": 0.01234,
    "total_duration_ms": 45000,
    "total_api_duration_ms": 2300,
    "total_lines_added": 156,
    "total_lines_removed": 23
  }
}
```

Example 3 (unknown):
```unknown
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}"
```

Example 4 (unknown):
```unknown
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract values using jq
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

# Show git branch if in a git repo
GIT_BRANCH=""
if git rev-parse --git-dir > /dev/null 2>&1; then
    BRANCH=$(git branch --show-current 2>/dev/null)
    if [ -n "$BRANCH" ]; then
        GIT_BRANCH=" | 🌿 $BRANCH"
    fi
fi

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}$GIT_BRANCH"
```

---

## Page Not Found

**URL:** https://code.claude.com/docs/settings

**Contents:**
- Page Not Found

---

## Manage Claude's memory

**URL:** https://code.claude.com/docs/en/memory

**Contents:**
- Manage Claude's memory
- ​Determine memory type
- ​CLAUDE.md imports
- ​How Claude looks up memories
- ​Quickly add memories with the # shortcut
- ​Directly edit memories with /memory
- ​Set up project memory
- ​Organization-level memory management
- ​Memory best practices

Learn how to manage Claude Code’s memory across sessions with different memory locations and best practices.

**Examples:**

Example 1 (unknown):
```unknown
See @README for project overview and @package.json for available npm commands for this project.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

Example 2 (unknown):
```unknown
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

Example 3 (unknown):
```unknown
This code span will not be treated as an import: `@anthropic-ai/claude-code`
```

Example 4 (unknown):
```unknown
# Always use descriptive variable names
```

---
