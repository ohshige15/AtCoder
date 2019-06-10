L = list(map(int, input().split()))
if L[0] == L[1]:
    print(L[2])
elif L[1] == L[2]:
    print(L[0])
else:
    print(L[1])
