S = input()
T = input()
st = {}
ts = {}
for s, t in zip(S, T):
    if s in st and st[s] != t:
        print("No")
        exit()
    if t in ts and ts[t] != s:
        print("No")
        exit()
    st[s] = t
    ts[t] = s
print("Yes")
