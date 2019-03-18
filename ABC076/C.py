S = input()
T = input()
if len(S) < len(T):
    print("UNRESTORABLE")
    exit()
for i in range(len(S) - len(T), -1, -1):
    for s, t in zip(S[i:i+len(T)], T):
        if s != "?" and s != t:
            break
    else:
        S = list(S)
        S[i:i+len(T)] = list(T)
        S = "".join(S).replace("?", "a")
        print(S)
        exit()
print("UNRESTORABLE")
