#!/usr/bin/env python3
"""
Coralia Sequence Uniqueness Verification

Verifies that the Coralia Sequence satisfies the uniqueness property:
each positive integer appears exactly once in the sequence (bijectivity).

This tool checks:
1. Injectivity: No term repeats (C(i) ≠ C(j) for i ≠ j)
2. Surjectivity: All integers 1..N appear in first N terms
3. Cascade validity: All consecutive pairs form valid triples

Usage:
    python verify_uniqueness.py --terms 1000
    python verify_uniqueness.py --terms 10000 --verbose

Author: Coralia.io Contributors
License: MIT
"""

from __future__ import annotations

import argparse
import sys
import time

# Add parent directory to path for imports
sys.path.insert(0, str(__file__).rsplit("/", 2)[0])
from generator.generate_coralia import generate_coralia, valid_triple


def verify_injectivity(sequence: list[int]) -> tuple[bool, str]:
    """
    Verify that all terms in the sequence are unique.

    Args:
        sequence: The Coralia Sequence to verify

    Returns:
        Tuple of (success, message)
    """
    seen = {}
    for i, val in enumerate(sequence):
        if val in seen:
            return (
                False,
                f"FAIL: Duplicate value {val} at indices {seen[val]} and {i}",
            )
        seen[val] = i

    return True, f"PASS: All {len(sequence)} terms are unique"


def verify_surjectivity(sequence: list[int]) -> tuple[bool, str]:
    """
    Verify that for a sequence of length N, all integers 1..N appear.

    Note: Due to the cascade constraint, surjectivity is only guaranteed
    in the limit. For finite sequences, we check that the sequence is
    a permutation of some subset of ℕ⁺.

    Args:
        sequence: The Coralia Sequence to verify

    Returns:
        Tuple of (success, message)
    """
    n = len(sequence)
    values = set(sequence)

    # Check for non-positive values
    if any(v <= 0 for v in sequence):
        return False, "FAIL: Sequence contains non-positive values"

    # Check that values form a contiguous set from 1 to max
    max_val = max(values)
    min_val = min(values)

    if min_val != 1:
        return False, f"FAIL: Minimum value is {min_val}, expected 1"

    missing = set(range(1, max_val + 1)) - values
    if missing:
        if len(missing) <= 10:
            return False, f"FAIL: Missing values in range [1, {max_val}]: {sorted(missing)}"
        else:
            return False, f"FAIL: {len(missing)} values missing in range [1, {max_val}]"

    # Check coverage ratio
    coverage = len(values) / max_val
    return True, f"PASS: Sequence covers [1, {max_val}] completely (coverage: {coverage:.2%})"


def verify_cascade_validity(sequence: list[int]) -> tuple[bool, str]:
    """
    Verify that all consecutive pairs form valid cascade triples.

    Args:
        sequence: The Coralia Sequence to verify

    Returns:
        Tuple of (success, message)
    """
    if len(sequence) < 2:
        return True, "PASS: Sequence too short for cascade validation (trivially valid)"

    invalid_count = 0
    first_invalid = None

    for n in range(1, len(sequence)):
        a = sequence[n - 1]
        b = sequence[n]

        if not valid_triple(a, b, n):
            invalid_count += 1
            if first_invalid is None:
                first_invalid = (n, a, b)

    if invalid_count > 0:
        n, a, b = first_invalid
        return (
            False,
            f"FAIL: {invalid_count} invalid cascade triple(s). "
            f"First at index {n}: ({a}, {b}, {n})",
        )

    return True, f"PASS: All {len(sequence) - 1} consecutive pairs form valid cascade triples"


def verify_minimality(sequence: list[int]) -> tuple[bool, str]:
    """
    Verify that each term is the minimal valid choice.

    This is computationally expensive as it requires checking all
    smaller candidates at each position.

    Args:
        sequence: The Coralia Sequence to verify

    Returns:
        Tuple of (success, message)
    """
    if len(sequence) == 0:
        return True, "PASS: Empty sequence (trivially minimal)"

    if sequence[0] != 1:
        return False, f"FAIL: C(0) = {sequence[0]}, expected 1"

    used = {sequence[0]}

    for n in range(1, len(sequence)):
        prev = sequence[n - 1]
        current = sequence[n]

        # Check that no smaller valid candidate exists
        for candidate in range(1, current):
            if candidate not in used and valid_triple(prev, candidate, n):
                return (
                    False,
                    f"FAIL: At index {n}, value {candidate} was valid but "
                    f"{current} was used instead",
                )

        used.add(current)

    return True, f"PASS: All {len(sequence)} terms are minimal valid choices"


def verify_all(
    sequence: list[int], verbose: bool = False, check_minimality: bool = True
) -> bool:
    """
    Run all verification checks on the sequence.

    Args:
        sequence: The Coralia Sequence to verify
        verbose: Print detailed progress
        check_minimality: Whether to run the expensive minimality check

    Returns:
        True if all checks pass, False otherwise
    """
    print(f"\nVerifying Coralia Sequence ({len(sequence)} terms)")
    print("=" * 50)

    all_passed = True
    checks = [
        ("Injectivity", verify_injectivity),
        ("Surjectivity", verify_surjectivity),
        ("Cascade Validity", verify_cascade_validity),
    ]

    if check_minimality:
        checks.append(("Minimality", verify_minimality))

    for name, check_fn in checks:
        if verbose:
            print(f"\nChecking {name}...", end=" ", flush=True)

        start = time.time()
        passed, message = check_fn(sequence)
        elapsed = time.time() - start

        if verbose:
            print(f"({elapsed:.3f}s)")
        print(f"  {name}: {message}")

        if not passed:
            all_passed = False

    print("=" * 50)
    if all_passed:
        print("All verification checks PASSED")
    else:
        print("Some verification checks FAILED")

    return all_passed


def main() -> int:
    """Main entry point for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Verify Coralia Sequence properties",
        epilog="Example: python verify_uniqueness.py --terms 1000",
    )
    parser.add_argument(
        "--terms",
        "-n",
        type=int,
        default=100,
        help="Number of terms to generate and verify (default: 100)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output with timing",
    )
    parser.add_argument(
        "--skip-minimality",
        action="store_true",
        help="Skip the expensive minimality check",
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        help="Read sequence from file instead of generating",
    )

    args = parser.parse_args()

    # Get or generate the sequence
    if args.input:
        print(f"Reading sequence from {args.input}...")
        with open(args.input) as f:
            content = f.read()
        # Parse comma or newline separated integers
        sequence = [int(x.strip()) for x in content.replace(",", "\n").split() if x.strip()]
    else:
        print(f"Generating {args.terms} terms of the Coralia Sequence...")
        start = time.time()
        sequence = generate_coralia(args.terms)
        elapsed = time.time() - start
        print(f"Generation completed in {elapsed:.3f}s")

    # Run verification
    all_passed = verify_all(
        sequence,
        verbose=args.verbose,
        check_minimality=not args.skip_minimality,
    )

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
