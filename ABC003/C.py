N, K = map(int, input().split())
R = list(sorted(list(map(int, input().split()))))
rate = 0
for r in R[-K:]:
    rate = (rate + r) / 2
print(rate)
