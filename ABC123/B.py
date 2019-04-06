L = sorted([int(input()) for _ in range(5)], key=lambda x: - x % 10)
t = L[0]
for l in L[1:]:
    if t % 10 != 0:
        t += (10 - t % 10)
    t += l
print(t)
