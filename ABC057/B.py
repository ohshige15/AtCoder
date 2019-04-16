N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
R = [list(map(int, input().split())) for _ in range(M)]
for a, b in S:
    min_j = -1
    min_d = 10 ** 10
    for j, (c, d) in enumerate(R):
        distance = abs(a - c) + abs(b - d)
        if distance < min_d:
            min_j = j
            min_d = distance
    print(min_j + 1)
