N, K = map(int, input().split())
A = list(map(int, input().split()))
a = sum(A[:K])
num = a
for i in range(N - K):
    a -= A[i]
    a += A[i + K]
    num += a
print(num)
