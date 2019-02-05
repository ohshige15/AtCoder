n, y = map(int, input().split())
for x_10000 in range(y // 10000 + 1):
    for x_5000 in range(y // 5000 + 1):
        x_1000 = n - (x_10000 + x_5000)
        if x_1000 < 0:
            break
        cost = x_10000 * 10000 + x_5000 * 5000 + x_1000 * 1000
        if cost > y:
            break
        if cost == y:
            print(x_10000, x_5000, x_1000)
            exit()
print("-1 -1 -1")
