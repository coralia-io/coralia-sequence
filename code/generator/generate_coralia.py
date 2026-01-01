"""
Coralia Sequence Generator
Author: Emma Cecile | ORCID: 0009-0008-4120-9309
"""

def generate_coralia():
    zones = [
        {'start': 0, 'gaps': [1, 1, 1]},
        {'start': 3, 'gaps': [2, 2, 2]},
        {'start': 9, 'gaps': [3, 3]},
        {'start': 15, 'gaps': [8, 7, 5]}
    ]
    result = [0]
    for zone in zones:
        current = zone['start']
        for gap in zone['gaps']:
            current += gap
            if current not in result:
                result.append(current)
    return sorted(result)

def gaps(seq):
    return tuple(seq[i+1] - seq[i] for i in range(len(seq)-1))

C = generate_coralia()
assert C == [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]

if __name__ == "__main__":
    print(f"C = {C}")
    print(f"gaps(C) = {gaps(C)}")
