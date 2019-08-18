N = int(input())
V = sorted(list(map(int, input().split())))
x = V[0]
for i in range(N - 1):
    x = (x + V[i + 1]) / 2
print(x)
