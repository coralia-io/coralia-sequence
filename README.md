# The Coralia Sequence

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18121786.svg)](https://doi.org/10.5281/zenodo.18121786)

A 12-element integer set with a distinctive gap structure that appears in multiple independent domains.

```
C = {0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35}
```

## What is this?

A mathematically unique sequence built from Fibonacci-Lucas constraints. Proven in the [accompanying paper](https://doi.org/10.5281/zenodo.18121786) to be the unique solution under a specific nine-axiom system.

It also has structural correspondences that practitioners in music, neuroscience, physics, and design may find suggestive.

## Who is this for?

These are potential application lenses, not claims of empirical validation.

| Audience | Why it might matter |
|----------|---------------------|
| Musicians | 12 tones, gap patterns mirror tension/resolution |
| Neuroscientists | Theta-gamma coupling ratios, sleep stage boundaries |
| Architects | Golden ratio proportions, spatial intervals |
| Game Devs | Difficulty curves, loot distribution, level pacing |
| Generative Artists | Algorithmic patterns, visual rhythm |
| Vibe Coders | One function, copy-paste, it works |
| Physicists | Kirkwood gaps, Arnold tongues, resonance |
| Data Scientists | Reference sequence for gap detection |
| UX Designers | Spacing and timing that feels natural |
| Sound Designers | Frequency ratios, beat templates |
| Writers | 4-zone story structure, non-uniform pacing |
| Productivity | Time-boxing with natural intervals |
| Educators | Concrete Fibonacci-Lucas example with proof |

## Quick Start

```python
C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]
gaps = [1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5]
```

That is the full object. Use it, test it, remix it.

## Why these numbers?

Four zones. Ascending gaps (1, 2, 3). Then a Fibonacci-Lucas cascade (8, 7, 5).

| Zone | Start | Gaps | Elements |
|------|-------|------|----------|
| 1 | 0 | 1, 1, 1 | 0, 1, 2, 3 |
| 2 | 3 | 2, 2, 2 | 5, 7, 9 |
| 3 | 9 | 3, 3 | 12, 15 |
| 4 | 15 | 8, 7, 5 | 23, 30, 35 |

The terminal triple (8, 7, 5) is the only descending Fibonacci-Lucas triple that sums to 20 with all elements at least 5.

Formally proven, computationally verified, and fully documented.

## The Math

- [Full paper (Zenodo)](https://doi.org/10.5281/zenodo.18121786)
- [Axioms and proofs](docs/MASTER_DOC.md)
- [Verification code](code/verification/)

## Use Cases

### Music
12 elements matches the chromatic scale. Gap sequence mirrors interval tension.

### Neuroscience
5 of 6 known theta-gamma coupling ratios appear in C.

### Architecture
φ-derived junctions at positions 3, 9, 15. Golden ratio spacing.

### Game Design
Non-linear progression: zones 1-3 feel normal, zone 4 explodes.

### Productivity
Time blocks: 1-1-1 (warmup), 2-2-2 (work), 3-3 (deep), 8-7-5 (wind down).

### Generative Art
Gap sequence as rhythm: [1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5]

## Citation

Cecile, E. (2026). The Coralia Sequence: A Unique Finite Integer Set Under Fibonacci-Lucas Terminal Constraints (1.1). Zenodo. https://doi.org/10.5281/zenodo.18121786

## Author

**Emma Cecile**
ORCID: [0009-0008-4120-9309](https://orcid.org/0009-0008-4120-9309)
Coralia LLC

## License

MIT. Use it for anything.
