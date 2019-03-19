H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w] != ".":
            continue
        num = 0
        if h != 0 and S[h - 1][w] == "#":
            num += 1
        if h != H - 1 and S[h + 1][w] == "#":
            num += 1
        if w != 0 and S[h][w - 1] == "#":
            num += 1
        if w != W - 1 and S[h][w + 1] == "#":
            num += 1
        if h != 0 and w != 0 and S[h - 1][w - 1] == "#":
            num += 1
        if h != H - 1 and w != 0 and S[h + 1][w - 1] == "#":
            num += 1
        if h != 0 and w != W - 1 and S[h - 1][w + 1] == "#":
            num += 1
        if h != H - 1 and w != W - 1 and S[h + 1][w + 1] == "#":
            num += 1
        S[h][w] = str(num)
    print("".join(S[h]))
