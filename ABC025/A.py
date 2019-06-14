from itertools import product
S = list(input())
N = int(input())
X = sorted(list(product(S, repeat=2)))
print("".join(X[N - 1]))
