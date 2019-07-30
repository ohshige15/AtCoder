from collections import deque
R, C = map(int, input().split())
s_x, s_y = map(int, input().split())
g_x, g_y = map(int, input().split())
M = [list(input()) for _ in range(R)]
S = [[10 ** 9 for _ in range(C)] for _ in range(R)]
S[s_y - 1][s_x - 1] = 0
q = deque([(s_x - 1, s_y - 1)])
while len(q) > 0:
    now = q.pop()
    # 上
    x, y = now[0], now[1] - 1
    if 0 <= y and M[y][x] == ".":
        if S[now[1]][now[0]] + 1 < S[y][x]:
            S[y][x] = S[now[1]][now[0]] + 1
            q.appendleft((x, y))
    # 下
    x, y = now[0], now[1] + 1
    if y < R and M[y][x] == ".":
        if S[now[1]][now[0]] + 1 < S[y][x]:
            S[y][x] = S[now[1]][now[0]] + 1
            q.appendleft((x, y))
    # 左
    x, y = now[0] - 1, now[1]
    if 0 <= x and M[y][x] == ".":
        if S[now[1]][now[0]] + 1 < S[y][x]:
            S[y][x] = S[now[1]][now[0]] + 1
            q.appendleft((x, y))
    # 右
    x, y = now[0] + 1, now[1]
    if x < C and M[y][x] == ".":
        if S[now[1]][now[0]] + 1 < S[y][x]:
            S[y][x] = S[now[1]][now[0]] + 1
            q.appendleft((x, y))
print(S[g_x - 1][g_y - 1])
