N = int(input())
num = 0
for n in range(1, N + 1):
    if len(str(n)) % 2 == 1:
        num += 1
print(num)
