N = int(input()) % 60
X = ["1", "2", "3", "4", "5", "6"]
for i in range(N):
    n = i % 5
    X[n], X[n + 1] = X[n + 1], X[n]
print("".join(X))
