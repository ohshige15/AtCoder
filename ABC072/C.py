from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = []
for a in A:
    B.extend([a - 1, a, a + 1])
B = Counter(B)
print(B.most_common(1)[0][1])
