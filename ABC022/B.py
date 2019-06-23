from collections import Counter
N = int(input())
A = Counter([int(input()) for _ in range(N)]).items()
print(sum([n - 1 for a, n in A]))
