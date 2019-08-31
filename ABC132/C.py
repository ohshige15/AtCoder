N = int(input())
D = sorted(list(map(int, input().split())))
h = N // 2
print(D[h] - D[h - 1])
