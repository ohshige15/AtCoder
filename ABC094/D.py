import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
n = A[-1]
x = bisect.bisect_left(A, n / 2)
if x == 0:
    print(n, A[0])
elif x == N:
    print(n, A[-1])
else:
    if n / 2 - A[x - 1] <= A[x] - n / 2:
        print(n, A[x - 1])
    else:
        print(n, A[x])
