N, T = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
C = [c for c, t in X if t <= T]
if len(C) == 0:
    print("TLE")
else:
    print(min(C))
