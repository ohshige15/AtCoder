from itertools import product
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
for indexes in product(range(K), repeat=N):
    xor = 0
    for t, i in enumerate(indexes):
        xor ^= T[t][i]
    if xor == 0:
        print("Found")
        exit()
print("Nothing")
