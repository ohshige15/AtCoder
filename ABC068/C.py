N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]
x = set()
y = set()
for a, b in L:
    if a == 1:
        x.add(b)
    if b == N:
        y.add(a)
if len(x & y) > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
