A, B = map(int, input().split())
S = input()
for a in range(A):
    if S[a] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print("No")
        exit()
if S[A] != "-":
    print("No")
    exit()
for b in range(B):
    if S[A + 1 + b] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print("No")
        exit()
print("Yes")
