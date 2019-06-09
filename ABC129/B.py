N = int(input())
W = list(map(int, input().split()))
result = 10 ** 9
for i in range(N - 1):
    s1 = sum(W[:i + 1])
    s2 = sum(W[i + 1:])
    result = min(abs(s1 - s2), result)
print(result)
