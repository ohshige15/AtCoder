import math
MOD = 10 ** 9 + 7
N, M = map(int, input().split())
if abs(N - M) > 1:
    print(0)
    exit()
n = math.factorial(N) % MOD
m = math.factorial(M) % MOD
if N == M:
    print(2 * n * m % MOD)
    exit()
print(n * m % MOD)
