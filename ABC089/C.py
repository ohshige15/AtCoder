from collections import Counter
from itertools import combinations
N = int(input())
S = [input()[0] for _ in range(N)]
S = Counter([s for s in S if s in ("M", "A", "R", "C", "H")])
trio = combinations(S.keys(), 3)
num = 0
for a, b, c in trio:
    num += S[a] * S[b] * S[c]
print(num)
