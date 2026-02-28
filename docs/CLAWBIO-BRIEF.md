# 🦖 ClawBio Presentation Brief

![ClawBio Logo](../img/clawbio-logo.jpeg)

**Use this to brief anyone (or any AI) on what ClawBio is and why it matters.**

---

## What is OpenClaw?

OpenClaw is the fastest-growing open-source project in GitHub history, with 180,000+ stars. Created by Peter Steinberger, it's a generalist AI agent framework — think of it as an operating system for AI agents. It runs on your laptop, connects to messaging platforms (Telegram, WhatsApp, Slack, Discord), and lets you build persistent agents with memory, tools, and personality. It's LLM-agnostic (Claude, GPT, local models) and has a plugin architecture called **Skills** — modular capabilities you can install with one command.

## What is ClawBio?

ClawBio is the first bioinformatics-native skill library for AI agents. Built by Manuel Corpas (Senior Lecturer at University of Westminster, Turing Fellow), it's a curated collection of modular skills that wrap proven bioinformatics tools (Biopython, SAMtools, Seurat, AlphaFold) into composable, agent-orchestrated workflows.

**The key innovation**: everything runs locally on your machine. No genomic data leaves your laptop. No cloud uploads. No data exfiltration.

## The Problem It Solves

General-purpose AI agents are powerful but blind to biology. Three specific gaps:

1. **Privacy** — Genomic data is sensitive. Patient VCFs, proprietary variants, and unpublished findings cannot be sent to cloud APIs. We need local-first execution.
2. **Reproducibility** — Biology demands audit trails. Every analysis step must be logged, versioned, and exportable as a reproducible pipeline (Conda env + Singularity + Nextflow).
3. **Domain knowledge** — A generic agent doesn't know that VCF files need ancestry-aware annotation, or that single-cell data requires doublet removal before clustering.

## How It Works

You describe what you want in natural language. A Bio Orchestrator detects your file type, routes to the right specialist skill, runs the analysis, and produces a markdown report with figures, tables, and a full reproducibility bundle.

**Architecture**:
```
User request (natural language)
    → Bio Orchestrator (routing + planning)
        → Specialist Skill (Equity Scorer, VCF Annotator, etc.)
            → Output: Markdown report + figures + audit log + repro bundle
```

## 🦖 The Skills (7 production, 6 planned)

| Skill | Status | Tests | What it does |
|-------|--------|-------|-------------|
| Bio Orchestrator | **Production** | — | Routes requests to the right skill automatically |
| PharmGx Reporter | **Production** | 24 | Pharmacogenomic report: 12 genes, 51 drugs, CPIC guidelines |
| Equity Scorer | **Production** | 24 | HEIM diversity metrics from VCF/ancestry data (0-100 score) |
| NutriGx Advisor | **Production** | 9 | Personalised nutrition report from 23andMe/AncestryDNA/VCF — 40 SNPs across 13 nutrient domains |
| Metagenomics Profiler | **Production** | — | Shotgun metagenomics: Kraken2 + RGI + HUMAnN3 |
| Ancestry PCA | **Production** | — | PCA decomposition vs SGDP (345 samples, 164 global populations) |
| Semantic Similarity | **Production** | — | Semantic Isolation Index for 175 GBD diseases from 13.1M PubMed abstracts |
| VCF Annotator | Planned | — | Variant annotation with VEP and ancestry context |
| Lit Synthesizer | Planned | — | PubMed/bioRxiv search with LLM summarisation |
| scRNA Orchestrator | Planned | — | Seurat/Scanpy automation: QC, clustering, DE analysis |
| Struct Predictor | Planned | — | AlphaFold/Boltz protein structure prediction |
| Seq Wrangler | Planned | — | FastQC, alignment, BAM processing |
| Repro Enforcer | Planned | — | Export any analysis as Conda env + Singularity + Nextflow |

## Why It Matters (the equity argument)

86% of GWAS participants are European. Polygenic risk scores, drug targets, and clinical guidelines are biased towards one population. The **HEIM Index** (Health Equity Index for Minorities) gives researchers a single number to quantify this. Score your dataset. Report it alongside your demographics. Track it over time. There is a paper in review on this — but the tool is open source and runnable tonight.

## Five Design Principles

1. **Local-first** — All processing on your machine. No mandatory cloud.
2. **Modular** — Each skill does one thing well. Compose via the orchestrator.
3. **Reproducible** — Every analysis generates audit trails + exportable pipelines.
4. **Auditable** — Human-review checkpoints before destructive actions.
5. **Secure** — Minimal permissions. Containerisation recommended.

## For the Non-Technical Audience

Imagine you're a genomics researcher. Today, you either (a) write custom scripts from scratch every time, or (b) send your sensitive patient data to a cloud service you don't control. ClawBio is a third option: you tell an AI agent what you want in plain English, it runs the analysis on your own laptop using established tools, and gives you back a report with everything needed to reproduce the result. Your data never leaves your machine.

## For the Technical Audience

Each skill is a `SKILL.md` (YAML frontmatter + markdown instructions) plus Python scripts. The agent reads the SKILL.md to understand capabilities, invokes Python via shell commands, and pipes results into a unified report. Skills are platform-agnostic — they work with any agent that can read markdown and execute shell commands. The reproducibility contract guarantees every run produces `commands.sh`, `environment.yml`, `checksums.sha256`, and `analysis_log.md`.

## The Call to Action

The repo goes live on 26 February 2026. MIT licensed. Anyone can build a skill using the provided template. Wanted skills from the community: GWAS Pipeline (PLINK/REGENIE), Metagenomics Classifier (Kraken2/MetaPhlAn), Clinical Variant Reporter (ACMG), Pathway Enricher (GO/KEGG), Phylogenetics Builder (IQ-TREE/RAxML).

## Context for the Meetup

- **Event**: London Bioinformatics Meetup — "10 Tips for Becoming a Top 1% AI User"
- **Date**: 26 Feb 2026, 18:45-19:45, Cavendish Campus, University of Westminster
- **Talk structure**: Tips 1-7 cover AI fluency habits (Claude Code, CLAUDE.md, RAG memory, voice, automation, persistent agents, compounding output). Tips 8-10 pivot to *building* with AI — where ClawBio is announced as the centrepiece, with a live demo of the Equity Scorer and a call for community contributions.
- **Audience**: ~40-50 people, mix of bioinformaticians, computational biologists, data scientists, and curious non-specialists.
- **Key framing** (from Steinberger insights): "The system emerged from daily use, not from a grand plan." Frame iterative discovery. Position as builder, not just analyst. Keep it authentic — no AI polish, no AI-generated images. Fun as competitive advantage.
