from collections import defaultdict
from bisect import bisect
s = input()
t = input()
S = defaultdict(list)
for i, c in enumerate(list(s)):
    S[c].append(i + 1)
now = 0
num = 0
for c in t:
    if c not in S:
        print(-1)
        exit()
    P = S[c]
    x = bisect(P, now)
    if x < len(P):
        num += P[x] - now
        now = P[x]
    else:
        num += len(s) - now
        num += P[0]
        now = P[0]
print(num)
