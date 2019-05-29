L, H = map(int, input().split())
N = int(input())
A = [int(input()) for _ in range(N)]
for a in A:
    if a < L:
        print(L - a)
    elif H < a:
        print(-1)
    else:
        print(0)
