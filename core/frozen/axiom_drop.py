"""
Axiom Drop Analysis for Paper III
Frozen artifact: DO NOT MODIFY

Author: Emma Cecile | ORCID: 0009-0008-4120-9309
Paper III Reference: Section 4

Demonstrates that removing any single axiom from the full set
results in multiple solutions, proving each axiom is necessary.
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

# Axiom checkers
def A1_size(S): return len(S) == 12
def A2_zero(S): return 0 in S
def A3_ceiling(S): return 35 in S and max(S) == 35
def A4_twelve(S): return 12 in S
def A5_anchors(S): return {1, 2, 3, 5, 7, 9, 15} <= set(S)
def A6_gap_alphabet(S):
    g = gaps(sorted(S))
    return all(x in {1, 2, 3} for x in g[:8])
def A7_gap_monotone(S):
    g = gaps(sorted(S))
    return all(g[i] <= g[i+1] for i in range(7))
def A8_tail_decreasing(S):
    g = gaps(sorted(S))
    return g[-3] > g[-2] > g[-1]
def A9_tail_fl(S):
    g = gaps(sorted(S))
    return all(x in FL for x in g[-3:])
def A10_tail_min(S):
    g = gaps(sorted(S))
    return all(x >= 5 for x in g[-3:])

ALL_AXIOMS = [
    ("A1: size=12", A1_size),
    ("A2: contains 0", A2_zero),
    ("A3: ceiling=35", A3_ceiling),
    ("A4: contains 12", A4_twelve),
    ("A5: anchors {1,2,3,5,7,9,15}", A5_anchors),
    ("A6: first 8 gaps in {1,2,3}", A6_gap_alphabet),
    ("A7: first 8 gaps monotone", A7_gap_monotone),
    ("A8: last 3 gaps decreasing", A8_tail_decreasing),
    ("A9: last 3 gaps in FL", A9_tail_fl),
    ("A10: last 3 gaps >= 5", A10_tail_min),
]

def check_all_except(S, skip_idx):
    """Check all axioms except the one at skip_idx."""
    for i, (name, check) in enumerate(ALL_AXIOMS):
        if i == skip_idx:
            continue
        if not check(S):
            return False
    return True

def enumerate_with_dropped_axiom(drop_idx):
    """Enumerate all 12-subsets satisfying all axioms except drop_idx."""
    # Fixed pool based on the axioms we're still using
    pool = list(range(36))
    survivors = []

    for combo in combinations(pool, 12):
        S = tuple(sorted(combo))
        if check_all_except(S, drop_idx):
            survivors.append(S)

    return survivors

def axiom_drop_analysis():
    """
    Run axiom drop analysis.

    For each axiom, count how many configurations satisfy all OTHER axioms.
    If dropping an axiom yields >1 solution, that axiom is necessary.
    """
    results = []

    for i, (name, _) in enumerate(ALL_AXIOMS):
        survivors = enumerate_with_dropped_axiom(i)
        results.append({
            "axiom": name,
            "dropped_index": i,
            "survivor_count": len(survivors),
            "necessary": len(survivors) > 1,
        })

    return results

if __name__ == "__main__":
    print("Axiom Drop Analysis - Paper III Frozen Artifact")
    print("=" * 50)
    print()
    print("Testing necessity of each axiom...")
    print("(This may take a few minutes)")
    print()

    results = axiom_drop_analysis()

    print(f"{'Axiom':<35} {'Drop Count':>12} {'Necessary':>10}")
    print("-" * 60)

    for r in results:
        necessary = "YES" if r["necessary"] else "NO"
        print(f"{r['axiom']:<35} {r['survivor_count']:>12} {necessary:>10}")

    print()
    all_necessary = all(r["necessary"] for r in results)
    print(f"All axioms necessary: {all_necessary}")
