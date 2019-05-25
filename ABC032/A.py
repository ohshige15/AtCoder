from fractions import gcd
a = int(input())
b = int(input())
n = int(input())
x = int(a * b / gcd(a, b))
t = x
while t < n:
    t += x
print(t)
