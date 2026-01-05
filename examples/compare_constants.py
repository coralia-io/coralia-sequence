#!/usr/bin/env python3
"""
Compare Constants
Shows how Coralia convergence points relate to mathematical constants.

Run: PYTHONPATH=/path/to/coralia-sequence python examples/compare_constants.py
"""

import math
from core.coralia import C, convergence_points

def main():
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio

    print("Coralia and Mathematical Constants")
    print("=" * 50)
    print()

    print(f"Golden ratio (phi): {phi:.6f}")
    print(f"phi^2: {phi**2:.6f}")
    print(f"phi^3: {phi**3:.6f}")
    print(f"phi^6: {phi**6:.6f}")
    print()

    print("Convergence points from Coralia:")
    for name, cp in convergence_points.items():
        print(f"  {name}: {cp['value']:.6f}")
        if 'formula' in cp:
            print(f"         {cp['formula']}")
    print()

    # The 43% cliff
    print("The 43% cliff:")
    cliff = 15/35
    print(f"  15/35 = {cliff:.6f} = 3/7")
    print(f"  This marks the regime change at Zone 4")
    print()

    # Fibonacci-Lucas terminal
    print("Terminal triple (8, 7, 5):")
    print("  F6 = 8  (Fibonacci)")
    print("  L4 = 7  (Lucas)")
    print("  F5 = 5  (Fibonacci)")
    print("  Sum: 8 + 7 + 5 = 20")

if __name__ == "__main__":
    main()
