N = int(input())
S = input()
if S[0] == "E":
    e = 0
    w = S.count("E") - 1
    before = "E"
else:
    e = 0
    w = S.count("E")
    before = "W"
now = w
for s in S[1:]:
    if s == "E":
        w -= 1
    if before == "W":
        e += 1
    before = s
    now = min(e + w, now)
print(now)
