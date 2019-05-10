N = int(input())
A = list(map(int, input().split()))
R = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
for i, _ in R:
    print(i + 1)
