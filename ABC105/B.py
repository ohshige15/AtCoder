N = int(input())
for c in range(0, N + 1, 4):
    if (N - c) % 7 == 0:
        print("Yes")
        exit()
print("No")
