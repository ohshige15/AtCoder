H, W = map(int, input().split())
N = int(input())
A = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])
C = [["0" for _ in range(W)] for _ in range(H)]
w = h = 0
direction = 1
for i, a in A:
    for j in range(a):
        C[h][w] = str(i + 1)
        w += direction
        if w == -1:
            w = 0
            h += 1
            direction = 1
            continue
        if w == W:
            w = W - 1
            h += 1
            direction = -1
for c in C:
    print(" ".join(c))
