A, B, = map(int, input().split())
num = max(A, B)
if num == A:
    A -= 1
else:
    B -= 1
num += max(A, B)
print(num)
