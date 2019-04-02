N = int(input())
A = [int(input()) for _ in range(N)]
i = 0
done = {a - 1: False for a in A}
num = 0
while True:
    i = A[i] - 1
    num += 1
    if i == 1:
        print(num)
        exit()
    if done[i]:
        print(-1)
        exit()
    done[i] = True
