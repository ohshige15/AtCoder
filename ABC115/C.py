N, K = map(int, input().split())
H = sorted([int(input()) for _ in range(N)], reverse=True)
diffs = [H[i] - H[i + K - 1] for i in range(len(H) - K + 1)]
print(min(diffs))
