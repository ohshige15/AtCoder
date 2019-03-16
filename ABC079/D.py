from itertools import chain
from collections import Counter
H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = Counter(list(chain.from_iterable([list(map(int, input().split())) for _ in range(H)])))
for _ in range(100):
    for i in range(10):
        for j in range(10):
            c = min([C[i][k] + C[k][j] for k in range(10)])
            C[i][j] = min(c, C[i][j])
num = 0
for i, n in A.items():
    if i == -1:
        continue
    num += C[i][1] * n
print(num)
