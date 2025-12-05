# Claudecode-Help - Enterprise

**Pages:** 7

---

## Manage costs effectively

**URL:** https://code.claude.com/docs/en/costs

**Contents:**
- Manage costs effectively
- ​Track your costs
  - ​Using the /cost command
  - ​Additional tracking options
- ​Managing costs for teams
  - ​Rate limit recommendations
- ​Reduce token usage
- ​Background token usage
- ​Tracking version changes and updates
  - ​Current version information

Learn how to track and optimize token usage and costs when using Claude Code.

**Examples:**

Example 1 (unknown):
```unknown
Total cost:            $0.55
Total duration (API):  6m 19.7s
Total duration (wall): 6h 33m 10.2s
Total code changes:    0 lines added, 0 lines removed
```

Example 2 (unknown):
```unknown
# Summary instructions

When you are using compact, please focus on test output and code changes
```

Example 3 (unknown):
```unknown
claude doctor
```

---

## Data usage

**URL:** https://code.claude.com/docs/en/data-usage

**Contents:**
- Data usage
- ​Data policies
  - ​Data training policy
  - ​Development Partner Program
  - ​Feedback using the /bug command
  - ​Session quality surveys
  - ​Data retention
- ​Data flow and dependencies
  - ​Cloud execution
- ​Telemetry services

Learn about Anthropic’s data usage policies for Claude

---

## Monitoring

**URL:** https://code.claude.com/docs/en/monitoring-usage

**Contents:**
- Monitoring
- ​Quick Start
- ​Administrator Configuration
- ​Configuration Details
  - ​Common Configuration Variables
  - ​Metrics Cardinality Control
  - ​Dynamic Headers
    - ​Settings Configuration
    - ​Script Requirements
    - ​Important Limitations

Learn how to enable and configure OpenTelemetry for Claude Code.

**Examples:**

Example 1 (unknown):
```unknown
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console

# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"

# 5. For debugging: reduce export intervals
export OTEL_METRIC_EXPORT_INTERVAL=10000  # 10 seconds (default: 60000ms)
export OTEL_LOGS_EXPORT_INTERVAL=5000     # 5 seconds (default: 5000ms)

# 6. Run Claude Code
claude
```

Example 2 (unknown):
```unknown
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.company.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer company-token"
  }
}
```

Example 3 (unknown):
```unknown
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}
```

Example 4 (unknown):
```unknown
#!/bin/bash
# Example: Multiple headers
echo "{\"Authorization\": \"Bearer $(get-token.sh)\", \"X-API-Key\": \"$(get-api-key.sh)\"}"
```

---

## Analytics

**URL:** https://code.claude.com/docs/en/analytics

**Contents:**
- Analytics
- ​Access analytics
  - ​Required roles
- ​Available metrics
  - ​Lines of code accepted
  - ​Suggestion accept rate
  - ​Activity
  - ​Spend
  - ​Team insights
- ​Using analytics effectively

View detailed usage insights and productivity metrics for your organization’s Claude Code deployment.

---

## Security

**URL:** https://code.claude.com/docs/en/security

**Contents:**
- Security
- ​How we approach security
  - ​Security foundation
  - ​Permission-based architecture
  - ​Built-in protections
  - ​User responsibility
- ​Protect against prompt injection
  - ​Core protections
  - ​Privacy safeguards
  - ​Additional safeguards

Learn about Claude Code’s security safeguards and best practices for safe usage.

---

## Identity and Access Management

**URL:** https://code.claude.com/docs/en/iam

**Contents:**
- Identity and Access Management
- ​Authentication methods
  - ​Claude API authentication
  - ​Cloud provider authentication
- ​Access control and permissions
  - ​Permission system
  - ​Configuring permissions
    - ​Permission modes
    - ​Working directories
    - ​Tool-specific permission rules

Learn how to configure user authentication, authorization, and access controls for Claude Code in your organization.

---

## Legal and compliance

**URL:** https://code.claude.com/docs/en/legal-and-compliance

**Contents:**
- Legal and compliance
- ​Legal agreements
  - ​License
  - ​Commercial agreements
- ​Compliance
  - ​Healthcare compliance (BAA)
- ​Security and trust
  - ​Trust and safety
  - ​Security vulnerability reporting

Legal agreements, compliance certifications, and security information for Claude Code.

---
