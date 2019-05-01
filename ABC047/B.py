W, H, N = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
i, j = 0, 0
w, h = W, H
for x, y, a in L:
    if a == 1:
        i = max(i, x)
    if a == 2:
        w = min(w, x)
    if a == 3:
        j = max(j, y)
    if a == 4:
        h = min(h, y)
if w <= i or h <= j:
    print(0)
else:
    print((w - i) * (h - j))
