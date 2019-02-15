N = int(input())
W = [input() for _ in range(N)]
exist = []
for i, w in enumerate(W):
    if w in exist:
        print("No")
        exit()
    if i != 0 and W[i - 1][-1] != w[0]:
        print("No")
        exit()
    exist.append(w)
print("Yes")
