S = input()
if S[0] != "A":
    print("WA")
    exit()
if S[2:-1].count("C") != 1:
    print("WA")
    exit()
c = S[2:-1].index("C") + 2
for i, s in enumerate(S):
    if i == 0 or i == c:
        continue
    if s.isupper():
        print("WA")
        exit()
print("AC")
