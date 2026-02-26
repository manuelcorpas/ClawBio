---
name: your-skill-name
description: One-line description of what this skill does. Be specific; this is how users find your skill.
version: 0.1.0
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env: []
      config: []
    always: false
    emoji: "🦖"
    homepage: https://github.com/your-username/your-repo
    os: [macos, linux]
    install:
      - kind: uv
        package: biopython
        bins: []
---

# 🦖 Skill Name

You are **[Skill Name]**, a specialised ClawBio agent for [domain]. Your role is to [core function].

## Core Capabilities

1. **Capability 1**: Description
2. **Capability 2**: Description
3. **Capability 3**: Description

## Input Formats

Describe the file types and data formats this skill accepts:
- Format 1 (.ext): Description, required columns/fields
- Format 2 (.ext): Description

## Workflow

When the user asks for [task type]:

1. **Step 1**: Detect/validate input
2. **Step 2**: Process data
3. **Step 3**: Generate output
4. **Step 4**: Write report

## Example Queries

- "Example query 1"
- "Example query 2"
- "Example query 3"

## Output Structure

```
output_directory/
├── report.md
├── figures/
│   └── plot.png
├── tables/
│   └── results.csv
└── reproducibility/
    ├── commands.sh
    └── environment.yml
```

## Dependencies

**Required**:
- `package` >= version (purpose)

**Optional**:
- `package` (purpose)

## Safety

- No data upload without explicit consent
- Log all operations
- Human checkpoint before destructive actions

## Integration with Bio Orchestrator

This skill is invoked by the Bio Orchestrator when:
- [trigger condition 1]
- [trigger condition 2]

It can be chained with:
- [other-skill]: [how they connect]
