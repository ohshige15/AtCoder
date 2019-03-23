from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split())))
A = sorted([(k, v) for k, v in A.items() if v >= 2], key=lambda x: x[0], reverse=True)
if len(A) == 0:
    print(0)
    exit()
if len(A) == 1:
    if A[0][1] >= 4:
        print(A[0][0] ** 2)
    else:
        print(0)
    exit()
if A[0][1] >= 4:
    print(A[0][0] ** 2)
else:
    print(A[0][0] * A[1][0])
