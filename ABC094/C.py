N = int(input())
X = list(map(int, input().split()))
L = sorted(X)
x1, x2 = L[N // 2 - 1], L[N // 2]
for x in X:
    if x1 < x:
        print(x1)
    else:
        print(x2)
