n = int(input())
P = [0 for _ in range(1000002)]
for _ in range(n):
    a, b = map(int, input().split())
    P[a] += 1
    P[b + 1] -= 1
for i in range(1000001):
    P[i + 1] += P[i]
result = 0
for i in range(1000001):
    result = max(P[i], result)
print(result)
