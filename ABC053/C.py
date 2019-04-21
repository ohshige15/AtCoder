x = int(input())
num = x // 11
x = x % 11
if x == 0:
    print(num * 2)
elif x <= 6:
    print(num * 2 + 1)
else:
    print(num * 2 + 2)
