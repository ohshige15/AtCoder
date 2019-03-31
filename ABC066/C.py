from collections import deque
n = int(input())
A = list(map(int, input().split()))
X = deque([str(A[0])])
append_ = True if n % 2 != 0 else False
for a in A[1:]:
    if append_:
        X.append(str(a))
    else:
        X.appendleft(str(a))
    append_ = not append_
print(" ".join(X))
