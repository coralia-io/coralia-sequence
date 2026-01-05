"""
The Coralia Sequence
A logic kernel for reasoning about stability, collapse, and rhythm in any system.
https://doi.org/10.5281/zenodo.18121786
"""

from .sequence import C, gaps, zones, convergence_points, generate
from .verify import verify_uniqueness, check_axioms
from .tools import detect_zone, gap_match, coherence_score

__version__ = "1.1.0"

__all__ = [
    "C", "gaps", "zones", "convergence_points", "generate",
    "verify_uniqueness", "check_axioms",
    "detect_zone", "gap_match", "coherence_score"
]
