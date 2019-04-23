x1, y1, x2, y2 = map(int, input().split())
x = abs(x2 - x1)
y = abs(y2 - y1)
for _ in range(y):
    print("U", end="")
for _ in range(x):
    print("R", end="")
for _ in range(y):
    print("D", end="")
for _ in range(x):
    print("L", end="")
print("L", end="")
for _ in range(y + 1):
    print("U", end="")
for _ in range(x + 1):
    print("R", end="")
print("D", end="")
print("R", end="")
for _ in range(y + 1):
    print("D", end="")
for _ in range(x + 1):
    print("L", end="")
print("U")
