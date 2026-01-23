# Coralia Classification (Trilogy Papers I–III)

A complete mathematical classification establishing the unique 12-element subset of {0, ..., 35} satisfying a natural axiom system, plus frozen reproducibility artifacts.

> Formerly known as *coralia-sequence*.

## The Set

```
C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
```

## What This Repository Contains

- **Classification result**: The set C is uniquely determined by axioms C1–C9
- **Frozen reproducibility**: Scripts and data to verify all claims in Papers I–III
- **Working code**: Library and examples for exploring the classification

## Papers

| Paper | Title | DOI |
|-------|-------|-----|
| I | Existence and Uniqueness | [10.5281/zenodo.18121785](https://doi.org/10.5281/zenodo.18121785) |
| II | Empirical Content of the Axioms | [10.5281/zenodo.18150002](https://doi.org/10.5281/zenodo.18150002) |
| III | Minimal Axioms and Classification | [10.5281/zenodo.18346226](https://doi.org/10.5281/zenodo.18346226) |

See [`papers/`](papers/) for local copies and supplementary materials.

## Trilogy Map

```
Paper I    →  Discovery: proves exactly one set satisfies C1–C9
Paper II   →  Empirical content: the axioms predict where constants land
Paper III  →  Minimality: establishes axiom independence and ceiling necessity
```

## Quick Start

```bash
git clone https://github.com/coralia-io/coralia-sequence.git
cd coralia-sequence
python examples/landing_demo.py
```

## Reproduction

Verify the classification result:

```bash
python frozen/code/enumeration_core.py    # Output: Solutions: 1
python frozen/code/ceiling_scan.py        # Shows uniqueness at ceiling=35
python frozen/code/axiom_drop.py          # Tests axiom independence
```

Verify file integrity:

```bash
cd frozen && sha256sum -c ../docs/checksums.txt
```

See [`docs/reproduction.md`](docs/reproduction.md) for detailed instructions and [`frozen/AUDIT_MANIFEST.md`](frozen/AUDIT_MANIFEST.md) for checksums.

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `papers/` | Paper PDFs and supplementary materials |
| `frozen/` | Reproducibility artifacts (code + data) |
| `core/` | Library implementation and proofs |
| `examples/` | Demonstration scripts |
| `interfaces/` | Reusable grammars, classifiers, exports |
| `sandbox/` | Domain applications (exploratory) |
| `docs/` | Documentation |

## Etymology

*Coralia* derives from Latin *corallium* ("coral") + *-ia*; pronounced /kəˈrɑːliə/ ("Coral-ee-uh").

## Citation

```bibtex
@misc{cecile2026coralia,
  author = {Cecile, Emma},
  title = {Coralia Classification (Trilogy Papers I--III)},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18346226}
}
```

See [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata.

## License

MIT — see [`LICENSE`](LICENSE).

## Author

Emma Cecile · [ORCID 0009-0008-4120-9309](https://orcid.org/0009-0008-4120-9309)
