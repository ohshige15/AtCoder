N, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(Q)]
A = [0] * N
for L, R, T in X:
    A[L - 1:R] = [T] * (R - L + 1)
print("\n".join(map(str, A)))
