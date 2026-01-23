"""
Landing Demo
See where mathematical constants land relative to C.

Run: python landing_demo.py
"""
import math

# The Coralia set C
C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]

def nearest_C(x):
    return min(C, key=lambda c: abs(c - x))

def nearest_not_C(x):
    E = [i for i in range(36) if i not in C]
    return min(E, key=lambda e: abs(e - x))

def lands_on(x):
    dc = abs(x - nearest_C(x))
    de = abs(x - nearest_not_C(x))
    return "C" if dc < de else "not C"

# Test some constants
constants = {
    'e²': math.e**2,
    'e^π': math.e**math.pi,
    'φ⁵': ((1 + math.sqrt(5))/2)**5,
}

print("Where do these land?\n")
for name, val in constants.items():
    nearest = nearest_C(val) if lands_on(val) == "C" else nearest_not_C(val)
    print(f"  {name} = {val:.2f} → lands on {nearest} ∈ {lands_on(val)}")
