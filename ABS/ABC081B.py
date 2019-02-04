n = int(input())
a_list = map(int, input().split())
num = 0
while True:
    a_list = [a / 2 for a in a_list if a % 2 == 0]
    if len(a_list) != n:
        break
    num += 1
print(num)
