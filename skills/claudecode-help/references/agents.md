# Claudecode-Help - Agents

**Pages:** 2

---

## Subagents

**URL:** https://code.claude.com/docs/en/sub-agents

**Contents:**
- Subagents
- ​What are subagents?
- ​Key benefits
- Context preservation
- Specialized expertise
- Reusability
- Flexible permissions
- ​Quick start
- ​Subagent configuration
  - ​File locations

Create and use specialized AI subagents in Claude Code for task-specific workflows and improved context management.

Open the subagents interface

Select 'Create New Agent'

**Examples:**

Example 1 (unknown):
```unknown
> Use the code-reviewer subagent to check my recent changes
```

Example 2 (unknown):
```unknown
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

Example 3 (unknown):
```unknown
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
model: sonnet  # Optional - specify model alias or 'inherit'
permissionMode: default  # Optional - permission mode for the subagent
skills: skill1, skill2  # Optional - skills to auto-load
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.
```

Example 4 (unknown):
```unknown
# Create a project subagent
mkdir -p .claude/agents
echo '---
name: test-runner
description: Use proactively to run tests and fix failures
---

You are a test automation expert. When you see code changes, proactively run the appropriate tests. If tests fail, analyze the failures and fix them while preserving the original test intent.' > .claude/agents/test-runner.md

# Create a user subagent
mkdir -p ~/.claude/agents
# ... create subagent file
```

---

## Agent Skills

**URL:** https://code.claude.com/docs/en/skills

**Contents:**
- Agent Skills
- ​Prerequisites
- ​What are Agent Skills?
- ​Create a Skill
  - ​Personal Skills
  - ​Project Skills
  - ​Plugin Skills
- ​Write SKILL.md
- ​Add supporting files
- ​Restrict tool access with allowed-tools

Create, manage, and share Skills to extend Claude’s capabilities in Claude Code.

**Examples:**

Example 1 (unknown):
```unknown
mkdir -p ~/.claude/skills/my-skill-name
```

Example 2 (unknown):
```unknown
mkdir -p .claude/skills/my-skill-name
```

Example 3 (unknown):
```unknown
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this Skill.
```

Example 4 (unknown):
```unknown
my-skill/
├── SKILL.md (required)
├── reference.md (optional documentation)
├── examples.md (optional examples)
├── scripts/
│   └── helper.py (optional utility)
└── templates/
    └── template.txt (optional template)
```

---
