import math
N = int(input())
A = sorted(list(map(int, input().split())))
if N == 2:
    print(max(A))
    exit()
result = []
num = 0
for a in A[1:]:
    if a % A[0] != 0:
        num += 1
        if num == 2:
            break
else:
    result.append(A[0])
for n in range(2, int(math.sqrt(A[0])) + 1):
    if A[0] % n != 0:
        continue
    num = 0
    x = A[0] // n
    for a in A[1:]:
        if a % x != 0:
            num += 1
            if num == 2:
                break
    else:
        result.append(x)
    num = 0
    for a in A[1:]:
        if a % n != 0:
            num += 1
            if num == 2:
                break
    else:
        result.append(n)
num = 0
B = A[0:1] + A[2:]
for a in B:
    if a % A[1] != 0:
        num += 1
        if num == 2:
            break
else:
    result.append(A[1])
for n in range(2, int(math.sqrt(A[1])) + 1):
    if A[1] % n != 0:
        continue
    num = 0
    x = A[1] // n
    for a in B:
        if a % x != 0:
            num += 1
            if num == 2:
                break
    else:
        result.append(x)
    num = 0
    for a in B:
        if a % n != 0:
            num += 1
            if num == 2:
                break
    else:
        result.append(n)
if len(result) != 0:
    print(max(result))
else:
    print(1)
