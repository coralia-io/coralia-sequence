"""
Nearest Element Classifier
Maps arbitrary values to nearest Coralia elements.
"""

from core.coralia import C, detect_zone

def nearest_element(value):
    """Find the nearest element in C to a given value."""
    if value <= C[0]:
        return C[0]
    if value >= C[-1]:
        return C[-1]

    for i, elem in enumerate(C):
        if value == elem:
            return elem
        if value < elem:
            # Between C[i-1] and C[i]
            if i == 0:
                return elem
            prev = C[i - 1]
            if value - prev <= elem - value:
                return prev
            return elem
    return C[-1]

def classify(value):
    """Return nearest element and its zone."""
    nearest = nearest_element(value)
    zone = detect_zone(nearest)
    return {
        "input": value,
        "nearest": nearest,
        "zone": zone,
        "distance": abs(value - nearest)
    }

def batch_classify(values):
    """Classify multiple values."""
    return [classify(v) for v in values]

if __name__ == "__main__":
    test_values = [0, 4, 6, 10, 18, 26, 33, 40]
    print("Nearest Element Classification")
    print("-" * 40)
    for v in test_values:
        result = classify(v)
        print(f"{v:3d} -> {result['nearest']:2d} (Zone {result['zone']}, dist={result['distance']})")
