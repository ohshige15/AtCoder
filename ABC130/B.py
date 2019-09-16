N, X = map(int, input().split())
L = list(map(int, input().split()))
num = 0
for n, l in enumerate(L):
    num += l
    if num > X:
        print(n + 1)
        exit()
print(N + 1)
