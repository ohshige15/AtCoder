N = int(input())
H = list(map(int, input().split()))
for n in range(N - 1, 0, -1):
    if H[n - 1] - H[n] > 1:
        print("No")
        exit()
    if H[n - 1] - H[n] == 1:
        H[n - 1] -= 1
print("Yes")
