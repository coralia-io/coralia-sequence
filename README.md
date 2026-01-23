# The Coralia Sequence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18121786.svg)](https://doi.org/10.5281/zenodo.18121786)

## What is this?

A mathematically defined set of integers with unusual structural properties, plus code to reproduce and test those properties.

```
C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
```

## Why does it exist?

It began as a pure math question: *Is there a unique 12-element subset of {0,...,35} satisfying certain structural constraints?*

Yes. Paper 1 proves it.

Paper 2 shows the axioms have predictive content: they predict where certain mathematical constants land when rounded to integers.

## What can I do with it in 5 minutes?

```bash
git clone https://github.com/coralia-io/coralia-sequence.git
cd coralia-sequence
python examples/landing_demo.py
```

Output:
```
Where do these land?

  e² = 7.39 → lands on 7 ∈ C
  e^π = 23.14 → lands on 23 ∈ C
  φ⁵ = 11.09 → lands on 11 ∈ not C
```

## Where do I go next?

| I want... | Go to... |
|-----------|----------|
| The math | `core/papers/` |
| Simple experiments | `examples/` |
| Domain applications | `sandbox/` |
| Reusable code | `interfaces/` |
| To know if this is for me | [WHO_THIS_IS_FOR.md](WHO_THIS_IS_FOR.md) |

---

## Structure

| Directory | Status | Contents |
|-----------|--------|----------|
| `core/` | Authoritative | Library, papers, proofs, tests |
| `interfaces/` | Reusable | Grammars, classifiers, exports |
| `sandbox/` | Exploratory | Domain applications |
| `examples/` | Entry point | Simple demos |

See [SCOPE.md](SCOPE.md)

---

## Papers

1. **Paper 1:** Existence and Uniqueness — [DOI](https://doi.org/10.5281/zenodo.18121786)
2. **Paper 2:** Empirical Content of the Axioms — [DOI](https://doi.org/10.5281/zenodo.18150002)
  

---

## Author

Emma Cecile · [ORCID](https://orcid.org/0009-0008-4120-9309)

## License

MIT
