K, S = map(int, input().split())
num = 0
for X in range(K + 1):
    for Y in range(min(K, S - X) + 1):
        Z = S - X - Y
        if Z < 0:
            break
        if K < Z:
            continue
        num += 1
print(num)
