from functools import reduce
from fractions import gcd
N = int(input())
T = [int(input()) for _ in range(N)]
print(reduce(lambda x, y: (x * y) // gcd(x, y), T, 1))
