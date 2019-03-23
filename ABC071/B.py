import string
S = sorted(list(set(input())))
for i, x in enumerate(string.ascii_lowercase):
    if len(S) <= i or S[i] != x:
        print(x)
        exit()
print("None")
