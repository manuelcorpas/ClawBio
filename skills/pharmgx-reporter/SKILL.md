---
name: clawbio-pharmgx-reporter
version: 0.1.0
description: Pharmacogenomic report from DTC genetic data (23andMe/AncestryDNA)
author: Manuel Corpas
license: MIT
tags:
  - pharmacogenomics
  - CPIC
  - DTC-genetics
  - precision-medicine
inputs:
  - name: input
    type: file
    format: [23andme, ancestrydna, tsv]
    description: Raw genetic data file from 23andMe or AncestryDNA
outputs:
  - name: report
    type: file
    format: markdown
    description: Pharmacogenomic report with gene profiles and drug recommendations
metadata:
  openclaw:
    category: bioinformatics
    homepage: https://github.com/manuelcorpas/ClawBio
    min_python: "3.9"
    dependencies: []
---

# 🦖 PharmGx Reporter

Generate a pharmacogenomic report from consumer genetic data (23andMe, AncestryDNA).

## What it does

1. Parses raw genetic data files (auto-detects 23andMe or AncestryDNA format)
2. Extracts 31 pharmacogenomic SNPs across 12 genes
3. Calls star alleles and determines metabolizer phenotypes
4. Looks up CPIC drug recommendations for 51 medications
5. Generates a markdown report with gene profiles, drug tables, and alerts

## Genes covered

CYP2C19, CYP2D6, CYP2C9, VKORC1, SLCO1B1, DPYD, TPMT, UGT1A1, CYP3A5, CYP2B6, NUDT15, CYP1A2

## Drug classes

Antiplatelet, opioids, statins, anticoagulants, PPIs, antidepressants (TCAs, SSRIs, SNRIs), antipsychotics, NSAIDs, oncology, immunosuppressants, antivirals

## Usage

```bash
python pharmgx_reporter.py --input patient_data.txt --output report
```

## Disclaimer

This tool is for research and educational purposes only. It is NOT a diagnostic device. Always consult a healthcare professional before making any medication decisions.
