from math import factorial
N = int(input())
A = list(map(int, input().split()))
before = A[0]
l = 0
pairs = []
for i, a in enumerate(A[1:]):
    r = i + 1
    if before >= a:
        pairs.append((l, r - 1))
        l = r
    before = a
pairs.append((l, N - 1))
num = 0
for l, r in pairs:
    n = r - l + 1
    if n >= 2:
        num += factorial(n + 1) // factorial(n - 1) // 2
    else:
        num += 1
print(num)
