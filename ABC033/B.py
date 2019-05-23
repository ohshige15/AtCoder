N = int(input())
X = [input().split() for _ in range(N)]
n = sum([int(p) for _, p in X])
for s, p in X:
    if n / 2 < int(p):
        print(s)
        exit()
print("atcoder")
