N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
if 0 in S:
    print(N)
    exit()
right = 0
x = 1
result = 0
num = 0
for left in range(N):
    while right < N and x * S[right] <= K:
        x *= S[right]
        num += 1
        right += 1
    if num > 0:
        result = max(result, num)
        x //= S[left]
        num -= 1
print(result)
