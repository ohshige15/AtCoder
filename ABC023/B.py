N = int(input())
S = input()
L = "b"
for i in range(N + 1):
    if S == L:
        print(3 * i)
        exit()
    L = "a" + L + "c"
    if S == L:
        print(3 * i + 1)
        exit()
    L = "c" + L + "a"
    if S == L:
        print(3 * i + 2)
        exit()
    L = "b" + L + "b"
    if N < 2 * i + 1:
        print(-1)
        exit()
