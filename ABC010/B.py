N = int(input())
num = 0
for a in map(int, input().split()):
    for i in range(10):
        if a % 2 == 0 or a % 3 == 2:
            a -= 1
            num += 1
        else:
            break
print(num)
