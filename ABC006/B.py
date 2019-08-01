n = int(input())
if n == 1 or n == 2:
    print(0)
    exit()
if n == 3:
    print(1)
    exit()
A = [0 for _ in range(n + 1)]
A[3] = 1
for i in range(4, n + 1):
    A[i] = (A[i - 1] + A[i - 2] + A[i - 3]) % 10007
print(A[n])
