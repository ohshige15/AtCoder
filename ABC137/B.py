K, X = map(int, input().split())
a = max(X - K + 1, -1000000)
b = min(X + K - 1, 1000000)
result = []
for i in range(a, b + 1):
    result.append(str(i))
print(" ".join(result))
