from itertools import combinations
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
for p, q in combinations([a, b, c, d, e], 2):
    if abs(p - q) > k:
        print(":(")
        exit()
print("Yay!")
