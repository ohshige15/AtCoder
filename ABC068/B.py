N = int(input())
if N == 1:
    print(1)
    exit()
X = [2, 4, 8, 16, 32, 64, 128]
for i, x in enumerate(X):
    if N < x:
        print(X[i - 1])
        exit()
