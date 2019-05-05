S = {x: input() for x in ("a", "b", "c")}
now = "a"
while True:
    T = S[now]
    if len(T) == 0:
        print(now.upper())
        exit()
    S[now] = T[1:]
    now = T[0]
