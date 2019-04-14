n = int(input())
A = list(map(int, input().split()))
s = 0
num = 0
sign = "+"
for a in A:
    s += a
    if sign == "+":
        if s > 0:
            pass
        else:
            num += abs(s) + 1
            s = 1
        sign = "-"
        continue
    if sign == "-":
        if s < 0:
            pass
        else:
            num += s + 1
            s = -1
        sign = "+"
        continue
s = 0
num2 = 0
sign = "-"
for a in A:
    s += a
    if sign == "+":
        if s > 0:
            pass
        else:
            num2 += abs(s) + 1
            s = 1
        sign = "-"
        continue
    if sign == "-":
        if s < 0:
            pass
        else:
            num2 += s + 1
            s = -1
        sign = "+"
        continue
print(min(num, num2))
