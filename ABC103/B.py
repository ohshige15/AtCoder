S = input()
T = input()
for i in range(len(S)):
    if S == T:
        print("Yes")
        exit()
    S = S[-1] + S[:-1]
print("No")
