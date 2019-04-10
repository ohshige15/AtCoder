N, T = map(int, input().split())
t_list = list(map(int, input().split()))
num = 0
for i in range(N - 1):
    t = t_list[i + 1] - t_list[i]
    if t <= T:
        num += t
    else:
        num += T
print(num + T)
