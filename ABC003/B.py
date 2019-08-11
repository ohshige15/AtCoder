S = input()
T = input()
for s, t in zip(S, T):
    if s == t:
        continue
    if s != "@" and t != "@":
        print("You will lose")
        exit()
    if s == "@" and t in "atcoder":
        continue
    if t == "@" and s in "atcoder":
        continue
    print("You will lose")
    exit()
print("You can win")
