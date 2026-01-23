"""
Voronoi landing classifier for the Coralia set C.
"""

C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]
E = [x for x in range(36) if x not in C]

def nearest(x, S):
    """Find nearest element in set S to value x."""
    return min(S, key=lambda s: abs(s - x))

def distance_to_C(x):
    """Distance from x to nearest C element."""
    return abs(x - nearest(x, C))

def distance_to_E(x):
    """Distance from x to nearest Exclusion."""
    return abs(x - nearest(x, E))

def lands_on(x):
    """
    Classify x as landing on C or E.
    Ties go to E.
    """
    dc = distance_to_C(x)
    de = distance_to_E(x)
    return "C" if dc < de else "E"

def gap_index(x):
    """Return which gap x falls into (0-indexed)."""
    for i, c in enumerate(C[:-1]):
        if c <= x < C[i+1]:
            return i
    return len(C) - 1
