N = int(input())
A = list(map(int, input().split()))
count = 0
for a in A:
    i = 0
    while a % 2 == 0 and a > 1:
        a //= 2
        i += 1
    count += i
print(count)
