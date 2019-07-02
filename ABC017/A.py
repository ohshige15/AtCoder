score = 0
for _ in range(3):
    s, e = map(int, input().split())
    score += s * 0.1 * e
print(int(score))
