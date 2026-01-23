# File Manifest

Complete listing of repository contents for the Coralia Classification.

## Root Files

| File | Description |
|------|-------------|
| `README.md` | Main repository documentation |
| `LICENSE` | MIT License |
| `CITATION.cff` | Machine-readable citation metadata |
| `SCOPE.md` | Project scope and boundaries |
| `WHO_THIS_IS_FOR.md` | Audience guidance |
| `.gitignore` | Git ignore rules |

## Papers (`papers/`)

| Path | Description |
|------|-------------|
| `papers/paper-1/README.md` | Paper I summary and links |
| `papers/paper-1/paper-1.pdf` | Paper I PDF (when available) |
| `papers/paper-2/README.md` | Paper II summary and links |
| `papers/paper-2/paper-2.pdf` | Paper II PDF (when available) |
| `papers/paper-3/README.md` | Paper III summary and links |
| `papers/paper-3/paper-3.pdf` | Paper III PDF (when available) |

## Frozen Reproducibility Artifacts (`frozen/`)

| Path | Description |
|------|-------------|
| `frozen/AUDIT_MANIFEST.md` | Checksums and verification instructions |
| `frozen/code/enumeration_core.py` | Exhaustive uniqueness search (Paper I) |
| `frozen/code/cascade_triple_enum.py` | Terminal gap triple enumeration |
| `frozen/code/ceiling_scan.py` | Ceiling value scan (Paper III) |
| `frozen/code/axiom_drop.py` | Axiom independence test (Paper III) |
| `frozen/data/survivor_tables.csv` | Axiom-drop survivor counts |

## Core Library (`core/`)

| Path | Description |
|------|-------------|
| `core/coralia/__init__.py` | Package initialization |
| `core/coralia/sequence.py` | Sequence definition and generation |
| `core/coralia/verify.py` | Axiom verification functions |
| `core/coralia/tools.py` | Utility functions |
| `core/proofs/verify_uniqueness.py` | Original uniqueness proof script |
| `core/proofs/cascade_triple_enum.py` | Cascade enumeration script |
| `core/tests/test_axioms.py` | Axiom test suite |

## Examples (`examples/`)

| Path | Description |
|------|-------------|
| `examples/README.md` | Examples documentation |
| `examples/landing_demo.py` | Constant landing demonstration |
| `examples/compare_constants.py` | Constant comparison utilities |
| `examples/plot_distances.py` | Distance visualization |

## Interfaces (`interfaces/`)

| Path | Description |
|------|-------------|
| `interfaces/README.md` | Interfaces documentation |
| `interfaces/grammars/canonical.py` | Canonical grammar representation |
| `interfaces/classifiers/nearest_integer.py` | Nearest integer classifier |
| `interfaces/exports/coralia_sequence.json` | JSON export of C |

## Sandbox (`sandbox/`)

Exploratory domain applications. See `sandbox/README.md` for details.

- `sandbox/validated/` — Empirically validated applications
- `sandbox/testable/` — Testable predictions
- `sandbox/origin/` — Origin investigations

## Documentation (`docs/`)

| Path | Description |
|------|-------------|
| `docs/trilogy_overview.md` | Overview of the three papers |
| `docs/reproduction.md` | Reproduction instructions |
| `docs/file_manifest.md` | This file |
| `docs/axioms.md` | Axiom definitions |
| `docs/domains.md` | Domain application notes |
| `docs/convergence_points.md` | Convergence point documentation |
| `docs/for_researchers.md` | Researcher guide |
| `docs/MASTER_DOC.md` | Master documentation |
