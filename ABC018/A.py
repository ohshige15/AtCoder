A = int(input())
B = int(input())
C = int(input())
R = sorted([A, B, C], reverse=True)
print(R.index(A) + 1)
print(R.index(B) + 1)
print(R.index(C) + 1)
