N = int(input())
A = list(map(int, input().split()))
result = 10 ** 9
for y in range(-100, 101):
    num = sum([(a - y) ** 2 for a in A])
    result = min(num, result)
print(result)
