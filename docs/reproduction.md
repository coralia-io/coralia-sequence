# Reproduction Guide

This guide explains how to reproduce the classification results from Papers I–III.

## Requirements

- Python 3.7 or later
- No external dependencies (standard library only)

## Quick Verification

Run all verification scripts:

```bash
python frozen/code/enumeration_core.py
python frozen/code/ceiling_scan.py
python frozen/code/axiom_drop.py
```

## Detailed Instructions

### Paper I: Uniqueness Verification

Verify that exactly one 12-element subset of {0, ..., 35} satisfies axioms C1–C9:

```bash
python frozen/code/enumeration_core.py
```

**Expected output:**
```
Solutions: 1
```

The script performs exhaustive search over all (26 choose 2) = 325 candidate pairs that could complete the required seed set.

### Paper II: Landing Demonstration

See where mathematical constants land relative to C:

```bash
python examples/landing_demo.py
```

**Expected output:**
```
Where do these land?

  e² = 7.39 → lands on 7 ∈ C
  e^π = 23.14 → lands on 23 ∈ C
  φ⁵ = 11.09 → lands on 11 ∈ not C
```

### Paper III: Axiom Independence

Test which axioms are necessary for uniqueness:

```bash
python frozen/code/axiom_drop.py
```

**Expected output:**
```
Axiom independence test: survivors when each axiom is dropped
------------------------------------------------------------
Drop C1  :   1 survivor(s) — dependent
Drop C2  :   1 survivor(s) — dependent
...
Drop C7  :   2 survivor(s) — INDEPENDENT
Drop C8  :   3 survivor(s) — INDEPENDENT
Drop C9  :   4 survivor(s) — INDEPENDENT
```

### Paper III: Ceiling Scan

Verify that ceiling=35 is the unique value yielding exactly one solution:

```bash
python frozen/code/ceiling_scan.py
```

**Expected output:**
```
Ceiling scan: solutions per ceiling value
----------------------------------------
ceiling=30: 0 solution(s)
ceiling=31: 0 solution(s)
...
ceiling=35: 1 solution(s) ← unique
...
ceiling=40: 0 solution(s)
```

## File Integrity Verification

Verify frozen files have not been modified:

```bash
cd frozen
sha256sum -c <<EOF
0910fa57f3c197deb2e2092356ed2ce573a070eaae9705599bd1ea0635c7295a  code/axiom_drop.py
9fdee17f0c28e38e670bb613285a54f4468cd6e6cd2161301d9f613973ff4297  code/cascade_triple_enum.py
efff6a3aa1839ab25e909d9e092fe0046711bf4506091482873c6071bdda095b  code/ceiling_scan.py
8dddad1141f4c714196bfc17e7319a637f33f7ac2e67f6413f3f560efa17dc69  code/enumeration_core.py
7ed30606b774568c7c54da91eb39c6d787e6a12c5ca5f9ffa29a6ce9f4dd852d  data/survivor_tables.csv
EOF
```

All checks should pass. See [`frozen/AUDIT_MANIFEST.md`](../frozen/AUDIT_MANIFEST.md) for the complete manifest.

## Running Tests

Run the axiom test suite:

```bash
python core/tests/test_axioms.py
```

**Expected output:**
```
pass test_c1
pass test_c2
pass test_c3
pass test_c4
pass test_c5
pass test_c7
All tests passed.
```
