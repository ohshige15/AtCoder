from collections import Counter
N = int(input())
S = Counter([input() for _ in range(N)])
M = int(input())
T = Counter([input() for _ in range(M)])
n = 0
for s, s_c in S.items():
    t_c = 0 if s not in T else T[s]
    n = max(n, s_c - t_c)
print(n)
