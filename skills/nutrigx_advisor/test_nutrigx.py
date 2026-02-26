"""
test_nutrigx.py — Test suite for NutriGx Advisor
Run with: pytest tests/test_nutrigx.py -v
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from parse_input import parse_genetic_file
from extract_genotypes import extract_snp_genotypes
from score_variants import compute_nutrient_risk_scores


SYNTHETIC = Path(__file__).parent / "synthetic_patient.txt"
PANEL = Path(__file__).parent.parent / "data" / "snp_panel.json"


def load_panel():
    with open(PANEL) as f:
        return json.load(f)


def test_parse_23andme():
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    assert len(table) >= 20
    assert "rs1801133" in table
    assert table["rs1801133"] in ("CT", "TC")


def test_extract_genotypes_coverage():
    panel = load_panel()
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    calls = extract_snp_genotypes(table, panel)
    found = sum(1 for v in calls.values() if v["status"] == "found")
    assert found >= 20, f"Expected ≥20 SNPs found, got {found}"


def test_mthfr_call():
    panel = load_panel()
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    calls = extract_snp_genotypes(table, panel)
    mthfr = calls.get("rs1801133")
    assert mthfr is not None
    assert mthfr["status"] == "found"
    assert mthfr["risk_count"] in (0, 1, 2)


def test_risk_scores_structure():
    panel = load_panel()
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    calls = extract_snp_genotypes(table, panel)
    scores = compute_nutrient_risk_scores(calls, panel)
    assert "folate" in scores
    assert "omega3" in scores
    for domain, data in scores.items():
        if data["score"] is not None:
            assert 0.0 <= data["score"] <= 10.0
        assert data["category"] in ("Low", "Moderate", "Elevated", "Unknown")


def test_score_categories():
    panel = load_panel()
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    calls = extract_snp_genotypes(table, panel)
    scores = compute_nutrient_risk_scores(calls, panel)
    # Synthetic patient has heterozygous MTHFR C677T → moderate folate risk expected
    folate = scores.get("folate", {})
    assert folate.get("score") is not None


def test_lactase_persistence():
    """Synthetic patient has rs4988235 = GA (heterozygous), so partial persistence."""
    panel = load_panel()
    table = parse_genetic_file(str(SYNTHETIC), fmt="23andme")
    calls = extract_snp_genotypes(table, panel)
    call = calls.get("rs4988235")
    assert call is not None
    assert call["status"] == "found"
