from fractions import gcd
A, B, C, D = map(int, input().split())
c = B // C - (A - 1) // C
d = B // D - (A - 1) // D
CD = C * D // gcd(C, D)
cd = B // CD - (A - 1) // CD
print((B - A) - (c + d - cd) + 1)
