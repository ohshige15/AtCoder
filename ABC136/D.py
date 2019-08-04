S = input()
A = []
t = 0
n, m = 1, 0
now = "R"
for i in range(1, len(S)):
    s = S[i]
    if now == "R":
        if s == "R":
            t = i
            n += 1
        else:
            m += 1
            now = "L"
    else:
        if s == "L":
            m += 1
        else:
            A.append((t, n, m))
            t = i
            n = 1
            m = 0
            now = "R"
else:
    A.append((t, n, m))
B = []
for t, n, m in A:
    for _ in range(n - 1):
        B.append("0")
    if abs(n - m) % 2 == 0:
        b = (n + m) // 2
        B.append(str(b))
        B.append(str(b))
    elif n > m:
        b = (n + m) // 2
        if n % 2 == 0:
            B.append(str(b))
            B.append(str(b + 1))
        else:
            B.append(str(b + 1))
            B.append(str(b))
    else:
        b = (n + m) // 2
        if m % 2 == 0:
            B.append(str(b + 1))
            B.append(str(b))
        else:
            B.append(str(b))
            B.append(str(b + 1))
    for _ in range(m - 1):
        B.append("0")
print(" ".join(B))
