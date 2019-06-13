N = int(input())
B = {n: int(input()) for n in range(2, N + 1)}
T = {i + 1: [] for i in range(N)}
for n, b in B.items():
    T[b].append(n)
S = {i + 1: 1 for i in range(N)}
for s in range(N, 0, -1):
    t = T[s]
    if len(t) == 0:
        continue
    x = [S[i] for i in t]
    S[s] = max(x) + min(x) + 1
print(S[1])
