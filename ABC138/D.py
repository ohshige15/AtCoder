N, Q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N - 1)]
P = [list(map(int, input().split())) for _ in range(Q)]
G = [[] for _ in range(N + 1)]
X = [0] * (N + 1)
for a, b in L:
    G[a].append(b)
for p, x in P:
    X[p] += x
for a, A in enumerate(G):
    for b in A:
        X[b] += X[a]
print(" ".join(map(str, X[1:])))
