N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for _ in range(N - 1)]
n = 1 if S <= W <= T else 0
X = W
for a in A:
    X += a
    if S <= X <= T:
        n += 1
print(n)
