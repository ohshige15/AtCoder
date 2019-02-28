N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
num = X
for a in A:
    num += sum([1 for i in range(0, D + 1) if i * a + 1 <= D])
print(num)
