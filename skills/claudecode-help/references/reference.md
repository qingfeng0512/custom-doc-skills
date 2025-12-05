# Claudecode-Help - Reference

**Pages:** 5

---

## App unavailable

**URL:** https://code.claude.com/docs/en/sdk/migration-guide

---

## CLI reference

**URL:** https://code.claude.com/docs/en/cli-reference

**Contents:**
- CLI reference
- ​CLI commands
- ​CLI flags
  - ​Agents flag format
  - ​System prompt flags
- ​See also

Complete reference for Claude Code command-line interface, including commands and flags.

**Examples:**

Example 1 (unknown):
```unknown
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "debugger": {
    "description": "Debugging specialist for errors and test failures.",
    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
  }
}'
```

Example 2 (unknown):
```unknown
claude --system-prompt "You are a Python expert who only writes type-annotated code"
```

Example 3 (unknown):
```unknown
claude -p --system-prompt-file ./prompts/code-review.txt "Review this PR"
```

Example 4 (unknown):
```unknown
claude --append-system-prompt "Always use TypeScript and include JSDoc comments"
```

---

## Slash commands

**URL:** https://code.claude.com/docs/en/slash-commands

**Contents:**
- Slash commands
- ​Built-in slash commands
- ​Custom slash commands
  - ​Syntax
    - ​Parameters
  - ​Command types
    - ​Project commands
    - ​Personal commands
  - ​Features
    - ​Namespacing

Control Claude’s behavior during an interactive session with slash commands.

**Examples:**

Example 1 (unknown):
```unknown
/<command-name> [arguments]
```

Example 2 (unknown):
```unknown
# Create a project command
mkdir -p .claude/commands
echo "Analyze this code for performance issues and suggest optimizations:" > .claude/commands/optimize.md
```

Example 3 (unknown):
```unknown
# Create a personal command
mkdir -p ~/.claude/commands
echo "Review this code for security vulnerabilities:" > ~/.claude/commands/security-review.md
```

Example 4 (unknown):
```unknown
# Command definition
echo 'Fix issue #$ARGUMENTS following our coding standards' > .claude/commands/fix-issue.md

# Usage
> /fix-issue 123 high-priority
# $ARGUMENTS becomes: "123 high-priority"
```

---

## Headless mode

**URL:** https://code.claude.com/docs/en/headless

**Contents:**
- Headless mode
- ​Overview
- ​Basic usage
- ​Configuration Options
- ​Multi-turn conversations
- ​Output Formats
  - ​Text Output (Default)
  - ​JSON Output
  - ​Streaming JSON Output
- ​Input Formats

Run Claude Code programmatically without interactive UI

**Examples:**

Example 1 (unknown):
```unknown
claude -p "Stage my changes and write a set of commits for them" \
  --allowedTools "Bash,Read" \
  --permission-mode acceptEdits
```

Example 2 (unknown):
```unknown
# Continue the most recent conversation
claude --continue "Now refactor this for better performance"

# Resume a specific conversation by session ID
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update the tests"

# Resume in non-interactive mode
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Fix all linting issues" --no-interactive
```

Example 3 (unknown):
```unknown
claude -p "Explain file src/components/Header.tsx"
# Output: This is a React component showing...
```

Example 4 (unknown):
```unknown
claude -p "How does the data layer work?" --output-format json
```

---

## Checkpointing

**URL:** https://code.claude.com/docs/en/checkpointing

**Contents:**
- Checkpointing
- ​How checkpoints work
  - ​Automatic tracking
  - ​Rewinding changes
- ​Common use cases
- ​Limitations
  - ​Bash command changes not tracked
  - ​External changes not tracked
  - ​Not a replacement for version control
- ​See also

Automatically track and rewind Claude’s edits to quickly recover from unwanted changes.

**Examples:**

Example 1 (unknown):
```unknown
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt
```

---
