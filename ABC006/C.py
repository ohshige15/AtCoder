N, M = map(int, input().split())
# x + y + z = N
# z = N - (x + y)
# 2 * x + 3 * y + 4 * (N - (x + y)) = M
# 2x + 3y + 4N - 4x - 4y = M
# -2x - y + 4N = M
# 4N - M = 2x + y
# y = 4N - M - 2x
for x in range(N + 1):
    y = 4 * N - M - 2 * x
    if y < 0:
        continue
    z = N - (x + y)
    if z < 0:
        continue
    print(x, y, z)
    exit()
print(-1, -1, -1)
