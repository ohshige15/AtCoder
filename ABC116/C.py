input()
H = list(map(int, input().split()))
count = 0
while any([h != 0 for h in H]):
    n = 0
    prev = 0
    for h in H:
        if prev == 0 and h != 0:
            n += 1
        prev = h
    count += n
    H = list(map(lambda x: x if x == 0 else x - 1, H))
print(count)
