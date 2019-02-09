K, A, B = map(int, input().split())
if A - B >= -2:
    print(1 + K)
    exit()
n = A
K = K - A + 1
if K % 2 == 0:
    n += int(K / 2) * (B - A)
else:
    n += int(K / 2) * (B - A) + 1
print(n)
