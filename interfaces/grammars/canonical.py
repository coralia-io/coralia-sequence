"""
Canonical expression grammars for Paper 2 testing.
"""
import math

PHI = (1 + math.sqrt(5)) / 2      # Golden ratio
RHO = 1.3247179572447460          # Plastic constant
TAU = 1.8392867552141612          # Tribonacci constant
DELTA_S = 1 + math.sqrt(2)        # Silver ratio

# e/π-analytic: continuous primitives
E_PI_ANALYTIC = {
    'e²': math.e**2,
    'e^e': math.e**math.e,
    'e^π': math.e**math.pi,
    'π²': math.pi**2,
    '2^π': 2**math.pi,
    'eπ': math.e * math.pi,
}

# Recurrence-defined: powers of dominant roots
RECURRENCE_DEFINED = {
    'φ³': PHI**3,
    'φ⁵': PHI**5,
    'φ⁷': PHI**7,
    'ρ⁵': RHO**5,
    'ρ⁷': RHO**7,
    'ρ⁹': RHO**9,
    'ρ¹¹': RHO**11,
    'τ³': TAU**3,
    'τ⁴': TAU**4,
    'τ⁵': TAU**5,
    'δₛ²': DELTA_S**2,
    'δₛ³': DELTA_S**3,
    'δₛ⁴': DELTA_S**4,
}

# Test domain
def in_omega(x):
    """Ω = (4, 35]"""
    return 4 < x <= 35
