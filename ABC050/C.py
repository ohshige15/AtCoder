from collections import Counter
N = int(input())
A = sorted(Counter(list(map(int, input().split()))).items(), key=lambda x: x[0])
if len(A) != (N + 1) // 2:
    print(0)
    exit()
if N % 2 == 1:
    if A[0][0] != 0 or A[0][1] != 1:
        print(0)
        exit()
    for (a, n), i in zip(A[1:], range(2, N + 1, 2)):
        if a != i or n != 2:
            print(0)
            exit()
else:
    for (a, n), i in zip(A, range(1, N + 1, 2)):
        if a != i or n != 2:
            print(0)
            exit()
print(2 ** (N // 2) % (10 ** 9 + 7))
