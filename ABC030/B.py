n, m = map(int, input().split())
if 12 <= n:
    n -= 12
n = 30 * n + 30 * (m / 60)
m = 6 * m
d = abs(m - n)
if 180 < d:
    d = 360 - d
print(d)
