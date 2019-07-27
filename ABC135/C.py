N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
num = 0
p = 0
for i in range(N):
    a = A[i]
    if a <= p:
        num += a
        p = B[i]
        continue
    a -= p
    num += p
    if a <= B[i]:
        num += a
        p = B[i] - a
        continue
    num += B[i]
    p = 0
else:
    num += min(p, A[-1])
print(num)
