N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
G = [0] * (N + 1)
for L, R in X:
    G[L - 1] += 1
    G[R] -= 1
for i in range(N):
    G[i + 1] += G[i]
print(sum([1 if g == M else 0 for g in G]))
