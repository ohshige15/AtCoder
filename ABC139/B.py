A, B = map(int, input().split())
t = 0
num = 1
while num < B:
    num -= 1
    num += A
    t += 1
print(t)
