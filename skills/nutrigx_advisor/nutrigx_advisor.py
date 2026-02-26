#!/usr/bin/env python3
"""
nutrigx_advisor.py — NutriGx Advisor: Personalised Nutrition from Genetic Data
ClawBio Skill v0.1.0

Usage:
    python nutrigx_advisor.py --input genome.txt --output results/
    python nutrigx_advisor.py --input variants.vcf --output results/ --format vcf
"""

import argparse
import json
import sys
from pathlib import Path

from parse_input import parse_genetic_file
from extract_genotypes import extract_snp_genotypes
from score_variants import compute_nutrient_risk_scores
from generate_report import generate_report
from repro_bundle import create_reproducibility_bundle


def main():
    parser = argparse.ArgumentParser(
        description="NutriGx Advisor — personalised nutrigenomics report from genetic data"
    )
    parser.add_argument(
        "--input", required=True,
        help="Path to genetic data file (23andMe .txt, AncestryDNA .csv, or .vcf)"
    )
    parser.add_argument(
        "--output", default="nutrigx_results",
        help="Output directory (created if absent)"
    )
    parser.add_argument(
        "--format", choices=["auto", "23andme", "ancestry", "vcf"], default="auto",
        help="Input file format (default: auto-detect)"
    )
    parser.add_argument(
        "--panel", default=None,
        help="Path to custom SNP panel JSON (default: data/snp_panel.json)"
    )
    parser.add_argument(
        "--no-figures", action="store_true",
        help="Skip figure generation (useful in headless environments)"
    )
    parser.add_argument(
        "--synthetic", action="store_true",
        help="Run on synthetic patient data (for testing)"
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Resolve SNP panel
    panel_path = Path(args.panel) if args.panel else Path(__file__).parent / "data" / "snp_panel.json"
    if not panel_path.exists():
        print(f"[ERROR] SNP panel not found at {panel_path}", file=sys.stderr)
        sys.exit(1)

    with open(panel_path) as f:
        snp_panel = json.load(f)

    input_path = Path(__file__).parent / "tests" / "synthetic_patient.txt" if args.synthetic else Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    print(f"[NutriGx] Parsing input: {input_path}")
    genotype_table = parse_genetic_file(str(input_path), fmt=args.format)
    print(f"[NutriGx] Loaded {len(genotype_table):,} variants")

    print("[NutriGx] Extracting SNP genotypes from panel ...")
    snp_calls = extract_snp_genotypes(genotype_table, snp_panel)

    present = sum(1 for v in snp_calls.values() if v["status"] == "found")
    print(f"[NutriGx] Panel coverage: {present}/{len(snp_panel)} SNPs found")

    print("[NutriGx] Computing nutrient risk scores ...")
    risk_scores = compute_nutrient_risk_scores(snp_calls, snp_panel)

    print("[NutriGx] Generating report ...")
    report_path = generate_report(
        snp_calls=snp_calls,
        risk_scores=risk_scores,
        snp_panel=snp_panel,
        output_dir=str(output_dir),
        figures=not args.no_figures,
        input_file=str(input_path)
    )

    print("[NutriGx] Creating reproducibility bundle ...")
    create_reproducibility_bundle(
        input_file=str(input_path),
        output_dir=str(output_dir),
        panel_path=str(panel_path),
        args=vars(args)
    )

    print(f"\n[NutriGx] ✓ Done. Report: {report_path}")
    print(f"[NutriGx] ✓ Results in: {output_dir}/")


if __name__ == "__main__":
    main()
