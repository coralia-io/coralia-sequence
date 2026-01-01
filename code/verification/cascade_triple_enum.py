#!/usr/bin/env python3
"""
Cascade Triple Enumeration

Utilities for enumerating and analyzing cascade triples in the context
of the Coralia Sequence. A cascade triple (a, b, n) satisfies specific
constraints that govern the sequence construction.

This module provides:
- Enumeration of all valid cascade triples for given parameters
- Analysis of cascade triple distributions
- Visualization helpers for cascade structure

Usage:
    python cascade_triple_enum.py --analyze 100
    python cascade_triple_enum.py --successors 5 10

Author: Coralia.io Contributors
License: MIT
"""

from __future__ import annotations

import argparse
import math
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class CascadeTriple:
    """Represents a cascade triple (a, b, n)."""

    a: int  # First value (previous term)
    b: int  # Second value (current term)
    n: int  # Index position

    def __str__(self) -> str:
        return f"({self.a}, {self.b}, {self.n})"

    @property
    def gap(self) -> int:
        """The absolute difference between a and b."""
        return abs(self.a - self.b)

    @property
    def has_correction(self) -> bool:
        """Whether this triple has a non-zero cascade correction."""
        return (self.a + self.b) % 3 == 0


def cascade_correction(a: int, b: int, n: int) -> int:
    """
    Compute the cascade correction term δ(a, b, n).

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


def cascade_threshold(a: int, b: int, n: int) -> int:
    """
    Compute the maximum allowed gap for a cascade triple.

    Args:
        a: First value in the cascade triple
        b: Second value in the cascade triple
        n: Index position

    Returns:
        The threshold value
    """
    return math.ceil(math.sqrt(n + 1)) + cascade_correction(a, b, n)


def is_valid_triple(a: int, b: int, n: int) -> bool:
    """
    Check if (a, b, n) forms a valid cascade triple.

    Args:
        a: Previous sequence value
        b: Candidate value
        n: Current index position

    Returns:
        True if valid, False otherwise
    """
    if a == b:
        return False
    if max(a, b) > 2 * n + 2:
        return False
    if abs(a - b) > cascade_threshold(a, b, n):
        return False
    return True


def enumerate_successors(a: int, n: int, max_val: int | None = None) -> Iterator[int]:
    """
    Enumerate all valid successors for position n given previous value a.

    Args:
        a: The previous value C(n-1)
        n: The current position (1-indexed)
        max_val: Optional maximum value to consider

    Yields:
        Valid successor values in ascending order
    """
    if max_val is None:
        max_val = 2 * n + 2

    for b in range(1, max_val + 1):
        if is_valid_triple(a, b, n):
            yield b


def enumerate_all_triples(max_n: int) -> Iterator[CascadeTriple]:
    """
    Enumerate all valid cascade triples up to index max_n.

    Args:
        max_n: Maximum index to enumerate

    Yields:
        All valid CascadeTriple objects
    """
    for n in range(1, max_n + 1):
        max_val = 2 * n + 2
        for a in range(1, max_val + 1):
            for b in range(1, max_val + 1):
                if is_valid_triple(a, b, n):
                    yield CascadeTriple(a, b, n)


def count_successors(a: int, n: int) -> int:
    """
    Count the number of valid successors for position n given previous value a.

    Args:
        a: The previous value
        n: The current position

    Returns:
        Number of valid successors
    """
    return sum(1 for _ in enumerate_successors(a, n))


def analyze_cascade_distribution(max_n: int) -> dict:
    """
    Analyze the distribution of cascade triples.

    Args:
        max_n: Maximum index to analyze

    Returns:
        Dictionary containing analysis results
    """
    gap_counts = Counter()
    correction_counts = Counter()
    triples_per_n = Counter()
    successors_per_a = {}

    for triple in enumerate_all_triples(max_n):
        gap_counts[triple.gap] += 1
        correction_counts[triple.has_correction] += 1
        triples_per_n[triple.n] += 1

    # Analyze successor counts for small values of a
    for a in range(1, min(21, max_n + 1)):
        counts = []
        for n in range(1, max_n + 1):
            counts.append(count_successors(a, n))
        successors_per_a[a] = {
            "min": min(counts),
            "max": max(counts),
            "mean": sum(counts) / len(counts),
        }

    return {
        "max_n": max_n,
        "total_triples": sum(triples_per_n.values()),
        "gap_distribution": dict(sorted(gap_counts.items())),
        "with_correction": correction_counts[True],
        "without_correction": correction_counts[False],
        "triples_per_n": dict(sorted(triples_per_n.items())),
        "successors_per_a": successors_per_a,
    }


def print_analysis(analysis: dict) -> None:
    """Print analysis results in a formatted way."""
    print(f"\nCascade Triple Analysis (max_n = {analysis['max_n']})")
    print("=" * 60)

    print(f"\nTotal valid triples: {analysis['total_triples']}")
    print(f"With cascade correction: {analysis['with_correction']}")
    print(f"Without cascade correction: {analysis['without_correction']}")

    print("\nGap Distribution (|a - b|):")
    for gap, count in sorted(analysis["gap_distribution"].items())[:10]:
        print(f"  Gap {gap}: {count} triples")
    if len(analysis["gap_distribution"]) > 10:
        print(f"  ... and {len(analysis['gap_distribution']) - 10} more gap values")

    print("\nTriples per index n (first 10):")
    for n, count in sorted(analysis["triples_per_n"].items())[:10]:
        print(f"  n = {n}: {count} valid triples")

    print("\nSuccessor count statistics (for small a):")
    for a, stats in sorted(analysis["successors_per_a"].items())[:10]:
        print(f"  a = {a}: min={stats['min']}, max={stats['max']}, mean={stats['mean']:.2f}")


def print_successors(a: int, n: int) -> None:
    """Print all valid successors for given a and n."""
    successors = list(enumerate_successors(a, n))
    print(f"\nValid successors for a={a} at position n={n}:")
    print(f"Threshold: ceil(sqrt({n+1})) + δ = {cascade_threshold(a, successors[0] if successors else a+1, n)}")
    print(f"Count: {len(successors)}")
    if successors:
        print(f"Values: {successors}")
        print(f"Range: [{min(successors)}, {max(successors)}]")
    else:
        print("No valid successors found!")


def main() -> int:
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Cascade Triple Enumeration and Analysis",
        epilog="Example: python cascade_triple_enum.py --analyze 100",
    )
    parser.add_argument(
        "--analyze",
        "-a",
        type=int,
        metavar="N",
        help="Analyze cascade triple distribution up to index N",
    )
    parser.add_argument(
        "--successors",
        "-s",
        nargs=2,
        type=int,
        metavar=("A", "N"),
        help="List valid successors for value A at position N",
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        metavar="N",
        help="Count total triples up to index N",
    )
    parser.add_argument(
        "--list",
        "-l",
        type=int,
        metavar="N",
        help="List all triples up to index N (warning: can be large)",
    )

    args = parser.parse_args()

    if args.analyze:
        analysis = analyze_cascade_distribution(args.analyze)
        print_analysis(analysis)
    elif args.successors:
        a, n = args.successors
        print_successors(a, n)
    elif args.count:
        total = sum(1 for _ in enumerate_all_triples(args.count))
        print(f"Total valid cascade triples for n ≤ {args.count}: {total}")
    elif args.list:
        print(f"All valid cascade triples for n ≤ {args.list}:")
        for triple in enumerate_all_triples(args.list):
            print(f"  {triple}")
    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
