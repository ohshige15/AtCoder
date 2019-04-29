N, x = map(int, input().split())
A = list(map(int, input().split()))
num = 0
for i in range(N - 1):
    diff = A[i] + A[i + 1] - x
    if diff <= 0:
        continue
    if diff <= A[i + 1]:
        A[i + 1] -= diff
    else:
        A[i] -= (diff - A[i + 1])
        A[i + 1] = 0
    num += diff
print(num)
