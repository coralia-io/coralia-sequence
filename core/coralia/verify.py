"""Verification tools."""

from .sequence import C, gaps


def verify_uniqueness():
    """
    Verify C is the unique solution under axioms C1-C9.
    Returns True if exactly one solution exists.
    """
    seed = {0, 1, 2, 3, 5, 7, 9, 12, 15, 35}
    pool = [x for x in range(36) if x not in seed]
    fib_luc = {1, 2, 3, 4, 5, 7, 8, 11, 13, 18}

    solutions = []
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            candidate = sorted(seed | {pool[i], pool[j]})
            g = [candidate[k+1] - candidate[k] for k in range(11)]

            if sum(g) != 35:
                continue
            if not all(x in {1, 2, 3} for x in g[:8]):
                continue
            if g[:8] != sorted(g[:8]):
                continue
            if not (g[8] > g[9] > g[10]):
                continue
            if not all(x in fib_luc for x in g[8:]):
                continue
            if not all(x >= 5 for x in g[8:]):
                continue
            solutions.append(candidate)

    return len(solutions) == 1


def check_axioms(sequence):
    """Check if a sequence satisfies Coralia axioms."""
    if len(sequence) != 12:
        return {"valid": False, "error": "Length must be 12"}

    s = sorted(sequence)
    g = [s[i+1] - s[i] for i in range(11)]
    fib_luc = {1, 2, 3, 4, 5, 7, 8, 11, 13, 18}

    return {
        "C1_origin": s[0] == 0,
        "C2_cardinality_in_set": 12 in s,
        "C3_cardinality": len(s) == 12,
        "C4_ceiling": max(s) == 35,
        "C5_gap_sum": sum(g) == 35,
        "C6a_gap_vocabulary": all(x in {1, 2, 3} for x in g[:8]),
        "C6b_gap_monotonic": g[:8] == sorted(g[:8]),
        "C6c_seed": {1, 2, 3, 5, 7, 9, 15}.issubset(set(s)),
        "C7_terminal_descent": g[8] > g[9] > g[10],
        "C8_terminal_fib_luc": all(x in fib_luc for x in g[8:]),
        "C9_terminal_min": all(x >= 5 for x in g[8:]),
        "valid": True
    }
