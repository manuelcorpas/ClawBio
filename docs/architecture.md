# 🦖 ClawBio Architecture

## Overview

ClawBio is a collection of modular AI agent skills for bioinformatics, designed around three principles: local-first execution, reproducible analysis, and composable workflows.

## System Design

```
                    ┌─────────────────────┐
                    │    User Request      │
                    │  (natural language)  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Bio Orchestrator   │
                    │  (routing + planning │
                    │   + report assembly) │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                 │
    ┌─────────▼───────┐ ┌─────▼──────┐ ┌───────▼────────┐
    │  Equity Scorer   │ │ Seq Wrangler│ │ Struct Predictor│
    │  VCF Annotator   │ │ scRNA Orch  │ │ Lit Synthesizer │
    │                  │ │             │ │ Repro Enforcer  │
    └─────────┬───────┘ └─────┬──────┘ └───────┬────────┘
              │                │                 │
              └────────────────┼────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Output Layer       │
                    │  - Markdown report   │
                    │  - Figures (PNG/SVG) │
                    │  - Audit log         │
                    │  - Repro bundle      │
                    └─────────────────────┘
```

## Routing Logic

The Bio Orchestrator routes requests based on:

1. **File extension**: `.vcf` -> equity-scorer/vcf-annotator, `.fastq` -> seq-wrangler, etc.
2. **Keyword matching**: "diversity" -> equity-scorer, "structure" -> struct-predictor, etc.
3. **User intent**: Explicit skill names override automatic routing.
4. **Chaining**: Multi-step requests trigger sequential skill invocation with output piping.

## Skill Independence

Every skill works standalone. The Bio Orchestrator adds:
- Automatic routing (user does not need to know skill names)
- Multi-skill chaining (pipe output of one skill to the next)
- Unified reporting (combine results from multiple skills)
- Reproducibility wrapping (Repro Enforcer applied automatically)

A user can invoke any skill directly without the orchestrator.

## Data Flow

```
Input File(s)
    │
    ▼
Validation (file type, format, size checks)
    │
    ▼
Processing (skill-specific computation)
    │
    ▼
Results (tables, metrics, intermediate files)
    │
    ▼
Visualisation (matplotlib/seaborn figures)
    │
    ▼
Report Assembly (markdown + embedded figures)
    │
    ▼
Reproducibility Export (conda env, commands, checksums)
    │
    ▼
Audit Log Append (timestamped action record)
```

## Privacy Model

ClawBio enforces a strict local-first privacy model:

- **No network calls** for data processing. All computation happens locally.
- **Optional network** only for: literature search (PubMed API), structure database queries (PDB/UniProt), and package installation.
- **Explicit consent** required before any data leaves the machine.
- **File access scoping**: Skills operate within the current working directory by default. Access to parent directories requires user confirmation.

## Reproducibility Contract

Every analysis produces:

1. **commands.sh**: Exact shell commands to reproduce the analysis without the agent.
2. **environment.yml**: Conda environment specification with pinned versions.
3. **checksums.sha256**: SHA-256 hashes of all input files.
4. **analysis_log.md**: Timestamped record of every action taken.

This means any result can be reproduced on any machine with the same inputs, independent of OpenClaw.

## Skill Packaging

Each skill is a directory containing:

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + markdown instructions
├── skill_name.py     # Optional: Python implementation
├── utils.py          # Optional: shared utilities
├── tests/            # Optional: test cases
│   └── test_skill.py
└── examples/         # Optional: example inputs/outputs
    ├── input.vcf
    └── expected_output.md
```

The SKILL.md is the primary artifact. The Python files are supporting code that the agent invokes via shell commands. This separation means:
- Skills can be reviewed as markdown (human-readable)
- Python code can be tested independently
- Skills work with any compatible agent platform, not just OpenClaw

## Integration with OpenBio

The existing [OpenBio skill](https://github.com/openclaw/skills) provides API access to:
- PDB (protein structures)
- UniProt (protein sequences and annotations)
- ChEMBL (bioactivity data)
- Pathway databases

ClawBio skills can call OpenBio for database lookups while keeping all computation local. For example, Struct Predictor might use OpenBio to fetch a reference structure from PDB, then run local AlphaFold for comparison.

## Extensibility

New skills follow the template at `templates/SKILL-TEMPLATE.md`. The Bio Orchestrator routing table is designed to be extended: add a new entry mapping file types or keywords to your skill, and the orchestrator routes to it automatically.

Community submissions go through ClawHub or direct PR to this repository. 🦖
