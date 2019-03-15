from itertools import product
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
x = - 10 ** 10
for a in product((0, 1), repeat=10):
    if not any(a):
        print(a)
        continue
    num = 0
    for f, p in zip(F, P):
        c = sum(map(lambda z: z[0] * z[1], zip(a, f)))
        num += p[c]
    x = max(x, num)
print(x)
