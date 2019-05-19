from collections import deque
N = int(input())
X = [list(map(int, input().split())) for _ in range(N - 1)]
class UnionFind:
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.par[y] = x
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
uf = UnionFind(N)
next_ = [[] for _ in range(N)]
for u, v, w in X:
    next_[u - 1].append((v - 1, w))
    next_[v - 1].append((u - 1, w))
    uf.union(u - 1, v - 1)
now = min(set(uf.par))
result = ["" for _ in range(N)]
result[now] = "0"
ver = deque([now])
while len(ver) > 0:
    now = ver.pop()
    color = result[now]
    for n, w in next_[now]:
        if result[n] != "":
            continue
        if w % 2 == 0:
            result[n] = color
        else:
            result[n] = "1" if color == "0" else "0"
        ver.append(n)
print("\n".join(result))
