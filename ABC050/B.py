N = int(input())
T = list(map(int, input().split()))
M = int(input())
K = [list(map(int, input().split())) for _ in range(M)]
total = sum(T)
for P, X in K:
    print(total - T[P - 1] + X)
