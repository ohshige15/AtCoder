N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
X = {}
for a, b in L:
    if b not in X:
        X[b] = []
    X[b].append(a)
now = 0
for b, Y in sorted(X.items(), key=lambda x: x[0]):
    for a in Y:
        now += a
        if b < now:
            print("No")
            exit()
print("Yes")
