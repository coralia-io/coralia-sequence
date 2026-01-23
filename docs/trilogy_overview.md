# Trilogy Overview

The Coralia Classification is established across three papers, each building on the previous.

## Paper I: The Coralia Sequence

**File:** `Cecile_2026_The_Coralia_Sequence.pdf`
**DOI:** [10.5281/zenodo.18121785](https://doi.org/10.5281/zenodo.18121785)

Poses the classification problem: find all 12-element subsets of {0, ..., 35} satisfying axioms C1–C9. Proves by exhaustive enumeration that exactly one such set exists:

```
C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
```

**Key contribution:** Establishes the uniqueness theorem.

## Paper II: Axioms That Predict

**File:** `Cecile_2026_Axioms_That_Predict.pdf`
**DOI:** [10.5281/zenodo.18150002](https://doi.org/10.5281/zenodo.18150002)

Investigates whether the axioms have predictive content beyond defining C. Shows that mathematical constants (e², e^π, φ^n, etc.) land on C-elements when rounded to nearest integers at rates exceeding chance expectation.

**Key contribution:** Demonstrates the axioms capture structural properties beyond mere set membership.

## Paper III: Aperture

**File:** `Cecile_2026_Aperture.pdf`
**DOI:** [10.5281/zenodo.18346226](https://doi.org/10.5281/zenodo.18346226)

*Aperture: The Geometry of Coralia*

Completes the classification by:

1. Testing axiom independence: dropping C7, C8, or C9 each allows additional solutions
2. Verifying ceiling necessity: only ceiling=35 yields exactly one solution
3. Establishing the axiom system is minimal for uniqueness

**Key contribution:** Proves the axiom set is tight—no axiom can be removed without losing uniqueness.

## Trilogy Structure

```
Paper I   →  WHAT exists (the unique set C)
Paper II  →  WHY it matters (predictive content)
Paper III →  HOW tight the result is (minimality)
```

## Supporting Materials

| File | Description |
|------|-------------|
| `Cecile_2026_Appendices_A-H.pdf` | Technical appendices |
| `Cecile_2026_AYNI.pdf` | Author's year-in notes |
| `Cecile_2026_References.pdf` | Consolidated bibliography |
| `Cecile_2026_Changelog.pdf` | Version history |

## Reproducibility

All claims are verified by scripts in [`frozen/`](../frozen/). See [`reproduction.md`](reproduction.md) for instructions.
