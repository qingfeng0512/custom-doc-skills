# Claudecode-Help - Deployment

**Pages:** 4

---

## Claude Code on Google Vertex AI

**URL:** https://code.claude.com/docs/en/google-vertex-ai

**Contents:**
- Claude Code on Google Vertex AI
- ​Prerequisites
- ​Region Configuration
- ​Setup
  - ​1. Enable Vertex AI API
  - ​2. Request model access
  - ​3. Configure GCP credentials
  - ​4. Configure Claude Code
  - ​5. Model configuration
- ​IAM configuration

Learn about configuring Claude Code through Google Vertex AI, including setup, IAM configuration, and troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com
```

Example 2 (unknown):
```unknown
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

# When CLOUD_ML_REGION=global, override region for unsupported models
export VERTEX_REGION_CLAUDE_3_5_HAIKU=us-east5

# Optional: Override regions for other specific models
export VERTEX_REGION_CLAUDE_3_5_SONNET=us-east5
export VERTEX_REGION_CLAUDE_3_7_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_0_OPUS=europe-west1
export VERTEX_REGION_CLAUDE_4_0_SONNET=us-east5
export VERTEX_REGION_CLAUDE_4_1_OPUS=europe-west1
```

Example 3 (unknown):
```unknown
export ANTHROPIC_MODEL='claude-opus-4-1@20250805'
export ANTHROPIC_SMALL_FAST_MODEL='claude-haiku-4-5@20251001'
```

---

## Development containers

**URL:** https://code.claude.com/docs/en/devcontainer

**Contents:**
- Development containers
- ​Key features
- ​Getting started in 4 steps
- ​Configuration breakdown
- ​Security features
- ​Customization options
- ​Example use cases
  - ​Secure client work
  - ​Team onboarding
  - ​Consistent CI/CD environments

Learn about the Claude Code development container for teams that need consistent, secure environments.

---

## Sandboxing

**URL:** https://code.claude.com/docs/en/sandboxing

**Contents:**
- Sandboxing
- ​Overview
- ​Why sandboxing matters
- ​How it works
  - ​Filesystem isolation
  - ​Network isolation
  - ​OS-level enforcement
- ​Getting started
  - ​Enable sandboxing
  - ​Configure sandboxing

Learn how Claude Code’s sandboxed bash tool provides filesystem and network isolation for safer, more autonomous agent execution.

**Examples:**

Example 1 (unknown):
```unknown
{
  "sandbox": {
    "network": {
      "httpProxyPort": 8080,
      "socksProxyPort": 8081
    }
  }
}
```

Example 2 (unknown):
```unknown
npx @anthropic-ai/sandbox-runtime <command-to-sandbox>
```

---

## Claude Code on Amazon Bedrock

**URL:** https://code.claude.com/docs/en/amazon-bedrock

**Contents:**
- Claude Code on Amazon Bedrock
- ​Prerequisites
- ​Setup
  - ​1. Submit use case details
  - ​2. Configure AWS credentials
    - ​Advanced credential configuration
      - Example configuration
      - Configuration settings explained
  - ​3. Configure Claude Code
  - ​4. Model configuration

Learn about configuring Claude Code through Amazon Bedrock, including setup, IAM configuration, and troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
aws configure
```

Example 2 (unknown):
```unknown
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

Example 3 (unknown):
```unknown
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name
```

Example 4 (unknown):
```unknown
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```

---
