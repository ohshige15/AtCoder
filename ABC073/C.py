from collections import Counter
N = int(input())
A = Counter([int(input()) for _ in range(N)])
num = 0
for a, n in A.items():
    if n % 2 == 1:
        num += 1
print(num)
