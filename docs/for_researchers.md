# For Researchers

How to test the Coralia Sequence in your domain.

## What is proven

- C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35} is unique under axioms C1-C9
- Terminal triple (8, 7, 5) is unique under its constraints
- 3 convergence points derive from φ³
- All proofs are computational and reproducible

## What is validated

- Sleep architecture (99.2-99.4 percentile)
- Heart rate variability
- Music theory (structural correspondence)

## What is testable

Everything in [domains.md](domains.md) marked "Testable"

## How to test

1. Define your domain dataset
2. Normalize to comparable scale if needed
3. Use tools from the package:
```python
from coralia import coherence_score, gap_match, detect_zone

result = coherence_score(your_data)
print(result)
```

4. Compare against null models
5. Report findings with appropriate caveats

## What to look for

- Gap pattern alignment
- Zone distribution
- Convergence point boundaries
- 43% cliff behavior

## Citing

Cecile, E. (2026). The Coralia Sequence: A Unique Finite Integer Set Under Fibonacci-Lucas Terminal Constraints (1.1). Zenodo. https://doi.org/10.5281/zenodo.18121786

## Contact

This repository is self-serve. For discussion, see [Substack](https://coralia.substack.com).
