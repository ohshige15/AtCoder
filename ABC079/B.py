N = int(input())
L = {-1: -1, 0: 2}
for i in range(1, N + 1):
    L[i] = L[i - 1] + L[i - 2]
print(L[N])
