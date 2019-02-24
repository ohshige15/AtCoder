H, W = map(int, input().split())
S = [input() for _ in range(H)]
for h, line in enumerate(S):
    before = "."
    result = []
    for w, s in enumerate(line):
        if before == "." and s == ".":
            result.append(True)
        if before == "." and s == "#":
            result.append((h != 0 and S[h - 1][w] == "#") or (h != H - 1 and S[h + 1][w] == "#"))
        if before == "#" and s == ".":
            result.append(True)
        if before == "#" and s == "#":
            result[-1] = True
            result.append(True)
        before = s
    if not all(result):
        print("No")
        break
else:
    print("Yes")
