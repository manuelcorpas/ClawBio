# ClawBio PharmGx Report

**Date**: 2026-02-28 20:05 UTC
**Input**: `demo_patient.txt`
**Format detected**: 23andme
**Checksum (SHA-256)**: `4c2e9c8a7fd58de831187dd847e30509fe72c5aee09ff80d617caa4ae8a0eedb`
**Total SNPs in file**: 30
**Pharmacogenomic SNPs found**: 30/30
**Genes profiled**: 12
**Drugs assessed**: 51

---

## Drug Response Summary

| Category | Count |
|----------|-------|
| Standard dosing | 21 |
| Use with caution | 20 |
| Avoid / use alternative | 10 |

### Actionable Alerts

**AVOID / USE ALTERNATIVE:**

- **Codeine** (Tylenol w/ Codeine) [CYP2D6]: Avoid codeine. Select alternative analgesic.
- **Tramadol** (Ultram) [CYP2D6]: Avoid tramadol. Select alternative analgesic.
- **Tamoxifen** (Nolvadex) [CYP2D6]: Consider aromatase inhibitor or higher tamoxifen dose with TDM.
- **Amitriptyline** (Elavil) [CYP2D6]: Avoid TCA. If necessary, reduce dose 50%.
- **Nortriptyline** (Pamelor) [CYP2D6]: Avoid TCA or reduce dose 50%.
- **Desipramine** (Norpramin) [CYP2D6]: Avoid TCA or reduce dose 50%.
- **Imipramine** (Tofranil) [CYP2D6]: Avoid TCA or reduce dose 50%.
- **Doxepin** (Sinequan) [CYP2D6]: Avoid TCA or reduce dose 50%.
- **Trimipramine** (Surmontil) [CYP2D6]: Avoid TCA or reduce dose 50%.
- **Clomipramine** (Anafranil) [CYP2D6]: Avoid TCA or reduce dose 50%.

**USE WITH CAUTION:**

- **Clopidogrel** (Plavix) [CYP2C19]: Consider alternative antiplatelet therapy (prasugrel, ticagrelor).
- **Hydrocodone** (Vicodin) [CYP2D6]: Reduced analgesia likely; consider alternative.
- **Oxycodone** (OxyContin) [CYP2D6]: Reduced analgesia possible; consider alternative.
- **Paroxetine** (Paxil) [CYP2D6]: Consider 50% dose reduction or alternative SSRI.
- **Fluoxetine** (Prozac) [CYP2D6]: Consider 50% dose reduction or alternative.
- **Venlafaxine** (Effexor) [CYP2D6]: Consider 50% dose reduction or switch to desvenlafaxine.
- **Metoprolol** (Lopressor) [CYP2D6]: Consider 50% dose reduction or alternative beta-blocker.
- **Ondansetron** (Zofran) [CYP2D6]: May have reduced antiemetic effect; consider alternative.
- **Risperidone** (Risperdal) [CYP2D6]: Consider 50% dose reduction.
- **Aripiprazole** (Abilify) [CYP2D6]: Reduce dose to 75% of usual.
- **Haloperidol** (Haldol) [CYP2D6]: Reduce dose; monitor for side effects.
- **Atomoxetine** (Strattera) [CYP2D6]: Start at lower dose; 2-fold higher exposure expected.
- **Phenytoin** (Dilantin) [CYP2C9]: Reduce dose 25%. Monitor levels closely.
- **Celecoxib** (Celebrex) [CYP2C9]: Start at lowest dose.
- **Flurbiprofen** (Ansaid) [CYP2C9]: Start at lowest dose.
- **Piroxicam** (Feldene) [CYP2C9]: Start at lowest dose; monitor.
- **Meloxicam** (Mobic) [CYP2C9]: Start at lowest dose.
- **Warfarin** (Coumadin) [CYP2C9+VKORC1]: Reduce initial dose. Use genotype-guided dosing algorithm.
- **Simvastatin** (Zocor) [SLCO1B1]: Lower dose or alternative statin. 4.5x myopathy risk.
- **Atorvastatin** (Lipitor) [SLCO1B1]: Consider CK surveillance.

---

## Gene Profiles

