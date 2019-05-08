A, B, C = map(int, input().split())
if A == B == 5 and C == 7 or \
   B == C == 5 and A == 7 or \
   C == A == 5 and B == 7:
    print("YES")
else:
    print("NO")
