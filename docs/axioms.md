# Axioms

The Coralia Sequence is uniquely determined by nine axioms.

## The Axioms

| Axiom | Name | Constraint |
|-------|------|------------|
| C1 | Origin | 0 ∈ C |
| C2 | Cardinality containment | \|C\| ∈ C |
| C3 | Cardinality | \|C\| = 12 |
| C4 | Ceiling | max(C) = 35 |
| C5 | Gap-sum closure | Σ gaps = 35 |
| C6a | Gap vocabulary | First 8 gaps ∈ {1, 2, 3} |
| C6b | Gap monotonicity | First 8 gaps non-decreasing |
| C6c | Seed specification | {1, 2, 3, 5, 7, 9, 15} ⊆ C |
| C7 | Terminal descent | Last 3 gaps strictly decreasing |
| C8 | Fibonacci-Lucas terminal | Last 3 gaps ∈ Fib ∪ Luc |
| C9 | Terminal minimum | Last 3 gaps ≥ 5 |

## Verification
```python
from coralia import check_axioms, C
print(check_axioms(C))
```

See [paper](https://doi.org/10.5281/zenodo.18121786) for full proofs.
