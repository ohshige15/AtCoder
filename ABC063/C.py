N = int(input())
S = [int(input()) for _ in range(N)]
score = sum(S)
if score % 10 != 0:
    print(score)
    exit()
R = [s for s in S if s % 10 != 0]
if len(R) == 0:
    print(0)
    exit()
print(score - min(R))
