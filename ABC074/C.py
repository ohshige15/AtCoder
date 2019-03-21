w1, w2, s1, s2, s_max, b_max = map(int, input().split())
waters = [0]
waters_base = [0]
while len(waters_base) > 0:
    base = waters_base.pop()
    water1 = base + 100 * w1
    water2 = base + 100 * w2
    if water1 not in waters and water1 <= b_max:
        waters.append(water1)
        waters_base.append(water1)
    if water2 not in waters and water2 <= b_max:
        waters.append(water2)
        waters_base.append(water2)
waters.pop(0)
sugars = [0]
sugars_base = [0]
while len(sugars_base) > 0:
    base = sugars_base.pop()
    sugar1 = base + s1
    sugar2 = base + s2
    if sugar1 not in sugars and sugar1 <= b_max:
        sugars.append(sugar1)
        sugars_base.append(sugar1)
    if sugar2 not in sugars and sugar2 <= b_max:
        sugars.append(sugar2)
        sugars_base.append(sugar2)
max_radio = -1
result = (-1, -1)
for water in waters:
    for sugar in sugars:
        if b_max < water + sugar:
            continue
        if water // 100 * s_max < sugar:
            continue
        ratio = sugar / (water + sugar)
        if max_radio < ratio:
            max_radio = ratio
            result = (water + sugar, sugar)
print(*result)
