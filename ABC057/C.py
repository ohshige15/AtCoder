import math
N = int(input())
M = int(math.sqrt(N))
n = 1
for m in range(M, 0, -1):
    if N % m == 0:
        n = m
        break
print(max(len(str(n)), len(str(N // n))))
