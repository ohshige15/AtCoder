N, D, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(D)]
Y = [list(map(int, input().split())) for _ in range(K)]
for s, k in Y:
    now = s
    for i, (l, r) in enumerate(X):
        if now < l or r < now:
            continue
        if l <= k <= r:
            print(i + 1)
            break
        if k < l:
            now = l
        else:
            now = r
