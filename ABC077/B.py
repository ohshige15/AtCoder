N = int(input())
for i in range(1, N + 2):
    if i ** 2 > N:
        print((i - 1) ** 2)
        break
