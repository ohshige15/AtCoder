A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
X = S * A + T * B
if S + T < K:
    print(X)
else:
    print(X - (S + T) * C)
