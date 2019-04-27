A, B, T = map(int, input().split())
num = 0
for _ in range(A, T + 1, A):
    num += B
print(num)
