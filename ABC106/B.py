N = int(input())
count = 0
for n in range(1, N + 1, 2):
    divisor = [i for i in range(2, n // 2 + 1) if n % i == 0]
    if len(divisor) == 6:
        count += 1
print(count)
