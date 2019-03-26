from collections import Counter
N = int(input())
A = list(map(int, input().split()))
X = Counter([4 if a % 4 == 0 else (2 if a % 2 == 0 else 1) for a in A])
for x in (1, 2, 4):
    if x not in X:
        X[x] = 0
if X[4] + 1 < X[1]:
    print("No")
    exit()
if X[4] + 1 == X[1] and X[2] != 0:
    print("No")
    exit()
print("Yes")
