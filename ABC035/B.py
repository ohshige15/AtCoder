from collections import Counter
S = Counter(list(input()))
T = int(input())
L = S["L"] if "L" in S else 0
R = S["R"] if "R" in S else 0
U = S["U"] if "U" in S else 0
D = S["D"] if "D" in S else 0
C = S["?"] if "?" in S else 0
x = abs(L - R)
y = abs(U - D)
if T == 1:
    print(x + y + C)
else:
    if x + y >= C:
        print(x + y - C)
    else:
        print((C - x - y) % 2)
