"""Core sequence definitions."""

C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]

gaps = [1, 1, 1, 2, 2, 2, 3, 3, 8, 7, 5]

zones = [
    {"zone": 1, "start": 0, "gaps": [1, 1, 1], "elements": [0, 1, 2, 3]},
    {"zone": 2, "start": 3, "gaps": [2, 2, 2], "elements": [5, 7, 9]},
    {"zone": 3, "start": 9, "gaps": [3, 3], "elements": [12, 15]},
    {"zone": 4, "start": 15, "gaps": [8, 7, 5], "elements": [23, 30, 35]},
]

# The three convergence points derived from φ³ ≈ 4.236
# These are where systems tip — not one threshold, but three
convergence_points = {
    "lambda_1": {
        "value": 6.25,
        "position": "between C[4]=5 and C[5]=7",
        "role": "Zone 1→2 transition"
    },
    "lambda_2": {
        "value": 17.944,  # φ⁶
        "position": "between C[8]=15 and C[9]=23",
        "role": "43% cliff — cascade begins"
    },
    "lambda_3": {
        "value": 21.246,  # Q₀
        "position": "between C[8]=15 and C[9]=23",
        "role": "Shadow/universal threshold"
    }
}


def generate():
    """Generate the Coralia Sequence from zone definitions."""
    result = [0]
    for zone in zones:
        current = zone["start"]
        for gap in zone["gaps"]:
            current += gap
            if current not in result:
                result.append(current)
    return sorted(result)
