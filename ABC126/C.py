import math
N, K = map(int, input().split())
result = 0.0
for n in range(1, N + 1):
    if K <= n:
        result += 1 / N
        continue
    t = (K + n - 1) // n
    x = math.ceil(math.log2(t))
    result += 1 / N * (0.5 ** x)
print(result)
