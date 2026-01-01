"""
Cascade Triple Enumeration
Author: Emma Cecile | ORCID: 0009-0008-4120-9309
"""
from itertools import combinations

def fib_luc_upto(n=20):
    fib, luc = {0, 1}, {2, 1}
    a, b = 0, 1
    while b <= n: fib.add(b); a, b = b, a + b
    a, b = 2, 1
    while b <= n: luc.add(b); a, b = b, a + b
    return fib | luc

if __name__ == "__main__":
    FL = sorted(fib_luc_upto(20))
    all_triples = [(a,b,c) for (c,b,a) in combinations(FL, 3) if a > b > c > 0 and a+b+c == 20]
    constrained = [(a,b,c) for (a,b,c) in all_triples if c >= 5]
    print(f"Without C9: {len(all_triples)} triples")
    print(f"With C9: {len(constrained)} triple: {constrained}")
