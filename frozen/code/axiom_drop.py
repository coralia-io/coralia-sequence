"""
Axiom Drop Test — Paper III Reproducibility Artifact
Author: Emma Cecile | ORCID: 0009-0008-4120-9309

Tests axiom independence by dropping each axiom and counting survivors.
"""
from itertools import combinations


def fib_luc_set(n=35):
    """Generate Fibonacci ∪ Lucas numbers up to n."""
    fib, luc = {0, 1}, {2, 1}
    a, b = 0, 1
    while b <= n:
        fib.add(b)
        a, b = b, a + b
    a, b = 2, 1
    while b <= n:
        luc.add(b)
        a, b = b, a + b
    return fib | luc


FL = fib_luc_set()
SEED = {1, 2, 3, 5, 7, 9, 15}


def check_axioms(S, drop=None):
    """
    Check if sequence S satisfies all axioms except the dropped one.
    drop: axiom name to skip (e.g., 'C1', 'C4', 'C9')
    """
    S = sorted(S)
    g = tuple(S[i + 1] - S[i] for i in range(len(S) - 1))

    checks = {
        'C1': lambda: 0 in S,
        'C2': lambda: len(S) in S,
        'C3': lambda: len(S) == 12,
        'C4': lambda: max(S) == 35,
        'C5': lambda: sum(g) == 35,
        'C6a': lambda: all(x in {1, 2, 3} for x in g[:8]),
        'C6b': lambda: all(g[i] <= g[i + 1] for i in range(7)),
        'C6c': lambda: SEED <= set(S),
        'C7': lambda: g[-3] > g[-2] > g[-1],
        'C8': lambda: all(x in FL for x in g[-3:]),
        'C9': lambda: all(x >= 5 for x in g[-3:]),
    }

    for name, check in checks.items():
        if name == drop:
            continue
        if not check():
            return False
    return True


def count_survivors(drop_axiom):
    """Count sequences satisfying all axioms except drop_axiom."""
    required = {0, 1, 2, 3, 5, 7, 9, 12, 15, 35}
    pool = [x for x in range(36) if x not in required]
    survivors = []

    for pair in combinations(pool, 2):
        S = sorted(required | set(pair))
        if check_axioms(S, drop=drop_axiom):
            survivors.append(S)

    return survivors


if __name__ == "__main__":
    axioms = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6a', 'C6b', 'C6c', 'C7', 'C8', 'C9']
    print("Axiom independence test: survivors when each axiom is dropped")
    print("-" * 60)

    for ax in axioms:
        survivors = count_survivors(ax)
        status = "INDEPENDENT" if len(survivors) > 1 else "dependent"
        print(f"Drop {ax:4s}: {len(survivors):3d} survivor(s) — {status}")
