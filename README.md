<p align="center">
  <img src="img/clawbio-social-preview.png" alt="ClawBio" width="600">
</p>

<h3 align="center">🦖 ClawBio</h3>

<p align="center">
  <strong>The first bioinformatics-native AI agent skill library.</strong><br>
  Built on <a href="https://github.com/openclaw/openclaw">OpenClaw</a> (180k+ GitHub stars). Local-first. Privacy-focused. Reproducible.
</p>

<p align="center">
  <a href="#quick-start"><img src="https://img.shields.io/badge/python-3.9+-blue?logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
  <a href="https://clawhub.ai"><img src="https://img.shields.io/badge/ClawHub-4_skills-orange" alt="ClawHub Skills"></a>
  <a href="https://manuelcorpas.github.io/ClawBio/slides/"><img src="https://img.shields.io/badge/slides-London_Bioinformatics_Meetup-purple" alt="Slides"></a>
</p>

---

## The Problem

You read a paper. You want to reproduce Figure 3. So you:

1. Go to GitHub. Clone the repo.
2. Wrong Python version. Fix dependencies.
3. Need the reference data — where is it?
4. Download 2GB from Zenodo. **Link is dead.**
5. Email the first author. **Wait 3 weeks.**
6. Paths are hardcoded to `/home/jsmith/data/`.
7. Two days later: still broken. **You give up.**

Now imagine the same paper published a **skill**:

```bash
python ancestry_pca.py --demo --output fig3
# Figure 3 reproduced. Identical. SHA-256 verified. 30 seconds.
```

**That's ClawBio.** Every figure in your paper should be one command away from reproduction.

---

## 🦖 What Is ClawBio?

A **skill** is a domain expert's knowledge — frozen into code — that an AI agent executes correctly every time.

```
ChatGPT / Claude  = a smart generalist who guesses at bioinformatics
🦖 ClawBio skill  = a domain expert's proven pipeline that the AI executes
```

- **Local-first**: Your genomic data never leaves your laptop. No cloud uploads, no data exfiltration.
- **Reproducible**: Every analysis exports `commands.sh`, `environment.yml`, and SHA-256 checksums. Anyone can reproduce it without the agent.
- **Modular**: Each skill is a self-contained directory (`SKILL.md` + Python scripts) that plugs into the orchestrator.
- **MIT licensed**: Open-source, free, community-driven.

## Why Not Just Use ChatGPT?

Ask Claude to "profile my pharmacogenes from this 23andMe file." It'll write plausible Python. But:

- It **hallucinates** star allele calls and uses outdated CPIC guidelines
- It **forgets** CYP2D6 \*4 is no-function (not reduced)
- You spend **45 minutes debugging** its output
- No reproducibility bundle. No audit log. No checksums.

ClawBio encodes the correct bioinformatics decisions so the agent gets it right first time, every time.

---

## 🦖 Skills

| Skill | Status | Description |
|-------|--------|-------------|
| [Bio Orchestrator](skills/bio-orchestrator/) | **MVP** | Routes bioinformatics requests to the right specialist skill |
| [PharmGx Reporter](skills/pharmgx-reporter/) | **MVP** | Pharmacogenomic report: 12 genes, 51 drugs, CPIC guidelines |
| [Ancestry PCA](skills/ancestry-pca/) | **MVP** | PCA decomposition vs SGDP (345 samples, 164 global populations) |
| [Semantic Similarity](skills/semantic-sim/) | **MVP** | Semantic Isolation Index for 175 GBD diseases from 13.1M PubMed abstracts |
| [Equity Scorer](skills/equity-scorer/) | Planned | HEIM diversity metrics from VCF/ancestry data |
| [VCF Annotator](skills/vcf-annotator/) | Planned | Variant annotation with VEP, ClinVar, gnomAD + ancestry context |
| [Lit Synthesizer](skills/lit-synthesizer/) | Planned | PubMed/bioRxiv search with LLM summarisation and citation graphs |
| [scRNA Orchestrator](skills/scrna-orchestrator/) | Planned | Scanpy automation: QC, clustering, DE analysis, visualisation |
| [Struct Predictor](skills/struct-predictor/) | Planned | AlphaFold/Boltz local structure prediction |
| [Repro Enforcer](skills/repro-enforcer/) | Planned | Export any analysis as Conda env + Singularity + Nextflow pipeline |

---

## 🦖 MVP Skills in Detail

### PharmGx Reporter — *Personal Scale*

Generates a pharmacogenomic report from consumer genetic data (23andMe, AncestryDNA):

- Parses raw genetic data (auto-detects format)
- Extracts **31 pharmacogenomic SNPs** across **12 genes** (CYP2C19, CYP2D6, CYP2C9, VKORC1, SLCO1B1, DPYD, TPMT, UGT1A1, CYP3A5, CYP2B6, NUDT15, CYP1A2)
- Calls star alleles and determines metabolizer phenotypes
- Looks up **CPIC drug recommendations** for **51 medications**
- Zero dependencies. Runs in **< 1 second**.

```bash
python pharmgx_reporter.py --input demo_patient.txt --output report
```

**Demo result**: CYP2D6 \*4/\*4 (Poor Metabolizer) → **10 drugs AVOID** (codeine, tramadol, 7 TCAs, tamoxifen), 20 caution, 21 standard.

