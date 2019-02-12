N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]
Y = sorted([(i, (p, y)) for i, (p, y) in enumerate(L)], key=lambda x: x[1])
result = [""] * M
x = 0
before_p = 0
for i, (p, y) in Y:
    if before_p != p:
        x = 0
        before_p = p
    x += 1
    result[i] = "{:06}{:06}".format(p, x)
for r in result:
    print(r)
