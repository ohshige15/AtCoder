from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split())))
num = 0
for a, n in A.items():
    if a < n:
        num += n - a
    if a > n:
        num += n
print(num)
