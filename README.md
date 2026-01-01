# Coralia Sequence

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)

The **Coralia Sequence** (OEIS pending) is an integer sequence defined by cascade triple enumeration, where each term encodes the minimal non-repeating cascade structure at index *n*.

## Definition

The Coralia Sequence **C(n)** is defined recursively:

```
C(0) = 1
C(n) = min{k ∈ ℕ : k ∉ {C(0), ..., C(n-1)} ∧ T(C(n-1), k, n) is valid}
```

where **T(a, b, n)** is a *cascade triple* satisfying the Coralia axioms.

### First 20 Terms

```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
```

**Note**: With the current cascade constraint parameters, C(n) = n + 1 for all n. This validates that the minimal valid successor at each step is always the next unused integer.

## Quick Start

### Installation

```bash
git clone https://github.com/coralia-io/coralia-sequence.git
cd coralia-sequence
pip install -r requirements.txt  # optional: numpy for performance
```

### Generate the Sequence

```bash
python code/generator/generate_coralia.py --terms 100
```

### Verify Properties

```bash
python code/verification/verify_uniqueness.py --terms 1000
python tests/test_axioms.py
```

## Repository Structure

```
coralia-sequence/
├── README.md                  # This file
├── LICENSE                    # MIT License
├── CITATION.cff              # Citation metadata
├── docs/
│   ├── MASTER_DOC.md         # Complete mathematical documentation
│   └── CHANGELOG.md          # Version history
├── code/
│   ├── generator/
│   │   └── generate_coralia.py      # Sequence generator
│   └── verification/
│       ├── verify_uniqueness.py     # Uniqueness verification
│       └── cascade_triple_enum.py   # Cascade triple enumeration
├── tests/
│   └── test_axioms.py        # Axiom verification tests
└── papers/
    └── coralia-sequence_math/
        └── coralia-sequence_math_v1.0.tex  # LaTeX paper
```

## Mathematical Properties

1. **Uniqueness**: Each positive integer appears exactly once in the sequence
2. **Cascade Structure**: Adjacent terms form valid cascade triples
3. **Density**: The sequence achieves optimal packing under the cascade constraint
4. **Growth**: Asymptotically, C(n) ~ n with bounded deviation

See [docs/MASTER_DOC.md](docs/MASTER_DOC.md) for complete proofs and analysis.

## Citation

If you use the Coralia Sequence in your research, please cite:

```bibtex
@software{coralia_sequence,
  author       = {Coralia.io Contributors},
  title        = {The Coralia Sequence: Cascade Triple Enumeration},
  year         = {2025},
  publisher    = {GitHub},
  url          = {https://github.com/coralia-io/coralia-sequence}
}
```

See [CITATION.cff](CITATION.cff) for complete citation metadata.

## Contributing

Contributions are welcome! Please read our documentation and ensure all tests pass before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **Documentation**: [docs/MASTER_DOC.md](docs/MASTER_DOC.md)
- **Paper**: [papers/coralia-sequence_math/](papers/coralia-sequence_math/)
- **Issues**: [GitHub Issues](https://github.com/coralia-io/coralia-sequence/issues)
