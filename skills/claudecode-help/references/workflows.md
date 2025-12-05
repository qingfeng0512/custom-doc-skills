# Claudecode-Help - Workflows

**Pages:** 5

---

## Page Not Found

**URL:** https://code.claude.com/docs/common-workflows

**Contents:**
- Page Not Found

---

## Claude Code GitHub Actions

**URL:** https://code.claude.com/docs/en/github-actions

**Contents:**
- Claude Code GitHub Actions
- ​Why use Claude Code GitHub Actions?
- ​What can Claude do?
  - ​Claude Code Action
- ​Setup
- ​Quick setup
- ​Manual setup
- ​Upgrading from Beta
  - ​Essential changes
  - ​Breaking Changes Reference

Learn about integrating Claude Code into your development workflow with Claude Code GitHub Actions

Create a custom GitHub App (Recommended for 3P Providers)

Configure cloud provider authentication

Create workflow files

Google Vertex AI workflow

**Examples:**

Example 1 (unknown):
```unknown
- uses: anthropics/claude-code-action@beta
  with:
    mode: "tag"
    direct_prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    custom_instructions: "Follow our coding standards"
    max_turns: "10"
    model: "claude-sonnet-4-5-20250929"
```

Example 2 (unknown):
```unknown
- uses: anthropics/claude-code-action@v1
  with:
    prompt: "Review this PR for security issues"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    claude_args: |
      --system-prompt "Follow our coding standards"
      --max-turns 10
      --model claude-sonnet-4-5-20250929
```

Example 3 (unknown):
```unknown
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # Responds to @claude mentions in comments
```

Example 4 (unknown):
```unknown
name: Code Review
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "/review"
          claude_args: "--max-turns 5"
```

---

## Interactive mode

**URL:** https://code.claude.com/docs/en/interactive-mode

**Contents:**
- Interactive mode
- ​Keyboard shortcuts
  - ​General controls
  - ​Multiline input
  - ​Quick commands
- ​Vim editor mode
  - ​Mode switching
  - ​Navigation (NORMAL mode)
  - ​Editing (NORMAL mode)
- ​Command history

Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.

**Examples:**

Example 1 (unknown):
```unknown
! npm test
! git status
! ls -la
```

---

## Common workflows

**URL:** https://code.claude.com/docs/en/common-workflows

**Contents:**
- Common workflows
- ​Understand new codebases
  - ​Get a quick codebase overview
  - ​Find relevant code
- ​Fix bugs efficiently
- ​Refactor code
- ​Use specialized subagents
- ​Use Plan Mode for safe code analysis
  - ​When to use Plan Mode
  - ​How to use Plan Mode

Learn about common workflows with Claude Code.

Navigate to the project root directory

Ask for a high-level overview

Dive deeper into specific components

Ask Claude to find relevant files

Get context on how components interact

Understand the execution flow

Share the error with Claude

Ask for fix recommendations

Identify legacy code for refactoring

Get refactoring recommendations

Apply the changes safely

Verify the refactoring

View available subagents

Use subagents automatically

Explicitly request specific subagents

Create custom subagents for your workflow

Identify untested code

Generate test scaffolding

Add meaningful test cases

Summarize your changes

Generate a PR with Claude

Identify undocumented code

Generate documentation

Add an image to the conversation

Ask Claude to analyze the image

Use images for context

Get code suggestions from visual content

Reference a single file

Reference a directory

Reference MCP resources

Provide context and ask Claude to think

Refine the thinking with follow-up prompts

Continue the most recent conversation

Continue in non-interactive mode

Show conversation picker

Understand Git worktrees

Create a new worktree

Run Claude Code in each worktree

Run Claude in another worktree

Manage your worktrees

Use text format (default)

Use streaming JSON format

Create a commands directory in your project

Create a Markdown file for each command

Use your custom command in Claude Code

Create a command file with the $ARGUMENTS placeholder

Use the command with an issue number

Create a commands directory in your home folder

Create a Markdown file for each command

Use your personal custom command

**Examples:**

Example 1 (unknown):
```unknown
cd /path/to/project
```

Example 2 (unknown):
```unknown
> give me an overview of this codebase
```

Example 3 (unknown):
```unknown
> explain the main architecture patterns used here
```

Example 4 (unknown):
```unknown
> what are the key data models?
```

---

## Claude Code GitLab CI/CD

**URL:** https://code.claude.com/docs/en/gitlab-ci-cd

**Contents:**
- Claude Code GitLab CI/CD
- ​Why use Claude Code with GitLab?
- ​How it works
- ​What can Claude do?
- ​Setup
  - ​Quick setup
  - ​Manual setup (recommended for production)
- ​Example use cases
  - ​Turn issues into MRs
  - ​Get implementation help

Learn about integrating Claude Code into your development workflow with GitLab CI/CD

**Examples:**

Example 1 (unknown):
```unknown
stages:
  - ai

claude:
  stage: ai
  image: node:24-alpine3.21
  # Adjust rules to fit how you want to trigger the job:
  # - manual runs
  # - merge request events
  # - web/API triggers when a comment contains '@claude'
  rules:
    - if: '$CI_PIPELINE_SOURCE == "web"'
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    GIT_STRATEGY: fetch
  before_script:
    - apk update
    - apk add --no-cache git curl bash
    - npm install -g @anthropic-ai/claude-code
  script:
    # Optional: start a GitLab MCP server if your setup provides one
    - /bin/gitlab-mcp-server || true
    # Use AI_FLOW_* variables when invoking via web/API triggers with context payloads
    - echo "$AI_FLOW_INPUT for $AI_FLOW_CONTEXT on $AI_FLOW_EVENT"
    - >
      claude
      -p "${AI_FLOW_INPUT:-'Review this MR and implement the requested changes'}"
      --permission-mode acceptEdits
      --allowedTools "Bash(*) Read(*) Edit(*) Write(*) mcp__gitlab"
      --debug
```

Example 2 (unknown):
```unknown
@claude implement this feature based on the issue description
```

Example 3 (unknown):
```unknown
@claude suggest a concrete approach to cache the results of this API call
```

Example 4 (unknown):
```unknown
@claude fix the TypeError in the user dashboard component
```

---
