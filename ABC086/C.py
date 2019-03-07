N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
t1 = x1 = y1 = 0
for t2, x2, y2 in L:
    t = t2 - t1
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    if x + y > t:
        print("No")
        break
    if (t - (x + y)) % 2 != 0:
        print("No")
        break
    t1 = t2
    x1 = x2
    y1 = y2
else:
    print("Yes")
