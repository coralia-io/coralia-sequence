"""Test Suite | Author: Emma Cecile"""
C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]

def gaps(seq):
    return tuple(seq[i+1] - seq[i] for i in range(len(seq)-1))

def test_c1(): assert 0 in C
def test_c2(): assert 12 in C
def test_c3(): assert len(C) == 12
def test_c4(): assert max(C) == 35
def test_c5(): assert sum(gaps(C)) == 35
def test_c7(): assert gaps(C)[-3] > gaps(C)[-2] > gaps(C)[-1]

if __name__ == "__main__":
    for name, obj in list(globals().items()):
        if name.startswith("test_") and callable(obj):
            obj()
            print(f"pass {name}")
    print("All tests passed.")
