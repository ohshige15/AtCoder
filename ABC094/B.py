N, M, X = map(int, input().split())
A = list(map(int, input().split()))
left = [1 if i in A else 0 for i in range(1, X)]
right = [1 if i in A else 0 for i in range(X + 1, N)]
print(min(sum(left), sum(right)))
