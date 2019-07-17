from scipy.sparse.csgraph import floyd_warshall
# def floyd_warshall(d, n):
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 d[i][j] = min(d[i][j], d[i][k] + d[k][j])
#     return d
N, M = map(int, input().split())
d = [[float("inf") if i != j else 0 for i in range(N)] for j in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    d[a - 1][b - 1] = d[b - 1][a - 1] = t
d = floyd_warshall(d)
print(min([max(t) for t in d]))
