N, M = map(int, input().split())
L = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
c = 0
for a, b in L:
    if b <= M:
        c += a * b
        M -= b
        continue
    c += a * M
    break
print(c)
