#!/usr/bin/env python3
"""
Coralia Sequence Generator

Generates the Coralia Sequence C(n), an integer sequence defined by cascade
triple enumeration where each term encodes the minimal non-repeating cascade
structure at index n.

Usage:
    python generate_coralia.py --terms 100
    python generate_coralia.py --terms 1000 --output coralia.txt
    python generate_coralia.py --index 42

Author: Coralia.io Contributors
License: MIT
"""

from __future__ import annotations

import argparse
import math
import sys
from typing import Iterator


def cascade_correction(a: int, b: int, n: int) -> int:
    """
    Compute the cascade correction term δ(a, b, n).

    δ(a, b, n) = floor(log₂(min(a, b) + 1)) if (a + b) mod 3 = 0
               = 0                           otherwise

    Args:
        a: First value in the cascade triple
        b: Second value in the cascade triple
        n: Index position

    Returns:
        The cascade correction term
    """
    if (a + b) % 3 == 0:
        return int(math.log2(min(a, b) + 1))
    return 0


def valid_triple(a: int, b: int, n: int) -> bool:
    """
    Check if (a, b, n) forms a valid cascade triple.

    A cascade triple must satisfy:
    1. Distinctness: a ≠ b
    2. Index Bound: max(a, b) ≤ 2n + 2
    3. Cascade Property: |a - b| ≤ ceil(sqrt(n + 1)) + δ(a, b, n)

    Args:
        a: Previous sequence value C(n-1)
        b: Candidate value for C(n)
        n: Current index position (1-based for validation)

    Returns:
        True if the triple is valid, False otherwise
    """
    # Distinctness
    if a == b:
        return False

    # Index Bound
    if max(a, b) > 2 * n + 2:
        return False

    # Cascade Property
    threshold = math.ceil(math.sqrt(n + 1)) + cascade_correction(a, b, n)
    if abs(a - b) > threshold:
        return False

    return True


def generate_coralia(num_terms: int) -> list[int]:
    """
    Generate the first num_terms of the Coralia Sequence.

    The sequence is defined by:
        C(0) = 1
        C(n) = min{k ∈ ℕ⁺ : k ∉ {C(0),...,C(n-1)} ∧ ValidTriple(C(n-1), k, n)}

    Args:
        num_terms: Number of terms to generate

    Returns:
        List containing the first num_terms of the Coralia Sequence
    """
    if num_terms <= 0:
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

            # Safety check: should never happen with correct implementation
            if candidate > 10 * num_terms:
                raise RuntimeError(
                    f"Failed to find valid successor at index {n}. "
                    "This indicates a bug in the cascade triple validation."
                )

    return sequence


def generate_coralia_iterator(max_terms: int | None = None) -> Iterator[int]:
    """
    Generate the Coralia Sequence lazily as an iterator.

    Args:
        max_terms: Optional maximum number of terms (None for infinite)

    Yields:
        Terms of the Coralia Sequence
    """
    yield 1
    used = {1}
    prev = 1
    n = 1

    while max_terms is None or n < max_terms:
        candidate = 1
        while True:
            if candidate not in used and valid_triple(prev, candidate, n):
                yield candidate
                used.add(candidate)
                prev = candidate
                break
            candidate += 1
        n += 1


def get_coralia_term(index: int) -> int:
    """
    Get a specific term C(index) of the Coralia Sequence.

    Args:
        index: The index (0-based) of the desired term

    Returns:
        The value C(index)
    """
    if index < 0:
        raise ValueError("Index must be non-negative")

    sequence = generate_coralia(index + 1)
    return sequence[index]


def format_sequence(sequence: list[int], per_line: int = 10) -> str:
    """
    Format the sequence for display.

    Args:
        sequence: The sequence to format
        per_line: Number of terms per line

    Returns:
        Formatted string representation
    """
    lines = []
    for i in range(0, len(sequence), per_line):
        chunk = sequence[i : i + per_line]
        line = f"{i:6d}: " + " ".join(f"{x:6d}" for x in chunk)
        lines.append(line)
    return "\n".join(lines)


def main() -> int:
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Generate the Coralia Sequence",
        epilog="Example: python generate_coralia.py --terms 100",
    )
    parser.add_argument(
        "--terms",
        "-n",
        type=int,
        default=20,
        help="Number of terms to generate (default: 20)",
    )
    parser.add_argument(
        "--index",
        "-i",
        type=int,
        help="Get a specific term C(index) instead of generating a range",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--compact",
        "-c",
        action="store_true",
        help="Compact output format (one term per line, no indices)",
    )
    parser.add_argument(
        "--comma",
        action="store_true",
        help="Comma-separated output",
    )

    args = parser.parse_args()

    # Generate or retrieve the sequence
    if args.index is not None:
        result = str(get_coralia_term(args.index))
    else:
        sequence = generate_coralia(args.terms)

        if args.comma:
            result = ", ".join(str(x) for x in sequence)
        elif args.compact:
            result = "\n".join(str(x) for x in sequence)
        else:
            result = format_sequence(sequence)

    # Output
    if args.output:
        with open(args.output, "w") as f:
            f.write(result + "\n")
        print(f"Output written to {args.output}")
    else:
        print(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
