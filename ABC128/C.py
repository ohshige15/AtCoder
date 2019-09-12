from itertools import product
N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))
result = 0
for switches in product((0, 1), repeat=N):
    for s, p in zip(S, P):
        num = sum([switches[s_ - 1] for s_ in s[1:]])
        if num % 2 != p:
            break
    else:
        result += 1
print(result)
