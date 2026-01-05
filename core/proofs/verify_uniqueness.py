"""
Uniqueness Verification
Author: Emma Cecile | ORCID: 0009-0008-4120-9309
"""
from itertools import combinations

def gaps(seq):
    return tuple(seq[i+1] - seq[i] for i in range(len(seq)-1))

def fib_set(n=35):
    a, b, s = 0, 1, {0, 1}
    while b <= n: s.add(b); a, b = b, a + b
    return s

def luc_set(n=35):
    a, b, s = 2, 1, {2, 1}
    while b <= n: s.add(b); a, b = b, a + b
    return s

FL = fib_set() | luc_set()

def satisfies_axioms(S):
    S = sorted(S)
    g = gaps(S)
    if len(S) != 12: return False
    if 0 not in S: return False
    if 12 not in S: return False
    if max(S) != 35: return False
    if sum(g) != 35: return False
    if not all(x in {1,2,3} for x in g[:8]): return False
    if not all(g[i] <= g[i+1] for i in range(7)): return False
    if not {1,2,3,5,7,9,15} <= set(S): return False
    if not (g[-3] > g[-2] > g[-1]): return False
    if not all(x in FL for x in g[-3:]): return False
    if not all(x >= 5 for x in g[-3:]): return False
    return True

if __name__ == "__main__":
    required = {0, 1, 2, 3, 5, 7, 9, 12, 15, 35}
    pool = [x for x in range(36) if x not in required]
    solutions = [sorted(required | set(c)) for c in combinations(pool, 2) if satisfies_axioms(required | set(c))]
    print(f"Solutions: {len(solutions)}")
