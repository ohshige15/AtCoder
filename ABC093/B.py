A, B, K = map(int, input().split())
L = []
for a in range(A, min(A + K, B + 1)):
    L.append(a)
for b in range(max(B - K + 1, A + 1), B + 1):
    if b not in L:
        L.append(b)
for l in L:
    print(l)