> ~7% of people are CYP2D6 Poor Metabolizers — codeine gives them zero pain relief. ~0.5% carry DPYD variants where standard 5-FU dose can be lethal. This skill catches both.

### Ancestry PCA — *Population Scale*

Runs principal component analysis on your cohort against the SGDP reference panel (345 samples, 164 global populations):

- Contig normalisation (chr1 vs 1)
- IBD removal (related individuals filtered)
- Common biallelic SNPs only
- Confidence ellipses per population
- Publication-quality **4-panel figure** generated instantly

```bash
python ancestry_pca.py --demo --output ancestry_report
```

**Demo result**: 736 Peruvian samples across 28 indigenous populations. Amazonian groups (Matzes, Awajun, Candoshi) sit in genetic space that no SGDP population occupies — genuinely underrepresented, not just in GWAS, but in the reference panels themselves.

### Semantic Similarity Index — *Systemic Scale*

Computes a Semantic Isolation Index for diseases using 13.1M PubMed abstracts and PubMedBERT embeddings (768-dim):

- **SII** (Semantic Isolation Index): higher = more isolated in literature
- **KTP** (Knowledge Transfer Potential): higher = more cross-disease spillover
- **RCC** (Research Clustering Coefficient): diversity of research approaches
- **Temporal Drift**: how research focus evolves over time
- Publication-quality **4-panel figure**

```bash
python semantic_sim.py --demo --output sem_report
```

**Key finding**: Neglected tropical diseases are **+38% more semantically isolated** (P < 0.0001, Cohen's d = 0.84). 14 of the 25 most isolated diseases are Global South priority conditions. Knowledge silos kill innovation — a malaria immunology breakthrough could help leishmaniasis, but the literatures don't talk to each other.

> Corpas et al. (2026). *HEIM: Health Equity Index for Measuring structural bias in biomedical research.* Under review.

---

## Quick Start

### Prerequisites

- [OpenClaw](https://github.com/openclaw/openclaw) installed and configured
- Python 3.9+
- Bioinformatics tools for your skill of choice (see individual SKILL.md files)

### Install and run

```bash
# Install a skill
openclaw install skills/pharmgx-reporter

# Run with natural language
openclaw "Profile the pharmacogenes in my 23andMe file at data/raw_genotype.txt"

# Or run directly
python skills/pharmgx-reporter/pharmgx_reporter.py --input data/raw_genotype.txt --output report
```

Every skill includes **demo data** so you can try it immediately without your own files.

---

## 🦖 Architecture

```
User: "Analyse the diversity in my VCF file"
         │
  ┌──────▼──────┐
  │  Bio         │  ← routes by file type + keywords
  │  Orchestrator│
  └──────┬──────┘
         │
  ┌──────▼──────────────────────────────────────────┐
  │                                                  │
  PharmGx    Ancestry    Semantic    Equity    VCF
  Reporter   PCA         Similarity  Scorer    Annotator ...
  │                                                  │
  └──────┬──────────────────────────────────────────┘
         │
  ┌──────▼──────┐
  │  Markdown    │  ← report + figures + checksums
  │  Report      │     + reproducibility bundle
  └─────────────┘
```

Each skill is standalone — the orchestrator routes to the right one, but every skill also works independently.

See [docs/architecture.md](docs/architecture.md) for the full design.

---

## Community Wanted Skills 🦖

We want skills from the bioinformatics community. If you work with genomics, proteomics, metabolomics, imaging, or clinical data — **wrap your pipeline as a skill**.

| Skill | What | Your expertise |
|-------|------|----------------|
| **claw-gwas** | PLINK/REGENIE automation | Statistical genetics |
| **claw-metagenomics** | Kraken2/MetaPhlAn wrapper | Microbiome |
| **claw-acmg** | Clinical variant classification | Clinical genomics |
| **claw-pathway** | GO/KEGG enrichment | Functional genomics |
| **claw-phylogenetics** | IQ-TREE/RAxML automation | Evolutionary biology |
| **claw-proteomics** | MaxQuant/DIA-NN | Proteomics |
| **claw-spatial** | Visium/MERFISH | Spatial transcriptomics |

See [CONTRIBUTING.md](CONTRIBUTING.md) for the submission process and [templates/SKILL-TEMPLATE.md](templates/SKILL-TEMPLATE.md) for the skill template.

---

## Presentation

ClawBio was announced at the **London Bioinformatics Meetup** on 26 February 2026.

- **Slides**: [manuelcorpas.github.io/ClawBio/slides/](https://manuelcorpas.github.io/ClawBio/slides/)
- **Talk**: *10 Tips for Becoming a Top 1% AI User* — with live demos of all three MVP skills

---

## Citation

If you use ClawBio in your research, please cite:

```bibtex
@software{clawbio_2026,
  author = {Corpas, Manuel},
  title = {ClawBio: An Open-Source Library of AI Agent Skills for Reproducible Bioinformatics},
  year = {2026},
  url = {https://github.com/ClawBio/ClawBio}
}
```

## Links

- 🦖 **Slides**: [manuelcorpas.github.io/ClawBio/slides/](https://manuelcorpas.github.io/ClawBio/slides/)
- [OpenClaw](https://github.com/openclaw/openclaw) — The agent platform
- [ClawHub](https://clawhub.ai) — Skill registry
- [HEIM Index](https://heim-index.org) — Health Equity Index for Minorities

## License

MIT — clone it, run it, build a skill, submit a PR. 🦖
