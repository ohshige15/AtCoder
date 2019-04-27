N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
X = 0
Y = 0
for v, c in zip(V, C):
    if v > c:
        X += v
        Y += c
print(X - Y)
