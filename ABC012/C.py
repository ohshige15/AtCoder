n = 2025 - int(input())
for i in range(1, 10):
    if n % i == 0 and 1 <= n // i <= 9:
        print(i, "x", n // i)
