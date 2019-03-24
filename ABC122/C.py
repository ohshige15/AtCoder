N, Q = map(int, input().split())
S = input()
X = [list(map(int, input().split())) for _ in range(Q)]
L = [0] * N
n = 0
for i in range(N - 1):
    if S[i:i + 2] == "AC":
        n += 1
    L[i] = n
L[-1] = n
R = [0] * N
n = 0
for i in range(1, N):
    if S[i - 1:i + 1] == "AC":
        n += 1
    R[i] = n
R[-1] = n
for l, r in X:
    if l == 1:
        print(R[r - 1])
    else:
        print(R[r - 1] - L[l - 2])
