N, Y = map(int, input().split())
for a in range(min(N, Y // 1000) + 1):
    for b in range(min(N - a, Y // 5000) + 1):
        c = N - a - b
        if 1000 * a + 5000 * b + 10000 * c == Y:
            print(c, b, a)
            exit()
print(-1, -1, -1)
