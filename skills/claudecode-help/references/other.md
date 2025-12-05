# Claudecode-Help - Other

**Pages:** 5

---

## Claude Code on Microsoft Foundry

**URL:** https://code.claude.com/docs/en/microsoft-foundry

**Contents:**
- Claude Code on Microsoft Foundry
- ​Prerequisites
- ​Setup
  - ​1. Provision Microsoft Foundry resource
  - ​2. Configure Azure credentials
  - ​3. Configure Claude Code
- ​Azure RBAC configuration
- ​Troubleshooting
- ​Additional resources

Learn about configuring Claude Code through Microsoft Foundry, including setup, configuration, and troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
export ANTHROPIC_FOUNDRY_API_KEY=your-azure-api-key
```

Example 2 (unknown):
```unknown
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1

# Azure resource name (replace {resource} with your resource name)
export ANTHROPIC_FOUNDRY_RESOURCE={resource}
# Or provide the full base URL:
# export ANTHROPIC_FOUNDRY_BASE_URL=https://{resource}.services.ai.azure.com

# Set models to your resource's deployment names
export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-4-5'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5'
export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-1'
```

Example 3 (unknown):
```unknown
{
  "permissions": [
    {
      "dataActions": [
        "Microsoft.CognitiveServices/accounts/providers/*"
      ]
    }
  ]
}
```

---

## Claude Code on the web

**URL:** https://code.claude.com/docs/en/claude-code-on-the-web

**Contents:**
- Claude Code on the web
- ​What is Claude Code on the web?
- ​Who can use Claude Code on the web?
- ​Getting started
- ​How it works
- ​Moving tasks between web and terminal
  - ​From web to terminal
- ​Cloud environment
  - ​Default image
    - ​Checking available tools

Run Claude Code tasks asynchronously on secure cloud infrastructure

**Examples:**

Example 1 (unknown):
```unknown
check-tools
```

Example 2 (unknown):
```unknown
API_KEY=your_api_key
DEBUG=true
```

Example 3 (unknown):
```unknown
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh"
          }
        ]
      }
    ]
  }
}
```

Example 4 (unknown):
```unknown
#!/bin/bash
npm install
pip install -r requirements.txt
exit 0
```

---

## Page Not Found

**URL:** https://code.claude.com/docs/troubleshooting

**Contents:**
- Page Not Found

---

## Troubleshooting

**URL:** https://code.claude.com/docs/en/troubleshooting

**Contents:**
- Troubleshooting
- ​Common installation issues
  - ​Windows installation issues: errors in WSL
  - ​Linux and Mac installation issues: permission or command not found errors
    - ​Recommended solution: Native Claude Code installation
    - ​Alternative solution: Migrate to local installation
- ​Permissions and authentication
  - ​Repeated permission prompts
  - ​Authentication issues
- ​Performance and stability

Discover solutions to common issues with Claude Code installation and usage.

**Examples:**

Example 1 (unknown):
```unknown
# Load nvm if it exists
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

Example 2 (unknown):
```unknown
source ~/.nvm/nvm.sh
```

Example 3 (unknown):
```unknown
export PATH="$HOME/.nvm/versions/node/$(node -v)/bin:$PATH"
```

Example 4 (unknown):
```unknown
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

---

## Claude Code on desktop

**URL:** https://code.claude.com/docs/en/desktop

**Contents:**
- Claude Code on desktop
- ​Claude Code on desktop (Preview)
- ​Features
- ​Installation
- ​Using Git worktrees
  - ​Copying files ignored with .gitignore
  - ​Launch Claude Code on the web
- ​Bundled Claude Code version
  - ​Enterprise configuration
- ​Related resources

Run Claude Code tasks locally or on secure cloud infrastructure with the Claude desktop app

**Examples:**

Example 1 (unknown):
```unknown
.env
.env.local
.env.*
**/.claude/settings.local.json
```

---
