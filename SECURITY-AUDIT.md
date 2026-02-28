# ClawBio Safety Audit: Silent Degradation Fixes

**Date**: 2026-02-28
**Commit**: `bbad73c`
**Scope**: All 4 production skills (PharmGx, Equity Scorer, NutriGx, Metagenomics)

## Background

A community review identified a systematic pattern across ClawBio skills: when encountering missing data, unknown values, or failed operations, the tools silently degraded to "everything is fine" defaults. Missing SNPs became reference-homozygous, unrecognised diplotypes became "Normal (inferred)", and failed subprocess calls became warnings.

This created a systematic bias toward **under-reporting risk and over-reporting normalcy**.

## Audit Methodology

Every function in all four production skills was examined for:
1. Missing input data treated as reference/normal
2. `.get()` defaults that hide missing information
3. `try/except` blocks that swallow errors and return optimistic results
4. Division-by-zero guards that fabricate values
5. Failed subprocesses downgraded to warnings

## Findings: 32 fixes across 4 skills

### PharmGx Reporter (11 fixes)

The most critical skill — drug safety recommendations.

| Severity | Finding | Fix |
|----------|---------|-----|
| **CRITICAL** | Zero PGx SNPs generated a full "all normal" report | Aborts with `sys.exit(1)` |
| **CRITICAL** | Missing SNPs → reference-homozygous (`*1/*1`) | Returns `NOT_TESTED` |
| **CRITICAL** | Missing DPYD → "Normal Metabolizer" (5-FU lethality risk) | Returns `Indeterminate (not genotyped)` |
| **CRITICAL** | Missing CYP2C9/VKORC1 → "Standard warfarin dose" | Returns `indeterminate` with clinical testing recommendation |
| **CRITICAL** | DEL/INS/TA7 variants always counted as 0 copies | Logged warning, variant skipped |
| **HIGH** | Unknown diplotype → "Normal (inferred)" | Returns `Unknown (unmapped diplotype: ...)` |
| **HIGH** | `phenotype_to_key` defaulted to `normal_metabolizer` | Defaults to `indeterminate` |
| **HIGH** | Missing phenotype in drug recs → "Use recommended dose" | Returns "Phenotype not covered by guidelines" |
| **HIGH** | Untested gene → drug silently omitted from report | Shows as `INSUFFICIENT DATA` |
| **HIGH** | Unknown file format → parsing proceeded anyway | Emits stderr warning |
| **MEDIUM** | Partial SNP coverage not indicated in diplotype | Annotated: e.g. `*1/*1 (2/4 SNPs tested)` |

**New features added:**
- `indeterminate` drug category for untested/unmapped genes
- Data Quality Warning section in report header
- Structural variant warnings logged to stderr

### Equity Scorer (7 fixes)

| Severity | Finding | Fix |
|----------|---------|-----|
| **CRITICAL** | 100% UNKNOWN populations scored 0.74/1.0 on representation | Sets to `None` with warning when >50% UNKNOWN |
| **CRITICAL** | CSV pipeline fabricated heterozygosity from hardcoded literature estimates | Labeled `literature_estimate` in report |
| **CRITICAL** | CSV pipeline claimed 100% FST coverage with no FST computed | Set to `0` (no FST computed) |
| **HIGH** | Missing GT field in VCF → used index 0 (wrong field) | Raises `ValueError` |
| **HIGH** | Division-by-zero → fabricated 0.0 allele frequency | Uses `NaN`, downstream uses `nanmean()` |
| **HIGH** | No polymorphic sites → FST = 0.0 ("identical populations") | Returns `NaN` |
| **HIGH** | Unmapped samples silently assigned UNKNOWN | Emits warning with count and percentage |

### NutriGx Advisor (8 fixes)

| Severity | Finding | Fix |
|----------|---------|-----|
| **CRITICAL** | Allele mismatch silently yielded `risk_count=0` (no risk) | Returns `status=allele_mismatch`, `risk_count=None` |
| **CRITICAL** | Zero panel coverage generated full report | Aborts with `sys.exit(1)` |
| **HIGH** | Unexpected `risk_count` values defaulted to 0.0 | Raises `ValueError` |
| **HIGH** | VCF parse errors silently dropped variants | Logged with variant details |
| **HIGH** | Unrecognised file format defaulted to 23andMe | Raises `ValueError` |
| **HIGH** | Missing GT in VCF FORMAT → used index 0 | Skips variant with warning |
| **HIGH** | Missing SNPs excluded from denominator, biasing scores low | Coverage qualifier added: e.g. `3/5 SNPs tested` |
| **MEDIUM** | Unknown domain → generic "no specific recommendation" | Shows `Insufficient genetic data to assess this domain` |

### Metagenomics Profiler (6 fixes)

| Severity | Finding | Fix |
|----------|---------|-----|
| **CRITICAL** | `run_command()` treated all failures as warnings | `critical=True` parameter; Kraken2/RGI raise `RuntimeError` |
| **CRITICAL** | Missing RGI output returned phantom file path | Raises `FileNotFoundError` |
| **CRITICAL** | Missing RGI file → empty DataFrame = "0 ARGs detected" | Reports `ANALYSIS FAILED: Resistome could not be profiled` |
| **HIGH** | Missing HUMAnN3 output returned fabricated path | Returns `None` |
| **HIGH** | Kraken2/Bracken did not verify output files exist | Post-run file existence check added |
| **HIGH** | HUMAnN3 database never validated | Validated like Kraken2; skip with note if missing |

**Report now distinguishes three states:**
- Analysis succeeded (normal output)
- Analysis failed (explicit `FAILED` banner)
- Analysis skipped by user (explicit `skipped` note)

## Design Principle

The core architectural fix: **distinguish "tested and found normal" from "never tested."**

Before this patch, every function in every pipeline treated these two states identically. After this patch:
- Missing data produces `NOT_TESTED`, `Indeterminate`, `NaN`, or `None`
- Reports include explicit Data Quality Warning sections
- Zero-data inputs abort instead of generating misleading reports
- Coverage qualifiers show how much data underlies each result

## Verification

- All 4 skills pass `ast.parse()` syntax validation
- PharmGx demo: 30/30 SNPs, 51 drugs assessed correctly
- PharmGx bad input: aborts with exit code 1 (zero SNPs)
- PharmGx safety regression: 7/7 tests pass (NOT_TESTED, Indeterminate, Unknown, warfarin, indeterminate drugs)
- Equity Scorer VCF demo: HEIM Score 76.2/100 with all figures
- Equity Scorer CSV demo: FST coverage now 0.0 (was 1.0), het labeled as literature estimate
- NutriGx demo: 23/28 SNPs found, 5 allele mismatches correctly flagged
- NutriGx empty input: aborts with exit code 1
- Metagenomics: syntax verified (requires external databases for full run)

## Disclaimer

ClawBio is a **research and educational tool**. It is not a medical device and does not provide clinical diagnoses. Consult a healthcare professional before making any medical decisions based on genetic data.
