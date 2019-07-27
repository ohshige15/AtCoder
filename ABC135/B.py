N = int(input())
P = list(map(int, input().split()))
X = sorted(P)
num = 0
for x, p in zip(X, P):
    if x != p:
        num += 1
if num == 0 or num == 2:
    print("YES")
else:
    print("NO")
