N = int(input())
P = [int(input()) for _ in range(N)]
print(sum(P) - int(max(P) / 2))
