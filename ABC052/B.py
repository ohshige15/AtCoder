N = int(input())
S = input()
x = 0
n = 0
for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    n = max(n, x)
print(n)
