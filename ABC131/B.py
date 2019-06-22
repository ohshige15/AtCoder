N, L = map(int, input().split())
S = sum([L + i for i in range(N)])
result_d = 10 ** 9
result = 0
for i in range(N):
    r = S - (L + i)
    if abs(S - r) < result_d:
        result_d = abs(S - r)
        result = r
print(result)
