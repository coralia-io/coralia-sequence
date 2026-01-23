"""
Ceiling Scan — Paper III Reproducibility Artifact
Author: Emma Cecile | ORCID: 0009-0008-4120-9309

Scans ceiling values to verify C4 (max(C) = 35) is necessary.
"""
from itertools import combinations


def fib_luc_set(n=50):
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


def count_solutions(ceiling):
    """Count valid sequences for a given ceiling value."""
    required = {0, 1, 2, 3, 5, 7, 9, 12, 15, ceiling}
    pool = [x for x in range(ceiling + 1) if x not in required]
    count = 0

    for pair in combinations(pool, 2):
        S = sorted(required | set(pair))
        if len(S) != 12:
            continue
        g = tuple(S[i + 1] - S[i] for i in range(11))
        if sum(g) != ceiling:
            continue
        if not all(x in {1, 2, 3} for x in g[:8]):
            continue
        if not all(g[i] <= g[i + 1] for i in range(7)):
            continue
        if not (g[-3] > g[-2] > g[-1]):
            continue
        if not all(x in FL for x in g[-3:]):
            continue
        if not all(x >= 5 for x in g[-3:]):
            continue
        count += 1

    return count


if __name__ == "__main__":
    print("Ceiling scan: solutions per ceiling value")
    print("-" * 40)
    for c in range(30, 41):
        n = count_solutions(c)
        marker = " ← unique" if n == 1 else ""
        print(f"ceiling={c}: {n} solution(s){marker}")
