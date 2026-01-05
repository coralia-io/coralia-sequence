#!/usr/bin/env python3
"""
Zone Classifier
Demonstrates zone detection for arbitrary values.

Run: PYTHONPATH=/path/to/coralia-sequence python examples/zone_classifier.py
"""

from core.coralia import C, zones, detect_zone

def main():
    print("Zone Classification Demo")
    print("=" * 50)
    print()

    # Show zone boundaries
    print("Zone boundaries (from C):")
    for z in zones:
        elements = z['elements']
        print(f"  Zone {z['zone']}: {elements[0]} to {elements[-1]}")
    print()

    # Test values
    test_values = [0, 2, 4, 6, 10, 14, 20, 25, 32, 35, 40]

    print("Classifying test values:")
    print("-" * 30)
    for v in test_values:
        zone = detect_zone(v)
        print(f"  {v:3d} -> Zone {zone}")
    print()

    # Practical interpretation
    print("Zone interpretation:")
    print("  Zone 1: Stable, incremental change")
    print("  Zone 2: Moderate transitions")
    print("  Zone 3: Approaching threshold")
    print("  Zone 4: Cascade/collapse dynamics")

if __name__ == "__main__":
    main()
