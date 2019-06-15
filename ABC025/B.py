N, A, B = map(int, input().split())
L = [input().split() for _ in range(N)]
X = 0
for s, d_ in L:
    d = int(d_)
    if d < A:
        d = A
    elif d > B:
        d = B
    if s == "West":
        X -= d
    else:
        X += d
if X < 0:
    print("West", abs(X))
elif X > 0:
    print("East", abs(X))
else:
    print(0)
