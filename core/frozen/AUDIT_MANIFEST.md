# Audit Manifest: Paper III Frozen Artifacts

**Author:** Emma Cecile
**ORCID:** 0009-0008-4120-9309
**Freeze Date:** 2026-01-23
**Paper Reference:** Paper III - "Uniqueness of the Coralia Configuration at Ceiling 35"

## Purpose

This directory contains frozen computational artifacts referenced by Paper III.
These files are provided verbatim for reproducibility and citation stability.

**DO NOT MODIFY** any files in this directory.

## Contents

| File | Description |
|------|-------------|
| `enumeration_core.py` | Core enumeration utilities and constants |
| `ceiling_scan.py` | Exhaustive enumeration at ceiling=35 with layered filtering |
| `axiom_drop.py` | Axiom necessity analysis |
| `survivor_tables.csv` | Tabulated survivors at each filter layer |
| `checksums.txt` | SHA256 checksums for verification |
| `AUDIT_MANIFEST.md` | This file |

## Mathematical Claims (Paper III)

The ceiling scan produces the following counts:

- **Interior candidates:** 171
- **L1 survivors:** 24 (after tail strictly decreasing filter)
- **L2 survivors:** 4 (after Fibonacci constraint on g[-3])
- **L3 survivors:** 1 (after tail minimum constraint)

**Unique Configuration:**
```
{0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
```

**Gap Vector:**
```
(1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5)
```

## Verification

To verify the outputs:

```bash
cd core/frozen
python3 ceiling_scan.py
```

Expected output:
```
Ceiling Scan - Paper III Frozen Artifact
==================================================
Running ceiling=35 scan...

Interior candidates: 171
L1 survivors: 24
L2 survivors: 4
L3 survivors: 1

Unique configuration: {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
Gap vector: (1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5)
```

## Checksum Verification

```bash
cd core/frozen
sha256sum -c checksums.txt
```

## Layer Definitions

### L0 (Interior Candidates)
- Size = 12
- Required anchors: {0, 1, 2, 3, 5, 7, 9, 12, 15, 35}
- Excluded elements: {4, 6, 8, 10, 11, 13, 14}
- Free slots: 2 elements from {16, 17, ..., 34}
- Count: C(19, 2) = 171

### L1 (Tail Strictly Decreasing)
- Last 3 gaps strictly decreasing: g[-3] > g[-2] > g[-1]

### L2 (Fibonacci Constraint)
- Third-to-last gap must be a Fibonacci number: g[-3] ∈ {0,1,2,3,5,8,13,21,34}

### L3 (Tail Minimum)
- All of last 3 gaps ≥ 5

## Related Papers

- **Paper I:** Existence and Uniqueness
  DOI: [10.5281/zenodo.18121786](https://doi.org/10.5281/zenodo.18121786)

- **Paper II:** Empirical Content of the Axioms
  DOI: [10.5281/zenodo.18150002](https://doi.org/10.5281/zenodo.18150002)

- **Paper III:** Uniqueness at Ceiling 35
  DOI: (pending Zenodo deposit)

## Notes

- Mathematical classification results are independent of empirical validation.
- Python version: 3.8+ (no external dependencies required)
- These artifacts are frozen for citation stability; do not modify.
