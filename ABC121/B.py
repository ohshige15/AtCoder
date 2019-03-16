N, M, C = map(int, input().split())
B = list(map(int, input().split()))
As = [list(map(int, input().split())) for _ in range(N)]
num = 0
for A in As:
    s = sum([a * b for a, b in zip(A, B)]) + C
    if s > 0:
        num += 1
print(num)
