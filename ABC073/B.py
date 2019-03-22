N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
print(sum([r - l + 1 for l, r in L]))
