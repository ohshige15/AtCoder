import math
N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=True)
S = sum([(-1) ** i * r ** 2 for i, r in enumerate(R)])
print(S * math.pi)
