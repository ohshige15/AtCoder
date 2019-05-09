N, K = map(int, input().split())
D = list(input().split())
while not all([n not in D for n in str(N)]):
    N += 1
print(N)
