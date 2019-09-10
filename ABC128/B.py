N = int(input())
R = [[i + 1] + input().split() for i in range(N)]
R.sort(key=lambda x: (x[1], - int(x[2])))
for r, _, _ in R:
    print(r)
