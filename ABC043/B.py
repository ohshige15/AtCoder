s = input()
r = ""
for t in s:
    if t == "B":
        if len(r) != 0:
            r = r[:-1]
    else:
        r += t
print(r)
