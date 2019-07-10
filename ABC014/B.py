n, X = map(int, input().split())
A = list(map(int, input().split()))
X = list(format(X, "b"))
print(sum([A[i] for i, x in enumerate(reversed(X)) if x == "1"]))
