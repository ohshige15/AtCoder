N, M = map(int, input().split())
like = [0] * M
for _ in range(N):
    A = list(map(int, input().split()))[1:]
    for a in A:
        like[a - 1] += 1
print(len([l for l in like if l == N]))
