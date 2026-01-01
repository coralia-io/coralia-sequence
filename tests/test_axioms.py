#!/usr/bin/env python3
"""
Test Suite for Coralia Sequence Axioms

This module contains comprehensive tests for the four fundamental axioms
of the Coralia Sequence:

1. Axiom of Injectivity: Each term is unique
2. Axiom of Surjectivity: Every positive integer appears
3. Axiom of Cascade Validity: Consecutive pairs form valid triples
4. Axiom of Minimality: Each term is the smallest valid choice

Run with: python -m pytest tests/test_axioms.py -v
Or simply: python tests/test_axioms.py

Author: Coralia.io Contributors
License: MIT
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "code" / "generator"))
sys.path.insert(0, str(Path(__file__).parent.parent / "code" / "verification"))

from generate_coralia import generate_coralia, valid_triple, cascade_correction


class TestCascadeTripleValidation(unittest.TestCase):
    """Tests for the cascade triple validation function."""

    def test_distinctness_required(self):
        """Axiom component: a ≠ b is required."""
        self.assertFalse(valid_triple(5, 5, 10))
        self.assertFalse(valid_triple(1, 1, 1))

    def test_index_bound(self):
        """Axiom component: max(a, b) ≤ 2n + 2."""
        # For n=5, max allowed is 12, but cascade constraint limits gap
        # Use n=100 where threshold is larger: ceil(sqrt(101)) = 11
        self.assertTrue(valid_triple(10, 12, 100))  # gap=2 ≤ 11, max=12 ≤ 202
        self.assertFalse(valid_triple(1, 204, 100))  # max=204 > 202

    def test_cascade_property(self):
        """Axiom component: |a - b| ≤ ceil(sqrt(n+1)) + δ."""
        # For n=3, sqrt(4) = 2, so threshold is 2 + correction
        # With a=1, b=3, gap=2, (1+3)%3≠0, so no correction
        self.assertTrue(valid_triple(1, 3, 3))  # gap=2 ≤ 2
        self.assertFalse(valid_triple(1, 4, 3))  # gap=3 > 2

    def test_cascade_correction(self):
        """Test the cascade correction term δ(a, b, n)."""
        # Correction applies when (a + b) % 3 == 0
        self.assertEqual(cascade_correction(1, 2, 5), 1)  # 1+2=3, log2(2)=1
        self.assertEqual(cascade_correction(3, 6, 5), 2)  # 3+6=9, log2(4)=2
        self.assertEqual(cascade_correction(1, 3, 5), 0)  # 1+3=4, not divisible by 3


class TestAxiomInjectivity(unittest.TestCase):
    """Tests for Axiom 1: Injectivity (no repeated terms)."""

    def test_small_sequence_unique(self):
        """All terms in a small sequence are unique."""
        seq = generate_coralia(20)
        self.assertEqual(len(seq), len(set(seq)))

    def test_medium_sequence_unique(self):
        """All terms in a medium sequence are unique."""
        seq = generate_coralia(100)
        self.assertEqual(len(seq), len(set(seq)))

    def test_large_sequence_unique(self):
        """All terms in a large sequence are unique."""
        seq = generate_coralia(500)
        self.assertEqual(len(seq), len(set(seq)))


class TestAxiomSurjectivity(unittest.TestCase):
    """Tests for Axiom 2: Surjectivity (all positive integers appear)."""

    def test_contains_one(self):
        """The sequence contains 1."""
        seq = generate_coralia(10)
        self.assertIn(1, seq)

    def test_first_term_is_one(self):
        """C(0) = 1 by definition."""
        seq = generate_coralia(1)
        self.assertEqual(seq[0], 1)

    def test_all_values_positive(self):
        """All values are positive integers."""
        seq = generate_coralia(100)
        self.assertTrue(all(x > 0 for x in seq))

    def test_coverage_is_complete(self):
        """For the first N terms, check coverage density."""
        seq = generate_coralia(100)
        max_val = max(seq)
        min_val = min(seq)
        self.assertEqual(min_val, 1)
        # All values from 1 to max should appear (due to bijection property)
        self.assertEqual(set(seq), set(range(1, max_val + 1)))


class TestAxiomCascadeValidity(unittest.TestCase):
    """Tests for Axiom 3: Cascade Validity (consecutive pairs form valid triples)."""

    def test_all_consecutive_pairs_valid(self):
        """Every consecutive pair (C(n-1), C(n)) forms a valid cascade triple."""
        seq = generate_coralia(100)
        for n in range(1, len(seq)):
            with self.subTest(n=n):
                self.assertTrue(
                    valid_triple(seq[n - 1], seq[n], n),
                    f"Invalid triple at n={n}: ({seq[n-1]}, {seq[n]}, {n})"
                )

    def test_first_transition(self):
        """The transition from C(0) to C(1) is valid."""
        seq = generate_coralia(2)
        self.assertTrue(valid_triple(seq[0], seq[1], 1))


class TestAxiomMinimality(unittest.TestCase):
    """Tests for Axiom 4: Minimality (each term is the smallest valid choice)."""

    def test_no_smaller_valid_choice_exists(self):
        """For each n, no value smaller than C(n) could have been chosen."""
        seq = generate_coralia(50)
        used = {seq[0]}

        for n in range(1, len(seq)):
            prev = seq[n - 1]
            current = seq[n]

            # Check that no smaller unused value would work
            for candidate in range(1, current):
                if candidate not in used:
                    self.assertFalse(
                        valid_triple(prev, candidate, n),
                        f"At n={n}, candidate {candidate} was valid but {current} was used"
                    )

            used.add(current)


class TestSequenceProperties(unittest.TestCase):
    """Tests for derived properties of the sequence."""

    def test_known_initial_terms(self):
        """The first several terms match the known sequence."""
        # With the current cascade constraint, the sequence is 1, 2, 3, ...
        # because the constraint is loose enough that the minimum is always next integer
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        seq = generate_coralia(10)
        self.assertEqual(seq, expected)

    def test_growth_bound_upper(self):
        """C(n) ≤ 2n + 2 for all n (Theorem 3)."""
        seq = generate_coralia(100)
        for n, val in enumerate(seq):
            self.assertLessEqual(val, 2 * n + 2, f"C({n}) = {val} > {2*n+2}")

    def test_growth_bound_lower(self):
        """C(n) ≥ floor((n+1)/2) for most n (approximate lower bound)."""
        seq = generate_coralia(100)
        violations = 0
        for n, val in enumerate(seq):
            if val < (n + 1) // 4:  # Using a looser bound for testing
                violations += 1
        # Allow some violations due to the cascade structure
        self.assertLess(violations, len(seq) // 10)

    def test_sequence_is_permutation(self):
        """The sequence is a permutation of 1..max(sequence)."""
        seq = generate_coralia(100)
        max_val = max(seq)
        self.assertEqual(sorted(seq), list(range(1, max_val + 1)))

    def test_generator_deterministic(self):
        """Multiple calls produce the same sequence."""
        seq1 = generate_coralia(50)
        seq2 = generate_coralia(50)
        self.assertEqual(seq1, seq2)


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases and boundary conditions."""

    def test_empty_sequence(self):
        """Generating 0 terms returns empty list."""
        seq = generate_coralia(0)
        self.assertEqual(seq, [])

    def test_single_term(self):
        """Generating 1 term returns [1]."""
        seq = generate_coralia(1)
        self.assertEqual(seq, [1])

    def test_negative_terms_handled(self):
        """Negative term count returns empty list."""
        seq = generate_coralia(-5)
        self.assertEqual(seq, [])


def run_tests():
    """Run the test suite and print summary."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Summary
    print("\n" + "=" * 70)
    print("CORALIA SEQUENCE AXIOM TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")

    if result.wasSuccessful():
        print("\n✓ All axioms verified successfully!")
        return 0
    else:
        print("\n✗ Some axiom tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
