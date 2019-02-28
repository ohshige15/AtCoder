N = int(input()) + 2
A = [0] + list(map(int, input().split())) + [0]
C = [abs(A[i] - A[i + 1]) for i in range(N - 1)]
cost = sum(C)
for i in range(1, N - 1):
    print(cost - C[i] - C[i - 1] + abs(A[i + 1] - A[i - 1]))
