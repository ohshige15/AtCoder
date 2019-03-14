N = int(input())
A = list(map(int, input().split()))
num = 0
while all([a % 2 == 0 for a in A]):
    num += 1
    A = [a // 2 for a in A]
print(num)