| Gene | Full Name | Diplotype | Phenotype |
|------|-----------|-----------|-----------|
| CYP2C19 | Cytochrome P450 2C19 | *1/*2 | Intermediate Metabolizer |
| CYP2D6 | Cytochrome P450 2D6 | *4/*4 | Poor Metabolizer |
| CYP2C9 | Cytochrome P450 2C9 | *1/*3 | Intermediate Metabolizer |
| VKORC1 | Vitamin K Epoxide Reductase | GA | Intermediate Warfarin Sensitivity |
| SLCO1B1 | Solute Carrier Organic Anion Transporter 1B1 | TC | Intermediate Function |
| DPYD | Dihydropyrimidine Dehydrogenase | Normal/Normal | Normal Metabolizer |
| TPMT | Thiopurine S-Methyltransferase | *1/*1 | Normal Metabolizer |
| UGT1A1 | UDP-Glucuronosyltransferase 1A1 | *1/*1 | Normal Metabolizer |
| CYP3A5 | Cytochrome P450 3A5 | *3/*3 | CYP3A5 Non-expressor |
| CYP2B6 | Cytochrome P450 2B6 | *1/*1 | Normal Metabolizer |
| NUDT15 | Nudix Hydrolase 15 | *1/*1 | Normal Metabolizer |
| CYP1A2 | Cytochrome P450 1A2 | *1/*1F | Normal Metabolizer |

## Interactive ClinPGx Link

**Explore this patient's pharmacogenomic profile** with CPIC, DPWG, and FDA guideline annotations:

[Open in ClinPGx](https://www.clinpgx.org/genotypeResults?q=%7B%22CYP2C19%22%3A%20%5B%22%2A1%22%2C%20%22%2A2%22%2C%20null%5D%2C%20%22CYP2D6%22%3A%20%5B%22%2A4%22%2C%20%22%2A4%22%2C%20null%5D%2C%20%22CYP2C9%22%3A%20%5B%22%2A1%22%2C%20%22%2A3%22%2C%20null%5D%2C%20%22DPYD%22%3A%20%5B%22Normal%22%2C%20%22Normal%22%2C%20null%5D%2C%20%22TPMT%22%3A%20%5B%22%2A1%22%2C%20%22%2A1%22%2C%20null%5D%2C%20%22UGT1A1%22%3A%20%5B%22%2A1%22%2C%20%22%2A1%22%2C%20null%5D%2C%20%22CYP3A5%22%3A%20%5B%22%2A3%22%2C%20%22%2A3%22%2C%20null%5D%2C%20%22CYP2B6%22%3A%20%5B%22%2A1%22%2C%20%22%2A1%22%2C%20null%5D%2C%20%22NUDT15%22%3A%20%5B%22%2A1%22%2C%20%22%2A1%22%2C%20null%5D%2C%20%22CYP1A2%22%3A%20%5B%22%2A1%22%2C%20%22%2A1F%22%2C%20null%5D%7D)

This link pre-fills ClinPGx with the patient's genotypes. No data is uploaded; the genotypes are encoded in the URL itself.

### CPIC Gene References

| Gene | Diplotype | Phenotype | CPIC Guideline |
|------|-----------|-----------|----------------|
| CYP2C19 | *1/*2 | Intermediate Metabolizer | [CYP2C19 on CPIC](https://cpicpgx.org/gene/cyp2c19/) |
| CYP2D6 | *4/*4 | Poor Metabolizer | [CYP2D6 on CPIC](https://cpicpgx.org/gene/cyp2d6/) |
| CYP2C9 | *1/*3 | Intermediate Metabolizer | [CYP2C9 on CPIC](https://cpicpgx.org/gene/cyp2c9/) |
| VKORC1 | GA | Intermediate Warfarin Sensitivity | [VKORC1 on CPIC](https://cpicpgx.org/gene/vkorc1/) |
| SLCO1B1 | TC | Intermediate Function | [SLCO1B1 on CPIC](https://cpicpgx.org/gene/slco1b1/) |
| DPYD | Normal/Normal | Normal Metabolizer | [DPYD on CPIC](https://cpicpgx.org/gene/dpyd/) |
| TPMT | *1/*1 | Normal Metabolizer | [TPMT on CPIC](https://cpicpgx.org/gene/tpmt/) |
| UGT1A1 | *1/*1 | Normal Metabolizer | [UGT1A1 on CPIC](https://cpicpgx.org/gene/ugt1a1/) |
| CYP3A5 | *3/*3 | CYP3A5 Non-expressor | [CYP3A5 on CPIC](https://cpicpgx.org/gene/cyp3a5/) |
| CYP2B6 | *1/*1 | Normal Metabolizer | [CYP2B6 on CPIC](https://cpicpgx.org/gene/cyp2b6/) |
| NUDT15 | *1/*1 | Normal Metabolizer | [NUDT15 on CPIC](https://cpicpgx.org/gene/nudt15/) |
| CYP1A2 | *1/*1F | Normal Metabolizer | [CYP1A2 on CPIC](https://cpicpgx.org/gene/cyp1a2/) |

## Detected Variants

| rsID | Gene | Star Allele | Genotype | Effect |
|------|------|-------------|----------|--------|
| rs762551 | CYP1A2 | *1F | AC | increased_function |
| rs2069514 | CYP1A2 | *1C | GG | decreased_function |
| rs3745274 | CYP2B6 | *9 | GG | decreased_function |
| rs28399499 | CYP2B6 | *18 | TT | no_function |
| rs4244285 | CYP2C19 | *2 | AG | no_function |
| rs4986893 | CYP2C19 | *3 | GG | no_function |
| rs12248560 | CYP2C19 | *17 | CC | increased_function |
| rs28399504 | CYP2C19 | *4 | AA | no_function |
| rs1799853 | CYP2C9 | *2 | CC | decreased_function |
| rs1057910 | CYP2C9 | *3 | AC | decreased_function |
| rs3892097 | CYP2D6 | *4 | TT | no_function |
| rs5030655 | CYP2D6 | *6 | TT | no_function |
| rs16947 | CYP2D6 | *2 | GG | normal_function |
| rs1065852 | CYP2D6 | *10 | CC | decreased_function |
| rs28371725 | CYP2D6 | *41 | CC | decreased_function |
| rs776746 | CYP3A5 | *3 | GG | no_function |
| rs10264272 | CYP3A5 | *6 | GG | no_function |
| rs41303343 | CYP3A5 | *7 | CC | no_function |
| rs3918290 | DPYD | *2A | CC | no_function |
| rs55886062 | DPYD | *13 | TT | no_function |
| rs67376798 | DPYD | D949V | TT | decreased_function |
| rs116855232 | NUDT15 | *3 | CC | no_function |
| rs147390019 | NUDT15 | *2 | GG | decreased_function |
| rs4149056 | SLCO1B1 | *5 | TC | decreased_function |
| rs1800460 | TPMT | *3B | CC | no_function |
| rs1142345 | TPMT | *3C | AA | no_function |
| rs1800462 | TPMT | *2 | CC | no_function |
| rs8175347 | UGT1A1 | *28 | CC | decreased_function |
| rs4148323 | UGT1A1 | *6 | GG | decreased_function |
| rs9923231 | VKORC1 | -1639G>A | GA | decreased_expression |

---

## Complete Drug Recommendations

| Drug | Brand | Class | Gene | Status | Recommendation |
|------|-------|-------|------|--------|----------------|
| Amitriptyline | Elavil | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA. If necessary, reduce dose 50%. |
| Clomipramine | Anafranil | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Codeine | Tylenol w/ Codeine | Opioid Analgesic | CYP2D6 | AVOID | Avoid codeine. Select alternative analgesic. |
| Desipramine | Norpramin | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Doxepin | Sinequan | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Imipramine | Tofranil | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Nortriptyline | Pamelor | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Tamoxifen | Nolvadex | SERM (Oncology) | CYP2D6 | AVOID | Consider aromatase inhibitor or higher tamoxifen dose with TDM. |
| Tramadol | Ultram | Opioid Analgesic | CYP2D6 | AVOID | Avoid tramadol. Select alternative analgesic. |
| Trimipramine | Surmontil | Tricyclic Antidepressant | CYP2D6 | AVOID | Avoid TCA or reduce dose 50%. |
| Aripiprazole | Abilify | Antipsychotic | CYP2D6 | CAUTION | Reduce dose to 75% of usual. |
| Atomoxetine | Strattera | ADHD Medication | CYP2D6 | CAUTION | Start at lower dose; 2-fold higher exposure expected. |
| Atorvastatin | Lipitor | Statin | SLCO1B1 | CAUTION | Consider CK surveillance. |
| Celecoxib | Celebrex | NSAID | CYP2C9 | CAUTION | Start at lowest dose. |
| Clopidogrel | Plavix | Antiplatelet Agent | CYP2C19 | CAUTION | Consider alternative antiplatelet therapy (prasugrel, ticagrelor). |
| Fluoxetine | Prozac | SSRI Antidepressant | CYP2D6 | CAUTION | Consider 50% dose reduction or alternative. |
| Flurbiprofen | Ansaid | NSAID | CYP2C9 | CAUTION | Start at lowest dose. |
| Haloperidol | Haldol | Antipsychotic | CYP2D6 | CAUTION | Reduce dose; monitor for side effects. |
| Hydrocodone | Vicodin | Opioid Analgesic | CYP2D6 | CAUTION | Reduced analgesia likely; consider alternative. |
| Meloxicam | Mobic | NSAID | CYP2C9 | CAUTION | Start at lowest dose. |
| Metoprolol | Lopressor | Beta-Blocker | CYP2D6 | CAUTION | Consider 50% dose reduction or alternative beta-blocker. |
| Ondansetron | Zofran | Antiemetic | CYP2D6 | CAUTION | May have reduced antiemetic effect; consider alternative. |
| Oxycodone | OxyContin | Opioid Analgesic | CYP2D6 | CAUTION | Reduced analgesia possible; consider alternative. |
| Paroxetine | Paxil | SSRI Antidepressant | CYP2D6 | CAUTION | Consider 50% dose reduction or alternative SSRI. |
| Phenytoin | Dilantin | Antiepileptic | CYP2C9 | CAUTION | Reduce dose 25%. Monitor levels closely. |
| Piroxicam | Feldene | NSAID | CYP2C9 | CAUTION | Start at lowest dose; monitor. |
| Risperidone | Risperdal | Antipsychotic | CYP2D6 | CAUTION | Consider 50% dose reduction. |
| Simvastatin | Zocor | Statin | SLCO1B1 | CAUTION | Lower dose or alternative statin. 4.5x myopathy risk. |
| Venlafaxine | Effexor | SNRI Antidepressant | CYP2D6 | CAUTION | Consider 50% dose reduction or switch to desvenlafaxine. |
| Warfarin | Coumadin | Anticoagulant | CYP2C9+VKORC1 | CAUTION | Reduce initial dose. Use genotype-guided dosing algorithm. |
| Atazanavir | Reyataz | Antiretroviral | UGT1A1 | OK | Use recommended dose. |
| Azathioprine | Imuran | Immunosuppressant | TPMT | OK | Use recommended dose. |
| Capecitabine | Xeloda | Antineoplastic | DPYD | OK | Use recommended dose. |
| Citalopram | Celexa | SSRI Antidepressant | CYP2C19 | OK | Use recommended starting dose. |
| Clozapine | Clozaril | Antipsychotic | CYP1A2 | OK | Use recommended dose. |
| Dexlansoprazole | Dexilant | Proton Pump Inhibitor | CYP2C19 | OK | Use recommended starting dose. |
| Efavirenz | Sustiva | Antiretroviral | CYP2B6 | OK | Use recommended dose. |
| Escitalopram | Lexapro | SSRI Antidepressant | CYP2C19 | OK | Use recommended starting dose. |
| Esomeprazole | Nexium | Proton Pump Inhibitor | CYP2C19 | OK | Use recommended starting dose. |
| Fluorouracil | 5-FU | Antineoplastic | DPYD | OK | Use recommended dose. |
| Irinotecan | Camptosar | Antineoplastic | UGT1A1 | OK | Use recommended dose. |
| Lansoprazole | Prevacid | Proton Pump Inhibitor | CYP2C19 | OK | Use recommended starting dose. |
| Mercaptopurine | Purinethol | Immunosuppressant | TPMT | OK | Use recommended dose. |
| Omeprazole | Prilosec | Proton Pump Inhibitor | CYP2C19 | OK | Use recommended starting dose. |
| Pantoprazole | Protonix | Proton Pump Inhibitor | CYP2C19 | OK | Use recommended starting dose. |
| Pravastatin | Pravachol | Statin | SLCO1B1 | OK | Use desired starting dose. |
| Rosuvastatin | Crestor | Statin | SLCO1B1 | OK | Use desired starting dose. |
| Sertraline | Zoloft | SSRI Antidepressant | CYP2C19 | OK | Use recommended starting dose. |
| Tacrolimus | Prograf | Immunosuppressant | CYP3A5 | OK | Use recommended dose (most patients). |
| Thioguanine | Tabloid | Immunosuppressant | TPMT | OK | Use recommended dose. |
| Voriconazole | Vfend | Antifungal | CYP2C19 | OK | Use recommended dose. |

---

## Disclaimer

This report is for **research and educational purposes only**. It is NOT a diagnostic device and should NOT be used to make medication decisions without consulting a qualified healthcare professional.

Pharmacogenomic recommendations are based on CPIC guidelines (cpicpgx.org). DTC genetic tests have limitations: they may not detect all relevant variants, and results should be confirmed by clinical-grade testing before clinical use.

## Methods

- **Tool**: ClawBio PharmGx Reporter v0.1.0
- **SNP panel**: 31 pharmacogenomic variants across 12 genes
- **Star allele calling**: Simplified DTC-compatible algorithm (single-SNP per allele)
- **Phenotype assignment**: CPIC-based diplotype-to-phenotype mapping
- **Drug guidelines**: 51 drugs from CPIC (cpicpgx.org), simplified for DTC context

## Reproducibility

```bash
python pharmgx_reporter.py --input demo_patient.txt --output report
```

**Input checksum**: `4c2e9c8a7fd58de831187dd847e30509fe72c5aee09ff80d617caa4ae8a0eedb`

## References

- Corpas, M. (2026). ClawBio. https://github.com/ClawBio/ClawBio
- CPIC. Clinical Pharmacogenetics Implementation Consortium. https://cpicpgx.org/
- Caudle, K.E. et al. (2014). Standardizing terms for clinical pharmacogenetic test results. Genet Med, 16(9), 655-663.
- PharmGKB. https://www.pharmgkb.org/
- ClinPGx. Clinical Pharmacogenomics. https://www.clinpgx.org/
