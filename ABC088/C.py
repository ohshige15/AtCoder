C = [list(map(int, input().split())) for _ in range(3)]
targets = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)]
for i, j in targets:
    if (C[i][i] + C[i][j] + C[j][i] + C[j][j]) % 2 != 0:
        print("No")
        break
else:
    if sum([sum(c) for c in C]) % 3 != 0:
        print("No")
    else:
        print("Yes")
