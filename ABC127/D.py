from collections import Counter
from collections import OrderedDict
N, M = map(int, input().split())
A = list(map(int, input().split()))
A_sorted = sorted(A)
A_counter = Counter(A)
A = OrderedDict({})
for a in A_sorted:
    A[a] = A_counter[a]
X = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1], reverse=True)
result = 0
i = 0
for a in A.keys():
    num = A[a]
    while True:
        if i == M:
            result += a * num
            break
        b, c = X[i]
        if c < a:
            result += a * num
            break
        if num <= b:
            result += c * num
            X[i] = [b - num, c]
            break
        result += c * b
        num -= b
        i += 1
print(result)
