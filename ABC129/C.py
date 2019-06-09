N, M = map(int, input().split())
A = [True for _ in range(N + 1)]
for _ in range(M):
    A[int(input())] = False
num = [0 for _ in range(N + 1)]
num[0] = num[1] = 1
for n in range(2, N + 1):
    if not A[n]:
        continue
    if A[n - 1]:
        num[n] += num[n - 1]
    if A[n - 2]:
        num[n] += num[n - 2]
    num[n] %= 10 ** 9 + 7
print(num[N] % (10 ** 9 + 7))
