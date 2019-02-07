n = int(input())
t = x = y = 0
result = "Yes"
for _ in range(n):
    t_now, x_now, y_now = map(int, input().split())
    move = abs(x_now - x) + abs(y_now - y)
    diff = t_now - t
    if move > diff or (diff - move) % 2 != 0:
        result = "No"
    t, x, y = t_now, x_now, y_now
print(result)
