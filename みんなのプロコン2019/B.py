from collections import Counter
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
X = Counter([a1, b1, a2, b2, a3, b3])
N = Counter([x[1] for x in X.items()])
if N[1] == 2 and N[2] == 2:
    print("YES")
else:
    print("NO")
