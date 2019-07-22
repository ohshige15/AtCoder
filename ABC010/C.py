import math
s_x, s_y, d_x, d_y, T, V = map(int, input().split())
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
for x, y in G:
    d1 = math.sqrt((x - s_x) ** 2 + (y - s_y) ** 2)
    d2 = math.sqrt((d_x - x) ** 2 + (d_y - y) ** 2)
    if d1 + d2 <= T * V:
        print("YES")
        exit()
print("NO")
