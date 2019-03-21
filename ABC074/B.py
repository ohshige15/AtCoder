N = int(input())
K = int(input())
X = list(map(int, input().split()))
print(sum([min(abs(x), abs(K - x)) * 2 for x in X]))
