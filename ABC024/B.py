N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.append(A[-1] + T)
t = 0
for i in range(N):
    a = A[i + 1] - A[i]
    t += T if a > T else a
print(t)
