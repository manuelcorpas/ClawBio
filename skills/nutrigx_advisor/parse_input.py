"""
parse_input.py — Multi-format genetic data parser
Supports: 23andMe .txt, AncestryDNA .csv, standard VCF
Returns: dict mapping rsid -> genotype string (e.g. "AT", "TT")
"""

import csv
import re
from pathlib import Path


def detect_format(filepath: str) -> str:
    """Auto-detect genetic file format from header."""
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith("##fileformat=VCF"):
                return "vcf"
            if "rsid" in line.lower() and "chromosome" in line.lower() and "genotype" in line.lower():
                return "23andme"
            if "rsid" in line.lower() and "allele1" in line.lower():
                return "ancestry"
            if not line.startswith("#"):
                break
    # Fallback: infer from extension
    ext = Path(filepath).suffix.lower()
    if ext == ".vcf":
        return "vcf"
    if ext == ".csv":
        return "ancestry"
    return "23andme"


def parse_23andme(filepath: str) -> dict:
    """Parse 23andMe raw data file. Returns {rsid: genotype}."""
    genotypes = {}
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            rsid, chrom, pos, genotype = parts[0], parts[1], parts[2], parts[3]
            if rsid.startswith("rs"):
                genotypes[rsid] = genotype.replace("-", "")
    return genotypes


def parse_ancestry(filepath: str) -> dict:
    """Parse AncestryDNA raw data file. Returns {rsid: genotype}."""
    genotypes = {}
    with open(filepath, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter="\t")
        # Handle comment lines
        raw = f.read() if not hasattr(reader, 'fieldnames') else ""
    
    # Re-read skipping comments
    lines = []
    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            if not line.startswith("#"):
                lines.append(line)
    
    reader = csv.DictReader(lines, delimiter="\t")
    for row in reader:
        rsid = row.get("rsid", "").strip()
        allele1 = row.get("allele1", "").strip()
        allele2 = row.get("allele2", "").strip()
        if rsid.startswith("rs"):
            genotypes[rsid] = allele1 + allele2
    return genotypes


def parse_vcf(filepath: str) -> dict:
    """Parse VCF file, extracting GT field. Returns {rsid: genotype_bases}."""
    genotypes = {}
    chrom_col, pos_col, id_col, ref_col, alt_col, gt_col = 0, 1, 2, 3, 4, 9

    with open(filepath, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if line.startswith("##"):
                continue
            if line.startswith("#CHROM"):
                continue
            parts = line.split("\t")
            if len(parts) < 10:
                continue
            rsid = parts[id_col]
            if not rsid.startswith("rs"):
                continue
            ref = parts[ref_col]
            alts = parts[alt_col].split(",")
            alleles = [ref] + alts

            fmt = parts[8].split(":")
            gt_idx = fmt.index("GT") if "GT" in fmt else 0
            sample = parts[gt_col].split(":")[gt_idx]
            # Handle phased (|) or unphased (/)
            indices = re.split(r"[|/]", sample)
            try:
                called = "".join(alleles[int(i)] for i in indices if i != ".")
                genotypes[rsid] = called
            except (IndexError, ValueError):
                pass
    return genotypes


def parse_genetic_file(filepath: str, fmt: str = "auto") -> dict:
    """Parse genetic data file in any supported format."""
    if fmt == "auto":
        fmt = detect_format(filepath)
    
    parsers = {
        "23andme": parse_23andme,
        "ancestry": parse_ancestry,
        "vcf": parse_vcf,
    }
    
    if fmt not in parsers:
        raise ValueError(f"Unknown format: {fmt}. Choose from: {list(parsers.keys())}")
    
    return parsers[fmt](filepath)
