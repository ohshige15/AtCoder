a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
x = int(input())
num = 0
for a in range(0, a_500 + 1):
    for b in range(0, b_100 + 1):
        for c in range(0, c_50 + 1):
            if a * 500 + b * 100 + c * 50 == x:
                num += 1
print(num)
