N = int(input())
A = list(map(int, input().split()))
dp = [[10 ** 9, 10 ** 9] for _ in range(N)]
dp[0][0] = dp[0][1] = 0
dp[1][0] = abs(A[1] - A[0])
dp[1][1] = 10 ** 9
for i in range(2, N):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + abs(A[i] - A[i - 1])
    dp[i][1] = min(dp[i - 2][0], dp[i - 2][1]) + abs(A[i] - A[i - 2])
print(min(dp[N - 1]))
