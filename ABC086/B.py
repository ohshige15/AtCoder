import math
a, b = input().split()
x = int(a + b)
sqrt_x = int(math.sqrt(x))
if sqrt_x ** 2 == x:
    print("Yes")
else:
    print("No")
