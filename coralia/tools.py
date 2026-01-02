"""Analysis tools."""

from .sequence import C, gaps, zones, convergence_points


def detect_zone(value, ceiling=35):
    """
    Map a value to its zone (1-4).
    Scales to [0, 35] if ceiling differs.
    """
    if ceiling != 35:
        value = (value / ceiling) * 35

    if value <= 3:
        return 1
    elif value <= 9:
        return 2
    elif value <= 15:
        return 3
    else:
        return 4


def gap_match(sequence):
    """
    Compare a sequence's gaps to Coralia gap pattern.
    Returns similarity score 0-1.
    """
    if len(sequence) < 2:
        return {"score": 0, "error": "Sequence too short"}

    s = sorted(sequence)
    g = [s[i+1] - s[i] for i in range(len(s) - 1)]

    if max(g) == 0:
        return {"score": 0, "error": "No variation"}

    norm_input = [x / max(g) for x in g]
    norm_coralia = [x / max(gaps) for x in gaps]

    min_len = min(len(norm_input), len(norm_coralia))
    diff = sum(abs(norm_input[i] - norm_coralia[i]) for i in range(min_len))
    score = max(0, 1 - diff / min_len)

    return {
        "score": round(score, 3),
        "input_gaps": g,
        "coralia_gaps": gaps
    }


def coherence_score(data):
    """
    Calculate alignment with Coralia structure.
    Returns score 0-1 with interpretation.
    """
    if not data:
        return {"score": 0, "interpretation": "No data"}

    c_set = set(C)
    hits = sum(1 for x in data if x in c_set)
    element_score = hits / len(data)

    gap_result = gap_match(data) if len(data) > 1 else {"score": 0}
    gap_score = gap_result.get("score", 0)

    combined = (element_score + gap_score) / 2

    if combined > 0.8:
        interp = "Strong alignment"
    elif combined > 0.5:
        interp = "Moderate alignment"
    elif combined > 0.2:
        interp = "Weak alignment"
    else:
        interp = "No significant alignment"

    return {
        "score": round(combined, 3),
        "element_score": round(element_score, 3),
        "gap_score": round(gap_score, 3),
        "interpretation": interp
    }
