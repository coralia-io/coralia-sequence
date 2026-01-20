"""
"""
Music / Interval-Class Mapping
Status: OBSERVED CORRESPONDENCE (descriptive)

This module does NOT claim that Coralia "generates" music theory.
It only labels Coralia gap sizes in semitones as interval classes (12-TET),
as a way to describe the lattice's internal step structure.
"""

from core.coralia import C, gaps, zones  # assumes these exist

# 12-tone equal temperament interval-class labels (semitones)
IC_LABELS = {
    0: "unison/octave equivalence",
    1: "minor 2nd (semitone)",
    2: "major 2nd (whole tone)",
    3: "minor 3rd",
    4: "major 3rd",
    5: "perfect 4th",
    6: "tritone",
    7: "perfect 5th",
    8: "minor 6th",
    9: "major 6th",
    10: "minor 7th",
    11: "major 7th",
    12: "octave",
}

def ic_label(semitones: int) -> str:
    """Return a conservative label for a semitone distance (mod 12)."""
    return IC_LABELS.get(semitones % 12, f"{semitones} semitones")

def analyze():
    print("Music / Interval-Class Description")
    print("=" * 44)
    print("Status: OBSERVED CORRESPONDENCE (descriptive)")
    print()
    print("What this is:")
    print("- A labeling of Coralia gap sizes as semitone interval classes (12-TET).")
    print()
    print("What this is NOT:")
    print("- Not a claim that Coralia generates harmony, consonance rules, or resolution.")
    print("- Not a claim of universality across tuning systems or musical traditions.")
    print()

    print(f"Coralia lattice size: {len(C)} elements")
    print(f"Coralia gaps: {gaps}")
    print("Gap labels (12-TET interval classes):")
    for g in gaps:
        print(f"  {g:>2} → {ic_label(g)}")
    print()

    # If `zones` is structured, we can still describe it without over-interpretation
    print("Zone description (interval-class framing):")
    print("  Z₁ (dense steps): emphasizes 1-semitone steps (fine-grained adjacency)")
    print("  Z₂ (moderate steps): emphasizes 2-semitone steps (whole-tone adjacency)")
    print("  Z₃ (wider steps): emphasizes 3-semitone steps (minor-third adjacency)")
    print("  Z₄ (sparse steps): emphasizes larger step sizes (context-dependent meaning)")
    print()
    print("Note: 'tension' and 'resolution' are context-dependent in music.")
    print("This analysis does not assign harmonic function to intervals.")

if __name__ == "__main__":
    analyze()
