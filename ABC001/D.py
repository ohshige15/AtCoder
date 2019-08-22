N = int(input())
T = sorted([input() for _ in range(N)])
X = []
for t in T:
    s, e = t.split("-")
    s1 = s[:2]
    s2 = s[2:]
    if int(s2[1]) in range(1, 5):
        s2 = s2[0] + "0"
    elif int(s2[1]) in range(6, 10):
        s2 = s2[0] + "5"
    e1 = e[:2]
    e2 = e[2:]
    if int(e2[1]) in range(1, 5):
        e2 = e2[0] + "5"
    elif int(e2[1]) in range(6, 10):
        if e2[0] != "5":
            e2 = str(int(e2[0]) + 1) + "0"
        else:
            e1 = "{0:02d}".format(int(e1) + 1)
            e2 = "00"
    s, e = s1 + s2, e1 + e2
    if len(X) > 0:
        if X[-1][1] < s:
            X.append([s, e])
        else:
            X[-1][1] = max(X[-1][1], e)
    else:
        X.append([s, e])
for s, e in X:
    print("{}-{}".format(s, e))
