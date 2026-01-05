"""
Canonical Grammar
Formal grammar representation of the Coralia Sequence.
"""

from core.coralia import C, gaps, zones

# Canonical forms
SEQUENCE = tuple(C)
GAPS = tuple(gaps)

# Zone grammar: (zone_id, gap_value, repetitions)
ZONE_GRAMMAR = [
    (1, 1, 3),  # Zone 1: gap=1, repeated 3 times
    (2, 2, 3),  # Zone 2: gap=2, repeated 3 times
    (3, 3, 2),  # Zone 3: gap=3, repeated 2 times
    (4, (8, 7, 5), 1),  # Zone 4: Fibonacci-Lucas cascade
]

# Terminal structure
TERMINAL_TRIPLE = (8, 7, 5)  # (F6, L4, F5)

def to_grammar_string():
    """Return formal grammar representation."""
    parts = []
    for zone_id, gap, reps in ZONE_GRAMMAR:
        if isinstance(gap, tuple):
            parts.append(f"Z{zone_id}:{gap}")
        else:
            parts.append(f"Z{zone_id}:{gap}^{reps}")
    return " ".join(parts)

def validate_structure(sequence):
    """Validate a sequence matches the Coralia grammar."""
    if len(sequence) != 12:
        return False, "Length must be 12"
    if sequence[0] != 0:
        return False, "Must start at 0"
    if sequence[-1] != 35:
        return False, "Must end at 35"

    # Check gaps match
    seq_gaps = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    if seq_gaps != list(GAPS):
        return False, f"Gap pattern mismatch"

    return True, "Valid"

if __name__ == "__main__":
    print(f"Grammar: {to_grammar_string()}")
    print(f"Valid: {validate_structure(list(C))}")
