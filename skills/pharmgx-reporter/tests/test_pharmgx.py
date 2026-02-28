"""
test_pharmgx.py — Automated test suite for PharmGx Reporter

Run with: pytest skills/pharmgx-reporter/tests/test_pharmgx.py -v

Uses the FIXED demo patient (demo_patient.txt) with known genotypes
so that all assertions are deterministic and reproducible.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from pharmgx_reporter import (
    PGX_SNPS,
    GENE_DEFS,
    GUIDELINES,
    detect_format,
    parse_file,
    call_diplotype,
    call_phenotype,
    phenotype_to_key,
    lookup_drugs,
    generate_report,
)

DEMO = Path(__file__).parent.parent / "demo_patient.txt"


# ── Parsing ────────────────────────────────────────────────────────────────────

def test_detect_format_23andme():
    lines = DEMO.read_text().split("\n")
    assert detect_format(lines) == "23andme"


def test_parse_file_finds_all_pgx_snps():
    fmt, total_snps, pgx_snps = parse_file(str(DEMO))
    assert fmt == "23andme"
    assert total_snps == 30  # 31 data lines but one has genotype "--" or is skipped
    assert len(pgx_snps) == len(PGX_SNPS), (
        f"Expected {len(PGX_SNPS)} PGx SNPs, got {len(pgx_snps)}"
    )


def test_parse_file_genotype_values():
    _, _, pgx = parse_file(str(DEMO))
    # CYP2C19 *2 het
    assert pgx["rs4244285"]["genotype"] == "AG"
    # CYP2D6 *4 hom
    assert pgx["rs3892097"]["genotype"] == "TT"
    # VKORC1 het
    assert pgx["rs9923231"]["genotype"] == "GA"


# ── Star Allele Calling ───────────────────────────────────────────────────────

def _profiles():
    """Build profiles from demo patient for reuse across tests."""
    _, _, pgx = parse_file(str(DEMO))
    profiles = {}
    for gene in GENE_DEFS:
        diplotype = call_diplotype(gene, pgx)
        phenotype = call_phenotype(gene, diplotype)
        profiles[gene] = {"diplotype": diplotype, "phenotype": phenotype}
    return profiles


def test_cyp2c19_diplotype():
    """Demo patient: rs4244285 AG (*2 het), rest ref → *1/*2."""
    p = _profiles()
    assert p["CYP2C19"]["diplotype"] == "*1/*2"


def test_cyp2d6_diplotype():
    """Demo patient: rs3892097 TT (*4 hom) → *4/*4."""
    p = _profiles()
    assert p["CYP2D6"]["diplotype"] == "*4/*4"


def test_vkorc1_genotype():
    """Demo patient: rs9923231 GA → GA diplotype."""
    p = _profiles()
    assert p["VKORC1"]["diplotype"] == "GA"


def test_slco1b1_genotype():
    """Demo patient: rs4149056 TC → TC diplotype."""
    p = _profiles()
    assert p["SLCO1B1"]["diplotype"] == "TC"


def test_cyp3a5_diplotype():
    """Demo patient: rs776746 GG (*3 hom) → *3/*3."""
    p = _profiles()
    assert p["CYP3A5"]["diplotype"] == "*3/*3"


# ── Phenotype Assignment ──────────────────────────────────────────────────────

def test_cyp2c19_intermediate():
    p = _profiles()
    assert p["CYP2C19"]["phenotype"] == "Intermediate Metabolizer"


def test_cyp2d6_poor():
    p = _profiles()
    assert p["CYP2D6"]["phenotype"] == "Poor Metabolizer"


def test_vkorc1_intermediate_sensitivity():
    p = _profiles()
    assert p["VKORC1"]["phenotype"] == "Intermediate Warfarin Sensitivity"


def test_slco1b1_intermediate():
    p = _profiles()
    assert p["SLCO1B1"]["phenotype"] == "Intermediate Function"


def test_cyp3a5_nonexpressor():
    p = _profiles()
    assert p["CYP3A5"]["phenotype"] == "CYP3A5 Non-expressor"


def test_dpyd_normal():
    """All DPYD SNPs are ref → Normal Metabolizer."""
    p = _profiles()
    assert p["DPYD"]["phenotype"] == "Normal Metabolizer"


def test_tpmt_normal():
    p = _profiles()
    assert p["TPMT"]["phenotype"] == "Normal Metabolizer"


# ── Drug Recommendations ──────────────────────────────────────────────────────

def test_drug_lookup_returns_all_categories():
    p = _profiles()
    results = lookup_drugs(p)
    assert "standard" in results
    assert "caution" in results
    assert "avoid" in results
    total = sum(len(v) for v in results.values())
    assert total > 0


def test_clopidogrel_caution_for_intermediate():
    """CYP2C19 *1/*2 → Intermediate → Clopidogrel should be caution."""
    p = _profiles()
    results = lookup_drugs(p)
    clop = [d for d in results["caution"] if d["drug"] == "Clopidogrel"]
    assert len(clop) == 1, "Clopidogrel should be in caution list"


def test_codeine_avoid_for_poor_cyp2d6():
    """CYP2D6 *4/*4 → Poor Metabolizer → Codeine should be avoid."""
    p = _profiles()
    results = lookup_drugs(p)
    codeine = [d for d in results["avoid"] if d["drug"] == "Codeine"]
    assert len(codeine) == 1, "Codeine should be in avoid list for CYP2D6 PM"


def test_simvastatin_caution_for_intermediate_slco1b1():
    """SLCO1B1 TC → Intermediate → Simvastatin should be caution."""
    p = _profiles()
    results = lookup_drugs(p)
    simva = [d for d in results["caution"] if d["drug"] == "Simvastatin"]
    assert len(simva) == 1, "Simvastatin should be in caution list"


# ── Phenotype Key Mapping ─────────────────────────────────────────────────────

def test_phenotype_key_mapping():
    assert phenotype_to_key("Normal Metabolizer") == "normal_metabolizer"
    assert phenotype_to_key("Poor Metabolizer") == "poor_metabolizer"
    assert phenotype_to_key("High Warfarin Sensitivity") == "high_warfarin_sensitivity"
    assert phenotype_to_key("CYP3A5 Non-expressor") == "poor_metabolizer"
    assert phenotype_to_key("Normal (inferred)") == "normal_metabolizer"


# ── Report Generation ─────────────────────────────────────────────────────────

def test_report_contains_key_sections():
    _, _, pgx = parse_file(str(DEMO))
    p = _profiles()
    results = lookup_drugs(p)
    report = generate_report(str(DEMO), "23andme", 31, pgx, p, results)
    assert "# ClawBio PharmGx Report" in report
    assert "Drug Response Summary" in report
    assert "Gene Profiles" in report
    assert "Detected Variants" in report
    assert "Disclaimer" in report
    assert "Methods" in report
    assert "Reproducibility" in report


def test_report_contains_disclaimer():
    _, _, pgx = parse_file(str(DEMO))
    p = _profiles()
    results = lookup_drugs(p)
    report = generate_report(str(DEMO), "23andme", 31, pgx, p, results)
    assert "NOT a diagnostic device" in report


# ── Data Integrity ─────────────────────────────────────────────────────────────

def test_all_genes_have_phenotype_mappings():
    """Every gene in GENE_DEFS must have at least one phenotype."""
    for gene, gdef in GENE_DEFS.items():
        assert "phenotypes" in gdef, f"{gene} missing phenotypes"
        assert len(gdef["phenotypes"]) >= 2, f"{gene} has fewer than 2 phenotypes"


def test_all_guideline_drugs_reference_valid_genes():
    """Every drug in GUIDELINES must reference a gene in GENE_DEFS."""
    for drug, info in GUIDELINES.items():
        if info.get("special") == "warfarin":
            continue
        gene = info["gene"]
        assert gene in GENE_DEFS, f"{drug} references unknown gene {gene}"
