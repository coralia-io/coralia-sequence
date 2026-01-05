"""
Planetary Resonance
Status: ORIGIN (Kirkwood gaps, angle of repose)

This is where the 3 tipping points framework came from.
"""

from coralia import C, gaps, convergence_points

def analyze():
    """Planetary resonance and stability analysis."""
    print("Planetary Resonance Analysis")
    print("=" * 40)
    print("Status: ORIGIN — where the framework came from")
    print()
    print("Kirkwood gaps in asteroid belt:")
    print("  Orbital resonances create forbidden zones")
    print("  Gap structure mirrors Coralia gaps")
    print()
    print("Angle of repose discovery:")
    print("  Systems have 3 tipping points, not 1")
    print("  Material stability follows zone structure")
    print()
    print("Convergence points:")
    for name, cp in convergence_points.items():
        print(f"  {name}: {cp['value']:.3f} — {cp['role']}")
    print()
    print("The 43% cliff (15/35 = 3/7) = regime change threshold")

if __name__ == "__main__":
    analyze()
