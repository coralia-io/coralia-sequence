#!/usr/bin/env python3
"""
Landing Demo
A first look at the Coralia Sequence.

Run: PYTHONPATH=/path/to/coralia-sequence python examples/landing_demo.py
"""

from core.coralia import C, gaps, zones, convergence_points

def main():
    print("The Coralia Sequence")
    print("=" * 50)
    print()

    # The sequence
    print(f"C = {C}")
    print(f"    {len(C)} elements")
    print()

    # The gap pattern
    print(f"Gaps: {gaps}")
    print("      [1,1,1] [2,2,2] [3,3] [8,7,5]")
    print("       zone1   zone2  zone3  zone4")
    print()

    # Zone structure
    print("Zone structure:")
    for z in zones:
        print(f"  Zone {z['zone']}: {z['elements']} (gaps: {z['gaps']})")
    print()

    # Key properties
    print("Key properties:")
    print(f"  Sum of elements: {sum(C)} = 142")
    print(f"  Sum of gaps: {sum(gaps)} = 35")
    print(f"  Terminal triple: (8, 7, 5) = (F6, L4, F5)")
    print(f"  43% cliff: 15/35 = 3/7 (regime change)")
    print()

    # Convergence points
    print("Convergence points:")
    for name, cp in convergence_points.items():
        print(f"  {name}: {cp['value']:.3f} - {cp['role']}")

if __name__ == "__main__":
    main()
