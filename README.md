# The Coralia Sequence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18121786.svg)](https://doi.org/10.5281/zenodo.18121786)

A logic kernel for reasoning about stability, collapse, and rhythm in any system.

```
C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
gaps = [1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5]
```

## What is this?

A 12-element integer set with a distinctive structure. Proven unique under nine axioms. Validated in sleep architecture, heart rate variability, and music theory.

Systems have 3 tipping points, not 1. This framework came from physics — angle of repose, Kirkwood gaps, orbital resonance.

**Read first:** [SCOPE.md](SCOPE.md) | [WHO_THIS_IS_FOR.md](WHO_THIS_IS_FOR.md)

## Quick Start

```bash
# Run a demo
PYTHONPATH=. python examples/landing_demo.py

# Verify the axioms
PYTHONPATH=. python core/tests/test_axioms.py
```

```python
from core.coralia import C, gaps, convergence_points, detect_zone

print(C)                    # The sequence
print(gaps)                 # The gap pattern
print(convergence_points)   # The 3 tipping points
print(detect_zone(17))      # Which zone? → 4
```

## The 3 Convergence Points

| Point | Value | Role |
|-------|-------|------|
| Λ₁ | 6.25 | Zone 1→2 transition |
| Λ₂ | φ⁶ ≈ 17.944 | 43% cliff — cascade begins |
| Λ₃ | Q₀ ≈ 21.246 | Shadow threshold |

All derive from φ³. See [convergence_points.md](docs/convergence_points.md).

## Structure

| Zone | Gaps | Character |
|------|------|-----------|
| 1 | 1, 1, 1 | Stable foundation |
| 2 | 2, 2, 2 | Steady growth |
| 3 | 3, 3 | Transition |
| 4 | 8, 7, 5 | Cascade |

## Repository Layout

```
coralia-sequence/
├── core/           # Authoritative (do not edit casually)
│   ├── coralia/    # Python package
│   ├── papers/     # Published papers
│   ├── proofs/     # Verification scripts
│   └── tests/      # Axiom tests
├── sandbox/        # Exploratory (contribute here)
│   ├── validated/  # Confirmed domains
│   ├── origin/     # Where it came from
│   └── testable/   # Hypotheses to test
├── examples/       # Entry point demos
├── interfaces/     # Reusable components
│   ├── grammars/   # Formal representations
│   ├── classifiers/# Mapping tools
│   └── exports/    # Data formats
└── docs/           # Documentation
```

## Domains

**Validated:** Sleep, HRV, Music

**Origin:** Physics (planetary resonance, crystallography, quantum)

**Testable:** Neural, circadian, linguistics, ecology, urban, visual, dance, film, network, algorithm, compression, learning

See [domains.md](docs/domains.md) for the full map.

## Documentation

- [Scope](SCOPE.md)
- [Who This Is For](WHO_THIS_IS_FOR.md)
- [Axioms](docs/axioms.md)
- [Convergence Points](docs/convergence_points.md)
- [Domain Map](docs/domains.md)
- [For Researchers](docs/for_researchers.md)

## Citation

Cecile, E. (2026). The Coralia Sequence: A Unique Finite Integer Set Under Fibonacci-Lucas Terminal Constraints (1.1). Zenodo. https://doi.org/10.5281/zenodo.18121786

## Author

Emma Cecile · [ORCID](https://orcid.org/0009-0008-4120-9309) · [Substack](https://coralia.substack.com)

## License

MIT
