A1, A2, B1, B2 = map(int, input().split())
if A1 <= B1 <= A2 <= B2:
    print(A2 - B1)
elif B1 <= A1 <= B2 <= A2:
    print(B2 - A1)
elif A1 <= B1 <= B2 <= A2:
    print(B2 - B1)
elif B1 <= A1 <= A2 <= B2:
    print(A2 - A1)
else:
    print(0)
