A, B, C = sorted(map(int, input().split()))
num = 0
if (C - A) % 2 == 0:
    num += (C - A) // 2
    if (C - B) % 2 == 0:
        num += (C - B) // 2
    else:
        num += (C - B) // 2
        num += 2
else:
    num += (C - A) // 2
    if (C - B) % 2 == 0:
        num += (C - B) // 2
        num += 2
    else:
        num += (C - B) // 2
        num += 1
print(num)
