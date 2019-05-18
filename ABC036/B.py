N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        print(S[N - j - 1][i], end="")
    print()
