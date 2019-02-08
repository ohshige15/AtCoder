input()
L = list(map(int, input().split()))
m = max(L)
if sum(L) - m > m:
    print("Yes")
else:
    print("No")
