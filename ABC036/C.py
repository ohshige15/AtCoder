N = int(input())
A = [int(input()) for _ in range(N)]
X = set(A)
L = {a: a for a in X}
for i, a in zip(range(len(X)), sorted(list(X))):
    L[a] = i
for a in A:
    print(L[a])
