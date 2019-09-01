N = int(input())
H = list(map(int, input().split()))
_max = 0
m = 0
before = H[-1]
for n in range(N - 2, -1, -1):
    now = H[n]
    _max = max(_max, m)
    if before <= now:
        m += 1
    else:
        m = 0
    before = now
_max = max(_max, m)
print(_max)
