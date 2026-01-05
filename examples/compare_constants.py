"""
Compare Constants
See the split: e-based expressions land on C, φ-based avoid it.

Run: python compare_constants.py
"""
import math

C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]
PHI = (1 + math.sqrt(5)) / 2

def lands_on_C(x):
    dc = min(abs(x - c) for c in C)
    de = min(abs(x - e) for e in range(36) if e not in C)
    return dc < de

# e-based expressions
e_based = {
    'e²': math.e**2,
    'e^e': math.e**math.e,
    'e^π': math.e**math.pi,
    '2^π': 2**math.pi,
    'eπ': math.e * math.pi,
}

# φ-based expressions
phi_based = {
    'φ³': PHI**3,
    'φ⁵': PHI**5,
    'φ⁷': PHI**7,
}

print("e-based expressions (continuous):")
print("-" * 40)
for name, val in e_based.items():
    status = "✓ C" if lands_on_C(val) else "✗ not C"
    print(f"  {name:6} = {val:6.2f} → {status}")

e_hits = sum(1 for v in e_based.values() if lands_on_C(v))
print(f"\n  Hit rate: {e_hits}/{len(e_based)} = {100*e_hits/len(e_based):.0f}%")

print("\n\nφ-based expressions (recurrence):")
print("-" * 40)
for name, val in phi_based.items():
    status = "✓ C" if lands_on_C(val) else "✗ not C"
    print(f"  {name:6} = {val:6.2f} → {status}")

phi_hits = sum(1 for v in phi_based.values() if lands_on_C(v))
print(f"\n  Hit rate: {phi_hits}/{len(phi_based)} = {100*phi_hits/len(phi_based):.0f}%")

print("\n" + "=" * 40)
print("The split: continuous → C, recurrence → not C")
