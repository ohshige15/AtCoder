n, a, b = map(int, input().split())
num = 0
for x in range(n + 1):
    s = sum(map(int, list(str(x))))
    if a <= s <= b:
        num += x
print(num)
