# Coralia Sequence: Master Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Formal Definition](#formal-definition)
3. [Cascade Triples](#cascade-triples)
4. [The Coralia Axioms](#the-coralia-axioms)
5. [Properties and Theorems](#properties-and-theorems)
6. [Algorithm](#algorithm)
7. [Computational Results](#computational-results)
8. [Open Problems](#open-problems)
9. [References](#references)

---

## Introduction

The **Coralia Sequence** is an integer sequence arising from the enumeration of cascade triples under a minimality constraint. It provides a canonical ordering of the positive integers that respects a specific combinatorial structure.

The sequence was developed to study permutation properties arising from cascading relationships between consecutive terms. Unlike simple permutations of the naturals, the Coralia Sequence encodes structural information about how integers can be arranged while maintaining cascade validity.

---

## Formal Definition

### Definition 1 (Coralia Sequence)

The Coralia Sequence **C: ℕ → ℕ⁺** is defined by:

```
C(0) = 1

C(n) = min{k ∈ ℕ⁺ : k ∉ {C(0), ..., C(n-1)} ∧ ValidTriple(C(n-1), k, n)}
```

where `ValidTriple(a, b, n)` is the cascade triple validation predicate defined below.

### Definition 2 (Cascade Triple)

A **cascade triple** is an ordered triple (a, b, n) ∈ ℕ⁺ × ℕ⁺ × ℕ satisfying:

1. **Distinctness**: a ≠ b
2. **Index Bound**: max(a, b) ≤ 2n + 2
3. **Cascade Property**: |a - b| ≤ ⌈√(n + 1)⌉ + δ(a, b, n)

where δ(a, b, n) is the **cascade correction term**:

```
δ(a, b, n) = ⌊log₂(min(a, b) + 1)⌋ if (a + b) mod 3 = 0
           = 0                      otherwise
```

---

## Cascade Triples

### Intuition

Cascade triples encode a relationship between consecutive sequence terms that balances:
- **Locality**: Terms should not deviate too far from each other
- **Coverage**: All positive integers must eventually appear
- **Structure**: The cascade property introduces non-trivial ordering constraints

### Enumeration

For a given position n and previous term a, the set of valid successors is:

```
Successors(a, n) = {b ∈ ℕ⁺ : ValidTriple(a, b, n)}
```

The Coralia Sequence always selects the minimum available successor.

### Example

At position n = 4 with C(3) = 4:
- Valid candidates: {5, 6, 7, ...} ∩ Successors(4, 4)
- Excluding already used: {1, 2, 3, 4} → must exclude these
- Threshold: ⌈√5⌉ + δ = 3 + 0 = 3
- First valid: 5 (since |4 - 5| = 1 ≤ 3)
- Therefore: C(4) = 5

---

## The Coralia Axioms

The Coralia Sequence satisfies four fundamental axioms:

### Axiom 1: Injectivity
```
∀ i, j ∈ ℕ : i ≠ j ⟹ C(i) ≠ C(j)
```
Each term in the sequence is unique.

### Axiom 2: Surjectivity
```
∀ k ∈ ℕ⁺ : ∃ n ∈ ℕ : C(n) = k
```
Every positive integer appears in the sequence.

### Axiom 3: Cascade Validity
```
∀ n ≥ 1 : ValidTriple(C(n-1), C(n), n)
```
Every consecutive pair forms a valid cascade triple.

### Axiom 4: Minimality
```
∀ n ≥ 1, ∀ k < C(n) : k ∈ {C(0), ..., C(n-1)} ∨ ¬ValidTriple(C(n-1), k, n)
```
Each term is the smallest valid choice.

---

## Properties and Theorems

### Theorem 1 (Existence and Uniqueness)

The Coralia Sequence exists and is unique.

**Proof Sketch**: By strong induction. The base case C(0) = 1 is given. For the inductive step, we show that for any n, the set of valid successors is non-empty (existence) and the minimum is well-defined (uniqueness). □

### Theorem 2 (Bijectivity)

The Coralia Sequence is a bijection from ℕ to ℕ⁺.

**Proof**: Follows from Axioms 1 and 2. □

### Theorem 3 (Growth Bound)

For all n ≥ 0:
```
n/2 ≤ C(n) ≤ 2n + 2
```

**Proof**: The upper bound follows from the Index Bound in the cascade triple definition. The lower bound follows from injectivity and counting arguments. □

### Theorem 4 (Asymptotic Density)

```
lim_{N→∞} (1/N) × |{n ≤ N : C(n) = n}| = 0
```

Fixed points have density zero.

### Theorem 5 (Mean Value)

```
lim_{N→∞} (1/N) × Σ_{n=0}^{N-1} C(n) = ∞
```

with the more precise estimate:
```
(1/N) × Σ_{n=0}^{N-1} C(n) ~ N/2
```

---

## Algorithm

### Naive Algorithm (O(n²) per term)

```python
def coralia_naive(num_terms):
    if num_terms == 0:
        return []

    sequence = [1]
    used = {1}

    for n in range(1, num_terms):
        prev = sequence[-1]
        candidate = 1

        while True:
            if candidate not in used and valid_triple(prev, candidate, n):
                sequence.append(candidate)
                used.add(candidate)
                break
            candidate += 1

    return sequence
```

### Optimized Algorithm (O(n log n) per term)

Using a priority queue to track unused integers, the search for valid successors can be accelerated significantly.

---

## Computational Results

### First 50 Terms

```
n:   0  1  2  3  4  5  6  7  8  9
C:   1  2  3  4  5  6  7  8  9 10

n:  10 11 12 13 14 15 16 17 18 19
C:  11 12 13 14 15 16 17 18 19 20

n:  20 21 22 23 24 25 26 27 28 29
C:  21 22 23 24 25 26 27 28 29 30

n:  30 31 32 33 34 35 36 37 38 39
C:  31 32 33 34 35 36 37 38 39 40

n:  40 41 42 43 44 45 46 47 48 49
C:  41 42 43 44 45 46 47 48 49 50
```

**Note**: With the current cascade parameters, C(n) = n + 1 for all n ≥ 0. The cascade constraint is sufficiently permissive that the smallest unused positive integer is always a valid successor.

### Statistics (first 10,000 terms)

| Metric | Value |
|--------|-------|
| C(n) = n + 1 for all n | True |
| Fixed points (C(n) = n) | 0 |
| All consecutive gaps = 1 | True |

Tightening the cascade constraint (e.g., reducing the threshold) would produce non-trivial permutations of the natural numbers.

---

## Open Problems

1. **Precise Asymptotics**: Determine the exact growth rate of max_{k≤n}|C(k) - k|.

2. **Distribution of Gaps**: Characterize the distribution of C(n+1) - C(n).

3. **Periodicity**: Are there infinitely many n where C(n) = n?

4. **Generalizations**: Study Coralia-like sequences with different cascade predicates.

---

## References

1. This repository: https://github.com/coralia-io/coralia-sequence
2. OEIS Foundation. *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org/

---

*Last updated: January 2025*
