# Verification Guide: Paper III Frozen Artifacts

## Requirements

- Python 3.8 or later
- No external dependencies required

## Quick Verification

```bash
cd core/frozen
python3 ceiling_scan.py
```

## Expected Output

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

All files should report `OK`.

## Paper III Claims Verified

| Metric | Expected | Description |
|--------|----------|-------------|
| Interior candidates | 171 | C(19,2) configurations with required anchors |
| L1 survivors | 24 | Pass: tail strictly decreasing |
| L2 survivors | 4 | Pass: g[-3] is Fibonacci |
| L3 survivors | 1 | Pass: all tail gaps ≥ 5 |

## Unique Configuration

```
Elements: {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
Gap vector: (1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5)
```

## Additional Verification Scripts

### Enumeration Core Test
```bash
python3 enumeration_core.py
```

### Axiom Drop Analysis
```bash
python3 axiom_drop.py
```

Note: Axiom drop analysis may take several minutes as it performs
exhaustive enumeration over C(36,12) ≈ 1.25 billion configurations
for each dropped axiom.

## Notes

- Mathematical classification results are independent of empirical validation.
- These frozen artifacts should not be modified.
- For questions, see AUDIT_MANIFEST.md or the referenced paper.
