N = int(input())
L = [input().split() for _ in range(N)]
S = sum([int(x) if u == "JPY" else float(x) * 380000 for x, u in L])
print(S)
