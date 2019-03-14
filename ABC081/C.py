from collections import Counter
N, K = map(int, input().split())
A = Counter(list(map(int, input().split())))
A = sorted(A.items(), key=lambda x: x[1], reverse=True)
print(sum([a[1] for a in A[K:]]))
