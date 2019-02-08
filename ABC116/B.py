a = int(input())
A = [a]
for i in range(2, 1000000):
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
    if a in A:
        print(i)
        break
    A.append(a)
