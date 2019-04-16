import math
from collections import Counter
N, A, B = map(int, input().split())
V = sorted(Counter(list(map(int, input().split()))).items(), key=lambda x: x[0], reverse=True)
if A <= V[0][1]:
    print(V[0][0])
    x = min(V[0][1], B)
    num = 0
    for i in range(A, x + 1):
        num += math.factorial(V[0][1]) // (math.factorial(V[0][1] - i) * math.factorial(i))
    print(num)
    exit()
l = []
num = 0
for v, n in V:
    if n >= A:
        l.extend([v] * A)
        num = math.factorial(n) // (math.factorial(n - A) * math.factorial(A))
        break
    else:
        l.extend([v] * n)
        A -= n
        B -= n
print(sum(l) / len(l))
print(num)
