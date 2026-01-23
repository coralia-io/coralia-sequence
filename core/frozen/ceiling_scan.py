"""
Ceiling Scan for Paper III
Frozen artifact: DO NOT MODIFY

Author: Emma Cecile | ORCID: 0009-0008-4120-9309
Paper III Reference: Sections 3.1-3.4

Performs exhaustive enumeration at ceiling=35 with layered axiom filtering.
"""

from itertools import combinations

def gaps(seq):
    """Compute consecutive differences."""
    return tuple(seq[i+1] - seq[i] for i in range(len(seq)-1))

def fib_set(n=35):
    """Fibonacci numbers up to n."""
    a, b, s = 0, 1, {0, 1}
    while b <= n:
        s.add(b)
        a, b = b, a + b
    return s

def luc_set(n=35):
    """Lucas numbers up to n."""
    a, b, s = 2, 1, {2, 1}
    while b <= n:
        s.add(b)
        a, b = b, a + b
    return s

FL = fib_set() | luc_set()
FIB = fib_set()

# Required anchor elements (determines first 8 gaps)
REQUIRED_ANCHORS = {0, 1, 2, 3, 5, 7, 9, 12, 15, 35}

# Excluded elements (would violate gap constraints between anchors)
EXCLUDED = {4, 6, 8, 10, 11, 13, 14}

def L1_tail_decreasing(S):
    """
    L1: Tail strictly decreasing constraint.
    - Last 3 gaps strictly decreasing (g[-3] > g[-2] > g[-1])
    """
    S = sorted(S)
    g = gaps(S)
    return g[-3] > g[-2] > g[-1]

def L2_tail_fib(S):
    """
    L2: Third-to-last gap in Fibonacci constraint.
    - The gap at position -3 must be a Fibonacci number.
    """
    S = sorted(S)
    g = gaps(S)
    return g[-3] in FIB

def L3_tail_min(S):
    """
    L3: Tail minimum constraint.
    - All of last 3 gaps must be >= 5.
    """
    S = sorted(S)
    g = gaps(S)
    return all(x >= 5 for x in g[-3:])

def ceiling_scan(ceiling=35):
    """
    Perform exhaustive scan at given ceiling.

    Returns dict with counts at each layer.
    """
    # Pool: elements not required and not excluded
    pool = [x for x in range(ceiling + 1)
            if x not in REQUIRED_ANCHORS and x not in EXCLUDED]

    # Need to choose 2 more elements to reach size 12
    free_slots = 12 - len(REQUIRED_ANCHORS)

    interior_candidates = []
    l1_survivors = []
    l2_survivors = []
    l3_survivors = []

    for combo in combinations(pool, free_slots):
        S = tuple(sorted(REQUIRED_ANCHORS | set(combo)))

        # All candidates at this point satisfy baseline
        interior_candidates.append(S)

        if not L1_tail_decreasing(S):
            continue
        l1_survivors.append(S)

        if not L2_tail_fib(S):
            continue
        l2_survivors.append(S)

        if not L3_tail_min(S):
            continue
        l3_survivors.append(S)

    return {
        "ceiling": ceiling,
        "interior_candidates": interior_candidates,
        "l1_survivors": l1_survivors,
        "l2_survivors": l2_survivors,
        "l3_survivors": l3_survivors,
    }

if __name__ == "__main__":
    print("Ceiling Scan - Paper III Frozen Artifact")
    print("=" * 50)
    print("Running ceiling=35 scan...")
    print()

    results = ceiling_scan(35)

    print(f"Interior candidates: {len(results['interior_candidates'])}")
    print(f"L1 survivors: {len(results['l1_survivors'])}")
    print(f"L2 survivors: {len(results['l2_survivors'])}")
    print(f"L3 survivors: {len(results['l3_survivors'])}")
    print()

    if results['l3_survivors']:
        unique = results['l3_survivors'][0]
        print(f"Unique configuration: {{{', '.join(map(str, unique))}}}")
        print(f"Gap vector: {gaps(unique)}")
