import math
n = int(input())
num = 10 ** 9
for x in range(n, 0, -1):
    i = int(math.sqrt(x))
    for j in range(i, 0, -1):
        if x % j == 0:
            diff1 = abs(x // j - j)
            diff2 = n - x
            num = min(num, diff1 + diff2)
            break
print(num)
