N = int(input())
P = list(map(int, input().split()))
num = 0
for i in range(N - 1):
    if i + 1 == P[i]:
        P[i], P[i + 1] = P[i + 1], P[i]
        num += 1
if N >= 2 and N == P[-1]:
    P[-1], P[-2] = P[-2], P[-1]
    num += 1
print(num)
