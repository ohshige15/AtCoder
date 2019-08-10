from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]
L = defaultdict(list)
for i, s in enumerate(S):
    s = "".join(sorted(s))
    L[s].append(i)
num = 0
for x in L.values():
    num += sum(range(len(x)))
print(num)
