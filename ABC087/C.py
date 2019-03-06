N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
n = 0
for i in range(N):
    n = max(n, sum(A1[0:i + 1]) + sum(A2[i:]))
print(n)
