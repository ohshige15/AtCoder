S = input()
num = 0
now = S[0]
for s in S:
    if s == now:
        continue
    if now == "B":
        now = "W"
    else:
        now = "B"
    num += 1
print(num)
